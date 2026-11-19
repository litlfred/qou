The speed of light $c_q = 1/(q-1)$
([speed of light](#def:information-speed-of-light)) is a derived,
$q$-dependent quantity. This remark records the $q$-connection
decomposition that produces it, its regime behaviour, the
Lieb--Robinson decay of the causal cone, and its place among the
information-theoretic speed limits.

**The $q$-connection decomposition.**
The archimedean $q$-connection
([$q$-connection](#ex:q-connection)) splits the gauge potential
into horizontal (spatial) and vertical (Reeb/temporal) components:

$$
  A_q =  q^{-1}A
  +  (1 - q^{-1})\iota_\xi A\varTheta
  =  q^{-1}A
  +  \hbar_q\iota_\xi A\varTheta.
$$

The weight $q^{-1}$ controls horizontal information transfer
(spatial propagation between fibres), while $\hbar_q = 1 - q^{-1}$
controls vertical information processing (Reeb flow within a fibre).
Each $f_q$-iteration applies $A_q$ once, simultaneously advancing
the Reeb phase by $\hbar_q$ and correlating adjacent fibres with
coupling strength $q^{-1}$.

**Physical meaning.**
In each discrete $f_q$-iteration:

* The Reeb flow advances the fibre phase by $\hbar_q$ (temporal
 information: one tick of the internal clock).
* The $q$-connection correlates the current fibre with adjacent
 fibres at coupling $q^{-1}$ (spatial information: one step of
 horizontal propagation).

A measurement within the light cone compares these two rates.
The speed of light is how many fibres of spatial information are
correlated per unit of Reeb phase advance:

$$
  c_q =  \frac{\text{spatial coupling per step}}
                   {\text{temporal advance per step}}
  =  \frac{q^{-1}}{\hbar_q}
  =  \frac{1}{q - 1}.
$$

**Regime behaviour.**

| Regime | $q$ | $c_q = 1/(q-1)$ | Interpretation |
| --------------- | ------------------------- | --------------------------- | ----------------------------------------------------------------- |
| Deep-quantum | $q \to \infty$ | $\to 0$ | No spatial propagation; each fibre is isolated |
| Deep quantum | $\varphi^2 \approx 2.618$ | $\approx 0.618 = 1/\varphi$ | Sub-luminal; spatial coupling suppressed |
| Observable universe | $q_0$ | $\approx 9.093$ | ${\sim}9$ fibres correlated per Reeb phase advance |
| Near-classical | $1.01$ | $100$ | Fast spatial propagation; nearly continuous |
| Classical limit | $q \to 1^+$ | $\to \infty$ | Instantaneous spatial coupling; the $q$-connection reduces to $A$ |

At $q = q_0$, the speed of light is $c \approx 9.093$ in units
where one Reeb phase advance $= 1$. This is **not** $1$. The
value $c = 1$ arises only if one redefines length units so that
one "Planck length" equals $c_q$ Reeb phases --- but that obscures
the physics. In the natural units of the $q$-connection (where
temporal ticks and spatial couplings are measured on the same
footing), $c$ is $q$-dependent and equals $1/(q-1)$.

**Consistency: $c$ diverges at the classical limit.**
As $q \to 1$, the $q$-connection $A_q \to A$ (the full instanton
connection): the horizontal component dominates, spatial correlations
propagate instantly relative to the Reeb tick, and smooth
Riemannian geometry with $c = \infty$ (instantaneous spatial
coupling) emerges. This is the Newtonian limit. To recover finite
$c$ in SI units, one rescales by the Planck time
$t_P^{\mathrm{SI}} = \sqrt{\hbar G / c_{\mathrm{SI}}^5}$, which
absorbs the divergence into the ratio of human-scale seconds to
Reeb ticks.

**Connection to the contact affine chart.**
The light cone of an affine chart
([light cone](#rem:light-cone-affine)) is the locus $|Z| = c_q$:
the boundary where horizontal diffusion exactly matches vertical
advance. Inside the cone ($|Z| < c_q$), spatial signals arrive
within one Reeb circuit. Outside ($|Z| > c_q$), the signal
requires multiple Reeb circuits and is causally delayed.

**Lieb--Robinson bound.**
The locality of $\nabla_q$ (it acts on adjacent fibres only) and
the unitarity of the $R$-matrix (norm-preserving braiding in the
rigid :refterm[monoidal category]{#monoidal-category} $\mathbf{C}$) give an exponential decay
outside the causal cone:

$$
  \bigl\lVert
    [\mathcal{O}_x(n), \mathcal{O}_y(0)]
  \bigr\rVert
   \leq 
  C  e^{-\mu(d(x,y) -  n \cdot c_q \cdot \hbar_q)}
$$

for constants $C, \mu > 0$ depending on $q$. The causal cone
boundary is $d(x,y) = n \cdot c_q \cdot \hbar_q = n \cdot q^{-1}$:
after $n$ discrete steps, a signal has propagated $n \cdot q^{-1}$
units of base-manifold distance.

**Comparison with information-theoretic speed limits.**

| Result | Bound | QOU analog |
| ------------------------ | --------------------------------------- | --------------------------------------------------------- |
| Margolus--Levitin (1998) | $\leq 2E/\pi\hbar$ ops/sec | $n_R(q) = 1/\hbar_q$ ops per Planck time |
| Bremermann (1962) | $\leq mc^2/h$ bits/sec/kg | $\mathfrak{B}(q) = q\eta_q / (q-1)^2$ bits per Planck time |
| Bekenstein (1981) | $S \leq 2\pi RE / \hbar c$ | Fibre entropy $\leq \eta_q$ per operation |
| Pawlowski (2009) | No-signaling from information causality | Lieb--Robinson decay outside $\lvert Z\rvert = c_q$ cone |
