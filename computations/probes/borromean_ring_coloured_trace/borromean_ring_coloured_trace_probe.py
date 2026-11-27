#!/usr/bin/env python3
"""borromean_ring_coloured_trace_probe — ring-coloured trace of the Borromean nucleon V³ (qou-99qc).

Owner question 2026-11-21: "Why are you not doing a trace on the Borromean ring with the strands?"
Pre-registered in PREREGISTRATION.md (commit 390bd49834) before this file was run.
Lean twin: QOU/BraidsAndKnots/BorromeanRingColouredTrace.lean.

Exact sympy over Q(q), level-2 Jimbo braiding on (C²)^{⊗3} (u = e₁, K = diag(q, q⁻¹)).
τ_c(b) = Tr(K^{⊗3} P_c ρ(b))/[2]³ = q^{2T³(c)} ⟨c|ρ(b)|c⟩/[2]³.
Numbers: mpmath, 70 dps, proton q₀, E₀ from qbeta_e0 (both forms, labelled). No float64.

Checks
  S1  whole-space z_D trace of V³ = J_Bor(q²)/[2]² (Borromean Jones; sanity of the matrices).
  H1  τ_c is NOT invariant under conjugation by the pure braids σ₁², σ₂² (8-dim, all colourings);
      the class sums are.
  H2  τ_c is not constant on a class.
  H3  flip u↔d: ⟨flip c|V³|flip c⟩(q) = ⟨c|(σ₁⁻¹σ₂)³|c⟩(q⁻¹).
  H4  class sums = FlavourWeightSplit ε_p, ε_n (closed form fV3) and ε_p = q² ε_n.
  H5  strand tracking: every strand pair crosses once with each sign; W-free amplitude = 1.
  T2  two-term insertions per colouring: all-pairs connected = 0; adjacent labelled.
Then numbers, then CODATA.
"""
from __future__ import annotations

import itertools
import json
import sys
import time
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parents[2]
for _p in ("computations", "computations/qbeta", "computations/substrate", "tools/qou-substrate/python"):
    sys.path.insert(0, str(_ROOT / _p))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

import qbeta_e0  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

DPS = 70
mp.mp.dps = DPS
T0 = time.time()
ASSERTS: list = []
FAILED: list = []
q = sp.symbols("q", positive=True)
h = q - 1 / q
D2 = q + 1 / q


def log(msg):
    print(f"[{time.time() - T0:7.1f}s] {msg}", flush=True)


def check(name, ok, note):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {note}", flush=True)
    ASSERTS.append({"name": name, "ok": bool(ok), "note": note})
    if not ok:
        FAILED.append(name)


def zero(expr):
    return sp.simplify(sp.together(expr)) == 0


# ---- 8-dim: basis index 4*s1 + 2*s2 + s3, s = 0 for u, 1 for d
R2 = sp.Matrix([[q, 0, 0, 0], [0, 0, 1, 0], [0, 1, h, 0], [0, 0, 0, q]])
I2 = sp.eye(2)
S1 = sp.kronecker_product(R2, I2)
S2 = sp.kronecker_product(I2, R2)
S1i, S2i = S1.inv(), S2.inv()
Kq = sp.diag(q, 1 / q)
K3 = sp.kronecker_product(sp.kronecker_product(Kq, Kq), Kq)
V = S1 * S2i
V3 = sp.simplify(V ** 3)
MIRROR3 = sp.simplify((S1i * S2) ** 3)
COL = ["".join("ud"[s] for s in t) for t in itertools.product((0, 1), repeat=3)]  # index -> label
IDX = {c: i for i, c in enumerate(COL)}
P_CLASS = ["uud", "udu", "duu"]
N_CLASS = ["udd", "dud", "ddu"]


def tau(M, c):
    i = IDX[c]
    return sp.factor(sp.together(K3[i, i] * M[i, i] / D2 ** 3))


def flip(c):
    return "".join("d" if x == "u" else "u" for x in c)


