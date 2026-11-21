#!/usr/bin/env python3
"""Does the GS reduction to H_3 destroy the coordination information?

## Why this was asked

`be017ea57b` (`guard(qou-brng)`) closed off the check-then-derive direction on
the coordination number `k` and named what would be informative instead:

    "a k derived from the substrate -- the braid word's own geometry, or a
     packing argument inside the framework -- then COMPARED to the plateau."

Whether that route is even available depends on a prior question: does the
coordination information SURVIVE the Groebner-Shirshov reduction into the H_3
quotient that the production chain actually carries? If the reduction destroys
it, no `k` can be read out of the normal form and the route needs the full
H_{3A} tower.

## The measurement, and the trap it was one step from

`gs_filtration_jet_shape_magic_probe` (merged 30c5628b56) measured the
**jet-grade shape** -- four term counts, one per Coxeter grade -- across bond
counts, and found the map many-to-one: **115 collisions** over 222
configurations, only 107 distinct shapes. The H_3 SHAPE does not determine the
number of inter-nucleon bonds.

The tempting inference is that the reduction destroyed the bond information,
and therefore that the substrate-derived-`k` route is blocked at H_3. **That
inference is false, and this probe is what caught it.** The shape is four
integers; the normal form is six Laurent polynomials. Equal shapes need not be
equal normal forms.

Measured over the same 222 configurations:

    shape collisions        115      distinct shapes         107
    NORMAL-FORM collisions    0      distinct normal forms   222

Not one pair of configurations shares a normal form. The closest shape-
colliding pair, `(Z=1, N=3, m=3)` against `(Z=1, N=3, m=1)`, differs in **261
Laurent coefficients**. So:

  * **The GS reduction to H_3 does NOT destroy the coordination information.**
    The bond count is recoverable from the normal form; only the coarse
    4-number grade summary loses it.
  * The substrate-derived-`k` route named in `be017ea57b` is **not blocked by
    the reduction**. Whether a `k` can actually be derived is a separate and
    still-open question -- this probe removes one candidate obstruction, it
    does not supply the derivation.

## Scope (STRICT -- this is a sample, not a theorem)

This is a **scope-(a) positive**: no collision was found among the
configurations swept. It is NOT a proof that the map
`(Z, N, bond count) -> normal form` is injective in general. The sweep is
every `Z, N <= --max-ZN` with every bond count `m <= C(A,2)`, laying bonds in
the construction's own order. A wider sweep can only strengthen or refute it;
neither is foreclosed here.

The companion negative -- that the SHAPE is genuinely many-to-one -- is not a
sample result in the same way: a single exhibited collision establishes it, and
115 are exhibited.

## Control

`build_atom_nf_bonds(Z, N, keep-all)` must reproduce `build_atom_nf_lau`
exactly, or the sweep is measuring a lookalike construction rather than the
corpus one. Asserted. This control exists because an earlier bond sweep on this
arc used a hand-rolled builder that appended bonds past `C(A,2)` and produced
the opposite answer.

PRECISION: exact over Q. Normal-form coefficients are `fractions.Fraction`;
comparison is exact dict equality. Nothing is evaluated at any numerical q, so
the NO-FLOAT64 discipline is satisfied structurally.
"""
from __future__ import annotations

import argparse
import os
import sys
import time
from fractions import Fraction
from math import comb  # float64-ok: exact integer binomial coefficient

sys.path[:0] = ['/home/user/qou/computations/probes',
                '/home/user/qou/computations',
                '/home/user/qou/computations/substrate']

from gs_filtration_jet_shape_magic_probe import (  # noqa: E402
    build_atom_nf_bonds, GRADE, MAX_GRADE, _first_m,
)
from symbolic_nf_q_degree_magic_probe import build_atom_nf_lau  # noqa: E402


def nf_key(nf) -> tuple:
    """Exact, hashable identity of a normal form. No rounding, no evaluation."""
    return tuple(tuple(sorted(c.items())) for c in nf)


def shape_key(nf) -> tuple:
    """The lossy 4-number summary the jet-shape probe measured."""
    t = [0] * (MAX_GRADE + 1)
    for i, c in enumerate(nf):
        t[GRADE[i]] += len(c)
    tot = sum(t)
    return tuple(Fraction(x, tot) for x in t)


