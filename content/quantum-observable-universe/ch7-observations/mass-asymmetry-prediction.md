**Statement.**
*In the QOU framework, the crossing energy weights $q$ (positive
crossing) and $q^{-1}$ (negative crossing) are asymmetric whenever
$q \neq 1$.  For a particle $K$ with $n_c$ positive crossings and
its antiparticle $\sigma(K)$ with $n_c$ negative crossings, the
crossing energies differ by*

$$
  \frac{|E_{\mathrm{cross}}(K)|}{|E_{\mathrm{cross}}(\sigma(K))|}
  \;=\; \frac{n_c \, q}{n_c \, q^{-1}}
  \;=\; q^2
  \;\approx\; 1.231
  \quad (q = 1.1097).
$$

**What this is and is not.**
This is **not** a prediction that $m_e \neq m_{e^+}$ in the
laboratory.  CPT invariance is experimentally established to
extraordinary precision:

| System | Bound on $|m - \bar{m}|/m$ | Experiment |
|--------|---------------------------|------------|
| $e^- / e^+$ | $< 8 \times 10^{-9}$ | TRAP (Gabrielse, 1999) |
| $p / \bar{p}$ | $< 1.6 \times 10^{-12}$ | BASE (CERN, 2022) |
| $H / \bar{H}$ | $< 2 \times 10^{-12}$ | ALPHA (CERN, 2020) |

The QOU is consistent with these bounds: the physical
(renormalized) masses are equal.  The $q^2$ ratio lives at the
**Skein (constituent) scale** --- the pre-renormalized algebraic
level where individual crossing weights are resolved.  The descent
to the physical scale averages over $n_R(q) \approx 10$ Reeb
iterations per Planck time, and the statistical-mechanical
coarse-graining
([stat-mech time](#rem:statistical-mechanical-time)) restores the
$q \leftrightarrow q^{-1}$ symmetry that CPT requires.

**Where the $q^2$ asymmetry IS observed.**
The Skein-scale asymmetry $q \neq q^{-1}$ does not show up in
mass measurements (CPT protects those).  It shows up in
**energy decompositions and coupling ratios** --- quantities that
resolve the individual crossing weights rather than the
coarse-grained sum:

1. **EM/strong ratio.**
   $\tanh(\ln q) = (q - q^{-1})/(q + q^{-1}) \approx 0.104$
   ([crossing energy interpretation](#rem:crossing-energy-interpretation)).
   This is the ratio of the antisymmetric channel (which sees
   $q \neq q^{-1}$) to the symmetric channel (which doesn't).
   **Observed**: electromagnetism is $\sim 10\%$ of the strong
   force at the constituent scale.  **Status: consistent.**

2. **Pair creation residual.**
   $E(e^-) + E(e^+) = 3(q - q^{-1}) \approx 0.630$ Skein units
   ([pair creation energy](#rem:pair-creation-energy)).
   If $q = q^{-1}$, pair creation would produce zero net crossing
   energy.  The nonzero residual is the Coulomb repulsion that
   drives the pair apart.  **Observed**: pairs fly apart.
   **Status: consistent.**

3. **Fine structure constant.**
   $\alpha_{\mathrm{EM}}^{-1} = [9]_q [10]_q / q^{-1} = 136.84$
   vs measured $137.036$
   ([fine structure](#rem:fine-structure-observation)).
   The $q^{-1}$ in the numerator (not $q$) reflects the asymmetry:
   the electromagnetic coupling is set by the *antiparticle*
   crossing weight.  **Observed**: $0.14\%$ discrepancy.
   **Status: close but not exact.**

4. **CP violation.**
   $\delta_{\mathrm{CP}} \sim 10^{-3}$ for kaons
   ([CP violation](#rem:cp-violation-evidence)).
   The complex-$q$ residual phase accumulates crossing-by-crossing,
   and the asymmetry $q \neq q^{-1}$ feeds the CKM phase.
   **Observed**: $\sim 2 \times 10^{-3}$ for kaons.
   **Status: right order of magnitude.**

**Summary.**

| Manifestation | QOU prediction | Observed | Status |
|--------------|---------------|----------|--------|
| Physical mass asymmetry | $= 0$ (CPT restored) | $< 10^{-9}$ | Consistent |
| EM/strong ratio | $\tanh(\ln q) = 0.104$ | $\sim 0.1$ | Consistent |
| Pair creation residual | $3(q - q^{-1}) = 0.630$ | Pairs repel | Consistent |
| $\alpha_{\mathrm{EM}}^{-1}$ | $136.84$ | $137.036$ | $+0.14\%$ |
| $\delta_{\mathrm{CP}}$ (kaons) | $\sim 10^{-3}$ | $\sim 2 \times 10^{-3}$ | Right order |

The $q^2$ Skein-scale asymmetry is the **common origin** of the
EM/strong ratio, pair creation energetics, fine structure constant,
and CP violation.  These are four independent observations explained
by a single structural fact: $q \neq 1$ makes positive and negative
crossings inequivalent.
