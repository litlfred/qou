---
doc_id: arxiv-math-0108011v1
doc_title: "The Homfly polynomial of the decorated Hopf link"
section_id: sec-009-3-the-hopf-link-decorated-with-columns-and-rows
section_title: "The Hopf link decorated with columns and rows"
section_number: 3
pages: 10-13
source_pdf: 0108011v1.pdf
source_sha256: e4af4b5d3c5ff6cd
toc_source: inferred
doc_brief: "The Homfly polynomial of the decorated Hopf link — The main goal is to ﬁnd the Homﬂy polynomial of a link formed by decorating each component of the Hopf link with the closure of a directly oriented"
---
rows
We now compute the series Eck(t) for any integer k ≥0. To do this, we start
with a surprisingly simple formula for ⟨ci, dj⟩.
Lemma 3.1 We have
⟨ci, dj⟩= ⟨ci⟩⟨dj⟩v−1(s2j −s2(j−i) + s−2i) −v
v−1 −v
for any integers i ≥0 and j ≥0.
Proof :
We shall prove the lemma by expressing the Homﬂy polynomial
of a certain decorated link in two diﬀerent ways and comparing the results.
The link in question is the 2-parallel of the unknot with framing 1 as shown
below, decorated with ci on one component and dj on the other component.
We denote its framed Homﬂy polynomial by R.
R = χ













ci
dj













= χ







ci dj







The positive curl on n strings belongs to the centre of the Hecke algebra
Hn, and so its product with any quasi-idempotent eλ, |λ| = n, is a scalar
multiple of eλ. The content, cn(x), of the cell x in row i and column j of
10
a Young diagram λ is deﬁned to be cn(x) = j −i. The scalar f(λ) was
calculated using skein theory in theorem 17 of [10] as
f(λ) = v−|λ|snλ
where nλ is twice the sum of the contents of all cells of λ. By removing the
curls on the two components of the 2-parallel we get
R = f(ci)f(dj)⟨ci, dj⟩.
(3)
The other way to calculate R is to regard it as the Homﬂy polynomial
of the unknot with framing 1 decorated by the product of ci and dj, as
elements of C. Since the elements Qλ are Schur functions, by Lukac [6], they
multiply according to the Littlewood-Richardson rules. We can then write
cidj = µi,j+1 + µi+1,j where µa,b is the simple hook Young diagram with a
cells in the ﬁrst column and b cells in the ﬁrst row. Hence
R = f(µi,j+1) ⟨µi,j+1⟩+ f(µi+1,j) ⟨µi+1,j⟩.
(4)
From the formula for f(λ) above we get
f(ci) = v−is−i(i−1), f(dj) = v−jsj(j−1), f(µa,b) = v−(a+b−1)sb(b−1)−a(a−1),
and hence
f(ci+1) = v−1s−2if(ci), f(dj+1) = v−1s2jf(dj), f(µi,j) = vf(ci)f(dj).
The following relations were shown skein theoretically in [1].
⟨ci+1⟩
=
v−1s−i −vsi
si+1 −s−i−1 ⟨ci⟩,
⟨dj+1⟩
=
v−1sj −vs−j
sj+1 −s−j−1 ⟨dj⟩,
⟨µi,j⟩
=
(sj −s−j)(si −s−i)
(v−1 −v)(si+j−1 −s−i−j+1) ⟨ci⟩⟨dj⟩.
We can in fact deduce the product formula (10) for
P ⟨ci⟩ti using only
the ﬁrst of these, and hence the closed formula (12) for ⟨λ⟩.
Using these relations equation (4) gives
R
=
f(µi,j+1) ⟨µi,j+1⟩+ f(µi+1,j) ⟨µi+1,j⟩
=
vf(ci)v−1s2jf(dj)(si −s−i)(v−1sj −vs−j)
(v−1 −v)(si+j −s−i−j) ⟨ci⟩⟨dj⟩
+s−2if(ci)f(dj)(sj −s−j)(v−1s−i −vsi)
(v−1 −v)(si+j −s−i−j) ⟨ci⟩⟨dj⟩
=
v−1(s2j −s2(j−i) + s−2i) −v
v−1 −v
f(ci)f(dj) ⟨ci⟩⟨dj⟩.
(5)
11
Equations (3) and (5) then give
⟨ci, dj⟩= ⟨ci⟩⟨dj⟩v−1(s2j −s2(j−i) + s−2i) −v
v−1 −v
since f(ci) and f(dj) are non-zero.
✷
Using our notation above, we have
Corollary 3.2
Hck(t) = 1 −v−1s−2k+1t
1 −v−1st
H∅(t)
for any integer k ≥0.
Proof :
Since H∅(t) = t∅(H(t)) = P
j≥0 ⟨dj⟩tj we must show that
(1 −v−1st) 1
⟨ck⟩
X
j≥0
⟨ck, dj⟩tj = (1 −v−1s−2k+1t)
X
j≥0
⟨dj⟩tj.
The constant terms of the power series in the above equation are equal to
1. To show that the coeﬃcients of tj on each side agree it is enough to show
that
1
⟨ck⟩⟨ck, dj⟩−v−1s 1
⟨ck⟩⟨ck, dj−1⟩= ⟨dj⟩−v−1s−2k+1 ⟨dj−1⟩.
(6)
By lemma 3.1 the left hand side of equation (6) is
⟨dj⟩v−1(s2j −s2(j−k) + s−2k) −v
v−1 −v
−v−1s ⟨dj−1⟩v−1(s2(j−1) −s2(j−1−k) + s−2k) −v
v−1 −v
.
Because
⟨dj⟩= ⟨dj−1⟩v−1sj−1 −vs−j+1
sj −s−j
this can be rewritten as
 (v−1sj−1 −vs−j+1)(v−1(s2j −s2(j−k) + s−2k) −v)
(sj −s−j)(v−1 −v)
−v−1sv−1(s2(j−1) −s2(j−1−k) + s−2k) −v
v−1 −v
!
⟨dj−1⟩.
(7)
12
The right hand side of equation (6) is
 v−1sj−1 −vs−j+1
sj −s−j
−v−1s−2k+1
!
⟨dj−1⟩.
(8)
It is straightforward to conﬁrm that the expressions (7) and (8) are equal,
and thus equation (6) follows.
✷
An immediate consequence of corollary 3.2 and lemma 2.2 is
Corollary 3.3
Eck(t) =
1 + v−1st
1 + v−1s−2k+1tE∅(t)
for any integer k ≥0.
4
