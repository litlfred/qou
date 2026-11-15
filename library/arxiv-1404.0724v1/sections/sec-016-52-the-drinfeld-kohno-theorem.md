---
doc_id: arxiv-1404.0724v1
doc_title: "Introduction to representations of braid groups"
section_id: sec-016-52-the-drinfeld-kohno-theorem
section_title: "The Drinfeld-Kohno theorem"
section_number: 5.2
pages: 26-32
source_pdf: 1404.0724v1.pdf
source_sha256: ea40edaad77c1617
toc_source: outline
doc_brief: "Introduction to representations of braid groups — These are lecture notes prepared for a minicourse given at the Cimpa Research School Algebraic and geometric aspects of representation the- ory, held"
duplicate_of: "ariasabad2015-revcolmat"
---
The Drinfeld-Kohno theorem
We have seen that modules over quasi-triangular bialgebras produce representations of the braid
groups. However, so far we have not encountered nontrivial examples of quasi-triangular bialge-
bras. A rich source of examples comes from Lie theory: the universal enveloping algebra U(g) of
a complex semisimple Lie algebra g can be deformed to obtain a quantum enveloping algebra.
These provide interesting examples of quasi-triangular bialgebras and of representations of the
braid groups.
In order to describe the Drinfeld-Jimbo bialgebras, it will be necessary to review some facts
regarding the classiﬁcation of semisimple Lie algebras.
A good reference for this subject is
Humphreys’ book [14]. Let g be a ﬁnite dimensional complex semisimple Lie algebra. A Cartan
subalgebra h ⊂g is an abelian subalgebra with the property that Ng(h) = h. Where Ng(h) is
the normalizer of h in g, i.e:
Ng(h) := {x ∈g : [h, x] ⊂h}.
Cartan subalgebras always exist and moreover, any two Cartan subalgebras are conjugated
to one another. Let us now on ﬁx a Cartan subalgebra h ⊂g. For any element x ∈h, the
linear map ad(x) : g →g is diagonalizable. Since h is abelian, all the maps ad(x) commute and
therefore g decomposes as a direct sum of eigenspaces:
g =
M
α∈h∗
gα,
for some functionals α ∈h∗so that:
[h, y] = α(h)y, if y ∈gα, h ∈h.
The set of roots, denoted by ∆, is the set of nonzero α ∈h∗in the decomposition above.
Lemma 5.11. Let g be a ﬁnite dimensional complex semisimple Lie algebra and h ⊂g a Cartan
subalgebra. For any α ∈h∗set
gα := {x ∈g : [h, x] = α(h)x for all h ∈h}.
Then:
[gα, gβ] ⊂gα+β.
If x ∈gα for α̸ = 0, ad(x) is nilpotent. If α + β̸ = 0 then gα is orthogonal to gβ with respect to
the Killing form. In particular, the restriction of κ to h = g0 is nondegenerate.
Proof. The ﬁrst claim follows from direct computation. Take h ∈h, x ∈gα and y ∈gβ:
[h[x, y]] = [[h, x], y] + [x, [h, y]] = (α(x) + β(x))[x, y].
For the second claim, consider y ∈gβ, then:
ad(x)n(y) ∈gnα+β,
since gγ is nonzero only for ﬁnitely many γ, we conclude that ad(x)n = 0 for n suﬃciently large.
Let us now prove the last statement. We choose a basis for g compatible with the decomposition
g = L
γ gγ then if x ∈gα and y ∈gβ then
ad(x) ◦ad(y) : gγ →gγ+α+β,
so if α + β̸ = 0 the matrix associated to ad(x) ◦ad(y) has zeros in the diagonal and therefore
κ(x, y) = 0.
□
The set ∆⊂h∗of roots of g has a beautiful combinatorial structure which makes it an abstract
root system. Let us recall this deﬁnition:
Deﬁnition 5.12. Let E be a ﬁnite dimensional real vector space with a symmetric positive
deﬁnite bilinear form ( , ). A root system in E is a ﬁnite subset ∆⊂E which spans E and does
not containing zero, such that:
1. If α ∈∆then −α ∈∆, and no other multiple of α is in ∆.
2. For each α ∈∆the reﬂection σα with respect to the plane orthogonal to α ﬁxes the set ∆.
3. If α, β ∈∆then
2(α, β)
(α, α) ∈Z.
Coming back to the roots of the Lie algebra g, since the Killing form κ is nondegenerate when
restricted to h, it induces a bilinear form in h∗which we still denote by κ.
Proposition 5.13. The set ∆spans a real vector space E ⊂h∗of dimension equal to the
complex dimension of h∗. Moreover, the bilinear form κ is positive deﬁnite when restricted to
E, and the set ∆is an abstract root system in E.
Proof. The interested reader may ﬁnd the proof of this proposition in Humphreys’ book [14]. □
The complete structure of an abstract root system ∆⊂E can be described by its Cartan
matrix, which is deﬁned as follows. Given v ∈E denote by Tv the space of vectors orthogonal to
v. We say that v ∈E is singular if v ∈Tα for some α ∈∆. We say that v ∈E is regular if it is
not singular. Clearly, regular vectors exist since E is not the union of ﬁnitely many hyperplanes.
Given a regular element v ∈E, the set ∆decomposes into positive and negative roots :
∆= ∆+ a
∆−,
where
∆+ := {α ∈∆: (v, α) > 0} and ∆−:= {α ∈∆: (v, α) < 0}.
We say that a positive root α is simple if it cannot be written in the form α = β1 + β2 where
β1, β2 are positive roots.
Deﬁnition 5.14. Let ∆be an abstract root system in E and v ∈E a regular element. Fix an
ordering α1, . . . , αl of the simple roots. The Cartan matrix of ∆with respect to v is the matrix:
Ci,j := 2(αi, αj)
(αi, αi) .
Proposition 5.15. The Cartan matrix C of the root system ∆is well deﬁned, up to conjugation
by a permutation matrix. Moreover, C has the following properties:
1. The entries Cij are non-positive integers if i̸ = j and Cii = 2.
2. There exists a unique diagonal matrix D = Diag(d1, . . . , dl) with di ∈{1, 2, 3}, such that
DC is symmetric and positive deﬁnite.
Proof. The interested reader can ﬁnd the proof in Humphreys’ book [14].
□
We are ready to deﬁne the quantum enveloping algebra of a complex semisimple Lie algebra.
These algebras are topological in the sense that all tensor products appearing in the deﬁnition
are topological tensor products, which we now deﬁne. We denote by C[[h]] the algebra of formal
power series in the variable h with complex coeﬃcients. A module M over C[[h]] has the structure
of a topological vector space: a basis of neighborhoods for zero is {hnM}n≥0.
Deﬁnition 5.16. Let M and N be C[[h]]-modules. The topological tensor product of M and N,
denoted M ˆ⊗N is the C[[h]]-module:
M ˆ⊗N := lim
←−
M ⊗C[[h]] N
hn(M ⊗C[[h]] N).
There is a natural map M ⊗C[[h]] N →M ˆ⊗N.
Deﬁnition 5.17. A topological quasi-triangular bialgebra is a C[[h]]-module A together with
structure maps and universal r-matrix as in the deﬁnition of quasi-triangular bialgebra, where
all tensor products are replaced by topological tensor products and structure maps are required
to be continuous.
The following notation will be useful in describing the Drinfeld-Jimbo construction. Given an
invertible element q in an algebra A and a positive integer n, we set:
[n]q := qn −q−n
q −q−1 ,
[n]q! := [n]q[n −1]q . . . [1]q,
n
k

