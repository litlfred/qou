**Algorithm (Symmetric Frobenius pairing on the Frobenius–Hopf aether and $H_n(q)$).**
*Evaluate the symmetric bilinear Frobenius pairing $\langle a, b \rangle_F = \mathrm{tr}_M(a b)$ induced from the [Frobenius–Hopf aether](#def:frobenius-hopf-substrate) $A$ onto $H_n(q)$, assemble the Coxeter Gram matrix $G_{u,v}(q)$, and certify involutive self-duality $\Psi = S^2 = \mathrm{id}$.*

### Input

- *Normal-form elements $a = \sum_{u \in S_n} a_u(q)\,T_u$ and $b = \sum_{v \in S_n} b_v(q)\,T_v$ in $H_n(q)$ (from [Step 2](#alg:gs-reduce-to-hecke-nf)).*
- *Markov trace functional $\mathrm{tr}_M \colon H_n(q) \to \mathbb{Q}(q)$ (from [Step 3](#alg:markov-trace), or GPMT-completed on higher-row ideals via [Step 5](#alg:wedderburn-decomposition)).*

### Output

- *Symmetric bilinear pairing value $\langle a, b \rangle_F \in \mathbb{Q}(q)$ and $n! \times n!$ Gram matrix $G_{u,v}(q) = \mathrm{tr}_M(T_u T_v)$.*
- *Algebraic verification of antipode involutivity $S^2(T_u) = T_u$ for all $u \in S_n$.*

### Algorithm

1. **Assemble the basis Gram matrix:** For each pair $(u, v) \in S_n \times S_n$ with $u \le v$ in shortlex order, reduce the product $T_u T_v$ to normal form via [Step 2](#alg:gs-reduce-to-hecke-nf), evaluate $G_{u,v}(q) = \mathrm{tr}_M(\mathrm{NF}(T_u T_v))$ via [Step 3](#alg:markov-trace), and set $G_{v,u}(q) = G_{u,v}(q)$ by trace cyclicity.
2. **Evaluate the bilinear form:** Compute $\langle a, b \rangle_F = \sum_{u, v \in S_n} a_u(q)\,G_{u,v}(q)\,b_v(q) \in \mathbb{Q}(q)$.
3. **Verify antipode involutivity:** Under the anti-automorphism $S(T_{s_i}) = T_{s_i}^{-1} = T_{s_i} - h \cdot 1$ (with bar twist $q \mapsto q^{-1}$ sending $h \mapsto -h$), apply $S$ twice to $T_u = T_{s_{i_1}} \cdots T_{s_{i_k}}$: order reversal applied twice restores $(s_{i_1}, \dots, s_{i_k})$ while $S(T_{s_i}^{-1}) = T_{s_i}$, certifying $\Psi(T_u) = S^2(T_u) = T_u$.

### Termination and Complexity

Once the symmetric $n! \times n!$ Gram matrix $G(q)$ is precomputed in $O((n!)^2)$ normal-form multiplications, each bilinear pairing $\langle a, b \rangle_F$ requires $O(|\mathrm{supp}(a)|\,|\mathrm{supp}(b)|)$ operations in $\mathbb{Q}(q)$, and antipode verification requires $O(n!)$ basis checks.

### Mathematical Justification

1. **Existence, symmetry, and uniqueness:** On the [Frobenius–Hopf aether](#def:frobenius-hopf-substrate) $A$, the categorical integral $\int_A \circ\,\mu$ defines a symmetric non-degenerate [Frobenius pairing](#def:frobenius-pairing) whose existence and scalar uniqueness are proved in [Frobenius-pairing existence](#prop:frobenius-pairing-exists) and [Frobenius-pairing uniqueness](#prop:frobenius-pairing-unique).
2. **Antipode and Gram positivity:** Involutive self-duality $S^2 = \mathrm{id}$ is established in [Frobenius antipode unification](#thm:frobenius-antipode-unifies-chirality-and-tower); on the two-row support at $q > 0$, positive definiteness of $G(q)$ supplies the convex cone of the confinement program in [Step 10](#alg:confinement-sdp).
