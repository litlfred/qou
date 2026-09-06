---
doc_id: arxiv-1011.6483v3
doc_title: "DERIVED HIGHER HOCHSCHILD HOMOLOGY"
section_id: sec-005-33-pointed-simplicial-sets-and-modules
section_title: "Pointed simplicial sets and modules"
section_number: 3.3
pages: 22-37
source_pdf: 1011.6483v3.pdf
source_sha256: 7a425e51860c37a4
doc_brief: "DERIVED HIGHER HOCHSCHILD HOMOLOGY — W e study the higher Hochschild chain functor, factorizatio n alge- bras and their relationship with topological chiral homolo gy."
---
how to add an A-module M to the story developed in Section 3.2.
Let A be a CDGA and recall from Example 2 the ( ∞, 1)-category A-Mod ∞ in-
duced by the (model category) A-Mod ofA-modules. Similarly, the model category
of pointed simplicial sets yields the ( ∞, 1)-category sSet∞∗ of pointed simplicial
sets (Example 1).
Since the inclusion pt•→ X• is always a coﬁbration, the canonical equivalence
CH •
X• (A,M )∼=M⊗ACH •
X• (A) given by Proposition 3 implies that
(8) CH •
X• (A,M ) ∼= M
L
⊗
A
CH •
X• (A) ∼= M
L
⊗
CH •
pt• (A)
CH •
X• (A).
naturally in A-Mod ∞ and CH •
X• (A)-Mod ∞.
Proposition 2, Proposition 3, Proposition 5, Theorem 1 and its proof imply
Theorem 3. The Hochschild chain lifts as a bifunctor of (∞, 1)-categoriesCH(−)(A,−) :
sSet∞∗×A-Mod ∞→A-Mod ∞ which satisﬁes the following axioms
(1) value on a point: there is a natural equivalence CH •
pt•(A,M )∼= M in
A-Mod ∞.
DERIVED HIGHER HOCHSCHILD, TCH, F ACTORIZATION ALGEBRAS 23
(2) action of CH : CH •
X• (A,M ) is naturally a CH •
X• (A)-module, i.e., the
Hochschild chain lifts as an (∞, 1)-functor CH •
X• (A,−) : A-Mod ∞ →
CH •
X• (A)-Mod ∞.
(3) bimonoidal: there is an natural equivalence
CH •
X•
∐ Y• (A,M )∼=CH •
X• (A,M )⊗CH •
Y• (A)
in A-Mod ∞ as well as in CH •
X•
∐ Y• (A)-Mod ∞, for any pointed simplicial
set X• and simplicial set Y•. For M∈A-Mod ∞ and N∈B-Mod ∞, there
is an natural equivalence
CH •
X• (A⊗B,M ⊗N )∼=CH •
X• (A,M )⊗CH •
X• (B,N )
in A⊗B-Mod ∞ and CH •
X• (A⊗B)-Mod ∞.
(4) locality: let f :Z•→ X• and g : Z•→Y• be maps in sSet∞∗. There is
an natural equivalence
CH •
X•
⋃ h
Z•Y•(A,M ⊗L
AN )∼=CH •
X• (A,M )⊗L
CH •
Z• (A)CH •
Y•(A,N )
in A-Mod ∞ and CH •
X•
⋃ h
Z•Y• (A)-Mod ∞. If N = A, then only X• needs
to be pointed and the maps may be in sSet∞.
(5) product: LetX•, Y• be pointed simplicial sets. There is an natural equiv-
alence
CH •
X•×Y•(A,M )
∼
→CH •
X•
(
CH •
Y• (A),CH •
Y• (A,M ))
)
in A-Mod ∞ and CH •
X•×Y• (A)-Mod ∞.
Note that from the point Axiom (1) and the locality Axiom (4) applied to
the canonical maps pt• → pt• and pt• → X• (given by the base point of X•)
follows immediately the equivalence (8) above. This property actually implies that
Axioms (1), (2) and (4) characterizeCH(−)(A,−):
Proposition 6. Let G : A-Mod ∞→ A-Mod ∞ be an (∞, 1)-functor and let M :
sSet∞∗×A-Mod ∞→A-Mod ∞ be any (∞, 1)-bifunctor which satisﬁes the following
axioms
i): value on a point: there is a natural equivalence M(pt•,M )∼= G(M )
naturally in A-Mod ∞.
ii): action of CH :M(X•,M ) is naturally a CHX• (A)-module.
iii): locality: Given maps f :Z•→X• and g :Z•→Y• with X• a pointed
simplicial set, There is a natural equivalence ( in A-Mod ∞)
M(X•∪h
Z•Y•,M )∼=M(X•,M )⊗L
CH •
Z• (A)CH •
Y• (A)
ThenM is naturally equivalent to CH(−)(A,G (−)) as an (∞, 1)-bifunctor.
Note that Axiom ii) is needed to make sense of Axiom iii).
Proof. Let Y• be in sSet∗ and g : pt•→ Y• be the structure map. The locality
axiom for the pushout pt•← pt•
g
→ Y• (where we take X• = pt•) gives natural
equivalences
M(X•,M ) ∼= M(pt•,M )
L
⊗
CH •
pt• (A)
CH •
X• (A) ∼= G(M )
L
⊗
CH •
pt• (A)
CH •
X• (A)
where the last equivalence follows from Axiom i). The result now follows from the
natural equivalences (8). □
24 G. GINOT, T. TRADLER, AND M. ZEINALIAN
One can specialize the locality Axiom (4) in Theorem 3 a bit more by considering
a pointed simplicial set Z• and pointed maps f :Z•→X• andg :Z•→Y•. In that
case, CH •
X• (A,M ) and CHY• (A,N ) inherit natural CH •
Z•(A)-modules structures
(induced by f and g). Then Theorem 3 yields a relative version of the Eilenberg-
Moore spectral sequence.
Corollary 6. Let W•∼= X•∪h
Z• Y• be a homotopy pushout, there is an natural
equivalence
CH •
X•∪h
Z•Y•
(
A,M
L
⊗
A
N
)
∼= CH •
X• (A,M )
L
⊗
CH •
Z• (A)
CH •
Y•(A,N )
in A-Mod ∞ and CH •
X•∪h
Z•Y•(A)-Mod ∞.
In particular there is a natural strongly convergent spectr al sequence of cohomo-
logical type of the form
Ep,q
2 :=Tor
HH •
Z• (A)
p,q
(
HH •
X• (A,M ),HH •
Y•(A,N )
)
=⇒HHp+q
W•
(
A,M
L
⊗
A
N
)
where q is the internal grading. The spectral sequence is furthermore a spectral
sequence of diﬀerential HH •
Z•(A)-modules.
Recall that we are considering a cohomological grading; thus the sp ectral se-
quence lies in the left half-plane with respect to this grading (and p is negative).
Proof. Let ˆM→M be a coﬁbrant replacement of M inA-Mod , ˆX•→X• a ﬁbrant
replacement of X• and ˆf :Z•→ ˆX• be a coﬁbration lifting f . By Theorem 3, we
haveCHW•
(
A,M⊗L
AN
)
∼=CHW•
(
A, ˆM⊗AN
)
(in CHW• (A)-Mod ) and
CH •
X• (A,M )∼=CH •
ˆX• (A, ˆM )∼= ˆM⊗ACH •
ˆX• (A).
Since ˆf :Z•→ ˆX• is a degree wise injection, it suﬃces to prove that
CH •
ˆX• (A) ⊗
CH •
Z• (A)
CHY•(A,N )∼=CH •
ˆX•∪Z•Y•(A,N )
as a CH •
ˆX•∪Z•Y•
(A) ∼= CH •
ˆX•
(A)⊗CH •
Z• (A)CHY• (A)-module which is Proposi-
tion 3. Now the spectral sequence is obtained as in the proof of Cor ollary 3 (using
Theorem 3 instead of Theorem 1). □
Example 6. IfX•,Y• andZ• are contractible, the spectral sequence in Corollary 6
boils down to the usual Eilenberg-Moore spectral sequence
TorH•(A)
p,q
(
H •(M ),H •(N )
)
=⇒Hp+q
(
M⊗L
AN
)
of diﬀerential H •(A)-modules (see [20]).
Remark 8. Besides the Eilenberg Moore spectral sequence 6, there is also an
Atiyah-Hirzebruch kind of spectral sequence for higher Hochsch ild chains: the skele-
tal ﬁltration of a simplicial set X• induces a decreasing ﬁltration ···⊃ Fp···⊃
F −1⊃F 0⊃{ 0} of CH •
X• (A,M ), where Fp := ⨁
n≤−pCH •
Xn (A,M ). This ﬁltra-
tion yields a left half-plane spectral sequence of cohomological typ e with exiting
diﬀerential and further, the cohomology of the associated grade d ⨁
pFp/Fp+1 is
the Hochschild chain complex over X• of the CGA H •(A) with value in H •(M ).
Hence we get from [7]:
DERIVED HIGHER HOCHSCHILD, TCH, F ACTORIZATION ALGEBRAS 25
Proposition 7. There is a strongly convergent spectral sequence of cohomol ogical
type
E2
p,q :=HHp+q
X• (H •(A),H •(M ))q =⇒HHp+q
X• (A,M )
whereq is the internal degree. If M =A, this is a spectral sequence of CDGAs.
For the sake of completeness, we also mention that there is anothe r spectral
sequence to compute higher Hochschild due to Pirashvili which is the G rothendieck
spectral sequence associated to the composition of functors X•↦→kX•↦→kX•⊗L
Γ
L(A) that was deﬁned in Proposition 4. See [30, Theorem 2.4] for details.
4. F actorization algebras and derived Hochschild functor ove r
spaces
The main goal of this section is to prove that Hochschild chains are a s pecial
kind of factorization algebras in the sense of [8] (allowing to compute it using covers
or CW-decomposition).
4.1. The Hochschild (∞, 1)-functor in Top . The Quillen equivalence between
the model categories of simplicial sets and topological spaces induc es an equivalence
Top ∞
S∞
−→sSet∞ of (∞, 1)-categories (Example 1). Here S∞ is the (∞, 1)-functor
lifting the singular set functor X ↦→S•(X) = Map (∆ •,X ). Recall that to any
spaceX we naturally associate the CDGA CH •
X (A) = CH •
S•(X)(A), the Hochschild
chains of A overX. The canonical adjunction map X•→S•(|X•|) yields a natural
quasi-isomorphism CH •
X• (A)→CH •
|X•|(A) of CDGAs by Proposition 4.
From the above equivalence Top ∞
∼
−→ sSet∞ (or alternatively by changing
sSet∞ to Top ∞ in all the proofs in Section 3.2 and 3.3), we deduce the following
topological counterpart to the results of Section 3.2 and Section 3 .3.
Proposition 8. i) The Hochschild chain over spaces functor (X,A )↦→CH •
X (A)
lifts as an (∞, 1)-bifunctor CH :Top ∞×CDGA ∞→CDGA ∞ ﬁtting into
the commutative diagram
sSet ∞ × CDGA ∞
CH /d47/d47 CDGA ∞
T op∞ × CDGA ∞
S∞ ≃
/d79/d79
CH
/d52/d52✐✐✐✐✐✐✐✐✐✐✐✐✐✐✐✐
that satisﬁes all the axioms of Theorem 1 (with Top ∞ instead of sSet∞).
ii) Further, up to natural equivalences of (∞, 1)-bifunctors, it is the only bi-
functor Top ∞×CDGA ∞→CDGA ∞ satisfying the axioms of Theorem 2
(with Top ∞ instead of sSet∞).
iii) Replacing sSet∞ by Top ∞ and sSet∞∗ by Top ∞∗, the analogs of Corol-
lary 3, Proposition 5, Corollary 5, Theorem 3 and Corollary 6 hold.
The fact that Hochschild chains are computed by taking colimits over ﬁnite
simplicial sets has the following translation for topological spaces.
Proposition 9 (Compact support). LetX be (weakly homotopic to) a CW -complex,
A a CDGA and M an A-module. There are natural equivalences
lim−→
K →X
K compact
(
CH •
K(A)
) ≃
−→CH •
X (A) and lim−→
K →X
K compact
(
CH •
K (A,M )
) ≃
−→CH •
X (A,M )
26 G. GINOT, T. TRADLER, AND M. ZEINALIAN
in CDGA ∞ and CH •
X (A)-Mod ∞ respectively.
Proof. Since CH •
X (A,M )∼= M⊗L
ACH •
X (A) in CH •
X (A)-Mod ∞, we only need to
prove that the ﬁrst map is an equivalence.
We ﬁrst assume X to be a CW -complex of ﬁnite dimension n. Let X• be a
simplicial set model of X with no non-degenerate simplices in dimension m > n.
Then, given a ﬁnite simplicial set K•, any map f : K• → X• factors through
a ﬁnite simplicial set ˜K• with no non-degenerate simplices in dimension m > n.
Thus, the realization | ˜K•| is compact. Conversely, if ˜K is a compact subset of the
CW -complex X, it has a simplicial model K• with ﬁnitely many non-degenerate
simplices. Further, any map K→ X has a compact image, since X is Hausdorﬀ,
and thus factors through a compact subset of X. We get a zigzag
lim−→
K →X
K compact
CH •
K(A)
≃
←− lim−→
˜K ⊂X
˜K compact
CH •
˜K (A)
≃
−→ lim−→
˜K•∈ FNDS(X•)
CH •
˜K•
(A)
≃
−→ lim−→
K• → X•
K• ﬁnite
CH •
K• (A)
≃
−→CH •
X• (A)
≃
−→CH •
X (A)
where the ﬁrst and third arrows are equivalences since they are ind uced by coﬁnal
functors. Here FNDS (X•) is the set of simplicial subsets of X• with ﬁnitely many
non-degenerate simplices. That the other arrows in the zigzag are equivalences
follows from Proposition 8 and thus the result is proved for ﬁnite dime nsionalCW -
complexes.
We now reduce the general case to the ﬁnite dimensional one. Let X• be a
simplicial set model of X. The geometric realization |sknX•| of sknX• is a ﬁnite
dimensional CW -complex, and, if K is compact, any map f : K→ X factors as
the composition K→|sknX•|֒→X for some n. Hence the natural map
lim−→
n
(
lim−→
˜K → |sknX•|
˜K compact
CH •
K(A)
)
−→ lim−→
K →X
K compact
CH •
K (A)
is a natural equivalence in CDGA ∞. The result now follows from the ﬁnite dimen-
sional case, the natural equivalence lim−→
n
CH •
sknX• (A)
∼
→CH •
X• (A) (see Remark 6),
and Proposition 8.i). □
Specifying Corollary 5 to the case of topological spaces that are ob tained by
attaching cells, we get the following lemma.
Lemma 1. Let X0 be (weakly homotopic to) a CW -complex and X be (weakly
homotopic to) a CW -complex obtained from X0 by attaching a countable family
(Cn)n∈N of cells. We let Xn be the result of attaching the ﬁrst n cells. For any
CDGA A, one has a natural equivalence
lim−→
n∈N
CH •
Xn (A)
≃
−→CH •
X (A)
in CDGA ∞, as well as lim−→
n∈N
CH •
Xn (A,M )
≃
−→CH •
X (A) in CH •
X (A)-Mod ∞.
DERIVED HIGHER HOCHSCHILD, TCH, F ACTORIZATION ALGEBRAS 27
Proof. SinceCH •
X (A,M )∼=M⊗L
ACH •
X (A) as CH •
X (A)-modules, we only need to
consider the case of CH •
X (A). Further, the cells Ci are homeomorphic to euclidean
balls and the attaching maps have domain given by their boundaries. T hus we
may assume that each Xn is obtained from a simplicial set model ( X0)• of X0
by adding ﬁnitely many non-degenerates simplices. Thus we get a seq uence of
coﬁbrations of simplicial sets ( i.e. degree wise injective maps) (X0)•֒→( X1)•···֒→
(Xn)•···֒→X• = lim−→
n∈N
(Xn)• which are (homotopy) models for the sequence of maps
X0→ X1→···→ X. By deﬁnition of Hochschild chains, there is a canonical
equivalence lim−→
K• →X•
K• ﬁnite
CH •
K• (A)∼= CH •
X• (A) of CDGAs. The maps ( Xn)•→ X•
assemble to give a map of colimits
(9) lim −→
n∈N
(
lim−→
K• → (Xn)•
K• ﬁnite
CH •
K• (A)
)
−→ lim−→
K• →X•
K• ﬁnite
CH •
K• (A).
Given a ﬁnite set Ki and a map fi :Ki→Xi, the image fi(Ki) lies in some ( Xn)i
sinceX• = lim−→
n∈N
(Xn)• andfi(Ki) is ﬁnite. This proves that the family K•→ (Xn)•
of maps from a pointed set into some ( Xn)• is coﬁnal and thus the map (9) is an
equivalence in CDGA ∞. □
Remark 9. It is possible to enhance the result of Lemma 1 in the following way.
One can take any space X∅ and a space X obtained by attaching a family (Ci)i∈I of
other spaces to it. Then, essentially the same argument as the one in Lemma 1 shows
that CH •
X (A) is the colimit lim−→CH •
XF (A) over all possible subspaces XF ⊂ X
obtained by attaching ﬁnitely many Ci’s.
Let us conclude this section by giving an analog of Leray acyclic cover theo-
rem/Mayer Vietoris principle for Hochschild chains.
LetX be a topological space and U = (Ui)i∈I be a good cover forX, i.e. a cover
such that the Ui and all of their nonempty ﬁnite intersections are contractible. We
denote N•(I) the nerve of the cover, that is N0(I) = I, N1(I) is the set of pairs of
indices i0,i 1 such that Ui0∩Ui1⁄=∅ and so on.
Corollary 7. Let X be a topological space and U = (Ui)i∈I be a good cover for
X such that the inclusions Ui∩Uj→Ui are coﬁbrations. Then there is a natural
equivalence
CH •
X (A)
≃
−→A⊗I L
⊗
A⊗N1(I)
A⊗I
inCDGA ∞. Here the left and right module structure are induced by the t wo canon-
ical projections N1(I)→N0(I) = I given by (i,j )↦→i, (i,j )↦→j.
Proof. Since each Ui is contractible, the natural map CH •
Ui(A)→ CH •
pt(A)∼= A
is an equivalence by Theorem 1 and similarly (when Ui∩Uj is not empty) for
the natural map CH •
Ui∩Uj (A)→ A becauseU is a good cover. Since X is the
coequalizer ∐
N1(I)Ui∩Uj ⇒ ∐
IUi→ X, the result follows from the coproduct
axiom (2) and the gluing axiom (3) in Theorem 1 (or Proposition 8). □
28 G. GINOT, T. TRADLER, AND M. ZEINALIAN
4.2. (Pre)F actorization algebras. We now explain a relationship between fac-
torization algebras (as deﬁned by Costello and Gwilliam [8, 9]) and Higher Hochschild
chains.
Let A be a CDGA and X be a topological space. We denote Op(X) the set of
open subsets of X. For every open subset V of X and a family of disjoint open
subsets U1,...,U n⊂V , there is a canonical morphism of CDGAs
µU1,...,Un,V :CH •
U1 (A)⊗···⊗ CH •
Un (A)→
(
CH •
V (A)
) ⊗n
→CH •
V (A)
induced by functoriality by the inclusions Ui֒→V and the multiplication in
CH •
V (A).
These maps are the structure maps of a prefactorization algebra onX in the sense
of [8, 9]. Note that for a (possibly ( ∞, 1)-) symmetric monoidal category ( C,⊗),
we denote by PFac X (C) the ((∞, 1)-) category of prefactorization algebras on
X taking values in C (see [8]). In particular, PFac X (CDGA) is the category
of commutative prefactorization algebras on X as deﬁned in [8]. We will actually
be only interested in the case where C is an ((∞, 1)-)category of algebras over an
(∞)-Hopf operad. We have:
Lemma 2. The rule U ↦→CH •
U (A) together with the maps µU1,...,Un,V deﬁne a
natural structure of a prefactorization algebra on X. Further
(1) The above rule A↦→
( (
CH •
(U)(A)
)
U∈Op(X);
(
µU1,...,Un,V
) )
deﬁnes a functor
CHX :CDGA→PFac X (CDGA).
(2)CHX lifts as an (∞, 1)-functorCHX :CDGA ∞→PFac X (CDGA ∞).
Proof. First we note that CH •
∅ (A)∼=k and that the maps µU1,...,Un,V are CDGAs
morphisms. Further, if V1,...,V l is a collection of pairwise disjoint open subsets of
V ∈Op(X) and U1,...,U n is another family of pairwise disjoint open subsets of V
such that each Ui is contained in some Vj, we can form the diagram
⨂ l
j=1
( ⨂
Ui⊂VjCH •
Ui (A)
) µU1 ,...,Un ,V
/d47/d47
⨂ l
j=1
(
µ(Ui ⊂Vj ),Vj
)
/d15/d15
CH •
V (A)
⨂ l
j=1
(
CH •
Vj (A)
)
µV1 ,...,Vj ,V
/d52/d52❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥
which is commutative by functoriality of Hochschild chains. This prove s that the
ruleU↦→CH •
U (A) is a prefactorization algebra with value in the category CDGA.
The naturality follows from the naturality of Hochschild chains in the a lgebra vari-
able and the lift to the ( ∞, 1)-framework follows from (the proof of) Proposition 8
and Theorem 1. □
In particular, the prefactorization algebra U↦→CH •
U (A) is a commutative pref-
actorization algebra.
Following the terminology of [8, 9], we said that an open cover U ofU∈Op(X) is
factorizing if, for all ﬁnite collections x1,...,x n of distincts points in U , there are
pairwise disjoint open subsets U1,...,U k inU such that {x1,...,x n}⊂ ⋃ k
i=1Ui.
To deﬁne a factorization algebra, we need to introduce the ˇCech complex of a
prefactorization algebra F . Let U be a cover and denote PU the set of ﬁnite
DERIVED HIGHER HOCHSCHILD, TCH, F ACTORIZATION ALGEBRAS 29
pairwise disjoint open subsets {U1,...,U n, Ui ∈ U}. Now the ˇCech complex
ˇC(U,F ) is the chain (bi-)complex
ˇC(U,F ) =
⨁
P U
F (U1)⊗···⊗F (Un)←
⨁
P U ×P U
F (U1∩V1)⊗···⊗F (Un∩Vm)←···
where the horizontal arrows are induced by the alternate sum of t he natural in-
clusions as for the usual ˇCech complex of a cosheaf (see [8]). Let us introduce a
convenient notation for the ˇCech complex: given α1,...,α k∈PU, we denote
F (α1,...,α k) =
⨂
Ui1 ∈α1,...,Uik ∈αk
F (Ui1∩···∩ Uik ),.
The prefactorization algebra structure yields, for all j = 1,...,k , natural maps
F (α1,...,α k)→F (α1,..., ˆαj,··· ,αk). The ˇCech complex of F can be simply
written as
(10) ˇC(U,F ) =
⨁
k>0
⨁
α1,...,αk∈P U
F (α1,...,α k)[k− 1].
The prefactorization algebra structure also induce a canonical ma p ˇC(U,F ) →
F (U ).
A prefactorization algebraF onX (with value in CDGA ork-Mod ) is said to be
a factorization algebra if, for all open subset U∈Op(X) and every factorizing
coverU of U , the canonical map
ˇC(U,F )→F (U )
is a quasi-isomorphism (see [9, 8]). When F is a commutative factorization algebra,
the sequence ⨁
α1,...,αk∈P UF (α1,...,α k)[k− 1] is naturally a simplicial CDGA and
thus the ˇCech complex ˇC(U,F ) has a natural structure of CDGA.
Note that X itself, is always a factorizing cover. A Hausdorﬀ space usually
admits many diﬀerent factorizing covers. This is in particular true fo r manifolds.
Indeed, choosing a Riemannian metric on a manifold X yields a nice factorizing
cover given by the set of geodesically convex neighborhoods of eve ry point in X.
It is shown in [8] that, if U is a basis for the topology of a space X which is
also a factorizing cover , and F is a U-factorization algebra , then one obtains a
factorization algebra iU
∗ (F ) on X deﬁned by
(11) iU
∗ (F )(V ) := ˇC(UV,F )
whereUV is the cover of V consisting of open subsets in U which are also subsets
of V . We recall that a U-factorization algebra is like a factorization algebra,
except that F (U ) is only deﬁned for U ∈U and further that we only require a
quasi-isomorphism ˇC(V,F )
∼
→ F(U ) for factorizing covers V of U consisting of
open sets in U.
A factorizing good cover is a good cover which is also a factorizing cover.
For instance, any CW-complex has a factorizing good cover. Admitt ing a basis
of factorizing good cover is a suﬃcient condition to prove that the H ochschild
prefactorization algebraCHX is a factorization algebra:
Theorem 4. Let X be a topological space with a factorizing good cover and A be
a CDGA. Assume further that there is a basis of open sets in X which is also a
factorizing good cover. The prefactorization algebra CHX :U↦→CH •
U (A) given by
Lemma 2 is a factorization algebra on X.
30 G. GINOT, T. TRADLER, AND M. ZEINALIAN
In particular, for any factorizing cover U of X, there is a canonical equivalence
of CDGAs
CH •
X (A)∼= ˇC(U,CHX ).
For instance the theorem applies to all manifolds (that we always ass ume to be
paracompact) and more generally to CW-complexes.
Proof. LetU be a factorizing good cover. We ﬁrst prove that the rule U↦→CH •
U (A)
is a U-factorization algebra . Since, we already know that U↦→CH •
U (A) is a pref-
actorization algebra (Lemma 2), we only need to prove that, for an y U ∈ U
and any factorizing cover V of U consisting of open sets in U, the canonical
map ˇC(V,CHX )
∼
→ CH •
U (A) is a quasi-isomorphism. Since U is contractible,
CHU
• (A) ∼= A by Theorem 1. Let us denote PV the set of ﬁnite pairwise dis-
joint open subsets {(U1,...,U n, Ui∈V} . Now the ˇCech complex ˇC(V,CHX ) is
the chain (bi-)complex
⨁
P V
CH •
U1 (A)⊗···⊗ CH •
Un (A)←
⨁
P V×P V
CH •
U1∩V1 (A)⊗···⊗ CH •
Un∩Vm (A)←···
where the horizontal arrows are induced by the alternate sum of t he natural inclu-
sions (see [8]). Since U is a good cover, Theorem 1 and the prefactorization algebra
structure ofCHX gives a natural equivalence of chain complexes
(12) ⨁
P V
CH •
U1 (A) ⊗ · · · ⊗ CH •
Un(A)
≃
/d15/d15
⨁
P V×P V
( ⨂ CH •
Ui∩Vj (A)
)
/d111/d111
≃
/d15/d15
· · ·/d111/d111
⨁
P V
A ⊗ · · · ⊗ A ⨁
P V×P V
A ⊗ · · · ⊗ A/d111/d111 · · ·/d111/d111
We can form a simplicial set N•(V) given by the nerve of the cover V. Since V is
factorizing, the canonical map
(13) lim −→
K•
disj
֒→N•(V)
K• ﬁnite
CH •
K• (A) −→ lim−→
K• →N•(V)
K• ﬁnite
CH •
K• (A)∼=CHN•(V)(A)
(where the the left colimit is over maps whose images are required to b e disjoint
open subsets) is an equivalence. The bottom line of diagram (12) now identiﬁes
with the left colimit of the map (13), hence with Hochschild chain comple x of nerve
N•(V). Since U is a good cover, the intersections ( U1
∐ ··· ∐ Un)∩ (V1
∐ ··· ∐ Vm)
are contractible. Thus by the Nerve Theorem (or Leray acyclic cov er), the geomet-
ric realization of N•(V) is quasi-isomorphic to the reunion ⋃
VUi =U . Since U is
assumed to be contractible, we get from above and Proposition 4 a n atural equiv-
alence (of prefactorization algebras) ˇC(V,CHX )(U )
≃
→ CH •
U (A) (∼= A). Thus the
U-prefactorization algebra U↦→CH •
U (A) is a U-factorization algebra. We denote
CHU thisU-factorization algebra.
To conclude, we are left to prove that the induced factorization alg ebraiU
∗ (CHU )
onX is equivalent to CHX as a prefactorization algebra. Let V be an open subset
of X. By [8], there is a natural equivalence iU
∗ (CHU )(V )∼= ˇC(UV,CH U ) (where
UV is the cover of V consisting of open subsets in U which are also subsets of V ).
DERIVED HIGHER HOCHSCHILD, TCH, F ACTORIZATION ALGEBRAS 31
Since the coverUV is a good cover, as in the case where V was inU above, there is
a natural equivalence
⨁
P UV
CH •
U1 (A) ⊗ · · · ⊗ CH •
Un(A)
≃
/d15/d15
⨁
P UV ×P UV
( ⨂ CH •
Ui∩Vj (A)
)
/d111/d111
≃
/d15/d15
· · ·/d111/d111
⨁
P UV
A ⊗ · · · ⊗ A ⨁
P UV ×P UV
A ⊗ · · · ⊗ A/d111/d111 · · ·/d111/d111
where, as for diagram (12) above, the bottom line is equivalent to th e Hochschild
chain complex CH •
N•(UV )(A) of the simplicial set N•(UV ) given by the nerve of
UV . Since U is a good cover, we can again use the Nerve Theorem to see that
CH •
N•(UV )(A)∼=CH •⋃
UV Ui
(A)∼=CH •
V (A) and thus to get the natural equivalence
(of prefactorization algebras) ˇC(V,i U
∗ (CHU ))(U )
≃
→CH •
V (A)∼=CHX (V ). □
IfF is a factorization algebra on X (with value in k-Mod or k-Mod ∞), and
f : X → Y is a continuous map, one can deﬁne the pushforward f∗(F ) by
the formula f∗(F )(V ) = F (f −1(V )) which actually is a factorization algebra on
Y , see [8]. Costello and Gwilliam [8, Section 3.a] have deﬁned the factorization
homology HF (F ) ofF as the pushforward p∗(F ) where p :X→pt is the unique
map. In other words, we have natural equivalences
(14) HF (F ) ∼= p∗(F ) ∼= F (X) ∼= ˇC(U,F )
ink-Mod ∞ (for any factorizing coverU ofX). Note that, despite its name, HF (F )
is a cochain complex (up to equivalences) and, in particular a derived object (which
may be thought as the “derived global sections” of F ). If F has value in CDGA,
then HF (F ) is an object in CDGA ∞ too. Theorem 4 and Lemma 2 yields
Corollary 8. Let X be a CW-complex. The Hochschild prefactorization func-
torCHX is actually a functor CHX : CDGA ∞ → FacX (CDGA ∞). Further,
the factorization homology of CHX (A) is equivalent to CHX
• (A) (as an object of
CDGA ∞); in other words the following diagram commutes:
CDGA ∞
CH •
X (−) /d47/d47
CHX
/d15/d15
CDGA ∞
FacX (CDGA ∞)
HF (−)
/d52/d52❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥
For manifolds, we will give below another geometric interpretation of the functor
CHX in terms of embeddings of manifolds in euclidean spaces (see Example 7 ,
Corollary 9 and Remark 11).
A factorization algebra F on a manifold is said to be locally constant , if, the
natural mapF (U )→F (V ) is a quasi-isomorphism when U⊂V are homeomorphic
to a ball (see [8, 9]). Furthermore, we call F a commutative constant factor-
ization algebra (on X), if there is a CDGA A, and natural quasi-isomorphisms
F (U )→ A for any open U ⊂ X homeomorphic to a ball. Here, natural means,
that for any pairwise disjoint open subsets homeomorphic to a ball U1,...,U n∈V
of a contractible open subset V ∈ X also homeomorphic to a ball, the following
32 G. GINOT, T. TRADLER, AND M. ZEINALIAN
diagram is commutative in k-Mod ∞
(15) F (U1)⊗···⊗F (Un)
/d15/d15
µU1 ,...,Un ,V
/d47/d47F (V )
/d15/d15
A
⊗n
m(n)
/d47/d47A
where m(n) is the (n− 1)-times iterated multiplication of A.
Example 7. A class of examples of locally constant factorization algebras occur s
as follows. By results of Lurie [25] (also see Proposition 10 below), th e data of
a locally constant factorization algebra on Rn is the same as the data of an En-
algebra. Thus any CDGA yields a locally constant factorization algebr a (denoted
A for the moment) on Rn (for any n≥ 1) and also, by restriction, on any open
subset of Rn.
Now, let X be any manifold, and let i :֒→Rn be an embedding of X in Rn.
Let NX be an open tubular neighborhood of X in Rn. We write p : NX → X
for the bundle map. Any factorization algebra F on Rn restricts to a factorization
algebraF|NX on NX and the pushforward p∗(F|NX ) is a factorization algebra
on X. Thus, a CDGA A yields a locally constant factorization algebra p∗(A|NX )
on X for any manifold X. Since p∗(F|NX )(U )∼=F (p−1(U )), it is easy to check
that p∗(A|NX ) is indeed locally constant. Since by construction there is a natural
quasi-isomorphismA(B)
∼
→ A =A(Rn) for any open ball B⊂ Rn, the induced
locally constant factorization algebra p∗(A|NX ) satisﬁes that there exists a natural
equivalenceA|NX (B)
∼
→A for any open set B∈Op(X) homeomorphic to a ball. In
other words, we can think to the factorization algebra p∗(A|NX ) as being constant
(and commutative).
Note that the previous analysis can be extended to any space X which embeds
as the base of locally trivial ﬁbration U→X where U is an open in some Rn and
the ﬁbers are homeomorphic to a ball.
Example 8. Let G be a discrete group acting properly discontinuously on a man-
ifold X. According to [8], any G-equivariant factorization algebra F onX yields a
factorization algebraFG on X/G. Further, it is easy to check that, if F is locally
constant then so isFG too. In particular any CDGA A yields a locally constant fac-
torization algebra on Rn/G for any discrete group acting properly discontinuously
on Rn.
The next corollary describes what constant commutative factorization algebra
are; namely they all are equivalent to derived Hochschild chains for s ome CDGA.
Corollary 9. LetX be a manifold and F a commutative factorization algebra such
that there exists a CDGA A and a natural equivalence F (B)
∼
→A for any open set
B∈Op(X) homeomorphic to a ball. Then F is equivalent to the Hochschild chain
factorization algebraCHX (A) (given by Lemma 2).
In particular, there is a natural equivalence HF (F )∼=CH •
X (A).
Proof. Choosing a Riemannian metric on X, the setBallg(X) of geodesic open balls
is factorizing. Further, F being constant, we have, for any α ={B1,...,B k}∈
DERIVED HIGHER HOCHSCHILD, TCH, F ACTORIZATION ALGEBRAS 33
Ballg(X), natural equivalences
F (α) =F (B1)⊗···⊗F (Bk) ∼=
k⨂
i=1
A∼=CH •
B1 (A)⊗···⊗ CH •
Bk (A)∼=CHX (α)
Similarly, there are natural equivalences
F (α1,...,α j) ∼= CHX (α1,...,α j)
for any α1,...,α j∈PBallg(X). Thus, by Theorem 4, we have
HF (F ) ∼= ˇC(Ballg(X),F )
∼=
⨁
k>0
⨁
α1,...,αk∈P Ball g(X)
F (α1,...,α k)[k− 1]
∼=
⨁
k>0
⨁
α1,...,αk∈P Ball g(X)
CHX (α1,...,α k)[k− 1] ∼= CH •
X (A).
It follows that we have an equivalence ˇC(Ballg(X),F )∼= ˇC(Ballg(X),CHX ). The
same analysis can be made for any open subset U∈Op(X) instead of X and the
naturality of Hochschild chains ensures that the equivalence F (U )∼= CH •
U (A) is
natural in U . □
Remark 10. Note that the above Corollary 9 can be extended to manifolds with
corners, where, by a locally constant factorization algebra on a ma nifold with cor-
ners, we mean a factorization algebra which is locally constant if, whe never re-
stricted to the strata (which are manifolds), it is locally constant se e [8, 2]. One
can extend the deﬁnition of constant factorization algebra in the s ame way.
Let us also sketch how Corollary 9 can be used in the general case of locally con-
stant commutative factorization algebras . Let A be a locally constant factorization
algebra on a manifold M and assume that there is a codimension 1 submanifold
(possibly with corners) N ofM with a trivialization N×I of its neighborhood such
that M is decomposable as M = X∪N ×I Y where X,Y are submanifolds (with
corners) of M glued along N×I. The inclusion i :N×I→X induces a map of
factorization algebras i∗(A|N ×I )→A |X , which gives a structure of A|N ×I -module
toA|X sinceA is commutative.
Lemma 3. IfA|Y is constant (say A|Y (B)∼= A for a CDGA A and any ball
B∈Op(Y )),A is equivalent to A|X
L
⊗
CHN ×I (A)
CHY (A) in FacM (CDGA ∞) (where
the factorization algebras are pushforward to M along the natural inclusions). In
particular,
HF (A) ∼= HF (A|X )
L
⊗
CH •
N ×I (A)
CH •
Y (A).
Using a handle decomposition of M , one can use the lemma above to compute
the homology of a locally constant commutative factorization algebr aA in terms of
(iterated) derived tensor products of derived Hochschild functo rs (see Section 5.2
for a related construction).
Proof. It essentially follows from Corollary 9 and Lemma 5. Indeed, since A|Y is
constant of type A, it is isomorphic to CHY (A) and similarly,A|N ×I∼=CHN ×I (A)
34 G. GINOT, T. TRADLER, AND M. ZEINALIAN
(by Corollary 9). Further, there is a quasi-isomorphism of prefact orization algebras:
(16) A|X
L
⊗
CHN ×I (A)
CHY (A) ∼= A|X⊗
⨁
ℓ≥0
A|N ×I [ℓ]⊗A |Y
where the middle term is the bar construction on A|N ×I . Applying the same con-
struction to the ˇCech complex of a factorizing cover yields thatA|X⊗L
CHN ×I (A)CHY (A)
is indeed a factorization algebra.
By the identity eq16 above, for any open U in X or open V inY , we have,
A|X
L
⊗
CHN ×I (A)
CHY (A)
(
U
)
∼= A|X
(
U
)
, A|Y
L
⊗
CHN ×I (A)
CHY (A)
(
V
)
∼= A|Y
(
V
)
Similarly, using that the two-sided bar construction of CH •
W (A) is naturally iso-
morphic toCH •
W (A) for any open W inN×I, we get that the restriction (to N×I)(
A|X⊗L
CHN ×I (A)CHY (A)
)
|N ×I is isomorphic toCHN ×I(A). Thus the factorization
algebraA|X⊗L
CHN ×I (A)CHY (A) is equivalent to the one obtained by gluing together
AX andAY along their intersection AN ×I , that is A. □
Remark 11. Corollary 9 implies that the factorization algebras p∗(A|NX ) are
independent (up to equivalences inFacX (k-Mod ∞)) of the choices of the embedding
and of the tubular neighborhood made in Example 7. Indeed, if i1 :֒→Rn1 and
i2 :֒→Rn2 are two embeddings of a manifold X in an euclidean space, and
given two choices Rn1⊃ N1X
p1
→ X,Rn2⊃ N2X
p2
→ X of tubular neighborhoods,
Corollary 9 implies that there are natural equivalences
p1∗(A|N1X )(U )
≃
−→CHU
• (A)
≃
←−p2∗(A|N2X )(U )
for open subsets U⊂X.
Example 9. LetM be a manifold and A =C∞(M ) its algebra of functions. Also
let Σ g be a compact Riemann surface of genus g andF the factorization algebra
(see Theorem 4) on Σ g deﬁned by the rule U↦→C•
U (C∞(M )) (here, in the deﬁnition
of Hochschild chains, the tensor product over k is the completed tensor product so
thatC∞(M )⊗C∞(M )∼=C∞(M×M )). Let Ω n(M ) denote the de Rham n-forms
on M , viewed as complex concentrated in degree 0.
An analogue of Hochschild-Kostant-Rosenberg theorem for Hoch schild chains
over surfaces [13, Theorem 4.3.3] implies that the factorization hom ology of F on
Σg is given by
HF (F )∼=SC ∞(M)
(
Ω 1(M )[2]
)
⊗
C ∞(M)
SC ∞(M)
(
Ω 1(M )
)
⊗
C ∞(M)
i=1...2g⨂
C ∞(M)
Ω •(M )[•]
where V [n] is the graded space ( V [n])i = Vi+n (i.e. with cohomological degree
shifted down by n) and SC ∞(M)(W ) is the symmetric graded algebra of a graded
C∞(M )-moduleW . In terms of graded-geometry the above isomorphism is equiva-
lent to saying that HF (F ) is (equivalent to) the algebra of functions of the graded
manifold
HF (F ) ∼= T [2](M )⊕
2g⨁
i=1
T [1]M.
DERIVED HIGHER HOCHSCHILD, TCH, F ACTORIZATION ALGEBRAS 35
We now study a homotopical strengthening of the locally constant c ondition.
We said that a factorization algebra on X is strongly locally constant if the
natural mapF (U )→F (V ) is a quasi-isomorphism when U⊂V are contractibles.
LetA be a CDGA; we say that a factorization algebra F is strongly constant of
typeA, if there exists a natural quasi-isomorphism F (U )→A for any contractible
U . Here, natural means, that for any pairwise disjoint contractible open subsets
U1,...,U n∈V of a contractible open subset V ∈X, the following diagram (similar
to diagram 15) is commutative in k-Mod ∞
F (U1)⊗···⊗F (Un)
/d15/d15
µU1 ,...,Un ,V
/d47/d47F (V )
/d15/d15
A
⊗n
m(n)
/d47/d47A
Example 10. The factorization algebras given by Theorem 4 are strongly consta nt
of type A.
Example 11. LetX be a manifold, A a CDGA and p∗(A|NX ) be the factorization
algebra on X constructed in Example 7. Corollary 9 and the homotopy invariance
of Hochschild chains implies that p∗(A|NX ) is a strongly constant factorization
algebra.
Now let X be a topological space that embeds as a retract i : X
֒→
←UX : r,
whereUX is an open subset of some Rn (wheren can be inﬁnite). Then, similarly
to the manifold case, the CDGA A yields a factorization algebra A on Rn and
a factorization algebra r∗(A|UX ) on X. The above paragraph implies that A is
strongly constant. Further if the ﬁbers of r are contractible, then r∗(A|UX ) is
strongly constant of type A.
We have the following analogue of Corollary 9 for strongly constant f actorization
algebras on a topological space that admits a factorizing good cove r (for instance
those given by Example 11 when X is a CW-complex)
Corollary 10. LetX be a topological space with a factorizing good cover and A be
a CDGA. Let F be a factorization algebra on X.
(1) AssumeF is strongly constant of type A, then one has a natural equivalence
HF (F )∼=CH •
X (A) in k-Mod ∞.
(2) Assume that there is a basis B of open sets which is a factorizing good
cover and that F is a factorization algebra which satisﬁes the strongly con-
stant condition (of type A) with respect to opens in B, i.e., there exists a
natural quasi-isomorphism F (U )→ A for U∈B (which is automatically
contractible). Then, there is a natural equivalence of fact orization algebras
F∼=CHX (A) betweenF and the Hochschild prefactorization algebra given
by Lemma 2 (in particular, F is strongly constant of type A).
Proof. The ﬁrst assertion is proved as in Corollary 9 using a factorizing good cover
U for X instead ofBallg(X) (and using a proof similar to the proof of Theorem 4
to get that ⨁
k>0
⨁
α1,...,αk∈P UCHX (α1,...,α k)[k− 1] ∼= CH •
X (A)).
Since any factorization algebra is uniquely deﬁned by its restriction t o a fac-
torizing basis, the second assertion follows easily from the ﬁrst one applied to all
V ∈B . □
36 G. GINOT, T. TRADLER, AND M. ZEINALIAN
As a further corollary to Theorem 4, we can extend the Hochschild c onstruction
as a pullback and pushforward of factorization algebras in a particu lar setting. The
pushforward construction of factorization algebras was describ ed above Corollary
8. Following [8], there is also a pullback construction for factorization algebras
given for an open immersion f :N→M . For a factorization algebra F on M , let
f ∗F be the factorization algebra on N given by f ∗F (U ) = F (f (U )) for all open
subsets U⊂N such that f|U :U→f (U ) is a homeomorphism, extended to a full
factorization algebra.
Now, assume that X,Y,Z are topological spaces, and that there is an open
immersion of X×֒→Z ofX×Y intoZ. For a factorization algebra F onZ, we
deﬁne the Hochschild factorization algebra with respect to X to be the factorization
algebra CHX (F ) ofF on Y given by
CHX (F ) := (prY )∗◦f ∗(F ), where Y
prY
←−X×Y
f
−→Z.
Here prY : X×Y →Y denotes the projection to Y . This construction induces a
functor, called CHX : FacZ (CDGA ∞)→ FacY (CDGA ∞),F↦→ (prY )∗◦f ∗(F )
which satisﬁes the following naturality condition.
Corollary 11. Assume that X, Y and Z all admit a basis of open sets which is a
factorizing good cover. Under the functors CHY :CDGA ∞→FacY (CDGA ∞) and
CHZ :CDGA ∞→FacZ(CDGA ∞) from Corollary 8, the functor CHX represents
the functor CH •
X on CDGA ∞, i.e., the following diagram commutes:
CDGA ∞
CH •
X /d47/d47
CHZ
/d15/d15
CDGA ∞
CHY
/d15/d15
FacZ(CDGA ∞)
CHX /d47/d47FacY (CDGA ∞)
Proof. Let A∈ CDGA ∞ andW be a basis and factorizing good cover by open
subsets U×V ⊂ X×Y such that U,V are contractible and f|U×V : U×V →
f (U×V ) is a homeomorphism. In particular, for U×V ∈W , we have natural
equivalences
f ∗(CHZ (A))(U×V )∼=CHZ(A)(f (U×V ))∼=CH •
f (U×V )(A)∼=A
since f (U×V ) is contractible. Hence Corollary 10 implies that f ∗(CHZ(A)) is
strongly constant of type A and further that, for any contractible open U⊂Y ,
CHX (CHZ(A))(U ) ∼= f ∗(CHZ(A))(X×U ) ∼= CH •
X×U (A) ∼= CH •
X (A).
ThusCHX (CHZ(A)) is a strongly constant factorization algebra on Y of type
CH •
X (A), hence, by Corollary 10.(2), is naturally equivalent to CHY (CH •
X (A)). □
As an application of the above Corollary 11, we look at the particular c ase where
X×Dn−k֒→Rn is an open immersion. In this case, CHX maps factorization
algebras in Rn to factorization algebras inDn−k, and thus via the inclusion Dn−k֒→
Rn−k also to factorization algebras in Rn−k,
CHX :Fac Rn (CDGA ∞)→Fac Rn−k (CDGA ∞).
DERIVED HIGHER HOCHSCHILD, TCH, F ACTORIZATION ALGEBRAS 37
