#!/usr/bin/env python3
"""Atomic Habiro coefficients via the Markov-peel route (bean `qou-lrnd`).

Covers A = 1 through A = 4 (proton, neutron, deuteron, helium-3,
tritium, helium-4). A = 3 is what motivated it -- see below -- but the
same route reaches A = 4 in well under a minute, so the scope is "every
atom the peel can carry", not "A = 3".

# Why this exists

`habiro_coefficients_atomic.py` obtains `tr_M` from
`markov_trace_symbolic`, which evaluates the Wedderburn sum

    tr_M(beta) = SUM_{lambda |- 3A} y_lambda(q) . chi^lambda(beta)

over every partition of `3A`.  At `A = 3` that is 30 partitions with
irreps up to dimension 216, and the cost was measured this session at
4.31 s/dim^2 -- extrapolating to **18.1 days**.  That measurement is
what closed the A = 3 door.

`markov_peel.tr_M_atomic` reaches the same object by a different road:
it reduces the braid word in the Hecke normal-form basis (256 terms at
A = 3) and takes the Markov trace by recursive ascent, never forming the
partition sum at all.  Measured here: **under two seconds**.

So the A = 3 blocker was a routing choice, not a compute wall.

# The two routes are the same object, not merely close

`sp.cancel(peel - partition_sum) == 0` exactly, for the proton and for
the deuteron -- verified in `assert_routes_agree()` below.  This is a
symbolic identity, not an agreement to N digits.

# The `cancel` is load-bearing -- do not remove it

`tr_M_atomic` returns an **unreduced** fraction and `to_u_polynomial`
does not cancel.  Without `sp.cancel` the deuteron comes out carrying a
spurious `(q^2+1)^2`: `deg_u(p) = 108` against the correct 100, with
denominator `192.u^46.(u^4+1)^5` instead of `(u^4+1)^3`.  The Habiro
coefficients are computed *from* `p_in_u`, so every `a_m` is then wrong
while `reconstruction_matches` still reports True -- reconstruction only
checks `p = SUM a_m (u;u)_m`, which holds for the wrong `p` too.

That failure is silent, and the only thing that caught it was running
the deuteron first and diffing against its committed values.  Hence the
validation below is a gate, not a courtesy.
"""
import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

import json  # noqa: E402
import time  # noqa: E402

import sympy as sp  # noqa: E402

from markov.markov_peel import tr_M_atomic  # noqa: E402
from habiro.habiro_coefficients_atomic import (  # noqa: E402
    to_u_polynomial,
    cyclotomic_expansion,
    reconstruct,
)
from qou_substrate.witness import WitnessBuilder  # noqa: E402

U = sp.Symbol("u", positive=True)
_HERE = _Path(__file__).resolve().parent
_ATOMIC_WITNESS = _HERE / "habiro-coefficients-atomic.witness.json"

# (Z, N, label). A=1 and A=2 are the validation set -- they have
# committed values. A=3 is the new computation.
ATOMS = [
    (1, 0, "proton", "p"),
    (0, 1, "neutron", "n"),
    (1, 1, "deuteron", "D"),
    (2, 1, "helium-3", None),
    (1, 2, "tritium", None),
    # A=4. AGENTS.md flags `A >= 4` as long-compute, so this was measured
    # before being added rather than assumed from the A=3 timings: tr_M
    # 24.5 s + cancel 18.1 s, deg_u(p) = 180, a_0..a_18, reconstruction
    # exact. That is the whole atom in well under a minute.
    (2, 2, "helium-4", None),
    # A=5. Measured: tr_M 325 s + cancel 84 s, deg_u(p) = 216, a_0..a_20,
    # reconstruction exact. Correct but ~7 minutes, so it is behind
    # `--max-a 5` rather than in the default run.
    (2, 3, "helium-5", None),
    # A=6. Measured: tr_M 2036 s + cancel 212 s, deg_u(p) = 260, a_0..a_22,
    # denom = 49152*u^110*(u^4+1)^11, reconstruction exact. ~38 min, so
    # `--max-a 6` and the long-compute logging discipline.
    (3, 3, "lithium-6", None),
]

