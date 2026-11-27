---
doc_id: arxiv-cond-mat-0404617v2
doc_title: "String-net condensation: A physical mechanism for topological phases"
section_id: sec-006-43-quasiparticle-excitations
section_title: "Quasiparticle excitations"
section_number: 4.3
pages: 8-10
source_pdf: cond-mat-0404617v2.pdf
source_sha256: 8e31b9ec8ac2e034
toc_source: inferred
doc_brief: "String-net condensation: A physical mechanism for topological phases — 18 sections: Front matter; Introduction; String-nets and gauge theories"
---
In this section, we ﬁnd the quasiparticle excitations
of the string-net Hamiltonian (10), and calculate their
statistics (e.g. the twists θα and the S matrix sαβ ). We
will only consider the topological phase with smooth con-
tinuum limit. That is, we will choose as = ds∑ N
i=0 d2
i
in our
lattice model.
Recall that the ground state satisﬁes QI = Bp = 1 for
all vertices I, and all plaquettes p. The quasiparticle ex-
citations correspond to violations of these constraints fo r
some local collection of vertices and plaquettes. We are
interested in the topological properties (e.g. statistics ) of
these excitations.
We will focus on topologically nontrivial quasiparticles
- that is, particles with nontrivial statistics or mutual
statistics. By the analysis in Ref. [29], we know that these
types of particles are always created in pairs, and that
their pair creation operator has a string-like structure,
with the newly created particles appearing at the ends.
(See Fig. 9). The position of this string operator is
unobservable in the string-net condensed state - only the
endpoints of the string are observable. Thus the two ends
of the string behave like independent particles.
If the two endpoints of the string coincide so that the
string forms a loop, then the associated closed string
operator commutes with the Hamiltonian. This follows
from the fact that the string is truly unobservable; the
action of an open string operator on the ground state
depends only on its endpoints.
Thus, each topologically nontrivial quasiparticle is as-
sociated with a (closed) string operator that commutes
with the Hamiltonian . To ﬁnd the quasiparticles, we need
to ﬁnd these closed string operators.
An important class of string operators are what we
will call “simple” string operators. The deﬁning property
of simple string operators is their action on the vacuum
state. If we apply a type- s simple string operator W (P )
to the vacuum state, it creates a type- s string along the
path of the string, P . We already have some examples of
these operators, namely the magnetic ﬂux operators Bs
p.
When Bs
p acts on the vacuum conﬁguration |0⟩, it creates
a type- s string along the boundary of the plaquette p.
Thus, we can think of Bs
p as a short type- s simple string
operator, W (∂p).
We would like to construct simple string operators
W (P ) for arbitrary paths P = I1, ..., IN on the hon-
eycomb lattice. Using the deﬁnition of Bs
p as a guide, we
make the following ansatz. The string operator W (P )
only changes the spin states along the path P . The ma-
trix element of a general type- s simple string operator
W (P ) between an initial spin state i1, ...iN and ﬁnal spin
state i′
1, ...i′
N is of the form
W i′
1i′
2...i ′
N
i1i2...i N (e1e2...eN ) =
( N∏
k=1
F s
k
)( N∏
k=1
ωk
)
(15)
where e1, ..., eN are the spin states of the N “legs” of P
(see Fig. 9) and
F s
k =



F eki∗
kik−1
s∗i′
k−1i′∗
k
, if P turns left at Ik
F
eki∗
k−1ik
si′
ki′∗
k−1
, if P turns right at Ik
(16)
ωk =



