---
# qou-bzy0
title: Three blocks in knots-particles-confinement are unregistered and never render
status: todo
type: task
created_at: 2026-08-24T21:01:32Z
updated_at: 2026-08-24T21:01:32Z
---

Found while closing qou-1ngr, 2026-08-24.

`content/quantum-observable-universe/knots-particles-confinement/knots-particles-confinement.ts` is the gate: a block whose slug is not in some section's `blocks[]` does not render, and its label does not resolve — any other block that links it fails validation with "Unresolved uses".

Sweep of the directory (~200 blocks) found exactly two stragglers, both committed and both complete:

  pion-mass-hyperbolic-threshold   (rem:pion-mass-hyperbolic-threshold)
  antiquark-channel-ledger         (rem:antiquark-channel-ledger, commit c8f1d436098)

Confirmed the hard way: adding `rem:antiquark-channel-ledger` to a new block's uses[] turned validate from "Valid — 26 issues" into "Invalid — 28", one of them an error. The reference was dropped instead, so rem:gluon-stabiliser-ledger states the volume contrast without linking the sibling remark that makes it.

Not just a registration edit — it needs an ordering decision. `antiquark-channel-ledger.ts` has `uses: ["rem:pion-mass-hyperbolic-threshold"]`, and the natural homes are sec:nucleon-derivation (it interprets def:derived-atom, section 2) for the ledger and the meson material (section 12) for the pion remark. Registering them in those spots makes the ledger point forward, which detangler-no-forward-ref will flag. Decide the placement, register both, then restore the cross-link from rem:gluon-stabiliser-ledger.

(The third unregistered slug is gluon-stabiliser-ledger itself, registered as part of qou-1ngr.)
