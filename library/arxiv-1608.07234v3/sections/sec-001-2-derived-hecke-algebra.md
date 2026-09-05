---
doc_id: arxiv-1608.07234v3
doc_title: "DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS AKSHAY VENKA TESH"
section_id: sec-001-2-derived-hecke-algebra
section_title: "Derived Hecke algebra"
section_number: 2
pages: 11-85
source_pdf: 1608.07234v3.pdf
source_sha256: 311730670d2fdcb7
doc_brief: "DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS AKSHAY VENKA TESH — We describe a graded extension of the usual Hecke algebra: i t acts in a graded fashion on the cohomology of an"
---
and deﬁne q so that 2q `δ “ dimY pKq. These have the same signiﬁcance as described
in (5), at least if we suppose that the center of G is anisotropic overF .
We will will work only with open compact subgroups with a prod uct structure, i.e.
(19) K “
ź
Kv
where Kv Ă GpFvq is an open compact subgroup, and Kv is a hyperspecial maximal
compact of Gv for all but ﬁnitely many primes v. A prime v will be “good” for K when
Kv is hyperspecial and the ambient group G is quasi-split at v. The “level of K” will be,
by deﬁnition, the (ﬁnite) set of all primes v which are not good.
G has a dual group G_, which we will regard as a split Chevalley group over Z; in
particular, its Lie algebra is deﬁned over Z, and its points are deﬁned over any ring R. We
regard it as equipped with a maximal torus T _ inside a Borel subgroup B_.
In the discussion of the Taylor–Wiles method, which takes pl ace in §6 and §8, it is
convenient to additionally assume:
G is simply connected and G_ is adjoint.
This is a minor issue, to avoid the usual difﬁculties of “squa re roots.” One could (better)
replaceG_ by some version of the c-group of [7].
When we discuss Galois cohomology, we will follow the usual c onvention that, for
a module M under the absolute Galois group GalpL{Lq of a ﬁeld M , we denote by
H ˚pL,M q the continuous cohomology of the proﬁnite group GalpL{Lq with coefﬁcients
inM . For L a number ﬁeld, with ring of integers O ĂL, we denote by H 1pOr 1
S s,M q Ă
H 1pL,M q the subset of classes that are unramiﬁed outside S andH 1
f pOr 1
S s,M q Ă H 1pOr 1
S s,M q
the classes that are, moreover, crystalline at p.
Warning: In the literature, the subscript f is often used to mean classes that are crys-
talline at p and unramiﬁed at all other places, not merely at places outside S. Indeed, we
implicitly used this notation in §1.2 and §1.3 when we wrote H 1
f pGQ, ´q. However, in the
remainder of the text, we will not use this convention. To avo id any confusion, on the one
occasion (in §9) we wish to refer to classes that are crystall ine at p and unramiﬁed at all
other places, we will use the notation H 1
f,ur. This notation will be reprised when it is used
so the reader need not remember it now.
2. D ERIVED HECKE ALGEBRA
We introduce the derived Hecke algebra (Deﬁnition 2.2) and t hen give two equivalent
descriptions in §2.3 and §2.4. The model given in §2.3 is by fa r the most useful. We shall
then describe the action of the derived Hecke algebra on the c ohomology of an arithmetic
group in §2.6, and then make it a bit more concrete in §2.10. Fi nally, §2.12 discusses some
minor points to do with change of coefﬁcient ring, and §2.13 d iscusses some other minor
points about passage between Z{ℓn coefﬁcients and Zℓ coefﬁcients.
Appendix A expands on various points of homological algebra that are used in the
current section.
2.1. As in §1.8, we ﬁx a prime v ofF , with residue ﬁeld Fv of characteristicpv and size
qv, and set Gv “ GpFvq. We denote by Uv an open compact subgroup of Gv. Eventually,
we will use only the case of Uv being either a maximal compact subgroup or an Iwahori
subgroup, but there is no need to impose this. When we are work ing strictly in a local
setting, we will abbreviate these simply to G andU :
G “Gv, U “Uv.
12 AKSHA Y VENKA TESH
It will also be convenient to ﬁx
(20) Vv “ a pro-pv, normal, ﬁnite index subgroup of Uv,
which we again abbreviate to V when it will cause no confusion.
Let S be a ﬁnite coefﬁcient ring in which qv is invertible. In what follows, by “ G-
module” we mean a module M under the group algebra SG with the property that every
m PM has open stabilizer in G. The category of G-modules is an abelian category and it
has enough projective objects (see §A.2).
The usual Hecke algebra for the pair pG,U q can be deﬁned as the endomorphism ring
HomSGpSrXs,S rXsq, whereX “G{U andSrXs denotes the freeS-module on a setX.
Motivated by this, we deﬁne:
2.2. Deﬁnition. The derived Hecke algebra for pG,U q with coefﬁcients in S is the graded
algebra
(21) H pG,U qS :“ Ext˚pSrG{U s,S rG{U sq,
where the Ext-group is taken inside the category of G-modules.
Let us record some variants on the notation:
- We will write simply H pG,U q when the coefﬁcients are understood to be S;
- We write H jpG,U q or H pjqpG,U q for the component in degree j, i.e. the Extj
summand on the right.
- In global situations where we have ﬁxed a level structure Kv⩽ Gv for all v, or
for almost all v, we will often write simply Hv,S for the corresponding derived
Hecke algebra H pGv,Kvq. Again we will write simply Hv if the coefﬁcients are
understood to be S.
If we choose a projective resolution P of SrG{U s as G-module, then H pG,U q is
identiﬁed with the cohomology of the differential graded al gebra HomSGpP, Pq. It will
be convenient for later use to make an explicit choice of P: Let Q be a free resolution
of the trivial module S in the category of SrU {V s-modules. We may take P to be the
compact induction (from U to G) of Q. Observe that all the groups Pi of the resulting
resolution are free S-modules.
2.3. Description in terms of invariant functions. We may also describe H pG,U q as the
algebra of “G-equivariant cohomology classes onG{U ˆG{U with ﬁnite support modulo
G.” We now spell out carefully what this means; an explicit iso morphism between this
description and Deﬁnition 2.2 is constructed in Appendix §A .
First some notation: forx,y PG{U , we denote byGxy the pointwise stabilizer of px,y q
insideG; it is a proﬁnite group. We denote by H ˚pGxy,S q the continuous cohomology of
Gxy with coefﬁcients in S (discretely topologized).
In this model, an element of H pG,U q is an assignment h that takes as input px,y q P
G{U ˆ G{U and produces as output hpx,y q P H ˚pGxy,S q, subject to the following
conditions:
‚ h isG-invariant, that is to say,rgs˚hpgx,gy q “ hpx,y q, where rgs˚ :H ˚pGgx,gy q Ñ
H ˚pGxyq is pullback by Adpgq.
‚ h has ﬁnite support modulo G, i.e. there is a ﬁnite subset T ĂG{U ˆG{U such
thathpx,y q “ 0 if px,y q does not lie in the G-orbit ofT .
DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS 1 3
The addition andS-module structure on H pG,U q is deﬁned pointwise. The product is
given by the rule
(22) h1 ˚h2px,z q “
ÿ
yPG{U
h1px,y qlo o omo oon
H˚ pGxyq
Yh2py,z qlo o omo o on
H˚ pGyz q
where we give the right-hand side the following meaning: The cup product on the right
makes sense inH ˚pGxyz,S q, i.e. ﬁrst restrict h1 andh2 toH ˚pGxyz,S q, and take the cup
product there. Now split G{U as a disjoint union šOi of orbits under Gxz; let O be one
such orbit. We regard
(23)
ÿ
yPO
h1px,y q Yh2py,z q :“ Cores
Gxy0 z
Gxz ph1px,y 0q Yh2py0,z qq
wherey0 PO is any representative, and the “trace” or corestriction is t aken fromGxy0z to
Gxz; note that the right-hand side of (23) is independent of choi ce of y0 P O. Adding up
over orbitsO gives the meaning of the right-hand side of (22).
Remark. Suppose that ∆ is a compact subgroup of G that stabilizes every point of G{U .
In this case, we can restrict h to get a functionh∆ :G{U ˆG{U ÑH ˚p∆ q. We also have
phh1q∆ “h∆ h1
∆ , where the right-hand multiplication is the more familiar
(24) h∆ h1
∆ px,z q “
ÿ
yPG{U
h∆ px,y q Yh1
∆ py,z q.
2.4. Double coset description. Finally, we can describe H pG,U q in terms of double
cosetsU zG{U . For x PG{U let
Ux “U X AdpgxqU
wheregx PG representsx (that is to say, x “gxU q. Then Ux is the stabilizer of x inU .
Fix a set of representatives rU zG{U s Ă G{U for the left U -orbits on G{U . Then we
have an isomorphism of S-modules
(25)
à
xPrUzG{Us
H ˚pUx,S q „Ñ H pG,U q
given thus: Fix a class z P rU zG{U s, and a representative gz P G forz – thus z “ gzU .
Letα P H ˚pUz,S q. Then the class of α P H ˚pUz,S q, considered as an element of the
left-hand side of (25), is carried to the function hz,α onG{U ˆG{U characterized by the
following properties:
(i) hz,αpx,y q “ 0 unless px,y q belongs to the G-orbit of pz,eU q.
(ii) hz,α sends pz,eU q toα PH ˚pUz,S q – note that Uz is exactly the common stabi-
lizer ofz andeU .
This gives another description of H pG,U q. It is harder to directly describe the mul-
tiplication rule in this presentation, and we use instead th e isomorphism to the previous
description. Later on we’ll describe explicitly the action ofhz,α on the cohomology of an
arithmetic manifold.
Now let us examine the “size” of H pG,U q; this discussion is really only motivational,
and so we will be a little informal. Suppose, for example, tha tG is split andU is hyperspe-
cial. In this case, the quotient U zG{U is parameterized by a dominant chamber X˚pAq`
inside the co-character group X˚pAq of a maximal split torus A. Moreover, if x P G{U
is a representative for a double coset parameterized by λ P X˚pAq, then the group Ux is,
14 AKSHA Y VENKA TESH
modulo a pro-p-subgroup, the Fv-points MλpFvq of the centralizer Mλ of λ. Thus we
obtain an isomorphism of S-modules:
H pG,U q :“
à
λPX˚ pAq`
H ˚pMλpFvq,S q
For “generic” λ – i.e., away from the walls of X˚pAq` – the group Mλ is a split torus; the
order of its Fv-points is a power of pqv ´ 1q. Thus if pqv ´ 1q is invertible on S, all the
terms of H pG,U q corresponding to dominant λ vanish.
In this paper we will be primarily concerned with the case whe nqv ´ 1 “ 0 insideS.
Although it is certainly interesting to study H pG,U q in general, the preceding discussion
shows that this case (i.e. qv “ 1 inS) is where H pG,U q is “largest.”
2.5. Derived invariants. IfM is any complex of G-modules, we may form the derived
invariants
derivedU -invariants onM :“ HomSGpSrG{U s,M q P DpModSq
where Hom is now derived Hom in the derived category of G-modules, taking values in
the derived category of S-modules.
Then the derived Hecke algebra automatically acts on the coh omology of the derived
invariants:
(26) H pG,U q ýH ˚pderivedU -invariants onM q.
Indeed, the derived invariants are represented by the compl ex HomSGpP,M q, where P
is as before any projective resolution of SrG{U s. The action of HomSGpP, Pq on this
complex furnishes the desired (right) action of H pG,U q.
Let us describe the derived invariants in more familiar term s. Let V be as in (20), and
consider the explicit projective resolution P discussed in §2.2; we see that the derived
U -invariants are computed by the complex HomSU pQ,M q. This coincides with U {V -
homomorphisms from Q to the termwise invariantsMV ; since Q is a projective resolution
ofS in the category of U {V -modules, we see that
(27) derived U -invariants onM » HomSU {V pS,M V q P DpModSq.
where the right hand side is derived homomorphisms, in the de rived category of U {V -
modules. In other words, there is an identiﬁcation
H ˚pderivedU -invariants onM q » H˚pU {V,M V q,
the group hypercohomology of the ﬁnite group U {V acting on the complex of termwise
invariantsMV .
2.6. Arithmetic manifolds. In the remainder of this section, we describe how the derived
Hecke algebras act on the cohomology of arithmetic manifold s.
We follow the notation of §1.8. In particular, we ﬁx K Ă GpAf q an open compact
subgroup, which we are supposing to have a product structure K “ ś
wKw; let us split
this as
K “K pvq ˆKv
whereK pvq “ ś
w‰vKw is the structure “away fromv.” Associated to this is an arithmetic
manifoldY pKq, as in (17).
We will construct an action of the derived Hecke algebra Hv “ HvpGv,Kvq on the
cohomology of Y pKq. To do so, we will exhibit Y pKq as the derived Kv-invariants on a
suitableGv-module, and then apply (26).
DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS 1 5
ForUv any open compact subgroup of Gv, let us abridge:
(28) C˚pUvq “ cochain complex of Y pK pvq ˆUvq withS coefﬁcients.
Now let
M “ limÝ ÑUv
C˚pUvq.
where the limit is taken over open compact subgroups Uv⩽ Gv. Visibly,M is a complex
of smoothGv-modules. Choosing Vv ĂKv as in (20), we have
MVv »C˚pVvq,
since we may interchange invariants and the direct limit; and then for a ﬁnite cover X ÑY
with Galois group D we have an isomorphism C˚pY q „ÑC˚pXqD. However, the derived
invariants of Kv{Vv on C˚pVvq “coincide with” the cohomology of Y pKq: the natural
map
C˚pY pKqq “ C˚pVvqKv {Vv Ñ HomSrKv{Vv spS,C ˚pVvqq
is a quasi-isomorphism, in the derived category of S-modules. This follows from the
fact that the terms C˚pVvq have no higher cohomology as Kv{Vv-modules, because each
CjpVvq is the module of S-valued functions on a free Kv{Vv-set and is in particular in-
duced from a representation of the trivial group.
We have exhibited a quasi-isomorphism
C˚pY pKqq » derivedKv-invariants onM
betweenC˚pY pKqq and a complex that represents the derived invariants of Kv acting on
M . Thus (26) gives a natural right action of H pGv,Kvq on the cohomology of Y pKq.
Remark. Although this is strictly a right action, we will often write it on the left, which con-
forms more to the usual notation for Hecke operators; the rea der should therefore remem-
ber that the multiplication needs to be appropriately switc hed at times, but this will cause
almost no issue because the derived Hecke algebra will prove to be graded-commutative at
all the places we use.
Of course, this description is totally incomprehensible; t hus we now work on translating
it to something more usable.
2.7. Digression: pullback from a congruence quotient. We ﬁrst need a brief digression
to construct certain cohomology classes on Y pKq. These are called “congruence classes”
in [10], because they capitulate in congruence covers of Y pKq.
There is a natural map
(29) H ˚pKv,S q Ý ÑH ˚pY pKq,S q,
where, on the left,H ˚pKv,S q is the continuous cohomology of the proﬁnite group K with
coefﬁcients in (discretely topologized) S. Indeed, any cohomology class for H ˚pKv,S q
is inﬂated from a quotient Kv{Kv,1. Let K1 be the preimage of Kv,1 inK. The covering
Y pK1q Ñ Y pKq has deck group Kv{Kv,1, and thus gives rise to a map, well-deﬁned up
to homotopy,
(30) Y pKq Ý Ñclassifying space of Kv{Kv,1.
We may then pull back cohomology classes along this map to get (29).
These “congruence” cohomology classes have a very simple be havior under Hecke op-
erators:
16 AKSHA Y VENKA TESH
2.8. Lemma. Let h be in the image of the map (29). F or any prime w of F that does
not divide the level of K or the size of S, such that GpFwq is split, and any usual Hecke
operatorT supported atw, we have
Th “ degpT qh.
We will give a direct proof, but let us note that one can also de duce the result from the
commutativity of the Hecke algebra atw (which is proved, under mild restrictions on w, in
§3). It is also likely that the assumption that GpFvq is split is unnecessary (sincew doesn’t
divide the level of K, it is automatically quasi-split by our deﬁnitions, which s hould be
enough for the argument below to go through).
Proof. It is easy to verify this if w ‰v, so we examine only the case w “v.
By the assumptions, we may suppose that Kv “ GpOvq, for a split reductive G over
Ov. Suppose that T arises from the double coset KvavKv, where, without loss, a lies in
a maximal split torus ApFvq that is in good position relative to Kv – i.e. it extends to a
maximal split torus of G.
We will show thath has the same pullback under the two natural maps
π1,π 2 :Y pK X AdpavqKq Ñ Y pKq,
namely, the natural map, and the map induced by multiplicati on by av; this implies the
Lemma.
There is an isomorphism X˚pAq » Av{pAv XKvq; let M be the centralizer in G of
the co-character in X˚pAq that corresponds to the class of a. Let K2 be the preimage,
underKv Ñ GpOv{̟D
v q, of MpOv{̟D
v q; here D is a large enough integer, and ̟v a
uniformizer.
Then, on the one hand, the inclusion K2 ãÑK X AdpavqK has index equal to a power
of qv. In particular, it induces an injection on H ˚p´,S q, so it is enough to verify that
π˚
1h “π˚
2h after pullback under Y pK2q Ñ Y pK X AdpavqKq.
However, the pullback H ˚pGpFvq,S q Ñ H ˚pKv,S q is an isomorphism. The class h
is therefore actually pulled back from GpFvq. Our assertion then follows from the fact that
the natural maps K2 Ý ÑGpFvq – namely, the reduction map, and the conjugate of the
reduction map by av – actually coincide. This proves that π˚
1h “π˚
2h, and concludes the
proof of the Lemma. □
This motivates the following deﬁnition:
2.9. Deﬁnition. W e say a classh PH ˚pY pKq,S q is Hecke-trivial if, for all places v that
do not divide the level of K and with residue characteristic invertible on S, and all Hecke
operatorsT supported atv,
pT ´ degpT qqnh “ 0.
for a sufﬁciently large integer n “ npT q. W e denote by H ˚pY pKq,S qtriv the submodule
of Hecke–trivial classes.
2.10. Concrete expression for the action of Hv on H ˚pY pKq,S q. Let us now give a
more down-to-earth description of the action of Hv,S onH ˚pY pKq,S q, with notation as
above. In particular, we will show that the action of element shz,α can be described in a
fashion that is very close to the usual deﬁnition of Hecke ope rators.
Fromz “ gzKv P Gv{Kv, and α P H ˚pKv X AdpgzqKvq, we obtain a class hz,α P
H pGv,Kvq, by the recipe of §2.4. Then:
2.11. Lemma. Write
Kz “K X AdpgzqK, K 1
z “K X Adpg´1
z qK.
DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS 1 7
Also, let xαy be the image of α underH ˚pKv X AdpgzqKvq
(29)
Ñ H ˚pY pKzq,S q. Then the
action ofhz,α onH ˚pY pKq,S q coincides with the following composite
(31) H ˚pY pKqq
rgzs˚
Ñ H ˚pY pKzqq
Yxαy
Ñ H ˚pY pKzqq Ñ H ˚pY pKqq,
where all cohomology is taken with S coefﬁcients, and the arrows are (respectively)
pullback by the map Y pKzq Ñ Y pKq induced by the map g ÞÑ ggz, cup with xαy, and
push-forward for the standard map Y pKzq Ñ Y pKq.
Note that this is almost exactly the same as a usual Hecke oper ator; we have just in-
serted the operation of Yxαy on the way. The fact that xαy is Hecke-trivial, in the sense
of Deﬁnition 2.9, is the key point that makes this operation c ommute with usual Hecke
operators.
Proof. Routine but extremely tedious; see §A. □
Remark. Note also the following trivial case: taking gz “ 1, we see that the operation of
“cup with α PH ˚pKv,S q” always belongs to the derived Hecke algebra.
Remark. As an example let us write out the argument that derived Hecke operators at dif-
ferent places always commute with one another. Fix placesv ‰w, elementsgv PGv,gw P
Gw, and classesαv PH ˚pKv X AdpgvqKvq andαw PH ˚pKw X AdpgwqKwq. We claim
that the composite of the two associated derived Hecke opera tors can be described in the
following way, which makes graded commutativity clear: Pus h-pull aong
Y pKq Ð Y pKgv XKgw q Ñ Y pKq,
but cup in the middle with the class ofαv Yαw. To verify this claim, examine the following
diagram:
(32) Y pKgv X Kgw q
ˆ gw
/d119/d119♦♦♦♦♦♦♦♦♦♦♦
/d39/d39❖❖❖❖❖❖❖❖❖❖❖
Y pKgv q
ˆ gv
/d122/d122✉✉✉✉✉✉✉✉✉
/d39/d39❖❖❖❖❖❖❖❖❖❖❖ Y pKgw q
ˆ gw
/d119/d119♦♦♦♦♦♦♦♦♦♦♦
/d36/d36❏❏❏❏❏❏❏❏❏
Y pKq Y pKq Y pKq
When we write (e.g.) ˆgv we mean that the map is induced by right multiplication by gv.
The composite of the derived Hecke operators is, by deﬁnitio n, obtained by going along
the bottom two rows. However, the middle diagram is a ﬁber pro duct square, and so the
two ways of going from Y pKgv q to Y pKgw q, via “push-pull” or “pull-push,” coincide.
To prove the desired claim, then, it sufﬁces to show that the t wo pullbacks of the class
xαvy P H ˚pY pKgv qq toH ˚pY pKgv XKgw qq – via the natural map, and via the map ˆgw
– actually coincide.
Equivalently, the classes obtained from αv, in the natural way on Y pKgv XgwKg ´1
w q
and onY pKgv Xg´1
w Kgwq are in fact compatible, under the map ˆgw from one space to
the other. However, these cohomology classes are obtained f rom a certain covering of the
spaces, obtained by adding extra level at v, and the compatibility follows from the fact that
ˆgw lifts to these coverings.
18 AKSHA Y VENKA TESH
2.12. Change of coefﬁcients. Let us examine what happens under a change of rings
S Ñ S1. The description of §2.4 and the explicit action of §2.10 mea ns that there is a
map of Hecke algebra Hv,S Ñ Hv,S 1 compatible with the actions on H ˚pY pKq,S q Ñ
H ˚pY pKq,S 1q. However, this does not make quite clear that the change of ri ngs map is
an algebra homomorphism. For completeness let us explain th is now, since we will want
to freely pass between Z{ℓn coefﬁcients for various ns.
The tensor product bSS1 is a right exact functor from SG-modules to S1G modules
and so it can be derived to a map of derived categories. Note th at this carries projectives to
projectives since HomS1Gv pP bSS1, ´q “ HomSGv pP, ´q.
This derived tensor product (let us write it as b) “carries SrGv{Kvs toS1rGv{Kvs:” if
we choose a projective replacement P ÑSrGv{Kvs the natural map
P bSS1 Ý ÑS1rGv{Kvs
is a quasi-isomorphism. Indeed it is possible to choose P so that each term of P is free
as anS-module (see the explicit resolution after (21)). Then P bSS1 has no cohomology
in higher degree (since this complex computes the TorSpSrGv{Kvs,S 1q and the former is
free) and thus it is a resolution of S1rGv{Kvs.
This yields at once a map
Hv,S Ñ Hv,S 1.
from the Hecke algebra with S coefﬁcients, to the same with S1 coefﬁcients. Explic-
itly, the left-hand side is represented by the cohomology of the differential graded algebra
HomSGpP, Pq, and this dga maps to HomS1Gv pP bS S1, P bS S1q, whose cohomology
computes Hv,S 1. This is the desired algebra map “change of coefﬁcients.”
Consider now the obvious map
ι : limÝ ÑUv
C˚pUvq Ñ limÝ ÑUv
C˚pUv;S1q,
where the notation is as in (28), and the right-hand side is de ﬁned the same way but with
S1 coefﬁcients. This induces
ι1 : HomSGpP, limÝ ÑUv
C˚pUvqq Ñ HomS1G
˜
P bSS1,
˜
limÝ ÑUv
C˚pUv;S1q
¸¸
wherein we compose with ι and extend by S-linearity. There are compatible actions of
Hv,S and Hv,S 1 on the left and right sides. On the other hand, the map ι1 induces on
cohomology the natural map H ˚pY pKq,S q Ñ H ˚pY pKq,S 1q.
To summarize: the actions of Hv,S on H ˚pY pKq,S q and Hv,S 1 on H ˚pY pKq,S 1q
are compatible, with respect to the natural maps Hv,S Ñ Hv,S 1 and H ˚pY pKq,S q Ñ
H ˚pY pKq,S 1q.
2.13. Passage from modℓn toℓ-adic; the global derived Hecke algebra. We now write
out in grotesque detail certain minor details of the passage from mod ℓn to ℓ-adic coef-
ﬁcients, which will be used without comment in our later proo fs. This section should
probably be skipped by the reader and consulted only as neede d.
In what follows, we will describe the straightforward versi on of the global derived
Hecke algebra using all good primes for K that do not divide ℓ; here “good” is deﬁned
after (19). When we refer to the global derived Hecke algebra without any further remark,
we are always referring to this version. We will remark, after the construction, how to
make a deﬁnition using a restricted set of primes.
DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS 1 9
The action of the derived Hecke algebra gives an algebra of en domorphisms rTn Ă
EndpH ˚pY pKq, Z{ℓnqq, namely the algebra of endomorphisms generated by all the de -
rived Hecke algebras Hv,Z{ℓn wherev varies over good primes of K that are not above
ℓ.
Now we have
H ˚pY pKq, Zℓq “ limÐ ÝH ˚pY pKq, Z{ℓnq
and we deﬁne the global derived algebra (relative to the ﬁxed set V of places) to be
(33) ˜T Ă EndpH ˚pY pKq, Zℓqq
to be those endomorphisms of the form limÐ Ýtn, for some compatible system tn P ˜Tn, i.e.
tn “reduces to tm” for n ąm in the sense that the following diagram should commute:
(34) H ˚pY pKq, Z{ℓnq
tn /d47/d47
/d15/d15
H ˚pY pKq, Z{ℓnq
/d15/d15
H ˚pY pKq, Z{ℓmq
tm /d47/d47H ˚pY pKq, Z{ℓmq.
Let ˜T˚
n be the systems of elements ptn,tn´1,...,t 1q, where tr P rTr for r ď n are
all compatible in the sense that the above diagram should com mute for each tr,tr1. In
particular, ˜T˚
n acts on Z{ℓr-valued cohomology for each r ď n. The inverse limit limÐ Ý˜T˚
n
acts onH ˚pY pKq, Zℓq, and its image in EndH ˚pY pKq, Zℓq is precisely the global derived
Hecke algebra ˜T.
Fixm. For n ěm consider the map
˜T˚
n Ñ ˜T˚
m.
For increasingn and ﬁxed m, the image of this map gives a decreasing sequence of subsets
of the ﬁnite set ˜T˚
m. This sequence must stabilize. Call this stabilization ˜T8,m; it is a
subring of rT˚
m and thus acts by endomorphisms of H ˚pY pKq, Z{ℓmq; also, there exists
Nm such that ˜T8,m coincides with the image of ˜T˚
Nm in ˜T˚
m.
The natural map
(35) limÐ Ý˜T˚
n Ñ ˜T8,m
is onto, since we’re dealing with an inverse system of ﬁnite s ets.
Let Hv,Z{ℓn be the local derived Hecke algebra at v with Z{ℓn-coefﬁcients. We show
later (§3.4) that, if ℓn dividesqv ´ 1, then the natural map Hv,Z{ℓn Ñ Hv,Z{ℓm is sur-
jective. It follows that if qv ´ 1 is divisible by ℓNm, then the image of ˜T˚
Nm acting on
H ˚pY pKq, Z{ℓmq contains the image of Hv,Z{ℓm . Therefore, the image of ˜T8,m acting
onH ˚pY pKq, Z{ℓmq contains the image of Hv,Z{ℓm .
In practice, we will establish “bigness” results of the foll owing type:
(*) For allm ďn, there exists sets of primesQn “ tq1,...,q ru such that
ℓn dividesqi´1 and the image of biHqi,Z{ℓm acting onH ˚pY pKq, Z{ℓmq
is “large:” H ˚pY pKq, Z{ℓmq is generated over biHqi,Z{ℓm by elements
of some ﬁxed degree D.
When we prove such results, it will not be for the full cohomol ogy of Y pKq but rather
for its localization at some ideal of the Hecke algebra, but w e suppress that for the current
discussion.
20 AKSHA Y VENKA TESH
Let us prove that, under this assumption (*), H ˚pY pKq, Zℓq is generated over ˜T by
elements of degreeD. The assumption implies (by the previous discussion, with n “Nm)
thatH ˚pY pKq, Z{ℓmq is generated over ˜T8,m by elements of degreeD; by (35), it is also
generated over limÐ Ý˜T˚
n by elements of degree D. That is to say,
plimÐ Ý˜T˚
nq bHDpY pKq, Z{ℓmq
surjects ontoH ˚pY pKq, Z{ℓmq for everym. By a compactness argument the same asser-
tion holds with Zℓ-coefﬁcients.
More generally, the same type of argument allows us to show th at various types of
“largeness” can be passed from Z{ℓm coefﬁcients to Zℓ.
2.14. Restricting places and the strict global derived Hecke alge bra. We can restrict
the primes and the powers of ℓ used in the above construction. It is convenient to index
these restrictions by a function
V : primes Ý Ñ t0, 1, 2,..., u Y t8u
where primesv withV pvq “ 0 will be not used at all in the deﬁnition.
In the above construction, replace rTn by the algebra generated by Hv,Z{ℓn wheren ď
V pvq. Proceeding as above, then, we obtain a restricted global He cke algebra ˜TpV q acting
on cohomology with Zℓ coefﬁcients. Informally, each prime v can be used at most at
torsion level Z{ℓV pvq.
For example, taking
(36) V0pvq “
#
0,v not good;
largest power ofℓ dividingqv ´ 1, else ,
the resulting algebra ˜TpV0q has the advantage that it will be graded commutative by the
results of §3, at least if ℓ doesn’t divide the order of the Weyl group.
It will be sometimes convenient to enlarge this by the usual H ecke algebra, i.e. deﬁning
the “strict” global derived Hecke algebra
˜T1 :“ algebra generated by ˜TpV0q and all underived Hecke operators at good places prime to ℓ.
However, by default, when we write ˜T, we mean the “full” version using V “ 8 for
all good primes not above ℓ, and V “ 0 at all other primes. Thus we have inclusions of
algebras, each inside endomorphisms of cohomology:
usual (underived) Hecke algebra T Ă ˜T1 Ă ˜T.
The advantage of ˜T1 is that it is clearly graded commutative.
Thus, for example, if m is a maximal ideal of T, the strict global derived Hecke algebra
˜T1 induces an algebra of endomorphisms of the m-completionH ˚pY pKq, Zℓqm:
H ˚pY pKq, Zℓqm b ˜T1 Ý ÑH ˚pY pKq, Zℓqm.
While a priori we do not know that the full ˜T preservesH ˚pY pKq, Zℓqm, this is true under
a mild additional assumption: For each good place w not equal to ℓ, let Tpwq be the prime-
to-w usual Hecke algebra, and mpwq the induced maximal ideal. Suppose that the natural
map
(37) H ˚pY pKq, Zℓqmpwq ÑH ˚pY pKq, Zℓqm
is an isomorphism. This is true, for example, if there exists Galois representations associ-
ated to cohomology classes (by the argument of [20, Lemma 6.2 0]). In this case, the local
DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS 2 1
derived Hecke algebra at w clearly preserves the left-hand side, and so also preserves the
right-hand side. Since this is true for all good w not dividing ℓ, the full ˜T also preserves
the m-completion of cohomology.
3. T ORUS LOCALIZATION AND SATAKE ISOMORPHISM
Our main goal here is to prove a version of the Satake isomorph ism that applies to the
derived Hecke algebra. Namely, take m “ ℓr a prime power. Suppose q ” 1 moduloℓr.
We show (see (40) for the precise statement)
derived Hecke algebra for split q-adic group with Z{ℓr-coefﬁcients
– pderived Hecke algebra for maximal torus with Z{ℓr coefﬁcients qW
where theW superscript means Weyl-ﬁxed, and we also require that ℓ does not divide the
order ofW .
For example, if q ” 1 moduloℓ, the derived Hecke algebra of PGL2pQqq with coefﬁ-
cients in Z{ℓ is isomorphic to
Z{ℓrx0,x ´1
0 ,y 1,z 2sZ{2
wherex0,y 1,z 2 have (respectively) degree 0, 1, 2, and the action of Z{2 switchesx˘1
0 and
negatesy1,z 2.
A consequence of our results is that (under our assumptions o nq,m ) the derived Hecke
algebra is graded commutative. We do not know if this is valid without any assumption on
q and the coefﬁcient ring S. Recall, however, that q ” 1 inS is precisely the case where
the Hecke algebra is largest, by the discussion of §2.4, and u nderstanding this case will be
enough for our global analysis.
3.1. It is a curious fact that, in characteristic dividing qv ´ 1, the Iwahori-Hecke algebra
of a split Fv-group is isomorphic to the group algebra of its afﬁne Weyl gr oup. A related
interesting phenomenon is that, under the same assumptions , the Satake isomorphism
Hecke algebra Ý ÑHecke algebra of torus
is given simply by restriction (!)
These points can be explained by “torus localization,” as we now explain. Using that
method we will derive our Satake isomorphism below. Of cours e this is a little bit cheap,
but it turns out to be exactly what we need anyway.
I am very grateful to David Treumann for conversations about this material. In particu-
lar, I learned about localization in the context of local geo metric Langlands from his paper
Smith theory and geometric Hecke algebras [33].
3.2. In this section and the next, G will be a split group over the nonarchimedean local
ﬁeld Fv. The coefﬁcient ring for all our Hecke algebras will be taken to be S “ Z{ℓr, for
a primeℓ andr ě 1. We shall suppose that ℓr divides pqv ´ 1q, whereqv is the cardinality
of the residue ﬁeld Fv. We also assume that ℓ is relatively prime to the order of the Weyl
group of G.
We ﬁx other notations as follows: Let G be a split group over Ov whose generic ﬁber
is identiﬁed with G. Let Kv “ GpOvq, a maximal compact subgroup of Gv “ GpFvq.
Let A be a maximal torus in G, and B a Borel subgroup of G containing A; we suppose
them to extend to a torus A and Borel B inside G. We write Av,Bv for the Fv-points of
A, B. We shall use the notation ApFvq˝ for the maximal compact subgroup of ApFvq,
and similar notation whenever the maximal compact subgroup is unique.
22 AKSHA Y VENKA TESH
LetW be the Weyl group for A. We write X˚ “X˚pAq for the co-character group of
A. We identify X˚ withAv{Av XKv ĂGv{Kv by means of the map
(38) χ PX˚ “ HompGm, Aq Ý Ñχp̟vq,
with̟v a uniformizer.
We write for short T “ ApFvq. The reduction map Av XKv ÑT splits uniquely, and
so we obtain a “Teichmüller” lift
(39) T ãÑAv XKv.
This induces a cohomology isomorphism, with Z{ℓr coefﬁcients.
We have a Cartan decomposition
Gv “Kv ¨Av ¨Kv
TheAv component of this decomposition is unique up to the action of the Weyl groupW .
3.3. Theorem. Let notations be as above; in particular the coefﬁcient ring is alwaysS “
Z{ℓr, whereℓr dividesqv ´ 1, andℓ does not divide the order of the W eyl group.
Then restriction (in the model of §2.3) deﬁnes an isomorphis m
(40)
derived Hecke algebra for pGv,Kvq „Ý Ñ derived Hecke algebra for pAv,Av XKvqW.
Let us explicate what we mean by “restriction.” As per §2.3, a n element h of the left-
hand side is an association:
px,y q P pGv{Kvq2↝ hpx,y q P H ˚pGxy,S q,
and its image h1 on the right-hand side is obtained by restricting to Av{pAv XKvq ãÑ
Gv{Kv and pulling back cohomology classes under the inclusion Axy ãÑ Gxy. The ele-
menth1 is clearlyAv-invariant, and it is also W -invariant:
rws˚h1pwx,wy q “ hpx,y q
because of the G-invariance ofh.
Because Axy “ Av X Kv for each x,y , and the the (Teichmüller) inclusion (39)
T ãÑ Av X Kv induces a cohomology isomorphism, we can regard h1 as a function
X˚ ˆX˚ Ý ÑH ˚pT,S q. We will often regard h1 as such without explicit comment.
The multiplication in this model is usual convolution in the X˚ variable, together with
multiplication inH ˚pT,S q. We may therefore identify the right-hand side of (40) with
(41) pSrX˚s bH ˚pT,S qqW ,
just as in (25), i.e. restrict to X˚ ˆ t0u and identify functions onX˚ with the group algebra
in the obvious way.
3.4. A useful corollary to this result is the following (alth ough even easier, as it does not
use the algebra structure): The induced map
derived Hecke algebra over Z{ℓn Ñ derived Hecke algebra over Z{ℓm
is a surjection forn ą m, under our assumption that ℓn dividesqv ´ 1. (We used this in
the discussion of §2.13).
In fact, we’re reduced to checking the same fact when C is a cyclic group of order
divisible byℓn, i.e.
H ˚pC, Z{ℓnq Ñ H ˚pC, Z{ℓmq
is surjective. This follows from a straightforward computa tion.
DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS 2 3
3.5. Some useful Lemmas.
3.6. Lemma. Any nontrivial root α of A on G is nontrivial on the ℓ-Sylow of Av XKv.
In particular ,α induces a nontrivial character ApFvq Ñ Fˆ
v .
Proof. This is just a matter of checking the residue characteristic is forced to be big
enough: if the claim is not true, the root α would be divisible by ℓr inX ˚pAq; but roots
are divisible at most by 2 because xα,α _y “ 2, and ℓ ą 2 because it’s prime to the order
of the Weyl group. □
3.7. Lemma. Use notation as above; in particular Fv is a ﬁnite ﬁeld of cardinality qv ” 1
moduloℓr, and the order of the W eyl group is not divisible by ℓ.
Then the restriction map from the cohomology H ˚pGpFvq, Z{ℓrq to W eyl-ﬁxed coho-
mology of the torus H ˚pApFvq, Z{ℓrqW is an isomorphism.
Proof. Write for short (and just for this proof) G,A,B for the Fv-points of G, A, B.
Consider the composite of restrictions
(42) H ˚pG, Z{ℓrq Ñ H ˚pB, Z{ℓrq „ÑH ˚pA, Z{ℓrq.
The second map is an isomorphism and its inverse is speciﬁed b y corestriction. Therefore
we can transport the W -action on H ˚pAq to a W -action on H ˚pB, Z{ℓrq; explicitly the
action ofw is
(43) CoresB
A ˝ rwsA ˝ ResB
A.
where rwsA is pullback of cohomology classes under Adpw´1q :A ÑA.
We will now show that ResG
B ˝ CoresG
B “ ř
wPWw, where the w-action on H ˚pBq is
that just deﬁned. Since CoresG
BResG
B “ |W |, which is invertible in Z{ℓr, we see that ResG
B
is injective and CoresG
B is surjective; so ResG
B is an isomorphism onto the W -invariants on
H ˚pB, Z{ℓrq, which implies the Lemma.
By the usual formula [6, Proposition 9.5], using the Weyl gro up W as a system of
representatives for double cosets, the composite equalsÿ
wPW
CoresB
wBw ´ 1XB ¨ Adpw´1q˚ ¨ ResB
BXw´ 1Bw
Butw´1Bw XB containsA, and rwBw ´1 XB :As “ 1 moduloℓr. So we can rewrite
thew-term as
CoresB
wBw ´ 1XB ¨ Adpw´1q˚ ¨ CoresBXw´ 1Bw
A ResB
A “ CoresB
A ¨ rwsA ¨ ResB
A
which is exactly the W -action onH ˚pBq, by (43). □
3.8. Lemma. LetG1,G 2 be ﬁnite groups. Suppose that G1 ãÑ G1 ˆG2 is the natural
inclusion, and M is a module for G1 ˆG2 killed by the order #G2 of G2. Then the
corestriction mapH ˚pG1,M q Ñ H ˚pG1 ˆG2,M q is zero.
Proof. Indeed, the composite H ˚pG1 ˆG2q ResÑ H ˚pG1q CoresÑ H ˚pG1 ˆG2q is multi-
plication by the order of G2, and is therefore zero with M coefﬁcients; but the ﬁrst Res is
surjective becauseG1 ÑG1 ˆG2 is split. □
3.9. Lemma. Let Γ Ă Gv be a ﬁnite ℓ-subgroup. Let S be the double centralizer of Γ ,
considered as an algebraic Fv-subgroup of G. Then:
(a) S has component group of prime-to-ℓ order ,
(b) the maximal compact subgroup SpFvq˝ of itsFv-points ﬁxes every point of Gv{Kv
that is ﬁxed by Γ .
24 AKSHA Y VENKA TESH
Proof. Letx PGv{Kv be ﬁxed by Γ . Conjugating Γ byGv we may suppose that x “Kv,
the identity coset in Gv{Kv.
Now, the quotient of the orders of G and A over the ﬁnite ﬁeld Fv is congruent to |W |
moduloℓ, because of our assumption ℓ dividesq ´ 1. Therefore there is an ℓ-Sylow ofKv
contained inAv XKv. Thus, further conjugating Γ byKv we can further assume that that
Γ Ă ApFvq XKv. The centralizer ZpΓ q of Γ is then a subgroup containing A. The double
centralizer S is thus contained in A and, of course, it contains Γ .
Because S Ă A, the maximal compact subgroup of SpFvq is contained in the maximal
compact ApFvq XKv of A; the latter ﬁxes x. This proves (b).
To verify the assertion about the component group of S, we ﬁrst verify that ZpΓ q is
connected. Note that S is contained in ZpΓ q by the analysis above, so it is in fact the center
of ZpΓ q. Then we are reduced to the following assertion: for any redu ctive group Z, the
component group of the center of Z is only divisible by primes dividing the order of the
Weyl group. Replacing Z by its quotient by the connected center, we can check the same
assertion for Z semisimple; so it is enough to check for Z simply connected semisimple.
There it is obvious case by case.
To see that Z “ ZpΓ q is connected, we can reason as follows: A is a maximal split torus
within Z, so any element of Z{Z0 has a representative in Z that belongs to the normalizer
of A. Here Z0 denotes the connected component. So it is enough to show that anyFv-point
n in the normalizer of A that belongs to Z actually belongs to Z0. Let w P AutpAq be the
element of the Weyl group of A corresponding to such ann. Fixγ P Γ . Sincen centralizes
Γ , we see thatw ﬁxes γ. Write N for theℓ-part ofq ´ 1. Soγ P ArN s » X˚ bµN ; ﬁxing
a primitiveN th root, we can identify ArN s withX˚{N . Since the order of w is relatively
prime to ℓ, we see – by taking invariants in X˚ Ñ X˚ Ñ X˚{N – that γ actually lies in
the image of some w-ﬁxed character Gm Ñ A.
Applying this reasoning for each γ P Γ , we see that w actually centralizes a subtorus of
A containing Γ . But the centralizer of that torus is a connected group, thus contained in
Z0. We conclude that Z is connected, as we claimed. □
3.10. Lemma. Supposez P Gv{Kv does not belong to the image of X˚ (where the map
X˚ãÑGv{Kv was deﬁned in (38)).
Let Γ be anℓ-Sylow ofAv XKv; thus Γ is anℓ-Sylow subgroup of Gxy. Let Γz be the
stabilizer ofz in Γ .
Then the corestriction map H ˚pΓzq Ñ H ˚pΓ q is zero with Z{ℓr coefﬁcients.
Proof. Note that the centralizer and so also the double centralizer of Γ is simply A. (Any
root of A is nontrivial on the ℓ-Sylow of Av XKv, by Lemma 3.6, so the connected
centralizer is A; the centralizer cannot be larger than A because any element of the Weyl
group acts nontrivially on Γ »X˚pAq{ℓr).
Let S be the double centralizer of Γz. Since Γz Ă Γ we also have S Ă A.
Let S0 be the identity component of S; it is a split torus. Because ((a) of §3.9) the
component group of S is prime-to-ℓ, we see that Γz lies inside S0, and thus inside the
maximal compact subgroup of S0pFvq. Let Γ ˚
z be theℓ-Sylow of S0pFvq. Thus Γz Ă Γ ˚
z .
Choose a complement S1 Ă A to S0, i.e. a subtorus with the property that S0 ˆS1 Ñ A
is an isomorphism. Now Γ Ă ApFvq˝ is anℓ-Sylow by computation of orders, so therefore
Γ “ Γ ˚
z ˆ Γ 1
where Γ 1 is theℓ-Sylow of S1pFvq˝.
DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS 2 5
If S1 were trivial, then S0 “ A; in that case, by (b) of §3.9, z lies in the ﬁxed set of
ApFvq˝, which is none other 6 than
X˚ ĂGv{Kv,
which contradicts our assumption. Therefore, S1 is nontrivial. We see at once that the order
of Γ 1 is divisible by the ℓ-part ofq ´ 1.
Thus, by Lemma 3.8, the corestriction from Γ ˚
z to Γ is zero with Z{ℓr coefﬁcients. The
corestriction from Γz to Γ factors through this one, so it is zero too.
□
3.11. Proof of Theorem 3.3. Throughout the proof, as in the statement of the theorem, we
take coefﬁcients in S “ Z{ℓr. Accordingly, we drop explicit mention of the coefﬁcients
from the notation.
Recall the explicit description of the Satake map, using the identiﬁcation (41) of the
toral derived Hecke algebra:
Given an assignment px,y q P Gv{Kv ÞÑ hpx,y q P H ˚pGxyq, we associate to it the
functionX˚ ˆX˚ Ý ÑH ˚pT q, given by
h1 : px,y q P pAv{Av XKvq2 ÞÑ ResGxy
T hpx,y q P H ˚pT q
We must show that the rule h ÞÑh1 gives an isomorphism
(44)
derived Hecke algebra for pGv,Kvq » derived Hecke algebra for pAv,Av XKvqW.
We ﬁrst verify that h ÞÑh1 is bijective. Each element of the derived Hecke algebra for
pGv,Kvq is uniquely of the form řha,α wherea P X `
˚ andα P H ˚pKv X AdpaqKvq,
with notation as in §2.4. The intersection of KvaKv with X˚ is precisely given by the
W -orbit of a by uniqueness of the Cartan decomposition. So the map h ÞÑh1 sendsha,α
to the function h1
a,α onX˚ ˆX˚ characterized byW -invariance and:
(i) hz,αpx,e q “ 0 unlessx PWa ;
(ii) hz,α sends pa,e q to the image of α PH ˚pKv X AdpaqKvq Ñ H ˚pT q.
It is enough, then, to show that each element of derived Hecke algebra for pAv,Av XKvqW
is uniquely a sum of such elements h1
a,α. This comes down to the fact that the map
(45) H ˚pKv X AdpaqKvq Ý ÑH ˚pT qWa
is an isomorphism, where Wa is the stabilizer of a in the Weyl group. But, if we write
M for the Levi subgroup of G that centralizesa, thenKv X AdpaqKv is, modulo a pro-p-
group, thek-pointsM pkq, andWa is identiﬁed with the Weyl group of M . So (45) follows
from Lemma 3.7.
6 Let N be the unipotent radical of the Borel B Ą A. If ApFvq˝ xKv “ xKv, we have x´ 1ApFvq˝ x Ă
Kv. By using the Iwasawa decomposition, it is enough to check th at if this inclusion holds for some x “ n P
NpFvq, then in fact n P Kv. In that case we have n´ 1an P Kv for all a P ApFvq˝ , and in particular
n´ 1pAdpaqnq P Kv for all such a.
Choose a generic positive element λ P X˚ pAq, giving an enumeration of the positive roots α 1, . . . , α s
so that xα i, λ y is increasing. For each such root we have a root subspace ui : Ga Ñ N , and the product
map uspxsqus´ 1pxs´ 1q . . . u 1px1q, from Gs
a Ñ N, extends to an isomorphism of schemes over Ov. In this
ordering, the commutator rui, u js involves only uk with k ą maxpi, j q.
Let x1 be the α 1 coordinate of n. We have pα 1paq ´ 1qx1 P Ov for all a P ApFv q˝ , which implies
x1 P Ov, cf. second paragraph of the proof of Lemma 3.10. Adjust n on the right by u1p´x1q to arrange that
x1 is trivial. Now proceed the same way for the α 2, α 3, . . . coordinate.
26 AKSHA Y VENKA TESH
To show thath ÞÑh1 preserves multiplication, we compute ph1h2q1px,z q; it equals the
restriction, fromGxz toT , of
ÿ
OĂGv {Kv
ÿ
yPO
h1px,y q Yh2py,z q.
the sum being grouped, as before, over orbits O ofGxz on such y. Recall that the inner
sum is understood by computing the cup-product h1px,y q Yh2py,z q for a single y P O,
and then corestricting from Gxyz toGxz. Therefore,
ph1h2q1px,z q “
ÿ
O
ResGxz
T CoresGxz
Gxyzh1px,y q Yh2py,z qloooooooooooooooooooooomoooooooooooooooooooooon
:“HpOq
and as usual we can express HpOq a sum over T -orbits on Gxz{Gxyz , that is to say, as a
sum ofT orbitsO1 ĂO:
(46) HpOq “
ÿ
O1
CoresT
Ty1 ResGxyz
Ty1 p... q
where we have chosen a representative y1 P O1 for each T -orbit O1 upon O; and the
injection Ty1 Ñ Gxyz that deﬁnes the restriction map is induced by an element of Gxz
conjugatingy1 toy.
We saw in Lemma 3.10 that the corestriction map vanishes unle ssy1 actually belongs
toX˚. (Indeed, writing Γ for the unique ℓ-Sylow of the abelian group T , then Γy1 is an
ℓ-Sylow ofTy1, and the corestriction map induced by Γy1 ÑTy1 is surjective on cohomol-
ogy.) In the case when y1 PX˚, we have Ty1 “T in which case O1 “ ty1u. We conclude
that
HpOq “
ÿ
y1POXX˚
ResGxyz
T ph1px,y q Yh2py,z qq
and ﬁnally adding up all O we get
ph1h2q1px,z q “
ÿ
yPX˚
ResGxyz
T ph1px,y q Yh2py,z qq
“
ÿ
yPX˚
ResGxy
T h1px,y q Y ResGyz
T h2py,z q “ h1
1h1
2px,z q.
This concludes the proof of the theorem.
4. I WAHORI -H ECKE ALGEBRA
In this section, we collect a few important facts about Iwaho ri–Hecke algebras. In
particular, we discuss the structure of the Iwahori–Hecke a lgebra at a Taylor–Wiles prime
(§4.2), the relation between modules over the (usual, i.e. n on-derived) Iwahori-Hecke
algebra and modules over the (usual) spherical Hecke algebr as (§4.4) and ﬁnally brieﬂy
discuss a localization result for the derived Iwahori-Heck e algebra (§4.6).
These results are presumably well-known to experts but they help us polish our presen-
tation of the Taylor-Wiles method – indeed similar ideas app ear in the paper of Khare and
Thorne [20].
DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS 2 7
4.1. We continue with the notation of the prior section (§3.2 ). In particular, Gv is the
Fv-points of a reductive split group.
In this section, we will also make use of the afﬁne Weyl group ˜W attached to G; by
deﬁnition this is the semidirect product X˚ ⋊W whereX˚ is the cocharacter group of the
maximal torus A, andW is the Weyl group of A.
LetS be the ring Z{ℓr, for a prime ℓ; this will be the coefﬁcient ring for all our Hecke
algebras and derived Hecke algebras. We suppose thatqv ” 1 moduloℓr and thatℓ doesn’t
divide the order of the Weyl group.
Let Iv be an Iwahori subgroup of Gv contained inside Kv and in good position with
reference to A. By this we mean that Iv stabilizes a chamber of the building that lies
inside the apartment deﬁned by A. An explicit choice of such an Iv can be obtained from
an integral model B of a Borel subgroup containing A:
Iv “ preimage of BpFvq inside GpOvq,
and the other such Ivs areW -conjugate to this one.
It will be helpful to keep in mind that the index rKv : Ivs ” | W | moduloℓr, in par-
ticular, this index is invertible in S. Take the Haar measure on Gv which assigns Iv mass
1.
4.2. The structure of the Iwahori algebra. Let HI be the Hecke algebra for Iv. We will
understand this to be deﬁned as
HI :“ HomSGv pSrGv{Ivs,S rGv{Ivsq.
This is identiﬁed with the set of S-valued and ﬁnitely supported functions f onIvzGv{Iv.
Namely, identifying such functions with measures (multipl ying by the Haar measure on
Gv, thought of as valued inS), each such functionf acts by right convolution onSrGv{Ivs,
and therefore deﬁnes an element of HI . Therefore, in the text, we will often produce
elements of HI by describing the associated bi-invariant function.
W arning:the resulting identiﬁcation
(47) HI » pfunctions onIvzGv{Ivq
is an anti-isomorphism of algebras if we equip the right-han d side with the convolution
product. When we multiply elements of HI , we will always understand the multiplication
to be that of HI , not the multiplication induced from the right hand side of ( 47).
We similarly deﬁne
HK “ HomSGv pSrGv{Kvs,S rGv{Kvsq,
HIK “ HomSGv pSrGv{Kvs,S rGv{Ivsq,
HIK “ HomSGv pSrGv{Ivs,S rGv{Kvsq.
IfV is anyG-representation, the algebra HomSGv pSrGv{Kvs,S rGv{Kvsq acts on the
right on VKv “ HomGv pSrGv{Kvs,V q. Similarly, elements HIK induces endomor-
phismsVIv Ñ VKv . Indeed a useful mnemonic for the subscript “ IK ” is that, acting as
explained above, HIK goes fromI-invariants toK-invariants, and so on. Also HIK, HKI
are bimodules for HK and HI .
As before, each of these can be identiﬁed with a space of funct ions. Thus, for example,
HIK » functions onKvzGv{Iv,(48)
and similarly for HIK, HK. As before, these identiﬁcations arise from the right convo lu-
tion action of the functions on SrGv{Kvs orSrGv{Ivs.
28 AKSHA Y VENKA TESH
Note that, somewhat contrary to what the notation might sugg est, an element of HIK
considered as a function is leftKv-invariant and rightIv-invariant. Again, we will use these
identiﬁcations such as (48) without comment to produce elem ents inside the various Hecke
algebras. The same warning applies here: the identiﬁcation s do not preserve multiplication;
the order must be switched, just as (47) is an anti-automorph ism. To avoid confusion here,
our convention is that products are always to be understood i n the sense of the HI, HK ,
etc., and not via convolution of functions.
It is useful later to deﬁne
(49) eK “ 1Kv
measurepKvq.
Considered as an element of HI it is idempotent. When considered as an element of HIK ,
it carries the identity coset ofSrGv{Kvs to ř
kPK{IkIv PSrGv{Ivs, and when considered
as an element of HKI , carries the identity coset of SrGv{Ivs to 1
rKv :Iv seKv PSrGv{Kvs.
In particular, eK P HIK induces the co-restriction map VIv Ñ VKv , and eK P HKI
induces the mapVKv ÑVIv which is the natural inclusion divided by the index rKv :Ivs.
Becauseq is congruent to 1 moduloℓr, the structure of HI is very simple. It is isomor-
phic simply to the group algebra of the afﬁne Weyl group:
(50) HI »Sr ˜W s
An explicit anti-isomorphism sends the characteristic fun ction ofIvwIv to the element w,
forw P ˜W ; in particular eK is sent to 1
|W |
ř
wPWw, the sum over the usual Weyl group.
This follows from the standard presentation of the Iwahori- Hecke algebra (for a refer-
ence with complex coefﬁcients, see [12, Theorem 4.2]); the k ey point is that the relation
pTs ´qqpTs ` 1q simpliﬁes to T 2
s “ 1 whenq “ 1 in the coefﬁcients. Actually it is also
possible to verify HI is isomorphic to Sr ˜W s by using torus localization, although we omit
the details.
4.3. Central element and discriminant. Every element of SrX˚sW is central in Sr ˜W s.
Therefore, (50) yields a natural map (indeed an isomorphism ) fromZ :“SrX˚sW to the
center of HI .
Then HI, HK have structures ofZ-algebra and HIK, HKI have structure ofZ-module,
all of which are compatible in the obvious way.
For example, the ring homomorphism Z Ñ HK is given by z ÞÑ eKzeK “ eKz. In
fact this is a ring isomorphism, as follows easily from the explicit presentation. Then e.g .
HIK has two structures of Z-module, one via Z Ñ HI and one via Z Ñ HK , and the
“compatibility” is that these two structures coincide.
4.4. Iwahori Hecke algebra. The next statement asserts that the bimodules HKI, HIK
give equivalences of categories, at least over the open subs et of SpecpZq where the “ W -
covering” SpecSrX˚s Ñ SpecSrX˚sW is étale. 7
4.5. Lemma. Let m be a maximal ideal of Z over which the mapZ ÑSrX˚s is étale, and
writeZ 1 for the localization of Z at m.
Write H1
K “ HK bZZ 1 and deﬁne similarly H1
I, H1
IK, H1
KI . Then the bimodules H1
IK
and H1
KI induce inverse equivalences of categories between H1
K modules and H1
I modules.
This is probably well-known in characteristic zero at least .
7I am grateful to Peter Schneider for correcting an error. In a n earlier version of this paper, this Lemma was
formulated over a larger open subset of Spec Z, but one step in the proof was not correct in this greater generality.
DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS 2 9
Proof. (Sketch).
Let’s show, for example, that the natural map induced by mult iplication
(51) HIK bHK HKI Ñ HI
yields an isomorphism after localization at m. In what follows, we denote such localization
with a prime: SrX˚s1 “SrX˚s bZZ 1.
Note that HI is free of rankw as a right module overSrX˚s (clear from (50)) and, being
ﬁnite étale, SrX˚s1 is free as a right module over Z 1 of rankw.
So H1
I is free of rankw2 overZ 1. Similarly, H1
IK and H1
KI are free of rankw and H1
K is
locally free of rank 1 as a Z 1-module. The obstruction to (51) being an isomorphism then
given by the vanishing of a suitable determinant; it is enoug h, therefore, to show that (51)
is onto after reducing modulo the maximal ideal m1 ofZ 1.
We can extend the natural homomorphism Z 1 Ñ Z 1{m1 to a homomorphism χ :
SrX˚s1 Ñ k, with k an algebraically closed ﬁeld containing the ﬁnite ﬁeld Z 1{m1. Note
thatk has characteristicℓ, and that χ is not ﬁxed by any element of W .
Now a homomorphism fromX˚ Ñkˆ is the same as an unramiﬁed k-valued character
χ of the maximal torus Av; so we may identify χ to a character of Av. We form the
corresponding induced representation V “ Vχ. Its elements consist of locally constant
k-valued functions on Gv that transform according to χ on a Borel subgroup containing
Av. Now VIv is ak-vector space of rank w, andVKv is ak-vector space of rank 1, andZ
acts on these spaces via the character χ (as follows, e.g. from (53) below).
We now show that the natural maps
Hab bZk Ñ HompVa,V bq
are isomorphisms fora andb belonging to tI,K u; that implies the desired claim, that is to
say, that (51) is onto after reducing modulo m.
Because the two sides have the same rank it is enough to check s urjectivity. In fact,
it’s enough to show surjectivity in the case of HII and to show that all the other maps
are nonzero (because then, for example, the image for HIK would be a nonzero subspace
of HompVIv,V Kv q which is stable under HompVIv,V Iv q.) The other maps are clearly
nonzero: the element eK induces a nonzero map in each of the cases IK,KI,KK . So we
are reduced to seeing that
(52) HI։ HompVIv,V Iv q.
But there’s a standard basis for VIv indexed by the Weyl group: vw pw P W q, whose
restriction to K is the characteristic function of the Bruhat cell indexed by w. The group
algebra of W , inside HI , acts by permuting the elements vw. Also the element λ P X˚,
considered again inside HI , acts by
(53) λ ¨vw “ xwχ,λ yvw.
In other words, as a representation of ˜W , this is the representation induced from the generic
characterχ, and so clearly irreducible. The surjectivity of (52) follo ws. □
4.6. Localization for the derived Iwahori–Hecke algebra. It will later on be helpful to
make use of localization for the derived Iwahori–Hecke algebra.
We deﬁne the derived Iwahori Hecke algebra as per the recipe o f §2, i.e.
HI :“ Ext˚
SGv pSrGv{Ivs,S rGv{Ivsq.
30 AKSHA Y VENKA TESH
As before this is isomorphic to the algebra of functionsh that associate to px,y q P Gv{Iv ˆ
Gv{Iv a class hpx,y q P H ˚pGxy,S q, with the product as described in §2.3. In a similar
way, we get derived versions HIK, HKI of the bimodules HKI, HIK deﬁned earlier.
Now, we can consider “restriction to ˜W , ” i.e.
(54) h1 P HII Ý Ñh1
1 P functions ˜W ˆ ˜W ÑH ˚pT,S q
whereT is as in §3.2 and we identify w P ˜W withwI PGv{Iv; and
(55) h2 P HIK Ý Ñh1
2 P functions ˜W ˆX˚ ÑH ˚pT,S q
where here we identify x PX˚ with the associated coset xKv; and we used the fact that T
stabilizes pointwise both ˜W ¨Iv andX˚ ¨Kv to restrict cohomology classes to T . Finally
we have a similar map for HKI .
Note that the right-hand side of (54) has an algebra structur e, at least restricting to
functions supported on ﬁnitely many ˜W -orbits, by means of the formula H1H2px,y q “ř
zP ˜W H1px,z q Y H2pz,y q (where all of x,y,z all belong to ˜W ). This algebra acts on
the right-hand side of (55), by means of the same formula, but H2 now belongs to the
right-hand side of (55), and therefore y is now taken to belong to X˚.
4.7. Lemma. Under our current notation and assumptions, (see §3.2), the map (54) is
an algebra morphism. Similarly, the map (55) is compatible with the map (54) and the
product HII ˆ HIK Ñ HIK ; similarly for HKI .
Proof. We want to show that (where h1,h 2 P HII )
Resph1h2q “ h1
1h1
2,
where Res means to restrict all Gv{Iv arguments to ˜W and restrict cohomology classes to
T ; we also want similar statements for the HII -action on HKI and HIK .
By precisely the same argument as in §3.11, we are reduced to t he following claim:
Claim: Let y1 belong to either Gv{Kv or Gv{Iv. Let Γ be an ℓ-Sylow
ofAv XKv. Let Γy1 be the stabilizer of y1 in Γ . Then the corestriction
H ˚pΓy1,S q Ñ H ˚pΓ,S q vanishes, unless y1 P X˚ Ă Gv{Kv or y1 P
˜W ĂGv{Iv.
We repeat the reasoning of Lemma 3.10: let S be the algebraic double centralizer of Γy1.
As before, Γy1 Ă Γ gives S Ă A. Let S0 be the identity component of S. By Lemma 3.9,
the component group of S is prime-to-ℓ. Therefore, Γy1 lies inside S0. Let Γ ˚
y1 Ă S0pFvq˝
be anℓ-Sylow of the maximal compact subgroup. Thus Γy1 Ă Γ ˚
y1.
Choose a complement S1 Ă A to S0, i.e. a subtorus with the property that S0 ˆS1 Ñ A
is an isomorphism. Then Γ ˚
y1 Ă S0pFvq˝ is an ℓ-Sylow, and Γ Ă ApFvq˝ is an ℓ-Sylow.
Therefore
Γ “ Γ ˚
y1 ˆ Γ 1
where Γ 1 is theℓ-Sylow of S1pFvq˝.
If S1 were trivial, then S0 “ A. In that case y1 lies in the ﬁxed set of ApFvq˝. In the
case wherey1 PGv{Kv this was proved in §3.9. However, the proof of this assertion also
applies word for word to establish the same assertion in the c asey1 PGv{Iv.
The ﬁxed set of ApFvq˝ onGv{Kv isX˚, as before, and the ﬁxed set of ApFvq˝ on
Gv{Iv is precisely ˜WIv ĂGv{Iv.8
8Here is a proof of the latter claim: if gIv is ﬁxed, then gKv P X˚ Kv, and modifying g by an element
of ApFv q, we can suppose g P Kv. We are reduced to computing the ApFvq˝ -ﬁxed points on Kv{Iv, which
DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS 3 1
Otherwise, S1 is not trivial, the corestriction Γ ˚
y1 Ñ Γ vanishes as before, and so the
corestriction Γy1 Ñ Γ vanishes too. □
5. T HE TRIVIAL REPRESENTATION
In this section we give our ﬁrst piece of global evidence that the derived Hecke algebra
can account for the “degree spreading” of Hecke eigenclasse s.
5.1. Let D be a division algebra of dimension d2 over an imaginary quadratic ﬁeld F .
Let G be the algebraic group of elements of norm 1 insideD. Let Y pKq be the arithmetic
manifold (17) associated to G and a level structureK. We shall supposeK to be contained
in the stabilizer of some maximal order OD. Observe that dimY pKq “ d2 ´ 1.
In this section we study the derived Hecke action on “Hecke-t rivial part” (see Deﬁnition
2.9) of the cohomology of Y pKq.
Recall that the global derived Hecke algebra ˜T consists of all endomorphisms ofH ˚pZℓq
that are limits (§2.13) , under H ˚pZℓq » limÐ ÝH ˚pZ{ℓnq, of endomorphisms that lie in the
algebra generated by all Hv,Z{ℓn .
5.2. Theorem. F or all but ﬁnitely many primes ℓ, the action of ˜T onH ˚pY pKq, Zℓq pre-
serves the trivial summand H ˚pY pKq, Zℓqtriv, and:
(i) The trivial part of the cohomology H ˚pY pKq, Zℓqtriv is cyclic over ˜T, generated
by the trivial class;
(ii) The image ˜Ttriv of ˜T in End H ˚pY pKq, Zℓqtriv is graded commutative. Also
˜Ttriv b Qℓ coincides with Qℓ-algebra generated by H ˚pY pKq, Qqtriv acting on
itself by means of the cup product.
Note the signiﬁcance of the second part of the statement: ins ide the Qℓ-derived Hecke
algebra there is a natural “preferred” rational structure. Our general conjecture (Conjecture
8.8) says that this should be true in great generality and the preferred rational structure is
related to motivic cohomology. Certainly the situation tha t we discuss here is quite easy
compared to the general case, but nonetheless it has several points of interest.
We also note that the theorem is almost certainly false (in the form stated above) if F is
not totally imaginary, for reasons related to (a) of §1.6.
We will deduce the Theorem from the following:
5.3. Lemma. Notation as above, so that G is the algebraic group arising from a division
algebra over the imaginary quadratic ﬁeld F . F or all sufﬁciently large ℓ, the following
statement holds:
F or each integern there are inﬁnitely many places v of the ﬁeld F , with
qv ” 1 modulo ℓn and where the division algebra is locally split, such
that the pullback map of (29)
H ˚pGpFvq, Z{ℓq Ñ H ˚pY pKq, Z{ℓqtriv
is surjective.
Note that the map above really does take values in the Hecke-t rivial cohomology, by
Lemma 2.8.
amount to the torus ﬁxed points on a ﬂag variety over Fv – using Lemma 3.6 to avoid problems with small
residue ﬁeld, these ﬁxed points are precisely the wIv with w P W , as desired.
32 AKSHA Y VENKA TESH
Proof. (Summary) The proof of Lemma (5.3) occupies §5.5 – §5.11. Aft er some initial
setup, we give in §5.8 certain conditions (a), (b), (c), (d) w hich imply the Lemma; and then
after §5.8 we check these conditions can actually be satisﬁe d. □
First of all, let us explain why the Lemma implies the theorem :
5.4. Lemma (5.3) implies the theorem.
Proof. First of all, ˜T preservesH ˚pY pKq, Zℓqtriv. This follows by the argument described
around (37). Explicitly, ﬁxing any prime w, we may ﬁnd a prime-to- w usual Hecke op-
eratorT for which the trivial part of Zℓ-cohomology coincides with the generalized zero
eigenspace for T ´ degpT q. (This can be checked over C, since we are supposing the
primeℓ to be large enough. See e.g. discussion after (59)).
By avoiding a ﬁnite set of ℓ, we may clearly suppose that H ˚pY pKq, Zq has no ℓ-
torsion, and that ℓ ąd. Similarly, we suppose that
H ˚pY pKq, Zqtriv bZ Z{ℓ ÑH ˚pY pKq, Z{ℓqtriv
is an isomorphism: see §5.6 for an explanation.
By Lemma 3.7, the mapH ˚pGpFvq, Z{ℓnq Ñ H ˚pGpFvq, Z{ℓq is surjective ifqv ” 1
moduloℓn. It follows from this that the surjectivity assertion of Lem ma 5.3 continues to
hold with coefﬁcients modulo ℓn.
Now we can consider an element of H ˚pGpFvq, Z{ℓnq as an element of the derived
Hecke algebra for G atv (see the Remark of §2.10). So the assertion implies that the c up
product action of each h P H ˚pY pKq, Z{ℓnqtriv is contained in the action of the derived
Hecke algebra; by passage to the limit, the cup product actio n of H ˚pY pKq, Zℓqtriv on
itself is contained in the action of the derived Hecke algebr a.
LetBℓ be the image of cup product H ˚pY pKq, Zℓqtriv Ñ EndpH ˚pY pKq, Zℓqtrivq.
Let ˜Ttriv be the image of ˜T inside EndpH ˚pY pKq, Zℓqtrivq. It remains to show that these
are equal. This comes down to the fact that ˜Ttriv is contained in the commutant of Bℓ and
so cannot be larger than it. In more detail:
Let ˜TpV0q
triv be the subring of ˜Ttriv deﬁned by only using local derived Hecke algebras
Hq,Z{ℓn with ℓn dividing q ´ 1, i.e. the restricted variant of the global derived Hecke
algebra deﬁned after (36).
We have inclusions
(56) Bℓ Ă ˜TpV0q
triv Ă ˜Ttriv,
where the ﬁrst inclusion follows from the argument just give n. To conclude the proof,
we will show that these are both equalities. Note, ﬁrst of all , that each element of ˜TpV0q
triv
commutes, in the graded sense, with each element of ˜Ttriv. Indeed, if q ” 1 moduloℓn,
the global action of Hq,Z{ℓn is readily seen to commute with Hv,Z{ℓn forv ‰ q, and it
commutes in the case v “q because Hq,Z{ℓn is known to be graded commutative.
Choose nowh P ˜Ttriv. There is b PBℓ such thath.1 “b.1 (here 1 is the trivial class in
H 0). Then ph ´bq.1 “ 0. The same is true then for both the even and odd components of
ph ´bq. But, as we just saw, both components commute in the graded se nse, with ˜TpV0q
triv ,
as we just saw, so in fact both of these components kill all of H ˚
triv. Thus h ´b “ 0, so
h PBℓ, as required. □
5.5. Recollections. LetN be an integer. (We will shortly ﬁx it to be “large enough.”)
DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS 3 3
Let UN be the standard unitary group, the stabilizer of řN
i“1 |zi|2. There are natural
maps
(57) bi-invariant differential forms on UN
„ÑH ˚pUN, Cq Ý ÑH ˚pGLN pOF q, Cq
obtained by the natural identiﬁcation of GLN pCq-invariant differential forms onGLN pCq{UN
with bi-invariant differential forms on UN (and then Hodge theory). The notation is a lit-
tle confusing: H ˚pUN q above refers to the singular cohomology of UN as a topological
space, whereasH ˚pGLN pOF qq refers to the group cohomology of GLN pOF q.
Moreover, the algebra of invariant differential forms on UN is a free exterior algebra
with primitive generators Ω 1, Ω 3,..., Ω 2N ´1 in degree 1, 3, 5,..., 2N ´ 1; “primitive” is
taken with respect to the coproduct on cohomology, induced b y UN ˆ UN Ñ UN . An
explicit representative for Ωj can be taken as
(58) X1,...,X j P LiepUN q ÞÑ anti-symmetrization of tracepX1 ¨ ¨ ¨Xjq
The same symbols Ωi will also be used to denote the corresponding invariant diff erential
forms on GLN pCq{UN . For later use, note that these can be restricted to cohomolo gy
classes for SUN and also to invariant differential forms on SLN pCq{SUN ; these restric-
tions kill Ω 1.
There are natural inclusions UN ãÑ UN `1 and GLN pOF q ãÑ GLN `1pOF q. For
ﬁxed j and large enough N , these induce isomorphisms in Hjp´, Cq. Moreover, these
isomorphisms are compatible with increasing N . By passage to the inverse limit we get
H ˚pU8, CqÝ ÑH ˚pGL8pOF q, Cq
Here (e.g) GL8 means in fact limÝ ÑGLN .
Both sides here carry compatible coproducts; for the right h and-side we can take the
coproduct induced by “intertwining” map (see e.g. [32, Chap ter 2]) GL8 ˆGL8 Ñ GL8.
9
The corresponding Pontryagin product on homology will be de noted by ˚.
In what follows, we ﬁx N to be divisible by d2 and chosen so large that
- the inclusion GLN ãÑ GL8 induces an isomorphism of integral group homol-
ogy in degrees ď d2, both with entries in OF and with entries in any residue
ﬁeld. (This is possible because, by a theorem of van der Kalle n [34, p. 289], the
range of homological stability can be taken uniformly in the se cases; indeed, van
der Kallen’s bounds for stability involve only the Krull dim ension in the case of
commutative rings.)
We will denote the stabilization map
HipGLN pOF qq Ñ HipGL8pOF qq
bya ÞÑap8q and its inverse byb ÞÑbpN q. We will use this notation for any choice
of coefﬁcients, not merely Z.
9To see that the coproducts are compatible amounts to say that the group multiplication and the intertwining
map both induce the same homomorphism on the stable cohomolo gy of UN . This follows from the Eckmann-
Hilton argument, or more directly as follows: Embed two comm uting copies U paq
N ˆ U pbq
N Ñ U2N by the
intertwining map. The group multiplication U2N ˆ U2N Ñ U2N when restricted to U paq
N ˆ U pbq
N on the source
gives the intertwining map U paq
N ˆ U pbq
N Ñ U2N . This fact, together with stability of homology, shows that the
two coproducts are compatible, as claimed.
34 AKSHA Y VENKA TESH
- The map (57) induces an surjection in degrees ă d2. (That this is possible is a
consequence of Borel’s result [4, (7.5)] asserting that coh omology classes in suf-
ﬁciently low degree are representable by invariant differe ntial forms on the sym-
metric space; Borel’s result is for a semisimple group, but w e readily deduce the
claimed result by applying it to SLN .) We have written “surjection” instead of
isomorphism just because of the issue of working with GL rather than SL: the
differential form corresponding to Ω 1 dies under (57)).
In a similar way to (57), we have an isomorphisms
(59)
H ˚pSUd, Cq Ñ SLdpCq invariant diff. forms on SLdpCq{SUd
„ÑH ˚pY pKq, Cqtriv.
For the surjectivity of the ﬁnal map: if a differential form ω on Y pKq satisﬁes Tω “
degpT qω for even one Hecke operator T , then by an easy “maximum modulus” argument
it must be invariant, 10 i.e. represented by a GpF b Rq invariant form on the correspond-
ing symmetric space. In particular, the cohomology H ˚pY pKq, Cqtriv is a free exterior
algebra, generated in degrees 3, 5,..., 2d ´ 1.
Finally let us recall (Borel) that theK-theory of OF is, modulo torsion, one-dimensional
in each odd degree, and that (Quillen) for any ﬁnite ﬁeld F of size q, the even K-groups
vanish and the odd K2s`1pFq » Z{pqs ´ 1q.
5.6. The constraints on ℓ. We impose the following constraints on ℓ:
(i) The cohomology of Y pKq with coefﬁcients in ℓ is torsion-free.
(ii) ℓ doesn’t divide gcdvppqv ´ 1q ¨ ¨ ¨ pq2d´1
v ´ 1qq, where the gcd is taken over all
qv ěq0 for large enough q0. (This gcd stabilizes forq0 large enough.)
(iii) ℓ is relatively prime to the numerator and denominator of the r ational number
M P Q˚ deﬁned in (62).
(iv) the cohomology H ˚pY pKq, Z{ℓqtriv is a free-exterior algebra on generators in
degree 3,..., 2d ´ 1.
(v) ℓ ąd2
(vi) The cohomology of GL8pOF q is free of ℓ-torsion in degrees less than d2.
All these assertions are automatically true for ℓ big enough. This is obvious for (i),
(ii), (iii), (v) and follows from the standard stability res ults for (vi). We examine (iv): We
saw after (59) that H ˚pY pKq, Qqtriv is a free exterior algebra; ﬁx generators e3,e 5,...
that belong to H ˚pY pKq, Zq. The products of the ei are linearly independent over Q, so
their reductions are also linearly independent over Z{ℓ for large enough ℓ. It remains to
show that they span H ˚pY pKq, Z{ℓqtriv. But that is obvious by counting dimensions: if
we ﬁx a Hecke operator T , then for sufﬁciently large ℓ the generalized zero eigenspace of
T ´degpT q onH ˚pY pKq, Z{ℓq has the same dimension as the generalized zero eigenspace
ofT ´ degpT q onH ˚pY pKq, Cq.
This concludes the proof that all of (i) – (vi) above are autom atically valid for large
enoughℓ. It would be interesting to see what happens for “bad” ℓ.
5.7. Let N be a large integer, as chosen in §5.5. Fix an embedding
(60) ι : G ãÑ SLN
for some large N , by taking a sum of many copies of the representation that ari ses from
the division algebra acting on itself. Then (in suitable coo rdinates) we may suppose that
10This uses compactness of Y pKq; in the general case the answer is substantially more compli cated
DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS 3 5
the open compact subgroupK is carried into the standard maximal compact ś
v SLN pOvq
of SLN pAf q, and the arithmetic group GpF q XK is consequently carried into SLN pOF q.
The mapι gives rise to a map of symmetric spaces, i.e. a map
GpCq{SUd Ñ SLN pCq{SUN,
where we have chosen a maximal compact for GpCq, which is isomorphic to SUd, and
then we have chosen a hermitian form on CN whose stabilizer SUN contains ιpSUdq.
Thus we get an embedding of locally symmetric spaces, also de noted byι:
(61) ι :Y pKq Ñ SLN pOF qzSLN pCq{SUNlooooooooooooooomooooooooooooooon
»BpSLN pOF qq
.
We can further composeι with the inclusion of SLN pOF q to GLN pOF q to give a map
Y pKq Ñ BpGLN pOF qq
5.8. In this section, we will formulate four claims (a)–(d) t hat will imply Lemma 5.3. We
will verify the claims in the remainder of the section.
Let 3 ď i ď 2d ´ 1 be odd and let ai P KipOF q be chosen so that it generates
KipOF q modulo torsion. Let rais be the image of ai inside HipGL8pOF q, Zℓq; as per
our notation above, raispN q is its preimage under the isomorphism HipGLN pOF q, Zℓq Ñ
HipGL8pOF q, Zℓq.
We’ll show that (for any n) there are inﬁnitely many places v, splitting the division
algebra and withqv ” 1 moduloℓn, and classesξi PHipGLN pFvq, Z{ℓq with the property
that:
(a) The image of ai inKipFvq{ℓ is nonzero. Call its image bi PKipFvq{ℓ; therefore,
bi is a generator of KipFvq{ℓ.
(b) The pairing xξi, rbispN qy ‰ 0 where rbis is deﬁned similarly to rais: it is the associ-
ated homology class under KipFvq Ñ HipGL8pFvq, Z{ℓq, and correspondingly
we have rbispN q PHipGLN pFvq, Z{ℓq.
(c) xξ3Y¨ ¨ ¨Yξ2d´1, prb3s ˚ ¨ ¨ ¨ ˚ rb2d´1sqpN qy ‰ 0, where * is the Pontryagin product
on the homology of GL8pFvq.
(d) Let rY pKqs P Hd2´1pY pKq, Qq be the fundamental class of Y pKq. Then there
existsM P Q˚ such that the image ι˚rY pKqs P H˚pGLN pOF q, Qq satisﬁes:
(62) ι˚rY pKqs “ M ¨ pra3s ˚ ra5s ˚ ¨ ¨ ¨ ˚ ra2d´1sqpN q.
where on the right we have the Pontryagin product for GL8pOF q, and ι is as in
(61).
Let us ﬁrst see why (a) – (d) implies Lemma 5.3. Recall that we c hoseℓ to not divide the
numerator or denominator of M , and also that the cohomology of GL8pOF q and so also
GLN pOF q isℓ-torsion free in degrees ăd2; therefore, condition (d) implies an equality in
Zℓ-homology:
(63) ι˚rY pKqs “ p unitq ¨ pra3s ¨ ¨ ¨ ˚ ra2d´1sqpN q.
Letπ be the projection from GLN pOF q to GLN pFvq. Write Ξi “π˚ξi PH ˚pGLN pOF q, Z{ℓq
andηi “ι˚Ξi PH ˚pY pKq, Z{ℓq. We have then
xΞi, raispN qy “ xπ˚ξi, raispN qy “ xξi,π ˚raispN qy “ xξi, rbispN qy ‰ 0
36 AKSHA Y VENKA TESH
sinceπ˚rais “ rbis. Also, in a similar way,
(64) xΞ 3 Y ¨ ¨ ¨ Y Ξ 2d´1, pra3s ˚ ¨ ¨ ¨ ˚ ra2d´1sqpN qy
“ unit multiple of xξ3 Y ¨ ¨ ¨ Yξ2d´1, prb3s ˚ ¨ ¨ ¨ ˚ rb2d´1sqpN qy ‰ 0
because the Pontryagin products and the stabilization maps are compatible with π˚. From
this and (63) we get
xη3 Y ¨ ¨ ¨ Yη2d´1, rY pKqsy “ x Ξ 3 Y ¨ ¨ ¨ Y Ξ 2d´1,ι ˚rY pKqsy ‰ 0.
But the Hecke-trivial cohomology of Y pKq moduloℓ is a free exterior algebra on gen-
erators in degrees 3,..., p2d ´ 1q. Fix such generators – call them ν3,ν 5,... . Each ηi is
also an element of this Hecke-trivial cohomology by Lemma 2. 8. It follows that
ηi “ unit ¨νi ` p product ofνjs withj ăiq
because otherwise the cup product η3 Y ¨ ¨ ¨ Yη2d´1 would be trivial. We conclude that, in
fact, the map
(65) H ˚pGpFvq, Z{ℓq Ñ H ˚pY pKq, Z{ℓqtriv
is onto as required. Therefore, to prove Lemma 5.3 it is sufﬁcient to prove (a)–(d) above.
5.9. V eriﬁcation of (d) from §5.8. Since we are supposing (57) to be a surjection in
degrees up to d2, it’s enough to verify that there is a nonzero M P C such that
(66) xι˚rY pKqs,ω y “ M xpra3s ˚ ¨ ¨ ¨ ˚ ra2d´1sqpN q,ω y
wheneverω is an invariant differential form on GLN pCq. We compute in the case (see
(58) for the deﬁnition):
ω “ ΩJ “ Ωj1 ^ ¨ ¨ ¨ ^ Ωjt
whereJ “ tj1,...,j tu, and show that both sides are nonzero if and only ifJ “ t3, 5,..., 2d´
1u. That is enough to prove (66).
The right hand side of (66) equals
(67) xra3s ˚ ¨ ¨ ¨ ˚ ra2d´1s,ω p8qy “ xra3s b ¨ ¨ ¨ b ra2d´1s, coproductpωp8qqy,
where we allow ourselves to write ωp8q P H ˚pGL8pOF q, Cq for the stabilization of the
cohomology class corresponding to ω. Now coprodpωp8qq is the product of various terms
of the shape
pΩj1 b 1 b 1 b ¨ ¨ ¨ 1 ` 1 b Ωj1 b 1 b ¨ ¨ ¨ b 1 ` ¨ ¨ ¨ qp8q
and from this we see (just for degree reasons) that the term on the right of (67) vanishes
if there is even one ji larger than 2d ´ 1 or one ji equal to 1. So J Ă t 3,..., 2d ´ 1u.
Again, for degree reasons, equality must hold. That shows th e right-hand side is zero
unlessJ “ t3, 5,..., 2d ´ 1u. When J “ t3, 5,..., 2d ´ 1u, the right-hand side becomes
xa3, Ω 3y ¨ xa5, Ω 5y... xa2d´1, Ω 2d´1y
and each factor xaj, Ωjy is nonzero: this is the nontriviality of the Borel regulator .
Now let us examine the left-hand side of (66), which equals xrY pKqs,ι ˚Ωj1 ^ ¨ ¨ ¨ ^
ι˚Ωjd y. It’s easy to see that ι˚Ω 1 vanishes. We also claim that ι˚Ωj must vanish for
j ą 2d ´ 1. Indeed we claim that ι˚Ωj, which deﬁnes an invariant form on Y pKq and
DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS 3 7
thus corresponds by (59) to an invariant differential form i n the cohomology of SUd, is
primitive as such. For that consider this diagram:
(68) invariant forms on SLN pCq{SUN /d47/d47
/d15/d15
invariant forms on GpCq{SUd
/d15/d15
SUN -invariant forms onisuN /d47/d47
/d15/d15
SUd-invariant forms onisud
/d15/d15
H ˚pSUN q /d47/d47H ˚pSUdq.
where the various maps of groups arise from the map ι of (60), and the top vertical maps
arise by restriction to the tangent space of the identity cos et. In other words, the element
ofH ˚pSUdq corresponding toι˚Ωj is just the pull-back of the element of H ˚pUN q corre-
sponding to Ωj under the group homomorphism
ϕ :SUd ÑUN
induced byι. In particular, ϕ˚Ωj is also primitive.
This shows that the left-hand side of (66) vanishes unless J “ t 3, 5,..., 2d ´ 1u. We
must still check that it is actually nonvanishing in this cas e. For this, we must show that
ι˚pΩ 3 ^ ¨ ¨ ¨ ^ Ω 2d´1q is nonvanishing, equivalently that
ϕ˚Ω 3 ^ ¨ ¨ ¨ ^ϕ˚Ω 2d´1
is a nonvanishing element of the cohomology of SUd. Since each ϕ˚Ωj is primitive it is
enough to see that they are all nonzero. The N -dimensional representation of SUd deﬁned
byϕ is isomorphic to the sum of many copies of the standard repres entation of SUd. Now
one can just compute explicitly with (58).
5.10. V eriﬁcation of (b) and (c) from §5.8. In words, what we have to do is produce
elementsθi P HipGL8pFvq, Z{ℓq for each odd 3 ď i ď 2d ´ 1; these θi should detect
(pair nontrivially with) a generator ofKipFvq, and the cup productθ3 Y ¨ ¨ ¨ Yθ2d´1 should
detect the Pontryagin product of the homology classes associated to those generators. Then
we may take ξi “θpN q
i PHipGLN pFvq, Z{ℓq.
Quillen shows a natural choice for θi: an equivariant Chern class derived from the
standard representation of GLN . In other words, write G “ GLN pFvq and write Γ for
the Galois group of Fv. The standard representation of GLN can be considered a G-
equivariant vector bundle on SpecpFvq, and thus we get a Chern class
c2i PH 2i
G,etpSpecFv, Z{ℓpiqq Ñ H 1
etpSpecFv, Z{ℓpiqq bH 2i´1pG, Z{ℓq
where on the left we have equivariant etale cohomology, and o n the right we have usual
etale cohomology; the arrow is explicated in [31, II.1.2, Le mma 1]. We may identify the
étale cohomlogy of Fv with the (continuous) group cohomology of Γ , and here Γ is acting
trivially on µℓ, and so H 1pSpec Fv, Z{ℓpiqq “ H 1pΓ, Z{ℓpiqq is identiﬁed with simply
µbi
ℓ . Fix a generator α forµℓ. Thus the image of c2i is of the form αi bθ2i´1, for some
θ2i´1 PH 2i´1pG, Z{ℓq. Similarly we can map c2i intoH 0pΓ, Z{ℓpiqq bH 2ipG, Z{ℓq; in
that way we get a class θ1
2i P H 2ipG, Z{ℓq so that the image of c2i isαi bθ1
2i. The class
c2i gives a morphism ( the “Soulé Chern class”)
(69) s :H2i´1pG, Z{ℓq Ñ H 1pΓ, Z{ℓpiqq
which sendsλ PH2i´1 to xθ2i´1,λ yαbi.
38 AKSHA Y VENKA TESH
These constructions are “stable” under increasing N – see [31, p. 257] – and so we
can consider θ2i´1,θ 1
2i as classes in H ˚pGL8pFvq, Z{ℓq, and the Soulé map as a map
H2i´1pGL8pFvq, Z{ℓq Ñ H 1pΓ, Z{ℓpiqq.
Now Soulé Chern class is known to be surjective when precompo sed with K2i´1 Ñ
H2i´1 ([31, Prop. 5, p 284]) (so long as i ăℓ – true by assumption on ℓ). This immediately
veriﬁes property (b), that is to say if we ﬁx a generator b2i´1 forK2i´1pFvq with associated
homology class rb2i´1s we have
0 ‰sprb2i´1sq “ xθ2i´1, rb2i´1syαbi
so xθ2i´1, rb2i´1sy ‰ 0 as desired.
To compute e.g. xθ3 Yθ5 Yθ7, rb3s ˚ rb5s ˚ rb7sy we rewrite it as
(70) “ xcoprodpθ3qcoprodpθ5qcoprodpθ7q,b 3 bb5 bb7y
Let us note that each rbis is primitive in homology – i.e. xrbis,α Yβy “ 0 ifα,β are
cohomology classes both in positive degree. This is because rbis comes from the image of
the Hurewicz mapπi ÑHi, so we can just pull back to the sphere Si and compute.
Quillen has shown [25, Proposition 2] (see also [25, Remark 2 , p.569]) that the coprod-
uct of (e.g.) θ7 equals
coprodpθ7q “ θ1
0lo omo on
1
bθ7 `θ1
2 bθ5 `θ1
4 bθ3 `θ1
6 bθ1 ` symmetric terms.
Thus, when we take the product coprodpθ3qcoprodpθ5qcoprodpθ7q, we get a sum of sev-
eral terms; because of the primitivity of rbis just noted, the only terms that contribute to
(70) will be those coming from
p1b1bθ3` 1bθ3b1` θ3b1b1qp1b1bθ5` 1bθ5b1` θ5b1b1qp1b1bθ7` 1bθ7b1` θ7b1b1q
and the only term of these with degree 3, 5, 7 in the ﬁrst, second and third factors is
θ3 bθ5 bθ7. Therefore,
xθ3 Yθ5 Yθ7, rb3s ˚ rb5s ˚ rb7sy “ x θ3 bθ5 bθ7, rb3s b rb5s b rb7sy
“
ź
xθ3, rb3syxθ5, rb5syxθ7, rb7sy ‰ 0
which gives (c) in the case d “ 4; the general case is the same.
5.11. V eriﬁcation of (a) from §5.8. Write O1 “ OF r1{ℓs. The Soulé maps from (69) ﬁt
in a commutative diagram
(71) K2i´1pO1q /d47/d47
/d15/d15
K2i´1pFvq
/d15/d15
H 1pΓ, Zℓpiqq /d47/d47H 1pGalpFv{Fvq, Zℓpiqq.
where Γ is now the Galois group of the maximal unramiﬁed extension of O1 ; note that
OF Ñ O1 induces an isomorphism on K2i´1 for i ą 1 (see [36, Theorem 4.6]). The
right-hand vertical arrow is an isomorphism for i ăℓ (Soulé, loc. cit. ) , and the left-hand
vertical arrow is a surjection (see [19]).
The map H 1pΓ, Zℓpiqq{ℓ ÑH 1pΓ, Fℓpiqq is an injection. Choose an element a2i´1 P
K2i´1pO1q whose image inH 1pΓ, Fℓpiqq is nonzero (note thatH 1pΓ, Zℓpiqq{ℓ is nonzero,
by computing Euler characteristic). A nontrivial class in H 1pΓ, Fℓpiqq is represented by a
nontrivial extension
(72) Fℓpiq Ñ M Ñ Fℓ,
DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS 3 9
in other words, by a homomorphism Γ Ñ GL2pZ{ℓq of the form
ˆ
ωi ρ
0 1
˙
Note that the image of this homomorphism must have size divis ible by ℓ; for otherwise
the extension (72) splits. By Chebotarev density, we may ﬁnd inﬁnitely many Frobenius
elements Frobv which map to ˆ
1 1
0 1
˙
which implies that the restriction of the extension class to H 1pFv, Fℓpiqq is nontrivial.
In other words, the image of a2i´1 inH 1pGalpFv{Fvq, Fℓpiqq, and so also in K2i´1{ℓ,
is nontrivial for ﬁnitely many v. This proves our assertion.
6. S ETUP FOR PATCHING
We continue in a global setting, but now turn to the study of te mpered cohomology.
This study will occupy most of the remainder of the paper (§6 – §8).
In the current section (§6) we will set up the various assumpt ions needed, and in the
next section (§7) we will use the relationship between the Ta ylor–Wiles method and the
derived Hecke algebra (outlined in §1.4) to prove our target theorem, Theorem 7.6: it says
the global derived Hecke algebra actually is big enough to be able to account for the degree
spread of cohomology.
In §8 we will explain how to index elements of the global deriv ed Hecke algebra by a
Selmer group, and use this to formulate our main Conjecture 8 .8.
A few apologies are in order:
‚ We switch notation slightly, working with modpn coefﬁcients rather than mod ℓn,
to better make contact with the standard presentations of Ga lois representations
and the Taylor-Wiles method.
‚ We have made no attempt to optimize the method for small prime s, and in par-
ticular make rather strong assumptions; in particular, we a ssume both that we are
in the “minimal case” of formally smooth local deformation r ings, and that the
Hecke ring at base level is isomorphic to Zp (no congruences).
6.1. Assumptions.
(1) Our general notations are as in §1.8, but we now specializ e to the case that the
number ﬁeld F is Q, and that G is a simply connected, semisimple Q-group. We
assume that G is split, and we ﬁx a Borel subgroup B and a maximal torus A
contained inside B.
(2) We ﬁx a level structure K0 Ă GpAf q, the “base level.” We write
Y p1q “ Y pK0q
for the arithmetic manifold ((17)) of level K0. We sometimes refer to this as the
“level 1” arithmetic manifold even though it is not literally so.
(3) Let Π be a tempered cohomological automorphic cuspidal represen tation for G,
factorizing as Π “ Π 8 b Πf over archimedean and ﬁnite places. We suppose that
ΠK0 ‰ 0, so that Π actually contributes to the cohomology of Y p1q.
(4) We write TK0 for the Hecke algebra at levelK0. It will be convenient to follow the
deﬁnition of [20] and deﬁne this in a derived sense: Consider the chain complex of
Y pK0q, with Zp coefﬁcients, as an object in the derived category of Zp-modules;
each (prime to the level, and to p) Hecke operator gives an endomorphism of
40 AKSHA Y VENKA TESH
this object. Deﬁne TK0 to be the Zp-algebra generated by such endomorphisms.
This has the advantage that TK0 acts on cohomology with coefﬁcients in any Zp-
module.
We may similarly form the Hecke algebra TK at a deeper levelK ĂK0; unless
speciﬁed, it will be generated only by Hecke operators at goo d primes for K.
(5) We shall suppose that the coefﬁcient ﬁeld of Π is Q, for simplicity – by this, we
mean that the eigenvalues of Hecke correspondences at all go od places for K0 lie
in Q, or equivalently the underlying representation Πv has a Q-rational structure
for all such v. Under this assumption, Π gives rise to a ring homomorphism
(73) TK0 Ñ Zp.
(6) Let T be the set of ramiﬁed places for Π , together with any places at which K0 is
not hyperspecial.
(7) Write
k “ Z{pZ
and ﬁx an algebraic closure k fork wherep ą 5 is a prime such that:
(a) H ˚pY pK0q, Zq isp-torsion free.
(b) p does not divide the order of the Weyl group of G, and also p RT , i.e. p is
not a bad place for Π orK.
(c) “No congruences between Π and other forms at level K0:”
Consider the composite homomorphism
(74) χ : TK0 Ñ Zp Ñk,
where the ﬁrst map is the action on Π , and the second map the obvious one.
Let m “ kerpχq be its kernel. We shall require that the induced map of
completions is an isomorphism:
(75) TK0,m
„Ý ÑZp
and moreover we shall assume the vanishing of homology after completion
at the maximal ideal m:
(76) HjpY p1q, Zpqm “ 0,j R rq, q `δs.
Observe that in favorable situations (75) implies (76), and both should be
true for all large enough p – see the Remark below for a further discussion.
Informally, (75) and (76) enforce that there are no congruen ces, modulo p,
between Π and other cohomological forms at level K0.
Note that the deﬁnitions of χ, m make sense at any level. Thus we use the no-
tationχ, m sometimes for the corresponding notions for other level str uctures
Y pKq, whereK ĂK0.
(8) We put
S “T Y tpu,
the collection of all primes that we have to worry about.
Remark. We expect that 7(c) should be automatically valid for p sufﬁciently large; in
practice, for the purposes of this paper, it is not an onerous assumption (the minimal level
conditions, enforced in (e) of §6.2, is more restrictive).
We give a proof that 7(c) is valid for all large enough p, for G an inner form of SLn
such thatY pKq is compact. It is likely this can be generalized to other sett ings, with more
work. In what follows, denote by TK0 the Hecke algebra deﬁned as above, but with Z
coefﬁcients; this is easily seen to be ﬁnitely generated ove r Z. Firstly, the algebra TK0 b C
DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS 4 1
is semisimple, because it acts faithfully on H ˚pY pK0q, Cq and this action is semisimple
(there is an invariant metric on harmonic forms). Thus, for a ll large enough primes p,
TK0 is étale over Z and thus (75) must be valid. If the homology in (76) is nonvani shing,
then there exists an eigenclass for TK0 onHj whose associated character factors through
TK0,m; by (75), this character must coincide with the action of TK0 on Π . In other words,
the Hecke eigensystem associated to Π occurs in degree j. This eigensystem corresponds
to an automorphic representation Π 1 such that Π 1
v “ Πv for almost all v. By the strong
multiplicity one theorem for GLn, this implies that Π 1
8 is tempered cuspidal, and then it
has nonvanishing pg,K q cohomology only in degrees rq, q `δs.
That’s the basic setup; now for Galois representations.
6.2. Assumptions about Galois representations; the deformatio n ring Rρ. We will
make assumptions very close to [14, Conjecture 6.1]. We brie ﬂy summarize them and
refer the reader to [14] for full details:
LetK ĂK0 be a deeper level structure, TK be as above, and let TK Ñk be a character.
We require that there exist a Galois representation
GalpQ{Qq Ñ G_p¯kq
satisfying the usual unramiﬁed compatibility, see (a) belo w.
Moreover, for the speciﬁc character TK Ñ k as in (74), i.e. the map associated to
the ﬁxed automorphic representation Π , reduced modulo p, we require more precise state-
ments: Let m be the kernel of TK Ñk, and TK,m the completion of TK at m. We require
there to exist a Galois representation 11
˜ρ : GalpQ{Qq Ý ÑG_pTK,mq
with the following properties:
(a) (Unramiﬁed compatibility): Fix a representation τ of G_. For all primes q not
dividing the level of K, the representation ρ is unramiﬁed at q, and the action of
tracepτ ˝ ˜ρqpFrobqq P TK,m coincides with the image of the (Satake)-associated
Hecke operatorTq,τ .
(b) Let ρ be the reduction modulo p of ˜ρ, so that
ρ : GalpQ{Qq Ñ G_pkq.
Thenρ has big image: when restricted to the Galois group of Qpζp8q, the image
ofρ contains the image of the k-points of the simply connected cover of G_.
(c) (V ague version: see [14, Conjecture 6.1] for precise for mulation): There is a rea-
sonable notion of “crystalline at p” representation into G_, and the representation
˜ρ is “crystalline at p.”
(d) (V ague version: see [14, Conjecture 6.1] and references therein for precise ver-
sion): The representation ˜ρ satisﬁes the expected local constraints (“local–global
compatibility”) when restricted to Qq; here q is a Taylor–Wiles prime (§6.3) that
divides the level of K. We also assume a natural version of local global compati-
bility at Iwahori level Y0pqq, formulated before Lemma 6.6.
(e) “‘All local deformation rings are all formally smooth:” we suppose that
H 0pQq, Adρq “ H 2pQq, Adρq “ 0 for allq PS “T Y tpu.
11Note that the assumption that there is a T-valued Galois representation, rather than a weaker notion such as
a determinant, is not reasonable unless one has a condition l ike “residual irreducibility.” In our case, however, we
are assuming that the residual representation ρ has very large image anyway – see (b) below.
42 AKSHA Y VENKA TESH
This means that the local deformation ring of ρ at primes q P T is isomorphic to
Zp, and the local deformation ring of ρ atq “ p is formally smooth. This keeps
our notation as light as possible. (We also use the formal smo othness to squeeze
the most out of the Taylor–Wiles method, but probably one can get something
without it.)
In particular, the natural map TK0,m Ñ Zp of (75) gives rise to a Galois representation
valued inG_pZpq, which we shall just call ρ:
(77) ρ : GalpQ{Qq Ý ÑG_pZpq,
which of course lifts the residual representation:
ρ : GalpQ{Qq Ý ÑG_pkq.
Let Rρ be the universal crystalline deformation ring of ρ, allowing ramiﬁcation only at the
setS. Good references for deformation rings are [13] or [15].
Let us now set up notations for Taylor–Wiles primes.
6.3. T aylor–Wiles primes and auxiliary level structures. A T aylor-Wiles primeof level
n is a primeq (we will also occasionally use the letter ℓ), not dividing the level ofK0, such
that:
- pn dividesq ´ 1, and
- ρpFrobqq is conjugate to a strongly regular element of T _pkq.
Here an element t PT _pkq is strongly regular if its centralizer inside G_ is equal to T _.
We are really interested in systems of such primes, and it is u seful to keep track of
the strongly regular element as part of the data. Fix once and for all a sufﬁciently large
integers. We will work with collections of such primes of cardinality s, which we call
Taylor–Wiles data:
- A T aylor-Wiles datumof leveln is a set of primesQn “ pq1,...,q sq together with
strongly regular elements pFrobT
q1,..., FrobT
qs q P T _pkq such that
- pn dividesqi ´ 1, and
- ρpFrobqi q is conjugate to FrobT
qi .
We will usually use q to denote a typical element of a Taylor–Wiles set of
primes, but occasionally we will also use the letter ℓ. Note that the set of possible
choices for each FrobT
qi has size |W |, the order of the Weyl group.
- Let r be the rank of the maximal torus A. Set
(78) R “rs, T _
s “ pT _qs, W s “Ws
thusT _
s is a torus and R is the rank of T _
s , andWs acts onT _
s .
- Level structures: If q RS is prime, we denote by
(79) Y0pqq Ñ Y p1q
the covering obtained by adding Iwahori level structure at q, i.e. we replace K0
by the preimage of a Borel subgroup under K0 Ñ GpFqq. Similarly, we get
Y1pqq by taking the preimage of a unipotent radical of a Borel subgr oup under
the same mapping. The covering Y1pqq Ñ Y0pqq is “Galois,” with Galois group
ApFqq » p Fˆ
q qr.
Suppose that pn dividesq ´ 1. In that case, deﬁne Y1pq,n q to be the unique
subcovering of Y1pqq Ñ Y0pqq such that the covering Y1pq,n q Ñ Y0pqq has
DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS 4 3
covering group pZ{pnqr. In summary:
(80)
ApFqq»pFˆ
q qr
hkkkkkkkkkkkkkkkikkkkkkkkkkkkkkkj
Y1pqq Ñ Y1pq,n q Ñ Y0pqqlooooooooomooooooooon
ApFqq{pn»pZ{pnqr
- For a Taylor–Wiles datum Qn of level n, we let Y ˚
1 pQnq be the ﬁber-product,
overY p1q, of all the coverings Y1pqi,n q Ñ Y p1q. Similarly we deﬁne Y0pQnq.
Therefore,Y ˚
1 pQnq Ñ Y0pQnq is Galois; we write
(81) Tn “ p Galois group of Y ˚
1 pQnq Ñ Y p1q q “
ź
qPQn
ApFqq{pn,
thus we have (non-canonically)
(82) Tn » pZ{pnqR.
As a shorthand we write
H˚pQn,S q :“H˚pY ˚
1 pQnq,S q
whereS is a ring of coefﬁcients.
6.4. Rings of diamond operators. We now set up the rings that are generated by “dia-
mond operators,” i.e. the deck transformation groups of our various coveringsY ˚
1 pQnq Ñ
Y0pQnq. Continuing with the notation of the prior section, put
(83) Sn “ Z{pnrTns, S 1
n “ ZprTns,
so these act on the Z{pn and Zp-valued chain complex of Y ˚
1 pQnq. Fixing, as in (82) , an
isomorphism ofTn with pZ{pnqR, we can identify this ring as follows.
(84) Sn » Z{pnrx1,...,x Rs{pp1 `xiqpn
´ 1q.
wherexi “ reis ´ 1,ei being a generator of the ith factor Z{pn under the isomorphism
(82). Recall R “rs as in (78).
Finally we form a “limit ring”
(85) S :“ Zprrx1,...,x Rss
The presentation (84) gives rise to obvious maps S։Sn and (compatible) augmenta-
tions of S andSn to Zp and Z{pn respectively, carrying all the xi variables to zero; we
denote by I andIn the corresponding kernels, so that S{I » Zp andSn{In » Z{pn. We
need the following easy Lemma:
Lemma. Let notations be as above. The natural map
(86) Ext˚
SnpZ{pn, Z{pnq Ñ Ext˚
S{pn pZ{pn, Z{pnq
(change of rings) is surjective. Also, the natural map
(87) Ext˚
S{pn pZ{pn, Z{pnq Ñ Ext˚
S pZp, Z{pnq
(change of ring, and functoriality of Ext in the ﬁrst argument) is an isomorphism.
Recall that the change of ring map ExtB Ñ ExtA induced by a ring map A Ñ B
can be realized by thinking of ExtB in terms of extensions of B-modules, and then just
regarding it as an extension of A-modules.
44 AKSHA Y VENKA TESH
Proof. For (86), it is sufﬁcient to check surjectivity on Ext1 because the right hand side
is generated by Ext0, Ext1: it can be computed to be an exterior algebra using a Koszul
resolution, see Lemma B.1. Now “morally speaking” this is be cause it is the pullback
on group H 1p´, Z{pnq induced by ZR
p Ñ p Z{pnqR, but this is not a real proof (at least
without discussing the relation between cohomology of proﬁ nite groups, and Exts over the
corresponding “completed” group algebra).
So we just compute both sides by using the compatible (under S{pn ÑSn) sequences
In ÑSn Ñ Z{pn and I{pn Ñ S{pn Ñ Z{pn; taking homomorphisms into Z{pn, we get
(88) Ext1
SnpZ{pn, Z{pnq » HomSnpIn, Z{pnq
`
» HompIn{I 2
n, Z{pnq
˘
and similar. (Note that the image of HomSnpSn, Z{pnq in HomSnpIn, Z{pnq is zero.)
So we need to check that the map
(89) I{pn ÑIn
induces an isomorphism when we take HomSp´, Z{pnq.
The homomorphisms HomSpIn, Z{pnq are precisely given by homomorphisms ϕ :
Tn Ñ Z{pn, namely, we send xi “ reis ´ 1 P In to ϕpeiq, using the notation after
(84). Since I{ppn, I2q is a free Z{pn module on x1,...,x R, it follows at once that (89)
induces an isomorphism as desired.
Now we discuss (87), which is not hard but we spell it out, main ly to be clear because
I ﬁnd change of rings confusing. Let π : P Ñ Zp be the Koszul resolution of Zp as an
S-module, and P “P {pn its reduction mod pn, so that π :P Ñ Z{pn is the Koszul res-
olution of Z{pn as an S{pn-module. There is an identiﬁcation Ext˚
S{pn pZ{pn, Z{pnq with
the cohomology of HompP, Z{pnq; it sends a closed element C P HompP, Z{pnrmsq to
the classα P Extm
S{pn pZ{pn, Z{pnq represented by the diagram Z{pn πÐ ÝP CÑ Z{pnrms
in the derived category of S{pn-modules (one can invert quasi-isomorphisms in the derived
category).
Consider now the diagram
(90) Z{pn P„
π/d111/d111 C /d47/d47 Z{pnrms
Zp
A
/d79/d79
P„
π/d111/d111/d111/d111
B
/d79/d79
where „ means quasi-isomorphism;A,B are the natural projections.
Now, the image α1 P ExtSpZp, Z{pnq ofα, under the map (87), is represented by the
map C ˝π´1 ˝A inside the derived category of S-modules, equivalently, by the com-
position C ˝ B ˝ π´1. In other words, the image α1 of α is represented by the class
C1 P HompP, Z{pnrmsq obtained by pulling back C P HompP, Z{pnrmsq viaP Ñ P .
That pullback induces an isomorphism of complexes
HomS{pn pP, Z{pnq » HomSpP, Z{pnq,
and thus, passing to cohomology, the desired isomorphism of Ext-groups. □
6.5. Adding level q structure: The relationship between homology at level Y p1q and
levelY0pqq. Fix a prime q that doesn’t divide the level of K0, satisfying q ” 1 modulo
pn. This section and the next two §6.5, §6.8, §6.11 all gather so me “standard” properties
of passing between level 1 and level q, working with Z{pn-cohomology. We remind the
reader that “level 1” does not literally mean level 1, but just the base level K0 at which we
work.
DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS 4 5
In the current section, we discuss the relationship between the homology of Y p1q and
Y0pqq; recall that Y0pqq was obtained by adding Iwahori level at q (see (79)).
We can use the discussion of §4.4: For S “ Z{pn, let HI, HK and so on be the (usual,
i.e. no “derived”!) Hecke algebras for pGq,Kqq, withS-coefﬁcients and let HIK, HKI be
the bimodules previously deﬁned in §4.2. There are natural m aps
(91) H ˚pY p1q,S q bHK HKI Ý ÑH ˚pY0pqq,S q,
H ˚pY0pqq,S q bHI HIK Ý ÑH ˚pY p1q,S q.
These maps are deﬁned by the “usual double coset formulas.” M ore formally, we may iden-
tify HK with HomSGq pSrGq{Kqs,S rGq{Kqsq, HKI with HomSGq pSrGq{Kqs,S rGq{Iqs)
and so forth; one may then proceed as in the discussion of §2.6 to deﬁne the maps of (91).
Before we go further, let us formulate a natural notion of “lo cal-global compatibility”
at level Y0pqq: the center of the Iwahori-Hecke algebra HI at level q, which is identiﬁed
(§4.3) with the Hecke algebra HK. We shall suppose:
(Local-global compatibility at levelY0pqq:) HK, identiﬁed with the center
of HI as just explained, acts on H˚pY0pqq,k qm by means of the same
(generalized) eigencharacter HK Ñk by which HK acts on Π .
It is feasible that this assumption could be avoided entirel y but since it is very likely to
be proven along with the other, more essential, local-globa l compatibility at Taylor-Wiles
primes it seems harmless to assume it.
6.6. Lemma. Let notation be as above, and assume the local-global compat ibility just
mentioned. Suppose that the prime q is such that ρpFrobqq is conjugate to a strongly
regular element of T _pkq. Then the maps (91) are isomorphisms when we localize at a
maximal ideal of HK induced by m. In particular , if q is part of a T aylor-Wiles datum of
leveln, then (91) induces
(92) H ˚pY0pqq, Z{pnqm
„Ð ÝH ˚pY p1q, Z{pnqm bHK HKI.
Proof. The assertion that (92) is an isomorphism follows from the as sertion that (91) is
an isomorphism by “localization at m” (taking a little care because the Hecke algebra for
Y0pqq andY p1q are not quite identically deﬁned, the former omitting the pr ime above q.
For a more detailed treatment of this point, please see [20, L emma 6.20]).
So it is enough to prove the ﬁrst assertion. Everything will b e with Z{pn coefﬁcients.
First note that the two natural ways of making a map
H ˚pY p1qq bHK HKI bHI HIK Ý ÑH ˚pY p1qq.
(i.e., ﬁrst contracting the ﬁrst two coordinates, or ﬁrst co ntracting the second two coordi-
nates) both coincide; similarly the other way around. We mak e the rest of the argument in
a more abstract setting.
Suppose R1,R 2 are two rings, and we are given an pR1,R 2q-bimodule M12 and an
pR2,R 1q-bimoduleM21, giving associated functors
F p´q “ ´ bR1M12, Gp´q “ ´ bR2M21
from (right)R1-modules to (right) R2-modules and vice versa, respectively.
We assume that F,G deﬁne an equivalence of categories, i.e. there are natural e quiva-
lences fromFG to the identity functor and from GF to the identity functor. (In our setting
aboveR1 “ H1
K,R 2 “ H1
I – the primes denote localization at the ideal of HK induced by
m – and the bimodules are H1
KI, H1
IK ; the assumptions are satisﬁed by Lemma 4.5.)
46 AKSHA Y VENKA TESH
Next letX be anR1-module, letY be anR2-module. (In our setting these are given by
the localized homology of Y p1q andY0pqq, respectively.) Suppose also we’re given maps
α :F pXq Ñ Y, β :GpY q Ñ X in such a way that the induced maps
(93) GpF pXqq
Gpαq
Ý ÑGpY q
β
Ý ÑX
(94) F pGpY qq
F pβq
Ý ÑF pXq αÝ ÑY
arise from the speciﬁed maps GF Ñ id andFG Ñ id.
Then the maps F pXq Ñ Y and GpY q Ñ X must be surjections (by inspection of
(93) and (94)); then in the diagram GpF pXqq Ñ GpY q Ñ X we have a composite of
surjections giving an isomorphism, so both are isomorphism s; in particular, GpY q Ñ X
andF pXq Ñ Y must be isomorphisms.
Applied to our original context, this concludes the proof of the ﬁrst assertion of the
Lemma. □
Note also that inside HI we have a copy of the monoid algebra krX `
˚ s, namely, the
action of “Uq-operators” IqχIq forχ PX `
˚ (see (38) for identiﬁcation of X˚ with a coset
space; X `
˚ is the positive cone corresponding to the Borel subgroup B). Each element
t PT _pkq deﬁnes a character χt :krX `
˚ s Ñ k of this monoid algebra: t corresponds (by
“Local Langlands”, easy in this split case) to an unramiﬁed c haracter ApQqq Ñ kˆ, i.e.
to a homomorphism X˚ Ñkˆ and then we just take the linear extension
(95) χt :krX `
˚ s Ñ k.
Using the previous Lemma, it is easy to compute the action of t his monoid algebra:
6.7. Corollary. Suppose that q is part of a T aylor-Wiles datum. Then the generalized
eigenvalues ofkrX `
˚ s acting onH ˚pY0pqq,k qm are all of the formχFrobT , where FrobT P
T _pkq is conjugate to the Frobenius at q, and the notation is deﬁned in (95).
The corollary asserts just the usual relationship between “ Tq eigenvalues at level 1 and
Uq eigenvalues at levelq.” We will omit the proof; it follows from the prior Lemma and a
straightforward computaiton.
Remark. LetH ˚pY0pqq, Z{pnqm,χFrobT be the summand ofH ˚pY0pqq, Z{pnqm correspond-
ing to theχFrobT -eigenspace ofkrX `
˚ s. For later use, we note that there is an isomorphism:
(96) H ˚pY0pqq, Z{pnqm,χFrobT –H ˚pY p1q, Z{pnqm
where the map from left to right is the pushforwardπ˚, and an inverse in the other direction
is given by the pullback π˚ together with projection to the χFrobT eigenspace.
To see these are inverses we compute in HI : with reference to the actions of (91), the
forward (pushforward) map corresponds to eK P HIK , and the reverse map corresponds
to |W |eKq P HKI whereq P SrX `
˚ s ãÑ HI is chosen to realize to the projection on the
χFrobT eigenspace, and eKq means the product of eK P HKI withq P HI . (See remarks
after (49)).
When we compose them we get |W |eKq P HI or |W |eKqeK P HK; to see, for ex-
ample, that the former acts as the identity endomorphism on H ˚pY0pqq, Z{pnqm,χFrobT ,
observe that it can be written as ř
wPWewq withew “IwI , and then we just use the fact
thatq annihilates all the krX `
˚ s-eigenspaces except the one indexed by FrobT , whereas
theew permutes the various eigenspaces.
DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS 4 7
6.8. Adding levelq structure continued: The homology at level Y1pq,n q. This section
together with the previous and subsequent ones – §6.5, §6.8, §6.11 – all gather some “stan-
dard” properties of passing between level 1 and levelq. So continue with q as in the prior
§, i.e., part of a Taylor–Wiles datum of level n.
We now consider the homology of Y1pq,n q – as deﬁned in (80) – and the action of its
Hecke algebra at levelY1pq,n q. Now this homology is basically glued from the homology
ofY0pqq: if we let F be the push-forward of the constant sheaf k fromY1pq,n q toY0pqq,
then F is a successive extension of copies of the constant sheaf k, in a Hecke equivariant
way.
We state some consequences of this more formally:
6.9. Lemma. Assume that q is part of a T aylor–Wiles datum of level n. Assume local-
global compatibility for Y0pqq, in the sense described after (91); let other assumptions
be as in §6.1. Let q,δ be as in (18). Then the homology HjpY1pq,n q, Zpqm vanishes for
j R rq, q `δs.
Proof. Clearly we can replace the role of Zp by Fp “ k, and then by the remark before
the proof, it is enough to prove the same for Y0pqq. By (92), it sufﬁces to prove the same
vanishing statement for Y p1q with Fp “k coefﬁcients. But this is part of our assumption
(7(a) from §6.1.) □
Now we want to say that this relationship between the homolog y ofY1pq,n q andY0pqq
is equivariant for Hecke operators at q. The full Hecke algebra is somewhat complicated
and we just deal with its “positive, commutative subalgebra .” Set ĂX˚ to be the quotient
of ApQqq by the subgroup pnApZqq. Denote by ∆ q the quotient of Qˆ
q by the subgroup
of Zˆ
q of index pn. Therefore ∆ q and ĂX˚ depend on n but we will suppress that from the
notation for simplicity. We may identify
ĂX˚ “X˚pAq b ∆ q,
and we think of ĂX˚ as a thickened version of the character lattice X˚pAq. From the
valuation ∆ q Ñ Z we get
(97) ĂX˚ ÑX˚
and we can deﬁne the “positive cone” ĂX˚
`
Ă ĂX˚ as the preimage of X `
˚ .
LetI be an Iwahori subgroup of GpQqq, andI 1⊳I the subgroup corresponding to the
coveringY1pq,n q, i.e. I{I 1 » p Z{pnqr. Then there is a natural map from Zpr rX `
˚ s to the
Iwahori-Hecke algebra at level I 1 sendingχ P ĂX˚ to the coset I 1χI 1. In particular, we get
an action of Zpr rX `
˚ s on the homology of Y1pq,n q.
6.10. Lemma. Any generalized eigenvalue ofkr rX `
˚ s acting onH˚pY1pq,n q,k qm is also a
generalized eigenvalue ofkr rX `
˚ s acting onH˚pY0pqq,k qm via the map kr rX `
˚ s Ñ krX `
˚ s
induced by (97).
Thus, by Corollary 6.7, we get a splitting
(98) H˚pY1pq,n q,k qm “
à
FrobT PT _ pkq
FrobT „ρpFrobqq
pH˚pY1pq,n q,k qqm,χFrobT
into the sum of generalized eigenspaces associated to the ch aractersχFrobT :kr rX `
˚ s Ñ k.
(In the subscript, „ means “is conjugate to.”) Again, this is nothing but a fancy w ay of
talking about the decomposition into “ Uq-eigenspaces.” The only point to note is that the
decomposition is canonically indexed by elements of T _pkq conjugate to the Frobenius.
48 AKSHA Y VENKA TESH
Proof. Write for short G “ GpQqq; let I be an Iwahori subgroup of G, and I 1⊳ I the
subgroup corresponding to the covering Y1pq,n q, i.e. I{I 1 » pZ{pnqr. We prove the same
statement in cohomology and without the m; the desired statement follows by dualizing
and localizing.
By the discussion of §2.6 we can identify
H ˚pY1pq,n q,k q » Ext˚
kGpkrG{I 1s,M q
H ˚pY0pqq,k q » Ext˚
kGpkrG{Is,M q
whereM is the direct limit of co-chain complexes of a family of cover ings, obtained by
adding more and more level structure at q.
Claim: We may ﬁlter krG{I 1s byG-submodulesF 0 ĂF 1 ĂF 2 Ă... such that:
(i) each successive quotient Fi`1{Fi is isomorphic as G-module to a sum of copies
ofkrG{Is,
(ii) For every χ P ĄX `
˚ , the action of I 1χI 1 preserves the ﬁltration, and the action on
the quotients coincides with the action of IχI .
Assuming the existence of this ﬁltration, the result follow s easily: we get long exact
sequences of the form
Extj
kGpFi´1,M q Ñ Extj
kGpFi,M q Ñ ExtjpkrG{Is,M q
Àe Ñ
and these are equivariant for the action of I 1χI 1, which acts by via IχI on the right-hand
summand. The result follows immediately by a descending ind uction.
To construct the desired ﬁltration regard krG{I 1s as the compact induction from I toG
of theI-representationkrI{I 1s, i.e
krGs bkrIskrI{I 1s
In particular, ∆ “I{I 1 acts byG-endomorphisms onkrG{I 1s, which is the action “by right
multiplication.” This action of δ P ∆ coincides with the action of I 1δI 1 and in particular
commutes with the action of kr rX `
˚ s.
Now we ﬁlter krG{I 1s by the kernelskrG{I 1sxmjy of successive powers mj of the max-
imal ideal m inkr∆ s. This ﬁltration is stable for kr rX `
˚ s because the actions of ∆ ,k r rX `
˚ s
commute. Also the jth term of the resulting ﬁltration is thus
Fj “krGs bkrIskr∆ sxmjy
and the jth graded is just krGs bkrIs
xmjy
xmj` 1y , i.e. a direct sum of copies of krG{Is, as
claimed.
It remains to check assertion (ii) in the Claim. For any y P mj´1, multiplication by y
gives a map
Fj{Fj´1 ÑF 1 “F 1{F 0
and a suitable sum of such maps is an isomorphism (as we see by c hecking the corre-
sponding assertion forkr∆ s). Since these multiplication maps commute with the action o f
kr rX `
˚ s we are reduced to computing the action of I 1χI 1 onF 1; nowF 1 is identiﬁed with
krG{Is is a natural way and the assertion is clear. □
6.11. Adding level q structure continued: Galois representations for level Y1pq,n q.
This section and the prior two §6.5, §6.8, §6.11 all gather so me “standard” properties of
passing between level 1 and level q. We now consider more closely the action of the
Iwahori-Hecke algebras at level Y1pq,n q and formulate local-global compatibility. First
let us look at the Galois side.
DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS 4 9
6.12. Lemma. Letq be a T aylor-Wiles prime of level n and assume that the unramiﬁed
representationρ|GQq has image inside T _. Then any deformation of ρ|GQq can be con-
jugated to one taking values in T _. In particular , any such deformation of ρ|GQq actually
factors throughGab
Qq » proﬁnite completion of Qˆ
q .
Proof. We may present the tame quotient of GQq as xF,t : FtF ´1 “ tqy, where t is a
generator of tame inertia.
Suppose thatA is an Artin local ring with maximal ideal m, and md “ 0. We are given
F,t inG_pAq that satisfy FtF ´1 “ tq, where t reduces to the identity in G_pkq andF
reduces to (after conjugating) a strongly regular element o fT _pkq. Conjugating, we may
suppose thatF belongs to the maximal torus T _pAq. We will prove by induction on d that
this forces t P T _pAq too. By the inductive hypothesis (obvious for d “ 1) the image of
t inG_pA{md´1q belongs to T _pA{md´1q. Write thus t “ t0δt wheret0 P T _pAq and
δt PG_pAq lies in the kernel of reduction modulo md´1.
Now in fact t0 lies in the kernel of reduction modulo m, and so t0 and δt actually
commute; indeed, t0 commutes with anything in the kernel of reduction modulo md´1.
Alsoδq´1
t “e. (To check these statements, just compute in the formal grou p ofG_ at the
identity.) Now,FtF ´1 “tq so that
F pt0δtqF ´1pt0δtq´1 “ pt0δtqq´1 PT _pAq
But the left hand side equals t0
`
AdpF qδt ¨δ´1
t
˘
t´1
0 , and so
AdpF qδt ¨δ´1
t PT _pAq
and sinceF is strongly regular this means that δt PT _pAq as desired. □
We now want to connect the Galois deformation ring relevant t o Y1pq,n q with the
Iwahori–Hecke algebra.
Letq be a Taylor–Wiles prime of level n. Suppose ﬁxed an element FrobT P T _pkq
conjugate to the Frobenius at q. Consider a deformation σ : GQ Ñ G_pRq ofρ, where
one allows now ramiﬁcation at q, and R is an Artin local ring with residue ﬁeld k. Then
we can uniquely conjugate σ so its restriction to to GQq factors as
Gab
Qq » yQˆq Ý ÑT _pRq,
and the image of a uniformizer in Qˆ
q reduces to FrobT . This map factors through (the
proﬁnite completion of) Qˆ
q {p1 `qZqq. Restricting to Fˆ
q we get
Fˆ
q ÑT _pRq
and pairing with characters of T _ we get Fˆ
q ˆX ˚pT _q Ñ R˚; by the duality of T _ and
A, this is the same thing as
(99) ApFqq Ñ R˚.
We emphasize that the map (99) depended on the choice of a toral element FrobT conjugate
to Frobenius; changing this element changes the map through the action of the Weyl group.
LetRuniv
SYtqu be Mazur’s universal deformation ring for ρ, allowing ramiﬁcation at q. By
our assumptions (§6.2) on the existence of Galois represent ations, there is a map
Runiv
SYtqu Ñ TK1pq,nq,m,
50 AKSHA Y VENKA TESH
where K1pq,n q is the level structure for Y1pq,n q. By means of this map, Runiv
SYtqu acts
onH ˚pY1pq,n q, Zpqm, and in particular on the summand H ˚pY1pq,n q, Zpqm,FrobT
q
under
(98). Thus, by (99), we get an action of ApFqq this cohomology group.
Now the assumption of local–global compatibility alluded t o in §6.2 is a strengthened
version of the following:
Local global compatibility: The action ApFqq ýH ˚pY1pq,n q, Zpqm,FrobT
q
just deﬁned coincides with the “geometric” action, i.e. whe rein ApFqq
acts by deck transformations on Y1pq,n q (see (80)).
By “strengthened version”, we mean that we require a similar assertion at a derived cate-
gory level, not just at the level of cohomology, and we also re quire the assertion for several
auxiliary primesq rather than a single one. For details, see [14, §13.5].
We say a deformation of ρ|GQq is of “inertial level ď n” if, when considered as a
representation of Qˆ
q by Lemma 6.12, and restricted to Fˆ
q , it factors through the quotient
Fˆ
q {pn. We denote by Runiv,ďn
SYtqu the quotient of Runiv
SYtqu that classiﬁes deformations of ρ
such thatρ|GQq has inertial level ďn. Explicitly,Runiv,ďn
SYtqu is the quotient of
(100) Runiv
SYtqu{xt ´ 1 : t is in the image of pnApFqq under (99)y.
Then local-global compatibility implies that the action of Runiv
SYtqu on the homology of
Y1pq,n q factors throughRuniv,ďn
SYtqu , according to our previous discussion.
7. P ATCHING AND THE DERIVED HECKE ALGEBRA
We continue with the notation and assumptions of the previou s section §6; see in par-
ticular §6.1 and §6.2. That section was primarily setup, and now we get down to proving
that the global derived Hecke algebra is “big enough,” in the sense discussed around (2).
The main result is Theorem 7.6.
We use the patching of the Taylor–Wiles method; more speciﬁc ally, we use the version
of that method that was discovered [9] by Calegari and Geragh ty, which applies to situa-
tions where the same Hecke eigensystem occurs in multiple de grees. We also use heavily
the presentation of the Calegari–Geraghty method given by K hare and Thorne [20].
7.1. Deformation rings and chain complexes at level Qn. Fix now a Taylor-Wiles da-
tumQn of leveln. (We will abusively use Qn both to denote the Taylor-Wiles datum and
simply the set of primes associated to that datum.)
Recall the deﬁnition of Y ˚
1 pQnq from §6.3: it is the ﬁber-product of coverings Y1pq,n q Ñ
Y p1q over q P Qn. We now collect together various results about the homology of
Y ˚
1 pQnq, which are essentially the same results as those already dis cussed for Y1pq,n q,
but using all the primes in Qn instead of just tqu.
7.2. Lemma. The homologyHjpY ˚
1 pQnq, Zpqm vanishes forj R rq, q `δs.
Proof. As in Lemma 6.9. □
Just as in (98), this homology group is split (by “ U -operators”) into summands indexed
by collections FrobT
q PT _pkq pq PQnq, where each FrobT
q is conjugate to the Frobenius
atq. In particular, since the Taylor–Wiles datum is equipped (§ 6.3) with a speciﬁc choice
of such a FrobT
q for eachq PQn, we can consider the summand
(101) H˚pY ˚
1 pQnq, Zpqm,FrobT
Qn
ĂH˚pY ˚
1 pQnq, Zpqm
indexed by these prescribed lifts.
DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS 5 1
Recall from (81) that Y ˚
1 pQnq Ñ Y0pQnq is Galois, with Galois group Tn. Let us
introduce notation for the deformation rings of interest to us: let
RQn “ universal deformation ring at level S šQn,
(102)
Rn “ quotient ofRQn classifying deformations of inertial level ďn at primes in Qn
For example, in the case when Qn “ tqu this was the ring Runiv,ďn
SYtqu discussed around
(100).
By the discussion of (99) and after, we get a morphismApFqi q{pn ÑRˆ
n , and therefore
we get (see (81)):
Tn ÑRˆ
n
What we know (local-global compatibility, assumed in §6.11 ) is that the natural action
of Tn (deck transformations) on homology of Y ˚
1 pQnq is compatible with its action via
Tn ÑRˆ
n . To say differently, we get a map
(103) Sn :“ Z{pnrTns Ñ Rn{pn,
and the natural action of Sn on the Z{pn homology ofY ˚
1 pQnq is compatible with that via
the map to Rn{pn.
Now consider the complex of singular chains
rCn “ ChainspY ˚
1 pQnq; Z{pnq
with Z{pn coefﬁcients. We think of it as a complex of Sn modules, because of the action
ofTn by deck transformations on Y ˚
1 pQnq. It is quasi-isomorphic to a bounded complex
of ﬁnite free Sn-modules and we have canonical identiﬁcations:
(104) H˚ rCn »H˚pY ˚
1 pQnq, Z{pnq
(105) H ˚HomSn p rCn, Z{pnq » H ˚pY0pQnq, Z{pnq
(106) H˚p ĂCn bSn Z{pnq » H˚pY0pQnq, Z{pnq.
Note that rCn is a free Sn-module, with basis given by the characteristic functions o f
an arbitrarily chosen set of representatives for Tn-orbits on singular simplices. Therefore,
the homology of HomSn p rCn, Z{pnq computes the homomorphisms from rCn to Z{pn in
the derived category of Sn-modules. By composition of homomorphisms in this derived
category, we get a map
(107) H ˚
´
HomSn p rCn, Z{pnq
¯
looooooooooooooomooooooooooooooon
»H˚ pY0pQnq,Z{pnq
ˆ Ext˚
Sn pZ{pn, Z{pnqlooooooooooomooooooooooon
»H˚ pTn,Z{pnq
ÑH ˚
´
HomSnp rCn, Z{pnq
¯
looooooooooooooomooooooooooooooon
»H˚ pY0pQnq,Z{pnq
With respect to the identiﬁcations noted underneath the res pective terms, this is precisely
the “natural” action of H ˚pTn, Z{pnq onH ˚pY0pQnq, Z{pnq. This natural action arises
thus: the covering Y ˚
1 pQnq Ñ Y0pQnq has covering group Tn, i.e. can be regarded as a
map
(108) Y0pQnq Ñ BTn
from Y0pQnq to the classifying space of Tn; this allows one to pull back cohomology
classes from Tn and take cup product. The coincidence of (107) and this “natu ral action”
is a general fact; for lack of a reference we sketch a proof in § B.4.
52 AKSHA Y VENKA TESH
It is possible to “cut down” rCn in a fashion that corresponds to the summand (101),
as is explained in [20] (see Lemma 2.12 thereof, and surround ing discussion). This can
be done compatibly for Y0pQnq andY ˚
1 pQnq and thus one gets a perfect complex Cn of
Sn-modules, equipped with identiﬁcations that are analogous to (104) and (105):
(109) H˚pCn; Z{pnq » H˚pY ˚
1 pQnq, Z{pnqm,FrobT,
(110) H ˚pHomSn pCn, Z{pnqq » H ˚pY0pQnq, Z{pnqm,FrobT
and again the action of Ext˚
SnpZ{pn, Z{pnq on the latter group corresponds to the natural
action by pulling back cohomology classes via (108). 12
7.3. Extracting the limit. Now we “pass to the limit” as per Taylor–Wiles and Calegari–
Geraghty. The idea is roughly speaking to extract, by a compa ctness argument, a subse-
quence of n along which the Cn,Sn,Rn are compatible, and then get limits C, S, R by
an inverse limit. Usually in modularity lifting one is only c oncerned with the limit of the
process; but in our case we also want to remember some facts ab out how this relates to the
Cn,Sn,Rn. A discussion of this process which emphasizes exactly what we need is given
in [14, §13], see in particular Theorem 13.1 therein.
We choose a sequence of Taylor-Wiles dataQn withn Ñ 8. After replacing the Qn by
a suitable subsequence and then reindexing – that is to say, r eplacingQi byQni for some
ni ąi, and then regarding Qni as a set of Taylor–Wiles primes of level i – we can arrange
that we can “pass to the limit.” After having done this, we obt ain at last the following data:
(a) A sequence of Taylor–Wiles data Qn of leveln.
Recall to this we have associated coverings Y ˚
1 pQnq Ñ Y0pQnq Ñ Y p1q, as
in §6.3, and the Galois group of the former map is called Tn; also (103) we set
Sn “ Z{pnrTns, the group algebra of Tn.
(b) With S “ Zprrx1,...,x Rss as in §6.4, a complex C of ﬁnite free S-modules,
equipped with a quasi-isomorphism
(111) C bSSn »Cn,
whereCn is as described in §7.1: a version of the chain complex of Y ˚
1 pQnq with
Z{pn coefﬁcients, but localized at m and FrobT .
(c) A quotient Rn ofRn, deﬁned as follows:
Recall from (102) the deﬁnition of Rn; a quotient of the crystalline deformation
ring at levelS šQn. We set
(112) Rn “Rn{ppn, mKpnqq
for a certain explicit function Kpnq, chosen so that e.g. action of Rn onH˚pCnq
automatically factors through Rn. We can and will assumeKpnq ě 2n. (The main
function ofKpnq is to make Rn Artinian, while still retaining enough information
about all of Rn for our purposes.)
12As a sanity check on this, note that the action of H ˚ pTn, Z{pnq on H ˚ pY0pQnq, Z{pnq indeed does
preserve the splitting into summands of the type (101); one c an see this directly by seeing that H ˚ pTn, Z{pnq,
considered inside the derived Iwahori-Hecke algebra, comm utes with the “positive subalgebra” used to deﬁne the
splitting (101).
DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS 5 3
(d) A “limit deformation ring” R » Zprrx1,...,x R´δss equipped with maps S Ñ R
and maps R Ñ Rn, R։ Rρ which are compatible, in the sense that this diagram
commutes:
(113) S /d47/d47
/d15/d15
R
/d15/d15
/d47/d47 Rρ
/d15/d15
Sn /d47/d47 Rn /d47/d47 Rρ{ppn, mKpnqq
(Recall here that Rρ is the deformation ring of ρ, with crystalline conditions
imposed, without adding any level, cf. §6.2).
Moreover, the composite S Ñ R Ñ Rρ factors through the augmentation S Ñ
Zp; and also the left-hand square induces an isomorphism
(114) R bSSn » Rn
(e) An action of R on H˚pCq, compatible with the S action, and with the maps
H˚pCq Ñ H˚pCnq, where R acts onH˚pCnq via R Ñ Rn.
(f) An identiﬁcation of
(115) H ˚pHomSpC, Zpqq „Ý ÑH ˚pY p1q, Zpqm,
compatible under (111) with the identiﬁcation H ˚pHomSn pCn, Z{pnqq » H ˚pY p1q, Z{pnqm
that is the composition of (110) with the pushforward. (This is described in dual
form in [14, Theorem 13.1(d)] but one gets similarly this res ult, and the statement
about compatibility is just a matter of looking at the deﬁnit ion of the map (115).
(g) (These last results use heavily the formal smoothness, a ssumption (e) from §6.2):
C has homology only in degree q, and its homology there HqpCq is free as R-
module. Moreover, one has an “ R “T result”
(116) R bS Zp » Rρ » image of TK0 in EndHqpY p1q, Zpqm.
7.4. The structure of S Ñ R. The limit process has given a map of rings S Ñ R, where S
and R are formal power series rings that represent, roughly speak ing, “limits” of the rings
Sn,Rn asn Ñ 8.
As in (77), the representation Π gives a liftρ to Zp of the residual representation ρ; this
corresponds to an augmentation Rρ Ñ Zp. Thus we also get an augmentation
f : R Ñ Zp,
and the pullback of this to S is the natural augmentation of S Ñ Zp ((d) of §7.3). In
particular, the kernel of f on S is precisely the ideal I.
Our assumptions imply that the map S Ñ R is surjective. Indeed, because S is complete
for the I-adic topology it is enough to verify that S{I Ñ R{IR is surjective. But R{I is a
Hecke ring by (116) and so isomorphic to Zp by (75). Note in particular that this also
means that IR is precisely the kernel of f .
The following easy lemma is now useful for explicit computat ions.
7.5. Lemma. W e can choose generatorsxi,yj for S, R, i.e.
S “ Zprrx1,...,x Rss, R “ Zprry1,...,y R´δss
such that thexi,yjs lie in the kernel of the compatible augmentations
S Ñ R Ñ Zp,
and the map S Ñ R is given by xi ÞÑyi fori ďR ´δ andxi ÞÑ 0 fori ąR ´δ.
54 AKSHA Y VENKA TESH
Proof. Write f : R Ñ Zp for the augmentation. Abstractly, R » Zprru1,...,u R´δss
where all the ui lie in the maximal ideal. Set yi “ui ´f puiq P kerpR Ñ Zpq. Then still
R » Zprry1,...,y R´δss. We have noted above that J :“ IR is precisely the kernel of the
augmentation R Ñ Zp; thus, the yi freely span as Zp-module the quotient J{J2.
Lift the yi to x1,...,x r P kerpS Ñ Zpq. Necessarily the xi span a saturated 13 Zp-
submodule of rank s inside I{I2 » Zs
p; they are Zp- independent because any linear re-
lation řaixi P I2 (with ai P Zp) would give rise to a corresponding linear relation in
R, a contradiction. Similarly, they are saturated because gi ven x1 and pa1...,a rq with
gcdpa1,...,a rq “ 1 andpx1 “ řaixi ` I2, we would get a corresponding relation in R,
again a contradiction.
Now extend the xi to a full Zp-basis xr`1,...,x s for I{I2. Each xj for j ą r is
sent under S Ñ R an element of J Ă R, which means that it can be written as a formal
polynomialPjpy1,...,y rq iny1,...,y r, with no constant term; so replacing xj byxj ´
Pjpx1,...,x rq we may suppose that xj ÞÑ 0 in R. □
Now we come to the main theorem of the section.
7.6. Theorem. Let assumptions be as in §6.1 and §6.2. The cohomology H ˚pY p1q, Zpqm
is generated, as a module over the strict global derived Hecke algebra (see §2.13 and §2.14
for deﬁnition with Zp coefﬁcients), by its minimal degree component H qpY p1q, Zpqm.
Proof. We use the setup of the Taylor–Wiles limit process (§7.3), be ginning with the fact
that the natural map
(117) H qpHomSpC, Zpqq b Extj
SpZp, Zpq։H q`jpHomSpC, Zpqq
is a surjection for all j: by (g) of §7.3 and Lemma 7.5, we can choose coordinates so
that S » Zprrx1,...,x Rss, and the complex C is quasi-isomorphic to a sum of copies of
S{pxR,...,x R´δ`1q concentrated in a single degree. So the surjectivity of (117 ) follows
from the “Koszul algebra” computations in §B of the Appendix .
Examine now the diagram, where all the maps are the obvious on es;
(118)
H qpHomSpC, Zpqq
“
/d15/d15
ˆ Exti
SpZp, Zpq
/d15/d15
/d47/d47 H q` ipHomSpC, Zpqq
V
/d15/d15
H qpHomSpC, Zpqq
V
/d15/d15
ˆ Exti
SpZp, Z{pnq /d47/d47 H q` ipHomSpC, Z{pnqq
“
/d15/d15
H qpHomSpC, Z{pnqq ˆ
`
Exti
SpZ{pn, Z{pnq
˘ /d47/d47
U
/d79/d79
H q` ipHomSpC, Z{pnqq
H qpHomSn pC bS Sn, Z{pnqq
f, „
/d79/d79
ˆ
`
Exti
Sn pZ{pn, Z{pnq
˘ Q /d47/d47
U 1
/d79/d79
H q` ipHomSnpC bS Sn, Z{pnqq.
„
/d79/d79
Here, the middle square “commutes” in the sense that the imag e of px,Uy q is the same
as the image of pVx,y q, i.e. U,V are adjoint for the pairing. The top and bottom squares
commute. All this is obvious, except for perhaps the bottom s quare which involves change
of rings, so let us talk through it: The map S Ñ Sn induces a forgetful map T from the
derived category ofSn-modules to the derived category of S-modules. Take
α PH qpHomSnpC bSSn, Z{pnqq, β P Exti
Sn pZ{pn, Z{pnq.
13Here we say that a submodule Q of a free Zp-module Q1 is saturated if the quotient Q1{Q is torsion-free.
DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS 5 5
We can regardα as a map C bSSn Ñ Z{pnrqs andβ as a map Z{pnrqs Ñ Z{pnrq `is,
both in the derived category ofSn-modules. Applying the functorT , we see thatTβ ¨Tα “
T pβαq. On the other hand, Tα is simply the morphism C bSSn Ñ Z{pnrqs considered
as a map of S-modules. If we pre-compose with γ : C Ñ C bSSn, considered as a map of
S-modules, we get f pαq. Similarly, T pβαqγ “f pβαq ¨γ. So Tβ.f pαq “ f pβαq: that is
the commutativity of the bottom square.
It follows from the Lemma of §6.4 that the composite U ˝U 1 is surjective. Also the
map V is surjective (because the cohomology of HomSpC, Zpq is torsion-free, by (115)
and assumption 7(a) of §6.1). Tracing through the above diag ram, this is enough to show
that the image of Q generates the codomain of Q.
Now, recall from (111) the quasi-isomorphism CbSSn »Cn; we have therefore shown
that H ˚pHomSnpCn, Z{pnqq is generated by H qpHomSn pCn, Z{pnqq as a module over
Ext˚
Sn pZ{pn, Z{pnq. As in the discussion after (107), this is equivalent to sayi ng that
H ˚pY0pQnq, Z{pnqm,FrobT is generated by its degree q component as a H ˚pTn, Z{pnq-
module, i.e.
(119) H qpY0pQnq, Z{pnqm,FrobT bH ˚pTn, Z{pnq։H ˚pY0pQnq, Z{pnqm,FrobT.
In what follows, let us write HI, HK for the tensor product of (derived) Iwahori-Hecke
algebras HI,q and derived Hecke algebra Hq overq PQn; and write HK, HKI, HIK, HI
for the (non-derived) algebras and bimodules of §6.5, but te nsoring over allq PQn. All of
these will be taken with Z{pn coefﬁcients.
Note that the action ofH ˚pTn, Z{pnq onH ˚pY0pQnq, Z{pnq factors through the action
of HI (e.g. see the Remark in §2.10). So H ˚pY0pQnq, Z{pnqm,FrobT is generated in
degree q over HI . Taking the sum over all possible lifts FrobT , as in (98), we see that
H ˚pY ˚
0 pQnq, Z{pnqm is also generated in degree q over the derived HI .
Now, each of the following maps are surjective:
H qpY p1q, Z{pnqm b HKI։H qpY0pQnq, Z{pnqm,
H qpY0pQnq, Z{pnqm b H j
I ։H q`jpY0pQnq, Z{pnqm,
H q`jpY0pQnq, Z{pnqm b HIK։H q`jpY p1q, Z{pnqm,
where the second statement is what we just proved, whereas th e ﬁrst and third statement
come from Lemma 6.6. Also there is a map
´
HKI b H j
I b HIK
¯
Ñ H j
K compatible
with the respective actions, just arising from composition of Exts. We get
H qpY p1q, Z{pnqm b H j
K։H q`jpY p1q, Z{pnqm.
Passing to the limit (as in the discussion of §2.13) conclude s the proof. □
8. T HE RECIPROCITY LAW
In §7 we proved, conditional under assumptions (§6.1, §6.2) on the existence of Galois
representations attached to modular forms and other assump tions that simplify the inte-
gral situation (§6.1), that the global derived Hecke algebr a is “big enough,” in the sense
discussed around (2).
We now turn to the question mentioned in §1.3: we index elements of this global derived
Hecke algebra by means of a certain dual Selmer group. This is achieved in Theorem 8.5.
This Theorem is not an end in itself; rather, it just gives the correct language for us to
formulate the central conjecture of the paper, Conjecture 8 .8.
56 AKSHA Y VENKA TESH
8.1. The coadjoint representations. We are interested in the co-adjoint representation,
i.e. the dual of the representation of G_ on its Lie algebra g_. Denoting by rg the Z-dual
to this Lie algebra, we obtain
Ad˚ :G_ ÑGLprgq
which we regard as a morphism of algebraic groups over Z. 14
In particular given a representation σ : GQ Ñ G_pRq we denote by Ad˚σ : GQ Ñ
GLpR bZ rgq the composition ofσ with the co-adjoint representation. When σ is valued in
Zp, we will write Ad˚σn for the reduction of Ad˚σ modulopn.
8.2. Galois cohomology. We will freely use the theory of Fontaine and Laffaille which
(in good circumstances) parameterizes crystalline repres entations of GalpQp{Qpq, even
with torsion coefﬁcients. For a summary, see §4 of [2].
Fix once and for all the interval r´p´3
2 , p´3
2 s Ă N of Hodge weights. We will say
that a representation of GalpQp{Qpq on a ﬁnitely generated Zp-module is “crystalline”
if it is isomorphic to a subquotient of a crystalline represe ntation with Hodge weights in
r´p´3
2 , p´3
2 s. This indexing of Hodge weights is useful for adjoint repres entations which
have weights symmetric around 0.
Recall that for any p-torsion crystallineM we can deﬁne
H 1
f pQp,M q Ă H 1pQp,M q
which classiﬁes those extensions M Ñ? Ñ 1 which are crystalline; it is in fact a submod-
ule and it is identiﬁed (by Fontaine-Laffaille theory) with a corresponding Ext-group in the
category of ﬁltered Dieudonné modules. In particular, this allows one to check that H 1
f is
isomorphic to the cokernel of the map
(120) F0DpM q 1´FrobÑ DpM q,
whereDpM q is the associated ﬁltered Dieudonné module. Also, the kerne l of 1 ´ Frob in
(120) is isomorphic to H 0pQp,M q. In particular, for M ﬁnite we have
(121) #H 1
f pQp,M q “ |DpM q|
|F 0DpM q| ¨ #H 0pQp,M q,
which can be effectively used to compute the size of H 1
f (note: the size of DpM q andM
coincide).
We will need to know that the subspaces H 1
f pQp,M q andH 1
f pQp,M ˚q (withM ˚ :“
HompM,µp8q are each other’s annihilators under the local duality pairi ngH 1pQp,M q ˆ
H 1pQp,M ˚q » Q{Z. This follows from the fact they annihilate each other (thei r product
would come from an Ext2 in the category of Fontaine–Laffaille modules, but the rele vant
Ext2 vanishes by [2, Lemma 4.4]) and a size computation using (121 ).
8.3. Selmer groups. Let QS be the largest extension of Q unramiﬁed outside S, and let
M be a module for the Galois group of QS{Q; thusM deﬁnes an étale sheaf on Zr 1
S s. We
write
H 1pZr 1
S s,M q Ą H 1
f pZr 1
S s,M q
for (respectively) the étale cohomology of M (equivalently the group cohomology of
GalpQS{Qq with coefﬁcients in M ), and the subset of this group consisting of classes
14Why the coadjoint representation rather than the adjoint? They are isomorphi c for G semisimple, at least
away from small characteristic. However, canonically what comes up for us is the coadjoint; for example, when
one works with tori, as in §9.1, the difference is important.
DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS 5 7
that are crystalline at p, i.e. classes whose image in H 1pQp,M q lies in the subgroup
H 1
f pQp,M q deﬁned above.
Note that we impose no local condition on classes in H 1
f pZr 1
S s,M q except for the crys-
talline condition at p.
We will writeH 1
f pQ,M q for the usual Bloch–Kato Selmer group: this is the subgroup
of classes in H 1pGalpQ{Qq,M q which are unramiﬁed away from p, and crystalline at p.
In general, we have an inclusion H 1
f pQ,M q Ă H 1
f pZr 1
S s,M q; the former is more restric-
tive, requiring that the cohomology class be unramiﬁed at pl aces ofS ´ tpu. However, in
our applications,M will be a module such that H 1pQv,M q vanishes forv PS ´ tpu, and
soH 1
f pQ,M q “ H 1
f pZr 1
S s,M q.
8.4. We will follow the notation of the previous section, des cribed in §6.1; in particu-
lar, we have an arithmetic manifold Y p1q “ Y pK0q, an automorphic representation Π ,
corresponding to a maximal ideal m of the Hecke algebra; and an associated Galois repre-
sentationρ :GQ ÑG_pZpq. We let S be the set of ramiﬁed primes for ρ orK0, together
withp.
Put
(122) V :“H 1
f pZr 1
S s, Ad˚ρp1qq_,
where we wrote ´_ for Homp´, Zpq. We will prove in Lemma 8.9 that both the H 1
f above
and V are (under our assumptions) free Zp-modules of rank δ.
We will produce an action of V onH ˚pY pKq, Zpqm. To explain it, ﬁx A a maximal
torus of G and let q be a Taylor–Wiles prime of level n, equipped with an element of
T _pkq conjugate to Frobenius at q. Let
Tq “ ApFqq{pn.
From this data we will construct:
- A natural embedding (§8.17) of
(123) ιq,n :H 1pTq, Z{pnq ãÑ
´
H p1q
q,Z{pn
¯
m
into the degree 1 component H p1q of the local, full level, derived Hecke algebra
Hq,Z{pn . (More precisely, we will use its completion at the maximal i deal m).
- A map
(124) fq,n :H 1pTq, Z{pnq Ñ V{pn,
We have already explained, in a special case, the construtio n offq,n in (16). We
brieﬂy outline the general case: Given α P H 1pTq, Z{pnq, we obtain, by (139),
an element α1 in the quotient of H 1pQq, Adρnq by unramiﬁed classes; now, we
associate toα the functional sendingβ PH 1
f pZr 1
S s, Ad˚ρp1qq to the local pairing
xα1,βqyq P Z{pn, whereβq is the restriction of β toH 1pQq, Ad˚ρp1qq.
Finally recall that under our assumptions (7(a) of §6.1) ,H ˚pY p1q, Zpqm is torsion-free;
its reduction modulo pn coincides withH ˚pY p1q, Z{pnqm.
8.5. Theorem. Let notation and assumptions be as established in §6 (in part icular §6.1,
§6.2). Let V be as in (122).
There exists a function a : Zě1 Ñ Zě1 and an action of V on H ˚pY p1q, Zpqm by
endomorphisms of degree `1 with the following property:
58 AKSHA Y VENKA TESH
(*) F or any n ě 1 and any prime q ” 1 modulo papnq, equipped with a strongly
regular element of T _pkq conjugate to ρpFrobqq, the two actions of H 1pTq, Z{pnq on
H ˚pY p1q, Z{pnqm coincide: one via fq,n and one via ιq,n.
The property (*) uniquely characterizes the V action (this is true for any function a).
In particular , the strict global derived Hecke algebra contains V, and so also the ex-
terior algebra freely generated by V (the induced map from ^˚V to endomorphisms of
H ˚pY p1q, Zpqm is injective).
Note that the uniqueness part of the statement is straightfo rward, because the con-
dition pins down the action of V{pr for arbitrarily large r: by Chebotarev, the images
fq,npH 1pTq, Z{pnqq generate V{pn even when restricted to primes q ” 1 modulopapnq;
this basically follows from the existence of Taylor–Wiles d ata (see in particular (142)).
Finally, under a further “multiplicity one” assumption, th is result is sufﬁcient to force
the whole derived Hecke algebra to be graded commutative. We separate this result from
the main analysis because it is inessential to our main goals and it requires this additional
multiplicity one assumption.
Before we state the proposition, we note that, by the argumen t of (37) together with [20,
Lemma 6.20], the action of global Hecke algebra ˜T on cohomology induces an action of ˜T
on onH ˚pY p1q, Zpqm.
8.6. Proposition. IfH qpY p1q, Zpqm “ Zp, then the image of the full global derived Hecke
algebra ˜T inside EndH ˚pY p1q, Zpqm in fact precisely coincides with the exterior algebra
generated by V, and in particular the global derived Hecke algebra (acting on m-part of
cohomology) is graded commutative.
This same conclusion of graded commutativity holds, more ge nerally, when there ex-
ists a semisimple Qp-algebra S of (degree-preserving) endomorphisms of H ˚pY p1q, Qpq
commuting with ˜T and such thatH qpY p1q, Zpqm b Qp has multiplicity one as a S-module.
Remark. - A natural choice for the commuting subalgebra S in Proposition 8.6 is the
Zp-algebra generated by the local underived Hecke algebras at all primes that are
not good. However, the multiplicity one condition is only re alistic when there is a
unique tempered representation π8 of GpRq with nontrivial pg, Kq-cohomology.
If this uniqueness condition is satisﬁed, then we would like ly expect the multiplic-
ity one condition to be valid in the great majority of cases.
Under the assumptions we are currently working (simply conn ected group, and
working over Q) only SL2n`1 has this property. However, this unicity of π8 in
fact applies whenever we work over a CM base ﬁeld, or for PGLn over Q. 15
The analysis of §6 – §8 would extend to those cases with only so me notational
changes.
- That we get an integral isomorphism of ˜T and ^˚V, in the ﬁrst statement of the
Proposition, is an artifact of our simplifying hypotheses. We don’t expect ˜T to be
an integral exterior algebra in general, but corresponding statements should remain
valid bQ.
In general, we would expect the ˜T to be T b ^˚V, where T is the usual Hecke
algebra, after tensoring with Q. But here our assumptions mean that T is just Zp,
and moreover that the conclusion is true integrally.
15Note that, for PGLn with n even, one should enlarge S using the action of the component group of the
archimedean maximal compact.
DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS 5 9
8.7. Formulation of the conjecture. We are now ready to state the conjecture, the for-
mulation of which is the main point of this paper. (Although t he trip was fun too.)
The formulation of the conjecture itself rests on the conjec ture of Langlands that as-
sociates to Π a motive, or more precisely a system of motives indexed by rep resentations
of the dual group. Unfortunately it is difﬁcult to ﬁnd a compr ehensive account of this
conjecture in print; the reader may consult the brief remark s in [21] or the appendix of
[24].
Continue with notation as in Theorem 8.5. As in the discussio n of §1.2 and §1.3, let
Mcoad be the motive with Q coefﬁcients associated to Π and the co-adjoint representation
of G_, if it exists. A priori , one may not always be able to descend the coefﬁcients of
Mcoad to Q, although we expect this is possible in most if not all cases. (See discussion in
[24, Appendix, A.3]). In what follows we assume that Mcoad can indeed be descended to
Q coefﬁcients; if not one can simply reformulate the conjectu re by replacing Q by a ﬁeld
extension.
Thus there is an identiﬁcation of Galois modules
étale realization of Mcoad » Ad˚ρ b Qp
and there is a regulator map from the motivic cohomology
H 1
motpQ,M coad,Zp1qq Ý ÑH 1
f pZr 1
S s, Ad˚ρp1qq b Qp.
As in §1.2.2, the motivic cohomology group on the left-hand s ide has been restricted to
classes that extend to an integral model. We assume that this regulator map is an isomor-
phism.16 Let VQp “ V b Qp, and let VQ be those classes in VQp whose pairing with
motivic cohomology lies in Q.
WriteH ˚pY p1q, ´qΠ for the Hecke eigenspace for the character TK0 Ñ Z associated
with Π (see (73)). Our assumptions imply that H ˚pY p1q, ZpqΠ “H ˚pY p1q, Zpqm.
8.8. Conjecture. Notation as above. With reference to the action
^˚VQp ýH ˚pY p1q, QpqΠ
furnished by Theorem 8.5, the action of VQ preservesH ˚pY p1q, QqΠ .
Some rather scant evidence is discussed in the next section ( §9). As we have mentioned
in the introduction, much more compelling is that we have bee n able to obtain numerical
evidence for a coherent analog of the conjecture, in a joint w ork with Michael Harris.
Recall (§6.2) we assume that
(125) H 0pQp, Adρq “ H 2pQp, Adρq “ 0
which implies the same conclusions for Ad˚ρp1q. In particular, H 1pQp, Ad˚ρp1qq is
torsion-free and surjects onto H 1pQp, Ad˚ρp1qq. Finally, H 1
f pQp, Ad˚ρp1qq is a satu-
rated submodule of H 1pQp, Ad˚ρp1qq and we have an equality of ranks
rankZpH 1
f pQp, Ad˚ρp1qq “ rankFpH 1
f pQp, Ad˚ρp1qq,
as follows from explicit computation. In particular,H 1
f pQp, Ad˚ρp1qq surjects ontoH 1
f pQp, Ad˚ρp1qq.
Also observe that, because of the assumed “big image” (§6.2 a ssumption (b)) ofρ, we have
(126) H 0pZr 1
S s, Ad˚ρp1qq “ 0,
16 In general, the appropriate conjecture is that the regulato r, taken to the group of classes that are crystalline
at p and unramiﬁed at all primes in S, is an isomorphism. However, by virtue of our assumptions in §6.2, part
(e), it is not necessary to explicitly impose “unramiﬁed at p rimes in S.”
60 AKSHA Y VENKA TESH
and soH 1pZr 1
S s, Ad˚ρp1qq is torsion-free.
8.9. Lemma. BothH 1
f pZr 1
S s, Ad˚ρp1qq and V are free Zp-modules of rank δ.
Proof. First of all, because the Taylor–Wiles method in this case im plies an R “T theo-
rem (see (116)) and we are assuming that the Hecke algebra is i somorphic to Zp (see (75))
we get from a tangent space computation that H 1
f pZr 1
S s, Adρq “ 0. We now apply Tate
global duality to this statement. It implies both the surjec tivity of
(127) H 1pZr 1
S s, Ad˚ρp1qq։ H 1pQp, Ad˚ρp1qq
H 1
f pQp, Ad˚ρp1qq,
and the injectivity of
(128) H 2pZr 1
S s, Ad˚ρp1qq ãÑ
ź
vPS
H 2pQv, Ad˚ρp1qq
loooooooooooomoooooooooooon
“0 by §6.2
so in fact H 2pZr 1
S s, Ad˚ρp1qq “ 0.
The surjectivity (127) holds also for Ad˚ρp1q, not just the mod p reduction. This fol-
lows because H 1pZr 1
S s, Ad˚ρp1qq surjects onto H 1pZr 1
S s, Ad˚ρp1qq, by (128); and the
induced map
H 1pQp, Ad˚ρp1qq
H 1
f pQp, Ad˚ρp1qq {p Ñ H 1pQp, Ad˚ρp1qq
H 1
f pQp, Ad˚ρp1qq
is an isomorphism.
The Euler characteristic formula, taken together with (126 ), (127) and (128), allows one
to compute
(129) dimH 1
f pZr 1
S s, Ad˚ρ p1qq “ δ.
Now examine the short exact sequences
(130) H 1pZr 1
S s, Ad˚ρp1qq
p /d47/d47
j
/d15/d15
H 1pZr 1
S s, Ad˚ρp1qq
/d15/d15
/d47/d47H 1pZr 1
S s, Ad˚ρp1qq
/d15/d15
H1pQp,Ad˚ ρp1qq
H1
f pQp,Ad˚ ρp1qq
p /d47/d47 H1pQp,Ad˚ ρp1qq
H1
f pQp,Ad˚ ρp1qq
/d47/d47 H1pQp,Ad˚ ρp1qq
H1pQp,Ad˚ ρp1qq
Since we have seen that j is onto, it follows that the induced maps of vertical kernels is a
short exact sequence; that and (129) imply that
H 1
f pZr 1
S s, Ad˚ρp1qq » Zδ
p,
as claimed. □
8.10. Cohomological vanishing in the T aylor–Wiles method. In the Taylor–Wiles method
we choose a set of primesQ such that, withSQ “SYQ, we have the following properties:
(a) Q is a Taylor–Wiles datum of some level, and
(b) The map H 1pZr 1
SQ s, Adρq Ñ H1pQp,Adρq
H1
f pQp,Adρq is surjective, and the mapH 2pZr 1
SQ s, Adρq Ñ
ś
vPQH 2pQp, Adρq is injective.
DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS 6 1
(Recall that our local assumptions at S mean there is no local cohomology there: §6.2,
assumption (e)).
Observe also that if Q is such a set of primes, and Q1 is a further set satisfying (a) and
(b), then certainly Q YQ1 satisﬁes (a) and (b) too. Indeed, the cohomological criteri a of
(b) are equivalent to asking that
(131) H 1
f pZr 1
SQ s, Ad˚ρ p1qq Ñ
ź
vPQ
H 1pQv, Ad˚ρp1qq
is injective, and this is stable under enlarging Q (it is equivalent to the same injectivity on
H 1
f pZr 1
S s, ´q, since anything in the kernel would be unramiﬁed at Q).
Now, if we choose a system of such data Qn of leveln, we can (by passing to a subse-
quence and reindexing, e.g. as in [14, §13.10]) achieve a new sequenceQn which satisfy
the “limit properties” of §7.3.
8.11. Deﬁnition. A sequence of T aylor–Wiles data Qn of leveln is called convergent if:
- Qn have the cohomological properties stated in (b) above and,
- One can pass to the limit in the sense of §7.3, i.e. there exist s data R, S, C,fn,gn
etc. satisfying all the properties enumerated in §7.3.
In particular, any sequence of Taylor–Wiles data has a conve rgent subsequence, after
reindexing the subsequence.
8.12. The tangent spaces to R andS. As in §7.4 both R and S are augmented to Zp:
S Ñ R Ñ Zp,
and the composite S Ñ Zp is the standard augmentation of S. The kernel of these aug-
mentations are denoted by J Ă R and I Ă S.
First of all, we set let tR be the “tangent space” to R over Zp, that is to say
tR » Hom˚pR, Zprεs{ε2q,
where the subscript ˚ means that the homomorphism lifts the natural augmentation R Ñ
Zp. Equivalently, R is the derivations of R{Zp into Zp, or the Zp-linear dual of J{J2.
We can make exactly the same deﬁnition for S. The surjection S։ R induces a surjec-
tion I{I2։ J{J2 and thus a natural injection tR Ñ tS with saturated image (i.e. split). We
write W for the cokernel of the map on tangent spaces, so we have an exa ct sequence
(132) tR ãÑ tS։ W.
Then W is a free Zp-module of rank δ.
8.13. T angent spaces toRn andSn. We suppose now thatQn are a convergent sequence
(§8.10) of Taylor–Wiles data.
Recall that S, R are deﬁned as “limits,” roughly speaking, of rings Sn Ñ Rn that occur
at levelQn in the Taylor–Wiles process. We recall that Rn is not the full (crystalline at p)
deformation ringRQn at levelQn, but is a “very deep” Artinian quotient of it.
These rings are also compatibly augmented over Z{pn, i.e.
Sn Ý ÑRn Ý ÑZ{pn
(see the bottom row of (113), and compose with the reduction o f the map Rρ Ñ Zp which
arises from our ﬁxed automorphic representation Π ).
8.14. Lemma. The mapRQn Ñ Rn induces an isomorphism upon applying Hom˚p´, Z{pnrεs{ε2q,
where Hom˚ means that the map lifts the natural augmentations to Z{pn.
62 AKSHA Y VENKA TESH
Proof. WriteA :“ Z{pnrεs{ε2. A map RQn ÑA gives rise to a deformation rρn :GQ Ñ
G_pZ{pnq that lifts the modulo pn reduction ofρ.
We want to show that RQn ÑA must factor through Rn. To do so we must show (see
(112)) that the map dies on the Kpnqth power of the maximal ideal mRQn , and also that
ρn automatically has inertial level ďn at primes in Qn (see page 50 for deﬁnition).
Note that the maximal ideal pp,ε q of Z{pnrεs{ε2 satisﬁes pp,ε qn`1 “ 0. SinceKpnq ě
n ` 1 by assumption, we only need verify that rρn has inertial level ďn at all Taylor–Wiles
primes. After suitably conjugating, we can suppose rρn|Qq to have image in T _ (see
Lemma 6.12). Restricted to inertia it takes image inside the kernel ofT _pZ{pnrεs{ε2q Ñ
T _pZ{pnq; this group has exponent pn, and so rρn has inertial conductor ďn. □
We also deﬁne
tRn “ Hom˚pRQn, Z{pnrεs{ε2q.
It doesn’t matter whether we useRQn or Rn in this deﬁnition, as we just showed. Similarly
we deﬁne
tSn “ Hom˚pSn, Z{pnrεs{ε2q.
There is a natural map tRn Ñ tSn induced bySn Ñ Rn.
Finally deﬁne
(133) Wn “ cokernel ptRn Ñ tSnq.
The maps R Ñ Rn and S Ñ Sn give rise to an isomorphism of short exact sequences
as below:
(134) 0 /d47/d47 tRn
/d47/d47
α,„
/d15/d15
tSn
β,„
/d15/d15
/d47/d47Wn
γ,„
/d15/d15
/d47/d47 0
0 /d47/d47 tR{pn /d47/d47 tS{pn /d47/d47 W{pn /d47/d47 0
This requires some explanation.
First of all, we explain the maps. Note ﬁrst of all that there i s a natural map tS{pn »
Hom˚pS, Z{pnrεs{ε2q, which is an isomorphism. Similarly for R. This means that there
are maps
(135) α : tSn Ñ tS{pn,β : tRn Ñ tR{pn
that are induced by the projections S ÑSn and R Ñ Rn. This explains α,β ; and the map
γ is the induced map on cokernels.
Next we see that α,β,γ are isomorphisms.
ForS this is the assertion that homomorphism S Ñ Z{pnrεs{ε2 factors through Sn.
Indeed, referring to the coordinate presentation (84) and ( 85), each element xi must go
to aε for some a P Z{pn, and then p1 `xiqpn
is carried to p1 `aεqpn
“ 1. For R,
we use the fact (114) that we can identify Rn with R bS Sn. As above, any homomor-
phism S Ñ Z{pnrεs{ε2 (lifting the augmentation) factors through Sn, and in particular
any homomorphism R Ñ Z{pn, lifting the natural one, factors through Rn.
Now, the bottom row is exact, by deﬁnition and the freeness of W. The top row is
exact at the left because the vertical maps α,β are isomorphisms, and exact at the right by
deﬁnition. Then it follows that γ is an isomorphism too.
This concludes the explanation of diagram (134).
DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS 6 3
8.15. T angent spaces toSn reinterpreted. Let us reinterpret the tangent space to Sn in
a few different (canonical) ways.
By (88) we have an isomorphism
(136) tSn » Ext1
Sn pZ{pn, Z{pnq
NowSn was, by deﬁnition (§6.4) , the Z{pn- group algebra of the group Tn; thus, from
the above equation, we get a canonical isomorphism
(137) tSn »H 1pTn, Z{pnq.
Next we connect tSn to Galois cohomology. Recall from Lemma 6.12 that, for any
q PQn, a deformation ofρ|Gq can be conjugated to lie in the torus, and in particular factors
through the proﬁnite completion of Qˆ
q . Now we can identify H 1pGq, Adρnq with the
set of lifts of ρn toG_pZ{pnrεs{ε2q, modulo conjugacy. This lift sends tame inertia to the
kernel of reduction modulo ε. In particular, having ﬁxed an element of T _pkq conjugate
toρpFrobqq, we get a canonical isomorphism
(138) H 1pQq, Adρnq
H 1urpQq, Adρnq » Hom
`
Fˆ
q, LiepT _q b Z{pn˘
Identifying the the Lie algebra with X˚pT _q, we get
(139)
H 1pQq, Adρnq
H 1urpQq, Adρnq » HompFˆ
q {pn, Z{pnq bX˚pT _q » HompX˚pAq b Fˆ
q {pn
looooooooomooooooooon
ApFq q{pn
, Z{pnq
(here the subscript “ur” means unramiﬁed) and thus, from (81 ) and (137)
(140) tSn »
à
qPQn
H 1pQq, Adρnq
H 1urpQq, Adρnq
where we emphasize that the isomorphism depends on the choic e of an element of T _pkq
conjugate to Frobenius at q, for each q PQn.
There is an isomorphism similar to (136) for tS; in particular, tS » Ext1
SpZp, Zpq and
more usefully
tS{pn » Ext1
SpZp, Z{pnq
The composite
(141) Ext1
Sn pZ{pn, Z{pnqÝ ÑExt1
SpZ{pn, Z{pnq Ñ Ext1
SpZp, Z{pnq.
gives the natural identiﬁcation – map β from (134) – of Ext1
Sn pZ{pn, Z{pnq “ tSn with
Ext1
SpZp, Z{pnq “ tS{pn.
8.16. Vn and Galois cohomology. We exhibit now a canonical surjection
(142) tSn։ V{pn
In fact, this surjection uses no more than the fact that Qn is a Taylor–Wiles datum. If we
suppose that Qn are a convergent sequence (§8.10) of Taylor–Wiles data, we w ill see that
this actually descends to an isomorphism
(143) Wn » V{pn,
i.e.Wn (deﬁned in (133)) is isomorphic to HompH 1
f pZr 1
S s, Ad˚ρ p1qq, Z{pnq.
64 AKSHA Y VENKA TESH
As before, let SQn be the union of the set S with the set Qn. Examine:
(144) Hom˚pRQn, Z{pnrεs{ε2q /d47/d47
„
/d15/d15
Hom˚pSn, Z{pnrεs{ε2q /d47/d47
„
/d15/d15
Wn
“
/d15/d15
H 1
f pZr 1
SQn
s, Adρnq
ϕ /d47/d47 ś
vPQn
H1pQv,Adρnq
H1urpQv,Adρnq
/d47/d47Wn.
The ﬁrst vertical map is just the computation of tangent spac es to deformation rings (work-
ing over Z{pn rather than a ﬁeld), the second vertical map is (140), and ϕ is restriction in
Galois cohomology.
There is now a natural pairing :
(145) H 1
f pZr 1
S s, Ad˚ρn p1qq ˆWn Ý ÑZ{pn
which, we emphasize again, depends on the choice of toral elements conjugate to Frobenius
at each prime in Qn. To be explicit, an element of Wn is represented by a collection
pβvq P
ź
vPQn
H 1pQv, Adρnq
H 1urpQv, Adρnq,
modulo imagepϕq; to pair α P H 1
f pZr 1
S s, Ad˚ρnp1qq with pβvqvPQn we take the sum of
local pairings
(146) pα, pβvqvPQn q ÞÑ
ÿ
pαv,βvqv
where the local pairing is deﬁned by restricting α to Qv and using local reciprocity. This
pairing (146) is well-deﬁned because each αv, i.e. the restriction of α to Qv, is actually
unramiﬁed. Moreover, if the collection pβvq come from a class in H 1
f pZr 1
SQn
s, Adρnq,
the value of (146) is zero by global reciprocity: our local as sumptions means that the local
pairings forv PS vanishes. Thus the pairing (146) descends to the quotient of ś
vPQnH 1
by imagepϕq. This concludes our discussion of (145).
We have also seen (§8.13, and similar arguments to Lemma 8.9) that both Wn and
H 1
f pZr 1
S s, Ad˚ρn p1qq are free Z{pn-modules of dimension δ. Let us check that (145) is
a perfect pairing of Z{pn modules, i.e. the map
Wn ÑH 1
f pZr 1
S s, Ad˚ρnp1qq_
is an isomorphism, where _ means homomorphisms to Z{pn. Since both sides have the
same size, it is enough to check that the map is surjective, an d thus enough to show that
the induced map
(147) tSn ÑH 1
f pZr 1
S s, Ad˚ρ p1qq_
is surjective, where _ now means homomorphisms to Z{p.
Now the Taylor-Wiles setQn is chosen (131) so thatH 1
f pZr 1
S s, Ad˚ρ p1qq ãÑ ś
vPQnH 1pQv, Ad˚ρp1qq.
The image of this map consists of classes unramiﬁed at Qn, so we also have
H 1
f pZr 1
S s, Ad˚ρ p1qq ãÑ
ź
vPQn
H 1pQv, Ad˚ρp1qqur
When we dualize this, and apply local duality at primes in Qn, we get the surjectivity of
(147).
DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS 6 5
8.17. The injection H 1pTqq ãÑ H p1q
q . In this section, we suppose that Qn is a Taylor–
Wiles datum of level n, but do not assume that it is part of a convergent sequence (§8 .10)
of Taylor–Wiles data. Let q P Qn, thus equipped with FrobT
q P T _pkq. We will work
exclusively with S “ Z{pn coefﬁcients. As before, Hq denotes the local derived Hecke
algebra atq, and H p1q
q denotes its degree 1 component. Let Tq “ ApFqq{pn.
We are going to describe the map (123), which is necessary for the formulation of the
Theorem. More precisely, we are going to describe a map
(148) θ :H 1pTqq Ñ
´
H p1q
q
¯
m
,
where the subscript means that we complete at the ideal of the Hecke algebra (i.e., the
degree zero component of Hq) corresponding to m.
The easiest way to think about θ is probably through the following property: for each
α PH 1pTqq, the action of θpαq onH ˚pY p1q, Z{pnqm is thus:
(149) Pullback to Y0pqq, project to FrobT
q -eigenspace, cup with α, pushdown to Y p1q.
where the projection is done with reference to the splitting of Corollary 6.7.
The formal deﬁnition of the map θ is given in (154), and the validity of (149) will follow
from the Lemma below.
The Satake isomorphism of §3 gives
Hq
„Ý Ñ pSrX˚s bH ˚pApFqqqqW
and in particular with Z{pn coefﬁcients the map H 1pTqq Ñ H 1pApFqqq is an isomor-
phism, so
H p1q
q
„Ý Ñ
`
SrX˚s bH 1pTqq
˘W
Now FrobT
q P T _pkq gives a map X˚pAq “ X ˚pT _q Ñ kˆ, i.e. it gives rise to a
character χFrobT
q
: SrX˚s Ñ k. The pullback of this to SrX˚sW deﬁnes the maximal
ideal m (using the Satake isomorphism). Let us denote by rm the extension of the ideal
m back to SrX˚s; we caution that it is no longer maximal, and rather it cuts ou t FrobT
q
together with all its W -conjugates. We have an identiﬁcation of completions
(150) SrX˚s rm –
à
wPW
SrX˚swχ,
where we have denoted by SrX˚swχ the completion of SrX˚s at the maximal ideal that is
the kernel of wχ.
Next the natural inclusion
(151) pSrX˚s bH ˚pTqqqW ãÑSrX˚s bH ˚pTqq
induces the ﬁrst map of
(152) pSrX˚s bH ˚pTqqqW
m
(151)
Ñ SrX˚s rm bH ˚pTqq
(150)
Ñ SrX˚sχ bH ˚pTqq.
The composite map of (152) is an isomorphism, and thus by comp osing with the Satake
isomorphism we get an isomorphism
(153)
´
H p1q
q
¯
m
„ÑSrX˚sχ bH 1pTqq.
We then deﬁne the map θ :H 1pTqq Ñ
´
H p1q
q
¯
m
by the rule
(154) θ :h PH 1pTqq ÞÑ 1 bh PSrX˚sχ bH 1pTqq
(153)´ 1
Ý Ñ
´
H p1q
q
¯
m
66 AKSHA Y VENKA TESH
where the superscript 1 refers to cohomological degree, and the ﬁnal map is the inver se of
(153). Note that this embedding depends on the choice of FrobT
q ; if we replace FrobT
q by
wFrobT
q then the embedding is modiﬁed by means of the natural action o fw onTq.
This concludes the description of the map H 1pTqq Ñ H p1q
q . We now want to justify
(149). For this we will describe an explicit preimage of θpαq under the map
(155) pHKI b HI b HIK q Ñ HK
in the case of the group GpQqq, where notation is as before (see, e.g. the proof of Theorem
7.6); note that HK coincides with what was previously called Hq. Observe that everything
here is a compatibly a module under the center of HII , which is identiﬁed (§4.3) with
SrX˚sW . In particular, it makes sense to complete at m.
Now let eλ P HII correspond to the characteristic function of IqλIq, where λ P X˚.
Thenλ ÞÑeλ deﬁnes an embedding SrX˚s Ñ HII , and, completing, an embedding
(156) SrX˚s rm Ñ pHII qm
As before (§4.2) we let eK be the characteristic function of Kq, divided by its measure;
if we write ew for the characteristic function of IqwIq, we have eK “ 1
|W |
ř
wPWew. It
can be considered, as in §4.2, as an element of HKI or HIK . Also |W |eKeλ P HKI (i.e.
the product of |W |eK P HKI witheλ P HII ) corresponds to the characteristic function of
IqλKq.
8.18. Lemma. Let Θ P SrX˚s rm be chosen so that it projects under (150) to the identity
inSrX˚sχ and to zero in all SrX˚swχ, forw PW not the identity. W e use the same letter
for its image Θ P pHII qm under (156).
F orh P H 1pTqq let xhy be the associated element of H p1q
I , i.e. xhy is supported on
the identity double coset of I, and the associated cohomology class is obtained from h by
means of the restriction isomorphism H 1pIq „ÑH 1pTqq.
Then the m-completion of (155) sends |W |eKΘ b xhy beK toθphq.
As above, the product eKΘ is understood as the product of eK P HKI with Θ P HII .
In words, this amounts precisely to the description (149) fo rθ, taking into account that Θ
realizes precisely the projection onto the FrobT
q component for the splitting (98).
Proof. Consider the map (no completions, at the moment)
(157)
´
HKI b H p1q
I b HIK
¯
Ñ H p1q
K Ñ
`
SrX˚s bH 1pTqq
˘W
We show it sends A :“eKeλ b xhy beK, forλ dominant, to the “ W -average” of λ bh,
i.e. |W |´1 ř
wPWw ¨ pλ bhq.
The claimed result will follow easily from this: Consider an element Θ 1 “ řcλλ P
SrX˚s with the property that cλ is nonzero only for λ dominant, and also Θ ” Θ 1 modulo
some high power of rm. Our claim implies that |W |eKΘ 1 b xhy beK is sent to the sum of
Weyl translates of řcλpλ bhq. The image of řcλpλ bhq in À
wPWSrX˚swχ bH 1pTqq
is very close to 1 bh in thew “ 1 factor, and very close to zero in the other factors; after
summing over W , its projection to the w “ 1 factor remains very close to 1 bh. Here
“very close” is taken in the topology of the complete local ri ngsSrX˚swχ. In other words,
θphq and the image of |W |eKΘ 1 b xhy beK under (155) and (153) are very close; in the
limit, this shows the desired result.
We will now consider everything in the “function model” of §2 .3. Let a1 P HKI,a 2 P
HIK be the images ofeKeλ,eK in the function model. Thena1 corresponds to the function
sending pxK,yI q to |W |´1 precisely when Iy ´1xK “ IλK , equivalently Kx ´1yI “
DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS 6 7
KλI, where we write λ P X˚ for the negative of λ. Also a2 corresponds to the function
pxI,yK q which is 1 exactly whenxK “yK . Moreover, the function xhy is supported on
the diagonal in G{I and sends pI,I q toh PH 1pTqq » H 1pIq.
The second map of (157) is given by restricting arguments to t he torus, and restricting
cohomology classes toTq. We can compute this restriction using the “localization” r esults
of §4.6; these results assert that restriction to the torus a ctually preserves multiplication.
We restrict to the torus. Suppose that µ P X˚ is dominant, with negative µ P X˚. We
compute:
ApK,µKq “
ÿ
yP ˜W
a1pK,yI qxhypyI,yI qa2pyI,µKq
The ﬁrst term is nonzero only for those y satisfyingKyI “KλI, i.e. y P ˜W XKλI. This
implies thaty “wλ, withw PW . So this equals
“ |W |´1 ÿ
wPW
xhypwλI,wλIqa2pwλI,µKq
The ﬁnal term is nonzero (and equals 1) exactly whenµK “wλK. Recall that both λ and
µ are dominant. Thus this only happens if λ “µ andw PWµ:
(158) ApK,µKq “ |W |´1δλµ
ÿ
wPWµ
xhypwλI,wλIq
On the right, xhypwλI,wλI q P H 1pTqq equalsw ¨h PH 1pTqq.
Now, the image of A under the derived Satake map is the W -invariant element of the
derived Hecke algebra of the torus deﬁned by
µ ÞÑ restriction toTq ofApµK,K q.
As we have just computed, for µ dominant,ApµK,K q “ ApK,µKq is nonvanishing only
whenµ “λ, where its value is |W |´1 ř
wPWµ wh. Therefore the image of A under (157)
is theW -average ofλ bh as claimed. □
8.19. Producing an action of V{pn on the cohomology at level 1. LetQn be a conver-
gent sequence of Taylor–Wiles data (§8.10). For each intege rn we will produce an action
of V{pn on automorphic cohomologyH ˚pY p1q, Z{pnqm. A priori these actions will not be
guaranteed to be compatible with one another; later we will s ee at least that they “converge
asn Ñ 8” to give an action of V onH ˚pY p1q, Zpqm.
More exactly, we begin by constructing an action of tSn, then prove (the Lemma below)
that it factors through Wn, and ﬁnally we have identiﬁed Wn » V{pn in (143). This gives
the desired action, and we will discuss the “convergence as n Ñ 8” in the next section.
Thus, letQn be a convergent sequence of Taylor–Wiles data.
We have
(159) tSn
(137)
– H 1pTn, Z{pnq
(148)
ãÑ degree 1 component of bqPQn pHqqm,
where the Hecke algebras are taken with Z{pn coefﬁcients. The composite embedding will
be denoted
(160) ιQn : tSn Ñ bqPQn pHqqm.
This gives rise to an action of tSn by degree `1 endomorphisms of automorphic coho-
mologyH ˚pY p1q, Z{pnqm, whose explicit description is essentially that already gi ven in
(149), just replacing the role of one prime by many.
68 AKSHA Y VENKA TESH
The embedding (137) and so also this action depends on the choice of elements FrobT
q P
T _pkq for each primeq PQn. Should we modify FrobT
q by an elementwq PW , the Weyl
group, the action of tSn is also modiﬁed (see comments after (154)) by the action of wq in
the obvious way.
8.20. Lemma. Let Qn be a convergent sequence of T aylor–Wiles data, as in Deﬁniti on
8.11. Then, for each n, the action of tSn onH ˚pY p1q, Z{pnqm (viaιQn ) is trivial on the
image of tRn, and thus factors through the map tSn ÑWn.
Proof. Consider the diagrams (118) of our previous story, now with i dentiﬁcations with tS
and tSn included:
(161)
H ˚pHomSpC, Zpqq
“
/d15/d15
ˆ
tShkkkkkkikkkkkkj
Ext1
SpZp, Zpq Q ˜v
/d15/d15
/d47/d47H ˚pHomSpC, Zpqq
/d15/d15
˜x PH ˚pHomSpC, Zpqq
V
/d15/d15
ˆ Ext1
SpZp, Z{pnq Q v /d47/d47H ˚pHomSpC, Z{pnqq
“
/d15/d15
x PH ˚pHomSpC, Z{pnqq ˆ
`
Ext1
SpZ{pn, Z{pnq
˘ /d47/d47
U
/d79/d79
H ˚pHomSpC, Z{pnqq
H ˚pHomSn pC bSSn, Z{pnqq
„
/d79/d79
ˆ
`
Ext1
SnpZ{pn, Z{pnq
˘
loooooooooooomoooooooooooon
tSn
/d47/d47
/d79/d79
H ˚pHomSn pC bSSn, Z{pnqq.
„
/d79/d79
In particular, letx PH ˚pHomSn pCbSSn, Z{pnqq be liftable to ˜x PH ˚pHomSpC, Zpqq;
letv P tSn » tS{pn be lifted to ˜v P tS. Then the image of px,v q in the bottom row is ob-
tained from projecting the image of p˜x, ˜vq at the top row.
Let us recall from §7.3 part (g) that C is quasi-isomorphic to R as an S-module in a
single degree. Thus we can explicitly compute what goes on in the top row. This explicit
computation (see Lemma B.1 in Appendix §B) shows that any ele ment ˜v P tS that lies in
the image of tR acts trivially onH ˚pHomSpC, Zpqq.
For later use, note that these explicit computations also sh ow that
(162) H ˚pHomSpC, Zpqq is free over ^˚tS{tR.
From (134) it then follows that imageptRn Ñ tSn q acts trivially on
H ˚pHomSn pC bSSn, Z{pnqq » H ˚pY0pQnq, Z{pnqm,FrobT,
where the action of tSn “H 1pTn, Z{pnq is by cup product, as in (119).
By (149) this means that the action of ιQn ptSnq on H ˚pY p1q, Z{pnqm is trivial on
imageptRn Ñ tSnq. Thus, this action of tSn onH ˚pY p1q, Z{pnqm factors throughWn as
claimed. □
8.21. Summary. Let us summarize more carefully what we have said to date:
For any Taylor–Wiles datum Qn we have an action of tSn “ HompTn, Z{pnq on
H ˚pY p1q, Z{pnqm constructed via an embedding
ιQn : HompTn, Z{pnq ãÑ derived Hecke algebra
DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS 6 9
(see (159)). On the other hand, we have a surjective morphism (see §8.16)
fQn : HompTn, Z{pnq։ V{pn.
These constructions, for a given n, depend only on Qn; they do not involve the Taylor–
Wiles limit process.
8.22. Deﬁnition. W e say that a T aylor–Wiles datum Qn of level n is strict of level n (or
just strict) if the map
tSn
ιQn
Ý ÑEndH ˚pY p1q, Z{pnqm
factors throughfQn . Thus, a strict T aylor-Wiles datum of leveln gives rise to an action of
V{pn onH ˚pY p1q, Z{pnqm.
What we have proved, then, amounts to the following:
8.23. Lemma. If theQn are a convergent sequence of T aylor–Wiles data (Deﬁnition 8 .11),
then eachQn is strict, in the sense of Deﬁnition 8.22.
Note we do not know that the resulting actions of V{pn are compatible for different n,
in any sense.
8.24. Dependence of our construction on choices. We now study dependence on choices.
Using the results of this §, we will conclude the proof of Theo rem 8.5 in §8.26.
First we discuss a minor point, the choice of FrobT
q s: Suppose we choose two different
such choices for a given set Qn, differing by the action of w PWs. (Recall from §6.3 that
Ws is just a product of copies of the Weyl group, one copy for each prime inQn). Then the
actions of tSn on cohomology differ by the action of w PWs (comment after (154)). Also,
w : tSn Ñ tSn is compatible with the pairings previously constructed, i. e. this diagram
commutes
(163) tSn
w
/d15/d15
ˆ H 1
f pZr 1
S s, Ad˚ρn p1qq
“
/d15/d15
FrobT
q /d47/d47 Z{pn
tSn ˆ H 1
f pZr 1
S s, Ad˚ρn p1qq
wFrobT
q /d47/d47 Z{pn
This shows that the action of V{pn onH ˚pY p1q, Z{pnqm did not depend on the choice of
FrobT
q s forq PQn.
We now discuss the more serious issue of choice of Taylor–Wil es data.
8.25. Lemma. Given two sequences Qn,Q 1
n of strict T aylor–Wiles data, there is a subse-
quence J of the integers with following property:
F or eachk ě 1, there is j0 such that, for each j P J,j ě j0, the two actions V
onH ˚pY p1q, Z{pkqm – arising from reducing modulo pk the “ Qj-action" and the “ Q1
j-
action" – coincide with one another . 17
Proof. It will be convenient to relabel the sequences of strict Taylor–Wiles data as Qp1q
n ,Q p2q
n .
It will be harmless to suppose that the sets of primes underly ingQp1q
n andQp2q
n are disjoint
(otherwise, we can e.g. just compare both of them with a third set, disjoint from both of
them).
17Recall that we are supposing that H ˚ pY p1q, Zpq is free over Zp.
70 AKSHA Y VENKA TESH
We will compare them both to Qn :“Qp1q
n
šQp2q
n (with the obvious choice of FrobT
q
for q P Qn). Of course Qn is bigger than either Qp1q
n or Qp2q
n . However it still a se-
quence of Taylor–Wiles data. Let Tn,T p1q
n ,T p2q
n be the analogues of Tn forQn,Q p1q
n ,Q p2q
n
respectively; then Tn “ T p1q
n ˆ T p2q
n , and correspondingly tSn “ tp1q
Sn ‘ tp2q
Sn , where
tSn “ HompTn, Z{pnq, etc.
We have a diagram
(164) tp1q
Sn
/d47/d47
αp1q
/d39/d39❖❖❖❖❖❖❖❖❖❖❖❖❖ tSn
α
/d15/d15
tp2q
Sn
αp2q
/d119/d119♦♦♦♦♦♦♦♦♦♦♦♦♦/d111/d111
H 1
f pZr 1
S s, Ad˚ρnp1qq_
where all the α-maps are as in §8.16.
The upper maps are compatible for the actions on cohomology p reviously deﬁned
(§8.19), and everything maps compatibly to the bottom group H 1
f pZr 1
S s, Ad˚ρnp1qq_.
Moreover the action of tp1q
Sn and tp2q
Sn on mod pn cohomology factors through the bottom
row by the assumed strictness. However, we do not know that th e action of tSn factors
throughα.
What is missing is control of the deformation ring after addi ng level Qn. To obtain
this, we must run now the Taylor–Wiles limit process for Qn. That involves passing to a
subsequence. In other words, all we are guaranteed is that th ere is a subsequence nj such
that pQnj,j q form a convergent sequence of Taylor–Wiles data of level j. It is possible that
nj is very much larger than j. Our prior analysis of convergent data (Lemma 8.23) implies
that the action of HompTnj, Z{pjq on modpj cohomology of Y p1q factors through V{pj,
or to say it explicitly:
(*) The action of tSnj onH ˚pY p1q, Z{pjqm, via its embedding ιQnj into
the derived Hecke algebra, followed by reduction to Z{pj coefﬁcients,
factors through the map
fQnj : tSnj ÑH 1
f pZr 1
S s, Ad˚ρjp1qq_.
The proof of the Lemma easily follows. We take J to be the subsequence of njs. Let
k be as in the Lemma. Take n “ nj, for any j ě k, and take wpiq P tpiq
Sn that have the
same image in H 1
f pZr 1
S s, Ad˚ρnp1qq_. The images of wpiq in tSn have the same image
in H 1
f pZr 1
S s, Ad˚ρjp1qq_, (we are using the fact that the map H 1pZr 1
S s, Adρnp1qq Ñ
H 1pZr 1
S s, Adρjp1qq is surjective, by discussion before (126)) and therefore th ey act the
same way on mod pk cohomology by (*) above. □
8.26. Conclusion of the proof of Theorem 8.5. Let us call a sequence of Taylor–Wiles
dataQn of leveln (where we do not require n to vary through all the integers, but possibly
some subsequence thereof) V-convergent if:
‚ EachQn is strict (Deﬁnition 8.22) thus giving an action of V onH ˚pY p1q, Z{pnqm.
‚ The actions converge to an action of of V on H ˚pY p1q, Zpqm. In other words,
if we ﬁx k, the action of V onH ˚pY p1q, Z{pkqm arising from reducing the Qn-
action is eventually constant.
By Lemma 8.23 and passing to a further subsequence, we see tha t V-convergent se-
quences exist. By Lemma 8.25, if Q,Q 1 are two V-convergent sequences, the resulting
DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS 7 1
actions of V on cohomology coincide. Thus at this point we have deﬁned an a ction of
V on cohomology that is independent of choices, namely, the ac tion arising from any V-
convergent sequence. This action has the following propert y:
p:q: For any sequence Qn of Taylor–Wiles data, there is a subsequence
Qnr such that (for everyr) the following two actions of tSnr onH ˚pY p1q, Z{prqm
coincide:
‚ The action viaι : tSnr Ñ derived Hecke algebra with Z{pr coefﬁcients
(see (160)).
‚ The action obtained from the V-action, via f : tSnr ։ V{pr (see
(142) ).
To see this, we ﬁrst pass from Qn to a convergent subsequence pQmr,r q, where we regard
Qmr as having levelr; by Lemma 8.23 this means that Qmr is a strict datum of levelr. We
then pass to a further subsequence m1
r to extract a V-convergent sequence; this gives the
assertions above, but with Z{pr and V{pr replaced by Z{pkprq, V{pkprq wherekprq Ñ 8
withr. Passing to a further subsequence gives the desired result.
Proof. (of Theorem 8.5, using p:q): We have already constructed an action of V; let us
prove, by contradiction, that it has property (*) from the Th eorem. Suppose that there is
an integer A and an inﬁnite sequence of primes qn ” 1 modulo pn such that the pull-
back of the action via fqn,A :H 1pTq, Z{pAq Ñ V{pA fails to coincide with the action of
H 1pTq, Z{pAq via the embedding ιqn,A into the derived Hecke algebra with Z{pA coefﬁ-
cients. We can choose a Taylor–Wiles system Qn containingqn and then get a contradic-
tion to p:q as soon as r ąA. This proves (*).
Now let us show that the image of ^˚V in endomorphisms of cohomology coincides
with the global derived Hecke algebra.
Refer to the diagram (161), constructed with a convergent se quence of Taylor–Wiles
data Qn. We will only use a subsequence of ns which is V-convergent. Consider for
n ěk the map
(165) W “ tS{tR
(134)
Ý ÑtSn {tRn
(142)
Ý ÑV{pk.
By (134) and the discussion after (142), the composite actua lly gives an isomorphism
(166) W{pk » V{pk.
For ﬁxed k and large n, the map (165) is independent of n: Choose ˜v P tS. Let vn,vm
be its image in tSn, tSm. As we saw in the diagram (161), the actions of vn,vm on modpk
cohomology must coincide, because both can be computed by me ans of the lift ˜v. For this
we are implicitly using (115) to see that the composite map
(167)
H ˚ pHomSpC, Zpqq Ñ H ˚ pHomSnpCbSSn, Z{pnqq
„
Ñ H ˚ pY p1q, Z{pnqm Ñ H ˚ pY p1q, Z{pkqm
is independent ofn, forn ěk.
So the images of vn,vm in V{pk have the same actions on mod pk cohomology. The
V{pk action on modpk cohomology is faithful (by (166) and (162)) so this forces the image
ofvn,vm in V{pk to coincide as claimed.
Therefore, passing to the limit overn, we get a map W{pk Ñ V{pk, which is easily seen
to be compatible as we increase k; thus the inverse limit over k deﬁnes an isomorphism
(168) W „Ñ V.
72 AKSHA Y VENKA TESH
Next, referring to (161) the action of Ext˚
S pS{I, S{Iq » ^ ˚tS on H ˚pHomSpC, Zpqq
certainly factors through ^˚W; this action of ^˚W onH ˚pHomSpC, Zpqq is compatible
under the identiﬁcations (115) and (168) with the action of ^˚V onH ˚pY p1q, Zpqm.
Therefore, by (162), V freely generates an exterior algebra inside EndpH ˚q, and H ˚
is freely generated over ^˚V byH qpY p1q, Zpqm, its minimal degree component. On the
other hand, the image of ^˚V in EndpH ˚q is contained in the global derived Hecke algebra
– the action of an element V is, by deﬁnition, a limit of actions of elements in the derive d
Hecke algebra. Indeed, V lies inside the strict global derived Hecke algebra. □
8.27. Proof of Proposition 8.6. . In our current situation, we have an inclusion
(169) ^˚ V Ă ˜T
and we have seen that H ˚pY p1q, Zpqm is generated by its lowest nonvanishing degree H q
as a ^˚V-module. If we know that H ˚pY p1q, Zpqm “ Zp, we argue that (169) is an
equality just as in the corresponding argument after (56).
If we are given S as in the statement of the Proposition, let M “H qpY p1q, ZpqmbZp Qp
as a S-module. It is semisimple by assumption, and the natural map
M b ^˚VQp ÑH ˚pY p1q, Zpqm b Qp
is now an isomorphism of S b ^˚VQp modules. However,
(graded) commutant of S b ^˚VQp on M b ^˚VQp “ S1 b ^˚VQp,
as can be veriﬁed by computing in steps: the commutant of S alone equals S1bEndp^˚VQp q,
and then inside here the (graded) commutant of ^˚VQp is S1 b ^˚VQp .
Since this commutant contains the image of ˜T acting on Qp-cohomology, the latter is
also graded commutative, since S1 is commutative by the multiplicity one hypothesis. Note
that the action on Qp cohomology is faithful because of our torsion freeness assu mption,
see 7(a) of §6.1. □
8.28. The action of Hecke operators. To conclude, let us translate what we have proved
into a more concrete assertion about the action of a derived H ecke operator.
Letq be a unramiﬁed prime for ρ, with q ” 1 modulopn, and such that ρpFrobqq is
conjugate to a strongly regular element of T _pkq. Let ν P X˚pAq` be strictly dominant
and let
α PH 1pApFqq, Z{pnq.
To this we can associate in a natural way (see below) a derived Hecke operator Tq,ν,α as
well as an element rq,ν,α s P V{pn; we will prove that the actions of these are compatible
(see Lemma below), justifying the assertions made in §1.5.
First of all, a small piece of linear algebra. Let k be a ﬁeld. Suppose given a ﬁxed
characterψ P X ˚pT _q. Let g P G_pkq be regular semisimple, with centralizer Zg; this
data allows us to construct a homomorphism of k-vector spaces
eψ,g : LiepT _q Ñ LiepZgq,
eψ,g :
ÿ
φ:T _ „ÑZg
xψ,φ ´1pgqy ¨dφ
where the sum is taken over all conjugations of T _ toZg over ¯k; the morphism is nonethe-
less deﬁned over k.
Example: if G_ “ SL2, take T _,B _ in the standard way to be the diagonal sub-
group and upper triangular matrices, and take ψ :
ˆ
x 0
0 x´1
˙
ÞÑ x. Then eψ,g sends
DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS 7 3
ˆ
1 0
0 ´1
˙
P LiepT _q to the element 2g ´ tracepgq P M2pkq: it’s enough to check this
forg PT _, where the result is clear.
Letq,ν,α be as described at the start of this subsection. We can then co nstruct a class
rq,ν,α s P V{pn
in the following way: regarding ν as a character of T _, and use the linear algebra con-
struction mentioned with k “ Qp to make the ﬁrst map of
(170) LiepT _q
eν, Frobq
Ý Ñ LiepZρpFrobqqq ãÑ LiepG_q
(at ﬁrst we get this bQp but then it preserves the integral structures, with referen ce to the
natural Zp-models of the three groups above). The resulting embedding LiepT _q Ñ Adρ
is a morphism of GalpQq{Qqq-modules, where LiepT _q is taken to have the trivial action.
As before, we may identify
H 1pApFqq, Z{pnq “ H 1pX˚pAq b Fˆ
q, Z{pnq “ HompFˆ
q,X ˚pT _q{pnq
and so from α we obtain a class
α1 P H 1pQq, LiepT _q{pnq
H 1urpQq, LiepT _q{pnq.
Here LiepT _q is taken as a trivial Galois module. We can then form
pushforward ofα1via (170) P H 1pQq, Adρnq
H 1urpQq, Adρnq.
and, as usual, this can be paired with H 1
f pZr 1
S s, Ad˚ρp1qq by means of local reciprocity.
In this way we obtain a functional H 1
f pZr 1
S s, Ad˚ρp1qq Ñ Z{pn, which we denote as
rq,ν,α s P V{pn.
8.29. Lemma. Letq,ν,α be as above. Let rq,ν,α s P V{pn be as deﬁned above.
LetTq,ν,α be the derived Hecke operator with Z{pn coefﬁcients which is supported on
theGq-orbit of pνKq,Kqq and whose value at pνKq,Kqq which corresponds to α under
the cohomology isomorphism H ˚pKq XνKqν´1, Z{pnq – H ˚pApFqq, Z{pnq.
ThenTq,ν,α corresponds to rq,ν,α s P V{pn, in the following asymptotic sense:
There isN0pmq such that forq,ν,α as above withq ” 1 modulopN0pmq, the actions of
Tq,ν,α and rq,ν,α s onH ˚pY p1q, Z{pmqm coincide.
Proof. Under the derived Satake isomorphism, Tq,ν,α is sent to
ÿ
w
wν bwα P
`
SrX˚s bH 1pApFqqq
˘W
.
With notation as in §8.17, let Θ ν PSrX˚sW
m be deﬁned so that its image under SrX˚sW
m ãÑ
SrX˚s ˜m ÑSrX˚sχ is equal to ν. Here, we regard ν PX˚ ãÑSrX˚s.
Then, after completing at m, we have an equality
SatakepTq,ν,αq “
ÿ
wPW
Θ wν ¨ Satakepθpwαqq P pSrX˚s bH 1pApFqqqqW
m
where θ is as in (154). (We can check this using the isomorphism (152) : it gives an
isomorphism of the target group with SrX˚sχ bH 1pTqq, under which θpwαq is, by its
very deﬁnition, sent to 1 bwα; under the same isomorphism Θ wν is sent to wν b 1, and
the result follows.)
74 AKSHA Y VENKA TESH
As before we have ﬁxed FrobT
q P T _pFpq an element conjugate to ρpFrobqq; ﬁx a
lift tq P T _pZpq that is conjugate to ρpFrobqq. Then Θ wν (more exactly, its preimage
under Satake) acts on H ˚pY p1q, Zpqm by xwν,tqy (this makes sense: wν PX ˚pT _q and
tq P T _pZpq, so they can be paired to get an element of Zˆ
p ). Using Theorem 8.5, we
see that the action of Tq,ν,α onH ˚pY p1q, Zpqm corresponds (in the sense of the lemma
statement) to the element
ÿ
wPW
xwν,tqy ¨fq,npwαq “
ÿ
wPW
xν,w ´1tqy fq,npwαq P V{pn.
Winding through the deﬁnitions, this element of V{pn is exactly rq,ν,α s. □
9. S OME VERY POOR EVIDENCE FOR THE MAIN CONJECTURE : T ORI AND THE
TRIVIAL REPRESENTATION
We verify that the main conjecture (Conjecture 8.8) holds in the case when G is an
anisotropic torus. This is straightforward, but still slig htly comforting.
One may also verify that a certain analogous statement to Con jecture 8.8 holds in the
situation studied in §5, but there we do not understand the si tuation clearly at present –
hopefully it will eventually prove to be a specialization of the general conjecture to the
nontempered case.
9.1. Setup. Let T be an anisotropic F -torus; let O be the ring of integers of F . Let us
ﬁx a ﬁnite set of places S such that T admits a smooth model over Or 1
S s. We assume it
contains all places ℘ above the rational prime p.
The associated symmetric space
S “ TpF b Rq{maximal compact
hasq,δ invariants (see (18)):
q “ 0,δ “ dimpSq.
The arithmetic manifold Y pKq associated to a level structure K is a disjoint union of
copies of S{∆ , where ∆ is a congruence subgroup of TpOq. Moreover the quotient S{∆
is a union of compact tori, and thus the rank of ∆ , i.e. dimQp∆ b Qq, equals δ. We will
suppose thatK is chosen so small that ∆ is free of p-torsion.
9.2. Galois cohomology. Let M be the motive associated to the ﬁrst homology group
H1pTq of T.
LetX˚pTq be the co-character group of T. It carries an action of GalpF {F q. Coming
fromX˚ bZ Gm
„Ñ T, we get an isomorphism of GalpF {F q-modules
Mp :“p-adic realization of M “X˚pTq bZ Zpp1q » limÐ ÝTrpns,
thep-adic Tate module of T. Computing with the Kummer sequence,
(171) H 1pOr 1
S s,Mpq » TpOr 1
S sq b Zp.
Inside the left-hand side, we can consider those classes tha t are crystalline at p and unram-
iﬁed at all primes away from p, including primes in S. We will denote this subgroup by
H 1
f,urpF,Mpq. 18
18For a precise deﬁnition we refer to [2]: the group we have call ed H 1
f, ur is the group denoted by H 1
f,U in [2,
Deﬁnition 5.1] with U taken to be all ﬁnite places. This group is often simply writt en H 1
f pF, ´q in the literature.
DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS 7 5
The subgroup on the right-hand side corresponding to H 1
f,urpF,Mpq, call it
∆ 1 Ă TpOr 1
S sq b Zp,
is commensurable to the image of ∆ b Zp in the right-hand side of (171). Indeed, the
constraint that a point t P TpOr 1
S sq have cohomology class in H 1
f,ur is equivalent to
forcing t to belong to a suitable open compact subgroup of TpFvq for each v P S; see
[18, Theorem 2.3.1] for this statement in the trickier case w henv is abovep. We suppose
(shrinking ∆ a little if necessary) that ∆ b Zp Ă ∆ 1.
Also, the motivic cohomologyH 1
motpM, Qp1qq is identiﬁed with with the TpQq b Q,
as we may see by ﬁrst passing to an extension that trivializes the torus T. Presumably the
following is valid, but I did not try to check it:
Assumption: The subgroup of “integral classes” H 1
motpMZ, Qp1qq (see
discussion after (7)) is identiﬁed with the image of ∆ b Q inside TpQq b
Q.
Now a cohomological automorphic form Π for T is trivial on the connected component
of TpF b Rq, i.e. they are the ﬁnite order idèle class characters of T. However, the
associated co-adjoint motive (see §1.2) doesn’t depend on w hich idele class character: we
have simply
p coadjoint motive for Π q p1q » M,
the motiveM described above. 19
Now let us examine Conjecture 8.8 in this case. Put
V “H 1
f,urpF,Mpq_,
whereMp is thep-adic etale realization, and _ denotes Zp-linear dual; thus V “ Homp∆ 1, Zpq.
The notationH 1
f,ur was deﬁned after (171).
There is a natural action of V onH ˚pY, Zpq, obtained from the maps
(172) V “H 1p∆ 1, Zpq Ñ H 1p∆ , Zpq.
Moreover, motivic cohomology gives a lattice in V b Q “H 1p∆ 1, Qpq (the classes which
are Q-valued on ∆ Ă ∆ 1) and obviously this lattice indeed preserves H ˚pY, Qq, in the
Q-linear extension of the action of V.
The only point to be discussed is that the action (172) is inde ed that resulting from the
same formalism as §8. We describe this only brieﬂy. Let v be a ﬁnite place not belonging
toS, so that T extends to a smooth torus over Ov. As usual we have an injection,
HompTpOvq, Z{pnq ãÑ derived Hecke algebra at v,
and thus an action of the left-hand group on the cohomology of H ˚pY, Z{pnq; explicitly,
this action is obtained by pulling back cohomology classes v ia ∆ Ñ TpOvq, and cup
product. By just the same procedure as that described in (124 ), we can construct a map
HompTpOvq, Z{pnq Ñ V{pn
lo omo on
»Homp∆ 1,Z{pnq
,
19 Indeed, the the Zp-linear dual of ˆT is identiﬁed with
LiepT _q_ » pLiepGmq b X˚ pT _qq_ » X ˚ pT _q b Zp » X˚ pTq b Zp
where we have ﬁxed an isomorphism Z » LiepGmq.
76 AKSHA Y VENKA TESH
and one veriﬁes this is the map induced by ∆ 1 Ñ TpOvq b Zp. Then the action of V{pn
on H ˚pY, Z{pnq is compatible with the “derived Hecke” action of HompTpOvq, Z{pnq
for allv; and in fact this compatibility determines the action of V{pn.
APPENDIX A. R EMEDIAL ALGEBRA
In this section we ﬁll in some “intuitively obvious” claims i n the text in grotesque detail,
in particular the identiﬁcations between various differen t models of the derived Hecke
algebra. (The word “remedial” in the title of this section re fers to my own lack of ﬂuency
with homological algebra.)
An action of a topological group will be called smooth if the stabilizer of every point
is an open subgroup. We will ﬁx a ﬁnite ring S of cardinality prime to p. A “smooth
representation of G”, in this section, will be a smooth action of G on an S-module. We
writeSG (or occasionallySrGs when typography requires) for the group algebra ofG with
coefﬁcients in S. We will write HomSG for homomorphisms of SG-modules; in §A.11
we abbreviate this to HomG because other notation becomes very dense.
Note that the usage of U andK in this section do not precisely match their usage in the
main text.
A.1. Let K be a proﬁnite group, which admits a pro- p open normal compact subgroup
U . Then the category C of smooth representations ofK is an abelian category with enough
projectives. In fact, if Q is a projective K{U module, then considering Q as a smooth
K-module ˜Q it remains projective: HomSK p ˜Q,V q “ HomSrK{UspQ,V U q andV ÞÑVU
is exact by the hypothesis on U . (One can lift U -invariants under a surjection V1։V2 by
averaging.)
In this situation, restriction to a ﬁnite index subgroup K 1 Ă K preserves projectivity.
Indeed HomSK 1pResK
K 1A,B q “ HomSK pA, IndK
K 1Bq and the induction functor is exact.
A.2. Now let G “ Gv be the points of a reductive group over a p-adic ﬁeld, or any
open subgroup thereof. Then the category of smooth represen tations of Gv is an abelian
category and it has enough projectives.
Indeed, considerW “SrG{U s for an open pro-p compactU ĂG. Then
HomSGpW,V q » VU,
which is obviously exact in V . So W is projective, and now given any other V we choose
generatorsvi forV , open pro-p compact subgroupsUi ﬁxing vi, corresponding projectives
Wi, and then get ÀWi։V .
Throughout the remainder of this section, we suppose that G is as above, that K is an
open compact subgroup of G (in particular, K is proﬁnite), and that U Ă K is a pro-p
open normal compact subgroup of K.
A.3. Fix a resolution of the trivial K-representation by projective smooth K-modules:
(173) Q : ¨ ¨ ¨ ÑQi Ñ ¨ ¨ ¨ Ñ Q1 ÑS.
(Here, and in what follows, we will use boldface letters to de note complexes.) To be
explicit, let us take Q to be the standard “bar” resolution of S by free SrK{U s-modules,
considered as a complex of smooth K-representations.
Then HompQ, Qq computes H ˚pK,S q, the continuous cohomology of the proﬁnite
groupK withS coefﬁcients: indeed, the the cohomology of HompQ, Qq is identiﬁed with
H ˚pK{U,S q, which is identiﬁed by pullback with the continuous cohomol ogyH ˚pK,S q.
DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS 7 7
The complex HompQ, Qq has the structure of differential graded algebra arising fr om
composition, and the resulting multiplication on H ˚pK,S q coincides with the cup product
(this reduces to a corresponding statement for a ﬁnite group ; for that see [37]).
IfK 1 Ă K is a ﬁnite index subgroup, then HomSK 1pQ, Qq still computes H ˚pK 1,S q
(see remarks above). Moreover, the averaging operator ř
K{K 1 – that is to say, the map
sending
f P HomSK 1pQ, Qq ÞÑ
ÿ
κ
κfκ ´1 P HomSK p... q
realizes the corestriction map H ˚pK 1,S q Ñ H ˚pK,S q, where the κ sum is taken over a
set of coset representatives for K{K 1 inK.
A.4. Induction and Frobenius reciprocity. We use the word “induction” for the functor
fromK-modules toG modules
(174) M↝ SG bSK M.
This is isomorphic to the usual “compact” induction, namely space of functions
indG
KpM q :“ t f :G ÑM :f pgkq “ k´1f pgq,(175)
f is supported on ﬁnitely many left translates of Ku
where the action of h PG is by left translation, i.e. lhf pxq “ f ph´1xq. We will drop the
word “compact” and simply refer to (175) or (174) as “inducti on”; we refer to the model
(175) for induction as the “function model.”
We can deﬁne inverse isomorphisms between (175) and (174) as follows: deﬁne indG
KpM q Ñ
SrGs bSrKsM via
f ÞÑ
ÿ
xPpG{Kq
gx bf pgxq,
wheregx PG is a representative forx PG{K; in the other direction, we send g bm to the
function supported on gK whose value ong equalsm
A.5. Frobenius reciprocity. We have Frobenius reciprocity
HomSGpindG
K M,N q » HomSK pM,N q
and therefore induction carries projective K-modules to projective G-modules. Explicitly
anSK -homomorphismf : M Ñ N is sent to its obvious G-linear extension SG bSK
M ÑN .
IfG ĄK has ﬁnite index, we also have the reverse adjointness (since “compact induc-
tion” and “induction” coincide): to give a K-mapf : M Ñ M 1 is the same as giving a
mapFf :M Ñ indG
KM 1. Explicitly, in the function model for the induced represen tation,
Ff is characterized by the property Ff pmqpeq “ f pmq, and so
Ff pmqpgq “ lg´ 1Ff pmqpeq “ Ff pg´1mqpeq “ f pg´1mq
and thus in the tensor product model
(176) Ff pmq “
ÿ
xPpG{Kq
gx bf pg´1
x mq
78 AKSHA Y VENKA TESH
A.6. Restriction of induced representations. Let Q be a smooth representation of K.
The restriction of indG
KQ toK is isomorphic to
(177)
à
xPKzG{K
SrKgxKs bSK Q »
à
K
SrKs bSKxQx »
à
x
indK
KxQx
wherex “gxK runs through a set of representatives for K-orbits on G{K, and we write
Kx “ K XgxKg ´1
x ; moreover for a K-module Q, we denote by Qx the Kx-module
whose underlying space is Q, but for which the action ˚ ofKx onQ is deﬁned thus:
(178) κ ˚q “
`
Adpg´1
x qκ
˘
q.
The ﬁrst map of (177) is given explicitly by
(179) k1gxk2 bq “k1gx bk2q ÞÑk1 bk2q
and the inverse map sends
(180) k bq ÞÑkgx bq.
In the function model of the induced representations, the co mposite map of (177) sends
F : KgxK Ñ Q to the function F 1 : k ÞÑ F pkgxq. In the reverse direction, given a
functionF 1 in the function model of indK
KxQx, the inverse of (177) sends it to
(181)
ÿ
kPK{Kx
kgx bf pkq P SrKgxKs bSK Q.
A.7. Derived Hecke algebra. The derived Hecke algebra for the pair pG,K q with coef-
ﬁcients in S is deﬁned as
à
i
Exti
SGpSrG{Ks,S rG{Ksq
where the Ext-groups are taken in the category of smooth S-representations.
We can construct an explicit model as follows. Let Q be as in (173). Then P “ indQ
is a projective resolution of SrG{Ks. In particular, HomSGpP, Pq has the structure of a
differential graded algebra and its cohomology gives the de rived Hecke algebra.
A.8. We will now explicitly describe the isomorphism (25) be tween the derived Hecke
algebra and its “double coset model.”
Let P, Q be as in §A.7.
We have
(182) HomSGpP, Pq “ HomSK pQ, indG
KQq
(177)
Ð Ý
à
xPKzG{K
HomSK pQ, indK
KxQxq
looooooooooooooooooomooooooooooooooooooon
“HomSKx pQ,Qxq
,
where x varies now through KzG{K, again gxK is a representative for x and Kx “
K X AdpgxqK, and the twist operation Qx is as described in (178).
Note that the last map induces a cohomology isomorphism. We must see thatH ˚pHomSK pQ, ´qq
commutes with the inﬁnite direct sum À
x indK
KxQx. However, Qx is cohomologically
concentrated in degree 0, and so the same is true for indK
KxQx; it is enough to show, then,
for anyK-modulesMi, the obvious map
à
i
HomSK pQ,Miq Ý ÑHomSK pQ,
à
i
Miqq
is a quasi-isomorphism. But this follows from the fact that t akingU invariants commutes
with inﬁnite direct sum, as does the functor H ˚pK{U, ´q.
DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS 7 9
Note that the cohomology of HomSKxpQ, Qxq is identiﬁed with H ˚pKx,S q, because
Q and Qx are resolutions of S, and moreover Q is a complex of projective Kx-modules.
Thus, (182) gives rise to an isomorphism:
(183) H ˚ pHomSGpP, Pqq »
à
x
H ˚pKx,S q.
For later use, we explicate the map of (182), going from right to left: An element f P
HomSKxpQ, Qxq must satisfyf pκqq “ pg´1
x κgxqf pqq forκ PKx; the associated element
of HomSK pQ, indG
KQq is given in the tensor product model of the induced represent ation
by the formula of (176):
q P Q ÞÑ
ÿ
kPK{Kx
kgx bf pk´1qq
which is well-deﬁned.
A.9. Action of derived Hecke algebra on derived invariants. Now suppose that M
is a complex of smooth G-representations. There is a natural action of EndSGpPq on
HomSGpP, Mq. Moreover, the latter complex computes the hypercohomolog y H˚pK, Mq
ofK with coefﬁcients in the complex M.
Thus, because of (183), we get an action of H ˚pKx,S q on H˚pK, Mq. Let us de-
scribe the action of hx PH ˚pKx,S q on H˚pK, Mq as explicitly as possible, in particular
justifying the claims of §2.10:
A.10. Lemma. With notation as above, the action of hx is given by the following compos-
ite:
H˚pK, Mq
Adpg´ 1
x q˚
Ý Ñ H˚pKx, Mxq
mÞÑgxm
Ý Ñ H˚pKx, Mq Yhx
Ý ÑH˚pKx, Mq CoresÝ ÑH˚pK, Mq.
Here the ﬁrst map is the pull-back induced by Adpg´1
x q : Kx ãÑ K, which pulls back M
to Mx.
Proof. Chooseh1
x P HomSK pQ, indK
KxQxq representinghx. For f P HomSGpP, Mq we
denote byfx P HomSK pindK
KxQx, Mq the restriction. We denote by rh1
xs P HomSKxpQ, Qxq
and rfxs P HomSKxpQx, Mq the elements obtained from h1
x,fx using Frobenius reci-
procity (but using the two different versions of Frobenius r eciprocity).
We want to compare the composition fx ˝h1
x and rfxs ˝ rh1
xs i.e.
(184)
h1
x P HomSK pQ, indK
Kx Qxq ˆ fx P HomSK pindK
Kx Qx, Mq /d47/d47 HomSK pQ, Mq
rh1
xs P HomSKxpQ, Qxq
„
/d79/d79
ˆ r fxs P HomSKx pQx, Mq /d47/d47
„
/d79/d79
HomSKx pQ, Mq
We compute
fx ˝h1
xpqq
(176)
“ fx
¨
˝ ÿ
kiPK{Kx
ki b rh1
xspk´1
i qq
˛
‚“
ÿ
ki
kirfxs ˝ rh1
xspk´1
i qq
i.e., this is what we get by averaging rfxs˝rh1
xs over the action ofK{Kx. The cohomology
class of the composition rfxs ˝ rh1
xs simply amounts (at the level of cohomology) to the
cup product of the class rfxs P H˚pKx, Mq (hypercohomology) with the class rh1
xs P
H ˚pKx,S q. So to prove the lemma it remains to show:
80 AKSHA Y VENKA TESH
Subclaim: The class rfxs P H˚pKx, Mq is obtained from rf s P H˚pK, Mq via
H˚pK, Mq
Adpg´ 1
x q˚
Ý Ñ H˚pKx, Mxq
mÞÑgxm
Ý Ñ H˚pKx, Mq
At the chain level this map is given by the composite
HomSK pQ, Mq Ñ HomSKxpQx, Mxq Ñ HomSKxpQx, Mq
where the ﬁrst map is the trivial map, just considering maps o fK modules asKx-modules
via Adpg´1
x q : Kx Ñ K; and the second map Mx Ñ M is given by m ÞÑ gxm. To
check the subclaim, note that rfxs P HomSKxpQx, Mq sendsq P Qx to the value of fx
on the element 1 bq P indK
KxQ, which is carried by the isomorphism inverse to (177) to
gx bq P indG
KQ; thus,
rfxs :q ÞÑgxf pqq
where here, on the right hand side, we regard f as a map Q Ñ M by Frobenius reciprocity
(i.e. we pull it back via the obvious embedding Q ãÑ P,q ÞÑ 1 bq). This concludes the
justiﬁcation of the subclaim. □
A.11. Multiplication in the derived Hecke algebra. We ﬁnally analyze composition (i.e.
multiplication) in the derived Hecke algebra, explicating it with respect to the isomorphism
(183), and thus justifying the description given in §2.3.
Letα,β,γ PG{K with representativesgα,gβ,gγ PG. Suppose given hα PH ˚pKgα q
and similarly for β. We will compute the product hβhα considered as elements of the
derived Hecke algebra – or more precisely the H ˚pKgγ q component of their product.
As in (182) we represent hα by an element h1
α P HomKpQ, indG
KQq, and denote by
rh1
αs the corresponding element of HomKgα pQ, Qgα q and similarly for hβ. By (176) we
have the explicit formula
h1
α :q PQ ÞÑ
ÿ
kPK{Kα
kgα b rh1
αspk´1qq P SrKgαKs bSK Q,
where we make a modest abuse of notation by identifying K{Kα to a set of representatives
for it inK. Now applyh1
β to the right-hand side, regardingh1
β P HomSGpP, Pq. The result
is:
(185)
ÿ
kPK{Kα
ÿ
k1PK{Kβ
kgαk1gβ b rh1
βsk1´1rh1
αsk´1 P HomKpQ,SG bSK Qq
The desired H ˚pKgγ q component of the product hβ ¨hα is given by considering all k,k 1
for whichkgαk1gβ PKgγK, i.e. it is represented by
(186)
ÿ
kgα k1gβ PKgγK
kgαk1gβ b rh1
βsk1´1rh1
αsk´1 P HomKpQ,S rKgγKs bSK Qq
By “dual” Frobenius reciprocity (see before (176)) the righ t-hand side can be identiﬁed
with HomKpQ, indK
Kγ Qγq » HomKγ pQ, Qγq. If we write kgαk1gβ “ k1gγk2, an ex-
plicit formula for the corresponding element of HomKpQ, indK
Kγ Qγq is given (179) by
q ÞÑ
ÿ
kgα k1gβ “k1gγk2
k1 bk2rh1
βsk1´1rh1
αsk´1pqqloooooooooooooooomoooooooooooooooon
PSK bSKγ Qγ
where the right-hand sum is over the same k,k 1 as before, and we consider only those k,k 1
such thatkgαk1gβ PKgγK. Then the corresponding element of HomKγ pQ, Qγq is given
(see (176)) by picking out those terms for which k1 P Kγ; in that case we can rewrite
DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS 8 1
k1gγk2 “ gγpAdpgγq´1k1qk2 and so we may as well suppose that k1 “ 1. Thus, the
desired result is
(187) ÿ
k,k1 :kgα k1gβ “gγk2
k2 rh1
βsk1´1
looomooon
HomKAdpkgα qKk1 gβ
pQkgα ,Qkgα k1gβ q
rh1
αsk´1
looomooon
HomKkgα pQ,Qkgα q
P HomKγ pQ, Qγq
Here we observed that
rh1
α s˝ k´ 1 P HomKkgα pQ, Qkgα q, rh1
β s˝ k1´ 1 P HomKk1 gβ
pQ, Qk1gβ q » HomAdpgqKk1 gβ
pQg, Qgk1gβ q
(the last isomorphism is the obvious one and we apply it to g “ kgα). 20 Returning to
(187), set
x “kgαk1gβK “gγK, y “kgαK, z “eK, U “ stabilizerpx,y,z q
Then x,y are in relative position β, and y,z are in relative position α, and x,z are in
relative positionγ.
Note also that
U “Kkgα X AdpkgαqKk1gβ “K X AdpkgαqK X Adpkgαk1gβqK.
Therefore, the composite occurring in (187)
F “
HomKAdpkgα qKk1 gβ
pQkgα ,Qkgα k1gβ q
hkkkikkkj
rh1
βsk1´1 ˝ r h1
αsk´1
looomooon
HomKgα pQ,Qkgα q
actually belongs to HomU pQ, Qkgα k1gβ q; as such F deﬁnes a cohomology class for U .
This cohomology class is given by taking the classeshα,hβ, transporting them to classes in
H ˚pKkgα q andH ˚pAdpkgαqK 1
k1gβ q, by means of Adpkq :Kgα »Kkgα and Adpkgαk1q :
Kβ » AdpkgαqK 1
k1gβ , restricting to U , and taking the cup product.
Said differently, let us think of hα as a G-invariant associationHα from pairs pu,v q P
G{K ˆG{K to cohomology classes in H ˚pGuvq – the one whose value at pgαK,e q is
given by the original cohomology class in H ˚pKgα q. Similarly for hβ. Then,
cohomology class of F “Hβpx,y q YHαpy,z q P H ˚pGxyz q
NowKγ “Gxz acts on the set of pk,k 1,k 2q as above, i.e. satisfying kgαk1gβ “gγk2,
via
κ : pk,k 1,k 2q ÞÑ pκk,k 1, Adpg´1
γ qκk2q.
For ﬁxed pk,k 1,k 2q the stabilizer of this Kγ-action is just U . The contribution of a single
Kγ-orbit is given by ÿ
κPKγ {U
Adpg´1
γ qκ ˝F ˝κ´1
which is to say that it averages F , considered as an element of HompQ, Qγq, over the
cosets of Kγ{U . (The Adg´1
γ accounts for the twisted action on Qγ). This precisely
realizes the corestriction from U toKγ.
20For example, to check the ﬁrst, note that for z P Kkgα and q P Q we have
rh1
α s ˝ k´ 1pzqq “ r h1
α s
`
pk´ 1zkqpk´ 1qq
˘
“ pg´ 1
α k´ 1zkg α qrh1
α s ˝ k´ 1pqq
Indeed, rh1
α s represents the class in H ˚ pKkgα q, obtained by applying Adpkq to the class hα P H ˚ pKgα q.
82 AKSHA Y VENKA TESH
In summary, we have recovered the description of multiplica tion in the derived Hecke
algebra given in §2.3.
APPENDIX B. K OSZUL ALGEBRA ; OTHER ODDS AND ENDS
LetB be a commutative ring with 1. Let
Brrx1,...,x rss “ S ιÝ ÑR “Brry1,...,y r´δss
whereι sendsxi toyi fori ďr ´δ, andxi to zero for i ąr ´δ.
Let pS be the kernel of the natural augmentation S ÑB, and similarly for R. Write tS
for theB-linear dual of for pS{p2
S and similarly for tR. Just as in (88) we have a canonical
identiﬁcation
Ext1
SpB,B q » tS.
We will prove:
B.1. Lemma. Ext˚
SpB,B q is a free exterior algebra over its degree 1 component; thus we
have Ext˚
SpB,B q » ^ ˚tS as graded B-algebra. Moreover , there is an identiﬁcation of
Ext˚
SpR,B q with ^˚ptS{tRq in such a way that the natural action of Ext˚
SpB,B q » ^ ˚tS
is the natural one obtained from the algebra map ^˚tS Ñ ^ ˚ptS{tRq.
This will follow from the computations of §B.2 (more precise ly, with the precisely
analogous computations wherein one replaces the role of sym metric algebras by power
series algebras).
B.2. Koszul algebra. LetW be a free module of rank e over a base ring B and consider
the ringR “ SymBpW q, i.e. “the ring of functions on W _.” In what follows we will omit
theB subscript on SymB.
We have a resolution
¨ ¨ ¨ Ñ SympW q b ^2W Ñ SympW q bW Ñ SympW qlooooooooooooooooooooooooooooooooooomooooooooooooooooooooooooooooooooooon
K
ÑB,
where the differential sends
r bw1 ^ ¨ ¨ ¨ ^wr P SympW q b ^iW ÞÑ
ÿ
i
p´1qi´1rwi bw1 ^... xwi ^...w r.
There is a corresponding resolution where we replace SympW q by its completion with
respect to the augmentation SympW q Ñ B, i.e. when we replace a symmetric algebra by
a formal power series algebra.
In particular, we get
HomRpK,B q »
`
^iW
˘_
with zero differentials.
and thus an identiﬁcation of Exti
RpB,B q with
`
^iW
˘_
.
In fact, Ext˚
RpB,B q is a free exterior algebra, where the algebra structure on th e Ext-
groups arising from their identiﬁcation with the cohomolog y of the differential graded
algebra
HomRpK, Kq.
To see this, one veriﬁes that each element of w P W _, considered as acting on K by
contractions, actually deﬁnes a degree ´1 endomorphism of K; the resulting inclusion
ľ˚
pW _q ãÑ HomRpK, Kq
gives a quasi-isomorphism of differential graded algebras .
DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS 8 3
Suppose now that U is a free submodule of W such that W {U is also free. In this
situation we have a quotient map
R “ SympW q Ñ SympW {U q :“ ¯R
We have a resolution ofR-modules (where the differential is given by the same formul a as
before):
¨ ¨ ¨ Ñ SympW q b ^2U Ñ SympW q bU Ñ SympW qloooooooooooooooooooooooooooooooooomoooooooooooooooooooooooooooooooooon
Q
„Ý Ñ ¯R,
and from this we identify Ext˚
Rp ¯R,B q with p^˚U q_.
B.3. Lemma. The action of Ext˚
RpB,B q » p^ ˚W q_ on this is the natural one that arises
from the mapW _ ÑU _.
Proof. It is enough to check this for the action of Ext1
RpB,B q. We have identiﬁcations:
Ext˚
Rp ¯R,B q » H ˚ pHomRpQ,B qq “ H ˚ pHomRpQ, Kqq.
Explicitly, a class in ωj P p^jU q_ » Extj
Rp ¯R,B q is represented by a map of complexes
Q Ñ K as follows:
(188) ¨ ¨ ¨ /d47/d47R b ^j`1U /d47/d47
f
/d15/d15
R b ^jU /d47/d47
ωj P^jU _
/d15/d15
R b ^j´1U
¨ ¨ ¨ /d47/d47K1 “R bW /d47/d47K0 “R /d47/d47 0.
(since this lifts the map Q ÑBrjs associated toωj).
Fix a basise1,...,e r forU and extend it to a basise1,...,e e forW . ForI Ă t1,...,e u
with cardinality r, we deﬁne eI P ^rW thus: write I “ ti1,...,i ru withi1 ă ¨ ¨ ¨ ă ir
and puteI “ei1 ^ei2 ^ ¨ ¨ ¨ ^eir . We may choose f to be given, explicitly, as
eJ P ^j`1U ÞÑ
ÿ
kPJ
p´1qrks´1ωjpeJ´kq bek PR bW,
where rks means the position of k inJ (i.e. if J is ordered in increasing order, then 1 for
the smallest element, two for the second smallest, etc.)
To compute, now, the action ofβ PW _ “ Ext1
RpB,B q on the class ωj, we just regard
β as anR-module mapK1 “R bW ÑR, and then compose
β ˝f P HomRp^j`1U bR,R q “
`
^j`1U
˘_
.
Explicitly,
β ˝f :eJ ÞÑ
ÿ
kPJ
p´1qrks´1βpekqωjpeJ´kq “ pβ ^ωj,eJ q
i.e.β ^ωj, whereβ is the image of β inU _. This concludes the proof. □
B.4. A result in topology. Suppose that π : X Ñ Y is a covering of pointed Hausdorff
topological spaces, with Galois group ∆ . This covering is classiﬁed by a map Y Ñ B∆
fromY to the classifying space of ∆ .
There are two natural actions of H ˚p∆ ,E q (withE a coefﬁcient ring) on H ˚pY,E q:
(a) The ﬁrst arises from pullback of cohomology classes unde rY Ñ B∆ together
with cup product.
84 AKSHA Y VENKA TESH
(b) The second arises from the identiﬁcation of the cochain c omplex of Y , with E
coefﬁcients, with
C˚pY ;Eq » HomE∆ pC˚pX,E q;Eq
where C˚pX;Eq is the cochain complex of X (or e.g. the complex of a ∆ -
equivariant cell structure), thought of as a complex of E∆ -modules. Then one
composes with self maps of E in the derived category of E∆ -modules.
For lack of a reference, we will prove the coincidence of thes e actions. For this we
will use the following standard Lemma concerning the coinci dence of singular and sheaf
cohomology (see [30] for a careful discussion; however this reference does not discuss the
product structures):
B.5. Lemma. F or any locally contractible Hausdorff space M , and any E-module A,
letA be the constant sheaf on M with constant value A, considered as an object of the
category of sheaves S ofE-modules onM .
Then the complex of local chains U ÞÑ C˚pU,A q deﬁnes a presheaf on M ; let C˚
A be
its sheaﬁﬁcation. Then A Ñ C˚
A is a ﬂasque resolution of A. Moreover , the natural maps
C˚pM,A q Ñ Γ pM, C˚
Aq “ HomSpA, C˚
Aq
induces, at the level of cohomology, an isomorphism
(189) H ˚pM,A q » Ext˚
SpA,A q
which carries the cup product on the left to the Ext-product to the right.
Proof. (that (a) and (b) coincide): Observe, ﬁrst of all, that every E∆ -moduleM gives a
locally constant sheafM onY , namely, the one represented by the coveringpXˆM q{∆ Ñ
Y . The cochains C˚pY,M q are then given by HomE∆ pC˚pX,E q,M q.
Fixα∆ P Hmp∆ ,E q. It gives rise to a homomorphism α :E ÑErms in the derived
category ofE∆ -modules, which can be represented by a diagram E „ÐP ÑErms where
P is a complex of projective E∆ -modules. Thus we get a diagram of locally constant
sheaves onY :
α :E „ÐP ÑErms.
This gives a map in the derived category of sheaves on Y , and thus an element of
Extm
S pE,E q; this element represents the pullback αY of α∆ to Y . or rather its image
under (189).
By the ﬁnal sentence of the Lemma, the cup product with αY is given, at the level of
cohomology, by the Ext-product, which is explicitly the composite:
H ˚pY,E q „ÐH ˚pY,P q Ñ H ˚pY,E rmsq
By the lemma, these groups are naturally identiﬁed with the c ohomology of the corre-
sponding cochain groups; so the above composite coincides w ith
HomE∆ pC˚pX,E q,E q „Ð HomE∆ pC˚pX,E q,P q Ñ HomE∆ pC˚pX,E q,E q
where the middle term is now the Hom-complex between two complexes.
But this composite is also given by the Ext-product, in the category of E∆ -modules,
with the class of α. This concludes the proof of the coincidence of (a) and (b). □
