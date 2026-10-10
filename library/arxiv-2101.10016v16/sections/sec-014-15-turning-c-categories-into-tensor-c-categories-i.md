---
doc_id: arxiv-2101.10016v16
doc_title: "Unitary coboundary weak quasi-Hopf algebras in the Kazhdan-Lusztig-Finkelberg theorem"
section_id: sec-014-15-turning-c-categories-into-tensor-c-categories-i
section_title: "Turning C*-categories into tensor C*-categories, I"
section_number: 15
pages: 109-114
source_pdf: 2101.10016v16.pdf.txt
source_sha256: 51d21209730be025
toc_source: inferred
doc_brief: "Unitary coboundary weak quasi-Hopf algebras in the Kazhdan-Lusztig-Finkelberg theorem — We construct, for every complex simple Lie algebra g and every positive integer level k, a unitary modular"
---
15. Turning C
∗
-categories into tensor C
∗
-categories, I
The problem of constructing unitary tensor categories is of great importance in connection with the study of fusion categories from quantum groups at roots of unity or conformal
field theory. In the former setting, a natural ∗-structure was introduced by Kirillov [111]
for certain even roots of unity, and unitarity was shown by Wenzl and Xu [185, 193]. A
tensor category is called unitarizable if it is tensor equivalent to a tensor C
∗
-category. We
have observed in Remark 12.11 that examples of non-unitarizable fusion categories from
quantum groups and certain roots of unity are known.
We start with the following setting, which will be called condition a).
a) Let C be a tensor category (resp. a braided tensor category) and C
+ a C∗
-category,
and assume that we have an equivalence of linear categories
F : C
+ → C.
Assuming that every object of C
+ is a finite direct sum of irreducible objects, we wish to
use F to upgrade C
+ to a tensor C∗
-category (resp. a braided tensor C
∗
-category with
unitary braided symmetry).
In this section we discuss a result which characterizes when a solution exists and is
unique.
We shall derive three main applications. The first one is the proof that Beilinson-FeiginMazur category O˜
ℓ
is a braided tensor C
∗
-category with unitary braided symmetry, and is
presented in Theorem 21.2. The second is the explicit construction of a similar structure
on the module category of the affine vertex operator algebra Vgkendowed with HuangLepowsky braided tensor category structure, see Theorem 23.10. A third application a
positive answer to a question posed by Galindo in [66] on uniqueness of unitary tensor
structures on tensor categories, Theorem 2.2.
A variant of the abstract results of this section will be useful in Sect. 28, 30, 32 were unitary weak quasi-Hopf algebras will be constructed with a direct method from the braiding
for certain general ribbon categories and in particular for those arising from the quantum
groups at roots of unity.
Definition 15.1. Let F : C
+ → C satisfy a). We shall say that the tensor structure
(resp. the braided tensor structure) of C is transportable compatibly with the C
∗
-structure,
or simply C
∗
-transportable to C
+ if C+ can be upgraded to a tensor C∗
-category (resp. a
braided tensor C
∗
-category with unitary braided symmetry) in such a way that F : C
+ → C
becomes a tensor equivalence (resp. a braided tensor equivalence).
We note that C
∗
-transportability will be possible only in certain circumstances. For
example, if C is a finite semisimple tensor category then we know that C is tensor equivalent
to some Rep(A), with A a semisimple weak quasi bialgebra. Since A admits the structure
of a C
∗
-algebra, the C
∗
-category C
+ of C∗
-representations of A satisfies a). On the other
hand, if C is not tensor equivalent to a tensor C
∗
-category, see Remark 12.11, then C
+ does
not admit any tensor C
∗
-structure that makes it tensor equivalent to C.

