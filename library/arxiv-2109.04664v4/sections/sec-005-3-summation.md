---
doc_id: arxiv-2109.04664v4
doc_title: "ON THE ASYMPTOTIC BEHA VIOR OF THE COLORED JONES POL YNOMIAL OF THE FIGURE-EIGHT KNOT ASSOCIA TED WITH A REAL NUMBER"
section_id: sec-005-3-summation
section_title: "Summation"
section_number: 3
pages: 7-8
source_pdf: 2109.04664v4.pdf
source_sha256: 639cd40a29752e3f
doc_brief: "ON THE ASYMPTOTIC BEHAVIOR OF THE COLORED JONES POLYNOMIAL OF THE FIGURE-EIGHT KNOT ASSOCIATED WITH A REAL NUMBER — W e study the asymptotic behavior of the N -dimensional colored Jones polynomial"
---
In this section, we use the quantum dilogarithm TN (z) to express JN (E;eξ/N )
without the product of a sequence.
Since the ﬁgure-eight knot E is amphicheiral, its colored Jones polynomial is sym-
metric, that is, JN (E;q) = JN (E;q−1). So we have JN (E;eξ/N ) = JN (E;e−ξ/N )
and we do not need to consider the case where ξ <0.
Recall that we choose a positive real number θ so that tan θ <π
ξ and that we
put γ := ξ
2Nπ √−1 . Putting z := ξ
2π √−1 (1 −l/N ) (0 <l<N ) in (2.5), we have
exp
(
TN
(
ξ
2π √−1 (1 −l/N ) − ξ
4Nπ √−1
))
exp
(
TN
(
ξ
2π √−1 (1 −l/N ) + ξ
4Nπ √−1
)) = 1 −eξ(1−l/N )
since
Re
( ξ
2π √−1
(
1 − l
N
)
eθ√−1
)
= ξ
2π
(
1 − l
N
)
sinθ< 1
2
(
1 − l
N
)
cosθ,
which is between 0 and cos θ. Therefore we have
k∏
l=1
(
1 −e(N −l)ξ/N )
=
k∏
l=1
exp
(
TN
(
ξ
2π √−1
(
1 − 2l+1
2N
) ))
exp
(
TN
(
ξ
2π √−1
(
1 − 2l−1
2N
) ))
=
exp
(
TN
(
ξ
2π √−1 (1 − 2k+1
2N )
))
exp
(
TN
(
ξ
2π √−1 (1 − 1
2N )
)) .
Similarly, putting z := ξ
2π √−1 (1 +l/N ) (0 <l<N ) in (2.5), we have
exp
(
TN
(
ξ
2π √−1 (1 +l/N ) − ξ
4Nπ √−1
))
exp
(
TN
(
ξ
2π √−1 (1 +l/N ) + ξ
4Nπ √−1
)) = 1 −eξ(1+l/N )
since
Re
( ξ
2π √−1
(
1 + l
N
)
eθ√−1
)
= ξ
2π
(
1 + l
N
)
sinθ< 1
2
(
1 + l
N
)
cosθ,
which is between 0 and cos θ. So we have
k∏
l=1
(
1 −e(N +l)ξ/N )
=
k∏
l=1
exp
(
TN
(
ξ
2π √−1
(
1 + 2l−1
2N
) ))
exp
(
TN
(
ξ
2π √−1
(
1 + 2l+1
2N
) ))
=
exp
(
TN
(
ξ
2π √−1 (1 + 1
2N )
))
exp
(
TN
(
ξ
2π √−1 (1 + 2k+1
2N )
)) .
