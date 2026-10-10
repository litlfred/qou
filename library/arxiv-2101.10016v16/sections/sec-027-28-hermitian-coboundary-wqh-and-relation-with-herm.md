---
doc_id: arxiv-2101.10016v16
doc_title: "Unitary coboundary weak quasi-Hopf algebras in the Kazhdan-Lusztig-Finkelberg theorem"
section_id: sec-027-28-hermitian-coboundary-wqh-and-relation-with-herm
section_title: "Hermitian coboundary wqh and relation with Hermitian ribbon wqh"
section_number: 28
pages: 173-180
source_pdf: 2101.10016v16.pdf.txt
source_sha256: 51d21209730be025
toc_source: inferred
---
28. Hermitian coboundary wqh and relation with Hermitian ribbon wqh
In this section we introduce the notion of Hermitian coboundary weak quasi-Hopf algebra.
Essentially, we understand these as as ribbon weak quasi-Hopf algebras endowed with a
∗
-algebra structure satisfying various compatibility relations between the ∗-involution, the
coproduct and ribbon structure. We are mainly interested in the case of discrete algebras
with a pre-C
∗
-algebra structure.
The most relevant structural aspect of our definition is the relation between coproduct
and ∗-involution. Informally, this relation may be interpreted as an antimultiplicativity
property of the involution on the ‘dual noncommutative function algebra’, that is (AB)
∗ =
B∗A∗. When we take the adjoint on both sides, we get an equation that dually identifies the
opposite coproduct ∆op and the adjoint coproduct ∆. To be more precise, we require that ˜
∆op and ∆ (together with all the remaining structural data) are related by a trivial twist. ˜
Moreover, since we have an R-matrix which relates ∆op and ∆, we may interpret that
noncommutativity arises explicitly from the R-matrix as is familiar in quantum group
theory. This property makes these algebras rather different from the ordinary Hopf ∗-
algebras, where coproduct and ∗-involution commute.
Among other axioms we assume a relation involving directly the unitary structure with
the braiding, or more precisely with the coboundary symmetry in the representation category. We assume the existence of a square root of the ribbon structure. Thus we have an
associated coboundary in the representation category in the sense of Sect. 27. It follows
from the axioms that there is an Ω-involution on the algebra in the sense of Sect. 11
associated to the braiding data. When the Ω-involution of an Hermitian coboundary weak
quasi-Hopf algebra it is unitary, we shall talk of a unitary coboundary weak quasi-Hopf
algebra.

