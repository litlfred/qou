This example constructs the rigid dualizing complex $\omega_A^\bullet$ for Bring's coordinate ring explicitly.

**Step 1: Identify the algebra.** Set $A = \mathcal{O}_q(\mathrm{SU}(2))$. As a $q$-deformation of a $3$-dimensional Lie group, $A$ is an Artin–Schelter regular algebra of global dimension $d = 3$.

**Step 2: Compute the dualizing complex.** For Artin–Schelter regular algebras of dimension $d$, the rigid dualizing complex is a shift of $A$ itself: $\omega_A^\bullet \cong A_\sigma[-3]$, where $A_\sigma$ denotes $A$ with bimodule structure twisted by the Nakayama automorphism $\sigma$.

**Step 3: Compute the Nakayama automorphism.** The Nakayama automorphism is determined by the modular element of the Haar state. On the generators:

$$
  \sigma(\alpha) = q^{-2}\alpha, \quad
  \sigma(\beta) = q^{2}\beta, \quad
  \sigma(\bar\alpha) = q^{2}\bar\alpha, \quad
  \sigma(\bar\beta) = q^{-2}\bar\beta.
$$

**Step 4: Verify the rigidifying isomorphism.** The rigid dualizing complex must satisfy $\omega_A^\bullet \simeq R\mathrm{Hom}_{A^e}(A, A^e)$ in $D(A^e)$. By Van den Bergh's theorem:

$$
  \mathrm{Ext}^i_{A^e}(A, A^e)
  = \begin{cases}
    A_\sigma & \text{if } i = 3, \\
    0 & \text{otherwise}.
  \end{cases}
$$

**Step 5: Van den Bergh duality.** For any finitely generated $A$-bimodule $M$, $\mathrm{Ext}^i_A(M, \omega_A^\bullet) \cong \mathrm{Tor}_{3-i}^A(M, A_\sigma)^\vee$.

On Bring's quantum observable universe, the dualizing complex encodes the Serre duality of the genus-$4$ curve. The Nakayama automorphism at $q = q_{\mathrm{Bring}}$ acts on the $8$ differentials by scaling with $q^{\pm 2}$, reflecting the $q$-deformed Hodge structure. The rigidity condition ensures this complex is intrinsic to Bring's curve.
