---
doc_id: arxiv-cond-mat-0404617v2
doc_title: "String-net condensation: A physical mechanism for topological phases"
section_id: sec-015-c-graphical-representation-of-the-hamiltonian
section_title: "Graphical representation of the Hamiltonian"
section_number: C
pages: 18-20
source_pdf: cond-mat-0404617v2.pdf
source_sha256: 8e31b9ec8ac2e034
toc_source: inferred
doc_brief: "String-net condensation: A physical mechanism for topological phases — 18 sections: Front matter; Introduction; String-nets and gauge theories"
---
OF THE HAMIL TONIAN
In this section, we provide an alternative, graphical,
representation of the lattice model (10). This graphical
representation provides a simple visual technique for un-
derstanding properties (a)-(c) of the Hamiltonian (10).
We begin with the 2 D honeycomb lattice. Imagine we
fatten the links of the lattice into stripes of ﬁnite width
(see Fig. 16). Then, any string-net state in the fat-
tened honeycomb lattice (Fig. 16a) can be viewed as a
superposition of string-net states in the original, unfat-
tened lattice (Fig. 16b). This mapping is obtained via
the local rules (4-7). Using these rules, we can relate the
amplitude Φ( X) for a string-net in the fattened lattice to
a linear combination of string-net amplitudes in the orig-
inal lattice: Φ( X) =∑ aiΦ( Xi). This provides a natural
linear relation between the states in the fattened lattice
and those in the unfattened lattice: |X⟩ = ∑ ai|Xi⟩.
This linear relation is independent of the particular way
in which the local rules (4-7) are applied, as long as the
rules are self-consistent.
In this way, the fattened honeycomb lattice provides
an alternative notation for representing the states in the
Hilbert space of (10). This notation is useful because
the magnetic energy operators Bs
p are simple in this rep-
resentation. Indeed, the action of the operator Bs
p on
the string-net state
⏐⏐⏐a
g
b h c
i
d
j
ekf
l
⟩
is equivalent to simply
adding a loop of type- s string:
Bs
p
⏐⏐⏐a
g
b h c
i
d
j
ekf
l
⟩
=
⏐⏐⏐a
g
b h c
i
d
j
ekf
l
s
⟩
As we described above, we can use the local rules (4-7)
to rewrite
⏐⏐⏐a
g
b h c
i
d
j
ekf
l
s
⟩
as a linear combination of the
physical string-net states with strings only on the links,
that is to reduce Fig. 17a to Fig. 17b. This allows us to
obtain the matrix elements of Bs
p.
The following is a particular way to implement the
above procedure:
Bs
p
⏐⏐⏐a
g
b h c
i
d
j
ekf
l
⟩
=
⏐⏐⏐
f k e
j
d
i
chb
g
a
l
s
⟩
=
∑
g′h′i′j′k′l′
F gg∗0
s∗sg′∗ F hh∗0
s∗sh′∗ F ii∗0
s∗si′∗ F jj ∗0
s∗sj′∗ F kk∗0
s∗sk′∗ F ll∗0
s∗sl′∗
⏐⏐⏐
f k k’k e
ii’ihh’h
l’
a
b c
d
s
s
s s
s
s
g
g
g’
l
l
j’j
j
⟩
=
∑
g′h′i′j′k′l′
F gg∗0
s∗sg′∗ F hh∗0
s∗sh′∗ F ii∗0
s∗si′∗ F jj ∗ 0
s∗sj′∗ F kk∗0
s∗sk′∗ F ll∗0
s∗sl′∗ F bg∗h
s∗h′g′∗F ch∗i
s∗i′h′∗F di∗j
s∗j′i′∗ F ej∗k
s∗k′j′∗ F f k∗l
s∗l′k′∗ F al∗g
s∗g′l′∗
⏐⏐⏐
f e
a
b c
d
s s
s
ss
sg’
g
h’h
i’
i’
j’
j’l
k
i
g’ h’
j
k’k’
l’
l’
⟩
=
∑
g′h′i′j′k′l′
F bg∗h
s∗h′g′∗ F ch∗i
s∗i′h′∗F di∗j
s∗j′i′∗ F ej∗k
s∗k′j′∗ F f k∗l
s∗l′k′∗F al∗g
s∗g′l′∗
⏐⏐⏐a
b h’ c
i’
d
j’
ek’f
l’
g’ ⟩
(C1)
Notice that (C1) is exactly (13). Thus, the graphical
representation of Bs
p agrees with the original algebraic
deﬁnition.
Using the graphical representation of Bs
p we can eas-
ily show that Bs1
p1 and Bs2
p2 commute. The derivation
is much simpler then the more straightforward algebraic
calculation. First note that these operators will commute
if p1, p2 are well-separated. Thus, we only have to con-
sider the case where p1 and p2 are adjacent, or the case
where p1, p2 coincide. We begin with the nearest neigh-
(a)
a
b c
d
ef
g’ i’
j’
k’
l’
h’
(b)
a
g
b h c
i
d
j
ek
l
f
s
FIG. 17: The action of Bs
p is equivalent to adding a loop of
type-s string. The resulting string-net state (a) is actually
a linear combination of the string-net states (b). The coef-
ﬁcients in this linear relation can be obtained by using the
local rules (4-7) to reduce (a) to (b).
bor case. The action of Bs1
p1 Bs2
p2 on the string-net state
Fig. 18a can be represented as Fig. 18b. Fig. 18b can
then be related to a linear combination of the string-net
states shown in Fig. 18c. The coeﬃcients in this relation
are the matrix elements of Bs1
p1
Bs2
p2
. But by the same ar-
gument, the action of Bs2
p2
Bs1
p1
can also be represented by
Fig. 18b. We conclude that Bs2
p2
Bs1
p1
, Bs1
p1
Bs2
p2
have the
same matrix elements. Thus, the two operators commute
in this case.
On the other hand, when p1 = p2, we have
Bs2
p Bs1
p
⏐⏐⏐
⟩
=
⏐⏐⏐
s2
s1
⟩
=
∑
k
F s1s∗
1 0
s∗
2 s2k∗
⏐⏐⏐ s
s
1
2
k
⟩
=
∑
k
F s1s∗
1 0
s∗
2 s2k∗ F k∗s2s1
s∗
2 k0 ds∗
2
⏐⏐⏐ k
⟩
=
∑
k
δk∗s2s1
⏐⏐⏐ k
⟩
(C2)
Thus,
Bs2
p Bs1
p =
∑
k
δk∗s2s1 Bk
p. (C3)
Since δk∗s2s1 is symmetric in s2, s1, we conclude that
Bs1
p Bs2
p = Bs2
p Bs1
p , so the operators commute in this case
as well. This establishes property (a) of the Hamiltonian
(10).
Equation (C3) also sheds light on the spectrum of the
Bs
p operators. Let the simultaneous eigenvalues of Bs
p
(with p ﬁxed) be {bs
q}. Then, by (C3) these eigenvalues
satisfy
∑
k
δk∗s2s1 bk
q = bs2
q bs1
q
We can view this as an eigenvalue equation for the ( N +
1) × (N + 1) matrix Ms2 , deﬁned by M i
s2,j = δj∗s2i. The
b c
d
e
g f
h
a
b c
d
e
k
o
g f
q p
r m
n
lji
h
a
ts s 2
b c
d
e
k
o
g f
q p
r m
n
lji
h
a
t
(a) (b) (c)
i’ j’ k’ l’
m’
n’o’p’q’
r’ t’1
FIG. 18: The action of Bs1
p1 Bs2
p2 on the string-net state (a)
can be represented by adding two loops of type- s1 and type-
s2 strings as shown in (b). The string-net state (b) is a linear
combination of the string-net states (c). The coeﬃcients ar e
obtained by using (4 -7) to reduce (b) to (c).
simultaneous eigenvalues bs2
q are simply the simultaneous
eigenvalues of the matrices Ms2 . In particular, this means
that the index q ranges over a set of size N + 1.
Each value of q corresponds to a diﬀerent possible state
for the plaquette p. The magnetic energies of these N +1
diﬀerent states are given by: Eq = −∑
s asbs
q. Depend-
ing on the parameter choice as, all on the plaquettes p
will be in one of these states q. In this way, the Hamilto-
nian (10) can be in N + 1 diﬀerent quantum phase. This
establishes property (b) of the Hamiltonian (10).
One particular state q is particularly interesting. This
state corresponds to the simultaneous eigenvalues bs =
ds. It is not hard to show that the parameter choice
as = ds∑
k d2
k
makes this state energetically favorable. In
fact, using (C3) one can show that Bp is a projector for
this parameter choice, and that Bp = 1 for this state.
Furthermore, the ground state wave function for this
parameter choice obeys the local rules (4-7). One way
to see this is to compare Bp
⏐⏐⏐i i
⟩
with Bp
⏐⏐⏐i i
⟩
.
For the ﬁrst state, we ﬁnd
Bp
⏐⏐⏐i i
⟩
=
∑
s
as
⏐⏐⏐i i s
⟩
=
∑
j,s
ds∑
k d2
k
F ii∗0
s∗sj∗
⏐⏐⏐i i
s
j ⟩
=
∑
j,s
vjvs
vi
∑
k d2
k
⏐⏐⏐i i
s
j ⟩
For the second state, we ﬁnd the same result:
Bp
⏐⏐⏐i i
⟩
=
∑
j,s
vjvs
vi
∑
k d2
k
⏐⏐⏐i i
s
j
⟩
It follows that
0 =
⟨
i i
⏐⏐⏐Bp
⏐⏐⏐Φ
⟩
−
⟨
i i
⏐⏐⏐Bp
⏐⏐⏐Φ
⟩
=
⟨
i i
⏐⏐⏐Φ
⟩
−
⟨
i i
⏐⏐⏐Φ
⟩
so
Φ
(
i i
)
= Φ
(
i i
)
This result means that the strings can be moved through
the forbidden regions at the center of the hexagons.
α
FIG. 19: The action of the string operator Wα (P ) is equiva-
lent to adding a type- α string along the path P . The result-
ing string-net state can be reduced to a linear combination o f
states on the honeycomb lattice, using the local rules (4-7) ,
(D1).
Thus, the local rules which were originally restricted to
the fattened honeycomb lattice can be extended through-
out the entire 2D plane. The wave function Φ obeys these
continuum local rules and has a smooth continuum limit.
We call such a state smooth topological state. This es-
tablishes property (c) of the Hamiltonian (10).
The wave functions of some smooth topological states
are positive deﬁnite. So those wave functions can be
viewed as the statistical weights of certain statistical
models in the same spatial dimensions. What is inter-
esting is that those statistical models are local models
with short-ranged interactions [10, 35, 36].
