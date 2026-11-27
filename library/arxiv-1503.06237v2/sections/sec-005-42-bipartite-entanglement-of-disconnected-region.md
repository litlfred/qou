---
doc_id: arxiv-1503.06237v2
doc_title: "Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence"
section_id: sec-005-42-bipartite-entanglement-of-disconnected-region
section_title: "Bipartite entanglement of disconnected regions"
section_number: 4.2
pages: 13-16
source_pdf: 1503.06237v2.pdf
source_sha256: 55572e7133514f4a
toc_source: outline
doc_brief: "Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence — We propose a family of exactly solvable toy models for the AdS/CFT correspondence based on a novel"
---
Unfortunately the proof of Theorem 2 does not directly generalize to a disconnected
regionA, nor even to connected regions for states, such as our holographic code states,
where not all perfect tensor indices are contracted in the bulk. We do not consider
this to be a serious problem for our models. However, we still ﬁnd it worthwhile to
introduce some machinery that allows us to quantify this presumption somewhat.
The ﬁrst technique we will introduce is an algorithmic procedure for constructing,
given a boundary regionA, a bulk curveγ⋆
A bounded by∂A such that the corresponding
tensorP is guaranteed to be an isometry. For a holographic state the isometry P maps
γ⋆
A to A, and for a holographic code P maps γ⋆
A and all incoming bulk indices of P to
A. Furthermore, γ⋆
A is a local minimum of the length, in the sense that no single tensor
can be added to or removed from P which reduces the length of the cut.
The algorithm makes essential use of the properties of perfect tensors and is quite
simple. We consider a sequence of cuts{cα} each bounded by∂A, and a corresponding
sequence of isometries {Pα}, such that each cut in the sequence is obtained from the
previous one by a local move on the bulk lattice. The sequence begins with the trivial
3The scalar curvature of a graph is somewhat tricky to deﬁne in general; the condition we really
need here is that the distance functional from one point on the dual network to another does not have
interior local maxima.
– 11 –
cut, A itself; in each step we identify one perfect tensor which has at least half of its
legs contracted with Pα and construct Pα+1 by adding this perfect tensor to Pα. Thus
Pα+1 is obtained by composing Pα with an isometry deﬁned by a perfect tensor, and
thereforePα+1 is an isometry ifPα is. The procedure halts when the cut reaches γ⋆
A and
no further local moves are possible. Though many diﬀerent sequences of local moves
are allowed,γ⋆
A is well deﬁned; tensors eligible for inclusion in Pα+1 remain so as other
tensors are included, so the output of the algorithm does not depend on the order of
inclusion. Following standard computer science terminology, we call this procedure the
greedy algorithm and call γ⋆
A the greedy geodesic. A step of the greedy algorithm is
illustrated in ﬁgure 6.
Figure 6 . A step in the greedy algorithm. The upper node has at least three legs contracted
with the region P , which we have shaded red, so we include it into P .
Figure 7 . Three examples where the greedy algorithm fails to ﬁnd the matching minimal
geodesics from complementary regions. The ﬁrst example involves disconnected regions in
the holographic state. The second example involves a positive curvature obstruction at the
center of the tiling which blocks the greedy geodesic from reaching the global minimal surface.
The third example involves a connected region for the holographic code. In both the ﬁrst and
the third ﬁgure the greedy algorithm ﬁnds minimal geodesics from both sides but they do
not match. In both cases, it is possible for the entropy to be slightly smaller than the length
of the geodesic. This depends on tensors which were not absorbed by either of the greedy
geodesics which we call the bipartite residual regions.
When the assumptions of Theorem 2 are satisﬁed, the argument in appendix B
ensures that the greedy algorithm will ﬁnd a true minimal geodesic γA. If there is
– 12 –
more than one minimal geodesic, as is sometimes the case, then the greedy algorithm
might continue past a minimal geodesic and proceed through minimal geodesics of
equal length. In that case, the tensors in between the successive geodesics deﬁne a
unitary transformation from one cut to the other. If A has more than one connected
component, if there is positive curvature, or if there are uncontracted bulk indices as
for a holographic code, the greedy algorithm does not necessarily succeed in ﬁnding
matching minimal geodesics, as we illustrate in ﬁgure 7.
In cases where the greedy algorithm fails to ﬁnd a minimal geodesic, we can still
use it to prove an interesting lower bound on the entropy SA. Suppose that γ⋆
A and
γ⋆
Ac are two greedy geodesics, produced by applying the greedy algorithm to A and its
complement Ac respectively, where P and Q are the corresponding tensors. Further-
more, suppose that γ⋆
A∩γ⋆
Ac is non-empty, in the sense that some links are cut by both
geodesics. We can represent that state as 4
|ψ⟩ =
∑
a,b,i,j,k
|ab⟩Pa,ijQb,ikSjk≡
∑
i,j,k
Sjk|Pij⟩A⊗|Qik⟩Ac. (4.5)
Here i denotes the index shared between γ⋆
A and γ⋆
Ac, j is the index unique to γ⋆
A, k is
the index unique to γ⋆
Ac, and S denotes the tensor that sits “in between” γ⋆
A and γ⋆
Ac.
We call the set of lattice sites in S the bipartite residual region (where the modiﬁer
“bipartite” draws a distinction with the multipartite residual region to be discussed
in section 4.3.) Because P and Q are isometries, both {|Pij⟩} and{|Qik⟩} are sets of
orthonormal vectors. Therefore, the marginal density operator for A is
ρA =
∑
i,j,j′,k
SjkS∗
j′k|Pij⟩⟨Pij′|. (4.6)
This density operator has support on the subspace of A spanned by{|Pij⟩}, which has
dimension v|γ⋆
A|, and this subspace has a decomposition into subsystems A1⊗A2 such
that the basis element |Pij⟩ may be expressed as |i⟩A1⊗|j⟩A2, where {|i⟩} and{|j⟩}
are orthonormal bases for A1 and A2 respectively. We may then write
ρA =
(∑
i
|i⟩⟨i|A1
)
⊗
(∑
j,j′,k
SjkS∗
j′k|j⟩⟨j′|A2
)
, (4.7)
4For holographic codes with dangling bulk legs, we assume for now that a product state is fed into
all bulk legs. If the input bulk state were entangled instead, there would be additional contributions
to the boundary entanglement which we are not including. This same proviso also applies to the
discussion in the following subsection.
– 13 –
and from the additivity of the entropy, using dim( A1) = v|A1| = v|γ⋆
A∩γ⋆
Ac|, we obtain
the following theorem.
Theorem 3. For a holographic state or code, if A is a (not necessarily connected)
boundary region and Ac is its complement, then the entropy of A satisﬁes
SA≥|γ⋆
A∩γ⋆
Ac|, (4.8)
whereγ⋆
A is the greedy geodesic obtained by applying the greedy algorithm to A and γ⋆
Ac
is the greedy geodesic obtained by applying the greedy algorithm to Ac.
We see from Theorem 3 that violations of the Ryu-Takayanagi formula are closely
related to the size of the bipartite residual region. In particular, if there is no bipartite
residual region then SA = |γ⋆
A|; the upper bound (4.4) and the lower bound (4.8)
together imply that γ⋆
A is in fact a minimal geodesic, and RT holds. We will argue in
section 4.3 that the bipartite residual region has size O(1) when the regions A and Ac
on the boundary have O(1) connected components. In this sense, the corrections to
the RT formula are typically small.
