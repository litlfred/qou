---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-037-the-smooth-case
section_title: "The smooth case"
section_number: null
pages: 200-214
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
We now generalize the above argument to any rational function whose singular
variety V is a complex manifold. The square-free part ˜Q of the polynomial Q
is the product of its distinct irreducible factors over the complex numbers, and
we say that Q is square-free if ˜Q = Q. We call z ∈V a smooth point if ∇˜Q(z)
is non-zero, and say that V is smooth if ˜Q and all its partial derivatives never
simultaneously vanish. The implicit function theorem implies that a smooth
singular variety can be viewed both as a (d−1)-dimensional complex manifold
and as a (2d −2)-dimensional real manifold, and both of these viewpoints will
be beneﬁcial. We introduce the square-free part of Q so that the converse also
holds.
Lemma 7.6. The inequality ∇˜Q(z) , 0 holds for a point z ∈VQ if and only
if V is a smooth manifold in a neighborhood of z.
Proof Sketch
The forward implication follows from the implicit function the-
orem. The converse, that ∇˜Q(z) = 0 implies a geometric singularity, is harder
to prove. Let mx denote the maximal ideal of functions vanishing at x in the
ring of polynomial functions vanishing on V, and let nx denote the maximal
ideal of functions vanishing at x in the ring of germs of analytic functions at
x (as deﬁned in Deﬁnition 10.42 below). Then ∇˜Q(x) = 0 implies mx/m2
x
has dimension d rather than d −1 (see [Sha13, Exercise 2.2 and Theorem 2.1])
7.2 The smooth case
183
so that nx/n2
x has dimension d, and this property is invariant under bi-analytic
mapping. At any smooth point of a complex hypersurface there is a coordinate
neighborhood taking x to the origin and making the hypersurface into the coor-
dinate plane where z1 = 0. In this case n0/n2
0 has dimension d−1, which would
be a contradiction, hence V is not a complex manifold in a neighborhood of
x. A little more work shows V is not locally a C∞manifold either.
□
Our starting point, as always, is the multivariate Cauchy Integral Formula
ar =
 1
2πi
!d Z
T
z−r−1F(z) dz ,
(7.7)
which gives an exact representation for ar. We view this representation not as
a standard integral from multivariate calculus, but as the integral of the diﬀer-
ential form ω = z−r−1F(z) dz over the d-chain T. The necessary background
on diﬀerential geometry and the basics of integration of forms is discussed in
Appendix A. Appendix B reviews concepts from algebraic topology, including
homology and cohomology classes. In particular, since M = Cd
∗\ V is the do-
main of holomorphicity for ω, the Cauchy integral depends only on the class
of T in the singular homology group Hd(M) and the class of ω in the singular
cohomology group Hd(M).
We break our argument into pieces, generally mirroring the ﬁnal approach
to Example 7.3 above. In this chapter we mainly stick to theoretical consider-
ations; methods for computing the quantities that arise are discussed in Chap-
ter 8.
Step 1: Characterize critical points
We begin by deﬁning the height function
hr(z) := −r · Relog z = −
d
X
j=1
r j log |z j| ,
which captures the magnitude of the Cauchy integrand

z−r−1F(z)

 = e|r| h ˆr(z) ·

z−1F(z)

as

z−1F(z)

 independent of |r|. The ordering hr gives to Cd
