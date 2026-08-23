# The 58 convention-C witnesses, triaged — 1 source migration, not 58

**Date:** 2026-08-23
**Beans:** `qou-9bfp` (this triage), `qou-xram` (the `hadron_knot_table` crash)
**Script:** [`computations/audits/convention_c_witness_triage.py`](../../computations/audits/convention_c_witness_triage.py)
**Follows:** [PR #5510](https://github.com/litlfred/qou/pull/5510) §3, which measured the 58 and explicitly declined to treat the number as a work order

## Result

```
convention-C witnesses found : 58        (independently reproduces #5510's count)

live-C-producer               1     needs a real source migration
stale-output                 25     mechanical: re-run the producer
deliberate-comparison         0     among these 58 — but the class is real, see below
unresolved                   32     needs an agent to look
```

#5510 was right that 58 is not a work order. **The actionable source surface is one file.**

## The one live convention-C producer

[`computations/mass-from-q-symbolic.py`](../../computations/mass-from-q-symbolic.py) — two sites, lines 314 and 424:

```python
1.0 / (Q0**0.5 + Q_INV0**0.5)      # = 1/(√q + 1/√q) = z_C
```

This is a **double** defect, and the second half is the more serious one:

1. **Convention C**, live, on a path that writes a witness parameter (`w.add_parameter("z_markov", …)` at 424).
2. **float64.** `1.0 / (Q0**0.5 + Q_INV0**0.5)` is float arithmetic end to end — `**0.5`, not `mp.sqrt`, and a `1.0` literal numerator. Per the 2026-08-18 STRICT directive this is a defect on its own, independent of the convention, and it is being *serialised into a witness*.

Fixing the convention without fixing the arithmetic would leave the second defect in place at the same line.

This count of **1 actionable source site** independently corroborates #5510's `convention-c-producer-audit.py` run, which reported the same number by a different method.

## The claim that the anchor witness contaminates its readers — no instance found

The in-flight framing when this was handed over was:

> `computations/q-pinning-50-digit.witness.json` — the canonical q₀ pinning
> witness, the declared source of truth — itself carries
> `derived_50_digit.z_markov = 0.49932…`, i.e. convention C. **Anything reading
> that field inherits C regardless of its own source.**

The first half is **true and worth recording**: the anchor witness does carry a convention-C `z_markov`.

The second half has **no instance in the corpus.** Measured:

- `grep '\["z_markov"\]' / '.get("z_markov"'` across all live `.py` → **zero reads.**
- Every reader of that block takes the `q` subfield: `["derived_50_digit"]["q"]`.
- The one reader that binds the whole dict, `q_parameter.py:111`, uses only `_d["q"]` and says so in a comment: *"Take ONLY q from the witness … NOT from the witness's q_inv/hbar_q strings."*

So the field is **inert** — a stale convention-C value recorded in the anchor witness and read by nothing. That makes it a provenance defect (the anchor advertises a convention it does not supply), **not** a live contamination path, and **not** the root cause of the 58.

This matters for sequencing: had the field been live, nothing downstream could be fixed before it, and the work order would invert. It is not, so the 58 decompose independently.

**Do not "fix" it by re-pinning the file.** AGENTS.md rule 1 is explicit that `q-pinning-50-digit.witness.json` is anchor-*defining* — it is what `_q0_value_for_anchor("muon")` reads, and re-pinning redefines what "muon" means corpus-wide (262 `Q0_FLIP`s, measured). Removing or relabelling an unread field is a different and much smaller operation than re-pinning, but it still touches the anchor file, so it is flagged here rather than done.

## The 32 unresolved are one shape, not thirty-two problems

Most carry the same signature: the producer is **byte-identical** to when it emitted the C value, yet contains no convention-C spelling. Both halves cannot be true of a self-contained producer, so the C came from **a dependency, not the file** — the import-cone drift class AGENTS.md documents (a producer's own source is stable while a module it calls changed).

That is a tractable next step, and it is one query rather than 32: resolve each producer's import cone to whichever module supplies its `z`. It is deliberately **not** done here — this triage scopes the work, and guessing the cone would re-commit the error the next section is about.

## The class that is not in these 58, and must never be swept

`deliberate-comparison` scores 0 here, which is a fact about *these witnesses*, not evidence the class is empty. The clearest member emits no witness at all:

[`computations/schur_principal_mpmath.py::_wenzl_constants_convention_C_HISTORICAL`](../../computations/schur_principal_mpmath.py) is live convention-C code, retained on purpose, and its docstring states why:

> **DEAD FOR PRODUCTION** — convention C, excised 2026-08-09. Retained because
> the excision has to stay **measurable**. … Left unpreserved, that comparison
> silently degrades to D-vs-D and reports C's `y_(1³)/y_(3)` as 0 with a
> spurious *integral* `N* = 2` — the exact opposite of the finding it exists to
> display.

Any future sweep keyed on "find C spellings, replace with D" destroys this and reports success. The triage script therefore checks for quarantine markers before classifying a C spelling as live.

## A detector error in this script, recorded rather than quietly fixed

The first run of this triage reported **3** live-C producers. Two were false positives of my own making: the closed-spelling regex allowed any expression inside `sqrt(...)` and any polynomial in the denominator, so

```python
sqrt(q ** 4 + q ** 2 + 1) / (q ** 2 + 1)      # NOT z_C
```

matched a pattern meant for `sqrt(q)/(q + 1)`. Two probes — `qbeta_direction_sanity_gate_probe.py` and `qbeta_symbolic_sdp_strict_complementarity.py` — were wrongly flagged as needing migration.

The arguments are now pinned (`sqrt(q)` exactly, denominator exactly `(q + 1)`), and the comment at that regex records the failure so it is not re-loosened. Noting it because a convention detector that over-fires produces exactly the wrong outcome here: it sends an agent to "migrate" correct code, which is how a working file becomes a broken one.

## What this is not

- **Not a verdict per witness.** These are high-recall candidates in the repo's usual sense. Producer drift cannot see import-cone drift; a hash match cannot separate "still computes C" from "computes D now, witness predates a rename". The decisive test is re-running the producer — which is what this triage exists to *scope*, because re-running all 58 is precisely what #5510 measured as the wrong move.
- **Not a sweep authorisation.** The 25 `stale-output` are mechanical *individually*; nothing here authorises a bulk regeneration, and `qou-1c4y`'s constraints still govern anything touching pins.
- **Not a check of `hadron_knot_table`.** It crashed twice for #5510 (missing `scipy`, then `dtype=object` into `scipy.sparse`) and is tracked as `qou-xram`. Any "just re-run the producer" plan silently does not apply to producers blocked that way.

## Reproduce

```bash
python3 -u computations/audits/convention_c_witness_triage.py
python3 -u computations/audits/convention_c_witness_triage.py --json triage.json
```
