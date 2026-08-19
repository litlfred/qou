---
doc_id: arxiv-2302.05903v2
doc_title: "On combinatorial generalization(s) of Borel transform: Averaging method in combinatorics of symmetric polynomials"
section_id: sec-005-a-collection-of-sum-formulas
section_title: "A collection of sum formulas"
section_number: null
pages: 6-7
source_pdf: 2302.05903v2.pdf
source_sha256: 9a17abd36cc8a317
doc_brief: "On combinatorial generalization(s) of Borel transform: Averaging method in combinatorics of symmetric polynomials — We elaborate on the recent suggestion to consider averaging of Cauchy identities"
---
To summarize, we can reproduce the whole collection of the single-Schur sums from [7, secs.1.5,3.4,3.5].
They are naturally divided in three blocks, and the formulas are given also in terms of symmetric variables
xi such that pk =P
ixk
i .
1. The first one is already familiar
X
R
SR =
Y
i
1
1−xi
Y
i<j
1
1−xixj
= exp
(∞X
k=1
p2
k
2k + p2k−1
2k− 1
)
(34)
X
R even
SR =
Y
i
1
1−x2
i
Y
i<j
1
1−xixj
= exp
(∞X
k=1
p2
k
2k + p2k
2k
)
(35)
X
R∨ even
SR =
Y
i<j
1
1−xixj
= exp
(∞X
k=1
p2
k
2k− p2k
2k
)
(36)
X
R
(−1)νRSR =
Y
i
1
1−xi
Y
i<j
1
1 +xixj
= exp
(∞X
k=1

(−1)kp2
k
2k + p2k−1
2k− 1 + p4k−2
2k− 1
)
(37)
X
R
tcRSR =
Y
i
1
1−txi
Y
i<j
1
1−xixj
= exp
(∞X
k=1
p2
k
2k +t2k−1 p2k−1
2k− 1 + (t2k− 1)p2k
2k
)
(38)
X
R
trRSR =
Y
i
1 +txi
1−x2
i
Y
i<j
1
1−xixj
= exp
(∞X
k=1
p2
k
2k +t2k−1 p2k−1
2k− 1 + (1−t2k)p2k
2k
)
(39)
where cR (rR) is the number of rows (lines) of odd length, and νR =P
i(i− 1)Ri. The first three lines follow
from the last two lines upon putting t = 0, 1.
6
2. The second block involves the skew Schur functions:
X
R
SR/Q =
Y
i
1
1−xi
Y
i<j
1
1−xixj
X
P
SQ/P = exp
(∞X
k=1
p2
k
2k + p2k−1
2k− 1
)X
P
SQ/P (40)
X
R even
SR/Q =
Y
i
1
1−x2
i
Y
i<j
1
1−xixj
X
P even
SQ/P = exp
(∞X
k=1
p2
k
2k + p2k
2k
) X
P even
SQ/P (41)
X
R∨ even
SR/Q =
Y
i<j
1
1−xixj
X
P∨ even
SQ/P = exp
(∞X
k=1
p2
k
2k− p2k
2k
) X
P∨ even
SQ/P (42)
for arbitrary Q.
3. The third direction is generalizations of these formulas to the Macdonald polynomials. We do not provide
relevant averages for this case in order to avoid overloading the text with unnecessary complicated formulas.
Still, we list the results. Denote
Hel
R :=
Y
(i,j)∈R
R∨
j−i even
1−qRi−jtR∨
j−i+1
1−qRi−j+1tR∨
j−i, H oa
R :=
Y
(i,j)∈R
Ri−j odd
1−qRi−jtR∨
j−i+1
1−qRi−j+1tR∨
j−i (43)
The full product HR is just the coefficient that stands in the sum of the Cauchy identity:
X
R
HRMR{pk}MR{¯pk} =
Y
i,j
(txi¯xj;q)∞
(xi¯xj;q)∞
= exp
(∞X
k=1
 1−tk
1−qk
pk ¯pk
k
)
(44)
with pk =P
ixk
i , ¯pk =P
i ¯xk
i . Then,
X
R
Hel
RMR =
Y
i
(txi;q)∞
(xi;q)∞
Y
i<j
(txixj;q)∞
(xixj;q)∞
= exp
(∞X
k=1
1−tk
1−qk
p2
k
2k + p2k−1
2k− 1
)
(45)
X
R
Hoa
R MR =
Y
i
(qtx2
i ;q2)∞
(1−xi)(q2x2
i ;q2)∞
Y
i<j
(txixj;q)∞
(xixj;q)∞
= exp
(∞X
k=1
 1−tk
1−qk
p2
k
2k + tk−qk
1 +qk
p2k
2k + p2k−1
2k− 1
)
(46)
X
R∨ even
Hel
RMR =
Y
i<j
(txixj;q)∞
(xixj;q)∞
= exp
(∞X
k=1
1−tk
1−qk
p2
k
2k− p2k
2k
)
(47)
X
R even
Hoa
R MR =
Y
i
(qtx2
i ;q2)∞
(x2
i ;q2)∞
Y
i<j
(txixj;q)∞
(xixj;q)∞
=
Y
i<j
(txixj;q)∞
(xixj;q)∞
= exp
(∞X
k=1
 1−tk
1−qk
p2
k
2k + 1 +tk
1 +qk
p2k
2k
)
(48)
