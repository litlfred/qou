---
doc_id: maximal-hoermander-q-var-revised-v03
doc_title: "q-variational Hörmander functional calculus and Schrödinger and wave maximal estimates"
section_id: sec-009-examples-and-concluding-remarks
section_title: "Examples and concluding remarks"
section_number: null
pages: 35-36
source_pdf: Maximal-Hoermander-q-Var-revised-v03.pdf
source_sha256: 135332c04a1b3bb8
toc_source: outline
doc_brief: "q-variational Hörmander functional calculus and Schrödinger and wave maximal estimates — 12 sections: Front matter; Introduction; R-boundedness"
---
Examples and concluding remarks
In this section, we shortly discuss examples of 0-sectorial operators A and of UMD lattices Y ,
to illustrate our main results from Sections 3 and 5. We will then end with some concluding
remarks and open questions related to the present article.
Hörmander calculus for (generalised) Gaussian estimates
For the ﬁrst result below,
we refer to [DK, Deﬁnitions 4.2 and 4.3] for the deﬁnition of a semigroup with Gaussian and
generalised Gaussian estimates. We recall the main theorem on Hörmander functional calculus
on Lp(Y ) for Gaussian estimates from [DKK].
Deﬁnition 7.1 Let p ∈(1, ∞), pY ∈(1, 2] and qY ∈[2, ∞). We put
(7.1)
α(p, pY , qY ) = max
1
p, 1
pY
, 1
2

−min
1
p, 1
qY
, 1
2

∈(0, 1).
Informally spoken, this is the length of the segment, which is the convex hull of the points
1
p,
1
pY ,
1
qY and 1
2 sitting on the real line.
Theorem 7.2 [DKK, Theorem 4.10] Let (Ω, dist, µ) be a space of homogeneous type with a
dimension d. Let A be a self-adjoint operator on L2(Ω) generating the semigroup (Tt)t⩾0. Let
p0 ∈[1, 2) and m ∈[2, ∞). Assume that (Tt)t⩾0 satisﬁes Gaussian (resp. generalised Gaussian)
estimates with parameter m (resp. p0, m). Let Y be a UMD lattice which is pY -convex and qY -
concave for some pY ∈(1, 2] (resp. pY ∈(p0, 2]) and qY ∈[2, ∞) (resp. qY ∈[2, p′
0)). Assume
that the convexiﬁcations Y pY and (Y ′)q′
Y are also UMD lattices. For example, if Y = Ls(Ω′)
for some s ∈(1, ∞), then any pY ∈(p0, s) and any qY ∈(s, p′
0) are admissible.
Finally,
assume that A has a bounded H∞(Σω) calculus on Lp(Ω, Y ) for some ﬁxed p ∈(1, ∞) (resp.
p ∈(p0, p′
0)) and ω ∈(0, π).
Then A has a Hörmander Hβ
2 calculus on Lp(Ω, Y ) with
β > α(p, pY , qY ) · d + 1
2
and α from (7.1).
Theorem 7.2 applies to a wide range of diﬀerential operators in diﬀerent contexts, including
those listed in the Introduction Section 1. For a discussion of many further examples where
Gaussian estimates are satisﬁed, we refer to [DuOS, Section 7], see also [DKK, Subsection 5.1]
and [DK, Subsection 4.1].
Note also that our semigroups do not need to be self-adjoint on L2(Ω) (if ever p = 2). Indeed,
suppose that the semigroup (Tt)t⩾0 consists of self-adjoint contractions on L2(Ω, µ), where Ωis
a space of homogeneous type, with dimension d ∈N. Then according to [DSY, Theorem 3.2],
there exists some r0 ∈[1, 2) such that for any p ∈(r0, ∞), any w ∈A p
r0 (Muckenhoupt weight
class [DSY, p. 1109]) and s > d+1
2 , the generator A of (Tt)t⩾0 has a Hörmander calculus on
Lp(Ω, wdµ). Picking p = 2, the semigroup (Tt)t⩾0 is thus uniformly bounded on L2(Ω, wdµ),
but if w ∈A 2
r0 is not constant, the semigroup (Tt)t⩾0 and the generator A are not self-adjoint
on this weighted L2 space.
34
Examples of UMD lattices
Apart from Lq(Ω′) spaces for 1 < q < ∞which are the major
examples of UMD lattices, one can also consider their intersections and sums when seen as
subspaces of the common superspace of (equivalence classes of) measurable functions over Ω′.
Lemma 7.3 Let 1 < q1, q2 < ∞. Let Ω′ be a σ-ﬁnite measure space.
1. Then Y = Lq1(Ω′) ∩Lq2(Ω′) equipped with the norm ∥f∥Y = max{∥f∥q1 , ∥f∥q2} and
obvious partial order is a UMD lattice.
2. Then Y = Lq1(Ω′)+Lq2(Ω′) equipped with the norm ∥f∥Y = inf{∥g∥q1 +∥h∥q2 : f = g+h}
and obvious partial order is also a UMD lattice.
For a simple proof, we refer to [DK, Lemma 4.9].
Concluding remarks
Already for classical (i.e. without q-variation or supremum in t > 0)
Hörmander multiplier theorems, a nice description of the exact norm ∥m(A)∥Lp→Lp in terms
of a function norm ∥m∥of the spectral multiplier is not known today. This problem is equally
present for our q-variational and maximal spectral multiplier estimates in this article and only a
step by step progression of suﬃcient conditions in the form ∥t 7→m(tA)(·)∥Lp→Lp(V q) ≲∥m∥...
seems to be manageable. In this direction, it would be interesting to know whether in the
contexts of Theorem 3.3 2. (q-variation) and of Theorem 5.1 2. (maximal estimate with time-
dependent ft) of semigroup generators, one can relax the summation condition to
X
n∈Z
∥m(2n·)ϕ0∥W c
2 (R)
1 + |n|
< ∞
as for maximal estimates in the euclidean case [CGHS], or with an additional factor log(|n|+2)
as in [Choi]. As another possible relaxation, one can ask the question, whether
X
n∈Z
∥m(2n·)ϕ0∥2
W c
q (R) < ∞
is suﬃcient for our estimates, which is known to be true for the classical maximal estimate of
the euclidean Laplacian [CGHS, (1.3)]. For this, it would be interesting to know whether there
are other approaches to q-variational and time dependent maximal estimates than ours, in case
of the euclidean Laplacian or sub-Laplacians on Lie groups. Also q-variational estimates for
spectral multipliers that do not decay at ∞are not well understood. Already the scalar case
Y = C would be interesting.
In the context of Section 4, it would be interesting to get information on the norm Cp,q,d,Y in
Theorem 4.2 and on Cp,q,Y in Proposition 4.4, depending on p, q(, d) and Y . Also one could try
to ﬁnd a proof of Proposition 4.4 using Hörmander functional calculus that also covers small,
so ﬁnally all, dimensions.
