#!/usr/bin/env python3
# COPIED VERBATIM from PR #8707 (branch claude/beta-routes-two-term-rerun-2026-11-21) for its word
# definitions and engine; imported as a module, its main() is not run here.
"""qou-99qc: the beta-decay routes P1/P4, P2, P3, L, N2 re-run under the covariant two-term trace.

Pre-registered: PREREGISTRATION.md (commit d38166d1cb), before any number. Engine: two_term_engine.py.

Words are copied verbatim (same letters, same conventions) from:
  P1/P4  branch claude/beta-gs-reduction-n-gammagamma-2026-11-20 (#8681), beta_gs_reduction_probe.py
         WORDS / build() / POINTS / sector definitions;
  P2     branch claude/beta-entangled-lepton-pair-2026-11-20 (#8680), qbeta_entangled_lepton_pair_probe.py
         B3 / nuc11 / final / full_twist / family_d_word;
  N2     branch claude/qbeta-n2-derived-nucleon-elements-2026-11-20 (#8636), words V1V2, V2V1, V1V1V1
         (V_i = σ_i σ_{i+1}^{-1}, 1-based) on the M4 lepton-strand model;
  L      branch claude/beta-additive-logtrace-energy-2026-11-21 (#8693): its balances are functions of
         the P1/P2 traces above, so its two-term shift is d/dc_em of those logs (read-only on #8693).
The photon is the ruled γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹ (owner 2026-11-20).

Each quantity is computed three times: exactly at q = 2 and q = 3/2 (Fraction; exact zero tests),
and in mpmath at the proton q₀, 70 dps. q → 1 orders are read off exact Fraction evaluations at
q = 1 + 10⁻³ and 1 + 10⁻⁴ (an estimate from exact arithmetic, labelled as such). The two-term
coefficient c_em is NOT chosen: rows report t₂ and t₂/t₁ = d log t / d c_em.
Run: python3 -u beta_routes_two_term_probe.py 2>&1 | tee /tmp/beta_routes_two_term.log
"""
from __future__ import annotations

import sys
import time
from fractions import Fraction as Fr
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parents[2]
for _p in ("computations", "tools/qou-substrate/python", str(_HERE)):
    sys.path.insert(0, str(_ROOT / _p) if not _p.startswith("/") else _p)

import mpmath as mp  # noqa: E402

import qou_substrate.constants as C  # noqa: E402
from qou_substrate.precision import fmt  # noqa: E402
import two_term_engine as E  # noqa: E402

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

COL_A = ("quark",) * 3 + ("lepton",) * 3
COL_B = ("quark",) * 3 + ("lepton",) + ("neutral",) * 2
COL_U6 = ("quark",) * 6
Q3 = ("quark",) * 3


def L(letters, coef=None):
    return [(E.ONE if coef is None else coef, list(letters))]


def word(*letter_lists):
    """product of single-monomial factors."""
    return [L(w) for w in letter_lists if w]


def photon(s, a0, a1, a2):
    return [(E.ONE, []), (a0, [s]), (a1, [s + 1]), (a2, [s, -(s + 1) - 1])]


# ── P1 / P4 ───────────────────────────────────────────────────────────────────────────────────
BETA = [0, -2] * 3
P1_WORDS = {
    "W0_split": ([], []),
    "W1_one_bridge": ([2], []),
    "W1sq_clasp": ([2, 2], []),
    "W2_two_same": ([2], [2]),
    "W2b_two_opposite": ([2], [-3]),
    "W3_loop_around_2": ([2, 1, 1, 2], []),
    "W4_loop_around_3": ([2, 1, 0, 0, 1, 2], []),
    "W4b_two_pair_strands_loop": ([3, 2, 2, 3], []),
    "W6_passage_and_return": ([2, 1, 0], [0, 1, 2]),
    "W7_passage_after_pair": ([], [0, 1, 2]),
}


def points():
    hq = E.q - E.ONE / E.q
    z = E.ZERO
    return {"bare": [z] * 6, "borromean": [z, z, E.q * hq, z, z, -hq / E.q]}


def gamma_factors(shift, pt):
    return [photon(shift, *pt[:3]), photon(shift, *pt[3:])]


def p1_element(pre, post, pt, N=6, shift=3):
    return [L(BETA)] + ([L(pre)] if pre else []) + gamma_factors(shift, pt) + ([L(post)] if post else [])


def ratio(a, b):
    return a / b if b != 0 else None


