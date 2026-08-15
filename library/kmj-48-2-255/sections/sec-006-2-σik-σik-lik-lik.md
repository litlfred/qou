---
doc_id: kmj-48-2-255
doc_title: "A Formula for the Colored Jones Polynomial of 2-Bridge Knots Toshie Takata"
section_id: sec-006-2-σik-σik-lik-lik
section_title: "(σik − σik′ )lik lik′"
section_number: 2
pages: 11-13
source_pdf: KMJ-48-2-255.pdf
source_sha256: 720279042c6d762b
doc_brief: "A Formula for the Colored Jones Polynomial of 2-Bridge Knots Toshie Takata — We derive a formula for the colored Jones polynomial of 2-bridge knots."
---
Finally, we get
C 0(l) = −d(l) +
∑
1≤k≤ p−t
2
1 − σik
2
∑
1≤s≤ik−1
ls +
∑
p−t
2 +1≤k≤ t−1
2
1 + σik
2
∑
1≤s≤ik−1
ls
−
∑
p−t
2 +1≤k≤p′
1 − σik
2
∑
1≤s≤ik−1
ls +
∑
p−t
2 +1≤k≤p′
1 + σik
2 lik −
p′
∑
j=1
lj − 1
2
p′
∑
j=1
σjlj
− 1
2


−
p′
∑
j=1
σjlj
2 +
∑
1≤k≤p′−1
∑
k+1≤k′≤p′
1 + sign(ik − ik′)
2 (σik − σik′ )lik lik′



+
∑
1≤k≤p′
σj
(
−
j−1∑
k=1
lik
) 
−
r′(j)∑
k=1
lik


= −d(l) +
∑
1≤k≤ p−t
2
1 − σik
2
∑
1≤s≤ik−1
ls +
∑
p−t
2 +1≤k≤ t−1
2
1 + σik
2
∑
1≤s≤ik−1
ls
+
∑
p−t
2 +1≤k≤p′
1 + σik
2 lik −
∑
p−t
2 +1≤k≤p′
1 − σik
2
∑
1≤s≤ik−1
ls −
p′
∑
j=1
lj − 1
2
p′
∑
j=1
σjlj
+ 1
2
p′
∑
j=1
σjlj
2 − 1
2



∑
1≤k≤p′−1
∑
k+1≤k′≤p′
1 + sign(ik − ik′)
2 (σik − σik′ )lik lik′



+
∑
1≤k≤p′
σj
(j−1∑
k=1
lik
) 

r′(j)∑
k=1
lik

 .
Similarly, we compute d(l) and C 0(l) in the case where p > 2t. From Figure
5, one can see that a blob of type (i) appears when the sign of the crossing corre-
sponding to k on the segment CD with 1 ≤ k ≤ p − t − 1 is −1. A blob of type
(ii) appears when the sign of the crossing corresponding to k on the segment CD
with p − t + 1 ≤ k ≤ p − 1 is −1 and when the sign of the crossing corresponding to
k on the segment CD with t + 1 ≤ k ≤ p − t − 1 is +1. Moreover one blob of the
266 Toshie Takata
type (ii) appears before the curve v1 arrives at the crossing 1 a and one blob of the
same type appears when the curve v1 meets the point C. Therefore, by Lemma 3,
it follows that
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
2 −
∑
t+1
2 +1≤k≤ p−t
2
1 + σik
2
+
∑
1≤k≤ p−t
2 −1
1 − σip′+1−k
2 −
∑
p−t
2 +1≤k≤p′
1 − σip′+1−k
2
−
∑
t+1
2 ≤k≤ p−t
2 −1
1 + σip′ +1−k
2 − 2
=
∑
1≤k≤ t+1
2
1 − σik
2 −
∑
t+1
2 +1≤k≤ p−t
2
σik −
∑
p−t
2 +1≤k≤p′
1 − σik
2
+
∑
1≤k≤ t−1
2
1 − σip′+1−k
2 −
∑
t+1
2 ≤k≤ p−t
2 −1
σip′+1−k −
∑
p−t
2 +1≤k≤p′
1 − σip′ +1−k
2 − 2
= −2
∑
t+1
2 ≤k≤ p−t
2
σik .
Here we used σi t+1
2
= 1 in the last equality. Accordingly, from Lemma 4, we obtain
d(l) = − 1
2
p′
∑
j=1
{
p′
∑
k=r′(j)
(σik + σip′−k ) +
p′
∑
k=j
(σk + σp′+1−k)}lj
+
∑
t+1
2 +1≤k≤ p−t
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
Next, we calculate the term ∑
a δa
∑
k≤ia
εklk. Non-trivial terms correspond to
the crossing of type (2) and blobs of both type on the curve v1. All blobs of type
(i) give
−
∑
1≤k≤ p−t
2
1 − σik
2
∑
1≤s≤ik−1
ls,
and all blobs of type (ii) except the special blob near C give
∑
p−t
2 +1≤k≤p′
1 − σik
2
∑
1≤s≤ik−1
ls +
∑
t+1
2 +1≤k≤ p−t
2
1 + σik
2
∑
1≤s≤ik−1
ls,
A Formula for the Colored Jones Polynomial of 2-Bridge Knots 267
and all crossings of type (2) give
∑
p−t
2 +1≤k≤p′
1 + σik
