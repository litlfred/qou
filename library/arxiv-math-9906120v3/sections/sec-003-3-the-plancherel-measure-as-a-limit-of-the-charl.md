---
doc_id: arxiv-math-9906120v3
doc_title: "Discrete orthogonal polynomial ensembles and the Plancherel measure"
section_id: sec-003-3-the-plancherel-measure-as-a-limit-of-the-charl
section_title: "The Plancherel measure as a limit of the Charlier ensemble"
section_number: 3
pages: 12-27
source_pdf: 9906120v3.pdf
source_sha256: 436982ef45e940bd
toc_source: inferred
doc_brief: "Discrete orthogonal polynomial ensembles and the Plancherel measure — We consider discrete orthogonal polynomial ensembles which are discrete analogues of the orthogonal polynomial ensembles in"
---
3.1. The limit of the Charlier ensemble. The Charlier ensemble is deﬁned
by (1.16). It can be obtained as a limit of the Meixner ensemble (1.14) by
taking q = α/MN and letting N →∞with M ﬁxed. In this limit
(1 −q)MN
M−1
Y
j=0
(N −M)!
j!(N −M + j)!
M
Y
i=1
λi + N −i
λi + M −i

qλi
(3.1)
→


M−1
Y
j=1
1
j!

WM(λ)
M
Y
i=1
 α
M
λi e−α/M

,
so we obtain (1.16). In light of Theorem 1.1 we see that it is reasonable to
expect that the Poissonized Plancherel measure should be the limit of the
Charlier ensemble as M →∞. The interpretation of the Charlier ensemble
in connection with random words, Proposition 1.5, also supports this since a
random word in the limit M →∞is like a permutation (no letter is used
twice), see also [TW3]. We will give an analytical proof of Theorem 1.2 that
does not use the RSK-correspondence. We start with the following simple but
important lemma.
Lemma 3.1. If M ≥ℓ(λ), then
(3.2)
VM(λ)WM(λ) = Vℓ(λ)(λ)Wℓ(λ)(λ).
Proof. We may assume that M > ℓ(λ). Note that, by deﬁnition, λi = 0
if i > ℓ(λ). Hence,
VM(λ) = Vℓ(λ)(λ)
ℓ(λ)
Y
i=1
M
Y
j=ℓ(λ)+1
(λi + j −i)
Y
ℓ(λ)<i<j≤M
(j −i)
= Vℓ(λ)(λ)
ℓ(λ)
Y
i=1
(λi + M −i)!
(λi + ℓ(λ) −i)!
Y
ℓ(λ)<i<j≤M
(j −i).
Thus in order to prove (3.2) we must show that
Y
ℓ(λ)<i<j≤M
(j −i) =
M
Y
i=ℓ(λ)+1
(λi + M −i)!,
but this is immediate since λi = 0 if i > ℓ(λ).
Proof of Theorem 1.2. It follows from the deﬁnition (1.12) of g(λ) that
(3.3)
|g(λ)| ≤c(g)max(ℓ(λ),L) ≤c(g)ℓ(λ)+L.
ENSEMBLES AND THE PLANCHEREL MEASURE
271
Let PCh,M,N be deﬁned by (1.21). Then,
Eα
Ch,M[g] =
X
λ∈ΩM
g(λ)


M−1
Y
j=1
1
j!

VM(λ)2WM(λ)
M
Y
j=1
 α
M
λj e−α/M

(3.4)
=
∞
X
N=0
e−α αN
N!
X
λ∈Ω(N)
M
g(λ)PCh,M,N[{λ}].
Thus, by (3.3) and the fact that ℓ(λ) ≤N if λ ∈Ω(N)
M ,
(3.5)

X
λ∈Ω(N)
M
g(λ)PCh,M,N[{λ}]

 ≤c(g)L+N,
since PCh,M,N is a probability measure on Ω(N)
M . Given ε > 0 we can choose K
so large that
(3.6)

∞
X
N=K+1
e−α αN
N! c(g)L+N

 ≤ε.