#: Default ceiling. A<=4 is the whole set in about a minute.
#:
#: MEASURED cost of `tr_M` (the dominant term), this 4-core container:
#:
#:     A=3     1.8 s      A=5    325 s
#:     A=4    24.6 s      A=6   2036 s
#:
#: Step ratios 13.7x, 13.2x, 6.3x -- so the growth FLATTENS at the top
#: rather than compounding, and A=6 came in at ~38 min against a ~70 min
#: extrapolation. Do not extrapolate A=7 from the 13x figure; measure it.
#: Anything above the default belongs under the AGENTS.md long-compute
#: logging discipline (`python3 -u ... 2>&1 | tee`).
DEFAULT_MAX_A = 4


def _sym(text: str):
    """Parse a witness polynomial string INTO `U`.

    `sp.sympify("u**100 + ...")` mints a bare `Symbol('u')` with no
    assumptions, which is a *different* symbol from `Symbol('u',
    positive=True)`.  Subtracting the two never yields zero, so a
    comparison written the obvious way reports a mismatch that is not
    there.  (Cost this session: one wrongly-retracted result.)
    """
    return sp.sympify(text, locals={"u": U})


def habiro_via_peel(Z: int, N: int) -> dict:
    """`tr_M` -> reduced fraction -> `p_in_u` -> Habiro coefficients."""
    t0 = time.time()
    expr = tr_M_atomic(Z, N, include_inter=True)
    q = next(s for s in expr.free_symbols if str(s) == "q")
    t_trace = time.time() - t0

    t0 = time.time()
    expr = sp.cancel(sp.together(expr))  # load-bearing -- see module docstring
    t_cancel = time.time() - t0

    p_u, shift, denom = to_u_polynomial(expr, q, U)
    coeffs = cyclotomic_expansion(p_u, U, max_m=40)
    reconstructs = sp.expand(reconstruct(coeffs, U, max_m=40) - p_u) == 0

    return {
        "Z": Z,
        "N": N,
        "A": Z + N,
        "n_strands": 3 * (Z + N),
        "tr_M_in_q": str(expr),
        "p_in_u": str(p_u),
        "shift": shift,
        "denom_in_u": denom,
        "denom_factored": str(sp.factor(_sym(denom))),
        "deg_p_u": int(sp.Poly(p_u, U).degree()),
        "habiro_coefficients": coeffs,
        "all_integral": all(c["integral"] for c in coeffs),
        "reconstruction_matches": bool(reconstructs),
        # Integer milliseconds, not seconds-as-float: wall time makes no
        # precision claim, and a raw float64 in a witness trips the
        # NO-FLOAT64 ratchet regardless of what the number means.
        "elapsed_trace_ms": int(round(t_trace * 1000)),
        "elapsed_cancel_ms": int(round(t_cancel * 1000)),
    }


def assert_routes_agree(w: WitnessBuilder) -> None:
    """The peel and the partition sum are the SAME rational function.

    Checked on the proton and the deuteron only: the partition route at
    A = 3 is the 18-day path this producer exists to avoid, so it cannot
    be part of a routine run.
    """
    from habiro.habiro_coefficients_atomic import markov_trace_symbolic

    q = sp.Symbol("q", positive=True)
    for Z, N, label in [(1, 0, "proton"), (1, 1, "deuteron")]:
        peel = tr_M_atomic(Z, N, include_inter=True)
        qp = next(s for s in peel.free_symbols if str(s) == "q")
        # route="partition" is PINNED. markov_trace_symbolic now defaults
        # to the peel, so leaving this defaulted would compare the peel
        # against itself and pass unconditionally -- a self-fulfilling
        # assertion, the exact defect class this check exists to rule out.
        part = markov_trace_symbolic(Z, N, q, include_inter=True,
                                     route="partition")
        delta = sp.cancel(sp.together(peel.subs(qp, q) - part))
        w.add_assertion(
            f"routes_agree_symbolically_{label}", str(delta), "0",
            source="peel - partition_sum, cancelled",
        )


