---
doc_id: arxiv-0911.3569v1
doc_title: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS"
section_id: sec-004-23-univariate-stable-polynomials
section_title: "Univariate stable polynomials."
section_number: 2.3
pages: 4-6
source_pdf: 0911.3569v1.pdf
source_sha256: 4e7c15c9724fb453
---
stable if and only if it has only real roots. Let f and g be two such polynomials,
let ξ1≤ξ2≤···≤ ξk be the roots of f, and let θ1≤θ2≤···≤ θ𝓁 be the roots of
g. These roots are interlaced if they are ordered so that ξ1≤θ1≤ξ2≤θ2≤··· or
θ1≤ξ1≤θ2≤ξ2≤··· . For each i∈ [𝓁], let ˆgi =g/(x−θi). If deg f≤ degg and
the roots of g are simple, then there is a unique ( a,b 1,...,b 𝓁)∈ R𝓁+1 such that
f =ag +b1ˆg1 +··· +b𝓁ˆg𝓁.
Exercise 2.5. Letf,g ∈ SR[x] be nonzero and such thatfg has only simple roots,
let deg f ≤ degg, and let θ1 <··· < θ𝓁 be the roots of g. The following are
equivalent:
(a) The roots of f and g are interlaced.
(b) The sequence f(θ1),f (θ2),...,f (θ𝓁) alternates in sign (strictly).
(c) In f =ag +∑𝓁
i=1biˆgi, all of b1,...,b 𝓁 have the same sign (and are nonzero).
TheWronskian off,g ∈ C[x] is W[f,g ] =f′·g−f·g′. If f =ag +∑𝓁
i=1biˆgi as
in Exercise 2.5 then
W[f,g ]
g2 = d
dx
(f
g
)
=
𝓁∑
i=1
−bi
(x−θi)2.
It follows that if f and g are as in Exercise 2.5(a) then W[ f,g ] is either positive
for all real x, or negative for all real x. Since W[ g,f ] = −W[f,g ] the condition
that deg f ≤ degg is immaterial. Any pair f,g with interlacing roots can be
approximated arbitrarily closely by such a pair with all roots of fg simple. It
follows that for any pair f,g with interlacing roots, the Wronskian W[f,g ] is either
nonnegative on all of R or nonpositive on all of R.
Nonzero univariate polynomials f,g ∈ SR[x] are in proper position, denoted by
f≪g, if W[f,g ]≤ 0 on all of R. For convenience we also let 0 ≪f and f≪ 0 for
anyf∈ SR[x]; in particular 0≪ 0.
Exercise 2.6. Let f,g ∈ SR[x] be real stable. Then f≪g and g≪f if and only
if cf =dg for some c,d∈ R not both zero.
Hermite-Kakeya-Obreschkoﬀ (HKO) Theorem (Theorem 6.3.8 of [14]). Let
f,g ∈ R[x]. Then af +bg∈ SR[x] for all a,b∈ R if and only if f,g ∈ SR[x] and
either f≪g or g≪f.
Hermite-Biehler (HB) Theorem (Theorem 6.3.4 of [14]) . Let f,g ∈ R[x].
Then g + if∈ S[x] if and only if f,g ∈ SR[x] and f≪g.
Proofs of HKO and HB. It suﬃces to prove these when fg has only simple roots.
For HKO we can assume that deg( f)≤ deg(g). Exercise 2.5 shows that if the
roots of f and g are interlaced then for all a,b ∈ R, the roots of g and af +bg
MULTIVARIATE STABLE POLYNOMIALS 5
are interlaced, so that af +bg is real stable. The converse is trivial if cf =dg for
some c,d ∈ R not both zero, so assume otherwise. From the hypothesis, both f
and g are real stable. If there are z0,z 1∈ H for which Im(f(z0)/g(z0)) < 0 and
Im(f(z1)/g(z1))> 0, then for someλ∈ [0, 1] the numberzλ = (1−λ)z0+λz1 is such
that Im(f(zλ)/g(zλ)) = 0. Thus f(zλ)−ag(zλ) = 0 for some real number a∈ R.
Since f−ag is stable (by hypothesis) and zλ∈ H, this implies that f−ag≡ 0, a
contradiction. Thus Im( f(z)/g(z)) does not change sign for z∈ H. This implies
Exercise 2.5(c): all the bi have the same sign (consider f/g at the points θi + iϵ for
ϵ> 0 approaching 0). Thus, the roots of f and g are interlaced.
For HB, let p = g + if. Considering i p =−f + ig if necessary, we can assume
that degf≤ degg. If f≪ g then Exercise 2.5(c) implies that Im( f(z)/g(z))≤ 0
for all z∈ H, so that g + if is stable. For the converse, let p(x) =c∏d
i=1(x−ξi),
so that Im(ξi)≤ 0 for all i∈ [d]. Now |z−ξi|≥| z−ξi| for all z∈ H and i∈ [d],
so that|p(z)|≥| p(z)| for all z∈ H. For any z∈ H with f(z)⁄= 0 we have
⏐⏐⏐⏐
g(z)
f(z) + i
⏐⏐⏐⏐≥
⏐⏐⏐⏐
g(z)
f(z) + i
⏐⏐⏐⏐ =
⏐⏐⏐⏐
g(z)
f(z)− i
⏐⏐⏐⏐,
and it follows that Im( g(z)/f(z))≥ 0 for all z∈ H with f(z)⁄= 0. Since fg has
simple roots it follows that g(x) +yf (x) is stable in S[x,y ]. By contraction and
specialization, both f and g are real stable. By scaling and specialization, af +bg
is stable for all a,b ∈ R. By HKO, the roots of f and g are interlaced. Since
Im(f(z)/g(z))≤ 0 for all z∈ H, all the bi in Exercise 2.5(c) are positive, so that
W[f,g ] is negative on all of R: that is f≪g. □
For λ : N→ R, let Tλ : R[x]→ R[x] be the linear transformation deﬁned by
Tλ(xn) = λ(n)xn and linear extension. A multiplier sequence (of the ﬁrst kind) is
such a λ for which Tλ(f) is real stable whenever f is real stable. P´ olya and Schur
characterized multiplier sequences as follows.
P´ olya-Schur Theorem(Theorem 1.7 of [4]) . Letλ : N→ R. The following are
equivalent:
(a) λ is a multiplier sequence.
(b) Fλ(x) =∑∞
n=0λ(n)xn/n! is an entire function which is the limit, uniformly on
compact sets, of real stable polynomials with all roots of the same sign.
(c) Either Fλ(x) or Fλ(−x) has the form
Cxneax
∞∏
j=1
(1 +αjx),
in which C∈ R, n∈ N, a≥ 0, all αj≥ 0, and ∑∞
j=1αj is ﬁnite.
(d) For all n∈ N, the polynomial Tλ((1 +x)n) is real stable with all roots of the
same sign.
One of the main results of Borcea and Br¨ and´ en’s theory is a great generalization
of the P´ olya-Schur Theorem – a characterization of all stability preservers : linear
transformations T : C[x]→ C[x] such that T (f) is stable whenever f is stable.
(Also the analogous characterization of real stability preservers.) This is discussed
in some detail in Section 5.3.
6 DAVID G. WAGNER
