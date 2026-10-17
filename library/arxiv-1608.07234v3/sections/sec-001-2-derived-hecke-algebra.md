---
doc_id: arxiv-1608.07234v3
doc_title: "DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS"
section_id: sec-001-2-derived-hecke-algebra
section_title: "Derived Hecke algebra"
section_number: 2
pages: 11-21
source_pdf: 1608.07234v3.pdf
source_sha256: 311730670d2fdcb7
toc_source: outline
---
11
and deﬁne q so that 2q ` δ “ dimY pKq. These have the same signiﬁcance as described
in (5), at least if we suppose that the center of G is anisotropic over F.
We will will work only with open compact subgroups with a product structure, i.e.
(19)
K “
ź
Kv
where Kv Ă GpFvq is an open compact subgroup, and Kv is a hyperspecial maximal
compact of Gv for all but ﬁnitely many primes v. A prime v will be “good” for K when
Kv is hyperspecial and the ambient group G is quasi-split at v. The “level of K” will be,
by deﬁnition, the (ﬁnite) set of all primes v which are not good.
G has a dual group G_, which we will regard as a split Chevalley group over Z; in
particular, its Lie algebra is deﬁned over Z, and its points are deﬁned over any ring R. We
regard it as equipped with a maximal torus T _ inside a Borel subgroup B_.
In the discussion of the Taylor–Wiles method, which takes place in §6 and §8, it is
convenient to additionally assume:
G is simply connected and G_ is adjoint.
This is a minor issue, to avoid the usual difﬁculties of “square roots.” One could (better)
replace G_ by some version of the c-group of [7].
When we discuss Galois cohomology, we will follow the usual convention that, for
a module M under the absolute Galois group GalpL{Lq of a ﬁeld M, we denote by
H˚pL, Mq the continuous cohomology of the proﬁnite group GalpL{Lq with coefﬁcients
in M. For L a number ﬁeld, with ring of integers O Ă L, we denote by H1pOr 1
S s, Mq Ă
H1pL, Mq the subset of classes that are unramiﬁed outside S and H1
fpOr 1
S s, Mq Ă H1pOr 1
S s, Mq
the classes that are, moreover, crystalline at p.
Warning: In the literature, the subscript f is often used to mean classes that are crys-
talline at p and unramiﬁed at all other places, not merely at places outside S. Indeed, we
implicitly used this notation in §1.2 and §1.3 when we wrote H1
fpGQ, ´q. However, in the
remainder of the text, we will not use this convention. To avoid any confusion, on the one
occasion (in §9) we wish to refer to classes that are crystalline at p and unramiﬁed at all
other places, we will use the notation H1
f,ur. This notation will be reprised when it is used
so the reader need not remember it now.
2. DERIVED HECKE ALGEBRA
We introduce the derived Hecke algebra (Deﬁnition 2.2) and then give two equivalent
descriptions in §2.3 and §2.4. The model given in §2.3 is by far the most useful. We shall
then describe the action of the derived Hecke algebra on the cohomology of an arithmetic
group in §2.6, and then make it a bit more concrete in §2.10. Finally, §2.12 discusses some
minor points to do with change of coefﬁcient ring, and §2.13 discusses some other minor
points about passage between Z{ℓn coefﬁcients and Zℓcoefﬁcients.
Appendix A expands on various points of homological algebra that are used in the
current section.
2.1.
As in §1.8, we ﬁx a prime v of F, with residue ﬁeld Fv of characteristic pv and size
qv, and set Gv “ GpFvq. We denote by Uv an open compact subgroup of Gv. Eventually,
we will use only the case of Uv being either a maximal compact subgroup or an Iwahori
subgroup, but there is no need to impose this. When we are working strictly in a local
setting, we will abbreviate these simply to G and U:
G “ Gv, U “ Uv.
12
AKSHAY VENKATESH
It will also be convenient to ﬁx
(20)
Vv “ a pro-pv, normal, ﬁnite index subgroup of Uv,
which we again abbreviate to V when it will cause no confusion.
Let S be a ﬁnite coefﬁcient ring in which qv is invertible. In what follows, by “G-
module” we mean a module M under the group algebra SG with the property that every
m P M has open stabilizer in G. The category of G-modules is an abelian category and it
has enough projective objects (see §A.2).
The usual Hecke algebra for the pair pG, Uq can be deﬁned as the endomorphism ring
HomSGpSrXs, SrXsq, where X “ G{U and SrXs denotes the free S-module on a set X.
Motivated by this, we deﬁne:
2.2. Deﬁnition. The derived Hecke algebra for pG, Uq with coefﬁcients in S is the graded
algebra
(21)
H pG, UqS :“ Ext˚pSrG{Us, SrG{Usq,
where the Ext-group is taken inside the category of G-modules.
Let us record some variants on the notation:
- We will write simply H pG, Uq when the coefﬁcients are understood to be S;
- We write H jpG, Uq or H pjqpG, Uq for the component in degree j, i.e. the Extj
summand on the right.
- In global situations where we have ﬁxed a level structure Kv ⩽Gv for all v, or
for almost all v, we will often write simply Hv,S for the corresponding derived
Hecke algebra H pGv, Kvq. Again we will write simply Hv if the coefﬁcients are
understood to be S.
If we choose a projective resolution P of SrG{Us as G-module, then H pG, Uq is
identiﬁed with the cohomology of the differential graded algebra HomSGpP, Pq. It will
be convenient for later use to make an explicit choice of P: Let Q be a free resolution
of the trivial module S in the category of SrU{V s-modules. We may take P to be the
compact induction (from U to G) of Q. Observe that all the groups Pi of the resulting
resolution are free S-modules.
2.3. Description in terms of invariant functions. We may also describe H pG, Uq as the
algebra of “G-equivariant cohomology classes on G{U ˆ G{U with ﬁnite support modulo
G.” We now spell out carefully what this means; an explicit isomorphism between this
description and Deﬁnition 2.2 is constructed in Appendix §A.
First some notation: for x, y P G{U, we denote by Gxy the pointwise stabilizer of px, yq
inside G; it is a proﬁnite group. We denote by H˚pGxy, Sq the continuous cohomology of
Gxy with coefﬁcients in S (discretely topologized).
In this model, an element of H pG, Uq is an assignment h that takes as input px, yq P
G{U ˆ G{U and produces as output hpx, yq P H˚pGxy, Sq, subject to the following
conditions:
‚ h is G-invariant, that is to say, rgs˚hpgx, gyq “ hpx, yq, where rgs˚ : H˚pGgx,gyq Ñ
H˚pGxyq is pullback by Adpgq.
‚ h has ﬁnite support modulo G, i.e. there is a ﬁnite subset T Ă G{U ˆ G{U such
that hpx, yq “ 0 if px, yq does not lie in the G-orbit of T .
DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS
13
The addition and S-module structure on H pG, Uq is deﬁned pointwise. The product is
given by the rule
(22)
h1 ˚ h2px, zq “
ÿ
yPG{U
h1px, yq
looomooon
H˚pGxyq
Y h2py, zq
looomooon
H˚pGyzq
where we give the right-hand side the following meaning: The cup product on the right
makes sense in H˚pGxyz, Sq, i.e. ﬁrst restrict h1 and h2 to H˚pGxyz, Sq, and take the cup
product there. Now split G{U as a disjoint union š Oi of orbits under Gxz; let O be one
such orbit. We regard
(23)
ÿ
yPO
h1px, yq Y h2py, zq :“ Cores
Gxy0z
Gxz
ph1px, y0q Y h2py0, zqq
where y0 P O is any representative, and the “trace” or corestriction is taken from Gxy0z to
Gxz; note that the right-hand side of (23) is independent of choice of y0 P O. Adding up
over orbits O gives the meaning of the right-hand side of (22).
Remark. Suppose that ∆is a compact subgroup of G that stabilizes every point of G{U.
In this case, we can restrict h to get a function h∆: G{U ˆG{U Ñ H˚p∆q. We also have
phh1q∆“ h∆h1
∆, where the right-hand multiplication is the more familiar
(24)
h∆h1
∆px, zq “
ÿ
yPG{U
h∆px, yq Y h1
∆py, zq.
2.4. Double coset description. Finally, we can describe H pG, Uq in terms of double
cosets UzG{U. For x P G{U let
Ux “ U X AdpgxqU
where gx P G represents x (that is to say, x “ gxUq. Then Ux is the stabilizer of x in U.
Fix a set of representatives rUzG{Us Ă G{U for the left U-orbits on G{U. Then we
have an isomorphism of S-modules
(25)
à
xPrUzG{Us
H˚pUx, Sq „
Ñ H pG, Uq
given thus: Fix a class z P rUzG{Us, and a representative gz P G for z – thus z “ gzU.
Let α P H˚pUz, Sq. Then the class of α P H˚pUz, Sq, considered as an element of the
left-hand side of (25), is carried to the function hz,α on G{U ˆ G{U characterized by the
following properties:
(i) hz,αpx, yq “ 0 unless px, yq belongs to the G-orbit of pz, eUq.
(ii) hz,α sends pz, eUq to α P H˚pUz, Sq – note that Uz is exactly the common stabi-
lizer of z and eU.
This gives another description of H pG, Uq. It is harder to directly describe the mul-
tiplication rule in this presentation, and we use instead the isomorphism to the previous
description. Later on we’ll describe explicitly the action of hz,α on the cohomology of an
arithmetic manifold.
Now let us examine the “size” of H pG, Uq; this discussion is really only motivational,
and so we will be a little informal. Suppose, for example, that G is split and U is hyperspe-
cial. In this case, the quotient UzG{U is parameterized by a dominant chamber X˚pAq`
inside the co-character group X˚pAq of a maximal split torus A. Moreover, if x P G{U
is a representative for a double coset parameterized by λ P X˚pAq, then the group Ux is,
14
AKSHAY VENKATESH
modulo a pro-p-subgroup, the Fv-points MλpFvq of the centralizer Mλ of λ. Thus we
obtain an isomorphism of S-modules:
H pG, Uq :“
à
λPX˚pAq`
H˚pMλpFvq, Sq
For “generic” λ – i.e., away from the walls of X˚pAq` – the group Mλ is a split torus; the
order of its Fv-points is a power of pqv ´ 1q. Thus if pqv ´ 1q is invertible on S, all the
terms of H pG, Uq corresponding to dominant λ vanish.
In this paper we will be primarily concerned with the case when qv ´ 1 “ 0 inside S.
Although it is certainly interesting to study H pG, Uq in general, the preceding discussion
shows that this case (i.e. qv “ 1 in S) is where H pG, Uq is “largest.”
2.5. Derived invariants. If M is any complex of G-modules, we may form the derived
invariants
derived U-invariants on M :“ HomSGpSrG{Us, Mq P DpModSq
where Hom is now derived Hom in the derived category of G-modules, taking values in
the derived category of S-modules.
Then the derived Hecke algebra automatically acts on the cohomology of the derived
invariants:
(26)
H pG, Uq
ý
H˚pderived U-invariants on Mq.
Indeed, the derived invariants are represented by the complex HomSGpP, Mq, where P
is as before any projective resolution of SrG{Us. The action of HomSGpP, Pq on this
complex furnishes the desired (right) action of H pG, Uq.
Let us describe the derived invariants in more familiar terms. Let V be as in (20), and
consider the explicit projective resolution P discussed in §2.2; we see that the derived
U-invariants are computed by the complex HomSUpQ, Mq. This coincides with U{V -
homomorphisms from Q to the termwise invariants M V ; since Q is a projective resolution
of S in the category of U{V -modules, we see that
(27)
derived U-invariants on M » HomSU{V pS, M V q P DpModSq.
where the right hand side is derived homomorphisms, in the derived category of U{V -
modules. In other words, there is an identiﬁcation
H˚pderived U-invariants on Mq » H˚pU{V, M V q,
the group hypercohomology of the ﬁnite group U{V acting on the complex of termwise
invariants M V .
2.6. Arithmetic manifolds. In the remainder of this section, we describe how the derived
Hecke algebras act on the cohomology of arithmetic manifolds.
We follow the notation of §1.8. In particular, we ﬁx K Ă GpAfq an open compact
subgroup, which we are supposing to have a product structure K “ ś
w Kw; let us split
this as
K “ Kpvq ˆ Kv
where Kpvq “ ś
w‰v Kw is the structure “away from v.” Associated to this is an arithmetic
manifold Y pKq, as in (17).
We will construct an action of the derived Hecke algebra Hv “ HvpGv, Kvq on the
cohomology of Y pKq. To do so, we will exhibit Y pKq as the derived Kv-invariants on a
suitable Gv-module, and then apply (26).
DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS
15
For Uv any open compact subgroup of Gv, let us abridge:
(28)
C˚pUvq “ cochain complex of Y pKpvq ˆ Uvq with S coefﬁcients.
Now let
M “ lim
ÝÑ
Uv
C˚pUvq.
where the limit is taken over open compact subgroups Uv ⩽Gv. Visibly, M is a complex
of smooth Gv-modules. Choosing Vv Ă Kv as in (20), we have
M Vv » C˚pVvq,
since we may interchange invariants and the direct limit; and then for a ﬁnite cover X Ñ Y
with Galois group D we have an isomorphism C˚pY q „
Ñ C˚pXqD. However, the derived
invariants of Kv{Vv on C˚pVvq “coincide with” the cohomology of Y pKq: the natural
map
C˚pY pKqq “ C˚pVvqKv{Vv Ñ HomSrKv{VvspS, C˚pVvqq
is a quasi-isomorphism, in the derived category of S-modules. This follows from the
fact that the terms C˚pVvq have no higher cohomology as Kv{Vv-modules, because each
CjpVvq is the module of S-valued functions on a free Kv{Vv-set and is in particular in-
duced from a representation of the trivial group.
We have exhibited a quasi-isomorphism
C˚pY pKqq » derived Kv-invariants on M
between C˚pY pKqq and a complex that represents the derived invariants of Kv acting on
M. Thus (26) gives a natural right action of H pGv, Kvq on the cohomology of Y pKq.
Remark. Although this is strictly a right action, we will often write it on the left, which con-
forms more to the usual notation for Hecke operators; the reader should therefore remem-
ber that the multiplication needs to be appropriately switched at times, but this will cause
almost no issue because the derived Hecke algebra will prove to be graded-commutative at
all the places we use.
Of course, this description is totally incomprehensible; thus we now work on translating
it to something more usable.
2.7. Digression: pullback from a congruence quotient. We ﬁrst need a brief digression
to construct certain cohomology classes on Y pKq. These are called “congruence classes”
in [10], because they capitulate in congruence covers of Y pKq.
There is a natural map
(29)
H˚pKv, Sq ÝÑ H˚pY pKq, Sq,
where, on the left, H˚pKv, Sq is the continuous cohomology of the proﬁnite group K with
coefﬁcients in (discretely topologized) S. Indeed, any cohomology class for H˚pKv, Sq
is inﬂated from a quotient Kv{Kv,1. Let K1 be the preimage of Kv,1 in K. The covering
Y pK1q Ñ Y pKq has deck group Kv{Kv,1, and thus gives rise to a map, well-deﬁned up
to homotopy,
(30)
Y pKq ÝÑ classifying space of Kv{Kv,1.
We may then pull back cohomology classes along this map to get (29).
These “congruence” cohomology classes have a very simple behavior under Hecke op-
erators:
16
AKSHAY VENKATESH
2.8. Lemma. Let h be in the image of the map (29). For any prime w of F that does
not divide the level of K or the size of S, such that GpFwq is split, and any usual Hecke
operator T supported at w, we have
T h “ degpT qh.
We will give a direct proof, but let us note that one can also deduce the result from the
commutativity of the Hecke algebra at w (which is proved, under mild restrictions on w, in
§3). It is also likely that the assumption that GpFvq is split is unnecessary (since w doesn’t
divide the level of K, it is automatically quasi-split by our deﬁnitions, which should be
enough for the argument below to go through).
Proof. It is easy to verify this if w ‰ v, so we examine only the case w “ v.
By the assumptions, we may suppose that Kv “ GpOvq, for a split reductive G over
Ov. Suppose that T arises from the double coset KvavKv, where, without loss, a lies in
a maximal split torus ApFvq that is in good position relative to Kv – i.e. it extends to a
maximal split torus of G.
We will show that h has the same pullback under the two natural maps
π1, π2 : Y pK X AdpavqKq Ñ Y pKq,
namely, the natural map, and the map induced by multiplication by av; this implies the
Lemma.
There is an isomorphism X˚pAq » Av{pAv X Kvq; let M be the centralizer in G of
the co-character in X˚pAq that corresponds to the class of a. Let K2 be the preimage,
under Kv Ñ GpOv{̟
D
v q, of MpOv{̟
D
v q; here D is a large enough integer, and̟
v a
uniformizer.
Then, on the one hand, the inclusion K2 ãÑ K X AdpavqK has index equal to a power
of qv. In particular, it induces an injection on H˚p´, Sq, so it is enough to verify that
π˚
1 h “ π˚
2 h after pullback under Y pK2q Ñ Y pK X AdpavqKq.
However, the pullback H˚pGpFvq, Sq Ñ H˚pKv, Sq is an isomorphism. The class h
is therefore actually pulled back from GpFvq. Our assertion then follows from the fact that
the natural maps K2 ÝÑ GpFvq – namely, the reduction map, and the conjugate of the
reduction map by av – actually coincide. This proves that π˚
1 h “ π˚
2 h, and concludes the
proof of the Lemma.
□
This motivates the following deﬁnition:
2.9. Deﬁnition. We say a class h P H˚pY pKq, Sq is Hecke-trivial if, for all places v that
do not divide the level of K and with residue characteristic invertible on S, and all Hecke
operators T supported at v,
pT ´ degpT qqnh “ 0.
for a sufﬁciently large integer n “ npT q. We denote by H˚pY pKq, Sqtriv the submodule
of Hecke–trivial classes.
2.10. Concrete expression for the action of Hv on H˚pY pKq, Sq. Let us now give a
more down-to-earth description of the action of Hv,S on H˚pY pKq, Sq, with notation as
above. In particular, we will show that the action of elements hz,α can be described in a
fashion that is very close to the usual deﬁnition of Hecke operators.
From z “ gzKv P Gv{Kv, and α P H˚pKv X AdpgzqKvq, we obtain a class hz,α P
H pGv, Kvq, by the recipe of §2.4. Then:
2.11. Lemma. Write
Kz “ K X AdpgzqK,
K1
z “ K X Adpg´1
z qK.
DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS
17
Also, let xαy be the image of α under H˚pKv X AdpgzqKvq
(29)
Ñ H˚pY pKzq, Sq. Then the
action of hz,α on H˚pY pKq, Sq coincides with the following composite
(31)
H˚pY pKqq
rgzs˚
Ñ H˚pY pKzqq
Yxαy
Ñ H˚pY pKzqq Ñ H˚pY pKqq,
where all cohomology is taken with S coefﬁcients, and the arrows are (respectively)
pullback by the map Y pKzq Ñ Y pKq induced by the map g ÞÑ ggz, cup with xαy, and
push-forward for the standard map Y pKzq Ñ Y pKq.
Note that this is almost exactly the same as a usual Hecke operator; we have just in-
serted the operation of Yxαy on the way. The fact that xαy is Hecke-trivial, in the sense
of Deﬁnition 2.9, is the key point that makes this operation commute with usual Hecke
operators.
Proof. Routine but extremely tedious; see §A.
□
Remark. Note also the following trivial case: taking gz “ 1, we see that the operation of
“cup with α P H˚pKv, Sq” always belongs to the derived Hecke algebra.
Remark. As an example let us write out the argument that derived Hecke operators at dif-
ferent places always commute with one another. Fix places v ‰ w, elements gv P Gv, gw P
Gw, and classes αv P H˚pKv X AdpgvqKvq and αw P H˚pKw X AdpgwqKwq. We claim
that the composite of the two associated derived Hecke operators can be described in the
following way, which makes graded commutativity clear: Push-pull aong
Y pKq Ð Y pKgv X Kgwq Ñ Y pKq,
but cup in the middle with the class of αvYαw. To verify this claim, examine the following
diagram:
(32)
Y pKgv X Kgwq
ˆgw
w♦♦♦♦♦♦♦♦♦♦♦
'❖
❖
❖
❖
❖
❖
❖
❖
❖
❖
❖
Y pKgvq
ˆgv
z✉✉✉✉✉✉✉✉✉
'❖
❖
❖
❖
❖
❖
❖
❖
❖
❖
❖
Y pKgwq
ˆgw
w♦♦♦♦♦♦♦♦♦♦♦
$❏
❏
❏
❏
❏
❏
❏
❏
❏
Y pKq
Y pKq
Y pKq
When we write (e.g.) ˆgv we mean that the map is induced by right multiplication by gv.
The composite of the derived Hecke operators is, by deﬁnition, obtained by going along
the bottom two rows. However, the middle diagram is a ﬁber product square, and so the
two ways of going from Y pKgvq to Y pKgwq, via “push-pull” or “pull-push,” coincide.
To prove the desired claim, then, it sufﬁces to show that the two pullbacks of the class
xαvy P H˚pY pKgvqq to H˚pY pKgv X Kgwqq – via the natural map, and via the map ˆgw
– actually coincide.
Equivalently, the classes obtained from αv, in the natural way on Y pKgv X gwKg´1
w q
and on Y pKgv X g´1
w Kgwq are in fact compatible, under the map ˆgw from one space to
the other. However, these cohomology classes are obtained from a certain covering of the
spaces, obtained by adding extra level at v, and the compatibility follows from the fact that
ˆgw lifts to these coverings.
18
AKSHAY VENKATESH
2.12. Change of coefﬁcients. Let us examine what happens under a change of rings
S Ñ S1. The description of §2.4 and the explicit action of §2.10 means that there is a
map of Hecke algebra Hv,S Ñ Hv,S1 compatible with the actions on H˚pY pKq, Sq Ñ
H˚pY pKq, S1q. However, this does not make quite clear that the change of rings map is
an algebra homomorphism. For completeness let us explain this now, since we will want
to freely pass between Z{ℓn coefﬁcients for various ns.
The tensor product bSS1 is a right exact functor from SG-modules to S1G modules
and so it can be derived to a map of derived categories. Note that this carries projectives to
projectives since HomS1GvpP bS S1, ´q “ HomSGvpP, ´q.
This derived tensor product (let us write it as b) “carries SrGv{Kvs to S1rGv{Kvs:” if
we choose a projective replacement P Ñ SrGv{Kvs the natural map
P bS S1 ÝÑ S1rGv{Kvs
is a quasi-isomorphism. Indeed it is possible to choose P so that each term of P is free
as an S-module (see the explicit resolution after (21)). Then P bS S1 has no cohomology
in higher degree (since this complex computes the TorSpSrGv{Kvs, S1q and the former is
free) and thus it is a resolution of S1rGv{Kvs.
This yields at once a map
Hv,S Ñ Hv,S1.
from the Hecke algebra with S coefﬁcients, to the same with S1 coefﬁcients. Explic-
itly, the left-hand side is represented by the cohomology of the differential graded algebra
HomSGpP, Pq, and this dga maps to HomS1GvpP bS S1, P bS S1q, whose cohomology
computes Hv,S1. This is the desired algebra map “change of coefﬁcients.”
Consider now the obvious map
ι : lim
ÝÑ
Uv
C˚pUvq Ñ lim
ÝÑ
Uv
C˚pUv; S1q,
where the notation is as in (28), and the right-hand side is deﬁned the same way but with
S1 coefﬁcients. This induces
ι1 : HomSGpP, lim
ÝÑ
Uv
C˚pUvqq Ñ HomS1G
˜
P bS S1,
˜
lim
ÝÑ
Uv
C˚pUv; S1q
¸¸
wherein we compose with ι and extend by S-linearity. There are compatible actions of
Hv,S and Hv,S1 on the left and right sides. On the other hand, the map ι1 induces on
cohomology the natural map H˚pY pKq, Sq Ñ H˚pY pKq, S1q.
To summarize: the actions of Hv,S on H˚pY pKq, Sq and Hv,S1 on H˚pY pKq, S1q
are compatible, with respect to the natural maps Hv,S Ñ Hv,S1 and H˚pY pKq, Sq Ñ
H˚pY pKq, S1q.
2.13. Passage from mod ℓn to ℓ-adic; the global derived Hecke algebra. We now write
out in grotesque detail certain minor details of the passage from mod ℓn to ℓ-adic coef-
ﬁcients, which will be used without comment in our later proofs. This section should
probably be skipped by the reader and consulted only as needed.
In what follows, we will describe the straightforward version of the global derived
Hecke algebra using all good primes for K that do not divide ℓ; here “good” is deﬁned
after (19). When we refer to the global derived Hecke algebra without any further remark,
we are always referring to this version.
We will remark, after the construction, how to
make a deﬁnition using a restricted set of primes.
DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS
19
The action of the derived Hecke algebra gives an algebra of endomorphisms rTn Ă
EndpH˚pY pKq, Z{ℓnqq, namely the algebra of endomorphisms generated by all the de-
rived Hecke algebras Hv,Z{ℓn where v varies over good primes of K that are not above
ℓ.
Now we have
H˚pY pKq, Zℓq “ lim
ÐÝ H˚pY pKq, Z{ℓnq
and we deﬁne the global derived algebra (relative to the ﬁxed set V of places) to be
(33)
˜T Ă EndpH˚pY pKq, Zℓqq
to be those endomorphisms of the form lim
ÐÝ tn, for some compatible system tn P ˜Tn, i.e.
tn “reduces to tm” for n ą m in the sense that the following diagram should commute:
(34)
H˚pY pKq, Z{ℓnq
tn
/

H˚pY pKq, Z{ℓnq

H˚pY pKq, Z{ℓmq
tm / H˚pY pKq, Z{ℓmq.
Let ˜T˚
n be the systems of elements ptn, tn´1, . . . , t1q, where tr P rTr for r ď n are
all compatible in the sense that the above diagram should commute for each tr, tr1. In
particular, ˜T˚
n acts on Z{ℓr-valued cohomology for each r ď n. The inverse limit lim
ÐÝ ˜T˚
n
acts on H˚pY pKq, Zℓq, and its image in EndH˚pY pKq, Zℓq is precisely the global derived
Hecke algebra ˜T.
Fix m. For n ě m consider the map
˜T˚
n Ñ ˜T˚
m.
For increasing n and ﬁxed m, the image of this map gives a decreasing sequence of subsets
of the ﬁnite set ˜T˚
m. This sequence must stabilize. Call this stabilization ˜T8,m; it is a
subring of rT˚
m and thus acts by endomorphisms of H˚pY pKq, Z{ℓmq; also, there exists
Nm such that ˜T8,m coincides with the image of ˜T˚
Nm in ˜T˚
m.
The natural map
(35)
lim
ÐÝ ˜T˚
n Ñ ˜T8,m
is onto, since we’re dealing with an inverse system of ﬁnite sets.
Let Hv,Z{ℓn be the local derived Hecke algebra at v with Z{ℓn-coefﬁcients. We show
later (§3.4) that, if ℓn divides qv ´ 1, then the natural map Hv,Z{ℓn Ñ Hv,Z{ℓm is sur-
jective. It follows that if qv ´ 1 is divisible by ℓNm, then the image of ˜T˚
Nm acting on
H˚pY pKq, Z{ℓmq contains the image of Hv,Z{ℓm. Therefore, the image of ˜T8,m acting
on H˚pY pKq, Z{ℓmq contains the image of Hv,Z{ℓm.
In practice, we will establish “bigness” results of the following type:
(*) For all m ď n, there exists sets of primes Qn “ tq1, . . . , qru such that
ℓn divides qi´1 and the image of biHqi,Z{ℓm acting on H˚pY pKq, Z{ℓmq
is “large:” H˚pY pKq, Z{ℓmq is generated over biHqi,Z{ℓm by elements
of some ﬁxed degree D.
When we prove such results, it will not be for the full cohomology of Y pKq but rather
for its localization at some ideal of the Hecke algebra, but we suppress that for the current
discussion.
20
AKSHAY VENKATESH
Let us prove that, under this assumption (*), H˚pY pKq, Zℓq is generated over ˜T by
elements of degree D. The assumption implies (by the previous discussion, with n “ Nm)
that H˚pY pKq, Z{ℓmq is generated over ˜T8,m by elements of degree D; by (35), it is also
generated over lim
ÐÝ ˜T˚
n by elements of degree D. That is to say,
plim
ÐÝ ˜T˚
nq b HDpY pKq, Z{ℓmq
surjects onto H˚pY pKq, Z{ℓmq for every m. By a compactness argument the same asser-
tion holds with Zℓ-coefﬁcients.
More generally, the same type of argument allows us to show that various types of
“largeness” can be passed from Z{ℓm coefﬁcients to Zℓ.
2.14. Restricting places and the strict global derived Hecke algebra. We can restrict
the primes and the powers of ℓused in the above construction. It is convenient to index
these restrictions by a function
V : primes ÝÑ t0, 1, 2, . . ., u Y t8u
where primes v with V pvq “ 0 will be not used at all in the deﬁnition.
In the above construction, replace rTn by the algebra generated by Hv,Z{ℓn where n ď
V pvq. Proceeding as above, then, we obtain a restricted global Hecke algebra ˜TpV q acting
on cohomology with Zℓcoefﬁcients. Informally, each prime v can be used at most at
torsion level Z{ℓV pvq.
For example, taking
(36)
V0pvq “
#
0, v not good;
largest power of ℓdividing qv ´ 1, else
,
the resulting algebra ˜TpV0q has the advantage that it will be graded commutative by the
results of §3, at least if ℓdoesn’t divide the order of the Weyl group.
It will be sometimes convenient to enlarge this by the usual Hecke algebra, i.e. deﬁning
the “strict” global derived Hecke algebra
˜T1 :“ algebra generated by ˜TpV0q and all underived Hecke operators at good places prime to ℓ.
However, by default, when we write ˜T, we mean the “full” version using V “ 8 for
all good primes not above ℓ, and V “ 0 at all other primes. Thus we have inclusions of
algebras, each inside endomorphisms of cohomology:
usual (underived) Hecke algebra T Ă ˜T1 Ă ˜T.
The advantage of ˜T1 is that it is clearly graded commutative.
Thus, for example, if m is a maximal ideal of T, the strict global derived Hecke algebra
˜T1 induces an algebra of endomorphisms of the m-completion H˚pY pKq, Zℓqm:
H˚pY pKq, Zℓqm b ˜T1 ÝÑ H˚pY pKq, Zℓqm.
While a priori we do not know that the full ˜T preserves H˚pY pKq, Zℓqm, this is true under
a mild additional assumption: For each good place w not equal to ℓ, let Tpwq be the prime-
to-w usual Hecke algebra, and mpwq the induced maximal ideal. Suppose that the natural
map
(37)
H˚pY pKq, Zℓqmpwq Ñ H˚pY pKq, Zℓqm
is an isomorphism. This is true, for example, if there exists Galois representations associ-
ated to cohomology classes (by the argument of [20, Lemma 6.20]). In this case, the local
DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS
21
derived Hecke algebra at w clearly preserves the left-hand side, and so also preserves the
right-hand side. Since this is true for all good w not dividing ℓ, the full ˜T also preserves
the m-completion of cohomology.
