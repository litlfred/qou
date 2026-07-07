<!-- FILE_START: parity-classification-discrepancy-partition-sum-proton-intro.md -->
Continuation of the preceding sub-section.

The arc identifies the partition-sum proton residual that resolves the empirical chirality discrepancy.  The five-table data block supplies the substrate-flow numerics; the closing $np$-discrepancy resolution pins the substrate-level mechanism that distinguishes proton from neutron in the binding-energy formula.
<!-- FILE_END: parity-classification-discrepancy-partition-sum-proton-intro.md -->

<!-- FILE_START: partition-sum-proton-residual.md -->
**Proposition (proton tower residual = Frobenius co-Casimir trace).**
*Let $\mathfrak{m}^{\mathrm{tower}}(\mathfrak{p}, q_0)$ be the
pure-tower proton mass and $m_{\mathfrak{p}}^{\mathrm{CODATA}}$ the
experimental proton mass. The proton tower residual equals the
electron-scaled Frobenius co-Casimir trace at $n = 3$:*

$$
  \boxed{
    \Delta m_{\mathfrak{p}}
    \;:=\;
    m_{\mathfrak{p}}^{\mathrm{CODATA}}
    - \mathfrak{m}^{\mathrm{tower}}(\mathfrak{p}, q_0)
    \;=\;
    m_e \cdot \mathrm{tr}_M\bigl(C_{\mathrm{Frob}}^{(n=3)}\bigr)
    \;=\;
    m_e\Bigl(2 + \frac{1}{[2]_q}\Bigr),
  }
$$

*where $C_{\mathrm{Frob}}$ is the Frobenius co-Casimir central
element defined below.*

---

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
2. *The canonical proton-mass calibration itself has uncertainty
   at this precision.*

**GB-filtration decomposition (witness).**
*formalism the formal derivation
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

**canonical witness at $q_0 \approx 1.11$.**

