---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-048-the-method-of-residue-forms
section_title: "The method of residue forms"
section_number: null
pages: 275-280
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
257
Deﬁnition 9.20 (strong torality). We say Q satisﬁes the strong torality hy-
pothesis on the torus T(w) if Q(z) = 0 and |z j| = |wj| for 1 ≤j ≤d −1 implies
that |zd| = |wd|.
Exercise 9.6. Suppose that the function Q(x, y) = a + bx + cy + dxy is bilinear.
What conditions on the constants a, b, c, d are equivalent to strong torality of
Q?
In the following proposition g is the multivalued function solving for zd as a
function of z◦; the number of values, counted with multiplicities, is the degree
m of zd in Q, except on a lower dimensional set where two values coincide.
The multivalued integrand should be interpreted as a sum over all m values.
Corollary 9.21 (reduction under strong torality). Suppose w satisﬁes all of the
hypotheses of Theorem 9.5 except that instead of w being ﬁnitely minimal, it
is minimal and Q satisﬁes the strong torality hypothesis on T(w). If all poles
of F on T(w) are simple (i.e., p = 1) then
ar =
 1
2πi
!d−1 Z
T(w◦)
(z◦)−r◦g(z◦)−rdΨ(z◦)dz◦
z◦,
where Ψ is given by (9.13).
Proof
This time we may take C1 to be the circle of radius of ρ −δ and C2 to
be the circle of radius ρ + δ for any δ ∈(0, ρ). The inner integral will be the
sum of simple residues at points g(z◦) for any z◦and the proof is completed
the same way as Theorem 9.17.
□
In this case dimension is reduced by one without localizing. The localization
occurs when we apply the multivariate saddle point results of Chapter 5, which
implies that this (d −1)-dimensional integral is determined by the behavior of
g and Ψ near the critical points on T(w).
Corollary 9.22. Suppose w satisﬁes all of the hypotheses of Theorem 9.5 ex-
cept that instead of w being ﬁnitely minimal, Q satisﬁes the torality hypothesis
on T(w). Then the conclusions of Theorem 9.5 still hold.
9.2 The method of residue forms
In this section we use the homological framework of previous chapters, to-
gether with the appendices, to prove Theorem 9.12. For convenience, we begin
by naming the minimality property assumed in Theorem 9.12.
258
Smooth point asymptotics
Deﬁnition 9.23 (ﬁnite criticality). We say Q is ﬁnitely critical on the torus
T(w) (in the direction ˆr) if the intersection of VQ with T(w) contains ﬁnitely
many critical points of Q in the direction ˆr.
Exercise 9.7. For which directions ˆr (if any) does the function Q(x, y) = (1 +
x)(1 + y) satisfy ﬁnite criticality on the unit torus T(1, 1)?
Suppose that p is a minimal point of V that is critical in direction ˆr and
lies in the exponential torus Te(x) = Relog−1(x) deﬁned by some x ∈∂B,
where B is a component of the complement of amoeba(Q). Further assume
that Te(x) ∩V contains only ﬁnitely many critical points p1, . . . , pm.
Proposition 9.24 (stratiﬁed ﬂow). For x′ ∈B arbitrarily close to x, the torus
Te(x′) may be deformed in M so that it remains ﬁxed in a neighborhood of
each critical point pj but moves to a height less than −ˆr · x outside of a larger
neighborhood of each.
Proof
This is a consequence of Theorem 11.5, which uses cones of hyperbol-
icity to create a deformation based on Theorem 11.1. In the case that the points
p1, . . . , pm are all smooth points, the cones and vectors can be constructed by
the simpler and more explicit Theorem 11.9 and Corollary 11.10.
□
We remark that because ˜Q is hyperbolic at all minimal points (see Proposi-
tion 11.26), the vector ﬂow used in the proof of Proposition 9.24 can also be
used to construct the general homotopy equivalence (C.3.1), giving the rela-
tive homology attachment groups up to points of height just below the minimal
points. An important practical consequence is the following principle, stating
that local integral formulae may be summed when ﬁnite criticality holds. It
follows immediately from the deformation in Proposition 9.24.
Theorem 9.25 (ﬁnite criticality implies sum of local contributions). Suppose
that w is a minimal point satisfying ﬁnite criticality, with all critical points on
T(w) enumerated p1, . . . , pm. If each of the pj are nondegenerate contributing
points and the Cauchy integral over a quasi-local cycle maximized near pj has
asymptotic expansion Φpj(r) then
ar ≈
m
X
j=1
Φpj(r) + E(r)
(9.17)
where E(r) grows exponentially slower than the common value of the |p−r
j |. □
Theorem 9.25 holds for general rational functions, not just those with smooth
denominators, for more general deﬁnitions of contributing points that are dis-
cussed in later chapters.
9.2 The method of residue forms
259
Figure 9.2 Spacetime generating function for a one-dimensional quantum walk.
Exercise 9.8. Let Q(x, y) = 1 −cy(1 + x) −xy2, where c ∈(0, 1). The func-
tion 1/Q is the spacetime generating function for the simplest non-trivial one-
dimensional quantum walk [BP07].
(a) Show that all singularities on the unit torus are minimal points.
(b) Show that the singularities on the unit torus are not ﬁnitely minimal.
(c) Show that for |a −1/2| < c/2 and ˆr =
h a
a+1,
1
a+1
i
there are two critical
points in the direction ˆr on the unit torus.
(d) Explain why (9.17) produces the picture in Figure 9.2 for the generating
function F(x, y) = 1/Q(x, y).
9.2.1 Theorem 9.12 via residue integrals
We are now ready to prove the minimal point version of the Main Theorem of
Smooth ACSV.
Proof of Theorem 9.12
Assume the hypotheses of Theorem 9.12 and let B be
the component of amoeba(Q)c corresponding to the convergent Laurent series
under consideration. We use the homological constructions and terminology
introduced in Appendix C. If T = Te(x) for some x ∈B and T ′ = Te(x′) for
some x′ ∈B′, where B′ is one of the components of amoeba(Q)c on which h ˆr
260
Smooth point asymptotics
is not bounded from below (whose existence is guaranteed by Theorem 6.29),
then the intersection class INT(T, T ′) is represented by the intersection of V
with any homotopy from T to T ′ intersecting V transversely. Choosing such
a homotopy whose time-t cross-sections are tori that expand with t and go
through w, perhaps slightly perturbed to intersect V transversely, the class
INT(T, T ′) can be represented by a smooth (d −1)-chain γ on V on which
h ˆr reaches its (not necessarily unique) maximum at w. The Cauchy integral
formula and the residue theorems from Chapter C imply
ar =
1
(2πi)d
Z
T
F(z)z−r−1 dz
=
1
(2πi)d−1
Z
γ
Res(F(z)z−r−1 dz) +
1
(2πi)d−1
Z
T ′ F(z)z−r−1 dz
=
1
(2πi)d−1
Z
γ
Res(F(z)z−r−1 dz).
(9.18)
Assume ﬁrst that Q is square-free and rd > 0, so that (C.2.1) in Proposi-
tion C.8 implies
ar = e−hr(w)
(2πi)d−1
Z
γ
e−λφ(z)
P(z)
Qzd(z) Qd
j=1 zj
dz◦
with λ = rd. Applying Theorem 5.3 with a generic triangulation of C = γ gives
an asymptotic expansion of ar which, after the change of variables zj = wjeiθj
and algebraic simpliﬁcation, gives the expression for Φw in (9.2). Note that
the Hessian determinant of h ˆr on V with respect to the θ j variables equals the
Hessian determinant with respect to the zj variables multiplied by the Jacobian
for the change of variables because the gradient of h ˆr restricted to V vanishes
at w.
This completes the proof of Theorem 9.12 in the case that p = 1 and rd > 0.
The derivation for p > 1 is similar, with Lemma C.13 describing the residue
and leading to (9.4). Likewise, accounting for the sign change in λ = −rd when
rd < 0 produces the sign factors in (9.4).
□
9.2.2 Homological decompositions
Our results above help us prove that there is at most one torus containing
smooth nondegenerate contributing points. A minimal torus with respect to
a component B and direction ˆr is a torus Te(x) for some x ∈∂B minimizing
ˆr · x on B, containing at least one point w = exp(x + iy) that is critical in
direction ˆr.
9.2 The method of residue forms
261
Proposition 9.26. Let F(z) = P(z)/Q(z) be the ratio of coprime polynomials
P and Q. Fix a direction ˆr, a component B of the complement of amoeba(Q)
on which h ˆr is bounded from below, and a component B′ on which h ˆr is not
bounded from below.
(i) There is at most one minimal torus with respect to B and ˆr satisfying
ﬁnite criticality and on which each critical point is smooth, contributing,
and nondegenerate.
(ii) Let T = Te(x) for some x ∈B and let T ′ = Te(x′) for some x′ ∈
B′. Given the existence of the torus described in (i), the projection of
INT(T, T ′) to the relative homology group Hd−1(V∗, V≤c−ε), for suﬃ-
ciently small ε > 0 and c = −ˆr · x, equals P
z∈W γz, where the cycle γz
is a generator for the cyclic local homology group Hd−1(Vz,loc
∗
).
(iii) The projection of [T] to (M, M≤c−ε) is equal to P
z∈W oγz, where γz is a
generator of the cyclic group Hd−1

