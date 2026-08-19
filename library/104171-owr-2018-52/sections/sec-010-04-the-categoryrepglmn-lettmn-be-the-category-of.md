---
doc_id: 104171-owr-2018-52
doc_title: "Mathematisches Forschungsinstitut Oberwolfach Report No. 52/2018"
section_id: sec-010-04-the-categoryrepglmn-lettmn-be-the-category-of
section_title: "The categoryRep(GL(m|n)). LetTm|n be the category of ﬁnite dimensional"
section_number: 0.4
pages: 30-36
source_pdf: 10.4171-owr-2018-52.pdf
source_sha256: b33ed36eaa470877
doc_brief: "Mathematisches Forschungsinstitut Oberwolfach Report No. 52/2018 — The workshop brought together experts investigating algeb raic Lie theory from the geometric and categorical viewpoints."
---
representations of GL(m|n). The categories Tm|n are not semisimple for m,n≥ 1.
As above we consider only objects that are retracts of iterated t ensor products of
irreducible representations L(λ). This subcategory is called TI
m|n and we denote
the pro-reductive group of its semisimple quotient by Hm|n. The crucial tool
to determine Hm|n is the Duﬂo-Serganova functor [DS05] [HW14] DS :Tm|n→
Tm−1|n−1. It allows us to reduce the determination of Hm|n to lower rank.
Theorem. [HW18, Theorem 5.15] a) Hm|n is a pro-reductive group. b) DS
restricts to a tensor functor DS :TI
m|n→T I
m−1|n−1 and gives rise to a functor
DS :TI
m|n/N→T I
m−1|n−1/N . c) There is an embedding Hm−1|n−1→Hm|n and
DS can be identiﬁed with the restriction functor.
Enveloping Algebras and Geometric Representation Theory 3111
We specialize now to GL(n|n) and use the notation Gn = (Hn|n)0
der and Gλ =
(Hλ)0
der. We also suppose that sdim(L(λ)) > 0 since we can replace L(λ) by its
parity shift. We say a representation is weakly selfdual (SD) if it is se lfdual after
restriction to SL(n|n).
Theorem. [HW18, Theorem 6.2] Gλ = SL(Vλ) if L(λ) is not (SD). If L(λ) is
(SD) and Vλ|Gλ′ is irreducible, Gλ =SO(Vλ) respectively Gλ =Sp(Vλ) according
to whether L(λ) is orthogonal or symplectic selfdual. If L(λ) is (SD) and Vλ|Gλ′
decomposes into at least two irreducibe representations, then Gλ∼
= SL(W ) for
Vλ|Gλ′
∼
=W⊕W ∨.
We conjecture that the last case in the theorem doesn’t happen. T he ambiguity
in the determination of Gλ is only due to the fact that we cannot exclude special
elements with 2-torsion in π0(Hn|n).
Theorem. [HW18, Theorem 6.8] Let λ∼µ ifL(λ)∼
=L(µ) or L(λ)∼
=L(µ)∨ after
restriction to SL(n|n). Then
Gn∼
=
∏
λ∈X +/∼
Gλ.
In down to earth terms, these theorems give
• the decomposition law of tensor products of indecomposable module s in
TI
m|n up to indecomposable summands of superdimension 0; and
• a classiﬁcation (in terms of the highest weights of Hλ and Hµ) of the in-
decomposable modules of non-vanishing superdimension in iterated t ensor
products of L(λ) and L(µ).
We remark that the statement about Gn|n implies a strange disjointness prop-
erty of iterated tensor products of irreducible representations of non vanishing
superdimension. For the general Tm|n-case ((where m≥n) recall that every max-
imal atypical block in Tm|n is equivalent to the principal block of Tn|n. We denote
the image of an irreducible representation L(λ) under this equivalence by L(λ0).
Conjecture. (work in progress) Suppose that sdim( L(λ)) > 0. Then Hλ ∼
=
GL(m−n)×Hλ0 and L(λ) corresponds to the representation LΓ⊗Vλ0 of Hλ.
HereLΓ is an irreducible representation of GL(m−n) which only depends on the
block Γ (the core of Γ).
References
[AP95] Henning Haahr Andersen and Jan Paradowski, Fusion categories arising from semisim-
ple Lie algebras. , Commun. Math. Phys., 169, 1995.
[AK02] Yves Andr´ e and Bruno Kahn, Nilpotence, radicaux et structures mono ¨ ıdales. Rend.
Semin. Mat. Univ. Padova, 108, 2002.
[Del02] Deligne, P., Cat´ egories tensorielles. (Tensor categories)., Mosc. Math. J. , 2, 2, 2002.
[Del90] Deligne, P., Cat´ egories tannakiennes. (Tannaka categories). , The Grothendieck
Festschrift, Collect. Artic. in Honor of the 60th Birthday o f A. Grothendieck. Vol. II,
Prog. Math. 87, 111-195 (1990)..
[DS05] Duﬂo, M. and Serganova. V., On associated variety for Lie superalgebras. ,
arXiv:math/0507198v1, 2005.
3112 Oberwolfach Report 52/2018
[EO18] Etingof, P. and Ostrik, V., On semisimpliﬁcation of t ensor categories, ArXiv e-prints,
1801.04409, 2018.
[He15] Heidersdorf, T., On supergroups and their semisimpl iﬁed representation categories, to
appear in: Algebr. Represent. Theory ArXiv e-prints, 1512. 03420, (2015).
[HW14] Heidersdorf, T. and W eissauer, R., Cohomological tensor functors on representations
of the General Linear Supergroup to appear in Mem. Am. Math. Soc., ArXiv e-prints,
1406.0321, 2014.
[HW18] Heidersdorf, T. and W eissauer, R., On classical tens or categories attached to the ir-
reducible representations of the General Linear Supergrou ps GL(n|n), ArXiv e-prints,
1805.00384, (2018).
Braidings, cacti and crystals
Jacob Greenstein
(joint work with Arkady Berenstein and Jian-Rong Li)
Let g be a reductive Lie algebra and let Uq(g) be the corresponding quantized
universal enveloping algebra (in fact our results can be formulated in a more
general framework of symmetrizable Kac-Moody algebras with ext ended weight
lattices). Consider the category Oint
q (g) whose objects are direct sums (possibly
inﬁnite) of simple ﬁnite dimensional Uq(g)-modules. Let W be the Weyl group
of g. After Lusztig ([Lus]), the braid group Br W corresponding to W acts on
the category Oint
q (g). This means that for every object V inOint
q (g) we have
a group homomorphism Br W → GL(V ), and these homomorphisms are natural
with respect to morphisms in Oint
q (g).
On the other hand, let Cact W be the cactus group associated with W (cf [Los,
B, DJS]). For W =Sn the corresponding group appeared in the study of Deligne-
Mumford compactiﬁcation of the moduli space of stable rational cu rves with n + 1
marked points and their applications in mathematical physics, as well as in the
context of coboundary categories introduced by Drinfeld [D]. One e xample of
such categories is provided by crystals, and the corresponding ac tion of Cact Sn ,
was studied in [HK, S].
In this talk we discuss an action of Cact W on the category Oint
q (g) ([BGL1])
which is connected to Lusztig’s symmetries. Our action on modules pr eserves their
lower and upper crystal lattices of Kashiwara and factors throug h to an action on
the corresponding crystal bases. We also study the action of the “largest cactus”
(the standard generator of Cact W which is mapped to the longest element of W
under the natural surjection Cact W → W ) on Gelfand-Kirillov model for the
categoryOint
q (g). We prove that it is an algebra anti-involution, and show that it
preserves the upper global crystal basis and hence the upper glo bal crystal basis
in each simple highest weight module. In fact, these involutions are clo sely related
to remarkable quantum twists studied by Kimura and Oya ([KO]).
Our motivation stems from the study of monomial braidings ([BGL2]). Namely,
starting from a vector space V and a braiding on V ⊗V , we obtain families of
braidings on V ⊗n⊗V ⊗n parametrized by bi-transitive (also known as bipartite)
relations on {1,...,n }. This can be further generalized and yields the notion, as
Enveloping Algebras and Geometric Representation Theory 3113
well as inﬁnite families of examples, of multibraidings. The ﬁrst example was con-
structed in [BG] in connection with quantum folding. Using the results of [BGL1]
and quantum Howe duality ([TL]) we connect the study of spectral p roperties
of such (multi)braidings to the purely combinatorial question of det ermining the
multiplicities of±1 eigenvalues of certain involutions in the cactus group on tensor
products of highest weight modules.
References
[BG] A. Berenstein and J. Greenstein, Quantum folding , Int. Math. Res. Not. 2011 (2011),
no. 21, 4821–4883
[BGL1] A. Berenstein, J. Greenstein, J.-R. Li, On cacti and crystals , preprint arXiv:1803.11330
(to appear)
[BGL2] A. Berenstein, J. Greenstein, J.-R. Li, Monomial braidings (in preparation)
[B] C. Bonnaf´ e, Cells and cacti , Int. Math. Res. Not. 2016 (2016) no. 19, 5775–5800
[D] V. G. Drinfel’d, Quasi-Hopf algebras , Algebra i Analiz 1 (1989), no. 6, 114–148
[HK] A. Henriques and J. Kamnitzer, Crystals and coboundary categories, Duke Math. J.
132 (2006), no. 2, 191–216
[KO] Y. Kimura and H. Oya, Twist automorphisms on quantum unipotent cells and dual
canonical bases, preprint arXiv:1701.02268.
[Los] I. Losev, Cacti and cells , preprint, arXiv:1506.04400
[Lus] G. Lusztig, Introduction to quantum groups, Progress in Mathematics, vol. 110,
Birkh¨ auser Boston, Inc., Boston, MA, 1993.
[DJS] M. Davis, T. Januszkiewicz, and R. Scott, R., Fundamental groups of blow-ups , Adv.
Math., 177 (2003), no. 1, 115–179
[S] A. Savage, Crystals, quiver varieties, and coboundary c ategories for Kac-Moody alge-
bras, Adv. Math. 221 (2009), no. 1, 22–53
[TL] V. Toledano Laredo, A Kohno-Drinfeld theorem for quantum Weyl groups , Duke
Math. J. 112 (2002), no. 3, 421–451.
On the pure cohomology of multiplicative quiver varieties.
Kevin McGerty
(joint work with Tom Nevins)
The study of moduli spaces of classes of representations of quive rs has a long
and important history: A celebrated example of the structures su ch study has
revealed is Lusztig’s geometric construction of the canonical basis . The perverse
sheaves which occur in Lusztig’s canonical basis can be characteris ed microlocally
in terms of the moduli spaces of representations of the preproje ctive algebra of
Dlab and Ringel, and framed versions of these moduli spaces also aro se in the
work of Kronheimer and Nakajima on moduli spaces of instantons. N akajima’s
later generalization of this work, and the rich theory that revealed have made
quiver varieties central objects of geometric representation th eory.
More recently, the study of moduli spaces of connections, and in p articular the
Deligne-Simpson problem, led Crawley-Boevey and Shaw [2] to introdu ce certain
“multiplicative” analogues of quiver varieties: these are symplectic v arieties which
are moduli spaces for a multiplicative version of the preprojective a lgebra, and they
include as special cases character varieties of Riemann surfaces w ith punctures.
3114 Oberwolfach Report 52/2018
Work of Boalch [1] has also show how such varieties arise as moduli spa ces of
irregular connections. In the present talk we describe recent join t work with T.
Nevins on the pure cohomology of multiplicative quiver varieties, show ing that
it is generated by the Chern classes of tautological bundles. (Unlike the setting
of Nakajima’s quiver varieties, the full cohomology ring of a multiplicat ive quiver
variety need not be pure, so the pure part is the largest subalgebr a one can hope
to generate by tautological classes.) Our main tool in establishing th is result is the
construction of a compactiﬁcation of a multiplicative quiver variety t o which the
tautological bundles naturally extend. To ﬁnd such a compactiﬁcat ion, we study
the moduli space of graded representations of a kind of “graded v ersion” of the
Crawley-Boevey-Shaw multiplicative preprojective algebra.
References
[1] P. Boalch, Global Weyl groups and a new theory of multiplicative quiver varieties, Geom.
Topol. 19 (2016) no. 6, 3467–3536.
[2] W. Crawley-Boevey, P. Shaw, Multiplicative preprojective algebras, middle convoluti on and
the Deligne-Simpson problem , Adv. Math. 201 (2006), 180–208.
The Coherent Satake Category
Harold Williams
(joint work with Sabin Cautis)
Let G be a complex reductive group. The Satake category PG(O)(GrG) of G(O)-
equivariant perverse sheaves on the aﬃne Grassmannian Gr G plays a fundamental
role in geometric representation theory and, in particular, the geo metric Langlands
program. Its structure is well understood via the geometric Sata ke equivalence of
[11, 5, 13], which states that PG(O)(GrG) is monoidally equivalent to the repre-
sentation category of the Langlands dual group G∨.
Like its constructible counterpart, the derived category of G(O)-equivariant
coherent sheaves on Gr G has a perverse t-structure [2] which is ﬁnite length and
stable under convolution. This gives us the coherent Satake categoryPG(O)
coh (GrG).
In contrast with PG(O)(GrG) this monoidal category is not semi-simple and is
poorly understood.
In the joint work [3] we pursue the structure theory of the coher ent Satake
category. Our main results are that
(1) PG(O)
coh (GrG) admits renormalized r-matrices,
(2) PG(O)
coh (GrG) is rigid as a monoidal category (i.e. every object has a left
and right dual), and
(3) PGLn(O)
coh (GrGLn) is a monoidal cluster categoriﬁcation.
By sayingPG(O)
coh (GrG) admits renormalized r-matrices, we mean that for any
nonzero objects F,G∈P G(O)
coh (GrG) there is a canonical nonzero map
rF,G :F∗G→G∗F ,
Enveloping Algebras and Geometric Representation Theory 3115
and that collectively these maps satisfy a list of several axioms. Rou ghly, these
axioms say that although the maps rF,G do not constitute a braiding ( F∗G and
G∗F are not isomorphic in general), their failure to do so is controlled in a pr ecise
sense by certain inequalities. The construction and characteristic properties of the
maps rF,G are similar to those of the renormalized r-matrices which appear in the
representation theory of quantum loop algebras [7] and KLR (or qu iver Hecke)
algebras [8], hence our terminology.
The origin of renormalized r-matrices in PG(O)
coh (GrG) is the Beilinson-Drinfeld
(BD) Grassmannian [1]. The BD Grassmannians of A1 and its powers are ind-
schemes GrG,An over An forn> 0. Collectively they form the prototypical example
of a factorization space, meaning they satisfy certain compatibility conditions on
their restrictions to diagonals and disjoint loci. Their role in the const ruction of
renormalized r-matrices is closely related to their role in establishing the commu-
tativity constraint used to prove the geometric Satake equivalenc e.
As in the setting of quantum loop algebras and KLR algebras [9], renor malized
r-matrices together with certain properties implied by rigidity strong ly constrain
the behavior of real simple objects – that is, objects whose convo lution square is
again simple. On the other hand, the coherent Satake category ha s an abundance
of real simple objects: for any integer ℓ and dominant coweight λ∨ an example is
given by the restriction of the line bundle O(ℓ) on Gr G to the G(O)-orbit closure
Gr
λ∨
G , shifted to lie in cohomological degree − 1
2 dim Gr
λ∨
G .
SincePG(O)
coh (GrG) is ﬁnite length, the classes of simple objects form a basis in
its Grothendieck ring KG(O)(GrG). Following the framework developed in [10] to
study the upper global or dual canonical bases of quantum group s [12, 6], results
(i) and (ii) above provide a mechanism by which this basis – in particular, the
subset formed by classes of real objects – may come to include the structure of a
cluster algebra.
A cluster algebra is a ring with a partial basis of a certain form: it cont ains
special elements (cluster variables) grouped into overlapping subs ets (clusters)
such that the monomials in any cluster are again basis elements [4]. Any two
clusters are connected by a sequence of mutations, an operation which creates a
new cluster by exchanging a single cluster variable for a new one.
For any particular G, to deduce that the classes of simple perverse coherent
sheaves endowKG(O)(GrG) with the structure of a cluster algebra (i.e. to dedue re-
sult (iii)) from results (i) and (ii) using the strategy of [10] one must s how, by hand,
that a ﬁnite subset of would-be cluster variables and mutations in KG(O)(GrG)
lift to suitable real simple objects and exact sequences. In [3] this is carried out
fully in the case G =GLn, however a similar result is anticipated in the case of a
general reductive group.
3116 Oberwolfach Report 52/2018
References
[1] A. Beilinson and V. Drinfeld, Quantization of Hitchin ’s ﬁbration and Langlands’ program ,
Algebraic and geometric methods in mathematical physics 19, 1–332.
[2] R. Bezrukavnikov, M. Finkelberg and I. Mirkovi´ c, Equivariant homology and K-theory of
aﬃne Grassmannians and Toda lattices , Compositio Mathematica 141 (2005), 746–768.
[3] S. Cautis and H. Williams, Cluster theory of the coherent Satake category , arXiv:1801.08111
(2018).
[4] S. Fomin and A. Zelevinsky, Cluster algebras. I. Foundations , Journal of the American
Mathematical Society 15 (2002), 497–529.
[5] V. Ginzburg, Perverse sheaves on a loop group and Langlands duality , arXiv:alg-
geom/9511007 (1995).
[6] M. Kashiwara, On crystal bases of the Q-analogue of universal enveloping algebras , Duke
Mathematical Journal 63 (1991), 465–516.
[7] M. Kashiwara, On level-zero representations of quantized aﬃne algebras , Duke Mathemat-
ical Journal 112 (2002), 117–175.
[8] S.-J. Kang, M. Kashiwara, and M. Kim, Symmetric quiver Hecke algebras and R-matrices
of quantum aﬃne algebras , arXiv:1304.0323 (2013).
[9] S.-J. Kang, M. Kashiwara, M. Kim, and S.-j. Oh, Simplicity of heads and socles of tensor
products, Compositio Mathematica 151 (2015), 377–396.
[10] S.-J. Kang, M. Kashiwara, M. Kim, and S.-j. Oh, Monoidal categoriﬁcation of cluster alge-
bras, Journal of the American Mathematical Society 31 (2018), 349–426.
[11] G. Lusztig, Singularities, character formulas, and a q-analog of weight multiplicities ,
Ast´ erisque101 (1983), 208–229.
[12] G. Lusztig, Canonical bases arising from quantized enveloping algebra s, Journal of the Amer-
ican Mathematical Society 3 (1990), 447–498.
[13] I. Mirkovi´ c and K. Vilonen, Perverse sheaves on aﬃne Grassmannians and Langlands du-
ality, Mathematical Research Letters 17 (2000), 13–24.
Grothendieck ring isomorphisms, cluster algebras and
Kazhdan-Lusztig polynomials
David Hernandez
(joint work with Hironori Oya)
