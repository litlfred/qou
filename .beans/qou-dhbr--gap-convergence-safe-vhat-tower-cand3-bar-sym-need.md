---
# qou-dhbr
title: 'convergence_safe_vhat_tower: z_bar RESOLVED on main; only the cand3_bar_sym NAME is stale'
status: todo
type: task
created_at: 2026-08-25T01:21:42Z
updated_at: 2026-08-25T06:40:00Z
---


## RESCOPED 2026-08-25 -- the substantive question is CLOSED, not open

This bean was written on PR #5738 while `computations/convergence_safe_vhat_tower.py:198`
still read

    z_bar = mp.mpf(1) / (mp.sqrt(qi) + mp.sqrt(q))  # = z (bar-symmetric)

and it argued that neither available edit was a mechanical migration,
so the choice was authorial. That was correct at the time.

**PR #5622 ("Excise convention C") then made the choice**, and it is on
`main`. The site is now line 207:

    z_bar = _markov_z(qi)

with a comment recording the verification: `markov_z(1/q) = z - h =
1/(q^3 + q) = 0.4036277383508259361649837` to 25 digits with difference
exactly 0.0, and `z/(z-h) = q^4` exactly -- so bar is not a symmetry of
`z_D`, it exchanges the channels. That is **option 1** of the two this
bean laid out (the true bar image), taken deliberately and documented.

**Do not re-open the z_bar question.** The analysis below is retained
because it is correct and agrees with main's, not because anything is
undecided.

## What actually remains -- the name, not the value

`cands["cand3_bar_sym"]` (line 284) and `towers["cand3_bar_sym"]`
(line 347) still carry `_bar_sym` in the name. Under convention D that
object is **not** bar-symmetric -- which is exactly what main's own
comment establishes. So the identifier now asserts a property its value
does not have, in a file whose comment three lines up explains why.

This is a naming defect, cheap and low-risk:

1. Rename to something that describes what it is under D -- the bar
   IMAGE candidate, not the bar-SYMMETRIC one (e.g. `cand3_bar_image`).
2. Grep for downstream readers of the key before renaming: it is a dict
   key, so any consumer indexes it by string.
3. Check `convergence-safe-vhat-tower.witness.json` -- the key is
   serialised into the payload, so a rename moves a committed field
   name and needs the witness regenerated in the same commit.

## Why the original bar-asymmetry argument still stands (retained)

`z_C` is bar-symmetric as an identity:

    z_C(1/q) = 1/(sqrt(1/q) + sqrt(q)) = 1/(1/sqrt(q) + sqrt(q)) = z_C(q)

`z_D` is not:

    z_D(q)   = q^3/(q^2 + 1)
    z_D(1/q) = q^-3/(q^-2 + 1) = q^-1/(q^2 + 1)
    ratio    = q^4

Measured at the proton pin: `z_C(q) = z_C(1/q) = 0.49932033418369445`,
while `z_D(q) = 0.61268803714646525` and `z_D(1/q) = 0.40362773835082594`.
Main's independently-recorded `0.4036277383508259361649837` agrees.

## Still worth checking when the rename lands

`bar_image_inside_radius`: `z_D(1/q) = 0.4036` and `z_D(q) = 0.6127` sit
at different distances from the `Li_2^q` convergence radius `q`, so a
candidate that converged under C may not under D. Main migrated the
value but this bean has not verified that the radius check was
re-examined.
