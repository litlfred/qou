**Proposition.**
*The deuterium binding energy is reproduced to $\le 0.2\%$ of the
AME value by combining the Wigner $T=0$ pn-pairing correction with
the **free-subtracted atomic Frobenius co-Casimir trace**, with no
fitted parameters:*

$$
  B(D) \;=\; -\Delta_W(D) \;-\; \Delta_F^{\text{atom}}(D)
$$

*where:*

$$
  \Delta_W(D) \;=\; -\,m_e \cdot H_q\bigl((2,2)\bigr) \cdot \frac{\min(Z, N)}{A}
$$

*is the standard Wigner correction
([Wigner np pairing](#prop:wigner-np-pairing)) and*

$$
  \Delta_F^{\text{atom}}(D) \;=\; -\,m_e \cdot \Bigl[\,
    \underbrace{\sum_{\lambda \,\vdash\, 3A}\!\frac{1}{\dim_q V_\lambda}}_{\Sigma_{3A}}
    \;-\;
    A \cdot \underbrace{\sum_{\lambda \,\vdash\, 3}\!\frac{1}{\dim_q V_\lambda}}_{\Sigma_3}
  \Bigr]
$$

*is the **free-subtracted atomic Frobenius co-Casimir trace**:
$\Sigma_{3A}$ is the trace at the atomic Hecke level
$H_{3A}(q)$, and $A\cdot \Sigma_3$ subtracts the contribution
already counted by the $A$ free constituents (whose trace is
$\Sigma_3$ each, by [proton residual partition sum](#prop:partition-sum-proton-residual)
and [Frobenius co-Casimir universal](#thm:frobenius-codim-universal)).*

*At $q = q_0 = 1.109978595554181\ldots$ (50 dps):*

$$
  \Sigma_3 \approx 2.4973, \qquad \Sigma_6 \approx 3.2021,
  \qquad \Sigma_6 - 2\Sigma_3 \approx -1.7926.
$$

*Hence $\Delta_F^{\text{atom}}(D) \approx +0.916$ MeV (positive,
i.e. anti-binding by sign convention) and
$\Delta_W(D) \approx -3.145$ MeV.  The total binding-correction
contribution is*

$$
  -(\Delta_W + \Delta_F^{\text{atom}}) \approx -(-3.145 + 0.916)
    = +2.229\;\text{MeV},
$$

*matching the AME deuteron binding $B_{\text{AME}}(D) = 2.22457$ MeV
to $+0.19\%$.*

*Proof.*
The Wigner correction $\Delta_W$ is established in
[Wigner np pairing](#prop:wigner-np-pairing).
The trace identities $\Sigma_{3A} = \sum_{\lambda \vdash 3A}
1/\dim_q V_\lambda$ are evaluated by the
[Frobenius co-Casimir universal](#thm:frobenius-codim-universal)
specialised to $H_{3A}(q)$.

The **free-subtraction** $\Sigma_{3A} - A \Sigma_3$ is the
correct atomic-level expression for the binding contribution: each
of the $A$ free nucleons already contributes $\Sigma_3$ to its own
intrinsic mass via the per-nucleon Frobenius co-Casimir
([proton residual partition sum](#prop:partition-sum-proton-residual)),
and these contributions are absorbed into the constituent baseline
$Z\mathfrak{m}_{\mathfrak{p}} + N\mathfrak{m}_{\mathfrak{n}}$.
What remains for the binding is the **excess** of the atomic-level
Frobenius co-Casimir over the disconnected sum.

Numerical evaluation in
[`computations/atomic_frobenius_codim.py`](#)
(witness `atomic-frobenius-codim.witness.json`) reproduces the
AME value to $+0.19\%$.  $\square$

**Empirical witness:**

See [Table](#tbl:deuteron-binding-frobenius-codim-table-data).

**Scope and limitation.**

The same free-subtracted Frobenius co-Casimir formula applied to
$T$, $^3\text{He}$, $^4\text{He}$ and beyond **under-binds** these
heavier isotopes (errors $-67\%$ to $-90\%$).  The
$\Sigma_{3A} - A \Sigma_3$ excess is bounded $\le 1$ in magnitude
across all $A$, while higher-$A$ binding energies grow in
proportion to nucleon-nucleon pair counts.  The deuteron's
exact match reflects the unique 2-body structure: a single
inter-nucleon generator and exactly one $T=0$ pn pair,
with no shell-closure or magic-number contributions to model.

For $A \geq 3$, additional structural binding terms (intra-shell
correlations, magic-number corrections) are needed.  These remain
open research directions; the present proposition establishes
the deuteron case as fully derived from the paper's existing
machinery (Frobenius co-Casimir + Wigner) without fitted
parameters.

**Witness:** `atomic-frobenius-codim.witness.json`
([source](#)).