Consequently,
(3.7)

Eα
Ch,M[g] −
K
X
N=0
e−α αN
N!
X
λ∈Ω(N)
M
g(λ)PCh,M,N[{λ}]

 ≤ε.
If M ≥K ≥N ≥ℓ(λ), λ ∈Ω(N)
M , we can identify Ω(N)
M
with P(N) and use
(3.2) to write
(3.8)
X
λ∈Ω(N)
M
g(λ)PCh,M,N[{λ}]
=
X
λ∈Ω(N)
M
g(λ)N!Vℓ(λ)(λ)2Wℓ(λ)(λ)2
M
Y
j=1
(λj + M −j)!
Mλj
M−1
Y
j=1
1
j!
=
X
λ∈P(N)
g(λ)PPlan,N[{λ}]
ℓ(λ)
Y
j=1
(λj + M −j)!
Mλj(M −j)! ,
where the last equality is a straightforward computation using the fact that
λj = 0 if j > ℓ(λ). Now,
ℓ(λ)
Y
j=1
(λj + M −j)!
Mλj(M −j)! =
ℓ(λ)
Y
j=1

1 −j −1
M

. . .

1 −j −ℓ(λ)
M

272
KURT JOHANSSON
which goes to 1 as M →∞for a ﬁxed λ. Since the sum in (3.7) is, for a ﬁxed
K, a sum over ﬁnitely many λ, we obtain
(3.9)
lim
M→∞
K
X
N=0
e−α αN
N!
X
λ∈Ω(N)
M
g(λ)PCh,M,N[{λ}]
=
K
X
N=0
e−α αN
N!
X
λ∈P(N)
g(λ)PPlan,N[{λ}].
Using (3.6) and the fact that PPlan,N is a probability measure on P(N), we
obtain
(3.10)

Eα
Plan[g] −
K
X
N=0
e−α αN
N!
X
λ∈Ω(N)
M
g(λ)PPlan,N[{λ}]

 ≤ε.
The theorem now follows from (3.7), (3.9) and (3.10).
3.2. Coulomb gas interpretation of the Plancherel measure. As M →∞
the number of particles in the Coulomb gas representation of the Charlier
ensemble goes to inﬁnity, so a Coulomb gas interpretation of the Plancherel
measure is not immediate. We will now show that we can actually approximate
Pα
Plan by a Coulomb gas with K particles, which gives a good approximation
if K is chosen large enough (depending on α).
Consider the Poissonization of the restriction of the Plancherel measure
to P(N)
M ,
F α
M[g] = e−α
∞
X
N=0
αN
N!
X
λ∈P (N)
M
g(λ)(f λ)2
N!
for g ∈GL. If M ≥L it follows from (1.12), (1.13) and Lemma 3.1 that
F α
M[g] = e−α X
λ∈ΩM
g(λ)VM(λ)2WM(λ)2
M
Y
i=1
αλi.
When M is large, we expect that F α
M[g] and Eα
Plan[g] should be close.
Lemma 3.2. Assume that g ∈GL and let d > 0 be given. There is a
numerical constant C such that if M ≥max(L, α exp(d + 1)), then
(3.11)

Eα
Plan[g] −F α
M[g]

 ≤C(c(g)e−d)M.
Proof. Set
RN,M[g] = Eα
Plan[g] −F α
M[g] =
∞
X
N=0
e−α αN
N!
X
λ∈P(N)\P(N)
M
g(λ)(f λ)2
N! .
ENSEMBLES AND THE PLANCHEREL MEASURE
273
If N ≤M, then RN,M[g] = 0 since then ℓ(λ) ≤P
i λi = N ≤M, so P(N) =
P(N)
M . If N > M ≥L, then |g(λ)| ≤c(g)N since λi = 0 if i > N. Thus,

Eα
Plan[g] −F α
M[g]

 ≤
∞
X
N=M+1
e−α αN
N!

RN,M[g]

