---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY TOM BRIDGELAND"
section_id: sec-044-b1-convergent-bps-structures
section_title: "B.1. Convergent BPS structures"
section_number: null
pages: 43-45
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY TOM BRIDGELAND — We study a class of Riemann-Hilbert problems arising naturally in Donald son-Thomas theory."
---
2.6 that a BPS structure (Γ , Z, Ω) is
called convergent if there exists R > 0 such that
∑
γ∈Γ
|Ω( γ)|· e−R|Z(γ)| <∞. (52)
Let us ﬁx an arbitrary norm ‖·‖ on the ﬁnite-dimensional vector space Γ ⊗Z R. Then we can ﬁnd
k1 < k 2 such that for any active class γ∈ Γ there are inequalities
k1·‖ γ‖ <|Z(γ)| < k 2·‖ γ‖. (53)
The ﬁrst inequality is the support property and requires the assum ption that γ ∈ Γ is active,
whereas the second is just the fact that the linear map Z : Γ ⊗Z R→ C has bounded norm. It
follows that in expressions such as ( 52), which are sums over active classes, we can equally well
use‖γ‖ or|Z(γ)| in the exponential factor.
Lemma B.1. Let (Γ , Z, Ω) be a convergent BPS structure and choose a norm ‖·‖ as above. Then
for any ǫ > 0 there is an R > 0 such that
∑
γ∈Γ
‖γ‖p·| DT(γ)|· e−R‖γ‖ < ǫ, (54)
for each integer p∈{ 0, 1, 2}.
Proof. Clearly it is enough to prove the result for each p∈{ 0, 1, 2} separately, so we can consider
p ﬁxed. For x≫ 0 there is an inequality
xp
e2x− 1 < e −x.
By the discussion above, we can take S > 0 so that the inequality ( 52) holds with R = S and|Z(γ)|
replaced with‖γ‖ in the exponential factor. The numbers ‖γ‖ are bounded below so increasing S
44 TOM BRIDGELAND
if necessary we can assume that
Sp‖γ‖p· (e2S‖γ‖− 1)−1 < e −S‖γ‖ < 1,
for all classes γ∈ Γ. Taking R = 2S and using the deﬁnition of DT invariants ( 2) gives
∑
γ∈Γ
‖γ‖p·| DT(γ)|· e−R‖γ‖ =
∑
γ∈Γ
∑
n≥1
1
n2·‖ nγ‖p·| Ω( γ)|· e−2nS‖γ‖
≤
∑
γ∈Γ
‖γ‖p·| Ω( γ)|· e−2S‖γ‖
1− e−2S‖γ‖ < S −p·
∑
γ∈Γ
|Ω( γ)|· e−S‖γ‖ <∞.
Since the numbers‖γ‖ appearing in the exponential factor are bounded below, by increas ing R we
can ensure that this sum is smaller than any given ǫ > 0. □
B.2. Partially deﬁned automorphisms. Let (Γ , Z, Ω) be a BPS structure, and ﬁx a convex
sector ∆ ⊂ C∗. As above, we also ﬁx a norm ‖·‖ on the vector space Γ ⊗Z R. In the next
subsection we will be interested in controlling Hamiltonian ﬂows of func tions on the twisted torus
T of the form DT( γ)· xγ, for those classes γ∈ Γ satisfying Z(γ)∈ ∆. Thus it makes sense to
deﬁne, for each real number R > 0, a subset
V∆ (R) =
{
ξ∈ T : γ∈ Γ active with Z(γ)∈ ∆ = ⇒ |xγ(ξ)| < exp(−R‖γ‖)
}
.
It is not clear that the subset V∆ (R)⊂ T is open in general, so we deﬁne U∆ (R) to be its interior.
We note the obvious implications
R2≥ R1 =⇒ U∆ (R2)⊆ U∆ (R1), ∆ 2⊇ ∆ 1 =⇒ U∆ 2(R)⊆ U∆ 1(R).
We think of the open subsets U∆ (R)⊂ T as forming a system of neighbourhoods of the boundary
in some ﬁctitious partial compactiﬁcation of T.
Lemma B.2. The open subset U∆ (R) = int V∆ (R)⊂ T is non-empty.
Proof. Take an element z∈ ∆. Since ∆ is acute we can ﬁnd a constant k > 0 such that
Z(γ)∈ ∆ = ⇒ Re
(
Z(γ)/z
)
> k·| Z(γ)|.
Take a point ξ∈ T. Using the support property, we conclude that for any active clas s γ∈ Γ with
Z(γ)∈ ∆, and all real numbers S > 0, there are inequalities
|e−SZ (γ)/z· ξ(γ)| = e−S Re(Z(γ)/z)·| ξ(γ)| < e −kS|Z(γ)|·| ξ(γ)| < e −cS‖γ‖·| ξ(γ)|,
RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY 45
for some universal constant c > 0. Since the numbers ‖γ‖ are bounded below, it follows that
the element e−SZ/z· ξ∈ T lies in the subset V∆ (R) for suﬃciently large S > 0. The argument
applies uniformly to all elements ξ lying in a compact subset of T, so we conclude that V∆ (R) has
non-empty interior. □
Let us deﬁne a ∆-map germ to be an equivalence class of holomorphic m aps of the form
f : U∆ (R)→ T, where two such maps fi : U∆ (Ri)→ T are considered to be equivalent if they
agree on the intersection U∆ (max(R1, R2)) of their domains. Thus a ∆-map germ gives a partially-
deﬁned holomorphic map f : T /axisshort/axisshort/arrowaxisrightT which is well-deﬁned on the open subset U∆ (R)⊂ T for all
suﬃciently large R > 0. A ∆-map germ f will be called bounded if for any ǫ > 0 one has
f (U∆ (R + ǫ))⊂ U∆ (R) (55)
for all suﬃciently large R > 0.
It is clear from ( 55) that composition of such maps is well-deﬁned and hence gives the se t of
bounded ∆-map germs the structure of a monoid. We write Aut ∆ (T) for the group of invertible
elements in this monoid, and call the elements of this group invertible b ounded ∆-map germs.
Elements of Aut ∆ (T) give partially-deﬁned holomorphic maps f : T /axisshort/axisshort/arrowaxisrightT with partially-deﬁned
inverses, and hence give a precise meaning to the idea of a partially-d eﬁned automorphism of T.
