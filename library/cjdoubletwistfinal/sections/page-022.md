---
doc_id: cjdoubletwistfinal
doc_title: "THE COLORED JONES POLYNOMIAL AND KONTSEVICH-ZAGIER SERIES FOR DOUBLE TWIST KNOTS"
section_id: page-022
section_title: "Page 22"
section_number: null
pages: 22-22
source_pdf: cJdoubletwistfinal.pdf
source_sha256: a1e18db5232b39f4
toc_source: undetermined
doc_brief: "THE COLORED JONES POLYNOMIAL AND KONTSEVICH-ZAGIER SERIES FOR DOUBLE TWIST KNOTS — Using a result of Takata, we prove a formula for the colored Jones polynomial of the double twist knots K(−m,−p) and"
---
22
JEREMY LOVEJOY AND ROBERT OSBURN
−
m−1
X
s=1
p
X
j=1
p
X
j′=j
n2mj′−m+s+1n2mj−m+s +
m−1
X
s=1
p
X
j=1
p
X
j′=j
n2mj′−m−sn2mj−m+s
−
p−1
X
j=0
m
X
i=2
n2mj+i−1n2mj+i.
(3.27)
Now, the last line of (3.27) is just the j′ = j term of the fourth line. In the second line,
perform the shift j′ →j′ + 1 and start the sum at j = 1. The second sum on this line then
cancels with the second sum of penultimate line, except for the j′ = j term. But this term now
becomes the j′ = j term for the second sum in the ﬁfth line. After simplifying and gathering
terms, we have
m−1
X
k=1
p
X
j=1
j
X
j′=1
n2mj′−2m+kn2mj−k+1 +
m−1
X
s=1
p
X
j=1
j−1
X
j′=1
n2mj′−m+sn2mj−m−s+1
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
n2mj′−sn2mj−2m+s +
m−1
X
s=1
p
X
j=1
j
X
j′=1
n2mj′−m−sn2mj−m+s
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
n2mj′−2m+sn2mj−2m+s −
m−1
X
s=1
p
X
j=1
j−1
X
j′=1
n2mj′−m+sn2mj−m+s
−
m−1
X
s=1
p
X
j=1
j
X
j′=1
n2mj′−2m+sn2mj−2m+s+1 −
m−1
X
s=1
p
X
j=1
j
X
j′=1
n2mj′−m+sn2mj−m+s+1.
(3.28)
Now we see that this is equal to (3.22) as follows. Namely, the ﬁrst line of (3.28) corresponds
to (i, j) ≡(i, −i + 1) mod 2m, the second line to (i, j) ≡(i, −i) mod 2m, the third line to
(i, j) ≡(i, i) mod 2m and the fourth line to (i, j) ≡(i, i + 1) mod 2m. This completes the proof
that (3.21) is equal to (3.22).
□
4. Concluding remarks and questions
The work in this paper may be compared with that of Hikami and the ﬁrst author in [14, 15,
18], where one ﬁnds generalized Kontsevich-Zagier functions Ft(q) and generalized U-functions
Ut(x; q) for torus knots T(2,2t+1). In the context of this family of torus knots, we have
Ft(q) := qt
∞
X
kt≥···≥k1≥0
(q)kt
t−1
Y
i=1
qki(ki+1)

ki+1
ki

(4.1)
and
Ut(x; q) := q−t
X
kt≥···≥k1≥1
(−xq)kt−1(−x−1q)kt−1 qkt
t−1
Y
i=1
qk2
i

ki+1 + ki −i + 2 Pi−1
j=1 kj
ki+1 −ki

.
(4.2)
(Note that F1(q) = F1,1(q) and U1(x; q) = U1,1(x; q) since the underlying knot in each case
is the trefoil). While both the torus knot and double twist knot families of functions satisfy
