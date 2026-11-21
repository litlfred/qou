#!/usr/bin/env python3
"""The axial observable IS the Gram radical — its pairing is canonical only in a ratio.

`borromean-axial-coupling.py` dies with `KeyError: 'gram_inverse'` because
`be59f01376` removed that key: under convention D the Markov-Gram on the H_3
NF basis is SINGULAR (rank 5, radical = the sign representation), so no `G^-1`
exists to emit. Bean `qou-cnbm` framed the fix as a choice between two readings
of the consumer's `G^{-1}|_{A*}` -- restrict-the-inverse vs invert-the-
restriction.

Measured, the choice does not arise, because the question is upstream of it.

The producer forms two observables from characters on the NF basis:

    O_V  trivial rep,  <O_V, b_j> = q^len(b_j)
    O_A  sign rep,     <O_A, b_j> = (-1/q)^len(b_j)

and dualises each against the Gram. `be59f01376` states the constraint that
decides them: "Dualising against a degenerate form is well-defined only for
vectors orthogonal to the radical, because generalized inverses differ
precisely by radical terms."

So the deciding test is each observable's overlap with the radical, and it
separates them completely (50 dps, exact route via `pyhecke.gram`):

    O_V   |cos to radical| = 2.95e-51     orthogonal to the arithmetic floor
    O_A   |cos to radical| = 1.0          IS the radical, exactly

That is not a near-miss to interpret. The radical is the sign representation
(`gram-matrix-dual.witness.json::radical_is_sign_representation = true`) and
`O_A` is the sign character, so the two coincide by construction.

CONSEQUENCE -- and the limit of it. Taken ALONE, the axial pairing has no
canonical value: it asks for the dual of a vector the form annihilates, and
generalized inverses differ by exactly the radical term. The trivial channel is
unaffected (orthogonal to the floor).

That is as far as this measurement reaches, and further than I first took it.
I originally concluded that `borromean-axial-coupling`'s `KeyError` was
therefore the corpus correctly refusing an impossible quantity, and that the
`gram_inverse` -> `gram_quotient_inverse` rename would manufacture a number.
**That inference is withdrawn.** `641c84f8b2` resolved the bean by asking what
CONSUMES the value: it enters a RATIO with the same `u_A` and the same
restricted matrix top and bottom, so scale cancels exactly and the result
depends on it only through the direction of `u_A^T M|_A`. The ambiguity is real
for the pairing in isolation and does not reach the computed quantity. That
commit says as much -- the full-support argument is "correct" but "does not
block the fix" -- and also measures `gram_quotient_inverse` to BE the
Moore-Penrose pseudo-inverse (3.76e-16 relative, annihilates the radical).

What this probe still establishes: the axial channel's dual pairing is
canonical only inside a scale-invariant combination. A future consumer that
uses it outside one inherits the ambiguity, and should read this before
assuming a pseudo-inverse settles it.

The lesson worth carrying: "this quantity is ill-defined" is not a finding
until you check what consumes it. The consumer's arithmetic was one function
call away and I did not look.

WHAT THIS DOES NOT SETTLE. Whether the axial coupling is meaningful under some
other convention, basis, or n. This measures H_3 in the NF basis under
convention D, which is what the producer uses and what the owner ruling of
2026-08-15 makes canonical. Scope-(a) per AGENTS.md: this construction, as it
stands, has no axial pairing -- not "the axial coupling cannot exist".

Upstream premise note: `conj:confinement-frobenius-reciprocity`'s proof opens
"The Markov trace tr_M is a non-degenerate Frobenius form on H_n(q)", which is
the hypothesis the master formula needs and which convention D makes false at
n=3. That is a content-level issue, recorded on `qou-cnbm`, not patched here.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent.parent
for _p in ("computations", "computations/substrate",
           "tools/pyhecke/python", "tools/qou-substrate/python"):
    sys.path.insert(0, str(_ROOT / _p))

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402


def main() -> int:
    t0 = time.monotonic()
    set_compute_dps()
    dps = 50

    from pyhecke.gram import radical_mp, NF_BASIS  # noqa: PLC0415
    from q_parameter import Q_MP  # noqa: PLC0415

    q0 = Q_MP
    qi0 = 1 / Q_MP
    rad = [mp.mpf(x) for x in radical_mp(dps)]

    obs = {
        "trivial": [q0 ** len(b) for b in NF_BASIS],
        "sign": [(-qi0) ** len(b) for b in NF_BASIS],
    }

    def dot(u, v):
        return sum((mp.mpf(a) * mp.mpf(b) for a, b in zip(u, v)), mp.mpf(0))

    n_rad = mp.sqrt(dot(rad, rad))
    rows = []
    for name, o in obs.items():
        n_o = mp.sqrt(dot(o, o))
        cos = abs(dot(o, rad) / (n_o * n_rad))
        rows.append({
            "observable": name,
            "abs_cos_to_radical": fmt(cos),
            "dualisable": bool(cos < mp.mpf(10) ** (-(dps // 2))),
        })

    print("axial observable vs the Gram radical (50 dps, exact route)")
    print("=" * 62)
    for r in rows:
        verdict = ("orthogonal — dual pairing well-defined"
                   if r["dualisable"] else
                   "ALONG the radical — canonical only inside a ratio")
        print(f"  {r['observable']:8} |cos| = "
              f"{mp.nstr(mp.mpf(r['abs_cos_to_radical']), 8):>14}   {verdict}")

    from qou_substrate.witness import WitnessBuilder  # noqa: PLC0415
    w = WitnessBuilder("axial-observable-is-the-gram-radical",
                       engine="python", start_time=t0)
    w.set_description(
        "Overlap of the trivial and sign characters with the convention-D "
        "Markov-Gram radical on the H_3 NF basis. The sign character IS the "
        "radical (|cos| = 1), so `borromean-axial-coupling`'s axial pairing "
        "has no canonical value TAKEN ALONE — but 641c84f8b2 showed the value "
        "enters a ratio where scale cancels exactly, so the ambiguity does "
        "not reach the computed quantity. The trivial channel is orthogonal "
        "to the 50-dps floor. Bean qou-cnbm."
    )
    w.add_data("by_observable", rows)
    w.add_data("radical", [fmt(x) for x in rad])
    # `computed=1, expected=1` asserted nothing: the |cos| the source string
    # cites was computed into `rows`, printed, and never compared, so a
    # radical that had drifted off the sign direction — the whole point of
    # this probe — would still have read "confirmed". Both overlaps the
    # description states are measured here, so both are asserted, against the
    # same 10^-(dps//2) floor the `dualisable` flag above already uses rather
    # than a threshold picked to fit (bean qou-26f2).
    cos_by_obs = {r["observable"]: r["abs_cos_to_radical"] for r in rows}
    radical_floor = mp.nstr(mp.mpf(10) ** (-(dps // 2)), 8)
    w.add_assertion(
        name="sign_character_is_the_radical_direction",
        computed=cos_by_obs["sign"], expected="1", tolerance=radical_floor,
        source="radical_is_sign_representation is true, so the sign character "
               "and the radical coincide by construction; |cos| = 1 confirms "
               "it numerically",
    )
    w.add_assertion(
        name="trivial_character_orthogonal_to_radical",
        computed=cos_by_obs["trivial"], expected="0", tolerance=radical_floor,
        source="the other half of the same measurement: the trivial channel "
               "is orthogonal to the radical down to the 50-dps floor, which "
               "is what makes its dual pairing well-defined",
    )
    print(f"Witness: {w.save()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
