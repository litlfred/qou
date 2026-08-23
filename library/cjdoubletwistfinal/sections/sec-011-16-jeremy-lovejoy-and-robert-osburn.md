---
doc_id: cjdoubletwistfinal
doc_title: "THE COLORED JONES POL YNOMIAL AND KONTSEVICH-ZAGIER SERIES FOR DOUBLE TWIST KNOTS"
section_id: sec-011-16-jeremy-lovejoy-and-robert-osburn
section_title: "JEREMY LOVEJOY AND ROBERT OSBURN"
section_number: 16
pages: 16-18
source_pdf: cJdoubletwistfinal.pdf
source_sha256: a1e18db5232b39f4
doc_brief: "THE COLORED JONES POLYNOMIAL AND KONTSEVICH-ZAGIER SERIES FOR DOUBLE TWIST KNOTS — Using a result of Takata, we prove a formula for the colored Jones polynomial of the double twist knots K(−m,−p) and"
---
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
