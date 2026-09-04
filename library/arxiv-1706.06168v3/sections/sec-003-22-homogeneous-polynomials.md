---
doc_id: arxiv-1706.06168v3
doc_title: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization"
section_id: sec-003-22-homogeneous-polynomials
section_title: "Homogeneous Polynomials"
section_number: 2.2
pages: 5-7
source_pdf: 1706.06168v3.pdf
source_sha256: ab3383a95f369922
doc_brief: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization — In 2009, Borcea and Br¨ and´ en characterized all linear oper ators on multivariate polynomials which preserve the"
---
2.1 Notation
Let [n] := {1, 2,...,n } and (1 m) := (1,..., 1) ∈ Nm
0 . For λ = (λ1,...,λ m) ∈ Nm
0 , we deﬁne:
Cλ[x1,...,x m] :=
{
f ∈ C[x1,...,x m] : deg xk (f ) ≤λk
}
That is, elements of Cλ[x1,...,x m] are of degree at most λk in the variable xk. In particular, we call
polynomials in C(1m)[x1,...,x m] multi-aﬃne . We will also use the shorthand Cn[x] to refer to univariate
polynomials of degree at most n.
Now we deﬁne similar spaces of polynomials which are homogeneous in pa irs of variables. These poly-
nomials should be seen as per-variable homogenizations of polynomials of the spaces deﬁned above. For
λ = (λ1,...,λ m) ∈ Nm
0 and K = C or K = R, we deﬁne:
VK(λ) = VK(λ1,...,λ m) := {p ∈ K[x1,y 1...,x m,y m] : p is homogeneous of degree λk in xk, yk}
We also use the shorthand V (λ) = VC(λ). As above, we call polynomials in V (1m) multi-aﬃne . The notation
used here is generalized from what is typically used to denote the irre ducible representations of SL 2(C). As
5
it turns out, spaces of homogeneous polynomials in two variables can be used to deﬁne these representations.
This will be made more precise in §3.
We let CP1 denote the projective space of lines in C2, and we will also identify this space with the
Riemann sphere. Note that CP1 can also be considered as a compact version of C with one extra point
added at inﬁnity. We will often identify CP1 with C (up to this extra point) via stereographic projection. A
circular region is then an open or closed disc, half-plane, or complement of a disc in C. The set of circular
regions is transitive under the action of M¨ obius transformations. We also use the name circular regions to
refer to the stereographic projections into CP1. Closed half-planes and complements of discs projected into
CP1 will contain the point at inﬁnity. Throughout, we will let ∂S denote the boundary of (the closure of)
the set S in CP1 and let S◦ denote the interior of S.
There is also a natural ordering structure on Nm
0 , along with a few basic operations that will be used
throughout. Fix λ = (λ1,...,λ m) and α = (α1,...,α m) in Nm
0 , and ﬁx β = (β1,...,β n) in Nl
0. We say
α ≤λ wheneverαk ≤λk for all k ∈ [m]. We deﬁne λ +α := (λ1 +α1,...,λ m +αm), |λ| :=λ1 + · · · +λm,
and λ ⊔β := (λ1,...,λ m,β 1,...,β l) ∈ Nm+l
0 .
We also make use of a number of shorthands. Fix µ,λ ∈ Nm
0 such that µ ≤ λ. We deﬁne xµ ∈
Cλ[x1,...,x m] via xµ :=xµ1
1 xµ2
2 · · ·xµm
m . Similarly, we deﬁne ∂µ
x :=∂µ1
x1∂µ2
x2 · · ·∂µm
xm , where ∂x := ∂
∂x . When
considering V (λ), we deﬁne yµ and ∂µ
y in the same way. Further, we deﬁne λ! := λ1! · · ·λm! and
( λ
µ
)
:=
λ!
µ!(λ−µ)! =
( λ1
µ1
)
· · ·
( λm
µm
)
. Finally, we denote ( −1)µ := (−1)µ1 · · · (−1)µm = (−1)|µ|.
2.2 Homogeneous Polynomials
The usual degree- n homogenization of a polynomial f ∈ Cn[x] is deﬁned on monomials as follows and is
extended linearly.
Hmgn : Cn[x] →V (n)
xk ↦→xkyn−k
More generally, for λ ∈ Nm
0 the degree-λ homogenization is deﬁned on monomials as follows and is extended
linearly.
Hmgλ : Cλ[x1,...,x m] →V (λ)
xµ ↦→xµyλ−µ
Cn[x] and V (n) are isomorphic as vector spaces via Hmg n, and we will mainly utilize bivariate homoge-
neous polynomials in V (n) over the usual univariate polynomials in Cn[x]. What homogeneity gets us is
a simpliﬁcation of a number of issues related to the fact that polynom ials in Cn[x] have at most n zeros.
Speciﬁcally, it is more natural to think of the missing zeros (when the number of zeros is less than n) as
being “at inﬁnity”. Certain results require premises restricting to c onvex regions or to polynomials of degree
exactly n (e.g., the classical Grace-Walsh-Szeg˝ o coincidence theorem), and such details vanish when consid-
ering homogeneous polynomials with possible roots at inﬁnity. Anothe r way to say this is that we consider
polynomials in V (n) to have exactly n roots in CP1, which can also be thought of as the Riemann sphere.
We also consider polynomials p(x,y ) = p(x1,y 1,...,x m,y m) ∈ V (λ) to have zeros in ( CP1)m, where each
pair (xk,y k) corresponds to a single factor of CP1 in ( CP1)m.
We use the notation ( a :b) ∈ CP1, which is meant to give oﬀ the connotation of a ratio; that is, ( a :b)
should feel like a/b. We also use the notation ( a :b) =
(
(a1 :b1),..., (am :bm)
)
∈ (CP1)m. Note that this
connotation aligns with the idea of considering the zeros of polynomia ls to be in ( CP1)m. given the following
equality. Deﬁning p := Hmg λ(f ) for a given polynomial f ∈ Cλ[x1,...,x m], we have:
p(x,y ) = p(x1,y 1,...,x m,y m) =
∏
k
yλk
k ·f (x1/y1,...,x m/ym) = yλ ·f (x/y)
Finally, we give an important deﬁnition which will essentially replace the n otion of a monic polynomial for
homogeneous polynomials.
6
Deﬁnition 2.1. Givenp ∈V (λ), we say that p is top-degree monic if the coeﬃcient of xλ in p equals 1. In
particular, if p ∈V (n) is top-degree monic, then p has no roots at inﬁnity.
