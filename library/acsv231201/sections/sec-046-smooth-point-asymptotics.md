---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-046-smooth-point-asymptotics
section_title: "Smooth point asymptotics"
section_number: null
pages: 263-271
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
Smooth point asymptotics
After discussing the overall framework of ACSV in Chapter 7, and the com-
putational tools needed to carry out the analysis in Chapter 8, we are now
ready to prove asymptotic theorems. As usual, we begin with a convergent
Laurent expansion F(z) = P
r∈Zd arzr in some domain D ⊂Cd and try to
determine asymptotic behavior of ar as r →∞with the normalized vector
ˆr =
r
|r| =
r
|r1|+···+|rd| restricted to compact sets. In this chapter we give results
when dominant asymptotic behavior is determined by the local behavior of F
near a ﬁnite set of points where its set of singularities V forms a manifold.
Typically we assume F is rational, although we also state results when F is
meromorphic.
Remark 9.1. The smoothness assumption of this chapter is generic, meaning
(for instance) that it holds for all rational functions except for those whose co-
eﬃcients lie in a ﬁxed proper algebraic set depending only on the degree of the
denominator. Although this might suggest that every example encountered in
practice is handled by the techniques of this chapter, non-generic behavior does
occur in many combinatorial applications. Nonetheless, a large fraction of the
multivariate generating functions encountered by the authors can be handled
by the techniques presented here, without going into the more general theory
of Chapters 10 and 11.
The Main Results of Smooth ACSV
We begin by stating the main theorems of this chapter. Let F(z) = P(z)/Q(z)
be the ratio of coprime polynomials, where Q ∈C[z] has square-free part
˜Q (equal to the product of its distinct irreducible factors). Recall from past
chapters that w ∈Cd
∗is a smooth critical point for the direction ˆr ∈Rd if and
only if (∇˜Q)(w) , 0 and
˜Q(w) = ˆriwd ˜Qzd(w) −ˆrdwi ˜Qzi(w) = 0
(1 ≤i ≤d −1).
(9.1)
245
246
Smooth point asymptotics
The case when the direction vector ˆr is the zero vector is trivial, so we
always assume that ˆr has a non-zero coordinate. When the series expansion
of F under consideration is a power series we can further assume the stronger
condition that ˆr has no zero coordinates, because asking for terms where (say)
rd = 0 corresponds to extracting terms from the (d −1)-variate series obtained
by setting zd = 0. In this case, because our results hold only for critical points
with non-zero coordinates, the smooth critical point equations imply that none
of the partial derivatives of ˜Q vanish.
For Laurent expansions, on the other hand, there are combinatorially inter-
esting cases where ˆr has zero coordinates. Even so, if there are to be smooth
critical points with non-zero coordinates then the critical point equations imply
the existence of a coordinate k such that rk , 0 and ˜Qzk(w) , 0. Without loss
of generality, we may assume this coordinate k is the ﬁnal coordinate d.
Consider a Laurent expansion of F with domain of convergence D. Theo-
rem 6.44 from Chapter 6 implies that if w is a smooth minimal critical point
(see Deﬁnition 7.7) for the direction ˆr then the hyperplane with normal ˆr going
through the point Relog(w) is a support hyperplane to B = Relog(D).
Deﬁnition 9.2 (contributing and nondegenerate points). The smooth minimal
critical point w described above is called a contributing point for the direction
ˆr if ˆr points away from B at Relog(w), meaning x · ˆr < Relog(w) · ˆr for
all x ∈B. The point w is nondegenerate if the Hessian matrix H deﬁned by
Lemma 8.22 in Chapter 8 is nonsingular with H = ˜Q.
Remark 9.3. If we consider the power series expansion of F(z), where ˆr has
positive coordinates, then every smooth minimal critical point is contributing.
This deﬁnition of nondegeneracy is equivalent to our previous deﬁnitions in
terms of the Hessian of the height function h(z) = −r · log z restricted to V.
Deﬁnition 9.2 is constructed so that contributing points are minimizers of the
height function h ˆr on D, which turn out to be the points determining asymp-
totic behavior. Conversely, non-contributing smooth minimal critical points are
maximizers of h ˆr on D; see Figure 9.1.
Exercise 9.1. Which of the components of the complement of the amoeba in
Figure 9.1 have a contributing point in the direction (1, −1)?
We break our main result into three versions, depending on the assumptions
required and the proof techniques used. Our ﬁrst version is the most restric-
tive, however it still holds in a wide variety of applications and has the ad-
vantage that it can be derived purely through complex analysis and classical
saddle point techniques, without the need for the homological framework of
Smooth point asymptotics
247
Figure 9.1 The amoeba complement component B1, corresponding to a power
series expansion, has one point on its boundary where its support hyperplane has
normal r = (1, 1), which corresponds to contributing points. On the other hand,
the component B2 has two boundary points with support hyperplanes having nor-
mals r = (1, 1), only one of which (the upper-most one) corresponds to contribut-
ing singularities.
Chapter 7. In order to simplify our presentation, we begin by stating it in the
common special case where Q is square-free and there is a single minimal
contributing point.
Theorem 9.4 (Main Theorem of Smooth ACSV (Local Version, Square-Free
Case)). Let F(z) = P(z)/Q(z) be the ratio of coprime polynomials P and Q
with convergent Laurent expansion F(z) = P
r∈Zd arzr. Suppose that there is
a compact set R ⊂Rd of non-zero directions such that if ˆr lies in R then F has
a smooth strictly minimal nondegenerate contributing point w = w( ˆr) ∈Cd
∗,
and let H = H( ˆr) be the Hessian matrix deﬁned by (8.7) and (8.8) when
H = Q. If Qzd(w) , 0 then
ar ≈Φw(r)
uniformly as r →∞with ˆr ∈R, where Φw(r) is an asymptotic series
Φw(r) = w−r|rd|(1−d)/2 (2π)(1−d)/2 sgn(rd)
p
det(sgn(rd) H)
∞
X
ℓ=0
Cℓ( ˆr)r−ℓ
d .
(9.2)
The square-root of the matrix determinant is the product of the principal branch
square-roots of its eigenvalues (which will have nonnegative real parts). The
248
Smooth point asymptotics
constants Cℓare explicitly computable in terms of the derivatives of P(z) and
Q(z) evaluated at z = w( ˆr). In particular,
C0 =
P(w)
−wdQd(w).
(9.3)
□
Theorem 9.4 is a special case of the following, which holds for poles of
general order.
Theorem 9.5 (Main Theorem of Smooth ACSV (Local Version)). Let F(z) =
P(z)/Q(z) be the ratio of coprime polynomials with convergent Laurent ex-
pansion F(z) = P
r∈Zd arzr. Suppose there exists a compact set R ⊂Rd of
non-zero directions such that if ˆr lies in R then F has a smooth strictly mini-
mal nondegenerate contributing point w = w( ˆr) ∈Cd
∗, and let H = H( ˆr) be
the Hessian matrix deﬁned by (8.7) and (8.8) when H = ˜Q. If (∂p
dQ)(w) , 0
and (∂q
dQ)(w) = 0 for all 0 ≤q < p then
ar ≈Φw(r)
uniformly as r →∞with ˆr ∈R, where Φw(r) is an asymptotic series
Φw(r) = w−r|rd|p−1+(1−d)/2 (2π)(1−d)/2 sgn(rd)p
p
det(sgn(rd) H)
∞
X
ℓ=0
Cℓ( ˆr)r−ℓ
d .
(9.4)
The square-root of the matrix determinant is the product of the principal branch
square-roots of its eigenvalues (which will have nonnegative real parts). The
constants Cℓare explicitly computable in terms of the derivatives of P(z) and
Q(z) evaluated at z = w( ˆr). In particular,
C0 = (−1)pP(w)p
wp
d(∂p
dQ)(w).
If w is a ﬁnitely minimal point (instead of being strictly minimal) such that
all points in the set W( ˆr) = T(w) ∩V vary smoothly with ˆr in R and are
contributing points satisfying the conditions above then
ar ≈
X
y∈W( ˆr)
Φy(r),
where each Φy is given by (9.4).
Exercise 9.2. What, in general, can go wrong pulling a factor of sgn(rd)d−1
out of the square-root in the denominator of (9.4)?
Smooth point asymptotics
249
Remark 9.6. An explicit (but unwieldy) formula for all coeﬃcients in (9.4)
is given in Section 9.4 below. If Q = Hp for some square-free H with ∇H
nonvanishing at w then
C0 =
(−1)pP(w)
(p −1)! (wd∂dH(w))p .
Remark 9.7. Our surgery approach below singles out the coordinate zd for a
residue computation, leading to an asymptotic expansion in powers of the non-
zero coordinate rd. With some extra work, the Fourier–Laplace integral used to
deduce asymptotics can be modiﬁed to provide an asymptotic series in powers
of |r|, giving an expansion of the form
Φw(r) = w−r
1
p
det(2π|r| H′)
∞
X
ℓ=0
C′
ℓ( ˆr)|r|−ℓ
(9.5)
for a new Hessian matrix H′. We leave details of such symmetric formulae to
Chapter 10, where asymptotics are computed using multivariate residue forms
that do not privilege individual coordinates.
Remark 9.8. If R = {s} contains a single point with sd > 0 then r = ns and
Φw(ns) ≈w−ns np−1+(1−d)/2 (2π)(1−d)/2
p
det(H)
∞
X
ℓ=0
Dℓn−ℓ
for constants Dℓwith D0 = (sd)p−dC0.
Example 9.9. The hypotheses of Theorem 9.5 can be simpliﬁed for bivariate
power series. In particular, suppose that F(x, y) = P(x,y)
Q(x,y) = P
i, j≥0 ai jxiyj admits
a strictly minimal critical point w = w(r) ∈C2
∗that varies smoothly as ˆr varies
in a compact neighborhood R of directions. If both P(x, y) and the expression
Q(x, y) = −xy2Q2
yQx −x2yQyQx −x2y2(Q2
yQxx + Q2
xQyy −2QxQyQxy) (9.6)
are non-zero when (x, y) = w( ˆr) for each ˆr ∈R then
ar,s ∼P(x, y)
−yQy
1
√
2π
x−ry−s
s
(−yQy)3
sQ
= P(x, y)
−xQx
1
√
2π
x−ry−s
s
(−xQx)3
rQ
(9.7)
as |r| →∞after setting (x, y) = w( ˆr), uniformly over ˆr ∈R.
◁
Exercise 9.3. Prove (9.7) by simplifying (9.2) in the bivariate case.
250
Smooth point asymptotics
Example 9.10 (binomial coeﬃcients continued). If F(x, y) = 1/(1−x−y) then
the coeﬃcient of xrys in the power series expansion of F is
r+s
s

