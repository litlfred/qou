---
doc_id: arxiv-math-9909088v1
doc_title: "The Gauss Map and a Noncompact Riemann-Roch Formula for Constructible Sheaves on Semiabelian Varieties"
section_id: page-007
section_title: "Page 7"
section_number: null
pages: 7-7
source_pdf: 9909088v1.pdf
source_sha256: 52cfb568951f195f
toc_source: undetermined
doc_brief: "The Gauss Map and a Noncompact Riemann-Roch Formula for Constructible Sheaves on Semiabelian Varieties — For an irreducible subvariety Z in an algebraic group G we deﬁne an integer gdeg(Z) ≥0 as the"
---
NONCOMPACT RIEMANN-ROCH
7
Proof of Theorem 1.3 in general
Let A be an abelian variety. We recall some elementary properties of line bundles
on A, see [10] [16]. If L is such a bundle, by La, a ∈A we denote its ﬁber at a.
By L0 we denote the total space of L with the zero section deleted, so L0 is a
principal C∗-bundle on A. As for any base variety, the correspondence L 7→L0
is an equivalence between the category of line bundles and isomorphisms and the
category of principal C∗-bundles.
Assume that L has degree 0.
Then the theorem of the square [16] provides
identiﬁcations
L0 ∼= C , La ⊗Lbg
−→La+b
which make L0 into a group, namely a semiabelian variety ﬁtting into an extension
(5.1)
0 →C∗→L0
p
−→A →0.
Next, any bundle L of degree 0 has a ﬂat connection. All such connections form
an aﬃne space Conn(L) over the vector space H0(A, Ω1) = a∗. Here a is the Lie
algebra of A. Let L be the Lie algebra of the group L0, so that we have the exact
sequence
(5.2)
0 →a∗→L∗
π
−→C →0.
Denote by eL = p∗L the pullback of L to L0. For any ∇∈Conn(L) let e∇be its
pullback to a connection in eL. Denote also by f the tautological section of eL over
L0 (given by the identity map).
(5.3) Proposition. The 1-forms e∇log f, ∇∈Conn(L), are invariant (with re-
spect to the group structure on L0). Their images in L∗under the evaluation at 0
form the subspace π−1(1), where π is as in (5.2).
Proof: Let us ﬁrst show the invariance. Note that e∇log f is just the Lie algebra-
valued 1-form on the total space of the principal C∗-bundle L0, describing the
connection ∇in L0 in the standard approach of diﬀerential geometry. So its in-
variance follows from the fact that the line bundle (L, ∇) (or, what is equivalent,
the C∗-bundle (L0, ∇)) satisﬁes the theorem on the square as a bundle with con-
nection. More precisely, if m, q1, q2 : A × A →A are the group structure and the
two projections, then the isomorphism
µ : q∗
1L ⊗q∗
2L →m∗L
given by the theorem on the square is an isomorphism of bundles with connection.
In particular, the induced isomorphism µa : La ⊗L →l∗
aL is an isomorphism of
bundles with connection on A. But the translation l(a,λ), λ ∈La \ {0} on L0 is
just given by µa(λ ⊗−). This shows the invariance. As for the second assertion
of Proposition 5.3, it is again obvious from the interpretation of eλ log f as the Lie
algebra-valued 1-form describing the connection and the identiﬁcation L0
0 = C∗.
(5.4) Corollary. The 1-forms se∇log f, s ∈C∗, ∇∈Conn(L), form a nonempty
Zariski open set in the space of all invariant 1-forms on L0.
Consider now several line bundles of degree 0, say L1, . . . , Ln, on A, and let
(5.5)
0 →(C∗)n →G = L0
1×A . . . ×AL0
n
p
−→A →0
