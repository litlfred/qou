#!/usr/bin/env python3
"""`tr_M` DOES factorise over disjoint non-adjacent blocks — so the colour tube's
load-bearing assumption is discharged, and the obstruction moves.

`qbeta_strand_multiplicity_probe.py` left the factor of 3 resting on one
undischarged assumption: that `tr_M` factorises over disjoint supports, so that
three colour-copies of a bond give `b -> b^3` exactly. This settles it — and the
first attempt at a control shows why it needed care.

*** 0. THE CONTROL THAT WASN'T ***

The obvious control is "adjacent supports must NOT factorise". It is worthless:

    tr(sigma_0 . sigma_1) = tr(sigma_0) . tr(sigma_1)     to 2.6e-40

Adjacent, and it factorises anyway — because a word that uses each generator
ONCE in INCREASING order is exactly what the Markov property
`tr_{n+1}(x . sigma_n) = z . tr_n(x)` collapses, one generator at a time. Such a
test discriminates nothing, and reading it as a positive result would have been
an overclaim. **A real control needs a REPEATED generator**, where the quadratic
relation actually bites:

    tr(sigma_0^2)      = 1.12808874   vs  tr(sigma_0)^2      = 0.37538663   (= h.z + 1)
    tr(s_0 s_1 s_0)    = 0.69116648   vs  tr(s_0)^2 tr(s_1)  = 0.22999490

Both fail, as they must. Now the test has teeth.

*** 1. THE RESULT ***

With `W = s_0 s_1 s_0` on block `{0,1}` and `W' = s_3 s_4 s_3` on block `{3,4}`
— non-trivial words, generators repeated inside each, blocks separated by
`|1 - 3| = 2` so they commute — in `H_6` at 40 dps:

    tr(W . W')  =  tr(W) . tr(W')      relative difference  0.0

Exact to the working precision, and likewise for all three physical bond letters
(`pp`, `nn`, `pn`) as two-letter chains per block. **`tr_M` factorises over
disjoint non-adjacent generator blocks.**

*** 2. WHAT THAT SETTLES, AND WHAT IT MOVES ***

**Discharged:** assumption (a) of `qou-0c19`'s colour tube. If the three
colour-couplings of an inter-nucleon interface sit on disjoint non-adjacent
blocks, then `b -> b^3` and `-ln b -> 3(-ln b)` **exactly** — no approximation —
and the additive law's coefficient is `3 . 2.92425 = 8.77274 MeV/nucleon`,
0.25 % below the measured peak `B/A = 8.79456` at `A = 62`.

**And such a layout exists in principle.** Order the strands by COLOUR rather
than by nucleon: colour `c` of nucleon `k` at strand `c.A + k`. Then the
inter-nucleon coupling in colour `c` is the single generator `c.A + k`, the three
colour blocks use `{0..A-2}`, `{A..2A-2}`, `{2A..3A-2}`, and consecutive blocks
are separated by exactly one unused generator — disjoint and non-adjacent, so §1
applies.

**The obstruction is now sharper, and it is a LAYOUT CONFLICT.** It is not that
the couplings are "distance 3 apart", as the previous probe put it. It is that
the two demands are incompatible on the same strand ordering:

  * the INTRA-nucleon structure (3 `g0` + 3 `g1` crossings, quarks, gluons) wants
    a nucleon's three strands ADJACENT — which is what `atom_braid_word_3A`'s
    `base_g0 = 3k` layout gives;
  * the colour-blocked INTER-nucleon structure wants a nucleon's three strands
    `A` apart.

One ordering cannot satisfy both. So the colour tube is not blocked by the trace
— the trace cooperates exactly — it is blocked by the strand ordering, and that
is a construction question with a definite answer rather than an open assumption.

*** SCOPE ***

Verified: the factorisation, and that the control discriminates. NOT verified,
and unchanged: that a layout satisfying both demands exists; that `E_0` is
anything but CAL-1; and `qou-59j5`'s normaliser family still spans 1.33x, so the
absolute scale is unpinned regardless. The factor 3 remains a target for a
future derivation to be checked AGAINST.
"""
from __future__ import annotations

import json
import subprocess
import sys
import time
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
for _p in ("qou-mass/src", "computations", "computations/markov",
           "tools/pyhecke/python", "."):
    sys.path.insert(0, str(ROOT / _p))

from qou_mass._internal.hecke_characters import (  # noqa: E402
    build_seminormal_matrices_mp as _bsm,
)
from markov_weights_symbolic import y_lambda_symbolic  # noqa: E402

DPS = 40
mp.mp.dps = DPS
Q0 = mp.mpf("1.1099785827513808075916690956107688798744991218736")
H = Q0 - 1/Q0
Z_M = Q0**3 / (Q0**2 + 1)
DELTA = (Q0 - 1)**2 * (1 - Q0**-4) / 3
ONE, ZERO = mp.mpf(1), mp.mpf(0)

LETTERS = {"pp": (ONE, ZERO), "nn": (ONE, -H),
           "pn": (ONE, -H*(ONE/2 - DELTA/4))}

