---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-141-6e-proof-of-lemma-63-rearrangement
section_title: "6E. Proof of Lemma 6.3: rearrangement"
section_number: null
pages: 272-275
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
tuple k=(k1,..., kn) with k1≤k2≤···≤ kn, Bn,r( j; k)=1 for j=0, Bn,r( j; k)=k
θ j
1 for j=1,..., n−1,
and for j= n we have Bn,r( j; k)=(k1··· kn/2)2r if n is even and Bn,r( j; k)=(k1··· k(n−1)/2)2rkr
(n+1)/2
if n is odd.
We may quickly dispatch the case j= 0, in which case
‖2δ‖−(2r−1)Bn,r( j; 2tσ−δσ)−1=‖ 2δ‖−(2r−1)≤ 1.
Burgess bounds for short character sums evaluated at forms 1939
For the remaining cases of j≥ 1, it is helpful to invert, and take the logarithm, and prove for ﬁxed δ and
ﬁxed j a lower bound for the quantity
log2
(
‖2δ‖(2r−1)Bn,r( j; 2tσ−δσ)
)
.
First we consider the case of 1≤ j≤ n− 1; for each of these j (using the fact that∑
iδσ(i)=∑
iδi),
log2
(
‖2δ‖(2r−1)Bn,r( j; 2tσ−δσ)
)
=(2r− 1)
( n∑
i=1
δσ(i)
)
+θ j(tσ( 1)−δσ( 1))
=θ jtσ( 1)+(2r− 1−θ j)δσ( 1)+(2r− 1)
n∑
i=2
δσ(i)≥θ jtσ( 1).
Here we used that for 1≤ j≤ n− 1 we haveθ j≤ r− 1, and moreoverδσ(i)≥ 0 for all 1≤ i≤ n. Thus
‖2δ‖−(2r−1)Bn,r( j; 2tσ−δσ)−1≤ 2−θ j tσ( 1)≤ 2−θ j t1= K
−θ j
1 ,
upon recalling that t1≤ t2≤···≤ tn.
Now we turn to the more complicated case of j= n. First we assume that n is even. Now we have
log2
(
‖2δ‖(2r−1)Bn,r( j; 2tσ−δσ)
)
=(2r− 1)
n∑
i=1
δσ(i)+ 2r
n/2∑
i=1
(tσ(i)−δσ(i)).
It is convenient to set temporarily for each i= 1,..., n the parameter 2n,i= 2r if 1≤ i≤ n/2 and
2n,i= 0 if n/2< i≤ n. Then upon recalling that each δi≤ ti, we have
log2
(
‖2δ‖(2r−1)Bn,r( j; 2tσ−δσ)
)
=(2r− 1)
n∑
i=1
δσ(i)+
n∑
i=1
2n,i(tσ(i)−δσ(i))=
n∑
i=1
2n,itσ(i)+
n∑
i=1
(2r− 1−2n,i)δσ(i)
≥
n∑
i=1
2n,itσ(i)+
n∑
i=1
2r−1−2n,i<0
(2r− 1−2n,i)tσ(i)+
n∑
i=1
2r−1−2n,i≥0
(2r− 1−2n,i)· 0
=
n∑
i=1
2r−1−2n,i<0
(2r− 1)tσ(i)+
n∑
i=1
2r−1−2n,i≥0
2n,itσ(i). (6-7)
(Here in the inequality, equality can occur for those δ such thatδi= ti for all 1≤ i≤ n/2 andδi= 0
for n/2< i≤ n. The inequality is where we see that if 2n,i= 2r, we must replaceδσ(i) by tσ(i) rather
than by 0; this is why in the ﬁnal statement of the inequality we lose slightly in the maximal moment,
compared to the nonmaximal moment. This effect is not possible in dimension n= 1.) Now by the
deﬁnition of 2n,i, the ﬁrst sum is over 1≤ i≤ n/2; the second sum is over n/2< i≤ n, in which range
2n,i= 0 so that the second sum is vacuous. Now we use the following simple observation.
1940 Lillian B. Pierce and Junyan Xu
Lemma 6.4 (rearrangement inequality). Let t1≤ t2≤···≤ tn be a ﬁxed nondecreasing sequence of real
numbers and a1≥···≥ an a ﬁxed nonincreasing sequence of real numbers. Then for any permutationσ
on{1,..., n}, and for any 1≤ M≤ n,
M∑
i=1
aiti≤
M∑
i=1
aitσ(i). (6-8)
This is a variant of a standard rearrangement inequality; for completeness we give a brief proof in
Section 7B. Applying this observation in (6-7) with M= n/2, we have shown that
log2
(
‖2δ‖(2r−1)Bn,r( j; 2tσ−δσ)
)
≥(2r− 1)
n/2∑
i=1
ti,
so that in the case of j= n even,
‖2δ‖−(2r−1)Bn,r( j; 2tσ−δσ)−1≤(2t1··· 2tn/2)−(2r−1)=(K1··· Kn/2)−(2r−1).
The argument is similar for j= n with n odd, and we only specify the necessary changes, starting with
log2
(
‖2δ‖(2r−1)Bn,r( j; 2tσ−δσ)
)
=(2r−1)
n∑
i=1
δσ(i)+2r
(n−1)/2∑
i=1
(tσ(i)−δσ(i))+r(tσ(( n+1)/2)−δσ(( n+1)/2)).
It is convenient to set temporarily for each i= 1,..., n the parameter2n,i= 2r if 1≤ i≤(n− 1)/2,
2n,(n+1)/2= r and2n,i= 0 if(n+1)/2< i≤ n. With this notation, the argument then proceeds as before,
until we reach the statement of (6-7), which now holds with this new deﬁnition of2n,i. Now the ﬁrst sum
on the right-hand side of (6 -7) is over 1≤ i≤(n− 1)/2, while the second sum on the right-hand side is
over i≥(n+1)/2, and has its only nonzero contribution coming fromi=(n+1)/2. We may conclude that
log2
(
‖2δ‖(2r−1)Bn,r( j; 2tσ−δσ)
)
≥
(n−1)/2∑
i=1
(2r− 1)tσ(i)+ rtσ(( n+1)/2).
We now apply (6-8) from Lemma 6.4 to conclude that
log2
(
‖2δ‖(2r−1)Bn,r( j; 2tσ−δσ)
)
≥
(n−1)/2∑
i=1
(2r− 1)ti+ rt(n+1)/2,
or equivalently,
‖2δ‖−(2r−1)Bn,r( j; 2tσ−δσ)−1≤(2t1··· 2t(n−1)/2)−(2r−1)(2t(n+1)/2)−r=(K1··· K(n−1)/2)−(2r−1)K−r
(n+1)/2.
This completes the proof of Lemma 6.3.
Burgess bounds for short character sums evaluated at forms 1941
