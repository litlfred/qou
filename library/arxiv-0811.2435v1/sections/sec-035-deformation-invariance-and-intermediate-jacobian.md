---
doc_id: arxiv-0811.2435v1
doc_title: "Stability structures, motivic"
section_id: sec-035-deformation-invariance-and-intermediate-jacobian
section_title: "Deformation invariance and intermediate Jacobian"
section_number: null
pages: 112-120
source_pdf: 0811.2435v1.pdf
source_sha256: 615b04eca83bcade
doc_brief: "Stability structures, motivic — 43 sections: Introduction; Counting problems for 3-dimensiona; Non-commutative varieties with pol"
---
We also expect the following (not very precise) conjecture t o be true as well.
Conjecture 7 The collection (Ω( γ))γ∈Γ is invariant with respect to the “po-
larization preserving” deformations of C, in the case when C is homologically
smooth in the sense of [42].
The motivation for the last Conjecture is the deformation in variance of
the virtual fundamental class in the “classical” Donaldson -Thomas theory.
Recall that homologically smooth Ext-ﬁnite categories can be thought as
non-commutative analogs of smooth proper schemes. Hence, w e can expect
that the moduli stacks of semistable objects in such categor ies are also proper
in some sense. Therefore, we can also expect that the degree o f the virtual
fundamental class is invariant under deformations.
112
Also, we expect the following generalization of our theory i n the case
when k = C and the 3 d Calabi-Yau category is homologically smooth (see
[42]).
1) First, we recall that even without imposing the Calabi-Ya u condition
one expects that a triangulated compact homologically smoo thA∞-category
C (possibly Z/2Z-graded) admits (conjecturally) a non-commutative pure
Hodge structure (see [39], [36], [42] about motivations, de ﬁnitions as well
as some conjectures and applications of this notion). In par ticular, periodic
cyclic homology groups HPeven(C) (resp. HPodd(C)) carry descending Hodge
ﬁltrations
HPeven(C)···⊃ Fi
even⊃Fi−1
even⊃..., i∈ Z
HPodd(C)···⊃ Fi
odd⊃Fi−1
odd ⊃..., i∈ Z + 1
2 .
In 3d Calabi-Yau case we assume that the smallest non-trivial ter m of the ﬁl-
trationF•
odd isF−3/2, dimF−3/2 = 1. Moreover, in general, it is expected that
there are lattices Keven
top (C) and Kodd
top (C) which belong to the corresponding
periodic cyclic homology groups (they represent the non-co mmutative version
of the image of the topological K-theory in the de Rham cohomology).
2) IfC is homologically smooth Calabi-Yau category then it is easy to see
that (assuming the degeneration of the Hodge-to-de Rham con jecture, see
[42]) the moduli spaceM of formal deformations ofC is smooth of dimension
dimM = 1
2 dimHPodd(C) (this is a corollary of the formality of the little
disc operad as well as the fact that the action of the Connes di ﬀerential is
represented by the rotation of the circle, which is homotopi cally trivial under
the assumption). It is expected that the global moduli space also exists.
Notice that the Calabi-Yau structure on C induces a symplectic structure on
the vector space HPodd(C) and in the 3 d case the moduli space M is locally
embedded into HPodd(C) as a Lagrangian cone.
3) We expect that for an arbitrary triangulated compact homo logically
smooth A∞-categoryC one has a non-commutative version of the Deligne
cohomology HD(C) which ﬁts into a short exact sequence
0→HPodd(C)/(F 1/2
odd +Ktop
odd(C))→HD(C)→F 0
even∩Ktop
even(C)→ 0 .
113
Morally,HD(C) should be thought as zero cohomology group of the homotopy
colimit of the following diagram of cohomology theories:
HC−
• (C)