. Solving the
smooth critical point equations yields the unique critical point
w =

r
r + s,
s
r + s

= (ˆr, ˆs) ,
which is strictly minimal by Lemma 6.41. We obtain
 r + s
s
!
∼(r + s)r+s
rrss
r
r + s
2πrs
as r, s →∞with r/s bounded away from zero and inﬁnity. For example, the
central binomial coeﬃcients given by r = s = n satisfy
2n
n

∼4n/ √πn.
◁
Example 9.11 (Delannoy numbers continued). If F(x, y) = 1/(1 −x −y −xy)
then we have the critical points
(x∗, y∗) =

√
r2 + s2 −s
r
,
√
r2 + s2 −r
s
or

−
√
r2 + s2 −s
r
, −
√
r2 + s2 −r
s
,
the ﬁrst of which is strictly minimal by Lemma 6.41. Writing d =
√
r2 + s2,
we directly compute
ars ∼

r
d −s
r 
s
d −r
s
s
rs (d2 + (r −s))
2π (r + s −d)  d2 + d(r −s)
as r, s →∞with r/s bounded away from zero and inﬁnity.
◁
We give a proof of Theorem 9.5 in Section 9.1 using the surgery method for
ACSV, which works in the presence of smooth ﬁnitely minimal contributing
points. Although the requirement of ﬁnite minimality makes proofs simpler, it
is computationally diﬃcult to check, and rules out cases that can be handled by
our other results. In Section 9.2 we use more advanced techniques (including
the theory of hyperbolic polynomials developed in Chapter 11) to prove an
extension of Theorem 9.5 that ignores non-critical points and only requires
that the torus T(w) contains a ﬁnite number of critical points. This gives a
large computational advantage, because generically there are a ﬁnite number
of critical points described by a zero-dimensional algebraic set.
Theorem 9.12 (Main Theorem of Smooth ACSV (Minimal Point Version)).
Let F(z) = P(z)/Q(z) be the ratio of coprime polynomials with convergent
Laurent expansion F(z) = P
r∈Zd arzr. Suppose there exists a compact set R ⊂
Rd of non-zero directions such that F has a smooth minimal nondegenerate
contributing point w = w( ˆr) ∈Cd
∗whenever ˆr ∈R. If the set W( ˆr) of solutions
Smooth point asymptotics
251
to (9.1) with the same coordinatewise modulus as w( ˆr) is ﬁnite and contains
only smooth nondegenerate contributing points that vary smoothly with ˆr then
ar ≈
X
y∈W( ˆr)
Φy(r),
(9.8)
uniformly as r →∞with ˆr ∈R, where Φy is deﬁned in (9.4).
Example 9.13 (negative binomial coeﬃcients). If F(x, y) = −x/(1−x−y) then
the coeﬃcient of x−rys in the Laurent series expansion of F converging in the
domain 1 + |y| < |x| is (−1)sr
s

