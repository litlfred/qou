---
doc_id: arxiv-2601.07906v2
doc_title: "A universal sum over topologies in 3d gravity"
section_id: sec-031-virasoro-tqft-identities
section_title: "Virasoro TQFT identities"
section_number: null
pages: 98-106
source_pdf: 2601.07906v2.pdf
source_sha256: e69b1bf37f2c75b0
toc_source: outline
doc_brief: "A universal sum over topologies in 3d gravity — We explore the sum over topologies in AdS3 quantum gravity and its relationship with the statistical interpretation of the boundary theory."
---
Virasoro TQFT identities
Here we collect some Virasoro TQFT manipulations and identities that are useful for
the computations that appear in the main text. All equalities should be understood
to hold at the level of the VTQFT partition functions, and may be applied as local
manipulations within a bigger network of Wilson lines.
Braiding.
Braiding of Wilson lines produces a phase:
1
3
2
= B1
23
1
3
2
= eπi(h2+h3−h1)
1
3
2
.
(C.1)
The opposite braiding involves the opposite phase. Configurations with opposite
patterns of over- and under-crossings are related by complex conjugation.
Fictitious identity line.
We will frequently simplify Wilson line configurations
via the insertion of a fictitious identity line followed by a fusion move:
1
2
1
=
Z ∞
0
dP ρ0(P)C0(P1, P2, P)
1
2
1
2
P
(C.2)
This has the effect of adding two trivalent vertices to the Wilson line configuration.
– 98 –
Wilson bubble.
The VTQFT Hilbert space on the twice-punctured sphere is one-
dimensional, and is only nontrivial when the two Wilson lines carry identical Liouville
momenta. Thus any cut along a 2-punctured sphere must produce an amplitude
proportional to a delta function. In the case of the Wilson bubble pictured below,
we have [11]:
1
2
3
4
=
δ(P1 −P4)
ρ0(P1)C0(P1, P2, P3)
1
.
(C.3)
Fusion kernel and the 6j symbol.
The Virasoro fusion kernel F implements the
fusion transformation on Wilson line configurations:
1
4
2
3
t
=
Z ∞
0
dPs FPtPs
P1 P2
P4 P3

1
2
4
3
s
.
(C.4)
The fusion kernel is simply related to the Virasoro 6j symbol via the relation:
P1 P2 Ps
P3 P4 Pt

=
1
ρ0(Ps)
r
C14tC23t
C12sC34s
FPtPs
P1 P2
P4 P3

.
(C.5)
Here we have introduced the convenient shorthand:
Cijk ≡C0(Pi, Pj, Pk) .
(C.6)
In cases where there is little room for confusion, we will occasionally represent the
6j symbol using the following abbreviated notation:
i j k
ℓm n

≡
Pi Pj Pk
PℓPm Pn

.
(C.7)
The Virasoro 6j symbol enjoys a tetrahedral symmetry that manifests as an invari-
ance under swapping the rows or columns of any 2 × 2 sub-block. For example, from
this we learn that the fusion kernel is straightforwardly related to its inverse as:
FPtPs
P1 P2
P4 P3

ρ0(Ps)C0(P1, P2, Ps)C0(P3, P4, Ps) =
FPsPt
P1 P4
P2 P3

ρ0(Pt)C0(P1, P4, Pt)C0(P2, P3, Pt) .
(C.8)
Written in terms of the 6j symbol, the fusion transformation (C.4) takes the form:
1
4
2
3
t
=
Z ∞
0
dPs ρ0(Ps)
1 2 s
3 4 t
 r
C12sC34s
C14tC23t
1
2
4
3
s
.
(C.9)
– 99 –
u-channel crossing.
The Virasoro fusion kernel also describes the crossing trans-
formations involving u-channel blocks. The crossing relations involve phases due to
the braiding of Wilson lines:
1
4
2
3
s
=
Z ∞
0
dPu eπi(P 2
s +P 2
u−P 2
1 −P 2
4 ) FPsPu
P1 P3
P2 P4

