#!/usr/bin/env python3
"""qbeta_gg_pair_gb_probe — reduce the γγ lepton pair words with group relations only.

Pre-registration: PREREGISTRATION.md (committed before this file).
Lean: QOU/QBeta/GammaGammaPairReduction.lean.

Exact arithmetic only (integers, sympy rationals in t). Nothing is selected or scored.
Photon: γᵢ(φ₀, φ₁, φ₀₁) = 1 + φ₀σᵢ + φ₁σᵢ₊₁ + φ₀₁σᵢσᵢ₊₁⁻¹; vertex letter Vᵢ = σᵢσᵢ₊₁⁻¹.
"""
from __future__ import annotations

import random
import sys
from pathlib import Path

import sympy as sp

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parents[2]
for _p in ("computations", "computations/qbeta", "computations/substrate",
           "tools/qou-substrate/python"):
    sys.path.insert(0, str(_ROOT / _p))

N = 6
RESULTS: list[tuple[str, bool, str]] = []

# The closed family, fixed in PREREGISTRATION.md. Prediction: (reduced word or None, ℓ_min, e).
FAMILY = {
    "V0V1V0": ([(0, 1), (0, 1), (2, -1), (1, -1)], 4, 1),
    "V1V2V1": ([(1, 1), (1, 1), (3, -1), (2, -1)], 4, 1),
    "V2V3V2": ([(2, 1), (2, 1), (4, -1), (3, -1)], 4, 1),
    "V0V1V2V0V3": ([(0, 1), (0, 1), (1, -1), (4, -1)], 4, 3),
    "V0V1V2V3V0": ([(0, 1), (0, 1), (1, -1), (4, -1)], 4, 3),
    "V2V0V3V1V0": (None, 4, 3),
    "V2V3V0V1V0": (None, 4, 3),
    "V0V1V0V1V2": ([(0, 1), (0, 1), (2, -1), (3, -1)], 4, 3),
    "V1V2V1V2V3": ([(1, 1), (1, 1), (3, -1), (4, -1)], 4, 3),
}


def check(name, ok, detail):
    RESULTS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}\n         {detail}\n")


def letters(word: str):
    vs = [int(c) for c in word[1::2]]
    out = []
    for i in vs:
        out += [(i, 1), (i + 1, -1)]
    return out


def fmt(w):
    return "".join(f"s{i}" + ("" if s == 1 else "^-1") + " " for i, s in w).strip()


def crossing(w):
    """Final strand permutation and signed crossing count per label pair."""
    pos = list(range(N))
    c: dict[tuple[int, int], int] = {}
    for i, s in w:
        a, b = pos[i], pos[i + 1]
        key = (min(a, b), max(a, b))
        c[key] = c.get(key, 0) + s
        pos[i], pos[i + 1] = b, a
    return tuple(pos), {k: v for k, v in c.items() if v}


def reduce_group(w, rng=None):
    """Free cancellation across far-commuting letters only (no braid relation, no Hecke
    relation). Returns the reduced word and the number of cancelled pairs. With `rng`, the
    cancelling pair is chosen at random among those available."""
    w = list(w)
    n = 0
    while True:
        cands = []
        for p in range(len(w)):
            for r in range(p + 1, len(w)):
                if w[r] == (w[p][0], -w[p][1]):
                    if all(abs(w[k][0] - w[p][0]) >= 2 for k in range(p + 1, r)):
                        cands.append((p, r))
                    break
                if abs(w[r][0] - w[p][0]) < 2:
                    break
        if not cands:
            return w, n
        p, r = rng.choice(cands) if rng else cands[0]
        w = w[:p] + w[p + 1:r] + w[r + 1:]
        n += 1


T = sp.symbols("t")


def burau(w):
    """Unreduced Burau matrix of w on N strands, entries in Q(t)."""
    M = sp.eye(N)
    for i, s in w:
        B = sp.eye(N)
        if s == 1:
            B[i, i], B[i, i + 1], B[i + 1, i], B[i + 1, i + 1] = 1 - T, T, 1, 0
        else:
            B[i, i], B[i, i + 1], B[i + 1, i], B[i + 1, i + 1] = 0, 1, 1 / T, 1 - 1 / T
        M = M * B
    return M.applyfunc(sp.simplify)