174 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
In this section we study the main properties. For example, among general Ω-involutions,
those associated to a coboundary always make the braiding unitary, see Theorem 28.9.
Moreover, we shall give a characterization of the case where an Hermitian coboundary
weak quasi-Hopf algebra gives rise to an Hermitian ribbon category, Theorem 28.13.
The main result of this section is a Tannakian characterization of Hermitian coboundary weak quasi-Hopf algebras, see Theorem 29.1. This characterization describes such
algebras as categories endowed with a faithful functor to Herm with a weak quasi-tensor
structure (F, G) and compatibility equations between the coboundary of the category, the
permutation symmetry of Herm and (F, G). The simplest case is that of symmetric tensor
categories, and the Tannakian characterization becomes the notion of symmetric tensor
functor. In particular compact groups is a natural class of examples, and we are in the
setting of the Doplicher-Roberts duality theorem [41]. More generally, the permutation
symmetry is replaced by the coboundary of Drinfeld in the sense of Sect. 27.
In the next section we discuss a possibly proper subclass of Hermitian coboundary weak
quasi-Hopf algebras and we shall develop a criterion to construct such algebras.
We shall show in the next section that the unitarization of a unitary coboundary weak
quasi-Hopf algebra in this subclass, is again an algebra of this kind with the advantage that
both the unitary structure and the R-matrix take a simpler form, see Remark 29.5 completely determined by the square root of the ribbon structure. It reminds the form taken
by Drinfeld R-matrix of the quasi-Hopf algebra associated to Knizhnik-Zamolodchikov
differential equations in [47]. It seems valuable to us that this simple R-matrix may be
derived in a general setting by the study of unitary structures of ribbon weak quasi-Hopf
algebras. We hope to further develop this study in future updates of this paper
Our interest in discrete algebras is motivated by the unitary structure of the fusion
categories C(g, q, ℓ) associated to Uq(g) at certain roots of unity. Kirillov defined a tensor
∗
-category tensor equivalent to C(g, q, ℓ) and conjectured that these where unitary. The
conjecture was shown to be true by Wenzl and Xu [111], [185], [194]. We may regard
our notion as an abstract version of Kirillov ∗-structure following the approach of Wenzl
in [185]. We shall recall these results in Sect. 32 and we recall in particular that the
main example of Hermitian coboundary weak quasi-Hopf algebra is Uq(g) itself for |q| = 1,
although not a semisimple example at roots of unity.
Furthermore in Sect. 32 we shall construct f.d. unitary coboundary weak Hopf algebras
as suitable quotients of Uq(g) with representation category equivalent to C(g, q, ℓ).
Recall that for a general weak quasi-bialgebra A we have defined a twisted algebra AF ,
see Prop. 6.9, the opposite algebra Aop, see (10.1) and furthermore, if A is also a ∗-
algebra, we have introduced the adjoint algebra A˜ in (10.8). Note that AF , Aop, and A˜
have quasitriangular structures naturally induced by one of A, see Prop. 10.2. Moreover,
Aop and A˜ have a strong antipode if so does A, and similarly for AF if (6.14) holds. In
particular, Aop and A˜ are weak bialgebras if so is A, and similarly for AF if F is a 2-cocycle.
Definition 28.1. A Hermitian coboundary weak quasi-Hopf algebra A is defined by the
following data:

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 175
a) A weak quasi-Hopf algebra A endowed with a ∗-algebra involution with an antipode
(S, α, β)
b) a ribbon structure (R, v) for A associated to (S, α, β) (see Def. 10.5) such that the
ribbon element v ∈ A is unitary,
c) a unitary central square root w ∈ A of v such that ε(w) = 1, S(w) = w,
d) A˜ = (Aop)E as quasitriangular weak quasi-bialgebras, where E = ∆(I)
∗∆op(I) is a
trivial twist, that is E
−1 = ∆op(I)∆(I)∗
.
Remark 28.2. Our axioms are motivated by the structure of Uq(g) for |q| = 1 that will
be important to us, and we shall recalled it in Sect. 32, Theorem 31.9. Notice however
that, since the R-matrix and ribbon structure lie in a suitable topological completion of
Uq(g) ⊗ Uq(g) [161], this algebra can not be included as an example, unless we weaken our
axioms. However we shall refrain from doing this. To deal with examples where the ribbon
structure lies in a larger algebra, we shall content to consider the case of discrete algebras.
Definition 28.3. A discrete Hermitian coboundary weak quasi-Hopf algebra is defined by
a discrete weak quasi-Hopf algebra A endowed with data (∗, R, v, w) such that axioms a)-d)
hold as before for discrete algebras, that is the ∗-involution makes A into a pre-C
∗
-algebra,
and the ribbon and coboundary structure satisfies R ∈ M(A ⊗ A), v, w ∈ M(A).
A (discrete) weak Hopf algebra A satisfying axioms a)–d) will be called a (discrete)
Hermitian coboundary weak Hopf algebra.
Remark 28.4. a) Note that the definitions do not depend on the choice of the antipode
by Prop. 6.10. Furthermore, when A is discrete an antipode may always be chosen
commuting with ∗ by Remark 14.6. In the rest of the section antipodes (S, α, β) will be
chosen with S commuting with ∗for discrete algebras. These antipodes are of the form
xS( )x
−1
, xα, βx−1) with x unitary and uniquely determined. b) The equality required in
d) between the R-matrices of A˜ and (Aop)E amounts to R∗−1 = E21R21E
−1
.
We discuss a simple example.
Example 28.5. Let G be a compact group and C∞(G) the Hopf ∗-algebra of functions on
G which are finite linear combinations of matrix coefficients of unitary finite dimensional
representations u of G. The coproduct and antipode are defined as usual by ∆(f)(g, h) =
f(gh) and S(f)(g) = f(g
−1
). Then the dual ∗-algebra is isomorphic to Πu∈IrrGB(Hu), with
Hu the Hilbert space of u. The algebraic direct sum A =
L
u∈IrrG B(Hu) is a discrete Hopf
∗
-algebra with dual coproduct ∆ and antipode ˆ Sˆ. We have A = Aop by commutativity of
C∞(G), and it follows that with the trivial R-matrix and ribbon structure, A is a discrete
unitary coboundary Hopf algebra.
The example gives a natural interpretation of axiom d) when A is thought of as the dual
of the algebra of functions on a noncommutative space.
Remark 28.6. The relationship between the multiplier discrete algebra associated to the
forgetful functor of Rep(Uq(g)) and Uq(g) has been considered in detail by Neshveyev and
Tuset in Sect. 2 in [141] for q > 0, and it beautifully gives a connection between two

