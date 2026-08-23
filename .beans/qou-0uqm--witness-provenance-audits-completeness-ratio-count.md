---
# qou-0uqm
title: witness_provenance_audit's completeness ratio counts 320 never-checked witnesses as complete — exempt and passed render identically
status: todo
type: task
created_at: 2026-08-22T21:14:23Z
updated_at: 2026-08-24T00:05:00Z
---


Split out of `qou-ivhc`, which root-caused how an audit witness carrying the
wrong canonical pin and **zero provenance fields** reported clean for a week.

## The defect

`computations/audits/witness_provenance_audit.py` returns exempt verdicts
**before examining any field**:

```python
def classify(path):
    if any(path.name.endswith(suf) for suf in AUDIT_SUFFIXES):
        return "PROV_AUDIT_EXEMPT", []
```

and then counts every exempt class in the numerator of the headline metric:

```python
completeness_ratio = (n_ok + n_audit + n_no_reader + n_ack) / n_total
```

So `missing_fields: []` means **"not checked"** and is byte-identical to
**"checked and complete"**, and a ratio named *completeness* cannot fall when
coverage falls. `q0-consistency-audit.witness.json` reported
`{"missing_fields": []}` on 2026-08-21 while carrying no `computedAt`,
`scriptFile`, `scriptHash` or `engine` at all.

The exemptions themselves are **correct** — audit/state-tracking witnesses
legitimately record other artefacts' stale values, and applying provenance and
pin rules to them would generate constant false positives. The defect is purely
in how exclusion is reported.

## Fixed (additive only — no verdict, assertion or exit code changed)

1. Each entry gains **`evaluated: true|false`**, so an exempt row is
   distinguishable from a passing one in the emitted JSON.
2. Three figures added beside the existing ratio, which is **kept unchanged** for
   continuity with prior runs:
   - `excluded_not_evaluated`
   - `completeness_ratio_evaluated` — of those actually checked
   - `evaluated_coverage` — what share of the corpus was checked at all
3. The summary now prints the split.

`--strict` gates on `n_missing > 0` and is untouched.

## Measured after the change

```
  total scanned          : 2714
  PROV_OK                : 2350
  PROV_AUDIT_EXEMPT      : 76
  PROV_EXEMPT_NO_READER  : 242
  PROV_EXEMPT_ACKNOWLEDGED: 2
  PROV_MISSING           : 44
  excluded (NOT evaluated): 320  = 76 audit + 242 no-reader + 2 acknowledged
  completeness ratio     : 0.984   (counts all exempt classes as complete)
  ├─ of those EVALUATED  : 0.982   (2350/2394)
  └─ corpus evaluated    : 0.882   (2394/2714) — the rest was never checked
```

**Worth stating plainly: this does not make the corpus look worse.** Provenance
quality among checked witnesses is genuinely good — 0.982, essentially the same
as the old headline. The number that was hidden is **coverage: 0.882**, i.e. 320
witnesses (11.8 %) that no provenance rule has ever been applied to. Those are
two different questions and the single ratio answered only the flattering one.

`PROV_EXEMPT_NO_READER` at **242** is the largest exempt class by far and is worth
its own look: "no reader" is a claim about the corpus that ages, and a witness
that gains a consumer does not lose the exemption automatically.

## Not done

The same shape exists in two sibling detectors and is recorded in `qou-ivhc`:

- `q0_anchor_consistency_audit.py` — `Q0_FLIP: 0` over 663 evaluated of ~2585,
  with 1922 `Q0_ANCHOR_MISSING` unevaluable and not surfaced in the headline.
- `q0_consistency_audit.py` / `witness_constant_staleness.py` — the same
  audit-suffix carve-out, granted by **filename** rather than by content.

Not touched here because the anchor audit's `Q0_FLIP` is a **CI-failing gate**;
adding coverage reporting there is safe by the same additive pattern used above,
but it should be done deliberately rather than folded into this change.

---

## The exempt class is itself INFLATED by a silent grep failure — and it fails OPEN

Swept the 242 `PROV_EXEMPT_NO_READER` witnesses asking "has the exemption aged?"
The answer is worse and more specific: **it was wrong at emission.**

### The mechanism, verified

`build_reference_index()` builds the "who cites this" index from two greps, each
wrapped so that failure is silent:

```python
    try:
        out = subprocess.run(
            ["grep", "-rhoE", pat, str(repo / "content")],
            capture_output=True, text=True, timeout=120,
        ).stdout
        paper = set(out.split())
    except Exception:   # noqa: BLE001
        pass            # ← a timeout leaves `paper` EMPTY, silently
```

and the rule is `has_reader() = name in paper or py_counts.get(name, 0) > 1`.

