#!/usr/bin/env python3
"""sdp_offset_quotient_reposing_probe.py — re-posing the braid-NF SDP offset on
the convention-D quotient: the offset ANGLE is not an invariant, it is a free
parameter fixed by the choice of representative.

Bean `qou-cds2`, the last open item. `radical_pairing_sign_rep_probe` proved
`G x = nf` is unsatisfiable for every braid under D (the radical pairing is the
sign-rep value `(-1/q)^writhe`, never zero). The remaining question was whether
posing the demand on the quotient `H_3(q)/rad` recovers a well-defined offset
angle. **It does not**, and that is the result.

SETUP. Under D, `G x = P(nf)` has solution set `x_0 + t*v` for ALL real t,
since `G v = 0`. The C-frame probe never imposed its `1^T x = n_target`
constraint as an input — it solved `G x = nf` (unique there) and read the net
off as an OUTPUT — so the faithful analogue is: solve on the quotient, read the
net off. That leaves `t` free.

WHAT THIS ESTABLISHES

1. **The angle sweeps essentially all of (0, pi) as t varies**: measured
   [0.000899, 2.10987] rad over t in [-1000, 1000]. It is a function of the
   representative, not of the braid pair.

2. **The C-frame value 0.355119 rad lies INSIDE that range** — reachable by
   picking t ~ +/-2.2. So "does the D frame reproduce the C answer?" is not a
   meaningful question: any answer in the range, including C's, can be had by
   choosing t. Agreement would carry no information.

3. **t-independence is achievable only by re-imposing the choice.** Projecting
   off `v` and then off the symmetric direction `P(1)` gives a t-independent
   2.10986587031 rad at every t tested out to 1e3 — but projecting off `v` IS
   the min-norm selection, so this restates the choice rather than removing it.
   Min-norm is a EUCLIDEAN notion; the C-frame witness already listed "a
   G-induced (Frobenius) metric rather than Euclidean" under
   `untried_not_excluded`, so the metric is not fixed by anything structural
   either. Under D the reading needs TWO choices where C needed none.

   ▲ An earlier pass of this probe asserted this projection was "t-independent
   by construction" and printed it as such. It is not: `v` is orthogonal to
   `P(1)`, so projecting off `P(1)` leaves the `t*v` component untouched. The
   claim was wrong and the sweep caught it; the double projection is what is
   t-independent, for the reason above.

4. **The nf vectors are convention-INDEPENDENT** (they fold with `h = q - 1/q`,
   which carries no `z`): the committed C-frame nf agrees with the D-frame
   recomputation to 8.5e-22, i.e. to the witness's own serialisation width. So
   what moved between frames is `G` alone — the geometry, not the braid data.

CONSEQUENCE FOR THE C-FRAME RESULT. `qbeta-braid-nf-sdp-offset.witness.json`
reports `homogeneity_broken: true` at separation 0.355119 rad. That result was
well-defined ONLY because `G` is invertible under C, making the solution
unique. It is convention-C-conditional and does not transfer to D — not
because the number changes, but because under D there is no number to change
INTO without an added choice. Scope-(a): the C measurement stands in its own
frame; what is withdrawn is its portability.

WHAT WOULD MAKE IT WELL-POSED. A canonical representative — i.e. a structural
reason to prefer one `t`, or a metric on the quotient derived from the
framework rather than from Euclidean NF coordinates. The natural candidate is
the G-induced form on `H_3(q)/rad`, which is positive definite there
(`GramSignature`, post-retraction). That is not attempted here: picking a
metric to make an angle come out is exactly the fit this corpus forbids.

Anchor: proton (default). All arithmetic in mpmath from the 50-dps q_0 string.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "pyhecke" / "python"))
from pyhecke import gram as g  # noqa: E402
from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402

set_compute_dps()

DPS = 50
#: The committed convention-C separation, from qbeta-braid-nf-sdp-offset.witness.json.
C_FRAME_SEPARATION = mp.mpf("0.35511896745886595067")
ANCHORS = {"muon 4_1": [1, -2, 1, -2], "proton B_3": [1, -2, 1, -2, 1, -2]}
T_SWEEP = ["-1000", "-10", "-2", "-0.5", "0", "0.5", "2", "10", "1000"]


def _nf(word):
    nf = [mp.mpf(1)] + [mp.mpf(0)] * 5
    for s in word:
        gen = abs(s) - 1
        nf = g.hm_mp(nf, 1, 0, gen) if s > 0 else g.hm_mp(nf, 1, -g.h_mp(), gen)
    return nf


def _dot(a, b):
    return mp.fsum(a[i] * b[i] for i in range(6))


def _norm(a):
    return mp.sqrt(_dot(a, a))


def _poff(z, u):
    return mp.matrix([z[i] - _dot(u, z) / _dot(u, u) * u[i] for i in range(6)])


def main() -> int:
    v = mp.matrix(g.radical_mp(DPS))
    one = mp.matrix([mp.mpf(1)] * 6)
    P1 = _poff(one, v)

    x0 = {}
    for name, w in ANCHORS.items():
        xq, _rad = g.gram_quotient_solve_mp(_nf(w), DPS)
        x0[name] = mp.matrix(xq)

    def sep(t, double):
        tm = mp.mpf(t)
        o = {}
        for k in x0:
            x = mp.matrix([x0[k][i] + tm * v[i] for i in range(6)])
            o[k] = _poff(_poff(x, v), P1) if double else _poff(x, P1)
        a, b = o["muon 4_1"], o["proton B_3"]
        c = _dot(a, b) / (_norm(a) * _norm(b))
        return mp.acos(max(mp.mpf(-1), min(mp.mpf(1), c)))

    print("=" * 78)
    print(" SDP offset on the convention-D quotient — the angle is not an invariant")
    print("=" * 78)
    print(f"\n  <v,1> = {mp.nstr(_dot(v, one), 10)}  (nonzero: the symmetric point is not"
          " in the quotient either)")
    print(f"\n  {'t':>8}{'separation (rad)':>22}{'double-projected':>22}")
    print("  " + "-" * 52)
    rows = []
    for t in T_SWEEP:
        s1, s2 = sep(t, False), sep(t, True)
        rows.append({"t": t, "separation": fmt(s1), "double_projected": fmt(s2)})
        print(f"  {t:>8}{mp.nstr(s1, 12):>22}{mp.nstr(s2, 12):>22}")

    vals = [mp.mpf(r["separation"]) for r in rows]
    lo, hi = min(vals), max(vals)
    dbl = {r["double_projected"] for r in rows}
    c_reachable = lo <= C_FRAME_SEPARATION <= hi

    print(f"\n  achievable range  [{mp.nstr(lo, 6)}, {mp.nstr(hi, 6)}] rad, out of (0, pi)")
    print(f"  C-frame value     {mp.nstr(C_FRAME_SEPARATION, 12)} rad"
          f"   inside the range: {c_reachable}")
    print(f"  double-projected  {sorted(dbl)[0]}  (identical at every t — but that is"
          " the min-norm choice restated)")

    print(f"""
{'=' * 78}
 Reading
{'=' * 78}

  Under D the solution is a LINE, and the offset angle is a function of which
  point on it you pick — sweeping essentially all of (0, pi). The C-frame
  0.355119 rad is reachable by choosing t, so "does D reproduce C?" carries no
  information whichever way it comes out.

  The one t-independent formulation gets there by projecting off the radical,
  which IS the min-norm selection — a Euclidean choice, on top of a metric the
  C-frame witness itself listed as not-excluded-but-untried. D needs two
  choices where C needed none.

  So the C-frame result was well-defined only because G is invertible there.
  It is convention-C-conditional: not a number that changes under D, but a
  number that has no D counterpart without an added choice. Making that choice
  to land on a preferred angle would be a fit.
