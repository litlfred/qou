---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables"
section_id: sec-032-the-smooth-case
section_title: "The smooth case"
section_number: null
pages: 200-224
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
---
We now generalize the above argument to any rational function whose singular
varietyV is a complex manifold. The square-free part ˜Q of the polynomial Q
is the product of its distinct irreducible factors over the complex numbers, and
we say that Q is square-free if ˜Q = Q. We callz∈V a smooth point if∇ ˜Q(z)
is non-zero, and say thatV is smooth if ˜Q and all its partial derivatives never
simultaneously vanish. The implicit function theorem implies that a smooth
singular variety can be viewed both as a (d−1)-dimensional complex manifold
and as a (2d− 2)-dimensional real manifold, and both of these viewpoints will
be beneﬁcial. We introduce the square-free part of Q so that the converse also
holds.
Lemma 7.6. The inequality∇ ˜Q(z), 0 holds for a pointz∈V Q if and only
ifV is a smooth manifold in a neighborhood ofz.
Proof Sketch The forward implication follows from the implicit function the-
orem. The converse, that∇ ˜Q(z) = 0 implies a geometric singularity, is harder
to prove. Let mx denote the maximal ideal of functions vanishing at x in the
ring of polynomial functions vanishing on V, and let nx denote the maximal
ideal of functions vanishing at x in the ring of germs of analytic functions at
x (as deﬁned in Deﬁnition 10.42 below). Then ∇ ˜Q(x) = 0 implies mx/m2
x
has dimension d rather than d− 1 (see [Sha13, Exercise 2.2 and Theorem 2.1])
7.2 The smooth case 183
so that nx/n2
x has dimension d, and this property is invariant under bi-analytic
mapping. At any smooth point of a complex hypersurface there is a coordinate
neighborhood takingx to the origin and making the hypersurface into the coor-
dinate plane where z1 = 0. In this casen0/n2
0 has dimension d−1, which would
be a contradiction, hence V is not a complex manifold in a neighborhood of
x. A little more work showsV is not locally a C∞ manifold either. □
Our starting point, as always, is the multivariate Cauchy Integral Formula
ar =
( 1
2πi
)d ∫
T
z−r−1F(z) dz, (7.7)
which gives an exact representation for ar. We view this representation not as
a standard integral from multivariate calculus, but as the integral of the diﬀer-
ential formω =z−r−1F(z) dz over the d-chain T. The necessary background
on diﬀerential geometry and the basics of integration of forms is discussed in
Appendix A. Appendix B reviews concepts from algebraic topology, including
homology and cohomology classes. In particular, sinceM =Cd
∗\V is the do-
main of holomorphicity for ω, the Cauchy integral depends only on the class
of T in the singular homology group Hd(M) and the class ofω in the singular
cohomology group Hd(M).
We break our argument into pieces, generally mirroring the ﬁnal approach
to Example 7.3 above. In this chapter we mainly stick to theoretical consider-
ations; methods for computing the quantities that arise are discussed in Chap-
ter 8.
Step 1: Characterize critical points
We begin by deﬁning the height function
hr(z) :=−r· Relogz =−
d∑
j=1
r j log|z j|,
which captures the magnitude of the Cauchy integrand
⏐⏐⏐z−r−1F(z)
⏐⏐⏐ = e|r| h ˆr(z)·
⏐⏐⏐z−1F(z)
⏐⏐⏐
as
⏐⏐⏐z−1F(z)
⏐⏐⏐ independent of|r|. The ordering hr gives toCd
∗ does not change if
r is multiplied by a positive scalar, so our arguments about the height function
will hold whenever r is replaced by any positive multiple. This invariance
property means that an analysis of ar asr→∞ with ˆr =r/|r| converging to
some ﬁxed ˆr∗ can usually be accomplished with the ﬁxed height function h ˆr∗.
In particular, if ˆr∗ is a ﬁxed direction and hr∗(x)< hr∗(y) then, asr→∞ with
ˆr→r∗, the Cauchy integrand is exponentially smaller atz =x than atz =y.
Whenr is understood we write simply h for hr.
184 Overview of analytic methods for multivariate GFs
Deﬁnition 7.7. A smooth critical pointz of the rational function F = P/Q in
the direction ˆr is a smooth point ofV∗ that is a critical point ofh ˆr :V∗→R as
a smooth mapping of real manifolds. The set of critical points in the direction
ˆr is denoted by critical(r).
The height function h ˆr is the real part of (a branch of) the analytic function
φ(z) =−r· logz, and the Cauchy–Riemann equations imply that the critical
points of F in the direction ˆr can also be computed as the critical points of
φ :V∗ → C as a (locally) holomorphic mapping of complex manifolds. In
particular, we have the following explicit deﬁnition of smooth critical points.
Lemma 7.8. Assume thatV is a smooth manifold and let ˜Q be the square-free
part of the denominator Q. Thenw∈Cd
∗ is a critical point in the direction ˆr if
and only if it satisﬁes the smooth critical point equations
˜Q(w) = rkw1 ˜Qz1(w)− r1wk ˜Qzk(w) = 0 (2 ≤ k≤ d), (7.8)
where ˜Qz j denotes the derivative of ˜Q with respect to the variable zj.
Proof The pointw is a critical point when Q(w) = 0 and the diﬀerential of
φ :V∗ → C is zero. Vanishing of this di ﬀerential occurs exactly when the
diﬀerential of φ as a map from Cd
∗ toC projects to zero on the tangent space
ofV∗ atw. Since the tangent space toV∗ atw is the hyperplane with normal
(∇ ˜Q)(w), the diﬀerential ofφ projects to zero if and only if (∇φ)(w) is parallel
to (∇ ˜Q)(w). These vectors are parallel if and only if all 2 × 2 minors of the
matrix 
(
∇ ˜Q
)
(w)
(∇φ) (w)
 =
