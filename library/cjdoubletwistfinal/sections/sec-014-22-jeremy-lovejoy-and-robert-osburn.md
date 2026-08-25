---
doc_id: cjdoubletwistfinal
doc_title: "THE COLORED JONES POL YNOMIAL AND KONTSEVICH-ZAGIER SERIES FOR DOUBLE TWIST KNOTS"
section_id: sec-014-22-jeremy-lovejoy-and-robert-osburn
section_title: "JEREMY LOVEJOY AND ROBERT OSBURN"
section_number: 22
pages: 22-22
source_pdf: cJdoubletwistfinal.pdf
source_sha256: a1e18db5232b39f4
doc_brief: "THE COLORED JONES POLYNOMIAL AND KONTSEVICH-ZAGIER SERIES FOR DOUBLE TWIST KNOTS — Using a result of Takata, we prove a formula for the colored Jones polynomial of the double twist knots K(−m,−p) and"
---
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
