---
doc_id: arxiv-2103.07383v1
doc_title: "On the Analyticity of Critical Points of the Generalized Integral Menger Curvature in the Hilbert Case"
section_id: sec-009-a-properties-of-analytic-functions
section_title: "A Properties of analytic functions"
section_number: null
pages: 25-27
source_pdf: 2103.07383v1.pdf
source_sha256: 9dca35ea16490ad8
---
In this section we aim to recall some statements related to analytic functions, which are used
in the paper. For further information on analytic functions we refer the reader for instance to
[KP02]. First we note that analytic functions can be characterized as follows, cf. for example
[Vor20, Corollary 3.2].
Proposition A.1. Letf∈C∞(R/Z, Rn) and s> 0. Then the functionf is analytic onR/Z if
there are positive constantsr and C such that
‖f(k)‖H 1+s≤Ck!
rk
holds for all integersk≥0.
This can be seen by using [KP02, Proposition 1.2.12] together with a standard covering
argument, Morrey’s inequality (see e.g. [AF03, Paragraph 4.16]), the equivalence of theW 1,2-
and the H1-norm on R/Z (cf. [Rei12, Lem. 1.2] or [AF03, 7.62]) as well as the embedding
Hs⊆Ht for anyt<s (cf. [Tay96, Chapter 4, Proposition 3.4]).
In addition, we need a special case of the Cauchy-Kovalevsky theorem, which can be derived
for example from [Fol95, (1.25)].
25
Theorem A.2 (Cauchy-Kovalevsky – ODE case).Suppose the functionG : R2n→Rn is
real analytic around(c0,c 1) for somec0,c 1∈Rn, and the functionf∈C∞((−ε,ε), Rn) of the
form f(x) = (f1(x),...,fn(x)), for anyε>0, is a solution of the initial value problem
f′′(x) =G(f(x),f′(x)) for x∈(−ε,ε) with
f(0) =c0, and
f′(0) =c1.
Then the functionf is real analytic around0.
The statement can be proven by themethod of majorants, e.g. as explained in the proof
of [KP02, 2.4.1]. At this point we remark that the strategy of proof for the main statement,
Theorem 1.2, is motivated from this method.
B Faà di Bruno’s formula
Faà di Bruno’s formula generalizes the chain rule to higher derivatives. In particular, thek-th
derivative of the composition of two functionsf,g ∈Ck(R, R) can be written as
(d
dt
{k
g(f(t)) =
∑
m1+2m2+···kmk=k,
m1,...,mk∈N0
k!
m1!1!m1m2!2!m2...mk!k!mk
g(m1+···+mk)(f(t))
k
j=1
(f(j)(t))mj.
R. Mishkov generalized Faà di Bruno’s formula to the multivariate case [Mis00]. The following
lemma and notation via the universal polynomial are taken directly from [BV19, Section 2.3].
Lemma B.1. Let U ⊆R be a neighborhood of0 and f ∈Ck(U, Rn), n∈N0. Moreover, let
V ⊆Rn be a neighborhood off(0) such thatf(U)⊆V and g∈Ck(V, R). Then we have for any
k∈N and x∈U
(d
dx
{k
g(f(x))=
∑
0
∑
1
···
∑
k
k!
k
i=1(i!)ri
k
i=1
n
j=1qij!
(∂αg)(f(x))
k
i=1
(f(i)
1 (x))qi1···(f(i)
n (x))qin
where the sums are over all non-negative integer solutions of the following equations
∑
0
:r1 + 2r2 +···+krk =k,
∑
1
:q11 +q12 +···+q1n =r1
...
∑
k
:qk1 +qk2 +···+qkn =rk
and α:= (α1,...,αn) with αj :=q1j +q2j +···+qkj for 1≤j≤n.
In the following we seldom need the precise form of Faà di Bruno’s formula in the multivariate
case but only the fact that there is a universal polynomialp(n)
k with non-negative coeﬃcients
independent off,g such that
(d
dx
{k
g(f(x)) =p(n)
k ({∂αg}|α|≤k,{f(j)
i }i=1,...,n,j=1,...,k) (20)
26
for all f ∈Ck(R, Rn) and g∈Ck(Rn, R).Furthermore, p(n)
k is one-homogeneous in the ﬁrst
entries.
Lemma B.2. Letk,n∈N, Cx,Cy > 0, x(i)
j > 0 and
yα∈
(
0,Cy
(|α|+ 1)!
r|α|+1
{
(21)
for allα∈Nn
0 with|α|≤k, i∈{1,...,k}and j∈{1,...,n}. Then, forC := max{1,Cx}
p(n)
k ({yα}|α|≤k,{Cxx(i)
j }i=1,...,k
j=1,...,n
)≤Cyp(n)
k


{
(|α|+ 1)!
(r
C
{|α|+1
{
|α|≤k
,{x(i)
j }i=1,...,k
j=1,...,n
(
(.
Note that as soon asyα=|∂αg|for some functiong which is analytic away from the origin, the
upper bound foryαin (21) automatically holds, see the proof of [BV19, Theorem 7.2].
Proof. Using the explicit form, we may compute
p(n)
k ({yα}|α|≤k,{Cxx(j)
i }i=1,...,k
j=1,...,n
)
=
∑
0
∑
1
···
∑
k
k!
k
i=1(i!)ri
k
i=1
n
j=1qij!
yα
k
i=1
n
j=1
(Cxx(i)
j )qij
≤Cy
∑
0
∑
1
···
∑
k
k!
k
i=1(i!)ri
k
i=1
n
j=1qij!
(|α|+ 1)!
r|α|+1 C|α|
x
k
i=1
n
j=1
(x(i)
j )qij,
as the sum of allqij is exactly|α|. EstimatingC|α|
x ≤C|α|+1 yields the desired result.
The explicit formula also allows us to estimate the norm of a Faà di Bruno polynomial in a
Banach algebra.
Lemma B.3. LetX be a Banach algebra with norm‖·‖in the sense that there is a universal
constantb such that forx,y∈X,‖xy‖≤b‖x‖‖y‖.
Furthermore, letk∈N and x(i)
j ,yα∈Xfor all α∈Nn
0 with|α|≤k, i∈{1,...,k}and
j∈{1,...,n}. Then,
‖‖‖‖p(n)
k ({yα}|α|≤k,{x(i)
j }i=1,...,k
j=1,...,n
)
‖‖‖‖≤p(n)
k ({b|α|‖yα‖}|α|≤k,{‖x(i)
j ‖}i=1,...,k
j=1,...,n
.
Note that in our application scenario, the product is just pointwise multiplication between func-
tions mapping toR.
Proof. The statement follows from the estimate‖m
l=1zl‖≤bm−1m
l=1‖zl‖for allzl∈Xand
the fact that theqij sum up to|α|together with the explicit formula of Faa di Bruno’s polynomial
in Lemma B.1, in particular the one-homogeneity of its ﬁrst entry.
