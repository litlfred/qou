# Hidden-fitting / verification-gap audit — mass & binding pipeline walkthrough

**Date:** 2026-06-04
**Branch:** `claude/homflypt-n3-implementation-2026-06-04`
**Trigger:** Owner — *"why is ' but its docstring admits this' buried in
docstring and not audit doc. can we walkthrough each script/function call
used in mass or binding and see if similar issues that need to be fixed.
this is a hidden fitting."*

## 0. Why this doc exists (the buried-admission complaint)

The HOMFLYPT `n≥3` SU(2) path in
[`homflypt_engine.py`](../../computations/homflypt_engine.py)
carries, **inside a source-code comment**, the admission that its output is
correct only up to an overall normalisation:

> *"For optimization consumers (Gram matrix, LP cost vectors, binding), the
> RATIOS between tr_M values are what matter, and these are exact. The
> absolute normalisation to match published Jones polynomial tables requires
> an additional factor … which is convention-dependent and cancels in
> ratios."* — `_homflypt_nstrand_numerical`, lines 648–657.

That is a **material limitation of a production compute path** documented
where no reviewer, audit sweep, or `grep docs/audits/` will ever find it.
Per AGENTS.md *"Before declaring 'open' … run the corpus-grep checklist"* and
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

[`homflypt_su_n_mass_tower.py`](../../computations/homflypt_su_n_mass_tower.py)
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

