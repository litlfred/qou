---
doc_id: arxiv-1706.06168v3
doc_title: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization"
section_id: sec-010-43-real-stable-polynomials
section_title: "Real Stable Polynomials"
section_number: 4.3
pages: 13-15
source_pdf: 1706.06168v3.pdf
source_sha256: ab3383a95f369922
---
We now give a number of classical real stability results, along with a fe w results from [ BB09a] and [ BB09b].
Additionally, we state these results for homogeneous polynomials in VR(λ), taking roots at inﬁnity into
account. The results of this section will come in to play mainly in §7, where we discuss real linear operators
and operators preserving interval- and ray-rootedness.
The ﬁrst result we will need for our considerations of VR(λ) is a version of the Hermite-Biehler theorem,
often called the Hermite-Kakeya-Obreschkoﬀ theorem. We state here without proof the multivariate version
essentially used in Theorem 1.9 of [ BB09a] (see also §2.4 of [ Wag11]). First we need a deﬁnition.
Deﬁnition 4.8. We say thatp,q ∈VR(λ) are in proper position, denoted p ≪q, if q +ip is weakly Hm
+ -stable
(equivalently, ifp +iq is weakly Hm
− -stable).
Proposition 4.9 (Multivariate Hermite-Biehler) . For p,q ∈ VR(λ), ap +bq is weakly real stable for all
a,b ∈ R if and only if either p ≪q or q ≪p.
This result will be crucial to our consideration of real polynomials and real stability (as it was in [ BB09a]).
Its main use for us in this direction is made explicit in the following.
Lemma 4.10. Fix λ ∈ Nm
0 , α ∈ Nl
0, and a linear operator T :V (λ) →V (α) which restricts to a real linear
operator from VR(λ) to VR(α). If T preserves weak real stability and p ∈V (λ) is stable, then T (p) is either
Hl
+-stable, Hl
−-stable, or identically zero.
Proof. By the Hermite-Biehler theorem, there exist q,r ∈ VR(λ) such that p = q +ir and aq +br is real
stable or zero for all a,b ∈ R. So, aT (q) +bT (r) is real stable or zero for all a,b ∈ R. By Hermite-Biehler
again, T (p) = T (q) +iT (r) is either Hl
+-stable, Hl
−-stable, or identically zero.
The next two results are from [ BB09a], the ﬁrst of which gives an equivalent characterization for a
polynomial to be a scalar multiple of a real stable polynomial. This result will be speciﬁcally used in §7 to
generalize complex operator theoretic stability results to the real stability case.
Lemma 4.11 ([BB09a], Proposition 4.1) . Let p ∈ VC(λ) be both Hm
+ -stable and Hm
− -stable. Then, p is a
(complex) scalar multiple of a real stable polynomial. In pa rticular, if nonzero q,r ∈ VR(λ) are such that
q ≪r and r ≪q, then r is a (real) scalar multiple of q.
The next result provides the degeneracy cases in the Borcea-Br¨ and´ en characterizations (recall the dimen-
sion restrictions of Theorems 1.1 and 1.2). We will use this result to explicate the link between our operator
characterization and the Borcea-Br¨ and´ en characterization (see Lemmas 6.11 and 7.3).
Lemma 4.12 ([BB09a], Lemma 3.2) . Let W ⊆ VK(λ) be a K-vector subspace (for K = C or K = R)
consisting only of weakly stable (resp. weakly real stable) polynomials. We have:
(a) If K = C, then dim(W ) ≤ 1.
(b) If K = R, then dim(W ) ≤ 2.
By applying appropriate M¨ obius transformations, note that ( a) of the above lemma can be generalized
to (C1 × · · · ×Cm)-stable polynomials for any open circular regions C1,...,C m ⊆ CP1.
We now state the last result of this section, which reﬁnes the Hermit e-Biehler theorem for top-degree
monic polynomials in VR(n). This reﬁnement comes through the notion of interlacing polynomials and is
much closer to the original statement of the classical Hermite-Bieh ler theorem (e.g., see Theorem 6.3.4 in
[RS02]).
13
Lemma 4.13. For top-degree monic p,q ∈ VR(n), p ≪ q if and only if the roots of p and q (denoted in
increasing order by (αk : 1) and (βk : 1), respectively) interlace on the real line in the following w ay:
α1 ≤β1 ≤α2 ≤β2 ≤ · · · ≤ αn ≤βn
Further, if these equivalent conditions hold, then ≪ gives a total order on the top-degree monic elements of
the span of p and q in VR(n). This order is equivalently deﬁned via the order of the kth largest roots, for any
k ∈ [n] such that αk ⁄=βk.
Proof. The fact that p ≪ q is equivalent to interlacing roots is the classical univariate Hermite-B iehler
theorem. That q has larger roots than p can be obtained by the fact that the ( n − 1)st derivative of q +ip
must be H+-stable. Since both polynomials are top-degree monic, this ( n − 1)st derivative will be a complex
linear combination of two linear terms. This complex linear combination is given as follows, where sq and
sp denote the respective sums of the roots of q and p:
∂n−1
x
(
q(x,y ) +ip(x,y )
)
= (n! ·x − (n − 1)! ·sqy) +i(n! ·x − (n − 1)! ·spy) = n!(1 +i)
(
x − sq +isp
n(1 +i)y
)
Since this polynomial is H+-stable, it must be that sq+isp
n(1+i) ∈ H−. We further compute:
H− ∋ sq +isp
n(1 +i) = (sq +isp)(1 −i)
2n = sq +sp +i(sp −sq)
2n
Therefore sq ≥sp, which is the same as saying that the sum of the roots of q is larger than that of p. Since
we already know that the roots of q and p interlace, this implies that q has larger roots than p.
As for the total ordering property, let r and s be two polynomials in the real span of p and q. Any real
linear combination of these polynomials is then a real linear combination ofp andq (and hence is real-rooted),
and Hermite-Biehler implies either r ≪s or s ≪r. By the above interlacing condition, it is straightforward
to see that this total order is given by looking at the order of the kth roots, for any k ∈ [n].
5 Grace’s Theorem
We now prove the multivariate homogeneous Grace’s theorem for so me speciﬁc projectively convex regions
and then derive a few important corollaries. These corollaries will be a lmost immediate once Grace’s theorem
has been proven, and yet will quickly yield stronger results regardin g linear operators in the next section.
In the usual proof of the classical univariate Grace’s theorem, re ference to linear factors of f ∈ Cn[x] is
necessary. This makes generalization to Cλ[x1,...,x m] diﬃcult, as multivariate polynomials do not necessar-
ily have any linear factors. In our new proof, we are able avoid refer ence to linear terms by using particular
features of the D map. This means that our proof method works for any λ.
Theorem 5.1. Fix λ ∈ Nm
0 and p,q ∈ V (λ). Also, denote C := H+ ∪ R+ and ~C := H− ∪ R−, where the
closures are considered to be in CP1. If p is Cm-stable and q is ~Cm-stable, then Dλ(p ⊗q) ⁄= 0.
Proof. We prove the theorem by induction on degree. For λ ≡ 0, the result is obvious. For |λ| ≥ 1, we can
assume WLOG that λ1 ≥ 1 by permuting the variables. Deﬁne δ1 := (1, 0, 0,..., 0) ∈ Nm
0 .
SinceC and ~C are projectively convex, Corollary 4.7 implies (a∂x1 +b∂y1)p isCm-stable for all (a :b) ∈C
and (c∂x1 +d∂y1)q is ~Cm-stable for all (c :d) ∈ ~C. To obtain a contradiction, we assume Dλ(p ⊗q) = 0. For
α ∈ H + ∪ R+ ⊂C (equivalently, −α ∈ H − ∪ R− ⊂ ~C), this gives:
Dλ−δ1
(
(α∂x1 +∂y1)p ⊗ (α∂x1 −∂y1)q
)
=α2Dλ−δ1 (∂x1p ⊗∂x1q) −Dλ−δ1 (∂y1p ⊗∂y1q) −αDλ(p ⊗q)
=α2Dλ−δ1 (∂x1p ⊗∂x1q) −Dλ−δ1 (∂y1p ⊗∂y1q)
14
By induction and the stability properties discussed above, we have Dλ−δ1 (∂x1p ⊗∂x1q) ⁄= 0, Dλ−δ1 (∂y1p ⊗
∂y1q) ⁄= 0, and Dλ−δ1
(
(α∂x1 +∂y1)p ⊗ (α∂x1 −∂y1)q
)
⁄= 0. This implies:
α2Dλ−δ1 (∂x1p ⊗∂x1q) −Dλ−δ1 (∂y1p ⊗∂y1q) ⁄= 0 =⇒α2 ⁄= Dλ−δ1 (∂y1p ⊗∂y1q)
Dλ−δ1 (∂x1p ⊗∂x1q) ∈ C \ {0}
However, we can pick α ∈ H + ∪ R+ such that α2 is any value of C \ { 0} we want, including that of
Dλ − δ 1 (∂y1 p⊗∂y1 q)
Dλ − δ 1 (∂x1 p⊗∂x1 q) . This contradiction gives the result.
