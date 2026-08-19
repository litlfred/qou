---
doc_id: arxiv-1701.06567v2
doc_title: "BPS spectra and 3-manifold invariants"
section_id: sec-070-431-unreﬁned-index-of-t-lp-1-with-wilson-loops
section_title: "Unreﬁned index of T [L(p, 1)] with Wilson loops"
section_number: 4.3.1
pages: 64-65
source_pdf: 1701.06567v2.pdf
source_sha256: c1610b50f5a7e22c
doc_brief: "BPS spectra and 3-manifold invariants — We provide a physical deﬁnition of new homological invariants Ha(M3) of 3- manifolds (possibly, with knots) labeled by abelian ﬂat connections."
---
The unreﬁned superconformal index — with contribution of the Cartan component of the
adjoint chiral removed, as in ( 3.40) — with the Wilson line inserted at the north pole reads:
⟨Wλ⟩≡I (q;Wλ) = 1
2
∑
m∈Z
∫ dz
2πizzpm·χλ(qm/2z)
×
(
q2|m| +q−2|m| + 4− 2
(
q|m| +q−|m|
)(
z2 + 1
z2
)
+
(
z4 + 1
z4
))
.
(4.41)
Assuming λ is irreducible, we identify it with its highest weight in Λ wt,su(2)/Z2∼= Z≥0. Our
convention is such that
χλ(z) = zλ+1−z−λ−1
z−z−1 . (4.42)
So, the insertion of an operator Wλ with odd value of λ automatically gives zero, because of
the non-trivial action of the center Z2⊂SU (2).
In the table below we present explicit results for p = 5 up to λ = 38:
λ ⟨Wλ⟩ λ ⟨Wλ⟩ λ ⟨Wλ⟩ λ ⟨Wλ⟩ λ ⟨Wλ⟩
0 3 2 −1 4 0 6 q−3 8 −q−3− 2q−5
10 2q−5 +q−7 12 −q−7 14 0 16 q−16 18 −q−16− 2q−20
20 2q−20 +q−24 22 −q−24 24 0 26 q−39 28 −q−39− 2q−45
30 2q−45 +q−51 32 −q−51 34 0 36 q−72 38 −q−72− 2q−80
.
This table is almost periodic. This can be understood from the action of Wilson lines on the
homological blocks. For the D2×S1 partition function of T [M3] with Wλ inserted at the
center of the disk, O∈D2, we have:
ˆZa(q;Wλ) = 1
|Wa|
∫ dz
2πiz (1−z±2)χλ(z)
∑
n∈pZ+a
qn2/pz2n. (4.43)
Wilson loops act in a very simple way on the homological blocks ˆZa(q). For L(p, 1), we have
ˆZ0 = 1, ˆZ1 =−q1/p, (4.44)
with the rest of the blocks being zero. Let us also formally extend ˆZa fora outside the range
{0, 1,..., ⌊p
2⌋} by ˆZa = 0 and deﬁne a “shift operator”
[j]ˆZa(q) := qj(2a−j)/pˆZa−j(q), a,j ∈ Z. (4.45)
Then,
ˆZa(q;Wλ) =
∑
b≡±a (mod p)
[λ/2]ˆZb(q), a ∈ Zp/Z2. (4.46)
This equation is not cyclic, and we took a to live in Z≥0. Then, one can verify that
⟨Wλ⟩ =
∑
a∈Zp/Z2
|Wa|ˆZa(q;Wλ)ˆZa(q−1). (4.47)
– 63 –
One can also deduce the action of Wλ on Za =∑
bSabˆZb by applying the S-transform,
but it won’t be very illuminating becauseZa(q;Wλ) will be a linear combination of allZa(q)’s.
This diﬀerence between ˆZa and Za again demonstrates the advantage of working with the
homological blocks ˆZa, rather than Za(q).
