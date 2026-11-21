---
doc_id: arxiv-math-0304010v1
doc_title: "Kerov's central limit theorem for the Plancherel measure on Young diagrams"
section_id: page-007
section_title: "Page 7"
section_number: null
pages: 7-7
source_pdf: 0304010v1.pdf
source_sha256: fc2296c027b3feb0
toc_source: undetermined
doc_brief: "Kerov's central limit theorem for the Plancherel measure on Young diagrams — Consider random Young diagrams with ﬁxed number n of boxes, dis- tributed according to the Plancherel measure Mn."
---
directed downwards, while the columns are counted along the second coordinate s,
directed to the right. Denote by ∂λ the doubly inﬁnite polygonal line which ﬁrst
goes upwards along the r-axis, next goes along the boundary line separating λ from
its complement in R2
+, and then goes to the right along the s–axis. For any a ∈Z′,
the diagonal line s−r = a intersects ∂λ at the midpoint of a certain segment, which
is either vertical or horizontal. According to these two possibilities a is either in
L(λ) or in −L(λ′). This proves (i).
(ii) By the very deﬁnition (1.1), the numbers a ∈Z′
+ such that the diagonal
s −r = a meets a vertical boundary segment are exactly the numbers a1, . . ., ad.
Likewise, the numbers −b ∈Z′
−such that the diagonal s−r = −b meets a horizontal
boundary segment are exactly the numbers −b1, . . ., −bd. This proves (ii).
□
For any λ ∈Y we set
Φ(z; λ) =
∞
Y
i=1
z + i −1
2
z −λi + i −1
2
,
z ∈C.
The product is actually ﬁnite, because λi = 0 when i is large enough. Therefore,
Φ(z; λ) is a rational function in z. We view it as a generating function of λ.
Proposition 1.2. In the notation (1.1), we have
Φ(z; λ) =
d
Y
i=1
z + bi
z −ai
,
(1.3)
which is the presentation of Φ(z; λ) as an incontractible fraction.
Proof. The equality (1.3) follows from Proposition 1.1. This is an incontractible
fraction, because the numbers a1, . . ., ad, −b1, . . . , −bd are pairwise distinct.
□
Another proof of the equality (1.3) is given in [ORV], it follows an idea from
[KO].
As the ﬁrst corollary of (1.3) note the relation
Φ(z; λ′) = 1/Φ(−z; λ).
Remark that Φ(z; λ) = 1 + O( 1
z) near z = ∞, hence both Φ(z; λ) and ln Φ(z; λ)
can be expanded in a power series in z−1, z−2, . . . about z = ∞.
Deﬁnition 1.3. The algebra of polynomial functions on the set Y, denoted as
A, is generated over R by the coeﬃcients of the above expansion of Φ(z; λ) or,
equivalently, of ln Φ(z; λ). We also assume that A contains 1.
Proposition 1.4. We have
ln Φ(z; λ) =
∞
X
k=1
pk(λ)
k
z−k ,
where
pk(λ) =
∞
X
i=1
[(λi −i + 1
2)k −(−i + 1
2)k]
(1.4)
=
d(λ)
X
i=1
[ak
i −(−bi)k].
(1.5)
7
