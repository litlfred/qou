#!/usr/bin/env python3
"""Is the 5₂ saddle sum rule a statement about Zagier's ENHANCED dilogarithm?

Lead
----
Zagier, *The Dilogarithm Function* (2007), §II.1 B (`uploads/fulltext.pdf`):
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

No fitting: the branch scan ranges over integers only, every candidate is
reported, and a MISS is reported as a MISS.

-- Ref: [manuscript] bean qou-0yqu; uploads/fulltext.pdf (Zagier 2007) §II.1 B
"""

from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp

mp.mp.dps = 50

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


def main() -> None:
    ys = roots()
    g1 = gate1_match(ys)
    g2 = gate2_residual(ys)
    g3 = gate3_mod_pi_sq(ys)
    verdict = (
        "IDENTIFIED: the sum rule is a mod-pi^2/2 statement about the enhanced "
        "dilogarithm"
        if g1["pass"] and g3.get("is_integer_multiple")
        else "NOT IDENTIFIED: see per-gate detail; the enhanced-dilogarithm "
        "reading does not close as stated"
    )
    result = {
        "probe": "qbeta_5two_enhanced_dilog_probe",
        "dps": mp.mp.dps,
        "source": "uploads/fulltext.pdf = Zagier, The Dilogarithm Function (2007), II.1 B",
        "gates": [g1, g2, g3],
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
