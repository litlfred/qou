---
doc_id: kmj-48-2-255
doc_title: "A Formula for the Colored Jones Polynomial of 2-Bridge Knots"
section_id: sec-001-2-proof-of-theorem-1
section_title: "Proof of Theorem 1"
section_number: 2
pages: 3-19
source_pdf: KMJ-48-2-255.pdf
source_sha256: 720279042c6d762b
toc_source: inferred
doc_brief: "A Formula for the Colored Jones Polynomial of 2-Bridge Knots — We derive a formula for the colored Jones polynomial of 2-bridge knots."
---
Firstly, we review a result in [5]. Let L be a knot in S3. We consider a 1-tangle
L′ whose closure is L. We assume that L′ is presented as a tangle diagram D in
258
Toshie Takata
generic position with respect to the height function with the end points at the top
and at the bottom. We orient D from the top to the bottom. Let c denote the
number of the crossings in a diagram D. There are eight crossing types given by
the orientations on the two strands and the sign of the crossing, two cap types,
and two cup types by the orientations on the strand in a tangle diagram. The two
crossoing types (1) and (2), the cap type (i), and the cup type (ii) as in Figure 2
are called leftpointing. We construct an enhanced Gauss diagram G for D, which is
a circle containing the combinatorial data which encodes D. We number crossings
by j = 1, · · · , c and denote by σj the sign of the j-th crossing.
We mark the base
K -2
K 2
K 2
K 2
K -2
K -2
(1)
(2)
(i)
(ii)
Figure 2.
A
B
1b-
1a-
2b-
2a-
1c-
1d-
2c-
2d-
C
D
1b+
1c+
2b+
2c+
2a+
2d+
1a+
1d+
K
2
K-2
K
2
K2
K2
K2
K-2
K-2
K-2
K
K
-2
K
-2
2
Figure 3.
point on a circle, which corresponds to the end at the top of D. As going around the
circle clockwise from the base point, with tracing the tangle strand according to its
orientation, we mark 2c points indexed by i = 1, · · · , 2c, which correspond to points
passing crossings on the tangle strand. So, exactly two points of these 2c points
except the base point correspond to one crossing, and one comes from the underpass
A Formula for the Colored Jones Polynomial of 2-Bridge Knots
259
and the other from the overpass. Join these two points on the circle by an oriented
chord from overpass to underpass, and assign the sign of the corresponding crossing.
Each i-th point on the circle is assigned with a pair (j(i), εi), simply denoted by
j(i)εi, where j(i) is the number of the passing crossing, and εi is 1 for an overpass
and −1 for an underpass. Moreover, the circle is marked with blobs K±2 placed
on the leftpointing crossings and cups and caps as in Figure 2. The result is an
enhanced Gauss diagram. For example, the enhanced Gauss diagram for Figure 1
is shown in Figure 3, where oriented chords are not drawn. We denote by i1, · · · , ib
the position of the blobs K±2, where the a-th blob is placed between the ia-th and
(ia + 1)-th positions on the circle, with K2δa.
We put
qj
=
1
2
X
i>j+
σi −1
2
X
i>j−
σi −1
2
c
X
j=1
σj,
d(l)
=
c
X
j=1
qjlj −1
2
X
a
δa −1
2σj,
C0(l)
=
−d(l) −
X
a
k≤ia
δaεklk −1
2
X
j
σjlj −1
2
X
i
k<i
σiεiliεklk
+
X
j
σj(
X
i<j−
εili)(
X
k<j+
εklk).
Theorem 2([5]). A formula for the n-colored Jones polynomial of a 0-framed knot
L0 is given by
JL0(n)
(2)
=
∞
X
lj =0
j=0,...,c
qCn(l)
c
Y
j=1
½
s(j) + lj
lj
¾
σj
(qσj(n−s(j)−1) −1) · · · (qσj(n−s(j)−lj) −1),
where s(j) = −P
i<j−εilj(i), and Cn(l) = d(l)n+C0(l). Here i < j−means i < i0
for i0 such that j = j(i0) and εi0 = −1.
We apply this formula to the 2-bridge knot S(p, t).
From Schubert’s normal form, we get a 1-tangle diagram as in Figure 4 and
5. The corresponding enhanced Gauss diagram without blobs and chords can be
expressed in Figure 7. The number of the crossings equals 2(p−1) = 4p′. We name
by ja (resp. jd) the crossing of the label (2j −1)t
mod 2p (resp. 2jt
mod 2p)
on CD for 1 ≤j ≤p′ and name by jc (resp. jb) the crossing of the label (2j −1)t
mod 2p (resp. 2jt
mod 2p) on AB for 1 ≤j ≤p′. For 1 ≤k ≤p′, there exists
a unique 1 ≤j ≤p′ such that 2k −1 ≡|r(j)| mod 2p, and then ika = ja and
ikc = jc. For 1 ≤j ≤p′, we deﬁne integers ˜r(j) so that ˜r(j) ≡2jt mod 2p and
260
Toshie Takata
−p < ˜r(j) < p.
For 1 ≤k ≤p′, there exists a unique 1 ≤j ≤p′ such that
2k ≡|˜r(j)| mod 2p, and then ik
′b = jb and ik
′d = jd. We have the following
lemma.
Lemma 3. (1) σjc = σja = (−1)[(2j−1)t/p], and σjd = σjb = (−1)[2jt/p].
(2) σja = σ(p′+1−j)b and σik′b = σip′+1−ka.
Proof. (1) It is clear from the deﬁnition.
(2) Since t is odd, 2(p′+1−j)t = (p+1−2j)t ≡pt+(1−t)p−(2j−1)t = p−(2j−1)t
mod 2p. If 2jt ≡±2k mod 2p for 1 ≤k ≤p′, 2(p′ +1−k)−1 = p−2k ≡p∓2jt ≡
p ∓2jt + (t −1)p ≡(p ∓2j)t mod 2p. So the claim holds.
□
Figure 4. p < 2t
t
p-1
p-t
1
2
t
Figure 5. p > 2t
t
t
p-t
p-1
2
1
Let us compute s(ja), s(jb), s(jc), s(jd) for j = 1, · · · , p′. Since the term with
s(j) < 0 does not contribute to the sum in the formula (2), s(1a) = −Pp′
j=1(ljb+ljc)
implies that ljb, ljc = 0 for j = 1, · · · , p′ and s(1a) = 0.
It also follows that
s(jb) = s((j + 1)a) = Pj
k=1 lka for 1 ≤j ≤p′ −1 and s(p′b) = Pp′
k=1 lka. We also
have s(1c) = −Pp′
j=1 ljd and so it follows that ljd = 0 for 1 ≤j ≤p′ and s(1c) = 0.
Thus only parameters lja appear in the formula (2). We may denote lja by simply
A Formula for the Colored Jones Polynomial of 2-Bridge Knots
261
1c
D
C
A
B
jb
j’c
1a
j’d
ja
Figure 6.
A
B
c+
1b-
1a-
2b-
2a-
p-1
2 b-
p-1
2
p-1
2 a-
d-
p-1
2 c-
p-1
2
1c-
1d-
2c-
2d-
C
D
i1
i1’d+
i
p-1
2
i
’d+
b+
a+
a+
Figure 7.
lj for 1 ≤j ≤p′. Moreover, we compute terms in C0(l). If j′a+ < ja+, then ±lj′a
appear in the sum P
i<ja+ εili. So, we have
(3)
X
i<ja+
εili = −
X
j′a+≥ja+
lj′ = −
X
r′(j′)≤r′(j)
lj′ = −
r′(j)
X
k=1
lik.
Similarly, noting that ljd = 0 and that jd corresponds to 2jt on the segment CD,
we have
(4)
X
i<jd+
εili = −
X
r′(j′)≤r′(j)
lj′ = −
r′(j)
X
k=1
lik.
An easy observation gives
(5)
X
i<jb+
εili =
X
i<jc+
εili = 0.
So, from (3), (4), (5) and s(jc) = s(jd) = 0,
(6)
X
j
σj(
X
i<j+
εili)(
X
k<j−
εklk) =
p′
X
j=1
σja(−
r′(j)
X
k=1
lik)(−s(ja)).
(Recall that ir′(j) = j). Now we compute qj. Since ja+ > ja−for any ja, using
262
Toshie Takata
Lemma 3, we get
qja
=
1
2(
X
i>ja+
σi −
X
i>ja−
σi −σja)
=
−1
2
X
ja+≥i≥ja−
σi
=
−1
2(
p′
X
k=r′(j)
(σika + σi′
kb) +
p′
X
k=j
(σka + σkb))
=
−1
2(
p′
X
k=r′(j)
(σika + σip′+1−ka) +
p′
X
k=j
(σka + σ(p′+1−k)a)).
We will write σja = σj.
We consider the case where p < 2t. Let us calculate P
a δa. From Figure 4,
a blob of type (i) appears when the sign of the crossing corresponding to k on
the segment CD with 1 ≤k ≤p −t −1 is −1 and when the sign of the crossing
corresponding to k on the segment CD with p −t + 1 ≤k ≤t −1 is +1. Note that
the blobs in the later case appear between the segment AB and CD (see Figrue 8
and 9). A blob of type (ii) appears when the sign of the crossing corresponding to
k on the segment CD with p −t + 1 ≤k ≤p −1 is −1. Moreover one blob of the
type (i) appears before the curve v2 reaches the crossing p′d and one blob of type
(ii) appears when the curve v1 meets the point C.
1
t
p-t-1
k
2
K
Figure 8.
t
p-t+1
t-1
k
K2
Figure 9.
A Formula for the Colored Jones Polynomial of 2-Bridge Knots
263
Thus
X
δa
=
X
1≤k≤p−t
2
1 −σik
2
−
X
p−t
2 +1≤k≤p′
1 −σik
2
+
X
p−t
2 +1≤k≤t−1
2
1 + σik
2
+
X
1≤k≤p−t
2 −1
1 −σip′+1−k
2
−
X
p−t
2 +1≤k≤p′
1 −σip′+1−k
2
+
X
p−t
2 +1≤k≤t−1
2
1 + σip′+1−k
2
=
X
1≤k≤p−t
2
1 −σik
2
+
X
p−t
2 +1≤k≤t−1
2
σik −
X
t+1
2 +1≤k≤p′
1 −σik
2
+
X
1≤k≤p−t
2 −1
1 −σip′+1−k
2
+
X
p−t
2 +1≤k≤t−1
2
σip′+1−k −
X
t+1
2 ≤k≤p′
1 −σip′+1−k
2
=
2
X
p−t
2 +1≤k≤t−1
2
σik.
Here we used Lemma 3.
It is easy to see that P σj = 4 Pp′
j=1 σja. Therefore, we obtain
d(l)
=
−1
2
p′
X
j=1
{
p′
X
k=r′(j)
(σik + σip′+1−k) +
p′
X
k=j
(σk + σp′+1−k)}lj
−
X
p−t
2 +1≤k≤t−1
2
σik −2
p′
X
j=1
σj
=
−1
2
p′
X
j=1
{
p′
X
k=r′(j)
(σik + σip′+1−k) +
p′
X
k=j
(σk + σp′+1−k)}lj −
p′
X
j=1
σj.
To show the second equality above, we need the following lemma.
Lemma 4. (1) If p < 2t, then
X
p−t
2 +1≤k≤t−1
2
σik = −
p′
X
j=1
σj.
(2) If p > 2t, then
X
t+1
2 ≤k≤p−t
2
σik =
p′
X
j=1
σj.
Proof. In the case where p < 2t, we focus the signs of the crossings labeled by even
on the segment w1. Note that the sum of their signs equals Pp′
j=1 σj. On the other
hand, from Figure 4, it follows that the sum of the signs of the crossings labeled
even j so that 2t −p + 1 ≤j ≤p −1 equals 0 and that the sum of the sign of the
crossing labeled even j so that 2 ≤j ≤2t −p −1 equals −P
p−t
2 +1≤k≤t−1
2 σik. So
264
Toshie Takata
(1) holds. Similarly, in the case where p > 2t, we examine the sum of the sign of
the crossing labeled even on the segment w1 in Figure 5. Note that the sum of their
signs equals Pp′
j=1 σj. From the diagram, it follows that the sum of the sign of the
crossing labeled even j so that 2 ≤j ≤2t equals 0 and that the sum of the sign of
the crossing labeled even j so that 2t + 2 ≤j ≤p −1 equals P
t+1
2 ≤k≤p−t
2 σik. So
we get the equality (2).
□
Next, we calculate the term P
a δa
P
k<ia εklk, which comes from the crossing
of type (2) on CD and blobs of both types on the curve v1. All blobs of type (i)
give
−
X
1≤k≤p−t
2
1 −σik
2
X
1≤s≤ik−1
ls −
X
p−t
2 +1≤k≤t−1
2
1 + σik
2
X
1≤s≤ik−1
ls,
and all blobs of type (ii) except the special blob of type (ii) near C give
X
p−t
2 +1≤k≤p′
1 −σik
2
X
1≤s≤ik−1
ls,
and all crossings of type (2) give
X
p−t
2 +1≤k≤p′
1 + σik
2
(−lik),
and the special blob gives Pp′
j=1 lj.
Moreover, we compute the term P
i
k<i σiεiliεklk. When i < 1a−, i > i1a+,
i = jb−, we have σiεili = 0. If i = 1a−, then P
i
k<i σiεiliεklk = 0. If i = ja−for
2 ≤j ≤p′,
(7)
σiεili
X
k<i
εklk = σj(−1)lj(−
j−1
X
k=1
lk),
and if i = ik′a+ for 1 ≤k′ ≤p′,
(8)
σiεili
X
k<i
εklk = σik′lik′(−
k′
X
k=1
lik).
We remark that ik′+1a±, · · · , ip′a± appear in the sum in the left hand side of (8).
We can see that the term σiklik(−lim) with k < m and j′ = ik > im = j in (8) is
A Formula for the Colored Jones Polynomial of 2-Bridge Knots
265
cancelled with the term σj′(−1)lj′(−lj) in (7). Thus, we get
X
i
k<i
σiεiliεklk
=
−
p′
X
j=1
σjlj
2 +
X
j>j′
ja+>j′a+
(σja −σj′a)ljalj′a
=
−
p′
X
j=1
σjlj
2 +
X
1≤k≤p′−1
X
k+1≤k′≤p′
1 + sign(ik −ik′)
2
(σik −σik′)liklik′.
Finally, we get
C0(l)
=
−d(l) +
X
1≤k≤p−t
2
1 −σik
2
X
1≤s≤ik−1
ls +
X
p−t
2 +1≤k≤t−1
2
1 + σik
2
X
1≤s≤ik−1
ls
−
X
p−t
2 +1≤k≤p′
1 −σik
2
X
1≤s≤ik−1
ls +
X
p−t
2 +1≤k≤p′
1 + σik
2
lik −
p′
X
j=1
lj −1
2
p′
X
j=1
σjlj
−1
2


