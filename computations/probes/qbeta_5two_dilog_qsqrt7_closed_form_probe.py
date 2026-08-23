#!/usr/bin/env python3
"""qbeta_5two_dilog_qsqrt7_closed_form_probe.py

*** PREMISE RETRACTED 2026-08-11 -- READ THIS FIRST ***

This file's docstring below calls Q(sqrt-7) "the invariant trace field of 5_2".
That is WRONG. 5_2's invariant trace field is the CUBIC field of discriminant
-23, and Q(sqrt-7) cannot embed in it: [Q(sqrt-7):Q] = 2 does not divide
[K:Q] = 3, so the tower law forbids it outright -- a scope-(b) structural
exclusion, not a numerical near-miss.

Q(sqrt-7) IS attached to 5_2, but as the ALEXANDER layer: Delta(t) = 2t^2-3t+2
has disc -7 and det(5_2) = |Delta(-1)| = 7, so it is the quadratic subfield of
Q(zeta_7) where the Z/7 branched cover's metabelian data lives. Reading the
GEOMETRIC trace field off that ABELIAN datum is the error. The quadratic field
actually attached to K is Q(sqrt-23) -- the A_3-fixed subfield of the S_3
Galois closure, which is the line the corpus's own A6 sigma-pair tower records.

WHAT THIS PROBE STILL ESTABLISHES, unchanged:

  (1) The Hakimoglu-Brown paper's Q(sqrt-7) Example 5 identity is correct. That
      is a fact about the PAPER, which is a pure beta-integral/special-functions
      paper containing no occurrence of "knot", "hyperbolic", "volume" or
      "trace field". It never claimed a 5_2 connection; the inference was ours.

  (2) Vol(5_2) = 3*|D(z1)| with D(z1) = D(z2). Correct, but FORCED, not a
      discovery: at m=1 the gluing equation gives z2 = 1/(1-z1), a standard
      six-fold Bloch-Wigner partner for which D(z2) = D(z1) is the textbook
      identity. It carries no field information either way.

No action VALUE was claimed here and none is retracted -- the DISCIPLINE note at
the end of the original docstring was correct. What is retracted is the FIELD.

Certification: qbeta_5two_trace_field_disc23_not_qsqrt7.py (5 assertions)
Correction:    docs/audits/2026-08-11-5two-trace-field-is-disc-minus-23.md
Bean:          qou-ynff

--- ORIGINAL DOCSTRING FOLLOWS (retained; its field claims are superseded) ---

The det(5_2)=7 dilog closed-form home for the bar-odd c3 action, via the owner-
uploaded paper "Analytic dilogarithm identities" (Hakimoglu-Brown, arXiv 2506.10206v2,
library/arxiv-2506.10206v2/2506.10206v2.pdf), whose Theorem 3 gives the closed form of a THREE-TERM
dilogarithm combination L(u)=Li2(z_a)+Li2(z_b)+Li2(u) -- exactly the shape of the
5_2 THREE-ideal-tetrahedron potential -- and whose Examples 5-8 evaluate it in the
field Q(sqrt-7) (WRONG: not the invariant trace field of 5_2 -- see the
retraction at the top of this docstring; K is the cubic of disc -23).

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
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
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
                 "and Vol(5_2)=3|D| exactly. NOTE (2026-08-11): both facts hold, but neither "
                 "carries field information -- at m=1 the gluing equation gives z2 = 1/(1-z1), a "
                 "six-fold Bloch-Wigner partner for which D(z2)=D(z1) is the textbook identity, so "
                 "Vol=3|D| is FORCED. The original 'a Q(sqrt-7) value, matching the paper's field' "
                 "gloss is RETRACTED: the trace field is the cubic of disc -23 (qou-ynff)")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        f"PREMISE RETRACTED 2026-08-11 (qou-ynff): this probe was written as '5_2 dilog "
        f"closed-form home = Q(sqrt-7)'. 5_2's invariant trace field is the CUBIC of "
        f"discriminant -23; Q(sqrt-7) cannot embed in it ([Q(sqrt-7):Q]=2 does not divide "
        f"[K:Q]=3, tower law -- a scope-(b) structural exclusion). Q(sqrt-7) is 5_2's "
        f"ALEXANDER layer (disc(2t^2-3t+2) = -7, det = 7), not its geometric one. See "
        f"qbeta_5two_trace_field_disc23_not_qsqrt7.py. WHAT THIS PROBE STILL SHOWS, unchanged: "
        f"(1) the paper's Q(sqrt-7) Example 5 to 22+ digits (toolbox "
        f"correct); (2) the corpus-verified 5_2 complex volume decomposes as Vol(5_2)=3*|D(z1)| "
        f"with D(z1)=D(z2) EXACTLY (Vol/|D|=3) -- the two distinct 5_2 tetrahedron shapes carry "
        f"equal Bloch-Wigner dilog -- though this is FORCED by z2 = 1/(1-z1) and carries no field "
        f"information. The ROUTE stated below is likewise NOT established: it was argued by solving "
        f"L(u) = Li2(z1)+2Li2(z2) numerically for u -- one equation in one unknown in an analytic "
        f"function -- and matching a sum's VALUE is not matching the TRIPLE. Original text follows: "
        f"the paper's "
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
        "PREMISE RETRACTED 2026-08-11 (qou-ynff): titled as the 'Q(sqrt-7) home' for the "
        "bar-odd c3 action, but 5_2's trace field is the cubic of disc -23 and Q(sqrt-7) "
        "cannot embed in it (tower law). Q(sqrt-7) is the Alexander layer. What survives: "
        "the paper's Q(sqrt-7) Example 5 verifies (a fact about the PAPER, which never "
        "claimed a 5_2 connection), and Vol(5_2)=3|D| holds but is forced by z2=1/(1-z1) "
        "and carries no field information. No action VALUE was claimed or is retracted.")
    wb.set_audit_only("docs/audits/2026-08-11-5two-trace-field-is-disc-minus-23.md")
    for a in assertions:
        wb.add_assertion(a["name"], str(a["passed"]), "True")
    wb.add_data("example5_lhs", mp.nstr(e5L, 15))
    wb.add_data("example5_rhs_ReLi2", mp.nstr(e5R, 15))
    wb.add_data("vol_5two", mp.nstr(abs(vol), 15))
    wb.add_data("bloch_wigner_z1", mp.nstr(Dz1, 15))
    wb.add_data("bloch_wigner_z2", mp.nstr(Dz2, 15))
    wb.add_data("vol_over_D", mp.nstr(vol_over_D, 12))
    wb.add_data("cs_re_complex_volume", mp.nstr(mp.re(cvol), 12))
    wb.add_data("paper", "library/arxiv-2506.10206v2/2506.10206v2.pdf (Hakimoglu-Brown, arXiv 2506.10206v2)")
    wb.add_data("route", "Theorem 3 L(u)=E(u) elementary at real-u substrate face = bar-odd action")
    wb.add_data("verdict", verdict)
    wb.save()
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
