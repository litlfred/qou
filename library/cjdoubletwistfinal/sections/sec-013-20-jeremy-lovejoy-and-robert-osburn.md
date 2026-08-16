---
doc_id: cjdoubletwistfinal
doc_title: "THE COLORED JONES POL YNOMIAL AND KONTSEVICH-ZAGIER SERIES FOR DOUBLE TWIST KNOTS"
section_id: sec-013-20-jeremy-lovejoy-and-robert-osburn
section_title: "JEREMY LOVEJOY AND ROBERT OSBURN"
section_number: 20
pages: 20-22
source_pdf: cJdoubletwistfinal.pdf
source_sha256: a1e18db5232b39f4
doc_brief: "THE COLORED JONES POLYNOMIAL AND KONTSEVICH-ZAGIER SERIES FOR DOUBLE TWIST KNOTS — Using a result of Takata, we prove a formula for the colored Jones polynomial of the double twist knots K(−m,−p) and"
---
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
