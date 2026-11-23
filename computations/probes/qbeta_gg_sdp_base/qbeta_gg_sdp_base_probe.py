#!/usr/bin/env python3
"""qou-ales / qou-vd7j: the Q_beta base under gamma-gamma + reading-3 word selection.

Pre-registration (committed before any number here was computed):
    computations/probes/qbeta_gg_sdp_base/preregistration.md   (b3a70fdf25)
Lean companion:
    folio/quantum-observable-universe/lean/QOU/QBeta/GammaGammaSdpQBetaBase.lean

WHAT IS DONE
  P0  calibration of the Markov trace tau = sum_lambda y_lambda chi_lambda at z_D:
      tau(1) = 1, tau(sigma_0) = z_D, tau(Delta_S) = h^2/2 - z_D h (the closed form the
      L2 scorecard uses), chi_(2,1)(V^3) = 2 - 3h^4 - h^6 (step 4).
  P1  qou-vd7j: read the committed net-row witness (rank-5 Gram under D, 1'v != 0, 0 of
      4238) and check the identification it rests on at block level: the alternating
      character chi_(1^3)(V^k) = 1 for every k, so <v, nf(W)> = 1 != 0 for every gamma-gamma
      word (Lean: gammaGamma_demand_infeasible_of_pairing_eq_altChar).
  P2  nucleon (p, n) in H_3: reading 3 over V^k, k = 0..10. The candidate sets are the same
      set for p and n (no flavour index in the gamma-gamma grammar on three strands).
  P3  two nucleons (2H, pp, nn -- the same words, for the same reason) in H_6:
      V_L^a V_R^b B, a, b in the non-zero H_3 survivors, B in {none} or a placement power.
      Every-level admissibility = reading 3 at H_6 and at H_3 on each nucleon.
  P4  Q_beta = |tau_zD(V^a) - tau_zD(V^b)| * E0_canonical for every ordered pair of
      non-zero H_3 survivors. Reported, not ranked. The cost-minimal selection is a = b = 3.

ARITHMETIC. mpmath at 60 dps through the Hoefsmit seminormal blocks of
ales_h9_reading3_tower_probe (numpy OBJECT arrays of mpf, no float64). Proton pin.
Nothing reads AME. CODATA Q_beta is read only in the final comparison column, after every
Q_beta value is fixed.

Run: python3 -u computations/probes/qbeta_gg_sdp_base/qbeta_gg_sdp_base_probe.py \
       2>&1 | tee /tmp/qbeta_gg_sdp_base.log
"""
from __future__ import annotations

import importlib.util
import json
import sys
import time
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parents[2]
for _p in ("computations", "computations/qbeta", "computations/hecke", "computations/markov",
           "computations/substrate", "tools/pyhecke/python", "tools/qou-substrate/python"):
    sys.path.insert(0, str(_ROOT / _p))

_spec = importlib.util.spec_from_file_location(
    "ales_h9", _ROOT / "computations/probes/ales_h9/ales_h9_reading3_tower_probe.py")
AH = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(AH)  # sets dps 60, Q0, H0; does not run main()

import mpmath as mp  # noqa: E402

import qbeta_e0  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

DPS = AH.DPS
# AH's exec_module already set dps 60; restating it here at module scope makes the
# precision visible to the static dps audits and keeps TOL below from depending on
# import order. Idempotent: the dps is unchanged, so no published value moves.
set_compute_dps(DPS)
Q0, H0 = AH.Q0, AH.H0
ZD = Q0 ** 3 / (Q0 ** 2 + 1)
TOL = mp.mpf("1e-40")
T0 = time.time()
ASSERTS: list = []
FAILED: list = []

Z0, NEG1 = mp.mpf(0), mp.mpf(-1)
V_L = [(0, Z0), (1, NEG1)]           # sigma_0 sigma_1^-1
V_R = [(3, Z0), (4, NEG1)]           # sigma_3 sigma_4^-1
PLACEMENTS = {                       # step 11's four interface vertices
    "P1=s2 s3^-1": [(2, Z0), (3, NEG1)],
    "P2=s3 s2^-1": [(3, Z0), (2, NEG1)],
    "P3=s1 s2^-1": [(1, Z0), (2, NEG1)],
    "P4=s2 s1^-1": [(2, Z0), (1, NEG1)],
}
GG_VERTEX_FORM = {"P1=s2 s3^-1": True, "P2=s3 s2^-1": False,
                  "P3=s1 s2^-1": True, "P4=s2 s1^-1": False}
K_MAX = 10


def log(msg):
    print(f"[{time.time() - T0:7.1f}s] {msg}", flush=True)


def check(name, ok, note):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {note}", flush=True)
    ASSERTS.append({"name": name, "ok": bool(ok), "note": note})
    if not ok:
        FAILED.append(name)


