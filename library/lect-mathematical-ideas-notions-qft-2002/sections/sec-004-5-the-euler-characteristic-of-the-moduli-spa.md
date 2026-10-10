---
doc_id: lect-mathematical-ideas-notions-qft-2002
doc_title: "Mathematical ideas and notions of quantum field theory"
section_id: sec-004-5-the-euler-characteristic-of-the-moduli-spa
section_title: "The Euler characteristic of the moduli space of curves"
section_number: "5"
pages: 30-38
source_pdf: lect-mathematical-ideas-notions-qft-2002.pdf
source_sha256: 95cac1ccd6c80226
toc_source: inferred
text_source: text rebuilt from glyph codes of the ps2pdf'd dvips PostScript (bitmap Type-3 fonts carry raw TeX OT1 codes; ps2pdf reports 'c' as U+0020, so a char-level rebuild maps it back and expands ligatures); prose good, display math flattened
---
5. The Euler characteristic of the moduli space of curves
Matrix integrals (in particular, computation of the polynomial Pm(x)) can be
used to calculate the orbifold Euler characteristic of the moduli space of curves.
This was done by Harer and Zagier in 1986. Here we will give a review of this
result (with some omissions).
5.1. Euler charactristics of groups. We start with recalling some basic notions
from algebraic topology.
Let − be a discrete group, and Y be a contractible finite dimensional CW com-
plex, on which − acts cellularly. This means that − acts by homeomorphisms of
Y that map each cell homeomorphically to another cell. We will assume that the
stabilizer of each cell is a finite group (i.e. Y is a proper −-complex).
Suppose first that the action of − is free (i.e. the stabilizers of cells are trivial).
This is equivalent to saying that − is torsion free (i.e has no nontrivial finite sub-
groups), since a finite group cannot act without fixed points on a contractible finite
dimensional cell complex (as it has infinite cohomological dimension).
In this case we can define a cell complex Y=− (a classifying space for −), and
i i
we have H (Y=−; A) = H (−; A) for any coeÆcient group A. In particular, if Y=−
is finite then − has finite cohomological dimension, and the Euler characteristic
MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY 31
P P
i i i
(−) := (−1) dim H (−; Q) is equal to (−1) ni(Y=−), where ni(Y=−) denotes
the number of cells in Y=− of dimension i.
This setting, however, is very restrictive, since it allows only groups of finite
cohomological dimension, and in particular excludes all non-trivial finite groups.
So let us consider a more general setting: assume that some finite index subgroup
0
−  −, rather than − itself, satisfies the above conditions. In this case, on may
define the Euler characteristic of − in the sense of Wall, which is the rational number
0 −1 0
[− : − ] (− ).
It is easy to check that the Euler characteristic in the sense of Wall can be
computed using the following Quillen's formula
X dim
(−1)
(−) =
jStabj
2cells(Y)=−
0
In particular, this number is independent of − (which is also easy to check directly).
−1
Example 1. If G is a finite group then (G) = jGj (one takes the trivial
group as the subgroup of finite index).
Example 2. G = SL2(Z). This group contains a subgroup F of index 12, which
is free in two generators (check it!). The group F has Euler characteristic −1, since
its classifying space Y=F is figure “eight” (i.e., Y is the universal cover of figure
“eight”). Thus, the Euler characteristic of SL2(Z) is −1=12.
The Euler characteristic in the sense of Wall has a geometric interpretation in
terms of orbifolds. Namely, suppose that − is as above (i.e. (−) is a well defined
rational number), and M is a contractible manifold, on which − act freely and
properly discontinuously. In this case, stabilizers of points are finite, and thus M=−
is an orbifold. This means, in particular, that to every point x 2 M=− is attached a
0
finite group Aut(x), of size ≤ [− : − ]. Let Xm be the subset of M=−, consisting of
points x such that Aut(x) has order m. It often happens that Xm has the homotopy
type of a finite cell complex. In this case, the orbofold Euler characteristic of M=−
P
is defined to be orb(M=−) = m (Xm)=m.
Now, we claim that orb(M=−) = (−). Indeed, looking at the projection
0 1 0 0
M=− ! M=−, it is easy to see that orb(M=−) = [−:−0](M=− ). But M=− is
0 0 0
a classifying space for − , so (M=− ) = (− ), which implies the claim.
Example. Consider the group − = SL2(Z) acting on the upper half plane
H. Then H=− is the moduli space of elliptic curves. So as a topological space it
is C , where all points have automorphism group Z=2, except the point i having
automorphism group Z=4, and  which has automorphism group Z=6. Thus, the
1 1 1 1
orbifold Euler characteristic of H=− is (−1) + + = − . This is not surprising
2 4 6 12
since we proved that orb(H=−) = (−), which was computed to be −1=12.
5.2. The mapping class group. Now let g  1 be an integer, and  be a closed
1
oriented surface of genus g. Let p 2 , and let − be the group of isotopy classes of
g
diffeomorphisms of  which preserves p. We will recall without proof some standard
facts about this group, following the paper of Harer and Zagier, Inv. Math.,v.85,
p.457-485.
1
The group −g is not torsion free, but it has a torsion free subgroup of finite index.
1 1
Namely, consider the homomorphism −g ! Sp(2g; Z=nZ) given by the action of −g
on H1(; Z=nZ). Then for large enough n (in fact, n  3), the kernel Kn of this
map is torsion free.
32 MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY
It turns out that there exists a contractible finite dimensional cell complex Y ,
1
to be constructed below, on which −g acts cellularly with finitely many cell orbits.
1
Thus, the Euler characteristic of − in the sense of Wall is well defined.
g
1
Theorem 5.1. (Harer-Zagier) (−g) = −PB2g=2g, where Bn are the Bernoulli
n z
numbers, defined by the generating function n0 Bnz =n! = ez−1 .
1 1
Remark 1. The group − acts on the Teichmu¨ller space T , which is, by
g g
definition the space of pairs ((R; z); f), where (R; z) is a complex Riemann surface
with a marked point z, and f is an isotopy class of diffeomorphisms R !  that
1
map z to p. One may show that Tg is a contractible manifold of dimension 6g − 4,
1 1
and that the action of − on T is properly discontinuous. In particular, we may
g g
1 1 1
define an orbifold M = T =− . This orbifold parametrizes pairs (R; z) as above;
g g g
therefore, it is called the moduli space of Riemann surfaces (=smooth complex
projective algebraic curves) with one marked point. Thus, Theorem 5.1 gives the
orbifold Euler characteristic of the moduli space of curves with one marked point.
Remark 2. If g > 1, one may define the analogs of the above objects without
marked points, namely the mapping class group −g, the Teichmu¨ller space Tg, and
the moduli space of curves Mg = Tg=−g (one can do it for g = 1 as well, but
in this case there is no difference with the case of one marked point, since the
translation group allows one to identify any two points on ). It is easy to see
1
that we have an exact sequence 1 ! 1() ! −g ! −g ! 1, which implies that
1
(−g) = (−g)=(). Thus, (−g) = orb(Mg) = B2g=4g(g − 1)
5.3. Construction of the complex Y . We begin the proof of Theorem 5.1 with
the construction of the complex Y , following the paper of Harer and Zagier. We
will first construct a simplicial complex with a − action, and then use it to construct
Y .
Let (ff1; :::; ffn) be a collection of closed simple unoriented curves on , which
begin and end at p, and do not intersect other than at p. Such a collection is called
an arc system if two conditions are satisfied:
(A) none of the curves is contractible to a point;
(B) none of the curves is contractible to each other.
Define a simplicial complex A, whose n − 1-simplices are isotopy classes of arc
systems consisting of n  1 arcs, and the boundary of a simplex corresponding to
(ff1; :::ffn) is the union of simplices corresponding to the arc system (ff1; :::; ff^i; :::; ffn)
(ffi is omitted).
1
It is clear that the group −g acts simplicially on A.
1 1 1
Example. Let g = 1, i.e.  = S  S . Then −g = SL2(Z). Up to its action,
1
there are only three arc systems (Fig. 17). Namely, viewing S as the unit circle in
the complex plane, and representing arcs parametrically, we may write these three
systems as follows:
i i i i i i i
B0 = f(e ; 1)g; B1 = f(e ; 1); (1; e )g; B2 = f(e ; 1); (1; e ); (e ; e )g
>From this it is easy to find the simplicial complex A. Namely, let T be the tree
with root t0 connected to three vertices t1; t2; t3, with each ti connected to two
vertices ti1; ti2, each tij connected to tij1; tij2, etc. (Fig.18). Put at every vertex of
T a triangle, with sides transversal to the three edges going out of this vertex, and
glue triangles along the sides. This yields the complex A, Fig.19 (check it!). The
action of SL2(Z) (or rather P SL2(Z)) on this complex is easy to describe. Namely,
MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY 33
2 3
recall that P SL2(Z) is generated by S; U such that S = U = 1. The action of
S; U on T is defined as follows: S is reflection with flip with respect to a side of the
triangle 0 centered at t0 (Fig.20), and U is rotation by 2=3 around t0.
B0 B1 B2
Figure 17. Three arc systems.
1
This example shows that the action of − on A is not properly discontinuous,
g
and some simplices have infinite stabilizers (in the example, it is the 0-dimensional
simplices). Thus, we would like to throw away the “bad” simplices. To do it,
let us say that an arc system (ff1; ::; ffn) fills up  if it cuts  into a union of
regions diffeomorphic to the open disk. Let A1 be the union of the simplices in A
corresponding to arc systems that do not fill up . This is a closed subset, since
Figure 18. Tree T
Figure 19. Complex A
34 MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY
Figure 20. Reflection with a flip.
the property of not filling up  is obviously stable under taking an arc subsystem.
Thus, A n A1 is an open subset of A. In the example above, it is the complex A
with 0-dimensional simplices removed.
The following theorem shows that A n A1 is in fact a combinatorial model for
1 1
the Teichmu¨ller space Tg , with the action of −g.
1
Theorem 5.2. (Mumford) (a) The action of −g on A n A1 is properly discontin-
uous.
1
(b) AnA1 is a topologically a manifold, which is −g-equivariantly homeomorphic
1
to the Teichmu¨ller space Tg ; in particular, it is contractible.
Remark 1. Theorem 5.2 exhibits the significance of conditions (A) and (B).
Indeed, if either of the conditions were dropped, then one could consider arc systems
(ff1; :::; ffn) with arbitrarily large n, while with conditions (A),(B), as seen from
Theorem 5.2, the largest value of n is 6g − 3.
Remark 2. If g = 1, Theorem 5.2 is clear from the explicit description of A
(convince yourself of this!).
Theorem 5.2 is rather deep, and we will not give its proof, which is beyond
the scope of this course. Rather, we will use it to define the “Poincare dual” CW
complex Y of A n A1. Namely, to each filling arc system (ff1; :::; ffn) we will assign
a 6g − 3 − n-dimensional cell, and the boundary relation is opposite to the one
before. The existence of this CW complex follows from the fact that A n A1 is a
manifold. For instance, in the case g = 1 the complex Y is the tree T .
Now, the complex Y is contractible (since so is A n A1), and admits a cellular
1
action of − with finitely many cell orbits and finite stabilizers. This means that
g
1
the Euler characteristic of −g is given by Quillen's formula.
X
1
1 dim
(−g) = (−1) :
jStabj
2cells(Y )=−1g
Example. In the g = 1 case, T has one orbit of 0-cells and one orbit of 1-
cells. The stabilizer of a 0-cell in SL2(Z) is Z=6, and of 1-cell is Z=4. Hence,
1 1 1
(SL2(Z)) = 6 − 4 = −12, which was already computed before by other methods.
1 1
5.4. Enumeration of cells in Y=−g. Now it remains to count cells in Y=−g, i.e.
to enumerate arc systems which fill  (taking into account signs and stabilizers)
To do this, we note that by definition of “filling”, any filling arc system S defines

