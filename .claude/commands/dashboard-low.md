---
description: Mass-binding dashboard for the LOW isotopes (²H–⁷Li). Prints binding B, error (B_AME/B), and mass M for the forms the producer actually reports (B_can⁰ / B_sym / B_tetra / B_qCLT_fac / E_C) against AME2020, from the one canonical Jones–Markov trace at α = E₀. No args.
---

Run the **low-isotope** mass-binding dashboard and present its tables verbatim.

```bash
python3 computations/mass_binding_dashboard.py --group low
```

Render the script's markdown tables directly to the user — they are already
GitHub-flavoured markdown. Then, if useful, add a one-line reading.

## 🛑 Read before presenting any number (updated 2026-11-20)

**α is the TOWER-SUMMED E₀ by default** — `m_e/(q₀(q₀−1))/(1−ℏ_q²)` =
4.2275 MeV, canonical by the 2026-09-03 full-tower ruling (`qbeta_e0.canonical`,
series open, bean `qou-y3bm`). Until 2026-11-20 the dashboard used the
order-zero 4.1860 MeV; every α-proportional binding column moved +0.991 %
(e.g. ²H B_sym 2.83 → 2.86, ⁴He 8.68 → 8.77). `--e0 order0` reproduces the
historical figures. `m_can` (Borromean brane tower) does not use α and is
unchanged.

**The log-path float64 collapse is drained.** The closed-form chain matches the
exact p(3A) trace to ~1e-49 MeV at 50 dps (measured 2026-11-20: 6.9e-50 at ²H,
8.6e-50 at ⁷Li). The old `_scalars()` and the `8.9e-16 MeV` footnote are gone.
**Not drained:** `q0 = float(_Q50)` in `_row` still feeds `W_lambda_float`
(the B_gate / B_vol columns, which overflow at ⁴⁰Ca/⁵⁶Fe) and `main()` casts
the CODATA m_p/m_n to float for display — open PR #8082, bean `qou-4ohh`.

**The n row's +501 ppb is the RETIRED mixed-base Q_β** (`derived_masses.
q_beta_kashiwara_n2_mev`, published z = 1 functional, convention-C ladder). It
is NOT the L2 scorecard's m_n (+1.389e5 ppb on the ruled z_D base). The
dashboard prints this stamp; quote both or neither.

**The Lean-build line is a stale file** (`build-logs/lean-build-status.json`,
2026-06-07). The dashboard now labels it STALE past 30 days; it is not evidence
about the current tree.

## Context to surface when presenting

- Every binding form is evaluated from the **one canonical transfer trace**
  `tr_m_atom_zn`; **B_AME** is the AME2020 experimental binding
  (`data/ame2020.json`). α = E₀ = m_e/(q₀(q₀−1)) ≈ 4.186 MeV.
- **Exactly one witness is read** —
  `computations/m-p-substrate-identity-50dps.witness.json`, for the constituent
  `m_p` / `m_n`. Everything else is computed live in-process at 50 dps, so most
  of the dashboard cannot be stale. That witness is self-stale by `scriptHash`
  with an unresolvable `commitSha`; re-running moves the payload by 1.7e-17
  (a drained float64 `m_e`), and **it should not be refreshed from a container
  lacking clarabel / mpmath 1.4.1** — doing so trades 1.7e-17 for a weaker
  environment stamp and four new raw-float64 fields.
- Its `allPassed: false` is **real physics, not a defect**: `m_n` misses CODATA
  by 501.43 ppb against a 10 ppb target.

## The forms the headline table actually prints

Verified at `mass_binding_dashboard.py:1115`:
`B_AME | σ_exp | B_can⁰ | B_sym | B_tetra | B_qCLT_fac | E_C`.

- `B_sym = α·ln(tr_free/tr_atom)` — the exact log-trace. **Compositional**:
  `B_sym = m_sym(atom) − Σ m_sym(free GB components)` with
  `m_sym(W) = −α·ln(tr_M(W))`, because `tr_free = tr_p^Z·tr_n^N`.
- `B_qCLT_fac = α·(A−1)·⟨bond-type L⟩` — the **p↔n colour-weighted** q-CLT.
- `B_can⁰`, `B_tetra` — see the producer's own tag table.
- `E_C` — Coulomb term, tagged `DERIVED*` and **conditional on an open
  Witten-κ Gram-determinant `sorry`**, plus an `A^(1/3)` saturation assumption.

**`B_sym` and `B_qCLT_fac` are tagged `POSITED`, not derived.** The log's
extensivity follows from the Markov property, but no block in the corpus
licenses `α·ln(ratio)` as an energy. The values are exact; the identification
is asserted. Do not present them as derived.

**`B_tetra` is exploratory and is not a result** — errors of 118×, 101×, 98×,
105× on the four lightest nuclei.

`B_lin` and `B_qCLT` are computed but demoted out of the headline table.
**There is no `B_magic`** — it occurs zero times in the producer; earlier
versions of this file advertised it.

The forms are **not** defined in `standard-part-functor.md`. The producer's own
docstring retracts that citation (corrected 2026-08-25): that block defines the
standard-part map `st: No_fin → ℝ` and the functor `St`, and contains no `B_`
form, no α and no binding.

**Exploratory** — no production rewire, no fit.

Sibling command: `/dashboard-sweep` (a low→high spread).
