---
doc_id: arxiv-math-0501112v3
doc_title: "GAUSSIAN FLUCTUATIONS OF CHARACTERS OF"
section_id: sec-024-31-factorization-of-characters-and-gaussian-ﬂuct
section_title: "Factorization of characters and Gaussian ﬂuctuations. The follow-"
section_number: 3.1
pages: 10-12
source_pdf: 0501112v3.pdf
source_sha256: f95088789da2453a
doc_brief: "GAUSSIAN FLUCTUATIONS OF CHARACTERS OF — We study asymptotics of reducible representations of the symmetric groups Sq for large q."
---
ing theorem is the main result of this article. In order not toscare the Reader
we postpone its proof to Section 4.
Theorem and Deﬁnition 3.1. For each q ≥ 1 let ρq be a representation of
Sq . We say that the sequence (ρq ) has the character factorization property
if it fulﬁlls one (hence all) of the following equivalent conditions:
• for any cycles σ 1, . . . , σ n with disjoint supports
(3.1) k(σ 1, . . . , σ n)q
|σ 1 |+···+|σ n |+2(n− 1)
2 = O(1);
• for any integers l1, . . . , l n ≥ 1
(3.2) k•(Σ l1 , . . . , Σ ln )q− l1 +···+ln − n+2
2 = O(1);
• for any integers l1, . . . , l n ≥ 1
(3.3) k(Σ l1 , . . . , Σ ln )q− l1 +···+ln − n+2
2 = O(1);
• for any integers l1, . . . , l n ≥ 2
(3.4) k(Rl1 , . . . , R ln )q− l1 +···+ln − 2(n− 1)
2 = O(1).
Remark. In Corollary 4.7 we will prove that if conditions (3.2) and (3 .3)
hold true then they also hold true in a more general situation when conju-
gacy classes (Σ li ) with only one non-trivial cycle are replaced by general
conjugacy classes Σ li,1 ,...,l i,m (i). Similarly one can show that if condition
(3.1) holds true then it also holds true in a general situation when we do not
assume that (σ i) are cycles.
GAUSSIAN FLUCTUATIONS OF CHARACTERS OF SYMMETRIC GROUPS 11
To show that a given sequence of representations has the character factor-
ization property usually it is the most convenient to verify condition (3.1)
or condition (3.2). Then conditions (3.3) and (3.4) are important corollaries
(for applications see Corollary 3.3 below).
Expressions appearing in conditions (3.1)–(3.4) are close ly related to
each other and knowledge of one of them allows us to compute th e oth-
ers (in fact this is how Theorem and Deﬁnition 3.1 will be prov ed). For
general n these formulas are quite involved, however in the following we
will need only such formulas for n ∈ {1, 2 }and these are provided by the
following theorem.
Theorem 3.2. Let (ρq ) has the character factorization property. If the limit
of one of the expressions (3.1)–(3.4) exists for n ∈ {1, 2 }then the limits of
all of the expressions (3.1)–(3.4) exist for n ∈ {1, 2 }.
These limits fulﬁll
(3.5) cl+1 := lim
q →∞
E(σ )q
l− 1
2 = lim
q →∞
E(Σ l)q− l+1
2 = lim
q →∞
E(Rl+1)q− l+1
2 ,
where σ is a cycle of length l and
(3.6) lim
q →∞
Cov(Rl1+1, R l2+1)q− l1 +l2
2 = lim
q →∞
Cov(Σ l1 , Σ l2)q− l1 +l2
2 =
lim
q →∞
Cov•(Σ l1 , Σ l2 )q− l1 +l2
2 +
∑
r≥1
∑
a1,...,a r ≥1
a1+···+ar =l1
∑
b1 ,...,b r ≥1
b1 +···+br =l2
l1l2
r ca1+b1 · · · car+br =
lim
q →∞
Cov(σ 1, σ 2)q
l1 +l2
2 − l1l2cl1+1cl2+1+
∑
r≥1
∑
a1,...,a r ≥1
a1+···+ar =l1
∑
b1 ,...,b r ≥1
b1 +···+br =l2
l1l2
r ca1+b1 · · · car+br
where σ 1, σ 2 are disjoint cycles of length l1, l 2, respectively, and where the
numbers ci were deﬁned in (3.5).
Proof of this theorem is also postponed to Section 4; we will p rove it
together with Theorem 3.1. Identity (3.5) was proved by Bian e [Bia98,
Bia01] and we skip its proof; for Readers acquainted with the results of
Section 4 and Section 5 it will be a simple exercise.
Corollary 3.3. Let (ρq ) be as in Theorem 3.2 and let λ be a random Young
diagram distributed according to the canonical probabilit y measure asso-
ciated to ρq .
