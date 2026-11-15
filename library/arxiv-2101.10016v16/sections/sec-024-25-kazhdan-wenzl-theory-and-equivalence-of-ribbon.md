---
doc_id: arxiv-2101.10016v16
doc_title: "Unitary coboundary weak quasi-Hopf algebras in the Kazhdan-Lusztig-Finkelberg theorem"
section_id: sec-024-25-kazhdan-wenzl-theory-and-equivalence-of-ribbon
section_title: "Kazhdan-Wenzl theory and equivalence of ribbon slN,q,ℓ-categories"
section_number: 25
pages: 149-163
source_pdf: 2101.10016v16.pdf.txt
source_sha256: 51d21209730be025
toc_source: inferred
doc_brief: "Unitary coboundary weak quasi-Hopf algebras in the Kazhdan-Lusztig-Finkelberg theorem — We construct, for every complex simple Lie algebra g and every positive integer level k, a unitary modular"
---
25. Kazhdan-Wenzl theory and equivalence of ribbon slN,q,ℓ-categories
This section can be read independently of the rest of the paper. The main result is the
proof of Theorem 2.6, that highlights the relevance of our weak Hopf algebras in identifying
associators of two categories in presence of a braided symmetry using classification methods
by Kazhdan-Wenzl in the type A case. This principle will be used for the other Lie types
in this paper.
Let g be a simple complex Lie algebra. We keep the notation fixed in the first paragraph
of the previous section for C(g, q, ℓ). We recall that the fusion categories C(g, q, ℓ) arising
from quantum groups at roots of unity are deeply related to fusion categories arising from
chiral CFT on the circle. Let k be a positive integer and let Vgk denote the affine Vertex
Operator Algebra (VOA) of level k with Rep(Vgk) the associated representation category.
By results of Huang [90, 92, 93, 94] this is a modular fusion category. The work by Kazhdan
and Lusztig and Finkelberg [55], [56] culminated in the construction of a second modular
tensor category O˜
ℓ associated to modules of affine Lie algebras at positive integer levels
for all the Lie types except E6, E7 k = 1 and E8, k = 1, 2. The combination of these
works prove that O˜
k and C(g, q, ℓ) are equivalent as ribbon categories for the specific roots
of unity q = e
iπ/dℓ with ℓ = k + hˇ.
On the other hand, the approach to CFT via conformal nets [64] provides examples of
modular fusion categories as well [107]. A general connection from VOA satisfying suitable
analytic conditions to conformal nets has recently been established [22].
An important example is the fusion category associated to the loop group conformal net
over SU(N) which is known to have the same fusion rules [181] and modular data (the S and
T matrices) as the corresponding affine VOA or quantum group categories. More precisely,
the associated Verlinde fusion ring RN,ℓ arises from positive energy representations of the
level k central extension of the loop group of SU(N) and also as the Grothendieck ring of
Rep(Vgk) or C(slN , q, ℓ) for any q such that q
2
is a primitive root of unity of order ℓ, in this
case ℓ = k + N see e.g. [6, 161, 3].
It is then natural to ask whether there is a classification of ribbon fusion categories
with Verlinde fusion rules of type A showing in particular ribbon equivalence of the fusion
categories arising from the three different settings. In this section we give a classification
result independent of Finkelberg equivalence theorem. We shall not assume that our

150 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
categories have a unitary structure, and we replace this condition with the possibly weaker
assumption of pseudounitarity in the sense of [51]. In this way our result may be useful
for the purposes of Sect. 22, 23 for this special case. In that section we construct unitary
structures of the representation category of all the affine vertex operator algebras.
a) Let RN denote the representation ring of SL(N, C). It is freely generated with basis eλ
parameterised by the set of dominant integral weights Λ, so every λ ∈ Λ is a non increasing
sequence (m1, . . . , mN−1) of non negative integers.
b) For a positive integer ℓ > N, let Λ+(q) be the Weyl alcove recalled at the beginning
of the previous section. For g = slN , Λ+(q) may be described by weights λ ∈ Λ satisfying
m1 ≤ ℓ − N. The Verlinde fusion ring RN,ℓ has a natural basis eλ with λ ∈ Λ
+(q). The
structure constants are determined by the Verlinde formula (see [92] in the setting of vertex
operator algebras, and references therein), or via characters of the affine Weyl group, the
Kac-Walton formula Exercise 13.35 in [103], [179]. The fusion ring RN,ℓ may also described
as a quotient of RN by a certain ideal, see [44].
We set RN,∞ = RN , so the general notation RN,ℓ will include N + 1 ≤ ℓ ≤ ∞ unless otherwise stated (as it will be for example in the main theorem of the section). Furthermore,
RN,ℓ will be regarded as a based ring in the sense, e.g., of [143].
Note that a semisimple rigid tensor category C with based Grothendieck ring isomorphic
to RN,ℓ for ℓ finite is a fusion category.
Frobenius-Perron dimensions of basis elements FPdim(Xi) of a commutative based ring
were introduced in [63], and one has FPdim(Xi) > 0. We refer to Sect. 8 in [51] or Chapter
4 in [50] for the development of the theory in generality. We shall be interested in the case
of the based Grothendieck ring Gr(C) of a fusion category C endowed with its natural basis
given by the equivalence classes of irreducible objects.
The main result is that Xi → FPdim(Xi) extends uniquely to a homomorphism of
algebras ϕ : Gr(C) → R, and ϕ is the unique homomorphism such that ϕ(Xi) > 0 for all i,
see Theorem 8.2 and Lemma 8.3 in [51]. The global Frobenius-Perron dimension is defined
as FPdim(C) = P
i FPdim(Xi)
2
.
The global categorical dimension is in turn defined as the sum of the squared dimensions
|Xi|
2 of simple objects Xi
. Squared and global categorical dimensions were introduced and
studied by M¨uger for spherical fusion categories in [132], [135] and extended to general
fusion categories in [51]. It is known that |Xi|
2 > 0 and, if C is spherical, |Xi
|
2 = d(Xi)2
,
with d the categorical dimension defined via the spherical structure, see Sec. 27. In
particular, d(Xi)
2
is independent of the choice of the spherical structure.
A fusion category C is called pseudo-unitary if the global dimension dim(C) equals the
Frobenius-Perron dimension FPdim(C).
The squared dimension of every simple object Xiis bounded above by FPdim(Xi)
2
,
hence C is pseudo-unitary if and only if these are all equalities, see Prop. 8.21 in [51]. By
Prop. 8.23 of the same paper a pseudo-unitary fusion category admits a unique pivotal
structure, in fact spherical, such that the categorical dimensions of simple objects Xi are
positive, or equivalently coincide with the FPdim(Xi).
We next specialise to braided fusion categories. In this case, pivotal (spherical) structures are in a natural bijective correspondence with balanced (ribbon) structures for the

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 151
braided symmetry, and the correspondence is recalled in Sect. 27. It also follows from the
previous paragraph that a pseudo-unitary braided fusion category admits a unique ribbon structure inducing positive categorical dimensions. We shall refer to it as the positive
ribbon structure. The aim of this section is to show Theorem 2.6 stated in the introduction.
For N = 2 Theorem 2.6 has recently been shown in [14] using Fr¨ohlich-Kerler classification [63]. It follows from Ex. 25.14 that the positivity requirement on the ribbon structures
can not be removed. Moreover it will be clear from the proof how a ribbon structure can
be positive only for a unique braiding. We reformulate Theorem 2.6 in a form useful for
applications.
Theorem 25.1. Let C and C
′
be modular fusion categories with positive categorical dimensions and with Grothendieck rings isomorphic to the Verlinde fusion ring RN,ℓ via an
isomorphism compatible with the corresponding T-matrices. Then C and C
′ are equivalent
as ribbon tensor categories.
Proof. The categories are pseudo-unitary by positivity of the categorical dimensions. Compatibility of the T-matrices implies compatibility of the ribbon structures. The conclusion
follows from Theorem 2.6. □
Remark 25.2. (closely related results in the literature) We recall that a characterization
of braided slN,∞-type categories has been made explicit Neshveyev and Yamashita in [140],
see also the thesis by Jordans [101], and a classification of the braided symmetries may be
found in [148]. In [140] the authors settle down the problem of reconstructing the twisted
categories obtained from Kazhdan-Wenzl classification, see Theorem 25.4, as representation
categories of quantum groups of their own, for q a positive real number. We note that
a result closely related to our following Prop. 25.9 has also been obtained in [13] in the
C
∗
-case with different methods. We also note the recent paper [54] on closely related
topics. Moreover, an analogue of some of the results in [140] have recently been studied
by Giannone in his thesis [71], where the weak Hopf algebra of [25] plays the role of the
universal enveloping algebra Uq(g) for q positive.
Definition 25.3. Following [110], a semisimple rigid tensor category C together with an
isomorphism of based rings ϕC : RN,ℓ → Gr(C) is called of slN,ℓ-type. Two slN,ℓ-type
categories (ϕC, C) and (ϕC′, C
′
) are equivalent if there is a tensor equivalence E : C → C
′
inducing an isomorphism between the Grothendieck rings compatible with ϕC and ϕC′.
The proof of Theorem 2.6 will occupy the rest of this section and it is based on KazhdanWenzl theory [110]. To summarize, Kazhdan-Wenzl theory gives a classification of slN,ℓtype tensor categories in terms of the categories arising from quantum groups both for
generic or root of unity values of the deformation parameter q, and a 3-cocycle on the dual
of the center of SU(N) which modifies the natural associator. We start recalling the main
result. We shall then show that the positive ribbon structure completely determines the
ribbon tensor category under our assumptions. The most delicate part of our analysis is a
characterization of braided pseudo-unitary slN,ℓ-type fusion categories among general slN,ℓtype categories, stated as Cor. 25.13, and relies on the theory of quasitriangular weak Hopf

