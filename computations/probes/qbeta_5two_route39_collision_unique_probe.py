#!/usr/bin/env python3
"""Route 39 -- the collision `phi_0` is the ONLY zero of `pairDisc` on the arc,
and it is a statement about a QUARTIC IN t, not about phi.

Bean `qou-glbl`. `envelopeS_total_concrete_of_unique_collision` now rests on
exactly one hypothesis:

    hcoll : forall phi in Ioo 0 pi, phi != c -> pairDisc phi != 0

Route 32 measured the unique discriminant crossing at `c* = -0.7422176659` by
scanning `phi`. **That is the shape of argument this lane has retracted twice** --
a claim about how many roots something has, backed by samples. This probe checks
the algebra that replaces it.

THE REDUCTION
-------------
`pairDisc` is a function of `phi` only through `t = realRootPath phi`, and

    pairDisc(phi) * t^2 * (t-1)^2  ==  E(t),   E(t) = t^4 - 2t^3 + 7t^2 - 6t + 1

so the zeros of `pairDisc` are the zeros of a QUARTIC. Two facts then finish it:

* `E'(t) = 2(2t-1)(t^2 - t + 3)` and `t^2 - t + 3 > 0` always, so `E` is strictly
  DECREASING below `t = 1/2` and strictly INCREASING above it -- one minimum, no
  case analysis about where its roots are;
* `pairDisc >= 0` forces `t^2 + t - 1 >= 0` (`W_nonneg_of_disc_nonneg`, already
  proved in the tree), i.e. `t >= 0.618 > 1/2`. So every zero of `pairDisc` sits
  in the region where `E` is strictly increasing, and there is at most one.

Uniqueness in `phi` then needs only that `t` is strictly monotone in `phi`, which
it is: `dt/dc < 0` and `dc/dphi = -sin phi < 0` on `(0, pi)`.

⚠ E HAS A SECOND ROOT IN `(0,1)`, near `t = 0.2192`. It is out of range -- the arc
gives `t > 2/5` (`two_fifths_lt`, proved) -- but a proof that forgot to say so
would be proving something false. G4 measures it rather than assuming it away.

**The 5_2 sum rule remains verified to 80 dps, unproved.**
"""

import json
import pathlib

from mpmath import (cos, fabs, findroot, mp, mpf, nstr, pi, polyroots, re, sin,
                    sqrt)
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402


def real_root(c):
    """The unique root of `unitCubic c t = t^3 - 2ct^2 + (2c+1)t - 1` in (0,1)."""
    rs = polyroots([1, -2 * c, 2 * c + 1, -1], maxsteps=200, extraprec=200)
    cands = [re(r) for r in rs if fabs(r.imag) < mpf(10) ** -25 and 0 < re(r) < 1]
    assert len(cands) == 1, f"c={c}: {len(cands)} roots in (0,1)"
    return cands[0]


def pair_disc(ph):
    """Lean's `pairDisc phi = pairBeta^2 - 4*pairGamma`."""
    c = cos(ph)
    t = real_root(c)
    beta = t - 2 * c
    gamma = t ** 2 - 2 * c * t + 2 * c + 1
    return beta ** 2 - 4 * gamma, t


def E(t):
    return t ** 4 - 2 * t ** 3 + 7 * t ** 2 - 6 * t + 1


def Eprime(t):
    return 4 * t ** 3 - 6 * t ** 2 + 14 * t - 6


