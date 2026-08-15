---
doc_id: arxiv-1701.06567v2
doc_title: "BPS spectra and 3-manifold invariants"
section_id: sec-006-22-d2s1-partition-function-of-t-m3-and-wrt-invar
section_title: "D2×S1 partition function of T [M3] and WRT invariant"
section_number: 2.2
pages: 7-14
source_pdf: 1701.06567v2.pdf
source_sha256: c1610b50f5a7e22c
doc_brief: "BPS spectra and 3-manifold invariants — We provide a physical deﬁnition of new homological invariants Ha(M3) of 3- manifolds (possibly, with knots) labeled by abelian ﬂat connections."
---
Now we are ready to present a slightly generalized and improved version of the results from [27,
sec. 6].
Categoriﬁcation of WRT invaraiant
Let ZSU (2)k[M3] be the partition function of SU (2) Chern-Simons theory with “bare” level
(k−2) onM3, also known as the WRT invariant. We use the standard “physics” normalization
where
ZSU (2)k
[
S2×S1]
= 1, (2.4)
and
ZSU (2)k
[
S3]
=
√
2
k sin
(π
k
)
. (2.5)
The following conjecture was proposed in [27]. 4
Conjecture 2.1 The WRT invariant can be decomposed into the following form:
ZSU (2)k[M3] = (i
√
2k)b1(M3)−1 ∑
a,b∈
TorH1(M3,Z)/Z2
e2πik𝓁k(a,a)Sab ˆZb(q)|
q→e
2πi
k
(2.6)
with56
ˆZb(q)∈ 2−cq∆bZ[[q]] ∆ b∈ Q, c ∈ Z+ (2.7)
3It is in fact (TorH1(M3, Z))∗/Z2 that is canonically identiﬁed with components of abelian ﬂat connections.
However, as the distinction between Tor H1(M3, Z) and its dual is only important in section 2.2, we will use
the same set of labels {a,b,... } for elements in both groups.
4A related conjecture was made in [28]. However it did not include the S-transform, which is crucial for
restoring integrality and categoriﬁcation.
5The constant positive integer c depends only on M3 and in a certain sense measures its “complexity”. In
many simple examples c = 0, and the reader is welcome to ignore 2−c factor which arises from some technical
subtleties. Its physical origin will be explained later in the paper.
6Later in the text we will sometimes use slightly redeﬁned quantities, ˆZa(q)→ q∆ˆZa(q), where ∆ is a
common, a independent rational number.
– 6 –
convergent in|q|< 1 and
Sab = e4πi𝓁k(a,b) +e−4πi𝓁k(a,b)
|Wa|
√
|TorH1(M3, Z)|
. (2.8)
In other words, we claim the existence of new 3-manifold invariants ˆZa, which admit q-series
expansion with integer powers and integer coeﬃcients (hence, more suitable for categoriﬁca-
tion) and from which the WRT invariant can be reconstructed via ( 2.6). While the formal
mathematical deﬁnition of the invariants ˆZa is waiting to be discovered, they admit a physics
deﬁnition that will be reviewed below and can be independently computed via techniques of
resurgent analysis. In particular, each term
∑
b∈TorH1(M3,Z)
e2πik𝓁k(a,a)Sab ˆZb(q)
⏐⏐⏐
q→e
2πi
k
≡e2πik𝓁k(a,a)Za(q) (2.9)
in the sum ( 2.6) is a certain resummation of the perturbative (in 2πi
k or, equivalently, in
(1−q)) expansions of the WRT invariant around the corresponding abelian ﬂat connection
a [22].
In order to avoid unnecessary technical complications, in the rest of this paper we assume
that TorH1(M3, Z) has no Z2 factors.7 Under this assumption, the S-matrix satisﬁes
∑
b
SabSbc =δac. (2.10)
Moreover, as will be discussed in detail below, physics predicts the existence of a Z× Z×
TorH1(M3, Z)/Z2 graded homological invariant of M3:
HD2[M3] =
⨁
a∈TorH1(M3,Z)/Z2
Ha[M3], Ha[M3] =
⨁
i∈Z+∆a,
j∈Z
Hi,j
a (2.11)
which categoriﬁes the q-series ˆZa(q). Namely 8,
ˆZa(q) =
∑
i∈Z+∆a,
j∈Z
qi(−1)j dimHi,j
a . (2.12)
Because of their close relation to homological invariants, we usually refer to ˆZa(q) as homo-
logical blocks. The vector space HD2[M3] can be interpreted as the closed 3-manifold analog
7Recall that TorH1(M3, Z), as a ﬁnitely generated abelian group, can be decomposed into TorH1(M3, Z) =∏
i Zpi. We ask for a fairly weak condition that Z2 doesn’t appear in this decomposition. In other words, M3
is a Z2-homology sphere. Equivalently, there is a unique Spin structure on M3, so that there is no ambiguity
in specifying Nahm-pole boundary condition for N = 4 SU (2) SYM on M3× R+ [18]. The general case, in
principle, could also be worked out. We leave it as an exercise to an interested reader.
8The presence of 1/2 factors that produce 2−c overall factor in (2.7) can be interpreted as presence of factors
∼= C[x] with degqx = 0 inHa[M3]. The q-graded Euler charecteristic of C[x] is naively divergent: 1+1+1+ ... ,
but its zeta-regularization gives 1/2.
– 7 –
of Khovanov-Rozansky knot homology. From this point of view, e4πi𝓁k(a,·) can be understood
as the variable associated with Tor H1(M3, Z)/Z2 grading and enters into the decomposition
(2.6) much like q, the variable for one of the Z-gradings (the “q-grading”). Note that the
label a inHi,j
a is reminiscent of the Spinc structure in Heegaard/monopole Floer homologies
of 3-manifolds. This fact, of course, is not an accident and plays an important role in the re-
lation between Heegaard/monopole Floer homologies of 3-manifolds and the categoriﬁcation
of WRT invariants [27].
Next, we describe the physics behind the Conjecture 2.1. (A mathematically inclined
reader may skip directly to Conjecture 2.2.)
(time) x
Figure 2: Another representation of the background in Figure 1.
Physics behind the proposal
From physics point of view, the homological invariantsHa[M3] can be realized by the following
M-theory geometry,
N ﬁvebranes: R× M3 × D2
∩ ∩
space-time: R× T∗M3 × TN
⟳ ⟳
symmetries: “ U(1)N” U(1)q×U(1)R.
(2.13)
or, equivalently, any of its dual descriptions (some of which will be discussed below). Here,
the ﬁrst two lines summarize the geometry of the ﬁvebranes and their ambient space, whereas
the last line describes their symmetries. The reason “ U(1)N” appears in quotes is that it is a
symmetry of our physical system only whenM3 is a Seifert 3-manifold, unlike the “universal”
symmetry group U(1)q×U(1)R.
In order to preserve supersymmetry for a general metric on M3, it has to be embedded in
the geometry of ambient space-time as a supersymmetric (special Lagrangian) cycleM3⊂CY3
which, according to McLean’s theorem, always looks like M3⊂T∗M3 near the zero section.
Equivalently, the geometryT∗M3 represents a partial topological twist on the ﬁvebrane world-
volume, upon which three of the scalar ﬁelds on the world-volume become sections of the
cotangent bundle of M3. As a result, one can ﬁrst reduce the 6d (2 , 0) theory — the world-
volume theory of M5-branes — on M3 to obtain a 3d N = 2 SCFT usually denoted as
T [M3;G], where G = U(N) or SU (N), N being the number of M5-branes. All SUSY-
protected objects like partition functions, index and BPS spectra of the resulting theory
– 8 –
T [M3;G] do not depend9 on the metric ofM3, and give rise to numerical as well as homological
invariants ofM3.
Similarly, in order to preserve supersymmetry of the brane system ( 2.13) along the other
world-volume directions of the ﬁvebranes, one needs to introduce a SUSY-preserving back-
ground alongD2. Moreover, it needs to be done in a way that preserves the rotation symmetry
U(1)q×U(1)R and allows to keep track of the corresponding quantum numbers (spins) of
BPS states, as required for categoriﬁcation. The suitable background can be described in a
number of equivalent ways: as the Omega-background along TN ∼= R4
q,t in which D2∼= R2 is
embedded as a linear subspace, or as a U(1)q×U(1)R invariant Lagrangian submanifold (the
“cigar”) D2 in the Taub-NUT space TN where one keeps track of the spin with respect to
the rotation symmetry, cf. Figure 2. To emphasize that one keeps track of both spins under
U(1)q×U(1)R symmetry, the adjective reﬁned is often added to the invariant, BPS state, or
other object under consideration.
WhenM3 is a Seifert manifold, the brane system (2.13) enjoys an extra symmetryU(1)N
that appears in a degeneration limit of the metric on M3 and can be used to redeﬁne the
R-symmetry of the SCFTT [M3]. When M3 is Σ×S1, the symmetryU(1)N×U(1)R is further
enhanced to the SU (2)N×SU (2)R R-symmetry of the 3dN = 4 theory T [Σ×S1]; when M3
is a generic Seifert manifold, one combination gives the R-symmetry of the 3d N = 2 theory
T [M3] which we denote as U(1)R, while another is a ﬂavor symmetry U(1)β, see [27, sec. 3.4]
for details.
After reduction on M3, the system ( 2.13) gives a theory T [M3;G] in space-time D2× R,
illustrated in Figure 1, and we can consider its Hilbert space with a certain boundary condition
at ∂D2 = S1. For N = 2 and G = SU (2) — the case that we will be mostly considering
in this paper — these boundary conditions turn out to be labeled by a∈ TorH1(M3, Z)/Z2.
Then, we arrive at a set of doubly-graded homological invariants of M3 labeled by a,
Ha[M3] = HT [M3](D2;a) =
⨁
i∈Z+∆a,
j∈Z
Hi,j
a , (2.14)
given by the BPS sector of the Hilbert space ofT [M3;SU (2)]. This is the subspace annihilated
by two of the four supercharges of the 3dN = 2 supersymmetry (diﬀerent choices are related
by automorphisms of the superconformal algebra, resulting in isomorphic BPS spaces). The
grading i counts the charge under the U(1)q rotation of D2 and the “homological” grading j
corresponds to R-charge of the U(1)R R-symmetry. When M3 is Seifert, the U(1)β symmetry
will give rise to the third grading 10 onHa[M3].
One can understand Ha[M3] =HT [M3](D2;a) as the massless multi-particle BPS spec-
trum of T [M3] with a label a∈ TorH1(M3, Z)/Z2 being a discrete charge. From M-theory
9A “folk theorem” states that any continuous deformation of the metric on M3 results in a Q-exact term
of the supergravity background. However, there may be dependence on discrete data such as the Atiyah
2-framing [29].
10Not to be confused with the extra “HOMFLY grading” e.g. on the right-hand side of ( 2.68).
– 9 –
point of view, the BPS particles of T [M3] arise from M2-branes ending on the pair of M5-
branes that realize the A1 6dN = (2, 0) theory. The boundaries of M2-branes wrap 1-cycles
(~a,−~a) so that [~a] = a∈ TorH1(M3, Z)/Z2. This is similar to the counting of BPS states
in [15]. Note, however, that BPS particles that arise from M2-branes ending on a non-torsion
1-cycles of M3 have mass and do not enter into the IR BPS spectrum. Therefore, it is el-
ements in Tor H1(M3, Z)/Z2 that give rise to physical boundary conditions which speciﬁes
a superselection sector labeled by this brane charge, resulting in a physical BPS Hilbert
spaceHa with integrality property. In contrast, a ﬂat connection, given by an element of
(TorH1(M3, Z))∗/Z2 doesn’t correspond to any physical boundary conditions. Instead, it is
a linear combination of physical boundary conditions leading to a mixture of diﬀerent charge
sectors.
From this point of view, the S-transform in Conjecture 2.1 carries out the change of basis
between charges (valued in TorH1(M3, Z)/Z2) and holonomies (valued in (TorH1(M3, Z))∗/Z2)
using the natural pairing between them via the “Aharonov-Bohm phase.” More precisely, the
M2-branes ending on M5-branes produce particles in the eﬀective 3d theory carrying electric-
magnetic charge b ∈ TorH1(M3, Z)/Z2.11 On the other hand, a ∈ (TorH1(M3, Z))∗/Z2
speciﬁed the holomony, and, by viewing (Tor H1(M3, Z))∗ as the group of characters of
TorH1(M3, Z), we have
Sab∝
∑
Z2 orbit of a
χa(b) =
∑
Z2 orbit of a
e4iπ𝓁k(a,b). (2.15)
Geometrically,Sab is the trace of the holonomy of the ﬂat connection labeled by a along the
1-cycle representing homology class b.
Alternatively, one can understand the boundary conditions in the type IIB duality frame
of the brane system ( 2.13), where S-transform can be interpreted as the S-duality of type
IIB string theory. Indeed, a quotient of the eleven-dimensional space-time by a circle action
U(1)q lands us in type IIA string theory, which can be further T-dualized along the “time”
circle S1. (Equivalently, these two dualities can be combined into one step, which is the
standard M-theory / type IIB duality.) The resulting system involves D3-branes ending
on a D5-brane, and S-duality of type IIB string theory maps it into a stack of D3-branes
ending on an NS5-brane [18]. Note, that the natural choice of boundary conditions at inﬁnity
for a system of D3-branes ending on an NS5-brane is an arbitrary (not necessarily abelian)
SL(2, C) ﬂat connection on M3. Such choice of a ﬂat connection corresponds to considering
analytically continuedSU (2) Chern-Simons theory on the Lefschetz thimble associated to that
ﬂat connection. However, in general, the corresponding partition function is not continuous in
a disk|q|< 1 due to Stokes phenomena. Instead, in ( 2.9) we consider quantities Za(q) which
are labeled by abelian ﬂat connections only, and analytic inside|q|< 1. As explained in [22],
for a given value of argk one can express Za(q) as a linear combination of the Feynman path
11Note that in the case of N M5-branes wrapping M3, the M2-branes produce states charged under the
magnetic U(1)N/SN (not necessarily U(N)) symmetry, as explained in [15].
– 10 –
integral on Lefschetz thimbles. If one were to write the S-transform in the basis corresponding
to Lefschetz thimbles, instead of Za(q), the S-matrix would be k-dependent.
By deﬁnition, each homological block ˆZa(q) is the graded Euler characteristics ( 2.35) of
Ha that can be computed as an supersymmetric partition function of T [M3] onD2×qS1 with
anN = (0, 2) supersymmetric boundary condition a and metric corresponding to rotation of
the disk D2 by argq when we go around the S1,
ˆZa(q) =ZT [M3](D2×qS1;a). (2.16)
If one knows the Lagrangian description of T [M3], this partition function can be computed
using localization, see e.g. [30].
Note, if the Lagrangian description of T [M3] contains chiral multiplets charged under
the gauge symmetry, carrying zero R-charge (at the unitarity bound) and with Neumann
boundary conditions, then the integral computing theD2×qS1 partition function (i.e. the half-
index) will be singular in general. For example, for g adjoint chiral multiplets the partition
function has the following form:
1
2
∫
|z|=1
dz
2πiz
f(z,q )
(1−z2)g−1(1−z−2)g−1, f (z,q ) =f(z−1,q )∈ Z[z,z−1][[q]]. (2.17)
A natural way to regularize it is to take the principle value prescription:
1
2 v.p.
∫
|z|=1
dz
2πiz
f(z,q )
(1−z2)g−1(1−z−2)g−1 ≡
1
4
(∫
|z|=1+ϵ
+
∫
|z|=1−ϵ
)
dz
2πiz
f(z,q )
(1−z2)g−1(1−z−2)g−1. (2.18)
As we will see in many examples, this regularization prescription is in agreement with the
relation between ˆZa(q) =ZT [M3](D2×qS1;a) and the WRT invariant. This is also the source
of the 2−c factor in (2.7).12
Resurgence in 3d N = 2 theories
The phenomenon of non-abelian contributions being distributed among the abelian ones can
be translated entirely into the language of 3d N = 2 ﬁeld theories. In fact, this phenomenon
is not limited to theories T [M3] associated with 3-manifolds and should be regarded more
broadly, as a decomposition of BPS quantities in gapless (conformal) theories into BPS spectra
of its massive deformations.
12Such factor can appear even without singularity, when there is only g = 1 adjoint chiral with R-charge 0.
It cancels the contribution of the vector multiplet, leaving
1
2
∫ dz
2πiz f(z,q ) = 1
2[z0 coeﬃcient of f(z,q )], (2.19)
where one can take f(z,q ) = 1, as an example.
– 11 –
Thanks to supersymmetric localization, partition functions of 3d N = 2 theories on
D2×qS1 can be reduced to ﬁnite-dimensional integrals, which in the limit q =eℏ→ 1 have
the form
Z(D2×qS1) =
∫
dz ∆(z) exp
(1
ℏ
~W(z) +...
)
. (2.20)
The multi-variable z = (z1,...,z r) typically comes from gauge factors, and ~W(z) can be
interpreted as a twisted superpotential of the 3d theory on a circle. Its critical points are the
vacua of the 2dN = (2, 2) eﬀective ﬁeld theory, which for a ﬁnite-size circle come in inﬁnite
towers. Indeed, when the 3d theory is compactiﬁed on a circle of ﬁnite radius, the variables
zi are C∗-valued and the equations for vacua also have the exponentiated form:
exp
(
∂~W
∂ logzi
)
= 1. (2.21)
For this reason, each vacuum comes in an inﬁnite family, much like saddle points of Chern-
Simons functional. Also, as in Chern-Simons theory, the critical points of ~W have the leading
order behavior
ℏn/2e
1
ℏ
~W(z∗)· (power series in ℏ) (2.22)
where the critical exponent n is the degree of degeneracy of the critical point z = z∗; the
larger the value of n the more singular the critical point is (see [31] for a careful treatment of
such factors).
Figure 3: Critical points of ~W in 3dN = 2 theories come in inﬁnite towers because, as in complex
Chern-Simons theory, the space of ﬁelds is not simply-connected. Moreover, a generic theory has
degenerate, non-Morse critical points, which arise, e.g., when the ﬁelds at the critical point have a
large stabilizer. In localization integrals, such critical points “absorb” the contributions of regular,
Morse critical points as trans-series.
– 12 –
Therefore, in the context of completely general 3d N = 2 theories we ﬁnd two key
elements of the resurgent analysis [22]: the critical points come in inﬁnite Z-towers and they
may have diﬀerent degree of degeneracy signalled by powers of ℏ = logq. Hence, applying
the resurgent analysis of [22] to the integral ( 2.20), we conclude that contributions of critical
points with smaller values of the exponent n will be “distributed” among critical points with
larger values of n.
In order to see this phenomenon in physically-motivated 3d N = 2 theories, such as 3d
SQED or SQCD, we simply need to look at examples with non-trivial range of values of n.
