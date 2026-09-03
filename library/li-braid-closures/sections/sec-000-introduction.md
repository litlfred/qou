---
doc_id: li-braid-closures
doc_title: "Knot polynomials on braid closures Eddy Li"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-2
source_pdf: Li-braid-closures.pdf
source_sha256: f7410e7be5bc187e
---
A knot is an embedding of the circleS 1 inS 3, while a link is an embedding of several circles
inS 3. Through the remainder of this paper, we tacitly work with tame links only.
Definition 1.1.Asplittingof a linkLis a manifoldB⊂S 3\Lsuch thatBis homeomorphic
toS 2 andLintersects both connected components ofS 3\B.
Informally, this occurs exactly whenLcan be separated into two rigid components that
can be moved arbitrarily far away from each other without disturbing isotopy classes.
Example 1.2.The Hopf link features two linked circles; physical intuition implies that it
exhibits no splitting. Indeed, if a split link has two circles, then it must be the unlink on
two circles, which has Jones polynomial− 1√
t(1 +t). Meanwhile, the Hopf link has different
Jones polynomial− 1√
t(1 + 1
t2 ).
The Jones polynomialV L(t) is obtained upon specialization of the HOMFLYPT poly-
nomialX L(q,Λ) atq= Λ =t, where we have used the capital letter Λ instead of the more
standardλin order to avoid confusion with the partitionsλ⊢n.
Proposition 1.3.IfLis a split link, then∆ L(t) = 0.
1
Proof.IfLsplits intoL 1 andL 2, then by the skein relations [1, Example 6.7] we have
XL(q,Λ) =− (1−Λq)X L1(q,Λ)XL2(q,Λ)√
Λ(1−q)
,
which must equal zero if Λq= 1 andq̸= 1. Since the Alexander polynomial satisfies
∆L(t) =X L(t, 1
t ), it follows that ∆L(t) = 0 for allt∈C\{1}. We finish by continuity.
By Proposition 1.3 that the Alexander polynomial detects all splittings. We concern
ourselves with the special value of thethe knot determinantV L(−1) = ∆L(−1).
Question 1.4.Is there a linkLwith no splitting such that∆ L(−1) = 0?
The answer to Question 1.4 is in the positive. In fact, given anyL, there is [2] an infinite
family of distinct linksL ′ all with Jones polynomial equal toV L′(t) =−(
√
t+ 1√
t)VL(t).
Thus ∆L′(−1) =V L′(−1) =X L′(−1,−1) = 0. However, the construction used to create
such links are quite complicated, so we will consider simpler methods.
Theorem 1.5(Theorems 3.8 and 3.9).There exists an infinite family of linksL m,k, indexed
by pairs of integers(m,k), with the property that any linkLsatisfyingV L(−1) = ∆L(−1) = 0
is equivalent to someL m,k. In addition,L m,k has a splitting if and only ifm= 0.
The construction of eachL m,k is much simpler than that of [2]. It turns out our work
also yields pairs of distinct non-split links with the same HOMFLYPT polynomial, as in
our second main result.
Theorem 1.6(Theorem 3.10).If6|k, thenX ˆγm,k(q,Λ) =X ˆγm+k
6,−k
(q,Λ).
The linksL m,k all contain either two or three circles, motivating us to consider how
∆L(−1) would behave ifLhad braid index at most 3 but was forced to be a knot. Surpris-
ingly, we prove the following third main result in Section 3.2.
Theorem 1.7(Theorem 3.15).IfLis a knot with braid index at most3, thenV L(−1)≡
∆L(−1)≡1 (mod 4).
