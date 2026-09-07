---
doc_id: arxiv-1801.05145v1
doc_title: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS"
section_id: sec-001-4-s-j-kang-m-kashiw-ara-m-kim-s-j-oh
section_title: "S.-J. KANG, M. KASHIW ARA, M. KIM, S.-J. OH"
section_number: 4
pages: 4-6
source_pdf: 1801.05145v1.pdf
source_sha256: 808da260edd433f7
doc_brief: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS — We prove that the quantum cluster algebra structure of a unipote nt quantum coordinate ring Aq(n(w)), associated with a symmetric Kac-Moody algebra and"
---
of an imaginary element b ∈ Bup such that b2 does not belong to Bup. Nevertheless,
the idea of considering subsets of Bup whose elements are q-commuting with each other
and studying the relations between those subsets has survived an d became one of the
motivations of the study of (quantum) cluster algebras.
In a series of papers [
8, 9, 11], Geiß, Leclerc and Schr¨ oer showed that the unipo-
tent quantum coordinate ring Aq(n(w)) has a skew-symmetric quantum cluster algebra
structure whose initial cluster consists of so called the unipotent quantum minors . In
[23], Kimura proved that Aq(n(w)) is compatible with the upper global basis Bup of
Aq(n); i.e., the set Bup(w) := Aq(n(w)) ∩ Bup is a basis of Aq(n(w)). Thus, with a
result of [ 4], one can expect that every cluster monomial of Aq(n(w)) is contained in
the upper global basis Bup(w), which is named the quantization conjecture by Kimura
([23]):
Conjecture ([11, Conjecture 12.9], [ 23, Conjecture 1.1(2)]) . When g is a symmetric
Kac-Moody algebra, every quantum cluster monomial in Aq1/2(n(w)) := Q(q1/2) ⊗Q(q)
Aq(n(w)) belongs to the upper global basis Bup up to a power of q1/2.
It can be regarded as a reformulation of Berenstein-Zelevinsky’s id eas on the mul-
tiplicative properties of Bup. There are some partial results of this conjecture. It is
proved for g =A2, A3, A4 and Aq(n(w)) = Aq(n) in [ 2] and [ 7, § 12]. When g =A(1)
1 ,
An andw is a square of a Coxeter element, it is shown in [
26] and [ 27] that the cluster
variables belong to the upper global basis. When g is symmetric and w is a square of
a Coxeter element, the conjecture is proved in [ 24]. Notably, Qin provided recently a
proof of the conjecture for a large class with a condition on the Wey l group element
w ([37]). Note that Nakajima proposed a geometric approach of this conj ecture via
quiver varieties ([ 35]).
In this paper, we prove the above conjecture completely by showin g that there exists
a monoidal categoriﬁcation of Aq1/2(n(w)).
In [12], Hernandez and Leclerc introduced the notion of monoidal categoriﬁcation of
cluster algebras. A simple object S of a monoidal category C is real ifS ⊗S is simple,
and is prime if there exists no non-trivial factorization S ≃S1 ⊗S2. They say that C
is a monoidal categoriﬁcation of a cluster algebra A if the Grothendieck ring of C is
isomorphic to A and if
(M1) the cluster monomials of A are the classes of real simple objects of C,
(M2) the cluster variables of A are the classes of real simple prime objects of C.
(Note that the above version is weaker than the original deﬁnition o f the monoidal
categoriﬁcation in [ 12].) They proved that certain categories of modules over symmetric
quantum aﬃne algebras U ′
q(g) give monoidal categoriﬁcations of some cluster algebras.
Nakajima extended this result to the cases of the cluster algebras of type A,D,E ([36])
(see also [ 13]). It is worth to remark that once a cluster algebra A has a monoidal
MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS 5
categoriﬁcation, the positivity of cluster variables of A and the linear independence of
cluster monomials of A follow (see [ 12, Proposition 2.2]).
In this paper, we reﬁne Hernandez-Leclerc’s notion of monoidal ca tegoriﬁcations
including the quantum cluster algebra case. Let us brieﬂy explain it. L et C be an
abelian monoidal category equipped with an auto-equivalence q and a tensor product
which is compatible with a decomposition C = ⨁
β∈Q Cβ. Fix a ﬁnite index set J =
Jex ⊔Jfr with a decomposition into the exchangeable part and the frozen par t. Let
S be a quadruple ( {Mi}i∈J,L, ~B,D ) of a family of simple objects {Mi}i∈J in C , an
integer-valued skew-symmetric J ×J-matrix L = (λi,j), an integer-valued J ×Jex-
matrix ~B = (bi,j) with skew-symmetric principal part, and a family of elements D =
{di}i∈J in Q. If this datum satisﬁes the conditions in Deﬁnition 6.2.1 below, then
it is called a quantum monoidal seed in C. For each k ∈ Jex, we have mutations
µk(L),µk( ~B) and µk(D) of L, ~B andD, respectively. We say that a quantum monoidal
seed S = ( {Mi}i∈J,L, ~B,D ) admits a mutation in direction k ∈ Jex if there exists a
simple object M ′
k ∈ Cµk(D)k which ﬁts into two short exact sequences ( 0.2) below in C
reﬂecting the mutation rule in quantum cluster algebras, and thus obtained qu adruple
µk(S ) := ({Mi}i⁄=k ∪ {M ′
k},µk(L),µk( ~B),µk(D)) is again a quantum monoidal seed in
C. We call µk(S ) the mutation of S in direction k ∈Jex.
Now the category C is called a monoidal categoriﬁcation of a quantum cluster algebra
A over Z[q±1/2] if
(i) the Grothendieck ring Z[q±1/2] ⊗Z[q±1]K(C) is isomorphic to A,
(ii) there exists a quantum monoidal seed S = ( {Mi}i∈J,L, ~B,D ) in
C such that [ S ] := ({qmi[Mi]}i∈J,L, ~B) is a quantum seed of A for
some mi ∈ 1
2Z,
(iii) S admits successive mutations in all directions in Jex.
(0.1)
The existence of monoidal category C which provides a monoidal categoriﬁcation of
quantum cluster algebra A implies the following:
(QM1) Every quantum cluster monomial corresponds to the isomor phism class
of a real simple object of C. In particular, the set of quantum cluster
monomials is Z[q±1/2]-linearly independent.
(QM2) The quantum positivity conjecture holds for A.
In the case of unipotent quantum coordinate ring Aq(n), there is a natural can-
didate for monoidal categoriﬁcation, the category of ﬁnite-dimen sional graded mod-
ules over a Khovanov-Lauda-Rouquier algebras ([
21, 22], [ 38]). The Khovanov-Lauda-
Rouquier algebras (abbreviated by KLR algebras), introduced by K hovanov-Lauda
[21, 22] and Rouquier [ 38] independently, are a family of Z-graded algebras which
categoriﬁes the negative half U −
q (g) of a symmetrizable quantum group Uq(g). More
