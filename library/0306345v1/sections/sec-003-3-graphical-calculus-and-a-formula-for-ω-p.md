---
doc_id: 0306345v1
doc_title: "Published: 16 June 2003 Skein-theoretical derivation of some formulas of Habiro Gregor Masbaum"
section_id: sec-003-3-graphical-calculus-and-a-formula-for-ω-p
section_title: "Graphical calculus and a formula for ω p"
section_number: 3
pages: 9-12
source_pdf: 0306345v1.pdf
source_sha256: 936aa08026b2683b
doc_brief: "Skein-theoretical derivation of some formulas of Habiro — We use skein theory to compute the coecients of certain power series considered by Habiro in his theory ofsl2 invariants of integral homol"
duplicate_of: "agt-v3-n1-p17-p"
---
Let us write ω = ω + and put
ω p =
∞∑
n=0
cn,p Rn . (23)
Note that the coeﬃcients cn,p are well-deﬁned (because Rn divides Rn+1 and
therefore the coeﬃcients C k
n,m in the product expansion RnRm =∑
k C k
n,m Rk
are zero if n or m is bigger than k .) We have
⟨ω p, x ⟩ = ⟨tp(x)⟩ (24)
for every even x. (This follows from (6) since circling with ω p is the same as
circling with p parallel copies of ω .) Of course, cn, 1 = cn, + and cn, −1 = cn, −
(it follows from the uniqueness of ω − that ω − = ω −1 ). The aim of this section
is to give a formula for the coeﬃcients cn,p (see Theorem 3.2 below).
We use the extension of the Kauﬀman bracket to admissibly colo red banded
trivalent graphs as in [MV]. (Such graphs are sometimes call ed spin networks;
for more background see e.g. [KL] and references therein.) A color is just an
integer ≥ 0. A triple of colors ( a, b, c ) is admissible if a + b + c ≡ 0 (mod 2)
and |a − b| ≤ c ≤ a + b. Let D be a planar diagram of a banded trivalent
graph. An admissible coloring of D is an assignment of colors to the edges
of D so that at each vertex, the three colors meeting there form an admissible
triple. The Kauﬀman bracket of D is deﬁned to be the bracket of the expansion
of D obtained as follows. The expansion of an edge colored n consists of n
parallel strands with a copy of the Jones-Wenzl idempotent fn inserted. (The
idempotent fn is characterized by the fact that xfn = fnx = 0 for every element
x of the standard basis of the Temperley-Lieb algebra other th an the identity
element; here, the standard basis consists of the ( n, n )-tangle diagrams without
crossings and without closed loops.) The expansion of a vert ex is deﬁned as in
Fig. 2, where the internal colors i, j, k are deﬁned by
i = (b + c − a)/ 2, j = (c + a − b)/ 2, k = (a + b − c)/ 2 . (25)
We have the fusion equation
b
a
=
∑
c
⟨c⟩
⟨a, b, c ⟩ b
a
c b
a (26)
Algebraic & Geometric Topology, Volume 3 (2003)
546 Gregor Masbaum
n
=
· · ·
· · · ,
a b
c
=
a b
c
k
ij
Figure 2: How to expand colored edges and vertices. The boxes sta nd for appropriate
Jones-Wenzl idempotents.
Here the sum is over those colors c so that the triple ( a, b, c ) is admissible, we
have ⟨c⟩ = ⟨ec⟩ = ( −1)c[c + 1], and the trihedron coeﬃcient ⟨a, b, c ⟩ is (see
[MV, Thm. 1]):
⟨a, b, c ⟩ =
a
c
b = (−1)i+j+k [i + j + k + 1]! [i]! [j]! [k]!
[a]! [b]! [c]! (27)
(here i, j, k are the internal colors as deﬁned in (25)). Note that ⟨n, n, 2n⟩ =
⟨2n⟩ so that
n
n
=
n
n
2n n
n + . . . (28)
We will need the following lemma.
Lemma 3.1 For 0 ≤ k ≤ n, one has
2n
2n
n
n
n
n 2k = ([k]!)2
[2k]!
2n
Proof This follows from the formula for the tetrahedron coeﬃcient given in
[MV, Thm. 2]. (The sum over ζ in that formula reduces to just one term.)
The key observation is that
2n
2n
n
n
Rk = 0 for k ⁄= n . (29)
Algebraic & Geometric Topology, Volume 3 (2003)
Skein-theoretical derivation of some formulas of Habiro 547
Indeed, if k < n , there are at most 2 k vertical strands in the middle and so
the result is zero because of the Jones-Wenzl idempotents f2n at the top and
bottom. On the other hand, if k > n , the result is zero because Rk annihilates
all even polynomials in z of degree < 2k .
If k = n one ﬁnds
2n
2n
n
n
Rn = (−1)n({n}!)2
2n
. (30)
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
2n = ⟨Rn, e 2n⟩
⟨e2n⟩
2n
2n
n
n
n
n 2n
hence (30) follows from (5) and Lemma 3.1.
On the other hand, since circling with ω p induces p full twists on even numbers
of strands (see (24)), we have, using (29), that
µ −2p
n cn,p
2n
2n
n
n
Rn = µ −2p
n
2n
2n
n
n
ω p =
2n
2n
n
n
· · · (31)
where there are 2 p crossings in the last diagram. (See (3) for the twist eigen-
values µ i .) Applying the fusion equation (26), we have
2n
2n
n
n
· · · =
n∑
k=0
δ(2k; n, n )2p ⟨2k⟩
⟨n, n, 2k⟩
2n
2n
n
n
n
n 2k (32)
where δ(c; a, b ) is the half-twist coeﬃcient deﬁned by
a
b
c = δ(c; a, b )
a
b
c .
Algebraic & Geometric Topology, Volume 3 (2003)
548 Gregor Masbaum
This coeﬃcient is computed in [MV, Thm. 3]. For us, it is enoug h to know
that
δ(c; a, b )2 = µ c
µ aµ b
which is easy to see. Using (30) and Lemma 3.1, it follows that
µ −2p
n cn,p (−1)n({n}!)2 =
n∑
k=0
µ p
2k
µ 2p
n
⟨2k⟩
⟨n, n, 2k⟩
([k]!)2
[2k]! .
The factors of µ −2p
n cancel out, and in view of (27), this gives the following
result:
Theorem 3.2 The coeﬃcients cn,p of ω p in (23) are given by
cn,p = 1
(a − a−1)2n
n∑
k=0
(−1)kµ p
2k[2k + 1]
[n + k + 1]! [n − k]! . (33)