a cellular decomposition of . Thus, let S be the Poincare dual of this cellular

decomposition. Since S has a unique zero cell, S has a unique 2-cell. Let n be the
 
number of 1-cells in S (or S ). Then (; S ) is obtained by gluing a 2n-gon (=the
MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY 35
unique 2-cell) according to a pairing of its sides preserving orientation. (Note that
 
S can be reconstructed as (S ) ).
This allows us to link the problem of enumerating filling arc systems with the
problem of counting such gluings, which was solved using matrix integrals. Namely,
the problem of enumerating filling arc systems is essentially solved modulo one
complication: because of conditions (A) and (B) on an arc system, the gluings we
will get will be not arbitrary gluings, but gluings which also must satisfy some
conditions. Namely, we have
Lemma 5.3. Let (ff1; :::; ffn) be a system of curves, satisfying the axioms of a filling
arc system, except maybe conditions (A) and (B). Then
(i) (ff1; :::; ffn) satisfies condition (A) iff no edge in the corresponding gluing is
glued to a neighboring edge.
(ii) (ff1; :::; ffn) satisfies condition (B) iff no two consequtive edges are glued to
another pair of consequtive edges in the opposite order.
-
I
loop homo-
topic to 0.
Figure 21
-
6
M
loops homotopic
to each other.
Figure 22
The lemma is geometrically evident, and its proof is obtained by drawing a
picture (Fig.21 for (i), Fig.22 for (ii)). Motivated by the lemma, we will refer to
the conditions on a gluing in (i) and (ii) also as conditions (A) and (B).
Denote by ”g(n); g(n); g(n) the numbers of gluings of a (labeled) 2n-gon into
a surface of genus g, with no conditions, condition (A), and conditions (A),(B),
respectively (so ”g(n) is the quantity we already studied).
Proposition 5.4. One has
X
1 n−1 g(n)
(− ) = (−1) :
g
2n
n
Proof. Each filling arc system  arises from 2n=jStab()j gluings (since the labeling
of the polygon does not matter for the resulting surface with an arc system). Thus,
the result follows from Quillen's formula. 
36 MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY
P n−1 g(n)
5.5. Computation of (−1) . Now it remains to compute the sum on
n 2n
the right hand side. To do this, we will need to link g(n) with ”g(n), which has
already been computed. This is accomplished by the following lemma.
Lemma 5.5. One has
 
