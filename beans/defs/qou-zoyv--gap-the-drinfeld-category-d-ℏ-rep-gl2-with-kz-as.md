---
# qou-zoyv
title: 'GAP: the Drinfeld category D_ℏ (Rep gl2 with KZ associator) is a ribbon category'
status: todo
type: task
priority: normal
created_at: 2026-10-12T18:13:09Z
updated_at: 2026-10-12T19:14:28Z
parent: qou-xhci
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
