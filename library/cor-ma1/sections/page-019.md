---
doc_id: cor-ma1
doc_title: "Overpartitions, lattice paths and Rogers-Ramanujan identities"
section_id: page-019
section_title: "Page 19"
section_number: null
pages: 19-19
source_pdf: cor-ma1.pdf
source_sha256: d90c91dcd82bfcab
toc_source: undetermined
doc_brief: "Corteel & Mallet, Overpartitions, lattice paths, and Rogers-Ramanujan identities (HAL hal-00017295) — extends Andrews, Bressoud and Burge to overpartitions via successive ranks and generalized…"
---
18
SYLVIE CORTEEL AND OLIVIER MALLET
Substituting into Lemma 6.1 and simplifying, we obtain
X
n1≥···≥nk≥0
q(
n1+1
2 )+n2
2+···+n2
k+ni+1+···+nk(−1/a)n1an1
(q)n1−n2 · · · (q)nk−1−nk(q)nk
=(−aq)∞
(q)∞
 
1 +
∞
X
n=1
q(k+1)n2+(k−i+1)n+(−a)n(−1/a)n
(−aq)n
+
∞
X
n=1
q(k+1)n2−(k−i)n(−a)n(−1/a)n
(−aq)n
!
=(−aq)∞
(q)∞
 
1 +
∞
X
n=1
q(k+1)n2+(k−i+1)n(−a)n(−1/a)n
(−aq)n
+
−1
X
n=−∞
q(k+1)n2+(k−i+1)n(−a)n(−1/a)n
(−aq)n
!
.
Replacing k by k −1 and i by i −1 gives (1.1).
□
6.2. A combinatorial proof. We will use and generalize the notion of relative height of a peak. This
notion was deﬁned by Bressoud in [14] for paths with no South steps and a simpler version of the deﬁnition
was given in [10]. We adapt this deﬁnition for the paths with South steps.
Deﬁnition 6.2. The relative height of a peak (x, y) is the largest integer h for which we can ﬁnd two vertices
on the path, (x′, y −h) and (x′′, y −h), such that x′ < x ≤x′′ and such that between these two vertices
there are no peaks of height > y and every peak of height y has abscissa ≥x.
The original deﬁnition was the same except x ≤x′′ was x < x′′. Indeed when there are no South steps
the case x = x′′ is impossible.
For example, the relative heights in the path from Figure 9 are, from left to right: 1, 2, 1, 4, 3, 2.
×
×
×
×
×
×
×
×
×
×
×
×
×
1
2
1
4
3
2
Figure 9. An example of a path and its relative heights.
We will prove here that
Proposition 6.3. The coeﬃcient of qnaℓin
(6.3)
q(
n1+1
2 )+n2
2+···+n2
k−1+ni+···+nk−1(−1/a)n1an1
(q)n1−n2 · · · (q)nk−2−nk−1(q)nk−1
is the number of paths with major index n and ℓSouth steps, starting at height k −i, whose height is less
than k and having nj peaks of relative height ≥j for 1 ≤j ≤k −1. Therefore,
X
n1≥···≥nk−1≥0
q(
n1+1
2 )+n2
2+···+n2
k−1+ni+···+nk−1(−1/a)n1an1
(q)n1−n2 · · · (q)nk−2−nk−1(q)nk−1
= Ek,i(a, q).
To prove this proposition we will use a result of Bressoud [14]
Lemma 6.4. The coeﬃcient of qn in
qn2
1+n2
2+···+n2
k−1+ni+···+nk−1
(q)n1−n2 · · · (q)nk−2−nk−1(q)nk−1
is the number of paths with major index n, no South steps, starting at height k −i, whose height is less than
k and having nj peaks of relative height ≥j for 1 ≤j ≤k −1.