∗does not change if
r is multiplied by a positive scalar, so our arguments about the height function
will hold whenever r is replaced by any positive multiple. This invariance
property means that an analysis of ar as r →∞with ˆr = r/|r| converging to
some ﬁxed ˆr∗can usually be accomplished with the ﬁxed height function h ˆr∗.
In particular, if ˆr∗is a ﬁxed direction and hr∗(x) < hr∗(y) then, as r →∞with
ˆr →r∗, the Cauchy integrand is exponentially smaller at z = x than at z = y.
When r is understood we write simply h for hr.
184
Overview of analytic methods for multivariate GFs
Deﬁnition 7.7. A smooth critical point z of the rational function F = P/Q in
the direction ˆr is a smooth point of V∗that is a critical point of h ˆr : V∗→R as
a smooth mapping of real manifolds. The set of critical points in the direction
ˆr is denoted by critical(r).
The height function h ˆr is the real part of (a branch of) the analytic function
φ(z) = −r · log z, and the Cauchy–Riemann equations imply that the critical
points of F in the direction ˆr can also be computed as the critical points of
φ : V∗→C as a (locally) holomorphic mapping of complex manifolds. In
particular, we have the following explicit deﬁnition of smooth critical points.
Lemma 7.8. Assume that V is a smooth manifold and let ˜Q be the square-free
part of the denominator Q. Then w ∈Cd
∗is a critical point in the direction ˆr if
and only if it satisﬁes the smooth critical point equations
˜Q(w) = rkw1 ˜Qz1(w) −r1wk ˜Qzk(w) = 0
(2 ≤k ≤d) ,
(7.8)
where ˜Qzj denotes the derivative of ˜Q with respect to the variable z j.
Proof
The point w is a critical point when Q(w) = 0 and the diﬀerential of
φ : V∗→C is zero. Vanishing of this diﬀerential occurs exactly when the
diﬀerential of φ as a map from Cd
∗to C projects to zero on the tangent space
of V∗at w. Since the tangent space to V∗at w is the hyperplane with normal
(∇˜Q)(w), the diﬀerential of φ projects to zero if and only if (∇φ)(w) is parallel
to (∇˜Q)(w). These vectors are parallel if and only if all 2 × 2 minors of the
matrix


∇˜Q

(w)
(∇φ) (w)
=
 ˜Qz1(w)
· · ·
˜Qzd(w)
−r1/w1
· · ·
−rd/wd
!
vanish. Vanishing of the minors simpliﬁes to give the smooth critical point
equations.
□
Remark 7.9. The smooth critical point equations (7.8) form a polynomial
system with d equations in d variables. It is therefore unsurprising that gener-
ically Q has a ﬁnite number of critical points (i.e., this holds for all polyno-
mials Q except for those whose coeﬃcients come from a ﬁxed algebraic set
depending only on the degree of Q). This follows directly from an algebraic
version of Sard’s Theorem, which can be found in [BPR03, Theorem 5.56];
see also [Mel21, Section 5.3.4] for an explicit derivation.
Exercise 7.4. Continuing Exercise 7.3, let r = (2, 1) and ﬁnd the critical points
for hr on V. Compute the heights of these critical points and compare them
to the limit height for the sequence approaching inﬁnity in Exercise 7.3. Is the
limit height larger than the heights of all critical points on V?
7.2 The smooth case 185

Proposition 7.10. Singularity of the Hessian matrix for h; in local coordinates
at a critical point for hs on the smooth variety V,, is independent of the choice
of coordinatization of V, as a complex manifold.

Proof Ata point p where V hp vanishes, the chain rule under a coordinate
change simplifies to H’ = JyH, where H’ is the new Hessian, H is the
old Hessian, and Jy is the Jacobian matrix of ‘Y at p. The claim follows from
nonsingularity of Jy at p. a

Definition 7.11. A smooth critical point w of h is called nondegenerate if the
Hessian matrix for / in local coordinates around w is nonsingular.

This definition is generalized to non-smooth points in Definition 7.34 below.
Under our assumption that V is smooth, one of the partial derivatives of the
square-free part of Q is nonvanishing at w. Without loss of generality, we
assume that 0., (w) # 0 is non-zero, so we can parametrize V near w as zy =
g(z°) = g(z1,...,Za-1) for some analytic function g defined in a neighborhood
of w°. The critical point w is nondegenerate if and only if the Hessian matrix
of h(z°, g(z°)) with respect to z1,...,Zg-1 has non-zero determinant at z° =
w*. We say h is a Morse height function when all of its critical points are
nondegenerate.

Remark. Most topological works, such as [Mil63; GM88], study spaces using
Morse height functions. However, as discussed in Appendix C, as long as there
are finitely many critical points the basic Morse decompositions hold whether
or not / is Morse: the topology of the space is still generated by attachments at
the critical points. However, the description of the attachments becomes more
complicated for non-Morse height functions.

