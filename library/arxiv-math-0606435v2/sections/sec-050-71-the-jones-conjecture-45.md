---
doc_id: arxiv-math-0606435v2
doc_title: "PROPERTIES OF CLOSED 3-BRAIDS"
section_id: sec-050-71-the-jones-conjecture-45
section_title: "The Jones conjecture 45"
section_number: 7.1
pages: 45-46
source_pdf: 0606435v2 (1).pdf
source_sha256: 6dddaf838a19f0f5
doc_brief: "PROPERTIES OF CLOSED 3-BRAIDS — We show that 3-braid links with given (non-zero) Alexander o r Jones polynomial are ﬁnitely many, and can be effectively determined."
---
Table 1:This table displays the Young tableauxYof 6 boxes, the decomposition into
πY′for 4-box Young tableauxY′of the sub-representation ofB4inπY(writingY′forπY′),
the multiplicitiesM(i,Y)of the 7 possible eigenvaluesδiofπY(α), and the quantitiesd
(=dimπY) andr(rank of the idempotentei) occurring in Jones’s lemma 9.3.
Y
Y′A2A+BA+2B+CB+CA+2B+D2B+2C+2DC+DB+2D+EC+2D+ED+2EE
11211
q41121
q13224111
−q121221
−q2121341321
q311142231
−q3121221
d15951016510951
r01324836641
30r/d06101212151818202430
46 7 Applications of the representation theory
In case Y is one of the one-hook diagrams like , then πY is by p. 354 bottom (a tensor product of a parity, which
disappears at even exponent sum, with) an exterior power of ψ 5. Thus, as in §7 (of Jones’s paper), one can evaluate
tr πY (βk) from the characteristic polynomial of the Burau matrix ψ 5(βk). We determined this way the corresponding
c(i,Y ), and veriﬁed them with a few extra values of k in (50). While it is clear that all c(i,Y ) should be rational
expressions in q, we expected them to be in fact Laurent polynomials. So we wer e a bit startled by the denominators
1 + q2. However, according to p. 343 top, the Hecke algebra may degenerate at roots of unityq, which justiﬁes at least
cyclotomic polynomials as denominators.
For Y = , πY was written down directly on p. 362, and for its transposed (dual) Young diagram , one uses Note
4.6.
There remain 3 representations, for Y = , , and its dual , with a total of 15 unknown c(i,Y ). These were
more complicated to ﬁnd, since we knew of no way to evaluate tr πY directly. To help ourselves, ﬁrst observe that we
have, for ﬁxed Y, the trace identities
7
∑
i=1
c(i,Y ) = tr πY ([4354]) = tr πY ([2132]) =
7
∑
i=1
M(i,Y )δi ,(51)
which again give a linear condition on the c(i,Y ). To ﬁnd further identities, we used (48) in a “backward” mann er.
We calculated for small1 k,l (k odd, |k| ≤ 5, |l| ≤ 1) the polynomial on the left using Morton-Short’s program [MS2].
We substituted the known c(i,Y ) on the right of (48), obtaining thus linear conditions for the yet unknown c(i,Y ). To
determine the coefﬁcients, it remains to understand the effect on tr πY of multiplying with the full twist ∆2
