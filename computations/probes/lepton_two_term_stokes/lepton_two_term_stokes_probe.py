#!/usr/bin/env python3
"""qou-99qc: the lepton two-term trace, derived the way the nucleon one was (Lagrangian + Stokes).

Pre-registered in PREREGISTRATION.md (commit e4ad92f18d) before any number. Lean:
QOU.QBeta.LeptonTwoTermStokesCovariance (sorry-free).

What this checks and computes, exact in ℚ(q) (sympy field, q = 2, 3/2 Fractions) and at the proton q₀
(mpmath, 70 dps). No floats on any value path. The coupling scale c_em is NOT chosen.

A. Carry test (the covariance the Stokes step requires). On V^{⊗4} with strand species carried along
   by each crossing, an insertion O is admissible iff ρ(σ_i)·O(col) = O(col∘(i i+1))·ρ(σ_i) for every
   crossing that occurs. Tested for: pairs only Q_pair (the 16:44 ruled object), the carried family
   (β/2)Q_tot² + κ Σ Q_a²/y_a with κ = −β·y_q/2 (the unique member that restricts to Q_pair on three
   quarks), Q_tot², and pairs with a charge-0 "neutral" doublet strand.
B. The carried family is a scalar on every total-weight space W_m (so its connected part is 0 on
   every word), and equal on n⊗ν and p⊗e⁻.
C. The #8707 routes (P1/P4, P2 families A and D, N2) with the derived insertion: connected part
   (scored) and raw part (unscored comparison), plus one-term values for context.
Run: python3 -u lepton_two_term_stokes_probe.py 2>&1 | tee /tmp/lepton_two_term_stokes.log
"""
from __future__ import annotations

import itertools
import sys
import time
from fractions import Fraction as Fr
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parents[2]
for _p in (str(_ROOT / "computations"), str(_ROOT / "tools/qou-substrate/python"), str(_HERE)):
    sys.path.insert(0, _p)

import mpmath as mp  # noqa: E402

import qou_substrate.constants as C  # noqa: E402
from qou_substrate.precision import fmt  # noqa: E402
import two_term_engine as E  # noqa: E402
import beta_routes_words as W  # noqa: E402  (#8707 words; its main() is not run)

W.E = E  # one engine instance
DPS = 70
mp.mp.dps = DPS
T0 = time.time()
ASSERTS: list = []


def log(msg):
    print(f"[{time.time() - T0:7.1f}s] {msg}", flush=True)


def check(name, ok, note=""):
    ASSERTS.append({"name": name, "ok": bool(ok), "note": note})
    log(f"{'PASS' if ok else 'FAIL'} {name} {note}")


Q0 = C.q_at(DPS)
ME = mp.mpf(C.M_E_MEV_STR)

# hypercharges (Q = T³ + Y/2): quark 1/3, lepton doublet −1. "neutral" has charge 0 on both states:
# it is NOT of the form T³ + Y/2 and has no Y.
def Y():
    return {"quark": E.ONE / 3, "lepton": -E.ONE}


def charges(col, b):
    return [E.CHARGE[c][x] for c, x in zip(col, b)]


def ins_value(kind, col, b):
    Qs = charges(col, b)
    tot = sum(Qs, E.ZERO)
    pair = sum((Qs[i] * Qs[j] for i in range(len(Qs)) for j in range(i + 1, len(Qs))), E.ZERO)
    if kind == "pairs":
        return pair
    if kind == "tot2":
        return tot * tot / 2
    if kind == "nat":  # (1/2)Q_tot² + κ Σ Q²/y, κ = −y_q/2 (β = 1)
        y = Y()
        kappa = -y["quark"] / 2
        return tot * tot / 2 + kappa * sum((Q * Q / y[c] for Q, c in zip(Qs, col)), E.ZERO)
    raise ValueError(kind)


def ins_blocks(kind, col):
    N = len(col)
    return {m: E.diag([ins_value(kind, col, b) for b in bs]) for m, bs in E.blocks(N).items()}


def swap(col, i):
    c = list(col)
    c[i], c[i + 1] = c[i + 1], c[i]
    return tuple(c)


