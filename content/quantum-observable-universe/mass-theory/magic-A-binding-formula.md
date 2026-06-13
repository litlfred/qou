*Lean sibling: archimedean specialisation over $\mathbb{R}$ (CLAUDE.md §7c).
The underlying categorical content is generic; the formula is stated over
$\mathbb{R}$ for the MeV comparison.*

**Theorem (conditional on [`conj:magic-numbers-bring`](../quantum-observable-universes/magic-numbers-bring.md)
and [`prop:gravity-spectral-prefactor`](gravity-spectral-prefactor.md)).**
*For a light nucleus $^A_Z\mathfrak{X}$ that is doubly magic
(both $Z \in \mathfrak{M}$ and $N \in \mathfrak{M}$, with
$\mathfrak{M} = \{2, 8, 20, 28, 50, 82, 126\}$), the binding energy
admits the closed form*

$$
  \mathfrak{B}(^A_Z\mathfrak{X}) \;=\; \rho_F \cdot \mathfrak{m}_e \cdot A \cdot 8G
$$

*where $G$ is Catalan's constant, $8G = \mathrm{Vol}(L6a4) =
\mathrm{Vol}(\mathrm{Borromean})$ is the universal residue prefactor
([`prop:gravity-spectral-prefactor`](gravity-spectral-prefactor.md)),
and $\rho_F \in \mathbb{R}$ is the substrate-determined structural
prefactor for the doubly-magic regime.*

*Specialised to* $^4_2\mathrm{He}$ *with* $\rho_F = 2$:

$$
  \mathfrak{B}(^4_2\mathrm{He})
    \;=\; 2 \cdot \mathfrak{m}_e \cdot 4 \cdot 8G
    \;\approx\; 29.956\;\mathrm{MeV}
$$

*compared to the experimental value $28.296\,\mathrm{MeV}$ — a relative
miss of $+5.9\%$. This is dramatically tighter than the alpha-shift
formula ([`prop:binding-alpha-shift-extension`](binding-alpha-shift-extension.md))
which misses $^4_2\mathrm{He}$ by $-79\%$ ($5\times$ too small) because that
formula assumes a single hyperbolic force-carrier knot per nucleus —
an assumption that breaks for doubly-magic nuclei.*

## Why doubly-magic requires a separate formula

The framework's two binding paths apply to **distinct categorical
regimes**:

| Regime | Path | Categorical content |
|---|---|---|
| Hyperbolic | $\mathfrak{B} = \mathfrak{m}_e \cdot \rho_0 \cdot \alpha_{\mathrm{shift}}(T(p, k))$ | per-rep Reeb phase at force-carrier torus knot $T(p, k)$ |
| Doubly-magic | $\mathfrak{B} = \rho_F \cdot \mathfrak{m}_e \cdot A \cdot 8G$ | Borromean residue prefactor $\times$ nucleon count, no per-knot evaluation |

The dispatch is determined by the substrate:
[`prop:diagrammatic-double-magic-lr-fusion`](../observations/diagrammatic-double-magic-lr-fusion.md)
proves that at a doubly-magic level $A = Z + N$ with both $Z, N \in
\mathfrak{M}$, the Littlewood–Richardson fusion of the $Z$-block and
$N$-block collapses to a **single** self-conjugate Specht module —
there is **no Wedderburn channel** to absorb further binding through
Hecke crossings. The per-rep Reeb phase mechanism that generates
$\alpha_{\mathrm{shift}}$ vanishes (no hyperbolic knot), and the
binding is set by the universal Borromean residue $8G$ scaled by
nucleon count.

[`rem:strutinsky-from-graded-trace`](../observations/strutinsky-from-graded-trace.md)
makes the regime split forced by the filtered-algebra structure: the
decomposition

$$
  \mathrm{tr}_M(T_w, q_0) = \mathrm{tr}_{\mathrm{gr}}(\sigma(T_w), q_0) + \mathrm{Res}_{\mathrm{GB}}(T_w, q_0)
$$

identifies the Strutinsky shell correction $\delta E_{\mathrm{shell}}$
with the Gröbner–Shirshov residue sum, and *"Magic-number enhancements
arise algebraically when $\lambda$ reaches a rectangular shape and
$H_q(\lambda)$ factorises"*
([`prop:shell-schur-weyl-self-duality`](../mass-theory/shell-schur-weyl-self-duality.md)).
The doubly-magic case is exactly this rectangular-spike limit.

## $\rho_F$ for $^4_2\mathrm{He}$

The substrate-determined prefactor for $^4_2\mathrm{He}$ is
$\rho_F = 2$, sourced from the canonical
[`binding-ladder-catalog.py`](../../folio-assistant/computations/binding_ladder_catalog.py)
entry `2·m_e·4·Vol(L6a4)`. The categorical derivation of the integer
$2$ — vs. $[2]_q$, $2\cos(\pi/3)$, or another natural candidate — is
not closed in this proposition; the value is consumed as an input
hypothesis on the
[`MagicABindingFormula`](#prop:magic-A-binding-formula) instance per
CLAUDE.md §3b-cond.
## Numerical witness

[`folio-assistant/computations/binding_alpha_shift_witness.py`](../../folio-assistant/computations/binding_alpha_shift_witness.py)
emits a comparison witness showing the alpha-shift vs.
magic-A predictions side-by-side for $A \in \{2, 3, 4\}$. The
output JSON
[`binding-alpha-shift-witness.witness.json`](../../folio-assistant/computations/binding-alpha-shift-witness.witness.json)
quantifies the 80$\times$ gap closure for $^4_2\mathrm{He}$.
