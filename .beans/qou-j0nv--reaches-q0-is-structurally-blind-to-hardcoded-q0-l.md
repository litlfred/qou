---
# qou-j0nv
title: reaches_q0() is structurally blind to hardcoded q0 literals — 38 producers stamped q0_anchor=False hold one
status: todo
type: bug
priority: normal
created_at: 2026-08-30T12:32:18Z
updated_at: 2026-08-30T12:32:18Z
---

Found while closing `qou-0hnz`; measured before filing.

## The defect

`scripts/migrate_bare_producer_provenance.py:114`

```python
Q_MARKERS = ("q_parameter", "Q_50_DIGIT", "qou_substrate.constants", "q_at", "Q_MP")
```

Every marker is a **resolution name**. A producer that hardcodes
`1.1099785955573347…` matches none of them, so `reaches_q0()` (`:164`) returns
False and the script stamps `q0_anchor=False` — "no q0 in this producer's cone" —
over a file with a q0 literal in it.

The function's own docstring says it is *"Deliberately conservative: anything
this cannot rule out is treated as q0-dependent, so the anchor is stamped."*
That is precisely backwards for literals: it cannot SEE them, so it silently
rules them out. The conservatism is real for the import-hop case and absent for
the literal case.

## Measured population

Of **389** producers stamping `q0_anchor=False`, **44** hold a q0 decimal literal
on a non-comment line with no resolution marker anywhere. Splitting those:

| | count |
|---|---|
| audits/detectors holding the literal as a fixture — legitimate | 6 |
| **real producers — the defect** | **38** |

Examples: `a3_magnitude_berezinian_crossterm_probe`,
`alpha_em_perloop_integer_forcedness_probe`,
`deltalambda/mu4_rhoF_cluster_derivation_probe`,
`probes/binding_additive_linked_cluster_probe`.

Consequence: those 38 carry no `q0Anchor`, land in `Q0_ANCHOR_MISSING`, and are
invisible to any check keyed on the stamp — while actually being q0-dependent.
This is how `tau_binding_hitchin_wzw_wall_probe` came to stamp
`q0_anchor=False` under a comment reading "no q0 in this producer's cone" with
the literal 30 lines above it.

## Todo

- [x] Add a q0-literal pattern to the detector so `reaches_q0` sees pinned files.
- [x] Do NOT mass-restamp on the strength of it — reported first, then RUN on
      owner instruction 2026-08-30.
- [x] Exempt audits/detectors that hold the literal deliberately as a fixture — **deliberately NOT done, see below**.


## Progress 2026-08-30 — detector fixed, restamp deliberately not run

`Q0_LITERAL = re.compile(r"1\.10997858|1\.109978595")` added and consulted by
`reaches_q0`. Covers both pins: proton `1.10997858…` and the muon family
`1.109978595…` (vintages A, A′ and C all share that prefix). `reaches_q0` is fed
comment-stripped source (`code_only`), so a pin quoted in prose does not trip it.

Verified directly:

| source | reaches_q0 |
|---|---|
| resolved via `q_parameter` | True (unchanged) |
| hardcoded pin A | **True** (was False) |
| hardcoded pin C | **True** (was False) |
| hardcoded proton | **True** (was False) |
| no q₀ | False |
| unrelated decimal `1.10998` | False — does not over-match |

**Effect, measured with the script's own `code_only` + import-hop logic** (this
supersedes the 38 in the filing, which used a rougher filter): of the producers
stamping `q0_anchor=False`, **41 real producers** now classify as q₀-dependent,
plus **6 audits/detectors**.

**No restamp was run.** Re-running the migration script would rewrite 41
producers' provenance in a single sweep; that is an owner-visible change and
belongs in its own pass, not as a side effect of fixing a detector.

### Why the audit exemption was NOT added

The filing proposed exempting audits that hold the literal as a fixture. On
reflection that reintroduces the same blind spot in a narrower form, and it
contradicts the function's own stated philosophy — *"deliberately conservative:
anything this cannot rule out is treated as q0-dependent, so the anchor is
stamped."* Over-stamping an audit is the **intended** failure direction;
under-stamping a producer is the defect being fixed. A path-based exemption
would also be fragile (it keys on directory names, not on what the file does).
Left unexempted on purpose; the 6 are named above so a restamp pass can judge
them individually.


## 2026-08-30 — restamped on owner instruction

**The migration script could not do it.** `--dry-run` finds only 16 *bare*
producers (2 transformable): its job is to ADD provenance to producers that have
none, and it detects already-touched files by `STAMP_MARKER`. The mis-stamped
population is already stamped — with `q0_anchor=False` — so it is excluded by
construction. Running `--apply` would have touched 2 unrelated files and none of
the real ones.

So the restamp was done directly, against the script's own documented rule
(module docstring): *"anything this script cannot show to be q0-free gets
`q0_anchor=None` (resolve and stamp)"*. `q0_anchor=False` → `q0_anchor=None`
in exactly the files where the FIXED `reaches_q0` returns True.

| | files | stamp sites |
|---|---|---|
| real producers | 47 | 59 |
| audits/fixtures (not exempted, see above) | 6 | 8 |
| **left alone** — genuinely q₀-free, stamp stays `False` | **336** | — |

53 files changed, AST-checked, 0 failures. Verified after: **0** q₀-reaching
files still stamped `False`, and the 336 free ones untouched.

(47, not the 41 in the filing: that number counted files where a literal was the
*sole* reason. This uses the script's full `reaches_q0`, so it also catches ones
reachable via the import hop that were stamped False anyway.)

### What this does NOT do

The stamp lives in the SOURCE. Those 47 witnesses do not carry a corrected
anchor until each producer is re-run — they will get one on next regeneration,
not now. No witness was regenerated here.

- [ ] Regenerate the 47 so their witnesses carry the anchor the source now
      resolves (qou-jjge).
