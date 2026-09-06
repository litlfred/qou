---
doc_id: arxiv-math-9804005v3
doc_title: "RINGS WITH AUSLANDER DUALIZING COMPLEXES"
section_id: sec-013-3-a-is-catenary-and-if-a-0-its-krull-dimension-i
section_title: "A is catenary, and (if A ⁄= 0) its Krull dimension is"
section_number: 3
pages: 8-9
source_pdf: 9804005v3.pdf
source_sha256: 62d069533bb97a00
doc_brief: "RINGS WITH AUSLANDER DUALIZING COMPLEXES — A ring with an Auslander dualizing complex is a generalizati on of an Auslander-Gorenstein ring."
---
KdimA ≤ max{d(p)} − min{d(p)}< ∞.
4. B is an Azumaya A-algebra.
The proof of the theorem is after the next lemma.
Lemma 1.14. Assume in addition that A is local. Then there is an integer d such
that Extq
A(M,R ) = 0 and Extq
B◦ (N,R ) = 0 for all q ⁄=d, all ﬁnite length A-modules
M and all ﬁnite length B◦-modulesN .
Proof. According to [Ye3] Proposition 5.4 (which works even when A ⁄=B; cf. ibid.
Proposition 2.5), left and right multiplications on R induce ring isomorphisms A ∼=
EndD(Mod(A⊗B◦))(R) ∼= Z(B). Moreover since A is noetherian and B◦ ∼= Ext0
A(R,R )
we see that B is a ﬁnite A-algebra. If N is an A-central (A ⊗B◦)-module, then
Extq
B◦ (N,R ) is a central A-bimodule.
Denote by K the residue ﬁeld of A. Let p0 := min {p | Extp
A(K,R ) ⁄= 0 } and
p1 := max {p | Extp
A(K,R ) ⁄= 0 }. By induction on length we see that for every
ﬁnite length A-module M , p0 = min {p | Extp
A(M,R ) ⁄= 0 } and p1 = max {p |
Extp
A(M,R ) ⁄= 0}.
Now take a nonzero ﬁnite length B◦-module N . Since we can view N as a
central A-bimodule, it follows that Ext q
B◦ (N,R ) is also a central A-bimodule for
every q; and so it has ﬁnite length. Deﬁne q0 := min {q | Extq
B◦(N,R ) ⁄= 0 }
and q1 := max {q | Extq
B◦ (N,R ) ⁄= 0 }. In the E2-page of the spectral sequence
of Proposition 1.7 we have nonzero terms Ep1,−q0
2 = Ext p1
A (Extq0
B◦ (N,R )) and
Ep0,−q1
2 = Extp0
A (Extq1
B◦ (N,R )), that appear in the right-top and left-bottom cor-
ners respectively. The convergence of the spectral sequence f orces p1 = q0 and
p0 =q1. Therefore we get d :=p1 =q0 =q1 =p0.
Proof of Theorem 1.13. 1. As observed in the proof of the lemma, B is a ﬁnite A-
algebra. Take a prime p ⊂A, and deﬁne Bp :=B⊗AAp andRp :=Ap⊗AR⊗BBp ∈
Db(Mod(Ap ⊗B◦
p)). We claim that Rp is a dualizing complex.
First note that the cohomologies H qR are central A-bimodules. Since A →
Ap is ﬂat and Ap ⊗AAp = Ap, there are isomorphisms H qRp ∼= Ap ⊗A HqR ∼=
HqR ⊗BBp. Therefore Rp ∼=Ap ⊗AR ∼=R ⊗BBp in Db(Mod(A ⊗B◦)). It is easy
to see that the cohomology bimodules H qR are ﬁnitely generated on both sides,
R HomAp(Rp,R p) ∼=B◦
p and R HomB◦p (Rp,R p) ∼=Ap.
In order to verify that Rp has ﬁnite injective dimension over B◦
p it suﬃces to
show that Extq
B◦p
(N,R p) vanishes for all ﬁnitely generated B◦
p-modulesN , for large
q. Now we can write N ∼=N ′ ⊗BBp for some ﬁnitely generated B◦-moduleN ′, and