q
:=
[n]q!
[n −k]q![k]q!.
Deﬁnition 5.18. Let g be a ﬁnite dimensional complex semisimple Lie algebra with Cartan
matrix C of size l × l. The Drinfeld-Jimbo algebra Uh(g) is the quotient of the free algebra over
C[[h]] on the set {Hi, Ei, Fi}i≤l by the closure of the two sided ideal generated by the following
relations:
[Hi, Hj] = 0,
[Ei, Fj] −δij
 
sinh(hdiHi
2
)
sinh(hdi
2 )
!
= 0,
[Hi, Ej] −CijEj = 0,
[Hi, Fj] + CijFj = 0,
1−Cij
X
k=0
(−1)k
1 −Cij
k

qi
EikEjE1−Cij−k
i
= 0, for i̸ = j,
1−Cij
X
k=0
(−1)k
1 −Cij
k

qi
FikFjF 1−Cij−k
i
= 0, for i̸ = j.
Here qi := exp (hdi
2 ).
Theorem 5.19 (Drinfeld [10]-Jimbo [15]). The algebra Uh(g) is a topological bialgebra with
structure maps characterized by the following properties:
∆h(Hi) = Hi ⊗1 + 1 ⊗Hi,
∆h(Ei) = Ei ⊗exp(hdiHi
4
) + exp(−hdiHi
4
) ⊗Ei,
∆h(Fi) = Ei ⊗exp(hdiHi
4
) + exp(−hdiHi
4
) ⊗Fi,
ϵh(Hi) = ϵh(Ei) = ϵh(Fi) = 0.
There exists a universal r-matrix Rh, which can be written explicitly, making Uh(g) a topological
quasi-triangular bialgebra. Moreover, there is a canonical isomorphism of algebras:
Uh(g)
h(Uh(g))
∼= U(g).
Proof. The proof of this theorem can be found in [10].
□
Given a ﬁnite dimensional representation V of the complex semisimple Lie algebra g, there
exists a corresponding representation of the Drinfeld-Jimbo algebra Uh(g). This fact can be
deduced from the following result:
Theorem 5.20. Let g be a ﬁnite dimensional complex semisimple Lie algebra with Drinfeld-
Jimbo algebra Uq(g). There exists an isomorphism of topological algebras:
ϕ : Uh(g) →U(g)[[h]],
which is the identity modulo h. Moreover, given any other such isomorphism ϕ′ there exists an
invertible element F ∈U(g)[[h]], congruent to 1 modulo h, such that for any x ∈Uh(g):
ϕ′(x) = Fϕ(x)F −1.
Proof. The proof of this theorem can be found in Kassel’s book [16].
□
The theorem above implies that given a complex ﬁnite dimensional representation V of g, the
C[[h]]-module V [[h]] is a representation of Uh(g), well deﬁned up to isomorphism. Indeed, V [[h]]
is a module over U(g)[[h]] and we can choose the isomorphism ϕ as above to make it a module
over the Drinfeld-Jimbo algebra. Since ϕ is unique up to conjugation, the isomorphism class of
the representation is well deﬁned. Because Uh(g) is a topological quasi-triangular bialgebra, the
universal r-matrix Rh ∈Uh(g)ˆ⊗Uh(g) deﬁnes an r-matrix on V [[h]]ˆ⊗V [[h]]. We conclude that
for each n ≥2 the C[[h]]-module V [[h]]ˆ⊗n ∼= V ⊗n[[h]] is a representation of the braid group Bn
by C[[h]]-linear automorphisms. We denote this representation by
ρDJ : Bn →AutC[[h]](V ⊗n[[h]]).
For a ﬁnite dimensional representation V of a complex semisimple Lie algebra g, there are
two diﬀerent constructions of representations of the braid groups. On the one hand, the mon-
odromy of the Knizhnik-Zamolodchikov connections gives the vector space V ⊗n the structure
of a representation of Bn. On the other hand, the universal r-matrix in the Drinfeld-Jimbo
algebra Uh(g) provides a representation of Bn on V ⊗n[[h]]. The relationship between these two
seemingly unrelated constructions is provided by the Drinfeld-Kohno theorem. For a complex
number h, let θn,h be the Knizhnik-Zamolodchikov connection with parameter h deﬁned by:
θn,h :=
h
2πiθn.
Since dθn = 0 = [θn, θn], the connection θn,h is ﬂat. As before, for each h ∈C we obtain
a representation of the braid group ρh : Bn →V ⊗n. The monodromy of the connection θn,h
can be computed explicitly in terms of iterated integrals and in particular, depends on h in an
analytic manner. Therefore, by taking Taylor series with respect to the parameter h, we obtain
a representation:
ρKZ : Bn →AutC[[h]](V ⊗n[[h]]).
Theorem 5.21 (Drinfeld [9] - Kohno [21]). Let g be a ﬁnite dimensional complex semisimple
Lie algebra and V a ﬁnite dimensional complex representation. For each n ≥2, the Knizhnik-
Zamolodchikov representation of of the braid group Bn:
ρKZ : Bn →AutC[[h]](V ⊗n[[h]]),
obtained by taking Taylor series on the monodromy of the Knizhnik-Zamolodchikov connection
is equivalent to the Drinfeld-Jimbo representation:
ρDJ : Bn →AutC[[h]](V ⊗n[[h]]),
obtained via the universal r-matrix of the Drinfeld-Jimbo algebra Uh(g).
Proof. The interested reader may refer to Kassel’s book [16].
□
References
[1] J. Alexander, A lemma on a system of knotted curves, Proc. Nat. Acad. Sci. 9 (1923), 93-95.
[2] V. Arnold, The cohomology ring of the group of dyed braids, Mat. Zametki 5 (1970),
227-231.
[3] E. Artin, Theory of braids, Ann. of Math. (2) 48 (1947), 101-126.
[4] S. Bigelow, Representations of braid groups, Proceedings ICM 2002 Vol II 37-45.
[5] S. Bigelow, A homological deﬁnition of the Jones polynomial, Geometry and Topology
monographs, Vol 4: Invariants of knots and three manifolds, 29-41.
[6] J. Birman, T. Brendle, Braids: a survey, Handbook of Knot Theory, Elsevier (2005).
[7] W. Burau, ¨Uber Zopfgruppen und gleischsinning verdrillte Verkettungen, Abh. Math. Sem.
Ham. II (1936), 171-178.
[8] S. Chmutov, S. Duzhin, J. Mostovoy, Introduction to Vassiliev knot invariants, Cambridge
University Press (2012).
[9] V. Drinfeld, Quasi-bialgebras, Leningrad Math. Journal 1 (1990) 1419-1457.
[10] V. Drinfeld, Quantum groups, Proceedings of the 1986 ICM, 798-820 Amer. Math, Soc.
[11] E. Fadell and J. Van Buskirk, The braid groups of E2 and S2, Duke Mathematical Journal,
29 (1962), 243-257.
[12] B. Farb, D. Margalit, A primer on the mapping class group, Princeton University Press
(2011).
[13] R. Fox and L Neuwirth, The braid groups, Math. Scand. 10. (1962), 119-126.
[14] J. E. Humphreys, Introduction to Lie algebras and representation theory, Graduate texts
in mathematics, Springer-Verlag.
[15] M. Jimbo, A q-diﬀerence analogue of U(g) and the Yang-Baxter equation, Letters in Math.
Phys. 10, 63-69, (1985).
[16] C. Kassel, Quantum groups, Springer Verlag (1994).
[17] C. Kassel,
M. Rosso,
V. Turaev,
Quantum groups and knot invariants,
Soci´et´e
Math´ematique de France (1997).
[18] C. Kassel, V. Turaev, Braid groups, Springer Verlag (2008).
[19] T. Kohno, Conformal ﬁeld theory and topology, Translations of Math. Monographs, Amer.
Math.Soc.
[20] T. Kohno, Quantum and homological representations of braid groups, Conﬁguration spaces,
Geometry, Combinatorics and Topology, Edizioni della Normale (2012), 355-372.
[21] T. Kohno, Monodromy representations of braid groups and Yang-Baxter equations, Ann.
Inst. Fourier 37 (1987) 139-160.
[22] D. Krammer, Braid groups are linear, Ann. Math. (2) 155 (2002), 131-156.
[23] R. J. Lawrence, Homological representations of the Hecke algebra, Comm. Math. Phys. 135
(1990), 141-191.
[24] A. Markov, ¨Uber die freie ¨Aquivalenz geschlossener Z¨opfe, Recueil Math. Moscou 1 (1935).
[25] D. Sinha, The homology of the little disks operad, Arxiv:math0610236v3.
