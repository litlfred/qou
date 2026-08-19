---
doc_id: agt-v3-n1-p17-p
doc_title: "Published: 16 June 2003 Skein-theoretical derivation of some formulas of Habiro Gregor Masbaum"
section_id: sec-004-3-graphical-calculus-and-a-formula-for-p
section_title: "Graphical calculus and a formula for !p"
section_number: 3
pages: 9-12
source_pdf: agt-v3-n1-p17-p.pdf
source_sha256: df196f0a732ad6b9
doc_brief: "Skein-theoretical derivation of some formulas of Habiro Gregor Masbaum — We use skein theory to compute the coecients of certain power series considered by Habiro in his theory ofsl2 invariants of"
---
Let us write ! =!+ and put
!p =
1X
n=0
cn;pRn : (23)
Note that the coecients cn;p are well-de
ned (because Rn divides Rn+1 and
therefore the coecients Ck
n;m in the product expansion RnRm =P
kCk
n;mRk
are zero if n or m is bigger than k.) We have
h!p;xi =htp(x)i (24)
for every even x. (This follows from (6) since circling with !p i st h es a m ea s
circling with p parallel copies of !.) Of course, cn;1 = cn;+ and cn;−1 = cn;−
(it follows from the uniqueness of !−that !−=!−1 ). The aim of this section
is to give a formula for the coecients cn;p (see Theorem 3.2 below).
We use the extension of the Kau
man bracket to admissibly colored banded
trivalent graphs as in [MV]. (Such graphs are sometimes called spin networks;
for more background see e.g. [KL] and references therein.) A color is just an
integer 0. A triple of colors ( a;b;c )i s admissible if a +b +c 0( m o d2 )
andja−bj c a +b.L e t D be a planar diagram of a banded trivalent
graph. An admissible coloring of D is an assignment of colors to the edges
of D so that at each vertex, the three colors meeting there form an admissible
triple. The Kau
man bracket of D is de
ned to be the bracket of the expansion
of D obtained as follows. The expansion of an edge colored n consists of n
parallel strands with a copy of the Jones-Wenzl idempotent f
n inserted. (The
idempotentfn is characterized by the fact thatxfn =fnx = 0 for every element
x of the standard basis of the Temperley-Lieb algebra other than the identity
element; here, the standard basis consists of the (n;n )-tangle diagrams without
crossings and without closed loops.) The expansion of a vertex is de
ned as in
Fig. 2, where the internal colors i;j;k are de
ned by
i =(b +c−a)=2;j =(c +a−b)=2;k =(a +b−c)=2 : (25)
We have the fusion equation
b
a
=
X
c
hci
ha;b;ci b
a
c b
a (26)
Algebraic &GeometricTopology, Volume 3 (2003)
546 Gregor Masbaum
n
=

 ,
ab
c
=
ab
c
k
ij
Figure 2: How to expand colored edges and vertices. The boxes stand for appropriate
Jones-Wenzl idempotents.
Here the sum is over those colors c so that the triple (a;b;c ) is admissible, we
havehci =heci =(−1)c[c + 1], and the trihedron coecient ha;b;ci is (see
[MV, Thm. 1]):
ha;b;ci = a
c
b =(−1)i+j+k [i +j +k +1 ] ![i]! [j]! [k]!
[a]! [b]! [c]! (27)
(here i;j;k are the internal colors as de
ned in (25)). Note that hn;n; 2ni =
h2ni so that
n
n
=
n
n
2n n
n + ::: (28)
We will need the following lemma.
Lemma 3.1 For 0kn, one has
2n
2n
n
n
n
n 2k = ([k]!)2
[2k]!
2n
Proof This follows from the formula for the tetrahedron coecient given in
[MV, Thm. 2]. (The sum over  in that formula reduces to just one term.)
The key observation is that
2n
2n
n
n
Rk =0 f o r k6=n: (29)
Algebraic &GeometricTopology, Volume 3 (2003)
Skein-theoretical derivation of some formulas of Habiro 547
Indeed, if k<n , there are at most 2 k vertical strands in the middle and so
the result is zero because of the Jones-Wenzl idempotents f2n at the top and
bottom. On the other hand, if k>n , the result is zero because Rk annihilates
all even polynomials in z of degree < 2k.
If k =n one 
nds
2n
2n
n
n
Rn =(−1)n(fng!)2
2n
: (30)
Indeed, applying (28), one has
2n
2n
n
n
Rn =
2n
2n
n
n
Rn
2n = hRn;e 2ni
he2ni
2n
2n
n
n
n
n 2n
hence (30) follows from (5) and Lemma 3.1.
On the other hand, since circling with !p induces p full twists on even numbers
of strands (see (24)), we have, using (29), that
−2p
n cn;p
2n
2n
n
n
Rn =−2p
n
2n
2n
n
n
!p =
2n
2n
n
n
 (31)
where there are 2p crossings in the last diagram. (See (3) for the twist eigen-
values i .) Applying the fusion equation (26), we have
2n
2n
n
n
 =
nX
k=0
(2k;n;n )2p h2ki
hn;n; 2ki
2n
2n
n
n
n
n 2k (32)
where (c;a;b )i st h e half-twist coecient de
ned by
a
b
c =(c;a;b )
a
b
c :
Algebraic &GeometricTopology, Volume 3 (2003)
548 Gregor Masbaum
This coecient is computed in [MV, Thm. 3]. For us, it is enough to know
that
(c;a;b )2 = c
ab
which is easy to see. Using (30) and Lemma 3.1, it follows that
−2p
n cn;p(−1)n(fng!)2 =
nX
k=0
p
2k
2p
n
h2ki
hn;n; 2ki
([k]!)2
[2k]! :
The factors of −2p
n cancel out, and in view of (27), this gives the following
result:
Theorem 3.2 The coecients cn;p of !p in (23) are given by
cn;p = 1
(a−a−1)2n
nX
k=0
(−1)kp
2k[2k +1 ]
[n +k +1 ] ![n−k]! : (33)
