---
doc_id: physrevd108106023
doc_title: "Knot-quiver correspondence for double twist knots"
section_id: sec-004-iii-knot-quiver-correspondence
section_title: "KNOT-QUIVER CORRESPONDENCE"
section_number: III
pages: 4-7
source_pdf: PhysRevD.108.106023.pdf
source_sha256: 50c7980e88cd21a0
toc_source: inferred
doc_brief: "Knot-quiver correspondence for double twist knots — 9 sections: Front matter; INTRODUCTION; Reverse engineering of Melvin-Mort"
---
OF DOUBLE TWIST KNOTS Kðp; −mÞ
We observe that the quiver matrix has a block structure
by performing a similar analysis of the previous section for
other examples of the double twist knots Kðp; −mÞ. Our
explicit computation suggests the following proposition.
Proposition. The r-colored Jones polynomial for double
twist knots Kðp; −mÞ, with p ≥m, can be expressed in the
quiver representation,
JrðKðp; −mÞ; qÞ ¼
X
d1þd2þþd4pmþ1¼r
ð−1ÞΛðp;−mÞqΞðp;−mÞ
×
ðq2; q2Þr
Q4pmþ1
i¼1
ðq2; q2Þdi
q
P
i;j CKðp;−mÞdidj;
ð8Þ
where the linear term Ξðp;−mÞ ≡P
i ξidi, phase factor
Λðp;−mÞ ≡P
i γidi.
The block structure of the matrix CKðp;−mÞ for some
examples lead to the following conjecture:
Conjecture. The generic structure of the quiver matrix
will take the form
CKðp;−mÞ ¼
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
@
F0
Fk
˜Fk
  
  
Fk
˜Fk
  
Fk
˜Fk
F⊤
k
U1
R1
˜R1
  
˜R1
R1
  
˜R1
R1
˜F⊤
k
R⊤
1
˜U1
T1
˜T1
...
...
  
T1
˜T1
F⊤
k
˜R⊤
1
T⊤
1
U2
˜R2
...
...
  
˜R2
R2
...
...
...
...
..
.
...
...
  
...
...
F⊤
k
R⊤
1
  
  
...
Ui
  
...
˜Ri
Ri
˜F⊤
k
˜R⊤
1
  
R⊤
i
  
˜Ui
  
Ti
˜Ti
...
...
...
...
..
.
...
...
..
.
...
...
F⊤
k
˜R⊤
1
T⊤
1
˜R⊤
2
  
..
.
..
.
  
Up
Rp
˜F⊤
k
R⊤
1
˜T⊤
1
R⊤
2
  
  
...
  
