#!/usr/bin/env python3
"""Is the Frobenius pairing on Z(H_n(q)) anti-diagonal on curvature-rank strata?

Bean `qou-xsv8`, fix step 2 -- the open thread left by the F5 agent (`qou-09e0`).

## The claim under test

`prf:spectral-sequence-collapse` carries a paragraph titled *"Frobenius duality
of strata"*:

    The Frobenius pairing <a, b> = int_A a.b gives a self-duality A ~ A^v.
    Under this duality the GB filtration J^0 > J^1 > ... > J^N maps to its
    annihilator filtration (J^l)^perp = J^{N-l}.
    This is POINCARE DUALITY OF CURVATURE-RANK STRATA: rank-l contributions
    pair with rank-(N-l) contributions under the Frobenius integral.

and the next paragraph says the derivation "need only enumerate central
idempotents e_lambda, compute their GB-depth ... binning by depth(lambda)". So
the strata the duality is asserted of are spanned by sets of central primitive
idempotents.

`prf:quantum-dilogarithm-stratified` Step 1 makes the same move, and the F5
agent refuted it there. This probe asks whether the same defect is present here.

## Why this is a measurement and not a re-derivation

The refutation is one line of algebra -- for ANY linear functional phi,

    phi(e_lambda . e_mu) = phi(delta_{lambda,mu} e_lambda),

so the Gram in the idempotent basis is diagonal whatever phi is. Re-deriving
that would be theatre. What is worth measuring is that the corpus's OWN
idempotents, at the one `n` where it has them explicitly, produce a diagonal
Gram with nonzero diagonal -- i.e. that the strata are SELF-dual, so the
asserted cross-stratum pairing is identically zero rather than merely unproved.

## Method: no algebra multiplication is needed

The canonical symmetrizing trace of `H_n(q)` is `tau(sum_w a_w T_w) := a_e`, and
`{T_{w^-1}}` is the dual basis of `{T_w}`:

    tau(T_u T_v) = delta_{u, v^-1}                                  (*)

(the AGENTS.md section 7a convention `sigma^2 = (q - q^-1) sigma + 1`; stated in
`docs/audits/scripts/central_idempotent_unit_coefficient.py`). So for
`x = sum_u a_u T_u` and `y = sum_v b_v T_v`,

    tau(x y) = sum_u a_u . b_{u^-1}

-- a bilinear form on coefficient vectors, needing only the inversion map on
`S_3`. This computes the Gram INDEPENDENTLY of the orthogonality assertion A2 of
`probe_h3_central_idempotents_exact.py`, rather than citing it.

Self-test on (*): completeness `sum_lambda e_lambda = 1` forces
`sum_lambda tau(e_lambda) = tau(1) = 1`. A3 checks it exactly. If (*) or the
committed coefficients were wrong, A3 fails.

Inputs: the exact QQ(q) coefficients committed in
`probe-h3-central-idempotents-exact.witness.json` (n = 3, six-word basis).

Precision: sympy exact rational functions in QQ(q) throughout; the single
numerical evaluation is mpmath `mpf` at the proton pin. No float64 anywhere.

Output: centre-frobenius-pairing-is-diagonal.witness.json
"""
from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401  (puts qou_substrate on the path)

import sympy as sp  # noqa: E402
import mpmath as mp  # noqa: E402

_HERE = Path(__file__).resolve().parent
_SRC = _HERE / "probe-h3-central-idempotents-exact.witness.json"

# S_3 in the committed word order [1, s0, s1, s0s1, s1s0, s0s1s0].
# Inverses: 1,s0,s1 are involutions; (s0s1)^-1 = s1s0; s0s1s0 is the longest
# element, also an involution. So inversion is the transposition (3 4).
WORDS = ["1", "s0", "s1", "s0s1", "s1s0", "s0s1s0"]
INV = [0, 1, 2, 4, 3, 5]

LABELS = ["(3)", "(2,1)", "(1,1,1)"]


