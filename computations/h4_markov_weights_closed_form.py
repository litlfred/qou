#!/usr/bin/env python3
"""Exact closed-form Jones–Markov weights ``w_λ`` for ``tr_M`` on the H₄(q)
subscript normal-form basis  (bean qou-x64l, step 4).

Why this exists
---------------
``QOU.Machinery.H4.trM4_cyclic`` is proved in Lean, but its *proof* transports
along the basis bridge into ``QOU.Machinery.H4.trM_cyclic``, which is the ASCII
Gram closure — eight chained modules, ~4.3 GB peak, and the reason a full
``lake build`` takes ~55 min instead of ~5. Retiring that chain needs an
independent proof of cyclicity on the subscript basis, and the route already
identified in the corpus is
``QOU.Machinery.BilinearTrace.gram_symm_of_rep_decomp``: if ``tr_M`` decomposes
as a finite weighted sum of representation traces, each multiplicative on
``mulNF₄``, Gram symmetry follows with *no* per-pair computation.
``HeckeH4Wedderburn.wedderburn₄`` supplies the five representations. The stated
open item was: *"what remains is identifying the Markov weights."*

This script identifies them, in closed form, and verifies them.

What is computed
----------------
1. The three generator actions and the 24 trace weights are transcribed from
   ``QOU/Machinery/HeckeH4StabilizationRung.lean`` (single source of truth), and
   the Hecke presentation is re-derived from them as a transcription check.
2. The centre of the algebra is computed as the nullspace of the commutator
   system; a generic central element is diagonalised, giving the five central
   primitive idempotents ``z_λ`` and hence the block dimensions ``1,1,2,3,3``.
3. The characters are read off as ``χ_λ(x) = tr(R_x · P_λ) / d_λ`` and the
   weights as ``w_λ = tr_M(z_λ) / d_λ``.
4. The closed forms below are checked against those, and the **decomposition
   itself** — ``tr_M(b_i) = Σ_λ w_λ χ_λ(b_i)`` — is checked on all 24 basis
   elements, at five independent rational ``q``.

The closed forms
----------------
With ``A = q²+1``, ``B = q⁴+q²+1``, ``C = q⁴+1`` (exactly the Wenzl genericity
factors ``h2``, ``h3``, ``h4`` that ``wedderburn₄`` already requires — the
weights are singular precisely off its locus, which is the consistency check
that they belong to that decomposition):

    w_(4)       =  (qz+1)(qAz+1)(qBz+1)        / (A²·B·C)          d = 1
    w_(3,1)     = -q (z-q)(qz+1)(qAz+1)        / (A²·C)            d = 3
    w_(2,2)     = -q³(z-q)(qz+1)               / (A²·B)            d = 2
    w_(2,1,1)   =  q²(z-q)(qz+1)(Az-q³)        / (A²·C)            d = 3
    w_(1,1,1,1) = -q³(z-q)(Az-q³)(Bz-q⁵)       / (A²·B·C)          d = 1

Every weight carries ``(z-q)`` except the trivial one and ``(qz+1)`` except the
sign one — ``q`` and ``-q⁻¹`` being the two Hecke eigenvalues.

Independent confirmation
------------------------
``computations/alpha-k-jones-markov-h4.witness.json`` carries the same five
weights as *floats*, at the substrate anchor, obtained by a different method (a
numerical constraint system, ``status: exploratory``). The closed forms above
reproduce all five to ~16 significant figures. That cross-check also fixes the
partition labelling, which the spectral computation alone does not determine.

Arithmetic
----------
Exact throughout: sympy ``Rational`` and symbolic ``z``. No float64 enters the
derivation; the only floats are the published comparison values being checked
against, and the residuals are reported as exact-vs-float differences.
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

from sympy import Matrix, Rational, cancel, expand, factor, simplify, symbols, sympify
from sympy import N as NUM

h, z, q = symbols("h z q")
N = 24

# --------------------------------------------------------------------------
# Transcribed from QOU/Machinery/HeckeH4StabilizationRung.lean.
# Each row lists (coefficient in h, source index), matching the Lean `![...]`.
# --------------------------------------------------------------------------

MUL0 = [
    [(1, 1)], [(1, 0), (h, 1)], [(1, 3)], [(1, 2), (h, 3)],
    [(1, 5)], [(1, 4), (h, 5)], [(1, 8)], [(1, 11)],
    [(1, 6), (h, 8)], [(1, 14)], [(1, 15)], [(1, 7), (h, 11)],
    [(1, 18)], [(1, 19)], [(1, 9), (h, 14)], [(1, 10), (h, 15)],
    [(1, 21)], [(1, 22)], [(1, 12), (h, 18)], [(1, 13), (h, 19)],
    [(1, 23)], [(1, 16), (h, 21)], [(1, 17), (h, 22)], [(1, 20), (h, 23)],
]
MUL1 = [
    [(1, 2)], [(1, 4)], [(1, 0), (h, 2)], [(1, 5)],
    [(1, 1), (h, 4)], [(1, 3), (h, 5)], [(1, 9)], [(1, 12)],
    [(1, 13)], [(1, 6), (h, 9)], [(1, 16)], [(1, 17)],
    [(1, 7), (h, 12)], [(1, 8), (h, 13)], [(1, 19)], [(1, 20)],
    [(1, 10), (h, 16)], [(1, 11), (h, 17)], [(1, 22)], [(1, 14), (h, 19)],
    [(1, 15), (h, 20)], [(1, 23)], [(1, 18), (h, 22)], [(1, 21), (h, 23)],
]
MUL2 = [
    [(1, 6)], [(1, 8)], [(1, 7)], [(1, 11)],
    [(1, 10)], [(1, 15)], [(1, 0), (h, 6)], [(1, 2), (h, 7)],
    [(1, 1), (h, 8)], [(1, 12)], [(1, 4), (h, 10)], [(1, 3), (h, 11)],
    [(1, 9), (h, 12)], [(1, 16)], [(1, 18)], [(1, 5), (h, 15)],
    [(1, 13), (h, 16)], [(1, 20)], [(1, 14), (h, 18)], [(1, 21)],
    [(1, 17), (h, 20)], [(1, 19), (h, 21)], [(1, 23)], [(1, 22), (h, 23)],
]

TRM4 = [
    1, z, z, z**2,
    z**2, h * z**2 + z, z, z**2,
    z**2, z**2, z**3, z**3,
    h * z**2 + z, z**3, z**3, h * z**3 + z**2,
    h * z**3 + z**2, h * z**3 + z**2, h * z**3 + z**2, h * z**3 + z**2,
    h**2 * z**3 + h * z**2 + z**3, h**2 * z**3 + 2 * h * z**2 + z,
    h**2 * z**3 + h * z**2 + z**3,
    h**3 * z**3 + h**2 * z**2 + 2 * h * z**3 + z**2,
]

# Reduced word for each basis index, recovered by BFS from e_0 (see `_bfs`).
WORDS = {
    0: (), 1: (0,), 2: (1,), 3: (1, 0), 4: (0, 1), 5: (0, 1, 0),
    6: (2,), 7: (1, 2), 8: (0, 2), 9: (2, 1), 10: (0, 1, 2), 11: (1, 0, 2),
    12: (1, 2, 1), 13: (0, 2, 1), 14: (2, 1, 0), 15: (0, 1, 0, 2),
    16: (0, 1, 2, 1), 17: (1, 0, 2, 1), 18: (1, 2, 1, 0), 19: (0, 2, 1, 0),
    20: (0, 1, 0, 2, 1), 21: (0, 1, 2, 1, 0), 22: (1, 0, 2, 1, 0),
    23: (0, 1, 0, 2, 1, 0),
}

# Published floats to cross-check against, from
# computations/alpha-k-jones-markov-h4.witness.json (status: exploratory).
#
# The anchor those floats were computed at is read from that witness at run
# time and is deliberately NOT copied here. It is a muon-era value that is
# stale against both documented pins, and embedding it would put a stale q0
# literal into this witness — which is the recurring defect the q0-drift gate
# exists to catch (AGENTS.md, "q0 anchor convention"). It is an input being
# quoted, not an anchor this computation adopts.
#
# This computation has no anchor of its own: the weights are exact rational
# functions of symbolic q, so they hold at every q on the genericity locus.
# Where a number is wanted, the canonical pin is the experimental (proton) one
# per the 2026-08-07 owner directive, and it is taken live from
# qou_substrate.constants rather than transcribed.
XCHECK_SOURCE = "alpha-k-jones-markov-h4.witness.json"
XCHECK_Z = "0.49932033403359827"

# Tolerance the cross-check is ASSERTED against, not merely reported at.
#
# Until 2026-08-24 `worst` was computed, printed and written into the witness
# and then never checked: the exit code keyed on `all_ok`, the symbolic
# q-verification, alone.  That made this control arm silent in exactly the
# direction it exists to catch.  `XCHECK_Z` is transcribed, so a CONVENTION
# change breaks loudly; the anchor is read from the artifact at run time
# (deliberately -- see the note above), so a RE-PIN of that artifact moved the
# comparison without failing anything.  The residual simply grew in a field
# nobody reads.
#
# 1e-12 is set from the measured floor with headroom, not fitted: the
# published values are float64, so the relative floor is ~1e-16, amplified to
# 2.10e-14 on `(1,1,1,1)` because that weight (-0.00084) sits near a
# cancellation.  The failure this must catch is four or more orders larger --
# the muon/proton pins differ by 11.5 ppb, so a re-pin moves these weights by
# ~1e-8 at worst.  Anything between 2.1e-14 and 1e-8 would do; 1e-12 leaves
# two orders above the observed floor and four below the smallest real defect.
XCHECK_MAX_REL = 1e-12
XCHECK_WEIGHTS = {
    "(4,)": "0.22752693019306408",
    "(3,1)": "0.18786885614150228",
    "(2,2)": "0.06947330464150198",
    "(2,1,1)": "0.02358747319685989",
    "(1,1,1,1)": "-0.0008425274911545449",
}
DIMS = {"(4,)": 1, "(3,1)": 3, "(2,2)": 2, "(2,1,1)": 3, "(1,1,1,1)": 1}


def _amat(mul):
    a = [[0] * N for _ in range(N)]
    for i, row in enumerate(mul):
        for (c, j) in row:
            a[i][j] += c
    return Matrix(a)


GENS = {0: _amat(MUL0), 1: _amat(MUL1), 2: _amat(MUL2)}


def closed_forms(qv, zv):
    """The five closed-form weights, keyed by partition."""
    A = qv**2 + 1
    B = qv**4 + qv**2 + 1
    C = qv**4 + 1
    zq = zv - qv          # vanishes on the trivial rep's eigenvalue
    qz = qv * zv + 1      # vanishes on the sign rep's eigenvalue
    return {
        "(4,)":       qz * (qv * A * zv + 1) * (qv * B * zv + 1) / (A**2 * B * C),
        "(3,1)":     -qv * zq * qz * (qv * A * zv + 1) / (A**2 * C),
        "(2,2)":     -qv**3 * zq * qz / (A**2 * B),
        "(2,1,1)":    qv**2 * zq * qz * (A * zv - qv**3) / (A**2 * C),
        "(1,1,1,1)": -qv**3 * zq * (A * zv - qv**3) * (B * zv - qv**5) / (A**2 * B * C),
    }


def check_presentation():
    """Re-derive the Hecke presentation from the transcribed actions."""
    I = Matrix.eye(N)
    Z = Matrix.zeros(N, N)
    out = {}
    for name, A in [("sigma0", GENS[0]), ("sigma1", GENS[1]), ("sigma2", GENS[2])]:
        out[f"hecke_quadratic_{name}"] = simplify(expand(A * A) - expand(h * A + I)) == Z
    out["braid_s0_s1"] = simplify(expand(GENS[0] * GENS[1] * GENS[0]
                                         - GENS[1] * GENS[0] * GENS[1])) == Z
    out["braid_s1_s2"] = simplify(expand(GENS[1] * GENS[2] * GENS[1]
                                         - GENS[2] * GENS[1] * GENS[2])) == Z
    out["far_commute_s0_s2"] = simplify(expand(GENS[0] * GENS[2]
                                               - GENS[2] * GENS[0])) == Z
    return out


def spectral_data(qv):
    """Central primitive idempotents, block dims, characters and empirical
    weights, at an exact rational `qv`."""
    hv = qv - Rational(1, 1) / qv
    sub = {h: hv}
    G = {k: A.subs(sub) for k, A in GENS.items()}
    Rj = {}
    for j, w in WORDS.items():
        M = Matrix.eye(N)
        for k in w:
            M = G[k] * M
        Rj[j] = M
    TR = [sympify(t).subs(sub) for t in TRM4]

    rows = []
    for k in G:
        Cm = [G[k] * Rj[j] - Rj[j] * G[k] for j in range(N)]
        for a in range(N):
            for b in range(N):
                rows.append([Cm[j][a, b] for j in range(N)])
    ns = Matrix(rows).nullspace()
    if len(ns) != 5:
        return None, hv, len(ns)

    cgen = sum((Rational(i + 1, 7) * ns[i] for i in range(5)), Matrix.zeros(N, 1))
    Rc = sum((cgen[j] * Rj[j] for j in range(N)), Matrix.zeros(N, N))
    e0 = Matrix.zeros(N, 1)
    e0[0] = 1

    evs = Rc.eigenvects()
    blocks = []
    for (val, mult, _) in evs:
        P = Matrix.eye(N)
        for (v2, _, _) in evs:
            if v2 != val:
                P = P * (Rc - v2 * Matrix.eye(N)) * (Rational(1, 1) / (val - v2))
        d = int(math.isqrt(int(mult)))
        chi = [cancel(simplify(((Rj[i] * P).trace()) / d)) for i in range(N)]
        zc = P * e0
        w_emp = cancel(simplify(sum((zc[i] * TR[i] for i in range(N)), 0) / d))
        blocks.append({"d": d, "chi": chi, "w": w_emp})
    return blocks, hv, TR


def main():
    print("=" * 72)
    print("H4(q) subscript-basis Markov weights -- exact closed form (qou-x64l)")
    print("=" * 72)

    print("\n[1] Hecke presentation re-derived from the transcribed actions")
    pres = check_presentation()
    for k, v in pres.items():
        print(f"      {k:28s} {'OK' if v else 'FAIL'}")
    if not all(pres.values()):
        print("  transcription check FAILED"); return 1

    results = {}
    all_ok = True
    for qv in [Rational(2), Rational(3), Rational(5, 2), Rational(7, 3), Rational(4)]:
        blocks, hv, TR = spectral_data(qv)
        key = str(qv)
        if blocks is None:
            results[key] = {"generic": False, "centre_dim": TR}
            print(f"\n[2] q={qv}: centre dim {TR} != 5, non-generic -- skipped")
            continue
        cf = {k: cancel(v) for k, v in closed_forms(qv, z).items()}
        # match empirical weights to closed forms
        matched = {}
        for name, expr in cf.items():
            for blk in blocks:
                if blk["d"] == DIMS[name] and simplify(blk["w"] - expr) == 0:
                    matched[name] = blk
                    break
        n_matched = len(matched)
        # decomposition on all 24 basis elements
        bad = []
        for i in range(N):
            rhs = sum((b["w"] * b["chi"][i] for b in blocks), 0)
            if simplify(TR[i] - rhs) != 0:
                bad.append(i)
        norm_ok = all(simplify(b["chi"][0] - b["d"]) == 0 for b in blocks)
        ok = (n_matched == 5) and (not bad) and norm_ok
        all_ok = all_ok and ok
        print(f"\n[2] q={qv}  h={hv}")
        print(f"      block dims                     {sorted(b['d'] for b in blocks)}"
              f"  (sum d^2 = {sum(b['d']**2 for b in blocks)})")
        print(f"      closed forms matched           {n_matched}/5")
        print(f"      chi_lambda(1) == d_lambda      {norm_ok}")
        print(f"      tr_M(b_i) = sum w chi(b_i)     "
              f"{'HOLDS on all 24' if not bad else f'FAILS at {bad}'}")
        results[key] = {
            "generic": True,
            "h": str(hv),
            "block_dims": sorted(b["d"] for b in blocks),
            "closed_forms_matched": n_matched,
            "character_normalisation_ok": bool(norm_ok),
            "decomposition_holds_on_all_24": not bad,
            "decomposition_failures": bad,
        }

    print("\n[3] Cross-check against computations/alpha-k-jones-markov-h4.witness.json")
    src = Path(__file__).with_name(XCHECK_SOURCE)
    published_q0 = json.loads(src.read_text())["substrate"]["q_0"]
    q0 = sympify(published_q0)
    z0 = sympify(XCHECK_Z)
    cf0 = closed_forms(q0, z0)
    xres = {}
    worst = 0.0
    for name, published in XCHECK_WEIGHTS.items():
        mine = NUM(cf0[name], 25)
        diff = abs(NUM(mine - sympify(published), 25))
        rel = float(diff / abs(NUM(sympify(published), 25)))
        worst = max(worst, rel)
        xres[name] = {"closed_form": str(mine), "published_float": published,
                      "relative_difference": f"{rel:.3e}"}
        print(f"      {name:11s} closed {str(mine)[:24]:24s} "
              f"published {published:22s} rel {rel:.2e}")
    xcheck_ok = worst <= XCHECK_MAX_REL
    unit = NUM(sum(cf0[k] * DIMS[k] for k in cf0), 25)
    print(f"      sum_lambda w_lambda * d_lambda = {unit}   (must be 1 = tr_M(1))")

    # Evaluate at the canonical (proton-pinned) anchor as well, so this witness
    # states which pin any numeric value of its belongs to.
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]
                           / "tools" / "qou-substrate" / "python"))
    from qou_substrate import constants as _c  # noqa: E402
    canonical_q0 = str(_c.Q_50_DIGIT_STR)
    cfc = closed_forms(sympify(canonical_q0), z0)
    at_canonical = {k: str(NUM(v, 25)) for k, v in cfc.items()}
    print(f"\n[3b] at the canonical proton pin q_0 = {canonical_q0[:22]}...")
    for k in XCHECK_WEIGHTS:
        print(f"      {k:11s} {at_canonical[k]}")
    print(f"      sum_lambda w_lambda * d_lambda = "
          f"{NUM(sum(cfc[k] * DIMS[k] for k in cfc), 25)}")

    witness = {
        "compute": "h4_markov_weights_closed_form",
        "description": (
            "Exact closed-form Jones-Markov weights w_lambda for tr_M on the "
            "H4(q) subscript normal-form basis. Supplies the missing input to "
            "BilinearTrace.gram_symm_of_rep_decomp, which is the route to an "
            "independent proof of trM4_cyclic that does not route through the "
            "ASCII Gram chain (bean qou-x64l step 4)."
        ),
        "status": "derived",
        "bean": "qou-x64l",
        "arithmetic": "exact (sympy Rational + symbolic z); no float64 in the derivation",
        "source_of_truth": (
            "generator actions and TRM4 transcribed from "
            "content/quantum-observable-universe/lean/QOU/Machinery/"
            "HeckeH4StabilizationRung.lean"
        ),
        "presentation_check": {k: bool(v) for k, v in pres.items()},
        "closed_forms": {
            "notation": "A = q^2+1, B = q^4+q^2+1, C = q^4+1 (the wedderburn4 "
                        "genericity factors h2, h3, h4)",
            "(4,)": "(q z + 1)(q A z + 1)(q B z + 1) / (A^2 B C)",
            "(3,1)": "-q (z - q)(q z + 1)(q A z + 1) / (A^2 C)",
            "(2,2)": "-q^3 (z - q)(q z + 1) / (A^2 B)",
            "(2,1,1)": "q^2 (z - q)(q z + 1)(A z - q^3) / (A^2 C)",
            "(1,1,1,1)": "-q^3 (z - q)(A z - q^3)(B z - q^5) / (A^2 B C)",
        },
        "block_dimensions": DIMS,
        "verification_by_q": results,
        "all_q_verified": all_ok,
        "anchor": {
            "has_own_anchor": False,
            "pin": "experimental (proton), per the 2026-08-07 owner directive",
            "q_0": canonical_q0,
            "q_0_source": "qou_substrate.constants.Q_50_DIGIT_STR (read live)",
            "note": (
                "The weights are exact rational functions of symbolic q and hold "
                "at every q on the genericity locus, so this computation does not "
                "depend on an anchor. The canonical proton pin is recorded so a "
                "later reader can tell which layer any numeric evaluation belongs "
                "to without inferring it from a call site."
            ),
            "weights_at_canonical_q0": at_canonical,
        },
        "cross_check_alpha_k_jones_markov_h4": {
            "markov_z": XCHECK_Z,
            "published_q0_source": (
                f"computations/{XCHECK_SOURCE}:substrate.q_0 (read at run time, "
                "not transcribed -- it is a muon-era value stale against both "
                "documented pins, quoted here only as the input those published "
                "floats were computed at)"
            ),
            "weights": xres,
            "worst_relative_difference": f"{worst:.3e}",
            "max_relative_difference_allowed": f"{XCHECK_MAX_REL:.0e}",
            "cross_check_passed": bool(xcheck_ok),
            "sum_w_times_dim": str(unit),
            "note": (
                "The published values are floats from an independent numerical "
                "constraint system (status: exploratory). Agreement at this level "
                "confirms the closed forms and fixes the partition labelling, "
                "which the spectral computation alone does not determine."
            ),
        },
    }
    out = Path(__file__).with_name("h4-markov-weights-closed-form.witness.json")
    out.write_text(json.dumps(witness, indent=2, sort_keys=True) + "\n")
    print(f"\n[4] wrote {out.name}")
    print(f"    all q verified: {all_ok};  worst cross-check rel diff: {worst:.3e}")
    if not xcheck_ok:
        print(
            f"\n    FAIL: the cross-check residual {worst:.3e} exceeds "
            f"XCHECK_MAX_REL = {XCHECK_MAX_REL:.0e}.\n"
            f"    This control arm reproduces the published record of "
            f"{XCHECK_SOURCE} at the anchor\n"
            f"    recorded IN that artifact.  A residual this large means the "
            f"artifact no longer\n"
            f"    carries the record these transcribed weights came from -- "
            f"most likely it was\n"
            f"    re-pinned.  Do NOT widen this tolerance: re-transcribe "
            f"XCHECK_WEIGHTS from the\n"
            f"    artifact's new contents, or point XCHECK_SOURCE at the copy "
            f"that still holds\n"
            f"    the original record."
        )
    return 0 if (all_ok and xcheck_ok) else 1


if __name__ == "__main__":
    sys.exit(main())