R⊤p
˜Up
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
A
;
ð9Þ
where X⊤stands for transposition of matrix X, the row
matrices
Fk ¼ ð−1; −1; … −1; −1Þ;
˜Fk ¼ ð0; 0; …0; 0Þ;
of size 1 × 2m and F0 ¼ 0. Let Xk denote the following set
of 2m × 2m matrices:
Xk ¼ fUk; ˜Uk; Rk; ˜Rk; Tk; ˜Tkg;
ð10Þ
where k ¼ 1; 2…p. All these matrices can be recursively
obtained using
Xk ¼ Xk−1 þ 2ðk −1ÞJ
∀k ≥2;
where J is a matrix of size 2m × 2m where all the elements
are one. So, knowing the set X1 is sufficient to determine
the full quiver matrix CKðp;−mÞ.
It appears that the set X1 for the simplest twist knot
Kðp ¼ 1; −m ¼ −1Þ ≡41 will suffice to obtain X1 for
double twist knots Kðp; −mÞ as Kðp; −mÞ ¼ Kðm; −pÞ
(K denotes mirror image of the knot K). However, our
matrix conjecture assumes p ≥m. Hence, our explicit
computations of set X1 for m ¼ 2, 3 is not derivable from
the CKðp;−1Þ.
In the following sections, we give some examples to
validate our proposition and conjecture. Specifically, we
work out the X1 set matrices for double twist knots
Kðm; −mÞ for m ¼ 1, 2, 3. This set is sufficient to obtain
the explicit quiver presentations for all the double twist
knots Kðp; −mÞ where m ¼ 1, 2, 3.
A. Knot-quiver correspondence for Kðp; −1Þ
Kðp; −1Þ are known in the literature as ‘twist knots’
which is the simplest class of double twist knots. In this
case, we fix the parameter m ¼ 1 and vary the other
parameter p. The simplest example, we consider p ¼ 1,
i.e., Kð1; −1Þ ¼ 41 knot. Using Eq. (8), we obtained the
quiver form of 41 as
Jrð41;qÞ¼
X
d1þþd5¼r
ð−1Þd3þd4q−2d2−2d1d2−2d2
2−d3þ2d2
5
×
ðq2;q2Þr
ðq2;q2Þd1ðq2;q2Þd2ðq2;q2Þd3ðq2;q2Þd4ðq2;q2Þd5
×q−2d1d3−4d2d3−d2
3þd4−2d2d4þd2
4þ2d5−2d2d5þ2d4d5:
Thus, the quiver matrix
C41 ¼
0
B
B
B
B
B
B
B
@
0
−1 −1
0
0
−1
−2 −2
−1 −1
−1
−2 −1
0
0
0
−1
0
1
1
0
−1
0
1
2
1
C
C
C
C
C
C
C
A
:
Similarly, we obtained other matrices for p ¼ 2, 3 i.e.,
C61 ¼
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
@
0
−1
−1
0
0
−1
−1
0
0
−1
−2
−2
−1
−1
−2
−2
−1
−1
−1
−2
−1
0
0
−1
−1
0
0
0
−1
0
1
1
0
0
1
1
0
−1
0
1
2
1
1
2
2
−1
−2
−1
0
1
0
0
1
1
−1
−2
−1
0
1
0
1
2
2
0
−1
0
1
2
1
2
3
3
0
−1
0
1
2
1
2
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
A
;
C81 ¼
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
@
0
−1
−1
0
0
−1
−1
0
0
−1
−1
0
0
−1
−2
−2
−1
−1
−2
−2
−1
−1
−2
−2
−1
−1
−1
−2
−1
0
0
−1
−1
0
0
−1
−1
0
0
0
−1
0
1
1
0
0
1
1
0
0
1
1
0
−1
0
1
2
1
1
2
2
1
1
2
2
−1
−2
−1
0
1
0
0
1
1
0
0
1
1
−1
−2
−1
0
1
0
1
2
2
1
1
2
2
0
−1
0
1
2
1
2
3
3
2
2
3
3
0
−1
0
1
2
1
2
3
4
3
3
4
4
−1
−2
−1
0
1
0
1
2
3
2
2
3
3
−1
−2
−1
0
1
0
1
2
3
2
3
4
4
0
−1
0
1
2
1
2
3
4
3
4
5
5
0
−1
0
1
2
1
2
3
4
3
4
5
6
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
A
:
These three examples confirm our conjecture for m ¼ 1.
For clarity, the explicit quiver matrix for any twist knot
Kðp; −1Þ is
CKðp;−1Þ ¼
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
@
F0
Fk
˜Fk
  
  
Fk
˜Fk
  
Fk
˜Fk
F⊤
k
U1
R1
˜R1
  
˜R1
R1
  
˜R1
R1
˜F⊤
k
R⊤
1
˜U1
T1
˜T1
...
...
  
T1
˜T1
F⊤
k
˜R⊤
1
T⊤
1
U2
˜R2
...
...
  
˜R2
R2
...
...
...
...
. .
.
...
...
  
...
...
F⊤
k
R⊤
1
  
  
...
Ui
  
...
˜Ri
Ri
˜F⊤
k
˜R⊤
1
  
R⊤
i
  
...
˜Ui
  
Ti
˜Ti
...
...
...
...
. .
.
...
...
..
.
...
...
F⊤
k
˜R⊤
1
T⊤
1
˜R⊤
2
  
...
...
  
Up
Rp
˜F⊤
k
R⊤
1
˜T⊤
1
R⊤
2
  
  
..
.
  
R⊤p
˜Up
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
A
;
ð11Þ
where the generators X1 ≡ðU1; ˜U1; R1; ˜R1; T1; ˜T1Þ are
as follows:
U1 ¼
 −2
