---
doc_id: arxiv-0811.2435v1
doc_title: "Stability structures, motivic"
section_id: sec-019-topology-on-the-space-of-stability-structures
section_title: "Topology on the space of stability structures"
section_number: null
pages: 56-60
source_pdf: 0811.2435v1.pdf
source_sha256: 615b04eca83bcade
doc_brief: "Stability structures, motivic — 43 sections: Introduction; Counting problems for 3-dimensiona; Non-commutative varieties with pol"
---
LetC be an ind-constructible weakly unital A∞-category over a ﬁeld k of
arbitrary characteristic. Let cl : Ob(C) → Γ ≃ Zn be a map of ind-
constructible sets (where Γ is considered as a countable set of points) such
that the induced map Ob(C)(
k)→ Γ factorizes through a group homomor-
phism cl k : K0(C(k))→ Γ. It is easy to see that for any ﬁeld extension
56
k′⊃ k we obtain a homomorphism cl k
′ :K0(C(k
′
))→ Γ.
In the case when C is a Calabi-Yau category we require that Γ is endowed
with an integer-valued bilinear form ⟨•,•⟩and the homomorphism cl k is
compatible with⟨•,•⟩and the Euler form on K0(C(k)).
For ind-constructible triangulated A∞-categories the notion of stability
structure admits the following version.
Deﬁnition 9 A constructible stability structure on (C, cl) is given by the
following data (cf. Introduction, Section 1.2):
• an ind-constructible subset
Css⊂Ob(C)
consisting of objects called semistable, and satisfying th e condition that
with each object it contains all isomorphic objects,
• an additive map Z : Γ → C called central charge, such that Z(E) :=
Z(cl(E))⁄= 0 if E∈C ss,
• a choice of the branch of logarithm LogZ(E)∈ C for any E ∈C ss
which is constructible as a function of E.
These data are required to satisfy the corresponding axioms from Section
1.2 for the category C(
k).
In particular
• the set of E∈C ss(k)⊂ Ob(C)(k) with the ﬁxed cl(E)∈ Γ \{ 0} and
ﬁxed LogZ(E) is a constructible set.
Before we proceed with the topology let us make a comparison w ith the
“Lie-algebraic” story of Section 2. First, we observe that t he set Css can
be thought of as an analog of the collection of elements ( a(γ))γ∈Γ\{0} from
Section 2.1. Then we give the following deﬁnition of another data and axioms
which is equivalent to the one given above and can be thought o f as an analog
of the collection of the group elements AV .
Deﬁnition 10 A constructible stability structure on (C, cl) is given by the
following data:
• an additive map Z : Γ → C,
57
• for any bounded connected setI⊂ R an ind-constructible subsetP(I)⊂
Ob(C)(k) which contains which every object all isomorphic objects.
These data are required to satisfy the following axioms 12:
• the zero object of the category C(k) belongs to all P(I),
• ∪n∈Z>0P([−n,n ]) = Ob(C)(k),
• if I1 < I2 in the sense that every element of I1 is strictly less than
any element of I2 then for any E1∈P (I1) and E2∈P (I2) one has
Ext≤0(E2,E 1) = 0 ,
• P(I + 1) =P(I)[1] where [1] is the shift functor in C(k),
• (Extension Property) If I =I1⊔I2 and I1<I 2 in the above sense then
the ind-constructible setP(I) is isomorphic to the ind-constructible sub-
set of such objects E∈Ob(C)(k) which are extensions E2→E→ E1
with Em∈P (Im),m = 1, 2,
• ifI is an interval of the length strictly less than one, E∈P (I),E⁄= 0,
then Z(cl(E)) belongs to the strict sector
VI ={z =reπiϕ∈ C∗|r> 0,ϕ∈I} ,
• there is a non-degenerate quadratic form Q on Γ R such thatQ| KerZ < 0,
and for any interval I of the length strictly less than 1 the set
{cl(E)∈ Γ|E∈P (I)}⊂ Γ
belongs to the convex cone C(VI,Z,Q ) deﬁned in Section 2.2,
• let I be an interval of the length strictly less than 1, and γ∈ Γ . Then
the set{E∈P (I)| cl(E) = γ} is constructible.
The equivalence of Deﬁnitions 9,10 can be proved similarly t o the proof
of Theorem 2.
With this equivalent description of a constructible stabil ity condition we
observe that the collection of sets P(I) considered for all intervals I with
12One should read expressions Ob(C),P(I) etc. in this list of axioms as sets of k-points.
58
the length less than 1 are analogous to the collection of elem ents AV where
V = VI (see Section 2.2) and the Extension Property is analogous to the
Factorization Property.
One has the following result.
Proposition 8 For any constructible stability structure on C and any ﬁeld
extension k⊂ k′ the categoryC(k′) carries a locally ﬁnite stability structure
in the sense of [9] with the central charge given by Z◦ clk′ and the collection
of additive subcategories P(I)(k′), where I runs through the set of bounded
connected subsets of R as above.
Proof. The proof is straightforward. Local ﬁniteness in the sense o f [9]
follows from our (stronger) assumption on the quadratic for m Q. ■
Let us denote by Stab(C, cl) the set of constructible stability structures on
C with a ﬁxed class map cl. Our goal is to introduce a topology on Stab(C, cl).
Let ∆ ⊂ C be a triangle with one vertex at the origin. We choose a branch
of the function z↦→Logz forz∈ ∆. We denote the corresponding argument
function by Arg(z). We denote by C∆ ,Log an A∞-subcategory ofC generated
by the zero object 0, semistable objects E withZ(E)∈ ∆ , Arg(E)∈ Arg(∆)
as well as extensions J of such objects satisfying the condition Z(J)∈ ∆.
We allow the case ∆ = V where V is a sector, in which case we will use
the notationCV,Log. It is easy to see that C∆ ,Log is an ind-constructible cat-
egory. Notice that in the language of ind-constructible set sP(I) we have
Ob(CVI,Log) = P(I) for some choice of the branch Log. The condition of
genericity of the sector VI corresponding to a closed interval I = [a,b ] of
the length less than 1 corresponds to the following generici ty condition of
the set P(I): both P({a}) and P({b}) are zero categories (equivalently
P([a,b ]) =P((a,b ))).
Let us ﬁx a non-degenerate quadratic form Q on Γ R such thatQ| KerZ < 0
andQ(cl(E))> 0 for any E∈C ss. We introduce the topology on Stab(C, cl)
in the following way. Let us consider a family σx = (Zx,Css
x ,... ),x ∈ X of
stability structures in a neighborhood of x0∈ X. Then for every point x,
a generic closed interval I = [a,b ] of the length less than 1 we have the full
categoryP(I)x⊂Ob(C). For a given γ∈ Γ \{ 0} we denote by P(I)x,γ the
constructible subset of objects E∈P (I)x such that cl(E) = γ.
We say that a family σx = (Zx,Css
x ,... ),x ∈ X of stability structures
parametrized by a topological space X is continuous at a given stability struc-
tureσx0 = (Z0,Css
0 ,... ) if:
59
a) The map x→Zx is continuous at x =x0.
b) There exists a neighborhood U ofx0 such that for any E∈C ss
x ,x∈U
we have Q(cl(E)) /greaterorequalslant0.
c) For any generic closed interval I of the length strictly less than 1 the
constructible setP(I)x,γ is locally constant near x0 (cf. Deﬁnition 3c)).
In this way we obtain a Hausdorﬀ topology on Stab(C, cl). We can deﬁne
a parallel transport along a path σt in the space Stab(C, cl) similarly to the
case of stability structures in graded Lie algebras discuss ed in Section 2. Each
time when we cross the wall of ﬁrst kind we use the above proper ty c) in order
to “recalculate” the set of semistable objects. In order to d o this we use the
following property: E ∈ Ob(C∆ ,Log) is semistable iﬀ there is no extension
E2→ E→ E1 where Ei,i = 1, 2 are non-zero objects of C∆ ,Log such that
Arg(E2) > Arg(E1). These considerations also ensure that the Theorem 1
from Introduction holds (i.e. the natural projection of the space of stability
conditions to the space of central charges is a local homeomo rphism).
4 Motivic functions and motivic Milnor ﬁber
