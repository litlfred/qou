---
# qou-q0inv
title: q0_consistency_audit labels the LIVE canonical q0 as "stale" — and contradicts itself
status: todo
type: task
priority: normal
created_at: 2026-08-23T17:25:00Z
updated_at: 2026-09-08T08:20:29Z
---

`computations/audits/q0_consistency_audit.py` scans `computations/**/*.py` and
flags scripts that hardcode what it calls the "stale" q₀. Its committed witness
carries three fields that cannot all be true at once:

```
canonical_q0_source : "q_parameter.q_at() / Q_50_DIGIT_STR (proton pin, habiro-refined)"
stale_pre_habiro_q0 : "1.10997858275138080759…"
canonical_proton_q0 : "1.10997859555733471989…"
```

Measured live:

```
q_parameter.Q          = 1.1099785827513808
q_parameter.Q_50_DIGIT = 1.1099785827513808075916690956107688798744991218736
```

**`Q_50_DIGIT_STR` IS the value the witness labels `stale_pre_habiro_q0`.** The
audit names that constant as its canonical source and, in the same payload,
calls its value stale. The value it calls `canonical_proton_q0` is the one
AGENTS.md calls the **muon / ideal-CAL-2** pin.

The docstring says the same thing (lines 6–11): *"Canonical q₀ is the
proton-anchored, habiro-refined value C = 1.10997859555733471… (`q_parameter.Q`)"*
— `q_parameter.Q` is not that value.

## Why this matters more than a comment typo

This is a **live tree-scanning audit**. If its labels are inverted, it is
telling every agent who runs it to migrate *away* from the pin AGENTS.md makes
canonical for all new compute (owner directive 2026-08-07).

## What I did NOT do, and why

I did not flip the labels. Doing so changes what the audit flags across the
whole tree — a convention migration, which AGENTS.md scopes as a tracked sweep
needing sign-off, not a drive-by inside a drain PR. Same reason `qou-akdup` was
beaned rather than fixed.

## A possible innocent reading, to check before flipping

Within `computations/`, the **muon** pin was historically called "canonical"
(the q0-value-drift audit still buckets 607 muon-pinned fields as `canonical`).
This audit may be using that older sense while *also* saying "proton pin" — in
which case the fix is to disambiguate the words, not swap the numbers. Either
way the current payload is self-contradictory.

## Also: the same root/subdir duplication as `qou-akdup`

Two witnesses, two paths, different payloads:

- `computations/audits/q0-consistency-audit.witness.json` — has all three fields
- `computations/q0-consistency-audit.witness.json` — has `canonical_q0_source`
  (without "habiro-refined") and **neither** of the two value fields

## Suggested disposition

1. Decide whether the numbers or the words are wrong.
2. Re-run and re-emit; deprecate the superseded root copy.
3. Re-check what the audit has been flagging in the meantime — anything it
   "migrated" may have been moved off the canonical pin.

Found while draining tier C (bean `dgpc`), PR #5289.

---

## 2026-08-23 — measured. The arithmetic is RIGHT; the naming and the conclusion are wrong.

I said "the labels are inverted." That was too blunt, and the correction matters
because it changes the fix.

### The audit's empirical claim checks out

It justifies itself with *"only C reproduces m_p/m_e to 10 sig-figs."* Tested at
50 dps via `m_μ/m_e = Vol(4₁)/ℏ_q²`:

| | q₀ | `m_μ/m_e` |
|---|---|---|
| **M** (audit calls this canonical) | 1.10997859555733471… | **206.768282989** |
| **A** = `q_parameter.Q` (audit calls this stale) | 1.10997858275138080… | 206.768326371 |
| CODATA | | 206.7682827 |

M matches to ~10 sig figs; A misses in the 8th digit. **The arithmetic is
correct.** That is not the defect.

### The defect is that M is the MUON pin, not "the proton-anchored value"

M is exactly the value obtained by inverting `m_μ/m_e = Vol(4₁)/ℏ_q²` — it
reproduces the muon ratio *because it is defined by it*. The audit calls it
*"the proton-anchored, habiro-refined value (`q_parameter.Q`)"*, and
`q_parameter.Q` is **A**, not M.

So A's 8th-digit miss on `m_μ/m_e` is not staleness. It is the **μ–p substrate
tension** — the framework's own documented 9.5σ prediction gap (AGENTS.md,
§q₀ anchor convention). The audit reads a predicted tension as a bug.

### Why this is now urgent rather than cosmetic

