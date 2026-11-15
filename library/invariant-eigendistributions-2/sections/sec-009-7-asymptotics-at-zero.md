---
doc_id: invariant-eigendistributions-2
doc_title: "Invariant eigendistributions on a semisimple Lie algebra and homology classes on the conormal variety II: representations of Weyl groups"
section_id: sec-009-7-asymptotics-at-zero
section_title: "Asymptotics at zero"
section_number: 7
pages: 12-16
source_pdf: Invariant_eigendistributions_2.pdf
source_sha256: ee43c3ebeff95265
toc_source: inferred
doc_brief: "Invariant eigendistributions on a semisimple Lie algebra and homology classes on the conormal variety II: representations of Weyl groups — 18 sections: Front matter; Contents; Introduction."
---
Recall the W-ﬁltration of Z by the inverse images Z(O) of nilpotent K-orbits O on N ∩k⊥, which gave
rise to the decomposition (4.1) of grH∗(Z). Passing from Z to S, the analogous ﬁltration of S by the
inverse images S(O) of Go-orbits on N ∩igo∗gives a ﬁltration of H2n(S) by the subgroups H2n(S( ¯O))
according to the closure relation among the O’s leading to the decomposition
grH2n(S) ≈

O
H2n(S(O)).
(1)
As in (4.2),
H2n(S(O)) ≈H2e(ν)(Bν)Ao(ν)
(2)
and the inclusion Bν ⊂
→B induces a W-injection
H2e(ν)(Bν)A(ν) ⊂
→H2e(ν)(B)
(3)
(Note that there is Ao(ν) in (2), A(ν) = Ao(ν) × Ao(ν) in (3).) We choose the same base point b1 = s1
to deﬁne the W-action on H2e(ν)(Bν)A(ν) and on H2e(ν)(B).)
We recall Borel’s description of the cohomology ring of B [Borel 1953]. For λ ∈h∗denote τλ the
U-invariant 2-from on B which at the base point s1 is given by
τλ(x · s1, y · s1) = λ([x, y])
for x, y ∈u
(4)
Set
ωλ = −1
2πiτλ
The map λ →ωλ extends to a map f →ωf from the ring C[h] of polynomial functions on h to the algebra
of diﬀerential forms on B. It annihilates the W-invariants with zero constant term in C[h], denoted I+,
and induces an isomorphism
C[h]/I+ ≈
→H∗(B),
[f] →[ωf],
(5)
where [f] is the class of f, [ωf] the class of ωf (in de Rahm cohomology). The transpose of (5) is an
isomorphism
H∗(B, C)≈
→H(h∗),
γ →cγ
(6)
REPRESENTATIONS OF WEYL GROUPS
13
where H(h∗) consists of the W-harmonic polynomials on h∗, i.e.
the polynomials annihilated by the
W-invariant constant coeﬃcient operators without constant term.
Explicitly, the isomorphism (6) is
deﬁned by

γ
ωf = ⟨cγ, f⟩.
(7)
The right side is the natural pairing ⟨xi, λj⟩/j! = ⟨x, λ⟩jδij.
cγ may also be deﬁned directly by the
equation
cγ(λ) =

γ
eωλ
(8)
as one sees by taking f = eλ in (7) using ⟨c, eλ⟩= c(λ). Composing (3) and (6) gives a map
H2e(ν)(Bν)A(ν) →He(ν)(h∗)
(9)
where He(ν)(h∗) denotes the homogeneous polynomials of degree e(ν) in H(h∗). Using further (2) we get
a map
H2n(S( ¯O)) →He(ν)(h∗),
Γ →cΓ ,
(10)
This last map (10) is of course not an isomorphism: it factors through the projection of H2n(S( ¯O)) onto
H2n(S(O)) as well as through the projection of H2e(ν)(Bν)Ao(ν) onto H2e(ν)(Bν)A(ν).
7.1 Theorem. For any nilpotent Go-orbit O in igo∗and any 2n-cycle Γ ∈H2n(S( ¯O)) over ¯O,
1
(2πi)n

