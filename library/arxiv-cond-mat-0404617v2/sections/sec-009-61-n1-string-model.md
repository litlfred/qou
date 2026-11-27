---
doc_id: arxiv-cond-mat-0404617v2
doc_title: "String-net condensation: A physical mechanism for topological phases"
section_id: sec-009-61-n1-string-model
section_title: "$N=1$ string model"
section_number: 6.1
pages: 12-14
source_pdf: cond-mat-0404617v2.pdf
source_sha256: 8e31b9ec8ac2e034
toc_source: inferred
doc_brief: "String-net condensation: A physical mechanism for topological phases — 18 sections: Front matter; Introduction; String-nets and gauge theories"
---
We begin with the simplest string-net model. In the
notation from section III, this model is given by
1. Number of string types: N = 1
2. Branching rules: ∅ (no branching)
3. String orientations: 1 ∗ = 1.
In other words, the string-nets in this model contain one
unoriented string type and have no branching. Thus,
they are simply closed loops. (See Fig. 3a).
We would like to ﬁnd the diﬀerent topological phases
that can emerge from these closed loops. According to
the discussion in section IV, each phase is captured by
a ﬁxed-point wave function, and each ﬁxed-point wave
function is speciﬁed by local rules (4-7) that satisfy the
self-consistency relations (8). It turns out that (8) have
only two solutions in this case (up to rescaling):
d0 = 1
d1 = F 110
110 = ±1
F 000
000 = F 101
101 = F 011
011 = 1
F 000
111 = F 110
001 = F 101
010 = F 011
100 = 1 (34)
where the other elements of F all vanish. The corre-
sponding local rules (4-7) are:
Φ
( )
= ± Φ
( )
Φ
( )
= ± Φ
( )
(35)
We have omitted those rules that can be derived from
topological invariance (4).
The ﬁxed-point wave functions Φ ± satisfying these
rules are given by
Φ ±(X) = ( ±1)Xc (36)
where Xc is the number of disconnected components in
the string conﬁguration X.
The two ﬁxed-point wave functions Φ ± correspond
to two simple topological phases. As we will see, Φ +
corresponds to Z2 gauge theory, while Φ − is a U (1) ×
U (1) Chern-Simons theory. (Actually, other topological
phases can emerge from closed loops - such as in Ref. [42–
44]. However, we regard these phases as emerging from
more complicated string-nets. The closed loops organize
into these eﬀective string-nets in the infrared limit).
The exactly soluble models (10) realizing these two
phases can be written as spin 1 /2 systems with one spin
on each link of the honeycomb lattice (see Fig. 12). We
regard a link with σx = −1 as being occupied by a type-1
string, and the state σx = +1 as being unoccupied (or
equivalently, occupied by a type-0 or null string). The
Hamiltonians for the two phases are of the form
H± = −
∑
I
QI, ± −
∑
p
Bp, ±
The electric charge term is the same for both phases
(since it only depends on the branching rules):
QI, ± = 1
2 (1 +
∏
legs of I
σx
i ) (37)
σ x
σ x σ x
σ z
σ z
σ z
σ zσ z
σ z
σ x σ x
σ x
σ x
σ x
σ x
x
xx
x
x
x
p
I
f(    )
f(    )
f(    )
f(    )
f(    )
f(    )
σ   =−1
σ   =−1σ   =−1
σ   =−1
σ   =−1
σ   =−1
FIG. 12: The Hamiltonians (39), (40), realizing the two N = 1
string-condensed phases. Each circle denotes a spin-1/2 sp in.
The links with σ x = − 1 are thought of as being occupied by
a type-1 string, while the links with σ x = +1 are regarded as
empty. The electric charge term acts on the three legs of the
vertex I with σ x. The magnetic energy term acts on the 6
edges of the plaquette p with σ z, and acts on the 6 legs of p
with an operator of the form f (σ x). For the Z2 phase, f = 1,
while for the Chern-Simons phase, f (x) = i(1−x)/ 2.
The magnetic terms for the two phases are
Bp, ± = 1
2 (B0
p, ± ± B1
p, ±) (38)
= 1
2

1 ±
∏
edges of p
σz
j ·
∏
legs of p
(
√
±1)
1−σ x
j
2

 Pp
