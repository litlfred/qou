---
doc_id: arxiv-cond-mat-0404617v2
doc_title: "String-net condensation: A physical mechanism for topological phases"
section_id: sec-004-41-fixed-point-wave-functions
section_title: "Fixed-point wave functions"
section_number: 4.1
pages: 4-6
source_pdf: cond-mat-0404617v2.pdf
source_sha256: 8e31b9ec8ac2e034
toc_source: inferred
doc_brief: "String-net condensation: A physical mechanism for topological phases — 18 sections: Front matter; Introduction; String-nets and gauge theories"
---
In this section, we attempt to capture the universal
features of string-net condensed phases in (2 + 1) dimen-
sions. Our approach, inspired by Ref. [35–37, 42–44],
is based on the string-net wave function. We construct
a special “ﬁxed-point” wave function for each string-net
condensed phase. We believe that these “ﬁxed-point”
wave functions capture the universal properties of the
corresponding phases. Each “ﬁxed-point” wave function
is associated with a six index object F ijk
lmn that satisﬁes
certain algebraic equations (8). In this way, we derive
a one-to-one correspondence between doubled topologi-
cal phases and tensor categories F ijk
lmn. We would like
to mention that a related result on the classiﬁcation of
(2 + 1)D topological quantum ﬁeld theories was obtained
independently in the mathematical community. [34]
Let us try to visualize the wave function of a string-net
condensed state. Though we haven’t deﬁned string-net
condensation rigorously, we expect that a string-net con-
densed state is a superposition of many diﬀerent string-
net conﬁgurations. Each string-net conﬁguration has
a size typically on the same order as the system size.
The large size of the string-nets implies that a string-net
condensed wave function has a non-trivial long distance
structure. It is this long distance structure that distin-
guishes the condensed state from the “normal” state.
In general, we expect that the universal features of a
string-net condensed phase are contained in the long dis-
tance character of the wave functions. Imagine compar-
ing two diﬀerent string-net condensed states that belong
to the same quantum phase. The two states will have
diﬀerent wave functions. However, by the standard RG
reasoning, we expect that the two wave functions will
look the same at long distances. That is, the two wave
functions will only diﬀer in short distance details - like
those shown in Fig. 6.
Continuing with this line of thought, we imagine per-
forming an RG analysis on ground state functions. All
FIG. 6: Three pairs of string-net conﬁgurations that diﬀer
only in their short distance structure. We expect string-ne t
wave functions in the same quantum phase to only diﬀer by
these short distance details.
Φ
Φ
Φ
Φ
a
b
c
d
FIG. 7: A schematic RG ﬂow diagram for a string-net model
with 4 string-net condensed phases a, b, c, and d. All the
states in each phase ﬂow to ﬁxed-points in the long distance
limit. The corresponding ﬁxed-point wave functions Φ a, Φ b,
Φ c, and Φ d capture the universal long distance features of
the associated quantum phases. Our ansatz is that the ﬁxed-
point wave functions Φ are described by local constraints of
the form (4-7).
the states in a string-net condensed phase should ﬂow
to some special “ﬁxed-point” state. We expect that the
wave function of this state captures the universal long
distance features of the whole quantum phase. (See Fig.
7).
In the following, we will construct these special ﬁxed-
point wave functions. Suppose Φ is some ﬁxed-point
wave function. We know that Φ is the ground state of
some ﬁxed-point Hamiltonian H. Based on our experi-
ence with gauge theories, we expect that H is free. That
is, H is a sum of local string kinetic energy terms with
no string tension terms:
H = tHt = t
∑
i
Ht,i
In particular, H is unfrustrated, and the ground state
wave function minimizes the expectation values of all
the kinetic energy terms {Hti} simultaneously. Minimiz-
ing the expectation value of an individual kinetic energy
term Ht,i is equivalent to imposing a local constraint
on the ground state wave function, namely Ht,i |Φ ⟩ =
Ei|Φ ⟩ (where Ei is the smallest eigenvalue of Ht,i ).
We conclude that the wave function Φ can be speciﬁed
uniquely by local constraint equations . The local con-
straints are linear relations between several string-net
amplitudes Φ( X1), Φ( X2), Φ( X3)... where the conﬁgura-
tions X1, X2, X3... only diﬀer by local transformations.
To derive these local constraints from ﬁrst principles
is diﬃcult, so we will use a more heuristic approach. We
will ﬁrst guess the form of the local constraints ( ie guess
the form of the ﬁxed-point wave function). Then, in the
next section, we will construct the ﬁxed-point Hamilto-
nian and show that its ground state wave function does
indeed satisfy these local relations. Our ansatz is that
the local constraints can be put in the following graphi-
cal form:
Φ
(
i
)
=Φ
(
i
)
(4)
Φ
(
i
)
=diΦ
( )
(5)
Φ
(
i l
k
j
)
=δijΦ
(
i l
k
i
)
(6)
Φ
(
mi
j k
l )
=
∑
n
F ijm
kln Φ
(
j
i
n k
l
)
(7)
Here, i, j, k etc. are arbitrary string types and the
shaded regions represent arbitrary string-net conﬁgura-
tions. The di are complex numbers. The 6 index sym-
bol F ijm
kln is a complex numerical constant that depends
on 6 string types i, j, m, k, l, and n. If one or more
of the branchings {i, j, m}, {k, l, m∗}, {i, n, l}, {j, k, n∗} is
illegal, the value of the symbol F ijm
kln is unphysical. How-
ever, for simplicity, we will set F ijm
kln = 0 in this case.
The local rules (4-7) are written using a new nota-
tional convention. According to this convention, the in-
dices i, j, k etc., can take on the value i = 0 in addition
to the N physical string types i = 1 , ...N. We think of
the i = 0 string as the “empty string” or “null string.”
It represents empty space - the vacuum. Thus, we can
convert labeled string-nets to our old convention by sim-
ply erasing all the i = 0 strings. The branching rules and
dualities associated with i = 0 are deﬁned in the obvious
way: 0 ∗ = 0, and {i, j, 0} is allowed if and only if i = j∗.
Our convention serves two purposes: it simpliﬁes nota-
tion (each equation in (4- 7) represents several equations
with the old convention), and it reveals the mathematical
framework underlying string-net condensation.
We now brieﬂy motivate these rules. The ﬁrst rule (4)
constrains the wave function Φ to be topologically invari-
ant. It requires the quantum mechanical amplitude for
a string-net conﬁguration to only depend on the topol-
ogy of the conﬁguration: two conﬁgurations that can be
continuously deformed into one another must have the
same amplitude. The motivation for this constraint is
our expectation that topological string-net phases have
topologically invariant ﬁxed-points.
The second rule (5) is motivated by the fundamental
property of RG ﬁxed-points: scale invariance. The wave
function Φ should look the same at all distance scales.
Since a closed string disappears at length scales larger
then the string size, the amplitude of an arbitrary string-
net conﬁguration with a closed string should be propor-
tional to the amplitude of the string-net conﬁguration
alone.
The third rule (6) is similar. Since a “bubble” is irrel-
evant at long length scales, we expect
Φ
(
i l
k
j
)
∝ Φ
(
i j
)
But if i ⁄= j, the conﬁguration i j is not allowed:
Φ
(
i j
)
= 0. We conclude that the amplitude
for the bubble conﬁguration vanishes when i ⁄= j (6).
The last rule is less well-motivated. The main point
is that the ﬁrst three rules are not complete: another
constraint is needed to specify the ground state wave
function uniquely. The last rule (7) is the simplest lo-
cal constraint with this property. An alternative motiva-
tion for this rule is the fusion algebra in conformal ﬁeld
theory.[45]
The local rules (4-7) uniquely specify the ﬁxed-point
wave function Φ. The universal features of the string-net
condensed state are captured by these rules. Equiva-
lently, they are captured by the six index object F ijm
kln ,
and the numbers di.
However, not every choice of ( F ijm
kln , di) corresponds to
a string-net condensed phase. In fact, a generic choice
of ( F ijm
kln , di) will lead to constraints (4-7) that are not
self-consistent. The only ( F ijm
kln , di) that give rise to self-
consistent rules and a well-deﬁned wave function Φ are
(up to a trivial rescaling) those that satisfy
F ijk
j∗i∗0 = vk
vivj
δijk
F ijm
kln = F lkm∗
jin = F jim
lkn∗ = F imj
k∗nl
vmvn
vj vl
N∑
n=0
F mlq
kp∗nF jip
mns∗ F js∗n
lkr∗ = F jip
q∗kr∗ F riq∗
mls∗ (8)
where vi = vi∗ = √di (and v0 = 1). (See appendix B).
Here, we have introduced a new object δijk deﬁned by
the branching rules:
δijk =
{
1, if {i, j, k} is allowed,
0, otherwise. (9)
There is a one-to-one correspondence between (2+1) D
string-net condensed phases and solutions of (8). These
solutions correspond to mathematical objects known as
tensor categories. [32] Tensor category theory is the fun-
damental mathematical framework for string-net conden-
sation, just as group theory is for particle condensation.
We have just shown that it gives a complete classiﬁca-
tion of (2 + 1) D string-net condensed phases (or equiva-
lently doubled topological phases): each phase is associ-
ated with a diﬀerent solution to (8). We will show later
that it also provides a convenient framework for deriving
the physical properties of quasiparticles.
It is highly non-trivial to ﬁnd solutions of (8). How-
ever, it turns out each group G provides a solution. The
solution is obtained by (a) letting the string-type index i
run over the irreducible representations of the group, (b)
letting the numbers di be the dimensions of the represen-
tations and (c) letting the 6 index object F ijm
kln be the 6 j
symbol of the group. The low energy eﬀective theory of
the corresponding string-net condensed state turns out to
be a deconﬁned gauge theory with gauge group G. An-
other class of solutions can be obtained from 6 j symbols
of quantum groups. It turns out that in these cases, the
low energy eﬀective theories of the corresponding string-
net condensed states are doubled Chern-Simons gauge
theories. These two classes of solutions are not necessar-
ily exhaustive: Eq. (8) may have solutions other then
gauge theories or Chern-Simons theories. Nevertheless,
it is clear that gauge bosons and gauge groups emerge
from string-net condensation in a very natural way.
In fact, string-net condensation provides a new per-
spective on gauge theory. Traditionally, we think of
gauge theories geometrically. The gauge ﬁeld Aµ is anal-
ogous to an aﬃne connection, and the ﬁeld strength Fµν
is essentially a curvature tensor. From this point of view,
gauge theory describes the dynamics of certain geometric
objects (e.g. ﬁber bundles). The gauge group determines
the structure of these objects and is introduced by hand
as part of the basic deﬁnition of the theory. In con-
trast, according to the string-net condensation picture,
the geometrical character of gauge theory is not funda-
mental. Gauge theories are fundamentally theories of
extended objects. The gauge group and the geometrical
gauge structure emerge dynamically at low energies and
long distances. A string-net system “chooses” a particu-
lar gauge group, depending on the coupling constants in
the underlying Hamiltonian: these parameters determine
a string-net condensed phase which in turn determines a
solution to (8). The nature of this solution determines
the gauge group.
One advantage of this alternative picture is that it uni-
ﬁes two seemingly unrelated phenomena: gauge interac-
tions and Fermi statistics. Indeed, as we will show in
section V, string-net condensation naturally gives rise to
both gauge interactions and Fermi statistics (or fractiona l
statistics in (2 + 1) D). In addition, these structures al-
ways appear together. [29]