Step 2: Intersect the torus with the singular variety

The Cauchy integral representation (7.7) holds for any torus T = Relog™!(a)
with x in the component B of amoeba(Q)° corresponding to the convergent
Laurent expansion with coefficients a,. We want to replace the domain of in-
tegration T with a domain of integration close to ‘V that “wraps around” the
singular variety, so we can use a residue computation in Step 3 below to reduce
to an integral “on” V.

If y is any (d — 1)-chain in ‘V,, then the Collar Lemma (Lemma C.1 in Ap-
pendix C) shows how to construct the tube oy around y, which is a d-chain
in the domain M where the Cauchy integral w is holomorphic. The tube oy
can be viewed as a union of circles with centers at the points of y, and the
186
Overview of analytic methods for multivariate GFs
map γ 7→oγ is well deﬁned as a map from the homology group Hd−1(V∗) to
Hd(M).
Theorem C.2 of Appendix C implies that o : Hd−1(V∗) →Hd(M) is injec-
tive, and if T ′ is any torus contained in M then pulling back [T −T ′] ∈Hd(M)
via o gives a well-deﬁned class INT(T, T ′) ∈Hd−1(V∗) known as the intersec-
tion class of T and T ′. By construction, [T] −[T ′] = o INT(T, T ′) in Hd(M),
so that
ar =
 1
2πi
!d Z
T
ω =
 1
2πi
!d Z
o INT(T,T ′)
ω +
 1
2πi
!d Z
T ′ ω .
One can picture o INT(T, T ′) by imagining a continuous deformation of T to
T ′. If this deformation is suﬃciently generic it will intersect V∗transversely,
with the intersection yielding INT(T, T ′). The tube around INT(T, T ′) is thus
the chain that needs to be added to account for passing the deformation through
V∗. See Figure 7.7 for an illustration.
Figure 7.7 An intersection class of T and T ′ with respect to V.
If we pick a torus T ′ so that
R
T ′ ω = 0 then we have succeeded in expressing
the Cauchy integral as an integral over a tube around a curve in V∗. Corol-
lary 6.29 implies the existence of such a torus, giving the following.
Proposition 7.12. Assume F is the ratio of coprime polynomials F(z) =
P(z)/Q(z). As r →∞in the direction ˆr there exists a torus T ′ such that
7.2 The smooth case
187
R
T ′ ω = 0 for all but ﬁnitely many r, and
ar =
 1
2πi
!d Z
o INT(T,T ′)
ω
(7.9)
whenever the integral over T ′ is zero.
□
Exercise 7.5. Let Q(x, y) = 1 −x −y −x2y2, whose amoeba is shown in
Figure 7.8. When r = (1, 1), which components of amoeba(Q)c have hr un-
bounded from below, and which vertices of the Newton polygon for Q do these
regions correspond to under the relationship described in Theorem 6.18?
Figure 7.8 Amoeba of Q(x, y) = 1 −x −y −x2y2.
We can convert the d-dimensional integral in (7.12) to a (d −1)-dimensional
integral over the intersection cycle, which lies in V∗. This is accomplished
using the concept of multivariate residues (also called Leray residues). Ap-
pendix C.2 gives a summary of multivariate residues, but for this discussion
it is suﬃcient to note that the residue form Res(τ) of a meromorphic d-form τ
with singularities contained in V is a (d−1) form restricted to V. Theorem C.9
implies that
1
2πi
Z
oγ
τ =
Z
γ
Res(τ)
for any (d −1)-chain γ in V∗and holomorphic d-form τ on M.
In particular, combining the residue operator with Proposition 7.12 gives the
following.
188
Overview of analytic methods for multivariate GFs
Proposition 7.13. If T ′ is a torus described by Proposition 7.12 then
ar =
 1
