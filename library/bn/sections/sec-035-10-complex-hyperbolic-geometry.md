---
doc_id: bn
doc_title: "Braid groups and Hodge theory Curtis T. McMullen 25 April, 2009"
section_id: sec-035-10-complex-hyperbolic-geometry
section_title: "Complex hyperbolic geometry"
section_number: 10
pages: 45-49
source_pdf: bn.pdf
source_sha256: 95ed0908ceb54a1c
doc_brief: "Braid groups and Hodge theory Curtis T. McMullen 25 April, 2009 — This paper gives an account of the unitary representations of the braid group that arise via the Hodge theory of cyclic branched cove"
---
In this section we discuss the cases where moduli space acqui res a complex
hyperbolic metric of ﬁnite volume. For example, we will see:
Theorem 10.1 Forn = 4, 5, 6, 8 and 12, the period map
fq : M0,n → CHn−3/ρq(Bn)
at q =ζ −2
n presents moduli space as the complement of a divisor in a ﬁnit e-
volume, arithmetic, complex-hyperbolic orbifold.
(This divisor corresponds to certain Dehn twists whose imag es underρq have
ﬁnite order.) Since M2 ∼
= M0, 6 we also have:
Corollary 10.2 The moduli space M2 can be completed to a complex hy-
perbolic orbifold of ﬁnite volume.
Note that the complex hyperbolic structure on M2 comes from Hodge struc-
tures on surfaces of genus four (obtained as triple covers of ˆC branched over
six points).
These results are special cases of the work of Deligne–Mosto w and Thurston,
which we recall below. We will also give a self-contained pro of of:
44
Theorem 10.3 If ρq(Bn) ⊂ U(1,s ) is discrete, then it is a lattice.
Corollary 10.4 Whenever U(Λ n,q ) ⊂ U(1,s ) is a lattice, so is ρq(Bn).
Table 9 furnishes 24 values of ( n,q ) with n ≥ 4 where this Corollary
applies, including the 5 cases covered by Theorem 10.1 above .
Hypergeometric functions and shapes of polyhedra. Let ~M0,n de-
note the moduli space of orderedpoints onˆC (anSn-covering space of M0,n ).
Let Pn denote the pure braid group of n points on the sphere. There is a
natural surjective map
Pn →π1(~M0,n ).
Following [DM1] and [DM2], let µ = (µ1,...,µ n) be a sequence of ratio-
nal weights satisfying
0<µ i< 1 and
∑
µi = 2.
Givenb = (b1,...,b n) ∈ C⟨n⟩, consider the multivalued algebraic 1-form
ωb = dx
(x −b1)µ 1 · · · (x −bn)µ n
·
Note that
K = (ωb) = −
∑
µibi
can be regarded as a generalized canonical divisor on ˆC, since deg( K) =
−2. The periods
∫ bj
bi ωb are multivariable hypergeometric functions, whose
ratios become well-deﬁned on the universal cover of ~M0,n . These period
coordinates give ~M0,n a complex hyperbolic metric gµ , whose holonomy
determines a representation
ξµ :Pn → Isom(CHn−3) ∼
= PU(1,n ).
Alternatively, following [Th2], one can consider |ωb| as a ﬂat metric on
ˆC with cone angles 2 π(1 −µi) at each point bi. The space ( ˆC, |ωb|) is then
isometric to a convex polyhedron in R3 of total area A =
∫
C |ωb|2. By
considering A as a quadratic form, Thurston obtains the same complex
hyperbolic metric gµ on M0,n as Deligne and Mostow. 1
The orbifold condition. The weights µ satisfy the orbifold condition if
whenevers =µi +µj < 1, either
1The work [Th2] grew out of a discussion of problem 3 of the 27th Mathematical
Olympiad (July 9, 1986).
45
• (1 −s)−1 ∈ Z, or
• µi =µj and 2(1 −s)−1 ∈ Z.
A list of the 94 diﬀerent weights µ satisfying this condition, with n ≥ 4,
is given in the Appendix to [Th2]. This condition allows us to formulate
following two important results.
Theorem 10.5 (Deligne–Mostow) If the weights (µi) satisfy the orbifold
condition, then the image ξµ (Pn) of the pure braid group is a lattice in
PU(1,n − 3).
Theorem 10.6 (Thurston) The metric completion of (~M0,n,g µ ) is a com-
plex hyperbolic cone manifold of ﬁnite volume. It is an orbifo ld iﬀ the weights
(µi) satisfy the orbifold condition.
See [DM1], [Mos1], and [Th2, Thm. 0.2], as well as [Par, Lemma 3.5], which
clariﬁes the relationship between the two results.
Equal weights. It is straightforward to see that when µ1 = · · · =µn = 2/n,
the constructions of Deligne–Mostow and Thurston give the s ame complex
hyperbolic structure on
M0,n ∼
= ~M0,n/Sn
as that furnished by the period mapping
fq : T0,n → H 1,n −3
of §6 at q =ζ −2
n (see Corollary 6.5). Similarly, if µ1 = · · · =µn−1 =k/d ⁄=
µn, then k/d ∈ (1/(n − 1), 2/(n − 1)) and the complex hyperbolic metric on
M∗
0,n −1 ∼
= ~M0,n/Sn−1
agrees with that furnished by the period mapping at q =ζ −k
d (see Corollary
6.3). In particular, the images of the holonomy maps ξµ (Pn) and ρq(Bn) are
commensurable, and hence Theorem 10.5 provides a criterion for ρq(Bn) to
be a lattice.
Arithmetic lattices. To complement the results above, we present a short
proof that ρq(Bn) ⊂ U(1,s ) is a lattice whenever it is discrete.
Proof of Theorem 10.3. Assume ρq(Bn) ⊂ U(1,s ) is discrete. Let
M = M∗
0,n or M0,n depending on whether q = ζ −2
d or not, and let Z =
CHs/ρq(Bn). As we have seen in §6, the period map deﬁnes an analytic
local homeomorphism of orbifolds fq : M → Z. By the Schwarz lemma,
46
fq is distance-decreasing from the Teichm¨ uller metric on M to (a suitable
multiple of) the complex hyperbolic metric on Z.
Let M be the Deligne-Mumford compactiﬁcation of M by stable curves
with marked points, and let ∂M = M −M . There is a unique maximal
analytic continuation of fq to an open set M 0 with M ⊂M 0 ⊂M .
A local model ( U,∂U ) for (M,∂M ) near any x ∈M is given by a ﬁnite
quotient of (∆ a × (∆ ∗)b, 0 × ∆ b near (0, 0). Since the puncture of ∆ ∗ is a
cusp, every element of π1(U ) is represented by a short loop in M . Thus
every element of H = f∗(π1(U )) ⊂π1(Z) is represented by a short loop in
Z.
If H is ﬁnite, then fq lifts to a map ~fq from a ﬁnite cover of U into
the bounded domain CHs, and hence fq itself extends analytically to a
neighborhood of x. That is, x ∈ M 0. Otherwise, there is an h ∈ H which
has no ﬁxed point in CHs but whose minimal translation distance is zero.
Then by the Schwarz lemma, fq(U ) is contained in the thin part of Z, and
hence fq tends to inﬁnity at x.
It follows that fq : M 0 → Z is proper. In particular, fq(M 0) = Z and
vol(Z) = vol(fq(M )) since dim∂M <dimM = dimZ. Since fq is a contrac-
tion, the volume of fq(M ) ⊂Z is no more than a constant multiple of the
volume of M in the Teichm¨ uller metric, which is ﬁnite (see e.g. [Mc1][T hm.
8.1]). Thus vol( Z)< ∞, and hence π1(Z) = ρq(Bn) is a lattice.
Note that Corollary 10.4 to Theorem 10.3 also follows from Th eorem
10.5 and the following observation regarding the 36 entries in Table 9 with
hyperbolic signature:
Proposition 10.7 Whenever U(Λ n,q ) ⊂ U(1,s ) is a complex hyperbolic lat-
tice, the corresponding weights µ satisfy the orbifold condition.
Proof of Theorem 10.1. For these values of n, the entry k/d = 2/n
appears in Table 9, so we may apply Theorem 10.6.
Arithmetic hyperbolic structures for n ≤ 12. An examination of Ta-
ble 9 also shows there is at least one arithmetic complex hype rbolic structure
on M∗
0,n for every value of n with 3 ≤n ≤ 11. (For n> 12, hyperbolic sig-
nature no longer occurs.)
When n = 3, M∗
0, 3 can be completed to give the hyperbolic orbifold
H/Γ(2, 3,p ) for any p > 6; this completion is arithmetic for 12 values of
p. There are 6 arithmetic hyperbolic structures on M∗
0, 4 besides the one
induced from the covering map M∗
0, 4 → M 0, 5; the case n = 4, q = ζ −1
3
47
was considered by Picard in 1883 [Pic]. There are also severa l arithmetic
hyperbolic structures on M∗
0,n for n = 5, 6, 7, but only one for each n =
8, 9, 10, 11, and none for M∗
12.
Non-arithmetic examples. Non-arithmetic lattices in U(1 ,s ), s > 1,
were ﬁrst discovered in [Mos1]. For the braid group, Theorem 10.6 shows
there is a unique case where ρq(Bn) is nonarithmetic but ( M∗
0,n,g µ ) is still
a complex hyperbolic orbifold: namely n = 4 and µ = (7, 7, 7, 7, 8)/18. In
this example q =ζ −7
18 and ρq(Bn) ⊂ U(1, 2).
Other values of µ giving non-arithmetic lattices are enumerated in [Th2,
Appendix]. Only a ﬁnite number of non-arithmetic lattices i n U(1,s ) are
presently known (up to commensurability).
Modular embeddings. Let us consider the non-arithmetic lattice coming
from n = 4 and d = 18 in more detail. In this case the equation y18 =
x(x − 1)(x −a)(x −b) determines a 2-dimensional family of curves X of
genus g = 25. As in §7, we can regard ∆ = Sp 2g(Z)T | Ker Φ d(T ∗) as an
irreducible, arithmetic lattice in the product of unitary g roups
∏
Φ d(q)=0, Im q<0
U (H 1(X)q) ∼
=U (1, 2)2 ×U (2)2.
Because of the U(2) factor, ∆ has no unipotents, so it determi nes a compact,
4-dimensional Shimura variety
S = (CH2 × CH2)/∆ .
Now let Γ = ρq(Bn) ⊂ U(1, 2) whereq =ζ −7
18 . Then Γ is a non-arithmetic
lattice. Let Z = CH2/Γ and let r =ζ −5
