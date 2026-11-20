## Necessity of a separate doubly-magic formula

The framework's two binding paths apply to **distinct categorical
regimes**:

| Regime | Path | Categorical content |
|---|---|---|
| Hyperbolic | $\mathfrak{B} = \mathfrak{m}_e \cdot \rho_0 \cdot \alpha_{\mathrm{shift}}(T(p, k))$ | per-rep Reeb phase at force-carrier torus knot $T(p, k)$ |
| Doubly-magic | $\mathfrak{B} = \rho_F \cdot \mathfrak{m}_e \cdot A \cdot 8G$ | Borromean residue prefactor $\times$ nucleon count, no per-knot evaluation |

The dispatch is determined by the substrate:
[Conjecture (diagrammatic double-magic)](../observations/diagrammatic-double-magic-lr-fusion.md)
proves that at a doubly-magic level $A = Z + N$ with both $Z, N \in
\mathfrak{M}$, the Littlewood–Richardson fusion of the $Z$-block and
$N$-block collapses to a **single** self-conjugate Specht module —
there is **no Wedderburn channel** to absorb further binding through
Hecke crossings. The per-rep Reeb phase mechanism that generates
$\alpha_{\mathrm{shift}}$ vanishes (no hyperbolic knot), and the
binding is set by the universal Borromean residue $8G$ scaled by
nucleon count.

[Strutinsky's shell correction as the categorical residue sum](../observations/strutinsky-from-graded-trace.md)
makes the regime split forced by the filtered-algebra structure: the
decomposition

$$
  \mathrm{tr}_M(T_w, q_0) = \mathrm{tr}_{\mathrm{gr}}(\sigma(T_w), q_0) + \mathrm{Res}_{\mathrm{GB}}(T_w, q_0)
$$

identifies the Strutinsky shell correction $\delta E_{\mathrm{shell}}$
with the Gröbner–Shirshov residue sum, and *"Magic-number enhancements
arise algebraically when $\lambda$ reaches a rectangular shape and
$H_q(\lambda)$ factorises"*
([Schur-Weyl justification of shell-operator self-duality](../knots-particles-confinement/shell-schur-weyl-self-duality.md)).
The doubly-magic case is exactly this rectangular-spike limit.

## $\rho_F$ for $^4_2\mathrm{He}$

The substrate-determined prefactor for $^4_2\mathrm{He}$ is
$\rho_F = 2$, sourced from the canonical
the canonical formalism
entry `2·m_e·4·Vol(L6a4)`. The categorical derivation of the integer
$2$ — vs. $[2]_q$, $2\cos(\pi/3)$, or another natural candidate — is
not closed in this proposition; the value is consumed as an input
hypothesis on the
[`MagicABindingFormula`](#prop:magic-A-binding-formula) instance.
## canonical witness

the canonical formalism
emits a comparison witness showing the alpha-shift vs.
magic-A predictions side-by-side for $A \in \{2, 3, 4\}$. The
output JSON
[`binding-alpha-shift-witness.witness.json`](../../../computations/binding-alpha-shift-witness.witness.json)
quantifies the 80$\times$ gap closure for $^4_2\mathrm{He}$.
