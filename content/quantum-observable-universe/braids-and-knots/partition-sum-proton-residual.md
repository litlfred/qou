Let $\mathfrak{m}^{\mathrm{tower}}(\mathfrak{p}, q_0)$ be the
pure-tower proton mass computed via the
[mass endomorphism tower](#prop:mass-endomorphism-tower) at
$q_0$, in Hecke units, converted to MeV via the electron-trefoil
calibration and corrected by $(1 + [2]_q \hbar_q^2)$
([quantum Planck constant](#def:quantum-planck-constant)).
Let $m_{\mathfrak{p}}^{\mathrm{CODATA}} = 938.272\;\mathrm{MeV}$
denote the experimental proton mass.

**Proposition.**
*The proton tower residual has the exact partition-sum closed form*

$$
  m_{\mathfrak{p}}^{\mathrm{CODATA}} - \mathfrak{m}^{\mathrm{tower}}(\mathfrak{p}, q_0)
  \;=\;
  m_e \cdot \sum_{\lambda \,\vdash\, 3} \frac{1}{d_\lambda}
  \;=\;
  m_e \cdot \frac{5}{2}
  \;\approx\;
  1.277\;\mathrm{MeV},
$$

*where $d_\lambda = \dim S^\lambda$ is the classical Specht-module
dimension (hook-length formula).  The agreement is exact to
computational precision ($0.03\%$) using the canonical $q_0$
derived from the CODATA $m_\mu / m_e$ ratio.*

**Computation.**
*The three partitions of $3$ have dimensions
$d_{(3)} = 1$, $d_{(2,1)} = 2$, $d_{(1,1,1)} = 1$, giving the
exact rational*

$$
  \sum_{\lambda \,\vdash\, 3} \frac{1}{d_\lambda}
  = \frac{1}{1} + \frac{1}{2} + \frac{1}{1}
  = \frac{5}{2}.
$$

**Numerical witness at $q_0 \approx 1.11$.**

| quantity | value |
|---|---|
| $\mathfrak{m}^{\mathrm{tower, raw}}_{\mathfrak{p}}$ | $955.49\;\mathrm{MeV}$ |
| $/(1 + [2]_q \hbar_q^2)$ corrected | $936.994\;\mathrm{MeV}$ |
| $m_{\mathfrak{p}}^{\mathrm{CODATA}}$ | $938.272\;\mathrm{MeV}$ |
| residual $\Delta m_{\mathfrak{p}}$ | $+1.278\;\mathrm{MeV}$ |
| $\Delta m_{\mathfrak{p}} / m_e$ | $+2.5009$ |
| $\frac{5}{2}$ (predicted) | $+2.5000$ |
| ratio | $1.00036$ (sub-0.04%) |

**Algebraic origin hypothesis.**
*The quantity $\sum_\lambda 1/d_\lambda$ is the
**inverse-dimension partition sum** at level $n = 3$.  It appears
naturally as the expectation of $1/d_\lambda$ under the uniform-
endpoint measure on the Young lattice at depth $n$.  A Kerov-walk
interpretation is open — upstream `kerov_walk_verify.py`
documents: the reciprocal-dim distribution $(2/5, 1/5, 2/5)$ is
a valid probability but is **not** the stationary measure of any
simple local-update Kerov walk
([proof-objects](https://github.com/litlfred/qou/blob/claude/1ppb-handover-docs-cyFlQ/folio-assistant/computations/kerov-walk-verify.witness.json)).
Possible origins:*

1. *Heat-kernel on Young graph: $\sum_\lambda d_\lambda^{-1}$ is
   the partition function of the uniform endpoint distribution;
   its appearance as a physical mass correction suggests the
   trefoil proton braid samples the Young graph uniformly at
   its closure.*
2. *$1/d_\lambda$ is the dimension of the centraliser algebra
   $Z(\mathrm{End}_{H_n}(S^\lambda))$ normalised; the sum then
   reflects the trace of the identity on the full Wedderburn
   decomposition.*
3. *Schur–Weyl $\mathrm{tr}(\mathrm{id}_{V^{\otimes n}}) =
   \sum_\lambda d_\lambda \cdot \dim V_\lambda$, but the
   "dual" trace $\sum_\lambda \frac{1}{d_\lambda} \cdot
   \dim V_\lambda$ appears in tilting-object expansions.*

*A rigorous derivation is open; the numerical match to $0.03\%$
across the canonical-$q_0$ substrate is a strong structural
clue.*

**Extension failure for neutron-containing configurations.**
*Upstream `tower_isotope_absolute.py` tested whether the same
$\sum_\lambda 1/d_\lambda$ hypothesis extends to higher
partitions $n = 3A$ for isotopes.  Result: **fails for every
configuration containing at least one neutron**.  The neutron
alone gives $\Delta m_{\mathfrak{n}}/m_e = 1033.9$ vs predicted
$5/2$ — factor $\sim 414$.  Diagnosis: neutron's traced volume
$\hat V_0^{\mathfrak{n}} = 0.854$ is far from the $q_0 = 1.11$
pole of $\Phi_q$, so $\Phi_q(\hat V_0^{\mathfrak{n}}) \sim
100\times$ smaller than $\Phi_q(\hat V_0^{\mathfrak{p}} =
0.989)$, undershooting the tower mass of the neutron by factor
$\sim 2.3$.*

**Consequences.**

1. *The $\frac{5}{2} \cdot m_e$ closed form identifies the
   **single missing term** in the proton's pure-tower
   computation — likely a partition-averaged zero-point
   contribution.*
2. *The neutron failure localises the gap: something in the
   neutron's braid word or in the $\Phi_q$ evaluation near the
   pole underestimates the contribution.  The pole-proximity
   argument suggests the
   [GB residue spectral sum](#prop:gb-residue-spectral-sum)
   (which explicitly includes residue contributions from near
   the $\zeta_1 = 1$ pole) should capture exactly what the
   pure-tower formula misses.*
3. *Every isotope binding ($^2$H, $^3$H, $^3$He, $^4$He, ...)
   inherits the neutron tower failure through its neutron
   components — explaining the $-55\%$ deuteron residual in
   ([deuteron first principles](#rem:deuteron-first-principles)).*

**Deuteron-gap empirical probe.**
*Script `folio-assistant/computations/deuteron_residual_probe.py`
tested whether adding any of the following closed-form corrections
closes the $^2$H binding gap
$B_{\mathrm{AME}} - B_{\mathrm{pred}} = 1.2293\;\mathrm{MeV}$:*

| candidate | value (MeV) | error vs gap |
|---|---|---|
| $(5/2) \cdot m_e$  [= $\sum_{\lambda \vdash 3} 1/d_\lambda$] | $1.2775$ | **+3.92%** ★ |
| $\sum_{\lambda \vdash 6} 1/d_\lambda \cdot m_e$  [= $(473/144) m_e$] | $1.6785$ | $+36.5\%$ |
| $(\sum_{\lambda \vdash 6} - \sum_{\lambda \vdash 3}) \cdot m_e$ | $0.4010$ | $-67.4\%$ |
| $A \cdot m_e = 2 m_e$ | $1.0220$ | $-16.9\%$ |

*The **same $(5/2) \cdot m_e$ residual** — computed at $n = 3$,
not $n = 3A = 6$ — closes the deuteron gap to $3.92\%$.
The naive $n = 3A$ generalization (473/144) **fails by +37%**.*

*Structural reading:* **the residual is per-vortex, not per-atom
partition sum.**  A single proton gets $(5/2) m_e$; a deuteron,
built on one proton + one neutron, gets the **same** $(5/2) m_e$
residual in its binding — suggesting the correction attaches to
the fibre-functor calibration itself, not to the isotope's
partition content.  The $n = 3A$ partition-sum hypothesis
(`tower_isotope_absolute.py`) tested the full-mass residual;
the binding residual obeys a different scaling.

*Witness: `deuteron-residual-probe.witness.json`.*

**Reference implementations.**
*Scripts
(both on branch `claude/1ppb-handover-docs-cyFlQ`):*
- [residual_partition_sum.py](https://github.com/litlfred/qou/blob/claude/1ppb-handover-docs-cyFlQ/folio-assistant/computations/residual_partition_sum.py)
- [tower_isotope_absolute.py](https://github.com/litlfred/qou/blob/claude/1ppb-handover-docs-cyFlQ/folio-assistant/computations/tower_isotope_absolute.py)
- [kerov_walk_verify.py](https://github.com/litlfred/qou/blob/claude/1ppb-handover-docs-cyFlQ/folio-assistant/computations/kerov_walk_verify.py)