2πi
!d−1 Z
INT(T,T ′)
Res ω.
(7.10)
□
Exercise 7.6. Suppose d = 1 and V = VQ where Q(z) = 2 −3z + z2. Let T be
a circle of some small positive radius ε and T ′ be a circle of some large radius
M.
(a) What is the cycle INT(T, T ′)?
(b) What is the form Res(ω) when ω = Q(z)−1z−n−1dz?
(c) What is
R
INT(T,T ′) Res(ω)?
(d) What is o INT(T, T ′)?
(e) Describe in words why o INT(T, T ′) is homologous to T−T ′ in H1(C∗\V).
Step 3: Determine a Morse-Theoretic Decomposition of the
Singular Variety
Having reduced the Cauchy integral to an integral over an intersection cycle
γ = INT(T, T ′) lying in the singular variety V∗, we now want to deform γ in
V∗to represent the coeﬃcient sequence of interest as a sum of saddle point in-
tegrals. Because we are currently assuming V is smooth, we could try to com-
pute such a representation by taking a gradient ﬂow of γ on V with respect to
the height function h ˆr. If γ can be deformed so that it lies in the neighborhood
of a nondegenerate critical point σ of h ˆr, except for points of height at most
σ −ε for some ε > 0, then we can apply the saddle point techniques of Chap-
ter 5 to compute asymptotics (up to an exponentially negligible error, coming
from ignoring points of lower height).
Actually computing such a gradient ﬂow on real examples is usually not
feasible. Fortunately, one of the most important consequences of Morse theory
is that under reasonable conditions there are only a ﬁnite number of possi-
bilities for the long-term behavior of such a ﬂow. In particular, as detailed in
Appendix C and summarized here, if the ﬂow does not stay at bounded height
while escaping to inﬁnity on V∗then we can ﬂow γ until it gets locally “stuck”
on one of the critical points of h ˆr.
Our results are phrased in the language of singular homology, reviewed
in Appendix B. Of particular use to us are the notions of relative homology,
which allows us to discuss homology near a critical point while ignoring points
7.2 The smooth case
189
Figure 7.9 The curve γ is deformed to a curve γz locally draped over a saddle z
centered at a critical point for the height function. The tubes around γ and γz are
also pictured.
of lower height that do not aﬀect dominant asymptotic behavior, and attach-
ments, which describe how to decompose the singular variety by joining to-
gether topologically simpler spaces. Our discussion here summarizes the main
points of the machinery developed in the appendices before applying them to
our situation.
Morse theory represents the topology of a manifold X equipped with a
smooth map h : X →R in terms of successive attachments. The smooth func-
tion h is referred to as a height function on X. As discussed above, we say h
is a Morse if its critical points are nondegenerate, and proper if the inverse
image of any closed interval is compact. Let X≤c denote the subspace of all
points z ∈X with h(z) ≤c and suppose that h is a proper Morse function. As
described in Section C.3 of Appendix C, Morse theory describes the change
in topology when the space X≤a is increased to X≤b using the language of at-
tachments. Moving from X≤a to X≤b is a homotopy equivalence (no change in
topology) unless h has critical values in [a, b]. When there is a single critical
point z with height in this interval, the topology changes via a topological at-
tachment: X≤b is homotopy equivalent to X≤a on which a λ-ball B is glued via
an attaching map φ : ∂B →X≤a. The value of λ is the Morse index of the criti-
cal point z, which can be thought of as the dimension of the downward facing
part of the generalized saddle at z and computed in local coordinates using the
Hessian of h at z.
Figure C.3 in Appendix C shows how the decapitated unit sphere S ≤1−ε be-
comes the full unit sphere by the attachment of a cap and the north pole (Morse
index 2), while Figure C.5 in Appendix C shows how a contractible patch near
190
Overview of analytic methods for multivariate GFs
the bottom of a torus becomes homotopy equivalent to a circle when a bridge
(homotopy equivalent to an arc) is added at the ﬁrst Morse index-1 critical
point. These diagrams are reproduced here in Figure 7.10 for convenience.
Figure 7.10 Two examples of attachments.
We now specialize to the case where X = V∗and h = h ˆr for some ﬁxed
unit vector ˆr. It is not true that h will always be proper, however we can work
around this diﬃculty. If σ ∈V∗is a critical point then the gradient (∇h ˆr)(σ)
projects to zero on the tangent plane TσV∗⊂Cd. Roughly speaking, a critical
point at inﬁnity is a sequence of points z(k) ∈V∗going oﬀto inﬁnity such
that the projection of (∇h ˆr)(z(k)) to Tz(k)V∗approaches zero as k →∞; the
associated critical value at inﬁnity is the limit of h ˆr(z(k)) as k →∞. Critical
points at inﬁnity are deﬁned formally in Deﬁnition 7.42 below. Provided there
are no critical points at inﬁnity, the classic results of Morse theory hold even
when the height function is not proper.
Lemma 7.14. Suppose h ˆr has no critical values at inﬁnity in the interval [a, b].
If there are no critical values in [a, b] then the inclusion X≤a ⊆X≤b is a ho-
motopy equivalence. If there is a single critical point z with critical value
h ˆr(z) = c ∈(a, b), then the pair (V≤b, V≤a) is homotopy equivalent to a λ-cell
relative to its boundary, where λ is the Morse index of the critical point z for
h ˆr.
Exercise 7.7. What is λ in the attachment in the bottom row of Figure 7.10?
It is convenient to postpone the proof of Lemma 7.14 until the more general
setting when we no longer require V to be smooth. After establishing addi-
tional results below, Lemma 7.14 follows directly from Lemma 7.25, which
asserts the homotopy equivalence, and the identiﬁcation of the attachment in
7.2 The smooth case 191

