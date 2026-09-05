#!/usr/bin/env python3
"""Higher rungs of the W_λ defect ladder — degree-3k law, exact through k=5.

Context.  The q-Plancherel defect 1 − Z(n) = Σ_k c_{2k}(n) h^{2k}
(h = q − 1/q) has per-rung polynomial coefficients c_{2k}(n) in n.  The
first two rungs are settled exactly:

  c_2(n) = C(n) = −n(n−1)(2n−13)/144            (degree 3; Lean-proved as
                                                  n144C_closed_form)
  c_4(n) = D(n)                                  (degree 6; PR #2965)

and the empirical pattern is **deg c_{2k}(n) = 3k**.  Before #2965 the
c_{2k} were obtained by Taylor *extraction* (mpmath, fragile past k≈3).
The Kerov–Plancherel-moment route (`exact_ladder` in the sibling producer)
makes each c_{2k}(n) an **exact rational** function of n — no extraction,
no float — so the degree law can be *checked exactly* at high k.

This probe:
  1. computes c_2..c_{2K} (K=5) as exact Fractions over n = 2..N via the
     Kerov route;
  2. reconstructs each c_{2k} as an exact polynomial in n by finite
     differences and reports its degree;
  3. verifies deg c_{2k} = 3k for k = 1..5 (extends #2965's k≤3);
  4. HELD-OUT check: reconstructs each polynomial from n=2..(3k+2) only,
     then predicts c_{2k} at larger n and confirms the exact match — so
     the degree-3k law is genuinely predictive, not an interpolation
     tautology.

Parameter-free; exit 0 on success.  Emits a witness JSON.
"""
import json
import os
import sys
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from keystone_wlambda_defect_coeff_ladder import exact_ladder  # noqa: E402
import os as _os_sidu  # noqa: E402 -- atomic witness write (qou-sidu)


def poly_degree(values):
    """Degree of the unique polynomial through (n, values[n]) via finite
    differences over exact Fractions.  values is a dict n -> Fraction."""
    ns = sorted(values)
    seq = [values[n] for n in ns]
    deg = 0
    while len(seq) > 1 and any(x != 0 for x in seq):
        nxt = [seq[i + 1] - seq[i] for i in range(len(seq) - 1)]
        if all(x == 0 for x in nxt):
            break
        seq = nxt
        deg += 1
    return deg


def newton_poly(points):
    """Newton forward-difference interpolation; returns f(x) as a callable
    on Fraction inputs.  points: list of (n:int, v:Fraction) on consecutive n."""
    ns = [Fraction(n) for n, _ in points]
    fd = [v for _, v in points]
    diffs = [fd[0]]
    cur = fd[:]
    while len(cur) > 1:
        cur = [cur[i + 1] - cur[i] for i in range(len(cur) - 1)]
        diffs.append(cur[0])
    h = ns[1] - ns[0] if len(ns) > 1 else Fraction(1)

    def f(x):
        x = Fraction(x)
        total = Fraction(0)
        term = Fraction(1)
        for j, d in enumerate(diffs):
            total += d * term / _fact(j)
            term *= (x - ns[0]) / h - j
        return total

    return f


def _fact(k):
    r = 1
    for i in range(2, k + 1):
        r *= i
    return Fraction(r)


def main():
    K = 5
    N = 19  # ample for deg up to 15 plus held-out tail
    ns = list(range(2, N + 1))

    # Collect exact c_{2k}(n) for k = 1..K.
    coeffs = {k: {} for k in range(1, K + 1)}
    for n in ns:
        cs = exact_ladder(n, K)  # [c_2, c_4, …, c_{2K}]
        for k in range(1, K + 1):
            coeffs[k][n] = cs[k - 1]

    rungs = []
    all_ok = True
    for k in range(1, K + 1):
        deg = poly_degree(coeffs[k])
        expect = 3 * k
        ladder_ok = deg == expect

        # Held-out predictive check: fit on the minimal n-window
        # (3k+1 points → degree 3k), predict on the remaining n.
        npts = expect + 1
        fit_ns = ns[:npts]
        fit_pts = [(n, coeffs[k][n]) for n in fit_ns]
        f = newton_poly(fit_pts)
        held_out = ns[npts:]
        heldout_ok = all(f(n) == coeffs[k][n] for n in held_out)

        all_ok = all_ok and ladder_ok and heldout_ok
        rungs.append({
            "k": k,
            "coeff": f"c_{2*k}",
            "degree": deg,
            "expected_degree_3k": expect,
            "degree_law_ok": ladder_ok,
            "fit_window_n": [fit_ns[0], fit_ns[-1]],
            "held_out_n": [held_out[0], held_out[-1]] if held_out else None,
            "held_out_predictive_ok": heldout_ok,
        })
        tag = "OK" if (ladder_ok and heldout_ok) else "FAIL"
        print(f"c_{2*k}(n): degree = {deg}  (3k = {expect})  "
              f"held-out predictive {'✓' if heldout_ok else '✗'}  -> LADDER {tag}")

    # Spot-confirm the two settled rungs against their closed forms.
    def C_closed(n):
        return Fraction(-n * (n - 1) * (2 * n - 13), 144)
    c2_match = all(coeffs[1][n] == C_closed(n) for n in ns)
    print(f"\nc_2(n) == −n(n−1)(2n−13)/144 (Lean n144C_closed_form)? {c2_match}")
    assert c2_match, "c_2 disagrees with the Lean-proved C(n) closed form"
    assert all_ok, "degree-3k law or held-out check FAILED"
    print("\nVERDICT: degree-3k law confirmed EXACTLY through k=5 (deg 3,6,9,12,15),")
    print("each rung held-out predictive — extends PR #2965 (k≤3) via the Kerov route.")

    witness = {
        "schema": "witness/v1",
        "name": "wlambda-ladder-higher-rungs",
        "description": "W_λ q-Plancherel defect ladder: exact c_{2k}(n) via Kerov "
                       "moments; degree-3k law confirmed exactly + held-out "
                       "predictively through k=5.",
        "computation": {
            "script": "computations/keystone_wlambda_ladder_higher_rungs.py",
            "method": "exact Kerov–Plancherel moment series (Fraction); finite-"
                      "difference degree; Newton held-out prediction",
            "parameter_free": True,
        },
        "result": {
            "K": K,
            "n_range": [ns[0], ns[-1]],
            "rungs": rungs,
            "degree_3k_law": all_ok,
            "c2_matches_lean_closed_form": c2_match,
        },
        "provenance": {
            "extends": "PR #2965 (exact_ladder, k≤3)",
            "lean_anchor": "QOU.BraidKnot.WLambdaDefectClosedForm.n144C_closed_form",
            "keystone_bean": "s5bb",
        },
    }
    import sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="python")
    witness["scriptFile"] = os.path.basename(__file__)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "wlambda-ladder-higher-rungs.witness.json")
    # Atomic write (bean `qou-sidu`): serialize to a sibling temp file and
    # `os.replace` it into position. `open(..., "w")` TRUNCATES before the
    # dump runs, so any exception in between leaves the committed witness
    # empty or partial -- the shape that emptied 22 witnesses to zero bytes
    # in one `producer_importability_audit` run. `os.replace` is atomic on
    # POSIX within a filesystem, hence a SIBLING temp file.
    _wpath_sidu = out
    _wtmp_sidu = str(_wpath_sidu) + ".tmp"
    with open(_wtmp_sidu, "w", encoding="utf-8") as fh:
        json.dump(witness, fh, indent=2)
        fh.write("\n")
    _os_sidu.replace(_wtmp_sidu, _wpath_sidu)
    print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
