> **DEPRECATED on 2026-05-24.** Undated audit document classified as workplan / status snapshot / migration-handoff / one-off investigation whose findings have been integrated into main or whose plan has been executed. Original audit preserved here for historical record. See [`docs/audits/INDEX.md`](../INDEX.md) §"5-tranche recommendation" T5 for the deprecation rationale.

# Family-4 atom-knot ID via motivic substrate — audit + path

`#433` item B. Continues PR #433's deferred follow-up after the
`b-over-a-spectral-decomposition` framework was deprecated and
replaced by the motivic substrate / Habiro-Adelic chain in PR #455.

## Current state

### Family-4 atoms (no knot assignments on main)

`computations/mass-table-ppb.witness.json`
`atoms_no_assignment`:

| sym | Z | N | A | B_AME (MeV) |
|-----|---|---|---|-------------|
| ⁶Li | 3 | 3 | 6  |  31.99405 |
| ⁷Li | 3 | 4 | 7  |  39.24453 |
| ⁹Be | 4 | 5 | 9  |  58.16498 |
| ¹¹B | 5 | 6 | 11 |  76.20548 |
| ¹⁴N | 7 | 7 | 14 | 104.65877 |
| ¹⁹F | 9 | 10 | 19 | 147.80137 |

### What main already has

`computations/braid-registry/` has parent-braid
ground-state entries for every family-4 atom in the table above:

- `li-6.json` — parent ordering `[0,1,0,1,1,0]` via exhaustive
  ground-state search (`log_trace = −3.6339`, n_orderings_searched = 20).
- `li-7.json` — analogous entry for ⁷Li.
- `be-9.json` — registry entry present for ⁹Be.
- `b-11.json` — registry entry present for ¹¹B.
- `n-14.json` — registry entry present for ¹⁴N.
- `f-19.json` — registry entry present for ¹⁹F.

Each provides a candidate ground-state braid, but **no `knot_id`** —
the registry stops at "we found the lowest-trace ordering" and does not
match the resulting braid against a knot-type table.

### What deprecated approach did (volume-match census)

PR #433's original plan: extend `mass-table-ppb` to ⁶Li/⁷Li via
volume-match search against a hp_volume@50dps knot table. Quarantined in
`dc5027e` ("deprecate volume-match atom-knot search; quarantine ⁶Li/⁷Li").
Reason: volume-matching against an empirical knot census conflates
geometric volume coincidence with structural knot identity.

## Motivic-substrate path (post-PR #455)

The Habiro-Adelic framework introduced in PR #455 reframes the substrate
as motivic (`def:motivic-substrate` in
`content/quantum-observable-universe/.../motivic-substrate.{ts,md,lean}`).
The chain to atom-knot ID becomes:

1. **Ground-state braid** — already in `braid-registry/li-{6,7}.json`.
2. **q-Markov trace** — compute `tr_M(T_w)` for the parent braid via the
   q-MN canonical wrapper (`mn_chi_q`, see
   `categorical-vs-fitted-q-decay-ba.md` §"Plancherel-vs-Wenzl-Schur
   Markov-trace bug" for the convention pinning).
3. **Motivic-Galois action** — apply the motivic-perpetual-obstruction
   endomorphism (cf. `chi-minus-six-chain motivic-Galois Step 8`,
   commit `8ff85968`) to identify the Galois orbit of the braid.
4. **Knot-class identification** — the orbit is a finite set of knot
   types in `K_motivic`; the braid's `tr_M(T_w)` matches at most one
   member up to `q_0`-precision floor.

Each step has a corresponding script / Lean class on main; what's
missing is the **glue script** that walks the chain end-to-end for the
six family-4 atoms.

## Concrete blockers (numbered, ranked)

1. **q-MN convention pin** — the Plancherel-vs-Wenzl-Schur Markov-trace
   bug surfaced in the #447 audit (sibling doc
   `docs/audits/categorical-vs-fitted-q-decay-ba.md`, landing in
   [PR #469](https://github.com/litlfred/qou/pull/469); not yet on `main`)
   blocks step 2 from emitting consistent values across scripts.
   Fix lands in #447 territory, not here.
2. **Motivic-Galois endomorphism** — main has the *axiomatic* class
   (`MotivicSubstrate`, `HabiroCompletion`) and downstream conditional
   theorems, but no concrete realization computing the action on a
   given parent braid. This is the principal gap.
3. **Knot-class table in `K_motivic`** — the post-#455 chain replaces
   the volume-match census with a motivic-Galois-orbit table; the table
   covering the family-4 atoms (up to ¹⁹F) is not yet generated.
   Here the current `f-19.json` braid-registry entry has parent ordering
   length $19$, i.e.\ a $19$-strand braid, so there are $19 - 1 = 18$
   Artin generators per the Skein product
   $P_N(q) = \prod_{i=0}^{A-2} \hat V_i(q)$.
   This parent-ordering length is not the same as braid-word length:
   word lengths for a ground-state braid can be larger than the
   generator count — up to $\binom{A}{2}$ in the worst case — so the
   table must be sized against the longest expected word, not against
   the strand count or a fixed word-length cutoff.

## Smallest defensible deliverable today

A scaffold script `family_4_motivic_probe.py` that, for each of
{⁶Li, ⁷Li, ⁹Be, ¹¹B, ¹⁴N, ¹⁹F}:

- loads the `braid-registry/<sym>.json` parent ordering (where it exists)
- records a q-MN character placeholder (`pending-convention-pin`)
  until the q-MN convention is pinned to the canonical Markov-trace
  conventions; the actual trace computation is blocker #2
- emits a witness JSON with status `motivic-pending-orbit-table`
  for each atom

This deliverable does **not** assign knot IDs (cannot, without the
orbit table). It documents the categorical state honestly so the
next agent picking this up has a concrete starting point.

## Out of scope

- Computing the motivic-Galois action concretely (blocker #2).
- Generating the `K_motivic` orbit table (blocker #3).
- Closing the family-4 row in `mass-table-ppb` (requires both blockers
  to land, plus the ⁶Li/⁷Li knot ID to flow through).

## References

- PR #455 (motivic-perpetual-obstruction reframing, merged `7955c65`)
- `dc5027e` (volume-match deprecation)
- `docs/audits/categorical-vs-fitted-q-decay-ba.md` (companion audit;
  landing in [PR #469](https://github.com/litlfred/qou/pull/469), not
  yet on `main`)
- `def:motivic-substrate`,
  `prop:motivic-perpetual-obstruction` (content blocks on main)
