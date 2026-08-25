---
# qou-ibcv
title: c-q-q0.derivation.json is muon-pinned but the validator re-evaluates it at the proton pin — a live layer straddle the crash was hiding
status: completed
type: task
priority: normal
created_at: 2026-08-23T17:01:46Z
updated_at: 2026-08-23T19:06:09Z
---

Surfaced by fixing the crash in `qou-n7ue` item 1. The validator detected this
and then died reporting it, so it has never been printed.

## The numbers

| | value | = |
|---|---|---|
| chain's own `operation` text | `q_0 = 1.1099785955573347` | **muon** pin |
| chain's `target_value` | `9.092678397394828` | `1/(q_muon − 1)` |
| validator's `Q_0` | `1.1099785827513808` | **proton** pin |
| validator's re-eval | `9.092679456150243` | `1/(q_proton − 1)` |
| `rel_diff` | `1.16e-7` | against tolerance `1e-12` |

`computations/c-q-q0.derivation.json`, sole c_q chain of the 73 scanned.

## What it is, and what it is not

It is the **μ–p substrate tension**, appearing as a layer straddle: the chain
carries a muon-derived target while the validator applies the proton default
(the 2026-08-07 directive). AGENTS.md: *"Never straddle the two layers inside
one quantity."* Same class as the μ₃ Fréchet probe, one layer up — that one
mixed a muon `y_λ` with a proton `χ_λ`; this one states a muon target and
checks it against a proton evaluator.

It is **not** a float64 artifact, which is what I expected to find.
`_eval_simple_algebra` does return a Python `float` (`1.0/(q-1.0)`) — itself
worth fixing, and flatly contrary to the module's own line 49 comment,
*"chain values are carried as mpf, never float64"*. But the gap is `1.16e-7`,
about **nine orders of magnitude** above float64 resolution. The arithmetic is
not the cause; do not "fix" this by raising precision and expect it to close.

## The choice, which is not mine to make

Two coherent resolutions, and they are not equivalent:

1. **Re-derive the chain at the proton pin** — `target_value` becomes
   `9.092679456150243`, matching the compute-layer default. Consistent with
   "proton everywhere in compute", but it edits a recorded derivation whose
   prose explicitly quotes the muon value, so the prose must move with it.
2. **Let the chain declare its anchor and evaluate at it** — the chain is an
   *ideal/CAL-2* artifact and is correct as written; the validator is wrong to
   impose the compute default on it. This needs a `q0Anchor` field on the
   chain schema and a validator that honours it.

Option 2 is the better fit for a *derivation* record — the ideal-layer framing
is untouched by the proton re-pin, which governs what code evaluates at, not
what the calibration is — but it is a schema change and the owner's call.

## Fixed here

Only the crash: `mp.nstr` in place of the `.2e` format spec, so the validator
can report rather than die. The straddle itself is untouched and needs the
decision above. `_eval_simple_algebra`'s float64 return is left alone too —
separate defect, same file, and fixing it changes no verdict here.

## RESOLVED — option 1 taken (owner's call, 2026-08-23): re-derived at the proton pin

`53673c01fd`. The chain now evaluates at the experimental/proton anchor, per
the 2026-08-07 directive that compute defaults to proton:

```
target_value  9.0926794561502453911039703556573825637151463686661
              = 1 / (1.1099785827513808075916690956107688798744991218736 - 1)
```

The prose moved with the number — the step name and `operation` quoted the muon
value, and leaving them would have reproduced the same straddle one layer down
in the text. The leaf's `notes` records which pin it is on and why, so the next
reader does not have to infer the layer from a call site.

**The 50 digits are load-bearing, not decoration.** `validate_chain` loads with
`json.load(f, parse_float=str)` precisely so the authored digits survive rather
than being rounded through float64 by `json` before the module sees them. A
16-digit `target_value` would have thrown away the precision the loader exists
to protect.

## Also fixed, because this work exposed it

`_eval_simple_algebra` computed `1.0 / (q - 1.0)` in **float64** against a
target authored to 50 places, so the comparison had a floor of ~1e-16 no matter
how tight `target_tolerance` was set. A chain tightened past that would have
failed for arithmetic reasons and been read as a derivation error — the
`c₃`-normalisation trap in a different costume. It now carries `mpf` and takes
`q` from `Q_50_DIGIT_STR` rather than the float64 back-compat alias `Q_0`.

Measured read-only at each stage, no witness written:

| state | rel_diff | vs `1e-12` tolerance |
|---|---|---|
| straddle (as found) | `1.16e-7` | fails by ~10⁵ |
| re-derived, float64 re-eval | `2.63e-16` | passes, at the arithmetic floor |
| re-derived, exact re-eval | **`4.86e-51`** | agrees to all 50 authored digits |

`scripts/precision-gates.sh --changed`: all blocking gates green.

## What was NOT done, and why it still matters

Option 2 — letting a chain **declare** its anchor and having the validator
honour it — is not implemented. It remains the better fit for a *derivation*
record: the ideal/CAL-2 framing is untouched by the proton re-pin, which
governs what code evaluates at, not what the calibration *is*. This fix makes
one chain consistent with the compute default; it does **not** stop the next
ideal-layer chain from being checked against an experimental-layer evaluator,
because nothing in the schema records which layer a chain belongs to.

There is exactly one c_q chain among the 73 scanned, so the blast radius today
is one file. Worth a schema bean if the corpus grows a second one.
