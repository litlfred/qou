**Conjecture (Plancherel--Shannon channel reading of $\tau(C_{\dim_q})$).**

*There exists a probability measure $p_q$ on partitions
$\lambda \vdash n$ — a $q$-deformation of the Plancherel measure
$p_1(\lambda) = d_\lambda^2 / n!$ — such that the Frobenius
co-Casimir trace*

$$
  \tau(C_{\dim_q}) \;=\; \sum_{\lambda \,\vdash\, n} \frac{1}{\dim_q(\lambda)}
$$

*([universal Frobenius co-dimension](#thm:frobenius-codim-universal))
equals, up to a $q$-dependent calibration $\kappa(q)$, the Shannon
entropy of $p_q$:*

$$
  \tau(C_{\dim_q}) \;\stackrel{?}{=}\; \kappa(q) \cdot
  H(p_q) \;=\; -\kappa(q) \sum_\lambda p_q(\lambda) \log p_q(\lambda).
$$

*Equivalently, $1/\dim_q(\lambda)$ is the **transmission resistance**
of the categorical channel $\lambda$, and $\tau(C_{\dim_q})$ is the
parallel-resistance sum of channels weighted by the Plancherel-like
measure $p_q$.*

**Status.** Open.  The simplest candidate
$p_q(\lambda) \propto 1/\dim_q(\lambda)$ — verified numerically by
`kerov_walk_verify.py` — does **not** reproduce a Kerov random-walk
construction, ruling out the most direct interpretation.  A
non-trivial $q$-deformation is required.

**Proof sketch.**

*Strategy.*  Three ingredients are needed:

1. **Identify the measure $p_q$.**  Candidates: (i) the
   $q$-Plancherel measure $p_q(\lambda) = \dim_q(\lambda)^2 / [n]_q!$
   (Kerov), (ii) a heat-kernel regularisation of the Plancherel trace
   on $\mathbf{Rep}(H_n(q))$, (iii) the Macdonald measure
   $\mathrm{MM}_{q,t=q}$ at the Hecke specialisation.

2. **Compute the entropy.**  For each candidate, evaluate
   $H(p_q) = -\sum p_q(\lambda) \log p_q(\lambda)$ symbolically at
   $n = 3, 4, 5, 6$ and compare to the verified values of
   $\tau(C_{\dim_q})$ in [substrate cost limits](#rem:frobenius-limits-substrate-cost).

3. **Solve for $\kappa(q)$.**  The calibration must be a function of
   $q$ alone (not $\lambda$ or $n$) and must satisfy $\kappa(1) =
   \sum_\lambda 1/d_\lambda \cdot 1/H(p_1)$ to recover the classical
   peak.

*What needs to be proved.*

- **(P1)** The chosen measure is normalised and supported on
  partitions of $n$.
- **(P2)** $\kappa(q)$ is independent of $n$ and $\lambda$.
- **(P3)** The entropy formula reproduces the verified limits
  $\tau \to 2$ at $q \to 0^+$ and $q \to \infty$, and the peak
  $\sum 1/d_\lambda$ at $q = 1$.
- **(P4)** The $q \leftrightarrow q^{-1}$ symmetry of
  $\tau(C_{\dim_q})$ matches the symmetry of $H(p_q)$.

*Obstructions.*  Constraint (P3) at $q \to 0^+$ is the hard one:
the Shannon entropy of $p_q$ must collapse to the entropy of a
two-atom measure on the self-dual partitions $(n)$ and $(1^n)$.
This forces $p_q$ to concentrate on the lattice endpoints in the
crystal limit $q \to 0$ — a property satisfied by the crystal-basis
Plancherel measure but not by the naive $q$-Plancherel measure.

*Anticipated form.*  $p_q(\lambda) = \dim_q(\lambda)^2 / Z_q$ with
$Z_q = \sum_\lambda \dim_q(\lambda)^2 = [n]_q!$ (the $q$-Plancherel
measure), restricted to its **crystal limit** at $q \to 0, \infty$.
The calibration is conjecturally $\kappa(q) = m_e / \log Z_q$.

**No-go: the Jones--Markov candidate is ruled out.**  The most
naive candidate measure $p_q(\lambda) = y_\lambda(q) \cdot
d_\lambda$ (which has the desired Plancherel-type normalisation
$\sum_\lambda y_\lambda^{(n)} d_\lambda = 1$) is **not** a
probability measure for any $n \geq 4$:
[`prop:shannon-jones-markov-no-go`](#prop:shannon-jones-markov-no-go)
proves $p_q((1,1,1,1)) < 0$ at $q_0$ via three independent
computational pathways agreeing to machine $\epsilon$.  This
narrows the search to the crystal-basis or heat-kernel-regularised
candidates listed above.

**Verification path.**  Symbolic computation at $n = 3, 4, 5, 6$
is tractable; the witness file would live at
`folio-assistant/computations/tau-codim-shannon.witness.json`.  If
all four constraints hold for every $n$ tested, this becomes
strong evidence; a rigorous proof requires a categorical entropy
identity on $\mathbf{Rep}(H_n(q))$.
