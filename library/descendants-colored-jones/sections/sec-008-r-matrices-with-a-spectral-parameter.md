---
doc_id: descendants-colored-jones
doc_title: "The descendant colored Jones polynomials"
section_id: sec-008-r-matrices-with-a-spectral-parameter
section_title: "R-matrices with a spectral parameter"
section_number: null
pages: 13-15
source_pdf: descendants_colored_jones.pdf
source_sha256: f00693a5926c074f
toc_source: outline
doc_brief: "The descendant colored Jones polynomials — We discuss two realizations of the colored Jones polyno- mials of a knot, one appearing in an unnoticed work of the second author in 1994 on quantum"
---
We begin our discussion of R-matrices by introducing some useful notation.
For a positive integer n ∈Z>0, we deﬁne
(18)
(x)n :=
n
	
k=1
(1 −xk),
⟨⟨x⟩⟩n :=
1 −xn
(1 −x)n
with the convention (x)0 := 1.
For a ﬁxed root of unity ζ of order N = ord(ζ) ∈Z>0, we deﬁne rational
functions w(x|n) ∈C(x) for all integers n ∈Z by the recurrence relation
(19)
w(x|n)(1 −xζn) = w(x|n −1),
w(x|0) = 1.
One has the addition property
(20)
w(x|m + n) = w(x|m)w(xζm|n)
(m, n ∈Z)
which, by taking into account the equality w(x|N) = 1/(1 −xN), gives the
quasi-periodicity property
(21)
(1 −xN)w(x|n + N) = w(x|n)
(n ∈Z).
Notice the relation to the q-Pochhammer symbols with q = ζ
(22)
w(x|n) =
1
(xζ; ζ)n
(n ∈Z≥0).
It follows that w(x|n) is a rational function of x with coeﬃcients in the
cyclotomic ﬁeld FN := Q(ζ) whose poles and zeros (if any) are integer powers
of ζ. We will call such rational functions, and more generally matrices of such
rational functions, N-cyclotomic.
In [Kas96], the second author considered the N-cyclotomic matrix
r(x; m, n) ∈MatN2(C(x)) deﬁned by the formula
⟨i, j|r(x; m, n)|k, l⟩= ⟨⟨x⟩⟩Nζ(i−k+n)(l−j) w(x/ζ|j −i −m)w(x|l −k + n)
w(x/ζ|j −k + n −m)w(x/ζ|l −i)
(23)
2320
Stavros Garoufalidis and Rinat Kashaev
(where the left hand-side is the bra-ket notation for the entries of a matrix)
and proved that it satisﬁes the Yang–Baxter equation
(24)
r1,2(x; m1, m2)r1,3(xy; m1, m3)r2,3(y; m2, m3)
= r2,3(y; m2, m3)r1,3(xy; m1, m3)r1,2(x; m1, m2)
where, along with continuous spectral parameters x and y, the integers m1,
m2, m3 play the role of discrete spectral parameters. Here, r1,2, r1,3 and r2,3
denote the N-cyclotomic matrices in MatN3(C(x)) obtained by interpreting r
as an endomorphism of an N-dimensional space V ⊗2, equipped with a basis,
and ri,j as the corresponding endomorphisms of V ⊗3, acting nontrivially on
the i, j copies of V in V ⊗3 and trivially on the remaining copy.
Aside from being a solution to the Yang–Baxter equation with a spectral
parameter, a somehow surprising fact is that r(x; m, n) is regular (i.e. it has a
ﬁnite limit) at x = 1. This follows from the existence of the gauge conjugating
matrix h(y, m) ∈MatN(C(y)) deﬁned by
(25)
⟨i|h(y, m)|j⟩= ζ(j−i)m⟨⟨y ζj−i⟩⟩N.
The entries of the matrix h(y, m) are, in fact, polynomials in y, it satisﬁes
the multiplicative property
(26)
h(x, m)h(y, m) = h(xy, m)
and it enters the important gauge symmetry transformation formulae for the
r-matrix (23):
h1(y, m + 1)r(x; m, n)h1(y−1, m + 1)
(27)
= r(xy; m, n) = h2(y−1, 0)r(x; m, n)h2(y, 0).
Here, h1 and h2 denote matrices in MatN2(C(y)) obtained by interpreting h
as an endomorphism of an N dimensional space V with a basis, and hj as
corresponding endomorphisms of V ⊗2 obtained by acting on the j-th copy of
V in V ⊗2 by h and on the remaining copy of V by identity.
The above gauge symmetry transformation formulae, together with the
fact that h(y, m) has polynomial entries in y, imply easily that r(x; m, n) is
regular at x = 1. An additional calculation shows that
(28)
⟨i, j|r(1; m, n)|k, l⟩= Vi,j−m,k−n,l(ζ)ζk−l−n+(k−i−n)m
The descendant colored Jones polynomials
2321
where
(29) Vi,j,k,l(ζ) := N θN({j −i −1}N + {l −k}N) θN({i −l}N + {k −j}N)
(¯ζ){j−i−1}N(ζ){i−l}N(¯ζ){l−k}N(ζ){k−j}N
and where ¯ζ denotes the complex conjugate of the complex number ζ and for
an integer k, {k}N denotes the unique integer such that
(30)
{k}N ≡k
(mod N),
0 ≤{k}N < N,
and
(31)
θN(k) := δk,{k}N
where δ is the standard Kronecker delta symbol. The regularity of the matrix
r(x; m, n) is reminiscent to the p-adic valuation of factorials in Landau’s work,
see for instance [RV, Sou20] and references therein.
A consequence of formula (28) is that the rows and columns of r(1; m, n)
are naturally indexed by elements of the additive group Z/NZ, as well as the
discrete spectral parameters are in Z/NZ.
