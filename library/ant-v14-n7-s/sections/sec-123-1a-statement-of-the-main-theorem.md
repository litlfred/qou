---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-123-1a-statement-of-the-main-theorem
section_title: "1A. Statement of the main theorem"
section_number: null
pages: 246-249
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
must satisfy in order to be “admissible” for our main result. We only need to rule out those forms F for
which a nontrivial bound for S(F; N, H) would naively fail, such as when F is a perfect1-th power
andχ is order1, or when F can be made to depend on fewer than n variables.
Condition ((1, q)-admissible). Let q be a ﬁxed prime and 1≥ 1 a ﬁxed integer. We will say that a
polynomial f∈ Fq[x1,..., xn] is(1, q)-admissible if the following holds. Factorize f= g1h, where
g, h∈ Fq[x1,..., xn] and h is1-th power-free over Fq. Then h has the property that it cannot be made
independent of (at least) one variable after a linear transformation, i.e., there exists no linear change of
variables A∈ GLn(Fq) such that h(x A)∈ Fq[x2,..., xn].
See Section 3 for further details on this condition, and a precise deﬁnition of being 1-th power-free.
If1≥ 2 is a ﬁxed integer, any form F∈ Z[x1,..., xn] such that F= G1H with G, H∈ Z[x1,..., xn]
where H is1-th power-free and nondegenerate with respect to changes of variables in GLn(Z), has
the property that its reduction modulo q is(1, q)-admissible for all but ﬁnitely many primes q; see
Lemma 3.4. For any D, the form x D
1+···+ x D
n is an example of such a form. Moreover, such forms
are generic among all forms in Z[x1,..., xn] of degree at most D, since those that violate the conditions
depend on fewer parameters.
Our main result is as follows:
Theorem 1.1. Letχ be a nonprincipal multiplicative Dirichlet character of order1 modulo a prime q.
Let n≥ 2 be ﬁxed. For each r≥ 1, deﬁne
2=2n,r=
⌊ r−1
n−1
⌋
.
Let H=(H1,..., Hn)∈ Rn
≥1 have maximum element Hmax and minimum element Hmin, and assume
HmaxHmin< q1+1/(22). For every degree D form F∈ Z[x1,..., xn] such that its reduction modulo q is
(1, q)-admissible, then uniformly in N=(N1,..., Nn), for every integer r≥ 1,
|S(F; N, H)|≪‖ H‖1−(1/2r)H−1/2r
min q(n2+1)/4r2(log q)n+1, (1-4)
in which the implied constant depends only on D,1, n, r and is otherwise independent of F.
Burgess bounds for short character sums evaluated at forms 1913
If one carries through our method of proof in the case n= 1, we may deﬁne 2=21,r= r for all
r≥ 1 and recover the Burgess bound (1-1) (up to the power of the logarithm). This result may also be
extended to apply to a rational function F= f1/f2 if it is appropriately regarded as f1 f1−1
2 . Analogous
to the proof of the Pólya–Vinogradov inequality, Fourier-based methods can prove a nontrivial bound for
S(F; N, H) for suitable forms F when Hi≫ q1/2+ε (see Section A.3); thus the upper bound restriction
on Hi in the hypothesis of the theorem is compatible with our interest in the range Hi≪ q1/2+ε.
For purposes of comparison, we state a direct corollary of Theorem 1.1 in the case that all coordinates
of H are of equal size.
Corollary 1.2. Assume the hypotheses of Theorem 1.1. SupposeH=(H, H,..., H) with H<q1/2+1/(42).
For every degreeD form F∈ Z[x1,..., xn] such that its reduction modulo q is(1, q)-admissible, then
uniformly in N=(N1,..., Nn), for every integer r≥ 1,
|S(F; N, H)|≪ H n−(n+1)/2rq(n2+1)/4r2(log q)n+1, (1-5)
in which the implied constant depends only on D,1, n, r and is otherwise independent of F.
Remark. The upper bound in Burgess’s original work is independent of the order of the character. In
our results, there is a possible dependence on the order 1. In our approach, this possible dependence
on1 appears in the constant C′′ provided by Theorem 4.4, which we apply to count the number of tuples
(x(1),..., x(2r)) that could result in “large” complete character sum values. In turn, the constant C′′
provided by Theorem 4.4 can depend on 1 because it encodes the sum of the degrees of the irreducible
components of certain subschemes, that are determined by n, r, D and1. See Section 4 and [Xu 2018,
Section 2.1] for details.
1B. The strength of Theorem 1.1: quantiﬁcations. In general, for a Burgess-style result such as (1 -1),
which holds for a range of integers r, to assess its strength for H near the lower-bound threshold that
yields a nontrivial bound for|S(N, H)|, we must compute which value of r produces maximum savings.
For example, in Burgess’s original result, ifH= q1/4+κ the bound (1-1) with parameter value r yields the
upper bound|S(N, H)|≪ Hq−δ whereδ=(4κr− 1)/(4r 2). Computing the maximum of δ with respect
to r, we see that by choosing r to be the nearest integer to 1/(2κ) we may obtain the best value δ≈κ2.
We perform an analogous optimization of our result, summarized in two corollaries.
Corollary 1.3. For each n≥ 2 and r≥ 1, Theorem 1.1 with the parameters n, r provides a nontrivial
upper bound|S(F; N, H)|= on,r,1, D(‖H‖) for all H=(H,..., H) with H= qβ withβ in the range
1
2− 2−1
22(n+1)<β≤ 1
2+ 1
42, (1-6)
in which2=2n,r=⌊(r− 1)/(n− 1)⌋. This range includes a nonempty interval of β< 1
2 as soon as
r≥ 2n− 1, so that2=2n,r> 1. In particular, this range always requiresβ>β n with
βn:= 1
2− 1
2(n+1). (1-7)
1914 Lillian B. Pierce and Junyan Xu
For H= qβn+κ for smallκ, we obtain a nontrivial bound‖H‖q−δn with savings approximately of size
δn≈ (n+ 1)2
4(n− 1)κ2
asκ→ 0.
Remark. In the approximate value of the savings δn stated above (and similarly in Corollary 1.4 below),
the symbol≈ is used to denote that certain approximations were used in the derivation, such as (i) letting
the valueθ1=⌊(r− 1)/(n− 1)⌋ be approximated by r/(n− 1), which is reasonable, for ﬁxed n, for the
very large values of r= r(κ) that are chosen whenκ→ 0; and (ii) considering the limiting case κ→ 0 in
order to isolate the main term in computations. More details are given in Section 7A.
The thresholdβn deﬁned in (1-7) has appeared in n-dimensional Burgess bounds that were previously
proved in very special cases, such as [Burgess 1967b; 1968; Davenport and Lewis 1963] (see Section 1C2
for an overview, including the stronger results [Chang 2008; 2009; Bourgain and Chang 2010; Heath-
Brown 2016]).
In full generality, our main result Theorem 1.1 is in fact stronger than Corollary 1.3, as it can allow
one or more of the lengths Hi to be smaller than qβn, as long as other Hi are commensurably larger.
We cannot let Hi vary in a completely uncontrolled fashion, since our savings comes from the smallest
parameter Hmin; thus we assume that H is proportionate, in the sense that Hmin≥‖ H‖c0/n for some
constant 0< c0≤ 1. The relation (1-9) below shows that if we take c0 smaller so that Hmin becomes a
decreasing proportion of‖H‖, for our Burgess bound to be nontrivial the geometric mean ‖H‖1/n is
forced into an ever shorter range near q1/2.
Corollary 1.4. For each n≥ 2 and r≥ 1, Theorem 1.1 with the parameters n, r provides a nontrivial
upper bound|S(F; N, H)|= on,r,1, D(‖H‖) for all H=(H1,..., Hn) with HminHmax< q1+1/22 as
long as Hmin≥‖ H‖c0/n for some 0< c0≤ 1 and‖H‖1/n= qβ withβ in the range
1
2− c02−1
22(n+c0)<β≤ 1
2+ 1
42, (1-8)
in which2=2n,r=⌊(r− 1)/(n− 1)⌋. This range includes a nonempty interval of β< 1
2 as soon as
r≥(1/c0+ 1)(n− 1)+ 1, so that c02> 1. In particular this range always requires‖H‖1/n= qβ with
β>β n,c0= 1
2− c0
2(n+c0)≥ 1
2− 1
2(n+1). (1-9)
Alternatively, we can state that Theorem 1.1 obtains a nontrivial upper bound if
‖H‖Hmin≫ qn/2+κ
for some smallκ. Asκ→ 0 we obtain a nontrivial bound‖H‖q−δn with
δn≈(n+ c0)2
4(n− 1)κ2.
Burgess bounds for short character sums evaluated at forms 1915
