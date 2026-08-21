---
doc_id: arxiv-math-0305275v1
doc_title: "Hyperbolic volume of representations of fundamental groups of cusped 3-manifolds"
section_id: sec-003-comparison-with-simplicial-volume
section_title: "Comparison with simplicial volume"
section_number: null
pages: 15-21
source_pdf: 0305275v1.pdf
source_sha256: 9b356a9d716a0d3e
doc_brief: "Hyperbolic volume of representations of fundamental groups of cusped 3-manifolds — Let W be a compact manifold and let ρ be a representation of its fundamental group into PSL(2 , C)."
---
Here we generalize the argument used to prove Theorem 4.10 to com pare
vol(ρ) with the simplicial volume of M, obtaining exactly the expected in-
equality.
Let ||(
M,∂M )|| be the simplicial volume of M relative to the boundary
(see [BP], [G], [Ku], [Th1] for more details), and let v3 be the volume of a
regular straight ideal tetrahedron of H3.
Theorem 5.1 For any representation ρ :π1(M) → Isom+(H3) we have
|vol(ρ)| ≤ v3 · ||(M,∂M )||.
Proof. For the proof we ﬁx a representation ρ : π1(M) → Isom+(H3) and a
pseudo-developing map Dρ for ρ.
Let c = ∑
iλiσi be a smooth singular chain in M ; here each simplex σi
is a piecewise smooth map from the standard tetrahedron ∆ 3 to M . The
simplicial volume of c is deﬁned as ||c|| = ∑ |λi|. The relative simplicial
volume of (M,∂ M ) is deﬁned as
||(M,∂M )|| = inf {||c|| : [c] = [M ] ∈H3(M,∂ M )}.
The proof has two main steps:
15
1. Given a smooth cycle c = ∑
iλiσi representing [M ], show that vol(ρ) =∑
i
∫
∆ 3λiσ∗
i (D∗
ρω), where ω is the volume form of H3.
2. By replacing c with its straightening, show that vol(ρ) = ∑
iλivi, where
vi is the volume of a straight version of σi.
From Step 2 it follows that
|vol(ρ)| ≤
∑
i
|λi| · |vi| ≤ v3 · ||c||.
Theorem 5.1 follows taking to the inﬁmum over all c’s representing [M].
Step 1 . Since a pseudo-developing map has the cone property on the cusp s,
the 3-form D∗
ρω deﬁned on M extends to a 3-form on M that vanishes at
the boundary. So we can consider the class [ D∗
ρω] ∈ H 3(M,∂M ). Since
[c] = [M ], then
vol(ρ) =
∫
M
D∗
ρω = ⟨[D∗
ρω], [M]⟩ = ⟨[D∗
ρω], [c]⟩ =
∑
i
∫
∆ 3
λiσ∗
i (D∗
ρω).
Step 2 . The idea is the following. Consider a lift ~c ofc to ˆ~M . Let c = (Dρ)∗~c
be the push-forward of ~c to H3 via Dρ and let Str( c) be a straightening of
c. Since the straightening is homotopic to the identity, then there ex ists a
chain-homotopy of degree one i.e. a map H from k-chains to (k + 1)-chains
such that Str − Id = H ◦∂ −∂ ◦H. Then we have
vol(ρ) = ⟨D∗
ρω, ~c⟩ = ⟨ω, (Dρ)∗~c⟩ = ⟨ω,c⟩
= ⟨ω, Str(c)⟩ + ⟨ω,∂H c⟩ − ⟨ω,H∂ c⟩
=
∑
i
λivi + ⟨dω,Hc⟩ − ⟨ω,H∂ c⟩.
The last two summands are zero because dω = 0 and, even if ∂c ⁄= 0,
everything can be made ρ-equivariantly so that the action of ρ cancels out
in pairs the contributions of ⟨ω,H∂ c⟩.
We formalize now this argument. Let Ck(X) denote the real vector space
of ﬁnite singular, piecewise smooth k-chains in a space X. Consider the
projection M → ˆM obtained by collapsing each boundary torus to a point.
Given a relative cycle c = ∑
iλiσi in Ck(M) i.e. a chain c such that ∂c ∈
Ck−1(∂M ), we also call c the chain induced on Ck( ˆM) with ∂c ∈ Ck(ideal
points). We call ~c a lift of c to ˆ~M , that is ~c = ∑
iλi~σi ∈Ck(ˆ~M ) where each
~σi is a lift of σi.
16
Remark 5.2 The chain ~c in general is not a relative cycle. Nevertheless,
since c is a relative cycle, assuming ∂~c = ∑
jljηj, there exists a family {αj}
of elements of π1(M) such that
∑
j
lj ·αj∗(ηj) ∈Ck(ideal points)
where π1(M) acts on ~M via deck transformations and αj∗(ηj) is the compo-
sition of αj with ηj.
We setσi = (Dρ)∗(~σi) and c = ∑
iλiσi = (Dρ)∗(~c) ∈Ck(H
3
). We restrict
now the class of simplices we want to use.
Deﬁnition 5.3 We call a k-simplex σ : ∆ k →
H
3
admissible if for any sub-
simplex η of σ, if the interior of η touches ∂H3 then η is constant. A chain
is admissible if its simplices are admissible.
Lemma 5.4 Letc′ = ∑
iλiσ′
i be a relative cycle in Ck(
M). Then there exists
a cycle c = ∑
iλiσi (with the same λi’s) such that [c′] = [ c] ∈ Hk(M,∂ M )
and such that c is admissible.
Proof. For any chain β ∈Ck(M ), deﬁne span(β) as the set of all the subsim-
plices ofβ (of any dimension). Given the chain c′, constructc as follows: near
∂M push c′ a little inside M, keeping ﬁxed only the simplices of span( ∂c′).
This operation can be made via an homotopy, so [c] = [c′]. Moreover, the only
simplices of c that touch∂M are the ones of span(∂c). Finally, c is admissible
because, if σi(x) ∈∂H3, then from the deﬁnition of pseudo-developing map
it follows that σi(x) is an ideal point. Thus x lies on a face F ofσi such that
the simplex η = (σi)|F belongs to span( ∂c). It follows that ~η is a constant
map and then also η is constant.
✷
We call C k(H
3
) the vector space of admissible chains. Note that the
boundary operator is well-deﬁned on ⊕kC k(H
3
) (The boundary of an admis-
sible cycle is admissible).
Deﬁnition 5.5 For any admissible simplex σ : ∆ k →
H
3
, a straightening
Str(σ) : ∆ k → H
3
is a simplex agrees with σ on the 0-skeleton, moreover
we require Str( σ) to be a standard map whose image is the convex hull
of its vertices. For any chain c = ∑
iλiσi a straightening of c is a chain
Str(c) = ∑
iλiStr(σi).
17
A straightening of a simplex is admissible because any straight simplex is
admissible. The straightening of a simplex is not unique in general. Neve r-
theless, as the following lemma shows, it is possible to choose a straigh tening
for any simplex compatibly with the boundary operator of ⊕kC k(H
3
).
Lemma 5.6 There exists a chain-map Str : ⊕kC k(H
3
) → ⊕ kC k(H
3
) that
maps each simplex to one of its straightenings and such that f or any isometry
γ of H3, γ∗ ◦ Str = Str ◦ γ∗.
Proof. LetK be the set of pairs {(B,f )} whereB is a sub-space of ⊕kC k(H
3
)
and f :B → ⊕ kC k(H
3
) is a linear map, such that:
• ∂(B) ⊂B.
• ∀γ ∈ Isom(H3), γ∗(B) ⊂B.
• ∀σ ∈B, f (σ) is a straightening of σ.
• ∀γ ∈ Isom(H3), f ◦γ∗ =γ∗ ◦f .
• f ◦∂ =∂ ◦f .
Note that K is not empty because each 0-simplex is admissible and it
is itself its unique straightening, so that ( C 0(H
3
),Id ) ∈ K. We order K by
inclusion (i.e. (B,f ) ≺ (C,g ) iﬀ B ⊂C andg|B =f ) and use Zorn’s lemma.
Let {(Bξ,f ξ)} be an ordered sequence in K. Clearly
(B∞ = ∪ξBξ,f ∞ = ∪ξfξ)
is an upper bound for {(Bξ,f ξ)}. It follows that there exists a maximal
element (B,f ) ∈ K. We claim that B = ⊕kC k(H
3
). Suppose the contrary.
Let k = min{n ∈ N :C n(H
3
) ⁄⊂B} and let σ be a simplex of C k(H
3
) \B. If
k = 0, set B1 the space spanned by B and
⋃
γ ∈Isom(H)3
γ∗(σ), deﬁne f (σ) = σ,
f (γ∗(σ)) = γ∗(f (σ)) and extend f on B1 by linearity. Then
(B,f ) ≺ (B1,f )
contradicting the maximality of (B,f ). If k >0, then f is deﬁned on ∂σ and,
as f (∂σ) is standard, it is not hard to show that it extends to a standard
map f (σ) deﬁned on the whole ∆ k. Then deﬁne B1 and extend f to B1 as
above. Again we have ( B,f ) ≺ (B1,f ), that contradicts the maximality of
(B,f ).
ThusB = ⊕kC k(H
3
) and f is the requested chain map Str.
✷
18
Lemma 5.7 There exists a homotopy operator H : ⊕kC k(H
3
) → ⊕ kC k(H
3
)
between Str and the identity such that H ◦γ∗ =γ∗ ◦H for any isometry γ of
H3.
Proof. A homotopy operator between Str and Id is a chain map of degree 1,
i.e. a map H :C k(H
3
) →C k+1(H
3
), such that
Str −Id =∂ ◦H −H ◦∂.
For any admissible σ : ∆ k → H
3
, let hσ (t,x ) be the homotopy constructed as
follows: hσ (t,x ) is the convex combination from σ(x) to Str(σ)(x) if σ(x) /∈
∂H3 and hσ (t,x ) = σ(x) otherwise. Note that from the admissibility of σ it
follows thathσ (∞,x ) = Str(σ)(x) for anyx. So the hσ actually is a homotopy
betweenσ and Str(σ).
As hσ is a map hσ : ∆ k × [0, ∞] → H
3
, up to triangulating ∆ k × [0, ∞],
it is a chain in Ck+1(H
3
). Fix a canonical triangulation of ∆ k × [0, ∞] and
deﬁne H(σ) as hσ . Since
∂(∆ k × [0, ∞]) = ∆ k × {∞} − ∆ k × {0} +∂∆ k × [0, ∞]
then ∂ ◦H = Str −Id +H ◦∂.
Sincehσ is constructed using geodesic rays, then for every isometry γ we
havehγ ◦σ =γ ◦hσ . It follows that H ◦γ∗ =γ∗ ◦H.
Finally, admissibility of hσ follows from admissibility of σ.
✷
Lemma 5.8 Let c = ∑
iλiσi be a chain in Ck(M ). Let {γj} be a ﬁnite set
of isometries and let A be the hyperbolic convex hull in H3 of
⋃
i,j
γj(Im(σi)).
Then A has ﬁnite volume.
Proof. Since Dρ has the cone property on the cusps and since c is a ﬁnite
sum of simplices, then A is contained in a geodesic polyhedron with a ﬁnite
number of vertices, and such a polyhedron has ﬁnite volume.
✷
We are now ready to complete the proof of Theorem 5.1. Let c =∑
iλiσi be a relative cycle in C3(M) such that [ c] = [ M] in H3(M,∂ M ).
By Lemma 5.4 we can suppose that c is admissible. Assume ∂~c = ∑
jljηj.
19
By Remark 5.2, there exists a ﬁnite set {αj} ⊂ π1(M) such that ∑
jlj ·αj∗ηj ∈
C2(ideal points).
LetA be as in Lemma 5.8, where we use {ρ(αj)}∪{ Id} as the set of isome-
tries. Since A has ﬁnite volume, then the volume form ω of H3 is an element
of H 3(A). Moreover, the straightening of any admissible simplex in C k(A)
is contained in C k(A) and, since the homotopy operator H is constructed
using convex combinations, then H is well-deﬁned on ⊕kC k(A). Called vi
the volume of the straight version of σi, we have
vol(ρ) = ⟨D∗
ρω, ~c⟩ = ⟨ω, (Dρ)∗(~c)⟩ = ⟨ω,c⟩
= ⟨ω, Strc⟩ + ⟨ω,H∂ c⟩ − ⟨ω,∂H c⟩
= ∑
iλivi + ⟨ω,H∂ c⟩ − ⟨dω,Hc⟩ = ∑
iλivi + ⟨ω,H∂ c⟩
By Lemma 5.7 we have ρ(αj)∗H = Hρ(αj)∗. Moreover, the volume form is
invariant by isometries. It follows that
⟨ω,H∂ c⟩ = ⟨ω,H ∑
jlj(Dρ)∗ηj⟩ = ∑
jlj⟨ω,H (Dρ)∗ηj⟩
= ∑
jlj⟨ρ(αj)∗ω,H (Dρ)∗ηj⟩ = ∑
jlj⟨ω,ρ (αj)∗H(Dρ)∗ηj⟩
= ∑
jlj⟨ω,Hρ (αj)∗(Dρ)∗ηj⟩ = ∑
jlj⟨ω,H (Dρ)∗αj∗ηj⟩
= ⟨ω,H (Dρ)∗
∑
jljαj∗ηj⟩.
The last product is zero because Dρ∗
∑
jljαj∗ηj lies on the ideal points of A,
where H is ﬁxed and ω vanishes.
This completes the proof of Theorem 5.1.
✷
Remark 5.9 Theorem 5.1 applies when the cycle c is an ideal triangulation.
So it implies Theorem 4.10.
Corollary 5.10 LetM be a graph 3-manifold. Then for all representations
ρ :π1(M) → Isom+(H3) we have vol(ρ) = 0 .
Proof. This is because for each graph manifold M we have ||(M,∂M )|| = 0
(see [G], [Ku]).
✷
Corollary 5.11 LetM be a complete hyperbolic 3-manifold of ﬁnite volume.
Then for all representations ρ : π1(M) → Isom+(H3) we have |vol(ρ)| ≤
vol(M).
20
Proof. This follows from the fact that for complete hyperbolic 3-manifold we
have vol(M) = v3||(M,∂M )|| (see [G], [Ku]).
✷
In [D] it is proved that, for compact manifolds, equality holds if and on ly
if ρ is discrete and faithful. In the next section we show that this is true in
general for manifolds of ﬁnite volume.
