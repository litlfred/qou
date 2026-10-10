---
doc_id: arxiv-2101.10016v16
doc_title: "Unitary coboundary weak quasi-Hopf algebras in the Kazhdan-Lusztig-Finkelberg theorem"
section_id: sec-005-6-weak-quasi-hopf-algebras
section_title: "Weak quasi-Hopf algebras"
section_number: 6
pages: 36-43
source_pdf: 2101.10016v16.pdf.txt
source_sha256: 51d21209730be025
toc_source: inferred
---
6. Weak quasi-Hopf algebras
In [47] Drinfeld introduced the notion of quasi-Hopf algebra as an extension of that of
Hopf algebra to the case where the coproduct is not coassociative. Quasi-Hopf algebras
are more flexible than Hopf algebras in that they admit a so called twist operation.
Quasi-Hopf algebras play an important role in the proof of the Drinfeld-Kohno theorem
on the connection between conformal field theory and quantum groups [47], see also [139].
However, quasi-Hopf algebras are not sufficiently general to describe fusion categories from
CFT. This follows from Frobenius-Perron theorem, according to which a fusion category C
admits a unique positive dimension function, it is the Frobenius-Perron dimension function,
ρ ∈ Irr(C) → FPdim(ρ), see Sect. 5 in [50], see also Sect. 16, 25. This implies that C is
tensor equivalent to Rep(A) for a quasi-Hopf algebra A if and only if FPdim takes values
in N, in this case A is unique up to twist deformation. However the integrality condition
is not satisfied already for the fusion category associated the Ising model, which may be
realised by an affine vertex operator algebra over sl2 at level 2 [125].

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 37
In the early 90s Mack and Schomerus [125] suggested to give up the request that the
coproduct is unital. This leads to the notion of weak quasi-Hopf algebra, that is the main
subject of this section and plays a central role in this paper. As we shall see, Drinfeld
notion of twist deformation extends in a natural way to weak quasi-Hopf algebras.
Definition 6.1. Let B be an algebra, and consider the linear category with objects idempotents of B and morphism spaces between two idempotents p, q ∈ B defined by
(p, q) := qBp = {T ∈ B : qT = T = T p}.
Given an element T ∈ (p, q), we shall refer to D(T) := p and R(T) := q as the domain
and range of T. We shall call T partially invertible if it is invertible as a morphism of that
category. In other words, if there is an element T
−1 ∈ (q, p) satisfying
T
−1T = p, T T −1 = q. (6.1)
Clearly T
−1
is unique in (q, p). We shall refer to T
−1 as the partial inverse, or simply the
inverse of T.
In most of our applications, p is given. Assume that we have T and T
−1
such that T
−1
is a partial left inverse of T in the sense of the first equation (6.1), then we have a unique
range q = T T −1such that T is partially invertible.
Definition 6.2. A weak quasi-bialgebra A is defined by the following data
a) algebra: a complex, associative algebra A with unit I,
b) coproduct: a possibly non-unital homomorphism ∆ : A → A ⊗ A
c) counit: a homomorphism ε : A → C satisfying
(ε ⊗ 1) ◦ ∆ = 1 = (1 ⊗ ε) ◦ ∆, (6.2)
d) associator: a partially invertible element Φ ∈ A ⊗ A ⊗ A with
D(Φ) = ∆ ⊗ 1(∆(I)), R(Φ) = 1 ⊗ ∆(∆(I)), (6.3)
Φ∆ ⊗ 1(∆(a)) = 1 ⊗ ∆(∆(a))Φ, a ∈ A, (6.4)
(1 ⊗ 1 ⊗ ∆(Φ))(∆ ⊗ 1 ⊗ 1(Φ)) = (I ⊗ Φ)(1 ⊗ ∆ ⊗ 1(Φ))(Φ ⊗ I), (6.5)
1 ⊗ ε ⊗ 1(Φ) = ∆(I). (6.6)
The relations ε ⊗ 1 ⊗ 1(Φ) = ∆(I) = 1 ⊗ 1 ⊗ ε(Φ) hold automatically, a result extending
a known result for quasi-bialgebras algebras. For example, the first follows from the fact
that the domain and range of ε ⊗ 1 ⊗ 1(Φ) is ∆(I), and then as in the quasi-bialgebra case
[47], one evaluates ε ⊗ ε ⊗ 1 ⊗ 1 on (6.5) and takes into account properties (6.2), (6.3),
(6.6). Equation (6.5) is called pentagon equation in the setting of weak quasi-bialgebras,
and plays an important role in connection with construction of tensor categories.
We shall find it useful to introduce a weaker terminology.
Definition 6.3. If we have a quadruple (A, ∆, ε, Φ) such that (A, ∆, ε) satisfies axioms
a), b), c) and Φ ∈ A ⊗ A ⊗ A satisfies (6.3), (6.6) then Φ is called a pre-associator.

