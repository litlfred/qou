---
doc_id: arxiv-math-0605314v1
doc_title: "A UNIFIED WITTEN-RESHETIKHIN-TURAEV INV ARIANT FOR INTEGRAL HOMOLOGY SPHERES KAZUO HABIRO"
section_id: sec-059-30-kazuo-habiro
section_title: "KAZUO HABIRO"
section_number: 30
pages: 30-31
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
doc_brief: "A UNIFIED WITTEN-RESHETIKHIN-TURAEV INVARIANT FOR INTEGRAL HOMOLOGY SPHERES KAZUO HABIRO — W e construct an invariant JM of integral homology spheres M with values in a completion ˆZ[q] of the"
---
Proof of Theorem 8.2. We may assume k1 =k = max(k1,... ,k m) without loss of
generality. (Otherwise, change the order of components of L.) Choose a bottom
tangle T∈ BTm such that cl(T ) = L. By Proposition 8.6,
JL(x1,... ,x m) = (tr x1
q ⊗···⊗ trxm
q )(JT ) = tr x1
q (y),
where we set y = (1⊗ trx2
q ⊗···⊗ trxm
q )(JT ), which is contained Z( ˜U ev
q ) by Propo-
sition 8.6. By the arguments in Section 4.4,
y =
∑
p≥0
apσp,
where ap∈ Z[q,q −1] for p≥ 0. Moreover, we have
x1 =
N∑
p=k
bp ˜P ′
p,
where bp∈ Z[q,q −1] and N≥k. Therefore, we have
trx1
q (y) =
N∑
p=k
apbptr
˜P ′
p
q (σp).
By Proposition 6.3, we have tr
˜P ′
p
q (σp)∈ {2p+1}q,p +1
{1}q
Z[q,q −1], hence the assertion.
8.4. Proof of Lemma 8.5. To prove Proposition 8.5, we need some lemmas.
Lemma 8.7. If y,y ′∈R Q(v) and x∈Uh, then we have
tryy ′
q (x) =
∑
try
q (x(1))try′
q (x(2)),
where ∆( x) = ∑ x(1)⊗x(2).
Proof. The assertion follows from the well-known identity for any two ﬁnite-dimensional
representationsW,W ′
trW ⊗W ′
q (x) = (tr W
q ⊗ trW ′
q )∆( x).
Lemma 8.8. (1) Ifn,l,l ′≥ 0,l⁄=l′ andj∈ Z, then we have trPn
q ( ˜F (l)K 2jel′
) = 0 .
(2) If 0≤n<l and j∈ Z, then we have trPn
q ( ˜F (l)K 2jel) = 0 .
(3) If 0≤l≤n and j∈ Z, then we have
trPn
q ( ˜F (l)K 2jel) = vnq−nj+2lj+l2 −ln{n}q!{n−l}q!
[ j +n− 1
n−l
]
q
[ j− 1
n−l
]
q
.(8.6)
Proof. The assertion (1) follows from the fact that l⁄= l′ implies that ˜F (l)K 2jel′
acts nilpotently on each Vn, n≥ 0.
The assertion (2) follows from the fact that Pn is a linear combination of V0,... , Vn,
and that if 0 ≤n<l , then el acts as 0 on V0,... , Vn.
We prove (3) by induction on n. The case n =l = 0 follows from
trP0
q (K 2j) = ǫ(K 2j) = 1.
A UNIFIED WITTEN-RESHETIKHIN-TURAEV INV ARIANT 31
Let n≥ 1. Set pn = V1−v2n−1−v−2n+1, so that Pn = Pn−1pn. Using Lemma
8.7, we have
trPn
q ( ˜F (l)K 2jel) = tr Pn−1pn
q ( ˜F (l)K 2jel) =
∑
trPn−1
q (x(1))trpn
q (x(2)),(8.7)
where ∑
x(1)⊗x(2) = ∆( ˜F (l)K 2jel)
=
l∑
r=0
l∑
s=0
[
l
s
]
q
( ˜F (l−r)K rK 2jel−sK s⊗ ˜F (r)K 2jes).
Sincepn is a linear combination of V0 and V1, we have tr pn
q (F (r)K 2jes) = 0 unless
(r,s ) = (0, 0) or (1, 1). Therefore, the right-hand side of (8.7) equals
trPn−1
q ( ˜F (l)K 2jel)trpn
q (K 2j) +q−l+1[l]qtrPn−1
q ( ˜F (l−1)K 2j+2el−1)trpn
q ( ˜F (1)K 2je).
(8.8)
By straightforward computation,
trpn
q (K 2j) = v−2j+1{j−n}q{j +n− 1}q,
trpn
q ( ˜F (1)K 2je) = v2j+1{1}q.
Using these identities and the inductive hypothesis, we can verify that (8.8) equals
the right-hand side of (8.6). This completes the proof.
Proof of Lemma 8.5. It suﬃces to prove that if n≥ 0 and x∈U ev
q , then we have
trP ′
n
q (x)∈ v
1
2 n(n−1)Z[q,q −1]. We may assume without loss of generality that x =
˜F (l)K 2jek with j ∈ Z, k,l ≥ 0. By Lemma 8.8, tr Pn
q (x)∈ vn{n}q!Z[q,q −1] =
v
1
2 n(n−1){n}!Z[q,q −1]. Therefore, we have the assertion.
