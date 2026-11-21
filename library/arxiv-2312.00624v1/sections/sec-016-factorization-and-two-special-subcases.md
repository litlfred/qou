---
doc_id: arxiv-2312.00624v1
doc_title: "On the structure of wave functions in complex Chern–Simons theory"
section_id: sec-016-factorization-and-two-special-subcases
section_title: "Factorization and two special subcases"
section_number: null
pages: 34-36
source_pdf: 2312.00624v1.pdf
source_sha256: bda867f7b84f69c3
toc_source: outline
doc_brief: "On the structure of wave functions in complex Chern–Simons theory — We study the structure of wave functions in complex Chern–Simons theory on the complement of a hyperbolic knot, emphasizing the"
---
Factorization and two special subcases
Let us apply the explicit formula for the Faddeev’s quantum dilogarithm at the rational point
b2 = P/Q, P, Q ∈Z>0 coprime, in Eq. (C.11) to the expression for Fk(y(x)), 0 ≤k ≤PQ−1, which
is given in Eq. (5.17). After appropriately rearranging the terms, we find the factorization
eFk(y(x)) = eF0(y(x))f0,k(y(x))f1,k(y(x))f2,k(y(x)) ,
(5.24)
where we have introduced the functions
f0,k(y(x)) =
h
1 −eQ(x−y(x))+πi(P+Q) 
1 −eQy(x)+πi(P+Q)i
k
P Q ,
(5.25a)
f1,k(y(x)) =
Q−1
Y
j=1



1 + ex−y(x)+ πiP
Q (2j+1) 
1 + ey(x)+ πiP
Q (2j+1+2k/P)

1 + ex−y(x)+ πiP
Q (2j+1−2k/P) 
1 + ey(x)+ πiP
Q (2j+1)


j
Q
,
(5.25b)
f2,k(y(x)) =
P−1
Y
j=1



1 + e
Q
P (x−y(x))+ πiQ
P (2j+1) 
1 + e
Q
P y(x)+ πiQ
P (2j+1+2k/Q)

1 + e
Q
P (x−y(x))+ πiQ
P (2j+1−2k/Q) 
1 + e
Q
P y(x)+ πiQ
P (2j+1)


j
P
,
(5.25c)
for 0 ≤k ≤PQ −1. Thus, we can write the state integral for arbitrary rational values of b2 in
Eq. (5.18) in the equivalent form
χ41(u; ℏ) = e
x2Q
2πiP +x(2Q−1
2 −Q
2P )
ibQ
p
∆(exQ)
h
eF0(y+(x))A(y+(x)) −eF0(y−(x))A(y−(x))
i
,
(5.26)
– 33 –
where the function A(y(x)) is defined by
A(y(x)) =
PQ−1
X
k=0
e−2xk
P f0,k(y(x))f1,k(y(x))f2,k(y(x)) ,
(5.27)
and F0(y(x)) can be expressed explicitly in terms of more elementary functions using Eq. (C.11).
We stress that the formula for the state integral in Eq. (5.26) allows us to more clearly separate the
contributions from the two non-abelian saddle connections of the 41-knot labeled by α = geom, conj,
as in the holomorphic/antiholomorphic block decomposition in Eq. (3.13). Indeed, expanding the
functions F0(y∓(x)) in powers of X, X−1 and suitably identifying the terms in the expansions,
we derive the integer constants c±s, s ∈Z>0, previously written in Eqs. (4.11a), (4.11b), for the
geometric and conjugate branches, respectively.
Let us consider now the two special choices b2 = P and b2 = 1/Q for P, Q ∈Z>0. In both
subcases, the closed formula for the state integral of the figure-eight knot in Eq. (5.26) specializes in
a correspondingly simpler and more compact form. We start by choosing b2 = P positive integer.
After some manipulations, the factorization formula in Eq. (5.24) reduces to the relation
eFk(y(x)) = eF0(y(x))
k−1
Y
j=0

1 + e
1
P (x−y(x))−πi
P (2j+1) 
1 + e
1
P y(x)+ πi
P (2j+1)
,
(5.28)
where 0 ≤k ≤P −1, and we can write the state integral in Eq. (5.26) for b2 = P as
χ41(u; ℏ) = e
x2
2πiP +x( 3
2 −1
2P )
ib
p
∆(ex)
h
eF0(y+(x))B(y+(x)) −eF0(y−(x))B(y−(x))
i
,
(5.29)
where the function B(y(x)) is simply defined by
B(y(x)) =
P−1
X
k=0
e−2xk
P
k−1
Y
j=0

1 + e
1
P (x−y(x))−πi
P (2j+1) 
1 + e
1
P y(x)+ πi
P (2j+1)
,
(5.30)
and F0(y(x)) can be expressed explicitly by means of Eq. (C.13a). Let us now choose b−2 = Q
positive integer. After some manipulations, the factorization formula in Eq. (5.24) becomes
eFk(y(x)) = eF0(y(x))
k−1
Y
j=0

1 + ex−y(x)−πi
Q (2j+1) 
1 + ey(x)+ πi
Q (2j+1)
,
(5.31)
and the exact partition function in Eq. (5.26) for b2 = 1/Q assumes the simplified form
χ41(u; ℏ) = e
x2Q
2πi +x( 3Q
2 −1
2)
ibQ
p
∆(exQ)
h
eF0(y+(x))C(y+(x)) −eF0(y−(x))C(y−(x))
i
,
(5.32)
where the function C(y(x)) is given by
C(y(x)) =
Q−1
X
k=0
e−2xk
k−1
Y
j=0

1 + ex−y(x)−πi
Q (2j+1) 
1 + ey(x)+ πi
Q (2j+1)
,
(5.33)
– 34 –
and F0(y(x)) can be expressed explicitly by means of Eq. (C.13b). We observe that the reduced fac-
torization formulae in Eq. (5.28), (5.31) for b2 = P and b2 = 1/Q with P, Q ∈Z>0 can alternatively
be derived by substituting ibk/P = ib−1k and ibk/P = ibk into the arguments of the Faddeev’s
quantum dilogarithms in Eq. (5.17) and applying the periodicity properties in Eqs. (C.8c), (C.8d)
and Eqs. (C.8a), (C.8b) to the resulting formulae for Fk(y(x)), 0 ≤k ≤PQ −1, respectively. In the
general case of b2 = P/Q, instead, we cannot resort to these quasi-periodicity properties because the
functions Fk(y(x)) contain, in general, a fractional shift in the arguments of the Faddeev’s quantum
dilogarithms.
