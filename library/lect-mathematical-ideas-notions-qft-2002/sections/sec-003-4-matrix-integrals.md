---
doc_id: lect-mathematical-ideas-notions-qft-2002
doc_title: "Mathematical ideas and notions of quantum field theory"
section_id: sec-003-4-matrix-integrals
section_title: "Matrix integrals"
section_number: "4"
pages: 21-30
source_pdf: lect-mathematical-ideas-notions-qft-2002.pdf
source_sha256: 95cac1ccd6c80226
toc_source: inferred
text_source: text rebuilt from glyph codes of the ps2pdf'd dvips PostScript (bitmap Type-3 fonts carry raw TeX OT1 codes; ps2pdf reports 'c' as U+0020, so a char-level rebuild maps it back and expands ligatures); prose good, display math flattened
doc_brief: "Mathematical ideas and notions of quantum field theory — 1. Generalities on quantum field theory 1.1. Classical mechanics. In classical mechanics, we study the motion of a par- ticle."
---
4. Matrix integrals
Let hN be the space of Hermitian matrices of size N. The inner product on hN
is given by (A; B) = Tr(AB). In this section we will consider integrals of the form
Z
2
−N =2 −S(A)=~
ZN = ~ e dA;
hN
R 2
−Tr(A )=2
where the Lebesgue measure dA is normalized by the condition e dA = 1,
P
2 m 3
and S(A) = Tr(A )=2 − m0 gmTr(A )=m is the action functional. We will be
interested the behavior of the coeÆcients of the expansion of ZN in gi for large
N. The study of this behavior will lead us to considering not simply Feynman
graphs, but actually fat (or ribbon) graphs, which are in fact 2-dimensional surfaces.
3
Note that we divide by m and not by m!. We will see below why such normalization will be
more convenient.
22 MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY
Thus, before we proceed further, we need to do some 2-dimensional combinatorial
topology.
4.1. Fat graphs. Recall from the proof of Feynman's theorem that given a finite
collection of flowers and a pairing  on the set T of endpoints of their edges, we
can obtain a graph − by connecting (or gluing) the points which fall in the same
pair.
Now, given an i-flower, let us inscribe it in a closed disk D (so that the ends
of the edges are on the boundary) and take its small tubular neighborhood in D.
This produces a region with piecewise smooth boundary. We will equip this region
with an orientation, and call it a fat i-valent flower. The boundary of a fat i-valent
flower has the form P1Q1P2Q2 : : : PiQiP1, where Pi; Qi are the angle points, the
intervals PjQj are arcs on cD, and QjPj+1 are (smooth) arcs lying inside D (see
Fig. 10).
3-valent flower fat 3-valent flower
Q1
P1
P2
Q2
Q3
P3
Figure 10
Now, given a collection of usual flowers and a pairing  as above, we can consider
the corresponding fat flowers, and glue them (respecting the orientation) along
intervals PjQj according to . This will produce a compact oriented surface with
boundary (the boundary is glued from intervals PjQj+1).
~
We will denote this surface by −, and call it the fattening of − with respect to
. A fattening of a graph will be called a fat (or ribbon) graph. Thus, a fat graph
is not just an oriented surface with boundary, but such a surface together with a
partition of this surface into fat flowers.
Note that the same graph − can have many different fattenings, and in particular
the genus g of the fattening is not determined by − (see Fig. 11).
4.2. Matrix integrals in large N limit and planar graphs. Let us now return
to the study of the integral ZN. By the proof of Feynman's theorem,
X Y ni ni(i=2−1) X
g ~
i
ln ZN = ( ) F;
inini!
n 
where the summation is taken over all pairings of T = T (n) that produce a con-
i
nected graph −, and F denotes the contraction of the tensors Tr(A ) using .
For a surface  with boundary, let () denote the number of connected com-
ponents of the boundary.
(−e)
Proposition 4.1. F = N .
MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY 23
−1 g = 0 −2 g = 0
−3 g = 1
Figure 11. Gluing a fat graph from fat flowers
N 
Proof. Let ei be the standard basis of C , and ei the dual basis. Then the tensor
m
Tr(A ) can be written as
N
X
m    
m
Tr(A ) = (ei1 
 ei2 
 ei2 
 ei3 
    
 eim 
 ei1; A ):
