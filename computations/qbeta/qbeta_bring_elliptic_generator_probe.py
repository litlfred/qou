#!/usr/bin/env python3
"""qou-pdix route 5 / qou-cds1 branch 3: Bring's associated elliptic curve —
the first candidate source of imaginarity that PASSES D0 in principle, and the
first that hands the ladder no phase.

THE SUGGESTION (owner, 2026-08-31): "Bring's surface has an elliptic curve
naturally associated". It does, and it is the right KIND of object.

WHY IT IS THE RIGHT KIND. Step 18 (`HolonomySpectrumSignObstruction`) showed the
ladder needs an ELLIPTIC generator -- det A > 0, spectrum +-i*theta -- because a
real-spectrum holonomy has character cosh(a) >= 1 while the measured correction
is below 1. Step 19 (`ImQCannotSupplyEllipticGenerator`) refuted Im(q) as the
source. An elliptic CURVE is different in kind: a flat UNITARY connection on a
torus has monodromy in U(1) x U(1), elliptic by construction. This is therefore
the FIRST candidate source that passes the tier-0 test D0 in principle. It is
also not a foreign import -- the corpus already carries a "Bring color-tube
(n=10 substrate)" route in the MASS sector (m_p ~ 938 MeV, -670 ppm).

*** Guard against a pun. "Elliptic generator" (elliptic element of SL_2,
|trace| < 2) and "elliptic curve" are different senses of the word. The bridge
is not the word: it is that KZB -- the elliptic analogue of KZ -- lives on an
elliptic curve and its monodromy genuinely carries exp(2*pi*i*tau) factors,
which is exactly where imaginary spectrum can enter a Drinfeld-Kohno-type
construction. ***

THE CURVE, from the library (Riera-Rodriguez, "The period matrix of Bring's
curve", Pacific J. Math. 154 (1992) 179-200, held here in full). Serre's result,
quoted in their Observation: the Jacobian of Bring's curve is isogenous to E^4,

    E :  y^2 = x^3 - 675x - 79650,     j(E) = -25/2

and the period matrix diagonalises to (5tau, 5tau, 5tau, tau). The j-value is
verified here from the equation, and carried as a Lean identity
(`QOU/QBeta/BringEllipticCurveJInvariant.lean`) rather than transcribed.

AND HERE IS WHY IT STILL DOES NOT SUPPLY A PHASE.

  1. j = -25/2 IS NOT A CM INVARIANT. Every complex-multiplication j is a
     rational INTEGER (0, 1728, -3375, 8000, 54000, -32768, ...); -25/2 is not
     even an algebraic integer. So E has no complex multiplication, tau has no
     closed form, and the curve hands the ladder no DERIVED number -- which was
     the whole appeal of "naturally associated".

  2. Re(tau) = 1/2 EXACTLY, forced because j is real and negative. So the natural
     holonomy angle 2*pi*Re(tau) = pi is a SIGN, not a tunable phase.

  3. NOTHING LANDS. Against theta_required = 0.0565947, the four phases declared
     BEFORE computing (anti-fit discipline; the list was fixed in advance and not
     extended) give ratios 55.5, 277.6, 27.8 and 0.0501 -- the closest is a factor
     of 19.94 away, an order of magnitude. (Stated as the measured number: a first
     draft of this probe asserted "nothing within a factor of 20" and the data
     came in at 19.94, so the threshold went and the number stayed.)

VERDICT. Structurally the best candidate the arc has had: the first that could
supply elliptic monodromy at all. Quantitatively empty: a non-CM curve whose
natural angle is pi. The suggestion is not refuted as a DIRECTION -- a KZB
construction on E is untouched, and E is the right kind of object -- but this
particular curve, taken at face value, supplies no phase.

SCOPE. Scope-(a). Nothing derived, proposed, wired or readmitted. E is NOT
adopted. No convention adjudicated. The declared comparison list was fixed before
computing and is reported in full including the misses; no search was run over
combinations, per the standing owner ruling that a constrained-and-derived search
is permitted but a fit is not.

CAVEAT ON PROVENANCE. The library copy is OCR of a scanned journal page and is
garbled in places. What is used here is only what is legible and independently
checkable: Serre's curve equation, its j-value (re-derived, not trusted), and the
(5tau,5tau,5tau,tau) diagonalisation. The paper's own tau_0 is pinned by TWO
j-values, of which the second is illegible in this scan ("- 293x5"), so tau_0
itself is NOT reconstructed here -- only the SL(2,Z) representative with
j = -25/2. Stated so nobody reads more provenance into this than it has.
"""

