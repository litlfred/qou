#!/usr/bin/env python3
# polynomial_q_not_applicable: hyperbolic-geometry numeric probe.
"""one_loop_c_sigma_percusp_dissolution_probe.py — the per-cusp factor was never there.

Bean `qou-fl4t` / `qou-pn5j`. Follows PR #4691, #4697, #4707, #4708 and the
multi-cusp derivation (`docs/audits/2026-08-07-one-loop-multicusp-derivation.md`).

THE CLAIM UNDER TEST

`computations/whitehead_c_sigma_torsion.py` reconciles the Jones-side constant
with a geometrically computed torsion through a PER-CUSP factor:

    c_sigma = 2^{(c-1)/2} * |tau_old|^{-1/2}

described there as "the standard per-cusp Gaussian-integration factor". PR
#4691 showed `|tau_old|` is not a topological invariant, so the factor was
fitted against an ambiguity of its own size and the three "confirmations"
(c = 1, 2, 3) constrained nothing. The impact analysis then guessed that fixing
the construction would DISSOLVE that line rather than repair it. This probe
tests that guess.

WHAT IS MEASURED, AND WHY IT IS NOT CIRCULAR

The Jones-side constants are computed from colored Jones / Kashaev asymptotics
with NO reference to any determinant:

    c_sigma(4_1)  = 0.75983568565159255077   (17 digits vs 3^{-1/4})
                    computations/whitehead-c-sigma-fig8-calib.witness.json
    c_sigma(L5a1) = 0.59460355750136053336   (20 digits vs 2^{-3/4})
                    computations/whitehead-c-sigma-hiprec.witness.json
    c_0(L6a4)     = -1.38281051225792130     (NMAX=56 Habiro tower)
                    computations/probes/borromean-jones-1loop-torsion.witness.json

The two are the SAME c_sigma definition — the fig8 calibration witness says so
in as many words ("same c_sigma definition ... as the Whitehead run"). So

    k_c := c_sigma * |tau_DG|^{1/2}

can be read off at c = 1 and at c = 2 independently, and compared. If the
1-loop prefactor really carries a per-cusp factor, k_c must move by sqrt(2)
between them.

RESULT: k_1 = k_2 = 2^{-1/2}, to the precision of the Jones extractions.
The per-cusp factor is gone. Section D states it as a ZERO-PARAMETER
PREDICTION: calibrate k on 4_1 alone, then predict c_sigma(L5a1) with nothing
adjustable, and compare against the 20-digit measurement.

WHY THE OLD FIT LOOKED LIKE IT WORKED (section E)

On the DEFAULT triangulations of 4_1, L5a1 and L6a4 — and only there —
`|tau_old| = 2^c |tau_DG|`. Substituting,

    2^{(c-1)/2} |tau_old|^{-1/2} = 2^{(c-1)/2} 2^{-c/2} |tau_DG|^{-1/2}
                                 = 2^{-1/2} |tau_DG|^{-1/2}

identically. The per-cusp factor is exactly the c-dependence needed to undo the
`2^c` between the wrong determinant and the right invariant. It was a
reparametrization, not a Gaussian-integration factor. Section E measures
whether that `2^c` relation is general or an artifact of those three defaults.

THIS ALSO CLOSES A CAVEAT THE DERIVATION LEFT OPEN

The multi-cusp derivation could not pin the overall constant at c >= 2:
invariance and the change-of-curve law are both blind to a factor depending
only on c. The Jones side is not — it is an outside measurement. Under the
1-loop prefactor form `c_sigma ∝ |tau|^{-1/2}` (the same assumption the corpus
already makes, validated on 4_1 to 17 digits), k_1 = k_2 pins that factor to
be ABSENT between c = 1 and c = 2.

  * c = 1 vs c = 2 is the strong comparison: identical c_sigma definition,
    17 and 20 digits.
  * c = 3 is SUPPORTING ONLY. Its own witness flags "an unresolved
    normalization+cusp offset" between the 1-cusp un-normalized 4_1 anchor and
    the 3-cusp Habiro tower, and its extraction gives p = 1.4993 against the
    exact 3/2. It is quoted here at the percent level, not as a third pin.

Audit-only. No float64 enters the witness.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "substrate"))
from _precision import set_compute_dps, fmt  # noqa: E402
from one_loop_torsion import one_loop  # noqa: E402

set_compute_dps()

ROOT = Path(__file__).resolve().parent.parent
MECHANISM = ["4_1", "5_2", "6_2", "7_4", "L5a1", "m125", "L6a2", "L6a1",
             "L6a4", "s776", "L7a1", "L8a1", "L10n1"]


def _w(rel):
    return json.loads((ROOT / rel).read_text())


def tau_old(name):
    """The superseded construction, verbatim: J = A - B z/(1-z), greedy independent
    edge rows + one meridian per cusp, no 1/2 and no flattening monomial."""
    import snappy

    M = snappy.Manifold(name)
    N, c = M.num_tetrahedra(), M.num_cusps()
    bits = int(mp.mp.dps * 3.3219) + 16
    z = [mp.mpc(mp.mpf(str(s.real()).replace(" ", "")),
                mp.mpf(str(s.imag()).replace(" ", "")))
         for s in M.tetrahedra_shapes("rect", bits_prec=bits)]
    t = [z[j] / (1 - z[j]) for j in range(N)]
    ge = M.gluing_equations("rect")
    ne = len(ge) - 2 * c

    def row(A, B):
        return [A[j] - B[j] * t[j] for j in range(N)]

    edges = [row(A, B) for (A, B, _) in ge[:ne]]
    mer = [row(*ge[ne + 2 * i][:2]) for i in range(c)]
    tol = mp.mpf(10) ** -20
    basis, chosen = [], []
    for i, e in enumerate(edges):
        v = list(e)
        for b in basis:
            p = next(k for k, x in enumerate(b) if abs(x) > tol)
            if abs(v[p]) > tol:
                f = v[p] / b[p]
                v = [a - f * bb for a, bb in zip(v, b)]
        if any(abs(x) > tol for x in v):
            basis.append(v)
            chosen.append(i)
    rows = [edges[i] for i in chosen[: N - c]] + mer
    return abs(mp.det(mp.matrix(rows)))


def main() -> int:
    import snappy

    calib = _w("whitehead-c-sigma-fig8-calib.witness.json")["data"] \
        if "data" in _w("whitehead-c-sigma-fig8-calib.witness.json") \
        else _w("whitehead-c-sigma-fig8-calib.witness.json")
    hip = _w("whitehead-c-sigma-hiprec.witness.json")
    borro = _w("probes/borromean-jones-1loop-torsion.witness.json")["data"]

    cs41 = mp.mpf(calib["c_sigma_fig8_extrapolated"])
    csW = mp.mpf(hip["c_sigma_extrapolated"])
    c0B = mp.mpf(str(borro["fit_vol_fixed"]["c0"]))
    csB = mp.e ** c0B

    tau41 = abs(one_loop(snappy.Manifold("4_1")))
    tauW = abs(one_loop(snappy.Manifold("L5a1")))
    tauB = abs(one_loop(snappy.Manifold("L6a4")))

    print("A. corrected DG 1-loop invariant (triangulation-invariant)\n")
    for nm, t, c in (("4_1", tau41, 1), ("L5a1", tauW, 2), ("L6a4", tauB, 3)):
        print(f"   |tau({nm})| = {mp.nstr(t, 22):<24} c={c}")

    print("\nB. Jones-side constants — measured, no determinant anywhere\n")
    print(f"   c_sigma(4_1)  = {mp.nstr(cs41, 22)}   (3^-1/4 to 17 digits)")
    print(f"   c_sigma(L5a1) = {mp.nstr(csW, 22)}   (2^-3/4 to 20 digits)")
    print(f"   c_sigma(L6a4) = exp(c_0) = {mp.nstr(csB, 18)}   (NMAX=56 tower)")

    print("\nC. k_c := c_sigma * |tau_DG|^{1/2}. A per-cusp factor would move it.\n")
    k1 = cs41 * mp.sqrt(tau41)
    k2 = csW * mp.sqrt(tauW)
    k3 = csB * mp.sqrt(tauB)
    ref = 1 / mp.sqrt(2)
    for lbl, k, c in (("4_1", k1, 1), ("L5a1", k2, 2), ("L6a4", k3, 3)):
        print(f"   c={c}  {lbl:6} k = {mp.nstr(k, 20):<24}"
              f" k/2^-1/2 = {mp.nstr(k / ref, 14)}")
    d12 = abs(k1 - k2) / k2
    print(f"\n   |k_1 - k_2| / k_2 = {mp.nstr(d12, 4)}   "
          f"({int(-mp.log10(d12)) if d12 > 0 else 99} digits of agreement)")
    print(f"   a per-cusp factor would require k_2 / k_1 = sqrt(2) = 1.4142…;"
          f" measured {mp.nstr(k2 / k1, 18)}")
    print(f"   c=3 supporting only: k_3 / k_1 = {mp.nstr(k3 / k1, 8)} "
          f"({mp.nstr(abs(k3 - k1) / k1 * 100, 3)}%, NMAX=56, normalization offset flagged)")

    print("\nD. ZERO-PARAMETER PREDICTION: calibrate k on 4_1, predict L5a1\n")
    pred = k1 / mp.sqrt(tauW)
    rel = abs(pred - csW) / csW
    dig = int(-mp.log10(rel)) if rel > 0 else 99
    print(f"   predicted c_sigma(L5a1) = {mp.nstr(pred, 22)}")
    print(f"   measured  c_sigma(L5a1) = {mp.nstr(csW, 22)}")
    print(f"   agreement: ~{dig} digits, nothing fitted.")
    ok = rel < mp.mpf("1e-14")

    print("\nE. mechanism — is |tau_old| = 2^c |tau_DG| general, or those three?\n")
    mech = {}
    general = True
    for nm in MECHANISM:
        M = snappy.Manifold(nm)
        c = M.num_cusps()
        try:
            old = tau_old(nm)
            new = abs(one_loop(M))
        except Exception as e:
            print(f"   {nm:8} ERROR {type(e).__name__}")
            continue
        r = old / new
        hit = abs(r - 2 ** c) / 2 ** c < mp.mpf("1e-20")
        general &= hit
        mech[nm] = {"cusps": c, "ratio_old_over_new": fmt(r),
                    "equals_2_pow_c": bool(hit)}
        print(f"   {nm:8} c={c}  |tau_old|/|tau_DG| = {mp.nstr(r, 16):<20}"
              f" 2^c = {2 ** c:<5} {'MATCH' if hit else 'no'}")
    print(f"\n   holds on every manifold tested: {general}")
    if not general:
        print("   => the 2^c relation is NOT an identity. It holds on the three")
        print("      default triangulations the per-cusp factor was fitted to,")
        print("      which is exactly why the fit looked like it worked.")

    print("\n" + "-" * 72)
    print("The per-cusp factor 2^{(c-1)/2} DISSOLVES. With the correct invariant")
    print("the law is c_sigma = 2^{-1/2} |tau_DG|^{-1/2}, the same constant at")
    print("c = 1 and c = 2, and the c=1 calibration predicts c=2 with nothing")
    print("adjustable. The old factor was the c-dependence needed to undo the")
    print("2^c between the wrong determinant and the DG invariant.")
    print()
    print("This also closes the normalization caveat the multi-cusp derivation")
    print("left open, for c = 1 vs 2: the Jones side is an outside measurement,")
    print("and it says the DG normalization carries NO extra c-dependence.")
    print("c = 3 is consistent at the percent level but its tower has a flagged")
    print("normalization offset, so it is supporting evidence, not a third pin.")
    print()
    print("c_sigma = 2^{-3/4} is now DERIVED from a triangulation-invariant")
    print("torsion plus a c=1 calibration -- but bean qou-pn5j should be moved")
    print("only after review: the step being asserted is the prefactor FORM")
    print("c_sigma ∝ |tau|^{-1/2}, which is validated on 4_1, not proved.")

    wit = {
        "description": (
            "The per-cusp factor 2^{(c-1)/2} in whitehead_c_sigma_torsion.py "
            "dissolves once the 1-loop determinant is corrected. k_c = c_sigma "
            "|tau_DG|^{1/2} is the same constant 2^{-1/2} at c=1 and c=2, so the "
            "c=1 calibration predicts c_sigma(L5a1) with zero free parameters. "
            "Also closes, for c=1 vs 2, the overall-normalization caveat left "
            "open by the multi-cusp derivation."
        ),
        "computation": "one_loop_c_sigma_percusp_dissolution_probe",
        "audit_only": True,
        "tau_dg": {"4_1": fmt(tau41), "L5a1": fmt(tauW), "L6a4": fmt(tauB)},
        "c_sigma_measured": {"4_1": fmt(cs41), "L5a1": fmt(csW), "L6a4": fmt(csB)},
        "k_c": {"1": fmt(k1), "2": fmt(k2), "3": fmt(k3)},
        "k1_vs_k2_rel_diff": fmt(d12),
        "per_cusp_factor_survives": False,
        "zero_parameter_prediction": {
            "predicted_c_sigma_L5a1": fmt(pred),
            "measured_c_sigma_L5a1": fmt(csW),
            "rel_diff": fmt(rel),
            "passes": bool(ok),
        },
        "mechanism_tau_old_over_tau_dg": mech,
        "mechanism_is_general": bool(general),
        "c3_supporting_only": (
            "borromean-jones-1loop-torsion.witness.json flags an unresolved "
            "normalization+cusp offset vs the 1-cusp anchor; p=1.4993 vs 3/2"
        ),
        "assumption": (
            "the 1-loop prefactor form c_sigma ∝ |tau|^{-1/2}, validated on 4_1 "
            "to 17 digits, is assumed — not proved — here"
        ),
        "bears_on": ["bean qou-fl4t", "bean qou-pn5j", "PR #4691", "PR #4697",
                     "PR #4707", "PR #4708"],
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    out = ROOT / "one-loop-c-sigma-percusp-dissolution.witness.json"
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    wit.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        wit, script_path=__file__, engine=None, q0_anchor=False)
    out.write_text(json.dumps(wit, indent=2, ensure_ascii=False) + "\n")
    print(f"\nWitness: {out.name}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
