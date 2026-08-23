---
doc_id: arxiv-2410.20973v1
doc_title: "SUMMABILITY FOR STATE INTEGRALS OF HYPERBOLIC KNOTS"
section_id: sec-006-21-existence-of-thimbles
section_title: "Existence of thimbles"
section_number: 2.1
pages: 9-12
source_pdf: 2410.20973v1.pdf
source_sha256: 852b7bbc81a62883
doc_brief: "SUMMABILITY FOR STATE INTEGRALS OF HYPERBOLIC KNOTS — We prove conjectures of Garoufalidis-Gu-Mari˜ no [ 9] that perturbative series associated with the hyperbolic knots 4 1 and 5 2 are resurgent and"
---
to V , we will use two descriptions of Σ and V . In particular, we choose branch cuts in the
upper half plane to deﬁne a function Λ (see Figure 2).
Figure 2. The two conventions for the branch cuts of the function V .
Taking the principle branch of Li 2 we ﬁnd that for
V (z+, m+) = B Li2(e(z+))
(2πi)2 + B
24 + A
2 z+(z+ + 1) + m+z+ ,
Λ( z−, m−) = −B Li2(e(−z−))
(2πi)2 + B
12− B
2
(
z−− 1
2
) 2
+ A
2 z−(z− + 1) + m−z− ,
(29)
and p = (z+, m+)∈ Σ we have 3
V (p) = V (z+, m+) = Λ( z−, m−)∈ C/Z , (30)
where z− = z−(p) = z+(p) and m− = m−(p) = m+(p) +B⌊z+(p)⌋. It will be useful to regard
the surface Σ as being given by A-copies of the complex plane, glued together along the
branch cuts at each integer point k∈ Z. In particular, allowing only m∈{ 0,··· , A− 1} as
opposed to m∈ Z. This can always be done using the second relation in Equation ( 3). We
have the derivative V ′ : Σ → C given by
V ′(z+, m+) = −B log(1− e(z+))
2πi + Az+ + A
2 + m+ ,
Λ ′(z−, m−) = −B log(1− e(−z−))
2πi + (A− B)z− + A
2 + B
2 + m− .
(31)
3In fact we have more generally, V (z, m ) = Λ( z, m + Bk)− Bk(k + 1)/ 2∈ C for k =⌊Re(z)⌋.
10 VERONICA F ANTINI AND CAMPBELL WHEELER
Fix a critical point p0 = (z0, m0) satisfying V ′(p0) = 0, as given in Equation (
5). Denote the
critical value of p0 as V0 = V (p0). We are interested in the level sets
Re((V (p)− V0)e−iϑ)∈ cos(2πϑ)Z (32)
as we vary ϑ∈ (−π/2, π/2)∪ (π/2, 3π/2).
Deﬁnition 2.1. If p∈ Σ such that V (p)∈ V0− ieiϑλ + Z for some constant λ > 0, then
let Γ p,ϑ denote the connected component of V0− ieiϑR≥λ + Z containing p. For the critical
point p0, letCp0,ϑ denote the connected component of V0− ieiϑR≥0 + Z containing p0.
Lemma 2.2. Suppose that eiϑ∈ C\S(V0) and p∈ Σ such that V (p)∈ V0− ieiϑR≥0 + Z.
Then the set Γ p,ϑ is a smooth curve with a parametrisation γ : R≥0→ Σ such that
lim
t→∞
γ′(t) = i
√
ieiϑ or − i
√
ieiϑ|(A− B)|
A− B . (33)
Proof. Firstly, notice that
Li2(e(z))
(2πi)2 + 1
24 = −Li2(1− e(z))
(2πi)2 − Li1(e(z))
2πi z (34)
and therefore, for small enough |z| there is a constant C0 > 0 such that
⏐
⏐
⏐Li2(e(z))
(2πi)2 + 1
24
⏐
⏐
⏐ < C 0|z log(−iz)| . (35)
Therefore, there exists constants C1, C2 > 0 such that, for k ∈ Z and small enough |z|
(independent of k), the representative of V with the smallest absolute value
4 satisﬁes
|V (z + k, m)| =
⏐
⏐
⏐
⏐
B Li2(e(z))
(2πi)2 + B
24 + A
2 (z + k)(z + k + 1) + mz
⏐
⏐
⏐
⏐
< BC 0|z log(z)| + A|z|2 +|Ak + m + A
2||z| < C 1|z log(−iz)| + C2(1 +|k|)|z| ,
(36)
and similarly
|Λ( z + k, m)| < C 1|z log(iz)| + C2(1 +|k|)|z| . (37)
Consider the set 5
Σ ǫ =
⋃
±
{
x∈ Σ
⏐
⏐
⏐Im(z±(p))∈± R≥0 and∀k∈ Z |z±(x)− k|≥ ǫ
1 +|k|
}
. (38)
Given eiϑ /∈S (V0) the set
V0− ieiϑR≥0 + Z (39)
is disjoint from 0∈ C/Z. From Equations ( 36) and ( 37) for any δ > 0, small enough ǫ = ǫ(δ),
and x∈ Σ\Σ ǫ we have|V (x)| < δ . Therefore, there exists ǫ > 0 such that Γ p,ϑ⊂ Σ ǫ.
4That means we choose a representative with |Re(V (z + k))|≤ 1/ 2.
5Here we restrict to m = 0, . . . , A − 1 to have a ﬁnite number of conditions for each point x.
SUMMABILITY FOR STATE INTEGRALS OF HYPERBOLIC KNOTS 11
On the set Σ ǫ we can approximate the derivative of V . To do this we notice that for a
ﬁxed α∈ (0, 1) there exists constants C3, C4 > 0 such that for p∈ Σ ǫ with Im( z+(p))≥ 0
and k∈ Z with Re( z+(p)− k)∈ (−1/2, 1/2] we have bounds
⏐
⏐
⏐log(1− e(z))
2πi
⏐
⏐
⏐≤ C3
|z− k|α≤ C3(1 +|k|)α
ǫα < C4|z|α
ǫα . (40)
Therefore, there is a constant C5 such that
|V ′(z)− Az| <|z|
( C5
|z|1−α + A
2|z| + m
|z|
)
. (41)
A similar bound works for Im( z−(p))≤ 0 replacing A by A− B. Therefore, for any δ1 > 0
there exists an M > 0 such that for p∈ Σ ǫ with Im( z+(p))≥ 0 and|z+(p)| > M
|V ′(p)− Az+(p)| <|z+(p)|δ1 , (42)
and for Im( z−(p))≤ 0 and|z−(p)| > M we ﬁnd that
|V ′(p)− (A− B)z−(p)| <|z−(p)|δ1 . (43)
Given the set of p∈ Σ ǫ with|z±(p)|≤ M is compact, we see that the intersection with Γ p,ϑ
is also compact. The remaining portion of Γ p,ϑ therefore has |z±(p)| > M . Assuming that
M is big enough, |z+(p)| > M , and Im( z+(p)) > 0 we see that
|Im(V (p)− V (p0)− A
2 z+(p)(z+(p) + 1)− mz+(p))|≤ C6 , (44)
for some constant C6 > 0. Given that Im( V (p)− V (p0))Im(ieiϑ)−1 < 0, this implies that
Re(z+(p))Im(ieiϑ) < 0. Therefore, the quadrant containing z+(p) is determined by the sign
of Im( ieiϑ). Moreover, the curve Γ p,ϑ has tangent at a point p given by
eiϑ
iV ′(p) . (45)
Therefore for |z+(p)| > M , there is a constant C7 independent of δ1 such that for all
Im(z+(p))≥ 0
⏐
⏐
⏐eiϑ|z+(p)|
iV ′(p) − eiϑ|z+(p)|
iAz+(p)
⏐
⏐
⏐ < δ 1C7 . (46)
Therefore, the tangent direction always points towards a line para llel to i
√
ieiϑ, which is
in the same quadrant as z+(p). Similarly for the lower half plane we ﬁnd that the tangent
direction always points towards a line parallel to −i
√
i(A− B)eiϑ, which is in the same
quadrant as z−(p). Therefore, in the limit, the tangent is described by Equation ( 33). □
Corollary 2.3. If eiϑ∈ C\S(V0), then the setCp0,ϑ is a smooth curve with a parametrisation
γ : R→ Σ such that the limit of γ′ at±∞ is given in Equation ( 33).
This describes the limiting behaviour of the thimbles associated to the ﬁnite set of critical
points of V . We see that outside a compact set the behaviour is trivial and tend s to a
straight line towards inﬁnity. This is illustrated in the following example.
12 VERONICA F ANTINI AND CAMPBELL WHEELER
Example 2.4. As an example of Corollary
2.3, we can consider the case ( A, B) = (1 , 2).
As we saw in the introduction, the critical points were located at ( −5/6, 0) and (−1/6, 0) in
Equation ( 6). Taking ϑ = 1.6650 we plot the set C(−5/6,0),ϑ in Figure 3. We can see that the
thimble wraps around the branch points at −2 and−1 and then tends to inﬁnity along lines
parallel to those predicted by Equation ( 33).
Figure 3. This ﬁgure depicts in orange the analytic continuation of the set
C(−5/6,0),ϑ for ϑ = 1.6650 and ( A, B) = (1 , 2). The blue lines are parallel to the
lines
√
−ieiϑ and
√
ieiϑ. The red crosses are the branch points of V .
Lemma 2.2 gives a complete description of the thimbles outside a compact set (d epend-
ing on ϑ). Next we study the behaviour of the thimbles inside the compact se t given by
Corollary 2.3 (speciﬁcally the constant M from Lemma 2.2). This will be described in the
following sections.
