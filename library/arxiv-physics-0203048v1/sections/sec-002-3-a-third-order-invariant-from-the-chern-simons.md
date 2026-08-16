---
doc_id: arxiv-physics-0203048v1
doc_title: "Towards a third-order topological invariant for magnetic ﬁelds"
section_id: sec-002-3-a-third-order-invariant-from-the-chern-simons
section_title: "A third-order invariant from the Chern-Simons three-for m"
section_number: 3
pages: 4-6
source_pdf: 0203048v1.pdf
source_sha256: 47204f32280e91a3
doc_brief: "Towards a third-order topological invariant for magnetic fields — An expression for a third-order link integral of three magne tic ﬁelds is presented."
---
In this section we construct a third-order invariant which, under c onditions speciﬁed
below, yields an invariant for three magnetic ﬁelds. The derivation is b ased on some
basic knowledge in diﬀerential geometry found e.g. in Frankel (1997 ).
We have noted before that equation (5) can be derived purely from the
homogeneous Maxwell equations. Written in diﬀerential forms it rea ds
d(A ∧ dA) = F ∧F, (9)
whereA is the one-form potential of the ﬁeld F . The right-hand side of this equation
is one of two (pseudo-) scalar Lorentz invariants that can be cons tructed from the
ﬁeld tensor. We can interpret this equation as a special case of a ge neral result in the
theory of Chern forms, namely the exactness of the second Cher n form
dtr(A ∧ dA −iq 2
3A ∧A ∧A) = tr(F ∧F ). (10)
In this equation A and F are a matrix valued one- and two-form. To be more precise
they take their values in the Lie-Algebra g of the structure group. In Yang-Mills
theory this is the symmetry group of the interaction under conside ration, with coupling
constant q. On the vector space g the trace deﬁnes a natural scalar product. For ω,
θ ∈ g, tr(ω ∧θ) = ωij ∧θji, where the indices denote matrix components.
Equation (10) holds for an arbitrary, not necessarily Abelian, ﬁeld s trength
F = dA −iqA ∧A. The three-form on the left-hand side is known as the Chern-
Simons three-form. For the case of electrodynamics, i.e. for the A belian structure
group U (1), F is given by F = dA, since A ∧A vanishes and equation (10) reduces
to (9). In the non-Abelian case equation (10) splits into a real and im aginary part
tr(dA ∧ dA) = d tr(A ∧ dA), (11)
2 tr(A ∧A ∧ dA) = d tr( 2
3A ∧A ∧A). (12)
As we will see in the following a third-order invariant can be derived fro m identity
(12) for the special case of the structure group SU (2).
Third-order topological invariant 5
Working with an SU (2) structure group it is appropriate to choose the Pauli
matrices σi, i=1, 2, 3, as a basis for the Lie Algebra su(2). All results, however, are
independent of this choice. The gauge potential A and ﬁeld strength F now have three
components
A =σiAi, F =σiF i, (13)
where the summation convention over repeated indices is assumed. Let us note that
in the following we will refer to these ﬁelds as Yang-Mills ﬁelds, although they do not
necessarily satisfy the Yang-Mills equation. Using the identities for P auli matrices
σjσk =iǫ jkl σl +δjk 1 and σjσkσl =iǫ jkl 1, (14)
equations (11) and (12) read
dAi ∧ dAi = d(Ai ∧ dAi), (15)
ǫijk dAi ∧Aj ∧Ak = 1
3 d(ǫijkAi ∧Aj ∧Ak). (16)
If we now interpret the three components of the Yang-Mills potent ial A as three
independent potentials of three electromagnetic ﬁelds F i
EM = dAi, the ﬁrst identity
states the helicity conservation (in IMHD) for the sum of the self-h elicities of the three
individual ﬁelds F i
EM , similar to the electrodynamic case. The second identity is new.
For convenience we introduce the two-form G1 = A2 ∧A3, here on IM4, and cyclic
permutations of it. Then we can write the second identity as
1
3 d(Ai ∧Gi) = F i
EM ∧Gi. (17)
To complete the analogy of this equation with equation (5) we have to rewrite it in
the language of three-vectors. Therefore we represent the on e-form Ai by the time
componentAi
0 and the three-vector Ai of the corresponding four-vector. The two-form
G1 is identiﬁed with the vector pair ( G1
E, G1
B) = (A3
0A2 −A2
0A3, A2 × A3), equivalent
to the identiﬁcation of FEM with the three-vector pair ( E,-B). Cyclic permutations
immediately lead to corresponding pairs for G2 andG3. Using these conventions, the
left- and right-hand side of equation (17) read respectively
1
3 d(Ai ∧Gi) = − 1
3
(
∂t(Ai · Gi
B) + ∇ · (Ai
0Gi
B + Ai × Gi
E)
)
vol4
= −
(
∂t(A1 · G1
B) + ∇ · (Ai
0Gi
B)
)
vol4
and
F i
EM ∧Gi = (Ei · Gi
B − Bi · Gi
E)vol4 = (Ei · Gi
B −Ai
0∇ · Gi
B)vol4.
Thus, identity (17) is equivalent to
∂t(A1 · G1
B) + ∇ · (Ai
0Gi
B) = −Ei · Gi
B +Ai
0∇ · Gi
B, (18)
which shows a similar structure as equation (5) in the case of helicity. It describes the
time evolution of the density A1 · A2 × A3 with its current Ai
0Gi
B and source term
−Ei · Gi
B +Ai
0∇ · Gi
B. This is the basis for the following theorem.
Theorem: Let B1, B2 and B3 be three magnetic ﬁelds with potentials Ai satisfying
Ei + v × Bi = 0. The integral over a volume V ⊂IR3
H (3)(B1, B2, B3) :=
∫
V
A1 · A2 × A3 d3x (19)
is a gauge invariant, conserved quantity, if
Third-order topological invariant 6
(i) the potentials obey ∇ · (Ai × Aj) = 0 for all i,j = 1, 2, 3,
(ii) the potentials obey the boundary condition Ai × n|∂V = 0 for n being the normal
vector to the boundary of the integration volume V .
Proof: Let us ﬁrst remark that condition (ii) of the theorem implies Bi · n|∂V = 0
as shown in Appendix A. It is therefore consistent with condition (i) s ince 0 =
(Bi · Aj − Ai · Bj)|∂V = ∇ · (Ai × Aj)|∂V . Moreover, we show in Appendix A that for
a simply connected volume with Bi · n|∂V = 0 condition (ii) can always be satisﬁed.
In order to prove the invariance of H (3) we observe that in an ideal dynamics equation
(18) can be written as
∂t(A1 · A2 × A3) + ∇ ·
(
v(A1 · A2 × A3)
)
=
∇ ·
( 1
3 v(Ai · Gi
B) −Ai
0Gi
B
)
+ (Ai
0 − Ai · v)∇ · Gi
B,
where the last term vanishes due to condition (i).
Integrating over the volume V yields the total time derivative of H (3) on the left-
hand side, while the right-hand side can be converted into a surface integral, analogous
to equation (8) in the case of helicity. The surface integral vanishe s since condition
(ii) of the theorem implies Gi
B = 0 on the boundary of the volume V . This, together
with the gauge invariance of H (3) shown in Appendix B, completes the proof.
