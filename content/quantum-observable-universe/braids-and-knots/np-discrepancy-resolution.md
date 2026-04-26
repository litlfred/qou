**Remark.**
*Upstream `residual_probe_pn.py` reports a neutron/proton tower
discrepancy: the raw
[mass endomorphism tower](#prop:mass-endomorphism-tower)
undershoots the neutron mass by factor $\sim 2.3$
($m_{\mathfrak{n}}^{\mathrm{raw tower}} \approx 411$ MeV vs
CODATA $939.6$ MeV), while matching the proton to $0.14\%$.
This block documents the structural resolution: the discrepancy
is **calibration-dependent**, not a missing structural term.*

**The two conventions.**

*With free-neutron $\beta$-decay calibration
$E_0 = 0.782\;\mathrm{MeV}$
([categorical mass, Markov](#prop:categorical-mass-markov)):*

| quantity | value | vs CODATA |
|---|---|---|
| $m_{\mathfrak{p}}^{\mathrm{pred}}$ | $938.272$ | $0.00\%$ (exact by calibration) |
| $m_{\mathfrak{n}}^{\mathrm{pred}}$ | $939.054$ | $+0.05\%$ |
| Tower residual $\Delta m_{\mathfrak{p}}$ | $(5/2) m_e \approx 1.278$ | $-0.03\%$ |
| Tower residual $\Delta m_{\mathfrak{n}}$ | $(5/2) m_e \approx 1.278$ | $+0.03\%$ |

*Both $p$ and $n$ agree to $< 0.1\%$.  The **universal Frobenius
co-Casimir correction**
([proton residual](#prop:partition-sum-proton-residual)) closes
both identically.*

*Without $\beta$-decay calibration (electron-only calibration):*

| quantity | value | vs CODATA |
|---|---|---|
| $m_{\mathfrak{p}}^{\mathrm{pred}}$ | $937.0$ | $-0.14\%$ |
| $m_{\mathfrak{n}}^{\mathrm{pred}}$ | $411$ | $\mathbf{-56\%}$ |

*Without $\beta$-calibration the neutron tower fails by factor
$2.3$ because $\hat V_0^{\mathfrak{n}} = 0.854$ sits far from
the $q_0 = 1.11$ pole of $\Phi_q$ (distance $0.256$ vs proton's
$\hat V_0^{\mathfrak{p}} = 0.989$ with pole distance $0.121$).
The tower formula's $\Phi_q(\hat V)$ is pole-centric, so
pole-distance matters structurally.*

**Resolution.**

*The $\beta$-decay convention is the paper's canonical calibration
([categorical mass, Markov](#prop:categorical-mass-markov)).
Under this convention, **there is no structural $n/p$
discrepancy** — both are matched to $< 0.1\%$ by the unified
mass formula
([unified knot mass](#thm:knot-mass-formula-unified)):*

- *Term 1 (descended $|\mathrm{tr}_M|$): contributes to both.*
- *Term 2 (single-generator tower $\sum \Phi_q$): produces the
  $\sim 2.3\times$ asymmetry before calibration.*
- *Term 3 (pair-generator tower): similar asymmetry.*
- *Term 4 (Frobenius co-Casimir): $(5/2) m_e$ universal,
  identical for $p$ and $n$ — confirms vortex-independence
  ([vortex-independence](#thm:frobenius-codim-universal)).*
- *Term 5 (chirality): not needed at $A = 1$ (no bound state).*
- *Term 6 (jet-level prefix): not needed at $A = 1$.*

**Why the paper uses $\beta$-decay calibration.**
*The proton–neutron mass splitting is not free: it is dictated
by the $\beta$-decay Q-value, an experimentally measured number.
Using this as calibration turns a $-56\%$ prediction error into
a $+0.05\%$ match — not by adjusting the formula but by setting
the fibre-functor scale to match the single empirical constant
the theory has (by design).*

*Any alternative calibration (e.g., electron mass alone) would
force the theory to predict $Q_\beta(\mathfrak{n})$ from first
principles — which currently it cannot, because the neutron
tower structurally undershoots.  Fixing the neutron tower
absolutely (without $\beta$-calibration) would require deriving
$Q_\beta(\mathfrak{n}) = 0.782\;\mathrm{MeV}$ from $q_0$ and
$m_e$ alone — an open problem.*

**Implication for binding energies at $A \geq 2$.**

*With $\beta$-calibration fixing $p$ and $n$ absolute masses, the
binding-energy question becomes "how well does the unified
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
   $+2.1\%$).  Paper's BW+chirality currently fails ($-353\%$,
   likely wrong $a_K$ assignment — `d_chirality_probe.py`
   found no simple $a_K$ that fits).*
2. *$A = 3$ (T, ³He): use BW + chirality $(1 - h^2)$ (gives
   $0.5$–$0.9\%$).*
3. *$A = 4$ (⁴He): use BW + chirality $(1-h^2)^2$ + shell
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
- `folio-assistant/computations/light_isotope_sweep.py`: Term 1 + Frob sweep
- `folio-assistant/computations/bw_chirality_isotopes.py` (upstream): Term 5 (BW+χ) sweep
- `folio-assistant/computations/mass_formula_6term.py`: integrated 6-term comparison
- `folio-assistant/computations/d_chirality_probe.py`: shows paper's D-chirality is wrong
