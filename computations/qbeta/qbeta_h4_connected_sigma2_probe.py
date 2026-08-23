#!/usr/bin/env python3
"""qbeta_h4_connected_sigma2_probe.py — bean 8we6 (session qou-8u91): the
DECISIVE subtracted-object test. Does the connected (sigma_2-supported) part
of the H4 baryon carry a c4-first rung, or does it too leak to c2?

Context. The Route-A gate-fail audit asked for "a subtracted/connected object
built to cancel the u^2/u^3 dressing" — but warned that ARRANGING the
cancellation (combining opposite-[s^4] candidates) is the fit trap. The
crossing-locus probe (qou-tti3, merged #3833) showed the FULL Delta(net)_4 of
the 4th-strand baryon has no derivable coupling with phi_4=phi_6=0. This probe
asks the sharper, DERIVED question: split the H4 element canonically into

    en = en_disc  +  en_conn
         (sigma_0/sigma_1-words)  (words that TOUCH sigma_2 = the 4th strand)

The disconnected part en_disc is H3-word content — route-B-pruned to be
H3-determined. en_conn is the genuinely-4-strand ("connected") object; the
projection onto sigma_2-support is CANONICAL (no tuned coefficient), so testing
it is not a fit. If en_conn's ladder is c4-first (phi_4=phi_6=0 for a derivable
coupling), that is exactly the object the audit asked for (LEAD). If en_conn
also leaks to c2, the route-B prune EXTENDS to the connected part and the whole
4th-strand baryon family is walled (a clean, publishable negative).

Diagnostic 1 — vanishing order at q=1. The c_k ladder needs Delta ~ (q-1)^1.
    ord_{q=1}(Delta_conn) < ord_{q=1}(Delta_net3)  =>  connected part DOMINATES
        at leading order: leaks below c2 (harder wall).
    ord equal, phi_4=phi_6 != 0                    =>  leaks at c2 (route-B
        prune extends).
    phi_4 = phi_6 = 0 at a derivable coupling       =>  c4-first LEAD.

Reuses the merged crossing-locus machinery (baryon_sym, phis_of, is_categorical,
alpha, beta). auditOnly; NO wiring; NO fit (canonical projection + derivability
gate; a tuned root is a wall). Scope-(a).
Witness: qbeta-h4-connected-sigma2.witness.json
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import sympy as sp
from mpmath import mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT))

from qbeta_h4_route_a_gate_probe import (  # noqa: E402
    HA, q, s, reduce_quiet, mul_terms, baryon, net,
)
from qbeta_h4_crossing_locus_probe import (  # noqa: E402
    alpha, beta, baryon_sym, phis_of, is_categorical,
)
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402


def sigma2_part(elem):
    """The connected part: NF words that TOUCH the 4th strand (contain gen 2)."""
    return {w: c for w, c in elem.items() if 2 in w}


def disc_part(elem):
    """The disconnected part: NF words in sigma_0/sigma_1 only (no gen 2)."""
    return {w: c for w, c in elem.items() if 2 not in w}


def vanishing_order(expr, maxord=10):
    """ord_{q=1} of a rational expr in q (order of the (q-1) zero; <0 for a pole)."""
    e = sp.cancel(sp.together(expr))
    num, den = sp.fraction(e)
    on = sp.Poly(sp.expand(num.subs(q, 1 + s)), s).as_expr()
    od = sp.Poly(sp.expand(den.subs(q, 1 + s)), s).as_expr()
    def low(p):
        for k in range(maxord + 1):
            if sp.simplify(sp.diff(p, s, k).subs(s, 0)) != 0:
                return k
        return maxord + 1
    return low(on) - low(od)


def main() -> int:
    t0 = time.monotonic()
    set_compute_dps()
    print("=" * 78)
    print(" 8we6 subtracted-object: connected sigma_2 part — c4-first or c2 leak?")
    print("=" * 78)

    # ── H3 baseline ──
    sig1_inv = {(1,): sp.Integer(1), (): -HA}
    unit = reduce_quiet(mul_terms({(0,): sp.Integer(1)}, sig1_inv))
    b3 = reduce_quiet(mul_terms(reduce_quiet(mul_terms(unit, unit)), unit))
    dnet3 = sp.simplify(net(baryon(b3, ["u", "d", "d"])) - net(baryon(b3, ["u", "u", "d"])))
    ord3 = vanishing_order(dnet3)
    print(f"\n[0] ord_(q=1) Delta(net)_3 = {ord3}   ({time.monotonic()-t0:.1f}s)")

    # ── symbolic H4 baryons, split into disconnected + connected ──
    en = baryon_sym(b3, ["u", "d", "d", "b"])
    ep = baryon_sym(b3, ["u", "u", "d", "b"])
    en_conn, ep_conn = sigma2_part(en), sigma2_part(ep)
    en_disc, ep_disc = disc_part(en), disc_part(ep)

    dnet_conn = sp.expand(net(en_conn) - net(ep_conn))
    dnet_disc = sp.expand(net(en_disc) - net(ep_disc))
    dnet_full = sp.expand(dnet_conn + dnet_disc)
    # sanity: disc+conn reconstructs the full crossing-locus object
    dnet_full_direct = sp.expand(net(en) - net(ep))
    recon_ok = sp.simplify(dnet_full - dnet_full_direct) == 0
    print(f"[1] split reconstructs full object: {recon_ok}")

    ord_conn = vanishing_order(dnet_conn)
    ord_disc = vanishing_order(dnet_disc)
    print(f"[2] ord_(q=1): connected = {ord_conn}, disconnected = {ord_disc}, "
          f"H3 = {ord3}")
    print(f"    connected(q=1) = {sp.simplify(dnet_conn.subs(q,1))}")

    # ── the disconnected part: is it H3-determined (route-B prune check)? ──
    #    Delta_disc should be a scalar multiple of Delta(net)_3 up to (alpha,beta)
    #    dressing if the prune holds on the reduced words.
    ratio_disc = sp.cancel(sp.together(dnet_disc) / sp.together(dnet3))
    disc_is_scalar = (ratio_disc.free_symbols <= {alpha, beta})
    print(f"[3] Delta_disc / Delta(net)_3 depends only on (alpha,beta) "
          f"[q-free scalar dressing]: {disc_is_scalar}")
    if disc_is_scalar:
        print(f"    ratio = {sp.simplify(ratio_disc)}")

    # ── the connected part's ladder: phi_4, phi_6 vs the H3 baseline ──
    verdict = {}
    grid_pass = []
    if ord_conn < ord3:
        print(f"\n[4] connected part DOMINATES at q=1 (ord {ord_conn} < {ord3}) "
              f"-> leaks BELOW c2. Harder wall; no c4-first object here.")
        verdict["class"] = "leaks_below_c2"
    else:
        # phis_of(a, b) returns [s^i] log(b/a); here we want log(conn/net3),
        # so call with (dnet3, dnet_conn).
        phis = phis_of(dnet3, dnet_conn)
        phi4 = sp.cancel(phis[3])
        phi6 = sp.cancel(phis[5])
        N4 = sp.expand(sp.numer(sp.together(phi4)))
        N6 = sp.expand(sp.numer(sp.together(phi6)))
        print(f"\n[4] connected ladder: phi_4, phi_6 as rational fns of (alpha,beta)")
        # categorical grid: does any nameable coupling zero BOTH (finite)?
        grid = [sp.Integer(0), sp.Rational(1, 2), sp.Rational(-1, 2),
                sp.Integer(1), sp.Integer(-1), sp.Integer(2), sp.Integer(-2)]
        for a_v in grid:
            for b_v in grid:
                if sp.simplify(N4.subs({alpha: a_v, beta: b_v})) != 0:
                    continue
                if sp.simplify(N6.subs({alpha: a_v, beta: b_v})) != 0:
                    print(f"    (a,b)=({a_v},{b_v}): phi_4=0 but phi_6!=0 (c3 leak)")
                    continue
                # finite-zero guard (avoid pole-locus 0/0, per the crossing-locus catch)
                f4v = sp.cancel(phi4.subs({alpha: a_v, beta: b_v}))
                f6v = sp.cancel(phi6.subs({alpha: a_v, beta: b_v}))
                if f4v == 0 and f6v == 0:
                    print(f"    *** (a,b)=({a_v},{b_v}): phi_4=phi_6=0 FINITE -> c4-FIRST LEAD")
                    grid_pass.append((str(a_v), str(b_v)))
        if not grid_pass:
            # evaluate phi_4 at the natural couplings to show the c2 leak size
            samples = {}
            for a_v, b_v in [(0, 0), (sp.Rational(1, 2), sp.Rational(1, 2)),
                             (1, 1), (0, 1), (1, 0)]:
                samples[f"({a_v},{b_v})"] = str(sp.nsimplify(sp.cancel(phi4.subs({alpha: a_v, beta: b_v}))))
            verdict["phi4_samples"] = samples
            verdict["class"] = "leaks_at_c2"
            print("    no derivable coupling zeroes both -> connected part ALSO "
                  "leaks at c2 (route-B prune extends to the connected part).")
            print(f"    phi_4 at natural couplings: {samples}")
        else:
            verdict["class"] = "c4_first_lead"
            verdict["grid_pass"] = grid_pass

    lead = bool(grid_pass)
    witness = {
        "computation": "qbeta-h4-connected-sigma2",
        "description": (
            "Bean 8we6 subtracted-object (qou-8u91): canonical split of the "
            "symbolic H4 4th-strand baryon into disconnected (sigma_0/sigma_1 "
            "words, route-B-pruned) + connected (sigma_2-supported) parts; test "
            "whether the CONNECTED object is c4-first (phi_4=phi_6=0 at a "
            "derivable coupling) or also leaks to c2. Vanishing-order diagnostic "
            "+ categorical-grid gate with the pole-locus finite-zero guard. "
            "Canonical projection (no tuned coefficient) => not a fit; a tuned "
            "root would be a wall. auditOnly; no wiring; scope-(a)."
        ),
        "audit_only": True,
        "reconstruct_ok": bool(recon_ok),
        "ord_q1": {"connected": int(ord_conn), "disconnected": int(ord_disc),
                   "h3": int(ord3)},
        "disconnected_is_h3_scalar_dressing": bool(disc_is_scalar),
        "disconnected_ratio": str(sp.simplify(ratio_disc)) if disc_is_scalar else None,
        "verdict_detail": verdict,
        "connected_c4_first_lead": lead,
        "assertions": [
            {"label": "disc+conn split reconstructs the full object", "passed": bool(recon_ok)},
            {"label": "connected-part ladder classified (lead or wall)",
             "passed": "class" in verdict},
        ],
        "verdict": ("CONNECTED sigma_2 object is c4-first at a derivable coupling "
                    "(LEAD)" if lead else
                    "connected sigma_2 object also leaks to/below c2 — route-B "
                    "prune extends to the connected part; the 4th-strand baryon "
                    "family is walled for a genuine c4^even rung (scope-a)"),
    }
    witness["allPassed"] = all(a["passed"] for a in witness["assertions"])
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="sympy")
    import os
    witness["scriptFile"] = os.path.basename(__file__)
    witness["durationMs"] = int((time.monotonic() - t0) * 1000)
    out = HERE / "qbeta-h4-connected-sigma2.witness.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(witness, f, indent=2, ensure_ascii=False, default=str)
        f.write("\n")
    print(f"\n  VERDICT: {witness['verdict']}")
    print(f"  Witness: {out.name}   ({time.monotonic() - t0:.1f}s wall)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
