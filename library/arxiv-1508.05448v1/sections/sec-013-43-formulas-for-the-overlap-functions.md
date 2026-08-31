---
doc_id: arxiv-1508.05448v1
doc_title: "Concentration of Measure Techniques and Applications"
section_id: sec-013-43-formulas-for-the-overlap-functions
section_title: "Formulas for the Overlap Functions"
section_number: 4.3
pages: 67-93
source_pdf: 1508.05448v1.pdf
source_sha256: 57d2c717d8ec74d0
---
Chalker and Mehlig were able to relate the overlap functions to expectations of func-
tions involving all the eigenvalues. The eigenvalue distribution for the complex Gini-
bre ensemble is well-known. In fact it is one of the simplest of the various Gaussian
ensembles. For example, as Chalker and Mehlig also point out in their paper,
R(1)
N (z) = N
πN !e−N|z|2
DN−1(z), (4.20)
59
where DN−1(z) equals the determinant of the ( N− 1)-dimensional square matrix
DN(z) where the matrix entries are best indexed for j,k∈{ 0,...,N − 2} as
[DN(z)]jk =
( Nj+k+4
π2(j!)(k!)
)1/2∫
C
λ
j
λk|z−λ|2 exp(−N|λ|2)d2λ. (4.21)
By rotational invariance of all the terms in the integrand other than |z−λ|2, which
is only quadratic, it happens thatDN(z) is a tridiagonal matrix. Hence, Chalker and
Mehlig point out that it is easy to derive a recursion relation for DN−1(z). It is easier
to deﬁne a new quantity DN−1(σ−2,z ) =DN−1(σ−1N−1/2z). Then they show
Dn+1(σ−2,z ) = ( σ−2|z|2 +n + 1)Dn(σ−2,z )−σ−2n|z|2Dn−1(σ−2,z ), (4.22)
and D0(σ−2,z ) = 1, D1(σ−2,z ) = 1 + σ−2|z|2. It turns out to be easy to solve this
recurrence relation, and Chalker and Mehlig give the formula
DN−1(σ−2,z ) = ( N− 1)!
N−1∑
n=0
(σ−2|z|2)n
n! , (4.23)
which is the partial sum for the series for ( N− 1)! exp(σ−2|z|2). In order to obtain
DN−1(z) one must takeσ−2 =N. One sees that the dividing line is|z|< 1 versus|z|>
1, as to whether enough terms have been included in the partial sum to get essentially
exp(N|z|2) or not. From this it follows that the measureR(1)
N (z)d2z converges weakly
to π−11[0,1](|z|2)d2z, as N →∞ . The reason for going into so much detail in this
example is that the other examples are similar, but harder. In fact, some of the
formulas are so complicated that so far they have eluded any explicit, exact formula
(at least as far as we have been able to ﬁnd in the literature).
Another easy result which follows from these explicit formulas, but which does
not appear in the paper of Chalker and Mehlig, is the scaling formula near the unit
circle. Let us record this for later reference.
60
Lemma 4.3.1. For any u∈ R,
R(1)
N (1−N−1/2u)
N→∞
−→ π−1Φ(2u) where Φ(x) = 1√
2π
∫ x
−∞
e−z2/2dz. (4.24)
Proof. Given the exact formula,
R(1)
N (1−N−1/2u) = π−1 exp(−N +N 1/2u)
N−1∑
n=0
(N−N 1/2u)n
n! , (4.25)
make the substitution n = N−N 1/2x for x∈{ N−1/2, 2N−1/2,...,N 1/2} and use
Stirling’s formula. Then replace the sum by an appropriate integral in x (of which
it is a Riemann sum approximation with ∆ x = N−1/2) by using the rigorous Euler-
Maclaurin summation formula.
We may note that using the Euler-Maclaurin summation formula, one may obtain
more terms as corrections of the leading-order term, just as one does for the asymp-
totic series in Stirling’s formula. Additionally, one may obtain formulas that are valid
for more values of u: one may obtain an asymptotic formula for R(1)
N (z)−π−1 as-
suming that|z|− 1<CN −1/2 for some C, and another formula forR(1)
N (z) assuming
that|z|− 1>−CN−1/2 for some C: the diﬀerence in being whether one chooses to
asymptotically evaluate the terms which are present in the partial sum for exp(N|z|2)
or whether one chooses to asymptotically evaluate the terms which are absent in that
partial sum.
4.3.1 More Involved Formulas:
The formula for O(1)
N is not much more complicated than the formula for R(1)
N , and
Chalker and Mehlig gave the explicit answer. It turns out that one may write O(1)
N
61
similarly toR(1)
N as
O(1)
N (z) = N
πN ! exp(−N|z|2)GN−1(z) where GN−1(z) = det[GN−1(z)],
∀j,k∈{ 0,...,N − 2},
[GN−1(z)]jk =
( Nj+k+4
π2(j!)(k!)
)1/2∫
C
λ
j
λk(N−1 +|z−λ|2) exp(−N|λ|2)d2λ.
(4.26)
The matrix GN−1(z) is also tridiagonal for the same reason as DN−1(z). In par-
ticular, there is again a recursion relation for GN−1(z). Deﬁning GN−1(σ−2,z ) =
GN−1(σ−1N−1/2z), one may see the recursion formula
Gn+1(σ−2,z )
= [Gn(σ−2,z )]nnGn(σ−2,z )− [Gn(σ−2,z )]n,n−1[Gn(σ−2,z )]n−1,nGn−1(σ−2,z )
= (σ−2 +n + 2)Gn(σ−2,z )−σ−2n|z|2Gn−1(σ−2,z ),
(4.27)
with G0(σ−2,z ) = 1 and G1(σ−2,z ) = 2 +σ−2|z|2.
Lemma 4.3.2. The exact solution to the recursion relation when σ−2 =N is
GN(z) = ( N− 1)!
N−1∑
n=0
(N−n) (N|z|2)n
n! . (4.28)
Using this formula, it is easy to see thatN−1ON(z)d2z converges weakly toπ−1(1−
|z|2)1[0,1](|z|2)d2z, which is precisely the behavior that Chalker and Mehlig found by
other techniques. We will return to their approach, shortly. For now, let us state the
analogue of Lemma 4.3.1.
Corollary 4.3.3. For any u∈ R,
O(1)
N (1−N−1/2u)∼ N 1/2
π
[
e−2u2
√
2π− 2uΦ(−2u)
]
, as N→∞ . (4.29)
62
Proof. The proof is perfectly analogous to the proof of Lemma 4.3.1, except we start
with Lemma 4.3.2 instead of equation (4.23).
One also needs the two point function O(2)
N in order to obtain any interesting
moments. The two-point function for the eigenvalues is easier to start with since
its distribution is known exactly. Using ideas related to the theory of orthogonal
polynomials, one may see that R(2)
N (z1,z 2) is determinantal. The canonical general
reference for this is [Mehta, 2004]. One may write the formula as
R(2)
N (z1,z 2) = π−2e−N|z1|2
e−N|z2|2
det (KN(zjzk))2
j,k=1 for KN(z) =
N−1∑
n=0
(Nz )n
n! .
(4.30)
From this one may determine the following asymptotics, proved in the same way as
before.
Lemma 4.3.4. DeﬁneC(2)
N (z1,z 2) = R(2)
N (z1,z 2)−R (1)
N (z1)R(1)
N (z2), the corrected
correlation function for the eigenvalues. Then for any ﬁxed u1,u 2∈ C
C(2)
N (1−N−1/2u1, 1−N−1/2u2)∼ π−2e−|u1−u2|2
|Φ(−u1−u2)|, (4.31)
where the deﬁnition of Φ is extended to the complex plane as
Φ(−u) = (2 π)−1/2e−u2/2
∫ ∞
0
e−x2/2e−uxdx
We have stated a somewhat precise limit for R(2)
N , but we do not know how to
get a precise limit for O(2)
N . Let us state one of Chalker and Mehlig’s main results as
a conjecture. In other words, they give a good argument for the calculation of O(2)
N
which is highly plausible on the basis of mathematical reasoning, but to the best of
our knowledge their result has not yet been fully rigorously proved.
Conjecture 4.3.5 (Chalker and Mehlig) . (i) For any two points z1,z 2 such that
63
|z1|< 1,|z2|< 1 and|z1−z2|> 0,
O(2)
N (z1,z 2)
N→∞
−→ −1
π2· 1−z1z2
|z1−z2|4. (4.32)
(ii) For any ω∈ C and z such that|z|< 1,
N−2O(2)
N
(
z + 1
2N−1/2ω,z− 1
2N−1/2ω
)
∼− π−2(1−|z|2) 1− (1 +|ω|2)e−|ω|2
|ω|4 ,
as N→∞ . (4.33)
Importantly, there is no asymptotic formula for z1 and z2 near the boundary of
the circle. For all the other cases, this regime gives lower-order corrections, beyond
the leading order.
Chalker and Mehlig’s approach is beautiful and compelling. They calculated an
explicit formula for O(2)
N (0,z ). Note, for instance, that R(2)
N (0,z ) = π−1(R(1)
N (z)−
π−1e−|z|2
), so the formula simpliﬁes when one of the arguments is 0. A similar fact
holds forO(2)
N (z1,z 2), even though it seems that it is not determinantal likeR(2)
N (z1,z 2).
Then, Chalker and Mehlig considered a universality-type argument to see how the
functional form should behave under transformations of the point 0 to other places on
the circle. Their argument is also a universal argument, applying to more ensembles
than just the complex Ginibre ensemble, but we will continue to consider just the
complex Ginibre ensemble, here.
The second part of their argument is the key to their formula. The function
O(2)
N (z1,z 2) may be expressed as the expectation of a non-local function of all the
eigenvalues ofAn. Chalker and Mehlig observe that the function depends mainly on
the eigenvalues in a core small area around z1 and z2. For this core, the distribution
of the eigenvalues should be universal, not depending on the proximity of z1 and
z2 to the boundary of the disk, as long as they are not near the boundary. Then
outside the core there is a self-averaging contribution of all the other eigenvalues,
64
which may be reduced to a Riemann integral approximation, and calculated. That
part does depend on the geometry of the point conﬁguration in the disk, but it is
easily calculated. Putting these two parts together with their formula for O(2)
N (0,z ),
they were able to arrive at (4.33).
The reader is advised most strongly to consult their beautiful paper.
Now we want to explain brieﬂy the ﬁrst part of their argument since it is a basis for
a diﬀerent proposal we have for how to prove their conjecture. Chalker and Mehlig
point out that O(2)
N (z1,z 2) may be calculated as the determinant of a 5-diagonal
matrix. In fact, it is easier to start with R(2)
N (z1,z 2):
R(2)
N (z1,z 2) = N 3
π2N!|z1−z2|2e−N|z1|2
e−N|z2|2
FN−2(z1,z 2), (4.34)
whereFN−2(z1,z 2) equals the determinant of the (N− 2)-dimensional square matrix
FN−2(z1,z 2), where
[FN−2(z1,z 2)]jk =
( Nj+k+6
π2(j + 1)!(k + 1)!
)1/2∫
C
λ
j
λk|z1−λ|2|z2−λ|2 exp(−N|λ|2)d2λ,
(4.35)
for j,k = 0,...,N − 3. Then the formula for O(2)
N (z1,z 2) is
O(2)
N (z1,z 2) = − N 2
π2N!e−N|z1|2
e−N|z2|2
HN−2(z1,z 2), (4.36)
whereHN−2(z1,z 2) equals the determinant of the (N− 2)-dimensional square matrix
HN−2(z1,z 2), where
[HN−2(z1,z 2)]jk =
( Nj+k+6
π2(j + 1)!(k + 1)!
)1/2
∫
C
λ
j
λk
[
|z1−λ|2|z2−λ|2 +N−1(
z1−λ
)
(z2−λ)
]
exp(−N|λ|2)d2λ, (4.37)
forj,k = 0,...,N −3. These are naturally 5-diagonal because of rotational invariance.
65
However, notice that if z1 = 0 or z2 = 0 then they become tri-diagonal again. Hence,
they are more easily calculable in that case. That is why O(2)
N (0,z ) is calculable.
In a later section, we are going to propose another method to proceed. We will
write down the recursion relation for the 5-diagonal matrix, which is harder than
for a tridiagonal matrix. Then, even if the formula is not exactly solvable, we argue
that it should be asymptotically solvable. We give more details in a later section, in
particular carrying out the asymptotic approach for the easier problem of calculating
R(2)
N (z) (which we may check against the exact solution).
4.4 Moments and Constraints on the Overlap Func-
tions
An ideal situation would be to ﬁnd an explict sum-formula for O(2)
N (z1,z 2), just as
Lemma 4.3.2 provides forO(1)
N (z), but so far, this has not been discovered. In the next
section, we will suggest a rigorous approach which may work to give the asymptotics,
even when no explicit formula is known. For now, let us state the constraints imposed
by the moment formula from before.
Recall from (4.19) for any nonnegative integers p and q,
mN((p); (q)) =
∫
C
zpzqO(1)
N (z)d2z +
∫
C
∫
C
zpwqO(2)
N (z,w )d2zd 2w.
Moreover, from the discussion at the end of Section 4.1.1,mN((p); (q)) equals 0 unless
p =q, and as noted at the end of Section 4.2, this is already reﬂected in the rotational
invariance properties ofO(1)
N (z) andO(2)
N (z1,z 2). Therefore, specializing, we see that
∫
C
|z|2pO(1)
N (z)d2z +
∫
C
∫
C
zp
1zp
2O(2)
N (z1,z 2)d2z1d2z2 = 1 , (4.38)
for each nonnegative integer p. This is the constraint formula. Let us now analyze
66
this formula, starting with the leading order terms, and going down in order.
4.4.1 Cancelling Divergences at Leading Order
For any ﬁxed z with|z|< 1, we have
O(1)
N (z)∼ Nπ−1(1−|z|2), (4.39)
and the corrections are actually exponentially small in N (since they arise as the
deep part of the right tail of the series for the exponential). Therefore, integrating,
we obtain the leading-order part of the contribution from O(1)
N (z) from the formula
above ∫
C
|z|2pO(1)
N (z)d2z∼ Nπ−1
∫
C
|z|2p(1−|z|2)1[0,1)(|z|2)d2z. (4.40)
The corrections to this formula are not exponentially small, incidentally. This is
because the formula forO(1)
N (z) is not exponentially close to the exact formula for all
z in the complex plane. For a ﬁxed|z|> 1 it is easy to see thatO(1)
N (z) is exponentially
small (hence exponentially close to the approximating function of 0 there). That is
because one only has the series for the exponential up to a small number of terms,
deep in the left tail. Near the circle, there are algebraic corrections, not exponential
ones.
Nevertheless, let us note that, by making a polar decomposition, z = reiθ, we
obtain
Nπ−1
∫
C
|z|2p(1−|z|2)1[0,1)(|z|2)d2z = N
∫ 1
0
tp(1−t)dt = N
(p + 1)(p + 2). (4.41)
Let us see how this cancels with the leading-order part of the O(2)
N integral.
We will use Chalker and Mehlig’s formula here for the leading-order part, even
though we do not yet know the corrections for the lower-order part near the circle.
67
Then we get
∫
C
∫
C
zp
1zp
2O(2)
N (z1,z 2)d2z1d2z2
∼−
∫
C
∫
C
(
z + ω
2N 1/2
)p(
z− ω
2N 1/2
)p
N 2π−2(1−|z|2)1[0,1)(|z|2)
1− (1 +|ω|2)e−|ω|2
|ω|4 N−1d2ωd 2z, (4.42)
where the N−1 associated to the volume-element d2ω-times-d2z is to account for the
Jacobian of the transformation from (z1,z 2) to (z,ω ). Now we will begin to separate
this formula into even another decomposition into leading terms, and sub-leading
terms. This is because, in the formulas zp
1 = (z+ 1
2N−1/2ω)p andzp
2 = (z− 1
2N−1/2ω)p,
clearly the leading order arises by ignoring the contributions of ω which each are
accompanied by negative powers of N. We really obtain, what we might call the
“leading order, leading order” term:
∫
C
∫
C
zp
1zp
2O(2)
N (z1,z 2)d2z1d2z2∼
−Nπ−2
∫
C
∫
C
|z|2p(1−|z|2)1[0,1)(|z|2) 1− (1 +|ω|2)e−|ω|2
|ω|4 N−1d2ωd 2z. (4.43)
Then it is easy to see that this splits. The integral over ω is
∫
C
1− (1 +|ω|2)e−|ω|2
|ω|4 d2ω = π
∫ ∞
0
1− (1 +t)e−t
t2 dt = π
∫ ∞
0
1
t2
(∫ t
0
se−sds
)
dt.
(4.44)
Integrating-by-parts, it is easy to see that this gives π. Therefore, we end up with
the exact negative of the leading order contribution by O(1)
N :
∫
C
∫
C
zp
1zp
2O(2)
N (z1,z 2)d2z1d2z2∼− Nπ−1
∫
C
|z|2p(1−|z|2)1[0,1)(|z|2)d2z
=− N
(p + 1)(p + 2). (4.45)
68
The fact that these two terms cancel is good, because each diverges, separately;
whereas, according to the formula, the exact answer is supposed to be 1.
4.4.2 The Sub-Leading Contribution from O(1)
N
For the ﬁrst integral, we are fortunate that the exact correction is known near the
circle. We will not attempt to keep track of the exponentially-small corrections which
are present away from the circle. Near the circle, the exact corrections are relevant
because they are not exponentially small.
Using Corollary 4.3, we know that
∫
C
|z|2pO(1)
N (z)d2z− N
(p + 1)(p + 2) =
N 1/2
π
∫
C
[
e−2u2
√
2π− 2uΦ(−2u)
]⏐⏐⏐⏐⏐
u=N 1/2(1−|z|)
|z|2pd2z +o(1), (4.46)
where the small term o(1) means that the remainder converges to 0 as N→∞ . This
remainder includes exponentially small corrections toO(1)
N (z) away from the circle, as
well as the systematic correction terms to the leading-order behavior near the circle
that arise from the Euler-Maclaurin series. The reason that these correction terms
to the Euler-Maclaurin summation formula are o(1) will arise momentarily: even the
leading order term is only order-1, constant.
Making the polar decomposition of z and then rewriting r = 1−N−1/2u so that
dr =N−1/2du (and reversing orientation of the integral), we have
∫
C
|z|2pO(1)
N (z)d2z− N
(p + 1)(p + 2)
= 2
∫ N 1/2
−∞
[
e−2u2
√
2π− 2uΦ(−2u)
]
(1−N−1/2u)2p+1du +o(1)
= 2
∫ ∞
−∞
[
e−2u2
√
2π− 2uΦ(−2u)
]
du +o(1).
(4.47)
69
In particular, this correction is independent ofp, modulo vanishingly small remainder
terms which are accumulated in theo(1). Rewriting u =x/2 and integrating by parts
gives a constant which is equal to 3/2.
We will not be able to make it to the order-1, constant terms in the N →∞
asymptotics series (in decreasing powers of N). The reason is that for O(2)
N , we do
not have suﬃciently precise asymptotics to get to that level. Instead, what we will
do next is to consider what constraints the formula for the moments imposes onO(2)
N .
4.4.3 Sub-Leading Divergences in the O(2)
N Term
We have now accounted for all the non-vanishing contributions from the O(1)
N term.
The leading-order divergence cancels with the leading-order divergence of the O(2)
N
term. The sub-leading order part of the O(1)
N contribution to the moment is already
order-1, constant, and it is independent of p. It equals 3 /2. Note that the moment
itself is also independent of p, it is 1.
Since we do not know the actual formula for O(2)
N , our plan for this section is
to consider the proposed formula for O(2)
N in the bulk. That still leads to one other
divergent contribution, diverging logarithmically in N. What this must mean is that
in the formula forO(2)
N (z1,z 2) forz1 andz2 close, and both near the circle, there must
be an edge correction, which leads to a counter-balancing divergence. This is what
we explain in some more detail, now. This subsection is detailed and technical.
We consider the proposed formula forO(2)
N that Chalker and Mehlig derived. This
is the correct formula in the bulk, following the argument of their paper, although
there is a lower-order correction near the circle. We will not include the correction
on the circle. Instead our calculations will show constraints that must be satisﬁed for
this correction formula. We use z1 =z + 1
2N−1/2ω and z2 =z− 1
2N−1/2ω so that
z1z2 =|z|2 + iIm[ωz]
N 1/2 −|ω|2
4N . (4.48)
70
Therefore, using the bulk formula we would have
∫
C
∫
C
zp
1zp
2O(2)
N (z1,z 2)d2z1d2z2
≈− N 2
π2
∫
C
∫
C
[
|z|2 + iIm[ωz]
N 1/2 −|ω|2
4N
]p(
1−
[
|z|2 + iIm[ωz]
N 1/2 −|ω|2
4N
])
· 1− (1 +|ω|2)e−|ω|2
|ω|4 1[0,1]
(⏐⏐⏐z± 1
2N−1/2ω
⏐⏐⏐
2)
N−1d2ωd 2z, (4.49)
where we use the approximation symbol ≈ to remind ourselves that this is only one
part of the eventual formula. Simplifying this, and writing z =reiθ and ω =ρeit, we
have
∫
C
∫
C
zp
1zp
2O(2)
N (z1,z 2)d2z1d2z2
≈− N
π2
∫
C
∫
C
[
r2 + irρ sin(θ−t)
N 1/2 − ρ2
4N
]p(
1−
[
r2 + irρ sin(θ−t)
N 1/2 − ρ2
4N
])
· 1− (1 +ρ2)e−ρ2
ρ4 1[0,4N]
(⏐⏐⏐ρ± 2N 1/2rei(t−θ)
⏐⏐⏐
2)
rρdrdρdθdt. (4.50)
Let us denote φ =t−θ. Integrating over the extra angular variable, simplifying
the power of ρ in the second line, and simplifying the indicator in the second line, we
obtain
∫
C
∫
C
zp
1zp
2O(2)
N (z1,z 2)d2z1d2z2
≈− 2N
π
∫
r∈[0,1]
∫
ρ>0
∫
φ∈[0,2π)
[
r2− irρ sin(φ)
N 1/2 − ρ2
4N
]p(
1−
[
r2− irρ sin(φ)
N 1/2 − ρ2
4N
])
· 1− (1 +ρ2)e−ρ2
ρ3 1[0,N 1/2R(r,φ)](ρ)rdrdρdφ, (4.51)
for
R(r,φ ) = 2
(√
1−r2 sin2(φ)−r| cos(φ)|
)
, (4.52)
71
arising from the condition|ρ± 2N 1/2reiφ|≤ 2N 1/2⇔ρ≤R(r,φ )N 1/2
Let us rewrite this once again, this time isolating diﬀerent functional terms that
we wish to consider in more detail:
∫
C
∫
C
zp
1zp
2O(2)
N (z1,z 2)d2z1d2z2
≈− 2N
π
∫
r∈[0,1]
∫
φ∈[0,2π)
(∫ N 1/2R(r,φ)
0
Fp(r,φ,ρ )W (ρ)dρ
)
rdrdφ, (4.53)
where
Fp(r,φ,ρ ) =
[
r2− irρ sin(φ)
N 1/2 − ρ2
4N
]p(
1−
[
r2− irρ sin(φ)
N 1/2 − ρ2
4N
])
, (4.54)
and
W (ρ) = 1− (1 +ρ2)e−ρ2
ρ3 . (4.55)
Now we note that we can expand
Fp(r,φ,ρ ) =
2p∑
k=0
f (k)
p (r,φ ) ρk
Nk/2. (4.56)
Odd powers of k have f (k)
p (r,φ ) which is an odd function of sin( φ). Since the rest
of the integral will contribute even factors, this means all odd powers will integrate
to zero, so we only keep track of even powers. We have already taken account of
f (0)
p (r,φ ) which is just f (0)
p (r) =r2p(1−r2). This was what gave us the leading order
divergence we considered in a past subsection.
Moreover, starting from the even power k = 4, we have
− 2N
π
∫
r∈[0,1]
∫
φ∈[0,2π)
(∫ N 1/2R(r,φ)
0
f (k)
p (r,φ ) ρk
Nk/2W (ρ)dρ
)
rdrdφ = O(1). (4.57)
The reason is thatN·N−k/2 =N−(k−2)/2 which is vanishing. This means that the lower
72
limit of integration is actually contributing a negligible correction, asymptotically for
largeN. Near the upper limit of integration, we may expand W (ρ)∼ρ−3. Therefore
we obtain near the upper limit, for k = 4, 6,... ,
− 2
πN (k−2)/2
∫
r∈[0,1]
∫
φ∈[0,2π)
f (k)
p (r,φ )
(∫ N 1/2R(r,φ)
0
ρk−3dρ
)
rdrdφ
=− 2
π
∫
r∈[0,1]
∫
φ∈[0,2π)
f (k)
p (r,φ ) [R(r,φ )](k−2)/2
k− 2 rdrdφ +o(1) = O(1). (4.58)
This only leaves the term with k = 2 which might diverge. Indeed, for this, we
just have
− 2
π
∫
r∈[0,1]
∫
φ∈[0,2π)
f (2)
p (r,φ )
(∫ N 1/2R(r,φ)
0
1− (1 +ρ2)e−ρ2
ρ dρ
)
rdrdφ.
The only divergent part of this arises near the upper limit for the ρ integral which
gives ln(N 1/2R(r,φ )) = 1
2 ln(N) + ln(R(r,φ )), so the logarithmic divergence is
− 2
π
∫
r∈[0,1]
∫
φ∈[0,2π)
f (2)
p (r,φ )
(∫ N 1/2R(r,φ)
0
1− (1 +ρ2)e−ρ2
ρ dρ
)
rdrdφ
=−ln(N)
π
∫
r∈[0,1]
∫
φ∈[0,2π)
rf (2)
p (r,φ )drdφ +O(1). (4.59)
It is easy to see that
f (2)
p (r,φ ) = 1
4r2p− p
4r2p−2(1−r2)− p(p− 1)
2 r2p−2(1−r2) sin2(φ) +pr2p sin2(φ).
(4.60)
73
Therefore, we have
∫
φ∈[0,2π]
f (2)
p (r,φ )dφ = 2π
(1
4r2p− p
4r2p−2(1−r2)− p(p− 1)
4 r2p−2(1−r2) +p
2r2p
)
= π
2
[
(p + 1)2r2p−p2r2p−2]
.
(4.61)
Therefore, the sub-leading order divergence is now
∫
C
∫
C
zp
1zp
2O(2)
N (z1,z 2)d2z1d2z2 + N
(p + 1)(p + 2) =−1
4 ln(N) +O(1). (4.62)
We may consider this particular form. It is independent of p. Near the circle, and for
z1 nearz2, the form of zp
1zp
2, to leading order is just |z|2p which is just 1, because z is
near the circle. This is the same explanation for the reason that the order-1, constant
term coming from O(1)
N term is independent of p. We also know that the moment
must be independent of p.
One could also try to calculate the order-1 contributions at this point, coming just
from the bulk formula for O(2)
N (z1,z 2). One could then check whether these combine
to a constant independent ofp. That would be yet another strong check that Chalker
and Mehlig’s formula for O(2)
N (z1,z 2) is true to very high accuracy in the bulk, and
only needs an edge correction near the circle.
It would be best to have a suﬃciently explict formula for O(2)
N (z1,z 2) to allow one
to see the correction near the circle. Then we could have an answer to settle this.
Next, we propose a method which we believe could potentially provide this.
74
4.5 Proposal to Rigorously Approach Chalker and
Mehlig’s Result
There are various ways to try to prove Chalker and Mehlig’s formula for the bulk
behavior ofO(2)
N . One way is to try to ﬁll in the details to make Chalker and Mehlig’s
argument rigorous. Their idea is to express O(2)
N in terms of the expectation of a
function of the eigenvalues, and then use the known eigenvalue marginal for the
complex Ginibre ensemble.
Here we want to propose a second method. The formula for O(2)
N (z1,z 2) is the
determinant of a 5-diagonal matrix. One may express such a determinant through a
recursion relation, although the recursion relation is signiﬁcantly more complicated
than in the tridiagonal case. It is higher order, and it is a vector valued recursion
relation for a vector with dimension greater than 1. We will not explicate this, here.
It is well-known, it just follows from Cramer’s rule, and it is widely used in numerical
codes.
Instead, what we want to advocate here is solving recursion relations, at least
asymptotically for large N, using adiabatic theory. We have not tried this yet for
O(2)
N (z1,z 2). There may be formidable diﬃculties which obstruct this approach, but
let us demonstrate the idea for an easier problem: re-deriving the formula forR(1)
N (z).
This leads to an easier problem. The key trick for this particular problem is to realize
thatR(1)
N (z), at least for the leading-order asymptotic formula, is constant in z for
|z|< 1.
4.5.1 The Recurrence Relation for R(1)
N (z) Using Matrices
We are treating the case ofR(1)
N (z) as a simpler toy model, in lieu of treating the real
problem of interest which is O(2)
N (z1,z 2). We hope to be able to handle O(2)
N (z1,z 2)
later, in another paper.
75
Recall from (4.20) that R(1)
N (z) = π−1[(N− 1)!]−1 exp(−N|z|2)DN−1(z), which
means from Stirling’s formula that
R(1)
N (z)∼ 1
π· 1√
2πN
e−(N−1) ln(N)+N(1−|z|2)DN−1(z). (4.63)
Moreover, recall that there is a recursion relation in (4.22). Namely, deﬁningDN−1(σ−2,z ) =
DN−1(σ−1N−1/2z), it happens that
Dn+1(σ−2,z ) = ( σ−2|z|2 +n + 1)Dn(σ−2,z )−σ−2n|z|2Dn−1(σ−2,z ).
Let us ﬁx σ2 =N−1 as Chalker and Mehlig do. Then
Dn+1(N,z ) = ( N|z|2 +n + 1)Dn(N,z )−Nn|z|2Dn−1(N,z ). (4.64)
Also, since the answer only depends on the magnitude of z, let us write r =|z| so
Dn+1(N,r ) = ( Nr 2 +n + 1)Dn(N,r )−Nnr 2Dn−1(N,r ). (4.65)
We want to calculateR(1)
N (r) which is asymptotically given by
R(1)
N (r)∼ 1
π· 1√
2πN
e−(N−1) ln(N)+N(1−r2)DN−1(N,r ). (4.66)
Now since we have a second-order recursion relation, let us deﬁne a two-dimensional
vector vn = [Dn−1(N,r ),Dn(N,r )]∗. (All our vectors and matrices will be real but
we use the adjoint instead of the transpose because we want to keep the symbol T
for other purposes.) Then the recursion relation says that
vn+1 = Anvn, A n =

 0 1
