# H16 pre-registration: the six-strand V³ word through the KL descent (2026-11-21, before any computation)

Inputs: ambient H̃ = H(S₆) at generic v (= q), T-basis, exact Laurent integers. Fixed group W ≅ B₃ with τ = s₃, b₁ = s₂s₄, b₂ = s₁s₅, L = (1, 2, 2). KL bases from H14.

Words. Closed X_T = (T̃_{s₂}T̃_{s₄}·(T̃_{s₁}T̃_{s₅})⁻¹)³ (the H9 doubled V³). Open X_B = T̃_{s₃}·X_T (wall at slot 0).
Folded words, computed directly in H(W, L): Z_T = (T_{b₁}T_{b₂}⁻¹)³, Z_B = T_τ·Z_T.

Naive descent Φ: expand X in the ambient KL basis, drop x ∉ W, send c̃_x ↦ c_x. This is the untwisted projection; Lusztig's twisted descent (§16.7) sends the doubled word to Z.

Criteria:
1. Mod-2 test: the c-basis coefficients of Φ(X) and of Z agree mod 2, coefficientwise, for both closed and open words. (Swapped pairs contribute in pairs; twisted multiplicities ≡ ordinary ones mod 2.)
2. Report whether Φ(X) = Z. The expectation is that they differ: that difference is exactly what the whole-word signs remove.
3. Evaluation. The H8 representation is bulk Jimbo Ř at Q_b = v² on (C²)^{⊗3}, wall 𝒦 = [[s, 1], [1, 0]] on strand 1 with s = v − v⁻¹, and pivot K = diag(v², v⁻²). Sanity first: the type-B relations hold in it, i.e. bulk braid, the wall quadratic and 𝒦₁Ř₁𝒦₁Ř₁ = Ř₁𝒦₁Ř₁𝒦₁. Then D from the H8 weight-space traces at v = q₀:
   - D(Z) must reproduce reading B, 0.94911520554914481986, to 20 digits;
   - report D(Φ(X)), the naive descent.
No D is adopted. D is a trace ratio, not a mass.
