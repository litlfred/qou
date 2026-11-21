---
doc_id: physrevd108106023
doc_title: "Knot-quiver correspondence for double twist knots"
section_id: sec-003-a-colored-homfly-pt-polynomials-for-a-class-of-d
section_title: "Colored HOMFLY-PT polynomials for a class of double twist knots Kðp; −mÞ"
section_number: A
pages: 4-4
source_pdf: PhysRevD.108.106023.pdf
source_sha256: 50c7980e88cd21a0
toc_source: inferred
doc_brief: "Knot-quiver correspondence for double twist knots — 9 sections: Front matter; INTRODUCTION; Reverse engineering of Melvin-Mort"
---
of double twist knots Kðp; −mÞ
For given positive integers p and m, the Alexander
polynomial of a double twist knot of type Kðp; −mÞ takes
the form
ΔKðp;−mÞðxÞ ¼ 1 −ðpmÞX:
ð5Þ
Here, X ¼ ð1−xÞ2
x
. Such a linear expression appeared in
many knots [13], suggesting the inverse binomial expan-
sion to take the following form:
1
ΔKðp;−mÞðxÞN−1 ¼
X
∞
0≤k1≤…≤k2mp
 N þ k2mp −2
k2mp

×
Y
2mp−1
i¼1
 kiþ1
ki
 ð1 −xÞ2k2mp
xk2mp
:
ð6Þ
Further, using the quantum deformation procedure dis-
cussed in [13] and taking A →q2ðN ¼ 2Þ in Eq. (6), the
colored Jones polynomial can be written as
JrðKðp; −mÞ; qÞ ¼
X
d1þd2þþd4mpþ1¼r
ð−1Þ
P
i γidiq
P
ξidi
× q
P
i;j CKðp;−mÞ
i;j
didjðq2; q2Þr
Qm
i¼1ðq2; q2Þdi
;
ð7Þ
where CKðp;−mÞ
i;j
is ð4pm þ 1Þ × ð4pm þ 1Þ matrix for
quiver QKðp;−mÞ. It is worth noting that ξi ¼ αi þ 2βi
and γi are integer parameters that can be determined by
comparing them with r ¼ 1, 2, 3 [14,22]. By this approach,
we explicitly determined fξig, fγig parameters (7) for
Kð2;−2Þ ¼ 83 knot,
Jrð83; qÞ ¼
X
d1þd2þþd17¼r
ð−1Þ
P
i γidi
× ðq2; q2Þr
q
P
i;j Ci;jdidj
Q17
i¼1ðq2; q2Þdi
q
P
ξidi;
where
P
iγidi ¼d11 þd13 þd14 þd16 þd3 þd5 þd6 þd8,
P
i ξidi ¼ ðd11 −2d12 −d13 þ d14 þ 2d15 þ 3d16 þ 4d17
−2d2 −d3 −4d4 −3d5 −d6 þ d8 þ 2d9Þ.
The
quiver
matrix CKð2;−2Þ ¼ C83 is as follows:
0
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
@
0
−1
−1
−1
−1
0
0
0
0
−1
−1
−1
−1
0
0
0
0
−1
−2
−2
−3
−3
−2
−2
−1
−1
−2
−2
−3
−3
−2
−2
−1
−1
−1
−2
−1
−2
−2
−1
−1
0
0
−1
−1
−2
−2
−1
−1
0
0
−1
−3
−2
−4
−4
−3
−3
−1
−1
−2
−2
−4
−4
−3
−3
−1
−1
−1
−3
−2
−4
−3
−2
−2
0
0
−1
−1
−3
−3
−2
−2
0
0
0
−2
−1
−3
−2
−1
−1
0
0
−1
−1
−2
−2
−1
−1
0
0
0
−2
−1
−3
−2
−1
0
1
1
0
0
−1
−1
0
0
1
1
0
−1
0
−1
0
0
1
1
1
0
0
0
0
1
1
1
1
0
−1
0
−1
0
0
1
1
2
1
1
1
1
2
2
2
2
−1
−2
−1
−2
−1
−1
0
0
1
0
0
−1
−1
0
0
1
1
−1
−2
−1
−2
−1
−1
0
0
1
0
1
0
0
1
1
2
2
−1
−3
−2
−4
−3
−2
−1
0
1
−1
0
−2
−2
−1
−1
1
1
−1
−3
−2
−4
−3
−2
−1
0
1
−1
0
−2
−1
0
0
2
2
0
−2
−1
−3
−2
−1
0
1
2
0
1
−1
0
1
1
2
2
0
−2
−1
−3
−2
−1
0
1
2
0
1
−1
0
1
2
3
3
0
−1
0
−1
0
0
1
1
2
1
2
1
2
2
3
3
3
0
−1
0
−1
0
0
1
1
2
1
2
1
2
2
3
3
4
1
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
A
To give clarity to the readers, we present a step-by-step
procedure for determining the quiver matrix for the knot 83
in the Appendix. The polynomial invariants matches with
the closed form [14] for large value of r as well confirming
that the above 83 quiver data is indeed correct. Such an
exercise for Kð2; −2Þ suggested that we could propose and
conjecture CKðp;−mÞ for the double twist knot family. We
discuss them in the following section.
