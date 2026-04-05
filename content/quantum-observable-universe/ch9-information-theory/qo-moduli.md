The **moduli of quantum observables** $\mathfrak{M}_{\mathrm{QO}}$
is the class of pairs $(\mathbf{C}, A)$ where:

- $\mathbf{C}$ is a rigid monoidal category (Axiom 1 of a
  [quantum universe](#def:quantum-universe)), and
- $A$ is a Frobenius–Hopf object in $\mathbf{C}$ (Axiom 2):
  a sextuple $(A, \mu, \eta, \Delta, \varepsilon, S)$ satisfying
  associativity, coassociativity, the Frobenius relation, and
  the antipode axiom.

This is a **definable class** in $\mathcal{L}_{\mathrm{RMC}}$:
each Frobenius–Hopf axiom is a first-order sentence in the
[language of rigid monoidal categories](#def:q-categorical-language).
Crucially, $\mathfrak{M}_{\mathrm{QO}}$ imposes only the structural
axioms (Axioms 1–2) — it does **not** require the observability,
measurability, or volume constraints that distinguish a QOU from
a bare quantum observable.

The moduli admits a natural stratification by quantum dimension:

$$
  \mathfrak{M}_{\mathrm{QO}}
  \;=\; \bigsqcup_{d \in \mathrm{End}(\mathbf{1})}
  \mathfrak{M}_{\mathrm{QO}}^{(d)},
  \qquad
  \mathfrak{M}_{\mathrm{QO}}^{(d)}
  = \{(\mathbf{C}, A) : \dim_q(V) = d\}
$$

where $V$ is the fundamental object of $A$. The stratum
$\mathfrak{M}_{\mathrm{QO}}^{([2]_q)}$ — quantum dimension
$[2]_q = q + q^{-1}$ — contains all quantum observables whose
gauge group deforms from $\mathrm{SU}(2)$.
