# Hidden-fitting / verification-gap audit — mass & binding pipeline walkthrough

**Date:** 2026-06-04
**Branch:** `claude/homflypt-n3-implementation-2026-06-04`
**Trigger:** Owner — *"why is ' but its docstring admits this' buried in
docstring and not audit doc. can we walkthrough each script/function call
used in mass or binding and see if similar issues that need to be fixed.
this is a hidden fitting."*

## 0. Why this doc exists (the buried-admission complaint)

The HOMFLYPT `n≥3` SU(2) path in
[`homflypt_engine.py`](../../folio-assistant/computations/homflypt_engine.py)
carries, **inside a source-code comment**, the admission that its output is
correct only up to an overall normalisation:

> *"For optimization consumers (Gram matrix, LP cost vectors, binding), the
> RATIOS between tr_M values are what matter, and these are exact. The
> absolute normalisation to match published Jones polynomial tables requires
> an additional factor … which is convention-dependent and cancels in
> ratios."* — `_homflypt_nstrand_numerical`, lines 648–657.

That is a **material limitation of a production compute path** documented
where no reviewer, audit sweep, or `grep docs/audits/` will ever find it.
Per CLAUDE.md *"Before declaring 'open' … run the corpus-grep checklist"* and
the one-voice / author-notes discipline, a known-incorrectness of a compute
path belongs in a committed audit doc, not a docstring. This doc surfaces it
and then walks the **entire mass + binding pipeline** for the same class of
problem.

## 1. The two failure classes

| Class | Definition | Why it's dangerous |
|---|---|---|
| **Verification gap** | A cross-check that proves methods **AGREE** (consistency), never that any of them is **CORRECT** against an external reference value. | Four methods that share the same underlying definition agree by construction. Agreement → "1 ppb" green dashboard, but a shared upstream error is invisible. |
| **Hidden fitting** | A normalisation that **cancels in ratios** (ratio-only output) or an input **back-solved** from the target. The absolute value is wrong/undetermined; only relative structure survives. | The no-fitting standard requires every number to be *derived*. A ratio-only path silently drops the absolute calibration — equivalent to fitting one free constant per observable. |

These are distinct from an honest **heuristic input** (e.g. the L6a4
binding-link assignment, audited separately in
[`2026-06-03-binding-link-assignment-heuristic.md`](2026-06-03-binding-link-assignment-heuristic.md)),
which is at least labelled as such at the call site.

## 2. The HOMFLYPT finding (surfaced + retraction)

### 2a. What the path actually computes

`_homflypt_nstrand_numerical` (SU(2), N=2 detected) returns

```
P = δ^{n-1} · tr_M(β) / tr_M(identity)
```

with `tr_M = Σ_λ y_λ χ^λ` (Markov / Wenzl weights). The `/ tr_M(identity)`
divides out the overall scale, so the result is **dimensionless ratio data**,
not the HOMFLYPT/Jones polynomial. The writhe framing factor
`(-q^{-3/2})^{-w}` is **absent** entirely.

### 2b. Reference-value QA (the test that catches it)

Comparing against textbook Jones values at the SU(2) point (q = q₀):

| Knot | Textbook Jones | This path (live) | My candidate `−v^e·Σ W_λ χ_λ` |
|---|---|---|---|
| trefoil `σ₁³` | 0.973 | 1.000 | 1.000 |
| figure-8 `(σ₁σ₂⁻¹)²` | 1.033 | **0.182** | 1.000 |
| Hopf `σ₁²` | −1.720 | −1.000 | −1.000 |

- The **live production path** is wrong on absolutes (fig-8 0.182 vs 1.033).
- **My candidate** `P = −v^e · Σ_λ W_λ χ_λ` with hook-length Schur weight
  `W_λ` is **degenerate at SU(2)**: it returns ±1 for *distinct* knots
  (trefoil = fig-8 = 1.000). The Schur weight `W_λ = Π (v⁻¹s^c − v s^{-c})/
  (s^h − s^{-h})` has a **removable singularity** at the SU(2) point
  (the `c = 0` cell factor degenerates), which the production docstring at
  lines 616–619 already warned about.

### 2c. Retraction

