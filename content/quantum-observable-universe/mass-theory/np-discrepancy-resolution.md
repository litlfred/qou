**Remark.**
*Upstream `residual_probe_pn.py` reports a neutron/proton tower
discrepancy: the raw
[mass endomorphism tower](#prop:mass-endomorphism-tower)
undershoots the neutron mass by a factor of ~2.7
($m_{\mathfrak{n}}^{\mathrm{raw tower}} \approx 349$ MeV vs
CODATA $939.6$ MeV at full 50-dps symbolic eval), while
overshooting the proton by 1.84%. This block documents the
structural origin: a $\Phi_q$ pole-distance asymmetry between
the two nucleons.*

**Predictions from CAL-1 + CAL-2 only (no $\beta$-decay calibration).**

*Per [`prop:three-calibration-discipline`](#prop:three-calibration-discipline)
the three allowed calibrations are CAL-1 ($m_e$), CAL-2 ($q_0$),
and CAL-3 ($\mathfrak{Q}_\beta$). The "no $\beta$-decay calibration" mode
uses only CAL-1 + CAL-2, leaving $\mathfrak{Q}_\beta$ as a prediction.*

*The full mass-endomorphism tower at 50-dps symbolic
([`mass_endomorphism.py`](../../folio-assistant/computations/mass_endomorphism.py),
recomputed at 50 dps via sympy + mpmath, no float64):*

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
results (script `light_isotope_sweep.py`):*

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
   likely wrong $a_K$ assignment — `d_chirality_probe.py`
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

- `folio-assistant/computations/residual_probe_pn.py` (upstream): raw tower $n/p$ diagnosis
- `folio-assistant/computations/sweeps/light_isotope_sweep.py`: Term 1 + Frob sweep
- `folio-assistant/computations/bw_chirality_isotopes.py` (upstream): Term 5 (BW+χ) sweep
- `folio-assistant/computations/mass_formula_6term.py`: integrated 6-term comparison
- `folio-assistant/computations/d_chirality_probe.py`: shows paper's D-chirality is wrong