152 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
algebras developed in the paper. We also give a parameterisation of the braided symmetries
and a classification of their ribbon structures that is useful in our proof.
25.1. Proof of Theorem 2.6, case ℓ = N + 1. The based ring RN,N+1 identifies with
ZZN , with basis ZN the cyclic group of order N. Hence a slN,N+1-type fusion category C is
pointed over ZN . By Prop 4.1 in [110], see also Example 7.12 and references therein, Vecω
ZN
exhaust the slN,N+1-categories, which are classified by ω ∈ H3(ZN , T). A general braided
pointed fusion category over the finite abelian group G of equivalence classes of irreducible
objects determines a quadratic form on G via q(g) = c(γ, γ), where g is the class of γ.
The pair (G, q) determines C as a braided tensor category by Theorem 8.4.9 in [50]. By
Remark 4.13 in [138], if θ is the ribbon structure associated to a braided symmetry c and a
spherical structure in a fusion category then on every object X, θX = TrX ⊗1(c(X, X)). In
a pointed fusion category c(X, X) is a scalar and d(X) = ±1 if X is irreducible, and hence
d(X) = 1 under the positivity requirement, and therefore θX = c(X, X). Hence q(g) = θγ.
In other words the datum (G, q) is equivalent to that of the fusion rules and the positive
ribbon structure. The result applies in particular to slN,N+1-type categories and the proof
is complete in this case.
As remarked in Ex. 18.1 these categories are unitary in a natural way, so the pseudounitarity assumption holds automatically.
25.2. Kazhdan-Wenzl theory. Examples of slN,∞-type categories are the representation
categories of quantum slN -groups for generic values of the deformation parameter. Specifically, the quantum group of [52] was originally considered in [110]. Being a quantization
of a Hopf algebra of functions, the category is described by corepresentations. In the
setting of tensor C
∗
-categories, it is natural to consider the category of unitary corepresentations of Woronowicz SUq(N) group, where q is real, this is e.g. the starting point
of [145, 148, 140, 101]. We refer to [141] for details on the natural tensor C
∗
-structure.
In a more general framework where a C
∗
-structure is not assumed, one may consider the
category of representations of the Drinfeld-Jimbo quantum group Uq(slN ) for q a non-zero
complex number, not a nontrivial root of unity. By representations we understand those
which can be obtained as direct sums of subrepresentations of tensor products of Weyl
modules. If q is positive, SUq(N) and Uq(slN ) induce equivalent tensor categories, see
[141]. To unify with the examples C(slN , q) at roots of unity, we shall adopt DrinfeldJimbo framework.
In the following we assume ℓ > N + 1. Then slN,ℓ-category is determined up to tensor
equivalence by two invariants, qC and τC, a pair of nonzero complex numbers, unique up to
passing to the pair with reciprocal values, which determines the tensor category, together
with the fixed isomorphism ϕ, up to equivalence. These invariants are defined, and related
to each other, as follows.
Let X ∈ C be an object in the class of the image of (1, 0, . . . , 0) under ϕC. The tensor
product of X with any irreducible is multiplicity free, and the fusion rules can be found

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 153
in [110]. Let a ∈ (X2, X2) be the idempotent onto the subobject (1, 1, 0, . . . , 0). Then
there is a nonzero complex number qC (unique up to passing to the inverse) such that
T := qC(I−a)−a ∈ (X2, X2) gives rise via the usual construction Ti = 1i−1⊗T ⊗1
n−i−1
to a
representation of the braid group πn : Bn → (Xn, Xn). If g1, . . . , gn−1 are the generators of
Bn, thus satisfying the presentation relations gigi+1gi = gi+1gigi+1, πn takes gi → Ti. In our
formulas, for simplicity, we are assuming that the category is strict. This representation
factors through the defining relations (gi − qC)(gi + 1) = 0, i = 1, . . . , n − 1, of the Hecke
algebra Hn(qC) since a is an idempotent. Thus we have representations of the Hecke
algebras denoted with the same symbol,
π
+
n
: Hn(qC) → (X
n
, Xn)
compatible with the tensor structure. The ambiguity in the choice of qC also gives π
′
n
:
Hn(qC
−1
) → (Xn, Xn), which may equivalently be thought of as another Hecke algebra
representation on the same parameter
π
−
n
: Hn(qC) → (X
n
, Xn),
the opposite, or dual representation via π
−
n
:= π
′
nβ = π
=
n α using the canonical isomorphism
β : Hn(q) → Hn(q
−1
) which relates the corresponding canonical generators via gi → −qhi,
and α : gi ∈ Hn(q) → q − 1 − gi ∈ Hn(q).
Let Cq,N,ℓ denote C(slN , q, ℓ) for q
2 a primitive root of unity of order ℓ, for ℓ < ∞ and
Cq,N,∞ the category Rep(Uq(slN )) for q not a non-trivial root of unity. Note that Cq,N,ℓ
does not change, up to tensor equivalence, under the passage from q to q
−1
. This may
be seen as follows. For ℓ = ∞ there is an isomorphism from the quantum group Uq(g),
to Uq−1 (g) given by Ei → KiFi
, Fi → EiK−1
i
, Ki → Ki. For ℓ < ∞ we may use an
analogous isomorphism for Ux(g), where x is now an indeterminate, and the quantum
group is regarded over C(x), (see [161], with our x corresponding to q), and taking into
account Lusztig’s specialization of Ux(g) to Uq(g) for q is a complex primitive root of unity.
For details see e.g. in Sect. 9.3, and 11.2 in [24] (for q of odd order) and [161].
The category Cq,N,ℓ becomes an slN,ℓ-type category as follows. Set X = Xq, the natural
N-dimensional representation of Uq(slN ), and ϕq : RN,ℓ → Gr(Cq,N,ℓ) the natural identification. We realize T as the element −σ defined in (4.13) of [191], with q in place of µ and
consider the associated Hecke algebra representations πn.
For a general slN,ℓ-category, it turns out that qC is a primitive root of unity of order ℓ for
ℓ finite, and is not a nontrivial root of unity for ℓ infinite. In the first case, Hn(qC) is not
semisimple for large values of n. In both cases, the kernels of π
+
n
and π
−
n
are completely
determined by the fusion rules, and the two representations are distinguished by the value
taken by a certain scalar invariant µC, see Theorem 4.1 in [110], which corresponds to the
value of a categorical left inverse of X on T, in the sense of [118] in the Hecke category.
The second invariant, called the twist of the category, is given by τC = p⊗1X ◦T1,N ◦1X ⊗
ν ∈ (X, X) ≃ C, where ν ∈ (ι, XN ) and p ∈ (XN , ι) satisfy p ◦ ν = 1 and T1,N = TN . . . T1
is an Hecke algebra element in the representations πn exchanging the first factor in a tensor
product of N + 1 objects with the following N factors. More precisely, if the category is

