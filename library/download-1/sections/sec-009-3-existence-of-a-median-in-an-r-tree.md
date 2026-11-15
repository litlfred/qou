---
doc_id: download-1
doc_title: "Central and L p -concentration of 1-Lipschitz maps into R -trees"
section_id: sec-009-3-existence-of-a-median-in-an-r-tree
section_title: "Existence of a median in an R-tree."
section_number: 3
pages: 11-13
source_pdf: Download (1).pdf
source_sha256: bbb001c909958e8a
toc_source: inferred
doc_brief: "Central and L p -concentration of 1-Lipschitz maps into R -trees — In this paper, we study the Le´vy-Milman concentration phenomenon of 1-Lipschitz maps from mm-spaces to R-trees."
---
Existence of a median in an R-tree.
Let T be an R-tree and  a ﬁnite Borel measure on T with m :¼ ðTÞ < þ1.
A median of  is a point z 2 T such that there exist two subtrees T 0, T 00  T such
that T ¼ T 0 [ T 00, T 0 \ T 00 ¼ fzg, ðT 0Þ  m=3, and ðT 00Þ  m=3.
EXAMPLE 3.1.
For i ¼ 1; 2; 3, let Ti :¼ fði; rÞ j r 2 ½0; þ1Þg be three copies
of ½0; þ1Þ equipped with the usual Euclidean distance function. The tripod T is
the metric space obtained by gluing together all these spaces Ti, i ¼ 1; 2; 3, at their
origins with the intrinsic distance function. We consider the Borel probability
measure  deﬁned by ðfði; 1ÞgÞ :¼ 1=3 for all i ¼ 1; 2; 3. We easily see that the
origin of T is a median of the measure . We note that there is no point in T
separating T into two subtrees with measures greater than 1/3.
The existence of a median of a ﬁnite Borel measure on a simplicial tree is
proved in [3, Proposition 5.2]. The purpose of this section is to prove the existence
of a median of a ﬁnite Borel measure on an R-tree, which is needed for the proofs
of our main theorems. Although the proof of the existence is similar to the proof
for the case of a simplicial tree, we give it for completeness:
PROPOSITION 3.2.
Every ﬁnite Borel measure on an R-tree has a median.
PROOF.
Let  be a ﬁnite Borel measure on an R-tree with m :¼ ðTÞ.
Assume that a point z 2 T satisﬁes that ðT 0Þ < m=3 for any T 0 2 C0
TðzÞ, then it is
easy to check that z is a median of . So, we assume that for any z 2 T there exists
TðzÞ 2 C 0
TðzÞ
such
that
ðTðzÞÞ  m=3.
If
for
some
z 2 T,
there
exists
T 0 2 C 0
TðzÞ n fTðzÞg such that ðT 0Þ  m=3, then this z is a median of . Thereby,
we also assume that ðT 0Þ < m=3 for any z 2 T and T 0 2 C 0
TðzÞ n fTðzÞg.
Fixing a point z0 2 T, we assume that there exists z 2 Tðz0Þ n fz0g such that
Central and Lp-concentration of 1-Lipschitz maps into R-trees
493
z0 2 TðzÞ. Put
t0 :¼ infft 2 ð0; dTðz0; zÞ j z0 2 Tðz0;zðtÞÞg:
CLAIM 3.3.
z0;zðt0Þ is a median of .
PROOF.
Assume ﬁrst that t0 ¼ 0. Then, taking a monotone decreasing
sequence ftng1
n¼1  ð0; dTðz0; zÞ such that tn ! 0 as n ! 1 and z0 2 Tðz0;zðtnÞÞ
for any n 2 N, we shall show that T1
n¼1 Tðz0;zðtnÞÞ  ðT n Tðz0ÞÞ [ fz0g. If it is,
we conclude that the point z0 ¼ z0;zð0Þ is a median of  as follows: From the
uniqueness of Tðz0;zðtnÞÞ, we have Tðz0;zðtnþ1ÞÞ  Tðz0;zðtnÞÞ for each n 2 N.
Thus, we get ðT1
n¼1 Tðz0;zðtnÞÞÞ ¼ limn!1 ðTðz0;zðtnÞÞÞ  m=3.
Suppose that there exists w 2 ðTðz0Þ n fz0gÞ \ T1
n¼1 Tðz0;zðtnÞÞ. Note that
ðz0; zT \ ðz0; wT 6¼ ;. Actually, if ðz0; zT \ ðz0; wT ¼ ;, then it follows from the
property (2) of R-trees that ½z; wT ¼ ½z0; zT [ ½z0; wT. Especially, we have
z0 2 ½z; wT. Since Tðz0Þ n fz0g is convex by virtue of Lemma 2.8, ½z; wT does not
contain the point z0. This is a contradiction. Thus, there exists t 2 ð0; dTðz0; zÞ
such
that
z0;zðtÞ 2 ðz0; zT \ ðz0; wT.
We
pick
n0 2 N
with
tn0 < t.
Since
w 2 ðTðz0Þ n fz0gÞ \ T1
n¼1 Tðz0;zðtnÞÞ  Tðz0;zðtn0ÞÞ n fz0g, we get z0;zðtÞ 2 ðz0;
wT  Tðz0;zðtn0ÞÞ n fz0g. Thereby, we get z0;zðtÞ 2 Tðz0;zðtn0ÞÞ n fz0;zðtn0Þg.
Therefore, since z0 2 Tðz0;zðtn0ÞÞ n fz0;zðtn0Þg and Tðz0;zðtn0ÞÞ n fz0;zðtn0Þg is
convex, we obtain
z0;zðtn0Þ 2 ½z0; z0;zðtÞT  Tðz0;zðtn0ÞÞ n fz0;zðtn0Þg:
This is a contradiction. Therefore, we have T1
n¼1 Tðz0;zðtnÞÞ  ðT n Tðz0ÞÞ [ fz0g.
We consider the other case that t0 > 0. Take a monotone increasing sequence
ftng1
n¼1  ð0; þ1Þ such that tn ! t0 as n ! 1 and z0 =2 Tðz0;zðtnÞÞ for each
n 2 N.
Then,
the
same
proof
in
the
case
of
t0 ¼ 0
implies
that
ðT1
n¼1 Tðz0;zðtnÞÞÞ  m=3 and T1
n¼1 Tðz0;zðtnÞÞ  ðT n Tðz0;zðt0ÞÞÞ [ fz0;zðt0Þg.
Therefore, z0;zðt0Þ is a median of . This completes the proof of the claim.

We next assume that z0 =2 TðzÞ for any z 2 Tðz0Þ. We denote by  the set of
all unit speed geodesics  : ½0; LðÞ ! Tðz0Þ such that ð0Þ ¼ z0 and ð½t; LðÞÞ 
TððtÞÞ for any t 2 ½0; LðÞ. Because of the assumption, we easily see
CLAIM 3.4.
For any z 2 Tðz0Þ, we have z0;z 2 .
CLAIM 3.5.
For any ; 0 2  with LðÞ  Lð0Þ, we have
½ð0Þ; ðLðÞÞT  ½0ð0Þ; 0ðLð0ÞÞT:
494
K. FUNANO
PROOF.
Suppose that
t0 :¼ supft 2 ½0; LðÞ j ½ð0Þ; ðtÞT  ½0ð0Þ; 0ðLð0ÞÞTg < LðÞ:
Then, we have ðtÞ =2 ½0ð0Þ; 0ðLð0ÞÞT
for any t > t0. Actually, if ðtÞ 2
½0ð0Þ; 0ðLð0ÞÞT, then we have ðtÞ ¼ 0ðtÞ. Thus, ½ðt0Þ; ðtÞT ¼ ½0ðt0Þ; 0ðtÞT
by the property ð2Þ of R-trees. Thereby, we get ½ð0Þ; ðtÞT  ½0ð0Þ; 0ðLð0ÞÞT.
Since t > t0, this contradicts the deﬁnition of t0. Therefore, from the property (2)
of R-trees, we have
½ðLðÞÞ; 0ðLð0ÞÞT ¼ ½ðt0Þ; ðLðÞÞT [ ½0ðt0Þ; 0ðLð0ÞÞT:
ð3:1Þ
Since ; 0 2 , we have ðLðÞÞ; 0ðLð0ÞÞ 2 Tððt0ÞÞ n fðt0Þg. So, from the
convexity of Tððt0ÞÞ n fðt0Þg, we get ½ðLðÞÞ; 0ðLð0ÞÞT  Tððt0ÞÞ n fðt0Þg.
This is a contradiction, because ðt0Þ 2 ½ðLðÞÞ; 0ðLð0ÞÞT
by (3.1). This
completes the proof of the claim.

Putting 	 :¼ supfLðÞ j  2 g, we shall show that 	 < þ1. If 	 < þ1, we
ﬁnish the proof of the proposition as follows: By the completeness of R-trees and
Claim 3.5, there exists unique  2  with LðÞ ¼ 	. We also note that 	 > 0 by
Claim 3.4. Thus, there exists a monotone increasing sequence ftng1
n¼1 of positive
numbers such that tn ! 	 as n ! 1. We easily see that Tððtnþ1ÞÞ  TððtnÞÞ for
any n 2 N and T1
n¼1 TððtnÞÞ ¼ fðLðÞÞg. Since ðTððtnÞÞÞ  m=3, the point
ðLðÞÞ is a median of .
Suppose that 	 ¼ þ1. Then, taking a sequence fng1
n¼1   such that
LðnÞ < Lðnþ1Þ
for
any
n 2 N
and
LðnÞ ! þ1
as
n ! 1,
we
obtain
T1
n¼1 TðnðLðnÞÞÞ ¼ ;. Since Tðnþ1ðLðnþ1ÞÞÞ  TðnðLðnÞÞÞ for any n 2 N,
we have
0 ¼ 
\
1
n¼1
TðnðLðnÞÞÞ
 
!
¼ lim
n!1 ðTðnðLðnÞÞÞÞ  m
3 ;
which is a contradiction. This completes the proof of the proposition.

