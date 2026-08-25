#!/usr/bin/env python3
"""Route-alpha prediction test: the basic-construction lift Lambda_a (bean 1jrh).

Evaluates the FULLY FORCED route-alpha candidate from
docs/scope/2026-07-02-1jrh-lambda-derivation-routes.md:

  Lambda_a = iota(DeltaT) * e_3,   e_3 = (q*1 - sigma_3)/(q + q^-1)

where DeltaT = sum_w c_w(q) T_w is the free-neutron-decay net transition
operator (6-word H3 NF basis, exact symbolic coefficients from
free-neutron-decay.witness.json) and e_3 is the Temperley-Lieb/Jones
projector on the new strand — the Jones basic construction for H3 in H4.
Zero free parameters; its level-4 content is a PREDICTION, never a fit.

Quantities (all via the merged Stage-C infra, PR #3228):
  P1. per-word Markov ratios zeta_w = tr_M^{H4}(w+(s3,)) / tr_M^{H3}(w) —
      word-independence is the Markov property for the third strand and
      decides route alpha structurally.
  P2. level-4 content  L4 = tr_M^{H4}(Lambda_a) - tau(e_3)*tr_M^{H3}(DeltaT),
      tau(e_3) = (q - zeta)/(q + q^-1), evaluated at BOTH anchors
      (proton q_at, muon q_muon_at) — the L3 anchor-stability gate.

Discipline: no fitting, only CAL 1-3 inputs (the decay witness + q0 anchors);
the outcome is reported as a scope-(a) statement either way. auditOnly.

Witness: qbeta-route-alpha-lift-prediction.witness.json
"""
from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path

import sympy as sp
from mpmath import mp

HERE = Path(__file__).resolve().parent            # computations/qbeta
ROOT = HERE.parent                                 # computations/
REPO = ROOT.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "substrate"))
sys.path.insert(0, str(ROOT / "habiro"))
sys.path.insert(0, str(REPO / "tools" / "qou-substrate" / "python"))

from qbeta_h4_stagec_markov_infra import tr_M  # noqa: E402  (merged #3228)
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

qs = sp.symbols("q", positive=True)


def load_net_words():
    """Per-word EXACT net coefficients c_w(q) = neutron - proton (sympy)."""
    d = json.loads((ROOT / "free-neutron-decay.witness.json").read_text())
    words, coeffs = [], []
    terms_n = d["neutron"]["nf_terms"]
    terms_p = d["proton"]["nf_terms"]
    assert [t["word"] for t in terms_n] == [t["word"] for t in terms_p]
    for tn, tp in zip(terms_n, terms_p):
        cn = sp.sympify(tn["coefficient_symbolic"], locals={"q": qs})
        cp = sp.sympify(tp["coefficient_symbolic"], locals={"q": qs})
        words.append(tuple(tn["word"]))
        coeffs.append(sp.simplify(cn - cp))
    return words, coeffs, mp.mpf(str(d["transition"]["delta_net"]))