vik vs
vi′
k
ωi′
k
ik , if P turns right, left at Ik, Ik+1
vik vs
vi′
k
¯ωi′
k
ik , if P turns left, right at Ik, Ik+1
1, otherwise
(17)
Here, ωi
j, ¯ωi
j are two (complex) two index objects that
characterize the string W .
Note the similarity to the deﬁnition of Bs
p. The major
diﬀerence is the additional factor ∏ N
k=1 ωk. We conjec-
ture that |ωj
i
vivs
vj
| = 1 for a type- s string, so ∏ N
k=1 ωk
is simply a phase factor that depends on the initial and
ﬁnal spin states i1, i2, ..., iN , i′
1, i′
2, ..., i′
N . This phase
vanishes for paths P that make only left or only right
turns, such as plaquette boundaries ∂p. In that case, the
deﬁnition of W (P ) coincides with Bs
p.
A straightforward calculation shows that the opera-
tor W (P ) deﬁned above commutes with the Hamiltonian
(10) if ωi
j, ¯ωi
j satisfy
¯ωm
j F sl∗i
kjm∗ ωl
i
vj vs
vm
=
N∑
n=0
F ji∗k
s∗nl∗ ωn
k F jl∗n
ksm∗
¯ωj
i =
N∑
k=0
ωk
i∗ F is∗k
i∗sj∗ (18)
The solutions to these equations give all the type- s simple
string operators.
For example, consider the case of Abelian gauge the-
ory. In this case, the solutions to (18) can be divided
into three classes. The ﬁrst class is given by s ⁄= 0,
ωj
i
vivs
vj
= ¯ωj
i
vivs
vj
= 1. These string operators create
electric ﬂux lines and the associated quasiparticles are
electric charges. In more traditional nomenclature, these
are known as (Wegner-)Wilson loop operators [39, 46].
The second class of solutions is given by s = 0, and
ωj
i
vivs
vj
= (¯ωj
i
vivs
vj
)∗ ⁄= 1. These string operators cre-
ate magnetic ﬂux lines and the associated quasiparti-
cles are magnetic ﬂuxes. The third class has s ⁄= 0 and
ωj
i
vivs
vj
= (¯ωj
i
vivs
vj
)∗ ⁄= 1. These strings create both elec-
tric and magnetic ﬂux and the associated quasiparticles
are electric charge/magnetic ﬂux bound states. This ac-
counts for all the quasiparticles in (2+1) D Abelian gauge
theory. Therefore, all the string operators are simple in
this case.
However, this is not true for non-Abelian gauge the-
ory or other (2 + 1) D topological phases. To compute
the quasiparticle spectrum of these more general theo-
ries, we need to generalize the expression (15) for W (P )
to include string operators that are not simple.
One way to guess the more general expression for
W (P ) is to consider products of simple string operators.
Clearly, if W1(P ) and W2(P ) commute with the Hamil-
tonian, then W (P ) = W1(P )·W2(P ) also commutes with
the Hamiltonian. Thus, we can obtain other string oper-
ators by taking products of simple string operators. In
general, the resulting operators are not simple. If W1 and
W2 are type-s1 and type-s2 simple string operators, then
the action of the product string on the vacuum state is:
W (P )|0⟩= W1(P )W2(P )|0⟩= W1(P )|s2⟩=
∑
s
δss1s2 |s⟩
where |s⟩ denotes the string state with a type- s string
along the path P and the vacuum everywhere else. If we
take products of more then two simple string operators
then the action of the product string on the vacuum is
of the form W (P )|0⟩=∑
s ns|s⟩where ns are some non-
negative integers.
We now generalize the expression for W (P ) so that it
includes arbitrary products of simple strings. Let W be
a product of simple string operators, and let ns be the
non-negative integers characterizing the action of W on
the vacuum: W (P )|0⟩=∑
s ns|s⟩. Then, one can show
that the matrix elements of W (P ) are always of the form
W i′
1i′
2...i ′
N
i1i2...i N (e1e2...eN ) =
∑
{sk}
( N∏
k=1
F sk
k
)
Tr
( N∏
k=1
Ω sk
k
)
(19)
where
Ω sk
k =



