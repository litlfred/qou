---
doc_id: arxiv-math-9804005v3
doc_title: "RINGS WITH AUSLANDER DUALIZING COMPLEXES"
section_id: sec-052-30-amnon-yekutieli-and-james-j-zhang
section_title: "AMNON YEKUTIELI AND JAMES J. ZHANG"
section_number: 30
pages: 30-30
source_pdf: 9804005v3.pdf
source_sha256: 62d069533bb97a00
doc_brief: "RINGS WITH AUSLANDER DUALIZING COMPLEXES — A ring with an Auslander dualizing complex is a generalizati on of an Auslander-Gorenstein ring."
---
Proof. First we observe that [Zh] Lemma 2.2 holds (same proof), and hence KdimM
≥ GKdimM and GKdimM <∞ for every ﬁnitely generated graded A-module M .
Therefore, replacing Ext i(−,A ) with Ext i
A(−,R ), the proof of [Zh] Theorem 3.1
can be copied verbatim. Let us just mention the key point of the pro of. We prove
by induction on GKdim M that for every ﬁnitely generated graded A-module (resp.
A◦-module) M :
(a) jR(M ) = − GKdimM .
(b) GKdim Ext j
A(M,R ) = GKdim M , where j =jR(M ).
(c) For every jR(M ) ≤i ≤ 0 one has GKdim Ext i
A(M,R ) ≤ −i.
This implies that A is graded Auslander and graded GKdim-Macaulay. By [Zh]
Lemma 2.2, Kdim M ≥ GKdimM = Cdim M , and by Theorem 4.14, Kdim M ≤
CdimM . Hence A is graded Kdim-Macaulay.
Theorem 0.6 is an immediate consequence of Theorems 5.13 and 5.14. A nother
consequence is Proposition 0.9 which we now prove.
Proof of Proposition 0.9. If A is connected graded, i.e., A0 = k, the assertion
follows from Theorems 5.13 and 5.14. Now assume A is not connected. Let
B :=k +A≥1, which is connected. Since A andB diﬀer by a ﬁnite rank k-module,
B is noetherian. It remains to verify the following statements.
(a) If M is a ﬁnitely generated graded A-module, then Kdim AM = KdimBM
and GKdimAM = GKdimBM .
(b) If A has enough normal elements, then so does B.
(c) If A is graded FBN, then so is B.
(a) The statement about GKdim is obvious because GKdim is determine d by the
degree of the Hilbert function of M (see [Zh] Lemma 2.2(1)). Next we consider
Kdim. Clearly Kdim AM = 0 if and only if M is a ﬁnitely generated k-module, if
and only if Kdim BM = 0. For higher dimension we consider the quotient category
QGrA := GrModA/ M0, where M0 = M0(Kdim) is the localizing subcategory con-
sisting of Kdim = 0 modules (torsion modules in the terminology of [AZ]). F or any
M ∈ GrModfA one has
KdimAM = Kdim GrModAM = Kdim QGrAM + 1.
Now since A and B diﬀer by a ﬁnite rank k-module, QGrA is equivalent to QGrB
by [AZ] Proposition 2.5, so Kdim QGrAM = Kdim QGrBM .
(b) Let p be a graded prime ideal of B which is not mB =B≥1. Then ApA and p dif-
fer by a ﬁnitely generated k-module, and hence GKdim A/ApA = GKdimB/p. Let
q be a graded prime of A minimal over ApA such that GKdim A/q = GKdimB/p.
Then the map B/p → A/q is injective, and bijective in positive degrees. Thus
normal elements of positive degree in A/q are also normal elements in B/p.
(c) The proof is similar to (b) and we leave it to the reader.
