---
# qou-rw91
title: 'PRECISION: 3 witnesses landed with no q0Anchor (Q0_ANCHOR_MISSING 1882 -> 1885)'
status: completed
type: task
priority: normal
created_at: 2026-08-15T10:57:22Z
updated_at: 2026-08-19T15:51:48Z
parent: qou-pq8k
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

Claimed 2026-08-15 by claude/agent-discussions-queue-gibk4e (session qou-pq8k). Dispatched to a background agent; work lands in a worktree and is integrated onto the session branch by the parent.

## RESOLVED 2026-08-15

**The third witness, read off the list rather than guessed.** `afff724830` no
longer exists (rewritten by the "second rebase"); the same regeneration is
`965a7ceec5` on `claude/agent-discussions-queue-gibk4e`. Diffing its
`Q0_ANCHOR_MISSING` name list against its predecessor gives exactly three
additions:

- `qbeta-ohtsuki-nz-bridge-b4.witness.json`
- `qns-phase-decorrelation-probe.witness.json`
- `qns-phase-scramble-probe.witness.json`   ← the third

**All three are genuinely q₀-free** (verified per producer by import cone).
The two `qns_phase_*` probes' `q = 1.0 + eps` is the Sabra/DN shell-spacing
ratio, not the substrate modulus — `eps = 1e-1` lands on 1.1, next to
q₀ ≈ 1.10998, which is coincidence and the reason to say so explicitly. The
qbeta b4 probe is π, √3, the exact Ohtsuki rungs and the 4₁ geometry; its one
non-trivial import (`probes/sdeformed_channel_signflip_probe.py`) imports only
json/subprocess/datetime/pathlib/mpmath, so `y_lambda_at`'s muon-cache straddle
is unreachable.

**The bean's instruction could not be followed as written, because the
vocabulary had no true value to record.** `proton` would assert the standing
default on numbers that never touched q₀ — the misrecord this field exists to
prevent. `ambiguous` means the opposite (`gen_q0_anchor_manifest.py:60`: BOTH
pins present, queued for a manual ruling). So the gap was in the vocabulary,
not the producers.

Added `q0Anchor: "independent"` + verdict `Q0_INDEPENDENT`. Producer-declared
only — the manifest generator already sees this class and drops it
(`# neither: no q₀ field — omit`), and inferring independence from "records no
q₀ value" would mint false layer-freedom claims, since a producer can use q₀
without serializing it.

  Q0_ANCHOR_MISSING  1889 -> 1886      (worktree baseline, not the bean's 1885 —
  Q0_INDEPENDENT        0 -> 3          7377d6624 added four more after filing)
  Q0_FLIP               0    unchanged

Each producer re-run, not hand-edited; all three exit 0 with byte-identical
numeric payloads.

Commits: `b4b293fc` (audit vocabulary) · `e6cc6ac5` (witness.py + 3 tests) ·
`aec323d3` (producers + witnesses) · `eb384e92` (audit witnesses).

**Carried forward.** `qou-pin1` hit this same wall on `chi-deuteron-h6`
(purely symbolic), settled for "manifest `ambiguous`, drop the stamp", and that
witness is still unstamped — it is now expressible as `independent`. The four
witnesses `7377d6624` added remain missing; `qbeta-ohtsuki-nz-bridge-b6` is the
b4 sibling and the obvious next one.

## Closed 2026-08-19 — resolved, partly by others (PR #5312)

All three named witnesses now read `q0Anchor: "independent"` on main.

**The bean's premise did not hold for these three.** It said "Fix at each
producer by recording the anchor" — but tracing all three producers shows
none of them reads a q₀ at all:

- `qns-phase-scramble-probe` / `qns-phase-decorrelation-probe` — Sabra
  shell-model turbulence integrators. Imports are `cmath`, `math`, `sys`,
  `time`, `WitnessBuilder`, `_precision.fmt`. No substrate parameter
  anywhere.
- `qbeta-ohtsuki-nz-bridge-b4` — extracts Taylor coefficients in a free
  small parameter `u` against the proved constant `A2 = i√3/4`, via
  `sdeformed_channel_signflip_probe.V41_integrated`, which is itself
  q₀-free. Never evaluated at a pin.

Stamping `"proton"` on any of them would have asserted a pin the compute
never used — false provenance, which is the opposite of what the rule
protects. The right answer was a third token, and the audit has since
grown exactly that (`Q0_INDEPENDENT`, requiring a `q0AnchorReason`).
I reached this independently before finding it already built; recording
the reasoning because the bean text still points the wrong way.

**Residue I did fix** (PR #5312): two witnesses claimed `independent`
with no reason — `markov-identity-symbolic` (reason in the producer, but
the committed witness predated it) and `qbeta-d-frame-markov-weights`
(reason present only as a source comment — the `qou-mw1p` shape, missed
by its drain). `Q0_INDEPENDENT_NO_REASON` 2 → 0.

Also corrected `markov-identity-symbolic`'s reason, which opened "No q0
is read" while its own producer hardcodes both pins as sample points.
Verdict right, justification wrong; found by exactly the grep the reason
was supposed to make unnecessary.

**Not closed by this:** `Q0_ANCHOR_MISSING` is 1904 and rising. That is
the pre-backfill population, not a failure (the strict gate fires only on
`Q0_FLIP`, which is 0), and draining it is a separate, much larger job.
