# RESULT: the (gl₆, gl₃⊕gl₃) coideal as colour on colour⊗flavour (bean `qou-ni4b`)

- Pre-registration: `PREREGISTRATION-gl6-coideal-colour.md`, commit `8217cac241b`, pushed before any code.
- Probe: `qcd_coideal_gl6_colour_probe.py`, output `qcd_coideal_gl6_colour_probe.out.json`.
- **32/32 checks pass. Every pre-registered prediction held.** One check is post-hoc and is labelled
  `posthoc` in the JSON.
- Exact arithmetic: sparse matrices over the fraction field ℚ(q, c₁, c₂, c₃, a, b). No float. q₀ is
  not used. Run time a few minutes.
- c₁, c₂, c₃ are free symbols throughout. c₄ = c₂ and c₅ = c₁ is Kolb's admissibility condition,
  and Q2 shows it is forced by the classical limit (without it the q = 1 closure is all of gl₆,
  dimension 36, not 18). s₃ = 0; s₃ ≠ 0 was not tested.

Setting: Jimbo U_q(gl₆) on ℂ⁶, variant-B coproduct, Ř = `jimbo_R(6, upper=True)`. Satake data AIII
quasi-split, X = ∅, τ(i) = 6 − i. Generators B_i = F_i − c_iE_{τ(i)}K_i⁻¹ (i = 1..5) and the θ-fixed
torus T_j = K_{ε_j}K_{ε_{7−j}}. The labelling v₁…v₆ = (1u)(2u)(3u)(3d)(2d)(1d) is the τ-orbit
structure, so J = 1_c⊗σ_x. The colour candidate is **B^col = ⟨B₁, B₂, B₄, B₅, T₁, T₂, T₃⟩**, which is
B with the τ-fixed node 3 removed. It is identified by its classical limit, not selected.

## Claim

**The (gl₆, gl₃⊕gl₃) coideal does contain a genuine quantum colour that moves with the strand at
generic q.** It meets (a), (b), (c), (e) and (f). It fails (d), and (d) fails for a reason that is
not about this construction. The reason is the S₃ sign character of the colour singlet. That makes
(d) and (f) incompatible for **every** construction whose q → 1 colour is sl₃⊗1 carried with the
strand.

1. **(a) holds.** On (ℂ⁶)^⊗n, n = 1, 2, 3, B^col satisfies the U_q(sl₃) relations exactly. Write
   e_i = B_{τ(i)}, f_i = B_i, k₁ = T₁T₂⁻¹ and k₂ = T₂T₃⁻¹. Then:
   - k e k⁻¹ = q^{a_ij} e;
   - [e_i, f_i] = −c_i(k_i − k_i⁻¹)/(q − q⁻¹);
   - the q-Serre relations hold;
   - [e_i, f_j] = 0 for i ≠ j.

   So after rescaling e_i by −1/c_i, B^col acts as a quotient of U_q(sl₃). Its classical closure is
   gl₃ (dimension 9). After a colour rescaling on the d-block, diag(1, −1/c₁, 1/(c₁c₂)), it is
   exactly gl₃⊗1_flavour.
2. **(b), (c), (f) hold.** B ⊂ U_q(gl₆), so Δⁿ(B) commutes with the Jimbo σ_i (checked, n = 2, 3).
   Hecke and braid hold, and Ř|_{q=1} = P = P_c⊗P_f.
3. **(e) holds in the K0 sense.** The B^col-invariants in V^⊗3 have dimension 8: one colour singlet
   for each flavour state. There are none in V⊗V. T_j acts on them by q, so k₁ and k₂ act by 1.
4. **(d) fails.** The singlet sector is an 8-dimensional H₃-module with tr σ₁ = 2(q² − 3)/q and
   tr σ₁σ₂ = −2(q² − 2)/q². That is **S^(1³)×4 ⊕ S^(2,1)×2**. It is isomorphic to the *fermionic*
   flavour model σ ↦ −Ř_f⁻¹ and not to the flavour model σ ↦ Ř_f, which is S^(3)×4 ⊕ S^(2,1)×2. Its
   K_f-Markov parameter is z_D(−q⁻¹) = −1/(q(q²+1)), not z_D = q³/(q²+1).

| | result | scope |
|---|---|---|
| (a) injective colour, U_q(sl₃) relations | ✓ n = 1, 2, 3 | exact on these modules |
| (b) commutes with H₃ | ✓ | structural: B ⊂ U_q(gl₆) |
| (c) Hecke + braid | ✓ | exact |
| (d) singlet sector = Ř_f flavour model, z_D | **✗**: fermionic model, z = z_D(−q⁻¹) | (b), sign invariant, see below |
| (e) one colour singlet per flavour state | ✓ dim 8 | exact |
| (f) transport | ✓ | exact |

## The K4 question

**Yes, this colour moves with the strand without forcing q² = 1, and the reason is structural.** K4
assumed colour acts strand-wise through a Hopf algebra on the colour factors only, Δ_H(x)⊗1_flavour.
The coideal coproduct is not of that form. On V⊗V:

Δ(B₁) = B₁⊗K₁⁻¹ + 1⊗F₁ − c₁K₅K₁⁻¹⊗E₅K₁⁻¹,

and here F₁ acts on the u-flavour of strand 2 with first leg 1, while E₅ acts on the d-flavour of
strand 2 with first leg K₅K₁⁻¹ = q^{(E₂₂−E₁₁)}⊗1 ≠ 1. So at q ≠ 1 the colour operator on strand 2
depends on that strand's flavour through q-weights of the other strands. This was checked:
- Δ²(B_i) does not commute with 1⊗(1_c⊗σ_x) for i = 1, 2, 4, 5. It does commute with the diagonal
  flavour 1_c⊗σ_z on either strand.
