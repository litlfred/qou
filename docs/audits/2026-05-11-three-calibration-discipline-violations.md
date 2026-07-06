# Three-calibration-discipline audit — main + open PRs

**Date:** 2026-05-11
**Branch:** `claude/neutron-mass-50dps-chain`
**Trigger:** Author confirmation (2026-05-11) that PR #637's
**three-calibration discipline** (CAL-1 $m_e$, CAL-2 $q_0$, CAL-3
$Q_\beta(n)$ as predicted output) is **normative**.

## Anchor — the normative 3 inputs

Per [`calibration-inputs.md`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/braids-and-knots/calibration-inputs.md)
(the canonical content block) and reinforced by PR #637:

| CAL | Input | What it fixes |
|-----|-------|---------------|
| **1** | $m_e$ (CODATA) | Leptonic mass scale (MeV ruler) |
| **2** | $m_\mu / m_e$ (CODATA) | Substrate parameter $q_0$ |
| **3** | $Q_\beta(n)$ (CODATA) | Hadronic energy scale $E_0$ |

**Consequence:** $m_p$ and $m_n$ are **predictions**, not inputs.
The relation $Q_\beta = m_n - m_p - m_e$ derives $Q_\beta$ from the
substrate-derived $m_p$, $m_n$, $m_e$ — it does **not** authorise
$m_p$ and $m_n$ as 4th and 5th calibration anchors.

This audit identifies sites on `main` (and consequence for open PRs)
that **consume $m_p$ and/or $m_n$ as inputs to a predicted quantity**
— direct violations of the normative discipline.

## Violation classes

| Class | Use of $m_p$, $m_n$ | Verdict |
|-------|---------------------|---------|
| **A. Hard violation** | Consumed as input to a formula whose output is presented as a *prediction* | Must be reframed |
| **B. Audit-only / informational** | Compared against, residual extracted from CODATA atomic-mass tables, never claimed as substrate-derived | OK — flag with "audit-only" status |
| **C. Diagnostic / probe** | Used for analysis of substrate-side errors, not for prediction | OK — internal tooling |
| **D. CODATA registry** | Re-export of CODATA values, downstream consumers tag their own status | OK — registry by design |

## Hard violations (Class A)

### Content block

**[`recomputed-low-isotope-mass-table.md:75–80`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/braids-and-knots/recomputed-low-isotope-mass-table.md)**

> *The 0.000 % on $p$ and $n$ is a tautology, not a prediction.*
> *The ρ_K leading-order ansatz is built from $m_p$ and $m_n$
> directly, so for $K = p$ ($Z = 1, N = 0$) and $K = n$ ($Z = 0,
> N = 1$) the formula returns the input mass exactly. This is by
> construction; **the framework's three CAL inputs are $m_e$, $m_p$,
> $m_n$ (CODATA), with $Q_\beta = m_n - m_p - m_e$ derived.***

This explicitly asserts $\{m_e, m_p, m_n\}$ are the 3 CAL inputs —
**directly contradicting** `calibration-inputs.md` and PR #637's
discipline. The mass table at lines 67–68 then reports
"0.000 % rel err" for $p$ and $n$ — labeled as a "tautology" but
still presented as the mass-table prediction.

**Fix:** Rewrite the "Two structural notes" section (lines 73–88)
to:
1. Flag the ρ_K LO formula as **post-calibration / illustrative**,
   not a substrate-only prediction.
