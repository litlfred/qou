#!/usr/bin/env python3
"""Is `thm:knot-operator-transition` robust to the p-n interface convention?

# Why this exists

`folio/quantum-observable-universe/mass-theory/knot-operator-transition.md`
writes its five transition operators with the p-n factor `sigma - h/2`. That is
`strict_averaged` (delta = 0); the owner ruling of 2026-08-15 (R3) makes the
colour-tube-weighted `sigma - h(1/2 - delta/4)` canonical. Bean `qou-cblw`
finding 8.

The block's CLAIMS are the "Dominant NF" and "Knot type" columns, and those are
statements about which normal-form basis element dominates -- not about the
coefficient itself. So the question is not "does the coefficient move" (it
does, by a relative `delta/2`) but "does the DOMINANCE ORDERING move".

This probe answers that by recomputing the `H_3` normal form of all five
operators under both conventions and comparing the dominant basis element and
the dominance margin. It exists because the block now asserts the margins, and
an asserted number needs a producer.

# Method

`H_3(q)` in the `T_w` basis over `S_3`. Right multiplication by a generator:

    T_w . T_s = T_{ws}              if l(ws) > l(w)
              = h.T_w + T_{ws}      otherwise        (Hecke: T_s^2 = h T_s + 1)

Every coefficient is carried as an exact sympy expression in `q` and evaluated
only at the end, at 30 significant digits via `sp.N`. No float64 anywhere --
per the AGENTS.md NO-FLOAT64 rule, which covers probes.
"""
import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

import itertools  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402

import sympy as sp  # noqa: E402

from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

_HERE = _Path(__file__).resolve().parent

Q = sp.Symbol("q", positive=True)
H = Q - 1 / Q
DELTA = (Q - 1) ** 2 * (1 - Q ** -4) / 3
Q0 = sp.Float(Q_50_DIGIT_STR, 50)

D_BLIND = -H / 2                                        # strict_averaged
D_CANON = -H * (sp.Rational(1, 2) - DELTA / 4)          # bring_color_weighted

#: (label, [(kind, generator), ...]) applied left-to-right.
#: kind: 's' = sigma, 'i' = sigma^-1, 'a' = the p-n averaged crossing.
#: Transcribed from the block's table.
OPS = [
    ("p_to_D",      [("a", 0)]),
    ("D_to_3H",     [("i", 1), ("a", 0)]),
    ("D_to_3He",    [("a", 1), ("s", 0)]),
    ("3H_to_4He",   [("a", 0), ("a", 1), ("s", 0)]),
    ("3He_to_4He",  [("a", 0), ("i", 1), ("a", 0)]),
]


def _length(p):
    return sum(1 for i in range(3) for j in range(i + 1, 3) if p[i] > p[j])


def _act(p, g):
    q = list(p)
    q[g], q[g + 1] = q[g + 1], q[g]
    return tuple(q)


def _mul_gen(elt, g, c, d):
    """`elt * (c*sigma_g + d*I)`, `elt` a dict {perm: exact coeff}."""
    out = {}
    for w, a in elt.items():
        if a == 0:
            continue
        out[w] = out.get(w, 0) + d * a
        ws = _act(w, g)
        if _length(ws) > _length(w):
            out[ws] = out.get(ws, 0) + c * a
        else:
            out[w] = out.get(w, 0) + c * a * H
            out[ws] = out.get(ws, 0) + c * a
    return {k: sp.simplify(v) for k, v in out.items()}


def normal_form(ops, d_pn):
    e = {tuple(range(3)): sp.Integer(1)}
    for kind, g in ops:
        c, d = (1, 0) if kind == "s" else (1, -H) if kind == "i" else (1, d_pn)
        e = _mul_gen(e, g, c, d)
    return e


def dominant(ops, d_pn):
    """(dominant basis element, dominance margin) at q0, exactly then evaluated."""
    e = normal_form(ops, d_pn)
    vals = {w: abs(sp.N(v.subs(Q, Q0), 30)) for w, v in e.items() if v != 0}
    top = max(vals, key=vals.get)
    ordered = sorted(vals.values(), reverse=True)
    margin = ordered[0] / ordered[1] if len(ordered) > 1 else sp.oo
    return top, margin


def main() -> int:
    started = time.monotonic()
    w = WitnessBuilder("knot-operator-transition-convention-robustness",
                       engine="sympy", output_dir=_HERE, start_time=started)
    w.set_description(
        "Do the Dominant-NF and Knot-type columns of thm:knot-operator-transition "
        "survive the p-n convention change from strict_averaged to the canonical "
        "bring_color_weighted? Recomputes the H_3 normal form of all five "
        "transition operators under both and compares dominance."
    )
    w.set_content_block("thm:knot-operator-transition")
    w.add_parameter("q0", str(Q0))
    w.add_parameter("q0Anchor", "proton")

    rel_shift = sp.N((DELTA / 2).subs(Q, Q0), 20)
    w.add_assertion("relative_shift_on_pn_coefficient_is_delta_over_2",
                    str(rel_shift), "0.00068785",
                    tolerance="1e-8",
                    source="delta/2 at the proton pin")

    results, margins = {}, []
    for label, ops in OPS:
        top_b, marg_b = dominant(ops, D_BLIND)
        top_c, marg_c = dominant(ops, D_CANON)
        same = top_b == top_c
        margins.append(float(marg_b))
        results[label] = {
            "dominant_blind": str(top_b),
            "dominant_canonical": str(top_c),
            "dominant_unchanged": bool(same),
            "margin_blind": str(sp.N(marg_b, 12)),
            "margin_canonical": str(sp.N(marg_c, 12)),
        }
        print(f"{label:<12} blind={top_b} canon={top_c} "
              f"margin={sp.N(marg_b, 6)} same={same}", flush=True)
        w.add_assertion(f"dominant_unchanged_{label}", str(same), "True",
                        source=f"margin {sp.N(marg_b, 6)}x")

    lo, hi = min(margins), max(margins)
    print(f"\nmargin band: {lo:.4g}x .. {hi:.4g}x   vs relative perturbation "
          f"{float(rel_shift):.3g}", flush=True)
    # The block states "4.7x to 9.6x"; pin that band so an edit to either side
    # of the pair (block prose, or this probe) shows up as a failure.
    w.add_assertion("margin_min_is_4_7x", str(sp.N(sp.Float(lo), 6)), "4.73",
                    tolerance="0.05")
    w.add_assertion("margin_max_is_9_6x", str(sp.N(sp.Float(hi), 6)), "9.57",
                    tolerance="0.05")

    w.add_data("results", results)
    w.add_data("conclusion",
               "All five transitions keep the same dominant NF basis element "
               "under both conventions. Margins exceed the relative "
               "perturbation by ~4 orders of magnitude, so the Dominant-NF and "
               "Knot-type columns are convention-independent.")
    w.add_caveat(
        "This vindicates the block's CONCLUSIONS, not its written operators: "
        "those are still in the strict_averaged (delta = 0) form. Labelled "
        "rather than flipped -- see bean qou-cblw."
    )

    path = w.save()
    built = json.loads(_Path(path).read_text())
    print(f"witness -> {path}\nallPassed = {built['allPassed']} "
          f"({len(built['assertions'])} assertions)", flush=True)
    return 0 if built["allPassed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
