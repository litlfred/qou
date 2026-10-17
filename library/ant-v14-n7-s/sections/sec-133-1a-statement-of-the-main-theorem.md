---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory"
section_id: sec-133-1a-statement-of-the-main-theorem
section_title: "1A. Statement of the main theorem"
section_number: null
pages: 246-247
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
toc_source: outline
---
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