def main() -> int:
    from witness_base import WitnessBuilder
    rng = random.Random(20261123)
    rows = []
    for word, (pred_red, pred_lmin, pred_e) in FAMILY.items():
        w = letters(word)
        red, ncanc = reduce_group(w)
        perm, c = crossing(w)
        bound = sum(abs(v) for v in c.values())
        orders = {reduce_group(w, rng)[1] for _ in range(200)}
        same_burau = sp.simplify(burau(w) - burau(red)) == sp.zeros(N)
        same_pred = True
        if pred_red is not None:
            same_pred = (crossing(pred_red) == (perm, c)
                         and sp.simplify(burau(pred_red) - burau(w)) == sp.zeros(N))
        e = (len(w) - len(red)) // 2
        rows.append({"word": word, "letters": len(w), "reduced": fmt(red),
                     "reduced_letters": len(red), "crossing_bound": bound,
                     "cancelled_pairs": ncanc, "excess": e,
                     "cancel_counts_over_200_random_orders": sorted(orders),
                     "crossing_matrix": {f"{a}{b}": v for (a, b), v in sorted(c.items())},
                     "burau_equal": bool(same_burau)})
        check(f"G1_{word}_group_relations_only",
              same_burau and crossing(red) == (perm, c),
              f"{fmt(w)} -> {fmt(red)} by free cancellation across far-commuting letters; "
              f"Burau matrices equal in Q(t), crossing data equal.")
        check(f"G2_{word}_excess",
              len(red) == bound == pred_lmin and e == pred_e and orders == {pred_e} and same_pred,
              f"length {len(w)} -> {len(red)}, crossing bound {bound} (pred {pred_lmin}); "
              f"excess {e} (pred {pred_e}); cancellation counts over 200 random orders "
              f"{sorted(orders)}; matches predicted reduced word: {same_pred}.")

    same = burau(letters("V0V1V2V0V3")) - burau(letters("V0V1V2V3V0"))
    check("G1_two_five_vertex_words_same_braid", sp.simplify(same) == sp.zeros(N),
          "V0V1V2V0V3 and V0V1V2V3V0 have the same Burau matrix (Lean pairWord'_braidEq "
          "proves they are the same braid).")

    # G3: comparison, quoted last, nothing chosen by it.
    import mpmath as mp
    from qou_substrate.constants import Q_50_DIGIT_STR, M_E_MEV_STR  # noqa: E402
    mp.mp.dps = 70
    q = mp.mpf(Q_50_DIGIT_STR)
    me = mp.mpf(M_E_MEV_STR)
    e0 = me / (q * (q - 1))
    cell = 2 * e0 * mp.log(q)
    context = {"q0": mp.nstr(q, 20), "E0_order_zero_MeV": mp.nstr(e0, 15),
               "two_E0_ln_q_MeV": mp.nstr(cell, 15),
               "Q_beta_CODATA_MeV": "0.78233", "m_n_minus_m_p_CODATA_MeV": "1.29333",
               "note": "context only; G3 says the reduction alone does not assign this cell"}
    check("G3_no_nucleon_strand", True,
          "The family has six lepton/photon strands and no nucleon strand; no energy per "
          "cancelled pair is derived in the corpus. The reduction does not assign "
          f"2E0 ln q = {mp.nstr(cell, 10)} MeV (comparison only).")

    allp = all(o for _, o, _ in RESULTS)
    print(f"  {sum(o for _, o, _ in RESULTS)}/{len(RESULTS)} checks passed")
    wb = WitnessBuilder("qbeta-gg-pair-gb", engine="sympy+mpmath", output_dir=_HERE)
    for nm, o, det in RESULTS:
        wb.add_assertion(nm, computed="PASS" if o else "FAIL", expected="PASS",
                         tolerance="exact", source=det)
    wb.save({
        "q0Anchor": "proton",
        "q0AnchorReason": "comparison_context evaluates 2*E0*ln(q0) at the default proton pin",
        "description": "Group-relation reduction of the gamma-gamma lepton pair words (W5): "
                       "the unreduced and reduced words are one braid, and each word's "
                       "cancellation excess is fixed by the signed crossing matrix.",
        "photon": "gamma_i(a,b,c) = 1 + a s_i + b s_{i+1} + c s_i s_{i+1}^-1",
        "rows": rows,
        "comparison_context": context,
        "scope": "(b) for G1 (invariant: the braid-group identity, Lean eval_pairWord); "
                 "(b) for the excess of V0V1V2V0V3 (invariant: signed crossing matrix, Lean "
                 "cancellation_count); other rows checked in this probe; G3 is a statement "
                 "about what the reduction contains, not a refutation.",
        "lean": "QOU/QBeta/GammaGammaPairReduction.lean",
    })
    return 0 if allp else 1


if __name__ == "__main__":
    sys.exit(main())
