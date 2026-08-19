---
doc_id: arxiv-hep-th-0001202v2
doc_title: "Towards cohomology of renormalization: bigrading the combinatorial Hopf algebra of rooted trees"
section_id: sec-001-2-the-second-grading
section_title: "The second grading"
section_number: 2
pages: 3-4
source_pdf: 0001202v2.pdf
source_sha256: b2e3e22ea3d51c0b
doc_brief: "Towards cohomology of renormalization: bigrading the combinatorial Hopf algebra of rooted trees — The renormalization of quantum ﬁeld theory twists the antipode of a non- cocommutative Hopf algebra"
---
The weight n of a rooted tree t is the number of its nodes. The weight of a forest F =
∏
j tj
is the sum of the weights of the trees tj in the product. This is the ﬁrst grading.
To deﬁne the index k for the second grading, k-primitivity, we use k-fold iterations of
the coproduct ∆, deﬁned by the highly nontrivial recursion [1]
∆( t) = t ⊗ e + (id ⊗ B+) ◦ ∆ ◦ B−(t) (3)
for a nonempty tree t. Here e is the empty tree, evaluating to unity, id is the identity map,
B− removes the root of t, and B+ combines the trees of a product by appending them
to a common root. The coproduct ∆ is coassociative. Hence it has a u nique iteration,
which may be written in a variety of equivalent ways. Since ∆ has only sin gle trees on
the right, the recursion
∆ k = (id ⊗ ∆ k−1) ◦ ∆ (4)
is particularly convenient. For a forest F =∏
j tj we have ∆ k(F ) = ∏
j ∆ k(tj).
Let X be a Q-linear combination of monomials of trees, i.e. of forests. We say tha t X
is k-primitive if every term of ∆ k(X) has at least one empty tree e. Symbolically we may
2
consider the composition of tensor products of the projection op erator P := id −E ◦ ¯e with
iterations of ∆. P projects onto the augmentation ideal Hc = {X ∈ H R | P (X) = X},
where X = P (X) + E ◦ ¯e(X). Here ¯e is the counit, which annihilates everything except
the empty tree, for which it gives ¯ e(e) = 1. The map from the rationals back to the
algebra is simply E(q) = qe for q ∈ Q. Hence P annihilates e and leaves everything else
unchanged. Let U0 := P and
Uk := (P ⊗ . . . ⊗ P/bracehtipupleft /bracehtipdownright/bracehtipdownleft /bracehtipupright
k+1 times
) ◦ ∆ k = (P ⊗ Uk−1) ◦ ∆ (5)
for k > 0. In using the recursive form, note should be taken that, in gener al, the projection
makes Uk(X1X2) ⁄= Uk(X1)Uk(X2): one should store results for forests; not just for trees.
We have said that X is k-primitive if Uk(X) = 0. Then clearly X is ( k + 1)-primitive,
since ∆ k+1(X) has at least two empty trees e in every term. We are interested in the
number, Hn,k := Dn,k − Dn,k −1, of weight-n terms that are k-primitive but are not ( k − 1)-
primitive, where Dn,k is the dimension of the subspace with weight n and index k. To
compute Dn,k for speciﬁc (and rather modest) values of n, k one considers the most general
linear combination X of weight-n terms, with unknown coeﬃcients, and solves Uk(X) = 0.
The rank deﬁciency of this large system of linear equations is Dn,k . From this one subtracts
the number Dn,k −1 of weight-n terms that are ( k−1)-primitive. By this means we obtained
the ﬁrst 7 rows of Tables 1 and 2, for the Hopf subalgebras Hladder and HCM, and inferred
their generating principles. In the case of the full Hopf algebra HR, bigraded in Table 3,
data were much harder to obtain. Fortunately the generating prin ciple is very distinctive.