def carried(kind, col, i):
    N = len(col)
    rho = E.rho_blocks(N, [[(E.ONE, [i])]])
    O, O2 = ins_blocks(kind, col), ins_blocks(kind, swap(col, i))
    return all(E._mclose(E.mm(rho[m], O[m]), E.mm(O2[m], rho[m])) for m in rho)


def part_A():
    E.use()  # symbolic ℚ(q)
    out = {}
    cols = sorted(set(itertools.permutations(("quark",) * 3 + ("lepton",))))
    for kind in ("pairs", "nat", "tot2"):
        res = {"quark-quark": [], "quark-lepton": []}
        for col in cols:
            for i in range(3):
                typ = "quark-quark" if col[i] == col[i + 1] else "quark-lepton"
                res[typ].append(carried(kind, col, i))
        out[kind] = {k: f"{sum(v)}/{len(v)} carried" for k, v in res.items()}
    # neutral doublet next to a quark: pairs with a third quark strand
    colN = ("quark", "quark", "neutral")
    out["pairs_with_neutral_doublet"] = {
        "quark-quark": "carried" if carried("pairs", colN, 0) else "NOT carried",
        "quark-neutral": "carried" if carried("pairs", colN, 1) else "NOT carried"}
    # two lepton strands (electron-as-B3-word reading has several lepton strands): lepton-lepton crossing
    colL = ("quark", "lepton", "lepton")
    out["nat_lepton_lepton"] = "carried" if carried("nat", colL, 1) else "NOT carried"
    out["pairs_lepton_lepton"] = "carried" if carried("pairs", colL, 1) else "NOT carried"
    check("A1 pairs-only carried at every quark-quark crossing", out["pairs"]["quark-quark"].startswith("6/6"))
    check("A2 pairs-only NOT carried at any quark-lepton crossing", out["pairs"]["quark-lepton"].startswith("0/"))
    check("A3 derived family carried at every crossing", all(v.split("/")[0] == v.split("/")[1].split()[0]
                                                            for v in out["nat"].values()))
    check("A4 Q_tot^2 carried at every crossing", all(v.split("/")[0] == v.split("/")[1].split()[0]
                                                     for v in out["tot2"].values()))
    check("A5 charge-0 doublet strand: pairs NOT carried at quark-neutral crossing",
          out["pairs_with_neutral_doublet"]["quark-neutral"] == "NOT carried")
    return out


def scalar_on_weight_spaces(kind, col):
    for m, bs in E.blocks(len(col)).items():
        vals = {ins_value(kind, col, b) for b in bs}
        if len(vals) != 1:
            return False
    return True


def part_B():
    E.use()
    out = {}
    for name, col in (("qqq+l", W.Q3 + ("lepton",)), ("COL_A (qqq+lll)", W.COL_A),
                      ("qqq (nucleon)", W.Q3)):
        out[name] = {k: scalar_on_weight_spaces(k, col) for k in ("nat", "pairs", "tot2")}
    check("B1 derived family scalar on every W_m (qqq+l, qqq+lll, qqq)",
          all(v["nat"] for v in out.values()))
    check("B2 pairs-only NOT scalar on W_m once a lepton strand is present",
          not out["qqq+l"]["pairs"] and not out["COL_A (qqq+lll)"]["pairs"])
    col = W.Q3 + ("lepton",)
    nnu, pe = (0, 1, 1, 0), (0, 0, 1, 1)  # bit 0 = u: (u,d,d)⊗ν, (u,u,d)⊗e⁻
    out["beta_values"] = {k: {"n(x)nu": str(ins_value(k, col, nnu)), "p(x)e": str(ins_value(k, col, pe))}
                          for k in ("nat", "pairs", "tot2")}
    check("B3 derived family: n⊗ν and p⊗e⁻ equal", ins_value("nat", col, nnu) == ins_value("nat", col, pe))
    check("B4 pairs-only splits them (−1/3 vs −1)", (ins_value("pairs", col, nnu), ins_value("pairs", col, pe))
          == (-E.ONE / 3, -E.ONE))
    # nucleon recovery: nat == pairs on three quarks, every state
    check("B5 derived family = ruled Q_pair on three quarks (state by state)",
          all(ins_value("nat", W.Q3, b) == ins_value("pairs", W.Q3, b)
              for b in itertools.product((0, 1), repeat=3)))
    return out


