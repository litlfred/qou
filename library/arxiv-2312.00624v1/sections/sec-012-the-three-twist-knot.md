---
doc_id: arxiv-2312.00624v1
doc_title: "On the structure of wave functions in complex Chern–Simons theory"
section_id: sec-012-the-three-twist-knot
section_title: "The three-twist knot"
section_number: null
pages: 26-29
source_pdf: 2312.00624v1.pdf
source_sha256: bda867f7b84f69c3
doc_brief: "On the structure of wave functions in complex Chern–Simons theory — We study the structure of wave functions in complex Chern–Simons theory on the complement of a hyperbolic knot, emphasizing the"
---
The state integral of the three-twist knot χ52(u; ℏ) can be expressed explicitly as [23, 29, 30]
χ52(u; ℏ) =e−πi
12− 5πi
3 c2
b

eπi(−2u2−4cbu)H(e2πbu, e4πbu, e4πbu, ;q)H(e2πb−1u, e4πb−1u, e4πb−1u; ˜q−1)
+ eπi(−2u2+4cbu)H(e−2πbu, e−4πbu, e−4πbu;q)H(e−2πb−1u, e−4πb−1u, e−4πb−1u; ˜q−1)
+H(e2πbu, e−2πbu, 1;q)H(e2πb−1u, e−2πb−1u, 1; ˜q−1)

,
(4.21)
where cb = i(b + b−1)/2 and the q-special functionH(x,y,z ;q) is defined by 12
H(x,y,z ;q) = (xq;q)∞(yq;q)∞
∞X
n=0
qn(n+1)zn
(q;q)n(xq;q)n(yq;q)n
, (4.22)
while (xq;q)∞ and (xq;q)n denote the quantum dilogarithm and the q-shifted factorial, respectively.
See Appendix C for their definitions. As for the case of the figure-eight knot in Section 4.1, using
Eq. (4.21), we can identify
ϕ(geom),WKB(X;q) = logH(X,X 2,X 2;q), (4.23a)
ϕ(conj),WKB(X;q) = logH(X−1,X−2,X−2;q), (4.23b)
ϕ(self),WKB(X;q) = logH(X,X−1, 1;q), (4.23c)
together with Cgeom =Cconj =Cself = e
3πi
4 and
is(geom)
0 (x)
ℏ +s(geom)
1 (x) + is(geom)
0 (xD)
ℏD
+s(geom)
1 (xD) = x2
iℏ + 2πx
ℏ +x + 5π2i
6ℏ + 5iℏ
24 , (4.24a)
is(conj)
0 (x)
ℏ +s(conj)
1 (x) + is(conj)
0 (xD)
ℏD
+s(conj)
1 (xD) = x2
iℏ− 2πx
ℏ −x + 5π2i
6ℏ + 5iℏ
24 , (4.24b)
is(self)
0 (x)
ℏ +s(self)
1 (x) + is(self)
0 (xD)
ℏD
+s(self)
1 (xD) = 5π2i
6ℏ + 5iℏ
24 . (4.24c)
12H(x,y ;q) is closely related to the q-hypergeometric function.
– 25 –
Indeed, the three terms in the RHS of Eq. (4.21) capture the contributions to the exact partition
function coming from the geometric, conjugate, and self-conjugate branches, respectively. These
are the only three non-abelian branches of the 52-knot, as described in Example 2.2. Moreover, as
before, we solve Eqs. (4.24a), (4.24b), and (4.24c) order by order in x and ℏ and obtain that
s(geom)
0 (x) = 5π2
6 − x2
2 , s (geom)
1 (x) =x, (4.25a)
s(conj)
0 (x) = 5π2
6 − x2
2 , s (conj)
1 (x) =−x, (4.25b)
s(self)
0 (x) = 5π2
6 , s (self)
1 (x) = 0. (4.25c)
In this way, we have fully determined the perturbative wave functions χ(α),WKB(u; ℏ) of the three-
twist knot in the resummed form of Eq. (3.1). As before, we verify successfully that they are
annihilated by the ˆA-operator in Eq. (2.36), as expected.
Let us now test the integrality conjecture in Eq. (3.6) for all three non-abelian branches. Ex-
panding the RHS of Eqs. (4.23a), (4.23b), and (4.23c) gives
ϕ(geom),WKB(X;q) =
X
k≥1
qk(Xk +X2k)
k(qk− 1) + log

