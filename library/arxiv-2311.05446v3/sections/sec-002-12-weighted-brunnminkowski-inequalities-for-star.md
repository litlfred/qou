---
doc_id: arxiv-2311.05446v3
doc_title: "NEW BRUNN–MINKOWSKI AND FUNCTIONAL INEQUALITIES VIA CONVEXITY OF ENTROPY"
section_id: sec-002-12-weighted-brunnminkowski-inequalities-for-star
section_title: "Weighted Brunn–Minkowski inequalities for star bodies"
section_number: 1.2
pages: 3-5
source_pdf: 2311.05446v3.pdf
source_sha256: c5809730f598a56d
doc_brief: "NEW BRUNN–MINKOWSKI AND FUNCTIONAL INEQUALITIES VIA CONVEXITY OF ENTROPY — We study the connection between the concavity properties of a measureνand the convexity properties of the associated"
---
spite the difficulties mentioned above when dealing with non-convex sets, in
this paper we prove the following theorem:
Theorem 1.3.LetV:R n→[0,∞)be ap-homogeneous convex function
for1<p<∞, and letνbe a measure with density dν
dx proportional toe−V .
LetK 0,K 1⊆R n be star bodies. Then for all0≤t≤1we have
ν((1−t)K 0 +tK 1)
p−1
pn ≥(1−t)ν(K 0)
p−1
pn +tν(K 1)
p−1
pn .(6)
To explain the terminology, we say thatK⊆R n is a star body ifKis a
Borel set such that for allx∈Kand 0≤λ≤1 we haveλx∈K(i.e. the
“star” ofKis always assumed to be at the origin). Also recall thatVis
p-homogeneous ifV(λx) =λ pV(x) for allx∈R n andλ>0.
Note that one specific choice,V(x) = 1
2|x|2, gives the Kolesnikov–Livshyts
result ((4)), but this time without the convexity assumption on the sets. For
any fixedp>1 the exponent p−1
pn is asymptotically (for largen) better than
the result of [34], and again we need no convexity or symmetry assumptions,
but of course our result is only for homogeneous potentials and not for all
log-concave measures. Note that asp→∞we have p−1
pn → 1
n, the opti-
mal exponent. This makes sense since for largepthe measureνis almost
uniform on some convex body, and such uniform measures do satisfy the
Brunn–Minkowski inequality with exponent 1
n, applicable to all Borel sets.
4 GAUTAM AISHWARYA AND LIRAN ROTEM
As mentioned above, as far as we know none of the previously used tech-
niques can prove a result like Theorem 1.3. Our proof will therefore follow
completely different lines, using tools of optimal transport and information
theory. We lift the problem at hand from the realm of geometry of sets to
the realm of geometry of measures, where calculus is sometimes “smoother”
than in classical differential geometry. Arguably, even for the Gaussian mea-
sure, our proof is simpler than the known arguments.
The theory of optimal transport gives us a natural way to interpolate
between two probability measuresµ 0 andµ 1, such that the interpolantµ t
is supported in the Minkowski average (1−t)·support(µ 0) +t·support(µ 1)
of the two supports, thereby playing a role parallel to the Minkowski aver-
aging of sets. Along these interpolations, the relative entropyD(·∥ν) enjoys
convexity properties of various degrees depending onν. The reader will find
precise definitions in Section 2. However, the main point is that a variational
formula forνcan be written in terms of the relative entropyD(·∥ν),
sup
µ∈P(K)
e−D(µ∥ν) =ν(K),(7)
where the supremum runs over all probability measures onKand is attained
at the normalized restrictionνK ofνtoK, allowing us to translate convexity
properties of the relative entropy into concavity properties of the measure
ν.
Since the density dνK
dν is radially decreasing whenKis a star body, we
will obtain Theorem 1.3 as a corollary to the following result.
Theorem 1.4.LetV:R n→[0,∞)be ap-homogeneous convex function
for1<p<∞, and letνbe the probability measure with density proportional
toe−V . Letµ 0,µ 1 be Borel probability measures, absolutely continuous with
respect toν, such that dµ0
dν and dµ1
dν are radially decreasing. Finally, let
{µt}t∈[0,1] be the displacement interpolation betweenµ 0 andµ 1. Then
t7→e −p−1
pn D(µt∥ν) (8)
is concave.
It is well known that the behavior of information-theoretic quantities un-
der optimal transport is intimately related to the geometry of the underlying
space, which is useful in the context of Brunn–Minkowski type inequalities
(see for example Remark 2.11). There are known proofs of the classical
Brunn–Minkowski or Pr´ ekopa–Leindler inequalities along these lines ([47,
Chapter 6]). However, to the best of our knowledge this is the first time
such tools are used to prove previously unknown Brunn–Minkowski type
inequalities for measures on Euclidean space.
To prove Theorem 1.4 we split the relative entropyD(µ∥ν) of a measureµ
into its “internal energy”D(µ∥Voln) and “potential energy”
R
Vdµcompo-
nents. We observe that, under the assumptions onµ 0 andµ 1 as in Theorem
