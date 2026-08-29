---
doc_id: arxiv-math-0203060v11
doc_title: "ON FUSION CATEGORIES"
section_id: sec-021-57-surjective-and-injective-functors
section_title: "Surjective and injective functors"
section_number: 5.7
pages: 20-21
source_pdf: 0203060v11.pdf
source_sha256: fa7e21ceab3e9933
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in pa rtic- ular, the theory of weak Hopf algebras), we prove a number of g eneral results about fusion categories in"
---
F : C → D be a unital tensor functor.
We will say that F is injective if it is fully faithful (in this case F identiﬁes C
with a full tensor subcategory of D). We will say that F is surjective if any simple
object X of D is contained in an object of the form F (T ),T ∈ C . If F is surjective
and C,D are indecomposable, then D is said to be a quotient category of C.
Now let M be a faithful module category over D. Then it is also a faithful
module category over C. Let R be a semisimple algebra with blocks labeled by
simple objects of M, and G the corresponding ﬁber functor D → R-bimod. Let
A = Endk(G), B = Endk(G ◦F ) be the corresponding weak Hopf algebras. Then
the functor F induces a morphism of weak Hopf algebras φF : A → B, and vice
versa. It is easy to check that F is surjective, respectively injective if and only if
φF is injective, respectively surjective.
ON FUSION CATEGORIES 21
Let us now consider the corresponding dual categories C∗, D∗ (we will drop the
subscript M, since the only module category we will consider in this subsection will
be M). We have a natural dual functor F ∗ : D∗ → C ∗, since any D-linear functor
Φ : M → M has a natural C-linear structure, deﬁned using F . It is clear that the
morphism φF ∗ :B∗ →A∗ is given by φF ∗ =φ∗
F .
Proposition 5.3. Let F : C → D be a unital tensor functor between multi-fusion
categories. If F is surjective (injective) then F ∗ is injective (surjective).
Proof. The claim is equivalent to the statement that surjectivity of φF is equivalent
to injectivity of φ∗
F , and vice versa, which is obvious. □