def p1_rows():
    out = {}
    for pk, pt in points().items():
        rb = E.rho_blocks(3, [L(BETA)])
        t1b = E.t_one(3, rb)
        rg = E.rho_blocks(3, gamma_factors(0, pt))
        t1g = E.t_one(3, rg)
        t2g = {c: E.t_two(col, rg) for c, col in (("A", ("lepton",) * 3), ("B", ("lepton", "neutral", "neutral")))}
        t2b = E.t_two(Q3, rb)
        for name, (pre, post) in P1_WORDS.items():
            r = E.rho_blocks(6, p1_element(pre, post, pt))
            rB = E.rho_blocks(6, [L(pre + post)]) if (pre or post) else E.rho_blocks(6, [L([])])
            t1 = E.t_one(6, r)
            t1B = E.t_one(6, rB)
            rec = {"t1": t1, "C1": t1 - t1b * t1g * t1B, "R1": ratio(t1, t1b * t1g * t1B)}
            for c, col in (("A", COL_A), ("B", COL_B)):
                t2 = E.t_two(col, r)
                t2B = E.t_two(col, rB)
                rec[f"t2_{c}"] = t2
                rec[f"t2_over_t1_{c}"] = ratio(t2, t1)
                rec[f"dlogR_{c}"] = t2 / t1 - t2b / t1b - t2g[c] / t1g - t2B / t1B
                rec[f"t2raw_{c}"] = E.t_two(col, r, "rawconn")
            rec["t2_U"] = E.t_two(COL_U6, r)
            # P4 sector traces (K-weighted, dim-normalised by 12 as #8681)
            ins_nonuc = None
            nn = lambda b: sum(1 if x == 0 else -1 for x in b[:3]) == -1 and b[3] == 0  # noqa: E731
            pe = lambda b: sum(1 if x == 0 else -1 for x in b[:3]) == +1 and b[3] == 1  # noqa: E731
            rec["P4_D1"] = (E.sector_trace(6, r, nn) - E.sector_trace(6, r, pe)) / 12
            for c, col in (("A", COL_A), ("B", COL_B)):
                ins = {m: v["cov"] for m, v in E.insertions(col).items()}
                insr = {m: v["rawconn"] for m, v in E.insertions(col).items()}
                rec[f"P4_D2_{c}"] = (E.sector_trace(6, r, nn, ins) - E.sector_trace(6, r, pe, ins)) / 12
                rec[f"P4_D2raw_{c}"] = (E.sector_trace(6, r, nn, insr) - E.sector_trace(6, r, pe, insr)) / 12
            del ins_nonuc
            out[f"{name}|{pk}"] = rec
    # W5: five strands, pair on 2-4 (shared strand 2)
    for pk, pt in points().items():
        r = E.rho_blocks(5, [L(BETA)] + gamma_factors(2, pt))
        t1 = E.t_one(5, r)
        rec = {"t1": t1}
        for c, col in (("A", Q3 + ("lepton",) * 2), ("Ashared", ("quark",) * 2 + ("lepton",) * 3)):
            rec[f"t2_{c}"] = E.t_two(col, r)
        out[f"W5_shared_strand|{pk}"] = rec
    return out


# ── P2 ────────────────────────────────────────────────────────────────────────────────────────
def p2_defs():
    one, z, hh = E.ONE, E.ZERO, E.q - E.ONE / E.q
    half = one / 2

    def letter(g, c=None, d=None):
        return (g, one if c is None else c, z if d is None else d)

    def inv(g):
        return (g, one, -hh)

    B3 = [letter(0), inv(1)] * 3

    def nuc11(kind):
        w = list(B3)
        if kind == "p":
            w += [letter(0), letter(0, d=-hh * half), letter(1, d=-hh * half)]
        else:
            w += [letter(0, d=-hh * half), letter(0, d=-hh * half), letter(1, d=-hh)]
        w += [letter(0), letter(0)]
        return w

    def power(g, k):
        return [letter(g)] * k if k >= 0 else [inv(g)] * (-k)

    TREFOIL = power(0, 3)

    def shift(w, s):
        return [(g + s, c, d) for g, c, d in w]

    def final(pw, j, k):
        return list(pw) + power(2, 2 * j) + shift(TREFOIL, 3) + power(4, 2 * k)

    def full_twist(gens, t):
        m = len(gens) + 1
        if t >= 0:
            return [letter(g) for g in gens] * (m * t)
        return [inv(g) for g in reversed(gens)] * (m * (-t))

    def family_d_word(pw, span, t, k):
        return list(pw) + full_twist(span, t) + shift(TREFOIL, 3) + power(4, 2 * k)

    def to_elem(w):
        return [[(c, [g]), (d, [])] for g, c, d in w]

    return B3, nuc11, TREFOIL, final, family_d_word, to_elem