def coeff_diff(a, b) -> int:
    """How many Laurent coefficients differ between two normal forms."""
    return sum(1 for i in range(len(a))
               for e in set(a[i]) | set(b[i])
               if a[i].get(e) != b[i].get(e))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-ZN", type=int, default=4,
                    help="sweep every Z, N <= this")
    a = ap.parse_args()
    t0 = time.time()

    print("=== control: keep-all must reproduce the canonical builder ===",
          flush=True)
    ctrl_n, ctrl_ok = 0, True
    for Z in range(0, a.max_ZN + 1):
        for N in range(0, a.max_ZN + 1):
            if Z + N == 0:
                continue
            ctrl_n += 1
            if build_atom_nf_bonds(Z, N, lambda p, k: True) != build_atom_nf_lau(Z, N):
                ctrl_ok = False
                print(f"  MISMATCH at Z={Z} N={N}", flush=True)
    print(f"  identical on all {ctrl_n} configurations: {ctrl_ok}", flush=True)

    print(f"\n=== sweep: every Z, N <= {a.max_ZN}, every bond count ===",
          flush=True)
    by_shape, by_nf = {}, {}
    shape_coll, nf_coll = [], []
    rows = []
    for Z in range(0, a.max_ZN + 1):
        for N in range(0, a.max_ZN + 1):
            A = Z + N
            if A < 2:
                continue
            for m in range(0, comb(A, 2) + 1):
                nf = build_atom_nf_bonds(Z, N, _first_m(m))
                sh, nk = shape_key(nf), nf_key(nf)
                rows.append({"Z": Z, "N": N, "bonds_kept": m,
                             "bonds_total": comb(A, 2),
                             "terms": sum(len(c) for c in nf)})
                if sh in by_shape:
                    shape_coll.append({"config": [Z, N, m],
                                       "collides_with": list(by_shape[sh])})
                else:
                    by_shape[sh] = (Z, N, m)
                if nk in by_nf:
                    nf_coll.append({"config": [Z, N, m],
                                    "collides_with": list(by_nf[nk])})
                else:
                    by_nf[nk] = (Z, N, m)
        print(f"  Z={Z} done", flush=True)

    n = len(rows)
    print(f"\n=== the contrast ===", flush=True)
    print(f"  configurations swept   : {n}", flush=True)
    print(f"  shape collisions       : {len(shape_coll):>4}   "
          f"distinct shapes       {len(by_shape)}", flush=True)
    print(f"  NORMAL-FORM collisions : {len(nf_coll):>4}   "
          f"distinct normal forms {len(by_nf)}", flush=True)

    example = None
    if shape_coll:
        c = shape_coll[0]
        (Z, N, m) = c["config"]
        (Z2, N2, m2) = c["collides_with"]
        x = build_atom_nf_bonds(Z, N, _first_m(m))
        y = build_atom_nf_bonds(Z2, N2, _first_m(m2))
        d = coeff_diff(x, y)
        example = {"a": c["config"], "b": c["collides_with"],
                   "same_shape": True, "same_normal_form": x == y,
                   "coefficients_differing": d}
        print(f"\n  first shape-colliding pair {tuple(c['config'])} vs "
              f"{tuple(c['collides_with'])}:", flush=True)
        print(f"    same normal form? {x == y}   "
              f"coefficients differing: {d}", flush=True)

    verdict = ("the GS reduction to H_3 does NOT destroy the coordination "
               "information -- the bond count is recoverable from the normal "
               "form; only the 4-number grade shape loses it"
               if not nf_coll else
               "normal-form collisions found -- the reduction DOES destroy "
               "bond-count information")
    print(f"\n  VERDICT: {verdict}", flush=True)
    print("  SCOPE: scope-(a) positive on the swept sample; NOT a proof of "
          "injectivity in general.", flush=True)

    payload = {
        "probe": "nf_bond_count_injectivity",
        "question": "does the Groebner-Shirshov reduction into the H_3 "
                    "quotient destroy the inter-nucleon coordination "
                    "information, blocking the substrate-derived-k route "
                    "named in be017ea57b (guard qou-brng)?",
        "answer": verdict,
        "scope": "scope-(a) positive: no normal-form collision found among the "
                 "configurations swept. NOT a proof that the map "
                 "(Z, N, bond count) -> normal form is injective in general. "
                 "The companion negative (the 4-number SHAPE is many-to-one) "
                 "is established by exhibited collisions and is not "
                 "sample-limited.",
        "why_this_probe_exists": "the merged jet-shape probe (30c5628b56) "
                                 "found 115 shape collisions; the tempting "
                                 "inference that the reduction destroyed the "
                                 "bond information is FALSE -- shape is four "
                                 "integers, the normal form is six Laurent "
                                 "polynomials",
        "control_keep_all_reproduces_canonical_builder": ctrl_ok,
        "control_configurations": ctrl_n,
        "max_ZN": a.max_ZN,
        "configurations_swept": n,
        "shape_collisions": len(shape_coll),
        "distinct_shapes": len(by_shape),
        "normal_form_collisions": len(nf_coll),
        "distinct_normal_forms": len(by_nf),
        "worked_example": example,
        "configurations": rows,
        "shape_collision_list": shape_coll,
        "normal_form_collision_list": nf_coll,
        "arithmetic": "exact over Q (fractions.Fraction); comparison is exact "
                      "dict equality; no float, no evaluation at any "
                      "numerical q",
    }
    try:
        from qou_substrate.witness import WitnessBuilder
        wb = WitnessBuilder.wrap_legacy(
            "nf-bond-count-injectivity", payload,
            script_path=__file__, engine="python+fractions",
            output_dir=os.path.dirname(os.path.abspath(__file__)),
            start_time=t0,
        )
        # Controls, not the verdict.
        wb.add_assertion("control_reproduces_canonical_builder",
                         computed=str(ctrl_ok), expected="True")
        wb.add_assertion("configurations_swept",
                         computed=str(n > 0), expected="True")
        wb.add_assertion("shape_is_many_to_one_on_this_sample",
                         computed=str(len(by_shape) < n),
                         expected="True")
        wb.add_assertion("normal_forms_distinct_on_this_sample",
                         computed=str(len(by_nf) == n),
                         expected="True")
        out = wb.save(extra={
            "auditOnly": True,
            "q0Anchor": "independent",
            "q0AnchorReason": "exact Laurent-polynomial normal forms over Q (fractions.Fraction) "
                              "compared by dict equality; nothing is evaluated at any numerical q",
        })
        print(f"\nWrote {out}", flush=True)
    except Exception as exc:  # pragma: no cover
        print(f"\n(witness not written: {exc})", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
