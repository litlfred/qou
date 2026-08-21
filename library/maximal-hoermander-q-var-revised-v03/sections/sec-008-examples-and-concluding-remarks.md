---
doc_id: maximal-hoermander-q-var-revised-v03
doc_title: "q-variational Hormander functional calculus and Schrodinger and wave maximal estimates"
section_id: sec-008-examples-and-concluding-remarks
section_title: "Examples and concluding remarks"
section_number: null
pages: 35-36
source_pdf: Maximal-Hoermander-q-Var-revised-v03.pdf
source_sha256: 135332c04a1b3bb8
doc_brief: "q-variational Hormander functional calculus and Schrodinger and wave maximal estimates — 10 sections: Introduction; R-boundedness; Preliminaries"
---
In this section, we shortly discuss examples of0-sectorial operatorsA and of UMD latticesY,
to illustrate our main results from Sections 3 and 5. We will then end with some concluding
remarks and open questions related to the present article.
Hörmander calculus for (generalised) Gaussian estimates For the ﬁrst result below,
we refer to [DK, Deﬁnitions 4.2 and 4.3] for the deﬁnition of a semigroup with Gaussian and
generalised Gaussian estimates. We recall the main theorem on Hörmander functional calculus
on Lp(Y ) for Gaussian estimates from [DKK].
Deﬁnition 7.1Letp∈(1,∞), pY ∈(1, 2] and qY ∈[2,∞).We put
(7.1) α(p,pY,qY ) = max
(1
p, 1
pY
, 1
2
{
−min
(1
p, 1
qY
, 1
2
{
∈(0, 1).
Informally spoken, this is the length of the segment, which is the convex hull of the points
1
p, 1
pY
, 1
qY
and 1
2 sitting on the real line.
Theorem 7.2 [DKK, Theorem 4.10] Let (Ω, dist,µ) be a space of homogeneous type with a
dimension d. LetA be a self-adjoint operator onL2(Ω) generating the semigroup(Tt)t>0. Let
p0∈[1, 2) andm∈[2,∞). Assume that(Tt)t>0 satisﬁes Gaussian (resp. generalised Gaussian)
estimates with parameterm (resp. p0,m). LetY be a UMD lattice which ispY-convex andqY-
concave for somepY ∈(1, 2] (resp. pY ∈(p0, 2]) andqY ∈[2,∞) (resp. qY ∈[2,p′
0)). Assume
that the convexiﬁcationsYpY and (Y′)q′
Y are also UMD lattices. For example, ifY = Ls(Ω′)
for some s ∈(1,∞), then any pY ∈(p0,s ) and any qY ∈(s,p′
0) are admissible. Finally,
assume thatA has a boundedH∞(Σω) calculus onLp(Ω,Y ) for some ﬁxedp∈(1,∞) (resp.
p∈(p0,p′
0)) andω∈(0,π).
Then A has a HörmanderHβ
2 calculus onLp(Ω,Y ) with
β >α(p,pY,qY )·d + 1
2
and αfrom (7.1).
Theorem 7.2 applies to a wide range of diﬀerential operators in diﬀerent contexts, including
those listed in the Introduction Section 1. For a discussion of many further examples where
Gaussian estimates are satisﬁed, we refer to [DuOS, Section 7], see also [DKK, Subsection 5.1]
and [DK, Subsection 4.1].
Note also that our semigroups do not need to be self-adjoint onL2(Ω) (if everp = 2). Indeed,
suppose that the semigroup(Tt)t>0 consists of self-adjoint contractions onL2(Ω,µ), whereΩ is
a space of homogeneous type, with dimensiond∈N. Then according to [DSY, Theorem 3.2],
there exists somer0∈[1, 2) such that for anyp∈(r0,∞), anyw∈A p
r0
(Muckenhoupt weight
class [DSY, p. 1109]) ands >d+1
2 , the generatorA of (Tt)t>0 has a Hörmander calculus on
Lp(Ω,wdµ). Picking p = 2, the semigroup (Tt)t>0 is thus uniformly bounded onL2(Ω,wdµ),
but ifw∈A 2
r0
is not constant, the semigroup(Tt)t>0 and the generatorA are not self-adjoint
on this weightedL2 space.
34
Examples of UMD lattices Apart fromLq(Ω′) spaces for 1<q <∞which are the major
examples of UMD lattices, one can also consider their intersections and sums when seen as
subspaces of the common superspace of (equivalence classes of) measurable functions overΩ′.
Lemma 7.3 Let 1<q 1,q 2 <∞. Let Ω′be aσ-ﬁnite measure space.
1. Then Y = Lq1(Ω′)\Lq2(Ω′) equipped with the norm‖f‖Y = max{‖f‖q1,‖f‖q2}and
obvious partial order is a UMD lattice.
2. ThenY =Lq1(Ω′)+Lq2(Ω′) equipped with the norm‖f‖Y = inf{‖g‖q1 +‖h‖q2 : f =g+h}
and obvious partial order is also a UMD lattice.
For a simple proof, we refer to [DK, Lemma 4.9].
Concluding remarks Already for classical (i.e. withoutq-variation or supremum int >0)
Hörmander multiplier theorems, a nice description of the exact norm‖m(A)‖Lp→Lp in terms
of a function norm‖m‖of the spectral multiplier is not known today. This problem is equally
present for ourq-variational and maximal spectral multiplier estimates in this article and only a
step by step progression of suﬃcient conditions in the form‖t↦→m(tA)(·)‖Lp→Lp(Vq) ≲‖m‖...
seems to be manageable. In this direction, it would be interesting to know whether in the
contexts of Theorem 3.3 2. (q-variation) and of Theorem 5.1 2. (maximal estimate with time-
dependent ft) of semigroup generators, one can relax the summation condition to
∑
n∈Z
‖m(2n·)ϕ0‖Wc
2 (R)
1 +|n| <∞
as for maximal estimates in the euclidean case [CGHS], or with an additional factorlog(|n|+ 2)
as in [Choi]. As another possible relaxation, one can ask the question, whether
∑
n∈Z
‖m(2n·)ϕ0‖2
Wcq (R) <∞
is suﬃcient for our estimates, which is known to be true for the classical maximal estimate of
the euclidean Laplacian [CGHS, (1.3)]. For this, it would be interesting to know whether there
are other approaches toq-variational and time dependent maximal estimates than ours, in case
of the euclidean Laplacian or sub-Laplacians on Lie groups. Alsoq-variational estimates for
spectral multipliers that do not decay at∞are not well understood. Already the scalar case
Y = C would be interesting.
In the context of Section 4, it would be interesting to get information on the normCp,q,d,Y in
Theorem 4.2 and onCp,q,Y in Proposition 4.4, depending onp,q (,d ) andY. Also one could try
to ﬁnd a proof of Proposition 4.4 using Hörmander functional calculus that also covers small,
so ﬁnally all, dimensions.
