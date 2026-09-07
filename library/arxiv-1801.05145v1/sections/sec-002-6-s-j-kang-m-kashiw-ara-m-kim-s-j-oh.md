---
doc_id: arxiv-1801.05145v1
doc_title: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS"
section_id: sec-002-6-s-j-kang-m-kashiw-ara-m-kim-s-j-oh
section_title: "S.-J. KANG, M. KASHIW ARA, M. KIM, S.-J. OH"
section_number: 6
pages: 6-8
source_pdf: 1801.05145v1.pdf
source_sha256: 808da260edd433f7
doc_brief: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS — We prove that the quantum cluster algebra structure of a unipote nt quantum coordinate ring Aq(n(w)), associated with a symmetric Kac-Moody algebra and"
---
precisely, there exists a family of algebras {R(−β)}β∈Q− such that the Grothendieck
ring of R-gmod := ⨁
β∈Q−R(−β)-gmod, the direct sum of the categories of ﬁnite-
dimensional graded R(−β)-modules, is isomorphic to the integral form Aq(n)Z[q±1] of
Aq(n) ≃U −
q (g). Here the tensor functor ⊗ of the monoidal category R-gmod is given
by the convolution product ◦, and the action of q is given by the grading shift functor.
In [
40, 39], Varagnolo-Vasserot and Rouquier proved that the upper global basis Bup of
Aq(n) corresponds to the set of the isomorphism classes of all self-dual simple modules
ofR-gmod under the assumption that R is associated with a symmetric quantum group
Uq(g) and the base ﬁeld is of characteristic 0.
Combining works of [ 11, 23, 40], the unipotent quantum coordinate ring Aq(n(w))
associated with a symmetric quantum group Uq(g) and a Weyl group element w is
isomorphic to the Grothendieck group of a monoidal abelian full subc ategory Cw of
R-gmod whose base ﬁeld k is of characteristic 0, satisfying the following properties :
(i) Cw is stable under extensions and grading shift functor, (ii) the compo sition factors
of M ∈ C w are contained in Bup(w) (see Deﬁnition 11.2.1). In particular, the ﬁrst
condition in ( 0.1) holds. However, it is not evident that the second and the third
condition in ( 0.1) on quantum monoidal seeds are satisﬁed. The purpose of this pap er
is to ensure that those conditions hold in Cw.
In order to establish it, in the ﬁrst part of the paper, we start with a continuation of
the work of [ 15] about the convolution products, heads and socles of graded mod ules
over symmetric KLR algebras. One of the main results in [ 15] is that the convolution
product M ◦N of a real simple R(β)-module M and a simple R(γ)-modules N has a
unique simple quotient and a unique simple submodule. Moreover, if M ◦N ≃N ◦M
up to a grading shift, then M ◦N is simple. In such a case we say that M and N
commute. The main tool of [ 15] was the R-matrix rM,N , constructed in [ 14], which is a
homogeneous homomorphism from M ◦N toN ◦M of degree Λ( M,N ). In this work,
we deﬁne some integers encoding necessary information on M ◦N,
~Λ(M,N ) := 1
2
(
Λ(M,N ) + (β,γ )
)
, d(M,N ) := 1
2
(
Λ(M,N ) + Λ(N,M )
)
and study the representation theoretic meaning of the integers Λ (M,N ), ~Λ(M,N ) and
d(M,N ).
We then prove Leclerc’s ﬁrst conjecture ([ 29]) on the multiplicative structure of
elements in Bup, when the generalized Cartan matrix is symmetric (Theorem 4.1.1 and
Theorem 4.2.1). Theorem 4.2.1 is due to McNamara ([ 34, Lemma 7.5]) and the authors
thank him for informing us of his result.
We say that b ∈ Bup is real if b2 ∈qZ Bup := ⨆
n∈ZqnBup.
MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS 7
Theorem ([29, Conjecture 1]) . Letb1 andb2 be elements in Bup such that one of them
is real and b1b2 ⁄∈qZBup. Then the expansion of b1b2 with respect to Bup is of the form
b1b2 =qmb′ +qsb′′ +
∑
c⁄=b′,b′′
γc
b1,b2(q)c,
whereb′ ⁄=b′′, m,s ∈ Z, m<s , and
γc
b1,b2(q) ∈qm+1Z[q] ∩qs−1Z[q−1].
More precisely, we prove that qmb′ and qsb′′ correspond to the simple head and the
simple socle of M ◦N, respectively, when b1 corresponds to a simple module M and
b2 corresponds to a simple module N.
Next, we move to provide an algebraic framework for monoidal cate goriﬁcation of
quantum cluster algebras. In order to simplify the conditions of qua ntum monoidal
seeds and their mutations, we introduce the notion of admissible pairs in Cw. A pair
({Mi}i∈J, ~B) is called admissible in Cw if (i) {Mi}i∈J is a commuting family of self-dual
real simple objects of Cw, (ii) ~B is an integer-valuedJ ×Jex-matrix with skew-symmetric
principal part, and (iii) for each k ∈J, there exists a self-dual simple object M ′
k in Cw
such that M ′
k commutes with Mi for all i ∈ J \ {k} and there are exact sequences in
Cw
0 →q ⨀
bi,k>0
M ⊙bi,k
i →q ~Λ(Mk,M ′
k)Mk ◦M ′
k → ⨀
bi,k<0
M ⊙(−bi,k)
i → 0
0 →q ⨀
bi,k<0
M ⊙(−bi,k)
i →q ~Λ(M ′
k,Mk)M ′
k ◦Mk → ⨀
bi,k>0
M ⊙bi,k
i → 0
(0.2)
where ~Λ(Mk,M ′
k) and ~Λ(M ′
k,Mk) are prescribed integers and ⨀ is a convolution prod-
uct up to a power of q.
For an admissible pair ({Mi}i∈J, ~B), let Λ = (Λ i,j)i,j∈J be the skew-symmetric matrix
where Λ i,j is the homogeneous degree of rMi,Mj
, the R-matrix between Mi andMj, and
let D = {di}i∈J be the family of elements in Q given by Mi ∈R(−di)-gmod.
Then, together with the result of [
11], our main theorem in the ﬁrst part of the paper
reads as follows:
Main Theorem 1 (Theorem
7.1.3 and Corollary 7.1.4). If there exists an admissible
pair ({Mi}i∈K, ~B) in Cw such that [S ] :=
(
{q−(wt(Mi),wt(Mi))/4[Mi]}i∈J, −Λ, ~B,D
)
is an
initial seed of Aq1/2(n(w)), then Cw is a monoidal categoriﬁcation of Aq1/2(n(w)).
The second part of this paper ( § 8–11) is mainly devoted to showing that there
exists an admissible pair in Cw for every symmetric Kac-Moody algebra g and its Weyl
group element w. In [ 11], Geiß, Leclerc and Schr¨ oer provided an initial quantum seed
in Aq(n(w)) whose quantum cluster variables are unipotent quantum minors. The
unipotent quantum minors are elements in Aq(n), which are regarded as a q-analogue
