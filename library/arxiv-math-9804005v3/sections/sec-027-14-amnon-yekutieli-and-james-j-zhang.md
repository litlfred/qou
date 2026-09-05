---
doc_id: arxiv-math-9804005v3
doc_title: "RINGS WITH AUSLANDER DUALIZING COMPLEXES"
section_id: sec-027-14-amnon-yekutieli-and-james-j-zhang
section_title: "AMNON YEKUTIELI AND JAMES J. ZHANG"
section_number: 14
pages: 14-15
source_pdf: 9804005v3.pdf
source_sha256: 62d069533bb97a00
doc_brief: "RINGS WITH AUSLANDER DUALIZING COMPLEXES — A ring with an Auslander dualizing complex is a generalizati on of an Auslander-Gorenstein ring."
---
Proof. By [ASZ] Lemma 1.1 the categories Mq,f/Mq−1,f and M◦
q,f/M◦
q−1,f are noe-
therian, hence by Theorem 2.15 they are also artinian.
At last here is:
Proof of Theorem 2.10. We already veriﬁed axioms (i) and (ii). The fact that
CdimR is ﬁnitely partitive is immediate from Corollary 2.16, and this in turn easily
implies axiom (iii) – cf. [MR] Corollary 8.3.6.
Corollary 2.17. Every ﬁnitely generated A-module has a CdimR-critical compo-
sition series.
Proof. By Theorem 2.10 and [MR] Proposition 6.2.20.
Let
d0 := inf {CdimRM |M ∈ ModA,M ⁄= 0}
d1 := CdimRA = sup{CdimRM |M ∈ ModA}.
Corollary 2.18. SupposeR ∈ D(Mod(A⊗B◦)) is an Auslander dualizing complex.
Then
KdimM ≤ CdimRM −d0
for all ﬁnitely generated A-modules M . In particular if CdimRM =d0 then M is
artinian.
Proof. By induction, starting with q =d0, Theorem 2.14 and Corollary 2.16 show
that KdimM ≤q −d0 for all M ∈ Mq,f .
Here is a generalization of [Bj] Theorem 1.14.
Theorem 2.19. (Gabber’s Maximality Principle) LetA andB bek-algebras, with
A left noetherian and B right noetherian, and let R ∈ D(Mod(A ⊗B◦)) be an Aus-
lander dualizing complex. Suppose N is a CdimR-pureA-module with CdimRN =
n, and M is a ﬁnitely generated submodule. Then there is a unique maxi mal module
˜M such that M ⊂ ˜M ⊂N , ˜M is ﬁnitely generated, and CdimR ˜M/M ≤n − 2.
Proof. Note that we do not assume N is ﬁnitely generated. The uniqueness is
clear because Cdim R is an exact dimension function. So it remains to show ex-
istence. If ˜M is any ﬁnitely generated submodule of N containing M , such that
CdimR ˜M/M ≤ n − 2, then Ext −n
A (M,R ) ∼= Ext−n
A ( ˜M,R ). Hence, by Theorem
2.14(3), the module ˜M embeds functorially into the ﬁnitely generated A-module
Ext−n
B◦ (Ext−n
A (M,R ),R ). This implies there is a maximal such ˜M .
The next two theorems generalize [GL] Theorems 1.4 and 1.6 by eliminat ing the
Gorenstein and Cohen-Macaulay conditions. From here on we consid er a single
noetherian algebra A (i.e. A =B).
Deﬁnition 2.20. Let dim be an exact dimension function.
1. dim is called symmetric if dimAM = dimA◦M for every bimodule M ﬁnitely
generated on both sides.
2. dim is called weakly symmetric if dimAM = dimA◦M for every bimodule M
which is a subquotient of A.
Lemma 2.21. Let dim be a weakly symmetric exact dimension function.
RINGS WITH AUSLANDER DUALIZING COMPLEXES 15