pλΓ
exλ−σλ = cΓ (λ)
1
(2πi)d

O
exO−σO + o(|λ|e)
(11)
Explanation and remarks. d = d(O) = dimCO,
e = e(O) = dimCBν(ν ∈O); xO is x considered as a
function on O; σO is the canonical 2-form on O:
σO(x · ν, y · ν) = ⟨ν, [x, y]⟩.
The equation (11) is understood as an identity of distributions on go, as usual. It will be abbreviated to
θΓ (λ) = cΓ (λ)θO + o(|λ|e).
(12)
with
θΓ (λ) =
1
(2πi)n

pλΓ
exλ−σλ ,
θO =
1
(2πi)d

O
exO−σO .
The equation (11) can also be written as an asymptotic relation as x →0 in go in the sense of Barbasch
and Vogan [1980]:
θΓ (λ) ∼cΓ (λ)θO as x →0 in go.
(13)
REPRESENTATIONS OF WEYL GROUPS
14
This means that cΓ (λ)θO is the leading term in the asymptotic expansion of θΓ (λ) at x = 0 described in
Theorem 1.3 of [Barbasch-Vogan 1980].
Proof of the theorem. Fix the Go-orbit O on N ∩igo∗and Γ ∈H2n(S( ¯O)). For f ∈C∞
c (g), set
ϕ(ξ) =

g
eξ(x)f(x)dx.
The theorem says that for all such f
(−1)n
(2πi)nn!

pλΓ
ϕσλn = cΓ (λ) (−1)d
(2πi)dd!

