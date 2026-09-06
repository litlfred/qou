---
doc_id: arxiv-1010.4386v5
doc_title: "ON THE HOMOLOGY OF COMPLETION AND TORSION"
section_id: sec-001-1-preliminaries-on-homological-algebra
section_title: "Preliminaries on Homological Algebra"
section_number: 1
pages: 4-7
source_pdf: 1010.4386v5.pdf
source_sha256: 168226dbb5a479ed
doc_brief: "ON THE HOMOLOGY OF COMPLETION AND TORSION — Let A be a commutative ring, and a a weakly proregular ideal in A."
---
This paper relies on delicate work with derived functors. Th erefore we begin
with a review of some facts on homological algebra. There are also a few new
results. By default all rings considered in the paper are com mutative.
Let M be an abelian category. As in [RD] we denote by C(M) the category of
complexes of objects of M, by K(M) its homotopy category, and by D(M) the derived
category. There are full subcategories D−(M), D+(M) and Db(M) of D(M), whose
objects are the bounded above, bounded below and bounded com plexes respectively.
Our notation for distinguished triangles in K(M) or D(M) is either L
α
− →M
β
− →
N
γ
− →L[1], or simply L→ M → N
△
− →if the names of the morphisms are not
important.
A complex P∈ C(M) is called K-projective if for any acyclic complex N∈ C(M)
the complex Hom M(P,N ) is also acyclic. A complex I∈ C(M) is called K-injective
if for any acyclic complex N ∈ C(M) the complex Hom M(N,I ) is also acyclic.
These deﬁnitions were introduced in [Sp]; in [Ke, Section 3] it is shown that “K-
projective” is the same as “having property (P)”, and “K-inj ective” is the same as
“having property (I)” .
A K-projective resolution of M∈ C(M) is a quasi-isomorphism P→M in C(M)
with P a K-projective complex. If every M ∈ C(M) admits some K-projective
resolution, then we say that C(M) has enough K-projectives. Similarly for K-
injectives.
Now we specialize to the case M := ModA, where A is a ring. A complex
P∈ C(ModA) is called K-ﬂat if for any acyclic complex N∈ C(ModA) the complex
N⊗AP is also acyclic. Note that a K-projective complex P is K-ﬂat.
Here is a useful existence result.
Proposition 1.1. LetA be a ring, and let M∈ C(ModA).
(1) The complex M admits a quasi-isomorphism P → M , where P is a K-
projective complex, and moreover each component Pi is a free A-module.
(2) The complex M admits a quasi-isomorphism P→M , where P is a K-ﬂat
complex, and moreover each component Pi is a ﬂat A-module.
ON THE HOMOLOGY OF COMPLETION AND TORSION 5
(3) The complex M admits a quasi-isomorphism M → I, where I is a K-
injective complex, and moreover each component Ii is an injective
A-module.
Proof. (1) This is proved in [Ke, Subsection 3.1], when discussing t he existence of
P-resolutions. Cf. [Sp, Corollary 3.5].
(2) This follows from (1), since any K-projective complex is also K-ﬂat.
(3) See [Ke, Subsection 3.2]. Cf. [Sp, Proposition 3.11]. □
In particular, the proposition says that C(ModA) has enough K-projectives, K-
ﬂats and K-injectives.
Remark 1.2. Let (X,A) be a ringed space, and let ModA be the category of
sheaves of A-modules. It is known that C(ModA) has enough K-injectives and
enough K-ﬂats; but their structure is more complicated than in the case of
C(ModA), and Proposition 1.1 might not hold.
Here are a few facts about K-projective and K-injective reso lutions, compiled
from [Sp, BN, Ke]. The ﬁrst are: a bounded above complex of pro jectives is K-
projective, a bounded above complex of ﬂats is K-ﬂat, and a bo unded below complex
of injectives is K-injective.
Once again M is an abelian category. Let E be some triangulated category, and
let F : K(M)→ E be a triangulated functor. If C(M) has enough K-projectives,
then the left derived functor (L F,ξ ) : D(M)→ E exists, and it is calculated by
K-projective resolutions. Likewise, if K(M) has enough K-injectives, then the right
derived functor (R F,ξ ) : D(M) → E exists, and it is calculated by K-injective
resolutions.
Let M ={Mi}i∈Z be a graded object of M. We deﬁne
(1.3) inf( M ) := inf{i|Mi⁄= 0}∈ Z∪{±∞}
and
(1.4) sup( M ) := sup{i|Mi⁄= 0}∈ Z∪{±∞}.
The amplitude of M is
(1.5) amp( M ) := sup(M )− inf(M )∈ N∪{±∞}.
(ForM = 0 this reads inf( M ) = ∞, sup(M ) =−∞ and amp(M ) = −∞.) Thus
M is bounded iﬀ amp( M )<∞.
ForM∈ D(M) we write H( M ) :={Hi(M )}i∈Z.
Deﬁnition 1.6. Let M and M′ be abelian categories, and let F : D(M)→ D(M′) be
a triangulated functor. Let E⊂ D(M) be a full additive subcategory (not necessarily
triangulated), and consider the restricted functor F|E : E→ D(M′).
(1) We say that F|E has ﬁnite cohomological dimension if there exist some
n∈ N and s∈ Z such that for every complex M∈ E one has
sup
(
H(F (M ))
)
≤ sup
(
H(M )
)
+s
and
inf
(
H(F (M ))
)
≥ inf
(
H(M )
)
+s−n.
The smallest such number n is called the cohomological dimension of F|E.
6 MARCO PORTA, LIRAN SHAUL AND AMNON YEKUTIELI
(2) If no such n and s exist then we say F|E has inﬁnite cohomological dimen-
sion.
The number s appearing in the deﬁnition represents the shift. (An easy ca lcu-
lation shows that if F|E is nonzero and has ﬁnite cohomological dimension n, then
the shift s in the deﬁnition is unique.)
If the functor F has ﬁnite cohomological dimension, then it is a way-out functor
in both directions , in the sense of [RD, Section I.7]. We will use this fact sever al
times.
Example 1.7. Take a nonzero ring A, and let P := A[1]⊕A[2], a complex with
zero diﬀerential concentrated in degrees −1 and−2. The functor F :=P⊗A− has
cohomological dimension n = 1, with shift s =−1.
Proposition 1.8. Let M, M′ and M′′ be abelian categories, and let F : D(M)→
D(M′) and F′ : D(M′)→ D(M′′) be triangulated functors. Assume the cohomo-
logical dimensions of F and F′ are n and n′ respectively. Then the cohomological
dimension of F′◦F is at most n +n′.
We leave out the easy proof.
Here is a useful criterion for quasi-isomorphisms (a varian t of the way-out argu-
ment). For i,j ∈ Z let C[i,j ](M) be the full subcategory of C(M) whose objects are
the complexes concentrated in the degree range [ i,j ] :={i,i + 1,...,j }.
Proposition 1.9. Let M and M′ be abelian categories, let F,G : M→ C(M′) be
additive functors, and let η :F→G be a natural transformation. Assume M′ has
countable direct sums, and consider the extensions F,G : C(M)→ C(M′) by the
direct sum totalization. Suppose M∈ C(M) satisﬁes these two conditions :
(i) There are j0,j 1∈ Z such that F (Mi),G (Mi)∈ C[j0,j 1](M′) for every i∈ Z.
(ii) The homomorphism ηM i : F (Mi)→ G(Mi) is a quasi-isomorphism for
every i∈ Z.
Then ηM :F (M )→G(M ) is a quasi-isomorphism.
Proof. Step 1. Assume that M is bounded. We prove that ηM is a quasi-iso-
morphism by induction on amp( M ). If amp( M ) = 0 then this is given. The
inductive step is done using the stupid truncation functors
(1.10) stt >i(M ), stt≤i(M ) : C(M)→ C(M),
and the related short exact sequences. See [RD, pages 69-70] , where the truncations
stt>i(M ) and stt≤i(M ) are denoted by τ>i(M ) and τ≤i(M ) respectively.
Step 2. Now M is arbitrary. We have to prove that H i(ηM ) : H i(F (M )) →
Hi(G(M )) is an isomorphism for every i∈ Z. For any i≤ j there is the double
truncation functor stt [i,j ] := stt≤j◦ stt>i. So let us ﬁx i. The homomorphism
Hi(ηM ) in M′ only depends on the homomorphism of complexes
stt[i−1,i +1](ηM ) : stt [i−1,i +1](F (M ))→ stt[i−1,i +1](G(M )).
Therefore we can replace ηM with ηM′ :F (M′)→G(M′), where
M′ := stt [j0+i−1,j 1+i+1](M ).
ButM′ is bounded, so by part (1) the homomorphism ηM′ is a quasi-isomorphism.
□
ON THE HOMOLOGY OF COMPLETION AND TORSION 7
To end this section, here is a basic result we need, that we cou ld not locate in
the literature (but that was used implicitly in [Sc]).
Proposition 1.11. Let M and N be abelian categories, let F : M→ N be an exact
additive covariant functor, and let G : M→ N be an exact additive contravariant
functor. Then for any M∈ C(M) there are isomorphisms Hk(F (M ))∼=F (Hk(M ))
and H−k(G(M ))∼=G(Hk(M )) in N. Moreover, these isomorphisms are functorial
in M , F and G.
Proof. These are very degenerate cases of Grothendieck spectral se quences. Here
is a direct proof. We use the notation Z k(M ) := Ker(d : Mk→ Mk+1), which is
the object of k-cocycles of M , and Y k(M ) := Coker(d : Mk−1→Mk), which does
not have a name. There are functorial isomorphisms
Hk(M )∼= Coker
(
d : Mk−1→ Zk(M )
) ∼= Ker
(
d : Yk(M )→Mk+1)
.
For any additive functor F : M→ N (not necessarily exact) there is an ob-
vious morphism α : F (Zk(M )) → Zk(F (M )), and it induces a morphism ¯ α :
F (Hk(M ))→ Hk(F (M )). An easy calculation shows that when F is exact, the
morphismsα and ¯α are isomorphisms.
Given a contravariant additive functor G : M→ N, there is a morphism (slightly
less obvious than α, because of the change in direction) β : G(Yk(M )) →
Z−k(G(M )). This induces a morphism ¯β : G(Hk(M )) → H−k(G(M )). When
G is exact, the morphisms β and ¯β are isomorphisms. □
Corollary 1.12. LetA be a ring, M a complex of A-modules,P a ﬂat A-module,
and I and injective A-module. There are isomorphisms
Hk(M⊗AP )∼= Hk(M )⊗AP
and
H−k(HomA(M,I ))∼= HomA(Hk(M ),I ),
functorial in M,P and I.
Proof. TakeF (M ) := M⊗AP andG(M ) := HomA(M,I ), and use the proposition
above. (These are degenerate cases of the Künneth Theorems. ) □
