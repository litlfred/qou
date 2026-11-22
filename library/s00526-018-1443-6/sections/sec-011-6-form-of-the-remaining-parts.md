---
doc_id: s00526-018-1443-6
doc_title: "On the analyticity of critical points of the Möbius energy"
section_id: sec-011-6-form-of-the-remaining-parts
section_title: "Form of the remaining parts"
section_number: 6
pages: 16-20
source_pdf: s00526-018-1443-6.pdf
source_sha256: 34f3cd94e3b2d9d7
toc_source: outline
doc_brief: "On the analyticity of critical points of the Möbius energy — We prove that smooth critical points of the Möbius energy E parametrized by arc-length are analytic."
---
We aim to transform the truncated remaining parts Rε
1 and Rε
2 of the decomposition of the
Möbius energy E in Sect. 3 into multiple integrals of analytic functions of several variables.
This helps us to estimate the derivatives of the orthogonal projections of Rε
1 and Rε
2 later.
Let 1
2 ≥ε > 0 and x ∈[0, 1]. We start by recalling the deﬁnition of the ﬁrst remaining
part
(R1γ )(x) = lim
ε↓0(Rε
1γ )(x)
where
(Rε
1γ )(x) := 4

|w|∈
'
ε, 1
2
(

1
|γ (x + w) −γ (x)|4 −1
w4

(γ (x + w) −γ (x) −w ˙γ (x))dw.
Similarly,
(R2γ )(x) = lim
ε↓0(Rε
2γ )(x),
where
(Rε
2γ )(x) := −2

|w|∈

ε, 1
2


1
|γ (x + w) −γ (x)|2 −1
w2

¨γ (x)dw.
Because the second remaining part is the more elementary one, we start by working with
P⊥
˙γ Rε
2γ now.
On the analyticity of critical points of the Möbius energy
Page 17 of 28
16
6.1 Form of P⊥
˙ R"
2
Theorem 6.1 We can express P⊥
˙γ Rε
2γ as multiple integral

P⊥
˙γ Rε
2γ

(x) =

|w|∈

ε, 1
2


[0,1]4(s1 −s2)2G2(· · · )(x)dφ1dφ2ds1ds2dw,
over the analytic function G2 : Rn \ {0} × R3n →Rn,
G2(· · · ) := P⊥
˙γ 

G2(· · · ) = 

G2(· · · ) −⟨

G2(· · · ), ˙γ ⟩˙γ ,
where 

G2 : Rn \ {0} × R3n →Rn deﬁned as 

G2(a, x, y, z) := −1
|a|2 ⟨x, y⟩Rn z is analytic
and 
G2(· · · ) is an abbreviation for

G2
 1
0
˙γ (· + tw)dt, ¨γ (· + s2w + (s1 −s2)φ1w), ¨γ (· + s2w + (s1 −s2)φ2w), ¨γ (·)

.
Proof We begin to compute the left-hand side part of the integrand of Rε
2γ by the fundamental
theorem of calculus, the arc-length parametrization of γ , and linearity of the scalar product
as
1
|γ (x + w) −γ (x)|2 −1
w2 =
w2
|γ (x + w) −γ (x)|2
1 −|γ (x+w)−γ (x)|2
w2
w2
= g2
 1
0
˙γ (x + tw)dt
 2

1 −|γ (x+w)−γ (x)|2
w2

w2
= g2
 1
0
˙γ (x + tw)dt
 
[0,1]2 | ˙γ (x + s1w) −˙γ (x + s2w)|2ds1ds2
w2
(6.1)
where g2(x) =
1
2|x|2 for all x ∈Rn \ {0} is analytic away from the origin and furthermore,
| ˙γ (x + s1w) −˙γ (x + s2w)|2
w2
= (s1 −s2)2
 1
0
 1
0
⟨¨γ (x + s2w + (s1 −s2)φ1w), ¨γ (x + s2w + (s1 −s2)φ2w)⟩Rn dφ1dφ2.
(6.2)
Therefore, we can rewrite Rε
2γ such that
(Rε
2γ )(x) =

|w|∈

ε, 1
2


[0,1]4(s1 −s2)2·

G2
 1
0
˙γ (x + tw)dt, ¨γ (x + s2w + (s1 −s2)φ1w), ¨γ (x + s2w + (s1 −s2)φ2w), ¨γ (x)

dφ1dφ2ds1ds2dw
where 

G2 : Rn \ {0} × R3n →Rn is deﬁned as

G2(a, x, y, z) := −2g2(a) ⟨x, y⟩Rn z
and is again an analytic function away from the origin in the ﬁrst variable, because sums,
products and compositions of analytic functions are analytic as well. Now by applying the
orthogonal projection P⊥
˙γ on Rε
2γ we obtain
16
Page 18 of 28
S. Blatt, N. Vorderobermeier

P⊥
˙γ Rε
2γ

(x) =

|w|∈

ε, 1
2


[0,1]4(s1 −s2)2(P⊥
˙γ 

G2(· · · ))(x)dφ1dφ2ds1ds2dw
where 

G2(· · · ) is an abbreviation for

G2
 1
0
˙γ (· + tw)dt, ¨γ (· + s2w + (s1 −s2)φ1w), ¨γ (· + s2w + (s1 −s2)φ2w), ¨γ (·)

.
Finally we can express P⊥
˙γ Rε
2γ as multiple integral

P⊥
˙γ Rε
2γ

(x) =

|w|∈

ε, 1
2


[0,1]4(s1 −s2)2G2(· · · )(x)dφ1dφ2ds1ds2dw,
over G2 : Rn \ {0} × R3n →Rn,
G2(· · · ) := P⊥
˙γ 

G2(· · · ) = 

G2(· · · ) −⟨

G2(· · · ), ˙γ ⟩˙γ ,
which is clearly analytic again.
⊓⊔
6.2 Form of P⊥
˙ R"
1
Now we may transfer the previous calculations to the orthogonal projection P⊥
˙γ Rε
1γ of the
ﬁrst remaining part.
Theorem 6.2 We can express P⊥
˙γ Rε
1γ as multiple integral

P⊥
˙γ Rε
1γ

(x) =

|w|∈

ε, 1
2


[0,1]4(r1 −r2)2G1(· · · )(x)dψ1dψ2dr1dr2dw,
over the analytic function G1 : Rn \ {0} × R3n →Rn,
G1(· · · ) := P⊥
˙γ 

G1(· · · ) = 

G1(· · · ) −⟨

G1(· · · ), ˙γ ⟩˙γ ,
(6.3)
where 

G1 : Rn \ {0} × R3n →Rn deﬁned as 

G1(a, x, y, z) := 2( 1
|a|4 +
1
|a|2 ) ⟨x, y⟩Rn z is
analytic and 

G1(· · · ) is an abbreviation for

G1
  1
0
˙γ (· + sw)ds, ¨γ (· + r2w + (r1 −r2)ψ1w),
¨γ (· + r2w + (r1 −r2)ψ2w),
 1
0
¨γ (· + tw)(1 −t)dt

.
(6.4)
Proof Similarly to the previous subsection we start by computing the integrand of Rε
1γ by
applying the integral form of the remainder of a Taylor polynomial

1
|γ (x + w) −γ (x)|4 −1
w4

(γ (x + w) −γ (x) −w ˙γ (x))
=

1
|γ (x + w) −γ (x)|4 −1
w4

w2
 1
0
¨γ (x + tw)(1 −t)dt
=

w2
|γ (x + w) −γ (x)|4 −1
w2
  1
0
¨γ (x + tw)(1 −t)dt.
(6.5)
On the analyticity of critical points of the Möbius energy
Page 19 of 28
16
By considering the fundamental theorem of calculus we may transform the term within the
brackets in (6.5) as
w2
|γ (x + w) −γ (x)|4 −1
w2 =
w4
|γ (x + w) −γ (x)|4
⎛
⎝1 −|γ (x+w)−γ (x)|4
w4
w2
⎞
⎠
=
w4
|γ (x + w) −γ (x)|4
1
w2

1 + |γ (x + w) −γ (x)|2
w2
 
1 −|γ (x + w) −γ (x)|2
w2

=

w4
|γ (x + w) −γ (x)|4 +
w2
|γ (x + w) −γ (x)|2
 1
w2

1 −|γ (x + w) −γ (x)|2
w2

= g1
 1
0
˙γ (x + sw)ds
 2
w2

1 −|γ (x + w) −γ (x)|2
w2


 !
"
:=E
where g1(x) =
1
2|x|4 +
1
2|x|2 for all x ∈Rn \{0} is analytic away from the origin. Furthermore,
by using (6.1) and (6.2) for computing E, we arrive at
(Rε
1γ )(x) =

|w|∈

ε, 1
2


[0,1]4(r1 −r2)2·

G1
  1
0
˙γ (x + sw)ds, ¨γ (x + r2w + (r1 −r2)ψ1w), ¨γ (x + r2w + (r1 −r2)ψ2w),
 1
0
¨γ (x + tw)(1 −t)dt

dψ1dψ2dr1dr2dw
where 

G1 : Rn \ {0} × R3n →Rn such that

G1(a, x, y, z) = 4g1(a) ⟨x, y⟩Rn z
and therefore analytic away from the origin in the ﬁrst variable. By applying the orthogonal
projection P⊥
˙γ on Rε
1γ we get

P⊥
˙γ Rε
1γ

(x) =

|w|∈
'
ε, 1
2
(

[0,1]4(r1 −r2)2(P⊥
˙γ 

G1(· · · ))(x)dψ1dψ2dr1dr2dw
where 

G1(· · · ) is an abbreviation for

G1
  1
0
˙γ (· + sw)ds, ¨γ (· + r2w + (r1 −r2)ψ1w),
¨γ (· + r2w + (r1 −r2)ψ2w),
 1
0
¨γ (· + tw)(1 −t)dt

.
In the end, we can also express P⊥
˙γ Rε
1γ as multiple integral

P⊥
˙γ Rε
1γ

(x) =

|w|∈
'
ε, 1
2
(

[0,1]4(r1 −r2)2G1(· · · )(x)dψ1dψ2dr1dr2dw,
over G1 : Rn \ {0} × R3n →Rn,
G1(· · · ) := P⊥
˙γ 

G1(· · · ) = 

G1(· · · ) −⟨

G1(· · · ), ˙γ ⟩˙γ ,
which is obviously analytic again.
⊓⊔
16
Page 20 of 28
S. Blatt, N. Vorderobermeier
