---
# qou-8p1h
title: 'qou-8p1x/h: Bruhat / GL_n(F_q) realisation of H_n(q) as a native route to PSL(2,7)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-colour
created_at: 2026-08-07T12:40:00Z
updated_at: 2026-10-10T13:49:32Z
parent: qou-8lxd
---

Parent: `qou-8p1x`. The strongest idea on the board, gated on `qou-8p1j`.

## The idea

`H_n(q)` is **by origin** the Iwahori–Hecke algebra of `GL_n(F_q)`: the
convolution algebra of `B`-bi-invariant functions, with basis indexed by the
Bruhat cells `G = union over w in W of BwB`. The framework already uses
`H_n(q)` as its core object, so this is not an import — it is that object's
defining realisation.

At `n = 3, q = 2` everything the colour section wants appears at once:

* complete flags: `sum over w in S_3 of 2^len(w) = 1+2+2+4+4+8 = 21`;
* point set of `PG(2,F_2)` = the **Fano plane**;
* `Aut = GL(3,F_2) = PSL(2,7)`, order `7 * 6 * 4 = 168`.

This would make the colour group **native rather than imported**, with the
complex **3** / **3bar** irreps of `PSL(2,7)` supplying the fibre — and it
would retire the octonion algebra from its current role as the section's
undefined sole foundation (`qou-8fl1`).

## Three honest problems

1. **`q = 2` is the whole ballgame.** The framework's `q` is a deformation
   parameter, and `q_0` is a *locally observed value that varies*. Jumping to
   `q = 2` because it yields `168` is textbook numerology absent a structural
   derivation. This is `qou-8p1j` and it is load-bearing: if it fails, this
   route collapses.
2. **`F_2^3` is not a `C`-fibre.** The bridge to a 3-dimensional fibre runs
   through the complex **3** of `PSL(2,7)`, which is rep theory one would have
   had anyway. So "native" is a claim about the *group*, weaker than it first
   sounds.
3. **The Hecke algebra is only the `B`-bi-invariant part.** Recovering
   `GL(3,F_2)` itself needs the building / the full induced representation, not
   `H_3(q)` alone.

## First concrete step

Do not start by computing. Start by asking whether the framework has any
structural reason to single out characteristic 2 (`qou-8p1j`). If it does not,
this route should be recorded as attractive-but-numerological and left alone.


---

## SUBSUMED FOR FLAVOUR (2026-08-07)

`qou-w5fw` / T3f already establishes that the Ocneanu parameter `a = q^{N-1}`
is free on the Hecke tower, so `N = 3` is reachable at the **same `q`** via
`a = q^2` — no characteristic-2 move needed. That is the better-formulated
version of this bean's instinct (get `N = 3` from the Hecke tower itself), and
it is already flagged in `qou-dwsh` §2c as the most promising direction.

**What survives here** is the genuinely different *colour* target: the Fano
plane as `PG(2,F_2)` with `Aut = GL(3,F_2) = PSL(2,7)`. That target really does
want `q = 2`, and so really does depend on `qou-8p1j`. Keep this bean scoped to
colour; do not use it to argue about flavour `N = 3`.


---

## 🛑 STALE CLAIM — `prop:color-su3-from-g2` does NOT have an empty `uses[]` (verified 2026-10-10)

This bean asserts the block carries no dependency edge. Measured on this branch at
`folio/.../braids-and-knots/color-su3-from-g2.ts:23`:

    uses: ["def:octonion-algebra"],

and the three comment lines immediately above it record the discharge explicitly:

    // def:octonion-algebra was authored 2026-08-29 (beans qou-7arp / qou-8fl1);
    // the NOTE that used to sit here, recording its absence, is discharged.
    // It sits immediately above this block in sec:color-algebra, so the edge
    // reads backward.

So the gap this bean names was **closed on 2026-08-29**. The same stale claim is
carried by `qou-8p1x`, `qou-8p1e` and `qou-8p1h`, i.e. three beans repeating one
fact that a fourth bean (`qou-8fl1`) had already fixed — the cross-bean staleness
pattern this front's epic (`qou-8lxd`) records: **read the beans a bean cites AND
the beans that cite it before working it.**

**A residual, and it is a different defect:** that comment says the edge *"reads
backward"* — `def:octonion-algebra` sits immediately above the block it is cited
from in `sec:color-algebra`. That is a forward-reference/ordering question for the
detangler arc, not an absent-edge question, and it is NOT what this bean claims.
Recorded, not filed: it changes a block's position, so it is an owner call.

Also verified: `qou-8p1x`'s route sub-beans **`qou-8p1i` and `qou-8p1j` are both
`scrapped`**, so any item here gated on either is gated on an abandoned route.
`qou-8p1h` in particular is blocked on nothing live.

Provenance: cross-session read-only pre-read of the 15 open `8f-colour` beans
(`/mnt/project-files/eightfold/8f-colour-preread.md`), confirmed on this branch at
`37bdbeef6b3` rather than taken on trust — the pre-read states its own path checks
were run partly against `main` at a different commit.

## Progress Note (2026-11-16)
- Formalized Bruhat / GL_3(F_2) = PSL(2,7) order 168 = 7*6*4, 7 Fano points + 7 lines = 14, and Bruhat length polynomial sum_{w in S_3} 2^{l(w)} = 21 complete flags in `QOU/Eightfold/BringThetaBruhatAndMesonH3.lean` (`bruhat_gl3_f2_psl27_and_fano_flag_certificate`) + 50-dps probe `bring_theta_bruhat_and_meson_h3_probe.py` (PR `litlfred/qou#8163`, head `bc5c91877bf9516be8cbcc8cd12c1a6501a5e983`).
