---
doc_id: arxiv-1512.04993v2
doc_title: "Complexity, action, and black holes"
section_id: sec-007-26-bound-on-complexity-growth-with-a-conserved-c
section_title: "Bound on complexity growth with a conserved charge"
section_number: 2.6
pages: 14-16
source_pdf: 1512.04993v2.pdf
source_sha256: b8047bc3d3815406
doc_brief: "Complexity, action, and black holes — Our earlier paper “Complexity Equals Action” conjectured that the quantum computational complexity of a holographic state is given by the classical action of a"
---
The bound Eq. 2.14 is general, but if the system carries conserved quantum numbers
such as charge Q or angular momentum J, a tighter bound might be possible. In-
tuitively this is because conserved charges provide a barrier to rapid complexiﬁcation
since some energy is tied up in noncomputing degrees of freedom. We ﬁrst motivate
the bound using the charged TFD state and then present the bound.
To deﬁne the charged version of the TFD state we introduce a chemical potential
µ. We may think of the chemical potential as an electrostatic potential that is positive
on one side of the black hole and negative on the other. The TFD state is given by
|TFDµ⟩ =Z−1/2
∑
α
e−β(Eα+µQα)/2|Eα,Qα⟩L|Eα,−Qα⟩R (2.15)
The time evolution of the state is modiﬁed by the chemical potential,
|ψ(tL,tR)⟩ =e−i(HL+µQL)tLe−i(HR−µQR)tR|TFDµ⟩. (2.16)
(Here HL and HR are the µ = 0 Hamiltonians.) By the same argument that lead to
the µ = 0 bound, the complexiﬁcation bound becomes
dC
dt≤ 2
πℏ [(M−µQ)− (M−µQ)gs] (charged black holes), (2.17)
13
where the subscript gs indicates the state of lowest ( M−µQ) for a given chemical
potential µ.6 For rotating black holes the bound becomes
dC
dt≤ 2
πℏ [(M− ΩJ)− (M− ΩJ)gs] (rotating black holes), (2.18)
where the role of the chemical potential is played by the angular velocity Ω.
Bounds of the type Eq. 2.17 and Eq. 2.18 can be understood using the thermody-
namic relation,
d(M−µQ) =TdS (2.19)
or its integrated form,
[(M−µQ)− (M−µQ)gs] =
∫ S
gs
TdS. (2.20)
In other words [(M−µQ)− (M−µQ)gs] is the heat content or internal energy relative
to the ground state at ﬁxedµ. One way to state our hypothesis that black holes are the
fastest computers is that they eﬃciently use all of their internal energy to complexify. 7
In other words black holes saturate the bound
dC
dt≤
∫ S
gs
TdS. (2.21)
For rotating black holes inD = 3 we ﬁnd that the bound is saturated. For charged
black holes the situation is more complicated. Assuming the true ground state is
empty AdS or the extremal black hole at ﬁxed chemical potential as appropriate, we
can show that the bound is sometimes saturated but generally violated. However,
proper evaluation of the bound raises a diﬃcult dynamical question, speciﬁcally the
nature of the ground state at nonzero chemical potential. The nature of the ground
state depends on the full operator content of the conformal ﬁeld theory and hence
requires a proper UV completion of Einstein-Maxwell theory. At least we must specify
the light charged degrees of freedom.
In some cases supersymmetry provides additional constraints and the bound seems
to be saturated. More generally the bound appears to be either qualitatively valid, up
to an order one factor, or badly violated but in a situation where the true ground state
is probably drastically diﬀerent from the extremal black hole. We ﬁnd the uncharged
bound of Eq. 2.14 is always obeyed.
6M−µQ is natural when viewing µ as an electrostatic potential which modiﬁes the total energy.
For another perspective on the proposed bound, note that the complexity of eiµQt oscillates in time
with period 2π/µ because Q has integer spectrum. We believe that the combination M−µQ serves
to remove this rapidly oscillating portion of the complexity.
7In earlier work the integral in Eq. 2.20 was replaced by the simpler expression TS. Generally the
two are approximately the same, but in§4 we will encounter a case in which they are not. This is the
case of near-extremal large charged AdS black holes.
14
