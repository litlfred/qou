---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-087-topology-of-complex-manifolds
section_title: "Topology of complex manifolds"
section_number: null
pages: 495-499
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
477
B.4 Topology of complex manifolds
For us, complex manifolds usually arise as (subsets of) varieties or the comple-
ments of varieties in Cd
∗, with ACSV requiring the integration of holomorphic
forms over chains of real dimension p contained in complex p-manifolds. This
ﬁnal section shows how the complex structure of a complex p-manifold makes
it behave in several ways like a real p-manifold, even though it actually has
real dimension 2p.
Proposition B.20 (Andreotti–Frankel Theorem). If X is a complex p-manifold
embedded in Cn for some n ≥p then X is homotopy equivalent to a CW
complex of dimension at most p. It follows that the singular homology groups
Hk(X) and singular cohomology groups Hk(X) vanish for all k > p.
Proof
Andreotti and Frankel [AF59] proved this for smooth algebraic (and
analytic) varieties using Morse theory. A sketch is given at the end of Ap-
pendix C.
□
Remark B.21. The complex projective space CPk is a complex manifold hav-
ing nonvanishing homology in all even dimensions up to 2k. Therefore it vi-
olates the conclusions of the Andreotti–Frankel Theorem, and cannot be em-
bedded in Cn for any n. This contrasts to the real case, where the Whitney
embedding theorem states that any real k-manifold can be embedded into R2k.
In fact, we can compute homology by considering only holomorphic forms.
If M is a complex p-manifold then the operator ω 7→dω preserves holo-
morphicity, so the holomorphic forms on M deﬁne a sub-cochain complex
Cn,holo of the de Rham complex Cn, called the holomorphic de Rham com-
plex. The inclusion Cn,holo ,→Cn does not, in general, induce an isomorphism
on cohomology, but once again this diﬃculty can be overcome by restricting
to manifolds embedded in complex space.
Proposition B.22 (holomorphic de Rham cohomology). Let M be a complex
p-manifold embedded in Cn. Then the inclusions Cn,holo(M) ,→Cn(M) induce
an isomorphism of cohomology rings. In particular, Hholo,k(M)  Hk(M) for
all k ≥0.
□
Proof
See Voisin [Voi02] and the notes at the end of this appendix.
□
We ﬁnish this appendix by observing a corollary of Proposition B.10 in the
complex setting.
Corollary B.23 (asymptotics depend only on relative homology class). Let X
be a complex manifold of dimension n with submanifold Y also of dimension
478
Algebraic topology
n, and deﬁne ω = ωλ = exp(λ φ(z)) η for some holomorphic n-form η and
holomorphic function φ on X. When C ≡C′ in Hn(X, Y) with Re{φ} ≤β on Y
then, as λ →∞,
Z
C
ωλ =
Z
C′ ωλ + O

