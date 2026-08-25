---
doc_id: malkin-2021-galois-action-on-motivic-fundamental-groups-thes
doc_title: "On the Galois action on motivic fundamental groups of punctured elliptic and rational curves"
section_id: sec-023-symmetric-correlators-modulo-depth
section_title: "Symmetric correlators modulo depth"
section_number: null
pages: 93-101
source_pdf: malkin-2021-galois-action-on-motivic-fundamental-groups-thesis.pdf
source_sha256: 3bc30dc6a4a03a7f
doc_brief: "On the Galois action on motivic fundamental groups of punctured elliptic and rational curves — On the Galois Action on Motivic Fundamental Groups of Punctured Elliptic and Rational Curves Nikolay"
---
In this section,
1(-) always refers to
1(-; C).
Change of base point formula
Fix?∈(. Let us deﬁne a mapd? :)(
1(-))→ )(
1(-)⊕ Q[(]) as follows.
For a wordl1⊗···⊗ l=∈)(
1(-)),
d?(l1⊗···⊗ l=)=
Õ
:
(−1):
Õ
81<82,···<8:<=
89+1>89+1
l1⊗···⊗(
⟨
l89,l89+1
⟩
(?))⊗···⊗ l=,
where⟨,⟩ is the skew-symmetric pairing:⟨l,l⟩ =−⟨l,l⟩ = 1. That is, it is the sum over all possible
85
replacements of pairs(l⊗l) and(l⊗l) by the puncture?, taken with appropriate sign. For example, we
have:
d?(1)= 1,
d?(l)=l,
d?(l⊗l)=l⊗l,
d?(l⊗l)=(l⊗l)−( ?),
d?(l⊗l⊗l)=(l⊗l⊗l)−( ?⊗l)+( l⊗?),
d?(l⊗l⊗l⊗l)=(l⊗l⊗l⊗l)−( ?⊗l⊗l)−( l⊗l⊗?)+( l⊗?⊗l)+( ?⊗?).
For0∈(,deﬁned?(0)=(0)−( ?),extendedbylinearityto Q[(]. Then,extend d? to)(
1(-)⊕ Q[(]):
ifG0,...,G :∈ Q[(], andΩ0,..., Ω:∈)(
1(-)), then
d?(Ω0⊗G0⊗···⊗ Ω:⊗G:)=d?(Ω0)⊗ d?(G0)⊗···⊗ d?(Ω:)⊗ d?(G:).
Lemma3.3 (Changeofbasepointformula) . Supposethat ?≠@. ThenthefollowingrelationholdsforHodge
correlators in weight> 2:
Cor?(G)= Cor@
(d?(G)). (3.11)
On the right side stands a sum of correlators obtained from the one on the left by taking all possible
replacements of punctures and pairs of adjacent cohomology classes with(?), taken with the appropriate
sign.
Before proceeding to the proof, let us illustrate the formula on some examples. In weight4,
Cor?(0,1,2)= Cor@(0,1,2)− Cor@(?,1,2)− Cor@(0,?,2 )− Cor@(0,1,? ),
Cor?(0,1,l, l)= Cor@(0,1,l, l)
−Cor@(?,1,l, l)− Cor@(0,?,l, l)− Cor@(0,1,? )+ Cor@(?,?,l, l),
Cor?(0,l, l,l, l)= Cor@(0,l, l,l, l)
−Cor@(?,l, l,l, l)− Cor@(0,?,l, l)+ Cor@(0,l,?, l)− Cor@(0,l, l,?)
+Cor@(?,?,l, l)− Cor@(?,l,?, l)+ Cor@(?,l, l,?).
86
If the left side of the expression only contains punctures, we recover a formula identical to the one found by
[GR], Theorem 2.6, for Hodge correlators on the puncturedP1. More generally, for symmetric correlators,
we have:
Corollary 3.4.Suppose that?≠@. Then we have the relation in weight> 2:
Cor?((<0,<′
0⊗G0⊗(<1,<′
1⊗G1⊗···⊗ (<=,<′=⊗G=)
= Cor@((<0,<′
0⊗(( G0)−( ?))⊗···⊗ (<=,<′=((G=)−( ?)))
=
Õ
:
(−1):
Õ
81<···<8:
Cor@((<0,<′
0⊗G0⊗···⊗ ?⊗···⊗ ?⊗···⊗ (<=,<′=⊗G=),
where on the right the puncturesG81,...,G 8: are replaced with@.
Proof. For all<,<′≥ 0,d?((<,<′)=(<,<′. □
Proof of Lemma 3.3.We ﬁrst prove the change of base point formula in the real Hodge realization, i.e, that it
holds on the level of the Hodge correlator functions CorH.
The Green’s functions associated to the points? and@ are related by

?(G,H)=
@(G,H)− 
@(G,?)− 
@(H,?)+ ,
where  is a constant that depends on the choices of tangent vectors at? and @. Now consider any tree
contributing to the Hodge correlator ofΩ0⊗( G0)⊗···⊗ Ω:⊗G:. Write the Green’s function
?(G,H)
assignedtoeachedgeintermsofthe 
@,andexaminethecontributionofthethreetermsin 
?(G,H)−
@(G,H):

@(G,?),
@(H,?), and for a given edge. There are three cases:
(1) An external edge decorated by a puncture0, assigned the function
?(G,0). Assigning the form
−
@(G,?) to gives the correlator where0 has been replaced by−(?). The terms and
@(0,?) are
constants. Because the Hodge correlator has weight> 2, there is at least one internal edge in the tree, so
the correlator where a constant has been placed on is the integral of an exact form3C(... ).
(2) An internal edge that splits the tree into two parts, one of which is decorated by two 1-forms. Suppose
that in
?(G,H), the vertex assigned the variableG is adjacent to external vertices labeledl1 andl2.
Then the terms
@(G,?) and are independent ofH, and the integral splits into a product; the integrand
for the subtree growing fromH is an exact form, so we get 0. For the term−
@(H,?), the integral also
splits into a product of
∫
l1∧l2 and the correlator withG replaced by an external vertex−(?).
87
(3) An internal edge that splits the tree into two parts, each of which is decorated by at least one puncture.
Then, as in the previous case, each term in the expression for
?(G,H) is independent of eitherG or H.
The integral splits into a product of two factors, one of which is 0.
We conclude that the change of base point is computed by adding all possible replacements of external
punctures0 by−(?) and pairsl1⊗l2 by−⟨l1,l 2⟩(?). This implies the lemma.
(Note that the assumption of weight> 2 was crucial to all arguments involving integration of the exact
form.)
One easily checks by induction that the coproducts of the two sides of (3.11) are equal. This implies the
result on the level of the Hodge correlators CorHod. □
Independence of base point
In this part, we prove the following important result.
Theorem 3.5.The symmetric Hodge correlators in weight> 2are independent of the base point modulo the
depth ﬁltration.
Formally, letG∈ )(
1(-)⊕ Q[(]). Then there exists~G, equal toG modulo lower-depth terms, such
thatCor?(~G) is independent of?.
In terms of generating functions, this theorem implies:
Corollary 3.6.The generating functionsΘ∗ satisfy the dihedral symmetry relations of Lemma 3.1:
Θ∗
B
(F0,...,F =|C0 :··· :C=
)
=Θ∗
B
(F1,...,F =,F 0|C1 :··· :C= :C0
)
=(−1)=+1Θ∗
B
(F=,...,F 1,F 0|C= :··· :C1 :C0
)
modulo lower-depth terms that are independent ofB.
Proof. By the cyclic symmetry and dihedral relations on correlators, these expressions are equal up to an
additive shift in the correlators’ arguments, equivalently, a change in base point. □
Notice that all terms on the right side of (3.11) havehigher or equal depth to the left side. It will be
necessary to ﬁnd correction terms of lower depth to obtain a formula of the form
Cor?(ℎ0⊗G0⊗···⊗ ℎ:⊗G:)+ Cor?(lower depth)= Cor@(ℎ0⊗G0⊗···⊗ ℎ:⊗G:)+ Cor@(l.d.)
88
when eachℎ8 a symmetric expression(<,<′.
The proof of the theorem relies on a key construction. We will ﬁnd elements:
(<0,<′
0∗(<1,<′
1∗···∗ (<=,<′=∈)(
1(-))
such that
d?((<0,<′
0∗(<1,<′
1∗···∗ (<=,<′=)= (3.12)
=
Õ
:
Õ
81<···<8:
(
(<0,<′
0∗···∗ (<81−1,<′
81−1
)
⊗( ?)⊗
(
(<81,<′
81
∗···∗ (<82−1,<′
82−1
)
⊗( ?)⊗ ....
Before showing how to construct these elements, let us prove the theorem, assuming these elements exist.
Proof of Theorem 3.5.Consider an element
G=(<0,<′
0⊗G0⊗(<1,<′
1⊗G1⊗···⊗ (<=,<′=⊗G=.
Let
 be a proper subset of{0,...,= }. Write
 as the union of its cyclically contiguous subsets, each of the
form{8,8+ 1,...,8 +:} (indices modulo=+ 1). LetG/
 be the element formed by replacing each
(<8,<′
8⊗G8⊗···⊗ G8+:⊗(<8+:,<′
8+:
by(<8,<′
8∗···∗ (<8+:,<′
8+:.
Now consider the corrected element:
~G=
Õ

(−1)|
|G/
.
It is equal toG modulo the depth ﬁltration. Also, let
H@ =(<0,<′
0⊗@⊗(<1,<′
1⊗@⊗···⊗ (<=,<′=⊗@,
and deﬁne~H@ in the same way. By a standard inclusion-exclusion argument, the property (3.12) implies that
d?(~G+ ~H@)= ~G+(terms containing@).
89
Because the correlator with base point@ is zero for the terms containing@, this gives
Cor?(~G+ ~H@)= Cor@(~G).
On the other hand, the Hodge correlator Cor?(~H@) depends only on?−@, and thus?7→ Cor?(~G)− Cor0(~G)
provides a group homomorphism→ R, and must be 0. Therefore, Cor?(~G) is independent of?. □
Lemma 3.7. There exist elements, independent of choice of symplectic basis of
1(-), satisfying (3.12).
Proof. We produce such elements explicitly:
(<0,<′
0∗···∗ (<:,<′
: = 1
2:
Õ
=0,=′
0,...,=:,=′
:
±(=0,=′
0⊗(=1,=′
1⊗···⊗ (=:,=′
:,
where the sum is taken over the=8,=′
8≥ 0 such that:
=8+=′
8 =
 

<8+<′
8+ 1 8= 0,:
<8+<′
8+ 2 0 <8 < :
,
(=0−=′
0)+···+( =:−=′
:)=(<0−<′
0)+···+( <:−<′
:).
A term is taken with the sign− if there is an odd number of8 (8= 0,...,: − 1) such that
(=0−=′
0)+···+( =8−=′
8) <(<0−<′
0)+···+( <8−<′
8),
otherwise with the sign+.
Examples:
(0,0∗(0,0= 1
2(ll−ll),
(0,0∗(1,0= 1
2(lll+lll−lll),
(0,0∗(0,0∗(0,0= 1
4(llll+llll−llll−llll+llll+llll).
Weexplaintheconstructionbypicture. Thebasiselementsof )(
1(-)) ofagivenweightareinbijection
with lattice paths: a wordl1⊗···⊗ l= corresponds to the path whose8-th step is(1, 0) if l8 = l and
(0, 1) ifl8 =l. The elements of)(
1(-)⊕ Q[?]) are lattice paths that also allow the diagonal step(1, 1),
corresponding to(?). (The points of the lattice path are simply the Hodge bidegrees of the initial subwords.)
90
−
+
(<0,<′
0⊗( ?)⊗ (<1,<′
1 (<0,<′
0∗(<1,<′
1
Figure 3.3. Construction of the element(<0,<′
0∗(<1,<′
1: the paths crossing the rays marked− and+are
taken with the corresponding sign.
−
+
Figure 3.4. The point of nonconcavity contributing a term to the right side of (3.12).
The mapd? replaces a path by the sum of all paths obtained by replacing steps (up, right) or (right, up) with
diagonal steps, in the latter case changing the sign.
To construct the element, we ﬁrst consider the concatenation of paths in(<0,<′
0, ..., (<:,<′
:, with a
step(1, 1) inserted between successive pairs. Draw a diagonal lineℓ8 bisecting the step that was inserted
between(<8−1,<′
8−1 and (<8,<′
8. Any path of the Hodge bidegree(˝<8+:, ˝<′
8+:) appears in a unique
term(=0,=′
0⊗···⊗ (=:,=′
:,andeach (=8,=′
8 isthesumofpathsbetweenthelines ℓ8 andℓ8+1. Thesignofapath
is a product of factors determined by the rays on which it crosses the diagonal lines:+1if below the step,−1
if above. (See Figure 3.3.)
Nowﬁxachoiceofarayofeachsuchdiagonal,andconsiderthetermscomingfromlatticepathscrossing
theserays. Weclaimthatanysuchtermsatisﬁes(3.12)modiﬁedbyafactorof 1
2:. Indeed,thesearethelattice
paths lying in a certain rectilinear region (right part of the ﬁgure). Most terms ind? are canceled; the only
terms remaining are those with segments(1, 1) at the points of nonconcavity of this region. This is precisely
the expression on the right of (3.12). (See Figure 3.4.) □
91
The simplest example of the corrected correlator, for(0)⊗( 1)⊗( 2):
(0)⊗( 1)⊗( 2)− 1
2(l⊗l−l⊗l)⊗( 1)⊗( 2)
− 1
2(0)⊗ (l⊗l−l⊗l)⊗( 2)
− 1
2(0)⊗( 1)⊗ (l⊗l−l⊗l).
(The terms where two points were replaced are 0, because of the reﬂection relations.)
3.2.3 Second shuﬄe relations
The depth 2 case: Dihedral symmetry
Theorem 3.8. The corrected symmetric Hodge correlators in depth 2 satisfy the second shuﬄe (dihedral
symmetry) relations modulo terms of lower depth that are independent of the base point.
The corrected element for
(<0,<′
0⊗( 0)⊗ (<1,<′
1⊗( G1)⊗ (<2,<′
2⊗( G1+G2)
+(<0,<′
0⊗( 0)⊗ (<2,<′
2⊗( G2)⊗ (<1,<′
1⊗( G1+G2) (3.13)
lies in the kernel of the mapCorB for everyB.
Proof. The corrected element for (3.13 changes sign under the mapG7→( G1+G2−G) and reﬂection. On the
other hand, it is invariant under this operation up to an additive shift (i.e., change in base point). □
Relations in higher depth
The second shuﬄe relationsare relations of the form
Õ
f∈Σ8,9
Θ∗(G0,Gf−1(8),Gf−1(2),...,G f−1(8+9))| C0,Cf−1(1),Cf−1(2),...,C f−1(8+9)
)+...,
perhapswithadditionaltermsoflowerdepth. TheHodgecorrelatorson P1 areknowntoobeysuchrelations,
in addition to the ﬁrst shuﬄe relations, the structural relations inCL∨
-,(,E 0; the lower-depth terms were
described precisely in Chapter 2.
TherelationofTheorem3.8isaspecialcaseofasecondshuﬄerelation. Indepth > 2,thesecondshuﬄe
relations are not equivalent to dihedral symmetry. However, one hopes for a generalization.
92
Conjecture3.9. ThesecondshuﬄerelationsforsymmetricellipticHodgecorrelatorsholdmodulothedepth
ﬁltration. The lower-depth terms are independent of the base pointB.
The lower-depth correction terms in depth> 2 are not known. In particular, the corrected correlators
do not satisfy the second shuﬄe relations in higher depth. However, calculations in low weight support this
conjecture. We may expect the elliptic relations to be deformations of the relations forP1 (see §3.4.2).
