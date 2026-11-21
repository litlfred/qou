---
doc_id: arxiv-math-0304010v1
doc_title: "Kerov's central limit theorem for the Plancherel measure on Young diagrams"
section_id: page-025
section_title: "Page 25"
section_number: null
pages: 25-25
source_pdf: 0304010v1.pdf
source_sha256: fc2296c027b3feb0
toc_source: undetermined
doc_brief: "Kerov's central limit theorem for the Plancherel measure on Young diagrams — Consider random Young diagrams with ﬁxed number n of boxes, dis- tributed according to the Plancherel measure Mn."
---
Corollary 4.13 (of the proof). Let σ and τ be two partitions with no common
part, i.e., for any i = 1, 2, . . ., at least one of the multiplicities mi(σ), mi(τ)
vanishes. Then
p#
σ p#
τ = p#
σ∪τ + ⟨terms of lower degree deg1( · )⟩.
Proof. Let ρ, X1, X2 be as in the beginning of the proof of Proposition 4.12.
Recall the claim stated in the second paragraph of that proof: either X1 ∩X2 = ∅
or X1 ∩X2 entirely consists of common nontrivial cycles of the permutations s1
and s−1
2 . The second possibility contradicts the assumption that σ and τ have no
common part. Hence the ﬁrst possibility holds, which means that ρ = σ ∪τ. We
know that the corresponding coeﬃcient f ρ
στ equals 1, which concludes the proof.
□
§5. The Plancherel measure and the law of large numbers
Consider the set Yn of Young diagrams with n boxes, n = 1, 2, . . ., and equip it
with the measure Mn, deﬁned by
Mn(λ) = dim2 λ
n!
,
λ ∈Yn .
This is a probability measure, because, by Burnside’s theorem,
X
λ∈Yn
dim2 λ = |Sn| = n!.
It is called the Plancherel measure, see [VeK1], [VeK2], [VeK3] for more details.
Given a function f on Yn , we deﬁne by ⟨f⟩n its expectation with respect to Mn.
That is,
⟨f⟩n =
X
λ∈Yn
f(λ)Mn(λ) = 1
n!
X
λ∈Yn
f(λ) dim2 λ.
If f is a function on the whole set Y, we write ⟨f⟩n instead of ⟨f |Yn⟩n . We shall
use this convention for functions f ∈A. In this way we get the family of linear
functionals ⟨· ⟩n , n = 1, 2, . . ., on the algebra A. These functionals have a very
simple form on the basis {p#
ρ }.
Proposition 5.1. For any partition ρ,
⟨p#
ρ ⟩n =
 n↓r,
ρ = (1r),
r = 1, 2, . . .,
0,
ρ̸ = (1r).
Proof. Set r = |ρ|. If n < r then p#
ρ vanishes on Yn, which agrees with the formula
in question, because n↓r = 0 whenever n < r.
Assume n ≥r. By the deﬁnition of p#
ρ , see Deﬁnition 4.1,
⟨p#
ρ ⟩n = n↓r · 1
n! ·
X
λ∈Yn
χλ
ρ∪1n−r dim λ.
Remark that the sum above equals the value of the regular character (i.e., the
character of the regular representation of Sn) on the conjugacy class ρ ∪1n−r.
But the regular character is the delta function at {e} ⊂Sn , multiplied by n!.
Therefore, the sum in question vanishes unless ρ ∪1n−r is the trivial class (i.e., ρ
itself is trivial, ρ = (1r)), in which case the sum equals n!. Consequently, we get
n↓r.
□
25
