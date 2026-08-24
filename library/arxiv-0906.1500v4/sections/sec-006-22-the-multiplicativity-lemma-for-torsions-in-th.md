---
doc_id: arxiv-0906.1500v4
doc_title: "Twisted Alexander invariant and non-abelian Reidemeister torsion for hyperbolic three-manifolds"
section_id: sec-006-22-the-multiplicativity-lemma-for-torsions-in-th
section_title: "The Multiplicativity Lemma for torsions. In this section, we brieﬂy review"
section_number: 2.2
pages: 5-5
source_pdf: 0906.1500v4.pdf
source_sha256: 9a586f6d134ca47f
doc_brief: "Twisted Alexander invariant and non-abelian Reidemeister torsion for hyperbolic three-manifolds — W e study a computational method of the hyperbolic Reidemeister torsion (also called in the"
---
the Multiplicativity Lemma for Reidemeister torsions (with sign).
First, we review the notion of compatible bases. Let 0 → E′ i
− →E
j
− →E′′ → 0 be a
short exact sequence of ﬁnite dimensional vector spaces and let s denotes a section of j.
Thus, i ⊕ s : E′ ⊕ E′′ → E is an isomorphism. We equip the three vector spaces E′, E
and E′′ respectively with the following three bases : b′ =
(
b′
1, . . . , b′
p
)
, b = ( b1, . . . , bn),
and b′′ =
(
b′′
1 , . . . , b′′
q
)
. With such notation, one has n = p + q, and we say that the bases
b′, b and b′′ are compatible if the isomorphism i ⊕ s : E′ ⊕ E′′ → E has determinant 1
in the bases b′ ∪ b′′ =
(
b′
1, . . . , b′
p, b′′
1 , . . . , b′′
q
)
of E′ ⊕ E′′ and b of E. If it is the case, we
write b ∼ b′ ∪ b′′.
Let us now review the multiplicativity property of the Reidemeister to rsion (with
sign).
Multiplicativity Lemma (Lemma 3.4.2 in [Tur86]) . Let
(3) 0 → C′
∗ → C∗ → C′′
∗ → 0
be an exact sequence of chain complexes. Assume that C′
∗, C∗ and C′′
∗ are based and
homology based. For all i, let c′i, ci and c′′i denote the reference bases of C′
i, Ci and C′′
i
respectively. Associated to (3) is the long sequence in homo logy
· · · → Hi(C′
∗) → Hi(C∗) → Hi(C′′
∗ ) → Hi−1(C′
∗) → · · ·
Let H∗ denote this acyclic chain complex and base H3i+2 = Hi(C′
∗), H3i+1 = Hi(C∗)
and H3i = Hi(C′′
∗ ) with the reference bases of Hi(C′
∗), Hi(C∗) and Hi(C′′
∗ ) respectively.
If for all i, the bases c′i, ci and c′′i are compatible, i.e. ci ∼ c′i ∪ c′′i, then
Tor(C∗, c∗, h∗)
= (−1)α(C ′
∗,C ′′
∗ )+ε(C ′
∗,C∗,C ′′
∗ ) Tor(C′
∗, c′∗, h′∗)Tor(C′′
∗ , c′′∗, h′′∗)Tor(H∗, {h′∗, h∗, h′′∗}, ∅)
where
α(C′
∗, C′′
∗ ) =
∑
i/greaterorequalslant0
αi−1(C′
∗)αi(C′′
∗ ) ∈ Z/2Z and
ε(C′
∗, C∗, C′′
∗ ) =
∑
i/greaterorequalslant0
{(βi(C∗) + 1)(βi(C′
∗) + βi(C′′
∗ )) + βi−1(C′
∗)βi(C′′
∗ )} ∈ Z/2Z.
The proof is a careful computation based on linear algebra, see [Tur 86, Lemma 3.4.2]
and [Mil66, Theorem 3.2]. This lemma appears to be a very powerful too l for computing
Reidemeister torsions. It will be used all over this paper.
