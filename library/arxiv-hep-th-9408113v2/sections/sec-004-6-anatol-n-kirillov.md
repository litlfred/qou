---
doc_id: arxiv-hep-th-9408113v2
doc_title: "Dilogarithm identities"
section_id: sec-004-6-anatol-n-kirillov
section_title: "Anatol N. Kirillov"
section_number: 6
pages: 6-6
source_pdf: 9408113v2.pdf
source_sha256: dadd96e1155e820f
doc_brief: "Dilogarithm identities — We study the dilogarithm identities from algebraic, analytic, asymptotic, K-theoretic, combinatorial and representation-theoretic points of view."
---
B. Feigin, A. Kato, A. Kuniba, B. Leclerc, N.A. Liskova, T. Mi wa, W. Nahm, M. Noumi,
R. Sasaki, E. Sklyanin, M. Suzuki, V. Tarasov, J.-Y. Thibon, A.Yu. Volkov and M. Waki-
moto for fruitful discussions and valuable remarks. I also t hank with much gratitude the
colleagues at Tokyo University for their invitation, their hospitality which made it possible
to ﬁnish this work.
I would like to acknowledge my special indebtedness to Dr. N. A. Liskova for the
inestimable help in preparing the manuscript to publicatio n.
1.1. Dilogarithm (G. Leibnitz (1696), L. Euler (1768), L. Rogers (1906)).
1.1.1. Euler’s and Rogers’ dilogarithm.
The Euler dilogarithm function Li2(x) deﬁned for 0 ≤x≤ 1 by
Li2(x) :=
∑
n≥1
xn
n2 =−
∫ x
0
log(1−t)
t dt (1.1)
is one of the lesser transcendental function. Nonetheless, it has many intriguing properties
and has appeared in various branches of mathematics and phys ics.
It is also convenient to introduce the Rogers dilogarithm fu nction L(x) deﬁned for
0<x< 1 by
L(x) :=
∞∑
n=1
xn
n2 + 1
2 logx· log(1−x) =− 1
2
∫ x
0
(log(1−y)
y + logy
1−y
)
dy. (1.2)
The function L(x) has an analytic continuation to the complex plane cut analo g the real
axis from−∞ to 0 and 1 to + ∞.
1.1.2. Five-term relation and characterization of Rogers’ diloga rithm.
Theorem A (W. Spence (1809), N. Abel (1830), C. Hill (1830), E. Kummer ( 1840)).
The function L(x) belongs to the class C∞((0, 1)) and satisﬁes the following functional
equations
