---
# qou-ivhc
title: q0_consistency_audit is POLARITY-INVERTED after the proton ruling — it classifies the canonical pin as a stale-q0 bug, and has a --strict CI-gate mode
status: in-progress
type: task
priority: normal
created_at: 2026-08-22T15:27:20Z
updated_at: 2026-08-22T19:28:25Z
---


Found while tracing `qou-cds3`'s finding that 22 witnesses hold a muon value in a
`proton`-named field. The worst of those was
`computations/audits/q0-consistency-audit.witness.json`; this bean is its cause.

## The inversion

`computations/audits/q0_consistency_audit.py` docstring, verbatim:

> Canonical q₀ is the proton-anchored, habiro-refined value
> **C = 1.10997859555733471…** (`q_parameter.Q`). The stale value is the
> pre-habiro proton solution **A = 1.10997858275138…**, differing from C at the
> 8th sig-fig (~1.2e-8). Scripts that hardcoded A — instead of importing the
> canonical q₀ from `q_parameter` — silently keep computing at the stale
> constant.

Measured today:

```
q_parameter.Q_MP  = 1.10997858275138080759166909561076
Q_50_DIGIT_STR    = 1.10997858275138080759166909561076
```

So **`A` — the value this audit calls stale and flags as a bug — IS
`q_parameter.Q` today.** And `C`, which it calls canonical and attributes to
`q_parameter.Q`, is the hand-typed muon constant (`qou-khac`), itself measured
**8.54e-11 stale** against what `q_muon_at()` now derives.

The docstring's parenthetical *"(`q_parameter.Q`)"* is therefore false on its own
terms: the symbol it names holds the other value.

## Why this is not cosmetic

Three multipliers, in increasing order of consequence:

1. **It classifies correct code as a defect.** A hit on the canonical pin
   assigned to a live constant is classified `production-hardcode — real bug`.
   Every script that correctly hardcodes or reproduces `1.10997858275138…` is
   counted as a migration failure.

2. **It is built to become a CI gate.** From the same docstring: *"Run with
   `--strict` to exit non-zero when any production-hardcode remains (CI gate once
   the backlog is cleared)."* Enabling that gate today would **fail the build for
   using the canonical value**, and the backlog can never clear, because the
   thing it counts is now the correct thing to do.

3. **Its witness asserts the wrong canonical pin, with no way to notice.**
   `q0-consistency-audit.witness.json` carries
   `canonical_proton_q0 = 1.10997859555733471…` — a *muon* value in a field named
   `canonical_proton_q0` — and has **no `computedAt`, no `scriptFile`, no
   `scriptHash`, no `engine`**. Nothing in the provenance machinery can flag it as
   stale, because it records no provenance at all. It is one of only two audits in
   the tree whose witness is written by `out.write_text(json.dumps(...))` directly
   rather than through `WitnessBuilder`.

## Why it went unnoticed — and it is a taxonomy row

