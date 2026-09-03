# `canonical-mass-table-242ppb` should NOT get a producer — it disagrees with the code it cites, in both directions

**Date:** 2026-08-30 · **Bean:** `qou-nro6` · **Upstream:**
[`2026-08-30-orphan-witness-triage.md`](2026-08-30-orphan-witness-triage.md)

Tier-A item 2 of the orphan triage. Unlike
`hecke-core-symbolic-migration`, which got a producer, **this one should not**,
and the reason is a finding rather than a scoping call.

## It declares itself hand-authored

Its own fields say so, and honestly:

```json
"auditOnly": true,
"provenance": "Hand-authored summary witness: no producer script was run to
               generate this file, so it carries none of the standard
               provenance fields (scriptFile, scriptHash, scriptCommitSha,
               computedAt)."
"open_gate": "delta_lambda",
"delta_lambda": { "status": "open",
                  "note": "... The B(K) above are NOT a derived Delta_lambda" }
```

So the `B_pred` column is explicitly **not derived** — it summarises a state of
play behind an open gate.

## But two content blocks cite it as a computed witness

- `mba-step09b-per-isotope-binding.ts` names it in `computation.witness`, with
  `script: "qou-mass/src/qou_mass/api.py"` and `status: "experimental"`;
- `mba-step09b-per-isotope-binding.md` calls it the *"Witness contract"*;
- `mba-chain-map.md` carries it as the step-9b row, against
  `qou_mass.predict(atom, observable="binding_energy")`.

## The named API does not reproduce the table

Running the API the chain map names, at current `main`:

| isotope | witness `B_pred` | witness err | live `predict` | live err |
|---|--:|--:|--:|--:|
| D | 2.735 | +23.0 % | **2.2488207** | **+1.09 %** |
| T | 8.992 | +6.0 % | **8.4685983** | **−0.16 %** |
| ³He | 8.739 | +13.2 % | **7.4889193** | **−2.97 %** |
| ⁴He | 29.317 | +3.6 % | 29.955677 | +5.87 % |
| ⁶Li | 33.526 | +4.8 % | 43.657005 | **+36.45 %** |
| ⁷Li | 40.776 | +3.9 % | 51.337671 | **+30.81 %** |
| ⁹Be | 60.207 | +3.5 % | 67.305750 | +15.72 % |
| ¹⁰B | 67.303 | +3.9 % | 75.593164 | +16.74 % |
| ¹²C | 95.225 | +3.3 % | 97.148000 | +5.41 % |

**Same observable and same anchor** — the live D result reports +10903 ppm on a
base of ≈ 2.2246, which is the witness's own `B_AME = 2.225`. So the two are
comparable and they disagree.

**They disagree in both directions.** The light isotopes are dramatically
better than the table claims (D +23.0 % → +1.09 %; T +6.0 % → −0.16 %; ³He
+13.2 % → −2.97 %), and everything from ⁴He up is dramatically worse (⁶Li
+4.8 % → +36.45 %). The table's story — a uniform ~3–5 % overshoot across
A = 4…12 — is not what the code now does at all.

## Why a producer would be the wrong fix

Writing one means choosing what it computes, and both options are bad:

1. **Emit the live `predict` numbers.** That silently replaces the paper's
   cited table with a different one, changing published error figures by up to
   32 points, under the cover of "adding provenance". A provenance PR must not
   move a physics number.
2. **Emit the committed numbers.** That is transcription, not derivation —
   exactly what the triage warned against. And it would freshly stamp
   `scriptFile`/`scriptHash` onto figures no live code produces, converting an
   honestly-labelled hand-authored summary into something that *looks*
   reproducible. Strictly worse than the current state.

The witness is already honest about what it is. **The defect is the manifest
claim around it**, not the file: `computation.witness` + `computation.script`
assert a producer relationship that does not exist, on a table whose own body
says it was hand-authored behind an open gate.

## What is actually needed

An author decision, not an agent one. The options, with what each costs:

- **Correct the manifests** — drop `computation` from
  `mba-step09b-per-isotope-binding.ts` (or mark it `auditOnly`), so the block
  stops asserting a producer. Cheapest; changes no number; leaves the paper
  citing a hand-authored summary *as* a hand-authored summary.
- **Regenerate the table from `qou_mass.predict` and update the prose** —
  honest and reproducible, but it moves published per-isotope errors by up to
  32 points and the ⁶Li/⁷Li rows become +30–36 %. That is a physics-facing
  change and needs the author's eyes on whether the live path is the one the
  appendix means.
- **Do nothing** — the appendix keeps citing a table the code disagrees with,
  and the next reader to check finds what this audit found.

**My recommendation, marked as judgement:** correct the manifests now
(option 1), and open the table-vs-code divergence as its own bean. They are two
different problems and only the first is a provenance question.

## Scope

This is a measurement and a recommendation. **No producer was written, no
witness was touched, no manifest was edited.** The divergence between the
committed table and the live API is reported as measured; this audit does not
claim which is correct.
