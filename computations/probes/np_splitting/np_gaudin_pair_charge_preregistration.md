# Pre-registration: does a Gaudin / KZ pair coupling between two nucleon blocks give a Coulomb term?

Date: 2026-11-22. Branch `claude/coulomb-photon-exchange-2026-11-22`, PR #9077, issue #9069.
Written and committed **before** the probe `np_gaudin_pair_charge_probe.py` exists.

Photon form in scope (owner ruling 2026-11-20): γ = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹. Not used
directly here; the earlier probes (audit §26-§27) showed no braid element at n = 6 gives a
Coulomb or isospin pair shift.

## Question

Owner, 2026-11-22: put the braids on Bring's surface. Locally, points z_A, z_B on a surface
carry the Knizhnik–Zamolodchikov connection ħ Σ Ω_ij d log(z_i − z_j) and the Gaudin
Hamiltonians Σ Ω_ij/(z_i − z_j). Does the pair term between two three-strand blocks give a
charge-charge energy c + κ·Q_A·Q_B, with a zero on the neutron (Q = 0)?

## Set-up (same as §26)

Six qubits, V = C², bit 0 = u. Blocks A = sites 0-2, B = sites 3-5. Block charge
Q = (#u) − 1, so p = 1, n = 0, Δ⁻ = −1, Δ⁺⁺ = 2; isospin W = 2Q − 1. Readout
T_X(a,b) = Tr(K^{⊗6} (Π_a ⊗ Π_b) V_A³ V_B³ X), ΔE_X = T_X / T_1, with V = σ₀σ₁⁻¹ on each
block (ruling A) and K = diag(q, q⁻¹).

Pair operators X, all summed over i ∈ A, j ∈ B:

| name | X | what it is |
|---|---|---|
| G-sl2 | Σ (½h_ih_j + e_if_j + f_ie_j) | rational sl(2) Casimir tensor (Gaudin numerator) |
| G-gl2 | Σ P_ij | gl(2) Casimir tensor = sl(2) part + ½·1⊗1 |
| G-cartan | Σ h_ih_j | the trigonometric (coth u) diagonal part |
| G-q, G-q^op | Δ_AB(C) − C_A − C_B | U_q(sl2) pair Casimir; the coproduct order that commutes with Ř is chosen by the probe and reported, the other kept as control |
| M | β_AB² | KZ monodromy: the full twist of block A around block B in H_6(q) |
| QQ | Σ q_iq_j, q = E₁₁ − ⅓ | the Coulomb operator itself, quark charges 2/3, −1/3 (control) |

Outcome classes per X, on all 16 sectors and on the 4 nucleon sectors:
O1 Coulomb c + κQ_AQ_B; O2 isospin c + κW_AW_B; O3 affine-bilinear otherwise; O4 not bilinear.

## Predictions (registered)

1. **G-sl2, G-gl2, G-cartan give O2 exactly, on every sector, at every q.** Argument: e and f
   change the weight, and Π_a, V³ and K preserve it, so the off-diagonal terms have zero
   trace; the Cartan part sums to Σ_i h_i = 2T₃ per block. So ΔE = 2T₃^A T₃^B (+ constant
   for gl(2)) = ½W_AW_B. The u(1) of gl(2) acts as the identity on V and only adds a constant;
   it is baryon number, the same for p and n.
2. **No gl(2)-invariant symmetric form can give O1.** The invariant forms on gl(2) are
   a·tr(XY) + b·tr X·tr Y. Their Cartan part is a(E₁₁⊗E₁₁ + E₂₂⊗E₂₂) + b·1⊗1 =
   (a/2)h⊗h + (a/2 + b)·1⊗1, with no h⊗1 cross term. Coulomb needs the cross term:
   Q⊗Q with Q = E₁₁ − ⅓ = ½h + ⅙ contains (h⊗1 + 1⊗h)/12. Equivalently, Coulomb has
   pp ≠ nn, and every invariant form is symmetric under the Weyl reflection u ↔ d, which
   swaps pp and nn.
3. **G-q is the open cell.** The q-coproduct is not Weyl symmetric (K ↔ K⁻¹ is q ↔ q⁻¹), so
   linear terms can appear. Prediction: O3 or O4, not O1. Not proved in advance.
4. **M gives O3 with α + β = 1 or O4**, never O1 or O2, because M is in the H_6 image and
   §27 found only that bilinear reachable there.
5. **QQ gives O1 with κ = 1, zero on n**, by construction. It is the control that the readout
   can see a Coulomb term when one is put in.

## Distance (stated, not computed)

The Gaudin term carries 1/(z_A − z_B) and the KZ connection integrates to
Ω·log(z_A − z_B). On a surface the Coulomb potential is log|z|, and 1/|z| needs three
dimensions. So the KZ/Gaudin coordinate dependence is the two-dimensional Coulomb law; the
question tested here is only whether its **charge factor** is Q_AQ_B.

## What would change the plan

- If any invariant X gives O1: that is the charge vertex; formalise it in Lean.
- If G-q gives O1 or a Coulomb pattern on nucleons: same.
- If all invariant X give O2 or O3 and only QQ gives O1: Coulomb needs a coupling that breaks
  the Weyl reflection, i.e. the Gell-Mann–Nishijima mixing Q = T₃ + B/2. Record that as the
  missing input, and check whether the helon ribbon twist (Bilson-Thompson, Gresnigt: charge
  = integral twists, a B₂ ≅ ℤ framing datum) can supply it.

Exact arithmetic only (sympy over Q(q), Fractions at q = 111/100, 7/5, 2). No fitting, no
empirical input.