X
n≥0
qn(n+1)X2n
Qn
i=1(1−qi)(1−qiX)(1−qiX2)

 , (4.26a)
ϕ(conj),WKB(X;q) =
X
k≥1
qk(X−k +X−2k)
k(qk− 1) + log

X
n≥0
qn(n+1)Xn
Qn
i=1(1−qi)(X−qi)(X2−qi)

 , (4.26b)
ϕ(self),WKB(X;q) =
X
k≥1
qk(Xk +X−k)
k(qk− 1) + log

X
n≥0
qn(n+1)Xn
Qn
i=1(1−qi)(1−qiX)(X−qi)

 . (4.26c)
Both terms on the RHS of Eq. (4.26a) for the geometric branch contribute with positive powers of
X. For the conjugate branch, we note that the negative powers of X arise entirely from the first
term on the RHS of Eq. (4.26b), while a factor of qσconj,n with
σconj,n =
n2
4

, n ∈ Z>0, (4.27)
appears in the denominator of the power series in X obtained by expanding the second term. Let
us stress that this negative power of q arises from the factors 13 Qn
i=1(X−qi)−1(X2−qi)−1 in the
summand inside the logarithm, and it is absent from both the X−1-series for the conjugate branch
and the X-series for the geometric branch. Finally, in the case of the self-conjugate branch, the first
term on the RHS of Eq. (4.26c) supplies both positive and negative powers of X, while the second
term only adds to the X-series after expansion. Here, a more complicated factor of qσself,n with
σself,n =
$
1
24
 
