---
# qou-khac
title: Two muon q0 values in circulation, differing at 3.15e-12
status: todo
type: task
created_at: 2026-08-15T21:19:10Z
updated_at: 2026-08-15T21:19:10Z
---


## What

Found while resolving `inter_nucleon_linked_channel`'s q0 (`qou-2ixd`, owner
ruled proton). Scanning every hand-typed `1.10997858…`/`1.10997859…` literal in
`computations/` turned up **18 that match neither canonical pin exactly**. Most
are harmless truncations (1e-16 to 1e-21 — simply fewer digits). Three are not:

| file | literal | \|d\| from muon-canonical |
|---|---|---|
| `gap_a3_overshoot_robustness_check.py` | `1.1099785955541805` | 3.15e-12 |
| `per_basis_row_invariants_probe.py` | `1.1099785955541805752815940796` | 3.15e-12 |
| `probes/flavor_split_alpha_dilog_expansion_probe.py` | `1.1099785955541810` | 3.15e-12 |

They are not truncations. They are a **second muon value**:

    muon-canonical (corpus, Q_MUON)  1.10997859555733471989976322048...
    muon variant   (these 3 files)   1.10997859555418057528159407961...
                                     |d| = 3.15e-12   rel = 2.84e-12

3.15e-12 is far above a rounding difference and far below anything a reader
would notice. The variant is the value recorded elsewhere in this session's
notes as `Vol(4_1)/(m_mu/m_e)`, so both plausibly have derivations — which is
exactly why this needs a ruling rather than a guess.

## Why it matters

The `inter_nucleon_linked_channel` case is the precedent. Its pin was wrong by
1.16e-8 and everything still *looked* right: assertions passed, values were
plausible. What exposed it was that `W_(1,1)` disagreed with the registry's own
`y_(2,1)` at digit 9 — and after the correction they agreed to 22. A near-miss
pin does not fail; it quietly shifts every derived number.

At 3.15e-12 these three would shift results in the 12th figure, which is above
the 1e-40 tolerances the trace gates now use and below the precision most
assertions check.

## Next

1. **Owner ruling: which muon value is canonical?** If `Q_MUON` is, the three
   files should import it; if the variant has a derivation, it needs a registry
   entry naming it, like the proton/muon split already has.
2. Once ruled, take it **by import** rather than retyping — the lesson from
   `qou-2ixd`: a literal cannot drift from a source it does not have.
3. The other 15 near-misses are truncations of a correct pin. Worth converting
   to imports on the same principle, but they are not wrong today.

---

## CORRECTION: not two competing canonicals — a stale pin kept as a control

Owner ruling 2026-08-15: **proton is canonical.** That was never in question and
my framing of this bean was wrong. There is no contest between two muon
"canonicals" needing adjudication. What is actually in the corpus:

| | value | role |
|---|---|---|
| canonical | `1.1099785827513808075916690956107688798744991218736` | **the** pin (registry, AGENTS.md 2026-08-07) |
| muon-current | `1.10997859555733471989976322048322502665620840878…` | `Q_MUON`, the documented muon anchor |
| muon-stale | `1.10997859555418057528159407960950937799328227995870` | a **superseded** muon value, deliberately retained |

The third is not a rival canonical. Two of the three files carrying it say so
in the source:

* `per_basis_row_invariants_probe.py:67` names the variable
  **`Q0_STALE_MUON_PIN`**, and its docstring describes "a q₀-STABILITY test
  across canonical (m_p-pin) and stale (muon-pin)" — the stale value is the
  *control*, and the point of the probe is that results do not depend on it.
* `probes/flavor_split_alpha_dilog_expansion_probe.py:51` has `_muon_q0()` and
  states "anchor-stable (proton-q₀ vs muon-q₀ drift 5.8e-8)".

That is the same pattern as convention C being kept quotable for labelled
comparison: a superseded value retained on purpose, and named as superseded.
Nothing to rule on.

## The one real defect

`computations/gap_a3_overshoot_robustness_check.py:35`

    Q0 = mp.mpf("1.1099785955541805")

is the **stale muon pin, unlabelled, as the file's only q₀** — no `_muon_q0()`,
no `STALE` in the name, no mention of muon anywhere in the module. Its docstring
meanwhile calls its inputs "the canonical inputs" and "the pinned q₀". It also
truncates: `…5541805` against the full `…55418057528159…`.

So the two files that use the stale pin *as a control* are fine, and the one
that uses it *as the pin* does not know it is doing so.

Its `Q0` is live — it feeds `q_int(m)` and an `(q^{1/2}+q^{-1/2})^{4N}` factor —
so this is not cosmetic. (That half-argument factor is a legitimate `[2]_{√q}`
q-integer, correctly not flagged by the producer audit; it is not a `z`.)

**Not changed here.** The module also carries `TRM` values cached "from the
#2635 canonical run", and switching `Q0` without establishing which pin those
were computed at would trade one inconsistency for another. That needs whoever
owns #2635, not a guess from me.

## Next

1. `gap_a3_overshoot_robustness_check.py` → proton pin by import, once the
   cached `TRM` provenance is established.
2. The other two need nothing.
3. Worth considering: the stale pin should live in one named constant that the
   control probes import, rather than being retyped (twice at full precision,
   once truncated, once as `1.1099785955541810` — four spellings of one
   superseded value).
