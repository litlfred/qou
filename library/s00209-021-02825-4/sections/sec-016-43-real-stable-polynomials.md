---
doc_id: s00209-021-02825-4
doc_title: "A representation theoretic explanation of the Borcea–Brändén characterization"
section_id: sec-016-43-real-stable-polynomials
section_title: "Real stable polynomials"
section_number: 4.3
pages: 15-16
source_pdf: s00209-021-02825-4.pdf
source_sha256: 85ca5ec21f42a988
toc_source: outline
doc_brief: "A representation theoretic explanation of the Borcea–Brändén characterization — In 2009, Borcea and Brändén characterized all linear operators on multivariate polynomials which preserve the property"
---
We now give a number of classical real stability results, along with a few results from [1]
and [2]. Additionally, we state these results for homogeneous polynomials in VR(λ), taking
roots at inﬁnity into account. The results of this section will come in to play mainly in Sect. 7,
where we discuss real linear operators and operators preserving interval- and ray-rootedness.
The ﬁrst result we will need for our considerations of VR(λ) is a version of the Hermite–
Biehler theorem, often called the Hermite–Kakeya–Obreschkoff theorem. We state here
without proof the multivariate version essentially used in Theorem 1.9 of [1] (see also §2.4
of [16]). First we need a deﬁnition.
Deﬁnition 4.8 We say that p, q ∈VR(λ) are in proper position, denoted p ≪q, if q + ip is
weakly Hm
+-stable (equivalently, if p + iq is weakly Hm
−-stable).
Proposition 4.9 (Multivariate Hermite–Biehler) For p, q ∈VR(λ), ap + bq is weakly real
stable for all a, b ∈R if and only if either p ≪q or q ≪p.
This result will be crucial to our consideration of real polynomials and real stability (as it
was in [1]). Its main use for us in this direction is made explicit in the following.
Lemma 4.10 Fix λ ∈Nm
0 , α ∈Nl
0, and a linear operator T : V (λ) →V (α) which restricts to
a real linear operator from VR(λ) to VR(α). If T preserves weak real stability and p ∈V (λ)
is stable, then T (p) is either Hl
+-stable, Hl
−-stable, or identically zero.
Proof By the Hermite–Biehler theorem, there exist q,r ∈VR(λ) such that p = q + ir and
aq + br is real stable or zero for all a, b ∈R. So, aT (q) + bT (r) is real stable or zero for all
a, b ∈R. By Hermite-Biehler again, T (p) = T (q) + iT (r) is either Hl
+-stable, Hl
−-stable,
or identically zero.
⊓⊔
The next two results are from [1], the ﬁrst of which gives an equivalent characterization for
a polynomial to be a scalar multiple of a real stable polynomial. This result will be speciﬁcally
used in Sect. 7 to generalize complex operator theoretic stability results to the real stability
case.
Lemma 4.11 [1, Proposition 4.1]Let p ∈VC(λ)be both Hm
+-stable and Hm
−-stable. Then, p is
a (complex) scalar multiple of a real stable polynomial. In particular, if nonzero q,r ∈VR(λ)
are such that q ≪r and r ≪q, then r is a (real) scalar multiple of q.
The next result provides the degeneracy cases in the Borcea–Brändén characterizations
(recall the dimension restrictions of Theorems 1.1 and 1.2). We will use this result to explicate
the link between our operator characterization and the Borcea–Brändén characterization (see
Lemmas 6.11 and 7.3).
Lemma 4.12 [1, Lemma 3.2] Let W ⊆VK(λ) be a K-vector subspace (for K = C or K = R)
consisting only of weakly stable (resp. weakly real stable) polynomials. We have:
1374 J. Leake

(a) IfK = C, then dim(W) < 1.
(b) If[K=R, then dim(W) < 2.

By applying appropriate Mébius transformations, note that (a) of the above lemma
can be generalized to (C; x --- x Cj)-stable polynomials for any open circular regions
Clee Cn € CPI.

We now state the last result of this section, which refines the Hermite-Biehler theorem
for top-degree monic polynomials in Vg(n). This refinement comes through the notion of
interlacing polynomials and is much closer to the original statement of the classical Hermite-
Biehler theorem (e.g., see Theorem 6.3.4 in [15]).

Lemma 4.13 For top-degree monic p,q € Vr(n), p < q if and only if the roots of p and q
(denoted in increasing order by (ax : 1) and (fx : 1), respectively) interlace on the real line
in the following way:

a < Bi Sa < By S++ SO < By

Further, if these equivalent conditions hold, then < gives a total order on the top-degree
monic elements of the span of p and q in Vp(n). This order is equivalently defined via the
order of the kth largest roots, for any k € [n] such that a, # Bx.

Proof The fact that p < q is equivalent to interlacing roots is the classical univariate Hermite-
Biehler theorem. That q has larger roots than p can be obtained by the fact that the (n — 1)st
derivative of g + ip must be 71,-stable. Since both polynomials are top-degree monic, this
(n — 1)st derivative will be a complex linear combination of two linear terms. This complex
linear combination is given as follows, where s, and s, denote the respective sums of the
roots of g and p:

an" (q(x, y) + ip(x, y)) = (nlx —(n— 1)! sgy) Fi! x — (n= D!- spy)
=masa(x— tie )
ma+o(s nd ai?

sq tisp

nddiy © H_. We further compute:

Since this polynomial is #1,-stable, it must be that

a ~ Sg ti8p — (Sq Fisp\L—i) _ Sq + Sp +i(Sp — Sq)
~~ n+i) 2n 7 2n

Therefore s, > s,, which is the same as saying that the sum of the roots of q is larger than
that of p. Since we already know that the roots of g and p interlace, this implies that g has
larger roots than p.

As for the total ordering property, let r and s be two polynomials in the real span of p
and q. Any real linear combination of these polynomials is then a real linear combination of
p and q (and hence is real-rooted), and Hermite—Biehler implies either r < s ors <r. By
the above interlacing condition, it is straightforward to see that this total order is given by
looking at the order of the kth roots, for any k € [n]. Oo