i1;:::;im=1
One can visualize each monomial in this sum as a labeling of the angle points
P1; Q1; : : : ; Pm; Qm on the boundary of a fat m-valent flower by i1; i2; i2; i3; : : : ; im; i1.
Now, the contraction using  of some set of such monomials is nonzero iff the sub-
e
script is constant along each boundary component of − (see Fig. 12). This implies
the result. 
ei em
Contraction nonzero iff

ej en i = r, j = p, j = m, k = r,
ej en
k = p, i = m,
 
ek en
ek en that is
i = r = k = p = j = m.
 
el en
Figure 12. Contraction defined by a fat graph.
e
Let Gc(n) is the set of isomorphism classes of connected fat graphs with ni i-
e e e
valent vertices. For − 2 Gc(n), let b(−) be the number of edges minus the number
of vertices of the underlying usual graph −.
Corollary 4.2.
X Y X (−e) b(−e)
ni N ~
ln ZN = ( gi ) :
e
jAut(−)j
n −e2Gec(n)
24 MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY
Q Q
ni e
Proof. Let Gfat(n) = Sni n ( Z=iZ) . This group acts on T , so that − =
e
−g, for any g 2 Gfat (since cyclic permutations of edges of a flower extend to its
fattening). Moreover, the group acts transitively on the set of  giving a fixed fat
e e
graph −, and the stabilizer of any  is Aut(−). This implies the result. 
Now for any compact surface  with boundary, let g() be the genus of . Then
e e e e
for a connected fat graph −, b(−) = 2g(−)−2+(−) (minus the Euler characteristic).
^
Thus, defining ZN(~) = ZN(~=N), we find
Theorem 4.3.
X Y X 2−2g(−e) b(−e)
^ ni N ~
ln ZN = ( gi ) :
e
jAut(−)j
n −e2Gec(n)
This implies the following important result, due to t'Hooft.
ln Z^N
Theorem 4.4. (1) There exists a limit W1 := limN!1 N2 . This limit is given
by the formula
X Y X b(−e)
ni ~
W1 = ( gi ) ;
e
jAut(−)j
n −e2Gec(n)[0]
e
where Gc(n)[0] denotes the set of planar connected fat graphs, i.e. those which
have genus zero.
P
^ 2 −2g
(2) Moreover, there exists an expansion ln ZN =N = g0 agN , where
X Y X b(−e)
ni ~
ag = ( gi ) ;
e
jAut(−)j
n −e2Gec(n)[g]
e
and Gc(n)[g] denotes the set of connected fat graphs which have genus g.
Remark 1. Genus zero fat graphs are said to be planar because the underlying
usual graphs can be put on the 2-sphere (and hence on the plane) without self-
intersections.
Remark 2. t'Hooft's theorem may be interpreted in terms of the usual Feynman
diagram expansion. Namely, it implies that for large N, the leading contribution
to ln(ZN (~=N)) comes from the terms in the Feynman diagram expansion corre-
sponding to planar graphs (i.e. those that admit an embedding into the 2-sphere).
4.3. Integration over real symmetric matrices. One may also consider the
matrix integral over the space sN of real symmetric matrices of size N. Namely,
one puts
Z
−N(N+1)=4 −S(A)=~
ZN = ~ e dA;
sN
where S and dA are as above. Let us generalize Theorem 4.4 to this case.
As before, consideration of the large N limit leads to consideration of fat flowers
and gluing of them. However, the exact nature of gluing is now somewhat different.
 
Namely, in the Hermitian case we had (ei 
 ej ; ek 
 el ) = ÆilÆjk, which forced us to
glue fat flowers preserving orientation. On the other hand, in the real symmetric

case ei = ei, and the inner product of the functionals ei 
 ej on the space of
symmetric matrices is given by (ei 
 ej; ek 
 el) = ÆikÆjl + ÆilÆjk. This means