110 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
We shall describe two main classes of tensor categories for which the tensor structure
(resp. the braided tensor structure) are transportable compatibly with the C
∗
-structure,
and two upgrading of C
+ corresponding to a C∗
-transportable tensor structure of C provide
unitarily (braided) tensor equivalent tensor C
∗
-categories. The notion of weak quasi-Hopf
algebra will play a prominent role.
In the mentioned applications, C plays the role of a category of infinite dimensional representations of interest of some algebraic structure endowed with a ‘fusion’ tensor product,
and C
+ the category of unitary representations on Hilbert spaces. The functor F : C+ → C
is the functor which forgets the unitary structure. The assumption that it be an equivalence
means that every object of C can be made into a unitary representation, an assumption
which is known to hold in a variety of circumstances.
We thus see that the abstract problem in our formulation admits as applications that
of making representation categories of VOAs or of affine Lie which are known to have
the structure of linear C
∗
-categories, and the structure of (braided) tensor categories, into
tensor C
∗
-categories (with unitary braided symmetry).
Example 15.2. An example illuminating the general methodology, and useful for our
application, is obtained with C the Andersen fusion category of a quantum group Uq(g)
associated to a complex simple Lie algebra, with q = e
iπ/ℓ with ℓ divisible by d, the ratio
between the squared lengths of the longest to the shortest root, and ℓ/d > hˇ, the dual
Coxeter number of g.
In this case, Wenzl shows in the first part of [185] that C is a linear C
∗
-category in a
natural way. In the second part, that C is in fact a tensor C
∗
-category with unitary braided
symmetry. The second part is based on the construction of a positive inner product of a
fusion tensor product of two representations satisfying the extra axioms, and compatible
with the starting linear C
∗
-structure of the category.
A note on notation. Since we shall deal at the same time with semisimple linear or C
∗
or tensor categories, or braided tensor categories, and sometimes we shall use only part of
the structure, we shall use a suffix + on a category to denote that it is a C
∗
-category and
on a functor if it is ∗-preserving. The continuous arrow in a diagram denotes a (braided)
tensor equivalence, while the dashed arrows are linear equivalences. Thus, if only some of
the categories or equivalences carry a (braided) tensor structure, the commutativity of the
diagram is understood to hold at the level of linear functors.
Definition 15.3. Let F : C
+ → C be as in a). Let A be a discrete (quasitriangular) weak
quasi bialgebra endowed with an involution of pre-C
∗
-algebra, and consider, accordingly,
the (braided) tensor category Rep(A) and the C
∗
-category Rep+
(A). A triple (A, E
+, E)
constituted by a ∗-equivalence E
+ : C+ → Rep+
(A) and a (braided) tensor equivalence
E : C → Rep(A) will be called compatible with F if the following diagram commutes

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 111
C
+ Rep+
(A)
C Rep(A)
E
+
F FA
E
where FA : Rep+(A) → Rep(A) is the forgetful functor.
A compatible triple defines a weak dimension function on C via D(ρ) := dim(E
′
(ρ)),
where E
′
is the composite of E with the forgetful functor Rep(A) → Vec. We next see that
compatible triples may be constructed and classified under mild assumptions.
Proposition 15.4. If (A, E, E
+) is a compatible triple for F : C+ → C then for any twist
F ∈ A ⊗ A of the (quasitriangular) weak quasi bialgebra structure and any positive twist
t ∈ A of the ∗-involution, the twisted (quasitriangular) algebra AF,t is part of another
compatible triple with the same weak dimension function and they are all of this form.
Proof. The proof follows from Prop. 7.2, Theorem 7.9 and part of Prop. 13.1. The braided
case follows from considering part c) of Prop. 10.2 in addition. □
Remark 15.5. As we shall see, natural constructions in conformal field theory give rise
to canonically associated associative algebras A, the Zhu algebras, and also to linear functors E, which are already known to play an important role in the theory of VOAs. The
construction of compatible triples for these remarkable examples is our main motivation
in the definition.
Proposition 15.6. F : C
+ → C admits a compatible triple if and only if C admits an
integral weak dimension function.
Proof. The notion of a compatible triple (A, E, E
+) may equivalently be given via an abstract construction as follows. There is a canonical isomorphism of algebras ϕ : A →
Nat0(E
′
) which induces an isomorphism of categories ϕ∗ : Rep(Nat0(E
′
)) → Rep(A) such
that ϕ∗Ee′ = E, where Ee′: C → Rep(Nat0(E
′
)) is the equivalence arising from TannakaKrein reconstruction of E
′
. There is also an isomorphism of ∗-algebras A → Nat0(E
+′
).
The compatibility condition implies H(E
+)′ = E′F, with H : Hilb → Vec the forgetful
functor. These remarks together with Tannaka-Krein duality results imply that giving a
compatible triple is the same thing as giving a faithful ∗-functor E
+′
: C
+ → Hilb and a
faithful weak quasi-tensor functor E
′
: C → Vec such that E
′F = HE+′
. Now it suffices to
apply Theorem 7.9, 13.9.
□
Theorem 15.7. Let F : C
+ → C satisfy a). Assume that the (braided) tensor category
C admits a weak dimension function D, and let (A, E
+, E) be a compatible triple with
dimension D. Then the tensor structure of C is C
∗
-transportable to C
+ via F if and only
if A can be upgraded to a unitary (resp. quasitriangular) weak quasi bialgebra (resp. such
that the R-matrix of A satisfies the unitarity condition stated in Prop. 13.2). If this is
the case, the diagram defining the triple becomes a commuting diagram of (braided) tensor