def p2_rows():
    B3, nuc11, TREFOIL, final, family_d_word, to_elem = p2_defs()
    nucs = {"p": nuc11("p"), "n": nuc11("n"), "beta_Bor": B3}
    out = {"objects": {}, "familyA": {}, "familyD": {}}
    for k, w in nucs.items():
        r = E.rho_blocks(3, to_elem(w))
        out["objects"][k] = {"t1": E.t_one(3, r), "t2": E.t_two(Q3, r)}
    re_ = E.rho_blocks(2, to_elem(TREFOIL))
    out["objects"]["e-"] = {"t1": E.t_one(2, re_), "t2": E.t_two(("lepton",) * 2, re_)}
    for j in (-1, 0, 1):
        for k in (-1, 0, 1):
            row = {}
            for pk, pw in nucs.items():
                r = E.rho_blocks(6, to_elem(final(pw, j, k)))
                t1, t2 = E.t_one(6, r), E.t_two(COL_A, r)
                row[pk] = {"t1": t1, "t2": t2, "t2_over_t1": t2 / t1}
            out["familyA"][f"j={j},k={k}"] = row
    for span_name, span in (("D3_strands_2_4", [1, 2]), ("D4_strands_1_4", [0, 1, 2])):
        for t in (-1, 1):
            for k in (-1, 0, 1):
                row = {}
                for pk, pw in nucs.items():
                    r = E.rho_blocks(6, to_elem(family_d_word(pw, span, t, k)))
                    t1, t2 = E.t_one(6, r), E.t_two(COL_A, r)
                    row[pk] = {"t1": t1, "t2": t2, "t2_over_t1": t2 / t1,
                               "C1": t1 - out["objects"][pk]["t1"] * out["objects"]["e-"]["t1"]}
                out["familyD"][f"{span_name},t={t},k={k}"] = row
    return out


# ── N2 (M4 model) ─────────────────────────────────────────────────────────────────────────────
N2_WORDS = {"V1V2": [0, -2, 1, -3], "V2V1": [1, -3, 0, -2], "V1V1V1": [0, -2] * 3}


def h3_projectors_on_4():
    """central idempotents of H_3 (strands 0-2) on each W_m of V^{⊗4}: (3) q^6, (2,1) q^0, (1³) q^-6."""
    D = E.rho_blocks(4, [L(E.full_twist_letters(3, [0, 1]))])
    ev = {"(3)": E.q ** 6, "(2,1)": E.ONE, "(1,1,1)": E.q ** -6}
    out = {}
    for m, M in D.items():
        d = len(M)
        P = {}
        for lam, e in ev.items():
            X = E.eye(d)
            for lam2, e2 in ev.items():
                if lam2 != lam:
                    X = E.mm(X, E.lin((E.ONE / (e - e2), M), (-e2 / (e - e2), E.eye(d))))
            P[lam] = X
        out[m] = P
    return out


def n2_rows():
    col = Q3 + ("lepton",)
    ins = E.insertions(col)
    Pm = h3_projectors_on_4()
    bl = E.blocks(4)
    sect = {"N": lambda b: sum(1 if x == 0 else -1 for x in b[:3]) == -1 and b[3] == 0,
            "P": lambda b: sum(1 if x == 0 else -1 for x in b[:3]) == 1 and b[3] == 1}
    out = {}
    for name, w in N2_WORDS.items():
        r = E.rho_blocks(4, [L(w)])
        M0 = r[0]
        rec = {}
        for s, pred in sect.items():
            Pi = E.diag([E.ONE if pred(b) else E.ZERO for b in bl[0]])
            for lam in ("(3)", "(2,1)"):
                Proj = E.mm(Pi, Pm[0][lam])
                rec[f"{s}{lam}_one"] = E.tr(E.mm(Proj, M0))
                rec[f"{s}{lam}_two_cov"] = E.tr(E.mm(Proj, E.mm(ins[0]["cov"], M0)))
        out[name] = rec
    return out