**If the `content/` grep fails, `paper` is empty, every witness looks uncited, and
the exempt class swells.** Because `PROV_EXEMPT_NO_READER` sits in the numerator
of `completeness_ratio`, that failure **raises the headline score**. A gate whose
index fails open, and reports a better number for having failed.

### Verified: the `content` branch contributed nothing to the committed report

Three witnesses picked from the exempt list and checked directly:

| witness | in `PROV_EXEMPT_NO_READER` | cited in `content/` today |
|---|---|---|
| `aomega-bps-sector-nondegeneracy` | **yes** | `mass-theory/aomega-fourone-dt-count.ts` |
| `canonical-mass-table-242ppb` | **yes** | `appendix-mass-binding-algorithms/mba-step09b-per-isotope-binding.ts` |
| `sigma-f-electron-shell-chain` | **yes** | `knots-particles-confinement/shell-closure-stability.ts` |

The audit's own `name in paper` test returns **True** for all three, so its own rule
would not have exempted them. Corroboration from the sweep: **all 44 surviving
`PROV_MISSING` entries have `py_occurrences > 1`; not one was retained as a gap by
the `content/` branch** — exactly the signature of `paper == set()`. Plausible
cause is the `timeout=120` on a 6.8 GB `content/` tree (6.5 GB of it untracked
`.lake` build output); that specific mechanism is **not proven** — a warm run here
took 8.3 s — so it is recorded as the likely cause, not a measured one.

### And the second half of the rule is inert

`py_counts > 1` contributes **nothing** to this class: the maximum py-occurrence
count across all 242 is **1** (62 have 0, 180 have 1). Every one of the 242
exemptions therefore rested solely on the `content/` grep that returned nothing.

### The rule is also blind by construction

`has_reader` cannot see a read whose path is built at runtime. The entire
`chi-*` cache family is consumed that way — e.g.
`bar_pairing_binding_observable.py:122` builds
`chi-{atom}-{kind}-h{n}-at-{q_tag}-50dps.witness.json` from an f-string, so no
literal filename appears anywhere. **12 of the 13 exempt `chi-*` witnesses have a
genuine runtime reader**; e.g. `canonical_tr_m_via_chi_cache.py:80,244` and
`delta_lambda_energy_scale_extensivity_probe.py:103`. It is also scoped to `.py`
under `computations/` only, so `.ts`/`.sh` readers elsewhere are invisible.

**Demonstrable genuine readers: 25 of 242 (10.3 %).** The naive "mentioned
anywhere" count is 227, but **79 % of those mention-sites are other audits' own
report JSON** — machine inventories, not readers. That distinction matters: it is
the difference between a 94 % error rate and a 10 % one, and only the second is
defensible.

### What this needs

1. **Fail loudly.** `check=True` on both greps, or record `paper_index_ok` in the
   witness so a failed index is visible rather than score-improving. This is the
   single highest-value change — it converts a fail-open gate into a fail-closed
   one.
2. **Cover dynamic reads**, or stop treating "no literal mention" as "no reader"
   for families known to be built by f-string.
3. **Exclude machine inventories** from any future "is it cited" measure.

My `evaluated_coverage` change above already surfaces the *symptom* — 320
witnesses excluded, 0.882 coverage — but not the cause. Not fixed here: (1) is a
behaviour change to a `--strict` gate and should be a deliberate call.

---

## FIXED 2026-08-23 — and the timeout is no longer a hypothesis

The bean recorded the `content/` grep timeout as *"the likely cause, not a
measured one"* (a warm run took 8.3 s). **It is now measured.** Running the audit
unchanged on this tree, with the health reporting added:

```
  reader index           : paper=0 name(s), py=2005 name(s)
  *** READER INDEX DID NOT BUILD ***
      paper_index: TimeoutExpired: Command '['grep', '-rhoE', …, '/workspace/qou/content']'
                   timed out after 120 seconds
```

`content/` is **6.8 GB**. The grep does not finish, `paper` comes back empty, and
every witness therefore looks reader-less. Before this change the run printed
**nothing at all** about it and reported a clean `completeness ratio 0.983`.

### Two changes

**1. The index reports its own health.** Both greps sat under
`except Exception: pass` and neither checked the return code — `grep` exits 0
with matches, 1 with none, ≥2 on error, and the code took `.stdout` regardless.
Now each records `*_ok` / `*_returncode` / `*_error`, the result goes into the
witness as `reader_index_health`, and a failed index prints an unmissable block
tying the failure to the exact count it inflates:

> *An empty index makes EVERY witness look reader-less, so the 242
> PROV_EXEMPT_NO_READER verdict(s) above are UNSUPPORTED — and they RAISE the
> completeness ratio, so this failure reads as an improvement.*

