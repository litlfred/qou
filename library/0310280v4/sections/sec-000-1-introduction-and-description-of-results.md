---
doc_id: 0310280v4
doc_title: "Stabilization in the braid groups II: Transversal simplicity of knots JOAN S BIRMAN WILLIAM W MENASCO The main result of this paper is a negative answer to the question: are all tr"
section_id: sec-000-1-introduction-and-description-of-results
section_title: "Introduction and description of results"
section_number: 1
pages: 1-4
source_pdf: 0310280v4.pdf
source_sha256: 1e146ee4ebc157f2
doc_brief: "Stabilization in the braid groups II: Transversal simplicity of knots JOAN S BIRMAN WILLIAM W MENASCO The main result of this paper is a negative answer to the question: are all transversal — 9 sectio"
---
This paper is about knots which are transverse to the standard tight contact structure in
R3, and about the ways in which topological information about braids can be used to
learn new things about these ‘transversal knots’. Our approach to contact topology had
its origins in the foundational paper of D Bennequin [2]. The results in this paper are
direct outgrowths of our work on the Markov Theorem without Stabilization (MTWS)
[6].
A knot in oriented R3 is the image X of an oriented circle S1 under a smooth embedding
e : S1→ R3. Viewing S3 as R3∪∞ , we also can think of X as being a knot in S3.
The topological knot typeX of X is its equivalence class under smooth isotopy of
the pair ( X, S3). A representative X∈X is said to be a closed braid if there is an
unknotted curve A⊂ (S3\ X), the axis, and a choice of ﬁbration H of the open solid
torus S3\ A by meridian discs{Hθ; θ∈ [0, 2π)} which we call ﬁbers, such that X
intersects every disc ﬁber Hθ transversally. We call the pair (H, A) a braid structure on
R3. If we regard A as the z–axis in R3 and the ﬁbers of H as half-planes through A,
there are natural cylindrical coordinates (ρ,θ, z), θ∈ [0, 2π) in R3. Parameterizing
X by (ρ(t),θ (t), z(t)), t∈ [0, 2π), X will be a closed braid ifρ(t)> 0 and dθ/dt> 0
at every point (ρ(t),θ (t), z(t))∈ X. See Figure 1(a), where two half-planes and two
fragments of a closed braid X are depicted. A braid isotopy of a closed braid is an
isotopy that is transverse to the braid ﬁbration and in the complement of the axis. The
braid isotopy type of the closed braid X is its equivalence class under braid isotopy.
Published: 4 October 2006 DOI: 10.2140/gt.2006.10.1425
1426 Joan S Birman and William W Menasco
z z z
(a) (b)
X
X
Hθ1
Hθ2
Figure 1: (a) Braid structure on R3 ; (b) 2–planes in the standard contact structure on R3 .
Note that these 2–planes are invariant under rotation about z–axis and translation along the
z–axis (which we use as the braid axis A).
Using the same cylindrical coordinates, the standard tightcontact structureξ in oriented
R3 is the kernel of the 1–formα =ρ2dθ + dz. Thinking of ξ as attaching a 2–plane
to each point in R3, Figure 1(b) shows some of the 2–planes associated to α, for
comparison of the braid structure and the contact structure. The ﬁeld of 2–planes
so-obtained is nowhere integrable.
An oriented knot X in contact R3 is said to be transverse if it is everywhere transverse
to the plane ﬁeld of the standard contact structure. Parameterizing X as before, a closed
braid X is transverse if and only if dθ/dt>−z′(t)/(ρ(t))2 for every t∈ [0, 2π]. We
use the symbol TX to denote a transversal knot. (For most of our discussion TX will
be transversal because it will also be a braid with respect to the z–axis.) Deﬁne two
transverse knots to be transversally isotopic if there is an isotopy h : R3× I→ R3
such that hs(X) = h(X, s)⊂ R3 is transversal for every s∈ I. The transversal knot
typeTX of a transverse knot TX is its equivalence class under transversal isotopy. An
obvious invariant of a transverse knot type is its topological knot type [TX ]top =X .
In his seminal paper [2], Bennequin showed that braids could be useful for the study
of contact structures on S3 or R3. Recently that idea was generalized by E Giroux
[11], who showed that open book decompositions of arbitrary 3–manifolds M3 might
be equally important for the study of contact structures on other 3–manifolds. Since
an open book structure on a 3–manifold generalizes our braid structures on R3, this
suggests that our work in this paper could have applications to the study of tight contact
structures on other 3–manifolds. Bennequin proved that every transversal knot is
transversally isotopic to a closed braid, and he discovered a very important numerical
invariantβ(TX ) (the Bennequin invariant) of transversal knot type which is natural
Geometry &Topology 10 (2006)
Stabilization in the braid groups II 1427
in the braid setting. To compute it when TX is also a closed braid having the z–axis
as it axis A, consider a regular projection of TX onto the plane z = 0. Let e(TX) be
the the algebraic crossing number of TX at the pre-images of the double points in the
projection. Let b(TX) be the braid index of TX, ie, its geometric linking number with
A. Then β(TX ) = e(TX)− b(TX). Note that both e(X) and b(X) are invariants of
braid isotopy, and thereforeβ is well-deﬁned on any closed braid, ie, the closed braid
need not represent a transversal knot type, and invariant under braid isotopy. Using
topological techniques Bennequin showed that for a ﬁxed topological knot typeX , the
integerβ has an upper but not a lower bound. While β(X) is well-deﬁned on closed
braids, it is not an invariant of X . Indeed, each topological knot type X includes
inﬁnitely many distinct transversal knot typesTX .
Are there other invariants of TX in addition to [TX ]top and β(TX )? A hint that
the problem might turn out to be quite subtle was in the paper [ 10] by Fuchs and
Tabachnikov, who proved that while ragbags ﬁlled with invariants of transversal knot
typesTX exist, based upon the work of V .I. Arnold in [1], they are all determined
by [TX ]top and β(TX ). Thus, the seemingly new invariants that many people had
discovered by using Arnold’s ideas were just a fancy way of encoding [TX ]top and
β(TX ). This lead to a deﬁnition: a transversal knot type TX is transversally simple if
it is determined by [TX ]top andβ(TX ).
In [7] purely topological techniques were used to give a purely topological restriction
onX which would insure that any associatedTX is transversally simple. This paper
begins where the work in [ 7] ended. Our main result is to answer the question of
whether all transversal knot types are transversally simple in the negative, by giving
an explicit inﬁnite family of examples of closed 3–braids that deﬁne transversal knot
types that are not transversally simple. Our methods are topological and indirect and
utilize the main result in [6]. After a draft of this paper was posted and submitted for
publication, Etnyre and Honda proved the existence of examples, although they could
not make them explicit [9]. Their methods, very different from ours, are based upon
techniques in contact topology.
Here is a guide to this paper. In Section 2.1 we discuss our terminology and state
Theorem 1, a simpliﬁed version of the MTWS. The full statement, and the proof, are to
be found in [6]. In Section 2 our work is directed toward the proof of Theorem 2, a
version of Theorem 1 which holds in the special case of links that are 3–braids, in the
transversal setting. In Theorem 3 of Section 3 we give our promised inﬁnite sequence
of pairs of closed 3–braids that deﬁne transversal knots types that are not transversally
simple, and prove that they have the properties that we claim they have.
Acknowledgments We thank Keiko Kawamuro for her careful reading of both [ 6]
Geometry &Topology 10 (2006)
1428 Joan S Birman and William W Menasco
and this paper. We also thank Hiroshi Matsuda for his very careful reading of an earlier
version of this paper, which turned up an error. We had claimed that a certain template
had braid index 6, but he showed that it had a closed 5–braid representative. The
example, and all results that depended upon it, have been removed.
The ﬁrst author acknowledges partial support from the following sources: the US
National Science Foundation, under Grants DMS-9402988, 9705019, 9973232 and
0405586. The second author acknowledges partial support from the following sources:
the U.S. National Science Foundations,under grants DMS-9200881, DMS-9626884
and DMS-0306062 ; and the Mathematical Sciences Research Institute, where he was a
Visiting Member during winter/spring of 1997.
