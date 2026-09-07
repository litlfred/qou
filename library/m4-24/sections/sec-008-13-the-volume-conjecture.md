---
doc_id: m4-24
doc_title: "Problems on invariants of knots and 3-manifolds Edited by T. Ohtsuki Preface"
section_id: sec-008-13-the-volume-conjecture
section_title: "The volume conjecture"
section_number: 1.3
pages: 21-25
source_pdf: m4-24.pdf
source_sha256: cf7c5e29b818e647
doc_brief: "Problems on invariants of knots and 3-manifolds Edited by T. Ohtsuki Preface — 111 sections: Introduction; Polynomial invariants of knots; The Jones polynomial"
---
In [196] R. Kashaev de
ned a series of invariants hLiN 2 C of a link L for
N =2 ; 3; by using the quantum dilogarithm. In [198] he observed, by
formal calculations, that
2 lim
N!1
loghLiN
N =v o l (S3−L)
for L = K41;K 52;K 61 ,w h e r ev o l (S3−L) denotes the hyperbolic volume of
S3−L. Further, he conjectured that this formula holds for any hyperbolic link
L. In 1999, H. Murakami and J. Murakami [296] proved that hLiN = JN (L)
for any link L,w h e r eJN (L) denotes the N -colored Jones polynomial 5 of L
evaluated at e2p−1=N .
Conjecture 1.19 (The volume conjecture, [198, 296]) For any knot K ,
2 lim
N!1
logjJN (K)j
N =v3jjS3−Kjj; (2)
wherejjjj denotes the simplicial volume and v3 denotes the hyperbolic volume
of the regular ideal tetrahedron.
Remark For a hyperbolic knot K , (2) implies that
2 lim
N!1
logjJN (K)j
N =v o l (S3−K):
Remark [296] Both sides of (2) behave well under the connected sum and
the mutation of knots. Namely,
jjS3−(K1#K2)jj =jjS3−K1jj +jjS3−K2jj;
JN (K1#K2)= JN (K1)JN (K2);
5This is the invariant obtained as the quantum invariant of links associated with the N -
dimensional irreducible representation of the quantum group Uq(sl2).
Geometry &TopologyMonographs, Volume 4 (2002)
394 T. Ohtsuki (Editor)
and JN (K)a n djjS3−Kjj do not change under a mutation of K . For details
see [296] and references therein.
Remark The statement of the volume conjecture for a linkL should probably
be the same statement as (2) replacing K with L. It is necessary to assume
that L is not a split link, since JN (L) = 0 for a split link L (then, the left
hand side of (2) does not make sense).
Example It is shown [200] that for a torus link L
lim
N!1
loghLiN
N =0;
which implies that (2) is true for torus links.
Remark Conjecture 1.19 has been proved for the 
gure eight knot K41 (see
[295] for an exposition). However, we do not have a rigorous proof of this
conjecture for other hyperbolic knots so far. We explain its diculty below,
after a review of a proof for K41 .
We sketch a proof of Conjecture 1.19 for the 
gure eight knotK41 ; for a detailed
proof see [295]. It is known that
JN (K41 )=
N−1X
n=0
(q)n(q−1)n; (3)
where we put q =e2p−1=N and
(q)n =( 1−q)(1−q2) (1−qn); (q)0 =1:
As N tends to in
nity 
xing n=N in 
nite, the asymptotic behaviour of the
absolute value of (q)n is described by
logj(q)nj =
nX
k=1
log

2s i nk
N

= N

Z n=N
0
log(2 sint)dt +O(logN)
=−N
2 Im
(
Li2(e2np−1=N)

+O(logN);
where Li2 denotes the dilogarithm function de
ned on C−fx2Rj x> 1g by
Li2(z)=
1X
n=1
zn
n2 =−
Z z
0
log(1−s)
s ds:
Geometry &TopologyMonographs, Volume 4 (2002)
Problems on invariants of knots and 3-manifolds 395
Noting that each summand of (3) is real-valued, we have that
JN (K41 )=
X
0n<N
exp
N
2 Im
(
Li2(e−2np−1=N)−Li2(e2np−1=N)

+O(logN)

:
The asymptotic behaviour of this sum can be described by the maximal point
z0 of Im
(
Li2(1=z)−Li2(z)

on the unit circle

z2C

jzj =1
}
.I nf a c tt h i sz0
is a critical point of Li 2(1=z)−Li2(z)i n C, and hence Im
(
Li2(1=z0)−Li2(z0)

gives the hyperbolic volume of S3−K41 . Therefore, the conjecture holds in
this case.
Next, we sketch a formal argument toward Conjecture 1.19 for the knot K52 .
Following [198], we have that
JN (K52 )=
X
0mn<N
(q)2
n
(q)m
q−m(n+1);
where the asterisk implies the complex conjugate. By applying the formal
approximation6
(q)n
?
exp
 N
2p−1
(
Li2(1)−Li2(e2np−1=N)

; (4)
(q)
n
?
exp
 N
2p−1
(
Li2(e−2np−1=N)−Li2(1)

;
we have that
JN (K52 )
?
X
0mn<N
exp
 N
2p−1
(2
2 −2Li2(e2np−1=N)
−Li2(e−2mp−1=N)+ 2n
N
2m
N

:
Further, by formally replacing7 the sum with an integral putting t =n=N and
s =m=N,w eh a v et h a t
JN (K52 )
??
N2
Z
0st1
exp N
2p−1
(2
2 −2Li2(e2p−1t)
−Li2(e−2p−1s)+2 t 2s

dsdt (5)
=−N2
42
Z
exp N
2p−1
(2
2 −2Li2(z)−Li2( 1
w )−logz logw
dw
w
dz
z ;
6It might be dicult to justify this approximation in a usual sense, since the argument of
(q)n ,g i v e nb y(q)n =j(q)nj q−n(n+1)=2(−p−1)n , changes discretely and quickly near the
limit.
7It might be seriously dicult to justify this replacement, since there is a large parameter
N in the power of the summand, which exponentially contributes the summand.
Geometry &TopologyMonographs, Volume 4 (2002)
396 T. Ohtsuki (Editor)
where the second integral is over the domain

(z;w )2C2 

jzj =jwj =1; 0
arg(w) arg(z) 2
}
, and the equality is obtained by putting z = e2p−1t
and w = e2p−1s . By applying the saddle point method 8 the asymptotic be-
haviour might be described by a critical value of
2
2 −2Li2(z)−Li2( 1
w)−logz logw: (6)
Since a critical value of this function gives a hyperbolic volume of S3−K52 ,
this formal argument suggests Conjecture 1.19 for K52 .
It was shown by Yokota [409], following ideas due to Kashaev [196] and Thurston
[382], that the hyperbolic volume of the complement of any hyperbolic knot K
is given by a critical value of such a function as (6), which is obtained from a
similar computation of JN (K)a sa b o v e .
Problem 1.20 Justify the above arguments rigorously.
Remark The asymptotic behaviour of JN (K) might be described by using
quantum invariants ofS3−K . We have some ways to compute the asymptotic
behaviour of such a quantum invariant, say, when K is a 
bered knot (in this
case, S3−K is homeomorphic to a mapping torus of a homeomorphism of a
punctured surface), and when we choose a simplicial decomposition of (a closure
of) S3−K . For details, see remarks of Conjecture 7.12.
The following conjecture is a complexi
cation of the volume conjecture (Con-
jecture 1.19).
Conjecture 1.21 (H. Murakami, J. Murakami, M. Okamoto, T. Takata,
Y. Yokota [297]) For a hyperbolic link L,
2
p
−1 lim
N!1
logJN (L)
N =C S (S3−L)+
p
−1vol(S3−L)
for an appropriate choice of a branch of the logarithm, where CS and vol denote
the Chern-Simons invariant and the hyperbolic volume respectively. Moreover,
lim
N!1
JN+1(L)
JN (L) =e x p
 1
2p−1
(
CS(S3−L)+
p
−1vol(S3−L)

: (7)
Remark It is shown [297], by formal calculations (such as (4) and (5)), that
Conjecture 1.21 is \true" for K52;K 61;K 63;K 72;K 89 and the Whitehead link.
8The saddle point method in multi-variables is not established yet. This might be a tech-
nical diculty.
Geometry &TopologyMonographs, Volume 4 (2002)
Problems on invariants of knots and 3-manifolds 397
Remark The statement for non-hyperbolic links should probably be the same
statement, replacing vol( S3−L)w i t hv3jjS3−Ljj.N o t e t h a t , i fL is not
hyperbolic, then it is also a problem (see Problem 7.16) to 
nd an appropriate
de
nition of CS(S3−L), which might be given by (7). It is necessary to assume
that L is not a split link, since JN (L) = 0 for a split link L.
Remark (H. Murakami) Zagier [410] gave a conjectural presentation of the
asymptotic behaviour of the following sum,
JN (K31 )=
N−1X
k=0
(q)k 
N!1
exp

−p−1