def main() -> int:
    t0 = time.monotonic()
    set_compute_dps()
    tol = mp.mpf("1e-40")

    from qou_substrate.constants import q_at, q_muon_at  # noqa: E402
    q_proton = q_at(50)
    q_muon = q_muon_at(50)
    anchors = [("proton", mp.mpf(str(q_proton))), ("muon", mp.mpf(str(q_muon)))]
    extra_q = [mp.mpf("1.05"), mp.mpf("1.2"), mp.mpf("0.93")]

    words, coeffs, dnet_wit = load_net_words()
    c_fns = [sp.lambdify(qs, c, "mpmath") for c in coeffs]

    print("=" * 76)
    print(" Route-alpha prediction: Lambda_a = iota(DeltaT)*e_3 (bean 1jrh)")
    print("=" * 76)
    print(f"  anchors: proton q0 = {mp.nstr(anchors[0][1], 22)}")
    print(f"           muon   q0 = {mp.nstr(anchors[1][1], 22)}"
          f"   (split {mp.nstr((anchors[0][1]/anchors[1][1]-1)*mp.mpf('1e9'), 4)} ppb)")

    assertions = []

    # GATE 0 — DeltaT reconstruction vs the decay witness (counit = coeff sum)
    dn0 = mp.fsum(f(anchors[0][1]) for f in c_fns)
    print(f"\n  GATE 0  Delta(net) @ proton q0: mine {mp.nstr(dn0, 12)}  "
          f"witness {mp.nstr(dnet_wit, 12)}")
    assertions.append({"label": "0: DeltaT net reconstruction matches witness (<1e-6)",
                       "passed": bool(abs(dn0 - dnet_wit) < mp.mpf("1e-6"))})

    # P1 — per-word Markov ratios zeta_w at every q point (the structural gate)
    print("\n  P1  zeta_w = tr_M^H4(w+(s3,))/tr_M^H3(w) — word-independence:")
    worst_markov = mp.mpf(0)
    zeta_at = {}
    for name, qv in anchors + [(f"q={mp.nstr(x, 4)}", x) for x in extra_q]:
        zetas = []
        for w in words:
            z = tr_M(4, w + (2,), qv) / tr_M(3, w, qv)
            zetas.append(z)
        dev = max(abs(z - zetas[0]) for z in zetas)
        worst_markov = max(worst_markov, dev)
        zeta_at[name] = zetas[0]
        print(f"    {name:>8}: zeta = {mp.nstr(zetas[0], 15)}   max word-dev {mp.nstr(dev, 3)}")
    markov_holds = worst_markov < tol
    assertions.append({"label": "P1: Markov property on third strand — zeta word-independent (<1e-40)",
                       "passed": bool(markov_holds)})

    # P2 — level-4 content of Lambda_a at both anchors
    #   tr_M^H4(Lambda_a) = sum_w c_w * [q*tr_M^H4(w) - tr_M^H4(w+(s3,))]/(q+1/q)
    #   shadow            = tau(e_3) * tr_M^H3(DeltaT),  tau(e_3) = (q - zeta)/(q+1/q)
    print("\n  P2  level-4 content L4(Lambda_a) at both anchors:")
    L4 = {}
    swing = None
    for name, qv in anchors:
        denom = qv + 1 / qv
        cvals = [f(qv) for f in c_fns]
        tr4 = mp.fsum(c * (qv * tr_M(4, w, qv) - tr_M(4, w + (2,), qv)) / denom
                      for c, w in zip(cvals, words))
        tr3 = mp.fsum(c * tr_M(3, w, qv) for c, w in zip(cvals, words))
        tau_e3 = (qv - zeta_at[name]) / denom
        L4[name] = tr4 - tau_e3 * tr3
        print(f"    {name:>8}: tr_M^H4(Lambda_a) = {mp.nstr(tr4, 15)}")
        print(f"              tau(e_3)*tr_M^H3(DeltaT) = {mp.nstr(tau_e3 * tr3, 15)}"
              f"   (tr3 = {mp.nstr(tr3, 12)}, tau(e_3) = {mp.nstr(tau_e3, 12)})")
        print(f"              L4 = {mp.nstr(L4[name], 6)}")
    both_zero = all(abs(v) < tol for v in L4.values())
    assertions.append({"label": "P2: level-4 content of Lambda_a vanishes at BOTH anchors (<1e-40)",
                       "passed": bool(both_zero)})
    if not both_zero and all(abs(v) > 0 for v in L4.values()):
        swing = abs(L4["proton"] / L4["muon"] - 1)
        print(f"    anchor swing |L4_p/L4_mu - 1| = {mp.nstr(swing, 6)}")

    # Verdict (scope-(a) phrasing either way; no fit anywhere)
    print()
    if markov_holds and both_zero:
        print("  VERDICT: the basic-construction lift is TRACE-TRANSPARENT — the")
        print("  Markov property makes e_3-dressing invisible to tr_M, so route alpha")
        print("  PREDICTS level-4 content = 0 exactly (c_4 rung = 0 on this route).")
        print("  Anchor-stable trivially (0 at both anchors). Scope-(a): a nonzero")
        print("  c_4 therefore requires NON-TRIVIAL defect coupling (routes beta/gamma).")
    else:
        print("  VERDICT: Lambda_a carries nonzero level-4 content — see L4 + swing.")

    # exit code gates on the LAW assertions (0 + P1); allPassed covers ALL
    # assertions so downstream witness tooling sees any failure (incl. P2).
    laws_ok = all(a["passed"] for a in assertions[:2])
    all_ok = all(a["passed"] for a in assertions)
    witness = {
        "description": (
            "Route-alpha prediction test (bean 1jrh / Stage C): the forced basic-"
            "construction lift Lambda_a = iota(DeltaT)*e_3 evaluated through the "
            "merged H4 Markov-trace infra at BOTH q0 anchors (proton q_at, muon "
            "q_muon_at). P1 measures the Markov property on the third strand "
            "(zeta_w word-independence); P2 measures the level-4 content "
            "tr_M^H4(Lambda_a) - tau(e_3)*tr_M^H3(DeltaT). Zero free parameters; "
            "no fit; outcome recorded scope-(a). auditOnly."
        ),
        "audit_only": True,
        "parameters": {
            "q_proton": mp.nstr(anchors[0][1], 50),
            "q_muon": mp.nstr(anchors[1][1], 50),
            "dps": mp.dps,
            "extra_q_points": [str(x) for x in extra_q],
            "nf_words": [list(w) for w in words],
        },
        "data": {
            "delta_net_at_proton_q0": mp.nstr(dn0, 30),
            "zeta_at_anchors": {k: mp.nstr(v, 30) for k, v in zeta_at.items()},
            "worst_markov_word_dev": mp.nstr(worst_markov, 6),
            "L4_level4_content": {k: mp.nstr(v, 30) for k, v in L4.items()},
            "anchor_swing": mp.nstr(swing, 10) if swing is not None else None,
            "markov_transparent": bool(markov_holds and both_zero),
        },
        "assertions": assertions,
        "allPassed": bool(all_ok),
    }

    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="mpmath")
    witness["scriptFile"] = os.path.basename(__file__)
    witness["durationMs"] = int((time.monotonic() - t0) * 1000)
    out = HERE / "qbeta-route-alpha-lift-prediction.witness.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(witness, f, indent=2, ensure_ascii=False, default=str)
        f.write("\n")
    print(f"\n  Witness: {out.name}   ({time.monotonic() - t0:.1f}s wall)")
    return 0 if laws_ok else 1


if __name__ == "__main__":
    sys.exit(main())
