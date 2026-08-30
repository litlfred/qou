---
doc_id: arxiv-math-0605314v1
doc_title: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres"
section_id: sec-087-133-the-p-adic-wrt-functions-in-this-subsection
section_title: "The p-adic WRT functions. In this subsection, we show that the WRT"
section_number: 13.3
pages: 49-51
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
doc_brief: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres — W e construct an invariant JM of integral homology spheres M with values in a completion ˆZ[q] of the polynomial ring"
---
function of an integral homology sphere can be extended to a p-adic analytic func-
tion on the unit circle in the ﬁeld Cp of complex p-adic numbers.
The ﬁeld Cp is deﬁned as follows (see [40, 13] for details). Let Qp be the ﬁeld of
p-adic numbers, and let |·| p : Qp→ R be the p-adic norm, deﬁned by
|x|p =
{
p− ordp(x) if x⁄= 0,
0 if x = 0,
where ord p(x)∈ Z is the p-adic ordinal. Let ¯Qp denote the algebraic closure of Qp.
It is well known that the norm |·| p on Qp uniquely extends to ¯Qp. Then Cp is
deﬁned to be the completion of ¯Qp with respect to the norm |·| p. The norm on
Cp induced by |·| p on ¯Qp is denoted again by |·| p. It is well known that Cp is
algebraically closed.
LetOp andPp denote the valuation ring and the valuation ideal, respecti vely,
of Cp, i.e.,
Op ={x∈ Cp : |x|p≤ 1}, Pp ={x∈ Cp : |x|p < 1}.
Let
U (Op) =Op\P p ={x∈ Cp : |x|p = 1}
denote the unit circle of Op, which consists of the multiplicative units in Op. In
particular, all the roots of unity in Cp are contained in U (Op). We may assume that
the setZ(⊂ ¯Q⊂ C) of complex roots of unity as a subset of U (Op) (by choosing a
ﬁeld homomorphism ¯Q֒→¯Qp(⊂ Cp)).
Lemma 13.2. For each x∈ U (Op), the sequence (x)n, n≥ 0, of elements in Op
is converging to 0 inOp.
Proof. Sincex∈U (Op), there is ζ∈Z such that x−ζ∈P p. Set r = ord(ζ). Then
1−xr = 1− (ζ + (x−ζ))r
= 1−
r∑
i=0
(r
i
)
ζr−i(x−ζ)i
=−
r∑
i=1
(r
i
)
ζr−i(x−ζ)i∈P p.
Since (x)rk is divisible by (1 −xr)k for each k≥ 0, it follows that ( x)n converges
to 0 as n→∞ .
Lemma 13.2 implies that for x∈ U (Op), the ring homomorphism Z[q]→O p,
f (q)↦→f (x), induces a continuous ring homomorphism
evx : ˆZ[q]→O p, f (q)↦→f (x).
Gathering the ev x for all x∈U (Op), we obtain a ring homomorphism
evU(Op) : ˆZ[q]→ Fun(U (Op),Op)
50 KAZUO HABIRO
such that ev U(Op)(f )(x) = ev x(f (q)). For f∈ ˆZ[q], the function
ˆf = ev U(Op)(f ) : U (Op)→O p(13.3)
is p-adic analytic of radius of convergence ≥ 1 everywhere in U (Op). I.e., ˆf has a
converging power series expansion at any point x∈U (Op) which coincides ˆf for all
y∈U (Op) with|y−x|p< 1.
It is easy to see that the restriction of ˆf to
U (Zp) ={x∈ Zp :|x|p = 1} =U (Op)∩ Qp
takes values in Zp.
For any subset V ⊂U (Op), ev U(Op) induces a ring homomorphism
evV : ˆZ[q]→ Fun(V,Op).
Proposition 13.3. Let V ⊂ U (Op) be an inﬁnite subset. Suppose that there is a
pointx∈U (Op) and a sequence xi∈V\x, i = 0, 1,... , such that limi→∞xi =x
with respect to the p-adic topology. Then evV is injective.
Proof. Suppose ev V (f ) = 0, f∈ ˆZ[q]. Deﬁne ˆf as in (13.3). Set D(x, 1) = {y∈
Op : |y−x|p < 1}. The restriction ˆfx = ˆf|D(x,1) : D(x, 1)→O p can be expressed
as a power series at q = x, convergent on D(x, 1). The assumption implies that
ˆfx = 0, i.e., ˆf (x) = 0 for all x∈D(x, 1).
Since x∈ U (Op), we have D(x, 1)∩Z⁄=∅. Moreover, if ζ∈ D(x, 1)∩Z and
ξ∈Z with ord(ξ) a power of p, thenζξ∈D(x, 1)∩Z . Since for each ζ∈D(x, 1)∩Z
we have f (ζ) = ˆf (ζ) = 0, it follows from Proposition 1.1 that f = 0.
Now we give applications of the above-mentioned facts to the WRT invariants.
For each integral homology sphere M , deﬁne the p-adic WRT function of M by
τ p(M ) = ev U(Op)(JM ) : U (Op)→O p,(13.4)
which is p-adic analytic of radius of convergence ≥ 1 everywhere in U (Op). τ p(M )
restricts to
τ p(M ) : U (Zp)→ Zp.
Note that these invariants generalize the one given in (13.2 ).
If V is as in Proposition 13.3, then JM is determined by the restriction of
τ p(M ) to V . In particular, for V = U (Op), JM (hence τ (M )) is determined by
τ p(M ) : U (Op)→O p and also by its restriction to U (Zp).
The following generalizes Conjecture 12.11.
Conjecture 13.4 (p-adic Non-vanishing Conjecture) . For any integral homology
sphereM , for any prime p, τ p(M ) : U (Op)→O p is nowhere zero.
If Conjecture 13.4 is true for at least one prime p, then Conjecture 12.11 is true.
As a partial result of Conjecture 13.4, we have the following result, closely related
to Corollary 12.10.
Proposition 13.5. If ζ∈Z⊂ U (Op) is a root of unity of order 1, 2, 3, 4 or 6,
then τ p(M ) has no zero on D(ζ, 1) ={x∈U (Op) :|x−ζ|p < 1}.
Proof. The assertion follows from τζ(M ) =±1 and the fact that the power series
expansion of τ p(M ) at q =ζ has coeﬃcients in Op.
A UNIFIED WITTEN-RESHETIKHIN-TURAEV INV ARIANT 51
Remark 13.6. By Corollary 12.10, τ p(M ) is non-vanishing at q =ζξ , where ξ∈Z
is of any prime power order. It follows from the analyticity t hat τ p(M ) is non-
vanishing on some neighborhood of ζξ .
