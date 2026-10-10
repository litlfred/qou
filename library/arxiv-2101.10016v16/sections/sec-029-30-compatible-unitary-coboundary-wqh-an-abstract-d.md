---
doc_id: arxiv-2101.10016v16
doc_title: "Unitary coboundary weak quasi-Hopf algebras in the Kazhdan-Lusztig-Finkelberg theorem"
section_id: sec-029-30-compatible-unitary-coboundary-wqh-an-abstract-d
section_title: "Compatible unitary coboundary wqh, an abstract Drinfeld-Kohno"
section_number: 30
pages: 183-187
source_pdf: 2101.10016v16.pdf.txt
source_sha256: 51d21209730be025
toc_source: inferred
---
30. Compatible unitary coboundary wqh, an abstract Drinfeld-Kohno
We know from a theorem of Galindo [66] that a braiding of a unitary fusion category
is always unitary. Now we reverse the question and ask is there a way of constructing a
unitary braided tensor category with a unitary braiding, equivalent to a given a braided
semisimple tensor category C? In applications we may already have a linear C
∗
-category
C
+ and a linear equivalence F : C+ → C and we want to turn C+ into a unitary braided
tensor category. Furthermore, if we have two braided tensor categories C1 and C2 which
are linearly equivalent to the same C
∗
-category C
+ via Fi
: C
+ → Ci
, i = 1, 2, under what
circumstances the corresponding constructions give unitarily equivalent braided tensor
categories C1
+
and C2
+
? If this can be achieved, it will follow in particular that C1 and C2
are also equivalent as braided tensor categories. In this section we set up a specific situation
and we construct a unitary braided tensor quasi-equivalence (E, E) : C1
+ → C2
+
. In other
words we reduce the problem to verification of the equation concerning the associativity
morphisms only, that is equation (4.6), (4.7) with (E, E, E
−1
) in place of (F, F, G). In
doing this, we follow ideas of Drinfeld [47] in his work on Drinfeld-Kohno theorem, except

