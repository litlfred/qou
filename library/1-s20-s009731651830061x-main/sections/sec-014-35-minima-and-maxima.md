---
doc_id: 1-s20-s009731651830061x-main
doc_title: "Constant term formulas for refined enumerations of Gog and Magog trapezoids"
section_id: sec-014-35-minima-and-maxima
section_title: "Minima and maxima"
section_number: 3.5
pages: 19-20
source_pdf: 1-s2.0-S009731651830061X-main.pdf
source_sha256: 8d591fe7f1673c52
toc_source: outline
doc_brief: "Fischer, Constant term formulas for refined enumerations of Gog and Magog trapezoids (JCTA 158, 2018, 560–604) — alternating sign matrices, plane partitions, constant-term methods."
---
A bottom-minimum is an entry in the leftmost SE-diagonal that is equal to the lower 
bound of its SE-diagonal, while a bottom-maximum is an entry in the rightmost NE-
diagonal that is equal to the upper bound of its NE-diagonal. A top-minimum is an entry 
equal to 1 and such entries can only be in the leftmost NE-diagonal. A top-maximum is 
an entry equal to m + n and such entries can only be in the rightmost SE-diagonal. Ob-
serve that minima (resp. maxima) as deﬁned for Gog trapezoids are top-minima (resp. 
bottom-maxima) as deﬁned for Gog pentagons.
Also in this case, it is not possible to include both, the inversions numbers, and the 
numbers of maxima and minima because for the numbers of minima and maxima we need 
to apply Corollary 6 in instances where b1, . . . , bn is not necessarily strictly increasing.
I. Fischer / Journal of Combinatorial Theory, Series A 158 (2018) 560–604
579
Corollary 6 implies in a similar way as for Gog trapezoids that the generating function 
of (m, n, kL, kR)-Gog pentagons with bottom row bn−kR+1, . . . , bkL w.r.t. the weight
Q#of bottom minima not including bn−kR+1
L
Q#of bottom maxima not including bkL
R
is the constant term of
(−1)
n−kR
2
 n−kR

i=1

1 −QL
xi
1 + xi

(1 + xi)i+1x1−kR−i
i
kL

i=n−kR+1
(1 + xi)bix−n+1
×
n

i=kL+1
(1 + QRxi)(1 + xi)m+kLx−n+i−kL
i

1≤i<j≤n
(xi −xj)(1 + xj + xixj)
w.r.t. x1, . . . , xn. Finally, the generating function of (m, n, kL, kR)-Gog pentagons with 
bottom row bn−kR+1, . . . , bkL that have at least one top-minimum and at least one top-
maximum w.r.t. the weight
P #of top minima
L
P #of top maxima
R
Q#of bottom minima not including bn−kR+1
L
Q#of bottom maxima not including bkL
R
is the constant term of the following expression in x1, . . . , xn.
(−1)
n−kR
2

+1PL(1 + PLx1)−1(1 + x1)2x−kR+1
1
PR(1 + xn −PRxn)−1x−kL+1
n
(1 + xn)kL+m
× QLQR
n−kR

i=2

1 −QL
xi
1 + xi

(1 + xi)i+1x1−kR−i
i
kL

i=n−kR
(1 + xi)bix−n+1
i
×
n−1

i=kL+1
(1 + QRxi)(1 + xi)m+kLx−n+i−kL
i

1≤i<j≤n
(xi −xj)(1 + xj + xixj).
In order to obtain the generating functions of Gog pentagons where the top row is ﬁxed, 
one has to proceed as in the previous subsection.