X
2n
”g(n) = g(n − i);
i
i
 
X
n
g(n) = g(n − i):
i
i
Proof. Proof of the first equation. Let  be a gluing of a 2n-gon  with labeled
vertices. If there is a pair of consequtive edges that are glued, we can glue them
to obtain a 2n − 2-gon. Proceeding like this as long as we can, we will arrive at
0
a 2n − 2i-gon , with a gluing  of its sides which satisfies condition (A). Note
0
that  and  do not depend on the order in which neighboring edges were glued
to each other, and  has a canonical labeling by 1; :::; 2n − 2i, in the increasing
0
order of the “old” labels. Now, we claim that each (;  ) is obtained in exactly
2n
ways; this implies the required statement.
i
Indeed, let us consider vertices of  that ended up in the interior of . They
have mapped to i points in the interior (each gluing of a pair of edges produces a
new point). Let us call these points w1; :::; wi, and let j be the smallest label of a
vertex of  that goes to wj. Then 1; :::; i is a subset of f1; :::; 2ng. This subset
0
completely determines the gluing  if (;  ) are given: namely, we should choose
j such that j + 1 6= k for any k, and glue the two edges adjacent to j; then
relabel by 1; :::; 2n − 2 the remaining vertices (in increasing order of “old” labels),
and continue the step again, and so on. From this it is also seen that any set of j
may arise. This proves the claim.
Proof of the second equation. Let  be a gluing of  (with labeled edges) which
satisfies condition (A) but not necessarily (B). If a1; a2 are consecutive edges that
are glued to consequtive edges b2; b1 in the opposite order, then we may unite a1; a2
into a single edge a, and b2; b1 into b, and obtain a 2n − 2-gon with a gluing.
Continuing so as long as we can, we will arrive at a 2n − 2i-gon  with a new
0
gluing  , which satisfies conditions (A) and (B). In , each (j-th) pair of edges
P
m−i
is obtained for mj + 1 pairs of edges in . Thus, j=1 mj = i. Furthermore, for
0
any (;  ) the collection of numbers m1; :::; mn−i defines (; ) uniquely, up to
deciding which of the m1 +1 edges constituting the first edge of  shold be labeled
0
by 1. Thus, each (;  ) arises in the number of ways given by the formula
X
(m1 + 1):
P
m1;:::;mn−i: mj=i
 
