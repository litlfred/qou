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
(`toffoli-lp-stability.witness.json`).
$\qquad\blacksquare$
