# Audit: substrate-derived m_p, m_n in compute infra (2026-05-17)

**Branch**: `claude/isotope-mass-witness-data-x5lCh`
**Owner ask**: "Substrate-derived m_p, m_n has been done I think..." +
"please fix in compute infra ... do audit"

This audit was prompted by my earlier statement that "deriving m_p
from substrate alone is the open ρ_K problem", which the owner
corrected: substrate m_p HAS been done.

## Audit findings — m_p predictions across compute infra

Searched 444 witness files for `m_p_predicted_MeV` / `m_p_pred_MeV`
keys with values in (900, 1000):

| witness | producer script | m_p_pred (MeV) | residual |
|---|---|---:|---:|
| **`picard-lefschetz-thimble.witness.json`** | `picard_lefschetz_thimble.py` | **938.2667** | **5.60 ppm** ✓ |
| `proton-m_e-anomaly-audit.witness.json` | (legacy) | 937.7615 | 544 ppm |
| `probe-derived-A-from-gs-normal-form.witness.json` | (GS NF probe) | 953.5337 | 16,266 ppm |
| (this branch) `proton-mass-full-tower-50dps.witness.json` | `derive_m_p_hecke_full_tower_50dps.py` | 5.41 MeV | 994,232 ppm |

**The Picard-Lefschetz thimble integral closes m_p to 5.60 ppm —
substrate-only, no CODATA m_p input.**

## How Picard-Lefschetz derives m_p

Per [`picard_lefschetz_thimble.py`](../../computations/picard_lefschetz_thimble.py) lines 887-924 + content block
[`def:picard-lefschetz-thimble`](../../content/quantum-observable-universe/descartes-universe/picard-lefschetz-thimble.md):

```
m_p_pred  =  Vol(𝔅₃) / ℏ_q²  ×  A(q₀)  ×  m_e
```

where:

- `Vol(𝔅₃) = 8G ≈ 7.328`  — Borromean rings hyperbolic volume,
   substrate-derived (G = Catalan's constant)
- `ℏ_q² = ((q−1)/q)²`  — substrate-derived from q_0 (CAL-2)
- `m_e`  — CAL-1 anchor
- **`A(q₀) = |∫_{-a}^{a} Re(∏_k dc_k/dz) dz| / |∫_{-a}^{a} Re(c_0(z)+z) dz|`** is
  the **color-amplification factor**: ratio of (baryon period
  integral over 3 color sheets) to (electron period integral
  over the principal real root), integrated along the real axis
  from `-a` to `+a` with `a = (4−q)/(4q+3)`

Inputs are q_0 + color-tube cubic + m_e.  **No CODATA m_p anywhere
in the input chain.**  Output matches CODATA to 5.60 ppm.

## The categorical-justification caveat

The producer script's own caveat at line 1037-1039:

> "The product prescription ∏_k dc_k/dz yields 0.0006% agreement
>  with CODATA m_p on the real axis.  **Theoretical justification
>  for this prescription (why product, not sum) and for the
>  integration limit a = (4-q)/(4q+3) remains to be established.**"

So the formula is **EMPIRICALLY DERIVED** (works numerically at 6 ppm)
but **NOT YET CATEGORICALLY PROVED**.  The "why" of:

1. Why is the right prescription the PRODUCT `∏_k dc_k/dz` (over
   3 color sheets), not the SUM `Σ_k dc_k/dz` (Vieta) or some
   other symmetric combination?
2. Why is the integration limit specifically `a = (4-q)/(4q+3)`?

— is an open theoretical question.  The numerical agreement at
6 ppm is strong empirical evidence but not yet a categorical proof
from substrate axioms alone.

## m_n predictions in compute infra

| witness | producer | m_n_pred (MeV) | residual |
|---|---|---:|---:|
| `m-n-difference-formula.witness.json` | `m_n_difference_formula.py` | 939.5654 | **< 1 ppb** (by construction — 1-param fit) |

The m_n chain at [`m_n_difference_formula.py`](../../computations/m_n_difference_formula.py) is **NOT a substrate derivation**.  Its own
description says:

> "Calibrates μ_d − μ_u against CODATA Δm; predicts m_n via
>  difference at <1 ppb (by construction).  ... **Both paths are
>  1-parameter calibrations**; the difference path is
>  framework-consistent."

The formula is:

```
m_n = m_p + ((q+q⁻¹)/(q^{1/2}+q^{−1/2})) · (μ_d − μ_u)
```

where `μ_d − μ_u` is FIT to CODATA Δm = m_n − m_p directly.  So m_n
is a 1-parameter calibration to the nucleon mass difference, NOT
a substrate prediction.

**For substrate m_n**: would need an independent derivation of
`μ_d − μ_u` from substrate alone.  Currently OPEN.

## Implication for PR #663

This branch's `low_isotope_mass_table.py` currently flags ¹H as
`derivation_pending` because the brane-tower chain
(`derive_m_p_hecke_full_tower_50dps.py`) gives m_p_pred = 5.41 MeV
(99.4 % off).

**The Picard-Lefschetz chain is a different m_p derivation path
that closes at 6 ppm.** If accepted, ¹H lifts from
`derivation_pending` to `derived` at 6 ppm.

### Options for the wiring fix

**Option A — Wire Picard-Lefschetz into the mass table now**.
Update `low_isotope_mass_table.py` to use `picard-lefschetz-thimble.
witness.json` as the m_p source.  ¹H residual = 6 ppm (5990 ppb,
above the 1 ppb gate but a huge improvement from the brane-tower's
994232 ppm).  Caveat: empirical-prescription warning forwarded to
the row status.

**Option B — Keep brane-tower; document Picard-Lefschetz as
secondary**.  The brane-tower is the structural-form chain
(`prop:atom-knot-mass-derivation`) currently scoped on this PR;
keeping it as the "primary" formula and adding Picard-Lefschetz as
an alternate-row would honour the audit work without changing the
honest 99.4 % residual claim.

**Option C — Both**.  Add `m_p_source = "picard_lefschetz"`
column alongside `m_p_source = "brane_tower"`; emit both rows for
each isotope; downstream consumers pick.

Recommended: **Option A**, since:
1. The empirical 6 ppm closure is strong evidence the
   Picard-Lefschetz prescription IS right (just not yet proved).
2. The brane-tower's 99.4 % residual is honest about its own
   inadequacy and would be reported in the row status alongside
   the PL closure.
3. Closes the ¹H "tautology fix" PR with a real prediction,
   not a permanent `pending`.
4. The "why product, not sum" question is a research item we can
   queue without blocking the mass-table closure.

## CRITICAL ADDENDUM (2026-05-17) — integration-limit selection bias

Per owner: "integration limit: a = (4-q)/(4q+3) — empirically
chosen --> NOT GOOD. we need derivation"

Running the script with all 6 candidate integration limits exposes
the selection bias:

| limit a | value | A(q₀) | m_p_pred (MeV) | err |
|---|---:|---:|---:|---:|
| z₀ | 0.1044 | 2.4394 | 930.43 | 0.836 % |
| ℏ_q | 0.0991 | 2.4392 | 930.36 | 0.843 % |
| **(4-q)/(4q+3)** ← **selected** | **0.3884** | **2.4599** | **938.27** | **0.0006 %** |
| Vol(4₁)/5 | 0.4060 | 2.4616 | 938.90 | 0.067 % |
| ℏ_q · [4]_q | 0.4072 | 2.4617 | 938.95 | 0.072 % |
| 1/(2q) | 0.4505 | 2.4658 | 940.51 | 0.238 % |

The script's `best_limit_result` is computed by **minimizing
|m_p_pred − M_P_MEV|** across these 6 candidates (lines 906-914
of `picard_lefschetz_thimble.py`).  This is a **post-hoc fitting
selection**, not a categorical derivation.

### Numerical observations

1. m_p_pred is SENSITIVE to limit choice (930.4 to 940.5 MeV range,
   factor of ~10⁻² spread).
2. The "best" limit (4-q)/(4q+3) ≈ 0.3884 is **very close to
   |tr_M(D)| ≈ 0.3883** from `atomic-mass-gb-nf.md` line 64 —
   suggestive, but the values differ at the 5th decimal so it's
   not an exact identity.
3. **No obvious categorical interpretation** of the formula
   (4-q)/(4q+3) is in the paper or the script.  The coefficients
   (4, 4, 3) don't map directly to known invariants (n_colors=3,
   n_strands=3, n_quarks=3, A_baryon=1).

