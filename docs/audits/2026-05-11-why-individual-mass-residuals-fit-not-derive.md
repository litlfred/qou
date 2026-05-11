# Why individual-mass residuals are large — fitting vs derivation audit

**Date:** 2026-05-11
**Branch:** `claude/neutron-mass-50dps-chain`
**Trigger:** "we are fitting/guessing not relying on derivation"

## Headline finding

**The framework's substrate-only formulas correctly predict
DIFFERENCES (Q_β, Δm), but the formulas for INDIVIDUAL masses
(m_p, m_n) are not actually derived — they depend on either (a) a
fitted unit-scale, or (b) an implicit ansatz that cat-units ratios
equal physical mass ratios.**

The 999M ppb residual on the substrate-only neutron chain is
honest exposure of (b), not noise.

## What works (genuinely derived)

| Quantity | Substrate path | Result | Status |
|----------|---------------|--------|--------|
| $Q_\beta$ | $\|\Delta(\text{net})\| \cdot E_0$, $E_0 = m_e/(q(q-1))$ | 0.7836 MeV (CODATA 0.7823, **+0.17%**) | ✓ derived from CAL-1 ($m_e$) + CAL-2 ($q_0$) alone |
| $\Phi_q$ closed form | $Q_\beta = m_e \cdot \|q_0^2 - 2 q_0 - 1\| \cdot (q_0+1)/(2 q_0^3)$ | 0.7836 MeV | ✓ pure CAL-1 + CAL-2 |
| $\hbar_q$, $c_q$ | $\hbar_q = (q-1)/q$, $c_q = 1/(q-1)$ | CODATA-matched | ✓ pure CAL-2 |

Pattern: **differences and dimensionless constants** are reachable.

## What doesn't work (fits / guesses creep in)

### Numerical diagnostic — `m_p_pred` is off by ~1570× from Path A alone

Substrate-only Path A (T1 + T4) at $q_0$, **no CODATA mass injection**:

```
m_e_Hecke  =  2.0027  (cat units)
m_p_Hecke  =  2.3414
m_n_Hecke  =  2.1993

Path A ratio  m_p_Hecke / m_e_Hecke  =  1.1691
CODATA       m_p / m_e               =  1836.15
→ Off by factor 1570×  (3 orders of magnitude)
```

The framework's cat-units ratios for individual particles **do not
carry the physical mass hierarchy**. Multiplying by $m_e^{\text{CODATA}}$
gives $m_p \approx 0.597$ MeV, not 938 MeV.

### E_0 conventions don't rescue it — all of them require fitting

Per `docs/audits/2026-05-10-hbar-q-scaling-audit.md`:

| Convention | $E_0$ value | $m_p$ via $E_0 \cdot |\mathrm{tr}_M(\beta_p)|$ | Error |
|------------|-------------|---------------------------------------------|-------|
| A — single-tick $m_e/(q(q-1))$ | 4.186 MeV | 9.80 MeV | −98.96% |
| B — $Q_\beta$-absorbed $Q_\beta/\|\Delta(\mathrm{net})\|$ | 4.179 MeV | 9.78 MeV | −98.96% |
| C — **proton back-fit** | 200 MeV | 468.3 MeV | −50.09% |

Conventions A and B are substrate-derived (CAL-1 + CAL-2 only) but
give $m_p \approx 10$ MeV — far from 938 MeV. Convention C is
**explicitly back-fitted** to give the right ballpark, and even
then it's 50% off.

**No $E_0$ convention reaches $m_p = 938$ MeV from the framework's
$|\mathrm{tr}_M|$-based formula.** The framework is structurally
missing the QCD binding scale.

### Where the "fit" is hiding

| Site | Fitting form | Severity |
|------|--------------|----------|
| `atomic_mass_via_rho_k.py:188` (LO formula) | $\rho_K^{LO} = (Z m_p + N m_n)/(m_e\|\mathrm{tr}_M\|)$ consumes CODATA $m_p, m_n$ | Hard violation per `2026-05-11-three-calibration-discipline-violations.md`; flagged in #637 as "LO TAUTOLOGY NOTICE" |
| `E_0_CONVENTIONS["C"]` | Back-fitted to 200 MeV "proton" anchor | Audited in `2026-05-10-hbar-q-scaling-audit.md`; flagged but not removed |
| Old `M_HECKE_PIPELINE_AT_Q0_LEGACY["p"] = 1.4283` | Numerologically tuned to $(m_p - m_e)/m_e$ ratio | Quarantined to `_LEGACY` dict by #637 |
| **Cat-units $\to$ MeV via ratio with $m_e$** | Assumes `m_X_Hecke / m_e_Hecke = m_X / m_e` | **Implicit ansatz, not derived**; this is the structural issue |

The last row is the deepest issue and the one closest to "fitting
by assumption". The framework writes:

$$
  m_X^{\text{pred}}\;=\;\frac{m_X^{\text{Hecke}}}{m_e^{\text{Hecke}}}\cdot m_e^{\text{CODATA}}
$$

