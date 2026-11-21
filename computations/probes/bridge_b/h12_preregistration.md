# H12 pre-registration: a graded strand model for the folded descent (2026-11-21, written before any computation)

Goal: a strand-level model whose mirror-twisted trace of a doubled word reproduces Lusztig §16.7(b): folded bulk letter with spectrum {q², −q⁻²} (H11 showed a plain swap gives {q², q⁻²}).

Model G: grade V = C² by the eigenlines of σ, with the −q⁻¹ line odd (the sign line; Lusztig's normalisation ε_{l̃(x)} = 1 in 16.4 fixes the even line to carry v^{l̃}). The doubled letter is σ⊗σ followed by the Koszul sign S(e_i⊗e_j) = (−1)^{|i||j|}; the descent is the trace twisted by the mirror swap P.

Pass criteria, all required:
1. tr(P·b^k) = q^{2k} + (−q⁻²)^k for k = 1..6 (one letter).
2. The swapped (mixed) lines contribute zero to every twisted trace (Lusztig 16.1(b)).
3. For two commuting doubled letters on V^{⊗4} with mirror swap, the twisted trace of words in b₁, b₂ equals the product of the one-letter Lusztig traces (factorisation, k₁, k₂ = 0..3).
4. The opposite grading (q line odd) must FAIL 1, so the grading is fixed by the normalisation, not chosen.

Out of scope here: a graded representation of the full six-strand H_6(q) with non-commuting letters and the wall; V³. If 1–4 pass, that is the next step. No D value is adopted from H12.