Theorem 7.35(b). In the present smooth case, a nice simplification occurs: be-
cause the height function is the real part of a complex (locally) analytic func-
tion, every critical point z ¢ V, has Morse index d — 1.

Exercise 7.8. Prove that the real part of a complex analytic function defined
on an open set in Cé has Morse index d, then prove that the real part of such a
function restricted to a smooth hypersurface has Morse index d— 1. Hint: The
Cauchy—Riemann equations yield a lot of information about the eigenvectors
and eigenvalues of the Hessian.

This characterization of the index allows us to show that Hg_\(V..) is homo-
logically a bouquet of (d — 1)-spheres, one quasi-local to each critical point. A
version of the following theorem, with the stronger assumption that h is proper
replacing the assumption of no CVAI, is stated and proved as Theorem C.39
in Appendix C (the appendices contain background material not specialized
to ACSV). The restriction that the critical values are distinct is removed in
Corollary 7.17.

Theorem 7.15. Assume that V is smooth, hp is a Morse height function, and
there are no critical values at infinity (according to Definition 7.43 below).
Assume further that the critical values cj = hp(z;) are distinct and listed in
descending order.

(i) Each projection Ha_-\(Vx) > Ha-1(Vecj+esV <e)-e) is surjective. In other
words, the relative homology generator at z; can be chosen to be an
absolute cycle.

(ii) Each inclusion Vz. © V. induces an injection on Hy-). In other words,
there are no relations: no homology generator ever gets killed.

It follows that Ha-\(V.) = Z” and that a basis y1,..., Ym for Ha-1(V+) can be
chosen so that each y; is a cycle on which hg attains its maximum value at Z;.

