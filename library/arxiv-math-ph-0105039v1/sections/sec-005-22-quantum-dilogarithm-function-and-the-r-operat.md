---
doc_id: arxiv-math-ph-0105039v1
doc_title: "December 23, 2000 (Revised Edition) Hyperbolic Structure Arising from a Knot Invariant Kazuhiro HIKAMI †"
section_id: sec-005-22-quantum-dilogarithm-function-and-the-r-operat
section_title: "Quantum Dilogarithm Function and the R Operator"
section_number: 2.2
pages: 5-8
source_pdf: 0105039v1.pdf
source_sha256: 850e6a00721e38d0
doc_brief: "December 23, 2000 (Revised Edition) Hyperbolic Structure Arising from a Knot Invariant Kazuhiro HIKAMI † — We study the knot invariant based on the quantum dilogarithm function."
---
We deﬁne a function Φ γ (ϕ) by an integral form following Ref. 13:
Φ γ (ϕ) = exp
( ∫
R+i 0
e−i ϕ x
4 sh(γ x) sh( π x)
dx
x
)
, (2.11)
where we take γ ∈ R. We note that in Ref. 14 an essentially same integral was intr oduced in
a context of the hyperbolic gamma function, and that in Ref. 1 5 another integral was studied as
the quantum exponential function which solves the same func tional equations below. Also the
integral (2.11) was used to compute the asymptotic form of Ka shaev’s invariant [4]. The function
Φ γ (ϕ) is known as a quantization of the dilogarithm function, and we have in a limit γ → 0
Φ γ (ϕ) ∼ exp
( 1
2 i γ Li2(−eϕ )
)
. (2.12)
We list below several interesting properties of the integral Φ γ (ϕ).
• Duality,
Φ π 2
γ
(ϕ) = Φ γ ( γ
π ϕ). (2.13)
• Zero points,
zeros of
(
Φ γ (x)
) ±1
=
{
∓i
(
(2 m + 1) γ + (2 n + 1) π
) ⏐
⏐m, n ∈ Z≥0
}
(2.14)
5
• Inversion relation,
Φ γ (x) · Φ γ (−x) = exp
(
− 1
2 i γ
( x2
2 + π2 + γ2
6
) )
. (2.15)
By taking a limit γ → 0 and using eq. (2.12), we obtain
Li2(−ex) + Li2(−e−x) + x2
2 + π2
6 = 0,
which is nothing but the inversion identity (2.4) for the Euler dilogarithm function.
• Difference equations,
Φ γ (ϕ + i γ)
Φ γ (ϕ − i γ) = 1
1 + eϕ , (2.16a)
Φ γ (ϕ + i π)
Φ γ (ϕ − i π) = 1
1 + e
π
γ ϕ . (2.16b)
• Pentagon relation [16–18],
Φ γ (ˆp) Φ γ (ˆq) = Φ γ (ˆq) Φ γ (ˆp + ˆq) Φ γ (ˆp), (2.17)
where ˆp and ˆq are the canonically conjugate operators satisfying the Hei senberg commuta-
tion relation,
[ˆp , ˆq] = −2 i γ. (2.18)
In this sense, the parameter γ in the integral (2.11) is the Planck constant.
• The Fourier transformation [19, 20],
1√4 π γ
∫
dy Φ γ (y) e
1
2 i γ x y = Φ γ (−x + iπ + iγ) e
1
2 i γ
(
x2
2 − 1
2 πγ − π 2+γ 2
6
)
, (2.19a)
1√4 π γ
∫
dy 1
Φ γ (y) e
1
2 i γ x y = 1
Φ γ (x − i π − i γ) e
− 1
2 i γ
(
x2
2 − 1
2 πγ − π 2+γ 2
6
)
, (2.19b)
1√4 π γ
∫
dy Φ γ (y + u)
Φ γ (y + v) e− 1
2iγ x y
= Φ γ (v − u − x + iπ + iγ)
Φ γ (v − u + iπ + iγ) Φ γ (−x − iπ − iγ) e
1
2iγ
(
x(u−iπ −iγ )+ 1
2 πγ + π 2+γ 2
6
)
.
(2.19c)
6
For our later convention, we rewrite the pentagon identity (2.17) into a simple form. We deﬁne
the S-operator on V ⊗ V by
S1, 2 = e
1
2 i γ ˆq1 ˆp2 Φ γ (ˆp1 + ˆq2 − ˆp2), (2.20)
where the Heisenberg operators ˆpa and ˆqa act on the a-th vector space V. Then the pentagon
identity (2.17) can be rewritten as
S2, 3 S1, 2 = S1, 2 S1, 3 S2, 3, (2.21)
where Sa,b acts on the a- and b-th spaces of V ⊗ V ⊗ V. See that the operator, T1, 2 = e
1
2 i γ ˆq1 ˆp2,
which is a prefactor of the S-operator (2.20), is a simple solution of eq. (2.21). We remark that the
pentagon identity (2.21) is a natural consequence of the Hei senberg double [21, 22], in which the
S-operator is given by
S =
∑
α
eα ⊗ eα .
Here {eα , eα } is a set of generators satisfying
eα eβ =
∑
γ
mγ
α β eγ ,
eα eβ =
∑
γ
µα β
γ eγ ,
eα eβ =
∑
γ,ρ,σ
mβ
ρ γ µγ σ
α eρ eσ .
For our purpose to deﬁne the knot invariant, we introduce the R-operator by use of the S-
operators as [18, 21, 23]
R12, 34 =
(
St4
1, 4
) −1
S1, 3 St2t4
2, 4
(
St2
2, 3
) −1
, (2.22)
and we set
ˇR12, 34 = P1, 3 P2, 4 R12, 34. (2.23)
Here ta means a transposition on the a-th space, and P is the permutation operator. The R-
operator acts on a vector space V⊗4. Based on the pentagon identity (2.21), we ﬁnd that the
ˇR-operator (2.23) satisﬁes the Yang–Baxter relation,
ˇR11′, 22′ ˇR22′, 33′ ˇR11′, 22′ = ˇR22′, 33′ ˇR11′, 22′ ˇR22′, 33′. (2.24)
7
By regarding the R-operator as an operator on W ⊗ W with W = V⊗2, this Yang–Baxter relation
can be seen as a braid relation as usual, which can be depicted as a projection onto 2-dimensional
space in Fig. 2.
=
Figure 2: Braid relation, or the constant Yang–Baxter equation.