Run on current main: **251 hits, 186 "production-hardcode"**. The flagged sites
include the canonical constant's **own regression tests**:

```
tools/qou-substrate/tests/test_codata_table.py:112
    assert repr(constants.Q) == "1.1099785827513808"
tools/qou-substrate/tests/test_vol_4_1_exact.py:48
    assert C.Q == 1.1099785827513808
tools/qou-substrate/tests/test_q0_anchor.py:248,318
    b.add_data("q0", "1.1099785827513808075916690956107688798744991218736")
```

Acting on those flags means editing the tests that pin `q_parameter.Q` to its
correct value — i.e. changing them to assert the muon value. The audit is
telling agents to migrate 186 production sites **off** the pin the 2026-08-07
owner directive makes canonical for all new compute.

### So the fix is naming + conclusion, not the numbers

1. Rename: M is the **ideal-CAL-2 / muon** pin, not "proton-anchored".
2. Reverse the verdict: hardcoding **A** is *correct* under the owner directive.
   What deserves flagging is hardcoding **either** value instead of importing
   `q_parameter` — a different and much smaller finding.
3. Re-check what it has flagged historically; anything "migrated" on its advice
   may have been moved off the canonical pin.

Still not applied here — this is a policy inversion in a tree-wide audit and
wants owner sign-off, not a drive-by. But the decision no longer needs guessing:
the numbers are right, the words and the conclusion are not.

---

## Addendum — the glob-hazard survey, and a number I withdrew

Having found four instances of "audit tool's repo-wide glob picks up files it
should not", I surveyed the audit layer for the same class. **Two corrections
to my own framing came out of it, and the second reverses the emphasis.**

### 1. I withdrew a "55 exposed tools" figure

A regex heuristic (`parents[\d]|parent.parent`) counted 61 globs as
"repo-rooted", of which 55 lacked a `.claude` exclusion. That number is
**unsound and is not claimed**: from `computations/audits/x.py`,
`parent.parent` resolves to `computations/`, **not** the repo root. The
heuristic conflates the two, which is precisely the distinction that decides
whether a glob can see `.claude/` at all. Publishing it would have been the
over-fire class this bean is otherwise about.

### 2. The two hazards are not equally live — and the one I emphasised is the weaker

| | status | scope |
|---|---|---|
| `.claude/worktrees/` | **ABSENT in a fresh container** | only bites a session that spawned sub-agent worktrees |
| `computations/_deprecated/` | **PRESENT, 893 entries** | every checkout, always |

All four instances I found were in a container carrying five stale sub-agent
worktrees. A fresh clone has none — so the `.claude` exclusion is **defensive
and conditional**, not a standing defect in 55 tools.

`_deprecated/` is the opposite: 893 retired copies sitting in-tree in every
checkout, reachable by any repo-wide name-match glob. From the survey,
**roughly 9 of ~32 audit tools with globs carry no `_deprecated` exclusion** —
including `ab_methodology_metrics`, `content_block_label_audit`,
`field_typeclass_audit`, `lean_ref_resolution_audit`,
`q0_declared_vs_recorded_sweep`, `q0_producer_pin_classifier`,
`tnjb_stale_stamp_migrate`.

That is the always-live exposure, and it is the one worth draining. It is also
the exact shape of the `resolve()` bug fixed in #5289: a live producer with a
`_deprecated` twin resolved to `None` because a uniqueness test counted both.

**Not claimed:** that those ~9 are currently producing wrong answers. Whether a
missing exclusion *bites* depends on the glob's root and on whether a name
collides with a retired copy — that needs per-tool measurement, which this
addendum does not do.

---

## Drain result — 2 resolvers fixed, 3 misresolutions measured

Followed the addendum's own recommendation. The `_deprecated` surface is **37
collisions**, not 890 files; of the 8 colliding `.py`, `__init__.py` is a
package marker, leaving **7 substantive**.

**Enumeration vs resolution.** Six unguarded tools only `rglob("*.ext")` —
retired files show up as extra findings, a mild problem. **Two** do bare-name
resolution unguarded, which can return the *wrong file*:

- `audits/q0_producer_pin_classifier.py:168` — `REPO.rglob(script_name)`
- `audits/tnjb_stale_stamp_migrate.py:160` — `REPO.rglob(sp.name)`

Both sort `(computations-first, fewest parts)` and take `hits[0]` — which
**ties** when the live copy is as deeply nested as the retired one.