Proof Part (i) of Theorem 7.44 below extends the fundamental Morse Lemma,
namely homotopy equivalence of M<, as c varies in an interval with no critical
values (Lemma C.27) from the case where / is a proper Morse function to the
case where / need not be proper but there are no CVAI in the interval. Part (ii)
of Theorem 7.44 extends the smooth attachment theorem for a single critical
value c (Theorem C.28) from the case where h is a proper Morse function to
the case where / need not be proper but there are no CVAI in the interval.
Accordingly, the conclusions of Theorems C.38 and C.39 hold for this case,
via the same argument. Specifically, these follow from the identification of the
attachment and from the homology long exact sequence for the filtration of
pairs (Map, —oo), where b; are real numbers between each successive pair of
192
Overview of analytic methods for multivariate GFs
critical values, b0 is above the highest critical value, and −∞is Mb for any b
less than the least critical value. See Section C.4 for details.
□
Remark 7.16. The isomorphism Hd−1(V∗) 
Lm
j=1 Hd−1(Vcj+ε, Vcj−ε) is not
natural. For each attachment at z j there is an arbitrary choice of an absolute
cycle γ j that projects to the generator of the homology group for the attach-
ment. The cycle γ j + α would do equally well for any cycle α supported on
Vcj−ε. One might say that the choice of γ1, . . . , γm, listed in decreasing order
of height, can be altered by an arbitrary upper triangular map, replacing γj
by γ j + P
i>j biγi. This is the so-called Stokes phenomenon, illustrated in Fig-
ure 7.11: the saddle point integral from z j might pass on either side of zi as it
travels downward, with the integrals over the two choices of contour diﬀering
by the integral over γi. Thus, for a cycle C the decomposition [C] = Pm
k=1 nkγk
is not natural. It is important to note, however, that the leading coeﬃcient nj∗is
well-deﬁned independent of the chosen basis {γj}, where j∗is the least index
such that nj∗, 0.
Figure 7.11 Stokes’s phenomenon reﬂects the fact that a curve draped over the
higher saddle can descend on either side of the lower saddle, as shown here by
two possible branches. The diﬀerence between these two curves is a curve draped
over the lower saddle.
The simplifying assumption of distinct critical values is not important. To
get rid of this, we deﬁne the local homology pair Vp,loc at a critical point p at
height c to be the pair (X, Y), where Y = V≤c−ε/2 and X is the union of Y with
the ball Bε(p) for ε > 0 suﬃciently small (see Deﬁnition C.31 of Appendix C
for full details). Any such pairs are homotopy equivalent as long as ε is small
enough that the 2ε-balls about diﬀerent critical points are disjoint.
Deformations deﬁned in Appendix C show that if there is a unique critical
point p with height c ∈[a, b] then, for small ε > 0, the local pair Vp,loc is
homotopy equivalent to the slab (V≤c+ε, Vc−ε). The beneﬁt to replacing the
slab by the local pair occurs when there are multiple critical points sharing a
7.2 The smooth case
193
critical value. If h ˆr(p) = c for all p in some ﬁnite set E then
(V≤b, V≤a) ≃
M
p∈E
Vp,loc,
(C.3.1)
giving the following.
Corollary 7.17. Replacing (Vcj+ε, Vc j−ε) by Vz,loc for each z, the conclu-
sions of Theorem 7.15 hold without the assumption of distinct critical values.
□
We end this subsection with some examples of this topological decomposi-
tion.
Example 7.18 (binomial coeﬃcients). Recall that the binomial coeﬃcients
ars =
r+s
r

