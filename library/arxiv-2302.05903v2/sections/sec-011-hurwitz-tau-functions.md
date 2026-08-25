---
doc_id: arxiv-2302.05903v2
doc_title: "On combinatorial generalization(s) of Borel transform: Averaging method in combinatorics of symmetric polynomials"
section_id: sec-011-hurwitz-tau-functions
section_title: "Hurwitz tau-functions"
section_number: null
pages: 12-13
source_pdf: 2302.05903v2.pdf
source_sha256: 9a17abd36cc8a317
doc_brief: "On combinatorial generalization(s) of Borel transform: Averaging method in combinatorics of symmetric polynomials — We elaborate on the recent suggestion to consider averaging of Cauchy identities"
---
The combinatorial Borel transform allows one to enrich the set of the Hurwitz τ-functions [14,20]
τ (n){p(1),...,p (n)} :=
X
R
q|R|d2−n
R SR{p(1)}...S R{p(n)} (85)
to make the power of dR and the number of Schur functions independent: suppose m>n , then
X
R
d2−m
R SR{p(1)}...S R{p(n)} =
D
τ (m){p(1),...,p (n),p (n+1),...,p (m)}
E
p(n+1),...,p(m)
(86)
Averaging here is performed over the m−n sets of time variables. For example, a direct counterpart of (1)
would be
X
R
q|R|
dR
=
X
R
q|R|
dR
D
SR{p(1)
E
| {z }
1
D
SR{p(2)
E
| {z }
1
D
SR{p(3)
E
| {z }
1
=
D
τ (3){p(1),p (2),p (3)}
E
p(1),p(2),p(3)
(87)
At the same time, from what we know about the spectrum of dimensions,
X
R
q|R|
dR
=
X
R
q|R| |R|!
dimR
=
∞X
r=0
r!·qr
(
2 + 2· 1
r− 1 + 2·
 
1
r(r−3)
2
+ 1
(r−1)(r−2)
2
!
+
+2·
 
1
r(r−1)(r−5)
6
+ 1
r(r−2)(r−4)
3
+ 1
(r−1)(r−2)(r−3)
6
!
+O(r−4)
)
(88)
This first item corresponds to representations [ r] and [1r], the second, to [r− 1, 1] and [2, 1r−2] and so on:
dim[r−1,1] =r− 1
dim[r−2,2] = r(r− 3)
2
dim[r−2,1,1] = (r− 1)(r− 2)
2
dim[r−3,3] = r(r− 1)(r− 5)
6
dim[r−3,2,1] = r(r− 2)(r− 4)
3
dim[r−3,1,1,1] = (r− 1)(r− 2)(r− 3)
6
... (89)
It is important that this is a discrete spectrum and multiplicities stabilize at large r. The smallest dimensions,
like listed in (89) are made from polynomials like rm
m!

1 +O(r−1)

, but at another end of the spectrum the
growth is already factorial. In particular, the biggest dimension Dr of all dimR at the given level |R| = r is
restricted at large r by [21]:
√
r!e−α1
√r(1+o(1))≤Dr≤
√
r!e−α2
√r(1+o(1)) (90)
where α1,2 are some constants. Still this growth is much weaker than r! in the numerator of (88). Thus
contributions with all m are divergent at large r =|R|, and one can expect the whole series to be ambiguous.
The same is true for any particular term in the expansion (88).
We will deal with the divergent sumsξ−ν =P
R
q|R|
dν
R
with negative powers ofdR as with formal power series.
Note that they have integer-valued coefficients, provided by inverse powers of representation dimensions dR =
|R|!
dimR
with multiplicities read from (7). Their plethystic logarithms Ψν(k) also have an interesting interpretation.
Indeed, consider
ξ−ν =
X
R
q|R|
dν
R
= exp
 ∞X
k=1
Ψν(k)qk
k
!
(91)
12
Remarkably, all the coefficients Ψ ν(k) are positive integers, and they can be interpreted as the numbers of
subgroups of index k in the fundamental group of a certain fiber space [22]. They are a little more complicated
(multi-linear) combinations of powers of above-mentioned integers dR = |R|!
dimR
so that in the decomposition
Ψν(k) =
∞X
n=1
cn(k)ην
n (92)
the spectrum ηn of Ψν(k) is more complicated than the spectrum d−1
R ofξ−ν, with some of elements ηn coming
from products of d−1
R , and the coefficients cn(k) are not obligatory positive (despite Ψ ν(k) is positive), and,
hence, they can not play a role of multiplicities.
One can compare the spectrum of ξ−ν (the values of d−1
R ),
|R| 1 2 3 4 5 6 ...
d−1
R 1 2 3 6 8 12 24 20 24 30 120 45 72 80 144 720 (93)
with the spectrum of Ψν(k) appearing in (92) (see Table 3 of [22], note that Ψν(k) are denoted asRν(k) in [22]):
Ψν(k)

Table 3

η1 η2 η3 η4 η5 η6 ...
Ψν(1) 1
Ψν(2) 1 2
Ψν(3) 1 2 3 6
Ψν(4) 1 2 3 4 6 8 12 24
Ψν(5) 1 2 3 4 8 12 20 30 120
Ψν(6) 1 2 3 4 6 8 9 12 16 18 20 24 30 36 45 48 72 80 120 144 720
...
where the quantities in the boxes are the products of the powers of the primary elements of the spectrum from
(93), and for each Ψν(k) only ηn corresponding to non-zero cn in (92) are specified.
