---
# qou-7loj
title: Canonical mass table's nucleon rows come from the DEPRECATED Vol·ρ witness (+2.89%)
status: completed
type: task
priority: normal
created_at: 2026-08-08T22:39:53Z
updated_at: 2026-09-08T04:15:34Z
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

## 2026-08-09 — WITNESSES REGENERATED; and the spectral correction was correcting the artifact

Built the missing `pyhecke_native` wheel in-sandbox (`maturin build --release`,
2m32s), so the producers ran end-to-end after all. The environment ended up
matching the recorded one **exactly** — python 3.11.15 / numpy 2.4.6 / sympy
1.14.0 / mpmath 1.3.0 / pyhecke_native 0.9.0. (My earlier note that the sandbox
had mpmath 1.4.1 was overtaken: installing sympy 1.14 pinned mpmath back to
1.3.0, so the version caveat no longer applies.)

**Reproduction check.** Re-running `canonical_mass_table_extended.py` on the
unfixed rows returned values **bit-identical** to the committed witness — only
`computedAt` / hashes / `durationMs` moved. So the environment reproduces the
corpus, and any number that *did* change is attributable to the fix.

Regenerated:

| witness | p / n before | after |
|---|--:|--:|
| `low-isotope-mass-table` | 965.384 / 966.715 (+2.89 %) | **938.2721 / 939.5654** (+1.35 / +2.39 ppb) |
| `canonical-mass-table-extended` | (no p/n rows under default `branching`) | unchanged numerically; hashes refreshed |
| `m-qclt-approx` | production gap **+2.89 %** | **1.35e-7 %** |

Note the extended table never carried p/n under its default method — the
nucleon rows appear only via the `auto` route the low-isotope wrapper uses,
which is why the defect hid in the wrapper's output rather than the table's.
(Wart, unrelated: the wrapper re-runs the producer restricted to 5 atoms and
so **overwrites** the 7-atom extended witness; the full producer has to be
re-run afterwards. Worth fixing separately.)

### The consequence — a scope-(a) negative worth reading

Regenerating `m-qclt-approx` failed exactly one assertion:
`spectral_correction_reduces_residual_gt_20x`, sourced *"derived θ/(8ℏ²) ≈
0.9711 closes +2.89% → ~-819 ppm"* (the 2026-05-28 audit's ~35× closure).

That closure was measured against a leading term that was +2.89 % high **because
of this defect**. The factor was removing an excess introduced by the deprecated
baseline. Against the canonical leading term it overshoots the other way, to
≈ **−2.89 %** — reduction 0.0028×, i.e. it makes the result worse by almost
exactly the amount it used to "fix".

The assertion is restated in the direction that is now true rather than
deleted, so the finding is recorded. **Scope (a), not (b)**: this says the
factor does not improve *this channel* as a multiplier on the canonical value.
It is **not** a structural exclusion of θ/(8ℏ_q²) — no invariant forbids the
quantity and its derivation is untouched. What is refuted is the +2.89 % →
−819 ppm *closure claim*, which rested on the wrong baseline.

**Follow-up:** `docs/audits/2026-05-28-spectral-phase-correction-derived.md`
needs re-reading against a canonical baseline; any downstream citation of the
"~35× closure" is suspect.

### Deliberately NOT regenerated

- `multi-layer-gap-decomposition` — its L1 layer *is* the deprecated nucleon
  mass and its stated subject is "the +2.89–3.86 % multi-isotope gap". A blind
  re-run would emit a decomposition of a gap that no longer exists under that
  framing. Needs re-scoping first, not a re-run.
- `lambda-scale-refinements-composed-predictions` — a λ_A refinements probe;
  studying the deprecated route is guardrail §3 permitted and correct here.

## 2026-08-09 — correction: the spectral audit's result was NOT invalidated

I over-claimed above and in PR #4839. Re-read of
[`2026-05-28-spectral-phase-correction-derived.md`](../docs/audits/2026-05-28-spectral-phase-correction-derived.md)
against a canonical baseline, with the arithmetic re-verified at 30 dps:

- `966.050 × 0.971120 = 938.150` → **−818.8 ppm** vs m_avg CODATA 938.919.
  The audit's −819 ppm and ~35× are exactly right and **independent of this
  defect** — it derives a correction *to the Vol·ρ·λ_A form*, and never
  claimed to correct the canonical route.
