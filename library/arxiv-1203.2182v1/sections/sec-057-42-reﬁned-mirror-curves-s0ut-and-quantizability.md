---
doc_id: arxiv-1203.2182v1
doc_title: "Volume Conjecture: Reﬁned and Categoriﬁed"
section_id: sec-057-42-reﬁned-mirror-curves-s0ut-and-quantizability
section_title: "Reﬁned mirror curves, S0(u,t ) and quantizability"
section_number: 4.2
pages: 60-61
source_pdf: 1203.2182v1.pdf
source_sha256: 2fe21af194f65227
doc_brief: "Volume Conjecture: Refined and Categorified — The generalized volume conjecture relates asymptotic behavior of the colored Jones polynomials to objects naturally deﬁned on an algebra ic curve, the"
---
Once we found the reﬁned quantum curves, we can easily determ ine the classical reﬁned
mirror curves. Namely, much as in the knot theory examples, w e can ﬁnd them in two ways.
First, they arise as q2 → 1 limit of the quantum curves. Secondly, they can be determin ed
by the saddle point analysis. As we will see momentarily, bot h methods consistently give the
same result. The limit q2 → 1 of the C3 quantum curve (4.12) leads to the following reﬁned
mirror curve
Aref(x,y ;q1) = 1 −q1y +q1x(−y)f. (4.22)
Similarly, the reﬁned mirror curve for the conifold can be ob tained form (4.20) and takes the
form
Aref(x,y ;q1) = 1 −q1y +q1x(−y)f +Q√q1x(−y)f +1. (4.23)
By looking at the form of this reﬁned A-polynomial, a careful reader will recognize a close
relation with the example of the unknot discussed in section 3. Indeed, a simple change of
variables
unknot conifold
x ↦→ (−1)f +1t−2xyf
y ↦→ (−t)− 1
2y
(4.24)
– 59 –
relates reﬁnedA-polynomials (3.152) and (4.23), provided that we identifyq1 = −t as in (4.7)
that the K¨ ahler parameter of the conifold is tuned to a special value:
Q = it− 3
2. (4.25)
Note, the transformation (4.24) preserves the holomorphic symplectic form Ω = i
ℏ
dx
x ∧ dy
y on
C∗ × C∗ relevant to quantization.
To conﬁrm that the same reﬁned curves (4.22) and (4.23) arise from the saddle point
analysis we follow the strategy of section 3.3.3, where we di scussed analogous curves coming
from knot theory examples. Speciﬁcally, much like in (3.166 ), we wish to approximate the
BPS partition functions Z open
BPS in (4.10) and (4.18) by the integral
Z open
BPS ∼
∫
dz e
1
ℏ (V (z,x;q1)+O(ℏ)). (4.26)
As the computation is analogous for C3 and the conifold, we present it just in the latter case;
the result for C3 is easily obtained by setting Q = 0. Therefore, using the conifold amplitude
in the form (4.18) and the expansion of the quantum dilogarit hm given in (3.154), we ﬁnd
V (z,x ;q1) = (log z)
(
πi(f + 1) + logxq1
)
+ f
