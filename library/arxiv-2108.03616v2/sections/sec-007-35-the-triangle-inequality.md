---
doc_id: arxiv-2108.03616v2
doc_title: "Circuit imbalance measures and linear programming ∗"
section_id: sec-007-35-the-triangle-inequality
section_title: "The triangle inequality"
section_number: 3.5
pages: 13-15
source_pdf: 2108.03616v2.pdf
source_sha256: 63696ad045602440
doc_brief: "Circuit imbalance measures and linear programming ∗ — We study properties and applications of various circuit imbalance mea sures associated with linear spaces."
---
An interesting additional fact about circuit imbalances is that the logarithm of the weights
satisfy the triangle inequality; this was shown in [ DHNV20]. Here, we formulate a stronger
version and give a simpler proof. Throughout, we assume that M(W ) is non-separable. Thus,
according to Proposition 2.2, for any i,j ∈ [n] there is a circuit C∈C W with i,j ∈C.
Theorem 3.21. LetW⊆ Rn be a linear space, and assume M(W ) is non-separable. Then,
13
(i) for any distinct i,j,k ∈ [n],KW
ij ⊆K W
ik·KW
kj ; and
(ii) for any distinct i,j,k ∈ [n], κij≤κik·κkj .
The proof relies on the following technical lemma that analy zes the scenario when almost all
vectors in W are elementary.
Lemma 3.22. LetW⊆ Rn be a subspace s.t. M(W ) is non-separable.
(i) If F(W ) ={g∈W\{ 0} : supp(g)⁄= [n]}, then KW
ij ⊆K W
ik·KW
kj .
(ii) If there exists g∈F (W ) such that |supp(g)| =n− 1, then
F(W ) ={g∈W\{ 0} : supp(g)⁄= [n]} .
Proof. For part (i), let δ∈K W
ij and let g∈F (W ) such that {i,j}⊂ supp(g) and|gj/gi| =δ. If
k∈ supp(g), then|gj/gi| =|gk/gi|·| gj/gk| shows the claim.
Assume k /∈ supp(g), and pick h∈F (W ) such that {i,k}⊂ supp(h) and let ˜h =hjg−gjh;
such a h exists by Proposition 2.2. Then ˜hj = 0 and ˜hk⁄= 0, so ˜h∈F (W ) by the assumption.
If ˜hi = 0 then hjgi =gjhi and so{i,j,k}⊂ supp(h) with hj/hi =gj/gi, therefore h certiﬁes the
statement as|hj/hi| =|hk/hi|·|hj/hk|. Otherwise, ˜hi⁄= 0 and h′ := ˜hig−gi˜h fulﬁlls h′∈F (W )
as h′
i = 0,{j,k}⊂ supp(h′). Now, using that ˜hj = 0 and gk = 0 it is easy to see that
⏐⏐⏐⏐⏐
˜hk
˜hi
·
h′
j
h′
k
⏐⏐⏐⏐⏐ =
⏐⏐⏐⏐⏐
˜hk
˜hi
·
˜higj−gi˜hj
˜higk−gi˜hk
⏐⏐⏐⏐⏐ =
⏐⏐⏐⏐⏐
˜hk
˜hi
·
˜higj
gi˜hk
⏐⏐⏐⏐⏐ =
⏐⏐⏐⏐
gj
gi
⏐⏐⏐⏐. (4)
We now turn to part (ii). Since there exists g ∈F (W ) with supp( g)⁄= n, we cannot have
[n]∈C (W ).
Let g∈F (W ) and i∈ [n] such that supp( g) = [n]\{i}. Consider any h∈ W , supp(h)⁄=
supp(g) such that supp( h)⁄= [n]. If h /∈F (W ) there exists ℓ∈F (W ) such that supp( ℓ) ⊊
supp(h). We must have i∈ supp(ℓ), since supp( ℓ)\ supp(g)⁄=∅. Then ˜h := hiℓ−ℓih fulﬁlls
˜h⁄= 0, ˜hi = 0 and supp( ˜h) ⊊ [n]\{i}, a contradiction to g∈F (W ).
Proof of Theorem 3.21. Part (ii) immediately follows from part (i), when taking C∈C W such
that|gC
j /gC
i| =κij. We now prove part (i).
Letδ∈K W
ij andC∈C W such that i,j ∈C and for g =gC ,|gj/gi| =δ. If k∈C then clearly
|gj/gi| =|gk/gi|·| gj/gk|∈K W
ik·KW
kj . Otherwise, let us select C ′∈C W such that i,k∈C ′, and
|C∪C ′| is minimal. Let h =gC′
and J =C ′\ (C∪{k}).
Claim 3.22.1. Let G = (C∪C ′)\J. Then for the space ˆW := πG(WC∪C′) we have that
gG,hG∈F ( ˆW ).
Proof. The statement that hG∈F ( ˆW ) is clear as hC∪C′ ∈F (WC∪C′) and the variables we
project out J fulﬁll J⊆ supp(h). For the statement on gG assume that there exists ˆg∈F ( ˆW )
such that supp(ˆg) ⊊ supp(gG). Then there exists a lift ˜ g∈F (WC∪C′) of ˆg and some ℓ∈J such
thatℓ∈ supp(˜g); note also that ˜gk =gk = 0. The vector ˆh :=hℓ˜g− ˜gℓh fulﬁlls ℓ /∈ supp(ˆh) and
k∈ supp(ˆh).
Now pick any circuit ˜h∈F ( ˆW ) such that k∈ supp(˜h) and supp( ˜h)⊆ supp(ˆh). Note that
J∪{k} is independent, as J∪{k}⊆ C ′\{i} ⊊ C ′. Therefore, supp( ˜h)∩ supp(g)⁄=∅. Hence,
forT :=C∪ supp(˜h) we have that M(WT ) is non-separable. In particular there exists a circuit
h′∈F (WT ) such that i,k ∈ supp(h′). As T ⊆ (C∪C ′)\{ℓ}, this is a contradiction to the
minimal choice of C ′.
As supp(hD)∪ supp(gD) = D and supp(hD)∩ supp(gD)⁄=∅ we have that F(W ′) is non-
separable. Further |supp(gD)| =|D|− 1, so we can apply Lemma 3.22 to learn δ∈K W ′
ij ⊆
KW ′
ik ·KW ′
kj . We can conclude δ∈K W
ik·KW
kj from Lemma 3.16.
14
If κW = 1, then the reverse inclusion KW
ik ·K W
kj ⊆K W
ij trivially holds, since 1 is the only
element in these sets. In Proposition 5.4, we give a necessary and suﬃcient condition for KW
ij =
KW
ik·KW
kj .
One may ask under which circumstances an element α∈K W
ik·KW
kj is also contained in KW
ij .
We give a partial answer by stating a suﬃcient condition in a r estrictive setting. For a basis B
ofM(W ), recallFB(W ⊥) from Lemma 3.12. Then, Lemmas 3.12 and 3.13 together imply:
Lemma 3.23. Given a basis B ⊆ [n] inM(W ) and g,h ∈ FB ⊆ F(W ⊥) such that i ∈
supp(g)∩B, j∈ supp(h)∩B and k∈ supp(g)∩ supp(h). Then |hj/hk|·| gk/gi|∈K W
ij .
