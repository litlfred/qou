---
doc_id: arxiv-1801.05145v1
doc_title: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS"
section_id: sec-018-2-λmn-λnm-for-some-c-k
section_title: "(Λ(M,N )+Λ(N,M )) for some c ∈ k×. □"
section_number: 2
pages: 22-24
source_pdf: 1801.05145v1.pdf
source_sha256: 808da260edd433f7
doc_brief: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS — We prove that the quantum cluster algebra structure of a unipote nt quantum coordinate ring Aq(n(w)), associated with a symmetric Kac-Moody algebra and"
---
Deﬁnition 3.2.2. For non-zero modules M and N, we set
d(M,N ) = 1
2
(
Λ(M,N ) + Λ(N,M )
)
.
Note that if M and N are simple modules, then we have d(M,N ) ∈ Z≥0. Note also
that ifM,N 1,N 2 are simple modules, then we have d(M,N 1◦N2) = d(M,N 1)+ d(M,N 2)
by Lemma 3.1.5 (ii).
Lemma 3.2.3 ([15]). LetM,N be simple modules and assume that one of them is real.
Then the following conditions are equivalent.
(i) d(M,N ) = 0 .
(ii) rM,N and rN,M are inverse to each other up to a constant multiple.
(iii) M ◦N and N ◦M are isomorphic up to a grading shift.
(iv) M ∇N and N ∇M are isomorphic up to a grading shift.
(v) M ◦N is simple.
Proof. By specializing the equations in Lemma 3.2.1 (ii) at z = 0, we obtain that
d(M,N ) = 0 if and only if rM,N ◦ rN,M = id N◦M and rN,M ◦ rM,N = id M◦N up to
non-zero constant multiples. Hence the conditions (i) and (ii) are eq uivalent.
The conditions (ii), (iii), (iv), and (v) are equivalent by [ 15, Theorem 3.2, Proposition
3.8, and Corollary 3.9]. □
MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS 23
Deﬁnition 3.2.4. LetM,N be simple modules.
(i) We say that M and N commute if d(M,N ) = 0 .
(ii) We say that M and N are simply-linked if d(M,N ) = 1 .
Proposition 3.2.5. Let M1,...,M r be a commuting family of real simple modules.
Then the convolution product
M1 ◦ · · · ◦Mr
is a real simple module.
Proof. We shall ﬁrst show the simplicity of the convolutions. By induction on r, we
may assume that M2 ◦ · · · ◦Mr is a simple module. Then we have
d(M1,M 2 ◦ · · · ◦Mr) =
r∑
s=2
d(M1,Ms) = 0
so that M1 ◦ · · · ◦Mr is simple by Lemma 3.2.3.
Since (M1 ◦ · · · ◦Mr) ◦ (M1 ◦ · · · ◦Mr) is also simple, M1 ◦ · · · ◦Mr is real. □
Deﬁnition 3.2.6. LetM1,...,M m be real simple modules. Assume that they commute
with each other. We set
M1
⨀ M2 :=q
~Λ(M1,M2)M1 ◦M2,⨀
1≤k≤m
Mk := (· · ·(M1
⨀ M2) · · ·) ⨀ Mm−1) ⨀ Mm
≃q
∑
1≤i<j≤m ~Λ(Mi,Mj)M1 ◦ · · · ◦Mm.
It is invariant under the permutations of M1,...,M m.
Lemma 3.2.7. Let M1,...,M m be real simple modules commuting with each other.
Then for any σ ∈ Sm, we have
⊙
1≤k≤m
Mk ≃ ⊙
1≤k≤m
Mσ(k) in R-gmod.
Moreover, if the Mk’s are self-dual, then so is ⊙1≤k≤mMk.
Proof. It follows from Lemma 3.1.4 and q ~Λ(Mi,Mj)Mi ◦Mj ≃q ~Λ(Mj,Mi)Mj ◦Mi. □
Proposition 3.2.8. Let f : N1 → N2 be a morphism between non-zero R-modules
N1,N 2 and let M be a non-zero R-module.
(i) If Λ(M,N 1) = Λ( M,N 2), then the following diagram is commutative:
M ◦N1
rM,N1 /d47/d47
M ◦f
/d15/d15
N1 ◦M
f ◦M
/d15/d15
M ◦N2
rM,N2 /d47/d47N2 ◦M.