**Replaying that exact tie-break: 3 of 7 pick `_deprecated/`** —
`path_b_habiro_mass_probe`, `rho_k_markov_multiplicativity_probe`,
`term5_aK_audit`. The other four are correct *only* because their live copy is
one level shallower; neither tool intends that.

`rho_k_markov_multiplicativity_probe.py` is the same file that broke
`witness_producer_executes_audit.resolve()` in #5289 — **third tool, same
collision**, because the fix keeps being applied per-tool rather than centrally.

Fixed both. Verified all three now resolve live.

**Not claimed:** that the misresolutions produced wrong committed output — that
needs a per-tool re-run and diff.

### Worth doing centrally

Three tools have now needed the same one-line guard. A shared
`resolve_producer(name)` helper — excluding `_deprecated`, `.claude`, `.git`,
`node_modules` — would end the recurrence. Not attempted here.


---

## 2026-09-08 — NOT closeable: the TITLE defect is live on `main`. The resolver sub-thread is fully fixed; the headline is not.

Read for the `qou-bstl` queue. The tool flagged this on `338a2acdc36`,
*"drain result — 2 resolvers fixed, 3 misresolutions measured"* — cause 1, and
the commit's own subject scopes itself to the resolvers, not the title.

### The title claim is CONFIRMED, live, today

`computations/audits/q0_consistency_audit.py` on `main`, run unmodified:

```
  [HARDCODE] computations/y_lambda_su_n.py:271  (old-q0)
             _Q = "1.1099785827513808075916690956107688798744991218736"
  [HARDCODE] tools/qou-substrate/tests/test_q0_anchor.py:251  (old-q0)
             b.add_data("q0", "1.1099785827513808075916690956107688798744991218736")
  [HARDCODE] tools/qou-substrate/tests/test_codata_table.py:112  (old-q0)
             assert repr(constants.Q) == "1.1099785827513808"

  production-hardcode    264
  TOTAL hits: 414  | production-hardcode: 264
```

`1.1099785827513808…` is **the live canonical proton pin**. Verified two ways
rather than assumed:

- `qou_substrate.constants.Q` → `1.1099785827513808`, and
  `Q_50_DIGIT_STR` → `1.1099785827513808075916690956107688798744991218736`.
- AGENTS.md §"q₀ anchor convention" names it verbatim as the experimental pin:
  *"proton, `m_p/m_e`, `q₀ ≈ 1.1099785827513808`, i.e. `q_parameter.Q`"*.

So the audit labels the canonical value `old-q0` — and the sharpest instance is
that it flags **`test_q0_anchor.py` and `test_codata_table.py`**, the tests whose
whole job is to pin that value, as hardcoding a stale one. The tests are right;
the classifier is inverted. 264 of 414 hits carry the label.

### The resolver sub-thread IS fully fixed — including the recurrence this bean predicted

The bean's closing line: *"Three tools have now needed the same one-line guard. A
shared `resolve_producer(name)` helper … would end the recurrence. Not attempted
here."*

Measured today, and the news is better than the bean feared:

| site | guard | mechanism |
|---|---|---|
| `q0_producer_pin_classifier.py:444` | ✅ | inline `_deprecated` / `.git` / `.claude` exclusion, with a comment citing the 3-of-7 measurement |
| `tnjb_stale_stamp_migrate.py:164` | ✅ | same, cross-referencing the classifier |
| `scripts/migrate_bare_producer_provenance.py:136` | ✅ | inline exclusion **plus** refuses on ambiguity (`len(cands) == 1`) |
| `audits/witness_producer_resolution_audit.py:189` | ✅ | filters `_deprecated`, and *reports* `PRODUCER_DEPRECATED_ONLY` as its own verdict rather than resolving silently |
| `scripts/regen-witnesses-mpmath141.py:95` | ✅ | exclusion at **index build time** (`_py_index`, line 87) |

**Live-tested** on the three names this bean measured as misresolving —
`path_b_habiro_mass_probe`, `rho_k_markov_multiplicativity_probe`,
`term5_aK_audit` — through the one resolver whose own body has no filter: all
three return the **live** copy.

So the *defect* has not recurred. What has recurred is the **duplication**: there
are now five independent implementations, correct by three different mechanisms,
and still no shared helper. That is the bean's actual open item, and it is a
maintainability item rather than a live bug.

### 🛑 Two wrong conclusions of mine on the way here, both caught by insisting on a live test

Recorded because the second is a reusable trap:

