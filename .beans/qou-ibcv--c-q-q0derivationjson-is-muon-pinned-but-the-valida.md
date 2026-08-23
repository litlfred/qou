---
# qou-ibcv
title: c-q-q0.derivation.json is muon-pinned but the validator re-evaluates it at the proton pin — a live layer straddle the crash was hiding
status: todo
type: task
priority: normal
created_at: 2026-08-23T17:01:46Z
updated_at: 2026-08-23T17:02:24Z
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
