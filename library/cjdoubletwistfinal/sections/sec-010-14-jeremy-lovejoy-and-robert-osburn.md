---
doc_id: cjdoubletwistfinal
doc_title: "THE COLORED JONES POL YNOMIAL AND KONTSEVICH-ZAGIER SERIES FOR DOUBLE TWIST KNOTS"
section_id: sec-010-14-jeremy-lovejoy-and-robert-osburn
section_title: "JEREMY LOVEJOY AND ROBERT OSBURN"
section_number: 14
pages: 14-16
source_pdf: cJdoubletwistfinal.pdf
source_sha256: a1e18db5232b39f4
doc_brief: "THE COLORED JONES POLYNOMIAL AND KONTSEVICH-ZAGIER SERIES FOR DOUBLE TWIST KNOTS — Using a result of Takata, we prove a formula for the colored Jones polynomial of the double twist knots K(−m,−p) and"
---
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
