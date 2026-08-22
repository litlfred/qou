---
doc_id: arxiv-math-0605314v1
doc_title: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres"
section_id: sec-091-2-klkl1l4kl2k2
section_title: "(k−l)(k−l+1)−l−4kl+2k2"
section_number: 2
pages: 53-54
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
doc_brief: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres — W e construct an invariant JM of integral homology spheres M with values in a completion ˆZ[q] of the polynomial ring"
---
ϕ(ek ˜F (k)K −2k+2l)trx
q (ek−l ˜F (k)elK −2k)trx′
q ( ˜F (l)ek ˜F (k−l)K −2k).
Using the identity tr x
q (yy ′) = tr x
q (y′S2(y)) for y,y ∈Uh, we obtain
trx
q (ek−l ˜F (k)elK −2k)trx′
q ( ˜F (l)ek ˜F (k−l)K −2k)
=q−2k+2l+3kl+l2
[
k
l
]
q
trx
q ( ˜F (k)K −2kek)trx′
q ( ˜F (k)K −2kek).
54 KAZUO HABIRO
Now, set x =Pi and x′ =Pi′ . By Lemma 8.8, we have for i≥ 0
trPi
q ( ˜F (k)K −2kek) = δi,kvkq−k2
{k}q!.
Moreover, using (2.4), we obtain
ϕ(ek ˜F (k)K −2k+2l) = ϕ(ek ˜F (k))K −2k+2l ={H}q,kK −2k+2l.
Using the above formulas, we obtain
(ϕ⊗ trPi
q ⊗ trPi′
q )(JB) = δi,i′
( i∑
l=0
(−1)lq
1
2 l(l+3)− 1
2 i(i+3)
[
i
l
]
q
K 2l−2i
)
{H}q,i({i}q!)2.
Using the identities
i∑
l=0
(−1)lq
1
2 l(l+3)− 1
2 i(i+3)
[
i
l
]
q
K 2l−2i ={−H− 2}q,i,
ϕ(σi) ={H}i{H +i + 1}i = (−1)i{H}i{−H− 2}i,
we obtain
(ϕ⊗ trPi
q ⊗ trPi′
q )(JB) = δi,i′{−H− 2}q,i{H}q,i({i}q!)2
=δi,i′{−H− 2}i{H}i({i}!)2 =δi,i′ (−1)iϕ(σi)({i}!)2.
Hence, we have (ϕ⊗ trP ′
i
q ⊗ tr
P ′
i′
q )(JB) = δi,i′ (−1)iϕ(σi). Then the assertion follows
from the well-known fact that ϕ is injective on the center Z(Uh).
Propositions 14.1 implies the following.
Corollary 14.2. Fori,j,k ≥ 0, we have
JA(P ′
i,P ′
j,P ′
k) =
{
(−1)i{2i + 1}i+1/{1} if i =j =k,
0 otherwise,(14.1)
JA(Vi, Vj, Vk) =
min(i,j,k)∑
p=0
(−1)p
[
i + 1 +p
2p + 1
][
j + 1 +p
2p + 1
][
k + 1 +p
2p + 1
]
({p}!)2{2p + 1}2p.
(14.2)
Proof. For (14.1), use Proposition 6.3. For (14.2), use (8.2).
Corollary 14.2 was ﬁrst stated using the Kauﬀman bracket in [ 16] without proof.
One can easily modify the arguments in [58] to obtain a skein- theoretic proof of
Corollary 14.2.