Vz,loc
∗

.
Proof
To prove (i), suppose there are two such tori Te(x) and Te(x′). Ap-
plying Theorems 9.12 and 9.25 to the rational function ˜F(z) = 1/ ˜Q(z) at the
points in each torus gives two, necessarily equal, asymptotic series estimating
the coeﬃcients {˜ar} uniformly as |r| →∞with r/|r| remaining in some neigh-
borhood R of ˆr (we replace P by 1 and Q by its square-free part as this does not
change the minimal tori or our nondegeneracy assumptions, but simpliﬁes the
asymptotic formulae). In particular, the leading term of each expansion Φw(r)
in (9.4) has the form C(w) exp(−r·x) exp(−ir·y)r(1−d)/2
d
with C nonvanishing.
Summing the contributions of the ﬁnitely many points on Te(x) (respectively
Te(x′)) gives a function of r that is nonvanishing at least on some ﬁnite-index
sublattice of Zd. Furthermore, the terms given by the elements of Te(x) and
the elements of Te(x′) diﬀer from each other in exponential growth, because
−x · r and −x′ · r disagree on R except possibly for a set of codimension 1.
This contradicts the fact that both expansions represent asymptotics for the
same sequences, so two such tori cannot exist.
To prove (ii), the deformation used to prove Theorem 5.3 shows that the
intersection cycle may be deformed to a sum of elements of local homology
groups. None of these can be zero because there is a term corresponding to
each in (9.8). Similarly, each is a relative homology generator: this can be seen
from the deformation, but an easier argument is that the corresponding term
Φw(r) is, up to sign, the integral obtained from a small (d −1)-patch and we
know the local homology generator is a (d −1)-ball modulo its boundary (see,
for example, Theorem C.38).
Conclusion (iii) can be argued similarly to (ii), using the stratiﬁed descrip-
tion of attachments from Theorem D.25 in place of Theorem C.38. Alterna-
262
Smooth point asymptotics
tively, the Thom isomorphism (Theorem C.2) says that o induces an injec-
tion from Hd−1(V∗) to Hd(Cd
∗\ V). Being functorial, it commutes with π∗
where π : V∗→(V∗, V≤c−ε) is projection. The Thom isomorphism carries
INT(T, T ′) to T −T ′, which is equal to T in Hd(V∗, V≤c−ε), proving (iii).
□
We remark that it is possible to have a minimal smooth contributing point p
in the direction ˆr, and another smooth critical (but not contributing) point p′
in the direction ˆr that is not minimal but has the same height as p.
