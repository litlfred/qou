---
doc_id: arxiv-math-0111205v1
doc_title: "arXiv:math/0111205v1 [math.CT] 19 Nov 2001"
section_id: sec-021-a-on-quantum-doubles-of-finite-dimensional-hopf
section_title: "On Quantum Doubles of Finite Dimensional Hopf Algebras"
section_number: A
pages: 54-62
source_pdf: 0111205v1.pdf
source_sha256: 66325a21651aff89
toc_source: inferred
doc_brief: "arXiv:math/0111205v1 [math.CT] 19 Nov 2001 — For every tensor category C there is a braided tensor category Z(C), the ‘center’ of C."
---
Hopf Algebras
The core of this paper was the proof that the quantum doubles of certain tensor categories
are modular. That Rep D(H) is modular has been proven for H = CG [2], where G is a
ﬁnite group, and for semisimple H over an algebraically closed ﬁeld k of characteristic zero
[13]. A proof which covers also weak Hopf algebras (or ﬁnite quantum groupoids) is given
in [41]. Our aim in this appendix is to give a proof which uses the ideas of Lyubashenko
[32, 33] and Majid [34] and therefore is more in the spirit of our proof in the categorical
54
situation. In the sequel H will always be a ﬁnite dimensional Hopf algebra. Since the
main application will be to quantum doubles the following will be useful.
Lemma A.1 Let H be a ﬁnite dimensional Hopf algebra H over the ﬁeld k and let D(H)
be the quantum double. The following are equivalent:
(i) H is semisimple and cosemisimple.
(ii) The antipode of H is involutive and char k ∤dim H.
(iii) D(H) is semisimple.
(iv) D(H) is cosemisimple.
Remark A.2 If the characteristic of k is zero then H is semisimple iﬀit is cosemisimple,
and the second condition in (ii) is vacuous.
✷
Proof. For the equivalences (i)⇔(iii)⇔(iv) see [47] and for (i)⇔(ii) see [14].
■
In order for the category Rep D(H) to be modular it must be semisimple, which by
the lemma reduces us to the case where H satisﬁes (i) and (ii).
Lemma A.3 Let H satisfy the (equivalent) conditions of Lemma A.1. Then there are
two-sided integrals Λ ∈H, µ ∈ˆH which are traces in the sense that
⟨µ, ab⟩= ⟨µ, ba⟩,
⟨αβ, Λ⟩= ⟨βα, Λ⟩
for all a, b ∈H, αβ ∈ˆH. The category Rep D(H) is a spherical category.
Proof. Semisimple Hopf algebras are unimodular [28], which by deﬁnition means that
there are two-sided integrals. By [28, Proposition 8], unimodular Hopf algebras satisfy
⟨µ, ab⟩= ⟨µ, bS2(a)⟩
∀a, b ∈H,
thus ⟨µ, ·⟩is tracial by involutivity of S.
Sphericity of Rep D(H) is now an obvious
consequence of [6] where it was shown under the weaker assumption that S2 is inner. ■
We brieﬂy recall some results on quasitriangular Hopf algebras. As shown be Drinfel’d
[12], the antipode of a ﬁnite dimensional quasitriangular Hopf algebra H is inner, i.e.
there is an invertible u ∈H such that S2(A) = uAu−1. One has the explicit formulae
u
=
m ◦(S ⊗id)(R21),
u−1
=
m ◦(id ⊗S2)(R21),
(I.e., u = P
i S(fi)ei if R = P
i ei ⊗fi). Furthermore, Drinfel’d proved
uS(u) = S(u)u ∈Z(H),
ε(u) = 1,
∆(u) = (R21R)−1(u ⊗u).
Recall [53] that a ribbon Hopf algebra is a quasitriangular Hopf algebra H together
with θ ∈Z(H) satisfying
θ2 = uS(u),
S(θ) = θ,
ε(θ) = 1,
∆(θ) = (R21R)−1(θ ⊗θ).
(A.1)
55
Proposition A.4 Let H be a quasitriangular semisimple and cosemisimple Hopf algebra.
Then H is a ribbon Hopf algebra with θ = u.
Proof. Since S2 = id it follows that Drinfel’d’s u is central.
Now [24, Proposition 4]
implies that u is a ribbon element.
■
Remark A.5 For a ribbon Hopf algebra H with θ = u the quantum trace, which for a
representation π on a vector space V is deﬁned by
Trq
π(X) := Tr ◦π(uθ−1 X),
coincides with the usual trace Tr on End V . In particular, all quantum dimensions d(π)
coincide with the classical dimensions dim Vπ.Therefore,
dim Rep H =
X
i
d(πi)2 =
X
i
(dim Vπi)2 = dimk H.
✷
In order to conclude that Rep H is modular it remains to prove that the S-matrix of the
ribbon category Rep H is invertible. A related notion of non-degeneracy was introduced
in [49], where a quasitriangular Hopf algebra was called factorizable if the map
ˆH →H :
z 7→⟨z ⊗id, I⟩,
I = R21R
is injective, thus invertible. Furthermore, it was shown that every quantum double D(H)
is factorizable. The notion of factorizability plays an important role in the works [34, 26]
where an action of SL(2, Z) on ribbon Hopf algebras is deﬁned and studied.
Definition A.6 ([34]) For a quasitriangular Hopf algebra the selfdual Fourier trans-
forms S+, S−are deﬁned by the linear endomorphisms of H:
S+(b)
=
(id ⊗µ)(R21(1 ⊗b)R12),
S−(b)
=
(id ⊗µ)(R−1
12 (1 ⊗b)R−1
21 ),
where µ is a left integral in ˆH. If H is ribbon the map T : H →H is deﬁned by T (b) = θb.
Theorem A.7 ([34]) For a factorizable ribbon Hopf algebra the following modular rela-
tions hold:
S+ ◦S−= id = S−◦S+,
(S+ ◦T )3 = λS2
+,
S2
+ = S,
(A.2)
where S(x) = R(2)S(Ad R(1)(x)) with Ad Y (x) = Y(1)xS(Y(2)) is the braided antipode, and
λ̸ = 0 is deﬁned by S+(θ) = λθ−1.
56
Lemma A.8 The following decompositions hold in every ﬁnite dimensional Hopf algebra.
a ⊗1 =
X
i
(1 ⊗xi)∆(yi) =
X
i
∆(yi)(1 ⊗S2(xi))
where
X
i
yi ⊗xi = (id ⊗S−1)∆(a).
Proof. Inserting P
i yi ⊗xi = a(1) ⊗S−1(a(2)) into P
i(1 ⊗xi)∆(yi) we obtain
(1 ⊗S−1(a(2)))∆(a(1)) = (1 ⊗S−1(a(3)))(a(1) ⊗a(2)) = a(1) ⊗S−1(a(3))a(2) = a ⊗1,
(A.3)
and the other equality is veriﬁed similarly.
■
Proposition A.9 Let H be a quasitriangular semisimple, cosemisimple Hopf algebra and
µ ∈ˆH a left integral. Then the selfdual Fourier transforms S± map the center of H into
itself:
S±(Z(H)) ⊂Z(H).
(A.4)
Proof. By [28, Proposition 8] unimodularity is equivalent to the identity
µ(ab) = µ(bS2(a)) ∀a, b ∈H,
(A.5)
which will be used in the sequel. Let a ∈H, b ∈Z(H). Then
a S+(b)
=
a (id ⊗µ)(R21(1 ⊗b)R12)
=
(id ⊗µ)((a ⊗1)R21R12(1 ⊗b))
=
X
i
(id ⊗µ)((1 ⊗xi)∆(yi)R21R12(1 ⊗b))
=
X
i
(id ⊗µ)((1 ⊗xi)R21R12(1 ⊗b)∆(yi))
(A.6)
=
X
i
(id ⊗µ)(R21R12(1 ⊗b)∆(yi)(1 ⊗S2(xi)))
=
(id ⊗µ)(R21R12(1 ⊗b)(a ⊗1))
=
(id ⊗µ)(R21R12(1 ⊗b)) a = S+(b) a,
thus S+(b) ∈Z(H). We have used b ∈Z(H), [∆(·), R21R12] = 0, (A.5) and the lemma.
■
Remark A.10 1. In restriction to the center, the braided antipode S appearing in (A.2)
equals the antipode S.
2. For a ribbon algebra H it is trivial that T maps Z(H) into itself, since θ ∈Z(H).
✷
57
The modularity condition requires invertibility of the matrix
Si,j = (Trq
πi ⊗Trq
πj)(R21R12),
(A.7)
where i, j range over the equivalence classes of irreducible representations of H. Now, in
the semisimple case the representations are in one-to-one correspondence with the minimal
projections in Z(H), which leads to the following result.
Theorem A.11 Let H be a factorizable quasitriangular semisimple and cosemisimple
Hopf algebra. Then the category Rep H is modular.
Proof. We have already proven that Rep H is a spherical ribbon category. Thus by Propo-
sition A.9 the center of H is stable under the Fourier transform S+. By factorizability
S+ is invertible, and the same holds for the restriction S+ ↾Z(H). By the remark after
Lemma A.4 the quantum traces on H-modules V , in terms of which the S-matrix is de-
ﬁned, coincide with the usual traces on EndV . In terms of the basis for Z(H) given by
the minimal idempotents Pi we obtain
S+(Pj) =
X
i
Sij Pi,
where the matrix S = (Sij) is invertible. But S is nothing but the modular matrix (A.7)
as we have
Sij
=
di µ(Pi S+(Pj)) = di (µ ⊗µ)(R21R12 (Pi ⊗Pj))
=
1
dj
(Trq
i ⊗Trq
j)(R21R12)
We have used µ(Pi) = 1/di and µ(x Pi) = 1/di Tri(x) [55].
■
Note that the proof is conceptually quite similar to our proof of modularity for general
semisimple spherical categories. In view of Lemma A.1 the following is now immediate:
Corollary A.12 Let H be semisimple and cosemisimple. Then Rep D(H) is modular.
We close the appendix with a remark which is meant to aid the reader in appreciating
the ‘self-duality’ of a quantum double D(H), in particular since in general it is not self-
dual in the sense of Hopf algebras: D(H)∗̸ ≃D(H). (For a ﬁnite abelian group G we in
fact have D(G) ≃D(G)∗≃CG ⊗C(G).) For any ﬁnite dimensional Hopf algebra one
can use the integrals to deﬁne ‘Fourier transforms’ H →ˆH. In [42] Fourier transforms
Fσ,σ′, σ, σ′ = ±, deﬁned as linear maps H →ˆH which intertwine certain actions of H on
H and ˆH by multiplication and translation, respectively, were studied systematically and
used to give a new proof of the invertibility of the antipode. There is a beautiful relation
between these more conventional Fourier transforms, relating H and ˆH, and the selfdual
Fourier transforms [34], which map D(H) onto itself. For simplicity we restrict ourselves
to FDKA’s, where things are easier since the Haar measures are two-sided invariant traces
and since there are unique Fourier transforms F : H →ˆH and ˆF : ˆH →H:
⟨F(x), y⟩
=
⟨µ, xS(y)⟩,
∀x, y ∈H,
(A.8)
⟨α, ˆF(β)⟩
=
⟨ˆS(α)β, Λ⟩,
∀α, β ∈ˆH,
(A.9)
58
where Λ, µ are the integrals in H, ˆH, respectively. If ι : H →D(H), ˆι : ˆH →D(H) are
the canonical embedding maps then the following diagram commutes:
ˆH ⊗H ˆι ⊗ι
✲D(H) ⊗D(H) m✲D(H)
H ⊗ˆH
ˆF ⊗F
❄
ι ⊗ˆι
✲D(H) ⊗D(H) m
✲D(H)
S−
❄
This nice observation is due to Kerler [26, Proposition 9] (with diﬀerent conventions), who,
however, did not emphasize the interpretation of F, ˆF as conventional Fourier transforms.
References
[1] D. Altschuler & A. Brugui`eres: Sliding property in sovereign categories. Preprint.
[2] D. Altschuler & A. Coste: Invariants of 3-manifolds from ﬁnite groups. In: Proc.
XXth Int. Conf. Diﬀ. Geom. Meth. in Theor. Phys., New York, 1991, pp. 219–233,
World Scientiﬁc, 1992.
[3] J. C. Baez & M. Neuchl:
Higher dimensional algebra. I: Braided monoidal 2-
categories. Adv. Math. 121, 196-244 (1996).
[4] J. C. Baez & J. Dolan: Categoriﬁcation. In: E. Getzler & M. Kapranov (eds.): Higher
Category Theory. Contemp. Math. 230, 1-36 (1998).
[5] J. W. Barrett & B. W. Westbury: Invariants of piecewise-linear 3-manifolds. Trans.
Amer. Math. Soc. 348, 3997-4022 (1996).
[6] J. W. Barrett & B. W. Westbury: Spherical categories. Adv. Math. 143, 357-375
(1999).
[7] A. Beliakova & C. Blanchet: Modular categories of types B, C and D. Comment.
Math. Helv. 76, 467-500 (2001).
[8] A. Brugui`eres: Cat´egories pr´emodulaires, modularisations et invariants de vari´et´es
de dimension 3. Math. Ann. 316, 215-236 (2000).
[9] A. Brugui`eres: Private communication.
[10] S. E. Crans: Generalized centers of braided and sylleptic monoidal 2-categories. Adv.
Math. 136, 183-223 (1998).
[11] V. G. Drinfel’d: Quantum groups. In: Proc. Int. Congr. Math, Berkeley 1986.
[12] V. G. Drinfel’d: On almost cocommutative Hopf algebras. Leningrad Math. J. 1,
321-342 (1990)
[13] P. Etingof & S. Gelaki: Some properties of ﬁnite dimensional semi-simple Hopf alge-
bras. Math. Res. Lett. 5, 191-197 (1998).
[14] P. Etingof & S. Gelaki: On ﬁnite-dimensional semisimple and cosemisimple Hopf
algebras in positive characterstic. Int. Math. Res. Not. 1998, 187-195.
59
[15] D. E. Evans & Y. Kawahigashi: On Ocneanu’s theory of asymptotic inclusions for
subfactors, topological quantum ﬁeld theories and quantum doubles. Int. J. Math. 6,
205-228 (1995).
[16] S. Gelfand & D. Kazhdan: Invariants of three-dimensional manifolds. Geom. Funct.
Anal. 6, 268-300 (1996).
[17] P. Ghez, R. Lima & J. E. Roberts: W ∗-categories. Pac. J. Math. 120, 79-109 (1985).
[18] M. Izumi: The structure of Longo-Rehren inclusions. Preprint 1998.
[19] M. Izumi: The structure of sectors associated with Longo-Rehren inclusions. Com-
mun. Math. Phys. 213, 127-179 (2000).
[20] A. Joyal & R. Street: Tortile Yang-Baxter operators in tensor categories. J. Pure
Appl. Alg. 71, 43-51 (1991).
[21] L. Kadison: New examples of Frobenius extensions. University Lecture Series #14,
AMS, 1999.
[22] C. Kassel: Quantum groups. Springer-Verlag, 1995.
[23] C. Kassel & V. G. Turaev: Double construction for monoidal categories. Acta Math.
175, 1-48 (1995).
[24] Kauﬀman, L. H., Radford, D. E.: A necessary and suﬃcient condition for a ﬁnite-
dimensional Drinfel’d double to be a ribbon Hopf algebra. J. Algebra 159, 98-114
(1993).
[25] Y. Kawahigashi, R. Longo & M. M¨uger: Multi-interval subfactors and modularity of
representations in conformal ﬁeld theory. Commun. Math. Phys. 219, 631-669 (2001).
[26] T. Kerler: Genealogy of non-perturbative quantum-invariants of 3-manifolds: the
surgical family. In: Geometry and physics (Aarhus, 1995), 503–547, Lecture Notes
in Pure and Appl. Math., 184, Dekker, New York, 1997.
[27] V. Kodiyalam & V. S. Sunder: Topological quantum ﬁeld theories from subfactors.
Chapman & Hall/CRC Research Notes in Mathematics, 2001.
[28] R. G. Larson & M. E. Sweedler: An associative orthogonal bilinear form for Hopf
algebras. Amer. J. Math. 91, 75-94 (1969).
[29] R. Longo: A duality for Hopf algebras and for subfactors I. Commun. Math. Phys.
159, 133-150 (1994).
[30] R. Longo & K.-H. Rehren: Nets of subfactors. Rev. Math. Phys. 7, 567-597 (1995).
[31] R. Longo & J. E. Roberts: A theory of dimension. K-Theory 11, 103-159 (1997).
[32] V. V. Lyubashenko: Tangles and Hopf algebras in braided categories. J. Pure Appl.
Alg. 98, 245-278 (1995).
[33] V. V. Lyubashenko: Modular transformations for tensor categories. J. Pure Appl.
Alg. 98, 279-327 (1995).
[34] V. V. Lyubashenko & S. Majid: Braided groups and quantum Fourier transform. J.
Algebra 166, 506-528 (1994).
60
[35] S. Mac Lane: Categories for the working mathematician. 2nd ed. Springer-Verlag,
1998.
[36] S. Majid: Representations, duals and quantum doubles of monoidal categories. Rend.
Circ. Mat. Palermo Suppl. 26, 197-206 (1991).
[37] T. Masuda: An analogue of Longo’s canonical endomorphism for bimodule theory
and its application to asymptotic inclusions. Int. J. Math. 8, 249-265 (1997).
[38] M. M¨uger: From subfactors to categories and topology I. Frobenius algebras in and
Morita equivalence of tensor categories. math.CT/0111204.
[39] M. M¨uger: From subfactors to categories and topology III. Triangulation invariants
of 3-manifolds and Morita equivalence of tensor categories. In preparation.
[40] M. M¨uger: On Galois extensions of braided tensor categories, mapping class group
representations and simple current extensions. In preparation.
[41] D. Nikshych, V. Turaev & L. Vainerman: Invariants of Knots and 3-manifolds from
Quantum Groupoids. math.QA/0006078.:
[42] F. Nill: Weyl algebras, Fourier transformations and integral on ﬁnite-dimensional
Hopf algebras. Rev. Math. Phys. 6, 149-166 (1994).
[43] A. Ocneanu (notes by Y. Kawahigashi): Quantum symmetry, diﬀerential geometry
of ﬁnite graphs and classiﬁcation of subfactors. Lectures given at Tokyo Univ. 1990.
[44] A. Ocneanu: An invariant coupling between 3-manifolds and subfactors, with con-
nections to topological and conformal quantum ﬁeld theory. Unpublished manuscript.
Ca. 1991.
[45] A. Ocneanu (notes by Y. Kawahigashi): Chirality for operator algebras. In: Araki,
H. et al. (eds.): Subfactors. World Scientiﬁc, 1994.
[46] V. Ostrik:
Module categories,
weak Hopf algebras and modular invariants.
math.QA/0111139.
[47] D. E. Radford: Minimal quasitriangular Hopf algebras. J. Algebra 157, 285-315
(1993).
[48] K.-H. Rehren: Braid group statistics and their superselection rules. In: D. Kastler
(ed.): The algebraic theory of superselection sectors. Introduction and recent results.
World Scientiﬁc, 1990.
[49] N. Yu. Reshetikhin & M. A. Semenov-Tian-Shansky: Quantum R-matrices and fac-
torization problems. J. Geom. Phys. 5, 533-550 (1988).
[50] N. Yu. Reshetikhin & V. G. Turaev: Invariants of 3-manifolds via link polynomials
and quantum groups. Invent. Math. 103, 547-598 (1991).
[51] N. Saaveda Rivano: Cat´egories Tannakiennes. LNM 265, Springer-Verlag, 1972.
[52] R. Street: The quantum double and related constructions. J. Pure Appl. Alg. 132,
195-206 (1998).
[53] V. G. Turaev: Quantum invariants of knots and 3-manifolds. Walter de Gruyter,
1994.
61
[54] V. G. Turaev & O. Y. Viro: State sum invariants of 3-manifolds and quantum 6j-
symbols, Topology 31, 865-902 (1992).
[55] S. L. Woronowicz: Compact matrix pseudogroups. Commun. Math. Phys. 111, 613-
665 (1987).
[56] D. N. Yetter: Framed tangles and a theorem of Deligne on braided deformations of
tannakian categories. Contemp. Math. 134, 325-350 (1992).
62
