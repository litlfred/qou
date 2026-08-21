---
doc_id: arxiv-math-0506456v1
doc_title: "Asymptotics of the quantum invariants for surgeries on the figure 8 knot"
section_id: sec-021-22-asymptotics-of-the-quantum-invariants-for-the
section_title: "Asymptotics of the quantum invariants for the ﬁgure 8 knot"
section_number: 22
pages: 21-23
source_pdf: 0506456v1.pdf
source_sha256: ce11210245a29eec
doc_brief: "Asymptotics of the quantum invariants for surgeries on the figure-8 knot (Andersen–Hansen, JKTR) — asymptotic expansion of the SU(2) Reshetikhin–Turaev invariants for surgeries on 4₁."
---
Conjecture 3. There exists surfaces Σ µ,ν,n
k,l,a,b ⊂ Ωµ,ν
k,l for (k,l ) ∈ { 0, 1}2, (a,b ) ∈
Fk,l, (µ,ν ) ∈ {±1}2 andn ∈ Z/|q|Z such that the leading order large r asymptotics
of the quantum invariant is given by
¯τr(Mp/q) ∼ isign(q)r
4
√
|q|
e
3πi
4 sign(pq) ∑
n∈Z/|q|Z
∑
(k,l)∈{0,1}2
∑
(a,b)∈Fk,l
∑
(µ,ν)∈{±1}2
µν
×
∫
Σ µ,ν,n
k,l,a,b
sin
(π
q (x − 2nd)
)
e2πirΦ a,b
n (x,y)dxdy. (4.37)
Moreover, ifp/q ⁄= 0 the surfaces Σ µ,ν,n
k,l,a,b ⊂ Ωµ,ν
k,l can be chosen such that any critical
point of Φ a,b
n belonging to Σ µ,ν,n
k,l,a,b also belongs to the set S in (1.5).
The rational behind this conjecture is that we anticipate an analysis of the
expression (4.34) paralleling our analysis of J ′
K(r) should be applicable. I.e. tan and
cot should be approximated by ±√
−1 depending on the signs of Im( y) and Im(x)
and ¯fn,r(x,y ) by∑
(a,b)∈Fk,l
sin
(
π
q (x − 2nd)
)
e2πirΦ a,b
n (x,y) for some deformation of
the part of C1
r ×C2
r which is contained in Ω k,l. We have partial analytic results
supporting this conjecture. The factor in front of the sum is simply the leading
term in the large r asymptotics of β1(r), see (4.35). In case p/q = 0 our results in
Appendix C show that we have to include critical points not belonging t o S in our
surfaces Σ µ,ν,n
k,l,a,b.
In the remaining part of this section we will compute the large r asymptotics of
the right-hand side of (4.37). The only task left is to calculate the lea ding term in
the large r asymptotic of the integrals
I =
∫
Σ µ,ν,n
k,l,a,b
sin
(π
q (x − 2nd)
)
e2πirΦ a,b
n (x,y)dxdy, (4.38)
where k,l ∈ { 0, 1}, (a,b ) ∈ Fk,l, µ,ν ∈ {± 1} and n ∈ Z. By the properties of
the surfaces Σ µ,ν,n
k,l,a,b postulated in Conjecture 3 this leading asymptotics should be
calculable by the saddle point method. Let us give some details. Assum e that
(x0,y 0) is a critical point of Φ = Φ a,b
n belonging to the surface Σ = Σ µ,ν,n
k,l,a,b and
assume that
Im ((Φ(x,y ) − Φ(x0,y 0))) ≥ 0
for all (x,y ) in a small neighborhood of ( x0,y 0) in Σ with equality only in ( x0,y 0).
In this case we say that Σ pass through the critical point ( x0,y 0) in the directions
of steepest descent. Moreover, assume this is satisﬁed for all cr itical points of Φ
inside Σ. Then the main contribution to the integral I in the large r limit is given
by integrating over small neighborhoods of the critical points in Σ.
Let us therefore begin by computing the stationary points of Φ a,b
n . To this end,
it is more convenient to work with the functions
Ψ a,b
n (x,y ) = ax +by + Φn(x,y ), (4.39)
a,b,n ∈ Z, so Φ a,b
n = Ψ a+b,a−b
n .
22 Asymptotics of the quantum invariants for the ﬁgure 8 knot
Let a,b,n ∈ Z and put Ψ = Ψ a,b
n . Let z =e2πix and w =e2πiy. Then
2πi∂Ψ
∂x (x,y ) = 2πi(a −y) − p
2q 2πix + 2πin
q + Log(1 −zw) − Log(1 −zw −1),
2πi∂Ψ
∂y (x,y ) = 2πi(b −x) + Log(1 −zw) + Log(1 −zw −1), (4.40)
where we have to assume (which we will also assume in what follows) tha t both zw
and zw −1 are diﬀerent from 1.
We will need to specify a certain square root of z, namely let v = eπix. Then
∂Ψ
∂x (x,y ) = 0 implies that
v−p =
(w −v2
1 −v2w
) q
, (4.41)
and ∂Ψ
∂y (x,y ) = 0 implies that
(1 −v2w)(w −v2) = v2w. (4.42)
Both equations (4.41) and (4.42) are independent of a, b, and n. We note that
(v,w ) = (0 , 0) is the only solution to (4.42) with v or w equal to zero. Note,
moreover, that (v,w ) is a common solution to (4.41) and (4.42) if and only if (¯ v, ¯w)
is a common solution to these two equations. By writing (4.41) as
(−1)qvp+2q =
( 1 −v2w
1 −v−2w
) q
and (4.42) as
(1 −v2w)(1 −v−2w) = −w
we see that ( v,w ) is a nonzero solution to (4.41) and (4.42) if and only if ( v−1,w )
is such a solution. If p is even, then ( v,w ) is a solution to (4.41) and (4.42) if and
only if ( −v,w ) is such a solution.
Let us oppositely begin with a common solution ( v,w ) ∈ C∗ × C∗ to (4.41)
and (4.42), where, as usual, C∗ = C \ {0}. Write v = eπix and w = e2πiy with
Re(x) ∈] − 1, 1] and Re( y) ∈] − 1/2, 1/2], i.e. x = 1
πi Log(v) and y = 1
2πi Log(w).
One now easily deduce from (4.42) that there exists a unique b ∈ Z such that
0 = 2πi(b −x) + Log
(
1 −e2πi(x+y)
)
+ Log
(
1 −e2πi(x−y)
)
, (4.43)
and from (4.41) we deduce that there exists a unique n ∈ Z such that
0 = −2πiy − p
qπix + 2πin
q + Log
(
1 −e2πi(x+y)
)
− Log
(
1 −e2πi(x−y)
)
. (4.44)
That is, there exists a unique pair of integers b,n such that ( x,y ) is a stationary
point of Ψ 0,b
n .
