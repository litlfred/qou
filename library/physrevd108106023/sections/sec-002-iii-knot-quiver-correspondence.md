---
doc_id: physrevd108106023
doc_title: "Knot-quiver correspondence for double twist knots Vivek Kumar Singh *"
section_id: sec-002-iii-knot-quiver-correspondence
section_title: "KNOT-QUIVER CORRESPONDENCE"
section_number: III
pages: 3-5
source_pdf: PhysRevD.108.106023.pdf
source_sha256: 50c7980e88cd21a0
---
106023-3
rewrite r-colored Jones as a motivic series to extract the
matrix of the quiver QKðp;−mÞ.
A. Colored HOMFLY-PT polynomials for a class
of double twist knots Kðp; − mÞ
For given positive integers p and m, the Alexander
polynomial of a double twist knot of type Kðp; −mÞ takes
the form
ΔKðp;−mÞðxÞ¼ 1 − ðpmÞX: ð5Þ
Here, X ¼ ð1−xÞ2
x . Such a linear expression appeared in
many knots [13], suggesting the inverse binomial expan-
sion to take the following form:
1
ΔKðp;−mÞðxÞN−1 ¼
X∞
0≤k1≤… ≤k2mp
/C18N þ k2mp − 2
k2mp
/C19
×
Y2mp−1
i¼1
/C18kiþ1
ki
/C19ð1 − xÞ2k2mp
xk2mp
: ð6Þ
Further, using the quantum deformation procedure dis-
cussed in [13] and taking A → q2ðN ¼ 2Þ in Eq. (6), the
colored Jones polynomial can be written as
JrðKðp; −mÞ;q Þ¼
X
d1þd2þ/C1/C1/C1þ d4mpþ1¼r
ð−1Þ
P
i γidi q
P
ξidi
× q
P
i;j CKðp;−mÞ
i;j didj ðq2; q2ÞrQm
i¼1ðq2; q2Þdi
; ð7Þ
where CKðp;−mÞ
i;j is ð4pm þ 1Þ × ð4pm þ 1Þ matrix for
quiver QKðp;−mÞ. It is worth noting that ξi ¼ αi þ 2βi
and γi are integer parameters that can be determined by
comparing them with r ¼ 1,2 ,3 [14,22]. By this approach,
we explicitly determined fξig, fγig parameters (7) for
Kð2;−2Þ ¼ 83 knot,
Jrð83;q Þ¼
X
d1þd2þ/C1/C1/C1þ d17¼r
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
ξidi ;
where P
i γidi ¼ d11 þ d13 þ d14 þ d16 þ d3 þ d5 þ d6 þ d8,P
i ξidi ¼ð d11 − 2d12 − d13 þ d14 þ 2d15 þ 3d16 þ 4d17
−2d2 − d3 − 4d4 − 3d5 − d6 þ d8 þ 2d9Þ. The quiver
matrix CKð2;−2Þ ¼ C83 is as follows:
0
BBB
BBBBBBB
BBBBBBBBB
BBBBBBB
BBBBBBB
BBBBB@
0
−1 −1 −1 −1 0000 −1 −1 −1 −1 0000
−1 −2 −2 −3 −3 −2 −2 −1 −1 −2 −2 −3 −3 −2 −2 −1 −1
−1 −2 −1 −2 −2 −1 −10 0 −1 −1 −2 −2 −1 −10 0
−1 −3 −2 −4 −4 −3 −3 −1 −1 −2 −2 −4 −4 −3 −3 −1 −1
−1 −3 −2 −4 −3 −2 −20 0 −1 −1 −3 −3 −2 −20 0
0 −2 −1 −3 −2 −1 −10 0 −1 −1 −2 −2 −1 −10 0
0 −2 −1 −3 −2 −10 1 1 00 −1 −1 0011
0 −10 −10 0111 0000 1111
0 −10 −10 0112 1111 2222
−1 −2 −1 −2 −1 −10 0 1 00 −1 −1 0011
−1 −2 −1 −2 −1 −10 0 1 0100 1122
−1 −3 −2 −4 −3 −2 −10 1 −10 −2 −2 −1 −11 1
−1 −3 −2 −4 −3 −2 −10 1 −10 −2 −1 0022
0 −2 −1 −3 −2 −10 1 2 01 −10 1122
0 −2 −1 −3 −2 −10 1 2 01 −10 1233
0 −10 −10 0112 1212 2333
0 −10 −10 0112 1212 2334
1
CCC
CCCCCCC
CCCCCCCCC
CCCCCCC
CCCCCCC
CCCCCA
To give clarity to the readers, we present a step-by-step
procedure for determining the quiver matrix for the knot 83
in the Appendix. The polynomial invariants matches with
the closed form [14] for large value of r as well confirming
that the above 83 quiver data is indeed correct. Such an
exercise for Kð2; −2Þ suggested that we could propose and
conjecture CKðp;−mÞ for the double twist knot family. We
discuss them in the following section.
III. KNOT-QUIVER CORRESPONDENCE
OF DOUBLE TWIST KNOTS Kðp; − mÞ
We observe that the quiver matrix has a block structure
by performing a similar analysis of the previous section for
other examples of the double twist knots Kðp; −mÞ.O u r
explicit computation suggests the following proposition.
Proposition. The r-colored Jones polynomial for double
twist knots Kðp; −mÞ, with p ≥ m, can be expressed in the
quiver representation,
JrðKðp; −mÞ; qÞ¼
X
d1þd2þ/C1/C1/C1þ d4pmþ1¼r
ð−1ÞΛðp;−mÞ qΞðp;−mÞ
× ðq2; q2ÞrQ4pmþ1
i¼1 ðq2; q2Þdi
q
P
i;j CKðp;−mÞdidj ;
ð8Þ
where the linear term Ξðp;−mÞ ≡ P
i ξidi, phase factor
Λðp;−mÞ ≡ P
i γidi.
The block structure of the matrix CKðp;−mÞ for some
examples lead to the following conjecture:
Conjecture. The generic structure of the quiver matrix
will take the form
VIVEK KUMAR SINGH et al. PHYS. REV . D 108, 106023 (2023)
106023-4
CKðp;−mÞ ¼
0
BB
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
F