112 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
equivalences and E
+ can be chosen unitary. Furthermore, any two tensor C∗
-completions of
C
+ obtained from a C∗
-transportable F yield unitary tensor equivalent tensor C
∗
-categories.
Proof. Following the proof of Prop. 15.6, and adopting the same notation, we shall identify
A with Nat0(E
+′
) as a ∗-algebra. If C
+ admits the structure of a tensor C∗
-category
over the underlying C
∗
-category such that F : C
+ → C becomes a tensor equivalence
then the composite of the left with the bottom equivalences in the diagram is a tensor
equivalence hence, by commutativity of the diagram, the composite of top with the right
equivalences C
+ → Rep+
(A) → Rep(A) is a tensor equivalence as well. On the other hand,
Rep(A) → Vec is a weak quasi-tensor functor, hence so is the composite C
+ → Rep+
(A) →
Rep(A) → Vec. But this functor factors through C
+ → Rep+
(A) → Hilb → Vec and
Hilb → Vec is both a forgetful functor and a tensor equivalence, and this implies that
E
+′
: C
+
→ Rep+(A) → Hilb is a (∗-preserving) weak quasi-tensor functor. It follows that
Nat0(E
+′
) can be made into a unitary weak quasi bialgebra and E
+ into a unitary tensor
equivalence by Theorem 13.5. This structure can be transferred to A, and therefore is
compatible with the given ∗-involution of A. It is now easy to see that it extends the given
weak quasi-bialgebra structure on A.
Conversely, if A admits the structure of a unitary weak quasi bialgebra with the given
∗
-structure then, by Corollary 12.6, Rep+(A) is a tensor C
∗
-category tensor equivalent to
Rep(A) and hence to C. The top equivalence of the diagram defining a compatible triple
acts from the linear category C
+ to the tensor category Rep+
(A). It is a general fact that
under this circumstance, C
+ can be made into a tensor category in such a way that E+ is
becomes a tensor equivalence. Indeed, given objects ρ, σ ∈ C
+, we define a tensor product
object ρ ⊗ σ in C
+
ρ ⊗ σ := S
+

E
+(ρ) ⊗ E+(σ)

,
and a tensor product morphism by a similar formula,
S ⊗ T := S
+

E
+(S) ⊗ E+(T)

