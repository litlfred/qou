---
doc_id: 9511222v1
doc_title: "Murnaghan-Nakayama Rules for Characters of Iwahori-Hecke Algebras of the Complex Reflection Groups G(r,p,n)"
section_id: sec-004-the-poset-theorem
section_title: "The Poset Theorem"
section_number: 4
pages: 19-26
source_pdf: 9511222v1.pdf
source_sha256: 2870b5b709d1f358
doc_brief: "Murnaghan-Nakayama Rules for Characters of Iwahori-Hecke Algebras of the Complex Reflection Groups G(r,p,n) — 5 sections: Introduction; Characters of Iwahori-Hecke Algebr; Characters of Iwahori-Hecke"
---
Curtis Greene [Gre] uses the theory of partially ordered sets (posets) and Mobius
functions to prove a rational function identity ([Gre], Theorem 3.3) which can
be used to derive the Murnaghan-Nakayama rule for symmetric group characters. In [HR], we modify Greene's theorem so that it can be applied to computing
Murnaghan-Nakayama rules for the irreducible characters of the Iwahori-Hecke algebras of type An 1; Bn, and Dn. In this section, we extend the poset theorem of
[HR] so that it can be applied to computing Murnaghan-Nakayama rules (Theorem
2.17) for the irreducible characters of the cyclotomic Iwahori-Hecke algebras of type
B.
A poset is planar in the (strong) sense if its Hasse diagram may be orderembedded in R  R without edge crossings even when extra bottom and top elements are added (see [Gre] for details). A linear extension of a poset P is a poset
L with the same underlying set as P and such that the relations in L form an
extension of the relations in P to a total order. We will denote by L(P ) the set of
all linear extensions L of P .
The Mobius function of a poset P is the function  : P  P ! Z de ned
inductively for elements a; b 2 P by
(
1
if a = b,
P
if a < b,
(4:1)
(a; b) = P (a; b) =
ax<b(a; x)
0
if a 6 b.
(See [Sta] for more details on Mobius functions).
Throughout this section, P^ will denote a planar poset with unique minimal
element u, and P = P^ fug will be the poset obtained by removing the minimal
element u from P^ . We let SC be the set of minimal elements of P , and we call
these elements sharp corners. Two sharp corners s1 and s2 of SC are \adjacent" if
they are not separated by another sharp corner as the boundary of P is traversed.
If s1 and s2 are adjacent elements of SC and the least common multiple s1 _ s2
exists, then we call s1 _ s2 a dull corner of P . We let DC denote the set of all dull
corners of P . Finally, we let cc denote the number of connected components of P ,
and note that cc = jSCj jDCj.
Let fxa ; a 2 P^ g, be a set of commutative variables indexed by the elements of
P^ . For each 0  k  r 1 and each pair a < b in P^ , de ne a weight, wt(k)(a; b), by
1
wt(k)(a; b) = 1 q xaqxb1 for all a; b 2 P; and
(4:2)
(
k
)
k
wt (u; a) = xa
for all a 2 P:
Then for any planar poset P^ with unique minimal element u, de ne
Y (k) P^ (a;b)
(k)(P^ ) =
wt (a; b)
;
(4:3)
a;b2P^
a=
6 b

where P^ (a; b) is the Mobius function for the poset P^ .
In [HR], Theorem 5.3, it is proved that
X (0) ^ (0)
 (L) =  (P )(q q 1 )cc 1;
L^ 2L(P^ )

(4:4)


20

T. HALVERSON AND A. RAM

and

! Y
Y
cc 1

X
L^ 2L(P^ )

(1)(L^ ) = (1)(P )0

s2SC

xs

!

d2DC

xd 1 ;

(4:5)

The expansion in (4.5) is equal to zero if there is more than one connected component in P .
The following is our extension of the poset theorem to include values of k > 1.

Theorem 4.6. Let P^ be a planar poset (as de ned above) with unique minimal
element u. Let P = P^ n fug. Then

X

(0)(L^ ) = (q q 1 )cc 1(0)(P );

L^ 2L(P^ )

and, for 1  k  r 1,

X

! Y
Y
1 cc 1

(k)(L^ ) = (k)(P )( q + q )

L^ 2L(P^ )

jX
DCj



t=0

s2SC

xs

d2DC

xd 1

!

( 1)t et(xDC )hk t cc (xSC )

where cc is the number of connected components of P , et(xDC ) is the elementary
symmetric function in the variables fxd ; d 2 DCg, and hk t cc(xSC ) is the homogeneous symmetric function in the variables fxs ; s 2 SCg.
For each s 2 SC de ne P^s to be the same poset as P^ except with the
additional relations s  s0 , for s 6= s0 2 SC, and all other relations implied by
transitivity. Each poset Ps is planar, and each linear extension of Ps must place
the sharp corner s (a minimal element of P ) immediately after u in the ordering,
so we have
Proof.

X

L^ 2L(P^ )

(k)(L^ ) =

X X

s2SC L^ s 2L(P^s )

(k)(L^ s ) =

X

s2SC

wt(k)(u; s) 1

X

Ls 2L(Ps )

(k)(Ls );

In P we have wt(k)(a; b) = wt(0)(a; b), so by [HR], Theorem 5.3, the second sum
can be computed as

X

Ls 2L(Ps)

(k)(Ls ) =

X

Ls 2L(Ps )

(0)(Ls ) = (0) = (k)(Ps );

since Ps is connected. Moreover, wt(0)(u; s) 1 = 1 for each s 2 SC, so the case
k = 0 is proved.


CHARACTERS OF IWAHORI-HECKE ALGEBRAS OF G(r; p; n)

21

From now on assume that 1  k  r 1. Then we have
X (k) ^ X (k)
 (L) =
wt (u; s) 1 (k)(Ps )
s2SC

L^ 2L(P^ )

= (k)(P )
(k)

=  (P )
= (k)(P )

X

s2SC

X

s2SC

X

s2SC

(k)
wt(k)(u; s) 1 (k)((PPs))
(k)

wt (u; s)

1

wt(k)(u; s) 1

Y wt(k)(a; b)Ps (a;b)

a;b2P wt
a=
6 b

Y

a;b2P
a=
6 b

(k)

(4:7)

(a; b)P (a;b)

wt(k)(a; b)Ps (a;b) P (a;b):

where Pi (a; b) and P (a; b) are the Mobius functions for their respective posets.
We use the work of Greene [Gre] to compute the di erences Ps (a; b) P (a; b)
for a < b 2 P . Let P  and Ps denote the dual of P and Ps , respectively (that is
u P  v , v P u). Then, P (u; v) = P  (v; u) (see [Sta], p. 120), so we want to
compute
Ps (b; a) P  (b; a) for a < b 2 P:
Using the Mobius notation of [Gre] (p. 8, formulas (7) and (8)), let

a =
so that

X

tP  a

P  (t; a)t;

a=

X
tP  a

t ;

and

a(s) =

and

a=

In this way, a(s) = a for all a 2 P  n SC, and

s(s) = s
It follows that

and

Y
a;b2P
a=
6 b

X

s02SCnfsg

tPs a

Ps (t; a)t;

X (s)
tPs a

X
d2DC

t :

d:

Ps (s0 ; s) P  (s0 ; s) = 1; for all s0 2 SC n fsg;
Ps (d; s) P  (d; s) = +1; for all d 2 DC;
Ps (a; b) P  (a; b) = 0; for all other a; b 2 P;

wt(k)(a; b)Ps (a;b) P (a;b) =

Y
s0 2SCnfsg

Substituting back into (4.7) gives
X (k) ^ (k) X (k)
wt (u; s) 1
 (L) =  (P )
L^ 2L(P^ )

s0 +

X

s2SC

wt(k)(s; s0 ) 1

Y
s0 2SCnfsg

Y
d2DC

wt(k)(s; s0 ) 1

wt(k)(s; d):

Y
d2DC

wt(k)(s; d):


22

T. HALVERSON AND A. RAM

Using the fact that jSCj jDCj = cc (the number of connected components of
p), we cancel factors of q q 1 and factor out xs and xd 1 as follows

Y

X k

X

q q 1
xs
(k)(L^ ) = (k)(P )
1
s2SC
s0 2SCnfsg 1 xs xs0
L^ 2L(P^ )
= (k)(P )

Y ! Y

s2SC

xs

F = (k)(P )

Y

(xd xs)
X
2DC
:
xd 1 (q q 1)cc 1
xks 1 dY
s2SC

Y ! Y
s2SC

q q 1

d2DC

!

d2DC

For notational convenience, let

!
! Y
1 xs xd 1

xs

s0 2SCnfsg

(xs0 xs )

!

d2DC

xd 1 (q q 1 )cc 1:

Order the sharp corners s1 ; s2; : : : ; sjSCj from left to right as the boundary of P is
traversed, and let jsij = i (its position in the ordering). Then

Y

X k 1 d2DC(xd xs )
Y
 (L) = F
xs

X (k) ^

s2SC

L^ 2L(P^ )

=F

=F

(xs0 xs)

s0 2SCnfsg

Y

xs ( 1)jSCj jsj Y

d2DC

X k1
s2SC

Y

X k1
s2SC

xs ( 1)jSCj jsj d2DC

Y

(xp xq )

p<q2SCnfsg
Y
(xp
xs) (xs xs0 )
0
s >s
p<q2SCnfsg

(xs0

s0 <s

(xd xs )

Y

(xd xs)

Y

p<q2SCnfsg

(xp xq )

V (xSC )

xq )

;

where V (xSC ) is the Vandermonde determinant in the variables fxs ; s 2 SCg. Moreover,

Y
d2DC

(xd xs ) =

jX
DCj
t=0

et (xDC )( 1)jDCj t xsjDCj t;

where et(xDC ) is the elementary symmetric function in the variables fxd ; d 2 DCg.
Again for notational convenience, let

G=

Y

(xp xq ):

p<q2SCnfsg


CHARACTERS OF IWAHORI-HECKE ALGEBRAS OF G(r; p; n)

We then have

X k1

X (k) ^

 (L) = F s2SC

L^ 2L(P^ )

=F

jX
DCj

xs

23

jX
DCj
j
SCj jsj
( 1)
et (xDC )( 1)jDCj txjDCj t G
s

t=0

V (xSC )

X jDCj t+k 1

( 1)t et(xDC ) s2SC

xs

( 1)jDCj+jSCj jsjG

V (xSC )
X jDCj t+k 1 jsj 1
xs
( 1) G
jX
DCj
s
2
SC
= F ( 1)jSCj jDCj 1 ( 1)t et(xDC )
:
V (x )
t=0

SC
t=0
Notice that xjsDCj t+k 1 = xsk t (jSCj jDCj)+jSCj 1 = xsk t cc+jSCj 1 and that the

X k t cc+jSCj 1

numerator

s2SC

xs

( 1)jsj 1

Y

(xp xq )

p<q2SCnfsg

(4:8)

is the alternating symmetrization of the monomial
j 2 xjSCj 3    xjSCj jSCj :
xsk1 t cc+jSCj 1 xsjSC
s3
sjSCj
2
When we divide the numerator (4.8) by the Vandermonde V (xSC ), we get the
Schur function s(k t cc;0;0;:::;0)(xSC ) or, equivalently, the homogeneous symmetric
function hk t cc(xSC ), and so

X

X
 (L^ ) = F ( 1)cc 1 ( 1)t et (xDC )hk t cc(xSC );
t=0
L^ 2L(P^ )
jDCj

(k)

and the proof is completed.

Special Cases.

The homogeneous symmetric function satis es hm (xSC ) = 0 unless m > 0, so if
k  1, then hk t cc(xSC ) = 0, unless cc  k. In particular, when k = 1, the poset
P must be connected (cc = 1), and
jX
DCj

and

t=0

( 1)t et (xDC )hk t cc (xSC ) = e0 (xDC )h0(xSC ) = 1

X
L^ 2L(P^ )

(1)(L^ ) = (1)(P )

Y ! Y
s2SC

xs

d2DC

!

xd 1 ;

(4:9)
(4:10)

which agrees with (4.5).

Shapes and Standard Tableaux.

P
Theorem 4.6 reduces the problem of computing L^ 2L(P^) (k)(L^ ) to computing
(k)(P ). In the case where P is the poset of a (skew) shape, the product (k)(P ) is


24

T. HALVERSON AND A. RAM

readily computed and has been done so for q = 1 by Green [Gre] and for generic q
in [HR]. The result uses the natural extension of the theory of shapes and tableaux
to the theory of partially ordered sets. (For a full treatment of this subject, see
[Sta], whose notation we use here).
If  is a shape (possibly skew), then we construct a corresponding poset P
whose Hasse diagram is given by placing a node in each box of  and then drawing
edges connecting nodes in adjacent boxes. The order relation in this poset is so
that the smallest nodes are in the upper left corners. For example,

$

$

and
Figure 4.11

Note that posets corresponding to shapes are always planar and that the sharp
and dull corners that we de ned for partitions and shapes (see Figure 2.19) are
exactly the sharp and dull corners of the corresponding poset.
Theorem 4.12. ([Gre], Theorem 3.3; [HR], Theorem 5.8) Let P be the poset of
any shape (or skew shape) , let fxb g be a set of commutative variables indexed
by fb 2 Pg, and let q be an indeterminate. De ne
1
wt(a; b) = 1 q xqa xb1 for all a; b 2 P
(4:13)
and
Y
wt(a; b)P (a;b):
(P) =
Then

a;b2P
a6=b

(P) =

Y 1 xbxa 1 ! Y q q 1 ! Y q q 1 !
D

q q 1

R 1

xbxa 1

C 1

xb xa 1

where
D is the set of pairs (a; b) of boxes in  adjacent (northwest to southeast) in a
diagonal,
R is the set of pairs (a; b) of boxes in  adjacent (west to east) in a row, and
C is the set of pairs (a; b) of boxes in  adjacent (north to south) in a column.
Let  be a shape (or a skew shape) and let L() be the set of standard tableaux
of shape . Linear extensions of the poset P are in one-to-one correspondence with
standard tableaux having skew shape  as follows: Given a standard tableau T of
shape  let T (k) denote the box containing k in T . Then the standard tableau T
corresponds to the linear extension L of the poset P which has underlying set P
and order relations given by T (k) L T (l) if k  l. We can identify the standard
tableau T with the chain L.
Let P^ be the poset P [ fug where the adjoined element u satis es u  a for
all a 2 P. The linear extensions of the poset P^ are in one-to-one correspondence


CHARACTERS OF IWAHORI-HECKE ALGEBRAS OF G(r; p; n)

25

with the linear extensions of the poset P. Thus, we can identify a standard tableau
T of shape  with a linear extension L^ of the poset P^.
Let  be the Mobius function of the linear extension L^ of P^ that corresponds
to the standard tableau T of shape . Then, since L^ is a chain,  satis es
(
a is adjacent to b in L^ , and
(a; b) = 01; ; ifif aa<<bb and
and a is not adjacent to b in L^ .
It follows that

Y
Y (k) (a;b)
wt (a; b)
= (xT (1))k
 (T ) =  (L^ ) =
(k)

n

(q q 1 ) :
1
i=2 1 xT (i 1) xT (i)

(k)

a<b2L^

Corollary 4.14. Let  be any shape (or skew shape) with n boxes. Let fxbg

be a set of commutative variables indexed by the boxes b 2 , and let q be an
indeterminate. Then
! Y
!
! Y
1
1
1
X (0)
Y
1
x
x
q
q
q
q
b a
 (T ) = (q q 1 )cc 1
1
1 ;
1
q
q
1
x
x
1
x
x
a
a
b
b
D
C
R
T 2L()

and, for 1  k  r 1,

X

! Y
Y
1 cc 1

(k)(T ) = ( q+q )

T 2L()

jX
DCj



s2SC

xs

d2DC

xd 1

!

( 1)t et (xDC )hk t cc(xSC )

Y 1 xbxa 1 ! Y q q 1 ! Y q q 1 !

;
t=0

D

q q 1

R 1

xb xa 1

C 1

xb xa 1

where
cc is the number of connected components of ,
SC is the set of sharp corners of ,
DC is the set of dull corners of ,
R is the set of pairs (a; b) of boxes in  adjacent (west to east) in a row,
C is the set of pairs (a; b) of boxes in  adjacent (north to south) in a column, and
D is the set of pairs (a; b) of boxes in  adjacent (northwest to southeast) in a
diagonal.
^ be the poset P [ fug, where
Proof. Let P be the poset of the shape , and let P
the adjoined element u satis es u  a for all a 2 P . Then P^ is aPplanar poset with
unique minimal element, so we apply Theorem 4.6 to compute T 2L()(k)(T ) =
P
(k)
(k)
L^ 2L(P^ ) (L^ ). This reduces the problem to computing  (P ). Inside of P ,
the weights (4.2) are all independent of k and of the form (4.13), so we use Theorem
4.12 to compute (k)(P ).


26

T. HALVERSON AND A. RAM

References

S. Ariki, Representation theory of a Hecke algebra of G(r; p; n), J. of Algebra 177 (1995),
164-185.
[AK] S. Ariki and K. Koike, A Hecke algebra of (Z=rZ) o Sn and construction of its irreducible
representations, Adv. in Math. 106 (1994), 216-243.
[BM] M. Broue and G. Malle, Zyklotomische Heckealgebren, Asterisque 212 (1993), 119-189.
[GP] M. Geck and G. Pfei er, On the irreducible characters of Hecke algebras, Adv. in Math.
102 (1993), 79-94.
[Gre] C. Greene, A rational function identity related to the Murnaghan-Nakayama formula for
the characters of Sn , J. Alg. Comb. 1 (1992), 235-255.
[HR] T. Halverson and A. Ram, Murnaghan-Nakayama rules for the characters of IwahoriHecke algebras of classical type, Trans. Amer. Math. Soc. (to appear).
[Hfs] P. N. Hoefsmit, Representations of Hecke algebras of nite groups with BN-pairs of classical type, Thesis, University of British Columbia, 1974.
[KW] R.C. King and B.G. Wybourne, Representations and traces of Hecke algebras Hn (q) of
type An 1 , J. Math. Phys. 33 (1992), 4-14.
[Mac] I. G. Macdonald, Symmetric Functions and Hall Polynomials, Oxford Univ. Press, 1979.
[Osi] M. Osima, On the representations of the generalized symmetric group, Math. J. Okayama
Univ. 4 (1954).
[Pfe1] G. Pfei er, Character values of Iwahori-Hecke algebras of type B, Progress in Math.,
Birkhauser (to appear).
[Pfe2] G. Pfei er, Charakterwerte von Iwahori-Hecke-Algebren von klassischem Typ, Aachener
Beitrage zur Mathematik, vol. 14, Verlag der Augustinus-Buchhandlung, Aachen, 1995.
[Ram] A. Ram, A Frobenius formula for the characters of the Hecke algebras, Invent. Math. 106
(1991), 461-488.
[ST] G. C. Shephard and J. A. Todd, Finite unitary re ection groups, Canad. J. Math. 6
(1954), 274-304.
[Sta] R. Stanley, Enumerative Combinatorics, vol. I, Wadsworth & Brooks/Cole, 1986.
[Ste] J. Stembridge, On the eigenvalues of representations of re ection groups and wreath products, Paci c J. Math. 140 (1989), 353{396.
[vdJ] J. van der Jeugt, An algorithm for characters of Hecke algebras Hn (q) of type An 1 , J.
Phys. A 24 (1991), 3719-24.
[You] A. Young, Quantitative substitutional analysis I-IX, Proc. London Math. Soc. (1901-1952).
[Ari]

Department of Mathematics, Macalester College, St. Paul, MN 55105

E-mail address : halverson@macalstr.edu

School of Mathematics and Statistics, University of Sydney, NSW 2006, Australia

E-mail address : ram a@maths.su.oz.au
