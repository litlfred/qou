**Proposition (conditional on
[`conj:mass-volume-factorization`](#conj:mass-volume-factorization)).**
*Let $\mathcal{R}_p \cong S^3$ be the Reeb bundle over the
exceptional divisor at brane point $p$
([Reeb bundle](#def:reeb-bundle)).  For a braid
$\beta \in B_3$, let $K_\beta \subset \mathcal{R}_p$ denote the
closure of the $q$-Reeb-flow trajectory of the three colour
tubes under $\beta$
([six canonical knot operators](#prop:six-canonical-knot-operators)),
and let $\nu(K_\beta)$ be an open tubular neighbourhood of
$K_\beta$ in $\mathcal{R}_p$.  Then the categorical Markov-trace
observable computed by
[vertex is the exceptional divisor](#prop:vertex-is-exceptional-divisor)
equals the JSJ-graded sum*

$$
  \mathrm{tr}_M\bigl(\rho(\beta)\bigr)
  \;=\;
  \sum_{P_i \text{ hyperbolic}}
  \rho_F(P_i)\,V_{\mathrm{hyp}}(P_i),
$$

*where the sum runs over the hyperbolic pieces $P_i$ of the JSJ
decomposition of the knot complement
$\mathcal{R}_p \setminus \nu(K_\beta)$, $V_{\mathrm{hyp}}$ is the
Thurston volume
([Thurston volume additivity](#prop:thurston-volume-additivity)),
and $\rho_F(P_i) \in \{m_e, 2m_e\}$ is the Frobenius packing
density determined by the local Wedderburn profile.*

This is the **Reeb-bundle face** of the existing mass-volume
factorisation conjecture
([mass-volume factorization](#conj:mass-volume-factorization)).
It packages the same equality with the geometric arena made
explicit: the categorical observable is computed *inside* the
Reeb bundle, and the right-hand side is the hyperbolic volume of
*its complement*.

**Conditional status, not a new conjecture.**  All
substantive content beyond
[mass-volume factorization](#conj:mass-volume-factorization)
is already established:

1. *Localisation in the Reeb bundle* — every Hecke generator
   factors through $\mathcal{R}_p$
   ([vertex is the exceptional divisor](#prop:vertex-is-exceptional-divisor)).

2. *Trajectory-to-knot identification* — the closure $K_\beta$
   of the colour-tube trajectories under $\phi^q_t$ is the
   topological knot whose complement carries the JSJ
   decomposition; this is the content of
   [six canonical knot operators](#prop:six-canonical-knot-operators)
   for the six generators and extends by composition to general
   braid words.

3. *Volume = trace* — this is exactly
   [mass-volume factorization](#conj:mass-volume-factorization),
   taken as the class hypothesis here.

The proposition adds **no new conjectural content**; its purpose
is to make the "complement is the volume" link explicit so the
reader can pass between the algebraic Markov-trace computation
and the geometric volume computation without searching across
chapters.

**Corollaries.**

- For pure-rotation braid words (3-cycles
  $\sigma_1\sigma_2$, $\sigma_2\sigma_1$) the trajectory $K_\beta$
  lies on a Heegaard torus inside $\mathcal{R}_p \cong S^3$.
  The complement admits a Seifert fibration; the JSJ
  decomposition has no hyperbolic pieces; the sum on the right
  is empty and $\mathrm{tr}_M(\rho(\beta)) = 0$ for the
  topological-mass component
  ([torus-knot zero volume via Reeb](#rem:torus-knot-zero-volume-via-reeb)).

- For Garside / Borromean / non-torus compositions the
  complement carries a non-trivial hyperbolic piece (e.g. the
  Borromean rings have $V_{\mathrm{hyp}} = 8G$ — the
  Gieseking–Meyerhoff constant — giving the published
  ${}^3\mathrm{He}$, ${}^4\mathrm{He}$ Borromean binding
  predictions of
  [mass-volume factorization](#conj:mass-volume-factorization))
  ([hyperbolic-knot positive volume via Reeb](#rem:hyperbolic-knot-positive-volume-via-reeb)).

- The Φ_q–JSJ archimedean bridge
  ([Φ_q tower JSJ bridge](#rem:phi-q-tower-jsj-bridge))
  is the Φ_q-tower decomposition of the right-hand side; the
  present proposition packages the left-hand side as a
  Reeb-bundle Markov trace.  The two together give the
  full algebra–to–geometry dictionary for nuclear binding.
