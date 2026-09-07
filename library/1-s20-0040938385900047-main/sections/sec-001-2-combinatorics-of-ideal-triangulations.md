---
doc_id: 1-s20-0040938385900047-main
doc_title: "ToporoPy Vol. 24, No. 3, pp. 307-332. 1985. 0040-9383185 s3.00+ .OO Printed III Great Britain. C 1985. Pcrgamon Press Ltd. VOLUMES OF HYPERBOLIC THREE-MANIFOLDS"
section_id: sec-001-2-combinatorics-of-ideal-triangulations
section_title: "Combinatorics of ideal triangulations"
section_number: 2
pages: 4-10
source_pdf: 1-s2.0-0040938385900047-main.pdf
source_sha256: f0db9d97f2ae83c6
doc_brief: "ToporoPy Vol. 24, No. 3, pp. 307-332. 1985. 0040-9383185 s3.00+ .OO Printed III Great Britain. C 1985. Pcrgamon Press Ltd. VOLUMES OF HYPERBOLIC THREE-MANIFOLDS — 7 sections: Introduction; Combinatori"
---
hyperbolic 3-manifolds, which we describe in 92. Our main combinatorial results, Theorem 
2.2, is a general property of “triangulations” with no 0-simplicies of open 3-manifolds and 
should be a useful tool for other purposes. 
52. COMBINATORICS OF IDEAL TRIANGULATIONS 
The hyperbolic objects whose volumes are best understood are ideal tetrahedra (geodesic 
tetrahedra with all vertices at infinity). To study the volume of our manifold M, it would be 
useful if we could decompose it into such tetrahedra, i.e., tetrahedra whose vertices are at the 
cusps of M. This is in general not possible. However, Thurston [S] has shown that any 
hyperbolic 3-manifold is obtainable from an ideally triangulated one by Dehn surgeries on 
some of the cusps. We therefore will assume that M is the result of k - h Dehn surgeries on a 
manifold N with k cusps which is triangulated as 
N = S, v . . . v S,. 
where each S, is a tetrahedron with its vertices deleted 
(14) 
VOLUMES OF HYPERBOLIC THREE-MANIFOLDS 311 
The triangulation in (1) is going to be considered as a purely topological one, i.e. as a 
combinatorial triangulation of an open 3-manifold N homeomorphic to the interior of a 
compact manifold with a boundary consisting of k tori. Thus N has k “toral” ends. We are 
going to put the structure of an ideal hyperbolic tetrahedron on each S,, imposing the 
compatibility conditions required to give N a smooth but not necessarily complete 
hyperbolic structure. We will then impose further conditions, corresponding to the Dehn 
surgeries at k - h of the ends of N, which say that these ends can be completed by adding a 
circle to give a smooth neighborhood of a closed geodesic. The remaining h ends of N will 
initially be complete, and thus have the structure of true hyperbolic cusps; this corresponds to 
the initial manifold M of the introduction. The manifolds M, are obtained by deforming the 
hyperbolic structures on the tetrahedra S, away from this initial position. To describe the 
situation more accurately we must introduce some notation. 
A general reference for hyperbolic triangulations, compatibility conditions, etc., is 
Thurston [7, Chapter 43. The reader may wish to refer to’the example in section 6 while 
reading the following general discussion. 
We remind the reader that an ideal tetrahedron S is described completely (up to isometry) 
by a single complex number z in the upper half plane such that the euclidean triangle cut out 
ofany vertex of S by a horosphere section is similar to the triangle in C with vertices 0,l and z. 
We write S = S(z). The numbers z, 1 - (l/z) and l/(1 -I) give the same tetrahedron; to 
specify z uniquely, we must pick an edge of S (the dihedral angle at this edge wil be arg (z)). 
We make such a choice for each S, and write 
S Y = S(G) 
Then to each edge of S, is associated one of the three numbers 
(v = 1, . . . ) n). 
1 1 z V 1---, and 
2, 1’ (15) 
the modulus of the edge, opposite edges of S, having the same modulus (see Fig. 1). The 
necessary and sufficient condition that (1) gives a (not necessarily complete) hyperbolic 
manifold is that at each edge e of N the tetrahedra S, abutting e “close up”as one goes around 
e (Fig. 2) and thus that the product of the corresponding moduli of the S, at e is e2ni (here the 
Fig. 1. 
312 Walter D. Neumann and Don Zagier 
Fig. 2. 
product is to be taken in the universal covering c* of C*, that is, the sum of the arguments 
should be exactly 27r). From (15) we see that these moduli have the form 
kzt(l -zJ”’ with (r’, r”)E { (l,O), (- 1, l), (0, -l)}, so the gluing condition at edge e gives 
(computing now only in C*) 
fi z$(l-z,)‘Y= &l 
v=l 
for some integers rl, rt depending on e (notice that r\and rt are not necessarily still I 1 in 
absolute value since more than one edge of S, may coincide with edge e of N). The fact that N 
has Euler characteristic zero (N is the interior of a compact 3-manifold with boundary a 
union of tori) implies by a simple calculation that the number of edges is equal to the number 
n of tetrahedra. We number the edges by an index j and write the edge relations as 
i z:;~(l-z,)‘~~= fl (i=l,...,n) (16) v=1 
Once we have chosen the numbers z, (satisfying the compatibility conditions), N acquires 
a smooth hyperbolic structure, in general incomplete. We need additional conditions to 
ensure that the completion of N is M. The torus Tassociated to any one of the k ends of N has 
a similarity structure given by its triangulation into the (0, 1, z) triangles cut off by 
horospheres at the vertices of the S,. To each vertex of each triangle of this triangulation is 
associated a number p, the modulus of the corresponding edge. If y is an oriented closed 
simplicial path, we define ~(7) to be ( - l)h” times the product of these moduli for the triangle 
vertices touching y on the right, where lyl is the number of 1-simplices of y (see Fig. 3). 
LEMMA 2.1. The number ME C* depends only on the homotopy class of y and defines a 
homomorphism 7c1 (T) = H, (T) + C*. 
Proof. In fact, the similarity structure on T defines a holonomy homomorphism n, (T) 
+ Sim ( E2) = Aff (C) and p(y) is just the derivative of the holonomy of the element of ~ci (T) 
represented by y (see [7, $4]), from which the lemma follows. However, there is a direct 
combinatorial proof: any deformation of y within its homotopy class can be obtained by 
successive elementary steps of the type illustrated in Fig. 4, and since the product of moduli 
Fig. 3. 
VOLUMES OF HYPERBOLIC THREE-MANIFOLDS 313 
Fig. 4. 
around a vertex is + 1 (the consistency condition at an edge) and the product of moduli of the 
vertices of a triangle is - 1 (cf. (1 S)), the lemma follows. n 
Notice that p is actually obtained from a homomorphism @:H, (T) 4 c*, obtained by 
considering the moduli in c* and replacing ( - l)‘Y1 by e-“’ 1~1. The condition that the end of N 
corresponding to the torus T is complete, i.e. a true hyperbolic cusp, is that ji be trivial, since 
this exactly says that the similarity structure on Tis euclidean. On the other hand, at the k - h 
Dehn surgered ends, one primitive element [y] E H 1 (T) has been killed by Dehn surgery and 
the fi of this y must be e *2xi. In particular p(y) = 1, and since p(y) is a product of edge moduli, 
each of which is one of the numbers (15), this relation takes the form 
Since this relation has exactly the same form as the consistency relations at edges (16), we use 
the same letter j to index surgered ends as we used for edges (with j now ranging from n + 1 
to n + k - h) and write the complete set of necessary conditions in the uniform form 
V~lz$(l-z,)‘~~= +l ,(j= l,...,n+k-h). (17) 
We note that these are only necessary conditions and not sufficient, since we are considering 
them in Q=* rather than c*. However, if we start at the value z” = (~7, . . . , zz)corresponding 
to the hyperbolic structure on M and deform z = (z,, . . , z,) preserving conditions (17), 
then, of course, the corresponding e* conditions are preserved, so we do get a deformation of 
the hyperbolic structure on M. 
We write N(z) for N with the hyperbolic structure determined by z = (z,, . . . , zy) 
satisfying the compatibility conditions. Thus M is the completion of N (z’) and the M, and 
M, of the Introduction are completions of suitable N(z). 
The h unsurgered cusps of N (z’), corresponding to the cusps of M, will be indexed by the 
letter i, 1 I i < h. Corresponding to the basis Li, “cti of HI (&) fixed in section 1, we have for 
this manifold additional relations I = 1, p(mi) = 1, (i = 1, . . . , h) as explained above, 
and again these can be written in the form 
Vfil(z~)‘:~(l-z~)‘:~=+I (i=l,...,h) (18) 
fi (~t)~;*(l -z:)~;= +l (i = 1, . . ,h) (19) 
v=l 
for some integers I;,, 111, I&, ml: (which are well defined, however, only after choosing closed 
simplicial curves on the T representing the homology classes di, +). 
We write L’, L", M', M", R', R" for the integer matrices (I:,), (I::), . . . , (rJy), (r;[y), and 
combine them into a single (n + k + h) x 2n matrix U as follows 
llvln l<v<n 
u= ;, 
i 
L” Illilh 
M" }lsilh (20) 
R' R" }lljsn+k-h 
314 Walter D. Neumann and Don Zagier 
where for convenience we recall our notational conventions: 
v + tetrahedra; ’ + Z”, ” + 1 -z,, (1 I v < n) 
i + unsurged cusps (1 I i I h) 
j + edges (1 I j I n) and surgered cusps (n < j I n + k - h). 
We also write L for the h x 2n matrix (L’, L”) and similarly M = (M’, M”), R = (R’, R”), so 
L 
U= M . 
0 
For any natural number m, denote by Jzm the symplectic matrix 
Jzm=(’ R InI 
-I, 0 ) . 
The fundamental fact about the combinatorics of our triangulation is the following result. 
THEOREM 2.2. Let U E Mn+h+L, Zn (E) be the matrix defined in (20). Then 
(21) 
The proof, which is rather long, is postponed to $3. 
For any matrix A with 2n columns we shall denote by [A] c Iw2” the row-space of A, that 
is, the subspace of [w2” generated by the rows of A. On (w2” we have the symplectic form 
C&Y> = +x J,,y’ 
Let C denote the matrix C = (,&), so U = (i). The content of Theorem 2.2 is that [U] is 
orthogonal (w.r.t. <, > ) to [R] and that the rows of C form a symplectic basis of [C]; in 
particular C has maximal rank, namely rank C = 2h. 
PROPOSITION 2.3. Rank R = n - h and rank U = n + h. Moreover, if I denotes orthogonal 
complement with respect to <, > then [U] ’ = [R]. 
Proof. The representation [U] = [C] + [R] is an orthogonal sum, so dim [U] 
= dim [C] + dim[R] = 2h + dim [R]. On the other hand, since [R] c [U] ‘, we have 
dim[R] Idim[U]‘= 2n-dim[U] = 2n-2h-dim[R], so dim[R] I n-h and 
equality holds if and only if [R] = [U] I. Thus it suffices to show dim [R] 2 n - h. 
Since dim [R] I n - h, at most n - h of the consistency relations (17) are independent, so. 
these relations determine a subvariety V c 63” of dimension at least h. We claim V has 
dimension exactly h at the point z” = (zy, . . . , zf). (This re-proves a result of Thurston [7, 
$51.) To show this, it suffices to show that the subvariety W of I/defined by the h additional 
relations 
“Dl d”U -z,)‘:= +l (i=l,...,h) 
(obtained by replacing zy by z, in (18)) has dimension 0 at z”. These h relations specify that the 
holonomies of the longitudes ei are parabolic. Since the holonomies of Gi and +PQ commute, 
mi then also has parabolic holonomy for each i, so the parameter z E W corresponds to the 
complete hyperbolic structure on M, which is unique by Mostow rigidity. Thus, if W had 
positive dimension, the ideal triangulation of M could be deformed. But this is impossible, 
since there are only countably many ideal triangulations of M (since there are only countably 
many geodesics in M which are asymptotic to either a cusp or a closed geodesic in each 
direction). 
Since V has dimension h at z”; we can pick a nearby point z = (z,, . . , zn) where V has 
dimension h and is nonsingular (in fact, as we shall see in $4, z = z” is such a point). We 
VOLUMES OF HYPERBOLIC THREE-MANIFOLDS 
rewrite the relations defining V as 
i (r~,logz,+r~Vlog(l-z,))=const. (=log(+l)) (j= 1,. . . ,n+k-h). 
v=l 
The Jacobian of this system of equations at z is RZ, where 
1 - 
/. 
21 
. . . 0 
\ 
0 i - 
Z” 
z= 
-1 
1 -zr . . . 0 
\: 
0 
Thus rank (RZ) = n - h, so rank R 2 n - h, as desired. 
-1 . . . 
-1 1 -z, 
315 
The following corollary will be the fundamental tool for proving the volume formulae. 
COROLLARY 2.4. Suppose x, YE Iw2” satisfy Rx’ = Ry’ = 0, Then xJ,,y’ = jxC’J,,,Cy’. 
Proof. Since 0 = Rx’ = R Jzn(x J2,,)’ the vector xJ,, is in [R] ‘, so by Proposition 2.3 we 
have xJZnc [VI, that is, xJzn = ZU for some ZE Rn+k+h. Also UJ,,C’ = 2(k) by Theorem 
2.2, so XC’ = -xJ;,C’ = -2z(k).Thus $xC’J~~C~’ = -Z($")J,,cy' = z(,c)y'= z(;)y' 
=zuyf= xJ2,yf, as desired. 
We close this section with a digression, namely to describe how the k relations between the 
rows of R, which must exist by Proposition 2.3, can be described explicitly in terms of the 
combinatorics. In fact these k relations occur among the first n rows of R, that is, the rows 
which correspond to edges of the triangulation. We denote the submatrix consisting of these 
rows by RO. We define a matrix X = (xV)r <i<k, 1 sj<n, where, for the purpose of this 
discussion, the index i indexes all ends of N rather than only the unsurgered ones, by letting 
xij E (0, 1,2) be the number of ends of the j-th l-simplex which terminate at the i-th end of N. 
PROPOSITION 2.5. XR, = 0 and X has (maximal) rank k. 
Proof. To see that XR, = 0 we must show 
for each torus K and tetrahedron S,. Each nonzero product xijr;V in (22) corresponds to an 
edge of S, which ends at the i-th cusp. Hence (22) is trivially true if none of the four vertices of 
S, is at this cusp. If S, does have a vertex at the i-th cusp, then there will be three edges jl, j2, j, 
contributing to (22) (see Fig. 5). They will each contribute 1 to Xij and will contribute (1, 0), 
(- 1, l), (0, - l), respectively, to (ri,,, ryv) by (1.5). Since (LO) + ( - 1, 1) + (0, - 1) = (O,O), (22) 
follows. 
To show that X has maximal rank, we show that XX’ is positive definite, i.e. that the 
auadratic form 
5 = (51,. . , 5,)” i i f: Xijxi’jtiti’ 
i=l i’c1 j=1 
(23) 
316 Walter D. Neumann and Don Zagier 
I; 
I’ /I 
; 
: 
,I’ h J2 , \ -_-9,’ 
/’ \ .‘, 
I’ 1, 1 .I’ 
/’ J3 
Fig. 5. 
is positive for { # 0. Since each edge has two ends, we have for each j either 
%(i)i = Xi2(j)j = 1, .Xij =0 fori${i,(j),i,(j)} withi,(j)#i,(j) 
or 
Xi, (j)j = 2, Xv = 0 for i # i,(j). 
In the second case we write i,(j) = i, (j). Then the right hand side of (23) equals 
i (<i,(j) + 5il(j)Jz 
j=l 
since i and i’ range over {il (j), i, (j)}. This can be zero only if ti has opposite sign at the two 
ends of every edge, and looking at any 2-simplex of the triangulation we see that this implies 
ti = 0 for all i. n
