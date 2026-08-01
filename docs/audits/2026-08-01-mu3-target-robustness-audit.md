# μ₃ target robustness audit (A=3 magnitude ROUTE 5, red-team / meta)

**Date:** 2026-08-01
**Branch:** `claude/mu3-target-robustness-audit-2026-08-01`
**Bean:** `qou-7gez`
**Mandate:** SKEPTICAL / red-team. Sibling agents (ROUTE 1–4) are chasing the
A=3 magnitude factor `r* = μ₃/c₃ ≈ 1.585` via cross-channel mechanisms
(operator branching, super-Berezinian, sub-link sum, Habiro element). This route
red-teams the *premise*: is `μ₃ = +0.4708 MeV` a genuine STRUCTURAL constant
worth deriving, or a residual-DECOMPOSITION ARTIFACT whose value drifts under
reasonable re-choices?

## Verdict (scope-(a))

**`r* = 1.585` is a legitimately-posed target at the ~10% level — NOT a
decomposition artifact, but NOT well-posed to 3 sig figs.** The cross-channel
hunt is **justified** (the target's *sign* and *O(1.6) magnitude* are real
structural facts), with one discipline caveat: siblings should score a derived
`c₃` by SIGN and by landing `r*` in the band `[1.50, 1.71]` (~±8%), **not** by
matching `1.585` to 3 sig figs — the residual physically cannot carry that
precision.

The initial red-team hypothesis (that a q-integer-convention swing of ~1.6×
makes `r*` an artifact) was **checked and retracted**: the convention is *pinned*
(see Axis (b)). The honest residual soft-spot is the ~±8% isospin-correction band
on a condition-number-≈8 residual, not a free-floating value.

## How μ₃ is defined (the exact recipe)

