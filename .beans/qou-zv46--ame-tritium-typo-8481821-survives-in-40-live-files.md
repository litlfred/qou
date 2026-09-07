---
# qou-zv46
title: AME tritium typo 8.481821 survives in 40 live files; 3He companion 7.718058 in 25
status: in-progress
type: task
priority: normal
created_at: 2026-09-06T03:41:22Z
updated_at: 2026-09-06T06:48:22Z
---

Not an inference — **already established prior art**. `computations/binding_canonical.py:610-623`
records that PR #1105 (2026-08-19) routed that file's targets through the
`AME_B_*_MEV_VALIDATION` accessors *"after finding the inline tritium value was
a typo (8.481821 for 8.481798)"*, and measured the residue it left behind:

```
6Li  31.994526  vs  31.9939872   (-538.8 eV)
7Li  39.244531  vs  39.2450807   (+549.7 eV)
7Be  37.600350  vs  37.6008409   (+490.9 eV)
```

That fix was applied to **one file**. The typo is still live everywhere else.

## Measured spread (vendored AME2020 via `codata_constants.ame_binding_mev`)

| literal | nuclide | AME2020 | offset | live files |
|---|---|---|---|---|
| `8.481821`  | ³H  | `8.4817962`  | **+24.8 eV** | 40 |
| `7.718058`  | ³He | `7.71804132` | **+16.7 eV** | 25 |

20 files carry both. Forms vary — bare float, `mp.mpf("…")`, `Decimal("…")`,
and a plain string in a table — so a single textual sweep will not catch them;
`8.481821` also appears inside prose/comments where it must stay (e.g. the
`binding_canonical.py` note above, and `w3_closeability_audit.py:311`'s printf).

Full site lists: `git grep -n '8\.481821' -- '*.py' | grep -v _deprecated` and
the same for `7\.718058`.

## Why this is not cosmetic

Both values are **denominators or numerators of published residuals**. The
T/³He pair is the standard mirror discriminator across this corpus, so a
per-atom offset does not cancel — it lands directly on the mirror mismatch these
probes exist to report. `deltalambda/*` alone carries the pair in 7 magnitude
probes as `B3H`/`B3He`.

## Scope notes

- **Do not touch `computations/_deprecated/`** (15 more files). Deprecated,
  and its own dominant lineage is `2.22456612` for D, off by 0.1 eV — noise.
- Most other near-misses found by the same scan are honest 6-dp roundings
  (±20 eV or less) of the right value, not stale numbers. Only the two above
  show the copy-paste signature of a single wrong source.
- Main's `drain(qou-psjm)` (372 AME/CODATA literals across 178 files,
  2026-09-05) did **not** reach these.

## Already done (this session, branch claude/anchor-followups-2026-08-08)

3 sites, both files verified by AST:
- `computations/phase5/phase3_triton_binding_convention_b.py` — `3He`
  `mp.mpf("7.71810")` (+58.7 eV) → `AME_B_HE3_MEV_VALIDATION`
- `computations/probes/rho_binding_constancy_probe.py` — `T` and `3He` bare
  float64 literals → `AME_B_TRITIUM_MEV_VALIDATION` / `AME_B_HE3_MEV_VALIDATION`

Both witnesses are queued to regenerate.

**The remaining ~62 live sites are UNCLAIMED — nobody is working them.**

---

## Update 2026-09-06 — 55 sites routed across 30 files

Claimed and worked on `claude/anchor-followups-2026-08-08`.

**Method.** AST-guided, not textual: only `ast.Constant` nodes were candidates,
so prose that legitimately QUOTES the typo is untouched — `binding_canonical.py`'s
PR #1105 note and this bean's own tables survive verbatim, which a `sed` sweep
would have corrupted.

**Type preserved at every site.** A bare float became `float(AME_B_*)`; an
`mp.mpf("...")` literal became the named mpf directly. Routing the SOURCE of a
value and changing its TYPE are two different changes and only the first
belongs to this bean.

Restricted to the 30 files that **already** imported `codata_constants`, so the
import risk is zero — the module is already resolvable from wherever each file
sets up `sys.path`; only a NAME was added to an existing import.

| literal | nuclide | offset | sites routed |
|---|---|---|---|
| `8.481821` | ³H | +24.8 eV | 25 |
| `7.718058` | ³He | +16.7 eV | 26 |
| `2.224573` | ²H | +6.8 eV | 4 |