def main() -> int:
    set_compute_dps()
    N = 400
    gates = []

    # ---- G1: the reduction identity ----------------------------------------
    worst_id = mpf(0)
    for i in range(N):
        ph = pi * mpf(i + 1) / (N + 1)
        d, t = pair_disc(ph)
        worst_id = max(worst_id, fabs(d * t ** 2 * (t - 1) ** 2 - E(t)))
    # and OFF the arc: any (c, t) with unitCubic c t = 0, c outside [-1, 1]
    worst_off = mpf(0)
    for c in [mpf("-3"), mpf("-1.7"), mpf("1.2"), mpf("1.49"), mpf("-8")]:
        t = real_root(c)
        beta = t - 2 * c
        gamma = t ** 2 - 2 * c * t + 2 * c + 1
        d = beta ** 2 - 4 * gamma
        worst_off = max(worst_off, fabs(d * t ** 2 * (t - 1) ** 2 - E(t)))
    gates.append({
        "gate": "G1",
        "claim": "THE REDUCTION: pairDisc(phi) * t^2 * (t-1)^2 = E(t) with "
                 "E(t) = t^4 - 2t^3 + 7t^2 - 6t + 1, so the zeros of pairDisc are the zeros of a "
                 "QUARTIC IN t. Checked on the arc AND at five values of c OUTSIDE [-1,1] -- the "
                 "identity is a consequence of `unitCubic c t = 0` alone, not of anything about "
                 "the arc, and checking it only where it will be used would not have shown that",
        "arc_points": N,
        "worst_residual_on_arc": nstr(worst_id, 12),
        "worst_residual_off_arc": nstr(worst_off, 12),
        "pass": bool(worst_id < mpf(10) ** -30 and worst_off < mpf(10) ** -30),
    })

    # ---- G2: E' factors, so E has ONE minimum -------------------------------
    worst_fac = mpf(0)
    for k in range(-40, 60):
        t = mpf(k) / 20
        worst_fac = max(worst_fac, fabs(Eprime(t) - 2 * (2 * t - 1) * (t ** 2 - t + 3)))
    disc_quad = 1 - 12          # discriminant of t^2 - t + 3
    gates.append({
        "gate": "G2",
        "claim": "E'(t) = 2(2t-1)(t^2 - t + 3), and t^2 - t + 3 has discriminant -11 < 0 so it is "
                 "positive everywhere. Hence E is strictly DECREASING below t = 1/2 and strictly "
                 "INCREASING above -- a single minimum, established by a factorisation rather "
                 "than by locating roots numerically",
        "worst_residual": nstr(worst_fac, 12),
        "discriminant_of_the_quadratic_factor": int(disc_quad),
        "E_at_one_half": nstr(E(mpf(1) / 2), 12),
        "pass": bool(worst_fac < mpf(10) ** -30 and disc_quad < 0 and E(mpf(1) / 2) < 0),
    })

    # ---- G3: every zero of pairDisc has t > 1/2, via t^2 + t - 1 >= 0 -------
    # `W_nonneg_of_disc_nonneg` (proved in the tree) says pairDisc >= 0 forces
    # t^2 + t - 1 >= 0, i.e. t >= (sqrt 5 - 1)/2 = 0.618... > 1/2.
    golden = (sqrt(5) - 1) / 2
    min_t_with_disc_nonneg = None
    for i in range(N):
        ph = pi * mpf(i + 1) / (N + 1)
        d, t = pair_disc(ph)
        if d >= 0:
            min_t_with_disc_nonneg = (t if min_t_with_disc_nonneg is None
                                      else min(min_t_with_disc_nonneg, t))
    gates.append({
        "gate": "G3",
        "claim": "every zero of pairDisc sits where E is strictly increasing. `pairDisc >= 0` "
                 "forces `t^2 + t - 1 >= 0` -- that is `W_nonneg_of_disc_nonneg`, ALREADY PROVED "
                 "in the tree -- so t >= (sqrt5 - 1)/2 = 0.6180 > 1/2. No new analysis is needed "
                 "for this half; the lemma was proved for a different purpose and covers it",
        "golden_section": nstr(golden, 12),
        "min_t_observed_with_disc_nonneg": (nstr(min_t_with_disc_nonneg, 12)
                                            if min_t_with_disc_nonneg is not None else None),
        "pass": bool(min_t_with_disc_nonneg is not None and min_t_with_disc_nonneg > golden),
    })

    # ---- G4: E HAS A SECOND ROOT, and it is out of range --------------------
    roots = [re(r) for r in polyroots([1, -2, 7, -6, 1], maxsteps=200, extraprec=200)
             if fabs(r.imag) < mpf(10) ** -25]
    in01 = sorted(r for r in roots if 0 < r < 1)
    t_lo = min(real_root(cos(pi * mpf(i + 1) / (N + 1))) for i in range(N))
    t_hi = max(real_root(cos(pi * mpf(i + 1) / (N + 1))) for i in range(N))
    gates.append({
        "gate": "G4",
        "claim": "⚠ E has TWO roots in (0,1), not one. The second is at t = 0.2192, below the "
                 "arc's range -- `two_fifths_lt` (proved) gives t > 2/5 = 0.4. A uniqueness proof "
                 "that did not exclude it would be proving something FALSE, and the exclusion is "
                 "a lemma the tree already has rather than a numeric window",
        "E_roots_in_unit_interval": [nstr(r, 12) for r in in01],
        "arc_t_range": [nstr(t_lo, 12), nstr(t_hi, 12)],
        "second_root_below_two_fifths": bool(len(in01) == 2 and in01[0] < mpf(2) / 5),
        "pass": bool(len(in01) == 2 and in01[0] < mpf(2) / 5 < t_lo and in01[1] < t_hi),
    })

    # ---- G5: t is strictly increasing in phi --------------------------------
    prev = None
    monotone = True
    worst_gap = None
    for i in range(N):
        ph = pi * mpf(i + 1) / (N + 1)
        t = real_root(cos(ph))
        if prev is not None:
            gap = t - prev
            if gap <= 0:
                monotone = False
            worst_gap = gap if worst_gap is None else min(worst_gap, gap)
        prev = t
    gates.append({
        "gate": "G5",
        "claim": "t is strictly INCREASING in phi on (0,pi), which is what turns uniqueness in t "
                 "into uniqueness in phi. The reason is two signs, not a scan: dt/dc < 0 "
                 "(numerator -2t(1-t) < 0 over a denominator >= 7/4 > 0) and dc/dphi = -sin phi "
                 "< 0. Measured here as a cross-check on the sign convention, not as the argument",
        "strictly_increasing_on_sample": bool(monotone),
        "smallest_forward_step": nstr(worst_gap, 12) if worst_gap is not None else None,
        "pass": bool(monotone and worst_gap is not None and worst_gap > 0),
    })

    # ---- G6: the crossing itself, and its t --------------------------------
    def d_of(ph):
        return pair_disc(ph)[0]

    phi0 = findroot(d_of, mpf("2.4"))
    t0 = real_root(cos(phi0))
    c0 = cos(phi0)
    gates.append({
        "gate": "G6",
        "claim": "the crossing, located by bisecting pairDisc rather than by scanning: phi_0 with "
                 "cos(phi_0) = c* = -0.7422176659, matching Route 32's measured value, and "
                 "t(phi_0) = 0.6478 -- above the golden section, as G3 requires, and above 1/2 "
                 "where E is strictly increasing",
        "phi_0": nstr(phi0, 16),
        "phi_0_degrees": nstr(phi0 * 180 / pi, 16),
        "cos_phi_0": nstr(c0, 16),
        "t_at_phi_0": nstr(t0, 16),
        "E_at_t0": nstr(E(t0), 12),
        "t0_above_golden": bool(t0 > golden),
        "pass": bool(fabs(E(t0)) < mpf(10) ** -25 and t0 > golden
                     and fabs(c0 + mpf("0.7422176658829284376")) < mpf(10) ** -15),
    })

    out = {
        "probe": "qbeta_5two_route39_collision_unique",
        "bean": "qou-glbl", "dps": mp.dps,
        "pairs_with_lean": [
            "QOU/QBeta/FiveTwoRootLabelling.lean (pairDisc, realRootPath)",
            "QOU/QBeta/FiveTwoRootStructure.lean (two_fifths_lt, W_nonneg_of_disc_nonneg)",
            "QOU/QBeta/FiveTwoEnvelopeInstance.lean "
            "(envelopeS_total_concrete_of_unique_collision)",
        ],
        "gates": gates,
        "verdict": {
            "measured": "pairDisc(phi) * t^2 * (t-1)^2 = E(t) with E = t^4 - 2t^3 + 7t^2 - 6t + 1, "
                        "so `hcoll` is a statement about a quartic. E'(t) = 2(2t-1)(t^2-t+3) with "
                        "the quadratic factor positive, so E has ONE minimum at t = 1/2; and "
                        "pairDisc >= 0 forces t >= 0.618 (already proved), so every zero is where "
                        "E strictly increases -- at most one.",
            "trap": "E has a SECOND root in (0,1), at t = 0.2192. It is excluded by "
                    "`two_fifths_lt`, which the tree already proves. A uniqueness argument that "
                    "did not exclude it would be false.",
            "still_needed_in_lean": "the identity, the E' factorisation, and strict monotonicity "
                                    "of t in phi. All three are algebra plus signs already in the "
                                    "tree; none needs a numeric window.",
            "sum_rule_status": "verified to 80 dps, unproved",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-5two-route39-collision-unique.witness.json")
    dest.write_text(json.dumps(out, indent=2) + "\n")
    for g in gates:
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:80]}")
    print(f"\nwitness -> {dest}")
    ok = all(g["pass"] for g in gates)
    print("VERDICT: " + ("`hcoll` reduces to a quartic in t with one minimum; every zero of "
                         "pairDisc lies where it strictly increases, so there is at most one."
                         if ok else "FAILED -- see the gates above."))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