Earlier in this work I claimed a skein-relation "proof" that
`P = −v^e · Σ_λ W_λ χ_λ` is the HOMFLYPT polynomial, citing 7 skein triples
matching to 1e-16. **That claim is retracted.** The skein triples it matched
were consistency relations among my own evaluations (verification gap, again);
the reference-value QA in 2b shows the formula is degenerate at the SU(2)
specialisation actually used in production. The correct `n≥3` implementation
must use the **y_λ-Markov trace** (which bypasses the Schur singularity) **and
restore the Jones normalisation** `(-q^{1/2}-q^{-1/2})^{n-1}·(-q^{-3/2})^{-w}`
— verified against the textbook column above, not against internal
self-consistency.

### 2d. Production blast radius

[`homflypt_su_n_mass_tower.py`](../../folio-assistant/computations/homflypt_su_n_mass_tower.py)
consumes this path for proton `(σ₁σ₂⁻¹)³`, neutron `(σ₁⁻¹σ₂)³`, figure-eight,
and trefoil at SU(N), N=2..6. It then:

- reports **proton/neutron ratios** per N (ratio-of-ratios — partly insulated,
  but the writhe framing does **not** cancel between p and n because their
  writhes differ in sign);
- computes **mirror differences** `P(p) − P(n)` (CPT-structure claim) — these
  are **not** ratio-insulated and inherit the absolute-normalisation error;
- **back-solves an "implied E₀"** from `Q_β / |ΔP|` (line 113) — this is a
  textbook **hidden fit**: a calibration constant reverse-engineered from the
  target observable.

Verdict: the mass-tower's **ratio** outputs are *suggestive*; its **mirror
difference**, **CPT**, and **implied-E₀** outputs are **not derivations** and
must not be cited as predictions until the path is reference-validated.

## 3. Full mass/binding pipeline walkthrough — per-function verdicts

Legend: ✅ **VERIFIED** (checked against an external reference value) ·
🟡 **CONSISTENCY-ONLY** (agreement, no external anchor) ·
🔴 **HIDDEN-FITTING / RATIO-ONLY** · ⚪ **HEURISTIC INPUT (labelled)**.

