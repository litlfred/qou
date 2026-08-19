---
doc_id: physrevd108106023
doc_title: "I. INTRODUCTION Knot-quiver correspondence (KQC) conjectured by Kucharski-Reineke-Stosic-Sulkowski [1] provides a new encoding of HOMFL Y -PT invariants of knots in terms of the re"
section_id: sec-001-ii-double-twist-knots
section_title: "DOUBLE TWIST KNOTS"
section_number: II
pages: 2-5
source_pdf: PhysRevD.108.106023.pdf
source_sha256: 50c7980e88cd21a0
doc_brief: "Knot-quiver correspondence for double twist knots Vivek Kumar Singh * — 9 sections: INTRODUCTION; DOUBLE TWIST KNOTS; Fk ˜Fk /C1/C1/C1 /C1/C1/C1 Fk ˜Fk"
---
by two variables, denoted as Kðp; −mÞ, illustrated in Fig. 1.
Note p; m ∈ Zþ denote the number of full twists, and the
Alexander polynomial is ΔðXÞ¼ 1 − pmX. Such a form
motivated us to attempt quiver representation for double
twist knots.
Even though the r-colored HOMFL Y -PT for any double
twist knot in the cyclotomic form are known [14,15],
rewriting them in the form of motivic series is still a
challenging problem. We tried to determine the quiver
representation of P
Kðp;−mÞ
r ðA ¼ qN ;q Þ following the meth-
odology in Ref. [13]. However, we faced computational
difficulty in deducing the A dependence in the quiver
representation. Also, we know that the quiver matrix CðKÞ
does not depend on the variable A ¼ qN . As our aim is to
conjecture the quiver matrix form for the double twist knots
Kðp; −mÞ, we focus on rewriting the r-colored Jones
polynomial ( A ¼ q
N¼2),
JrðKðp; −mÞ;q Þ ≡ PKðp;−mÞ
r ðA ¼ q2;q Þ;
as a motivic series. Particularly, we obtain quiver matrix
CKðp;−mÞ
i;j associated with the Kðp; −mÞ for m ≤ 3.W e
conjecture that the quiver matrix CKðm;−mÞ
i;j is sufficient to
recursively generate the quiver matrix for all the double
twist knots Kðp ≠ m; −mÞ.
We follow the route of reverse engineering of MMR
expansion [13] to derive the motivic series form for
PKðp;−mÞ
r ðA ¼ qN ;q ÞjN¼2. We now briefly review the
reverse engineering formalism, which sets the notation
and procedure we follow for Kðp; −mÞ in the next section.
A. Reverse engineering of Melvin-Morton-Rozansky
(MMR) expansion
Melvin-Morton-Rozansky (MMR) expansion states that
the symmetric r-colored HOMFL Y -PT for knotK has the
following semiclassical expansion:
lim
ℏ→0;r→∞
PKr ðA; q¼ eℏÞ ≃ 1
ΔKðxÞN−1
þ
X∞
k¼1
/C18RK
k ðx; NÞ
ΔKðxÞ
/C19Nþ2k−1
ℏk; ð2Þ
with the leading term being the Alexander polynomial
ΔKðxÞ, and the variable x in terms of color r is
FIG. 1. Double twist knots ( m, p denote number of full twists).
VIVEK KUMAR SINGH et al. PHYS. REV . D 108, 106023 (2023)
106023-2
x ¼ qr ¼ const. The symbol RK
k ðx; NÞ represents polyno-
mials in the variable x. The reverse approach is to obtain
PKr ðA; qÞ using the Alexander polynomial ΔKðxÞ [13]. This
approach also has obstacles to lift the ℏ → 0 expansion to
q-dependent PKr ðA; qÞ but can be fixed for some situations
by comparing with the data of symmetric r-colored
HOMFL Y -PT polynomials known for r ¼ 1,2 ,3 .W e
briefly highlight the steps involved in the reverse engineer-
ing formalism of MMR expansion [13]:
(i) We rewrite the Alexander polynomial in new var-
iable X ¼
ð1−xÞ2
x . Thus, the Alexander polynomial
takes the following form:
ΔðxÞ¼ 1 −
Xs
i¼1
ai
ð1 − xÞ2i
xi ≡ 1 − gðXÞ;
where the coefficients ai are integers, and s is a
positive integer.
(ii) Now, we use the following inverse binomial theo-
rem:
1
ð1 − uÞn ¼
X∞
m¼0
/C18n þ m − 1
m
/C19
um;
to write the first term of MMR expansion (2)
as follows:
1
ΔðxÞN−1 ¼
X∞
m¼0
/C18N þ m − 2
m
/C19
gðXÞm ¼
X∞
k¼0
ckXk
¼
X∞
k¼0
ðk!ckÞ Xk
k! : ð3Þ
(iii) We make the following quantum deformation to get
the quantum-deformed polynomial:
Xk
k! ¼ ð1 − xÞ2k
k!xk ⇝
/C20r
k
/C21
q
q−rkð−Aqrt3; qÞk:
Here, the variable t is known as the refined param-
eter. In this article, we take t ¼ −1 to obtain
unrefined polynomial invariants for double twist
knots. The term within parentheses represents the
q-Pochhammer, while square brackets correspond to
the q-binomials, which are defined as
/C20r
k
/C21
q
¼ ðq; qÞr
ðq; qÞkðq; qÞr−k
; ðx; qÞk ¼
Yk−1
i¼0
ð1 − xqiÞ:
(iv) Further, the coefficient k!ck⟶
q−deformation
˜cK
k
depends on the knot K and must be written in
terms of q-Pochhammers, q-binomials, and ðq; AÞ-
dependent powers so that
PKr ðA; qÞ¼
Xr
k¼0
/C20r
k
/C21
q−rkðAqr; qÞk ˜cK
k
can be transformed into the following form to
deduce the corresponding quiver QK:
PKr ðA; qÞ¼
X
d
ð−1Þ
P
i γidi q
P
i;j CK
i;jdidj ðq2; q2ÞrQm
i¼1ðq2; q2Þdi
× q
P
αidi A
P
βidi : ð4Þ
Here, CK
i;j is the quiver matrix, and the variables αi,
βi and γi are integer parameters. The set fdig ≡ d
must obey r ¼ d1 þ d2… þ dn with di ≥ 0. Even
though such a transformation is motivated by
comparing Ooguri-V afa partition function [16] with
the motivic generating series [17–19],i ti ss t i l la
hard problem to obtain ˜cK
k for any knot.
Note that the quadratic power of q depends on CK
i;j, and it is
independent of A ¼ qN . Hence, we work with the colored
Jones polynomials JrðK;q Þ of a knot K to extract its quiver
matrix using the reverse engineering techniques of MMR
formalism replacing A → q2 in Eq. (4).2
The plan of the paper is as follows: In Sec. II A,w e
briefly discuss the colored Jones polynomials of double
twist knot Kðp; −mÞ obtained from the reverse engineering
techniques of MMR expansion. In Sec. III, we conjecture
CK
i;j for K ¼ Kðp; −mÞ and validate it for some double twist
knots. We conclude in Sec. IV summarizing our results,
enumerating some open questions and future directions.
II. DOUBLE TWIST KNOTS
We have listed some of the double twist knots Kðp; −mÞ
in Table I.
As these double twist knots belong to arborescent family,
the symmetric r-colored HOMFL Y -PT polynomials can be
obtained for every r from Chern-Simons theory [20,21].I n
fact, colored HOMFL Y -PT for arbitraryr in closed form is
given in Ref. [14]. Hence, our aim is not to reconstruct
r-colored HOMFL Y -PT for double twist knots. We now
present the reverse engineering of MMR formalism (2) to
TABLE I. Examples of double twist knots Kðp; −mÞ.
Kðp; −mÞ Knots
Kðp; −1Þ Twist knots
Kð2; −2Þ 83
Kð3; −2Þ 103
2Theorem 1.1, in Ref. [5] indicates the colored Jones
polynomials of rational links also admit generating functions
in quiver form.
KNOT-QUIVER CORRESPONDENCE FOR DOUBLE TWIST KNOTS PHYS. REV . D 108, 106023 (2023)
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