( ˜Qz1(w) ··· ˜Qzd(w)
−r1/w1 ··· − rd/wd
)
vanish. Vanishing of the minors simpliﬁes to give the smooth critical point
equations. □
Remark 7.9. The smooth critical point equations (7.8) form a polynomial
system with d equations in d variables. It is therefore unsurprising that gener-
ically Q has a ﬁnite number of critical points (i.e., this holds for all polyno-
mials Q except for those whose coe ﬃcients come from a ﬁxed algebraic set
depending only on the degree of Q). This follows directly from an algebraic
version of Sard’s Theorem, which can be found in [BPR03, Theorem 5.56];
see also [Mel21, Section 5.3.4] for an explicit derivation.
Exercise 7.4. Continuing Exercise 7.3, letr = (2, 1) and ﬁnd the critical points
for hr onV. Compute the heights of these critical points and compare them
to the limit height for the sequence approaching inﬁnity in Exercise 7.3. Is the
limit height larger than the heights of all critical points onV?
7.2 The smooth case 185
Proposition 7.10. Singularity of the Hessian matrix for hˆr in local coordinates
at a critical point for hˆr on the smooth varietyV∗ is independent of the choice
of coordinatization ofV∗ as a complex manifold.
Proof At a point p where∇ h ˆr vanishes, the chain rule under a coordinate
change Ψ simpliﬁes toH′ = JΨH, whereH′ is the new Hessian, H is the
old Hessian, and JΨ is the Jacobian matrix of Ψ atp. The claim follows from
nonsingularity of JΨ atp. □
Deﬁnition 7.11. A smooth critical pointw of h is called nondegenerate if the
Hessian matrix for h in local coordinates aroundw is nonsingular.
This deﬁnition is generalized to non-smooth points in Deﬁnition 7.34 below.
Under our assumption that V is smooth, one of the partial derivatives of the
square-free part of Q is nonvanishing at w. Without loss of generality, we
assume that ˜Qzd(w), 0 is non-zero, so we can parametrizeV nearw as zd =
g(z◦) = g(z1,..., zd−1) for some analytic function g deﬁned in a neighborhood
ofw◦. The critical pointw is nondegenerate if and only if the Hessian matrix
of h(z◦, g(z◦)) with respect to z1,..., zd−1 has non-zero determinant at z◦ =
w◦. We say h is a Morse height function when all of its critical points are
nondegenerate.
Remark. Most topological works, such as [Mil63; GM88], study spaces using
Morse height functions. However, as discussed in Appendix C, as long as there
are ﬁnitely many critical points the basic Morse decompositions hold whether
or not h is Morse: the topology of the space is still generated by attachments at
the critical points. However, the description of the attachments becomes more
complicated for non-Morse height functions.
Step 2: Intersect the torus with the singular variety
The Cauchy integral representation (7.7) holds for any torus T = Relog−1(x)
withx in the component B of amoeba(Q)c corresponding to the convergent
Laurent expansion with coeﬃcients ar. We want to replace the domain of in-
tegration T with a domain of integration close to V that “wraps around” the
singular variety, so we can use a residue computation in Step 3 below to reduce
to an integral “on”V.
Ifγ is any (d− 1)-chain inV∗ then the Collar Lemma (Lemma C.1 in Ap-
pendix C) shows how to construct the tube oγ aroundγ, which is a d-chain
in the domain M where the Cauchy integral ω is holomorphic. The tube oγ
can be viewed as a union of circles with centers at the points of γ, and the
186 Overview of analytic methods for multivariate GFs
mapγ↦→ oγ is well deﬁned as a map from the homology group Hd−1(V∗) to
Hd(M).
Theorem C.2 of Appendix C implies that o : Hd−1(V∗)→ Hd(M) is injec-
tive, and if T′ is any torus contained inM then pulling back [T− T′]∈ Hd(M)
via o gives a well-deﬁned class INT(T, T′)∈ Hd−1(V∗) known as the intersec-
tion class of T and T′. By construction, [T]− [T′] = o INT(T, T′) in Hd(M),
so that
ar =
( 1
2πi
)d ∫
T
ω =
( 1
2πi
)d ∫
o INT(T,T′)
ω +
( 1
2πi
)d ∫
T′
ω.
One can picture o INT(T, T′) by imagining a continuous deformation of T to
T′. If this deformation is su ﬃciently generic it will intersectV∗ transversely,
with the intersection yielding INT(T, T′). The tube around INT(T, T′) is thus
the chain that needs to be added to account for passing the deformation through
V∗. See Figure 7.7 for an illustration.
Figure 7.7 An intersection class of T and T′ with respect toV.
If we pick a torus T′ so that
∫
T′ω = 0 then we have succeeded in expressing
the Cauchy integral as an integral over a tube around a curve in V∗. Corol-
lary 6.29 implies the existence of such a torus, giving the following.
Proposition 7.12. Assume F is the ratio of coprime polynomials F (z) =
P(z)/Q(z). As r → ∞in the direction ˆr there exists a torus T ′ such that
7.2 The smooth case 187
∫
T′ω = 0 for all but ﬁnitely manyr, and
ar =
( 1
2πi
)d ∫
o INT(T,T′)
ω (7.9)
whenever the integral over T′ is zero. □
Exercise 7.5. Let Q(x, y) = 1− x− y− x2y2, whose amoeba is shown in
Figure 7.8. When r = (1, 1), which components of amoeba(Q)c have hr un-
bounded from below, and which vertices of the Newton polygon forQ do these
regions correspond to under the relationship described in Theorem 6.18?
Figure 7.8 Amoeba of Q(x, y) = 1− x− y− x2y2.
We can convert thed-dimensional integral in (7.12) to a (d− 1)-dimensional
integral over the intersection cycle, which lies in V∗. This is accomplished
using the concept of multivariate residues (also called Leray residues). Ap-
pendix C.2 gives a summary of multivariate residues, but for this discussion
it is suﬃcient to note that the residue form Res(τ) of a meromorphic d-formτ
with singularities contained inV is a (d−1) form restricted toV. Theorem C.9
implies that
1
2πi
∫
oγ
τ =
∫
γ
Res(τ)
for any (d− 1)-chainγ inV∗ and holomorphic d-formτ onM.
In particular, combining the residue operator with Proposition 7.12 gives the
following.
188 Overview of analytic methods for multivariate GFs
Proposition 7.13. If T′ is a torus described by Proposition 7.12 then
ar =
( 1
2πi
)d−1 ∫
INT(T,T′)
Resω. (7.10)
□
Exercise 7.6. Suppose d = 1 andV =VQ where Q(z) = 2− 3z + z2. Let T be
a circle of some small positive radiusε and T′ be a circle of some large radius
M.
(a) What is the cycle INT(T, T′)?
(b) What is the form Res(ω) whenω = Q(z)−1z−n−1dz?
(c) What is
∫
INT(T,T′) Res(ω)?
(d) What is o INT(T, T′)?
(e) Describe in words why o INT(T, T′) is homologous toT−T′ in H1(C∗\V).
Step 3: Determine a Morse-Theoretic Decomposition of the
Singular Variety
Having reduced the Cauchy integral to an integral over an intersection cycle
γ = INT(T, T′) lying in the singular varietyV∗, we now want to deform γ in
V∗ to represent the coeﬃcient sequence of interest as a sum of saddle point in-
tegrals. Because we are currently assumingV is smooth, we could try to com-
pute such a representation by taking a gradient ﬂow of γ onV with respect to
the height function h ˆr. Ifγ can be deformed so that it lies in the neighborhood
of a nondegenerate critical point σ of h ˆr, except for points of height at most
σ−ε for someε> 0, then we can apply the saddle point techniques of Chap-
ter 5 to compute asymptotics (up to an exponentially negligible error, coming
from ignoring points of lower height).
Actually computing such a gradient ﬂow on real examples is usually not
feasible. Fortunately, one of the most important consequences of Morse theory
is that under reasonable conditions there are only a ﬁnite number of possi-
bilities for the long-term behavior of such a ﬂow . In particular, as detailed in
Appendix C and summarized here, if the ﬂow does not stay at bounded height
while escaping to inﬁnity onV∗ then we can ﬂowγ until it gets locally “stuck”
on one of the critical points of h ˆr.
Our results are phrased in the language of singular homology , reviewed
in Appendix B. Of particular use to us are the notions of relative homology,
which allows us to discuss homology near a critical point while ignoring points
7.2 The smooth case 189
Figure 7.9 The curve γ is deformed to a curve γz locally draped over a saddlez
centered at a critical point for the height function. The tubes around γ andγz are
also pictured.
of lower height that do not a ﬀect dominant asymptotic behavior, and attach-
ments, which describe how to decompose the singular variety by joining to-
gether topologically simpler spaces. Our discussion here summarizes the main
points of the machinery developed in the appendices before applying them to
our situation.
Morse theory represents the topology of a manifold X equipped with a
smooth map h : X→R in terms of successive attachments. The smooth func-
tion h is referred to as a height function on X. As discussed above, we say h
is a Morse if its critical points are nondegenerate, and proper if the inverse
image of any closed interval is compact. Let X≤c denote the subspace of all
pointsz∈ X with h(z)≤ c and suppose that h is a proper Morse function. As
described in Section C.3 of Appendix C, Morse theory describes the change
in topology when the space X≤a is increased to X≤b using the language of at-
tachments. Moving from X≤a to X≤b is a homotopy equivalence (no change in
topology) unless h has critical values in [ a, b]. When there is a single critical
pointz with height in this interval, the topology changes via a topological at-
tachment: X≤b is homotopy equivalent to X≤a on which aλ-ball B is glued via
an attaching mapφ :∂B→ X≤a. The value ofλ is the Morse index of the criti-
cal pointz, which can be thought of as the dimension of the downward facing
part of the generalized saddle atz and computed in local coordinates using the
Hessian of h atz.
Figure C.3 in Appendix C shows how the decapitated unit sphere S≤1−ε be-
comes the full unit sphere by the attachment of a cap and the north pole (Morse
index 2), while Figure C.5 in Appendix C shows how a contractible patch near
190 Overview of analytic methods for multivariate GFs
the bottom of a torus becomes homotopy equivalent to a circle when a bridge
(homotopy equivalent to an arc) is added at the ﬁrst Morse index-1 critical
point. These diagrams are reproduced here in Figure 7.10 for convenience.
Figure 7.10 Two examples of attachments.
We now specialize to the case where X =V∗ and h = h ˆr for some ﬁxed
unit vector ˆr. It is not true that h will always be proper, however we can work
around this diﬃculty. Ifσ∈V ∗ is a critical point then the gradient (∇h ˆr)(σ)
projects to zero on the tangent plane TσV∗⊂Cd. Roughly speaking, a critical
point at inﬁnity is a sequence of points z(k) ∈V ∗ going oﬀ to inﬁnity such
that the projection of (∇h ˆr)(z(k)) to Tz(k)V∗ approaches zero as k→∞ ; the
associated critical value at inﬁnity is the limit of h ˆr(z(k)) as k→∞ . Critical
points at inﬁnity are deﬁned formally in Deﬁnition 7.42 below. Provided there
are no critical points at inﬁnity, the classic results of Morse theory hold even
when the height function is not proper.
Lemma 7.14. Suppose h ˆr has no critical values at inﬁnity in the interval[a, b].
If there are no critical values in [a, b] then the inclusion X≤a⊆ X≤b is a ho-
motopy equivalence. If there is a single critical point z with critical value
h ˆr(z) = c∈ (a, b), then the pair (V≤b,V≤a) is homotopy equivalent to aλ-cell
relative to its boundary, whereλ is the Morse index of the critical point z for
h ˆr.
Exercise 7.7. What isλ in the attachment in the bottom row of Figure 7.10?
It is convenient to postpone the proof of Lemma 7.14 until the more general
setting when we no longer require V to be smooth. After establishing addi-
tional results below, Lemma 7.14 follows directly from Lemma 7.25, which
asserts the homotopy equivalence, and the identiﬁcation of the attachment in
7.2 The smooth case 191
Theorem 7.35(b). In the present smooth case, a nice simpliﬁcation occurs: be-
cause the height function is the real part of a complex (locally) analytic func-
tion, every critical pointz∈V∗ has Morse index d− 1.
Exercise 7.8. Prove that the real part of a complex analytic function deﬁned
on an open set inCd has Morse index d, then prove that the real part of such a
function restricted to a smooth hypersurface has Morse index d− 1. Hint: The
Cauchy–Riemann equations yield a lot of information about the eigenvectors
and eigenvalues of the Hessian.
This characterization of the index allows us to show thatHd−1(V∗) is homo-
logically a bouquet of (d− 1)-spheres, one quasi-local to each critical point. A
version of the following theorem, with the stronger assumption thath is proper
replacing the assumption of no CV AI, is stated and proved as Theorem C.39
in Appendix C (the appendices contain background material not specialized
to ACSV). The restriction that the critical values are distinct is removed in
Corollary 7.17.
Theorem 7.15. Assume thatV is smooth, h ˆr is a Morse height function, and
there are no critical values at inﬁnity (according to Deﬁnition 7.43 below).
Assume further that the critical values c j = h ˆr(z j) are distinct and listed in
descending order.
(i) Each projection H d−1(V∗)→ Hd−1(V≤c j+ε,V≤c j−ε) is surjective. In other
words, the relative homology generator at z j can be chosen to be an
absolute cycle.
(ii) Each inclusion V≤c⊆V∗ induces an injection on H d−1. In other words,
there are no relations: no homology generator ever gets killed.
It follows that Hd−1(V∗)Zm and that a basisγ1,...,γ m for Hd−1(V∗) can be
chosen so that eachγ j is a cycle on which h ˆr attains its maximum value atz j.
Proof Part (i) of Theorem 7.44 below extends the fundamental Morse Lemma,
namely homotopy equivalence ofM≤c as c varies in an interval with no critical
values (Lemma C.27) from the case where h is a proper Morse function to the
case where h need not be proper but there are no CV AI in the interval. Part (ii)
of Theorem 7.44 extends the smooth attachment theorem for a single critical
value c (Theorem C.28) from the case where h is a proper Morse function to
the case where h need not be proper but there are no CV AI in the interval.
Accordingly, the conclusions of Theorems C.38 and C.39 hold for this case,
via the same argument. Speciﬁcally, these follow from the identiﬁcation of the
attachment and from the homology long exact sequence for the ﬁltration of
pairs (M≤b j,−∞), where b j are real numbers between each successive pair of
192 Overview of analytic methods for multivariate GFs
critical values, b0 is above the highest critical value, and−∞ isMb for any b
less than the least critical value. See Section C.4 for details. □
Remark 7.16. The isomorphism Hd−1(V∗)
⨁m
j=1 Hd−1(Vc j+ε,Vc j−ε) is not
natural. For each attachment at z j there is an arbitrary choice of an absolute
cycle γ j that projects to the generator of the homology group for the attach-
ment. The cycle γ j +α would do equally well for any cycle α supported on
Vc j−ε. One might say that the choice of γ1,...,γ m, listed in decreasing order
of height, can be altered by an arbitrary upper triangular map, replacing γ j
byγ j + ∑
i> j biγi. This is the so-called Stokes phenomenon, illustrated in Fig-
ure 7.11: the saddle point integral fromz j might pass on either side ofzi as it
travels downward, with the integrals over the two choices of contour diﬀering
by the integral overγi. Thus, for a cycleC the decomposition [C] = ∑m
k=1 nkγk
is not natural. It is important to note, however, that the leading coeﬃcient n j∗ is
well-deﬁned independent of the chosen basis {γ j}, where j∗ is the least index
such that n j∗ , 0.
Figure 7.11 Stokes’s phenomenon reﬂects the fact that a curve draped over the
higher saddle can descend on either side of the lower saddle, as shown here by
two possible branches. The diﬀerence between these two curves is a curve draped
over the lower saddle.
The simplifying assumption of distinct critical values is not important. To
get rid of this, we deﬁne the local homology pairVp,loc at a critical pointp at
height c to be the pair (X, Y), where Y =V≤c−ε/2 and X is the union of Y with
the ball Bε(p) forε >0 suﬃciently small (see Deﬁnition C.31 of Appendix C
for full details). Any such pairs are homotopy equivalent as long as ε is small
enough that the 2ε-balls about diﬀerent critical points are disjoint.
Deformations deﬁned in Appendix C show that if there is a unique critical
pointp with height c∈ [a, b] then, for small ε > 0, the local pair Vp,loc is
homotopy equivalent to the slab (V≤c+ε,Vc−ε). The beneﬁt to replacing the
slab by the local pair occurs when there are multiple critical points sharing a
7.2 The smooth case 193
critical value. If h ˆr(p) = c for allp in some ﬁnite set E then
(V≤b,V≤a)≃
⨁
p∈E
Vp,loc, (C.3.1)
giving the following.
Corollary 7.17. Replacing (Vc j+ε,Vc j−ε) byVz,loc for each z, the conclu-
sions of Theorem 7.15 hold without the assumption of distinct critical values.
□
We end this subsection with some examples of this topological decomposi-
tion.
Example 7.18 (binomial coeﬃcients). Recall that the binomial coe ﬃcients
ars =
(r+s
r
)
have bivariate generating functionF(x, y) = 1/(1−x−y). If ˆr = (r, s)
with r + s = 1 and r, s∈ (0, 1) then as r varies from 0 to 1, the critical point
w( ˆr) of F in the direction ˆr slides from (0, 1) to (1, 0). The homology group
H1(V∗) has a single generator γz∗. The homology group H2(M) is cyclic as
well, generated by oγz∗. ◁
Example 7.19 (Delannoy numbers). The Delannoy number generating func-
tion from Example 2.7 in Chapter 2 is 1/(1− x−y− xy). The situation is similar
to Example 7.18, except that as r varies from 0 to 1 the critical pointw( ˆr) tra-
verses the arc the other way from (0 , 1) to (1, 0), and there is another critical
pointw′ traversing a hyperbola in the third quadrant. ◁
Exercise 7.9. Consider the amoeba of the denominatorQ(x, y) = 1− x− y− xy
of the Delannoy generating function, shown in Figure 7.12.
(a) Compute the critical points w andw′ in the direction determined by r =
(2, 3), then draw dots wherep = Relog(w) andp′ = Relog(w′) lie on the
amoeba.
(b) Find a path β, from the power series component of the amoeba complement
to a component where the Cauchy integral is zero, that enters the amoeba
atp and exits it atp′.
(c) Describe γ = Relog−1(β).
(d) State why [ γ] = INT(T, T′) in H1(V∗) and why
∫
γ Resω is easy to esti-
mate, where
ω = x−2n−1y−3n−1
1− x− y− xydx∧ dy.
194 Overview of analytic methods for multivariate GFs
Figure 7.12 Amoeba for the Delannoy generating function Q(x, y) = 1−x−y−xy.
Each point interior to the amoeba is the image of precisely two points ofV under
Relog.
Result: a saddle point integral decomposition in the smooth case
Theorem 7.15 and Corollary 7.17 give a basis ofHd−1(V∗) consisting of cycles
that attain their maximum values at critical points. Vanishing of dh ˆr|V atz
is equivalent to z−r being in stationary phase at z for any ( d− 1)-chain γ j
supported onV∗. Thus, combining Theorem 7.15 and Corollary 7.17 with the
integral representation in Proposition 7.13 gives the following, our ultimate
goal for generating functions with smooth singular varieties.
Theorem 7.20 (smooth saddle point integral decomposition). Assume thatV
is smooth, h ˆr is a Morse height function, and that there are no critical values
at inﬁnity (see Deﬁnition 7.43 below). Assume further that the critical values
c j = h ˆr(z j) for 1≤ j≤ m are listed in descending order. Then there exist
integers κ j ∈ Z and smooth chains of integration γ j with heights uniquely
maximized atz j, such that
ar =
m∑
j=1
κ j
(2πi)d−1
∫
γ j
z−r−1 Res(F(z) dz). (7.11)
The integral in the jth summand is in stationary phase at z j. The least j such
that κ j , 0, and the homology class ∑
j′∈Eκ j′γ j′ for all j ′ such that z j′ has
height c j, are uniquely deﬁned. □
There are two important tasks remaining: computing asymptotics of the sad-
dle point integrals and determining the integersκ j. While integral asymptotics
(in this smooth case) follow in a straightforward manner from the results of
Chapter 5, it can be very di ﬃcult to determine these unknown integers. We
7.2 The smooth case 195
discuss both of these questions in Chapter 9, where we derive explicit asymp-
totic formulae for ar in terms of the generating function F(z). Readers who
are interested only in smooth asymptotics (and do not need to see the technical
discussion of critical points at inﬁnity) may go directly to Chapters 8 and 9,
after a brief discussion about removing our simplifying hypotheses.
The requirement of no critical value at inﬁnity is essential: when there are
critical points at inﬁnity, asymptotics are in principle a ﬀected. Classifying
these cases and computing the asymptotics remains an open problem discussed
further in Chapter 13. Removing the smoothness assumption involves the ap-
paratus of stratiﬁed Morse theory, which we make use of in the next section.
The assumption that h ˆr is nondegenerate is not essential, however in its ab-
sence there is no longer a unique cycle γ j for each j. We handle this case, for
now, by two examples.
Example 7.21 (cubic degeneracy). The simplest degeneracy at a critical point,
a so-called monkey saddle, leads to two independent homology generators as
in Figure 7.13. ◁
Figure 7.13 Two homology generators associated with a monkey saddle.
196 Overview of analytic methods for multivariate GFs
While critical points are generically nondegenerate, we now give one com-
binatorial example in which a critical point w is indeed degenerate and con-
tributes more than one generator.
Example 7.22 (bi-colored supertrees). Example 9.32 in Chapter 9 looks at
a rational generating function counting bi-colored supertrees (certain planar
binary trees that need not concern us here). The singular variety is the smooth
surface deﬁned by the vanishing of Q(x, y) = x5y2 + 2x2y− 2x3y + 4y + x− 2.
When ˆr = (1/2, 1/2) then there are two nondegenerate critical points, u and v,
together with a critical pointw near which h ˆr is quartic (so doubly degenerate).
Accordingly there is one cycle γu, one cycle γv, and three cycles γ( j)
w which
may be conﬁgured all to enter w along the solid arc and exit along one of the
three dashed arcs shown in Figure 7.14. ◁
Figure 7.14 The supertree generating function yields two nondegenerate critical
points and one doubly degenerate critical point.
7.3 The general case via stratiﬁed Morse theory
We now drop the assumption that the singular varietyV is smooth. As detailed
in Appendix D, the correct notion for us is the concept of a Whitney stratiﬁed
space: every real or complex algebraic (or analytic) variety admits a Whitney
stratiﬁcation, and the analytic constructions we require for asymptotics can
be built for stratiﬁed spaces. In this chapter we recount only the results from
Appendix D that we directly require. Although we typically assume that F is
7.3 The general case via stratiﬁed Morse theory 197
a rational function to simplify our presentation, the results discussed here hold
for general meromorphic functions with minor modiﬁcations.
Example 7.23. Figure 7.15 shows the zero setV of the polynomial Q = (z3−
x2)(2− x− y− z). We can split the variety V into a ﬁnite number of semi-
algebraic strata (deﬁned by polynomial equalities and inequalities): two strata
of codimension 1,
S 1 =
{
x + y + z = 2 and z3− x2 , 0
}
S 2 =
{
z3− x2 = 0 and x + y + z, 2
}
\{ x = z = 0},
two strata of codimension 2,
S 3 =
{
z3− x2 = 0 and x + y + z = 2 and (x, z), (0, 0)
}
,
S 4 ={(x, z) = 0 and y, 2},
and one stratum of codimension 3 at the point
S 5 ={z3− x2 = x + y + z− 2 = x = z = 0} ={(0, 2, 0)}.
Note that we introduce additional strata both to account for multiple irreducible
components ofV and to account for singularities in individual components. ◁
As described in Appendix D, it is usually not su ﬃcient to partitionV into
any general set of smooth manifolds – we must also make sure the elements in
such a partition “ﬁt together nicely.” This concept is formalized by the notion
of a Whitney stratiﬁcation, given in Deﬁnition D.3 of Appendix D. For the rest
of this chapter we ﬁx a Whitney stratiﬁcation of V, which is a partition ofV
into manifolds{Sα :α∈ I} indexed by some partially ordered set I such that
(i) Sα∩ Sβ ,∅ if and only if Sα⊂ Sβ if and only ifα≤β, and
(ii) if α<β , if the sequences{xi∈ Sβ} and{yi∈ Sα} both converge toy∈ Sα,
if the lines 𝓁i = xi yi converge to a line 𝓁, and if tangent planes Txi(Sβ)
converge to a plane T, then both𝓁 and Ty(Sα) are contained in T.
We always take algebraic stratiﬁcations deﬁned by polynomial equalities
and inequalities. In fact, we may assume that our Whitney stratiﬁcation is de-
ﬁned by a ﬁnite sequence of nested algebraic setsV = F0⊃ F1⊃···⊃ Fm =
∅ such that the connected components of the setsFi\ Fi+1 for all 1≤ i≤ m− 1
form the strata. If S is a stratum deﬁned as a connected component of Fi\ Fi+1
then the dimension of the stratumS (respectively thecodimension of the stra-
tum S ) is the dimension (respectively codimension) ofFi⊂Cd as an algebraic
set. Whitney stratiﬁcations exist for all algebraic (and analytic) varieties, and
algorithms to compute them are discussed in Chapter 8 and Appendix D.
198 Overview of analytic methods for multivariate GFs
Figure 7.15 The zero set of Q = (z3− x2)(2− x− y− z).
Stratiﬁed critical points
A pointp in a stratum S is said to be a (stratiﬁed) critical point for the height
function h = h ˆr if the restriction dh|S vanishes atp. Analogously to the smooth
case above, becauseh is the real part ofφ(z) =−r·logz the Cauchy–Riemann
equations imply thatp is a critical point if the gradient of φ lies in the normal
space to S atp. If S has codimension k then there exists an open set U ⊂
Cd containing p and irreducible polynomials g1,..., gk such that S∩ U =
V(g1,..., gk)∩ U (i.e., S is locally deﬁned by the polynomials gi nearp).
The point p is a critical point if and only if the gradient ( ∇φ)(p) lies in the
complex span of the gradients ( ∇ g1)(p),..., (∇ gk)(p). Although φ involves
logarithms, its gradient is a rational function, so we may compute stratiﬁed
critical point by solving polynomial systems. Computation of stratiﬁed critical
points is discussed at greater length in Chapter 8.
Recall from Chapter 6 that the logarithmic gradient of a diﬀerentiable func-
tion f atz∈Cd is the vector
∇log f (z) = (z1 fz1,..., zd fzd(z)) , (7.12)
with the word logarithmic coming from the fact that the logarithmic gradient
of f (z) atz = exp(x) is the gradient of ( f◦ exp)(z) atz =x. Ifp is a smooth
7.3 The general case via stratiﬁed Morse theory 199
point of the algebraic hypersurface deﬁned by the vanishing of Q, then the
vanishing of dh ˆr|V atp is equivalent to the direction vector ˆr being parallel
to (∇log Q)(p). More generally, vanishing of dh ˆr|S atp is equivalent to ˆr lying
in the space spanned by the logarithmic gradients of the functions g j locally
deﬁning the stratum S atp.
Figure 7.16 The point z on a stratum S deﬁned by the vanishing of two trans-
versely intersecting smooth sheets in three dimensions is a critical point in the
direction ˆr ifr lies in the log-normal plane to S atz.
Example 7.24. IfV is the union of two transversely intersecting smooth
sheets deﬁned by the vanishing of two polynomialsg1 and g2 thenz is a critical
point onVg1\V g2 in a direction ˆr ifr is parallel to (∇log g1)(z), and the anal-
ogous criteria holds for critical points on Vg2\V g1. A critical point z on the
intersection stratum S =Vg1∩V g2, pictured in Figure 7.16, hasr lying some-
where in the log-normal plane spanned by (∇log g1)(z) and (∇log g2)(z). ◁
Exercise 7.10. Describe the set of directionsr∈ R2
∗ such that dh ˆr|S = 0 at a
point (x, y, z) of the codimension 2 stratum S 3 in Example 7.23.
Obstructions are critical points
The fundamental lemma of Morse theory, described in Lemma 7.14 above,
states that, in the absence of critical values at inﬁnity, critical values are the
only places the topology of the sublevel sets of a manifold can change. The
fundamental lemma of stratiﬁed Morse theory says that (stratiﬁed) critical val-
ues are still the only places the topology of M≤c andV≤c can change, and
thus are the only places obstructions to pushing down cycles of integration
can occur. Lemma 7.14 also speciﬁes the nature of the attachment at a critical
point, but since this requires a more lengthy explanation, we state the stratiﬁed
version of Lemma 7.14 without describing the attachment. As a reminder, we
200 Overview of analytic methods for multivariate GFs
postpone the formal deﬁnitions of critical points at inﬁnity and critical values
at inﬁnity until Deﬁnition 7.42 below.
Lemma 7.25. If h ˆr has no critical values (including at inﬁnity) in [a, b], then
the inclusionM≤a⊆M≤b is a homotopy equivalence. The same is true of the
inclusionV≤a⊆V≤b.
Remark 7.26. The fact that stratiﬁed critical values isolate all the topological
change inV∗ may be less surprising than the fact that they do so inM.
Letp be a stratiﬁed critical point for h ˆr in some stratum S . Mirroring our
deﬁnition ofVp,loc above, we let
Mp,loc := (M≤c−ε∪ B2ε(p),M≤c−ε),
for any suﬃciently smallε> 0, which is deﬁned up to homotopy equivalence.
The simplifying assumption of distinct critical values often fails in ACSV ,
for example if there is a pair of complex conjugate critical points, necessitating
one further deﬁnition. Let c be a critical value, let p1,..., pm be the critical
points at height c, and assume ε is suﬃciently small so that the balls B2ε(pi)
are disjoint.
Deﬁnition 7.27 (all attachments at height c). Under the setup above, the total
attachment pair at height c is
(Mc+,Mc−) :=
M≤c−ε∪
m⋃
j=1
B2ε(p j), M≤c−ε
 . (7.13)
