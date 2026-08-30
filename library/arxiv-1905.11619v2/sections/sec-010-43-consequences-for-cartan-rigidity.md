---
doc_id: arxiv-1905.11619v2
doc_title: "L2-COHOMOLOGY, DERIVATIONS AND QUANTUM MARKOV SEMI-GROUPS ON q-GAUSSIAN ALGEBRAS"
section_id: sec-010-43-consequences-for-cartan-rigidity
section_title: "Consequences for Cartan rigidity"
section_number: 4.3
pages: 16-17
source_pdf: 1905.11619v2.pdf
source_sha256: f634f9ec4357d5f3
doc_brief: "L2-COHOMOLOGY, DERIVATIONS AND QUANTUM MARKOV SEMI-GROUPS ON q-GAUSSIAN ALGEBRAS — We study (quasi-)cohomological properties through an anal ysis of quantum Markov semi-groups."
---
already obtained in an unpublished manuscript by Avsec [Avs 11], where they were proved for any
−1 < q < 1. Our cohomological properties in the next section are new h owever. Recall that we
assumed that dim( HR) <∞.
We recall that a von Neumann algebra M has the W ∗CMAP (weak-∗ complete metric approx-
imation property) if there exists a net Φ i : M→ M of completely contractive normal ﬁnite rank
maps such that for every x∈ M we have Φ i(x)→ x σ -weakly and lim sup i‖Φ i : M→ M‖cb = 1.
Theorem 4.15. For any HR and|q| ⩽ dim(H)− 1
2 the q-Gaussian algebra Γ q(HR) is strongly solid.
Proof. By [Avs11] we see that Γ q(HR) has the W ∗CMAP. In Corollary 3.12, we have constructed a
closable derivation ∂(= ∂1) :Aq→ L2(Γ q(HR))∇. This derivation is real by [Cas18, Lemma 3.10]
and proper as ∂∗∂ = ∆ and ∆ has compact resolvent. Further, by Theorem 4.14 we ﬁn d that
(Φ t)t≥0 is immediately gradient-S2 and gradientS2 if|q| < dim(H)− 1
2 .
In case|q| < dim(H)− 1
2 from Theorem 3.9 we see that the left and rightAq actions on L2(Γ q(HR))∇
extend to normal Γ q(HR) actions. Moreover, the thus-obtained Γ q(HR)-Γ q(HR) bimodule L2(Γ q(HR))∇
is weakly contained in the coarse bimodule of Γ q(HR). Then [OzPo10b, Corollary B] implies the
result except that we need a reformulation of [OzPo10b, Coro llary B] in terms of derivations instead
of cocycles; that version can be found in [Cas18, Appendix A] (even for stable normalizers).
For arbitrary|q|≤ dim(H)− 1
2 the proof follows in the same way using [Cas18, Proposition 4 .3]
instead of Theorem 3.9; one only needs to prove that the left a nd rightAq actions on L2(Γ q(HR))∇
extend to normal Γ q(HR) actions. We do this in Proposition 4.16. □
Proposition 4.16. The left and right Aq-actions on L2(Γ q(HR))∇ extend to commuting normal
Γ q-actions.
Proof. The proof follows [Cas18, Proposition 3.8]. We prove it for t he left action, the proof for the
right action is similar. We must show that the action is weakl y continuous on the unit ball. Take
elementary Wick operators a = Wq(ξ), b = Wq(η ), c = Wq(µ ), d = Wq(ν )∈A q. For ξ = ξ1⊗. . .⊗ξn
we refer to n as the length of Wq(ξ). Consider,
(4.7) ⟨x· a⊗∇ bΩ , c⊗∇ dΩ⟩ =− 1
2⟨d∗(∆( c∗xa) + c∗∆( x)a− ∆( c∗x)a− c∗∆( xa))bΩ , Ω⟩
Let x, a, b, c, d have length X, A, B, C, D respectively. The operator ∆ preserves the length of a
Wick word. Then using Lemma 4.3 we see that each of the express ions d∗∆( c∗xa)b, d∗c∗∆( xa)b,
d∗∆( c∗x)ab and d∗c∗∆( x)ab is a linear combination of Wick words of length at least X− A− B−
C− D. Therefore if X > A + B + C + D then (4.7) is 0. We therefore see that the map
(4.8) Aq→ C : x↦→⟨x· a⊗∇ bΩ , c⊗∇ dΩ⟩,
L2-COHOMOLOGY, DERIV ATIONS AND SEMI-GROUPS ON q-GAUSSIAN ALGEBRAS 17
factors through the normal projection P≤X : Γ q(HR)→ Γ q(HR) onto Wick words of length ≤ X.
The range of this projection is ﬁnite dimensional and contai ned in Aq. Hence (4.8) extends to a
normal map Γ q(HR)→ C.
Now let x∈ Γ q(HR) with ‖x‖≤ 1 and let xj∈ Γ q(HR) with‖xj‖≤ 1 be a net converging to x
weakly (Kaplansky’s density theorem). Let ξ, η∈ L2(Γ q(HR))∇ and let ξ0, η0 be in the linear span
of vectors of the form a⊗ bΩ with a, b∈A q as in the previous paragraph with ‖ξ− ξ0‖,‖η− η0‖ < ε.
Let j0 be such that for j > j 0 we have|⟨(x− xj)ξ0, η0⟩| < ε. Then,
|⟨(x− xj)ξ, η⟩|≤|⟨(x− xj)ξ0, η0⟩| +‖x− xj‖‖ξ− ξ0‖‖η0‖ +‖x− xj‖‖ξ‖‖η− η0‖
≤ε + 2ε‖η0‖ + 2ε‖ξ‖.
□
