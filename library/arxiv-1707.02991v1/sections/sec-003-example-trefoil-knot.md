---
doc_id: arxiv-1707.02991v1
doc_title: "BPS states, knots and quivers"
section_id: sec-003-example-trefoil-knot
section_title: "Example – trefoil knot"
section_number: null
pages: 4-5
source_pdf: 1707.02991v1.pdf
source_sha256: f4f539f74403dd24
doc_brief: "BPS states, knots and quivers — 5 sections: BPS states, knots and quivers; Moduli of quiver representations; Knot invariants from quiver repres"
---
We illustrate the above correspondence in the exam-
ple of trefoil knot, whose reduced colored HOMFLY-PT
polynomials arise by setting t =−1 in (8). Using the
q-binomial identity (z;q)k = ∑
i
[k
i
]
(−z)iq
i(i−1)
2 , the q-
binomial and the last product in (8) take form
[r
k
](a2
q2 ;q2)
k =
k∑
i=0
(q2;q2)r
(
− a2
q2
)i
qi(i−1)
(q2;q2)r−k(q2;q2)i(q2;q2)k−i
.
Introducingr =d1+d2+d3,k =d2+d3,i =d3 withdi≥
0, and normalizing Pr(a,q ) by (q2;q2)r, the generating
5
function (4) can be rewritten as in (12)
P (x) =
∞∑
r=0
Pr(a,q )
(q2;q2)r
xr =
∑
d1,d2,d3≥0
q
∑
i,jCi,jdidj−2d1−3d3(−1)d3a2d1+2d2+4d3x
∑
idi
(q2;q2)d1(q2;q2)d2(q2;q2)d3
(14)
with C =


0 1 1
1 2 2
1 2 3

. The corresponding quiver is shown
in ﬁg. 1 and, as we claimed above, its vertices corre-
spond to generators of HOMFLY-PT homology. Fur-
thermore, diagonal elements (0 , 2, 3) of matrix C (rep-
resenting numbers of loops at vertices of the quiver) in-
deed agree with homological degrees encoded in the un-
colored superpolynomial (9), coeﬃcients li =−2, 0, 3 of
linear terms in di in the power of q in (14) are given by
li =qi−ti, coeﬃcientsai = 2, 2, 4 in the power ofa agree
with a-degrees of generators of HOMFLY-PT homology,
and additional minus sign (−1)d3 is determined by just
one generator with odd t-degree t3 = 3.
We stress that rewriting of the generating function of
colored HOMFLY-PT polynomials in the form (14) guar-
antees that it can be written in the product form (11),
so that LMOV invariants are expressed as combinations
(with integer coeﬃcients) of integer motivic Donaldson-
Thomas invariants Ω d1,d2,d3;j. This proves the LMOV
conjecture for 31 knot, for all symmetric representations.
Analogous calculations can be performed for other
knots, e.g. rewriting formulas for colored superpolyno-
mials in [30]. A general formalism facilitating such com-
putations and their consequences is presented in [34].
