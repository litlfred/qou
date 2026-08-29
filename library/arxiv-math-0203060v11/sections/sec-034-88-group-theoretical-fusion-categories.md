---
doc_id: arxiv-math-0203060v11
doc_title: "ON FUSION CATEGORIES"
section_id: sec-034-88-group-theoretical-fusion-categories
section_title: "Group-theoretical fusion categories"
section_number: 8.8
pages: 39-40
source_pdf: 0203060v11.pdf
source_sha256: fa7e21ceab3e9933
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in pa rtic- ular, the theory of weak Hopf algebras), we prove a number of g eneral results about fusion categories in"
---
with integer Frobenius-Perron dimensions is the category C(G,H,ω,ψ ) associated
to quadruples ( G,H,ω,ψ ), where G is a ﬁnite group, H is a subgroup, ω ∈
Z 3(G, C∗) is a 3-cocycle, ψ ∈ C2(H, C∗) a 2-cochain such that dψ = ω|H (see
[O1]). Namely, let Vec G,ω be the category of ﬁnite dimensional G-graded vec-
tor spaces with associativity deﬁned by ω. Let Vec G,ω(H) be the subcategory of
VecG,ω of objects graded by H. Consider the twisted group algebra A = Cψ[H].
Since dψ =ω|H, it is an associative algebra in this category. Then C(G,H,ω,ψ ) is
deﬁned to be the category of A-bimodules in VecG,ω.
Remark 8.39. If (ω′,ψ ′) is another pair of elements such that ω′ =ω +dη,ψ ′ =
ψ +η|H +dχ, η ∈ C2(G, C∗), χ ∈ C1(H, C∗), then C(G,H,ω,ψ ) is equivalent
to C(G,H,ω ′,ψ ′). Thus, the categories C(G,H,ω,ψ ) are parametrized by the set
S(G,H ) of equivalence classes of pairs ( ω,ψ ) under the above equivalence, which
is a ﬁbration over Ker( H 3(G, C∗) → H 3(H, C∗)) with ﬁber being a torsor over
Coker(H 2(G, C∗) →H 2(H, C∗)).
Deﬁnition 8.40. A fusion category is said to be group-theoretical if it is of the
form C(G,H,ω,ψ ).
40 PA VEL ETINGOF, DMITRI NIKSHYCH, AND VIKTOR OSTRIK
Remark 8.41. We note that there may be more than one way to represent a given
fusion category in the form C(G,H,ω,ψ ). In particular, G is not uniquely deter-
mined. However, |G| is uniquely determined, since it equals the global dimension
of C(G,H,ω,ψ ).
Group-theoretical fusion categories have the following simple char acterization.
Let us say that a fusion category D is pointed if all its simple objects are invertible.
Any pointed fusion category has the form Vec G,ω.
Proposition 8.42. [O1]. A fusion category C is group-theoretical if and only if it
is dual to a pointed category with respect to some indecompos able module category.
Corollary 8.43. Group-theoretical fusion categories have integer Frobenius-Perron
dimensions of simple objects. In particular, they are pseud o-unitary.
Proof. This follows from Proposition 8.42, Theorem 8.35, and the fact that a ny
invertible object has Frobenius-Perron dimension 1. □
It is clear from the results of [O1] that the class of group-theoret ical categories
is closed under tensor product, taking the opposite category, an d taking the dual
category with respect to an indecomposable module category. Mor eover, the fol-
lowing result shows that this class is also closed under taking a subcat egory or a
component of a quotient category.
Proposition 8.44. (i) A full fusion subcategory of a group-theoretical catego ry is
group-theoretical.
(ii) A component in a quotient category of a group-theoretic al category is group-
theoretical.
Proof. (i) Let C ⊂ D be fusion categories ( C is a full subcategory), and let D be
group-theoretical. Let M be an indecomposable module category over D such that
D∗ is VecG,ω. Then by Proposition 5.3, C∗ is a quotient of Vec G,ω. Let I label the
component categories of C∗. It is clear that for each g ∈ G and i ∈I there exists
a unique g(i) ∈I such that the functor g⊗ is an equivalence Cir → Cg(i)r for each
r ∈I. So we have an action of G onI. Let j ∈I andH be the stabilizer of j inG.
For any g ∈H, denote by ¯gjj the projection of g to the fusion category C∗
jj . Then
the assignment g → ¯gjj is a surjective tensor functor Vec H,ω → C ∗
jj . This functor
must map invertible objects to invertible objects. Hence, all simple o bjects of C∗
jj
are invertible, so C∗
jj is pointed, and hence C is group-theoretical (as it is dual to
C∗
jj with respect to a module category).
(ii) Let D be group-theoretical, F : D → C be surjective ( C is indecomposable),
and Cii a component of C. We need to show that Cii is group-theoretical. Let
M be an indecomposable module category over C. It suﬃces to show that C∗ is
group-theoretical, as C∗ is dual to Cii with respect to the i-th part of M. But by
Proposition 5.3, C∗ is embedded into D∗, so it suﬃces to know that D∗ is group-
theoretical, which follows by duality from the fact that D is group-theoretical. □
