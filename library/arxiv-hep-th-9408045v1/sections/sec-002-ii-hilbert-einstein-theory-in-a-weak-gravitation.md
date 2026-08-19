---
doc_id: arxiv-hep-th-9408045v1
doc_title: ""
section_id: sec-002-ii-hilbert-einstein-theory-in-a-weak-gravitation
section_title: "Hilbert-Einstein theory in a weak gravitational ﬁeld"
section_number: II
pages: 3-7
source_pdf: 9408045v1.pdf
source_sha256: a9786c0f44a4e659
doc_brief: "Constrained analysis of topologically massive gravity — We quantize the Einstein gravity in the formalism of weak gra vitational ﬁelds by using the constrained Hamiltonian method."
---
The Hilbert-Einstein Lagrangian reads
L = 1
2κ2
√−g R , (2.1)
where κ is the Einstein constant and we shall use the following ﬂat me tric convention
diag. (+, −, . . . ,−). At it was said in the introduction, we are not making here an y re-
striction to the spacetime dimensions D.
Considering weak gravitational ﬁelds we take the expansion around the ﬂat space
geometry as
gµν (x) = ηµν − κ hµν (x) . (2.2)
Introducing (2.2) into (2.1) and just keeping free ﬁelds we g et
L = 1
4 ∂λ hµν ∂λ hµν − 1
4 ∂λ hµ
µ ∂λ hν
ν + 1
2 ∂λ hλ
µ ∂µ hν
ν − 1
2 ∂λ hλ
µ ∂ν hνµ , (2.3)
where it was considered that the metric is symmetric. Expres sion (2.3) is known as the
Fierz-Pauli Lagrangian for massless particles of spin 2. It is a gauge theory and the
corresponding gauge transformation reads
δhµν = ∂µ ζ ν + ∂ν ζ µ . (2.4)
We are going to study the resulting theory described by the La grangian density (2.3)
making use of the constrained Hamiltonian procedure due to D irac [5]. Since this is a
noncovariant method, it might be convenient to separate tim e and space components in
the expression above. We write down the result as
L = 1
4
( ˙hij ˙hij − ˙hi
i ˙hj
j
)
+
(
∂ihj
j − ∂jhij) ˙h0
i − V , (2.5)
3
where
V = − 1
2 ∂ih0j∂ih0j − 1
4 ∂ihjk ∂ihjk + 1
2 ∂ih00∂ihj
j + 1
4 ∂ihj
j∂ihk
k
− 1
2 ∂ihi
j ∂jh00 − 1
2 ∂ihi
j∂jhk
k + 1
2 ∂ihi0∂jhj0 + 1
2 ∂ihij∂khkj . (2.6)
The canonical momenta are
π00 = ∂L
∂ ˙h00
= 0 , (2.7a)
π0i = ∂L
∂ ˙h0i
= 1
2
(
∂ihj
j − ∂jhij)
, (2.7b)
πij = ∂L
∂ ˙hij
= 1
2
( ˙hij − ηij ˙hk
k
)
. (2.7c)
There are D primary (ﬁrst-class) constraints [5]
Ω = π00 ≈ 0 , (2.8a)
Ω i = π0i + 1
2
(
∂jhij − ∂ihj
j
)
≈ 0 . (2.8b)
This is in agreement with Castellani assumption that stabli shes that the number of sym-
metries of the theory (characterized by each one of the compo nents of ζµ ) is the same as
the number of primary ﬁrst-class constraints [6].
The next step is to look for secondary constraints. We ﬁrst co nstruct the primary
Hamiltonian density
H = π00 ˙h00 + 2π0i ˙h0i + πij ˙hij − L + λΩ + λiΩ i ,
= πij ˙hij − 1
4
˙hij ˙hij + 1
4 hi
i ˙hj
j +
(
λ + ˙h00
)
Ω +
(
λi + 2 ˙h0i
)
Ω i + V . (2.9)
4
We notice that is possible to redeﬁne the Lagrange multiplie rs λ and λi in order to ab-
sorb the velocities ˙h00 and ˙h0i. The remaining velocities can be eliminated by using the
momentum expressions (2.7c). The ﬁnal result reads
H = πijπij + 1
2−D πi
i πj
j + λΩ + λiΩ i + V . (2.10)
Considering the fundamental Poisson brackets (*)
{
h00(x), π 00(y)
}
= δ(D− 1)(
⃗ x− ⃗ y
)
, (2.11a)
{
h0i(x), π 0j(y)
}
= δi
j δ(D− 1)(
⃗ x− ⃗ y
)
, (2.11b)
{
hij(x), π kl(y)
}
= 1
2
(
δi
kδj
l + δi
l δj
k
)
δ(D− 1)(
⃗ x− ⃗ y
)
. (2.11c)
and using the Hamiltonian (2.10) we obtain from the consiste ncy condition the following
secondary-constraints
Φ = ∇2hi
i + ∂i∂j hij ≈ 0 , (2.12a)
Φ i = 2∂jπij + ∂i∂j h0i + ∇2h0i ≈ 0 . (2.12b)
Introducing these constraints into the Lagrangian by means of new Lagrange multipliers
and using the consistency condition again we verify that the re are no tertiary constraints.
We notice that constraints Φ and Φ i are also ﬁrst-class.
In order to calculate the Dirac brackets we have to ﬁx the gaug e. Let us start from
the corresponding of the Coulomb gauge of the electromagnet ic Maxwell theory, i.e.
∂ihij ≈ 0 . (2.13)
(*) It will always be understood that brackets are taken at th e same time x0 = y0.
5
We also choose that
h00 ≈ 0 , (2.14a)
h0i ≈ 0 . (2.14b)
With the gauge condition h0i ≈ 0, the secondary constraints Φ i just turns to be ∂jπij ≈ 0.
Compatibility with the equation of motion permit us to infer that
πi
i ≈ 0 . (2.15)
Summarizing, the full set of (second-class) constraints is
Ω = π00 ≈ 0 , (2.16a)
Ψ = h00 ≈ 0 , (2.16b)
Ω i = π0i ≈ 0 , (2.16c)
Ψ i = h0i ≈ 0 , (2.16d)
Φ = hi
i ≈ 0 , (2.16e)
Σ = πi
i ≈ 0 , (2.16f )
Σ i = ∂jhji ≈ 0 , (2.16g)
Φ i = ∂jπji ≈ 0 . (2.16h)
This set contains 4 D constraints. There is no sense cases with D ≤ 2 because the number
of degrees of freedom will be negative. D = 3 also corresponds to a nonphysical case where
the number of degrees of freedom is zero. In general, the numb er of degrees of freedom is
D(D−3)/2.
The calculation of the Dirac brackets is directly done by mea ns of a hard algebraic
work. The nonvanishing ones are
6
{
hij(x), π kl(y)
}
=
[ 1
2
(
δi
l ∂j∂k + δi
k ∂j∂l + δj
l ∂i∂k + δj
k ∂i∂l
) 1
∇2
+ 1
2
(
δi
k δj
l + δi
l δj
k
)
− 1
D − 2 ηijηkl
− 1
D − 2
(
ηij∂k∂l + ηkl∂i∂j) 1
∇2
+ D − 3
D − 2
∂i∂j∂k∂l
∇4
]
δ(D− 1)(⃗ x− ⃗ y) . (2.17)
We clearly notice that, in fact, the case with D = 2 does not make sense by virtue of terms
with ( D− 2)− 1. Further, one can show that for D = 3 the above bracket is zero.
Looking at (2.17), we observe that there are no problem with o rdering operators, so
it can be directly transformed into commutator by means of th e usual rule of quantization
{
Dirac brackets
}
− → 1
i¯h
[
commutators
]
. (2.18)
Considering the transformations above, one can calculate t he propagators among the hij
ﬁelds. The result is
< 0|T
(
hij(−k) hkl(k)|0 >= i
k2
[
δi
kδj
l + δi
l δj
k + 1
⃗k2
(
δi
k kjkl + δi
l kjkk + δj
k kikl + δj
l kikk
)
− 2
D − 2
(
ηijηkl + ηij kkkl
⃗k2
− ηkl
kikj
⃗k2
)
+ 2(D − 3)
(D − 2)
kikjkkkl
⃗k4
]
. (2.19)
We notice that there is no dynamical massive pole.
