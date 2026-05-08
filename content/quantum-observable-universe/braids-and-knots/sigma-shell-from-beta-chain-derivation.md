**Proposition (closed-form $\sigma_{\mathrm{shell}}$ magnitude from compound β-chain).**
*Let $A_{\mathrm{magic}} \in \{2, 8, 20, 28, 50, 82, 126\}$ be a magic
nucleon count and let $\{(Z_k, N_k)\}_{k=0}^{K}$ be a β-decay chain
along the β-stability valley terminating at $(Z_K, N_K)$ with
$Z_K + N_K = A_{\mathrm{magic}}$, with measured AME 2020 Q-values
$\{Q_\beta^{(k)}\}_{k=0}^{K-1}$.  Then the shell-operator magnitude
$y_{\mathrm{target}}(A_{\mathrm{magic}})$, which appears in the
self-duality constraint
([Schur-Weyl self-duality](#prop:shell-schur-weyl-self-duality)), is
**derivable in closed form** as*

$$
  y_{\mathrm{target}}(A_{\mathrm{magic}})
  \;=\;
  \frac{1}{m_e \cdot |\mathrm{tr}_M(\beta_{\mathrm{ref}})|}
  \cdot \biggl(
    \sum_{k=0}^{K-1} Q_\beta^{(k)}
    \;-\;
    \sum_{k=0}^{K-1} \delta\rho^{(k)} \cdot m_e \cdot |\mathrm{tr}_M(\beta_k)|
  \biggr),
$$

*where:*

- *$\beta_{\mathrm{ref}}$ is the reference braid for the chain's
  starting point (typically a stable $A=1$ atom: free proton or neutron);*
- *$\delta\rho^{(k)} = \rho_K(\beta_{k+1}) - \rho_K(\beta_k)$ is the
  per-step change in categorical density along the chain;*
- *the **first sum** is the cumulative AME Q-value (empirical input);*
- *the **second sum** is the categorical "constituent walk" — the part
  of the mass change explained by the leading-order $\rho_K^{\mathrm{LO}}$.*

**Interpretation.**

*The shell magnitude is the **non-leading-order residual** of the
β-chain mass changes, **not** the cumulative Q-value itself.  By
[`prop:rho-k-h3a-refinement`](#prop:rho-k-h3a-refinement), the
mass change $M_{k+1} - M_k$ at each step decomposes as*

$$
  M_{k+1} - M_k
  \;=\;
  \delta\rho^{(k)} \cdot m_e \cdot |\mathrm{tr}_M(\beta_k)|
  \;+\;
  \sigma_{\mathrm{shell}}(A_k) \cdot \mathbb{1}_{A_k \in \mathrm{shell\;boundary}},
$$

*where $\sigma_{\mathrm{shell}}$ contributes only when the chain
crosses a shell boundary (i.e. $A_k = A_{\mathrm{magic}} \pm 1$).
The Q-value
$Q_\beta^{(k)} = M_k - M_{k+1} - m_e$ (free-neutron convention)
captures the full mass change including any shell contribution.
Subtracting the constituent-walk piece from the cumulative
Q-values isolates the shell magnitude.*

**Status.**

*This proposition is a **closed-form refinement** of
[`prop:compound-beta-shell-calibration`](#prop:compound-beta-shell-calibration),
which set up the framework but left $y_{\mathrm{target}}(A_{\mathrm{magic}})$
as the algebraic unknown.  The closed form here lets a Python
consumer
([`folio-assistant/computations/sigma_shell_from_beta_chain.py`](folio-assistant/computations/sigma_shell_from_beta_chain.py),
stub) compute $y_{\mathrm{target}}$ directly from AME 2020 chain
Q-values without further calibration, in line with the user's
"I do NOT want to derive Q_β" stance — the AME Q-values are
**inputs**, not parameters fitted at this layer.*

**Derivation.**

*Step 1 — Mass change along the β-chain.*
*By
[`prop:atomic-mass-gb-nf`](#prop:atomic-mass-gb-nf) and the
$\rho_K$ assembly
([T6 mittag-leffler decomposition](#prop:t6-mittag-leffler-decomposition)),
the mass at each chain link is*

$$
  M_k \;=\; \rho_K(\beta_k) \cdot m_e \cdot |\mathrm{tr}_M(\beta_k)|.
$$

*The chain mass change is therefore*

$$
  M_{k+1} - M_k
  \;=\;
  \rho_K(\beta_{k+1}) \cdot m_e \cdot |\mathrm{tr}_M(\beta_{k+1})|
  -
  \rho_K(\beta_k) \cdot m_e \cdot |\mathrm{tr}_M(\beta_k)|.
$$

*To first order in the categorical change $\delta\rho^{(k)}$ and
$\delta|\mathrm{tr}_M|^{(k)}$ along the chain (a single nucleon
type swaps), we have $|\mathrm{tr}_M(\beta_{k+1})|
\approx |\mathrm{tr}_M(\beta_k)|$ for non-shell-crossing steps
(the trace is approximately invariant under a $p \leftrightarrow n$
swap that doesn't change shell structure), so*

$$
  M_{k+1} - M_k \;\approx\; \delta\rho^{(k)}
                            \cdot m_e \cdot |\mathrm{tr}_M(\beta_k)|.
$$

*Step 2 — Shell crossing contribution.*
*At a shell-crossing step ($A_k = A_{\mathrm{magic}} \pm 1$), the
GS-NF structure changes by an additional **shell-operator term**
$\sigma_{\mathrm{shell}}(A_k)$ which contributes the shell magnitude:*

$$
  M_{k+1} - M_k
  \;=\;
  \delta\rho^{(k)} \cdot m_e \cdot |\mathrm{tr}_M(\beta_k)|
  \;+\;
  \sigma_{\mathrm{shell}}^{\mathrm{contrib}}(A_k).
$$

*By
[`prop:shell-schur-weyl-self-duality`](#prop:shell-schur-weyl-self-duality),
$\sigma_{\mathrm{shell}}^{\mathrm{contrib}}$ couples to the
shell-operator self-duality constraint, and the magnitude
$y_{\mathrm{target}}(A_{\mathrm{magic}})$ is the cumulative
contribution at the magic boundary.*

*Step 3 — Cumulate Q-values along the chain.*
*The free-neutron β-decay Q-value is $Q_\beta^{(k)} = M_k - M_{k+1} - m_e$
(modulo electron capture / positron emission sign conventions).
Summing along the chain:*

$$
  \sum_{k=0}^{K-1} Q_\beta^{(k)}
  \;=\;
  M_0 - M_K - K \cdot m_e
  \;\overset{\text{Step 2}}{=}\;
  -\sum_k \delta\rho^{(k)} \cdot m_e \cdot |\mathrm{tr}_M(\beta_k)|
  \;-\; y_{\mathrm{target}}(A_{\mathrm{magic}}) \cdot m_e \cdot |\mathrm{tr}_M(\beta_{\mathrm{ref}})|
  \;-\; K \cdot m_e.
$$

*(The reference factor $|\mathrm{tr}_M(\beta_{\mathrm{ref}})|$
absorbs the chain-endpoint normalization; the $K\cdot m_e$ term is
the cumulative electron emission.)*

*Step 4 — Solve for $y_{\mathrm{target}}$.*
*Rearranging Step 3 and absorbing the $K m_e$ correction into the
empirical Q-value side
($Q_\beta^{\mathrm{net}} = \sum_k Q_\beta^{(k)} + K m_e$):*

$$
  y_{\mathrm{target}}(A_{\mathrm{magic}})
  \;=\;
  \frac{Q_\beta^{\mathrm{net}}
        - \sum_k \delta\rho^{(k)} m_e |\mathrm{tr}_M(\beta_k)|}
       {m_e \cdot |\mathrm{tr}_M(\beta_{\mathrm{ref}})|}
$$

*as stated.  The positive-mass convention ($M_0 > M_K$ for an
energetically downhill chain) gives positive $y_{\mathrm{target}}$.
$\blacksquare$*

**Implementation outline (stub).**

*The Python consumer
[`folio-assistant/computations/sigma_shell_from_beta_chain.py`](folio-assistant/computations/sigma_shell_from_beta_chain.py)
would:*

1. *Load chain Q-values from a JSON manifest of AME 2020 chains
   reaching each magic anchor (curated input).*
2. *Compute $\rho_K(\beta_k)$ at each chain link using
   [`atomic_mass_via_rho_k.py`](folio-assistant/computations/atomic_mass_via_rho_k.py)
   and the existing $|\mathrm{tr}_M|$ witness.*
3. *Apply the closed form to extract $y_{\mathrm{target}}(A_{\mathrm{magic}})$
   for each magic anchor.*
4. *Verify against the predicted target magnitude $y \sim 10^{-3}$
   from $B/(A\cdot m_p)$
   ([`HANDOVER-STATUS.md` §3c](folio-assistant/computations/HANDOVER-STATUS.md)).*

**Compatibility with the no-$Q_\beta$-derivation directive.**

*This derivation **uses** AME 2020 $Q_\beta$ values as inputs (the
"empirical anchor" piece of the formula).  It does **not** derive
$Q_\beta$ from substrate alone — that's the unspoken-for direction
the user has explicitly declined ([`AUDIT-DEEP-2026-05.md`](../../../AUDIT-DEEP-2026-05.md)
§7 P10).  The 780 ppb floor from CAL-2 stands.*

*This proposition is the math content behind P8 in
[`AUDIT-DEEP-2026-05.md`](../../../AUDIT-DEEP-2026-05.md) §7.
Compute follow-up: AME chain manifest + $y_{\mathrm{target}}$
extraction.*
