---
doc_id: download
doc_title: "Concentration of empirical distribution functions with applications to non-i.i.d. models"
section_id: sec-002-proof-of-theorem-11
section_title: "Proof of Theorem 1.1"
section_number: null
pages: 7-10
source_pdf: Download.pdf
source_sha256: ca9639465b08d34c
toc_source: outline
doc_brief: "Concentration of empirical distribution functions with applications to non-i.i.d. models — 12 sections: Front matter; Introduction; Empirical Poincaré inequalities"
---
We shall now study the concentration properties of empirical measures Fn around their mean F
based on Poincaré-type inequalities. In particular, we shall prove Theorem 1.1, which provides a
bound on the mean of the Kantorovich–Rubinstein distance
W1(Fn,F) =
 +∞
−∞
|Fn(x) −F(x)|dx.
Note that it is homogeneous of order 1 with respect to the random vector (X1,...,Xn).
We ﬁrst need a general observation.
Lemma 3.1. Given distribution functions F and G, for all real a < b and a natural number N,
 b
a
|F(x) −G(x)|dx ≤
N

k=1

 ak
ak−1

F(x) −G(x)

dx
 + 2(b −a)
N
,
where ak = a + (b −a) k
N .
Proof. Let I denote the collection of those indices k such that in the kth subinterval k =
(ak−1,ak), the function ϕ(x) = F(x) −G(x) does not change sign. Let J denote the collection
of the remaining indices. Then, for k ∈I,

k
|F(x) −G(x)|dx =


k

F(x) −G(x)

dx
.
In the other case k ∈J, since ϕ changes sign on k, we may write
sup
x∈k
|ϕ(x)| ≤Osck(ϕ) ≡sup
x,y∈k

ϕ(x) −ϕ(y)

≤Osck(F) + Osck(G) = F(k) + G(k),
where, in the last step, F and G are treated as probability measures. Hence, in this case,

k |F(x) −G(x)|dx ≤(F(k) + G(k))|k|. Combining the two bounds and using |k| =
b−a
N , we get that
 b
a
|F(x) −G(x)|dx
≤

k∈I


k

F(x) −G(x)

dx
 +

k∈J

F(k) + G(k)

|k|
≤
N

k=1


k

F(x) −G(x)

dx
 + b −a
N
N

k=1

F(k) + G(k)

.
□
Remark. As the proof shows, the lemma may be extended to an arbitrary partition a = a0 <
a1 < ··· < aN = b, as follows:
 b
a
|F(x) −G(x)|dx ≤
N

k=1

 ak
ak−1

F(x) −G(x)

dx
 + 2 max
1≤k≤N(ak −ak−1).
Let us now apply the lemma to the space (Rn,μ) satisfying a Poincaré-type inequality. Con-
sider the partition of the interval [a,b] with k = (ak−1,ak), as in Lemma 3.1. By Corollary 2.4,
E
 b
a
|Fn(x) −F(x)|dx ≤
N

k=1
E


k

Fn(x) −F(x)

dx
 + 2(b −a)
N
≤σ
√n
N

k=1

F(k) + 2(b −a)
N
.
By Cauchy’s inequality, 
N
k=1
√F(k) ≤
√
N(
N
k=1 F(k))1/2 ≤
√
N, hence,
E
 b
a
|Fn(x) −F(x)|dx ≤σ
√
N
√n + 2(b −a)
N
.
Now, let us rewrite the right-hand side as
σ
√n(
√
N + c
N ) with parameter c = 2(b−a)
σ/√n and op-
timize it over N. On the half-axis x > 0, introduce the function ψ(x) = √x + c
x (c > 0). It has
derivative ψ′(x) =
1
2√x −c
x2 , therefore ψ is decreasing on (0,x0] and is increasing on [x0,+∞),
where x0 = (2c)2/3. Hence, if c ≤1
2, we have
inf
N ψ(N) = ψ(1) = 1 + c ≤1 + c1/3.
If c ≥1
2, then the argmin lies in [1,+∞). Choose N = [x0] + 1 = [(2c)2/3] + 1 so that N ≥2
and N −1 ≤x0 < N ≤x0 + 1. Hence, we get
ψ(N) ≤

√x0 + 1

+ c
x0
= 1 + ψ(x0) = 1 +
3
22/3 c1/3.
Thus, in both cases, infN ψ(N) ≤1 +
3
22/3 c1/3 ≤1 + 3( b−a
σ/√n)1/3 and we arrive at the following
corollary.
Corollary 3.2. Under PI(σ 2), for all a < b,
E
 b
a
|Fn(x) −F(x)|dx ≤σ
√n

1 + 3
 b −a
σ/√n
1/3
.
The next step is to extend the above inequality to the whole real line. Here, we shall use the
exponential integrability of the measure F .
Proof of Theorem 1.1. Recall that the measure μ is controlled by using two independent para-
meters: the constant σ 2 and A, deﬁned by
|EXi −EXj| ≤Aσ,
1 ≤i,j ≤n.
One may assume, without loss of generality, that −Aσ ≤EXi ≤Aσ for all i ≤n.
Lemma 2.2 with g(x) = xi, t = 1 and Chebyshev’s inequality give, for all h > 0,
P{Xi −EXi ≥h} ≤3e−h/σ,
P{Xi −EXi ≤−h} ≤3e−h/σ.
Therefore, whenever h ≥Aσ,
P{Xi ≥h} ≤3e−(h−Aσ)/σ,
P{Xi ≤−h} ≤3e−(h−Aσ)/σ.
Averaging over all i’s, we obtain similar bounds for the measure F, that is, 1 −F(h) ≤
3e−(h−Aσ)/σ and F(−h) ≤3e−(h−Aσ)/σ . After integration, we get
 +∞
h

1 −F(x)

dx ≤3σe−(h−Aσ)/σ,
 −h
−∞
F(x)dx ≤3σe−(h−Aσ)/σ.
Using |Fn(x) −F(x)| ≤(1 −Fn(x)) + (1 −F(x)) so that E|Fn(x) −F(x)| ≤2(1 −F(x)), we
get that
E
 +∞
h
|Fn(x) −F(x)|dx ≤6σe−(h−Aσ)/σ
and similarly for the half-axis (−∞,−h). Combining this bound with Corollary 3.2, with
[a,b] = [−h,h], we obtain that, for all h ≥Aσ,
E
 +∞
−∞
|Fn(x) −F(x)|dx ≤σ
√n

1 + 6

h
σ/√n
1/3
+ 12σe−(h−Aσ)/σ.
Substituting h = (A + t)σ with arbitrary t ≥0, we get that
E
 +∞
−∞
|Fn(x) −F(x)|dx ≤σ
√n

1 + 6

(A + t)√n

1/3 + 12√ne−t

.
Finally, the choice t = logn leads to the desired estimate
E
 +∞
−∞
|Fn(x) −F(x)|dx ≤Cσ
A + logn
n
1/3
.
□
