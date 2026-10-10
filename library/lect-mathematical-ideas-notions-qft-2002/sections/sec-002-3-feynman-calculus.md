---
doc_id: lect-mathematical-ideas-notions-qft-2002
doc_title: "Mathematical ideas and notions of quantum field theory"
section_id: sec-002-3-feynman-calculus
section_title: "Feynman calculus"
section_number: "3"
pages: 7-21
source_pdf: lect-mathematical-ideas-notions-qft-2002.pdf
source_sha256: 95cac1ccd6c80226
toc_source: inferred
text_source: text rebuilt from glyph codes of the ps2pdf'd dvips PostScript (bitmap Type-3 fonts carry raw TeX OT1 codes; ps2pdf reports 'c' as U+0020, so a char-level rebuild maps it back and expands ligatures); prose good, display math flattened
---
3. Feynman calculus
3.1. Wick's theorem. Let V be a real vector space of dimension d with volume
element dx. Let S(x) be a smooth function on a box B  V which attains a
minimum at x = c 2 Interior(B), and g be any smooth function on B. In the last
section we have shown that the function
Z
−d=2 S(c)=~ −S(x)=~
I(~) = ~ e g(x)e dx
B
admits an asymptotic power series expansion in ~:
m
(8) I(~) = A0 + A1~ +    + Am~ +   
Our main question now will be: how to compute the coeÆcients Ai?
It turns out that although the problem of computing I(~) is transcendental, the
problem of computing the coeÆcients Ai is in fact purely algebraic, and involves
only differentiation of the functions S and g at the point c. Indeed, recalling the
8 MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY
proof of equation 8 (which we gave in the 1-dimensional case), we see that the
calculation of Ai reduces to calculation of integrals of the form
Z
−B(x;x)=2
P (x)e dx;
V
where P is a polynomial and B is a positive definite bilinear form (in fact, B(v; u) =
(cvcuS)(c)). But such integrals can be exactly evaluated. Namely, it is suÆcient
to consider the case when P is a product of linear functions, in which case the
answer is given by the following elementary formula, known to physicists as Wick's
theorem.
For a positive integer k, consider the set f1; : : : ; 2kg. By a pairing  on this set
we will mean its partition into k disjoint two-element subsets (pairs). A pairing
can be visualized by drawing 2k points and connecting two points with an edge if
they belong to the same pair (see Fig. 1). This will give k edges, which are not
connected to each other.
1 3 1 3
2 4 2 4
1 3
2 4
Figure 1. Pairings of the set f1; 2; 3; 4g
Let us denote the set of pairings on f1; : : : ; 2kg by k. It is clear that jkj =
(2n)!
2nn! . For any  2 k, we can think of  as a permutation of f1; : : : ; 2kg, such that
2
 = 1 and  has no fixed points. Namely,  maps any element i to the second
