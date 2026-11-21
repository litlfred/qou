---
doc_id: arxiv-math-0108046v3
doc_title: "arXiv:math/0108046v3 [math.RT] 3 May 2002"
section_id: page-013
section_title: "Page 13"
section_number: null
pages: 13-13
source_pdf: 0108046v3.pdf
source_sha256: f47c1bd39c671cf3
toc_source: undetermined
doc_brief: "Presenting Schur algebras — Motivated by work of R.M. Green, we obtain a pre- sentation of Schur algebras (both the classical and quantized ver- sions) in terms of generators and relations."
---
PRESENTING SCHUR ALGEBRAS
13
which is the same as
λi
b

φ(1λ) since from the preceding proof φ(1λ) =
(δµλ)µ. Since φ is an isomorphism, part (a) is proved.
Part (b) follows immediately from part (a). Then by the result of
part (b) we obtain the equalities HB = HB ·1 = HB
P
λ 1λ = P
λ λB1λ,
proving part (c).
We write Nn
i0 for the set of B = (Bi) ∈Nn such that Bi0 = 0.
Corollary 3.7. For any ﬁxed choice of i0 (1 ≤i0 ≤n) the set {HB |
B ∈Nn
i0, |B| ≤d} is a Q-basis for T 0 and a Z-basis for T 0
Z.
Proof. The sets Λ(n, d) and {B ∈Nn
i0, |B| ≤d} have the same cardi-
nality. For instance, the map
λ →λ −λi0εi0
is bijective between the sets in question, with inverse map
B →B + (d −|B|)εi0.
Thus, to prove the result it is enough to show that the set {HB | B ∈
Nn
i0, |B| ≤d} spans T 0
Z. This can be deduced by considering a certain
order (depending on i0) on each of these sets.
Fixing 1 ≤i0 ≤n, we order the set Λ(n, d) by declaring that λ
precedes λ′ if λi0 < λ′
i0, or if λi0 = λ′
i0 and there exists an index l̸ = i0
such that λj ≥λ′
j for all j ∈{1, . . . l} −{i0}. Similarly, we order the
set {B ∈Nn
i0, |B| ≤d} by declaring that B precedes B′ if there exists
an index l̸ = i0 such that bj ≥b′
j for all j ∈{1, . . . l}−{i0}. With these
orderings, it follows from part (c) of the preceding proposition that the
matrix of coeﬃcients obtained by expressing the HB’s in terms of the
1λ’s is lower unitriangular. To see this, observe that for any given B,
with corresponding λ = B +(d−|B|)εi0, any µ which succeeds λ in the
above order satisﬁes µB = 0, and moreover λB = 1. It follows that these
equations can be inverted over Z and so every 1λ is expressible as a Z-
linear combination of elements from the set {HB | B ∈Nn
i0, |B| ≤d}.
This proves that this set spans T 0
Z and, by our remarks above, it must
therefore be a Q-basis, and thus is linearly independent over Z, and
hence also a Z-basis. The proof is complete.
The next step is to ﬁnd spanning sets for the plus part T + and minus
part T −of T. For this we use the following result.
