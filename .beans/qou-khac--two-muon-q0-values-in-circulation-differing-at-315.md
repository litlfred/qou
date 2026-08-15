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