1
4
2
3
u
(C.10)
=
Z ∞
0
dPu ρ0(Pu)eπi(P 2
s +P 2
u−P 2
1 −P 2
4 )
1 2 s
4 3 u
 r
C13uC24u
C12sC34s 1
4
2
3
u
.
(C.11)
Wilson triangle.
The VTQFT Hilbert space on the 3-punctured sphere is one-
dimensional, so cutting a configuration of Wilson lines along a sphere punctured by
three Wilson lines prepares a state proportional to that of the corresponding trivalent
vertex. A simple example is the Wilson triangle shown below, which is related to the
trivalent vertex by a factor proportional to the Virasoro 6j symbol [11]:
s
t
4
3
1
2
=
r
C12s
C34sC14tC23t
1 2 s
3 4 t

s
1
2
.
(C.12)
Wilson square.
With the Wilson triangle identity one can decompose more com-
plicated Wilson line configurations into integrals over 6j symbols. For example, the
“Wilson square” shown below prepares a state in the Hilbert space of the 4-punctured
sphere, which admits the following representation:
a
b
c
d
1
4
3
2
=
Z ∞
0
dPs ρ0(Ps)Cacs
a
b
c
d
a
c
1
4
3
2
s
(C.13)
=
Z ∞
0
dPs ρ0(Ps)
r
C12sC34s
C1daC4abC3bcC2cd
1 a d
c 2 s
 4 a b
c 3 s
 1
2
4
3
s
(C.14)
=
Z ∞
0
dPt ρ0(Pt)
r
C14tC23t
C1daC4abC3bcC2cd
1 d a
b 4 t
 3 b c
d 2 t
 1
4
2
3
t
.
(C.15)
The above relation resembles a crossing equation for a boundary 4-point function
on the disk in BCFT, and indeed with a particular choice of operator normalization
– 100 –
it is equivalent to the disk boundary 4-point function in Liouville CFT with FZZT
boundary conditions [137–140], where the Liouville momenta of the a, b, c, d Wilson
lines correspond to the FZZT parameters (which are straightforwardly related to
the boundary cosmological constants) of the boundary conditions. Similarly we can
interpret the Wilson triangle above in terms of the FZZT boundary 3-point function
[139]. The connection between simple observables in Virasoro TQFT and Liouville
BCFT with FZZT boundary conditions will be explored in more detail elsewhere.
The modular crossing kernel and relation to the fusion kernel.
The Vi-
rasoro modular kernel S locally implements the modular S transformation on the
once-punctured torus. It can be recast as an integral over the fusion kernel:
SP1P2[P0]
ρ0(P2)C0(P2, P2, P0) =
Z ∞
0
dP eπi(2hP +h0−2h1−2h2)
FP0P
P1 P2
P1 P2

C0(P1, P2, P) .
(C.16)
This relation can be derived by computing the Virasoro TQFT amplitude on the
Hopf link with an extra Wilson line embedded in S3, as discussed in [12]:
2
1
0
.
(C.17)
This representation makes it manifest that the modular kernel satisfies the following
identity that swaps the lower indices:
SP1P2[P0]
ρ0(P2)C0(P2, P2, P0) =
SP2P1[P0]
ρ0(P1)C0(P1, P1, P0) .
(C.18)
It is sometimes cleaner to express VTQFT amplitudes in terms of the modular kernel
in the ‘Racah-Wigner’ normalization [20], which following [85] we denote with a hat:
bSP1P2[P0] =
1
ρ0(P2)
s
C0(P1, P1, P0)
C0(P2, P2, P0)SP1P2[P0].
(C.19)
In this normalization the modular kernel is invariant under swapping its lower indices:
bSP1P2[P0] = bSP2P1[P0] .
(C.20)
The modular kernel normalized this way can also be expressed as the following inte-
gral over the Virasoro 6j symbol:
bSP1P2[P0] =
Z ∞
0
dP ρ0(P)eπi(2hP +h0−2h1−2h2)
P1 P2 P
P2 P1 P0

(C.21)
– 101 –
=
Z ∞
0
dP ρ0(P)eπi(2h1+2h2−2hP )
P1 P2 P
P2 P1 P0

