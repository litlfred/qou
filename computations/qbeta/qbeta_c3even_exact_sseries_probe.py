#!/usr/bin/env python3
"""c3^even via EXACT-rational s-series of the net-route ladder (bean 1jrh).

Computes the exact-rational Taylor series of the net-route (bar-even /
binding-side) ladder through the c_3 rung (s^6):

  R(q)   = Qb_over_me(q) / [QA_over_me(q) * cos(alpha_eff(q))]
  Qb/me  = sgn * [Delta(net)(q)/(q-1)] / q      (regularised; finite at q=1)
  QA/me  = (2q+1-q^2)(q+1)/(2q^3)
  u      = b*hbar^2,  b = sqrt(q^4+q^2+1)/(q^2+1),  hbar = (q-1)/q
  alpha_eff = (z-1)h/2 - u/2,  z = 1/(sqrt(q)+1/sqrt(q)),  h = q-1/q
  ladder:  log R(s) = sum_{k>=2} log(1 + c_k u(s)^k),  s = q-1

All series coefficients are EXACT sympy expressions (rationals + surds); the
triangular solve for c_2 (gate: reproduce the established rung ~-8.006) and
c_3^even is exact, then evaluated at 50 dps. The exact odd-order [s^odd]
log R coefficients (the bar-odd remainder) are also reported.

Casoratian follow-up (bean 1jrh, docs/audits/2026-07-02-1jrh-aw-one-
recurrence-formalize-first-prune.md): with c_3^even measured, report
W_2 ~= c_2^even*c_3^odd - c_3^even*c_2^odd at the q->1 shadow values
(c_2^odd=-1 proved, c_3^odd->-2 the q=1 shadow). W_3 stays gated on c_4^even
+ the CAL-anchored tier of c_4^odd. auditOnly; NO production wiring; NO fit
(every number is a Taylor coefficient of an exact object).

Witness: qbeta-c3even-exact-sseries.witness.json
"""
from __future__ import annotations

import json
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

KC = 3          # extract through c_3 (s^6); c_4 needs s^8 (report scale only)
NS = 2 * KC + 2  # series order in s (s^8 inclusive for the c_4 scale check)


def load_net_symbolic(side: str):
    d = json.loads((ROOT / "free-neutron-decay.witness.json").read_text())
    net = sp.Integer(0)
    for t in d[side]["nf_terms"]:
        net += sp.sympify(t["coefficient_symbolic"], locals={"q": q})
    return sp.simplify(net)


