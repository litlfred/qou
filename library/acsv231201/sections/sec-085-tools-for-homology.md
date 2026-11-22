---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-085-tools-for-homology
section_title: "Tools for homology"
section_number: null
pages: 486-493
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
Although we can compute the homology of a variety, or the complement of a
variety, by triangulating the space and computing simplicial homology, this can
be very expensive (such algorithms are generally considered eﬃcient if they
run in single-exponential instead of doubly-exponential time; see [Bas08] for
a survey of complexity results in this area). Furthermore, instead of computing
the entire set of homology groups of a singular variety, we often only need
some partial information in our integral manipulations, for instance throwing
away topological information that does not aﬀect dominant asymptotics.
Because of such considerations, it is useful to have additional tools to com-
pute homology. One of the most eﬀective approaches is to work recursively,
studying a space X using a subspace A ⊂X and the quotient space X/A. The
relationship between the homology groups of X, X/A, and A is explicit but
intricate, with the homologies ﬁtting into a type of nesting structure. We thus
require some additional algebraic constructions to describe precisely what is
going on.
An exact sequence of abelian groups (and in particular, complex vector
spaces) is a sequence of maps
· · · →Xn+1
fn+1
−−−→Xn
fn−→Xn−1 →. . . ,
where the image of each map is equal to the kernel of the next. For instance, an
exact sequence of the form 0
ϵ−→A
α−→B says 0 = Image(ϵ) = Kernel(α), so α
is injective, while an exact sequence of the form A
α−→B
ϵ−→0 says Image(α) =
Kernel(ϵ) = B, so α is surjective. A short exact sequence is an exact sequence
of the form
0 →X →Y →Z →0 ,
meaning the map from X to Y is injective and the map from Y to Z is surjective.
B.2 Tools for homology
469
Remark B.7. When X, Y, and Z are ﬁnite dimensional complex vector spaces
of dimensions k, ℓ, and m, respectively, then a short exact sequence 0 →X →
Y →Z →0 implies ℓ= k + m and Y = X ⊕Z as a direct sum. However,
this splitting is not natural: X embeds naturally into Y but there is no canonical
choice of coset representatives for Y/Z.
A short exact sequence of chain complexes is a map of chain complexes
which is a short exact sequence on the n-chains for all n. One very useful fact
about short exact sequences of chain complexes is that they give rise to long
exact homology sequences.
Theorem B.8 (Zig-Zag Lemma). Let 0 →A
α−→B
β−→C →0 be a short exact
sequence of chain complexes. Then there is an exact sequence
· · · →Hn+1(C)
∂∗
−→Hn(A)
α∗
−−→Hn(B)
β∗
−→Hn(C)
∂∗
−→Hn−1(A) →. . . ,
(B.2.1)
where α∗and β∗are the homology maps induced by the chain maps α and β.
Proof
See [Mun84, Lemma 24.1].
□
The exact sequence (B.2.1) in Theorem B.8 is known as the long exact se-
quence on homology. The homology map ∂∗has a natural but unwieldy deﬁ-
nition; instead of deﬁning it in general we describe it explicitly in the situation
most relevant to us in Corollary B.11 below.
Relative homology and excision
Our goal is to apply Theorem B.8 to a short exact sequence of chain complexes
related to embedding a subspace A into a space X and then taking the quotient
to map into X/A. In fact, we consider a slightly more general setting which is
also useful for our asymptotic calculations.
A pair of spaces (X, A) is any pair of topological spaces with A a subspace
of X. A pair map f : (X, A) →(X′, A′) between pairs of spaces is any (topo-
logical) map f : X →X′ such that f(A) ⊂A′. The inclusion A ,→X induces
an inclusion of chain complexes C(A) ,→C(X), and we let C(X, A) denote the
pair complex whose n-chains are the quotient group Cn(X)/Cn(A). The rela-
tive homology of the pair (X, A) is the homology H∗(X, A) = H∗(C(X, A)) of
the pair complex.
One may think of relative homology roughly as the homology of X if the
subspace A were to be shrunk to a point: Hn(X, A) contains relative cycles
γ ∈Cn(X) with ∂γ ∈Cn−1(A) modulo relative boundaries β = ∂ζ + α, where
ζ ∈Cn+1(X) and α ∈Cn(A). We thus search for cycles that do not bound, but
are willing to count a chain as a cycle if its boundary is in A; see Figure B.2.
470
Algebraic topology
X
Y
γ
Figure B.2 γ is a relative cycle in C(X, Y).
We often use relative homology to “ignore” regions that do not contribute to
dominant asymptotics in our integral manipulations.
The concept of homotopy equivalence is deﬁned for pairs of spaces simi-
larly to the deﬁnition for spaces, and homotopy equivalent pairs have the same
relative homology.
Example B.9. Let X be the unit ball in Rn and A be the unit sphere S n−1. To
compute the homology of the pair (X, A) we consider the unit n-simplex ∆n
and its boundary: topologically (∆n, ∂∆n) and (Bn, S n−1) are homeomorphic,
so their relative homologies are the same. The simplicial chain complex for ∆n
contains all faces of ∆n, hence it has simplices in dimensions 0 through n. The
complex of the pair is non-trivial only in dimension n because every face of
dimension less than n is supported on ∂∆n. Proposition B.5 (that simplicial and
singular homology coincide) extends to pairs composed of a simplicial com-
plex and a subcomplex. Therefore, the singular homology of the pair (Bn, S n−1)
is computed by this rather small chain complex, leading to Hk(Bn, S n−1)  C
when k = n and 0 otherwise.
◁
Exercise B.4. What is the relative homology of (S 2, S 2
−), where S 2 is the 2-
sphere and S 2
−is the closed southern hemisphere?
Relative homology is useful for approximating integrals due to the following
result.
Proposition B.10 (asymptotics depend only on relative homology class). Let
X be a manifold of dimension n with submanifold Y also of dimension n, and
let φ be a smooth complex-valued function on X satisfying ℜ{φ} ≤β on Y for
some β ∈R. Suppose that ω = ωλ = exp(λ φ(z)) η for some closed k-form η on
B.2 Tools for homology
471
X with k ≤n. If C and C′ are k-chains on X with C ≡C′ in Hk(X, Y) then, as
λ →∞,
Z
C
ωλ =
Z
C′ ωλ + O

