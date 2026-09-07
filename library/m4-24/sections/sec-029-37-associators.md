---
doc_id: m4-24
doc_title: "Problems on invariants of knots and 3-manifolds Edited by T. Ohtsuki Preface"
section_id: sec-029-37-associators
section_title: "Associators"
section_number: 3.7
pages: 60-63
source_pdf: m4-24.pdf
source_sha256: cf7c5e29b818e647
doc_brief: "Problems on invariants of knots and 3-manifolds Edited by T. Ohtsuki Preface — 111 sections: Introduction; Polynomial invariants of knots; The Jones polynomial"
---
An associator  is de
ned to be an invertible group-like element in A(###;C)
satisfying that "2=1 2A (##;C) and the following relations,
= ;
= w h e r ew ep u tH = :
Geometry &TopologyMonographs, Volume 4 (2002)
Problems on invariants of knots and 3-manifolds 433
Here, i and "i are the comultiplication and the counit acting on thei-th solid
line; see [29] for these notations. An associator is derived from a Drinfel’d series
’(A;B )b y
= ’
(
;

2A (###;C); (17)
where a Drinfel’d series is an invertible group-like power series’(A;B )o fn o n -
commutative indeterminates A and B satisfying certain relations.
The Drinfel’d associator is given as follows. We consider the di
erential equa-
tion
G0(z)= 1
2p−1
A
z + B
z−1

G(z); (18)
for an analytic function G of the variable z,w h e r eG(z) belongs to the formal
power series ringChhA;Biiof non-commutative indeterminatesA andB.T h e r e
exists unique solutions G() and G() of the above di
erential equation of
the forms
G()(z)= f(z)zA=2p−1
G()(z)= g(1−z)(1−z)B=2p−1
where f(z)a n d g(z) are analytic functions with f(0) = g(0) = 12ChhA;Bii
de
ned in a neighborhood of 0 2C.T h e p o w e r s e r i e s’KZ(A;B )2ChhA;Bii
is de
ned by G() =G()’KZ(A;B ). The associator derived from ’KZ(A;B )
by (17) is called the Drinfel’d associator.
Problem 3.13 Find a combinatorial direct presentation of an associator for
all degrees, in particular, an associator with rational coecients.
Remark We still do not have a combinatorial direct presentation of any as-
sociator for all degrees. This implies that we still do not know a combinatorial
direct presentation of the Kontsevich invariant of each knot for all degrees (ex-
cept for the trivial knot); see Problem 3.1 and its remarks. Bar-Natan [29]
showed a combinatorial degree-by-degree proof of the existence of solutions of
the de
ning relations of a pair ( R; ). Our de
nition of  follows from the
de
ning relations when R is given by exp
(1
2

.
Remark The only associator whose coecients can be directly presented for
all degrees so far is the Drinfel’d associator. We can present all degrees of the
Drinfel’d associator by a limit of iterated integrals (see (19)) of by multiple zeta
functions (see (20)). It is known [248] that all associators are related to each
Geometry &TopologyMonographs, Volume 4 (2002)
434 T. Ohtsuki (Editor)
other by \twists", which are some actions of symmetric elements in A(##;C)
on associators.
Remark ’KZ(A;B ) is presented by the following limit ,
’KZ(A;B ) = lim
"!0
"−B=2p−1G"(1−")"A=2p−1; (19)
where we regard "x as
"x = exp(x log")=1+ x log" +x2 (log")2
2 + :
Further,G" is a solution of (18) given by
G"(1−")=1+
1X
m=1
Z
"t1tm1−"
w(tm) w(t1)dt1 dtm;
putting
w(t)= 1
2p−1
A
t + B
t−1

:
Remark In [248], ’KZ(A;B ) is presented by
’KZ(A;B )=1+
1X
l=1
X
a;b;p;q
(−1)jbj+jpj(a + p; b + q)
a + p
p
b + q
q

Bjqj(A;B )(a;b)Ajpj; (20)
where the second sum runs over a; b; p; q such that the sum of their length is
equal to l and entries of them are non-negative integers. Here, the notations
are given by
(a; b)= (1; 1; ; 1| {z }
a1−1
;b 1 +1; 1; 1; ; 1| {z }
a1−1
;b 2 +1; ; 1; 1; ; 1| {z }
al−1
;bl +1 );
jaj =a1 +a2 + +al;a
b

=
a1
b1
a2
b2


al
bl

;
(A;B )(a;b) =Aa1Bb1 AalBbl:
for a =( a1; ;al)a n d b =( b1; ;bl), where the multiple zeta function is
de
ned by
(a1;a 2; ;ak)=
X
n1<n2<<nk2N
n−a1
1 n−a2
2  n−ak
k :
Geometry &TopologyMonographs, Volume 4 (2002)
Problems on invariants of knots and 3-manifolds 435
In particular,
’KZ(A;B )=1 + 1
24[A;B ]−(3)
(2p−1)3 ([A; [A;B ]]+[B; [A;B ]])+

terms of
degree 4

:
Remark In [29], an associator with rational coecients is given in low degrees
by
log’(A;B )= [A;B ]
48 −8[A; [A; [A;B ]]] + [A; [B; [A;B ]]]
11520
+ [A; [A; [A; [A; [A;B ]]]]]
60480 + [A; [A; [A; [B; [A;B ]]]]]
1451520 + 13[A; [A; [B; [B; [A;B ]]]]]
1161216
+ 17[A; [B; [A; [A; [A;B ]]]]]
1451520 + [A; [B; [A; [B; [A;B ]]]]]
1451520
−(interchange of A and B)
+ (terms of degree 8):
Problem 3.14 (J. Roberts) Construct a rational Drinfel’d associator in the
context of rational homotopy theory.
Remark (J. Roberts) The theory of 1-minimal models provides a represen-
tation of the pure braid group, which is the fundamental group of the con
gu-
ration space of distinct ordered points in C, the \pure braid space" for short.
This is the representation coming from the Kontsevich integral. A better way
to describe it is as a representation of the fundamental groupoid of the pure
braid space, using \basepoints at in
nity" described by associations (bracket-
ings) of the points. In this picture, the Drinfel’d associator is the image of a
certain path which changes the basepoint. Is there a theory of 1-minimal mod-
els for fundamental groupoids which gives a straightforward construction of a
(rational-valued) associator, as an alternative to the tricky iterative procedures
of [29]?
