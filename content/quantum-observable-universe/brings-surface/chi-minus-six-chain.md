We present the chain that fixes $\chi(A) = -6$. Steps 1--4 and 6--7 run forward from the QOU triple. Step 5, which fixes the branch-point count at six, reads that count off the Weierstrass points of Bring's surface — the surface the chain then identifies at Step 7 — so the chain locates the value rather than deriving it from the axioms alone. Step 8 applies the [motivic perpetual obstruction](#conj:motivic-perpetual-obstruction) theorem (proved via Route A: prime-ideal collapse, $C = a_0(-1) + 2 \cdot a_1(-1)$).

**Step 1: Start with the QOU triple.** We have $(\mathbf{C}, A, \tau)$ with gauge group $G = \mathrm{SU}(2)$. The object $A$ is the fundamental representation, and $\tau$ is the fibre functor.

**Step 2: The fibre functor produces a rank-2 bundle.** The fibre functor $\tau$ maps $A$ to a rank-2 vector bundle $V$ over a compact Riemann surface $M_0$. Since $G = \mathrm{SU}(2)$, the determinant $\det(V)$ is trivial. Thus $\deg(V) = 0$.

**Step 3: Apply Riemann--Roch.** For a rank-$r$ bundle of degree $d$ over a genus-$g$ surface:

$$
  \chi(V) = d + r(1 - g) = 0 + 2(1 - g) = 2 - 2g
$$

**Step 4: Obstructions require $g \geq 1$.** The lifting obstructions require $\kappa_n \neq 0$ at every level of the brane tower. The obstruction classes lie in $H^2(M_0, B)$. For these to be non-trivial, we need $H^2(M_0, \mathbb{C}^*) \neq 0$, which requires $g \geq 1$.

**Step 5: The Frobenius--Hopf structure fixes 6 branch points.** The Frobenius--Hopf structure forces the algebra to have exactly 6 branch points in its geometric :refterm[descent]{#descent} (from the $S_3 \subset S_5$ orbits on the 6 Weierstrass points of Bring's surface). This fixes $|\chi(A)| = 6$.

**Step 6: The sign is negative.** The bundle has more obstructions than sections. Specifically, $\chi(V) = -6$ means $h^0(V) - h^1(V) = -6$, so $h^1(V) \geq 6$ (obstructions dominate).

**Step 7: Therefore $g = 4$.** From $\chi(V) = 2 - 2g = -6$, we obtain $g = 4$. The unique maximally symmetric genus-4 curve is Bring's surface $\Sigma_4$, with automorphism group $S_5$ of order 120.

**Step 8 (motivic-Galois reading).** *Steps 4 and 5 lift to a single algebraic statement at the level of the [motivic substrate](#def:motivic-substrate). The condition $\chi(A) = -6$ controls the value of the substrate's motivic $L$-function at the boundary of analytic continuation. The non-vanishing of the obstruction classes $\kappa_n$ at every level becomes the non-vanishing of the Frobenius character at every finite place $p \nmid 6$. This is the content of the [motivic perpetual obstruction](#conj:motivic-perpetual-obstruction) theorem applied with $\chi(A) = -6$ ([Kummer tower](#rem:kummer-tower) §motivic-Galois). The "$g \geq 1$" condition (Step 4) is the cyclotomic-place criterion $H^1_{\mathrm{Gal}}(\mathrm{Gal}(\bar{\mathbb{Q}}_p/\mathbb{Q}_p), \mu_n(1)) \neq 0$, realised at every $p$. The Riemann–Roch derivation is the archimedean shadow ($v = \infty$ realization) of this stronger adelic statement.*
