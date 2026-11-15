---
doc_id: arxiv-math-0304010v1
doc_title: "Kerov's central limit theorem for the Plancherel measure on Young diagrams"
section_id: page-026
section_title: "Page 26"
section_number: null
pages: 26-26
source_pdf: 0304010v1.pdf
source_sha256: fc2296c027b3feb0
toc_source: undetermined
doc_brief: "Kerov's central limit theorem for the Plancherel measure on Young diagrams — Consider random Young diagrams with ﬁxed number n of boxes, dis- tributed according to the Plancherel measure Mn."
---
Proposition 5.2. For any f ∈A, the expectation ⟨f⟩n is a polynomial in n. The
degree of this polynomial is bounded from above by 1
2 deg1(f).
Proof. It suﬃces to check this for f = p#
ρ . Let r = |ρ|. If ρ̸ = (1r) then ⟨f⟩n ≡0,
by virtue of Proposition 5.1. If ρ = (1r) then, by Proposition 5.1, ⟨f⟩n = n↓r. On
the other hand, deg1(f) = 2r, which agrees with the claim.
□
We deﬁne the function Ω(x) on R by
Ω(x) =
 2
π(x arcsin x
2 +
√
4 −x2),
|x| ≤2,
|x|,
|x| ≥2.
Note that both expressions agree at x = ±2, so that Ω(x) is continuous. Moreover,
the ﬁrst derivative Ω′(x) is continuous on the whole R, while Ω′′(x) is not. This is
clear from the explicit expressions
Ω′(x) = 2
π arcsin x
2 ,
Ω′′(x) = 2
π
1
√
4 −x2 ,
|x| < 2.
Next, we have |Ω′(x)| < 1 for |x| < 2, which implies that Ω(x) belongs to D0.
Applying (2.2) for ω = Ωwe get
epk[Ω] = −k
Z
R
xk−1
Ω(x) −|x|
2
′
dx = −k
2
Z 2
−2
xk−1( 2
π arcsin x
2 −sgn x)dx.
Proposition 5.3. We have
epk[Ω] =



(2m)!
m!m! ,
k = 2m,
m = 1, 2, . . .,
0,
k = 1, 3, 5, . . . .
Proof. Since Ω(x) is even, epk[Ω] = 0 for odd k. For even k we get from (2.2)
ep2m[Ω] =
Z 2
0
(1 −2
π arcsin x
2) d(x2m).
Setting x = 2 sin θ and integrating by parts we get the result.
□
We proceed to the “law of large numbers” for the Plancherel measures Mn.
Actually, it is implied by the “central limit theorem” which will be established in
§7. However, we prefer to give here an independent short proof.
Recall that in Deﬁnition 2.3 we have attached to any Young diagram λ ∈Yn a
function λ( · ) ∈D0. We deﬁne now a scaled version of it:
¯λ(x) = n−1/2λ(n1/2x),
x ∈R,
λ ∈Yn .
This is a special case of Deﬁnition 2.10. The correspondence λ 7→¯λ( · ) provides an
embedding Yn֒ →D0.
26