def main() -> int:
    t0 = time.monotonic()
    q = sp.symbols("q", positive=True)
    raw = json.loads(_SRC.read_text())["data"]

    coeffs = {}
    for lab in LABELS:
        key = f"pi_{lab}_coeffs_words_1_s0_s1_s0s1_s1s0_s0s1s0"
        coeffs[lab] = [sp.sympify(c, locals={"q": q}) for c in raw[key]]

    # ---- Gram of B(x, y) = tau(x y) in the idempotent basis, via (*) --------
    def tau_prod(a, b):
        return sp.cancel(sp.together(sum(a[u] * b[INV[u]] for u in range(6))))

    gram = [[tau_prod(coeffs[l1], coeffs[l2]) for l2 in LABELS] for l1 in LABELS]

    assertions = []

    def check(name, cond, detail):
        assertions.append({"name": name, "passed": bool(cond), "detail": detail})
        print(f"  [{'OK ' if cond else 'FAIL'}] {name}: {detail}")
        return bool(cond)

    print("Frobenius Gram on Z(H_3(q)) in the central-idempotent basis, exact QQ(q):")
    for i, l1 in enumerate(LABELS):
        row = "  ".join(str(sp.simplify(gram[i][j])) for j in range(3))
        print(f"  e_{l1:<8} | {row}")

    # ---- A1: off-diagonal vanishes identically -----------------------------
    off = [(LABELS[i], LABELS[j], sp.simplify(gram[i][j]))
           for i in range(3) for j in range(3) if i != j]
    ok_off = all(v == 0 for _, _, v in off)
    check("A1_offdiagonal_identically_zero", ok_off,
          f"all {len(off)} off-diagonal entries are 0 in QQ(q): "
          f"{sorted({str(v) for _, _, v in off})}")

    # ---- A2: diagonal is nonzero (each stratum is SELF-dual) ---------------
    diag = [sp.cancel(sp.simplify(gram[i][i])) for i in range(3)]
    ok_diag = all(d != 0 for d in diag)
    check("A2_diagonal_nonzero", ok_diag,
          "tau(e_lambda) != 0 for all three lambda: " + "; ".join(
              f"{LABELS[i]} -> {diag[i]}" for i in range(3)))

    # ---- A3: self-test of (*) and of the committed coefficients ------------
    tot = sp.cancel(sp.simplify(sum(diag)))
    check("A3_completeness_selftest", tot == 1,
          f"sum_lambda tau(e_lambda) = {tot} (must be tau(1) = 1; this "
          "validates both the tau(T_u T_v) = delta_{u,v^-1} rule and the "
          "committed coefficients)")

    # ---- A4: the diagonal entries equal the T_e coefficients ---------------
    ok_te = all(sp.simplify(diag[i] - coeffs[LABELS[i]][0]) == 0 for i in range(3))
    check("A4_diagonal_is_Te_coefficient", ok_te,
          "B(e_lambda, e_lambda) = tau(e_lambda) = the T_e coefficient, as it "
          "must be for an idempotent")

    # ---- A5: numerical value at the proton pin ----------------------------
    from q_parameter import Q_50_DIGIT_STR as Q50

    def eval_at(expr, q0):
        """Evaluate a QQ(q) rational function at `q0` in mpmath.

        Numerator and denominator are taken as INTEGER-coefficient polynomials
        and Horner-evaluated in mpf separately, then divided once. Nothing is
        routed through `float`, and no sympy Float ever enters -- substituting a
        sympy Float would silently set the working precision from the literal
        rather than from mp.dps.
        """
        num, den = sp.fraction(sp.cancel(sp.together(expr)))
        pn = sp.Poly(num, q).all_coeffs()
        pd = sp.Poly(den, q).all_coeffs()
        def horner(cs):
            acc = mp.mpf(0)
            for c in cs:
                acc = acc * q0 + mp.mpf(int(c))
            return acc
        return horner(pn) / horner(pd)

    with mp.workdps(60):
        q0 = mp.mpf(str(Q50))
        vals = {LABELS[i]: eval_at(diag[i], q0) for i in range(3)}
        ok_pos = all(v > 0 for v in vals.values())
        tot0 = sum(vals.values())
        ok_sum0 = abs(tot0 - 1) < mp.mpf(10) ** (-45)
        shown = "; ".join(f"{k} -> {mp.nstr(v, 25)}" for k, v in vals.items())
    check("A5_diagonal_positive_at_q0", ok_pos and ok_sum0,
          "at the proton pin q0 = " + mp.nstr(q0, 20) + ": " + shown +
          f"  (numeric completeness sum = {mp.nstr(tot0, 25)}, |sum - 1| < 1e-45: "
          f"{ok_sum0})")

    verdict = (
        "The Frobenius pairing restricted to Z(H_3(q)) is DIAGONAL in the "
        "central-idempotent basis, with nonzero diagonal. So two DISTINCT "
        "curvature-rank strata -- each a span of idempotents -- pair to "
        "IDENTICALLY ZERO, and each stratum is SELF-dual. The asserted "
        "'rank-l pairs with rank-(N-l)' is zero exactly where it claims to be "
        "perfect, whenever l != N-l. This is the qou-xsv8 defect, present in "
        "prf:spectral-sequence-collapse as well as in "
        "prf:quantum-dilogarithm-stratified Step 1."
    )
    print("\n" + verdict)

    out = {
        "computation": "centre-frobenius-pairing-is-diagonal",
        "scriptFile": os.path.basename(__file__),
        "computedAt": time.strftime("%Y-%m-%dT%H:%M:%S+00:00", time.gmtime()),
        "bean": "qou-xsv8",
        "kind": "exploratory-probe",
        "engine": "sympy exact QQ(q); mpmath mpf for the single q0 evaluation",
        "free_parameters": 0,
        # q0 enters ONLY in A5, a display evaluation of an exact QQ(q) quantity;
        # every assertion that carries the verdict is anchor-free.
        "q0Anchor": "proton",
        "q0Value": Q50,
        "inputs": {
            "n": 3,
            "idempotent_source": "probe-h3-central-idempotents-exact.witness.json",
            "word_basis": WORDS,
            "inversion_permutation": INV,
            "tau_rule": "tau(T_u T_v) = delta_{u, v^-1}  (AGENTS.md 7a convention)",
        },
        "results": {
            "gram_offdiagonal": sorted({str(v) for _, _, v in off}),
            "gram_diagonal": [str(d) for d in diag],
            "diagonal_sum": str(tot),
            "verdict": verdict,
            "scope": "(b) structural exclusion -- the invariant is e_l.e_m = 0 "
                     "for l != m, which holds for every linear functional and "
                     "every n, so no choice of filtration or of Frobenius form "
                     "can restore a cross-stratum pairing on idempotent strata.",
        },
        "assertions": assertions,
        "allPassed": all(a["passed"] for a in assertions),
        "durationMs": int((time.monotonic() - t0) * 1000),
    }
    wp = _HERE / "centre-frobenius-pairing-is-diagonal.witness.json"
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    out.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        out, script_path=__file__, engine=None, q0_anchor=None)
    wp.write_text(json.dumps(out, indent=2) + "\n")
    print(f"\nwitness -> {wp}")
    return 0 if out["allPassed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
