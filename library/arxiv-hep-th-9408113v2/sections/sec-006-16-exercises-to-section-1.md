---
doc_id: arxiv-hep-th-9408113v2
doc_title: "Dilogarithm identities"
section_id: sec-006-16-exercises-to-section-1
section_title: "Exercises to Section 1."
section_number: 1.6
pages: 31-34
source_pdf: 9408113v2.pdf
source_sha256: dadd96e1155e820f
toc_source: inferred
doc_brief: "Dilogarithm identities — We study the dilogarithm identities from algebraic, analytic, asymptotic, K-theoretic, combinatorial and representation-theoretic points of view."
---
1.6. Exercises to Section 1.
1. Using the integral representation (1.1) for the Euler dilogarithm Li2(x), prove the
simple single-variable functional equations
i) Li2(z) + Li2(−z) = 1
2Li2(z2),
ii) Li2(z) + Li2(−z) = Li −2(1) −log z log(1 −z),
(L. Euler, 1768),
iii) Li2(−z) + Li2

−1
z

= 2Li2(−1) −1
2 log2(z).
2. Prove the following ﬁve-term, two-variable functional equations
i) Li2

x
1 −x ·
y
1 −y

= Li2

x
1 −y

+Li2

y
1 −x

−Li2(x)−Li2(y)−log(1−x) log(1−y),
(W. Spence, 1809; N. Abel, 1830)
ii) Li2(x) −Li2(y) + Li2
y
x

+ Li2
1 −x
1 −y

−Li2
y(1 −x)
x(1 −y)

= Li2(1) −log x log
1 −x
1 −y

,
(W. Schaeﬀer, 1846)
iii) Li2
x(1 −y)2
y(1 −x)2

= Li2

−x · 1 −y
1 −x

+Li2

−1
y · 1 −y
1 −x

+Li2
x(1 −y)
y(1 −x)

+Li2
1 −y
1 −x

+1
2 log2(y),
(E. Kummer, 1840)
iv) L(x) + L(y) −L(xy) = L
x(1 −y)
1 −xy

+ L
y(1 −x)
1 −xy

+ log
 1 −x
1 −xy

log
 1 −y
1 −xy

.
(L. Rogers, 1906)
3. Prove the following nine-term, three-variable functional equations
i) Li2
vw
xy

= Li2
v
x

+ Li2
w
y

+ Li2
v
y

+ Li2
w
x

+ Li2(x) + Li2(y) −Li2(v)−
Li2(w) + 1
2 log2
−x
y

,
subject to the constraint (1 −v)(1 −w) = (1 −x)(1 −y)
(W. Mantel, 1898),
ii) L
 (1 −x)(1 −y)
(1 −v)(1 −w)

+L

1 −x
1 −vy−1

+L

1 −x
1 −wy−1

−L

1 −v
1 −vy−1

−L

1 −w
1 −wy−1

+L(x) + L(y) −L(v) −L(w) = L(1), subject to the constraint xy = vw, x, y, v, w ∈R
(compare with (1.30)).
Prove the accessibility of these identities.
4. Prove (L(r, θ) := ReL(reiθ), r, θ ∈R)
L

sin θ
sin(ϕ + θ), ϕ

+ L

sin ϕ
sin(ϕ + θ), θ

= π2 
B2(ϕ + θ) −B2(θ) −B2(ϕ)
	
.
32
Anatol N. Kirillov
5. Prove the accessibility of Rogers’ functional equation (Proposition D) for n = 3.
6. Prove the accessibility of the following dilogarithm identities
i) 6L
1
3

−L
1
9

= π2
3 ,
ii)
n
X
k=2
L
 1
k2

+ 2L

1
n + 1

