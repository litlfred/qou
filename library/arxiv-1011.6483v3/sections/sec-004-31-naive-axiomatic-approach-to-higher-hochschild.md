---
doc_id: arxiv-1011.6483v3
doc_title: "DERIVED HIGHER HOCHSCHILD HOMOLOGY"
section_id: sec-004-31-naive-axiomatic-approach-to-higher-hochschild
section_title: "Naive axiomatic approach to higher Hochschild homology"
section_number: 3.1
pages: 10-22
source_pdf: 1011.6483v3.pdf
source_sha256: 7a425e51860c37a4
doc_brief: "DERIVED HIGHER HOCHSCHILD HOMOLOGY — W e study the higher Hochschild chain functor, factorizatio n alge- bras and their relationship with topological chiral homolo gy."
---
recall the standard construction of chain complexes computing hig her Hochschild
homology (also called Hochschild homology over spaces) following [30, 1 3]. The
higher Hochschild complex is a functor CH :sSet×CDGA→CDGA. This func-
tor is deﬁned as follows: the tensor products A⊗B of two CDGAs has an natural
structure of CDGA(in other words, CDGA has a symmetric monoidal structure
canonically induced by the underlying tensor product of chain comple xes). Fur-
thermore, the multiplication A⊗A→ A is an algebra homomorphism since A
is commutative. It follows that a CDGA can be thought of a strict symmetric
DERIVED HIGHER HOCHSCHILD, TCH, F ACTORIZATION ALGEBRAS 11
monoidal functor from the category of ﬁnite sets with disjoint unio n to the cate-
gory of chain complexes (whose value on a ﬁnite set J is given by A⊗J ), which can
be extended to the category of all sets by taking colimits. Given a sim plicial set
X•, thought of as a functor ∆ op→ sSet, compose these two functors to obtain a
simplicial complex X•↦→A⊗X• . The total complex (that is the geometric real-
ization
⏐⏐A⊗X•
⏐⏐) of this simplicial complex is, by deﬁnition, CH •
X• (A,A ). In more
details, we get the following explicit deﬁnitions.
Deﬁnition 2. First let Y• : ∆ op→S ets∗ be a ﬁnite pointed simplicial set, and
for k ≥ 0, we set yk := Yk−{∗} to be the complement of the base point in
Yk. Furthermore, let ( A = ⨁
i∈ZAi,d, •) be a diﬀerential graded, associative,
commutative algebra, and ( M = ⨁
i∈ZMi,dM ) a diﬀerential graded module over
A (viewed as a symmetric bimodule). Then, the Hochschild chain complex of
A with values in M overY• is deﬁned as 2CH •
Y•(A,M ) := ⨁
n∈ZCHn
Y• (A,M ),
where
CHn
Y•(A,M ) :=
⨁
k≥0
(M⊗A⊗yk )n+k
is given by a sum of elements of total degree n +k. In order to deﬁne a diﬀerential
D onCH •
Y• (A,M ), we deﬁne morphisms di :Yk→Yk−1, for i = 0,...,k as follows.
First note that for any map f :Yk→Yl of pointed sets, and for m⊗a1⊗···⊗ ayk∈
M⊗A⊗yk , we denote by f∗ :M⊗A⊗yk→M⊗A⊗yl,
(1) f∗(m⊗a1⊗···⊗ ayk ) = (−1)ǫn⊗b1⊗···⊗ byl,
where bj = ∏
i∈f −1(j)ai (or bj = 1 if f −1(j) = ∅) for j = 0,...,y l, and n =
m•
∏
i∈f −1(basepoint),i⁄=basepointai. The sign ǫ in equation (1) is determined by the
usual Koszul sign rule of (−1)|x|•|y| wheneverx moves acrossy. In particular, there
are induced boundaries ( di)∗ : CHk
Y• (A,M )→ CHk−1
Y• (A,M ) and degeneracies
(sj)∗ :CHk
Y• (A,M )→CHk+1
Y• (A,M ), which we denote by abuse of notation again
bydi andsj. Using these, the diﬀerential D :CH •
Y•(A,A )→CH •
Y•(A,A ) is deﬁned
by letting D(a0⊗a1⊗···⊗ ayk ) be equal to
yk∑
i=0
(−1)k+ǫia0⊗···⊗ d(ai)⊗···⊗ ayk +
k∑
i=0
(−1)idi(a0⊗···⊗ ayk ),
where ǫi is again given by the Koszul sign rule, i.e., (−1)ǫi = (−1)|a0|+···+|ai−1|.
The simplicial conditions on di imply that D2 = 0.
If Y• : ∆ op → Sets is a ﬁnite (not necessarily pointed) simplicial set, we
may still deﬁne CH •
Y• (A) := ⨁
n∈ZCHn
Y• (A,A ) via the same formula as above,
CHn
Y•(A,A ) := ⨁
k≥0(A⊗A⊗yk )n+k. Formula (1) again induces boundaries di and
degeneracies si, which produce a diﬀerential D of square zero on CH •
Y• (A,A ) as
above.
If Y• is any simplicial set we deﬁne
CH •
Y• (A,M ) := lim−→
K• → Y•,
K• ﬁnite
CH •
K•(A,M )
2W e recall that we are using a cohomological type grading for o ur diﬀerential graded modules,
see Convention (7) on page 7, hence the upper index n. Note that, nowhere in this paper will we
consider Hochschild cochains.
12 G. GINOT, T. TRADLER, AND M. ZEINALIAN
as the colimit over all ﬁnite simplicial sets. If Y• is ﬁnite, then this deﬁnition agrees
with the previous ones thanks to the Yoneda lemma.
Remark 2. Note that due to our grading convention, if A is non graded, or con-
centrated in degree 0, then HHY•• (A,A ) is concentrated in non positive degrees. In
particular, our grading is opposite of the one in [21].
Note that the equation (1) also makes sense for any map of simplicial pointed sets
f :Xk→Yk. Since A is graded commutative and M symmetric, (f◦g)∗ =f∗◦g∗,
henceY•↦→CH •
Y• (A,M ) is a functor from the category of ﬁnite pointed simplicial
sets to the category of simplicial k-vector spaces, see [30]. If M = A, CH •
Y• (A)
is a functor from the category of ﬁnite simplicial sets to the catego ry of simplicial
k-algebras.
Now note that any map g : A→ B of CDGAs and any maps of modules ρ :
M → N over g : A→ B, i.e. ρ(am) = g(a)ρ(m), induces a map CH •
Y•(g,ρ ) :
CH •
Y•(A,M )→CH •
Y•(B,N ) of simplicial vector spaces.
The chain complex
(
CH •
Y• (A),D
)
inherits a structure of (diﬀerential graded)
algebra. This is a formal consequence of the fact that CH •
Y• (A) is a simplicial
commutative algebra. Indeed, given two simplicial vector spaces V• and W•, one
deﬁnes a simplicial structure on the simplicial space ( V×W )k := Vk⊗Wk using
the boundaries dV
i ⊗dW
i and degeneracies sV
i ⊗sW
i . The shuﬄe product is (the
collection of) maps sh :Vp⊗Wq→ (V×W )p+q deﬁned by
sh(v⊗w) =
∑
(µ,ν)
sgn(µ,ν )(sνq...s ν1 (v)⊗sµp...s µ1 (w)),
where (µ,ν ) denotes a (p,q )-shuﬄe, i.e. a permutation of{0,...,p +q−1} mapping
0≤ j≤ p− 1 to µj+1 and p≤ j≤ p +q− 1 to νj−p+1, such that µ1 <··· < µp
and ν1<··· <ν q.
SinceCH •
Y• (A,M ) is a simplicial vector space, we obtain an induced shuﬄe map
sh :CH •
Yp (A,M )⊗CH •
Yq (B,N )→CH •
Yp+q (A⊗B,M ⊗N ) for any CDGAs A,B
and modules M,N . Now, since A is a CDGA, the multiplication µ :A⊗A→A is
an algebra map, and the map ν : M⊗A→ M a map of A-modules. Composing
these maps with the shuﬄe products we obtain the multiplication
shY• :CH •
Y• (A,M )⊗CH •
Y• (A)
sh
→CH •
Y•(A⊗A,M⊗A)
CH •
Y• (µ,ν)
−→ CH •
Y•(A,M ).
Proposition 1. The multiplicationshY• makesCH •
Y• (A) a diﬀerential graded com-
mutative algebra and CH •
Y•(A,M ) a DG-module over CH •
Y• (A), which are natural
in A and M .
Proof. The proof of the algebra structure is given in [13, Proposition 2.4.2] and the
proof of the module structure is the same. □
Note that CH •
pt•(A) is the (chain complex associated to the) constant sim-
plicial CDGA A. In particular there is a canonical quasi-isomorphism η : A =
CH •
pt0
(A)→ CH •
pt•(A) splitting the augmentation map CH •
pt•(A)→ CH •
pt0
(A).
It follows from Proposition 1 above that if X• is a pointed simplicial set, the canon-
ical map pt•→X• induces a natural A-module structure on CH •
X• (A,M ) (and an
A-algebra structure on CH •
X• (A)). In other words, CH •
X• (A,M ) is naturally an
A-module.
Summing up the previous discussion and proposition we obtain:
DERIVED HIGHER HOCHSCHILD, TCH, F ACTORIZATION ALGEBRAS 13
Corollary 1. The rule (Y•,A )↦→(CH •
Y• (A),D,sh Y• ) is a functor CH : sSet×
CDGA → CDGA. Similarly, the rule (Y•,M ) ↦→(CH •
Y• (A,M ),D,sh Y•) is a
functor CH :sSet∗×A-Mod→A-Mod .
Deﬁnition 3. The Hochschild homology of a CDGA A over a simplicial set X• is
the cohomology 3 HH •
X• (A) = H •(CH •
X• (A),D ) of the CDGA ( CH •
X• (A),D,sh )
as a commutative graded algebra.
Further if X• is pointed and M is an A-module, the Hochschild homology of A
with value in M overX• is the homology HH •
X• (A,M ) = H ∗(CH •
X• (A,M ),D ) as
a graded module over HH •
X•(A).
Now letX be a topological space, we deﬁne the Hochschild homology of a CDGA
A overX to be HH •
S•(X)(A) where
S•(X) = Map (∆ •,X )
is the singular simplicial set of X. If X is pointed, then S•(X) is a pointed simplicial
set and we deﬁne the Hochschild homology of a CDGAA with value in anA-module
M overX to be HH •
S•(X)(A,M ).
The Hochschild chain functor satisﬁes the following properties which allows to
build explicitly and easily these chain complexes out of other simplicial sets and do
computations (for instance, see [30, 12, 13]).
Proposition 2 (Tensor Products of CDGAs and disjoint union of simplicial sets) .
LetA,B be two CDGAs. For any X•∈sSet, there is a canonical isomorphism
CH •
X• (A⊗B)∼=CH •
X• (A)⊗CH •
X• (B)
of CDGAs. Further for any simplicial set Y•, one has a natural isomorphism
CH •
X•
∐ Y•(A)∼=CH •
X• (A)⊗CH •
Y• (A)
of CDGAs and a natural isomorphism of modules
CH •
X•
∐ Y• (A,M )∼=CH •
X• (A,M )⊗CH •
Y• (A)
if X• is a pointed simplicial set.
Proof. It follows from the canonical isomorphisms ( A⊗B)⊗n∼= A⊗n⊗B⊗n and
A⊗n+m∼=A⊗n⊗A⊗m. □
Recall that, by functoriality, if f :Y•→X• is a map of simplicial sets, then for
any CDGA A, we have a map of algebra f∗ :CH •
Y•(A)→CH •
X• (A) which exhibits
the Hochschild complex of A overX• as a module over the Hochschild complex of
A overY•. Let Z •→X•, Z•→Y• be two maps of simplicial sets and let W• be a
pushout W•∼=X•
∐
Z•Y•.
Proposition 3. There is a natural map of simplicial modules 4
CH •
X• (A,M )⊗CH •
Z• (A,A)CH •
Y• (A,A )→CH •
W• (A,M )
3Recall that we are using a cohomological type grading for our diﬀerential graded modules, see
Convention (7) on page 7.
4The tensor product in Proposition 3 is the tensor product of ( simplicial) modules over the
simplicial diﬀerential graded commutative algebra CH •
Z• (A, A). Passing to the Hochschild chain
complexes, it induces a natural map of CDGAs and modules and y ield a quasi-isomorphism if Z•
injects into either X• or Y•, see [13, Corollary 2.4.3].
14 G. GINOT, T. TRADLER, AND M. ZEINALIAN
which is a map of algebras if M = A (with its natural module structure). If Z•
injects into either Z•
f•→X• or Z•
g•→Y•, then this map is in fact an isomorphism
of CH •
W• (A)-modules.
Proof. The proof [13, Lemma 2.1.6] given in the case M =A applies to any module
M . □
Corollary 2. The rule (X•,A )↦→HH •
X• (A) is a functor HH :sSet×CDGA→
CGA which satisﬁes the following axioms
(1) bimonoidal: Hochschild homology is monoidal with respect to the monoida l
structures given by the disjoint union of simplicial sets an d tensor products
of algebras. In other words, there are natural isomorphisms :
HH •
X•×Y•(A)∼=HH •
X•(A)⊗HH •
Y•(A), HH•
X• (A⊗B)∼=HH •
X•(A)⊗HH •
X• (B).
(2) homotopy invariance : if f : X• → Y• and g : A → B are (weak)
homotopy equivalences, then HH (f,g ) : HH •
X• (A)→HH •
Y• (B) is an iso-
morphism.
(3) point There is a natural isomorphism HH •
pt(A)∼=A
A similar statement holds with the category of topological s paces instead of simplicial
sets, and with the pointed analogs of these categories (as in Corollary 1).
Proof. This follows from Proposition 3, Proposition 2, Corollary 1 and Propos ition 4
below. □
The axioms listed in the above proposition are not enough to uniquely deter-
mine Hochschild homology as a functor. Indeed, we are missing an ana log of the
Excision/Mayer-Vietoris axioms in the classical Eilenberg-Steenrod axioms for sin-
gular homology. The analog of this axiom is similar to the locality axiom of a Topo-
logical Field Theory. In view of Proposition 3, we wish to compute the H ochschild
homology over an union of two open sets as the tensor product of t he Hochschild
homology of each open tensored over the Hochschild homology over their intersec-
tion. This forces us to take derived tensor products. Thus a better framework for
an axiomatic description of Hochschild chains is given by considering de rived cate-
gories or (∞, 1)-categories. We deal with this locality axiom in Section 3.2 below.
This axiom translates into an Eilenberg-Moore spectral sequence f or Hochschild
homology, see Corollary 3.
A crucial property of Hochschild chains which allows to pass to homot opy cat-
egories, is the fact, proved by Pirashvili [30], that the higher Hoch schild chain
complex is invariant along quasi-isomorphisms in both arguments.
Proposition 4. [Homotopy and homology invariance] If f :X•→Y• is a map of
simplicial sets inducing an isomorphism in homology H•(X)
≃
→ H•(Y ) , then the
map CH •
X• (A,M )→CH •
Y•(A,M ) is a quasi-isomorphism.
Further if h :A→B is a quasi-isomorphism of CDGAs, then the induced map
h• :CH •
X• (A)→CH •
X• (B) is a quasi-isomorphism of CDGAs.
If Z• is a pointed simplicial set and M is a B-module, the induced map h• :
CH •
Z•(A,M )→ CH •
Z• (B,M ) is a quasi-isomorphism of CH •
Z• (A)-modules and
if α : M → N is a map of B-modules, the induced map α• : CH •
Z• (B,M )→
CH •
Z•(B,N ) is a quasi-isomorphism of CH •
Z• (B)-modules.
DERIVED HIGHER HOCHSCHILD, TCH, F ACTORIZATION ALGEBRAS 15
Proof. This is essentially due to Pirashvili [30]. Indeed, let Γ be the category o f
ﬁnite sets, then the Hochschild chain complex CH •
X• (A) is isomorphic to the tensor
product
kX•⊗ΓL(A)
of the left Γ-module L(A) and the simplicial right Γ-module kX• . Here the left
Γ-moduleL(A) is deﬁned by n↦→A⊗n+1 and formula (1). The right Γ-module kX•
is deﬁned by n↦→ lim−→
K• ﬁnite
k
[
Hom Γ
(
[n],K •
)
] where [n] is the ﬁnite set {0,...,n },
see [30]. A quasi-isomorphism of CDGAs induces a quasi-isomorphism of left Γ-
module and similarly for a quasi-isomorphism of simplicial sets. Since eac h right
Γ-module kXm (m∈ N) is a projective right Γ-module (see [30]), the tensor product
kX•⊗ΓL(A) is quasi-isomorphic to the derived tensor product kX•⊗L
ΓL(A). It
follows that this complex is invariant along quasi-isomorphisms in both a rguments
(X• and A). The proof in the case of pointed simplicial sets and modules is the
same with the category Γ replaced by the category of pointed ﬁnite sets. □
3.2. Higher Hochschild as an (∞, 1)-functor. In this section we deal with ax-
ioms for the theory of higher Hochschild chains instead of mere homology. That
is, we upgrade the previous section, in particular Corollary 2, to the setting of
derived categories, or more precisely ( ∞, 1)-categories. Said otherwise, we replace
the category of simplicial sets by its homotopical analogue: the ( ∞, 1)-category of
simplicial sets denoted sSet∞ and we replace the category of commutative diﬀeren-
tial algebras by CDGA ∞, the (∞, 1)-category associated to the derived category of
commutative diﬀerential graded algebras (obtained by inverting qu asi-isomorphisms
of CDGAs).
In this settting, we will prove that the axioms determine uniquely the Hochschild
chain as an (∞, 1)-functor (lifting Hochschild homology). These axioms are not spe-
ciﬁc to CDGA but rather come from the fact that any presentable ( ∞, 1)-category is
(homotopically) canonically tensored over simplicial sets according t o [22, Corollary
4.4.4.9].
Theorem 1. There is a canonical equivalence CHX• (A)∼= X• ⊠A between the
Hochschild chains and the tensor of A and X•, i.e. there are natural equivalences
(in sSet∞)
(2) MapCDGA ∞
(
CHX• (A),B
) ∼= MapsSet∞
(
X•, MapCDGA ∞(A,B )
)
.
In particular, the Hochschild chains lift as a functor of (∞, 1)-categories CH :
sSet∞×CDGA ∞→CDGA ∞ which satisﬁes the following axioms
(1) value on a point: there is a natural equivalence CH •
pt(A)∼=A of CDGAs.
(2) monoidal: CH is monoidal with respect to both variables. Precisely, ther e
are natural equivalences
CH •
X•
∐ Y• (A)∼=CH •
X• (A)⊗CH •
Y• (A),
CH •
X• (A⊗B)∼=CH •
X• (A)⊗CH •
X• (B).
(3) homotopy gluing/pushout: CH sends homotopy pushout in sSet∞ to
homotopy pushout in CDGA ∞. More precisely, given maps Z•
f
→X• and
Z•
g
→ Y• in sSet∞, and W•∼= X•
⋃ h
Z•Y• a homotopy pushout, there is a
16 G. GINOT, T. TRADLER, AND M. ZEINALIAN
natural equivalence
CH •
W• (A)∼=CH •
X• (A)⊗L
CH •
Z• (A)CH •
Y• (A).
In particular Theorem 1 implies similar statements involving the homoto py cat-
egories of simplicial sets and CDGAs instead of their ( ∞, 1)-reﬁnement. Axiom (3)
is the locality axiom (as for Topological Field Theories) playing the role of the
excision/Mayer-Vietoris axiom for classical homology.
Proof. The second equivalence in the monoidal axiom follows from Proposition 2.
The rest is an immediate consequence of [22, Corollary 4.4.4.9], § 3.1 and the fact
that the coproduct in CDGA ∞ is given by the tensor product of CDGAs. Note that
the axioms can also be proved easily and directly using the results of S ection 3.1,
as we now demonstrate for the interested reader’s convenience ( this incidentally
yields immediately another proof of the identiﬁcation of derived Hoch schild chains
with a tensor). We already know that the Hochschild chain complex de ﬁnes a
bifunctor (X•,A )↦→CH •
X• (A) from the category sSet×CDGA to CDGA, see
Proposition 1. The ( ∞, 1)-categories sSet∞ and CDGA ∞ both arise from suit-
ables localizations of the weak equivalences (see Section 2.3). That is sSet∞ =
LCSeSp(N•(LH (sSet,WsSet))) and CDGA ∞ =LCSeSp(N•(LH (CDGA,WCDGA )))
where WsSet and WCDGA are the respective subcategories of weak equivalences in
sSet andCDGA given in Sections 2.1 and 2.2. Thus, in order to show that the func-
tor (X•,A )↦→CH •
X• (A) lifts to the (∞, 1)-associated categories, it suﬃces to show
that this bifunctor passes to the (hammock) localization of these m odel categories
along their subcategory of weak equivalences WsSet and WCDGA . By construc-
tion of the hammock localization functor LH , it suﬃces to prove that the usual
Hochschild chain complex bifunctor maps weak equivalences (in sSet×CDGA) to
weak equivalences (in CDGA) which follows from Proposition 4. More precisely,
the bifunctor CH :sSet∞×CDGA ∞→CDGA ∞ is the bifunctor induced by the
bifunctor
LCSeSp
(
N•
(
(CH •
−(−))
))
:LCSeSp(N•(LH(sSet×CDGA,WsSet×WCDGA )))
−→ LCSeSp(N•(LH (CDGA,WCDGA )))
obtained by localizing the Hochschild chains.
When X• is contractible, Proposition 4 implies that there is an natural equiva-
lence CH •
X• (A)∼= CH •
pt• (A)∼= A of CDGAs where pt• is the standard simplicial
model of a point, see [13, Example 2.3.4]. This proves the value on a po int axiom.
The compatibility with the monoidal structures follows from Proposit ion 2 since
both monoidal functors ∐ : sSet×sSet→ sSet and⊗k : CDGA×CDGA →
CDGA are Quillen exact, thus passes to the ( ∞, 1)-category induced by the model
categories structures.
It remains to prove the homotopy gluing axiom. We let f• :Z•→X• and g• :
Z•→Y• be simplicial sets maps. Since we already know that the Hochschild cha in
complex preserves weak equivalences, we can replace W• by the pushout X•
⋃
Z•
ˆY•
where ˆg• :Z•→ ˆY• is a coﬁbration and p : ˆY
≃
→Y is a ﬁbrant replacement of Y .
By Proposition 3, there is a natural isomorphism
(3) CH •
X•
⋃
Z•
ˆY•(A)∼=CH •
X• (A)⊗CH •
Z• (A)CH •
ˆY• (A).
DERIVED HIGHER HOCHSCHILD, TCH, F ACTORIZATION ALGEBRAS 17
Since Z•
ˆg•
֒→ˆY• is injective, the induced map ˆ g∗ : CH •
Z• (A)→ CH •
ˆY•
(A) of
CDGAs exhibitsCH •
ˆY•
(A) as a semi-free CH •
Z• (A) algebra, thus the tensor product
in the quasi-isomorphism (3) can be replaced by a derived tensor pro duct:
(4) CH •
X•
⋃
Z•
ˆY•(A)∼=CH •
X• (A)⊗L
CH •
Z• (A)CH •
ˆY• (A).
By homotopy invariance, the mapp∗ :CH •
ˆY•
(A)∼=CH •
Y•(A) is a quasi-isomorphism
and thus the homotopy pushout axiom follows from the quasi-isomor phism (4). □
Remark 3. As in Corollary 2, the (model) categories of simplicial sets and (com-
pactly generated) topological spaces being Quillen equivalent, one c an replace
sSet∞ by its topological counterpart Top ∞ in Theorem 1. This yield the Hochschild
chain functor over spaces CH :Top ∞×CDGA ∞→CDGA ∞, see§ 4. By deﬁni-
tion Hochschild chain are functorial in spaces; for instance any con tinuous map f :
X→Y between topological spaces induces a chain map f• :CH •
X (A)→CH •
Y (A)
which is an equivalence if f is a weak-equivalence. We will get back to and focus
on this Hochschild functor over topological spaces in Section 4
The locality axiom (3) in Theorem 1 yields an Eilenberg-Moore type spectral
sequence for computing higher Hochschild homology.
Corollary 3. Given an homotopy pushout W• ∼= X•∪h
Z• Y•, there is a natural
strongly convergent spectral sequence of cohomological ty pe of the form
Ep,q
2 :=Tor
HH •
Z• (A)
p,q
(
HH •
X• (A),HH •
Y• (A)
)
=⇒HHp+q
W• (A)
where q is the internal grading. The spectral sequence is furthermore a spectral
sequence of diﬀerential HH •
Z•(A)-algebras.
Recall that we are considering a cohomological grading; in particular the spectral
sequence is concentrated in the left half-plane with respect to this grading (and p
is negative).
Proof. By Theorem 1, we haveCH •
W• (A)∼=CH •
X• (A)⊗L
CH •
Z• (A)CH •
Y•(A) as CDGAs.
Now the spectral sequence follows from standard results on deriv ed tensor prod-
ucts (of CH •
Z• (A)-modules) [20, Theorem 4.7]. That the spectral sequence is one
of algebras comes from the fact, that we can choose a semi-free r esolution of CH •
X•
by a CH •
Z• -algebra. □
Example 4. (1) It is a well-known fact, that the usual Hochschild complex
of an associative algebra A CH•(A) = CH •
S1•
(A) may be written as a Tor
over the bimodule Ae = A⊗Aop, see e.g. [21, Proposition 1.1.13]. More
explicitly,
HH •(A) = TorAe
• (A,A ).
Identifying HHpt•• (A) = A, and HH •
{pt•,pt−
• }(A) = A⊗Aop = Ae, where
pt−
• denotes the point with opposite orientation, we see that, in this cas e,
the spectral sequence of Corollary 3 collapses at the E2 level,
TorHH
{pt• ,pt−
• }•• (A) (
HH •
pt• (A),HH •
pt• (A)
)
=HH •
S1
•(A)
where we used that S1
• ∼= pt•∪h
{pt,pt−}• pt• and further that when A is
commutative,Aop =A.
18 G. GINOT, T. TRADLER, AND M. ZEINALIAN
(2) Let f• :Z•→X• be a map of simplicial spaces. Then, the mapping cone
(Cf )• is given as the homotopy pushout ( Cf )•∼=X•∪h
Z• pt•. We obtain a
spectral sequence computing HH •
(Cf )•(A),
Tor
HH •
Z• (A)
p,q
(
HH •
X• (A),A
)
=⇒HH •
(Cf )• (A)
(3) In a more straightforward way, we may use the gluing property to give
explicit models for spaces with cubic subdivisions. Our starting point is
given by models for interval I• and the square I 2
• via,
CH •
I• (A) =
∑
k
A⊗(k+2) and CH •
I 2
• (A) =
∑
k
A⊗(k+2)2
.
The ith diﬀerential is given in the case of I• by multiplying the ith and
(i + 1) th tensor factors, and in the case of I 2
• by multiplying the ith and
(i + 1)th column of tensor factors and the ith and (i + 1)th rows of tensor
factors simultaneously. For more detail, see [13, Example 2.3.4]. Then
we obtain the Hochschild complex for the cylinder C• = I 2
•∪(I•∪I•)I• by
gluing I 2
• and I• along I•∪I• on opposite edges of I 2
• , and with this the
torus T• = C•∪(I•∪I•)I• by gluing the remaining sides together. A more
elaborate version of this is given in [13, Example 2.3.2]. By using similar,
but more elaborate considerations, one can in fact obtain Hochsch ild models
over any surface, see [13, Section 3.1].
Higher Hochschild chain complexes behaves much like cochains of mapping spaces
(see [13, sections 2.2, 2.4]). Indeed they satisfy a kind of exponent ial law:
Proposition 5 (Finite Products of simplicial sets) . LetX•, Y• be simplicial sets.
Then there is a natural equivalence
CH •
X•×Y•(A)
∼
→CH •
X•
(
CH •
Y• (A)
)
in CDGA ∞.
Proof. It follows from Corollary 2.4.4 of [13]. □
The Hochschild chain functor CH :sSet∞×CDGA ∞→CDGA ∞ is essentialy
(up to equivalences) determined by the homotopy pushout axiom, c oproduct and
its value on a point. In other words, it is the unique (∞, 1)-functor (up to natural
equivalences) satisfying the three axioms (value on a point, coprod uct and locality)
listed below in Theorem 2. This is once again a consequence of the fact that higher
Hochschild is a tensor. The precise uniqueness statement is :
Theorem 2 (Derived Uniqueness). Let (X•,A )↦→FX• (A) be a bifunctor sSet∞×
CDGA ∞→CDGA ∞ which satisﬁes the following three axioms.
(1) value on a point: There is a natural equivalence of CDGAs Fpt• (A)∼=A.
(2) coproduct: There are natural equivalences
F∐
I
(Xi)•(A)∼= lim−→
K ⊂ I
K ﬁnite
⨂
k∈K
F(Xk)•(A)
DERIVED HIGHER HOCHSCHILD, TCH, F ACTORIZATION ALGEBRAS 19
(3) homotopy gluing/pushout: F sends homotopy pushout in sSet∞ to
homotopy pushout in CDGA ∞. More precisely, given two maps Z•
f
→X•
and Z•
g
→ Y• in sSet∞, and W•∼= X•
⋃ h
Z•Y• a homotopy pushout, one
has a natural equivalence
FW• (A)∼=FX• (A)⊗L
FZ• (A)FY•(A).
Then F is naturally equivalent to the higher Hochschild chains bif unctor CH as a
bifunctor i.e. as an object in Hom (∞,1)−cat(sSet∞×CDGA ∞,CDGA ∞).
Proof. This is a consequence of the fact that CDGA ∞ (and actually any presentable
(∞, 1)-category) is uniquely tensored over sSet∞, see [22, Corollay 4.4.4.9].
Alternatively it can be prove by noticing that any simplicial set X• is a (ho-
motopy) colimit of its skeletal ﬁltration sknX•, which in turns is obtained by
taking a homotopy pushout of skn−1X• with coproducts of standard model ∆ n
•
of the simplices which are contractible. Then the axioms imply an equiva lence
FsknX• (A)
≃
→CH •
sknX•(A) which commutes with the inclusions skn−1X•֒→sknX•
so that it induces an natural equivalence FX• (A)∼=CHX• (A) since the latter sat-
isﬁes teh axioms by Theorem 1.
For the interested reader, we now make this sketch more precise. Let (X•,A )↦→
FX• (A) be a functor satisfying the assumption of Theorem 2. If X• is a ﬁnite
discrete simplicial set, there are natural equivalences in CDGA ∞
FX• (A)∼=FX0 (A)∼=F∐
x∈X0 {x}(A)∼=A⊗X0∼=CH •
X• (A)
since both bifunctors F and CH are homotopy invariant, commute with ﬁnite
coproducts and satisﬁes Axiom (1). If X• is discrete, non-necessarily ﬁnite, then
Axiom (2) implies that FX• (A)∼= lim−→
K ﬁnite
FK (A)∼= lim−→
K ﬁnite
A⊗K∼= CH •
X• (A) by
deﬁnition of Hochschild chain of simplicial sets (Deﬁnition 2).
LetsknX• be the nth-skeleton of a simplicial set X• (see [14] for instance), i.e.,
the sub-simpicial set generated by all non-degenerate simplices of dimension less
than or equal to n. Note that X• is the ﬁltered colimit X• = ⋃
n≥0sknX•. Since
sk0X• is a discrete simplicial set, we have an natural (in A andX•) equivalence of
algebras Fsk0X•(A)
≃
→CH •
sk0X•(A).
Now assume n≥ 1 and that we have a natural equivalence (induced by a natural
zigzag of quasi-isomorphisms) of CDGAs Fskn−1X• (A)
≃
→ CH •
skn−1X• (A) (for any
simplicial set X•). Let NXn be the subset of non-degenerate simplices in Xn, ∆ n
•
be the standard simplicial model ∆ n
k =Hom ∆ ([k], [n]) of the topologicaln-simplex
and ∂∆ n
• its boundary (that is the sub-complex obtained by dropping the only
non-degenerate simplex of dimension n). Note that ∆ n
• is contractible and ∂∆ n
• is
a simplicial model for the sphere Sn−1. For n≥ 1, one has a pushout diagrams
(5) ∐
x∈NX n∂∆ n
•
jn /d47/d47/d127 /d95
in
/d15/d15
skn−1X•/d127 /d95
/d15/d15∐
x∈NX n ∆ n
• /d47/d47sknX•
20 G. GINOT, T. TRADLER, AND M. ZEINALIAN
which are homotopy pushouts since the vertical arrows are coﬁbr ations of simplicial
sets. Thus Axiom (3) and Theorem 1 yield natural equivalences
FsknX• (A)∼=Fskn−1X• (A)⊗L
F∐
x∈N Xn ∂∆ n
• (A)F∐
x∈N Xn ∆ n
• (A)
of F∐
x∈N Xn ∆ n
• (A)-algebras as well as a natural equivalence
CH •
sknX• (A)∼=CH •
skn−1X•(A)⊗L
CH •∐
x∈N Xn ∂∆ n
• (A)CH •∐
x∈N Xn ∆ n
• (A)
of CH •∐
x∈N Xn∂∆ n
• (A)-algebras. Here the modules structures are the natural ones
induced by the maps in the pushout diagram (5).
We now deduce that FsknX• (A) is equivalent to CH •
sknX•(A). Recall from
Example 2, that an equivalence A
∼
→ B of CDGAs induces an equivalence of
their (∞, 1)-categories of modules B-Mod ∞
∼
→ A-Mod ∞. Note that ∂∆ n
• has
no non-degenerate simplices in dimension n and higher. Thus ∂∆ n
• = skn−1∂∆ n
•
and, by our induction assumption, we have a natural equivalence of CDGAs be-
tweenF∐
x∈N Xn∂∆ n
• (A) andCH •∐
x∈N Xn∂∆ n
• (A) as well as between Fskn−1X•(A) and
CH •
skn−1X• (A). Further, as the modules structures are induced by the simplicial
set map ∐
x∈NX n∂∆ n
•→skn−1X•, it follows that the diagram
F∐
x∈N Xn∂∆ n
• (A)⊗Fskn−1X• (A) ≃ /d47/d47
µ◦(jn⊗1)
/d15/d15
CH •∐
x∈N Xn∂∆ n
• (A)⊗CH •
skn−1X• (A)
µ◦(jn⊗1)
/d15/d15
Fskn−1X• (A) ≃ /d47/d47CH •
skn−1X• (A)
is commutative (here µ is the multiplication and jn the top map in diagram (5)).
HenceCH •
skn−1X•(A) is equivalent to Fskn−1X• (A) as an F∐
x∈N Xn∂∆ n
• (A)-CDGA.
We are left to prove that F∐
x∈N Xn ∆ n
• (A) and CH •∐
x∈N Xn ∆ n
• (A) are equivalent
F∐
x∈N Xn∂∆ n
• (A)-CDGAs. By the homotopy invariance and value on a point ax-
iom, we have a natural equivalence F∐
x∈N Xn ∆ n
• (A)
≃
→ A⊗#NX n (induced by the
unique map ∆ n
•→ pt• for each non-degenerate simplex in NXn) and further the
F∐
x∈N Xn∂∆ n
• (A)-algebra structure on A⊗#NX n is induced by the canonical map∐
x∈NX n∂∆ n
• −→ ∐
x∈NX npt•. The same argument holds for Hochschild chains
CH instead of F so that we have a commutative diagram
F∐
x∈N Xn∂∆ n
• (A) ≃ /d47/d47
in
/d15/d15
CH •∐
x∈N Xn∂∆ n
• (A)
in
/d15/d15
F∐
x∈N Xn ∆ n
• (A) ≃ /d47/d47A⊗#NX n CH •∐
x∈N Xn ∆ n
• (A)≃/d111/d111
from which it follows that both CH •∐
x∈N Xn ∆ n
• (A) and F∐
x∈N Xn ∆ n
• (A) are equiva-
lent to A⊗#NX n as F∐
x∈N Xn∂∆ n
• (A)-CDGAs. Tensoring the previous equivalence
withA⊗#NX n (overF∐
x∈N Xn∂∆ n
• (A)) we obtain a natural equivalenceFsknX• (A)∼=
CH •
sknX• (A) in CDGA ∞.
By induction, we get (for all n’s) natural equivalencesFsknX• (A)
≃
→CH •
sknX• (A)
which commutes with the inclusions skn−1X•֒→sknX•. Since X• = ⋃
n≥0sknX•,
DERIVED HIGHER HOCHSCHILD, TCH, F ACTORIZATION ALGEBRAS 21
there is a coequalizer in the ( ∞, 1)-category sSet∞:
∐
n∈NsknX•
δ
/d15/d15
id /d47/d47 ∐
n∈NsknX•
/d15/d15∐
n∈NsknX• /d47/d47X•
where δ : ∐
n∈NsknX•→ ∐
n∈NsknX• is the map induced by the canonical inclu-
sionssknX•→skn+1X•. Thus by axiom (3), there is a natural equivalence
(6) FX• (A)∼=F∐
n∈NsknX• (A)
L
⊗
F∐
n∈N skn X• (A)
F∐
n∈NsknX• (A)
and similarly for Hochschild chains by Theorem 1. By axiom (2) applied to the
bifunctorsF andCH , the natural equivalences FsknX• (A)
≃
→CH •
sknX• (A) for all n
thus yield a natural equivalence F∐
n∈NsknX• (A)∼=CH •∐
n∈NsknX• (A). The natural
equivalence of CDGAs FX• (A)∼=CH •
X• (A) now follows from equivalence (6) and
the analogous equivalence for Hochschild chains. □
Remark 4. If A is concentrated in non-positive degrees, then CH •
X• (A) is also
concentrated in non-positive degrees. This happens for instance if A is the CDGA
associated to a simplicial (non-graded) commutative algebra. In th at case, it is
possible to replace CDGA andCDGA ∞ in Theorem 1 and Theorem 2 by CDGA ≤0
the category of CDGAs concentrated in non-positive degrees and CDGA ≤0
∞ its
associated (∞, 1)-categories (the proofs being unchanged).
Remark 5. Again, one can replace sSet∞ by its topological counterpart Top ∞ in
Theorem 2, see Proposition 8.
Remark 6. Note that one can deduce from the coproduct axiom (2) in Theorem 2
and the natural equivalence (6) that the natural map lim−→FsknX•(A)
≃
→FX• (A) is
an equivalence. This is in particular true for Hochschild chains:
(7) lim −→
n≥0
CHsknX•(A)
≃
→CHX• (A).
Remark 7. If G : CDGA ∞→ CDGA ∞ is a functor, one can replace the value
on a point axiom by the existence of a natural quasi-isomorphism Fpt(A)∼=G(A).
The proof of the Theorem 2 shows the following
Corollary 4. LetG :CDGA ∞→CDGA ∞ be a functor and (X•,A )↦→FX• (A) be
a bifunctor sSet∞×CDGA ∞→CDGA ∞ which satisﬁes the axioms (2) and (3)
in Theorem 2 and with axiom (1) replaced by Fpt• (A)∼= G(A). Then FX• (A) is
naturally equivalent CH •
X• (G(A)).
For instance, consider the bifunctor given by ( X•,A )↦→CH •
X• (A)⊗CH •
X• (B)
whose value on a point is the functor A↦→A⊗B. By Corollary 4, this functor is
isomorphic to (X,A )↦→CH •
X• (A⊗B) which gives another proof of the fact that the
Hochschild chains preserve ﬁnite coproduct of CDGAs. The same ar gument shows
thatCH also commutes with ﬁnite homotopy pushouts of CDGAs, see Corollar y 5
below.
22 G. GINOT, T. TRADLER, AND M. ZEINALIAN
Corollary 5. The Hochschild chain bifunctor CH :sSet∞×CDGA ∞→CDGA ∞
commutes with ﬁnite colimits in sSet∞ and all colimits in CDGA ∞, that is there
are natural equivalences
CH •
lim−→
F
Xi•(A) ∼= lim−→
F
CH •
Xi• (A) ( for a ﬁnite category F ),
CH •
X• ( lim−→Ai) ∼= lim−→CH •
X• (Ai).
Here the colimits are colimits in sSet∞ or CDGA ∞.
Proof. Any ﬁnite colimits can be obtained by a composition of coproducts and
pushouts (or coequalizers). Thus the result for colimits in sSet∞ follows from
Theorem 1, Axioms (2) and (3). Let lim−→
i∈I
Ai be a non-empty colimit of CDGAs
and let i0 be an object in the indexing category I. By functoriality we can deﬁne
a functor GI :CDGA ∞→CDGA ∞ by the formula A↦→GI (B) := lim−→
˜Bi where
˜Bi∼=Ai if i⁄=i0 and ˜Bi0
∼=B. In other words we ﬁx all the variables but the one
indexed by i0. Now applying Corollary 4 to the bifunctor F :sSet∞×CDGA ∞→
CDGA ∞ deﬁned by FX• (B)∼= lim−→CH •
X• ( ˜Bi) we get an natural equivalence
CH •
X• ( lim−→
i∈I
Ai)∼= lim−→
i∈I
CH •
X• (Ai).
Since the simplicial module n↦→CH •
Xn (k) is isomorphic to the constant simplicial
k-algebra n↦→k, the result also follows for empty colimits. □
Example 5. By Corollary 5, given two maps f :R→A andg :R→B of CDGAs,
there is a natural equivalence (in CDGA ∞)
CH •
X•
(
A
L
⊗
R
B
)
∼= CH •
X• (A)
L
⊗
CH •
X• (R)
CH •
X• (B).
