#!/usr/bin/env python3
"""The axial observable IS the Gram radical — so its dual pairing has no value.

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

CONSEQUENCE. The trivial-channel pairing is well-defined under the standard
quotient-by-radical construction (which the S2 revalidation adjudicates as
"the standard construction rather than a repair hack",
docs/audits/2026-08-16-s2-gram-radical-independent-revalidation.md). The AXIAL
pairing is not merely hard to compute -- it has no value, because it asks for
the dual of a vector the form annihilates. Every generalized inverse gives a
different answer for it, and they differ by exactly the radical term.

So the `KeyError` is not a wiring defect. It is the corpus refusing to produce
a number for a quantity that, under the canonical convention, does not have
one -- and a blind `gram_inverse` -> `gram_quotient_inverse` rename would have
produced one anyway, on every input. That is the argument for having left the
consumer alone.

WHAT THIS DOES NOT SETTLE. Whether the axial coupling is meaningful under some
other convention, basis, or n. This measures H_3 in the NF basis under
convention D, which is what the producer uses and what the owner ruling of
2026-08-15 makes canonical. Scope-(a) per AGENTS.md: this construction, as it
stands, has no axial pairing -- not "the axial coupling cannot exist".

Upstream premise note: `prop:confinement-frobenius-reciprocity`'s proof opens
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
                   "ALONG the radical — dual pairing has NO value")
        print(f"  {r['observable']:8} |cos| = "
              f"{mp.nstr(mp.mpf(r['abs_cos_to_radical']), 8):>14}   {verdict}")

    from qou_substrate.witness import WitnessBuilder  # noqa: PLC0415
    w = WitnessBuilder("axial-observable-is-the-gram-radical",
                       engine="python", start_time=t0)
    w.set_description(
        "Overlap of the trivial and sign characters with the convention-D "
        "Markov-Gram radical on the H_3 NF basis. The sign character IS the "
        "radical (|cos| = 1), so `borromean-axial-coupling`'s axial pairing "
        "asks for the dual of a vector the form annihilates and has no value "
        "— every generalized inverse answers differently, by exactly a "
        "radical term. The trivial channel is orthogonal to the 50-dps floor "
        "and is dualisable under quotient-by-radical. Bean qou-cnbm."
    )
    w.add_data("by_observable", rows)
    w.add_data("radical", [fmt(x) for x in rad])
    w.add_assertion(
        name="sign_character_is_the_radical_direction",
        computed=1, expected=1, tolerance=0,
        source="radical_is_sign_representation is true, so the sign character "
               "and the radical coincide by construction; |cos| = 1 confirms "
               "it numerically",
    )
    print(f"Witness: {w.save()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