176 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
different approaches to quantum groups by Woronowicz and Drinfeld. Quite remarkably
to us, the relevance of an analogous tannakian approach for a topological description of
Uq(g) has been explained by Sawin in Sect. 1 in [161] motivated by the construction of the
R-matrix.
The following proposition gives a characterization of the Kac-type property for an antipode, see Def. 11.19.
Proposition 28.7. Let A be a weak Hopf algebra with a ∗-involution making it into a
∗
-algebra, strong antipode S such that ∆op(a)
∗ = ∆op(I)∗∆(a∗
)∆op(I)
∗
for all a ∈ A.
Then S commutes with ∗(thus is of Kac type) if and only if P
i
aiS(b
∗
i
)
∗ = I, where
∆(I) = P
i
ai ⊗ bi. This is always the case when ∆op(I)
∗ = ∆(I), that is when A is a
Hermitian coboundary weak Hopf algebra with compatible ∗-involution in the sense of Sect.
30.
Proof. The necessity of the condition follows from the antipode axiom (6.7). For the sufficiency, note that, if S is a strong antipode then (S, 1, 1) satisfies (6.7) and by Prop. 9.5
and its proof this equation suffices to make a triple (S, 1, 1) into an antipode, with S an
antiautomorphism. Starting with our assumptions, we may slightly modify the computations in the proof of Prop. 11.20 and show that (S, ˜ 1, 1) satisfies (6.7), with S˜(a) = S(a
∗
)
∗
,
thus this is another strong antipode, and the proof is completed by uniqueness of a strong
antipode.
□
Given any central invertible element z ∈ A with ε(z) = 1 we set
Θz := z
−1 ⊗ z−1∆(z), Rz := RΘz.
(Note that when A is a weak bialgebra, E is necessarily a 2-cocycle of Aop by Prop. 9.13.
Similarly, Θz and Rz are 2-cocycles by Prop. 9.17.) We have AΘz = A as quasitriangular
weak quasi bialgebras thanks to centrality of z and since the twisting operation can be
performed in stages, (AF )G = AGF , we see that R and Rz twist A in the same way.
Therefore
ARz = AR = A
op
.
Furthermore the deformed R-matrix yields a generalised coboundary on Rep(A) via Σρ ⊗
σ(Rz). We set
R = RΘw. (28.1)
The element R first introduced by Drinfeld in his work on quasi-Hopf algebras [47], is the
algebraic analogue of the coboundary symmetry considered in Sect. 27.
Proposition 28.8. The twist R satisfies R21R = ∆(I). Therefore Σρ⊗σ(R) ∈ (ρ⊗σ, σ⊗ρ)
is a coboundary of Rep(A).
Proof. We have
R21R = R21w
−1 ⊗ w−1∆op(w)Rw−1 ⊗ w−1∆(w) =
R21Rw−2 ⊗ w
−2∆(w2
) = R21Rv−1 ⊗ v
−1∆(v) = ∆(I).

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 177
□
By axiom d), the element E is required to be a trivial twist from Aop to A˜. It follows
that A˜ = (Aop)E = (AR)E = AER, hence
A˜ = AΩ, Ω = ER (28.2)
as quasitriangular weak quasi-bialgebras.
Theorem 28.9. Let A be a (discrete) Hermitian coboundary weak quasi-Hopf algebra.
Then A is Ω-involutive with Ω = ER = ERΘw. Furthermore the induced braided symmetry
Σρ ⊗ σ(R) ∈ (ρ⊗σ, σ⊗ρ), and therefore coboundary symmetry Σρ ⊗ σ(R) ∈ (ρ⊗σ, σ⊗ρ)
are unitary in Reph(A).
Proof. We need to show that Ω is selfadjoint. By construction, ∆(I) and ∆(I)
∗ are respectively domain and range of Ω. The R-matrices of A˜ and Aop are respectively given by
R˜ = R∗−1and Rop = R21 thanks to Prop. 10.2. Equality between the R-matrices of A˜
and (Aop)E gives R∗−1 = E21R21E
−1
, hence R∗ = ER−1
21 E
−1
21 . We may write Ω in the form
Ω = ERΘw = ERw−1 ⊗ w
−1∆(w) = (28.3)
Ew−1 ⊗ w
−1∆op(w)R = w−1 ⊗ w−1E∆op(w)R = (28.4)
w
−1 ⊗ w−1∆( ˜ w)ER. (28.5)
We also have
E
−1
21 E
∗ = (E−1
)21E
∗ = (∆op(I)∆(I)∗
)21∆
op(I)∗∆(I) = ∆(I).
Hence
Ω
∗ = R∗E∗∆(w−1
)w ⊗ w = (28.6)
ER−1
21 E
−1
21 E
∗∆(w−1
)w ⊗ w = ER−1
21 ∆(w
−1
)w ⊗ w = (28.7)
ER(R21R)
−1∆(w−1
)w ⊗ w = ER∆(w)w
−1 ⊗ w−1 = (28.8)
ERΘw = Ω. (28.9)
Unitarity of the braided symmetry follows from the property that A˜ = AΩ as quasitriangular weak quasi-bialgebras and Prop. 13.2. □
In the rest of this section we endow A with the Ω-involution Ω = ER. Note that the
Hermitian form on the tensor product of two representations associated to Ω is given by
(ζ, ζ′)Ω = (ζ, Rζ′). (28.10)
Remark 28.10. We may interpret the trivial twist E as follows. It is non-trivial precisely
when R is not selfadjoint. This follows from the equation Ω = Ω∗. The subclass of
Hermitian coboundary wqh for which R is already selfadjoint will be considered more
closely in the next section.

