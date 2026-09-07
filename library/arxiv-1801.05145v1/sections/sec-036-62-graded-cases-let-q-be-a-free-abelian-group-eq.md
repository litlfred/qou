---
doc_id: arxiv-1801.05145v1
doc_title: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS"
section_id: sec-036-62-graded-cases-let-q-be-a-free-abelian-group-eq
section_title: "Graded cases. Let Q be a free abelian group equipped with a symmetric bilinear"
section_number: 6.2
pages: 41-44
source_pdf: 1801.05145v1.pdf
source_sha256: 808da260edd433f7
doc_brief: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS — We prove that the quantum cluster algebra structure of a unipote nt quantum coordinate ring Aq(n(w)), associated with a symmetric Kac-Moody algebra and"
---
form
( , ) : Q × Q → Z such that (β,β ) ∈ 2Z for all β ∈ Q.
42 S.-J. KANG, M. KASHIW ARA, M. KIM, S.-J. OH
We consider a k-linear abelian monoidal category C satisfying (
6.1) and the following
conditions:


















































(i) We have a direct sum decomposition C = ⨁
β∈Q
Cβ such that the
tensor product ⊗ sends Cβ × Cγ to Cβ+γ for every β,γ ∈ Q.
(ii) There exists an object Q ∈ C 0 satisfying
(a) there is an isomorphism
RQ(X) : Q ⊗X ∼− →X ⊗Q
functorial in X ∈ C such that
Q ⊗X ⊗Y
RQ(X)
/d47/d47
RQ(X⊗Y )
/d44/d44
X ⊗Q ⊗Y
RQ(Y )
/d47/d47X ⊗Y ⊗Q
commutes for any X,Y ∈ C ,
(b) the functor X ↦→Q ⊗X is an equivalence of categories.
(iii) for any M, N ∈ C , we have Hom C(M,Q ⊗n ⊗N) = 0 except
ﬁnitely many integers n.
(6.2)
We denote byq the auto-equivalenceQ ⊗ • of C, and call it the grading shift functor .
In such a case the Grothendieck group K(C) is a Q-graded Z[q±1]-algebra: K(C) =⨁
β∈Q
K(C)β where K(C)β =K(Cβ). Moreover, we have
K(C) = ⨁
S
Z[q±1][S],
where S ranges over equivalence classes of simple modules. Here, two simple m odules
S and S′ are equivalent if qnS ≃S′ for some n ∈ Z.
ForM ∈ Cβ, we sometimes write β = wt(M) and call it the weight of M. Similarly,
for x ∈ Q(q1/2) ⊗Z[q±1]K(Cβ), we write β = wt(x) and call it the weight of x.
Deﬁnition 6.2.1. We call a quadruple S = ({Mi}i∈J,L, ~B,D ) a quantum monoidal
seed in C if it satisﬁes the following conditions :
(i) ~B = (bij)i∈J,j ∈Jex is an integer-valued J ×Jex-matrix whose principal part is skew-
symmetric,
(ii) L = (λij)i,j∈J is an integer-valued skew-symmetric J ×J-matrix,
(iii) D = {di}i∈J is a family of elements in Q,
(iv) {Mi}i∈J is a family of simple objects such that Mi ∈ Cdi for any i ∈J,
(v) Mi ⊗Mj ≃qλijMj ⊗Mi for all i,j ∈J,
(vi) Mi1 ⊗ · · · ⊗Mit is simple for any sequence (i1,...,i t) in J,
(vii) The pair (L, ~B) is compatible in the sense of (5.3) with d = 2,
(viii) λij − (di,dj) ∈ 2Z for all i,j ∈J,
MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS 43
(ix)
∑
i∈J
bikdi = 0 for all k ∈Jex.
Let S = ( {Mi}i∈J,L, ~B,D ) be a quantum monoidal seed. For any X ∈ C β and
Y ∈ Cγ such that X ⊗Y ≃qcY ⊗X and c + (β,γ ) ∈ 2Z, we set
~Λ(X,Y ) = 1
2
(
−c + (β,γ )
)
∈ Z
and
X ⊙Y :=q
~Λ(X,Y )X ⊗Y ≃q
~Λ(Y,X )Y ⊗X.
Then X ⊙Y ≃Y ⊙X. For any sequence ( i1,...,i ℓ) in J, we deﬁne
ℓ⨀
s=1
Mis := (· · · ((Mi1 ⊙Mi2) ⊙Mi3) · · ·) ⊙Miℓ.
Then we have
ℓ⨀
s=1
Mis =q
1
2
∑
1≤u<v≤ℓ(−λiu iv +(diu,div ))Mi1 ⊗ · · · ⊗Miℓ.
For any w ∈ Sℓ, we have
ℓ⨀
s=1
Miw(s) ≃
ℓ⨀
s=1
Mis
Hence for any subset A of J and any set of non-negative integers {ma}a∈A, we can
deﬁne ⨀
a∈A
M ⊙ma
a .
For (ai)i∈J ∈ ZJ
≥0 and (bi)i∈J ∈ ZJ
≥0, we have
(⨀
i∈J
M ⊙ai
i
)
⊙
(⨀
i∈J
M ⊙bi
i
)
≃ ⨀
i∈J
M ⊙(ai+bi)
i .
Let S = ( {Mi}i∈J,L, ~B,D ) be a quantum monoidal seed. When the L-commuting
family {[Mi]}i∈J of elements of Z[q±1/2] ⊗Z[q±1]K(C) is algebraically independent, we
shall deﬁne a quantum seed [ S ] in Z[q±1/2] ⊗Z[q±1]K(C) by
[S ] = ( {q−(di,di)/4[Mi]}i∈J,L, ~B).
Set
Xi :=q−(di,di)/4[Mi].
Then for any a = (ai)i∈J ∈ ZJ
≥0, we have
X a =q−(µ,µ)/4[⨀
i∈J
M ⊙ai
i ],
where µ = wt( ⨀
i∈J
M ⊙ai
i ) = wt(X a) = ∑
i∈Jaidi.
44 S.-J. KANG, M. KASHIW ARA, M. KIM, S.-J. OH
For a given k ∈ Jex, we deﬁne the mutation µk(D) ∈ QJ of D in direction k with
respect to ~B by
µk(D)i =di (i ⁄=k), µ k(D)k = −dk +
∑
bik>0
bikdi.
Note that
µk(µk(D)) = D.
Note also that (µk(L),µk( ~B),µk(D)) satisﬁes conditions (viii) and (ix) in Deﬁnition 6.2.1
for any k ∈Jex.
We have the following
Lemma 6.2.2. Set X ′
k =µk(X)k, the mutation of Xk as in (5.6). Set ζ = wt(X ′
k) =
−dk + ∑
bik>0bikdi. Then we have
qmk[Mk]q(ζ,ζ )/4X ′
k =q[ ⨀
bik>0
M ⊙bik
i ] + [ ⨀
bik<0
M ⊙(−bik)
i ],
qm′
kq(ζ,ζ )/4X ′
k[Mk] = [ ⨀
bik>0
M ⊙bik
i ] +q[ ⨀
bik<0
M ⊙(−bik)
i ],
where 








mk = 1