−2
−2
−1

;
˜U1 ¼
 1
1
1
2

;
R1 ¼
 −1
−1
0
0

;
˜R1 ¼
 −2
−2
−1
−1

;
T1 ¼
 0
0
1
1

;
˜T1 ¼
 1
1
2
2

;
and Fk ¼ ð −1;
−1 Þ,
˜Fk ¼ ð 0;
0 Þ, and F0 ¼ ð0Þ.
Based on these calculations, we can infer the general
expressions for the linear term Ξðp; −1Þ and the phase
factor Λðp; −1Þ in proposition (11) for any given value
of p,
Ξðp;−1Þ ¼ 2pd4pþ1 þ
X
p
i¼1
ρ1ðiÞd4i−3 þ ρ2ðiÞd4i−2
þ ρ3ðiÞd4i−1 þ ρ4ðiÞd4i;
ð12Þ
where ρ1ðiÞ ¼ 2i −2, ρ2ðiÞ ¼ 2i −4, ρ3ðiÞ ¼ −3 þ 2i,
ρ4ðiÞ ¼ −1 þ 2i, and the phase factor is
Λðp;−1Þ ¼
X
2p
i¼1
d1
2ðð−1Þiþ1þ4iþ1Þ:
ð13Þ
These results agree with the quiver matrix of twist knots
obtained in Ref. [1].
B. Knot-quiver correspondence for Kðp; −2Þ
We have already worked out Kð2; −2Þ ≡83 knot in
Sec. II A. Further, we explicitly worked out colored Jones
for Kðp ¼ 3; −2Þ ≡103, and the quiver matrix elements
CKðp¼3;−2Þ are presented in the Appendix.
Our matrix form for p ¼ 3 is consistent with our
conjecture (9), and the basic set of matrices X1 are
U1 ¼
0
B
B
B
B
@
−2 −2 −3 −3
−2 −1 −2 −2
−3 −2 −4 −4
−3 −2 −4 −3
1
C
C
C
C
A
;
˜U1 ¼
0
B
B
B
B
@
−1 −1 0 0
−1
0
1 1
0
1
1 1
0
1
1 2
1
C
C
C
C
A
;
R1 ¼
0
B
B
B
B
@
−2 −2 −1 −1
−1 −1
0
0
−3 −3 −1 −1
−2 −2
0
0
1
C
C
C
C
A
;
˜R1 ¼
0
B
B
B
B
@
−2 −2 −3 −3
−1 −1 −2 −2
−2 −2 −4 −4
−1 −1 −3 −3
1
C
C
C
C
A
;
T1 ¼
0
B
B
B
B
@
−1 −1 −2 −2
0
0
−1 −1
0
0
0
0
1
1
1
1
1
C
C
C
C
A
;
˜T1 ¼
0
B
B
B
B
@
−1 −1 0 0
0
0
1 1
1
1
1 1
2
2
2 2
1
C
C
C
C
A
;
ð14Þ
Fk ¼ð−1; −1; −1 −1Þ, ˜Fk ¼ð0; 0; 0 0Þ, and F0 ¼ð0Þ.
We further worked out for p ¼ 4, 5 as well and verified
our conjecture (9) form obeyed. From these computations,
we can deduce the general form of the linear term Ξðp;−2Þ
and phase factor Λðp;−2Þ in the proposition (8) for arbitrary
p as
Ξðp;−2Þ ¼
X
2p
i
ðτ1ðiÞd4iþ1 þ τ2ðiÞd4i þ τ3ðiÞd4i−1
þ τ4ðiÞd4i−2Þ;
ð15Þ
where τ1ðiÞ ¼ −2 þ 2ð−1Þi þ i, τ2ðiÞ ¼ −3 þ 2ð−1Þi þ i,
τ3ðiÞ ¼ −2 þ i, τ4ðiÞ ¼ −3 þ i, and the phase factor is
Λðp;−2Þ ¼
X
4pþ1
i¼2
dð−3þ4i−ð−1Þðbi
2cÞ1
2Þ:
ð16Þ
Using the above data, we can write the colored Jones
polynomial for any Kðp; −2Þ in quiver presentation with
the quiver matrix consistent with the conjecture (9). So far,
we have obtained the set of matrices X1 for m ¼ 1, 2. With
the hope of deducing the pattern for the set X1 for any m,
we investigate double twist knots with m ¼ 3 in the
following section.
C. Knot-quiver correspondence for Kðp; −3Þ
Following reverse MMR, we could write the quiver
presentation for Kð3; −3Þ and obtain the quiver matrix
CKð3;−3Þ. The explicit matrix form is presented in the
Appendix. The generators (X1) of the quiver matrix can
be read off comparing with the conjectured form (9),
U1 ¼
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
@
−2
−2
−3
−3
−3
−3
−2
−1
−2
−2
−2
−2
−3
−2
−4
−4
−5
−5
−3
−2
−4
−3
−4
−4
−3
−2
−5
−4
−6
−6
−3
−2
−5
−4
−6
−5
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
A
;
˜U1 ¼
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
@
−3
−3
−2
−2
0
0
−3
−2
−1
−1
1
1
−2
−1
−1
−1
0
0
−2
−1
−1
0
1
1
0
1
0
1
1
1
0
1
0
1
1
2
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
A
;
R1 ¼
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
@
−2
−2
−2
−2
−1
−1
−1
−1
−1
−1
0
0
−4
−4
−3
−3
−1
−1
−3
−3
−2
−2
0
0
−5
−5
−3
−3
−1
−1
−4
−4
−2
−2
0
0
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
A
;
˜R1 ¼
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
@
−2
−2
−3
−3
−3
−3
−1
−1
−2
−2
−2
−2
−2
−2
−4
−4
−5
−5
−1
−1
−3
−3
−4
−4
−2
−2
−4
−4
−6
−6
−1
−1
−3
−3
−5
−5
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
A
;
T1 ¼
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
@
−1
−1
−3
−3
−4
−4
0
0
−2
−2
−3
−3
−1
−1
−2
−2
−2
−2
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
0
0
1
1
1
1
1
1
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
A
;
˜T1 ¼
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
@
−3
−3
−2
−2
0
0
−2
−2
−1
−1
1
1
−1
−1
−1
−1
0
0
0
0
0
0
1
1
1
1
1
1
1
1
2
2
2
2
2
2
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
A
;
Fk ¼ð−1; −1; −1 −1 −1 −1Þ, ˜Fk ¼ð0; 0; 0 0 0 0Þ,
and F0 ¼ ð0Þ. We have verified that our conjecture (9) is
true for p ¼ 4, 5. The linear term and phase factor in the
proposition (8) for p ¼ 3, 4 are as follows:
Ξð3;−3Þ ¼ −2d2 −d3 −4d4 −3d5 −6d6 −5d7 −3d8
−2d9 −d10 þ d12 þ 2d13 þ d15 −2d16
−d17 −4d18 −3d19 −d20 þ d22 þ 2d23
þ 3d24 þ 4d25 þ 2d26 þ 3d27 þ d29 −2d30
−d31 þ d32 þ 2d33 þ 3d34 þ 4d35
þ 5d36 þ 6d37;
Ξð4;−3Þ ¼ Ξð3;−3Þ þ 4d38 þ 5d39 þ 2d40 þ 3d41 þ d43
þ 3d44 þ 4d45 þ 5d46 þ 6d47 þ 7d48 þ 8d49;
Λð3;−3Þ ¼ d3 þ d5 þ d7 þ d8 þ d10 þ d12 þ d15
þ d17 þ d19 þ d20 þ d22 þ d24 þ d27
þ d29 þ d31 þ d32 þ d34 þ d36;
Λð4;−3Þ ¼ Λð3;−3Þ þ d39 þ d41 þ d43 þ d44 þ d46 þ d48:
Probably, there is a closed-form expression for Ξp;−3 and
Λp;−3 for any p. We are not able to infer the closed form
from the above data.
Ideally, it would be beneficial to find the set of matrices
X1 for any m as well as the closed form for Ξp;−m and Λp;−m.
The size of the quiver matrix ð4mp þ 1Þ × ð4mp þ 1Þ
makes the computations difficult.
