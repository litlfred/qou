---
doc_id: arxiv-math-0203206v1
doc_title: "Representations of Algebraic Quantum Groups and Reconstruction Theorems for Tensor Categories"
section_id: sec-025-4-cocommutative-algebraic-quantum-groups-vs-comp
section_title: "Cocommutative Algebraic Quantum Groups vs. Compact Group s"
section_number: 4
pages: 20-25
source_pdf: 0203206v1.pdf
source_sha256: 371611f719e6f53c
doc_brief: "Representations of Algebraic Quantum Groups and Reconstruction Theorems for Tensor Categories — We give a pedagogical survey of those aspects of the abstract representation theory of quantum groups"
---
Definition 4.1 Let (A, ∆) be an aqg. The intrinsic group G of (A, ∆) is the following subgroup of the unitaries
in the multiplier algebra M (A):
G = {g ∈M (A) | ∆ g =g ⊗g, g∗g =gg ∗ = 1}.
Since the extended comultiplication ∆ : M (A) → M (A ⊗A) is a unital ∗-homomorphism and the algebra
M (A) is associative, the set G is indeed a group. It is easy to see that ε(g) = 1 and S(g) = g−1 =g∗, for any
g ∈G.
20
Remark 4.2 It can be shown that any bounded group-like element of M (A) is automatically unitary with
S(g) = g∗. A proof of this may be found in [20] and [11], but the above deﬁnition s uﬃces for our purposes.
Lemma 4.3 Let (A, ∆) be a discrete aqg. Equipped with the product topology, M (A) =∏
i∈IB(Hi) is a complete
locally convex topological vector space and A is dense in M (A).
Proof. Since the blocks B(Hi) are Banach spaces, the functions ‖pi(·)‖ form a separating family of seminorms
which induces the product topology. Completeness is obvious by sem isimplicity of the B(Hi), i ∈ I. To see
that A is dense in M (A), let x ∈M (A) and consider the net ( xλ)λ∈Λ in A given by xλ = ⊕i∈λpi(x), where Λ
is the collection of ﬁnite subsets of I directed by inclusions. Then clearly xλ →x. ■
Proposition 4.4 If (A, ∆) is a discrete aqg, its intrinsic group G is a compact topological group w.r.t. the
product topology on M (A).
Proof. Note that a net ( gλ) converges to g inG iﬀ pi(gλ) →pi(g) in norm, for all i ∈I. By Tychonov’s theorem
it suﬃces to show that G is closed in ∏
i∈IU (B(Hi)). Given a net ( gλ) in G which converges to a ∈M (A), we
must show that ∆ a = a ⊗a. Let i,j ∈ I and consider the ﬁnite dimensional non-degenerate ∗-representation
(pi ⊗pj)∆ : A →B(Hi ⊗Hj). By Proposition 2.10, we may write
(pi ⊗pj)∆ ≃
⨁
k∈I
Nk
ijpk.
Since both these expressions are non-degenerate ∗-representations, they extend to equivalent unital ∗-representations
of M (A), which we now identify. Therefore
(pi ⊗pj)∆ a =
⨁
k∈I
Nk
ijpk(a) = lim
λ
⨁
k∈I
Nk
ijpk(gλ) = lim
λ
(pi ⊗pj)∆ gλ
= lim
λ
pi(gλ) ⊗pj(gλ) = pi(a) ⊗pj(a) = (pi ⊗pj)(a ⊗a),
thus ∆ a =a ⊗a and G is closed. ■
Remark 4.5 Note furthermore that in the proof of the proposition we have sho wn that
∆ : M (A) =
∏
i∈I
B(Hi) →M (A ⊗A) =
∏
i,j∈I
B(Hi ⊗Hj)
is continuous w.r.t. the product topologies.
Proposition 4.6 Suppose (A, ∆) is a discrete aqg with intrinsic group G. Let π be a non-degenerate ∗-
representation of A on a ﬁnite dimensional Hilbert space K. Deﬁne a map uπ :G →B(K) by
uπ :g ↦→π(g),
where the extension of π to M (A) is understood. Then uπ is strongly continuous and D : (K,π ) ↦→(K,uπ)
together with the identity map on the morphisms is a faithful and tensor functor from Repf (A, ∆) to the category
RepfG of ﬁnite dimensional continuous representations of G.
21
Proof. Continuity ofuπ w.r.t. the topology on G is obvious. As π :M (A) →B(K) is a unital ∗-homomorphism,
clearly (K,uπ) ∈ RepG. Functoriality and faithfulness of D are obvious. Monoidality follows from the calcula-
tion
D(π1 ×π2)(g) = (π1 ⊗π2)∆ g =π1(g) ⊗π2(g) = uπ1(g) ⊗uπ2(g) = (uπ1 ×uπ2)(g)
for all g ∈G and πi ∈ Rep(A, ∆). Every π ∈ Rep(A, ∆) is equivalent to a direct sum of the representations pi
by Proposition 2.10. Each upi is (strongly) continuous and therefore the direct sum is strongly c ontinuous. ■
Thus far we have not assumed ( A, ∆) to be cocommutative. The following characterization of cocommu ta-
tivity will be crucial for proving that D gives rise to an equivalence of categories.
Theorem 4.7 A discrete aqg (A, ∆) is cocommutative iﬀ
spanC{g | g ∈G} =M (A).
Remark 4.8 This theorem implies that
spanC{pi(g) | g ∈G} =B(Hi)
for every i ∈I and in particular that A = span C{gIi | i ∈I,g ∈G}. These results are rigorous formulations of
the heuristic idea that a cocommutative aqg is ‘spanned by its grouplik e elements’. Before we give the proof of
Theorem 4.7 we show that it leads to the desired equivalence of categ ories.
In what follows we ﬁx a cocommutative discrete aqg ( A, ∆) where A = ⊕i∈IB(Hi) and let G denote its
intrinsic group. For every i ∈ I, ui : g ↦→pi(g) ∈ B(Hi) is a continuous unitary representation of G. By
Theorem 4.7, the span of pi(g), g ∈G is dense in B(Hi), thus ui is irreducible. This deﬁnes a map γ :I →IG.
Proposition 4.9 The map γ is a bijection.
Proof. If there is a unitary V :Hi →Hj such that Vpi(g) = pj(g)V for all g ∈G then Vpi(x) = pj(x)V for all
x ∈ spanC{g |g ∈G}. Since these x are dense in M (A) by Theorem 4.7 and the pi are continuous we conclude
that Vpi(x) = pj(x)V for all x ∈M (A), thus i =j so that γ :I →IG is injective.
Obviously if g ⁄= e there is an i ∈ I such that pi(g) ⁄= 1B(Hi). Since the category Rep f (A, ∆) is monoidal
and has conjugates, γ(I) ⊂IG is closed w.r.t. conjugation and tensor products and reduction. Th e surjectivity
of γ now follows from the following well known group theoretical fact. ■
Lemma 4.10 Let G be a compact group and let J ⊂ IG be closed w.r.t. conjugation and tensor products and
reduction. If J separates points on G then J =IG.
Proof. For every equivalence class i ∈IG pick a representative ui. The assumptions on J imply that the span
of the matrix elements ( uj)nm, j ∈J is a unital ∗-subalgebra of C(G). Since it separates the points of G it is
dense in C(G) by the Stone-Weierstrass theorem and therefore dense in L2(G,µ ), where µ is the Haar measure.
If there were a k ∈IG\J then by the Peter-Weyl theorem the matrix elements of uk would be orthogonal to the
dense subspace of L2(G,µ ) generated by the ( uj)nm, j ∈J, which is a contradiction. ■
Theorem 4.11 Let (A, ∆) be a cocommutative discrete aqg and G its intrinsic group. Then the functor D :
Rep(A, ∆) → RepG induces a canonical equivalence of tensor ∗-categories:
Repf (A, ∆)
⊗
≃ RepfG.
22
Proof. In view of Proposition 4.6 it only remains to prove that the functor D is full and essentially surjective.
By Proposition 2.10 the category Rep f (A, ∆) is semisimple, and for a compact group G the semisimplicity of
RepfG is well known. Recall from Section 2.1 that a faithful functor betwe en semisimple categories is full if
and only if it maps simple objects to simple objects and non-isomorphic simple objects have non-isomorphic
images. The ﬁrst property was used to deﬁne the map γ of Proposition 4.9, and the second is the injectivity of
γ. Finally, essential surjectivity of D is expressed by surjectivity of γ. Since D is monoidal it gives rise to an
equivalence of tensor categories by [31]. ■
Now we prove the characterization of cocommutative discrete aqg used above.
Proof of Theorem 4.7. Clearly, if the closure of span C{g |g ∈G} is M (A), then by linearity and continuity of
∆ : M (A) →M (A ⊗A), we see that ( A, ∆) is cocommutative. We prove the converse direction. By Lemma 4.3
it suﬃces to show that any x ∈A is the limit of linear combinations of elements of G. Fix x ∈A. For any aqg
(A, ∆) there exists a linear inclusion Q :֒→ ˆA∗
r determined by
Q(b)ˆπr(ˆa) = ˆa(b) = ϕ(ba)
for all a,b ∈A. To see this, to any a,b ∈A we can choose an element c ∈A such that ˆc ˆb∗∗
= ˆb∗∗
. (Such c can
be obtained as inverse Fourier transform of a local unit for ˆb∗∗
in ˆA.) Now we observe that
Q(b)ˆπr(ˆa) = ϕ((b∗)∗a) = ˆψ( ˆb∗∗
ˆa) = ˆψ(ˆc ˆb∗∗
ˆa) = ˆψ( ˆb∗∗
ˆaˆρ(ˆc)) = (ˆπr(ˆa)ˆΛ(ˆρ(ˆc)), ˆΛ( ˆb∗)),
so Q(b) = ( ·ˆΛ(ˆρ(ˆc)), ˆΛ( ˆb∗)). Now ˆAr is a unital commutative C∗-algebra. Let Y be the set of ∗-characters on
ˆAr. Gelfand’s theorem tells us that Y is a compact Hausdorﬀ space and that the map Γ : ˆAr → C(Y ) given
by Γ(a)(y) = y(a), for all a ∈ ˆAr and y ∈ Y , is a unital ∗-isomorphism from ˆAr to the C∗-algebra C(Y ) of
continuous functions on Y . Thus Q(x)Γ −1 ∈ C(Y )∗. By the Krein-Milman theorem for probability measures
[27, Theorem 2.5.4] any element of C(Y )∗ is a w∗-limit of linear combinations of Dirac measures δy ∈C(Y )∗.
Hence we may write
Q(x)Γ −1 = lim
λ
∑
k
cλkδyλk
for some cλk ∈ C and yλk ∈Y . Thus we get
ˆa(x) = Q(x)ˆπr(ˆa) = Q(x)Γ −1Γˆπr(ˆa) = lim
λ
∑
k
cλkδyλk Γˆπr(ˆa)
= lim
λ
∑
k
cλkΓˆπr(ˆa)(yλk) = lim
λ
∑
k
cλkyλk ˆπr(ˆa)
for all a ∈A. Now the yλk ˆπr : ˆA → C are unital ∗-homomorphisms, so we may deﬁne gλk ∈M (A) by
gλk = (ι ⊗yλk ˆπr)U,
where U ∈ M (A ⊗ ˆA) is the universal corepresentation of ( A, ∆). Since U is unitary, so are the elements gλk
and moreover,
∆ gλk = ∆( ι ⊗yλk ˆπr)U = (ι ⊗ι ⊗yλk ˆπr)(∆ ⊗ι)U = (ι ⊗yλk ˆπr)(U13U23)
= ( ι ⊗yλk ˆπr)U ⊗ (ι ⊗yλk ˆπr)U =gλk ⊗gλk,
thus all gλk ∈G.
Now for any ξ ∈ B(Hi)′ and i ∈ I observe that ξpi ∈ ˆA since ϕ is, up to a factor di, the trace on B(Hi).
Thus by Theorem 3.4 we have ( ξpi ⊗ι)U =ξpi. Hence by the previous formulae we get
ξpi(x) = lim
λ
∑
k
cλkyλk ˆπr(ξpi) = lim
λ
∑
k
cλkyλk ˆπr(ξpi ⊗ι)U
= lim
λ
∑
k
cλkξpi(ι ⊗yλk ˆπr)U = lim
λ
∑
k
cλkξpi(gλk) = lim
λ
ξpi(
∑
k
cλkgλk).
23
Since this is true for all i ∈I and ξ ∈B(Hi)′, we thus get
x = lim
λ
∑
k
cλkgλk
as desired. ■
This concludes the proof of Theorem 4.7.
Corollary 4.12 For every i ∈I we have spanC{pi(g) | g ∈G} =B(Hi).
Proof. First we show that for 0 ⁄= a ∈ A, there exist g ∈ G such that ϕ(ga) ⁄= 0. Thus let 0 ⁄= a ∈ A. Then
there exists x ∈A such that ˆa(x) = ϕ(xa) ⁄= 0, thus ˆa =ϕ(·a) ⁄= 0. Furthermore, there exists a ﬁnite set Λ ⊂I
such that
ˆa(b) = ϕ(ba) =
∑
i∈Λ
diTri(pi(ba)),
for all b ∈M (A). Since the product in M (A) is continuous, we thus see that ˆa :M (A) → C is continuous. Thus
by Theorem 4.7 there exists g ∈G such that ϕ(ga) ⁄= 0.
Assume now that span C{pi(g) | g ∈ G} ⁄= B(Hi). Then there exists a non-zero a ∈ B(Hi) such that
TrB(Hi)(pi(g)a) = 0 for all g ∈G. Since ϕ ↾B(Hi) = diTrB(Hi), this is a contradiction. ■
Let G be a compact group and consider a unitary representation u : G → B(K) of G on some ﬁnite
dimensional Hilbert space K. Since u is continuous (here with respect to the norm), we have u ∈C(G,B (K)).
Since C(G,B (K)) ∼
= C(G) ⊗B(K), we may thus regard u as a unitary element ˜V of the unital ∗-algebra
C(G) ⊗B(K). Now u : G → B(K) being a representation simply means that (∆ ⊗ι) ˜V = ˜V13 ˜V23, where
∆ : C(G) → C(G ×G) ∼
= C(G) ⊗C(G) is given by ∆( a)(g,g ′) = a(gg ′), for all a ∈ C(G) and g,g ′ ∈ G.
Thus ˜V is a unitary corepresentation of the commutative compact quantu m group ( C(G), ∆) in the sense of
Woronowicz. It is easy to see that one may recover u from ˜V byu(g) = (δg ⊗ι) ˜V , for g ∈G.
Theorem 4.13 Let (A, ∆) be a cocommutative discrete aqg, so ( ˆA, ˆ∆) is a commutative compact aqg. Let G
be the compact group such that (C(G), ∆) ∼
= ( ˆAr, ˆ∆ r). For any V ∈ Corepf ( ˆA, ˆ∆) , let ˜V ∈ C(G) ⊗B(K) be
the unitary corepresentation of (C(G), ∆) given by ˜V = (ˆπr ⊗ι)V . Then there exists an isomorphism from G
to the intrinsic group of (A, ∆) given by
g ↦→˜g = (ι ⊗δg ˆπr)U ∈M (A),
whereU is the universal corepresentation of (A, ∆) . Moreover, the equivalence
Corepf ( ˆA, ˆ∆)
P
− →Repf (A, ∆)
Df
− →RepfG
given by the composition
V ↦→πV ↦→uπV =:uV,
with P and Df established in Theorem 3.14 and Theorem 4.11, is described m ore directly by
uV (˜g) = (δg ⊗ι) ˜V,
for all g ∈G.
Proof. From the proof of Theorem 4.7, it is easily seen that g ↦→˜g is indeed a homeomorphism from G
to the intrinsic group of ( A, ∆) which also preserves the products. Let g ∈ G. We proceed to show that
24
uV (˜g) = (δg ⊗ι) ˜V . Since V ∈ ˆA ⊗B(K) we may write V =∑
kωk ⊗xk for ωk ∈ ˆA and xk ∈B(K). Then
uV (˜g) = uV ((ι ⊗δg ˆπr)U ) = πV ((ι ⊗δg ˆπr)U )
= ([( ι ⊗δg ˆπr)U ] ⊗ι)V =
∑
k
[(ι ⊗δg ˆπr)U ](ωk)xk =
∑
k
(ωk ⊗δg ˆπr)Uxk
=
∑
k
δg ˆπr((ωk ⊗ι)U )xk =
∑
k
δg ˆπr(ωk)xk = (δg ˆπr ⊗ι)(
∑
k
ωk ⊗xk) = (δg ˆπr ⊗ι)V = (δg ⊗ι) ˜V,
as claimed. ■
