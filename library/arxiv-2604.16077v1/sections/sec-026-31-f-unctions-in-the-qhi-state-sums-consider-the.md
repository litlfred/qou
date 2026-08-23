---
doc_id: arxiv-2604.16077v1
doc_title: "VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INVARIANTS: THE FIGURE EIGHT KNOT COMPLEMENT"
section_id: sec-026-31-f-unctions-in-the-qhi-state-sums-consider-the
section_title: "F unctions in the QHI state sums. Consider the rational functions ωN (.,. |n),n ∈ N,"
section_number: 3.1
pages: 20-22
source_pdf: 2604.16077v1.pdf
source_sha256: 2f1140b9d5fee38a
doc_brief: "VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INVARIANTS: THE FIGURE EIGHT KNOT COMPLEMENT — We compute the real part of the semi-classical limit of the se quence of quantum hyperbolic invariants (QHI) of"
---
deﬁned on the curve FN := {(x,y ) ∈ C2| xN +yN = 1} by
(46) ωN (x,y |0) = 1 , ωN (x,y |n) =
n∏
j=1
y
1 −xζj if n ≥ 1.
Since (1 −x)(1 −xζ)... (1 −xζN −1) = 1 −xN =yN , we have
ωN (x,y |N +n) = ωN (x,y |n).
These functions are closely related to Faddeev’s [28, 29] non compact quantum dilogarithm
Φb, and therefore to the classical Euler dilogarithm Li 2. The function Φ b is deﬁned as follows;
it can be regarded as a kind of double Barnes’ sine function ([ 31]). Let b ∈ C be such that
R(b) ⁄= 0. Deﬁne
√
ℏ := 1
b + b−1.
VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INV ARIANTS 21
Denote by R +i0 the real axis directed from −∞ to ∞, slightly deformed near 0 so as to
pass above 0. Then Φ b is the holomorphic function deﬁned in the strip |I(z)| < |I(i/2
√
ℏ)|
by the integral formula
(47) Φ b(z) = exp
(1
4
∫
R+i0
e−2izw dw
w sinh(bw) sinh(b−1w)
)
.
Denote by Log(Φ b(z)) the integral on the RHS. It satisﬁes the functional equati on
(48) Log
(
Φb
(
z −i b±1
2
))
= Log
(
Φb
(
z +i b±1
2
))
+ Log(1 +e2πb±1z).
Therefore Φ b can be extended to a meromorphic function of z ∈ C, satisfying the functional
equation
(49) Φ b
(
z −i b±1
2
)
= (1 + e2πb±1z)Φb
(
z +i b±1
2
)
.
The poles and zeros of Φ b are the pointsz = i
2
√
ℏ +mib+nib−1 andz = −( i
2
√
ℏ +mib+nib−1)
respectively, where m,n ∈ N.
We will use the following version of Φ b. Let b = 1√
N , and set
(50) ˆSN (z) := Φ 1√
N
(√
N
2π
(
z −i(π − π
N )
) )
.
Denote by Log( ˆSN (z)) the integral obtained from the one in (47) by the change of v ariable
in (50). Then Log( ˆSN (z)) is a holomorphic function of z in the strip − 2π
N < I(z)< 2π, and
it satisﬁes the functional equation
(51) Log( ˆSN (z)) = Log( ˆSN (z + 2iπ
N )) + Log(1 −ez+ 2iπ
N ).
Therefore it can be extended to an analytic function on C with cuts [0 , +∞[+i(2π + 2πp
N ),
p ∈ N, and [0, +∞[−i(l + 1) 2π
N , l ∈ N. All this implies that ˆSN is holomorphic and without
zeros in the strip − 2π
N < I(z)< 2π, it satisﬁes the functional equation
(52) ˆSN (z) = ˆSN (z + 2iπ
N )(1 −ez+ 2iπ
N ),
and it can be extended to a meromorphic function on C with sets of poles and simple poles
(53) P = {2iπ +i 2pπ
N , p ∈ N}, P1 = {2iπ +i 2pπ
N , p ∈ {0,...,N − 1}}
respectively, and zeroes
Z = {−(l + 1)i 2π
N, l ∈ N}.
Moreover the functional equation (52) yields
(54) ωN (ez,y |n) =
n∏
j=1
y
1 −ezζj =yn ˆSN (z + 2niπ/N)
ˆSN (z)
for every y,z ∈ C such that yN = 1 −eNz . The function Φ b has a number of remarkable
properties, see [29, 1]. In particular, its ”semi-classica l limit”, as b → 0+, recovers the Euler
dilogarithm function (see [63] and Lemma 3.3 below),
(55) Li 2(x) = −
∫ x
0
Log(1 −t)
t dt, x ∈ C \ [1, +∞[.
Basically, the connection between the two functions can be g uessed by comparing the formula
(47) with the following integral representation. It is well -known, but we recall a proof for it
is short and illuminating.