n
It is easy to show (check!) that this number is equal to . The second equation
i
is proved. 
The completion of the proof of Theorem 5.1 depends now on the following com-
putational lemma.
MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY 37
Lemma 5.6. Let ”(n); (n); (n), n  0, be sequences satisfying the equations
 
X
2n
”(n) = (n − i);
i
i
 
X
n
(n) = (n − i):
i
i
 
2n
Assume also that ”(n) = f(n), where f is a polynomial such that f(0) = 0.
n
P
n−1
Then (0) = 0, (n) has finitely many nonzero values, and (−1) (n)=2n =
0
f (0).
Proof. Let us first consider any sequences ”(n), (n), and (n) linked by the equa-
tions of the lemma. Let E(z), M(z), and L(z) be their generating functions (i.e.
P
n
E(z) = ”(n)z etc.). We claim that
n0
p p
1 + 1 − 4z 1 − 1 − 4z
E(z) = L( p ):
2(1 − 4z) 2 1 − 4z
To see this, it suÆces to consider the case i = Æki for some k. In this case,
       
X X
2n n − i n 2p + 2q q p+q
E(z) = z = z
i k p k
i;n p;q0
But the function
 
X
2p + r p
Fr(z) := z
p
p0
equals
 p r
1 1 − 1 − 4z
Fr(z) = p ;
1 − 4z 2z
−1
as may be easily seen by induction from the recursion Fr = z (Fr−1−Fr−2), r  2.
Substituting this in the formula for E(z), one gets (after trivial simplifications)
p p
1 + 1 − 4z 1 − 1 − 4z
k
E(z) = ( p ) ;
2(1 − 4z) 2 1 − 4z
as desired.
Now assume that ”(n) satisfies the polynomiality condition. This means that
1
E(z) = P (zc)jz=0 p , where P is a polynomial with vanishing constant term.
1−4z
z
To prove our claim, it suÆces to consider the case P (z) = (1 + a) − 1, where a is
0
a formal parameter (so P (0) = ln(1 + a)). In this case we get
1 1
E(z) = p − p
1 − 4(1 + a)z 1 − 4z
Hence,
1 1
L(u) = (p − 1)
1 + u 1 − 4au(1 + u)
Therefore,
X Z 0 X   Z 1
k−1 1 1 2p p−1 p p−1 p−1
(−1) k=2k = L(u)du=u = (−1) a x (1−x) dx:
2 −1 2 p 0
k p1
38 MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY
R
1 p−1 p−1 2
But x (1 − x) dx is a beta integral, and it equals (p − 1)! =(2p − 1)!. Thus,
0 P
p−1 p
the above integral equals (−1) a =p = ln(1 + a), as desired. 
p1
Now we finish the proof of the theorem. Recall that using matrix integrals we
have proved the formula
   
