---
doc_id: zhao-standard-2010
doc_title: "Standard Relations of Multiple Polylogarithm Values at Roots of Unity"
section_id: sec-025-24-jianqiang-zhao
section_title: "Jianqiang Zhao"
section_number: 24
pages: 24-26
source_pdf: Zhao_standard_2010.pdf
source_sha256: 94a70847c2937ba7
doc_brief: "Standard Relations of Multiple Polylogarithm Values at Roots of Unity — Let N be a positive integer."
---
Theorem 8.3. If p ≥ 5 is a prime then ker βp2 ⁄= 0 and
d(2, p2) < D (2, p2) = ( p2 − p + 2)2/4.
Proof. By the proof of Delign-Goncharov’s bound D(2, p2) in [17, 5.25] we only
need to show ker βp2 ⁄= 0. In the following we adopt the same notation as in
[17] and [30].
Fix a primitive p2th root of unity µ . Put e(a) = eµ a for all integer a. Deﬁne
gk,j = e(pk + j) + e(p2 − pk − j) + e(pj) + e(p2 − pj)
for 0 ≤ k < (p − 1)/2, 1 ≤ j ≤ p − 1, and for k = (p − 1)/2, 1 ≤ j ≤ (p − 1)/2.
One only needs to prove the following
Claim. Let h = (p − 3)/2. Then one has
h∑
k=0
h∑
l=k
p−2∑
j=2
{gk,1, gl,j} +
h+1∑
k=0
h+1∑
j=2
{gk,1, gh+1,j}
+
h∑
k=0
h∑
l=k+1
p−2∑
j=2
{gk,p−1, gl,j} +
h∑
k=0
h+1∑
j=2
{gk,p−1, gh+1,j}
−
h∑
k=0
h∑
l=k
p−2∑
j=2
{gk,j , gl,p−1} −
h∑
k=0
h∑
l=k
p−2∑
j=2
{gk,j , gl+1,1} = 0.
There are h(2h + 3)2 = hp2 distinct terms on the left, each with coeﬃcient ±1.
The proof of the claim is straight-forward by a little tediou s change of indices
and regrouping.
−
h∑
k=0
h∑
l=k
p−2∑
j=2
{gk,j , gl+1,1} =
h∑
k=0
k∑
l=0
p−2∑
j=2
{gk+1,1, gl,j} =
h+1∑
k=1
k−1∑
l=0
p−2∑
j=2
{gk,1, gl,j}.
Then the expression in the claim becomes
h∑
k=1
h∑
l=0
p−2∑
j=2
{gk,1, gl,j} +
h∑
l=0
p−2∑
j=2
{g0,1, gl,j} +
h∑
l=0
p−2∑
j=2
{gh+1,1, gl,j}
+
h+1∑
k=0
h+1∑
j=2
{gk,1, gh+1,j} +
h∑
k=0
h∑
l=0
p−2∑
j=2
{gk,p−1, gl,j} +
h∑
k=0
h+1∑
j=2
{gk,p−1, gh+1,j}
=
h+1∑
k=0
h∑
l=0
p−2∑
j=2
{gk,1, gl,j} +
h+1∑
k=0
h+1∑
j=2
{gk,1, gh+1,j}
+
h∑
k=0
h∑
l=0
p−2∑
j=2
{gk,p−1, gl,j} +
h∑
k=0
h+1∑
j=2
{gk,p−1, gh+1,j}.
Let us write {a, b} = {e(a), e(b)}. By deﬁnition
Documenta Mathematica 15 (2010) 1–34
Relations of Multiple Polylogarithm V alues 25
{gk,1, gl,j}
={pk + 1, pl + j} + {−pk − 1, pl + j} + {p, pl + j} + {−p, pl + j}
+{pk + 1, −pl − j} + {−pk − 1, −pl − j} + {p, −pl − j} + {−p, −pl − j}
+{pk + 1, pj} + {−pk − 1, pj} + {p, pj} + {−p, pj}
+{pk + 1, −pj} + {−pk − 1, −pj} + {p, −pj} + {−p, −pj}
={pk + 1, pl + j} + {p(p − k) − 1, pl + j} + {p, pl + j} + {−p, pl + j}
+{pk + 1, p(p − 1 − l) + p − j} + {p(p − k) − 1, p(p − 1 − l) + p − j}
+ {p, p(p − 1 − l) + p − j} + {−p, p(p − 1 − l) + p − j}
+{pk + 1, pj} + {p(p − k) − 1, pj} + {p, pj} + {−p, pj}
+{pk + 1, p(p − j)} + {p(p − k) − 1, p(p − j)}+{p, p(p − j)}+{−p, p(p − j)}.
Then
h+1∑
k=0
h∑
l=0
p−2∑
j=2
{gk,1, gl,j} =
h+1∑
k=0
h∑
l=0
p−2∑
j=2
{pk + 1, pl + j} + {p(p − k) − 1, pl + j}
+{pk + 1, p(p − 1 − l) + j} + {p(p − k) − 1, p(p − 1 − l) + j}
+{p, pl + j} + {−p, pl + j} + {p, p(p − 1 − l) + j} + {−p, p(p − 1 − l) + j}
+2{pk + 1, pj} + 2{p(p − k) − 1, pj} + 2{p, pj} + 2{−p, pj}
=
h+1∑
k=0
p−1∑
l=0,l⁄=h+1
p−2∑
j=2
{pk + 1, pl + j} +
p∑
k=h+2
p−1∑
l=0,l⁄=h+1
p−2∑
j=2
{pk − 1, pl + j}
+
h+1∑
k=0
p−1∑
l=0,l⁄=h+1
p−2∑
j=2
(
{p, pl + j} + {−p, pl + j}
)
+ 2(h + 1)
h+1∑
k=0
p−2∑
j=2
{pk + 1, pj}
+2(h + 1)
p∑
k=h+2
p−2∑
j=2
{pk − 1, pj} + 2(h + 2)(h + 1)
p−2∑
j=2
(
{p, pj} + {−p, pj}
)
.
Thus
h+1∑
k=0
h∑
l=0
p−2∑
j=2
{gk,1, gl,j} +
h+1∑
k=0
h+1∑
j=2
{gk,1, gh+1,j}
=
h+1∑
k=0
p−1∑
l=0
p−2∑
j=2
{pk + 1, pl + j} +
p∑
k=h+2
p−1∑
l=0
p−2∑
j=2
{pk − 1, pl + j}
+ p + 1
2
p−1∑
l=0
p−2∑
j=2
(
{p, pl + j} + {−p, pl + j}
)
+ p
h+1∑
k=0
p−2∑
j=2
{pk + 1, pj}
+p
p∑
k=h+2
p−2∑
j=2
{pk − 1, pj} + p(p + 1)
2
p−2∑
j=2
(
{p, pj} + {−p, pj}
)
.
Documenta Mathematica 15 (2010) 1–34
