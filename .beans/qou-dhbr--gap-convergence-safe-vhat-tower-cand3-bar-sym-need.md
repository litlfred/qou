---
# qou-dhbr
title: 'GAP: convergence_safe_vhat_tower cand3_bar_sym needs re-derivation under convention D'
status: todo
type: task
created_at: 2026-08-25T01:21:42Z
updated_at: 2026-08-25T01:21:42Z
---


## The site

`computations/convergence_safe_vhat_tower.py:198`

    z_bar = mp.mpf(1) / (mp.sqrt(qi) + mp.sqrt(q))  # = z (bar-symmetric)

Flagged actionable by `convention-c-producer-audit.py`; classed **B4** by
`convention-c-triage.py` (emits a committed witness). NOT migrated on
PR #5738, deliberately — it is a conclusion, not a definition.

## Why substitution is invalid here (rule 4 / qou-cds1)

The trailing comment is the whole problem. `z_C` **is** bar-symmetric,
as an identity:

    z_C(1/q) = 1/(sqrt(1/q) + sqrt(q)) = 1/(1/sqrt(q) + sqrt(q)) = z_C(q)

`z_D` is **not**:

    z_D(q)   = q^3/(q^2 + 1)
    z_D(1/q) = q^-3/(q^-2 + 1) = q^-1/(q^2 + 1)
    ratio    = q^4

Measured at the proton pin: `z_C(q) = z_C(1/q) = 0.49932033418369445`,
while `z_D(q) = 0.61268803714646525` and `z_D(1/q) = 0.40362773835082594`.

So `z_bar = z` is a **convention-C fact**, and the file has built a named
candidate on it: `cands["cand3_bar_sym"]` (line 275), with
`vhat_std_bar_image_q_to_qinv`, `F_on_bar_image`,
`bar_image_inside_radius` and `towers["cand3_bar_sym"]`
(`tower_bar_gm`, line 326) all downstream of it.

## Both available edits change recorded mathematics

- Write `z_bar = qi**3/(qi**2 + 1)` — the true bar image of `z_D`. Then
  `z_bar != z` and `cand3_bar_sym` is no longer the bar-**symmetric**
  candidate. Its identity changes; the name becomes wrong; whatever the
  candidate was evidence for is now evidence about a different object.
- Write `z_bar = q**3/(q**2 + 1)` — preserving `z_bar = z`. This keeps
  the C-era *structure* while carrying a D *value*, which is exactly the
  move `qou-cds1` bans and `QOU.QBeta.decayLadder_zC_threeRow_ne_zero`
  makes untenable in the adjacent case.

Neither is a mechanical convention fix. Someone has to decide what the
bar candidate **is** in the D frame, and that is authorial.

## What re-derivation has to settle

1. Is there a bar-symmetric object in the D frame at all? If the bar
   involution `q -> 1/q` no longer fixes the Markov parameter, does
   `cand3` survive in any form, or is it C-only and to be retired?
2. If it survives, is the right D object the bar image `z_D(1/q)`, or a
   symmetrised combination (`sqrt(z_D(q) z_D(1/q))`, which is
   `q/(q^2+1)` — rational, and worth checking against the Wenzl
   normalisation `z_W = q z_D`)?
3. Whatever is chosen, `bar_image_inside_radius` must be re-checked:
   `z_D(1/q) = 0.4036` and `z_D(q) = 0.6127` sit at different distances
   from the `Li_2^q` convergence radius `q`, so a candidate that
   converged under C may not.

## Blast radius

The file emits `convergence-safe-vhat-tower.witness.json`. It is ALSO
one of the 19 measured live consumers of `_li_2_q_util.load_q_50dps`,
whose `z` was migrated to D on PR #5738 — so this file already has a
D-frame `z` on line 178 sitting next to a C-frame `z_bar` on line 198.
That mixed state is itself a reason to prioritise this: the file
currently straddles the two conventions in one computation, which is
the shape AGENTS.md warns about for pins.

## Do not

Do not "fix" this by deleting the `# = z (bar-symmetric)` comment. The
comment is accurate about the code as written; it is the code that has
to move, once someone decides where to.