= π2
6 ,
iii) If α =
√
2 −1, then
4L(α) −L(α2) = π2
4 ,
(L. Lewin)
4L(α) + 4L(α2) −L(α4) = 5π2
12 ,
(L. Lewin)
5L(α2) −L(α4) = π2
6 .
(L. Lewin)
iv) Let us take a =
√
3 −1
2
and c =
√
3 −1, then
12L(a) + 3L(a2) −2L(a3) = 5π2
6 ,
(J. Loxton)
12L(c) −9L(c2) −2L(c3) + L(c6) = π2
2 .
(J. Loxton)
v) Let u be the solution in (0, 1) of the quintic u5 + u4 −u3 + u2 = 1. Then
L(u6) + L(u5) −2L(u3) + 8L(u2) −5L(u) = π2
6 .
7. Prove the accessibility of the so-called θ-family of single-variable functional equations
(see [Le4], Chapter 6, Section (6.4)).
8. Prove the Coxeter and Lewin relations (1.11) and (1.12) using the Ray multivariable
functional equation (Proposition E).
Hint: take r(x, t) in the following forms
(1 −ρx)(1 + ρ3x) −(1 −ρ3x)(1 −t),
t := ρ2;
(1 + ρ6x) −(1 + ρ2x)(1 −t),
t := ρ3;
(1 −ρ2x)(1 + ρ10x) −(1 −ρ4x)2(1 −t),
t := ρ4;
(1 + ρ12x)(1 + ρ3x) −(1 + ρ4x)2(1 −t),
t := ρ6,
or
(1 + ρ12x)(1 + ρ6x) −(1 −ρ8x)(1 + ρ4x)(1 −t),
t := ρ6.
Dilogarithm identities
33
9. Prove the following properties of the Wigner-Bloch dilogarithm D(z).
i) For 0 < θ < π the function D(z) is positive and attains its maximum value on the half
line Lθ := {z | arg z = θ} at z = eiθ.
ii) The function D(z) attains its maximum on the complex plane C at z = e
2πi
3 .
iii) lim
z→∞D(z) = 0.
iv) D(z) = 1
2{Cl2(2θ) + Cl2(2w) −Cl2(2θ + 2w)}, where θ = arg z, w = arg(1 −z).
Hint: using the ﬁve-term relation for D(z), to show
D
z
z

+ D
1 −z
1 −z

= 2D(z) + D
z(1 −z)
z(1 −z)

.
10. Prove the accessibility of the following dilogarithm identities (the Lewin Conjec-
tures, [Le3]).
i) Let α = 5 −
√
21
2
be the root of the quadratic equation x2 −5x + 1 = 0. Then
42L(α) −3L(α2) −6L(α3) + L(α6) = 5π2
3 ;
ii) Let β = 4 −
√
15 be the root of the quadratic equation x2 −8x + 1 = 0. Then
30L(β) + 2L(β2) −2L(β3) −L(β4) = 5π2
6 ;
iii) Let γ = 5 −2
√
6 be the root of the quadratic equation x2 −10x + 1 = 0. Then
46L(γ) −15L(γ2) −2L(γ3) + L(γ6) = π2.
11. (We use the notation of Section 1.5). Let us deﬁne for a given positive rational
number p the set of integers {sk}, k =, 1, 2, . . . such that
j + 1
p + 2

= k iﬀsk ≤j < sk+1,
s0 := 0. For dilogarithm sum (1.37) to show
s(j, 2, p) =
3p
p + 2 −6j(j + 2)
p + 2
+ 6t(j, p),
where t(j, p) = (2k + 1)j + k −2
k
X
a=0
sa iﬀsk ≤j < sk+1.
12. Let us deﬁne Rogers’ trilogarithm as
L3(x) = Li3(x) −log |x|L(x) −1
6 log2 |x| log(1 −x).
34
Anatol N. Kirillov
Prove
i) (Landen’s third-order functional equations)
L3(x) + L3(1 −x) + L3
 −x
1 −x

= ζ(3),
L3(x) + L3(−x) = 1
4L3(x2).
ii) L3
1
2

= 7
8ζ(3), L3(ρ2) = 4
5ζ(3).
(J. Landen, 1780)
iii) (Nine-term relation)
2L3(x) + 2L3(y) + 2L3
x(1 −y)
x −1

+ 2L3
y(1 −x)
y −1

+ 2L3
1 −x
1 −y

+ 2L3
x(1 −y)
y(1 −x)

−L3(xy) −L3
x
y

−L3
x(1 −y)2
y(1 −x)2

= 2ζ(3).
(E. Kummer, 1840)
Does this functional equation deﬁne the trilogarithm uniquely?
iv) Let α = 1
2(5 −
√
21). Then
1
36L3(α6) −1
4L3(α2) + 7L3(α) = 77
18ζ(3).
