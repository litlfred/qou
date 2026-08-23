#!/usr/bin/env python3
"""Route 9: the 5₂ sum rule becomes a RATIONALITY statement, via Bloch torsion at ℚ(ζ₇)⁺.

Context
-------
Bean ``qou-b7cy`` (child of ``qou-0yqu``).  Route 8 (``qou-8v3k``) transported the
sum rule to the totally real cyclotomic point:

    Σⱼ Re Vⱼ = −3π²/2   ⟺   Σₖ Re V(−1, yₖ) = −π²/2,   yₖ = −1 − 2cos(2πk/7)

Set ``w := −y = 1 + 2cos(2πk/7)``, a root of ``w³ − 2w² − w + 1 = 0``, and
``V(−1,y) = 2·Li₂(w) + Li₂(−w) + log²w``.

The point of this route
-----------------------
Route 6 hoped the problem would "stop being a transcendental evaluation and
become a rationality statement", and failed.  **That is achieved here**, by a
different mechanism, and the remaining unknown is a single rational number.

**The algebraic key (a ring identity, hence a Lean one-liner):**

    (1 − w)²·(1 + w) = 1 − w − w² + w³ = w²        using   w³ = 2w² + w − 1

Therefore, for the ℤ[F]-element ``ξ := 2[w] + [−w]``,

    δ(ξ) = 2·(w ∧ (1−w)) + ((−w) ∧ (1+w)) = w ∧ [(1−w)²(1+w)] = w ∧ w² = 0

in ``∧²F* ⊗ ℚ`` (the torsion ``−1`` dies on tensoring).  So **ξ lies in the Bloch
group ``B(F)``** for ``F = ℚ(ζ₇)⁺``.

``F`` is **totally real**, so ``r₂ = 0`` and by Borel ``B(F) ⊗ ℚ = 0``: every
element of ``B(F)`` is torsion.  The Rogers dilogarithm sends torsion elements of
the Bloch group into ``π²ℚ``.  Hence

    Σ_σ L(σ(ξ)) ∈ π²ℚ                     ← PROVED (modulo the classical theorem)

and the measured value is **exactly π²/2** (gate G5, 26 digits).

Gates
-----
G1  w, 1−w, 1+w are units: norms −1, −1, +1 (from the minimal polynomials).
G2  The ring identity (1−w)²(1+w) = w², at all three embeddings.
G3  w³ − 2w² − w + 1 = 0 at all three embeddings (the minimal polynomial).
G4  V(−1,yₖ) = 2Li₂(wₖ) + Li₂(−wₖ) + log²wₖ reproduces Route 8's −π²/2.
G5  Σₖ Re[2L(wₖ) + L(−wₖ)] = π²/2 exactly, with L the Rogers dilogarithm.
G6  Σₖ Re V = Σₖ Re L(ξₖ) − π², exactly.

⚠ What is proved and what is not
--------------------------------
**Proved (elementary algebra):** G1–G3, hence ``δ(ξ) = 0``, hence ``ξ ∈ B(F)``.
**Classical input:** F totally real ⟹ B(F) torsion ⟹ ``L(ξ) ∈ π²ℚ``.
**NOT proved — verified only:** that the rational is ``1/2`` (G5), and the
branch bookkeeping constant ``−π²`` in G6.  A per-embedding formula
``V − L(ξ) = iπ·log[(1−w)/w]`` was tried and is **FALSE** — it fails at two of
the three embeddings on branch grounds; only the *sum* is exact.  That
bookkeeping still needs doing properly.

So the sum rule is now: **one rational number away**, with the rationality itself
proved rather than hoped for.  Sum rule status: verified to 80 dps, unproved.
"""
from __future__ import annotations

import json
import pathlib

from mpmath import cos, fabs, log, mp, mpf, nstr, pi, polylog, re
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
TOL = mpf(10) ** -30


def rogers(z):
    return polylog(2, z) + log(z) * log(1 - z) / 2


