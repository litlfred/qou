*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Proposition.**
*Let $T_q \in H_3(q)$ be the $q$-Toffoli element, realised as
the $3$-strand braid word whose traced volume matrix is $M(q)$
([Toffoli transfer matrix](#prop:toffoli-transfer-matrix)).
Let $G = (\mathrm{tr}_M(b_i \cdot b_j))_{i,j}$ be the Gram matrix
of the normal-form basis
([Gram matrix](#prop:frobenius-gram-matrix)). Write the $q$-Toffoli
in NF coordinates as $T_q = \sum_{i=1}^{6} t_i(q) \, b_i$.
Then:*

1. **(Stability region.)** *The $q$-Toffoli element is LP-stable
   ([LP-dual stability](#prop:lp-dual-stability)) — all Hecke
   amplitudes have the correct sign and the confinement LP
   ([confinement as LP](#prop:confinement-lp)) is feasible — on
   the **physical regime** $q > 1$. Three operator zeros in
   $(0, \infty)$ delimit the sub-physical behaviour:*

$$
  q_\star \,=\, 1/\varphi^2 \,=\, (3 - \sqrt{5})/2 \,\approx\, 0.3820,
  \qquad
  q_\Phi \,\approx\, 0.4656,
  \qquad
  q \,=\, 1,
$$

   *where $\varphi = (1 + \sqrt{5})/2$ is the golden ratio.*

2. **(Three operator thresholds.)** *Each zero corresponds to a
   different Hecke amplitude vanishing:*

See [Table 1](#tbl:toffoli-lp-stability-table1-data).

   *At $q_\star$ the diagonal amplitude $P_{7,7}$ vanishes; at
   $q_\Phi$ the q-AND amplitude $\Phi$ reverses sign; at $q = 1$
   the q-AND vanishes (classical reversible Toffoli has trivial
   amplitude).*

3. **(Dual shadow prices.)** *For $q > 1$, the LP dual has
   bounded shadow prices $y_i^*(q)$ satisfying*

$$
  |y_i^*(q)|
   \leq 
  \kappa(\mathrm{G}(q)) \cdot \|t(q)\|,
$$

   *where $\kappa(\mathrm{G}(q)) = \lambda_{\max}(G)/|\lambda_{\min}(G)|$
   is the Gram condition number. At the physical substrate
   value $q_0 \approx 1.110$: $\kappa(G(q_0)) \approx 3.03$
   (verified in the witness file), and all shadow prices are
   bounded in Skein units.*

4. **(Physical-substrate stability.)** *At $q_0 \approx 1.110$:*

$$
  P_{7,7}(q_0) \,\approx\, 0.5514,
  \qquad
  \Phi(q_0) \,\approx\, 0.0495,
$$

   *both strictly positive. The $q$-Toffoli is LP-stable at the
   physical substrate value, and $\{q$-Toffoli$, H\}$ generates
   a universal reversible computation on the Reeb bundles
   ([q-GoL](#prop:q-game-of-life)).*

**Substrate stability table** (verified numerically by
`toffoli-lp-stability.witness.json`):

See [Table 2](#tbl:toffoli-lp-stability-table2-data).

*Proof.*
The Gram matrix $G$ over $H_3(q)$ has characteristic polynomial
whose eigenvalue crossings are controlled by the discriminant
of the Hecke relation $(T - q)(T + q^{-1}) = 0$. The smallest
eigenvalue $\lambda_{\min}(\mathrm{G}(q))$ is a continuous function of
$q$ and, in the computed witness scan, remains negative
throughout the sampled domain, consistent with the standard
representation channel carrying an indefinite pairing.

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
$q_\star = 1/\varphi^2 = (3 - \sqrt{5})/2 \approx 0.382$.

Solving $\Phi(q) = 0$ in $(0, \infty)$: the factor $(q - 1)$
gives $q = 1$; the factor $(q^{3/2} + q^{1/2} - 1)$ gives, with
$x = q^{1/2}$, the cubic $x^3 + x - 1 = 0$ whose unique real
root is $x \approx 0.6824$, hence $q_\Phi \approx 0.4656$; the
factor $(q^{3/2} + q + 1)$ has no real root in $(0, \infty)$.

For $q > 1$: both $P_{7,7}(q) > 0$ and $\Phi(q) > 0$, and the
Wedderburn weights
$W_{\mathrm{sym}} = W_{\mathrm{alt}} = q^2/(q^4 + 4q^2 + 1)$,
$W_{\mathrm{std}} = (q^2+1)^2/(q^4 + 4q^2 + 1)$ are all
positive. The Toffoli element is LP-stable with all amplitudes
of the correct sign.

For $q \in (q_\Phi, 1)$: $\Phi(q) < 0$ — the q-AND acquires a
phase reversal rather than a simple flip — so the $q$-Toffoli
does **not** realise a CCNOT-semantics target flip.

The boundedness of shadow prices follows from LP duality
([LP-dual stability](#prop:lp-dual-stability)): $|y^*|$ is
bounded by the primal norm times the Gram condition number
$\kappa(\mathrm{G}(q)) = \lambda_{\max}(G)/|\lambda_{\min}(G)|$, which
is finite on $q > 1$. At $q_0 \approx 1.110$ the witness
gives $\kappa(G(q_0)) \approx 3.03$ and
$\lambda_{\min}(G(q_0)) \approx -0.956$
(`toffoli-lp-stability.witness.json`). $\square$

**Physical consequence.**
The substrate parameter $q_0 \approx 1.110$ lies comfortably in
the stable regime. The $q$-GoL ([q-Game of Life](#prop:q-game-of-life))
is therefore well-defined and information-preserving. A
hypothetical substrate with $q < q_\star$ would exhibit
topologically unstable Toffoli amplitudes — no universal
reversible computation is possible, and the substrate cannot
support information-bearing automata.

**Witness:** `toffoli-lp-stability.witness.json` evaluates
$P_{7,7}(q)$, $\Phi(q)$, and the Gram spectrum $\{\lambda_i(\mathrm{G}(q))\}$
on the grid $q \in \{0.30, 0.35, q_\star, 0.45, 0.60, 0.80,
0.95, 1.00, 1.05, q_0, 1.25, 1.50, 2.00, 3.00\}$. Confirms
$P_{7,7}(q_\star) = 0$ numerically, locates the q-AND zero
between $q = 0.45$ and $q = 0.60$, and verifies that both
amplitudes are strictly positive at $q_0$.
