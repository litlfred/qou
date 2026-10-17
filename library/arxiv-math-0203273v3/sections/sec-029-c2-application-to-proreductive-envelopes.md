---
doc_id: arxiv-math-0203273v3
doc_title: "arXiv:math/0203273v3 [math.CT] 12 Oct 2002"
section_id: sec-029-c2-application-to-proreductive-envelopes
section_title: "Application to proreductive envelopes"
section_number: C.2
pages: 138-146
source_pdf: 0203273v3.pdf
source_sha256: 824715d110e34305
toc_source: inferred
---
velopes it will be convenient to use the following terminology. Let f : H →K be
a k-homomorphism from an afﬁne k-group to a proreductive k-group. Call f uni-
versal if each k-homomorphism H →K′ to a proreductive K′ factors, uniquely
up to conjugation by a k-point of K′, through f. Equivalently, f is universal if its
conjugacy class is the embedding of H into its proreductive envelope. Th´eor`eme
19.3.1 states that for each H there exists a universal f. Call f minimal if f factors
through no proper proreductive subgroup of K. If L is proreductive, h : H →L is
universal, and f = lh, then f is universal if and only if l is an isomorphism and f
is minimal if and only if l is faithfully ﬂat.
By considering k-homomorphisms to general linear groups it can be seen that
if f is universal then f ∗induces a bijection on isomorphism classes of objects
(Proposition 19.3.4). We note also the following fact, which generalises a result
due to Kostant [33, Theorem 3.6]. If f is universal, then any k-homomorphism
h : H →K′ to a proreductive K′ factors through f uniquely up to conjugation by
a unique k-point of the prounipotent radical RuCK′(h) of the centraliser CK′(h) of
h. Equivalently, if h = lf then CK′(l) is a Levi subgroup of CK′(h), i.e. CK′(h)
is the semidirect product of RuCK′(h) and CK′(l). To verify this, let L be a Levi
subgroup of CK′(h). Then h factors through the proreductive subgroup CK′(L) of
K′, so by universality of f the conjugate of l by some k-point z of CK′(h) factors
through CK′(L). Thus L ⊂zCK′(l)z−1 ⊂CK′(h) and zCK′(l)z−1 = L since
CK′(l) is proreductive.
The main facts required about universal and minimal k-homomorphisms are con-
tained in the following lemma.
NILPOTENCE, RADICAUX ET STRUCTURES MONO¨IDALES
139
Lemma C.7. Let f : H →K be a k-homomorphism from an afﬁne k-group to a
proreductive k-group. Then
(i) f is universal if and only if f is minimal and each representation of H is a
direct summand of f ∗V for some representation V of K.
(ii) If f is minimal then fk′ : Hk′ →Kk′ is minimal for any extension k′ of k.
(iii) If f is universal then fk′ : Hk′ →Kk′ is universal for any algebraic exten-
sion k′ of k.
Proof. Factor f as H
g→L
l→K with L proreductive and g universal. Then g∗
induces a bijection on isomorphism classes of objects, and f is universal (resp.
minimal) if and only if l is an isomorphism (resp. faithfully ﬂat).
Thus f is universal ⇐⇒f is minimal and l is a closed immersion. Further l is a
closed immersion ⇐⇒each representation of L is a direct summand of some l∗V
(because L is proreductive) ⇐⇒each representation of H is a direct summand of
some f ∗V . This gives (i).
If W is representation of a k-group G, write mG(W) for the multiplicity of
the trivial G-representation k in a decomposition of W into G-indecomposables.
Clearly mG(W) is the rank of the canonical k-homomorphism W G →WG, so it
is preserved by extension of the scalars. Then l is surjective ⇐⇒l∗is fully faith-
ful (because L is proreductive) ⇐⇒dimk HomK(k, V ) = dimk HomL(k, l∗V )
for each representation V of K ⇐⇒mK(V ) = mL(l∗V ) for each V ⇐⇒
mK(V ) = mH(f ∗V ) for each V ⇐⇒each V is a direct summand of some V1 for
which mK(V1) = mH(f ∗V1) (because mK(V ) ≤mH(f ∗V )). By Lemma C.6(i),
if the last condition is satisﬁed it is also satisﬁed with f, H and K replaced by fk′,
Hk′ and Kk′. This gives (ii).
For (iii) it is enough by (i) and (ii) to show if each representation of H is a direct
summand of some f ∗V then each representation of Hk′ is a direct summand of
some f ∗
k′V ′. This is clear from Lemma C.6(ii).
□
Theorem C.3. Let H be an afﬁne k-group and let k′ be an extension of k. Then the
canonical morphism p Red(Hk′) →p Red(H)k′ is an isomorphism if and only if
either k′ is algebraic over k or the prounipotent radical of H is of dimension ≤1.
Proof. Let f : H →K, with K proreductive, be universal. Then p Red(Hk′) →
p Red(H)k′ is an isomorphism ⇐⇒fk′ is universal ⇐⇒each representation of Hk′
is a direct summand of some f ∗
k′W ′ (Lemma C.7) ⇐⇒each representation of Hk′ is
a direct summand of some f ∗W ⊗k k′ (Lemma C.6(i)) ⇐⇒each representation of
Hk′ is a direct summand of some V ⊗kk′. The result thus follows from Theorem C.2.
□
Theorem C.4. Let U be a unipotent k-group of dimension 1, equipped with an
action of the proreductive k-group M. Then
(i) There exists an M-embedding U →SL(2) for some action of M on SL(2).
(ii) If f : U →SL(2) is an M-embedding and h : U →K is an M-homomorphism
with K proreductive, then there is an M-homomorphism l : SL(2) →K, unique
up to conjugation by a k-point of K ﬁxed by M, such that h = lf.
140
YVES ANDR´E ET BRUNO KAHN
(iii) If f : U →SL(2) is an M-embedding then (the conjugacy class of) f ⋊M :
U ⋊M →SL(2) ⋊M is the embedding of U ⋊M into its proreductive envelope.
Proof. By Lemma C.5 there is a k-homomorphism g : U ⋊M →GL(2) non-trivial
on U. The restriction of g to U factors through an M-embedding f : U →SL(2),
where M acts on SL(2) through g and the inner action of GL(2). This gives (i).
It will sufﬁce to prove (ii) and (iii) for the f just constructed. Consider ﬁrst (iii).
Let L be a proreductive subgroup of SL(2)⋊M through which f ⋊M factors. Then
L∩SL(2) ⊃U is reductive since SL(2) is normal in SL(2)⋊M, so L∩SL(2) = L
and L ⊃SL(2). Also L ⊃M, so L = SL(2) ⋊M. Thus f ⋊M is minimal. The
projection U ⋊M →M factors through f ⋊M : U ⋊M →SL(2) ⋊M, and g
factors through f ⋊M by construction. Thus (f ⋊M)∗is essentially surjective by
Lemma C.5, and so universal by Lemma C.7(i).
Given h as in (ii), h⋊M is by universality of f ⋊M the composite of f ⋊M with
a k-homomorphism SL(2)⋊M →K ⋊M, necessarily of the form l⋊M for some
M-homomorphism l. Thus h = lf. If also h = l′f for an M-homomorphism l′, then
l and l′ are by universality of f conjugate by a unique k-point α of the prounipotent
radical of the centraliser of h. This implies that lk′ and l′
k′ are conjugate by mα for
any extension k′ of k and m ∈M(k′). Since M stabilises the centraliser of h and
so the prounipotent radical of this centraliser, M ﬁxes α by uniqueness.
□
An afﬁne k-group G will be called ﬁnite dimensional if its quotients of ﬁnite type
are of bounded dimension. It is equivalent to require that the connected component
of G be an extension of a group of ﬁnite type by a pro´etale group.
Lemma C.8. If k is algebraically closed then a connected ﬁnite dimensional reduc-
tive k-group has only a ﬁnite number of non-isomorphic irreducible representations
of given dimension and determinant.
Proof. The connected semisimple case follows from Weyl’s dimension formula. In
general, a connected ﬁnite dimensional reductive group is a quotient of T × G for
some protorus T and connected semisimple G. An irreducible representation of
T × G of dimension n and determinant χ is the tensor product of an n-dimensional
irreducible representation of G with a 1-dimensional representation of T deﬁned by
a character ψ with ψn = χ. Since there is at most one such ψ, the result follows
from the connected semisimple case.
□
Theorem C.5. The proreductive envelope of an afﬁne k-group H is of ﬁnite type
over k (resp. ﬁnite dimensional) if and only if H is of ﬁnite type over k (resp. ﬁnite
dimensional) and the prounipotent radical of H is of dimension ≤1.
Proof. The “if” is clear by Theorem C.4(iii). Let f : H →K, with K proreductive,
be universal. For the “only if”, it sufﬁces to show that if the prounipotent radical of
H has dimension > 1 then K is not ﬁnite dimensional. By Lemma C.7(iii) we may
suppose that k is algebraically closed. If ¯H is a quotient of H and ¯H →¯K, with ¯K
proreductive, is universal, then H →¯H →¯K is minimal, and so factors through
a faithfully ﬂat K →¯K. Replacing H by an appropriate ¯H, we may thus further
suppose H to be of ﬁnite type (see also Proposition 19.4.7 c)). Let j : H0 →H
NILPOTENCE, RADICAUX ET STRUCTURES MONO¨IDALES
141
be the embedding of the connected component of H and g : H0 →L, with L
proreductive, be universal, so that fj = lg for some l : L →K. Then l is a
closed immersion. Indeed otherwise some representation of L would not be a direct
summand of any l∗V , whence the same would hold with L and l replaced by H0
and j, since f ∗and g∗induce bijections on isomorphism classes of objects. But each
representation W of H0 is a direct summand of j∗IndH
H0 W. Replacing H by H0
we may thus suppose H connected (see also Proposition 19.4.7 a)). Then K also is
connected, as is seen by considering k-homomorphisms to ﬁnite groups.
By Theorem C.1 there is a family V of representations of H, parametrised by
A1, such that the set of H-isomorphism classes of the ﬁbres Vx for x ∈A1(k) is
inﬁnite. There thus exists an inﬁnite set S of pairwise non-isomorphic irreducible
representations V of H such that each V ∈S is a direct summand of some Vx for
x ∈A1(k). Let T be the radical of a a Levi subgroup of H. The restrictions to
T of the Vx are isomorphic, so among direct summands of the Vx there are only a
ﬁnite number of possible T-isomorphism classes. Since the determinant of a rep-
resentation of H is deﬁned uniquely by its restriction to T, it follows that there is
an inﬁnite subset S′ of S such that each V ∈S′ has the same determinant χ. Then
χ = ψ ◦f for a unique character ψ of K. Each V ∈S′ is isomorphic to f ∗W for
some representation W of K, and each such W has determinant ψ and dimension at
most that of the ﬁbres of V. Lemma C.8 then shows that K is not ﬁnite dimensional.
□
By a similar argument it can be shown for example that if k is uncountable the
proreductive envelope of an afﬁne k-group with prounipotent radical of dimension
> 1 is not a countable limit of k-groups of ﬁnite type.
142
YVES ANDR´E ET BRUNO KAHN
R´EF´ERENCES
[1] Y. Andr´e, B. Kahn, Construction inconditionnelle de groupes de Galois motiviques, C.R. Acad.
Sci. Paris, S´er I. 331 (2002), 989–994.
[2] A. Beilinson, Height pairing between algebraic cycles, in : K-theory, Arithmetic and Geometry,
Lect.notes in Math. 1289, Springer (1987), 27–41.
[3] D. Benson, Representations and cohomology I, Cambridge studies 30, Cambridge Univ.
Press,1995.
[4] F. Beukers, D. Brownawell, G. Heckman, Siegel normality, Annals of Math. 127 (1988), 279–
308.
[5] N. Bourbaki, Alg`ebre, chapitre VIII, Hermann, 1958.
[6] N. Bourbaki, Groupes et alg`ebres de Lie, chapitre VI, Hermann/CCLS, 1975.
[7] N. Bourbaki, Groupes et alg`ebres de Lie, chapitre VIII, Hermann/CCLS, 1975.
[8] L. Breen, Tannakian categories, in Motives, Proc. Symposia pure Math. 55 (I), AMS, 1994, 337–
376.
[9] A. Brugui`eres, Th´eorie tannakienne non commutative, Comm. in Algebra, 22(14) (1994), 5817–
5860.
[10] A. Brugui`eres, Tresses et structure enti`ere sur la cat´egorie des repr´esentations de SLN quantique,
Comm. in Algebra 28 (2000), 1989–2028.
[11] H. Cartan, S. Eilenberg, Homological algebra, Princeton Univ. Press, 1956.
[12] P. Cartier, Construction combinatoire des invariants de Vassiliev-Kontsevich des nœuds, C. R.
Acad. Sci. Paris 316 (1993), 1205–1210.
[13] J. Cuntz, D. Quillen, Algebra extensions and nonsingularity, Journal A.M.S. 8 2 (1995), 251–
289.
[14] P. Deligne, Cat´egories tannakiennes, in : The Grothendieck Festschrift, vol. 2, Birkh¨auser P.M.
87 (1990), 111–198.
[15] P. Deligne et al., Quantum ﬁelds and strings : a Course for Mathematicians, AMS, 1999.
[16] P. Gabriel, Des cat´egories ab´eliennes, Bull. Soc. Math. France 90 (1962), 323–448.
[17] P. Gabriel, Probl`emes actuels de th´eorie des repr´esentations, L’Ens. Math. 20 (1974), 323–332.
[18] J. Giraud, Cohomologie non ab´elienne, Springer, 1971.
[19] A. Grothendieck, Sur quelques points d’alg`ebre homologique, Tohoku Math. J. (2), 9 (1957),
119–221.
[20] V. Ginzburg, Principal nilpotent pairs in a semisimple Lie algebra. I, Invent. Math. 140 (2000),
511–561.
[21] V. Guletskii, C. Pedrini, The Chow motive of the Godeaux surface, pr´epublication (2001).
[22] D. Happel, Triangulated categories in the representation theory of ﬁnite dimensional algebras,
London Math. Soc. Lect. notes 119 (1988), Cambridge Univ. Press.
[23] G. Higman, On a conjecture of Nagata, Proc. Camb. Philos. Soc. 52 (1956), 1–4.
[24] N. Jacobson, Ann. of Math. 36 (1935), 875–881.
[25] U. Jannsen, Motives, numerical equivalence and semi-simplicity, Invent. Math. 107 (1992),
447–452.
[26] U. Jannsen, Equivalence relations on algebraic cycles, in The arithmetic and geometry of alge-
braic cycles (Banff, AB, 1998), 225–260, NATO Sci. Ser. C Math. Phys. Sci., 548, Kluwer Acad.
Publ., Dordrecht, 2000.
[27] A. Joyal, R. Street, Braided monoidal categories, Adv. in Math. 102 (1993), 20–78.
[28] C. Kassel, M. Rosso, V. Turaev, Quantum groups and knot invariants, S.M.F. Panoramas et
synth`eses 5 (1997).
NILPOTENCE, RADICAUX ET STRUCTURES MONO¨IDALES
143
[29] N. Katz, W. Messing, Some consequences of the Riemann hypothesis for varieties over ﬁnite
ﬁelds, Invent. Math. 23 (1974), 73–77.
[30] G. M. Kelly, On the radical of a category, J. Australian Math. Soc. 4 (1964), 299–307.
[31] O. Kerner, A. Skowro´nski, On module categories with nilpotent inﬁnite radical, Compos. Math.
77 3 (1991), 313–333.
[32] S.I. Kimura, Chow motives can be ﬁnite-dimensional, in some sense, `a paraˆıtre au J. of Alg.
Geom.
[33] B. Kostant, The principal three-dimensional subgroup and the Betti numbers of a complex sim-
ple Lie group, Amer. J. Math. 81 (1959), 973–1032.
[34] K. K¨unneman, On the Chow motive of an abelian scheme, in : Motives, Proc. Symposia pure
Math. 55 (I), AMS, 1994, 189–205.
[35] P.Y. Leduc, cat´egories semi-simples et cat´egories primitives, Canad. J. Math. 20 (1968), 612–
628.
[36] S. Mac Lane, Categories for the working mathematician, 2`eme ´ed., Springer GTM 5 (1998).
[37] G. A. Margulis, Discrete subgroups of semisimple Lie groups, Springer, Berlin, 1991.
[38] B. Mitchell, Rings with several objects, Adv. Math. 8 (1972), 1–161.
[39] V.V. Morozov, Sur un ´el´ement nilpotent dans une alg`ebre de Lie semi-simple (en russe), Dokl.
Akad. Nauk SSSR 36 (1942), 83–86.
[40] V.V. Morozov, Sur le centralisateur d’une sous-alg`ebre semi-simple d’une alg`ebre de Lie semi-
simple (en russe), Dokl. Akad. Nauk SSSR 36 (1942), 259–261.
[41] J.P. Murre, On a conjectural ﬁltration on the Chow groups of an algebraic variety, parts I and II,
Indag. Math. 4 (1993), 177–201.
[42] M. Nagata, On the nilpotency of nil-algebras, J. Math. Soc. Japan 4 (1952), 296–301.
[43] M. Nathanson, Classiﬁcation problems in K-categories, Fund. Math. 105 3 (1979/80), 187–197.
[44] P. O’Sullivan, lettres aux auteurs, 29 avril et 12 mai 2002.
[45] D. I. Panyushev, Nilpotent pairs in semisimple Lie algebras and their characteristics, Internat.
Math. Res. Notices 2000 1–21.
[46] A. Piard, Indecomposable representations of a semi-direct product sl(2) ⋉A and semi-simple
groups containing sl(2) ⋉A, in : Sympos. Math. XXXI (Roma, 1988), 185–195, Acad. Press,
1990.
[47] Platon, Ph´edon, § LIII.
[48] N. Popescu, Abelian categories with applications to rings and modules, Acad. Press, 1973.
[49] M. Prest, Model theory and modules, L.M.S. Lecture note series 130, Cambridge Univ. Press
1988.
[50] C. M. Ringel, Recent advances in the representation theory of ﬁnite dimensional algebras, in
Representation theory of ﬁnite groups and ﬁnite-dimensional algebras, Birkh¨auser Progress in
Math. 95 (1991).
[51] L. Rowen, Ring theory, vol. 1, Acad. Press, 1988.
[52] W. Rump, Doubling a path algebra, or : how to extend indecomposable modules to simple
modules, in : Representation theory of groups, algebras and orders (Costant¸a, 1995), An. S¸tiint¸.
Univ. Ovidius Constant¸a Ser Mat. 4 2 (1996), 174–185.
[53] N. Saavedra Rivano, cat´egories tannakiennes, Lect. Notes in Math. 265, Springer, 1972.
[54] J.-P. Serre, G`ebres, L’Ens. Math. 39 (1993), 33–85.
[55] J.-P. Serre, Propri´et´es conjecturales des groupes de Galois motiviques et des repr´esentations
l-adiques, in Motives, Proc. Symposia pure Math. 55 (I), AMS, 1994, 377–400.
144
YVES ANDR´E ET BRUNO KAHN
[56] D. Simson, A. Skowro´nski, The Jacobson radical power series of module categories and the
representation type, Bol. Soc. Mat. Mexicana 5 2 (1999), 223–236.
[57] R. Street, Ideals, radicals and structure of additive categories, Appl. Cat. Structures 3 (1995),
139–149.
[58] R. Thomason, The classiﬁcation of triangulated categories, Compos. Math. 105 (1997), 1–27.
[59] V. Voevodsky, A nilpotence theorem for cycles algebraically equivalent to zero, International
Mathematics Research Notices 4 (1995), 1–12.
[60] P. Vogel, Invariants de Witten-Reshetikin-Turaev et th´eories quantiques des champs, in : Panora-
mas et synth`eses 7 (1999), 117-143.
NILPOTENCE, RADICAUX ET STRUCTURES MONO¨IDALES
145
INDEX TERMINOLOGIQUE
A-id´eal `a gauche . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.3.4, 1.3.10, 6.2.1
A-module (`a gauche) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1.3.3, 1.3.10, 2.1.1, 11.1, appendice A
A-bimodule . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .11.1
anneau de repr´esentations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .10.2.1, 20.2
artinien . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .2.1.2, 2.3.2, 2.3.4, A.2.1, A.2.3
auto-dual . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.4.4, 2.1.2, 2.2.6, 2.3.2, 19.5.2
Auslander (alg`ebre d’) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17.2
biproduit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1.1
compact . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.3.5, 5.1.3, 5.2.2, 5.2.5, 5.3.1, 5.3.2, 14.1.3
compl´ement unipotent . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19.3.2
conservatif . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.4.4, 1.4.7, 1.4.8, 2.3.4, 5.2, 7.1.6, 19.4.6, A.2.14
coproduit (de cat´egories) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . A.2.2
cor´etraction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.4.4, 1.4.9, 7.1.3
dimension (rigide) . . . . . . . . . . . . . 7.1, 7.2.4, 7.2.7, 7.3.1, 7.3.2, 8.1.2, 8.1.3, 8.2.4, 8.3, 9.1.7, 9.2.1
dimension ﬁnie au sens de Kimura . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9.1.1
dimension de Kimura (ou kimension) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9.1.13
dual . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .5.2.1, 6.1, 10.2.1, 13.8.3, 14.1.3, 17.1.2
enveloppe pro-semi-simple . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17.1
enveloppe r´eductive . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20.1.2
enveloppe pro-r´eductive . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19.3.2
´epaisse . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1.2
faiblement (exact, ´epi) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .19.2.1, 19.4.4, 19.4.5
gerbe . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14.2.1, 18.2.5,
groupe `a conjugaison pr`es . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19.1, 19.3.2
h´er´editaire . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17.3
Hochschild (homologie) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10.2, 11.2.1
Hochschild (cohomologie) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11.2
id´eal (bilat`ere) d’une cat´egorie additive . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.3
indice . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.2.7
K-cat´egorie, K-foncteur, K-lin´eaire . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1
Kimura (cat´egorie de) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .9.1.16
mono¨ıdal (id´eal) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1.1
mono¨ıdal (foncteur) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .13.1
Morita (´equivalence de) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1.3.9
pr´esentation ﬁnie . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1.3.7
produit local (de cat´egories) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . A.2.2
proﬁnie (alg`ebre) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17.1
pseudo-ab´elien . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1
puissance ext´erieure, sym´etrique . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .7.2.3
radical . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.4.1
⊗-radical . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .7.4.1
radical inﬁni . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1.1
radiciel (mon mari) . . . . . . . . . . . . . . . . . . . . . . 1.4.6, 2.1.5, 2.3.4, 3.1.2, 4.1.4, 12.2.1, 13.7.1, 15.4.1
146
YVES ANDR´E ET BRUNO KAHN
r´etraction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.4.4, 1.4.9
rigide . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1, 7.1.4, 8.2, 8.1.2, 8.1.1, 7.1.7, 8.2.2, 8.3.1, 10.1, 18.1.1
semi-primaire . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .2.3.1
semi-simple . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.1.1, A.2.1
s´eparable (cat´egorie) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.2.6
simple (objet, cat´egorie) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .A.2.1
sorite . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13.3
stricte (cat´egorie mono¨ıdale, foncteur mono¨ıdal) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13.4
strictement (semi-primaire, de Wedderburn, K-lin´eaire)
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1.3
structure balanc´ee . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15.3.4, 15.3.6
trace. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .7.1, 7.2,
7.2.1, 7.2.6, 7.3.1, 7.3.3, 8.2, 10.1,10.2
tressage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1, 7.1, 7.1.4, 15.1, 15.2, 15.3.3, 15.3.5, 15.3.6
tressage inﬁnit´esimal . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15.3.6, 15.4.2
type de repr´esentation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1.1, 3.2, 3.2.1, 17.2, 17.3, 19.7
Wedderburn (cat´egorie de) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.4.1
D´EPARTEMENT DE MATH´EMATIQUES ET APPLICATIONS, ´ECOLE NORMALE SUP´ERIEURE,, 45
RUE D’ULM, 75230 PARIS CEDEX 05, FRANCE.
E-mail address: andre@dmi.ens.fr
INSTITUT
DE
MATH´EMATIQUES
DE
JUSSIEU,
175–179
RUE
DU
CHEVALERET,
75013 PARIS, FRANCE.
E-mail address: kahn@math.jussieu.fr
39 EDGECLIFFE AVE, COOGEE, NSW 2034, AUSTRALIA
E-mail address: pjosullivan@optusnet.com.au
