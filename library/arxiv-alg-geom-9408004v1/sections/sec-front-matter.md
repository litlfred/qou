---
doc_id: arxiv-alg-geom-9408004v1
doc_title: "CUBICS, INTEGRABLE SYSTEMS, AND"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-20
source_pdf: 9408004v1.pdf
source_sha256: d3bc00265294aa02
---
arXiv:alg-geom/9408004v1  9 Aug 1994
CUBICS, INTEGRABLE SYSTEMS, AND
CALABI-YAU THREEFOLDS
Ron Donagi 1
University of Pennsylvania
and
Eyal Markman 2
University of Michigan
To Professor Hirzebruch, on his 65 th birthday
§0. Introduction
In this work we construct an analytically completely integr able Hamil-
tonian system which is canonically associated to any family of Calabi-Yau
threefolds. The base of this system is a moduli space of gauge d Calabi-Yaus
in the family, and the ﬁbers are Deligne cohomology groups (o r intermediate
Jacobians) of the threefolds. This system has several inter esting properties:
the multivalued sections obtained as Abel-Jacobi images, o r “normal func-
tions”, of a family of curves on the generic variety of the fam ily, are always
Lagrangian; the natural aﬃne coordinates on the base, which are used in
the mirror correspondence, arise as action variables for th e integrable sys-
tem; and the Yukawa cubic, expressing the inﬁnitesimal vari ation of Hodge
structure in the family, is essentially equivalent to the sy mplectic structure
on the total space.
We begin our study by exploring this equivalence in a much mor e gen-
eral context. The general question is as follows: Given a fam ily of abelian
varieties, when is there a symplectic form on the total space with respect
to which the abelian varieties are Lagrangian? This turns ou t to involve a
symmetry condition on the partials of the period map for the f amily. Equiv-
alently, this amounts to the existence of a ﬁeld of cubics on t he tangent
bundle to the base, such that the diﬀerential of the period ma p at each
point is given by contraction with the cubic. We give several versions of
this ‘cubic condition’ in §1. For most of the examples and applications, we
refer the reader to the survey [DM]. The one example which we w ork out in
detail here is the integrable system of a Calabi-Yau family, where the ‘cubic’
is Yukawa’s.
1Supported by grants from NSF and NSA
2Supported by Rackham Fellowship, University of Michigan, 1 993
1
The last section is entirely speculative. We muse on the role which the
CY integrable system might play in the mirror conjecture: we would like to
separate the conjecture into a formal part, which deals with a ‘mirror trans-
form’ for objects consisting of an integrable system togeth er with certain La-
grangian multisections and other lists of data, and a geomet ric, Torelli-like
part, saying that a CY family can be recovered from its integr able system.
The attempt to read oﬀ all relevant data (= the partition func tions for the
A and B models) directly from the system leads to some Hodge theoret ic
questions which we cannot solve, concerning the informatio n encoded in a
normal function and especially in its inﬁnitesimal invaria nt.
It is our pleasure to acknowledge beneﬁcial and pleasant con versations
with R. Bryant, I. Dolgachev, M. Green, P. Griﬃths, S. Katz, L . Katzarkov,
D. Morrison, T. Pantev and E. Witten.
§1. The cubic condition .
Our goal in this section is to describe the conditions on a giv en family
π : X → U of abelian varieties (or complex tori) for there to exist, lo cally
over U, an algebraic (or analytic) symplectic structure σ on X such that π
is a Lagrangian ﬁbration with respect to σ. (In this situation we say that
the family admits a Lagrangian structure.) What we want is a closed, non-
degenerate holomorphic 2-form σ on X such that the ﬁbers Xu := π−1(u)
are Lagrangian (= maximal isotropic) subvarieties with res pect to σ.
By way of motivation, let us review the corresponding questi ons for C ∞
objects. Any C ∞ family π : X → U of real tori is locally trivial, i.e. locally
(over U) isomorphic to U × (S1)n. In particular, a Lagrangian structure
exists whenever dim U = n = dim (ﬁbers). Given a C ∞ symplectic mani-
fold ( X,σ ) with Lagrangian ﬁbration π : X → U , there is a natural aﬃne
structure on the ﬁbers Xu [AG,2.42]; so if these ﬁbers are compact, they
must be tori. In this case the base U also acquires a natural integral-aﬃne
structure, i.e. an atlas of coordinate systems which diﬀer on intersec tions
by a combination of arbitrary translations and Z-linear transformations. To
get these coordinates, we choose a basis γ1(u), · · ·,γ n(u) for the integral ho-
mology H1(Xu, Z), varying smoothly with u in an open subset U 0 of U, as
well as a 1-form τ on π−1(U 0) satisfying dτ =σ. (These always exist.) We
then let
(1) ti(u) :=
∫
γ i(u)
τ, i = 1, · · ·,n.
The freedom of changing τ (by a closed 1-form) and the γi (by the action
ofGLn(Z)) then allows the ti to change by a translation and Z-linear trans-
formation, respectively. These ti are called action variables . They deﬁne
2
Hamiltonian vector ﬁelds which are tangent to the Xu and integrate to give
the angle variables
(ϕ1, · · ·,ϕ n) : Xu
∼→ Rn/(2πZ)n.
The latter give the aﬃne structure on the ﬁbers.
A completely integrable Hamiltonian system (CIHS) on the 2n-dimensional
symplectic manifold ( X,σ ) is an ODE (given, say, by a vector ﬁeld v)
which possesses n independent integrals u1, · · ·,u n in involution (i.e. they
Poisson-commute). This translates immediately to a Lagran gian ﬁbration
π : X → Rn (where π = (u1, · · ·,u n)), and the ﬂow is linearized on the
level tori Xu, i.e. v is tangent to the ﬁbers, and v|Xu is a constant linear
combination of the ∂/∂ϕ i with coeﬃcients which depend smoothly on u.
The corresponding algebraic object is an algebraically completely inte-
grable Hamiltonian system (ACIHS): we want X to be a 2 n-dimensional
non-singular complex algebraic variety, σ a closed, non-degenerate holomor-
phic (2, 0)-form on X , π : X → U a morphism whose ﬁbers Xu are abelian
varieties which are Lagrangian subvarieties of ( X,σ ), and v a Hamiltonian
vector ﬁeld for some algebraic (Hamiltonian) function on U. Such an ODE
can be solved more-or-less explicitly, in terms of theta fun ctions. Numerous
examples, both in mathematics and in physics, are well-know n; we refer to
[DKN] for a survey, and to [DM] for some recent examples. What we are
asking here is, essentially, to decide when a given family of abelian varieties
underlies an ACIHS.
The ﬁrst new feature of the algebraic situation is that a fami ly of abelian
varieties need not be locally trivial. Rather, it is speciﬁe d by its classifying
map
q : U → A g,
where Ag is the moduli space of abelian varieties of dimension g and of a
given polarization type. The given family π : X → U is recovered as the
pullback via q of the universal abelian variety Xg → A g. (The latter, of
course, does not quite exist, but it exists locally away from abelian varieties
with excess automorphisms, and also globally on a ﬁnite “lev el” branched
cover of Ag.)
Let V → U be the vertical bundle determined byπ : X → U . Its ﬁber over
u ∈ U can be identiﬁed with the tangent space T0Xu, or with the universal
cover of Xu. Deformation theory identiﬁes the tangent space to Ag at a
non-singular point [X] ∈ A g with Sym 2V , where V := T0X. We may thus
write the diﬀerential of the classifying map as
(2) dq :T U → Sym 2V.
If the family π : X → U admits a Lagrangian structure then the sym-
3
plectic form σ induces an isomorphism
(3) i =σ−1 : V ∗ ∼→T U.
We reﬁne our question by considering pairs consisting of the familyπ : X →
U together with the isomorphism i, and asking for the existence of σ which
is compatible with both. Our ﬁrst answer is:
Theorem 1. (Inﬁnitesimal cubic condition ) Consider a family π :
X → U of polarized abelian varieties with classifying map q : U → A g and
vertical bundle V, together with an isomorphism (3). Then there exists a
non-degenerate holomorphic 2-form σ on X for which π is Lagrangian and
which induces the given isomorphism i, if and only if the composition of (2)
and (3):
dq ◦i ∈Hom(V ∗,Sym 2V) = Γ( V ⊗ Sym 2V)
comes from a cubic c ∈ Γ(Sym 3V). In this case, there is a unique σ for
which the 0-section of π is Lagrangian.
Proof.
The short exact sequence of sheaves on X :
0 →π∗V → T X → π∗T U → 0
determines a subsheaf F of Λ 2T X which ﬁts in the exact sequences:
0 → F → Λ 2T X → π∗Λ 2T U → 0
0 →π∗Λ 2V → F → π∗(V ⊗ T U) → 0.
We are looking for a 2-vector σ−1, a section of Λ 2T X , for which the ﬁbers of
π are isotropic; this means that σ−1 goes to 0 in π∗Λ 2T U, so it comes from
a section of F . The question is therefore whether the given
i ∈H 0(U, V ⊗ T U) ⊂H 0(X,π ∗(V ⊗ T U))
is in the image of H 0(X, F ). Locally in U, this happens if and only if i goes
to 0 under the coboundary map
π∗π∗(V ⊗ T U) → R1π∗π∗Λ 2V
‖ ‖
V ⊗ T U → Λ 2V ⊗ V.
The bottom map factors as β ◦ (1 ⊗dq), where
1 ⊗dq : V ⊗ T U → V ⊗ Sym 2V
4
comes from the diﬀerential of the classifying map q, and β is part of the
(exact) Koszul complex
0 →Sym 3V
α
→ V ⊗ Sym 2V
β
→ Λ 2V ⊗ V → · · · .
We conclude that the desired 2-vector σ−1 exists locally if and only if
dq ◦i = (1 ⊗dq)(i) ∈ V ⊗ Sym 2V
comes, via α, from a section of Sym 3V. The global existence of σ will follow
by patching local solutions, once we know uniqueness. For th is, let σ1,σ 2 be
two local solutions. Then σ1 −σ2 induces the 0-map from T U to V ∗, hence
it is the pullback of a 2-form ϕ on U. But restricting to the 0-section of π
showsϕ = 0, so σ1 =σ2 as required.
Q.E.D
We view this theorem as an inﬁnitesimal answer to our problem :
If we replace U by its ﬁrst-order germ at the point u ∈ U , then the theorem
provides a necessary and suﬃcient condition for existence o f a Lagrangian
structure for π : X → U . In general, it provides a non-degenerate 2-form
σ, but an additional condition is needed for σ to be closed. For this, it is
convenient to replace the moduli space Ag by the Siegel upper half space:
Hg := {g ×g symmetric complex matrices Z with im(Z)> 0}.
Over Hg there is (for each polarization type) a universal (marked) abelian
variety Xg → Hg, whose ﬁber over Z ∈ Hg is V/L , where V ≈ Cg is a
ﬁxed complex vector space, and L is the lattice generated by the 2 g columns
of the g × 2g matrix (I,Z ). (Here I is the g ×g identity matrix, when
the polarization is principal, and in general it is the g ×g integral diagonal
matrix whose entries are the elementary divisors of the pola rization.) Any
family π : X → U of abelian varieties which are marked (i.e. endowed with
a continuously varying symplectic basis of the ﬁber homolog ies H1(Xu, Z),
u ∈ U ) determines a period map
p : U → Hg,
and is recovered as the pullback via p of the universal family Xg. (The
classifying mapq, from U to Ag, is obtained by composition with the quotient
map Hg → A g .)
Let us consider the complex analogue of the action-angle coo rdinates and
the corresponding aﬃne structures. A symplectic family π : X → U of
bare abelian varieties, given by the classifying map q : U → A g, determines
locally on U a set of 2g action variables, given by formula (1). To get action
coordinates, we need to choose g of these. Now the polarization on the ﬁbers
5
Xu gives a symplectic structure on H1(Xu, Z), so the natural thing to do is
to choose a Lagrangian basis γ1(u), · · ·,γ g(u), i.e. a basis of a continuously
varying Lagrangian subspace. On the other hand, the choice o f a marking
of the family π, i.e. a lifting of q to a period map p : U → Hg, is equivalent
to the choice of a dual pair γ1, · · ·,γ g andγg+1, · · ·,γ 2g of Lagrangian bases.
Combining this with (1), we get:
Lemma 1. Let π : X → U be a family of abelian varieties with La-
grangian structure. The choice of Lagrangian basis γ1, · · ·,γ g of the ﬁber
homologies determines an aﬃne structure on U. The choice of a mark-
ing γ1, · · ·,γ 2g (or of a period map p : U → Hg) determines a pair of aﬃne
structures. The aﬃne coordinates {ui}, {ti} corresponding to the Lagrangian
basesγ1, · · ·,γ g and γg+1, · · ·,γ 2g, respectively, are related by:
dti =
∑
pij(u)duj.
We note that, even with these choices, the angle coordinates ϕi are still
multivalued, i.e. they can be deﬁned only locally. Their diﬀ erentials dϕi
are more intrinsic: they correspond symplectically to stra ight ﬂows (with
respect to the aﬃne structure) on U. The ϕi can be uniquely determined on
the vertical bundle V (= the ﬁberwise universal cover) by setting ϕi = 0 on
the 0-section of V.
We ﬁx once and for all the vector space V ≈ Cg. Any marked family
π : X → U of abelian varieties then comes with a trivialization of its vertical
bundle,
(4) V ≈ V ⊗ OU.
We identify Hg with an open subset of Sym 2V , so the diﬀerential of the
period map becomes
dp :T U → Sym 2V ⊗ OU.
The aﬃne structure on U, determined by γ1, · · ·,γ g and a Lagrangian struc-
ture, is then given by an isomorphism
α :V ∗ ⊗ OU
∼→T U.
Theorem 2. (Global Cubic Condition ) Consider a family π :
X → U of marked abelian varieties, with period map p : U → Hg, where
U has an aﬃne structure α :V ∗ ⊗ OU
∼
→T U. Then π admits a Lagrangian
structure which induces α if and only if the composition
dp ◦α ∈Hom(V ∗ ⊗ OU,Sym 2V ⊗ OU ) = Γ( V ⊗Sym 2V ⊗ OU )
comes from a cubic c ∈ Γ(Sym 3V ⊗ OU ).
6
Proof.
Note that the trivialization (4) takes α to the isomorphism i of (3), and
dp goes to dq of (2). The “only if” therefore follows from Theorem 1.
Conversely, we start with the standard symplectic structur e on the cotan-
gent bundle T ∗U. Via the aﬃne structure α and the trivialization (4), we
get a symplectic structure σ on the vertical bundle V. The projection to U
is Lagrangian with respect to σ as is the 0-section. We want σ to descend
to X . Equivalently, σ should be invariant under translation by the section
sm,n :u ↦→m +p(u)n,
for any m,n ∈ Zg, which happens if and only if the sections sm,n are La-
grangian. Back on T ∗U, we want the corresponding 1-forms on U to be
closed. This is always true for the sm, 0, since α is assumed to be an aﬃne
structure. For s0,n , we need closedness of the g 1-forms ∑ pij(u)duj. This
amounts to equality of mixed partials, hence to the symmetry condition on
dp ◦α. We conclude that if dp ◦α is symmetric then σ descends to a La-
grangian structure on π. This induces α by construction.
Q.E.D
Remarks.
(1) Another way to state this is as follows. Given the period m ap p and
the isomorphism i, we get an isomorphism
α :V ∗ ⊗ OU
∼
→T U.
If the cubic condition holds (with respect to i), we get the 2-form σ by The-
orem 1. This σ is closed (i.e. gives a Lagrangian, or symplectic, structur e)
if and only if the isomorphism α is integrable, i.e. if and only if α integrates
to an aﬃne structure on U.
(2) In the situation of the theorem, we deduce from the equali ty of mixed
partials that locally in U there is a function f ∈ Γ( OU ) such that
∂2f =p, ∂ 3f =c,
as sections of Sym 2T ∗U, Sym 3T ∗U respectively. Here ∂ denotes the total
derivative with respect to the aﬃne structure on U, so∂k denotes, essentially,
the kth term in the Taylor expansion. f is unique up to adding an aﬃne
function. Conversely, any holomorphic f on a complex manifold U withV ∗-
aﬃne structure determines a Lagrangian family of abelian va rieties on the
open subset of U where Im(∂2f )> 0.
7
(3) Much of the above extends to Lagrangian structures on fam ilies of
complex tori. The new feature is that p lands in V ⊗V , instead of Sym 2V ,
so we can write p =p+ +p−, with p+ symmetric, p− skew symmetric. The
result is that in order to have a Lagrangian structure, p− must be locally
constant on U, while p+ satisﬁes a cubic condition as above.
In particular, everything goes through with no changes for f amilies of po-
larized complex tori, regardless of the positivity of the polarizat ion. In terms
of the period matrix, we still require symmetry (Riemann’s ﬁ rst bilinear re-
lation) but not positivity. This is the situation which aris es in §2.
(4) Another rather straightforward extension involves rep lacing the sym-
plectic structure σ (or rather, its inverse) by a Poisson structure, given by a
2-vectorψ ∈ Γ(Λ 2T X ) satisfying a closedness condition. Now we start with
an inclusion i : V ∗֒→T U (or α : V ∗ ⊗ O U֒→T U) and we ask whether
a given family π : X → U of abelian varieties (or complex tori) admits a
Poisson structure ψ such that π∗ψ = 0 on U and which induces the given i.
As before, the answer amounts to a cubic condition,
dp ◦i ∈ Γ(Sym 3V).
We refer to [DM] for the details.
(5) Dually, one can ask for existence of quasisymplectic str uctures
(= closed, but possibly degenerate, 2-forms) on the total sp ace X of a fam-
ily of abelian varieties, such that the family is Lagrangian , but this time
inducing a given inclusion
j :T U֒V ∗.
Again, the answer [DM] is in terms of a symmetry condition on dp, but of a
slightly diﬀerent form: the condition is that dp ⊗j, which lives in
(Sym 2V ⊗ T ∗U) ⊗ (V ∗ ⊗T ∗U),
maps under contraction to an element of V ⊗T ∗U ⊗T ∗U which is symmetric
in the last two variables, i.e. it is in V ⊗Sym 2T ∗U. (This can be contracted
withj again, to give an element of ⊗3T ∗U. The “cubic condition”, asserting
that this last tensor is in Sym 3T ∗U, follows from the previous symmetry
condition, but is in general too weak to imply it.)
(6) Several examples and applications of the cubic conditio ns are discussed
in [DM] and [M2]. Jacobi’s ACIHS (whose ﬂows include the geod esic ﬂows on
ellipsoids and the Neumann ﬂow) is particularly simple: the “cubics” turn out
to be Fermat cubics ing variables,
g∑
i=1
x3
i . These happen to have an invariance
property which can be stated as follows: the linear system of polar quadrics
(generated by the g quadricsx3
i ) is invariant under the g-dimensional group
of rescalings, xi ↦→aixi, i = 1, · · ·,g . This in turn translates into existence
8
of a g-dimensional family of two-forms on the family for which the ﬁbration
is Lagrangian, locally near each point of the base U. (Only one of these, up
to homothety, extends to a Lagrangian structure on the entir e family.)
Jacobi’s system has been extended to higher rank by Adams, Ha rnad
and Hurtubise [AHH] and by Beauville [B]. This system as well as Hitchin’s
[H] are special cases of the spectral system constructed in [ M1] and [Bn]
in terms of twisted endomorphisms of vector bundles on curve s. The Pois-
son structure on this system has a simple description in term s of the cubic
condition, cf. [DM]. A further generalization to a Lagrangi an structure on
the space of Lagrangian sheaves on an arbitrary symplectic ( or Poisson, or
quasi-symplectic) variety is given in [M2]. (This includes the various spec-
tral systems, as well as Mukai’s symplectic structure on spa ces of sheaves
on K3 surfaces, etc.) Here too, the symplectic (respectively Po isson, quasi-
symplectic) structure can be exhibited in terms of its under lying cubic, cf.
[DM].
§2. The Calabi-Yau integrable system .
In this section we construct the analytically completely in tegrable Hamil-
tonian system associated to any complete family of Calabi-Y au threefolds.
We also study the sections of this system corresponding to cu rves on the
generic Calabi-Yau.
LetX be a Calabi-Yau threefold, i.e. a three dimensional compact K¨ ahler
manifold satisfying
H 0(Ω 1
X) = H 0(Ω 2
X) = 0
ωX ≈ O X.
Here Ω i
X is the sheaf of holomorphic i-forms on X, OX = Ω 0
X is the structure
sheaf, andωX = Ω 3
X the canonical sheaf. We denote the holomorphic tangent
bundle by TX. By (holomorphic) gauge we mean a non-zero section s ∈
H 0(ωX).
Hodge theory gives us the Hodge decomposition
H 3(X, C) = H 3, 0 ⊕H 2, 1 ⊕H 1, 2 ⊕H 0, 3
and the Hodge ﬁltration
F p = ⊕i≥pH i, 3−i,
together with bilinear maps
Bp :H 1(TX) ×H p,q →H p−1,q +1
which express the variation of the Hodge structure: as X is deformed in a
direction v ∈ H 1(TX), its H p,q moves to ﬁrst order within F p−1 (Griﬃths
9
transversality) and an element w ∈H p,q moves in the direction of Bp(v,w ).
The H p,q can be described as spaces of harmonic ( p,q )-forms on X (thus
giving the inclusion H p,q֒→H 3(X, C)), or as the sheaf cohomology groups
H q(X, Ω p
X). In the case of a CY threefold X, we have:
(i) H 3, 0 = H 0(ωX) is the one-dimensional complex vector space of holo-
morphic gauges.
(ii) H 2, 1 = H 1(Ω 2) is isomorphic to H 1(TX). More canonically, each holo-
morphic gauge s ∈H 3, 0, s ⁄= 0, determines an isomorphism
⌋s :H 1(TX)
∼
→ H 2, 1
v ↦→ B3(v,s ).
(iii) H 1, 2 and H 0, 3 can be identiﬁed either with the complex conjugates of
H 2, 1 andH 3, 0 (with respect to the real subspace H 3(X, R) ofH 3(X, C)),
or with their dual spaces ( H 2, 1)∗, (H 3, 0)∗ (the pairing is given by inte-
gration over X).
The Griﬃths intermediate Jacobian of X is
J(X) := H 3(X, C)/(F 2H 3 +H 3(X, Z)) ≈ (F 2H 3)∗/λ(H3(X, Z)),
where H3(X, Z) is identiﬁed with a lattice in ( F 2H 3)∗ by the map λ :
H3(X, Z)֒→( F 2H 3)∗ which is the composition of integration
H3(X, Z) → H 3(X, C)∗
γ ↦→
∫
γ
and projection
H 3(X, C)∗ → →(F 2H 3)∗.
J(X) is a complex torus, but in general not an abelian variety: it satisﬁes
Riemann’s ﬁrst bilinear relation, but not the second. It has the important
property that it depends holomorphically on X. This means that given a
holomorphic familyχ : X → M of compact K¨ ahler manifoldsXt,t ∈ M, the
intermediate Jacobians J(Xt) ﬁt together naturally to form a holomorphic
family π : J → M , called the relative intermediate Jacobian of the family
χ.
The theorem of Bogomolov, Tian and Todorov [Bo,Ti,To] says t hat each
moduli spaceM of Calabi-Yaus is smooth and unobstructed, i.e. the Kodaira -
Spencer map gives an isomorphism
T[X]M ≈→H 1(TX)
for every CY X. We say that a family χ : X → M of CYs Xt,t ∈ M , is
complete if its classifying map M → M is a local isomorphism. It follows
10
that M is smooth with tangent space H 1(TXt) at t. Typically such families
might consist of all CYs in some open subset of M, together with some
“level” structure. We fatten the family by adding the holomo rphic gauge: let
ρ : ~M → M be the C∗-bundle over M underlying the line bundle χ∗ωX / M,
so a point of ~M is given by a pair ( X,s ) with X ∈ M ands ∈H 0(ωX)\(0).
There is a pullback family ~χ : ~X → ~M, where ~X := X × M ~M. We let
π : J → M and ˜π : ~J → ~M denote the relative intermediate Jacobians of
χ, ~χ respectively.
Theorem 3. π : ~J → ~M is an analytically completely integrable Hamil-
tonian system.
Proof.
Step I . We claim that there is a canonical isomorphism
(5) i−1 :T(X,s ) ~M ≈ F 2H 3(X, C).
Indeed, ρ : ~M → M gives a short exact sequence:
0 →T(X,s )( ~M/M) →T(X,s ) ~M → TXM → 0,
in which the subspace can be identiﬁed with H 0(ωX), and the quotient with
H 1(TX), hence via ⌋s with H 1(Ω 2
X). We need to identify this sequence
naturally with the one deﬁning F 2H 3:
0 →H 0(ωX) →F 2H 3(X, C) →H 1(Ω 2
X) → 0.
In other words, we are claiming that the extension data in the two sequences
match, globally over ~M.
For this, it suﬃces to construct a natural map from T(X,s ) ~M toF 2H 3(X, C),
which induces the identity on the subspace and quotient.
One way to obtain this map is to note that the bundle R3 ~χ∗C has the
tautological section s, which is actually in the subbundle F 3R3 ~χ∗C. The
Gauss-Manin connection applied to this section maps T(X,s ) ~M toH 3(X, C),
but by Griﬃths transversability it lands in F 2H 3. This map is easily seen to
have the required properties. For future use we want an expli cit description
of this map. We do this using Dolbeault cohomology.
Think of a 1-parameter family ( Xt,s t) ∈ ~M, depending on the parameter
t, as a ﬁxed C ∞ manifoldX on which there is given a 1-parameter family of
complex structures, speciﬁed by their ∂-operators ∂t, and also a family st of
C ∞ 3-forms on X such that st is of type (3 , 0) with respect to ∂t. Since the
st are now on a ﬁxed underlying X, we can expand with respect to t:
st =s0 +ta (mod. t2).
11
Griﬃths’ transversality now says that the derivative, a, is in F 2H 3. It clearly
depends only on ﬁrst-order data, i.e. on the tangent vector t o ~M along
(Xt,s t) at t = 0. This produces the map
T(X,s ) ~M → F 2H 3(X, C)
with the desired properties.
Step II . We want a non-degenerate 2-form σ on ~J makingπ Lagrangian.
By Theorem 1, this is equivalent to ﬁnding a cubic ˜ c on T ~M satisfying
⌋˜c = d˜p ◦i, where ˜p is the period map for ~χ : ~X → ~M and i is the inverse
of (5). Since ˜ p factors through the period map p for χ : X → M , it is
reasonable to look for a cubic c in ρ∗Sym 3T ∗M ⊂ Sym 3T ∗ ~M, satisfying
⌋c =dp ◦i. But this is precisely where the Yukawa cubic of our CY family
(also known as the Bryant-Griﬃths cubic, cf. [BG]) lives. Ab stractly, this is
cup product, followed by a “rescaling” by the gauge squared, and integration,
c :Sym 3H 1(TX) cup→ H 3(Λ 3TX) = H 3(ω−1
X ) s2
→H 3(ωX)
∫
→ C.
Hodge theoretically, this is the third iterate of the deriva tive of the period
map (or of the inﬁnitesimal variation of Hodge structure):
B1 ◦B2 ◦B3 :Sym 3H 1(TX) ×H 3, 0 →H 0, 3,
where the 1-dimensional spaces H 3, 0 and H 0, 3 ∼= (H 3, 0)∗ are trivialized by
means of s. The equality ⌋c =dp ◦i follows immediately from this interpre-
tation, cf. [CGGH].
Step III . We still need to check that the 2-form we constructed is clos ed.
We could construct an aﬃne structure on ~M and use Theorem 2. Instead, we
verify the closedness directly, and obtain the aﬃne structu re as corollary. We
do this by checking that the standard symplectic form on T ∗ ~M is invariant
under translation by the image of λ : H3( ˜X/ ˜M, Z)֒→( F 2H3)∗, hence it
descends to a symplectic form on ~J .
Since the question is local on ~M, we may assume that the bundle of
lattices R3χ∗Z on M is trivial. Let X0 be the CY ﬁber over a base point
0 ∈ M. The choice of γ0 ∈H3(X0, Z) determines a family γ = (γt)t∈M,γt ∈
H3(Xt, Z), and these are taken by λ toF 2H 3(Xt, C)∗. By the identiﬁcation
i of (5), we end up with a section
∫
γ
∈ Γ( ~M,T ∗ ~M).
We need to show that (the image of) this section is Lagrangian , with respect
to the standard symplectic form on T ∗ ~M. Equivalently, we need to show
12
that the 1-form ξ on ~M which corresponds to the section
∫
γ of T ∗ ~M is
closed.
Consider the function g : ~M → C given by
g(X,s ) :=
∫
γ
s.
We claim ξ = dg. Indeed, if a ∈ T(X,s ) ~M is the tangent vector to the
1-parameter family (Xt,s t) then we have, as in Step I:
st =s0 +ta (mod t2).
and therefore
<dg,a> = ( ∂/∂t)|t=0 g(Xt,s t)
= ( ∂/∂t)|t=0
∫
γ st
=
∫
γ a =<ξ,a>.
Q.E.D
Remark.
In order to obtain the Lagrangian structure, we did not need t o specify
the “level” of the moduli space M. In order to have an ACIHS, we need
in addition to the Lagrangian structure also a set of global H amiltonians,
i.e. a set of 1 + h2, 1 independent functions on ~M. For this, we choose the
level structure to include, at least, the choice of a Lagrang ian basis for the
H3(Xt, Z), say γ0, · · ·,γ h2,1. As our Hamiltonians we then take
˜ti :=
∫
γ i
s i = 0, · · ·,h 2, 1.
We will see another interpretation for these functions shor tly.
Lemma 2. The symplectic form σ on ~J is exact.
Proof.
For very general reasons, the symplectic form ˜ σ on T ∗ ~M is exact: it
equals d˜τ , where ˜τ is the action 1-form on T ∗ ~M. (If qi are coordinates on
~M andpi the corresponding linear coordinates on the ﬁbers, then ˜ τ is given
by
∑
pidqi and ˜σ by
∑
dpi ∧dqi.) To obtain σ, we identiﬁed T ∗ ~M with the
vertical bundle V of ~J (whose ﬁber at ( X,s ) is F 2H 3(X, C)), and observed
that ˜σ was invariant under translation by locally constant integr al cycles γ,
hence it descended to σ on ~J .
13
A ﬁrst guess for an antidiﬀerential τ ofσ might be simply ˜τ (pulled back
byi, but we suppress this), but ˜ τ is not invariant under translations: if the
cycle γ corresponds, as in Step III of the proof of Theorem 3, to a 1-fo rm ξ
on ~M, then translating by γ changes ˜τ by addition of π∗ξ, whereπ : V → ~M
is the projection. To correct this discrepancy, we consider the tautological
function f ∈ Γ( OV ) whose value at a point ( X,s,v ) ∈ V (with (X,s ) ∈ ~M
and v ∈F 2H 3(X)∗) is given by
(6) f (X,s,v ) := v(s).
Now f is ﬁber-linear, so df is constant on ﬁbers, and therefore translation
by γ changes df by π∗ of a 1-form on ~M, and this 1-form is immediately
seen to be ξ. We conclude that ˜ τ −df is a global 1-form on V which is
invariant under translation by each γ, hence descends to a 1-form τ on ~J
which satisﬁes dτ =σ, as required.
Q.E.D
Remarks.
(1) Another way to see the exactness of σ is to note that it is the sym-
plectiﬁcation of a contact structure κ on J . In general, a contact manifold
(J,κ ) determines an exact symplectic structure on the natural C∗-bundle
~J over J . Conversely, according to [AG], page 78, a symplectic struc ture
σ on a manifold ~J with a C∗-action ρ is the symplectiﬁcation of a contact
structure on the quotient J if and only if σ is homogeneous of degree 1 with
respect to ρ. In our case, there are two independent C∗-actions on the total
space of V ≈ T ∗ ~M: the C∗-action on ~M lifts to an action ρ′ on T ∗ ~M, and
there is also the action ρ′′ which commutes with the projection to ~M and is
linear on the ﬁbers. The symplectic form ˜ σ is homogeneous of weight 0 with
respect to ρ′ and of weight 1 with respect to ρ′′. Neither of these actions
descends to ~J , but their product ρ :=ρ′ ⊗ρ′′ does. The symplectic form σ on
~J is homogeneous of weight 1 with respect to ρ, so it is the symplectiﬁcation
of a contact structure on J , and in particular it is exact.
In the notation of the proof, the actions are given, for t ∈ C∗, by :
ρ′ : (X,s,v ) ↦→ (X, ts, t −1v)
ρ′′ : (X,s,v ) ↦→ (X, s, tv )
ρ : (X,s,v ) ↦→ (X, ts, v ).
The corresponding vector ﬁelds on V are taken by ˜σ to the 1-forms −df, ˜τ ,
and τ = ˜τ −df, respectively. Of these, only τ descends to a closed 1-form
on ~J . (Another description of this contact structure is in Remar k (2) to
Theorem 4.)
14
(2) The tautological relative 3-form s on ~X over ~M induces a relative
1-form on ~J over ~M. We note that our 1-form τ on ~J is a lift of this
tautological relative 1-form.
Lemma 3. The Hamiltonians ˜ti =
∫
γ is (cf. remark after Theorem 3)
are equal (up to sign) to the action variables for ~J , given by (1).
Proof.
The 3-cycle γi in X determines a 1-cycle, say Γ i, in J(X). The action
variables (1) are given as
∫
Γ iτ . By the proof of Lemma 2, τ pulls back to
˜τ −df, where f is given by (6), and ˜τ vanishes on ﬁbers of π. Therefore:
∫
Γ i
τ = −
∫
Γ i
df = −
∫
γ i
s.
Q.E.D
Let A be the group of 1-cycles in X (i.e. the free abelian group generated
by all curves), and A0 the subgroup of 1-cycles homologous to 0. There is a
well-deﬁned Abel-Jacobi map:
ν : A0 →J(X).
If the cycle C is the boundary of a 3-chain Γ, then ν(C) is the image in J(X)
of
∫
Γ , considered as an element of H 3(X, C)∗. The image is independent of
the choice of Γ. (This is the analogue for 1-cycles of the natu ral map from
divisors homologous to 0 to Pic 0(X) .)
Given a family χ : X → M of threefolds and a relative 1-cycle C → M
in A0(X/M) (i.e. for each t ∈ M , Ct is a 1-cycle homologous to 0 in Xt),
there is a corresponding section
ν(C) ∈H 0(M, J (X/M))
whose value at t ∈ M is ν(Ct) in J(Xt). This is called the normal function
of the relative cycle C.
Abstractly, a normal function is deﬁned as a section ν of J whose local
liftings to sections ν of R3χ∗C = H3 satisfy the diﬀerential equation
∇ν ∈F 1H3,
or equivalently
(7) ( ∇ν,s ) = 0,
15
where ∇ is the Gauss-Manin connection on H3. This condition is inde-
pendent of the choice of ν, by Griﬃths transversality. It is automatically
satisﬁed by the Abel-Jacobi image of a family of relative 1-c ycles, cf. [G2].
More generally, we can consider multivalued 1-cycles and no rmal func-
tions: a map B → M gives a pullback family of CYs over B, and we can
consider a family of relative, null-homologous 1-cycles in this pullback; this
determines a normal function over B, and we can consider its image (or that
of an abstract normal function over B) in J . We refer to such subvarieties
(no longer sections) of J as multivalued normal functions.
Theorem 4. For the symplectic structure on ~J constructed in Theorem
3, the image ν(A0( ~X/ ~M)) is isotropic. In other words, the normal func-
tion of any (multivalued) family of null-homologous 1-cycles on Calabi-Yau
threefolds gives an isotropic subvariety of ~J .
Proof.
This is a variation on Step III in the proof of Theorem 3. Say we are
given a family C → B of null-homologous 1-cycles on gauged Calabi-Yaus;
this means that there is a map t : B → ~M such that for b ∈ B , the ﬁber
Cb is a null-homologous 1-cycle in Xt(b). The Abel-Jacobi map ν : B → ~J
is then a lift of t, and we claim that its image is isotropic. Locally in B we
choose 3-chains Γ b such that∂Γ b =Cb; this determines local lifts ν : B → H 3
and ˜ν : B → T ∗ ~M of ν. Let ˜τ be the action 1-form on T ∗ ~M, so d˜τ is the
symplectic form. We need to show that ξ := ˜ν∗˜τ is a closed 1-form on B.
Atb ∈ B , ξ is given by
∫
Γ b. The new feature here is that instead of 3-cycles
γb ∈H3(Xb, Z) we have the 3-chains Γ b, with variable boundary Cb.
As before, we think (locally in ~M) of X as being a ﬁxed C ∞ manifold,
with variable complex structure ∂t and 3-form st, t ∈ ~M. We consider the
function deﬁned locally on B:
g : B − →C
g(b) :=
∫
Γ bst(b);
we claim that ξ =dg. This time, both the integrand and the chain in
∫
Γ bst(b)
depend on b. Let v denote an appropriate normal vector to (the support of)
Cb along Γ b. (For details, see [Gr2]). We then have:
(8) ∂
∂bg(b) =
∫
Γ b
∂st(b)
∂b +
∫
Cb
v⌋st(b).
But st(b) is of type (3 , 0) with respect to the complex structure ∂t(b), so the
contractionv⌋st(b) is of type (2 , 0), regardless of the type of v. On the other
16
hand, the (Poincar´ e dual of)Cb is of type (2, 2) with respect to this complex
structure, so the second term vanishes identically. As in th e proof of Theo-
rem 3, we then conclude that dg =ξ, as required.
Q.E.D
Remarks. The proof shows that Theorem 4 can be strengthened in two
directions:
(1) Let τ = ˜τ −df be the 1-form on ˜J constructed in Lemma 2, satisfying
dτ =σ. (The function f is given by formula (6).) Then each normal function
ν gives an integral manifold of τ , i.e. ν∗τ = 0. (This of course implies
ν∗σ = 0.) Indeed, in the notation of the proof we have ν∗˜τ =ξ andν∗f =g,
so what we show is exactly the vanishing of ν∗τ = ξ −dg. If we consider
instead normal functions for J over M (suppressing the gauge), we see that
they are integral manifolds for the contact structure on J given in Remark
1 after Lemma 2.
(2) The result of Theorem 4 holds for any normal function, not only for
those coming from cycles. In fact, the condition ν∗τ = 0 is equivalent to
Griﬃths’ diﬀerential equation for a normal function. In thi s general setting
we deﬁne the function g on B as the inner product
g := (ν,s )
of the sections ν (= the lift of ν) and s (= the (3, 0)-form). Its value depends
only on the partial lift ˜ν : B → T ∗ ~M; we have g = ˜ν∗f . The crucial formula
(8) becomes:
dg = (ν, ∇s) + (∇ν,s ).
So we have ν∗τ = ˜ν∗˜τ −dg = −(∇ν,s ), and the vanishing of ν∗τ is indeed
equivalent to the diﬀerential equation (7) of a normal funct ion.
We can deﬁne the contact structure on J , and hence the symplectic struc-
ture on ~J , in terms of normal functions: The contact distribution is g iven at
a point (X0,ν 0) ∈ J as the subspace of T(X0,ν 0)J spanned by diﬀerentials of
all normal functions ν deﬁned near X0. If we choose one such ν, we obtain
a splitting
T(X0,ν 0)J ≈ F 2H 3(X0)∗ ⊕TX0M,
in terms of which the contact distribution is
H 2, 1(X0)∗ ⊕TX0M,
and this subspace is independent of the choice of ν, by (7).
(3) An example of a “multi-valued” normal function is given b y the in-
clusion ν : B֒→~J of the total space B of a family of abelian subvarieties,
17
B → S (where S comes with a map i : S → ~M, and the ﬁber Bs is an
abelian subvariety of the torus J(Xi(s))). We conclude:
Corollary. The total space of any family of abelian subvarieties of ~J is
isotropic.
The generalized Hodge conjecture says that ν(B) is actually contained in
ν(A0( ~X/ ~M)), but this is not known. At ﬁrst sight it also seems plausibl e
that a maximal ν(B), as well as each component of ν(A0( ~X/ ~M)), should
actually be Lagrangian; there are, however, counterexamples to this.
The intermediate Jacobian is the connected component of the origin in a
larger group D(X), the Deligne cohomology group of X, cf. [EZ]. This ﬁts
in the exact sequence
0 →J(X) →D(X)
ϕ
→H 2, 2(X, Z) → 0,
where H 2, 2(X, Z) := H 2, 2(X, C) ∩H 4(X, Z). For a Calabi-Yau, this is the
same as H 4(X, Z). (The relation of D to J is analogous to that of Pic to
Pic 0.) The Abel-Jacobi map A0(X) → J(X) extends to an Abel-Jacobi
(aka cycle-class) map,
ν : A(X) →D(X),
such that ϕ ◦ν : A(X) →H 2, 2(X, Z) sends a cycle to its fundamental class.
Everything works well for families: a family X → M determines a relative
Deligne group D(X/M) whose ﬁber over t ∈ M is D(Xt), and there is an
Abel-Jacobi map
ν : A(X/M) → D (X/M)
which ﬁber-by-ﬁber agrees with the previous ν.
Theorem 5. Let D = D(X/M) be the relative Deligne group of a com-
plete family of CY threefolds, let ~D = D( ~X/ ~M) be the relative Deligne
group of the gauged family, and let J, ~J be the corresponding relative Jaco-
bians. Then there is a natural contact structure κ on D with symplectiﬁcation
σ =dτ on ~D with the following properties:
(a) σ,τ andκ restrict to the previously constructed structures on ~J and J .
(b) The ﬁbration ~D → ~M is Lagrangian.
(c) All normal functions ν(A( ~X/ ~M)) are integral manifolds for τ (hence
isotropic for σ), and normal functions ν(A(X/M)) are integral mani-
folds for κ.
18
Proof.
Each component of D (respectively ~D) is locally isomorphic to J (respec-
tively ~J . In order to extend σ,τ,κ we need a collection of local sections of
D (and ~D) with the properties:
(1) For each t ∈ M and each component of D(Xt), there is a local section
deﬁned near t and passing through this component.
(2) The diﬀerence of any two local sections in the same compon ent is an
integral manifold for σ,τ,κ .
Indeed, such a collection of sections determines a collecti on of local iso-
morphisms of components of D (respectively ~D) with J (respectively ~J ), so
we deﬁne σ,τ,κ as pullbacks of the corresponding structures on ~J and J .
This is well-deﬁned by (2), and covers ~D and D, by (1). Now such a collection
is given, in our case, by the normal functions of all 1-cycles , ν(A(X/M)):
property (1) follows from the Lefschetz theorem on (1 , 1)-classes, and prop-
erty (2) amounts to our Theorem 4 and the remarks following it .
Q.E.D
As an immediate corollary, we get the following result of Gri ﬃths [G1].
(There it is proved only for quintic threefolds, but the argu ment works in
general, once we know the unobstructedness of moduli [Bo,Ti ,To].)
Corollary. On a generic CY, algebraic equivalence of 1-cycles implies
AJ-equivalence; in other words, the Abel-Jacobi map is consta nt on any
connected family of 1-cycles.
Proof.
The AJ image of the family is isotropic, by Theorem 5, and dominates
~M, hence it is Lagrangian and meets the generic ﬁber discretel y, so the AJ
map is locally constant on the connected family, hence const ant.
Q.E.D
Note. These results have analogues for Calabi-Yaus of odd dimens ions n =
2k + 1 ≥ 3: The universal kth intermediate (or middle-dimensional) Jacobian
~J k( ~X/ ~M), as well as the corresponding relative Deligne cohomology , have
19
natural quasi-symplectic structures, i.e. closed 2-forms which in general will
be degenerate. The ﬁbers of the projections of ~J or ~D to ~M are Lagrangian,
i.e. maximal isotropic with respect to the 2-form (but of dim ension greater
than dim ~M, because of the degeneracy). All normal functions, or Abel-
Jacobi images of families of k-cycles, are isotropic. For the details, see [DM].
§3. Mirrors.
To a given family X → M of Calabi-Yaus, there are two ways of asso-
ciating an (N = 2, c = 9) (super) conformal ﬁeld theory (CFT). Physicists
refer to these as the A-model and B-model theories. A key quantity in the
CFT is its partition function , which is a cubic form on a vector space V ,
depending on some auxiliary parameters q.
In the A-model, one takes V := H 1, 1(X) = H 2(X, C), where X is a
general CY in the given family. On it there is the cubic form To po, giving
the topological cup product. For each k ∈ H2(X, Z) ≈ H 2(X, Z)∗ (we
replace Z-homology or cohomology by its image in the Q-(co)homology, i.e.
we ignore torsion classes), we think of k3 as a cubic form on V . The partition
function is then:
(9) Topo +
∑
k,d
nkk3qdk.
In the summation, k runs over H 2(X, Z)∗ and d over positive integers. The
coeﬃcient nk is the “number of rational curves” of fundamental class k in
