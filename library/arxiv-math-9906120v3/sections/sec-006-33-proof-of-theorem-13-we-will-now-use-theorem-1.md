---
doc_id: arxiv-math-9906120v3
doc_title: "Discrete orthogonal polynomial ensembles and the Plancherel measure By Kurt Johansson"
section_id: sec-006-33-proof-of-theorem-13-we-will-now-use-theorem-1
section_title: "Proof of Theorem 1.3. We will now use Theorem 1.2 to prove The-"
section_number: 3.3
pages: 18-23
source_pdf: 9906120v3.pdf
source_sha256: 436982ef45e940bd
doc_brief: "Discrete orthogonal polynomial ensembles and the Plancherel measure By Kurt Johansson — We consider discrete orthogonal polynomial ensembles which are discrete analogues of the orthogonal polynomial"
---
orem 1.3, but before we can do this we need certain asymptotic results for
ENSEMBLES AND THE PLANCHEREL MEASURE
277
Charlier polynomials and Bessel functions. Let
wa(x) = e−a ax
x! ,
x ∈N,
a > 0.
The normalized Charlier polynomials, cn(x; a), n ≥0 are orthonormal on N
with respect to this weight. The relevant value of the parameter a for us will
be a = α/M, and we deﬁne the Charlier kernel
Kα
Ch,M(x, y) = √αcM(x; α
M )cM−1(y; α
M ) −cM−1(x; α
M )cM(y; α
M )
x −y
(3.21)
× wα/M(x)1/2wα/M(y)1/2,
for x̸ = y and
(3.22)
Kα
Ch,M(x, x)
= √αwα/M(x)
h
c′
M

x; α
M

cM−1

x; α
M

−cM−1

x; α
M

c′
M

x; α
M
i
.
The polynomials cn(x; α/M), n ≥0, have the generating function
∞
X
n=0
 α
M
n/2 1
√
n!
cn

x; α
M

wn = e−αw/M(1 + w)x.
It follows from this formula that we have the following integral representations.
If 0 < r ≤√α/M, then
(3.23)
cn(x; α
M ) =
r
n!
Mn
1
2π
Z π
−π
e−√αreiθ 
1 + Mreiθ
√α
x
1
(reiθ)n dθ
and if √α/M < r, then
cn(x; α
M ) =
r
n!
Mn
1
2π
Z π
−π
e−√αreiθ 
1 + Mreiθ
√α
x
1
(reiθ)n dθ
(3.24)
−(−1)n sin πx
π
Z r
√α/M
e
√αs
Ms
√α −1
x
s−nds
s ,
for any x ∈R, where the powers are deﬁned using the principal branch of the
logarithm.
We want to write the Charlier kernel in a form that will be convenient for
later asymptotic analysis. Deﬁne, for a given r > 0, x ∈Z,
Aα
M(x) = √α M!
MM wα/M(x)

1 + M
√α
2x
e−2√α,
Dα,r
M (x, g) = 1
2π
Z π
−π
g(reiθ)e
√α(1−reiθ)
√α + Mreiθ
√α + M
x
1
(reiθ)M dθ,
278
KURT JOHANSSON
F α,r
M (x, g) = (−1)x+M+1
Z r
√α/M
g(s)e
√α(1+s)

√α −Ms
√α + M

x
s−M ds
s ,
if r > √α/M, and if r ≤√α/M, then F α,r
M (x, g) = 0. Then, some computation
shows that when x is an integer (the case we are interested in),
(3.25)
Kα
Ch,M(x, y) =
q
Aα
M(x)Aα
M(y)Dα,r
M (x, g1)Dα,r
M (y, g2) −Dα,r
M (x, g2)Dα,r
M (y, g1)
x −y
,
when x̸ = y, and
Kα
Ch,M(x, x) = Aα
M(x)

Dα,r
M (x, g2)Dα,r
M (x −1, g3) −Dα,r
M (x, g1)Dα,r
M (x −1, g4)

(3.26)
+ Aα
M(x)

F α,r
M (x, g1)Dα,r
M (x, g2) −F α,r
M (x, g2)Dα,r
M (x, g1)

,
where g1(z) ≡1, g2(z) = z −1,
g3(z) =
√α + Mz
√α + M

log
√α + Mz
√α + M

