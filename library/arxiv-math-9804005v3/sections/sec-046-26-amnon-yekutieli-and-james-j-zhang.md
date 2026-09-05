---
doc_id: arxiv-math-9804005v3
doc_title: "RINGS WITH AUSLANDER DUALIZING COMPLEXES"
section_id: sec-046-26-amnon-yekutieli-and-james-j-zhang
section_title: "AMNON YEKUTIELI AND JAMES J. ZHANG"
section_number: 26
pages: 26-28
source_pdf: 9804005v3.pdf
source_sha256: 62d069533bb97a00
doc_brief: "RINGS WITH AUSLANDER DUALIZING COMPLEXES — A ring with an Auslander dualizing complex is a generalizati on of an Auslander-Gorenstein ring."
---
We denote by D the duality functor R Hom A(−,R ), where R is the balanced dual-
izing complex of A. Recall that according to Theorem 4.7, H −iDM ∼= (RiΓ mM )∗.
By deﬁnition Cdim M = sup{i | H−iDM ⁄= 0}, so trivially
CdimM ≤ max{CdimM ′, CdimM/M ′}(5.3)
for all M ′ ⊂M .
Lemma 5.4. If M is t-torsion-free then CdimM = Cdim M/tM + 1 . If d =
CdimM then H−dDM is t-torsion-free.
Proof. Let σ be the automorphism of A such that t ·a = σ(a) ·t, and let σM be
the corresponding twisted module. Then we have an exact sequenc e
0 → σ−1
M (−l)
t·
− →M →M/tM → 0
where l is the degree of t. It is easy to see that H iD(σ−1
M (−l)) ∼= (HiDM )σ−1
(l),
so there is a long exact sequence
HiD(M/tM ) → HiDM
·t
− →(HiDM )σ−1
(l) → Hi+1D(M/tM ).(5.5)
If Hi+1D(M/tM ) = 0 then by the graded Nakayama Lemma we get H iDM = 0.
Therefore
CdimM/tM ≤ CdimM ≤ CdimM/tM + 1.
Now let d = CdimM . We need to show that H −dD(M/tM ) = 0. If not, then
CdimM/tM = d, and hence also Cdim M/tnM = Cdim tn−1M/tnM = d for all
n ≥ 1. According to Proposition 4.18 the algebra A/(t)n has the graded Auslander
property. This implies that
Cdim H−dD(tn−1M/tnM ) = d and Cdim H −d+1D(M/tn−1M ) ≤d − 1.
Looking at the exact sequence
0 → H−dD(M/tn−1M ) → H−dD(M/tnM )
→ H−dD(tn−1M/tnM )
φ
− →H−d+1D(M/tn−1M )
we see that φ cannot be an injection. Therefore
H−dD(M/tn−1M ) ⫋ H−dD(M/tnM ) ⊂ H−dD(M ).
But this is true for all n ≥ 1, contradicting with the noetherian property of
H−dD(M ). The upshot is that H dD(M/tM ) = 0. Taking i = −d in (5.5) we
conclude that H dDM is t-torsion-free.
Lemma 5.6. LetN be the t-torsion submodule of M . Then
CdimM = max{CdimN, CdimM/N }.
Proof. Let d be the right hand side. Trivially Cdim M ≤ d holds. Assume
CdimM < d. Dualizing the exact sequence 0 → N → M → M/N → 0 we
obtain a long exact sequence
· · · → HiD(M/N ) → HiDM → HiDN → Hi+1D(M/N ) → Hi+1DM → · · ·
and taking i = −d − 1 we see that H −dD(M/N ) = 0, so Cdim M/N < d. Hence
CdimN = d. Also taking i = −d we see that H −dDN ⊂ H−d+1D(M/N ). Now
H−dDN is t-torsion, yet by Lemma 5.4, H −d+1D(M/N ) is t-torsion-free. We con-
clude that H −dDN = 0, which is a contradiction.
RINGS WITH AUSLANDER DUALIZING COMPLEXES 27
Lemma 5.7.
CdimM = max{CdimL, CdimM/L}
for every L ⊂M .
Proof. By (5.3) it remains to prove “ ≥”. Let N be the t-torsion submodule of
M . By (5.2) we have Cdim N ≥ CdimN ∩L. On the other hand by Lemma
5.6, CdimM = max {CdimN, CdimM/N } and CdimL = max {CdimN ∩L, Cdim
L/N ∩L}. Hence it suﬃces to prove that Cdim M/N = max{CdimL/N ∩L, Cdim
M/L}. So we may assume M =M/N is t-torsion-free.
If P :=M/L is also t-torsion-free then we get a short exact sequence
0 →L/tL →M/tM →P/tP → 0.
Hence the assertion follows from Lemma 5.4.
In general let L′ ⊃L be such that L′/L is the t-torsion submodule of M/L. So
tnL′ ⊂L for some n. By Lemma 5.4,
CdimL′/L ≤ CdimL′/tnL′ = CdimL′ − 1
and hence, from the long exact sequence of duality, we get Cdim L = Cdim L′.
Applying the previous paragraph and Lemma 5.6 we have
CdimM = max{CdimL′, CdimM/L′}
= max{CdimL, CdimM/L′}
= max{CdimL, CdimL′/L, CdimM/L′}
= max{CdimL, CdimM/L}
and we ﬁnish the proof.
Lemma 5.8. Supposetn kills the t-torsion submodule of M . Then
CdimM ≤ CdimM/tnM + 1.
Proof. Let N be the t-torsion submodule of M and P :=M/N . Then tnM ∼=tnP
is an t-torsion-free submodule of M and P/tnP ∼=M/(N ⊕tnM ). By Lemmas 5.4
and 5.6,
CdimM = max{CdimN, CdimP } = max{CdimN, CdimP/tnP + 1}.
On the other hand by Lemma 5.7,
CdimM/tnM = max{CdimN, CdimP/tnP }.
It remains to combine these equalities.
Proof of Theorem 5.1. As mentioned above part 1 is a consequence of Theorems
4.5 and 4.6, and [AZ] Theorem 8.8.
2. Recall that the Auslander condition says that if N ⊂ H−iDM then CdimN ≤i.
We can assume A is prime and t is regular. By Lemma 5.7 it suﬃces to prove that
Cdim H−iDM ≤ i for all i. According to (5.2) the inequality holds for t-torsion
modules, so using the long exact sequence of duality we may assume t hat M is
t-torsion-free.
Choosen such that tn kills the t-torsion submodule of H −iDM . The short exact
sequence
0 →M
tn·
− − →σn
M (nl) → σn
(M/tnM )(nl) → 0
