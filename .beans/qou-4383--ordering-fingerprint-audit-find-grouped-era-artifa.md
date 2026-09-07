---
# qou-4383
title: 'Ordering fingerprint audit: find grouped-era artifacts by VALUE, not by symptom'
status: in-progress
type: task
priority: normal
created_at: 2026-09-07T04:29:13Z
updated_at: 2026-09-07T04:33:18Z
---

## The tool

`computations/audits/intra_ordering_value_fingerprint_audit.py` — scans every
committed witness for grouped-era |tr_M| values, matched to **15 significant
digits** against fingerprints computed **live** from `atom_braid_word_3A` under
both orderings at both documented pins (never transcribed, so a re-pin moves
them rather than silently invalidating the scan).

Unlike the three sweeps that missed `compute_tau_M_nucleon_H3`, this keys on the
**answer**, not on a symptom. A 15-digit match to `1.14575969245730087` *is*
that number — the corpus's own coincidence floor puts 9–11 figures at 2.7 %, so
fifteen is not a near miss. That makes the count of *witnesses carrying grouped
values* exact, in a way a symptom count never is.

## Measured — 3548 witnesses scanned

| | count |
|---|---:|
| carry a **grouped**-era value | **89** |
| carry a **borromean** (canonical) value | 15 |
| of the 89: `qou-mass/` duplicates | 6 |
| of the 89: `computations/` originals | 83 |

Age of the 83 originals: **59** from 2026-08 (pre-ruling, expected stale),
**21** from 2026-09, 3 undated.

### The sharp set — 10 computed AFTER the 2026-09-05 ruling

    2026-09-05  derivation-chain-audit                      derivation_chain_validator.py
    2026-09-05  two-row-vs-higher-row-binding-split         two_row_vs_higher_row_binding_split.py
    2026-09-05  the_character_closure_block_..._convention_c_probe
    2026-09-06  atomic-mass-via-rho-k                       atomic_mass_via_rho_k.py
    2026-09-06  qbeta-habiro-pochhammer-convention          (producer field absent)
    2026-09-06  habiro/habiro-exact-qbeta                   habiro_exact_qbeta.py
    2026-09-06  qbeta-bond-factors-derived                  qbeta_bond_factors_derived_probe.py
    2026-09-06  qbeta-mixed-chain-closed-form               qbeta_mixed_chain_closed_form_probe.py
    2026-09-06  atomic-tr-m-helium4                         atomic_tr_m_helium4.py
    2026-09-06  gap-a4-L1-light-series-probe-perknot-rerun

These ran *under* the ruling and still emitted grouped values, so they are live
source behaviour, not merely stale artifacts.

**One is already accounted for.** `atomic-tr-m-helium4` is mine: arm (A), the
disjoint-product route, is deliberately retained and labelled non-canonical
(`qou-hft3`), and it reads the grouped proton leg. Expected, not a finding.

**One is informative.** `gap-a4-L1-light-series-probe-perknot-rerun` was in the
`qou-y2o7` sweep and classified `same` — so it does *not* take its baselines
from `compute_tau_M_nucleon_H3` and reaches grouped values some other way. That
is a second, independent route into the grouped frame, and the reason the
value-keyed scan is worth having.

The other eight want per-site reading. **Not swept.**

## The sharpest actionable finding: `qou-mass/` has forked

All six `qou-mass/src/qou_mass/` hits have a `computations/` twin, and at least
one pair has demonstrably diverged:

    computations/atomic-tr-m-mpfr-50dps.witness.json
        2026-09-06   0.62932842249…  0.47513351767…  0.15196834395…   BORROMEAN
    qou-mass/src/qou_mass/atomic-tr-m-mpfr-50dps.witness.json
        2026-08-29   1.14575978231…  0.98774375682…  0.57517232973…   GROUPED

This is the **second** instance of this defect class — the habiro pair forked
the same way and was synced under `qou-y2o7`. And these are not inert copies:
`qou_mass/_internal/canonical_trm_reference.py` reads
`atomic-tr-m-mpfr-50dps.witness.json`, and `chi_monotone_transfer.py`
references `chi-helium-3-h9-at-q0-50dps.witness.json`. So the `qou_mass`
package is computing against grouped-era references while `computations/` has
moved.

**No producer writes the `qou-mass` copies**, which is exactly why no
symptom-keyed sweep could ever have found them: there is nothing to raise, and
nothing to name `atom_braid_word_3A`.

