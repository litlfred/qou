*Let $y_\lambda(q)$ denote the coefficient of $\chi^\lambda$ in the Frobenius
expansion $\mathrm{tr}_M^{\mathrm{Jones}} = \sum_{\lambda \vdash 3} y_\lambda \,
\chi^\lambda$ of the **Jones-normalised** Markov trace on $\mathrm{H}_3(q)$ —
the $V_{\mathrm{Jones}} / [2]_q^{\,c-1}$ Temperley–Lieb closure of
[Borromean Markov trace $\mathrm{tr}_M(\beta_{\mathrm{Bor}}) = (4 + h^2 - 3h^4 - h^6)/(h^2 + 4)$](borromean-markov-trace-closed-form.md),
i.e. the trace computing the **Borromean rings' Jones polynomial**. (This is
**not** the full-Hecke Ocneanu trace consumed by the mass/binding pipeline —
see the **Scope** note below.) Then for all $q$:*

$$
  \boxed{\;\;
  y_{(3)}(q) \;=\; \frac{[4]_q}{[2]_q^{3}},
  \qquad
  y_{(2,1)}(q) \;=\; \frac{1}{[2]_q^{2}},
  \qquad
  y_{(1^3)}(q) \;=\; 0.
  \;\;}
$$

*At the symmetric point $q = 1$ these evaluate to*

$$
  \bigl(y_{(3)},\, y_{(2,1)},\, y_{(1^3)}\bigr)\big|_{q=1}
  \;=\;
  \bigl(\tfrac{1}{2},\, \tfrac{1}{4},\, 0\bigr)
  \qquad \text{— \emph{not} uniform.}
$$

The scope of this trace normalisation, the immediate Borromean
corollary, the chirality of the weights, the notation distinctions,
and the significance for the Borromean derivation are collected in
[the Wenzl-weights context](#rem:h3-markov-wenzl-weights-context).

**Archimedean specialisation.** What follows sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
