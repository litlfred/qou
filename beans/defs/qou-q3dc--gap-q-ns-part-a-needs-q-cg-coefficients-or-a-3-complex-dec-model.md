---
# qou-q3dc
title: 'GAP: q-NS Part A needs the q-Clebsch-Gordan triad coefficients or a 3-complex DEC model'
status: in-progress
type: task
priority: normal
created_at: 2026-11-27T18:40:00Z
updated_at: 2026-11-27T19:10:00Z
parent: qou-pa7n
---

Follow-up to qou-pa7n (PR #9537). Two results show Part A of `conj:regularity-breakdown` is false on every finite or two-dimensional model:
- `partA_fails_on_truncation` (q_ns_modal_triad.lean) covers every finite truncation of the triad model;
- `partA_fails_dec2d` (q_ns_dec_refinement.lean) covers every 2-complex at every resolution, given an enstrophy-skew advection.

**Two routes forward.**

1. **q-CG coefficients.** Compute the coefficients of `μ∘(v⊗∇_q v)` on SU_q(2) Peter–Weyl modes, i.e. the q-Clebsch–Gordan / 6j coefficients times the `∇_q` symbol. Instantiate `TriadCoeff` with them (the conservation field must be proved, not assumed). Then state Part A as a primary conjecture over the infinite-mode system. Note that `∇_q = q⁻¹∇ + (1−q⁻¹)(ι_ξ∇)Θ` is a derivation, so energy conservation should follow from Leibniz and the dagger adjointness. That is to be proved.
2. **3-complex DEC model.** Build `C⁰→C¹→C²→C³` with vortex stretching and state Part A over refining 3-complexes.

Open conjecture: do not close until Part A is proved or refuted. QOU-formalised sources only (owner rule 2026-11-27).

## 2026-11-27 progress (route 1, q-CG; PR pending)
`q_ns_triad_derivation.lean` (sorry-free): triad conservation is now DERIVED for the advection from the Leibniz rule and `τ∘X = 0` (`transport_skew`, `advectionTriad`). The corpus q-connection field is a derivation (`qField`). `parseval` and `transfer_eq_advection` tie the Galerkin transfer to the advection. Remaining hypotheses: the Clebsch–Gordan selection rule `hsel`; incompressibility; a commutative trace setting (the O_q(SU(2)) Haar state is not tracial, so the noncommutative picture needs a twisted Leibniz rule; open); and the numerical q-CG values. Audit `docs/audits/2026-11-27-qns-triad-conservation-from-leibniz.md`. Part A stays open; do not close.

## 2026-11-27 progress: noncommutative case
`q_ns_triad_noncomm.lean` (PR #9545, sorry-free): triad conservation holds for ANY linear functional
on a noncommutative algebra, given an untwisted divergence-free derivation; the energy sees only the
symmetrised form. Traciality is not needed, so the Haar modular twist is no obstruction. Remaining gap:
is `∇_q` an untwisted derivation on O_q(SU(2))? Twisted derivations break the argument. Still open:
q-CG selection rule derivation, numerical couplings, infinite-mode Part A.

## 2026-11-27 progress: twisted transport
The corpus 3D calculus on O_q(SU(2)) (ex:connection-su2) has twisted vector fields, so the untwisted
result does not apply. `q_ns_twisted_transport.lean` (sorry-free) proves the exact budget
φ(Xu·u)+φ(u·Xu) = φ(Xu·(u−θu)) for a θ-twisted, φ-divergence-free X. For the q-difference
D = (θ−id)/c with φ∘θ = φ, it is −c·φ(Du·Du): q-difference transport dissipates at first order in c.
Open: build the 3D-calculus vector fields on OqSU2 and get the sign and size of c; Part A.

## 2026-11-27 — orientation and balanced difference (PR #9558)

- `qDiff_neg`: the sign of the one-sided budget −c·φ(Du·Du) flips with the orientation of the difference.
- `qCen_energy_conserving`: the balanced difference (θ − θ⁻¹)/c conserves energy exactly for θ-invariant φ.
- `theta3D`: the Woronowicz 3D-calculus twist (q⁻², q⁴, q⁻⁴, q²) is the corpus `torusScaleAlgEquiv q (q⁻²) (q⁴)`; `theta3D_energy` gives both budgets on OqSU2.
- Still open: which difference the 3D-calculus vector fields are; Haar invariance (a hypothesis); positivity and the *-structure; Part A (qou-pa7n).

## 2026-11-27 — coproduct and Cartan field (PR #9565); theta3D scoped (PR #9558 e724703559a)

- `OqSU2Coproduct.lean`: coproduct on O_q(SU(2)); diagonal-character translations are torus scalings (right (u,u⁻¹), left (u,u)); HK σ = left_q ∘ right_{q⁻³}, two-sided.
- Left-invariant fields of (ε,χ)-twisted derivations are one-sided twisted; `cartanField`: (ε − χ_u)/c gives c⁻¹(f − R_u f), the one-sided qDiff, so its budget is −c·φ(Du·Du).
- Correction: `theta3D` (HK σ) is the cocycle twist, not the Leibniz twist; #9558 docstring and audit doc now say so.
- Still open: Woronowicz's exact Cartan functional and u (Woronowicz 1987 not in library); off-diagonal fields; coassociativity; Haar state; Part A (qou-pa7n).

## 2026-11-27 — Woronowicz's Cartan field pinned (PR #9573)

- From Woronowicz 1987 (owner upload, now library/woronowicz1987-twisted-su2): χ₁ = (ε − f₁)/(1 − ν⁻²), f₁ = diag char at ν⁻² ((2.2), (2.5)); values (2.3) and Leibniz (2.7) proved in `OqSU2WoronowiczCartan.lean`.
- Dictionary: β = −νγ*, δ = α*, q = ν. So u = q⁻², c = 1 − q⁻²; one-sided budget −c·φ(Du·Du) = (q⁻² − 1)φ(Du·Du).
- Still open: sign (positivity, *-structure), χ₀/χ₂ (separate thread B), Haar (thread C), Part A (qou-pa7n).

**2026-11-27 — `*`-structure (PR #9581).** `CompactQuantumMetrics/OqSU2Star.lean`, sorry-free.
The corpus `compactStar` matches Woronowicz's `*`; `Δ(x*) = (*⊗*)Δx`; torus and characters
intertwine with `u ↦ u⁻¹`; for the Cartan field, `(Xa)* = −T_{u⁻¹,u}(X(a*))`, and for `a* = a`,
`Xa·Xa = −(T(Xa))*·Xa`. So the budget integrand is minus a twisted square. Positivity of `φ`
alone does not sign it; the Haar modular property is needed. Still open: that step, χ₀/χ₂,
Haar invariance, Part A (`qou-pa7n`).

**2026-11-27 — note from the off-diagonal thread (PR #9593).** The 3D calculus has twist characters
diag(q⁻¹, q⁻², q⁻¹): χ₀ ↔ X₊ and χ₂ ↔ −q·X₋, both twisted by q⁻¹. χ₁ is the Cartan field, twisted by q⁻².
Use these when the budget is extended to all three directions.
