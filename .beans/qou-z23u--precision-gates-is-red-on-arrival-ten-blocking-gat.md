---
# qou-z23u
title: 'precision-gates is red on arrival: ten blocking gates, all inherited debt'
status: in-progress
type: task
priority: normal
created_at: 2026-09-03T15:43:09Z
updated_at: 2026-09-03T15:52:43Z
---

## Measured 2026-09-03 on main `26bd234527` — and mostly already owned

**Check-before-work paid off: bean `qou-hah0` (in-progress) already owns this**
and has landed two of its fixes on main — `2b768409987` (the preflight only
checked `mpmath`, so 4 of 8 reds were phantoms dying on ModuleNotFoundError)
and `ba4c0cf3e1a` (a float64-padding red). Do not re-diagnose from scratch;
read that bean first. What follows is what is NEW since its 2026-08-30 run.

### The 18 "flips" were 1 flip and 17 unmappable LABELS (fixed, 82b2535ce8 + d2767e894e)

`Q0_FLIP` is documented as *"anchor and q0Value disagree"* — a checked
contradiction. One branch returned it when the anchor label could not be mapped
to a pin at all, where nothing was compared. 17 of 18 were that branch:
witnesses writing prose into the token field (`'proton (experimental pin)'`,
`'both: proton q_at() + muon q_muon_at() @ CODATA 2022'`).

This reconciles `qou-hah0`'s `Q0_FLIP 1` with today's 18 — the prose-labelled
witnesses landed after their run.

**And the producers were not careless: `stamp_staleness_metadata` had no reason
slot for a string anchor.** `q0AnchorReason` was written on exactly one path,
the `q0_anchor=False` branch. A producer wanting to say *why* had one field to
say it in. An API gap presenting as seventeen producer defects.

Fixed both ends: new `Q0_ANCHOR_UNRECOGNISED` verdict (still CI-failing —
"could not check" is never green — but counted apart from a real flip), and
`q0_anchor_reason` added to the helper with all 17 call sites split. All 17
re-run, 17 ok / 0 failed, **every computed number byte-identical** including
`q0Value`. `Q0_ANCHOR_UNRECOGNISED` 17 → 0.

### tower-walk probe: two gates, one root (producer fixed, WITNESS NOT REGENERATED)

`tower_walk_magic_replication_probe` sat in `never_raises_dps` AND
`witness_float64_padding` at once. Its comment says it aggregates 77 traces in
mpmath so float64 error does not compound — correct intent, not delivered:
**`mp.dps` on entry was 15**, mpmath's default, where an mpf sum accumulates
exactly as a float sum. Then it serialized with a bare `fmt`, default width
**60** digits, on values whose source is `float(abs(np.trace(st)))` — float64
by construction. 22 padded fields.

The halves pull opposite ways: raising dps fixes the arithmetic and makes the
serialization worse. Both fixed.

**The witness is stale until someone re-runs it with a real compute budget.**
Recorded runtime 40 min; this container measured 5 of 77 partitions in 434 s
for the first of five configurations. The walk touches no mpmath so the dps
raise costs nothing on the hot path — the machine is just slower.

### Still open

- **`hadron-knot-table` — the one real Q0_FLIP.** `qou-hah0` settled the
  direction (audit right, witness stale, per the CODATA-2022 migration) and
  says to claim it separately: its producer runs >50 min for one bound atom
  before its own timeout. Not an idle-pass fix.
- **1 false positive in the padding audit**: `hardcoded-literal-audit.witness.json`
  `data.rows[349].hits[0].literal` is a literal that audit FOUND in source and
  recorded as evidence (`matches_constant: AME_B_TRITIUM_MEV_VALIDATION`). The
  detection is sound — it IS a double's expansion — but the padding audit
  cannot tell a quoted number from a computed one. Wants a declared
  quoted-evidence carve-out in the style of `precision_tier`, counted apart.
- 4 NEW `never_raises_dps` producers (31/6/3/2 constructions), 10 NEW q0-value
  drifts all at −0.0769 ppb (the CODATA-2022 anchor migration; scoped under
  `qou-3f7a` / `qou-tekx`), 3 raw-float64 regressions, 69 NEW unstamped.
