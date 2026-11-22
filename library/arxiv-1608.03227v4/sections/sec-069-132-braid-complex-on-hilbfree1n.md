---
doc_id: arxiv-1608.03227v4
doc_title: "Knot homology and sheaves on the Hilbert scheme of points on the plane"
section_id: sec-069-132-braid-complex-on-hilbfree1n
section_title: "Braid complex on Hilbfree1,n"
section_number: 13.2
pages: 74-75
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
toc_source: outline
doc_brief: "Knot homology and sheaves on the Hilbert scheme of points on the plane — For each braid β ∈Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗× C∗- equivariant sheaves on the"
---
1,n . In this subsection we explain how one could construct for every β ∈Brn
a periodic complex Sβ ∈Dper
Tsc(Hilbfree
1,n ) such that the hypercohomology of the complex is an isotopy invariant
of the link L(β). First let us explain a construction of the sheaf.
First let us introduce the analogs of the previous constructions for the Kn¨orrer reduced spaces. We deﬁne
X 2,fr to be a subvariety of X 2 × V 0 consisting of (X, g, Y, u) such that
C⟨X, Ad−1
g (Y )⟩u = V
The space X 2,fr is an open subvariety of X 2,fr × V and we can restrict the Kn¨orrer Φn × idV on this
open set to obtain:
Φn : MFsc
B2(X 2,fr, W) →MFsc
B2(X2,fr, W).
There is forgetful map fgt : X 2,fr →X 2 and the argument almost identical to the proof of Lemma 12.2
implies that fgt∗is the homomorphism of the convolution algebras and
(13.61)
Φn ◦fgt∗= fgt∗◦Φn.
It is natural to deﬁne X 1 := b× n and respectively we have the analog of the closure map je : X 1 →X 2
by je(X, Y ) = (X, e, Y ). Similarly, we deﬁne X 1,fc ⊂b × n × V to be ﬁ
Hilb
free
1,n
and we have a natural map
je : X 1,fc →X2,fr.
For any β ∈Brn we deﬁne the element of Dper
Tsc(Hilbfree
1,n ):
Sβ := j∗
e( ¯Cβ).
For a element S ∈Dper
Tsc(Hilbfree
1,n ) we denote by H(S) the doubly graded space of the hypercohomology of
the complex and let us introduce:
Hk(β) := H(Sβ ⊗∧kB)
The main result of the paper is the following
74
Theorem 13.3. The doubly graded space
Hk(β) := H(k+wr(β)−n−1)/2(β)
is the isotopy invariant of L(β).
Let us denote by H∗(Sβ ⊗∧mB) = Hodd(Sβ ⊗∧kB) ⊕Heven(Sβ ⊗∧kB) the sheaf on Hilbfree
1,n
that is the
sheaf of homology of the complex Sβ. Since the matrix factorization S′
β is supported on the critical locus
of W, the sheaf H∗(Sβ) is supported on subvariety Hilb1,n. Moreover, the following statement implies the
theorem 1.3 from the introduction.
Corollary 13.4. There is a spectral sequence with E2 term equal
(H∗(HilbL
1,n, H∗(Sβ ⊗∧kB)), d)
d : Hk(HilbL
1,n, Hodd/even(Sβ ⊗∧kB)) →Hk−1(HilbL
1,n, Heven/odd(Sβ ⊗∧kB)),
that converges to Hk(β).