−Nnr 2 Nr 2 +n + 1

 , (4.67)
and we want DN−1(N,r ) = e∗
2vN−1, where {e1,e 2} is the standard basis for R2. In
76
order to have a simpler formula, we note that we can write v1 =A0e2, for A0 deﬁned
as above. In seeking R(1)
N (r), we really have
R(1)
N (r)∼ 1
π· 1√
2πN
e−(N−1) ln(N)+N(1−r2)e∗
2AN−2··· A1A0e2. (4.68)
The idea is to try to express this using the spectral decomposition of the matrices
An, where we use the fact that the matrices An are varying slowly in n, as much as
possible. This is why we call this the adiabatic approach.
4.5.2 Spectral Formulas and Summary of Main Contribution
We may summarize the spectral information as
λ±
n = N
2

r2 + n + 1
N ±
√(n + 1
N −r2
)2
+ 4r2N−1

 ,
V±
n =

 1
λ±
n

 , W ±
n =± 1
λ+
n−λ−
n

−λ±
n
1

 ;
AnV±
n = λ±
nV±
n , (W±
n )∗An = λ±
n (W±
n )∗, (Wσ
n )∗Vτ
n = δσ,τ, for σ,τ ∈{ +1,−1}.
(4.69)
In particular, An =λ+
nV +
n (W +
n )∗ +λ−
nV−
n (W−
n )∗. Therefore, we can rewrite the con-
clusion of the recursion relation as
R(1)
N (r)∼ 1
π· 1√
2πN
e−(N−1) ln(N)+N(1−r2)e∗
2AN−2··· A1A0e2
= 1
π· 1√
2πN
e−(N−1) ln(N)+N(1−r2)
∑
σ∈{+1,−1}N−1
(N−2∏
n=0
λσ(n)
n
)
([Wσ(0)
0 ]∗e2)(e∗
2Vσ(N−2)
N−2 )
·
(N−1∏
n=0
[Wσ(n+1)
n+1 ]∗Vσ(n)
n
)
.
(4.70)
77
Anticipating that the main contribution to this sum will be σ(0) =··· =σ(N− 1) =
+1, we may rewrite this as
R(1)
N (r)∼ 1
π· 1√
2πN
e−(N−1) ln(N)+N(1−r2)MN(r)PN(r), (4.71)
whereMN(r) is the “main term”
MN(r) =
(N−2∏
n=0
λ+
n
)
([W +
0 ]∗e2)(e∗
2V +
N−2)·
(N−1∏
n=0
[W +
n+1]∗V +
n
)
, (4.72)
andPN(r) will be a series of perturbations
PN(r) =
∑
σ∈{+1,−1}N−1
(N−2∏
n=0
λσ(n)
n
λ+
n
)
([Wσ(0)
0 ]∗e2)(e∗
2Vσ(N−2)
N−2 )
([W +
0 ]∗e2)(e∗
2V +
N−2) ·
(N−1∏
n=0
[Wσ(n+1)
n+1 ]∗Vσ(n)
n
[W +
n+1]∗V +
n
)
.
(4.73)
We know that we are trying to ﬁnd that the leading order behavior of R(1)
N (r) is
as follows: it is constant, equal to π−1, for r < 1, and it is exponentially small for
r >1. We will not try to recover the boundary behavior near r = 1 in this note. (In
fact, what we hope to be able to do in a later paper is to calculate O(2)
N (z1,z 2) in a
similar way, and especially to determine the edge behavior when z1 and z2 are near
the circle.) Let us quickly note how we may dispense with the r >1 case so that we
may focus on r <1.
The largest contribution toMN(r) comes from the product of eigenvalues
(N−2∏
n=0
λ+
n
)
= exp
[N−2∑
n=0
ln(λ+
n )
]
= e(N−1) ln(N) exp