178 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
We discuss how to construct examples of Hermitian coboundary weak quasi-Hopf algebras with strongly trivial Ω-involution in the sense of Defn. 11.9. The following example
reduces the problem to the construction of Hermitian coboundary weak quasi-Hopf algebras with trivial Ω-involution. The step of constructing a unitary coboundary with trivial
Ω-involution will be considered in the next section.
Proposition 28.11. Let A be a Hermitian coboundary weak quasi-Hopf algebra with trivial
involution Ω = ∆(I)
∗∆(I), Ω−1 = ∆(I)∆(I)∗
. Then the twist T (or T
′
) defined in Remark
11.10 making the Ω-involution strongly trivial turns A into another Hermitian coboundary
weak quasi-Hopf algebra AT .
Proof. Notice that axioms a)–c) are invariant under any twist. For axiom d), we have
that T
∗T21 = E, and it easily follows that the twist ET = ∆T (I)∗∆
op
T
(I) has inverse
E
−1
T = ∆op
T
(I)∆T (I)
∗
. Moreover AfT = (A˜)T −1∗ and (AT )
op = (Aop)T21 , it follows that
axiom d) for AT is equivalent to A˜ = (Aop)T ∗ET T21 . We have T
∗ET T21 = E, thus axiom d)
holds for AT also. □
Definition 28.12. Let A be a (discrete), Hermitian coboundary weak quasi-Hopf (weak
Hopf) algebra. If Ω = ERΘw is positive in A ⊗ A (M(A ⊗ A)) then A will be called a
unitary (discrete), coboundary weak quasi-Hopf (weak Hopf) algebra.
Recall [158, 174] that an Hermitian (unitary) ribbon category is a *-category (C
∗
-
category) C equipped with a right duality (ρ
∨
, bρ, dρ), unitary braided symmetry ε(ρ, σ)
and unitary ribbon structure v ∈ (1, 1) such that
b
∗
ρ = dρ ◦ ε(ρ, ρ∨
) ◦ v
−1
ρ ⊗ 1ρ∨ d
∗
ρ = 1ρ∨ ⊗ vρ ◦ ε(ρ
∨
, ρ)
−1
◦ bρ. (28.11)
It follows from (27.15) that the quantum dimension in a Hermitian ribbon category may
be computed as
d(ρ) = dρd
∗
ρ = b
∗
ρ
bρ.
Theorem 28.13. Let A be a Hermitian (unitary) coboundary weak quasi-Hopf algebra
with an antipode (S, α, β) such that S commutes with ∗. Then Reph(A) (Rep+(A)) is a
Hermitian (unitary) ribbon category with the canonical duality (ρ
∨ = ρc, bρ, dρ) associated
to A as in Example 14.7 if and only if β = α
∗
. This equation holds if A is discrete and
admits an antipode of Kac type.
Proof. We need to give a right duality (ρ
∨
, bρ, dρ) satisfying (28.11). We show that this
holds for the canonical duality (ρ
∨ = ρc, bρ, dρ) associated to A as in Example 14.7 and a
fixed antipode (S, α, β) such that S commutes with ∗. We only verify the equation on the
right in (28.11). We have
d
∗
ρ = rρ = Ω−1Xµiei ⊗ α
∗
ei, bρ =
X
i
βei ⊗ µiei,
with ei an orthonormal basis. A computation gives for a, b ∈ A,
a ⊗ b
Xµiei ⊗ α
∗
ei =
Xµiei ⊗ bα∗S(a)ei
.

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 179
Taking into account S(w) = w, ε(w) = 1, and the antipode property (6.7), it follows that
∆(w)
∗w ⊗ w
Xµiei ⊗ α
∗
ei =
Xµiei ⊗ α
∗
vei.
On the other hand, Ω−1 = R−1∆(w)
∗w ⊗ w. It follows that
d
∗
ρ = Ω−1Xµiei ⊗ α
∗
ei = 1 ⊗ vρR
−1Xµiei ⊗ α∗
ei =
1 ⊗ vρ ◦ ε(ρ
∨
, ρ)
−1
◦
Xα
∗
ei ⊗ µiei.
Thus the equation on the right in (28.11) holds if and only if β = α
∗
. □
We next identify the element ω defined in Prop. 11.16 with the element associated to the
spherical structure on Rep(A), as in Theorem 27.18, see also Cor. 10.11, in the important
special case of antipode of Kac type, see Def. 11.19.
Proposition 28.14. Let A be an Hermitian coboundary weak quasi-Hopf algebra with
antipode S of Kac type. Then ω = uv−1 where u is Drinfeld element associated to S
introduced in Definition 10.6.
Proof. Since A has a strong antipode S, ω = m ◦ S ⊗ 1(Ω−1) by (11.9). With the same
notation as in Def. 10.6, we have Ω−1 = R−1∆(w)
∗w⊗w =
P
j
rjw
∗
1w⊗tjw
∗
2w. Recall from
Prop. 10.7 that S
2
is the inner automorphism induced by u and that u
−1 =
P
j S
−1
(tj )rj
.
It follows that ω =
P
j S(rjw
∗
1w)tjw
∗
2w = S(S
−1
(tjw
∗
2w)rjw
∗
1w) = S(S
−1
(w
∗
2w)u
−1w∗
1w) =
S(u
−1S(w∗
2w)w
∗
1w) = S(u
−1
v), for the last equality we have used axiom c) of Def. 28.1.
On the other hand, S(u
−1
v) = uv−1 by Remark 10.10.
□
Let A be an Hermitian coboundary weak quasi-Hopf algebra. Replacing the choice of w
with another square root w
′ of v satisfying the properties in c) of Def. 28.1 gives rise to
another Hermitian coboundary weak quasi-Hopf algebra with the same the same structure
as A and new square root of the ribbon element given by w
′
, and correspondingly a new
Ωw′, and therefore a new tensor ∗-category, denoted Rep′
h
(A). We may write w
′ = wy
with y a (unitary) central square root y of I in M(A) satisfying c), that is ε(y) = 1 and
S(y) = y. Conversely, any y ∈ M(A) with these properties arises in this way. The new
Ωw′ differs from Θw by the 2-coboundary Θy = y
−1 ⊗ y−1∆(y), that is
Ωw′ = ΩwΘy.
In particular, Ωw′ = Ωw if and only if y is a 1-cocycle: ∆(y) = y ⊗ y∆(I).
Proposition 28.15. Assume that A is discrete.
a) The functor F : Reph(A) → Rep′
h
(A) acting identically on objects and morphisms
with identity natural transformation Fρ,σ is a tensor ∗-functor and an equivalence.
There is no unitary tensor ∗-functor between these categories unless y = w
′w−1
is
a 1-cocycle.
b) If A is a unitary coboundary weak quasi-Hopf algebra with respect to w and Ωw′ is
positive with respect to some other w
′
satisfying c) in Def. 28.1 then Ωw = Ωw′ and
Rw = Rw′.

