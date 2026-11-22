#!/usr/bin/env python3
"""he4_closed_form_probe.py: the 4He gamma-gamma binding of ../he4_gg_all_pairs in
closed form (issue #8960, item 4). PROBE, adopts nothing.

What the gamma-gamma probe assembles (read from he4_gg_all_pairs_probe.py):
  * nucleon blocks N_k = the 11-letter production blocks of
    mass_at_3A_proper.atom_braid_word_3A(Z, N, include_inter=False), block k on
    strands 3k..3k+2, order p..p n..n (4He: p p n n);
  * bond G^3 = (sigma_{3j-1} sigma_{3j}^{-1})^3 = V^3 shifted to 3j-1, placed after
    block j (chain), or conjugated by the over/under transport T_ij (all pairs);
  * Markov trace at z_D = q^3/(q^2+1), tr(1) = 1, sigma^2 = h sigma + 1;
  * B_diff = E0 (tr_free - tr_atom), B_log = E0 ln(tr_free/tr_atom).

Results:
  1. Chain (proved, MarkovTraceGammaGammaChain.lean): tr_atom = tr N0 * prod_{j>=1} b(N_j),
     b(N) = tr(V^3 N^{(1)}); tr_free = prod tr N_j. Symbolic in q, exact at q0.
  2. All pairs: no single-nucleon factorisation. Split measured into
     pairwise product * convergence factor * crossing remainder, where the
     convergence factor rho_k(N) (k bonds landing on one nucleon) is a
     single-nucleon closed form on k+3 strands and the crossing remainder is
     what is left; A = 3 all-pairs traces recomputed exactly (N0 factored out,
     towerTr_disjoint) and checked against the witness.

Exact arithmetic only: sympy QQ(q) field and fractions.Fraction at the rational
proton pin; mpmath only to print. No float.
"""
from __future__ import annotations

import json
import sys
import time
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMP = HERE.parents[1]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(COMP))
sys.path.insert(0, str(COMP / "substrate"))

import _path_bridge  # noqa: E402, F401
import mpmath as mp  # noqa: E402

from q_parameter import Q_50_DIGIT_STR  # noqa: E402  (proton pin)
from witness_base import WitnessBuilder  # noqa: E402
from hecke_exact import Ring  # noqa: E402

mp.mp.dps = 80
T0 = time.time()
GG_WITNESS = COMP / "probes" / "he4_gg_all_pairs" / "he4-gg-all-pairs.witness.json"


def log(msg):
    print(f"[{time.time() - T0:7.1f}s] {msg}", flush=True)


def to_mp(x):
    if isinstance(x, Fraction):
        return mp.mpf(x.numerator) / x.denominator
    return mp.mpf(x)


def digits(a, b):
    """Agreement in significant digits between two mpf values."""
    d = abs(a - b)
    if d == 0:
        return "exact to stored precision"
    return mp.nstr(-mp.log10(d / abs(b)), 4)


def conv_word(R, N, k, variant="over"):
    """k external strands 0..k-1 each bonded (V^3 on k-1, k) to the nucleon on
    strands k..k+2; strand s is carried to k-1 by sigma_s...sigma_{k-2} and back."""
    w = []
    for s in range(k - 1, -1, -1):
        gens = list(range(s, k - 1))
        up, dn = (R.S, R.I) if variant == "over" else (R.I, R.S)
        w += [up(g) for g in gens] + R.V3(k - 1) + [dn(g) for g in reversed(gens)]
    return w + N(k)


def G3(R, j):
    return [R.S(3 * j - 1), R.I(3 * j)] * 3


def tG3(R, i, j, variant):
    gens = list(range(3 * i + 2, 3 * j - 1))
    up, dn = (R.S, R.I) if variant == "over" else (R.I, R.S)
    return [up(g) for g in gens] + G3(R, j) + [dn(g) for g in reversed(gens)]


def build(R, blocks, bonds, variant):
    """Same placement rule as he4_gg_all_pairs_probe.build (running max J)."""
    A = len(blocks)
    after = {k: [] for k in range(A)}
    J = 0
    for i, j in bonds:
        J = max(J, j)
        after[J] += tG3(R, i, j, variant)
    w = []
    for k in range(A):
        w += [(a, b, g + 3 * k) for a, b, g in blocks[k]] + after[k]
    return w


