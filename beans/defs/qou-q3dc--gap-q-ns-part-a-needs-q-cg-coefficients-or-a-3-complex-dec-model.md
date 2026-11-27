---
# qou-q3dc
title: 'GAP: q-NS Part A needs the q-Clebsch-Gordan triad coefficients or a 3-complex DEC model'
status: in-progress
type: task
priority: normal
created_at: 2026-11-27T18:40:00Z
updated_at: 2026-11-27T22:30:00Z
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

**2026-11-27 — budget integrand is minus a square (PR #9596).** For `u = s²`, `a* = a`, and a
`T_{s⁻¹,s}`-invariant `φ`: `φ(Xa·Xa) = −φ(w*w)`, `w = T_{s⁻¹,s}(Xa)`. Sorry-free. CONDITIONAL
consequence, not proved: if the Haar state is torus-invariant and positive, then `h(Xa·Xa) ≤ 0`
and the budget `−c·h(Du·Du)` has the sign of `c` (Woronowicz: `u = q⁻²`, `s = q⁻¹`). No modular
property is needed. Open: Haar torus invariance + positivity (Haar thread), off-diagonal
directions, Part A.

**2026-11-27 — Haar fact (1) proved (PR #9599, `haarState_torus`).** Next: when #9596 and #9599
are both on main, add the corollary `h(Xa·Xa) = −h(w*w)` with no invariance hypothesis. Fact (2),
positivity, is still open (Haar thread).

## 2026-11-27T19:37Z — off-diagonal budget identities (PR #9608)
`OqSU2BudgetAllDirections.lean`: `(X_{s0,sp,sm}a)* = -T_{q,q⁻¹}(X_{s0,sm,sp}(a*))`; for s²=q⁻¹, self-adjoint a, torus-invariant φ: φ(X₊a·X₋a) = -φ(w*w). Sorry-free, generic R. Conditional on Haar positivity (open, #9599): h(X₊a·X₋a) ≤ 0. Still open: which pairing is the transport budget; Haar positivity; Part A (qou-pa7n). Not closing.

## 2026-11-27T20:05Z — budget sign (PR #9648, on #9617 + #9646)
`OqSU2BudgetSign.lean`: for q>0, q≠1, ordered field, self-adjoint a: h(X a·X a) ≤ 0 (Cartan), h(X₊a·X₋a) ≤ 0 (s²=q⁻¹). Sorry-free. Open: identification of these integrands as the q-NS transport budget; any q→1 control; Part A (qou-pa7n). Not closing.

## 2026-11-27T20:40Z — point 1 (identification), Cartan direction
PR #9662 `q_ns_cartan_transport_budget.lean`: for the Cartan field X, `h(Xu·u)+h(u·Xu) = c·h(Xu·Xu)`, so the Cartan budget integrand IS the Haar energy rate along u̇ = Xu (up to step c), and that rate is ≤ 0 for self-adjoint u, q>0, q≠1, c⁻¹>0. Sorry-free. Still open: (i) that u̇ = Xu is the q-NS transport (corpus has no ∇_q on O_q(SU(2))); (ii) the X₊X₋ pair is not a single-field energy rate (twisted_energy_budget gives a mixed X₊/Cartan term h(X₊u·(u−θu))); (iii) q → 1 (q-Bessel thread). Part A qou-pa7n open.

## 2026-11-27T20:26Z — from q-Bessel thread, PR #9666 (OqSU2BudgetLittleQJacobi.lean)
On the torus-invariant block K[ζ], ζ=βγ: Cartan field kills K[ζ] (cartanField_ev), so h(Xu·Xu)=0 there and the X₊/X₋ pair carries the whole budget. L=X₊X₋ lower bidiagonal, diagonal λ_n = q[n]_q[n+1]_q, Haar-symmetric; h(X₊a·X₋b) = −q⁻² h(a·Lb). Per-mode factor q⁻¹[n]_q[n+1]_q → n(n+1) as q→1 (finite per mode). Consequence for point 1: on K[ζ] the Cartan identification of #9662 is vacuous; the pair term still needs its own transport identification. Open: other weight blocks, existence of eigenpolynomials p_n, relation to the mixed term h(X₊u·(u−θu)). Part A qou-pa7n open.

## 2026-11-27T20:41:00Z — triad front (thread "Part A of conj:regularity-breakdown"), PR #9681

- Property 3 vs anomaly: already settled by 9a8e9d9 (owner card "Weaken decay clause, keep Part A"). Property 3 is now a modal balance with transfer T_k, so it does not forbid an anomaly. Property 2 (the energy inequality) does not forbid one either.
- On the block K[ζ]: the X₊X₋ pair budget term is 2νq² times the energy rate of u̇ = −νLu, h(u·Lu) ≥ 0, and that flow dissipates (q_ns_block_viscous_dissipation.lean).
- A candidate triad coupling: X₊ζ^{j+1}·X₋ζ^{k+1} = [j+1]_{q²}[k+1]_{q²}(q ζ^{j+k+1} + q² ζ^{j+k+2}). That is forward-only in ζ-degree, with coefficients ≥ (j+1)(k+1) for q ≥ 1 (q_ns_block_pair_cascade.lean). Sorry-free.
- Still open: (i) that this pair product is the q-NS advection (no ∇_q on O_q(SU(2))); (ii) the coefficients in the little q-Jacobi basis; (iii) a transfer lower bound along a solution; (iv) Part A. This bean stays open.

## 2026-11-27T21:20Z — PR #9713: h∘X₊ = 0 / h∘X₋ = 0 on the blocks (sorry-free)

`QOU/FluidDynamics/q_ns_haar_field_invariance.lean`: h(X₊ x) = 0 for x ∈ K[ζ] ∪ βδ·K[ζ], h(X₋ x) = 0 for x ∈ K[ζ] ∪ αγ·K[ζ]. The βδ case reduces to h(Lζ^{k+1}) = 0; the αγ case uses βδ·αγ = ζ + q⁻¹ζ² and the Jackson moments. GAP kept open: h∘X₊ = 0 on all of O_q(SU(2)) needs a PBW-type spanning of the weight-(0,−2) part or full Haar invariance; neither is in the corpus. Part A remains open.



**2026-11-27 (thread 'Prove PBW spanning for the Haar algebra'), PR #9731.** PBW basis of O_q(SU(2)) over any comm ring, any unit q: `CompactQuantumMetrics/OqSU2PBW.lean` (mono_span, mono_linearIndependent, pbwBasis, pbwEquiv, monoRep_faithful). Whole-algebra Haar vanishing for q not a root of unity: `QOU/FluidDynamics/q_ns_haar_field_invariance_full.lean` (haarState_fieldPlus_eq_zero, haarState_fieldMinus_eq_zero, haarState_fieldZero_eq_zero). Closes #9713's open whole-algebra item. Still open: (id⊗h)Δ = h(·)1; roots of unity; ∇_q link.

2026-11-27: PR #9758 (stacked on rename #9756) proves (id⊗h)Δ = h·1 and (h⊗id)Δ = h·1 for q not a root of unity. It also proves uniqueness: a functional killed by X±, X₀, or a left-invariant one, equals g(1)·h. Root-of-unity no-go: if g(1) ≠ 0 and g∘X₊ = 0 then every [n+1]_{q²} ≠ 0, so at a nontrivial root of unity no normalised invariant functional exists. Coassociativity is in OqSU2Coassoc.lean. Not covered: q = ±1; positivity remains in #9646.

**2026-11-27 (thread 'Audit the q-Bessel special-function dictionary'), PR #9746.** Cartan Haar pairing nondegenerate (`OqSU2CartanPairingNondegenerate.lean`, q-Hilbert via a Lagrange numerator, no determinant); little q-Jacobi eigenpolynomials p_n of L span K[ζ], h(p_m p_n)=0 for m≠n, h(p_n²)≠0 (`OqSU2LittleQJacobiBasis.lean`); every weight-block pairing K[ζ](βδ)^s × (αγ)^s K[ζ] nondegenerate on both sides (`q_ns_block_pairing_nondegenerate.lean`). Sorry-free. Still open: L self-adjoint per block, giving the α=s little q-Jacobi basis (bean qou-t3nx); Part A.


## 2026-11-27 triad transfer by PBW block (PR #9766)

qou PR #9766, file QOU/FluidDynamics/q_ns_haar_triad_weight.lean, is sorry-free. For the twisted fields X+, X-, X0, the block coupling D_X(x,y) = h(x * X y) obeys two rules.

- Selection rule: D_X(x,y) vanishes unless w_x + w_y + w_X = 0.
- Twisted skew symmetry: on the selection support, D_X(x,y) = -q^(-(a+m)) D_X(y,x) for all three fields, where (a,m) is the weight of the receiving block.

So transfer is exactly skew iff a + m = 0, which on a PBW monomial (a,b,c) is a + b - c = 0. This computes the twist that q_ns_triad_noncomm left as a gap.

Not established: the link to nabla_q, any nonzero coupling, Part A. The bean stays open.