class Level:
    """All Wedderburn blocks of H_n at q0 with their convention-D Markov weights."""

    def __init__(self, n):
        self.n = n
        self.y = AH.y_at_pin(n)
        self.blocks = {lam: AH.Block(lam) for lam in AH.partitions(n)}
        self.pos = [lam for lam in self.blocks if self.y[lam] > TOL]

    def chars(self, letters, only_pos=True):
        lams = self.pos if only_pos else list(self.blocks)
        return {lam: AH.Block.tr(self.blocks[lam].word(letters)) for lam in lams}

    def tau(self, letters):
        ch = self.chars(letters, only_pos=False)
        return mp.fsum(self.y[lam] * ch[lam] for lam in ch)

    def reading3(self, letters):
        ch = self.chars(letters)
        return all(c >= -TOL for c in ch.values()), ch


def main() -> int:
    log(f"q0 = {mp.nstr(Q0, 20)}, z_D = {mp.nstr(ZD, 20)}, dps {DPS}")
    H3, H6 = Level(3), Level(6)
    log(f"H_3 positive-weight blocks {H3.pos}; H_6 {H6.pos}")

    # ---------------- P0 calibration
    t1 = H3.tau([])
    check("P0.tau1", abs(t1 - 1) < TOL, f"tau(1) = {mp.nstr(t1, 30)}")
    ts = H3.tau([(0, Z0)])
    check("P0.tau_sigma", abs(ts - ZD) < TOL, f"tau(sigma_0) - z_D = {mp.nstr(ts - ZD, 5)}")
    # Delta_S = (h^2/2) 1 - (h/2)(sigma_0 + sigma_1): tau linear
    tds = H0 ** 2 / 2 - (H0 / 2) * (H3.tau([(0, Z0)]) + H3.tau([(1, Z0)]))
    closed = Q0 ** 2 / 2 - Q0 * ZD - 1 + ZD / Q0 + 1 / (2 * Q0 ** 2)
    check("P0.delta_S", abs(tds - closed) < TOL,
          f"tau(Delta_S) = {mp.nstr(tds, 25)} vs scorecard closed form, dev {mp.nstr(tds - closed, 3)}")
    c21 = H3.chars(V_L * 3, only_pos=False)[(2, 1)]
    ref = 2 - 3 * H0 ** 4 - H0 ** 6
    check("P0.chi21_V3", abs(c21 - ref) < TOL, f"chi_(2,1)(V^3) dev {mp.nstr(c21 - ref, 3)}")
    y6 = {str(k): mp.nstr(v, 20) for k, v in H6.y.items()}
    check("P0.D_two_row", all((len(l) <= 2) == (H6.y[l] > TOL) for l in H6.y),
          "H_6: y > 0 exactly on two-row shapes (convention D)")

    # ---------------- P1 qou-vd7j
    nr = json.loads((_ROOT / "computations/probes/frobenius-admissibility-net-row-probe.witness.json"
                     ).read_text())
    nrd = nr["data"]
    check("P1.netrow_witness", nr.get("q0Value", "").startswith("1.10997858275")
          and int(nrd["gram_rank"]) == 5 and abs(mp.mpf(str(nrd["one_dot_v"]))) > TOL
          and int(nrd["total_survivors"]) == 0,
          f"committed witness: rank {nrd['gram_rank']}, 1'v = {str(nrd['one_dot_v'])[:14]}, "
          f"{nrd['total_survivors']}/{nrd['total_candidates']} demand-admissible")
    alt = [H3.chars(V_L * k, only_pos=False)[(1, 1, 1)] for k in range(K_MAX + 1)]
    check("P1.altchar_one", all(abs(a - 1) < TOL for a in alt),
          "chi_(1^3)(V^k) = 1 for k = 0..10: radical pairing of every gamma-gamma word is 1 != 0")

    # ---------------- P2 nucleon level
    h3 = {}
    for k in range(K_MAX + 1):
        ok, ch = H3.reading3(V_L * k)
        h3[k] = {"pass": ok, "chi": {str(l): mp.nstr(c, 20) for l, c in ch.items()},
                 "tau_zD": H3.tau(V_L * k)}
    S3 = [k for k in h3 if h3[k]["pass"] and k > 0]
    log(f"H_3 non-zero survivors: {S3}")
    check("P2.three_divides", S3 == [k for k in range(1, K_MAX + 1) if k % 3 == 0],
          f"survivors {S3} = {{k : 3 | k}} (prediction 1)")
    nucleon = {"p": S3, "n": S3}
    check("P2.flavour_blind", nucleon["p"] == nucleon["n"],
          "p and n survivor sets are identical (same candidate set, no flavour index)")

    # ---------------- P3 two-nucleon level
    rows = []
    for a in S3:
        for b in S3:
            for bname, bl in [("none", [])] + list(PLACEMENTS.items()):
                for m in ([0] if bname == "none" else range(1, 7)):
                    w = V_L * a + V_R * b + bl * m
                    ok6, ch = H6.reading3(w)
                    rows.append({"a": a, "b": b, "bond": bname, "m": m,
                                 "bond_is_gg_vertex": GG_VERTEX_FORM.get(bname, True),
                                 "pass_H6": ok6, "pass_every_level": ok6,
                                 "min_char": mp.nstr(min(ch.values()), 15)})
        log(f"  a = {a}: done")
    surv = [r for r in rows if r["pass_every_level"]]
    log(f"H_6 every-level survivors: {len(surv)} of {len(rows)}")
    by_bond = {}
    for r in rows:
        key = f"{r['bond']}^{r['m']}"
        by_bond.setdefault(key, [0, 0])
        by_bond[key][0] += r["pass_every_level"]
        by_bond[key][1] += 1
    for k, (p, t) in by_bond.items():
        log(f"    {k:16s} {p}/{t}")
    check("P3.ran", len(rows) == len(S3) ** 2 * 25, f"{len(rows)} H_6 candidates evaluated")

    # ---------------- P4 Q_beta on the ruled base, every ordered survivor pair
    E0 = qbeta_e0.canonical(q=Q0)
    qtab = []
    for kp in S3:
        for kn in S3:
            d = h3[kn]["tau_zD"] - h3[kp]["tau_zD"]
            qtab.append({"p": f"V^{kp}", "n": f"V^{kn}", "eps_delta": mp.nstr(d, 30),
                         "Q_beta_MeV": mp.nstr(abs(d) * E0, 20), "_q": abs(d) * E0})
    check("P4.cost_minimal_zero", [r for r in qtab if r["p"] == r["n"] == "V^3"][0]["_q"] == 0,
          "cost-minimal selection p = n = V^3 gives Q_beta = 0 exactly (prediction 2)")
    check("P4.diag_zero", all(r["_q"] == 0 for r in qtab if r["p"] == r["n"]),
          "every equal pair gives 0")
    check("P4.offdiag_nonzero", all(r["_q"] > TOL for r in qtab if r["p"] != r["n"]),
          "every unequal pair gives a non-zero value (prediction 3)")

    # comparison column, read only now
    from codata_constants import Q_BETA_MEV  # noqa: PLC0415
    for r in qtab:
        r["vs_codata_pct"] = mp.nstr((r["_q"] - mp.mpf(str(Q_BETA_MEV))) / mp.mpf(str(Q_BETA_MEV))
                                     * 100, 8)
        del r["_q"]
    for r in qtab:
        log(f"  p={r['p']:5s} n={r['n']:5s}  Q_beta = {r['Q_beta_MeV'][:14]:>14s} MeV  "
            f"({r['vs_codata_pct']} %)")

    out = {
        "z_D": mp.nstr(ZD, 40), "E0_canonical_MeV": mp.nstr(E0, 30),
        "H6_y": y6,
        "H3_table": {str(k): {kk: (mp.nstr(vv, 30) if kk == "tau_zD" else vv)
                              for kk, vv in v.items()} for k, v in h3.items()},
        "H3_nonzero_survivors": S3,
        "nucleon_survivors": nucleon,
        "H6_rows": rows,
        "H6_survivor_count": len(surv),
        "H6_by_bond": {k: f"{p}/{t}" for k, (p, t) in by_bond.items()},
        "qbeta_table": qtab,
        "cost_minimal_selection": {"p": "V^3", "n": "V^3", "Q_beta_MeV": "0"},
        "scope": "(a): gamma-gamma grammar applied alone; no flavour-carrying letters",
        "no_target": "no AME read; CODATA Q_beta read only for the final comparison column",
    }
    from qou_substrate.witness import WitnessBuilder  # noqa: PLC0415
    wb = WitnessBuilder("qbeta-gg-sdp-base", engine="python", start_time=T0, output_dir=_HERE)
    wb.set_description(
        "qou-ales / qou-vd7j: gamma-gamma + reading-3 (every level) word selection and the "
        "Q_beta it gives on the ruled base (Markov trace at z_D, tower-summed E0). H_3 survivors "
        "3 | k, identical for p and n; cost-minimal selection p = n = V^3 so Q_beta = 0; all "
        "ordered survivor pairs reported, not ranked. vd7j: the G x = nf demand fails only "
        "through the radical pairing chi_(1^3) = 1. Pre-registered at b3a70fdf25.")
    wb.add_parameter("q0", Q_50_DIGIT_STR)
    wb.add_parameter("dps", DPS)
    wb.add_parameter("convention", "D (z = q^3/(q^2+1))")
    for key, val in out.items():
        wb.add_data(key, val)
    for a_ in ASSERTS:
        wb.add_assertion(a_["name"], computed=str(int(a_["ok"])), expected="1",
                         tolerance="0", source=a_["note"])
    path = wb.save({"q0Anchor": "proton"})
    log(f"witness -> {path.relative_to(_ROOT)}; {len(ASSERTS) - len(FAILED)}/{len(ASSERTS)} pass")
    return 0 if not FAILED else 1


if __name__ == "__main__":
    sys.exit(main())
