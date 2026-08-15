---
doc_id: arxiv-2601.15862v1
doc_title: "SYNTHETIC DIFFERENTIAL JET BUNDLES ARE REDUCED"
section_id: sec-001-2-statement-and-proof
section_title: "Statement and Proof"
section_number: 2
pages: 1-14
source_pdf: 2601.15862v1.pdf
source_sha256: e37fa9b4515f58d1
doc_brief: "SYNTHETIC DIFFERENTIAL JET BUNDLES ARE REDUCED — We have previously observed that the theory of solutions of par- tial differential equations, regarded asdiffietiesinside jet bundles, acquires a"
---
Appendix A. Background 9
References 14
1.Introduction
The tenet ofsynthetic differential geometry(SDG, cf. [Koc79; Lav96; Koc10])
is that concepts and results in differential geometry often find a more natural and
powerful formulation after faithfully embedding the category of smooth manifolds
into a suitabletopos(cf. [MM92; Bor94]) whereinfinitesimal spacesexist as actual
objects.
Such a “well-adapted” SDG topos is theCahiers toposdue to E. Dubuc ([Dub79],
cf. [GS25b,§2]), which we may think of as the category offormal smooth sets
(recalled in§A.1 — here “formal” is common jargon for “infinitesimally thickened”
or “haloed”). This is a differential-geometric analog of working withformal schemes
in algebraic geometry.
One striking example is from the geometry of partial differential equations. On
top of describing classical solutions, SDG can treat formal (power series) solutions
of partial differential equations as primary objects. Classically, these formal solu-
tions appeared in the guise ofdiffietiesinside infinite jet bundles (a very fruitful
perspective due to [Vin81], brief background is recalled in§A.3). Their appearance
Date: January 23, 2026.
2020Mathematics Subject Classification.Primary: 58A03, 51K10, 58A20 Secondary: 18F15,
35A30 .
Key words and phrases.Synthetic differential geometry, infinite jet bundles, Cahiers topos,
formal smooth sets.
Funding: IK’s work is supported by theCzech Academy of SciencesResearch Plan
RVO:67985840. The remaining authors are supported byTamkeen UAEunder theNYU Abu
Dhabi Research Institute grantCG008.
1
arXiv:2601.15862v1  [math.DG]  22 Jan 2026
2 GRIGORIOS GIOTOPOULOS, IGOR KHAVKINE, HISHAM SATI, AND URS SCHREIBER
in SDG turns out to become largely structural (namelycomonadic) when viewed in
the synthetic context of formal (infinitesimally thickened) smooth sets. This is the
result of [KS26]. However, a key technical step in this identification had remained
unproven, recalled as Thm. 2.1 below:
Namely, withinfinite jet bundles(A.9) being projective limits of finite-dimensional
manifolds, there area prioritwo different ways of regarding them among formal
smooth sets: Either by first taking the limit (in Fr´ echet manifolds) and then passing
to formal smooth sets, or the other way around! We prove here that that these two
constructions are naturally isomorphic.
This has crucial implications for applications in variational calculus and in La-
grangian field theory, cf Cor. 2.2 below.
The result may be “intuitively expected” to be true, but proving it is not entirely
trivial. Here we provide a detailed and largely constructive proof. Besides filling
this particular gap in the previous literature, our proof may be interesting for the
technique it uses, which seems to be new, and may be adapted to other situations,
cf. Rem. 2.7 below.
2.Statement and Proof
We writei ! (Def. A.7) for the inclusion of smooth sets — such as Fr´ echet mani-
folds (Lem. A.9) — among formal smooth sets.
Theorem 2.1.For E Σ a finite-dimensional surjective submersion of smooth
manifolds, passage to formal smooth sets preserves the projective limit involved in
forming its infinite jet bundleJ ∞
Σ E(cf.§A.3), in that there is a natural isomor-
phism:
(2.1)i !
(
lim←−k∈N
Jk
ΣE
)
≃lim←−k∈N
(
i!Jk
ΣE
)
.
By the characterization [KS26, Prop. 2.29; GS25a, Cor. 3.6] of smooth maps out
of Fr´ echet projective limit manifolds (“locally pro-manifolds”), Thm. 2.1 implies:
Corollary 2.2.The maps of formal smooth sets from a synthetic jet bundleJ ∞
Σ E
to a finite-dimensional manifoldFis in canonical bijection with point-set smooth
maps which are locally of finite jet order(as considered in [Tak79]).
We prove Thm. 2.1 below after establishing a few lemmas, based on the following
recognition principle for reduced objects among formal smooth sets:
Lemma 2.3.An objectX∈FrmSmthSetisreduced (A.2)iff the following two
conditions hold:
(i)All germs of maps out of aU×D∈FrmCrtSpintoXfactor through some
V∈CrtSp :
(2.2) ∀U×D V X.
∀
∃ι ∃f
SYNTHETIC DIFFERENTIAL JET BUNDLES ARE REDUCED 3
(ii)The equivalence relation on the set of such factorizations(ι,f)which is
generatedby the relation
(2.3) (ι,f)∼(ι ′,f)⇔
V
U×D X
V′
∃
fι
ι′ f′
is that of equal composites, hence:
(2.4) (ι,f)∼
∃
···∼(ι ′,f′)⇔f◦ι=f ′◦ι′.
Proof.This is an immediate reformulation of the followingcoendformula for the
left Kan extension on presheaves (cf. [Kel82, p. 4.25; Lor21, (2.27)]):
(2.5) (i !X)(U×D)≃
∫V∈CrtSp
FrmCrtSp(U×D, V)×X(V),
which (seen under the Yoneda lemma) says that mapsU×D i!X in FrmSmthSet
are in natural bijection to equivalence classes of pairs consisting of a mapU×D V
(in FrmCrtSp FrmSmthSet) into a Cartesian space V∈CrtSp FrmCrtSpi
and a mapV X in SmthSet, subject to the equivalence relation which is gener-
ated by compatible maps ϕ:V V′ (in CartSp) between the factor spaces:
{
U×D i!X
}
≃
{(
U×D Vι ,V X
f )}/ 