N−2∑
n=0
ln

1
2

r2 + n + 1
N +
√(n + 1
N −r2
)2
+ 4r2N−1





 .
(4.74)
Moreover, deﬁning tn+1 = (n + 1)/N, the sum is ( N− 1) times a Riemann sum
78
approximation so that:
1
N ln
[
e−(N−1) ln(N)
(N−2∏
n=0
λ+
n
)]
=
∫ 1
0
ln
(1
2
(
r2 +t +
√
(t−r2)2 + 4r2N−1
))
dt +o(1)
=
∫ 1
0
ln
(1
2
(
r2 +t +
√
(t−r2)2
))
dt +o(1)
=
∫ 1
0
ln(max{r2,t})dt +o(1),
(4.75)
where the remainder term o(1) is a quantity which converges to 0 as N→∞ . Hence
we may see, by integrating, that
lim
N→∞
1
N ln
[
e−(N−1) ln(N)
(N−2∏
n=0
λ+
n
)]
=



ln(r2) if r≥ 1,
r2− 1 if r∈ [0, 1].
(4.76)
This means that, incorporating the exponential part of the prefactor for R(1)
N (r),
lim
N→∞
1
N ln
[
e−(N−1) ln(N)+N(1−r2)
(N−2∏
n=0
λ+
n
)]
=



