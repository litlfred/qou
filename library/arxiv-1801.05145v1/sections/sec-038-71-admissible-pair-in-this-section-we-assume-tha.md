---
doc_id: arxiv-1801.05145v1
doc_title: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS"
section_id: sec-038-71-admissible-pair-in-this-section-we-assume-tha
section_title: "Admissible pair. In this section, we assume that R is a symmetric KLR algebra"
section_number: 7.1
pages: 45-48
source_pdf: 1801.05145v1.pdf
source_sha256: 808da260edd433f7
doc_brief: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS — We prove that the quantum cluster algebra structure of a unipote nt quantum coordinate ring Aq(n(w)), associated with a symmetric Kac-Moody algebra and"
---
over a base ﬁeld k.
46 S.-J. KANG, M. KASHIW ARA, M. KIM, S.-J. OH
From now on, we focus on the case when C is a full subcategory of R-gmod stable
under taking convolution products, subquotients, extensions an d grading shift. In
particular, we have
C = ⨁
β∈Q−
Cβ, where Cβ := C ∩R(−β)-gmod,
and we have the grading shift functor q on C. Hence we have
K(Cβ) ⊂U −
q (g)β,
and K(C) has a Z[q±1]-basis consisting of the isomorphism classes of self-dual simple
modules.
Deﬁnition 7.1.1. A pair ({Mi}i∈J, ~B) is called admissible if
(i) {Mi}i∈J is a family of real simple self-dual objects of C which commute with each
other,
(ii) ~B is an integer-valued J ×Jex-matrix with skew-symmetric principal part,
(iii) for each k ∈Jex, there exists a self-dual simple object M ′
k of C such that there is
an exact sequence in C
0 →q ⨀
bik>0
M ⊙bik
i →q
~Λ(Mk,M ′
k)Mk ◦M ′
k → ⨀
bik<0
M ⊙(−bik)
i → 0,(7.1)
and M ′
k commutes with Mi for any i ⁄=k.
Note that M ′
k is uniquely determined by k and ({Mi}i∈J, ~B). Indeed, it follows from
q ~Λ(Mk,M ′
k)Mk ∇M ′
k ≃ ⨀
bik<0
M ⊙(−bik)
i and [ 15, Corollary 3.7]. Note also that if there is
an epimorphism qmMk ◦M ′
k ։ ⨀
bik<0
M ⊙(−bik)
i for some m ∈ Z, then m should coincide
with ~Λ(Mk,M ′
k) by Lemma 3.1.4 and Lemma 3.2.7.
For an admissible pair ( {Mi}i∈J, ~B), let Λ = (Λ ij)i,j∈J be the skew-symmetric matrix
given by Λ ij = Λ(Mi,Mj). and let D = {di}i∈J be the family of elements of Q− given
bydi = wt(Mi).
Now we can simplify the conditions in Deﬁnition 6.2.1 and Deﬁnition 6.2.3 as follows.
Proposition 7.1.2. Let ({Mi}i∈J, ~B) be an admissible pair in C, and let M ′
k (k ∈Jex)
be as in Deﬁnition 7.1.1. Then we have the following properties.
(a) The quadruple S := ({Mi}i∈J, −Λ, ~B,D ) is a quantum monoidal seed in C.
(b) The self-dual simple object M ′
k is real for every k ∈Jex.
(c) The quantum monoidal seed S admits a mutation in each direction k ∈Jex.
(d) Mk and M ′
k are simply-linked for any k ∈Jex (i.e., d(Mk,M ′
k) = 1) .
MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS 47
(e) For any j ∈J and k ∈Jex, we have
Λ(Mj,M ′
k) = −Λ(Mj,Mk) − ∑
bik<0 Λ(Mj,Mi)bik,
Λ(M ′
k,Mj) = −Λ(Mk,Mj) + ∑
bik>0 Λ(Mi,Mj)bik.(7.2)
Proof. (d) follows from the exact sequence ( 7.1) and Lemma 3.2.18.
(b) follows from the exact sequence ( 7.1) by applying Corollary 3.2.21 to the case
M =Mk, N =M ′
k, X =q ⨀
bik>0
M ⊙bik
i and Y = ⨀
bik<0
M ⊙(−bik)
i .
(e) follows from
Λ(Mj,Mk) + Λ(Mj,M ′
k) = Λ( Mj,Mk ∇M ′
k) = Λ
(
Mj, ⨀
bik<0
M ⊙(−bik)
i
)
=
∑
bik<0
Λ(Mj,Mi)(−bik)
and
Λ(Mk,Mj) + Λ(M ′
k,Mj) = Λ( M ′
k ∇Mk,Mj) = Λ
(⨀
bik>0
M ⊙bik
i ,Mj
)
=
∑
bik>0
Λ(Mi,Mj)bik.
Let us show ( a). The conditions (i)–(v) in Deﬁnition 6.2.1 are satisﬁed by the
construction. The condition (vi) follows from Proposition 3.2.5 and the fact that Mi
is real simple for every i ∈ J. The condition (viii) is nothing but Lemma 3.1.2. The
condition (ix) follows easily from the fact that the weights of the ﬁrs t and the last
terms in the exact sequence ( 7.1) coincide.
Let us show the condition (vii) in Deﬁnition 6.2.1. By ( 7.2) and ( d) of this proposi-
tion, we have
2δjk = 2 d(Mj,M ′
k) = −2 d(Mj,Mk) −
∑
bik<0
Λ(Mj,Mi)bik +
∑
bik>0
Λ(Mi,Mj)bik
= −
∑
bik<0
Λ(Mj,Mi)bik −
∑
bik>0
Λ(Mj,Mi)bik = −
∑
i∈J
Λ(Mj,Mi)bik
for k ∈Jex and j ∈J. Thus we have shown that S is a quantum monoidal seed in C.
Let us show ( c). Let k ∈ Jex. The exact sequence ( 6.4) follows from ( 7.1) and the
equality
~Λ(Mk,M ′
k) = 1
2
(
(wt(Mk,M ′
k) −
∑
bik<0
Λ(Mk,Mi)bik
)
=mk,(7.3)
48 S.-J. KANG, M. KASHIW ARA, M. KIM, S.-J. OH
which is an immediate consequence of ( 7.2).
Similarly, taking the dual of the exact sequence ( 7.1), we obtain an exact sequence
0 → ⨀
bik<0
M ⊙(−bik)
i →q−~Λ(Mk,M ′
k)+(wtMk,wtM ′
k)M ′
k ◦Mk →q−1 ⨀
bik>0
M ⊙bik
i → 0,
which gives the exact sequence ( 6.5).
It remains to prove that µk(S ) := ( {Mi}i⁄=k ∪ {M ′
k},µk(−Λ),µk( ~B),µk(D)) is a
quantum monoidal seed in C for any k ∈Jex.
We see easily that µk(S ) satisﬁes the conditions (i)–(iv) and (vii)–(ix) in Deﬁni-
tion 6.2.1.
For the condition (v), it is enough to show that for i,j ∈J we have
µk(−Λ)ij = −Λ(µk(M)i,µk(M)j),
whereµk(M)i =Mi fori ⁄=k andµk(M)k =M ′
k. In the case i ⁄=k andj ⁄=k, we have
µk(−Λ)ij = −Λ(Mi,Mj) = −Λ(µk(Mi),µk(Mj)).
The other cases follow from ( 7.2).
The condition (vi) in Deﬁnition 6.2.1 for µk(S ) follows from Proposition 3.2.5 and
the fact that {µk(M)i}i∈J is a commuting family of real simple modules. □
Now we are ready to give one of our main theorems.
Theorem 7.1.3. Let ({Mi}i∈J, ~B) be an admissible pair in C and set
S = ({Mi}i∈J, −Λ, ~B,D )
as in Proposition 7.1.2. We set [S ] := ( {q− 1