.
Here S
+ : Rep+
(A) → C
+is an inverse equivalence of E+, Moreover, if α denotes the unitary
associator in Rep+(A) we define the morphisms
α
′
ρ,σ,τ : (ρ ⊗ σ) ⊗ τ → ρ ⊗ (σ ⊗ τ )
by
α
′
ρ,σ,τ :=
S
+(1E+(ρ) ⊗ η
−1
E+(σ)⊗E+(τ)
◦ αE+(ρ),E+(σ),E+(τ) ◦ ηE+(ρ)⊗E+(σ) ⊗ 1E+(τ)).
where η : E
+S+ → 1 is a natural transformation. Then, thanks to the fact that E+ is
∗
-preserving, S
+ may be chosen ∗
-preserving, η unitary by Prop. 4.16, and Rep+(A) is a
tensor C
∗
-category, it is immediate to check that that the relation (S ⊗ T)
∗ = S∗ ⊗ T∗
holds on morphisms and α
′
is unitary. This gives the C
∗
- tensor structure on C
+.
Moreover, E
+ becomes a tensor equivalence with unitary tensor structure Eρ,σ := η
−1
E+(ρ)⊗E+(σ)
.
Since the forgetful Rep+(A) → Rep(A) is a tensor equivalence as well with the trivial tensor

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 113
structure, it follows that F : C
+ → C has a unique tensor structure such that EF = FAE+
as tensor functors.
If in addition A is quasitriangular with R.matrix satisfying the stated unitarity condition
then Rep+(A) is a braided tensor category with unitary braided symmetry, let it be c. We
define a unitary natural transformation c
′
in C
+
c
′
(ρ, σ) = S
+(c(E+(ρ), E+(σ))).
It is straightforward to verify that this natural transformation satisfies the two hexagon
equations with respect to α
′
.
Uniqueness. Let us next consider a new tensor C
∗
-category C
′
coinciding with C
+ as
a C
∗
-category and making F into a new tensor equivalence F
′
. Applying the above construction in the opposite direction, that is with S
+ in place of E+, gives a new tensor
C
∗
-category structure to Rep+(A), denoted Rep′(A) and new unitary tensor equivalences
S
′
: Rep′(A) → C
′ and E′
: C
′ → Rep′
(A) coinciding with S
+ and E+ as functors, respectively. We obtain a new tensor structure on the identity functor FA : Rep′
(A) → Rep(A)
solving now the equation for the tensor structures obtained from EF′ = FAE
′
. This gives a
weak quasi-tensor structure to the forgetful functor Rep′(A) → Hilb, and therefore Rep′(A)
becomes unitarily tensorially equivalent to Rep+(A′) where A′is a new unitary weak quasibialgebra compatible with the original C
∗
-algebra A, thanks to Theorem 13.5. It follows
from Prop. 7.2 that A′ as a weak quasi-bialgebra is only varying by a twist of A. Therefore
Rep+(A′) is unitarily tensor equivalent to Rep+(A) by Prop. 12.8 and 12.9, and finally to
C
+.
□
It follows in particular from the previous characterization that if the tensor structure of
C is C
∗
-transportable to C
+ then C is tensor equivalent to a tensor C∗
-category, namely
Rep+(A). We next show more interestingly that the converse implication holds. The
following result will find important applications in the categories arising from affine vertex
operator algebras, Sect. 23.
Theorem 15.8. Let F : C
+ → C satisfy a) and assume that C admits a weak dimension
function (e.g. C is a finite semisimple (braided) tensor category). If C is (braided) tensor equivalent to a (unitarily braided) tensor C
∗
-category D+, then the (braided) tensor
structure of C is C
∗
-transportable to C
+ in a unique way up to unitary (braided) tensor
equivalence. Moreover in this way C
+ becomes unitarily (braided) tensor equivalent to D+.
Proof. Let D be a weak dimension function on C, and G : D+ → C a tensor equivalence.
Then D′(ρ) := D(G(ρ)) is a weak dimension function on D+ since G(ρ ⊗ σ) is isomorphic
to G(ρ)⊗G(σ) and D is isomorphism invariant. We may then construct a faithful ∗-functor
of C
∗
-categories D+ → Hilb corresponding to D′ and a weak quasi-tensor structure on the
composite D+ → Hilb → Vec. By the C
∗
-version of Tannaka-Krein duality, see Theorem
13.5, the algebra A of natural transformations of this functor becomes a unitary weak
quasi bialgebra, with a corresponding involutive structure (∗, Ω) and such that Rep+
(A)
is unitarily tensor equivalent to D+. Let G
′
: C → D+ be an inverse tensor equivalence
of G and let E be the composed tensor equivalence C → D+ → Rep(A) where the latter

114 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
functor is obtained from the duality theorem in the tensor linear case, see Theorem 7.6 (or
equivalently, forgetting the C
∗
-structure of A). We may then pick a factorisation of EF
through a ∗-equivalence E
+ : C+ → Rep+
(A) and the forgetful functor Rep+(A) → Rep(A)
by Prop. 13.9. Let † denote the corresponding involution on A. Since all pre-C
∗
-algebra
involutions of A are twisted from one another, we may find a twist t ∈ A, positive with
respect to ∗, such that t
† = t−1a∗
t. We may endow A with the twisted involutive structure (†
, Ωt) by Prop. 11.14 and obtain the complete structure and an associated tensor
C
∗
-category Rep+
t
(A). We have thus shown that (A, E
+, E) is a compatible triple for F
satisfying the necessary and sufficient condition of Theorem 15.7 of C
∗
-transportability.
Thus C
+ becomes a tensor C∗
-category unitarily tensor equivalent to Rep+
t
(A) and therefore to D+ by Prop. 13.1. In the special case that C is a finite semisimple tensor category,
it always admits a weak dimension function by Remark 17.4. In the braided case, the same
R-matrix satisfies the unitarity condition stated in Prop. 13.2 with respect to the twisted
involutive structure (†, Ωt), and therefore it makes Rep+
t
(A) into a unitarily braided tensor
category. We may apply the braided case of Theorem 15.7. □
