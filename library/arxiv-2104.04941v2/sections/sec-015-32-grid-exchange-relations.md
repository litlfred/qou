---
doc_id: arxiv-2104.04941v2
doc_title: "FOCK–GONCHAROV COORDINATES FOR SEMISIMPLE LIE GROUPS S. GILLES"
section_id: sec-015-32-grid-exchange-relations
section_title: "Grid exchange relations"
section_number: 3.2
pages: 14-15
source_pdf: 2104.04941v2.pdf
source_sha256: 84426ed37754aa78
doc_brief: "FOCK–GONCHAROV COORDINATES FOR SEMISIMPLE LIE GROUPS S. GILLES — Fock and Goncharov [FG06b] introduced cluster ensembles, p roviding a framework for coordi- nates on varieties of surface"
---
justify the exchange relations of µrotTw and~µFlipcore, and to prove Lemmas 7.4 and 7.6:
Theorem 3.5 ([FZ99, Theorem 1.17]) . For u,v two words in the Weyl group W such that length(usi) =
length(u) + 1 and length(vsi) = length(v) + 1, and A the Cartan matrix,
∆ uωi,vωi ∆ usiωi,vsiωi = ∆ usi ωi,vωi∆ uωi,vsiωi +
∏
j⁄=i
(∆ uωj ,vωj )−Aj,i.
Remark 3.6. It appears that this theorem only allows us to adjust the mino r coordinates by one letter at
a time: si. By the same logic as Remark 2.20, however, we actually are ab le to adjust u and v by longer
sequences of letters, as long as they do not contain multiple si.
We use this theorem in situations where, mutating at va,b,
∆ usiωi,vsiωi = Coordinate of va,b before mutation
∆ uωi,vωi = Coordinate of va,b after mutation
∆ uωi,vsiωi = Coordinate to left of va,b
∆ usiωi,vωi = Coordinate to right of va,b
∆ uωj ,vωj = Coordinates in same column as va,b
14
Example 3.7. We look ahead to the results of Section 5 and assume all edge co ordinates are 1 for simplicity.
Figure 9 depicts QC4 partway through the rotation mutation. The minors associat ed to relevant coordinates
(see the proof of Lemma 7.4 for details) are at this point
v22 : ∆ w1ω2,w10ω2 = ∆ w3s2ω2,w11s2ω2
v21 : ∆ w5ω2,w10ω2 = ∆ w3ω2,w11s2ω2
v23 : ∆ w1ω2,w14ω2 = ∆ w3s2ω2,w11ω2
v12 : ∆ w5ω1,w13ω1 = ∆ w3ω1,w11ω1
v32 : ∆ w1ω3,w11ω3 = ∆ w3ω3,w11ω3
v11v12v13
v21v22v23
v31v32v33
v41v42v43
B1
B2
B3
B4
C1
C2
C3
C4
A1A2A3A4
Figure 9. After applying µ {v11,v 21,v 31,v 41,v 12 } to QC4. The next mutation in µrot is
at v22.
The equality follows from Remark 2.20. Therefore, by applyi ng the identity we see that mutating at v22
will change the coordinate to ∆ w3ω2,w11ω2 = ∆ w6ω2,w14ω2 .
Finally, we note that the requirements on u and v may be loosened, which we need to prove Lemma 7.6.
Lemma 3.8. Even if length(usi) ⁄= length(u) + 1 or length(vsi) ⁄= length(v) + 1, the result of Theorem 3.5
still holds as long as u and v are subwords of a repeated Coxeter element c.
Proof. From the proof in [FZ99], the only reason for the length condi tion is to ensure that vsi = vsi (and
similar for u), since the lifting is not quite a homomorphism: for example sisi ⁄=e.
However, the only situations in which multiplication is not preserved is when the multiplication by si
induces a length-shortening identity in W . But if u andv are subwords of a repeated Coxeter element, their
suﬃxes will always be of the form wk. These admit no length-shortening braid relations.
So the only possibility for vsi ⁄=vsi is if vsi contains a copy of w0 =ch/2. But ch =sG is an element of
H. By prepending copies of ch to either u or v, we may ensure that the diﬀerence in length between u and
v is never more than h
2 − 1. Then, using
∆ wuωi,wvω i(g) = ∆ uωi,vωi (w−1gw)
we reduce to the case where u and v are each some wk shorter than w0. By replacing g with wgw −1sǫ
G
(where ǫ ∈ 0, 1 depending on the exact diﬀerence between u and v), the desired identity follows from the
regular theorem. □
