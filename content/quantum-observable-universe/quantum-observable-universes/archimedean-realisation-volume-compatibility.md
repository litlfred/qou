Two archimedean realisations act on the substrate $q$-volume of a QOU
braid/knot, along *different* source and target types:

- the **local** archimedean realisation functor $\tau_\infty \colon
  \widehat{\mathbb{Z}[q]} \to \mathbb{C}[\![q-1]\!]$ (the $q \to 1$ Taylor
  germ), applied to the Habiro-ring volume
  $V(\beta) = -\mathrm{Li}_2^q(-V_0(\beta))$
  ([$q$-dilogarithm](#def:q-dilogarithm),
  [generating functions solve the Reeb flow](#rem:generating-functions-solve-reeb-flow));
- the **global** archimedean realization functor
  $\mathcal{R}_{\mathrm{top}} \colon \widehat{\mathcal{M}} \to \mathbb{R}$
  ([archimedean realization functor](#def:archimedean-realization-functor)),
  applied to the motivic volume class $\mu(\beta) \in \widehat{\mathcal{M}}$.

Because their types differ ($\widehat{\mathbb{Z}[q]} \to
\mathbb{C}[\![q-1]\!]$ versus $\widehat{\mathcal{M}} \to \mathbb{R}$), the
two functors are **not** equal as functors. The substantive claim is that
they agree *as real-valued volume observables* on the QOU volume classes.

**Conjecture.** *For every QOU braid $\beta$, the archimedean value of the
Habiro-ring volume under $\tau_\infty$ and the topological realization of the
motivic volume under $\mathcal{R}_{\mathrm{top}}$ coincide, and both equal the
Bloch–Wigner / Thurston hyperbolic volume of the associated hyperbolic piece:*

$$
  \operatorname{ev}_{q \to 1}\bigl(\tau_\infty(-\mathrm{Li}_2^q(-V_0(\beta)))\bigr)
  \;=\;
  \mathcal{R}_{\mathrm{top}}\bigl(\mu(\beta)\bigr)
  \;=\;
  V_{\mathrm{hyp}}(K_\beta),
$$

*naturally in $\beta$ — i.e. $\tau_\infty \circ (-\mathrm{Li}_2^q \circ (-V_0))$
and $\mathcal{R}_{\mathrm{top}} \circ \mu$ are the same map on the QOU volume
classes $\widehat{\mathcal{M}}_{\mathrm{QOU}}$.*

**Scaffolding (established).** Both maps are well defined: $\tau_\infty$ is the
Habiro $q \to 1$ evaluation, and $\mathcal{R}_{\mathrm{top}} = \pi_\infty \circ
\chi_{\mathrm{top}}$ is the composite realization. On the individual cases
already witnessed in the corpus — the figure-eight and trefoil complements —
both sides reduce to the same Bloch–Wigner sum
([Thurston volume additivity](#prop:thurston-volume-additivity)), so the
*scaffolding half* of the compatibility holds on those cases.

**Open (the conjecture proper).** The *general* naturality — that the identity
holds for **all** QOU braids simultaneously, as an equality of maps rather than
case-by-case numerology — is of Kashaev volume-conjecture strength and is not
proved here. It is the volume-observable face of the
`QOU.Habiro.HabiroFlowSolution` open conjecture flagged in
[generating functions solve the Reeb flow](#rem:generating-functions-solve-reeb-flow):
the assertion that $\tau_\infty$ commutes with the three Habiro-ring
constructions.