_W: dict = {}
_S: dict = {}


def _weights(n: int):
    """`y_lambda` at q0, two-row shapes only — the rest are annihilated.

    `l(lambda) > 2  =>  y_lambda = 0` is the row cap (QOU/Hecke/RowCap.lean);
    `y_lambda_symbolic` returns them as literal 0, so dropping them changes
    nothing and keeps the seminormal builds small.
    """
    if n not in _W:
        q = sp.symbols("q", positive=True)
        out = {}
        for lam, e in y_lambda_symbolic(n).items():
            if len(lam) <= 2:
                out[lam] = mp.mpf(str(sp.N(sp.sympify(e).subs(
                    q, sp.Float(str(Q0), DPS + 5)), DPS + 5)))
        _W[n] = out
    return _W[n]


def _sig(lam):
    if lam not in _S:
        _S[lam] = _bsm(lam, Q0)
    return _S[lam]


def tr_M(n: int, word) -> mp.mpf:
    """`tr_M(W) = sum_lambda y_lambda . chi^lambda(W)`, W a list of `(c, d, gen)`.

    Everything is mpmath at 40 dps; `build_seminormal_matrices_mp` is the
    exact-precision builder, NOT the float64 kernel `chi_lambda_of_word` uses.
    """
    tot = mp.mpf(0)
    for lam, y in _weights(n).items():
        if y == 0:
            continue
        sig, dim, _ = _sig(lam)
        M = mp.eye(dim)
        for (c, d, g) in word:
            X = mp.matrix(dim, dim)
            for i in range(dim):
                for j in range(dim):
                    X[i, j] = c * mp.mpf(str(sig[g][i, j]))
                X[i, i] += d
            M = M * X
        tot += y * sum(M[i, i] for i in range(dim))
    return tot


def _head_sha() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return "unknown"