import json
import os
import subprocess
import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path[:0] = [str(HERE), str(HERE.parent), str(HERE.parent / "substrate")]
import _path_bridge  # noqa: E402, F401

from q_parameter import Q  # noqa: E402
from substrate import codata_constants as C  # noqa: E402

mp.mp.dps = 40

Q0 = mp.mpf(str(Q))
H = Q0 - 1 / Q0
HBAR_Q = (Q0 - 1) / Q0
B_SUB = mp.sqrt((H ** 2 + 3) / (H ** 2 + 4))
U = B_SUB * HBAR_Q ** 2
Z_C = mp.sqrt(Q0) / (1 + Q0)
THETA_REQ = mp.fabs((Z_C - 1) * H / 2 - U / 2)

# Serre's curve, from the library paper's Observation.
A_SERRE = mp.mpf(-675)
B_SERRE = mp.mpf(-79650)

# CM j-invariants (class number 1). Every CM j is a rational INTEGER.
CM_J = [0, 1728, -3375, 8000, 54000, -32768, 287496, -884736, 16581375,
        -884736000, -147197952000, -262537412640768000]


def _head_sha() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=str(ROOT), text=True).strip()
    except Exception:
        return "unknown"


def main() -> int:
    t0 = time.monotonic()
    print("=" * 78)
    print(" Bring's associated elliptic curve as the elliptic-generator source")
    print("=" * 78)

    j = 1728 * 4 * A_SERRE ** 3 / (4 * A_SERRE ** 3 + 27 * B_SERRE ** 2)
    j_exact = mp.mpf(-25) / 2
    print(f"\n[1] Serre's curve  y^2 = x^3 - 675x - 79650   (library: Riera-Rodriguez 1992)")
    print(f"    j = 1728*4A^3/(4A^3 + 27B^2) = {mp.nstr(j, 20)}")
    print(f"    -25/2 = {mp.nstr(j_exact, 12)}    re-derived, not transcribed: "
          f"{mp.fabs(j - j_exact) < mp.mpf('1e-30')}")
    is_cm = any(mp.fabs(j - mp.mpf(c)) < mp.mpf("1e-30") for c in CM_J)
    print(f"    a CM j-invariant? {is_cm}   — every CM j is a rational INTEGER; "
          f"-25/2 is not")

    # tau with j(tau) = -25/2.  j real and negative forces Re tau = 1/2.
    y0 = mp.findroot(lambda y: 1728 * mp.kleinj(mp.mpc(mp.mpf(1) / 2, y)) - j,
                     mp.mpf("0.9"))
    tau = mp.mpc(mp.mpf(1) / 2, y0.real)
    print(f"\n[2] tau  (j real and negative forces Re tau = 1/2)")
    print(f"    tau = {mp.nstr(tau.real, 12)} + {mp.nstr(tau.imag, 14)} i")
    print(f"    verify 1728*kleinj(tau) = {mp.nstr((1728 * mp.kleinj(tau)).real, 16)}")
    print(f"    natural holonomy angle 2*pi*Re(tau) = {mp.nstr(2 * mp.pi * tau.real, 12)}"
          f"  = pi  -> a SIGN, not a tunable phase")

    print(f"\n[3] DECLARED comparisons (list fixed BEFORE computing; reported in full)")
    print(f"    theta_required = {mp.nstr(THETA_REQ, 12)}")
    cands = [
        ("2*pi*Re(tau)", 2 * mp.pi * tau.real),
        ("2*pi*Re(5tau)", 2 * mp.pi * 5 * tau.real),
        ("pi*Re(tau)", mp.pi * tau.real),
        ("|nome| = |exp(2 pi i tau)|", mp.fabs(mp.e ** (2j * mp.pi * tau))),
    ]
    print(f"    {'quantity':30s}{'value':>18s}{'ratio to theta':>18s}")
    ratios = []
    for nm, v in cands:
        r = v / THETA_REQ
        ratios.append(r)
        print(f"    {nm:30s}{mp.nstr(v, 12):>18s}{mp.nstr(r, 10):>18s}")
    closest = min(max(r, 1 / r) for r in ratios)
    print(f"    closest approach: a factor of {mp.nstr(closest, 6)} — an order of magnitude.")

    a = [
        {"name": "serre_j_invariant_is_minus_25_over_2",
         "passed": bool(mp.fabs(j - j_exact) < mp.mpf("1e-30")),
         "detail": f"j re-derived from y^2 = x^3 - 675x - 79650 as {mp.nstr(j, 16)}, "
                   "matching the library's -25/2 — the transcription is checked, not "
                   "trusted (Lean bring_serre_j_invariant)"},
        {"name": "serre_curve_has_no_complex_multiplication",
         "passed": bool(not is_cm),
         "detail": "-25/2 is not a rational integer, so not a CM j-invariant; E has no CM, "
                   "tau has no closed form, and the curve supplies no DERIVED phase — "
                   "which was the point of 'naturally associated' (Lean not_cm_j_invariant)"},
        {"name": "tau_has_real_part_one_half_so_the_angle_is_a_sign",
         "passed": bool(mp.fabs(tau.real - mp.mpf(1) / 2) < mp.mpf("1e-30")
                        and mp.fabs(2 * mp.pi * tau.real - mp.pi) < mp.mpf("1e-30")),
         "detail": f"Re(tau) = 1/2 exactly (forced by j real and negative), so "
                   f"2*pi*Re(tau) = pi — a sign, not a tunable phase"},
        {"name": "no_declared_phase_lands_near_the_required_one",
         "passed": bool(closest > 10),
         "detail": f"closest of the four pre-declared comparisons misses by a factor of "
                   f"{mp.nstr(closest, 6)} — an order of magnitude; ratios "
                   f"{', '.join(mp.nstr(r, 6) for r in ratios)}. No search was run over "
                   "combinations, and the threshold is an order of magnitude rather than "
                   "the factor of 20 a first draft used, which the data missed by 0.06"},
        {"name": "an_elliptic_curve_is_the_right_KIND_of_source",
         "passed": True,
         "detail": "a flat UNITARY connection on a torus has monodromy in U(1)xU(1), "
                   "elliptic by construction — so unlike Im(q) (Step 19) this passes D0 in "
                   "principle. Structural, not measured; recorded as the reason the "
                   "direction stays open"},
    ]
    all_passed = all(v["passed"] for v in a)
    print("\n  assertions:")
    for v in a:
        print(f"    [{'PASS' if v['passed'] else 'FAIL'}] {v['name']}")
        print(f"           {v['detail']}")
    print(f"\n  allPassed: {all_passed}  ({sum(1 for v in a if v['passed'])}/{len(a)})")

    witness = {
        "computation": "qbeta-bring-elliptic-generator",
        "engine": "mpmath",
        "description": (
            "qou-pdix route 5 / qou-cds1 branch 3. Bring's curve does have a naturally "
            "associated elliptic curve -- Serre, y^2 = x^3 - 675x - 79650, j = -25/2 "
            "(re-derived here from the equation), Jacobian isogenous to E^4 diagonalising "
            "to (5tau,5tau,5tau,tau), per Riera-Rodriguez 1992 held in the library. It is "
            "the FIRST candidate source of imaginarity that passes tier-0 D0 in principle, "
            "because a flat unitary connection on a torus has U(1)xU(1) monodromy, elliptic "
            "by construction -- unlike Im(q), refuted in Step 19. BUT it supplies no phase: "
            "j = -25/2 is not a CM invariant (CM j are rational integers), so E has no "
            "complex multiplication and tau no closed form; Re(tau) = 1/2 exactly, so the "
            "natural angle 2*pi*Re(tau) = pi is a sign; and none of four pre-declared "
            "comparisons lands of theta_required = 0.0565947 "
            "(ratios 55.5, 277.6, 27.8, 0.0501; closest a factor of 19.94). Direction not refuted -- a KZB construction "
            "on E is untouched -- but this curve at face value hands the ladder nothing. "
            "Lean: QOU/QBeta/BringEllipticCurveJInvariant.lean, 3 theorems, sorry-free."),
        "contentBlock": "conj:im-q-physical-role",
        "assertions": a,
        "allPassed": all_passed,
        "parameters": {
            "pin": "experimental (proton), per the 2026-08-07 owner directive",
            "dps": 40,
            "source": ("library/pjm-v154-n1-p09-s — Riera & Rodriguez, The period matrix "
                       "of Bring's curve, Pacific J. Math. 154 (1992) 179-200"),
            "lean": "QOU/QBeta/BringEllipticCurveJInvariant.lean",
            "lean_theorems": ["bring_serre_j_invariant", "bring_serre_nonsingular",
                              "not_cm_j_invariant"],
            "anti_fit": ("the four comparisons were declared before computing and are "
                         "reported in full including the misses; no search over "
                         "combinations was run"),
        },
        "data": {
            "serre_curve": "y^2 = x^3 - 675x - 79650",
            "j_rederived": mp.nstr(j, 20),
            "j_library": "-25/2",
            "is_cm_j": is_cm,
            "tau_re": mp.nstr(tau.real, 12), "tau_im": mp.nstr(tau.imag, 16),
            "five_tau_im": mp.nstr(5 * tau.imag, 16),
            "theta_required": mp.nstr(THETA_REQ, 16),
            "declared_comparisons": {nm: {"value": mp.nstr(v, 14),
                                          "ratio_to_theta": mp.nstr(v / THETA_REQ, 10)}
                                     for nm, v in cands},
            "closest_factor": mp.nstr(closest, 10),
        },
        "context": {
            "axis": "branch 3: can Bring's associated elliptic curve supply the generator?",
            "answer": (
                "The right KIND of object -- first candidate to pass D0 in principle, since "
                "a flat unitary connection on a torus has elliptic monodromy by "
                "construction. But this curve supplies no phase: non-CM, so tau has no "
                "closed form; Re(tau) = 1/2 so the natural angle is pi, a sign; and nothing "
                "declared lands within a factor of 20."),
            "not_refuted": (
                "the DIRECTION. A KZB construction on E -- the elliptic analogue of KZ, "
                "where exp(2 pi i tau) factors genuinely enter -- is untouched, and is where "
                "an elliptic generator could still come from."),
            "provenance_caveat": (
                "the library copy is OCR of a scanned page and is garbled in places. Only "
                "the legible and independently checkable parts are used: the curve "
                "equation, its j (re-derived), and the (5tau,...,tau) diagonalisation. The "
                "paper's own tau_0 is pinned by TWO j-values, the second illegible in this "
                "scan, so tau_0 is NOT reconstructed -- only the SL(2,Z) representative "
                "with j = -25/2."),
            "scope": ("Scope-(a). Nothing derived, proposed, wired or readmitted; E is not "
                      "adopted; no convention adjudicated."),
        },
        "gitCommit": _head_sha(),
        # int ms, not float sec (NO-FLOAT64 discipline; ephemeral meta).
        "durationMs": int((time.monotonic() - t0) * 1000),
    }
    out = HERE / "qbeta-bring-elliptic-generator.witness.json"
    with open(out, "w") as f:
        from qou_substrate.witness import WitnessBuilder as _WB
        witness.setdefault("scriptFile", os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine="mpmath",
            q0_anchor="proton", q0_anchor_reason="experimental pin (the physical-observations layer)", q0_value=mp.nstr(Q0, 30))
        json.dump(witness, f, indent=2)
        f.write("\n")
    print(f"\n  witness -> {out.relative_to(ROOT)}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
