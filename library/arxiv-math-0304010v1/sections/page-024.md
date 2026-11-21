---
doc_id: arxiv-math-0304010v1
doc_title: "Kerov's central limit theorem for the Plancherel measure on Young diagrams"
section_id: page-024
section_title: "Page 24"
section_number: null
pages: 24-24
source_pdf: 0304010v1.pdf
source_sha256: fc2296c027b3feb0
toc_source: undetermined
doc_brief: "Kerov's central limit theorem for the Plancherel measure on Young diagrams — Consider random Young diagrams with ﬁxed number n of boxes, dis- tributed according to the Plancherel measure Mn."
---
Proposition 4.12. For any partition σ and any k ≥2,
p#
σ p#
k = p#
σ∪k +
(
k · mk(σ) · p#
(σ\k)∪1k + . . . ,
mk(σ) ≥1,
. . .,
mk(σ) = 0,
(4.8)
where the partition σ \ k is obtained from σ by removing one part equal to k, i.e.,
mi(σ \ k) =
 mi(σ),
i̸ = k,
mk(σ) −1,
i = k,
and dots mean terms of lower degree, i.e., with deg1( · ) < |σ|1 + k.
Proof. Assume ﬁrst that τ is an arbitrary partition (not necessarily τ = (k)) and
search for partitions ρ such that f ρ
στ̸ = 0 and |ρ|1 = |σ|1 + |τ|1. Let us employ the
notation introduced in the proof of Proposition 4.7 and apply Corollary 4.8. We
get B{1}(s1) = ∅, B{1}(s2) = ∅, and |B{1}(s)| = |X1 ∩X2|. This means that in
X1 ∩X2 there is no 1-cycle (=ﬁxed point) for s1 and s2, but all points of X1 ∩X2
are are ﬁxed by s.
This shows that either X1 ∩X2 = ∅or X1 ∩X2 entirely consists of common
nontrivial cycles of the permutations s1 and s−1
2 .
Now apply this conclusion to the special case τ = (k) that we need. Recall that
k ≥2. The ﬁrst possibility, X1 ∩X2 = ∅, means that ρ = σ ∪τ = σ ∪(k). Then
the corresponding coeﬃcient f ρ
στ equals 1, see (4.1). This explains the term p#
σ∪k
in the right–hand side of (4.8).
The second possibility means that X1 ⊇X2 , because s−1
2
reduces to a single k–
cycle, which is also a k–cycle of s1. This implies that mk(σ) ≥1 and ρ = (σ\k)∪1k.
It remains to evaluate the coeﬃcient f ρ
στ. Let us abbreviate m = mk(σ), l =
m1(σ). We must prove that f ρ
στ = km. To do this we apply Proposition 4.5. We
readily get
zρ
zσzτ
= (k + l)!
l!k2m ,
so that f ρ
στ = km is equivalent to
gρ
στ = (k + l)!
l!k
.
Let us check this. By the deﬁnition of gρ
στ , in our situation it equals the number
of ways to choose a k–cycle inside a (k + l)–point set. This number equals
(k + l)!
k!l!
· (k −1)! = (k + l)!
l!k
,
(the number of k–point subsets inside a (k + l)–point set, times the number of
diﬀerent k–cycle structures on a given k–point set). This concludes the proof.
□
Finally, note that
inv(p#
ρ ) = (−1)|ρ|+ℓ(ρ)p#
ρ .
(4.9)
Indeed, this follows from the deﬁnition of p#
ρ . In particular,
inv(p#
k ) = (−1)k−1p#
k .
(4.10)
This symmetry property will be used in the proofs of Proposition 7.3 and Theorem
10.2.
24
