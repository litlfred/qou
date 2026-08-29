---
doc_id: arxiv-1905.11619v2
doc_title: "L2-COHOMOLOGY, DERIVATIONS AND QUANTUM MARKOV SEMI-GROUPS ON q-GAUSSIAN ALGEBRAS"
section_id: sec-005-3-gradient-tensoring-n-cocycles-and-gradient-sp
section_title: "Gradient tensoring, n-cocycles and gradient-Sp"
section_number: 3
pages: 5-8
source_pdf: 1905.11619v2.pdf
source_sha256: f634f9ec4357d5f3
doc_brief: "L2-COHOMOLOGY, DERIVATIONS AND QUANTUM MARKOV SEMI-GROUPS ON q-GAUSSIAN ALGEBRAS — We study (quasi-)cohomological properties through an anal ysis of quantum Markov semi-groups."
---
The aim of this section is to construct n-cocycles in Hochschild cohomology using quantum
Markov semi-groups.
Deﬁnition 3.1. A quantum Markov semi-group (Φ t)t≥0 on ( M, τ ) is a semi-group of unital
completely positive maps Φ t : M→ M that preserve the trace, i.e. τ◦ Φ t = τ for all t≥ 0. Further
we assume that Φ t is symmetric τ (Φ t(x)y) = τ (xΦ t(y)), x, y∈ M . Moreover, we assume that for
every x∈ M the map t↦→Φ t(x) is continuous for the strong topology of M .
3.1. Gradient tensoring. Let (Φ t)t≥0 be a quantum Markov semi-group on M . Let
Φ (2)
t : L2(M )→ L2(M ) : xΩ τ↦→Φ t(x)Ω τ ,
be the corresponding semi-group on L2(M ). Let ∆ ≥ 0 be its generator, i.e. ∆ is the unbounded
positive (self-adjoint) operator on L2(M ) such that
exp(−t∆) = Φ (2)
t
as a semi-group on L2(M ).
Assumption 1. We shall assume that there exists a σ-weakly dense∗-subalgebraA of M such that
AΩ τ is contained in the domain of ∆ and moreover ∆( AΩ τ)⊆A Ω τ. We simply write ∆( a), a∈A
for the map ∆ on the level of A. We assume moreover that for every a∈A the map t↦→Φ t(a) is
norm continuous. Let
A :=A
‖ · ‖
be the C ∗-closure of A. In general we cannot guarantee the existence of such an alge braA, but
in many concrete cases it exists. The assumption should be co mpared to similar assumptions and
remarks made in [CFL00, Section 5], [JuMe12] or [Cas18].
We introduce the following deﬁnition, which is in principle A-dependent. For p = 2 it was
introduced in [Cas18].
Deﬁnition 3.2. Let 1 ⩽ p ⩽ ∞. We say that a quantum Markov semi-group (Φ t)t≥0 is immedi-
ately gradient-Sp if for every a, b∈A and every t > 0 we have that
(3.1) Ψ a,b
t : x↦→−1
2 Φ t (∆( axb) + a∆( x)b− ∆( ax)b− a∆( xb)) ,
extends to a bounded map xΩ τ↦→Ψ a,b
t (x)Ω τ on L2(M ) that is moreover inSp. (Φ t)t≥0 is gradient-
Sp if for every a, b∈A the map (3.1) is in Sp for t = 0. We set Ψ a,b = Ψ a,b
0 .
Example 3.3. We illustrate Deﬁnition 3.2 by a simple (counter)example. S uppose that T is the
torus seen as the unit circle in C. Let ek(z) = zk, z∈ T. Let A be the span of ek, k∈ Z, i.e. the
∗-algebra of trigonometric polynomials. Set M = L∞(T).
• Let ∆ be the Laplacian given by ∆( ek) = k2ek which generates the heat semi-group
(e−t∆ )t≥0. This semi-group is not gradient- Sp for any 1 ≤ p≤∞ . Indeed, we ﬁnd that
Ψ el,e m(ek) =− 1
2 ((l + k + m)2 + k2− (l + k)2− (k + m)2)el+k+m =−lm el+k+m,
and this map is not even compact on L2(T) unless lm = 0.
6 MARTIJN CASPERS, YUSUKE ISONO, AND MATEUSZ W ASILEWSKI
• However, if we consider the Poisson semi-group (e−t∆
1
2
)t≥0 then we ﬁnd,
Ψ el,e m(ek) =− 1
2 (|l + k + m| +|k|−| l + k|−| k + m|)el+k+m,
which is 0 as soon as |k|≥| l| +|m|. Therefore Ψ el,e m is ﬁnite rank and therefore ( e−t∆
1
2
)t≥0
is gradient-Sp for every p∈ [1,∞].
Remark 3.4. Morally, one can expect that a quantum Markov semi-group is g radient-Sp if the
eigenvalues of the generator grow (almost) linearly (like f or the Poisson semi-group) and if there is
not too much interaction between the operators a and b in an expression axb if x has a very large
‘length’ (this obviously requires more structure to explai n in more detail). The current paper gives
quantitative examples of this, see Section 4 and Theorem B of Section 1. More examples as well as
stability properties for gradient-S2 for free products were given in [Cas18].
In [CiSa03] the following bimodule is constructed. We set th e gradient form (or carr´ e du
champ),
Γ( x, y) = 1
2 (∆( y)∗x + y∗∆( x)− ∆( y∗x)), x, y ∈A ,
which we view as an A-valued inner product. Let H be any A-A-bimodule. Equip the algebraic
tensor product A⊗ alg H with the (degenerate) inner product
⟨x⊗ ξ, y⊗ η⟩ =⟨Γ( x, y)ξ, η⟩, x, y ∈A , ξ, η∈ H.
The Hilbert space obtained by quotienting out the degenerat e part and taking the completion will
be called the gradient tensor product which we denote by H∇. We will denote by a⊗∇ ξ, a∈
A, ξ∈ H the class of a⊗ ξ in H∇. H∇ has anA-A bimodule structure given by the left action
(3.2) x· (y⊗∇ ξ) = xy⊗∇ ξ− x⊗∇ yξ, x, y ∈A , ξ∈ H,
and the right action
(3.3) ( y⊗∇ ξ)· x = y⊗∇ ξx, x, y ∈A , ξ∈ H.
Proposition 3.5. The left and right actions deﬁned in (3.2) and (3.3) are well-deﬁned contractive
left and right actions of A that moreover commute. That is, H∇ is an A-A-bimodule where A is
the C ∗-closure ofA.
Proof. The proof in case H = L2(M ) is the trivial M -M -bimodule is given as [CiSa03, Lemma
3.5]. But in fact the same proof works for any A-A-bimodule H. Note that the proof that the right
action is contractive is straightforward. □
Deﬁnition 3.6. We call (Φ t)t≥0 gradient coarse if the A-A-bimodule actions on L2(M )∇ extend
to normal M -M -bimodule actions and further L2(M )∇ is weakly contained in the coarse bimodule
of M .
By Proposition 3.5 for an A-A-bimodule H we may deﬁne
H∇(n) = ((H∇)∇ . . .)∇,
for the n-fold application of H ↦→H∇. The following connects the map (3.1) to the bimodule
structure deﬁned above.
Lemma 3.7. Let H be an A-A-bimodule. For x, y, a, b∈A and ξ, η∈ H we have,
⟨x· (a⊗∇ ξ)· y, b⊗∇ η⟩ =⟨Ψ b∗ ,a (x)ξy, η⟩.
L2-COHOMOLOGY, DERIV ATIONS AND SEMI-GROUPS ON q-GAUSSIAN ALGEBRAS 7
Proof. Indeed, we ﬁnd that,
⟨x· (a⊗∇ ξ)· y, b⊗∇ η⟩ =⟨(xa⊗∇ ξy− x⊗∇ aξy), b⊗∇ η⟩
=⟨(Γ( xa, b)− Γ( x, b)a)ξy, η⟩
= 1
2⟨(∆( b∗)xa + b∗∆( xa)− ∆( b∗xa)− ∆( b∗)xa− b∗∆( x)a + ∆( b∗x)a)ξy, η⟩
=⟨Ψ b∗ ,a (x)ξy, η⟩.
This concludes the proof. □
Remark 3.8. Let H be an A-A-bimodule and let ξ∈ H. Then the functional on A⊗max Aop
given by x⊗ yop↦→⟨xξy, ξ⟩ is positive and therefore also its restriction to A⊗alg Aop→ C sends
elements of the form x∗x with x∈ A⊗alg Aop to non-negative reals. Therefore if this map is ⊗min
continuous we obtain a positive map A⊗min Aop→ C.
For any n∈ N≥1, we say that a vector ξ∈ L2(M )∇(n) is algebraic if it is contained in a linear
span of elements of a0⊗∇ a1⊗∇···⊗ ∇ an for some a0, . . . , an∈A .
Theorem 3.9. Let n ∈ N≥1. Suppose that the quantum Markov semi-group Φ = (Φ t)t≥0 is
gradient-Sp for p = 2n.
Then for any algebraic ξ∈ L2(M )∇(n), AξA is contained in the coarse bimodule L2(M )⊗ L2(M )
as A-A bimodules. In particular, L2(M )∇(n) is contained in an inﬁnite multiple of the coarse
bimodule L2(M )⊗ L2(M ) as A-A bimodules and the A-A bimodule actions on L2(M )∇(n) extend
to normal M -M bimodule actions via this embedding.
Proof. Take a0, a1, . . . , an, b0, b1, . . . , bn∈A . Consider vectors α := a0⊗ . . .⊗ an−1⊗ anΩ τ, β :=
b0⊗ . . .⊗ bn−1⊗ bnΩ τ∈ L2(M )∇(n). For x, y∈A we get from Lemma 3.7 that,
⟨x· α· y, β⟩ =⟨x· (a0⊗∇ . . .⊗∇ an−1⊗∇ anΩ τ )· y, b0⊗∇ . . .⊗∇ bn−1⊗∇ bnΩ τ⟩
=⟨Ψ b∗
n− 1,a n− 1◦ . . .◦ Ψ b∗
1,a 1◦ Ψ b∗
0,a 0(x)anΩ τ y, bnΩ τ⟩
=⟨b∗
nΨ b∗
n− 1,a n− 1◦ . . .◦ Ψ b∗
1,a 1◦ Ψ b∗
0,a 0(x)anΩ τ , Ω τ y∗⟩
=⟨b∗
nΨ b∗
n− 1,a n− 1◦ . . .◦ Ψ b∗
1,a 1◦ Ψ b∗
0,a 0(x)anΩ τ , y∗Ω τ⟩,
where the last equality uses the fact that Ω τ y∗ = y∗Ω τ .
Since each Ψ b∗
j ,a j is an element of Sp with p = 2n we ﬁnd that
Ψ := Ψ b∗
n− 1,a n− 1◦ . . .◦ Ψ b∗
1,a 1◦ Ψ b∗
0,a 0∈S 2.
Then also xΩ τ↦→b∗
nΨ( x)anΩ τ is inS2. Therefore, there exists ζα,β ∈ L2(M )⊗ L2(M ) such that,
(3.4) ⟨x· α· y, β⟩ =⟨xΩ τ⊗ y∗Ω τ , ζα,β ⟩
Since the map M op ∋ yop ↦→y∗ ∈ M is a ∗-isomorphism, we deduce that assigning (3.4) to
x⊗ yop∈ M⊗alg M op is⊗min-bounded and moreover normal.
Now take any algebraic α ∈ L2(M )∇(n). The previous paragraph shows that the map ρ :
M⊗ M op : x⊗ yop→⟨ x· α· y, α⟩ extens to M⊗M op. Moreover, ρ is positive on A⊗ algAop→ C,
see Remark 3.8. We claim that ρ is also a positive map M⊗M op→ C. Indeed, take z∈ M⊗M op
positive and write z = d∗d, d∈ M⊗M op. By Kaplansky’s density theorem, let dj∈A⊗A op be
a bounded net converging strongly to d. Then d∗
j dj→ d∗d = z weakly and hence σ-weakly since
these topologies coincide on the unit ball. Since ρ is normal (i.e. σ-weakly continuous), we get
0≤ ρ(d∗
j dj)→ ρ(z). Since L2(M )⊗ L2(M ) is the standard Hilbert space for M⊗M op there exists
8 MARTIJN CASPERS, YUSUKE ISONO, AND MATEUSZ W ASILEWSKI
ζα ∈ L2(M )⊗ L2(M ) such that ⟨x· α· y, α⟩ =⟨x· ζα· y, ζα⟩. As algebraic vectors in L2(M )∇(n)
form a dense subspace, we conclude by Lemma 2.2. □
Corollary 3.10. Suppose that the quantum Markov semi-group (Φ t)t≥0 is gradient-S2; then it is
gradient coarse.