- At q = 1, c = −1 the same operators commute with 1⊗(1_c⊗σ_x) (post-hoc check). So the flavour
  dependence is purely a q ≠ 1 effect.

K4's hypothesis therefore fails, and its q² = 1 conclusion does not apply. **The price is that
colour and flavour no longer factorise at generic q.** Only the diagonal flavour U(1) (σ_z, the u/d
weight) commutes with colour strand-wise. Note also that the B-invariant flavour direction of the full
coideal is σ_x (u ± d), since J = 1_c⊗σ_x. Isospin su(2) is not a symmetry of the coideal.

## Why (d) cannot be met together with (f): a scope-(b) exclusion, invariant = S₃ sign

At q = 1, (f) gives σ = P_c⊗P_f. The unique sl₃-invariant in (ℂ³)^⊗3 is ε, and P_c acts on it by −1.
So on the colour-singlet sector σ|_{q=1} = −P_f. But (d) asks for Ř_f|_{q=1} = P_f. On (ℂ²)^⊗3 these
are non-isomorphic S₃-representations: tr σ₁ is −4 against +4, and this was measured here as the
q → 1 limit of the exact character. H₃(q) is semisimple at generic q and its multiplicities are
integers that are constant on a Zariski-open set, so the mismatch persists at generic q. That is
exactly the S^(1³)×4 ⊕ S^(2,1)×2 measured.

So **every** construction whose q → 1 colour is sl₃⊗1 *carried with the strand* has a colour-singlet
sector that is the sign twist of the flavour model, never the flavour model itself.
- This is a statement about the pre-registered test (d), not about this coideal.
- The proof is the argument above, not a Lean theorem. It has not been formalised.
- K0 meets (d) only because it does not transport colour.
- The sign twist is the Hecke automorphism σ ↦ −σ⁻¹. It maps convention D (zero weight on S^(1³)) to
  the trace with zero weight on S^(3). It does not map D to itself.

Consequences for the D question:
- On the singlet sector, any colour-blind flavour twist G = 1_c⊗diag(a, b) gives a trace with block
  weights m₃ = 0, m₂₁ = ab(a+b) and m₁₃ = (a+b)(a²+b²).
- D's zero on S^(1³) would require a² + b² = 0 (b = ±ia), or b = −a, which also kills S^(2,1). These
  are recorded as a SELECTION-only flag. Nothing is chosen.
- D read as "kill S^(1³)" sees only the S^(2,1)×2 part of the transported baryon. That is the same
  radical statement as `qcd_colour_full_tower` and `qcd_coideal_colour` post-hoc 2–3.

## Other measurements

- **Q4, K-matrix of the full B.** The commutant on ℂ⁶ is span{1, J_q} with J_q antidiagonal. The
  reflection equation on α·1 + β·J_q holds exactly on the line α = 0, so K = J_q.
  - Its eigenvalues are ±c₁⁸c₂⁶√(−c₃⁵q⁵), each with multiplicity 3. So K² is a scalar and the
    type-B eigenvalue ratio is −1.
  - K⊗1 commutes with Δ²(B).
  - The commutant of B^col on ℂ⁶ has dimension 4: the flavour matrices, conjugated by the
    c-rescaling.
- **Q6(i), product twists.** Each of the 4 B^col-invariant twists T₁ on ℂ⁶ gives T₁⊗piv either
  trace 0 or Markov parameter z₆ = q⁶/[6]_q. That is the Schur argument of the prior probe with
  ℂ⁶ irreducible for U_q(gl₆). z_D does not appear.
- **Q2.** The full B has classical closure of dimension 18 (gl₃⊕gl₃). The removed generator B₃ is the
  only flavour-mixing one: B₃|_{q=1} = E^c₃₃⊗[[0, −c₃], [1, 0]].

## What is established and what is not

Established, exactly over ℚ(q, c):
- U_q(sl₃) colour inside the (gl₆, gl₃⊕gl₃) coideal, commuting with the transported gl₆ Hecke
  action. This is the first construction on this branch to meet (a), (b), (c), (e) and (f) at once.
- Its singlet sector is the fermionic flavour model.

Not established:
- (d). This is a pre-registered fail. The sign argument says no transported sl₃ colour can meet (d)
  as worded, so the real question is whether (d) is the right test. **That is a modelling decision
  for the owner** (see the bean), not a computational result.
- Relations beyond n = 3. The probe verifies U_q(sl₃) relations on V^⊗n for n ≤ 3, not an algebra
  isomorphism B^col ≅ U_q(sl₃).
- s₃ ≠ 0, non-product twists, n ≥ 4, and a Lean formalisation (none written).
- The literature claim that the diagonal-type QSP coideal is isomorphic to U_q(g) was not checked
  against a source. It was not used; only the relations above were measured.
- No gluon is identified. Nothing was selected.

## Verification

- `python3 -u qcd_coideal_gl6_colour_probe.py` → `SUMMARY 32/32`, exit 0.
- `scripts/precision-gates.sh --changed`: the RED lines are the same repo-wide ratchets as in
  `qcd_coideal_colour/RESULT.md` (q0-anchor flip/refill, never-raises-dps, reference-literal,
  witness-value copy, q0-value drift). None names this directory. The gate rewrote eight audit
  witnesses, which were restored and not staged.
