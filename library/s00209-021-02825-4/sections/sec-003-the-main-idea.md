---
doc_id: s00209-021-02825-4
doc_title: "A representation theoretic explanation of the Borcea–Brändén characterization"
section_id: sec-003-the-main-idea
section_title: "The main idea"
section_number: null
pages: 3-4
source_pdf: s00209-021-02825-4.pdf
source_sha256: 85ca5ec21f42a988
toc_source: outline
doc_brief: "A representation theoretic explanation of the Borcea–Brändén characterization — In 2009, Borcea and Brändén characterized all linear operators on multivariate polynomials which preserve the property"
---
A major purpose of this paper is to explain a certain conceptual thread in the history of
polynomial stability theory: that it is often possible to determine general stability information
from restricted sets of polynomials. For example, the Pólya-Schur and Borcea–Brändén
characterizations derive from a single polynomial (i.e., the symbol) stability properties of a
whole collection of polynomials in the output of a given linear operator. Additionally, the
Grace–Walsh–Szeg˝o coincidence theorem says that stability information of any polynomial
can be determined from its polarization, which is of degree at most one in each variable.
As it turns out, these sorts of phenomena can be explained using relatively basic algebraic
and representation theoretic concepts. We view Cn[x] as a representation of SL2(C) via the
standard action, given as follows. For φ ∈SL2(C) and f ∈Cn[x], we deﬁne:
(φ · f )(x) := f (φ−1x)
Here φ−1 acts on x ∈C as a Möbius transformation, or equivalently φ acts on the roots of f .
(Similarly, Cλ[x1, . . . , xm] can be viewed as a representation of (SL2(C))m via this action
in each variable.) Under this interpretation, important maps like polarization, projection, the
apolarity form, and even the symbol turn out to be invariant under these SL2(C) actions. This
leads us to a conceptual thesis: SL2(C)-invariant maps transfer stability information.
The goal of this paper is then to explicate and answer the most important question related
to this thesis: what does it mean for the symbol map to be SL2(C)-invariant and how does
it transfer stability information? To answer this, we consider the following standard ideas
relating spaces of linear operators to tensor products.
Let W1, W2 be two ﬁnite dimensional representations of a group G, and let Hom(W1, W2)
denote the space of linear maps from W1 to W2. Then, Hom(W1, W2) ∼= W ∗
1 ⊠W2 (the outer
1362
J. Leake
tensor product) can viewed as a representation of G × G. If we further have a G-invariant
bilinear form on W1, then we also have W1 ∼= W ∗
1 . This leads to the following identiﬁcation:
Hom(W1, W2) ∼= W ∗
1 ⊠W2 ∼= W1 ⊠W2
If W1 and W2 are spaces of polynomials, each in m variables, then their tensor product
W1 ⊠W2 is isomorphic to a larger space of polynomials in 2m variables. That is, a linear
operator between polynomial spaces W1 and W2 can be associated to some polynomial in
double the variables, via the above identiﬁcation of representations. This is precisely the idea
of the symbol of an operator.
Let’s see how this works in the univariate case. Consider Cn[x] as a representation of
the group SL2(C), as described above. It is then a standard result that the classical bilinear
apolarity form is invariant under the action of Möbius transformations. That is, the apolarity
form is an SL2(C)-invariant bilinear form on Cn[x]. This form, applied to f , g ∈Cn[x] with
coefﬁcients fk, gk, is deﬁned as follows:
⟨f , g⟩n :=
n

k=0
n
k
−1
(−1)k fkgn−k
With this, we obtain the identiﬁcation described above: Hom(Cn[x], Cm[x]) ∼= Cn[x] ⊠
Cm[x] ∼= C(n,m)[x, z]. The ﬁnal piece of the puzzle is then to ﬁnd a way to transfer stability
information through this identiﬁcation of representations. The key result to this end is the
classical Grace’s theorem:
Theorem [8] Let f , g ∈Cn[x] be polynomials of degree exactly n. Further, let C be some
open or closed circular region such that f is C-stable and g is (C\C)-stable. Then, ⟨f , g⟩n̸ =
0.
That is, the apolarity form not only provides the link between a linear operator and its
symbol, but also captures stability information. So, whatever stability claims we can make
about polynomials in C(n,m)[x, z] can then be seamlessly transferred to corresponding linear
operators in Hom(Cn[x], Cm[x]). From this we are able to recover the Borcea–Brändén
characterization. Additionally, all of the theory here relating stability and the representation
theory of SL2(C) can be generalized to multivariate polynomials in a straightforward manner.
The details will be discussed in Sect. 3.
In a similar fashion, other important maps also have SL2(C)-invariance properties (e.g.,
polarization and projection, as used in the Grace–Walsh–Szeg˝o coincidence theorem, explic-
itly give the isomorphisms of a classical representation theoretic result; see Appendix B). A
main feature of our conceptual thesis is that it allows for a uniﬁcation of many seemingly
related results in polynomial stability theory. A crucial point to make then is that Grace’s
theorem is at the heart of this uniﬁcation. That said, a signiﬁcant portion of this paper is
devoted to discussing it.
