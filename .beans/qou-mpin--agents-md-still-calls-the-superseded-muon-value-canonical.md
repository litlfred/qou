---
# qou-mpin
title: 'AGENTS.md still calls the SUPERSEDED muon value "the frozen canonical pin" — the anchor moved to CODATA 2022 by owner ruling on 2026-08-22'
status: todo
type: task
priority: high
created_at: 2026-08-29T12:05:00Z
updated_at: 2026-08-29T12:05:00Z
---

Found while establishing whether the `Q0_FLIP: 2` red in
`scripts/precision-gates.sh` was mine (it is not — see below). It nearly
misled me into "fixing" a witness that is correct.

## The finding

`qou_substrate.witness._q0_value_for_anchor("muon")` now returns

    1.109978595642739046681795129380001752700065561029011556974045769999095

read from `computations/q-pinning-50-digit.witness.json`. That is the
**CODATA-2022 lepton-tower derivation**. It was set deliberately by
`fca08de7d29` (2026-08-22): *"muon anchor -> CODATA 2022 (owner ruling):
derive it, stop the self-certification"*.

**AGENTS.md has not caught up.** Its §"q₀ anchor convention" and the
`muon_pin_three_values_probe.py` note still describe

    1.1099785955573347…

as *"the frozen canonical pin"*, and treat the CODATA-2022 value
(`…56427390…`) as one of the two *alternatives* to it. Those roles are now
reversed. Anything built on that labelling is affected:

- the **counting table** (871 / 477 at ten digits vs 468 / 149 at the full
  canonical literal) counts matches against the superseded literal, so
  "carries the muon fingerprint" now means something different again;
- the migration guidance's **rule 1** — *"NEVER re-pin an anchor-DEFINING
  witness"* — reads as an absolute, and the owner has since overridden it
  once, deliberately, with a derivation. The rule is still the right
  default; what is stale is that it does not record the exception, so an
  agent meeting the moved anchor concludes it is looking at the 2026-08-19
  regression rather than at an owner ruling.

## Why this is not a witness defect (the thing I nearly got wrong)

`hadron-knot-table.witness.json` carries `q0Value =
1.10997859555733471989…`, which is exactly the value AGENTS.md calls
canonical. Against the live anchor it reads as a **flip**. My first
reading was that the *audit's* expectation looked questionable, since it
disagreed with the documented canonical pin. That was backwards: the
audit is right and the document is stale.

The two live flips are the tail of an in-progress, owner-sanctioned drain
(`cfe73b8eb5f`, 2026-08-28, *"re-run the flip producers at the derived
anchor — Q0_FLIP 83 -> …"*), not new breakage:

| witness | anchor | q0Value | reading |
|---|---|---|---|
| `a-K-via-lp-dual-hecke-basis` | muon | `1.10997858275138…` | the **proton** pin under a muon label — a genuine straddle |
| `hadron-knot-table` | muon | `1.10997859555733…` | the **superseded** muon pin — awaiting the drain |

Neither is touched by any branch of mine. Last touched by `ce4eb6b3ba0`
and `bc8131bd58e` respectively, both other sessions.

## What to do

Not a code change. The decision is **which text in AGENTS.md to correct
and how far to go**, and it belongs to the owner because AGENTS.md is the
instruction file every agent reads:

1. **Minimal** — relabel: CODATA-2022 becomes the canonical muon pin,
   `…55573347…` becomes the superseded one. Cheap, no counts re-measured,
   leaves the counting table quoting a literal nobody should match on.
2. **Minimal + re-measure** — also re-run
   `muon_pin_three_values_probe.py` and replace the 871/477/468/149 table.
   Costs one probe run; makes the table mean what it says again.
3. **Also record the exception to rule 1** — one sentence noting the
   anchor-defining witness WAS re-pinned once, on 2026-08-22, by owner
   ruling, and that the prohibition is a default rather than an absolute.
   This is the one that prevents the specific misreading that produced
   this bean.

**Recommendation (judgement, not a finding): 1 + 3.** They are the two
that stop an agent drawing the wrong conclusion; the re-measure in 2 is
worth doing but is a separate, larger pass and nothing depends on it
today.

**Default if nothing is done:** nothing breaks. The anchor is correct, the
drain continues, and agents keep meeting a document that names the
superseded value canonical — which cost this session about twenty minutes
and one wrong intermediate conclusion.
