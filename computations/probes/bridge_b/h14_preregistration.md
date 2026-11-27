# H14 pre-registration: whole-word (KL-basis) signs for the folded descent (2026-11-21, before any computation)

H13 showed a sign per crossing fails. Lusztig §16.4–16.6 puts the sign on each element x of the fixed group: [B_x, φ_x] maps to the folded KL basis element, with coefficients f_{y,x} = ṗ_{y,x} given by the ι-twisted trace on the graded spaces whose dimensions are the ambient KL coefficients.

Setup. Ambient W̃ = S₆, generators s₁…s₅, ι: s_j ↔ s_{6−j} (conjugation by w₀). Fixed group W (order 48, type B₃) with generators τ = s₃, b₁ = s₂s₄, b₂ = s₁s₅ and weights L = ambient length: L(τ) = 1, L(b₁) = L(b₂) = 2. Same indeterminate v on both sides (16.6). KL bases computed independently on each side, by the bar-invariance algorithm with c_s = T_s + v^{−L(s)}.

Testable consequences (ι² = 1, so a twisted trace on a space of dimension d is an integer ≡ d mod 2 with absolute value ≤ d):
1. For every pair y ≤ x in W: each coefficient of the folded p_{y,x}(v) is ≡ the matching coefficient of the ambient p̃_{y,x}(v) mod 2, and has absolute value ≤ it.
2. If 1 holds, report where the two differ. Those positions are where the whole-word sign ε is not +1, i.e. where a naive "keep the ambient coefficient" descent is wrong.
3. Control: the equal-parameter folded algebra (all L = 1) must fail 1 somewhere, otherwise the test does not discriminate between weightings.

If 1 and 3 pass, the descent map on the KL basis (c̃_x ↦ c_x for x ∈ W, swapped pairs ↦ 0, signs from 2) is the strand-level model of Lusztig's descent, and by 16.7 it sends each doubled letter to T_b with eigenvalues {v², −v⁻²} = {q², −q⁻²}, i.e. reading B. No new D is computed; D stays a trace ratio, not a mass.