X X
n+1−2g (2n)! n p x
(14) Pn(x) := ”g(n)x = 2
2nn! p p + 1
g p0
Let us set q = n − p. Then expression (14) takes the form
   
X
2n n n!
−q
(15) Pn(x) = 2 x(x − 1):::(x − n + q):
n q (n − q + 1)!
q0
−2g n+1
We claim nowthat the coeÆcient of x (g  1) in the polynomial Pn(x)=x
2n
are of the form fg(n), where fg is a polynomial. Indeed, contributions to the
n
−2g
coeÆcient of x come from terms with q ≤ 2g only, so it suÆces to check that each
of these contributions is as stated. This reduces to checking that the coeÆcients of
the Laurent polynomial Q(x; n) = (1 − 1=x):::(1 − n=x) are polynomials in n, which
vanish at −1 (except, of course, the leading coeÆcient). To see this, let Q(x; a) =
−(x)
−(x−a)xa (this equals to Q(x; n) if a = n). This function has an asymptotic Taylor
expansion in 1=x as x ! +1, and it is easy to show that the coeÆcients are
polynomials in a. Moreover, Q(x; −1) = 1, which implies the required statement.
Furthermore, we claim that fg(0) = 0: again, this follows from the fact that the
non-leading coeÆcients of the expansion of Q(x; a) vanish at a = 0. But this is
clear, since Q(x; 0) = 1.
Thus, we are in a situation where Lemma 5.6 can be applied. So it remains to
P
0 −2g
compute f (0)x . To do this, observe that the terms with q > 1 do not
g1 g
0
contribute to f (0), as they are given by polynomials of n that are divisible by
g
2
n . So we only need to consider q = 0 and q = 1. For q = 1, the contribution is
−1
the value of (2x) (1 − 1=x):::(1 − n=x) at n = 0, i.e. it is 1=2x. For q = 0, the
contribution is the derivative at 0 with respect to n of (1 − 1=x):::(1 − n=x)=(n + 1),
d Q(x;a) d
i.e. it is daja=0 a+1 = −1 + daja=0Q(x; a). Thus, we have (asymptotically)
X 0
1 d 1 − (x)
0 −2g
fg(0)x = + ja=0Q(x; a) = + − log x
2x da 2x −(x)
g1
0
However, the classical asymptotic expansion for − =− is:
0 X1
− (x) 1 B2g −2g
= log x − − x :
−(x) 2x 2g
g=1
0
This implies that fg(0) = −B2g=2g. Hence the Harer-Zagier theorem is proved.
