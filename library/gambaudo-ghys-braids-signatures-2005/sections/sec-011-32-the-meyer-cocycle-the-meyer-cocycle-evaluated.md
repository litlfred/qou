---
doc_id: gambaudo-ghys-braids-signatures-2005
doc_title: "Braids and signatures"
section_id: sec-011-32-the-meyer-cocycle-the-meyer-cocycle-evaluated
section_title: "The Meyer cocycle. — The Meyer cocycle evaluated on a pair of"
section_number: 3.2
pages: 17-19
source_pdf: gambaudo-ghys-braids-signatures-2005.pdf
source_sha256: 647f4c28cab7428d
doc_brief: "Braids and signatures — 62 sections: Introduction; (v1) −v1 =v2 −γ 2(v2) and deﬁne; (α,β ) which is a 2-fold branched"
---
elements in Sp(2g, R) is also related to the signature of 4-manifolds as follows.
Let P be the oriented pair of pants (the oriented 2-sphere minus th ree discs)
and W 4 a 4-manifold which is an oriented ﬁbration over P whose ﬁber is a
closed oriented surface F with genus g (the orientation on M is induced by the
orientations on P and F ).
It turns out that the signature of the oriented manifold W 4 only depends on
the monodromy maps on the ﬁrst homology group H1(F ; R) of the surface F .
The intersection form on H1(F ; R) is a symplectic form which is invari-
ant under the action induced by homeomorphisms of F . Thus we can iden-
tifyH1(F ; R) (equipped with the intersection form) to R2g (equipped with the
standard symplectic form). This allows us to associate with each loop on the
pair of pants P (based at some base point in P ) an element in Sp(2g, R).
τ
1
τ
2
P
Figure 9. Pair of pants
The homology ofW 4 can be computed from the associated spectral sequence.
Consider the E2
1, 1 term of this spectral sequence, i.e. the ﬁrst homology group
H1(P ;H1(F ; R)). The skew symmetric intersection on this homology
H1
(
P ;H1(F ; R)
)
⊗H1
(
P ;H1(F ; R)
)
− →H1(F ; R) ⊗H1(F ; R)
followed by the skew-symmetric intersection form on the coe ﬃcient module
H1(F ; R) ⊗H1(F ; R) − → R
produces a real quadratic form q on H1(P ;H1(F ; R)). Meyer shows in [9]
that the signature of W 4 is equal to the signature of this quadratic form q,
which amounts to showing that the other terms in the spectral sequence do not
contribute to the signature of W 4. In turn, the signature of q can be easily
computed from γ 1 and γ 2. Meyer’s Theorem is the following:
Theorem 3.2 (Meyer). — Let γ 1 and γ 2 be the two elements in Sp(2g, R)
respectively induced by the two generators τ 1 and τ 2 of the fundamental group
BULLETIN DE LA SOCI ´ET´E MATH ´EMATIQUE DE FRANCE
558 GAMBAUDO (J.-M.) & GHYS (E.)
π 1(P ) ( see Figure 9). The signature σ (W 4) of the oriented manifold W 4 is
given by the evaluation of the Meyer cocycle on the pair (γ 1,γ 2):
σ (W 4) = Meyer(γ 1,γ 2).
This fact is all we need for the proof of Theorem A and the reade r might skip
the rest of this subsection. However, we believe that it is us eful to give a more
conceptual deﬁnition of Meyer cocycle and its relationship with the signatures
of ﬁbrations over a pair of pants.
We ﬁrst show that Meyer Theorem 3.2 follows from Novikov-Wal l Theorem.
If one splits the pair of pants in two halves as in Figure 10, th e manifold W
appears as the union of two 4-manifolds glued along part of th eir boundaries,
as discussed above. Each one of the two pieces has a signature equal to 0 since
they are both homeomorphic to the product of a 3-manifold by a n interval.
One is therefore led to evaluate the defect δ in this situation. In this case, the
surface Σ consists of two copies of F and the three corresponding Lagrangian
subspaces of H1(F ; R) ⊕ H1(F ; R) are the graphs of the identity, and of the
actions of the two given diﬀeomorphisms in homology. The deﬁ nition of Maslov
ternary index δ reduces precisely to the deﬁnition of the Meyer cocycle that
we gave in the introduction and we get indeed Meyer Theorem fr om Novikov-
Wall Theorem.
W
F
F
Figure 10. Splitting a pair of pants
We can at last give the ﬁnal deﬁnition of Meyer cocycle.
Given a symplectic automorphism γ of some symplectic vector space ( E, Ω),
its graph
Graph(γ ) =
{
(x,γ (x))
}
⊂ E ×E
is a Lagrangian subspace of E × E equipped with the symplectic structure
Ω ⊕ − Ω. Hence, if we are given three symplectic automorphisms γ 1,γ 2,γ 3,
we can consider the Maslov ternary index
meyer(γ 1,γ 2,γ 3) of (Graph(γ 1), Graph(γ 2), Graph(γ 3)).
This deﬁnes a 2-cocycle in the homogeneous bar resolution si nce obviously
meyer(γ 1,γ 2,γ 3) = meyer(γγ 1γ ′,γγ 2γ ′,γγ 3γ ′) for every γ,γ ′in the symplectic
group of (E, Ω). The associated inhomogeneous cocycle is
Meyer(γ 1,γ 2) = meyer(id,γ 1,γ 1γ 2) = meyer(γ − 1
1 , id,γ 2).
tome 133 – 2005 – n o 4
BRAIDS AND SIGNATURES 559
Going back to the deﬁnition of the Maslov ternary index, one s ees that in
order to compute Meyer( γ 1,γ 2), one should consider the space of triples
(v1,γ − 1
