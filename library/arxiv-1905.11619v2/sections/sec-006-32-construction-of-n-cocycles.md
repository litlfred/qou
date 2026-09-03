---
doc_id: arxiv-1905.11619v2
doc_title: "L2-COHOMOLOGY, DERIVATIONS AND QUANTUM MARKOV SEMI-GROUPS ON q-GAUSSIAN ALGEBRAS"
section_id: sec-006-32-construction-of-n-cocycles
section_title: "Construction of n-cocycles."
section_number: 3.2
pages: 8-9
source_pdf: 1905.11619v2.pdf
source_sha256: f634f9ec4357d5f3
doc_brief: "L2-COHOMOLOGY, DERIVATIONS AND QUANTUM MARKOV SEMI-GROUPS ON q-GAUSSIAN ALGEBRAS — We study (quasi-)cohomological properties through an anal ysis of quantum Markov semi-groups."
---
expense of changing the bimodule. We will remedy this change by using Schatten-Sp properties
below.
Theorem 3.11. Let H be an A-A-bimodule and let f :A⊗(n−1) → H be a linear map. Set
Gf :A⊗n→ H∇ by,
(Gf )(a1⊗ . . .⊗ an) := a1⊗∇ f (a2⊗ . . .⊗ an)∈ H∇.
Then Gd + dG = 0 , where d’s are the diﬀerentials of the appropriate cochain complexe s. In par-
ticular, G maps cocycles to cocycles and coboundaries to coboundaries , so it induces a map on the
level of cohomology G∗ : H n(A, H)→ H n+1(A, H∇).
Proof. Let us ﬁrst compute G(d f). We have
d f(a1⊗···⊗ an) = a1f (a2⊗···⊗ an) +
n−1∑
k=1
(−1)kf (a1⊗···⊗ akak+1⊗···⊗ an)
+ (−1)nf (a1⊗···⊗ an−1)an,
hence
G(d f)(a0⊗···⊗ an) = a0⊗∇ a1f (a2⊗···⊗ an) +
n−1∑
k=1
(−1)ka0⊗∇ f (a1⊗···⊗ akak+1⊗···⊗ an)
+ (−1)na0⊗∇ f (a1⊗···⊗ an−1)an.
On the other hand:
−d(Gf )(a0⊗···⊗ an) =−a0(a1⊗∇ f (a2⊗···⊗ an)) + a0a1⊗∇ f (a2⊗···⊗ an)
+
n−1∑
k=1
(−1)ka0⊗∇ f (a1⊗···⊗ akak+1⊗···⊗ an)
+ (−1)na0⊗∇ f (a1⊗···⊗ an−1)an.
Note that
−a0(a1⊗∇ f (a2⊗···⊗ an)) =−a0a1⊗∇ f (a2⊗···⊗ an) + a0⊗∇ a1f (a2⊗···⊗ an).
It follows that G(d f) =−d(Gf ), i.e. dG + Gd = 0. □
Corollary 3.12. The map,
∂n :A⊗n→ L2(M )∇(n) : a1⊗ . . .⊗ an↦→a1⊗∇ . . .⊗∇ an⊗∇ Ω τ.
deﬁnes an n-cocycle, i.e. an element in C n(A, L2(M )∇(n) ).
Proof. For n = 1 we get ∂1(ab) = ab⊗∇ Ω τ = a· (b⊗∇ Ω τ ) + (a⊗∇ Ω τ)· b = a∂1(b) + ∂1(a)b and
so the corollary follows. For higher n use Theorem 3.11 inductively. □