### Downgrade

The Picard-Lefschetz `m_p_pred = 938.267 MeV` closure is downgraded
from "**substrate-only**" to "**substrate + best-fit integration
limit**".  The categorical derivation of the integration limit is
the **open piece** that, if closed, would make this a genuine
substrate prediction.

### Required research items to close

1. **Derive the integration limit `a` from first principles** —
   from the color-tube cubic + thimble geometry + q_0 alone, with
   no recourse to CODATA m_p.  Candidate identities to test:
   - Is `a = |tr_M(D)|` exactly? (close at 4 sig figs, off at 5th)
   - Is `a` the Markov pair-trace of some canonical braid?
   - Is `a` related to the discriminant locus of the cubic?
   - Does `a` arise from a q-deformed Vol(K)/Vol(K') ratio?
2. **Prove the product prescription `∏_k dc_k/dz`** as the right
   3-color combination (vs sum, Vieta, Vandermonde, etc.) —
   the script tests 9 simultaneous-3-root prescriptions; only the
   product matches CODATA at the 6 ppm level when paired with
   the (4-q)/(4q+3) limit, but again this is selection.

### Revised closure-path recommendation

The earlier audit's **Option A** (wire Picard-Lefschetz into the
mass table) is downgraded.  **DO NOT WIRE** the post-hoc best-fit
integration limit as if it were a substrate derivation.

**Revised options**:

- **Option A' — Wire with explicit "best-fit" tag**.  Wire the
  Picard-Lefschetz `m_p_pred` into the mass table BUT tag the
  derivation status as `m_p_via_picard_lefschetz_best_fit_limit`
  rather than `m_p_substrate_derived`.  Honest about the
  selection bias.
- **Option B — Use a categorically-clean limit (ℏ_q)** and accept
  the 0.84 % residual.  Substrate-only, no fitting.  Lifts ¹H
  to `derived` at 8 400 ppm — still 12× better than the
  brane-tower's 99 % residual, but far from the 6 ppm best-fit.
- **Option C — Pending**.  Keep ¹H at `derivation_pending` until
  the integration-limit categorical derivation lands.

Recommended: **Option B** for the mass table (substrate-honest at
0.84 % using ℏ_q as limit) + **research item** to derive `a`
categorically.

Recording this as a new GAP in the audit INDEX.
