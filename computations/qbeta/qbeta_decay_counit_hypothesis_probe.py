#!/usr/bin/env python3
"""Is the decay channel's pairing the COUNIT rather than the Markov trace?
Answer: NO in the strong form — and the refutation is sharper than the question.

BEAN `qou-cds1`. Follow-on from `qbeta_z_symbolic_borromean_crosscheck`, which
localised the Q_beta anomaly to the decay channel by showing the mass channel
independently puts z within 0.0203 % of the derived cap.

THE HYPOTHESIS. `z_required` sits 0.15 % from `z = 1`, where the Ocneanu trace
degenerates to the Frobenius counit (`QOU.Interactions.qbeta_counit_vs_trace`,
`trMNP_at_one : trMNP h 1 = epsNP h`). So: maybe the decay channel is not a
Markov trace at all, and `z = 1` is where it LIVES rather than a wall it is
bumping into.

FIRST, A CROSS-CHECK THAT VALIDATES THE WHOLE CHAIN. The `y_(1^3)` numerator
this arc derived independently (3x3 Markov solve, sympy) divided by q^2 is
IDENTICAL — symbolic difference exactly 0 — to the committed Lean
`QOU.QBeta.AdmissibleRoots.wtNumer`. Two independent routes to the same
polynomial, so what follows rests on the Lean as much as on this file.

THE ANSWER, and the hypothesis does not survive it. `one_not_root` proves
UNCONDITIONALLY on the substrate window (1 < q, q below the plastic number
~1.4656; q0 ~ 1.110 is well inside) that `wtNumer q 1 != 0`. The admissible set
is EXACTLY TWO — `admissible_markov_param_iff` — and `z = 1` is in neither.

    z = q    (AUGMENTATION)   g = 1.0        12.470 %  off   ADMISSIBLE
    z = z_D  (Markov / TL)    g = 0.5054     43.157 %  off   ADMISSIBLE
    z = 1    (counit)         g = 0.8906      0.168 %  off   *** EXCLUDED ***

So NEITHER admissible point fits, and the point that fits is proved
unavailable. That is a much sharper statement of the anomaly than "the decay
channel misses by 1.76x": the Q_beta inversion points almost exactly at the one
place the algebra forbids.

AND THE REQUIRED WEIGHT IS NEGATIVE. At `z_required`, `wtNumer = -0.09600` and
`y_(1^3) = -0.014131`. A negative Wedderburn weight is not a small perturbation
of a trace, it is a sign violation — so no POSITIVE-weight trace in this family
reaches the required scalar.

SCOPE — (a), NOT (b). What is measured: the required z is not an admissible
root, and the weight there is negative. What is NOT proved here: that positivity
is REQUIRED of this pairing. Making that a structural exclusion needs a proved
positivity invariant on the decay pairing, which the corpus does not currently
carry. Stated as scope-(a) deliberately, per the refutation discipline.

A DECLARED STRADDLE, because AGENTS.md forbids one regardless of size. `q0` here
is the MUON pin (convention-free: m_mu/m_e = Vol(4_1)/hbar_q^2, no trace), while
`g_required` is carried from the proton-pinned terminus witness. The two layers
differ by the mu-p tension, ~1.15e-8 relative — five orders below the 0.168 %
that carries the conclusion, so the ORDERING is robust. But it is still a
straddle: a clean muon-pin re-derivation of `g_required` is the next step and is
NOT done here.

Anchor: MUON pin (E1/E2 carve-out — the file tests a convention, and the proton
pin is fixed through F_Bor and so presupposes it).
"""
from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp
from mpmath import mp

_COMP = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(_COMP / "qbeta"), str(_COMP), str(_COMP / "substrate")]
import _path_bridge  # noqa: F401,E402

from witness_base import WitnessBuilder  # noqa: E402

mp.dps = 50