have bivariate generating function F(x, y) = 1/(1−x−y). If ˆr = (r, s)
with r + s = 1 and r, s ∈(0, 1) then as r varies from 0 to 1, the critical point
w( ˆr) of F in the direction ˆr slides from (0, 1) to (1, 0). The homology group
H1(V∗) has a single generator γz∗. The homology group H2(M) is cyclic as
well, generated by oγz∗.
◁
Example 7.19 (Delannoy numbers). The Delannoy number generating func-
tion from Example 2.7 in Chapter 2 is 1/(1−x−y−xy). The situation is similar
to Example 7.18, except that as r varies from 0 to 1 the critical point w( ˆr) tra-
verses the arc the other way from (0, 1) to (1, 0), and there is another critical
point w′ traversing a hyperbola in the third quadrant.
◁
Exercise 7.9. Consider the amoeba of the denominator Q(x, y) = 1−x−y−xy
of the Delannoy generating function, shown in Figure 7.12.
(a) Compute the critical points w and w′ in the direction determined by r =
(2, 3), then draw dots where p = Relog(w) and p′ = Relog(w′) lie on the
amoeba.
(b) Find a path β, from the power series component of the amoeba complement
to a component where the Cauchy integral is zero, that enters the amoeba
at p and exits it at p′.
(c) Describe γ = Relog−1(β).
(d) State why [γ] = INT(T, T ′) in H1(V∗) and why
R
γ Res ω is easy to esti-
mate, where
ω = x−2n−1y−3n−1
1 −x −y −xydx ∧dy .
194
Overview of analytic methods for multivariate GFs
Figure 7.12 Amoeba for the Delannoy generating function Q(x, y) = 1−x−y−xy.
Each point interior to the amoeba is the image of precisely two points of V under
Relog.
Result: a saddle point integral decomposition in the smooth case
Theorem 7.15 and Corollary 7.17 give a basis of Hd−1(V∗) consisting of cycles
that attain their maximum values at critical points. Vanishing of dh ˆr|V at z
is equivalent to z−r being in stationary phase at z for any (d −1)-chain γj
supported on V∗. Thus, combining Theorem 7.15 and Corollary 7.17 with the
integral representation in Proposition 7.13 gives the following, our ultimate
goal for generating functions with smooth singular varieties.
Theorem 7.20 (smooth saddle point integral decomposition). Assume that V
is smooth, h ˆr is a Morse height function, and that there are no critical values
at inﬁnity (see Deﬁnition 7.43 below). Assume further that the critical values
cj = h ˆr(z j) for 1 ≤j ≤m are listed in descending order. Then there exist
integers κ j ∈Z and smooth chains of integration γj with heights uniquely
maximized at z j, such that
ar =
m
X
j=1
κj
(2πi)d−1
Z
γ j
z−r−1 Res(F(z) dz) .
(7.11)
The integral in the jth summand is in stationary phase at z j. The least j such
that κ j , 0, and the homology class P
j′∈E κ j′γj′ for all j′ such that z j′ has
height c j, are uniquely deﬁned.
□
There are two important tasks remaining: computing asymptotics of the sad-
dle point integrals and determining the integers κj. While integral asymptotics
(in this smooth case) follow in a straightforward manner from the results of
Chapter 5, it can be very diﬃcult to determine these unknown integers. We
7.2 The smooth case
195
discuss both of these questions in Chapter 9, where we derive explicit asymp-
totic formulae for ar in terms of the generating function F(z). Readers who
are interested only in smooth asymptotics (and do not need to see the technical
discussion of critical points at inﬁnity) may go directly to Chapters 8 and 9,
after a brief discussion about removing our simplifying hypotheses.
The requirement of no critical value at inﬁnity is essential: when there are
critical points at inﬁnity, asymptotics are in principle aﬀected. Classifying
these cases and computing the asymptotics remains an open problem discussed
further in Chapter 13. Removing the smoothness assumption involves the ap-
paratus of stratiﬁed Morse theory, which we make use of in the next section.
The assumption that h ˆr is nondegenerate is not essential, however in its ab-
sence there is no longer a unique cycle γ j for each j. We handle this case, for
now, by two examples.
Example 7.21 (cubic degeneracy). The simplest degeneracy at a critical point,
a so-called monkey saddle, leads to two independent homology generators as
in Figure 7.13.
◁
Figure 7.13 Two homology generators associated with a monkey saddle.
196
Overview of analytic methods for multivariate GFs
While critical points are generically nondegenerate, we now give one com-
binatorial example in which a critical point w is indeed degenerate and con-
tributes more than one generator.
Example 7.22 (bi-colored supertrees). Example 9.32 in Chapter 9 looks at
a rational generating function counting bi-colored supertrees (certain planar
binary trees that need not concern us here). The singular variety is the smooth
surface deﬁned by the vanishing of Q(x, y) = x5y2 + 2x2y −2x3y + 4y + x −2.
When ˆr = (1/2, 1/2) then there are two nondegenerate critical points, u and v,
together with a critical point w near which h ˆr is quartic (so doubly degenerate).
Accordingly there is one cycle γu, one cycle γv, and three cycles γ(j)
w which
may be conﬁgured all to enter w along the solid arc and exit along one of the
three dashed arcs shown in Figure 7.14.
◁
Figure 7.14 The supertree generating function yields two nondegenerate critical
points and one doubly degenerate critical point.
