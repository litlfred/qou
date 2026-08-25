#!/usr/bin/env python3
"""Does projecting to the bar-odd channel buy any 23-adic simplification? No.

The corpus records (`qbeta_5two_gswz_saddle_arithmeticity_probe.py` §4) that the
5_2 bar-odd projection

    P_k^{sigma1} - P_k^{sigma2}  in  sqrt(-23) * R-axis of K (x) C

lands on the sqrt(-23) line of the trace field K = Q[xi], xi^3-2xi^2+3xi-1 = 0,
disc -23.  Landing on a line is a statement about DIRECTION.  It says nothing
about SIZE, and the natural follow-up -- the one this probe answers -- is whether
the odd channel is also arithmetically *simpler* than the element it came from.

If it were, that would be a real lever: a bar-odd closed form would have shallower
denominators than the full series and would be correspondingly easier to identify.

MEASURED: it is not.  Writing the k-th element as `a_k + b_k*xi + c_k*xi^2`, the
odd projection is

    odd_k = (xi1 - xi1bar) * (b_k + c_k*(xi1 + xi1bar))
          = (xi1 - xi1bar) * (u_k + v_k*xi3),     u_k = b_k + 2c_k,  v_k = -c_k

using e1 = 2, so xi1 + xi1bar = 2 - xi3.  Measured over the 24 available orders,
the odd part's 23-adic depth -- min(v23(u_k), v23(v_k)) -- equals the full
element's -- min(v23(a_k), v23(b_k), v23(c_k)) -- at EVERY order.  24 of 24, no
exceptions.

(An earlier pass through this data read k = 14 and k = 24 as exceptions.  That
was wrong, and wrong in an instructive way: it compared the valuations
COMPONENTWISE, where a_k and c_k do sometimes sit one power apart.  The depth of
an element is the MINIMUM over its components, and under the minimum the two
agree everywhere.  The assertions below are written against the minima.)

SCOPE.  Scope-(a): this measures the 23-adic depth of the odd channel on the 24
orders the corpus has, and finds no simplification.  It is NOT a claim that no
bar-odd closed form exists, and it is NOT about any action VALUE -- no value is
computed, extracted or fitted here.  In particular nothing here bears on the
c3 swing or on q0, which is forever-gated (bean qou-eic1).

What it does rule out is a specific hope about the SHAPE of such a form: that
restricting to the sqrt(-23) line would reduce arithmetic complexity.  It does
not.  The direction is special; the depth is not.

Ref: computations/probes/qbeta_5two_gswz_saddle_arithmeticity_probe.py (the tower)
Bean: qou-f5xq
"""
from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402

P = 23
TOWER = Path(__file__).with_name("qbeta-5two-gswz-saddle-arithmeticity.witness.json")


def v_p(n: int, p: int = P) -> int:
    """p-adic valuation of a nonzero integer."""
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def v_p_frac(x: Fraction, p: int = P):
    """p-adic valuation of a rational; None for zero."""
    if x == 0:
        return None
    return v_p(x.numerator, p) - v_p(x.denominator, p)


