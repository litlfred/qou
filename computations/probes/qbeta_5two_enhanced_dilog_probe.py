#!/usr/bin/env python3
"""Is the 5₂ saddle sum rule a statement about Zagier's ENHANCED dilogarithm?

Lead
----
Zagier, *The Dilogarithm Function* (2007), §II.1 B (`library/zagier-the-dilogarithm-function/zagier-the-dilogarithm-function.pdf`):
the **enhanced dilogarithm** is

    D̃(ẑ) = F(v) + u·v/2,     F(v) = Li₂(1 − e^v),

on the abelian cover ``X̃ = {(u,v) ∈ ℂ² : e^u + e^v = 1}`` of
``P¹(ℂ) ∖ {0,1,∞}``.  Writing ``z = e^u = 1 − e^v``, that is

    D̃ = Li₂(z) + ½·log(z)·log(1−z)      with SPECIFIED branches u, v,

and it takes values in ``ℂ/(π²/2)ℤ`` — it is well defined only modulo
``π²/2``, and only on Bloch-group combinations, not on individual arguments.

Three facts make this look like our object:

1. The sum rule's summand ``Vⱼ = 3·Li₂(yⱼ) + Log(−yⱼ)²`` has the shape
   ``Li₂ + (log)(log)`` — with branch data, which is exactly what ``X̃`` tracks.
2. The roots satisfy ``y² = (1−y)³``, i.e. ``2u = 3v + 2πi·k`` with
   ``k = (1,−1,0)`` (measured in `qbeta_5two_route5_branch_data_probe`, G4).
   On that locus ``½uv`` collapses to a multiple of ``u²`` plus a ``πi·k·u``
   term — so ``3·D̃`` is ``3Li₂ + u² + (branch term)``, matching ``V``'s shape.
3. The sum rule's value is ``−3π²/2 = −3·(π²/2)`` — an exact multiple of the
   enhanced dilogarithm's ambiguity ``π²/2``.

If ``Σⱼ Vⱼ`` really is ``3·Σⱼ D̃`` on a Bloch-group element, then the sum rule
is not a transcendental evaluation at all: it is the statement that a class in
``ℝ/(π²/2)ℤ`` **vanishes**.  That would explain the clean rational answer and
would change what a proof has to do.

This probe TESTS that, it does not assume it.

Gates
-----
G1  On the branch locus, is ``Vⱼ = 3·D̃`` for SOME consistent branch choice
    ``(n, m)`` — i.e. ``u = Log y + 2πi·n``, ``v = Log(1−y) + 2πi·m`` subject to
    ``e^u = y``, ``e^v = 1−y``?  Scanned over a small integer window, per root.
    Reported per root with the winning ``(n,m)`` or an explicit MISS.

G2  Whatever ``V − 3D̃`` is, is it in ``π²ℚ`` (small denominators) or ``2πi·ℤ·u``
    — i.e. pure branch noise — rather than something transcendental?

G3  Is ``Σⱼ Re D̃`` (principal branches) an exact rational multiple of ``π²/2``?
    This is the mod-``π²/2`` vanishing statement, tested directly and
    independently of whether G1 succeeds.

G4  What the residual actually is, in closed form — and why the reading fails.

No fitting: the branch scan ranges over integers only, every candidate is
reported, and a MISS is reported as a MISS.

-- Ref: [manuscript] bean qou-0yqu; library/zagier-the-dilogarithm-function/zagier-the-dilogarithm-function.pdf (Zagier 2007) §II.1 B
"""

from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

TWO_PI_I = 2j * mp.pi
B_CORPUS = (-1, +1, +1)
SCAN = range(-2, 3)


def roots():
    rs = mp.polyroots([1, -2, 3, -1], maxsteps=200, extraprec=200)
    real = [r for r in rs if abs(mp.im(r)) < mp.mpf(10) ** -35]
    cplx = [r for r in rs if abs(mp.im(r)) >= mp.mpf(10) ** -35]
    cplx.sort(key=lambda r: -mp.im(r))
    return cplx[0], cplx[1], mp.mpc(mp.re(real[0]))


def V(y, b):
    """The sum rule's summand, as the corpus defines it."""
    return 3 * mp.polylog(2, y) + (mp.log(y) + b * mp.pi * 1j) ** 2