P
2(n + 2)
3
2
− 1
!%
, n ∈ Z>0, (4.28)
13Note that there are twice as many contributing factors of q−1 here compared to the conjugate branch of the
figure-eight knot, in agreement with the observed formulae for the functions σconj,n in Eqs. (4.7), (4.27).
– 26 –
whereP (n) denotes then-th prime number, occurs in the denominator of the power series inX after
summing up the contribution from the expansion of the second term on the RHS of Eq. (4.26c). This
originates from the factors Qn
i=1(X−qi)−1 in the summand inside the logarithm.
As we have done for the 41-knot, after extracting the coefficients a(α)
±n(q), n∈ Z>0, from the
series for ϕ(α),WKB(X;q), we obtain the functions D(α)
±s (q), s∈ Z>0, by applying the formulae in
Eqs. (3.8), (3.11). Again, these are non-trivial polynomials with integer coefficients. In particular,
the first few of them are
D(geom)
1 (q) =q, D (geom)
2 (q) =−q(−1 +q), D (geom)
3 (q) =D(geom)
4 (q) =−q3,
D(geom)
5 (q) =q4(−1 +q2), D (geom)
6 (q) =q4(−1 + 2q2 +q4),
D(geom)
7 (q) =q5(−1 +q(1 +q)2),
(4.29)
for the geometric solution,
D(conj)
1 (q) =D(conj)
2 (q) =−1, D (conj)
3 (q) =−2−q, D (conj)
4 (q) =−(1 +q)(1 + 2q),
D(conj)
5 (q) =−2− 2q− 7q2− 4q3−q4,
D(conj)
6 (q) =−(1 +q)(1 + 2q + 3q2 + 6q3 + 7q4 + 2q5)
D(conj)
7 (q) =−2− 2q− 8q2− 11q3− 20q4− 23q5− 32q6− 19q7− 6q8−q9,
(4.30)
for its conjugate, and
D(self)
1 (q) =2q, D (self)
2 (q) = 1 +q2, D (self)
3 (q) = 1 +q2 + 2q4,
D(self)
4 (q) =− 1−q +q2 + 2q4 + 3q6 +q7,
D(self)
5 (q) =− 1 +q−q2 + 2q3 + 4q5 +q6 + 6q7 + 2q8 + 2q9,
D(self)
6 (q) =− 1−q2− 2q4 + 2q5− 2q6 + 4q7 +q8 + 8q9 + 4q10
+ 11q11 + 7q12 + 5q13 + 3q14 +q15,
D(self)
7 (q) =− 1−q3− 2q5 +q6− 4q7 + 4q8− 3q9 + 9q10 + 4q11 + 18q12
+ 12q13 + 27q14 + 18q15 + 17q16 + 10q17 + 8q18 + 2q19 + 2q20,
(4.31)
for the self-conjugate one. Trivially, we have that
D(conj)
−1 (q) =D(conj)
−2 (q) =q, D (conj)
−s (q) = 0 s≥ 3,
D(self)
−1 (q) =q, D (self)
−s (q) = 0 s≥ 2.
(4.32)
We have verified numerically that the polynomials D±s(q) have integer coefficients up to s = 20 for
all three branches. We then compute the integers c±s,s∈ Z>0, using Eqs. (3.27), (3.28), which give
{c(geom)
s }s∈Z>0 ={1, 1,−8,−15, 1, 64, 148, 49,−575,−1599,−1088, 5088,... }, (4.33a)
{c(conj)
s }s∈Z>0 =(−1){1, 5, 28, 101, 401, 1544, 6077, 24101, 96418, 388205, 1571307, 6387608,... },
(4.33b)
{c(self)
s }s∈Z>0 ={2, 10, 38, 122, 402, 1486, 5931, 24058, 96995, 389810, 1572397, 6382526... },
(4.33c)
– 27 –
whilec(conj)
−s = [s]2+5[s+1]2, where [s]2 denotes the remainder of the division ofs by 2, andc(self)
−s = 1
for all s∈ Z>0. We observe that the above sequences of integers satisfy the relation
c(geom)
s +c(conj)
s +c(self)
s =c(conj)
−s +c(self)
−s , s ∈ Z>0. (4.34)
which corresponds to the analogous formula in Eq. (4.13) for the figure-eight knot. Note that, in both
our examples, the sum of the integer sequences {cs} over all branches equals the sum of the integer
sequences{c−s}, which is a periodic function of s∈ Z>0. Again, the alternative computational
approach of Appendix B agrees with the above results.
Let us now go back to the quantum A-polynomial for the 52-knot written in Eq. (2.36). The
corresponding q-difference equation in the form of Eq. (2.19) is of third order. Precisely, we have
ˆA52( ˆP, ˆX,q )χ(α),WKB(u; ℏ) = 0, (4.35)
where χ(α),WKB(u; ℏ) is the resummed perturbative wave function in Eq. (3.49) associated with the
branch α. In the rational case of q = e2πiP
Q with P,Q ∈ Z>0 coprime, Eq. (4.35) can be solved in
closed form by directly applying the results of Section 3.4.2. As for the 41-knot, let us consider the
case α = geom and drop the label to simplify our notation. After appropriately accounting for the
exponential prefactor containing the functions s0,1(x) in Eq. (4.25a), the q-difference equation above
assumes the form in Eq. (3.74) with the identifications
A(X) =q−2X−2C2(X,q )
C3(X,q ), B (X) =q−2X−4C1(X,q )
C3(X,q ), C (X) =X−6C0(X,q )
C3(X,q ), (4.36)
whereC0,C 1,C 2,C 3 are the coefficient functions defined in Eq. (2.37). Substituting the expressions in
Eq. (4.36) into Eq. (3.81) and computing the matrix MQ(X), we can then derive explicit formulae
for Πυ and υ0 from Eqs. (3.92), (3.94). We stress that the ambiguity in the definition of Θ 2 is
resolved by requiring Eq. (3.71) to be satisfied with α = geom, which implies the choice m = 2.
Plugging these into Eq. (3.95), we find the functions Υ( X) and φQ(X) for the geometric branch of
the three-twist knot. We can easily use the resulting explicit expression for φQ(X) to numerically
evaluate the integer constants cs, s∈ Z>0, for the geometric branch by applying Eq. (3.48) for
any choice of P,Q ∈ Z>0 coprime, thus producing a third independent computation which is in
perfect agreement with the previous two. The same discussion can be applied to the conjugate and
self-conjugate branches of the 52-knot, in which case the appropriate functions s0,1(x) are written
in Eqs. (4.25b), (4.25c) and the ambiguity in the choice of m in Eq. (3.93c) is fixed by imposing
the condition in Eq. (3.71) with α = conj, self, yielding m = 1 and m = 0, respectively. Again, the
corresponding integer constants c±s, s∈ Z>0, for the conjugate and self-conjugate branches match
our previous results.
