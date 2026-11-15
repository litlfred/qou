---
doc_id: arxiv-math-0304010v1
doc_title: "Kerov's central limit theorem for the Plancherel measure on Young diagrams"
section_id: page-016
section_title: "Page 16"
section_number: null
pages: 16-16
source_pdf: 0304010v1.pdf
source_sha256: fc2296c027b3feb0
toc_source: undetermined
doc_brief: "Kerov's central limit theorem for the Plancherel measure on Young diagrams — Consider random Young diagrams with ﬁxed number n of boxes, dis- tributed according to the Plancherel measure Mn."
---
about z = ∞. In other words,
p#
k (λ) = −Res
z=∞(F(z)dz).
After simple transformations we get
F(z) = −1
k (z −n)↓k
Φ(z −n + 1
2; λ)
Φ(z −n + 1
2 −k; λ) .
The residue at z = ∞will not change under the shift z 7→z +n −1
2. Consequently,
p#
k (λ) = −Res
z=∞

−1
k (z −1
2)↓k
Φ(z; λ)
Φ(z −k; λ)

,
which completes the proof.
□
We shall employ the following notation. Given a formal series A(t), let
[tk]{A(t)} = ⟨the coeﬃcient of tk in A(t)⟩.
The next result is due to Wassermann [Wa, §III.6].
Proposition 3.3. For any k = 1, 2, . . ., the function p#
k (λ) introduced in Deﬁni-
tion 2.1 belongs to the algebra A. Its expression through the generators p1, p2, . . .
of A can be described as follows:
p#
k = [tk+1]


−1
k
k
Y
j=1
(1 −(j −1
2)t) · exp


∞
X
j=1
pjtj
j
(1 −(1 −kt)−j)




.
(3.2)
Proof. By Proposition 3.2,
p#
k (λ) = [tk+1]







−1
k tk (t−1 −1
2)↓k
Φ(t−1; λ)
Φ

t
1−kt
−1
; λ








.
We have
tk(t−1 −1
2)↓k =
k
Y
j=1
(1 −(j −1
2)t)
and, by Proposition 1.4,
Φ(t−1; λ) = exp


∞
X
j=1
pj(λ)
j
tj

.
This yields (3.2), which in turn implies that p#
k ∈A.
□
16