184 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
for as already said we forget the associativity morphisms, and again ideas of Wenzl [185]
in his work of the unitary structures of fusion categories C(g, q, ℓ) of quantum groups at
roots of unity.
In the introduction of Section 28 we have interpreted axiom d) of Definition 28.1 as a
noncommutativity property of the function algebra from a dual viewpoint. This interpretation disregards the trivial twist E, and therefore becomes more meaningful when the
trivial twist is actually trivial. This leads us to the following stronger definition.
Definition 30.1. A Hermitian coboundary weak quasi-Hopf algebra (A, ∆, Φ, R, v, w, ∗, S, α, β)
is called compatible with the ∗-involution if it satisfies one of the following equivalent conditions,
1) E = ∆(I)
∗ = ∆op(I),
2) ∆(a)
∗ = ∆op(a∗
), a ∈ A,
3) Ω = R,
4) R is selfadjoint.
Thus axiom d) of Def. 28.1 is replaced by the stronger axiom
d’) A˜ = Aop as quasitriangular weak quasi-bialgebras.
In particular we have R∗−1 = R21. Unitary, discrete, or weak Hopf versions are naturally
defined.
Example 28.5 is of this kind. In Sect. 32 we construct examples associated to fusion categories C(g, q, ℓ) associated to Uq(g) at certain roots of unity with compatible ∗
-involution.
In the rest of the paper we restrict to the unitary case.
Proposition 30.2. Let A be a discrete unitary coboundary wqh with a generating representation ρ. Then A has compatible ∗
-involution if and only if
σ ⊗ ρ(R), σ ⊗ ρ(R
−1
)
σ ⊗ ρ ⊗ ρ(I ⊗ R1 ⊗ ∆(R)), ρ ⊗ ρ ⊗ σ(R ⊗ I∆ ⊗ 1(R))
are positive for every irreducible representation σ.
Proof. Necessity is clear. We note that the associativity morphisms σ ⊗ ρ ⊗ ρ(Φ) and
ρ ⊗ ρ ⊗ σ(Φ) are unitary w.r.t. the given unitary coboundary structure, which is defined
by R on the involved subspaces. By Theorem 26.2, A becomes a unitary coboundary
wqh with compatible ∗-involution. On the other hand the original coboundary structure
Ω = ∆(I)
∗R and the new compatible coboundary structure Ω′ = R coincide of the spaces
of σ ⊗ ρ and therefore coincide everywhere by the conclusion of Theorem 26.2.
□
The following remark is an analogue of Remark 29.5 for the subclass of wqh of this
section, and takes a perhaps remarkable stronger form that seems to remind of the form
taken by the R-matrix in the specific case of Drinfeld category [47] for quasi-Hopf algebras.

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 185
Remark 30.3. Let A be a discrete Hermitian coboundary wqh with compatible ∗-involution
and let Ω by a trivial involution with respect to a tensor product representation ρ ⊗ σ.
Thus we have on the space of ρ ⊗ σ,
Ω = ∆(I)
∗∆(I) = R, R = ∆(I)
∗w ⊗ w∆(w−1
). (30.1)
When the Ω-involution is in addition strongly trivial with respect to ρ⊗σ (recall that this
is automatic when A is discrete unitary by Prop. 4.21) then in the representation space of
ρ ⊗ σ,
Ω = ∆(I) = R, R = w ⊗ w∆(w
−1
). (30.2)
In particular, if this holds for any pair of simple representations ρ, σ then A has a cocommutative coproduct (∆ = ∆(op)) by centrality of w.
Note that if T is a twist of A with left inverse T
−1
then by definition ∆(I) is the domain
of T and range of T
−1
. If A has a compatible ∗-involution then we also have that T
−1∗
21
has domain ∆op(I)
∗ = ∆(I), T21 has domain ∆op(I) = ∆(I)
∗
, T
∗ has range ∆(I)∗
.
The following result is our abstract analogue of Drinfeld-Kohno theorem.
Theorem 30.4. Let A = (A, ∆, Φ, R, v, w) be a discrete unitary coboundary weak quasiHopf algebra with compatible ∗
-involution (
∗
, Ω = R ≥ 0). Let (T, T −1
, P, Q) be a quadruple
of elements in M(A ⊗ A): such that T is a twist of A with left inverse T
−1
, P, Q are
selfadjoint projections in M(A ⊗ A) such that
P Q = 0, P + Q = I
T = (T
−1
)
∗
21, R = T
∗T−, R
−1
= T
−1
− (T
−1
)
∗
.
where
T− = (P − Q)T, T −1
− = T
−1
(P − Q).
Then
a) AT is another discrete unitary coboundary weak quasi-Hopf algebra with compatible involution, and associated quadruple (∆T (I), ∆T (I), P, Q) satisfying the same
properties with respect to the twisted structure of AT :
ΩT = ∆∗
T
(I)∆T (I)− = ∆op
T
(I)∆T (I)− = RT ≥ 0
RT = ∆op
T
(I)∆T (I)−w ⊗ w∆T (w
−1
),
where ∆T (I)− = (P − Q)∆T (I),
b) If ρ and σ are two Hilbert space ∗-representations of A such that ρ ⊗ σ(QT) = 0
and ρ ⊗ σ(T
−1Q) = 0 then
ρ ⊗ σ(T−) = ρ ⊗ σ(T), ρ ⊗ σ((T−)
−1
) = ρ ⊗ σ(T
−1
).
Moreover,
(FT )ρ,σ(FT )
∗
ρ,σ = 1, (GT )
∗
ρ,σ(GT )ρ,σ = 1, (GT )ρ,σ = (FT )
∗
ρ,σ.

