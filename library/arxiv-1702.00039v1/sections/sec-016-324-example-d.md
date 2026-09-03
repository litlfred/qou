---
doc_id: arxiv-1702.00039v1
doc_title: "Gentle introduction to Soergel bimodules I: The basics NICOLAS LIBEDINSKY"
section_id: sec-016-324-example-d
section_title: "Example D"
section_number: 3.2.4
pages: 17-18
source_pdf: 1702.00039v1.pdf
source_sha256: b47ca7d1cf7b44be
doc_brief: "Gentle introduction to Soergel bimodules I: The basics NICOLAS LIBEDINSKY — This paper is the ﬁrst of a series of introductory papers on the fascinating world of Soergel bimodules."
---
Kazhdan-Lusztig polynomials were discovered (or invented) in 1979, but it
was only in 1990 that Matthew Dyer gave a formula [Dy] to calculate induc-
tively the Kazhdan-Lusztig basis for a Universal Coxeter system (we will not
reproduce here the proof, although it is not a difﬁcult one). In this case, every
element has only one expression as a product of elements ofS .
Theorem 3.4 (Dyer’s Formula) Let x∈Un and x =rs··· with r,s,... ∈S.
Then we have the following recursive formula
brbx = ( v +v−1)bx
btbx = btx if t⁄=r,s
bsbx = bsx +brx if s⁄=r (12)
Our baby examples A and B are particular cases of example C (the case of
dihedral groups). We just saw in equation (11) that Dyer’s Formula is also
true for Dihedral groups (the ﬁrst case of the formula comes from the fact
bsbs = (v +v−1)bs and the second case never appears in Dihedral groups). In
fact the same proof works for the inﬁnite Dihedral group as we said in Remark
2. So the whole point of this theorem is that the calculation of the Kazhdan
Lusztig basis in this case is local in nature, i.e. different strings of alternating
simple reﬂections “don’t intersect each other” in the following sense.
Let x =··· psps be an alternating sequence of simple reﬂections ending by s,
and y = srsrs··· an alternating sequence of simple reﬂections starting by s.
Then we use the following notation
bx∗by := bxby
(v +v−1)
It is an exercice to prove thatbx∗by∈H (hint: bx is divisible on the right and
by is divisible on the left bybs). Consider the element
x :=srsrsrprpruqtqrqrqrq.
As we said, the calculation is local, we have
bx =bsrsrsr∗brprpr∗bru∗buq∗bqtq∗bqrqrqrq.
With Dyer’s Formula in hand we could have done all the calculations we did
in the other examples with no effort. We apply it three times and we obtain
• bsr =bsbr
17
• bsrbs =bsrs +bs−→bsrs =bsbrbs−bs
• bsrsbr =bsrsr +bsr−→bsrsr =bsbrbsbr− 2bsbr
Aha!
3.3 Proof of Theorem 3.2
Proof We reproduce the beautiful (and simple) proof of Soergel [So3, Theo-
rem 2.1] of the stronger version explained in Remark 1.