−
p′
X
j=1
σjlj
2 +
X
1≤k≤p′−1
X
k+1≤k′≤p′
1 + sign(ik −ik′)
2
(σik −σik′)liklik′



+
X
1≤k≤p′
σj
Ã
−
j−1
X
k=1
lik
! 
−
r′(j)
X
k=1
lik


=
−d(l) +
X
1≤k≤p−t
2
1 −σik
2
X
1≤s≤ik−1
ls +
X
p−t
2 +1≤k≤t−1
2
1 + σik
2
X
1≤s≤ik−1
ls
+
X
p−t
2 +1≤k≤p′
1 + σik
2
lik −
X
p−t
2 +1≤k≤p′
1 −σik
2
X
1≤s≤ik−1
ls −
p′
X
j=1
lj −1
2
p′
X
j=1
σjlj
+1
2
p′
X
j=1
σjlj
2 −1
2



X
1≤k≤p′−1
X
k+1≤k′≤p′
1 + sign(ik −ik′)
2
(σik −σik′)liklik′



+
X
1≤k≤p′
σj
Ãj−1
X
k=1
lik
! 

r′(j)
X
k=1
lik

.
Similarly, we compute d(l) and C0(l) in the case where p > 2t. From Figure
5, one can see that a blob of type (i) appears when the sign of the crossing corre-
sponding to k on the segment CD with 1 ≤k ≤p −t −1 is −1. A blob of type
(ii) appears when the sign of the crossing corresponding to k on the segment CD
with p −t + 1 ≤k ≤p −1 is −1 and when the sign of the crossing corresponding to
k on the segment CD with t + 1 ≤k ≤p −t −1 is +1. Moreover one blob of the
266
Toshie Takata
type (ii) appears before the curve v1 arrives at the crossing 1a and one blob of the
same type appears when the curve v1 meets the point C. Therefore, by Lemma 3,
it follows that
X
δa
=
X
1≤k≤p−t
2
1 −σik
2
−
X
p−t
2 +1≤k≤p′
1 −σik
2
−
X
t+1
2 +1≤k≤p−t
2
1 + σik
2
+
X
1≤k≤p−t
2 −1
1 −σip′+1−k
2
−
X
p−t
2 +1≤k≤p′
1 −σip′+1−k
2
−
X
t+1
2 ≤k≤p−t
2 −1
1 + σip′+1−k
2
−2
=
X
1≤k≤t+1
2
1 −σik
2
−
X
t+1
2 +1≤k≤p−t
2
σik −
X
p−t
2 +1≤k≤p′
1 −σik
2
+
X
1≤k≤t−1
2
1 −σip′+1−k
2
−
X
t+1
2 ≤k≤p−t
2 −1
σip′+1−k −
X
p−t
2 +1≤k≤p′
1 −σip′+1−k
2
−2
=
−2
X
t+1
2 ≤k≤p−t
2
σik.
Here we used σi t+1
2
= 1 in the last equality. Accordingly, from Lemma 4, we obtain
d(l)
=
−1
2
p′
X
j=1
{
p′
X
k=r′(j)
(σik + σip′−k) +
p′
X
k=j
(σk + σp′+1−k)}lj
+
X
t+1
2 +1≤k≤p−t
2
σik −2
p′
X
j=1
σj
=
−1
2
p′
X
j=1
{
p′
X
k=r′(j)
(σik + σip′+1−k) +
p′
X
k=j
(σk + σp′+1−k)}lj −
p′
X
j=1
σj.
Next, we calculate the term P
a δa
P
k≤ia εklk. Non-trivial terms correspond to
the crossing of type (2) and blobs of both type on the curve v1. All blobs of type
(i) give
−
X
1≤k≤p−t
2
1 −σik
2
X
1≤s≤ik−1
ls,
and all blobs of type (ii) except the special blob near C give
X
p−t
2 +1≤k≤p′
1 −σik
2
X
1≤s≤ik−1
ls +
X
t+1
2 +1≤k≤p−t
2
1 + σik
2
X
1≤s≤ik−1
ls,
A Formula for the Colored Jones Polynomial of 2-Bridge Knots
267
and all crossings of type (2) give
X
p−t
2 +1≤k≤p′
1 + σik
2
(−lik),
and the special blob gives Pp′
j=1 lj.
From Figure 7, we can see
X
i
k<ia
σiεiliεklk
=
−
p′
X
j=1
σjlj
2 +
X
j>j′
ja+>j′a+
(σja −σj′a)ljalj′a
=
−
p′
X
j=1
σjlj
2 +
X
1≤k≤p′−1
X
k+1≤k′≤p′
1 + sign(ik −ik′)
2
(σik −σik′)liklik′,
and so it is obtained that
C0(l)
=
−d(l)
+
X
1≤k≤p−t
2
1 −σik
2
X
1≤s≤ik−1
ls −
X
p−t
2 +1≤k≤p′
1 −σik
2
X
1≤s≤ik−1
ls
−
X
t+1
2 +1≤k≤p−t
2
1 + σik
2
X
1≤s≤ik−1
ls −
X
p−t
2 +1≤k≤p′
1 + σik
2
(−lik)
−
p′
X
j=1
lj −1
2
p′
X
j=1
σjlj
−1
2{−
p′
X
j=1
σjlj
2 +
X
1≤k≤p′
X
k+1≤k′≤p′
1 + sign(ik −ik′)
2
(σik −σik′)liklik′}
+
X
1≤k≤p′
σj
Ã
−
j−1
X
k=1
lk
! 
−
r′(j)
X
k=1
lik


