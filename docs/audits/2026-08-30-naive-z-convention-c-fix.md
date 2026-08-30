# The naive-z convention-C residue: fixed at the producer, and one orphan left standing

**Date:** 2026-08-30 · **Branch:** `claude/mu4-magnitude-gap-2026-08-30` · **Bean:** `qou-9o0z`
**Scope:** (a). Verdict unchanged; numbers move.

## What was wrong

[`deuteron_naive_z_physical_probe.py`](../../computations/deltalambda/deuteron_naive_z_physical_probe.py)
computed its central quantity as

```python
v = mp.sqrt(q0); two_v = v + 1/v
z_naive = 1 / two_v            # == √q/(q+1) == z_C
```

That is **convention C**, excised by the owner rulings of 2026-08-09 and
2026-08-15 R1. It is the **sqrt-variable spelling** `AGENTS.md` catalogues as
detector-blind — the shape audit keys on assignment/return forms and reports
these *nowhere*, which is why it survived every C sweep.

**It was a live defect, not a deliberate C reference.** By `AGENTS.md`'s own
criterion a deliberate C site announces itself (a `_legacy` name, an
`@[deprecated]`, or a docstring saying convention-C / comparison / historical).
This one was presented as *"the naive Markov bond factor"* — unqualified.

## Fixed at the producer; the verdict survives

`z_naive = q0**3 / (q0**2 + 1)` — convention D. Re-run: **exit 0, all assertions
pass**, verdict unchanged (*"HONEST NEGATIVE … PHYSICAL at A=2, EXCLUDED at
A=4"*). What moved:

| quantity | was (C) | now (D) | status |
|---|--:|--:|---|
| `z` | 0.4993203342 | 0.6126880371 | — |
| A=2 `det = 1−z²` | 0.7506792 | 0.6246134 | still **> 0**: still PHYSICAL |
| A=4 `det = (1−5z²)(1−z²)` | −0.1851205 | −0.5477442 | still **< 0**: still EXCLUDED |
| `b2 = −ln det` | 0.2867769 | 0.4706224 | — |
| required scale to reach `B_AME` | 7.76 MeV | 4.73 MeV | still undrivable |

**Both legs of the cross-A argument hold under D, and the A=4 exclusion
strengthens** — `z_D` sits further above the `1/√5 = 0.4472136` ceiling than
`z_C` did.

Three docstring figures contradicted the new output and were corrected in place
(`z ~ 0.4993`, `det = 0.751`, `b2 is O(0.2–0.3)`, `7.76 MeV`), plus two verdict
strings still spelling `z = 1/[2]_v`. Leaving those would have reproduced the
declaration-vs-body defect this repo keeps hitting. `z_naive_C_historical` is
retained in the output **solely** so the delta is auditable.

**Coincidence, flagged and dismissed:** `b2(z_D) = 0.47062` sits 0.04 % from the
μ₃ simplex target `0.4708`. They are **not comparable** — `b2` is a
dimensionless log-cumulant, the μ₃ target is in MeV. Recorded so the next reader
does not spend time on it.

## The orphan that is NOT fixed here, and why

[`a4-interface-magnitude-one-scalar-gate.witness.json`](../../computations/deltalambda/a4-interface-magnitude-one-scalar-gate.witness.json)
carries the same stale value in `inputs.naive_z_bond_factor` (`0.499320334`) and
in its `description`. It is **not fixed**, for a stated reason:

- **It has no provenance at all** — `scriptFile`, `engine`, `computedAt`,
  `commitSha`, `scriptHash` are all absent. It is a **bare witness**.
- **No producer writes it.** The only `.py` mentioning the string is the probe
  above, and that is a docstring citation of the companion *audit doc*; the
  probe emits `deuteron-naive-z-physical-but-does-not-close.witness.json`.
- So the only way to change its number is to **hand-edit a witness**, which
  `AGENTS.md` forbids outright. Per the bare-producer rule the correct sequence
  is: **give it a producer that emits provenance first**, then regenerate.

**The exclusion it supports is unaffected either way** — verified above, `z_D`
is excluded more strongly than `z_C`. What is stale is the cited number, not the
verdict. Tracked as follow-up rather than papered over.

## Verification

- Probe: **exit 0**, all assertions pass, re-run three times across the edits.
- Convention arithmetic exact in `mpf` from `q₀`; `float()` only in display.
- Exit codes captured directly, never through a pipe.
