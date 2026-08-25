---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-140-6d-application-of-the-nonmaximal-upper-bound
section_title: "6D. Application of the nonmaximal upper bound"
section_number: null
pages: 271-272
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
sums over m. Fixδ (with 0≤δi≤ ti for each i). Notice that we may not havet1−δ1≤ t2−δ2≤···≤ tn−δn
even though t1≤ t2≤···≤ tn, so we may need to reorder t−δ before applying Lemma 6.1. Let σ be a
permutation of{1, 2,..., n} (depending onδ) such that
tσ( 1)−δσ( 1)≤ tσ( 2)−δσ( 2)≤···≤ tσ( n)−δσ( n). (6-5)
Given an n-tuple x, let xσ=(xσ( 1), xσ( 2),..., xσ( n)), and 2tσ−δσ=(2tσ( 1)−δσ( 1),..., 2tσ( n)−δσ( n)). Recall
the discussion on permutations of variables in Section 3D; for any permutation π of{1,..., n} deﬁne the
form Fπ(X) by setting Fπ(X1,..., Xn)= F(Xπ(1),..., Xπ(n)).
Lettingσ−1 be the permutation inverse ofσ , then
S(F; m, 2t−δ)=
∑
x∈(m,m+2t−δ)
χ( F(x))=
∑
xσ∈(mσ,mσ+2tσ−δσ)
χ( Fσ−1(xσ))= S(Fσ−1; mσ, 2tσ−δσ).
Note that mσ ranges over all n-tuples with coordinates modulo q as m does, and that the last argument in
S(Fσ−1; mσ, 2tσ−δσ) satisﬁes the requirement (6-5) so that we may apply Lemma 6.1 withn, r, D,1, q,χ
as before but now to the form Fσ−1; here we use the uniformity of Lemma 6.1 with respect to the form.
(We recall from Lemma 3.5 that the reduction modulo q of Fσ−1 is(1, q)-admissible if and only if F is.)
1938 Lillian B. Pierce and Junyan Xu
We may conclude (using the fact that‖2tσ−δσ‖=‖ 2t−δ‖=‖ 2t‖·‖ 2δ‖−1) that
∑
m
|mi|≤2q
max
k≤K
|S(F; m, k)|2r≪n,r,D,1 T 2r−1 ∑
δ
0≤δi≤ti
‖2δ‖‖2tσ−δσ‖2r
n∑
j=0
q(n+ j)/2Bn,r( j; 2tσ−δσ)−1
= T 2r−1 ∑
δ
0≤δi≤ti
‖2t‖2r‖2δ‖−(2r−1)
n∑
j=0
q(n+ j)/2Bn,r( j; 2tσ−δσ)−1
= T 2r−1‖2t‖2r
n∑
j=0
q(n+ j)/2 ∑
δ
0≤δi≤ti
‖2δ‖−(2r−1)Bn,r( j; 2tσ−δσ)−1
≤ T 2r‖K‖2r
n∑
j=0
q(n+ j)/2 max
δ
0≤δi≤ti
{
‖2δ‖−(2r−1)Bn,r( j; 2tσ−δσ)−1}
. (6-6)
Here we recall that‖2t‖=‖ K‖. Note that in the case of dimension n= 1 (andθ1= r), the sum over j is
comprised of the two terms
qn/22−δ(2r−1)+ qn2−δ(2r−1)(2t−δ)−r≤ qn/2+ qn2−rt= qn/2+ qn K−r,
familiar from the classical 1-dimensional Burgess argument.
Now in general for n≥ 2 we must reinterpret Bn,r( j; 2tσ−δσ)−1 in terms of the coordinates of K= 2t,
in which we recall that t1≤ t2≤···≤ tn; this argument is more complicated, and in particular for j= n
we will get a positive power of 2δ we cannot ignore as in the case of n= 1 (e.g., compare to the top line
of [Heath-Brown 2013, p. 204]). We summarize the necessary result:
Lemma 6.3. For K= 2t with t1≤···≤ tn, for eachδ≤ t, letσ be a permutation of the indices{1,..., n}
such that tσ( 1)−δσ( 1)≤···≤ tσ( n)−δσ( n). Then
‖2δ‖−(2r−1)Bn,r( j; 2tσ−δσ)−1≤



1 if j= 0,
K
−θ j
1 if j= 1,..., n− 1,
(K1··· Kn/2)−(2r−1) if j= n, n even,
(K1··· K(n−1)/2)−(2r−1)K−r
(n+1)/2 if j= n, n odd.
Once we apply this lemma to (6 -6), upon noting that T 2r≤ 22nr(log2 Kn)2nr≪(log Kn)2nr, we have
proved Proposition 6.2.