=
−d(l) +
X
1≤k≤p−t
2
1 −σik
2
X
1≤s≤ik−1
ls +
X
p−t
2 +1≤k≤p′
1 + σik
2
lik
−
X
p−t
2 +1≤k≤p′
1 −σik
2
X
1≤s≤ik−1
ls −
X
t+1
2 +1≤k≤p−t
2
1 + σik
2
X
1≤s≤ik−1
ls
268
Toshie Takata
−
p′
X
j=1
lj −1
2
p′
X
j=1
σjlj + 1
2
p′
X
j=1
σjlj
2
−1
2



X
1≤k≤p′
X
k+1≤k′≤p′
1 + sign(ik −ik′)
2
(σik −σik′)liklik′



+
X
1≤k≤p′
σj(
j−1
X
k=1
lk)(
r′(j)
X
k=1
lik).
We compute the remaining term in the formula (2). Since σ1 = 1, s(1a) = 0,
and s(ja) = Pj−1
k=1 lk(2 ≤j ≤p′),
c
Y
j=1
½ s(j) + lj
lj
¾
σj
(qσj(n−s(j)−1) −1) · · · (qσj(n−s(j)−lj) −1)
=
p′
Y
j=1
½ Pj
k=1 lk
lj
¾
σj
(qσj(n−Pj−1
k=1 lk−1) −1) · · · (qσj(n−Pj−1
k=1 lk−lj) −1).
Putting mj := Pj
k=1 lk and m0 = 0, the right hand side is changed to
(9)
p′
Y
j=1
½
mj
mj −mj−1
¾
σj
(qσj(n−mj−1−1) −1) · · · (qσj(n−mj) −1).
Noting that
(qσj(n−mj−1−1) −1) · · · (qσj(n−mj) −1) = (qσj)n−mj−1−1
(qσj)n−mj−1
,
(10)
½
mj
mj −mj−1
¾
σj
=
(qσj)mj
(qσj)mj−mj−1(qσj)mj−1
,
(11)
(qσ)m
(qσ′)m
= (−1)
σ−σ′
2
mq
σ−σ′
2
· 1
2 m(m+1),
(12)
(9) can be exchanged to
(qσp′)n−1(qσp′)mp′
(qσp′)n−mp′−1


