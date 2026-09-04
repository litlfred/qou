#!/usr/bin/env python3
"""Verify at q0 that D6 flavor conjugation leaves the color-tube generator invariant.

The Open-R&D compute prototype of `conj:c-from-color-flavor-swap` (D6
charge-conjugation closure): check numerically at the substrate q0 that the
flavor-conjugation involution C (u <-> ubar, d <-> dbar on each color sheet)
leaves the color-tube weighted inter-nucleon Hecke generator

    sigma^(F1, F2) = sum_{(c1,c2) in {r,g,b}^2} W_{c1c2}(F1, F2) * sigma^{eps(c1,c2,F1,F2)}

invariant: sigma^(C F1, C F2) = sigma^(F1, F2), for every nucleon pair drawn
from {p, n, pbar, nbar}.

Scope (honest). The closed form of W is open (open question 1 of
`conj:inter-nucleon-channel-color-tube`), so the probe runs the UNIFORM
projection W = 1/9 — the only W realisation available today — together with
the block's stated chirality rule eps (+1 flavor match, -1 flavor-conjugate
pair, 0 mixed). Under C both W (constant) and eps (proved conjugation-
invariant, Lean `chiralitySign_conj_invariant` in
`QOU/BraidsAndKnots/CFromColorFlavorSwap.lean`) are unchanged, so invariance
is EXPECTED; the probe is the numeric cross-check of that derivation at q0,
in an actual 2-dim Hecke representation, not an independent test of the
conjectural Bring-derived W (which does not exist yet). Exact eps/W table
invariance is also checked over all 16 nucleon pairs x 9 color pairs.

The Hecke generator is represented two ways at q0 (repo-default precision):
  * the eigenvalue model diag(q, -1/q) (the two Hecke channels), and
  * a non-diagonal 2-dim seminormal-style matrix conjugate of it,
so the matrix identity is not an artifact of diagonality.

No fit, parameter-free. Long-compute logging not required (runtime << 5 min).

Run:  python3 -u verify_c_color_swap.py
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import _path_bridge as _bridge  # noqa: E402, F401
from q_parameter import Q_50_DIGIT_STR  # noqa: E402  (canonical substrate q0, 50 digits)
from witness_base import WitnessBuilder  # noqa: E402

import mpmath as mp  # noqa: E402

# Raise the compute precision before any mpmath value is built. Without this
# the file computes at mpmath's default 15 dps -- ~17 digits, i.e. float64 --
# while presenting mpf values. NO FLOAT64 EVER; drained under bean `qou-j6gb`,
# whose audit says to fix it AT THE SOURCE with the idempotent call rather
# than baselining the file to silence the gate.
from _precision import set_compute_dps  # noqa: E402
set_compute_dps()
# Precision is centralized: importing witness_base/qou_substrate applies the
# repo-default compute/serialization dps (recorded in the witness
# precisionMetadata) — do not override mp.mp.dps here.

COLOR_SHEETS = ("r", "g", "b")
COLOR_PAIRS = [(c1, c2) for c1 in COLOR_SHEETS for c2 in COLOR_SHEETS]

# Flavor content on the (r, g, b) sheets; "u~" / "d~" denote conjugates.
NUCLEONS = {
    "p": ("u", "u", "d"),
    "n": ("u", "d", "d"),
    "pbar": ("u~", "u~", "d~"),
    "nbar": ("u~", "d~", "d~"),
}

CONJ = {"u": "u~", "u~": "u", "d": "d~", "d~": "d"}


def conj_content(content):
    """The C-action on a nucleon's color-sheet flavor triple."""
    return tuple(CONJ[f] for f in content)


def flavor_at(content, sheet):
    return content[COLOR_SHEETS.index(sheet)]


def chirality_sign(c1, c2, F1, F2):
    """The block's stated eps rule: +1 match / -1 conjugate pair / 0 mixed."""
    f1, f2 = flavor_at(F1, c1), flavor_at(F2, c2)
    if f1 == f2:
        return 1
    if f1 == CONJ[f2]:
        return -1
    return 0