# ── C. routes ────────────────────────────────────────────────────────────────────────────────
def t_ins(col, rho, ins, conn):
    N = len(col)
    tot = E.ZERO
    for m, M in rho.items():
        A = ins[m]
        if conn:
            d = len(A)
            A = E.lin((E.ONE, A), (-E.tr(A) / d, E.eye(d)))
        tot += E.q ** m * E.tr(E.mm(A, M))
    return tot / E.QD2 ** N


def routes():
    out = {"P1P4": {}, "P2A": {}, "P2D": {}, "N2": {}}
    insA = ins_blocks("nat", W.COL_A)
    ins4 = ins_blocks("nat", W.Q3 + ("lepton",))
    for pk, pt in W.points().items():
        rb = E.rho_blocks(3, [W.L(W.BETA)])
        t1b = E.t_one(3, rb)
        for name, (pre, post) in W.P1_WORDS.items():
            r = E.rho_blocks(6, W.p1_element(pre, post, pt))
            t1 = E.t_one(6, r)
            t2c = t_ins(W.COL_A, r, insA, True)
            t2r = t_ins(W.COL_A, r, insA, False)
            nn = lambda b: sum(1 if x == 0 else -1 for x in b[:3]) == -1 and b[3] == 0  # noqa: E731
            pe = lambda b: sum(1 if x == 0 else -1 for x in b[:3]) == +1 and b[3] == 1  # noqa: E731
            D1 = (E.sector_trace(6, r, nn) - E.sector_trace(6, r, pe)) / 12
            insc = {m: E.lin((E.ONE, A), (-E.tr(A) / len(A), E.eye(len(A)))) for m, A in insA.items()}
            D2c = (E.sector_trace(6, r, nn, insc) - E.sector_trace(6, r, pe, insc)) / 12
            D2r = (E.sector_trace(6, r, nn, insA) - E.sector_trace(6, r, pe, insA)) / 12
            out["P1P4"][f"{name}|{pk}"] = {"t1": t1, "t1_beta": t1b, "t2_conn": t2c,
                                           "t2raw_over_t1": t2r / t1 if t1 != 0 else None,
                                           "P4_D_one_term": D1, "P4_D_two_term_conn": D2c, "P4_D_raw": D2r}
    B3, nuc11, TREFOIL, final, family_d_word, to_elem = W.p2_defs()
    nucs = {"p": nuc11("p"), "n": nuc11("n")}
    for j in (-1, 0, 1):
        for k in (-1, 0, 1):
            row = {}
            for pk, pw in nucs.items():
                r = E.rho_blocks(6, to_elem(final(pw, j, k)))
                t1 = E.t_one(6, r)
                row[pk] = {"t1": t1, "t2_conn": t_ins(W.COL_A, r, insA, True),
                           "t2raw_over_t1": t_ins(W.COL_A, r, insA, False) / t1}
            out["P2A"][f"j={j},k={k}"] = row
    for span_name, span in (("D3_strands_2_4", [1, 2]), ("D4_strands_1_4", [0, 1, 2])):
        for t in (-1, 1):
            for k in (-1, 0, 1):
                row = {}
                for pk, pw in nucs.items():
                    r = E.rho_blocks(6, to_elem(family_d_word(pw, span, t, k)))
                    t1 = E.t_one(6, r)
                    row[pk] = {"t1": t1, "t2_conn": t_ins(W.COL_A, r, insA, True),
                               "t2raw_over_t1": t_ins(W.COL_A, r, insA, False) / t1}
                out["P2D"][f"{span_name},t={t},k={k}"] = row
    for name, w in W.N2_WORDS.items():
        r = E.rho_blocks(4, [W.L(w)])
        out["N2"][name] = {"t1": E.t_one(4, r), "t2_conn": t_ins(W.Q3 + ("lepton",), r, ins4, True),
                           "t2raw_over_t1": t_ins(W.Q3 + ("lepton",), r, ins4, False) / E.t_one(4, r)}
    return out