Source: `computations/deltalambda/deltalambda_kappa_interface_residual_simplex_probe.py`
(`AdditiveResidualSimplex` #4320) and
`deltalambda_saturation_det_ceiling_probe.py` (ρ_strong construction).

```
ρ_grad(A) = [A]_q! / [2]_q!               # subtracted graded "model" baseline
ρ_strong(A) = B_strong(A) / B(²H)         # isospin/Coulomb-corrected AME target
M(A) = ρ_strong(A) − ρ_grad(A)
simplex solve over coordination counts C(A,k):
    μ₂ = M(2),  μ₃ = M(3) − 3·μ₂,  μ₄ = M(4) − 6·μ₂ − 4·μ₃
```

The 3×3 counts matrix `[[1,0,0],[3,1,0],[6,4,1]]` is UNIT-triangular (det = 1),
and `M(2) = 0` is **forced** by the deuteron self-reference (`ρ_strong(2) = 1`,
`ρ_grad(2) = 1`, both by construction). Therefore:

> **μ₃ = M(3) EXACTLY** = `B(³H)/B(²H) − [3]_q` = `3.8128 − 3.3420 = 0.4708`.

`μ₃` is a **single-isotope residual re-labelled**, not a statistical moment of a
distribution. The canonical value reproduces exactly: `μ₃ = 0.470767`,
`r* = μ₃/0.297 = 1.5851`.

## The cancellation structure (why precision is limited)

`μ₃ = 3.8128 − 3.3420` is a **12.3% residual of two O(3.4) numbers** →
**condition number ≈ 8.1**. Any relative perturbation of either operand is
amplified ~8× in μ₃. This alone caps μ₃ as a low-precision target regardless of
the mechanism used to derive `c₃`.

## Robustness under re-choices (companion probe)

Probe: `computations/deltalambda/mu3_target_robustness_audit_probe.py`
→ `mu3-target-robustness-audit.witness.json`. All values at the muon-canonical
`q₀ = 1.10997859…`, `c₃ = 0.297` (#4364 H₉ lift).

### Axis (a) — which A=3 isotope / isospin correction enters ρ_strong(3)?

| choice for B_strong(3) | μ₃ | r* | vs canonical |
|---|---|---|---|
| **triton ³H direct (canonical)** | **0.4708** | **1.585** | 1.00× |
| ³He + E_C(sphere) | 0.5090 | 1.714 | 1.08× |
| ³He + E_C(pair) | 0.4454 | 1.500 | 0.95× |
| mean(³H, ³He+E_C) | 0.4899 | 1.649 | 1.04× |
| ³He raw (NO Coulomb corr.) | 0.1274 | 0.429 | 0.27× |
| mean(³H, ³He raw) | 0.2991 | 1.007 | 0.64× |

**Finding:** within the *physically-defensible isospin-corrected-strong family*
(³H, ³He+E_C variants, mean) μ₃ ∈ [0.445, 0.509], **spread only 1.14× (±~8%)**,
`r* ∈ [1.50, 1.71]`. μ₃ collapses to 0.127 (0.27×) only under raw ³He with **no**
Coulomb correction — physically inconsistent (comparing a Coulomb-suppressed
binding to a strong-only ladder), so not a defensible re-choice. **Axis (a) is
reasonably robust; the ~±8% band is the honest irreducible uncertainty.**

### Axis (b) — the subtracted "model" ladder ρ_grad(3) convention

| convention | ρ_grad(3) | μ₃ | r* | legitimacy |
|---|---|---|---|---|
| **unbalanced [3]_q @ q₀ (canonical)** | 3.3420 | 0.4708 | 1.585 | **pinned-correct** |
| balanced [3]_q @ q₀ | 3.0437 | 0.7691 | 2.590 | **ILLEGITIMATE** |
| unbalanced [3]_q @ q₀_proton | 3.3420 | 0.4708 | 1.585 | pinned-correct |
| classical (q→1: [3]=3) | 3.0000 | 0.8128 | 2.737 | limit-only |

The balanced-vs-unbalanced swing is **1.63×** — which happens to *coincide* with
the `r* ≈ 1.585` the cross-channel hunt seeks. This looked like a smoking gun for
"artifact." **It was checked and retracted:** `ρ_grad(A) = [A]_q!` is the
*q-scaled coinvariant graded dimension* (per `deltalambda_damping_nonmonotone_wall_probe.py`
context / #4300 `JetFiltrationTwoAnchorNoGo`). By Chevalley, the graded dimension
of the `S_A` coinvariant algebra is `∏_{k=1}^A [k]_q` with the **Gaussian
(unbalanced)** `[k]_q = 1+q+…+q^{k-1}`. So the unbalanced convention is **forced**
by ρ_grad's categorical meaning — the "balanced" row is not a legitimate
re-choice (it would not be a graded dimension). The q₀ pin (muon vs proton) is
**not a lever** (identical to 8 sig figs). **Axis (b) is pinned; no free knob.**

### Axis (c) — the "moment-extraction method"

**Collapses.** With exactly 3 isotopes pinning 3 coefficients through a
unit-triangular matrix, the decomposition is an EXACT invertible relabel — there
is no residual, no over-determination, and hence **no raw-central-moment vs
Richardson vs cumulant freedom**. `μ₃ = M(3)` identically. The "moment" language
is a coordinate name, not a statistical estimate.

## What the corpus already proves about robustness (fairness)

`deltalambda_damping_nonmonotone_wall_probe.py` + #4300 establish:
- The residual sign is **+ at A=3, − at A=4** for BOTH the isospin-corrected
  targets AND the raw AME ratios (`B(³H)/B(²H)=3.814`, `B(⁴He)/B(²H)=12.72`) —
  the sign is **insensitive to the anchor values**.
- The required correction is **non-monotone** in A, so it **cannot be a damping**
  (a damping only subtracts). This is why the A=3 baseline `[3]_q` is stable: a
  damped (smaller) ladder at A=3 would *worsen* the undershoot, so no damped
  replacement moves ρ_grad(3).

So `sign(μ₃)=+` and the ≥3-body purity are corpus-proved robust; only the
*magnitude* carries the ~±8% band.

## Formalized invariant — μ₂ FORCED vs μ₃ FREE

`content/quantum-observable-universe/lean/QOU/MassTheory/Mu3TargetWellPosedness.lean`
(verified `lean`-direct, exit 0, sorry-free, over generic `[CommRing R]`; §7c —
no archimedean construct). The solve is `solMu2 = m₂`, `solMu3 = m₃ − 3·m₂`.

| lemma | content |
|---|---|
| `mu2_pinned_cannot_reach_one` | under `M(2)=0`, `μ₂ = 0` for every A=3,4 target, so it **cannot equal 1** — a real structural constraint (needs `Nontrivial R`) |
| `mu3_surjective_in_target` | `∀ v ∃ m₃, solMu3 0 m₃ m₄ = v` — μ₃ hits every value: nothing pins it |
| `mu3_eq_A3_target_of_deuteron` | `μ₃ = m₃` under `M(2)=0` — the "3-body moment" is one isotope's residual |
| `forced_free_contrast` | the pinned-μ₂-misses-1 ∧ free-μ₃-hits-`v` capstone |

**Reading:** μ₂ = 0 is a *forced* invariant (the residual provably cannot have a
2-body/edge component ≠ 0); μ₃ is a *free coordinate* whose value is exactly the
A=3 AME residual — its structural content is its **sign + order of magnitude**,
not a 3-sig-fig number.

## Advice to the ROUTE 1–4 siblings

1. The hunt is **justified** — `μ₃ > 0` (proved), ≥3-body pure (μ₂=0 forced), and
   `|μ₃| ≈ 0.47 ± 0.04` are real structural facts, not an artifact.
2. **Score a derived `c₃` by sign and by landing `r*` in `[1.50, 1.71]`
   (~±8%)** — the isospin-correction band. Do **not** tune a mechanism to
   reproduce `1.585` to 3 sig figs: that would over-fit the isospin convention
   inside a condition-number-8 residual.
3. A mechanism that lands the correct sign and `r* ≈ 1.6 ± 0.1` at **0 fit** is a
   genuine success; a 3-sig-fig "match" is a red flag, not a win.

## Anti-fit / honesty ledger

- **0 free parameters** in the robustness probe; `μ₃`, AME, CODATA never inverted
  to solve a canonical weight. The probe only re-runs the canonical recipe under
  a matrix of convention choices and reports the spread.
- The one durable negative here — "μ₃'s 3-sig-fig value is not well-posed" — is
  classified **scope-(a)** (a precision/convention limitation of the *residual*),
  NOT a scope-(b) structural exclusion of any ingredient. The sign and O(1)
  magnitude stand.
- Red-team hygiene: the strongest first-pass claim (axis-(b) convention swing
  ⇒ artifact) was **checked against the corpus and retracted** — the convention
  is categorically pinned. Honest correction recorded rather than shipped.
- Lean is formalize-first, sorry-free, no laundering, generic base ring.
  Nothing wired to production.

## Files

- Probe: `computations/deltalambda/mu3_target_robustness_audit_probe.py`
- Witness: `computations/deltalambda/mu3-target-robustness-audit.witness.json`
- Lean: `content/quantum-observable-universe/lean/QOU/MassTheory/Mu3TargetWellPosedness.lean`
- This audit: `docs/audits/2026-08-01-mu3-target-robustness-audit.md`
