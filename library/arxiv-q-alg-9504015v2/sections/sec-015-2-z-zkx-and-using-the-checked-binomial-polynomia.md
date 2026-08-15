---
doc_id: arxiv-q-alg-9504015v2
doc_title: "Witten’s Invariants of Rational Homology Spheres at Prime"
section_id: sec-015-2-z-zkx-and-using-the-checked-binomial-polynomia
section_title: "Z ZK[x] and using the “checked binomial polynomial”"
section_number: 2
pages: 15-17
source_pdf: 9504015v2.pdf
source_sha256: ea5588225a393477
doc_brief: "Witten’s Invariants of Rational Homology Spheres at Prime — We establish a relation between the coeﬃcients of asymptotic expan sion of the trivial connection contribution to Witten’s invariant of"
---
P ∨
m(α) = ( m!)∗α(α − 1) · · ·(α − m + 1) = ( m!)∗
m∑
l=0
Cm,lαl, (3.6)
we ﬁnd that



K−1∑
m=0
[ m
2 ]∑
l=0
(m!)∗Cm,2lG(p, q; l)4ln2lxm−l



⋄
=
( pq∗
K
)



K−1
2∑
m=0
xm
m∑
l=0
(m!)∗Cm,l(−1)l(p∗q)ln2l



⋄
(3.7)
We limited the sum over m in the l.h.s. of this equation to m ≤ K − 1 because for m ≥ K
the minimum power of xm−l is greater that K−1
2 . Note that since m ≤ K − 1, then ( m!)∗ is
well deﬁned.
If we substitute the expansion
[G(p, q; l)]⋄ =
K−1
2 −l∑
m=0
Gm(p, q; l) xm + x
K+1
2 −lw, w ∈ Z Z[ˇq] (3.8)
into eq. (3.7), then we can ﬁnd all the coeﬃcients Gm(p, q; l) by equating the coeﬃcients of
l.h.s. and r.h.s. of eq. (3.7) at equal powers of x and n. These coeﬃcients have to be equal
due to the following simple lemma:
Lemma 3.1 If a degree of a polynomial P (n) ∈ Z ZK[n] is less than K and P (n) = 0 for all
n ∈ Z ZK, then all the coeﬃcients of P (n) are zero modulo K.
14
The proof follows from the fact that the K × K Van-der-Monde determinant in Z ZK is
non-zero.
Each gaussian sum G(p, q; l) appears in the l.h.s. of eq. (3.7) with its own power of n:
n2l. Therefore the coeﬃcients Gm′(p, q; l) of eq. (3.8) can be calculated by “dividing” the
polynomial ( −1)l(p∗q)l∑ K−1
2
m=l (m!)∗Cm,lxm appearing at n2l in the r.h.s. of eq. (3.7) by the
polynomial
∑ K−1
m=2l Cm,2l4lxm−l appearing in the r.h.s. of that equation at the same power
on n. The division is not quite well-deﬁned, hence the indeterminacy in the e lements w of
eq. (3.8).
This whole calculation of dividing the polynomials can be made more explicit if we go
back to eq. (3.5) and make the following substitutions:
ˇq2nα = e2nα log(1+x) =
∞∑
l=0
(2nα)l
l! (log(1 + x))l, (3.9)
ˇq−pq∗n2
= e−pq∗n2 log(1+x) =
∞∑
l=0
(−1)l (pq∗n2)l
l! (log(1 + x))l. (3.10)
After “checking” the logarithm
log∨(1 + x) = x
K−2∑
n=0
(−1)n(n + 1)∗xn (3.11)
we see that eq. (3.7) transforms into



K−1
2∑
l=0
G(p, q; l)(2n)2l((2l)!)∗(log∨(1 + x))l
(
log∨(1 + x)
x
) l



⋄
(3.12)
=
( pq∗
K
)



K−1
2∑
l=0
(−1)ln2l(pq∗)l(l!)∗(log∨(1 + x))l



⋄
.
Thus we ﬁnd that
[G(p, q; m)]⋄ = ( −1)m
( pq∗
K
)
(2∗)2m(2m)!(m!)∗
[(
x
log∨(1 + x)
) m] ⋄
+x
K+1
2 −mw, w ∈ Z Z[ˇq]. (3.13)
Consider now the following identity which is an integral analog of eq. (3 .5):
∫ +∞
−∞
dα ˇq
p
q α2
ˇq2nα = ei π
4 sign( p
q )
( K
2
) 1
2
⏐
⏐
⏐
⏐
⏐
q
p
⏐
⏐
⏐
⏐
⏐
1
2
ˇq− q
p n2
. (3.14)
15
After substituting eqs. (3.9), (3.10) we ﬁnd that
∫ +∞
−∞
dα ˇq
p
q α2
α2mxm = ei π
4 sign( p
q )
( K
2
) 1
2
⏐
⏐
⏐
⏐
⏐
q
p
⏐
⏐
⏐
⏐
⏐
1