The audit was **correct when written**. Before 2026-05-28 the muon-anchored value
*was* the pin (`q_muon_at`'s own docstring: *"This was the pin until 2026-05-28;
now superseded by `q_at()` (m_p anchor)"*), and the 2026-08-15 owner ruling made
the proton pin canonical. The audit's polarity was never revisited.

The general shape, worth adding to
`docs/audits/2026-08-15-detector-blindness-taxonomy.md`: **a detector that encodes
which value is canonical becomes an anti-detector the moment the ruling moves.**
It does not go quiet and it does not fail — it keeps reporting confidently, with
the sign flipped, and its report reads exactly like a real backlog. Every other
row in that taxonomy is a detector that *misses* something; this is one that
*asserts the opposite*.

## Not run, deliberately

`main()` writes the witness unconditionally (`:182`, no dry-run flag), so running
it would regenerate the inverted artefact and refresh its timestamp. The static
evidence above is decisive without it. Whoever fixes this should invert the
polarity **before** the next run, or the run will overwrite the current witness
with an equally wrong one that merely looks fresher.

## What it needs

1. Swap `A` and `C` throughout — canonical is the proton pin, stale is the
   pre-ruling muon value — and re-derive the `tr_M` leaf literals it screens for,
   which are quoted at the old canonical and are presumably inverted too.
2. Read the canonical value from `q_parameter` **at runtime** instead of quoting a
   literal in the docstring and the scan table. The whole defect is that the audit
   hardcodes the thing it exists to stop others hardcoding.
3. Emit through `WitnessBuilder` so the witness carries `computedAt`/`scriptHash`
   and the staleness gates can see it.
4. Do **not** enable `--strict` in CI until 1–3 land.

Related: `qou-cds3` (the 22 mislabelled witnesses, of which this is one),
`qou-khac` (the muon constant this audit calls canonical is itself stale by
8.54e-11).

---

## Summary of Changes (2026-08-22) — FIXED

`computations/audits/q0_consistency_audit.py` inverted and re-run.

### What changed

1. **Polarity swapped.** `OLD_Q0_PATTERNS` now scans for the pre-ruling **muon**
   family (`10997859555`, covering both the hand-typed `…55733…` and the
   `…55418…` variant); it previously scanned for the proton pin.
   `STALE_TRM_PATTERNS` swapped to the muon-anchored tr_M leaves.
   **No number was recomputed** — both sets were already written down in this
   file's own comments (`…062286/…332971/…864715` vs `…0614425445/…2332299/…2864240`),
   so the swap introduces no new numeric claim.
2. **The canonical pin is now read at runtime** from `q_parameter.Q_50_DIGIT_STR`
   instead of being quoted. This is the point: the file already *named*
   `q_parameter` as the canonical source at `canonical_q0_source` and then
   hardcoded a different (muon) literal beside it. Quoting the pin is the defect
   the audit exists to catch, and the literal went stale exactly that way.
3. **Provenance added** — `computedAt`, `scriptFile`, `scriptHash`, `engine`. The
   witness previously had none of these, so no staleness gate could see it.
4. Docstring rewritten to record the inversion, its cause, and that
   `legit-muon-xcheck` now carries more load (every muon literal matches the
   stale pattern, so intentional cross-checks rely on that classifier).

### Verified

Re-run output:

```
canonical_proton_q0  = 1.1099785827513808075916690956107688798744991218736   (runtime)
computedAt           = 2026-08-22T19:30:16Z
scriptHash           = 1ea40576a700
total_hits           = 488
  production-hardcode  288
  legit-muon-xcheck    113
  stale-docstring       87
```

**Regression check — the whole point.** Hits firing on the canonical proton pin:
**0**. Eight hits *mention* it, and all eight are lines carrying **both** values,
where the match is on the muon pattern and the proton digits are incidental
context — e.g. `_EXPECTED_PREFIX = {"muon": "1.109978595557", "proton":
"1.109978582751"}` (classified `legit-muon-xcheck`, correctly) and
`q₀_proton = 1.10997858275138…  q₀_muon = 1.10997859555418…` (`stale-docstring`).

### The 288 are a real backlog, and it is the SOURCE-side twin of `qou-cds3`

Sample: `a4_interface_kl_subpath_closure.py:27` and
`a4_option_e_color_tube_closure.py:23` both open with
`Q0_STR = "1.10997859555733471989976322048…"` — the stale hand-typed muon
constant, assigned to a live constant. `qou-cds3` measured 424 **witnesses**
carrying hand-typed muon values; this is the same migration surface in **source**,
at 288 sites.

Sharpest single instance: `tools/qou-substrate/tests/test_q0_anchor.py` **asserts**
`payload["q0Value"].startswith("1.109978595557")` — a test in the substrate
package that pins the stale muon value as the anchor and would fail if the
canonical pin were emitted.

### Note: the corpus already had a correct sibling audit

`computations/audits/q0_anchor_consistency_audit.py` carries
`_EXPECTED_PREFIX = {"muon": "1.109978595557", "proton": "1.109978582751"}` — the
right polarity. So two near-identically-named audits sat side by side, one correct
and one inverted, for a week. Worth a look at whether they should be one file;
not merged here, since that is a scoping decision rather than a defect fix.

### Still not done

`--strict` must stay **off in CI**. It now fails correctly rather than
incorrectly, but 288 real hits means enabling it gates the build on the whole
muon→proton source migration, which is `qou-cds3`'s unauthorised bulk sweep.