.
(C.22)
In the second line above we have used the fact that the modular kernel satisfies the
reality property
bS∗
P1P2[P0] = e−πih0 bSP1P2[P0].
(C.23)
We can also go the opposite direction, and express the 6j symbol (with repeated
external momenta) in terms of the modular kernel. This is the Virasoro-Verlinde
formula [85]:
P3 P3 P0
P1 P1 P2

=
Z ∞
0
dP bSP1P[P0] SPP2[1] bSPP3[P0]∗.
(C.24)
Consistency conditions of the Moore-Seiberg construction.
The Virasoro
fusion kernel/6j symbol and the modular crossing kernel describe the behaviour of
Virasoro conformal blocks (or components of Virasoro blocks) under the action of
elementary crossing moves. As such, they are subject to a number of consistency
conditions [57], which have been established in [64, 141]. They are given as:
• Idempotency:
Z ∞
0
dPb ρ0(Pb)
1 4 a
3 2 b
 1 2 b
3 4 c

= δ(Pa −Pc)
ρ0(Pa)
,
(C.25a)
Z ∞
0
dPb ρ0(Pb) bSPaPb[P0]bS∗
PbPc[P0] = δ(Pa −Pc)
ρ0(Pa)
.
(C.25b)
• Pentagon identity:
Z ∞
0
dP ρ0(P)
1 2 c
5 4 P
 1 3 b
6 4 P
 2 3 a
6 5 P

=
a b c
1 2 3
 a b c
4 5 6

.
(C.26)
• Hexagon identity:
Z ∞
0
dPt ρ0(Pt)eπi(h1+h2+h3+h4−hs−ht−hu)
1 4 t
3 2 s
 1 3 u
2 4 t

=
1 3 u
4 2 s

.
(C.27)
• (ST)3 = 1 relation:
Z ∞
0
dP2 ρ0(P2) bSP1P2[P0]e−2πi P3
j=1(hj−c
24 )bSP2P3[P0] = bSP1P3[P0] .
(C.28)
• Relation at g = 1, n = 2:
bSP1P2[P3]
Z ∞
0
dP4 ρ0(P4)
2 0′ 4
0 2 3

e2πi(h4−h2)
0 0′ 5
2 2 4

=
Z ∞
0
dP6 ρ0(P6)
1 0 6
0′ 1 3
 0 0′ 5
6 6 1

