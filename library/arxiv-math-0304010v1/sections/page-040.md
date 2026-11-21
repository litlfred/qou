---
doc_id: arxiv-math-0304010v1
doc_title: "Kerov's central limit theorem for the Plancherel measure on Young diagrams"
section_id: page-040
section_title: "Page 40"
section_number: null
pages: 40-40
source_pdf: 0304010v1.pdf
source_sha256: fc2296c027b3feb0
toc_source: undetermined
doc_brief: "Kerov's central limit theorem for the Plancherel measure on Young diagrams — Consider random Young diagrams with ﬁxed number n of boxes, dis- tributed according to the Plancherel measure Mn."
---
Proposition 8.7. We have t(n)
= t(n)
Proof. Recall that for any measure from M0, the ﬁrst moment equals zero. In
particular, this holds for bλ and µs-c, which implies t(n)
1
≡0.
Next, the relation h2 = 1
2(p2
1 + p2) in the algebra Λ turns, under the morphism
(2.18), into the relation eh2 = ep2/2 = p1 in the algebra A. It follows that eh2[λ( · )] ≡
n = |λ|, which implies eh2[¯λ( · )] ≡1. This in turn means that the second moment of
bλ equals 1. On the other hand, the second moment of µs-c also equals 1. Therefore,
the second moment of bλ −µs-c equals 0 for any λ ∈Yn, so that eh(n)
2
≡0.
□
Theorem 8.8 (Central limit theorem for transition measures, cf. Theo-
rem 7.1).
3
In the notation introduced above,
n
t(n)
k
o
k≥3
d
−→
n√
k −1 ξk−1
o
k≥3 ,
where ξ2, ξ3, . . . are independent standard Gaussian random variables.
Here we start with k = 3, because t(n)
1
= t(n)
2
≡0, see Proposition 8.5.
Outline of proof. Since the argument is strictly parallel to that given above for
Theorem 7.1, we will not repeat all the details.
Step 1: Expressing ehk through p#
1 , p#
2 , . . ., up to lower weight terms.
This is a counterpart of Proposition 3.7. We start with formula (3.6) of Propo-
sition 3.7, which we rewrite as follows
p#
k−1 = −
1
k−1 [tk]{A−(k−1)(t)} + . . .,
k = 2, 3, . . .,
where
A(t) = 1 +
∞
X
j=2
ehjtj
and dots mean lower weight terms. Applying Proposition 3.6 we invert this formula
and get
ehk =
1
k + 1[uk]{Bk+1(u)} + . . .,
k = 2, 3, . . .,
where
B(u) = 1 +
∞
X
j=2
p#
j−1uj
and dots mean a polynomial in {p#
j−1} of weight < k, where, by deﬁnition,
wt(p#
j−1) = j. More explicitly,
ehk =
X
m2,m3,...
2m2+3m3+···=k
k↓(P mi−1)
Q mi!
Y
(p#
i−1)mi + lower weight terms.
(8.8)
3As was already mentioned in Introduction, this result is due to the authors.
40
