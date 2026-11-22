---
doc_id: arxiv-hep-th-9506138v1
doc_title: "Black Hole Complementarity vs. Locality"
section_id: sec-008-a2-correspondence-with-low-energy-minkowski-fiel
section_title: "Correspondence with Low Energy Minkowski Field Theory"
section_number: A.2
pages: 19-22
source_pdf: 9506138v1.pdf
source_sha256: bb85afba0530402c
toc_source: inferred
doc_brief: "Black Hole Complementarity vs. Locality — 18 sections: Front matter; Introduction; The Nice-Slice Argument"
---
Local quantum ﬁeld theory in Minkowski space provides a very good description of
the low-energy world we observe, and any uniﬁed theory should reproduce the structure of
local Minkowski ﬁeld theory for kinematic situations appropriate to low-energy Minkowski
observers. This structure includes the requirement that the commutator of gauge-invariant
local ﬁelds must vanish at spacelike separation. In this section, we show that the low-energy
ﬁelds obtained from light-front string ﬁeld theory satisfy this requirement.
Consider a Minkowski observer, whose measuring apparatus is sensitive to frequencies
of order E ≪1/
√
α′. Such an observer will describe physics by a set of low-energy ﬁelds
ˆφA(x), which can be obtained from the component ﬁelds φA of light-front string ﬁeld theory
by integrating φA(y) against a test function f(x −y). The Fourier components ˜f(q) of f
have support only for qµ <∼E.
Let us consider the vector ﬁeld, which clearly enters the low-energy Minkowski theory.
The interaction picture vector ﬁeld is expanded as
Ab
µ(x) =
24
X
λ=1
Z
dD−2p
(2π)D−2
Z
dp+
4πp+

ǫµ(λ) a(p+,⃗p, λ, b) eip·x + h. c.

,
(A.16)
where the ǫµ(λ) are polarization vectors which correspond to the polarization states λ and
b is the relevant group index. In the light-front gauge, A+ = 0, and A−is expressed as a
nonlocal function of the D −2 transverse components Ai. The commutation relations for
A−will therefore be nonlocal even in free ﬁeld theory. For this reason, we restrict ourselves
to commutators of the transverse ﬁelds, which do vanish in free ﬁeld theory. The matrix
element involving massless vectors can now be calculated using equation (A.12), and we
obtain
⟨0|[ ˆAa
i (x1), ˆAb
j(x2)]|3, c⟩= (2π)D−1gf abc
 2
Y
r=1
Z
dD−2pr
(2π)D−2
Z ∞
−∞
dαr
4π|αr|
!
× F(α1, α2)
P3
r=1 p−
r
δ
 3
X
r=1
αr

δD−2 3
X
r=1⃗
pr

˜V1(1, i; 2, j; 3) eip1·x1+ip2·x2
×
h
˜f1(−p2 −p3) ˜f2(p2)e−ix+
1
P3
r=1 p−
r −˜f1(p1) ˜f2(−p1 −p3)e−ix+
2
P3
r=1 p−
r
i
.
(A.17)
Consider the ﬁrst term in the square brackets. The function ˜f2 constrains pµ
2 ∼E, and the
function ˜f1 constrains the sum pµ
2 + pµ
3 ∼E, which implies that pµ
3 ∼E as well. A similar
argument holds for the second term. In other words, the commutator of two low-energy
operators is itself a low-energy operator, and does not couple to states of high energy.
Therefore, for the matrix element (A.17) to be non-negligible, the state |3, c⟩must be a
low-energy state, which we will select to be a vector boson polarized along the k direction.
The three vector boson vertex is
˜V1(1, i; 2, j; 3, k) =

δij
Pk
α3
+ δjk
Pi
α1
+ δki
Pj
α2
+ 2α′ PiPjPk
α1α2α3

exp
τ0
2
3
X
r=3
p−
r

,
(A.18)
where⃗P = α1⃗p2 −α2⃗p1 is cyclically symmetric. We can now substitute this expression
into equation (A.17).
Since the test functions restrict the allowed momenta to be of order E ≪1/
√
α′,
we keep only the leading terms in α′. The only dependence on α′ comes from the vertex
(A.18), both from the explicit dependence shown and through τ0, which is properly written
τ0 = α′
3
X
r=3
αr log(α′α2
r) .
(A.19)
Dropping the test functions, the leading term of the commutator is
⟨0|[ ˆAa
i (x1), ˆAb
j(x2)]|3, c, k⟩= (2π)D−1gf abc
 2
Y
r=1
Z
dD−2pr
(2π)D−2
Z ∞
−∞
dαr
4π|αr|
!
× F(α1, α2)
P3
r=1 p−
r
δ
 3
X
r=1
αr

δD−2 3
X
r=1⃗
pr

eip1·x1+ip2·x2
×

δij
Pk
α3
+ δjk
Pi
α1
+ δki
Pj
α2
 h
e−ix+
1
P3
r=1 p−
r −e−ix+
2
P3
r=1 p−
r
i
.
(A.20)
which is the same result as that obtained from Yang-Mills theory in the light-front gauge.
The commutator (A.20) does not vanish for x1 −x2 spacelike, because the integrand
is nonpolynomial in the longitudinal momenta αr.
This does not violate the rules of
local ﬁeld theory, however, because the ﬁelds Aa
i are not gauge invariant. It is only the
commutators of gauge invariant local ﬁelds, such as trF 2, which are required to vanish
when the arguments of the ﬁelds are spacelike related. This ensures that a gauge invariant
signal cannot propagate faster than the speed of light.
What we have shown is that
the commutator of low-energy gauge ﬁelds obtained from light-front string ﬁeld theory
is exactly the same as that predicted by low-energy ﬁeld theory.
In other words, the
commutator of low Minkowski energy ﬁelds does not acquire any additional nonlocality in
string theory. Therefore, one may construct the usual gauge invariant ﬁelds from the Aa
µ,
and they will commute at spacelike separations.
Light-front string ﬁeld theory has thus passed an important test.
Had we found
that light-front string ﬁeld theory introduces additional nonlocality into the commutator
of low-energy ﬁelds, it would have indicated a catastrophic breakdown in the low-energy
predictions of the theory, and the commutator (and perhaps the theory itself) could not
be taken seriously. As it stands, the theory avoids introducing any additional nonlocality
at low energy, and we can proceed to study the predictions it makes for higher energy.