that besides the usual (orientation preserving) gluing of fat flowers, we now must
MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY 25
o
allow gluing with a twist of the ribbon by 180 . Fat graphs thus obtained will
be called twisted fat graphs. That means, a twisted fat graph is a surface with
boundary (possibly not orientable), together with a partition into fat flowers, and
orientations on each of them (which may or may not match at the cuts, see Fig.13).
Figure 13. Twisted-fat graph
Now one can show analogously to the Hermitian case that the 1=N expansion of
^ ^
ln ZN (where ZN = ZN(2~=N)) is given by the same formula as before, but with
etw
summation over the set G (n) of twisted fat graphs:
c
Theorem 4.5.
X Y X 2−2g(−e) b(−e)
^ ni N ~
ln ZN = ( gi ) :
e
jAut(−)j
n −e2Getcw(n)
Here the genus g of a (possibly non-orientable) surface is defined by g = 1 − =2,
2
where  is the Euler characteristic. Thus the genus of RP is 1=2, the genus of the
Klein bottle is 1, and so on.
In particular, we have the analog of t'Hooft's theorem.
ln Z^N
Theorem 4.6. (1) There exists a limit W1 := limN!1 N2 . This limit is given
by the formula
X Y X b(−e)
ni ~
W1 = ( gi ) ;
e
jAut(−)j
n −e2Getcw(n)[0]
etw
where G (n)[0] denotes the set of planar connected twisted fat graphs, i.e. those
c
which have genus zero.
P
^ 2 −2g
(2) Moreover, there exists an expansion ln ZN =N = g0 agN , where
X Y X b(−e)
ni ~
ag = ( gi ) ;
e
jAut(−)j
n −e2Getcw(n)[g]
etw
and G (n)[g] denotes the set of connected twisted fat graphs which have genus g.
c
Exercise. Consider the matrix integral over the spaceqN of quaternionic Her-
mitian matrices. Show that in this case the results are the same as in the real case,
m
except that each twisted fat graph counts with a sign, equal to (−1) , where m is
the number of twistings (i.e. mismatches of orientation at cuts). In other words,
^ ^
ln ZN for quaternionic matrices is equal ln Z2N for real matrices with N replaced
by −N.
Hint: use that the unitary group U(N; H ) is a real form of Sp(2N), and qN
2
is a real form of the representation of  V , where V is the standard (vector)
26 MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY
representation of Sp(2N). Compare to the case of real symmetric matrices, where
2
the relevant representation is S V for O(N), and the case of complex Hermitian

matrices, where it is V 
 V for GL(N).
4.4. Application to a counting problem. Matrix integrals are so rich that even
the simplest possible example reduces to a nontrivial counting problem. Namely,
consider the matrix integral ZN over complex Hermitian matrices in the case
2 2m 2
S(A) = Tr(A )=2 − sTr(A )=2m, where s = 0 (i.e. we work over the ring
2
C [s]=(s )). In this case we can set ~ = 1. Then from Theorem 4.4 we get
Z
2
2m −Tr(A )=2
Tr(A )e dA = Pm(N);
hN
P
m+1−2g
where Pm(N) is a polynomial, given by the formula Pm(N) = g0 ”g(m)N ,
and ”g(m) is the number of ways to glue a surface of genus g from a 2m-gon with
labeled sides by gluing sides preserving the orientation. Indeed, in this case we
have only one fat flower of valency 2m, which has to be glued with itself; so a direct
application of our Feynman rules leads to counting ways to glue a surface of a given
genus from a polygon.
The value of this integral is given by the following non-trivial theorem.
Theorem 4.7. (Harer-Zagier, 1986)
m  
X
(2m)! m p x(x − 1) : : : (x − p)
Pm(x) = 2 :
2mm! p (p + 1)!
p=0
The theorem is proved in the next subsections.
Looking at the leading coeÆcient of Pm, we get.
Corollary 4.8. The number of ways to glue a sphere of a 2m-gon is the Catalan
 
1 2m
number Cm = m+1 m .
Corollary 4.8 actually has another (elementary combinatorial) proof, which is as
follows. For each pairing  on the set of sides of the 2m-gon, let us connect the
midpoints of the sides that are paired by straight lines (Fig.14). It is geometrically
evident that if these lines don't intersect then the gluing will give a sphere. We
claim that the converse is true as well. Indeed, we can assume that the statement
is known for the 2m − 2-gon. Let  be a gluing of the 2m-gon that gives a sphere.
If there is a connection between two adjacent sides, we may glue them and go from
a 2m-gon to a 2m − 2-gon (Fig. 15). Thus, it is suÆcient to consider the case when
adjacent sides are never connected. Then there exist adjacent sides a and b whose
lines (connecting them to some c; d) intersect with each other. Let us now replace
0
 by another pairing  , whose only difference from  is that a is connected to b
