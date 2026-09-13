---
doc_id: arxiv-2103.07383v1
doc_title: "On the Analyticity of Critical Points of the Generalized Integral Menger Curvature in the Hilbert Case"
section_id: sec-001-3-estimate-of-the-main-term-qp
section_title: "Estimate of the main term Q(p)"
section_number: 3
pages: 7-9
source_pdf: 2103.07383v1.pdf
source_sha256: 9dca35ea16490ad8
doc_brief: "On the Analyticity of Critical Points of the Generalized Integral Menger Curvature in the Hilbert Case — We prove the analyticity of smooth critical points for generalized integral Menger cur- vature"
---
Next we investigate the order of the main termQ(p), for which we need to examine itsL2-
representation ﬁrst.
Lemma 3.1. Let p∈( 7
3, 8
3), s≥0 and γ∈H3p−4+s(R/Z, Rn) be parametrized by arc-length.
Then, there is⟨Q(p)(γ)∈Hs(R/Z, Rn) such that for allh∈H
3
2p−2(R/Z, Rn),
Q(p)(γ,h) =

R/Z
⟨
⟨Q(p)(γ)(u),h (u)
⟩
du.
In particular,⟨Q(p) mapsC∞(R/Z, Rn) into itself. The Fourier coeﬃcients of⟨Q(p), for allk∈Z,
are given by
ˆ⟨Q(p)(γ)(k) =q(p)
k |k|3p−4ˆγ(k).
The constantsq(p)
k are bounded independently ofn, and satisfy
0≤q(p)
k =c +o(1)
as|k|→∞for c> 0.
Proof. By [BR15, Proposition 4.1], we have
Q(p)(γ,h) =
∑
k∈Z
ϱk
⟨
ˆγ(k), ˆh(k)
⟩
Cn
, where ϱk =c|k|3p−4 +o(|k|3p−4) as|k|→∞,
for anyh∈H
3
2p−2(R/Z, Rn). In particular, theϱk are independent ofn, cf. their deﬁnition in
the proof of [BR15, Proposition 4.1]. Settingq(p)
k :=|k|4−3pϱk, which implies that theq(p)
k are
also independent ofn, we obtain
(1 +k2)
s
2
⏐⏐q(p)
k |k|3p−4ˆγ(k)
⏐⏐= (1 +k2)
s
2|c +o(1)||k|3p−4|ˆγ(k)|
≤(1 +k2)
s
2 ˜c|k|3p−4|ˆγ(k)|≤˜c(1 +k2)
3p−4+s
2 |ˆγ(k)|as|k|→∞
for some ˜c > 0. The right hand side, taken as a sequence ink∈Z, is in𝓁2(Z) because γ∈
H3p−4+s(R/Z, Rn), see [Tay96, Chapter 4, (3.8)], and so⟨Q(p)(γ), the inverse Fourier transform
7
ofq(p)
k |k|3p−4ˆγ(k), is well-deﬁned and inHs(R/Z, Rn). Allq(p)
k |k|3p−4 are real asQ(p) maps real
functions to real numbers andˆγ(k) = ˆγ(−k) due to the real image ofγ. Thus, ⟨Q(p)(γ)(u) =∑
k∈Zq(p)
k |k|3p−4ˆγ(k)e−2πiku= ˆγ(0) +∑
k∈Nq(p)
k |k|3p−4ℜ(ˆγ(k)e−2πiku) for almost allu∈R/Z
meaning that⟨Q(p)(γ) maps into the real numbers.
By Parseval’s relation [Gra14, Proposition 3.2.7 (3)], we have

R/Z
⟨
⟨Q(p)(γ)(u),h (u)
⟩
du =
∑
k∈Z
⟨
q(p)
k |k|3p−4ˆγ(k), ˆh(k)
⟩
Cn
=
∑
k∈Z
ϱk
⟨
ˆγ(k), ˆh(k)
⟩
Cn
=Q(p)(γ,h).
Remark 3.2. Assuming C5-regularity ofγ, one may explicitly calculate
⟨Q(p)(γ)(u) :=

D
|v−w|−p|v|2−p|w|2−p·
( ∆−w,0γ
−w −∆ w,0γ
w
w +
∆−v,0γ
−v −∆ v,0γ
v
v
+
∆ v,0γ
v −∆ v−w,−wγ
v
w +
∆ w,0γ
w −∆ w−v,−vγ
w
v
(
dw dv.
The proof works via ﬁrst restricting to the case|v|,|w|> εto obtain the formula and then
showing existence forε= 0 by means of several Taylor approximations. Since this method is
quite technical and long, we choose to omit it here.
From the previous Lemma 3.1, we deduce the following indispensable corollary regarding the
order of the main termQ(p).
Corollary 3.3. Given real numbersp∈( 7
3, 8
3) andm≥0, there exists a constant⟨C = ⟨C(p)> 0
such that for all curvesγ∈C∞(R/Z, Rn) and integersl≥0
‖γ(l+3)‖H m+3p−7≤⟨C‖∂l⟨Q(p)(γ)‖H m
holds.
Proof. By applying Lemma 3.1, well-known properties of Fourier coeﬃcients and the elementary
estimate (1 +k2)3p−7≤(2|k|)2(3p−7) for anyk∈Z\0, we get
‖∂l⟨Q(p)(γ)‖2
H m =
∑
k∈Z
(1 +|k|2)m|ˆ∂l⟨Q(p)(γ)(k)|2
=
∑
k∈Z
(1 +|k|2)m(2π|k|)2l|ˆ⟨Q(p)(γ)(k)|2
=
∑
k∈Z
(1 +|k|2)m(2π|k|)2l(q(p)
k )2|k|2(3p−4)|ˆγ(k)|2
≥inf
k∈Z\0
{(q(p)
k )2(2π)−622(7−3p)}
∑
k∈Z
(1 +|k|2)m+3p−7(2π|k|)2(l+3)|ˆγ(k)|2
= ⟨C−2∑
k∈Z
(1 +|k|2)m+3p−7|ˆγ(l+3)(k)|2
= ⟨C−2‖γ(l+3)‖2
H m+3p−7,
where ⟨C := infk∈Z\0{|q(p)
k |(2π)−327−3p}−1 is a positive constant only depending onp. In partic-
ular, independence ofn follows from Lemma 3.1.
8
