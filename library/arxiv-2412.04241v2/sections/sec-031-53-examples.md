---
doc_id: arxiv-2412.04241v2
doc_title: "THE HABIRO RING OF A NUMBER FIELD"
section_id: sec-031-53-examples
section_title: "Examples"
section_number: 5.3
pages: 65-68
source_pdf: 2412.04241v2.pdf
source_sha256: 308d1dd1c42bd979
doc_brief: "THE HABIRO RING OF A NUMBER FIELD — We introduce the Habiro ring of a number field K and modules over it graded by K3(K)."
---
for some different ground rings. We will illustrate how one can test whether a Galois invariant
function near roots of unity is actually an element of a Habiro ring.
Example 5.6. Recall the Kashaev invariant of the trefoil from equation (5) (often called
the Kontsevich-Zagier series). We can compute the first few terms in the expansions at
66 STA VROS GAROUF ALIDIS, PETER SCHOLZE, CAMPBELL WHEELER, AND DON ZAGIER
ζ1,ζ 2,ζ 3,ζ 4 (with q =ζm(1−u))
F31,1(u) = 1 + u + 2u2 + 5u3 + O(u4),
F31,2(u) = 3 + 11 u + O(u2),
F31,3(u) = 5 −ζ3 + O(u),
F31,4(u) = 8 − 3ζ4 + O(u).
(334)
These give rise to the vector
( γ1,1,0| γ2,1,0 γ1,2,0| γ3,1,0 γ3,1,1 γ1,3,0| γ4,1,0 γ4,1,1 γ2,2,0 γ1,4,0 )
= ( 1 | 3 1 | 5 −1 2 | 8 −3 11 5 ) ,
(335)
which when multiplied by M−1
5 gives the expected
( a1,0| a2,0 a2,1| a3,0 a3,1 a3,2| a4,0 a4,1 a4,2 a4,3)
= ( 1 | 1 0 | 1 0 0 | 1 0 0 0) . (336)
To see just how delicate the property of being in the Habiro ring is, notice that simply
changing the number γ1,1,0 from 1 to 2 by would give the sequence

2

 3
4
1
4

 65
72
−1
72
17
72

 275
288
−7
144
1
32
17
72

, (337)
where the integrality has been completely ruined.
Example 5.7. In this example we will see what the introduction of denominators does to
the Habiro ring. The Habiro function F (q)∈ HQ whose image under ι is the collection of
(constant) power series
F (ζm(1−u)) =

1 if m is odd,
0 if m is even (338)
does not belong to HZ, but is an element of HZ[1/2]. Indeed, it can be written
F (q) = 1+ 1
4(−1+q) (q;q)1+ 1
8(1−q+q2) (q;q)2+ 1
32(−5+2q+q2+4q3) (q;q)3+··· . (339)
Similarly, the element G(q) = F (q2)−F (q), whose image under ι is the collection of (con-
stant) power series
G(ζm(1−u)) =

1 if m ≡ 2 (mod 4)
0 otherwise , (340)
is also an element of HZ[1/2], and can be written
G(q) = 1
4(1−q) (q;q)1 + 1
8(−1 +q−q2) (q;q)2 + 1
32(1− 2q + 3q2− 4q3) (q;q)3 +··· . (341)
Example 5.8. Our final example is an element of the Habiro ring of the ring of integers,
with 1/23 adjoined, of the field K = Q(α)/(α3−α2 + 1), the cubic field of discriminant
THE HABIRO RING OF A NUMBER FIELD 67
−23, associated to the Kashaev invariant of the knot 5 2. We define a collection of series
(Ψ52,m)m≥1 using the residue formulas given in Section 4.1. Specifically, we define
Ψ52,m(u) := Res
wm=z
J52(1,w,ζ m(1−u))dw
w , (342)
where
J52(t,w,q ) :=
∞X
k=0
qk(k+1)w2k
(qw;q)3
k
tk (343)
and setz = 1−α2 so thatz2(1−z)−3 = 1. The collection Ψ 52,m is related to the symmetrised
series f (52)(q)f (52)(q−1) discussed in Section 4.6. For example, equation (283) is equal to
(3α− 2)Ψ52,1(−x). One can compute the first few coordinates via the expansions
Ψ52,1(u) = 1
23(−9α2 + 3α + 2) + 1
234 (444α2 + 3417α− 1287)u2
+ 1
234 (444α2 + 3417α− 1287)u3 + O(u4),
Ψ52,2(u) = 1
23(−43α2 + 22α + 7) + O(u2),
Ψ52,3(u) = 1
23(−111α2 + 60α + 17) + O(u),
Ψ52,4(u) = 1
23(−242α2 + 119α + 41) + O(u),
(344)
giving rise to the vector


γ1,1,0
γ2,1,0
γ1,2,0
γ3,1,0
γ3,1,1
γ1,3,0
γ4,1,0
γ4,1,1
γ2,2,0
γ1,4,0


=


1
23(−9α2 + 3α + 2)
1
23(−43α2 + 22α + 7)
0
1
23(−111α2 + 60α + 17)
0
1
234 (444α2 + 3417α− 1287)
1
23(−242α2 + 119α + 41)
0
0
1
234 (444α2 + 3417α− 1287)


. (345)
(That the coordinates here are in K as opposed to K[ζm] is because ϕ(m)≤ 2 for m< 5 and
Ψ52 is a symmetrisation; in general, the coordinates are in K[ζm +ζ−1
m ].) This vector when
68 STA VROS GAROUF ALIDIS, PETER SCHOLZE, CAMPBELL WHEELER, AND DON ZAGIER
multiplied by M−1
5 gives the vector


1
23(−9α2 + 3α + 2)
1
92(−34α2 + 19α + 5)
1
92(34α2− 19α− 5)
1
6716184(−5376038α2 + 3018917α + 785707)
1
6716184(2070166α2− 1142197α− 309323)
1
6716184(4552234α2− 2529235α− 674333)
1
26864736(−22020494α2 + 10246115α + 3924793)
1
13432368(−5376038α2 + 3018917α + 785707)
1
8954912(10100386α2− 4938301α− 1720695)
1
6716184(4552234α2− 2529235α− 674333)


, (346)
which has denominator 26864736 = 2 5· 3· 234. If we instead apply the correct Frobenius
automorphism and then multiply by M−1
5 we find


γ1,1,0
φ2(γ2,1,0)
γ1,2,0
φ3(γ3,1,0)
φ3(γ3,1,1)
γ1,3,0
φ4(γ4,1,0)
φ4(γ4,1,1)
φ2(γ2,2,0)
γ1,4,0


= 1
234


225α2 + 213α + 142
241α2 + 113α + 74
0
279α2 + 132α + 151
0
156α2 + 249α + 153
161α2 + 115α + 4
0
0
156α2 + 249α + 153


(mod 288),


a1,0
a2,0
a2,1
a3,0
a3,1
a3,2
a4,0
a4,1
a4,2
a4,3


= 1
234


225α2 + 213α + 142 (mod 288)
4α2 + 47α + 55 (mod 72)
68α2 + 25α + 17 (mod 72)
0 (mod 4)
2α2 + 2α (mod 4)
2α2 + 3α + 1 (mod 4)
0 (mod 1)
0 (mod 1)
0 (mod 1)
0 (mod 1)


,
(347)
where now everything is integral away from the prime 23.