Not synced here. Whether `qou-mass` is a vendored package with its own cadence
or a mirror that must track `computations/` is a packaging question, and
overwriting six live inputs on a guess is the kind of sweep this arc has
avoided. It needs an owner call — but it is a small, bounded one.

## What a hit does and does not mean

A hit says the **witness payload** is grouped-era. It does not say the producer
is broken: it may be fixed while the artifact was never regenerated (re-run to
tell them apart), or the site may be deliberately historical — three are, and
pass `intra_order="grouped"` on purpose. A non-hit is not a clean bill either: a
witness recording only derived quantities carries no |tr_M| to match.

---

## 2026-09-07 — swept, with the stale-vs-live discriminator applied

Re-ran the audit: **89 → 83 witness files**, 84 → 81 candidates.

### The `qou-mass` fork is closed, and the packaging question is answered

The bean's sharpest finding has resolved under it. `atomic-tr-m-mpfr-50dps` and
`chi-helium-3-h9-at-q0-50dps` are now **identical** across
`qou-mass/src/qou_mass/` and `computations/`, both dated 2026-09-06, both
carrying the same values. A sibling closed it.

The packaging question — *"vendored package with its own cadence, or a mirror
that must track `computations/`?"* — is answerable from evidence rather than an
owner guess, and I measured it rather than leaving it open:

- `docs/audits/2026-05-19-qou-mass-deprecation-audit.md` already names
  `computations/` **"Authoritative originals"** and the `_internal/` tree
  "entirely redundant with computations/".
- That audit is from May and the package has since gone `0.1.0a1` → `1.0.0`, so
  I re-measured today: of the 43 vendored modules that are no longer
  byte-identical, **42 differ only by the folio `_path_bridge` shim** (a
  path-fixup line meaningless inside the package). The sole real difference is
  `__init__.py`, which is package boilerplate.

So it is a mirror, maintained to the line, and `computations/` is authoritative.
The three remaining `qou-mass` hits are **not forks**: each has the *same*
`computedAt` as its twin (2026-08-19 / 08-29 / 08-30), i.e. both sides are
pre-ruling stale. They belong to the "59 from 2026-08, expected stale" bucket,
not to an owner call.

### The eight post-ruling sites, swept

Applied the discriminator the bean named and did not run — *re-run the producer,
re-scan, diff the hit list* — to seven of the eight:

| site | verdict |
|---|---|
| `habiro-exact-qbeta` | **stale artifact** — regenerated, dropped out |
| `two-row-vs-higher-row-binding-split` | **stale artifact** — regenerated, dropped out |
| `the_character_closure_..._convention_c_probe` | **deliberate** — its subject *is* the convention-C table `prop:q-hecke-seminormal-character-closure` publishes; added to the audit's `DELIBERATE` set |
| `derivation-chain-audit` | **live** — still emits grouped after a clean re-run |
| `atomic-mass-via-rho-k` | **live** |
| `qbeta-bond-factors-derived` | **live** |
| `qbeta-mixed-chain-closed-form` | **live** |
| `qbeta-habiro-pochhammer-convention` | not re-run — witness carries no producer field |

### Why the stale ones were stuck: they crashed *after* computing

Three of the seven died on the **last line of `main()`** with

    ModuleNotFoundError: No module named 'qou_substrate'

in the provenance-stamp block. Everything was computed; nothing was written. So
their witnesses were **unregenerable**, which is why they still carried
grouped-era values months after the ruling — not because anyone chose to keep
them.

`computations/_path_bridge` already puts `qou_substrate`
(`tools/qou-substrate/python`) within reach; these three simply never imported
it. Fixed in all three. `two_row_vs_higher_row_binding_split` now exits 0; the
two `qbeta` probes now run to completion and write their witnesses, exiting 1 on
their own honest assertion failures (a closed form that does not reproduce every
atom; two constants extracted rather than derived) — substantive open questions,
not crashes.

**This is the general lesson for the remaining 81.** A stale witness is not
evidence that anyone intended a grouped value; it can simply mean the producer
cannot write. Re-running is cheap and separates the two, and until it is done a
hit count is an upper bound on the real finding count.

### Remaining

- 4 confirmed-live grouped emitters need per-site reading (why do they reach the
  grouped frame?).
- 81 candidates un-swept; the 59 from 2026-08 are pre-ruling and expected stale,
  so re-running is the first move there too, not reading.
