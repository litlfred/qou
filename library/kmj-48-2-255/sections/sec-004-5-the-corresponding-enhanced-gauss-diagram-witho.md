---
doc_id: kmj-48-2-255
doc_title: "A Formula for the Colored Jones Polynomial of 2-Bridge Knots Toshie Takata"
section_id: sec-004-5-the-corresponding-enhanced-gauss-diagram-witho
section_title: "The corresponding enhanced Gauss diagram without blobs and chords can be"
section_number: 5
pages: 5-10
source_pdf: KMJ-48-2-255.pdf
source_sha256: 720279042c6d762b
doc_brief: "A Formula for the Colored Jones Polynomial of 2-Bridge Knots Toshie Takata — We derive a formula for the colored Jones polynomial of 2-bridge knots."
---
expressed in Figure 7. The number of the crossings equals 2( p − 1) = 4 p′. We name
by ja (resp. jd) the crossing of the label (2 j − 1)t mod 2 p (resp. 2 jt mod 2 p)
on CD for 1 ≤ j ≤ p′ and name by jc (resp. jb) the crossing of the label (2 j − 1)t
mod 2 p (resp. 2 jt mod 2 p) on AB for 1 ≤ j ≤ p′. For 1 ≤ k ≤ p′, there exists
a unique 1 ≤ j ≤ p′ such that 2 k − 1 ≡ | r(j)| mod 2 p, and then ika = ja and
ikc = jc. For 1 ≤ j ≤ p′, we deﬁne integers ˜ r(j) so that ˜r(j) ≡ 2jt mod 2 p and
260 Toshie Takata
−p < ˜r(j) < p . For 1 ≤ k ≤ p′, there exists a unique 1 ≤ j ≤ p′ such that
2k ≡ | ˜r(j)| mod 2 p, and then ik
′b = jb and ik
′d = jd. We have the following
lemma.
Lemma 3. (1) σjc = σja = (−1)[(2j−1)t/p], and σjd = σjb = (−1)[2jt/p].
(2) σja = σ(p′+1−j)b and σik ′b = σip′+1−ka.
Proof. (1) It is clear from the deﬁnition.
(2) Since t is odd, 2( p′ +1 −j)t = (p+1 −2j)t ≡ pt+(1 −t)p−(2j −1)t = p−(2j −1)t
mod 2 p. If 2 jt ≡ ±2k mod 2 p for 1 ≤ k ≤ p′, 2( p′ + 1− k) − 1 = p − 2k ≡ p ∓ 2jt ≡
p ∓ 2jt + (t − 1)p ≡ (p ∓ 2j)t mod 2 p. So the claim holds. □
Figure 4. p < 2t
t
p-1
p-t
1
2
t Figure 5. p > 2t
t
t
p-t
p-1
2
1
Let us compute s(ja), s(jb), s(jc), s(jd) for j = 1, · · · , p′. Since the term with
s(j) < 0 does not contribute to the sum in the formula (2), s(1a) = − ∑p′
j=1(ljb +ljc)
implies that ljb, ljc = 0 for j = 1 , · · · , p′ and s(1a) = 0. It also follows that
s(jb) = s((j + 1)a) = ∑j
k=1 lka for 1 ≤ j ≤ p′ − 1 and s(p′b) = ∑p′
k=1 lka. We also
have s(1c) = − ∑p′
j=1 ljd and so it follows that ljd = 0 for 1 ≤ j ≤ p′ and s(1c) = 0.
Thus only parameters lja appear in the formula (2). We may denote lja by simply
A Formula for the Colored Jones Polynomial of 2-Bridge Knots 261
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
A Bc+
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
d -
p-1
2 c-
p-1
2
1c-
1 d -
2c-
2 d -
CD i1 i1’d + i p-1
2
i ’d +
b+
a+ a+ Figure 7.
lj for 1 ≤ j ≤ p′. Moreover, we compute terms in C 0(l). If j′a+ < ja +, then ±lj′a
appear in the sum ∑
i<ja+ εili. So, we have
(3)
∑
i<ja+
εili = −
∑
j′a+≥ja+
lj′ = −
∑
r′(j′)≤r′(j)
lj′ = −
r′(j)∑
k=1
lik .
Similarly, noting that ljd = 0 and that jd corresponds to 2 jt on the segment CD ,
we have
(4)
∑
i<jd+
εili = −
∑
r′(j′)≤r′(j)
lj′ = −
r′(j)∑
k=1
lik .
An easy observation gives
(5)
∑
i<jb+
εili =
∑
i<jc+
εili = 0.
So, from (3), (4), (5) and s(jc) = s(jd) = 0,
(6)
∑
j
σj(
∑
i<j+
εili)(
∑
k<j−
εklk) =
p′
∑
j=1
σja(−
r′(j)∑
k=1
lik )(−s(ja)).
(Recall that ir′(j) = j). Now we compute qj. Since ja+ > ja − for any ja, using
262 Toshie Takata
Lemma 3, we get
qja = 1
2 (
∑
i>ja+
σi −
∑
i>ja−
σi − σja)
= − 1
2
∑
ja+≥i≥ja−
σi
= − 1
2 (
p′
∑
k=r′(j)
(σika + σi′
kb) +
p′
∑
k=j
(σka + σkb))
= − 1
2 (
p′
∑
k=r′(j)
(σika + σip′ +1−ka) +
p′
∑
k=j
(σka + σ(p′+1−k)a)).
We will write σja = σj.
We consider the case where p < 2t. Let us calculate ∑
a δa. From Figure 4,
a blob of type (i) appears when the sign of the crossing corresponding to k on
the segment CD with 1 ≤ k ≤ p − t − 1 is −1 and when the sign of the crossing
corresponding to k on the segment CD with p − t + 1 ≤ k ≤ t − 1 is +1. Note that
the blobs in the later case appear between the segment AB and CD (see Figrue 8
and 9). A blob of type (ii) appears when the sign of the crossing corresponding to
k on the segment CD with p − t + 1 ≤ k ≤ p − 1 is −1. Moreover one blob of the
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
p- t +1
t -1
k
K2 Figure 9.
A Formula for the Colored Jones Polynomial of 2-Bridge Knots 263
Thus
∑
δa =
∑
1≤k≤ p−t
2
1 − σik
2 −
∑
p−t
2 +1≤k≤p′
1 − σik
2 +
∑
p−t
2 +1≤k≤ t−1
2
1 + σik
2
+
∑
1≤k≤ p−t
2 −1
1 − σip′ +1−k
2 −
∑
p−t
2 +1≤k≤p′
1 − σip′ +1−k
2 +
∑
p−t
2 +1≤k≤ t−1
2
1 + σip′+1−k
2
=
∑
1≤k≤ p−t
2
1 − σik
2 +
∑
p−t
2 +1≤k≤ t−1
2
σik −
∑
t+1
2 +1≤k≤p′
1 − σik
2
+
∑
1≤k≤ p−t
2 −1
1 − σip′ +1−k
2 +
∑
p−t
2 +1≤k≤ t−1
2
σip′+1−k −
∑
t+1
2 ≤k≤p′
1 − σip′+1−k
2
= 2
∑
p−t
2 +1≤k≤ t−1
2
σik .
Here we used Lemma 3.
It is easy to see that ∑ σj = 4 ∑p′
j=1 σja. Therefore, we obtain
d(l) = − 1
2
p′
∑
j=1
{
p′
∑
k=r′(j)
(σik + σip′+1−k ) +
p′
∑
k=j
(σk + σp′+1−k)}lj
−
∑
p−t
2 +1≤k≤ t−1
2
σik − 2
p′
∑
j=1
σj
= − 1
2
p′
∑
j=1
{
p′
∑
k=r′(j)
(σik + σip′+1−k ) +
p′
∑
k=j
(σk + σp′+1−k)}lj −
p′
∑
j=1
σj.
To show the second equality above, we need the following lemma.
Lemma 4. (1) If p < 2t, then
∑
p−t
2 +1≤k≤ t−1
2
σik = −
p′
∑
j=1
σj.
(2) If p > 2t, then
∑
t+1
2 ≤k≤ p−t
2
σik =
p′
∑
j=1
σj.
Proof. In the case where p < 2t, we focus the signs of the crossings labeled by even
on the segment w1. Note that the sum of their signs equals ∑p′
j=1 σj. On the other
hand, from Figure 4, it follows that the sum of the signs of the crossings labeled
even j so that 2 t − p + 1 ≤ j ≤ p − 1 equals 0 and that the sum of the sign of the
crossing labeled even j so that 2 ≤ j ≤ 2t − p − 1 equals − ∑
p−t
2 +1≤k≤ t−1
2
σik . So
264 Toshie Takata
(1) holds. Similarly, in the case where p > 2t, we examine the sum of the sign of
the crossing labeled even on the segment w1 in Figure 5. Note that the sum of their
signs equals ∑p′
j=1 σj. From the diagram, it follows that the sum of the sign of the
crossing labeled even j so that 2 ≤ j ≤ 2t equals 0 and that the sum of the sign of
the crossing labeled even j so that 2 t + 2 ≤ j ≤ p − 1 equals ∑
t+1
2 ≤k≤ p−t
2
σik . So
we get the equality (2). □
Next, we calculate the term ∑
a δa
∑
k<ia εklk, which comes from the crossing
of type (2) on CD and blobs of both types on the curve v1. All blobs of type (i)
give
−
∑
1≤k≤ p−t
2
1 − σik
2
∑
1≤s≤ik−1
ls −
∑
p−t
2 +1≤k≤ t−1
2
1 + σik
2
∑
1≤s≤ik−1
ls,
and all blobs of type (ii) except the special blob of type (ii) near C give
∑
p−t
2 +1≤k≤p′
1 − σik
2
∑
1≤s≤ik−1
ls,
and all crossings of type (2) give
∑
p−t
2 +1≤k≤p′
1 + σik