def main():
    gg = json.loads(GG_WITNESS.read_text())["data"]
    rows = gg["rows"]
    E0 = mp.mpf(gg["E0_MeV"])  # taken from the gamma-gamma witness, not re-derived here

    # ---------------- symbolic single-nucleon factors over Q(q)
    S = Ring()
    sym = {
        "tr_p": S.tr(3, S.proton()), "tr_n": S.tr(3, S.neutron()),
        "b_p": S.tr(4, S.V3() + S.proton(1)), "b_n": S.tr(4, S.V3() + S.neutron(1)),
        "tr_V3": S.tr(3, S.V3()),
    }
    h, z = S.h, S.z
    assert sym["tr_V3"] == 1 - h ** 4 + h ** 4 * z ** 2 - h ** 5 * z
    sym["mu_p_minus_1"] = sym["b_p"] / sym["tr_p"] - 1
    sym["mu_n_minus_1"] = sym["b_n"] / sym["tr_n"] - 1
    for k in (2, 3):
        sym[f"rho{k}_n"] = S.tr(k + 3, conv_word(S, S.neutron, k)) / sym["tr_n"]
        sym[f"rho{k}_p"] = S.tr(k + 3, conv_word(S, S.proton, k)) / sym["tr_p"]
    log("symbolic factors done")
    # q = 1
    at1 = {k: str(v.numer.as_expr().subs("q", 1) / v.denom.as_expr().subs("q", 1))
           for k, v in sym.items()}
    log(f"q = 1: {at1}")

    # ---------------- exact at the proton pin
    R = Ring(Q_50_DIGIT_STR)
    ex = {"tr_p": R.tr(3, R.proton()), "tr_n": R.tr(3, R.neutron()),
          "b_p": R.tr(4, R.V3() + R.proton(1)), "b_n": R.tr(4, R.V3() + R.neutron(1))}
    mu_p, mu_n = ex["b_p"] / ex["tr_p"], ex["b_n"] / ex["tr_n"]
    rho = {}
    for k in (2, 3):
        for v in ("over", "under"):
            rho[(k, v)] = R.tr(k + 3, conv_word(R, R.neutron, k, v)) / ex["tr_n"]
    assert rho[(2, "over")] == rho[(2, "under")] and rho[(3, "over")] == rho[(3, "under")]
    # order of the three converging bonds does not matter either (checked: all 3! orders)
    import itertools
    r3_orders = set()
    for perm in itertools.permutations(range(3)):
        w = []
        for s in perm:
            gens = list(range(s, 2))
            w += [R.S(g) for g in gens] + R.V3(2) + [R.I(g) for g in reversed(gens)]
        r3_orders.add(R.tr(6, w + R.neutron(3)) / ex["tr_n"])
    assert len(r3_orders) == 1 and r3_orders.pop() == rho[(3, "over")]
    rho2, rho3 = rho[(2, "over")], rho[(3, "over")]
    log("exact proton-pin factors done")

    P, N = ex["tr_p"], ex["tr_n"]
    chain_model = {
        "2H": (P * N, mu_n), "3H": (P * N * N, mu_n ** 2),
        "3He": (P * P * N, mu_p * mu_n), "4He": (P * P * N * N, mu_p * mu_n ** 2),
    }
    checks, chain_rows = {}, []
    for atom, (tf, ratio) in chain_model.items():
        wr = next(r for r in rows if r["atom"] == atom and r["route"] == "gg chain")
        tA = tf * ratio
        Bd = E0 * (to_mp(tf) - to_mp(tA))
        chain_rows.append({
            "atom": atom, "tr_free": mp.nstr(to_mp(tf), 50), "tr_atom": mp.nstr(to_mp(tA), 50),
            "ratio": mp.nstr(to_mp(ratio), 50), "B_diff_MeV": mp.nstr(Bd, 40),
            "digits_tr_free_vs_witness": digits(to_mp(tf), mp.mpf(wr["tr_free"])),
            "digits_tr_atom_vs_witness": digits(to_mp(tA), mp.mpf(wr["tr_atom"])),
            "digits_ratio_vs_witness": digits(to_mp(ratio), mp.mpf(wr["ratio_atom_over_free"])),
            "digits_B_diff_vs_witness": digits(Bd, mp.mpf(wr["B_diff_MeV"])),
        })
        checks[f"{atom}_chain_ratio_gap"] = abs(to_mp(ratio) - mp.mpf(wr["ratio_atom_over_free"]))
        log(f"{atom} chain: ratio {mp.nstr(to_mp(ratio), 30)}  witness {wr['ratio_atom_over_free']}")

    # ---------------- 4He chain, term by term
    tf4 = to_mp(P * P * N * N)
    ep, en = to_mp(mu_p - 1), to_mp(mu_n - 1)
    terms = {
        "eps_p (bond into nucleon 1, a proton)": -E0 * tf4 * ep,
        "2 eps_n (bonds into nucleons 2, 3, neutrons)": -E0 * tf4 * 2 * en,
        "2 eps_p eps_n + eps_n^2 (second order)": -E0 * tf4 * (2 * ep * en + en ** 2),
        "eps_p eps_n^2 (third order)": -E0 * tf4 * ep * en ** 2,
    }
    he4_chain_terms = {k: mp.nstr(v * 1000, 20) + " keV" for k, v in terms.items()}
    total = sum(terms.values())
    assert abs(total - E0 * (tf4 - to_mp(P * P * N * N * mu_p * mu_n ** 2))) < mp.mpf(10) ** -70
    log(f"4He chain B_diff = {mp.nstr(total * 1000, 20)} keV")

    # ---------------- A = 3 all pairs, exact (N0 factored out by towerTr_disjoint)
    A3_bonds = [(0, 1), (1, 2), (0, 2)]
    a3_rows = []
    for atom, blocks in (("3H", [R.proton(), R.neutron(), R.neutron()]),
                         ("3He", [R.proton(), R.proton(), R.neutron()])):
        tN = [R.tr(3, b) for b in blocks]
        for v in ("over", "under"):
            w = build(R, blocks, A3_bonds, v)
            assert w[:11] == blocks[0]
            rest = [(a, b, g - 2) for a, b, g in w[11:]]
            assert min(g for _, _, g in rest) >= 0
            ratio = R.tr(7, rest) / (tN[1] * tN[2])
            wr = next(r for r in rows if r["atom"] == atom and r["route"] == "all pairs"
                      and r["variant"] == v)
            a3_rows.append({"atom": atom, "variant": v, "ratio_exact": mp.nstr(to_mp(ratio), 50),
                            "digits_vs_witness": digits(to_mp(ratio), mp.mpf(wr["ratio_atom_over_free"]))})
            checks[f"{atom}_allpairs_{v}_gap"] = abs(to_mp(ratio) - mp.mpf(wr["ratio_atom_over_free"]))
            log(f"{atom} all pairs {v}: exact {mp.nstr(to_mp(ratio), 30)}  witness {wr['ratio_atom_over_free']}")

    # ---------------- 4He all pairs, split against the witness rows
    pairwise = to_mp(mu_p * mu_n ** 5)       # each bond -> mu of its right nucleon
    convergent = to_mp(mu_p * rho2 * rho3)    # bonds landing on one nucleon taken together
    he4_rows = []
    for r in rows:
        if r["atom"] != "4He" or r["route"] == "gg chain":
            continue
        meas = mp.mpf(r["ratio_atom_over_free"])
        Bm = mp.mpf(r["B_diff_MeV"])
        B_pair = -E0 * tf4 * (pairwise - 1)
        B_conv = -E0 * tf4 * (convergent - pairwise)
        B_cross = -E0 * tf4 * (meas - convergent)
        he4_rows.append({
            "route": r["route"], "variant": r["variant"], "ratio_witness": r["ratio_atom_over_free"],
            "crossing_factor": mp.nstr(meas / convergent, 20),
            "B_diff_witness_keV": mp.nstr(Bm * 1000, 15),
            "B_pairwise_keV": mp.nstr(B_pair * 1000, 15),
            "B_convergence_keV": mp.nstr(B_conv * 1000, 15),
            "B_crossing_keV": mp.nstr(B_cross * 1000, 15),
            "sum_minus_witness_keV": mp.nstr((B_pair + B_conv + B_cross - Bm) * 1000, 5),
        })
        log(f"4He {r['route']:14s} {r['variant']:5s} pair {mp.nstr(B_pair*1e3, 8)} "
            f"conv {mp.nstr(B_conv*1e3, 8)} cross {mp.nstr(B_cross*1e3, 8)} keV")

    def fs(x):
        return str(x)

    wb = WitnessBuilder("he4-closed-form", engine="sympy QQ(q) field + fractions.Fraction (hecke_exact.py)",
                        output_dir=HERE)
    wb.set_description(
        "PROBE, adopts nothing (issue #8960 item 4). Closed form of the 4He gamma-gamma "
        "binding of probes/he4_gg_all_pairs. Chain: tr_atom = tr N0 * prod_{j>=1} tr(V^3 N_j^(1)) "
        "(Lean: MarkovTraceGammaGammaChain.towerTr_he4_ggChain_word), exact in Q(q) and at the "
        "proton pin. All pairs: no single-nucleon factorisation; split into pairwise product, "
        "convergence factors rho_k(N) (closed form) and a measured crossing remainder.")
    wb.add_data("assembly", {
        "blocks": "atom_braid_word_3A(Z,N,include_inter=False), 11 letters per nucleon, order p..p n..n",
        "bond": "G^3 = (sigma_{3j-1} sigma_{3j}^-1)^3 after block j; non-neighbours conjugated by T_ij over/under",
        "trace": "Markov, z_D = q^3/(q^2+1), h = q - 1/q, tr(1) = 1",
        "B_diff": "E0 (tr_free - tr_atom)", "E0_MeV_source": "he4-gg-all-pairs.witness.json E0_MeV",
    })
    wb.add_data("closed_forms_Qq", {k: fs(v) for k, v in sym.items()})
    wb.add_data("closed_forms_at_q_equals_1", at1)
    wb.add_data("he4_chain_formula",
                "tr_atom = tr_p * b_p * b_n^2, tr_free = tr_p^2 tr_n^2, ratio = mu_p mu_n^2, "
                "B_diff = E0 tr_p (tr_p tr_n^2 - b_p b_n^2), mu_N = b_N / tr_N")
    wb.add_data("proton_pin_values", {
        "tr_p": mp.nstr(to_mp(P), 50), "tr_n": mp.nstr(to_mp(N), 50),
        "b_p": mp.nstr(to_mp(ex["b_p"]), 50), "b_n": mp.nstr(to_mp(ex["b_n"]), 50),
        "mu_p": mp.nstr(to_mp(mu_p), 50), "mu_n": mp.nstr(to_mp(mu_n), 50),
        "rho2_n": mp.nstr(to_mp(rho2), 50), "rho3_n": mp.nstr(to_mp(rho3), 50),
        "rho2_n_over_mu_n_sq": mp.nstr(to_mp(rho2 / mu_n ** 2), 30),
        "rho3_n_over_mu_n_cubed": mp.nstr(to_mp(rho3 / mu_n ** 3), 30),
        "pairwise_mu_p_mu_n5": mp.nstr(pairwise, 40), "convergent_mu_p_rho2_rho3": mp.nstr(convergent, 40),
    })
    wb.add_data("chain_rows", chain_rows)
    wb.add_data("he4_chain_terms", he4_chain_terms)
    wb.add_data("he4_chain_B_diff_keV", mp.nstr(total * 1000, 30))
    wb.add_data("a3_all_pairs_exact", a3_rows)
    wb.add_data("he4_all_pairs_split", he4_rows)
    for k, v in checks.items():
        wb.add_assertion(k, computed=v, expected=0, tolerance=mp.mpf("1e-28"),
                         source="witness ratios are stored to 30 significant digits")
    wb.save({"q0Anchor": "proton"})
    log("witness written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
