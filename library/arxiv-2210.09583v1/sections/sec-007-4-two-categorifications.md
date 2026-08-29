---
doc_id: arxiv-2210.09583v1
doc_title: "A NEW PRESENTATION OF THE osp(1|2)-POL YNOMIAL LINK INVARIANT"
section_id: sec-007-4-two-categorifications
section_title: "Two Categorifications"
section_number: 4
pages: 12-13
source_pdf: 2210.09583v1.pdf
source_sha256: 38fc6fa465a06a7b
doc_brief: "A NEW PRESENTATION OF THE osp(1|2)-POL YNOMIAL LINK INVARIANT — There is a known connection between the osp(1|2n) polynomial knot invariant J n K and the so(2n + 1) knot invariant soJ n K studied by"
---
As we know from [ 10, 4], the osp(1|2) polynomial (and hence our invariant ˆJ) is practically identical
to the Jones polynomial. Now that we have this Kauﬀman-bracket ty pe deﬁnition of ˆJ , it should not
come as much of a surprise that one can categorify this invariant us ing a homology theory that is
practically identical to Khovanov homology. Indeed, we show in this s ection that one can repeat the
construction of Khovanov homology seen in [ 3] but where an extra /CI
4-grading is attached to everything
to get a categoriﬁcation. We then construct a /CI × /CI
4-graded version of Putyra’s covering Khovanov
homology [ 28] in a similar fashion.
Notation 4.1. An ”e-graded” object refers to an object with a /CI × /CI
4-grading.
For example, an e-graded vector space is a /CI × /CI
4-graded vector space.
Deﬁnition 4.2. Let egV ec be subcategory of V ect consisting of /CI × /CI
4-graded vector spaces and
degree-preserving linear maps.
This is a symmetric monoidal category with the same braiding as V ect. The tensor product of
linear maps is given by ( f ⊗ g)(v ⊗ w) = f (v) ⊗ g(w). We bring this example up to emphasize that the
/CI
4-grading doesn’t impact the tensor product of linear maps or the br aiding like the /CI
2-grading does
for superspaces. For the remainder of the paper, we choose to w ork with modules instead of vector
spaces.
An e-graded module M over a e-graded ring R is a /CI × /CI
4-graded R-module such that R(a,b)M(x,y) ⊂
M(x+a,y+b). We refer to the degree of a homogeneous element in some e-grade d module with deg(−)
for the rest of the paper.
Deﬁnition 4.3. The category of e-graded R-modules R-emod is the subcategory of R-mod whose ob-
jects are e-graded R-modules and whose morphisms are degree preserving R-module homomorphisms.
For our discussion on Khovanov homology, we set R = /CI (concentrated in degree (0 , 0)).
Deﬁnition 4.4. Let W = ⨁
(m,n)∈ /CI × /CI
4
Wm,n be a e-graded R-module with homogeneous components
Wm,n. The graded dimension of W is the power series dim q,τ (W ) =∑
m,n qmτ ndim(Wm,n). When W
is ﬁnite dimensional, this lies in /CI
τ [q, q−1].
Deﬁnition 4.5. Let W =⨁ Wm,n as before. Then deﬁne {(a, b)} to be the degree shift. That is, we
set W {(a, b)}(m,n) = W(m−a,n−b) so that dim q,τ W {(a, b)} = qaτ bdimq,τ W .
A NEW PRESENTATION OF THE osp(1|2)-POLYNOMIAL LINK INV ARIANT AND CATEGORIFICATION 13
Let 2Cob denote the category of 2D-cobordisms Cob 3(∅) from [ 3]. The objects are closed 1-
dimensional manifolds (collections of circles), and the morphisms are given by 2-dimensional cobordisms
between these collections of circles up to boundary preserving isot opies. We also use the grading con-
ventions in [ 3, Section 6], which tell us that the degree of a cobordism W : Σ 1{m} → Σ 2{n} is given
by χ(W ) + n − m. We will later attach an additional /CI
4-grading to this category.
