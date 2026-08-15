---
# qou-rw91
title: 'PRECISION: 3 witnesses landed with no q0Anchor (Q0_ANCHOR_MISSING 1882 -> 1885)'
status: todo
type: task
created_at: 2026-08-15T10:57:22Z
updated_at: 2026-08-15T10:57:22Z
---


Found by a full `scripts/precision-gates.sh` run, 2026-08-15, while
working `qou-6ixs`. The regenerated audit witness is committed in
`afff724830` with the count named.

```
audits/q0-anchor-consistency-audit.witness.json
  Q0_ANCHOR_MISSING  1882 -> 1885
```

Three witnesses landed **without recording which q₀ pin they used**.
Two are visible in the diff:

- `qbeta-ohtsuki-nz-bridge-b4.witness.json`
- `qns-phase-decorrelation-probe.witness.json`

The third is in the regenerated list and needs reading off.

**Why this matters more than the count suggests.** AGENTS.md
§"q₀ anchor convention" rule 4 is explicit: *"Say which pin you used. Any
new witness must record its q₀ so a later reader can tell which layer it
belongs to without inferring it from a call site."* The rule exists
because of the muon/proton layer-straddling class — the μ₃ Fréchet probe
took `y_λ` from the muon-built cache while evaluating `χ_λ` at the proton
`q₀`, an 11.54 ppb separation that is the μ–p substrate tension itself.
A witness with no anchor recorded is exactly the state in which that
defect is undetectable by inspection.

Not this branch's landings. Fix at each producer by recording the anchor,
not by backfilling the audit.