and c to d (Fig. 16). One sees by inspection (check it!) that this does not decrease
the number of boundary components of the resulting surface. Therefore, since 
0 0
gives a sphere, so does  . But  has adjacent sides connected, the case considered
before, hence the claim.
Now it remains to count the number of ways to connect midpoints of sides with
lines without intersections. Suppose we draw one such line, such that the number
of sides on the left of it is 2k and on the right is 2l (so that k + l = m − 1). Then we
MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY 27
Figure 14. Pairing of sides of a 6-gon.
1
6 2 1 2
- 6
5
*5 3 4 3
4
Figure 15
-
Figure 16
face the problem of connecting the two sets of 2k and 2l sides without intersections.
This shows that the number of gluings Dm satisfies the recursion
X
Dm = DkDl
k+l=m−1
P
m
In other words, the generating function Dmx = 1+x+   satisfies the equation
p
2 1− 1−4x
f − 1 = xf . This implies that f = 2x , which yields that Dm = Cm. We are
done.
Corollary 4.8 can be used to derive the the following fundamental result from
the theory of random matrices, discovered by Wigner in 1955.
Theorem 4.9. (Wigner's semicircle law) Let f be a continuous function on R of
at most polynomial growth at infinity. Then
1 Z p 2 1 Z 2 p
−Tr(A )=2 2
lim Trf(A= N)e f(x) 4 − x dx:
N!1 N hN 2 −2
This theorem is called the semicircle law because it says that the graph of the
density of eigenvalues of a large random Hermitian matrix distributed according to
2
−Tr(A )=2
`the “Gaussian unitary ensemble” (i.e. with density e dA) is a semicircle.
Proof. By Weierstrass uniform approximation theorem, we may assume that f is a
polynomial. (Exercise: Justify this step).
28 MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY
2m
Thus, it suÆces to check the result if f(x) = x . In this case, by Corollary 4.8,
the left hand side is Cm. On the other hand, an elementary computation yields
R p
1 2 2m 2
2 −2 x 4 − x = Cm, which implies the theorem. 
4
4.5. Hermite polynomials. The proof of Theorem 4.7 given below uses Hermite
polynomials. So let us recall their properties.
Hermite's polynomials are defined by the formula
n
2 d 2
n x −x
Hn(x) = (−1) e e :
n
dx
n
So the leading term of Hn(x) is (2x) .
We collect the standard properties of Hn(x) in the following theorem.
P n
t
Theorem 4.10. (i) The generating function of Hn(x) is f(x; t) = n0 Hn(x) n!
2
2xt−t
= e .
00 0
(ii) Hn(x) satisfy the differential equation f − 2xf + 2nf = 0. In other words,
2
−x =2 1 2 1 2
Hn(x)e are eigenfunctions of the operator L = −2 c + 2 x (Hamiltonian of
1
the quantum harmonic oscillator) with eigenvalues n + .
2
(iii) Hn(x) are orthogonal:
Z
1
1 2
−x n
p e Hm(x)Hn(x)dx = 2 n!Æmn
 −1
(iv) One has
Z
1
1 2 (2m)!
−x 2m 2(k−m)
p e x H2k(x)dx = 2
 −1 (m − k)!
(if k > m, the answer is zero).
(v) One has
2 Xr
Hr (x) r!
= H2k(x):
r k 2
2 r! 2 k! (r − k)!
k=0
Proof. (sketch)
P n n
n t d
(i) Follows immediately from the fact that the operator (−1) n! dxn maps a
function g(x) to g(x − t).
(ii) Follows from (i) and the fact that the function f(x; t) satisfies the PDE
fxx − 2xfx + 2tft = 0.
R 2
−x
(iii) Follows from (i) by direct integration (one should compute f(x; t)f(x; u)e dx
R
using a shift of coordinate).
R 2 2
2m 2xt−t −x
(iv) By (i), one should calculate x e e dx. This integral equals
R
Z Z  
2m −(x−t)2 2m −y2 p X 2m (2m − 2p)! 2p
x e dx = (y + t) e dy ==  t :
R R p 2p 2m−p(m − p)!
The result is now obtained by extracting individual coeÆcients.
(v) By (iii), it suÆces to show that
Z
r+k 2
1 2 2 r! (2k)!
2 −x
p Hr (x)H2k(x)e dx = 2
 R k! (r − k)!
4
I adopted this proof from D.Jackson's notes
MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY 29
To prove this identity, let us integrate the product of three generating functions.
By (i), we have
Z
1 2
−x 2(tu+tv+uv)
p f(x; t)f(x; u)f(x; v)e dx = e :
 R
r r 2k
Extracting the coeÆcient of t u v , we get the result. 
4.6. Proof of Theorem 4.7. We need to compute the integral
Z
2
2m −Tr(A )=2
Tr(A )e dA:
hN
To do this, we note that the integrand is invariant with respect to conjugation by
unitary matrices. Therefore, the integral can be reduced to an integral over the
eigenvalues 1; : : : ; N of A.
N
More precisely, consider the spectrum map  : hN ! R =SN. It is well known
(due to H.Weyl) that the direct image dA is given by the formula dA =
P 2 Q
Ce− i i =2 i<j(i − j)2d, where C > 0 is a normalization constant that will
not be relevant to us. Thus, we have
R P P 2 Q
RN( i 2i m)e− i=2 i<j(i − j)2d
Pm(N) = RRN e− P 2i =2 Qi<j(i − j)2d
To calculate the integral Jm in the numerator, we will use Hermite's polynomials.
n
Observe that since Hn(x) are polynomials of degree n with highest coeÆcient 2 ,
Q
−N(N−1)=2
we have i<j(i − j) = 2 det(Hk(i)), where k runs through the set
0; 1; : : : ; n − 1. Thus, we find
Z
X P 2 Y
Jm := ( 2i m)e− i =2 (i − j)2d =
RN
i i<j
Z
2 P 2 Y
2m+N =2N 21me− i (i − j)2d =
RN
i<j
(12) Z
P 2
2m−N(N−2)=2N 21me− i det(Hk(j))2d =
RN
Z
P 2 X Y
2m−N(N−2)=2N 21me− i ( (−1)(−1)
 Hi(i)H
i(i))d:
RN
;
2SN i

(Here (−1) denotes the sign of ).
Since Hermite polynomials are ortogonal, the only terms which are nonzero are
the terms with (i) = 
(i) for i = 2; : : : ; N. That is, the nonzero terms have  = 
.
Thus, we have
Z
P 2 X Y
Jm = 2m−N(N−2)=2N 21me− i ( Hi(i)2d =
RN
2SN i
(13) NX−1 Z 1
1 2
m−N(N−2)=2 2m 2 −x
2 N!fl0 : : : flN−1 x Hj(x) e dx;
flj −1
j=0
30 MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY
R 1 2 −x2
where fli = −1 Hi(x) e dx are the squared norms of the Hermite polynomials.
Applying this for m = 0 and dividing Jm by J0, we find
NX−1 Z 1
1 2
m 2m 2 −x
Jm=J0 = 2 x Hj(x) e dx
flj −1
j=0
p
i
Using Theorem 4.10 (iii) and (v), we find: fli = 2 i! , and hence
1 Z NX−1 Xj 2mx2mH2k(x) −x2
Jm=J0 = p e dx
k 2
 R 2 k! (j − k)!
j=0 k=0
Now, using (iv), we get
NX−1 Xj k
(2m)! 2 j!
Jm=J0 = =
m 2
2 (m − k)!k! (j − k)!
j=0 k=0
N−1 j    
X X
(2m)! k m j
2 :
2mm! k k
j=0 k=0
The sum over k can be represented as a constant term of a polynomial:
j    
X
k m j m −1 k
2 = C:T:((1 + z) (1 + 2z ) ):
k k
k=0
Therefore, summation over j (using the formula for the sum of the geometric pro-
gression) yields
−1 N Xm    
(2m)! m (1 + 2z ) − 1 (2m)! p m N
Jm=J0 = C:T:((1 + z) ) = 2
2mm! 2z−1 2mm! p p + 1
p=0
We are done.
