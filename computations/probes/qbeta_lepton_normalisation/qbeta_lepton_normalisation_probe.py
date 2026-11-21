#!/usr/bin/env python3
"""qbeta_lepton_normalisation_probe — the derived lepton-strand normalisation (issue #8833).

Premises (N1)-(N3) and reporting rules: PREREGISTRATION.md (committed first). Lean:
QOU/QBeta/LeptonStrandNormalisation.lean (normExponent_forced, spectator_of_forced,
sector_idle_ne_one, summed_idle_eq_one).

  x_hat(W) = q^(-2 wr W) Tr(K^9 (P_p (x) 1) rho(W)) / [2]^c(W)

on the 1560 words of qbeta_gg_process_word (same family). Nucleon sector observed (proton,
weight q); lepton strands summed.

Checks
  M1  Jimbo partial quantum trace over the last strand: ptr(K R) = q^2 1, ptr(K R^-1) = q^-2 1
      (exact sympy): stabilisation times q^(+-2), cancelled by the framing factor (N3).
  M2  every word has writhe 0 and 7 closure components.
  M3  on the bare nucleon (n = c = 3) x_hat is the ruled eps_p (N1).
  M4  an idle summed strand leaves x_hat unchanged (N2), numerically on beta_Bor (x) 1.
  M5  unlinked words factorise as eps_p * Ihat(L)/[2]^4; e-nubar and mirror values exact.
  M6  report: x_hat for all words, window hits, none selected.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parents[2]
for _p in ("computations", "computations/qbeta", "computations/substrate",
           "tools/qou-substrate/python"):
    sys.path.insert(0, str(_ROOT / _p))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, _ROOT / rel)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


gg = _load("_gg", "computations/probes/qbeta_gg_lepton_pair/qbeta_gg_lepton_pair_probe.py")
pw = _load("_pw", "computations/probes/qbeta_gg_process_word/qbeta_gg_process_word_probe.py")

mp.mp.dps = 60
Q0 = mp.mpf(Q_50_DIGIT_STR)
D2 = Q0 + 1 / Q0
WINDOW = (mp.mpf("0.33174"), mp.mpf("0.40872"))
RESULTS: list[tuple[str, bool, str]] = []


def check(name, ok, detail):
    RESULTS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}\n         {detail}\n")


def kweight(b, n, q):
    return q ** (n - 2 * bin(b).count("1"))


def obs_trace(word, n, q, obs):
    """Tr(K^n P rho(word)), P = basis vectors b with obs(b) true."""
    tot = 0
    for b in range(2 ** n):
        if not obs(b):
            continue
        v = {b: 1 + 0 * q}
        for (i, s) in reversed(word):
            v = gg.apply_crossing(v, n, i, s, q)
        if v.get(b):
            tot += kweight(b, n, q) * v[b]
    return tot


def writhe(word):
    return sum(s for _, s in word)


def main() -> int:
    qs = sp.symbols("q", positive=True)
    ok1 = True
    for s, expect in ((+1, qs ** 2), (-1, qs ** -2)):
        for a in (0, 1):
            for a2 in (0, 1):
                tot = 0
                for b in (0, 1):
                    v = gg.apply_crossing({(a << 1) | b: sp.Integer(1)}, 2, 0, s, qs)
                    tot += (qs if b == 0 else 1 / qs) * v.get((a2 << 1) | b, 0)
                want = expect if a == a2 else 0
                ok1 &= sp.simplify(tot - want) == 0
    check("M1_partial_quantum_trace_is_q_squared", ok1,
          "ptr_last(K R) = q^2 * 1 and ptr_last(K R^-1) = q^-2 * 1 exactly (Jimbo R): a "
          "stabilisation multiplies the trace by q^(2 s), removed by q^(-2 writhe). Strand "
          "count changes, component count does not, so only [2]^c is invariant (N3).")

    beta = gg.gg_word((0, 0, 0))
    p_obs3 = lambda b: bin(b).count("1") == 1  # noqa: E731
    eps_p = obs_trace(beta, 3, Q0, p_obs3) / D2 ** 3
    check("M3_nucleon_is_D1", abs(eps_p - mp.mpf("0.40872")) < mp.mpf("1e-5"),
          f"x_hat(beta_Bor) = eps_p = {mp.nstr(eps_p, 15)} (n = c = 3, so [2]^c = [2]^n).")
    nuc_obs4 = lambda b: bin(b >> 1).count("1") == 1  # noqa: E731
    x4 = obs_trace(beta, 4, Q0, nuc_obs4) / D2 ** 4
    check("M4_idle_summed_strand_invariant", abs(x4 - eps_p) < mp.mpf("1e-50"),
          f"beta_Bor (x) idle strand, lepton strand summed, / [2]^4: {mp.nstr(x4, 15)} = eps_p. "
          f"Restricted to one sector it would be eps_p * q^(+-1)/[2] (Lean sector_idle_ne_one).")

    # family (identical to qbeta_gg_process_word)
    wit = __import__("json").load(open(_ROOT / "computations/probes/qbeta_gg_process_word/"
                                       "qbeta-gg-process-word.witness.json"))
    n = 9
    nuc_obs9 = lambda b: bin(b >> 6).count("1") == 1  # noqa: E731
    rows, ok2, ok5 = [], True, True
    lep_inv = {}
    for r in wit["rows"]:
        lv = [int(t) - 3 for t in r["lepton"].split("V")[1:]]
        X = [int(t) for t in r["junction"].split("V")[1:]] if r["junction"] else []
        lw = gg.gg_word(lv)
        W = gg.gg_word(X) + beta + pw.shift(lw, 3)
        k, _lk, _sc = gg.strand_data(W, n)
        ok2 &= writhe(W) == 0 and k == 7
        key = r["lepton"]
        if key not in lep_inv:
            lep_inv[key] = obs_trace(lw, 6, Q0, lambda b: True) / D2 ** 4
        xh = Q0 ** (-2 * writhe(W)) * obs_trace(W, n, Q0, nuc_obs9) / D2 ** k
        if not X:
            ok5 &= abs(xh - eps_p * lep_inv[key]) < mp.mpf("1e-40")
        rows.append({"lepton": key, "lepton_kind": r["lepton_kind"], "junction": r["junction"],
                     "junction_vertices": len(X), "x_hat": mp.nstr(xh, 20),
                     "lepton_invariant": mp.nstr(lep_inv[key], 20),
                     "in_window": bool(WINDOW[0] < xh < WINDOW[1])})
    check("M2_writhe_zero_seven_components", ok2,
          "every W = X beta_Bor L has writhe 0 and 7 closure components.")
    q = Q0
    hopf_e = (q ** 4 + 1) / (q ** 4 * (q ** 2 + 1))
    hopf_m = q ** 2 * (q ** 4 + 1) / (q ** 2 + 1)
    vals = {mp.nstr(v, 30) for v in lep_inv.values()}
    exact = all(min(abs(v - hopf_e), abs(v - hopf_m)) < mp.mpf("1e-40") for v in lep_inv.values())
    check("M5_unlinked_factorise", ok5 and exact,
          f"unlinked x_hat = eps_p * Ihat(L)/[2]^4 to 1e-40; Ihat(L)/[2]^4 takes only the two "
          f"values (q^4+1)/(q^4 (q^2+1)) = {mp.nstr(hopf_e, 12)} (e- nubar) and "
          f"q^2 (q^4+1)/(q^2+1) = {mp.nstr(hopf_m, 12)} (mirror): {len(vals)} distinct.")
    xs = [mp.mpf(r["x_hat"]) for r in rows]
    hits = [r for r in rows if r["in_window"]]
    def rng(sel):
        v = [mp.mpf(r["x_hat"]) for r in rows if sel(r)]
        return f"[{mp.nstr(min(v), 8)}, {mp.nstr(max(v), 8)}]"
    det = (f"{len(rows)} words. x_hat all {rng(lambda r: True)}; e-nubar unlinked "
           f"{rng(lambda r: r['lepton_kind']=='e-nubar' and not r['junction_vertices'])}, linked "
           f"{rng(lambda r: r['lepton_kind']=='e-nubar' and r['junction_vertices'])}; mirror unlinked "
           f"{rng(lambda r: r['lepton_kind']=='mirror' and not r['junction_vertices'])}, linked "
           f"{rng(lambda r: r['lepton_kind']=='mirror' and r['junction_vertices'])}. In window: "
           f"{len(hits)} (e-nubar {sum(r['lepton_kind']=='e-nubar' for r in hits)}, mirror "
           f"{sum(r['lepton_kind']=='mirror' for r in hits)}). None selected.")
    check("M6_report", True, det)
    from collections import Counter
    print("   hits by junction:", Counter((r["lepton_kind"], r["junction"]) for r in hits))

    allp = all(o for _, o, _ in RESULTS)
    print(f"  {sum(o for _, o, _ in RESULTS)}/{len(RESULTS)} checks passed")
    wb = WitnessBuilder("qbeta-lepton-normalisation", engine="mpmath")
    for nm, o, d in RESULTS:
        wb.add_assertion(nm, computed="PASS" if o else "FAIL", expected="PASS",
                         tolerance="exact", source=d)
    wb.save({
        "description": ("Derived lepton-strand normalisation q^(-2 wr) Tr(K (P_p x 1) rho)/[2]^c "
                        "from (N1) agreement, (N2) spectator, (N3) closure invariance; x_hat on "
                        "the 1560 qbeta_gg_process_word words. Nothing selected."),
        "q0": Q_50_DIGIT_STR, "eps_p": mp.nstr(eps_p, 30), "window": ["0.33174", "0.40872"],
        "rows": rows,
        "caveats": ["premises N1-N3 are the agent's, for the owner to confirm",
                    "x_hat restricts the nucleon sector, so it is not a full link invariant"],
    })
    return 0 if allp else 1


if __name__ == "__main__":
    sys.exit(main())
