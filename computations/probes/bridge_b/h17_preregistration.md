# H17 pre-registration: the descent at n = 4 and n = 5 (2026-11-21, before any computation)

Question. H16 checked Lusztig's twisted descent on the six-strand V³ word. Does the same descent behave the same way at n = 4 (wall of weight 1) and n = 5 (wall of weight 3, the case the wording fix to conj:type-b-folding-cpt added)?

Folding (from H15). Both fold to B₂, with one bulk generator b and one wall generator w:
- n = 4: b = s₁s₃ (L = 2), w = s₂ (L = 1).
- n = 5: b = s₁s₄ (L = 2), w = s₂s₃s₂ (L = 3).

Word. B₂ has only one bulk generator, so the two-bulk-letter V³ = (σ₀σ₁⁻¹)³ of H16 has no counterpart here. The pre-registered stand-in is the chiral cube in the two folded generators, Z = (T_b T_w⁻¹)³, computed directly in H(B₂, L). Its ambient double X is the same word with each folded letter replaced by its ambient reduced word: T_b = T_{s₁}T_{s₃} (or T_{s₁}T_{s₄}), T_w = T_{s₂} (or T_{s₂}T_{s₃}T_{s₂}), and inverses reversed. This is a stand-in, not the photon vertex. Only the descent's behaviour is tested.

Naive descent Φ is as in H16: expand X in the ambient KL basis, drop x ∉ W, and send c̃_x to c_x.

Criteria:
1. Φ(X) ≡ Z mod 2, coefficientwise in the folded KL basis, at n = 4 and n = 5. This is the pass/fail test.
2. Report whether Φ(X) = Z, and how many ambient KL terms are swapped.
3. Representation check, reported, not pass/fail. Take bulk Ř at Q_b = v² on (C²)^{⊗2} and the wall 𝒦 = [[s, 1], [1, 0]] ⊗ 1 with s = v^L − v^{−L}. Check the wall quadratic and the B₂ relation 𝒦Ř𝒦Ř = Ř𝒦Ř𝒦, at L = 1 and at L = 3. If the relation fails at L = 3, this two-strand model has no weight-3 wall. That is a finding about the model, and no trace is reported for that case. If it holds, report the K²-weighted weight-space traces of Z and Φ(X) at q₀ and at q → 1. No D is formed: two strands carry no n/p split. Nothing is compared with experiment.

What would count against the wording fix: criterion 1 failing at n = 5.
