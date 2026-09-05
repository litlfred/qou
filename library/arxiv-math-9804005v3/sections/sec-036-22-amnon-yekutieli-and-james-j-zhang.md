---
doc_id: arxiv-math-9804005v3
doc_title: "RINGS WITH AUSLANDER DUALIZING COMPLEXES"
section_id: sec-036-22-amnon-yekutieli-and-james-j-zhang
section_title: "AMNON YEKUTIELI AND JAMES J. ZHANG"
section_number: 22
pages: 22-23
source_pdf: 9804005v3.pdf
source_sha256: 62d069533bb97a00
doc_brief: "RINGS WITH AUSLANDER DUALIZING COMPLEXES — A ring with an Auslander dualizing complex is a generalizati on of an Auslander-Gorenstein ring."
---
Theorem 4.7 (Local Duality) . LetR be a balanced dualizing complex over a noe-
therian connected graded k-algebra A. Then for any graded k-algebra B and any
M ∈ D(GrMod(A ⊗B◦)) there is a functorial isomorphism
R Homgr
A (M,R ) ∼= (RΓ mM )∗.
This is proved by combining [VdB] Theorems 5.1 and 6.3. The theorem wa s ﬁrst
proved in [Ye1], but only for M ∈ Db
f (GrModA).
Proposition 4.8 ([VdB] Proposition 8.2(2)) . A balanced dualizing complex R is
rigid in the graded sense.
Remark 4.9. According to an exercise in [VdB] (whose only proof we know is
quite involved), if I is a graded-injective A-module, then I has injective dimension
≤ 1 in ModA. An immediate consequence of this fact is that a graded dualizing
complex R over A is also an ungraded dualizing complex. The special case we
need, namely that a balanced dualizing complex R is rigid in the ungraded sense,
is proved by other means in Corollary 6.7.
Here is another result from [VdB]. Let us write mAe for the augmentation ideal
of Ae, so mAe = m ⊗A◦ +A ⊗ m◦.
Theorem 4.10 ([VdB] Corollary 4.8) . AssumeA has a balanced dualizing complex
R. Let M ∈ D(GrModAe) have ﬁnitely generated cohomology modules on both sides.
Then there is a functorial isomorphism
RΓ mM ∼= RΓ mAeM ∼= RΓ m◦M.
We obtain the following interesting result:
Corollary 4.11. Let R be a balanced dualizing complex over A. Then there is a
functorial isomorphism
R HomA(M,R ) ∼= R HomA◦ (M,R )
for M ∈ D(GrModAe) with ﬁnitely generated cohomology modules on both sides.
We shall write Cdim A instead of Cdim R;A when R is the balanced dualizing
complex, and when we are working in GrModA. Since a balanced dualizing complex
is rigid in the ungraded sense (by Corollary 6.7), this is consistent with Deﬁnition
3.10.
Deﬁnition 4.12. If A has a graded Auslander balanced dualizing complex R we
say A is graded Auslander . Furthermore if dim is an exact dimension function
on graded modules, and if R is graded dim-Macaulay, then we say A is graded
Auslander dim-Macaulay.
According to [Ye1] Theorem 3.9, any two graded dualizing complexes R1,R 2
satisfy R2 ∼= R1 ⊗A Aσ(m)[n], for an automorphism σ and an integers n,m . It
follows that R1 is graded Auslander iﬀ R2 is so. In particular, if A is graded
Gorenstein, then A is graded Auslander-Gorenstein in the usual sense iﬀ it is graded
Auslander in the sense of Deﬁnition 4.12.
Taking cohomologies in the previous corollary we get:
Corollary 4.13. Suppose A is graded Auslander. Then Cdim is symmetric on
graded modules. That is to say, if M is a graded A-bimodule, ﬁnitely generated on
both sides, then CdimAM = CdimA◦M.
RINGS WITH AUSLANDER DUALIZING COMPLEXES 23
IfA is graded Auslander we have a bound on Krull dimension of graded mod ules:
Theorem 4.14. SupposeA is graded Auslander. Then
KdimM ≤ CdimM = sup{q | HqRΓ mM ⁄= 0}< ∞
for all ﬁnitely generated graded A-modulesM .
Proof. By Theorem 4.7, if M ⁄= 0, we have Cdim M = sup {q | HqRΓ mM ⁄= 0 }.
Next for a ﬁnitely generated graded A-module M the Krull dimension is the same
when computed in GrModA and in ModA. And by the graded variant of Corollary
2.18 we get Kdim M ≤ CdimRM , since clearly d0 = 0.
Lemma 4.15. Let A → B be a ﬁnite homomorphism of noetherian connected
gradedk-algebras, with augmentation ideals mA, mB. Assume A satisﬁes condition
