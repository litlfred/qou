---
doc_id: arxiv-1305.7175v4
doc_title: "NONLINEAR TRACES"
section_id: sec-006-31-preliminaries
section_title: "Preliminaries"
section_number: 3.1
pages: 16-17
source_pdf: 1305.7175v4.pdf
source_sha256: 5a09955f4fb6a57e
doc_brief: "NONLINEAR TRACES — W e combine the theory of traces in homotopical algebra with s heaf theory in de- rived algebraic geometry to deduce general ﬁxed point and ch aracter formulas."
---
by J. Lurie [L1, L2, L4], see Chapter I.1 of [GR2] for an excellent over view.
Throughout what follows, we will ﬁx once and for all a symmetric mono idal (∞, 2)-categoryA
with unit object 1 A. By forgetting non-invertible 2-morphisms we obtain a symmetric mo noidal
(∞, 1)-category f (A), which we will abusively refer to as A whenever only invertible higher
morphisms are involved. Conversely, given a symmetric monoidal ( ∞, 1)-categoryC, we can
always regard it as a symmetric monoidal (∞, 2)-categoryi(C) with all 2-morphisms invertible. 5
5One can understand the above two operations as forming an adj oint pair ( i, f ).
NONLINEAR TRACES 17
Thus developments for higher ∞-categories equally well apply to the more familiar ( ∞, 1)-
categories. In what follows, noninvertible 2-morphisms only play a sig niﬁcant role starting with
Section 3.4.
We will use ⊗ to denote the symmetric monoidal structure of A. We will write Ω A =
EndA(1A) for the “based loops” in A, or in other words, the symmetric monoidal ( ∞, 1)-
category of endomorphisms of the monoidal unit 1 A. Note that the monoidal unit 1 Ω A is
nothing more than the identity id 1A of the monoidal unit 1 A.
Example 3.1 (Algebras). Fix a symmetric monoidal ( ∞, 1)-categoryC, and let A = Alg(C)
denote the Morita (∞, 2)-category of algebras, bimodules, and intertwiners of bimodules within
C. The forgetful map A = Alg(C)→C is symmetric monoidal, and in particular, the monoidal
unit 1 A is the monoidal unit 1 C equipped with its natural algebra structure. Finally, we have
ΩA≃C .
For a speciﬁc example, one could take C = k-mod = dgVect k the (∞, 1)-category of com-
plexes of k-modules (with quasi-isomorphisms inverted). Then A = Alg(C) is the ( ∞, 2)-
category of k-algebras, bimodules, and intertwiners of bimodules.
Example 3.2 (Categories). A natural source of ( ∞, 2)-categories is given by various theories
of (∞, 1)-categories. For example, one could consider dgCatk, the (∞, 2)-category of k-linear
stable presentable∞-categories (ork-linear presentable dg categories), k-linear continuous func-
tors, and natural transformations.
Observe that Alg( k-mod) is a full subcategory of dgCatk, via the functor assigning to a
k-algebra its stable presentable ∞-category of modules. The essential image consists of dg
categories admitting a compact generator.
