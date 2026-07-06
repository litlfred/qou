**Proposition.** The derived atom $\mathcal{A}(Z, N)$ is:

1. **Beta-stable** if and only if, for all single nucleon exchanges $\mathfrak{p} \leftrightarrow \mathfrak{n}$ at fixed $A = Z + N$:

$$
  |\mathrm{dem}(\mathcal{A}(Z, N))|
  \;\leq\;
  |\mathrm{dem}(\mathcal{A}(Z \pm 1, N \mp 1))|.
$$

The stable configuration minimizes the demand magnitude at fixed $A$.

2. **Shell-closed** (noble-gas-like) if and only if $\mathrm{dem}(\mathcal{A}) = \varnothing$. All NF coefficients are non-negative.
3. **Doubly magic** if both the nucleus $\mathcal{N}(Z, N)$ and the atom $\mathcal{A}(Z, N)$ have locally minimal Markov trace $\mathrm{tr}_M$ among neighboring $(Z, N)$.

## Examples

| Atom | $|\mathrm{dem}|$ | Demand channels | Status |
|:---|---:|:---|:---|
| ${}^1\mathrm{H}$ | $0.024$ | $\sigma_1$ | Open $1s^1$ shell |
| ${}^2\mathrm{H}$ | $0.058$ | $e^-$ | Fusible |
| ${}^3\mathrm{He}$ | $0.000$ | **none** | Shell-closed |
| ${}^4\mathrm{He}$ | $0.098$ | $\sigma_0, L_-$ | Doubly magic (lowest $\mathrm{tr}_M$) |

The demand-free ${}^3\mathrm{He}$ and the Markov-trace-minimal ${}^4\mathrm{He}$ represent two distinct stability mechanisms: shell closure (zero demand) and action minimization (lowest trace).

## Connection to beta decay

The $e^-$ demand channel in the nucleon normal form represents beta decay receptivity. A nucleon with $c_{e^-} < 0$ is receptive to emitting an electron. The transition $\mathfrak{n} \to \mathfrak{p} + e^- + \bar\nu$ occurs when:

$$
  |c_{e^-}(\mathfrak{n})| > |c_{e^-}(\mathfrak{p})|
  \quad \text{and} \quad
  \mathrm{net}(\mathfrak{n}) < \mathrm{net}(\mathfrak{p}).
$$

At $q_0$, $|c_{e^-}(\mathfrak{n})| = 0.044 > 0.043 = |c_{e^-}(\mathfrak{p})|$ and $\mathrm{net}(\mathfrak{n}) = 0.811 < 0.999 = \mathrm{net}(\mathfrak{p})$. Both conditions hold. Thus, the free neutron beta-decays.

## Inductive scaling via transfer matrix identities

For nuclei with $A > 4$, the NF computation scales polynomially via inductive Gröbner--Shirshov reduction ([derived atom](#def:derived-atom)). The key identity is the transfer matrix factorization: the product of two inter-nucleon crossings reduces via the Hecke relation before the next nucleon is appended. For same-type nucleon pairs:

$$
  C_{pp} \cdot C_{pp} = H_A \cdot C_{pp} + \mathbf{1},
  \qquad
  C_{nn} \cdot C_{nn} = \mathbf{1} - H_A \cdot C_{nn}.
$$

These are instances of the Hecke relation $\sigma_i^2 = H_A \sigma_i + \mathbf{1}$ applied to typed crossings. They ensure that iterated same-type nucleon pairs do not increase the NF complexity beyond linear growth in the number of nucleons.

**Witness:** `confinement-operator-selection.witness.json`, `four-term-photon-to-atoms.witness.json`.