def main(argv: list[str] | None = None) -> int:
    import argparse

    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--max-a", type=int, default=DEFAULT_MAX_A,
                    help=f"largest A to compute (default {DEFAULT_MAX_A}; "
                         "A=5 adds ~7 min, A=6 is an hour-plus)")
    args = ap.parse_args(argv)

    started = time.monotonic()
    w = WitnessBuilder("habiro-coefficients-via-peel", engine="sympy",
                       output_dir=_HERE, start_time=started)
    w.set_description(
        "Atomic Habiro cyclotomic coefficients for A=1..4 (through helium-4) "
        "obtained via markov_peel.tr_M_atomic instead of the Wedderburn "
        "partition sum. The partition route was measured at ~18.1 days for "
        "A=3; this one does A=3 in seconds and A=4 in under a minute. Gated "
        "on exact reproduction of every committed A<=2 value."
    )
    w.set_content_block("prop:markov-pair-z2")

    committed = w.add_upstream(_ATOMIC_WITNESS)["results"]
    by_key = {k.split()[0]: v for k, v in committed.items()}

    results = {}
    for Z, N, label, ref_key in ATOMS:
        if Z + N > args.max_a:
            print(f"{label:10s} A={Z+N} SKIPPED (--max-a {args.max_a})",
                  flush=True)
            continue
        r = habiro_via_peel(Z, N)
        results[label] = r
        print(f"{label:10s} A={r['A']} n={r['n_strands']} "
              f"deg_u={r['deg_p_u']:3d} a_0..a_{len(r['habiro_coefficients'])-1} "
              f"trace={r['elapsed_trace_ms']}ms cancel={r['elapsed_cancel_ms']}ms",
              flush=True)

        w.add_assertion(f"reconstruction_exact_{label}",
                        str(r["reconstruction_matches"]), "True")

        # VALIDATION GATE: every atom with a committed value must
        # reproduce it EXACTLY -- polynomial, denominator, and every a_m.
        if ref_key and ref_key in by_key:
            ref = by_key[ref_key]
            w.add_assertion(
                f"p_in_u_matches_committed_{label}",
                str(sp.expand(_sym(r["p_in_u"]) - _sym(ref["p_in_u"])) == 0),
                "True", source=str(_ATOMIC_WITNESS.name))
            w.add_assertion(
                f"denom_matches_committed_{label}",
                str(sp.expand(_sym(r["denom_in_u"]) - _sym(ref["denom_in_u"])) == 0),
                "True", source=str(_ATOMIC_WITNESS.name))
            ref_am = ref.get("habiro_coefficients") or []
            same = (len(ref_am) == len(r["habiro_coefficients"])) and all(
                sp.expand(_sym(a["a_m"]) - _sym(b["a_m"])) == 0
                for a, b in zip(ref_am, r["habiro_coefficients"]))
            w.add_assertion(f"all_a_m_match_committed_{label}", str(same), "True",
                            source=f"{len(ref_am)} coefficients")

    assert_routes_agree(w)

    w.add_parameter("max_a", args.max_a)
    w.add_data("results", results)
    w.add_data("method",
               "markov_peel.tr_M_atomic + sp.cancel + to_u_polynomial "
               "+ cyclotomic_expansion")
    w.add_caveat(
        "The A>=3 coefficients are NOT cross-checked against an independent "
        "second computation -- there is none: the partition-sum route is the "
        "18-day path this producer exists to avoid. Their warrant is that the "
        "SAME code path reproduces every committed A<=2 value exactly, and "
        "that the two routes are symbolically identical where both can run."
    )
    w.add_caveat(
        "Convention: this inherits whatever p-n interface convention "
        "atom_canonical_crossings emits (kind 'averaged_weighted', the "
        "colour-weighted form). It does NOT inherit the colour-BLIND Rust "
        "gram.rs path -- see bean qou-cblw."
    )

    path = w.save()
    print(f"\nwitness -> {path}", flush=True)
    built = json.loads(_Path(path).read_text())
    print(f"allPassed = {built['allPassed']}  "
          f"({len(built['assertions'])} assertions)", flush=True)
    return 0 if built["allPassed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