# ── structural checks and closed forms (symbolic) ──────────────────────────────────────────────
def symbolic_block():
    from sympy import factor
    E.use()
    res = {}
    ins = E.insertions(("quark", "lepton"))
    res["N2_quark_lepton_W0_c_minus_mean"] = {k: str(factor((v - ins[0]["mean"]).as_expr()))
                                              for k, v in ins[0]["Ecoef"].items()}
    for kpow in (1, 2, 3):
        r = E.rho_blocks(2, [L([0] * kpow)])
        res[f"t2_sigma^{kpow}_quark_lepton"] = str(factor(E.t_two(("quark", "lepton"), r).as_expr()))
        res[f"t1_sigma^{kpow}"] = str(factor(E.t_one(2, r).as_expr()))
    for col in (("quark",) * 3 + ("lepton",), ("quark", "quark", "lepton"), ("quark",) * 4):
        ins = E.insertions(col)
        res[f"Ecoef_minus_mean {'-'.join(c[0] for c in col)}"] = {
            m: {k: str(factor((v - ins[m]["mean"]).as_expr())) for k, v in ins[m]["Ecoef"].items()}
            for m in sorted(ins)}
    # route-word closed forms on 4 strands: β_Bor ⊗ lepton strand, with and without a wrap
    for nm, letters in (("beta(x)1", BETA), ("beta.s2^2 (lepton wraps strand 2)", BETA + [2, 2]),
                        ("beta.s2.s1.s1.s2 (lepton loops 2 nucleon strands)", BETA + [2, 1, 1, 2])):
        r = E.rho_blocks(4, [L(letters)])
        res[f"t1 {nm}"] = str(factor(E.t_one(4, r).as_expr()))
        res[f"t2 {nm} qqql"] = str(factor(E.t_two(Q3 + ("lepton",), r).as_expr()))
    return res


def evaluate_all():
    return {"P1P4": p1_rows(), "P2": p2_rows(), "N2": n2_rows()}


def flat(d, p=""):
    if isinstance(d, dict):
        for k, v in d.items():
            yield from flat(v, f"{p}/{k}")
    else:
        yield p, d


def order_at_one(v3, v4):
    """exact values at q = 1+1e-3, 1+1e-4 -> estimated power of (q-1)."""
    if v3 == 0 or v4 == 0:
        return None
    return round(float(mp.log(abs(mp.mpf(v3.numerator) / v3.denominator / (mp.mpf(v4.numerator) / v4.denominator))) / mp.log(10)))


