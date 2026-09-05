---
doc_id: arxiv-1011.6483v3
doc_title: "DERIVED HIGHER HOCHSCHILD HOMOLOGY"
section_id: sec-010-55-some-applications
section_title: "Some applications"
section_number: 5.5
pages: 55-59
source_pdf: 1011.6483v3.pdf
source_sha256: 7a425e51860c37a4
doc_brief: "DERIVED HIGHER HOCHSCHILD HOMOLOGY — W e study the higher Hochschild chain functor, factorizatio n alge- bras and their relationship with topological chiral homolo gy."
---
5.5.1. Another construction of topological chiral homology for fr amed manifolds.
Let M be an m-dimensional manifold which is n-framed. Given an En-algebra
A, we can deﬁne the topological chiral homology
∫
MA of M with values in A. By
Proposition 13 and Theorem 6,
∫
MA is the factorization homology of a factorization
algebra on M×Dn−m. We explain how to construct this factorization algebra
directly.
56 G. GINOT, T. TRADLER, AND M. ZEINALIAN
Since M is n-framed, there is a bundle isomorphism ϕ :T (M×Dn−m)
≃
−→ Rn
where Rn is a trivial bundle over M×Dn−m. Choosing a Riemannian metric on
M×Dn−m, we have, using the spray associated to the exponential map, can onical
diﬀeomorphisms of (a basis of) open neighborhoods of any x∈M×Dn−m to open
sets in the tangent space T (M×Dn−m)x of M×Dn−m at x. Composing with
the map ϕ induced by the framing, we get diﬀeomorphisms U↦→ψ(Ux)∈Op(Rn)
where U is a (geodesically convex) open neighborhood of x.
LetU be the cover of M×Dn−m obtained by considering the U above such that
φx(Ux)∈B all (Rn) is an euclidean ball. The cover U is a factorizing basis of open
subsets of M×Dn−m.
To anyU∈U , we associate A(U ) = A, a (ﬁxed) En-algebra. We wish to extend
A into a factorization algebra. Since A is anEn-algebra, it deﬁnes a locally constant
factorization algebra on Rn (see [9, 25] and Proposition 10), which we, by abuse
of notation, again denote by A. For any pairwise disjoint U1,··· ,Un ∈U , and
V ∈U such that Ui⊂V (i = 1··· n), we deﬁne the structure maps µU1,...,Un,V (see
Section 4.2) by the following commutative diagram:
A(U1)⊗···⊗A (Un)
≃
/d15/d15
µU1 ,...,Un ,V
/d47/d47A(V )
≃
/d15/d15
A(ψ(U1))⊗···⊗ A(ψ(Un)) /d47/d47A(ψ(V ))
where the lower arrow is given by the En-algebra structure of A. This yields a
U-factorization algebra (in the sense of [8] and § 4.2) since A is a factorization
algebra on Rn and M×Dn−m is framed. By [8, Section 3], we can now extend A
to a factorization algebra on M×Dn−m.
Corollary 13. There is an equivalence of En−m-algebras∫
M
A ∼= HF (M,A).
Proof. For any ball U , we have a natural equivalence
∫
UA∼=A∼=A(U ). Now the
result follows from Theorem 6 (and its proof) after taking global se ctions. □
Note that topological chiral homologyTC M (A) is independent of the Riemannian
metric, hence the factorization algebra A ∈Faclc
M×Dn−m (k-Mod ∞) on M thus
obtained is also independent of the Riemannian metric.
5.5.2. Interpretation of topological chiral and higher Hochschil d in terms of mapping
spaces. As we have already noticed, higher Hochschild chains behave much like
mapping spaces (and thus so do
∫
MA for CDGAs A). Indeed,
Corollary 14. Let A = Ω ∗N be the de Rham forms on a d-connected manifold
(with its usual diﬀerential). Then for any manifold M of dimension m≤d, there
is a natural quasi-isomorphism
∫
MA∼= Ω ∗(NM ), the space of (Chen) de Rham
forms of the mapping space NM =Map (M,N ).
In other words, topological chiral homology of M with value in Ω ∗N calculates
the mapping space NM (if N is suﬃciently connected).
Proof. By Theorem 5, we are left to a similar statement for CHM (Ω ∗N ). Since
M is m-dimensional it has a simplicial model with no non-degenerate simplices
DERIVED HIGHER HOCHSCHILD, TCH, F ACTORIZATION ALGEBRAS 57
in dimensions above m. Now the result follows from [13, Proposition 2.5.3 and
Proposition 2.4.6]. □
Remark 18. By [13, Section 2.4], there is a canonical map
∫
M Ω ∗N→ Ω ∗(NM ).
Further, it is possible to replace N by any nilpotent space (by mimicking the proof
of [13, Propositions 2.5.3 and 2.4.6]) and Ω ∗N by a Sullivan model of N .
We now give a (derived/homotopical) algebraic geometry statement . Recall that
k denotes a ﬁeld of characteristic zero and let dStk be the (model) category of
derived stacks over k described in details in [32, Section 2.2] (which is a derived
enhancement of the category of stacks over k). This category admits internal Hom’s
that we denote by RMap (X, Y) following [32, 33]. To any simplicial set X•, we
associate the constant simplicial presheaf k-Alg→ sSet deﬁned by R↦→X• and
we denote X the associated stack. For a (derived) stack Y, we denote OY its
functions [32] ( i.e.,OY := RHom(Y, A1)).
Corollary 15. Let R = RSpec(R) be an aﬃne derived stack (for instance an aﬃne
stack) [32]. Then the Hochschild chains over X• with coeﬃcient in R represent the
mapping stack RMap (X, R). That is,
ORMap (X,R) ∼= CH •
X• (R).
Proof. The bifunctor ( X, RSpec(R))↦→RMap (X, RSpec(R)) is contravariant in
X and R ∈ CDGA ≤0. Thus, ORMap (X,R) deﬁnes a covariant bifunctor. Since
RMap (−, R) sends (homotopy) limits to (homotopy) colimits, it follows from The-
orem 2 (also see Remark 4) that ORMap (X,R) is equivalent to CH •
X• (R). □
Example 13. Let B•Z be the nerve of Z and BZ its associated stack. Recall
that there is an homotopy equivalence S1→|B•Z| (actually induced by a simpli-
cial set map, see [21]). From Corollary 15 we recover that the derive d loop stack
LR := RMap (BZ, R) is represented by CH •
B•Z(R)
≃
←−CH •
S1
•
(R) the standard
Hochschild chain complex of R as was proved in [33]. Similarly, the derived torus
mapping stack RMap (BZ× BZ, R) is represented by CH •
S1×S1(R) and the sec-
ondary cyclic homology in the sense of [33] is represented by the hom otopy ﬁxed
points CH •
S1×S1 (R)h(S1×S1) with respect to the induced action of the simplicial
group B•Z×B•Z on the derived mapping space.
Remark 19. Sheaﬁfying (or rather stackifying) the higher Hochschild derived f unc-
tor, it seems possible to extend Corollary 15 to general derived sch emes.
5.5.3. Topological chiral Homology and homology spheres. Topological chiral ho-
mology of CDGAs is a homology invariant, and thus, in particular, a hom otopy
invariant. Indeed, we have the following corollary.
Corollary 16. Let f : M → N be smooth map between two manifolds inducing
isomorphisms on homology and A be a CDGA, then
∫
MA∼=
∫
NA.
Proof. This follows from Theorem 5 and the quasi-isomorphism invariance of CH •
(−)(A)
(Proposition 4). □
Example 14. The composition S3→ SO(3)→ SO(3)/I, where I is the icosa-
hedral group, induces an isomorphism on homology. To see this note that the
fundamental group of SO(3)/I is the binary icosahedral group ˜I which is a perfect
58 G. GINOT, T. TRADLER, AND M. ZEINALIAN
group and therefore H1(SO(3)/I) = 0. The result SO(3)/I is the Poincar´ e homol-
ogy sphere and has thus the same topological chiral homology with v alue in any
CDGA as S3.
Remark 20. Note that we study topological chiral homology in the framework of
chain complexes, i.e. we have ﬁxed the ( ∞, 1)-category of chain complexes as our
“ground” monoidal (∞, 1)-category. If one works in some other framework (such
as topological spaces), one can expect to have more reﬁned invar iants.
Remark 21. Note that S1 has two diﬀeomorphic 1-framings (speciﬁed by a choice
of orientation). This accounts for the fact that classically there is only one Hochschild
complex for associative algebras. There are countably many 2-fra mings for the cir-
cle, one for each integer, giving rise to equivalent topological chiral homologies when
the integrand is a CDGA. It would therefore be meaningful to look fo r an explicit
E2-algebra that distinguishes these framings from one another, if su ch exists. Sim-
ilarly, it would be interesting to ﬁnd an explicit E3-algebra that distinguishes the
two 3-framings of S1.
5.5.4. Fubini formula for topological chiral homology. The exponential law for Hochschild
chains (Proposition 5) has an analogue for topological chiral homolo gy.
Corollary 17. Let M , N be manifolds and A be an Ed[M×N ]-algebra. Then,∫
NA has a canonical lift as an Ed[M ]-algebra and further, there is an equivalence
of Ed-algebras ∫
M×N
A ∼=
∫
M
( ∫
N
A
)
.
Proof. Replacing M by M× Rd and using Lemma 4, it is enough to prove the
result for d = 0. Since the homology of a factorization algebra on X is given by the
pushforward along the canonical map p :X→pt, by Theorem 6, one has
(29)
∫
M×N
A∼=p∗
(
TC M×N (A)
) ∼=p∗
(
π∗
(
TC M×N (A)
))
where π : M×N→ M is the canonical projection. Since TC M×N (A) is locally
constant,π∗
(
TC M×N (A) is also locally constant whose value on an open ball D⊂
M is given by π∗
(
TC M×N (A)(U )∼=TC M×N (A)(U×N )∼=
∫
NA. This deﬁnes
the canonical Ed[M ]-algebra structure on
∫
NA and the result now follows from the
equivalence (29). □
Example 15. LetM ,N bem +k-framed and n +ℓ-framed manifolds of respective
dimension m, n and A be an En+k+m+ℓ-algebra. Then, the product M×N is
canonically m +n +k +ℓ-framed and A is an Ek+ℓ-algebra. Then, Corollary 17
yields an equivalence of Ek+ℓ-algebras:
∫
M×N
A ∼=
∫
M
( ∫
N
A
)
.
In particular, if A is a CDGA, then Corollary 17 reduces to the exponential law for
Hochschild chains (Proposition 5) under the equivalence between to pological chiral
homology and derived Hochschild chains (Theorem 5).
DERIVED HIGHER HOCHSCHILD, TCH, F ACTORIZATION ALGEBRAS 59
