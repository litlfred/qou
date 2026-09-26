---
# qou-dhbr
title: 'convergence_safe_vhat_tower: z_bar RESOLVED on main; only the cand3_bar_sym NAME is stale'
status: completed
type: task
priority: normal
created_at: 2026-08-25T01:21:42Z
updated_at: 2026-08-25T07:37:29Z
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


---

## CORRECTED 2026-08-25 (PR #5750) — do NOT rename; the name is right and the CODE is wrong

This bean's rescoped remainder — "rename `cand3_bar_sym`, since under
convention D that object is not bar-symmetric" — is **withdrawn**. The premise
that the object is not bar-symmetric is correct; the diagnosis is not, and
acting on it would have enshrined a live bug as the intent.

Measured at q0 (70 dps, mpmath end to end):

    vhat_bar(q) - vhat(1/q)           = -0.18083
    gm(q)   = sqrt(|vhat|*|vhat_bar|) =  0.5561440948168445630758605
    gm(1/q)                           =  0.3111671166808308712169974
    gm(q) - gm(1/q)                   =  0.24498

So `gm` is indeed not bar-symmetric — this bean was right about that, and my
first hypothesis (that the geometric mean is symmetric by construction, so the
name is fine) was **refuted by measurement**. But the cause is not `z_D`.

Rebuilding the crossing chain with the **barred** `h` —
`nucleon_chains(quarks, qi - q)` instead of reusing the chain built from `+h` —
makes both differences **exactly 0.0**, with `gm = 0.27820062359787614354` at
`q` and at `1/q`. The chain's `(c, d)` entries carry `d = -h` for
`sigma^-1 = sigma - h`, built from the unbarred `h`, while the recurrence is
handed `qi - q = -h`; one evaluation therefore carries `h` at both signs.

**PR #5622 fixed only half the bar image.** `z_bar` was the Markov-parameter
half and that fix is correct and stands; the chain half was never barred.

Consequences:

- The name `cand3_bar_sym` is **accurate as intent** — the module header
  defines candidate 3 as "Bar-symmetrization (q to 1/q) of the argument", and
  the geometric-mean construction *is* exactly bar-symmetric on a correct bar
  image. Renaming it to `cand3_bar_image` would relabel the defect as the
  design, and would move a key serialised into the witness at three places.
- The blast radius, measured anyway: 4 sites in the producer, 3 in its own
  witness (which the producer regenerates), and one descriptive prose mention
  in `docs/audits/2026-06-01-vhat-tower-im-cancellation.md`. No registry, no
  content block, no Lean, no other script indexes the key. Small — but the
  right action is still not to rename.

The real defect is now tracked as **`qou-b7vr`**, which carries the numbers, the
one-line fix, and the reason it was not applied (it moves the committed
`+0.995 %` p/n signal that backs a recorded refutation of candidate 3).

Landed on PR #5750 instead: the convention-C `_std_vhat` docstring
(`z = 1/(q^{1/2}+q^{-1/2})`, stale since #5622 — docstring only, no number
affected) and a comment at the `z_bar` site recording all of the above.
