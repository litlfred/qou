#!/usr/bin/env python3
"""Guard: the H_3 transition cache must be keyed on `q` (bean `qou-h3qk`).

WHY THIS EXISTS
---------------
`reduced_block_kernel.get_h3_transitions(ab0, ab1, ab2, q, qi, shape_in, c_in, Dc)`
computes with `q` -- `hq = q - qi`, and `D(delta) = hq / (1 - q**(-2*delta))` --
but until 2026-09-04 its module-level cache keyed only on

    (ab0, ab1, ab2, shape_in, c_in)

so a second `q` reaching an entry already populated by a first `q` silently
received the FIRST `q`'s amplitudes. No raise, no warning.

The `ab` tuples are themselves functions of `q`, so most pairs of `q` differ in
the key and miss correctly. That is what made this survivable in practice and
also what makes it a poor thing to rely on: `_H3_TRANSITION_CACHE` is a MODULE
-level dict living for the whole interpreter and shared across unrelated
callers, so a collision is a property of the process, not of any one caller.

This audit does not wait for a natural collision. It FORCES one -- calling
`get_h3_transitions` twice with identical `(ab, shape, c)` and different `q` --
which is exactly the state the old key could not distinguish.

WHAT THIS ASSERTS
-----------------
1. A forced collision returns DIFFERENT amplitudes for different `q`, and each
   equals what the same `q` gives on a cold cache. This fails on the old key.
2. Working precision is part of the identity too: the same `q` at 50 and at 90
   dps must not serve one block for the other.
3. Production is unmoved -- the atom traces at q0 are what they were.

NO FLOAT64: all arithmetic is mpmath.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import _path_bridge  # noqa: F401, E402
import mpmath as mp  # noqa: E402

import reduced_block_kernel as RBK  # noqa: E402
from reduced_block_kernel import get_h3_transitions  # noqa: E402
from tr_m_atom_via_transfer import tr_m_atom_zn  # noqa: E402

#: Regression baseline for check (3), "production unmoved". CANONICAL
#: (borromean) as of 2026-09-13.
#:
#: ⚠ THESE MOVED, AND THE MOVE WAS CORRECT. Until 2026-09-13 this table held
#: the GROUPED-era values
#:
#:     D 0.575172243917771870826535343986   T 0.229310102104556507332090810269
#:   3He 0.403767036851428170368670253333  4He 0.160974145442407381825873440981
#:
#: so check (3) had been failing on all four atoms since the 2026-09-05
#: intra-nucleon ordering ruling (bean `qou-hu1f`) made the borromean word
#: canonical. Nothing this audit actually audits was broken: checks (1) and
#: (2), the cache-key and dps-key tests that are its subject, passed
#: throughout. It was a stale reference guarding against a change that had
#: already been ruled correct — a standing red, which is a gate someone
#: eventually silences.
#:
#: NOT ASSUMED — MEASURED. Found by the source-literal arm of
#: `intra_ordering_value_fingerprint_audit.py`, which matched the 3He entry to
#: the grouped helium-3 fingerprint at 15 significant digits. Then confirmed
#: by recomputing `tr_m_atom_zn` with `atom_braid_word_3A` forced to each
#: ordering: **all four old values reproduce exactly under `grouped`, and all
#: four new ones under `borromean`.** So the baseline was the old frame and the
#: code is in the new one, rather than the reverse.
_PRODUCTION = {
    "D":   ("0.151968339204231607592665697751", "0.299015017184640076702160426771"),
    "T":   ("0.0291440423609720653572542187919", "0.142072056797304797470498604255"),
    "3He": ("0.0585962536544363802189567154521", "0.188178642999488779263479037146"),
    "4He": ("0.0112374176597674215641995493744", "0.0894099805019306003820475658199"),
}
_ZN = {"D": (1, 1), "T": (1, 2), "3He": (2, 1), "4He": (2, 2)}

# One fixed (ab0, ab1, ab2, shape_in, c_in) reused at two different `q`. The
# ab tuples are held FIXED on purpose: in the wild they would move with `q`
# and the keys would differ, which is the accident that hid this defect.
_AB = ((1, 0), (1, 0), (1, 0))
_SHAPE_IN, _C_IN = (2, 1), 1


def _call(q):
    return get_h3_transitions(*_AB, q, 1 / q, _SHAPE_IN, _C_IN, {})


def _same(a, b):
    return set(a) == set(b) and all(a[k] == b[k] for k in a)


def main() -> int:
    mp.mp.dps = 50
    fails = []
    qA, qB = mp.mpf("1.11"), mp.mpf("1.9")

    # (1) forced collision: two q, one cache.
    RBK._H3_TRANSITION_CACHE.clear()
    warm_A = _call(qA)
    warm_B = _call(qB)                      # same key under the OLD scheme
    RBK._H3_TRANSITION_CACHE.clear()
    cold_B = _call(qB)
    RBK._H3_TRANSITION_CACHE.clear()
    cold_A = _call(qA)

    print("forced key collision, q_A = 1.11 then q_B = 1.9 on one cache:")
    print(f"  warm(q_B) == warm(q_A)  : {_same(warm_B, warm_A)}   (want False)")
    print(f"  warm(q_B) == cold(q_B)  : {_same(warm_B, cold_B)}   (want True)")
    print(f"  warm(q_A) == cold(q_A)  : {_same(warm_A, cold_A)}   (want True)")
    if _same(warm_B, warm_A):
        fails.append("q_B received q_A's amplitudes — `q` is not in the cache key")
    if not _same(warm_B, cold_B):
        fails.append("warm q_B differs from cold q_B — the cache is serving something else")
    if not _same(warm_A, cold_A):
        fails.append("warm q_A differs from cold q_A")

    # (2) precision is part of the identity.
    RBK._H3_TRANSITION_CACHE.clear()
    mp.mp.dps = 50
    at50 = _call(mp.mpf("1.11"))
    mp.mp.dps = 90
    at90 = _call(mp.mpf("1.11"))            # must NOT be served the 50-dps block
    n50 = {k: mp.nstr(v, 60) for k, v in at50.items()}
    n90 = {k: mp.nstr(v, 60) for k, v in at90.items()}
    served_stale = (set(n50) == set(n90) and all(n50[k] == n90[k] for k in n50))
    print(f"\nsame q at 50 vs 90 dps: 90-dps block is byte-identical to the "
          f"50-dps one: {served_stale}   (want False)")
    if served_stale:
        fails.append("a 90-dps call was served the 50-dps block — dps is not in the key")

    # (3) production unmoved.
    mp.mp.dps = 50
    RBK._H3_TRANSITION_CACHE.clear()
    print("\nproduction q0 (default pin, default dps):")
    for name, (a_want, f_want) in _PRODUCTION.items():
        Z, N = _ZN[name]
        ta, tf, _, _ = tr_m_atom_zn(Z, N)
        a_got, f_got = mp.nstr(ta, 30), mp.nstr(tf, 30)
        ok = (a_got == a_want and f_got == f_want)
        print(f"  {name:>4}  {'OK ' if ok else 'MOVED'}  atom={a_got}  free={f_got}")
        if not ok:
            fails.append(f"{name}: atom {a_got} != {a_want} or free {f_got} != {f_want}")

    print()
    if fails:
        for f in fails:
            print(f"  FAIL  {f}")
        return 1
    print("PASS — cache keyed on q and dps; production unchanged.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