38 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
We shall see that the notion of pre-associator is useful as in many interesting cases coming
from categories from CFT, where a pre-associator can be introduced using only data of
the coproduct. If we disregard Φ we shall see that Rep(A) is a pre-tensor category. But if
one can show that Φ satisfies the remaining axioms of an associator (partial invertibility,
the intertwining relation (6.4) and the pentagon equation (6.5)) then (A, ∆, ε, Φ) is a weak
quasi-bialgebra and Rep(A) is a tensor category that by construction depends up to tensor
equivalence only on (A, ∆, ε). We shall develop this in Sect. 7 and we see an application
in Sect. 33, 34, 21.
Definition 6.4. A weak quasi-Hopf algebra is a weak quasi-bialgebra with an antipode: an
antiautomorphism S of A together with elements α, β ∈ A for which
S(a(1))αa(2) = ε(a)α, a(1)βS(a(2)) = ε(a)β, a ∈ A (6.7)
xβS(y)αz = I = S(x
′
)αy′βS(z
′
), (6.8)
where m : A ⊗ A → A is the multiplication map and we use the notation Φ = x ⊗ y ⊗ z,
Φ
−1 = x′ ⊗ y′ ⊗ z′
.
If ∆ is unital, the definition of weak quasi-Hopf algebra reduces to that of quasi-Hopf
algebra introduced by Drinfeld in [47]. The following example provides the simplest family
of quasi-Hopf algebras.
Example 6.5. Let G be a finite group. The algebra Funω(G) of complex valued functions on G is a commutative quasi-bialgebra with coproduct ∆(f)(g, h) = f(gh), counit
ε(f) = f(e), associator given by a normalized 3-cocycle ω : G3 → T. If ω is trivial we recover the usual Hopf algebra Fun(G). If ω is a 3-cocycle and ωF (g, h, k) =
F(h, k)F(g, hk)ω(g, h, k)F
−1
(gh, k)F
−1
(g, h) is a cohomologous 3-cocycle via a normalized 2-cochain F then FunωF
(G) = (Fun(G)ω)F . It follows that the twist isomorphism
class of Funω(G) is determined by the class of ω in H3(G, T). An antipode is given by
S(f)(g) = f(g
−1
), α(g) = ω(g, g−1, g)
−1
, β(g) = 1. (Note that the 3-cocycle relation for
ω yields the equality ω(g, g−1, g) = ω(g
−1
, g, g−1)
−1
, which is useful to verify the antipode
axioms.)
Definition 6.6. An antipode (S, α, β) will be called strong if α = β = I.
Remark 6.7. An antiautomorphism S of A can be a strong antipode only if it satisfies
the following compatibility conditions with the associator,
xS(y)z = I, S(x
′
)y
′S(z′
) = I. (6.9)
For example, when A is a bialgebra, that is Φ = I ⊗ I ⊗ I, then the above equations
obviously hold and the notion of a strong antipode reduces to the usual notion of antipode
of a Hopf algebra. More generally, in the weak case we shall see that equations (6.9) are
satisfied by the associator of a weak Hopf algebra, see Sect. 9.
Definition 6.8. Let A be a weak quasi-bialgebra with coproduct ∆ and counit ε.
a) A twist is a pair of elements T, T −1 ∈ A ⊗ A such that T
−1
is a partial left inverse
of T, that is T
−1T = ∆(I) and such that ε ⊗ 1(T) = 1 ⊗ ε(T) = I.

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 39
b) A trivial twist of A is a twist of the form E = P ∆(I) where P ∈ A ⊗ A is an
idempotent, E
−1 = ∆(I)P, EE−1 = P.
If P is a trivial twist then P = ∆P (I). In particular, in the framework of quasi-bialgebras
the only trivial twist is the identity, and this motivates our terminology. Trivial twists may
informally be thought as the necessary adjustment between two weak bialgebra structures
that that would be coinciding except for the value the coproducts take on the identity.
Trivial twists will arise in the study of unitary structures in Sect. 10 and unitary ribbon
structures in Sect. 28, 30, 32.
Proposition 6.9. A twist T of a weak quasi bialgebra A gives rise to another weak quasibialgebra, denoted AT , with the same algebra structure and counit as A but coproduct and
associator given by
∆T (a) = T ∆(a)T
−1
ΦT = I ⊗ T1 ⊗ ∆(T)Φ∆ ⊗ 1(T
−1
)T
−1 ⊗ I. (6.10)
If A has antipode (S, α, β), then AT has antipode (S, αT , βT ) where
αT = S(f
′
)αg′, βT = fβS(g), (6.11)
and T = f ⊗ g, T
−1 = f′ ⊗ g′
.
Proof. Verification of the axioms can be done as in the unital case, [105], with slight
modifications due to non triviality of domain idempotents. □
In the last part of the section we extend to weak quasi-Hopf algebras properties of
antipodes of quasi-Hopf algebras [47].
Proposition 6.10. Let A be a weak quasi-Hopf algebra with antipode (S, α, β). Then for
every invertible u ∈ A, the triple (S, α, β) defined by
S(a) = uS(a)u
−1
, (6.12)
α = uα, β = βu−1(6.13)
is another antipode of A. Conversely, any antipode is of this form with u ∈ A uniquely
determined by (6.12) and one of the equations in (6.13).
Proof. From (6.5) it follows that
(1 ⊗ 1 ⊗ ∆(Φ))(∆ ⊗ 1 ⊗ 1(Φ))(Φ−1 ⊗ I) =
(I ⊗ Φ)(1 ⊗ ∆ ⊗ 1(Φ))((1 ⊗ ∆(∆(I))) ⊗ I) = (I ⊗ Φ)(1 ⊗ ∆ ⊗ 1(Φ)).
We may extend the proof of the quasi-Hopf case, i.e. Prop. 1.1 of [47], to the weak
case. □
Notice that u and u
−1
can be derived from (6.13) if one of the antipodes is strong.
Corollary 6.11. Let A be a weak quasi-Hopf algebra and (S, α, β) an antipode. Then
a) A admits a strong antipode if and only if α and β are invertible and β = α
−1
. In
particular a strong antipode is unique and given by ad(α
−1
)S.