≤
∞
X
N=M+1
e−α αN
N! c(g)N.
This last sum is estimated as follows.
By Stirling’s formula there is a nu-
merical constant C such that exp(−α)αN/N! ≤C exp(−αf(N/α)), where
f(x) = x log x + 1 −x.
If N/α ≥exp(d + 1), then f(N/α) ≥dN/α, and
so exp(−α)αN/N! ≤exp(−dN). The lemma is proved.
Recall from the introduction that PM can be naturally identiﬁed with
ΩM. For K < M we deﬁne
ΩM,K = {λ ∈ΩM ; λK+1 = · · · = λM = 0},
and Ω∗
M,K = ΩM \ ΩM,K. If 1 ≤j ≤M −K we set
Ω∗
M,K(j) = {λ ∈Ω∗
M,K ; λM+1−j > 0 but λi = 0, M + 1 −j < i ≤M},
so that Ω∗
M,K = ∪M−K
j=1
Ω∗
M,K(j). The next lemma asserts that ℓ(λ) is not too
large for typical λ that we will consider.
Lemma 3.3. Let g ∈GL be generated by f. Assume that f satisﬁes
(3.12)
0 ≤f(x) ≤C0f(x −1)
for all x ∈Z and some constant C0. Then
(3.13)
e−α
X
λ∈Ω∗
M,K(j)
g(λ)VM(λ)2WM(λ)2
M
Y
i=1
αλi ≤(C0α)M−j+1
(M −j + 1)!2 F α
M[g].
Proof. It will be most convenient to use the discrete Coulomb gas rep-
resentation.
Set xj = λM+1−j + j −1, j = 1, . . . , M and let ∆M(x) =
Q
1≤i<j≤M(xj −xi) be the Vandermonde determinant. Also, set A = {x ∈
NM ; 0 ≤x1 < · · · < xM} and Aj = {x ∈A ; xi < i for i < j and xj ≥j},
j = 1, . . . , M. Note that λ ∈Ω∗
M,K(j) translates into x ∈Aj. If x ∈Aj,
then xi = i −1 for i = 1, . . . , j −1 and we have the ﬁrst hole in the particle
conﬁguration x at j −1. Now,
(3.14)
X
λ∈Ω∗
M,K(j)
g(λ)VM(λ)2WM(λ)2
M
Y
i=1
αλi =
X
x∈Aj
∆M(x)2
M
Y
i=1
αxi
xi!2 f(xi + K −M).
274
KURT JOHANSSON
We want to show that, with high probability, the ﬁrst hole must be fairly close
to M. Deﬁne Tj : Aj →A by Tj(x) = (x1, . . . , xj−1, xj −1, . . . , xM −1) = x′.
Clearly, Tj : Aj →Tj(Aj) is a bijection. Write
Lα
M(x) = ∆M(x)2
M
Y
i=1
αxi
xi!2 f(xi + K −M).
For x ∈Aj,
 ∆M(x)
∆M(x′)
2 M
Y
i=1
(x′
i!)2
(xi!)2 αxi−x′
i = αM−j+1
 ∆M(x)
∆M(x′)
2 M
Y
i=j
1
x2
i
.
Since
M
Y
i=j
1
x2
i
≤
M
Y
i=j
1
i2 =
(j −1)!
M!
2
and
∆M(x)
∆M(x′) =
M
Y
k=j
xk
xk −(j −1) ≤
M
Y
k=j
k
k −(j −1) =
 M
j −1

if x ∈Aj, we obtain, using our assumption on f,
Lα
M(x) ≤(C0α)M−j+1
(M −j + 1)!2 Lα
M(Tj(x)).
Inserting this into (3.14) yields
e−α
X
λ∈Ω∗
M,K(j)
g(λ)VM(λ)2WM(λ)2
M
Y
i=1
αλi = e−α X
x∈Aj
Lα
M(x)
≤(C0α)M−j+1
(M −j + 1)!2 e−α X
x∈Aj
Lα
M(Tj(x)) ≤(C0α)M−j+1
(M −j + 1)!2 F α
M[g],
and the lemma is proved.
Lemma 3.4. Let g ∈GL be generated by f which satisﬁes (3.12). Assume
that M > K ≥max(L, e√2C0α). Then,
(3.15)