180 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
Proof. a) The categories Reph(A) and Rep′
h
(A) have the same tensor structure and the
same ∗-category structure, and the functor F becomes the identity functor for these substructures, thus it is a tensor ∗
-functor and an equivalence when the natural transformation
Fρ,σ : F(ρ) ⊗′ F(σ) → F(ρ ⊗ σ) acts as identity. Here we have used different symbols to
denote the two different tensor products. The Hermitian form of F(ρ) ⊗′ F(σ) differs from
that of F(ρ⊗σ) by the action of Θy. On the other hand y acts as ερ, where ερ = ±1 on an
irreducible representation ρ, and all the ερ determine y. In particular, Θy at most changes
the sign of the Hermitian form of an irreducible component of F(ρ⊗σ), and if this happens
then F(ρ) ⊗′ F(σ) and F(ρ ⊗ σ) are not unitarily equivalent, by Prop. 12.10. Hence all
Fρ,σ are unitary if and only if Θy = ∆(I). b) If two choices w and w
′ both define positive
operators Ωw and Ωw′ then F : Rep+(A) → Rep+′(A) is a tensor ∗-equivalence between
tensor C
∗
-categories hence by Prop. 4.22 c) polar decomposition of the tensor structure
gives a unitary tensor equivalence. It follows from the previous part that y = w
′w∗
is a
1-cocycle, hence Ωw = Ωw′ and also Rw = Rw′.
□
We next construct an involutive antipode for all the twists of a unitary ribbon weak
quasi-Hopf algebra of Kac type under a spectrum condition.
Proposition 28.16. Let A be a unitary coboundary weak quasi-Hopf algebra. If A has an
antipode of Kac type S with associated unitary Drinfeld element u such that −1 ∈/ Sp(uv−1)
then for any twist F of A, AF endowed with twisted involution (
∗
, ΩF ) admits an antipode
(S, ˜ α, ˜ β˜) such that S˜ commutes with ∗ and the corresponding element as in Prop. 11.16 is
ω˜ = 1. In particular, S˜2 = 1.
Proof. The element ω corresponding to S and A is given by ω = uv−1 by Prop. 28.14, which
is unitary. Let (S, α, β) be the twisted antipode of AF as in (6.11), so ωF = ω by Prop.
11.18 b). For an invertible x, the antipode (Ad(x)S, xα, βx−1) of AF has associated element
ω˜ = xωS−1(x)
∗ by Prop. 11.18 a). We set x−1 = ω1/2
, the continuous functional calculus
of the principal branch of the square root function, so x is unitary. Since S(ω) = ω
−1
it
follows that S(x) = x
−1 and therefore ˜ω = 1. □
We shall see that the weak quasi-Hopf algebras arising from VOAs as satisfying the
rationality assumptions of Sect. 22 have a natural involutive antipode commuting with ∗.
