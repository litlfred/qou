---
doc_id: arxiv-2302.05903v2
doc_title: "On combinatorial generalization(s) of Borel transform: Averaging method in combinatorics of symmetric polynomials"
section_id: sec-003-derivation-of-various-sum-formulas-by-the-averag
section_title: "Derivation of various sum formulas by the averaging method"
section_number: null
pages: 4-5
source_pdf: 2302.05903v2.pdf
source_sha256: 9a17abd36cc8a317
doc_brief: "On combinatorial generalization(s) of Borel transform: Averaging method in combinatorics of symmetric polynomials — We elaborate on the recent suggestion to consider averaging of Cauchy identities"
---
The averaging method can be easily modified to handle more examples. Say, we can ask the average ⟨SR⟩ = 1
only for even diagramsR, i.e. with all rows of even lengths, and vanishes otherwise. The corresponding measure
is still Gaussian,
Measure B :
(
⟨SR⟩B = 1 for even R
⟨SR⟩B = 0 otherwise : dµB∼
∞Y
k=1
dpk exp

− p2
2k−1
2(2k− 1)− (p2k− 1)2
4k

(18)
and the counterpart of (12) is
X
R even
SR =
X
R
SR⟨SR⟩B
| {z }
δR,even
=
D
e
P∞
k=1
pk ¯pk
k
EB
¯p
=
∞Y
k=1
exp
p2
k
2k + p2k
2k

(19)
Let us demonstrate how to prove that ⟨SR⟩B is non-zero and equal to 1 only for even partitions. To this end,
we note that the measure B is obtained from A by the shift of times pk→pk− (−1)k. In other words, we have
⟨SR{pk}⟩B =

SR{pk + (−1)k}

A
=
X
P
SR/P{(−1)k}⟨SR{pk}⟩A [8]
=
X
P
SR/P{(−1)k} =
X
P
(−1)|R|+|P|SR/P{1} (20)
The choice of pk = 1 is equivalent to choosing only one non-zero symmetric variable x1 = 1, and the sumP
P (−1)|P|SR/P{1} is not zero only when R is an even partition, which follows from the representation of the
skew Schur function SR/P = P
TxT with the sum running over all tableaux T of shape R−P , see details
in [7, Eq.(5.12)].
All further examples in this section are proved analogously. Note that checking this kind of claims is much
easier than proving them: one can just calculate simple Gaussian averages of the Schur functions at any concrete
example.
4
Now, in order to pick up only even columns, one need to make transposition, which is equivalent to changing
signs of all the time variables: the relevant measure, which gives ⟨SR⟩ = 1 for all even-column diagrams and
zero otherwise is
Measure C:
(
⟨SR⟩C = 1 for even R∨
⟨SR⟩C = 0 otherwise : dµC∼
∞Y
k=1
dpk exp

− p2
2k−1
2(2k− 1)− (p2k + 1)2
4k

(21)
and
X
R∨ even
SR =
X
R
SR⟨SR⟩C
| {z }
δR∨,even
=
D
e
P∞
k=1
pk ¯pk
k
EC
¯p
=
∞Y
k=1
exp
p2
k
2k− p2k
2k

(22)
Likewise the average with ⟨SR⟩D = (−1)νR(−1)3|R|/2 with νR = PlR
i=1(i− 1)Ri is provided by the Gaussian
measure
Measure D: ⟨SR⟩D = (−1)νR(−1)3|R|/2 : dµD∼
∞Y
k=1
exp

−p2
k
2k + (−1)k√
−1p2k−1
2k− 1− p4k−2
2k− 1

dpk (23)
Then
X
R
(−1)νRSR{p} =
X
R
(−1)|R|/2SR{p}⟨SR⟩D =
*
exp
 ∞X
k=1
(−1)k/2pk ¯pk
k
!+D
¯p
=
=
∞Y
k=1
exp

− p2
2k−1
2(2k− 1) + p2
2k
4k + p2k−1
2k− 1 + p4k−2
2k− 1

(24)
If cR counts the number of rows of odd length in R, then, introducing a formal parameter t,
Measure E: ⟨SR⟩E =tcR : dµE∼
∞Y
k=1
exp

−(p2k−1−t2k−1)2
2(2k− 1) − (p2k− 1 +t2k)2
4k

dpk (25)
and
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
(26)
Counting the number of columns of odd length is provided by the same formula with all the signs ofpk inverted,
see (34) below.
