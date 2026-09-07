---
doc_id: arxiv-0806.2317v1
doc_title: "Bounds for codes and designs in complex subspaces Aidan Roy ∗"
section_id: sec-005-bounds
section_title: "Bounds"
section_number: null
pages: 14-18
source_pdf: 0806.2317v1.pdf
source_sha256: c54e80d460413a5e
doc_brief: "Bounds for codes and designs in complex subspaces Aidan Roy ∗ — We introduce the concepts of complex Grassmannian codes and designs."
---
The correct normalizations satisfy
⟨Zµ,a , Z µ,a ⟩ = Zµ (1, 1, . . . , 1) = dim Hµ .
With the exception of the case µ = 0 (which is normalized correctly in the
formula above), normalizations for Zµ will not play a role in the results which
follow.
6 Bounds
Recall that an A-code is a collection S of subspaces in Gm,n such that tr(PaPb) ∈
A for every a ⁄= b in S. In this section, we ﬁnd upper bounds on the size of an
A-code in terms of either the cardinality of A or its elements. A summary of
the results for |A| ≤ 2 is given in Table 1.
If A = {α 1, . . . , α k}, then the annihilator of A is the function
annA(x) :=
k∏
i=1
(x − α i),
14
The signiﬁcance of the annihilator is that ann A(tr(PaPb)) = 0 for any a ⁄= b
in S. More generally, for any polynomial f , an f -code is a collection S of
subspaces such that f (tr(Pa)) ⁄= 0 and f (tr(PaPb)) = 0 for every a ⁄= b in S. If
A is any set of angles and f is the annihilator of A, then an A-code is also an
f -code.
Theorem 6.1. If S ⊆ G m,n is an A-code, with |A| = k, then
|S| ≤ dim(Homk(n)) ≤
(n2 + k − 1
k
)
.
Proof. We prove more generally that if S is an f -code, with deg( f ) = k, then
|S| ≤ dim(Homk(n)). The result then follows by taking f to be the annihilator
of A.
Consider the zonal polynomials fa(b) := f (tr(PaPb)), for a ∈ S. Note that
fa is in Hom k(n), since fa(b) is a degree- k polynomial in the entries of Pb. Since
fa(b) = 0 for every b ∈ S except a, and fa(a) ⁄= 0, the set {fa : a ∈ S} is linearly
independent. Thus the number of functions |S| is at most the dimension of the
space Hom k(n).
Corollary 6.2. Let S be a collection of subspaces in Gm,n such that tr(PaPb) =
α for all a ⁄= b in S. Then
|S| ≤ n2.
Proof. Use Theorem 6.1 with the degree-1 annihilator of α , which induces
zonal polynomials in Hom 1(n).
Since fa(b) is also a degree- k symmetric polynomial in the principal angles
of a and b, it follows that fa is also in Hk(m, n ). Then by the same argument
as in Theorem 6.1, we have
Corollary 6.3. If S ⊆ G m,n is an A-code, with |A| = k, then
|S| ≤ dim(Hk(m, n )).
If equality holds, then the functions fa form a basis for the space. Moreover,
the space Hk(m, n ) is exactly the space of functions on S.
Theorem 6.1 and Corollary 6.3 are called absolute bounds for Grassmannian
codes, because the bounds depend only on the number of diﬀeren t inner product
values that occur in S. When m = 1 these bounds reduce to the absolute
bounds of Delsarte, Goethals and Seidel [11, Theorem 6.1]. T here is also a
relative bound , which depends on the actual values of the inner products and
is sometimes tighter.
15
Theorem 6.4. Let f (y1, . . . , y m) ∈ R[y1, . . . , y m] be a symmetric polynomial
such that f =∑
µ cµ Zµ , where Zµ is a zonal orthogonal polynomial, and each
cµ ≥ 0. Further assume that c0 is strictly positive. If S is a set of subspaces in
Gm,n such that fa(b) := f (y1(a, b ), . . . , y m(a, b )) is nonpositive for every a ⁄= b
in S, then
|S| ≤ f (1, . . . , 1)
c0
.
Proof. Since fa(b) ≤ 0 for b ⁄= a, summing over all b ∈ S, we have
∑
b∈S
fa(b) ≤ fa(a) = f (1, . . . , 1).
Then averaging over all a ∈ S,
f (1, . . . , 1) ≥ 1
|S|
∑
a,b ∈S
fa(b)
= 1
|S|
∑
µ
cµ
∑
a,b ∈S
Zµ (a, b ).
By Lemma 5.1, the inner sum is non-negative for µ ⁄= 0. If µ = 0, then
Z0(a, b ) = 1 for all a and b, and hence,
f (1) ≥ 1
|S| c0
∑
a,b ∈S
1
= c0|S|.
Equality holds if and only if fa(b) = 0 for every a ⁄= b ∈ S and for each
µ ⁄= 0, we have either cµ = 0 or ∑
a∈S Zµ,a = 0. (We will see in Section 9 that
when cµ > 0 for all |µ | ≤ deg(f ), this implies that we have a Grassmannian
t-design.)
By way of example, we consider the case of an {α }-code in detail.
Corollary 6.5. Let S be a subset of Gm,n such that tr(PaPb) = α for all a ⁄= b
in S, and α < m 2/n . Then
|S| ≤ n(m − α )
m2 − nα .
Proof. The ﬁrst two zonal orthogonal polynomials are Z0(y) = 1 and (up to
normalization) Z1(y) =∑ m
i=1 yi−m2/n . The annihilator for α is the polynomial
f (x) = x − α , which induces the zonal polynomial at subspace a given by
fa(b) = tr( PaPb) − α tr(Pb)
m =
m∑
i=1
yi − α,
16
for principle angles y1, . . . , y m of a and b. Thus we may write
f (y1, . . . , y m) =
m∑
i=1
yi − α
= c1Z1(y) +
(m2
n − α
)
Z0(y).
Applying Theorem 6.4, we ﬁnd that
|S| ≤ f (1, . . . , 1)
c0
= m − α
m2/n − α .
When m = 1, we recover Delsarte, Goethals and Seidel’s bound for com plex
equiangular lines:
|S| ≤ n(1 − α )
1 − nα .
Similarly, using the zonal orthogonal polynomials Z0, Z 1, Z 1, 1 and Z2, we
get a bound on the size of a subset containing two inner produc ts, say α and
β .
Corollary 6.6. Let S be a subset of Gm,n such that tr(PaPb) ∈ α, β for all
a ⁄= b in S. Further assume that
α + β ≤ 2(m2n − 4m + n)
n2 − 4 ,
α + β − nαβ
m2 < m2n − 2m + n
n2 − 1 .
Then
|S| ≤ n(m − α )(m − β )
m2
[
(m+1)2
2(n+1) + (m−1)2
2(n−1) − (α + β ) + nαβ
m2
] .
When m = 1 this reduces to the Delsarte, Goethals and Seidel bound of
|S| ≤ n(n + 1)(1 − α )(1 − β )
2 − (n + 1)(α + β ) + n(n + 1)αβ
for lines in complex projective space CP n−1.
17
