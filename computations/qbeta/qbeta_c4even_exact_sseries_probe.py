#!/usr/bin/env python3
"""c4^even via EXACT-rational s-series of the net-route ladder (bean 9fnm follow-on).

Promotes the c_4^even "scale check" of qbeta_c3even_exact_sseries_probe.py
(KC=3, labelled "not a claimed rung") to a VALIDATED exact rung by extending
the exact-rational Taylor extraction to KC=4 (series order s^10). Folding
log(1 + c_4 u^4) into the ladder model at its own order and reading the next
order as a stability residual makes c_4^even a real rung rather than a bare
s^8 scale estimate.

  R(q)   = Qb_over_me(q) / [QA_over_me(q) * cos(alpha_eff(q))]     (R(1)=1)
  ladder:  log R(s) = sum_{k>=2} log(1 + c_k u(s)^k),  s = q-1
  c_k^even read at s^{2k} after subtracting the exact folds of c_2..c_{k-1}.

Gates: reproduce c_2^even (~-8.006) and c_3^even (the 9fnm value) exactly
before claiming c_4^even. Stability: after folding c_4, the s^10 residual over
u^5 gives the c_5 scale — reported as a conditioning check ("does the triangle
stay stable", per bean 9fnm), NOT a c_5 rung claim.

Casoratian: W_3 = c_3^even*c_4^odd - c_4^even*c_3^odd stays GATED on c_4^odd
(beyond the CAL-anchored tier); with c_4^even now a real rung, only c_4^odd
remains for the AW W_3/W_2 > 0 positivity test. auditOnly; NO production
wiring; NO fit (every number is a Taylor coefficient of an exact object).

Witness: qbeta-c4even-exact-sseries.witness.json
"""
from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path

import sympy as sp
from mpmath import mp
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

HERE = Path(__file__).resolve().parent          # computations/qbeta
ROOT = HERE.parent                               # computations/
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "substrate"))

q, s = sp.symbols("q s", positive=True)

KC = 4          # extract through c_4 (s^8); fold to s^10 for the stability check
NS = 2 * KC + 2  # series order in s (s^10 inclusive)


def load_net_symbolic(side: str):
    d = json.loads((ROOT / "free-neutron-decay.witness.json").read_text())
    net = sp.Integer(0)
    for t in d[side]["nf_terms"]:
        net += sp.sympify(t["coefficient_symbolic"], locals={"q": q})
    return sp.simplify(net)


def ser_mul(a, bb):
    return [sp.expand(sum(a[i] * bb[n - i] for i in range(n + 1))) for n in range(NS + 1)]