40 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
b) If A admits a strong antipode S then the same holds for a twisted algebra AT if and
only if
m ◦ S ⊗ 1(T
−1
) = (m ◦ 1 ⊗ S(T))−1. (6.14)
Proof. The proof follows from (6.11) and Prop. 6.10. □
By [47], p. 1424, when Φ = I, thus A is a bialgebra, and (S, α, β) is an antipode then
β = α
−1
, thus we may always assume that the antipode is strong. We shall see that this
property extends to any weak bialgebra with an antipode of a weak quasi-Hopf algebra,
see Prop. 9.5. We illustrate these notions for the quasi-Hopf algebras defined in Example
6.5.
Example 6.12. It follows from Cor. 6.11 that A = Funω(G) has a strong antipode if and
only if ω(g, g−1, g) = 1 for all g. For example, when G = ZN , each complex N-th root
of unity w induces the 3-cocycle ωw(a, b, c) = w
γ(a,b)c
, with γ(a, b) = ⌊
a+b
N
⌋ − ⌊ a
N
⌋ − ⌊ b
N
⌋,
where ⌊λ⌋ is the greatest integer not exceeding λ. Furthermore this association gives an
isomorphism of the group of N-th roots of unity with H3(ZN , T). If h is the natural
generator of ZN , ω(h, h−1, h) = w. It follows that Funωw
(ZN ) ∈ H if and only if w = 1.
Quite interestingly, elements of Funω(G) ∈ H′can be twisted to elements of H which
are not Hopf algebras, but this can happen only if a certain obstruction of the associator
vanishes. More in detail, F is a twist such that (Funω(G))F ∈ H if and only if βF = α
−1
F
which amounts to solve the equation
F(g
−1
, g)ω(g, g−1, g) = F(g, g−1) (6.15)
When there are elements g ∈ G with g
2 = e and such that ω(g, g, g) ̸= 1 then clearly the
equation has no solution. For example, for G = Z2, ω−1(h, h, h) = −1. Note that this is a
general property, λg := ω(g, g, g) = ±1 when g
2 = e, and it is not difficult to see that the
property that λ take the value −1 on some involutive element g is the only obstruction to
solve equation (6.15) for a normalized twist F. For example the obstruction vanishes if G
has odd order. We shall come back to 3-cocycles on ZN in Sect. 25, cf. (25.1).
Drinfeld showed that the antipode of a quasi-Hopf algebra satisfies a twisted anticomultiplicativity property with the coproduct which extends the usual (i.e. untwisted)
anticomultiplicativity in the framework of Hopf algebras. We in turn extend this to weak
quasi-Hopf algebras. Since our arguments are a straightforward generalisation of [47], we
shall only briefly sketch the needed modifications. Set
γ = V ((I ⊗ Φ
−1
)(1 ⊗ 1 ⊗ ∆(Φ))), δ = V
′
((∆ ⊗ 1 ⊗ 1(Φ))(Φ−1 ⊗ I)) (6.16)
where V, V ′: A⊗4 → A⊗2 are defined by V (a ⊗ b ⊗ c ⊗ d) = S(b)αc ⊗ S(a)αd and
V
′
(a ⊗ b ⊗ c ⊗ d) = aβS(d) ⊗ bβS(c).
Proposition 6.13. Let A be a weak quasi-Hopf algebra. Then the new weak quasi-Hopf
algebra with same algebra structure and counit but coproduct S⊗S◦∆op◦S
−1 and associator
S ⊗ S ⊗ S(Φ321) is a twist of A by a unique partially invertible element f ∈ A ⊗ A such
that
γ = f · ∆(α), δ = ∆(β) · f
−1
. (6.17)

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 41
Explicitly, D(f) = ∆(I), R(f) = S ⊗ S ◦ ∆op(I),
f∆(S(a))f
−1 = S ⊗ S(∆op(a)), S ⊗ S ⊗ S(Φ321) = Φf . (6.18)
We have f = S ⊗ S(∆op(p))γ∆(qβS(r)) and f
−1 = ∆(S(p)αq)δS ⊗ S(∆op(r)). In particular, if the antipode is strong then f = γ, f
−1 = δ.
Proof. The proof of the first relation in (6.18) follows from the following two lemmas, in
turn extending Lemmas 1 and 2 of [47] to weak quasi-Hopf algebras. More precisely, thanks
to Lemma 6.14 we may apply lemma 6.15 to B = A ⊗ A, p = ∆(I), q = S ⊗ S(∆op(I)),
f = ∆, g = ∆ ◦ S, ρ = ∆(α), σ = ∆(β), g = S ⊗ S ◦ ∆op
, ρ = γ, σ = δ. We omit the proof
of the second relation of (6.18). □
Lemma 6.14. We have:
a)
γ = V ((Φ ⊗ I)(∆ ⊗ 1 ⊗ 1(Φ−1))), δ = V
′
((1 ⊗ 1 ⊗ ∆(Φ−1))(I ⊗ Φ)), (6.19)
b) for a ∈ A,
(S ⊗ S(∆op(a(1))))γ∆(a(2)) = ε(a)γ∆(a(1))δ(S ⊗ S(∆op(a(2)))) = ε(a)δ (6.20)
c)
∆(x)δ(S ⊗ S(∆op(y)))γ∆(z) = ∆(I) = (6.21)
∆(I)(S ⊗ S(∆op(p)))γ∆(q)δ(S ⊗ S(∆op(r))) (6.22)
Proof. a) By the cocycle property (6.5) we can write
γ = V (I ⊗ (∆ ⊗ 1(∆(I)))(1 ⊗ ∆ ⊗ 1(Φ))(Φ ⊗ I)(∆ ⊗ 1 ⊗ 1(Φ−1))).
By the defining antipode property (6.7) we have, for T ∈ A⊗4,
V (a ⊗ ∆(b) ⊗ c · T) = ε(b)V (a ⊗ I ⊗ I ⊗ c · T) = V (1 ⊗ 1 ⊗ ε ⊗ 1(a ⊗ b ⊗ c)134T).
It suffices to choose a ⊗ b ⊗ c = I ⊗ ∆(I)Φ and T = (Φ ⊗ I)(∆ ⊗ 1 ⊗ 1(Φ−1)). The identity
involving δ can be proved in a similar way. The proof of b) and c) is a straightforward
generalisation of the case of quasi-Hopf algebras. We refrain from giving details, and we
refer the interested reader to [47].
□
Lemma 6.15. Let B be a algebra, p an idempotent in B, f : A → B a homomorphism
and g : A → B an anti-homomorphism with f(I) = g(I) = p, and ρ, σ ∈ pBp such that:
g(a(1))ρf(a(2)) = ε(a)ρ, f(a(1))σg(a(2)) = ε(a)σ (6.23)
where a ∈ A. Moreover,
f(x)σg(y)ρf(z) = p, g(p)ρf(q)σg(r) = p (6.24)
In addition, we have an idempotent q ∈ B, ρ, σ ∈ qBp and an anti-homomorphism g :
A → B with g(I) = q also satisfying (6.23) - (6.24) (in (6.24) q replaces p). Then there
exists a unique partially invertible element F ∈ B with D(F) = p, R(F) = q, such that
F ρ = ρ, σF = σ (6.25)

