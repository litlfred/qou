# Draining the derivation-chain gap — tiering and program of work

**Tool:** [`computations/audits/derivation_gap_categorize.py`](../../computations/audits/derivation_gap_categorize.py)
(read-only; `--json`, `--tier <name>`). Re-run it rather than quoting the numbers
below — they move as chains land.

## Why the headline number was not actionable

`derivation_chain_validator.py` reports one figure: witnesses with no derivation
chain. After the recursive-scan fix (#5269) that figure became honest (~2.6k) but
it was still not *workable*, because it mixed objects with completely different
obligations — a QA tool's output, an exploratory probe, and a production compute
all counted the same. The first job was to split it by **the work each witness
actually needs**.

## The tiers

| tier | count | what it is | what closes it |
|---|--:|---|---|
| **A** audit-only | 737 | witness declares `auditOnly` — it records a QA/audit tool's *finding*, not a derivation of a physical target | **EXEMPT** (landed) — reported in its own bucket, never dropped |
| **B** probe | 287 | exploratory scope-(a) compute under `probes/` | low priority; a chain is meaningful but these are not production |
| **C** family | 66 | production witness whose producer emits **many** witnesses | **one chain drains the whole family** — the audit matches producers by basename |
| **D** singleton | 1233 | production witness with its own producer | per-compute authoring by someone who understands that derivation |
| **E** orphan | 186 | **no producer script on disk** | provenance triage first — a chain cannot honestly be authored |

**Actionable (C + D): 1299.** A and E are not "work avoided": A is a category
correction, E is blocked on recovering provenance.

## Why tier A is an exemption and not a cover-up

The distinction matters, because hiding a gap inside a measurement is exactly the
defect #5269 fixed. The difference:

* #5269's invisibility was an **accident** — a non-recursive glob nobody chose.
* Tier A is a **stated classification**: demanding a first-principles chain for
  the output of a sorry-counter is a category error. The audit already skipped
  its *own* witness on precisely this basis.

So tier A is reported as `audit-only-exempt`, a bucket of its own, printed in the
summary line beside the others. The denominator is visible; nothing shrinks
silently.

## Order of work

1. **Tier C, largest family first.** Highest yield per chain. `canonical_isotope_witness`
   (120 shards) landed as the first drain — see the worked example below.
2. **Tier D, by domain owner.** The irreducible bulk. A chain here is only honest
   if its author understands that compute; authoring one for compute you do not
   understand is the laundering the discipline forbids.
3. **Tier E, triage.** Recover the producer or retire the witness. Do not author a
   chain against a producer that no longer exists.
4. **Tier B, last.** Probes are exploratory by construction.

## Worked example — what a family chain may and may not claim

[`canonical-isotope-witness.derivation.json`](../../computations/canonical-isotope-witness.derivation.json)
drains 120 shard witnesses with one chain, because `canonical_isotope_witness.py`
is a read-many/compute-little **orchestrator**: it assembles upstream layer
predictions, attaches AME 2020 reference values, and records upstream witness
sha256/commitSha.

Its trust profile is `{derived: 1, script-cited: 4}` — and that is the honest
result, not a shortfall. **A composition chain records assembly and provenance; it
does not make its inputs derived.** The audit's vocabulary already carries the
distinction: any chain with a SCRIPT_CITED step is `derivation-backed`, never
`derivation-fully-trusted`. Draining a family makes the composition auditable and
pins it to specific upstream state; the upstream producers still need their own
chains.

Read that as the standard for the rest of the program: a chain that *cites* is
worth authoring, and must not be described as a chain that *derives*.
