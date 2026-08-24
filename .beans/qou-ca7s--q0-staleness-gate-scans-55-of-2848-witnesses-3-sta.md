---
# qou-ca7s
title: q0 staleness gate scans 55 of 2848 witnesses — 3 stale reported, 454 real
status: todo
type: bug
priority: normal
created_at: 2026-08-23T20:17:00Z
updated_at: 2026-08-23T20:17:40Z
---

## What

`computations/substrate/witness_constant_staleness.py` is the q₀-constant
staleness detector, run `--strict` as a **blocking** gate by
`scripts/staleness-gates.sh`. Its docstring describes a corpus-wide detector:

> "…leaving **~390 witnesses** carrying the pre-re-pin q₀ that
> `run_pipeline.py` happily reports as 'fresh'." / "Wire it into the
> witness-pipeline so any future constant re-pin auto-flags the affected
> witnesses."

Line 277 as shipped:

```python
for wf in sorted(glob.glob(str(HERE / "*.witness.json"))):
```

`HERE` is `computations/substrate/`. One directory, **non-recursive**. It has
never looked at the rest of the tree.

## Measured, with the file's own predicates

Reusing this module's `Q0_SHAPE`, `AUDIT_SUFFIXES` and
`derived_output_exempt` — not a re-implementation, because a scan that
differs from the gate's own logic measures the scan:

| scope | scanned | q₀-stale |
|---|---|---|
| as shipped | **55** | **3** |
| whole tree (minus `.git`/`.claude`/`_deprecated`) | **2848** | **454** |

454 is the same order as the **~390** the docstring itself names. That is what
makes this an implementation/intent mismatch rather than a deliberate narrow
scope.

## 454 is NOT 454 defects — and this is the part to carry forward

Classified by the witness's **declared** `q0Anchor`:

| declared | count | reading |
|---|---|---|
| *(none)* | 340 | undeclared — cannot be adjudicated from the file alone |
| `muon` | 52 | **consistent.** The gated `qou-1c4y` migration population. Leave them. |
| `proton` | **49** | **contradictory** — declares proton, carries a non-proton q₀-shaped value |
| `independent` | 9 | needs the `q0AnchorReason` read |
| `ambiguous` | 3 | — |
| `comparison` | 1 | — |

The 49 are the class bean **`qou-bdkx`** triages. **That bean lists 2 of
them**, because it was written from the 55-file scan — so its "4 witnesses
declare one anchor and carry another" is 4 out of 55, not 4 in the corpus.
Nothing in the bean says otherwise; the scope simply was not visible.

**Even the 49 are candidates, not findings.** A proton-declaring witness may
carry a muon value as a *deliberate comparison* — one of them is literally
`low-isotope-binding-model-comparison.witness.json` — and at least one basin
match, `1.109940825176`, is **neither** pin, so the basin regex `1\.1099\d{6,}`
is catching something else entirely. `qou-bdkx` is right that this needs
per-witness triage and must never be batch-fixed.

## A fifth contradictory case, in the direction the bean has none of

Found while draining tier C of the derivation-chain gap:
`computations/derived-chi-catalogue-matrix-m-mu-n-mpfr.witness.json` declared
`q0Anchor: "muon"` with the muon `q0Value`, while `data.q_0_substrate_str` and
**both** code paths in its producer (`derived_chi_catalogue_matrix_m_mpfr.py`
lines 523 and 692) use `Q_50_DIGIT_STR` — the **proton** pin.

Every case in `qou-bdkx` runs the other way (declares proton / independent /
none, carries muon). This one declares **muon** and carries **proton**, which
is why the "muon basin" framing does not reach it.

Resolved by re-running the producer, per the never-hand-edit rule. The diff is
the evidence: masking ephemeral and timing fields, **exactly two fields moved**
— `q0Anchor` muon→proton and `q0Value` — and **zero** mathematical fields. The
computation was proton-pinned all along; only the label was wrong. Resolution
class (b) from `qou-bdkx`: payload right, declaration wrong.

## Done here (PR #5584)

`--tree` added as an **opt-in** flag, with the scope note and these numbers in
the source beside the glob. Default behaviour is byte-identical (55 scanned, 3
stale, verified).

Opt-in rather than a default flip because `scripts/staleness-gates.sh` runs
this `--strict` as a blocking gate: changing the default turns a green
blocking gate red with 454 findings in one commit, and 392 of those (340
undeclared + 52 muon) are not actionable without the `qou-1c4y` sign-off.

## Next

1. Triage the 49 contradictory ones per `qou-bdkx`'s (a)/(b) rubric. Start
   with the ones whose producer reads a named accessor — those settle fast,
   as the derived-chi case did.
2. Decide what an undeclared anchor means for the 340. Probably: require
   `q0Anchor` at `WitnessBuilder` level so the class cannot grow, then
   backfill.
3. Flip `--tree` to the default **only** after 1 and 2, or the blocking gate
   cannot be green.
4. Update `qou-bdkx` to say its counts were 55-file-scoped.
