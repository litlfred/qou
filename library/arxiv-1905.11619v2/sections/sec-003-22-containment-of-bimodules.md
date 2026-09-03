---
doc_id: arxiv-1905.11619v2
doc_title: "L2-COHOMOLOGY, DERIVATIONS AND QUANTUM MARKOV SEMI-GROUPS ON q-GAUSSIAN ALGEBRAS"
section_id: sec-003-22-containment-of-bimodules
section_title: "Containment of bimodules"
section_number: 2.2
pages: 3-4
source_pdf: 1905.11619v2.pdf
source_sha256: f634f9ec4357d5f3
doc_brief: "L2-COHOMOLOGY, DERIVATIONS AND QUANTUM MARKOV SEMI-GROUPS ON q-GAUSSIAN ALGEBRAS — We study (quasi-)cohomological properties through an anal ysis of quantum Markov semi-groups."
---
Hilbert space together with ∗-homomorphisms πl :A→ B(H) and πr :Aop→ B(H) whose images
commute. If A is a von Neumann algebra then we assume moreover that πl and πr are normal.
We write L2(M ) for the trivial bimodule and L2(M )⊗ L2(M ) for the coarse bimodule with the
usual left and right actions. Let H and K be M -M bimodules. We say that H is contained in K
if H is (isomorphic to) a sub-bimodule of K; i.e. H is a closed subspace of K that is invariant for
the bimodule actions of M . We say that H is quasi-contained in K if H is contained in ⊕i∈I H
for some index set I. We use Popa’s deﬁnition of weak containment [Popa].
Deﬁnition 2.1. Let M be a von Neumann algebra and let H and K be M -M -bimodules. We say
that H is weakly contained in K if for every ǫ > 0, every ﬁnite set F ⊆ M and every ξ∈ H
there exists ﬁnitely many ηj∈ K indexed by j∈ G such that for x, y∈ F ,
|⟨xξy, ξ⟩−
∑
j∈G
⟨xηjy, ηj⟩| < ε.
Notation H≼ K.
The following clariﬁes the connection to containment in the way we encounter it in this paper.
Lemma 2.2. Let M be a von Neumann algebra and A a σ-weakly dense ∗-subalgebra of M with
norm closure A. Let H be an A-A-bimodule and let K be an M -M -bimdoule. Suppose that there
4 MARTIJN CASPERS, YUSUKE ISONO, AND MATEUSZ W ASILEWSKI
exists a dense subspace D⊆ H such that for every ξ∈ D there exists an η∈ K such that for every
x, y∈A we have
⟨xξy, ξ⟩ =⟨xηy, η⟩.
Then for every ξ∈ D the sub-bimodule Hξ := AξA of H is contained in K as A-A bimodules.
Consequently, H is contained in a (possibly inﬁnite) direct sum of copies of K and further the A-A
bimodule actions on H extend to normal M -M -bimodule actions.
Proof. Take ξ∈ D. By assumption there exists η∈ K such that for all x, y∈A we have that
⟨xξy, ξ⟩ =⟨xηy, η⟩. Then set U : Hξ→ K by aξb↦→aηb where a, b∈A and it follows that this
map is isometric and intertwines the bimodule actions (of A and then by continuity of A).
Since U Hξ admits normal M -M bimodule actions, we can extend the A-A actions on Hξ to
normal M -M bimodule actions.
Let Σ be the set of all families of unit vectors ( ξi)i in H such that each Hξi := AξiA is a sub A-A
bimodule of K and that all Hξi are orthogonal with each other. By Zorn’s lemma, take a maxim al
element (ξi)i in Σ. Let Pi be the orthogonal projection onto Hξi and suppose by contradiction that
P := ∑
i Pi⁄= 1 H. Note that P commutes with A-A bimodule actions. Let ξ∈ D be such that
(1− P )ξ⁄= 0 and ﬁx η∈ K such that⟨aξb, ξ⟩ =⟨aηb, η⟩. Then observe that for all ﬁnitely many
ai, bi∈A ,
‖
∑
i
ai(1− P )ξbi‖ =‖(1− P )
∑
i
aiξbi‖ ⩽ ‖
∑
i
aiξbi‖ =‖
∑
i
aiηbi‖.
One can deﬁne a contraction v : AηA→ A(1− P )ξA by v(aηb) = a(1− P )ξb for a, b∈A . Then
since v∗v commutes with A-A bimodule actions, if we put η′ := (v∗v)1/ 2η, then it satisﬁes
⟨a(1− P )ξb, (1− P )ξ⟩ =⟨aη′b, η′⟩, for any a, b∈A .
This contradicts the maximality of ( ξi)i. We conclude that there is an A-A bimodule embedding
H =
⨁
i
Hξi⊂
⨁
i
K
and we can extend the A-A actions to normal M -M bimodule actions via this embedding. □