- What actually changed is the result's **role**: canonical m_avg is already
  +1.87 ppb, so composing the factor with it double-corrects (→ 911.802,
  −2.888 %). The narrow true statement is *do not compose this factor with the
  canonical absolute mass* — not "the closure claim is refuted".
- "Every downstream citation is suspect" was also wrong: the sweep found
  **one** consumer, `m_qclt_approx.py`, already handled in #4839.
  `vol_density_borromean_spectral` has no callers; `e0_lambda_composite.py`
  only names the function in prose.

The `m_qclt_approx` assertion text is accurate as written (it is scoped to
that channel); the over-reach was in the PR summary and in this bean, and the
audit now carries a dated §"Re-read against a canonical baseline".


---

## CLOSED 2026-09-08 — the whole chain is canonical on `main`, and BOTH deferred items have since been closed by others

Verified on `main` `29126ed0ed6`, at every hop this bean traced.

### The core defect: fixed at the producer, not papered over

`canonical_mass_table_extended.py::lookup_nucleon_mass_borromean` no longer
reads a witness. It calls the facade:

```python
from canonical_mass import nucleon_mass_mev  # noqa: E402 — facade
return (float(nucleon_mass_mev(species)),
        "canonical_mass facade (muon-anchored Hecke energy)")
```

`del borromean  # retained for call-site compatibility; no longer consulted`,
and the pre-2026-08-08 name is kept as a loud-failure alias *"so an older call
site fails loudly at review time rather than silently resurrecting the +2.89 %
route"*. The 24-line HISTORY docstring records the defect and — the part worth
keeping — **why no guard saw it**: the value crossed as data, so
`noncanonical_reentry_audit.py` had no AST edge.

Every witness downstream in the chain this bean drew now carries CODATA:

| witness | m_p | m_n |
|---|---|---|
| `canonical-mass-table-extended` | 938.27 | 939.56 |
| `low-isotope-mass-table` | 938.27 | 939.56 |
| `m-qclt-approx` | 938.27 | 939.56 |

Not 965.38 / 966.71 anywhere. The 2.89 % disagreement between two committed
production mass tables is gone.

### The two things this bean deliberately left — both now closed, by others

- **The wart** (*"the wrapper re-runs the producer restricted to 5 atoms and so
  overwrites the 7-atom extended witness … Worth fixing separately"*) is fixed
  and carries its own bean: `low_isotope_mass_table.py:104-106` —
  *"Invoke canonical_mass_table_extended.py end-to-end, at FULL coverage.
  Deliberately does **not** pass `--atoms` (bean `qou-xwet`)."* Corroborated by
  the artifact: the committed extended witness holds **9 rows**, not a
  truncated 5.
- **`multi-layer-gap-decomposition`** (*"Needs re-scoping first, not a re-run"*)
  was re-scoped **and** re-run on 2026-08-23, two weeks after this bean's last
  entry. Its L1 layer now reads `pred 938.2720894273243` against
  `actual 938.27208943` — **err −2.7e-09 MeV**, and `total_L1_MeV` is
  **8.22e-07**, down from ~27 MeV/nucleon. Its own per-row `reason` says it:
  *"L1 closed: observed gap −0.000000 % is already below the projected 1.948 %
  (canonical_mass facade; the projection assumes a Vol·ρ-era gap)."*

### One thing found while verifying, NOT part of this bean — filed separately

That same producer's **emitted strings** were not updated with its numbers.
`multi_layer_gap_decomposition.py`'s module docstring is correct
(*"L1 measures **+0.0000 MeV for every atom**"*, *"the Markov × 5/2 projection
is correspondingly **inapplicable**"*), but the two strings it writes INTO the
witness still say *"L1 dominates free-nucleon errors (+27 MeV per nucleon)"* and
*"Structural Markov × 5/2 closes ~14.5 MeV of L1 per free nucleon — a 1.5× gap
closure"*. So the witness — the artifact a downstream reader actually consumes —
contradicts both the file's own docstring and its own computed
`total_L1_MeV = 8.22e-07`. Fixed in this PR under AGENTS.md's
corpus-derived exemption (the file's own docstring fixes the answer).

### The 2026-08-09 self-correction stands and is not disturbed

*"the spectral audit's result was NOT invalidated"* — the −819 ppm / ~35×
closure is correct and independent of this defect; what changed is its **role**
(do not compose that factor with the canonical absolute mass). Nothing here
re-opens that.
