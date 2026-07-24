# Coordination: c₃ bar-odd / qbeta φ_odd fibre resummation (2026-07-24)

**Home PR:** #4140 (`claude/argument-principle-residue-sum-2026-07-20`) ·
**Session review after ~4-day gap.** Coordination only — no new results.

## Scope map

| PR / ref | Relationship to #4140's c₃ bar-odd work | Class |
|---|---|---|
| **#3805** — A_ω via GGM 3d-index of 4₁ | My fork isolates c₃'s open piece to the **fibre-branch Δ_ω phase = their integer A_ω**. Direct dependency; they supply the sign I need. | overlap + dependency |
| **#4127** — octahedral 4-dilog μ₀ resurgence | Same alien-derivative / Stokes machinery (μ₀ = 1 tetrahedron of 4); resurgence face | overlap |
| **#4146** — week-review workplan | Lists "qbeta φ_odd fibre bar-odd resummation (2c-2 obstructed at bar-pair)" as frontier #4 = my active work | coordination hub |
| **#4142** — binding/mass workplan | "Q_β value leg measurement-limited" — consistent with my L2 finding | coordination |
| main `ecdadf24` — qbeta-g3 bar-pair pole-swap (2c-2 obstruction) | Parallel-confirms the bar-pair obstruction from the block-level side | main-watch |

## Established on #4140 (2026-07-20, fork resolution)

- c₃ bar-odd part `S = c₃ + Vol(4₁) = h·D(ũ)`; `d_k ∈ ℚ(√3)` **derived** from the
  symbolic GB-reduced net decay-width (determined triangular solve, no CODATA fit).
- Fork `|S| = |(q;q)_3|` exact-vs-resurgent → **resurgent**: `|S|_geom = 0.00945 =
  |(q;q)_3|·1.0074`; `D(ũ)` divergent (radius→0, KC22 holds).
- Lean `QOU.Mass.QbetaC3PochhammerPhase` (sorry-free): `S = (q;q)_3 · phase`, phase
  bar-even via the `h`-factorization; open residual `ResurgentPhaseFromAlienDatum`
  (no instance) = the fibre Δ_ω phase.

## Division of labour — CORRECTED 2026-07-24

> **⛔ The original "substrate magnitude / fibre sign" split below was WRONG.**
> The substrate Borel sum is an anchor-blind floor (`h·D_opt ≈ −0.0035`) that does
> NOT reproduce `S` (`−0.0395`/`+0.0097`) — magnitude included (Écalle witness M4;
> `docs/audits/2026-07-24-c3-barodd-fork-correction.md`). So `#4140` does **not**
> own a derived magnitude.

- **The dominant anchor-dependent `c₃^odd` is open in BOTH magnitude and sign**, via
  either the `1/ũ³` representational amplification (#3636) or the fibre `A_ω`
  (#3805) — neither derived. The odd-channel substrate Borel-sum route is a
  **known negative** (do not re-run; cite the Écalle witness).
- **#3805's `A_ω`** remains the most promising handle for the fibre-saddle branch,
  but it supplies the *whole* anchor-dependent object there, not merely a sign on an
  already-derived magnitude.
- Correction comments posted on #3805 + #4146 withdrawing the "magnitude derived"
  claim.

### Original (withdrawn) split
- ~~#4140 owns the substrate magnitude; #3805 owns the sign; `c₃^odd =
  h·D(ũ)_substrate · sign(A_ω)`.~~ — withdrawn per M4.

## Anti-double-derive note

Posted on #4146 asking any session on the odd-channel solve to flag. main
`ecdadf24` is block-level (bar-pair pole-swap), *not* the ladder Borel sum — no
collision. Intent comments: #3805 (comment 5071846047), #4146 (5071846549).

## Queued (not done this pass)

- Rebase #4140 onto post-`ecdadf24` main (3 commits; do at prepare-merge, not silently).
- Wire #3805's A_ω into `ResurgentPhaseFromAlienDatum` once it lands as a derived integer.
