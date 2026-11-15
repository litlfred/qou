---
doc_id: arxiv-math-0605314v1
doc_title: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres"
section_id: sec-031-83-proof-of-theorem
section_title: "Proof of Theorem"
section_number: 8.3
pages: 29-30
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
toc_source: inferred
doc_brief: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres — We construct an invariant JM of integral homology spheres M with values in a completion d Z[q] of the polynomial ring"
---
tion.
Lemma 8.5. If x ∈Uev
q
and y ∈P, then we have try
q(x) ∈Z[q, q−1].
Using Lemma 8.5, we obtain the following generalization of (4.2).
Proposition 8.6. If T is an m-component, algebraically-split, 0-framed bottom
tangle, and if x2, . . . , xm ∈P, then we have
(1 ⊗trx2
q ⊗· · · ⊗trxm
q
)(JT ) ∈Z( ˜Uev
q ).
Proof. By Lemma 8.5,
(1 ⊗trx2
q ⊗· · · ⊗trxm
q
)((Uev
q )⊗m) ⊂Uev
q .
(8.3)
Let N ≥0 be such that
x2, . . . , xm ∈SpanQ(v){P ′
0, P ′
1, . . . , P ′
N} = SpanQ(v){V0, V1, . . . , VN}.
(8.4)
If p > N then we have trxi
q (Fp(Uev
q )) = 0 for i = 2, . . . , m, since ep acts as zero on
V0, V1, . . . , VN. Therefore, we have
(1 ⊗trx2
q ⊗· · · ⊗trxm
q
)(Fp((Uev
q )⊗m)) ⊂Fp(Uev
q ).
(8.5)
Now, (8.3), (8.5) and Theorem 4.1 imply the assertion.
30
KAZUO HABIRO
Proof of Theorem 8.2. We may assume k1 = k = max(k1, . . . , km) without loss of
generality. (Otherwise, change the order of components of L.) Choose a bottom
tangle T ∈BTm such that cl(T ) = L. By Proposition 8.6,
JL(x1, . . . , xm) = (trx1
q ⊗· · · ⊗trxm
q
)(JT ) = trx1
q (y),
where we set y = (1 ⊗trx2
q ⊗· · · ⊗trxm
q
)(JT ), which is contained Z( ˜Uev
q ) by Propo-
sition 8.6. By the arguments in Section 4.4,
y =
X
p≥0
apσp,
where ap ∈Z[q, q−1] for p ≥0. Moreover, we have
x1 =
N
X
p=k
bp ˜P ′
p,
where bp ∈Z[q, q−1] and N ≥k. Therefore, we have
trx1
q (y) =
N
X
p=k
apbptr
˜
P ′
p
q (σp).
By Proposition 6.3, we have tr
˜
P ′
p
q (σp) ∈{2p+1}q,p+1
{1}q
Z[q, q−1], hence the assertion.