def uniform_weight(_c1, _c2, _F1, _F2):
    """The uniform-flavor projection W = 1/9 (the only realisation of W today)."""
    return mp.mpf(1) / 9


def sigma_matrices(q):
    """Two 2-dim realisations of the Hecke generator sigma at q.

    (1) diag(q, -1/q): the two Hecke channels (eigenvalue model);
    (2) a non-diagonal conjugate P diag(q, -1/q) P^-1 with a fixed generic P,
        so matrix cancellations cannot hide behind diagonality.
    Both satisfy (sigma - q)(sigma + 1/q) = 0.
    """
    d = mp.matrix([[q, 0], [0, -1 / q]])
    P = mp.matrix([[1, 1], [mp.mpf(1) / 3, 2]])  # generic invertible
    Pinv = P**-1
    return {"diag": d, "conjugated": P * d * Pinv}


def weighted_generator(sigma, sigma_inv, ident, F1, F2, weight_fn):
    """sigma^(F1,F2) = sum over the 9 color pairs of W * sigma^eps."""
    acc = mp.matrix(2, 2)
    for (c1, c2) in COLOR_PAIRS:
        w = weight_fn(c1, c2, F1, F2)
        e = chirality_sign(c1, c2, F1, F2)
        m = sigma if e == 1 else (sigma_inv if e == -1 else ident)
        acc += w * m
    return acc


def max_abs_diff(A, B):
    return max(abs(A[i, j] - B[i, j]) for i in range(2) for j in range(2))


def run():
    q = mp.mpf(Q_50_DIGIT_STR)
    reps = sigma_matrices(q)
    ident = mp.matrix([[1, 0], [0, 1]])

    # --- exact table check: eps and W invariant under C, all 16 pairs x 9 sheets
    eps_mismatches = 0
    w_mismatches = 0
    for n1, F1 in NUCLEONS.items():
        for n2, F2 in NUCLEONS.items():
            for (c1, c2) in COLOR_PAIRS:
                if chirality_sign(c1, c2, conj_content(F1), conj_content(F2)) != \
                        chirality_sign(c1, c2, F1, F2):
                    eps_mismatches += 1
                if uniform_weight(c1, c2, conj_content(F1), conj_content(F2)) != \
                        uniform_weight(c1, c2, F1, F2):
                    w_mismatches += 1

    # --- numeric generator check at q0, both representations
    results = {}
    worst = mp.mpf(0)
    for rep_name, sigma in reps.items():
        sigma_inv = sigma**-1
        rep_worst = mp.mpf(0)
        for n1, F1 in NUCLEONS.items():
            for n2, F2 in NUCLEONS.items():
                g = weighted_generator(sigma, sigma_inv, ident, F1, F2, uniform_weight)
                g_conj = weighted_generator(sigma, sigma_inv, ident,
                                            conj_content(F1), conj_content(F2),
                                            uniform_weight)
                d = max_abs_diff(g, g_conj)
                rep_worst = max(rep_worst, d)
        results[rep_name] = rep_worst
        worst = max(worst, rep_worst)

    # sanity: the involution really is an involution on the content table
    invol_ok = all(conj_content(conj_content(F)) == F for F in NUCLEONS.values())

    return {
        "q0": mp.nstr(q, 50),
        "eps_mismatches": eps_mismatches,
        "w_mismatches": w_mismatches,
        "pairs_checked": len(NUCLEONS) ** 2,
        "max_abs_generator_diff_by_rep": {k: mp.nstr(v, 5) for k, v in results.items()},
        "max_abs_generator_diff": worst,
        "involution_ok": invol_ok,
    }


