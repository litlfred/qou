---
# qou-zoyv
title: 'GAP: the Drinfeld category D_ℏ (Rep gl2 with KZ associator) is a ribbon category'
status: in-progress
type: task
priority: normal
created_at: 2026-10-12T18:13:09Z
updated_at: 2026-11-18T07:46:25Z
parent: qou-59vq
---

Needed to instantiate the KZ Step 2 ribbon lemma at D_ℏ (θ = e^{iπℏC}). No Lean construction of D_ℏ as a MonoidalCategory with the KZ associator exists; pentagon/hexagon are matrix identities in QOU/KZ/KZPentagon, KZHexagon (#7706), not yet packaged as BraidedCategory with twist and duals. Do not close while open.


## 2026-10-12 — what instantiating the Step-2 ribbon lemma at D_ℏ still requires (from qou-xyxc)
The abstract lemma is proved: QOU.MathlibExt.ribbon_hecke_dimension / ribbon_hecke_qDim_eq_qint_two (QOU/MathlibExt/RibbonHeckeDimension.lean, sorry-free). Its hypotheses, which D_ℏ must supply:
[Category C] [MonoidalCategory C] [BraidedCategory C] [RightRigidCategory C] [RibbonCategory C] (QOU.MathlibExt.Ribbon: BalancedCategory twist + twist_dual), [Preadditive C] [Linear k C] [MonoidalPreadditive C] [MonoidalLinear k C], and for V = ℂ²: (i) β−β⁻¹ = (q−q⁻¹)•𝟙 on V⊗V, (ii) θ_V = q²•𝟙, (iii) qDimTwistedWith V Vᘁ is a scalar d•𝟙 (true if End(𝟙)=k), (iv) 𝟙_V ≠ 0, q²≠1.
What exists: QOU/KZ/KZPentagon.pentagon and QOU/KZ/KZHexagon.hexagon are identities in a Banach algebra R for KZ associators Φ / phiKZ of residue data (t12, t23, …; A, B, C=−A−B), with eπ the half-monodromy; QOU.Mass.KohnoTwoPoint.exchange_eq_classical gives the two-strand Hecke eigenvalues for the KZ transport. None of these is stated as a MonoidalCategory.
Missing, in order: (1) the category D_ℏ itself: objects = fin-dim gl2-reps (or a skeletal model V^{⊗n}), hom = gl2-equivariant maps, ⊗ = vector tensor, associator α_{X,Y,Z} = Φ_KZ(ℏ t_{XY}, ℏ t_{YZ}) acting on X⊗Y⊗Z — requires Φ as a natural iso for ARBITRARY objects (current Φ is for fixed residue matrices), naturality in X,Y,Z, and the Mathlib pentagon in the form (α ▷ W) ≫ α ≫ (X ◁ α) = α ≫ α, translated from the matrix pentagon (needs: Φ functorial under equivariant maps; coproduct identities Φ(t12+t13, t23) etc. — the 'Res.Rel' data must be instantiated from actual Casimir tensors and the infinitesimal braid relations proved for them); unitors trivial (Φ(0,·) = 1). (2) Braiding β_{X,Y} = flip ∘ e^{iπℏ t_{XY}} and Mathlib's two hexagons from KZHexagon.hexagon (with the sign/convention matching Mathlib's braiding_tensor_right/left). (3) Duals: RightRigidCategory needs ExactPairing (η, ε) for each X with zigzags *with respect to the KZ associator* — the classical ev/coev do not satisfy the zigzag in D_ℏ; they must be corrected by a scalar/element built from Φ (Drinfeld's ν = Φ-contraction), and that ν must be shown invertible. (4) Twist θ_X = e^{iπℏ C_X} (C = Casimir), with BalancedCategory.twist_tensor (θ_{X⊗Y} = β β (θ⊗θ): Casimir identity C_{X⊗Y} = C_X + C_Y + 2 t_{XY} plus the monodromy β_{Y,X}β_{X,Y} = e^{2πiℏ t} conjugated by associators) and twist_dual (C_{Xᘁ} = C_X, plus compatibility with the corrected ε). (5) Linear structure over ℂ and End(𝟙) = ℂ. Steps (3)–(4) are the substantive missing mathematics; (1)–(2) are packaging of existing matrix identities but still need the infinitesimal braid relations for actual gl2 Casimir tensors stated as Res.Rel. Still open; do not close.

## 2026-10-12 — progress, PR #7743 (branch claude/drinfeld-category-dhbar-2026-10-12). Everything below is sorry-free, compiled lean-direct, and #print axioms gives [propext, Classical.choice, Quot.sound].

**S1 — done.**
- GLnResidues.casimirLeg_eq_flipP: the split gl_n Casimir on legs i≠j is P_ij.
- GLnKZ.kzRes_rel: Res.Rel holds for t_ij = ℏP_ij.
- Non-resonance for ℏ∉ℚ, via a general annihilator-of-ad lemma (GLnResidues.aeval_adL_eq_zero, nonResonant_of_int_roots).
- GLnKZ.pentagon_gln and GLnKZ.hexagon_gln: concrete instances of KZPentagon.pentagon and KZHexagon.hexagon in Matrix (Fin m → Fin n) with the ℓ∞ operator norm.

**S2 prerequisites — done.**
- Shift invariance Φ(A,B+z) = Φ(A,B) = Φ(A+z,B) for z commuting with A and B: KZShift.phiKZ_shift_right/left and KZShiftPhi.Φ_shift_right/left. The proof goes through the formal Euler-operator gauge and Cauchy product with the binomial series E = (1−t)^z. The identity series E t = (1−t)^z is KZShift.series_eq_tpow_one_sub.
- Φ(0,B) = Φ(A,0) = 1 (KZShiftPhi.Φ_zero_left/right).
- Pentagon in Drinfeld coproduct form, Φ^{234}Φ^{1,23,4}Φ^{123} = Φ^{1,2,34}Φ^{12,3,4} (KZShiftPhi.pentagon_drinfeld, for any Res with Rel).
- Functoriality f(Φ(A,B)) = Φ(fA,fB) for continuous ℂ-algebra maps (KZFunctorial.map_Φ). This handles whiskering.
- Non-resonance of ℏT for EVERY integer matrix T when ℏ is transcendental over ℚ (NonResonantInt.nonResonant_smul_intMatrix). This covers block Casimirs of all sizes. Note: the hypothesis changes from ℏ∉ℚ to ℏ transcendental.
- Block Casimirs t_{X,Y} = Σ_{i∈X,j∈Y} P_ij on V^{⊗N}:
  - Res.Rel for any 4 disjoint blocks (BlockResidues.blockRes_rel);
  - pentagon_blocks for any 4-block partition;
  - hexagon_blocks for 3 blocks in central form, e^{-iπA}Φ(C',A)e^{-iπC'}Φ(B,C')e^{-iπB}Φ(A,B) = e^{-iπT}, T = A+B+C' (KZHexagonCentral.hexagon_central).

**Still open, in order.**

(S2/S3 packaging) The Mathlib MonoidalCategory and BraidedCategory instances are not built. The intended design is:
- objects n : ℕ (meaning V^{⊗n});
- Hom = equivariant matrices, i.e. those commuting with the diagonal gl action Σ_i E^{(i)}_ab. For sl2-duals, use sl2-equivariance; the Casimir differs by central scalars, which shift invariance absorbs.
- α_{l,m,k} = reindex(Nat.add_assoc) ∘ Φ(ℏt_{L,M}, ℏt_{M,K}).
- pentagon: from pentagon_blocks after transporting by reindex conjugations (map_Φ).
- hexagons: from hexagon_blocks plus conjugation by block permutations.

This is engineering (casts Fin((l+m)+k) vs Fin(l+(m+k)), and naturality from commute_phiKZ). It is not new mathematics, but it is large and is NOT done.

(S4 duals) A genuine mathematical obstacle.
- The data: for V = ℂ², sl2, ε: V⊗V→1 and η: 1→V⊗V. The zigzag (1⊗ε)∘α_{V,V,V}∘(η⊗1) = ν·id_V, with ν = ⟨σ₂₃|Φ(ℏP12,ℏP23)|σ₁₂⟩ (a singlet overlap: a matrix entry of Φ_KZ on the 2-dim spin-1/2 multiplicity space).
- The exact pairing needs ν ≠ 0, plus the matching scalar for the other zigzag.
- ν ≠ 0 is not a consequence of anything proved. Classically it follows either from the Gauss hypergeometric connection formula (Γ-ratios), or from: ν = 0 ⇒ a KZ solution has pure exponents at 0 and 1 ⇒ after the gauge t^{ℏ}(1−t)^{-ℏ} it is entire with regular growth at ∞, hence a polynomial ⇒ an integrality condition on ℏ. Both need global analytic continuation on ℂ∖{0,1} and behaviour at ∞, which the KZ files do not have.
- A partial observation, NOT formalised: by shift invariance plus conjugation by the cyclic leg permutation π, the hexagon on the multiplicity space becomes (e^{-iπA}π²X)³ = 1 with X = Φ(A,B). This alone does not force ν ≠ 0.

(S5) Twist e^{iπℏC}, twist_tensor and twist_dual depend on S4.

(S6) Blocked on S4.

Do not close.

## 2026-10-12 (later) — S4 done on |ℏ| ≤ 1/12 by the small-ℏ route (PR #7743, commit 2a5bb23674). Sorry-free; #print axioms gives [propext, Classical.choice, Quot.sound].

**SmallHbar.lean — explicit bound on ‖Φ − 1‖.**
- The bound: ‖Φ_KZ(A,B) − 1‖ ≤ (1+δₑ)²(1 + a/(1−3a))(1 + a/(1−4a)) − 1, where ‖A‖, ‖B‖ ≤ a and δₑ = e^{a·log 2} − 1.
- Ingredients: coefficient estimate ‖H_{k+1}‖ ≤ β(1+β)^k with β = a/(1−2a); series bound ‖H(1/2) − 1‖ ≤ a/(1−3a); Neumann-series inverse; exp bound.
- Consequence: norm_Φ_sub_one_lt_half gives ‖Φ − 1‖ < 1/2 for a ≤ 1/12.

**ZigZag.lean — duals for V = ℂ².**
- nonResonant_of_norm_lt: 2‖A‖ < 1 implies non-resonance. So for |ℏ| < 1/2 there is no ℚ or transcendence hypothesis.
- zig_scalar: the zigzag (1⊗ε)Φ(η⊗1) = ν·1. Proof by SL₂-equivariance, via commutation with g^{⊗3} and the two unipotent generators.
- zag_eq_zig: the second zigzag equals the first. Proof by conjugation with P₁₃ plus map_Φ.
- zig_ne_zero: ν ≠ 0 for |ℏ| ≤ 1/12, since zig(1) = −1 and ‖zig Φ − zig 1‖ ≤ 2‖Φ − 1‖ < 1.
- zigzag_identities: with ε' = ν⁻¹ε, both zigzag identities hold exactly.

**Comparison, docstring only (not in any proof).** |ℏ₀| = log q₀/π ≈ 0.0332, which is less than 1/12.

**Caveats.**
- Residues are the gl₂ flips P_ij. The sl₂ Casimir differs by scalars, so its associator is the same Φ by Φ_shift_left/right.
- ε and η are SL₂-equivariant, not GL₂-equivariant. So D_ℏ must use sl₂-equivariant morphisms.

**Still open.**
- S2/S3: Mathlib MonoidalCategory/BraidedCategory packaging (design above).
- S5: twist, twist_tensor, twist_dual.
- S6: the ribbon_hecke application.

Do not close.

## 2026-10-12 (later) — S2 DONE (PR #7743, head 84dca08885). D_ℏ is a Mathlib MonoidalCategory.

**Hypothesis.** instance MonoidalCategory (QOU.KZ.Drinfeld.DH c) for [Fact (Transcendental ℚ c)]. Sorry-free; #print axioms gives [propext, Classical.choice, Quot.sound].

**Construction.**
- Objects: tensor words in V = ℂ² (Obj); legs are Sum types.
- Morphisms: sl₂-equivariant matrices.
- ⊗: Kronecker product.
- Associator: α = reidx(sumAssoc) · Φ_KZ(ℏ t_{X,Y}, ℏ t_{Y,Z}), where t_{X,Y} are block Casimirs (sums of flips).
- Unitors: reindexing.

**Proofs.**
- pentagon_mat: reindexings are moved left with reidx_ΦB (via Φ_intertwine); whiskers are handled by map_Φ through the algebra maps X ↦ X⊗1 and X ↦ 1⊗X; what remains is BlockResidues.pentagon_blocks.
- natural_mat: flip = sl₂ Casimir + 1/2, so the sl₂ block Casimirs are intertwined by tensor products of equivariant maps. The central-scalar shift (Φ_shift_left/right) plus KZIntertwine.Φ_intertwine finish it.
- Triangle: Φ(0,0) = 1.

**Still open, in order.**
- S3: braiding β_{X,Y} = reidx(swap) · e^{iπℏ t_{X,Y}} and the Mathlib hexagons, from hexagon_blocks plus shift invariance.
- S4 packaging: duals for every object, not only V. Note the duals of V exist only for |ℏ| ≤ 1/12 (ZigZag), so D_ℏ with RightRigid needs both |ℏ| ≤ 1/12 and ℏ transcendental, unless non-resonance is handled otherwise.
- S5: twist.
- S6: the ribbon_hecke application.

Do not close.


### 2026-10-12 — S3 DONE: BraidedCategory (DH c), sorry-free
- Braiding β_{X,Y} = reidx(swap)·exp(iπℏ t^{sl}_{X,Y}) (Drinfeld/Braiding.lean): equivariant, invertible, natural. sl₂ residue required (gl₂ scalar ½|X||Y| breaks naturality across word lengths).
- Block hexagon hexagon_sl (Drinfeld/Hexagon.lean) from BlockResidues.hexagon_blocks via KZHexagonCentral.hexagon_rearranged; gl₂/sl₂ scalars central and cancel.
- Matrix hexagons hexagon_fwd_mat / hexagon_rev_mat (reverse = forward block identity with blocks reversed); instance in Drinfeld/Braided.lean.
- #print axioms instBraidedCategoryDH = [propext, Classical.choice, Quot.sound]. Commits 0fa2667266, 3f4d77881f (PR #7743).
- OPEN: S4 rigidity for all objects (ν ≠ 0 currently only for ‖ℏ‖ ≤ 1/12, ZigZag.lean; transcendental ∧ small needed jointly); S5 twist/ribbon; S6.


### 2026-10-13 — S5 + S6 DONE (sorry-free), RibbonDH.lean
- S5: `Linear.lean` (Preadditive/Linear ℂ/MonoidalPreadditive/MonoidalLinear ℂ on DH c); `Twist.lean` (θ_X = exp(iπℏΩ_X), Ω = sl₂ Casimir; natural; θ_{X⊗Y} = (θ_X⊗θ_Y)β_{Y,X}β_{X,Y}); `RibbonDH.lean`: `balanced` (BalancedCategory, ℏ transcendental), `ribbon` (RibbonCategory, + ‖ℏ‖ ≤ 1/12). Ribbon axiom via: invariant pairing ε gives ε(Ω⊗1)=ε(1⊗Ω) ⇒ ε(θ⊗1)=ε(1⊗θ) (`eps_twist`) + mates detected by evaluation (`eq_of_whiskerRight_comp_evaluation`).
- Hecke: `hecke_DH`: s·β_{V,V} − s⁻¹·β⁻¹ = (q−q⁻¹)·𝟙, s=e^{iπℏ/2}, q=e^{iπℏ}. The UNSCALED relation β−β⁻¹ ∈ ℂ·𝟙 is FALSE for every transcendental ℏ (`not_hecke_unscaled`, proved): sl₂ braiding has eigenvalues s on Sym², −s⁻³ on Λ². So ribbon_hecke_qDim_eq_qint_two does not apply verbatim; used `ribbon_hecke_dimension_scaled` (same proof, generic ribbon category).
- S6: `qDim_V_eq_qint_two`: qDimTwistedWith V Vᘁ = (q + q⁻¹)•𝟙_𝟙 in DH c, q = e^{iπℏ}, θ_V = e^{3iπℏ/2} = q^{3/2}; hypotheses Fact(Transcendental ℚ ℏ), Fact(‖ℏ‖ ≤ 1/12) (jointly satisfiable: exists_admissible). #print axioms: propext, Classical.choice, Quot.sound only.
- Still open (stream goal): identification of the KZ braid rep with Jimbo's (β on V^{⊗n} vs Jimbo R-matrix) — this bean's dimension result is one input.

## Parented 2026-11-15 (owner-approved bean triage)

Parent `qou-xhci` → `qou-59vq`. The old parent was missing or absent, so the bean had no epic; this attaches it to the subtree its subject belongs to. No other field changed.

- Round 72 (`lane-e667`): Formalized `qou-sx5r`, `qou-slck`, `qou-dgsw`, `qou-jfr8`, `qou-zoyv` in `QOU.Foundations.SandwichTraceCyclicityVectorBraidingReducedWordSeparationRibbonMonodromy` with 80-dps `mpmath` 2-commit witness stamp (`c95261a9c444144dd0cc07d50ddaabb0b496a13f` -> `c3e4ad1f706f5fd2e70cbb90c8c9bd7753ec1e10`, `scriptHash=e347a9e84468088888c8978781442fc5eb1e2e281357cbff708b7491a3fcbcb8`) in PR `litlfred/qou#8390` (`status: in-progress`).