F α
M[g] −F α
K[g]

 ≤2
 C0αe2
(K + 1)2
K+1
F α
M[g].
Proof. If λ ∈ΩM,K then ℓ(λ) ≤K < M and hence by Lemma 3.1, (1.11)
and the fact that ΩM,K and ΩK can be identiﬁed we obtain
e−α
X
λ∈ΩM,K
g(λ)VM(λ)2WM(λ)2
M
Y
i=1
αλi = F α
K[g].
ENSEMBLES AND THE PLANCHEREL MEASURE
275
The left-hand side of (3.15) is
≤
M−K
X
j=1
e−α
X
λ∈Ω∗
M,K(j)
g(λ)VM(λ)2WM(λ)2
M
Y
i=1
αλi
≤
M−K
X
j=1
(C0α)M−j+1
(M −j + 1)!2 F α
M[g]
≤
∞
X
j=K+1
(C0α)j 1
j!2 F α
M[g] ≤2
 C0αe2
(K + 1)2
K+1
F α
M[g]
by (3.13). This completes the proof of the lemma.
We can now demonstrate how the Plancherel measure can be approxi-
mated by a Coulomb gas, (compare with the discussion in the Appendix in
[BDJ1]).
Proposition 3.5. Assume that g ∈GK is generated by f which satisﬁes
(3.12). Let K = [r√α], r >
√
2C0e2. Then,
(3.16)
Eα
Plan[g] = (1 + O(r−K)) 1
Zα
K
X
h∈NK
∆K(h)2
K
Y
i=1
αhi
hi!2
K
Y
i=1
f(hi),
where
Zα
K =
X
h∈NK
∆K(h)2
K
Y
i=1
αhi
hi!2 .
Proof. Write
(3.17)
Eα
Plan[g] = Eα
Plan[g] −F α
M[g] + F α
M[1]
Eα
Plan[1]
F α
M[g]
F α
K[g]
F α
K[1]
F α
M[1]
F α
K[g]
F α
K[1].
By Lemma 3.2
(3.18)
lim
M→∞F α
M[g] = Eα
Plan[g].
By Lemma 3.4 and the choice of K and r
(3.19)
F α
K[g]
F α
M[g] = 1 + O(r−K),
for any M > K, and similarly with g replaced by 1. Using (3.18) and (3.19)
in (3.17) and letting M →∞we obtain
Eα
Plan[g] = (1 + O(r−K))F α
K[g]
F α
K[1],
which is exactly (3.16). The proposition is proved.
276
KURT JOHANSSON
Thus we have an approximate Coulomb gas picture of the (shifted) rows
of λ under the Plancherel measure analogous to Dyson’s Coulomb gas picture
for the eigenvalues of a random matrix.
Remark 3.6. The conﬁning potential for the discrete Coulomb gas in
(3.16) is
V α
K[hi] = −1
K log(αhi/(hi!)2)
with limit
lim
α→∞V α
K[Kx] = 2[x log x + (log r −1)x] = V (x).
We can now use general techniques for Coulomb gases, see e.g. [Jo1], [Jo3],
to deduce asymptotic distribution properties. The potential V has the (con-
strained) equilibrium measure; compare with Section 2 in [Jo3], u(t)dt, where
u(t) =





