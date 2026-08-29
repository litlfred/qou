---
doc_id: arxiv-math-0111205v1
doc_title: "From Subfactors to Categories and Topology II"
section_id: sec-019-41-a-frobenius-algebra-in-c-c-op
section_title: "A Frobenius Algebra in C ⊠ C op"
section_number: 4.1
pages: 17-18
source_pdf: 0111205v1.pdf
source_sha256: 66325a21651aff89
doc_brief: "From Subfactors to Categories and Topology II — For every tensor category C there is a braided tensor category Z(C), the ‘center’ of C."
---
Throughout this section C will be a strict spherical tensor category with simple unit
over an algebraically closed ﬁeld F. We require that C is semisimple with ﬁnite set Γ
of isomorphism classes of simple objects and dim C ⁄= 0. The set Γ has a distinguished
element 0 representing the tensor unit and an involution i ↦→ı which associates with
every class the class of dual objects. We choose representer s {Xi, i ∈ Γ } of these classes,
which are arbitrary except that we require X0 = 1. (We emphasize that we do not require
Xi = Xı. This can be achieved by a suitable strictiﬁcation of the cat egory if and only
if all self-dual objects are orthogonal [5]. (The terms real vs. pseudo-real do not seem
appropriate if F ⁄= C.)) We choose once and for all square roots of the di = d(Xi),
as well as λ =
√
dim C and (dim C)1/4 =
√
λ. Let N k
ij be the dimension of the space
Hom(Xk, XiXj), let {tkα
ij , α = 1, . . . , N k
ij} be a basis in Hom( Xk, XiXj) and let {t′kα
ij } be
the basis in Hom( XiXj, Xk) which is dual in the sense of t′kα
ij ◦ tk,β
ij = δαβ. Note that this
normalization of the dual basis diﬀers from the one provided b y the trace by a factor of
dk. The present choice is more convenient since otherwise the d imensions would appear
in the equation
∑
k,α
tkα
ij ◦ t′kα
ij = idXiXj .
The choice of the of the square roots, the Xi and of the bases {tkα
ij } is immaterial but will
be kept ﬁxed throughout the rest of the paper, and the symbols Γ , Xi, Nk
ij, tkα
ij will keep
the above meanings.
With these preparations we can embark on the 2-categorical a pproach to the quantum
double. We deﬁne
A = C ⊠ Cop, (4.1)
ˆXi = Xi ⊠ X op
i ∈ Obj A. (4.2)
By [38, Lemma 2.9], Cop, C ⊗ F Cop and A are strict spherical in a canonical way. Every
ˆXi, i ∈ Γ is simple and if it is self-dual (i.e. if i = ı) then it is orthogonal irrespective of
whether Xi is orthogonal or symplectic.
The following is a very slight generalization of [30, Propos ition 4.10].
Proposition 4.1 Let F be quadratically closed and let C be F-linear semisimple spherical
with dim C ⁄= 0. There is a normalized canonical Frobenius algebra Q = (Q, v, v′, w, w′) in
A = C ⊠ Cop (with λ1 = λ2 = λ) such that
Q ∼=
⨁
i∈Γ
ˆXi. (4.3)
Proof. Clearly, d(Q) = dim C. By deﬁnition of Q there are morphisms
vi ∈ Hom( ˆXi, Q), v ′
i ∈ Hom(Q, ˆXi), i ∈ Γ ,
such that
v′
i ◦ vj = δijid ˆXi
,
∑
i
vi ◦ v′
i = id Q. (4.4)
17
Deﬁning v = λ1/2v0, v′ = λ1/2v′
0, (2.7) is trivial. With t′kα
ij ∈ HomC(XiXj, Xk) ≡
HomCop(X op
k , Xop
i X op
j ) the morphisms
ˆtk
ij =
N k
ij∑
α=1
tkα
ij ⊠ t′kα
ij ∈ HomA( ˆXk, ˆXi ˆXj)
are independent of the choices of the bases {tkα
ij }. Then
w = λ−1/2 ∑
i,j,k∈Γ
√
didj
dk
vi ⊗ vj ◦ ˆtk
ij ◦ v′
k (4.5)
is in Hom A(Q, Q2), and w′ ∈ HomA(Q2, Q) is deﬁned dually. Eqs. (2.3, 2.4) of Deﬁnition
2.1 are almost obvious. (Use N j
0i = δij). The proof that w, w′ satisfy (2.1, 2.2) and (2.5)
is omitted since it is entirely analogous to the one in [30, p. 591]. Finally, w′ ◦ w = λidQ
is proven by a simple computation observing ˆt′k
ij ◦ ˆtk
ij = N k
ij id ˆXk
and using
∑
i,j
didjN k
ij =
∑
i,j
didjN ı
jk =
∑
j
dkd2
j = dk dim C = dkλ2. (4.6)
Thus ( Q, v, v′, w, w′) is a canonical Frobenius algebra in A. ■
Thus Theorem 2.2 applies and yields a spherical bicategory E. ( E is strict as a bicat-
egory except for the existence of non-trivial unit constrai nts for 1B and strict pivotal [6]
except for isomorphisms γX,Y : Y ◦ X → X ◦ Y which are non-trivial whenever Ran( Y ) =
Src(X) = B.) In particular, we have a spherical tensor category B = EN DE (B). In
the rest of the paper A, Q, E and B will have the above meanings. By construction Q
contains the identity object of A with multiplicity 1, thus J, J and 1B are simple by [38,
Proposition 5.3] and d(J) = d(J ) = λ. (The condition (iii) of that proposition can also
easily be veriﬁed directly.)
Lemma 4.2 dim B = (dim C)2.
Proof. Follows from dim B = dim A and dim A = (dim C)2. The former is [38, Proposition
5.16] and the latter is obvious since the simple objects of C ⊠ Cop are those of the form
X ⊠ Y op with X, Y simple. ■
In the sequel we will write 1 instead of 1op in order to alleviate the notation.
