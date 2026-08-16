---
doc_id: arxiv-q-alg-9608020v2
doc_title: "∂x i + (n −j)θ +u 1≤i,j ≤n D(u;θ)Pλ (x;θ) = ( ∏ (λ i + (n −i)θ +u) Pλ (x;θ),(1.1) where V (x) =∏ i<j(xi −xj) is the Vandermonde determinant and u is a parame- ter. The operators {D"
section_id: sec-005-1-looking-at
section_title: "Looking at"
section_number: 1
pages: 4-5
source_pdf: 9608020v2.pdf
source_sha256: 727268098db7f23d
doc_brief: "SHIFTED JACK POLYNOMIALS, BINOMIAL — In this note we prove an explicit binomial formula for Jack poly nomials and discuss some applications of it. 1. Jack polynomials ( [M,St])."
---
the highest derivatives one easily proves that the map
(3.4) D(n;θ) → S 1
which takes an operator D to the distribution ψ D
ψ D(f ) = (Df )(1,..., 1)
is an order preserving isomorphism of linear spaces.
Proof of the theorem. Consider the Taylor expansion of Pλ (x;θ) about the point ¯
1.
Since Jack polynomials form a linear basis in symmetric poly nomials this expansion
has the form
(3.5) Pλ (1 +x1,..., 1 +xn;θ) =
∑
µ
ψ µ (Pλ )Pµ (x;θ), ψ µ ∈ S 1.
Note that ψ µ is of order ≤ |µ |. By virtue of the isomorphisms (2.1) and (3.4) we
have
(3.6) Pλ (1 +x1,..., 1 +xn;θ) = Pλ (1,..., 1)
∑
µ
fµ (λ)Pµ (x;θ), f µ ∈ Λ θ (n),
where degfµ ≤ |µ |. On the other hand
(3.7) Pλ (1 +x1,..., 1 +xn;θ) = Pλ (x1,...,x n;θ) + lower degree terms .
From (3.6) and (3.7) we obtain
fµ (λ) =
{ 0, |λ| ≤ |µ |,λ ⁄=µ,
1/P µ (1,..., 1), λ =µ.
Sincefµ is a polynomial of degree ≤ |µ | it is completely determined by its values
at the points λ, |λ| ≤ |µ |. Therefore, fµ is proportional to P ∗
µ and by (3.1)
fµ (x) = H ′(µ )
(nθ)µH(µ )P ∗
µ (x;θ),
which concludes the proof. □
SHIFTED JACK POLYNOMIALS, BINOMIAL FORMULA, AND APPLICATI ONS 5
Remark. The coeﬃcients
( λ
µ
)
θ in the expansion
Pλ (1 +x1,..., 1 +xn;θ)
Pλ (1,..., 1;θ) =
∑
µ
( λ
µ
)
θ
Pµ (x1,...,x n;θ)
Pµ (1,..., 1;θ) .
are called the generalized binomial coeﬃcients . They were studied by C. Bingham
[Bi] in the special case θ = 1/ 2, using group–theoretical methods, and by M. Lassalle
[La] for general θ. Then a proof of the main results announced in [La] was propos ed
by J. Kaneko (see [K], section 5). Our theorem says that this b inomial coeﬃcient
(3.8)
( λ
µ
)
θ
= P ∗
µ (λ;θ)
H(µ )
is a shifted symmetric polynomial in λ which by (2.4) and (2.5) is just as complex
as the Jack polynomial Pµ (x;θ) itself. The main results of Lassalle can be easily
deduced from (3.8). For example, it is clear that (3.8) does n ot depend on n and
vanishes unless µ ⊂ λ. The recurrence relation (see [La], th´ eor` emes 2, 3, 5 and
corollaire in section 6) is equivalent to the formula (5.2) b elow.
Note also that the coeﬃcients (3.8) admit a simple formula wh en θ = 1 (see
A. Lascoux [Lasc] and Example 10 in [M], section I.3) or when λ 1 = · · · =λ n (see
J. Faraut and A. Kor´ anyi [FK], Prop. XII.1.3 (ii)).
Binomial formulas for characters of classical groups are di scussed in [OO2] 3.
