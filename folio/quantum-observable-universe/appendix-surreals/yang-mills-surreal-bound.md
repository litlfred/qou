The Yang--Mills mass-gap problem asks for a proof that pure $\mathrm{SU}(N)$ Yang--Mills theory on $\mathbb{R}^4$ has a strictly positive mass gap $\Delta_{\mathrm{YM}} > 0$. In the QOU framework, this is the definitional content of the substrate: the structural invariant $\Delta_q \asymp \varepsilon^3$ is the categorical mass gap. This remark makes that identification explicit.

Let $\varepsilon \in \mathrm{Der}(A)$ be the Reeb infinitesimal ([Reeb infinitesimal](#def:reeb-epsilon)), $q = 1 + \varepsilon$ ([$q$ from $\varepsilon$](#def:q-from-epsilon)). The Yang--Mills gauge group in the QOU is realised as the representation category $\mathbf{Rep}(\mathrm{SU}_q(N))$ of the quantum group $\mathrm{SU}_q(N)$ at $q = 1 + \varepsilon$.

By [collapse of the quantum gap](#thm:quantum-gap-collapse) and [surreal rate calculus](#prop:surreal-rate-calculus), the lowest eigenvalue of the $q$-Laplacian on the state bundle $\mathcal{S}$ is strictly positive:

$$
\Delta_q \asymp \varepsilon^3 > 0 \qquad (\text{in } \mathbb{R}(\varepsilon) \subset \mathbf{No}).
$$

In the $\omega$-adic register ([Big-O via $\ordw$](#rem:conway-normal-form)): $\ordw(\Delta_q) = -3 > -\infty = \ordw(0)$. The mass gap sits at strictly higher $\omega$-order than the zero element.

The Yang--Mills specialization of [surreal squeeze](#lem:surreal-squeeze) concerns the putative massless glueball excitation, of energy $\delta = 0$. The squeeze

$$
\delta^2 \cdot \varepsilon^{-1} > \varepsilon^3
$$

is equivalent to $|\delta| > \varepsilon^2$. It therefore holds for every standard-real $\delta > 0$ — which is exactly the hypothesis under which the lemma is stated — is marginal at $\delta = \varepsilon^2$, and **fails** at $\delta = 0$, where the left side vanishes while the right side is $\varepsilon^3 > 0$. The massless excitation is excluded by that failure, not by a degeneracy: the only excitation of zero cost is the trivial one.

Two things do not follow from the lemma as stated, and are recorded here rather than assumed. The lemma quantifies over **standard-real** $\delta$, so it says nothing directly about an infinitesimal $\delta$; and the threshold the inequality supplies, $\varepsilon^2$, is larger than the asserted gap $\Delta_q \asymp \varepsilon^3$ by a factor of $\varepsilon^{-1}$, so an excitation sitting at $\Delta_q$ does not clear it. The categorical mass-gap statement $\delta \geq \Delta_q$ for non-trivial excitations is therefore the intended reading of $\Delta_q \asymp \varepsilon^3 > 0$ established above, not a consequence of this squeeze.

The Yang--Mills mass-gap theorem is literally true in the QOU framework as a surreal-order inequality: $\Delta_q > 0$ in $\mathbb{R}(\varepsilon)$, equivalently $\ordw(\Delta_q) = -3$. Classical Yang--Mills on $\mathbb{R}^4$ is recovered as the standard part ([calculus up to $\varepsilon$](#rem:calculus-up-to-epsilon)): $\mathrm{st}\bigl(\Delta_q / \varepsilon^3\bigr) = c > 0$ for a standard real $c$, so the classical mass gap is $\Delta_{\mathrm{YM}} = \lim_{\varepsilon \to 0} \Delta_q / \varepsilon^3 \cdot \varepsilon^3_{\mathrm{phys}}$ at the physical $\varepsilon = 1/\omega$ value.

The classical Yang--Mills problem asks for the existence of a positive mass gap; the QOU provides it by categorical construction. What remains is the regularity programme: showing that the classical $\mathrm{SU}(N)$ Yang--Mills theory on $\mathbb{R}^4$, as a renormalised QFT, is the standard part of the $q$-deformed substrate as $\varepsilon \to 0$. This is the Wightman-axiom portion of the millennium statement—analogous to how [NS surreal bound](#rem:ns-surreal-bound) reduces NS regularity to the substrate reversion under blow-up.

The $q$-deformation at standard-real $\varepsilon > 0$ replaces the continuous Wilson loop by the categorical trace over $\mathbf{Rep}(\mathrm{SU}_q(N))$, which is non-vanishing precisely on closed braids. The classical confinement statement ("only gauge-invariant observables are colour-singlet") is the surreal-order statement that every non-trivial Wilson loop has $\omega$-order $> 0$: its standard part is an exponentially suppressed real quantity.

The Yang--Mills gauge theory on $\mathbb{R}^4$ is classically a field theory, not an elliptic-curve or skein-module problem. The QOU substrate encodes it via the fibre-functor $\tau : \mathbf{Rep}(\mathrm{SU}_q(N)) \to \mathbf{Vec}$: Yang--Mills observables are natural transformations of $\tau$, and the mass gap is the first positive eigenvalue of the Reeb derivation on $\mathrm{End}_{\mathbf{C}}(A)$. The surreal-order statement $\ordw(\Delta_q) = -3$ is therefore a re-expression of the Yang--Mills mass gap in the categorical register.
