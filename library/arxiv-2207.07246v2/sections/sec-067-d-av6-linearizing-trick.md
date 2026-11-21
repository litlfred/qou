---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-067-d-av6-linearizing-trick
section_title: "D AV6' LINEARIZING TRICK"
section_number: null
pages: 150-153
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
toc_source: outline
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 73 sections: Front matter; ABSTRACT; ACKNOWLEDGEMENTS"
---
140
Here I follow the note written by my advisor, and present how the six AV6’
operators in the propagator are linearized. First of all, notice that for non-negative
integer n,
hP6
p=1 vp(rij)Op
ij
in
can still be express by the linear combination of the
same 6 operators (just with diﬀerent coeﬃcients in front of the each operator). The 6
operators form a group. This is the foundation.
We then follow my advisor’s way of labeling the order of the operators. For a given
ij pair, label them 1 and 2, we wish to calculate the AV6’ propagator linear in the 6
of its operators such that,
e−[vc+vσ⃗σ1·⃗σ2+vtS12+vτ⃗τ1·⃗τ2+vστ⃗τ1·⃗τ2⃗σ1·⃗σ2+vtτS12⃗τ1·⃗τ2]∆τ
=
pc + pσ⃗σ1 ·⃗σ2 + ptt12 + pτ⃗τ1 ·⃗τ2 + pστ⃗τ1 ·⃗τ2⃗σ1 ·⃗σ2 + ptτt12⃗τ1 ·⃗τ2
(D.1)
where S12 is the tensor operator in Eq.(2.20). We need to solve for the coeﬃcients
pc, pσ, pt, pτ, pστ, ptτ. We choose z axis to be along ˆr in S12, and for the 6 operators we
can ﬁnd 6 states in terms of the total isospin quantum number T and spin quantum
number S and its z component Sz. We list the states and the corresponding eigenvalues
for certain operators in Table D.1.
Table D.1: The 6 total isospin and spin states of the AV6’ interaction.
Label
State
τ1 · τ2
σ1 · σ2
S12
Degeneracy
1
|S = 1, |Sz| = 1⟩⊗|T = 1⟩
1
1
2
6
2
|S = 1, Sz = 0⟩⊗|T = 1⟩
1
1
-4
3
3
|S = 1, |Sz| = 1⟩⊗|T = 0⟩
-3
1
2
2
4
|S = 1, Sz = 0⟩⊗|T = 0⟩
-3
1
-4
1
5
|S = 0⟩⊗|T = 0⟩
1
-3
0
3
6
|S = 0⟩⊗|T = 0⟩
-3
-3
0
1
Next, we sandwich e−[vc+vσ⃗σ1·⃗σ2+vtS12+vτ⃗τ1·⃗τ2+vστ⃗τ1·⃗τ2⃗σ1·⃗σ2+vtτS12⃗τ1·⃗τ2]∆τ between each
of the 6 labeled states listed in Table D.1, and we get the 6 equations correspondingly,
⟨1|e−[vc+vσ⃗σ1·⃗σ2+vtS12+vτ⃗τ1·⃗τ2+vστ⃗τ1·⃗τ2⃗σ1·⃗σ2+vtτS12⃗τ1·⃗τ2]∆τ|1⟩
⇒1⃝
e1 = exp [−(vc + vσ + 2vt + vτ + vστ + 2vtτ)∆τ]
⟨2|e−[vc+vσ⃗σ1·⃗σ2+vtS12+vτ⃗τ1·⃗τ2+vστ⃗τ1·⃗τ2⃗σ1·⃗σ2+vtτS12⃗τ1·⃗τ2]∆τ|2⟩
⇒2⃝
e2 = exp [−(vc + vσ −4vt + vτ + vστ −4vtτ)∆τ]
⟨3|e−[vc+vσ⃗σ1·⃗σ2+vtS12+vτ⃗τ1·⃗τ2+vστ⃗τ1·⃗τ2⃗σ1·⃗σ2+vtτS12⃗τ1·⃗τ2]∆τ|3⟩
⇒3⃝
e3 = exp [−(vc + vσ + 2vt −3vτ −3vστ −6vtτ)∆τ]
⟨4|e−[vc+vσ⃗σ1·⃗σ2+vtS12+vτ⃗τ1·⃗τ2+vστ⃗τ1·⃗τ2⃗σ1·⃗σ2+vtτS12⃗τ1·⃗τ2]∆τ|4⟩
⇒4⃝
e4 = exp [−(vc + vσ −4vt −3vτ −3vστ + 12vtτ)∆τ]
⟨5|e−[vc+vσ⃗σ1·⃗σ2+vtS12+vτ⃗τ1·⃗τ2+vστ⃗τ1·⃗τ2⃗σ1·⃗σ2+vtτS12⃗τ1·⃗τ2]∆τ|5⟩
⇒5⃝
e5 = exp [−(vc −3vσ + vτ −3vστ)∆τ]
⟨6|e−[vc+vσ⃗σ1·⃗σ2+vtS12+vτ⃗τ1·⃗τ2+vστ⃗τ1·⃗τ2⃗σ1·⃗σ2+vtτS12⃗τ1·⃗τ2]∆τ|6⟩
⇒6⃝
e6 = exp [−(vc −3vσ −3vτ + 9vστ)∆τ] .
141
From Eq.(D.1), we know that we need to solve for the coeﬃcients pc, pσ, pt, pτ, pστ, ptτ
from the already obtained values of e1, e2, e3, e4, e5, e6,
e1 = pc + pσ + 2pt + pτ + pστ + 2ptτ
e2 = pc + pσ −4pt + pτ + pστ −4ptτ
e3 = pc + pσ + 2pt −3pτ −3pστ −6ptτ
e4 = pc + pσ −4pt −3pτ −3pστ + 12ptτ
e5 = pc −3pσ + pτ −3pστ
e6 = pc −3pσ −3pτ + 9pστ,
which can be written in the matrix form,







e1
e2
e3
e4
e5
e6







=







1
1
2
1
1
2
1
1
−4
1
1
−4
1
1
2
−3
−3
−6
1
1
−4
−3
−3
12
1
−3
0
1
−3
0
1
−3
0
−3
9
0














pc
pσ
pt
pτ
pστ
ptτ







.
(D.2)
The coeﬃcients pc, pσ, pt, pτ, pστ, ptτ can be solved by matrix inversion,







pc
pσ
pt
pτ
pστ
ptτ







= 1
48







18
9
6
3
9
3
6
3
2
1
−9
−3
6
−6
2
−2
0
0
6
3
−6
−3
3
−3
2
1
−2
−1
−3
3
2
−2
−2
2
0
0














e1
e2
e3
e4
e5
e6







.
(D.3)
In other words, once we know e1, e2, e3, e4, e5, e6, the coeﬃcients pc, pσ, pt, pτ, pστ, ptτ
are written as,
pc = (6e1 + 3e2 + 2e3 + e4 + 3e5 + e6)/16,
pσ = (6e1 + 3e2 + 2e3 + e4 −9e5 −3e6)/48,
pt = (3e1 −3e2 + e3 −e4)/24,
pτ = (2e1 + e2 −2e3 −e4 + e5 −e6)/16,
pστ = (2e1 + e2 −2e3 −e4 −3e5 + 3e6)/48,
ptτ = (e1 −e2 −e3 + e4)/24 .
The six coeﬃcients pc, pσ, pt, pτ, pστ, ptτ are the corresponding six up(rij) in Eq.(2.65).
142