42 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
g(a) = F g(a)F
−1
. (6.26)
We have
F = g(p)ρf(q)σg(r), F −1 =
X
i
g(p)ρf(q)σ g(r). (6.27)
Proof. We first show uniqueness. Let F be partially invertible with the stated domain and
range and satisfying (6.25). Inserting the explicit form of p and q given in (6.24) in the
equalities F = F p and F
−1 = qF −1
, respectively, and taking into account the mentioned
relations (6.25), gives formulas (6.27).
We apply the map W : A⊗3 → B, W(b ⊗ c ⊗ d) = g(b)ρf(c)σg(d), respectively to
(∆ ⊗ 1(∆(a)))Φ−1 and Φ−1(1 ⊗ ∆(∆(a))) and obtain, if F is defined as in (6.27), F g(a) =
g(a)F. Similarly, applying the map X : A⊗4 → B, X(b⊗c⊗d⊗e) = g(b)ρf(c)σg(d)ρf(e),
to the equality:
(1 ⊗ 1 ⊗ ∆(Φ))(∆ ⊗ 1 ⊗ 1(Φ))(Φ−1 ⊗ I) =
= (I ⊗ Φ)(1 ⊗ ∆ ⊗ 1(Φ))(1 ⊗ ∆(∆(I)) ⊗ I)
gives F ρ = ρ. The relations F F −1 = q, F
−1F = p follow again from (6.25). □
We next show that a strictly coassociative coproduct with trivial associator in the of a
weak case, quasi-Hopf algebra is not compatible with non-unitality of the coproduct.
Proposition 6.16. Let A be a weak quasi-Hopf algebra with coassociative coproduct and
associator Φ = ∆ ⊗ 1 ◦ ∆(I) = Φ−1. Then A is a Hopf algebra.
Proof. It is easy to see that Φ is an associator and that the elements α and β defining
an antipode are invertible, hence A admits a strong antipode, say S. We are left to
show that ∆(I) = I ⊗ I. The element γ defined by relation (6.16) turns out to be I
thanks to coassociativity of ∆. Hence S satisfies the untwisted anticomultiplicative relation
∆ ◦ S = S ⊗ S ◦ ∆op by the previous proposition. We use the notation ∆(x) = x1 ⊗ x2 and
∆(I) = a ⊗ b and compute
∆(I) = ∆(I)ε(a)b ⊗ I = ∆(ε(a)I)b ⊗ I = ∆(a1S(a2))b ⊗ I =
∆(aS(b1))b2 ⊗ I = a1S(b1,2)b2 ⊗ a2S(b1,1) = a1S(b2,1))b2,2 ⊗ a2S(b1) =
a1ε(b2) ⊗ a2S(b1) = a1 ⊗ a2S(b1ε(b2)) = a1 ⊗ a2S(b) =
a ⊗ b1S(b2) = a ⊗ ε(b)I = aε(b) ⊗ I = I ⊗ I.
□
In conclusion of the section we introduce a class of most interest in this paper, those
for which the underlying algebra is isomorphic to a direct sum of full matrix algebras.
Although we are mostly interested in finite dimensional algebras, in the following definition
we allow infinite dimensionality. The direct sum of full matrix algebras
A =
M
r
Mnr(C),

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 43
is the algebra with elements of the form (ar) with ar ∈ Mnr, and only finitely many of
them are nonzero. The identity of Mnris a minimal central projection of A and will be
denoted by er. Similarly, the direct product
M(A) = Y
r
Mnr(C)
is the algebra of elements (ar) of the same form but with no further restriction on the
entries. There is no distinction between A and M(A) precisely when the index set is finite,
which amounts to say that A is unital.
Definition 6.17. An algebra A is called discrete if it is isomorphic to a direct sum of
full matrix algebras. A discrete weak quasi bialgebra (Hopf algebra) is a discrete algebra
endowed with coproduct, counit and associator where the axioms of a weak quasi bialgebra
are modified as follows. A coproduct ∆ : A → M(A ⊗ A) is assumed to take values in
M(A ⊗ A) = Q
r,s Mnr ⊗ Mns
. For fixed integers r, s, the sum P
j ∆(ej )er ⊗ er is well
defined as only finitely many entries are nonzero. Then the coproduct ∆ extends to a
map M(A) → M(A ⊗ A) via the formula ∆(a)er ⊗ es =
P
j ∆(aj )er ⊗ es for a = (aj ),
and the extension is a homomorphism. In particular, ∆(I) is a well defined idempotent of
M(A ⊗ A). Similarly, ∆ ⊗ 1 and 1 ⊗ ∆ extend to M(A ⊗ A). The associator Φ, counit ε
(and the antipode (S, α, β) in the Hopf case) are defined as in the unital case, except that
Φ, α, β may lie in the corresponding multiplier algebras.
Most of the results of this section hold for discrete weak quasi bialgebras (Hopf algebras).
In Sect. 11 we shall introduce involutive and C
∗
-versions. As we shall see in later sections,
such a class is useful to study semisimple tensor categories. We also note that Van Daele
developed a theory for the multiplier Hopf algebras, a class of algebras more general than
the discrete Hopf algebras [177]. An analogous generalization from the theory of weak
quasi-Hopf algebras goes beyond the aim of this paper.
