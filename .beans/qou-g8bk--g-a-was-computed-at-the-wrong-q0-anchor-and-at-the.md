---
# qou-g8bk
title: g_A was computed at the wrong q0 anchor, and at the right one the LP degenerates
status: todo
type: task
created_at: 2026-08-23T22:43:45Z
updated_at: 2026-08-23T22:43:45Z
---

## Two findings, and the second is the one that needs an owner

### 1. The witness was stamped `muon` while computing at the `proton` value

`borromean-axial-coupling.witness.json` at HEAD declared

    q0Anchor: "muon"
    q0Value:  1.10997859555733471989976322048322502665620840878015368

while its own data recorded

    observable_vector.char_on_basis[1] = 1.1099785827513808     <- the PROTON pin

`q0_anchor_manifest.json` lists `borromean-axial-coupling` under `ideal_muon`
(110 entries), so the manifest agrees with the stamp. `q_parameter`'s
auto-select now applies it, and a regeneration moves the computed value to
1.1099785955573347 — the muon pin. **This is the first time this witness's
numbers and its own declared pin agree.**

That is bean `tnjb`'s exact hazard — a muon value read as a proton one, with a
provenance field vouching for it — caught in the act, on the correcting side.
The two assertion flips are therefore NOT a regression to revert:

    g_A                  HEAD 1.0                   ->  0.5797873108533357
                         (expected 1.2754, tol 0.5)
    lp_duality_gap_zero  HEAD 3.821440179968053e-16 ->  0.020884511792466608
                         (tol 1e-10)

### 2. At the anchor it declares, the LP does not close — and that is the finding

The corrected result does not stand up. The operator-selection LP degenerates
rather than solving:

    active_basis_names   ['γ']              ->  ['γ', 'σ₀', 'σ₁']
    x_star[0]            -265025.0078…      ->  -1000000.0      <- EXACTLY the box bound
    duality_gap          3.8e-16            ->  0.0209
    primal / dual obj    ~1e-16 / -7e-19    ->  0.02088 / 5.2e-08

`x_star` pinned at a round −1,000,000 is a variable sitting on its bound. The
0.0209 duality gap is therefore a **degenerate LP, not a physical answer**.

So the honest statement is:

> **g_A = 1.0 was obtained at the wrong anchor, and at the declared muon anchor
> the operator-selection LP does not close at all. Neither the old 1.0 nor the
> new 0.58 is a result.**

## The decision needed

Which is true:

  (a) this producer is **physical-layer and mis-tagged** in
      `q0_anchor_manifest.json` — it should be under the proton pin, the old
      LP was solving the right problem, and the manifest entry is the bug; or

  (b) it is **ideal-layer, correctly tagged**, and the LP is genuinely
      infeasible/degenerate at the muon anchor — in which case g_A has no
      value from this route and the producer's claim needs withdrawing or
      re-deriving.

The evidence does not settle it: the manifest and the witness's own stamp both
say muon, which favours (b); but a clean 3.8e-16 duality gap at the proton
value is not what an accidentally-right anchor usually looks like, which
favours (a).

## Do not

- **Do not revert.** The old numbers were computed at an anchor the witness
  itself disclaims.
- **Do not widen the 1e-10 `lp_duality_gap_zero` tolerance.** A gap of 0.0209
  with a variable on its box bound is not a tolerance question.
- **Do not re-stamp the witness to `proton` to make it consistent** without
  deciding (a) vs (b) first — that is the same class of move as editing a
  witness to look fresh.

Found during the self-staleness drain on
`claude/mass-table-comprehensive-triage`; the two flips are recorded in
qou-60r9 and point here.
