---
doc_id: s00209-021-02825-4
doc_title: "A representation theoretic explanation of the Borcea–Brändén characterization"
section_id: sec-004-a-generalized-graces-theorem-and-interval--and-r
section_title: "A generalized Grace's theorem and interval- and ray-rootedness"
section_number: null
pages: 4-5
source_pdf: s00209-021-02825-4.pdf
source_sha256: 85ca5ec21f42a988
toc_source: outline
doc_brief: "A representation theoretic explanation of the Borcea–Brändén characterization — In 2009, Borcea and Brändén characterized all linear operators on multivariate polynomials which preserve the property"
---
In [2], Borcea and Brändén are able to prove a multivariate Grace’s theorem using their
operator characterization. In this paper we will prove the multivariate version from scratch,
and then use it to derive a new characterization of stability-preserving linear operators. In
addition, we generalize it to projectively convex regions, which consist of an open circular
region with a portion of its boundary (see Sect. 4.2). We state our new result as follows.
A representation theoretic explanation...
1363
Note that this result can be seen as an extension of the generalized Grace’s theorem given in
Corollary 4.4 of [17].
Theorem 5.1 Fix λ ∈Nm
0 and f , g ∈Cλ[x1, . . . , xm] such that f and g both have a nonzero
term of degree λ. Also, denote C := H+ ∪R+ and 
C := H−∪R−. If f is Cm-stable and g
is 
Cm-stable, then ⟨f , g⟩λ̸ = 0.
This result can, for instance, give stability information about positive- and negative-rooted
polynomials. Since the apolarity form is invariant under the action of Möbius transformations,
we immediately obtain similar statements regarding the union of any open circular region and
a portion of its boundary. Notice also that, unlike the classical Grace’s theorem, the stability
regions C and 
C have non-empty intersection.
In the vein of this extension, we provide a new characterization of a certain class of linear
operators which preserve ray- and interval-rootedness. The problem of classifying all such
operators is still open in general (see e.g., the end of [3]). Here, we solve this problem for
a restricted class of operators: namely, operators which both preserve weak real-rootedness
and also preserve ray- or interval-rootedness. Our main result in this direction is stated as
follows, where a polynomial is called J-rooted when all of its roots are in J:
Theorem 7.8 Fix a linear operator T : Rn[x] →Rm[x] which has image of dimension
greater than two. Further, let I, J ⊆R be intervals or rays. Up to certain degree restric-
tions, T preserves weak real-rootedness and maps I-rooted polynomials to nonzero J-rooted
polynomialsifandonlyifSymb(T )iseither(H−∪I)×(H+\J)-stableor(H−∪I)×(H−\J)-
stable.
In Sect. 7.4, this result is stated in a more restricted manner as the degeneracy condition
(image dimension) and degree restrictions end up being more tedious than in the other results.
Corollary 7.9 and further explication then give the result as stated here.
As a ﬁnal note, all of the results given here in the introduction are stated slightly differently
in Sects. 5, 6, 7. In particular, the notation V (λ) is used in place of Cλ[x1, . . . , xm], and
reference is made to CP1 (i.e., the Riemann sphere). This notation has to do with consideration
of “roots at inﬁnity”, which allows us to remove degree restrictions and avoid reference to
convex circular regions. We discuss this rigorously in Sect. 2.2.