element (i) of the pair containing i.
−1  
Theorem 3.1. Let B denote the inverse form on V , and let `1; : : : ; `m 2 V .
Then, if m is even, we have
Z
d=2 X Y
(2)
−B(x;x)=2 −1
`1(x) : : : `m(x)e dx = p B (`i; `(i))
V det B
2m=2 i2f1;:::;mg=
If m is odd, the integral is zero.
Proof. If m is odd, the statement is obvious, because the integrand is an odd
function. So consider the even case. Since both sides of the equation are symmetric
polylinear forms in `1; : : : ; `m, it suÆces to prove the result when `1 =    = `m = `.
Further, it is clear that the formula to be proved is stable under linear changes of
MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY 9
variable (check it!), so we can choose a coordinate system in such a way that
2 2
B(x; x) = x1 +    + xd, and `(x) = x1. Therefore, it is suÆcient to assume that
d = 1, and `(x) = x. In this case, the theorem says that
Z
1
2 (2k)!
2k −x =2 1=2
x e dx = (2) ;
k
−1 2 k!
which is easily obtained from the definition of the Gamma function by change of
2
variable y = x =2. 
Examples.
Z
d=2
(2)
−B(x;x)=2 −1
`1(x)`2(x)e dx = p B (`1; `2):
V det B
Z
−B(x;x)=2
`1(x)`2(x)`3(x)`4(x)e dx =
V
d=2
(2)
−1 −1 −1 −1 −1 −1
p (B (`1; `2)B (`3; `4) + B (`1; `3)B (`2; `4) + B (`1; `4)B (`2; `3)):
det B
Wick's theorem shows that the problem of computing Ai is of combinatorial
nature. In fact, the central role in this computation is played by certain finite
graphs, which are called Feynman diagrams. They are the main subject of the
remainder of this section.
3.2. Feynman's diagrams and Feynman's theorem. We come back to the
problem of computing the coeÆcients Ai. Since each particular Ai depends only on
a finite number of derivatives of g at c, it suÆces to assume that g is a polynomial,

or, more specifically, a product of linear functions: g = `1 : : : `N , `i 2 V . Thus, it
suÆces to be able to compute the series expansion of the integral
Z
−d=2 S(c)=~ −S(x)=~
< `1 : : : `N >:= ~ e `1(x) : : : `N(x)e dx
B
Without loss of generality we may assume that c = 0, and S(c) = 0. Then the
P
B(x;x) Br(x;x;:::;x)
(asymptotic) Taylor expansion of S at c is S(x) = + , where
2 r3 r!
r
Br = d f(0). Therefore, regarding the left hand side as a power series in ~, and
p
making a change of variable x ! x= ~ (like in the last section), we get
Z
B(x;x) P r=2−1 Br(x;:::;x)
< `1 : : : `N >= ~N=2 `1(x) : : : `N(x)e− 2 − r3 ~ r! dx:
V
(This is an identity of expansions in ~, as we ignored the rapidly decaying error
which comes from replacing the box by the whole space).
The theorem below, due to Feynman, gives the value of this integral in terms of
Feynman diagrams. This theorem is easy to prove but is central in quantum field
theory, and will be one of the main theorems of this course. Before formulating this
theorem, let us introduce some notation.
Let G3(N) be the set of isomorphism classes of graphs with N 1-valent “ex-
ternal” vertices, labeled by 1; : : : ; N, and a finite number of unlabeled “internal”
vertices, of any valency  3. Note that here and below graphs are allowed to have
multiple edges between two vertices, and loops from a vertex to itself (see Fig. 2).
For each graph − 2 G3(N), we define the Feynman amplitude of − as follows.
1. Put the covector `j at the j-th external vertex.
2. Put the tensor −Bm at each m-valent internal vertex.
10 MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY
3. Take the contraction of the tensors along edges of −, using the bilinear
−1
form B . This will produce a number, called the amplitude of − and denoted
F−(`1; : : : ; `N).
Remark. If − is not connected, then F− is defined to be the product of num-
bers obtained from the connected components. Also, the amplitude of the empty
diagram is defined to be 1.
Theorem 3.2. (Feynman) One has
d=2 X b(−)
(2) ~
< `1 : : : `N >= p F−(`1; : : : ; `N);
det B jAut(−)j
−2G3(N)
where b(−) is is the number of edges minus the number of internal vertices of −.
(here by an automorphism of − we mean a permutation of vertices AND edges
which preserves the graph structure, see Fig. 3; thus there can exist nontrivial
automorphisms which act trivially on vertices).
Remark 1. Note that this sum is infinite, but ~-adically convergent.
Remark 2. We note that Theorem 3.2 is a generalization of Wick's theorem:
the latter is obtained if S(x) = B(x; x)=2. Indeed, in this case graphs which
−0
N = 0
−1 −2 −3
1 1 2
N = 0 N = 1 N = 2
−4
1 2
N = 2
Figure 2. Elements of G3(N)
?
1
=
Figure 3. An automorphism of a graph
MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY 11
give nonzero amplitudes do not have internal vertices, and thus reduce to graphs
corresponding to pairings .
Let us now make some comments about the terminology. In quantum field
theory, the function < `1 : : : `N > is called the N-point correlation function, and
−1
graphs − are called Feynman diagrams. The form B which is put on the edges is
called the propagator. The cubic and higher terms Bm=m! in the expansion of the
function S are called interaction terms, since such terms (in the action functional)
describe interaction between particles. The situation in which S is quadratic (i.e.,
there is no interaction) is called a free theory; i.e. for the free theory the correlation
functions are determined by Wick's formula.
Remark 3. Sometimes it is convenient to consider normalized correlation func-
tions < `1 : : : `N >norm=< `1 : : : `N > = < ; > (where < ; > denotes the integral
without insertions). Feynman's theorem implies that they are given by the formula
X b(−)
~
< `1 : : : `N >norm= F−(`1; : : : ; `N);
jAut(−)j
−2G (N)
3

where G3(N) is the set of all graphs in G3(N) which have no components without
extrenal vertices.
3.3. Another version of Feynman's theorem. Before proving Theorem 3.2, we
would like to slightly modify and generalize it. Namely, in quantum field theory
it is often useful to consider an interacting theory as a deformation of a free the-
~ ~
ory. This means that S(x) = B(x; x)=2 + S(x), where S(x) is the perturbation
P
~
S(x) = m0 gmBm(x; x; : : : ; x)=m!, where gm are (formal) parameters. Consider
the partition function
Z
−d=2 −S(x)=~
Z = ~ e dx
V
as a series in gi and ~ (this series involves only positive powers of gi but arbitrary
Q
ni
powers of ~; however, the coeÆcient of a given monomial g is a finite sum,
i i
and hence contains only finitely many powers of ~).
Let n = (n0; n1; : : :) be a sequence of nonnegative integers, almost all zero. Let
G(n) denote the set of isomorphism classes of graphs with n0 0-valent vertices, n1
1-valent vertices, n2 2-valent vertices, etc. (thus, now we are considering graphs
without external vertices).
Theorem 3.3. One has
 
d=2 X Y X b(−)
(2) ni ~
Z = p gi F−;
det B jAut(−)j
n i −2G(n)
where F− is the amplitude defined as before, and b(−) is the number of edges minus
the number of vertices of −.
We will prove Theorem 3.3 in the next subsection. Meanwhile, let us show that
Theorem 3.2 is in fact a special case of Theorem 3.3. Indeed, because of symmetry
of the correlation functions with respect to `1; : : : ; `N, it is suÆcient to consider
N
the case `1 =    = `N = `. In this case, denote the correlation function < ` >
N N
(expectation value of ` ). Clearly, to compute < ` > for all N, it is suÆcient to
P N
t` N t
compute the generating function < e >:= < ` > . But this expectation
N!
value is exactly the one given by Theorem 3.3 for gi = 1, i  3, g0 = g2 = 0,
12 MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY
g1 = −~t, B1 = `, B0 = 0, B2 = 0. Thus, Theorem 3.3 implies Theorem 3.2 (note
that the factor N! in the denominator is accounted for by the fact that in Theorem
3.3 we consider unlabeled, rather than labeled, 1-valent vertices – convince yourself
of this!).
3.4. Proof of Feynman's theorem. Now we will prove Theorem 3.3. Let us
p
make a change of variable y = x= ~. Expanding the exponential in a Taylor series,
we obtain
X
Z = Zn;
n
where
Z Y ni
g
−B(y;y)=2 i i=2−1 ni
Zn = e (−~ Bi(y; y; : : : ; y)) dy
V (i!)nini!
i
Writing Bi as a sum of products of linear functions, and using Wick's theorem, we
find that the value of the integral for each n can be expressed combinatorially as
follows.
1. Attach to each factor −Bi a “flower” — a vertex with i outgoing edges (see
Fig. 4).
0-valent flower
1-valent flower
3-valent flower
Figure 4
2. Consider the set T of ends of these outgoing edges (see Fig. 5), and for any
pairing  of this set, consider the corresponding contraction of tensors −Bi using
−1
the form B . This will produce a number F ().
3. The integral Zn is given by
d=2 Y ni X
(2) g i
(9) Zn = p i ~ni(2 −1) F
det B (i!)nini!
i 
Now, recall that pairings on a set can be visualized by drawing its elements as
points and connecting them with edges. If we do this with the set T , all ends of
outgoing edges will become connected with each other in some way, i.e. we will
MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY 13
Figure 5. The set T for ~n = (0; 0; 0; 2; 1; 0; 0; : : :) (the set of white circles)
obtain a certain (unoriented) graph − = − (see Fig. 6). Moreover, it is easy to see
that the number F () is nothing but the amplitude F−.
It is clear that any graph − with ni i-valent vertices for each i can be obtained
in this way. However, the same graph can be obtained many times, so if we want
to collect the terms in the sum over , and turn it into a sum over −, we must find
the number of  which yield a given −.
: r:
Figure 6. A pairing  of T and the corresponding graph −.
14 MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY
For this purpose, we will consider the group G of permutations of T , which
preserves “flowers” (i.e. endpoints of any two edges outgoing from the same flower
end up again in the same flower). This group involves
1) permutations of “flowers” with a given valency;
2) permutation of the i edges inside each i-valent “flower”.
Q Q
ni
More preQcisely, the group G is the semidirect product ( i Sni) n ( i Si ). Note
ni
that jGj = i(i!) ni!, which is the product of the numbers in the denominator of
the formula (9).
The group G acts on the set of all pairings  of T . Moreover, it acts transitively
on the set P− of pairings of T which yield a given graph −. Moreover, it is easy to
see that the stabilizer of a given pairing is Aut(−). Thus, the number of pairings
giving − is
Q
ni
i(i!) ni!
:
jAut(−)j
Hence,
Q
X X ni
i(i!) ni!
F = F−:
jAut(−)j
 −