def main():
    out = {}
    log("S1: Borromean Jones")
    full = sp.together((K3 * V3).trace() / D2 ** 3)
    t = q ** 2
    jones = -t ** 3 + 3 * t ** 2 - 2 * t + 4 - 2 / t + 3 / t ** 2 - 1 / t ** 3
    check("S1", zero(full - jones / D2 ** 2), "Tr(K^3 V^3)/[2]^3 = J_Bor(q^2)/[2]^2")

    log("closed forms of the six colourings")
    taus = {c: tau(V3, c) for c in P_CLASS + N_CLASS}
    for c, v in taus.items():
        log(f"  tau_{c} = {v}")
    out["tau_closed_forms"] = {c: str(v) for c, v in taus.items()}
    out["diag_closed_forms"] = {c: str(sp.factor(V3[IDX[c], IDX[c]])) for c in P_CLASS + N_CLASS}

    log("H1: conjugation by pure braids")
    noninv = {}
    for gname, g, gi in (("s1^2", S1 * S1, S1i * S1i), ("s2^2", S2 * S2, S2i * S2i)):
        C = sp.simplify(g * V3 * gi)
        d = {c: str(sp.factor(sp.together(C[IDX[c], IDX[c]] - V3[IDX[c], IDX[c]]))) for c in P_CLASS + N_CLASS}
        noninv[gname] = d
        nz = [c for c in d if d[c] != "0"]
        check(f"H1-{gname}-changes", len(nz) > 0, f"colourings changed: {nz}")
        cs_ok = all(zero(sum(C[IDX[c], IDX[c]] - V3[IDX[c], IDX[c]] for c in cl)) for cl in (P_CLASS, N_CLASS))
        check(f"H1-{gname}-classsum-invariant", cs_ok, "class sums unchanged")
    out["conjugation_changes_of_diagonal"] = noninv

    log("H2: class constancy")
    check("H2-p-not-constant", not zero(taus["uud"] - taus["udu"]), "tau_uud != tau_udu")
    check("H2-n-not-constant", not zero(taus["udd"] - taus["dud"]), "tau_udd != tau_dud")

    log("H3: flip = mirror + bar")
    ok = all(zero(V3[IDX[flip(c)], IDX[flip(c)]] - MIRROR3[IDX[c], IDX[c]].subs(q, 1 / q)) for c in P_CLASS + N_CLASS)
    check("H3", ok, "<flip c|V^3|flip c>(q) = <c|mirror|c>(1/q) for all six")

    log("H4: class sums")
    epsP = sp.together(sum(taus[c] for c in P_CLASS))
    epsN = sp.together(sum(taus[c] for c in N_CLASS))
    P = q ** 12 - 3 * q ** 10 + 3 * q ** 8 - 5 * q ** 6 + 3 * q ** 4 - 3 * q ** 2 + 1
    fV3 = (q ** 2 - 1) * P / (q ** 4 * (q ** 2 + 1) ** 3)
    check("H4-fV3", zero(epsN - epsP - fV3), "sum_n tau - sum_p tau = fV3 (FlavourWeightSplit)")
    check("H4-qsq", zero(epsP - q ** 2 * epsN), "eps_p = q^2 eps_n")
    out["eps_p"] = str(sp.factor(epsP))
    out["eps_n"] = str(sp.factor(epsN))

    log("H5: strand tracking and W-free amplitude")
    pos = [0, 1, 2]
    crossings = []
    for (i, s) in [(0, +1), (1, -1)] * 3:
        a, b = pos[i], pos[i + 1]
        crossings.append((a, b, s))
        pos[i], pos[i + 1] = b, a
    check("H5-pure", pos == [0, 1, 2], "V^3 is a pure braid")
    lk = {}
    for a, b, s in crossings:
        k = tuple(sorted((a, b)))
        lk[k] = lk.get(k, 0) + s
    check("H5-lk0", all(v == 0 for v in lk.values()), f"signed crossing sums per pair: {lk}")
    strict = {}
    for c in P_CLASS + N_CLASS:
        amp = sp.Integer(1)
        for a, b, s in crossings:
            if c[a] == c[b]:
                amp *= q ** s
        strict[c] = sp.factor(K3[IDX[c], IDX[c]] * amp / D2 ** 3)
    check("H5-amp1", all(zero(strict[c] - K3[IDX[c], IDX[c]] / D2 ** 3) for c in strict), "W-free amplitude = 1")
    strict_diff = sp.factor(sum(strict[c] for c in N_CLASS) - sum(strict[c] for c in P_CLASS))
    check("H5-diff", zero(strict_diff + 3 * q ** 2 * (q ** 2 - 1) / (q ** 2 + 1) ** 3), f"strict n-p = {strict_diff}")
    out["strict_n_minus_p"] = str(strict_diff)
    out["crossings_by_strand"] = crossings

    log("T2: two-term insertions per colouring")
    Qc = {"u": sp.Rational(2, 3), "d": sp.Rational(-1, 3)}

    def qpair(c, pairs):
        return sum(Qc[c[i]] * Qc[c[j]] for i, j in pairs)

    allp = [(0, 1), (1, 2), (0, 2)]
    adj = [(0, 1), (1, 2)]
    tt = {}
    for c in P_CLASS + N_CLASS:
        tt[c] = {"all_pairs_raw_coeff": str(qpair(c, allp)), "adjacent_raw_coeff": str(qpair(c, adj)),
                 "all_pairs_raw": str(sp.factor(qpair(c, allp) * taus[c])),
                 "adjacent_raw": str(sp.factor(qpair(c, adj) * taus[c]))}
    check("T2-allpairs-scalar", all(qpair(c, allp) == 0 for c in P_CLASS) and all(qpair(c, allp) == sp.Rational(-1, 3) for c in N_CLASS),
          "all-pairs insertion is 0 on W_p and -1/3 on W_n: connected part 0 per colouring")
    out["two_term_per_colouring"] = tt
    adj_conn_diff = sp.factor(sum((qpair(c, adj) + sp.Rational(2, 9)) * taus[c] for c in N_CLASS) - sum(qpair(c, adj) * taus[c] for c in P_CLASS))
    check("T2-adjacent-matches-QTrace", zero(adj_conn_diff - (q - 1) ** 4 * (q + 1) ** 4 * (q ** 2 + 2) * (2 * q ** 4 + 1) / (9 * q ** 4 * (q ** 2 + 1) ** 3)),
          "per-colouring adjacent connected sums to deltaT_adjacent_connected_eq")

    if FAILED:
        log(f"FAILED: {FAILED}")
    log("numbers at proton q0")
    q0 = mp.mpf(Q_50_DIGIT_STR)
    E0c = qbeta_e0.canonical(q=q0)
    E0z = qbeta_e0.order_zero(q=q0)

    def ev(expr):
        f = sp.lambdify(q, sp.together(sp.sympify(expr)), modules="mpmath")
        return f(q0)

    nums = {"q0": Q_50_DIGIT_STR, "E0_canonical_tower_MeV": mp.nstr(E0c, 40), "E0_order_zero_MeV": mp.nstr(E0z, 40)}
    nums["tau_at_q0"] = {c: mp.nstr(ev(taus[c]), 40) for c in taus}
    dcls = ev(epsN - epsP)
    dstr = ev(strict_diff)
    nums["class_sum_n_minus_p"] = mp.nstr(dcls, 40)
    nums["strict_n_minus_p"] = mp.nstr(dstr, 40)
    from codata_constants import Q_BETA_MEV  # noqa: PLC0415  (comparison column only)
    QB_CODATA = mp.mpf(str(Q_BETA_MEV))
    tbl = []
    for name, d in (("class_sum (= scored eps_flavour)", dcls), ("W-free strict colouring", dstr)):
        for en, E in (("canonical_tower", E0c), ("order_zero", E0z)):
            Q = abs(d) * E
            tbl.append({"functional": name, "E0": en, "Q_MeV": mp.nstr(Q, 30),
                        "vs_codata_pct": mp.nstr(100 * (Q / QB_CODATA - 1), 10)})
            log(f"  {name:35s} {en:16s} Q = {mp.nstr(Q, 15)} MeV  ({mp.nstr(100 * (Q / QB_CODATA - 1), 6)} % vs CODATA)")
    nums["qbeta_table"] = tbl
    nums["codata_Q_beta_MeV"] = mp.nstr(QB_CODATA, 20)
    out["numbers"] = nums
    for c in taus:
        log(f"  tau_{c}(q0) = {mp.nstr(ev(taus[c]), 20)}")
    return out


if __name__ == "__main__":
    data = main()
    from qou_substrate.witness import WitnessBuilder  # noqa: PLC0415
    wb = WitnessBuilder("borromean-ring-coloured-trace", engine="python", start_time=T0, output_dir=_HERE)
    wb.set_description(
        "qou-99qc: ring-coloured trace of the Borromean nucleon V^3. Per-colouring values are not "
        "link invariants (pure-braid conjugation moves them); class sums equal the scored "
        "eps_flavour; the W-free strict colouring is lk-determined (lk = 0). Pre-registered at 390bd49834.")
    wb.add_parameter("q0", Q_50_DIGIT_STR)
    wb.add_parameter("dps", DPS)
    wb.add_parameter("convention", "D (z = q^3/(q^2+1))")
    for key, val in data.items():
        wb.add_data(key, val)
    for a_ in ASSERTS:
        wb.add_assertion(a_["name"], computed=str(int(a_["ok"])), expected="1", tolerance="0", source=a_["note"])
    path = wb.save({"q0Anchor": "proton"})
    log(f"witness -> {path}; {len(ASSERTS) - len(FAILED)}/{len(ASSERTS)} pass")
    sys.exit(1 if FAILED else 0)
