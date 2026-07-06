*Proof.*
The Gram matrix $G$ over $H_3(q)$ has a characteristic polynomial whose eigenvalue crossings are controlled by the discriminant of the Hecke relation $(T - q)(T + q^{-1}) = 0$. The smallest eigenvalue $\lambda_{\min}(\mathrm{G}(q))$ is continuous in $q$. In the computed witness scan, it remains negative throughout the sampled domain. This is consistent with the standard representation channel carrying an indefinite pairing.

Write $T_q$ in the NF basis. The target-flip amplitude $P_{7,6}(q) = \Phi(q)$ determines the off-diagonal mass component. The diagonal $P_{7,7}(q)$ determines the Wedderburn weight of the standard channel ([Toffoli transfer matrix](#prop:toffoli-transfer-matrix)). Positivity of $G\vec{t}(q)$ therefore reduces to the positivity of the product $P_{7,7}(q) \cdot W_{\mathrm{std}}(q)$ with the appropriate sign from $\Phi(q)$.

Solving $P_{7,7}(q) = 0$: set $x = q^{1/2}$ to obtain $x^2 + x - 1 = 0$. This gives $x = (\sqrt{5} - 1)/2 = 1/\varphi$, and hence $q_\star = 1/\varphi^2 = (3 - \sqrt{5})/2 \approx 0.382$.

Solving $\Phi(q) = 0$ in $(0, \infty)$: the factor $(q - 1)$ gives $q = 1$. The factor $(q^{3/2} + q^{1/2} - 1)$ yields the cubic $x^3 + x - 1 = 0$ (for $x = q^{1/2}$), whose unique real root is $x \approx 0.6824$, hence $q_\Phi \approx 0.4656$. The factor $(q^{3/2} + q + 1)$ has no real root in $(0, \infty)$.

For $q > 1$: both $P_{7,7}(q) > 0$ and $\Phi(q) > 0$. The Wedderburn weights $W_{\mathrm{sym}} = W_{\mathrm{alt}} = q^2/(q^4 + 4q^2 + 1)$ and $W_{\mathrm{std}} = (q^2+1)^2/(q^4 + 4q^2 + 1)$ are strictly positive. The Toffoli element is LP-stable with all amplitudes of the correct sign.

For $q \in (q_\Phi, 1)$: $\Phi(q) < 0$. The q-AND acquires a phase reversal rather than a simple flip. Thus, the $q$-Toffoli does **not** realise a CCNOT-semantics target flip.

The boundedness of shadow prices follows from LP duality ([LP-dual stability](#prop:lp-dual-stability)). The dual norm $|y^*|$ is bounded by the primal norm times the Gram condition number $\kappa(\mathrm{G}(q)) = \lambda_{\max}(G)/|\lambda_{\min}(G)|$. This is finite for $q > 1$. At $q_0 \approx 1.110$, the witness gives $\kappa(G(q_0)) \approx 3.03$ and $\lambda_{\min}(G(q_0)) \approx -0.956$ (`toffoli-lp-stability.witness.json`). $\square$

**Physical consequence.**
The substrate parameter $q_0 \approx 1.110$ lies comfortably in the stable regime. The $q$-GoL ([q-Game of Life](#prop:q-game-of-life)) is therefore well-defined and information-preserving. A hypothetical substrate with $q < q_\star$ would exhibit topologically unstable Toffoli amplitudes. Under such conditions, no universal reversible computation is possible, and the substrate cannot support information-bearing automata.

**Witness:** `toffoli-lp-stability.witness.json` evaluates $P_{7,7}(q)$, $\Phi(q)$, and the Gram spectrum $\{\lambda_i(\mathrm{G}(q))\}$ on the grid $q \in \{0.30, 0.35, q_\star, 0.45, 0.60, 0.80, 0.95, 1.00, 1.05, q_0, 1.25, 1.50, 2.00, 3.00\}$. It confirms $P_{7,7}(q_\star) = 0$ numerically. It locates the q-AND zero between $q = 0.45$ and $q = 0.60$. It verifies that both amplitudes are strictly positive at $q_0$.
