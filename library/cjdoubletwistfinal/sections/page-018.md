---
doc_id: cjdoubletwistfinal
doc_title: "THE COLORED JONES POLYNOMIAL AND KONTSEVICH-ZAGIER SERIES FOR DOUBLE TWIST KNOTS"
section_id: page-018
section_title: "Page 18"
section_number: null
pages: 18-18
source_pdf: cJdoubletwistfinal.pdf
source_sha256: a1e18db5232b39f4
toc_source: undetermined
doc_brief: "THE COLORED JONES POLYNOMIAL AND KONTSEVICH-ZAGIER SERIES FOR DOUBLE TWIST KNOTS — Using a result of Takata, we prove a formula for the colored Jones polynomial of the double twist knots K(−m,−p) and"
---
18
JEREMY LOVEJOY AND ROBERT OSBURN
+
m−1
X
s=1
p
X
j=1
j−1
X
j′=1
n2mj′−sn2mj−2m+s−1 +
m−1
X
s=1
p
X
j=1
j
X
j′=1
n2mj′−m−sn2mj−m+s−1
−
m−1
X
s=1
p
X
j=1
j−1
X
j′=1
n2mj′−2m+sn2mj−2m+s−1 −
m−1
X
s=1
p
X
j=1
j−1
X
j′=1
n2mj′−m+sn2mj−m+s−1
−
m
X
s=2
p
X
j′=1
j−1
X
j′=1
n2mj′−2m+s−1n2mj−2m+s−1 −
m
X
s=2
p−1
X
j=1
p
X
j′=j+1
n2mj−m+s−1n2mj′−m+s−1
−
m−1
X
s=1
p
X
j=1
n2mj−m+sn2mj−m+s−1 −
p−1
X
j=0
m
X
i=0
n2mj+i−1n2mj+i.
(3.17)
Now we see that this is equal to (3.5) as follows. The ﬁrst four lines of (3.17) correspond to the
ﬁrst term in (3.5); namely, the ﬁrst line of (3.17) corresponds to (i, j) ≡(i, −i) mod 2m, the
second line to (i, j) ≡(i, −i −1) mod 2m, the third line to (i, j) ≡(i, i −1) mod 2m and the
fourth line to (i, j) ≡(i, i) mod 2m. Finally, the ﬁfth line of (3.17) matches the second sum of
(3.5). Thus, we have proven that (3.4) equals (3.5).
□
Proof of Theorem 1.2. As (1.12) reduces to (1.13) when m = 1 and this case was proven in
[28], we assume m ≥2. Using Lemmas 2.4 and 2.5, one can check that for l = 4mp + 1 and
t = 4mp −2p + 1
a(n) = −
2p−1
X
j=1
(−1)jnmj
(3.18)
and b1(n) + b2(n) equals
p
X
j=1
"m−1
X
i=0
n2mj−2m+i −
2m−1
X
i=m+1
n2mj−2m+i
#
+
m
X
k=1
p
X
j=1
j
X
j′=1
(n2mj−k+1 −n2mj−k)(n2mj′−2m+k −n2mj′−2m)
−
m−1
X
s=1
p
X
j=2
j
X
j′=2
(n2mj−m−s+1 −n2mj−m−s)(n2mj′−2m −n2mj′−3m+s)
+
p
X
j=1
 
p
X
j′=j
(n2mj′ −n2mj′−2m+1) + n2mj−2m+1
!
n2mj−2m
+
m−1
X
s=1
p
X
j=1
 
j
X
j′=1
(n2mj′−s −n2mj′−2m+s) +
p
X
j′=j+1
(n2mj′−s −n2mj′−2m+s+1)
!
n2mj−2m+s
