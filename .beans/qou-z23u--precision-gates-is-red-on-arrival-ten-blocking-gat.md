---
# qou-z23u
title: 'precision-gates is red on arrival: ten blocking gates, all inherited debt'
status: in-progress
type: task
priority: normal
created_at: 2026-09-03T15:43:09Z
updated_at: 2026-09-03T16:59:06Z
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


## Result: 10 blocking reds -> 8, and the two that went green were one root each

Measured with the full `scripts/precision-gates.sh` on this branch.

**Green: `float64-padding ratchet`.** 70 padded occurrences -> 12, NEW 58 -> 0,
exit 1 -> 0; everything left is under baseline and in `_deprecated`. Four
fixes, and only the first was cosmetic:

1. `tower_walk_magic_replication_probe` — 22 fields. Aggregated in mpmath
   "so float64 error does not compound", at `mp.dps` **15**, where an mpf sum
   accumulates exactly as a float sum. Then serialized with a bare `fmt`,
   default width **60**, on values sourced from `float(abs(np.trace(st)))`.
   The halves pull opposite ways — raising dps fixes the arithmetic and makes
   the serialization worse — which is why it sat in TWO gates at once.
2. `qbeta_three_nucleon_nf_alpha_spread_probe` — `mp.mpf("0.99839767")` is the
   RIGHT idiom, defeated by ORDERING: module scope, dps still 15, so the mpf
   held the 53-bit double; `main()` raised dps to 50 and `str()` printed that
   double out to fifty digits. The code looks correct on its own line.
3+4. `path_b_defect_binding_probe` / `path_b_habiro_mass_probe` — **not
   cosmetic**. `M_AME` was a MIXED dict (`"n"` mpf from the registry, five
   siblings bare floats) feeding a binding energy computed as ~1876 − ~1876 ≈
   1e-5 MeV. Catastrophic cancellation, measured at **2.525e-9 relative**, and
   the witness moved by exactly that: `B_AME_MeV`
   `0.000001270690003244…` -> `0.000001270689999999…`. The padding flag was a
   SYMPTOM of a real numerical defect, not fake precision over a right answer.

   Did NOT swap in the registry's `M_D_MEV_VALIDATION` though the producer
   already imports two registry constants: those are NUCLEAR masses
   (1875.61294500), these are ATOMIC (1876.12393). The tidy-up would have
   silently changed what is compared.

**Green: `import-time dps ratchet`** — fix (2) is one of its sites.

**`q0-anchor flip` still red, but honestly: 1, not 18.** The 17 unmappable
labels are gone (see above) and the remainder is `hadron-knot-table`, which
`qou-hah0` says to claim separately with a real compute budget.

The last padding NEW was a **false positive** and is now carved out:
`hardcoded-literal-audit.witness.json` records literals it FOUND in source as
evidence. The mechanism already existed and already held two other audits'
witnesses — only the name was wrong (`SELF_OUTPUTS` for a set that was never
just self-output). Renamed `QUOTED_EVIDENCE_WITNESSES`, kept a LIST rather than
a heuristic (a "looks like evidence" test is what would let real padding hide),
and it now reports itself by name, since an exclusion nobody can see is
indistinguishable from a hole.

### Still red (8), none touched by this work
`q0-anchor flip` (1, needs a compute budget) · `q0-anchor refill ratchet`
(owned by `qou-fl0a`) · `never-raises-dps` (3 NEW) · `raw-float64` (3 regressed)
· `q0-value drift` (10 NEW at −0.0769 ppb, scoped under `qou-3f7a`/`qou-tekx`)
· `CODATA stale-edition` · `mixed mpf/f64` (1 over baseline) · `witness
scriptFile provenance` (1 NOT_A_PRODUCER).