1,
if 0 ≤t ≤1 −2/r
1
2 −1
π arcsin( r
2(t −1)),
if 1 −2/r ≤t ≤1 + 2/r
0,
if t ≥1 + 2/r.
Pick f(t) = exp(φ(t/[r√α])) with φ : R →R continuous, bounded together
with its derivative and φ(t) = 0 if t ≤0. Then,
g(λ) =
∞
Y
i=1
exp(φ(λi + [r√α] −i
[r√α]
)).
If we pick r suﬃciently large (depending on φ) we can use (3.19) and (3.20) to
show that
(3.20)
lim
α→∞
1
[r√α] log Eα
Plan[g(λ)] =
Z 1+2/r
0
φ(t)u(t)dt.
From the limit (3.20) it is possible to deduce Vershik and Kerov’s Ω-law for
the asymptotic shape of the Young diagram, [VK], see also [AD], where an
outline of the argument using the hook-integral is given. (The r-dependence
in the formulas above goes away after appropriate rescaling.) From what has
been said above we see that the Ω-law is directly related to an equilibrium
measure for a discrete Coulomb gas. Using the general results in [Jo3] we can
use (3.16) to show upper- and lower-tail large deviation formulas for λ1 (= the
length of the longest increasing subsequence in a random permutation) under
the Poissonized Plancherel measure. These formulas have been proved in [Se1],
[Jo2] and [DZ] by other methods and we will not give the details of the new
proof.
3.3. Proof of Theorem 1.3. We will now use Theorem 1.2 to prove The-
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
3.4. Asymptotics of the Plancherel measure. Theorem 1.3 can be used
to analyze the asymptotic properties of the Plancherel measure in diﬀerent
regions. One can distinguish three cases corresponding to three diﬀerent scaling
limits of the Bessel kernel. First we have the edge scaling limit,
(3.35)
lim
α→∞α1/6Bα(2√α + ξα1/6, 2√α + ηα1/6) = A(ξ, η),
where A is the Airy kernel deﬁned in (1.4). This is the case that is considered
in Theorem 1.4. Secondly we have the bulk scaling limit,
(3.36)
lim
α→∞Bα(r√α, r√α + u) = sin(uR)
uπ
,
u ∈Z, −2 < r < 2, where R = arccos(r/2); the right-hand side is the discrete
sine kernel. We will not discuss the local behavior in the bulk of the Young
diagram; see [BOO]. Thirdly we have an intermediate region,
(3.37)
lim
α→∞πα1/4−δ/2Bα(2√α −αδ + πξα1/4−δ/2, 2√α −αδ + πηα1/4−δ/2)
= sin π(ξ −η)
π(ξ −η)
,
if 1/6 < δ < 1/2, the ordinary sine kernel.
Thus in this region the local
behavior is the same as that in the bulk in a random Hermitian matrix. The
limits (3.35) to (3.37) can be proved using the saddle-point method on the
integral formula for the Bessel function. From the point of view of the Coulomb
gas picture of the Young diagram, the cases one and three are similar to the
random matrix case since at the edge a discrete Coulomb gas approximates a
continuous Coulomb gas. Case two is diﬀerent however, since in the bulk the
discrete nature is manifest; the charges sit close to each other.
Before turning to the proof of Theorem 1.4 we have to say something
about de-Poissonization, the joint distribution of the ﬁrst k rows (k largest
eigenvalues) and the asymptotics of the Bessel kernel.
We have the following generalization of a lemma in [Jo2].
Lemma 3.8. Let µN = N + 4√N log N and νN = N −4√N log N. Then
there is a constant C such that, for 0 ≤xi ≤N,
(3.38)
PµN
Plan[λ1 ≤x1, . . . , λk ≤xk] −C
N 2 ≤PPlan,N[λ1 ≤x1, . . . , λk ≤xk]
≤PνN
Plan[λ1 ≤x1, . . . , λk ≤xk] + C
N 2 .
Proof. This is proved as Lemmas 2.4 and 2.5 in [Jo2]. Denote a permu-
tation in SN by π(N) and let SN+1(j) denote the set of all π(N+1) such that
π(N+1)(N + 1) = j.
Each π(N+1) in SN+1(j) is mapped to a permutation
Fj(π(N+1)) in SN by replacing each π(N+1)(i) > j by π(N+1)(i) −1. The map
282
KURT JOHANSSON
Fj is a bijection from SN+1(j) to SN. Apply the Robinson-Schensted corre-
spondence to Fj(π(N+1)) to obtain the P-tableau. Replace the entries i by
i + 1 for i = j, . . . , N and then insert j. This insertion can only increase the
length of any row and we obtain the P-tableau for π(N+1). Thus,
λi(Fj(π(N+1))) ≤λi(π(N+1)),
for all rows. If we deﬁne g(π(N)) to be 1 if λi(πN) ≤xi for i = 1, . . . , k and 0
otherwise, we see that
g(Fj(π(N+1))) ≥g(π(N+1)),
and we can proceed exactly as in [Jo2] using the fact that the Plancherel
measure on P(N) is the push-forward of the uniform distribution on SN.
For x ∈RM, n ∈Nk and a sequence I = (I1, . . . , Ik) of intervals in R we
let χ(I, n, x) denote the characteristic function for the set of all x ∈RM such
that exactly nj of the xi’s belong to Ij, j = 1, . . . , k. A computation shows
that for a single interval
χ(Ij, nj, x) = 1
nj!
∂nj
∂znj
j
M
Y
i=1
(1 + zjχIj(xi))

