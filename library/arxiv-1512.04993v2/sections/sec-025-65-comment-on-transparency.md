---
doc_id: arxiv-1512.04993v2
doc_title: "Complexity, action, and black holes"
section_id: sec-025-65-comment-on-transparency
section_title: "Comment on transparency"
section_number: 6.5
pages: 42-47
source_pdf: 1512.04993v2.pdf
source_sha256: b8047bc3d3815406
doc_brief: "Complexity, action, and black holes — Our earlier paper “Complexity Equals Action” conjectured that the quantum computational complexity of a holographic state is given by the classical action of a"
---
Finally, let us comment on the transition in complexity growth that occurs at|tw|−t∗ =
tR. This transition is precisely the transparent and opaque horizons of [55]. From
Eq. 6.14 we see that there is a period during which the complexity decreases on the
right side,
dC
dtR
< 0, (|tw|− t∗ >t R). (6.24)
This corresponds to the thermodynamically rare situation of an “opaque” horizon.
Any observer that jumps into the black hole will get destroyed at the horizon by a high
41
energy shock wave!
On the other hand, fortR >|tw|−t∗ Eq. 6.13 indicates that the complexity resumes
it normal increasing behavior,
dC
dtR
> 0, (|tw|− t∗ <t R). (6.25)
According to [55] increasing complexity corresponds to a “transparent” horizon. As
mentioned in §6.1, this is because we have evolved the state to a point where the
backreaction of the precursor is negligible. Were an observer to jump in, at the horizon
he or she would only encounter a harmless particle of vanishing energy.
We can also use the CA-duality to generalize the notion of transparency to localized
shock wave geometries. For these geometries, the strength of the shock wave h(x) is
dependent on spatial position. One can deﬁne a speciﬁc complexity c(x) by not inte-
grating the action over the spatially transverse directions of the Wheeler-DeWitt patch.
This is roughly a measure of how the complexity is changing along these transverse
directions. We expect that c(x) will be a piecewise continuous function, with the point
of transition depending on x. As before, the transition occurs when W moves oﬀ the
past singularity. Computing this point of transition as a function of x,tw,tR, we ﬁnd
that a “wave of transparency” propagates ballistically with the butterﬂy velocity vB.
7 Tensor network model of
Einstein-Rosen bridge growth
In this section we will perform a nontrivial test of our conjecture using tensor networks.
Tensor networks provide a microscopic account of complexity growth, and we will show
that this microscopic account agrees with the results from CA-duality. Further, as the
case with shock waves in §6, this derivation highlights that the complexity growth is
dual to the minimal quantum circuit that builds the state.
The tensor-network model serves several purposes. It justiﬁes the reduction of the
UV Hilbert space of the CFT to a number of active qubits that is not UV sensitive
and instead scales like the entropy; it gives a concrete model of complexity along the
lines discussed in Appendix A; it shows that the growth of complexity is roughly given
by TS ; it justiﬁes the Hartman-Maldacena proposal [3]; and it further supports our
speculation that there is an eﬀective low-energy notion of complexity that the action
is calculating. We ﬁrst discuss the tensor network picture for one side of the two-sided
black hole; then we discuss the tensor network for the two-sided black hole and examine
42
its time development.13
Recall that a CFT is expected to have no long range entanglement on scales longer
than the inverse temperature 1 /T . The basic picture is that the ground state renor-
malization group (RG) circuit remains a good description of the ﬁnite temperature RG
circuit on scales shorter than 1/T ; at longer scales the state becomes trivial (unentan-
gled). The RG circuit will typically diﬀer from the ground state circuit as the scale 1/T
is approached, but for simplicity we model the physics using the ground state circuit
and a sharp cutoﬀ at scale 1 /T .
The ﬁnite temperature state of the CFT is then
ρ(L,T ) =Vkρ(L/2k, Λ0)
(
V†)k
(7.1)
where V is one circuit layer implementing coarse graining by a factor of 2, Λ 0 is some
UV energy scale [ρ(L′,T = Λ0) has only cutoﬀ-scale correlations], and k = log2(Λ0/T )
is the RG depth. The system size is denoted by the argument L in ρ(L,T ) and the
number of lattice sites is ( LΛ0)D−2 (recall that the CFT lives in D− 1 spacetime
dimensions; D is the bulk spacetime dimension).
That was the description of one side of the black hole, but what about the two-
sided black hole that puriﬁes ρ(L,T )? Let the thermoﬁeld double state which puriﬁes
ρ(L,T ) be|TFD(L,T )⟩. The RG circuit for the thermoﬁeld double state may then be
written
|TFD(L,T )⟩ =Vk⊗ (V∗)k|TFD(L/2k, Λ0)⟩ (7.2)
where V∗ appears because ρ(L,T ) and|TFD(L,T )⟩ are related by a partial transpose
on the second factor. The state|TFD(L′, Λ0)⟩ roughly consists of (L′Λ0)D−2 EPR pairs
shared between the two sides of the thermoﬁeld double.
(In fact, this cannot be quite right because the spectrum ofρ(L,T ) is not completely
degenerate—the thermoﬁeld double state is not perfectly maximally entangled—so
some spread of the eigenvalues of the reduced state is necessary. However this is not
an essential part of the story.)
Now we time evolve the TFD state with the Hamiltonian H⊗I +I⊗H. This can
be represented by a tensor network where we act on the thermoﬁeld double state with
U(t)⊗U(t), where U(t) =e−iHt is time evolution with respect to the UV Hamiltonian
H. Let us ask about the complexity of the resulting state. A naive estimate is
Cnaive =CRG +cΛ0(LΛ0)D−2t, (7.3)
but in fact this UV divergent expression is only an upper bound. A much more eﬃcient
circuit can be found by ﬁrst renormalizing the operator U(t), see Figs. 15 and 16.
43
Figure 15: Step 1: the time evolution acting on the UV degrees of freedom is renormal-
ized into a time evolution acting on the IR degrees of freedom. The orange connection
is the Einstein-Rosen bridge, the red region is the RG network, and the blue parts
represent time evolution.
Figure 16: Step 2: the IR time evolution is “rotated” from vertical to horizontal and
becomes a part of the Einstein-Rosen bridge. The orange connection is the Einstein-
Rosen bridge, the red regions are the RG networks, and the blue parts represent time
evolution.
44
To compute this renormalization it is useful to work with an inﬁnitesimal time step:
U(δt) = I−i(δt)H. The crucial piece of physics is that H is a scaling operator with
dimension ∆H = 1 (because it is the integral of the energy density which has dimension
D− 1). Hence we have
H(L)V =V 2−∆HH(L/2), (7.4)
where V is one layer of the RG circuit, 14 and the parenthetical superscript indicates
the size of the system. By deﬁnition we have I(L)V =VI (L/2). It follows that for one
RG step (
I(L)−iδtH (L))
V =V
(
I(L/2)−iδt2−∆HH(L/2))
(7.5)
and that for k RG steps
(
I(L)−iδtH (L))
Vk =Vk
(
I(L/2k)−iδt2−∆HkH(L/2k)
)
. (7.6)
Thus time evolution at the UV scale for time t can be traded for time evolution at a
longer scale for time 2−∆Hkt. Alternatively, if the UV Hamiltonian HL has microscopic
energy scale Λ 0 and acts on ( LΛ0)D−2 sites, we may obtain the same action from a
renormalized Hamiltonian with UV scale Λ 0/2k acting on (LΛ0/2k)D−2 sites.
If the number of RG steps is k = log 2(Λ0/T ) then the scale of the renormalized
Hamiltonian is Λ 0/2k =T and the number of sites on which it acts is ( LΛ0/2k)D−2 =
(LT )D−2. Evolving for total time t, the complexity is now upper bounded by
C≤C RG +cT (LT )D−2t∼C RG +TS (T )t. (7.7)
This is illustrated in Fig. 15. The tensor network analysis therefore gives qualitatively
the same result as we independently derived using CA-duality.
Complexity per gate is O(c)
Implicit in the above analysis was the assumption that the complexity per gate in the
tensor network is roughly c for a CFT 2 (with the obvious generalization to higher di-
mensions). This is not a trivial assertion; for example, it was proposed [57] that random
tensors make a good starting point for thinking about the entanglement properties of
holographic ﬁeld theories. However, with high probability a random tensor would be
of at least scrambling complexity O(c logc) and possibly (depending on the ensemble
13For additional work on the relationship between tensor networks and geometry, see also [56–63].
14This equation can in principle contain another term, call it O, on the RHS. This term must have
the property that V †O = 0 and represents a high-energy contribution not captured by acting with
H (L/2) and thenV . It can nevertheless be argued to be irrelevant for the complexity growth. To fully
show that the eﬀective IR time evolution is approximately unitary one would have to examine this
correction term more carefully.
45
from which the tensor is drawn) of much higher complexity. Recently random tensors
have been further advanced [62, 64, 65] as toy models of holography and have been
shown to satisfactorily model the entanglement structure of the ﬁeld theory in terms
of bulk minimal surfaces. However here we argue that such models do not correctly
capture the complexity properties of the holographic ﬁeld theory.
Let us justify this claim. First, note that each line in the tensor network should be
understood as consisting of O(c) degrees of freedom bundled together. In other words,
every site of the lattice theory has O(c) degrees of freedom, so if, for example, the ﬁeld
theory consists of a large- N SU(N) gauge theory, then each lattice site consists of a
large-N matrix quantum mechanics (coupled to the other sites) and we expectc∼N 2.
It is easiest to ﬁrst analyze the part of the network corresponding to conventional
time evolution (the wormhole part). Implementing one layer of gates in the circuit
corresponds to evolving with our properly normalized local Hamiltonian for a time of
order the inverse temperature. Since the local Hamiltonian acts on O(c) degrees of
freedom per site and we evolve for a time of order β, the complexity of the resulting
tensor is also O(c). This implies that the rate of increase in complexity is proportional
to the product of the central charge c, the number of thermal cells ( LT )D−2, and the
temperature T . This combines to give ST .
Now let us analyze the RG part of the network (the part outside the horizon).
Suppose we are performing a 2 → 1 RG procedure in one boundary spatial dimension
(D = 3) by mapping the ground state onL sites to the ground state on L/2 sites. This
mapping is accomplished by some unitary transformation acting on the local degrees
of freedom. Existence of a smooth continuum limit suggests that this unitary is the
exponential of a local Hermitian generator. In other words, the RG generator should
share the rough characteristics of an ordinary local Hamiltonian acting on the system.
The basic point is then that to achieve scrambling complexityO(c logc) for the local
gates, we would have to run the local evolution for a time O(logc). However, because
the local generator also couples neighboring sites, correlations will be generated at
scale O(logc). This is unphysical—correlations of O(logc) are not compatible with
bulk locality on the AdS scale. Hence the RG transformation must correspond to
running a local generator for a RG time of order one. This implies that the complexity
of the gates in the RG transformation are O(c) as claimed.
