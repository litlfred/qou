#!/usr/bin/env python3
"""qbeta_5two_phi_odd_oneloop_vanishing_probe.py

Different-context attack on phi_odd (the intrinsic bar-odd datum of the 5_2 substrate
saddle-pair; sibling classical-strip extraction gives phi_odd_arg_sum = -0.004145,
mag_odd_ratio-1 = 0.0864 via the certified 2-loop (238) strip). This probe computes
the CLASSICAL (1-loop, saddle-point) bar-odd phase independently from the verified
5_2 quantum-volume saddle machinery + the 1-loop Hessian delta -- no exact-Z solve,
no (238) input.

STRUCTURAL RESULT: the substrate has three saddles -- a real saddle sigma_3
(Re V = 6.91, arg(a) = -pi/4, exponentially absent from the ray contour) and a
CONJUGATE PAIR sigma_1/sigma_2 (Re V = 1.815, Im V = +/-2.293) that co-dominates the
ray tau = it/2pi. For that conjugate pair, the classical amplitude a_sigma = 1/sqrt(i*delta_sigma)
has

    arg(a_1) + arg(a_2) = -pi/2   AND   arg(b_1) + arg(b_2) = -pi/2   (bar image),

so the CLASSICAL bar-odd arg-sum phase is EXACTLY ZERO. Therefore the sibling's
phi_odd = -0.004145 is generated ENTIRELY by the SUB-LEADING quantum amplitude (the
2-loop (238) correction) -- the classical geometric saddle data (V, delta) carries NO
bar-odd datum, by conjugate symmetry.

INSIGHT (why this matters): this is the MECHANISM behind the corpus's repeated
"geometric routes are anchor-smooth / null" findings (5_2 quantum volume anchor-smooth,
classical CS anchor-invariant, branch-point locus generic). The bar-odd datum is
intrinsically QUANTUM / 2-loop -- invisible to the classical volume/Hessian by the
sigma_1/sigma_2 conjugate symmetry -- which independently confirms that the sibling's
certified 2-loop strip is ESSENTIAL, not optional.

DISCIPLINE: scope-(a)/(b). (b): the 1-loop pair arg-sum is EXACTLY -pi/2 (conjugate
symmetry, a proved cancellation), so the classical bar-odd phase is 0. Does NOT compute
phi_odd's value (that is the 2-loop amplitude, sibling-owned). No fit; no c_k wired; no
tier change.
"""
from __future__ import annotations

import importlib.util
import itertools
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()


def _load_5two():
    here = Path(__file__).resolve().parent
    spec = importlib.util.spec_from_file_location(
        "p5", str(here / "qbeta_5two_quantum_volume_probe.py"))
    P = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(P)
    return P


def delta(x, y):
    return y - (1 + x + 1 / x) / y + 2 / y ** 2


def saddles(m):
    m2 = m * m
    A = [m2, -(m2 + 1), mp.mpf(1)]
    B = [-mp.mpf(1), m2]
    C = [mp.mpf(0)] * 4
    for i, a in enumerate(A):
        for j, b in enumerate(B):
            C[i + j] += a * b
    C[2] += -m2
    r = mp.polyroots(C, maxsteps=300, extraprec=150)
    return [(y / (m2 - y), y) for y in r]


