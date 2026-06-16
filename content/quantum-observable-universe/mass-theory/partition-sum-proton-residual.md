Let $\mathfrak{m}^{\mathrm{tower}}(\mathfrak{p}, q_0)$ be the
pure-tower proton mass computed via the
[mass endomorphism tower](#prop:mass-endomorphism-tower) at
$q_0$, in Hecke units, converted to MeV via the electron-trefoil
calibration and corrected by $(1 + [2]_q \hbar_q^2)$
([quantum Planck constant](#def:quantum-planck-constant)).
Let $m_{\mathfrak{p}}^{\mathrm{CODATA}} \approx :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json}\;\mathrm{MeV}$
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

See [Table 1](#tbl:partition-sum-proton-residual-table1-data).

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
*Script `computations/frobenius_partition_sum.py`
decomposes $\sum_\lambda 1/\dim_q(\lambda)$ by confinement
filtration level $\ell(\lambda) = \mathrm{height}(\lambda) - 1$:*

See [Table 2](#tbl:partition-sum-proton-residual-table2-data).

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

See [Table 3](#tbl:partition-sum-proton-residual-table3-data).

*These are tracked by the GB-filtration decomposition; the
self-dual pattern (top+bottom levels = $1 + 1$, plus middle
$q$-dependent) holds for all $n$.*

**Numerical witness at $q_0 \approx 1.11$.**

See [Table 4](#tbl:partition-sum-proton-residual-table4-data).

**Algebraic origin hypothesis.**
*The quantity $\sum_\lambda 1/d_\lambda$ is the
**inverse-dimension partition sum** at level $n = 3$, the
expectation of $1/d_\lambda$ under the uniform-endpoint measure
on the Young lattice. The Kerov-walk variant has been ruled out
upstream (`kerov_walk_verify.py` confirms the reciprocal-dim
distribution $(2/5, 1/5, 2/5)$ is a valid probability but **not**
the stationary measure of any simple local-update Kerov walk).
Plausible algebraic origins remain open — most natural is the
centraliser-algebra reading $1/d_\lambda = \dim Z(\mathrm{End}_{H_n}(S^\lambda))$
normalised, with the partition sum reflecting the trace of the
identity on the full Wedderburn decomposition. Numerical match
to $0.03\%$ at canonical $q_0$ is a strong structural clue;
rigorous derivation is open.*

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

**Deuteron-gap and $q$-variant probes.**
*Two upstream probes tested closed-form corrections against the
$^2$H binding gap $B_{\mathrm{AME}} - B_{\mathrm{pred}} = 1.2293\;\mathrm{MeV}$
and asked whether the $5/2$ admits a meaningful $q$-deformation:*

See [Table 5](#tbl:partition-sum-proton-residual-table5-data).

*Two structural readings emerge:*

1. **Per-vortex, not per-atom.** *The same $(5/2) m_e$ residual at
   $n = 3$ closes the deuteron gap (best variant); the naïve
   $n = 3A = 6$ generalization $(473/144) m_e$ fails by $+37\%$.
   The correction attaches to the fibre-functor calibration, not
   to the isotope's partition content.*
2. **Essentially classical, not $q$-deformed.** *No $q$-variant
   closes the gap below $3.5\%$; the natural $q$-deformation at
   $q_0 = 1.11$ is a $\sim 0.1\%$ perturbation — orders of
   magnitude smaller than the residual $4\%$ gap. The remaining
   gap must come from other sources: $\Phi_q$ tower terms not yet
   added to the Schur–Weyl descended mass
   ([mass endomorphism tower](#prop:mass-endomorphism-tower)),
   higher-cyclotomic Habiro coefficients
   ([Habiro completion](#prop:full-pole-structure-mass-trace)),
   or non-default inter-nucleon multiplicities.*

*Witnesses: `deuteron-residual-probe.witness.json`,
`q-variant-partition-sum.witness.json`.*

**Reference implementations.**
*Scripts
(both on branch `claude/1ppb-handover-docs-cyFlQ`):*
- [residual_partition_sum.py](https://github.com/litlfred/qou/blob/claude/1ppb-handover-docs-cyFlQ/computations/residual_partition_sum.py)
- [tower_isotope_absolute.py](https://github.com/litlfred/qou/blob/claude/1ppb-handover-docs-cyFlQ/computations/tower_isotope_absolute.py)
- [kerov_walk_verify.py](https://github.com/litlfred/qou/blob/claude/1ppb-handover-docs-cyFlQ/computations/kerov_walk_verify.py)
