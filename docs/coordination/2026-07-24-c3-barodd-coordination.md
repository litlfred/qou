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

## Division of labour (agreed via intent comments)

- **#4140 (this branch):** the SUBSTRATE side — the odd-channel *determined solve*
  (Borel-sum the derived `d_k` at substrate to `~10⁻³⁹`), giving c₃'s bar-odd
  **magnitude**. In progress (agent relaunched 2026-07-24 after the prior run was
  lost to a session gap).
- **#3805:** the FIBRE side — A_ω as a derived integer (GGM 3d-index), giving the
  anchor **sign**. Their A_ω plugs into my `ResurgentPhaseFromAlienDatum`.
- Convergence: when both land, `c₃^odd = h·D(ũ)_substrate · sign(A_ω)`; cite both.

## Anti-double-derive note

Posted on #4146 asking any session on the odd-channel solve to flag. main
`ecdadf24` is block-level (bar-pair pole-swap), *not* the ladder Borel sum — no
collision. Intent comments: #3805 (comment 5071846047), #4146 (5071846549).

## Queued (not done this pass)

- Rebase #4140 onto post-`ecdadf24` main (3 commits; do at prepare-merge, not silently).
- Wire #3805's A_ω into `ResurgentPhaseFromAlienDatum` once it lands as a derived integer.
