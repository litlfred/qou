---
doc_id: arxiv-1704.01735v4
doc_title: "Modular curves, invariant theory and E8"
section_id: sec-011-4-t-az-a
section_title: "T A(z), A"
section_number: 4
pages: 21-22
source_pdf: 1704.01735v4.pdf
source_sha256: 3935747ae9291f76
doc_brief: "Modular curves, invariant theory and E8 — The E8 root lattice can be constructed from the modular curve X(13) by the invariant theory for the simple group PSL(2 , 13)."
---
(
−1
z
)
= e
πi
4
√zS A(z), (3.16)
where S and T are given in (3.1) and (3.2), and 0 < arg√z ≤ π/2.
Recall that the principal congruence subgroup of level 13 is the no rmal
subgroup Γ(13) of Γ = PSL(2 , Z) deﬁned by the exact sequence 1 → Γ(13) →
Γ(1)
f
→ G → 1 where f (γ) ≡ γ (mod 13) for γ ∈ Γ = Γ(1). There is
a representation ρ : Γ → PGL(6, C) with kernel Γ(13) deﬁned as follows:
if t =
(
1 1
0 1
)
and s =
(
0 −1
1 0
)
, then ρ(t) = T and ρ(s) = S. To see
that such a representation exists, note that Γ is deﬁned by the pr esentation
⟨s, t; s2 = ( st)3 = 1 ⟩ satisﬁed by s and t and we have proved that S and T
satisfy these relations. Moreover, we have proved that G is deﬁned by the
presentation ⟨S, T ; S2 = T 13 = (ST )3 = 1⟩. Let p = st−1s and q = st3. Then
h := q5p2 · p2q6p8 · q5p2 · p3q =
(
4, 428, 249 −10, 547, 030
−11, 594, 791 27 , 616, 019
)
satisﬁes that ρ(h) = H. The oﬀ-diagonal elements of the matrix h, which
corresponds to H, are congruent to 0 mod 13. The connection to Γ 0(13)
should be obvious.
Put xi(z) = η(z)ai(z) and yi(z) = η3(z)ai(z) (1 ≤ i ≤ 6). Let
X(z) = ( x1(z), . . . , x6(z))T and Y (z) = ( y1(z), . . . , y6(z))T .
Then X(z) = η(z)A(z) and Y (z) = η3(z)A(z). Recall that η(z) satisﬁes
the following transformation formulas η(z + 1) = e
πi
12 η(z) and η
(
− 1
z
)
=
e− πi
4
√zη(z). By Proposition 3.2, we have
X(z + 1) = e− 2πi
3 ρ(t)X(z), X
(
−1
z
)
= zρ(s)X(z),
Y (z + 1) = e− πi
2 ρ(t)Y (z), Y
(
−1
z
)
= e− πi
2 z2ρ(s)Y (z).
Deﬁne j(γ, z) := cz + d if z ∈ H and γ =
(
a b
c d
)
∈ Γ(1). Hence, X(γ(z)) =
u(γ)j(γ, z)ρ(γ)X(z) and Y (γ(z)) = v(γ)j(γ, z)2ρ(γ)Y (z) for γ ∈ Γ(1), where
21
u(γ) = 1 , ω or ω2 with ω = e
2πi
3 and v(γ) = ±1 or ±i. Since Γ(13) = ker
ρ, we have X(γ(z)) = u(γ)j(γ, z)X(z) and Y (γ(z)) = v(γ)j(γ, z)2Y (z) for
γ ∈ Γ(13). This means that the functions x1(z), . . ., x6(z) are modular forms
of weight one for Γ(13) with the same multiplier u(γ) = 1 , ω or ω2 and y1(z),
. . ., y6(z) are modular forms of weight two for Γ(13) with the same multiplier
v(γ) = ±1 or ±i.
From now on, we will use the following abbreviation
Aj = Aj(a1(z), . . . , a6(z)) (0 ≤ j ≤ 6),
Dj = Dj(a1(z), . . . , a6(z)) ( j = 0, 1, . . . ,12, ∞)
and
Gj = Gj(a1(z), . . . , a6(z)) (0 ≤ j ≤ 12).
We have 




























A0 = q
1