V V
U×D X
V′, V′
ϕ ϕ
fι
ι′ f′




,
where on the right we mean that a pair as on the top of the diagram is in relation
to a pair as shown at the bottom ifϕexists that makes the two triangles commute.
Under passage to sheaves (A.3) this statement holds on germs of maps, as
claimed.□
The archetype of Thm. 2.1 is the statement that the projective limit defining
the projectively infinite-dimensional Cartesian space (cf. [KS26, Def. 2.24, Prop.
2.26]),
(2.6)R ∞ := lim←−
(
R2 R1 R0
)
∈ FrchtMfd SmthSet(A.8) ,
is preserved:
Proposition 2.4.Passage to haloed smooth sets preserves the projective limit in-
volved in forming the infinite Cartesian space(2.6):
(2.7)i !
(
lim←−k∈N
Rk
)
≃lim←−k∈N
(
i!Rk
)
.
Proof.It will suffice to observe that the right-hand side of (2.7) is reduced (proved
below in Lem. 2.5), whence (using (A.7)):
(2.8) lim ←−k∈N
(
i!Rk
)
=ℜlim←−k∈N
(
i!Rk
)
≃i !i∗ lim←−k∈N
(
i!Rk
)
.
4 GRIGORIOS GIOTOPOULOS, IGOR KHAVKINE, HISHAM SATI, AND URS SCHREIBER
With that and by full faithfulness ofi ! (Lem. A.8), the claim is equivalent to:
(2.9) lim ←−k∈N
Rk ≃i ∗
(
lim←−k∈N
(
i!Rk
))
.
But this holds sincei ∗ commutes with (projective) limits (being a right adjoint)
and then using (A.5).□
Hence the key is to see that:
Lemma 2.5.The limiting objectlim←−k(i!Rk)is reduced(A.2).
Proof.In view of Lem. 2.3, we first show that every top map of the following form
factors through someV∈CrtSp as shown at the bottom:
U×D V lim←−k∈N
(
i!Rk
)
.
Since we are dealing with maps into a limit, we need to equivalently see that every
commuting diagram of maps of the form
U×D
i!R3 i!R2 i!R1 i!R0
factors in this form:
U×D
V
i!R3 i!R2 i!R1 i!R0.
Now, a map U×D i!Rk in FrmSmthSet is just a morphism in FrmCrtSp of the
form U×D Rk (becausei ! preserves representables, cf. Lem. A.8), hence is a
k-tuple
(
[fi]
)k
i=1 of elements ofC ∞(U×D). By Def. A.6, every such element [f i] is
an equivalence class of an elementf i ∈C ∞(U×R d), for somed∈Ndepending
only onD. Hence, if we takeV:=U×R d then we may choose thesef i for each
given [fi]:
U×D
U×Rd
Rk+1 Rk
([fi])k+1
i=1 ([fi])k
i=1
(fi)k+1
i=1 (fi)k
i=1
to achieve the desired factorization.
In order to conclude with Lem. 2.3, we still need to show that any two such factor-
izations of the same map are related by a compatible zig-zag (2.4) of maps between
the intermediateVs. This follows from: (i) the evident observation that every fac-
torization is related to one whereιis a formal proper embedding of arbitrarily high
SYNTHETIC DIFFERENTIAL JET BUNDLES ARE REDUCED 5
codimension (Lem. A.11), combined with (ii) the more laborious verification that
any two of these whose composites are equal are in zig-zag relation to each other.
This is finally shown as Lem. 2.8 below.□
With this we conclude:
Proof of Thm. 2.1.The key is to observe that the right hand side of (2.1) is re-
duced, in that
lim←−k∈N
(
i!Jk
ΣE
)
≃i !i∗ lim←−k∈N
(
i!Jk
ΣE
)
,
from which the claim will follow formally, just as in the proof of Prop. 2.4: Sincei !
is fully faithful, the desired condition (2.1) thereby becomes equivalent to:
lim←−k∈N
(
Jk
ΣE
)
≃i ∗ lim←−k∈N
(
i!Jk
ΣE
)
,
which holds, sincei ∗ commutes with projective limits (being a right adjoint) and
then using thati ∗◦i !≃id (A.5).
To see that the right-hand side of (2.1) is indeed reduced, consider a dashed
horizontal map of the form
U×D lim←−ki!Jk
ΣE
i!Σ,
where at the bottom we are indicating the induced map to Σ, over which everything
is fibered. By Lem. 2.3 we need to show that a germ of the horizontal dashed
map factors through a Cartesian space. By the fact that E Σ is assumed to
be a surjective submersion, and hence similarly all ofJ k
ΣE→J k−1
Σ E→ ··· →
Σ, there is a representative of the germ of eachU×D→i !Jk
ΣEwhich factors
through a trivial fibrationU k×D↪→i !Jk
Rn Rn+m. But upon further restriction
to common overlaps, these yield a representative for the germ of the original map
U×D→lim←−ki!Jk
ΣE(with domain to be denoted U
′
U) which factors through
the corresponding jet bundle of a trivial fibration:
U′×D lim←−ki!Jk
Rn Rn+m lim←−ki!Jk
ΣE
i!Rn+m i!E
i!Rn i!Σ.
⌟
Thereby we have reduced the situation to essentially that of Prop. 2.4 and the proof
follows analogously.□
It just remains to prove the very last statement in the proof of Lem. 2.5. This
is the step that requires most of the work, we prove it as Lem. 2.8 below.
Notation 2.6.For ease of notation we shall now abbreviate the “synthetic differ-
ential version” ofR ∞ (2.6) as
(2.10)R ∞ := lim←−k
i!Rk ∈FrmSmthSet
6 GRIGORIOS GIOTOPOULOS, IGOR KHAVKINE, HISHAM SATI, AND URS SCHREIBER
(though once we are done with the proof of Lem. 2.8, Prop. 2.4 asserts thatR ∞ is
isomorphic toi !R∞).
Remark2.7.Sincei !Rk =R k ∈FrmCrtSp (A.4), the plots ofR ∞ (2.10) are
nothing butN-tuples of smooth functions:
Hom(U×D,R ∞)≃lim←−k∈N
Hom(U×D,R k)≃
∏
k∈N
Hom(U×D,R 1)
≃
∏
k∈N
C∞(U×D).
This means in particular that we may add and subtract among these plots (used
in (2.14) and (2.17) below) and apply Hadamard’s lemma to them (used in (2.13)
and (2.16) below).
In fact, in the following proof we only use that elements ofC ∞(U,R∞) (forU∈
CrtSp) are additive and subject to Hadamard’s lemma, and hence the analogous
argument applies in caseR ∞ is replaced by any other object for which this is the
case.
Lemma 2.8.Given an outer commuting diagram as follows:
V
U×D W R∞,
V′
fαι
ι′
ϕ
f′
α′
whereιandι ′ are formal proper embeddings(Def. A.10)of sufficiently high codi-
mension, there existsW∈CrtSpsuch that the diagram may be filled by dashed
maps as shown, making all triangles commute.
In order to make the proof of Lem. 2.8 transparent, we present it in stages
of increasing generality. We begin with the simple case whereU≡ ∗andD≡
D1(1)≡Spec
(
C∞(R1)/(x2)
)
.
Lemma 2.9.Given a commuting diagram of smooth functions of the form of the
outer solid arrows in the following diagram:
V
D1(1) W R∞
V′
fαι
ι′
ϕ
f′
α′
↔
TV
∗ TW TR∞,
TV′
Tf
Tα˜ι
˜ι′
Tϕ
Tf′
Tα′
whereιandι ′ are monomorphisms, then there existsW∈CrtSpand smooth maps
corresponding to the dashed arrows that make the whole diagram commute.
Proof.We may assume without restriction of generality that the base points picked
byιandι ′ are the origins of 0∈Vand 0∈V ′, respectively (otherwise reparametrize),
hence that
˜ι(•) =:v 0∈T 0V,
˜ι′(•) =:v ′
0∈T 0V′.
SYNTHETIC DIFFERENTIAL JET BUNDLES ARE REDUCED 7
The assumption thatιandι ′ are monomorphic means thatv 0̸= 0 andv ′
0̸= 0.
Therefore (writingV⊥⊂Vfor the orthogonal subspace tov 0 andV ′
⊥⊂V ′ for the
orthogonal subspace tov ′
0), we may coordinatizeVandV ′ by:
R×V ⊥ V
(t,⃗ x)↦−→(tv0,⃗ x),
∼ R×V ′
⊥ V′
(t′,⃗ x′ ) ↦−→(t′v′
0,⃗ x′).
∼
Now set
W:=V×V ′×R 1
and
V W
(t,⃗ x)↦−→
(
(t,⃗ x),(t,0),0
)
,
α V′ W
(t′,⃗ x′) ↦−→
(
(t′,0),(t′,⃗ x′),t′2
)
.
α′
Since
α(0,0) =
(
(0,0),(0,0),0
)
,
α′(0,0) =
(
(0,0),(0,0),0
)
,
∂
∂tα(0,0) =
(
(1,0),(1,0),0
)
,
∂
∂t′α′(0,0) =
(
(1,0),(1,0),0
)
,
this makes the left part of our diagram commute.
Finally, to defineϕ, first consider
δ:R−→R ∞(2.11)
t↦−→f′(t,0)−f(t,0).(2.12)
By the commutativity of the outer diagram, we haveδ(0) = 0 and d
dtδ(0) = 0.
Hence by Hadamard’s lemma there is a smooth function
(2.13) µ:R R∞,such thatδ(t) =t 2·µ(t).
With that function in hand, finally define
(2.14)ϕ:
(
(t,⃗ x),(t′,⃗ x′),j
)
↦−→f(t,⃗ x)−f′(t,0) +f ′(t,⃗ x′) +j·µ(t).
We check that this makes the right part of our diagram commute, since:
ϕ◦α(t,⃗ x) =ϕ
(
(t,⃗ x),(t,0),0
)
=f(t,⃗ x) + 0 + 0,
and
ϕ◦α ′(t′,⃗ x′) =ϕ
(
(t′,0),(t′,⃗ x′),t′2
)
=f(t ′,0)−f ′(t′,0)/bracehtipupleft/bracehtipdownright/bracehtipdownleft/bracehtipupright
−δ(t′)
+f′(t′,⃗ x′) +t′2·µ(t′)/bracehtipupleft/bracehtipdownright/bracehtipdownleft/bracehtipupright
δ(t′)
=f ′(t′,⃗ x′).
This completes the proof.□
Next, we generalize this proof to the case where (stillU≡∗but)Dis arbitrary.
To that end, choose an inclusion D Rd with minimaldand choose a set of
generators
(2.15) ⃗h:=
(
hi∈C ∞(Rd)
)n
i=1
(for somen∈N)
for the kernel of the dual algebra homomorphism C∞(Rd) C∞(D).
8 GRIGORIOS GIOTOPOULOS, IGOR KHAVKINE, HISHAM SATI, AND URS SCHREIBER
Lemma 2.10.Given a commuting diagram of smooth functions of the form of the
outer solid arrows in the following diagram:
V
D W R∞,
V′,
fαι
ι′
ϕ
f′
α′
whereιandι ′ are monomorphisms, then there existsW∈CrtSpand dashed maps
also making the inner diagram commute.
Proof.Without restriction of generality we may assume thatι(0) = 0∈Vand
ι′(0) = 0∈V ′ (otherwise reparametrize). Sinceιandι ′ are monomorphic, we may
decomposeV,V ′ respectively into the span of the image ofι,ι ′ and its orthogonal
complement, respectively:
Rd×V⊥ V ,
Rd×V ′
⊥ V′.
∼
∼
Now take
W:=V×V ′×Rn
and
α(⃗t,⃗ x) :=
(
(⃗t,⃗ x),(⃗t,0),0
)
α′(⃗t′,⃗ x′) :=
(
(⃗t′,0),( ⃗t′,⃗ x′),⃗h(⃗t′)
)
,
where the last component are the values of the generators (2.15) of the nil ideal.
Then we have the following composites (where in the lower lines we show the
pullback of the canonical coordinate functions along the top map, whose inspection
is sufficient for identifying these maps, cf. [GS25b, Prop. 4.6])
D Rd×V⊥ Rd×V⊥× Rd×V′
⊥× Rn
[⃗t] ⃗t ⃗t
0 ⃗ x ⃗ x
[⃗t′] ⃗t′ ⃗t′
0 0 ⃗ x′
0 0 ⃗j
ι α
and
D Rd×V ′
⊥ Rd×V⊥× Rd×V′
⊥× Rn
[⃗t] ⃗t ⃗t
0 0 ⃗ x
[⃗t′] ⃗t′ ⃗t′
0 ⃗ x′ ⃗ x′
0 ⃗h(⃗t′) ⃗j,
ι′ α′
where in the last line we use that the functions⃗h(2.15) vanish onD, by assumption.
Since these two composite maps hence agree, the left part of our diagram commutes.
SYNTHETIC DIFFERENTIAL JET BUNDLES ARE REDUCED 9
Now consider
Rd R∞
⃗t ↦−→f′(⃗t,0)−f( ⃗t,0).
δ
By the commutativity of the outer part of our diagram, the components of this
map are in the ideal spanned by theh i (2.15), so that
(2.16)δ( ⃗t) = ∑
ihi(⃗t)µ i(⃗t) for some ( µi :R d R∞)n
i=1.
With this in hand, finally define
(2.17)ϕ
(
(⃗t,⃗ x),(⃗t′,⃗ x′ ), ⃗j
)
:=f( ⃗t,⃗ x)−f′(⃗t,0) +f ′(⃗t,⃗ x′) +∑
ijiµi(⃗t).
We check by direct computation that this indeed makes the right part of our diagram
commute:
ϕ◦α( ⃗t,⃗ x) =ϕ
(
(⃗t,⃗ x),(⃗t,0),0
)
=f( ⃗t,⃗ x) + 0 + 0
and
ϕ◦α ′(⃗t′,⃗ x′) =ϕ
(
(⃗t′,0),( ⃗t′,⃗ x′),⃗h(⃗t)
)
=f( ⃗t,0)−f ′(⃗t,0)/bracehtipupleft/bracehtipdownright/bracehtipdownleft/bracehtipupright
−δ(⃗t)
+f′(⃗t,⃗ x′) +∑
ihi(⃗t)µ i(⃗t)/bracehtipupleft/bracehtipdownright/bracehtipdownleft/bracehtipupright
δ(⃗t)
=f ′(⃗t,⃗ x′).
This completes the proof.□
Finally, it is not much more work to lift this proof to full generality:
Proof of Lem. 2.8.By Lem. A.12 we may assume, without restriction of generality,
that, up to diffeomorphism on the target:
ι|U×{∗} ≃(id ,0) :U U× ˜V≃V
ι′|U×{∗} ≃(id,0) :U U× ˜V′≃V ′.
But under this identification, we have over each pointu∈Uthe exact situation
of Lem. 2.10, and hence the solution is as given there, just withWhaving another
factor ofUand withα,α ′ andϕdepending on a further variableu∈U.
Concretely, in generalizing Lem. 2.9 this way:
(i)The parametrization ofVis now as a bundle overU×R, with (u,t·
v(u),⃗ xv(u))∈V, where⃗ x v(u) are elements perpendicular tov(u).
(ii)The correspondingδis now a mapU×R→R ∞ which satisfiesδ(u,0) = 0,
∂
∂tδ(u,0) = 0 and so, by thepartial/parameterized versionof Hadamard’s
lemma Thm. A.5, may be written asδ(u,t) =t 2·µ(u,t) for a smooth
µ:U×R→R ∞.□
AppendixA.Background
For reference in the main text, here we briefly record some basic definitions and
facts.
10 GRIGORIOS GIOTOPOULOS, IGOR KHAVKINE, HISHAM SATI, AND URS SCHREIBER
A.1.Formal Smooth Sets.We briefly review the topos offormal smooth sets
([Sch13, Def. 4.5.5; KS26,§2.1; GS25b,§2], exposition in [Sch25]), equivalent (by
[GS25b,§4.1]) to Dubuc’sCahiers topos[Dub79; KR87], which is a “well-adapted
model” for synthetic differential geometry.
Our ground field is the real numbers. We write CAlg for the category of com-
mutativeR-algebras.
Definition A.1. (i)We write CrtSp for the category whose objects are the
Cartesian spacesR n,n∈N, and whose morphisms are the smooth func-
tions between these. Hence this is the full subcategory of smooth manifolds
CrtSp SmthMfd
on the Cartesian spaces. We will denote generic Cartesian spaces byU,V∈
CrtSp.
(ii)We regard this category as a site by equipping it with the coverage (Grothendieck
pre-topology) of differentiably good open covers.
Proposition A.2(cf. [KMS93,§35]).The functor which forms (plain)R-algebras
of smooth functions constitutes a full inclusion of smooth manifolds, hence in par-
ticular of Cartesian spaces(Def. A.1):
CrtSp SmthMfd CAlgopC∞(−)
Definition A.3.The category ofinfinitesimally thickened points(haloed points)
is the full subcategory of the opposite of commutative algebras
FrmPnt CAlgop
D ↦−→C∞(D).
on those what are calledWeil algebrasin the SDG literature orArtin local algebras
in algebraic geometry, namely those of the form
C∞(D)≃ R R⊕V ,
whereV⊂C ∞(D) is a finite-dimensional ideal which isnilpotentin that
∃k∈N :V k+1 = 0.
The smallestkfor which this holds is theorder of nilpotencyofD.
Example A.4.Aninfinitesimal diskof dimensiond∈Nand order of infinitesi-
malityk∈Nis an infinitesimally thickened pointD d(k)∈FrmPnt (Def. A.3) of
the form
C∞
(
Dd(k)
)
≃C ∞(Rd)/(x1,···,x d)k+1
≃R[ϵ 1,···,ϵ d]/(ϵ1,···,ϵ d)k+1.
The second equivalence above follows by Hadamard’s lemma, which we repeat-
edly refer to. For reference, we state it in a version that covers both parameters
and partial derivatives:
SYNTHETIC DIFFERENTIAL JET BUNDLES ARE REDUCED 11
Lemma A.5(Hadamard’s Lemma, cf. [DK04, Lem. 2.2.7], we follow [GS25b,
Lem. 4.1]).For any smooth functionf(x,y)∈C ∞(Rk×R m)and anyl∈N,
there exist smooth functions{h i1···il+1}i1,···,i l+1=1,···,m ⊂C ∞(Rk×Rm)such that
f=f(x,0) +
m∑
i=1
yi∂yif(x,0) + 1
2
m∑
i,j=1
yiyj∂yi∂yjf(x,0)
+···+ 1
l!
m∑
i1,···,i l=1
yi1···y il·∂yi1···∂ yilf(x,0)
+
m∑
i1,···,i l+1=1
yi1···y il+1·hi1···il+1(x,y).
Definition A.6. (i)The category offormal Cartesian spacesis the full sub-
category of the opposite of commutative algebras,
FrmCrtSp CAlgop
U×D ↦−→C∞(U)⊗ RC∞(D),
C∞(−)
on those which are tensor products of an algebra of smooth functions on a
U∈CrtSp (cf. Prop. A.2) with those on aD∈FrmPnt (Def. A.3).
(ii)We regard this category as a site by equipping it with the coverage (Grothendieck
pre-topology) whose covering families are of the form
{
Ui×D U×D
ιi×id }
i∈I
for
{Ui U
ιi
}i∈I
a covering family in CrtSp (a differentiably good open cover).
By construction, we have a fully faithful inclusion of sites:
(A.1) CrtSp FrmCrtSp
U ↦−→U×D 0.
i
Definition A.7.We say that the sheaf topos
(i)over CrtSp is the category ofsmooth sets,
(ii)over FrmCrtSp is the category offormal smooth sets,
and that the essential image of the former under the left base changei ! along the
inclusion (A.1) constitute thereducedformal smooth sets:
(A.2) SmthSet := Sh(CrtSp) Sh(FrmCrtSp) =: FrmSmthSet,
i!
⊥
i∗
Herei ! on sheaves is theleft Kan extensioni ! of presheaves (2.5) followed by
sheafificationL, and we are using thati ∗ manifestly preserves sheaves:
(A.3)
PSh(CrtSp) PSh(FrmCrtSp)
Sh(CrtSp) Sh(FrmCrtSp).
i!
⊥
i∗
i!
⊥
i∗
⊥ L
Now, basic category theory shows the following important properties:
12 GRIGORIOS GIOTOPOULOS, IGOR KHAVKINE, HISHAM SATI, AND URS SCHREIBER
Lemma A.8.The inclusioni ! in(A.2):
(i)preserves representables V∈CrtSp SmthSet in that:1
(A.4) i!V≃V≡V×D 0∈FrmCrtSp FrmSmthSet,
(ii)is fully faithful, hence
(A.5)i ∗◦i !≃id,
(iii)and such that thereducedobjects X∈SmthSet FrmSmthSet
i!
are equiv-
alently those which are isomorphic to theirpurely reduced aspectℜ(X),
(A.6)X≃ℜ(X),
where
(A.7)ℜ:=i !◦i∗.
Proof.The first statement follows with the coend formula (2.5): Every pair (ι,f) (of
maps into a Cartesian spaceVfactoring through a Cartesian spaceW) is equivalent
to its actual composite regarded as the pair (f◦ι,id), like this:
W
U×D V.
V
f
f
ι
f◦ι id
This shows thati ! on presheaves preserves representables. Finally, our coverage is
clearly subcanonical in that representable presheaves are already sheaves.
For the second statement cf. [Kel82, Prop. 4.23] with [Mac98,§IV.3 Thm. 1].
From this the last statement follows.□
A classical notion in infinite-dimensional differential geometry areFr´ echet man-
ifolds(cf. [Ham82,§I.4]). These are faithfully subsumed here:
Lemma A.9.The evident inclusion of Fr´ echet manifolds among smooth sets(and
hence further among formal smooth sets Def. A.7)
(A.8)
FrchtMfd SmthSet
X ↦−→
(
U↦→C∞(U,X)
)
is fully faithful.
Proof.This is essentially the statement of [Los94, Thm. 3.1.1], cf. [KS26, Prop.
2.22]. □
A.2.Formal embeddings.
Definition A.10.A map i:U×D V in FrmCrtSp (Def. A.6) is aformal
embeddingif its restriction toU×{0}is an embedding of smooth manifolds and its
restriction to each{u}×Dis a monomorphism. Moreover, this is aproperformal
embedding if the restriction toU×{0}is also a proper map.
The following lemma is immediate but still worth recording:
1We are leaving the Yoneda embedding notationally implicit.
SYNTHETIC DIFFERENTIAL JET BUNDLES ARE REDUCED 13
Lemma A.11.Every U×D V Xi f
is equivalent(2.3)to(ι,f ′), whereιis
a formal proper embedding(Def. A.10)of arbitrarily high codimension.
Proof.Choose a monomorphism (wheredmay be arbitrarily large) of the form
δ:U×D U×R d (cf. [GS25b, Cor. 4.3(iii)]), note that this makes the fol-
lowing diagram commute:
V
U×D X,
V×(U×R d)
fi
ι:=(i,δ)
f′:=f◦pr V
prV
and finally observe thatι:= (i,δ) is a formal proper embedding.□
Lemma A.12.For every proper embedding ι:R n Rn+c of sufficiently high
codimensionc, there exists a diffeomorphism ofR n+c under which the embedding
is a rectilinear inclusion:i≃(id,0).
Proof.First we claim that there exists a proper smooth homotopy fromito (id,0).
This may be seen by observing that proper maps extend to pointed maps between
one-point compactifications (cf. [Jam84, p. 80]). In our case the extended maps
are of the form Sn Sn+c and hence pointed null-homotopic forc≥1. This
pointed null-homotopy comes from a proper homotopy between the original maps
as desired.
From this it follows thatiis related to (id,0) by ambient isotopy (with [Hir76,
§8.1 Exc. 11], which requiresc >1 +n) and thus by diffeotopy (with [Hir76,§8.1
Thm. 1.3]).□
A.3.Jet Bundles.For traditional background on jet bundle geometry cf. [Sau89;
Tak79].
A finite-rankjet bundleJ k
ΣEis the bundle of all possible partial derivatives,
of order≤k, of sections of a given surjective submersion p:E Σ of smooth
manifolds.
This traditional notion has a slick synthetic differential formulation ([KS26,
§3.3][GS25b,§2.4]) in terms of the maximal infinitesimal disksDs(k) Σ (Ex. A.4)
around any points∈Σ: The fiber ofJ k
ΣEoversconsists of the sections ofpover
Ds(k):
(Jk
ΣE)s≃FrmSmthSet /Σ
(
Ds(k), E
)
≡



E
Ds(k) Σ
p



,
andJ k
ΣEcanonically inherits the structure of a smooth manifold this way.
Now, the evident inclusions Ds(k) Ds(k+ 1) thus induce natural projections
Jk+1
Σ E Jk
ΣE, and theinfinite rankjet bundle (cf. [Sau89,§7]) is the projective
limit over these projections:
(A.9)J ∞
Σ E:= lim←−k∈N
Jk
ΣE.
14 GRIGORIOS GIOTOPOULOS, IGOR KHAVKINE, HISHAM SATI, AND URS SCHREIBER
Traditionally, this limit is understood in the category of Fr´ echet manifolds (cf.
Lem. A.9), and it is nota prioriclear how this relates to the corresponding limit
formed in formal smooth sets, since the inclusioni ! (A.2) does not preserve limits
in general
Thati ! does preserve the particular limits (A.9) is the content of our main result
Thm. 2.1.