By disjointness of the balls B2ε(p j), this is a direct sum in the category of pairs
ofMp j,loc, hence the homologyH∗(Mc+,Mc−) is the direct sum
m⨁
j=1
H∗(Mp j,loc).
Lemma 7.28. Suppose h ˆr has no critical values at inﬁnity in [a, b] and has a
single critical value c in [a, b], occurring in the interior (a, b). Then the pairs
(M≤b′,M≤a′) are naturally homotopy equivalent for any a≤ a′ < c< b′≤ b.
Lemmas 7.25 and 7.28 are taken from [BMP22]; a sketch of the proof is
reproduced in Section 7.5.
Building by attachment
We now ﬁt together the attachments at critical points of all possible heights.
This involves classical topological facts, and works without knowing the ho-
motopy type of any individual attachment.
Let c1 > c2 >··· > cm denote the critical values in the interval [ cm,∞)
7.3 The general case via stratiﬁed Morse theory 201
Figure 7.17 Building M via successive attachments at the critical values c1 >
c2 >··· > cm. In this case we attach three bumps toMcm− around critical points
at height cm, then attach a single bump, and so on until attaching two ﬁnal bumps.
and assume there are no CV AI in [ cm,∞). For each j let c j− denote c j− ε
whereε> 0 is suﬃciently small so that there are no critical values or CV AI in
[c j−ε, c j), and letc j+ denote c j+ε whereε> 0 is suﬃciently small so that there
are no critical values or CV AI in (c, c j +ε]. Intuitively, we think of building up
the spaceM from the spaceMcm− by successive attachment. First, we attach
(Mcm+,Mcm−) to arrive at the space Mcm+, which, by Lemma 7.28, is homo-
topy equivalent to the spaceMcm−1−. Next we attach the pair (Mcm−1+,Mcm−1−).
Repeating this until the pair (Mc1+,Mc1−) has been attached, we have built the
spaceMc1+, which is homotopy equivalent toM≤b for all suﬃciently large b,
and hence toM itself. This process is illustrated in Figure 7.17. The “bump”
N(p) near a point p is the intersection ofM with a ball of su ﬃciently small
radiusδ. Shrinkingε if necessary, (Mc j−∪N (p),Mc j) has the homotopy type
of the local pairMp,loc discussed above.
Each attachment has a long exact homology sequence. Because all of the
spaces involved are cell complexes of real dimension at mostd (see Section D.4
of Appendix D), the homology groupsHk of dimension k≥ d+1 vanish. Thus,
the long exact sequence for any j≤ m always begins
0→ Hd(Mc j−)→ Hd(Mc j+)→ Hd(Mc j+,Mc j−)→··· . (7.14)
Deﬁnition 7.29. For each critical point p at height c j, let G(p) denote the
image in Hd(Mc j+,Mc j−) of the map projecting Mc j−∪N (p) to the pair
(Mc j−∪N (p),Mc j), as in Figure 7.17. In other words, G(p) are those relative
d-homology classes, once the bumpN(p) nearp is added, that are represented
by absolute cycles. We further deﬁne G = G(c j) :=
⨁
h(p)=c j
G(p).
202 Overview of analytic methods for multivariate GFs
The sequence (7.14) gives rise to the short exact sequence
0→ Hd(Mc j−)→ Hd(Mc j+)→ G→ 0. (7.15)
As we are working with coe ﬃcients in C, there is no torsion, hence the short
exact sequence implies a (not natural) direct sum
Hd(Mc j+) Hd(Mc j−)⊕ Hd(Mc j+,Mc j−). (7.16)
Assuming Lemmas 7.25 and 7.28, we have proved the following.
Theorem 7.30. Suppose there are no critical values at inﬁnity above height a
and ﬁnitely many critical values c1 >··· > cm in [a,∞). Then the homology of
M is given by
Hd(M) Hd (M<a)⊕
⨁
p
G(p),
where G(p) is deﬁned in Deﬁnition 7.29 and the sum is over critical points p
such that h ˆr(p)≥ a. If there are no critical values at inﬁnity and ﬁnitely many
critical values then
Hd(M,M−∞)
⨁
p
G(p)
where M−∞ denotesM≤a for any a less than the least critical value, and the
sum is over all critical points. □
Description of the attachments
Next we describe the attachment cycles forM. We could also develop the at-
tachment cycles forV∗ in the stratiﬁed setting, however our asymptotic results
don’t need them so we skip this extra step.
The key to understanding attachments in Whitney stratiﬁed spaces is a lo-
cal product structure described in Theorem D.9 of Appendix D, which follows
from the famous (and somewhat di ﬃcult) Thom’s Isotopy Lemma (Lemma
D.16 in Appendix D). The Isotopy Lemma says that for a ﬁxed stratum S of
dimension j and any pointp∈ S there is a neighborhood ofp where the space
V looks like R j× N where N is the normal slice of the strata (see Deﬁni-
tion 7.32 and Figure 7.18 below).
What does the local product structure imply for our attachments? Letp∈ S
be a critical point for the height functionh, and consider S as a complex mani-
fold of dimension i (where it has dimension j = 2i as a real manifold). Because
h is the real part of (a branch of) an analytic function, it is harmonic and all
critical points have Morse index i. Thus, when S is arranged by height near
p there is an i-dimensional part that ‘bends downwards’ and ani-dimensional
7.3 The general case via stratiﬁed Morse theory 203
part that ‘bends upwards’. By the local product structure, the pair for the at-
tachment ofM atp is (homotopy equivalent to) the product of a pair (Bi,∂ Bi)
in the tangent space to S and a pair (L,L∩M ≤c−ε), where c is the height of
p, the constantε >0 is suﬃciently small, andL denotes the normal link (the
intersection ofM with the normal space to S atp in a suitable small neighbor-
hood ofp, described in Deﬁnition 7.32 below).
Figure 7.18 An example of an attachment given by the product of a torus with an
arc (a relative 3-torus).
Example 7.31. Figure 7.18 shows an example of an attachment on a stra-
tum S 1 with complex dimension 1 deﬁned by the intersection of two trans-
versely intersecting smooth sheets. In one direction it curves down, as shown;
in the other direction it curves up (this is not shown). The level set deﬁned
by h(z) = c−ε is the horizontal line and the pair ( B1,∂ B1) is the black arc
modulo its endpoints. The normal link is the complement of two intersecting
complex lines in complex 2-space, which is homotopy equivalent to a 2-torus.
The 2-torus can be drawn arbitrarily close top, so it can be chosen as an abso-
lute cycle and the pair (L,L∩M ≤c−ε) is simply (L,∅)≃L . The attachment
pair is obtained by sliding the 2-torus along the black arc from one endpoint
to the other, with the second element in the pair being the starting and ending
positions. Because an arc modulo its boundary is a circle, this means the at-
tachment is a 3-torus, manifested as a 2-torus times an arc that localizes to a
1-torus. ◁
Formal statement of the attachments
The following deﬁnitions and results are special cases of material in Sec-
tion D.3 of Appendix D. Attachments are deﬁned in the category of (homotopy
types of) topological pairs, as are both the tangential and normal Morse data.
Products in this category are deﬁned by
(A, B)× (C, D) = (A× C, A× D∪ B× C), (7.17)
204 Overview of analytic methods for multivariate GFs
and the homology of a product obeys the usual K¨unneth formula for homology
with complex coeﬃcients,
Hk(U× V) =
k⨁
j=0
H j(U)× Hk− j(V). (7.18)
For the spaceM, we deﬁne the Morse data for the attachment at a critical point
p∈V∗ by the following steps.
Deﬁnition 7.32 (Morse data). Let S be a stratum of complex codimension k
containing a critical pointp at height c.
(i) The tangential Morse data T (p) at p is the homotopy type of the pair
(Bd−k,∂ Bd−k) consisting of a ball of codimension k modulo its boundary.
A representative of this class is the unstable manifold for the negative
gradient ﬂow induced by h ˆr onV (the set of points that ﬂow into the
critical point under the positive gradient ﬂow, see [HPS77, Section 4]
or [Con78a]).
(ii) The normal plane Np(S) toS atp is the (complex) orthogonal comple-
ment of the tangent space Tp(S).
(iii) The normal slice N atp is the mutual intersection of V, a su ﬃciently
small ball aboutp, and the normal plane Np(S).
(iv) The normal linkL(p) is the mutual intersection ofM, a suﬃciently small
ball aboutp, and N.
(v) The normal Morse data L(p) is the pair (L(p)≥c,L(p)=c), whereL(p)=c
is the intersection of the normal link with the real codimension 1 surface
where h ˆr(z) = c.
(vi) The Morse data atp is the product of the tangential and normal Morse
data.
The following result, which is the main result in the monograph [GM88], is
stated as Theorem D.21 in Appendix D.
Theorem 7.33. The homotopy type of the attachment pairMp,loc is the Morse
data atp. □
Theorem 7.33 yields a general topological decomposition of Hd(M,−∞),
which is a stratiﬁed version of Theorem 7.15.
Deﬁnition 7.34. A critical pointp in direction ˆr on a stratumS is called non-
degenerate if h ˆr|S is nondegenerate in the sense of Deﬁnition 7.11 (meaning
the Hessian for h ˆr|S in local coordinates aroundp is nonsingular).
7.3 The general case via stratiﬁed Morse theory 205
Theorem 7.35. Fix ˆr and assume there are no critical values at inﬁnity. Let
z1,..., zm enumerate the stratiﬁed critical points of V∗ in (weakly) decreas-
ing order of the height function h ˆr, where the stratum containingz j has com-
plex codimension kj. If all critical points are quadratically nondegenerate then
there are cycles γ1,...,γ m onV∗, along with a basis β j,1,...β j,s j for the k j-
homology of the normal Morse data, with the following properties.
(a) h ˆr achieves its maximum onγ j atz j;
(b) γ j≃ (Bd−k j,∂ Bd−k j);
(c) A basis for the integer homology group H d(M,−∞) can be formed by cy-
clesσ j,i =γ j×β j,i which, for ﬁxed j, form a basis for G (z j).
Proof Theorem 7.33 and part ( i) of Deﬁnition 7.32 imply ( a) and (b). Com-
paring parts ( v) and ( vi) of the deﬁnition with Theorem 7.30 gives ( c). The
fact that{σ j,i} is an integer homology basis follows from the lack of torsion in
Hd(M), which follows from the fact thatV∗ andM have the homotopy type of
a d-dimensional cell complex (see Theorem D.23), with no boundaries in di-
mension d. Because the Morse theoretic results identify the homotopy type of
the attachments, not just the relative homology groups, the cyclesσ j,i generate
homology with both integer and rational coeﬃcients. □
While this theorem may look somewhat abstract, its power lies in its gener-
ality, and typical applications can be simple. For instance, in Figure 7.19 we
have a surfaceV with complementM :=C2
∗\V where H2(M) has one gen-
erator local to a critical point in a stratum of complex dimension 0 and two
quasi-local to critical points in strata of dimension 1; the former has a 2-torus
for its normal link, while the latter have normal links of dimension 1 which
may be taken to be topological circles.
A further generalization removes the assumption of quadratic nondegener-
acy. We do not use this generalization in this text, as we directly compute
integral manipulations for the few quadratically degenerate cases that arise.
Corollary 7.36. Without the assumption of quadratic nondegeneracy of h ˆr at
each critical pointp, a modiﬁed version of Theorem 7.35 still holds. Instead of
a pair (B,∂ B) consisting of a ball and its boundary, the tangential Morse data
is replaced by a more general collection of (d− k j)-cycles{γ j,k : 1≤ k≤ r j}
where r j is the rank of H d−k j(V≤c,V≤c−ε). Consequently, the basis in part (d)
of Theorem 7.35 is instead formed by cycles γ j,k×β j,i for 1≤ j≤ m with
1≤ k≤ r j and 1≤ i≤ s j.
Exercise 7.11. LetM be a manifold of real dimensiond inRn for d< n. Many
classical Morse-theoretic analyses use the height function h(x) = d(p,x),
206 Overview of analytic methods for multivariate GFs
Figure 7.19 Critical points and their normal and tangential homology generators.
On the right are two index-1 smooth critical points with tangential relative ho-
mology generators γ and normal homology generators β≍ S 1. On the left is an
isolated self-intersection point γ ofV, thus a zero-dimensional stratum, pictured
with a two-dimensional normal link homotopy equivalent to (and in the picture
homeomorphic to) a 2-torus.
where d is distance and p is a ﬁxed point in Rn\M . Explain why this is not
a good Morse function to use if trying to establish the “bouquet of spheres”
result for smooth varieties – described before Theorem 7.15 above – via The-
orem 7.35(b).
