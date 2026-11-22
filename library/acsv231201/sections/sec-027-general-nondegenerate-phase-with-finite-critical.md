---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-027-general-nondegenerate-phase-with-finite-critical
section_title: "General nondegenerate phase with finite critical set"
section_number: null
pages: 143-147
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
125
necessary technical result in Lemma 5.10 below, which completes our proof of
this theorem.
□
Lemma 5.10. Let W = {z ∈Cd : Re{S (z)} > 0} and suppose that α ∈GLd(C)
maps Rd into W. If M = αTα is the matrix representing the quadratic form
S ◦α and π is the projection map from Cd onto Rd then π ◦α is orientation
preserving on Rd if and only if det α is the product of the principal square roots
of the eigenvalues of M (rather than the negative of this).
Proof
First suppose α ∈GLd(R). Then M has positive eigenvalues, and the
product of their principal square roots is positive. The map π is the identity on
Rd, so the claimed statement boils down to saying that α preserves orientation
if and only if it has positive determinant, which is true by deﬁnition. In the
general case, let αt = πt ◦α, where πt(z) = Re{z} + (1 −t) Im{z}. Since
πt(Rd) ⊆W for all 0 ≤t ≤1, the matrix Mt = αT
t αt always has eigenvalues
with nonnegative real parts. The product of the principal square roots of the
eigenvalues is a continuous function on the set of nonsingular matrices with
no negative real eigenvalues. The determinant of αt is a continuous function
of t, and we have seen it agrees with the product of principal square roots of
eigenvalues of Mt when t = 1 (the real case), so by continuity this is the correct
sign choice for all 0 ≤t ≤1. Taking t = 0 proves the lemma.
□
Exercise 5.8. Suppose φ is the logarithm of an analytic function, deﬁned only
up to the addition of (2πi)n for n ∈Z. How does this aﬀect the conclusion of
Theorem 5.2?
5.4 General nondegenerate phase with ﬁnite critical set
In this section we prove Theorem 5.3 by moving the chain of integration of I
so that Re φ is minimized only at the ﬁnite set of critical points, then applying
Theorem 5.2. We ﬁrst remark on some diﬀerences from our previous argu-
ments. While the chain of integration may be deﬁned on a subspace X ⊆Rd,
the form in the integrand will be extended to a neighborhood of X in Cd and the
deformation in general will not be conﬁned to X. To accomplish this, we deﬁne
a complexiﬁcation of X with analytic structure. Our deformation is deﬁned by
a smooth vector ﬁeld v which, although not analytic, lies in the complex tan-
gent bundle to the complexiﬁcation of each stratum. The proof is broken into
the following steps.
(1) Deﬁne the complexiﬁcation X ⊗C.
(2) Extend φ and η to a neighborhood U of X in Cd.
126
Multivariate Fourier–Laplace integrals
(3) Construct a vector ﬂow v on U, tangent to the strata of X⊗C and vanishing
precisely on G, such that ⟨Re dφ, v⟩> 0 on U \ G.
(4) Show that
R
C e−λφη =
R
C′ e−λφη, where C′ is obtained from C by ﬂowing
along v for a short time.
(5) Use Theorem 5.2 on the deformed chain C′.
Step (2) follows in a straightforward manner from Step (1). Step (3) is where
the special assumptions on X are used. This allows us to follow the methodol-
ogy of locally constant vector ﬁelds and partitions of unity in [ABG70], rather
than the more diﬃcult methodology of controlled vector ﬁelds in [Mat70].
Step (4) is an application of Stokes’s Theorem together with the crucial obser-
vation that part of the boundary of the chain representing the deformation lies
in a complex manifold of dimension less than d. Step (5), once we reach it, is
immediate.
Step 1: Complexiﬁcation
Lemma 5.11. Under the hypotheses of Theorem 5.3, there is a complex strat-
iﬁed space X ⊗C with strata S ⊗C as S ranges over the strata of X, such that
X ⊗C is a neighborhood of X in Cd and such that the chart maps ψ⊗C : Ck →
S ⊗C restricted to Rk are chart maps for S.
Proof
We complexify ∆p in Cp and Md−k in Cd separately and take the prod-
uct. First, we note that the set ∆p is deﬁned by p + 1 linear inequalities. Re-
laxing these by ε > 0 produces a neighborhood D of ∆p in Rd. Taking the
product with a suﬃciently small imaginary interval [−εi, εi] in each of the p
coordinates produces a complex stratiﬁed space that is a neighborhood of ∆p
in Cd. Because of our assumptions, we can complexify Md−k to V. Taking the
product of F ⊗C and Md−k ⊗C as stratiﬁed spaces, where F is a face of ∆p,
produces (F × M) ⊗C; these are the strata S ⊗C and ﬁt together to form the
stratiﬁed space X ⊗C satisfying the conclusion of the theorem.
□
Remark 5.12. In Chapter 9, we always have k = 1 and Md−k is a smooth
open (d −1)-patch in VQ. In Chapter 10, we have k = 0 and Md is a patch
of a middle-dimensional torus in Cd \ V. In general, under the condition that
the real tangent space spans a complex space of dimension d −k, one may
deﬁne Md−k ⊗C to be the intrinsic complexiﬁcation of M, namely the smallest
complex manifold containing M. This is known to exist [BER99], following a
construction of [BW59], and will be a complex (d −k)-manifold.
Exercise 5.9. Suppose X is the circle in R3 deﬁned by the real solutions to
x2 + y2 −1 = z = 0. Find the complexiﬁcation X ⊗C.
5.4 General nondegenerate phase with ﬁnite critical set
127
Step 2: Extending analytic maps
Proposition 5.13. Let φ : X →C be an analytic map on an analytic stratiﬁed
space X, and let ψ1 and ψ2 be chart maps whose ranges are overlapping do-
mains N1 and N2 in X. As y takes values in the intersection of the ranges of
ψ1 ⊗C and ψ2 ⊗C, the function ˜φ = ˜φj deﬁned by
˜φj(y) = τj ◦(ψ j ⊗C)−1(y)
(5.12)
is independent of j, where τ j represents analytic continuation of the map φ◦ψ j
from the real parameter space to a complex neighborhood of it. This common
value deﬁnes an analytic extension of φ on a neighborhood of X in Cd.
Proof
The maps ˜φ1 and ˜φ2 agree when y ∈N1 ∩N2 ∩X. Being analytic, they
must agree in a neighborhood of X in X ⊗C.
□
Step 3: Constructing the vector ﬂow
Lemma 5.14. Under the assumptions of Theorem 5.3, there is a vector ﬁeld v
on a neighborhood U of X in Cd, tangent to each complexiﬁed stratum S ⊗C
of X ⊗C and vanishing only on G, with the property that ⟨Re dφ, v⟩> 0 at
every point of U \G. For suﬃciently small s, there is a well-deﬁned diﬀerential
ﬂow Ψ : [0, 1] × |C| →Cd satisfying (d/dt)Ψ(t, x) = s v(Ψ(t, x)), and the map
x 7→Ψ(ε, x) is a local diﬀeomorphism for suﬃciently small ε > 0.
Proof
As described in Proposition D.14 of Appendix D, there is a diﬀeo-
morphic local product structure under the assumptions of Theorem 5.3. The
argument discussed in Step 2 of the proof of Proposition D.13 in Appendix D
implies that there is a Lipschitz vector ﬂow v on a neighborhood U of X in Cd
deﬁned by (D.2.1). This vector ﬁeld v is tangent to each complexiﬁed stratum,
vanishes precisely on G, and satisﬁes ⟨Re dφ, v⟩> 0 on U \ G.
The map x 7→Ψ(ε, x) is a local diﬀeomorphism for suﬃciently small
ε > 0 because v is smooth and bounded (see, for example, [Lee03, Propo-
sition 9.12]).
□
Step 4: Deforming the contour
Composing the ﬂow from Lemma 5.14 with the simplex σ j gives a homotopy
from each σ j to a new analytic simplex σ′
j, and summing the σ′
j deﬁnes a new
chain C′. Because v is tangent to S ⊗C for each stratum S, the ﬂow preserves
each complexiﬁed stratum S ⊗C, and because ∂C is contained in the union of
strata of dimensions at most p + d −k −1, it follows that Ψ(∂C) is contained in
the union of complexiﬁed strata of dimensions at most p + d −k −1.
128
Multivariate Fourier–Laplace integrals
Lemma 5.15. Using the above notation,
Z
C
e−λφη =
Z
C′ e−λφη .
(5.13)
Proof
The homotopy Ψ deﬁned by Lemma 5.14 is a chain with boundary
C−C′−[0, 1]×∂C. Since e−λφη is a holomorphic p+d−k-form, it is annihilated
by the diﬀerential, and Stokes’s Theorem implies
0 =
Z
Ψ
d(e−λφη)
=
Z
∂Ψ
e−λφη
=
Z
C′ e−λφη −
Z
C
e−λφη −
Z
D
e−λφη ,
where D is a chain representing [0, 1] × ∂C. Because e−λφη is a holomorphic
(p + d −k)-form, its integral vanishes over any p + d −k-chain supported
on a (p + d −k −1)-dimensional complex manifold (see Exercise A.15 of
Appendix A), ﬁnishing the proof.
□
Exercise 5.10. A simpler version of the deformation argument can be illus-
trated in two real variables. Suppose that V(x, y) is a smooth function on R2 and
η = Vx(x, y)dx + Vy(x, y)dy. Assume that a homotopy H : [0, T] × [0, 1] carries
the path α : [0, T] →R2 to the path β : [0, T] →R2, meaning H(t, 0) = α(t)
and H(t, 1) = β(t) for all t ∈[0, T]. If f(u) = H(0, u) and g(u) = H(T, u) then
what conditions on d f and dg guarantee that
R
α η =
R
β η by implying that the
integrals over the paths traced out by the endpoints of the path as it moves from
α to β are everywhere zero?
Step 5: Evaluating the integral on C′
From the construction of v we see that C′ = Pm
j=1 σ′
j, where each simplex
σ′
j contains the same critical point q in its interior as σ j. By Lemma 5.14 we
know that Re φ(σ′
j(x)) ≥Re φ(σ j(x)) ≥0 for all j ≤m and x ∈∆p, where
the ﬁrst inequality is strict unless σ j(x) is a critical point. Thus, the image |C′|
is a stratiﬁed space represented analytically by (p + d −k)-simplices σ′
j for
1 ≤j ≤m and the function Re φ is nonnegative and vanishes precisely on G′.
If σ′
j contains no point of G′ then the modulus of
R
σ′
j e−λφ(z) η is bounded
above by Me−λK, where M = max{|A(x)| : x ∈∆d} and K = min{Re φ(x) :
x ∈∆d}. If σ′
j contains q ∈G′ then translating the preimage of q to the origin
turns ∆p+d−k into a neighborhood N of the origin on which A and ˜φ = φ ◦σ′
j
are analytic and Re ˜φ(z) ≥0, with equality only at the origin. Theorem 5.2
