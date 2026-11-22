---
doc_id: fulltext
doc_title: "The Dilogarithm Function"
section_id: sec-001-1-special-values
section_title: "Special values"
section_number: 1
pages: 4-6
source_pdf: fulltext.pdf
source_sha256: 05079cf525c6ba0f
toc_source: inferred
doc_brief: "The Dilogarithm Function — 14 sections: Front matter; The dilogarithm function in geomet; Special values"
---
1 Special values
Let us start with the question of special values. Most functions have either
no exactly computable special values (Bessel functions, for instance) or else a
countable, easily describable set of them; thus, for the gamma function
Γ(n) = (n −1)! ,
Γ

n + 1
2

= (2n)!
4nn!
√π ,
and for the Riemann zeta function
ζ(2) = π2
6 ,
ζ(4) = π4
90,
ζ(6) = π6
945,
. . . ,
ζ(0) = −1
2,
ζ(−2) = 0,
ζ(−4) = 0,
. . . ,
ζ(−1) = −1
12,
ζ(−3) =
1
120,
ζ(−5) = −1
252,
. . . .
Not so the dilogarithm. As far as anyone knows, there are exactly eight
values of z for which z and Li2(z) can both be given in closed form:
B
Li2(0) = 0,
Li2(1) = π2
6 ,
Li2(−1) = −π2
12,
Li2
1
2

= π2
12 −1
2 log2(2),
The Dilogarithm Function
7
Li2

3 −
√
5
2

= π2
15 −log2

1 +
√
5
2

,
Li2

−1 +
√
5
2

= π2
10 −log2

1 +
√
5
2

,
Li2

1 −
√
5
2

= −π2
15 + 1
2 log2

1 +
√
5
2

,
Li2

−1 −
√
5
2

= −π2
10 + 1
2 log2

1 +
√
5
2

.
Let me describe a recent experience where these special values ﬁgured, and
which admirably illustrates what I said about the bizarreness of the occur-
rences of the dilogarithm in mathematics. From Bruce Berndt via Henri Cohen
I learned of a still unproved assertion in the Notebooks of Srinivasa Ramanu-
jan (Vol. 2, p. 289, formula (3.3)): Ramanujan says that, for q and x between
0 and 1,
q
x +
q4
x +
q8
x +
q12
x + · · ·
= 1 −
qx
1 +
q2
1 −
q3x
1 +
q4
1 −
q5x
1 + · · ·
“very nearly.” He does not explain what this means, but a little experimen-
tation shows that what is meant is that the two expressions are numerically
very close when q is near 1; thus for q = 0.9 and x = 0.5 one has
LHS = 0.7767340194 · · · ,
RHS = 0.7767340180 · · · ,
A graphical illustration of this is also shown.
8
Don Zagier
The quantitative interpretation turned out as follows [9] : The diﬀerence
between the left and right sides of Ramanujan’s equation is O

exp
 π2/5
log q

for
x = 1, q →1. (The proof of this used the identities
1
1 +
q
1 +
q2
1 +
q3
1 + · · ·
=
∞
	
n=1

1 −qn( n
5 ) =

(−1)rq
5r2+3r
2

(−1)rq
5r2+r
2
,
which are consequences of the Rogers-Ramanujan identities and are surely
among the most beautiful formulas in mathematics.) For x →0 and q →1
the diﬀerence in question is O

exp
 π2/4
log q

, and for 0 < x < 1 and q →1 it
is O

exp
 c(x)
log q

where c′(x) = −1
x arg sinh x
2 = −1
x log


1 + x2/4 + x/2

.
For these three formulas to be compatible, one needs
 1
0
1
x log(

1 + x2/4 + x/2) dx = c(0) −c(1) = π2
4 −π2
5 = π2
20 .
Using integration by parts and formula A.3.1 (6) of [4] one ﬁnds
 1
x log


1 + x2/4 + x/2

dx = −1
2 Li2


1 + x2/4 −x/2
2
−1
2 log2(

1 + x2/4 + x/2) + (log x) log(

1 + x2/4 + x/2) + C ,
so
 1
0
1
x log(

1 + x2/4 + x/2) dx = 1
2 Li2(1) −1
2

Li2
3 −
√
5
2

+ log21 +
√
5
2

= π2
12 −π2
30 = π2
20 !
