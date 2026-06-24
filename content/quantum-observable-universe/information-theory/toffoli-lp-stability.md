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