186 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
Thus on the tensor product space of ρ⊗σ the twisted Hermitian form and R-matrix
are trivial ΩT = ∆T (I) = RT . It follows that
RT = w ⊗ w∆T (w
−1
), ∆T (a)
∗ = ∆T (a∗
)
on this space.
c) If the assumptions in b) hold for any pair of irreducible ∗-representations ρ, σ of A
then
T = T−, T −1 = (T−)
−1
, ∆T (I) = ∆T (I)−.
Moreover the twisted structure (FT , GT ) is strongly unitary. Thus the R-matrix
RT and the Hermitian form ΩT simplify further as in (30.2). In particular, the
coproduct ∆T of AT is cocommutative, ∆T = ∆op
T
.
Proof. a) We have T
−1
(T
−1
)
∗
21 = ∆(I), T
∗T21 = ∆(I)∗
. Let (F, G) be the weak quasi-tensor
structure defining the forgetful functor of A. Then by Theorem 29.1 equations (29.1) and
(29.2) hold for (F, G). Let (FT , GT ) be the new weak quasi-tensor structure obtained from
the twist T, FT = F T −1, GT = T G. We have
FTΣF
∗
T = F T −1Σ(T
−1
)
∗F∗ = F T −1
(T
−1
)
∗
21ΣF
∗ = F(GF)ΣF∗ = FΣF∗
and similarly
G
∗
TΣGT = G
∗T∗T21ΣG = G∗
(GF)
∗ΣG = G∗ΣG.
It follows that equations (29.1) and (29.2) hold for (FT , GT ). The twisted R-matrix RT
induces a unitary braided symmetry in Rep+(AT ) by Remark 13.3. Moreover the twisted
associator of AT is unitary Rep+(AT ) by invariance of axioms of Ω-involution under twisting. It follows from Theorem 29.1 again that AT is a unitary coboundary weak quasi-Hopf
algebra. It follows from Prop. 10.2 c) that
RT = T21RT −1 = T21T
∗
(P − Q)T T −1 = T21(T
−1
)21(P − Q)T T −1 = ∆op
T
(I)(P − Q)∆T (I).
We also have ∆T (I)
∗ = (T−1
)
∗T∗ = T21T
−1
21 = ∆op
T
(I) thus AT has a compatible ∗-
involution. This is also equivalent to RT = ΩT . The formula for RT follows from the
definition of R in (28.1) for a general Hermitian coboundary wqh. b) In this case we
have ρ ⊗ σ(T−) = ρ ⊗ σ(P T) = ρ ⊗ σ((P + Q)T) = ρ ⊗ σ(T). In a similar way,
ρ ⊗ σ(T
−1
− ) = ρ ⊗ σ(T
−1
). It follows that (FT )ρ,σ(FT )
∗
ρ,σ = Fρ,σρ ⊗ σ(T
−1
(T
−1
)
∗
)F
∗
ρ,σ =
Fρ,σρ ⊗ σ(R)
−1F∗
ρ,σ = Fρ,σGρ,σG∗ρ,σF
∗
ρ,σ = 1. One similarly shows that (GT )
∗
ρ,σ(GT )ρ,σ = 1.
The equality (GT )
∗
ρ,σ = (FT )ρ,σ follows from Prop. 4.21. Since ∆T is induced by (FT , GT )
on the tensor product space, it follows that ∆T is ∗-invariant on this space, and also that
ΩT acts trivially. c) This follows from b) and Tannaka-Krein duality.
□
We have seen that general Hermitian (unitary) coboundary wqh are Hermitian (ribbon)
if and only if the elements α, β of the antipode satisfy β = α
∗
, and that it suffices that
the antipode be of Kac type, see Theorem 28.13. We next ask when in addition we have
a (unitary) modular fusion category.

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 187
Theorem 30.5. Let A be a discrete unitary coboundary wqh algebra with compatible ∗-
involution satisfying all the assumptions in the statement and in part c) of theorem 30.4
(e.g. A has strongly trivial involution, see Def. 11.9). Let T be the twist defined in Theorem
30.4. Then T induces a canonical unitary equivalence of ribbon categories Rep+(A) →
Rep+(AT ). Moreover, if A is semisimple then Rep(A) is modular if and only if Rep(AT )
is modular. If A has antipode defined by elements α and β such that β = α
∗
(e.g. of Kac
type) then Rep+(A) is a unitary modular fusion category if and only if so is Rep+(AT ).
