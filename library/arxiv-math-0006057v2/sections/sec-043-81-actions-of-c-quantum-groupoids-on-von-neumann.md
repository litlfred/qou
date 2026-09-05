---
doc_id: arxiv-math-0006057v2
doc_title: "FINITE QUANTUM GROUPOIDS AND THEIR APPLICA TIONS"
section_id: sec-043-81-actions-of-c-quantum-groupoids-on-von-neumann
section_title: "Actions of C∗-quantum groupoids on von Neumann algebras. Let a"
section_number: 8.1
pages: 32-34
source_pdf: 0006057v2.pdf
source_sha256: c881434fe9f4b04f
doc_brief: "FINITE QUANTUM GROUPOIDS AND THEIR APPLICA TIONS — W e give a survey of the theory of ﬁnite quantum groupoids (wea k Hopf algebras), including foundations of the theory and app lications to ﬁnite"
---
von Neumann algebra M be a left H-module algebra in the sense of Deﬁnition 4.1.1
via a weakly continuous action of a C∗-quantum groupoid
H ⊗CM ∋x ⊗m ↦→(x⊲m ) ∈M
such that (x⊲m )∗ =S(x)∗⊲m ∗ and x⊲ 1 = 0 iﬀ εt(t) = 0.
Then one can show ([NSzW], 3.4.2) that the smash product algebra (n ow we
call it crossed product algebra and denote by M>⊳H), equipped with an involution
[m ⊗x]∗ = [(x∗
(1)⊲m ∗) ⊗x∗
(2)], is a von Neumann algebra.
The collection M H = {m ∈M |x⊲m =εt(x)⊲m, ∀x ∈H} is a von Neumann
subalgebra of M , called a ﬁxed point subalgebra . The centralizer M ′ ∩M>⊳H
always contains a the source counital subalgebra Hs. Indeed, if y ∈ Hs, then
∆( y) = 1 (1) ⊗ 1(2)y, therefore
[1 ⊗y][m ⊗ 1] = [( y(1)⊲m ) ⊗y(2)] = [(1 (1)⊲m ) ⊗ 1(2)y]
= [ m ⊗y] = [m ⊗ 1][1 ⊗y],
for any m ∈ M , and Hs ⊂ M ′ ∩M>⊳H. An action of H is called minimal if
Hs =M ′ ∩M>⊳H.
One can deﬁne the dual action of ˆH on the von Neumann algebra M>⊳H as in
(24) and construct the von Neumann algebra ( M>⊳H)>⊳ˆH.
Remark 8.1.1. The following results hold true if S2 = id, i.e., if H is involutive
([N1], 4.6, 4.7).
(a) M ⊂M>⊳H ⊂ (M>⊳H)>⊳ˆH is a basic construction;
(b) M>⊳H is free as a left M -module;
(c) (M>⊳H)>⊳ˆH ∼=M ⊗CMn(C) for some integer n.
Example 8.1.2. For a trivial action of H onHt and the corresponding dual action
of ˆH onH ∼=Ht>⊳H (see Example 4.1.3 (i) and (ii)), Ht ⊂H ⊂H>⊳ˆH is the basic
construction of ﬁnite-dimensional C∗-algebras with respect to the Haar conditional
expectation Et ([BSz2], 4.2).
IfH is a connected C∗-quantum groupoid having a minimal action on a II 1 factor
M then one can show ([NSzW], 4.2.5, 4.3.5) that ˆH is also connected and that
N =M H ⊂M ⊂M1 =M>⊳H ⊂M2 = (M>⊳H)>⊳ˆH ⊂ · · ·
is the Jones tower of factors of ﬁnite index with the derived tower
N ′ ∩N = C ⊂N ′ ∩M =Ht ⊂N ′ ∩M1 =H ⊂N ′ ∩M2 =H>⊳ˆH ⊂ · · ·
FINITE QUANTUM GROUPOIDS AND THEIR APPLICA TIONS 33
The fact that the last triple of ﬁnite-dimensional C∗-algebras is a basic construc-
tion, means exactly that the subfactor N ⊂M has depth 2. Moreover, the ﬁnite-
dimensional C∗-algebras
H ∗ ⊂ H ∗>⊳H
∪ ∪
Ht =H ∗
s ⊂ H,
(65)
form a canonical commuting square , which completely determines the equivalence
class of the initial subfactor. This implies that any biconnected C∗-quantum group-
oid has at most one minimal action on a given II 1 factor and thus corresponds to
no more than one (up to equivalence) ﬁnite index depth 2 subfactor .
Remark 8.1.3. It was shown in ([N1], 5) that any biconnected involutiveC∗-quantum
groupoid has a minimal action on the hyperﬁnite II 1 factor. This action is con-
structed by iterating the basic construction for the square (65) in the horizontal
direction, see [N1] for details.
8.2. Construction of a C∗-quantum groupoid from a depth 2 subfactor.
Let N ⊂M be a ﬁnite index ([ M :N ] = λ−1) depth 2 II 1 subfactor and
N ⊂M ⊂M1 ⊂M2 ⊂ · · ·(66)
the corresponding Jones tower, M1 = ⟨M, e1⟩, M2 = ⟨M1, e2⟩,..., where e1 ∈
N ′ ∩M1, e2 ∈ M ′ ∩M2, · · · are the Jones projections. The depth 2 condition
means that N ′ ∩M2 is the basic construction of the inclusion N ′ ∩M ⊂N ′ ∩M1.
Let τ be the trace on M2 normalized by τ (1) = 1.
Let us denote
A =N ′ ∩M1, B =M ′ ∩M2, B t =M ′ ∩M1, B s =M ′
1 ∩M2
and let Tr be the trace of the regular representation of Bt on itself. Since both
τ and Tr are non-degenerate, there exists a positive invertible eleme ntw ∈Z(Bt)
such that τ (wz) = Tr (z) for all z ∈Bt (the index of τ |M ′∩M1 in the sense of [W]).
Proposition 8.2.1. There is a canonical non-degenerate duality form between A
and B deﬁned by
⟨a, b⟩ =λ−2τ (ae2e1wb) = λ−2TrE Bt (bae2e1),(67)
for all a ∈A and b ∈B.
Proof. If a ∈A is such that ⟨a, B⟩ = 0 , then, using [PP1], 1.2, one has
τ (ae2e1B) = τ (ae2e1(N ′ ∩M2)) = 0,
therefore, using the properties of τ and Jones projections, we get
τ (aa∗) = λ−1τ (ae2a∗) = λ−2τ (ae2e1(e2a∗)) = 0,
so a = 0. Similarly for b ∈B.
Using the duality ⟨a, b⟩, one deﬁnes a coalgebra structure on B :
⟨a1 ⊗a2, ∆( b) ⟩ = ⟨a1a2, b⟩,(68)
ε(b) = ⟨1, b⟩,(69)
for all a,a 1,a 2 ∈A and b ∈B. Similarly, one deﬁnes a coalgebra structure on A.
We deﬁne a linear endomorphism SB :B →B by
EM1 (be1e2) = EM1 (e2e1SB(b)),(70)
34 DMITRI NIKSHYCH AND LEONID V AINERMAN
Note that τ ◦SB =τ . Similarly one can deﬁne a linear endomorphism SA :A →A
such that EM ′ (SA(a)e2e1) = EM ′ (e1e2a) and τ ◦SA =τ .
Proposition 8.2.2. ([NV2], 4.5, 5.2): The following identities hold :
(i) SB(Bs) = Bt,
(ii) S2
B(b) = b and SB(b)∗ =SB(b∗),
(iii) ∆( b)(SB(z) ⊗ 1) = ∆( b)(1 ⊗z), ∆( bz) = ∆( b)(z ⊗ 1), (∀z ∈Bt),
(iv) SB(bc) = SB(c)SB(b),
∆( SB(b)) = (1 ⊗w−1)(SB(b(2)) ⊗SB(b(1)))(SB(w) ⊗ 1).
Deﬁne an antipode and new involution of B by
S(b) = SB(wbw−1), b † =S(w)−1b∗S(w).(71)
Theorem 8.2.3. With the above operations B becomes a biconnectedC∗-quantum
groupoid with the counital subalgebras Bs and Bt.
Proof. One can check ([NV2], 4.6) that ∆(1) ∈Bs ⊗Bt, hence, since ∆(1) ∈Bs ⊗Bt
and Bt commutes with Bs, we have
(id ⊗ ∆)∆(1) = 1 (1) ⊗ ∆(1)(1 (2) ⊗ 1)
= (1 ⊗ ∆(1))(∆(1) ⊗ 1) = (∆(1) ⊗ 1)(1 ⊗ ∆(1))
which is axiom (1) of Deﬁnition 2.1.1. The axiom (2) dual to it is obtained s imilarly,
considering the comultiplication in A.
As a consequence of the “symmetric square” relations BM1 = M1B = M2 one
obtains ([NV2], 4.12) the identity
bx =λ−1EM1 (b(1)xe2)b(2) for all b ∈B, x∈M1,(72)
from where it follows that
EM1 (bxye2) = λ−1EM1 (b(1)xe2)EM1 (b(2)ye2) for all b ∈B, x,y ∈M1.(73)
We use this identity to prove that ∆ is a homomorphism :
⟨a1a2, bc⟩ = ⟨λ−1EM1 (ca1a2e2), b⟩
= ⟨λ−2EM1 (c(1)a1e2)EM1 (c(2)a2e2), b⟩
= ⟨λ−1EM1 (c(1)a1e2),b (1) ⟩⟨λ−1EM1 (c(2)a2e2), b(2) ⟩
= ⟨a1, b(1)c(1) ⟩⟨a2, b(2)c(2) ⟩,
for all a1,a 2 ∈A, whence ∆( bc) = ∆( b)∆( c). Next,
⟨a, ε(1(1)b)1(2) ⟩ = ⟨1, 1(1)b ⟩⟨a, 1(2) ⟩
= ⟨λ−1EM1 (be2), 1(1) ⟩⟨a, 1(2) ⟩
= ⟨λ−1EM1 (be2)a, 1 ⟩ = ⟨a, λ−1EM1 (be2) ⟩,
therefore εt(b) = λ−1EM1 (be2) (similarly, εs(b) = λ−1EM ′
