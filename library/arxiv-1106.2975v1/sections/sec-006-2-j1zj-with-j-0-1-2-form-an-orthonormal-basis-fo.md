---
doc_id: arxiv-1106.2975v1
doc_title: "The Polyanalytic Ginibre Ensembles"
section_id: sec-006-2-j1zj-with-j-0-1-2-form-an-orthonormal-basis-fo
section_title: "(j+1)zj, with j = 0, 1, 2, . . ., form an orthonormal basis for the"
section_number: 2
pages: 22-23
source_pdf: 1106.2975v1.pdf
source_sha256: 7e966c7392b70ae0
doc_brief: "The Polyanalytic Ginibre Ensembles — For integers n, q = 1, 2, 3, . . ., let Poln,q denote the C-linear space of polynomials in z and ¯z, of degree ≤n −1 in z and of degree ≤q −1 in ¯z."
---
space A2
m,1(C). The functions Tm,r[ej,m] are computed using Proposition 4.2 above,
and we then recognize that we can identify them with the basis elements which
appear in Proposition 2.1. We clearly have that
span
n
Tm,r[ej,m] : 0 ≤j ≤n −1, 0 ≤r ≤q −1
o
= Polm,n,q,
and in view of the orthogonality properties in Proposition 2.1, we also must have
(4.1)
span{Tm,r[ej,m] : 0 ≤j ≤n −1} = Polm,n,r+1 ⊖Polm,n,r,
where the “⊖” is with respect to the inner product in L2(C, e−m|z|2). Following
Vasilevski [25], then, we deﬁne the pure polyanalytic Fock space of level r + 1:
(4.2)
δPolm,n,r+1 := Polm,n,r+1 ⊖Polm,n,r,
δA2
m,n,r+1(C) := A2
m,r+1(C) ⊖A2
m,r(C),
with the understanding that Polm,n,0 := {0} and A2
m,0(C) := {0}. The operator Tm,r
now becomes an isometric isomorphism
Tm,r : A2
m,1(C) →δA2
m,n,r+1(C),
Tm,r : Polm,n,1 →δPolm,n,r+1.
The Polyanalytic Ginibre Ensembles
23
We obtain the orthogonal decompositions
Polm,n,q =
q−1
M
r=0
δPolm,n,r+1,
A2
m,q(C) =
q−1
M
r=0
δA2
m,r+1(C).
As a consequence, if Kδ:m,n,r+1 and Kδ:m,r+1 denote the reproducing kernels for the
spaces δPolm,n,r+1 and δA2
m,r+1(C), respectively, we must have that
Km,n,q =
q−1
X
r=0
Kδ:m,n,r+1,
Km,q =
q−1
X
r=0
Kδ:m,r.
(4.3)
The poly-Bargmann transforms. For m = 1, the poly-Bargmann transform of level
r is deﬁned by
Br[ f] := Tr ◦B[ f].
Proposition 4.3. We have
Br[ f](z) =
1
(2π)1/4 √
r!
Z
R
f(t)Hr(t −z −¯z) etz−1
2 z2−1
4 t2dt,
r = 0, 1, 2, . . . .
Proof. We proceed by induction. For r = 0, the formula reduces to the usual
Bargmann transform (if we recall that H0 = 1). By the induction hypothesis, we
suppose therefore that the formula is valid for all integers up to r −1. From the
semi-group property T1 ◦Tr−1 = r1/2Tr, we see that
Br[ f] = Tr ◦B[ f] = r−1/2T1 ◦Tr−1 ◦B[ f](z) = r−1/2T1 ◦Br−1[ f].
Since the formula holds for r −1, the following calculation shows that it holds for
r as well:
r−1/2e|z|2∂z

[(r −1)!]−1/2Hr−1(t −z −¯z) etz−1
2 z2−1
4 t2e−|z|2
= (r!)−1/2 
−H′
r−1(t −z −¯z) + (t −z −z)Hr−1(t −z −¯z)

etz−1
2 z2−1
4 t2
= (r!)−1/2Hr(t −z −¯z)etz−1
2 z2−1
4 t2;
here, we used the standard identity Hr(x) = xHr−1(x) −H′
r−1(x). The proof is com-
plete.
□
