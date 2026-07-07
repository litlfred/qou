<!-- FILE_START: nuclear-binding-intro.md -->
With the derived atom $\mathcal{A}(Z, N)$ in hand, we identify stable $(Z, N)$ pairs and shell closures. The linear programming demand profile alone dictates nuclear and atomic stability. Three operator regimes for nuclear binding partition the $(Z, N)$ lattice into torus-knot, Hopf-link, and post-magic regions, reproducing the empirical magic ladder. We conclude by asserting that the valley of stability is the demand-minimizing locus in $(Z, N)$-space.
<!-- FILE_END: nuclear-binding-intro.md -->

<!-- FILE_START: nuclear-operator-regimes.md -->
**Proposition.**
*In the inductive construction of $\mathcal{N}(Z, N)$, the optimal inter-nucleon binding operator $\Phi_k$ at step $k$ belongs to one of three regimes:*

**(Regime I — Shell filling).**
*Within the first nuclear shell, the demand-minimizing operator is the torus knot $T_{2,n_s}$ where $n_s$ is the shell size:*

$$
  \Phi_k = T_{2,5} = (\sigma_0\sigma_1)^2\sigma_0
  \qquad (k = 1,\; p \to pp)
$$

**(Regime II — Magic shell closure).**
*At and immediately after a magic number, the optimal operator is a Hopf link $L_\pm$:*

$$
  \Phi_k \in \{L_+ = \sigma_0\sigma_1,\; L_- = \sigma_1\sigma_0\}
$$

*The Hopf link achieves demand closure at magic shell boundaries.*

**(Regime III — Open shell).**
*Beyond a closed magic shell, the optimal operator reverts to the bare typed crossing:*

$$
  \Phi_k \in \{C_{pp},\; C_{pn},\; C_{nn}\}
$$

The operator transitions from $T_{2,5}$ to $L_+$ at the first magic number, then to $L_-$ at the shell boundary, and finally to $C_{pn}$ in the open shell. The $\mathcal{B}_3$ Borromean operator is never selected at the nuclear level; it remains purely a quark-level confinement operator.
<!-- FILE_END: nuclear-operator-regimes.md -->

<!-- FILE_START: nuclear-operator-regimes-interpretation.md -->
The three operator regimes carry this physical interpretation:

- **Regime I** (torus knot): Initial nucleons interact as individual particles. The residual strong force between them forms the cinquefoil $T_{2,5}$.
- **Regime II** (Hopf link): At magic numbers, the filled shell acts collectively. A new nucleon crosses the entire shell rather than individual nucleons. This collective Hopf link binds the new nucleon, driving shell closure.
- **Regime III** (bare crossing): Beyond the magic shell, the nucleus is large enough that new nucleons interact via simple pairwise crossings. The existing normal form already encodes the collective effects.
<!-- FILE_END: nuclear-operator-regimes-interpretation.md -->

<!-- FILE_START: demand-profile.md -->
**Definition.**
*Let $\mathcal{A}(Z, N) = \sum_w c_w \cdot w$ be a derived atom in normal form. Its **demand profile** is*

$$
  \mathrm{dem}(\mathcal{A})
  \;=\;
  \{(w, c_w) : c_w < 0\}
  \;\subset\;
  \mathrm{NF}(B_A) \times \mathbb{R}_{<0}.
$$

*The **demand magnitude** is $|\mathrm{dem}| = \sum_{c_w < 0} |c_w|$.*

**Archimedean specialisation.** This block invokes real- or complex-analytic constructs. Categorical identities remain valid over an abstract coefficient ring; their archimedean realisation is specialised here.
<!-- FILE_END: demand-profile.md -->

<!-- FILE_START: demand-stability.md -->
**Proposition.**
*The derived atom $\mathcal{A}(Z, N)$ is:*

1. ***Beta-stable** if and only if, for all single nucleon exchanges $\mathfrak{p} \leftrightarrow \mathfrak{n}$ at fixed $A = Z + N$:*

$$
  |\mathrm{dem}(\mathcal{A}(Z, N))|
  \;\leq\;
  |\mathrm{dem}(\mathcal{A}(Z \pm 1, N \mp 1))|.
$$

*The stable configuration minimizes the demand magnitude at fixed $A$.*

2. ***Shell-closed** if and only if $\mathrm{dem}(\mathcal{A}) = \varnothing$. All NF coefficients are non-negative.*
3. ***Doubly magic** if both the nucleus $\mathcal{N}(Z, N)$ and the atom $\mathcal{A}(Z, N)$ have locally minimal Markov trace $\mathrm{tr}_M$ among neighboring $(Z, N)$.*

The demand-free ${}^3\mathrm{He}$ and the Markov-trace-minimal ${}^4\mathrm{He}$ represent two distinct stability mechanisms: shell closure (zero demand) and action minimization (lowest trace).

## Connection to beta decay

The $e^-$ demand channel in the nucleon normal form represents beta decay receptivity. A nucleon with $c_{e^-} < 0$ is receptive to emitting an electron. The transition $\mathfrak{n} \to \mathfrak{p} + e^- + \bar\nu$ occurs when:

$$
  |c_{e^-}(\mathfrak{n})| > |c_{e^-}(\mathfrak{p})|
  \quad \text{and} \quad
  \mathrm{net}(\mathfrak{n}) < \mathrm{net}(\mathfrak{p}).
$$

At $q_0$, both conditions hold. Thus, the free neutron beta-decays.

## Inductive scaling via transfer matrix identities

For nuclei with $A > 4$, the NF computation scales polynomially via inductive Gröbner--Shirshov reduction. The key identity is the transfer matrix factorization: the product of two inter-nucleon crossings reduces via the Hecke relation before the next nucleon is appended. For same-type nucleon pairs:

$$
  C_{pp} \cdot C_{pp} = H_A \cdot C_{pp} + \mathbf{1},
  \qquad
  C_{nn} \cdot C_{nn} = \mathbf{1} - H_A \cdot C_{nn}.
$$

These are instances of the Hecke relation $\sigma_i^2 = H_A \sigma_i + \mathbf{1}$ applied to typed crossings. They ensure that iterated same-type nucleon pairs do not increase the NF complexity beyond linear growth in the number of nucleons.
<!-- FILE_END: demand-stability.md -->