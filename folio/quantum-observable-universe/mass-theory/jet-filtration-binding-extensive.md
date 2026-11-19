**Proposition (extensivity of the body-order binding).**
*Write the jet-filtration binding of [binding manybody equals jet filtration conjecture](#conj:binding-manybody-eq-jet-filtration) as*

$$
  B(A) \;=\; \sum_{n=2}^{A} \mathfrak{m}_e \, a_D^{(n)} \, w_n ,
$$

*with $\mathfrak{m}_e \geq 0$, and $a_D^{(n)} \geq 0$, $w_n \geq 0$ for every body
order $n$. Then $B$ is **monotone non-decreasing in the body-order cutoff $A$**:*

$$
  A \leq A' \;\Longrightarrow\; B(A) \leq B(A') ,
$$

*and it is **strictly increasing** whenever a new body order contributes
positively: if $\mathfrak{m}_e\, a_D^{(A+1)}\, w_{A+1} > 0$ (and $A+1 \geq 2$), then
$B(A) < B(A+1)$.*

Adding nucleon body orders can only increase binding. This is exactly the
**extensive** behaviour the *intensive* rotation-phase reading
$\theta_\lambda = \arccos(\chi^\lambda/d_\lambda)$ structurally lacked — a bounded
per-block phase cannot grow with the nucleon number $A$, so a single-parameter rotation-phase ansatz cannot close heavy-nucleus binding. The body-order series
supplies extensivity, because each term $\mathfrak{m}_e a_D^{(n)} w_n$ is a non-negative
contribution and the number of terms grows with $A$.

The proof is elementary — monotonicity of a finite sum of non-negative terms over
the nested index sets $\{2,\ldots,A\} \subseteq \{2,\ldots,A'\}$.

**Scope (what is *not* asserted here).** The three deeper inputs are carried as
non-negativity/positivity *hypotheses* on $a_D^{(n)}$ and $w_n$ rather than derived in
this proposition.

1. The **super-exponential magnitude** of the Seiberg–Witten period
   $a_D^{(n)} = \oint_{\mathcal{S}_c}\lambda_{\mathrm{SW}}^{(n)}$ supplies the
   *quantitative* extensive channel.
2. The **non-abelian-Stokes identity** $a_D^{(n)} = \mathrm{lw}(n-1)$ equates the period to the mean
   quantum dimension (conjectural, with residue-sum
   form [Seiberg–Witten period residue sum](#prop:sw-period-residue-sum)).
3. The per-atom **residue weight** $w_n(K)$ provides the $\rho\cdot A$ scale rule via a
   $q$-difference recursion output.

What is established is the *qualitative* extensivity: given non-negative period and
weight data, the body-order binding grows with $A$.

**Mathematical standing of (1)–(3).** Carrying (1)–(3) as hypotheses here separates the elementary monotonicity statement from three distinct analytical problems. Item (2) is conjectural: no unconditional derivation yet equates the prolongation period to the mean quantum dimension $\mathrm{lw}(n-1)$. Item (1) is established at the level of **asymptotic growth**: the period is super-exponential by the square-root branch geometry of the colour cubic, independently corroborated by the residue-sum expansion, and corresponds to the $q$-deformed involution count $T_q(n) = n\,\mathrm{lw}(n-1) \to I(n)$. However, no low-order $q$-holonomic recurrence fixes the exact $q$-statistic; in particular, the falling factorial $(1/2)_n$ outgrows $\mathrm{lw}$ and no constant geometric factor absorbs the ratio. Item (3) reflects a rank-$2$ boundary condition: $w_3$ enters as an independent datum because no scalar kernel exists on the carrier.

The quantitative match to experimental binding energies therefore depends on (1)–(3) as inputs, of which (2) remains the unproved step.