**2. The paper index uses `git grep`, so it actually builds.** Tracked files
only: **~2–5 s instead of >120 s**, and it is the *more correct* semantics —
`content/` is overwhelmingly untracked build output, and an untracked build
artifact is not the paper citing a witness. The original recursive grep is
retained as a fallback (`paper_index_fallback`) for use outside a git checkout.

### Measured effect — fixing a fail-open makes the number WORSE, which is right

| | index empty | index builds |
|---|---|---|
| paper index | 0 names | **588 names** |
| `PROV_EXEMPT_NO_READER` | 242 | **229** |
| `PROV_MISSING` | 45 | **57** |
| `completeness_ratio` | 0.9838 | **0.9790** |

**13 witnesses were being exempted as "nothing reads this" while the paper cites
them**, and 12 of those become `PROV_MISSING`. That is the whole point: the
failure was not neutral, it was scoring in its own favour, and the corrected
number is lower. Any completeness figure quoted from this audit before today was
measured against an empty index.

### Scope — deliberately NOT changed

- **`--strict` semantics.** Unchanged: still exits 1 on `PROV_MISSING` only.
  Note this file is **not** gate-wired. `scripts/precision-gates.sh:267` wires a
  *different* script with a near-identical name — `computations/witness_provenance_audit.py`,
  which asks "does this `scriptFile` actually write this witness?" — not
  `computations/audits/witness_provenance_audit.py` (this I14 completeness
  audit). Worth stating, because the names invite exactly that confusion.
- Bean items **(2) dynamic reads** and **(3) exclude machine inventories** are
  untouched. `has_reader` still cannot see an f-string-built path, so the
  `chi-*` family is still exempted for a reason that is false for 12 of 13 of
  them. That is a semantics change, not a fail-open fix.

### Checked and CLEARED — the gate-wired sibling is not an instance

I went looking for the same defect in the blocking gate
(`computations/witness_provenance_audit.py`) and it is **not there**. It has a
first-class `UNCONFIRMED` verdict — *"asserted as unchecked", "deliberately not
folded into either neighbour"* — and its headline names its own denominator:
`"N witnesses carry a scriptFile claim"`. Its three `continue` paths exclude 292
of 2719 claim-less witnesses, but that population is disclosed in the headline,
so by this campaign's criterion it is not a defect. Recorded because I nearly
filed it as one.

---

## Items (2) and (3) ADDRESSED 2026-08-23 — differently, and on purpose

### (2) Dynamic reads — FIXED

`has_reader` matched literal filenames only, so a consumer building its path with
an f-string was invisible and its whole family looked reader-less. **33 distinct
f-string witness names** exist under `computations/`:

```
chi-{atom}-h{n}-at-q0-50dps.witness.json          (20 sites)
chi-{atom}-{kind}-h{n}-at-{q_tag}-50dps.witness.json
habiro-coefficients-{slug}.witness.json
atom-chi-rust-{iso}.witness.json                  … 33 total
```

`build_dynamic_readers` compiles them to family matchers, placeholders → `[^.]+`.

**The interesting part is what had to be rejected.** Compiled naively,
`chi-{atom_label}.witness.json` becomes `chi-[^.]+\.witness\.json` and claims
**every** `chi-*` witness in the corpus — `chi-convention-audit`,
`chi-content-eigenbasis`, `chi-convention-trM-ratio-probe`. A matcher that
over-claims manufactures readers, which un-exempts witnesses and produces
provenance accusations against caches the owner directive says not to chase.

So a pattern is trusted only with **≥ 12 characters of literal anchoring**
(placeholders excluded, `.witness.json` suffix excluded). Measured across
thresholds:

| min literal | patterns kept | exempt witnesses reached | spurious |
|---|---|---|---|
| 0 | 33/33 | 59 | **4** |
| 8 | 28/33 | 42 | 0 |
| **12** | **27/33** | **42** | **0** |
| 16 | 22/33 | 42 | 0 |

12 is the smallest threshold that is clean and keeps the most patterns. The
**6 rejected patterns are printed**, not dropped silently — a family behind one
of them can still look reader-less, and that is exactly the kind of residual
this bean exists to make legible.

### Effect, and a correction to my own estimate

| | after the `git grep` fix | + dynamic readers |
|---|---|---|
| `PROV_EXEMPT_NO_READER` | 229 | **217** |
| `PROV_MISSING` | 57 | **70** |
| corpus evaluated | 0.886 | **0.891** |
| completeness ratio | 0.9790 | **0.974** |

**12 witnesses moved, not the 42 I measured first.** `has_reader` is consulted
only for witnesses already sitting at `PROV_MISSING` (`:242`), so the other 30
were never in a state the exemption could apply to. Coverage up, score down —
both the honest direction, again.

