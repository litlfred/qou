---
doc_id: arxiv-0908.3425v1
doc_title: "Chiral Perturbation Theory: Introduction and Recent Resul ts in the One-Nucleon Sector S. Scherer"
section_id: sec-034-master-integral
section_title: "Master integral"
section_number: null
pages: 59-60
source_pdf: 0908.3425v1.pdf
source_sha256: 5e88d45bbc1c1b9b
doc_brief: "Chiral Perturbation Theory: Introduction and Recent Resul ts in the One-Nucleon Sector S. Scherer — We provide an introduction to the basic concepts of chiral pe rturbation theory and discuss some"
---
We have seen that the modiﬁed minimal subtraction scheme ~MS does not produce the desired power
counting. We will discuss the power-counting problem in ter ms of the dimensionally regularized one-loop
integral
H(p2,m 2,M 2;n) ≡ − i
∫ dnk
(2π)n
1
[(k −p)2 −m2 +i0+](k2 −M 2 +i0+)
= −i
∫ dnk
(2π)n
1
[k2 − 2p ·k + (p2 −m2) +i0+](k2 −M 2 +i0+). (214)
We are interested in nucleon four-momenta close to the mass- shell condition, p2 ≈m2, counting p2 −m2
as O(q) and M 2 as O(q2). In order to conform with Ref. [Becher and Leutwyler, 1999] , we have omitted
the factor µ4−n and have reversed the overall sign in comparison with our pre vious deﬁnition of IN π. Let
us turn to the discussion of H(p2,m 2,M 2;n). To that end, we make use of the Feynman parametrization
1
ab =
∫ 1
0
dz 1
[az +b(1 −z)]2 (215)
witha = (k −p)2 −m2 +i0+ andb =k2 −M 2 +i0+, interchange the order of integrations, and perform
the shift k →k +zp, to obtain
H(p2,m 2,M 2;n) = −i
∫ 1
0
dz
∫ dnk
(2π)n
1
[k2 −A(z) +i0+]2,
where
A(z) = z2p2 −z(p2 −m2 +M 2) +M 2.
Making use of
∫ dnk
(2π)n
(k2)p
(k2 −A)q = i(−)p−q
(4π)
n
2
Γ
(
p + n
2
)
Γ
(
q −p − n
2
)
Γ
(
n
2
)
Γ(q)
Ap+ n
2 −q
with p = 0 and q = 2, we ﬁnd
H(p2,m 2,M 2;n) = 1
(4π)
n
2
Γ
(
2 −n
2
)∫ 1
0
dz[A(z) −i0+]
n
2 −2. (216)
The relevant properties can nicely be displayed at the thres hold p2
thr = (m + M)2, where A(z) =
[z(m +M) −M]2 is particularly simple. The small imaginary part can be drop ped in this case, because
A(z) is never negative. Splitting the integration interval int o [0,z 0] and [z0, 1] with z0 =M/(m +M),
we have, for n> 3,
∫ 1
0
dz[A(z)]
n
2 −2 =
∫ z0
0
dz[M −z(m +M)]n−4 +
∫ 1
z0
dz[z(m +M) −M]n−4
= 1
(n − 3)(m +M) (M n−3 +mn−3),
yielding, through analytic continuation, for arbitrary n
H((m +M)2,m 2,M 2;n) =
Γ
(
2 − n
2
)
(4π)
n
2 (n − 3)
(
M n−3
m +M + mn−3
m +M
)
. (217)
The ﬁrst term, proportional to M n−3, is deﬁned as the so-called infrared singular part I. Since M → 0
impliesp2
thr →m2 this term is singular for n ≤ 3. The second term, proportional to mn−3, is deﬁned as
the infrared regular part R. Note that for non-integer n the infrared singular part contains non-integer
powers of M, while an expansion of the regular part always contains non- negative integer powers of M
only.
59