1. I ran an `awk`-range extraction over the three `resolve_producer` bodies and
   got **`guarded: 0`** for all three. The extraction was broken — it printed no
   `rglob` lines either, which is what made the zero suspect. **A zero from a
   detector written seconds earlier is not evidence.**
2. Reading `regen-witnesses-mpmath141.py::resolve_producer` directly, I found no
   `_deprecated` filter and was about to report it as an unguarded *regeneration*
   script — higher blast radius than a classifier. **Wrong: the guard is in
   `_py_index()`, one call up**, which excludes `_deprecated`, `.lake`,
   `/_internal/` and `/.git/` when building the basename map, so the resolver
   never sees a retired candidate.

   **For a resolver, read the index it consults, not only the function.** A
   filter applied at index-build time is invisible in the resolver's body and is
   strictly better engineering than the inline form — the correct implementation
   is the one that looks unguarded.

### Verdict

Stays `todo`, on the title. The next honest step is the classifier's own
old-vs-current q₀ table, not the resolvers: whatever list it treats as "old"
contains the canonical value.


---

## 2026-09-08 — ROOT CAUSE: the audit's docstring asserts a premise the corpus RETIRED. It is not a pattern typo; the two values are exactly backwards.

Following the title defect to its source. `computations/audits/q0_consistency_audit.py`
lines 7-11, verbatim:

> *"Canonical q₀ is the proton-anchored, habiro-refined value
> **C = 1.10997859555733471…** (`q_parameter.Q`). The stale value is the
> pre-habiro proton solution **A = 1.10997858275138…**, differing from C at the
> 8th sig-fig (~1.2e-8). Scripts that hardcoded A — instead of importing the
> canonical q₀ from `q_parameter` — silently keep computing at the stale
> constant."*

and line 70:

```python
OLD_Q0_PATTERNS = [re.compile(r"10997858275"), re.compile(r"(?<!\d)858275(?!\d)")]
```

**Both assignments are inverted against the corpus today**, checked three ways:

| the audit calls it | value | what the corpus says |
|---|---|---|
| **"Canonical q₀ … `q_parameter.Q`"** | `1.10997859555733471…` | **RETIRED.** AGENTS.md:2649 — *"**A** former frozen pin (retired)"*; :3155 — *"the **RETIRED** pin"* |
| **"the stale value … pre-habiro"** | `1.10997858275138…` | **THE LIVE DEFAULT.** AGENTS.md:3120 — *"q₀ ≈ 1.1099785827513808 — **this is the DEFAULT for all new compute and all production code**"*; and `qou_substrate.constants.Q` returns exactly `1.1099785827513808` |

So the pattern `10997858275` matches the canonical pin's own digit string, and
the audit flags every correct use of it — **264 production-hardcode hits of
414**, including `tools/qou-substrate/tests/test_q0_anchor.py` and
`test_codata_table.py`, the tests whose job is to pin that value.

### It is CROSS-LAYER, not merely stale

The audit's "canonical" is a **muon**-layer value; its "stale" is the **proton**
pin. So it does not just quote an out-of-date number — it demands that compute
use a muon value where the 2026-08-07 owner directive says proton is the default
for all production code. Two directives passed it by: the proton default
(2026-08-07) and the frozen-pin retirement (ruled 2026-08-22, implemented
2026-08-28). Its own citation is
`docs/audits/2026-06-21-q0-clusterA-migration-plan.md` — June, before both.

### 🛑 I did NOT fix this, deliberately

Correcting the docstring alone would leave the file self-inconsistent the other
way; correcting the pattern requires deciding **what "stale q₀" should mean
now**, and that is a judgement the corpus does not settle. AGENTS.md's
ask-first override does not exempt it: it neither increases precision nor is
fixed by a corpus artifact I can point a reviewer at. The blast radius is
recorded above so the decision can be made without re-measuring.

**What happens if nobody acts:** the audit keeps reporting 264 false
production-hardcodes and stays unusable as the `--strict` CI gate its own
docstring proposes (*"Run with `--strict` to exit non-zero when any
production-hardcode remains (CI gate once the backlog is cleared)"*). The
backlog can never clear, because the backlog is the canonical value.

**My judgement, marked as judgement:** retire the `old-q0` half of this audit
rather than re-point it. The value it was built to chase (pre-habiro A) is three
directives out of date, and the two live q₀ questions — anchor consistency and
the muon/proton flip — already have dedicated, current instruments in
`q0_anchor_consistency_audit.py` and `muon_pin_stored_vs_live_gate.py`. The
`stale-trM` half is a separate detector and is untouched by this.
