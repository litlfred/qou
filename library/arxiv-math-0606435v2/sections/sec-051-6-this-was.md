---
doc_id: arxiv-math-0606435v2
doc_title: "PROPERTIES OF CLOSED 3-BRAIDS"
section_id: sec-051-6-this-was
section_title: "This was,"
section_number: 6
pages: 46-47
source_pdf: 0606435v2 (1).pdf
source_sha256: 6dddaf838a19f0f5
doc_brief: "PROPERTIES OF CLOSED 3-BRAIDS — We show that 3-braid links with given (non-zero) Alexander o r Jones polynomial are ﬁnitely many, and can be effectively determined."
---
however, done also by Jones in §9, lemma 9.3:
πY (∆2
n) = qrn(n−1)/ d IdπY .(52)
For givenY , the number r = rY is calculated as in lemma 9.1 from ﬁgure 3.3, and d = dY = dim πY more easily by the
hook length formula on p. 341. Call eY = n(n − 1)r/ d (with n = 6) the exponent2 of q on the right hand-side of (52).
These values are given in table 1. Two simple checks are ∑
Y ⊢n
d2
Y = n! (because the multiplicity of each irrep in the
Hecke algebra equals its dimension), and thateY are integers (Remark on p. 358 bottom) and satisfyeY +eY = n(n −1)
for all Y (because of Note 4.6). So (48) gets
−(1 − q) · . . .· (1 − q6)X(ˆβk,l)(q,λ) =
√
λ
e−5
∑
Y ⊢6
ˆWY (q,λ)ql·eY
7
∑
i=1
c(i,Y ) δk
i ,(53)
with e = [βk,l] = 4 + 4k + 30l.
Actually, each polynomial X(ˆβk,l) gives 6 equations for c(i,Y ), because there are 6 relevant λ-coefﬁcients on both
hand-sides of (48) (in degrees e − 5
2 , e − 3
2 , . . . , e + 5
2 ; it is helpful to multiply again by (1 + q2) to get disposed of
the denominators of the known c(i,Y )). We have with 18 polynomials 111 equations (6 equations per polynomial
plus the three relevant trace equations (51)). Still the res ulting system was too hard to solve by computer, using
MATHEMATICA
TM
[Wo], since its coefﬁcients are (Laurent) polynomials in q, with dozens of terms each.
However, substituting some (rational) values of q, the system can be solved immediately. We used this to check ﬁ rst
the rank of the matrix (i.e. which equations are linearly red undant). Again we were surprised that for 15 variables
c(i,Y ) the rank was only 14. This, however, can be explained from our restraint to odd k (which we chose for
some, purely technical, component number concerns in the calculation with Morton-Short’s program). Whenever two
opposite eigenvalues δi and δi′ = −δi occur in πY (α), the equations (48) for odd k can detect only c(i,Y ) − c(i′,Y ).
The trace equations (51), which involve c(i,Y ) and c(i′,Y ) with the same sign, remedy the shortcoming for and
its transposed diagram, but for we have two pairs (i,i′) of opposite eigenvalues, so we still lose one dimension.
1In the parametrization P(v,z), used by Morton-Short, unlike for X, the coefﬁcients of P(ˆβk,l ) become quickly large and produce machine size
integer overﬂows. In particular, we could not calculate correctly polynomials for |l| > 2.
2This is not to be confused with the variable e, which we use for exponent sum of a braid, or with the idempotent ei from Jones’s lemma 9.1.
