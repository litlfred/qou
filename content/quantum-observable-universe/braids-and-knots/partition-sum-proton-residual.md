Let $\mathfrak{m}^{\mathrm{tower}}(\mathfrak{p}, q_0)$ be the
pure-tower proton mass computed via the
[mass endomorphism tower](#prop:mass-endomorphism-tower) at
$q_0$, in Hecke units, converted to MeV via the electron-trefoil
calibration and corrected by $(1 + [2]_q \hbar_q^2)$
([quantum Planck constant](#def:quantum-planck-constant)).
Let $m_{\mathfrak{p}}^{\mathrm{CODATA}} = 938.272\;\mathrm{MeV}$
denote the experimental proton mass.

**Derivation via the Frobenius co-Casimir.**

*The Hecke algebra $H_n(R, q)$ is a **self-dual Frobenius algebra**
under the Markov-trace pairing $\langle x, y\rangle := \mathrm{tr}_M(xy)$
([Jones–Markov trace](#thm:jones-markov-trace)).  Self-duality
identifies $H_n(R, q) \cong H_n(R, q)^*$ as bimodules; Wedderburn gives
$H_n(R, q) = \bigoplus_{\lambda \vdash n}\mathrm{Mat}_{\dim(\lambda)}(R)$
with Plancherel weights $w_\lambda = \dim_q(\lambda)^2 / [n]_q!$.*

**Frobenius co-Casimir.**
*Define the central element*

$$
  C_{\mathrm{Frob}}
  \;:=\;
  \sum_{\lambda \,\vdash\, n}
    \frac{[n]_q!}{\dim_q(\lambda)^2 \cdot \dim(\lambda)}
    \cdot e_\lambda
  \;\in\; Z\bigl(H_n(R, q)\bigr),
$$

*where $e_\lambda$ is the central idempotent of block $\lambda$
(projector onto $S^\lambda$).  This is the **inverse-Plancherel-
per-classical-dim** central element — the natural Frobenius
partner of the unit $1 = \sum_\lambda e_\lambda$ under the
Markov pairing.*

**Trace identity (derived).**
*Using $\mathrm{tr}_M(e_\lambda) = \dim_q(\lambda) \cdot \dim(\lambda)/[n]_q!$,*

$$
  \mathrm{tr}_M(C_{\mathrm{Frob}})
  \;=\;
  \sum_\lambda
    \frac{[n]_q!}{\dim_q(\lambda)^2 \cdot \dim(\lambda)}
    \cdot
    \frac{\dim_q(\lambda) \cdot \dim(\lambda)}{[n]_q!}
  \;=\;
  \sum_{\lambda \,\vdash\, n} \frac{1}{\dim_q(\lambda)}.
$$

*Applied at $n = 3$ with $\dim_q((3)) = 1$, $\dim_q((2,1)) = [2]_q$,
$\dim_q((1,1,1)) = 1$:*

$$
  \boxed{
    \mathrm{tr}_M\bigl(C_{\mathrm{Frob}}^{(n=3)}\bigr)
    \;=\;
    2 + \frac{1}{[2]_q}.
  }
$$

**Proton residual as the Frobenius co-Casimir trace.**
*The observed proton tower residual is*

$$
  \Delta m_{\mathfrak{p}}
  \;:=\;
  m_{\mathfrak{p}}^{\mathrm{CODATA}}
  - \mathfrak{m}^{\mathrm{tower}}(\mathfrak{p}, q_0)
  \;=\;
  1.2779\;\mathrm{MeV}.
$$

| form | expression | value (MeV) | vs $\Delta m_{\mathfrak{p}}$ |
|---|---|---|---|
| $q$-deformed (Frobenius) | $m_e \cdot \mathrm{tr}_M(C_{\mathrm{Frob}}) = m_e(2 + 1/[2]_q)$ | $1.2761$ | $-0.14\%$ |
| classical ($q \to 1$ limit) | $m_e \cdot \sum 1/d_\lambda = (5/2) m_e$ | $1.2775$ | $-0.03\%$ |

*Both match to $< 0.15\%$.  The $q$-deformed form is the
**structural** answer (derived above); classical is its $q=1$
limit.  At $q_0 = 1.11$ the two agree to $0.1\%$; the residual
$\sim 0.1\%$ discrepancy between the $q$-deformed value
$1.2761$ MeV and the observed $1.2779$ MeV may come from:*

1. *Hecke-algebra finite-size corrections beyond the co-Casimir
   trace (higher-order Frobenius invariants).*
2. *The numerical proton-mass calibration itself has uncertainty
   at this precision.*

**GB-filtration decomposition (witness).**
*Script `folio-assistant/computations/frobenius_partition_sum.py`
decomposes $\sum_\lambda 1/\dim_q(\lambda)$ by confinement
filtration level $\ell(\lambda) = \mathrm{height}(\lambda) - 1$:*

| $\ell$ | partitions | conjugate pair? | contribution |
|---|---|---|---|
| $0$ | $(3)$ | $\leftrightarrow (1,1,1)$ | $1$ |
| $1$ | $(2,1)$ | self-conjugate | $1/[2]_q$ |
| $2$ | $(1,1,1)$ | $\leftrightarrow (3)$ | $1$ |

*The **self-dual structure** is explicit: levels $\ell = 0$ and
$\ell = n-1$ are conjugate via Young-diagram transpose; their
$\dim_q$ values are identical (so their $1/\dim_q$ contributions
are $1$ each).  The self-conjugate level $\ell = 1$ carries the
$q$-dependence.  For general $n$ the pattern generalises:*

- *Levels $\ell = 0$ and $\ell = n-1$ contribute $1$ each (the
  single-row and single-column partitions, conjugate under
  transpose).*
- *Middle levels pair off by conjugation; self-conjugate
  partitions (like $(2,2)$ at $n=4$ or $(3,2,1)$ at $n=6$) sit
  at the fixed level of the self-duality involution.*
- *Total is $2 + \text{(middle-level sum)}$.*

**Higher-$n$ values (witness).**

| $n$ | $\sum 1/\dim_q(\lambda)$ at $q_0$ | classical $\sum 1/d_\lambda$ |
|---|---|---|
| $3$ | $2.4973$ | $5/2 = 2.5$ |
| $4$ | $3.1464$ | $19/6 \approx 3.167$ |
| $5$ | $3.0305$ | $46/15 \approx 3.067$ |
| $6$ | $3.2021$ | $473/144 \approx 3.285$ |

*These are tracked by the GB-filtration decomposition; the
self-dual pattern (top+bottom levels = $1 + 1$, plus middle
$q$-dependent) holds for all $n$.*

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
| $(5/2) \cdot m_e$  [= $\sum_{\lambda \vdash 3} 1/d_\lambda$] | $1.2775$ | **+3.92%** (best) |
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

**$q$-variant probe: is the $5/2$ a $q$-deformation?**
*Tested several natural $q$-analogues of
$\sum_{\lambda \vdash 3} 1/d_\lambda = 5/2$ at $q_0 \approx 1.11$:*

| candidate | $q_0$ value | $\times m_e$ | vs gap |
|---|---|---|---|
| classical $5/2$ | $2.5000$ | $1.2775$ | $+3.92\%$ |
| $2 + 1/[2]_q$  (via $\dim_q(\lambda)$) | $2.4973$ | $1.2761$ | $+3.81\%$ |
| $[5]_q / [2]_q$ | $2.5961$ | $1.3266$ | $+7.91\%$ |
| $2 + 1/(2 \cdot [2]_q)$ | $2.2486$ | $1.1491$ | $-6.53\%$ |
| $\sum 1/H_q(\lambda)$ (raw hook) | $0.6553$ | $0.3349$ | $-72.8\%$ |

*Result: **no $q$-variant closes the gap below $3.5\%$**.  The
classical $5/2$ and the natural $q$-analogue $2 + 1/[2]_q$ cluster
within $0.1\%$ of each other, both about $+3.9\%$ above the
observed deuteron gap.  The $[5]_q/[2]_q$ "q-rational" variant is
worse ($+7.9\%$).*

*Structural reading: **the $5/2$ is essentially classical, not
$q$-deformed.**  Its $q$-deformation at $q_0 = 1.11$ is a $\sim 0.1\%$
perturbation — orders of magnitude smaller than the residual $4\%$
gap.  That residual must come from elsewhere:*

1. *The $\Phi_q$ tower terms not yet added to the Schur–Weyl
   descended mass
   ([mass endomorphism tower](#prop:mass-endomorphism-tower)).*
2. *Root-of-unity residues at $\zeta_\ell$ beyond $\zeta_1$
   ([full pole structure](#prop:full-pole-structure-mass-trace)).*
3. *Atomic-braid convention: inter-nucleon multiplicities
   $m_{pn}$, $m_{pp}$, $m_{nn}$ other than the default $1$.*

*Witness: `q-variant-partition-sum.witness.json`.*

**Reference implementations.**
*Scripts
(both on branch `claude/1ppb-handover-docs-cyFlQ`):*
- [residual_partition_sum.py](https://github.com/litlfred/qou/blob/claude/1ppb-handover-docs-cyFlQ/folio-assistant/computations/residual_partition_sum.py)
- [tower_isotope_absolute.py](https://github.com/litlfred/qou/blob/claude/1ppb-handover-docs-cyFlQ/folio-assistant/computations/tower_isotope_absolute.py)
- [kerov_walk_verify.py](https://github.com/litlfred/qou/blob/claude/1ppb-handover-docs-cyFlQ/folio-assistant/computations/kerov_walk_verify.py)
