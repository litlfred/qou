---
# qou-zbws
title: 'NO-FLOAT64 hole: q_parameter raises the 50-dps floor ONLY on the muon anchor — every proton/default-anchor producer computes at mpmath''s 15'
status: todo
type: bug
created_at: 2026-09-02T21:53:12Z
updated_at: 2026-09-02T21:53:12Z
---

Found while fixing `qou-uiut` (the YSN braid defect). **Owner-facing**: the
fix is one line, but it changes the working precision of every producer on the
default anchor, so it is a numbers-move, not a refactor.

## Measured

    $ QOU_Q0_ANCHOR=<unset>  python3 -c "import hecke_core_legacy; ..."
        mp.dps after import : 15
        1/q                 : 0.900918283955741472368572431151   <- float64 tail
    $ QOU_Q0_ANCHOR=proton
        mp.dps after import : 15
        1/q                 : 0.900918283955741472368572431151
    $ QOU_Q0_ANCHOR=muon
        mp.dps after import : 50
        1/q                 : 0.900918273492422300050994867878   <- real 50 digits

`QOU_Q0_ANCHOR` is UNSET in this container, so 15 is the live default.

## Why

`computations/substrate/q_parameter.py:205`

    _mp.mp.dps = max(_mp.mp.dps, 50)

sits at 8-space indent — inside `if _anchor in ("ideal", "muon", "canonical"):`
(line 113). Its own comment states the directive as a GLOBAL one:

    > Owner directive 2026-07-06: "global dps 50 for compute accuracy". The
    > muon-anchored compute runs at a standing global precision of 50 dps —
    > this is the intended compute floor, NOT a temporary bump, so it is set
    > globally

but it is only set on that branch. On any other anchor the precision comes
from `qou_substrate/constants.py:316`:

    with _mp.workdps(_DPS_DEFAULT):
        Q_MP = q_at(_DPS_DEFAULT)
        ...

`workdps` RESTORES the ambient precision on exit — deliberately, and its
comment says so ("this module does NOT mutate the caller's mp.mp.dps"). So the
cached `_MP` VALUES are 50-digit mpf objects, but the ambient precision drops
back to mpmath's default 15 and every subsequent operation on them rounds to
~17 digits.

The two mechanisms are individually correct and jointly leave the floor unset.

## Why it matters

`hecke_core_legacy` was excised to mpf end to end under NO-FLOAT64 (bean
`qou-9ay6`) — `math` removed from the module entirely, `scipy.sparse` replaced
with a `_CooMPF` class written specifically because scipy refuses dtype object.
On the default anchor all of that arithmetic runs at 15 dps. The types say mpf;
the digits are float64. Nothing in the code shows it, and `repr()` displays at
the ambient dps, so a spot-check LOOKS right.

This is the same failure mode NO-FLOAT64 exists to prevent, one level up: not a
float64 value in an mpf pipeline, but an mpf pipeline evaluated at float64
precision.

Concretely measured on the `_M22_*` (2,2) constants (now fixed in `qou-uiut`
by deriving them lazily): frozen at import-time dps 15, they disagreed with
`_build_ysn_matrices` called later at 50 dps by **1.98e-17** — float64 epsilon,
inside the module the directive was applied to.

## The fix, and why it is not mine to land

Hoist the floor out of the anchor branch so it applies on every anchor. One
line. But:

- it raises the working precision of EVERY producer that imports
  `q_parameter` without setting its own dps, on the default anchor;
- so every witness those producers emit changes in its trailing digits;
- and the corpus's witness-equality ratchets will all go red at once.

That is the correct direction under NO-FLOAT64 and it is a corpus-wide
renumbering. Needs an owner call on sequencing, not a quiet commit.

## Scope to measure before landing

- [ ] Enumerate producers that import `q_parameter` and never set `mp.dps`
      (those are the ones whose numbers move).
- [ ] Producers that DO call `set_compute_dps()` are already at 50 and unaffected
      — count them, they are the safe majority or they are not.
- [ ] Decide whether the floor belongs in `q_parameter` or in
      `qou_substrate.constants` next to `_DPS_DEFAULT`.
