---
doc_id: oberwolfachreports1223-v20120708-9-40
doc_title: "Mathematisches Forschungsinstitut Oberwolfach Report No. 28/2012 Invariants in Low-Dimensional Topology and Knot Theory Organised by"
section_id: sec-018-spinal-open-books-and-algebraic-torsion-in-conta
section_title: "Spinal open books and algebraic torsion in contact 3-manifolds"
section_number: null
pages: 36-39
source_pdf: OberwolfachReports1223_v20120708_9_40.pdf
source_sha256: 94f82cfc185955ba
toc_source: inferred
doc_brief: "Mathematisches Forschungsinstitut Oberwolfach Report No. 28/2012 Invariants in Low-Dimensional Topology and Knot Theory Organised by — This meeting concentrated on topological invariants in low di"
---
Chris Wendl
(joint work with Janko Latschev, Samuel Lisi, Jeremy Van Horn-Morris)
It is a long-standing conjecture1 in 3-dimensional contact topology that if (M, ξ)
is any tight contact manifold and (M ′, ξ′) is obtained from (M, ξ) by Dehn surgery
along a Legendrian knot with framing −1 relative to the canonical contact fram-
ing, then (M ′, ξ′) is also tight. Since Legendrian surgery can be viewed as the
1During the same workshop, Andy Wand announced a proof of this conjecture using open
book decompositions and a new characterization of tightness in terms of the monodromy map.
Invariants in Low-Dimensional Topology and Knot Theory
37
attachment of a Weinstein 2-handle and thus gives rise to a Stein cobordism from
(M, ξ) to (M ′, ξ′), it is immediate that it always preserves symplectic ﬁllability;
the latter implies tightness, but the converse is not true. The following joint result
with Janko Latschev shows that there is a great deal of interesting structure within
the class of contact manifolds that are tight but not ﬁllable.
Theorem 1 ([1]). There exists a nested inﬁnite sequence of classes of closed
contact 3-manifolds
{all} = Ξ0 ⊃Ξ1 ⊃Ξ2 ⊃. . . ⊃Ξ∞⊃{symplectically ﬁllable}
with the following properties:
(1) For each k = 0, 1, 2, . . ., ∞, Ξk is preserved by Legendrian surgery,
(2) Ξ1 contains all closed contact 3-manifolds that are tight.
It is possible that Ξ1 in this result may be precisely the class of tight contact
3-manifolds: this would be equivalent to the statement that a closed contact 3-
manifold has vanishing contact homology if and only if it is overtwisted. That
would of course imply a new proof of the conjecture about surgery and tightness,
but as yet no one knows how to prove that vanishing contact homology implies
overtwistedness. Regardless, one can interpret the theorem as saying that there
is an inﬁnite hierarchy of “degrees of tightness,” in which some tight contact
manifolds are tighter than others. There are examples to show that the inclusions
Ξk 3→Ξk−1 are all proper (see below).
There are also candidates that might
belong to Ξ∞without being ﬁllable, but no proof of this as yet.
The classes Ξk are deﬁned in terms of a contact invariant that lives in the
Symplectic Field Theory outlined by Eliashberg, Givental and Hofer. The version
of SFT we are interested in is, roughly speaking, the homology of a chain complex
HSFT
∗
(M, ξ) := H∗(A[[ℏ]], DSFT) ,
where A is a free graded commutative algebra with unit, with generators qγ cor-
responding to closed Reeb orbits γ on (M, ξ), ℏis a formal variable, and
DSFT : A[[ℏ]] →A[[ℏ]]
is a linear operator that encodes a count of rigid pseudoholomorphic curves in
the symplectization of (M, ξ), with cylindrical ends asymptotic to closed Reeb
orbits. This homology is functorial with respect to exact symplectic cobordisms:
in particular, whenever there exists an exact cobordism from (M−, ξ−) to (M+, ξ+),
it induces an R[[ℏ]]-module morphism
HSFT
∗
(M+, ξ+) →HSFT
∗
(M−, ξ−)
which maps [ℏk] 2→[ℏk] for all k ≥0. This property is especially useful in light of
the following hypothetical example: suppose that for some choice of suitable data,
the symplectization of (M, ξ) contains only one rigid pseudoholomorphic curve,
which has genus 0, no negative ends and positive ends approaching a set of k
distinct Reeb orbits γ1, . . . , γk. Then it turns out that
DSFT (qγ1 . . . qγk) = ℏk−1,
38
Oberwolfach Report 28/2012
hence the element [ℏk−1] vanishes in HSFT
∗
(M, ξ). Among other things, this implies
that (M, ξ) cannot have an exact symplectic ﬁlling, as [ℏk] is nontrivial in HSFT
∗
(∅)
for every k ≥0.
With this example in mind, we deﬁne a numerical invariant, called the order of
algebraic torsion, by
AT(M, ξ) = sup{k ≥0 | [ℏk−1]̸ = 0 ∈HSFT
∗
(M, ξ)} ∈{0, 1, 2, . . ., ∞},
and then deﬁne (M, ξ) to be in Ξk if and only if AT(M, ξ) ≥k. It follows imme-
diately from the properties described above that if (M, ξ) ∈Ξk and there is an
exact cobordism from (M, ξ) to (M ′, ξ′), then (M ′, ξ′) ∈Ξk; in particular this is
true whenever the latter is obtained from the former by Legendrian surgery, since
Stein cobordisms are always exact.
To ﬁnd interesting examples of contact 3-manifolds with varying orders of al-
gebraic torsion, one needs a source of existence and uniqueness results for holo-
morphic curves. One such source is the relationship between Lefschetz ﬁbrations
and a certain generalization of open book decompositions. To motivate the idea,
consider a Lefschetz ﬁbration Π : E →Σ whose base and generic ﬁber are both
compact oriented surfaces with nonempty boundary. The boundary of E then has
two smooth faces ∂E = ∂hE ∪∂vE, which each inherit ﬁbrations
∂hE :=
'
z∈Σ
∂Ez →Σ
∂vE := E|∂Σ →∂Σ ∼= S1 ⊔. . . ⊔S1.
In the simplest example, if Σ is a disk, then the resulting decomposition of ∂E can
be viewed as an open book decomposition, with ∂hE as a tubular neighborhood
of the binding.
More generally, we deﬁne a spinal open book on a closed oriented 3-manifold M
to be a decomposition of the form M = MΣ∪MP , where the two pieces (called the
spine and paper respectively) both come with ﬁbrations: the ﬁbers of MP →S1
are surfaces with boundary, the connected components of which are called pages,
while ﬁbers of MΣ →Σ are circles, with Σ being a compact oriented surface with
boundary, the connected components of which are called vertebrae. We require
additionally that the boundary of every page should be a disjoint union of ﬁbers
of the spine. We then say that a contact structure ξ is supported by the spinal
open book if it admits a contact form α such that dα is positive on the interiors
of all pages and the ﬁbers on MΣ are closed Reeb orbits.
It’s important to note that in these deﬁnitions, neither Σ nor the ﬁbers of
MP →S1 need be connected, so there can be multiple vertebrae and multiple
families of pages with varying topological types, though in the speciﬁc example of
the boundary of a Lefschetz ﬁbration, this does not happen. Indeed, most spinal
open books cannot be boundaries of Lefschetz ﬁbrations, and this observation
becomes very powerful in light of the following joint result with Sam Lisi and
Jeremy Van Horn-Morris:
Invariants in Low-Dimensional Topology and Knot Theory
39
Theorem 2 ([2]). Suppose (M, ξ) is supported by a spinal open book containing a
page of genus 0. Then the symplectic ﬁllings of (M, ξ) (up to symplectic deforma-
tion equivalence) are in one-to-one correspondence with the Lefschetz ﬁbrations (up
to diﬀeomorphism) that restrict to the given spinal open book at their boundaries.
This generalizes a result in [3] which covers the case Σ = D2. The main reason
such results hold is that spinal open books always give rise to holomorphic curves:
in general, one can choose data such that each genus g page of a spinal open book
lifts to a holomorphic curve of index 2 −2g in the symplectization, so for the case
g = 0, these curves have the “expected” dimensions and can be extended to a
family of holomorphic curves foliating any given ﬁlling. Alternatively, the genus 0
pages in the symplectization can be counted in order to compute SFT, giving rise
to the following:
Theorem 3 ([2]). Suppose (M, ξ) is supported by a spinal open book containing a
page of genus 0 with k+1 boundary components, and also a page of positive genus.
Then [ℏk] = 0 ∈HSFT
∗
(M, ξ).
The simplest examples are S1-invariant contact structures on manifolds of the
form S1 ×Σ, where Σ is a closed oriented surface. In this case the surfaces {∗}×Σ
are convex, and the above theorem applies for instance if the dividing set consists
of k + 1 curves cutting Σ into two pieces, of which one has genus 0 and the other
does not. It is shown in [1] that this contact manifold satisﬁes AT = k, hence it
belongs to Ξk \ Ξk+1.
References
[1] J. Latschev and C. Wendl, Algebraic torsion in contact manifolds, Geom. Funct. Anal. 21
(2011), no. 5, 1144–1195. With an appendix by M. Hutchings.
[2] S. Lisi, J. Van Horn-Morris and C. Wendl, On symplectic ﬁllings of spinal open book de-
compositions, in preparation.
[3] C. Wendl, Strongly ﬁllable contact manifolds and J-holomorphic foliations, Duke Math. J.
151 (2010), no. 3, 337–384.
