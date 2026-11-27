---
doc_id: arxiv-cond-mat-0404617v2
doc_title: "String-net condensation: A physical mechanism for topological phases"
section_id: sec-007-5-string-net-condensation-in-31-and-higher-dimen
section_title: "String-net condensation in $(3+1)$ and higher dimensions"
section_number: 5
pages: 10-12
source_pdf: cond-mat-0404617v2.pdf
source_sha256: 8e31b9ec8ac2e034
toc_source: inferred
doc_brief: "String-net condensation: A physical mechanism for topological phases — 18 sections: Front matter; Introduction; String-nets and gauge theories"
---
AND HIGHER DIMENSIONS
In this section, we generalize our results to (3 + 1) and
higher dimensions. We ﬁnd that there is a one-to-one
correspondence between (3 + 1) (and higher) dimensional
string-net condensates and mathematical objects known
as “symmetric tensor categories.” [32] The low energy
eﬀective theories for these states are gauge theories cou-
pled to bosonic or fermionic charges.
Our approach is based on the exactly soluble lattice
spin Hamiltonian (10). In that model, the spins live on
the links of the honeycomb lattice. However, the choice
of lattice was somewhat arbitrary: we could equally well
have chosen any trivalent lattice in two dimensions.
Trivalent lattices can also be constructed in three and
higher dimensions. For example, we can create a space-
ﬁlling trivalent lattice in three dimensions, by “splittin g”
the sites of the cubic lattice (see Fig. 10). Consider the
spin Hamiltonian (10) for this lattice, where I runs over
all the vertices of the lattice, and p runs over all the
“plaquettes” (that is, the closed loops that correspond
to plaquettes in the original cubic lattice).
This model is a natural candidate for string-net con-
densation in three dimensions. Unfortunately, it turns
out that the Hamiltonian (10) is not exactly soluble on
this lattice. The magnetic ﬂux operators Bs
p do not com-
mute in general.
This lack of commutativity originates from two diﬀer-
ences between the plaquettes in the honeycomb lattice
and in higher dimensional trivalent lattices. The ﬁrst
diﬀerence is that in the honeycomb lattice, neighboring
plaquettes always share precisely two vertices, while in
higher dimensions the boundary between plaquettes can
contain three or more vertices (see Fig. 11). The exis-
tence of these interior vertices has the following conse-
quence. Imagine we choose orientation conventions for
each vertex, so that we have a notion of “left turns” and
“right turns” for oriented paths on our lattice (such an
orientation convention can be obtained by projecting the
3D lattice onto a 2 D plane - as in Fig. 11). Then, no
matter how we assign these orientations the plaquette
boundaries will always make both left and right turns.
Thus, we cannot regard the boundaries of the 3 D pla-
quettes as small closed strings the way we did in two
dimensions (since small closed strings always make all
left turns, or all right turns). But the magnetic ﬂux op-
erators Bs
p only commute if their boundaries are small
closed strings. It is this inconsistency between the alge-
braic deﬁnition of Bs
p and the topology of the plaquettes
that leads to the lack of commutativity.
To resolve this problem, we need to deﬁne a Hamil-
tonian using the general simple string operators W (∂p)
rather then the small closed strings Bs
p. Suppose
(ωi
sj, ¯ωi
sj), s = 0 , 1, ...N are type- s solutions of (18). Af-
ter picking some “left turn”, “right turn” orientation con-
vention at each vertex, we can deﬁne the corresponding
type-s simple string operators Ws(P ) as in (15). Sup-
pose, in addition, that we choose ( ωi
sj, ¯ωi
sj) so that the
string operators satisfy Wr ·Ws =∑
t δrstWt (this prop-
erty ensures that Ws(∂p) are analogous to Bs
p). Then, a
natural higher dimensional generalization of the Hamil-
tonian (10) is
H = −
∑
I
QI −
∑
p
Wp, W p =
N∑
s=0
asWs(∂p) (31)
For a two dimensional lattice, the conditions (18) are suf-
ﬁcient to guarantee that the Hamiltonian (31) is an ex-
actly soluble realization of a doubled topological phase.
(This is because the plaquette boundaries ∂p are not
linked and hence the Ws(∂p) all commute). However,
in higher dimensions, one additional constraint is neces-
sary.
This constraint stems from the second, and perhaps
more fundamental, diﬀerence between 2 D and higher di-
mensional lattices. In two dimensions, two closed curves
always intersect an even number of times. For higher
dimensional lattices, this is not the case. Small closed
curves, in particular plaquette boundaries, can (in a
sense) intersect exactly once (see Fig. 11). Because of
this, the objects ωi
jk must satisfy the additional relation:
ωi
jk = ¯ωi
kj (32)
One can show that if this additional constraint is satis-
ﬁed, then (a) the higher dimensional Hamiltonian (31)
is exactly soluble, and (b) the ground state wave func-
tion Φ is deﬁned by local topological rules analogous to
(4-7). This means that (31) provides an exactly soluble
realization of topological phases in (3 + 1) and higher
dimensions.
x
y
z
I
I1
I2
3I4
p
p
p
1
2
3
FIG. 11: Three plaquettes demonstrating the two fundamen-
tal diﬀerences between higher dimensional trivalent latti ces
and the honeycomb lattice. The plaquettes p1, p2 lie in the
xz plane, while p3 is oriented in the xy direction. Notice that
p1 and p2 share three vertices, I1, I2, I3. Also, notice that
the plaquette boundaries ∂ p1 and ∂ p3 intersect only at the
line segment I3I4. The boundary ∂ p1 makes a left turn at
I3, and a right turn at I4. Thus, viewed from far away, these
two plaquette boundaries intersect exactly once (unlike th e
pair ∂ p1 and ∂ p2).
Each exactly soluble Hamiltonian is associated with
a solution ( F ijm
kln , ωi
jk, ¯ωi
jk) of (8), (18), (32). By analogy
with the two dimensional case, we conjecture that there is
a one-to-one correspondence between topological string-
net condensed phases in (3 + 1) or higher dimensions,
and these solutions. The solutions ( F ijm
kln , ωi
jk , ¯ωi
jk) cor-
respond to a special class of tensor categories - symmet-
ric tensor categories. [32] Thus, just as tensor categories
are the mathematical objects underlying string conden-
sation in (2 + 1) dimensions, symmetric tensor categories
are fundamental to string condensation in higher dimen-
sions.
There are relatively few solutions to (8), (18), (32).
Physically, this is a consequence of the restrictions on
quasiparticle statistics in 3 or higher dimensions. Un-
like in two dimensions, higher dimensional quasiparticles
necessarily have trivial mutual statistics, and must be ei-
ther bosonic or fermionic. From a more mathematical
point of view, the scarcity of solutions is a result of the
symmetry condition (32). Doubled topological phases,
such as Chern-Simons theories, typically fail to satisfy
this condition.
However, gauge theories do satisfy the symmetry con-
dition (32) and therefore do correspond to higher dimen-
sional string-net condensates. Recall that the gauge the-
ory solution to (8) is obtained by (a) letting the string-
type index i run over the irreducible representations of
the gauge group, (b) letting the numbers di be the dimen-
sions of the representations, and (c) letting the 6 index
object F ijm
kln be the 6 j symbol of the group. One can
check that this also provides a solution to (18), (32), if
we set ωi
jk
vj vk
vi
= −1 when j = k and the invariant ten-
sor in k ⊗ k ⊗ i∗ is antisymmetric in the ﬁrst two indices,
and ωi
jk
vj vk
vi
= 1 otherwise. This result is to be expected,
since the string-net picture of gauge theory (section II)
is valid in any number of dimensions. Thus, it is not
surprising that gauge theories can emerge from higher
dimensional string-net condensation.
There is another class of higher dimensional string-
net condensed phases that is more interesting. The low
energy eﬀective theories for these phases are variants of
gauge theories. Mathematically, they are obtained by
twisting the usual gauge theory solution by
˜ωi
jk = ωi
jk ·(−1)P (j)P (k) (33)
Here P (i) is some assignment of parity (“even”, or “odd”)
to each representation i. The assignment must be self-
consistent in the sense that the tensor product of two
representations with the same (diﬀerent) parity, decom-
poses into purely even (odd) representations. If all the
representations are assigned an even parity - that is P (i)
is trivial - then the twisted gauge theory reduces to stan-
dard gauge theory.
The major physical distinction between twisted gauge
theories and standard gauge theories is the quasiparti-
cle spectrum. In standard gauge theory, the fundamen-
tal quasiparticles are the electric charges created by the
N + 1 string operators Wi. These quasiparticles are all
bosonic. In contrast, in twisted gauge theories, all the
quasiparticles corresponding to “odd” representations i
are fermionic.
In this way, higher dimensional string-net condensa-
tion naturally gives rise to both emerging gauge bosons
and emerging fermions. This feature suggests that gauge
interactions and Fermi statistics may be intimately con-
nected. The string-net picture may be the bridge between
these two seemingly unrelated phenomena. [29]
In fact, it appears that gauge theories coupled to
fermionic or bosonic charged particles are the only pos-
sibilities for higher dimensional string-net condensates :
mathematical work on symmetric tensor categories sug-
gests that the only solutions to (8), (18), (32) are those
corresponding to gauge theories and twisted gauge theo-
ries. [48]
We would like to point out that (3 + 1) dimensional
string-net condensed states also exhibit membrane con-
densation. These membrane operators are entirely anal-
ogous to the string operators. Just as open string oper-
ators create charges at their two ends, open membrane
operators create magnetic ﬂux loops along their bound-
aries. Furthermore, just as string condensation makes the
string unobservable, membrane condensation leads to the
unobservability of the membrane. Only the boundary of
the membrane - the magnetic ﬂux loop - is observable.
