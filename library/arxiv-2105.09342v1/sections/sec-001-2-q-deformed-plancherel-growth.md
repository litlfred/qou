---
doc_id: arxiv-2105.09342v1
doc_title: "A Unitary Matrix Model for q-deformed Plancherel Growth"
section_id: sec-001-2-q-deformed-plancherel-growth
section_title: "q-deformed Plancherel growth"
section_number: 2
pages: 4-7
source_pdf: 2105.09342v1.pdf
source_sha256: 57ae12327da7b9a1
---
The Plancherel growth of Young diagrams has been a topic of intense study over many
years. In order to explain the growth process, let λk denote a Young diagram with k boxes.
1Look at [14] and references therein for other applications of Plancherel measure and its q-deformation
in physics.
4
Consider two Young diagrams λk and λk+1 such that λk+1 is obtained from λk by adding
one box. One can associate a transition probability
ptran(λk;λk+1) = 1
k + 1
dimλk+1
dimλk
(2.1)
ifλk+1 is obtained from λk by adding one box, and zero otherwise. Here, dim λk denotes the
dimension of the representation of symmetric group Sk corresponding to Young diagram λk
and is given by
dimλk = k!∏
u∈λk
h(u) = k!∏
ihi!
∏
i<j
(hi−hj). (2.2)
We denote the total number of boxes in a Young diagram by l(λ) and the number of boxes
in ith row by{λi}i=1,..,l(λ) such that λ1≥λ2≥...≥λl(λ)≥ 0. The hook number for a given
λi is given by
hi =λi +l(λ)−i. (2.3)
They satisfy the constraint
h1 >h 2 >··· >h l(λ) > 0. (2.4)
The expression (2.2) is known as thehook length formula [16]. For a growth process governed
by (2.1), one can calculate the probability to ﬁnd a Young diagram λk at the kth level,
starting from a diagram with zero box. See [1] for details. It turns out to be the well known
Plancherel probability and is given by
P(λk) = (dimλk)2
k! . (2.5)
A natural q-deformation of the Plancherel growth process has been studied in [9, 17,
18]. It follows from the representation theory of Iwahori-Hecke algebras. The transition
probability of going from λk to λk+1 is given by
pq
tran(λk;λk+1) =qb(λk+1)−b(λk)
∏
u∈λk
[h(u)]∏
u∈λk+1
[h(u)] (2.6)
where 0 <q < 1 is the deformation parameter. The constant b is given by
b(λ) =
l(λ)∑
i=1
(i− 1)λi (2.7)
and
1∏
u∈λk
[h(u)] =
∏
i<j[hi−hj]∏
i[hi]! . (2.8)
5
The square bracket in the above expression represents the q-analogue of a positive integer
deﬁned as
[x] = 1−qx (2.9)
and
[x]! = [x][x− 1]··· [2][1]. (2.10)
The probability measure associated to a Young diagram λk growing according to (2.6) is
given by
Pq(λk) = (1−q)k dimλk
qb(λk)
∏
u∈λk
[h(u)]. (2.11)
This is the q-deformed Plancherel measure considered in [9, 18]. Using lim q→1
[x]
1−q = x, we
see that
lim
q→1
Pq(λk) =P(λk). (2.12)
Thus, in the limit q→ 1, the q-deformed measure reduces to the Plancherel measure.
Strahov in [9] gave a diﬀerential model for the q-deformed Plancherel growth process
(2.6). He introduced a function vk(u) which describes the proﬁle of a rotated Young diagram
as shown in ﬁg.(2). As the number of boxes becomes very large, Strahov deﬁned a rescaled
X
Y
Figure 2: A typical Young diagrams written in the Russian convention.
function
ˆvk(u) = v(u
√
k)√
k
(2.13)
such that the area under the curve is ﬁnite. The boundary of Young diagram becomes
smooth under scaling. He also introduced a q-deformedR function associated with ˆvk, given
by
Rˆv(x;q) = 1−q
1−qx exp
[
− lnq−1
∫ dσ(u)
1−qx−u
]
(2.14)
where σ(u) = 1
2(ˆv(u)−|u|) is deﬁned as the charge of a diagram [5]. It was shown that
the dynamical equation governing the growth of Young diagrams equipped with q-deformed
6
Plancherel measure is given in terms of the R-function as
∂Rˆv(.,t;q)(x;q)
∂x + (1−q)
lnq−1 R−1
ˆv(.,t;q)(x;q)∂Rˆv(.,t;q)(x;q)
∂t = 0. (2.15)
This is a q-analogue of the automodel equation. It can be expressed in diﬀerent equivalent
forms in terms of various other quantities associated to Young diagrams [9].
There exists another interesting class of q analog of Plancherel measure studied in [2] for
which
Pq(λk) =
(dimqλk
k!
)2
=k!(1−q)2k q2b(λk)
∏
u∈λk
[h(u)]2 =k!(1−q)2kq2b(λk)
∏
1≤i<j≤N[hi−hj]2
∏N
i=1([hi]!)2
. (2.16)
Such a measure plays an important role in the context of topological string theory partition
function on certain Calabi-Yau threefolds and Gromov-Witten invariants of P1 [10–14]. Un-
like (2.11), here the probability is proportional to the square of q dimension. This simpliﬁes
the large N analysis to a great extent. The saddle point equation can be solved exactly
in terms of the deformation parameter q. We observe that the behaviour of the automodel
diagrams is qualitatively the same in both cases. Therefore, we mainly focus on the growth
process governed by (2.16) and write a q-analogue of the automodel equation in terms of
Young diagram density . For completeness, we also discuss the growth process under (2.11).
However, in this case we are only able to provide the correction to automodel diagrams for
the values of q close to 1.
