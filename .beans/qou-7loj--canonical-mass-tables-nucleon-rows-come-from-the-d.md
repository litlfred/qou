---
# qou-7loj
title: Canonical mass table's nucleon rows come from the DEPRECATED Vol·ρ witness (+2.89%)
status: todo
type: task
created_at: 2026-08-08T22:39:53Z
updated_at: 2026-08-08T22:39:53Z
---

Found 2026-08-08 while triaging `qou-efcv` (PR #4822 follow-on). **Not a prose
defect — a live compute-wiring one**, and it survives every existing guard.

## The chain

`canonical_mass_table_extended.py::lookup_nucleon_mass_borromean` (lines
331–376) reads the free-nucleon rows out of a witness file:

```
m-p-borromean-verification-50dps.witness.json   # computedAt 2026-07-02, q0Anchor: muon
  data.proton.m_p_pred_MeV  = 965.38447552523690767   # +2.89 % vs CODATA 938.27
  data.neutron.m_n_pred_MeV = 966.71477359056614042   # +2.89 % vs CODATA 939.57
  data.proton.vol_density_borromean_q0 = 1890.51…     # ← the deprecated form, by name
```

Those land in the table as `prediction_type="mass"`,
`prediction_method=CANONICAL_TRACE`, and propagate:

    m_p_borromean_verification_50dps.py            (Vol·ρ · λ_A — DEPRECATED 2026-06-24)
      → m-p-borromean-verification-50dps.witness.json
        → canonical_mass_table_extended.py         (nucleon rows)
          → canonical-mass-table-extended.witness.json
            → low_isotope_mass_table.py            ("via the canonical pipeline")
              → low-isotope-mass-table.witness.json
                → m_qclt_approx.py                 ("framework-predicted nucleon masses … production")

Per [`docs/canonical-mass-formula-guardrail.md`](../docs/canonical-mass-formula-guardrail.md)
the canonical absolute nucleon mass is the muon-anchored Hecke energy,
`m_p = 2·(m_μ·F_Bor − 6·m_e) ≈ 938.27 MeV`, and **every** absolute-mass
consumer must route through the `canonical_mass.py` facade. This chain does
not: it is 27 MeV/nucleon (+2.89 %) high, under a `CANONICAL_TRACE` label.

Corroborating: `mass-table-comprehensive.witness.json` — which *does* route
through the facade — carries `m_p = 938.272089`. Two committed production
mass tables disagree on m_p by 2.89 %.

## Why no guard sees it

A fourth surface, beyond the three PR #4822 mapped:

| guard | scope | why it misses this |
|---|---|---|
| `canonical_mass_status_guard.py` (.md) | prose | not prose |
| …`--scan-py` (new) | docstrings | not a docstring — the formula is nowhere in the text |
| `noncanonical_reentry_audit.py` | AST call sites | **no import and no call** — the hop is `json.loads` of a witness path, so there is no edge to find |

The deprecated value crosses the boundary as **data**. Both audits are
source-code readers; a witness-to-witness dataflow is invisible to both. That
is the generalisable finding, not just this one wire.

## Next steps (not done here — needs a working compute env)

1. Decide the intended semantics: should the extended table's nucleon rows come
   from `canonical_mass.nucleon_mass_mev()` (facade, 938.27), or is the
   Borromean-tower column deliberately the historical Vol·ρ figure? If the
   latter it must not be `prediction_method=CANONICAL_TRACE`, and the label
   must say which form it is.
2. Re-emit the affected witnesses (`canonical-mass-table-extended`,
   `low-isotope-mass-table`, anything projecting them). **Blocked in the
   PR #4822/#4826 sandbox: `mpmath` is not installed**, so this was not
   attempted rather than half-done.
3. Consider a witness-level guard — the surface no existing audit covers:
   flag any witness whose numeric fields sit within tolerance of a known
   deprecated magnitude (965.38 / 966.71 / 966 / 406) while claiming a
   canonical `prediction_method`. That closes the class, not the instance.

Docstring pointers to this were added in PR #4826
(`m_p_borromean_verification_50dps.py`, `m_qclt_approx.py`) so a reader hits
the warning at either end of the chain; the wiring itself is untouched.

## 2026-08-08 — CODE FIXED and verified; WITNESSES STILL STALE (PR #4833)

`lookup_nucleon_mass_borromean` → `lookup_nucleon_mass_canonical`, now calling
`canonical_mass.nucleon_mass_mev()`. The old name is kept as an alias so an
older call site is visible at review rather than silently resurrecting the
route. The CODATA *reference* was also being read out of the same deprecated
witness — that is what kept each row's `err_ppm` looking self-consistent while
the prediction sat 2.89 % off — so it now comes from `codata_constants`.

Verified by direct call (mpmath 1.4.1 installed into the sandbox):

| row | was | now | CODATA | err |
|---|--:|--:|--:|--:|
| proton  | 965.384476 (+2.890 %) | 938.272089427 | 938.272088160 | **+1.35 ppb** |
| neutron | 966.714774 (+2.890 %) | 939.565422765 | 939.565420520 | **+2.39 ppb** |

Those two ppb figures are the ones
[`canonical-mass-formula-guardrail.md`](../docs/canonical-mass-formula-guardrail.md)
independently states for the canonical route — they were not fed in, so the
agreement is a real cross-check, not a restatement. Composite rows return
`(None, None)`; the binding-energy path is untouched.

Locked by `computations/canonical_mass_table_nucleon_rows_test.py` (5/5), which
asserts both the ppb bound and the explicit absence of the two deprecated
magnitudes, so a regression names itself.

### ⚠ Still open — the data

The **committed witnesses are unchanged and still carry 965.384 / 966.715**:

- `canonical-mass-table-extended.witness.json`
- `low-isotope-mass-table.witness.json`
- and the projections `m-qclt-approx`, `multi-layer-gap-decomposition`,
  `lambda-scale-refinements-composed-predictions`

Regeneration needs the `pyhecke_native` Rust wheel for the `tr_M` column, which
is not built in this sandbox (`laurent_q_rust: pyhecke_native missing`), so the
producer cannot run end-to-end here. `mpmath`/`sympy`/`numpy` pip-installed
fine; only the Rust extension is missing. Re-run in an env with the wheel:

    python3 -u canonical_mass_table_extended.py 2>&1 | tee /tmp/cmte.log
    python3 -u low_isotope_mass_table.py        2>&1 | tee /tmp/limt.log

Note the sandbox has mpmath **1.4.1** where the witness recorded **1.3.0**;
regenerate on the pinned version so unrelated last-digit churn does not land.

**Honest note:** an exploratory `--atoms p,n` run of the producer overwrote
`canonical-mass-table-extended.witness.json` with an errored (0-row) result.
Reverted immediately via `git checkout --`; verified restored (7 rows) and the
working tree is clean. That producer writes its witness even when every row
errors, which is worth fixing separately.

### Still worth doing: the class, not the instance

A witness-level guard — flag any witness whose numeric fields sit within
tolerance of a known deprecated magnitude while claiming a canonical
`prediction_method`. That closes the fourth surface; this fixes one wire on it.