eπi(h0+h0′)bS∗
P6P2[P5] .
(C.29)
– 102 –
Verlinde lasso.
The looping of a Wilson line by a “Verlinde lasso” as shown below
produces a state that is proportional to the corresponding trivalent vertex by a factor
of the modular crossing kernel [142]:
2
1
3
= SP1P2[P3]
S1P2[1]
2
3
(C.30)
This can be derived by inserting an identity line between the 1 and u Wilson lines,
doing a fusion transformation, reducing the resulting Wilson triangle in terms of
the 6j symbol using (C.12), and then recognizing the integral representation of the
modular crossing kernel (C.22). The opposite pattern of over- and under-crossings
leads to the complex conjugate amplitude.
Verlinde loop.
Taking the limit P3 →1 of the Verlinde lasso relation leads to
the observation that Verlinde loops can be removed up to a factor of the modular
crossing kernel [20]:
2
1
1
= SP1P2[1]
S1P2[1]
2
(C.31)
Hooked lines.
In studying knots and links in Virasoro TQFT we often encounter
configurations involving Wilson lines linked as shown below, which can be simplified
as follows:
2
1
=
Z ∞
0
dP ρ0(P)C12P e2πi(hP −h1−h2)
P
1
1
2
2
(C.32)
=
Z ∞
0
dP ′ ρ0(P ′)
p
C11P ′C22P ′ bS∗
P1P2[P ′]
1
1
2
2
P ′
(C.33)
These representations can be derived either by inserting a fictitious identity line
between the two Wilson lines and then fusing the two lines, or by inserting an identity
line between two ends of the same Wilson line, doing a fusion move, and then applying
the Verlinde lasso rule (C.30). The latter introduces a factor of the modular crossing
kernel. The linking with the opposite pattern of over- and under-crossings leads to
the complex-conjugate amplitude.
– 103 –
Looped lines.
With these basic rules amplitudes involving Verlinde loops sur-
rounding more complicated configurations of Wilson lines can be evaluated by in-
serting various fictitious identity lines. For example, in the case of two looped lines
as shown below, we have:
1
2
u
u
=
Z ∞
0
dP ρ0(P)C12P bSuP[1]
1
2
1
2
P
(C.34)
=
Z ∞
0
dP ρ0(P)
p
C11PC22P bS∗
uP1[P]bSuP2[P]
P
1
2
1
2
(C.35)
The first line is derived by inserting a fictitious identity line between the 1 and
2 Wilson lines, and the second by inserting an identity line between two ends of
the u Wilson line. As an aside, in a similar spirit to the comments made below
(C.15), the above is proportional to the bulk two-point function in Liouville CFT
on the disk with FZZT boundary conditions (where the Liouville momentum of the
u Wilson line corresponds to the FZZT parameter associated to the disk), with the
expressions in the first and second lines corresponding to the closed- and open-string
channels respectively.
Omega-loop.
A special role is played by the so-called Ω-loop, which is a closed
Wilson line whose role is to project onto the identity Virasoro representation inside
the loop. In VTQFT this is implemented by integrating the Liouville momentum of
the privileged Wilson line weighted by the Cardy density of states ρ0(P) = S1P[1]:
Ω
Ω
≡
Z ∞
0
dP ρ0(P)
P
P
.
(C.36)
We can obtain some nice identities by acting with the Ω-loop on simple configurations
of Wilson lines. For example, enclosing a single Wilson line it simply projects that
Wilson line to the identity:
P
Ω
Ω
= δ(P −1)
ρ0(P)
P
.
(C.37)
To apply the Ω-loop to more complicated configurations we use the rules of VTQFT
to fuse Wilson lines such that a single representation runs through the loop and then
project that representation to the identity. In this work a privileged role is played
– 104 –
by the action of the Ω-loop on a pair of Wilson lines, which can be computed by
combining (C.2) and (C.37)
1
2
Ω
u
= δ(P1 −P2)
ρ0(P1)
1
2
(C.38)
This means that the Ω-loop around two parallel Wilson lines exactly implements the
cylinder surgery operation discussed in section 4.2.
Let us also comment on the meaning of the delta-function δ(P −1) appearing in
(C.37). It is meant to denote that the Wilson line originally labeled by the Liouville
momentum P is projected to the identity line, which is non-normalizable in VTQFT.
To rigorously make sense of it, we would need to delve into the theory of distributions,
see [143] or [144] for an attempt within 2d CFT. For the purposes of this paper, in
practice we only require the identity (C.38). The presence of an Ω-loop around a
single line typically leads to non-hyperbolic manifolds. In fact, the condition a) for
the cylinder surgery of the gravitational machine is precisely tailored to avoid this
situation.
Action of the modular transform on knotted graphs.
Using the relation-
ship between the modular and the fusion kernels (C.16), we can diagrammatically
represent the action of a S-transform on a loop in a knotted trivalent graph:
Z ∞
0
dP2 SP1P2[P0]
0
2
=
Z ∞
0
dP2 ρ0(P2)
0
1
2
(C.39)
=
0
1
Ω
.
(C.40)
Here the three lines are meant as a proxy for any more general configuration of Wilson
lines. This equation tells us that the S-transformed diagram now has an additional
Dehn filling. On the right-hand side the Wilson line with Liouville momentum P2
is integrated with the ρ0 kernel and thus acts as an Ωloop. One can derive this
expression by utilizing (C.16) and noting that:
0
2
1
1
P
= e2πi(h1+h2−hP )
C0(P2, P2, P0)FP0P
P2P1
P2P1

ρ0(P)C0(P, P1, P2)2
0
2 .
(C.41)
– 105 –