0 if r∈ [0, 1],
ln(r2)− 1 +r2 if r >1,
(4.77)
and it is easy to see that ln(x)≤x− 1 for all x∈ (0,∞) by convexity of− ln(x). For
r >1 this is exponentially small: to leading order eN[ln(r2)−1+r2]. We claim that no
other factor is exponentially large, so that we obtain
lim
N→∞
N−1 ln(R(1)
N (r)) =



0 if r∈ [0, 1],
ln(r2)− 1 +r2 if r >1.
(4.78)
Therefore, we will henceforth assume r <1.
When r <1, we claim that we need to do a more careful analysis of the product.
The time scale tn =n/N is too rough when tn is near r2. The purely discrete scale n
79
is too ﬁne. Therefore, we use the intermediate time scale Tn = (tn−r2)N 1/2, instead.
Then we may rewrite
λ+
n = N exp(ψ+(Tn+1)),
ψ+(Tn+1) = ln
(
r2 + 1
2N−1/2Tn+1 + 1
2N−1/2
√
T 2
n+1 + 4r2
)
(4.79)
so that (N−2∏
n=0
λ+
n
)
= NN−1 exp
(N−1∑
n=0
ψ+(Tn+1)
)
. (4.80)
Then we use the Euler-Maclaurin summation formula to obtain all other terms in the
asymptotic series which are signiﬁcant, including some boundary terms that come
with the Euler-Maclaurin formula. (To do an integral such that
∫ (1−r2)N 1/2
−r2N 1/2 ψ+(T )dT ,
one may ﬁnd it useful to deﬁne T = 2r sinh(x) so that dT = 2r cosh(x)dx and
√
T 2 + 4r2 = 2r cosh(x), as well. Doing all this leads to
(N−2∏
n=0
λ+
n
)
∼ e·r(1−r2)eN ln(N)−N(1−r2). (4.81)
It is also easy to use the deﬁnitions of V +
n and W +
n to show that
[W +
0 ]∗e2∼ N−1r−2 and e∗
2V +
N−2∼ N. (4.82)
Using the Euler-Maclaurin summation formula, one may also prove that
N−1∏
n=0
[W +
n+1]∗V +
n ∼ r
1−r2N−1/2. (4.83)
The details of the Euler-Maclaurin summation formula for this product as well as
for the product of the eigenvalues are not trivial. (The product of the eigenvalues is
harder than the product of the inner-products.) They may be done, in particular, by
80
using the intermediate time-scale parameter Tn. Therefore, we obtain
MN(r) = e
√
Ne (N−1) ln(N)−N(1−r2). (4.84)
Therefore, since
R(1)
N (r)∼π−1(2πN )−1/2 exp(−(N− 1) ln(N) +N(1−r2))MN(r)PN(r)
we see that
R(1)
N (r)∼ π−1 e√
2πPN(r). (4.85)
Now we will argue thatPN(r) is actually independent of r, to leading order.
4.6 Invariance of the Perturbation Series PN (r)
Let us write
PN(r) =
∑
σ∈{+1,−1}N−1
PN(σ;r), (4.86)
for
PN(σ;r) =
(N−2∏
n=0
λσ(n)
n
λ+
n
)
([Wσ(0)
0 ]∗e2)(e∗
2Vσ(N−2)
N−2 )
([W +
0 ]∗e2)(e∗
2V +
N−2) ·
(N−1∏
n=0
[Wσ(n+1)
n+1 ]∗Vσ(n)
n
[W +
n+1]∗V +
n
)
. (4.87)
Let us think of σ as a sequence of switches, from the + state to the − state, or
vice-versa.
81
Using the notation tn =n/N and Tn =N 1/2(tn−r2), we may write
[Wτ
n+1]∗(Vσ
n−Vσ
n+1) = − τN−1/2
2
√
T 2
n+1 + 4r2
(
1 +σ Tn +Tn+1√
T 2
n + 4r2 +
√
T 2
n+1 + 4r2
)
=− τ
2
√
T 2
n+1 + 4r2
(
1 +σ Tn +Tn+1√
T 2
n + 4r2 +
√
T 2
n+1 + 4r2
)
∆Tn,
(4.88)
where we deﬁne ∆Tn = Tn+1−Tn = N−1/2. This means that in a time ∆ Tn there
is a factor proportional to ∆ Tn contributing toPN(σ;r), if we switch from σ = +
to τ =− or from σ =− to τ = + because in these cases [ Wτ
n+1]∗Vσ
n+1 = 0. This is
representative of a Poisson process of jumps.
Moreover, if at a one jumps from + to − and at b one jumps back to +, then for
all n∈{a,...,b − 1} there is a contribution to PN(σ;r) equal to
λ−
n
λ+
n
· [W−
n+1]∗V−
n
[W +
n+1]∗V +
n
= r2 + 1
2N−1/2Tn+1− 1
2N−1/2√
T 2
n+1 + 4r2
r2 + 1
2N−1/2Tn+1 + 1
2N−1/2
√
T 2
n+1 + 4r2
·
1 + 1
2
√
T 2
n+1+4r2
(
1− Tn+Tn+1√
T 2n+4r2+
√
T 2
n+1+4r2
)
∆Tn
1− 1
2
√
T 2
n+1+4r2
(
1 + Tn+Tn+1√
T 2n+4r2+
√
T 2
n+1+4r2
)
∆Tn
,
(4.89)
and this quantity is asymptotic to exp
(
−
[ √
T 2
n+1+4r2
r2+ 1
2N−1/2Tn+1
− 1√
T 2
n+1+4r2
]
∆Tn
)
, when
one takes N →∞ if one also takes a sequence of TnN such that |TnN|/N1/2→ 0.
Moreover the product is decreasing very rapidly as|Tn| gets large on an order-1 scale.
Therefore, the correction to this asymptotic formula is neglible, for the purpose of
calculating the leading order behavior of PN(r). Therefore, deﬁning P++
N (r) to be
the sum of those PN(σ;r) with σ starting at + at the left endpoint and returning
to + at the right endpoint, with some number of intervals of − in between, we have
the eﬀect of switching from + to −, staying at− for an interval, and then switching
82
back. This gives
lim
N→∞
P++
N (r) = 1 +
∞∑
K=1
∫
−∞<S1<···<S2K<∞
K∏
k=1

 1
2
√
S2
2k−1 + 4r2

1 + S2k−1√
S2
2k−1 + 4r2




exp
(
−
K∑
k=1
∫ S2k
S2k−1
[√
s2 + 4r2
r2 − 1√
s2 + 4r2
]
ds
)
K∏
k=1
[
− 1
2
√
S2
2k + 4r2
(
1− S2k√
S2
2k + 4r2
)]
dS1··· dS2n
= 1 +
∞∑
K=1
(−1)K
∫
−∞<x1<···<x2K<∞
K∏
k=1
( 1
[1 + exp(−2x2k−1)][1 + exp(2x2k)]
)
exp
(
−
K∑
k=1
∫ x2k
x2k−1
[4 cosh2(x)− 1]dx
)
dx1··· dx2K,
(4.90)
where we made the change of variables Sk = 2r sinh(xk), which is useful, as we have
also mentioned before. Let us comment on where the r-dependence went. In fact the
limits of integration for S1 andS2K should be−r2N 1/2 <S 1 andS2K < (1−r2)N 1/2.
Since the exponentials are negative (and growing in magnitude), the integrand is
converging rapidly. Therefore, we can replace the limits of integration, by allowing
integrals over all space, with a correction due to the tails of the integrals which are
exponentially small. Then the substitution we have made from Sk to xk eliminates
the r dependence, entirely. Finally, we mention that we can do the integral in the
83
exponential to simplify the formula, a bit:
lim
N→∞
P++
N (r)
= 1+
∞∑
K=1
(−1)K
∫
−∞<x1<···<x2K<∞
exp
( K∑
k=1
[
− ln
(
1 +e−2x2k−1
)
+ sinh(2x2k−1)−x2k−1
]
)
exp
(
−
K∑
k=1
[
ln
(
1 +e2x2k
)
+ sinh(2x2k)−x2k
]
)
dx1··· dx2K
= 1 +
∞∑
K=1
(−1)K
·
∫
−∞<x1<···<x2K<∞
e− ∑K
k=1(ln[cosh(x2k−1)]+ln[cosh(x2k)]+sinh(2x2k)−sinh(2x2k−1))dx1··· dx2K.
(4.91)
Again, note that this is rapidly decreasing as x1 → −∞or x2K → ∞. To get
the analogous terms P+−
N (r),P−+
N (r) and P−−
N (r), we can just alter this formula
essentially by taking x1→−∞ or x2K→∞ or both. (This is not entirely correct
because we lose terms corresponding to the density for crossing, but morally it is still
correct because the terms remaining are certainly going to 0.) Therefore
lim
N→∞
PN(r) = lim
N→∞
P++
N (r). (4.92)
Since we know that limN→∞R(1)
N (r) must equalπ−1 on the disk (for instance because
the area of the disk is 1) this leaves the calculation to show that
1+
∞∑
K=1
(−1)K
∫
−∞<x1<···<x2K<∞
e− ∑K
k=1(ln[cosh(x2k−1)]+ln[cosh(x2k)]+sinh(2x2k)−sinh(2x2k−1))dx1··· dx2K
?
=
√
2π
e . (4.93)
At this time we cannot see a direct method to prove this, but we hope to explore it
in a later paper.
84
