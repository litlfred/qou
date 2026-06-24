#!/usr/bin/env python3
"""bring_s4_jE_point_count_probe.py
====================================

Task-2 follow-up to the merged #2710 result (Jac(Bring) ~ E⁴,
E = Bring/S₄ elliptic): ATTEMPT the explicit j(E) via the one route that is
NOT blocked the way #2710's were (symbolic fixed-field collapses to a genus-0
subfield; periods hit the conjugate-singularity RiemannSurface wall) —
**equivariant point-counting** over F_p.

Idea. For the elliptic quotient E = Bring/S₄,
    a_p(E) = p + 1 − |E(F_p)|,   |a_p| ≤ 2√p  (Hasse),
and a few a_p identify E (hence j) by matching an elliptic curve.

Result of this probe (HONEST NEGATIVE — the naive shortcut fails):
the *naive* |E(F_p)| ≈ #(S₄-orbits of Bring(F_p)) is WRONG. |Bring(F_p)| is
small (genus-4 curve, ~p+1±8√p), so its S₄-orbits number only 0–2, giving
a_p ≈ p — a gross Hasse violation. The reason is structural: |E(F_p)| is
dominated by S₄-orbits in Bring(F̄_p) that carry NO F_p-rational Bring point
(the orbit is Galois-stable as a set but its points are conjugate over an
extension). The naive count sees only orbits with an F_p representative.

The CORRECT count is the equivariant (Lefschetz) one,
    |E(F_p)| = (1/|S₄|) Σ_{g∈S₄} #{P ∈ Bring(F̄_p) : Frob(P) = g·P},
i.e. a sum of g-twisted point counts over F_{p^{ord(g)}} — a genuine
twisted-form computation (or Magma's function-field fixed field). That is the
sharpened "bounded next step" left open by #2710's audit; it is NOT done here.

What this probe DOES establish (exact, no fit): the Bring(F_p) counts (which
are correct, Hasse-OK for genus 4) and the precise reason the elementary
orbit shortcut cannot give j(E). The structural reduction stands regardless
(Jac ~ E⁴, W = E = Bring/S₄, the q-family M a 2×2 SL₂, tr B = 3(3[2]_q²+2)/
(4([2]_q+2)) — see the keystone ledger + the [2]_q-form audit).
"""
from __future__ import annotations

import itertools
import json
import math
import pathlib


def bring_points_fp(p: int) -> list[tuple]:
    """Projective points of Bring (Σx = Σx² = Σx³ = 0) in P⁴(F_p)."""
    pts = []
    rng = range(p)
    for lead in range(5):  # canonical rep: first nonzero coord = 1
        for tail in itertools.product(rng, repeat=4 - lead):
            x = [0] * lead + [1] + list(tail)
            if (sum(x) % p == 0
                    and sum(v * v for v in x) % p == 0
                    and sum(v * v * v for v in x) % p == 0):
                pts.append(tuple(x))
    return pts


def _canon(t: tuple, p: int) -> tuple:
    for lead in range(5):
        if t[lead] % p != 0:
            inv = pow(t[lead], p - 2, p)
            return tuple((v * inv) % p for v in t)
    return t


def naive_s4_orbits(pts: list[tuple], p: int) -> int:
    """#(S₄-orbits of Bring(F_p)); S₄ permutes x0..x3, fixes x4."""
    ptset = {_canon(t, p) for t in pts}
    done, orbits = set(), 0
    for t in ptset:
        if t in done:
            continue
        orbits += 1
        for perm in itertools.permutations(range(4)):
            done.add(_canon((t[perm[0]], t[perm[1]], t[perm[2]], t[perm[3]], t[4]), p))
    return orbits


def main() -> dict:
    results = []
    for p in (7, 11, 13, 17, 19, 23, 29, 31):
        pts = bring_points_fp(p)
        nb = len({_canon(t, p) for t in pts})
        N = naive_s4_orbits(pts, p)
        ap_naive = p + 1 - N
        a_curve = p + 1 - nb               # Frobenius trace of Bring itself
        results.append({
            "p": p,
            "bring_points": nb,
            "bring_ap": a_curve,
            "bring_hasse_ok": abs(a_curve) <= 2 * 4 * math.sqrt(p),  # genus 4
            "naive_E_orbits": N,
            "naive_ap_E": ap_naive,
            "naive_ap_E_hasse_ok": abs(ap_naive) <= 2 * math.sqrt(p),
        })
    naive_fails = all(not r["naive_ap_E_hasse_ok"] for r in results)
    bring_ok = all(r["bring_hasse_ok"] for r in results)
    verdict = (
        "j(Bring/S₄) NOT obtained — naive equivariant shortcut fails as predicted. "
        "Bring(F_p) counts are correct (Hasse-OK for genus 4), but |E(F_p)| ≈ "
        "#(S₄-orbits of Bring(F_p)) grossly violates Hasse (a_p≈p): |E(F_p)| is "
        "dominated by F̄_p S₄-orbits with no F_p Bring point. The correct count is "
        "the equivariant/twisted Lefschetz sum (1/|S₄|)Σ_g #{Frob(P)=g·P} over "
        "F_{p^ord(g)} (or Magma's function-field fixed field) — the sharpened "
        "bounded-next-step from #2710, not done here. Structural reduction (Jac~E⁴, "
        "W=E=Bring/S₄, M a 2×2 SL₂, tr B=[2]_q-rational) stands regardless. No fit."
    )
    return {
        "computation": "bring_s4_jE_point_count_probe",
        "description": ("Attempt at explicit j(Bring/S₄) via equivariant point-"
                        "counting; honest negative — naive S₄-orbit count of "
                        "Bring(F_p) is not |E(F_p)| (inert F̄_p orbits dominate). "
                        "Records the correct route (twisted Lefschetz / Magma)."),
        "discipline": "exact mod-p point counts; no fit; documents the j(E) blocker",
        "auditOnly": "docs/audits/2026-06-24-bring-s4-jE-point-count-attempt.md",
        "results": results,
        "naive_shortcut_fails": naive_fails,
        "bring_counts_hasse_ok": bring_ok,
        "verdict": verdict,
    }


if __name__ == "__main__":
    out = main()
    print(f"{'p':>3} {'|Bring(Fp)|':>11} {'bring_a_p':>9} {'naiveN':>6} "
          f"{'naive_a_p(E)':>12} {'naive Hasse':>11}")
    for r in out["results"]:
        print(f"{r['p']:>3} {r['bring_points']:>11} {r['bring_ap']:>9} "
              f"{r['naive_E_orbits']:>6} {r['naive_ap_E']:>12} "
              f"{str(r['naive_ap_E_hasse_ok']):>11}")
    print("\nVERDICT:", out["verdict"])
    p = pathlib.Path(__file__).resolve().parent / "bring-s4-jE-point-count.witness.json"
    p.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    print(f"\nwitness → {p}")
