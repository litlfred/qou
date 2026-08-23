---
doc_id: zhao-standard-2010
doc_title: "Standard Relations of Multiple Polylogarithm Values at Roots of Unity"
section_id: sec-026-26-jianqiang-zhao
section_title: "Jianqiang Zhao"
section_number: 26
pages: 26-28
source_pdf: Zhao_standard_2010.pdf
source_sha256: 94a70847c2937ba7
doc_brief: "Standard Relations of Multiple Polylogarithm Values at Roots of Unity — Let N be a positive integer."
---
Similarly,
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
k=1
p−1∑
l=0
p−2∑
j=2
{pk − 1, pl + j} +
p−1∑
k=h+2
p−1∑
l=0
p−2∑
j=2
{pk + 1, pl + j}
+ p − 1
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
k=1
p−2∑
j=2
{pk − 1, pj}
+p
p−1∑
k=h+2
p−2∑
j=2
{pk + 1, pj} + p(p − 1)
2
p−2∑
j=2
(
{p, pj} + {−p, pj}
)
.
Altogether the expression in the claim is reduced to
X :=
p−1∑
k=0
p−1∑
l=0
p−2∑
j=2
{pk + 1, pl + j} +
p∑
k=1
p−1∑
l=0
p−2∑
j=2
{pk − 1, pl + j}
+p
p−1∑
l=0
p−2∑
j=2
(
{p, pl + j} + {−p, pl + j}
)
+ p
p−1∑
k=0
p−2∑
j=2
{pk + 1, pj}
+p
p∑
k=1
p−2∑
j=2
{pk − 1, pj} + p2
p−2∑
j=2
(
{p, pj} + {−p, pj}
)
.
To see this last expression can be reduced to 0 we recall that b y deﬁnition [17,
(5.13.6)]
{a, b} = {ea, eb} = [ea, eb] + ∂a(eb) − ∂b(ea),
where ∂a is the derivation deﬁned by ∂a(e0) = 0 and ∂a(eζ) = [ −[ζ](ea), eζ]
for any p2th root of unity ζ (see [17, (5.13.4)]). Thus by abuse of notation
[x, y] = [ e(x), e(y)] we get
X =
p−1∑
k=0
p−1∑
l=0
p−2∑
j=2
(
[pk + 1, pl + j] − [p(k + l) + j + 1, pl + j]
+ [p(k + l) + j + 1, pk + 1]
)
(42)
+
p∑
k=1
p−1∑
l=0
p−2∑
j=2
(
[pk − 1, pl + j] − [p(k + l) + j − 1, pl + j]
+ [p(k + l) + j − 1, pk − 1]
)
(43)
+p
p−1∑
l=0
p−2∑
j=2
(
[p, pl + j] − [p(l + 1) + j, pl + j] + [p(l + 1) + j, p]
Documenta Mathematica 15 (2010) 1–34
Relations of Multiple Polylogarithm V alues 27
+[−p, pl + j] − [p(l − 1) + j, pl + j] + [p(l − 1) + j, −p]
)
(44)
+p
p−1∑
k=0
p−2∑
j=2
(
[pk + 1, pj] − [p(j + k) + 1, pj] + [p(j + k) + 1, pk + 1]
)
(45)
+p
p∑
k=1
p−2∑
j=2
(
[pk − 1, pj] − [p(j + k) − 1, pj] + [p(j + k) − 1, pk − 1]
)
(46)
+p2
p−2∑
j=2
(
[p, pj] − [p(j + 1), pj] + [p(j + 1), p] + [−p, pj]
− [p(j − 1), pj] + [p(j − 1), −p]
)
. (47)
Now by skew-symmetry of Lie bracket
(42) + (43)
=
p−1∑
k=0
p−1∑
l=0
p−2∑
j=2
[pk + 1, pl + j] +
p−1∑
k=0
p−1∑
l=0
p−2∑
j=2
[pk + j, pl + j + 1]
−
p−1∑
k=0
p−1∑
l=0
p−1∑
j=3
[pk + 1, pl + j] +
p∑
k=1
p−1∑
l=0
p−2∑
j=2
[pk − 1, pl + j]
−
p∑
k=1
p−1∑
l=0
p−3∑
j=1
[p(k + l) + j, pl + j + 1] +
p∑
k=1
p−1∑
l=0
p−3∑
j=1
[pl + j, pk − 1]
=
p−1∑
k=0
p−1∑
l=0
[pk + 1, pl + 2] +
p−1∑
k=0
p−1∑
l=0
[pk + p − 2, pl + p − 1]
−
p−1∑
k=0
p−1∑
l=0
[pk + 1, pl + p − 1] +
p∑
k=1
p−1∑
l=0
[pk − 1, pl + p − 2]
−
p∑
k=1
p−1∑
l=0
[pk + 1, pl + 2] +
p∑
k=1
p−1∑
l=0
[pl + 1, pk − 1] = 0 .
Similarly we can easily ﬁnd that (44) = (45) = (46) = (47) = 0. Th is ﬁnishes
the proof of the theorem.
Remark 8.4. The theorem corrects a misprint in the statement of [30, Thm. 2].
In the three cases ( w, N) = (2 , 8), (2, 10) and (2 , 12) we see that SR(N ) >
d(w; N ) = D(w; N ). By numerical computation we have
Conjecture 8.5. We have
d(2, 8) = 9 , d (2, 10) = d(2, 12) = 15 ,
Documenta Mathematica 15 (2010) 1–34
