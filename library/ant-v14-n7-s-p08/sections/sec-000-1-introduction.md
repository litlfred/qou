---
doc_id: ant-v14-n7-s-p08
doc_title: "Burgess bounds for short character sums evaluated at forms"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-8
source_pdf: ant-v14-n7-s-p08.pdf
source_sha256: 81b8f00fe5fbd0f6
toc_source: inferred
doc_brief: "Burgess bounds for short character sums evaluated at forms — 11 sections: Front matter; Introduction; Method of proof: an overview"
---
The celebrated Burgess bound [1957] proves that for χ a nonprincipal multiplicative Dirichlet character
modulo a prime q, the character sum
S(N, H) =
X
x∈Z
N<x≤N+H
χ(x)
is bounded for every integer r ≥1 by
|S(N, H)| ≪r H1−1/rq(r+1)/4r2 log q.
(1-1)
From this it can be deduced that S(N, H) admits a nontrivial bound o(H) for H as small as H = q1/4+κ,
for any κ > 0. Bounds for S(N, H) have many applications, and as we survey in Section 1C, Burgess’s
inﬂuential work set records that remain the best known today.
This paper proves the ﬁrst n-dimensional Burgess bound for short multiplicative character sums evalu-
ated at generic homogeneous polynomial arguments of arbitrarily large degree. Let χ be a nonprincipal
multiplicative character modulo a prime q. Let n ≥1 be a ﬁxed dimension, and F ∈Z[x1, . . . , xn] a form
of degree D. For any N = (N1, . . . , Nn) ∈Rn, H = (H1, . . . , Hn) ∈Rn
≥1, deﬁne
S(F; N, H) =
X
x∈Zn
xi∈(Ni,Ni+Hi]
χ(F(x)).
(1-2)
Given H, we will deﬁne ∥H∥= H1 · · · Hn, so that in particular, ∥H∥is a trivial bound for |S(F; N, H)|.
Previous to the work of this paper, when the lengths Hi are short, that is ≪q1/2+ε, nontrivial bounds for
MSC2010: 11L40.
Keywords: character sums.
1912
Lillian B. Pierce and Junyan Xu
S(F; N, H) of the form o(∥H∥) were known only in special cases, such as when F is a product of n
linear forms that are linearly independent over Fq, or when n = 2 and F is a binary quadratic form (see
Section 1C2 for details). In this paper, we prove nontrivial bounds for S(F; N, H) in any dimension n
for a very general class of “admissible” forms F, as long as
∥H∥Hmin ≫qn/2+κ,
for some κ > 0, where Hmin = mini Hi. In particular, this is satisﬁed when H = (H, . . . , H) with
H = qβn+κ for any κ > 0, where
βn = 1
2 −
1
2(n+1).
(1-3)
1A. Statement of the main theorem. We now provide a formal statement of the condition that a form F
must satisfy in order to be “admissible” for our main result. We only need to rule out those forms F for
which a nontrivial bound for S(F; N, H) would naively fail, such as when F is a perfect 1-th power
and χ is order 1, or when F can be made to depend on fewer than n variables.
Condition ((1, q)-admissible). Let q be a ﬁxed prime and 1 ≥1 a ﬁxed integer. We will say that a
polynomial f ∈Fq[x1, . . . , xn] is (1, q)-admissible if the following holds. Factorize f = g1h, where
g, h ∈Fq[x1, . . . , xn] and h is 1-th power-free over Fq. Then h has the property that it cannot be made
independent of (at least) one variable after a linear transformation, i.e., there exists no linear change of
variables A ∈GLn(Fq) such that h(x A) ∈Fq[x2, . . . , xn].
See Section 3 for further details on this condition, and a precise deﬁnition of being 1-th power-free.
If 1 ≥2 is a ﬁxed integer, any form F ∈Z[x1, . . . , xn] such that F = G1H with G, H ∈Z[x1, . . . , xn]
where H is 1-th power-free and nondegenerate with respect to changes of variables in GLn(Z), has
the property that its reduction modulo q is (1, q)-admissible for all but ﬁnitely many primes q; see
Lemma 3.4. For any D, the form x D
1 + · · · + x D
n is an example of such a form. Moreover, such forms
are generic among all forms in Z[x1, . . . , xn] of degree at most D, since those that violate the conditions
depend on fewer parameters.
Our main result is as follows:
Theorem 1.1. Let χ be a nonprincipal multiplicative Dirichlet character of order 1 modulo a prime q.
Let n ≥2 be ﬁxed. For each r ≥1, deﬁne
2 = 2n,r =
j r −1
n−1
k
.
Let H = (H1, . . . , Hn) ∈Rn
≥1 have maximum element Hmax and minimum element Hmin, and assume
HmaxHmin < q1+1/(22). For every degree D form F ∈Z[x1, . . . , xn] such that its reduction modulo q is
(1, q)-admissible, then uniformly in N = (N1, . . . , Nn), for every integer r ≥1,
|S(F; N, H)| ≪∥H∥1−(1/2r)H−1/2r
min
q(n2+1)/4r2(log q)n+1,
(1-4)
in which the implied constant depends only on D, 1, n,r and is otherwise independent of F.
Burgess bounds for short character sums evaluated at forms
1913
If one carries through our method of proof in the case n = 1, we may deﬁne 2 = 21,r = r for all
r ≥1 and recover the Burgess bound (1-1) (up to the power of the logarithm). This result may also be
extended to apply to a rational function F = f1/f2 if it is appropriately regarded as f1 f 1−1
2
. Analogous
to the proof of the Pólya–Vinogradov inequality, Fourier-based methods can prove a nontrivial bound for
S(F; N, H) for suitable forms F when Hi ≫q1/2+ε (see Section A.3); thus the upper bound restriction
on Hi in the hypothesis of the theorem is compatible with our interest in the range Hi ≪q1/2+ε.
For purposes of comparison, we state a direct corollary of Theorem 1.1 in the case that all coordinates
of H are of equal size.
Corollary 1.2. Assume the hypotheses of Theorem 1.1. Suppose H =(H, H, . . . , H) with H <q1/2+1/(42).
For every degree D form F ∈Z[x1, . . . , xn] such that its reduction modulo q is (1, q)-admissible, then
uniformly in N = (N1, . . . , Nn), for every integer r ≥1,
|S(F; N, H)| ≪Hn−(n+1)/2rq(n2+1)/4r2(log q)n+1,
(1-5)
in which the implied constant depends only on D, 1, n,r and is otherwise independent of F.
Remark. The upper bound in Burgess’s original work is independent of the order of the character. In
our results, there is a possible dependence on the order 1. In our approach, this possible dependence
on 1 appears in the constant C′′ provided by Theorem 4.4, which we apply to count the number of tuples
(x(1), . . . , x(2r)) that could result in “large” complete character sum values. In turn, the constant C′′
provided by Theorem 4.4 can depend on 1 because it encodes the sum of the degrees of the irreducible
components of certain subschemes, that are determined by n,r, D and 1. See Section 4 and [Xu 2018,
Section 2.1] for details.
1B. The strength of Theorem 1.1: quantiﬁcations. In general, for a Burgess-style result such as (1-1),
which holds for a range of integers r, to assess its strength for H near the lower-bound threshold that
yields a nontrivial bound for |S(N, H)|, we must compute which value of r produces maximum savings.
For example, in Burgess’s original result, if H = q1/4+κ the bound (1-1) with parameter value r yields the
upper bound |S(N, H)| ≪Hq−δ where δ = (4κr −1)/(4r2). Computing the maximum of δ with respect
to r, we see that by choosing r to be the nearest integer to 1/(2κ) we may obtain the best value δ ≈κ2.
We perform an analogous optimization of our result, summarized in two corollaries.
Corollary 1.3. For each n ≥2 and r ≥1, Theorem 1.1 with the parameters n,r provides a nontrivial
upper bound |S(F; N, H)| = on,r,1,D(∥H∥) for all H = (H, . . . , H) with H = qβ with β in the range
1
2 −
2−1
22(n+1) < β ≤1
2 + 1
42,
(1-6)
in which 2 = 2n,r = ⌊(r −1)/(n −1)⌋. This range includes a nonempty interval of β < 1
2 as soon as
r ≥2n −1, so that 2 = 2n,r > 1. In particular, this range always requires β > βn with
βn := 1
2 −
1
2(n+1).
(1-7)
1914
Lillian B. Pierce and Junyan Xu
For H = qβn+κ for small κ, we obtain a nontrivial bound ∥H∥q−δn with savings approximately of size
δn ≈(n + 1)2
4(n −1)κ2
as κ →0.
Remark. In the approximate value of the savings δn stated above (and similarly in Corollary 1.4 below),
the symbol ≈is used to denote that certain approximations were used in the derivation, such as (i) letting
the value θ1 = ⌊(r −1)/(n −1)⌋be approximated by r/(n −1), which is reasonable, for ﬁxed n, for the
very large values of r = r(κ) that are chosen when κ →0; and (ii) considering the limiting case κ →0 in
order to isolate the main term in computations. More details are given in Section 7A.
The threshold βn deﬁned in (1-7) has appeared in n-dimensional Burgess bounds that were previously
proved in very special cases, such as [Burgess 1967b; 1968; Davenport and Lewis 1963] (see Section 1C2
for an overview, including the stronger results [Chang 2008; 2009; Bourgain and Chang 2010; Heath-
Brown 2016]).
In full generality, our main result Theorem 1.1 is in fact stronger than Corollary 1.3, as it can allow
one or more of the lengths Hi to be smaller than qβn, as long as other Hi are commensurably larger.
We cannot let Hi vary in a completely uncontrolled fashion, since our savings comes from the smallest
parameter Hmin; thus we assume that H is proportionate, in the sense that Hmin ≥∥H∥c0/n for some
constant 0 < c0 ≤1. The relation (1-9) below shows that if we take c0 smaller so that Hmin becomes a
decreasing proportion of ∥H∥, for our Burgess bound to be nontrivial the geometric mean ∥H∥1/n is
forced into an ever shorter range near q1/2.
Corollary 1.4. For each n ≥2 and r ≥1, Theorem 1.1 with the parameters n,r provides a nontrivial
upper bound |S(F; N, H)| = on,r,1,D(∥H∥) for all H = (H1, . . . , Hn) with HminHmax < q1+1/22 as
long as Hmin ≥∥H∥c0/n for some 0 < c0 ≤1 and ∥H∥1/n = qβ with β in the range
1
2 −
c02−1
22(n+c0) < β ≤1
2 + 1
42,
(1-8)
in which 2 = 2n,r = ⌊(r −1)/(n −1)⌋. This range includes a nonempty interval of β < 1
2 as soon as
r ≥(1/c0 + 1)(n −1) + 1, so that c02 > 1. In particular this range always requires ∥H∥1/n = qβ with
β > βn,c0 = 1
2 −
c0
2(n+c0) ≥1
2 −
1
2(n+1).
(1-9)
Alternatively, we can state that Theorem 1.1 obtains a nontrivial upper bound if
∥H∥Hmin ≫qn/2+κ
for some small κ. As κ →0 we obtain a nontrivial bound ∥H∥q−δn with
δn ≈(n + c0)2
4(n −1) κ2.
Burgess bounds for short character sums evaluated at forms
1915
1C. Overview of previous literature. To situate our results, we recall previous literature on Burgess
bounds and in particular for the sums S(F; N, H).
1C1. The classical Burgess bound. For any integer q ≥1, the Pólya–Vinogradov inequality states that
|S(N, H)| ≪q1/2 log q (see [Pólya 1918; Vinogradov 1918] or for a modern treatment [Iwaniec and
Kowalski 2004, §12.4]). This provides a nontrivial upper bound for |S(N, H)| as long as H ≫q1/2+ε
for some ε > 0. When H is shorter than this range, the sum is considered to be “short,” and obtaining an
o(H) bound is much more difﬁcult. Conjecturally, under the generalized Riemann hypothesis, a bound as
strong as |S(0, H)| ≪ε H1/2qε should hold for all ε > 0, thus leading to a nontrivial upper bound in any
range H ≫ε q3ε (see, e.g., [Iwaniec and Kowalski 2004, Equation (12.54)], or [Friedlander et al. 2013,
Equation (9.6)]; see also the more general Conjecture Cn in [Friedlander et al. 2013, §9]).
Burgess [1957; 1962; 1963; 1986] showed that for χ a primitive character to a prime modulus q, for
all integers r ≥1, the inequality (1-1) holds, with an implied constant uniform in N, yielding a nontrivial
bound for H ≫q1/4+κ, κ > 0. More generally, with log q replaced by qε for arbitrarily small ε, Burgess
proved that this bound also holds for cube-free moduli q for all r ≥1, and for any integer q, for r ≤3.
The q1/4+κ “threshold” of the Burgess bound remains essentially unimproved since its inception, despite
signiﬁcant interest, due to its applications.
As a consequence of (1-1), Burgess [1963] proved a landmark subconvexity bound

