---
doc_id: arxiv-hep-th-9408045v1
doc_title: ""
section_id: sec-003-iii-topologically-massive-gravitation
section_title: "Topologically massive gravitation"
section_number: III
pages: 7-14
source_pdf: 9408045v1.pdf
source_sha256: a9786c0f44a4e659
doc_brief: "Constrained analysis of topologically massive gravity — We quantize the Einstein gravity in the formalism of weak gra vitational ﬁelds by using the constrained Hamiltonian method."
---
When the spacetime dimension is odd, it is possible to introd uce a CS term in the
Lagrangian. In this section we concentrate on the 2+1 case. T he corresponding CS
Lagrangian reads
7
LCS = 1
µ ǫλµν Γ ρ
λσ
(
∂µ Γ σ
ρν + 2
3 Γ σ
µξ Γ ξ
νρ
)
. (3.1)
Considering the expansion of weak gravitational ﬁelds give n by (2.2) we get
LCS = κ2
2µ ǫλµν
(
∂σ hρ
λ ∂ρ ∂µ hσ
ν − ∂σ hρ
λ ∂σ ∂µ hρν
)
. (3.2)
Making the separation of space and time components and addin g the result to (2.5) the
result is
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
i + κ2
µ ǫij
(
˙hk
0 ∂k∂i h0j
− ∂i∂k h00 ˙hk
j − ∂ihk
0 ¨hkj + ¨hk
i ∂kh0j + 1
2 ∂k∂lhl
i ˙hk
j
+ 1
2
˙hk
i ¨hkj + 1
2 ∇2h0
i ˙h0j + 1
2 ∇2hk
i ˙hkj
)
− V , (3.3)
where
V = 1
2 ∂ih0j∂ih0j + 1
4 ∂ihjk ∂ihjk − 1
2 ∂ih00∂ihj
j − 1
4 ∂ihj
j∂ihk
k
+ 1
2 ∂ihi
j ∂jh00 + 1
2 ∂ihi
j∂jhk
k − 1
2 ∂ihi
0∂jhj0 − 1
2 ∂ihi
j∂khkj
− κ2
µ ǫij
(
∂khl
0∂i∂lhk
j − ∇2hk
0∂ihkj − ∇2h00∂ih0j
)
. (3.4)
We observe that the inclusion of the CS Lagrangian leads to th e appearance of higher
derivative terms [7]. The correct Hamiltonian treatment re quires a phase space as hµν ⊕
˙hµν ⊕ πµν ⊕ sµν , where πµν and sµν are the canonical momenta conjugate to hµν and ˙hµν ,
respectively. Now, velocities have to be considered as inde pendent coordinates. Using the
general expressions
8
πµν = ∂L
∂ ˙hµν
− ∂
∂t
∂L
∂¨hµν
− 2∂i
∂L
∂ (∂i ˙hµν )
, (3.5)
sµν = ∂L
∂¨hµν
, (3.6)
we get
π00 = 0 , (3.7a)
π0i = 1
2
(
∂ihj
j − ∂jhji
)
+ κ2
2µ
(
2ǫjk ∂j∂ih0
k − ǫij∇2h0j
)
, (3.7b)
πij = 1
2
(
˙hij − ηij ˙hk
k
)
+ κ2
4µ ǫik
(
2∂k∂jh00 − ∂j∂lhl
k + 2¨hj
k
− ∇2hj
k − 2∂k ˙hj
0 − 2∂j ˙h0
k + (i ↔ j)
)
, (3.7c)
s00 = 0 , (3.7d)
s0i = 0 , (3.7e)
sij = κ2
2µ
[
ǫik (
∂khj
0 + ∂jh0k − 1
2
˙hj
k
)
+ (i ↔ j)
]
. (3.7f )
These lead to the following set of primary constraints
Ω = π00 ≈ 0 , (3.8a)
Ω i = π0i + 1
2
(
∂jhji − ∂ihj
j
)
− κ2
2µ
(
2ǫjk ∂j∂ih0
k − ǫij∇2h0
j
)
≈ 0 , (3.8b)
Λ = πi
i + 1
2
˙hi
i − κ2
2µ ǫij∂j∂khk
i ≈ 0 , (3.8c)
Θ = s00 ≈ 0 , (3.8d)
Θ i = s0i ≈ 0 , (3.8e)
Θ ij = sij −
[ κ2
2µ ǫik
(
∂khj
0 + ∂jh0k − 1
2
˙hj
k
)
+ (i ↔ j)
]
. (3.8f )
The total primary Hamiltonian density in this case reads
9
H = πµν ˙hµν + sµν ¨hµν − L + λΩ + λiΩ i + ρΘ + ρiΘ i + ρijΘ ij + ξΛ . (3.9)
Developing the expression above, one can show that some term s can be absorbed by re-
deﬁning the Lagrange multipliers. One interesting point, t hat might be opportune to be
mentioned, is that ¨hij are also eliminated in this way and not by using the expressio n
(3.7c) that gives πij in terms of ¨hij (this expression is not a constraint). This is provi-
dential because it is not possible to use (3.7c) in order to ex press ¨hij in terms of πij and
other components of the phase space. This is so because the co eﬃcient of ¨hij does not
have inverse.
The ﬁnal expression for the primary hamiltonian density rea ds
H = πij ˙hij − 1
4
(
˙hij ˙hij + 2∂ih0j∂ih0j + ∂ihjk ∂ihjk − ˙hi
i ˙hj
j
− 2∂ih00∂ihj
j − ∂ihj
j∂ihk
k + 2∂ihi
j∂jh00
+ 2∂ihi
j ∂jhk
k − 2∂ihi
0∂jhj0 − 2∂ihi
j∂khkj
)
+ κ2
2µ ǫij
(
2∂i∂kh00 ˙hk
j − 2∂khl
0∂l∂ihk
j + 2∇2hk
0∂ihkj
+ 2∇2h00∂ih0j − ∂k∂lhl
i ˙hk
j − ∇2hk
i ˙hkj
)
+λΩ + λiΩ i + ρΘ + ρiΘ i + ρijΘ ij + ξΛ . (3.10)
Using the consistency condition and making properly combin ations of the ﬁnal constraints
in order to obtain the biggest number of ﬁrst-class ones we ge t the ﬁnal set
(i) 1st class contraints
Ω = π00 ≈ 0 , (3.11a)
Θ = s00 ≈ 0 , (3.11b)
Θ i = s0i ≈ 0 , (3.11c)
10
Γ i = ∂jsij − π0i − 1
2
(
∂jhji − ∂ihj
j
)
+ κ2
4µ
(
2ǫji∂k∂jhk0
+ ǫij∇2h0j − ǫjk ∂k ˙hi
j + ǫij∂k ˙hk
j
)
≈ 0 , (3.11d)
ξi = ∂jπij + 1
2
(
∇2hi
0 + ∂j∂ihj0
)
− κ2
4µ ǫjk ∂j
(
∂l∂ihl
k + ∇2hi
k
)
≈ 0 , (3.11e)
Γ = ∂i∂jsij − 1
2
(
∂i∂jhij + ∇2hi
i
)
+ κ2
2µ ǫij∂i
(
4∇2h0j + 3∂k ˙hk
j
)
≈ 0 . (3.11f )
(ii) 2nd class contraintsΘ ij = sij −
[ κ2
2µ ǫik
(
∂khj
0 + ∂jh0k − 1
2
˙hj
k
)
+ (i ↔ j)
]
≈ 0 , (3.12a)
Λ = πi
i + 1
2
˙hi
i − κ2
2µ ǫij∂j∂khk
i ≈ 0 . (3.12b)
In fact we notice that there is just one degree of freedom for D =3.
We use the Dirac method iteratively. The elimination of the s econd-class constraints
above results in the following preliminar brackets
{
hij(x), π kl(y)
} ∗
= 1
2
(
δi
k δj
l + δi
l δj
k
)
δ(2)(⃗ x− ⃗ y) ,
{ ˙hij(x), s kl(y)
} ∗
= 1
4
(
δi
k δj
l + δi
l δj
k − ηij ηkl
)
δ(2)(⃗ x− ⃗ y) ,
{ ˙hij(x), ˙hkl(y)
} ∗
= − µ
4κ2
(
ǫi
k δj
l + ǫi
l δj
k + ǫj
k δi
l + ǫj
l δi
k
)
δ(2)(⃗ x− ⃗ y) ,
{
sij(x), s kl(y)
} ∗
= − κ2
16µ
(
ǫi
k δj
l + ǫi
l δj
k + ǫj
k δi
l + ǫj
l δi
k
)
δ(2)(⃗ x− ⃗ y) ,
{
hij(x), ˙hkl(y)
} ∗
= −ηij ηkl δ(2)(⃗ x− ⃗ y) ,
{ ˙hij(x), π kl(y)
} ∗
= − κ2
4µ ηij (
ǫm
l ∂m∂k + ǫm
k ∂m∂l
)
δ(2)(⃗ x− ⃗ y) ,
{
h00(x), π 00(y)
} ∗
= δ(2)(⃗ x− ⃗ y) ,
{ ˙h00(x), s 00(y)
} ∗
= δ(2)(⃗ x− ⃗ y) ,
{
h0i(x), π 0j(y)
} ∗
= 1
2 δi
j δ(2)(⃗ x− ⃗ y) . (3.13)
11
The remaining brackets are zero. To calculate the ﬁnal Dirac brackets we have to ﬁx
the gauge. Here we also choose the corresponding of the Coulo mb gauge (2.13), plus the
further conditions (2.14a) and (2.14b). Consistency with t he equations of motion permit
us also to choose
˙h00 ≈ 0 ,
˙h0i ≈ 0 ,
˙hi
i ≈ 0 ,
∂ihij ≈ 0 . (3.14)
With this gauge choice, the set of constraints given by (3.11 ) becomes second-class. It is
then possible to calculate the Dirac brackets. After a hard a lgebraic work we get
{
hij(x), π kl(y)
} D
= −
[
ηijηkl + ηij ∂k∂l
∇2 + ηkl
∂i∂j
∇2
− 1
2
(
δi
kδj
l + δi
k
∂j∂l
∇2 + δi
l
∂j∂k
∇2 + (i ↔ j)
) ]
δ(2)(⃗ x− ⃗ y) , (3.17a)
{
πij(x), π kl(y)
} D
= − κ2
4µ
[ (
ǫml∂m∂k + ǫmk∂m∂l
) (
ηij + 2 ∂i∂j
∇2
)
− 2
(
ηkl + 2 ∂k∂l
∇2
) (
ǫmi∂m∂j + i ↔ j
) ]
δ(2)(⃗ x− ⃗ y) , (3.17b)
{ ˙hij(x), ˙hkl(y)
} D
= − µ
4κ2
(
ǫi
lδj
k + ǫi
kδj
l + i ↔ j
)
δ(2)(⃗ x− ⃗ y) , (3.17c)
{ ˙hij(x), s kl(y)
} D
= 1
4
(
δi
kδj
l + δi
l δj
k − ηijηkl
)
δ(2)(⃗ x− ⃗ y) , (3.17d)
{
sij(x), s kl(y)
} D
= − κ2
16µ
(
ǫi
lδj
k + ǫi
kδj
l + i ↔ j
)
δ(2)(⃗ x− ⃗ y) , (3.17e)
{
hij(x), ˙hkl(y)
} D
=
(
ηij + ∂i∂j
∇2
) (
ηkl + 2 ∂k∂l
∇2
)
δ(2)(⃗ x− ⃗ y) , (3.17f )
{ ˙hij(x), π kl(y)
} D
= κ2
2µ
(
ǫm
l∂m∂k + l ↔ k
) (
ηij + ∂i∂j
∇2
)
δ(2)(⃗ x− ⃗ y) , (3.17g)
{
hij(x), s kl(y)
} D
= κ2
4µ∇2 ηij
(
ǫm
l∂m∂k + l ↔ k
) (
ηij + ∂i∂j
∇2
)
δ(2)(⃗ x− ⃗ y) ,(3.17h)
{
πij(x), s kl(y)
} D
= κ4
8µ2
(
δi
k∂j∂l + ∂i∂j∂k∂l
∇2 + i ↔ j; l ↔ k
)
δ(2)(⃗ x− ⃗ y) , (3.17i)
12
{ ˙hij(x), π 0k(y)
} D
=
( 1
2 ηij + ∂i∂j
∇2
)
∂kδ(2)(⃗ x− ⃗ y) , (3.17j)
{
sij(x), π 0k(y)
} D
= κ2
4µ
(
ǫmi∂m∂j + ǫmj∂m∂i
)
∂k δ(2)(⃗ x− ⃗ y) . (3.17k)
One can check the validity of the brackets above by showing th at they are strongly con-
sistent with all the constraints.
We notice that there are no problem with ordering operators. So, the above brack-
ets can be transform without problems to commutators by mean s of the usual rule of
quantization given by (2.18). The Feynman propagators amon g the ﬁelds hij are (details
of calculating Feynman propagators when there are higher de rivatives can be found in
references [8])
< 0|T
(
hij(x)hkl(y)|0 >=i
∫ d3k
(2π)3
eik(x− y)
k2( µ 2
κ4 − 4k2
0
)
[
4κ2k2
0
kkkl
⃗k2
ηij
− µ2
κ4
(
ηijηkl + kikj
⃗k2
ηkl + 2 kkkl
⃗k2
ηij + 2 kikjklkk
⃗k4
)
− µ2
2κ2
(
ηj
l ηi
k + ηj
kηi
l − 2ηklηij
)
+ 8k2
0
( 1
2 ηijηkl + kkkl
⃗k2
ηij + 1
2
kikj
⃗k2
ηkl + kikjkkkl
⃗k4
)
− µ2
κ2⃗k2
(
kkklηij + kikjηkl −
(
kiklηj
k + i ↔ j; k ↔ l
) )
+ iµk0
⃗k2
( 1
2 ǫpikpkjηkl + ǫi
kkjkl + i ↔ j; k ↔ l
)
− iµk0
2
(
ǫk
iηj
l + i ↔ j; k ↔ l
) ]
. (3.18)
We observe that there is a massive (topological) pole given b y µ/2κ2. This is in agreement
with previous results found in literature [3,4,9] and show t he consistency of the quantization
procedure we have used.
13
