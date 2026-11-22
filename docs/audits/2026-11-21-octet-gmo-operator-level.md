# Octet Gell-Mann–Okubo for the weighted Murphy operator, and the Coleman–Glashow bridge

Date 2026-11-21. PR #8957, issue #8956. Follows `2026-11-21-isospin-murphy-octet.md`.

## 1. What was done

Two items, both on the weighted Jucys–Murphy operator built from the repo's Jimbo braiding
(`StrangeStrandOctet.jimbo`):

1. **Lean, sorry-free** (`QOU/BraidsAndKnots/IsospinMurphyOctetThreeStrand.lean`):
   - `weightSpaceTrace_eq`: on `(Cⁿ)^{⊗3}` with `σ₁ = Ř ⊗ 1`, `σ₂ = 1 ⊗ Ř`, the weighted Murphy trace over the weight space of `{a, a, b}` equals the 3×3 block formula `murphyTrace` with the Jimbo coefficients. So the block results are statements about the repo's braiding.
   - `coleman_glashow_weightSpace`: Coleman–Glashow `D_Σ = D_N + D_Ξ` holds for that operator for every `n`, every three distinct flavours and every weight. It is an identity of the operator, so reproducing it is evidence for nothing (operator-level `cg_cannot_discriminate`).
   - Verified with lean-direct, `-DautoImplicit=false -s 65536`, exit 0. `#print axioms` gives only `propext`, `Classical.choice`, `Quot.sound`.
2. **Exact probe** (`computations/flavour_strange_strand/octet_gmo_operator_probe.py`):
   - Gell-Mann–Okubo with the octet projected out by the central idempotent of `H₃`.
   - Λ is separated from Σ⁰ by the q-isospin Casimir of the `U_q(sl₂)` on `(u, d)` whose coproduct commutes with `σ₁, σ₂`; this commutation is checked in the probe.
   - The mass of a state is `tr(Q M_w)/tr(Q)`. Here `Q` is the octet ⋅ isospin ⋅ weight projector, of rank 2 in each case. `Q` commutes with every `L_k`, so there is no operator-ordering choice in `M_w`.

Not done in Lean: the octet and isospin projectors. The GMO figures below are exact symbolic probe output, not theorems.

## 2. GMO result

Weights are isospin-symmetric (`w_u = w_d = a`, `w_s = b`; hypercharge is a special case). Ratios are to `Ξ − N`, which cancels both the breaking strength and the unit. So each ratio is a function of `q` alone, with no free parameter beyond the flavour order.

| | order u<d<s | order s<u<d | PDG (comparison only) |
|---|---|---|---|
| GMO / (Ξ − N), closed form | `+q²h²(2q²+3) / ((q²+3)(q⁴+q²+1))` | `−q²h²(3q⁴+q²+1) / (2q⁸+4q⁶+3q⁴+q²+2)` | — |
| GMO / (Ξ − N) at q = 1 | 0 | 0 | — |
| GMO / (Ξ − N) at the proton q₀ | **+0.01854** | **−0.01839** | **−0.0679** |
| (Σ − N)/(Ξ − N) at q₀ (q = 1: ½) | 0.4219 | 0.4313 | 0.6701 |
| (Λ − N)/(Ξ − N) at q₀ (q = 1: ½) | 0.5198 | 0.5290 | 0.4659 |

Here `h = q − q⁻¹`, so `q²h² = (q² − 1)²`. GMO is `2(N + Ξ) − 3Λ − Σ`.

### What it says

- **At q = 1 GMO holds exactly**, for any isospin-symmetric weight. With general weights the defect at q = 1 is `w_u − w_d`, i.e. pure isospin breaking. This is the classical statement that first-order SU(3) breaking satisfies GMO.
- **The q-deformation gives a definite second-order GMO deviation of order `h²`** with no fitted coefficient. Its size is ≈ 1.85 % of `Ξ − N` at q₀, against 6.8 % in the data: **3.7× too small**.
- **Its sign is set by the flavour order**, which the corpus does not derive: + for u<d<s, − for s<u<d. Choosing s<u<d because it matches the sign of the data would be selection against the target. This is a scope-(a) result: no sign prediction without a derived order.
- **Λ comes out above Σ in both orders.** That is the wrong way round: the data have Σ − Λ ≈ 77 MeV. At q = 1 they are degenerate (`OctetWeightDegeneracy.lean`), and the q-deformation splits them in the wrong direction. This is scope (a), this operator only, and it parallels the wrong-sign `α₂/α₁` of the isospin-Murphy audit.
- The order u<s<d (s between u and d) was not run. The simple-coproduct `U_q(sl₂)` on non-adjacent flavours does not commute with `Ř`, so the isospin projector needs the non-simple-root generators.

## 3. Relation to `GellMannOkuboSecondOrder.lean`

That file proves that the **ansatz** `a + bY + c·d + eY² + f·d² + g·Y·d` can reach any octet masses, so second-order GMO is vacuous as a constraint on it. That remains true. The probe here instead fixes the operator and **computes** its second-order GMO, which is a parameter-free number once an order is fixed. That number misses: wrong magnitude by 3.7×, and the wrong Σ–Λ ordering.

## 4. Open

- Lean for the octet and isospin projectors (would turn §2 into theorems).
- A derivation of the flavour order. It decides the GMO sign, and per the Lean bridge it also decides whether hypercharge splits Σ (`sigma_split_s_between`).
- The u<s<d order, with the full `U_q(sl₃)` coproduct.