zj=−1
and hence
(3.39) χ(I, n, x) =
1
n1! . . . nk!
∂n1+···+nk
∂zn1
j . . . ∂znk
j
M
Y
i=1
k
Y
j=1
(1 + zjχIj(xi))

z1=···=zk=−1
.
Note that if the intervals are pairwise disjoint, then Qk
j=1(1 + zjχIj(xi)) =
1 + Pk
j=1 zjχIj(xi); compare with [TW2].
Let P be a probability measure
on RM and let a1 ≥· · · ≥ak. Set Ij+1 = (aj+1, aj], j = 1, . . . , k −1 and
I1 = (a1, ∞). Let
Lk = {n ∈Nk ;
r
X
j=1
nj ≤r −1, r = 1, . . . , k}.
Deﬁne x(j) to be the jth largest of the xi’s. Then,
(3.40)
P[x(1) ≤a1, . . . , x(k) ≤ak] =
X
n∈Lk
E[χ(I, n, x)].
Hence, the problem of investigating the distribution function in (3.40) reduces
to investigating expectations of the right-hand side of (3.39).
In the proof of Theorem 1.4 we will need some asymptotic results for
Bessel functions.
ENSEMBLES AND THE PLANCHEREL MEASURE
283
Lemma 3.9. Let M0 > 0 be given. Then there exists a constant C =
C(M0) such that if we write x = 2√α + ξα1/6, then
(3.41)
|Jx(2√α)| ≤Cα−1/6 exp

−1
4 min
1
4α1/6, |ξ|1/2

|ξ|

for ξ ∈[−M0, ∞). Furthermore
(3.42)
lim
α→∞α1/6Jx(2√α) = Ai (ξ),
uniformly for ξ ∈[−M0, M0].
This can be deduced from classical asymptotic results, [Wa] and it is also
rather straightforward to proceed as in Section 5 of [Jo3] using the integral
formula (3.28).
We are now ready for the
Proof of Theorem 1.4. We will prove (1.20). The proof of (1.19) is analo-
gous using the Hermite kernel instead. From Lemma 3.8, the fact that a dis-
tribution function is increasing in its arguments, that the distribution function
F(t1, . . . , tk) is continuous and √µN −
√
N ≈2√log N, √νN −
√
N ≈2√log N,
we see that it suﬃces to prove that
(3.43)
lim
α→∞Pα
Plan[λ1 −1 ≤2√α + t1α1/6, . . . λk −k ≤2√α + tkα1/6] = F(t1, . . . , tk),
for any ﬁxed (t1, . . . , tk) ∈Rk, t1 ≥· · · ≥tk. Set
Ij+1 = (2√α + tj+1α1/6, 2√α + tjα1/6],
j = 1, . . . , k −1
and I1 = (2√α + t1α1/6, ∞). By (3.39) and (3.40) it is enough to consider the
expectations
(3.44)
Eα
Plan


∞
Y
i=1
k
Y
j=1
(1 + zjχIj(λj −j))

