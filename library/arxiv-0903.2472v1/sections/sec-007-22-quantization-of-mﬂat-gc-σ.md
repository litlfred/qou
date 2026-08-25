---
doc_id: arxiv-0903.2472v1
doc_title: "Exact Results for Perturbative Chern-Simons Theory with Complex Gauge Group"
section_id: sec-007-22-quantization-of-mﬂat-gc-σ
section_title: "Quantization of Mﬂat (GC, Σ)"
section_number: 2.2
pages: 15-18
source_pdf: 0903.2472v1.pdf
source_sha256: 637cfd1d4d833c02
doc_brief: "Exact Results for Perturbative Chern-Simons Theory with Complex Gauge Group — We develop several methods that allow us to compute all-loop partition functions in perturbative Chern-Simons theory with"
---
Now, let us describe another approach to Chern-Simons gauge theory, based on quantiza-
tion of moduli space spaces of ﬂat connections. We focus on a t heory with complex gauge
group, which is the main subject of the present paper. 3
As we already mentioned in the introduction, Chern-Simons g auge theory (with any
gauge group) associates a Hilbert space HΣ to a closed Riemann surface Σ and a vector in
HΣ to every 3-manifold M with boundary Σ. We denote this vector as |M⟩∈H Σ . If there
are two such manifolds, M+ and M−, glued along a common boundary Σ (with matching
orientation), then the quantum invariant Z(M ) that Chern-Simons theory associates to
the closed 3-manifold M =M+∪Σ M− is given by the inner product of two vectors |M+⟩
and|M−⟩ inHΣ
Z(M ) = ⟨M+|M−⟩. (2.19)
Therefore, in what follows, our goal will be to understand Ch ern-Simons gauge theory on
manifolds with boundary, from which invariants of closed ma nifolds without boundary can
be obtained via (2.19).
Since the Chern-Simons action (1.1) is ﬁrst order in derivat ives, the Hilbert space HΣ
is obtained by quantizing the classical phase space, which i s the space of classical solutions
on the 3-manifold R× Σ. According to (1.3), such classical solutions are given pr ecisely
by the ﬂat connections on the Riemann surface Σ. Therefore, i n a theory with complex
gauge group GC, the classical phase space is the moduli space of ﬂat GC connections on Σ,
modulo gauge equivalence,
Mﬂat (GC, Σ) = Hom( π1(Σ),G C)/conj. (2.20)
3We will see, however, that quantization of Chern-Simons the ory with complex gauge group GC is closely
related to quantization for compact group G. Indeed, as we shall describe in Section 2.2.1, this relatio n
may be used to justify the “analytic continuation” approach to computing perturbative GC invariants.
– 14 –
As a classical phase space, Mﬂat (GC, Σ) comes equipped with a symplectic structure ω,
which can also be deduced from the classical Chern-Simons ac tion (1.1). Since we are inter-
ested only in the “holomorphic” sector of the theory, we shal l look only at the kinetic term
for the ﬁeld A (and not ¯A); it leads to a holomorphic symplectic 2-form on Mﬂat (GC, Σ):
ω = i
4ℏ
∫
Σ
TrδA∧ δA. (2.21)
We note that this symplectic structure does not depend on the complex structure of Σ,
in accord with the topological nature of the theory. Then, in Chern-Simons theory with
complex gauge group GC, the Hilbert space HΣ is obtained by quantizing the moduli space
of ﬂat GC connections on Σ with symplectic structure (2.21):
quantization of (Mﬂat (GC, Σ),ω ) ↝ HΣ . (2.22)
Now, let us consider a closed 3-manifold M with boundary Σ = ∂M , and its associated
state|M⟩∈H Σ . In a (semi-)classical theory, quantum states correspond t o Lagrangian
submanifolds of the classical phase space. Recall that, by d eﬁnition, a Lagrangian subman-
ifoldL is a middle-dimensional submanifold such that the restrict ion of ω toL vanishes,
ω|L = 0 . (2.23)
For the problem at hand, the phase space is Mﬂat (GC, Σ) and the Lagrangian submanifold
L associated to a 3-manifold M with boundary Σ = ∂M consists of the classical solutions
onM . Since the space of classical solutions on M is the moduli space of ﬂat GC connections
on M ,
Mﬂat (GC,M ) = Hom(π1(M ),G C)/conj., (2.24)
it follows that
L = ι
(
Mﬂat (GC,M )
)
(2.25)
is the image of Mﬂat (GC,M ) under the map
ι :Mﬂat (GC,M )→M ﬂat (GC, Σ) (2.26)
induced by the natural inclusion map π1(Σ) →π1(M ). One can show thatL⊂M ﬂat (GC, Σ)
is indeed Lagrangian with respect to the symplectic structu re (2.21).
Much of what we described so far is very general and has an obvi ous analogue in Chern-
Simons theory with arbitrary gauge group. However, quantiz ation of Chern-Simons theory
with complex gauge group has a number of good properties. In t his case the classical phase
spaceMﬂat (GC, Σ) is an algebraic variety; it admits a complete hyper-K¨ ahl er metric [28],
and the Lagrangian submanifold L is a holomorphic subvariety of Mﬂat (GC, Σ). The
hyper-K¨ ahler structure onMﬂat (GC, Σ) can be obtained by interpreting it as the moduli
spaceMH(G, Σ) of solutions to Hitchin’s equations on Σ. Note that this re quires a choice
of complex structure on Σ, whereas Mﬂat (GC, Σ) ∼
=MH(G, Σ) as a complex symplectic
manifold does not. Existence of a hyper-K¨ ahler structure o nMﬂat (GC, Σ) considerably
– 15 –
simpliﬁes the quantization problem in any of the existing fr ameworks, such as geometric
quantization [54], deformation quantization [6, 32], or “b rane quantization” [24].
The hyper-K¨ ahler moduli spaceMH(G, Σ) has three complex structures that we de-
note as I, J, and K =IJ , and three corresponding K¨ ahler forms, ωI, ωJ , and ωK. In the
complex structure usually denoted by J,MH (G, Σ) can be identiﬁed with Mﬂat (GC, Σ) as
a complex symplectic manifold with the holomorphic symplec tic form (2.21),
ω = 1
ℏ (ωK +iωI). (2.27)
Moreover, in this complex structure, L is an algebraic subvariety of Mﬂat (GC, Σ). To be
more precise, it is a (ﬁnite) union of algebraic subvarietie s, each of which is deﬁned by
polynomial equations Ai = 0. In the quantum theory, these equations are replaced by
corresponding operators ˆAi acting onHΣ that annihilate the state |M⟩.
Now, let us consider in more detail the simple but important c ase when Σ is of genus
1, that is Σ = T 2. In this case, π1(Σ) ∼
= Z× Z is abelian, and
Mﬂat (GC,T 2) = ( TC× TC)/W , (2.28)
where TC is the maximal torus of GC andW is the Weyl group. We parametrize each copy
of TC by complex variables l = (l1,...,l r) and m = (m1,...,m r), respectively. Here, r is
the rank of the gauge group GC. The values of l and m are eigenvalues of the holonomies
of the ﬂat GC connection over the two basic 1-cycles of Σ = T 2. They are deﬁned up to
Weyl transformations, which act diagonally on TC× TC.
The moduli space of ﬂat GC connections on a 3-manifold M with a single toral bound-
ary,∂M =T 2, deﬁnes a complex Lagrangian submanifold
L⊂ (TC× TC)/W . (2.29)
(More precisely, this Lagrangian submanifold comprises th e top-dimensional (stable) com-
ponents of the moduli space of ﬂat GC connections on Σ.) In particular, a generic irreducible
component ofL is deﬁned by r polynomial equations
Ai(l,m ) = 0 , i = 1,...,r, (2.30)
which must be invariant under the action of the Weyl group W (which simultaneously acts
on the eigenvalues l1,...,l r and m1,...,m r). In the quantum theory, these equations are
replaced by the operator equations (1.12),
ˆAi(ˆl, ˆm)Z(M ) = 0 , i = 1,...,r. (2.31)
For Σ = T 2 the complex symplectic structure (2.21) takes a very simple form
ω = i
ℏ
r∑
i=1
dui∧dvi, (2.32)
– 16 –
where we introduce new variables u and v (deﬁned modulo elements of the cocharacter
lattice Λ cochar = Hom( U (1), T)), such that l =−ev and m =eu. In the quantum theory,
u and v are replaced by operators ˆu and ˆv that obey the canonical commutation relations
[ˆui, ˆvj] = −ℏδij . (2.33)
As one usually does in quantum mechanics, we can introduce a c omplete set of states |u⟩
on which ˆu acts by multiplication, ˆui|u⟩ =ui|u⟩. Similarly, we let |v⟩ be a complete basis,
such that ˆvi|v⟩ =vi|v⟩. Then, we can deﬁne the wave function associated to a 3-manif old
M either in the u-space or v-space representation, respectively, as ⟨u|M⟩ or⟨v|M⟩. We