### (3) Machine inventories — MEASURED and reported, deliberately NOT enforced

113 of the 114 `.json` files under `content/` that cite a witness name are
`*.qa.json` **QA sidecars** — generated from a block, not authored, and named by
`AGENTS.md` itself as bulk machine output. So a name appearing only there is not
really "the paper cites this."

Measured: **8** names reach the paper index only via a `*.qa.json` sidecar; a
further **3** only via `content/pipeline/` tooling; 11 together, which is the
figure I first quoted before separating the two scopes. The audit reports the 8
it can attribute to sidecars.

**Not enforced, and the reason matters.** Excluding them would move witnesses
*into* the exempt class — reducing what the audit evaluates. This bean's entire
thesis is that unevaluated is the thing to avoid, so silently shrinking the
evaluated set to be more "correct" would be the wrong trade for me to make
unilaterally. The count is printed and stored in the witness
(`paper_citations_only_from_machine_sidecar`) so whoever owns the rule can decide
with the number in front of them.

### Witness refresh checked for provenance downgrade

`python 3.11.15 / numpy 2.4.6 / scipy 1.17.1` before **and** after, and the run
emitted no environment warning — so this refresh does not weaken the record, the
way the `guarded-off-audit` refresh would have. Checked, not assumed.

---

## STATE OF THIS BEAN — 2026-08-23

| what it needed | state |
|---|---|
| (1) fail loudly instead of scoring on a failed index | **fixed** — health recorded + reported, and the index now *builds* (`git grep`, ~2 s vs a >120 s timeout) |
| (2) cover dynamic reads | **fixed** — 27 of 33 f-string families matched, 6 rejected as too weakly anchored and printed |
| (3) exclude machine inventories | **measured and reported; decision deferred** |

Cumulative effect on the audit, from the state this bean opened in:

| | at filing (index silently empty) | now |
|---|---|---|
| paper index | **0 names** | 588 |
| `PROV_EXEMPT_NO_READER` | 242 | **217** |
| `PROV_MISSING` | 45 | **70** |
| corpus evaluated | 0.882 | **0.891** |
| completeness ratio | 0.9838 | **0.974** |

The ratio fell every time something was fixed. That is the shape of a metric
that had been rising on failures.

### Left `todo` for one residual, and it is a decision not a defect

Whether a `*.qa.json` sidecar counts as the paper citing a witness. Excluding
them removes 8 names from the reader index, which moves those witnesses *into*
the exempt class — less evaluated, not more. That trade is the rule owner's to
make, and the number is now printed and stored in the witness rather than argued
about.

Also unchanged by design: `--strict` still fails on `PROV_MISSING` only, and this
file remains **not** gate-wired (`scripts/precision-gates.sh:267` wires the
similarly-named `computations/witness_provenance_audit.py`, a different audit).

---

## Merge note 2026-08-23 — the witness regenerated from MERGED code, not picked from a side

Merging `origin/main` conflicted on `witness-provenance-audit.witness.json`. The
producer `.py` auto-merged cleanly — my `build_dynamic_readers` /
`_sidecar_only_citations` alongside a sibling's `_is_prose` from `077de4548` —
but **neither side's witness had been produced by the merged code**, so taking
either would have committed a number no version of the script actually emits.
Resolved by completing the merge and **re-running the audit**.

### The sibling's fix is the same defect class, and worth reading

`077de4548` — *"a prose `scriptFile` is missing provenance, not provenance"*.
Six witnesses carry `scriptFile` values like
`"(legacy — no matching producer found; provenance pending manual triage)"`. That
string is truthy, so the emptiness test scored them `PROV_OK`. Their own commit
message states the consequence plainly:

> the I14 campaign (`f893cc92`, 2026-05-19) reached `prov_missing: 0` /
> `completeness_ratio: 1.00` **partly by WRITING THIS MARKER**, and the gate that
> should have noticed went green.

A perfect-score gate reached by writing the excuse into the field it checks.

### Combined effect

| | index empty (bean filed) | + my two fixes | + sibling `_is_prose` (merged) |
|---|---|---|---|
| `PROV_MISSING` | 45 | 70 | **89** |
| `PROV_EXEMPT_NO_READER` | 242 | 217 | **209** |
| `completeness ratio` | 0.9838 | 0.974 | **0.967** |
| corpus evaluated | 0.882 | 0.891 | **0.893** |

Three independent fixes, all pushing the headline **down** and coverage **up**.
The 0.9838 this bean opened against was the product of an empty index *and* six
self-written exemption markers.

Environment identical before and after (`python 3.11.15 / numpy 2.4.6 / scipy
1.17.1 / mpmath 1.4.1`), no environment warning — checked before committing, as
for every witness refresh in this campaign.