O
ϕσOd + o(|λ|e).
To determine the asymptotic behaviour of the integral on the left we need some general remarks on
symplectic structure. Let Q be an orbit of the complex group G on the nilpotent cone N in g∗. As before,
put
B∗(Q) = {(b, ν)|ν ∈Q}
Then there are injections
B∗(Q) ⊂
→B × Q
(15)
B∗(Q) ⊂
→Ωλ
(16)
the ﬁrst map being the natural inclusion, the second one the restriction of the bijection
pλ : B∗→Ωλ, u · (s1, ν) →u · (λ + ν)
(u ∈U, ν ∈s1⊥). In view (15) and (16) we can restrict to B∗(Q) the 2-form τλ + σQ on B × Q and the
2-form σλ on Ωλ.
7.2 Lemma. The 2-forms τλ + σQ and σλ agree on B∗(Q).
Proof of the lemma. Because of U-invariance it suﬃces to show that the forms agree at a point (s1, ν)
with ν ⊂s1⊥∩Q. Let
u(t) · (s1, v(t) · ν)
(17)
be a smooth curve on B∗(Q) with u(t) ∈U, v(t) ∈G, v(t) · ν ∈s1⊥, u(0) = 1, v(0) = 1. Its tangent
vector at t = 0 is
(u′ · s1, (u′ + v′) · ν)
(18)
REPRESENTATIONS OF WEYL GROUPS
15
u′, v′ ∈g being the tangent vectors of u(t) and v(t) at t = 0. The 2-form τλ + σQ assigns to two such
tangent vectors at (s1, ν) the value
⟨λ, [u′, u′′]⟩+ ⟨ν, [u′, u′′]⟩+ ⟨ν, [u′, v′′]⟩+ ⟨ν, [v′, u′′]⟩+ ⟨ν, [v′, v′′]⟩.
(19)
The curve on Ωλ corresponding to (17) under the injection (16) is
u(t) · λ + u(t)v(t) · ν
and its tangent vector at λ + ν, corresponding to the vector (18) at (s1, ν), is
u′ · (λ + ν) + v′ · ν.
The 2-form σλ assigns to two such tangent vectors at λ + ν the value
⟨λ, [u′, u′′]⟩+ ⟨ν, [u′, u′′]⟩+ ⟨ν, [u′, v′′]⟩+ ⟨ν, [v′, u′′]⟩+ ⟨λ + ν, [v′, v′′]⟩.
(20)
The last term of (20) = 0, as λ + s1⊥⊂Ωλ is an isotropic (in fact Lagrangian) submanifold of Ωλ, which
is clear. The same is true of the last term of (19), but this is less clear: it is known that, for any b, b⊥∩Q
is a co-isotropic subvariety of Q [Joseph 1984, Lemmas 7.5 and 9.6(i)] of dimension = 1/2 = dimQ (as
follows from [Spaltenstein 1977] and [Steinberg 1976, section 4]), hence in fact Lagrangian. Thus (19)
agrees with (20), proving the lemma.
Remark. The fact that b⊥∩Q is Lagrangian on Q is mentioned in [Ginsburg 1986, Proposition 4.3]. The
proof indicated there uses general facts from symplectic geometry. [NB(2003). These facts (moment maps
preserving Poisson brackets) imply also that the form σQ is the canonical 2-form on B∗over the open
orbit Q, where B∗→{N is regular.]
We return to the proof of the theorem. Apply the above lemma to the G-orbit Q containing the Go-orbit
O. The ﬁbration
Bν ⊂
→B∗(Q) →Q
(21)
restricts to
Bν ⊂
→S(O) →O.
(22)
For Γ it suﬃces to take a component of S(O). As explained for Z(O) in connection with (4.2), a component
of S(O) is a dense part of an Sw , denoted Sw(O). The ﬁbration (22) restricts to a ﬁbration
Bνw ⊂
→Sw(O) →O.
(23)
According to Steinberg [1976] the ﬁbre Bνw = Sw(O)∩Bν over ν ∈O in (23) is a single orbit of components
of Bν under the component group Ao(ν) of the stabilizer of ν in Go. These components all have the same
REPRESENTATIONS OF WEYL GROUPS
16
dimension e = e(O) = dimCBν, by a result of Spaltenstein [1977]. The fundamental class of such a
component in H2e(B) is independent of ν in O, as O is connected. Note, incidentally, that
d + e = n
because of the ﬁbration (14). Now calculate:
(−1)n
(2πi)nn!

pλSw(O)
ϕσλn =
(−1)n
(2πi)nn!

Sw(O)
(ϕ ◦pλ)(τλ + σO)n
=
(−1)n
(2πi)nd!e!

O
 
Bν w
ϕ(pλ(b, ν))τλe(db)

σOd(dν) + o(|λ|e)
(24)
where we used the ﬁbration (22) and Lemma 7.2 to write the integral over Sw(O) as an integral over the
ﬁbre Bνw followed by an integral over the base O.
In the integral (24) write (b, ν) = u·(s1, ν1) with u ∈U and ν1 ∈s1⊥. Then the integrand becomes
ϕ(pλ(b, ν)) = ϕ(u · (λ + ν1))
= ϕ(u · ν1) + o(|λ|)
= ϕ(ν) + o(|λ|)
Thus
(24) =
(−1)n
(2πi)nd!e!

O
ϕ(ν)
 
Bν w
τλe(db)

σOd(dν) + o(|λ|e)
=
(−1)d
(2πi)dd!

O
ϕ(ν)⟨c, eλ⟩σOd(dν) + o(|λ|e)
=
(−1)d
(2πi)dd!c(λ)

O
ϕ(ν)σOd(dν) + +o(|λ|e)
(25)
where c = cνw ∈He(h∗) is the harmonic polynomial on h∗representing the fundamental class of Bνw in
H∗(B) under Borel’s isomorphism (6). As in (7), ⟨c, f⟩is the natural pairing of polynomials on h∗and
formal power series on h , so that ⟨c, eλ⟩= c(λ). This proves the theorem.
