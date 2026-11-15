---
# qou-mw1p
title: q0Anchor 'independent' is a bare token; the reason lives only in source comments
status: completed
type: task
priority: normal
created_at: 2026-08-16T02:14:02Z
updated_at: 2026-08-16T02:40:15Z
---

## Where it came from

Design advice from the #5124 owner, comment 5304560893 (2026-08-15 22:37),
given in reply to my intent note on `qou-rw91` and offered as "scar tissue
rather than review" from having built the same shape twice that week. I did
not act on it because I never saw it: my read of that thread was truncated by
pagination and I reported the truncation as "no reply". The advice had two
points.

**Point 1 — a positive declaration must be visible in the COUNT, not just the
record. Already satisfied, partly by luck.** `Q0_INDEPENDENT` is emitted and
counted beside `Q0_ANCHOR_MISSING` (5 vs 1885 as of `dad40261`), so declaring
independence does not shrink the inventory into silence. Their warning was
that if it did, "the next person to add a genuinely-forgotten anchor will
reach for it."

**Point 2 — the declaration must carry its REASON, in the artifact. NOT
satisfied; this bean.** What shipped is a bare token:

    w.save({"q0Anchor": "independent"})

The reason exists only as a source comment in each producer — e.g. that the
`qns_phase_*` probes' `q = 1.0 + eps` is the Sabra/DN **shell-spacing ratio**,
not the substrate modulus, and that `eps = 1e-1` landing on 1.1 beside
q₀ ≈ 1.10998 is coincidence. A reader opening the witness JSON sees
`"independent"` and nothing else. Their formulation:

> `q0_independent: "free parameter u; no substrate value read"` survives the
> next reader; `true` doesn't.

They also noted the precedent on the same axis — `<!-- literal-source: … -->`,
where "the marker is worth almost nothing; the text after the colon is the
whole value."

## Scope

Five witnesses currently carry the bare token (3 from `qou-rw91`, 2 from
`qou-kx04`), all on `main` as of `dad40261`:

- `qbeta-ohtsuki-nz-bridge-b4` / `-b6` — free parameter `u`; π, √3, exact
  Ohtsuki rungs, 4₁ geometry
- `qns-phase-decorrelation-probe` / `qns-phase-scramble-probe` — Sabra/DN
  shell-spacing ratio over `EPS_SWEEP`
- `dt-crossknot-snappy-slope-hardening`

## Design question for whoever takes it

Whether the reason belongs as a free-text `q0AnchorReason` beside the token, or
whether `q0Anchor` should itself accept a string, is open. A separate field
keeps the token machine-checkable (the audit's `classify()` matches on exact
tokens and maps anything unrecognised to `Q0_FLIP`, so widening the token to
free text would need care). The audit + `WitnessBuilder` guard added in
`b4b293fc` / `e6cc6ac5` are the touch points.

Not urgent — nothing is wrong on main. This makes a correct record legible.


## RESOLVED 2026-08-16 (PR #5194)

`q0AnchorReason` (free text) now rides beside `q0Anchor`, and all five
witnesses carrying the bare token have been re-run with a reason specific to
that producer — a generic string would have reproduced the same emptiness.

**Design question, decided: a separate field, not a widened token.** The
audit's `classify()` matches exact tokens and maps anything unrecognised to
`Q0_FLIP`, so folding free text into `q0Anchor` would have made every reasoned
declaration a flip. The token stays machine-checkable; the reason sits beside
it.

**Made visible in the count**, applying the same principle one level down:
`Q0_INDEPENDENT_NO_REASON` counts declarations that omit it, so a thin
declaration cannot pass as a complete one. End state
`Q0_INDEPENDENT 5 / Q0_INDEPENDENT_NO_REASON 0 / Q0_FLIP 0`.

**Dropped with its anchor.** A reason outliving the anchor it explains would
read as provenance for a claim the witness no longer makes — worse than none.
Two new tests cover carry and drop.

Not gating: `--strict` still exits only on `Q0_FLIP`, so the new verdict
reports without blocking.