154 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
not strict, XN = ((X ⊗X)⊗X). . . and we need to use associativity morphisms in defining
τC.
Given C, with associativity morphisms α, and given a N-th root of unity w, we may
consider a new tensor category, C
w with the same representation ring, the same structure
as C except for the associativity morphisms, which are modified as follows,
α
w
Xλ,Xµ,Xν
:= w
γ(|λ|,|µ|)|ν|αXλ,Xµ,Xν
, (25.1)
for λ, µ, ν ∈ Λ (or in Λ+(q) accordingly), where γ is the function γ(a, b) = [ a+b
N
]−[
a
N
]−[
b
N
]
and |λ| = m1 + · · · + mN−1.
It is easy to see that qC does not change when passing to a twisted category. This is not
the case for τC, which does change and in fact determines the root of unity w defining the
twist. Indeed, starting with a given C as before, if X is the conjugate of X naturally realized
as a subobject of XN−1, we have ν ∈ (ι, X ⊗ X). Taking into account the associativity
morphisms, it follows that τC is the composite (X0 = X)
X0 −→ X0(XX)
α−1
−→ (X0X)X
T1,N−1⊗1
−→ (XX0)X (25.2)
α−→ X(X0X)
1⊗T1,1 −→ X(XX0)
α−1
−→ (XX)X0 −→ X0. (25.3)
Passing from C to C
w gives rise to a modification in the computation of the corresponding
invariant only on the associativity morphisms. More precisely, the second part, (25.3), does
not change, by centrality of the deforming factor in α
w, see (25.1), while (25.2) changes by
a factor w
−1
. This follows from a simple computation, since X corresponds to (1, . . . , 1).
Thus τCw = w
−1
τC.
The following theorem is due to Kazhdan and Wenzl [110]. For completeness sake we
include a proof.
Theorem 25.4. Let C be a slN,ℓ-type tensor category with N + 1 < ℓ ≤ ∞, ϕC : RN,ℓ →
Gr(C) an isomorphism and let X, qC and τC be defined as above. Then there is a N-th root
of unity w such that τC = (−1)N w
−1
q
N−1
, where q is a complex square root of qC. The pair
(qC, τC) is unique up to the pair with reciprocal values and determines the pair (C, ϕC) up
to equivalence. Furthermore, there is an equivalence of (C, ϕC) with (C
w
q,N,ℓ, ϕq).
Proof. Kazhdan-Wenzl left inverse µC takes the value stated in Theorem 4.1 in [110] on
T. It follows that the representation πn of the Hecke algebra is quasi equivalent to that
arising from the quantum group in Cq,N,ℓ. In the generic case, a computation of τC as
in the statement may be found e.g. in Lemma 8.1 of [148], version in arXiv. with Ti
corresponding to −gi there, based on a computation of the left inverse on the generator T
for C = Cq,N,ℓ and the mentioned Hecke algebra representation of the quantum group, see
Prop. 4.1 and Theorem 3.3 (a) in [145], with N and µC in turn corresponding to d and λ−d
there. See also [101]. In the root of unity case, we may argue in the same way, using now
Theorem 3.3 (b) [145] and replacing S with the morphism still denoted S of the appendix
of [25], and derive in a similar way an N-th root of unity w such that τC takes the stated
value. We then conclude following [110]: up to passing to C
w−1
, we may assume with no
loss of generality that τC = (−1)N q
N−1
, by (25.2), and (25.3). We have thus reduced the

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 155
values of the invariant qC, τC to those it would take on Cq,N,ℓ. It is easy to see that this value
of τC in the twisted category means that the element ν ∈ (ι, X N ) of [110] and the Hecke
algebra representations together satisfy the setting of section 6 in [145], that is equations
(6.1)–(6.4), where a (braided) tensor equivalence with Cq,N,ℓ has been exhibited for q real
taking X to Xq, thus compatible with ϕ and ϕq. More precisely, braided symmetries are
constructed from certain normalizations of the Hecke algebra generator which is necessary
to match T with the R-matrix of the quantum group in the representation X. There is
minimal change for other generic values of q. For the root of unity case, we may argue
similarly, using the information and analogous equations in the appendix of [25] again. □
It will be useful for us to specialize Kazhdan-Wenzl theory to the untwisted tensor
categories. In the following result, ≃ denotes an equivalence between pairs (C
w
q,N,ℓ, ϕq).
Corollary 25.5. Let q ∈ C
× be either not a non trivial root of unity or such that q2
is
a primitive root of unity of order ℓ > N + 1, and let q
′ ∈ C× be another complex number
with the same property. Then:
For N even,
a) Cq,N,ℓ ≃ Cq
′
,N,ℓ if and only if q
′ = q or q′ =
1
q
;
b) C−q,N,ℓ ≃ C
−1
q,N,ℓ.
For N odd, Cq,N,ℓ ≃ Cq
′
,N,ℓ if and only if q
′ = ±q, q′ = ±
1
q
.
25.3. Braided symmetries in slN,ℓ-type categories. Since the work of [52, 191] and
the theory of universal R-matrix of Drinfeld, see e.g. [24], it has been known that Uq(g)
gives rise to braided tensor categories. For the case of C(slN , q) see e.g. [161]. There is
a simple parameterisation of all the possible braided symmetries of Cq,N,ℓ. We start with
the two canonical braided symmetries, ε
+ and its opposite ε− derived from the R-matrix
of the quantum group and its opposite, R
−1
21 , respectively, see also remark 25.7.
Proposition 25.6. Let z and z
′
vary among the N-th roots of unity. Then for N + 1 <
ℓ ≤ ∞ there are 2N braided symmetries, ε
+
z and ε
−
z
′ of Cq,N,ℓ uniquely determined by
ε
+
z
(X, X) = zε+(X, X), ε−
z
′(X, X) = z
′
ε
−(X, X).
Furthermore, this is a complete list.
Proof. Since Cq,N,ℓ admits X as a generating object, any braided symmetry c is determined
by c(X, X) thanks to (5.7), (5.8), (5.9) By the fusion rules of X2, a suitable normalization
of c(X, X) will induce a representation of a Hecke algebra. By Kazhdan-Wenzl theory,
the eigenvalue of the properly normalized c(X, X) corresponding to I − a can only be q
±1
C
,
so that c(X, X) is a scalar multiple of ε
+(X, X) or ε−(X, X). By naturality of c(X, X)
on the morphism ν ∈ (ι, XN ), the scalar is a N-th root of unity. Conversely, for any
N-th root of unity z, the modified morphisms cz(Xn, Xm) = z
nmc(Xn
, Xm) still satisfy
the same relations and also the naturality property on the full subcategory with objects
tensor powers of X, and hence everywhere, as a consequence of (Xn, Xm) ̸= 0 if and only
if n ≡ m(modN). We may then apply these considerations to ε
+ and ε−. □