eλβ
.
Proof
This follows immediately from Proposition B.10, because dω = 0 for
a holomorphic n-form on a complex n-manifold.
□
Notes
From their origins near the end of the nineteenth century, homology and co-
homology have become crucial tools in many areas of mathematics. Much of
our presentation of the material in this appendix follows Hatcher [Hat02] and
Munkres [Mun84], and further details can be found in those sources.
The Andreotti–Frankel Theorem is true in much greater generality than
Proposition B.20: for instance, it holds for all algebraic varieties in complex
aﬃne space, regardless of whether they are smooth or singular. This was ﬁrst
proved in [Kar79] via stratiﬁed Morse theory. The complement of a variety VQ
is biholomorphically equivalent to the variety V1−zd+1Q in one greater dimen-
sion, hence complements of d-dimensional aﬃne algebraic varieties are also
homotopy equivalent to d-dimensional cell complexes.
Voisin [Voi02] proves Proposition B.22 by showing that holomorphic de
Rham hypercohomology (cohomology with coeﬃcients in a sheaf resolution)
is the same as the ordinary de Rham cohomology, hence the same as smooth
cohomology and singular cohomology. For Stein spaces, such as embedded
complex manifolds, this resolution is ﬂat and holomorphic de Rham hyperco-
homology boils down to the cohomology of the holomorphic de Rham com-
plex itself. Special cases were known earlier; for example, if A is a complex
hyperplane arrangement then Brieskorn [Bri73] showed that the forms d f/ f as
f varies over annihilators of hyperplanes in A generate the cohomology ring
of the complement M of A.
Additional exercises
Exercise B.9. Deﬁne the M¨obius strip as the quotient of the cell complex
representing the unit square as ∆1 × ∆1 via the three identiﬁcations (0, 0) ∼
(1, 1), (0, 1) ∼(1, 0) and (0) × ∆1 ∼−(1) × ∆1.
(1) What is the dimension of this cell complex?
B.4 Topology of complex manifolds
479
(2) Give a basis for each space Z0, B0, Z1, B1, Z2, and B2.
(3) Compute the homology of the M¨obius strip with coeﬃcients in C from this
cell complex.
(4) What changes, if anything, if you use coeﬃcients in Z instead of coeﬃ-
cients in C?
Exercise B.10. Let X = C∗= C \ {0} be the punctured plane, the simplest case
of the complement of a hyperplane arrangement. To establish the complex de
Rham Theorem for H1(X) we need to show that holomorphic 1-forms ω and
θ map to the same element of the dual of H1(X) if and only if they diﬀer by a
coboundary d f.
(1) Use Theorem B.18 to prove the forward implication.
(2) Compute the homology of X by verifying that the embedding of S 1 into X
is a homotopy equivalence.
(3) Let ω be any holomorphic 1-form on X. Use Stokes’s Theorem to show
that
R
C ω = 0 for any C homologous to zero in H1(X).
(4) Let γ be the unit circle oriented, say, counterclockwise, and let η = ω −
cdz/z, where c = (2πi)−1 R
γ ω. Show that
R
C η = 0 for every C ∈Z1(X).
Hint: Use part 2.
(5) Show that
R
γ ω =
R
γ θ implies ω−θ = d f for some holomorphic function f.
Hint: You can construct f by integrating from an arbitrary ﬁxed basepoint.
Exercise B.11. Let X be the complex curve {(x, y) ∈C2 : x2 + y2 = 1}. By
the Andreotti–Frankel Theorem, it is homotopy equivalent to a cell complex
of (real) dimension 1. Demonstrate this by ﬁnding a deformation retract of X
onto a one-dimensional manifold.
Appendix C
Residue forms and classical Morse theory
In our ﬁrst two appendices, we developed the mathematics needed to prove
that the Cauchy integral representation
ar =
 1
2πi
!s Z
C
F(z) z−r−1dz
for the coeﬃcients of a convergent Laurent series F(z) =
P(z)
Q(z) = P
r arzr
depends only on the singular homology class of the chain C and the de Rham
cohomology class of the form F(z) z−r−1dz in the domain of holomorphicity
M =
z ∈Cd : Q(z)
d
Y
j=1
z j , 0

of the integrand.
In this appendix, we begin to discuss how such a representation allows us
to manipulate Cauchy integrals into a form where we can derive asymptotic
information. First, we discuss intersection classes and residue forms, which
illustrate how to convert the Cauchy integral into an integral lying “on” the
singular set V ⊂Cd of F. After introducing these concepts, we discuss how
to use Morse theory to manipulate integrals over chains in V into representa-
tions that will ultimately allow us to use saddle point approximations. Morse
theory is a large subject, and our treatment is restricted to the core topics we
need: height functions, attachments, homology groups, and homotopy type. In
this appendix we focus on the case where V∗:= V ∩Cd
∗is a complex mani-
fold. Appendix D, our ﬁnal appendix, describes extensions of this material to
general algebraic sets (and their complements) using stratiﬁed Morse theory.
480
