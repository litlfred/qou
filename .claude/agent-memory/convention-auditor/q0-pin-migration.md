# q0-pin-migration — running the muon→proton re-pin

Detail split out of `MEMORY.md`, which is injected into the system prompt and
capped at 200 lines / 25 KB. Read this file **before touching the re-pin
sweep** (`qou-1c4y`) — its first attempt broke `main` for 208 producers.

## STABLE — the migration is authorised, with four bought constraints

Owner, 2026-08-15: *"we want proton unless for an explicit reason (like
comparison on proton vs muon results). otherwise pin proton"* / *"fix all,
even if not visible."* Scope: bean `qou-1c4y`. The first attempt broke
`main` for **208 producers** (`qou-m9xp`). The constraints:

1. **NEVER re-pin an anchor-DEFINING witness.** Re-pinning
   `q-pinning-50-digit.witness.json` redefines what "muon" *means* — 262
   `Q0_FLIP`s, and `q_parameter`'s guard then hard-fails every `ideal_muon`
   producer including the one that would regenerate the anchor.
   `q0_repin_sweep.py` excludes it by name; do not remove that.
2. **The muon anchor keeps its definition.** Something must still hold the
   muon 50-digit string or the ideal/CAL-2 layer becomes unstatable.
3. **A comparison producer needs BOTH pins**, via a per-process override,
   and belongs under `physical_proton`.
4. **Do not split the change.** The manifest reclassification and the
   witnesses it re-pins are one change. PR #5049 merged the witnesses and
   held the manifest; the half that landed is the half that broke `main`.

**Do NOT "migrate" by emptying `ideal_muon` in
`computations/q0_anchor_manifest.json`.** `q_parameter.py` selects by
membership, so an empty list means no producer ever resolves to the muon
anchor and the anti-corruption guard can never fire. It also relabels every
already-emitted muon witness as proton. The list does not end at zero:
several producers refuse a proton run *by design*
(`atomic_tr_m_mpfr_50dps`, `he4_stage2_ranking_seminormal_xcheck`,
`cross_check_trM_1ppb`), and `q_pinning_50_digit` defines the anchor.

