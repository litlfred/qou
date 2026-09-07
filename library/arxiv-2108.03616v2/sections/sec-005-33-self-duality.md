---
doc_id: arxiv-2108.03616v2
doc_title: "Circuit imbalance measures and linear programming ∗"
section_id: sec-005-33-self-duality
section_title: "Self-duality"
section_number: 3.3
pages: 10-12
source_pdf: 2108.03616v2.pdf
source_sha256: 63696ad045602440
doc_brief: "Circuit imbalance measures and linear programming ∗ — We study properties and applications of various circuit imbalance mea sures associated with linear spaces."
---
We next show that both κW and ˙κW are self-dual. These rely on the following duality property
of circuits. We introduce the following more reﬁned quantit ies that will also come useful later
on.
10
Deﬁnition 3.11 (Pairwise Circuit Imbalances) . For a space W ⊆ Rn and variables i,j ∈ [n]
we deﬁne
KW
ij :=
{ ⏐⏐⏐⏐
gj
gi
⏐⏐⏐⏐ :{i,j}⊆ supp(g),g∈F (W )
}
, κ W
ij := maxKW
ij ,
˙KW
ij :=
{
lcm(p,q ) : p,q∈ N, gcd(p,q ) = 1,p
q∈K W
ij
}
.
We call κW
ij the pairwise imbalance between i and j.
Cleary, κW = maxi,j∈[n]κW
ij for a nontrivial linear space W . We use the following simple
lemma.
Lemma 3.12. Consider a matrix A∈ Rm×n in basis form for B⊆ [n], i.e., AB = Im. Let
W = ker(A); thus, W ⊥ = span(A⊤). The following hold.
(i) The rows of A form a circuit basis of W ⊥, denoted as FB(W ⊥).
(ii) For any two rows Ai,Aj, i,j ∈B, i⁄=j, and k∈ [n]\B, the vector h =AjkAi−AikAj
fulﬁlls h∈F (W ⊥).
Proof. For part (i), the rows are clearly linearly independent and span W ⊥. Therefore, every
g∈W ⊥ must have supp(g)∩B⁄=∅, and if supp( g)∩B ={i} then g =giAi. These two facts
imply that each Ai is support minimal in W ⊥, that is, Ai∈F (W ⊥).
For part (ii), there is nothing to prove if Aik = 0 or Ajk = 0; for the rest, assume both
are nonzero. Assume for a contradiction h /∈F (W ⊥); thus, there exists a g∈ W ⊥, g⁄= 0 and
supp(g) ⊊ supp(h). We have supp( h)∩B ={i,j}. If supp( g)∩B ⊊ {i,j}, as above we get that
g =giAi org =gjAj, a contradiction since hk = 0 but Aik,Ajk⁄= 0. Hence, supp( g)∩B ={i,j}.
By part (i), we have g =giAi +gjAj; and since hk = 0 it follows that gi/gj =−Ajk/Aik; thus,
g is a scalar multiple of h, a contradiction.
Lemma 3.13. For any i,j ∈ [n] we have KW
ij =
{
α−1 :α∈K W ⊥
ji
}
. Equivalently: for every
elementary vector g∈F (W ) with indices i,j ∈ supp(g) there exists an elementary vector h∈
F(W ⊥) such that |hi/hj| =|gj/gi|.
Proof. Let g∈F (W ) such that i,j ∈ supp(g). If supp( g) = {i,j} then any h∈F (W ⊥) with
i∈ supp(h) fulﬁlls gihi +gjhj =⟨g,h⟩ = 0, so j∈ supp(h) and|hi/hj| =|gj/gi|.
Else, there existsk∈ supp(g)\{i,j}. Let us select a basis B ofM(W ) with supp(g)\B ={k}.
Let A∈ Rm×n be a matrix in basis form for B with ker(A) = W , and let h =AjkAi−AikAj,
an elementary vector in F(W ⊥) by Lemma 3.12(ii).
By the construction, |hi/hj| =|Ajk/Aik|. On the other hand,
⟨
g,Ai⟩
= 0 and supp(g)\B =
{k} implies gi =−gkAik and similarly
⟨
g,Aj ⟩
= 0 implies gj =−gkAjk . The claim follows.
ForκW , duality is immediate from the above:
Proposition 3.14 ([DHNV20]). For any linear subspace W⊆ Rn, we have κW =κW ⊥.
Let us now show duality also for ˙ κW ; this was shown in [ Lee89, Lemma 2.1] in a slightly
diﬀerent form.
Proposition 3.15. For any rational linear subspace W⊆ Rn, we have ˙κW = ˙κW ⊥.
Proof. Recall the p-adic valuation νp(n) deﬁned in ( 1). It suﬃces to show that νp( ˙κW ) =
νp( ˙κW ⊥) for any prime p∈ P. We can reformulate as
νp( ˙κW ) = νp(lcm
{
lcm(gC ) : C∈C W
}
)
= max
{
νp(lcm(gC )) : C∈C W
}
= max
{
νp(α) : i,j∈ [n],α∈ ˙KW
ij
}
.
Lemma 3.13 implies that the last expression is the same for W and W ⊥.
11
We next show that κW and ˙κW are monotone under projections and restrictions of the
subspace.
Lemma 3.16. For any linear subspace W⊆ Rn, J⊆ [n] and i,j ∈J, we have
KπJ (W )
ij ⊆K W
ij , KWJ
ij ⊆K W
ij , ˙KπJ (W )
ij ⊆ ˙KW
ij , and ˙KWJ
ij ⊆ ˙KW
ij .
Proof. Let g∈F (WJ ). Then ( g, 0[n]\J )∈F (W ) and so KWJ
ij ⊆K W
ij . Note that πJ (W ) =
((W ⊥)J )⊥ and so by Proposition 3.13,
KπJ (W )
ij =
{
α−1 :α∈K (W ⊥)J
ji
}
⊆
{
α−1 :α∈K W ⊥
ji
}
=KW
ij. (3)
The same arguments extend to ˙Kij.
Proposition 3.17. For any linear subspace W⊆ Rn and J⊆ [n], we have
κWJ≤κW, κ πJ (W )≤κW , ˙κWJ≤ ˙κW, and ˙κπJ (W )≤ ˙κW.