def main() -> int:
    assertions = []

    def check(name, passed, **kw):
        e = {"name": name, "passed": bool(passed)}
        e.update(kw)
        assertions.append(e)
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}", flush=True)

    P = _load_5two()
    q0 = q_at(45)
    S, Sb = saddles(q0), saddles(1 / q0)

    def pack(saddle_list):
        out = []
        for x, y in saddle_list:
            _, cv = P.complex_volume(x, y)
            a = 1 / mp.sqrt(1j * delta(x, y))
            out.append({"ReV": mp.re(cv), "ImV": mp.im(cv), "amp": a})
        return out

    dat, datb = pack(S), pack(Sb)
    print("\n substrate saddles (m=q0):", flush=True)
    for d in dat:
        print(f"   ReV={mp.nstr(d['ReV'],7)}  ImV={mp.nstr(d['ImV'],7)}  "
              f"|a|={mp.nstr(abs(d['amp']),7)}  arg(a)={mp.nstr(mp.arg(d['amp']),7)}", flush=True)

    # identify the conjugate pair: two saddles with equal ReV and opposite ImV
    pair = None
    for i, j in itertools.combinations(range(3), 2):
        if abs(dat[i]["ReV"] - dat[j]["ReV"]) < mp.mpf("1e-20") and \
           abs(dat[i]["ImV"] + dat[j]["ImV"]) < mp.mpf("1e-20"):
            pair = (i, j)
    print(f"\n conjugate co-dominant pair (equal ReV, opposite ImV): sigma indices {pair}", flush=True)
    check("conjugate_pair_identified", pair is not None,
          source="two of the three 5_2 substrate saddles form a conjugate pair "
                 "(equal Re V=1.815, Im V=+/-2.293) -- the ray-co-dominant sigma_1/sigma_2")

    i, j = pair
    argsum_a = mp.arg(dat[i]["amp"]) + mp.arg(dat[j]["amp"])
    argsum_b = mp.arg(datb[i]["amp"]) + mp.arg(datb[j]["amp"])
    oneloop_phi_odd = argsum_a - argsum_b
    print(f"\n classical (1-loop) pair arg-sum: a-image={mp.nstr(argsum_a,12)}  "
          f"bar-image={mp.nstr(argsum_b,12)}  (both = -pi/2 = {mp.nstr(-mp.pi/2,10)})", flush=True)
    print(f" => classical bar-odd phase phi_odd(1-loop) = {mp.nstr(oneloop_phi_odd,10)} "
          f"(target 2-loop value -0.004145)", flush=True)
    argsum_is_minus_half_pi = abs(argsum_a - (-mp.pi / 2)) < mp.mpf("1e-20") and \
        abs(argsum_b - (-mp.pi / 2)) < mp.mpf("1e-20")
    oneloop_vanishes = abs(oneloop_phi_odd) < mp.mpf("1e-20")
    check("classical_pair_argsum_is_minus_half_pi", argsum_is_minus_half_pi,
          computed=f"arg-sum(a)={mp.nstr(argsum_a,10)}, arg-sum(b)={mp.nstr(argsum_b,10)}",
          source="the conjugate pair's classical amplitude arg-sum is EXACTLY -pi/2 for "
                 "both the pair and its bar image (conjugate symmetry of 1/sqrt(i*delta))")
    check("classical_bar_odd_phase_vanishes", oneloop_vanishes,
          computed=f"phi_odd(1-loop)={mp.nstr(oneloop_phi_odd,6)}",
          source="the classical (1-loop) bar-odd arg-sum phase is EXACTLY 0 -- so the sibling "
                 "phi_odd=-0.004145 is generated ENTIRELY by the sub-leading (2-loop) amplitude")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        f"phi_odd IS A PURELY 2-LOOP DATUM -- the classical bar-odd phase VANISHES (scope-(a)/(b) "
        f"insight, independent of the sibling GGM strip). The 5_2 substrate has a real saddle "
        f"(Re V=6.91, arg a=-pi/4, ray-absent) plus a CONJUGATE PAIR sigma_1/sigma_2 (Re V=1.815, "
        f"Im V=+/-2.293). For that pair the classical amplitude 1/sqrt(i*delta) has arg-sum EXACTLY "
        f"-pi/2 for BOTH the pair and its bar image, so the classical (1-loop) bar-odd phase is "
        f"EXACTLY 0. Therefore the sibling's phi_odd=-0.004145 is generated ENTIRELY by the "
        f"sub-leading QUANTUM amplitude (the certified 2-loop (238) correction) -- the classical "
        f"geometric saddle data (V, delta) carries NO bar-odd datum, by conjugate symmetry. This is "
        f"the MECHANISM behind the corpus's 'geometric routes are anchor-smooth/null' findings: the "
        f"bar-odd datum is intrinsically quantum/2-loop, invisible to the classical volume/Hessian. "
        f"Independently confirms the sibling 2-loop strip is essential, not optional. No fit; no c_k; "
        f"no tier change."
    )
    print("\nVERDICT:", verdict, flush=True)

    wb = WitnessBuilder("qbeta-5two-phi-odd-oneloop-vanishing", engine="mpmath")
    wb.set_description(
        "Independent (classical saddle) attack on phi_odd: the 5_2 substrate conjugate pair "
        "sigma_1/sigma_2 has classical amplitude arg-sum EXACTLY -pi/2 for both the pair and its "
        "bar image, so the 1-loop bar-odd phase VANISHES -- phi_odd=-0.004145 is a purely 2-loop "
        "datum. The mechanism behind the geometric-route anchor-smooth nulls.")
    wb.set_audit_only("docs/audits/2026-07-18-5two-phi-odd-purely-2loop.md")
    for a in assertions:
        wb.add_assertion(a["name"], str(a["passed"]), "True")
    wb.add_data("saddle_ReV", [mp.nstr(d["ReV"], 10) for d in dat])
    wb.add_data("saddle_ImV", [mp.nstr(d["ImV"], 10) for d in dat])
    wb.add_data("conjugate_pair_indices", list(pair))
    wb.add_data("classical_pair_argsum_a", mp.nstr(argsum_a, 15))
    wb.add_data("classical_pair_argsum_b", mp.nstr(argsum_b, 15))
    wb.add_data("classical_phi_odd_1loop", mp.nstr(oneloop_phi_odd, 12))
    wb.add_data("target_phi_odd_2loop", "-0.004144702346")
    wb.add_data("verdict", verdict)
    wb.save()
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