P
Finally, note that the exponent of ~ in equation (9) is (i=2 − 1), which is the
i
number of edges of − minus the number of vertices, i.e. b(−). Substituting this into
(9), we get the result.
i
Example. Let d = 1, V = R, gi = g, Bi = −z for all i (where z is a formal
variable), ~ = 1. Then we find the asymptotic expansion
Z
1 1 x2 zx X X z2k
p e− 2 +ge = gn ;
2 −1 jAut(−)j
n0 −2G(n;k)
where G(n; k) is the set of isomorphism classes of graphs with n vertices and k
edges. Expanding the left hand side, we get
2 2
X X 2k z n =2
z e
= ;
jAut(−)j n!
k −2G(n;k)
and hence
X 2k
1 n
= ;
k
jAut(−)j 2 k!n!
−2G(n;k)
Exercise. Check this by direct combinatorics.
3.5. Sum over connected diagrams. Now we will show that the logarithm of
the partition function Z is also given by summation over diagrams, but with only
connected diagrams taken into account. This significantly simplifies the analysis
of Z in the first few orders of perturbation theory, since the number of connected
diagrams with a given number of vertices and edges is significantly smaller than
the number of all diagrams.
d=2
(2)
Theorem 3.4. Let Z0 = det(B) . Then one has
X Y X b(−)
ni ~
ln(Z=Z0) = gi F−;
jAut(−)j
n i −2Gc(n)
where Gc(n) is the set of connected graphs in G(n).
MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY 15
Remark. We agree that the empty graph is not connected.
Proof. For any graphs −1, −2, let −1−2 stand for the disjoint union of −1 and −2,
n
and for any graph − let − denote the disjoint union of n copies of −. Then every
k1 kl
graph can be uniquely written as −1 : : : −l , where −j are connected non-isomorphic
graphs. Moreover, it is clear that F−1−2 = F−1F−2, b(−1−2) = b(−1) + b(−2), and
Q
k1 kl kj
jAut(−1 : : : −l )j = j(j(Aut(−j)j kj!). Thus, exponentiating the equation of
Theorem 3.4, and using the above facts together with the Taylor series for the
x
function e , we arrive at Theorem 3.3. As the Theorem 3.3 has been proved, so is
Theorem 3.4 
3.6. Loop expansion. It is very important to note that since summation in The-
orem 3.4 is over connected Feynman diagrams, the number b(−) is the number of
−1
loops in − minus 1. In particular, the lowest coeÆcient in ~ is that of ~ , and
0
it is the sum over all trees; the next coeÆcient is of ~ , and it is the sum over all
diagrams with one loop (cycle); the next coeÆcient to ~ is the sum over two-loop
diagrams, and so on. Therefore, physicists refer to the expansion of Theorem 3.4
as loop expansion.
Let us study the two most singular terms in this expansion (with respect to ~),
i.e. the terms given by the sum over trees and 1-loop graphs.
Let x0 be the critical point of the function S. It exists and is unique, since gi are
(j)
assumed to be formal parameters. Let G (n) denote the set of classes of graphs
in Gc(n) with j loops. Let
X Y X
ni F−
(ln(Z=Z0))j = gi :
jAut(−)j
n i −2G(j)(n)
Theorem 3.5.
(10) (ln(Z=Z0))0 = −S(x0);
and
1 det(B)
(11) (ln(Z=Z0))1 = ln :
00
2 det S (x0)
Proof. First note that the statement is purely combinatorial. This means, in par-
ticular, that it is suÆcient to check that the statement yields the correct asymptotic
expansion of the right hand sides of equations (10),(11). in the case when S is a
PN
polynomial with real coeÆRcients of the form B(x; x)=2 + i=0 giBi(x; x; : : : ; x)=i!.
−d=2 −S(x)=~
To do this, let Z = ~ e , where B is a suÆciently small box around 0.
B
For suÆciently small gi, the function S has a unique global maximum point x0 in
B, which is nondegenerate. Thus, by the steepest descent formula, we have
−S(x0)=~
Z=Z0 = e I(~);
q
det(B) 2
where I(~) = det S00(x0)(1 + a1~ + a2~ +    ) (asymptotically). Thus,
1 det(B)
−1
ln(Z=Z0) = −S(x0)~ + ln + O(~):
00
2 det S (x0)
This implies the result. 
16 MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY
Physicists call the expression (ln(Z=Z0))0 the classical (or tree) approxima-
tion to the quantum mechanical quantity ~ ln(Z=Z0), and the sum (ln(Z=Z0))0 +
~(ln(Z=Z0))1 the one loop approximation. Similarly one defines higher loop approx-
imations. Note that the classical approximation is obtained by finding the critical
point and value of the classical action S(x), which in the mechanics and field theory
situation corresponds to solving the classical equations of motion.
3.7. Nonlinear equations and trees. As we have noted, Theorem 3.5 does not
involve integrals and is purely combinatorial. Therefore, there should exist a purely
combinatorial proof of this theorem. Such a proof indeed exists. Here we will give
a combinatorial proof of the first statement of the Theorem (formula (10)).
0
Consider the equation S (x) = 0, defining the critical point x0. This equation
can be written as x = fi(x), where
X
^−1
fi(x) := − giB Bi(x; x; : : : ; x; ?)=(i − 1)!;
i1
^−1  −1
where B : V ! V is the operator corresponding to the form B .
In the sense of power series norm, fi is a contracting mapping. Thus, x0 =
N
limN!1 fi (x), for any initial vector x 2 V . In other words, we will obtain x0 if
we keep substituting the series fi(x) into itself. This leads to summation over trees
(explain why!). More precisely, we get the following expression for x0:
X Y X
ni F−
x0 = ( gi ) ;
jAut(−)j
n −2G(0)(n;1)
(0)
where G (n; 1) is the set of trees with one external vertex and ni internal vertices
P
of degree i. Now, since S(x) = B(x; x)=2 + giBi(x; x; : : : ; x)=i!, the expression
Q
ni F−
−S(x0) equals the sum of expressions ( gi )jAut(−)j over all trees (without exter-
nal vertices). Indeed, the term B(x0; x0)=2 corresponds to gluing two trees with
external vertices (identifying the two external vertices, so that they disappear); so
it corresponds to summing over trees with a marked edge, i.e. counting each tree
as many times as it has edges. On the other hand, the term giBi(x0; : : : ; x0)=i!
corresponds to gluing i trees with external vertices together at the external vertices
P
(making a tree with a marked vertex). So giBi(x0; : : : ; x0)=i! corresponds to
summing over trees with a marked vertex, i.e. counting each trees as many times
as it has vertices. But the number of vertices of a tree exceeds the number of edges
by 1. Thus, the difference −S(x0) of the above two contributions corresponds to
summing over trees, counting each exactly once. This implies formula (10).
3.8. Counting trees and Cayley's theorem. In this section we will apply The-
orem 3.5 to tree counting problems, in particular will prove a classical theorem due
n−2
to Cayley that the number of labeled trees with n vertices is n .
We consider essentially the same example as we considered above: d = 1, Bi =
2
x x
−1, gi = g. Thus, we have S(x) = 2 − ge . By Theorem 3.5, we have
X X
1
n
g = −S(x0);
jAut(−)j
n0 −2T(n)
where T (n) is the set of isomorphism classes of trees with n vertices, and x0 is the
0 x
root of the equation S (x) = 0, i.e. x = ge .
MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY 17
−x
In other words, let f(z) be the function inverse to xe near x = 0. Then we
have x0 = f(g). Thus, let us find the Taylor expansion of f. This is given by the
following classical result.
Proposition 3.6. One has
X n−2
n
n
f(g) = g :
(n − 1)!
n1
P
n
Proof. Let f(g) = n1 ang . Then
I I
1 f(g) 1 x
−x
an = dg = d(xe ) =
n+1 −x n+1
2i g 2i (xe )
I
n−1 n−2 n−2
1 1 − x n n n
nx
e dx = − = :
n
2i x (n − 1)! (n − 2)! (n − 1)!

Now we find
2 f(g)
−S(x0) = −f(g) =2 + ge :
Thus
f(g)
0 f(g) 0 f(g) f(g)
−(d=dg)S(x0) = −f(g)f (g) + ge f (g) + e = e = :
g
This means that
Z
g X n−2
f(a) n
n
−S(x0) = da = g :
0 a n!
n1
This shows that
X n−2
1 n
=
jAut(−)j n!
−2T(n)
n!
But each isomorphism class of unlabeled trees with n vertices has noniso-
jAut(−)j
morphic labelings. Thus the latter formula implies
n−2
Corollary 3.7. (A. Cayley) The number of labeled trees with n vertices is n .
3.9. Counting trees with conditions. In a similar way we can count labeled
trees with conditions on vertices. For example, let us compute the number of
labeled trivalent trees with m vertices (i.e. trees that have only 1-valent and 3-
valent vertices). Clearly, m = 2k, otherwise there is no such trees. The relevant
2
x 3
action functional is S(x) = 2 − g(x + x =6). Then the critical ppoint x0 is obtained
2 1− 1−2g2
from the equation g(x =2 + 1) − x = 0, which yields x0 = g . Thus, the
tree sum (ln(Z=Z0))0 equals
2 3=2
1 − (1 − 2g )
(ln(Z=Z0))0 = −S(x0) = − 1:
2
3g
Expanding this in a Taylor series, we find
1
X
1  3      (2n − 1)
2n+2
(ln(Z=Z0))0 = g
(n + 2)!
n=0
Hence, we get
18 MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY
Corollary 3.8. The number of trivalent labeled trees with m = 2k vertices is
(2k)!
(2k − 3)!! .
(k+1)!
3.10. Counting oriented trees. Feynman calculus can be used to count not only
non-oriented, but also oriented graphs. For example, suppose we want to count
labeled oriented trees, whose vertices are either sources or sinks (see Fig. 7). In
this case, it is easy to see (check it!) that the relevant integration problem is in two
x y
dimensions, with the action S = xy − be − ae . So the critical point is found from
the equations
−y −x
xe = a; ye = b:
Like before, look for a solution (x; y) = (x0; y0) in the form
X X
p q p q
x = a + cpqa b ; y = b + dpqa b :
p1;q1 p1;q1
A calculation with residues similar to the one we did for unoriented trees yields
I I I I
qx+py p−1 q−1
1 x 1 e q p
cpq = da^db = (1−xy)dx^dy = :
2 p+1 q+1 2 p q+1
(2i) a b (2i) x y (p − 1)!q!
p−1 q−1
q p
Similarly, dpq = p!(q−1)! . Now, similarly to the unoriented case, we find that
−acaS(x; y) = x, −bcbS(x; y) = y, so
Z a X q−1 p−1
x p q
p q
−S(x; y) = b + du = a + b + a b
0 u p!q!
p;q1
This implies that the number of labeled trees with p sources and q sinks is
q−1 p−1 (p+q)!
p q . In particular, if we specify which vertices are sources and which
p!q!
q−1 p−1
are sinks, the number of trees is p q .
3.11. 1-particle irreducible diagrams and the effective action. Let Z = ZS
be the partition function corresponding to the action S. In the previous subsections
we have seen that the “classical” (or “tree”) part (ln(ZS=Z0))0 of the quantity
ln(ZS=Z0) is quite elementary to compute – it is just minus the critical value of the
action S(x). Thus, if we could find a new “effective” action Seff (a “deformation”
of S) such that
(ln(ZSeff =Z0))0 = ln(ZS=Z0)
-
1 4
q
-
2 5
s
-
3 6
Figure 7. A labeled oriented tree with 3 sources and 3 sinks.
MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY 19
(i.e. the classical answer for the effective action is the quantum answer for the
original one), then we can regard the quantum theory for the action S as solved. In
other words, the problem of solving the quantum theory attached to S (i.e. finding
the corresponding integrals) essentially reduces to the problem of computing the
effective action Seff.
We will now give a recipe of computing the effective action in terms of amplitudes
of Feynman diagrams.
Definition 3.9. An edge e of a connected graph − is said to be a bridge, if the
graph − n e is disconnected. A connected graph without bridges is called 1-particle
irreducible (1PI).
Remark. This is the physical terminology. The mathematical terminology is
“2-connected”.
To compute the effective action, we will need to consider graphs with external
edges (but having at least one internal vertex). Such a graph − (with N external
edges) will be called 1-particle irreducible if so is the corresponding “amputated”
graph (i.e. the graph obtained from − by removal of the external edges). In partic-
ular, a graph with one internal vertex is always 1-particle irreducible (see Fig. 8),
while a single edge graph without internal vertices is defined not to be 1-particle
irreducible.
not a bridge


6
a bridge
1PI graph with
two external edges
non-1PI graph with
four external edges
Figure 8
Let us denote by G1−irr(n; N) the set of isomorphism classes of 1-particle irre-
ducible graphs which N external edges and ni i-valent internal vertices for each i
(where isomorphisms are not allowed to move external edges).
20 MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY
Theorem 3.10. The effective action Seff is given by the formula
X
B(x; x) Bi
Seff(x) = − ;
2 i!
i0
where
X Y X b(−)+1
ni ~
BN (x; x; : : : ; x) = ( gi ) F−(x; x; : : : ; x);
jAut(−)j
n i −2G1−irr(n;N)

where x 2 V is defined by x(y) := B(x; y)
2 j
Thus, Seff = S + ~S1 + ~ S2 + :: The expressions ~ Sj are called the j-loop
corrections to the effective action.
This theorem allows physicists to worry only about 1-particle irreducible dia-
grams, and is the reason why you will rarely see other diagrams in a QFT textbook.
As before, it is very useful in doing low order computations, since the number of
1-particle irreducible diagrams with a given number of loops is much smaller than
the number of connected diagrams with the same number of loops.
Proof. The proof is based on the following lemma from graph theory.
Lemma 3.11. Any connected graph − can be uniquely represented as a tree, whose
vertices are 1-particle irreducible subgraphs (with external edges), and edges are the
bridges of −.
The lemma is obvious. Namely, let us remove all bridges from −. Then − will
turn into a union of 1-particle irreducible graphs, which should be taken to be the
vertices of the said tree.
The tree corresponding to the graph − is called the skeleton of − (see Fig. 9).
Graph: Skeleton:
Figure 9. The skeleton of a graph.
It is easy to see that the lemma implies the theorem. Indeed, it implies that
the sum over all connected graphs occuring in the expression of ln(ZS=Z0) can be
written as a sum over skeleton trees, so that the contribution from each tree is
(proportional to) the contraction of tensors Bi put in its vertices, and Bi is the
(weighted) sum of amplitudes of all 1-particle irreducible graphs with i external
edges. 
MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY 21
3.12. 1-particle irreducible graphs and the Legendre transform. Recall the
notion of Legendre transform.

Let f be a smooth function on a vector space Y , such that the map Y ! Y given
by x ! df(x) is a diffeomorphism. Then one can define the Legendre transform of

f as follows. For p 2 Y , let x0(p) be the critical point of the function (p; x) − f(x)
(i.e. the unique solution of the equation df(x) = p). Then the Legenedre transform

of f is the function on Y defined by
L(f)(p) = (p; x0) − f(x0):

It is easy to see that the differential of L(f) is also a diffeomorphism Y ! Y (in
2
fact, inverse to df(x)), and that L (f) = f.
2 2
Example. Let f(x) = ax =2. Then px − f = px − x =2 has a critical point at
2 2 2
p = x=a, and the critical value is p =2a. L(ax =2) = p =2a. Similarly, if f(x) =
−1
B(x; x)=2 where B is a nondegenerate symmetric form, then L(f)(p) = B (p; p)=2.
Now let us consider Theorem 3.10 in the situation of Theorem 3.2. Thus, S(x) =
3
B(x; x)=2 + O(x ), and we look at
Z
Jx−S(x)
Z(J) = ~−d=2 e ~ dx
V
By Theorem 3.10, one has
ln(Z(J)=Z0) = −Seff(x0; J);
where the effective action Seff(x; J) given by summation over 1-particle irreducible
graphs.
Now, we must have Seff(x; J) = −J  x + Seff(x), since the only 1PI graph which
contains 1-valent internal vertices (corresponding to J) is the graph with one edge,
connecting an internal vertex with an external one (so it yields the term −J x, and
other graphs contain no J-vertices). This shows that ln(Z(J)=Z0) is the critical
value of J  x − Seff(x). Thus we have proved the following.
Proposition 3.12. We have
Seff(x) = L(ln(Z(J)=Z0)); ln(Z(J)=Z0) = L(Seff(x)):
Physicists formulate this result as follows: the effective action is the Legendre
transform of the logarithm of the generating function for quantum correlators (and
vice versa).
