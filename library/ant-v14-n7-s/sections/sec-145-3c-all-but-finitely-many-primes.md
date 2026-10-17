---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory"
section_id: sec-145-3c-all-but-finitely-many-primes
section_title: "3C. All but finitely many primes"
section_number: null
pages: 258-258
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
toc_source: outline
---
are “admissible” over Fq for all but ﬁnitely many primes. The formal statement is here:
Lemma 3.4. Let 1 ≥1 be ﬁxed. Let F ∈Z[x1, . . . , xn] and suppose F factors as F = G1H with
G, H ∈Z[x1, . . . , xn] and H being 1-th power-free over Z. Furthermore, assume that H is nondegenerate
over Z, in the sense that there is no A ∈GLn(Z) such that H(x A) ∈Z[x2, . . . , xn]. Then for all but ﬁnitely
many primes q, the reduction of F modulo q is (1, q)-admissible.
Proof. For a ﬁxed prime q, we reduce F, G, H modulo q to f, g, h ∈Fq[x1, . . . , xn]. By Lemma 3.22
of [Xu 2018], since H is 1-th power-free over Z then for all but ﬁnitely many primes q, h is 1-th
power-free over Fq. Letting Q1 denote this ﬁnite set of exceptional primes, then for all q̸ ∈Q1, we have
that f = g1h with h being 1-th power-free over Fq. As a consequence of Lemma 3.2 (6), since H is
nondegenerate over Z, the reduction h of H modulo q can be invariant under a nontrivial translation in Fn
q
only for ﬁnitely many primes q; we will call this exceptional set Q2. Finally, let Q3 denote the primes
q ≤deg F. We now proceed to consider the primes q /∈Q1 ∪Q2 ∪Q3; for such primes, h is not invariant
under any nontrivial translation in Fn
q, and (3) in Lemma 3.3 shows that h cannot be made independent of
any indeterminate by a linear change of variables in GLn(Fq). This proves the lemma. (Here we excluded
primes in Q3 because we cite Lemma 3.3, but we note that the speciﬁc implications of this lemma that
we employ here do not need the assumption q > deg F.)
□