156 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
Remark 25.7. The braided symmetries described in the previous proposition are perhaps
more clearly explained by the specialization process of the R-matrix of the quantum group.
More precisely, this matrix, at the level of the integral form U
†
A′(g) of Ux(g), with x a formal
variable as in [161] where our x corresponds to q in that paper, depends on a root s of
order L of x via s
L = x, where L is the smallest integer such that for any pair of dominant
weights λ, µ, L⟨λ, µ⟩ is an integer. The values of L are listed in table 1 in [161]. We
then specialize x to a primitive complex root of unity q, and let ℓ
′ be its order and s to
a fixed but arbitrary complex L-th root q
1/L of q. Note that our q1/L is not necessarily a
primitive root of unity of order Lℓ′ as in Sect. 2 in [161], thus our specialization needs to
be slightly generalized. One has L = N for g = slN . It follows that X ⊗ X(R) corresponds
to the operator computed in Sect. 8.3G of [24], where e
h
corresponds to x and gives rise
to our braided symmetry ε
− through ε−(X, X) = ΣX ⊗ X(R). The N possible choices of
s = q
1/N give the symmetries z′
ε
−, and a similar relation holds between the specialization
of opposite R-matrix R
−1
21 and the symmetries zε+.
The 2N braided symmetries of Prop. 25.6 give rise to braided tensor categories (Cq,N,ℓ, ε±
z
).
We shall need the following property.
Remark 25.8. Our aim is to show that the identity isomorphism between the representation rings of any two of (Cq,N,ℓ, ε±
z
) can not be induced by a braided tensor equivalence.
An explicit proof of this fact between two categories of the kind (Cq,N,ℓ, ε+
z
) (or (Cq,N,ℓ, ε−
z
))
which fixes the generating object X may be found e.g. at page 8 of [148] (arxiv version) for
q real. Those arguments extend to a nonzero complex generic q or to the root of unity case
with the same modifications indicated in the proof of Theorem 25.4. Since an isomorphism
between two objects in a braided tensor category induces a braided tensor equivalence between the full braided tensor subcategories they generate, it also follows that there is no
braided tensor equivalence which takes the generating object X to an equivalent object,
and the conclusion follows in this case. On the other hand for a pair of the kind (Cq,N,ℓ, ε+
z
)
and (Cq,N,ℓ, ε−
z
′), an argument may be found in the proof of Theorem 2.6 relying on the
comparison of the ribbon structures.
We refer the reader also to [18, 19] for further studies on these braided symmetries.
Up to a sign change of q = (qC)
1/2
for N even, an slN,∞-type braided tensor category C
is tensor equivalent to some Rep(Uq(slN )). (The case N = 2 holds without the braided
symmetry requirement, as it follows from the work of [63], or also from Theorem 25.4,
since H3(Z2, T) ≃ Z2, see also Cor. 25.5.) For N > 2 a proof has been given in Remark
4.4 of [140] based on the Tannakian property of Rep(Uq(slN )) which provides a discrete
Hopf algebra. We need to extend this result slN,ℓ-type categories for ℓ < ∞. However it
is not obvious how to modify the methods of [140] for general q (with q
2
is a primitive
root of unity of order ℓ) as the categories C(slN , q) are not associated to Hopf algebras.
Perhaps the most natural way to proceed is to restrict to some subclass large enough to
hold our applications. We shall thus first consider only the roots of unity q such that
q
2
is of order large enough as in Def. 19.1. This will enable us to replace the role of the
discrete Hopf algebra of [140] with the weak Hopf algebra A = AW (slN , q, ℓ) of Sect. 32, its
quasi-triangular structure developed in Sect. 10 and the notion of 3-coboundary associator

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 157
for weak Hopf algebras, Sect. 9. We shall include a proof since it becomes slightly more
technical due to non-triviality of the associator of A.
Proposition 25.9. Let (C, ϕC) be an slN,ℓ-type tensor category and assume that either
ℓ = ∞ or q = q
1/2
C = ±e
±iπ/ℓ (or, more generally q2 = qC of order large enough as in Def.
19.1). Then C admits a braided symmetry if and only if w = 1 for N odd and w = ±1 for
N even.
Proof. The case ℓ = ∞ (q generic) has been considered in [140]. By Kazhdan-Wenzl
theory an slN,ℓ-type category (C, ϕC) is equivalent to (C(slN , q, ℓ))w, ϕq). For the case
q = ±e
±iπ/ℓ recall that the weak Hopf algebra AW (slN , q, ℓ) of Sect. 32 has representation
category tensor equivalent to C(slN , q, ℓ). Let, as before, ∆ and Φ = 1 ⊗ ∆(P)∆ ⊗ 1(P),
P = ∆(I), be the natural coproduct and associator of A. Consider the weak quasi bialgebra
Aw = (A, ∆, Φw), with the new associator Φw = ΦΥw, where Υw = Υ ∈ A ⊗ A ⊗ A is
the central invertible element given by Υ = w
γ(|λ|,|µ|)|ν|
. Let us regard C(slN , q, ℓ) as tensor
equivalent to Rep(A) and therefore C(slN , q, ℓ)
w to Rep(Aw). Let Rq denote the R-matrix
of A, hence by Prop. 10.4
∆ ⊗ 1(Rq) = Φ312(Rq)13(Rq)23Φ, 1 ⊗ ∆(Rq) = Φ−1
231(Rq)13(Rq)12Φ
−1
123.
If we assume that C is braided then so is Rep(Aw), hence by duality Aw is quasi-triangular.
Let R be the corresponding R-matrix. Thus R satisfies equations (10.2)–(10.5) with respect
to Φw. Since Υ123 = Υ213, taking also into account the computations in the proof of Prop.
10.4, equations (10.4)–(10.5) become
∆ ⊗ 1(R) = Φ312R13R23ΦΥ, 1 ⊗ ∆(R) = Υ−1
231Φ
−1
231R13R12Φ
−1
123.
We consider the twist F = R−1
q R, cf. (10.15), which satisfies ∆F = ∆ and
I ⊗ F1 ⊗ ∆(F) = [I ⊗ Rq1 ⊗ ∆(Rq)]−1I ⊗ R1 ⊗ ∆(R),
F ⊗ 1∆ ⊗ 1(F) = [∆op ⊗ 1(Rq)Rq ⊗ 1]−1∆
op ⊗ 1(R)R ⊗ 1.
We set, as before, P = a ⊗ b, ∆(a) = a1 ⊗ a2, ∆(b) = b1 ⊗ b2 and compute
I ⊗ Rq1 ⊗ ∆(Rq)[∆op ⊗ 1(Rq)Rq ⊗ 1]−1 =
(Rq)23Φ
−1
231(Rq)13(Rq)12Φ
−1
123(Rq)
−1
12 Φ
−1
213(Rq)
−1
13 (Rq)
−1
23 Φ
−1
321 =
(Rq)23Φ
−1
231(Rq)13(Rq)12∆ ⊗ 1(P)1 ⊗ ∆(P)∆ ⊗ 1(P)(Rq)
−1
12 b1 ⊗ a ⊗ b2(Rq)
−1
13 (Rq)
−1
23 Φ
−1
321 =
(Rq)23Φ
−1
231(Rq)13(a2 ⊗ a1 ⊗ b)(b1 ⊗ a ⊗ b2)(Rq)
−1
13 (Rq)
−1
23 Φ
−1
321 =
(Rq)23(b ⊗ a1 ⊗ a2)(Rq)13(1 ⊗ ∆(P)∆ ⊗ 1(P)1 ⊗ ∆(P))213(Rq)
−1
13 (Rq)
−1
23 Φ
−1
321 =
(Rq)23(b ⊗ a1 ⊗ a2)(b2 ⊗ a ⊗ b1)(Rq)
−1
23 Φ
−1
321 =
(Rq)23(∆ ⊗ 1(P)1 ⊗ ∆(P)∆ ⊗ 1(P))231(Rq)
−1
23 (b2 ⊗ b1 ⊗ a) =
(b ⊗ a2 ⊗ a1)(b2 ⊗ b1 ⊗ a) = Φ−1
321.
Hence, using centrality of Υ,
[I ⊗ F1 ⊗ ∆(F)]−1F ⊗ 1∆ ⊗ 1(F) =
[I ⊗ R1 ⊗ ∆(R)]−1I ⊗ Rq1 ⊗ ∆(Rq)[∆op ⊗ 1(Rq)Rq ⊗ 1]−1∆
op ⊗ 1(R)R ⊗ 1 =

