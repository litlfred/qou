---
description: Mass-binding dashboard for the LOW isotopes (²H–⁷Li). Prints binding B, error (B_AME/B), and mass M for the forms the producer actually reports (B_can⁰ / B_sym / B_tetra / B_qCLT_fac / E_C) against AME2020, from the one canonical Jones–Markov trace at α = E₀. No args.
---

Run the **low-isotope** mass-binding dashboard and present its tables verbatim.

```bash
python3 computations/mass_binding_dashboard.py --group low
```

Render the script's markdown tables directly to the user — they are already
GitHub-flavoured markdown. Then, if useful, add a one-line reading.

## 🛑 Read before presenting any number

**The producer computes in float64.** `_scalars()` (line 314) returns
`float(mex), float(q0x), float(e0x)`, so m_e, q₀ and α are downcast and every
binding number below is float64 with `math.log` / `math.exp`. Consequences when
presenting:

- **No digit past ~1e-16 relative is meaningful.** The proton row's
  `err m_can` has roughly four good figures, not seven.
- **Do not repeat the printed `Δ vs exact trace` figure or its
  `max|Δ| = 8.9e-16 MeV` footnote as an identity.** On an ~8.7 MeV quantity
  that is 1.0e-16 relative — exactly float64 ε, the floor of the arithmetic
  rather than a measurement. Redone in exact arithmetic (mpf end to end,
  `tr_m_atom_zn` at 50 dps) the agreement is **4.28e-50 MeV**, at the 50-dps
  serialisation floor — 34 orders better than printed. Honest phrasing:
  *"agrees to 4.3e-50 MeV at 50-dps compute precision."*

This is a NO-FLOAT64 violation under the 2026-08-18 directive and is invisible
to every gate: the ratchets scan witnesses and this script emits none, the
source-level gates key on `mpf(<float>)` / `mp.dps` / module-consts, and
`mpf_mixed_arithmetic_audit` looks for mpmath↔f64 *mixing*, which this evades by
collapsing to pure float before any arithmetic. Tracked as bean `qou-4ohh`;
**the drain is not done.**

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
