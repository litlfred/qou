#!/usr/bin/env python3
"""delta_tr_attribution.py — exact attribution of the probe-d Delta_tr move (bean qou-xj4p).

`probe_d_dressing_is_proton_net.py` uses Delta_tr = tr_M(free) - tr_M(atom) for the
deuteron (Z=N=1). Its committed witness (computed 2026-07-04, PR #3295, commit
581c176f480 on main = recorded commitSha 4dfe838c398) carries 0.59516889262234348652;
the producer on main now gives 0.14704667798040846911.

This script walks the four inputs that changed between those two runs, one at a time,
along a fixed path, and records each step's exact contribution (mpmath, 70 dps, no
float64 arithmetic anywhere):

  0. OLD configuration, reconstructed on main: grouped confinement core,
     Jones-Markov y_lambda in convention C evaluated at the RETIRED muon pin
     (what the 2026-07-04 run actually read, from the then-muon-built
     y-lambda-at-q0 cache), chi^lambda at the 50-digit proton q0 on a word whose
     interface d was built from the float64 proton q0.
  1. (b) q0 pin of y_lambda: retired muon -> proton (removes the layer straddle).
  2. (a) Markov convention: C (z = sqrt q/(q+1)) -> D (z = q^3/(q^2+1)).
  3. (c) precision: interface d built from the float64 q0 -> from the 70-digit q0
     (measured in a 581c176f480 worktree; recorded, ~1e-20).
  4. word ruling 2026-09-05 (qou-hu1f): grouped -> alternating (borromean) core.

Step 0 must reproduce the committed witness value; the final step must reproduce the
producer's live value. Both are checked. Muon pins at CODATA 2018 / 2022 are reported
for completeness (candidate b).

AUDIT-ONLY. Does not touch the probe, its assertion, or its witness.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMP = next(p for p in HERE.parents if p.name == "computations")
sys.path.insert(0, str(COMP))
sys.path.insert(0, str(COMP / "substrate"))

import mpmath as mp  # noqa: E402

mp.mp.dps = 70

import tr_m_atom_via_transfer as T  # noqa: E402
from chi_general_word import chi_all_lambda_any  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from schur_principal_mpmath import (  # noqa: E402
    y_lambda_at_q0_mpmath_convention_C_HISTORICAL as y_C,
)
from q_parameter import Q_50_DIGIT_STR, Q_MP, Q_MUON_50_DIGIT_STR  # noqa: E402
from qou_substrate.constants import MASS_RATIO_MU_E_STR  # noqa: E402  (CODATA 2022)

# The committed (2026-07-04) witness is still the one on main: read its Delta_tr
# rather than copying the literal.
PROBE_WITNESS = COMP / "probes" / "probe-d-dressing-is-proton-net.witness.json"
OLD_WITNESS = mp.mpf(json.loads(PROBE_WITNESS.read_text())["data"]["numerical"]["Delta_tr"])

Q_PROTON = Q_MP  # the 70-digit proton q0 tr_m_atom_zn itself uses for y_lambda
# The retired (frozen, pre-2026-08-22) muon pin. The 2026-06-22 y-lambda-at-q0 cache
# that the 2026-07-04 run read carried it as parameters.q_0 to 60 digits, which agree
# with Q_MUON_50_DIGIT_STR to 49 digits; the difference moves Delta_tr below 1e-45.
Q_MUON_RETIRED = mp.mpf(Q_MUON_50_DIGIT_STR)
# Candidate (c), the float64 word: the 2026-07-04 word builder computed the
# interface coefficients d from the float64 q0 (d = -0.1045301493978196827 vs
# -0.1045301493978196577 now). Main's builder cannot rebuild that word (it rejects
# or re-lifts a float64 q), so this step was measured in a worktree at 581c176f480
# by swapping chi tables between the two trees (RESULTS.md); its value is recorded
# here, not recomputed.
C_PRECISION_MEASURED = mp.mpf("-1.35e-20")
VOL41 = 2 * mp.clsin(2, mp.pi / 3)


def q_muon(ratio: str) -> mp.mpf:
    return 1 / (1 - mp.sqrt(VOL41 / mp.mpf(ratio)))


def y_D(n, q):
    return {tuple(k): mp.mpf(str(v)) for k, v in y_lambda_at(n, q).items()}


def chis(intra: str, q_word, allow_float64: bool = False):
    """chi^lambda(atom), chi^lambda(free) at the 70-digit proton q0, on a word whose
    interface coefficients are built at q_word (None = the canonical 70-digit q0)."""
    out = []
    for inter in (True, False):
        w = atom_braid_word_3A(1, 1, include_inter=inter, intra_order=intra, q=q_word,
                               allow_float64=allow_float64)
        out.append(chi_all_lambda_any(w, 6))
    return out


def dtr(y, ca, cf):
    return mp.fsum(y[k] * (cf.get(k, mp.mpf(0)) - ca.get(k, mp.mpf(0))) for k in y)


def main() -> int:
    ca_g, cf_g = chis("grouped", None)
    ca_b, cf_b = chis("borromean", None)

    path = [
        ("0 old: C, y@muon_retired, grouped",
         dtr(y_C(6, Q_MUON_RETIRED), ca_g, cf_g)),
        ("1 (b) y pin muon_retired -> proton",
         dtr(y_C(6, Q_PROTON), ca_g, cf_g)),
        ("2 (a) convention C -> D",
         dtr(y_D(6, Q_PROTON), ca_g, cf_g)),
        ("3 word ruling grouped -> borromean",
         dtr(y_D(6, Q_PROTON), ca_b, cf_b)),
    ]
    live_tr = T.tr_m_atom_zn(1, 1, dps=70)
    live = mp.mpf(live_tr[1]) - mp.mpf(live_tr[0])

    total = path[-1][1] - path[0][1]
    steps = []
    print(f"{'step':45s} {'Delta_tr':>28s} {'contribution':>26s} {'share':>10s}")
    for i, (name, v) in enumerate(path):
        c = v - path[i - 1][1] if i else mp.mpf(0)
        share = c / total if i else mp.mpf(0)
        steps.append({"step": name, "Delta_tr": mp.nstr(v, 30),
                      "contribution": mp.nstr(c, 25) if i else "0",
                      "share_of_total_move": mp.nstr(share, 12) if i else "0"})
        print(f"{name:45s} {mp.nstr(v, 25):>28s} {mp.nstr(c, 18):>26s} {mp.nstr(share, 8):>10s}")

    log_total = mp.log(path[-1][1] / path[0][1])
    log_shares = {path[i][0]: mp.nstr(mp.log(path[i][1] / path[i - 1][1]) / log_total, 12)
                  for i in range(1, len(path))}

    # Candidate (b) completeness: y_lambda at the other muon pins, both conventions,
    # grouped word at the 70-digit q0.
    pins = {"muon_retired": Q_MUON_RETIRED,
            "muon_codata2018": q_muon("206.7682830"),  # CODATA 2018 (historical, superseded)
            "muon_codata2022": q_muon(MASS_RATIO_MU_E_STR),
            "proton": Q_PROTON}
    pin_table = {}
    for pn, qv in pins.items():
        pin_table[pn] = {"C": mp.nstr(dtr(y_C(6, qv), ca_g, cf_g), 25),
                         "D": mp.nstr(dtr(y_D(6, qv), ca_g, cf_g), 25)}
    # Order-independence check: the convention step taken at the muon pin.
    conv_at_muon = (dtr(y_D(6, Q_MUON_RETIRED), ca_g, cf_g)
                    - dtr(y_C(6, Q_MUON_RETIRED), ca_g, cf_g))
    # Word ruling taken under convention C (order dependence of steps 2/4).
    word_under_C = dtr(y_C(6, Q_PROTON), ca_b, cf_b) - dtr(y_C(6, Q_PROTON), ca_g, cf_g)

    checks = {
        # The committed value minus step 0 is exactly the (c) float64-word step
        # (measured separately, see C_PRECISION_MEASURED): ~1.3e-20, below the
        # witness's 20 recorded digits. So step 0 matches the witness to 1e-19 and
        # the 20th-digit residual is (c), not an unattributed remainder.
        "step0_reproduces_committed_witness_1e-19":
            bool(abs(path[0][1] - OLD_WITNESS) < mp.mpf("1e-19")),
        "step0_minus_witness_matches_measured_c_step":
            bool(abs((OLD_WITNESS - path[0][1]) + C_PRECISION_MEASURED) < mp.mpf("1e-20")),
        "step4_equals_live_tr_m_atom_zn":
            bool(abs(path[-1][1] - live) < mp.mpf("1e-55")),
    }
    for k, v in checks.items():
        print(f"  {k}: {v}")
    print(f"  convention step taken at muon_retired: {mp.nstr(conv_at_muon, 18)}")
    print(f"  word-ruling step taken under convention C: {mp.nstr(word_under_C, 18)}")
    print("  log shares:", log_shares)

    out = {
        "c_precision_step_measured_in_old_tree": mp.nstr(C_PRECISION_MEASURED, 5),
        "computation": "probe-d-delta-tr-attribution",
        "engine": "mpmath",
        "scriptFile": Path(__file__).name,
        "commitSha": subprocess.run(["git", "rev-parse", "HEAD"], cwd=HERE,
                                    capture_output=True, text=True).stdout.strip(),
        "bean": "qou-xj4p",
        "auditOnly": True,
        "q0Anchor": "proton",
        "q0Value": Q_50_DIGIT_STR,
        "note": "q0Anchor is the chi^lambda evaluation point; step 0 deliberately "
                "evaluates y_lambda at the retired muon pin to reconstruct the "
                "2026-07-04 layer straddle.",
        "compute_dps": 70,
        "old_witness_Delta_tr": mp.nstr(OLD_WITNESS, 20),
        "live_tr_m_atom_zn_Delta_tr": mp.nstr(live, 30),
        "path": steps,
        "log_shares": log_shares,
        "pin_table_grouped_word": pin_table,
        "convention_step_at_muon_retired": mp.nstr(conv_at_muon, 25),
        "word_ruling_step_under_convention_C": mp.nstr(word_under_C, 25),
        "checks": checks,
        "allPassed": all(checks.values()),
    }
    (HERE / "delta-tr-attribution.witness.json").write_text(json.dumps(out, indent=1) + "\n")
    return 0 if out["allPassed"] else 1


if __name__ == "__main__":
    sys.exit(main())
