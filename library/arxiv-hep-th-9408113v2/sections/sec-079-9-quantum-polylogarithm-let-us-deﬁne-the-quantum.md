---
doc_id: arxiv-hep-th-9408113v2
doc_title: "Dilogarithm identities"
section_id: sec-079-9-quantum-polylogarithm-let-us-deﬁne-the-quantum
section_title: "(Quantum polylogarithm). Let us deﬁne the quantum polyloga rithm as the following"
section_number: 9
pages: 86-96
source_pdf: 9408113v2.pdf
source_sha256: dadd96e1155e820f
doc_brief: "Dilogarithm identities — We study the dilogarithm identities from algebraic, analytic, asymptotic, K-theoretic, combinatorial and representation-theoretic points of view."
---
formal series (k≥ 1)
Lik(x;q) :=
∑
n≥1
xn
n(1−qn)k−1. (10)
• Prove that (k≥ 2)
exp (Lik(x;q)) =
∏
m=(m1,...,mk−2)∈Zk−2
+
eq(q|m|x), (11)
where|m| :=m1 +... +mk−2.
Hint: it is clear that Lik(x;q)−Lik(qx;q) = Lik−1(x;q). Consequently,
Lik(x;q) =
∑
m≥0
Lik−1(qmx;q),
exp (Lik(x;q)) =
∏
m≥0
exp (Lik−1(qmx;q)).
• (Functional equation for quantum trilogarithm). Prove tha t if x and y satisfy the
Weyl relation xy =qyx, then
exp (Li3(x;q)) exp (Li3(y;q)) = exp (Li3(y;q)) exp (Li3((y)∞x;q)) (12)
= exp (Li3(y(x)∞;q)) exp (Li3(x;q)).
Dilogarithm identities 87
It is a very intertesting task to study the asymptotic behavi or of the quantum polyloga-
rithm functional equations (see e.g. (2.64), (2.65) and (9) , (11), (12)) when q =ζe−ǫ→ 1,
ǫ→ 0, where ζ = exp
(2πi
l
)
. We intended to consider this interesting subject in [Kir10 ].
Appendix.
Proof of Proposition E, n = 2, A = 1. We have the following series of relations coming
from the functional equation (1.4):
• L(β1/α2) +L(α2x1)−L(β1x1)−L
(β1(1−α2x1)
α2(1−β1x1)
)
−L
((α2−β1)x1
1−β1x1
)
= 0,
• L(β1/α1) +L(α1x2)−L(β1x2)−L
(β1(1−α1x2)
α1(1−β1x2)
)
−L
((α1−β1)x2
1−β1x2
)
= 0,
• L(β2/α1) +L(α1x1)−L(β2x1)−L
(β2(1−α1x1)
α1(1−β2x1)
)
−L
((α1−β2)x1
1−β2x1
)
= 0,
• L(β2/α2) +L(α2x2)−L(β2x2)−L
(β2(1−α2x2)
α2(1−β2x2)
)
−L
((α2−β2)x2
1−β2x2
)
= 0,
• L
((α1−β1)x2
1−β1x2
)
+L
((α2−β1)x1
1−β1x1
)
−L(t)−L
(x1(α2−β1)(1−β2x2)
(1−β1x1)(1−α2x2)
)
−L
(x2(α1−β1)(1−β2x1)
(1−β1x2)(1−α1x1)
)
= 0,
• L
((α1−β2)x1
1−β2x1
)
+L
((α2−β2)x2
1−β2x2
)
−L(t)−L
(x1(α1−β2)(1−β1x2)
(1−β2x1)(1−α1x2)
)
−L
(x2(α2−β2)(1−β1x1)
(1−β2x2)(1−α2x1)
)
= 0,
• L
(β1(1−α2x1)
α2(1−β1x1)
)
+L
(β2(1−α1x1)
α1(1−β2x1)
)
−L
(β1β2(1−t)
α1α2
)
−L
(β1(1−α2x1)(1−β2x2)
(1−β1x1)(α2−β2)
)
−L
(β2(1−α1x1)(1−β1x2)
(1−β2x1)(α1−β1)
)
= 0,
• L
(β1(1−α1x2)
α1(1−β1x2)
)
+L
(β2(1−α2x2)
α2(1−β2x2)
)
−L
(β1β2(1−t)
α1α2
)
−L
(β1(1−α1x2)(1−β2x1)
(1−β1x2)(α1−β2)
)
−L
(β2(1−α2x2)(1−β1x1)
(1−β2x2)(α2−β1)
)
= 0,
• L
((α2−β2)x2(1−β1x1)
(1−α2x1)(1−β2x2)
)
+L
(β1(1−α2x1)(1−β2x2)
(α2−β2)(1−β1x1)
)
−L (x2β1)
−L
( −β1/α1
1−β1/α1
)
−L
( −α1x2
1−α1x2
)
= 0,
• L
((α1−β1)x2(1−β2x1)
(1−α1x1)(1−β1x2)
)
+L
(β2(1−α1x1)(1−β1x2)
(α1−β1)(1−β2x1)
)
−L (x2β2)
88 Anatol N. Kirillov
−L
( −β2/α2
1−β2/α2
)
−L
( −α2x2
1−α2x2
)
= 0,
• L
((α2−β1)x1(1−β2x2)
(1−α2x2)(1−β1x1)
)
+L
(β2(1−α2x2)(1−β1x1)
(α2−β1)(1−β2x2)
)
−L (x1β2)
−L
( −β2/α1
1−β2/α1
)
−L
( −α1x1
1−α1x1
)
= 0,
• L
((α1−β2)x1(1−β1x2)
(1−α1x2)(1−β2x1)
)
+L
(β1(1−α1x2)(1−β2x1)
(α1−β2)(1−β1x2)
)
−L (x1β1)
−L
( −β1/α2
1−β1/α2
)
−L
( −α2x1
1−α2x1
)
= 0.
Let us denote by S the LHS of the sum of all of these relations. Let D be a diﬀerence
between the LHS and the RHS of the identity from Proposition E . Then one can check
S =−2D−
∑
i,j
{
L(αixj) +L
( −αixj
1−αixj
)
− 2L(αi/αj)
}
+ 2L(1) = 0.
But it follows from the integral representation (1.2) that a function
l(t) :=
∑
i,j
{
L(αixj(t)) +L
( −αixj(t)
1−αixj(t)
)}
does not depend on t. Taking t = 1 one can ﬁnd this constant. The result is
l(t) = 2
∑
L(αi/αj) + 2L(1),
consequently,D = 0.
Note that the next Lemma and identities (A1)-(A2) had played the key role in the
proving of Proposition E.
Lemma A1. Letr(x,t ) be a polynomial as in Proposition E. Then we have
i)
(
1− Aβ1...β n
α1...α n
(1−t)
) n∏
l=1
(1−βxl) =
n∏
l=1
(
1− β
αl
)
, where β = βk for some k,
1≤k≤n,
ii)
(
1− Aβ1...β n
α1...α n
(1−t)
) n∏
l=1
(1−αxl) = −(1−t)
n∏
l=1
(
1− βl
α
)
, where α = αk for
some k, 1≤k≤n.
Corollary (of Lemma A1, with n = 2). We have
1− (α1−β1)x2(1−β2x1)
(1−β1x2)(1−α1x1) =− (α1−β1)(α1−β2)
(1−β1x2)(1−α1x1)(α1α2−β1β2(1−t)), (A1)
1− β1(1−β2x2)(1−α2x1)
(α2−β2)(1−β1x1) = α1(α2−β1)
(1−β1x1)(α1α2−β1β2(1−t)). (A2)
Dilogarithm identities 89
References*
[A] K. Aomoto. Addition theorem of Abel type for hyper-logar ithms. Nagoya Math. J. ,
1982, v.88, 55-71.
[AL] D. Acreman and J.H. Loxton. Asymptotic analysis of Rama nujan pairs. Aequat. Math. ,
1986, v.30, 106-117.
[An1] G. Andrews. The theory of partitions. Addison-Wesley Publishing Company , 1976.
[An2] G. Andrews. Multiple series Rogers-Ramanujan type id entities. Paciﬁc J. Math. , 1984,
v.114, 267-283.
[An3] G. Andrews. q-series: their development and application in analysis, nu mber theory,
combinatorics, physics, and computer algebra. Regional conference series in mathe-
matics, ISSN 0160-7642 , 1985, no.66.
[ABBFV] G. Andrews, R. Baxter, D. Bressoud, W. Burge, P. Forr ester and G. Viennot. Partitions
with prescribed hook diﬀerences. Europ. J. Combinatorics , 1987, v.8, 341-350.
[ABF] G. Andrews, R. Baxter and P. Forrester. Eight-vertex SOS -model and generalized
Rogers-Ramanujan-type identities. J. Stat. Phys. , 1984, v.35, 193-266.
[AB] G. Andrews and D. Bressoud. On the Burge correspondence between partitions and
binary words. Rocky Mtn. J. Math. , 1985, v.15, 225-233.
[AAB] A. Agarwal, G. Andrews and D. Bressoud. The Bailey latt ice. J. Indian Math. Soc. ,
1987, v.51, 57-73.
[B] W. Bailey. Identities of the Rogers-Ramanujan type. Proc. London Math. Soc. (2) ,
1949, v.50, 1-10.
[BR] V. Bazhanov and N. Reshetikhin. Restricted solid-on-s olid models connected with
simply laced algebras and conformal ﬁeld theory. J. Phys. A , 1990, v.23, 1477-1492.
[BGSV] A. Beilinson, A. Goncharov, V. Schechtman and A. Varc henko. Aomoto dilogarithm,
mixed Hodge structures, and motivic cohomology of pairs of t riangles on the plane. The
Grothendieck Festschrift, vol.1, Birkhauser, Progress in Math. Series, Boston , 1990,
v.86, 135-172.
[Ber] A. Berkovich. Fermionic counting of RSOS-states and V irasoro character formulas for
the unitarity minimal series M (ν,ν + 1). Exact results. Preprint Univ. Bonn , 1994,
31p.; hep-th/9403073.
[Bl] S. Bloch. Application of the dilogarithm function in al gebraic K-theory and algebraic
geometry. Proc. of the International Symp. on Alg. Geom.(Kyoto Univ., Kyoto,1977),
103-114, Kinokuniya Book Store, Tokyo, 1978.
[BS] P. Bouwknegt and K. Schoutens. W symmetry in Conformal Field Theory. Phys. Rep. ,
1993, v.223, 183-276.
[Bre1] D. Bressoud. Analytic and combinatorial generaliza tion of the Rogers-Ramanujan iden-
tities. Mem. Amer. Math. Soc. , 1980, v.224, 54p.
* Most of the following are referred in our lectures. All are r elevant in one way or the
other to the topics presented.
90 Anatol N. Kirillov
[Bre2] D. Bressoud. An easy proof of the Rogers-Ramanujan id entities. J. Number Theory ,
1983, v.16, 235-241.
[Bre3] D. Bressoud. Problems on the Z-statistic. Discrete Math. , 1988/89, v.73, 37-48.
[Bre4] D. Bressoud. Lattice paths and the Rogers-Ramanujan identities. Lect, Notes in Math. ,
1987, v.1395, 140-172.
[Bre5] D. Bressoud. In the land of OZ. in ” q-series and partitions” (ed. D. Stanton), IMA
Volumes in Math. and Applic., v.18, Springer-Verlag, New-Y ork, 1989, 45-55.
[Bre6] D. Bressoud. The Bailey lattice: an introduction. In Ramanujan Revisited (G. Andrews
et al. eds.), Academic Press, Inc. , 1988, 57-67.
[Bro1] J. Browkin. Conjectures on the dilogarithm. In K-theory, 1989, v.3, 29-56.
[Bro2] J. Browkin. K-theory, cyclotomic equations and Clansen’s functions. In [Le4], Chapter
11, 233-273.
[Bry] R.K. Brylinski. Limits of weight spaces, Lusztig’s q-analog and ﬁberings of adjoint
orbits. J. Amer. Math. Soc. , 1989, v.2, 517-533.
[Bur] W. Burger, A three-way correspondence between partit ions. Eorop. J. Comb. , 1982,
v.3, 195-213.
[Ca] J.L. Cathelineau. Homologie du groupe lineaire et poly logarithmes. Seminaire BOUR-
BAKI, 1992-93, n0 772, 23p.
[Co] H.S.M. Coxeter. The functions of Schl¨ aﬂi and Lobachev sky. Quart. J. Math. Oxford
Ser., 1935, v.6, 13-29.
[D1] S. Dasmahapatra. String hypothesis and characters of c oset CFTs. Preprint IC/93/91,
1993, 13p.
[D2] S. Dasmahapatra. On state counting and characters. City Univ. Preprint , 1994, 22p.
[DJKMO1] E. Date, M. Jimbo, A. Kuniba, T. Miwa and M. Okado. Ex actly solvable SOS models
II: Proof of the star-triangle relation and combinatorial i dentities. Adv. Studies in
Pure Math. , 1988, v.16, 17-122.
[DJKMO2] E. Date, M. Jimbo, A. Kuniba, T. Miwa and M. Okado. Pa th, Maya Diagrams and
representations of ˆsl(r, C). Adv. Studies in Pure Math. , 19, v., 149-191.
[DKKMM] S. Dasmahapatra, R. Kedem, T.R. Klassen, B.M. McCoy and E. Melzer. Quasi-
particles, Conformal Field Theory, and q-series. Int. J. Modern Phys. , 1993, v.7,
3617-3648.
[DKMM] S. Dasmahapatra, R. Kedem, B.M. McCoy and E. Melzer. V irasoro characters from
Bethe equations for the critical ferromagnetic three-stat e Potts model. J. Stat. Phys. ,
1994, v.74, 239-274.
[DS] J.L. Dupont and C.-H. Sah. Dilogarithm identities in Co nformal Field Theory and
group homology. Preprint, 1993.
[EKK] F. Essler, V.E. Korepin and K. Schoutens. Fine structu re of the Bethe ansatz for the
spin- 1
2 Heisenberg XXX model. J. Phys. A: Math. Gen. , 1992, v.25, 4115-4126.
[FK] L.D. Faddeev and R.M. Kashaev. Quantum dilogarithm. Preprint, 1993, 8p.
[FV] L.D. Faddeev and A.Yu. Volkov. Abelian current algebra and the Virasoro algebra on
the lattice. Preprint HU-TFT-93-29 , 1993.
Dilogarithm identities 91
[FeFr] B. Feigin and E. Frenkel. Coinvariants of nilpotent s ubalgebras of the Virasoro algebra
and partition identities. Advances in Soviet Mathematics , 1993, v.9.
[FF] B. Feigin and D. Fuchs. Representations of the Virasoro algebra. in ”Representa-
tions of inﬁnite-dimensional Lie groups and Lie algebras” , eds. A.M. Vershik and D.P.
Zhelobenko, Gordon and Breach, 1990, 465-554.
[FeNO] B. Feigin, T. Nakanishi and H. Ooguri. The annihilati ng ideals of minimal models. Int.
J. Mod. Phys. , 1992, v.1A, 217-238.
[FeSt] B.L. Feigin and A.V. Stoyanovsky. Quasi-particles m odels for the representations of
Lie algebras and geometry of ﬂag manifold. Preprint, 1993, 35p.
[Fi] S. Fishel. The combinatorics of certain entries in the t wo-parameter Kostka matrix.
Preprint, 1993, 9p.
[Fo] D. Foata. Distribution eul´ eriennes et manoniennes su r le group des permutations. in
Higher Combinatorics , [M. Aigner, ed. Berlin, 1976], p.27-49, Amsterdam, D. Reid el,
1977 (Proc. NATO Adv. Study Inst.)
[FQ] O. Foda and Y.-H. Quano. Virasoro character identities from the Andrews-Bailey
construction. Univ. Melbourne Preprint No.26 , 1994, 18p.
[FB] P. Forrester and R. Baxter. Further exact solutions of t he eight-vertex SOS model
and generalizations of the Rogeres-Ramanujan identities. J. Stat. Phys. , 1985, v.38,
435-472.
[FrSz1] E. Frenkel and A. Szenes. Dilogarithm identities, q-diﬀerence equations and the Vira-
soro algebra. Duke Math. J., Int. Math. Res. Notices , 1993, v.2, 53-60.
[FrSz2] E. Frenkel and A. Szenes. Crystal bases, dilogarith m identities and torsion in algebraic
K-groups. Preprint, 1993, 33p.
[Ga] A. Garsia. Orthogonality of Milne’s polynomials and ra ising operators. Discrete Math.,
1992, v.99, 247-264.
[GM] A. Garsia and S. Milne. A Rogers-Ramanujan bijection. J. Comb. Theory, Ser. A ,
1981, v.31, 289-339.
[GR] G. Gasper and M. Rahman. Basic hypergeometric series. Cambridge Univ. Press ,
1990.
[GS] I. Gessel and D. Stanton. Applications of q-Lagrange inversion to basic hypergeometric
series. Trans. Amer. Math. Soc. , 1983, v.277, 173-201.
[Gre] J. Greene. Bijections related to statistics on words. Discrete Math. , 1988, v.68, 15-29.
[GKO] P. Goddard, A. Kent, and D. Olive. Virasoro algebras an d coset space models. Phys.
Lett., 1985, v.B152, 88-93.
[GW] F. Goodman and H. Wenzl. Littlewood-Richardson coeﬃci ents for Hecke algebras at
roots of unity. Adv. Math. , 1990, v.82, 244-265.
[Go] A, Goncharov. Hyperlogarithms, mixed Tate motives and multipleζ-numbers. Preprint
MSRI-058-93, 1993, 35p.
[Han] G.-N. Han. Une courte d´ emonstration d’un resultat su r la Z-statistique. C.R. Acad.
Sci. Paris, Serie I , 1992, t.314, 969-971.
92 Anatol N. Kirillov
[JKS] U. Jannsen, S. Kleiman and J.-P. Serre (eds). Motives. Proc. Symp. in Pure Math. ,
AMS, Providence, 1994, v.55, part 2.
[JMMO] M. Jimbo, K.C. Misra, T. Miwa and M. Okado. Combinator ics of representations of
Uq(ˆsl(n)) at q = 0. Commun. in Math. Phys. , 1991, v.136, 543-566.
[Kac] V.G. Kac. Inﬁnite dimensional Lie algebras. Cambridge Univ. Press , 1990.
[KP] V. Kac and D. Peterson. Inﬁnite-dimensional Lie algebr as, theta functions and modular
forms. Adv. Math. , 1984, v.53, 125-264.
[KW1] V. Kac and M. Wakimoto. Modular invariant representat ions of inﬁnite-dimensional
Lie algebras and superalgebras. Proc. Natl. Acad. Sci. USA , 1988, v.85, 4956-4960.
[KW2] V. Kac and M. Wakimoto. Modular and conformal invarian ce constraints in represen-
tation theory of aﬃne algebras. Adv. Math. , 1988, v.70, 156-236.
[KW3] V. Kac and M. Wakimoto. Integrable highest weight modu les over aﬃne superalgebras
and number theory. Preprint, 1994, 44p.
[KKMMNN] S.-J. Kang, M. Kashiwara, K.C. Misra, T. Miwa, T. Na kashima and A. Nakayashiki.
Aﬃne crystals and vertex models. Int. J. Mod. Phys. , 1992, v.A7, 449-484.
[Ka] M. Kashiwara. On the crystal bases of the q-analog of universal enveloping algebras.
Duke Math. J. , 1991, v.63, 465-516.
[K] R. Kaufmann. Pathspace decompositions for the Virasoro algebra and its Verma mod-
ules. Preprint Bonn-TH-94-05 , 1994, 19p. and hep-th/9405041.
[KKMM1] R. Kedem, T.R. Klassen, B.M. McCoy and E. Melzer. Fer mionic quasi-particle rep-
resentations for characters of ( G(1))1× (G(1))1/(G(1))2. Phys. Lett. , 1993, v.B304,
263-270.
[KKMM2] R. Kedem, T.R. Klassen, B.M. McCoy and E. Melzer. Fer mionic sum representations
for conformal ﬁeld theory characters. Phys. Lett. , 1993, v.B307, 68-76.
[KeMa] R. Kedem and B.M. McCoy. Construction of modular bran ching functions from Bethe’s
equations in the 3-state Potts chain. J. Stat. Phys. , 1993, v.71, 865-901.
[KMM] R. Kedem, B.M. McCoy and E. Melzer. The sums of Rogers, S chur and Ramanujan
and Bose-Fermi correspondence in 1+1-dimensional quantum ﬁeld theory. Preprint
ITP-SB-93-19, 1993, 27p.
[Kir1] A.N. Kirillov. Combinatorial identities and comple teness of states for the generalized
Heisenberg magnet. Zap. Nauch. Sem. LOMI (in Russian) , 1984, v. 131, 88-105.
[Kir2] A.N. Kirillov. Completeness of the Bethe vectors for generalized Heisenberg magnet.
Zap. Nauch. Sem. LOMI (in Russian) , 1984, 134, 169-189.
[Kir3] A.N. Kirillov. On the Kostka-Green-Foulkes polynom ials and Clebsch-Gordan num-
bers. Journ. Geom. and Phys. , 1988, v.5, p.365-389.
[Kir4] A.N. Kirillov. On identities for the Rogers dilogari thm function related to simple Lie
algebras. Zap. Nauch. Sem. LOMI (in Russian) , 1987, v.164, 121-133 and J. Soviet
Math., 1989, v.47, 2450-2459.
[Kir5] A.N. Kirillov. Unimodality of generalized Gaussian coeﬃcients. C.R.Acad.Sci.Paris,
1992, t.315, Serie I, 497-501.
[Kir6] A.N. Kirillov. Fusion algebra and Verlide’s formula . Preprint, 1992, 9p.
Dilogarithm identities 93
[Kir7] A.N. Kirillov. Dilogarithm identities, partitions and spectra in conformal ﬁeld theory,
Part I. Submitted to Algebra and Analysis , 1992, 25p.
[Kir8] A.N. Kirillov. Generalization of the Gale-Ryser the orem. Preprint LITP-93-22 , 1993,
10p.
[Kir9] A.N. Kirillov. Decomposition of symmetric and exter ior powers of the adjoint repre-
sentation of gl(N ). 1.Unimodality of principal specialization of the intern al product of
the Schur functions. Int. J. Mod. Phys. , 1992, v.7, 545-579.
[Kir10] A.N. Kirillov. Quantum polylogarithms. Preprint, 1994.
[KK] A.N. Kirillov and S.V. Kerov. Combinatorial algorithm s related with Bete’s ansatz for
GL(n,C ). submitted to Algebra and Analysis , 1992.
[KL] A.N. Kirillov and N.A. Liskova. Completeness of Bethe’ s states for generalized XXZ
model. Preprint UTMS-94-47, Tokyo Univ. , 1994, 20p.
[KlMe] T. Klassen and E. Melzer. Purely elastic scattering t heories and their ultra-violet limit.
Nucl. Phys. , 1990, v.B338, 485-528.
[KR1] A.N. Kirillov and N.Yu. Reshetikhin. Exact solution o f the XXZ Heisenberg model
of spin S. J. Soviet Math. , 1986, v.35, 2627-2643.
[KR2] A.N. Kirillov and N.Yu. Reshetikhin. The Bethe ansatz and the combinatorics of
Young tableaux. J. Soviet Math. , 1988, v.41, p.925-955.
[Ku] A. Kuniba. Thermodynamics of the Uq(X (1)
r ) Bethe ansatz system with q a root of
unity. Nucl. Phys. , 1993, v.B389, 209-244.
[KN] A. Kuniba and T. Nakanishi. Spectra in Conformal Field T heories from the Rogers
dilogarithm. Modern Phys. Lett. , 1992, v.A7, 3487-3494.
[KNS] A. Kuniba, T. Nakanishi and J. Suzuki. Characters in Co nformal Field Theories from
thermodynamic Bethe ansatz. Modern Phys. Lett. , 1993, v.A7, 1649-1659.
[LS] A. Lascoux and M.-P. Sch¨ utzenberger. Sur une conjectu re de H.O. Foulkes. C. R.
Acad. Sci. Paris , 1978, v.286A, p.323–324.
[LP] J. Lepowsky and M. Primc. Structure of the standard modu les for the aﬃne Lie algebra
A(1)
1 . Contemporary Math., AMS, Providence , 1985, v.46.
[Lv] M. Levine. The indecomposable K3 of ﬁelds. Ann. Ec. Norm. Sup. , 1989, v.22,
255-344.
[Le1] L. Lewin. Dilogarithm and associated functions. North Holland, Amsterdam , 1981.
[Le2] L. Lewin. The dilogarithm in algebraic ﬁelds. J. Austral. Math. Soc. Series A , 1982,
v.33, 302-330.
[Le3] L. Lewin. The inner structure of the dilogarithm in alg ebraic ﬁelds. J. Number Theory,
1984, v.19, 345-373.
[Le4] L. Lewin. The order-independence of the polylogarith mic ladder structure–implications
for a new category of functional equations. Aequat. Math. , 1986, v.30, 1-20.
[Le5] L. Lewin (ed). Structural properties of polylogarith ms. Math. Surveys and Mono-
graphs, 1991, v.37.
[Li] S. Lichtenbaum. Groups related to scissors-congruenc e groups. Contemporary Math.,
1989, v.83, 151-157.
94 Anatol N. Kirillov
[Lin] X.-S. Lin. Knot invariants and iterated integrals. Prepr. IAS , 1994, 10p.
[Lit] D.E. Littlewood. The theory of group characters. Oxford University Press , 1950.
[Lo1] J.H. Loxton. Special values of the dilogarithm functi on. Acta Mathematica, 1984, v.43,
155-166.
[Lo2] J.H. Loxton. Partition identities and the dilogarith m, in [Le4], Chapter 13, pp.287-299.
[Lu1] G. Lusztig. Green polynomials and singularities of un ipotent classes. Adv. Math. ,
1981, v.42, p.169-178.
[Lu2] G. Lusztig. Singularities, character formulas, and a q-analog of weight multiplicities.
Ast´ erisque, 1983, v.101-102, p.208-227.
[Lu3] G. Lusztig. Modular representations and quantum grou ps. Contemporary Math., 1989,
v.82, 59-77.
[Ma] I.G. Macdonald. Symmetric Functions and Hall Polynomi als. Oxford University Press ,
1979.
[Me1] E. Melzer. The many faces of a character. Lett. Math. Phys. , 1994, v.31, 233-246.
[Me2] E. Melzer. Fermionic character sums and the corner tra nsfer matrix. Int. J. Mod.
Phys., 1994, v.A9, 1115-1136.
[Ml1] S. Milne. Classical partition functions and the U (n + 1) Rogers-Selberg identity. Dis-
crete Math. , 1992, v.99, 199-246.
[Ml2] S. Milne. The Cl Rogers-Selberg identity. SIAM J. Math. Anal. , 1994, v.25, 571-595.
[Ml3] S. Milne. The multidimensional 1ψ1 sum and Macdonald identities for A(1)
l . Proc
Sympos. Pure Math. , 1989, v.49 (part 2), 323-359.
[ML] S. Milne and G. Lilly. Consequences of the Al and Cl Bailey transform and Bailey
lemma. Preprint, 1992, 28p.
[Mi1] J. Milnor. Introduction to algebraic K-theory. Annals of Math. Studies , v.72, Prince-
ton Univ. Press, 1971.
[Mi2] J. Milnor. Hyperbolic geometry : the ﬁrst 150 years. Bull A.M.S. , 1982, v.6, 9-24.
[Mi3] J. Milnor. On polylogarithms, Hurwitz zeta-function , and the Kubert identities. En-
seign. Math. , 1983, v.29, 281-322.
[MM] K.C. Misra and T. Miwa. Crystal base for the basic repres entation of Uq(ˆsl(n)). Com-
mun. in Math. Phys. , 1990, v.134, 79-88.
[MS] A.S. Merkuriev and A.A. Suslin. On the K3 of a ﬁeld. Math. USSR Izv. , 1991, v.36,
541-565.
[Mo] D. Moak. The q-analogue of Stirling’s formula. Rocky Mtn. J. Math. , 1984, v.14,
403-413.
[NRT] W. Nahm, A. Recknagel and M. Terhoeven. Dilogarithm id entities in Conformal Field
Theory. Mod. Phys. Lett. , 1993, v.A8, 1835-1848.
[O] J. Oesterl´ e. Polylogarithmes. Seminaire BOURBAKI , 1992-93, n0762, 16p.
[P1] P. Paule. On identities of the Rogers-Ramanujan type. J. Math. Analysis and Appl. ,
1985, v.107, 255-284.
[P2] P. Paule. The concept of Bailey chains. Publ. I.R.M.A., Strasbourg , 1988, Actes 18 e
S´ eminaire Lotharingien, 53-76.
Dilogarithm identities 95
[Q1] Y.-H. Quano. Polynomial identities of the Rogers-Rama nujan type. Univ. Melbourne
Preprint, No. 25 , 1994, 25p.
[Q2] Y.-H. Quano. On equivalence between Bose/Fermi Viraso ro characters. Univ. Mel-
bourne Preprint, No. 27 , 1994, 9p.
[Ray] G. Ray. Multivariable polylogarithm identities, in [ Le5], Chapter 7, pp. 123-169.
[R] N.Yu. Reshetikhin. Quasitriangularity of quantum grou ps at root of unity. Preprint,
hep-th/9403105, 1994, 17p.
[RS] B. Richmond and G. Szekeres. Some formulas related to di logarithm, the zeta function
and the Andrews-Gordon identities. J. Austral. Math. Soc. , 1981, v.A31, 362-373.
[R-C] A. Rocha-Caridi. Vacuum vector representations of th e Virasoro algebra. in ”Vertex
Operator in Mathematical Physics” (eds. J. Lepowsky, S. Mandelstam and I.M. Singer),
Publications of MSRI, Springer-Verlag, 1984, v.3, 451-473 .
[Ro] L. Rogers. On function sum theorems connected with the s eries
∞∑
n=1
xn
n2 . Proc. London
Math. Soc. , 1907, v.4, 169-189.
[Ros] M. Rosso. Finite dimensional representations of the q uantum analog of the enveloping
algebra of a complex simple Lie algebra. Commun. Math. Phys. , 1988, v.117, 581-593.
[Sa] B. Sagan. The symmetric group. Wadsworth & Brooks/Cole, Paciﬁc Grove, CA , 1991.
[Se] A. Sergeev. Tensor algebra of the deﬁning representati on as the module over Lie su-
peralgebras gl(m,n ) and Q(n). Math. USSR, Sbornik , 1985, v.51, 419-424.
[Ser] V. Serganova. Kazhdan-Lusztig polynomials for the Li e superalgebras gl(m/n). Yale
Univ. Preprint , 1992, 8p.
[Sl] L.J. Slater. Further identities of the Rogers-Ramanuj an type. Proc. London Math.
Soc., 1951, v.54, 147-167.
[Stn1] R.P. Stanley. GL(n, C) for combinatorialists. in “Surveys in Combinatorics” (ed.
E.K.Lloyd), London Math. Soc., Lecture Note Series, No.82, Cambridge University
Press, Cambridge , 1983, 187-199.
[Stn2] R.P. Stanley. The stable behavior of some characters of SL(n, C). Linear and Multil.
Algebra, 1984, v.16, 3-27.
[Stm] J.R. Stembridge. Hall-Littlewood polynomials, plan e partitions and the Rogers-Rama-
nujan identities. Trans Amer. Math. Soc. , 1990, v.319, 469-498.
[Su] A.A. Suslin. K3 of a ﬁeld and the Bloch group. Proc. of the Steklov Inst. of Math. ,
1991, v.4, 217-239.
[Te] I. Terada. A generalization of the length symmetry and v ariety of N -stable ﬂags.
Preprint, 1993, 26p.
[Tr1] M. Terhoeven. Lift of dilogarithm to partition identi ties. Preprint Bonn-HE-92-36 ,
1992 and hep-th/9211120.
[Tr2] M. Terhoeven. Dilogarithm identities, fusion rules a nd structure constants of CFTs.
Preprint Bonn-HE-93-24 , 1993, 11p.
[TV] V. Tarasov and A. Varchenko. Asymptotic solutions to th e quantized Knizhnik-Zamo-
lodchikov equation and Bethe vectors. Prepr. UTMS-94-46, Tokyo Univ. , 1994.
96 Anatol N. Kirillov
[UN] K. Ueno and M. Nishizawa. Quantum groups and zeta-funct ions. Preprint, 1994, 12p.
[V] A. Varchenko. Multidimensional hypergeometric functi ons in conformal ﬁeld theory,
algebraic K-theory, algebraic geometry. ICM, Kyoto , 1990, v.1, 281-300.
[W1] G.N. Watson. A new proof of the Rogers-Ramanujan identi ties. J. London Math. Soc. ,
1929, v.4, 4-9.
[W2] G.N. Watson. A note on Spence’s logarithmic transcende nt. Quart. J. Math. Oxford ,
1937, Ser. 8, 39-42.
[Za1] D. Zagier. Hyperbolic manifolds and special values of Dedekind zeta-functions. Invent.
Math., 1986, v.83, 285-301.
[Za2] D. Zagier. The remarkable dilogarithm. J. Math. Phys. Sci. , 1988, v.22, 131-145.
[Za3] D. Zagier. The remarkable dilogarithm (number theory and related topics). Papers
presented at the Ramanujan colloquium, Bombay , 1988, TIFR.
[Za4] D. Zagier. Polylogarithms, Dedekind zeta-functions and the algebraic K-theory of
ﬁelds. in Arithmetic Algebraic Geometry, Birkhauser , G. van der Geer e.a. (eds), 1991,
v.89, 391-430.
[Zm] Al. Zamolodchikov. Thermodynamic Bethe ansatz in rela tivistic models: scaling 3-
state Potts and Lee-Yang models. Nucl. Phys. , 1990, v.B342, 695-720.
[ZB] D. Zeilberger and D. Bressoud. A proof of Andrew’s q-Dyson conjecture. Discrete
Math., 1985, v.54, 201-224.
