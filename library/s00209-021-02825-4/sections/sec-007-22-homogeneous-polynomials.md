---
doc_id: s00209-021-02825-4
doc_title: "A representation theoretic explanation of the Borcea–Brändén characterization"
section_id: sec-007-22-homogeneous-polynomials
section_title: "Homogeneous polynomials"
section_number: 2.2
pages: 6-8
source_pdf: s00209-021-02825-4.pdf
source_sha256: 85ca5ec21f42a988
toc_source: outline
---
2.1 Notation
Let [n] := {1, 2, . . . , n} and (1m) := (1, . . . , 1) ∈Nm
0 . For λ = (λ1, . . . , λm) ∈Nm
0 , we
deﬁne:
Cλ[x1, . . . , xm] :=

f ∈C[x1, . . . , xm] : degxk( f ) ≤λk

That is, elements of Cλ[x1, . . . , xm] are of degree at most λk in the variable xk. In particular,
we call polynomials in C(1m)[x1, . . . , xm] multi-afﬁne. We will also use the shorthand Cn[x]
to refer to univariate polynomials of degree at most n.
Now we deﬁne similar spaces of polynomials which are homogeneous in pairs of variables.
These polynomials should be seen as per-variable homogenizations of polynomials of the
spaces deﬁned above. For λ = (λ1, . . . , λm) ∈Nm
0 and K = C or K = R, we deﬁne:
VK(λ) = VK(λ1, . . . , λm)
:= {p ∈K[x1, y1 . . . , xm, ym] : p is homogeneous of degree λk in xk, yk}
We also use the shorthand V (λ) = VC(λ). As above, we call polynomials in V (1m) multi-
afﬁne. The notation used here is generalized from what is typically used to denote the
irreducible representations of SL2(C). As it turns out, spaces of homogeneous polynomials
in two variables can be used to deﬁne these representations. This will be made more precise
in Sect. 3.
123
A representation theoretic explanation...
1365
We let CP1 denote the projective space of lines in C2, and we will also identify this space
with the Riemann sphere. Note that CP1 can also be considered as a compact version of C
with one extra point added at inﬁnity. We will often identify CP1 with C (up to this extra
point) via stereographic projection. A circular region is then an open or closed disc, half-
plane, or complement of a disc in C. The set of circular regions is transitive under the action
of Möbius transformations. We also use the name circular regions to refer to the stereographic
projections into CP1. Closed half-planes and complements of discs projected into CP1 will
contain the point at inﬁnity. Throughout, we will let ∂S denote the boundary of (the closure
of) the set S in CP1 and let S◦denote the interior of S.
There is also a natural ordering structure on Nm
0 , along with a few basic operations that
will be used throughout. Fix λ = (λ1, . . . , λm) and α = (α1, . . . , αm) in Nm
0 , and ﬁx
β = (β1, . . . , βn) in Nl
0. We say α ≤λ whenever αk ≤λk for all k ∈[m]. We deﬁne λ+α :=
(λ1+α1, . . . , λm+αm), |λ| := λ1+· · ·+λm, and λ⊔β := (λ1, . . . , λm, β1, . . . , βl) ∈Nm+l
0
.
We also make use of a number of shorthands. Fix μ, λ ∈Nm
0 such that μ ≤λ. We deﬁne
xμ ∈Cλ[x1, . . . , xm] via xμ := xμ1
1 xμ2
2 · · · xμm
m . Similarly, we deﬁne ∂μ
x := ∂μ1
x1 ∂μ2
x2 · · · ∂μm
xm ,
where ∂x :=
∂
∂x . When considering V (λ), we deﬁne yμ and ∂μ
y in the same way. Further, we
deﬁne λ! := λ1! · · · λm! and
λ
μ
	
:=
λ!
μ!(λ−μ)! =
λ1
μ1
	
· · ·
λm
μm
	
. Finally, we denote (−1)μ :=
(−1)μ1 · · · (−1)μm = (−1)|μ|.
2.2 Homogeneous polynomials
The usual degree-n homogenization of a polynomial f ∈Cn[x] is deﬁned on monomials as
follows and is extended linearly.
Hmgn : Cn[x] →V (n)
xk →xk yn−k
More generally, for λ ∈Nm
0 the degree-λ homogenization is deﬁned on monomials as follows
and is extended linearly.
Hmgλ : Cλ[x1, . . . , xm] →V (λ)
xμ →xμyλ−μ
Cn[x] and V (n) are isomorphic as vector spaces via Hmgn, and we will mainly utilize
bivariate homogeneous polynomials in V (n) over the usual univariate polynomials in Cn[x].
What homogeneity gets us is a simpliﬁcation of a number of issues related to the fact that
polynomials in Cn[x] have at most n zeros. Speciﬁcally, it is more natural to think of the
missing zeros (when the number of zeros is less than n) as being “at inﬁnity”. Certain
results require premises restricting to convex regions or to polynomials of degree exactly
n (e.g., the classical Grace–Walsh–Szeg˝o coincidence theorem), and such details vanish
when considering homogeneous polynomials with possible roots at inﬁnity. Another way
to say this is that we consider polynomials in V (n) to have exactly n roots in CP1, which
can also be thought of as the Riemann sphere. We also consider polynomials p(x, y) =
p(x1, y1, . . . , xm, ym) ∈V (λ) to have zeros in (CP1)m, where each pair (xk, yk) corresponds
to a single factor of CP1 in (CP1)m.
We use the notation (a : b) ∈CP1, which is meant to give off the connotation of a ratio;
that is, (a : b) should feel like a/b. We also use the notation (a : b) =

(a1 : b1), . . . , (am :
bm)
	
∈(CP1)m. Note that this connotation aligns with the idea of considering the zeros of
123
1366
J. Leake
polynomials to be in (CP1)m. given the following equality. Deﬁning p := Hmgλ( f ) for a
given polynomial f ∈Cλ[x1, . . . , xm], we have:
p(x, y) = p(x1, y1, . . . , xm, ym) =

k
yλk
k · f (x1/y1, . . . , xm/ym) = yλ · f (x/y)
Finally, we give an important deﬁnition which will essentially replace the notion of a monic
polynomial for homogeneous polynomials.
Deﬁnition 2.1 Given p ∈V (λ), we say that p is top-degree monic if the coefﬁcient of xλ in
p equals 1. In particular, if p ∈V (n) is top-degree monic, then p has no roots at inﬁnity.