p′
Y
j=1
(qσj)mj−mj−1


−1
A Formula for the Colored Jones Polynomial of 2-Bridge Knots
269
×
p′−1
Y
j=2
(−1)
σj −σj+1
2
mjq
σj −σj+1
2
1
2 mj(mj+1)
×
p′−1
Y
j=2
(−1)
σj+1−σj
2
(n−mj−1)q
σj+1−σj
2
1
2
(n−mj)(n−mj−1)
=
(qσp′)n−1(qσp′)mp′
(qσp′)n−mp′−1


p′
Y
j=1
(qσj)mj−mj−1


−1
q
−n Pp′−1
j=1
σj+1 −σj
2
mj.
Here we used σ2 = σp′ = −1 if p < 2t and σ2 = σp′ = 1 if p > 2t. Recalling
mj −mj−1 = lj, it is changed to
(qσp′)n−1(qσp′)mp′
(qσp′)n−mp′−1
(−1)
Pp′
j=1 ljq−Pp′
j=1
1
2 σjlj(lj+1)
(13)
×


p′
Y
j=1
(q−σj)mj−mj−1


−1
q−n Pp′−1
j=1
σj+1−σj
2
mj.
Accordingly, we obtain
d(l) −
p′−1
X
j=1
σj+1 −σj
2
mj
=
−1
2
p′
X
j=1
{
p′
X
k=r′(j)
(σik + σip′+1−k) +
p′
X
k=j
(σk + σp′+1−k)}(mj −mj−1)
−
p′
X
j=1
σj −
p′−1
X
j=1
σj+1 −σj
2
mj
=
−1
2
p′
X
j=1
p′
X
k=r′(j)
(σik + σip′+1−k)(mj −mj−1) −1
2
p′
X
j=1
p′
X
k=j
(σk + σp′+1−k)(mj −mj−1)
−
p′
X
j=1
σj −
p′−1
X
j=1
σj+1 −σj
2
mj
=
−1
2
p′
X
j=1
p′
X
k=r′(j)
(σik + σip′+1−k)(mj −mj−1) −1
2
p′
X
j=1
(
p′
X
k=j
(σk + σp′+1−k)mj
−
p′
X
k=j+1
(σk + σp′+1−k)mj) −
p′
X
j=1
σj −
p′−1
X
j=1
σj+1 −σj
2
mj
270
Toshie Takata
=
−1
2
p′
X
j=1
p′
X
k=r′(j)
(σik + σip′+1−k)(mj −mj−1) −1
2
p′
X
j=1
(σj + σp′+1−j)mj
−
p′
X
j=1
σj −1
2
p′−1
X
j=1
(σj+1 −σj)mj
=
−1
2
p′
X
j=1
p′
X
k=r′(j)
(σik + σip′+1−k)(mj −mj−1)
−1
2
p′−1
X
j=1
(σj+1 + σp′+1−j)mj −1
2(σp′ + σ1)mp′ −
p′
X
j=1
σj
=
a(m),
and for the case where p < 2t,
C0(l) −
p′
X
j=1
1
2σjlj(lj + 1)
=
−a(m) −1
2
p′−1
X
j=1
(σj+1 −σj)mj
+
X
1≤k≤p−t
2
1 −σik
2
mik−1 +
X
p−t
2 +1≤k≤t−1
2
1 + σik
2
mik−1
+
X
p−t
2 +1≤k≤p′
1 + σik
2
mik −
X
p−t
2 +1≤k≤p′
mik−1 −mp′ −
p′
X
j=1
σj(mj −mj−1)
−1
2