> **On the implied-E₀ back-solve (owner Q, 2026-06-04: "E₀ is knot
> dependent?").** No — in a correct derivation `E₀ = m_e/(q₀(q₀−1)) ≈ 4.186
> MeV` is a **single universal constant**, the same for every knot/channel.
> The mass-tower computes `E₀_implied = Q_β/|ΔP|` *separately per channel N*
> and gets a *different* value each time, none equal to 4.186 (the print
> string even says "vs canonical E₀ ≈ 4.186 MeV"). A calibration that comes
> out knot/channel-dependent is the **signature of a fit**: one free constant
> absorbing the mismatch, exactly the pathology the 3-calibration discipline
> forbids (cf. the per-partition Δ_λ gate in AGENTS.md). If `|ΔP|` were the
> right structural quantity, `Q_β/|ΔP|` would yield the *same* E₀ in every
> channel.

## 2e. The DEEPER root cause (added 2026-06-04): a degenerate evaluation point

Building the reference-QA module (§4.1, now
[`homflypt_reference_qa.py`](../../computations/homflypt_reference_qa.py))
surfaced a root cause **deeper than ratio-only normalisation**: the engine's
SU(N) specialisation exponent was wrong, putting the SU(2) evaluation at a
**degenerate point**.

- The engine set `v = q^{(N-1)/2}`. For N=2 that is `v = q^{1/2}`, and then
  `1/v − v = q^{-1/2} − q^{1/2} = −z`, so the loop value
  `δ = (1/v − v)/z ≡ −1` **identically, for every q**.
- `δ = −1` is the **degenerate Jones point** (`t` a 6th root of unity) where
  every link invariant collapses to `±1`. This is *why* distinct knots
  returned the same value (trefoil = figure-8 = ±1) — not a bug in any single
  formula, but the **evaluation point carrying no knot information**.
- The correct SU(N) HOMFLY point is `a = s^N` with `s = q^{1/2}`, i.e.
  `v = q^{N/2}`, giving `δ = −[N]_s` (non-degenerate). **Fixed** in
  `homflypt_at_su_n` (exponent `N/2`); the fix makes trefoil (2.564) and
  figure-8 (1.595) distinct again.

### Consequence for the SU(2) mass tower

The entire `homflypt_su_n_mass_tower` SU(2) channel was evaluating the knot
invariant at `δ=−1`. Its proton/neutron "ratios" and "mirror differences" at
N=2 were therefore either trivially `±1` or pure normalisation noise — **not
physical knot data**. The exponent fix is necessary but **not sufficient**:

### Residual: absolute normalisation is broken AND inconsistent across paths

Even after the exponent fix, `homflypt_reference_qa.py` reports **0/5** against
the skein reference, because the engine's paths disagree with each other *and*
with the reference:

| knot (at corrected v=q^{N/2}) | skein reference | engine n=2 path | engine n≥3 path |
|---|---|---|---|
| unknot | 1.000 | 1.000 ✓ | 1.981 |
| Hopf | −2.352 | −2.113 | 2.789 |
| trefoil | 0.960 | 0.878 | 2.564 |

- The **n=2 path** (`_homflypt_2strand_numerical`) uses the Ocneanu trace with
  the **Hecke** loop convention `z_Hecke = q − q⁻¹` (Hopf `= δq + (q−1)`),
  so its `z` ≠ the `z = q^{1/2} − q^{-1/2}` passed by `homflypt_at_su_n`.
- The **n≥3 path** uses the ratio-only `δ^{n-1}·tr_M(β)/tr_M(id)`, whose
  `δ^{n-1}` is the *n-component-unlink* norm — wrong for a 1-component knot
  closure, and the writhe framing is dropped entirely.

So the engine has **inconsistent variable conventions across its own code
paths**, none of which equals a clean external HOMFLY. Restoring a single
correct normalisation requires reverse-engineering this engine's specific
`y_λ`/`χ` Ocneanu-trace convention; that is **left as an open item** (the
reference-QA module is the gate). This audit does **not** claim the engine
now produces correct absolute invariants — only that the degeneracy is fixed
and the gate exists.

## 3. Full mass/binding pipeline walkthrough — per-function verdicts

Legend: ✅ **VERIFIED** (checked against an external reference value) ·
🟡 **CONSISTENCY-ONLY** (agreement, no external anchor) ·
🔴 **HIDDEN-FITTING / RATIO-ONLY** · ⚪ **HEURISTIC INPUT (labelled)**.

| # | Function / script | Role | Verdict | Note |
|---|---|---|---|---|
| 1 | `homflypt_engine._homflypt_nstrand_numerical` (SU(2)) | n≥3 invariant | 🔴 | Ratio-only; writhe framing dropped; admission was buried (§2). **Exponent degeneracy fixed (§2e); absolute norm still OPEN** (0/5 vs reference). |
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

## 4. Recommended fixes (priority order) — status this PR

1. ✅ **DONE — reference-value QA module**
   [`homflypt_reference_qa.py`](../../computations/homflypt_reference_qa.py):
   skein-relation reference (self-tested symbolically against textbook Hopf +
   trefoil) for the 2-strand torus family, applied to the n≥3 path via Markov
   stabilisation. Reports **0/5** against the engine today — the verification
   gap (row 4/8) is now a real, failing gate.
2. 🟡 **PARTIAL — `homflypt_at_su_n` exponent fix.** The degenerate point
   `δ≡−1` (root cause, §2e) is **fixed** (`v = q^{N/2}`; distinct knots now
   distinct). The **absolute normalisation remains OPEN**: the engine's n=2
   and n≥3 paths use inconsistent `z` conventions and neither matches the
   skein reference (§2e table). Closing it requires reverse-engineering this
   engine's `y_λ`/`χ` Ocneanu-trace convention — tracked by the failing
   reference-QA gate. The buried docstring admission is replaced with an
   explicit "ABSOLUTE-NORMALISATION OPEN" warning pointing here.
3. ✅ **DONE — mass-tower demoted.** `homflypt_su_n_mass_tower.py` now opens
   with an EXPLORATORY banner; the `E0_implied = Q_β/|ΔP|` block is relabelled
   a **back-solve / fit diagnostic**, not a prediction.
4. ⬜ **TODO (follow-up) — reference χ^λ test** for a small partition with a
   known closed-form (e.g. `χ^{(n)}`, `χ^{(1ⁿ)}`) added to
   `cross_check_trM_1ppb` so the shared-definition cluster (row 4/7/8) gets one
   external anchor.
5. ⬜ **TODO (separate track) — converge binding inputs (rows 9–11)** onto an
   actual SDP derivation (binding-link heuristic audit); not in scope here.

## 5. Scope of this PR

Delivered on this branch: the **surfacing + walkthrough** (this doc), the
**reference-QA gate** (§4.1, fails 0/5 by design), the **degeneracy exponent
fix** (§4.2, partial — absolute norm left open and gated), and the
**mass-tower demotion** (§4.3). The remaining absolute-normalisation work
(§4.2 residual), the `χ^λ` reference anchor (§4.4), and the binding-input SDP
convergence (§4.5) are explicit follow-ups. This PR does **not** claim the
HOMFLY engine now produces correct absolute invariants — it claims the gap is
*surfaced, gated, and de-degenerated*.

## References

- [`2026-06-03-binding-link-assignment-heuristic.md`](2026-06-03-binding-link-assignment-heuristic.md)
- [`2026-06-04-nuclear-binding-derivation-completeness-ledger.md`](2026-06-04-nuclear-binding-derivation-completeness-ledger.md)
- `homflypt_engine.py` `_homflypt_nstrand_numerical` (the buried admission)
- `cross_check_trM_1ppb.py` (the consistency-only "1 ppb" dashboard)