def flat(d, p=""):
    if isinstance(d, dict):
        for k, v in d.items():
            yield from flat(v, f"{p}/{k}")
    else:
        yield p, d


def order_at_one(v3, v4):
    if v3 == 0 or v4 == 0:
        return None
    a = mp.mpf(v3.numerator) / v3.denominator
    b = mp.mpf(v4.numerator) / v4.denominator
    return int(mp.nint(mp.log(abs(a / b)) / mp.log(10)))


def main():
    log(f"q0 (proton) = {mp.nstr(Q0, 30)}")
    out = {"A_carry_test": part_A()}
    log("A done")
    out["B_weight_space_scalar_and_beta_values"] = part_B()
    log("B done")
    runs = {}
    for tag, qv in (("q2", Fr(2)), ("q3/2", Fr(3, 2)), ("q1+1e-3", Fr(1001, 1000)), ("q1+1e-4", Fr(10001, 10000))):
        E.use(qv, Fr(1))
        check(f"[{tag}] engine: t1(σ) = z_D", E.t_one(3, E.rho_blocks(3, [W.L([0])])) == E.q ** 3 / (E.q ** 2 + 1))
        runs[tag] = dict(flat(routes()))
        log(f"routes at {tag}")
    E.use(Q0, mp.mpf(1), exact=False, tol=mp.mpf(10) ** -55)
    runs["q0"] = dict(flat(routes()))
    log("routes at q0")
    table = {}
    for k, v in runs["q0"].items():
        a, b = runs["q2"][k], runs["q3/2"][k]
        zero = (a == 0 and b == 0) if (a is not None and b is not None) else None
        o3, o4 = runs["q1+1e-3"][k], runs["q1+1e-4"][k]
        table[k] = {"q0": fmt(v) if v is not None else None, "exact_zero": zero,
                    "order_(q-1)_est": (order_at_one(o3, o4) if (o3 is not None and o4 is not None and not zero)
                                        else None)}
    conn = [v["exact_zero"] for k, v in table.items() if k.endswith("t2_conn") or k.endswith("P4_D_two_term_conn")]
    check("C1 derived connected two-term = 0 exactly on every route word (P1/P4, P2 A/D, N2)", all(conn),
          f"{len(conn)} quantities")
    out["routes"] = table
    out["comparison"] = {"Q_beta_codata_MeV": fmt(mp.mpf(C.M_N_MEV_STR) - mp.mpf(C.M_P_MEV_STR) - ME),
                         "note": "comparison only; c_em not chosen; nothing selected by residual"}
    from qou_substrate.witness import WitnessBuilder  # noqa: PLC0415
    wb = WitnessBuilder("lepton-two-term-stokes", engine="python", start_time=T0, output_dir=_HERE)
    wb.set_description("qou-99qc: the two-term (QED) trace with a lepton strand, derived as for the nucleon "
                       "(Lagrangian matter term + carry condition through every crossing). Pre-registered "
                       "e4ad92f18d. Not wired to any scorecard; c_em not chosen.")
    wb.add_parameter("q0", fmt(Q0))
    wb.add_parameter("dps", DPS)
    wb.add_parameter("insertion", "(1/2)Q_tot^2 - (y_q/2) sum Q_a^2/y_a  (beta = 1), y_q = 1/3, y_l = -1")
    wb.add_parameter("premise", "L: lepton doublet braided by the same Jimbo R (owner-undecided)")
    wb.add_data("results", out)
    for a_ in ASSERTS:
        wb.add_assertion(a_["name"], computed=str(int(a_["ok"])), expected="1", tolerance="0", source=a_["note"])
    path = wb.save({"q0Anchor": "proton"})
    fails = [a_ for a_ in ASSERTS if not a_["ok"]]
    log(f"witness -> {path}; {len(ASSERTS) - len(fails)}/{len(ASSERTS)} pass")
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