↓
Ktop
• (C)−−−→HP•(C)
where HC−
• (C) is the negative cyclic homology.
Any object of C should have its characteristic class in HD(C). More
precisely, there should be a homomorphism of groups chD :K0(C)→HD(C)
(in the case of Calabi-Yau manifold it is related to holomorp hic Chern-Simons
functional). The reason for this is that every object E∈Ob(C) has natural
characteristic classes in Ktop
0 (C) and in HC−
0 (C) whose images in HP 0(C)
coincide with each other. The total space Mtot of the ﬁbration Mtot →
M with the ﬁber HD(C) over the point [ C]∈M should be a holomorphic
symplectic manifold (cf. [20]). Moreover, any ﬁber of this ﬁ bration (i.e. the
groupHD(C) for given [C]) is a countable union of complex Lagrangian tori.
By analogy with the commutative case we expect that the locus L⊂M tot
consisting of values of chD is a countable union of Lagrangian subvarieties.
Every such subvariety can be either a ﬁnite ramiﬁed covering ofM or a
ﬁbration over a proper subvariety of M with the ﬁbers which are abelian
varieties.
4) For generic [ C]∈M one can use the triple ( K0(C),HD(C),chD) in-
stead of the triple ( K0(C), Γ, cl). Analogs of our motivic Donaldson-Thomas
invariants Amot
V ∈ RV will be formal countable sums of points in HD(C)
with “weights” which are elements of the motivic ring
Dµ. The pushforward
map from HD(C) to Γ = F 0
even∩Ktop
0 (C) gives the numerical DT-invariants.
The continuity of motivic DT-invariants means that after ta king the quasi-
classical limit the weights become integer-valued functio ns on the set of those
irreducible components of L which are ﬁnite ramiﬁed coverings on M.
These considerations lead to the following
Question 2 Is there a natural extension of the numerical DT-invariants to
those components of L which project to a proper subvariety of M?
Remark 26 Let us notice the similarity of the above considerations wit h
those in the theory of Gromov-Witten invariants. Suppose X is a 3d complex
114
compact Calabi-Yau manifold with H 1(X, Z) = 0 . Then we have an exact
sequence
0→H 3
DR(X)/(F 2H 3
DR(X) +H 3(X, Z))→H 4
D(X)→H 4(X, Z)→ 0 ,
where H 4
D(X) = H4(X, Z→O X→ Ω 1
X) is the Deligne cohomology. Then
any curve C ⊂ X deﬁnes the class [C] ∈ H 4
D(X). For a generic com-
plex structure on X the class is constant in any smooth connected family of
curves. Moreover, a stable map to X deﬁnes a class in H 4
D(X). Then we have
exactly the same picture with holomorphic symplectic ﬁbrat ionMtot→M
with the Lagrangian ﬁbers, as we discussed above. Similarly to the case of
DT-invariants the GW-invariants appear as inﬁnite linear c ombinations of
points in H 4
D(X), but this time with rational coeﬃcients. We expect that the
well-known relationship “GW=DT” (see [47]) should be a stat ement about the
equality of the above-discussed counting functions (assum ing positive answer
to the above question).
7.3 Absence of poles in the series AHall
V
Here we are going to discuss a stronger version of the Conject ure 5.
Conjecture 8 Let
D+ := Mµ(Spec(k))[L−1/2] be the ring of equivalence
classes of motivic functions. Then the automorphism of the m otivic quantum
torus given by x↦→Amot
V x(Amot
V )−1 preserves the subring ∏
γ∈C(V )∩Γ
D+ˆeγ for
all strict sectors V⊂ R2.
It is enough to check the conjecture for all x = ˆeγ,γ ∈ Γ. Moreover,
because of Factorization Property it is enough to consider t he case when
V = l is a ray. In the latter case we can split the inﬁnite product in to
those corresponding to diﬀerent arithmetic progression, h ence reducing the
conjecture to the case when Z(Γ) ∩ l = Z>0·γ0 for some non-zero γ0∈ Γ.
Then we have
Amot
l =Amot
l (ˆeγ0) = 1 +
∑
n/greaterorequalslant1
cnˆen
γ0∈
Dµ[[ˆeγ0]] .
Using the commutation relations in the motivic quantum toru s we have:
Amot
l (ˆeγ0) ˆeγ(Amot
l (ˆeγ0))−1 = ˆeγAmot
l (L⟨γ0,γ⟩ˆeγ0)Amot
l (ˆeγ0)−1 .
115
Since for any series f (t) = 1 + ... we have
f (Lnt)
f (t) = f (Lnt)
f (Ln−1t)... f (Lt)
f (t) ,
in order to prove the conjecture it suﬃces to check that
Amot
l (Lˆeγ0)Amot
l (ˆeγ0)−1∈
D+[[ˆeγ0]] .
Since in that case we are dealing with objects whose central c harges belong
to the ray l, we can restrict ourselves to the subcategory Cl. The latter
can be thought of as a heart of the t-structure of an ind-constructible 3 d
Calabi-Yau category with vanishing Euler form. More precisely, Cl(k) is
an abelian artinian category with Hom Cl(k)(E,F ) := Ext 0
C(
k)(E,F ). Then
K0(Cl(k))≃⊕ E⁄=0Z· [E], where the sum runs over the set of non-zero simple
objects of Cl(k).
Next, we can reduce the conjecture to a special case when cl k(E) = γ0
is a ﬁxed class for all simple objects E ofCl(k). Indeed, let us consider an
ind-constructible homomorphism cl ′
k : K0(Cl(
k))→ Γ′ := Z⊕ Z such that
cl′
k(E) = (1, 0) if cl k(E) = γ0 and cl′
k(E) = (0, 1) if cl k(E)∈{ 2γ0, 3γ0,... }
for a simple object E. Let choose two complex numbers z1,z 2 in such a way
that 0 < Arg(z1) < Arg(z2) < π and deﬁne a central charge Z′ : Γ ′→ C
by the formula Z′((1, 0)) = z1,Z′((0, 1)) = z2. In this way we obtain a new
stability structure on the triangulated envelope of Cl(
k) with the same heart.
In particular, the element Amot
l will be decomposed into an inﬁnite product:
Amot
l =
−→∏
Amot
l′
of series Amot
l′ corresponding to abelian categories Cl′(
k) for the new stability
structure. One of these categories will be the subcategory g enerated by
simple objects E such that cl ′
k(E) = γ0. Let us call such category pure of
class γ0. All other categories Cl′(
k) do not contain objects with the class
γ0. Repeating the procedure we reduce the conjecture to the cas e of pure
category of the class mγ0 for some m /greaterorequalslant1. Similarly to the above arguments
we can reduce it further to the case m = 1. In this case the conjecture follows
from the one below which concerns Hall algebras of categorie s which are no
longer required to carry a Calabi-Yau structure.
116
In order to formulate this new conjecture we are going to use t he fol-
lowing set-up. Let ( C,A) be a pair consisting of an ind-constructible tri-
angulated A∞-category over a ground ﬁeld k andA ⊂Ob(C) be an ind-
constructible subset such that A(k) is the heart of a bounded t-structure
inC(k). We assume that simple objects of the abelian category A(k) form
a constructible subset of Ob(C)(k) and every object in A(k) is a ﬁnite ex-
tension of simple ones. These data are equivalent to a specia l kind of an
ind-constructible category with a stability structure. Na mely, let us take
Γ := Z and deﬁne cl k(E) = 1 for every simple object of A(k). It follows
that cl k(F ) = length(F ) for any object of A(k). Furthermore, we choose
a complex number z0 in the upper-half plane and deﬁne a central charge
Z : Γ → C by the formula Z(1) = z0. Then A =Cl for l = R>0·z0. There-
fore the element AHall
l deﬁned for this stability structure can be thought of
as a series in one variable:
AHall
l (t) = 1 +
∑
n/greaterorequalslant1
cntn.
Let us deﬁne a subalgebra H +(C)⊂H(C) to be the set of linear combi-
nation of elements of the form
Ln· [Z→Ob(C)]
wheren∈ Z andZ→Ob(C) is a 1-morphism of ind-constructible stacks (see
Section 4.2) with Z being an ordinary constructible set endowed with trivial
action of the trivial group. The multiplication law in H(C) preserves such
class of elements.
Conjecture 9 The element Fl(t) := AHall
l (Lt)AHall
l (t)−1 belongs to the com-
pleted Hall algebra ˆH +(C) (i.e. we do not invert motives [GL(n)],n /greaterorequalslant1 of
the general linear groups).
Below we discuss two special cases in which the above conject ure holds.
But ﬁrst we present a similar motivating statement in the cas e of ﬁnite ﬁelds.
LetR be ﬁnitely generated algebra over a ﬁnite ﬁeld Fq, andR−modf denotes
the category of ﬁnite-dimensional (over Fq) left R-modules. We deﬁne the
Hall algebra H(R−modf ) as a unital associative algebra over the ring Z[ 1
q ]
generated by the isomorphism classes [ M] of objects of R−modf with the
117
multiplication
[E]· [F ] = q− dim Hom(F,E )
∑
α∈Ext1(F,E )
[Eα] ,
where, as before, Eα denotes an extension with the class α.
Proposition 13 Let
A(t) :=
∑
[M ]∈Iso(R−modf )
[M]
# Aut(M)t dimM .
Then
F (t) := A(qt)A(t)−1∈H(R−modf )[[t]] .
Moreover,
F (t) =
∑
I⊂R,I=RI, dimR/I<∞
[R/I]t dimR/I .
Hence the quotient F (t) does not have denominator ( qn− 1),n /greaterorequalslant1 and
can be represented in terms of the “non-commutative Hilbert scheme” of left
ideals in R of ﬁnite codimension.
Proof. Let us make use of the basis of “renormalized” elements
ˆ[E] := [E]
# Aut(E)
in the Q-algebra H(R−modf )⊗ Q. Then the product can be rewritten in
a more familiar form:
ˆ[E]·ˆ[F ] =
∑
[G]
c
c[G]
c[E], c[F ]
ˆ[G],
where the structure constant c
c[G]
c[E], c[F ]∈ Z denotes the number of subobjects in
G isomorphic to E and such that the quotient is isomorphic to F . In these
notation we have:
A(t) =
∑
[M ]
ˆ[M]tdimM .
118
Since ﬁrst statement of the Proposition follows from the sec ond one, we are
going to show the latter. In the new notation it becomes:
∑
I⊂R,I=RI, dimR/I<∞
ˆ[R/I]# Aut(R/I)tdimR/I·
∑
[M ]
ˆ[M]tdimM =
=
∑
[N ]
ˆ[N]qdimNtdimN .
Let us ﬁx an object N, and consider the coeﬃcient of the term ˆ[N]tdimN .
In the RHS it is equal to qdimN . It is easy to see that the corresponding
coeﬃcient in the LHS is of the form
∑
I⊂R,I=RI, dimR/I<∞
∑
N ′⊂N,N ′≃R/I
# Aut(R/I) =
=
∑
I⊂R,I=RI, dimR/I<∞
∑
֒→N
1 = #N =qdimN.
Notice that in the last sum we consider all possible embeddin gs of R/I to
N and every summand corresponds to a choice of a cyclic vector i n a cyclic
submodule in N. This proves the Proposition. ■
The above Proposition suggest to interpret our category as a category of
modules and then apply similar arguments which reduce the su m (or even
the motivic integral) to the sum over all cyclic submodules. It is useful to
keep this in mind when considering two examples in the next su bsection.
Remark 27 The subalgebra H +(C) of the Hall algebra has the advantage
that one can apply the Euler characteristic χ to its elements ﬁberwise over
Ob(C) , and get a constructible Z-valued function (with constructible support)
on the ind-constructible set Iso(C) of isomorphism classes of objects of C(k).
The multiplication in H +(C) descends to a multiplication on the abelian group
of such functions. It is easy to see that this multiplication is commutative,
and one has
νE×νF =νE⊕F
where νE etc. are delta-functions (see Section 6.1). This follows fr om the
fact that for any non-zero α∈ Ext1(F,E ) all objects Etα are isomorphic to
each other for t∈ k
×
, and the Euler characteristic of Gm is zero.
119