def main():
    gates = []
    W = [1 + 2 * cos(2 * pi * k / 7) for k in (1, 2, 3)]

    # G3 -- minimal polynomial
    w3 = max(fabs(w ** 3 - 2 * w ** 2 - w + 1) for w in W)
    gates.append({"gate": "G3", "claim": "w^3 - 2w^2 - w + 1 = 0 for w = 1+2cos(2 pi k/7)",
                  "worst": nstr(w3, 8), "pass": bool(w3 < TOL)})

    # G1 -- units
    norms = {}
    for nm, f in (("w", lambda w: w), ("1-w", lambda w: 1 - w), ("1+w", lambda w: 1 + w)):
        P = mpf(1)
        for w in W:
            P *= f(w)
        norms[nm] = nstr(P, 20)
    ok1 = (fabs(mpf(norms["w"]) + 1) < TOL and fabs(mpf(norms["1-w"]) + 1) < TOL
           and fabs(mpf(norms["1+w"]) - 1) < TOL)
    gates.append({"gate": "G1", "claim": "w, 1-w, 1+w are UNITS of Q(zeta_7)+ (norms -1, -1, +1)",
                  "norms": norms, "pass": bool(ok1)})

    # G2 -- the ring identity
    w2 = max(fabs((1 - w) ** 2 * (1 + w) - w ** 2) for w in W)
    gates.append({"gate": "G2",
                  "claim": "(1-w)^2 (1+w) = w^2  [ring identity via w^3 = 2w^2 + w - 1]",
                  "worst": nstr(w2, 8),
                  "consequence": "delta(2[w]+[-w]) = w ^ w^2 = 0, so xi lies in the Bloch group B(F)",
                  "pass": bool(w2 < TOL)})

    # G4 -- Route 8's reduced target in w-coordinates
    tot = sum(re(2 * polylog(2, w) + polylog(2, -w) + log(w) ** 2) for w in W)
    e4 = fabs(tot + pi ** 2 / 2)
    gates.append({"gate": "G4", "claim": "sum_k Re[2Li2(w)+Li2(-w)+log^2 w] = -pi^2/2 (Route 8 target)",
                  "value": nstr(tot, 26), "abs_err": nstr(e4, 6), "pass": bool(e4 < TOL)})

    # G5 -- THE RATIONALITY VALUE
    totL = sum(re(2 * rogers(w) + rogers(-w)) for w in W)
    e5 = fabs(totL - pi ** 2 / 2)
    gates.append({"gate": "G5",
                  "claim": "sum_k Re[2L(w)+L(-w)] = pi^2/2 exactly  (L = Rogers dilogarithm)",
                  "value": nstr(totL, 26), "over_pi_sq": nstr(totL / pi ** 2, 20),
                  "abs_err": nstr(e5, 6),
                  "note": "rationality is PROVED by Bloch torsion (G2 + F totally real); "
                          "that the rational is 1/2 is VERIFIED here, not proved",
                  "pass": bool(e5 < TOL)})

    # G6 -- the branch bookkeeping constant
    d6 = tot - totL
    e6 = fabs(d6 + pi ** 2)
    gates.append({"gate": "G6", "claim": "sum_k Re V = sum_k Re L(xi) - pi^2 exactly",
                  "difference": nstr(d6, 26), "over_pi_sq": nstr(d6 / pi ** 2, 20),
                  "abs_err": nstr(e6, 6),
                  "caveat": "the per-embedding formula V - L(xi) = i pi log[(1-w)/w] is FALSE "
                            "(fails at two embeddings on branch grounds); only the SUM is exact",
                  "pass": bool(e6 < TOL)})

    # G7 -- THE PER-EMBEDDING LADDER: much stronger than the trace statement
    ms = [17, 5, -1]
    per = []
    w7 = mpf(0)
    for k, w, m in zip((1, 2, 3), W, ms):
        v = re(2 * rogers(w) + rogers(-w))
        err = fabs(v - mpf(m) * pi ** 2 / 42)
        w7 = max(w7, err)
        per.append({"k": k, "w": nstr(w, 18), "value": nstr(v, 26),
                    "claim": f"{m}*pi^2/42", "over_L1": f"{m}/7", "abs_err": nstr(err, 6)})
    # minimality of the denominator 42
    dens = []
    for w in W:
        q = re(2 * rogers(w) + rogers(-w)) / pi ** 2
        for d in range(1, 400):
            if fabs(q * d - mp.nint(q * d)) < mpf(10) ** -25:
                dens.append(d)
                break
    gates.append({"gate": "G7",
                  "claim": "PER-EMBEDDING: Re[2L(w_k)+L(-w_k)] = m_k pi^2/42 with m = (17,5,-1), "
                           "i.e. (m_k/7) L(1) -- a level-7 dilogarithm ladder",
                  "per_embedding": per,
                  "m": ms, "sum_m": sum(ms), "sum_m_over_42": "21/42 = 1/2",
                  "minimal_denominators": dens,
                  "worst": nstr(w7, 8),
                  "note": "verified separately to 100 dps with residuals ~1e-101; denominators of 7 "
                          "in units of L(1) are the signature of level-7 ladders. Bloch torsion "
                          "(G2 + F totally real) PROVES each value is in pi^2 Q; the specific "
                          "numerators 17, 5, -1 are verified, not derived.",
                  "pass": bool(w7 < TOL and dens == [42, 42, 42])})

    # G8 -- END-TO-END composition. Every other gate checks one link in isolation;
    # this one reconstructs the ORIGINAL sum rule from the three numerators alone,
    # back through Route 9 (Rogers -> V, -pi^2) and Route 8 (x = -1 -> x = 1, -pi^2).
    recon = sum(mpf(m) * pi ** 2 / 42 for m in ms) - pi ** 2 - pi ** 2
    e8 = fabs(recon - (-3 * pi ** 2 / 2))
    gates.append({"gate": "G8",
                  "claim": "END-TO-END: (sum m_k) pi^2/42 - pi^2 [Rogers->V] - pi^2 [transport back] "
                           "= -3 pi^2/2, the original sum rule at x = 1",
                  "reconstructed": nstr(recon, 26),
                  "original_target": nstr(-3 * pi ** 2 / 2, 26),
                  "abs_err": nstr(e8, 6),
                  "note": "the other gates each check one link; this checks that the two reductions "
                          "COMPOSE. 21/42 = 1/2, then 1/2 - 1 - 1 = -3/2.",
                  "pass": bool(e8 < TOL)})

    out = {
        "probe": "qbeta_5two_route9_bloch_torsion_rationality",
        "bean": "qou-b7cy",
        "parent_bean": "qou-0yqu",
        "builds_on": "qou-8v3k (Route 8 transport to x = -1)",
        "dps": mp.dps,
        "gates": gates,
        "verdict": {
            "route9": "RATIONALITY PROVED; the specific rational still to be pinned",
            "proved_elementarily": "(1-w)^2(1+w) = w^2 is a ring identity given w^3 = 2w^2 + w - 1, "
                                   "hence delta(2[w]+[-w]) = w ^ w^2 = 0, hence xi is in the Bloch "
                                   "group B(F) for F = Q(zeta_7)+. w, 1-w, 1+w are all units.",
            "classical_input": "F totally real => r_2 = 0 => B(F) tensor Q = 0 (Borel), so xi is "
                               "torsion, and Rogers L maps Bloch torsion into pi^2 Q.",
            "still_open": "that the rational is exactly 1/2 (G5), and the -pi^2 branch constant (G6). "
                          "A per-embedding branch formula was tried and is FALSE; only the sum is exact.",
            "significance": "Route 6 hoped the problem would stop being a transcendental evaluation and "
                            "become a rationality statement, and failed. That is achieved here by a "
                            "different mechanism. The sum rule is now one rational number away.",
            "sum_rule_status": "verified to 80 dps, unproved -- UNCHANGED",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-5two-route9-bloch-torsion-rationality.witness.json")
    dest.write_text(json.dumps(out, indent=2) + "\n")
    for g in gates:
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:86]}")
    print(f"\nwitness -> {dest}")
    print("VERDICT: rationality PROVED via Bloch torsion; the rational 1/2 still to be pinned.")
    return 0 if all(g["pass"] for g in gates) else 1


if __name__ == "__main__":
    raise SystemExit(main())