2. Replace the 5-anchor framing with the 3-anchor discipline.
3. Mark the $p, n$ rows as "calibration anchors (tautology)" rather
   than predictions; the genuine substrate-only predictions for
   $\{p, n\}$ live in the Φ_q tower path (PR #637: +1.84% / −62.9%).
4. Keep the $D, T, ^3\mathrm{He}$ predictions and their
   $\Delta$-column residuals, but label them as
   "post-calibration ρ_K LO sanity check" rather than
   "substrate-only prediction".

### Script

**[`atomic_mass_via_rho_k.py:188`](https://github.com/litlfred/qou/blob/main/computations/atomic_mass_via_rho_k.py)**

```python
def rho_K_leading_order(Z: int, N: int, abs_tr_M: mp.mpf) -> mp.mpf:
    """ρ_K^{LO}(Z, N) = (Z·m_p + N·m_n) / (m_e·|tr_M(K)|)."""
    return (Z * M_P_MEV + N * M_N_MEV) / (M_E_MEV * abs_tr_M)
```

The numerator $Z \cdot m_p + N \cdot m_n$ uses **both** CODATA $m_p$
and $m_n$. By construction the function returns $\text{CODATA mass} /
(m_e \cdot |\mathrm{tr}_M|)$, so `predict_mass(Z, N, ...)` returns
the CODATA mass identically for $\{p, n, A=1\}$. The "0.23% MAE on
$D, T, ^3\mathrm{He}$" is a post-calibration interpolation, not a
substrate-only prediction.

**Fix:** Either
- Reframe the script's docstring and output as "post-calibration
  ρ_K LO interpolation" (audit-only), OR
- Deprecate this script and replace its downstream consumers with
  the Φ_q substrate-only path from PR #637.

## Audit-only / informational (Class B) — no fix required

These scripts consume $m_p$, $m_n$ as inputs but only to **extract**
empirical binding energies from CODATA atomic masses (working
*backwards*, not claiming substrate-derived predictions):

| Script | Pattern | Status |
|--------|---------|--------|
| [`atom_mass_additive_baseline.py:76`](https://github.com/litlfred/qou/blob/main/computations/atom_mass_additive_baseline.py) | $M_\text{free} = Z m_p + N m_n + Z m_e$ → $\Delta_\text{binding} = M_\text{free} - M_\text{AME}$ | OK (baseline extraction) |
| [`isotope-mass-table.py:261`](https://github.com/litlfred/qou/blob/main/computations/isotope-mass-table.py) | Same pattern, comparison table | OK |
| [`channel_product_mass.py:102,121`](https://github.com/litlfred/qou/blob/main/computations/channel_product_mass.py) | Same pattern | OK |
| [`unified-mass-molecular.py:227,351`](https://github.com/litlfred/qou/blob/main/computations/unified-mass-molecular.py) | Same pattern | OK |
| [`categorical_q_decay_ba_low_isotopes.py:351`](https://github.com/litlfred/qou/blob/main/computations/categorical_q_decay_ba_low_isotopes.py) | Constituent mass for $\beta$-decay $Q$-value extraction | OK |
| [`path_b_defect_binding_probe.py:80`](https://github.com/litlfred/qou/blob/main/computations/probes/path_b_defect_binding_probe.py) | Baseline | OK (probe) |
| [`delta_lambda_empirical_tabulation.py:395`](https://github.com/litlfred/qou/blob/main/computations/delta_lambda_empirical_tabulation.py) | `# = ρ_K^LO · m_e · |tr_M|` — comment explicitly identifies the additive baseline with the ρ_K LO prediction | **Caveat: documents the tautology directly; safe under Class B framing** |

## Diagnostic / probe (Class C) — no fix required

The `probe_neutron_gap_round{2,3,4,5,6}.py`,
`neutron_error_diagnostic.py`, `proton_residual_rootcause.py`,
`proton_m_e_anomaly_audit.py`, `m_n_difference_formula.py` family
are diagnostic tools that consume $m_p$, $m_n$ to *analyse*
substrate-side errors. They do not output substrate-derived
predictions. OK.

## Registry / CODATA re-export (Class D) — no fix required

[`codata_masses.py`](https://github.com/litlfred/qou/blob/main/computations/codata_masses.py),
[`codata_constants.py`](https://github.com/litlfred/qou/blob/main/computations/substrate/codata_constants.py),
[`experimental_constants.py`](https://github.com/litlfred/qou/blob/main/computations/substrate/experimental_constants.py)
re-export CODATA values. Their downstream consumers tag their own
status. OK.

## Existing-on-main legitimacy summary

`atomic_mass_via_rho_k.py` was added in **PR #564** (landed
`86aaeb51a`, ledger row "P4″ · ρ_K assembly path"). At the time it
was framed as a **200× improvement** vs the legacy $E_0$ path. Under
the **new normative** 3-calibration discipline confirmed by #637,
this script's claim of being a "prediction" is incorrect — it is a
post-calibration interpolation. The script itself doesn't need to
be deleted; its **framing in the content block** is what needs to
change.

## Recommendations

1. **(highest priority)** Patch
   [`recomputed-low-isotope-mass-table.md:75–80`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/braids-and-knots/recomputed-low-isotope-mass-table.md)
   to align with the normative 3-input discipline. Mark $p, n$ rows
   "calibration anchors (tautology)"; mark $D, T, ^3\mathrm{He}$
   rows "post-calibration ρ_K LO interpolation".
2. **(coordinate with PR #637)** Add a docstring note to
   `atomic_mass_via_rho_k.py` clarifying its post-calibration role
   and a forward-reference to the Φ_q substrate-only path being
   built on #637.
3. **(after #637 merges)** Audit whether any **other** content
   blocks downstream of `atomic-mass-via-rho-k.witness.json` carry
   "prediction" language; rewrite if so.
4. **(open question for author)** Should the ρ_K LO formula be
   retained as a **calibration cross-check** (informational) or
   formally deprecated in favour of the Φ_q path?  Both currently
   coexist on `main`.

## Out of scope (this audit)

- The 8 Class-B scripts that compute additive nucleon-mass baseline
  to extract binding from CODATA atomic-mass tables — these are
  standard nuclear-physics data analysis.
- The 5 Class-C diagnostic probes.
- The 3 Class-D registry files.
- Lean-side: no Lean theorems consume $m_p$, $m_n$ as predicted
  outputs (verified: `M_P_MEV` and `M_N_MEV` constants don't appear
  outside Python).
