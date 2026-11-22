---
doc_id: 0306345v1
doc_title: "Skein-theoretical derivation of some formulas of Habiro Introduction"
section_id: sec-003-3-graphical-calculus-and-a-formula-for-ωp
section_title: "Graphical calculus and a formula for ωp"
section_number: 3
pages: 9-12
source_pdf: 0306345v1.pdf
source_sha256: 936aa08026b2683b
toc_source: inferred
doc_brief: "Skein-theoretical derivation of some formulas of Habiro — We use skein theory to compute the coeﬃcients of certain power series considered by Habiro in his theory of sl2 invariants of integral homol"
duplicate_of: "agt-v3-n1-p17-p"
---
Graphical calculus and a formula for ωp
Let us write ω = ω+ and put
ωp =
∞
X
n=0
cn,pRn .
(23)
Note that the coeﬃcients cn,p are well-deﬁned (because Rn divides Rn+1 and
therefore the coeﬃcients Ck
n,m in the product expansion RnRm = P
k Ck
n,mRk
are zero if n or m is bigger than k.) We have
⟨ωp, x⟩= ⟨tp(x)⟩
(24)
for every even x. (This follows from (6) since circling with ωp is the same as
circling with p parallel copies of ω.) Of course, cn,1 = cn,+ and cn,−1 = cn,−
(it follows from the uniqueness of ω−that ω−= ω−1). The aim of this section
is to give a formula for the coeﬃcients cn,p (see Theorem 3.2 below).
We use the extension of the Kauﬀman bracket to admissibly colored banded
trivalent graphs as in [MV]. (Such graphs are sometimes called spin networks;
for more background see e.g. [KL] and references therein.) A color is just an
integer ≥0. A triple of colors (a, b, c) is admissible if a + b + c ≡0 (mod 2)
and |a −b| ≤c ≤a + b. Let D be a planar diagram of a banded trivalent
graph. An admissible coloring of D is an assignment of colors to the edges
of D so that at each vertex, the three colors meeting there form an admissible
triple. The Kauﬀman bracket of D is deﬁned to be the bracket of the expansion
of D obtained as follows. The expansion of an edge colored n consists of n
parallel strands with a copy of the Jones-Wenzl idempotent fn inserted. (The
idempotent fn is characterized by the fact that xfn = fnx = 0 for every element
x of the standard basis of the Temperley-Lieb algebra other than the identity
element; here, the standard basis consists of the (n, n)-tangle diagrams without
crossings and without closed loops.) The expansion of a vertex is deﬁned as in
Fig. 2, where the internal colors i, j, k are deﬁned by
i = (b + c −a)/2, j = (c + a −b)/2, k = (a + b −c)/2 .
(25)
We have the fusion equation
b
a
=
X
c
⟨c⟩
⟨a, b, c⟩
b
a
c
b
a
(26)
Algebraic & Geometric Topology, Volume 3 (2003)
546 Gregor Masbaum

Figure 2: How to expand colored edges and vertices. The boxes stand for appropriate
Jones-Wenzl idempotents.

Here the sum is over those colors c so that the triple (a,b,c) is admissible, we
have (c) = (e-) = (—1)°{e + 1], and the trihedron coefficient (a,b,c) is (see
[MV, Thm. 1]):

Cc

_ viajar lit p++ A! A! La! ay!
(a,b, ¢) = Co = (“i [a]! [B]! [ec]! (7)

(here i,j,k are the internal colors as defined in (25)). Note that (n,n, 2n) =
(2n) so that

TU Soar< +o (28)

We will need the following lemma.

Lemma 3.1 For 0 <k <n, one has

2n

Proof This follows from the formula for the tetrahedron coefficient given in
[MV, Thm. 2]. (The sum over ¢ in that formula reduces to just one term.) O

The key observation is that

2n
n

mi = 0 for k#n. (29)
\ Jn
2n

Algebraic & Geometric Topology, Volume 3 (2003)
Skein-theoretical derivation of some formulas of Habiro 547

Indeed, if k < n, there are at most 2k vertical strands in the middle and so
the result is zero because of the Jones-Wenzl idempotents fg, at the top and
bottom. On the other hand, if k > n, the result is zero because R; annihilates
all even polynomials in z of degree < 2k.

If k =n one finds
2n 2n
n

Ral | = (-1)"({n}!)? . (30)

n
2n

Indeed, applying (28), one has

2n

"C BL Rn _ (Rnseon) Zan
n 7 (€2n) n n

2n 2n

hence (30) follows from (5) and Lemma 3.1.

On the other hand, since circling with w? induces p full twists on even numbers
of strands (see (24)), we have, using (29), that

2n 2n
n n n
Hy? Cnp fi = mu? af =
n \ Jn
2n

where there are 2p crossings in the last diagram. (See (3) for the twist eigen-
values y;.) Applying the fusion equation (26), we have

Algebraic & Geometric Topology, Volume 3 (2003)
548
Gregor Masbaum
This coeﬃcient is computed in [MV, Thm. 3]. For us, it is enough to know
that
δ(c; a, b)2 =
µc
µaµb
which is easy to see. Using (30) and Lemma 3.1, it follows that
µ−2p
n
cn,p(−1)n({n}!)2 =
n
X
k=0
µp
2k
µ2p
n
⟨2k⟩
⟨n, n, 2k⟩
([k]!)2
[2k]!
.
The factors of µ−2p
n
cancel out, and in view of (27), this gives the following
result:
Theorem 3.2 The coeﬃcients cn,p of ωp in (23) are given by
cn,p =
1
(a −a−1)2n
n
X
k=0
(−1)kµp
2k[2k + 1]
[n + k + 1]! [n −k]! .
(33)