def report(res):
    print("# verify_c_color_swap — D6 flavor conjugation vs the color-tube generator (q0)\n")
    print(f"q0 = {res['q0']}\n")
    print(f"nucleon pairs checked: {res['pairs_checked']} (p, n, pbar, nbar squared), "
          f"9 color pairs each")
    print(f"eps table C-mismatches: {res['eps_mismatches']} (expect 0)")
    print(f"W table C-mismatches:   {res['w_mismatches']} (expect 0)")
    print(f"C is an involution on the content table: {res['involution_ok']}")
    print("max |sigma^(CF1,CF2) - sigma^(F1,F2)| elementwise, per representation:")
    for k, v in res["max_abs_generator_diff_by_rep"].items():
        print(f"  {k:>10}: {v}")
    print("\nScope: uniform-projection W = 1/9 + the block's eps rule — the numeric"
          " cross-check of the Lean derivation (chiralitySign_conj_invariant +"
          " weight constancy), NOT a test of the conjectural Bring-derived W"
          " (closed form open).")


def main(argv=None):
    # start_time captured before the compute, so the witness durationMs
    # measures the probe runtime rather than just witness serialization.
    t0 = time.monotonic()
    res = run()
    report(res)

    w = WitnessBuilder("verify-c-color-swap", engine="python", start_time=t0)
    w.set_description(
        "Open-R&D prototype of conj:c-from-color-flavor-swap (D6): verifies at the 50-digit "
        "substrate q0 that the flavor-conjugation involution C (u<->ubar, d<->dbar per color sheet) "
        "leaves the color-tube weighted inter-nucleon Hecke generator sigma^(F1,F2) = "
        "sum W_{c1c2} sigma^{eps(c1,c2,F1,F2)} invariant, for all 16 nucleon pairs from "
        "{p,n,pbar,nbar} in two 2-dim Hecke representations (diagonal eigenvalue model and a "
        "non-diagonal conjugate). Runs the UNIFORM projection W=1/9 (the only W realisation today; "
        "the Bring-derived closed form is open — open question 1 of "
        "conj:inter-nucleon-channel-color-tube) with the block's stated eps rule, so this is the "
        "numeric cross-check of the Lean derivation (CFromColorFlavorSwap.lean: "
        "chiralitySign_conj_invariant + signedWeightSum_conj_invariant), not an independent test "
        "of the conjectural W. Exact eps/W table invariance also checked (144 cells each). "
        "No fit, parameter-free."
    )
    w.add_data("q0", res["q0"])
    w.add_data("pairs_checked", res["pairs_checked"])
    w.add_data("eps_mismatches", res["eps_mismatches"])
    w.add_data("w_mismatches", res["w_mismatches"])
    w.add_data("involution_ok", res["involution_ok"])
    w.add_data("max_abs_generator_diff_by_rep", res["max_abs_generator_diff_by_rep"])
    w.add_assertion(
        "c_swap_leaves_generator_invariant",
        computed=float(res["max_abs_generator_diff"]),
        expected=0.0, tolerance=1e-45,
        source="For every nucleon pair (F1,F2) in {p,n,pbar,nbar}^2 and both 2-dim Hecke "
               "representations at q0, the color-tube weighted generator with uniform W and the "
               "stated eps rule satisfies sigma^(CF1,CF2) = sigma^(F1,F2) to < 1e-45 elementwise "
               "(repo-default precision; see precisionMetadata). Matches the Lean derivation: eps is C-invariant "
               "(chiralitySign_conj_invariant, sorry-free) and the uniform W is constant; the "
               "conjectural class field weight_conj_invariant asserts the same for the open "
               "Bring-derived W.",
    )
    w.add_assertion(
        "eps_and_w_tables_c_invariant",
        computed=float(res["eps_mismatches"] + res["w_mismatches"]),
        expected=0.0, tolerance=0.0,
        source="Exact check over all 16 nucleon pairs x 9 color pairs (144 cells per table): "
               "eps(c1,c2,CF1,CF2) == eps(c1,c2,F1,F2) and W(c1,c2,CF1,CF2) == W(c1,c2,F1,F2).",
    )
    out = w.save()
    print(f"\nwitness -> {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