L
  1
2 + it, χ


 ≪t,ε q1/4−1/16+ε
for all ε > 0, with χ a nonprincipal Dirichlet character modulo q as above; there is a corresponding
hybrid subconvexity bound

L
  1
2 + it, χ


 ≪ε (|t|q)1/4−1/16+ε of Heath-Brown [1980]. This remains the
best bound known to hold for all Dirichlet L-functions. (Special cases of the modulus q in which a better
subconvexity bound is known include: smooth moduli [Graham and Ringrose 1990; Goldmakher 2010;
Chang 2014; Irving 2016]; prime-power moduli [Postnikov 1956; Barban et al. 1964; Gallagher 1972;
Mili´cevi´c 2016], or powerful moduli [Iwaniec 1974]. Most recently, Petrow and Young [2018] proved a
better Weyl-strength subconvex estimate of size q1/6 for all cube-free moduli q.1) There is great interest
in establishing bounds of at least the strength of a “Burgess exponent” for analogous bounds in higher
rank contexts. For example, in the GL(2) setting, the “Burgess bound” for an L-function of a Hecke cusp
form g twisted by a primitive Dirichlet character χ modulo q is

L
  1
2 + it, g ⊗χ


 ≪g,ε q1/2−1/8+ε for
all ε > 0 (as has been obtained in [Bykovskii 1996; Blomer and Harcos 2008]). Reaching the Burgess
exponent in new settings, or even re-proving such Burgess bounds is currently an important proving
ground for new methods (e.g., [Munshi 2018] via a GL(2) delta method and subsequently [Aggarwal
et al. 2018] via a trivial delta method).
In another direction, the Burgess bound establishes an upper bound for the least quadratic non-
residue n(p) modulo a prime p. Vinogradov conjectured that n(p) ≪ε pε for every ε > 0; Burgess’s
1After the writing of this paper, Petrow and Young [2019] posted a preprint proving a Weyl-strength subconvex estimate for
all Dirichlet L-functions, without a restriction on the modulus q. This breakthrough result also implies a small improvement on
the classical Burgess upper bound (1-1) for the cases r = 2, 3 but not for larger r.
1916
Lillian B. Pierce and Junyan Xu
bound (1-1) proves n(p) ≪ε p(4√e)−1+ε for any ε > 0, which held the record from [Burgess 1957] until
the quantiﬁcation in [Banks and Guo 2017]. In this vein, there are continued efforts toward the goal
of improving the inequality (1-1) directly, such as reducing the power of the logarithm (see [Iwaniec
and Kowalski 2004, Equation (12.58) and Remark p. 329; Kerr et al. 2019]), deducing improvements in
certain special cases from conjectural improvements on the Pólya–Vinogradov inequality [Fromm and
Goldmakher 2019], and making connections to the Elliott–Halberstam conjecture and “Type II sums” in
sieve methods [Tao 2015, Conjecture 1.5, Theorem 1.6, Remark 1.7].
1C2. Previous literature on special cases of S(F; N, H). In the n-dimensional setting of the sums
S(F; N, H), previous literature mainly focused on two special cases. Burgess [1967b; 1968] considered
the case in which
F(x) =
n
Y
i=1
Li(x)
(1-10)
is a product of n linear forms Li ∈Z[x1, . . . , xn] that are linearly independent over Fq, for q prime. In
this multilinear setting, he proved a nontrivial bound |S(F; N, H)| = O(∥H∥q−δ) for H = (H, . . . , H)
and a certain δ = δ(κ) > 0 as long as H = qβn+κ for some κ > 0, with βn as deﬁned in (1-7). Bourgain
and Chang [2010] incorporated ideas from additive combinatorics to improve this signiﬁcantly, proving a
nontrivial bound |S(F; N, H)| = O(∥H∥q−δ) for H = (H, . . . , H) and a certain δ = δ(κ) > 0 as long
as H = q1/4+κ for some κ > 0, thus obtaining an n-dimensional result as strong as the original Burgess
threshold in each dimension.
The second case in which signiﬁcant results are known is in dimension n = 2 when F is a binary
quadratic form. In this special case, the work of Burgess above, for bilinear sums in n = 2, combined with
results of Davenport and Lewis [1963] on analogues of the Burgess bound over Fq2, initially provided
a nontrivial upper bound for S(F, N, H) for q prime and Hi > q1/3+κ (that is Hi > qβ2+κ with β2 as
in (1-7)), where F is any binary quadratic form that is not a perfect square over Fq; that is for any
F(x1, x2) = x2
1 + ax1x2 + bx2
2 with a2̸ ≡4b (mod q). Chang [2009, Theorem 11] introduced ideas of
additive combinatorics to this setting, and improved this to a nontrivial upper bound for S(F, N, H) for
H1, H2 > q1/4+κ, i.e., a 2-dimensional result as strong as the original Burgess threshold in each dimension.
Most recently, Heath-Brown [2016, Theorem 3] proved that this latter result continues to hold for any
odd square-free modulus q such that (q, det(F)) = 1.
Remark. It remains an interesting open question to bound S(F; N, H), with all Hi as short as q1/4+κ
for κ > 0, in the general case of an arbitrary form F whose reduction modulo q is (1, q)-admissible.
1C3. Further related literature. We brieﬂy mention certain other results that are related to multivariate
sums similar to S(F; N, H), although not of exactly the type we consider in this paper. Davenport and
Lewis [1963] considered the case of χ a nonprincipal character of F∗
qn for q prime, and a linear form
F(x1, . . . , xn) = ω1x1 + · · · + ωnxn for ω1, . . . , ωn a ﬁxed basis of Fqn. They proved that S(F, N, H) =
O(∥H∥q−δ) for some δ = δ(κ) where Hi > qβn+κ for some κ > 0. As remarked in [Burgess 1968], for
Burgess bounds for short character sums evaluated at forms
1917
n = 2 this provides a corresponding upper bound for S(F; N, H) in the case that F is an irreducible
binary quadratic form x2
1 + ax1x2 + bx2
2 over Fq, in which case χ(F(x1, x2)) is a character (mod q)
of x1 + ωx2 ∈Q(ω), where ω = 1
2a + 1
2
√
a2 −4b. In the n-dimensional setting, if one assumes that
ω1, . . . , ωn is a certain special type of basis (such as a power basis), stronger results have also been
obtained; Burgess [1967a] and Karatsuba [1970] proved nontrivial upper bounds in the stronger range
Hi > q1/4+κ. Without such special assumptions, Chang [2008] improved on Davenport and Lewis (for
n ≥5) by proving a nontrivial bound as soon as ∥H∥> q2n/5+κ for some κ > 0, and furthermore in
dimension n = 2 Chang [2009, Theorem 5] proved that Hi ≫q1/4+κ sufﬁces for any κ > 0. See also
[Chang 2008] for certain results of Burgess-type for multiplicative character sums over sumsets.
Finally, we mention work on mixed character sums in multivariate settings, of the form
S(F, g; N, H) =
X
x∈(N,N+H]
e(g(x))χ(F(x)),
with a polynomial g ∈R[x1, . . . , xn]. In [Pierce 2016] the ﬁrst author proved nontrivial upper bounds
for such multivariate sums in the regime Hi ≫q1/4+κ, in the special case F(x) = x1 · · · xn (generalizing
[Heath-Brown and Pierce 2015] in dimension n = 1). This was later generalized by Kerr [2014] to
the case of F(x) multilinear as in (1-10). A second paper in this series will prove Burgess bounds for
S(F, g; N, H) for any form F whose reduction modulo q is (1, q)-admissible.
1D. Outline of the paper. We present in Section 2 a heuristic overview of the proof of Theorem 1.1,
which illustrates how the stratiﬁcation result of the second author [Xu 2018] plays a key role. In Section 3
we gather together the lemmas we need to motivate and utilize the condition of (1, q)-admissibility. In
Section 4 we give a convenient restatement and strengthening of the stratiﬁcation results of [Xu 2018];
we expect this version will be of independent interest in other applications. In Section 5 we begin the
n-dimensional Burgess argument, reaching the key new novel steps in Section 6, which carries out the
stratiﬁcation and a Menshov–Rademacher argument involving permuting variables. In Section 7 we
complete the Burgess argument and choose parameters optimally; subsequently we verify the corollaries.
In the Appendix we provide a comparison illustrating the utility of the stratiﬁcation, and a conditional
argument that assumes a stronger stratiﬁcation result, which shows that the threshold βn is stable under
such an improvement.
1E. Notation. We will use the notation x ∈(N, N + H] to denote the range of a sum over a box
(N, N + H] = Q
i(Ni, Ni + Hi], and will let ∥H∥= Q
i Hi for any tuple H. We will write aq to mean
(a1q, . . . , anq) and a/q to mean (a1/q, . . . , an/q). We will also use notations such as x ≤a to denote
xi ≤ai for i = 1, . . . , n and a (mod p) to mean we regard each ai (mod p). We deﬁne Hmax := maxi Hi
and Hmin := mini Hi. We will use the Vinogradov notation A ≪B to denote that there exists a constant C
such that |A| ≪C B, and A ≪κ B to denote that C may depend on the parameter κ. In the following
work, all implied constants may depend on n,r, D, 1 := ord χ and possibly an arbitrarily small ε > 0
without further speciﬁcation, but will never depend on N, H, q.
1918
Lillian B. Pierce and Junyan Xu
