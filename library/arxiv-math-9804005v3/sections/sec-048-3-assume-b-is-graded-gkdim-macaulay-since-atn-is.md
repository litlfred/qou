---
doc_id: arxiv-math-9804005v3
doc_title: "RINGS WITH AUSLANDER DUALIZING COMPLEXES"
section_id: sec-048-3-assume-b-is-graded-gkdim-macaulay-since-atn-is
section_title: "Assume B is graded GKdim-Macaulay. Since A/(tn) is graded GKdim-Macaulay"
section_number: 3
pages: 28-29
source_pdf: 9804005v3.pdf
source_sha256: 62d069533bb97a00
doc_brief: "RINGS WITH AUSLANDER DUALIZING COMPLEXES — A ring with an Auslander dualizing complex is a generalizati on of an Auslander-Gorenstein ring."
---
for n ≥ 1 (by Proposition 4.18), it suﬃces to show that Cdim M = GKdimM for
t-torsion-free modules. We know that in this case GKdim M = GKdimM/tM + 1,
and by Lemma 5.4 this is true also for Cdim M .
Finally assume B is graded Kdim-Macaulay. Again we need only consider M
which is t-torsion-free. It is clear that Kdim M ≥ KdimM/tM + 1. Hence it
follows from Lemmas 5.4 and 5.7 that Kdim M ≥ CdimM . But by Theorem 4.14,
KdimM ≤ CdimM .
Example 5.9. Let us consider a simple case of Theorem 7.1. Let A =B[t] where
t is a central variable of degree 1. Let RB be the balanced dualizing complex of B.
Then the balanced dualizing complex of A is nothing but
RA =RB ⊗k[t] Ω 1
k[t]/k[1] ∼=RB[t](−1)[1]
where Ω 1
k[t]/k = k[t] · dt ∼= k[t](−1) as graded k[t]-modules. This follows from
[VdB] Theorem 7.1, which states that if B,C are noetherian connected graded k-
algebras with balanced dualizing complexes RB andRC respectively, and ifB ⊗C is
noetherian, then RB ⊗RC is a balanced dualizing complex over B ⊗C. By Theorem
5.1,A is graded Auslander and Kdim-(resp. GKdim-)Macaulay if and only if B is.
Corollary 5.10. Let A be a connected graded k-algebra with a balanced dualizing
complex. Suppose that every graded prime quotient A/p satisﬁes one of the following
conditions:
(i) A/p is graded Auslander (resp. and graded Kdim-(or GKdim)-Macaulay); or
(ii) A/p has a normal element of positive degree.
Then A is graded Auslander (resp. and graded Kdim-(or GKdim-)Macaulay)
Proof. Use Proposition 4.18, Theorem 5.1 and induction on Kdim A.
Recall that A has enough normal elements if every graded prime quotient A/p
(except for p = m) contains a normal element of positive degree. By Corollary 5.10,
a noetherian connected graded algebra with enough normal elemen ts is Auslander
and GKdim-Macaulay. In the rest of this section we generalize this st atement.
Corollary 5.11. LetA andB be noetherian connected graded k-algebras. Assume
A has a balanced dualizing complex and is graded Auslander (resp. and graded
Kdim(or GKdim)-Macaulay), and B has enough normal elements. Then A ⊗B is
a noetherian connected graded k-algebra with a balanced dualizing complex, and it
is graded Auslander (resp. and graded Kdim(or GKdim)-Macaulay).
Proof. We ﬁrst prove that A ⊗B is noetherian by induction on Kdim B. Suppose
{p1, · · ·, pn} is the complete set of minimal graded primes of B. Then some product∏ t
i=1 pni is zero. For any s ≥ 1 let Ws :=∏ s−1
i=1 pni/∏ s
i=1 pni, where W1 =B/pn1,
and let Bs = B/pns. Since Ws is a ﬁnitely generated Bs-module, A ⊗Ws is a
ﬁnitely generated A ⊗Bs-module. Hence it suﬃces to show that each A ⊗Bs is
RINGS WITH AUSLANDER DUALIZING COMPLEXES 29
noetherian. This reduces to the case when B is prime. Hence we may assume B has
a regular normal element t of positive degree. It is obvious that 1 ⊗t is a regular
normal element in A ⊗B. By induction hypothesis, A ⊗B/(t) is noetherian, and
therefore A ⊗B is noetherian by [ATV] Theorem 8.2.
The graded Auslander and Macaulay properties follow from the same inductive
procedure and Theorem 5.1.
In [SZ] Theorem 3.10 it was shown that a connected graded PI algebr a of ﬁnite
injective dimension (i.e. a Gorenstein algebra) is graded Auslander-G orenstein and
graded GKdim-Macaulay. This was extended in [Zh] to an algebra A having enough
normal elements. Corollary 5.11 (when A = k) generalizes these theorems by
eliminating the Gorenstein condition. We extend the result further in Theorems
5.13 and 5.14 below.
Deﬁnition 5.12. Let R be a balanced dualizing complex over A.
