---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties"
section_id: sec-029-b2-generic-representations-in-the-distinguished
section_title: "B.2 Generic representations in the distinguished component."
section_number: null
pages: 49-55
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties — This is a survey on Reidemeister torsion for hyperbolic thre e-manifolds of ﬁnite volume."
---
nent.
Next comes the proof of genericity results used in Paragraph 4.3.1. Recall the
notation
ρk1,k2 ∶= Symk1,k2 ρ.
Recall also that a character χ ∈X0(M 3) is called (k1, k2)-exceptional if there
exists a representation ρ ∈hom(π1M 3, SL2(C)) with character χρ = χ such that
H 0(M 3; ρk1,k2) ≠0. The set of (k1, k2)-exceptional characters is denoted by
Ek1,k2 .
Lemma B.9. If k1 ≠k2, then a (k1, k2)-exceptional character is reducible. In
particular the (k1, k2)-exceptional set Ek1,k2 is a ﬁnite subset of X0(M 3).
Proof. In the holomorphic case ( k2 = 0), assume that H 0(M 3; ρk) ≠0. Then
there is a non-trivial subspace of Ck+1 ﬁxed by Sym k(ρ(π1M 3)), where ρ(π1M 3)
denotes the Zariski closure of ρ(π1M 3). Since Sym k is irreducible, this means
that ρ(π1M 3) is not the full group SL 2(C), which in the holomorphic setting
means that ρ is reducible.
When k2 ≠0, one can only work with the real Zariski closure, and the
previous argument yields that either ρ is reducible or it is contained in a real
subgroup conjugate to PSL 2(R) or SU (2). The restriction of Sym k1 ⊗Symk2 to
those real subgroups is equivalent to Sym k1 ⊗Symk2 , which by Klebsh-Gordan
formula decomposes as
Symk1 ⊗Symk2 = Symk1+k2 ⊕ Symk1+k2−2 ⊕⋯ ⊕ Sym/divides.⊗lt0k1−k2/divides.⊗lt0. (60)
As k1 ≠k2 the powers of Sym in (60) are non-trivial, hence the argument in the
holomorphic case applies again.
Recall that we say that a property is generic when it holds true for a non-
empty Zariski open subset of X0(M 3), and that the ground ﬁeld is either C or
R, depending on whether the discussion is in the holomorphic setting, f or Sym k,
or not, for Sym k1,k2 .
Lemma B.10. Let M 3 be a hyperbolic manifold with one cusp and let k1 ≠k2 ∈
N be such that k1 or k2 is odd. Then the set
{χρ ∈X0(M 3) /divid⟩s.alt0 dim H 0(T 2; ρk1,k2) = 0}
49
is a non-empty Zariski open subset of the curve X0(M 3).
Proof. By upper semi-continuity of the dimension of the cohomology (see th e
proof of Proposition 3.16), it suﬃces to show that dim H 0(T 2; ρk1,k2 ) = 0 for
some representation ρ with character in X0(M 3). When k1 is odd and k2 is
even, or vice-versa, then it holds for the lift of the holonomy of the complete
structure, by Lemma B.5. If both k1 and k2 are odd, consider an orbifold Dehn
ﬁlling on M 3 with ﬁlling curve γ that consists in adding a solid torus with
singular core curve with branching order n. By the Dehn ﬁlling theorem, for n
large enough it is hyperbolic and the restriction ρ of its holonomy has character
in X0(M 3). The holonomy of the curve γ is conjugate to
ρ(γ) = − /par⟩nl⟩ft.alt4e
πi
n 0
0 e− πi
n
/par⟩nright.alt4 .
As the core of the geodesic has non-trivial length, the complex leng th of its
holonomy has nonzero real part. Thus we can ﬁnd a peripheral cur ve γ′ with
holonomy
ρ(γ′) = /par⟩nl⟩ft.alt4λ 0
0 1
λ
/par⟩nright.alt4
with λ not real nor unitary. This yields that ρk1,k2 (γ′) has no eigenvalue 1,
hence H 0(T 2; ρk1,k2) = 0.
Next lemma implies Lemma 4.12, as F k1,k2 = (X0(M 3) − Z k1,k2) ∪ Ek1,k2 .
Lemma B.11. Let M 3 be a hyperbolic manifold with one cusp and let k1 ≠k2 ∈
N be such that k1 and k2 are even.
(a) The set of characters
Z k1,k2 = {χρ ∈X0(M 3) /divid⟩s.alt0 dim H0(T 2; ρk1,k2 ) = 1}
is a non-empty Zariski open subset of the curve X0(M 3).
(b) For any [γ] ∈H 1(T 2; Z), [γ] ≠0, the set
Z k1,k2
γ = {χρ ∈Z k1,k2 /divid⟩s.alt0i∗(a ∩ [γ]) is a basis for H1(M 3; ρk1,k2 )}
is non-empty and Zariski open.
Proof. For (a), given any non-trivial peripheral element γ ∈π1T 2, for a generic
character χρ ∈X0(M 3), ρ(γ) is a diagonal matrix, with eigenvalues diﬀerent
from ±1 and so that ρk1,k2 (γ) has only one eigenvalue equal to one. This prop-
erty is in fact Zariski open (over C when k2 = 0, over R otherwise), cf. the proof
of Lemma B.10.
Next comes the proof of (b). Any nonzero element in H 1(T 2; Z) is repre-
sented by a simple closed curve γ. Consider the orbifold On obtained by Dehn
ﬁlling M 3 along γ, so that the soul of the solid torus is the branching locus,
with branching index n ∈N. For n suﬃciently large, On is hyperbolic, and
its holonomy restricts to a representation with character χρ ∈X0(M 3). As
Symk1 ⊗Symk2 of the holonomy of On is acyclic, a Mayer-Vietoris argument
50
yields that a ∩ γ is a basis for H 1(M 3; ρk1,k2 ). Then the argument for a generic
ρ follows from semi-continuity.
Notice that for all but ﬁnitely many curves γ we may take a trivial branching
index n = 1 and work with manifolds instead of orbifolds. However, in order to
consider all ﬁlling slopes, one needs to work with orbifolds.
For any character χρ in Z k1,k2
γ , by the long exact sequence in cohomology
and Poincar´ e duality, the inclusion induces an isomorphism, H2(M 3; ρk1,k2 ) ≅
H2(T 2; ρk1,k2 ). In addition, Poincar´ e duality again gives a natural isomor-
phism H2(T 2; ρk1,k2) ≅H 0(T 2; ρk1,k2 ) which yields that a ∩ [T 2] is a basis for
H2(T 2; ρk1,k2 ). Thus Lemma B.11(b) yields Proposition 4.13.
References
[1] M. Abert, N. Bergeron, I. Biringer, T. Gelander, N. Nikol ov, J. Raimbault, and I. Samet.
On the growth of L2-invariants for sequences of lattices in Lie groups. ArXiv e-prints ,
October 2012.
[2] I. Agol and N. M. Dunﬁeld. Certifying the Thurston norm vi a SL(2, C)-twisted homol-
ogy. ArXiv e-prints , January 2015.
[3] Dror Bar-Natan and Edward Witten. Perturbative expansi on of Chern-Simons theory
with noncompact gauge group. Comm. Math. Phys. , 141(2):423–440, 1991.
[4] Leila Ben Abdelghani. Espace des repr´ esentations du gr oupe d’un nœud classique dans
un groupe de Lie. Ann. Inst. Fourier (Grenoble) , 50(4):1297–1321, 2000.
[5] Leila Ben Abdelghani. Vari´ et´ e des caract` eres et slice ´ etale de l’espace des repr´ esentations
d’un groupe. Ann. Fac. Sci. Toulouse Math. (6) , 11(1):19–32, 2002.
[6] Nicolas Bergeron and Akshay Venkatesh. The asymptotic g rowth of torsion homology
for arithmetic groups. J. Inst. Math. Jussieu , 12(2):391–447, 2013.
[7] Michel Boileau and Joan Porti. Geometrization of 3-orbi folds of cyclic type. Ast´ erisque,
272:208, 2001. Appendix A by Michael Heusener and Porti.
[8] A. Borel and N. W allach. Continuous cohomology, discrete subgroups, and represent a-
tions of reductive groups , volume 67 of Mathematical Surveys and Monographs . Amer-
ican Mathematical Society, Providence, RI, second edition , 2000.
[9] Gerhard Burde. Darstellungen von Knotengruppen. Math. Ann. , 173:24–33, 1967.
[10] Danny Calegari. Real places and torus bundles. Geom. Dedicata, 118:209–227, 2006.
[11] A. Casella, F. Luo, and S. Tillmann. Pseudo-developing maps for ideal triangulations
II: Positively oriented ideal triangulations of cone-mani folds. ArXiv e-prints , September
2015.
[12] T. A. Chapman. Topological invariance of Whitehead tor sion. Amer. J. Math. , 96:488–
497, 1974.
[13] Jeﬀ Cheeger. Analytic torsion and the heat equation. Ann. of Math. (2) , 109(2):259–
322, 1979.
[14] Marshall M. Cohen. A course in simple-homotopy theory . Springer-Verlag, New York-
Berlin, 1973. Graduate Texts in Mathematics, Vol. 10.
[15] Marc Culler. Lifting representations to covering grou ps. Adv. in Math. , 59(1):64–70,
1986.
[16] Marc Culler and Peter B. Shalen. Varieties of group repr esentations and splittings of
3-manifolds. Ann. of Math. (2) , 117(1):109–146, 1983.
[17] G. de Rham, S. Maumary, and M. A. Kervaire. Torsion et type simple d’homotopie .
Expos´ es faits au s´ eminaire de Topologie de l’Universit´ ede Lausanne. Lecture Notes in
Mathematics, No. 48. Springer-Verlag, Berlin-New York, 19 67.
[18] Georges de Rham. Introduction aux polynˆ omes d’un nœud . Enseignement Math. (2) ,
13:187–194 (1968), 1967.
51
[19] Tudor Dimofte and Stavros Garoufalidis. The quantum co ntent of the gluing equations.
Geom. Topol., 17(3):1253–1315, 2013.
[20] Tudor Dimofte and Sergei Gukov. Quantum ﬁeld theory and the volume conjecture. In
Interactions between hyperbolic geometry, quantum topology and number theory , volume
541 of Contemp. Math. , pages 41–67. Amer. Math. Soc., Providence, RI, 2011.
[21] J´ erˆ ome Dubois. Non abelian Reidemeister torsion and volume form on the SU ( 2) -
representation space of knot groups. Ann. Inst. Fourier (Grenoble) , 55(5):1685–1734,
2005.
[22] J´ erˆ ome Dubois. A volume form on the SU ( 2) -representation space of knot groups.
Algebr. Geom. Topol. , 6:373–404, 2006.
[23] Jerome Dubois and Stavros Garoufalidis. Rationality o f the SL ( 2,C) -Reidemeister tor-
sion in dimension 3. Topology Proc., 47:115–134, 2016.
[24] J´ erˆ ome Dubois and Rinat Kashaev. On the asymptotic ex pansion of the colored Jones
polynomial for torus knots. Math. Ann. , 339(4):757–782, 2007.
[25] J´ erˆ ome Dubois and Yoshikazu Yamaguchi. The twisted Alexander polynomial for ﬁnite
abelian covers over three manifolds with boundary. Algebr. Geom. Topol. , 12(2):791–
804, 2012.
[26] Nathan M. Dunﬁeld, Stefan Friedl, and Nicholas Jackson . Twisted Alexander polyno-
mials of hyperbolic knots. Exp. Math. , 21(4):329–352, 2012.
[27] Nathan M. Dunﬁeld, Stavros Garoufalidis, Alexander Sh umakovitch, and Morwen
Thistlethwaite. Behavior of knot invariants under genus 2 m utation. New York J.
Math., 16:99–123, 2010.
[28] Stefano Francaviglia and Joan Porti. Rigidity of repre sentations in SO ( 4,1) for Dehn
ﬁllings on 2-bridge knots. Paciﬁc J. Math. , 238(2):249–274, 2008.
[29] W olfgang Franz. ¨Uber die Torsion einer ¨Uberdeckung. J. Reine Angew. Math. , 173:245–
254, 1935.
[30] W olfgang Franz. Torsionsideale, Torsionsklassen und Torsion. J. Reine Angew. Math. ,
176:113–124, 1936.
[31] Daniel S. Freed. Reidemeister torsion, spectral seque nces, and Brieskorn spheres. J.
Reine Angew. Math. , 429:75–89, 1992.
[32] David Fried. Analytic torsion and closed geodesics on h yperbolic manifolds. Invent.
Math., 84(3):523–540, 1986.
[33] Stefan Friedl and Stefano Vidussi. A survey of twisted A lexander polynomials. In The
mathematics of knots , volume 1 of Contrib. Math. Comput. Sci. , pages 45–94. Springer,
Heidelberg, 2011.
[34] William M. Goldman. The symplectic nature of fundament al groups of surfaces. Adv.
in Math. , 54(2):200–225, 1984.
[35] William M. Goldman. Invariant functions on Lie groups a nd Hamiltonian ﬂows of
surface group representations. Invent. Math. , 85(2):263–302, 1986.
[36] L. Guillou and A. Marin. Notes sur l’invariant de Casson des sph` eres d’homologie de
dimension trois. Enseign. Math. (2) , 38(3-4):233–290, 1992. With an appendix by
Christine Lescop.
[37] Sergei Gukov and Hitoshi Murakami. SL ( 2,C) Chern-Simons theory and the asymp-
totic behavior of the colored Jones polynomial. In Modular forms and string duality ,
volume 54 of Fields Inst. Commun. , pages 261–277. Amer. Math. Soc., Providence, RI,
2008.
[38] Robin Hartshorne. Algebraic geometry . Springer-Verlag, New York, 1977. Graduate
Texts in Mathematics, No. 52.
[39] M. Heusener, V. Munoz, and J. Porti. The SL(3,C)-charac ter variety of the ﬁgure eight
knot. ArXiv e-prints , May 2015.
[40] Michael Heusener. An orientation for the SU ( 2) -representation space of knot groups. In
Proceedings of the Paciﬁc Institute for the Mathematical Sc iences Workshop “Invari-
ants of Three-Manifolds” (Calgary, AB, 1999) , volume 127, pages 175–197, 2003.
52
[41] Michael Heusener and Joan Porti. Deformations of reduc ible representations of 3-
manifold groups into PSL 2( C) . Algebr. Geom. Topol. , 5:965–997, 2005.
[42] Michael Heusener and Joan Porti. Inﬁnitesimal project ive rigidity under Dehn ﬁlling.
Geom. Topol., 15(4):2017–2071, 2011.
[43] Michael Heusener, Joan Porti, and Eva Su´ arez Peir´ o. D eformations of reducible rep-
resentations of 3-manifold groups into SL 2( C) . J. Reine Angew. Math. , 530:191–227,
2001.
[44] Kazuhiro Hikami and Hitoshi Murakami. Representation s and the colored Jones poly-
nomial of a torus knot. In Chern-Simons gauge theory: 20 years after , volume 50 of
AMS/IP Stud. Adv. Math. , pages 153–171. Amer. Math. Soc., Providence, RI, 2011.
[45] Michael Kapovich. Deformations of representations of discrete subgroups of SO ( 3,1) .
Math. Ann. , 299(2):341–354, 1994.
[46] Michael Kapovich. On the dynamics of pseudo-Anosov hom eomorphisms on represen-
tation varieties of surface groups. Ann. Acad. Sci. Fenn. Math. , 23(1):83–100, 1998.
[47] R. M. Kashaev. The hyperbolic volume of knots from the qu antum dilogarithm. Lett.
Math. Phys. , 39(3):269–275, 1997.
[48] Paul Kirk and Charles Livingston. Twisted Alexander in variants, Reidemeister torsion,
and Casson-Gordon invariants. Topology, 38(3):635–661, 1999.
[49] T. Kitano. Reidemeister torsion of a 3-manifold obtain ed by a Dehn-surgery along the
ﬁgure-eight knot. ArXiv e-prints , June 2015.
[50] Teruaki Kitano. Reidemeister torsion of Seifert ﬁbere d spaces for SL ( 2; C) -
representations. Tokyo J. Math. , 17(1):59–75, 1994.
[51] Teruaki Kitano. Reidemeister torsion of the ﬁgure-eig ht knot exterior for SL ( 2; C) -
representations. Osaka J. Math. , 31(3):523–532, 1994.
[52] Teruaki Kitano. Reidemeister torsion of Seifert ﬁbere d spaces for SL ( n; C) -
representations. Kobe J. Math. , 13(2):133–144, 1996.
[53] Teruaki Kitano. Twisted Alexander polynomial and Reid emeister torsion. Paciﬁc J.
Math., 174(2):431–442, 1996.
[54] Teruaki Kitano and Takayuki Morifuji. Twisted Alexand er polynomials for irreducible
SL( 2,C) -representations of torus knots. Ann. Sc. Norm. Super. Pisa Cl. Sci. (5) ,
11(2):395–406, 2012.
[55] Takahiro Kitayama and Yuji Terashima. Torsion functio ns on moduli spaces in view of
the cluster algebra. Geom. Dedicata, 175:125–143, 2015.
[56] Sean Lawton. Generators, relations and symmetries in p airs of 3 ×3 unimodular matrices.
J. Algebra, 313(2):782–801, 2007.
[57] Xiao Song Lin. Representations of knot groups and twist ed Alexander polynomials.
Acta Math. Sin. (Engl. Ser.) , 17(3):361–380, 2001.
[58] Alexander Lubotzky and Andy R. Magid. Varieties of repr esentations of ﬁnitely gener-
ated groups. Mem. Amer. Math. Soc. , 58(336):xi+117, 1985.
[59] Gw´ ena¨ el Massuyeau. An introduction to the abelian Re idemeister torsion of three-
dimensional manifolds. Ann. Math. Blaise Pascal , 18(1):61–140, 2011.
[60] Pere Menal-Ferrer and Joan Porti. Local coordinates fo r SL ( n,C) -character varieties of
ﬁnite-volume hyperbolic 3-manifolds. Ann. Math. Blaise Pascal , 19(1):107–122, 2012.
[61] Pere Menal-Ferrer and Joan Porti. Mutation and SL ( 2,C) -Reidemeister torsion for
hyperbolic knots. Algebr. Geom. Topol. , 12(4):2049–2067, 2012.
[62] Pere Menal-Ferrer and Joan Porti. Twisted cohomology f or hyperbolic three manifolds.
Osaka J. Math. , 49(3):741–769, 2012.
[63] Pere Menal-Ferrer and Joan Porti. Higher-dimensional Reidemeister torsion invariants
for cusped hyperbolic 3-manifolds. J. Topol., 7(1):69–119, 2014.
[64] John J. Millson. A remark on Raghunathan’s vanishing th eorem. Topology, 24(4):495–
498, 1985.
[65] J. Milnor. Whitehead torsion. Bull. Amer. Math. Soc. , 72:358–426, 1966.
53
[66] John Milnor. Two complexes which are homeomorphic but c ombinatorially distinct.
Ann. of Math. (2) , 74:575–590, 1961.
[67] John Milnor. A duality theorem for Reidemeister torsio n. Ann. of Math. (2) , 76:137–
147, 1962.
[68] John W. Milnor. Inﬁnite cyclic coverings. In Conference on the Topology of Manifolds
(Michigan State Univ., E. Lansing, Mich., 1967) , pages 115–133. Prindle, W eber &
Schmidt, Boston, Mass., 1968.
[69] Takayuki Morifuji. Representations of knot groups int o SL ( 2,C) and twisted Alexander
polynomials. In Handbook of group actions. Vol. I , volume 31 of Adv. Lect. Math.
(ALM), pages 527–576. Int. Press, Somerville, MA, 2015.
[70] W erner M¨ uller. Analytic torsion and R-torsion of Riem annian manifolds. Adv. Math. ,
28:233–305, 1978.
[71] W erner M¨ uller. Analytic torsion andR-torsion for unimodular representations. J. Amer.
Math. Soc. , 6(3):721–753, 1993.
[72] W erner M¨ uller. The asymptotics of the Ray-Singer anal ytic torsion of hyperbolic 3-
manifolds. In Metric and diﬀerential geometry , volume 297 of Progr. Math. , pages
317–352. Birkh¨ auser/Springer, Basel, 2012.
[73] W erner M¨ uller and Jonathan Pfaﬀ. The analytic torsion and its asymptotic behaviour
for sequences of hyperbolic manifolds of ﬁnite volume. J. Funct. Anal. , 267(8):2731–
2786, 2014.
[74] W erner M¨ uller and Jonathan Pfaﬀ. The analytic torsion and its asymptotic behaviour
for sequences of hyperbolic manifolds of ﬁnite volume. J. Funct. Anal. , 267(8):2731–
2786, 2014.
[75] Vicente Mu˜ noz and Joan Porti. Geometry of the SL ( 3,C) –character variety of torus
knots. Algebr. Geom. Topol. , 16(1):397–426, 2016.
[76] Hitoshi Murakami. The coloured Jones polynomial, the C hern-Simons invariant, and
the Reidemeister torsion of the ﬁgure-eight knot. J. Topol., 6(1):193–216, 2013.
[77] Hitoshi Murakami and Jun Murakami. The colored Jones po lynomials and the simplicial
volume of a knot. Acta Math. , 186(1):85–104, 2001.
[78] W alter D. Neumann. Combinatorics of triangulations an d the Chern-Simons invariant
for hyperbolic 3-manifolds. In Topology ’90 (Columbus, OH, 1990) , volume 1 of Ohio
State Univ. Math. Res. Inst. Publ. , pages 243–271. de Gruyter, Berlin, 1992.
[79] W alter D. Neumann and Don Zagier. Volumes of hyperbolic three-manifolds. Topology,
24(3):307–332, 1985.
[80] Liviu I. Nicolaescu. The Reidemeister torsion of 3-manifolds , volume 30 of de Gruyter
Studies in Mathematics . W alter de Gruyter & Co., Berlin, 2003.
[81] Tomotada Ohtsuki and Toshie Takata. On the Kashaev inva riant and the twisted Rei-
demeister torsion of two-bridge knots. Geom. Topol., 19(2):853–952, 2015.
[82] Joan Porti. Torsion de Reidemeister pour les vari´ et´ es hyperboliques. Mem. Amer. Math.
Soc., 128(612):x+139, 1997.
[83] Joan Porti. Mayberry-Murasugi’s formula for links in h omology 3-spheres. Proc. Amer.
Math. Soc. , 132(11):3423–3431 (electronic), 2004.
[84] M. S. Raghunathan. On the ﬁrst cohomology of discrete su bgroups of semisimple Lie
groups. Amer. J. Math. , 87:103–139, 1965.
[85] Jean Raimbault. Exponential growth of torsion in abeli an coverings. Algebr. Geom.
Topol., 12(3):1331–1372, 2012.
[86] Kurt Reidemeister. Homotopieringe und Linsenr¨ aume. Abh. Math. Semin. Univ. Hamb. ,
11:102–109, 1935.
[87] Daniel Ruberman. Mutation and volumes of knots in S3. Invent. Math. , 90(1):189–215,
1987.
[88] Kevin P. Scannell. Local rigidity of hyperbolic 3-mani folds after Dehn surgery. Duke
Math. J. , 114(1):1–14, 2002.
[89] Daniel S. Silver and Susan G. Williams. Mahler measure, links and homology growth.
Topology, 41(5):979–991, 2002.
54
[90] Ya¸ sar S¨ ozen. On a volume element of a Hitchin componen t. Fund. Math., 217(3):249–
264, 2012.
[91] Ya¸ sar S¨ ozen. Symplectic chain complex and Reidemeister torsion of compact manifolds.
Math. Scand. , 111(1):65–91, 2012.
[92] William P. Thurston. Three-dimensional manifolds, Kl einian groups and hyperbolic
geometry. Bull. Amer. Math. Soc. (N.S.) , 6(3):357–381, 1982.
[93] William P. Thurston. Three-dimensional geometry and topology. Vol. 1 , volume 35
of Princeton Mathematical Series . Princeton University Press, Princeton, NJ, 1997.
Edited by Silvio Levy.
[94] A. T. Tran. Reidemeister torsion and Dehn surgery on twi st knots. ArXiv e-prints ,
June 2015.
[95] V. G. Turaev. Reidemeister torsion in knot theory. Uspekhi Mat. Nauk , 41(1(247)):97–
147, 240, 1986.
[96] Vladimir Turaev. Introduction to combinatorial torsions . Lectures in Mathematics ETH
Z¨ urich. Birkh¨ auser Verlag, Basel, 2001. Notes taken by Felix Schlenk.
[97] Vladimir Turaev. Torsions of 3-dimensional manifolds , volume 208 of Progress in
Mathematics. Birkh¨ auser Verlag, Basel, 2002.
[98] `E. B. Vinberg and V. L. Popov. Invariant theory. In Algebraic geometry, 4 (Russian) ,
Itogi Nauki i Tekhniki, pages 137–314, 315. Akad. Nauk SSSR, Vsesoyuz. Inst. Nauchn.
i Tekhn. Inform., Moscow, 1989.
[99] Masaaki W ada. Twisted Alexander polynomial for ﬁnitel y presentable groups. Topology,
33(2):241–256, 1994.
[100] Andr´ e W eil. Remarks on the cohomology of groups. Ann. of Math. (2) , 80:149–157,
1964.
[101] Pierre Will. Groupes libres, groupes triangulaires et tore ´ epoint´ e da ns PU(2,1) .
PhD thesis, Universit´ e Pierre et Marie Curie – Paris VI, 200 6. Available at
http://hal.archives-ouvertes.fr/tel-00130785v1 .
[102] Edward Witten. Quantum ﬁeld theory and the Jones polyn omial. Comm. Math. Phys. ,
121(3):351–399, 1989.
[103] Edward Witten. On quantum gauge theories in two dimens ions. Comm. Math. Phys. ,
141(1):153–209, 1991.
[104] Artur W otzke. Die Ruellsche Zetafunktion und die anal ytische Torsion hyperbolischer
Mannigfaltigkeiten. Bonner Mathematische Schriften, Nr. 389., PhD thesis, Bonn, 2008.
[105] Y. Yamaguchi. A surgery formula for the asymptotics of the higher dimensional Reide-
meister torsion and Seifert ﬁbered spaces. ArXiv e-prints , October 2012.
[106] Y. Yamaguchi. The asymptotic behavior of the Reidemei ster torsion for Seifert manifolds
and PSL(2;R)-representations of Fuchsian groups. ArXiv e-prints , October 2014.
[107] Yoshikazu Yamaguchi. Limit values of the non-acyclic Reidemeister torsion for knots.
Algebr. Geom. Topol. , 7:1485–1507, 2007.
[108] Yoshikazu Yamaguchi. Higher even dimensional Reidem eister torsion for torus knot
exteriors. Math. Proc. Cambridge Philos. Soc. , 155(2):297–305, 2013.
[109] Yoshikazu Yamaguchi. Twisted Alexander polynomials , character varieties and Reide-
meister torsions of double branched covers. Topology Appl., 204:278–305, 2016.
[110] Yoshiyuki Yokota. From the Jones polynomial to the A-polynomial of hyperbolic knots.
In Proceedings of the Winter Workshop of Topology/Workshop of Topology and Com-
puter (Sendai, 2002/Nara, 2001) , volume 9, pages 11–21, 2003.
Departament de Matem `atiques
Universitat Aut`onoma de Barcelona.
08193 Bellaterra, Spain
and
Barcelona Graduate School of Mathematics (BGSMath)
porti@mat.uab.cat
55