vik vsk
vi′
k
Ω i′
k
sksk+1ik , if P turns right, left at Ik, Ik+1
vik vsk
vi′
k
¯Ω i′
k
sksk+1ik , if P turns left, right at Ik, Ik+1
δsksk+1 ·Id, otherwise
(20)
and Ω i
stj, ¯Ω i
stj are two 4 index objects that characterize
the string operator W . For any quadruple of string types
i, j, s, t, (Ω i
stj, ¯Ω i
stj) are (complex) rectangular matrices
of dimension ns × nt. Note that type- s0 simple string
operators correspond to the special case where ns = δs0s.
In this case, the matrices Ω i
stj, ¯Ω i
stj reduce to complex
numbers, and we can identify
Ω i
stj = ωi
jδss0 δts0 , ¯Ω i
stj = ¯ωi
jδss0 δts0 . (21)
As we mentioned above, products of simple string op-
erators are always of the form (19). In fact, we be-
lieve that all string operators are of this form. Thus,
we will use (19) as an ansatz for general string operators
in (2 + 1) D topological phases. This ansatz is compli-
cated algebraically, but like the deﬁnition of Bs
p, it has a
simple graphical interpretation (see appendix D).
A straightforward calculation shows that the closed
string W (P ) commutes with the Hamiltonian (10) if Ω
3
W(P)
i23
14
2
1
I
II
I 1
23
4
i i
e e
e e
FIG. 9: Open and closed string operators for the lattice
spin model (10). Open string operators create quasiparti-
cles at the two ends, as shown on the left. Closed string
operators, as shown on the right, commute with the Hamil-
tonian. The closed string operator W (P ) only acts non-
trivially on the spins along the path P = I1, I2... (thick
line), but its action depends on the spin states on the
legs (thin lines). The matrix element between an initial
state i1, i 2, ... and a ﬁnal state i′
1, i ′
2, ... is W
i′
1i′
2...
i1i2... (e1e2... ) =
(F
e2i∗
2 i1
s∗i′
1i′∗
2
F
e3i∗
3 i2
s∗i′
2i′∗
3
... ) ·(
vi1 vs1
vi′
1
ω
i′
1
i1
vi3 vs3
vi′
3
¯ω
i′
3
i3 ... ) for a type- s sim-
ple string and W
i′
1i′
2...
i1i2... (e1e2... ) = ∑
{sk }(F
e2i∗
2 i1
s∗
2 i′
1i′∗
2
F
e3i∗
3 i2
s∗
3 i′
2i′∗
3
... ) ·
Tr(
vi1 vs1
vi′
1
Ω
i′
1
s1s2i1 δ s2s3 Id
vi3 vs3
vi′
3
¯Ω
i′
3
s3s4i3 ... ) for a general string.
and ¯Ω satisfy
N∑
s=0
¯Ω m
rsj F sl∗i
kjm∗ Ω l
sti
vjvs
vm
=
N∑
n=0
F ji∗k
t∗nl∗ Ω n
rtkF jl∗n
krm∗
¯Ω j
sti =
N∑
k=0
Ω k
sti∗ F it∗k
i∗sj∗ (22)
The solutions (Ω m, ¯Ω m) to these equations give all the
diﬀerent closed string operators Wm. However, not all
of these solutions are really distinct. Notice that two
solutions (Ω 1, ¯Ω 1), (Ω 2, ¯Ω 2) can be combined to form a
new solution (Ω ′, ¯Ω ′):
Ω ′j
sti = Ω j
1,sti ⊕ Ω j
2,sti
¯Ω ′j
sti = ¯Ω j
1,sti ⊕ ¯Ω j
2,sti (23)
This is not surprising: the string operator W ′ corre-
sponding to (Ω ′, ¯Ω ′) is simply the sum of the two op-
erators corresponding to (Ω 1, 2, ¯Ω 1, 2): W ′ = W1 + W2.
Given this additivity property, it is natural to con-
sider the “irreducible” solutions (Ω α , ¯Ω α ) that cannot be
written as a sum of two other solutions. Only the “ir-
reducible” string operators Wα create quasiparticle-pairs
in the usual sense. Reducible string operators W create
superpositions of diﬀerent strings - which correspond to
superpositions of diﬀerent quasiparticles. [51]
To analyze a topological phase, one only needs to ﬁnd
the irreducible solutions (Ω α , ¯Ω α ) to (22). The number
M of such solutions is always ﬁnite. In general, each so-
lution corresponds to an irreducible representation of an
algebraic object. In the case of lattice gauge theory, there
is one solution for every irreducible representation of the
quantum double D(G) of the gauge group G. Similarly,
in the case of doubled Chern-Simons theories there is one
solution for each irreducible representation of a doubled
quantum group.
The structure of these irreducible string operators Wα
determines all the universal features of the topological
phase. The number M of irreducible string operators is
the number of diﬀerent kinds of quasiparticles. The fu-
sion rules Wα Wβ =∑ M
γ =1 hγ
αβ Wγ determine how bound
states of type- α and type- β quasiparticles can be viewed
as a superposition of other types of quasiparticles.
The topological properties of the quasiparticles are also
easy to compute. As an example, we now derive two par-
ticularly fundamental objects that characterize the spins
and statistics of quasiparticles: the M twists θα and the
M × M S-matrix, sαβ [13, 25, 35, 47].
The twists θα are deﬁned to be statistical angles of
the type- α quasiparticles. By the spin-statistics theo-
rem they are closely connected to the quasiparticle spins
sα : eiθ α = e2πis α . We can calculate θα by comparing the
quantum mechanical amplitude for the following two pro-
cesses. In the ﬁrst process, we create a pair of quasipar-
ticles α, ¯α (from the ground state), exchange them, and
then annihilate the pair. In the second process, we create
and then annihilate the pair without any exchange. The
ratio of the amplitudes for these two processes is precisely
eiθ α .
The amplitude for each process is given by the expec-
tation value of the closed string operator Wα for a par-
ticular path P :
A1 =
⟨
Φ
⏐⏐⏐ α
⏐⏐⏐Φ
⟩
(24)
A2 =
⟨
Φ
⏐⏐⏐ α
⏐⏐⏐Φ
⟩
(25)
Here, |Φ ⟩ denotes the ground state of the Hamiltonian
(10).
Let (Ω α , ¯Ω α , nα ) be the irreducible solution corre-
sponding to the string operator Wα . The above
two amplitudes can be then be expressed in terms of
(Ω α , ¯Ω α , nα ) (see appendix D):
A1 =
∑
s
d2
s ·Tr(Ω 0
α,sss ∗ ) (26)
A2 =
∑
s
nα,s ds (27)
Combining these results, we ﬁnd that the twists are given
by
eiθ α = A1
A2
=
∑
s d2
s ·Tr(Ω 0
α,sss ∗ )∑
s nα,s ds
(28)
Just as the twists θα are related to the spin and statis-
tics of individual particle types α, the elements of the
S-matrix, sαβ describe the mutual statistics of two parti-
cle types α, β. Consider the following process: We create
two pairs of quasiparticles α, ¯α, β, ¯β, braid α around β,
and then annihilate the two pairs. The element sαβ is
FIG. 10: A three dimensional trivalent lattice, obtained by
splitting the sites of the cubic lattice. We replace each ver tex
of the cubic lattice with 4 other vertices as shown above.
deﬁned to be the quantum mechanical amplitude A of
this process, divided by a proportionality factor D where
D2 = ∑
α (∑
s nα,s ds)2. The amplitude A can be cal-
culated from the expectation value of Wα , Wβ for two
“linked” paths P :
A =
⟨
Φ
⏐⏐⏐
αβ ⏐⏐⏐Φ
⟩
(29)
Expressing A in terms of (Ω α , ¯Ω α , nα ), we ﬁnd
sαβ = A
D = 1
D
∑
ijk
Tr(Ω k
α,iij ∗ ) ·Tr(Ω k∗
β,jji ∗ )didj (30)