158 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
Υ231Φ123R
−1
12 R
−1
13 Φ231R
−1
23 Φ
−1
321Φ321R23R13Φ213R12Υ123 =
Υ231Φ123R
−1
12 R
−1
13 Φ231R13Φ213R12Υ123 = ΦΥ231Υ,
we have omitted the computations leading to the last equality, as they are very similar to
the previous ones. Hence ΦΥ231Υ satisfies (9.1), and one may similarly establish validity
(9.2), thus ΦΥ231Υ is a 3-coboundary associator which may be twisted to Φ by F by Prop.
9.13. On the other hand as observed in [140] (Υw)231Υw is cohomologous to Υw2 on the
dual of the center of SU(N), and therefore we find a tensor equivalence between C(slN , q, ℓ)
and C(slN , q, ℓ)
w2
which identifies the generating representations, and hence is compatible
with the chosen isomorphisms with RN,ℓ. From Kazhdan-Wenzl classification we derive
w
2 = 1 and we finally apply Cor. 25.5. □
25.4. Pseudo-unitarity. If a given ribbon structure for the braided symmetry of a fusion
category C induces a spherical structure making the categorical dimensions of the simple
objects positive then C is pseudo-unitary. It follows that C(slN , q, ℓ) is pseudo-unitary for
q = ±e
±iπ/ℓ and N + 1 < ℓ < ∞ with respect to the natural ribbon structure, by [2] (and
in fact unitary by [185, 194]). In this subsection we prove that these fusion categories may
be intrinsically characterized among general fusion slN,ℓ-type categories by the property of
being both braided and pseudo-unitary.
Proposition 25.10. Let q ∈ C be such that q
2
is a non-trivial root of unity of order
ℓ > N + 1. Then C(slN , q, ℓ) is pseudo-unitary if and only if q = ±e
±iπ/ℓ
.
Proof. Our proof follows that of an analogous result for the Lie type B given in Theorem
3.8 in [159], with a slight modification due to the non-uniqueness of the spherical structures
for N even in our case, see the following Prop. 25.11. More in detail, we write q = ±qz,
with qz = e
iπz/ℓ and z an integer with 1 ≤ z ≤ ℓ − 1 and gcd(z, ℓ) = 1. Let X be
the object of C(slN , q, ℓ) corresponding to the fundamental representation and assume
N = 2k even. Up to a sign, the categorical dimension d(X) with respect to any spherical
structure equals dqz(X) := qz
N−1 + qzN−3 + · · · + qz−(N−1) = 2Pk
j=1 cos((2j − 1)πz/ℓ).
Furthermore, FPdim(X) = dq1(X′) where X′is a corresponding object in the category
C(slN , q1) for q1 = e
iπ/ℓ, since these two categories have isomorphic representation rings
with an isomorphism identifying X to X′ and we know that dq1takes positive values on
the irreducibles. We claim that dqz(X) < dq1(X′) for z ̸= 1. Thus if dqz(X) > 0 then
|d(X)| = dqz(X) which then can equal FPdim(X) only if q = ±e
iπ/ℓ. If dqz
(X) < 0
then |d(X)| = −dqz(X) = 2Pk
j=1 cos((2j − 1)π(ℓ − z)/ℓ). Since ℓ − z satisfies the same
properties as z, pseudo-unitarity again implies ℓ − z = 1 hence q = ±e
−iπ/ℓ. To show the
claim, observe that the set S1 of points q1
2j−1 = ei(2j−1)π/ℓ
, j = 1, . . . k all lie in the upper
semicircle. Furthermore the conditions gcd(z, ℓ) = 1 and ℓ ≥ N + 2 imply ℓ ∤ (2j − 1)z.
In particular qz
2j−1 ̸= 1 for all j. Assume that z is such that the subset S2 of {q
±(2j−1)
z }
contained in the upper semicircle differs from S1. The first point in the natural order of the
semicircle is q1. Furthermore two adjacent points of S2 correspond to arcs whose distance
is at least 2π/ℓ. Therefore there must be an element of S1 in between unless they both lie

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 159
after the last q
N−1
1
. Since cos is an even function, it follows that dqz(X) may be computed
considering elements of S2, and we have dqz
(X) < dq1(X′) by the above remarks. We are
left to show that for z ̸= 1, S1 ̸= S2. For this we may apply arguments analogous to those
of the last part of the mentioned theorem of [159].
In the case where N is odd the proof is simplified by the fact that C(slN , q, ℓ) admits
a unique spherical structure, so d(X) is uniquely determined. We may thus complete the
proof with argument similar to the even case, taking into account the additional information that d(X) = q
N−1
z + · · · + q
−(N−1)
z = −1 + 2Pk
j=0 cos(2jπz/ℓ) where N = 2k + 1.
□
For completeness we recall from Example 18.1 that C(slN , q, ℓ) are always unitary if q
2
is a primitive root of unity of order ℓ = N + 1. Here below we remark about classification
of spherical structures on Cq,N,ℓ.
Proposition 25.11. For N odd, Cq,N,ℓ has a unique spherical structure, for N even it has
two.
Proof. In a fusion category C spherical structures are parameterised by the group of
monoidal natural transformations from the identity functor to itself and taking values
±1 on the irreducibles, see Exercise 4.7.16 of [50] for a precise statement. In the case
where C admits a simple generating object X, any such natural transformation η is determined by the value it takes on X as follows. If ηX = λ1X then on any tensor power,
ηXr = λ
r1Xr by monoidality. It follows from naturality and complete reducibility that the
values that η takes on the simple summands of Xr also coincide with λ
r
. Hence if λ = 1
then η is the identity natural transformation, while if λ = −1 then η takes value 1 (−1)
on the simple summands of even (odd) tensor powers of X. In our specific case, if X = Xq
we must have λ
N = 1 since the tensor unit is a subobject of XN
q
. Hence for N odd the
conclusion follows. For N even, the specific fusion rules of an slN -type tensor category
show that any odd tensor power of Xq is disjoint from an even tensor power. This implies
existence of a monoidal natural transformation η ∈ (1, 1) taking these values. □
The next step is that of characterizing general pseudo-unitary slN,ℓ-type fusion categories
for ℓ > N + 1. To do this, we regard the relationship between C(slN , q, ℓ)
w, and C(slN , q, ℓ)
as an example of a general construction described in [15] of a new fusion category C
ω
from
from a given one C and a T-valued 3-cocyle ω on the chain group Ch(C), and we study
invariance of pseudo-unitarity under ω in this framework.
Let C be a semisimple monoidal category with associativity morphisms α. The chain
group Ch(C) introduced in [10, 69] is defined as follows. Consider a complete family
Irr(C) = {ρα, α ∈ A} of simple objects of C endowed with the smallest equivalence relation
≃ making all the irreducible subobjects ργ appearing in the decomposition of ρα ⊗ ρβ for
fixed α, β ∈ A, equivalent. Then Ch(C) = Irr(C)/ ≃ is a group with [ρα][ρβ] = [ργ].
The trivial element is the class of the tensor unit, and [ρα]
−1 = [ρα]. This is an interesting
group. For example, it identifies naturally with the dual of the centre of the compact group
G for C = Rep(G) [133]. Furthermore, the group of nonzero C-valued homomorphisms
on Ch(C) identifies with the group of natural monoidal transformations of the identity

