---
doc_id: arxiv-1504.07260v3
doc_title: "Fricke S-duality in CHL models"
section_id: sec-010-32-self-duality-and-the-witten-index
section_title: "Self-duality and the Witten index"
section_number: 3.2
pages: 20-22
source_pdf: 1504.07260v3.pdf
source_sha256: 707cb014400a3f05
doc_brief: "Fricke S-duality in CHL models — We consider four dimensional CHL models with sixteen spacetime supersym- metries obtained from orbifolds of type IIA superstring on K3×T 2 by aZN symmetry acting"
---
From the above discussion, it is clearly important to determine which CHL models are self-
dual under Fricke S-duality. This can be determined simply in terms of the Frame shape∏
a|Nam(a) of g, by analyzing the associated Witten index as we now show.
LetC be a non-linear sigma model on K3 and g be a symmetry ofC of order N
preserving theN = (4, 4) superconformal algebra. We will assume that the orbifold ofC
by g is a consistent CFTC′; in our previous notation, this means thatλ = 1 and ˆN =N
(the caseλ >1 is treated in appendix A.3). It follows that the orbifold CFTC′ is either
a non-linear sigma model on K3 or on a four dimensional torusT 4. Furthermore,C′ has a
symmetryQ of orderN (the quantum symmetry) that acts by multiplication bye
2πir
N on
the gr-twisted states.
Let∏
a|Nam(a),m(a)∈ Z, be the cycle shape associated tog. By (2.16), the condition
that the orbifold is consistent, i.eλ = 1, is equivalent to
∑
a|N
m(N/a)a∈ 24Z . (3.15)
The cycle shape determines the eigenvalues ofg on the 24 dimensional space Ramond-
Ramond ground states ofC. In this section, we will prove that the cycle shape describing
the action ofQ on the RR ground states of the orbifold theoryC′ is∏
a|Nam(N/a). This
statement needs a reﬁnement whenC′ is a torus model; we will be more precise below.
In general, the topology of the target space of aN = (4, 4) superconformal ﬁeld theory
C with central chargec = 6 can be distinguished by the Witten index3
IC(τ.¯τ) = TrRR((−1)F + ˜FqL0− c
24 ¯q
¯L0− c
24 ) =
{
24 ifC is a K3 model
0 ifC is a torus model,
(3.16)
where q = e2πiτ. The Witten index is the specialization to z = 0 of the elliptic genus
φ(τ,z ). By standard arguments, the only non-vanishing contribution to this trace comes
from the RR ground states, i.e. states with conformal weights(h, ¯h) = ( c
24, ¯c
24) = ( 1
4, 1
4), so
that the Witten index is actually a constant and it equals the Euler characteristic of the
target space.
If the theory has a symmetryg one can consider ag-twined version of the Witten index
(the specialization toz = 0 of the twining elliptic genusφg(τ,z ))
IC
g := TrRR(g(−1)F + ˜FqL0− c
24 ¯q
¯L0− c
24 ) , (3.17)
which is again a constant. In the case we are considering, whereC is a K3 model and
g has cycle shape ∏
a|Nam(a), the twining indexIC
g is simply the trace ofg on its 24-
dimensional representation (the RR ground states in K3 models have all positive fermion
number (−1)F + ˜F), so that
IC
g =
∑
a|N
m(a)
a∑
k=1
e
2πik
a =m(1) , (3.18)
3Of course, the Witten index can be deﬁned even for theories with a smaller superconformal algebra, in
particular forN = (2, 2) theories.
– 19 –
which is just the dimension of the ﬁxed subspace ofg. More generally, for any powergj we
have
IC
gj =
∑
u|(j,N)
m(u)u , (3.19)
where the right hand side is the dimension of the ﬁxed subspace ofgj. Notice that, once
the twined indicesIC
gj are known for allj = 1,...,N , using (3.19) one can reconstruct the
cycle shape ofg.
Similarly, one can consider the twined Witten indicesIC′
Qk, k = 1,...,N , associated
with the action of the quantum symmetryQ on the RR ground states of the orbifold theory
C′. Using standard orbifold techniques, this index can be computed in terms of the Frame
shape ofg (see appendix A.3)
IC′
Qk =
∑
n|(k,N)
m(N/n)n . (3.20)
By specializing to the casek =N, we obtain the Witten index of the orbifold theoryC′
IC′
=
∑
n|N
m(N/n)n . (3.21)
Thus, the condition (3.15) of consistency of the orbifoldC′ implies that the elliptic genus
of the orbifold theory is a multiple of24. Now, we see that, if (3.15) is satisﬁed, then the
only two possibilities areIC′
= 0 for a torus model andIC′
= 24 for a K3 model. This can
be also veriﬁed a posteriori for all possible cycle shapes of Conway elements.
IfIC′
= 24, thenC′ is a K3 model, and by comparing this formula with (3.19), we
conclude thatQ must correspond to a cycle shape∏
a|Nam(N/a). In particular,Q has the
same cycle shape asg if and only if the cycle shape is ‘balanced’ with balancing number
N, i.e.
m(a) =m(N/a) . (3.22)
If (3.22) holds, then (3.15) is automatically satisﬁed andC is a K3 model.
WhenC′ is a torus model, i.e.IC′
= 0, the cycle shape∏
a|Nam(N/a) determines the
eigenvalues ofQ(−1)F + ˜F on the RR ground states. Notice that, in this case, the fermion
number has to be taken into account, as it acts non-trivially on the RR ground states.
To summarise, the above analysis shows that there are three possible cases to take into
account:
Case 1: If the Frame shape isbalanced with balancing numberN, i.e. if
m(N/a) =a , (3.23)
for alla|N, then ∑
a|N
m(N/a)a = 24 , (3.24)
the orbifoldC′ is again a K3 model and the quantum symmetryQ has the same
Frame shape asg. Thus, in this case, the CHL model is self-dual and the latticeΛm
is N-modular.
– 20 –
Case 2: If the Frame shape is not balanced, but
∑
a|N
m(N/a)a = 24 , (3.25)
thentheorbifold C′ isagainaK3model, butFrameshape ∏
a|nam(N/a) ofthequantum
symmetryQ is diﬀerent fromg. Thus, in this case, S-duality relates two diﬀerent CHL
models. In particular, ifΛm and Λ′
m are the lattices of magnetic charges in these two
models, we have the relation
Λ∗
m∼= Λ′
m(N) . (3.26)
Case 3: If ∑
a|N
m(N/a)a = 0 , (3.27)
then the orbifoldC′ is a torus model. Thus, the CHL model is dual to type IIA on
(T 4×S′)/ZN× ˜S′.
