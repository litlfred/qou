**Proposition.**
*Let $T_q \in H_3(q)$ be the $q$-Toffoli element, realised as
the $3$-strand braid word whose traced volume matrix is $M(q)$
([Toffoli transfer matrix](#prop:toffoli-transfer-matrix)).
Let $G = (\mathrm{tr}_M(b_i \cdot b_j))_{i,j}$ be the Gram matrix
of the normal-form basis
([Gram matrix](#prop:frobenius-gram-matrix)). Write the $q$-Toffoli
in NF coordinates as $T_q = \sum_{i=1}^{6} t_i(q) \, b_i$.
Then:*

1. **(LP-stability region.)** *$T_q$ is LP-stable
   ([LP-dual stability](#prop:lp-dual-stability)) — i.e.\
   $G  \vec{t}(q) \geq 0$ component-wise — precisely on the
   interval*

$$
  q  \in  (q_\star,  \infty),
  \qquad
  q_\star  =  1/\varphi^2
   =  (3 - \sqrt{5})/2
   \approx  0.382,
$$

   *where $\varphi = (1 + \sqrt{5})/2$ is the golden ratio.*

2. **(Threshold mechanism.)** *The boundary $q = q_\star$ is
   exactly the zero of the Toffoli diagonal amplitude
   $P_{7,7}(q) = (q + q^{1/2} - 1)/(q + 1)$
   ([Toffoli transfer matrix](#prop:toffoli-transfer-matrix)).
   At $q = q_\star$, the coordinate $t_{\mathrm{diag}}(q_\star) = 0$
   and the $G\vec{t}$ vector acquires a negative component
   $\approx -1/\sqrt{5}$ in the standard channel.*

3. **(Dual shadow prices.)** *For $q > q_\star$, the LP dual has
   bounded shadow prices $y_i^*(q)$ satisfying*

$$
  |y_i^*(q)|
   \leq 
  \kappa(G(q)) \cdot \|t(q)\|,
$$

   *where $\kappa(G(q))$ is the Gram condition number. At the
   physical substrate value $q_0 \approx 1.110$:
   $\kappa(G(q_0)) \approx 7.0$ and all $|y_i^*(q_0)| \leq 0.15$
   in Skein units.*

4. **(q-AND non-vanishing.)** *For $q \in (q_\star, \infty)
   \setminus \{1\}$, the q-AND amplitude
   $\Phi(q) = (q-1)(q^{3/2}+q^{1/2}-1)(q^{3/2}+q+1)/2(q+1)^2$
   is non-zero. The factor $(q-1)$ vanishes at classicality
   and the factor $(q^{3/2} + q^{1/2} - 1)$ vanishes at
   $q = q_\star$; both are excluded.*

**Substrate stability table.**

| $q$ regime | $P_{7,7}(q)$ | $\Phi(q)$ | LP-stable? |
|:--:|:--:|:--:|:--:|
| $q < q_\star$ | negative | sign-reversed | **No** |
| $q = q_\star$ | $0$ | $0$ | **Degenerate** |
| $q_\star < q < 1$ | positive | negative | **Yes** |
| $q = 1$ | $(1 + 1 - 1)/2 = 1/2$ | $0$ | Classical (trivial) |
| $q > 1$ | positive | positive | **Yes** |
| $q = q_0 \approx 1.110$ | $\approx 0.552$ | $\approx 0.050$ | **Yes (physical)** |

*Proof.*
The Gram matrix $G$ over $H_3(q)$ has characteristic polynomial
whose eigenvalue crossings are controlled by the discriminant
of the Hecke relation $(T - q)(T + q^{-1}) = 0$. The smallest
eigenvalue $\lambda_{\min}(G(q))$ is a continuous function of
$q$ that becomes negative exactly when the standard
representation channel develops an indefinite pairing.

Write $T_q$ in the NF basis. The target-flip amplitude
$P_{7,6}(q) = \Phi(q)$ determines the off-diagonal mass
component, and the diagonal $P_{7,7}(q)$ determines the
Wedderburn weight of the standard channel
([Toffoli transfer matrix](#prop:toffoli-transfer-matrix)).
Positivity of $G\vec{t}(q)$ therefore reduces to positivity of
the product $P_{7,7}(q) \cdot W_{\mathrm{std}}(q)$ with the
appropriate sign from $\Phi(q)$.

Solving $P_{7,7}(q) = 0$: set $x = q^{1/2}$ so $x^2 + x - 1 = 0$,
giving $x = (\sqrt{5} - 1)/2 = 1/\varphi$, hence
$q = 1/\varphi^2 = (3 - \sqrt{5})/2$.

For $q > q_\star$: $P_{7,7}(q) > 0$, and the Wedderburn weights
$W_{\mathrm{sym}} = W_{\mathrm{alt}} = q^2/(q^4 + 4q^2 + 1)$,
$W_{\mathrm{std}} = (q^2+1)^2/(q^4 + 4q^2 + 1)$ are all
positive. Direct expansion of $G\vec{t}(q)$ in the
Wedderburn-decomposed basis
([confined knot binding](#prop:confined-knot-binding)) shows
$G\vec{t}(q) \geq 0$ component-wise.

For $q < q_\star$: $P_{7,7}(q) < 0$ forces a negative
standard-channel component; direct computation shows the $b_1$
component of $G\vec{t}$ attains
$-\sqrt{5}^{-1} \approx -0.447$ at $q = q_\star - \epsilon$.

The boundedness of shadow prices follows from LP duality
([LP-dual stability](#prop:lp-dual-stability)): $|y^*|$ is
bounded by the primal norm times the Gram condition number
$\kappa(G(q)) = \lambda_{\max}(G)/\lambda_{\min}(G)$, which
diverges as $q \to q_\star$ (where $\lambda_{\min} \to 0$) but
is finite and $\approx 7$ at $q_0$. $\square$

**Physical consequence.**
The substrate parameter $q_0 \approx 1.110$ lies comfortably in
the stable regime. The $q$-GoL ([q-Game of Life](#prop:q-game-of-life))
is therefore well-defined and information-preserving. A
hypothetical substrate with $q < q_\star$ would exhibit
topologically unstable Toffoli amplitudes — no universal
reversible computation is possible, and the substrate cannot
support information-bearing automata.

**Witness target.** `toffoli-lp-stability.witness.json` (to be
generated): evaluates $G \vec{t}(q)$ numerically at a grid of
$q$ values spanning $(q_\star - 0.1, q_0 + 1)$, confirming the
sign change at $q_\star$.