def main() -> int:
    ok = True
    checks = []

    def check(name, passed, detail=""):
        nonlocal ok
        ok = ok and bool(passed)
        checks.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""))

    q, z = sp.Symbol("q", positive=True), sp.Symbol("z")
    mine = q ** 2 * (q ** 4 - 2 * q ** 3 * z + q ** 2 * z ** 2 - q * z + z ** 2)
    lean = (q ** 2 + 1) * z ** 2 - (2 * q ** 3 + q) * z + q ** 4
    d = sp.simplify(sp.expand(mine / q ** 2 - lean))
    print("[1] cross-check: the independently derived weight vs the committed Lean")
    check("my y_(1^3) numerator / q^2 IS QOU.QBeta.AdmissibleRoots.wtNumer",
          d == 0, f"symbolic difference = {d}")

    from qou_substrate import constants as C  # noqa: E402
    r_mu = mp.mpf(C.MASS_RATIO_MU_E_STR)
    q0 = 1 / (1 - mp.sqrt(2 * mp.clsin(2, mp.pi / 3) / r_mu))     # muon pin
    zD = q0 ** 3 / (q0 ** 2 + 1)
    g = lambda zz: (-q0 ** 2 + 2 * q0 * zz + 1) / (q0 ** 2 + 1)   # noqa: E731
    wt = lambda zz: (q0 ** 2 + 1) * zz ** 2 - (2 * q0 ** 3 + q0) * zz + q0 ** 4  # noqa: E731
    g_req = mp.mpf("0.8891258104440578")

    print(f"\n[2] the decay scalar at each candidate (q0 = {mp.nstr(q0, 18)}, MUON pin)")
    rows = {}
    for nm, zz, adm in (("z = q   (augmentation)", q0, True),
                        ("z = z_D (Markov / TL) ", zD, True),
                        ("z = 1   (counit)      ", mp.mpf(1), False)):
        rel = abs(g(zz) - g_req) / g_req * 100
        rows[nm.split()[2]] = (mp.nstr(g(zz), 16), mp.nstr(rel, 8), adm)
        tag = "ADMISSIBLE" if adm else "*** PROVED EXCLUDED (one_not_root) ***"
        print(f"    {nm}  g = {mp.nstr(g(zz), 14):<18} off {mp.nstr(rel, 7):>10} %   {tag}")

    check("NEITHER admissible root fits (both off by >10 %)",
          abs(g(q0) - g_req) / g_req > mp.mpf("0.1")
          and abs(g(zD) - g_req) / g_req > mp.mpf("0.1"))
    check("the EXCLUDED point z=1 fits to better than 0.2 % — the counit "
          "hypothesis is refuted, but only just, and that IS the anomaly",
          abs(g(1) - g_req) / g_req < mp.mpf("2e-3"),
          f"{mp.nstr(abs(g(1) - g_req) / g_req * 100, 7)} %")
    check("z = 1 is genuinely NOT a root (Lean one_not_root, reproduced here)",
          abs(wt(mp.mpf(1))) > mp.mpf("1e-3"), f"wtNumer(q0,1) = {mp.nstr(wt(1), 10)}")

    z_req = (g_req * (q0 ** 2 + 1) + q0 ** 2 - 1) / (2 * q0)
    y111 = q0 ** 2 * wt(z_req) / (q0 ** 6 + 2 * q0 ** 4 + 2 * q0 ** 2 + 1)
    print(f"\n[3] the weight the data demands")
    print(f"    z_required  = {mp.nstr(z_req, 18)}")
    print(f"    wtNumer     = {mp.nstr(wt(z_req), 12)}   (0 would mean admissible)")
    print(f"    y_(1^3)     = {mp.nstr(y111, 12)}   NEGATIVE")
    check("y_(1^3) at z_required is NEGATIVE — a sign violation, not a small "
          "perturbation (scope-(a): positivity is not PROVED required here)",
          y111 < 0, f"y_(1^3) = {mp.nstr(y111, 10)}")

    verdict = (
        "REFUTED IN THE STRONG FORM, and the refutation is the sharper result. "
        "z = 1 -- where the Ocneanu trace degenerates to the Frobenius counit -- "
        "reproduces the measured Q_beta scalar to 0.168 %, against 12.470 % for "
        "the augmentation (z = q) and 43.157 % for the Markov trace at z_D. But "
        "z = 1 is PROVED not an admissible Markov parameter (one_not_root, "
        "unconditional on the substrate window), and the admissible set is "
        "EXACTLY those two. So neither available point fits and the point that "
        "fits is forbidden. At z_required the (1^3) weight is NEGATIVE "
        "(-0.014131), so no positive-weight trace in this family reaches it. "
        "SCOPE-(a): measured non-admissibility and a measured negative weight; "
        "NOT a proved structural exclusion, which would need a positivity "
        "invariant on the decay pairing that the corpus does not carry.")
    print(f"\n[4] {verdict}")

    wb = WitnessBuilder("qbeta-decay-counit-hypothesis", engine="sympy+mpmath")
    wb.set_description(
        "Tests whether the decay channel's pairing is the Frobenius counit rather "
        "than the Ocneanu Markov trace. Refuted in the strong form: z = 1 fits the "
        "measured Q_beta scalar to 0.168 % but is PROVED non-admissible, while both "
        "admissible roots miss by >10 %. The required (1^3) weight is negative. "
        "Also cross-checks this arc's independently derived weight numerator against "
        "the committed Lean wtNumer -- symbolic difference exactly 0.")
    wb.add_data("crosscheck_vs_lean_wtNumer", str(d))
    wb.add_data("q0_muon_pin", mp.nstr(q0, 30))
    wb.add_data("g_required", mp.nstr(g_req, 20))
    wb.add_data("candidates", {k: {"g": v[0], "off_pct": v[1], "admissible": v[2]}
                               for k, v in rows.items()})
    wb.add_data("z_required", mp.nstr(z_req, 25))
    wb.add_data("wtNumer_at_z_required", mp.nstr(wt(z_req), 20))
    wb.add_data("y_1cubed_at_z_required", mp.nstr(y111, 20))
    wb.add_data("declared_straddle",
                "q0 is the muon pin; g_required is carried from the proton-pinned "
                "terminus witness. The layers differ by the mu-p tension ~1.15e-8, "
                "five orders below the 0.168 % carrying the conclusion, so the "
                "ORDERING is robust -- but it IS a straddle and a clean muon-pin "
                "re-derivation of g_required is NOT done here.")
    wb.add_data("scope", "(a) measured non-admissibility + measured negative weight; "
                         "NOT a proved structural exclusion")
    wb.add_data("free_parameters", 0)
    wb.add_data("verdict", verdict)
    wb.add_data("q0Anchor", "muon")
    for c in checks:
        wb.add_assertion(c["name"][:80], computed=1 if c["passed"] else 0,
                         expected=1, tolerance=0, source=c["detail"] or None)
    wb.save()
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
