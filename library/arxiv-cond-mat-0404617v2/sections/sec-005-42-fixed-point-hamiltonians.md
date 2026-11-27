---
doc_id: arxiv-cond-mat-0404617v2
doc_title: "String-net condensation: A physical mechanism for topological phases"
section_id: sec-005-42-fixed-point-hamiltonians
section_title: "Fixed-point Hamiltonians"
section_number: 4.2
pages: 6-8
source_pdf: cond-mat-0404617v2.pdf
source_sha256: 8e31b9ec8ac2e034
toc_source: inferred
doc_brief: "String-net condensation: A physical mechanism for topological phases — 18 sections: Front matter; Introduction; String-nets and gauge theories"
---
In this section, we construct exactly soluble lattice spin
Hamiltonians with the ﬁxed-point wave functions Φ as
ground states. These Hamiltonians provide an explicit
realization of all (2 + 1) D string-net condensates and
therefore all (2 + 1) D doubled topological phases (pro-
vided that we generalize these models as discussed in
Appendix A). In the next section, we will use them to
calculate the physical properties of the quasiparticle ex-
citations.
For every (F ijm
kln , di) satisfying the self-consistency con-
ditions (8) and the unitarity condition (14), we can con-
struct an exactly soluble Hamiltonian. Let us ﬁrst de-
scribe the Hilbert space of the exactly soluble model. The
model is a spin system on a (2D) honeycomb lattice, with
a spin located on each link of the lattice. Each “spin” can
be in N + 1 diﬀerent states labeled by i = 0, 1, ..., N. We
assign each link an arbitrary orientation. When a spin
is in state i, we think of the link as being occupied by
a type- i string oriented in the appropriate direction. We
think of the type-0 string or null string as the vacuum
(ie no string on the link).
I
p
i*i*
i* ii*
i
k k*
k
k* k
j
j*
j
j*
j
j*
j*
j j
j*
j
i
i
i
FIG. 8: A picture of the lattice spin model (10). The electric
charge operator QI acts on the three spins adjacent to the
vertex I, while the magnetic energy operator Bp acts on the
12 spins adjacent to the hexagonal plaquette p. The term QI
constrains the string-nets to obey the branching rules, whi le
Bp provides dynamics. A typical state satisfying the low-
energy constraints is shown on the right. The empty links
have spins in the i = 0 state.
The exactly soluble Hamiltonian for our model is given
by
H = −
∑
I
QI −
∑
p
Bp, B p =
N∑
s=0
asBs
p (10)
where the sums run over vertices I and plaquettes p of
the honeycomb lattice. The coeﬃcients as satisfy as∗ =
a∗
s but are otherwise arbitrary.
Let us explain the terms in (10). We think of the
ﬁrst term QI as an electric charge operator. It measures
the “electric charge” at site I, and favors states with no
charge. It acts on the 3 spins adjacent to the site I:
QI
⏐⏐⏐⏐
k
i j
⟩
= δijk
⏐⏐⏐⏐
k
i j
⟩
(11)
where δijk is the branching rule symbol (9). Clearly, this
term constrains the strings to obey the branching rules
described by δijk . With this constraint the low energy
Hilbert space is essentially the set of all allowed string-
net conﬁgurations on a honeycomb lattice. (See Fig. 8).
We think of the second term Bp as a magnetic ﬂux
operator. It measures the “magnetic ﬂux” though the
plaquette p (or more precisely, the cosine of the magnetic
ﬂux) and favors states with no ﬂux. This term provides
dynamics for the string-net conﬁgurations.
The magnetic ﬂux operator Bp is a linear combination
of (N +1) terms Bs
p, s = 0, 1, ..., N. Each Bs
p is an opera-
tor that acts on the 12 links that are adjacent to vertices
of the hexagon p. (See Fig. 8). Thus, the Bs
p are essen-
tially (N +1) 12 ×(N +1) 12 matrices. However, the action
of Bs
p does not change the spin states on the 6 outer links
of p. Therefore the Bs
p can be block diagonalized into
(N + 1)6 blocks, each of dimension ( N + 1)6 × (N + 1)6.
Let Bs,g ′h′i′j′k′l′
p,ghijkl (abcdef ), with a, b, c... = 0 , 1, ..., N, de-
note the matrix elements of these ( N + 1)6 matrices:
Bs
p
⏐⏐⏐⏐⏐⏐⏐⏐
a
b c
ef
d
h
l
g i
k
j
⟩
=
∑
m,...,r
Bs,g ′h′i′j′k′l′
p,ghijkl (abcdef )
⏐⏐⏐⏐⏐⏐⏐⏐
a
b c
ef
d
g’
j’k’
l’
i’
h’ ⟩
(12)
Then the operators Bs
p are deﬁned by
Bs,g ′h′i′j′k′l′
p,ghijkl (abcdef )
= F al∗g
s∗g′l′∗ F bg∗h
s∗h′g′∗F ch∗i
s∗i′h′∗F di∗j
s∗j′i′∗F ej∗k
s∗k′j′∗ F f k∗l
s∗l′k′∗ (13)
(See appendix C for a graphical representation of Bs
p).
One can check that the Hamiltonian (10) is Hermitian if
F satisﬁes
F i∗j∗m∗
k∗l∗n∗ = (F ijm
kln )∗ (14)
in addition to (8). Our model is only applicable to topo-
logical phases satisfying this additional constraint. We
believe that this is true much more generally: only topo-
logical phases satisfying the unitarity condition (14) are
physically realizable.
The Hamiltonian (10) has a number of interesting
properties, provided that ( F ijm
kln , di) satisfy the self-
consistency conditions (8). It turns out that:
1. The Bs
p and QI ’s all commute with each other.
Thus the Hamiltonian (10) is exactly soluble.
2. Depending on the choice of the coeﬃcients as, the
system can be in N + 1 diﬀerent quantum phases.
3. The choice as = ds∑ N
i=0 d2
i
corresponds to a topolog-
ical phase with a smooth continuum limit. The
ground state wave function for this parameter
choice is topologically invariant, and obeys the lo-
cal rules (4-7). It is precisely the wave function Φ,
deﬁned on a honeycomb lattice. Furthermore, QI ,
Bp are projection operators in this case. Thus, the
ground state satisﬁes QI = Bp = 1 for all I, p,
while the excited states violate these constraints.
The Hamiltonian (10) with the above choice of as pro-
vides an exactly soluble realization of the doubled topo-
logical phase described by F ijm
kln . We can obtain some in-
tuition for the Hamiltonian (10) by considering the case
where F ijm
kln is the 6 j symbol of some group G. In this
case, it turns out that QI and Bp are precisely the elec-
tric charge and magnetic ﬂux operators in the standard
lattice gauge theory with group G. Thus, (10) is the
usual Hamiltonian of lattice gauge theory, except with
no electric ﬁeld term. This is nothing more than the
well-known exactly soluble Hamiltonian of lattice gauge
theory. [20, 39] In this way, our construction can be
viewed as a natural generalization of lattice gauge the-
ory.
In this paper, we will focus on the smooth topolog-
ical phase corresponding to the parameter choice as =
ds∑ N
i=0 d2
i
(see appendix C). However, we would like to
mention that the other N quantum phases also have non-
trivial topological (or quantum) order. However, in these
phases, the ground state wave function does not have a
smooth continuum limit. Thus, these are new topological
phases beyond those described by continuum theories.
