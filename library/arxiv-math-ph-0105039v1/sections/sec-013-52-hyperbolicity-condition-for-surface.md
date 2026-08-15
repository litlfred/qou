---
doc_id: arxiv-math-ph-0105039v1
doc_title: "December 23, 2000 (Revised Edition) Hyperbolic Structure Arising from a Knot Invariant Kazuhiro HIKAMI †"
section_id: sec-013-52-hyperbolicity-condition-for-surface
section_title: "Hyperbolicity Condition for Surface"
section_number: 5.2
pages: 18-20
source_pdf: 0105039v1.pdf
source_sha256: 850e6a00721e38d0
doc_brief: "December 23, 2000 (Revised Edition) Hyperbolic Structure Arising from a Knot Invariant Kazuhiro HIKAMI † — We study the knot invariant based on the quantum dilogarithm function."
---
We ﬁrst consider a surface Da, which is surrounded by alternating crossings as in Fig. 7. W e
assign octahedron for each crossing following eq. (5.7), and introduce variables as shown there. A
contribution to the invariant τ1(L) from above segment of link L is thus given by
∫ ∫ ∫
dp1 · · · dpn
n−1∏
i=0
⟨pi+1, xi+1 | S−1 | yi, pi⟩, (5.12)
18
Da
/d50/d50/d50
/d50/d50/d50
/d50/d50/d50/d50/d50/d50/d50/d50/d50/d50/d50/d50/d50
/d50/d50/d50/d50/d50/d50/d50/d50/d50/d50/d50/d50/d50
/d13/d13/d13
/d13/d13/d13
/d13/d13/d13/d13/d13/d13/d13/d13/d13/d13/d13/d13/d13
/d13/d13/d13/d13/d13/d13/d13/d13/d13/d13/d13/d13/d13
/d50/d50/d50
/d50/d50/d50
/d50/d50/d50/d50/d50/d50/d50/d50/d50/d50/d50/d50/d50
/d50/d50/d50/d50/d50/d50/d50/d50/d50/d50/d50/d50/d50
/d13/d13/d13
/d13/d13/d13
/d13/d13/d13/d13/d13/d13/d13/d13/d13/d13/d13/d13/d13
/d13/d13/d13/d13/d13/d13/d13/d13/d13/d13/d13/d13/d13
⊗
⊗⊗
⊗
⊗⊗
/d7/d7/d15
/d15
/d15
/d15/d37/d37/d76 /d76 /d76 /d76
/d76 /d76 /d76 /d76
/d101/d101/d76 /d76 /d76 /d76
/d76 /d76 /d76 /d76/d71/d71/d15
/d15
/d15
/d15
/d47/d47/d95/d95 /d95 /d95
/d15/d15/d31
/d31
/d31
/d31
/d31
/d31
/d31
/d31 /d79/d79/d31
/d31
/d31
/d31
/d31
/d31
/d31
/d31
/d111/d111/d95 /d95/d95 /d95
/d47/d47/d95 /d95/d95 /d95
/d79/d79/d31
/d31
/d31
/d31
/d31
/d31
/d31
/d31/d15/d15/d31
/d31
/d31
/d31
/d31
/d31
/d31
/d31
/d111/d111/d95/d95 /d95 /d95
/d87/d87/d47
/d47
/d47
/d47 /d57/d57/d114/d114/d114/d114
/d114/d114/d114/d114
/d121/d121/d114/d114/d114/d114
/d114/d114/d114/d114 /d23/d23/d47
/d47
/d47
/d47
/d71/d71/d15
/d15
/d15
/d15 /d101/d101/d76/d76/d76/d76
/d76/d76/d76/d76
/d37/d37/d76/d76/d76/d76
/d76/d76/d76/d76 /d7/d7/d15
/d15
/d15
/d15
/d23/d23/d47
/d47
/d47
/d47/d121/d121/d114 /d114 /d114 /d114
/d114 /d114 /d114 /d114
/d57/d57/d114 /d114 /d114 /d114
/d114 /d114 /d114 /d114/d87/d87/d47
/d47
/d47
/d47
p′
1
p1
p′
2
p2
p′
3
p3
p′
n
pn
x1
y1
x2
y2
x3
y3
yn
xn
①
②
③
Figure 7: A segment of linkL which is surrounded by alternating crossings is depicted. We number
each vertex as①,②, . . ..
where we use y0 = yn and p0 = pn. By substituting an asymptotic form (4.1), we get pi+1 =
p1 + ∑ i
j=1 yj for i > 0, and the integral reduces to
δ(y1 + · · · + yn) ·
∫
dp1 exp 1
2 i γ
( n−1∑
i=0
( π2
6 − Li2(exi+1−pi) − xi+1 yi
)
+
∑
1≤i<j≤n
yi yj
)
.
We evaluate this integral at the saddle point, whose condition is
n−1∏
i=0
(
1 − exi+1−pi
)
= 1. (5.13)
This equation coincides with the hyperbolicity condition f or gluing n tetrahedra in surface Da
along an axis parallel to axes ⊗ in Fig. 7 (see also Fig. 14 and Fig. 16 for n = 3 and n = 2 cases).
We can see that the same correspondence occurs for non-alternating case. We suppose a surface
Da is surrounded like Fig. 7 whereas each vertex i is either over-crossing
Da
or under-crossing
Da
, which we denote i ∈ O and i ∈ U respectively. In this case a contribution to the invariant is
19
given by
∫ ∫ ∫
dp1 · · · dpn
∏
i∈O
⟨pi+1, xi+1 | S−1 | yi, pi⟩ ·
∏
i∈U
⟨xi+1, pi+1 | S | pi, yi⟩. (5.14)
By substituting an expression (4.1) we obtain
pk+1 = p1 +
∑
1≤i≤k
i∈O
yi −
∑
1≤i≤k
i∈U
xi+1,
∑
i∈O
yi =
∑
i∈U
xi+1,
and the integral becomes
δ(
∑
i∈O
yi −
∑
i∈U
xi+1)
∫
dp1 exp 1
2 i γ
( ∑
i∈O
( π2
6 − Li2(exi+1−pi) − xi+1 yi
)
+
∑
i∈U
(
−π2
6 + Li2(eyi−pi+1) + xi+1 yi
)
+
∑
i,j ∈O
i<j
yi yj −
∑
i∈U
j∈O
xi+1 yj +
∑
i,j ∈U
i≤j
xi+1 xj+1
)
.
The saddle point equation is given as
∏
i∈O
(
1 − exi+1−pi
)
·
∏
i∈U
(
1 − eyi−pi+1
) −1
= 1, (5.15)
which coincides with the hyperbolicity equation around an axis in Da parallel to axes ⊗.
