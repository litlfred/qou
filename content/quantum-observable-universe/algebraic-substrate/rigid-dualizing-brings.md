Continuing the
[Bring coordinate ring](#def:brings-coordinate-ring), we construct
the [rigid dualizing complex](#def:rigid-dualizing-complex)
$\omega_A^\bullet$ explicitly — replacing "there exists a canonical
isomorphism" with a concrete computation.

**Step 1: identify the algebra.** Set
$A = \mathcal{O}_q(\mathrm{SU}(2))$, the quantum coordinate ring.
As a $q$-deformation of a $3$-dimensional Lie group, $A$ is an
Artin–Schelter regular algebra of global dimension $d = 3$.

**Step 2: compute the dualizing complex.** For Artin–Schelter
regular algebras of dimension $d$, the rigid dualizing complex is
a shift of $A$ itself:

$$
  \omega_A^\bullet \cong A_\sigma[-d]
$$

where $A_\sigma$ denotes $A$ with bimodule structure twisted by
the Nakayama automorphism $\sigma$, and $[-d]$ is the cohomological
shift by $d = 3$.

**Step 3: compute the Nakayama automorphism.** For
$\mathcal{O}_q(\mathrm{SU}(2))$, the Nakayama automorphism is
determined by the modular element of the Haar state
\cite{woronowicz1988}. On the
generators:

$$
  \sigma(\alpha) = q^{-2}\alpha, \quad
  \sigma(\beta) = q^{2}\beta, \quad
  \sigma(\bar\alpha) = q^{2}\bar\alpha, \quad
  \sigma(\bar\beta) = q^{-2}\bar\beta.
$$

This is the inner automorphism by the group-like element
$K^2 \in \mathcal{U}_q(\mathfrak{su}(2))$, where $K$ is the
Cartan generator satisfying $K\alpha K^{-1} = q^{-1}\alpha$.

**Step 4: verify the rigidifying isomorphism.** The rigid dualizing
complex must satisfy
$\omega_A^\bullet \simeq R\mathrm{Hom}_{A^e}(A, A^e)$
in $D(A^e)$. For Artin–Schelter regular $A$:

$$
  \mathrm{Ext}^i_{A^e}(A, A^e)
  = \begin{cases}
    A_\sigma & \text{if } i = d = 3, \\
    0 & \text{otherwise}.
  \end{cases}
$$

This is Van den Bergh's theorem applied to $\mathcal{O}_q(\mathrm{SU}(2))$.
The Ext computation uses the Koszul resolution of $A$ as an
$A^e$-module, which for the $3$-dimensional case has the form:

$$
  0 \to A^e \to (A^e)^3 \to (A^e)^3 \to A^e \to A \to 0.
$$

**Step 5: Van den Bergh duality.** For any finitely generated
$A$-bimodule $M$:

$$
  \mathrm{Ext}^i_A(M, \omega_A^\bullet)
  \cong H^{3-i}(M)^\vee
  = \mathrm{Tor}_{3-i}^A(M, A_\sigma)^\vee.
$$

This is Poincaré duality in the noncommutative setting.

**Bring's surface specialisation.** On Bring's QOU, the dualizing
complex $\omega_A^\bullet = A_\sigma[-3]$ encodes the Serre duality
of the genus-$4$ curve. The Nakayama automorphism $\sigma$ at
$q = q_{\mathrm{Bring}}$ acts on the $8$ holomorphic/anti-holomorphic
differentials of $\Sigma_4$ by scaling with $q^{\pm 2}$, reflecting
the $q$-deformed Hodge structure. The rigidity condition ensures this
complex is intrinsic to Bring's curve — independent of any choice of
embedding or coordinates.