. There is a unique critical point
w =

−r
−r + s,
s
−r + s

,
where now, because r > s, the ﬁrst coordinate of w is positive while the sec-
ond is negative. This point is minimal, since it lives on the boundary {(x, y) ∈
C2 : 1 + |y| = |x|} of the domain of convergence of this Laurent series, and
contributing. Ultimately, we obtain
[x−rys]F ∼(−1)s
rr
(r −s)r−sss
r
r
2π(r −s)s.
Note that if we replace x by 1/x in F, we obtain G = 1/(1 −x + xy), whose
(r, s)-coeﬃcient is (−1)sr
s

. This is consistent with the usual identity
 −r
s
!
= (−1)s
 r + s −1
s
!
for binomial coeﬃcients when r, s > 0. Replacing y by −y, we are led back
to the generating function 1/(1 −x −xy) for binomial coeﬃcients examined
above.
◁
Example 9.14 (Chebyshev polynomials). Let F(z, w) = 1/(1−2zw+w2) be the
generating function for Chebyshev polynomials of the second kind [Com74].
To use Theorem 9.12 for an arbitrary direction (r, s) with nonnegative indices
and r/s ∈(0, 1), we ﬁrst compute the critical points w± =

i

β −β−1
/2, iβ

,
where β = ±
q
s−r
s+r. These points are minimal by Corollary 6.36 because if
we substitute (z, w) = (tx, ty) in the denominator then |2xy −y2| is at most
t2 
1 −β2 + β2
< 1, and hence T(tw±) ∩V = ∅for all t ∈(0, 1). These points
are contributing because any smooth minimal critical points are contributing
for power series expansions.
Summing the asymptotic contributions given by the two points implies
ars ∼
r
2
π(−1)(s−r)/2
 
