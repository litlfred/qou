---
doc_id: arxiv-1608.07234v3
doc_title: "DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS"
section_id: sec-009-appendix-a-remedial-algebra
section_title: "Appendix A. Remedial algebra"
section_number: null
pages: 76-82
source_pdf: 1608.07234v3.pdf
source_sha256: 311730670d2fdcb7
toc_source: outline
doc_brief: "DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS — We describe a graded extension of the usual Hecke algebra: it acts in a graded fashion on the cohomology of an arithmetic group Γ."
---
In this section we ﬁll in some “intuitively obvious” claims in the text in grotesque detail,
in particular the identiﬁcations between various different models of the derived Hecke
algebra. (The word “remedial” in the title of this section refers to my own lack of ﬂuency
with homological algebra.)
An action of a topological group will be called smooth if the stabilizer of every point
is an open subgroup. We will ﬁx a ﬁnite ring S of cardinality prime to p. A “smooth
representation of G”, in this section, will be a smooth action of G on an S-module. We
write SG (or occasionally SrGs when typography requires) for the group algebra of G with
coefﬁcients in S. We will write HomSG for homomorphisms of SG-modules; in §A.11
we abbreviate this to HomG because other notation becomes very dense.
Note that the usage of U and K in this section do not precisely match their usage in the
main text.
A.1.
Let K be a proﬁnite group, which admits a pro-p open normal compact subgroup
U. Then the category C of smooth representations of K is an abelian category with enough
projectives. In fact, if Q is a projective K{U module, then considering Q as a smooth
K-module ˜Q it remains projective: HomSKp ˜Q, V q “ HomSrK{UspQ, V Uq and V ÞÑ V U
is exact by the hypothesis on U. (One can lift U-invariants under a surjection V1 ։ V2 by
averaging.)
In this situation, restriction to a ﬁnite index subgroup K1 Ă K preserves projectivity.
Indeed HomSK1pResK
K1A, Bq “ HomSKpA, IndK
K1Bq and the induction functor is exact.
A.2.
Now let G “ Gv be the points of a reductive group over a p-adic ﬁeld, or any
open subgroup thereof. Then the category of smooth representations of Gv is an abelian
category and it has enough projectives.
Indeed, consider W “ SrG{Us for an open pro-p compact U Ă G. Then
HomSGpW, V q » V U,
which is obviously exact in V . So W is projective, and now given any other V we choose
generators vi for V , open pro-p compact subgroups Ui ﬁxing vi, corresponding projectives
Wi, and then get À Wi ։ V .
Throughout the remainder of this section, we suppose that G is as above, that K is an
open compact subgroup of G (in particular, K is proﬁnite), and that U Ă K is a pro-p
open normal compact subgroup of K.
A.3.
Fix a resolution of the trivial K-representation by projective smooth K-modules:
(173)
Q : ¨ ¨ ¨ Ñ Qi Ñ ¨ ¨ ¨ Ñ Q1 Ñ S.
(Here, and in what follows, we will use boldface letters to denote complexes.)
To be
explicit, let us take Q to be the standard “bar” resolution of S by free SrK{Us-modules,
considered as a complex of smooth K-representations.
Then HompQ, Qq computes H˚pK, Sq, the continuous cohomology of the proﬁnite
group K with S coefﬁcients: indeed, the the cohomology of HompQ, Qq is identiﬁed with
H˚pK{U, Sq, which is identiﬁed by pullback with the continuous cohomology H˚pK, Sq.
DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS
77
The complex HompQ, Qq has the structure of differential graded algebra arising from
composition, and the resulting multiplication on H˚pK, Sq coincides with the cup product
(this reduces to a corresponding statement for a ﬁnite group; for that see [37]).
If K1 Ă K is a ﬁnite index subgroup, then HomSK1pQ, Qq still computes H˚pK1, Sq
(see remarks above). Moreover, the averaging operator ř
K{K1 – that is to say, the map
sending
f P HomSK1pQ, Qq ÞÑ
ÿ
κ
κfκ´1 P HomSKp. . . q
realizes the corestriction map H˚pK1, Sq Ñ H˚pK, Sq, where the κ sum is taken over a
set of coset representatives for K{K1 in K.
A.4. Induction and Frobenius reciprocity. We use the word “induction” for the functor
from K-modules to G modules
(174)
M ⇝SG bSK M.
This is isomorphic to the usual “compact” induction, namely space of functions
indG
KpMq
:“
tf : G Ñ M : fpgkq “ k´1fpgq,
(175)
f is supported on ﬁnitely many left translates of Ku
where the action of h P G is by left translation, i.e. lhfpxq “ fph´1xq. We will drop the
word “compact” and simply refer to (175) or (174) as “induction”; we refer to the model
(175) for induction as the “function model.”
We can deﬁne inverse isomorphisms between (175) and (174) as follows: deﬁne indG
KpMq Ñ
SrGs bSrKs M via
f ÞÑ
ÿ
xPpG{Kq
gx b fpgxq,
where gx P G is a representative for x P G{K; in the other direction, we send g bm to the
function supported on gK whose value on g equals m
A.5. Frobenius reciprocity. We have Frobenius reciprocity
HomSGpindG
K M, Nq » HomSKpM, Nq
and therefore induction carries projective K-modules to projective G-modules. Explicitly
an SK-homomorphism f : M Ñ N is sent to its obvious G-linear extension SG bSK
M Ñ N.
If G Ą K has ﬁnite index, we also have the reverse adjointness (since “compact induc-
tion” and “induction” coincide): to give a K-map f : M Ñ M 1 is the same as giving a
map Ff : M Ñ indG
KM 1. Explicitly, in the function model for the induced representation,
Ff is characterized by the property Ffpmqpeq “ fpmq, and so
Ffpmqpgq “ lg´1Ffpmqpeq “ Ffpg´1mqpeq “ fpg´1mq
and thus in the tensor product model
(176)
Ffpmq “
ÿ
xPpG{Kq
gx b fpg´1
x mq
78
AKSHAY VENKATESH
A.6. Restriction of induced representations. Let Q be a smooth representation of K.
The restriction of indG
KQ to K is isomorphic to
(177)
à
xPKzG{K
SrKgxKs bSK Q »
à
K
SrKs bSKx Qx »
à
x
indK
KxQx
where x “ gxK runs through a set of representatives for K-orbits on G{K, and we write
Kx “ K X gxKg´1
x ; moreover for a K-module Q, we denote by Qx the Kx-module
whose underlying space is Q, but for which the action ˚ of Kx on Q is deﬁned thus:
(178)
κ ˚ q “
`
Adpg´1
x qκ
˘
q.
The ﬁrst map of (177) is given explicitly by
(179)
k1gxk2 b q “ k1gx b k2q ÞÑ k1 b k2q
and the inverse map sends
(180)
k b q ÞÑ kgx b q.
In the function model of the induced representations, the composite map of (177) sends
F : KgxK Ñ Q to the function F 1 : k ÞÑ Fpkgxq. In the reverse direction, given a
function F 1 in the function model of indK
KxQx, the inverse of (177) sends it to
(181)
ÿ
kPK{Kx
kgx b fpkq P SrKgxKs bSK Q.
A.7. Derived Hecke algebra. The derived Hecke algebra for the pair pG, Kq with coef-
ﬁcients in S is deﬁned as
à
i
Exti
SGpSrG{Ks, SrG{Ksq
where the Ext-groups are taken in the category of smooth S-representations.
We can construct an explicit model as follows. Let Q be as in (173). Then P “ indQ
is a projective resolution of SrG{Ks. In particular, HomSGpP, Pq has the structure of a
differential graded algebra and its cohomology gives the derived Hecke algebra.
A.8.
We will now explicitly describe the isomorphism (25) between the derived Hecke
algebra and its “double coset model.”
Let P, Q be as in §A.7.
We have
(182)
HomSGpP, Pq “ HomSKpQ, indG
KQq
(177)
ÐÝ
à
xPKzG{K
HomSKpQ, indK
KxQxq
looooooooooooooooooomooooooooooooooooooon
“HomSKxpQ,Qxq
,
where x varies now through KzG{K, again gxK is a representative for x and Kx “
K X AdpgxqK, and the twist operation Qx is as described in (178).
Note that the last map induces a cohomology isomorphism. We must see that H˚pHomSKpQ, ´qq
commutes with the inﬁnite direct sum À
x indK
KxQx. However, Qx is cohomologically
concentrated in degree 0, and so the same is true for indK
KxQx; it is enough to show, then,
for any K-modules Mi, the obvious map
à
i
HomSKpQ, Miq ÝÑ HomSKpQ,
à
i
Miqq
is a quasi-isomorphism. But this follows from the fact that taking U invariants commutes
with inﬁnite direct sum, as does the functor H˚pK{U, ´q.
DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS
79
Note that the cohomology of HomSKxpQ, Qxq is identiﬁed with H˚pKx, Sq, because
Q and Qx are resolutions of S, and moreover Q is a complex of projective Kx-modules.
Thus, (182) gives rise to an isomorphism:
(183)
H˚ pHomSGpP, Pqq »
à
x
H˚pKx, Sq.
For later use, we explicate the map of (182), going from right to left: An element f P
HomSKxpQ, Qxq must satisfy fpκqq “ pg´1
x κgxqfpqq for κ P Kx; the associated element
of HomSKpQ, indG
KQq is given in the tensor product model of the induced representation
by the formula of (176):
q P Q ÞÑ
ÿ
kPK{Kx
kgx b fpk´1qq
which is well-deﬁned.
A.9. Action of derived Hecke algebra on derived invariants. Now suppose that M
is a complex of smooth G-representations. There is a natural action of EndSGpPq on
HomSGpP, Mq. Moreover, the latter complex computes the hypercohomologyH˚pK, Mq
of K with coefﬁcients in the complex M.
Thus, because of (183), we get an action of H˚pKx, Sq on H˚pK, Mq. Let us de-
scribe the action of hx P H˚pKx, Sq on H˚pK, Mq as explicitly as possible, in particular
justifying the claims of §2.10:
A.10. Lemma. With notation as above, the action of hx is given by the following compos-
ite:
H˚pK, Mq
Adpg´1
x q˚
ÝÑ
H˚pKx, Mxq
mÞÑgxm
ÝÑ
H˚pKx, Mq Yhx
ÝÑ H˚pKx, Mq Cores
ÝÑ H˚pK, Mq.
Here the ﬁrst map is the pull-back induced by Adpg´1
x q : Kx ãÑ K, which pulls back M
to Mx.
Proof. Choose h1
x P HomSKpQ, indK
KxQxq representing hx. For f P HomSGpP, Mq we
denote by fx P HomSKpindK
KxQx, Mq the restriction. We denote by rh1
xs P HomSKxpQ, Qxq
and rfxs P HomSKxpQx, Mq the elements obtained from h1
x, fx using Frobenius reci-
procity (but using the two different versions of Frobenius reciprocity).
We want to compare the composition fx ˝ h1
x and rfxs ˝ rh1
xs i.e.
(184)
h1
x P HomSKpQ, indK
KxQxq
ˆ
fx P HomSKpindK
KxQx, Mq
/ HomSKpQ, Mq
rh1
xs P HomSKxpQ, Qxq
„
O
ˆ
rfxs P HomSKxpQx, Mq
/
„
O
HomSKxpQ, Mq
We compute
fx ˝ h1
xpqq
(176)
“ fx
¨
˝
ÿ
kiPK{Kx
ki b rh1
xspk´1
i
qq
˛
‚“
ÿ
ki
kirfxs ˝ rh1
xspk´1
i
qq
i.e., this is what we get by averaging rfxs˝rh1
xs over the action of K{Kx. The cohomology
class of the composition rfxs ˝ rh1
xs simply amounts (at the level of cohomology) to the
cup product of the class rfxs P H˚pKx, Mq (hypercohomology) with the class rh1
xs P
H˚pKx, Sq. So to prove the lemma it remains to show:
80
AKSHAY VENKATESH
Subclaim: The class rfxs P H˚pKx, Mq is obtained from rfs P H˚pK, Mq via
H˚pK, Mq
Adpg´1
x q˚
ÝÑ
H˚pKx, Mxq
mÞÑgxm
ÝÑ
H˚pKx, Mq
At the chain level this map is given by the composite
HomSKpQ, Mq Ñ HomSKxpQx, Mxq Ñ HomSKxpQx, Mq
where the ﬁrst map is the trivial map, just considering maps of K modules as Kx-modules
via Adpg´1
x q : Kx Ñ K; and the second map Mx Ñ M is given by m ÞÑ gxm. To
check the subclaim, note that rfxs P HomSKxpQx, Mq sends q P Qx to the value of fx
on the element 1 b q P indK
KxQ, which is carried by the isomorphism inverse to (177) to
gx b q P indG
KQ; thus,
rfxs : q ÞÑ gxfpqq
where here, on the right hand side, we regard f as a map Q Ñ M by Frobenius reciprocity
(i.e. we pull it back via the obvious embedding Q ãÑ P, q ÞÑ 1 b q). This concludes the
justiﬁcation of the subclaim.
□
A.11. Multiplication in the derived Hecke algebra. We ﬁnally analyze composition (i.e.
multiplication) in the derived Hecke algebra, explicating it with respect to the isomorphism
(183), and thus justifying the description given in §2.3.
Let α, β, γ P G{K with representatives gα, gβ, gγ P G. Suppose given hα P H˚pKgαq
and similarly for β. We will compute the product hβhα considered as elements of the
derived Hecke algebra – or more precisely the H˚pKgγq component of their product.
As in (182) we represent hα by an element h1
α P HomKpQ, indG
KQq, and denote by
rh1
αs the corresponding element of HomKgαpQ, Qgαq and similarly for hβ. By (176) we
have the explicit formula
h1
α : q P Q ÞÑ
ÿ
kPK{Kα
kgα b rh1
αspk´1qq P SrKgαKs bSK Q,
where we make a modest abuse of notation by identifying K{Kα to a set of representatives
for it in K. Now apply h1
β to the right-hand side, regarding h1
β P HomSGpP, Pq. The result
is:
(185)
ÿ
kPK{Kα
ÿ
k1PK{Kβ
kgαk1gβ b rh1
βsk1´1rh1
αsk´1 P HomKpQ, SG bSK Qq
The desired H˚pKgγq component of the product hβ ¨ hα is given by considering all k, k1
for which kgαk1gβ P KgγK, i.e. it is represented by
(186)
ÿ
kgαk1gβPKgγK
kgαk1gβ b rh1
βsk1´1rh1
αsk´1 P HomKpQ, SrKgγKs bSK Qq
By “dual” Frobenius reciprocity (see before (176)) the right-hand side can be identiﬁed
with HomKpQ, indK
KγQγq » HomKγpQ, Qγq. If we write kgαk1gβ “ k1gγk2, an ex-
plicit formula for the corresponding element of HomKpQ, indK
KγQγq is given (179) by
q ÞÑ
ÿ
kgαk1gβ“k1gγk2
k1 b k2rh1
βsk1´1rh1
αsk´1pqq
loooooooooooooooomoooooooooooooooon
PSKbSKγ Qγ
where the right-hand sum is over the same k, k1 as before, and we consider only those k, k1
such that kgαk1gβ P KgγK. Then the corresponding element of HomKγpQ, Qγq is given
(see (176)) by picking out those terms for which k1 P Kγ; in that case we can rewrite
DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS
81
k1gγk2 “ gγpAdpgγq´1k1qk2 and so we may as well suppose that k1 “ 1. Thus, the
desired result is
(187)
ÿ
k,k1:kgαk1gβ“gγk2
k2
rh1
βsk1´1
looomooon
HomKAdpkgαqKk1gβ
pQkgα ,Qkgαk1gβ q
rh1
αsk´1
looomooon
HomKkgα pQ,Qkgα q
P HomKγpQ, Qγq
Here we observed that
rh1
αs˝k´1 P HomKkgα pQ, Qkgαq, rh1
βs˝k1´1 P HomKk1gβ pQ, Qk1gβq » HomAdpgqKk1gβ pQg, Qgk1gβq
(the last isomorphism is the obvious one and we apply it to g “ kgα). 20 Returning to
(187), set
x “ kgαk1gβK “ gγK, y “ kgαK, z “ eK, U “ stabilizerpx, y, zq
Then x, y are in relative position β, and y, z are in relative position α, and x, z are in
relative position γ.
Note also that
U “ Kkgα X AdpkgαqKk1gβ “ K X AdpkgαqK X Adpkgαk1gβqK.
Therefore, the composite occurring in (187)
F “
HomKAdpkgαqKk1gβ
pQkgα ,Qkgαk1gβ q
hkkkikkkj
rh1
βsk1´1
˝
rh1
αsk´1
looomooon
HomKgα pQ,Qkgα q
actually belongs to HomUpQ, Qkgαk1gβq; as such F deﬁnes a cohomology class for U.
This cohomology class is given by taking the classes hα, hβ, transporting them to classes in
H˚pKkgαq and H˚pAdpkgαqK1
k1gβq, by means of Adpkq : Kgα » Kkgα and Adpkgαk1q :
Kβ » AdpkgαqK1
k1gβ, restricting to U, and taking the cup product.
Said differently, let us think of hα as a G-invariant association Hα from pairs pu, vq P
G{K ˆ G{K to cohomology classes in H˚pGuvq – the one whose value at pgαK, eq is
given by the original cohomology class in H˚pKgαq. Similarly for hβ. Then,
cohomology class of F “ Hβpx, yq Y Hαpy, zq P H˚pGxyzq
Now Kγ “ Gxz acts on the set of pk, k1, k2q as above, i.e. satisfying kgαk1gβ “ gγk2,
via
κ : pk, k1, k2q ÞÑ pκk, k1, Adpg´1
γ qκk2q.
For ﬁxed pk, k1, k2q the stabilizer of this Kγ-action is just U. The contribution of a single
Kγ-orbit is given by
ÿ
κPKγ{U
Adpg´1
γ qκ ˝ F ˝ κ´1
which is to say that it averages F, considered as an element of HompQ, Qγq, over the
cosets of Kγ{U. (The Adg´1
γ
accounts for the twisted action on Qγ). This precisely
realizes the corestriction from U to Kγ.
20For example, to check the ﬁrst, note that for z P Kkgα and q P Q we have
rh1
αs ˝ k´1pzqq “ rh1
αs
`
pk´1zkqpk´1qq
˘
“ pg´1
α k´1zkgαqrh1
αs ˝ k´1pqq
Indeed, rh1
αs represents the class in H˚pKkgαq, obtained by applying Adpkq to the class hα P H˚pKgαq.
82
AKSHAY VENKATESH
In summary, we have recovered the description of multiplication in the derived Hecke
algebra given in §2.3.
