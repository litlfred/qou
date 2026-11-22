---
doc_id: arxiv-math-0408078v2
doc_title: "A basis for the full Homfly skein of the annulus"
section_id: sec-011-calculations
section_title: "Calculations"
section_number: null
pages: 13-16
source_pdf: 0408078v2.pdf
source_sha256: b632eb5e9b7a1753
toc_source: outline
doc_brief: "A basis for the full Homfly skein of the annulus — A basis, denoted {Qλ,µ}, for the full Homﬂy skein of the annulus C was introduced in [18], where λ and µ are partitions of integers n and p into k"
---
choice of v will be unimportant, and we frequently suppress it, giving simply
the template.
2.2
Calculations
Throughout this section we use matrices whose entries are drawn from the
sequences of elements of A or C described in section 1.8. The sequences will
be denoted by the letters used there, h, h∗, y, y∗, l, r, L, R. The deﬁnitions
can in all cases be extended to allow for negative index by setting hj = h∗
j =
yj = y∗
j = lj = rj = Lj = Rj = 0 when j < 0. The equations at the end of
section 1.8 relating the sequences continue to hold in the extended range.
Lemma 2.1 For each i ≥1 and ﬁxed index vector we have the following
equations in A.
det
 
i
↓
· · ·
y∗
R
· · ·
· · ·
y
r
· · ·
!
=
det
 
i
↓
· · ·
y∗
y∗
· · ·
· · ·
y
y
· · ·
!
(16)
det
 
i
↓
· · ·
y∗
L
· · ·
· · ·
y
l
· · ·
!
=
det
 
i
↓
· · ·
y∗
y∗
· · ·
· · ·
y
y
· · ·
!
(17)
13
Proof:
The column operation Ci+1 7→saCi + Ci+1 applied to the matrix
on the lefthand side of equation (16) gives the matrix on the righthand side,
using (13) on starred rows and (12) on standard rows.
The column operation Ci+1 7→s−1aCi +Ci+1 works similarly for equation
(17) using (11) on starred rows and (10) on standard rows.
✷
Corollary 2.2 For each j ≥1 we have
det
 
j
↓
· · ·
y∗
R
⊣
· · ·
y
r
⊣
!
= det
 
j
↓
· · ·
y∗
⊣
· · ·
y
⊣
!
= det
 
j
↓
· · ·
y∗
L
⊣
· · ·
y
l
⊣
!
Proof: Apply equation (16) repeatedly, for i from j onwards, to get the ﬁrst
equation, and similarly use (17) repeatedly to get the second equation.
✷
Lemma 2.3 For each j ≥1 we have
(s −s−1) det
 
j
↓
· · ·
y∗
· · ·
· · ·
y
· · ·
!
=
s det
 
j
↓
· · ·
L
· · ·
· · ·
l
· · ·
!
−s−1 det
 
j
↓
· · ·
R
· · ·
· · ·
r
· · ·
!
.
Proof:
Expand the determinants by the jth column, using equations (15)
on the starred rows and (14) on the standard rows.
✷
Notation. Write
∆j
=
det
 
j+1
↓
L
⊣
R
⊣
l
⊣
r
⊣
!
, 0 ≤j < k∗+ k,
∆k∗+k
=
det
 L
⊣
l
⊣

,
for any choice of index vector.
14
Lemma 2.4 We have
(s −s−1) det
 
j
↓
L
⊣
y∗
L
⊣
l
⊣
y
l
⊣
!
= s∆j −s−1∆j−1, 1 ≤j ≤k∗+ k.
Proof:
(s −s−1) det
 
j
↓
L
⊣
y∗
L
⊣
l
⊣
y
l
⊣
!
=
(s −s−1) det
 
j
↓
L
⊣
y∗
R
⊣
l
⊣
y
r
⊣
!
,
by corollary 2.2
=
s∆j −s−1∆j−1, by lemma 2.3
✷
Expanding further by lemma 2.3 gives
s∆j −s−1∆j−1 = s det

L
⊣
l
⊣

−s−1 det
 
j
↓
L
⊣
R
L
⊣
l
⊣
r
l
⊣
!
.
(18)
Corollary 2.5 We have
k∗+k−1
X
j=1
s2j det

L
⊣
l
⊣

+ det

R
⊣
r
⊣

=
k+k∗
X
j=1
s2j−2 det
 
j
↓
L
⊣
R
L
⊣
l
⊣
r
l
⊣
!
.
Proof:
Multiply both sides of (18) by s2j−1 and sum to get
s2(k∗+k)∆k∗+k −∆0
=
k+k∗
X
j=1
s2j det

L
⊣
l
⊣

−
k+k∗
X
j=1
s2j−2 det
 
j
↓
L
⊣
R
L
⊣
l
⊣
r
l
⊣
!
,
and then rearrange the terms.
✷
15
Lemma 2.6 For any index vector w we have
s−k∗
 k∗+k−1
X
j=1
s2j
!
det
 l(h∗)
⊣
l(h)
⊣

w
+ sk∗det
 r(h∗)
⊣
r(h)
⊣

w
= s−k∗
k+k∗
X
j=1
det
 
j
↓
l(h∗)
⊣
s2jr(h∗)
l(h∗)
⊣
l(h)
⊣
s2j−2r(h)
l(h)
⊣
!
w
.
Proof:
Recall that Ln−1 = (−a)s−1l(h∗
n) and Rn−1 = (−a)sr(h∗
n).
Use
corollary 2.5 with index vector v given by reducing all starred indices of w
by 1, and leaving the standard indices unaltered. Then take out a factor of
−a from each starred row to get
(−a)k∗
 k∗+k−1
X
j=1
s2j
!
det

s−1l(h∗)
⊣
l(h)
⊣

w
+ (−a)k∗det

sr(h∗)
⊣
r(h)
⊣

w
= (−a)k∗
k+k∗
X
j=1
s2j−2 det
 
j
↓
s−1l(h∗)
⊣
sr(h∗)
s−1l(h∗)
⊣
l(h)
⊣
r(h)
l(h)
⊣
!
w
.
The factor (−a)k∗can be cancelled. Extract k∗further factors of s or s−1
from the starred rows, and insert the factor s2j−2 into the jth column of the
appropriate matrix to complete the proof.
✷
