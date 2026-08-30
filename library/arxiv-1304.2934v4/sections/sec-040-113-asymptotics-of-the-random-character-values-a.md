---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I:"
section_id: sec-040-113-asymptotics-of-the-random-character-values-a
section_title: "Asymptotics of the random character values and partitions"
section_number: 11.3
pages: 96-100
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
doc_brief: "MOD-φ CONVERGENCE, I: — In this paper, we use the framework of mod- φ convergence to prove pre- cise large or moderate deviations for quite general sequences of real valued random variables (Xn)n∈N"
---
2, and consider the random variable
Vn,k = n2/3 (X(n)
ρ − pk(ω)),
where ρ is a k-cycle. If p2k−1(ω)− (pk(ω))2 > 0, then the previous results show that
E[ezVn,k ] = exp
(
n1/3
2 σ2 z2 + 1
6 L z3
)
(1 + o(1)),
where σ and L are the quantities given in the statement of Theorem 11.4. This ends the
proof of Theorem 11.4 and Corollary 11.5. Note that the speed of convergence of the
cumulants is each time a O((αn)−1) because of the polynomial behavior established in
Lemma 11.9; therefore, one can indeed apply Proposition 5.2 with αn = n and βn =
n−1. The theorem can be extended to other permutations ρ of S(∞) than cycles: if ρ
has cycle-type µ, then deﬁne
Vn,µ = n2/3 (X(n)
ρ − pµ(ω)).
Then the generating series of Vn,µ is asymptotically given by:
E[ezVn,µ] = exp
(
n1/3
2 σ2(µ) z2 + 1
6 L(µ) z3
)
,
where σ2(µ) = limn→∞ n κ(2)(X(n)
ρµ ) and L(µ) = limn→∞ n2 κ(3)(X(n)
ρµ ) are the limit-
ing quantities given in Section 11.2.2. Hence, provided that σ2(µ) > 0, one has mod-
Gaussian convergence of Vn,µ, and the limiting variance σ2(µ) is non-zero under the
same conditions as those given in Remark 11.6. Under these conditions, one can also
easily establish mod-Gaussian convergence for every vector of renormalized random
character values (Vn,µ1, . . . ,Vn,µ𝓁)
MOD-φ CONVERGENCE, I 97
Remark 11.14. There is one case which is not covered by our theorem, but is of particular
interest: the case ω = (( 0, 0, . . .), (0, 0, . . .)). This parameter of the Thoma simplex
corresponds to the Plancherel measures of the symmetric groups, and in this case, since
p2(ω) = p3(ω) = ··· = 0, the parameters of the mod-Gaussian convergence are
all equal to 0. Indeed, the random character values under Plancherel measures do
not have ﬂuctuations of order n−1/2. For instance, Kerov’s central limit theorem ( cf.
[Hor98, IO02]) ensures that the random character values
nk/2ˆχλ(ck)√
k
on cycles ck of lengths k≥ 2 converges in law towards independent Gaussian vari-
ables; so the ﬂuctuations are of order n−k/2 instead of n−1/2. One still expects a mod-
Gaussian convergence for adequate renormalizations of the random character values;
however, the combinatorics underlying the asymptotics of Plancherel measures are
much more complex than those of general central measures — see [ ´Sni06a] — and we
have not been able to prove mod-Gaussian convergence here.
From the estimates on the laws of the random character values, one can prove many
estimates for the parts λ1, λ2, . . . of the random partitions taken under central mea-
sures. The arguments of algebraic combinatorics involved in these deductions are de-
tailed in [FM12, Mél12], so here we shall only state results. Given a partition λ =
(λ1, . . . ,λ𝓁) of size n, the Frobenius coordinates of λ are the two sequences
(
λ1− 1
2, λ2− 3
2, . . . ,λd− d + 1
2
)
,
(
λ′
1− 1
2, λ′
2− 3
2, . . . ,λ′
d− d + 1
2
)
where λ′
1, λ′
2, etc. are the sizes of the columns of the Young diagram of λ, and d is
the size of the diagonal of the Young diagram. Denote (a1, . . . ,ad), (b1, . . . ,bd) these
coordinates, and
Xλ =
d
∑
i=1
ai
n δ(
ai
n ) +
d
∑
i=1
bi
n δ(
− bi
n
).
This is a (random) discrete probability measure on [−1, 1] whose moments
pk(λ) = nk
∫ 1
−1
xk−1 Xλ(dx)
are also the moments of the Frobenius coordinates, so Xλ encodes the geometry of the
Young diagram λ. We shall also need
Xω =
d
∑
i=1
αi δ(αi) +
d
∑
i=1
βi δ(−βi) + γ δ(0),
which will appear in a moment as the limit of the random measures Xλ. Here, γ =
1− ∑∞
i=1 αi− ∑∞
i=1 βi. Notice that En,ω[X(n)
k ] = τω(ck) = Xω(xk−1).
It is shown in [IO02] that for any partition λ of size n and for any k,
pk(λ) = Σk(λ) + remainder,
where the remainder is a linear combination of symbols Σµ with|µ| < k. It fol-
lows that the cumulants of the pk’s satisfy the same estimates as the cumulants of the
Σk’s. Therefore, the rescaled random variable∇(xk−1) = n2/3 (Xλ(xk−1)− Xω(xk−1))
98 VALENTIN FÉRAY, PIERRE-LOÏC MÉLIOT, AND ASHKAN NIKEGHBALI
converges in the mod-Gaussian sense with parameters n1/3 σ2 and limiting function
ψ(z) = exp(L z3
6 ), where σ2 and L are given by the same formula as in the case of the
random character value X(n)
k , that is to say
σ2 = k2(
p2k−1(ω)− pk(ω)2)
;
L = k3(
(3k− 2) p3k−2(ω)− (6k− 3) p2k−1(ω) pk(ω) + (3k− 1) pk(ω)3)
.
Actually, one has mod-Gaussian convergence for any ﬁnite vector of random variables
∇(xk−1), k≥ 1.
We don’t know how to obtain from there moderate deviations for the partsλ1, λ2, . . .
of the partition; but one has at least a central limit theorem when one has strict inequal-
ities α1 > α2 >··· > αi >··· and β1 > β2 >··· > βi >··· (see [Mél12], and also
[Buf12]). Indeed, for any smooth test function ψi equal to 1 around αi and to 0 outside
a neighborhood of this point, one has
Xλ(ψi)− Xω(ψi) = ai
n− αi (54)
with probability going to 1, and then the quantities in the left-hand side renomalized
by√n converge jointly towards a Gaussian vector with covariance
κ(i, j) = δij αi− αiαj. (55)
So, the ﬂuctuations
√
n
( λi
n− αi
)
of the rows of the random partitions taken under central measures Pn,ω converge
jointly towards a Gaussian vector with covariances given by Equation (55), and one
can include in this result the ﬂuctuations
√
n
( λ′
j
n− βj
)
of the columns of the random partitions, with a similar formula for their covariances.
The reason why it becomes difﬁcult to get by the same technique the moderate de-
viations of the rows and columns is that in Equation (54), one throws away an event
of probability going to zero (because of the law of large numbers satisﬁed by the rows
and the columns, see e.g. [KV81]). However, one cannot a priori neglect this event in
comparison to rare events such as {ai− nαi≥ n2/3 x}; indeed, these rare events are
themselves of probability going exponentially fast to zero. Also, there is the problem
of approximation of smooth test functions by polynomials, which one has to control
precisely when doing these computations. One still conjectures these moderate devia-
tions to hold, and n2/3( ai
n− αi
)
to converge in the mod-Gaussian sense with parame-
ters n1/3(αi− α2
i ) and limiting function
ψ(z) = exp
(
αi− 3α2
i + 2α3
i
6 z3
)
MOD-φ CONVERGENCE, I 99
— this is what one obtains if we ignore the previous caveats, and still suppose the αi
and βj all distinct. As explained in [Mél12] (see also [KV86]), this would give mod-
erate deviations for the lengths of the longest increasing subsequences in a random
permutation obtained by generalized rifﬂe shufﬂe.
100 VALENTIN FÉRAY, PIERRE-LOÏC MÉLIOT, AND ASHKAN NIKEGHBALI
