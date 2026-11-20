*The unified iterative correction accumulates binding energy sequentially over the Young seminormal trace. For a partition $\lambda \vdash k$ write*

$$
  u_\lambda \;=\; \frac{w_\lambda}{d_\lambda} \;-\; \frac{1}{[k]_q!},
  \qquad
  \varrho_\lambda(s) \;=\; \frac{1}{\mu_\lambda + s},
  \qquad
  s_\ast \;=\; \frac{q_0 - 1}{q_0},
$$

*where $w_\lambda$ is the $q$-deformed Wedderburn weight, $d_\lambda = \dim V_\lambda$, and $\mu_\lambda = \sum_{\square \in \lambda} [c(\square)]_q\,[c(\square)+1]_q$ is the Jucys–Murphy $q$-Casimir eigenvalue on the $\lambda$-block, so that $\varrho_\lambda$ is the [$q$-resolvent](#def:q-resolvent) evaluated at the Planck-step Reeb frequency $s_\ast$. The per-partition contribution is*

$$
  B_\lambda(Z, N)
  = m_e \cdot H_q(\lambda) \cdot u_\lambda \cdot \varrho_\lambda(s_\ast) \cdot
    \big( \ln\big| \mathrm{tr}\, \mathbf{M}_\lambda^{(0..A)} \big| -
          \ln d_\lambda \big),
$$

*and the total unified correction is the sum of $B_\lambda(Z, N)$ over every enumerated $\lambda$.*

Only multi-dimensional mixing partitions carry a non-zero $u_\lambda$: the subtrahend $1/[k]_q!$ is exactly $\min_\lambda (w_\lambda / d_\lambda)$, so it annihilates the two one-dimensional blocks $(k)$ and $(1^k)$ at every level and nothing else.

The formulation bypasses special-case branching entirely. Each atomic step computes an independent energy increment from the transition trace difference, and the increments telescope, so the per-partition total depends on the running product only through its final trace. The process extracts the binding increment via identical algebraic mechanisms across all values of $A$.

## No sign selection on blocks

The sum above is unrestricted. Restricting it to those $\lambda$ with $\mathrm{tr}\, \mathbf{M}_\lambda^{(0..A)} \le 0$ is not a consequence of the Frobenius positivity constraint, as the following shows.

Complementary slackness for a Frobenius positivity constraint $\langle \Phi, \pi_\lambda \rangle \ge 0$ makes *tight* mean $\mathrm{tr} = 0$, not $\mathrm{tr} \le 0$. Under that reading every selected block contributes the same constant and the total reads nothing about the nucleus; the selected set also meets the domain of $\ln|\cdot|$ nowhere.

The [operator-selection programme](#prop:operator-selection-lp) is degenerate as well: its net-constraint dual vanishes identically and its minimiser set is a positive-dimensional face, so complementary slackness on that programme cannot single out a partition set at all.

Nor was the restriction a perturbation. Summing over all $\lambda$ instead gives a total larger by a factor of $1.93$ at $A = 2$ and $1.95$ at $A = 4$, evaluated at the production truncation $k_{\mathrm{exact}} = 11$; at $k_{\mathrm{exact}} = 4$ the same two factors are $4.60$ and $3.40$. The quantity is strongly truncation-dependent — the unrestricted $A = 2$ total spans a factor of $43$ across $k_{\mathrm{exact}} = 4 \ldots 11$ — so neither factor means anything quoted without its tier. The two readings coincide only when the excluded blocks happen to cancel exactly.

Removing the restriction is not an accuracy improvement. At $A = 2$ the AME2020 binding is $+2.2246\;\mathrm{MeV}$, and the restricted and unrestricted totals are both negative, the unrestricted one lying further from the measured value. What the removal discards is a selection step whose stated justification is false, not a term that was bringing the prediction closer to the data.

The name $u_\lambda$ is a per-partition weight in closed form. It is **not** a shadow price of any programme — it is not the net-constraint dual, which vanishes, and at $H_3$ it is $(0,\,0.16695,\,0)$ against the partition-indexed Frobenius duals $(1,\,1,\,0)$ of [the mass-coefficient block](#prop:mass-coefficient-shadow-price). It is written $y_\lambda$ in the compute, where it is evaluated by `hecke_core_legacy.lp_shadow_price`; that name is historical and is not the Markov partition weight of the same glyph.
