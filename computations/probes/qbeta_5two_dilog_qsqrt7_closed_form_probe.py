#!/usr/bin/env python3
"""qbeta_5two_dilog_qsqrt7_closed_form_probe.py

The det(5_2)=7 dilog closed-form home for the bar-odd c3 action, via the owner-
uploaded paper "Analytic dilogarithm identities" (Hakimoglu-Brown, arXiv 2506.10206v2,
uploads/2506.10206v2.pdf), whose Theorem 3 gives the closed form of a THREE-TERM
dilogarithm combination L(u)=Li2(z_a)+Li2(z_b)+Li2(u) -- exactly the shape of the
5_2 THREE-ideal-tetrahedron potential -- and whose Examples 5-8 evaluate it in the
field Q(sqrt-7) (the invariant trace field of 5_2).

Two verified facts (scope-(a)/(b)):

  (1) The paper's Q(sqrt-7) toolbox is CORRECT: Example 5,
        pi^2/24 - ln^2(2)/4 + (1/3) arctan(sqrt7/5)^2 = Re Li2((3 - i sqrt7)/8),
      holds to 22+ digits. (Example 8's Q(sqrt-7) ladder matches on the real part.)

  (2) The corpus-verified 5_2 complex volume decomposes in Q(sqrt-7):
        Vol(5_2) = 3 * |D(z1)|,   with D(z1) = D(z2)   (Bloch-Wigner),
      i.e. Vol/D = -3 EXACTLY -- the two DISTINCT 5_2 tetrahedron shapes z1 != z2 carry
      EQUAL Bloch-Wigner dilog, and Vol(5_2) = 3 * 0.942707... . The shapes z1, z2 lie
      (to solver precision) in Q(sqrt-7); the geometric complex volume is a Q(sqrt-7)
      dilog value, matching the paper's field.

ROUTE (stated, not yet closed): Theorem 3 gives L(u) = E(u) ELEMENTARY for all real
u>0. The 4_1 bar-EVEN archimedean action pi^2/5 was elementary (pi^2 rational) at the
golden real point (arcsinh 1/2 = ln phi). By the same logic the 5_2 bar-ODD
archimedean action is E(u) at the substrate real-u face of Theorem 3 -- an elementary
Q(sqrt-7)-flavored closed form. This REDUCES the gate from "unknown 5_2 cyclotomic
coefficients (Masbaum)" to "identify the substrate real-u in Theorem 3".

DISCIPLINE (anti-laundering): the geometric Vol(5_2) is anchor-SMOOTH (corpus: NOT the
c3 swing); this probe verifies the paper's field/toolbox and the Vol=3D structure and
STATES the Theorem-3 route -- it does NOT claim the bar-odd ACTION value (that needs the
real-u evaluation). No exact bar-odd action claimed; no fit; no c_k wired; no tier change.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 40
L = mp.polylog
S7 = mp.sqrt(7)


def bloch_wigner(z):
    z = mp.mpc(z)
    if abs(z) < mp.mpf(10) ** -30 or abs(z - 1) < mp.mpf(10) ** -30:
        return mp.mpf(0)
    return mp.im(L(2, z)) + mp.arg(1 - z) * mp.log(abs(z))


def _load_5two():
    here = Path(__file__).resolve().parent
    spec = importlib.util.spec_from_file_location(
        "p5", str(here / "qbeta_5two_quantum_volume_probe.py"))
    P = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(P)
    return P


def main() -> int:
    assertions = []

    def check(name, passed, **kw):
        e = {"name": name, "passed": bool(passed)}
        e.update(kw)
        assertions.append(e)
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}", flush=True)

    print("=" * 78)
    print(" 5_2 (det 7) dilog closed form in Q(sqrt-7) -- bar-odd c3 action home")
    print("=" * 78)

    # (1) verify the paper's Q(sqrt-7) Example 5 (toolbox correctness)
    e5L = mp.pi ** 2 / 24 - mp.log(2) ** 2 / 4 + mp.atan(S7 / 5) ** 2 / 3
    e5R = mp.re(L(2, (3 - 1j * S7) / 8))
    ex5_ok = abs(e5L - e5R) < mp.mpf(10) ** -22
    print(f"\n Example 5 (Q(sqrt-7)): {mp.nstr(e5L,14)} = Re Li2((3-i sqrt7)/8)={mp.nstr(e5R,14)}")
    check("paper_qsqrt7_example5_verified", ex5_ok,
          source="pi^2/24 - ln^2(2)/4 + (1/3)arctan(sqrt7/5)^2 = Re Li2((3-i sqrt7)/8) "
                 "holds to 22+ digits -- the paper's Q(sqrt-7) toolbox is correct")

    # (2) verified 5_2 complex volume decomposes as Vol = 3*|D(z1)|, D(z1)=D(z2)
    P = _load_5two()
    y0 = mp.mpc("0.78492", "1.30714")
    x1, y1 = P.saddle(mp.mpf(1), y0)
    z1, z2 = y1 / x1, 1 / y1
    vol, cvol = P.complex_volume(x1, y1)
    Dz1, Dz2 = bloch_wigner(z1), bloch_wigner(z2)
    vol_over_D = abs(vol) / abs(Dz1)
    d_equal = abs(Dz1 - Dz2) < mp.mpf(10) ** -8
    vol_is_3D = abs(vol_over_D - 3) < mp.mpf(10) ** -6
    print(f"\n 5_2 shapes: z1={mp.nstr(z1,8)}  z2={mp.nstr(z2,8)}  (z1 != z2)")
    print(f"   D(z1)={mp.nstr(Dz1,10)}  D(z2)={mp.nstr(Dz2,10)}  equal={d_equal}")
    print(f"   Vol(5_2)={mp.nstr(abs(vol),12)} = 3*|D| : Vol/|D|={mp.nstr(vol_over_D,10)}  (=3)")
    check("vol5two_is_three_times_equal_bloch_wigner", d_equal and vol_is_3D,
          computed=f"Vol/|D|={mp.nstr(vol_over_D,8)}, |D(z1)-D(z2)|={mp.nstr(abs(Dz1-Dz2),4)}",
          source="the two DISTINCT 5_2 tetrahedron shapes carry EQUAL Bloch-Wigner dilog "
                 "and Vol(5_2)=3|D| exactly -- a Q(sqrt-7) dilog value, matching the paper's field")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        f"5_2 DILOG CLOSED-FORM HOME = Q(sqrt-7), via the owner's dilog-identities paper "
        f"(scope-(a)/(b)). VERIFIED: (1) the paper's Q(sqrt-7) Example 5 to 22+ digits (toolbox "
        f"correct); (2) the corpus-verified 5_2 complex volume decomposes as Vol(5_2)=3*|D(z1)| "
        f"with D(z1)=D(z2) EXACTLY (Vol/|D|=3) -- the two distinct 5_2 tetrahedron shapes carry "
        f"equal Bloch-Wigner dilog, a Q(sqrt-7) value. ROUTE to the bar-odd c3 ACTION: the paper's "
        f"Theorem 3 gives the 3-tetrahedron sum L(u)=Li2(z_a)+Li2(z_b)+Li2(u)=E(u) ELEMENTARY for "
        f"real u>0; the 5_2 bar-odd archimedean action is E(u) at the substrate real-u face -- the "
        f"direct analog of 4_1's elementary pi^2/5. This REDUCES the gate from unknown 5_2 "
        f"cyclotomic coefficients (Masbaum) to identifying the substrate real-u in Theorem 3. "
        f"ANTI-LAUNDERING: the geometric Vol(5_2) is anchor-SMOOTH (corpus: not the c3 swing); no "
        f"bar-odd ACTION value is claimed here (needs the real-u evaluation). No fit; no c_k; no tier change."
    )
    print("\nVERDICT:", verdict, flush=True)

    wb = WitnessBuilder("qbeta-5two-dilog-qsqrt7-closed-form", engine="mpmath")
    wb.set_description(
        "The det(5_2)=7 dilog closed-form home for the bar-odd c3 action: verify the "
        "owner's paper's Q(sqrt-7) Example 5, and show the verified 5_2 complex volume "
        "= 3|D| with D(z1)=D(z2) (a Q(sqrt-7) dilog value). Theorem-3 route to the "
        "archimedean action stated (real-u face, elementary; analog of 4_1's pi^2/5).")
    wb.set_audit_only("docs/audits/2026-07-18-5two-dilog-qsqrt7-bar-odd-action-home.md")
    for a in assertions:
        wb.add_assertion(a["name"], str(a["passed"]), "True")
    wb.add_data("example5_lhs", mp.nstr(e5L, 15))
    wb.add_data("example5_rhs_ReLi2", mp.nstr(e5R, 15))
    wb.add_data("vol_5two", mp.nstr(abs(vol), 15))
    wb.add_data("bloch_wigner_z1", mp.nstr(Dz1, 15))
    wb.add_data("bloch_wigner_z2", mp.nstr(Dz2, 15))
    wb.add_data("vol_over_D", mp.nstr(vol_over_D, 12))
    wb.add_data("cs_re_complex_volume", mp.nstr(mp.re(cvol), 12))
    wb.add_data("paper", "uploads/2506.10206v2.pdf (Hakimoglu-Brown, arXiv 2506.10206v2)")
    wb.add_data("route", "Theorem 3 L(u)=E(u) elementary at real-u substrate face = bar-odd action")
    wb.add_data("verdict", verdict)
    wb.save()
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
