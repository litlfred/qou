---
doc_id: physrevd108106023
doc_title: "Knot-quiver correspondence for double twist knots"
section_id: sec-002-ii-double-twist-knots
section_title: "DOUBLE TWIST KNOTS"
section_number: II
pages: 2-3
source_pdf: PhysRevD.108.106023.pdf
source_sha256: 50c7980e88cd21a0
toc_source: inferred
---
by two variables, denoted as Kðp; −mÞ, illustrated in Fig. 1.
Note p; m ∈Zþ denote the number of full twists, and the
Alexander polynomial is ΔðXÞ ¼ 1 −pmX. Such a form
motivated us to attempt quiver representation for double
twist knots.
Even though the r-colored HOMFLY-PT for any double
twist knot in the cyclotomic form are known [14,15],
rewriting them in the form of motivic series is still a
challenging problem. We tried to determine the quiver
representation of PKðp;−mÞ
r
ðA ¼ qN; qÞ following the meth-
odology in Ref. [13]. However, we faced computational
difficulty in deducing the A dependence in the quiver
representation. Also, we know that the quiver matrix CðKÞ
does not depend on the variable A ¼ qN. As our aim is to
conjecture the quiver matrix form for the double twist knots
Kðp; −mÞ, we focus on rewriting the r-colored Jones
polynomial (A ¼ qN¼2),
JrðKðp; −mÞ; qÞ ≡PKðp;−mÞ
r
ðA ¼ q2; qÞ;
as a motivic series. Particularly, we obtain quiver matrix
CKðp;−mÞ
i;j
associated with the Kðp; −mÞ for m ≤3. We
conjecture that the quiver matrix CKðm;−mÞ
i;j
is sufficient to
recursively generate the quiver matrix for all the double
twist knots Kðp ≠m; −mÞ.
We follow the route of reverse engineering of MMR
expansion [13] to derive the motivic series form for
PKðp;−mÞ
r
ðA ¼ qN; qÞjN¼2. We now briefly review the
reverse engineering formalism, which sets the notation
and procedure we follow for Kðp; −mÞ in the next section.
A. Reverse engineering of Melvin-Morton-Rozansky
(MMR) expansion
Melvin-Morton-Rozansky (MMR) expansion states that
the symmetric r-colored HOMFLY-PT for knot K has the
following semiclassical expansion:
lim
ℏ→0;r→∞PKr ðA;q ¼ eℏÞ≃
1
ΔKðxÞN−1
þ
X
∞
k¼1
RK
k ðx;NÞ
ΔKðxÞ
Nþ2k−1
ℏk;
ð2Þ
with the leading term being the Alexander polynomial
ΔKðxÞ, and the variable x in terms of color r is
FIG. 1.
Double twist knots (m, p denote number of full twists).
VIVEK KUMAR SINGH et al.
PHYS. REV. D 108, 106023 (2023)
106023-2
x ¼ qr ¼ const. The symbol RK
k ðx; NÞ represents polyno-
mials in the variable x. The reverse approach is to obtain
PKr ðA; qÞ using the Alexander polynomial ΔKðxÞ [13]. This
approach also has obstacles to lift the ℏ→0 expansion to
q-dependent PKr ðA; qÞ but can be fixed for some situations
by comparing with the data of symmetric r-colored
HOMFLY-PT polynomials known for r ¼ 1, 2, 3. We
briefly highlight the steps involved in the reverse engineer-
ing formalism of MMR expansion [13]:
(i) We rewrite the Alexander polynomial in new var-
iable X ¼ ð1−xÞ2
x
. Thus, the Alexander polynomial
takes the following form:
ΔðxÞ ¼ 1 −
X
s
i¼1
ai
ð1 −xÞ2i
xi
≡1 −gðXÞ;
where the coefficients ai are integers, and s is a
positive integer.
(ii) Now, we use the following inverse binomial theo-
rem:
1
ð1 −uÞn ¼
X
∞
m¼0
 n þ m −1
m

um;
to write the first term of MMR expansion (2)
as follows:
1
ΔðxÞN−1 ¼
X
∞
m¼0
 N þ m −2
m

gðXÞm ¼
X
∞
k¼0
ckXk
¼
X
∞
k¼0
ðk!ckÞ Xk
k! :
ð3Þ
(iii) We make the following quantum deformation to get
the quantum-deformed polynomial:
Xk
k! ¼ ð1 −xÞ2k
k!xk
⇝
 r
k

q
q−rkð−Aqrt3; qÞk:
Here, the variable t is known as the refined param-
eter. In this article, we take t ¼ −1 to obtain
unrefined polynomial invariants for double twist
knots. The term within parentheses represents the
q-Pochhammer, while square brackets correspond to
the q-binomials, which are defined as
 r
k

q
¼
ðq;qÞr
ðq;qÞkðq;qÞr−k
;
ðx;qÞk ¼
Y
k−1
i¼0
ð1 −xqiÞ:
(iv) Further,
the
coefficient
k!ck⟶
q−deformation ˜cK
k
depends on the knot K and must be written in
terms of q-Pochhammers, q-binomials, and ðq; AÞ-
dependent powers so that
PKr ðA; qÞ ¼
X
r
k¼0
 r
k

q−rkðAqr; qÞk˜cK
k
can be transformed into the following form to
deduce the corresponding quiver QK:
PKr ðA; qÞ ¼
X
d
ð−1Þ
P
i γidi q
P
i;j CK
i;jdidjðq2; q2Þr
Qm
i¼1ðq2; q2Þdi
× q
P
αidiA
P
βidi:
ð4Þ
Here, CK
i;j is the quiver matrix, and the variables αi,
βi and γi are integer parameters. The set fdig ≡d
must obey r ¼ d1 þ d2… þ dn with di ≥0. Even
though such a transformation is motivated by
comparing Ooguri-Vafa partition function [16] with
the motivic generating series [17–19], it is still a
hard problem to obtain ˜cK
k for any knot.
Note that the quadratic power of q depends on CK
i;j, and it is
independent of A ¼ qN. Hence, we work with the colored
Jones polynomials JrðK; qÞ of a knot K to extract its quiver
matrix using the reverse engineering techniques of MMR
formalism replacing A →q2 in Eq. (4).2
The plan of the paper is as follows: In Sec. II A, we
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
the symmetric r-colored HOMFLY-PT polynomials can be
obtained for every r from Chern-Simons theory [20,21]. In
fact, colored HOMFLY-PT for arbitrary r in closed form is
given in Ref. [14]. Hence, our aim is not to reconstruct
r-colored HOMFLY-PT for double twist knots. We now
present the reverse engineering of MMR formalism (2) to
TABLE I.
Examples of double twist knots Kðp; −mÞ.
Kðp; −mÞ
Knots
Kðp; −1Þ
Twist knots
Kð2; −2Þ
83
Kð3; −2Þ
103
2Theorem 1.1, in Ref. [5] indicates the colored Jones
polynomials of rational links also admit generating functions
in quiver form.
