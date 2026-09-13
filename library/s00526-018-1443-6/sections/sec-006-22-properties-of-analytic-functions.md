---
doc_id: s00526-018-1443-6
doc_title: "Calc. Var. (2019) 58:16 Calculus of Variations On the analyticity of critical points of the Möbius energy Simon Blatt 1 · Nicole Vorderobermeier 1 © The Author(s) 2018"
section_id: sec-006-22-properties-of-analytic-functions
section_title: "Properties of analytic functions"
section_number: 2.2
pages: 5-8
source_pdf: s00526-018-1443-6.pdf
source_sha256: 34f3cd94e3b2d9d7
doc_brief: "Calc. Var. (2019) 58:16 Calculus of Variations On the analyticity of critical points of the Möbius energy Simon Blatt 1 · Nicole Vorderobermeier 1 © The Author(s) 2018 — We prove that smooth critical"
---
Let us recall some elementary facts about analytic functions. More on the topic can be found
for example in [ 9, Chapter 6.4] and [ 11, Chapter 1, D]. Let n, m ∈ N and /Omega1⊆ Rm be an
open set throughout this section.
We will use the following well-known characterization of analytic functions, which can
be deduced from [ 24, Proposition 2.2.10] by a standard covering argument.
Theorem 2.2 Let f ∈ C∞(/Omega1,Rn). Then f is analytic on /Omega1if and only if for every compact
set K ⊂ /Omega1there are constants r K > 0,C K < ∞ such that
‖∂α f ‖L∞(K) ≤ CK
|α|!
r|α|
K
holds for every multiindex α ∈ Nm
0 .
Combining this with the embedding of the classical Sobolev space W k = W k,2 into C0
for k ∈ N with k > m
2 we get the following.
Corollary 2.3 Let f ∈ C∞(/Omega1,Rn). Then f is analytic on R/Z if and only if for every compact
set K ⊂ /Omega1there are constants r K > 0,C K < ∞ such that
‖∂α f ‖W 1(K) ≤ CK
|α|!
r|α|
K
holds for every multiindex α ∈ Nm
0 .
From the equivalence of the W 1-a n dt h eH 1-norm on R/Z we hence get
Corollary 2.4 Let f ∈ C∞(R/Z, Rn). Then f is analytic on /Omega1if and only if there are
constants r > 0,C < ∞ such that
‖∂k f ‖H 1 ≤ C k!
r k
holds for all k ∈ N0.
123
16 Page 6 of 28 S. Blatt, N. Vorderobermeier
Let us mention a special case of the theorem of Cauchy–Kovalevskaya, which is originally
an existence and uniqueness theorem for analytic nonlinear partial differential equations
associated with Cauchy initial value problems. Proofs based on the method of majorants
which we will also use to prove the main result of this article can be found in [ 11, Chapter
1, D] and [ 9, Chapter 4.6.3, Theorem 2].
Theorem 2.5 (Cauchy–Kovalevskaya—ODE case) Let ε> 0. Suppose g : Rn → Rn is real
analytic around 0, and f ∈ C∞(]− ε, ε[, Rn),f (x) = ( f1(x) ,..., fn(x)), be a solution of
the initial value problem
{
˙f (x) = g( f (x)) for x ∈] −ε, ε[
f (0) = 0.
Then f is real analytic around 0.
2.3 Faà di Bruno’s formula
For two functions f , g ∈ Ck(R, R) Faà di Bruno’s formula tells us that
( d
dt
) k
g( f (t))
=
∑
m1+2m2+···km k=k,
m1,...,mk∈N0
k!
m1!1!m1 m2!2!m2 ... mk!k!mk
g(m1+···+mk)( f (t))
k∏
j=1
( f ( j)(t))m j .
Mishkov [27] generalized this formula to the multivariate case.
Lemma 2.6 Let U ⊆ R be a neighborhood of 0 and f ∈ Ck(U, Rn),n ∈ N. Moreover , let
V ⊆ Rn be a neighborhood of f (0) such that f (U) ⊆ V and g ∈ Ck(V, R). Then we have
for any k ∈ N0 and x ∈ U
∂k g( f (x)) =
∑
0
∑
1
···
∑
k
k!
∏k
i=1(i!)ri
∏k
i=1
∏n
j=1 qij !
(∂α g)( f (x))
k∏
i=1
(
f (i)
1 (x)
)qi1 ···
(
f (i)
n (x)
)qin
where the sums are over all non-negative integer solutions of the following equations
∑
0
: r1 + 2r2 +···+ krk = k,
∑
1
: q11 + q12 +···+ q1n = r1
...
∑
k
: qk1 + qk2 +···+ qkn = rk
and α := (α1,...,α n) with α j := q1 j + q2 j +···+ qkj for 1 ≤ j ≤ n.
123
On the analyticity of critical points of the Möbius energy Page 7 of 28 16
Remark 2.7 In the following we will not need the precise form of Faà di Bruno’s formula in the
multivariate case but only the fact that there is a universal polynomial p(n)
k with non-negative
coefﬁcients independent of f , g such that
∂k g( f (x)) = p(n)
k ({∂α g}|α|≤k,{∂ j fi}i=1,...,n, j=1,...,k) (2.2)
for all f ∈ Ck(R, Rn), g ∈ Ck(Rn, R), n ∈ N and k ∈ N0. Furthermore, p(n)
k is one-
homogeneous in the ﬁrst entries.
3 Decomposition of the ﬁrst variation of E
In 1994, Freedman, He and Wang stated the Gâteaux differentiability of the Möbius energy
E and additionally a formula of the ﬁrst variation of E [10, Lemma 6.1, Lemma 6.4.]. Reiter
could prove that E is Fréchet differentiable and he computed its ﬁrst variation at an injective
regular curve η ∈ H 2 in direction h ∈ H 2 [38, Chapter 2]. In order to work with the Möbius
energy in a sophisticated way, He and Reiter used a kind of linearization of the ﬁrst variation
of E in [17,38]. Using these ideas and results, we want to determine a suitable decomposition
of the ﬁrst variation of the Möbius energy E at γ which helps us proving the main result
Theorem 1.2.
Assume n ∈ N and let γ ∈ C∞(R/Z, Rn) be a simple, closed, and by arc-length
parametrized curve. Recall that the orthogonal projection of Rn onto the normal vector
plane to γ at γ( x) P⊥
˙γ( x) : Rn → Rn for every g ∈ Rn is given by
(P⊥
˙γ g)(x) := P⊥
˙γ( x)(g) := g −⟨g, ˙γ( x)⟩Rn ˙γ( x).
Then we get by [ 10, Lemma 6.4.] and [ 38, Theorem 2.24] the following
Theorem 3.1 The ﬁrst variation of E at γ ∈ H 2(R/Z, Rn) in direction h ∈ H 2(R/Z, Rn)
may be written as
δE(γ, h) =
∫1
0
⟨(Hγ) (x), h(x)⟩Rn dx (3.1)
where
(Hγ) (x) := 2 lim
ε↓0
∫
|w|∈
[
ε, 1
2
]
(
2
P⊥
˙γ( x)(γ (x + w) − γ( x))
|γ( x + w) − γ( x)|2 −¨γ( x)
)
dw
|γ( x + w) − γ( x)|2 .
Since P⊥
˙γ( x)( ˙γ( x)) = 0, ⟨˙γ( x), ¨γ( x)⟩Rn = 0 and by the linearity of P⊥
˙γ( x) for all x ∈ R/Z,
one sees that
(Hγ) (x) = (P⊥
˙γ ~Hγ) (x) = P⊥
˙γ( x)((~Hγ) (x)) (3.2)
where
(~Hγ) (x) := 2 lim
ε↓0
∫
|w|∈
[
ε, 1
2
]
(
2γ( x + w) − γ( x) − w ˙γ( x)
|γ( x + w) − γ( x)|2 −¨γ( x)
)
dw
|γ( x + w) − γ( x)|2 .
123
16 Page 8 of 28 S. Blatt, N. Vorderobermeier
Now, motivated by [17,38] as explained above, simply by adding and subtracting the terms
4(γ (x+w)−γ( x)−w ˙γ( x))
w4 and 2 ¨γ( x)
w2 , we may decompose ~H into three functionals Q, R1, R2
given point-wise for all x ∈[ 0, 1] by
Qγ( x) = lim
ε↓0
Qεγ( x), R1γ( x) = lim
ε↓0
Rε
1γ( x), R2γ( x) = lim
ε↓0
Rε
2γ( x),
where for any 0 <ε ≤ 1
2
(Qεγ) (x) := 2
∫
|w|∈
[
ε, 1
2
]
(
2γ( x + w) − γ( x) − w ˙γ( x)
w2 −¨γ( x)
) dw
w2 ,
(Rε
1γ) (x) := 4
∫
|w|∈
[
ε, 1
2
]
( 1
|γ( x + w) − γ( x)|4 − 1
w4
)
(γ (x + w) − γ( x) − w ˙γ( x))dw,
(Rε
2γ) (x) := −2
∫
|w|∈
[
ε, 1
2
]
( 1
|γ( x + w) − γ( x)|2 − 1
w2
)
¨γ( x)dw,
such that
(~Hγ) (x) = (Qγ) (x) + (R1γ) (x) + (R2γ) (x) (3.3)
for all x ∈ R/Z.
In the upcoming section we will see that Q contains the highest order part of the ﬁrst
variation of E. We will see that the tangential part of Q is the most difﬁcult part to get under
control, whereas R1 and R2 are of lower order and can be estimated more elementary.