def main():
    log(f"q0 (proton) = {mp.nstr(Q0, 30)}")
    runs = {}
    for tag, qv in (("q2", Fr(2)), ("q3/2", Fr(3, 2)), ("q1+1e-3", Fr(1001, 1000)), ("q1+1e-4", Fr(10001, 10000))):
        E.use(qv, Fr(1))
        # engine validation on this field
        zD = E.q ** 3 / (E.q ** 2 + 1)
        check(f"[{tag}] t1(σ) = z_D", E.t_one(3, E.rho_blocks(3, [L([0])])) == zD)
        hh = E.h
        check(f"[{tag}] t1(β_Bor) = Lean closed form",
              E.t_one(3, E.rho_blocks(3, [L(BETA)])) == (4 + hh ** 2 - 3 * hh ** 4 - hh ** 6) / (hh ** 2 + 4))
        runs[tag] = evaluate_all()
        log(f"evaluated at {tag}")
    E.use(Q0, mp.mpf(1), exact=False, tol=mp.mpf(10) ** -55)
    runs["q0"] = evaluate_all()
    log("evaluated at q0")
    exact_keys = dict(flat(runs["q2"]))
    exact_keys2 = dict(flat(runs["q3/2"]))
    o3, o4 = dict(flat(runs["q1+1e-3"])), dict(flat(runs["q1+1e-4"]))
    table = {}
    for k, v in flat(runs["q0"]):
        a, b = exact_keys[k], exact_keys2[k]
        zero = (a == 0 and b == 0) if (a is not None and b is not None) else None
        table[k] = {"q0": fmt(v) if v is not None else None, "exact_zero": zero,
                    "order_(q-1)_est": order_at_one(o3[k], o4[k]) if (o3[k] is not None and o4[k] is not None and not zero) else None}
    # ---- pre-registered checks
    P1 = {k: v for k, v in table.items() if k.startswith("/P1P4/")}
    check("PR1: colouring U (all strands quark) gives t2 = 0 exactly on every P1 word",
          all(v["exact_zero"] for k, v in P1.items() if k.endswith("/t2_U")))
    check("PR2-variant: β_Bor alone (3 quark strands) has t2 = 0 (P2 objects)",
          all(table[f"/P2/objects/{n}/t2"]["exact_zero"] for n in ("p", "n", "beta_Bor", "e-")))
    check("PR3: raw (non-covariant) connected is non-zero on W0 split, colouring A",
          not table["/P1P4/W0_split|bare/t2raw_A"]["exact_zero"])
    check("PR4: covariant t2 non-zero on W0 split, colouring A (static-colour effect, not exchange)",
          not table["/P1P4/W0_split|bare/t2_A"]["exact_zero"])
    out = {"table": table}
    # colour-block covariance (comparison): Q_pair is constant on every joint eigenspace of the
    # block totals (quark block, lepton block, neutral block) -> its sector-connected part is 0
    # for every word (Lean pairSum_union + pairSum_eq_of_total_eq).
    E.use(Fr(2), Fr(1))
    ok = True
    for col in (COL_A, COL_B, Q3 + ("lepton",), ("quark", "lepton")):
        groups = {}
        for b in __import__("itertools").product((0, 1), repeat=len(col)):
            key = tuple(sum(1 if x == 0 else -1 for x, c in zip(b, col) if c == k)
                        for k in ("quark", "lepton", "neutral"))
            groups.setdefault(key, set()).add(E.qpair_diag(col, b))
        ok &= all(len(v) == 1 for v in groups.values())
    check("colour-block sectors: Q_pair constant on each (so colour-block-covariant t2 = 0 on every word)", ok)
    # derived summaries at q0
    E.use(Q0, mp.mpf(1), exact=False, tol=mp.mpf(10) ** -55)
    m_mu = ME * 2 * mp.clsin(2, mp.pi / 3) / (1 - 1 / Q0) ** 2
    S6 = m_mu * mp.fprod([(Q0 ** k - Q0 ** -k) / (Q0 - 1 / Q0) for k in range(1, 7)]) / Q0 ** 6
    summ = {"S6_MeV (P4 scale, #8681)": fmt(S6)}
    for w in ("W0_split", "W1_one_bridge", "W7_passage_after_pair"):
        d2 = mp.mpf(table[f"/P1P4/{w}|bare/P4_D2_A"]["q0"])
        summ[f"P4 {w} S6*D2_A per unit c_em (MeV)"] = fmt(S6 * d2)
        summ[f"P4 {w} c_em that would put S6*D2_A at CODATA Q_beta (comparison only)"] = fmt(
            (mp.mpf(C.M_N_MEV_STR) - mp.mpf(C.M_P_MEV_STR) - ME) / (S6 * d2))
    thr = {}
    for w in N2_WORDS:
        for s_ in ("N", "P"):
            for lam in ("(3)", "(2,1)"):
                one = mp.mpf(table[f"/N2/{w}/{s_}{lam}_one"]["q0"])
                two = mp.mpf(table[f"/N2/{w}/{s_}{lam}_two_cov"]["q0"])
                thr[f"{w} {s_}{lam}"] = fmt(-one / two)
    summ["N2 c_em at which each reading-3 trace changes sign (first order)"] = thr
    out["summaries"] = summ
    log("symbolic closed forms")
    out["closed_forms"] = symbolic_block()
    check("N=2 quark-lepton: E(Q)^conn coefficient = ±(q²−1)/(3(q²+1)) (Lean BetaRoutesTwoTerm)",
          out["closed_forms"]["N2_quark_lepton_W0_c_minus_mean"] ==
          {0: "(q - 1)*(q + 1)/(3*(q**2 + 1))", 1: "-(q - 1)*(q + 1)/(3*(q**2 + 1))"})
    out["comparison"] = {"Q_beta_codata_MeV": fmt(mp.mpf(C.M_N_MEV_STR) - mp.mpf(C.M_P_MEV_STR) - ME),
                         "m_e_MeV": fmt(ME)}
    from qou_substrate.witness import WitnessBuilder  # noqa: PLC0415
    wb = WitnessBuilder("beta-routes-two-term", engine="python", start_time=T0, output_dir=_HERE)
    wb.set_description("qou-99qc: beta routes P1/P4, P2, P3, L, N2 re-run under the covariant two-term "
                       "(all-pairs charge, E-projected, quantum-trace weighted) trace. Pre-registered at "
                       "d38166d1cb. Not wired to any scorecard; c_em not chosen.")
    wb.add_parameter("q0", fmt(Q0))
    wb.add_parameter("dps", DPS)
    wb.add_parameter("trace", "quantum trace Tr(K^N .)/[2]_q^N = Ocneanu at z_D = q^3/(q^2+1)")
    wb.add_parameter("charges", "quark u 2/3 d -1/3; lepton u=nu 0 d=e- -1 (C-lep, assumed); neutral 0")
    wb.add_data("results", out)
    for a_ in ASSERTS:
        wb.add_assertion(a_["name"], computed=str(int(a_["ok"])), expected="1", tolerance="0", source=a_["note"])
    path = wb.save({"q0Anchor": "proton"})
    fails = [a_ for a_ in ASSERTS if not a_["ok"]]
    log(f"witness -> {path}; {len(ASSERTS) - len(fails)}/{len(ASSERTS)} pass")
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
