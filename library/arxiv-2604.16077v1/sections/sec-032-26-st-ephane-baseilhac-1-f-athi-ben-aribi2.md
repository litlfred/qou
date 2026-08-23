---
doc_id: arxiv-2604.16077v1
doc_title: "VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INVARIANTS: THE FIGURE EIGHT KNOT COMPLEMENT"
section_id: sec-032-26-st-ephane-baseilhac-1-f-athi-ben-aribi2
section_title: "ST ´EPHANE BASEILHAC 1, F ATHI BEN ARIBI2"
section_number: 26
pages: 26-27
source_pdf: 2604.16077v1.pdf
source_sha256: 2f1140b9d5fee38a
doc_brief: "VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INVARIANTS: THE FIGURE EIGHT KNOT COMPLEMENT — We compute the real part of the semi-classical limit of the se quence of quantum hyperbolic invariants (QHI) of"
---
·
0
·
2iπ
U
·
−c +iK
·−c +i
(
2π − (α + 1)π
N
)
·M +i
(
2π − (α + 1) π
N
)
·M +i(α − 1)π
N
·i(α − 1)π
N
·i
(
(α − 1)π
N + 2kπ
)
UM,α,k,K,c
Figure 2. The domain U and the sets UM,α,k,K,c .
(iii) The sequence of functions exp( 1
N ΨN ) converges uniformly to the constant function with
value 1 on compact subsets of U .
Remark 3.6. (i) The condition R(z)< −c for some c> 0 when 2π −(α+1) π
N ≤ I(z) ≤K is
in place to ensure that the half-space stays at distance from the singular points 2iπ + 2iπp/N,
p ∈ N, of Ψ N .
(ii) The proof below provides an explicit upper bound of | exp( 1
N ΨN )| on UM,α,k,K,c .
Proof. (i) Any point of R+i]0, 2π[ is contained in R+i]− π
N, 2π− π
N [ forN large enough, where
ΨN has the integral formula given by (62) and (59). By using Lemm a 3.2 and Lebesgue’s
dominated convergence theorem it is clear that the second su mmand in the formula (62)
converges simply on R +i]0, 2π[. Thus it remains to prove it also for Ξ N .
Recall the function ǫ in (59). It is easy to see that ǫ is holomorphic on R ∪D(0,R ), that
limx→0ǫ(x) = − 1
6 , and that there is a scalar σR > 0 such that |ǫ(x)| ≤ σR for all x ∈
Ω ∪D(0,R ) (see [11, pp. 364-365] for details). Let us split Ξ N (z) as
(64) Ξ N (z) =
∫
v∈Ω∩D(0,R)
ǫ
(v
N
) exp(−izv
π −v + v
N )
4 sinh(v) dv
+
∫
v∈]−∞,−R]
ǫ
(v
N
) exp(−izv
π −v + v
N )
4 sinh(v) dv +
∫
v∈[R,+∞[
ǫ
(v
N
) exp(−izv
π −v + v
N )
4 sinh(v) dv.
VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INV ARIANTS 27
Note that for all N the integrand is a holomorphic function of z and v. It has modulus less
than σR|
exp(−i zv
π −v+R)
4 sinh(v) | for v ∈ Ω ∩D(0,R ), where this function is continuous and hence
integrable. Now set z =x +iy, so that 0 <y < 2π. For a real v ⁄= 0 we have
⏐
⏐
⏐
⏐ǫ
(v
N
) exp(−izv
π −v + v
N )
4 sinh(v)
⏐
⏐
⏐
⏐ ≤σR
⏐
⏐
⏐
⏐
exp(−izv
π −v + v
N )
4 sinh(v)
⏐
⏐
⏐
⏐
=σR
exp(v(−1 + y
π + 1
N ))
4 sinh(v) .
Let c−,c + be positive real numbers such that 0 < c− < y
π < c+ < 2, and assume that N
is large enough so that y
π + 1
N < c+. Then the RHS is ≤ σR
exp(v(c+−1))
4 sinh(v) on [+R, +∞[ and
≤σR
exp(v(c−−1))
4 sinh(v) on [ −∞, −R[, where these functions are integrable on these intervals. Then
we can apply Lebesgue’s dominated convergence theorem to th e three integrals. By summing
the results we get
lim
N →+∞
ΞN (z) = − 1
6
∫
v∈Ω
exp(−izv
π −v)
4 sinh(v) dv,
The arguments above show also that the integral on the RHS is a holomorphic function of z
in the strip R +i]0, 2π[, which concludes the proof of (i).
(ii) First consider | exp( 1
N ΨN )| on ] − ∞,M ] +i] − π
N, 2π − π
N [. Let α> 0 be ﬁxed, and apply
(57) with δ of the form δN :=απ
N . For any z ∈] − ∞,M ] +i[δN − π
N, 2π −δN − π
N ], we ﬁnd
(65) 1
N |ΨN (z)| ≤ B′
απ + πeM/2
2απ
√
1 − π2
24
+ B′′
N ,
which is bounded from above by a constant independent of N . This proves the claim on the
strip (α − 1)π
N < I(z)< 2π − (α + 1)π
N .
Assume now that R(z) < 0. Denote by CM,α,B ′,B′′ the constant on the RHS of (65).
By repeated use of (51) we can shift z by −2iπ, thus getting R(Log( ˆSN (z − 2iπ))) =
R(Log( ˆSN (z))) +∑ N
k=1 Log|1 −ez+ 2iπ
N | = R(Log( ˆSN (z))) + Log|1 −eNz |. Then the diﬀerence
of (56) with the same identity where z is replaced by z − 2iπ has real part
(66) R(ΨN (z)) − R(ΨN (z − 2iπ)) = −N Log|1 −eNz |.
Therefore R (ΨN (z − 2iπ)) ≤ R (ΨN (z)) + N Log(1 + |eNz |) ≤ R (ΨN (z)) + N Log(2), and
hence | exp( 1
N ΨN (z))| = exp( 1
N R (ΨN (z))) ≤ exp(CM,α,B ′,B′′ +kLog(2)) for any z in a half-
strip ] − ∞, 0[+i(2πk′ + [δN − π
N, 2π −δN − π
N ]), where k ≤k′ ≤ 0.
To ﬁx the ideas take now for instance α := 1
