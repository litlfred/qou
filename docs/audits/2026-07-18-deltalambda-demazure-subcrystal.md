# Δ_λ binding-magnitude: the DAMPED graded dimension (Demazure sub-crystal)

**Date:** 2026-07-18 · **Axis:** per-isotope binding
`B(K) = m_e·Σ_λ y_λ χ^λ Δ_λ` — the **magnitude** wall ·
**Tier:** derivation probe, scope-(a) honest negative + scope-(b) proved
bracket/obstruction. **No fit; nothing wired.** Gate: Δ_λ open-for-all for
derivation routes (owner reversal 2026-07-13); anti-fit discipline honored.

Follow-on to **#4012**
([`docs/audits/2026-07-18-deltalambda-jet-filtration-magnitude.md`](2026-07-18-deltalambda-jet-filtration-magnitude.md)).

Probe: [`computations/deltalambda/deltalambda_demazure_subcrystal_magnitude_probe.py`](../../computations/deltalambda/deltalambda_demazure_subcrystal_magnitude_probe.py)
· witness `deltalambda-demazure-subcrystal-magnitude.witness.json` (6 assertions, exit 0).
Lean: [`QOU/MassTheory/DemazureSubcrystalGradedDim.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/DemazureSubcrystalGradedDim.lean)
(sorry-free, `lean`-direct exit 0).

## 0. Where #4012 left the magnitude

#4012 proved the **full** coinvariant graded dimension
`W_A(q) = [A]_q! = ∏_{k=1}^A [k]_q = Σ_{w∈S_A} q^{ℓ(w)}` (a NON-determinant
object) **escapes** the `SaturationRhoCap` determinant ceiling `ρ_A ≤ C(A,2)`,
but **overshoots** A=4:

```
sub-extensive  −ln det  (ρ_A ≤ C(A,2);  undershoots both, capped)
     <  true binding magnitude  <
super-extensive  W_A(q)  (ρ_grad(3)=3.34 [−12%],  ρ_grad(4)=15.74 [+21%])
```

The missing piece #4012 identified: a **bounded A=3→A=4 growth damping** of the
factorial step `[4]_q ≈ 4.71` down toward the observed data step `≈ 3.42`,
**without** falling back below the `C(A,2)` cap.

**AGENTS.md §7b** names the interpolator precisely — a **Demazure sub-crystal**
graded dimension (partial sum over a Bruhat prefix `{w ≤ v}`, the "incomplete /
resonance state").

## 1. The object — a Bruhat sub-sum of `[A]_q!` (parameter-free, not a determinant,
not the prior Demazure-fibre ansatz)

`[A]_q!` factors as a product of coset length-gen functions:
`[A]_q! = ∏_{k=1}^A [k]_q`, where `[k]_q = 1+q+…+q^{k-1}` is the Poincaré
polynomial of the minimal-coset-representative set of `S_k/S_{k-1}` (reps of
lengths `0,…,k−1`). A **coset-chain Demazure sub-crystal** truncates each coset
at a Bruhat prefix level `t_k ≤ k−1`:

```
ρ_dem(A) = ∏_{k=3..A} [t_k+1]_q ,   t_k ∈ {0,…,k−1}
           (deuteron W₂ = [2]_q kept FULL — the saturated 2-body reference)
```

Full `t_k = k−1` recovers `[k]_q` and `ρ_dem = ρ_grad` (#4012). The **only**
choices are the *discrete* truncation levels `t_k`; `q₀` is fixed from the
substrate before any comparison.

**Distinct from the failed prior "Demazure-fibre" ansatz.** That ansatz
([`demazure-fiber-markov-trace.md`](../../content/quantum-observable-universe/mass-theory/demazure-fiber-markov-trace.md),
one of the six refuted Δ_λ closures) *re-weights the per-partition Jones–Markov
coefficient* `T^Dem(λ;w) = y_λ · D_w(λ)/D_{w₀}(λ)`. Here the object is the
cross-A **graded dimension itself**, Bruhat-truncated — the DAMPED companion to
#4012's full graded dim, not a per-λ reweight.

## 2. Result

Strong targets (AME2020 + Lean #3986/#3990 Coulomb premise, identical to #4012):
`ρ_strong(3) = 3.813`, `ρ_strong(4) = 13.032`, data step `= 3.418`.
Substrate `q₀` (muon-canonical): `[2]=2.110, [3]=3.342, [4]=4.710`.

| A | target | Demazure family (all truncations) | reading |
|---|--------|-----------------------------------|---------|
| 3 | **3.813** | `{1, 2.110, 3.342}`, max = full `[3]_{q₀}` = **3.342** | whole family **below** target |
| 4 | **13.032** | drop-top `[3]·[3]` = **11.169** … full `[3]·[4]` = **15.740** | target **bracketed** |

### 2a. A=4 — BRACKETED, and it tightens #4012 (Q2 → yes)

The A=4 target sits between two **consecutive** top-coset truncations of the
A3→A4 step (keep 3 vs 4 reps), holding A2→A3 full:

```
drop-top  [3]_q·[3]_q = 11.169   (−14.3%)
   <   ρ_strong(4) = 13.032   <
full      [3]_q·[4]_q = 15.740   (+20.8%)
```

This **tightens** #4012's window `{C(4,2)=6 (det cap), 15.74 (full graded)}` to
`{11.17, 15.74}` — the lower end rises from `6` to `11.17` with a genuinely
structural (non-determinant, non-fitted) object. Proved q-independently in Lean:
`demazure_A4_droptop_le_full` (`[3]²_q ≤ [3]_q·[4]_q`) orders the endpoints, and
`demazure_droptop_exceeds_det_cap` (`6 < [3]²_q`, indeed `≥ 9`) shows the *damped*
lower bracket still escapes the cap the determinant provably cannot clear.

### 2b. A=3 — structurally UNREACHABLE by pure damping (Q1 → no; Q3 obstruction)

A Bruhat sub-sum is **monotone `≤`** the full sum (`demazure_A3_family_le_full`:
`1 ≤ [2]_q ≤ [3]_q`), so the family maximum is the **full** ratio `ρ_grad(3) =
[3]_q`. But the full A=3 ratio *already undershoots* (`[3]_{q₀} = 3.34 < 3.81`).
Therefore the **entire** Demazure sub-crystal family lies below the A=3 target —
**no** member reaches it.

This is the structural obstruction: **pure damping is monotone the WRONG way for
A=3.** The A=3 target `3.813 > 3 = 3!/2!` exceeds even the classical coinvariant
ceiling, so A=3 needs **amplification** (`q > 1` pushing `[3]_q` up, requiring
`q ≈ 1.25`), the exact *opposite* of a sub-crystal truncation.

## 3. Verdict (scope-(a)) and the refined reading

**The Demazure sub-crystal graded dimension, alone, does not reproduce
`{3.81, 13.03}` at a single parameter-free `q₀`.** It is the **correct sign** for
the A=4 overshoot (damping brackets and tightens it) but the **wrong sign** for
the A=3 undershoot (monotone `≤` full, which already undershoots). It is **not
excluded as an ingredient** (permanence): a damping factor of this form may
compose with an A=3 amplification term.

This *refines* #4012's "the correct object is a damped graded dimension":

> A **pure** Demazure damping cannot be the whole correction — it is
> monotone-decreasing, and A=3 needs the graded dimension driven *above* its
> classical ceiling. The correction is **two-sided**: an A=3 amplification
> (`q`-driven, above `3!/2!`) composed with an A=4 growth damping (Demazure /
> resonance truncation). One knob cannot do both — but this is a *combination*
> statement, not an exclusion of the graded-dimension ingredient.

**No fit; nothing wired.** The truncation levels are discrete structural choices,
enumerated exhaustively (12 members); none lands both within 5%, and selecting a
`t_k` to hit the data would be the forbidden 7th fit — not done.

## Cross-references

- Predecessor (full graded dim): `deltalambda_jet_filtration_magnitude_probe.py`,
  [`JetFiltrationGradedDimEscape.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/JetFiltrationGradedDimEscape.lean);
  [`docs/audits/2026-07-18-deltalambda-jet-filtration-magnitude.md`](2026-07-18-deltalambda-jet-filtration-magnitude.md).
- Determinant cap this escapes: `SaturationRhoCap.lean` (`ρ_A ≤ C(A,2)`);
  no-go family [`2026-07-18-deltalambda-exchange-determinant-family-nogo.md`](2026-07-18-deltalambda-exchange-determinant-family-nogo.md).
- **Distinct** prior per-partition ansatz (refuted):
  [`demazure-fiber-markov-trace.md`](../../content/quantum-observable-universe/mass-theory/demazure-fiber-markov-trace.md);
  Option-E ledger [`docs/coordination/option-e.md`](../coordination/option-e.md) (§"Six prior ansätze").
- Attack-vector map: [`docs/audits/2026-07-18-deltalambda-attack-vector-map.md`](2026-07-18-deltalambda-attack-vector-map.md).
- §7b Demazure sub-crystals for resonances (authoring guidance): `AGENTS.md §7b`;
  KLR-dialog assessment [`docs/audits/2026-05-30-klr-dialog-assessment.md`](2026-05-30-klr-dialog-assessment.md).
