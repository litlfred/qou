---
# qou-bdkx
title: 4 witnesses declare one q0 anchor and carry another — declaration/payload contradiction
status: todo
type: bug
created_at: 2026-08-23T07:53:49Z
updated_at: 2026-08-23T07:53:49Z
---

Split out of qou-p8lx after re-measuring the `q0 constant staleness` gate on
main (2026-08-23). The gate flags 6 witnesses in the muon basin; they are NOT
one backlog.

CONSISTENT — valid as recorded, part of the GATED bulk migration (qou-1c4y,
needs scoped sign-off). Do not drain these here:

  lever1-binding-core-characterization        q0Anchor=muon,  .q0Value muon
  lever1-binding-habiro-single-element-test   q0Anchor=muon,  .params.q0 + .q0Value muon

CONTRADICTORY — declared anchor disagrees with the payload. Actionable WITHOUT
the gated migration, because the fix is to reconcile a declaration with a
value, not to re-pin the corpus:

  lever1-color-eq-intrinsic-tau-rapidity   declares 'proton'
      .results.substrate_q0.q = 1.10997859556        (muon basin)
  lever1-color-eq-lambda-sw-rapidity       declares 'proton'
      .results.q0 = 1.109978595557335                (muon basin)
  z2bn-tau-derivation-probe                declares 'independent'
      q0AnchorReason: "Reads no substrate value. PROVED by run..."
      .q0 = 1.1099785955573347199                    (records one anyway)
  knot-volumes                             declares NO anchor
      .assertions[9].computed = 1.1099785955541805

This is the "layer straddle" AGENTS.md calls a defect regardless of size: an
ideal-layer (muon) value inside an experimental-layer (proton) declaration.

## Per-witness triage still needed — do NOT batch-fix

Each has two possible resolutions and they are not interchangeable:
  (a) the declaration is right, the payload is stale  -> re-run the producer
      at the declared pin;
  (b) the payload is right, the declaration is wrong  -> fix the declaration.

Which applies needs the producer read. AGENTS.md is strict here: never
hand-edit a witness to match a table — fix the producer and re-run.

`z2bn-tau-derivation-probe` is the most interesting: 'independent' means
"reads no substrate value", so either the .q0 field is informational
provenance (declaration right, field misleading) or the probe does consume
q0 and the declaration is false. Those have opposite fixes.

## Measurement note

My first scan of these reported `knot-volumes: 0 muon-carrying fields` while
the gate reported one. My scan only walked STRING values; the value is a JSON
number. Anyone re-measuring must walk numbers too — repr() the float, do not
rely on the serialized text.