X
1≤k≤p′
X
k+1≤k′≤p′
1 + sign(ik −ik′)
2
(σik −σik′)(mik −mik−1)(mik′ −mik′−1)



+
X
1≤k≤p′
σjmj−1(
r′(j)
X
k=1
(mik −mik−1))
=
−a(m) −(1 + σp′)mp′ + 1
2
p′−1
X
j=1
(σj+1 −σj)mj
+
X
1≤k≤p−t
2
1 −σik
2
mik−1 +
X
p−t
2 +1≤k≤t−1
2
1 + σik
2
mik−1
+
X
p−t
2 +1≤k≤p′
1 + σik
2
mik −
X
p−t
2 +1≤k≤p′
mik−1
A Formula for the Colored Jones Polynomial of 2-Bridge Knots
271
−1
2



X
1≤k≤p′−1
X
k+1≤k′≤p′
1 + sign(ik −ik′)
2
(σik −σik′)(mik −mik−1)(mik′ −mik′−1)



+
X
1≤k≤p′
σjmj−1
r′(j)
X
k=1
(mik −mik−1)
=
b1(m) + b2(m),
and for the case where p > 2t,
C0(l) −
p′
X
j=1
1
2σjlj(lj + 1)
=
−a(m) −1
2
p′−1
X
j=1
(σj+1 −σj)mj
+
X
1≤k≤p−t
2
1 −σik
2
mik−1 +
X
p−t
2 +1≤k≤p−1
2
1 + σik
2
mik −
X
p−t
2 +1≤k≤p−1
2
mik−1
−
X
t+1
2 +1≤k≤p−t
2
1 + σik
2
mik−1 −mp′ −
p′
X
j=1
σj(mj −mj−1)
−1
2