def enhanced(y, n, m):
    """Zagier's D̃ = Li₂(z) + u·v/2 at branch offsets (n, m), or None if the
    covering constraint e^u = y, e^v = 1 − y fails at working precision."""
    u = mp.log(y) + n * TWO_PI_I
    v = mp.log(1 - y) + m * TWO_PI_I
    if abs(mp.exp(u) - y) > mp.mpf(10) ** -30:
        return None
    if abs(mp.exp(v) - (1 - y)) > mp.mpf(10) ** -30:
        return None
    return mp.polylog(2, y) + u * v / 2


def gate1_match(ys):
    out = []
    for name, y, b in zip(("y1", "y2", "y3"), ys, B_CORPUS):
        target = V(y, b)
        best = None
        for n in SCAN:
            for m in SCAN:
                d = enhanced(y, n, m)
                if d is None:
                    continue
                err = abs(target - 3 * d)
                if best is None or err < best[0]:
                    best = (err, n, m)
        out.append(
            {
                "root": name,
                "best_abs_error": mp.nstr(best[0], 8) if best else None,
                "best_n": best[1] if best else None,
                "best_m": best[2] if best else None,
                "exact_match": bool(best and best[0] < mp.mpf(10) ** -30),
            }
        )
    return {
        "gate": "G1",
        "claim": "V_j == 3*Dtilde at some integer branch offset (n,m)",
        "scan_window": [SCAN.start, SCAN.stop - 1],
        "per_root": out,
        "pass": all(o["exact_match"] for o in out),
    }


def gate2_residual(ys):
    """V − 3D̃ at the PRINCIPAL branch: is it π²-rational / branch noise?"""
    out = []
    pi2 = mp.pi**2
    for name, y, b in zip(("y1", "y2", "y3"), ys, B_CORPUS):
        d = enhanced(y, 0, 0)
        if d is None:
            out.append({"root": name, "principal_branch_valid": False})
            continue
        r = V(y, b) - 3 * d
        out.append(
            {
                "root": name,
                "principal_branch_valid": True,
                "residual_re": mp.nstr(mp.re(r), 15),
                "residual_im": mp.nstr(mp.im(r), 15),
                "residual_re_over_pi_sq": mp.nstr(mp.re(r) / pi2, 15),
                "residual_re_over_half_pi_sq": mp.nstr(mp.re(r) / (pi2 / 2), 15),
            }
        )
    return {
        "gate": "G2",
        "claim": "V - 3*Dtilde is branch noise (pi^2-rational real part), not transcendental",
        "per_root": out,
    }


def gate3_mod_pi_sq(ys):
    """Σⱼ Re D̃ at the principal branch, measured against π²/2."""
    pi2 = mp.pi**2
    ds = [enhanced(y, 0, 0) for y in ys]
    if any(d is None for d in ds):
        return {"gate": "G3", "principal_branch_valid": False}
    total_re = sum(mp.re(d) for d in ds)
    ratio = total_re / (pi2 / 2)
    nearest = mp.nint(ratio)
    return {
        "gate": "G3",
        "claim": "sum_j Re Dtilde is an exact rational multiple of pi^2/2",
        "sum_re_Dtilde": mp.nstr(total_re, 25),
        "ratio_to_half_pi_sq": mp.nstr(ratio, 20),
        "nearest_integer": int(nearest),
        "distance_to_nearest_integer": mp.nstr(abs(ratio - nearest), 8),
        "is_integer_multiple": bool(abs(ratio - nearest) < mp.mpf(10) ** -25),
        "sum_rule_target_ratio": -3,
        "note": (
            "The sum rule says sum_j Re V_j = -3 pi^2/2. If V = 3*Dtilde then "
            "sum_j Re Dtilde = -pi^2/2, i.e. ratio = -1."
        ),
    }


