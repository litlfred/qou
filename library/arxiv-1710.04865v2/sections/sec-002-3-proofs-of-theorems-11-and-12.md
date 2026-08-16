---
doc_id: arxiv-1710.04865v2
doc_title: "THE COLORED JONES POL YNOMIAL AND KONTSEVICH-ZAGIER SERIES FOR DOUBLE TWIST KNOTS"
section_id: sec-002-3-proofs-of-theorems-11-and-12
section_title: "Proofs of Theorems 1.1 and 1.2"
section_number: 3
pages: 12-22
source_pdf: 1710.04865v2.pdf
source_sha256: ac8f436173d550e8
doc_brief: "THE COLORED JONES POLYNOMIAL AND KONTSEVICH-ZAGIER SERIES FOR DOUBLE TWIST KNOTS — Using a result of Takata, we prove a formula for the colored Jones polynomial of the double twist knots K(−m,−p) and"
duplicate_of: "cjdoubletwistfinal"
---
Proof of Theorem 1.1. As (1.7) reduces to (1.8) when m = 1 and this case was proven in [28],
we assume m ≥ 2. Using Lemmas 2.2 and 2.3, one can check that for l = 4mp− 1 and
t = 4mp− 2p− 1
a(n) =
2p−1∑
j=1
(−1)jnmj− 1 (3.1)
and b1(n) +b2(n) equals
1 +n2mp−1 +
p∑
j=1
(m−1∑
i=1
n2mj−2m+i−
2m−1∑
i=m
n2mj−2m+i
)
+
p∑
j=1
j∑
j′=1
m−1∑
k=1
k∑
k′=1
(n2mj−k−n2mj−k−1)(n2mj′−2m+k−k′+1−n2mj′−2m+k−k′)
−
p∑
j=1
j∑
j′=1
m∑
k=1
m−k+1∑
k′=1
(n2mj−m−k+1−n2mj−m−k)(n2mj′−2m−k′+1−n2mj′−2m−k′)
+
m−1∑
s=1
p∑
j=1
(j−1∑
j′=1
(n2mj′−s−n2mj′−2m+s) +
p∑
j′=j
(n2mj′−s−n2mj′−2m+s−1)
)
n2mj−2m+s−1
THE COLORED JONES POLYNOMIAL FOR DOUBLE TWIST KNOTS 13
+
p∑
j=1
( p∑
j′=j
(n2mj′−m−n2mj′−m−1)
)
n2mj−m−1
−
p−1∑
j=1
( p∑
j′=j+1
(n2mj′−1−n2mj′−2m) +n2mj
)
n2mj−1
−
m−1∑
s=1
p∑
j=1
( j∑
j′=1
(n2mj′−m+s−n2mj′−m−s) +
p∑
j′=j+1
(n2mj′−m+s−1−n2mj′−m−s)
)
n2mj−m+s−1.
(3.2)
Also, by (2.1) and (2.2)
X(n) = (−1)n2mp−1q−Nn 2mp−1 (q)N−1(q)n2mp−1
(q)N−n2mp−1−1
×
p∏
j=1
(−1)n2mj−1−n2mj−mq
1
2
m∑
s=1
(n2mj−2m+s−n2mj−2m+s−1)(n2mj−2m+s−n2mj−2m+s−1+1)
2m−1∏
s=1
(q)n2mj−2m+s−n2mj−2m+s−1
×
p−1∏
j=1
(−1)n2mj−n2mj−1
(q)n2mj−n2mj−1
.
(3.3)
Upon comparing (2.3) and (3.1)–(3.3) with (1.7) and then simplifying, it suﬃces to prove that
for m≥ 2
p∑
j=1
j∑
j′=1
m−1∑
k=1
k∑
k′=1
(n2mj−k−n2mj−k−1)(n2mj′−2m+k−k′+1−n2mj′−2m+k−k′)
−
p∑
j=1
j∑
j′=1
m∑
k=1
m−k+1∑
k′=1
(n2mj−m−k+1−n2mj−m−k)(n2mj′−2m−k′+1−n2mj′−2m−k′)
+
m−1∑
s=1
p∑
j=1
(j−1∑
j′=1
(n2mj′−s−n2mj′−2m+s) +
p∑
j′=j
(n2mj′−s−n2mj′−2m+s−1)
)
n2mj−2m+s−1
+
p∑
j=1
( p∑
j′=j
(n2mj′−m−n2mj′−m−1)
)
n2mj−m−1
−
p−1∑
j=1
( p∑
j′=j+1
(n2mj′−1−n2mj′−2m) +n2mj
)
n2mj−1
14 JEREMY LOVEJOY AND ROBERT OSBURN
−
m−1∑
s=1
p∑
j=1
( j∑
j′=1
(n2mj′−m+s−n2mj′−m−s) +
p∑
j′=j+1
(n2mj′−m+s−1−n2mj′−m−s)
)
n2mj−m+s−1
+
p∑
j=1
[(n2mj−2m+1 + 1
2
)
−n2mj−2m+1n2mj−2m +
(n2mj−m−1
2
)
−n2mj−mn2mj−m−1
+ 1
2
m−1∑
s=2
(n2mj−2m+s−n2mj−2m+s−1)(n2mj−2m+s−n2mj−2m+s−1 + 1)
]
(3.4)
equals
∑
1≤i<j≤2mp−1
m∤i
ϵi,j,mninj−
2mp−2∑
i=1
nini+1 (3.5)
where ϵi,j,m is given by (1.5). Here, we have used the fact that
p∑
j=1
(m−1∑
i=1
n2mj−2m+i−
2m−2∑
i=m
n2mj−2m+i
)
−
p−1∑
j=1
n2mj−1 =
2mp−2∑
i=1
γi,mni +
p−1∑
i=1
n2mi, (3.6)
where γi,m is given by (1.6), together with the identities
1
2
p∑
j=1
m∑
s=1
(n2mj−2m+s−n2mj−2m+s−1)(n2mj−2m+s−n2mj−2m+s−1 + 1)
=
p∑
j=1
(n2mj−2m
2
)
+
(n2mj−m + 1
2
)
+
p∑
j=1
[(n2mj−2m+1 + 1
2
)
−n2mj−2m+1n2mj−2m +
(n2mj−m−1
2
)
−n2mj−mn2mj−m−1
+ 1
2
m−1∑
s=2
(n2mj−2m+s−n2mj−2m+s−1)(n2mj−2m+s−n2mj−2m+s−1 + 1)
]
(3.7)
and
p∑
j=1
(n2mj−2m
2
)
+
(n2mj−m + 1
2
)
+
p−1∑
i=1
n2mi =
2p−1∑
i=1
(nmi + 1
2
)
. (3.8)
We now sketch how to proceed from (3.4) to (3.5). Let Li denote the ith line of (3.4). First,
note that
THE COLORED JONES POLYNOMIAL FOR DOUBLE TWIST KNOTS 15
L7 +L8 =
p−1∑
j=0
m−1∑
i=1
n2
2mj+i−
p−1∑
j=0
m∑
i=1
n2mj+i−1n2mj+i. (3.9)
Next, observe that both L1 and L2 simplify as the sum on k′ telescopes in each case. Thus,
L1 =
m−1∑
k=1
p∑
j=1
j∑
j′=1
(n2mj−k−n2mj−k−1)(n2mj′−2m+k−n2mj′−2m) (3.10)
L2 =−
m∑
k=1
p∑
j=1
j∑
j′=1
(n2mj−m−k+1−n2mj−m−k)(n2mj′−2m−n2mj′−3m+k−1). (3.11)
Now, splittingL1 into two sums according to the second factor and then using the fact that the
resulting second sum telescopes gives
L1 =
m−1∑
k=1
p∑
j=1
j∑
j′=1
(n2mj−k−n2mj−k−1)n2mj′−2m+k +
p∑
j=1
j∑
j′=1
(n2mj−m−n2mj−1)n2mj′−2m
=
m−1∑
k=1
p∑
j=1
j∑
j′=1
n2mj−kn2mj′−2m+k−
m−1∑
k=1
p∑
j=1
j∑
j′=1
n2mj−k−1n2mj′−2m+k
+
p∑
j=1
j∑
j′=1
n2mj−mn2mj′−2m−
p∑
j=1
j∑
j′=1
n2mj−1n2mj′−2m. (3.12)
A similar simpliﬁcation for (3.11) yields
L2 =−
p∑
j=1
j∑
j′=1
(n2mj−m−n2mj−2m)n2mj′−2m
+
m∑
k=1
p∑
j=1
j∑
j′=1
(n2mj−m−k+1−n2mj−m−k)n2mj′−3m+k−1
=−
p∑
j=1
j∑
j′=1
n2mj−mn2mj′−2m +
p∑
j=1
j∑
j′=1
n2mj−2mn2mj′−2m
+
m∑
k=1
p∑
j=1
j∑
j′=1
n2mj−m−k+1n2mj′−3m+k−1−
m∑
k=1
p∑
j=1
j∑
j′=1
n2mj−m−kn2mj′−3m+k−1. (3.13)
Observe that the third sum in (3.12) cancels with the ﬁrst sum in (3.13). Also, if we take s = 1
in the second triple sum of L3,
m−1∑
s=1
p∑
j=1
p∑
j′=j
(n2mj′−s−n2mj′−2m+s−1)n2mj−2m+s−1,
16 JEREMY LOVEJOY AND ROBERT OSBURN
then this cancels with the fourth sum of (3.12) and the second sum of (3.13). Putting all of this
together and expanding sums we have that (3.4) equals
m−1∑
k=1
p∑
j=1
j∑
j′=1
n2mj−kn2mj′−2m+k−
m−1∑
k=1
p∑
j=1
j∑
j′=1
n2mj−k−1n2mj′−2m+k
+
m∑
k=1
p∑
j=1
j∑
j′=1
n2mj−m−k+1n2mj′−3m+k−1−
m∑
k=1
p∑
j=1
j∑
j′=1
n2mj−m−kn2mj′−3m+k−1
+
m−1∑
s=1
p∑
j=1
j−1∑
j′=1
n2mj′−sn2mj−2m+s−1−
m−1∑
s=1
p∑
j=1
j−1∑
j′=1
n2mj′−2m+sn2mj−2m+s−1
+
m−1∑
s=2
p∑
j=1
p∑
j′=j
n2mj′−sn2mj−2m+s−1−
m−1∑
s=2
p∑
j=1
p∑
j′=j
n2mj′−2m+s−1n2mj−2m+s−1
+
p∑
j=1
p∑
j′=j
n2mj′−mn2mj−m−1−
p∑
j=1
p∑
j′=j
n2mj′−m−1n2mj−m−1
−
p−1∑
j=1
p∑
j′=j+1
n2mj′−1n2mj−1 +
p−1∑
j=1
p∑
j′=j+1
n2mj′−2mn2mj−1−
p−1∑
j=1
n2mjn2mj−1
−
m−1∑
s=1
p∑
j=1
j∑
j′=1
n2mj′−m+sn2mj−m+s−1 +
m−1∑
s=1
p∑
j=1
j∑
j′=1
n2mj′−m−sn2mj−m+s−1
−
m−1∑
s=1
p∑
j=1
p∑
j′=j+1
n2mj′−m+s−1n2mj−m+s−1 +
m−1∑
s=1
p∑
j=1
p∑
j′=j+1
n2mj′−m−sn2mj−m+s−1
+
p−1∑
j=0
m−1∑
i=1
n2
2mj+i−
p−1∑
j=0
m∑
i=1
n2mj+i−1n2mj+i.
(3.14)
The second sum on the ﬁfth line of (3.14) can now be taken into the second sum of the fourth
line, increasing the upper limit of summation there to m. In this sum, we can then exchange j
and j′ and reindex, giving
−
m∑
s=2
p∑
j=1
j∑
j′=1
n2mj−2m+s−1n2mj′−2m+s−1.
Now take out the term j′ =j and shift the indices in this term by j→j + 1 and s→s + 1 to
cancel with the ﬁrst sum on the last line of (3.14). Finally, in the second line of (3.14), perform
the shift j′→j′ + 1 and start the sum at j′ = 1 (as j′ = 0 gives 0) to obtain
m∑
k=1
p∑
j=1
j−1∑
j′=1
n2mj−m−k+1n2mj′−m+k−1−
m∑
k=1
p∑
j=1
j−1∑
j′=1
n2mj−m−kn2mj′−m+k−1. (3.15)
THE COLORED JONES POLYNOMIAL FOR DOUBLE TWIST KNOTS 17
We now remove the k = m term from the second sum in (3.15) and note that what remains
cancels with the second sum in the penultimate line of (3.14). In total, this yields that (3.4)
equals
m−1∑
k=1
p∑
j=1
j∑
j′=1
n2mj−kn2mj′−2m+k−
m−1∑
k=1
p∑
j=1
j∑
j′=1
n2mj−k−1n2mj′−2m+k
+
m∑
k=1
p∑
j=1
j−1∑
j′=1
n2mj−m−k+1n2mj′−m+k−1−
p∑
j=1
j−1∑
j′=1
n2mj−2mn2mj′−1
+
m−1∑
s=1
p∑
j=1
j−1∑
j′=1
n2mj′−sn2mj−2m+s−1−
m−1∑
s=1
p∑
j=1
j−1∑
j′=1
n2mj′−2m+sn2mj−2m+s−1
+
m−1∑
s=2
p∑
j=1
p∑
j′=j
n2mj′−sn2mj−2m+s−1−
m∑
s=2
p∑
j=1
j−1∑
j′=1
n2mj−2m+s−1n2mj′−2m+s−1
+
p∑
j=1
p∑
j′=j
n2mj′−mn2mj−m−1
−
p−1∑
j=1
p∑
j′=j+1
n2mj′−1n2mj−1 +
p−1∑
j=1
p∑
j′=j+1
n2mj′−2mn2mj−1−
p−1∑
j=1
n2mjn2mj−1
−
m−1∑
s=1
p∑
j=1
j∑
j′=1
n2mj′−m+sn2mj−m+s−1 +
m−1∑
s=1
p∑
j=1
j∑
j′=1
n2mj′−m−sn2mj−m+s−1
−
m−1∑
s=1
p∑
j=1
p∑
j′=j+1
n2mj′−m+s−1n2mj−m+s−1
−
p−1∑
j=0
m∑
i=1
n2mj+i−1n2mj+i.
(3.16)
We now simplify further. The k = 1 term of the ﬁrst sum in the second line cancels with the
s = 1 term of the sum in the penultimate line. The ﬁrst sum on the fourth line cancels with
the second sum of the ﬁrst line once we remove the k =m− 1 term. This k =m− 1 term then
cancels with the ﬁfth line. The ﬁrst sum in the sixth line is the s =m term of the sum in the
penultimate line. The second sum in the sixth line cancels with the second sum in the second
line. The last sum in the sixth line is the i = 0 term in the last line. Finally, we remove the
j′ =j term from the ﬁrst sum in the seventh line and write it in the last line. Thus, (3.4) equals
m−1∑
k=1
p∑
j=1
j∑
j′=1
n2mj′−2m+kn2mj−k +
m∑
k=2
p∑
j=1
j−1∑
j′=1
n2mj′−m+k−1n2mj−m−k+1
18 JEREMY LOVEJOY AND ROBERT OSBURN
+
m−1∑
s=1
p∑
j=1
j−1∑
j′=1
n2mj′−sn2mj−2m+s−1 +
m−1∑
s=1
p∑
j=1
j∑
j′=1
n2mj′−m−sn2mj−m+s−1
−
m−1∑
s=1
p∑
j=1
j−1∑
j′=1
n2mj′−2m+sn2mj−2m+s−1−
m−1∑
s=1
p∑
j=1
j−1∑
j′=1
n2mj′−m+sn2mj−m+s−1
−
m∑
s=2
p∑
j′=1
j−1∑
j′=1
n2mj′−2m+s−1n2mj−2m+s−1−
m∑
s=2
p−1∑
j=1
p∑
j′=j+1
n2mj−m+s−1n2mj′−m+s−1
−
m−1∑
s=1
p∑
j=1
n2mj−m+sn2mj−m+s−1−
p−1∑
j=0
m∑
i=0
n2mj+i−1n2mj+i.
(3.17)
Now we see that this is equal to (3.5) as follows. The ﬁrst four lines of (3.17) correspond to the
ﬁrst term in (3.5); namely, the ﬁrst line of (3.17) corresponds to ( i,j )≡ (i,−i) mod 2 m, the
second line to (i,j )≡ (i,−i− 1) mod 2 m, the third line to ( i,j )≡ (i,i− 1) mod 2 m and the
fourth line to (i,j )≡ (i,i ) mod 2 m. Finally, the ﬁfth line of (3.17) matches the second sum of
(3.5). Thus, we have proven that (3.4) equals (3.5).
□
Proof of Theorem 1.2. As (1.12) reduces to (1.13) when m = 1 and this case was proven in
[28], we assume m≥ 2. Using Lemmas 2.4 and 2.5, one can check that for l = 4mp + 1 and
t = 4mp− 2p + 1
a(n) =−
2p−1∑
j=1
(−1)jnmj (3.18)
and b1(n) +b2(n) equals
p∑
j=1
[m−1∑
i=0
n2mj−2m+i−
2m−1∑
i=m+1
n2mj−2m+i
]
+
m∑
k=1
p∑
j=1
j∑
j′=1
(n2mj−k+1−n2mj−k)(n2mj′−2m+k−n2mj′−2m)
−
m−1∑
s=1
p∑
j=2
j∑
j′=2
(n2mj−m−s+1−n2mj−m−s)(n2mj′−2m−n2mj′−3m+s)
+
p∑
j=1
( p∑
j′=j
(n2mj′−n2mj′−2m+1) +n2mj−2m+1
)
n2mj−2m
+
m−1∑
s=1
p∑
j=1
( j∑
j′=1
(n2mj′−s−n2mj′−2m+s) +
p∑
j′=j+1
(n2mj′−s−n2mj′−2m+s+1)
)
n2mj−2m+s
THE COLORED JONES POLYNOMIAL FOR DOUBLE TWIST KNOTS 19
−
p∑
j=1
( p∑
j′=j
(n2mj′−m+1−n2mj′−m)
)
n2mj−m
−
m−1∑
s=1
p∑
j=1
(j−1∑
j′=1
(n2mj′−m+s−n2mj′−m−s) +
p∑
j′=j
(n2mj′−m+s+1−n2mj′−m−s)
)
n2mj−m+s.
(3.19)
Also, by (2.1) and (2.2)
X(n) = (−1)n2mpq−Nn 2mp (q)N−1(q)n2mp
(q)N−n2mp−1
×
p∏
j=1
(−1)n2mj−n2mj−mq
1
2
m∑
s=1
(n2mj−2m+s−n2mj−2m+s−1)(n2mj−2m+s−n2mj−2m+s−1+1)
2m∏
s=1
(q)n2mj−2m+s−n2mj−2m+s−1
.
(3.20)
Upon comparing (2.3) and (3.18)–(3.20) with (1.12) and then simplifying, it suﬃces to prove
that for m≥ 2
m∑
k=1
p∑
j=1
j∑
j′=1
(n2mj−k+1−n2mj−k)(n2mj′−2m+k−n2mj′−2m)
−
m−1∑
s=1
p∑
j=2
j∑
j′=2
(n2mj−m−s+1−n2mj−m−s)(n2mj′−2m−n2mj′−3m+s)
+
p∑
j=1
p∑
j′=j
(n2mj′−n2mj′−2m+1)n2mj−2m +
p∑
j=1
n2mj−2m+1n2mj−2m
+
m−1∑
s=1
p∑
j=1
( j∑
j′=1
(n2mj′−s−n2mj′−2m+s) +
p∑
j′=j+1
(n2mj′−s−n2mj′−2m+s+1)
)
n2mj−2m+s
−
p∑
j=1
( p∑
j′=j
(n2mj′−m+1−n2mj′−m)
)
n2mj−m
−
m−1∑
s=1
p∑
j=1
(j−1∑
j′=1
(n2mj′−m+s−n2mj′−m−s) +
p∑
j′=j
(n2mj′−m+s+1−n2mj′−m−s)
)
n2mj−m+s
+
p∑
j=1
[(n2mj−2m+1 + 1
2
)
−n2mj−2m+1n2mj−2m +
(n2mj−m−1
2
)
−n2mj−mn2mj−m−1
20 JEREMY LOVEJOY AND ROBERT OSBURN
+ 1
2
m−1∑
s=2
(n2mj−2m+s−n2mj−2m+s−1)(n2mj−2m+s−n2mj−2m+s−1 + 1)
]
(3.21)
equals
∑
1≤i<j≤2mp
m∤i
∆i,j,mninj (3.22)
where ∆i,j,m is given by (1.10). Here, we have used (3.7), (3.8) and the fact that
p∑
j=1
[m−1∑
i=0
n2mj−2m+i−
2m−1∑
i=m+1
n2mj−2m+i
]
=
2mp−1∑
i=1
βi,mni +
p−1∑
i=1
n2mi (3.23)
where βi,m is given by (1.11).
We now sketch how to go from (3.21) to (3.22). Let ˆLi denote the ith line of (3.21). We ﬁrst
split ˆL1 into two parts according to the second factor and note that the sum on k in the second
part telescopes. Thus,
ˆL1 =
m∑
k=1
p∑
j=1
j∑
j′=1
(n2mj−k+1−n2mj−k)n2mj′−2m+k +
p∑
j=1
j∑
j′=1
(n2mj−m−n2mj)n2mj′−2m. (3.24)
Similarly, we split ˆL2 into two parts according to the second factor and note that the sum on s
in the ﬁrst part telescopes. Thus,
ˆL2 =−
p∑
j=1
j∑
j′=1
(n2mj−m−n2mj−2m+1)n2mj′−2m
+
m−1∑
s=1
p∑
j=2
j∑
j′=2
(n2mj−m−s+1−n2mj−m−s)n2mj−3m+s.
(3.25)
Here, we have used the fact thatn0 := 0. Now, the k =m term of the ﬁrst sum in (3.24) cancels
with ˆL5. If we combine the double sum of (3.24) with the double sum in ˆL3, then the resulting
sum cancels with the ﬁrst sum in (3.25). Note that ˆLi =Li for i = 7 and 8. Hence, the single
sum in ˆL3 cancels with the i = 1 term of the second sum in (3.9). Putting this together and
expanding sums we now have that (3.21) equals
THE COLORED JONES POLYNOMIAL FOR DOUBLE TWIST KNOTS 21
m−1∑
k=1
p∑
j=1
j∑
j′=1
n2mj−k+1n2mj′−2m+k−
m−1∑
k=1
p∑
j=1
j∑
j′=1
n2mj−kn2mj′−2m+k
+
m−1∑
s=1
p∑
j=2
j∑
j′=2
n2mj−m−s+1n2mj′−3m+s−
m−1∑
s=1
p∑
j=2
j∑
j′=2
n2mj−m−sn2mj′−3m+s
+
m−1∑
s=1
p∑
j=1
j∑
j′=1
n2mj′−sn2mj−2m+s−
m−1∑
s=1
p∑
j=1
j∑
j′=1
n2mj′−2m+sn2mj−2m+s
+
m−1∑
s=1
p∑
j=1
p∑
j′=j+1
n2mj′−sn2mj−2m+s−
m−1∑
s=1
p∑
j=1
p∑
j′=j+1
n2mj′−2m+s+1n2mj−2m+s
−
m−1∑
s=1
p∑
j=1
j−1∑
j′=1
n2mj′−m+sn2mj−m+s +
m−1∑
s=1
p∑
j=1
j−1∑
j′=1
n2mj′−m−sn2mj−m+s
−
m−1∑
s=1
p∑
j=1
p∑
j′=j
n2mj′−m+s+1n2mj−m+s +
m−1∑
s=1
p∑
j=1
p∑
j′=j
n2mj′−m−sn2mj−m+s
+
p−1∑
j=0
m−1∑
i=1
n2
2mj+i−
p−1∑
j=0
m∑
i=2
n2mj+i−1n2mj+i.
(3.26)
We combine the j′ =j term from the ﬁrst sum of the third line in (3.26) with the ﬁrst sum
on the fourth line, and then cancel this with the second sum in the ﬁrst line. Next, the j′ =j
term in the second sum of the third line cancels with the ﬁrst sum in the last line. Thus, (3.21)
equals
m−1∑
k=1
p∑
j=1
j∑
j′=1
n2mj−k+1n2mj′−2m+k
+
m−1∑
s=1
p∑
j=2
j∑
j′=2
n2mj−m−s+1n2mj′−3m+s−
m−1∑
s=1
p∑
j=2
j∑
j′=2
n2mj−m−sn2mj′−3m+s
+
m−1∑
s=1
p∑
j=1
j−1∑
j′=1
n2mj′−sn2mj−2m+s−
m−1∑
s=1
p∑
j=1
j−1∑
j′=1
n2mj′−2m+sn2mj−2m+s
−
m−1∑
s=1
p∑
j=1
p∑
j′=j+1
n2mj′−2m+s+1n2mj−2m+s
−
m−1∑
s=1
p∑
j=1
j−1∑
j′=1
n2mj′−m+sn2mj−m+s +
m−1∑
s=1
p∑
j=1
j−1∑
j′=1
n2mj′−m−sn2mj−m+s
22 JEREMY LOVEJOY AND ROBERT OSBURN
−
m−1∑
s=1
p∑
j=1
p∑
j′=j
n2mj′−m+s+1n2mj−m+s +
m−1∑
s=1
p∑
j=1
p∑
j′=j
n2mj′−m−sn2mj−m+s
−
p−1∑
j=0
m∑
i=2
n2mj+i−1n2mj+i.
(3.27)
Now, the last line of (3.27) is just the j′ = j term of the fourth line. In the second line,
perform the shift j′→ j′ + 1 and start the sum at j = 1. The second sum on this line then
cancels with the second sum of penultimate line, except for the j′ =j term. But this term now
becomes the j′ = j term for the second sum in the ﬁfth line. After simplifying and gathering
terms, we have
m−1∑
k=1
p∑
j=1
j∑
j′=1
n2mj′−2m+kn2mj−k+1 +
m−1∑
s=1
p∑
j=1
j−1∑
j′=1
n2mj′−m+sn2mj−m−s+1
+
m−1∑
s=1
p∑
j=1
j−1∑
j′=1
n2mj′−sn2mj−2m+s +
m−1∑
s=1
p∑
j=1
j∑
j′=1
n2mj′−m−sn2mj−m+s
−
m−1∑
s=1
p∑
j=1
j−1∑
j′=1
n2mj′−2m+sn2mj−2m+s−
m−1∑
s=1
p∑
j=1
j−1∑
j′=1
n2mj′−m+sn2mj−m+s
−
m−1∑
s=1
p∑
j=1
j∑
j′=1
n2mj′−2m+sn2mj−2m+s+1−
m−1∑
s=1
p∑
j=1
j∑
j′=1
n2mj′−m+sn2mj−m+s+1.
(3.28)
Now we see that this is equal to (3.22) as follows. Namely, the ﬁrst line of (3.28) corresponds
to (i,j )≡ (i,−i + 1) mod 2 m, the second line to ( i,j )≡ (i,−i) mod 2 m, the third line to
(i,j )≡ (i,i ) mod 2m and the fourth line to (i,j )≡ (i,i + 1) mod 2m. This completes the proof
that (3.21) is equal to (3.22). □
