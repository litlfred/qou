---
doc_id: arxiv-q-alg-9707006v1
doc_title: "Drinfeld twist for quantum su(2) in the adjoint representation"
section_id: sec-011-52-quantum-symmetrization
section_title: "Quantum symmetrization"
section_number: 5.2
pages: 9-10
source_pdf: 9707006v1.pdf
source_sha256: b9513be9294f56d9
toc_source: inferred
doc_brief: "Drinfeld twist for quantum su(2) in the adjoint representation — We give a detailed description of the adjoint representation of Drinfeld’s twist element, as well as of its coproduct, for suq(2)."
---
Quantum symmetrization
We consider here the problem of quantum symmetrization of identical particle states. We supply, for reasons
of self-containment, a brief exposition of the relevant theory, along the lines of [7], which contains a thorough
discussion.
As a ﬁrst step towards the implementation of quantum group symmetries in quantum mechanics and quantum
ﬁeld theory, the question of the compatibility of Bose/Fermi statistics with quantum group actions ought to be
addressed. Consider, for concreteness, a two (identical) particle system in quantum mechanics. The Hilbert space
of the system is split into symmetric and antisymmetric subspaces, a division which is respected by the action
of classical Lie algebra generators. This latter fact is traced to the symmetry of the classical coproduct under
exchange of the two spaces, so that the classical permutation matrix P commutes with the representation of the
coproduct of the generators
[P, ρ⊗2(∆c(x))] = 0,
x ∈U(g),
where g is the Lie algebra under consideration and ρ the representation through which it acts on the one-particle
states. In the quantum case, the lack of cocommutativity implies that the quantum group action mixes the two
eigenspaces of P. The problem is rectiﬁed with the introduction of a quantum permutation operator P F , given
by conjugation by F of the classical one, i.e. P F = FPF −1. One easily shows that
[P F , ρ⊗2(∆(x))] = 0
x ∈Uq(g) ,
(38)
which guarrantees that quantum symmetric and antisymmetric states (deﬁned as eigenstates of P F ) remain such
after being acted upon by elements of Uq(g) (in the above equation, F is computed in ρ).
Specifying g, in the discussion above, to be su(2) and working in the representation ρr, we ﬁnd
SF = {1,
1
1 + q4
 
1
q2
q2
q4
!
,
1
1 + q4



q4 −q2 + 1
q3 −q
q2
q3 −q
q2
−q3 + q
q2
−q3 + q
q4 −q2 + 1


}
(39)
while
AF = {0,
1
1 + q4
 
q4
−q2
−q2
1
!
,
1
1 + q4



q2
−q3 + q
−q2
−q3 + q
(q2 −1)2
q3 −q
−q2
q3 −q
q2


}
(40)
where SF ≡F 1
2(1 + P)F −1 and AF ≡F 1
2(1 −P)F −1 are the quantum symmetrizer and antisymmetrizer
respectively. In the c-sector, SF and AF are equal to their classical counterparts. Clearly, SF 2 = SF (similarly
for AF ) and SF AF = 0.
For systems with more than two identical particles one proceeds along similar lines. The quantum permutation
matrix for adjacent spaces i, i + 1 is given by P F
i,i+1 = Fq12...nPi,i+1Fq
−1
12...n, where Pi,i+1 is the corresponding
classical permutation matrix and Fq12...n is the representation of (∆(n−1) ⊗id)F (diﬀerent choices for Fq12...n
are possible).
For example, for n = 3, Fq123 can be obtained from the crystal limit result of section 4 as
Fq123 = Fq0123F10
−1