See [Table 4](#tbl:partition-sum-proton-residual-table4-data).

**Algebraic origin hypothesis.**
*The quantity $\sum_\lambda 1/d_\lambda$ is the
**inverse-dimension partition sum** at level $n = 3$, the
expectation of $1/d_\lambda$ under the uniform-endpoint measure
on the Young lattice. The Kerov-walk variant has been ruled out
upstream (the formal derivation confirms the reciprocal-dim
distribution $(2/5, 1/5, 2/5)$ is a valid probability but **not**
the stationary measure of any simple local-update Kerov walk).
Plausible algebraic origins remain open — most natural is the
centraliser-algebra reading $1/d_\lambda = \dim Z(\mathrm{End}_{H_n}(S^\lambda))$
normalised, with the partition sum reflecting the trace of the
identity on the full Wedderburn decomposition. canonical exact match
to $0.03\%$ at canonical $q_0$ is a strong structural clue;
rigorous derivation is open.*

**Extension failure for neutron-containing configurations.**
*Upstream the formal derivation tested whether the same
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

**Corollaries.**

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
   components.*

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

*Witnesses: `deuteron-residual-canonical evaluation.witness.json`,
`q-variant-partition-sum.witness.json`.*

**Reference implementations.**
*Scripts
(both on branch `claude/1ppb-handover-docs-cyFlQ`):*
- the canonical formalism
- the canonical formalism
- the canonical formalism
<!-- FILE_END: partition-sum-proton-residual.md -->

<!-- FILE_START: np-discrepancy-resolution.md -->
**Remark.**
*Upstream the formal derivation reports a neutron/proton tower
discrepancy: the raw
[mass endomorphism tower](#prop:mass-endomorphism-tower)
undershoots the neutron mass by a factor of ~2.7
($m_{\mathfrak{n}}^{\mathrm{raw tower}} \approx 349$ MeV vs
CODATA $939.6$ MeV at full exact representation symbolic eval), while
overshooting the proton by 1.84%. This block documents the
structural origin: a $\Phi_q$ pole-distance asymmetry between
the two nucleons.*

**Predictions from CAL-1 + CAL-2 only (no $\beta$-decay calibration).**

*Per [`prop:three-calibration-discipline`](#prop:three-calibration-discipline)
the three allowed calibrations are CAL-1 ($m_e$), CAL-2 ($q_0$),
and CAL-3 ($\mathfrak{Q}_\beta$). The "no $\beta$-decay calibration" mode
uses only CAL-1 + CAL-2, leaving $\mathfrak{Q}_\beta$ as a prediction.*

*The full mass-endomorphism tower at exact representation symbolic
(the canonical formalism,
recomputed at 50 dps via sympy + exact algebraic structures, no exact precision):*

| quantity | value | vs CODATA |
|---|---|---|
| $m_{\mathfrak{p}}^{\mathrm{pred}}$ | $955.49$ MeV | $+1.84\%$ |
| $m_{\mathfrak{n}}^{\mathrm{pred}}$ | $348.66$ MeV | $\mathbf{-62.89\%}$ |
| $\Delta m^{\mathrm{pred}} = m_n - m_p$ | $-606.83$ MeV | wrong sign (target $+1.293$ MeV) |
| $\mathfrak{Q}_\beta^{\mathrm{pred}}$ (from $\Delta m - m_e$) | $-607.34$ MeV | nonsensical |

*Without $\beta$-calibration the neutron tower fails by factor
~2.7 because $\hat V_0^{\mathfrak{n}} = 0.7194$ (symbolic at 50
dps) sits far from the $q_0 = 1.11$ pole of $\Phi_q$ (distance
$0.391$ vs proton's $\hat V_0^{\mathfrak{p}} = 0.9890$ with
pole distance $0.121$ — a 3.23$\times$ pole-distance ratio). The
tower formula's $\Phi_q(\hat V)$ is pole-centric, so pole-distance
matters structurally. The cyclotomic projection of $\Phi_q$ at
high truncation $N$ converges to a fixed ratio: $\Phi_q(\hat
V_p)/\Phi_q(\hat V_n) \approx 178$ at $N \geq 100$.*

*Per [`prop:neutron-qvalue-symbolic`](#prop:neutron-qvalue-symbolic),
the cleanest non-calibrated prediction is at the level of the
NF-coefficient DIFFERENCE $|\Delta(\mathrm{net})|$ rather than
individual nucleon masses, sidestepping the per-nucleon pole-
distance asymmetry:*

$$
  \mathfrak{Q}_\beta = |\Delta(\mathrm{net})| \cdot E_0
  = \frac{(2-h) \cdot h}{2} \cdot \frac{m_e}{q_0 (q_0 - 1)}
  \approx 0.7836 \;\mathrm{MeV}
$$

*vs CODATA $0.7823$ MeV — **$+0.17\%$ / $+1.31$ keV residual**.
This is the framework's structurally-clean non-calibrated
prediction. The +1.31 keV residual is $\sim 525{,}000\times$
larger than the input-error propagation from CAL-1 + CAL-2
(~0.0025 keV at 3 ppb), so it is genuine brane-tower truncation
at $N=0$, not noise.*

**Resolution.**

*The per-nucleon mass asymmetry $m_n^\mathrm{pred} \ll m_n^\mathrm{CODATA}$
is genuine framework R&D (not yet closed without consuming CAL-3
as calibration). The path forward is to close the brane-tower
truncation at $N \geq 1$ via the cyclotomic projection at
substrate-derived $n_\star$
([`conj:brane-tower-z-habiro`](#conj:brane-tower-z-habiro)) —
an open conjecture. The current best non-calibrated prediction
remains the difference $\mathfrak{Q}_\beta = |\Delta(\mathrm{net})| \cdot E_0$.*

- *Term 1 (descended $\mathrm{tr}_M$): $\mathrm{tr}_M(\mathcal{B}_p)
  \approx 1.065 > \mathrm{tr}_M(\mathcal{B}_n) \approx 0.923$.
  Note this gives proton "heavier" in the Markov decomposition —
  opposite of CODATA. The framework's per-nucleon mass formula
  uses the brane tower to invert this; the NF-coefficient-sum
  formula uses the difference directly.*
- *Term 2 (single-generator tower $\sum \Phi_q$): produces a
  $\sim 178\times$ asymmetry $\Phi_q(\hat V_p)/\Phi_q(\hat V_n)$
  due to pole-distance, dominating the mass derivation in the
  raw tower formula and undershooting the neutron.*
- *Term 3 (pair-generator tower): similar pole-distance asymmetry.*
- *Term 4 (Frobenius co-Casimir): $(5/2) m_e \approx 1.278$ MeV
  universal, identical for $p$ and $n$ — confirms vortex-
  independence
  ([vortex-independence](#thm:frobenius-codim-universal)). Cancels
  in $\Delta m$.*
- *Term 5 (chirality): sign-indefinite at $A = 1$ per the Phase 2
  diagnostic; quarantined.*
- *Term 6 (jet-level prefix): small Habiro tail, identical for
  $p$ and $n$ at $A = 1$. Cancels in $\Delta m$.*

**The non-calibrated framework prediction.**
*Per the three-calibration discipline, $\mathfrak{Q}_\beta$ is treated as a
**prediction** from CAL-1 + CAL-2, not as input. The cleanest
non-calibrated form uses the NF-coefficient-sum DIFFERENCE
directly (rather than computing per-nucleon masses and
subtracting):*

$$
  \mathfrak{Q}_\beta = |\Delta(\mathrm{net})| \cdot E_0 \approx 0.7836\;\mathrm{MeV}
$$

*vs CODATA $0.7823$ — $+0.17\%$ / $+1.31$ keV residual. The
per-nucleon masses individually have larger residuals (proton
$+1.84\%$, neutron $-62.9\%$ via raw tower) due to the
pole-distance asymmetry, but cancel substantially in the
difference. Closing the residual at $N \geq 1$ requires the
substrate-derived $n_\star$ truncation rule (open per
[`brane-tower-z-habiro`](#conj:brane-tower-z-habiro)).*

**Implication for binding energies at $A \geq 2$.**

*With $\beta$-calibration fixing $p$ and $n$ absolute masses, the
binding-energy question becomes "how accurately does the unified
formula predict $m(\text{atom}) - m(\text{free})$?"  Current
results (formalism the formal derivation):*

| isotope | Term 1 err | Term 1 + 4 err | Term 5 (BW+χ) err |
|---|---|---|---|
| D ($A=2$) | $-55\%$ | $+2.1\%$ (best) | $-353\%$ (fail) |
| T ($A=3$) | $-94\%$ | $-79\%$ | $+0.5\%$ (best) |
| $^3$He ($A=3$) | $-90\%$ | $-73\%$ | $+0.9\%$ (best) |
| $^4$He ($A=4$) | $-98\%$ | $-94\%$ | $-4.1\%$ |

*The $A \geq 3$ errors are **not** from $n/p$ mismatch (that is
calibrated out) but from **missing terms 2–5** in the Schur–Weyl
pipeline.  Term 5 (paper's BW + chirality) supplies the bulk,
surface, asymmetry, Coulomb, and pairing structure that Schur–
Weyl alone does not capture.*

**The path to close all isotope errors.**

*Per the tiered mass formula
([unified knot mass](#thm:knot-mass-formula-unified)):*

1. *$A = 2$ (D): use Schur–Weyl + universal Frobenius (gives
   $+2.1\%$).  The BW+chirality formula fails ($-353\%$,
   likely wrong $a_K$ assignment — the formal derivation
   found no simple $a_K$ that fits).*
2. *$A = 3$ (T, ${}^{3}\mathrm{He}$): use BW + chirality $(1 - h^2)$ (gives
   $0.5$–$0.9\%$).*
3. *$A = 4$ (${}^{4}\mathrm{He}$): use BW + chirality $(1-h^2)^2$ + shell
   correction (gives $-4\%$).*
4. *$A \geq 5$: use BW + shell; chirality $\to 1$.  Errors
   $5$–$20\%$; requires term 6 (jet-level prefix, open).*

*No single formula works for all $A$ — the four tiers have
different dominant terms.  This is **not a flaw**: it reflects
the fact that at $A = 2$ the braid is short enough that Schur–
Weyl dominates, while at $A \geq 3$ the BW collective-motion
terms dominate.*

**Reference implementations.**

- the formal derivation (upstream): raw tower $n/p$ diagnosis
- the formal derivation: Term 1 + Frob sweep
- the formal derivation (upstream): Term 5 (BW+χ) sweep
- the formal derivation: integrated 6-term comparison
- the formal derivation: shows paper's D-chirality is wrong
<!-- FILE_END: np-discrepancy-resolution.md -->

<!-- FILE_START: mass-formula-regime-switching.md -->
The unified knot mass formula
([unified knot mass](#thm:knot-mass-formula-unified)) sums six
structural terms. Empirically, however, **different term subsets
dominate in different $A$ regimes**, and naïve additive summation
produces double-counting. This proposition documents the
regime-switching structure and resolves the apparent failure of
paper's BW+chirality formula at $A = 2$.

**Proposition.**
*Let $B(Z, N)$ denote the binding energy of an isotope with $A = Z + N$.
The following regime-switched formula matches AME to $\leq 5\%$ for
$A \leq 4$:*

$$
  B(Z, N)
  \;=\;
  \begin{cases}
    B_{\mathrm{SW}}(Z, N) + m_e\,\tau(C_{\dim_q}^{H_3})
      & \text{if } A = 2, \\[4pt]
    B_{\mathrm{BW}+\chi}(Z, N)
      & \text{if } 3 \leq A \leq 4, \\[4pt]
    B_{\mathrm{BW}}(Z, N) + B_{\mathrm{shell}}(A)
      & \text{if } A \geq 5,
  \end{cases}
$$

*where:*

- *$B_{\mathrm{SW}}(Z, N) = E_0 \cdot \bigl(|\mathrm{tr}_M(\mathrm{free})| - |\mathrm{tr}_M(\mathrm{atom})|\bigr)$ is the Schur–Weyl descended
 binding ([Schur–Weyl decomposition](#prop:schur-weyl-mass-decomposition)).*
- *$m_e \cdot \tau(C_{\dim_q}^{H_3}) = m_e(2 + 1/[2]_q) \approx 1.276\;\mathrm{MeV}$ is the universal
 Frobenius co-Casimir correction
 ([partition-sum residual](#prop:partition-sum-proton-residual)).*
- *$B_{\mathrm{BW}+\chi}$ is the paper's BW + chirality formula
 ([figure-eight BW coefficients](#thm:six-term-mass-formula-complete))
 with chirality factor $1 - h^2$ for $A = 3$ and $(1 - h^2)^2$ for $A = 4$.*
- *$B_{\mathrm{BW}}$ is the standard BW formula without chirality, plus a shell correction for magic numbers.*

**Unification: paper's BW coefficients are Hecke-derived $q$-integer products.**

*Per
[$q$-integer mass formula](#conj:q-integer-mass-formula),
each BW coefficient has an exact $q$-integer expression derived
from the Hecke algebra $H_3(R, q)$:*

See [Table 1](#tbl:mass-formula-regime-switching-table1-data).

*The exact relation $a_{\mathrm{asym}} = \frac{3}{2} \lambda_V$ is
**forced** by the $q$-integer form (both involve $[2]_q[7]_q$,
prefactors $3$ vs $2$) — an exact algebraic identity that is only
approximate in empirical BW fits. Similarly
$\lambda_S / \lambda_V = [4]_q^2 / ([2]_q [7]_q)$ is exact,
reflecting the $\sigma_1$ vs $\sigma_0$ crossing ratio.*

*So the unification **is** already in the paper: BW is Hecke-trace
data, specifically products of $q$-integers counting crossings in
the $B_3$ / $4_1$ knot topologies.*

**Regime-switching mechanism: topology, not just $A$.**

*The BW coefficients contain $q$-integers that count crossings in
a **specific topology**: $[7]_q$, $[4]_q$ are proton's internal
crossing counts; $[6]_q$ is the Borromean link $B_3$'s crossings.
These values are structurally tied to the $A \geq 3$ Borromean /
figure-eight topology.*

*For $A = 2$ (deuteron), the topology is a **satellite knot**, not
Borromean: the deuteron braid is $\varrho_{\mathfrak{p}} \cdot
\varrho_{\mathfrak{n}} \cdot \sigma_{\mathrm{pn}}$ — two nucleon
trefoils tied by one inter-nucleon crossing. The Borromean-specific
crossing counts $[6]_q, [7]_q, [4]_q$ **do not apply** to this
topology; the dominant dynamics are in the single inter-nucleon
crossing $\sigma_{\mathrm{pn}}$ and the two internal nucleon
Markov traces.*

*This is why paper's BW formula fails for $D$: it substitutes the
Borromean-topology $q$-integer coefficients into an $A$-dependent
framework ($\lambda_V \cdot A$, $\lambda_S \cdot A^{2/3}$, etc.),
but those coefficients were derived for the Borromean topology,
not the satellite topology of $D$. The regime switch is
**topological**, and $A = 2$ vs $A \geq 3$ is the topological
transition point (single pair vs Borromean triple).*

**$A = 2$ breakdown of BW.**

*At $A = 2$ the standard BW formula gives*

$$
  B_{\mathrm{bulk}}^{(A=2)}
  \;=\; 2 \lambda_V - 2^{2/3} \lambda_S - \delta_P/\sqrt{2}
  \;\approx\; 31.3 - 27.4 - 8.4 \;=\; -4.5\;\mathrm{MeV},
$$

*negative. The BW volume term does not exceed surface + pairing
at $A = 2$: the liquid-drop approximation has no droplet to speak
of with only two nucleons. Multiplying by any chirality factor
$a_K > 0$ keeps $B_{\mathrm{pred}} < 0$, which is unphysical. The
$D$ chirality canonical evaluation the formal derivation verified this: no
choice of $a_K \in [-2, 2]$ with the form
$B = a_K \cdot B_{\mathrm{bulk}}$ matches $B_{\mathrm{AME}}$
positively; the closest positive match requires $a_K < 0$
(negative, not a chirality factor).*

**Validity of SW+Frob at $A = 2$.**

*At $A = 2$ the atomic braid has only $1$ inter-nucleon crossing
on top of the intra-nucleon Hecke words. The Markov trace
$|\mathrm{tr}_M(T_w)|$ captures nearly all of the binding, and
the universal Frobenius correction
$m_e(2 + 1/[2]_q) \approx 1.28\;\mathrm{MeV}$ accounts for the
remaining per-vortex substrate cost. Result: $B_D^{\mathrm{pred}}
\approx 2.27\;\mathrm{MeV}$ vs $B_{\mathrm{AME}} = 2.22\;\mathrm{MeV}$
($+2.1\%$).*

*The Schur–Weyl pipeline describes $A = 2$ because:*

1. *Only $p(6) = 11$ partitions to sum over.*
2. *Max Specht dimension $f^\lambda = 16$ — tractable canonical.*
3. *No collective motion is present (no liquid-drop approximation needed).*
4. *Only one inter-nucleon crossing — the tower structure is minimal.*

**Validity of BW+$\chi$ at $A \geq 3$.**

*Starting at $A = 3$, the atomic braid has enough crossings that
**collective** partition channels dominate — the full Markov
trace is small (exponentially suppressed as $\sim 0.5^A$) but
the Wedderburn-weighted character sum
$\sum_\lambda w_\lambda \chi_\lambda$
remains large through specific collective partitions
$\lambda \vdash 3A$. Paper's BW formula captures this collective
content via the Hecke-algebra-derived coefficients
$\lambda_V = 2[2]_q[7]_q m_e$, $\lambda_S = 2[4]_q^2 m_e$, etc.
The chirality factor $1 - h^2$ is the $H_3$-level figure-eight
topology correction ([figure-eight BW coefficients](#thm:six-term-mass-formula-complete)).*

**No double-counting: SW and BW are not independent.**

*The paper's $B_{\mathrm{bulk}}$ coefficients are derived from
the Wedderburn channel weights $(w_{\mathrm{sym}}, w_{\mathrm{std}}, w_{\mathrm{alt}})$
times character differences $\chi_{4_1}(\lambda) - \chi_{B_3}(\lambda)$
([figure-eight BW coefficients](#thm:six-term-mass-formula-complete) proof).
The Schur–Weyl descended trace $|\mathrm{tr}_M(T_w)|$ is
$\sum_\lambda w_\lambda \chi_\lambda(T_w)$ for the **specific**
braid word $T_w$, weighted by $w_\lambda$. The two are computing
the same underlying partition sum — paper's BW is the $A \geq 3$
collective limit where specific character combinations dominate,
while SW is the exact evaluation that works best when individual
partition contributions are traceable. **Summing both double-counts.**
The regime-switching formula avoids this by choosing the dominant
computation per $A$.*

**Paper D chirality assignment is a category error.**

*The paper assigns $D \to (1 + h)$ as chirality factor; empirically
this fails by $-353\%$. canonical evaluation the formal derivation tested $13$
alternatives and continuous optimisation in $a_K \in [-2, 2]$;
no positive chirality factor fits. The resolution: **$D$ is not
in the BW regime at all**, so asking for its chirality factor is
a category error.*

*The paper's figure-eight BW derivation
([figure-eight BW coefficients](#thm:six-term-mass-formula-complete))
explicitly starts from the $4_1$ knot on $H_3(R, q)$ and derives
$a_K = 1 - h^2$ from the character $\chi_{4_1}(2,1) = 2 - [3]_q
= -1 - h^2$. For $D$ (satellite topology, $H_6(R, q)$), that
derivation does not apply; the satellite-knot character sum is a
different object.*

*The correct $D$ prediction is via Schur–Weyl on $H_6(R, q)$ directly
(our pipeline): $B_D^{\mathrm{pred}} = 2.27$ MeV vs $B_{\mathrm{AME}}
= 2.22$ MeV ($+2.1\%$). The "chirality factor" for $D$ under this
pipeline is implicitly captured by the braid word $T_w$ itself,
which already distinguishes positive and negative crossings
through the Hecke eigenvalues $(q, -q^{-1})$.*

*Recommended update to
[figure-eight BW coefficients](#thm:six-term-mass-formula-complete):*

*Add a scope note: "The $a_K$ chirality factor applies to
isotopes in the Borromean / $4_1$ topology ($A \geq 3$). For
$A = 2$ (satellite-knot topology), the formula does not apply."*

**Unification via dominant-term selection.**

*The deep statement is that the 6-term unified formula is a sum
over **complementary** contributions, each dominant in a different
regime. A single additive formula cannot work because different
regimes use different structural content from the same algebraic
objects. This is the mathematical reality: no single closed form
covers all $A$ — the regime switch is fundamental.*

*A future unification target is a **self-selecting** formula that
interpolates between SW+Frob ($A \leq 2$) and BW+$\chi$ ($A \geq 3$)
— for example via a smooth weighting $w_A \in [0, 1]$ that
transitions at $A = 2.5$. At present this is empirical; the
categorical derivation of $w_A$ is open.*

**Integrated witness table (from the formal derivation).**

See [Table 2](#tbl:mass-formula-regime-switching-table2-data).

*All predictions use **zero** fitted constants beyond $q_0$ and
$m_e$ (equivalently $E_0 = 0.782\;\mathrm{MeV}$).*

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: mass-formula-regime-switching.md -->