where Pp is the projection operator Pp =∏
I∈p QI . The
projection operator Pp can be omitted without aﬀecting
the physics (or the exact solubility of the Hamiltonian).
We have included it only to be consistent with (10). If
we omit this term, the Hamiltonian for the ﬁrst phase
(Φ +) reduces to the usual exactly soluble Hamiltonian of
Z2 lattice gauge theory (neglecting numerical factors):
H+ = −
∑
I
∏
legs of I
σx
i −
∑
p
∏
edges of p
σz
j (39)
The Hamiltonian for the second phase,
H− = −
∑
I
∏
legs of I
σx
i +
∑
p
(
∏
edges of p
σz
j )(
∏
legs of p
i
1−σ x
j
2 )
(40)
is less familiar. However, one can check that in both
cases, the Hamiltonians are exactly soluble and the two
ground state wave functions are precisely Φ ± (in the σx
basis).
Next we ﬁnd the quasiparticle excitations for the two
phases, and the corresponding S-matrix and twists θα .
In both cases, equation (22) has 4 irreducible solu-
tions ( nα,s , Ω ij
α,st , ¯Ω ij
α,st ), α = 1, 2, 3, 4 - corresponding to
4 quasiparticle types. For the ﬁrst phase (Φ +) these so-
lutions are given by:
n1, 0 = 1, n 1, 1 = 0, Ω 0
1, 000 = 1, Ω 1
1, 001 = 1
n2, 0 = 0, n 2, 1 = 1, Ω 1
2, 110 = 1, Ω 0
2, 111 = 1
n3, 0 = 1, n 3, 1 = 0, Ω 0
3, 000 = 1, Ω 1
3, 001 = −1
n4, 0 = 0, n 4, 1 = 1, Ω 1
4, 110 = 1, Ω 0
4, 111 = −1
L-vertex
R-leg
P
j
i
I
FIG. 13: A closed string operator W (P ) for the two models
(39),(40). The path P is drawn with a thick line, while the legs
are drawn with thin lines. The action of the string operators
(41),(44) on the legs is diﬀerent for legs that branch to the
right of P , “R-legs”, and legs that branch to the left of P , “L-
legs.” Similarly, we distinguish between “R-vertices” and “L-
vertices” which are ends of “R-leg” and “L-leg” respectivel y.
The other elements of Ω vanish. In all cases ¯Ω = Ω.
The corresponding string operators for a path P are
W1 = Id
W2 =
∏
edges of P
σz
j
W3 =
∏
R-legs
σx
k
W4 =
∏
edges of P
σz
j
∏
R-legs
σx
k (41)
where the “R-legs” k are the legs that are to the right
of P . (See Fig. 13). Technically, we should multiply
these string operators by an additional projection opera-
tor∏
I∈P QI , in order to be consistent with the general
result (19). However, we will neglect this factor since it
doesn’t aﬀect the physics.
Once we have the string operators, we can easily cal-
culate the twists and the S-matrix. We ﬁnd:
eiθ 1 = 1, e iθ 2 = 1, e iθ 3 = 1, e iθ 4 = −1 (42)
S = 1
2


1 1 1 1
1 1 −1 −1
1 −1 1 −1
1 −1 −1 1

 (43)
This is in agreement with the twists and S-matrix for
Z2 gauge theory: W1 creates trivial quasiparticles, W2
creates magnetic ﬂuxes, W3 creates electric charges, W4
creates electric/magnetic bound states.
In the second phase (Φ −), we ﬁnd
n1, 0 = 1, n 1, 1 = 0, Ω 0
1, 000 = 1, Ω 1
1, 001 = 1
n2, 0 = 0, n 2, 1 = 1, Ω 1
2, 110 = 1, Ω 0
2, 111 = i
n3, 0 = 0, n 3, 1 = 1, Ω 1
3, 110 = 1, Ω 0
3, 111 = −i
n4, 0 = 1, n 4, 1 = 0, Ω 0
4, 000 = 1, Ω 1
4, 001 = −1
Once again, the other elements of Ω vanish. Also, in all
cases, ¯Ω = Ω ∗. The corresponding string operators for a
path P are
W1 = Id
W2 =
∏
edges of P
σz
j
∏
R-legs
i
1−σ x
j
2
∏
L-vertices
(−1)sI
W3 =
∏
edges of P
σz
j
∏
R-legs
(−i)
1−σ x
j
2
∏
L-vertices
(−1)sI
W4 =
∏
R-legs
σx
j (44)
where the “L-vertices” I are the vertices of P adjacent to
legs that are to the left of P . The exponent sI is deﬁned
by sI = 1
4 (1 − σx
i )(1 + σx
j ), where i, j are the links just
before and just after the vertex I, along the path P . (See
Fig. 13).
We ﬁnd the twists and S-matrix are
eiθ 1 = 1, e iθ 2 = i, e iθ 3 = −i, e iθ 4 = 1 (45)
S = 1
2


1 1 1 1
1 −1 1 −1
1 1 −1 −1
1 −1 −1 1

 (46)
We see that W1 creates trivial quasiparticles, W2, W3
create semions with opposite chiralities and trivial mu-
tual statistics, and W4 creates bosonic bound states of
the semions. These results agree with the U (1) × U (1)
Chern-Simons theory
L = 1
4π KIJ aIµ ∂ν aJλ ǫµνλ , I, J = 1, 2 (47)
with K-matrix
K =
(
2 0
0 −2
)
(48)
Thus the above U (1) × U (1) Chern-Simons theory is the
low energy eﬀective theory of the second exactly soluble
model (with d1 = −1).
Note that the Z2 gauge theory from the ﬁrst exactly
soluble model (with d1 = 1) can also be viewed as a
U (1) × U (1) Chern-Simons theory with K-matrix [23]
K =
(
0 2
2 0
)
(49)