eλβ
.
Proof
By deﬁnition, the diﬀerence between C and C′ is a relative boundary
C −C′ = ∂D + C′′ with C′′ supported on Y. Using Stokes’s Theorem (Theo-
rem A.24),

Z
C
ω −
Z
C′ ω

 =

Z
∂D
ω +
Z
C′′ ω

 =

Z
D
dω +
Z
C′′ ω

=

Z
C′′ ω

 ≤
Z
C′′ eλβ|η| ≤Keλc′,
where K =
R
C′ |η| and the appearance of |η| in an integral means that when η is
pulled back to integrate, we integrate the modulus of the result.
□
Let (X, A) be a pair for which A is a strong deformation retract of an open
neighborhood in X. It can be shown [Mun84, Ex. 39.2] that for all n ≥1
the relative homology group Hn(X, A) is isomorphic to the singular homol-
ogy group Hn(X/A) of the quotient X/A, obtained from X by shrinking A to a
point. This gives a way of computing the homology of a quotient X/A: apply-
ing Theorem B.8 to the short exact sequence of chain complexes 0 →C(A) →
C(X) →C(X, A) →0 gives a long exact sequence computing H∗(X, A), and
hence H∗(X/A), from H∗(X), H∗(A) and some knowledge of the maps in the
long exact sequence.
Corollary B.11. Let A be a subspace of X. Then there is a long exact sequence
of the pair (X, Y),
· · · →Hn+1(X, A)
∂∗
−→Hn(A)
i∗−→Hn(X)
j∗−→Hn(X, A)
∂∗
−→Hn−1(A) →· · · ,
where i∗and j∗are the maps induced by the inclusions of A into X, and X
into (X, A), respectively, and ∂∗is the map induced by taking a relative cycle
γ ∈Cn(X) to its boundary ∂γ ∈Cn−1(A). When A is a deformation retract of
an open neighborhood in X then this long exact sequence holds with Hn(X, A)
replaced by ˜Hn(X/A), where the reduced homology group ˜Hn is the same Hn
when n > 0, and has dimension one less when n = 0.
Exercise B.5 (computing homology of S n−1). Let X = ∆n and let Y be the
subcomplex of cells with dimension strictly less than n. Use the long exact
sequence for the pair (X, Y) to determine Hn−1(Y).
One important feature of relative homology is the excision property.
472
Algebraic topology
X
Y
γ
U
Figure B.3 (X \ U, Y \ U) ,→(X, Y) is a homology isomorphism.
Proposition B.12 (excision theorem). Given subspaces U ⊂Y ⊂X such that
U ⊂int(Y), the inclusion (X \ U, Y \ U) ,→(X, Y) induces an isomorphism
H∗(X \ U, Y \ U)  H∗(X, Y).
Proof
See [Hat02, Theorem 2.20].
□
Informally, Proposition B.12 says that the relative homology of (X, Y) can-
not see the interior of U; Figure B.3 gives an illustration. Relative homology
can also be used to deﬁne another important homology theory for cell com-
plexes. If X = Xn is a cell complex then the cellular chain complex of X is the
complex
· · · →Hn+1(Xn+1, Xn)
∂n+1
−−−→Hn(Xn, Xn−1)
∂n
−→Hn−1(Xn−1, Xn−2) →· · · ,
where we deﬁne X−1 = ∅and ∂n is the composition of the boundary opera-
tor mapping Hn(Xn, Xn−1) to Hn−1(Xn−1) with the inclusion of Hn−1(Xn−1) into
Hn−1(Xn−1, Xn−2). The homology groups of this cellular chain complex form
the cellular homology groups of X. Cellular homology is homology of (rela-
tive) homology, and can be surprisingly useful. Although its deﬁnition might
seem technical and contrived, Hn(Xn, Xn−1) can be interpreted easily as linear
combinations of the n-cells in X. The following result makes cellular homol-
ogy a tool for computation.
Proposition B.13. If X is a cell complex then the nth singular homology group
of X is isomorphic to the nth cellular homology group of X.
Among other things, Proposition B.13 implies that if X can be represented
by a cell complex with no n-cells then Hn(X) = 0. See [Hat02, Section 2.2] for
a full discussion of cellular homology, its implications, and a proof of Propo-
sition B.13.
B.2 Tools for homology
473
The homology of a union
Instead of decomposing a space X using a subspace and the corresponding
quotient space, we can instead represent X as a union X = A ∪B for subspaces
A, B ⊂X such that X = int(A) ∪int(B) and describe the homology of X in
terms of the homologies of A, B, and A ∩B. In particular, there is a short
exact sequence of chain complexes deﬁned by the short exact sequence in each
dimension,
0 →Cn(A ∩B)
p−→Cn(A) ⊕Cn(B)
s−→Cn(A) + Cn(B) →0,
where p(a) = (−a, a) and s(a, b) = a+b, with Cn(A)+Cn(B) ⊆Cn(X) denoting
a sum inside the space of chains on X. The corresponding long exact sequence
is known as the Mayer–Vietoris sequence.
Theorem B.14 (Mayer–Vietoris sequence). Let A, B ⊂X be such that X is
the union of the interiors of A and B. Then the inclusion of the chain complex
C∗(A) + C∗(B) ,→C∗(X) induces an isomorphism in homology. It follows that
there is a long exact homology sequence
· · · →Hk(A ∩B) →Hk(A) ⊕Hk(B) →Hk(X) →Hk−1(A ∩B) →· · · .
Proof
See [Hat02, Proposition 2.21] or [Mun84, Theorem 33.1].
□
Exercise B.6. Use the Mayer–Vietoris sequence to re-compute the homology
of S n by decomposing it as the union of two hemispheres, expanded a little so
their interiors cover S n. How does the result of this computation relate to a geo-
metric understanding of two balls glued along their boundary? Try visualizing
in dimensions one and two for greatest intuition.
Attachments and the homology of a product
Relative homology is useful for our asymptotic computations because it allows
us to “ignore” points that are asymptotically negligible. In practice, to study
complex integrals whose domains of integration are allowed to vary in some set
M we describe M by attaching diﬀerent spaces together as needed. In essence,
we express M on-the-ﬂy as a cell complex until we have enough information
to perform the necessary asymptotic computations (much more information on
this approach is given in the next appendix on Morse theory). This section, our
ﬁnal on the basics of homology, describes product complexes, attachments,
and products of pairs.
Let C′ and C′′ be chain complexes with boundary maps ∂′ and ∂′′. The
tensor product complex (or simply product complex) of C′ and C′′ is the chain
complex C = C′ ⊗C′′ whose n-chains Cn are deﬁned by the direct sum Cn =
Ln
k=0 C′
k ⊗C′′
n−k, where a basis for the tensor product C′
k ⊗C′′
n−k is given by
474
Algebraic topology
elements σk ⊗τn−k as σk ranges over a basis for C′
k and τn−k ranges over a basis
for C′′
n−k. The boundary operator ∂of C is deﬁned by ∂(σk ⊗τn−k) = (∂′σk) ⊗
τn−k + (−1)kσk ⊗(∂′′τn−k). The product Z = X × Y of two simplicial complexes
X and Y is naturally a cell complex, and this deﬁnition is constructed so that
the product chain complex C(X) ⊗C(Y) is isomorphic [Mun84, Theorem 57.1]
to the cellular chain complex of Z.
Example B.15. Consider C = ∆1 as a cell complex with two 0-cells {[0], [1]}
and one 1-cell σ1 = [0, 1] oriented from 0 to 1, meaning that ∂σ1 = [1] −
[0]. Then C × C has four 0-cells {(0, 0), (1, 0), (0, 1), (1, 1)}, four 1-cells {σ1 ×
[0], σ1 × [1], [0] × σ1, [1] × σ1}, and one 2-cell σ1 × σ1.
◁
Exercise B.7. Write the circle S 1 as a cell complex, then describe the product
cell complex S 1×S 1. Compute the homology of S 1×S 1 from this cell complex.
The homology of a product is given by the K¨unneth formula. Because we
study homology with complex coeﬃcients, the formula is relatively simple.
Theorem B.16 (K¨unneth product formula). If C′ and C′′ are the singular chain
complexes for two cell complexes then there is a natural isomorphism
M
p+q=n
Hp(C′) ⊗Hq(C′′) →Hn(C′ ⊗C′′) .
Proof
See [Mun84, Theorem 58.5].
□
Exercise B.8. Use the K¨unneth formula to compute the homology of S 1 × S 1
and verify it is the same as you computed in Exercise B.7.
Generalizing the attaching maps for cell complexes, the attachment of a
space Y to a space X along a closed subset Y0 ⊆Y by the map φ : Y0 →X is
the topological quotient (X ⊔Y)/φ obtained from the disjoint union of X and
Y by identifying each y ∈Y0 with φ(y) ∈X. The triple (Y, Y0, φ) is known as
attachment data.
Remark. When φ is one-to-one, attachments are more or less the same as
unions; that is, both X and Y naturally embed in the attachment and their union
covers the attachment. In general, an attachment can be thought of as a union of
a space X with a quotient Y/φ, where points y1, y2 ∈Y0 are identiﬁed if φ(y1) =
φ(y2). While the two spaces in a union play symmetric roles, the attachment
of a space Y to a space X is described asymmetrically. This coincides with the
framework of ﬁltered spaces built up by successive attachments, described in
the next appendix. Thus attachments, while not entirely new, provide a useful
way to build up a space.
