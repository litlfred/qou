---
doc_id: arxiv-math-0603732v2
doc_title: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS"
section_id: sec-033-62-noetherian-pi-hopf-algebras
section_title: "Noetherian PI Hopf algebras"
section_number: 6.2
pages: 21-23
source_pdf: 0603732v2.pdf
source_sha256: 3464a2ddc2e54f3a
doc_brief: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS — W e show that many noetherian Hopf algebras A have a rigid du- alising complex R with R ∼= ν A1[d]."
---
bra, and consider conditions (1) and (2) of (6.1). By Skryabin’s res ult Proposition
1.1(b), the antipode of A is bijective, so (2) is satisﬁed. As for (1), ﬁrst note that
A is Auslander-Gorenstein, of dimension d, say, by [WZ1, Theorem 0.1]. By [Br2,
Theorem A] there is an irreducible left A-module W for which Ext d
A(W, A) ⁄= 0,
so that [BG1, Lemma 1.11] conﬁrms that Ext d
A(V, A) ⁄= 0 for every left irreducible
A-module V . Hence [SZ, Theorem 3.10(iii)(a)] ensures that A is (Krull) Cohen-
Macaulay. Since the Krull and GK-dimensions coincide for aﬃne noeth erian PI
algebras by [MR, Proposition 13.10.6 and Theorem 6.4.8], we can conclud e that
A is Auslander-Gorenstein and Cohen-Macaulay. Thus, by Lemma 6.1, A is AS-
Gorenstein.
The situation regarding (3) of (6.1) in the PI case is less straightfor ward, since it
depends on the characteristic of k. The enveloping algebra of the two-dimensional
solvable non-abelian Lie algebra in positive characteristic demonstra tes that diag-
onalisability of ξ and thus of ν will fail in general for Hopf algebras which are ﬁnite
modules over their centres. Nevertheless, in this setting ν has ﬁnite order up to an
inner automorphism, and so Maschke’s theorem comes into play in cha racteristic
0. Here is the required result:
22 K.A. BROWN AND J.J. ZHANG
Proposition. Let A be a noetherian aﬃne PI Hopf algebra of ﬁnite global dimen-
sion.
(a) The winding automorphism ξ has ﬁnite order.
(b) Some power of the antipode S of A is inner.
(c) The Nakayama automorphism ν has ﬁnite order up to inner automorphisms.
Proof. The discussion in the opening paragraph of this subsection shows th at A
is homologically homogeneous, so that A is a ﬁnite module over its centre by [SZ,
Theorem 5.6(iv)].
(a) By [L WZ, Lemma 5.3(g)], io(A) is ﬁnite. This is saying that ξ has ﬁnite
order.
(b,c) Follow from part (a) and Proposition 4.6(b,c). □
Notice that the proof of the proposition works without the global d imension
hypothesis provided A is a ﬁnite module over its centre.
Given (b) of the proposition, it makes sense to ask:
Question. If A is a noetherian aﬃne PI Hopf algebra, does the antipode of A have
ﬁnite order?
For regular PI Hopf algebras the equalities (4) of (6.1) are valid. To s ee this, we
need a lemma. Recall for its proof that the Nakayama automorphism acts trivially
on the centre, by Proposition 4.4(b).
Lemma. Let A be a noetherian aﬃne PI Hopf algebra of ﬁnite global dimensio n,
and let ν = ξS 2 be its Nakayama automorphism.
(a) ν, ν−1 ∈ N (A).
(b) If σ ∈ N (A) and the restriction of σ to the centre is the identity, then
σA/[A, σA] ⁄= 0 .
Proof. (a) By [BG1, Corollary 1.8], A is a direct sum of prime rings. The central
idempotents corresponding to the direct summands of A are ﬁxed by ν. For this
reason we may assume A is a prime ring (and forget about the coalgebra structure
for the rest of the proof).
Since A is a noetherian aﬃne prime PI algebra, the Goldie quotient ring Q(A)
is isomorphic to the central localization AC−1, where C = Z(A) \ { 0}. Clearly
Q(A) is a central simple algebra with centre Z(A)C−1 [MR, Theorem 13.6.5]. The
automorphism ν extends to Q(A) naturally, still denoted by ν. The restriction of
ν to the centre Z(Q) is the identity, and so, by the Skolem-Noether theorem, ν is
an inner automorphism. Thus there is an invertible element x ∈ Q(A) such that
ν(b) = xbx−1 for all b ∈ Q(A). Write x = ms−1 where m ∈ A is not a zero divisor
and s ∈ Z(A) \ {0}. Then, for every a ∈ A,
ν(a)m = xax−1m = xas = xsa = ma.
Hence ν ∈ N (A). The proof works for any automorphism whose restriction to the
centre is the identity, and in particular for ν−1.
(b) As in (a) we may assume A is prime. Let Q = Q(A). It suﬃces to show that
there is an elememt m ∈ A such that m ⁄∈[Q, σQ]. By the proof of (a), σ is an
inner automorphism, say σ(b) = mbm−1 for some regular element m ∈ A. For all
a, b ∈ Q,
σ(b)a − ab = mbm−1a − ab = m(bm−1a − m−1ab) = m[b, m−1a].
NOETHERIAN HOPF ALGEBRAS 23
This means that [ Q, σQ] = m[Q, Q]. Since 1 ⁄∈[Q, Q], we deduce m ⁄∈[Q, σQ]. □
Theorem. Let A be a noetherian aﬃne PI Hopf algebra of GK-dimension d.
(a) A has rigid dualising complex ν A1[d] where ν = ξS 2 is the Nakayama auto-
morphism of A.
(b) Suppose that A has ﬁnite global dimension. Then Hdim A = Hcdim A =
gldim A = d.
Proof. (a) By the opening paragraph of (6.2) A is AS-Gorenstein of dimension d,
so this is immediate from Proposition 4.5.
(b) This follows from the above lemma and Theorem 3.4(c) and 5.3(c). Note
that the latter applies because A (and hence Ae) are ﬁnite modules over their aﬃne
centres, by [SZ, Theorem 5.6(iv)]. □
