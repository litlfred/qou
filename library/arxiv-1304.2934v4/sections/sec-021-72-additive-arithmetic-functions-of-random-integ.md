---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I:"
section_id: sec-021-72-additive-arithmetic-functions-of-random-integ
section_title: "Additive arithmetic functions of random integers"
section_number: 7.2
pages: 50-55
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
doc_brief: "MOD-φ CONVERGENCE, I: — In this paper, we use the framework of mod- φ convergence to prove pre- cise large or moderate deviations for quite general sequences of real valued random variables (Xn)n∈N"
---
times write log(log n) = log2 n, which is negligible in comparison to log n as n goes to
inﬁnity.
7.2.1. Number of prime divisors, counted without multiplicities. Denote P the set of prime
numbers, ω(k) the number of distinct prime divisors of an integer k, and ωn the ran-
dom variable ω(k) with k random integer uniformly chosen in [n] :={1, 2, . . . ,n}. The
random variable ωn satisﬁes the Erdös-Kac central limit theorem (cf. [EK40]):
ωn− log logn√
log logn →N R(0, 1).
In this section, we show that ωn converges mod-Poisson and present precise deviation
results for it. Such a result was established in [KN10, Section 4]. But in the latter article,
mod-φ convergence is deﬁned via convergence of the renormalized Fourier transform,
while here we work with Laplace transform. Therefore, we need to justify that the
convergence also holds for Laplace transforms.
We start from the Dirichlet series of yω(k), which is:
∑
k≥1
yω(k)
ks = ∏
p∈P
(
1 + y
ps− 1
)
,
well-deﬁned and absolutely convergent if Re (s) > 1. The Selberg-Delange method
allows to extract from this formula precise estimates for the generating function of ωn;
see [Ten95] and references therein.
Proposition 7.4. [Ten95, Section II.6, Theorem 1] For any A > 0, we have, for any y in C
with|y|≤ A
∑
k≤n
yω(k) = n (log n)y−1 (λ0(y) + O(1/ logn)),
where
λ0(y) = 1
Γ(y) ∏
p∈P
(
1 + y
p− 1
)(
1− 1
p
)y
MOD-φ CONVERGENCE, I 51
and the constant hidden in the O symbol depends only on A.
Remark 7.5. In fact, [Ten95, Section II.6, Theorem 1] gives a complete asymptotic ex-
pansion of ∑k≤n yω(k) in terms of powers of 1/ log(n). For our purpose, the ﬁrst term
is enough: we will see that it implies mod-Poisson convergence with a speed of con-
vergence as precise as wanted.
Setting y = ez, this can be rewritten as an asymptotic formula for the Laplace trans-
form of ωn.
E[ez ωn] = 1
n
n
∑
k=1
ez ω(k) = (log n)ez−1λ0(ez) (1 + O(1/ logn))
= e(ez−1) log logn λ0(ez) (1 + O(1/ logn)).
Recall that the constant in the O symbol is uniform on sets {w,|w|≤ A}, that is on
bands{z, Re(z)≤ log(A)}. In particular the convergence is uniform on compact sets.
Therefore, one has the following result.
Proposition 7.6. The sequence of random variables (ωn)n≥1 converges mod-Poisson with pa-
rameter tn = log2 n and limiting function ψ(z) = λ0(ez) on the whole complex plane. This
takes place with speed of convergence O(1/ logn), that is O((tn)−ν) for all ν > 0.
Using Theorem 3.4, we get immediately the following deviation result.
Theorem 7.7. Let x > 0. Assume x log2 n∈ N. Then
P[ωn = x log2 n] = λ0(x) ( 1 + O(1/ log2 n))
(log n)x log(x)−x+1√
2πx log2 n. (30)
Furthermore, if x > 1, then
P[ωn≥ x log2 n] = λ0(x) ( 1 + O(1/ log2 n))
(log n)x log(x)−x+1√
2πx log2 n
1
1− 1
x
. (31)
Remark 7.8. The ﬁrst equation (30) is not new: it is due to Selberg [Sel54] and presented
in a slightly different form than here in [Ten95, Section II.6, Theorem 4]. Note also that,
as the speed of mod-Poisson convergence of ωn is O
((
tn
)−ν)
for all ν > 0, Theorem
3.4 gives asymptotic expansions of the above probabilities, up to an arbitrarily large
power of 1/ log logn. Theorem 4 in [Ten95, Section II.6] also gives such estimates. The
second statement (31) follows from [Rad09, Theorem 2.8]; it is a nice feature of the
theory of mod-φ convergence to allow to recover quickly such deep arithmetic results
(though we still need Selberg-Delange asymptotics).
7.2.2. Number of prime divisors, counted with multiplicities. In this section, we give sim-
ilar results for the number of prime divisors Ωn of a random integer in {1, 2, . . . ,n},
counted with multiplicities. An important difference is that, here, the mod-Poisson con-
vergence occurs only on a band and not on the whole complex planeC. In this case the
Dirichlet series is given by:
∑
k≥1
yΩ(k)
ks = ∏
p∈P
(
1− y
ps
)−1
,
52 VALENTIN FÉRAY, PIERRE-LOÏC MÉLIOT, AND ASHKAN NIKEGHBALI
which again is well-deﬁned and absolutely convergent for Re(s) > 1. Note that, unlike
in the case of ω(k), the right-hand side has some pole, the smallest in modulus being
for y = 2s. Again, a precise estimate for the generating function follows from the work
of Selberg and Delange; see [Ten95] and references therein.
Proposition 7.9. [Ten95, Section II.6, Theorem 2] For any δ with 0 < δ < 1, we have, for
any y in C with|y|≤ 2− δ
∑
k≤n
yΩ(k) = n (log n)y−1 (ν0(y) + O(1/ logn)),
where
ν0(y) = 1
Γ(y) ∏
p∈P
(
1− y
p
)−1(
1− 1
p
)y
and the constant hidden in the O symbol depends only on δ.
Note the difference with Proposition 7.4: the function ν0 has a simple pole for y = 2
(while λ0 is an entire function) and the estimate in Proposition 7.9 holds (uniformly on
compacts) only for|y| < 2.
Setting again y = ez, this can be rewritten as an asymptotic formula for the Laplace
transform of Ωn on the bandS(−∞,log 2) ={z, Re(z) < log 2}.
E[ez Ωn] = 1
n
n
∑
k=1
ez Ω(k) = e(ez−1) log logn ν0(ez) (1 + O(1/ logn)).
Recall that the constant in the O symbol is uniform on sets{y,|y|≤ 2− δ}, that is on
bands{z, Re(z) < log(2− δ)}. In particular the convergence is uniform on compact
sets. Therefore, one has the following result.
Proposition 7.10. The sequence of random variables (Ωn)n≥1 converges mod-Poisson with
parameter t n = log2 n and limiting function ψ(z) = ν0(ez), on the band S(−∞,log 2). This
takes place with speed of convergence O(1/ log(n)), that is O((tn)−ν), for all ν > 0.
As for ωn, this implies precise deviation results. However, as the convergence only
takes place on a band, the range of these results is limited (note the condition x < 2 in
the theorem below).
Theorem 7.11. Fix x with 0 < x < 2. Assume x log2 n∈ N. Then
P[Ωn = x log2 n] = ν0(x) ( 1 + O(1/ log2 n))
(log n)x log(x)−x+1√
2πx log2 n. (32)
Furthermore, if 1 < x < 2,
P[Ωn≥ x log2 n] = ν0(x) ( 1 + O(1/ log2 n))
(log n)x log(x)−x+1√
2πx log2 n
1
1− 1
x
. (33)
Again, the ﬁst equation was discovered by Selberg [Sel54] and can be found in a
slightly different form in [Ten95, Section II.6, Theorem 5].
MOD-φ CONVERGENCE, I 53
Remark 7.12. An extension of Equation (32) for x > 2 is given in [Ten95, Section II.6,
Theorem 6]. This involves the type of singularity of the limiting function ν0(ez) at the
edge of the convergence domain. Here, ν0(y) has only a simple pole in y = 2, and the
residue appears in the deviation results. It would be interesting to see if this kind of
idea can be used in the general framework of mod- φ convergence, but this is outside
the scope of this already quite long paper.
7.2.3. Other arithmetic functions. In this paragraph, we generalize the two examples ωn
and Ωn above. The goal is to understand the phase transition between the convergence
on a band and the convergence on the complex plane.
Let f : N→ Z be a function with the following properties:
(i) f is additive, that is f (mn) = f (m) + f (n) if m∧ n = 1;
(ii) for every prime p, one has f (p) = 1.
We necessarily have f (1) = 0. For C > 0, we say that such a function has a C-linear
growth if there exists B such that
| f (pk)|≤ B + C k for any p∈ P and any k > 0.
If f has a C-linear growth for any C > 0, we say that f has a sublinear growth. In
particular, since Ω(pk) = k (for all p and k), the function Ω has a 1-linear growth,
while ω has a sublinear growth (for all p and k, ω(pk) = 1). We are interested in
the random variable fn, which is equal to the value f (k) of f on a random integer k
chosen uniformly between 1 and n. Note that the additivity condition ensures that the
following Dirichlet series factorizes:
F(y, s) :=
∞
∑
k=1
y f (k)
ks = ∏
p∈P
(
1 + y f (p)
ps + y f (p2)
p2s +···
)
.
Again, one can use the Selberg-Delange method to get precise estimates for the Laplace
transform.
Proposition 7.13. Suppose that f fulﬁlls (i) and (ii) and has a C-linear groth for some C > 0.
For any δ with 0 < δ < 1
2, we have, for any y in C with (2− 2δ)−1/C≤| y|≤ (2− 2δ)1/C,
∑
k≤n
y f (k) = n (log n)y−1 (τ0(y) + O(1/ logn)), (34)
where the constant hidden in the O symbol depends on δ, B and C (but not on y), and
τ0(y) = 1
Γ(y) ∏
p∈P
(
1 + y f (p)
p + y f (p2)
p2 +···
)(
1− 1
p
)y
.
Proof. The proof is an easy adaptation of the proof of [Ten95, Section II.6, Theorems 1
and 2]. We will only indicate the necessary modiﬁcations, assuming that the reader
can consult Tenenbaum’s book.
Fix δ ∈ (0, 1
2 ), and y in C with (2− 2δ)−1/C ≤ |y| ≤(2− 2δ)1/C. We set Y =
max(|y|,|y|−1); by assumption, 1≤ Y≤ (2− 2δ)1/C, and on the other hand,
|y f (pk)|≤ YB+Ck
54 VALENTIN FÉRAY, PIERRE-LOÏC MÉLIOT, AND ASHKAN NIKEGHBALI
as f has a C-linear growth. We have, for any prime p and|ξ| < Y−C, the bound
∑
k≥0
|y f (pk) ξk| < 1 + ∑
k≥1
YB+Ck|ξ|k≤ 1 + YB YC|ξ|
1− YC|ξ|.
Therefore, for each prime p, the following formula deﬁnes a holomorphic function for
|ξ| < Y−C≤ 1:
hy,p(ξ) =
(
1 + y f (p)ξ + y f (p2)ξ2 + . . .
)
(1− ξ)y .
Moreover, we have
|hy,p(ξ)| <
(
1 + YB YC|ξ|
1− YC|ξ|
)
eY| log(1−ξ)|.
Consider now the coefﬁcients of the power series expansion of hy,p around the origin,
i.e. the numbers by(pk) such that
hy,p(ξ) = 1 + ∑
k≥1
by(pk)ξk.
Note that by(p) = 0 for any p∈ P. With the previous hypotheses,
1
2− δ < Y−C≤| y|−C.
By Cauchy’s formula applied to the circle of radius 1/ (2− δ), one has, for any prime
p, any complex number y such that (2− 2δ)1/C≤| y|≤ (2− 2δ)1/C, and any k≥ 1:
|bw(pk)|≤ M(δ, B, C) (2− δ)k,
where
M(δ, B, C) = sup
|ξ|=1/(2−δ)
1≤Y≤(2−2δ)1/C
(
1 + YB YC|ξ|
1− YC|ξ|
)
eY| log(1−ξ)| < +∞.
Denote ζ is the Riemann zeta function. The same arguments as in the proof of [Ten95,
Section II.6, Theorem 1] shows that
G(y, s) := F(y, s) ζ(s)−y = ∏
p∈P
(
1 + ∑
k≥2
by(pk)
pks
)
is convergent and uniformly bounded for Re(s) > 3/4 and y such that (2− 2δ)−1/C≤
|y| ≤(2− 2δ)1/C. Therefore, we can apply [Ten95, Section II.5, Theorem 3], which
gives the asymptotic formula (34). □
Setting y = ez, Proposition 7.13 can be rewritten as an asymptotic formula for the
Laplace transform of fn:
E[ez f n] = 1
n
n
∑
k=1
ez f (k) = e(ez−1) log logn) (τ0(ez) + O(1/ logn)),
where the constant hidden in O depends on δ, B and C, but is uniform on |Re(z)|≤
(log(2− 2δ))/C. This yields the following mod-convergence result:
MOD-φ CONVERGENCE, I 55
Proposition 7.14. Assume f is an arithmetic function that fulﬁlls (i) and (ii) and has a C-
linear growth for some constant C > 0. Then, the sequence of random variables ( fn)n≥1
converges mod-Poisson with parameter t n = log2 n and limiting function ψ(z) = τ0(ez) on
the band
S(− log 2
C , log 2
C ).
This takes place with speed of convergence O(1/ logn), that is O((tn)−ν) for all ν > 0.
As a consequence, if f has a sublinear growth, then the convergence takes place on the whole
complex plane.
It is then straightforward to write deviation results, analog to Equations (31) and (33),
for a generic function f as above.
Remark 7.15. If the additive function f is non-negative, as is the case forω(n) and Ω(n),
then it is easily seen that one can perform the whole proof of Proposition 7.13 assuming
only|y|≤ (2− 2δ)1/C (but not|y|≥ (2− 2δ)−1/C). Therefore, one has in this case a
mod-Poisson convergence on the band
S(−∞, log 2
C ) instead of S(− log 2
C , log 2
C ).