160 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
functor on C [69, 15]. Finally, for modular categories, Ch(C) identifies with the dual of the
(abelian) group of invertible elements of C [69].
The chain group induces a grading on C, in the sense that there are full subcategories Cg
indexed by elements of g ∈ Ch(C) such that every object ρ ∈ C decomposes uniquely up
to isomorphism into a direct sum of objects ρg ∈ Cg and with the property that for g ̸= h,
objects of Cg are disjoint from objects of Ch. The group structure of Ch(C) implies that
the grading is compatible with the tensor structure: ι ∈ Ce and ρ ⊗ σ ∈ Cgh for ρ ∈ Cg,
σ ∈ Ch.
We consider C
ω
, the monoidal category with the same structure as C except for the
associativity morphisms, which are given by α
ω
ρ,σ,τ = ω(g, h, k)αρ,σ,τ , where [ρ] = g, [σ] = h,
[τ ] = k. Note that C
ω may be regarded as a special case of a categorical analogue of
Prop. 7.11. In other words, C and C
ω have isomorphic Grothendieck rings and chain
groups, and, in the framework of fusion categories, they have the same Frobenius-Perron
dimension function. We denote by dC(ρ) and dCω (ρ) the categorical dimensions of an object
ρ considered in C or C
ω
respectively with respect to preassigned spherical structures.
Proposition 25.12. Let C be a fusion category and ω ∈ Z
3
(Ch(C); T) normalized. If D
is the right duality functor of C associated to the right duality (ρ
∨
, bρ, dρ) and η ∈ (1, D2)
is a pivotal (spherical) structure then (ρ
∨
, bω, dω) is a right duality for C
ω where bω
ρ =
bρ, d
ω
ρ = dρω
−1
(g, g−1, g), with ρ simple and [ρ] = g. Furthermore η
ω = η is a pivotal
(spherical) structure for the associated right duality functor Dω. In particular, if η is
spherical under the correspondence (η, D) → (η
ω
, Dω) we have dC(ρ) = dCω (ρ) for every
object ρ. Furthermore, C is pseudo-unitary if and only if so is C
ω
.
Proof. Let ρ be an object of Cg and let (b, d), (b
′
, d′) solve the right and left duality
equations respectively for ρ in C in the sense of (5.1)–(5.4) with ρ
∨ = ∨ρ. Then a solution
of the corresponding equations in C
ω
is given by (b
ω
, dω), (b
′ω
, d′ω) where b
ω = b, dω =
dω−1(g, g−1, g), b
′ω = b′ω(g, g−1
, g), d
′ω = d′
. To verify the duality relations it is useful to
recall the equality ω(g, g−1, g) = ω(g
−1
, g, g−1)
−1 which follows from the 3-cocycle equation
for ω.
We now start with a right duality (ρ
∨
, bρ, dρ) in C and recall that the associated right
duality functor D was defined in (5.6). The right duality functor Dω of C
ω associated
with the solution (ρ
∨
, bω
ρ
, dω
ρ
) of the previous paragraph acts as D on objects, while on
morphisms T ∈ (ρ, σ) with σ ∈ Ch we have Dω(T) = ω
−1
(h, h−1, h)D(T). Let η ∈ (1, D2)
be a pivotal structure. Consider the left duality (ρ
∨
, b′
ρ
, d′
ρ
) defined by (27.3) with η in
place of u. It follows that C
ω has left duality (ρ∨
, b′ω
ρ
, d′ω
ρ
). The natural transformation η
ω
in C
ω defined by (27.4) with d′
ω
and bω in place of d
′ and b takes the same values as η.
Furthermore the natural transformation say Fρ,σ in C making D2into a tensor functor is
also natural in C
ω and makes D2
ω
into a tensor functor. Indeed, it is easy to see that D2
ω
acts as D2 on αρ,σ,τ if ρ, σ, τ are homogeneous, and therefore in general. It follows that
validity of Def. 4.8 for D2implies validity for D2
ω by linearity. Hence η
ω
is monoidal by
Def. 4.7, and therefore is a pivotal structure in C
ω which is spherical if so was η. The
formulas also show that dC(ρ) = db′ = dωb
′
ω = dCω (ρ) with respect to these structures.
Since C and C
ω have the same global FPdim, the last assertion is also clear.

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 161
□
Corollary 25.13. Among the slN,ℓ-type tensor categories (C, ϕC) with N + 1 < ℓ < ∞
only those equivalent to some (C(slN , q, ℓ))w, ϕq) ((C(slN , q, ℓ), ϕq) resp.) with q = e
iπ/ℓ for
N odd and q = ±e
iπ/ℓ for N even are pseudo-unitary (pseudo-unitary and braided resp.).
Proof. This follows immediately from Propositions 25.10, 25.12, 25.9, Cor. 25.5. □
25.5. Proof of Theorem 2.6, case ℓ > N + 1.
Proof. Let us fix an isomorphism of based rings ϕC : RN,ℓ → Gr(C). Then (C, ϕC) is equivalent to (C(slN , q, ℓ), ϕq) with q = e
iπ/ℓ for N odd and precisely to one of (C(slN , q, ℓ), ϕq)
where q takes the values q = ±e
iπ/ℓ for N even, according to an equivalence E inducing ϕC, by Cor. 25.13. A similar conclusion holds for (C
′
, ϕC′) for any choice of
ϕC′ : RN,ℓ → Gr(C
′
). We fix ϕC′ = f ◦ ϕC, and denote by E
′
the corresponding equivalence with (C(slN , q′
, ℓ), ϕq
′). Using the based ring isomorphisms induced by E and E
′
between the Grothendieck rings, their compatibility with ϕC and ϕC′, we find an isomorphism g : Gr(C(slN , q, ℓ)) → Gr(C(slN , q′
, ℓ)) which identifies the classes of the respective
generating representations Xq and Xq
′. Let us now take into consideration the braided
symmetries, say c and c
′ of C and C′
respectively, and their ribbon structures, identified
with analogous structures in the quantum group categories via the equivalences and denoted in the same way. For C(slN , q, ℓ) we can only have c = zε+ or c = z
′
ε
− by Prop. 25.6,
where z and z
′ have the same meaning. Taking into consideration Remark 25.7, we identify
each of the 2N possible braided symmetries with one derived from the R-matrix R or the
opposite R
−1
21 , subject to a choice of a complex N-th root q
1/N . Then C(slN , q, ℓ) becomes
a ribbon category with positive ribbon structure ˜θλ = q
±⟨λ,λ+2ρ⟩
, where ⟨ , ⟩ is a symmetric
invariant bilinear form of slN such that ⟨α, α⟩ = 2 for (short) roots, the plus or minus sign
are determined by the choice of R or R
−1
21 , see [24]. On the other hand C(slN , q, ℓ) also
has the positive ribbon structure θλ, hence θλ = ˜θλ by uniqueness of the positive ribbon
structures recalled before the statement of Theorem 2.6. Assuming that θ corresponds to
the plus sign we have that θXq = q
N2−1
N (more details on this formula may be found in the
proof of the following proposition). We claim that we may assume that θ
′
corresponds to
a plus sign as well. Hence we similarly have θXq
′ = q
′
N2−1
N . If N is odd we have already
settled q = q
′ and our assumption θXq = θXq
′
shows that we are taking the same Nth root
of q, and therefore we have a braided, in fact ribbon, tensor equivalence. If N is even then
N2 − 1 is odd, and since θ
N
Xq = θ
N
Xq
′ we may exclude that q and q
′ have opposite signs. It
follows again that the two Nth roots of q are the same and we get the same conclusion.
We finally show the claim. If on the contrary we had an opposite symmetry c
′
in C
′
then
q = q
′−1
for N = 2 and q
2 = q′−2
for N > 2. In the first case we conclude as before since
by Prop. 25.5 q and q
−1 gives rise to equivalent tensor categories again. In the second case
we use the twist equation c(Xq, Xq)
2 = θXq ⊗ θXq ◦ θ
−1
Xq⊗Xq
and similarly for Xq
′, θ
′ and c′
,
which implies c(Xq, Xq)
2 and c′
(Xq
′, Xq′)
2 have the same eigenvalues. This implies q4
C = 1
and therefore N + 1 < ℓ ≤ 4 giving no solution. □

