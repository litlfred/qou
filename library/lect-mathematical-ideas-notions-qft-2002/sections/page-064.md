---
doc_id: lect-mathematical-ideas-notions-qft-2002
doc_title: "Mathematical ideas and notions of quantum field theory"
section_id: page-064
section_title: "Page 64"
pages: 64-64
pdf_page: 64
source_pdf: lect-mathematical-ideas-notions-qft-2002.pdf
source_sha256: 95cac1ccd6c80226
text_source: ocr
granularity: page
doc_brief: "Mathematical ideas and notions of quantum field theory — 78 sections: Page 1; Page 2; Page 3"
---
64 MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY

It is clear that this quantity depends only on dv and not on dup and dv; sepa-
rately.

Thus, f f(v)dv is defined as the integral of the suitably normalized top coefficient
of f (expanded with respect to some homogeneous basis of AV,"). To write it in
coordinates, let £1,...,€m be a linear system of coordinates on V such that dv =
Spite (such coordinate systems will be called unimodular with respect to dv).
Then f f(v)dv equals f ftop(1,-.-5%n)dx1..den, where ftop is the coefficient of
1...) in the expansion of f.

9.6. The Berezinian of a matrix. Now we generalize to the supercase the defini-
tion of determinant (since we need to generalize Jacobian, which is a determinant).

Let R be a supercommutative ring. Fixt two nonnegative integers m,n. Let A
bean+m by n+m matrix over R. Split A in the blocks A,,, A12, A21, A22 so that
Aj, isn by n, and Ago is m by m. Assume that the matrices A,;,A92 have even
elements, while 42; and A; have odd elements. Assume also that Ago is invertible.

Definition 9.4. The Berezinian of A is the element
det( Ai; — Ai2 A535 Aa1)
det(A22)

(where the determinant of the empty matrix is agreed to be 1; so for m = 0 one
has BerA = det A, and for n = 0 one has BerA = (det .A)~').

Ber(A) := ER

Remark. Recall for comparison that if A is purely even then
det (A) := det(Ai1 — A12A551 Aor) det (Ave).
The Berezinian has the following simpler description. Any matrix A as above
admits a unique factorization A = A,ApA_, where A;, Ao, A~ are as above, and

in addition A, A_ are block upper (respectively, lower) triangular with 1 on the
diagonal, while Ao is block diagonal. Then Ber(A) = det ((Ao)11)/ det((Ao)22).

Proposition 9.5. If A,B be matrices as above, then Ber(AB) = Ber(A)Ber(B).

Proof. From the definition using triangular factorization, it is clear that it suffices
to consider the case A = A_, B = B,. Let X = (A_)o1, Y = (By)12 (matrices
with odd elements). Then the required identity is

det(1—Y(1+ XY)7!X) = det(1 + XY).
To prove this relation, let us take the logarithm of both sides and expand using
Taylor’s formula. Then the left hand side gives
— So mV (+ XY)*(XY)F 1X) /k
k>1

Using the cyclic property of the trace, we transform this to

So Tr((1+ XY)K(XY)') /&

k>1

(the minus disappears since X, Y have odd elements). Summing the series, we find
that the last expression equals

—TrIn(1 — (1+ XY)"!XY) =Trin(1 + XY),

as desired. Oo
