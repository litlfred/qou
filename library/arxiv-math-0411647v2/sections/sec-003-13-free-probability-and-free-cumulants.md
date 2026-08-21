---
doc_id: arxiv-math-0411647v2
doc_title: "Asymptotics of characters of symmetric groups, genus expansion and free probability"
section_id: sec-003-13-free-probability-and-free-cumulants
section_title: "Free probability and free cumulants"
section_number: 1.3
pages: 4-6
source_pdf: 0411647v2.pdf
source_sha256: d79f96b416cb28da
doc_brief: "Asymptotics of characters of symmetric groups, genus expansion and free probability — The convolution of indicators of two conjugacy classes on the symmetric group Sq is usually a complicated linear"
---
cumulants of the transition measure of a given Young diagram . The
notion of free cumulants plays a fundamental role in the free proba-
bility, a theory which was initiated by V oiculescu in order t o answer
some old questions in the theory of operator algebras but it s oon evolved
into an exciting self–standing theory with many links to oth er ﬁelds, see
[HP00, VDN92, V oi95, V oi00]. This theory can be viewed as a hi ghly
non–commutative probability theory in which the notion of i ndependence
of random variables was replaced by a non–commutative notio n of free-
ness. For the purpose of this article we shall concentrate on the combina-
torial aspect of this theory connected with non–crossing pa rtitions [Kre72]
and mentioned above free cumulants, which were introduced b y Speicher
[Spe94, Spe97, Spe98].
1.3.1. Free convolution and free cumulants. For probability measures µ,
ν on the real line one can deﬁne their free convolution µ ⊞ ν which is
also a probability measure on the real line. One of the ﬁrst pr oblems of
free probability was to study this convolution. The simples t approach is to
consider the sequence of moments
(1.1) Mi(µ ) =
∫
R
xi dµ (x)
of a given measure µ and ask what is the relation between the moments
of µ ⊞ ν and the moments of µ and ν. Unfortunately, in turns out that
the answer is given by a sequence of quite complicated polyno mials. The
solution to the above problem of ﬁnding a nice description of the free con-
volution is given by free cumulants. To the measureµ we assign a sequence
of its free cumulants R1(µ ), R 2(µ ), . . . ; every free cumulant Ri(µ ) is a cer-
tain polynomial in the moments of µ, and conversely, every moment of µ
can be expressed as a certain polynomial in free cumulants; t herefore the
sequence of moments and the sequence of free cumulants carry the same
ASYMPTOTICS OF CHARACTERS AND GENUS EXPANSION 5
information. The advantage of the notion of free cumulants o ver the no-
tion of moments is the simplicity of the relation between fre e cumulants:
Rn(µ ⊞ ν ) = Rn(µ ) + Rn(ν ). In this article we are not interested in the
study of free convolution; our point is that free cumulants have a miraculous
property of simplifying certain complicated non–commutative relations.
1.3.2. Free cumulants of the transition measure.In this article we study the
relation between the transition measure µ λ of a Young diagram λ and the
characters of the corresponding irreducible representati on. The simplest
idea would be to describe the transition measure in terms of i ts moments
Mi(µ λ), however—as we already mentioned—the relation between the se
moments and characters turns out to be quite complicated. Si milarly as
in the example from the above Section 1.3.1, free cumulants c an simplify
dramatically the complexity of the formulas: it was shown byBiane [Bia98]
that for each n the value Σ n of the normalized character on the n–cycle can
be expressed as a certain polynomial in free cumulants R2, R 3, . . . of the
transition measure of the corresponding Young diagram. Fur thermore, the
leading term is particularly simple, namely
(1.2) Σ n = Rn+1 + lower degree terms.
The fundamental property of this polynomial, called Kerov p olynomial, is
that it is universal for all Young diagrams.
Kerov polynomials seem to have very interesting combinator ial proper-
ties but not too much about them is known [Bia03, Sta02a, Sta02b]. Kerov
conjectured that all coefﬁcients of Kerov polynomials are non–negative in-
tegers; this conjecture seems to be quite difﬁcult. Unfortu nately, Kerov’s
conjecture does not seem to have interesting applications, but on the other
hand its proof might be much more interesting than the conjec ture itself:
Biane [Bia03] suggested that the coefﬁcients of Kerov polyn omials might
be interpreted as the number of certain intervals in the decomposition of the
Cayley graph of the symmetric group and it would be very inter esting to
state Biane’s conjecture in a more concrete form.
1.3.3. The second main result: second-order expansion for Kerov po lyno-
mials. One of the main results of this paper is a more precise asympto tic
expansion of characters
(1.3) Σ n = Rn+1+
∑
m 2,m 3, ···≥0
2m 2 +3m 3+4m 4+···=n− 1
1
4
( n + 1
3
)( m2 + m3 + · · ·
m2, m 3, . . .
) ∏
s≥2
(
(s − 1)Rs
) m s
+
lower degree terms,
6 PIOTR ´SNIADY
which was conjectured by Biane [Bia03]. In other words: we ca lculate
explicitly the coefﬁcients of Kerov polynomials correspon ding to the two
highest–degree terms. We also outline an algorithm which can provide such
an expansion of any order.
After the ﬁrst version of this article was made public [ ´Sni03a, ´Sni03b]
Goulden and Rattan [GR05] using different methods found an e xplicit for-
mula for all coefﬁcients of Kerov polynomials. The Kerov’s positivity con-
jecture remains open until now.
