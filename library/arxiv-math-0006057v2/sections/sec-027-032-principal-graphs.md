---
doc_id: arxiv-math-0006057v2
doc_title: "Finite Quantum Groupoids and Their Applications"
section_id: sec-027-032-principal-graphs
section_title: "Principal graphs"
section_number: 0.32
pages: 41-44
source_pdf: 0006057v2.pdf
source_sha256: c881434fe9f4b04f
toc_source: inferred
doc_brief: "Finite Quantum Groupoids and Their Applications — We give a survey of the theory of ﬁnite quantum groupoids (weak Hopf algebras), including foundations of the theory and applications to ﬁnite depth"
---
as follows ([JS], 4.2, [GHJ], 4.1). Let X = NL2(M)M and consider the following
sequence of N −N and N −M bimodules :
NL2(N)N, X, X ⊗M X∗, X ⊗M X∗⊗N X, . . .
obtained by right tensoring with X∗and X. The vertex set of the principal graph
is indexed by the classes of simple bimodules appearing as summands in the above
sequence. Let us connect vertices corresponding to bimodules NYN and NZM by
l edges if NYN is contained in the decomposition of NZN, the restriction of NZM,
with multiplicity l.
We apply Theorem 9.2.6 to express the principal graph of a ﬁnite depth subfactor
N ⊂M in terms of the quantum groupoid associated with it.
Let B and K be a quantum groupoid and its left coideal ∗-subalgebra such that
B acts on N and (N ⊂M) ∼= (N ⊂N>⊳K). Then bK = NL2(M)M, where we view
K as a relative (B, K) Hopf module as in Example 9.2.3
By Theorem 9.2.6 we can identify irreducible N −N (resp. N −M) bimodules
with simple B-comodules (resp. relative right (B, K) Hopf modules). Consider a
bipartite graph with vertex set given by the union of (classes of) simple B-comodules
and simple relative right (B, K) Hopf modules and the number of edges between the
vertices U and V representing B-comodule and relative right (B, K) Hopf module
respectively being equal to the multiplicity of U in the decomposition of V (when
the latter is viewed as a B-comodule) :
simple B-comodules
· · · | · · · | · · ·
simple relative right (B, K) Hopf modules
The principal graph of N ⊂M is the connected part of the above graph containing
the trivial B-comodule.
It was shown in ([NV3], 3.3, 4.10) that:
(a) the map δ : I 7→[g−1/2S(I)g1/2]′∩bB ⊂bB>⊳B deﬁnes a lattice anti-isomorphism
between ℓ(B) and ℓ( bB);
(b) the triple δ(I) ⊂bB ⊂bB>⊳I is a basic construction.
42
DMITRI NIKSHYCH AND LEONID VAINERMAN
Proposition 9.3.1. If K is a coideal ∗-subalgebra of B then the principal graph
of the subfactor N ⊂N>⊳K is given by the connected component of the Bratteli
diagram of the inclusion δ(K) ⊂bB containing the trivial representation of bB.
Proof. First, let us show that there is a bijective correspondence between right
relative (B, K) Hopf modules and ( bB>⊳K)-modules. Indeed, every right (B, K)
Hopf module V carries a right action of K. If we deﬁne a right action of bB by
v ⊳x = ⟨v(1), x ⟩v(2),
v ∈V, x ∈bB,
then we have
(v ⊳k) ⊳x
=
⟨v(1)k(1), x ⟩(v(2) ⊳k(2)) = ⟨v(1), (k(1) ⊲x) ⟩(v(2) ⊳k(2))
=
(v ⊳(k(1) ⊲x)) ⊳k(2),
for all x ∈bB and k ∈K which shows that kx and (k(1) ⊲x)k(2) act on V exactly in
the same way, therefore V is a right ( bB>⊳K)-module.
Conversely, given an action of ( bB>⊳K) on V , we automatically have a B-comodule
structure such that
⟨v(1)k(1), x ⟩(v(2) ⊲k(2))
=
⟨v(1), x(1) ⟩⟨k(1), x(2) ⟩(v(2) ⊳k(2))
=
(v ⊳(k(1) ⊲x)) ⊳k(2) = (v ⊳k) ⊳x
=
⟨x, (v ⊳k)(1) ⟩(v ⊳k)(2),
which shows that v(1)k(1) ⊗(v(2) ⊳k(2)) = (v ⊳k)(1) ⊗(v ⊳k)(2), i.e., that V is a right
relative (B, K)-module.
Thus, we see that the principal graph is given by the connected component the
Bratteli diagram of the inclusion bB ⊂bB>⊳K containing the trivial representation
of bB. Since bB>⊳K is the basic construction for the inclusion δ(K) ⊂bB, therefore
the Bratteli diagrams of the above two inclusions are the same.
Corollary 9.3.2. If N ⊂N>⊳B is a depth 2 inclusion corresponding to the quan-
tum groupoid B, then its principal graph is given by the Bratteli diagram of the
inclusion bBt ⊂bB.
Proof. In this case K = B and inclusion bBt ⊂bB is connected, so that δ(K) = bBt
(note that bB is biconnected).
References
[BS] S. Baaj and G. Skandalis, Unitaires multiplicatifs et dualit´e pour les produits crois´es de
C∗-alg´ebres, Ann. Sci. ENS., 26 (1993), 425–488.
[Ba] O. Babelon, Universal exchange algebra for Bloch waves and Liouville theory, Comm. Math.
Phys., 139 (1991), 619–643.
[ABRR] D. Arnaudon, E. Buﬀenoir, E. Ragoucy, and Ph. Roche, Universal Solutions of Quantum
Dynamical Yang-Baxter Equations, Lett.Math.Phys., 44 (1998), 201-214.
[BBB] O. Babelon, D. Bernard, and E. Billey, A Quasi-Hopf algebra interpretation of quantum
3-j and 6-j symbols and diﬀerence equations, Phys. Lett. B, 375 (1996), no. 1-4, 89–97.
[BM] R. Blattner, S. Montgomery, A duality theorem for Hopf module algebras, J. Algebra, 95
(1985), 153–172.
[Bo] G. B¨ohm, Doi-Hopf modules over weak Hopf algebras, preprint math.QA/9905027 (1999).
[BNSz] G. B¨ohm, F. Nill, and K. Szlach´anyi, Weak Hopf algebras I. Integral theory and C∗-
structure, J. Algebra, 221 (1999), 385–438.
[BSz1] G. B¨ohm, K. Szlach´anyi, A coassociative C∗-quantum group with nonintegral dimensions,
Lett. in Math. Phys, 35 (1996), 437–456.
FINITE QUANTUM GROUPOIDS AND THEIR APPLICATIONS
43
[BSz2] G. B¨ohm, K. Szlach´anyi, Weak Hopf algebras II. Representation Theory, Dimensions and
the Markov Trace, math.QA/9906045 (1999), to appear in J. Algebra.
[BSz3] G.
B¨ohm,
K.
Szlach´anyi,
Weak
C∗-Hopf
algebras
and
Multiplicative
Isometries,
math.QA/9810070 (1998), to appear in J. Operator Theory.
[D] M.-C. David, Paragroupe d’Adrian Ocneanu et algebre de Kac, Pacif. J. of Math., 172 (1996),
331–363.
[E1] M. Enock, Sous-facteurs interm´ediaires et groupes quantiques mesur´es, J. Operator Theory,
42 (1999), 305–330
[E2] M. Enock, Inclusions of von Neumann algebras and quantum groupoids, Inst. Math. de
Jussieu, Pr´epublication, 231 (1999).
[EVal] M. Enock and J.-M. Vallin, Inclusions of von Neumann algebras and quantum groupoids,
Inst. Math. de Jussieu, Pr´epublication, 156 (1998), to appear in J. Funct. Anal.
[EG] P. Etingof and S. Gelaki. Some properties of ﬁnite dimensional semisimple Hopf algebras,
Math. Res. Letters 5 (1998), 191-197.
[EN] P. Etingof, D. Nikshych, Dynamical quantum groups at roots of 1, preprint math.QA/0003221
(2000).
[ES] P. Etingof, O. Schiﬀmann, Lectures on the dynamical Yang-Baxter equations, preprint,
math.QA/9908064 (1999).
[ESS] P. Etingof, T. Schedler, and O. Schiﬀmann, Explicit quantization of dynamical r-matrices
for ﬁnite dimensional semisimple Lie algebras, preprint, math.QA/9912009 (1999).
[EV] P. Etingof, A. Varchenko, Exchange dynamical quantum groups, Comm. Math. Phys., 205
(1999), 19–52.
[Fe] G. Felder, Elliptic quantum groups, XIth International Congress of Mathematical Physics
(1994), 211–218, Internat. Press, Cambridge, (1995).
[GHJ] F. Goodman, P. de la Harpe, and V.F.R. Jones, Coxeter Graphs and Towers of Algebras,
M.S.R.I. Publ. 14, Springer, Heidelberg, 1989.
[H1] T. Hayashi, Face algebras. I. A generalization of quantum group theory, J. Math. Soc. Japan,
50 (1998), 293–315.
[H2] T. Hayashi, Face algebras and their Drinfel’d doubles, Algebraic groups and their generaliza-
tions: quantum and inﬁnite-dimensional methods (University Park, PA, 1991), 49–61, Proc.
Sympos. Pure Math., 56, Providence, RI, 1994.
[H3] T. Hayashi, Galois quantum groups of II1 subfactors, Tohoku Math. J., 51 (1999), 365–389.
[ILP] M. Izumi, R. Longo, and S. Popa, A Galois correspondence for compact groups of auto-
morphisms of von Neumann algebras with a generalization to Kac algebras, J. Funct. Anal.,
155 (1998), 25–63.
[KS] A. Klimyk and K. Schm¨udgen, Quantum groups and their representations, Springer Verlag
(1997).
[KY] H. Kosaki and S. Yamagami, Irreducible bimodules associated with crossed product algebras,
Intern. J. Math., 3 (1992), 661-676.
[J] V. Jones, Index for subfactors, Invent. math., 72 (1983), 1-25.
[JS] V. Jones and V.S. Sunder, Introduction to Subfactors, London Math. Soc. Lecture Notes
234, Cambridge University Press, 1997.
[Lu] J.-H. Lu, Hopf algebroids and quantum groupoids, Internat. J. Math., 7 (1996), 47–70.
[L] G. Lusztig, On quantum groups at roots of 1, Geom. Dedicata, 35 (1990), 89–113.
[M] S. Montgomery, Hopf Algebras and Their Actions on Rings, CBMS Regional Conference
Series in Mathematics, 82, AMS, 1993.
[Ma] S. Majid, Foundations of quantum group theory, Cambridge University Press, Cambridge,
(1995).
[Mal1] G. Maltsiniotis, Groupo¨ıdes quantiques, C. R. Acad. Sci. Paris, 314, Serie I (1992), 249-
252.
[Mal2] G. Maltsiniotis, Groupo¨ıdes quantiques, preprint, (1999).
[N] F. Nill, Axioms of Weak Bialgebras, math.QA/9805104 (1998).
[N1] D. Nikshych, Duality for actions of weak Kac algebras and crossed product inclusions of II1
factors, to appear in the Journal of Operator Theory, math.QA/9810049 (1998).
[N2] D. Nikshych, A duality theorem for quantum groupoids, to appear in Contemporary Mathe-
matics, math.QA/9912226 (1999).
[NTV] D. Nikshych, V. Turaev, and L. Vainerman, Quantum groupoids and invariants of knots
and 3-manifolds, math.QA/0006078 (2000).
44
DMITRI NIKSHYCH AND LEONID VAINERMAN
[NV1] D. Nikshych, L. Vainerman, Algebraic versions of a ﬁnite dimensional quantum groupoid,
Lecture Notes in Pure and Appl. Math., 209 (2000), 189-221.
[NV2] D. Nikshych, L. Vainerman, A characterization of depth 2 subfactors of II1 factors, J.
Func. Analysis, 171 (2000), 278-307.
[NV3] D. Nikshych, L. Vainerman, A Galois correspondence for II1 factors, math.QA/0001020
(2000).
[NSzW] F. Nill, K. Szlach´anyi, H.-W. Wiesbrock, Weak Hopf algebras and reducible Jones in-
clusions of depth 2, I : From crossed products to Jones towers, preprint math.QA/9806130
(1998).
[O1] A. Ocneanu, Quantized groups, string algebras and Galois theory for algebras, Operator
Algebras and Applications, Vol. 2, London Math. Soc. Lecture Notes Series 135, Cambridge
Univ. Press, Cambridge, U.K., (1988).
[O2] A. Ocneanu, Quantum Cohomology, Quantum groupoids and Subfactors unpublished talk
given at the First Caribbean School of Mathematics and Theoretical Physics, Guadeloupe,
(1993).
[P] R. Pierce, Associative algebras, Graduate Texts in Mathematics, 88, Springer Verlag, (1982).
[Po] S. Popa, Classiﬁcation of amenable subfactors of type II, Acta Math., 172 (1994), 163–255.
[PP1] M. Pimsner and S. Popa, Entropy and index for subfactors, Ann. Sci. Ecole Norm. Sup.,
19 (1986), no. 3, 57–106.
[PP2] M. Pimsner and S. Popa, Iterating the basic construction, Trans. Amer. Math. Soc., 310
(1988), no. 1, 127–133.
[R] J. Renault, A groupoid approach to C∗-algebras, Lecture Notes in Math. 793, Springer-Verlag,
1980.
[RT] N. Reshetikhin, V. Turaev, Invariants of 3-manifolds via link polynomials and quantum
groups, Invent. Math., 103 (1991), 547-597.
[S] W. Szyma´nski, Finite index subfactors and Hopf algebra crossed products, Proc. Amer. Math.
Soc., 120 (1994), no. 2, 519–528.
[Ta] M. Takeuchi, Relative Hopf modules – equivalencies and freeness criteria, J. Algebra, 60
(1979), 452-471.
[T] V. Turaev, Quantum invariants of knots and 3-manifolds, de Gruyter Studies in Mathematics,
18, Walter de Gruyter & Co., Berlin, (1994).
[V] L. Vainerman, A note on quantum groupoids, C. R. Acad. Sci. Paris, 315, Serie I (1992),
1125–1130.
[V1] J.-M. Vallin, Bimodules de Hopf et poids op´eratoriels de Haar, J. of Operator Theory, 35
(1996), 39–65.
[V2] J.-M. Vallin, Groupo¨ıdes quantiques ﬁnis, Universit´e d’Orl´eans, Pr´epublication, 6 (2000).
[W] Y. Watatani. Index for C∗-subalgebras, Memoirs AMS, 424 (1990).
[Xu] P. Xu, Quantum groupoids, preprint, math.QA/9905192 (1999).
[Y] T. Yamanouchi, Duality for generalized Kac algebras and a characterization of ﬁnite groupoid
algebras, J. Algebra, 163 (1994), 9–50.
UCLA, Department of Mathematics, 405 Hilgard Avenue, Los Angeles, CA 90095-
1555, USA
E-mail address: nikshych@math.ucla.edu
Universit´e de Strasbourg, D´epartement de Math´ematiques, 7, rue Ren´e Descartes,
F-67084 Strasbourg, France
E-mail address: wain@agrosys.kiev.ua, vaynerma@math.u-strasbg.fr