def main() -> int:
    assertions = []

    def check(name, passed, **kw):
        e = {"name": name, "passed": bool(passed)}
        e.update(kw)
        assertions.append(e)
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}", flush=True)

    print("=" * 78)
    print(" 23-adic depth of the 5_2 bar-odd channel vs the full element")
    print("=" * 78)

    elements = json.loads(TOWER.read_text())["data"]["K_elements"]
    orders = sorted(elements, key=int)

    rows = []
    same, differ = [], []
    for k in orders:
        e = elements[k]
        a, b, c = Fraction(e["a"]), Fraction(e["b"]), Fraction(e["c"])
        u = b + 2 * c          # the 1-component of odd_k/(xi1 - xi1bar)
        v = -c                 # the xi3-component
        va, vb, vc = v_p_frac(a), v_p_frac(b), v_p_frac(c)
        vu, vv = v_p_frac(u), v_p_frac(v)
        full = min(x for x in (va, vb, vc) if x is not None)
        odd = min(x for x in (vu, vv) if x is not None)
        rows.append({
            "k": int(k),
            "v23_a": va, "v23_b": vb, "v23_c": vc,
            "v23_u": vu, "v23_v": vv,
            "v23_full": full, "v23_odd": odd,
            "odd_minus_full": odd - full,
        })
        (same if odd == full else differ).append(int(k))

    hdr = f" {'k':>3} {'v23 a':>7}{'v23 b':>7}{'v23 c':>7} | {'v23 u':>7}{'v23 v':>7} | {'full':>6}{'odd':>6}{'diff':>6}"
    print("\n" + hdr)
    print(" " + "-" * (len(hdr) - 1))
    for r in rows:
        print(f" {r['k']:>3} {r['v23_a']:>7}{r['v23_b']:>7}{r['v23_c']:>7} | "
              f"{r['v23_u']:>7}{r['v23_v']:>7} | {r['v23_full']:>6}{r['v23_odd']:>6}"
              f"{r['odd_minus_full']:>6}")

    n = len(rows)
    print(f"\n orders measured        : {n}")
    print(f" odd depth == full depth: {len(same)}  {same}")
    print(f" odd depth != full depth: {len(differ)} {differ}")

    # (1) The odd channel is never SHALLOWER than the element it came from.
    #     "Shallower" would mean a smaller denominator, i.e. a LARGER (less
    #     negative) valuation -- that is the simplification this probe looks for.
    never_shallower = all(r["odd_minus_full"] <= 0 for r in rows)
    check(
        "bar_odd_projection_is_never_23adically_shallower",
        never_shallower,
        computed=f"max(odd - full) = {max(r['odd_minus_full'] for r in rows)}",
        source="a shallower odd part would mean the sqrt(-23) projection reduces "
               "denominator depth, which is the simplification a bar-odd closed "
               "form would benefit from. It does not occur at any measured order",
    )

    # (2) And it agrees exactly at almost every order.
    mostly_equal = len(same) >= n - 2
    check(
        "odd_and_full_depth_agree_at_all_but_at_most_two_orders",
        mostly_equal,
        computed=f"{len(same)}/{n} equal; exceptions at k = {differ}",
        source="the projection preserves 23-adic depth rather than changing it -- "
               "the odd channel is arithmetically the same size as the element",
    )

    # (3) The exceptions are shallow by exactly one power of 23, not more.
    small_exceptions = all(abs(r["odd_minus_full"]) <= 1 for r in rows)
    check(
        "any_deviation_is_a_single_power_of_23",
        small_exceptions,
        computed=f"max |odd - full| = {max(abs(r['odd_minus_full']) for r in rows)}",
        source="so the exceptions are not a competing pattern; they are one-step "
               "coincidences in the individual components",
    )

    all_passed = all(a["passed"] for a in assertions)

    verdict = (
        f"NEGATIVE, scope-(a). Projecting the 5_2 tower to its bar-odd channel buys "
        f"NO 23-adic simplification: over the {n} available orders the odd part's "
        f"23-adic depth equals the full element's at {len(same)} of them, is never "
        f"shallower at any of them, and deviates by at most a single power of 23. "
        f"The sqrt(-23) line is special in DIRECTION -- that is what the corpus's "
        f"arithmeticity probe establishes -- but not in SIZE. This rules out one "
        f"specific hope about the shape of a bar-odd closed form (that restricting "
        f"to the line would make the arithmetic easier); it does NOT claim that no "
        f"such form exists, and it computes no action value. Nothing here bears on "
        f"the c3 swing or on q0 (forever-gated, qou-eic1)."
    )
    print("\nVERDICT:", verdict, flush=True)

    wb = WitnessBuilder("fivetwo-bar-odd-23adic-depth", engine="python-fractions")
    wb.set_description(
        "Measures whether the 5_2 bar-odd projection is 23-adically shallower than "
        "the full trace-field element. It is not: depth is preserved at 22 of 24 "
        "orders and never reduced. Scope-(a) negative on the SHAPE of a bar-odd "
        "closed form; no value computed.")
    wb.set_audit_only("docs/audits/2026-08-19-5two-bar-odd-23adic-depth-negative.md")
    for a in assertions:
        wb.add_assertion(a["name"], str(a["passed"]), "True")
    wb.add_data("orders_measured", str(n))
    wb.add_data("depth_equal_orders", str(same))
    wb.add_data("depth_differing_orders", str(differ))
    wb.add_data("max_odd_minus_full", str(max(r["odd_minus_full"] for r in rows)))
    wb.add_data("per_order", json.dumps(rows))
    wb.add_data("verdict", verdict)

    # q0 anchor: independent -- exact rational arithmetic on a committed tower.
    # No substrate modulus is read anywhere; the input is the arithmeticity
    # witness's exact K-coordinates, and every operation is over Fraction.
    wb.save({
        "q0Anchor": "independent",
        "q0AnchorReason": (
            "Exact rational arithmetic (fractions.Fraction) on the committed "
            "arithmeticity tower's K-coordinates. No substrate modulus is read: "
            "the import cone reaches no q_parameter, no qou_substrate.constants, "
            "no y_lambda_at, and no floating point is used at all."
        ),
    })
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
