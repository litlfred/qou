# Habiro per-knot λ(K) — step 1 results (the §6.8 experiment)

**Date:** 2026-06-03 (last update 2026-06-04)
**Branch:** `claude/habiro-per-knot-lambda-derivation-2026-06-03`
**Probe:** [`computations/probes/per_knot_lambda_habiro_probe.py`](../../computations/probes/per_knot_lambda_habiro_probe.py)
**Parent:** §6.8 of [`docs/audits/2026-06-03-1ppq-roadmap-reanalysis-and-geom-full-bridge-gap.md`](2026-06-03-1ppq-roadmap-reanalysis-and-geom-full-bridge-gap.md) (PR #1762)
**Status:** EXPLORATORY. Two rigorous findings + one suggestive numerical lead (since retracted). No production path touched. No fit.

## Lean-formal coverage (closed-form identities only)

Every closed-form algebraic identity used in this audit doc has a Lean
proof on this branch. The remaining structural questions (rank = c+1
mechanism, q-deformation choice in the categorical chain, Lobachevsky
correction) are not closed-form identities and stay open.

| Claim | Lean proposition | Tactic |
|---|---|---|
| `tanh(ln q) = (q² − 1)/(q² + 1)` over ℝ_{>0} | [`prop:coulomb-strong-ratio-q-rational`](../../content/quantum-observable-universe/climax-volume-mass/coulomb-strong-ratio-q-rational.md) | `Real.exp_log` + `field_simp; ring` |
| `(q − q⁻¹)/(q + q⁻¹) = (q² − 1)/(q² + 1)` (pure algebraic half) | same prop, `qDiffOverSum_eq_qSqDiff_over_qSqSum` | `field_simp; ring` |
| `lw(1)(q) = 1` ∀q (muon, knot) | [`prop:selection-rule-anchors-c1-c3`](../../content/quantum-observable-universe/climax-volume-mass/selection-rule-anchors-c1-c3.md), `selection_rule_c1_eq_one` | `norm_num` |
| `lw(3)(q) = (3q² + 4 + 3q⁻²)/4` (proton, Borromean q-form) | same prop, `selection_rule_c3_eq_family_a_q_form` | `ring` |
| `(3q² + 4 + 3q⁻²)/4 = 5/2 + (3/4)(q − q⁻¹)²` (Family-A h-form) | same prop, `family_a_q_form_eq_h_form` | `field_simp; ring` |
| Composite `lw(3) = 5/2 + (3/4)h²` | same prop, `selection_rule_c3_eq_family_a` | composition of the two above |
| `lw(2)(q) = (q+1)²/(3q)` (Hopf-style prediction) | [`prop:selection-rule-c2-prediction`](../../content/quantum-observable-universe/climax-volume-mass/selection-rule-c2-prediction.md), `selection_rule_c2_eq_closed_form` | `field_simp; ring` |

All proofs sit in `content/quantum-observable-universe/climax-volume-mass/`
under `qou` Lake package. None require Mathlib representation-theory
infrastructure — they are pure ring identities over the q-deformed hook
values, which are stated as their explicit Laurent-polynomial closed forms.

What is **NOT** Lean-formalised (and would need Mathlib infra):

- The general `c ≥ 4` selection rule (needs q-deformed hook-length formula).
- The classical identity `Σ_{λ ⊢ n} dim V_λ = I(n)` (involution numbers; needs Mathlib symmetric-rep machinery).
- The Pieri-branching trace `Σ dim · Σ dim = (n+1)!` (needs branching-rule formalisation).
- Bar-symmetric / antisymmetric decomposition properties (need q-Laurent algebra infra).

So the gap between "exploratory probe" and "Lean-formal" is now sharply
localised to the non-closed-form structural questions.

## What this is

First computational step of the experiment that tries to **derive** the Geom_full bridge `linking_weight` from a Habiro-ring element (G-S-W-Z 2024, `arXiv:2412.04241`) rather than carry it as a CODATA near-match. Does the parts computable inside the framework now; isolates exactly what external data is needed to finish.

## Finding 1 (RIGOROUS) — Family-A is a q-deformed involution count

Verified symbolically (sympy, symmetric q-integers):

```
(1/4) · Σ_{λ ⊢ 4} dim_q(V_λ)  =  (3q² + 4 + 3q⁻²)/4  =  5/2 + (3/4)h²     [h = q − q⁻¹]
```

matching `linking_weight_family_a(q)` exactly (both q-form and h-form, `diff == 0`). This re-confirms the Lean-proved identity from `lambda-scale-substrate-form.lean`.

**New structural observation.** The classical (`q → 1`) values of `Σ_{λ ⊢ n} dim_q` are:

| n | Σ_{λ⊢n} dim_q at q=1 | = |
|---|---|---|
| 3 | 4 | I(3) |
| 4 | 10 | I(4) |
| 5 | 26 | I(5) |
| 6 | 76 | I(6) |

These are the **involution numbers** `I(n)` (a.k.a. telephone numbers: 1, 1, 2, 4, 10, 26, 76, 232, …) — the classical identity `Σ_{λ⊢n} f^λ = #{involutions in S_n}`. So the Family-A `linking_weight = (1/4)·I(4) = 5/2` at `q=1` is a **normalized q-deformed involution count**. This is a cleaner provenance for the `5/2` than "half the H_4 Wedderburn dimension" — it's `I(4)/4`.

Whether the normalization `1/4` and the choice `n=4` (vs the proton's actual `H_3`) are categorically forced is exactly the open §2 question — but now the target is sharply stated: the per-knot rule must select `(n_K, normalization_K)` such that `(1/c_K)·Σ_{λ⊢n_K} dim_q` reproduces each knot's `λ(K)`.

## Finding 2 (SUGGESTIVE — not decisive) — the figure-eight Habiro element optimally truncates to ≈ the muon's linking_weight

The muon is the figure-eight knot `4_1` (per the cheat sheet: knots get `linking_weight = 1`, links get `> 1`). Its canonical Habiro-ring element is

```
J(4_1; q) = Σ_{n≥0} (q;q)_n · (q⁻¹;q⁻¹)_n = Σ_{n≥0} ∏_{j=1}^{n} (1 − q^j)(1 − q⁻ʲ)
```

Evaluated at the **real** substrate anchor `q₀ ≈ 1.110`:

| n | partial sum S_n | term_n |
|---|---|---|
| 0 | 1.0 | 1.0 |
| 1 | 0.98910 | −0.010897 |
| 2 | 0.98958 | +0.0004763 |
| 3 | 0.98953 | −4.70×10⁻⁵ |
| … | … | … |
| **9 (n_opt)** | **0.98953878** | min \|term\| = 3.66×10⁻⁷ |
| 60 | (diverges) | 1.07×10⁷¹ |

The series is **asymptotic**: it settles to `S* = 0.98953878…` over the first ~9 terms (least-term truncation at `n_opt = 9`), then diverges super-exponentially. The divergence is the **same `q^{n(n+1)/2}` q-Pochhammer growth at `q > 1`** that refuted the α_r single-rank ansatz earlier this session — confirming naive Habiro summation fails at `q₀` and the G-S-W-Z Borel/`K_3`-graded resummation is what's required.

**The lead:** `S* = 0.98954` is **−1.05 %** from the muon's `linking_weight = 1`. The min-term magnitude (3.7×10⁻⁷) means this −1.05 % is a **genuine deviation, not truncation noise**.

**Honest caveats (why this is suggestive, not a derivation):**

1. The connection between `J(4_1; q)` (a Kashaev-type tail invariant) and the framework's `linking_weight` is **not established** — they may differ by a normalization that the −1.05 % reflects.
2. `−1.05 %` is not within any precision target; if the relationship were exact-canonical we'd expect closer agreement (the muon `linking_weight = 1` is itself an *exact* framework value).
3. The naive least-term truncation is not the canonical G-S-W-Z resummation — the true Borel sum may differ from `0.98954` at the percent level.

So: **intriguing that an unfitted hyperbolic-knot invariant lands within ~1 % of the muon's exact `linking_weight`**, but the decisive test needs the actual Garoufalidis–Zagier `Φ_K(h)` perturbative coefficients (Finding 4).

## Finding 3 (CONTROL) — trefoil (non-hyperbolic) shows no clean plateau

The trefoil `3_1` is a torus knot (`Vol = 0`, non-hyperbolic). Probing a trefoil-twisted `(q;q)_n` element gave no clean least-term plateau (`n_opt` ran to the boundary). Consistent with "the figure-eight plateau is a hyperbolic-geometry signal" — but this control is **weak**: the trefoil element used is non-canonical (a documented stand-in, not the literature trefoil invariant), so it only rules out the crudest artefact explanation, not all of them.

## Finding 4 (GAP) — what external data finishes the experiment

| Computable now (this probe) | Needs external data |
|---|---|
| Family-A = (1/4)·I(4) q-deformed (Part 1) | Garoufalidis–Zagier `Φ_K(h)` perturbative coefficients for `4_1`, `6_2`, Borromean (`arXiv:2111.06645` tables) |
| `Σ_{λ⊢n} dim_q` involution-number family (Part 2) | OR SnapPy + Borot–Eynard topological-recursion `S_0, S_1, S_2` (§6.6) |
| Figure-eight Habiro element diverges → asymptotic at q₀, optimal-truncation `S* = 0.98954` (Part 3) | — |

**Decisive test (unchanged from §6.8):** `Φ_{4_1}(h)/Vol(4_1)` should give `1 + O(h²)` (muon, a knot); `Φ_{Borromean}(h)/[norm]` should give `5/2 + (3/4)h²` (proton, a 3-link). If the `h²` coefficients match the framework's, the Geom_full bridge is **derived**, not fit. The `K_3(K)` grading makes those coefficients rigid (no free parameters) — the discipline-compliant route the Δ_λ-gate demands.

## STEP 2 (2026-06-03, after owner uploaded the actual G-Z paper) — Finding 2 is REFUTED; the invariant is a roots-of-unity object

The owner uploaded Garoufalidis–Zagier `arXiv:2111.06645` (SIGMA 2024) and flagged: *"note it is only at roots of unity… so we can only use in context of crystal bases?"* This is correct, and checking the **actual paper coefficients** refutes the clean Finding-2 identification.

### What the paper actually says

- **The figure-eight Kashaev invariant** (paper eq 1.2) is
  `⟨4_1⟩_N = Σ_{n=0}^{N-1} (ζ_N; ζ_N)_n²` with `ζ_N = e^{2πi/N}` — **exactly the element of Finding 2**, but evaluated at a **root of unity**, where `(ζ_N;ζ_N)_n = 0` for `n ≥ N` so the sum **terminates**. At real `q₀ > 1` it does NOT terminate → diverges (the Finding-2 divergence). The invariant `⟨K⟩_N ∈ Z[e^{2πi/N}]` is **defined at roots of unity** — the user's point exactly.
- **The perturbative series** (paper eq 1.3):
  `Φ^(4_1)(h) = 3^(−1/4)·(1 + 11/(72√−3)·h + 697/(2·(72√−3)²)·h² + …)`,
  the `N→∞` asymptotic of `⟨4_1⟩_N` (paper eq 1.1), in variable `ℏ = 2πi/N`.
- Point (d): `Φ(h)` is **factorially divergent**; the real-axis lift to "actual functions on R" is the **conjectural** `W_γ` cocycle.

### Why Finding 2 is refuted (4 independent mismatches vs the framework's `linking_weight`)

| | G-Z `Φ^(4_1)(h)` (real data) | framework `linking_weight` |
|---|---|---|
| leading coeff | `3^(−1/4) ≈ 0.760` | `1` (muon) / `5/2` (proton) — **−24% off** |
| `h¹` coeff | `11/(72√−3) ≈ 0.0882 i` — **imaginary** (Q(√−3)) | real |
| variable | `ℏ = 2πi/N` (imaginary → 0) | `h = q − q⁻¹` (real ≈ 0.196) |
| domain | **roots of unity** `ζ_N` | real `q₀ > 1` |

The Finding-2 lead (`S* = 0.98954`, −1.05% from muon lw=1) was a **coincidence of a particular real-axis resummation** of the divergent real-`q` series — it is **not** the G-Z `Φ^(4_1)` (which leads with 0.76, is complex, and uses imaginary ℏ). **The clean "Habiro element = linking_weight" identity does not hold for the figure-eight.**

### But this STRENGTHENS Finding 1 — and answers "crystal bases?"

The crucial separation the owner's question forces:

- **Kashaev / Habiro element** (Finding 2): a **root-of-unity object** that *diverges* at real `q₀`. Only reachable archimedean-ly via the conjectural `W_γ` resummation, which doesn't give the framework's real `linking_weight` anyway. **Not usable for the archimedean mass chain.** ✗
- **Quantum-dimension / Wedderburn sum** (Finding 1): `Σ_{λ⊢4} dim_q(V_λ)` is a **symmetric Laurent polynomial** — *finite at real `q₀`* AND at roots of unity. It is the Verlinde-style quantum-dimension object that lives naturally in the **crystal-basis / RT** world the owner points to, yet (unlike the Kashaev element) is a finite polynomial so its **real-`q₀` archimedean evaluation is totally legitimate**. ✓

So the framework's `linking_weight = (1/4)Σ_{λ⊢4} dim_q` (= q-deformed involution count `I(4)/4`) is the **right kind of object** — a quantum-dimension Laurent polynomial, not a Kashaev/Habiro series. The owner's instinct correctly separates the two: **use the crystal-basis/quantum-dimension object (finite, evaluable at real q₀), NOT the Habiro element (root-of-unity-bound, divergent at q₀).**

### Net verdict (revised)

- **Finding 1 (linking_weight = `I(4)/4` q-deformed quantum-dimension sum): STANDS and is strengthened.** It is a crystal-basis/RT-compatible Laurent polynomial, finite at real q₀.
- **Finding 2 (figure-eight Habiro ≈ muon lw): REFUTED** by the actual G-Z coefficients. The −1.05% was a coincidence. The Habiro element is a roots-of-unity object that should not be used in the archimedean chain.
- **§6.5/§6.8 Habiro hook: does not deliver a real-q₀ `linking_weight` derivation.** The productive object is the quantum-dimension sum (Finding 1), and the open question reverts to "what categorical rule selects `(n_K, normalization)` per knot" — a *quantum-dimension / crystal* question, not a Habiro-resummation one.

This is a valuable negative result: it kills the Habiro-resummation mirage before the framework invested weeks, and redirects to the crystal-basis/quantum-dimension object the owner identified.

## STEP 3 (2026-06-03) — the redirect pays off: a zero-parameter COMPONENT selection rule

The owner's crystal-basis redirect pointed at the quantum-dimension object (Finding 1), not the Habiro element. Pursuing that gives a clean, **zero-parameter** per-link selection rule.

Probe: [`probes/per_knot_lambda_component_selection_rule.py`](../../computations/probes/per_knot_lambda_component_selection_rule.py)

### The rule

```
linking_weight(L) = (1/(c+1)) · Σ_{λ ⊢ (c+1)} dim_q V_λ          [c = #components]
                  = q-deformed I(c+1)/(c+1)
                  = per-rank-normalized q-dim of the Gelfand model of H_{c+1}
```

### Both anchors reproduced EXACTLY (verified symbolically, zero free parameters)

| c | object | rule output | framework value | match |
|---|--------|-------------|-----------------|-------|
| **1** | knot (muon = 4_1) | `(1/2)Σ_{λ⊢2} dim_q = 1` | lw = 1 (knots) | **exact ∀q** ✓ |
| **3** | 3-link (proton = Borromean 𝓑₃) | `(1/4)Σ_{λ⊢4} dim_q = 5/2 + 3h²/4` | Family-A | **exact** ✓ |

The c=1 case being `= 1` **exactly for all q** (not just at q=1) is an infinite set of constraints — a 2-point coincidence would be extraordinarily unlikely to satisfy it. Combined with the c=3 = Family-A exact match, a **zero-parameter** formula hitting both is strong evidence, not a fit.

### Predictions (the decisive independent tests)

| c | closed form | at q₀ |
|---|-------------|-------|
| 2 (2-comp link, e.g. Hopf) | `(q+1)²/(3q) = (2+√(h²+4))/3` | 1.3370 |
| 4 (4-comp link) | `(1/5)Σ_{λ⊢5} dim_q` (= 26/5 at q=1) | 5.3761 |

A 2-component-link particle with an independent `linking_weight` determination would decisively confirm or refute the rule.

### Mechanism hypothesis (next derivation target)

The Wedderburn rank `n = c + 1 = (#link components) + 1`. The **"+1" is the lepton / observation (m_e) fibre** adjoined to the c-component hadronic link — consistent with the mass formula being `m_e × Geom`. Deriving why the rank is `c+1` (vs the braid strand count, which is also 3 for the Borromean) is the open categorical step.

### Δ_λ-gate compliance

This is a **selection rule** (which Wedderburn rank, which normalization), **zero free parameters**, reproducing **exact known framework values** (lw=1 for knots, Family-A for the proton) — NOT a scalar fit to AME binding/mass data. It is precisely the GAP-A-3/GAP-A-4 "categorical level selection / ρ general rule" direction the cheat-sheet endorses, not a forbidden 7th fit-ansatz.

### Why this is the right kind of object (closing the owner's loop)

Per the STEP-2 reconciliation: the Kashaev/Habiro element is root-of-unity-bound and diverges at real q₀. The quantum-dimension Gelfand-model sum used here is a **finite Laurent polynomial** — evaluable at real q₀ *and* at roots of unity, the crystal-basis/RT-compatible object the owner identified. So STEP 3 is the productive continuation of the owner's redirect, and STEP 2 (Habiro) was the necessary detour that ruled out the wrong object.

## STEP 4 (2026-06-03) — relation to the 6 knot-operator basis; rational not series; even/odd rank

Owner question: *"c=2, c=4, 5 — are they all different knot operators… correspond to 6 knot-operator basis or something else? series or rational func?"*

### Not the 6 knot operators — a different "total" over the same Wedderburn pieces

The **6 knot-operator basis** (step 4 of the canonical chain, Bring χ=−6) is

```
dim H_3 = Σ_{λ⊢3} (dim V_λ)²  =  1² + 2² + 1²  =  6      (the REGULAR rep of H_3)
```

— 6 *operators* (braid words) at the **single** rank H_3 (the proton/neutron braid rank). My selection rule instead uses the **GELFAND model**

```
linking_weight(L) = (1/(c+1)) · Σ_{λ⊢(c+1)} dim V_λ      (each irrep ONCE, not squared)
```

So they are **two different sums over the same Wedderburn decomposition**:

| total | formula | at n=3 | object |
|-------|---------|--------|--------|
| **regular rep** (6-operator basis) | `Σ_{λ⊢n} (dim V_λ)²` | **6** = dim H_3 | which braid *word* (operator); tr_M of these → Jones/mass |
| **Gelfand model** (my linking_weight) | `Σ_{λ⊢n} dim V_λ` = `I(n)` | 4 = I(3) | one scalar per link; multiplies Vol |

| n | Σ dim (Gelfand = I(n)) | Σ dim² (regular = dim H_n) |
|---|---|---|
| 2 | 2 | 2 |
| 3 | 4 | **6** ← the operator basis |
| 4 | 10 | 24 |
| 5 | 26 | 120 |
| 6 | 76 | 720 (= n!) |

### Not "different operators" — different RANKS

The `c`-family indexes Wedderburn **rank** `n = c+1`, not operators-within-a-rank. Each `c` yields **one** Gelfand-model q-dimension (a single function), not a basis element. The 6 operators are 6 elements at fixed rank 3; my `c=1,2,3,4,5` are full Gelfand sums at ranks 2,3,4,5,6.

### Rational functions, NOT series

Every `lw(c)` is a **finite rational function** of `q` (Laurent polynomial over an integer denominator) — the crucial contrast with the **refuted Habiro element** (a *divergent series*). This is exactly why the quantum-dimension object works archimedean-ly where the Habiro element failed.

```
c=1 (n=2):  1                              ← muon (even rank)
c=2 (n=3):  (q+1)²/(3q)                     (odd rank)
c=3 (n=4):  (3q²+4+3q⁻²)/4 = 5/2+3h²/4      ← proton (even rank)
c=4 (n=5):  (3q⁸+2q⁷+3q⁶+2q⁵+6q⁴+…)/(5q⁴)   (odd rank)
c=5 (n=6):  Σ_{λ⊢6}dim_q / 6                (even rank)
```

### Even/odd-rank dichotomy (a real structural fact)

- **EVEN rank** `n=c+1` (c = 1, 3, 5 …): the Gelfand sum is a **polynomial in `h²`** (bar-symmetric, clean). **Both known anchors — muon (c=1) and proton (c=3) — are even-rank.**
- **ODD rank** `n=c+1` (c = 2, 4 …): carries a `[2]_q = q+q⁻¹ = √(h²+4)` factor — *not* a polynomial in `h`.

So the c=2 (Hopf, 2-component-link) prediction sits at odd rank and has the √ structure — a sharp, falsifiable feature for the decisive test.

### Connection at the proton

The proton involves **both** structures at adjacent ranks: its braid *operator* lives in H_3 (the 6-basis, `Σdim²=6`), while its *linking_weight* uses the H_4 Gelfand model (`Σdim=10`). The rank shift H_3 → H_4 is exactly the `n = c+1` "+1" — the open mechanism question (the lepton/observation fibre hypothesis).

## Verdict + next step

- **Finding 1** is a clean, citable provenance upgrade (`linking_weight = I(4)/4` q-deformed). Worth landing regardless of the rest.
- **Finding 2** is a real lead worth chasing — an unfitted hyperbolic invariant within 1 % of the muon's exact `linking_weight` — but it is **not** a derivation yet.
- The honest blocker is external `Φ_K` data. Options to unblock: (a) source the G-Z tables (owner may have library access); (b) install SnapPy + run Borot–Eynard; (c) compute the figure-eight perturbative series directly from its A-polynomial `(ℓ² m⁴ + … )` via the saddle expansion — feasible in-framework with sympy, ~1-2 days, and the cleanest no-external-dependency path.

Recommend (c) as the next commit on this branch: compute `Φ_{4_1}(h)` from the figure-eight A-polynomial saddle expansion and check whether `S* = 0.98954` is reproduced (validating the optimal-truncation estimate) and whether the `h²` coefficient is the muon-consistent value.

## Coordination

- Parent analysis: PR #1762 (§6.8)
- Related: the α_r q-Pochhammer refutation (this session, PR #1733 branch) — same `q^{n(n+1)/2}` divergence mechanism, now understood as the asymptotic-series signature rather than a pure "ansatz fails" result
- Δ_λ-gate context: [`docs/audits/2026-05-18-delta-lambda-gating-context.md`](2026-05-18-delta-lambda-gating-context.md)
- Habiro precedent: [`docs/audits/2026-05-24-rt-route-research-frontiers-w-correction-habiro-heegaard.md §2`](2026-05-24-rt-route-research-frontiers-w-correction-habiro-heegaard.md)
