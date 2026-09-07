---
doc_id: arxiv-1206.5522v6
doc_title: "FACTORIZATION HOMOLOGY OF TOPOLOGICAL MANIFOLDS"
section_id: sec-010-35-homology-theories
section_title: "Homology theories"
section_number: 3.5
pages: 23-28
source_pdf: 1206.5522v6.pdf
source_sha256: 6e992242435b5e9f
doc_brief: "FACTORIZATION HOMOLOGY OF TOPOLOGICAL MANIFOLDS — Factorization homology theories of topological manifolds , after Beilinson, Drinfeld and Lurie, are homology-type theories for topological"
---
factorization homology; this is the central conceptual result of t his paper.
Theorem 3.24. For V a symmetric monoidal ∞-category which is⊗-presentable, there is an equiv-
alence ∫
: AlgDiskB
n
(V) /d47/d47 H(MﬂdB
n , V) : evRn
/d111/d111
between DiskB
n -algebras in V and homology theories of B-framed n-manifolds with coeﬃcients in
V. This equivalence is implemented by the factorization homo logy functor ∫ and the functor of
evaluation on Rn.
Proof. Proposition 3.7 recognizes factorization homology as a symmetric mo noidal left Kan exten-
sions, thereby implementing the left adjoint in an adjunction
i! : AlgDiskB
n
(V)⇄ Fun⊗(
MﬂdB
n , V
)
: i∗ .
The unit of this adjunction is an equivalence because DiskB
n → MﬂdB
n is fully faithful, and the
Kan extension along a fully faithful functor restricts as the origina l functor. The counit of this
adjunction evaluates on a symmetric monoidal functor F as a morphism
∫
A→ F, where A = F|Rn
is the DiskB
n -algebra deﬁned by the values of F on disjoint unions of B-framed Euclidean n-spaces.
It remains to verify that this counit is an equivalence.
Since both F and
∫
A are symmetric monoidal and agree on Rn, the map
∫
M A→ F(M ) is an
equivalence for M isomorphic to a disjoint union of Euclidean spaces, M∼=
⨆
I Rn. Using induction,
we will now see that the values of F and
∫
A agree on thickened spheres Sk× Rn−k, the base case of
k = 0 just having been shown. In the inductive step, assume the resu lt for Si−1× Rn−i+1. Choose
a standard collar-gluing Si f
− →[−1, 1] with Si−1 = f −1(0)⊂ Si an equator. There results a collar-
gluing of Si× Rn−i. For F a homology theory, we obtain the equivalence
∫
Si×Rn−i A≃ F(Si× Rn−i)
via the intermediate equvialences
∫
Si× Rn−i
A ≃
∫
Ri
−1× Rn−i
A
⨂
∫
Si−1×Rn−i+1
A
∫
Ri
+1× Rn−i
A ≃ F(Ri
− 1 × Rn− i)
⨂
F(Si−1× Rn−i+1)
F(Ri
+1 × Rn− i) ≃ F(Si × Rj )
where the ﬁrst equivalence is by the ⊗-excision property of factorization homology, the last equiva-
lence is by the assumption that F is a homology theory, and the middle equivalence is by induction.
We now restrict to the case of B-framed n-manifolds where n is not equal to 4. By the handlebody
theory for topological manifolds ([KS] for n > 5, [Qu] for n = 5, and [Mo] for n = 3) all such
manifolds admits a handle decomposition. We now prove the result out side dimension 4 by induction
on the handle decomposition. The base case is assured. To verify th e inductive step, let M be
obtained from M0 by adding a handle of index q + 1. Therefore M can be expressed as a collar-
gluing M ∼= M0
⋃
Sq×Rn−q
Rn, where Rn is an open neighborhood of the ( q + 1)-handle in M . The
values F and
∫
A agree on the three constituent submanifolds of M , and they both satisfy ⊗-excision,
so the values F(M )≃
∫
M A are equivalent.
23
This leaves the case of topological 4-manifolds, which do not admit ha ndle decompositions in
general. Because both F and
∫
A are symmetric monoidal, we can reduce to the case that M
is connected. Now, any connected topological 4-manifold M admits a smooth structure on the
complement M /i⋉tegerdivide{x} of a point x∈ M , [Qu]. Consequently, M /i⋉tegerdivide{x} admits a handle decomposition,
which can be constructed from any Morse function on M /i⋉tegerdivide{x}, and the preceding argument thereby
implies the equivalence F(M /i⋉tegerdivide{x})≃
∫
M/integerdivide{x} A. Applying the ⊗-excision property to the collar-
gluing M /i⋉tegerdivide{x} ⋃
Sn−1×R
Rn∼= M , since F and
∫
A agree on the constituent submanifolds, we obtain
the equivalence F(M )≃
∫
M A. Therefore every homology theory F for n-manifolds is equivalent to
factorization homology with coeﬃcients in F(Rn).
□
We record here this technical comparison of factorization homolog y with diﬀerent target ∞-
categories. (This result is also Proposition 5.5.2.17 of [Lu2].)
Lemma 3.25. For G : V→ V′ a symmetric monoidal functor between ⊗-presentable∞-categories
whose restriction to underlying ∞-categories preserves geometric realizations, there is a c anonical
equivalence
∫
◦G
≃
− →G◦
∫
of functors AlgDiskB
n
(V)→ Fun⊗(MﬂdB
n , V′).
Proof. The two functors agree on disjoint unions of Euclidean spaces, so it suﬃces to check that
G
∫
A is a homology theory with values in V′. This is immediate by the assumption on G. □
A result identical to Theorem 3.24 holds for topological n-manifolds with boundary.
Theorem 3.26. For V a symmetric monoidal ∞-category which is ⊗-presentable, and for B→
BTop(n) a map of spaces, there is an equivalence between ∞-categories
∫
: AlgDisk∂,B
n
(V) /d47/d47 H(Mﬂd∂,B
n , V) : evRn,Rn−1×[0,1)
/d111/d111
from Disk∂,B
n -algebras in V and homology theories of B-framed n-manifolds with coeﬃcients in V.
This equivalence is implemented by the factorization homol ogy functor
∫
and evaluation on B-framed
Euclidean n-spaces and half-spaces.
Proof. After Proposition 3.9 it is enough to consider the case where B is equivalent to BTop(n), and
so we omit it from the notation and discussion. Let F : Mﬂd∂
n→ V be a symmetric monoidal functor
satisfying the⊗-excision condition, and let A be the restriction of F to Disk∂
n. For a manifold with
boundary M , we prove that the canonical morphism
∫
M A→ F(M ) is an equivalence. By ⊗-excision
applied to the collar-gluing ∂M× [0, 1) ⋃
∂M×R
M∼= M , where M is the interior of M , we obtain a
diagram in V ∫
∂M ×[0,1)
A
⨂
∫
∂M ×R
A
∫
M
A /d47/d47
/d15/d15
F(∂M× [0, 1)) ⨂
F(∂M×R)
F(M )
/d15/d15∫
M
A /d47/d47 F(M )
in which the vertical morphisms are equivalences. It now suﬃces to s how that the top horizontal
morphism is an equivalence. The equivalences of
∫
M A→ F(M ) and
∫
∂M×R A→ F(∂M× R) are
given by Theorem 3.24; the last equivalence
∫
∂M ×[0,1) A→ F(∂M× [0, 1)) by follows by Theorem
3.24 and Proposition 2.16. □
Remark 3.27. There is an analogous theorem available for stratiﬁed spaces prove d in §2 of [AFT2],
where embeddings are conically smooth and preserve the stratiﬁca tions. The previous theorems hold
24
if the⊗-presentable condition is weakened to the condition that the monoid al structure distributes
over sifted colimits.
The following example describes how factorization homology specialize s to usual homology.
Example 3.28. Let V⊕ be either the ∞-category of chain complexes or of spectra equipped with the
direct sum monoidal structure. Since every object V therein has an essentially unique morphism
V⊕ V → V , there is an equivalence AlgDiskfr
n
(V⊕)≃ V. The factorization homology of a framed n-
manifold M with coeﬃcients in V is then equivalent to
∫
M V ≃ C∗(M, V ), or Σ ∞
∗ M⊗ V for spectra,
the stabilization of M smashed with V . There is a natural functor lim−→Mﬂdfr
n→ Spacesﬁn , and this
functor is an equivalence because: it is fully faithful since lim−→k Embfr(M× Rk, N× Rk)→ Map(M×
R∞, N× R∞)≃ Map(M, N ) is a weak homotopy equivalence for every M and N ; it is essentially
surjective since every ﬁnite CW complex X can be embedded into Rm for m suﬃciently large, and
thus it is homotopy equivalent to a framed n-manifold, namely an open regular neighborhood of the
embedding. Theorem 3.24 thereby specializes to the formulation of t he Eilenberg–Steenrod axioms
given in the introduction. If one sets V to be the opposite Chop, then one likewise recovers the
Eilenberg–Steenrod axioms for cohomology.
To this point, we have worked with topological manifolds and embeddin gs with the compact-open
topology, but other choices could have been made, for instance, t o work with smooth manifolds, or
to have regarded the embeddings spaces as discrete. We next rem ark on as to how these alternate
choices play out.
Remark 3.29. One could replace the ∞-category of topological n-manifolds and embeddings with
that of smooth n-manifolds and smooth embeddings, Mﬂdsm
n , or piecewise linear n-manifolds and
piecewise linear embeddings, MﬂdPL
n , and Theorem 3.24 is still valid. The proof, in fact, is even
simpler, as the existence of handlebody structures is much easier t han in the case of topological
manifolds. However, a consequence of smoothing theory [KS] is an equivalence
Mﬂdsm
n ≃ MﬂdBO(n)
n
between smooth n-manifolds and BO(n)-framed topological n-manifolds, so long as n is not equal
4, so nothing new is obtained by considering smooth or piecewise linear manifolds rather than
B-framed topological manifolds. In the case of smooth 4-manifolds, there is still an equivalence
Disksm
4 ≃ DiskBO(4)
4 , and so combining the smooth and topological versions of Theorem 3 .24 gives
an equivalence
H(Mﬂdsm
n , V)≃ H(MﬂdBO(4)
4 , V)
between homology theories for smooth 4-manifolds and homology th eories for BO(4)-framed topolog-
ical 4-manifolds. Since the BO(4)-framing on the tangent microbundle is only a very weak measure
of a smooth structure in dimension 4 (e.g., there is a single BO(4)-framing of R4, in contrast to the
uncountably many smooth structures), this form of factorizatio n homology is not a reﬁned invariant
of smooth 4-manifolds.
In the subsequent sections, we will be solely concerned with the hom ology theories of Deﬁnition
3.15. There do, however, exist very interesting functors in Fun⊗(Mﬂdn, V) which do not satisfy the
⊗-excision property. In [BFN] the authors were particularly concer ned with one such construction:
given a stack X over k, one can deﬁne a functor Mﬂdn → Stacks→ Modk given by sending a
manifold M to the cotensor with X, M↝ X M , and then taking sheaf cohomology of the structure
sheaf of this stack. In the case of the circle, M = S1, this gives the Hochschild homology of X:
O(X S1
)≃ HC∗(X). As soon as X is nonaﬃne, this construction will generically fail to satisfy ⊗-
excision. While the cotensor only depends on the homotopy type of M , as we shall see in Proposition
5.1, it has a more reﬁned generalization taking as input a derived stac k deﬁned over n-disk algebras,
rather than commutative algebras, as in [Fra1].
25
Deﬁnition 3.30. Let V be a symmtric monoidal ∞-category which is ⊗-presentable. For a B-
framed n-manifold M and a functor X : AlgDiskB
n
(V)→ Spaces, the factorization homology of M
with coeﬃcients in X is the object in V
∫
M
X := lim
A∈Aﬀ op
/X
∫
M
A
where Aﬀ≃ AlgDiskB
n
(V)op is the image of the Yoneda embedding in Fun
(
AlgDiskB
n
(V), Spaces
)
.
Intuitively, the object ∫
M X is Γ( X, ∫
M O), the global sections of the presheaf on X obtained
by applying factorization homology of M to the structure sheaf of X. From the vantage oﬀered
by Costello and Gwilliam in [CG], this generalization of factorization homolo gy serves as a candi-
date for the structure of observables in a topological quantum ﬁe ld theory which is not necessarily
perturbative, a direction we will pursue in future work.
4. Nonabelian Poincar ´e duality
Applying Theorem 3.24, we oﬀer a slightly diﬀerent perspective, and p roof, of the nonabelian
Poincar´ e duality of Salvatore [Sa], Segal [Se3], and Lurie [Lu2], which calculate factorization homol-
ogy with coeﬃcients in iterated loop spaces as a compactly supporte d mapping space.
Deﬁnition 4.1. For a space B, the ∞-category SpacesB is that of retractive spaces over B. The
∞-category Spaces≥n
B is the full ∞-subcategory of SpacesB consisting of those X⇄ B for which
the retraction is n-connective, that is, π∗X→ π∗B is an isomorphism for ∗ < n with any choice of
base-point of B.
Equivalently, an object X∈ Spaces≥n
B may be thought of as a ﬁbration X→ B with a distin-
guished section for which, for each b∈ B, the ﬁber Xb is n-connective.
Deﬁnition 4.2. For X∈ SpacesB and M→ B a space over B, the space Γ c(M, X ) of compactly
supported sections of X over M is the subspace of Map/B(M, X ) consisting of those maps f : M→ X
over B for which there is a compact subspace K⊂ M with the property that the restriction factors
through the section: f|M/integerdivideK : M→ B→ X.
For B→ BTop(n) as before, note that Γ c(−, X) deﬁnes a covariant functor MﬂdB
n → Spaces.
By inspection, this functor carries ﬁnite disjoint unions to ﬁnite pro ducts of spaces, which is to
say that Γ c(−, X) is symmetric monoidal with respect to the Cartesian monoidal stru cture on the
∞-category of spaces.
To easily state the next result, Theorem 4.4, we introduce some ter minology. Each point g∈ B
determines a symmetric monoidal functor Diskfr
n→ DiskB
n . Thereafter, each symmetric monoidal
functor A : DiskB
n→ Spaces determines the associative monoid
π0(A, g) : Diskfr
1
Rn−1×−
−−−−−→Diskfr
n−→ DiskB
n
A
−−→Spaces
π0
− −− →Set .
We say A is group-like if, for each g∈ B, this monoid π0(A, g) is a group.
Example 4.3. In the case B≃∗ so that a B-framing is a framing in the standard sense, a symmetric
monoidal functor A : Diskfr
n→ Spaces is the data of an En-algebra, and this En-algebra is group-like
in the standard sense if and only if A is group-like in the the sense just above.
Theorem 4.4. The functor Γc : SpacesB→ Fun⊗(MﬂdB
n , Spaces) restricts as a fully faithful functor
Spaces≥n
B֒→H(MﬂdB
n , Spaces)
from n-connective retractive spaces over B to homology theories. The essential image consists of
those F for which the restriction F| DiskB
n
is group-like.
26
The following is the core technical detail in the proof of Theorem 4.4, that the assignment of
compactly supported sections Γ c(−, X) is⊗-excisive in our sense, provided the retraction X→ B is
suﬃciently connected. The fullness of the functor above is a param etrized form of May’s theorem
from [Ma], identifying n-connective objects as Diskfr
n-algebras, which is Theorem 5.1.3.6 of [Lu2].
Lemma 4.5. Let M be B-framed manifold, equipped with a collar-gluing M ′ ⋃
M0×R
M ′′∼= M . Let
X∈ Spaces≥n
B be an n-connective space over B. There is a natural weak homotopy equivalence
Γc(M ′, X) ×
Γc(M0×R,X)
Γc(M ′′, X) ≃ Γc(M, X )
between the quotient of the product Γc(M ′, X)× Γc(M ′′, X) by the diagonal action of Γc(M0× R, X)
and the space of compactly supported sections of X over M .
Proof. Since M0֒→M is a proper embedding, a compactly supported section over M can be
restricted to obtain a compactly supported section over M0, as well as over M /i⋉tegerdivideM ′ and over
M /i⋉tegerdivideM ′′. Namely, there is a diagram among spaces of compactly supported s ections
Γc(M ′, X)× Γc(M ′′, X)
/d41/d41❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚ /d47/d47
/d15/d15
Γc(M ′′, X)
/d15/d15
Γc(M, X ) /d47/d47
/d15/d15 /d40/d40❘❘❘❘❘❘❘❘❘❘❘❘❘ Γc(M /i⋉tegerdivideM ′, X)
/d15/d15
Γc(M ′, X) /d47/d47 Γc(M /i⋉tegerdivideM ′′, X) /d47/d47 Γc(M0, X).
By inspection, the bottom horizontal sequence is a ﬁber sequence , as is the right vertical sequence, as
is the diagonal sequence. Also, the inner square is pullback because M ′ ⋃
M0×R
M ′′∼= M is a pushout.
Because M0⊂ M is equipped with a regular neighborhood, these ﬁber sequences are in fact Serre
ﬁbration sequences, and so the inner square is a weak homotopy pu llback square. In particular,
there is a right homotopy coherent action of Ω Γ c(M0, X) on Γ c(M ′, X), a left homotopy coherent
action of Ω Γ c(M0, X) on Γ c(M ′′, X), and a continuous map of topological spaces
(7) Γ c(M ′, X) ×
Ω Γ c(M0,X)
Γc(M ′′, X)−→ Γc(M, X )
from the balanced homotopy coinvariants. Because X → B is n-connective and M0 is ( n− 1)-
dimensional, the base Γ c(M0, X) is connected. It follows that the map (7) is in fact a weak homotopy
equivalence. The assertion follows after the canonical identiﬁcatio n Ω Γ c(M0, X)∼= Γc(M0× R, X)
as group-like E1-spaces.
□
As a consequence, we recover the following theorem of Salvatore [S a], Segal [Se3], and Lurie [Lu2].
Corollary 4.6 (Nonabelian Poincar´ e duality). For any X in Spaces≥n
B , with associated DiskB
n -
algebra Ω n
BX∈ AlgDiskB
n
(Spaces), there is a natural equivalence
∫
M
Ω n
BX ≃ Γc(M, X )
between the factorization homology of a B-framed n-manifold M with coeﬃcients in Ω n
BX and the
space of compactly supported sections of X over M .
Proof. We apply Theorem 3.24: Since Γ c(−, X) is a homology theory, it is equivalent to factorization
homology with coeﬃcients in Γ c(Rn, X), which is identiﬁed as the n-fold loop space of the ﬁber of
the map X→ B, Γ c(Rn, X)≃ Ω n
BX. □
27
This result specializes to Poincar´ e duality between twisted homology and compactly supported
cohomology, as we will now explain. Given X≃ BTop(n)× K(A, i) a product with an Eilenberg-
MacLane space, then Ω n
BTop(n)X≃ Mapc(Rn, K(A, i))≃ K(A, i− n) is an n-disk algebra in spaces,
where the multiplication is the usual group structure on K(A, i−n) but is equipped with a nontrivial
action of Top(n). We then have an equivalence of spaces
∫
M
Mapc(Rn, K(A, i))≃ Mapc(M, K (A, i))
which is the space level version of the equivalence Hτ
∗(M, A[i− n])≃ H∗
c (M, A[i]), obtained by
applying Ω ∞ to the spectrum level equivalence given by Atiyah duality. Given an A-orientation of
M , then one can additionally untwist the lefthand side, as usual.
Remark 4.7. The factorization homology
∫
M Ω n
BX is built from conﬁguration spaces of disks in M
with labels deﬁned by X → B, and the preceding result thereby has roots in the conﬁguration
space models of mapping spaces dating to the work of Segal, May, Mc Duﬀ and others in the 1970s,
see [Se1], [Ma], [Mc], and [B¨ o]. Factorization homology is not a generaliza tion of the classical
conﬁguration spaces with labels, as described in [B¨ o], because the c onﬁguration space with labels
in X models a mapping space with target the n-fold suspension of X, rather than into X itself.
Instead, factorization homology generalizes the conﬁguration sp aces with summable or amalgamated
labels of Salvatore [Sa] and Segal [Se3].
Proof of Theorem 4.4. Corollary 4.6 identiﬁes the functor Γ c : Spaces≥n
B → H(MﬂdB
n , Spaces) as
the composition Γ c : Spaces≥n
B
Ω n
B
−−→DiskB
n
∫
− →H(MﬂdB
n , Spaces). Theorem 3.24 gives that
∫
is fully
faithful, so it remains to argue that Ω n
B is fully faithful with essential image the group-like DiskB
n -
algebras in spaces. This is immediate because, for instance, Spaces/B is an ∞-topos (Theorem
5.1.3.6 of [Lu2]).
□