X
1≤k≤p′
X
k+1≤k′≤p′
1 + sign(ik −ik′)
2
(σik −σik′)(mik −mik−1)(mik′ −mik′−1)



+
X
1≤k≤p′
σjmj−1(
r′(j)
X
k=1
(mik −mik−1))
=
−a(m) −(1 + σp′)mp′ + 1
2
p′−1
X
j=1
(σj+1 −σj)mj
+
X
1≤k≤p−t
2
1 −σik
2
mik−1 +
X
p−t
2 +1≤k≤p′
1 + σik
2
mik −
X
p−t
2 +1≤k≤p′
mik−1
−
X
t+1
2 +1≤k≤p−t
2
1 + σik
2
mik−1
−1
2



X
1≤k≤p′−1
X
k+1≤k′≤p′
1 + sign(ik −ik′)
2
(σik −σik′)(mik −mik−1)(mik′ −mik′−1)



+
X
1≤k≤p′
σjmj−1(
r′(j)
X
k=1
(mik −mik−1)) = b1(m) + b2(m).
272
Toshie Takata
Thus we obtain the formula (1).
For example, we give an explicit formula for the colored Jones polynomial of
the knot 62, which is not a twist knot. The knot 62 has the Schubert’s normal form
S(11, 7). We see p′ = 5,
σ1 = 1, σ2 = −1, σ3 = −1, σ4 = 1, σ5 = 1,
r′(1) = 4, r′(2) = 1, r′(3) = 5, r′(4) = 3, r′(5) = 2, i1 = 2, i2 = 5, i3 = 4, i4 = 1, i5 = 3,
σi1 = −1, σi2 = −1, σi3 = 1, σi4 = 1, σi5 = −1,
and so
5
X
k=r′(1)
(σik + σi6−k) = −2,
5
X
k=r′(2)
(σik + σi6−k) = −2,
5
X
k=r′(3)
(σik + σi6−k) = −2,
5
X
k=r′(4)
(σik + σi6−k) = 0,
5
X
k=r′(5)
(σik + σi6−k) = 0,
4
X
j=1
(σj+1 + σ6−j) = −2m1 −2m4.
Thus, we get a(m) = 1 + m1 + m3 + m4. Moreover, we calculate
X
1≤k≤2
1 −σik
2
mik−1 = m1+m4,
X
3≤k≤2
mik−1 = m3+m2,
X
3≤k≤5
1 + σik
2
mik = m4+m1,
1 + σ5 = 0,
4
X
j=1
(σj+1 −σj)mj = −2m1 + 2m3 −2m4,
X
1≤k≤p′−1
X
k+1≤k′≤p′
1 + sign(ik −ik′)
2
(σik −σik′)(mik −mik−1)(mik′ −mik′−1)
=
−2(m2 −m1)m1 −2(m5 −m4)(m4 −m3) −2(m5 −m4)m1 + 2(m4 −m3)(m3 −m2),
p′
X
j=1
σj(
r′(j)
X
k=1
(mik −mik−1))mj−1
=
−m1(m2 −m1) −m2m5) + m3(m2 −m1 + m5 −m3) + (−m4)(m2 −m1 + m5 −m4),
and so b1(m) = −1 −m2 −m3 + m1m5 −m2m5 −m1m3. It is easy to compute
b2(m) = m3.
A Formula for the Colored Jones Polynomial of 2-Bridge Knots
273
Finally, we obtain
JS(11,7)(n)
=
X
0≤mj−1≤mj ≤n−1
1≤j≤5
qn(1+m1+m3+m4)−1−m2+m1m5−m2m5−m1m3
×(q)n−1(q)m5
(q)n−m5−1
((¯q)m1(q)m2−m1(q)m3−m2(¯q)m4−m3(q)m5−m4)−1 (−1)m5.