.
If we write φα(s) = Qk
j=1(1 + zjχIj(s)) −1 it follows from Theorem 1.3, with
L = 0, that the expectation (3.44) can be written as
(3.45)
Fα(z, t) =
∞
X
k=0
1
k!
X
h∈Nk
k
Y
j=1
φα(hj) det[Bα(hi, hj)]k
i,j=1.
Note that Fα(z, t) is an entire function of z. Set Jj+1 = (tj+1, tj], j = 1, . . . ,
k −1, J1 = (t1, ∞) and write ψ(s) = Qk
j=1(1 + zjχJj(s)) −1. Deﬁne
(3.46)
F(z, t) =
∞
X
k=0
1
k!
Z
Rk
k
Y
j=1
ψ(ξj) det[A(ξi, ξj)]k
i,j=1.
284
KURT JOHANSSON
We want to show that
(3.47)
lim
α→∞Fα(z, t) = F(z, t),
uniformly for z in a compact subset of Ck. Then also derivatives of Fα(z, t)
converge to the corresponding derivatives of F(z, t).
The limit (3.43) then
follows with
(3.48)
F(t1, . . . , tk) =
X
n∈Lk
1
n1! . . . nk!
∂n1+···+nk
∂zn1
1 . . . ∂znk
k
F(z, t)

z1=...zk=−1
.
So it remains to prove (3.47). Note that φα(s) = 0 if s < 2√α+tkα1/6 and
that φα(s) = ψ(α−1/6(s−2√α)). Given r ∈R we set A(r) = {r, r+1, r+2, . . . }.
Then,
(3.49)
Fα(z, t) =
∞
X
l=0
1
l!
X
h∈A(tkα1/6)l
lY
j=1
ψ
 hj
α1/6

det[ ˜Bα(ξ, η)]
1
(α1/6)l ,
where ˜Bα(ξ, η) = α1/6Bα(2√α + ξα1/6, 2√α + ηα1/6).
We can now prove
that (3.47) holds pointwise in z by the same argument as was used in the
proof of the analogous statement in Section 3 of [Jo3]. That proof depends on
the following properties of the kernel; compare with Lemma 3.1 in [Jo3] and
Lemma 4.1 below.
(i) For any M0 > 0 there is a constant C = C(M0) such that for all ξ ≥−M0
∞
X
m=1
Bα(2√α + ξα1/6 + m, 2√α + ξα1/6 + m) ≤C.
(ii) For any ε > 0, there is an L > 0 such that
∞
X
m=1
Bα(2√α + Lα1/6 + m, 2√α + Lα1/6 + m) ≤ε,
for all suﬃciently large α.
(iii) For any M0 > 0 and any ε > 0

 ˜Bα  n
α1/6 , m
α1/6

−A
 n
α1/6 , m
α1/6


 ≤ε
for all integers m, n ∈[−M0α1/6, M0α1/6] provided α is suﬃciently large.
The estimate (i) is used to estimate the tail in the k-summation in (3.49),
(ii) is used to limit the h-summation and (iii) is used to prove that the Riemann
sums converge to integrals.
If z belongs to a compact set K there is a constant C, independent of z,
such that ||ψ||∞≤C. Together with (i) this shows that the family {Fα(z, t)}
is uniformly bounded for α > 0, z ∈K and hence (3.47) holds uniformly by a
normal family argument.
ENSEMBLES AND THE PLANCHEREL MEASURE
285
The properties (i) to (iii) above are straightforward to prove using the
representation (3.31) and Lemma 3.9. To prove (i) and (ii) we use
∞
X
m=1
Bα(x + m, x + m) =
∞
X
n=1
nJ2
x+n+1(2√α),
which can be estimated using (3.41) (we get a Riemann sum).
Similarly,
˜Bα(
n
α1/6 ,
m
α1/6 ) can be written as a Riemann sum, using (3.31), which is con-
trolled using (3.41) and (3.42). This Riemann sum can be compared with the
corresponding Riemann sum for the following representation of the Airy kernel,
[TW1],
A(ξ, η) =
Z ∞
0
Ai (ξ + t)Ai (η + t)dt
and in this way we obtain (iii).