The deuteron literal is a **third** member of the family, found while wrapping
a long line: `2.224573` against AME `2.2245662`. Only the 4 sites where it sat
in the *same tuple* as a T/³He value just fixed were done — leaving D wrong
beside a corrected T would be incoherent. The rest are listed below.

Also `w3_closeability_audit.py:313` printed the label `vs B_AME 8.481821` next
to a value that is now correct; the label now interpolates `B_AME['3H']`
instead of hardcoding it. Same hardcode-vs-derive defect as bean qou-24i9.

Verified: 0 dangling names over the 30 changed files, 0 literal constants left
in them, all four `AME_B_*_MEV_VALIDATION` names exist and are `mpf`,
suites 64 + 145 green.

### STILL OPEN — 23 sites, unclaimed

**11 files need a NEW `codata_constants` import** (and a `sys.path` insert),
which is why they were held back from the mechanical pass — each needs its own
path setup read:

`binding_hbarq_rung_forward_test` · `binding_mass_rung_derivation_probe` ·
`binding_n3_forcing_probe` · `binding_row_length_stratification` ·
`binding_volume_defect_route_refuted` · `deltalambda/mu3_target_robustness_audit_probe` ·
`probes/binding_closed_form_C_vs_D_probe` · `probes/binding_production_route_C_vs_D_probe` ·
`probes/binding_sum_C_vs_D_per_isotope_probe` · `two_row_vs_higher_row_binding_split` ·
`qou-mass/.../canonical_tower`

**14 of the 23 are BARE STRINGS**, e.g. `("3H", 3, "8.481821")` or
`Decimal("8.481821")`. These are deliberately not mechanically rewritten: a
string literal is consumed differently at each site (parsed later, used as a
dict key, formatted for display), so each needs reading. `fmt(AME_B_*)` is the
likely form but is a per-site decision.

**8 deuteron sites** not adjacent to a fixed T/³He: `per_braid_tower:122`,
`probes/h6_deuteron_free_word_chi_lambda_probe:58`, and a uniform group of six
`qbeta/qbessel_*` files all computing `B_DEU_OVER_ME = mpf("2.224573") /
mpf("0.510999")`. That group is one edit repeated six times. (Its `0.510999`
for m_e is only 0.05 eV off CODATA — noise, not this family.)

### Regeneration debt

All 30 producers now emit different numbers, so their witnesses are stale by
construction. **Not regenerated here**: the `hadron_knot_table` run (bean
qou-uiut) holds the checkout, and this campaign does not run two producers
concurrently. Queued.

---

## Update 2026-09-06 (second pass) — all 23 remaining sites routed; 0 literals left

The tree now contains **zero** `8.481821` / `7.718058` / `2.224573` literal
constants outside `_deprecated/`, verified by AST over every tracked `.py`.

Handled by form, because a string is consumed differently at every site:

- **6 `qbeta/qbessel_*`** — `B_DEU_OVER_ME = mpf("2.224573") / mpf("0.510999")`
  → `AME_B_DEUTERON_MEV_VALIDATION / M_E_MEV`. **Both** operands were typed:
  the binding +6.8 eV, and m_e 0.1 ppm off CODATA. Small alone, but this is a
  RATIO used as a scale target, so both land in it. Measured shift: 4.3533803 →
  4.3533675 (3 ppm). Their claim is "within striking distance of ~4.35", so the
  conclusion is untouched — the number is simply now sourced.
- **9 whole AME tables** routed rather than just their tritium entry.
  `mass_rung`, `closed_form_C_vs_D` and friends carried 5–7 nuclides each and
  the neighbours were off too (⁴He +10.6 eV, ⁶Li −538.8 eV, ⁷Li +549.7 eV).
  Fixing only the typo would leave a half-corrected table — the same argument
  that pulled the deuteron in.
- **String tables** keep their string shape via a local
  `_B(Z, A) = mp.nstr(ame_binding_mev(Z, A), 12)`. Checked first that `nstr`
  at 12 digits reproduces AME's own quoted digits **exactly** for every
  nuclide used (²H…¹⁶O), so nothing is lost in the rendering.
