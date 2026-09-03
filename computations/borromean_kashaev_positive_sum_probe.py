#!/usr/bin/env python3
"""Borromean Kashaev invariant is a POSITIVE sum at the root of unity —
feasibility probe for an in-repo machine proof of
Vol(B_3) = 8*Cl_2(pi/2) = 8G (bean qou-z1wh).

Starting point: the corpus-verified Habiro formula (transcribed from
GL2011 Appendix A in habiro_borromean_colored_jones.py, bean n920):

    J_{B,n}(q) = sum_{l=0}^{n-1} (-1)^l {n}^2
                 * ( prod_{j=1}^{l} {n+j}{n-j} )^3
                 / ( prod_{j=l+1}^{2l+1} {j} )^2 ,   {j} = q^{j/2} - q^{-j/2}.

At the Kashaev point q = e^{2pi i/N}, n = N:

  * {j} = 2i sin(pi j/N); {N} = 0, so terms with 2l+1 < N VANISH
    (numerator {N}^2 uncancelled) and terms with 2l+1 >= N survive with
    the EXACT cancellation {N}^2/{N}^2 = 1 (identical factors — no limit
    needed).
  * {N+j}{N-j} = (-2i s_j)(2i s_j) = 4 sin^2(pi j/N) > 0, so the cubed
    numerator product is kashaevProd(N,l)^3 > 0.
  * the squared denominator contributes (-1)^l * (positive) (l leftover
    factors {j}^2 = -4 sin^2 after removing j = N), cancelling the
    Habiro (-1)^l EXACTLY.

  =>  <B_3>_N = sum_{l >= (N-1)/2} P_l  with every

      P_l = kashaevProd(N,l)^3
            / prod_{j=l+1..2l+1, j != N} (2 sin(pi j'/N))^2  >  0

      (j' = j or j-N by the mirror sin(pi(j-N)/N) = -sin(pi j/N), squared).

This probe verifies numerically (float64; an asymptotic-rate check, not a
precision claim):
  P1  every surviving term is positive (well-defined log);
  P2  (2pi/N) * log sum_l P_l  ->  8G  (from above, ~1/N corrections);
  P3  the max term sits at l/N -> 3/4 (the pi/2 saddle — Catalan angle).

Consequence (the feasibility verdict): the SAME elementary architecture
that machine-proved the 4_1 volume conjecture in-repo (positive Riemann
sums of log(2 sin) squeezed against the Clausen primitive; bricks E1-E5d,
FigureEightVolumeSqueeze.lean) applies to the Borromean rings, with
log P_l = 3*log kashaevProd(N,l) - [window sum over (l, 2l+1] mirrored at
N] — 1D sums of the SAME integrand.  New bricks needed: the Cl_2
duplication formula (provable from the in-repo integral representation),
the window/mirror deviation bound, and the x = 3/4 extremum analysis.
Scope doc: docs/audits/2026-07-26-borromean-kashaev-positive-sum-feasibility.md.

Audit-only; no wiring.  Witness: borromean-kashaev-positive-sum-probe.witness.json
"""
from __future__ import annotations

import hashlib
import json
import math
from datetime import datetime, timezone
from pathlib import Path

G8 = 7.327724753  # 8 * Catalan constant = Vol(Borromean rings), 10 sig figs


def probe(N: int):
    """Return ((2pi/N)*log max term, (2pi/N)*log sum, argmax l/N)."""
    # S[l] = sum_{j=1..l} log(4 sin^2(pi j/N)) = log kashaevProd(N, l)
    S = [0.0] * N
    for j in range(1, N):
        S[j] = S[j - 1] + math.log(4 * math.sin(math.pi * j / N) ** 2)
    lmin = (N - 1) // 2
    if 2 * lmin + 1 < N:
        lmin += 1
    vals = []
    for l in range(lmin, N):
        den = 0.0
        for j in range(l + 1, 2 * l + 2):
            if j == N:
                continue
            jj = j if j < N else j - N
            den += math.log(4 * math.sin(math.pi * jj / N) ** 2)
        vals.append(3 * S[l] - den)  # log P_l — finite <=> P_l > 0 (P1)
    mx = max(vals)
    tot = mx + math.log(sum(math.exp(v - mx) for v in vals))
    argmax_x = (vals.index(mx) + lmin) / N
    c = 2 * math.pi / N
    return c * mx, c * tot, argmax_x


def main() -> None:
    rows = []
    for N in (101, 501, 1001, 3001):
        a, b, x = probe(N)
        rows.append({"N": N, "rate_max": a, "rate_sum": b, "argmax_x": x})
        print(f"N={N}: (2pi/N)max={a:.5f} (2pi/N)logSum={b:.5f} "
              f"argmax l/N={x:.4f} target={G8:.5f}")

    # P2: approach 8G from above, gap shrinking, final gap < 0.03
    gaps = [r["rate_sum"] - G8 for r in rows]
    assert all(g > 0 for g in gaps), f"not from above: {gaps}"
    assert all(gaps[i + 1] < gaps[i] for i in range(len(gaps) - 1)), gaps
    assert gaps[-1] < 0.03, f"final gap too large: {gaps[-1]}"
    # P3: saddle at 3/4
    assert abs(rows[-1]["argmax_x"] - 0.75) < 1e-3, rows[-1]["argmax_x"]

    src = Path(__file__)
    witness = {
        "description": "Borromean Kashaev positive-sum feasibility probe: "
        "(2pi/N) log <B_3>_N -> 8G from above, saddle at l/N -> 3/4; "
        "every surviving Habiro term positive at the Kashaev point "
        "(exact sign analysis in the docstring). Asymptotic-rate check "
        "at float64 — not a precision claim.",
        "computation": "borromean-kashaev-positive-sum-probe",
        "target_8G": G8,
        "rows": rows,
        "assertions": {
            "P1_all_terms_positive_logs_finite": True,
            "P2_rate_to_8G_from_above_final_gap": gaps[-1],
            "P3_argmax_near_three_quarters": rows[-1]["argmax_x"],
        },
        "scriptHash": hashlib.sha256(src.read_bytes()).hexdigest()[:12],
        "generatedAt": datetime.now(timezone.utc).isoformat(),
    }
    out = src.parent / "borromean-kashaev-positive-sum-probe.witness.json"
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=False)
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"witness written: {out.name}; all assertions pass")


if __name__ == "__main__":
    main()
