---
doc_id: ant-v14-n7-s-p06
doc_title: "Moments of quadratic twists of elliptic curve L-functions over function ﬁelds"
section_id: sec-009-2-vuv-m
section_title: "V(u,v, m)"
section_number: 2
pages: 21-22
source_pdf: ant-v14-n7-s-p06.pdf
source_sha256: 4881141ef679dd5a
doc_brief: "Moments of quadratic twists of elliptic curve L-functions over function fields — 24 sections: Introduction and statement of resu; L′(; Some useful lemmas"
---
)
uniformly for|α|,|β|≤ 1/g, where M(u,v, m) and V(u,v, m) are given by (4-9) and (4-11) respectively.
Remark 4.2. Note that the same upper bound as above holds if we replace L(E⊗χD,w) with
L(E⊗χD𝓁,w) for a ﬁxed polynomial 𝓁 with (𝓁,1)= 1. Since the proof of the upper bound for
this twisted moment is the same as the proof of Theorem 4.1, we only focus on 𝓁= 1.
We ﬁrst need the following proposition, whose proof is similar to the proof of Theorem 3.3 in [Altu ˘g
and Tsimerman 2014].
Proposition 4.3. Let D∈ H∗
2g+1 and let m= deg(L(E⊗χD,w)) . Then for h≤ m and z withℜ(z)≥ 0
we have
log
⏐⏐L
(
E⊗χD, 1
2+ z
)⏐⏐≤ m
h+ 1
hℜ
( ∑
j≥1
deg(P j)≤h
χD(P j)(α( P) j+β( P) j) log qh− j deg(P)
|P| j(1/2+z+1/(h log q)) log q j
)
.
Proof. We write
L(E⊗χD, s)=
m∏
j=1
(1−α jq1/2−s),
where|α j|= 1 (see [Hall et al. 2017]). Then
L′
L(E⊗χD, s)= log q
(
−m
2+
m∑
j=1
( 1
1−α jq1/2−s− 1
2
))
. (4-1)
1874 Hung M. Bui, Alexandra Florea, Jonathan P. Keating and Edva Roditty-Gershon
We put s=σ+ z and integrate (4-1) with respect toσ from 1
2 toσ0, whereσ0> 1