- **2 Decimal-only modules** (`binding_row_length_stratification`,
  `two_row_vs_higher_row_binding_split`) keep all arithmetic in `Decimal` at
  prec 60; mpmath appears solely to read the registry. Their NO-FLOAT64 note is
  about the arithmetic, not about forbidding an import.
- **`qou-mass/.../canonical_tower.py`** — import scoped inside
  `if __name__ == "__main__"`, because `codata_constants` is a SIBLING module
  resolvable only under direct invocation there; a module-level import would
  have broken the package path for no gain.

### A regression I introduced and caught

The `_B` helper was first inserted after `import mpmath as mp`, which in 4
files sits *above* `import _path_bridge` — so `from codata_constants import`
ran before the path existed and those 4 producers failed to import at all.
Caught by actually importing every edited file under a write guard, not by
reading the diff. Helper moved below the bridge; all 4 import again.

Attribution checked rather than assumed: the same import harness was run
against HEAD in a clean `git worktree`, and the 4 remaining failures
(3 × `markov_weights_symbolic`, an artifact of `spec_from_file_location` not
reproducing direct invocation, and `mu3_target_robustness_audit_probe` which
WRITES at import) are **identical at HEAD** — pre-existing, not regressions.

Verified: 0 literals tree-wide, 0 dangling names, suites 64 + 145 green.

## Remaining — regeneration only

All source sites are done. What is left is the witness debt: ~50 producers now
emit different numbers. Blocked on the `hadron_knot_table` run (bean qou-uiut)
holding the checkout — this campaign does not run two producers at once.

---

## 2026-09-07 — regeneration run. 37 of 39, and three of my own bugs

The witness debt is cleared for every producer that can run: **37 of 39
producer→witness pairs regenerate clean, 31 witnesses changed, 0 still carrying
`8.481821` or `7.718058`, 11 now carrying the corrected `8.4817962`.**

Running them found three defects that AST verification could not, all mine
except the third:

**1. The import rewriter destroyed aliased imports.** It rebuilt each
`from codata_constants import (...)` from the AST using `a.asname or a.name`,
which for `M_E_MEV as m_e` yields the ALIAS and drops the `as` — emitting
`import m_e`, a name that does not exist. Four files:
`binding_ladder_catalog` (`m_e`), `borromean_binding_recompute` and
`borromean_per_lambda_fr_probe` (`M_E`), `catalan_binding` (`_M_E_MEV`,
`_M_N_MEV`, `_M_P_MEV`). Restored from git; 0 broken imports remain.

**2. `probe_9b` used the constants at MODULE level** while its codata import
sits inside `main()`, so the name was unbound at import time. Module-scope
import added.

**3. `mpf.__format__` — NOT mine.** mpmath **1.3.0 raises**
`TypeError: unsupported format string` on a `:.3f` spec that **1.4.x accepts**,
and this project pins `mpmath>=1.3,<1.5`. sympy had pulled 1.3.0 into this
container. The affected values (`AME_B_HE3/HE4_MEV_VALIDATION` in `ATOMS`
tables) were mpf **before** my edits — verified against `c3c2033d4a^`. I began
patching print sites one at a time; installing a pin-permitted **1.4.1** fixed
~9 producers at once. Two `float()`-at-the-print-site fixes were kept anyway,
since a producer should not depend on which permitted version is installed.

### The corpus's own gate stopped a bad commit

The first clean batch produced 31 witnesses of which **19 had a DEGRADED
`environment` block** — they had silently dropped `clarabel`, absent from this
container. `witness_base` warns exactly this: *"the environment block records
LESS than the witness on disk … install it and re-run rather than committing
the weaker record; the numbers can be identical while the provenance silently
degrades."* clarabel installed, batch re-run, **0 degraded**.

### Still failing — pre-existing, not this bean

`binding_ladder_catalog` and `binding_bring_enhancement_compare` both die with
`TypeError: Object of type mpf is not JSON serializable` on the witness write.
Reproduced at `c3c2033d4a^` (before any zv46 edit), so pre-existing. The mpf
reaching `json.dump` comes from `AME_B_*` entries that were already there. Not
fixed here; it wants the producer to serialise with `fmt`, which is a change to
how those two write witnesses rather than to what they read.

**Remaining on this bean: those two producers' witnesses.** Everything else is
regenerated and consistent.
