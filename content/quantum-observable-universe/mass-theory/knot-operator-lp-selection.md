**Proposition (knot-operator LP/SDP selection via Gram-inverse dual basis; conditional on [`conj:weak-spectral-completeness`](#conj:weak-spectral-completeness)).**

*Let $R$ be the categorical coefficient ring with $q \in R$ generic
(not a root of unity in $R$ — note $q = 1$ IS excluded), and let
$H_n(q)$ be the Iwahori-Hecke algebra over $R$ in the standard
generators ([Hecke-Skein convention](https://github.com/litlfred/qou/blob/main/CLAUDE.md) §7a).
Let $\{b_i\}$ be a Frobenius-non-degenerate basis (e.g. the
Gröbner-Shirshov NF basis $\{\gamma, \sigma_0, \sigma_1, L_+, L_-,
e^-\}$ for $H_3(q)$ on three strands). Then for any confinement
target $T \in H_n(q)$ — a bound-state defined by a vector of
required NF-channel multiplicities $n_T = (n_T^i)_{i=1}^{|\text{basis}|}
\in R^{|\text{basis}|}$ — the selection of a knot operator
$\beta(T_{m,m'}) \in H_n(q)$ producing $T$ is determined by the
Frobenius-Gram-inverse LP/SDP dual basis:*

$$
  \min_{\substack{x \geq 0 \\ G^{-1} S x \;\geq\; n_T}}
  \;\;\sum_{m'} t_{(m, m')} \, x_{(m, m')},
$$

*where $S = (s_{i,(m, m')})$ is the supply matrix encoding which
NF channel each torus knot $T_{m,m'}$ produces (computed by
[`knot-operator-table.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/knot-operator-table.witness.json)
for $H_3(q)$ matter operators and
[`knot-operator-table-h2.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/knot-operator-table-h2.witness.json)
for $H_2(q)$ EW even-twist links), $t_{(m, m')}$ is the crossing
energy ($q$-rational expression in $R$), and $G^{-1}$ is the
Frobenius co-Casimir Gram-inverse.*

*By Schrijver §7.4 strong duality + complementary slackness, the
LP dual variables $(y_0^*, y^*)$ supply:*

- *the **shadow price** $y_0^*$ of the net-multiplicity
  constraint;*
- *per-NF-channel **Frobenius positivity shadow prices** $y_i^* \geq
  0$ for each demand channel;*
- *the **active set** $A^*(T) := \{(m, m') : x_{(m, m')}^* > 0\}$
  identifying which knot operators actually contribute to the
  bound state $T$.*

*The selected operator is the unique $T_{m,m'}$ with $x_{(m,
m')}^* > 0$ when $A^*(T)$ is a singleton; otherwise the bound
state is a Wedderburn superposition with weights given by
$x^*$.*

### Statement (formal)

Define the **demand profile** of a confinement $T$ as the negative
NF coefficients (knot-operator basis table)
of the formal product $T = \prod_i b_i^{n_T^i}$. Define the
**supply profile** of a candidate knot operator $\beta(T_{m,m'})$
as the vector of positive NF coefficients in $b_i \cdot
\beta(T_{m,m'}) \cdot b_j$ ranging over basis pairs $(b_i, b_j)$.

The LP

$$
  \begin{aligned}
    \min_{x \geq 0} \quad & \sum_{(m, m')} t_{(m, m')} \, x_{(m, m')} \\
    \text{s.t.} \quad     & \sum_{(m, m')} S_{i, (m, m')} \, x_{(m, m')}
                            \;\geq\; n_T^i, \qquad i = 1, \ldots, \dim H_n(q),
  \end{aligned}
$$

is feasible iff the bound state $T$ is **physically realisable** —
i.e. iff the demand profile lies in the positive cone spanned by
the supply profiles. The Frobenius pairing
$\langle \cdot, \cdot \rangle_F$ on $H_n(q)$ provides the natural
inner product underlying the SDP relaxation.

**The Gram-inverse $G^{-1}$ is the canonical dual basis** for the
constraint matrix: rewriting the LP in the dual basis transforms
the constraint $S x \geq n_T$ into $\widetilde{S} x \geq G^{-1}
n_T$ where $\widetilde{S}$ is sparse (each torus knot couples to
at most a small fixed number of dual-basis directions). This is
the LP-rewriting that makes operator selection efficient.

### Existence + uniqueness of the selection

*By LP duality (Schrijver §7.2 strong duality), if the LP is
feasible, the optimal active set $A^*(T)$ is determined by the
complementary slackness condition*

$$
  y_i^* > 0 \;\;\Longleftrightarrow\;\;
  \text{constraint } i \text{ is tight at } x^*.
$$

*The active set is generically unique (Schrijver §7.4); ties
correspond to degenerate confinements with a continuous family of
operator-selection equivalents.*

### Existing instances (from witness data)

Per [`confinement-operator-selection.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/confinement-operator-selection.witness.json):

| Confinement | Active operator (LP-optimal) | NF demand | Crossing energy $t_{(m,m')}$ |
|-------------|------------------------------|-----------|-----------------------------:|
| Proton | $L_+ = \sigma_0\sigma_1$ | 0 | $\approx 0.152$ at $q_0$ |
| Neutron | $L_+ = \sigma_0\sigma_1$ | 0 | $\approx 0.106$ at $q_0$ |

Per [`knot-operator-table-h2.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/knot-operator-table-h2.witness.json):

- **EW carriers** $T(2,4), T(2,6), T(2,8)$ in $H_2(q)$ select the
  Wedderburn-(sym, alt) projector pair as the LP-active set,
  superseded — see Hoefsmit n=6 lift below.

### EW-sector LP/SDP-dual input via Wedderburn-pair volumes

The EW-sector instance of this proposition draws its supply
matrix from the Wedderburn-block-decomposed pair amplitude
$|V_i V_j|_{\rm Wedderburn}$ defined in
[`wedderburn_pair_volumes.py`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/wedderburn_pair_volumes.py)
(integrated from  commit `06305f30c`):

$$
  |V_i V_j|_{\rm Wedd}
  \;=\;
  w_{\rm sym} \cdot \lambda_i^{\rm sym} \lambda_j^{\rm sym}
  \;+\; w_{\rm std} \cdot \mathrm{tr}_{\rm Markov}(M_i M_j)\big|_{\rm std\ block}
  \;+\; w_{\rm alt} \cdot \lambda_i^{\rm alt} \lambda_j^{\rm alt},
$$

where $M_i$ are the full $2 \times 2$ transfer matrices (not just
the $(m_{21}, m_{22})$ bottom row used by the basic
`hecke_core.atom_per_generator_volumes`).

**LP/SDP-dual pair amplitudes for the EW sector:**

| Pair | Categorical interpretation |
|------|----------------------------|
| $\|V_W V_Z\|_{\rm Wedd}$ | LP-active edge: $W^\pm \leftrightarrow Z$ coupling via shared sym/alt block on $V^{\otimes 6}$ |
| $\|V_Z V_H\|_{\rm Wedd}$ | LP-active edge: $Z \leftrightarrow H$ Higgs vacuum-induced linkage |
| $\|V_W V_H\|_{\rm Wedd}$ | LP-active edge: $W^\pm \leftrightarrow H$ Yukawa-like coupling |
| $\|V_W V_W\|_{\rm Wedd}$ | self-pair amplitude for $W^\pm$ (charge-2 channel) |

These amplitudes feed the supply matrix $S$ in the LP for the EW
operator-selection instance. Combined with the Hoefsmit
cell-content multiplicities $(4, 2, 1, 3, 3, 1, 2, 4)$ of
[`thm:hoefsmit-ew-cell-content`](#thm:hoefsmit-ew-cell-content),
they determine the active set $A^*(T)$ for each EW confinement
target.

The LP dual variables (shadow prices) $y^* \geq 0$ then identify
the saturated demand channels — the EW-sector analog of the
existing $\{e^-, L_+, L_-, \gamma\}$ active-set extraction for
matter operators.
### Audit-flag impact

*Closing this proposition would close the methodological
discontinuity in the **FROB-FILTER** flag (the
Frobenius-positivity activation threshold between $A = 3$ and
$A = 6$ in
[`docs/audits/-nv-frob-filter-conjectures.md`](https://github.com/litlfred/qou/blob/main/docs/audits/-nv-frob-filter-conjectures.md)):
the activation rule becomes a **derived consequence** of
LP/SDP duality, not an empirical fit per atomic mass.*

**Witness inputs.**
[`gram-matrix-dual.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/gram-matrix-dual.witness.json),
[`knot-operator-table.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/knot-operator-table.witness.json),
[`knot-operator-table-h2.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/knot-operator-table-h2.witness.json),
[`confinement-operator-selection.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/confinement-operator-selection.witness.json).

**Audit doc.** [`docs/audits/-path-alpha-bring-refinement.md`](https://github.com/litlfred/qou/blob/main/docs/audits/-path-alpha-bring-refinement.md).