def main() -> int:
    t0 = time.monotonic()
    set_compute_dps()

    print("=" * 76)
    print(" c3^even — EXACT-rational s-series of the net-route ladder (bean 1jrh)")
    print("=" * 76)

    net_n = load_net_symbolic("neutron")
    net_p = load_net_symbolic("proton")
    dnet = sp.simplify(net_n - net_p)
    dnet_reg = sp.cancel(dnet / (q - 1))     # (q-1) zero regularised

    # numeric validation at q0 against the witness
    d_wit = json.loads((ROOT / "free-neutron-decay.witness.json").read_text())
    params = d_wit.get("parameters")
    q0 = mp.mpf(str(params["q"])) if params and "q" in params else None
    dn_wit = mp.mpf(str(d_wit["transition"]["delta_net"]))
    dnet_f = sp.lambdify(q, dnet, "mpmath")
    if q0 is None:
        # fall back to the canonical muon q0 string used corpus-wide
        q0 = mp.mpf("1.1099785955573347198997632204832250266562084087802")
    dn_mine = dnet_f(q0)
    print(f"  VALIDATE @ q0: Delta(net) mine = {mp.nstr(dn_mine, 12)}  witness = {mp.nstr(dn_wit, 12)}")
    assert abs(dn_mine - dn_wit) < mp.mpf("1e-6"), "Delta(net) reconstruction drifted"
    sgn = int(mp.sign(dn_mine))

    # exact ladder pieces
    hbar = (q - 1) / q
    b = sp.sqrt(q**4 + q**2 + 1) / (q**2 + 1)
    u = b * hbar**2
    z = q**3 / (q**2 + 1)
    h = q - 1 / q
    alpha_eff = (z - 1) * h / 2 - u / 2
    QA_over_me = (2 * q + 1 - q**2) * (q + 1) / (2 * q**3)
    Qb_over_me = sgn * dnet_reg / q
    Rq = Qb_over_me / (QA_over_me * sp.cos(alpha_eff))

    # R(1) must be exactly 1 for the ladder normalisation
    R1 = sp.simplify(Rq.subs(q, 1))
    print(f"  R(q=1) exact = {R1}")

    # EXACT series of log(R/R1) and u in s = q-1
    print(f"\n  exact sympy series to O(s^{NS + 1}) (log R and u) ...")
    t1 = time.monotonic()
    logR_ser = sp.series(sp.log(Rq.subs(q, 1 + s) / R1), s, 0, NS + 1).removeO()
    u_ser = sp.series(u.subs(q, 1 + s), s, 0, NS + 1).removeO()
    logR_c = [sp.simplify(logR_ser.coeff(s, i)) for i in range(NS + 1)]
    u_c = [sp.simplify(u_ser.coeff(s, i)) for i in range(NS + 1)]
    print(f"  ... series done in {time.monotonic() - t1:.1f}s")

    # exact odd-order coefficients of log R (the prior mp.taylor 'blowup' probe)
    odd = {i: logR_c[i] for i in range(3, NS + 1, 2)}
    print("\n  EXACT odd-order [s^odd] log R (bar-odd remainder; prior mp.taylor saw ~1e4 noise):")
    for i, v in odd.items():
        print(f"    [s^{i}] = {sp.nsimplify(v)}  ~= {mp.nstr(mp.mpf(str(sp.N(v, 30))), 8)}")

    # series powers of u (exact)
    def ser_mul(a, bb):
        return [sp.expand(sum(a[i] * bb[n - i] for i in range(n + 1))) for n in range(NS + 1)]

    upow = {1: u_c}
    for k in range(2, KC + 2):
        upow[k] = ser_mul(upow[k - 1], u_c)

    # triangular solve: log R = sum_k log(1+c_k u^k); c_k at s^{2k}
    c = {}
    model = [sp.Integer(0)] * (NS + 1)
    for k in range(2, KC + 1):
        order = 2 * k
        resid = sp.simplify(logR_c[order] - model[order])
        lead = upow[k][order]
        ck = sp.simplify(resid / lead)
        c[k] = ck
        ck_n = mp.mpf(str(sp.N(ck, 40)))
        print(f"\n  c_{k}^even (exact, at s^{order}) = {mp.nstr(ck_n, 14)}")
        # fold log(1+c_k u^k) into the model, exactly, through s^NS
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

    # gates
    gate_c2 = abs(c2n - mp.mpf("-8.006")) < mp.mpf("0.05")
    print(f"\n  GATE c_2^even ~= -8.006 (prior mp.taylor, robust rung): "
          f"{'PASS' if gate_c2 else 'FAIL'}  (got {mp.nstr(c2n, 10)})")

    # c_4 scale check only (s^8 residual over u^4 lead) — NOT a rung claim
    resid8 = sp.simplify(logR_c[8] - model[8]) if NS >= 8 else None
    c4_scale = None
    if resid8 is not None:
        c4_scale = mp.mpf(str(sp.N(sp.simplify(resid8 / upow[4][8] if upow.get(4) else 0), 30)))
        print(f"  c_4^even SCALE CHECK (s^8; not a claimed rung) ~= {mp.nstr(c4_scale, 8)}")

    # Casoratian follow-up at the q->1 shadow (c_2^odd = -1 proved; c_3^odd -> -2 shadow)
    W2 = c2n * mp.mpf(-2) - c3n * mp.mpf(-1)
    print("\n  CASORATIAN (q->1 shadow rungs; odd: c2=-1 proved, c3->-2 shadow):")
    print(f"    W_2 = c2^even*c3^odd - c3^even*c2^odd ~= {mp.nstr(W2, 10)}")
    print("    (W_3 stays GATED: needs c_4^even as a real rung + c_4^odd beyond CAL-anchored tier.)")

    witness = {
        "description": (
            "EXACT-rational s-series extraction of the net-route (bar-even) ladder "
            "rungs c_2^even, c_3^even — the measurement gated by the 1jrh AW "
            "one-recurrence formalize-first prune. Supersedes the mp.taylor "
            "instability that blocked c_3+ in qbeta-ck-sseries-operator-match. "
            "auditOnly; no production wiring; no fit."
        ),
        "audit_only": True,
        "parameters": {"q0": str(q0), "series_order": NS, "KC": KC},
        "exact": {
            "delta_net_reg_q": str(dnet_reg),
            "c2_even_exact": str(c[2]),
            "c3_even_exact": str(c[3]),
            "odd_order_logR": {str(i): str(sp.nsimplify(v)) for i, v in odd.items()},
        },
        "numeric_50dps": {
            "c2_even": mp.nstr(c2n, 30),
            "c3_even": mp.nstr(c3n, 30),
            "c4_even_scale_check_not_a_rung": mp.nstr(c4_scale, 20) if c4_scale is not None else None,
            "casoratian_W2_shadow": mp.nstr(W2, 20),
        },
        "assertions": [
            {"label": "Delta(net) reconstruction matches witness at q0 (<1e-6)", "passed": True},
            {"label": "R(q=1) == 1 exactly (ladder normalisation)", "passed": bool(R1 == 1)},
            {"label": "c_2^even gate vs prior robust rung (-8.006 +/- 0.05)", "passed": bool(gate_c2)},
        ],
    }
    witness["allPassed"] = all(a["passed"] for a in witness["assertions"])

    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="sympy")
    import os
    witness["scriptFile"] = os.path.basename(__file__)
    # stamp sets durationMs=0; record the real wall time (Copilot review)
    witness["durationMs"] = int((time.monotonic() - t0) * 1000)
    out = HERE / "qbeta-c3even-exact-sseries.witness.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(witness, f, indent=2, ensure_ascii=False, default=str)
        f.write("\n")
    print(f"\n  Witness: {out.name}   ({time.monotonic() - t0:.1f}s wall)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