2r
√
s2 −r2
!−r 
r
s −r
s + r

−s r s + r
r(s −r)
252
Smooth point asymptotics
when r + s is even, while ars = 0 when r + s is odd. These asymptotics are
uniform as r/s varies over any compact subset of (0, 1).
◁
Exercise 9.4. Redo Examples 9.13 and 9.14 using Theorem 9.5 instead of
Theorem 9.12. What extra conditions do you need to check?
In the presence of minimal critical points we do not need to rule out the
critical points at inﬁnity (CPAI) discussed in previous chapters. However, if
we do rule out CPAI then Theorem 7.20 applies and we get the following.
Theorem 9.15 (Main Theorem of Smooth ACSV (No CPAI Version)). Sup-
pose that, as ˆr varies over a compact set R ⊂Rd of non-zero directions, the
function F has no CPAI with height at least M ∈R, and that the set W = W( ˆr)
of critical points with height larger than M is ﬁnite and consists of smooth non-
degenerate points. Then there exist κw ∈Z for w ∈W with
ar ≈
X
w∈W
κw Φw(r) + O(eM|r|) ,
(9.9)
where each Φw is the asymptotic series deﬁned by (9.4).
To determine dominant asymptotic behavior, it is necessary to identify the
highest critical points w with non-zero coeﬃcients κw. This seems to be a
very diﬃcult task in general, but we can say more in some circumstances.
For instance, κw = 1 for any smooth minimal contributing points, and if ar
is not eventually zero and M = −∞then at least one κw is non-zero. If the
exponential growth of a sequence can be determined or bounded using other
means, this can also be used to identify the highest coeﬃcients which are non-
zero, and thus pin down asymptotics up to these unknown integers.
Although Theorem 9.15 is the most abstract of our main theorems, it follows
directly from the large amount of technical background in Chapter 7 and the
appendices, and some computations from the proof of Theorem 9.12 below.
Proof of Theorem 9.15
Fix a direction ˆr. In the absence of CPAI at height M
or above, Theorem 7.20 in Chapter 7 shows that, for some ε > 0, the homology
group Hd(M, M≤M−ε) has a basis indexed by the critical points σ1, . . . , σm for
Q whose elements are smooth cycles γ j such that h ˆr attains its maximum on
γ j at σj and
ar =
m
X
j=1
κ j
(2πi)d−1
Z
γj
Res

F(z)z−r−1 dz

+ O(eM|r|).
We will determine this residue integral and its uniform error term with ˆr in our
proof of Theorem 9.12 below, giving the stated expansion.
□