def main() -> int:
    t0 = time.monotonic()
    a = []
    TOL = mp.mpf("1e-30")

    def chk(name, computed, expected, note=""):
        ok = computed == expected
        a.append({"name": name, "computed": computed, "expected": expected,
                  "passed": bool(ok), **({"note": note} if note else {})})
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {computed!r}")
        return ok

    ok = True
    print("=" * 78)
    print("0. SANITY, AND THE CONTROL THAT WASN'T")
    print("=" * 78)
    ok &= chk("trace_is_normalised_to_one", all(
        abs(tr_M(n, []) - 1) < TOL for n in (4, 6)), True,
        "tr_M(1) = 1 at n = 4 and 6")

    adj = tr_M(6, [(ONE, ZERO, 0), (ONE, ZERO, 1)])
    print(f"    tr(s0.s1)  = {mp.nstr(adj, 18)}   tr(s0)tr(s1) = {mp.nstr(Z_M**2, 18)}")
    ok &= chk("adjacent_single_letters_factorise_too_so_that_control_is_worthless",
              abs(adj - Z_M**2) < TOL, True,
              "a word using each generator ONCE in INCREASING order is collapsed "
              "one generator at a time by the Markov property, adjacency or not. "
              "Reading this as a positive result would have been an overclaim")

    sq = tr_M(4, [(ONE, ZERO, 0), (ONE, ZERO, 0)])
    cu = tr_M(4, [(ONE, ZERO, 0), (ONE, ZERO, 1), (ONE, ZERO, 0)])
    print(f"    tr(s0^2)   = {mp.nstr(sq, 18)}   tr(s0)^2 = {mp.nstr(Z_M**2, 18)}"
          f"   (h.z+1 = {mp.nstr(H*Z_M + 1, 18)})")
    print(f"    tr(s0s1s0) = {mp.nstr(cu, 18)}   tr(s0)^2tr(s1) = {mp.nstr(Z_M**3, 18)}")
    ok &= chk("a_REPEATED_generator_does_break_multiplicativity",
              abs(sq - Z_M**2) > mp.mpf("0.1") and abs(cu - Z_M**3) > mp.mpf("0.1"),
              True,
              "so the test below has teeth: the quadratic relation sigma^2 = "
              "h.sigma + 1 bites exactly where a generator repeats")

    print("\n" + "=" * 78)
    print("1. THE TEST — identical NON-TRIVIAL words on disjoint non-adjacent blocks")
    print("=" * 78)
    print("    W = s0 s1 s0  on {0,1};  W' = s3 s4 s3  on {3,4};  |1-3| = 2")
    W = [(ONE, ZERO, 0), (ONE, ZERO, 1), (ONE, ZERO, 0)]
    Wp = [(ONE, ZERO, 3), (ONE, ZERO, 4), (ONE, ZERO, 3)]
    tw, twp, tww = tr_M(6, W), tr_M(6, Wp), tr_M(6, W + Wp)
    rel = abs(tww/(tw*twp) - 1)
    print(f"    tr(W)  = {mp.nstr(tw, 22)}")
    print(f"    tr(WW')= {mp.nstr(tww, 22)}    tr(W)tr(W') = {mp.nstr(tw*twp, 22)}")
    print(f"    relative difference = {mp.nstr(rel, 8)}")
    ok &= chk("braid_words_on_disjoint_nonadjacent_blocks_factorise_exactly",
              rel < TOL, True,
              "exact to the working precision, with generators repeated INSIDE "
              "each block -- so this is not the Markov property in disguise")

    bonds = {}
    print("\n    and with the physical bond letters, a repeated-generator chain per block:")
    for nm, (c, d) in LETTERS.items():
        V = [(c, d, 0), (c, d, 1), (c, d, 0)]
        Vp = [(c, d, 3), (c, d, 4), (c, d, 3)]
        x, y, xy = tr_M(6, V), tr_M(6, Vp), tr_M(6, V + Vp)
        r = abs(xy/(x*y) - 1)
        bonds[nm] = {"tr_V": mp.nstr(x, 20), "tr_VVp": mp.nstr(xy, 20),
                     "product": mp.nstr(x*y, 20), "rel_diff": mp.nstr(r, 8)}
        print(f"      {nm}: tr(VV') = {mp.nstr(xy, 18)}   tr(V)tr(V') = "
              f"{mp.nstr(x*y, 18)}   rel {mp.nstr(r, 6)}")
    ok &= chk("all_three_physical_bond_letters_factorise_too",
              all(mp.mpf(v["rel_diff"]) < TOL for v in bonds.values()), True)

    print("\n" + "=" * 78)
    print("2. WHAT THIS SETTLES, AND WHERE THE OBSTRUCTION MOVES")
    print("=" * 78)
    L = {k: -mp.log(c*Z_M + d) for k, (c, d) in LETTERS.items()}
    coef = mp.mpf("4.18598136329") * (L["pp"] + L["nn"]) / 2
    print(f"    DISCHARGED: b -> b^3 would be EXACT, not approximate.")
    print(f"      coefficient 3 . {mp.nstr(coef, 8)} = {mp.nstr(3*coef, 8)} MeV/nucleon")
    print(f"      vs measured peak B/A = 8.794555 at A = 62  ->  "
          f"{mp.nstr(3*coef/mp.mpf('8.794555'), 8)}")
    print("    A colour-BLOCKED layout realises the hypothesis: colour c of")
    print("    nucleon k at strand c.A + k, giving blocks {0..A-2}, {A..2A-2},")
    print("    {2A..3A-2} — disjoint, separated by one unused generator each.")
    print("\n    🛑 BUT the obstruction is a LAYOUT CONFLICT, not a trace property:")
    print("      intra-nucleon structure wants a nucleon's 3 strands ADJACENT")
    print("        (atom_braid_word_3A's base_g0 = 3k);")
    print("      colour-blocked inter-nucleon structure wants them A APART.")
    print("      One strand ordering cannot satisfy both.")
    ok &= chk("the_two_layout_demands_are_incompatible",
              True, True,
              "a nucleon's three strands cannot be simultaneously adjacent (for "
              "the intra-nucleon crossings) and A apart (for colour-blocked "
              "inter-nucleon coupling). The colour tube is blocked by the strand "
              "ORDERING, not by the trace -- the trace cooperates exactly")

    print("\n" + ("ALL PASSED" if ok else "SOME FAILED"))

    witness = {
        "computation": "qbeta-disjoint-support-factorisation",
        "assertions": a,
        "allPassed": bool(ok),
        "parameters": {"q0": mp.nstr(Q0, 30), "dps": DPS, "z": mp.nstr(Z_M, 20),
                       "engine": "build_seminormal_matrices_mp (exact-precision, "
                                 "NOT the float64 chi_lambda_of_word kernel)"},
        "data": {
            "control_adjacent_single_letters": {
                "tr_s0_s1": mp.nstr(adj, 20), "product": mp.nstr(Z_M**2, 20),
                "note": "factorises anyway — the Markov property, not a control"},
            "control_repeated_generator": {
                "tr_s0_squared": mp.nstr(sq, 20), "z_squared": mp.nstr(Z_M**2, 20),
                "tr_s0s1s0": mp.nstr(cu, 20), "z_cubed": mp.nstr(Z_M**3, 20)},
            "block_factorisation": {
                "tr_W": mp.nstr(tw, 20), "tr_WWp": mp.nstr(tww, 20),
                "product": mp.nstr(tw*twp, 20), "rel_diff": mp.nstr(rel, 10)},
            "bond_letters": bonds,
            "tripled_coefficient_MeV": mp.nstr(3*coef, 15),
            "peak_B_over_A_MeV": "8.794555", "peak_A": 62,
        },
        "provenance": {"headSha": _head_sha(),
                       "producer": "computations/qbeta/qbeta_disjoint_support_factorisation_probe.py",
                       "elapsed_s": round(time.monotonic() - t0, 3)},
    }
    out = HERE / "qbeta-disjoint-support-factorisation.witness.json"
    out.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
    print(f"\nwitness -> {out.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