,
and g4(z) = g2(z)g3(z). Note that all the gi’s are bounded on |z| = r.
The discrete Bessel kernel is deﬁned by (1.10) for x̸ = y and
(3.27)
Bα(x, x) = √α[Lx(2√α)Jx+1(2√α) −Jx(2√α)Lx+1(2√α)]
for x = y, where Lx(t) =
d
dxJx(t). The Bessel function has the integral repre-
sentation
(3.28)
Jx(2√α) = 1
2π
Z π
−π
e
√α( 1
r e−iθ−reiθ)+ixθrxdθ −sin πx
π
Z r
0
e
√α(−1/s+s)sxds
s ,
for x ∈R, r > 0. Diﬀerentiation shows that for integer x,
Lx(2√α) = 1
2π
Z π
−π
log(reiθ)e
√α( 1
r e−iθ−reiθ)+ixθrxdθ
(3.29)
−(−1)x
Z r
0
e
√α(−1/s+s)sxds
s .
The next lemma shows that the discrete Bessel kernel is the M →∞limit
of the Charlier kernel and establishes some technical estimates. (We will only
consider the case when x, y are integers but this restriction can be removed.)
Lemma 3.7. For any x, y ∈Z,
(i)
(3.30)
lim
M→∞Kα
Ch,M(M + x, M + y) = Bα(x, y).
(ii)
(3.31)
Bα(x, y) =
∞
X
k=1
Jx+k(2√α)Jy+k(2√α).
ENSEMBLES AND THE PLANCHEREL MEASURE
279
Furthermore, there is a constant C = C(α, L), such that
(iii)
(3.32)
∞
X
x=−L
Kα
Ch,M(M + x, M + x) ≤C
if M is large enough, and
(iv)
(3.33)
∞
X
x=−L
Bα(x, x) ≤C.
(In (3.33) we can take C(α, L) = α/
√
2 + L.)
Proof. We have to show that (3.25) and (3.26) converge to (1.10) and
(3.27) respectively. Using Stirling’s formula we see that Aα
M(M + x) →√α as
M →∞. The result then follows from the integral formulas above, the fact
that
lim
M→∞e
√α(1−z)
√α + Mz
√α + M
x+M 1
zM = e
√α(1/z−z)zy,
and g3(z) →z log z as M →∞. This establishes (3.30). The identity (3.31)
follows from the recursion relation Jx+1(t) = 2xJx(t)/t−Jx−1(t), which implies
Bα(x, y) = Jx+1(t)Jy+1(t) + Bα(x + 1, y + 1),
and (3.31) follows by using the decay properties of the Bessel function; see
Lemma 3.9 below.
The estimate (3.32) is proved using the formula (3.26). Stirling’s formula
can be used to show that Aα
M(x + M) ≤2√α for all x ≥0. We have

√α + Mz
√α + M

M
1
|z|M

√α + Mz
√α + M

y
≤

1 +
√α
M|z|
M 
|z| +
√α
M
y
≤exp((1 −δ)−1√α)(1 −δ/2)y
if |z| = r = 1 −δ and M ≥2√α/δ. This estimate can be used in the integral
formulas for Dα,r
M and F α,r
M
and we obtain
|Dα,1/2
M
(M + x; gi)|, |F α,1/2
M
(M + x; gi)| ≤Ce4√α(3
4)x.
Thus,
∞
X
x=−L
Kα
Ch,M(M + x, M + x) ≤C√αe4√α
∞
X
x=−L
(3
4)x.
The estimate (iv) can be proved in a similar way but we can also proceed
as follows. Using the generating function for the Bessel functions Jn(t), n ∈Z,
280
KURT JOHANSSON
one can show that P∞
n=1 n2Jn(t)2 = t2/4, see [Wa, 2.72(3)], and P∞
n=1 Jn(t)2 =
1
2(1 −J0(t)2) ≤1/2, so by (ii) and the fact that B(x, x) ≤1,
∞
X
x=−L
Bα(x, x) ≤L +
∞
X
n=1
nJn(2√α)2 ≤α/
√
2 + L,
where we have used the Cauchy-Schwarz inequality. The lemma is proved.
We are now ready for the
Proof of Theorem 1.3. We have
Eα
Ch,M[g] =
M−1
Y
j=1
1
j!
X
λ∈ΩM
M
Y
i=1
f(λi + L −i)VM(λ)2WM(λ)
M
Y
i=1
 α
M
λi
e−α/M.
If we make the change of variables hi = λi + M −i, this can be written
Eα
Ch,M[g] =
1
Zα
M
X
h∈NM
M
Y
i=1
(1 + φ(hi −M + L))∆M(h)2
M
Y
i=1
wα/M(hi).
Now, using a standard computation from random matrix theory, see [Me],
[TW2], we can write this as
(3.34) Eα
Ch,M[g] =
M−1
X
k=0
X
h∈Nk
k
Y
i=1
φ(hi) det(Kα
Ch,M(hi+M −L, hj+M −L))k
i,j=1
since φ(t) = 0 if t < 0. The Charlier kernel is positive deﬁnite, so we have the
estimate

 det(Kα
Ch,M(xi, xj))k
i,j=1

 ≤
k
Y
j=1
Kα
Ch,M(xj, xj).
Thus, by Lemma 3.7(iii),

X
h∈Nk
k
Y
i=1
φ(hi) det(Kα
Ch,M(hi + M −L, hj + M −L))k
i,j=1

≤||φ||k
∞

∞
X
x=−L
Kα
Ch,M(M + x, M + x)
k
≤(C||φ||∞)k.
The analogous estimate for the Bessel kernel follows from Lemma 3.7(iv).
These estimates and Lemma 3.7(i) allow us to take the M →∞limit in
(3.34). By Theorem 1.2 this gives (1.18). The theorem is proved.
Note that we could just as well use Theorem 1.1 and the Meixner ensemble
to prove Theorem 1.3. The proof would be the same and we just have to prove
(3.30) and (3.32) for the Meixner ensemble instead.
ENSEMBLES AND THE PLANCHEREL MEASURE
281
