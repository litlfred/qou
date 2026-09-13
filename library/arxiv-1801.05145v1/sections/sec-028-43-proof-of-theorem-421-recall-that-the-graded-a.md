---
doc_id: arxiv-1801.05145v1
doc_title: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS"
section_id: sec-028-43-proof-of-theorem-421-recall-that-the-graded-a
section_title: "Proof of Theorem 4.2.1. Recall that the graded algebra R(β) (β ∈ Q+) is"
section_number: 4.3
pages: 36-37
source_pdf: 1801.05145v1.pdf
source_sha256: 808da260edd433f7
doc_brief: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS — We prove that the quantum cluster algebra structure of a unipote nt quantum coordinate ring Aq(n(w)), associated with a symmetric Kac-Moody algebra and"
---
geometrically realized as follows ([ 40]). There exist a reductive group G and a G-
equivariant projective morphism f : X → Y from a smooth algebraic G-varietyX to
an aﬃne G-varietyY deﬁned over the complex number ﬁeld C such that
R(β) ≃ ~EndDb
G(kY )(Rf∗(kX[dimX])) as a graded k-algebra.
Here, D b
G(kY ) denotes the G- equivariant derived category of the G-variety Y with
coeﬃcient k, and ~EndDb
G(kY )(K) = ~HomDb
G(kY )(K,K ) with
~HomDb
G(kY )(K,K ′) := ⨁
n∈Z
HomDb
G(kY )(K,K ′[n]).
We denote by kX[dimX] the direct sum of the constant sheaves on each connected
components of X, all of which are shifted by their dimensions. By the decomposition
theorem ([ 1]), we have a decomposition
Rf∗(kX [dimX]) ≃ ⨁
a∈J
Ea ⊗ Fa,
MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS 37
where {Fa}a∈J is a ﬁnite family of simple perverse sheaves on Y and Ea is a non-zero
ﬁnite-dimensional graded k-vector space such that
Hk(Ea) ≃H −k(Ea) for any k ∈ Z.(4.1)
The last fact ( 4.1) follows from the hard Lefschetz theorem ([ 1]).
Set Aa,b = ~HomDb
G(kY )(Fb, Fa). Then we have the multiplication morphisms
Aa,b ⊗Ab,c →Aa,c
so that
A := ⨁
a,b∈J
Aa,b
has a structure of Z-graded algebra such that
A≤0 := ⨁
n≤0
An =A0 ≃ kJ.
Hence the family of the isomorphism classes of simple objects (up to a grading shift)
inA-gmod is {ka}a∈J . Here, ka is the module obtained by the algebra homomorphism
A →A≤0 ≃ kJ → k, where the last arrow is the a-th projection. Hence we have
K(A-gmod) ≃ ⨁
a∈J
Z[q±1][ka].
On the other hand, we have
R(β) ≃ ⨁
a,b∈J
Ea ⊗Aa,b ⊗E∗
b.
Set
L := ⨁
a,b∈J
Ea ⊗Aa,b.
Then, L is endowed with a natural structure of ( ⨁
a,b∈J
Ea ⊗Aa,b ⊗E∗
b,A )-bimodule. It
is well-known that the functor M ↦→L ⊗AM gives a graded Morita-equivalence
Φ : A-gmod ∼− →R(β)-gmod.
Note that Φ( ka) ≃Ea and {Ea}a∈J is the set of isomorphism classes of self-dual simple
graded R(β)-modules by ( 4.1).
By the above observation, in order to prove the theorem, it is enou gh to show the
corresponding statement for the graded ring A, which is obvious.