def gate4_residual_closed_form(ys):
    """The residual is NOT noise -- it is exactly computable, and that is what
    kills the pure-rationality reading.

    On the branch locus ``2u = 3v + 2πi·k`` one gets ``(3/2)uv = u² − πi·k·u``,
    so at the principal branch

        V − 3·D̃ = (u + bπi)² − u² + πi·k·u = πi(2b + k)·u − b²π²

    with ``u = Log y``.  Per root, with ``(b,k) = (−1,1), (1,−1), (1,0)``:

        y₁:  −πi·u − π²   ⟹  Re = π·arg(y₁) − π²
        y₂:  conjugate    ⟹  Re = π·arg(y₁) − π²
        y₃:  −π²          ⟹  Re = −π²         (u real, and 2u = 3v exactly)

    Summing and imposing the sum rule ``Σ Re V = −3π²/2`` gives the exact
    restatement

        Σⱼ Re D̃(yⱼ) = π²/2 − (2/3)·π·θ,      θ = arg y₁.

    **This is the negative result.**  The ``π·θ`` term is not in ``π²ℚ``, so the
    sum rule does NOT reduce to "a class in ℝ/(π²/2)ℤ vanishes" under this
    identification.  Scope-(a): this particular set-up does not close.  It does
    NOT exclude an enhanced-dilogarithm formulation on a different covering
    point or a different Bloch element.
    """
    y1, _y2, _y3 = ys
    theta = mp.arg(y1)
    pi = mp.pi
    predicted = [pi * theta - pi**2, pi * theta - pi**2, -(pi**2)]
    actual = []
    for y, b in zip(ys, B_CORPUS):
        d = enhanced(y, 0, 0)
        actual.append(mp.re(V(y, b) - 3 * d))
    worst = max(abs(a - p) for a, p in zip(actual, predicted))
    lhs = sum(mp.re(enhanced(y, 0, 0)) for y in ys)
    rhs = pi**2 / 2 - mp.mpf(2) / 3 * pi * theta
    return {
        "gate": "G4",
        "claim": "the residual V - 3*Dtilde has an exact closed form: pi i (2b+k) u - b^2 pi^2",
        "predicted_residual_re": [mp.nstr(p, 15) for p in predicted],
        "actual_residual_re": [mp.nstr(a, 15) for a in actual],
        "worst_abs_error": mp.nstr(worst, 8),
        "closed_form_verified": bool(worst < mp.mpf(10) ** -25),
        "exact_restatement": "sum_j Re Dtilde(y_j) == pi^2/2 - (2/3) pi theta,  theta = arg y_1",
        "restatement_lhs": mp.nstr(lhs, 25),
        "restatement_rhs": mp.nstr(rhs, 25),
        "restatement_abs_error": mp.nstr(abs(lhs - rhs), 8),
        "restatement_holds": bool(abs(lhs - rhs) < mp.mpf(10) ** -20),
        "negative_result": (
            "The pi*theta term is NOT in pi^2 Q, so the sum rule does NOT reduce "
            "to the vanishing of a class in R/(pi^2/2)Z under this identification. "
            "SCOPE-(a): this set-up does not close. It does NOT exclude an "
            "enhanced-dilogarithm formulation at a different covering point or on "
            "a different Bloch element -- no invariant forbids that, so no "
            "scope-(b) claim is made."
        ),
    }


def main() -> None:
    ys = roots()
    g1 = gate1_match(ys)
    g2 = gate2_residual(ys)
    g3 = gate3_mod_pi_sq(ys)
    g4 = gate4_residual_closed_form(ys)
    verdict = (
        "IDENTIFIED: the sum rule is a mod-pi^2/2 statement about the enhanced "
        "dilogarithm"
        if g1["pass"] and g3.get("is_integer_multiple")
        else "REFUTED (scope-a): V is NOT 3*Dtilde at any integer branch offset; "
        "the residual is exactly pi i (2b+k) u - b^2 pi^2 (G4), leaving a "
        "pi*arg(y_1) term outside pi^2 Q. The sum rule does not reduce to a "
        "mod-pi^2/2 rationality statement under this identification."
    )
    result = {
        "probe": "qbeta_5two_enhanced_dilog_probe",
        "dps": mp.mp.dps,
        "source": "library/zagier-the-dilogarithm-function/zagier-the-dilogarithm-function.pdf = Zagier, The Dilogarithm Function (2007), II.1 B",
        "gates": [g1, g2, g3, g4],
        "verdict": verdict,
        "scope": (
            "Numerical only. A positive result would REFRAME the open problem "
            "(transcendental evaluation -> rationality mod pi^2/2), not prove the "
            "sum rule. Scope-(a) throughout: nothing here excludes any ingredient."
        ),
    }
    print(json.dumps(result, indent=2))
    out = Path(__file__).resolve().parents[1] / "qbeta-5two-enhanced-dilog.witness.json"
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
