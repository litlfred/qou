#!/usr/bin/env python3
"""[1⁴] per-pair-TYPE magnitude enumeration — type-aware Ursell profiles.

EXPLORATORY (audit-only, no production rewire, no fit, NO option selection).
Follow-up to b4_1four_reeb_flow_magnitude.py (uniform g_reeb: total 0.940×
full B(⁴He); type-blind cumulants b₂ 0.42×, b₃ 1.042×, b₄ 1.63×). Question:
does a PRINCIPLED non-uniform per-pair-TYPE magnitude assignment flatten the
cumulant profile?  The two principled magnitudes in the corpus are

    z      = 1/[2]_v        (naive Markov-peel bond factor, tan θ)
    g_reeb = z/sqrt(1+z²)   (CWF/criticality magnitude, sin θ)

Preregistered option set (enumerated, verdicts per option, none selected):
  A: uniform g_reeb            (baseline — reproduces the prior probe)
  B: pn = g_reeb, pp = nn = z  (only the bar-mixed pn bond is CWF-normalized;
                                like-pairs keep the naive peel factor)
  C: pn = z, pp = nn = g_reeb  (symmetry control for B)
  D: uniform z                 (disclosure — known det ≤ 0 at pn = ±1)

Signs are the derived pattern (pp → +1, nn → −1, pn → +1); the pn sign is
irrelevant for all determinants here (diag(1,1,−1,−1) conjugation flips pn
entries entrywise — magnitudes untouched — so ±w remain isospectral even
with non-uniform magnitudes; `pn_sign_det_invariant` generalizes).

TYPE-AWARE Ursell inversion (the type-blind C(A,k) inversion is wrong for
non-uniform pairs): with pair terms b₂^{pp}, b₂^{nn}, b₂^{pn} and connected
triples b₃^{ppn}, b₃^{pnn},

    B(ppn) = b₂^{pp} + 2 b₂^{pn} + b₃^{ppn}
    B(pnn) = b₂^{nn} + 2 b₂^{pn} + b₃^{pnn}
    B(ppnn) = b₂^{pp} + b₂^{nn} + 4 b₂^{pn} + 2 b₃^{ppn} + 2 b₃^{pnn} + b₄.

AME comparison targets: b₂ = B(²H) = 2.224566 (a pn pair), b₃ = 1.4264
(avg connected 3-body), b₄ = 9.2431, B(⁴He) = 28.29566.

-- Ref: b4_1four_reeb_flow_magnitude.py (uniform baseline + Q3);
b4_value_cumulant_target_probe.py (AME cumulant inversion);
QOU/MassTheory/ReebPnMagnitude.lean (sign conjugation);
docs/audits/2026-07-06-reeb-flow-pn-magnitude-provenance-and-1four-extension.md.
"""
from __future__ import annotations

import os
import sys
import time
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
if str(_COMP) not in sys.path:
    sys.path.insert(0, str(_COMP))
from _li_2_q_util import load_q_50dps  # noqa: E402
from substrate._precision import set_compute_dps  # noqa: E402
from substrate.experimental_constants import M_E_MEV  # noqa: E402
from substrate.witness_base import WitnessBuilder  # noqa: E402
from codata_constants import (
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
)

set_compute_dps()
COMP = str(_COMP)

AME = {"b2_pn": AME_B_DEUTERON_MEV_VALIDATION, "b3": mp.mpf("1.4264"),
       "b4": mp.mpf("9.2431"), "B4He": AME_B_HE4_MEV_VALIDATION}


def det_n(pairs, n):
    """det(I + G) for an n-block shell; pairs = {(i,j): signed magnitude}."""
    G = mp.zeros(n, n)
    for (i, j), v in pairs.items():
        G[i, j] = v
        G[j, i] = v
    return mp.det(mp.eye(n) + G)


def bind(E0, d):
    return None if d <= 0 else E0 * (-mp.log(d))