| # | Function / script | Role | Verdict | Note |
|---|---|---|---|---|
| 1 | `homflypt_engine._homflypt_nstrand_numerical` (SU(2)) | n≥3 invariant | 🔴 | Ratio-only; writhe framing dropped; admission was buried (§2). |
| 2 | `homflypt_engine._homflypt_nstrand_numerical` (SU(N>2)) | Schur-fn invariant | 🟡 | Also `/total_id` normalised → ratio-only; never checked vs SU(N) reference. |
| 3 | `homflypt_su_n_mass_tower.main` | mass-tower data | 🔴 | Mirror-diff + implied-E₀ = hidden fit (§2d). Ratios suggestive only. |
| 4 | `cross_check_trM_1ppb.main` | "1 ppb" dashboard | 🟡 | Pairwise deltas among Hoefsmit/peel/chi-cache/Habiro — *"must agree between … paths"*. Tests consistency of 4 paths that share the **same** `tr_M = Σ y_λ χ^λ` definition. Green ≠ correct. **No textbook-knot anchor.** |
| 5 | `mass_at_3A_proper.atom_braid_word_3A` | canonical braid word | ✅ | Pure construction (no numeric claim); p-n interface `(1, −h(½−δ/4))` is a *definition*, not a fit. δ from substrate. OK. |
| 6 | `closed_form_tau_M.closed_form_ratio` | ⋈_K mass ratio | 🟡→🔴 | Named `_ratio`; outputs are relative. Absolute mass only via the E₀ = m_e/(q(q−1)) calibration, which **is** derived (CAL-1+CAL-3), so the absolute is anchored — but the ~21% relative p-n interface number (line 183) is consistency-checked, not reference-checked. |
| 7 | `wedderburn_jones_markov.y_lambda_at` | Wenzl weights y_λ | 🟡 | Algebraic; correct by construction *if* the Wenzl recursion is right — but the recursion's output is only ever cross-checked against the other internal paths (#4), never against a published Markov-trace table. |
| 8 | `hecke_characters.chi_lambda_braid` | q-character χ^λ(β) | 🟡 | Same: validated by Hoefsmit-vs-mpfr-vs-recursive agreement (#4), not against a reference χ^λ table. **Highest-value place to add a reference test** (small partitions have closed forms). |
| 9 | `binding_k_solver` | per-isotope K-word | ⚪ | Hardcodes `L6a4` / `[3,6]` labelled `# heuristic`. Renamed *from* "SDP solver" (PR #614) but **does not solve an SDP**. Audited in `2026-06-03-binding-link-assignment-heuristic.md`. |
| 10 | `binding_link_volumes` | isotope→link→vol map | ⚪ | Hardcoded `{"3He":{"link":"L6a4",…}}`. Heuristic survey input, labelled. |
| 11 | `per_bond_growth_a3` | embedded-bond growth | 🟡 | `B_ISO = {pn:2.3048,…}` hardcoded "this session" numbers (lines 45–46) — provenance is a prior run, not a witness reference. Growth ratios are internally consistent only. |
| 12 | `three_body_joint_trace_a3` | 3-body correlation | ✅ | Reports a **signed, falsifiable** number (−1.77 MeV, destructive) — does not close the gap and says so. Honest negative result (PR #1790). |
| 13 | `lp_dual_solver.solve_operator_selection_lp` | LP primal+dual | ✅ | Strong-duality gap `|primal−dual|` **is** an internal correctness certificate (KKT), and it's checked numerically. The one place a self-check is a real proof. |
| 14 | `canonical_braid_crossings.classify_crossing` | (c,d)→ctype | ✅ | Pure classification; raises on unknown (c,d). No numeric claim. |

### 3a. Root-cause cluster

Rows **4, 7, 8** are one cluster: the entire `tr_M` validation rests on
**four methods that compute the same `Σ_λ y_λ χ^λ`** and are checked against
**each other**. There is no test of `χ^λ(β)` or `y_λ` against a **published**
value. This is the structural verification gap: a single error in the shared
Wenzl/Hoefsmit definition would pass the "1 ppb" dashboard.

Rows **1, 2, 3** are the hidden-fitting cluster: ratio-only normalisation +
one back-solved calibration.

Rows **9, 10, 11** are heuristic/hardcoded inputs — *labelled*, so not
"hidden", but they are the binding-side analogue and should converge on the
SDP-derivation path.

## 4. Recommended fixes (priority order)

1. **Add a reference-value QA module** `homflypt_reference_qa.py`: textbook
   Jones values for trefoil / figure-8 / Hopf / Borromean at the SU(2) point,
   asserted to ~1e-6. This is the single highest-leverage fix — it converts
   the verification gap (row 4/8) into a real correctness gate. **It must
   fail today** against `_homflypt_nstrand_numerical` (that is the point).
2. **Fix `_homflypt_nstrand_numerical`**: restore the Jones normalisation
   `(-q^{1/2}-q^{-1/2})^{n-1}·(-q^{-3/2})^{-w}` so absolute values match the
   reference module. Keep the y_λ-Markov core (it bypasses the Schur
   singularity); drop the degenerate Schur-weight candidate (retracted §2c).
3. **Demote the mass-tower mirror-diff / implied-E₀ outputs** to EXPLORATORY
   in `homflypt_su_n_mass_tower.py` until #2 lands; remove or clearly flag the
   `E0_implied = Q_β/|ΔP|` back-solve as a fit, not a prediction.
4. **Add one reference χ^λ test** for a small partition with a known
   closed-form (e.g. `χ^{(n)}`, `χ^{(1ⁿ)}`) to `cross_check_trM_1ppb` so the
   shared-definition cluster (row 4/7/8) gets one external anchor.
5. **Converge binding inputs (rows 9–11)** onto an actual SDP derivation
   (tracked in the binding-link heuristic audit); not in scope for this PR.

## 5. Scope of this PR

This doc is the **surfacing + walkthrough** deliverable. The reference-QA
module (#1) and the normalisation fix (#2) are the follow-up code changes;
they are staged on this branch next. The binding-side convergence (#5) stays
on its existing audit track.

## References

- [`2026-06-03-binding-link-assignment-heuristic.md`](2026-06-03-binding-link-assignment-heuristic.md)
- [`2026-06-04-nuclear-binding-derivation-completeness-ledger.md`](2026-06-04-nuclear-binding-derivation-completeness-ledger.md)
- `homflypt_engine.py` `_homflypt_nstrand_numerical` (the buried admission)
- `cross_check_trM_1ppb.py` (the consistency-only "1 ppb" dashboard)