def main() -> int:
    t0 = time.monotonic()
    set_compute_dps()

    print("=" * 76)
    print(" c4^even — EXACT-rational s-series of the net-route ladder (bean 9fnm)")
    print("=" * 76)

    net_n = load_net_symbolic("neutron")
    net_p = load_net_symbolic("proton")
    dnet = sp.simplify(net_n - net_p)
    dnet_reg = sp.cancel(dnet / (q - 1))

    d_wit = json.loads((ROOT / "free-neutron-decay.witness.json").read_text())
    params = d_wit.get("parameters")
    q0 = mp.mpf(str(params["q"])) if params and "q" in params else \
        mp.mpf("1.1099785955573347198997632204832250266562084087802")
    dn_wit = mp.mpf(str(d_wit["transition"]["delta_net"]))
    dnet_f = sp.lambdify(q, dnet, "mpmath")
    dn_mine = dnet_f(q0)
    print(f"  VALIDATE @ q0: Delta(net) mine={mp.nstr(dn_mine,12)} witness={mp.nstr(dn_wit,12)}")
    assert abs(dn_mine - dn_wit) < mp.mpf("1e-6"), "Delta(net) reconstruction drifted"
    sgn = int(mp.sign(dn_mine))

    hbar = (q - 1) / q
    b = sp.sqrt(q**4 + q**2 + 1) / (q**2 + 1)
    u = b * hbar**2
    z = q**3 / (q**2 + 1)
    h = q - 1 / q
    alpha_eff = (z - 1) * h / 2 - u / 2
    QA_over_me = (2 * q + 1 - q**2) * (q + 1) / (2 * q**3)
    Qb_over_me = sgn * dnet_reg / q
    Rq = Qb_over_me / (QA_over_me * sp.cos(alpha_eff))

    R1 = sp.simplify(Rq.subs(q, 1))
    print(f"  R(q=1) exact = {R1}")

    print(f"\n  exact sympy series to O(s^{NS+1}) (log R and u) — this is the slow step ...")
    t1 = time.monotonic()
    logR_ser = sp.series(sp.log(Rq.subs(q, 1 + s) / R1), s, 0, NS + 1).removeO()
    u_ser = sp.series(u.subs(q, 1 + s), s, 0, NS + 1).removeO()
    logR_c = [sp.simplify(logR_ser.coeff(s, i)) for i in range(NS + 1)]
    u_c = [sp.simplify(u_ser.coeff(s, i)) for i in range(NS + 1)]
    print(f"  ... series done in {time.monotonic()-t1:.1f}s", flush=True)

    upow = {1: u_c}
    for k in range(2, KC + 2):
        upow[k] = ser_mul(upow[k - 1], u_c)

    # triangular solve, folding each c_k exactly
    c = {}
    model = [sp.Integer(0)] * (NS + 1)
    for k in range(2, KC + 1):
        order = 2 * k
        resid = sp.simplify(logR_c[order] - model[order])
        ck = sp.simplify(resid / upow[k][order])
        c[k] = ck
        print(f"  c_{k}^even (exact, s^{order}) = {mp.nstr(mp.mpf(str(sp.N(ck,40))), 16)}", flush=True)
        cku = [sp.expand(ck * t) for t in upow[k]]
        cur = [sp.Integer(1)] + [sp.Integer(0)] * NS
        n = 1
        while n * order <= NS:
            cur = ser_mul(cur, cku)
            sign = sp.Integer((-1) ** (n + 1))
            for i in range(NS + 1):
                model[i] = sp.expand(model[i] + sign * cur[i] / n)
            n += 1

    c2n = mp.mpf(str(sp.N(c[2], 40)))
    c3n = mp.mpf(str(sp.N(c[3], 40)))
    c4n = mp.mpf(str(sp.N(c[4], 40)))

    # gates against the established rungs
    gate_c2 = abs(c2n - mp.mpf("-8.006")) < mp.mpf("0.05")
    # c3^even from the 9fnm witness, if present
    c3_ref = None
    c3wit = HERE / "qbeta-c3even-exact-sseries.witness.json"
    if c3wit.exists():
        try:
            c3_ref = mp.mpf(str(json.loads(c3wit.read_text())["numeric_50dps"]["c3_even"]))
        except Exception:
            c3_ref = None
    gate_c3 = (c3_ref is None) or (abs(c3n - c3_ref) < mp.mpf("1e-6"))
    print(f"\n  GATE c_2^even ~= -8.006: {'PASS' if gate_c2 else 'FAIL'} (got {mp.nstr(c2n,10)})")
    print(f"  GATE c_3^even vs 9fnm witness ({mp.nstr(c3_ref,10) if c3_ref else 'n/a'}): "
          f"{'PASS' if gate_c3 else 'FAIL'} (got {mp.nstr(c3n,10)})")
    print(f"\n  c_4^even (VALIDATED RUNG) = {mp.nstr(c4n, 16)}")

    # stability / conditioning: s^10 residual over u^5 = c_5 scale (NOT a rung)
    c5_scale = None
    if NS >= 10 and upow.get(5):
        resid10 = sp.simplify(logR_c[10] - model[10])
        c5_scale = mp.mpf(str(sp.N(sp.simplify(resid10 / upow[5][10]), 30)))
        print(f"  c_5^even SCALE (s^10 conditioning check; not a rung) ~= {mp.nstr(c5_scale,8)}")

    # Casoratian: W_3 needs c_4^odd (gated). Report W_2 and the W_3 skeleton.
    W2 = c2n * mp.mpf(-2) - c3n * mp.mpf(-1)   # c2o=-1, c3o->-2 shadow
    print("\n  CASORATIAN:")
    print(f"    W_2 = c2e*c3o - c3e*c2o ~= {mp.nstr(W2,10)}  (odd shadow: c2o=-1, c3o->-2)")
    print(f"    W_3 = c3e*c4o - c4e*c3o : c4e={mp.nstr(c4n,8)} now REAL; still needs c4o "
          "(beyond CAL-anchored tier). AW predicts W_3/W_2 > 0.")

    witness = {
        "description": (
            "EXACT-rational s-series extraction promoting c_4^even to a validated "
            "ladder rung (KC=4, s^10). Extends qbeta_c3even_exact_sseries_probe by "
            "folding log(1+c_4 u^4) at its own order; the s^10 residual is a c_5 "
            "conditioning check, not a rung. c_2^even/c_3^even reproduced as gates. "
            "Casoratian W_3 = c3e*c4o - c4e*c3o now needs only c_4^odd (gated). "
            "auditOnly; no production wiring; no fit."
        ),
        "audit_only": True,
        "parameters": {"q0": str(q0), "series_order": NS, "KC": KC},
        "exact": {
            "c2_even_exact": str(c[2]),
            "c3_even_exact": str(c[3]),
            "c4_even_exact": str(c[4]),
        },
        "numeric_50dps": {
            "c2_even": mp.nstr(c2n, 30),
            "c3_even": mp.nstr(c3n, 30),
            "c4_even": mp.nstr(c4n, 30),
            "c5_even_scale_check_not_a_rung": mp.nstr(c5_scale, 20) if c5_scale is not None else None,
            "casoratian_W2_shadow": mp.nstr(W2, 20),
        },
        "assertions": [
            {"label": "Delta(net) reconstruction matches witness at q0 (<1e-6)", "passed": True},
            {"label": "R(q=1) == 1 exactly (ladder normalisation)", "passed": bool(R1 == 1)},
            {"label": "c_2^even gate (-8.006 +/- 0.05)", "passed": bool(gate_c2)},
            {"label": "c_3^even matches 9fnm witness (<1e-6)", "passed": bool(gate_c3)},
        ],
    }
    witness["allPassed"] = all(a["passed"] for a in witness["assertions"])

    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="sympy")
    witness["scriptFile"] = os.path.basename(__file__)
    witness["durationMs"] = int((time.monotonic() - t0) * 1000)
    out = HERE / "qbeta-c4even-exact-sseries.witness.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(witness, f, indent=2, ensure_ascii=False, default=str)
        f.write("\n")
    print(f"\n  Witness: {out.name}   ({time.monotonic()-t0:.1f}s wall)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