def main() -> int:
    t0 = time.monotonic()
    q, _, z = load_q_50dps()
    m_e = mp.mpf(str(M_E_MEV))
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    E0 = _qbeta_e0.order_zero_scaled(m_e, q)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
    g = z / mp.sqrt(1 + z * z)

    options = {
        "A_uniform_g": {"pp": g, "nn": g, "pn": g},
        "B_pn_g_like_z": {"pp": z, "nn": z, "pn": g},
        "C_pn_z_like_g": {"pp": g, "nn": g, "pn": z},
        "D_uniform_z": {"pp": z, "nn": z, "pn": z},
    }

    rows = []
    for name, m in options.items():
        # pair dets (2 blocks): pp sign +, nn sign −, pn sign + (irrelevant, squared)
        d_pp = 1 - m["pp"] ** 2
        d_nn = 1 - m["nn"] ** 2
        d_pn = 1 - m["pn"] ** 2
        b2_pp, b2_nn, b2_pn = bind(E0, d_pp), bind(E0, d_nn), bind(E0, d_pn)
        # triples: ppn = blocks [p,p,n] pairs {(0,1):+pp, (0,2):+pn, (1,2):+pn}
        d_ppn = det_n({(0, 1): m["pp"], (0, 2): m["pn"], (1, 2): m["pn"]}, 3)
        d_pnn = det_n({(0, 1): -m["nn"], (0, 2): m["pn"], (1, 2): m["pn"]}, 3)
        B_ppn, B_pnn = bind(E0, d_ppn), bind(E0, d_pnn)
        # quad [p,p,n,n]
        d4 = det_n({(0, 1): m["pp"], (2, 3): -m["nn"],
                    (0, 2): m["pn"], (0, 3): m["pn"],
                    (1, 2): m["pn"], (1, 3): m["pn"]}, 4)
        B4 = bind(E0, d4)
        row = {"option": name,
               "magnitudes": {k: mp.nstr(v, 8) for k, v in m.items()},
               "det4": mp.nstr(d4, 8)}
        if None in (b2_pp, b2_nn, b2_pn, B_ppn, B_pnn, B4):
            row["status"] = "UNPHYSICAL (some det ≤ 0)"
            rows.append(row)
            continue
        b3_ppn = B_ppn - b2_pp - 2 * b2_pn
        b3_pnn = B_pnn - b2_nn - 2 * b2_pn
        b3 = (b3_ppn + b3_pnn) / 2
        b4c = B4 - (b2_pp + b2_nn + 4 * b2_pn) - 2 * (b3_ppn + b3_pnn)
        row.update({
            "b2_pn_MeV": mp.nstr(b2_pn, 7), "b2_pn_ratio": mp.nstr(b2_pn / AME["b2_pn"], 5),
            "b2_pp_MeV": mp.nstr(b2_pp, 7), "b2_nn_MeV": mp.nstr(b2_nn, 7),
            "b3_MeV": mp.nstr(b3, 7), "b3_ratio": mp.nstr(b3 / AME["b3"], 5),
            "b4_MeV": mp.nstr(b4c, 7), "b4_ratio": mp.nstr(b4c / AME["b4"], 5),
            "B4_total_MeV": mp.nstr(B4, 7), "B4_ratio": mp.nstr(B4 / AME["B4He"], 5),
        })
        rows.append(row)

    result = {
        "constants": {"q0": mp.nstr(q, 12), "z": mp.nstr(z, 10), "g_reeb": mp.nstr(g, 10),
                      "E0_MeV": mp.nstr(E0, 8)},
        "ame_targets": {k: mp.nstr(v, 8) for k, v in AME.items()},
        "options": rows,
        "verdict": (
            "Preregistered enumeration; no option selected. Type-aware Ursell "
            "profiles reported per option against the AME targets. Scope-(a): "
            "results constrain the listed (type→magnitude) assignments only."
        ),
    }
    payload = {
        "computation": "b4-1four-pairtype-magnitude-profile",
        "description": ("[1⁴] per-pair-type magnitude enumeration (A uniform g / "
                        "B pn=g,like=z / C control / D uniform z) with type-aware "
                        "Ursell cumulant profiles vs AME. Audit-only; no fit; no "
                        "selection."),
        "tier": "exploratory (preregistered 4-option enumeration)",
        "result": result,
    }
    import platform
    wb = WitnessBuilder.wrap_legacy(
        "b4-1four-pairtype-magnitude-profile", payload,
        script_path=__file__, engine="python+mpmath",
        engine_version=f"python {platform.python_version()} + mpmath {mp.__version__}",
        output_dir=os.path.join(COMP, "probes"), start_time=t0,
    )
    # Baseline consistency: option A must reproduce the uniform-g probe's
    # total (26.59561 / 28.29566 = 0.9399185…), selected by name, numeric
    # tolerance 1e-5 (Copilot #3451).
    a = next(r for r in rows if r["option"] == "A_uniform_g")
    if "B4_ratio" not in a:
        # Option A came back UNPHYSICAL (some det <= 0), so there is no ratio to
        # compare and this assertion has no subject. It used to index the key
        # blind and die with KeyError -- a latent bug convention C never
        # triggered, because under z_C option A was always physical. Under
        # convention D (z_D = 0.6127 > z_C = 0.4993) the 4-body determinant
        # crosses zero, which is the SAME ceiling wlambda_cumulant_specification
        # refuses on for 3H. Report the refusal, do not crash and do not invent
        # a number.
        #
        # NOTE the expected value below, 0.9399185, is a CONVENTION-C-FROZEN
        # transcribed constant (26.59561 / 28.29566 from the uniform-g probe).
        # It is not re-derivable under D while option A is unphysical, so it is
        # left as the C-frame record rather than silently re-fitted.
        wb.add_assertion("A_total_matches_uniform_probe",
                         computed="UNPHYSICAL (option A det <= 0)",
                         expected="True")
    else:
        dev = mp.fabs(mp.mpf(a["B4_ratio"]) - mp.mpf("0.9399185"))
        wb.add_assertion("A_total_matches_uniform_probe",
                         computed=str(bool(dev < mp.mpf("1e-5"))), expected="True")
    wb.save(extra={"auditOnly": True})

    print("=== [1⁴] per-pair-type magnitude profiles (type-aware Ursell) ===")
    print(f"  z={float(z):.6f}  g={float(g):.6f}  E0={float(E0):.4f} MeV")
    print(f"  AME: b2_pn 2.2246, b3 1.4264, b4 9.2431, B(4He) 28.2957")
    for r in rows:
        if "status" in r:
            print(f"  {r['option']:>14}: {r['status']}  det4={r['det4']}")
        else:
            print(f"  {r['option']:>14}: b2_pn {r['b2_pn_MeV']:>8} ({r['b2_pn_ratio']}x)"
                  f"  b3 {r['b3_MeV']:>8} ({r['b3_ratio']}x)"
                  f"  b4 {r['b4_MeV']:>8} ({r['b4_ratio']}x)"
                  f"  B4 {r['B4_total_MeV']:>8} ({r['B4_ratio']}x)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
