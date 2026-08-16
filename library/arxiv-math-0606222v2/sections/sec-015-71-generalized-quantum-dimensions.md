---
doc_id: arxiv-math-0606222v2
doc_title: "QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIONS"
section_id: sec-015-71-generalized-quantum-dimensions
section_title: "Generalized quantum dimensions"
section_number: 7.1
pages: 30-32
source_pdf: 0606222v2.pdf
source_sha256: 5c2a45596d04dd07
doc_brief: "QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIONS — We derive explicit dimension formulas for irreducible MF-spherical KF-re- presentations where KF is the maximal compact subgroup of the"
---
the generalized dimension Dq(λ).
Lemma 7.1. We have
Dq(λ) = a−|λ|t−2(ρ,λ)
n∏
i=1
vi(λi;q)
∏
1≤j<k≤n
w+
j,k(λj +λk;q)w−
j,k(λj −λk;q), λ ∈ Λ n,
wherevi(m;q), w±
j,k(m;q) for m ∈ Z+ are given by
vi(m;q) =
(
atn−i,q−1abtn−i;q
)
m
(
qtn−i,bt n−i;q
)
m
(1 −q2m−1abt2(n−i))
(1 −q−1abt2(n−i)) ,
w+
j,k(m;q) =
(
q−1abt2n−j−k+1;q
)
m(
abt2n−j−k−1;q
)
m
(1 −qm−1abt2n−j−k)
(1 −q−1abt2n−j−k) ,
w−
j,k(m;q) =
(
tk−j+1;q
)
m(
qtk−j−1;q
)
m
(1 −qmtk−j)
(1 −tk−j) .
Proof. This follows from a direct computation using the evaluation formulas a nd the qua-
dratic norm formulas for the multivariable little q-Jacobi polynomials. □
The explicit expressions for the generalized dimensions associated t o the fundamental
partitions ωr ∈ Λ n (r = 0,...,n ) simplify drastically.
Proposition 7.2. Forr = 0,...,n we have
(7.1) Dq(ωr) =
(
qabt2n−r−1,t n+1−r,at n−r,abt 2n−r;t
)
r(
q,t,bt n−r,abt n−r−1;t
)
r
(1 −abt2n−2r−1
1 −abt2n−1
)
a−rtr(r+1−2n).
Proof. Note that
|ωr| =r, 2(ρ,ω r) = r(2n −r − 1).
By Lemma 7.1 we thus obtain
(7.2)
Dq(ωr) = a−rtr(r+1−2n)
r∏
i=1
vi(1;q)
∏
1≤j<k≤r
w+
j,k(2;q)
r∏
j=1
n∏
k=r+1
w+
j,k(1;q)
r∏
j=1
n∏
k=r+1
w−
j,k(1;q).
QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIO NS 31
By direct computations we obtain the explicit expressions
r∏
i=1
vi(1;q) =
(
atn−r,q−1abtn−r;t
)
r
(
qabt2n−2r;t2)
r(
qtn−r,bt n−r;t
)
r
(
q−1abt2n−2r;t2)
r
,
∏
1≤j<k≤r
w+
j,k(2;q) =
(
abt2n−r;t
)
r
(
q−1abt2n−2r,qabt 2n−2r−1;t2)
r(
q−1abt2n−2r,qabt 2n−2r−1,abt 2n−2r−1;t
)
r
(1 −abt2n−2r−1)
(1 −abt2n−1) ,
r∏
j=1
n∏
k=r+1
w+
j,k(1;q) =
(
q−1abt2n−2r,abt 2n−2r−1;t
)
r(
q−1abtn−r,abt n−r−1;t
)
r
,
r∏
j=1
n∏
k=r+1
w−
j,k(1;q) =
(
tn+1−r,qt n−r;t
)
r(
t,q ;t
)
r
.
(7.3)
Only the second formula needs explanation. Set
er(u;t) =
∏
1≤j<k≤r
(1 −ut1−j−k
1 −ut−j−k
)
,
then we can write
∏
1≤j<k≤r
w+
j,k(2;q) = er(q−1abt2n)er(abt2n)er(abt2n−1)er(qabt2n−1).
On the other hand, by induction to r ∈ {1,...,n },
er(u;t) =
(
ut2−2r;t2)
r−1(
ut1−2r;t
)
r−1
.
Combining both formulas we easily obtain the desired expression for ∏
1≤j<k≤rw+
j,k(2;q).
The lemma now follows by substituting the expressions (7.3) in (7.2), a nd by simplifying
the resulting expression. □
As a curiosity, note that the elementary identity
(
ut1−r;t
)
r = (−u)rt− 1
2 r(r−1)(
u−1;t
)
r
allows us to rewrite (7.1) as
Dq
(
ωr) =
(
t−n,a−1t1−n,a−1b−1t1−2n,q−1a−1b−1t2−2n;t
)
r(
t,q,b −1t1−n,a−1b−1t2−n;t
)
r
(1 −a−1b−1t1+2r−2n
1 −a−1b−1t1−2n
) (
qat2n−1) r
for r = 0,...,n , which one recognizes as the weight function for t-Racah polynomials, see
e.g. [14].
32 URI ONN AND JASPER V. STOKMAN
