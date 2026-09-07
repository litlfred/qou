---
doc_id: arxiv-0806.2317v1
doc_title: "Bounds for codes and designs in complex subspaces Aidan Roy ∗"
section_id: sec-004-zonal-polynomials
section_title: "Zonal polynomials"
section_number: null
pages: 10-14
source_pdf: 0806.2317v1.pdf
source_sha256: c54e80d460413a5e
doc_brief: "Bounds for codes and designs in complex subspaces Aidan Roy ∗ — We introduce the concepts of complex Grassmannian codes and designs."
---
describe those results in the next section.
5 Zonal polynomials
A zonal polynomial at a point a ∈ G m,n is a function on points b ∈ G m,n which
depends only on the the principle angles between a and b. Given any univariate
polynomial f (x) of degree k, we deﬁne the zonal polynomial of f at b as follows:
if f (x) =∑ k
i=0 fixi, then
fa(b) =
k∑
i=0
fi tr(PaPb)i.
Here Pa and Pb are the projection matrices for a and b. As written, the zonal
polynomial is not homogeneous, but by embedding the constan t 1 into Hom 1(n)
in the form tr( Pb)/m , the exponents in fa(b) may be “pushed up” and we may
assume fa is in Hom k(n). To see that fa(b) only depends on the principal angles
between a and b, note that tr( PaPb) is simply the sum of the principal angles.
There is another set of zonal polynomials that play a particu lar role in the
theory of Delsarte bounds. Let Hµ be an irreducible representation in L2(Gm,n ).
10
Then for each a ∈ G m,n , deﬁne the zonal orthogonal polynomial Zµ,a to be the
unique element of Hµ such that for every p ∈ Hµ ,
⟨Zµ,a , p ⟩ = p(a).
Then zonal polynomials are invariant under the unitary grou p, in the following
sense:
Zµ,b (a) = ⟨U ∗Zµ,a , U ∗Zµ,b ⟩ = ⟨Zµ,U a , Z µ,U b ⟩ = Zµ,U b (U a).
The value of Zµ,b (a) depends on the U (n)-orbit of ( a, b ) and therefore depends
on the principle angles of a and b. With this in mind we sometimes write
Zµ,a (b) = Zµ (a, b ) or Zµ,a (b) = Zµ (y1, . . . , y m), where ( y1, . . . , y m) are the prin-
cipal angles of a and b.
Schur orthogonality [22, Theorem 3.3] for irreducible repr esentations implies
that Zµ,a and Zν,b are orthogonal for µ ⁄= ν. So, we have
⟨Zµ,a , Z ν,b ⟩ = δµ,ν Zµ (a, b ).
Moreover, Zµ,a (b) = Zµ,b (a) is in fact real and symmetric in a and b. The zonal
polynomials satisfy some other important properties, incl uding the following
positivity condition:
Lemma 5.1. For any subset S ⊆ G m,n ,
∑
a,b ∈S
Zµ (a, b ) ≥ 0.
Equality holds only when ∑
a∈S Zµ,a = 0.
Proof. We have
∑
a,b ∈S
Zµ (a, b ) =
∑
a,b ∈S
⟨Zµ,a , Z µ,b ⟩
=
⟨∑
a∈S
Zµ,a ,
∑
b∈S
Zµ,b
⟩
≥ 0.
Equality holds if and only if ∑
a∈S Zµ,a = 0.
The second important condition the zonal polynomials satis fy is called the
addition formula :
11
Lemma 5.2. Let e1, . . . , e N be an orthonormal basis for the irreducible sub-
space Hµ . Then
N∑
i=1
ei(a)ei(b) = Zµ (a, b ).
Proof. Since Zµ,a is in Hµ , we may write it as a linear combination of
e1, . . . , e N :
Zµ,a =
N∑
i=1
⟨ei, Z µ,a ⟩ei
=
∑
i
ei(a)ei.
So, it follows that Zµ,a (b) =∑
i ei(a)ei(b).
James and Constantine give an explicit formula for the zonal orthogonal
polynomials of Gm,n in terms of Schur polynomials, the irreducible characters
of SL(m, C). If y = (y1, . . . , y m) are variables and σ = (s1, . . . , s m) is a partition
into at most m parts, then the (unnormalized) Schur polynomial is deﬁned as
Xσ (y) := det(ysj+m−j
i )i,j
det(yk−j
i )i,j
.
Each Schur polynomial is a symmetric polynomial in ( y1, . . . , y m). For more
information about Schur polynomials, see Stanley [23, Chap ter 7]. The nor-
malized Schur polynomial X ∗
σ is the multiple of Xσ such that X ∗
σ (1, . . . , 1) = 1.
To deﬁne the zonal orthogonal polynomials for Gm,n , ﬁrst deﬁne the ascend-
ing product
(a)s := a(a + 1) . . . (a + s − 1),
and given a partition σ = ( s1, . . . , s m), deﬁne complex hypergeometric coeﬃ-
cients
[a]σ :=
m∏
i=1
(a − i + 1)si.
Further assume we have a partial order ≤ on partitions deﬁned such that
(s1, . . . , s m) ≤ (k1, . . . , k l) if and only if si ≤ ki for all i. Letting y + 1 :=
(y1 + 1, . . . , y m + 1), the complex hypergeometric binomial coeﬃcients [ κσ ] are
given by the formula
X ∗
κ (y + 1) =
∑
σ ≤κ
[ κ
σ
]
X ∗
σ (y).
12
We can now deﬁne the zonal orthogonal polynomials for Gm,n . The following
result is due to James and Constantine [17].
Theorem 5.3. Let
ρσ :=
m∑
i=1
si(si − 2i + 1)
and let σ and κ partition s and k respectively. Also let
[c](κ,σ ) :=
∑
i
[ κ
σi
][ σi
σ
]
(k − s)
[ κ
σ
] [c](κ,σ i)(
c + ρκ −ρσ
k−s
) ,
where the summation is over partitions σi = (s1, . . . , s i−1, s i + 1, s i+1, . . . ) that
are nonincreasing. Then up to normalization, the zonal orth ogonal polynomial
for Hκ is
Zκ (y) :=
∑
σ ≤κ
(−1)s
[ κ
σ
]
[c](κ,σ )
[a]σ
X ∗
σ (y),
where y = (y1, . . . , y m) is the set of principal angles.
The ﬁrst few normalized Schur polynomials are:
X ∗
0 (y) = 1
X ∗
1 (y) = 1
m
m∑
i=1
yi
X ∗
1, 1(y) = 1(m
2
)
∑
i<j
yiyj
X ∗
2 (y) = 1(m+1
2
)
( m∑
i=1
y2
i +
∑
i<j
yiyj
)
.
Up to normalization by a constant, the ﬁrst few zonal orthogo nal polynomials
are:
Z0(y) = 1
Z1(y) = nX ∗
1 (y) − m
Z1, 1(y) = m(m − 1) − 2(n − 1)(m − 1)X ∗
1 (y) + (n − 1)(n − 2)X ∗
1, 1(y)
Z2(y) = m(m + 1) − 2(n + 1)(m + 1)X ∗
1 (y) + (n + 1)(n + 2)X ∗
2 (y).
13
A {α } {α, β }
Absolute
bound n2
(n2
2
)
(m > 1)
Relative
bound
n(m − α )
m2 − nα
n(m − α )(m − β )
m2
[
(m+1)2
2(n+1) + (m−1)2
2(n−1) − (α + β ) + nαβ
m2
]
Relative
bound
conditions
α < m2
n α + β ≤ 2(m2n − 4m + n)
n2 − 4 ,
α + β − nαβ
m2 < m2n − 2m + n
n2 − 1
