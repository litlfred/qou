---
doc_id: 4geo-dedi-rev
doc_title: "On the quantum Teichmüller invariants of fibred cusped 3-manifolds"
section_id: sec-021-on-the-quantum-teichm-uller-invariants-of-fibred
section_title: "ON THE QUANTUM TEICHM ¨ULLER INVARIANTS OF FIBRED CUSPED 3-MANIFOLDS (page 23)"
section_number: null
pages: 23-23
source_pdf: 4GEO-DEDI-REV.pdf
source_sha256: e4d52947b71a3f37
toc_source: inferred
doc_brief: "On the quantum Teichmüller invariants of fibred cusped 3-manifolds — 26 sections: Front matter; ON THE QUANTUM TEICHM ¨ULLER INVAR; ON THE QUANTUM TEICHM ¨ULLER INVAR"
---
22
ST´EPHANE BASEILHAC1, RICCARDO BENEDETTI2
Let us consider now Theorem 1.2. For the convenience of the reader we re-state it. We keep the
usual setting. Recall that Mφ is the interior of a compact manifold ¯
Mφ with boundary made by tori.
Second Main Theorem. There is a neighborhood of i∗(rh) in i∗(X0(Mφ)) ⊂X(S) such that:
(1) For any isomorphism class of local representations of Tq
S whose holonomy lies in this neighbor-
hood, there are:
• A representative ρ of the class, and representations ρλ, ρλ′ belonging to ρ and acting on
(CN)⊗2m,
• a layered QH triangulation (T,˜b, w) of Mφ such that Hred
N (T,˜b, w) = Hred
N (Mφ, r, κ), for some
weight κ ∈H1(∂¯
Mφ, C∗) and augmented character r of π1(Mφ) such that the restriction of r
to π1(S) is the holonomy of ρ,
such that the operator Hred
N (TCφ,˜b, w)T is a QHI intertwiner which intertwins ρλ and ρλ′ as in Propo-
sition 4.5. The load of ρ is determined by the values of the weight κ at the meridian curves that form
¯S ∩¯
Mφ.
(2) The family of QHI intertwiners {Hred
N (TCφ,˜b, w)T } consists of the QT intertwiners which inter-
twin ρλ to ρλ′ and whose traces are well deﬁned invariants of triples (Mφ, r, κ) such that the restriction
of r to π1(S) is the holonomy of ρ.
Proof. (1) Let ρ: Tq
λ →End((CN)⊗2m) be a local representation with parameters ({x(e)}e∈λ(1), h).
Recall Proposition 3.1 and the discussion that follows. Assume that the augmented character [(r, {ξΓ}Γ)]
associated to ρ lies in i∗(X0(Mφ)), and can be encoded by a system of shape parameters w ∈A0 ⊂A,
the simply connected open neighborhood of wh in G(T,˜b) chosen before Remark 3.4. Then we can lift
w to a system of quantum shape parameters w ∈A0,N, and using the QH-triangulation (TCφ,˜b, w),
we can deﬁne a local representation ρ′ : Tq
λ →End((CN)⊗2m) in the same way as ρ0 in the proof
of Proposition 4.5 (see (31)). It has quantum shear-bend coordinates x(e), e ∈λ(1), and parameters
({x(e)}e∈λ(1), h′), where h′ = Q
e∈λ(1) x(e). The system {x(e)}e∈λ(1) is the same for ρ and ρ′, so in order
that ρ′ ∼= ρ, it remains to show that we can choose w so that h′ = h. But (h′)N = Q
e∈λ(1) x(e) = hN,
so h′ = ζh for some N-th root of unity ζ. On the other hand, by Theorem 3.5 (1), at all the meridian
curves mj of ∂¯
Mφ we have
κN(w)(mj)N = ±a−2
j
where aj is deﬁned before the identity (22), and we note that a−2
j
is the dilation factor of the similarity
transformation associated to the conjugate of r(mj) ﬁxing ∞, whence the squared eigenvalue at mj
selected by [(r, {ξΓ}Γ)]. Hence
(h′)2N = a−2
1
. . . a−2
r
= ±κN(w)(m1)N . . . κN(w)(mr)N.
Moreover, there is w′ ∈A0,N so that κN(w′)(m1) . . . κN(w′)(mr) is any given N-th root of a−2
1
. . . a−2
r .
Let ζ′ be the N-th root of unity such that (h′)2 = ζ′κN(w)(m1) . . . κN(w)(mr). By using the formula
(6) it is easy to check that
(35)
κN(w)(mj) = (−q−1)tj
Y
e|pj∈∂e
W+(e)
where W+(e) is the lateral quantum shape parameter of (S, λ) at the edge e of λ, tj is the number
of spikes of the triangles of λ at the j-th puncture pj of S, and the product is over all the edges e,
counted with multiplicity, having pj as an endpoint. Recalling that there are 3m = −3χ(S) edges in
λ, we deduce
κN(w)(m1) . . . κN(w)(mr) = (−q−1)3.2m Y
e∈λ(1)
W+(e)2
(36)
= (−q−1)6m(−q)6m Y
e∈λ(1)
x(e)2 = (h′)2.
(37)
Hence ζ′ = 1. Then take w′ ∈A0,N so that κN(w′)(m1) . . . κN(w′)(mr) = (h′)2ζ−2. The load h′′
of the representation ρ′′ associated to w′ satisﬁes (h′′)2 = (h′)2ζ−2 = h2. Since N is odd, and again
(h′′)N = hN, eventually h = h′′. This achieves the proof of the claim (1) of the theorem.
