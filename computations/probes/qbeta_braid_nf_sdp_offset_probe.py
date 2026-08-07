#!/usr/bin/env python3
"""qbeta_braid_nf_sdp_offset_probe.py — the braid's own operator content in the
SDP, and its offset from the lattice saddle point.

THE PROPOSAL (owner, 2026-08-07, restated): a particle interaction is not an
isolated event — it IS an SDP solution, and that solution is what begins the
braid/knot interaction. The solution should carry the magnitude and angle of the
knot's initial trajectory and its OFFSET FROM THE LATTICE SADDLE POINT; the
energy of the interaction should be the magnitude, and possibly the angle of
incidence.

TWO EARLIER READINGS FAILED, EACH NAMING THE FIX:

  1. Angle-structure LP — the offset x_geom − x_LP vanishes identically
     (2.4e-16, 5.0e-16) because both anchors sit at the symmetric point.
     `QOU/Knot/SymmetricOptimum.lean` proves why: `optima_coincide` shows two
     concave objectives INVARIANT under the symmetry share their optimum. Fix
     named: the objective must BREAK the symmetry.
  2. Canonical confinement LP — homogeneous. `G x ≥ 0` is a cone, so the
     feasible set at net `n` is `n ×` a fixed polytope; with `t`, `G`
     knot-independent and only `n_target = |tr_M(K)|` varying, two knots give
     PARALLEL offsets (angle drift measured EXACTLY 0). One knot-dependent
     number, ratio-shaped, unfalsifiable by `ratio_attained`. Fix named: the
     braid's operator content must enter the OBJECTIVE or the GRAM, not merely
     the scalar net.

THIS PROBE TAKES THE FIX. The Frobenius-demand program
(`solve_frobenius_dual_lp`) is

    min t·x   s.t.  1ᵀx = n_target,   G x = nf      (a VECTOR demand)

and `nf` is the NORMAL-FORM vector of the braid word in `H_3(q)` — the braid's
own operator content, reduced through the Gröbner-Shirshov tables
(`pyhecke.gram.hm`). Since `G` is invertible (rank 6), `G x = nf` fixes
`x* = G⁻¹ nf` uniquely, and `nf`'s DIRECTION varies per knot, not merely its
scale. Homogeneity is therefore broken and the offset direction becomes
knot-dependent — giving a MAGNITUDE *and* an ANGLE per knot, two numbers, which
is what the falsifiability bar requires.

Both anchors are 3-braids, so both live in the SAME 6-dimensional NF space and
are directly comparable:
    muon anchor    4₁  = closure of (σ₁σ₂⁻¹)²
    proton anchor  𝔹₃  = closure of (σ₁σ₂⁻¹)³

THE LATTICE SADDLE POINT. Per `SymmetricOptimum`, the point a symmetry-invariant
objective would select is the symmetric one; at net `n` in 6 coordinates that is
`x_sym = (n/6)·1`. The offset is `x* − x_sym`, and the knot-dependence of its
direction is exactly what the two failed readings lacked.

GATES (a wrong inverse would silently poison everything downstream):
  G0  `σ_g · σ_g⁻¹ = 1` in NF, for both generators — verifies that
      `σ⁻¹ = σ − h·I` (from the Hecke relation σ² = hσ + 1) is encoded right.
  G1  `G x* = nf` to round-off — the solve is consistent.
  G2  the two offsets are NOT parallel — i.e. homogeneity really is broken.
      If they ARE parallel this route collapses to the previous one and the
      verdict says so.

THE TEST. The A-free curve (PR #4513) requires
    (L − ϑ_μ²)/(L − ϑ_p²) = S_μ/S_p = r,  L = ln²q₀,
and since r < 0 the pair must STRADDLE ln q₀. Checked as a necessary condition
first, then the ratio itself.

METRIC FIXED IN ADVANCE (anti-fit): Euclidean in NF coordinates, the same for
both anchors, chosen before any number was computed. No alternative metric is
tried and none is selected to make a value come out right.

Scope (STRICT). Measures parameter-free data and compares to an A_ω-free
constraint. Nothing tuned; no ϑ asserted; nothing wired. A miss is a miss.

Run: python3 -u computations/probes/qbeta_braid_nf_sdp_offset_probe.py \
       2>&1 | tee /tmp/qbeta_braid_nf_sdp.log
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.precision import set_compute_dps  # noqa: E402
from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402

_TOOLS = Path(__file__).resolve().parent.parent.parent / "tools" / "pyhecke" / "python"
if _TOOLS.is_dir() and str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from pyhecke import gram as _gram  # noqa: E402

set_compute_dps()

S_MUON = mp.mpf("0.00968298")
S_PROTON = mp.mpf("-0.03945936")
# Canonical proton-pinned substrate modulus, READ not typed. The T4 probe's old
# literal 1.11020 was a unit conflation (it solved 2*ln q = h instead of using
# q0); fixed 2026-08-07, which moved the derived theta by -0.60% / -0.05%.
Q0 = mp.mpf(Q_50_DIGIT_STR)

IDENT = [1.0, 0.0, 0.0, 0.0, 0.0, 0.0]


def sigma(nf, gen):
    """Right-multiply by σ_gen  →  hm(nf, c=1, d=0, gen)."""
    return _gram.hm(nf, 1.0, 0.0, gen)


def sigma_inv(nf, gen):
    """Right-multiply by σ_gen⁻¹ = σ_gen − h·I  →  hm(nf, c=1, d=−h, gen).

    From the Hecke relation σ² = hσ + 1 with h = q − q⁻¹.
    """
    return _gram.hm(nf, 1.0, -float(_gram.h), gen)


def braid_nf(n_reps):
    """NF vector of (σ₁ σ₂⁻¹)^n — generators 0 and 1 in pyhecke indexing."""
    nf = list(IDENT)
    for _ in range(n_reps):
        nf = sigma(nf, 0)
        nf = sigma_inv(nf, 1)
    return nf


def main() -> int:
    print("=" * 78)
    print(" braid NF in the Frobenius-demand SDP — offset from the lattice saddle")
    print("=" * 78)

    G = np.asarray([[float(v) for v in row] for row in _gram.gram_matrix()],
                   dtype=float)
    Ginv = np.linalg.inv(G)
    d = G.shape[0]
    print(f"\n  NF basis ({d}): {list(_gram.NF_NAMES)}   h = q₀ − q₀⁻¹ = "
          f"{float(_gram.h):.12g}")

    # ---- G0 GATE: is σ⁻¹ really the inverse? ----
    print("\n[G0] gate — σ_g · σ_g⁻¹ = 1 in NF (verifies σ⁻¹ = σ − h·I):")
    g0_ok = True
    for gen in (0, 1):
        back = sigma_inv(sigma(list(IDENT), gen), gen)
        err = max(abs(a - b) for a, b in zip(back, IDENT))
        ok = err < 1e-12
        g0_ok = g0_ok and ok
        print(f"     gen {gen}: max|σσ⁻¹ − 1| = {err:.3g}  → {ok}")

    anchors = {"muon (4₁)": 2, "proton (𝔹₃)": 3}
    res = {}
    print("\n[nf] braid normal forms and their SDP solutions:")
    for name, reps in anchors.items():
        nf = np.asarray(braid_nf(reps), dtype=float)
        x = Ginv @ nf
        g1 = float(np.linalg.norm(G @ x - nf))
        net = float(np.ones(d) @ x)
        x_sym = np.full(d, net / d)
        off = x - x_sym
        mag = float(np.linalg.norm(off))
        res[name] = {"reps": reps, "nf": nf.tolist(), "x_star": x.tolist(),
                     "G1_resid": g1, "net": net,
                     "offset": off, "offset_norm": mag,
                     "tr_M": float(_gram.nf_tr(list(nf)))}
        print(f"    {name:<12} (σ₁σ₂⁻¹)^{reps}")
        print(f"      nf      = [{', '.join(f'{v:.6g}' for v in nf)}]")
        print(f"      tr_M    = {res[name]['tr_M']:.12g}   net 1ᵀx* = {net:.12g}")
        print(f"      G1 |Gx*−nf| = {g1:.3g}   ‖offset from saddle‖ = {mag:.12g}")

    g1_ok = all(r["G1_resid"] < 1e-6 for r in res.values())

    # ---- G2: are the two offsets parallel (i.e. did homogeneity survive)? ----
    o1 = res["muon (4₁)"]["offset"]
    o2 = res["proton (𝔹₃)"]["offset"]
    cos = float(o1 @ o2 / (np.linalg.norm(o1) * np.linalg.norm(o2)))
    cos = max(-1.0, min(1.0, cos))
    sep = float(np.arccos(cos))
    not_parallel = abs(sep) > 1e-7 and abs(sep - np.pi) > 1e-7
    print(f"\n[G2] angle BETWEEN the two anchors' offsets = {sep:.12g} rad")
    print(f"     offsets are NOT parallel (homogeneity broken): {not_parallel}")
    if not not_parallel:
        print("     ** parallel ⇒ this collapses to the homogeneous case; the "
              "direction carries no knot information. **")

    # ---- the readings, tested against the A-free curve ----
    lnq = mp.log(Q0)
    L = lnq**2
    r_target = S_MUON / S_PROTON
    print(f"\n[T1] A-free test (r = {mp.nstr(r_target, 10)} < 0 ⇒ the pair must "
          f"straddle ln q₀ = {mp.nstr(lnq, 8)}):")
    # reading 'mag'  : ϑ_K = ‖offset‖
    # reading 'angsep': not per-knot (it is a single pairwise number) — excluded
    #                   by construction, noted so no one reads it as a candidate
    # THREE readings, DECLARED TOGETHER before any is evaluated, and ALL
    # reported whatever they do — the pairwise separation is deliberately NOT a
    # candidate (it is one number for the pair, not one per knot).
    #   'offset_magnitude'  ||offset||               — the "magnitude"
    #   'angle_to_t'        angle(offset, t)         — the ANGLE OF INCIDENCE
    #                                                  onto the objective
    #   'angle_to_sym'      angle(offset, 1)         — angle to the symmetric
    #                                                  (lattice-saddle) direction
    t_vec = np.asarray([float(v) for v in _gram.TR_M], dtype=float)
    ones = np.ones(d)

    def ang_between(u, v):
        c = float(u @ v / (np.linalg.norm(u) * np.linalg.norm(v)))
        return float(np.arccos(max(-1.0, min(1.0, c))))

    readings = {
        "offset_magnitude": {k: mp.mpf(repr(res[k]["offset_norm"])) for k in res},
        "angle_to_t": {k: mp.mpf(repr(ang_between(res[k]["offset"], t_vec)))
                       for k in res},
        "angle_to_sym": {k: mp.mpf(repr(ang_between(res[k]["offset"], ones)))
                         for k in res},
    }
    verdicts = {}
    for label, vals in readings.items():
        tm, tp = vals["muon (4₁)"], vals["proton (𝔹₃)"]
        straddle = bool(tm < lnq < tp)
        rr = None
        if straddle:
            den = L - tp**2
            rr = (L - tm**2) / den if den != 0 else None
        matches = bool(rr is not None and abs(rr - r_target) < mp.mpf("1e-3"))
        verdicts[label] = {
            "theta_mu": mp.nstr(tm, 14), "theta_p": mp.nstr(tp, 14),
            "straddles_lnq0": straddle,
            "ratio": mp.nstr(rr, 14) if rr is not None else None,
            "matches_r": matches,
        }
        print(f"     reading {label!r}: ϑ_μ = {mp.nstr(tm, 10)}, "
              f"ϑ_p = {mp.nstr(tp, 10)}  → straddles: {straddle}"
              + (f"   ratio = {mp.nstr(rr, 10)} vs r = {mp.nstr(r_target, 10)}"
                 if rr is not None else ""))
    # 'angle_to_sym' is VACUOUS BY CONSTRUCTION: offset = x - (net/d)*1 has
    # 1^T offset = net - net = 0, so it is orthogonal to 1 and the angle is
    # pi/2 for EVERY input. Recorded as a construction artifact, not a
    # measurement — the same class of error as taking arccos of round-off.
    verdicts["angle_to_sym"]["vacuous_by_construction"] = True
    verdicts["angle_to_sym"]["why"] = (
        "offset is orthogonal to the all-ones direction by construction "
        "(1^T offset = 0), so this angle is pi/2 identically and carries no "
        "information about any knot")
    print("     NOTE: 'angle_to_sym' is pi/2 identically — offset ⊥ 1 by "
          "construction. Vacuous, not a measurement.")
    hit = any(v["matches_r"] for v in verdicts.values())
    any_straddle = any(v["straddles_lnq0"] for v in verdicts.values())

    verdict = (
        ("THE BRAID'S OPERATOR CONTENT DOES BREAK THE HOMOGENEITY — the two "
         "anchors' offsets are genuinely non-parallel "
         f"(separation {sep:.6g} rad), so unlike every earlier reading the "
         "direction carries knot information and the route supplies a MAGNITUDE "
         "and an ANGLE per knot rather than one scaled number. That is the "
         "falsifiability bar cleared. "
         if not_parallel else
         "HOMOGENEITY SURVIVED — the two offsets are parallel, so the direction "
         "carries no knot information and this collapses to the previously "
         "excluded case. ")
        + ("BUT NONE OF THE THREE DECLARED READINGS SUPPLIES ϑ: all fail the "
           "A-free curve's necessary straddling condition. "
           if not any_straddle else
           ("AND A READING LANDS ON THE A-FREE CURVE — this requires "
            "independent confirmation before any claim is made. " if hit else
            "AND A READING STRADDLES BUT MISSES THE A-FREE RATIO. "))
        + "WHAT IS ESTABLISHED EITHER WAY: the machinery now exists to put the "
        "braid's own operator content into the SDP — nf_of_word/hm reduces the "
        "braid word through the Grobner-Shirshov tables, G x = nf pins x* = "
        "G^-1 nf uniquely, and the offset from the symmetric point (the lattice "
        "saddle, per SymmetricOptimum) is computable per knot. Gates: sigma "
        "inverse verified against the Hecke relation, and G x* = nf to "
        f"{max(r['G1_resid'] for r in res.values()):.2g}. "
        "One of the three, 'angle_to_sym', turned out VACUOUS BY CONSTRUCTION "
        "— the offset is orthogonal to the all-ones direction by definition "
        "(1^T offset = 0), so that angle is pi/2 identically for every knot; it "
        "is recorded as an artifact rather than a measurement. So two "
        "substantive readings were tested, not three. "
        "SCOPE (a): the readings tested use a metric fixed in advance "
        "(Euclidean in NF coordinates). Untried and NOT excluded: a G-induced "
        "(Frobenius) metric, which is the geometrically natural one here since "
        "G is the Frobenius form the program is written in; and the offset's "
        "individual COMPONENTS (per-Wedderburn-channel) rather than any scalar "
        "summary of it. Nothing fitted; nothing wired; the S values formed the "
        "test only.")
    print("\nVERDICT:", verdict)

    wb = WitnessBuilder("qbeta-braid-nf-sdp-offset", engine="pyhecke+numpy+mpmath")
    wb.set_description(
        "Owner proposal: the interaction IS an SDP solution carrying the knot's "
        "magnitude, angle, and offset from the lattice saddle. Takes the fix "
        "named by two prior exclusions (angle-structure offset vanishes at the "
        "symmetric point; canonical confinement LP is homogeneous) by putting "
        "the braid's own operator content into the program: the Frobenius-demand "
        "LP G x = nf with nf the normal-form vector of the braid word in H_3(q). "
        "Both anchors are 3-braids ((s1 s2^-1)^2 for 4_1, ^3 for Borromean) so "
        "both live in the same 6-dim NF space. Measures the offset from the "
        "symmetric point (the lattice saddle per SymmetricOptimum) and tests the "
        "magnitude reading against the A_omega-free curve. Metric fixed in "
        "advance (Euclidean in NF coords). Nothing fitted; nothing wired.")
    wb.set_content_block("conj:im-q-physical-role")
    wb.add_data("program", "min t.x s.t. 1^T x = n_target, G x = nf "
                           "(Frobenius vector demand)")
    wb.add_data("braid_words", {"muon (4_1)": "(s1 s2^-1)^2",
                                "proton (B_3)": "(s1 s2^-1)^3"})
    wb.add_data("nf_basis", list(_gram.NF_NAMES))
    wb.add_data("anchors", {k: {kk: vv for kk, vv in v.items()
                                if kk != "offset"} for k, v in res.items()})
    wb.add_data("offset_separation_rad", sep)
    wb.add_data("homogeneity_broken", bool(not_parallel))
    wb.add_data("readings_tested", verdicts)
    wb.add_data("readings_declared_together",
                ["offset_magnitude", "angle_to_t (the angle of incidence onto "
                 "the objective)", "angle_to_sym (angle to the lattice-saddle "
                 "direction)"])
    wb.add_data("pairwise_separation_not_a_candidate",
                "the angle BETWEEN the two anchors' offsets is one number for "
                "the pair, not one per knot, so it cannot serve as theta_K; "
                "reported only as the homogeneity-broken diagnostic")
    wb.add_data("a_free_target_r", mp.nstr(r_target, 16))
    wb.add_data("metric_fixed_in_advance",
                "Euclidean in NF coordinates, identical for both anchors, chosen "
                "before any value was computed")
    wb.add_data("untried_not_excluded",
                ["a G-induced (Frobenius) metric rather than Euclidean",
                 "the offset components rather than its norm",
                 "an angle to a canonical reference rather than the pairwise "
                 "separation"])
    wb.add_data("verdict", verdict)
    wb.add_assertion("G0_sigma_inverse_correct",
                     computed=1.0 if g0_ok else 0.0, expected=1.0, tolerance=0.5,
                     source="sigma_g * sigma_g^-1 = 1 in NF for both generators, "
                            "verifying sigma^-1 = sigma - h*I from the Hecke "
                            "relation")
    wb.add_assertion("G1_solve_consistent",
                     computed=1.0 if g1_ok else 0.0, expected=1.0, tolerance=0.5,
                     source="G x* = nf to < 1e-6 for both anchors")
    wb.save()
    print("  witness -> computations/probes/qbeta-braid-nf-sdp-offset.witness.json")
    return 0 if (g0_ok and g1_ok) else 1


if __name__ == "__main__":
    raise SystemExit(main())