162 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
Note that the positivity assumption in Theorem 2.6 is redundant for N odd by uniqueness of the ribbon structure of every braided symmetry of Cq,N,ℓ, Prop. 25.11. The following
example shows that this assumption can not be dropped for N even.
Example 25.14. Consider C(sl2, q, ℓ) for q = e
iπ/ℓ with ℓ > 3 and the braided symmetries
ε
+
1
and ε
+
−1 described in Prop. 25.6. By Remark 25.8, the identity isomorphism between
the corresponding representation rings can not be induced by a braided tensor equivalence.
On the other hand, each of the two braided categories has its own positive ribbon structure,
say θ1 and θ−1 respectively. For an irreducible λ = aΛ1 we have θ1(λ) = q
a
2
(a+2)
, θ−1(λ) =
(−q
1/2
)
a(a+2) where q1/2 = eiπ/2ℓ
. If η ∈ (1, 1) is the natural monoidal transformation of
the identity functor taking value −1 on the generating object X then it follows from the
proof of Prop. 25.11 that ηθ−1 = θ1. But ηθ−1 is another ribbon structure for ε
+
−1
.
We conclude the section with a partial result concerning ribbon equivalence of examples
of slN,ℓ-type categories where pseudo-unitarity is not assumed but the ribbon structure is
fixed.
Proposition 25.15. Let q and q
′ ∈ C be either not non-trivial roots of unity or else
square to primitive roots of unity of order ℓ > N + 1 and let us endow both C(slN , q, ℓ)
and C(slN , q′, ℓ) with some braided symmetry. If there is an isomorphism of based rings
f : Gr(C(slN , q, ℓ)) → Gr(C(slN , q′, ℓ)) identifying the generating representations and
compatible with the canonical ribbon structures then there is a ribbon tensor equivalence
F : C(slN , q, ℓ) → C(slN , q′, ℓ) inducing f, q and q
′ are related as in Prop. 25.5, and we
may arrange q = q
′
.
Proof. We write the respective braided symmetries c and c
′ as in the proof of the previous
theorem, where now q and q
′ are general. We again have that the canonical ribbon structure
of C(slN , q, ℓ) takes the form θλ = q
±⟨λ,λ+2ρ⟩
. We need to be a bit more explicit on the
exponents, so we write λ =
PN−1
1 njΛj
, where Λj are the fundamental weights, nj are
non-negative integers and ρ =
PN−1
1 Λj
. Then ⟨Λk,Λj ⟩ = djdk,j , where dk,j are such that
Λk =
P
j
dk,jαj, with αj the simple roots, dj =
⟨αj ,αj ⟩
2
, hence equal to 1 in our case. This
gives ⟨λ, λ + 2ρ⟩ =
P
k,j nk(nj + 2)dk,j . The matrix (dk,j ) is given in Table 1 at pag. 69 of
[98]. In particular one obtains ⟨Λk,Λk + 2ρ⟩ =
k
N
(N − k)(N + 1), see e.g. Sect. 6 in [148],
and more generally
⟨nΛk, nΛk + 2ρ⟩ = n[⟨Λk,Λk + 2ρ⟩ + (n − 1)dk,k] =
n
N
[k(N − i)(N + 1) + (n − 1)k(N − k)] = nk
N
(N − k)(N + n).
Assuming again that θ corresponds to the plus sign, we have
θΛ1 = q
N− 1
N , θ2Λ1 = q
2N+2− 4
N
and for N > 2 we in addition consider
θΛ2 = q
2N−2− 4
N .

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 163
It follows that
θ2Λ1θ
−2
Λ1 = q
2− 2
N , θ2Λ1
θ
−1
Λ2 = q
4
.
We claim that we may assume that θ
′
corresponds to a plus sign as well, and we show it
in the same way. The first equation gives q = q
′
for N = 2. Assuming N > 2, the second
equation gives q
′ = ±q or q′ = ±iq. a) Case q′ = −q. If N is odd then q and −q give
rise to equivalent tensor categories by Prop. 25.5. We may thus assume with no loss of
generality that q = q
′
. If N is even then N2 −1 is odd and since θ
N
Λ1 = θ
′N
Λ1 we may exclude
q
′ = −q. b) We next show that the cases q′ = ±iq are not realized. We need to compute
the ribbon structure of weights which are sums of different fundamental weights, and for
this we use the following addition formula which follows from bilinearity and symmetry of
the inner product
⟨Λ1 + λ,Λ1 + λ + 2ρ⟩ = ⟨Λ1,Λ1 + 2ρ⟩ + ⟨λ, λ + 2ρ⟩ + 2⟨λ,Λ1⟩.
On the other hand, the equation θ
N
Λ1 = θ
′N
Λ1
requires N odd, we may thus consider the
weights µ = Λ N−1
2
and ν = Λ N+1
2
and since ⟨Λk,Λ1⟩ =
k
N we have
⟨µ + ν,Λ1⟩ = 1.
Applying the addition formula to µ and ν in place of λ and comparing the ribbon structure
on the weights in {Λ1, µ, ν,Λ1 + µ,Λ1 + ν} leads to q
2⟨µ,Λ1⟩ = (q′
)
2⟨µ,Λ1⟩ and q2⟨ν,Λ1⟩ =
(q
′
)
2⟨ν,Λ1⟩
, hence after term by term multiplication we get (q
′
)
2 = q
2
, contradicting q ̸= 0.
Hence in all cases we may arrange q
′ = q. The relation θΛ1 = θ′
Λ1
now implies that also
the corresponding two N-roots q
1/N and q′1/N are the same, and we thus have a ribbon
tensor equivalence F : C → C
′
inducing f. □
