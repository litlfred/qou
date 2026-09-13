---
doc_id: arxiv-math-9301212v1
doc_title: "APPEARED IN BULLETIN OF THE"
section_id: sec-002-0-1-tf-u-εt-dt
section_title: "(1 − t)f ′(u + εt) dt"
section_number: 0
pages: 4-5
source_pdf: 9301212v1.pdf
source_sha256: 029787800ddf73e5
---
and
ε− = ε−(u) = D((I ◦ γ)(u − ε), (I ◦ γ)(u)) = f (u)ε − ε2
∫ 1
0
(1 − t)f ′(u − εt) dt.
Since |f ′(w)| is uniformly bounded, we have
1
ε+
= 1
f (u)ε
[
1
1 + (ε/f (u))
∫ 1
0 (1 − t)f ′(u + εt) dt
]
= 1
f (u)ε
[
1 − ε
f (u)
∫ 1
0
(1 − t)f ′(u + εt) dt + O(ε2)
]
= 1
f (u)ε − 1
f (u)2
∫ 1
0
(1 − t)f ′(u + εt) dt + O(ε).
Similarly,
1
ε−
= 1
f (u)ε + 1
f (u)2
∫ 1
0
(1 − t)f ′(u − εt) dt + O(ε).
Then by (4)
(5)
regularization (2) = 4 −
∫
R/l Z
2
ε du
+
∫ ∫
R/l Z×[0, 1]
(1 − t)
f (u) [f ′(u + εt) − f ′(u − εt)] du dt + O(ε)
= 4 − 2l
ε + O(ε) + O(ε).
Comparing (3) and (5), we get
Eε(γ) − Eε(I ◦ γ) = O(ε);
hence, E(γ) = E(I ◦ γ).
For the second assertion, let I send a point of γ to inﬁnity. In this case L = ∞
and, thus, the constant term 4 in (5) disappears. □
Acknowledgment
The authors wish to thank Adriano Garsia and Fred Hickling for usefu l discus-
sions.
M ¨OBIUS INV ARIANCE OF KNOT ENERGY 5
