---
doc_id: arxiv-math-0605314v1
doc_title: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres"
section_id: sec-076-1232-the-ohtsuki-series-as-mentioned-in-the-intr
section_title: "The Ohtsuki series. As mentioned in the introduction, according to Lawrence’s"
section_number: 12.3.2
pages: 41-42
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
doc_brief: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres — W e construct an invariant JM of integral homology spheres M with values in a completion ˆZ[q] of the polynomial ring"
---
conjecture proved by Rozansky, the Ohtsuki series τ O(M ) for an integral homology
sphere can be deﬁned as the unique element τ O(M )∈ Z[[q− 1]] such that for each
root of unity ζ of odd prime power order r, τ O(M )|q=ζ converges p-adically to
τζ(M )∈ Z[ζ], i.e., we have
evζ(τ O(M )) = τζ (M ) (12.4)
in Zp[ζ]∼
= lim
←−nZ[ζ]/(pn)∼
= lim
←−nZ[ζ]/((ζ− 1)n), where
evζ : Z[[q− 1]]→ Zp[ζ]
denote the ring homomorphism induced by the evaluation map
evζ : Z[q]→ Z[ζ], f (q)↦→f (ζ).
These properties characterize τ O(M ).
Theorem 12.6. For every integral homology sphere M , we have ι1(JM ) = τ O(M ).
Proof. For each root of unity ζ of prime power order r =pe, we have the following
commutative diagram
ˆZ[q]
ι1
−−−−→Z[[q− 1]]
evζ


↓


↓ evζ
Z[ζ] −−−−→
i
Zp[ζ].
Here i is the inclusion. By the commutativity of the diagram and by T heorem
11.1, we have ev ζι1(JM ) = i evζ(JM ) = i(τζ(M )). Therefore, by (12.4), we have
evζ (ι1(JM )) = ev ζ(τ O(M )). The assertion follows from Lemma 12.7.
42 KAZUO HABIRO
Lemma 12.7. The map
Z[[q− 1]]→
∏
p:odd prime
Zp[ζp], x ↦→(evζp(x))p,
is injective. Here ζp = exp 2π√
−1
p .
Proof. Writex = ∑
n≥0xn(q−1)n. We assume that ev ζp (x) = 0 for all p, and we see
that xn = 0 by induction on n. Let n≥ 0 and suppose that x0 =··· =xn−1 = 0.
Then, for every odd prime p, we have ev ζp(x) ≡ xn(ζ− 1)n mod (ζ− 1)n+1.
Therefore, xn is divisible by p. It follows that xn = 0.