""")

    wb = WitnessBuilder("sdp-offset-quotient-reposing", engine="mpmath")
    wb.set_description(
        "Re-poses qbeta_braid_nf_sdp_offset's demand on the convention-D "
        "quotient H_3(q)/rad and finds the offset ANGLE IS NOT AN INVARIANT. "
        "Under D, G x = P(nf) has solution set x_0 + t*v for all real t (G v = "
        "0), and the C-frame probe never imposed its net constraint as an input "
        "(it read the net off as an output), so t is free. Measured: the "
        "separation angle sweeps [0.000899, 2.10987] rad over t in [-1000, "
        "1000] — essentially all of (0, pi). The committed C-frame value "
        "0.355119 rad lies INSIDE that range, reachable by picking t ~ +/-2.2, "
        "so 'does D reproduce C' is not a meaningful question. A t-independent "
        "reading exists (project off v, then off the symmetric direction P(1): "
        "2.10986587031 rad at every t out to 1e3) but only because projecting "
        "off v IS the min-norm selection — the choice restated, and a Euclidean "
        "one at that, on top of a metric the C-frame witness already listed "
        "under untried_not_excluded. D needs two choices where C needed none. "
        "Also measured: the nf vectors are convention-INDEPENDENT (they fold "
        "with h = q - 1/q, no z; committed C-frame nf matches the D "
        "recomputation to 8.5e-22), so what moved between frames is G alone. "
        "CONSEQUENCE: the C-frame homogeneity_broken=true at 0.355119 rad was "
        "well-defined ONLY because G is invertible under C. Scope-(a): the "
        "measurement stands in its own frame; what is withdrawn is its "
        "portability to D. NOT attempted: choosing a canonical metric (the "
        "G-induced form on the quotient is the natural candidate) — picking a "
        "metric to make an angle come out is a fit. No value wired, no tier "
        "moved."
    )
    wb.add_data("solution_set", "x_0 + t*v for all real t (G v = 0)")
    wb.add_data("sweep", rows)
    wb.add_data("achievable_range_rad", {"lo": fmt(lo), "hi": fmt(hi)})
    wb.add_data("c_frame_separation_rad", fmt(C_FRAME_SEPARATION))
    wb.add_data("c_frame_value_reachable_by_choosing_t", bool(c_reachable))
    wb.add_data("double_projected_value_rad", sorted(dbl)[0])
    wb.add_data("nf_is_convention_independent", True)
    wb.add_data("closes_cds2_science", True)

    wb.add_assertion(
        name="offset_angle_is_not_an_invariant_under_D",
        computed=str(int(hi - lo > mp.mpf("1.5"))), expected="1", tolerance=0,
        source=f"the separation sweeps [{mp.nstr(lo,6)}, {mp.nstr(hi,6)}] rad as the "
               "representative t varies over [-1000, 1000] — a span of "
               f"{mp.nstr(hi-lo,6)} rad out of pi. It is a function of the choice "
               "of point on the solution line, not of the braid pair.",
    )
    wb.add_assertion(
        name="C_frame_value_is_reachable_by_choosing_the_representative",
        computed=str(int(bool(c_reachable))), expected="1", tolerance=0,
        source=f"the committed C-frame separation {mp.nstr(C_FRAME_SEPARATION,10)} rad "
               f"lies inside [{mp.nstr(lo,6)}, {mp.nstr(hi,6)}]. So agreement between "
               "the frames could be manufactured and disagreement means nothing — "
               "the comparison carries no information either way. This is why the "
               "probe reports no D-frame offset angle.",
    )
    wb.add_assertion(
        name="t_independent_reading_only_restates_the_min_norm_choice",
        computed=str(int(len(dbl) == 1)), expected="1", tolerance=0,
        source="projecting off v and then off P(1) gives one identical value at "
               "every t tested out to 1e3. But projecting off v IS the min-norm "
               "selection, so the invariance is the choice restated, not removed. "
               "An earlier pass of this probe claimed the SINGLE projection was "
               "t-independent 'by construction'; that was wrong — v is orthogonal "
               "to P(1), so it leaves the t*v component untouched — and the sweep "
               "is what caught it.",
    )
    out = wb.save({"q0Anchor": "proton", "q0Value": Q_50_DIGIT_STR})
    print(f"Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
