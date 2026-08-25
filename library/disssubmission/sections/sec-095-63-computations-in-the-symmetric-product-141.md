---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-095-63-computations-in-the-symmetric-product-141
section_title: "Computations in the symmetric product 141"
section_number: 6.3
pages: 149-150
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 121 sections: Acknowledgements; Introduction; Introduction"
---
in H2c(X). Then θb· η = h∗
d([Θ]b· µ), so from the projection formula we
obtain the degree
degCd(xa· θb· η) = degX(hd!(xa)· [Θ]b· µ)
wherehd! : H2a(Cd)−→H2(a+g−d)(X) denotes the Gysin morphism. We
can assume without loss of generality thatb +c≤ g. For the fundamental
classxa = [Cb+c] then
hd!(xa)· [Θ]b = [Wb+c]· [Θ]b = 1
(g−b−c)! [Θ]g−c
by the Poincar´e formula. This easily implies the claim of the lemma if one
uses that[Θ]g−c = (g−c)!∑|J|=g−c ηJ. □
COROLLARY 6.5. Let η∈ H2c(Cd) be a monomial inλ1, . . . ,λ2g for
some c∈ N0. Then
degCd
(cd−c(Cd)· η) =
{
(−1)d−c·(2(g−1−c)
d−c
) if η = ηI for some I,
0 otherwise.
Proof. By [6, sect. VII.5] the Chern polynomial ofCd can be written
as the power seriesct(Cd) = (1 +tx)d−g+1· e−tθ/(1+tx). Writing out the
exponential series and then expanding the occuring powers of 1+tx via the
binomial series, we obtain
ct(Cd) = ∑
b≥0
(−1)b
b! (tθ)b (1+tx)d−g+1−b
= ∑
b≥0
∑
a≥0
(−1)b
b!
(d−g+1−b
a
)·xa· θb·ta+b .
In particular, looking at the coefﬁcient oftd−c in the above series and using
lemma 6.4 we obtain thatcd−c(Cd)· η = 0 unless η = ηI for some I, in
which case
degCd
(cd−c(Cd)· η) = ∑
a+b=d−c
(−1)b
b!
(d−g+1−b
a
)·xa· θb· η
= ∑
a+b=d−c
(−1)b(d−g+1−b
a
)(g−c
b
)
= (−1)d−c ∑
a+b=d−c
(g−2−c
a
)(g−c
b
).
Up to the sign this last expression coincides with the coefﬁcient oftd−c in
the power series
∑
a≥0
(g−2−c
a
)ta· ∑
b≥0
(g−c
b
)tb = (1+t)g−2−c(1+t)g−c = (1+t)2(g−1−c)
so we are done by binomial expansion of the right hand side. □
142 Chapter 6 – The generic rank of Brill-Noether sheaves