with no derivation that the ratio $m_X^{\text{Hecke}}/m_e^{\text{Hecke}}$
equals the physical $m_X/m_e$. Empirically it doesn't:
$m_X^{\text{Hecke}}/m_e^{\text{Hecke}} = \mathcal{O}(1)$ for any
particle the framework's $|\mathrm{tr}_M|$-based formula touches,
while physical mass ratios span $\mathcal{O}(10^3)$ at the proton scale.

## Why differences work but absolutes don't (structural reason)

The framework's $|\mathrm{tr}_M|$ is a **topological invariant** of
the braid — it captures crossing structure, bar-involution behavior,
and Hecke-algebra normal forms. It does **not** capture:

- Quark masses ($m_u, m_d, m_s$) — these are SM inputs the
  framework doesn't currently consume.
- QCD binding scale ($\Lambda_{\text{QCD}} \approx 200$ MeV) — the
  dominant contribution to proton mass via gluon-field energy.
- Electromagnetic energy splitting.

The proton and neutron are both 3-strand braids in $H_3$ with 11
crossings. Their topological difference is small — one $\sigma$ vs
$\sigma^{-1}$ in the (u,u,d) vs (u,d,d) flavor encoding. Indeed
$|tr_M(\beta_p)| - |tr_M(\beta_n)| \approx 0.14$ at $q_0$ — small
compared to $|tr_M|$ itself ($\sim 1$). That topological difference
**can** be derived; multiplying by an $E_0$ derived from
CAL-1 + CAL-2 gives $Q_\beta = +0.78$ MeV, matching CODATA to
+0.17%.

But the absolute mass of either particle requires the full QCD
energy — which the topology-only framework doesn't carry.
Multiplying $|tr_M|$ by any $E_0$ derived from CAL-1+CAL-2 gives
$\mathcal{O}(\text{MeV})$, not $\mathcal{O}(\text{GeV})$. The
1570× / 3-orders-of-magnitude gap is **inherent**, not numerical.

This is what PR #637 calls "the substrate-only framework is
honest about the residual" — the 1.84% / −62.9% errors on
individual nucleon masses (via the Φ_q tower path) are the
framework's actual state, not a numerical issue to close.

## Recommended reframing

| Quantity | Status under current framework | Recommendation |
|----------|-------------------------------|----------------|
| $Q_\beta(n)$ | **DERIVED** to +0.17% via $\Delta(\text{net}) \cdot E_0$ | Keep as substrate-derived prediction (also CAL-3 calibration anchor, but the closed form ≈ CODATA). |
| $\Delta m = m_n - m_p$ | DERIVABLE via $Q_\beta + m_e$ (Δ(net) approach) | Same as $Q_\beta$. |
| $m_p$, $m_n$ individually | **NOT DERIVED** — gap of $\sim 10^3$ to CODATA | Reframe paper's claim: the substrate-only framework predicts mass DIFFERENCES (Q_β, isospin splits), not absolute hadron masses. Absolute masses require QCD binding-scale input. |
| $m_e$ | CAL-1 (definitional anchor) | Keep. |
| $m_\mu$ | DERIVED via $m_\mu = m_e \cdot \mathrm{Vol}(4_1) / \hbar_q^2$ | Keep. |

The current `recomputed-low-isotope-mass-table.md` already flags
the $(p, n)$ rows as "calibration tautology, not a prediction
quality" (post-#637). The next iteration should extend this honesty
to the broader **paper-level claim about predicting absolute
nucleon masses** — the framework does not currently do that.

## What this means for the neutron-chain residual on PR #640

The 999M ppb residual on `build_neutron_mass_50dps_chain.py` is the
**honest substrate-only deliverable**. No fitting needed to fix it
— the residual IS the deliverable. Closing it would require:

1. Adding a QCD-scale calibration input (would be CAL-4, violating the
   3-input discipline).
2. OR closing the brane-tower $n_\star$ truncation rule
   (`brane-tower-z-habiro` open conjecture) to bring T2+T3 in for A=1
   — speculative.
3. OR fundamentally restructuring the framework to encode flavor
   information ($u$ vs $d$ quark) at the braid level.

None of these are 1ppb-trail items. The 1ppb target was always for
$Q_\beta$ (which works), not for individual $m_p / m_n$ (which
don't).

## Action items

1. **Update PR #640 description** to clearly state the residual is a
   structural exposure, not a fit-to-close target. (chain itself
   already says this in its notes.)
2. **Coordinate question for author**: should the paper claim that
   the framework predicts absolute nucleon masses, or only mass
   differences and ratios? Current state implies the former; the
   evidence supports only the latter.
3. **Optional**: deprecate `E_0_CONVENTIONS["C"]` (the 200 MeV
   back-fit) since it's explicit fitting per the 3-cal discipline.

## Cross-references

- `np-discrepancy-resolution.md` (on main, post-#637) — same finding from a different angle.
- `derived_masses.py` (on main, post-#637) — the Q_β closed form.
- `2026-05-10-non-calibrated-mass-state-of-play.md` — comprehensive state of play.
- `2026-05-10-hbar-q-scaling-audit.md` — three E_0 conventions audited.
- `2026-05-11-three-calibration-discipline-violations.md` — earlier audit on the m_p, m_n input violations.
