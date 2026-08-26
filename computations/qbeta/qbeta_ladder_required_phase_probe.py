#!/usr/bin/env python3
"""qbeta_ladder_required_phase_probe.py — what phase does the Q_β ladder
actually require, and how far is each convention from it?

BACKGROUND (bean `qou-cds1`, tranche S1 of the 2026-08-15 convention ruling).

The committed ladder is

    Q_A   = m_e·|q²−2q−1|(q+1)/(2q³)
    Q_N1  = Q_A·cos(α − u/2)                     α = (z−1)h/2,  u = b·ℏ_q²
    Q_N2  = Q_N1·(1 + c₂u²)                      c₂ = −1  (hardcoded)
    c₃    = (Q_codata/Q_N2 − 1)/u³

Substituting `z_D` for `z_C` moves the reported `c₃` from ≈ −2.07 to ≈ −974
(registry §9g). That number is routinely read as "convention D breaks the
ladder by three orders of magnitude", which overstates what it measures.

WHAT THIS PROBE MEASURES INSTEAD.  `α` enters at exactly one place, inside a
cosine, and `c₃` is obtained by *inverting* the ladder against the measured
Q-value. So `α` is not a free prediction — the ladder pins it. Invert for it:

    α_req = u/2 − arccos( Q_codata / (Q_A·(1 + c₂u²)) )

(negative branch: every substrate anchor has α < 0), and then report each
convention's distance from `α_req` **in radians**. That is the same
information `c₃` carries, in units that do not divide by `u³ ≈ 6e-7` and so
do not inflate a small phase error into a large-looking number.

The `1/u³` is also what makes `c₃` a poor unit for this comparison: it is a
fixed magnifier, identical for both conventions, so the C→D ratio in `c₃` is
just the C→D ratio in the cosine residual. Reporting radians makes the size
of the actual disagreement legible.

WHAT THIS IS NOT.  Not a derivation of `α` in either frame, and not a fit:
nothing here is proposed as a value for anything. `α_req` is a measurement of
what the ladder demands, computed to make the C-vs-D gap interpretable.

SCOPE.  Scope-(a) throughout, per AGENTS.md §"Before declaring refuted": the
statements below are about *this* ladder with *this* phase ansatz. Nothing
here excludes convention D from the decay channel by a proved invariant.

Anchor: the experimental (proton) pin, per the 2026-08-07 owner directive.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qbeta_utils import substrate_ladder_quantities  # noqa: E402
from qou_substrate.constants import q_at, q_muon_at  # noqa: E402
from substrate import codata_constants as C  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402

set_compute_dps()

ME = mp.mpf(str(C.M_E_MEV))
QCOD = mp.mpf(str(C.Q_BETA_MEV))
C2 = mp.mpf(-1)  # hardcoded in the committed extraction


def z_C(q):
    """Convention C: z = √q/(1+q).  Equivalently 1/(√q + 1/√q) — the
    spelling `qbeta_utils.substrate_ladder_quantities` actually uses, and one
    of the forms a name-level convention detector does not see."""
    return mp.sqrt(q) / (1 + q)


def z_D(q):
    """Convention D: z = q³/(q²+1).  Canonical per the 2026-08-15 ruling."""
    return q ** 3 / (q ** 2 + 1)


def q_a_over_me(q):
    return mp.fabs(q ** 2 - 2 * q - 1) * (q + 1) / (2 * q ** 3)


def analyse(q, label):
    s = substrate_ladder_quantities(q, convention="C")
    h, u = s["h"], s["u"]
    Q_A = ME * q_a_over_me(q)

    # Invert the ladder for the phase it requires (c₃ = 0 exactly).
    cos_req = QCOD / (Q_A * (1 + C2 * u ** 2))
    if not (-1 < cos_req < 1):
        raise ValueError(f"{label}: cos_req={cos_req} outside (-1, 1)")
    alpha_req = u / 2 - mp.acos(cos_req)

    rows = []
    for name, z in (("C", z_C(q)), ("D", z_D(q))):
        alpha = (z - 1) * h / 2
        # c₃ this phase implies, via the committed extraction.
        Q_N2 = Q_A * mp.cos(alpha - u / 2) * (1 + C2 * u ** 2)
        c3 = (QCOD / Q_N2 - 1) / u ** 3
        rows.append({
            "convention": name,
            "z": z,
            "alpha": alpha,
            "alpha_minus_required": alpha - alpha_req,
            "rel_dev_from_required": (alpha - alpha_req) / alpha_req,
            "c3_implied": c3,
        })

    # How tightly is α pinned?  d(cos)/dα = −sin(α−u/2), so a phase error δα
    # produces a relative cosine error |sin(α−u/2)|·δα, which the extraction
    # divides by u³. Demanding |c₃| ≤ 1 gives the window below.
    slope = mp.fabs(mp.sin(alpha_req - u / 2))
    alpha_window = u ** 3 / slope

    return {
        "anchor": label,
        "q": q,
        "h": h,
        "u": u,
        "Q_A_MeV": Q_A,
        "Q_codata_MeV": QCOD,
        "alpha_required": alpha_req,
        "alpha_window_for_c3_le_1": alpha_window,
        "rows": rows,
    }


def main() -> int:
    print("=" * 78)
    print(" Q_β ladder: the phase it REQUIRES, vs what each convention supplies")
    print("=" * 78)

    results = []
    for q, label in ((q_at(), "proton (experimental pin)"),
                     (q_muon_at(), "muon (ideal CAL-2 pin)")):
        r = analyse(q, label)
        results.append(r)
        print(f"\n### {label}   q = {mp.nstr(r['q'], 20)}")
        print(f"  Q_A       = {mp.nstr(r['Q_A_MeV'], 12)} MeV")
        print(f"  Q_codata  = {mp.nstr(r['Q_codata_MeV'], 12)} MeV")
        print(f"  α_required= {mp.nstr(r['alpha_required'], 12)}")
        print(f"  window for |c₃| ≤ 1: ±{mp.nstr(r['alpha_window_for_c3_le_1'], 4)} rad")
        print(f"\n  {'conv':>5} {'z':>14} {'α':>14} {'α−α_req':>14} "
              f"{'rel':>10} {'c₃':>12}")
        print("  " + "-" * 74)
        for row in r["rows"]:
            print(f"  {row['convention']:>5} {float(row['z']):>14.9f} "
                  f"{float(row['alpha']):>14.9f} "
                  f"{float(row['alpha_minus_required']):>14.3e} "
                  f"{float(row['rel_dev_from_required']):>9.2%} "
                  f"{float(row['c3_implied']):>12.4f}")

    # ── Is α_C the required phase as a FUNCTION of q, or only at q₀? ────────
    #
    # The two anchors are 11.5 ppb apart, and α_req moves ~100× further than
    # α_C does across that gap. If that holds over a real range, then α_C
    # agreeing with α_req at q₀ is a point coincidence, not a functional
    # identity — the two curves cross, they do not coincide. This is the
    # discriminating test between "the C ladder's phase is derived" and "the C
    # ladder's phase happens to be close at the substrate anchor", and it is
    # independent of which convention is canonical.
    q0 = results[0]["q"]
    slope_rows = []
    for frac in ("1e-4", "1e-3", "1e-2"):
        d = mp.mpf(frac)
        qs = [q0 * (1 - d), q0, q0 * (1 + d)]
        req = []
        acs = []
        for qq in qs:
            s = substrate_ladder_quantities(qq, convention="C")
            Q_A = ME * q_a_over_me(qq)
            cr = QCOD / (Q_A * (1 + C2 * s["u"] ** 2))
            if not (-1 < cr < 1):
                req.append(None)
                acs.append(None)
                continue
            req.append(s["u"] / 2 - mp.acos(cr))
            acs.append((z_C(qq) - 1) * s["h"] / 2)
        if any(v is None for v in req):
            # NOT silently dropped: the guard firing is itself a result. Past
            # this step size Q_A(q) falls below Q_codata, so cos_req > 1 and
            # the ladder has NO real phase at all — there is no α whatever
            # that closes it. Report the step and move on.
            slope_rows.append({
                "rel_step": frac,
                "d_alpha_required_dq": None,
                "d_alpha_C_dq": None,
                "slope_ratio": None,
                "note": "no real phase solves the ladder at this step "
                        "(Q_A < Q_codata ⇒ arccos argument leaves [−1, 1])",
            })
            continue
        d_req = (req[2] - req[0]) / (qs[2] - qs[0])
        d_aC = (acs[2] - acs[0]) / (qs[2] - qs[0])
        slope_rows.append({
            "rel_step": frac,
            "d_alpha_required_dq": d_req,
            "d_alpha_C_dq": d_aC,
            "slope_ratio": d_req / d_aC,
        })

    print("\n" + "=" * 78)
    print(" Do α_required and α_C agree as FUNCTIONS of q, or only at q₀?")
    print("=" * 78)
    print(f"\n  {'step':>8} {'dα_req/dq':>18} {'dα_C/dq':>18} {'ratio':>12}")
    print("  " + "-" * 60)
    for row in slope_rows:
        if row["d_alpha_required_dq"] is None:
            print(f"  {row['rel_step']:>8}   — {row['note']}")
            continue
        print(f"  {row['rel_step']:>8} {float(row['d_alpha_required_dq']):>18.6f} "
              f"{float(row['d_alpha_C_dq']):>18.6f} "
              f"{float(row['slope_ratio']):>12.2f}")

    live = [r for r in slope_rows if r["d_alpha_required_dq"] is not None]
    if live:
        s = live[0]
        opposed = s["d_alpha_required_dq"] * s["d_alpha_C_dq"] < 0
        print(f"""
  α_required and α_C move in {'OPPOSITE' if opposed else 'the same'} directions with q
  (slopes {float(s['d_alpha_required_dq']):+.3f} vs {float(s['d_alpha_C_dq']):+.3f}, ratio {float(s['slope_ratio']):.1f}).

  {'They therefore CROSS at the substrate anchor rather than coincide.' if opposed else ''}
  {'The ~2e-5 rad agreement at q0 is a transversal crossing of two curves' if opposed else ''}
  {'with different q-dependence, not a functional identity. A derived phase' if opposed else ''}
  {'would track alpha_required as q moves; this one runs the other way.' if opposed else ''}""")

    # ── Does the slope mismatch ALONE account for the cross-anchor swing? ───
    #
    # The c₃ cross-anchor swing (≈0.0491 between the proton and muon pins) is
    # treated in the corpus as a signature needing explanation — AGENTS.md's
    # fibre-vs-observable banner reads it as evidence that c₃(q) is a
    # complex-analytic fibre object sampled at real q₀, and registry §9g
    # records "REFUTED-as-real-q survives" off it.
    #
    # If α_req and α_C simply cross at an angle, the swing is forced with no
    # fibre content at all: differencing two curves of different slope over an
    # 11.5 ppb anchor gap. dc₃/dα = tan(α − u/2)/u³ at the solution, so
    #
    #     Δc₃  =  [tan(α−u/2)/u³] · (dα_C/dq − dα_req/dq) · Δq
    #
    # is a pure prediction from the two slopes. Compare it to the measured
    # swing. Agreement means the swing carries no information beyond "the two
    # curves cross transversally".
    swing = None
    if live and len(results) > 1:
        pr, mu = results[0], results[1]
        s = live[0]
        alpha_C_p = next(r for r in pr["rows"] if r["convention"] == "C")["alpha"]
        dc3_dalpha = mp.tan(alpha_C_p - pr["u"] / 2) / pr["u"] ** 3
        dq = mu["q"] - pr["q"]
        predicted = dc3_dalpha * (s["d_alpha_C_dq"]
                                  - s["d_alpha_required_dq"]) * dq
        observed = (next(r for r in mu["rows"] if r["convention"] == "C")["c3_implied"]
                    - next(r for r in pr["rows"] if r["convention"] == "C")["c3_implied"])
        swing = {
            "dc3_dalpha": dc3_dalpha,
            "slope_mismatch_rad_per_q": s["d_alpha_C_dq"] - s["d_alpha_required_dq"],
            "delta_q_muon_minus_proton": dq,
            "predicted_swing": predicted,
            "observed_swing": observed,
            "rel_agreement": mp.fabs(predicted - observed) / mp.fabs(observed),
        }
        print("\n" + "=" * 78)
        print(" Is the cross-anchor c₃ swing anything but the slope mismatch?")
        print("=" * 78)
        print(f"""
  dc₃/dα                            = {mp.nstr(dc3_dalpha, 9)}
  slope mismatch (dα_C − dα_req)/dq = {mp.nstr(swing['slope_mismatch_rad_per_q'], 9)}
  Δq (muon − proton)                = {mp.nstr(dq, 9)}

  PREDICTED swing, from slopes only = {mp.nstr(predicted, 9)}
  OBSERVED  c₃(muon) − c₃(proton)   = {mp.nstr(observed, 9)}
  agreement                         = {float(swing['rel_agreement']):.3%}

  The swing is the two curves crossing at an angle, differenced over an
  11.5 ppb anchor gap. Scope-(a): this removes the swing as EVIDENCE FOR
  fibre-level c₃(q) structure. It does not refute fibre structure.

  It also fixes the S_leak genericity window. S_leak := c₃ + V changes sign
  across the anchors exactly when V lies between −c₃(p) and −c₃(m), so that
  window's width IS |c₃(p) − c₃(m)| = the swing = {float(mp.fabs(observed)):.4f} — the 0.049
  AGENTS.md already flags as making the Vol(4₁) offset non-unique. Same
  number, same phenomenon, now traced to the slope mismatch.
""")

    p = results[0]
    cC = next(r for r in p["rows"] if r["convention"] == "C")
    cD = next(r for r in p["rows"] if r["convention"] == "D")

    print("\n" + "=" * 78)
    print(" Reading")
    print("=" * 78)
    print(f"""
  The ladder pins α to a window of half-width ~{float(p['alpha_window_for_c3_le_1']):.1e} rad
  (that is what |c₃| ≤ 1 means as a statement about the phase). Against that:

    convention C misses by {float(cC['alpha_minus_required']):.2e} rad  ({float(cC['rel_dev_from_required']):+.2%})
    convention D misses by {float(cD['alpha_minus_required']):.2e} rad  ({float(cD['rel_dev_from_required']):+.2%})

  So "c₃: −2 → −974" is the SAME fact as "the phase error grows from
  ~{float(abs(cC['rel_dev_from_required'])):.2%} to ~{float(abs(cD['rel_dev_from_required'])):.0%}". The three-orders-of-magnitude appearance
  comes from dividing by u³ ≈ {float(p['u']**3):.1e}, a magnifier applied identically to
  both conventions — not from D failing by three orders of magnitude.

  What this does establish, scope-(a): the required phase is set by the
  measured Q-value to a part in ~10⁴ of α, and z_D sits ~{float(abs(cD['rel_dev_from_required'])):.0%} away. A D-frame
  ladder therefore cannot be recovered by substituting z_D into α = (z−1)h/2
  — the gap is far outside the window, so the FUNCTIONAL FORM of the phase
  must change, not the value of z inside it. That prunes the whole
  one-parameter class "α = (z−1)h/2, z a convention parameter" for D.

  What it does NOT establish: that convention C's α is derived. C lands
  inside the window, but the ladder inverts against CODATA, so landing there
  is agreement-to-{float(abs(cC['rel_dev_from_required'])):.0e}, not a derivation. Per
  content/.../q-beta-cos-resummation.ts, the eigenphase identification is
  AXIOMATISED (class QOU.Interactions.QBetaCosResummation), and (z−1)h/2
  first enters the corpus as the O(h) Taylor coefficient of the Form-A/Form-B
  bridge (1−h/2)/(1−zh/2), which is algebraic in z and carries no
  representation-theoretic content by itself. Both frames are un-derived
  here; only C is numerically close.
""")

    wb = WitnessBuilder("qbeta-ladder-required-phase", engine="mpmath")
    wb.set_description(
        "Inverts the Q_β precision ladder for the phase α it requires "
        "(α_req = u/2 − arccos(Q_codata/(Q_A(1+c₂u²))), c₂ = −1 hardcoded as "
        "in the committed extraction), and reports each Markov convention's "
        "distance from it in RADIANS rather than in c₃ units. Shows that the "
        "reported c₃ swing −2.07 → −974 under C → D is a phase-error growth "
        "from ~4e-4 to ~29% magnified by the fixed 1/u³ factor, not a "
        "three-orders-of-magnitude failure. Establishes scope-(a) that the "
        "class 'α = (z−1)h/2 with z a convention parameter' cannot yield a "
        "D-frame ladder: the required window is ~1e-5 rad and z_D sits ~1e-2 "
        "away, so the functional form must change. Does NOT claim C's α is "
        "derived — the ladder inverts against CODATA and the eigenphase "
        "identification is axiomatised. No fit; nothing wired."
    )
    wb.add_data("c2_hardcoded", C2)
    wb.add_data("anchors", [
        {
            "anchor": r["anchor"],
            "q": fmt(r["q"]),
            "u": fmt(r["u"]),
            "Q_A_MeV": fmt(r["Q_A_MeV"]),
            "Q_codata_MeV": fmt(r["Q_codata_MeV"]),
            "alpha_required": fmt(r["alpha_required"]),
            "alpha_window_for_c3_le_1": fmt(r["alpha_window_for_c3_le_1"]),
            "conventions": [
                {k: (fmt(v) if isinstance(v, mp.mpf) else v)
                 for k, v in row.items()}
                for row in r["rows"]
            ],
        }
        for r in results
    ])

    # The two conventions differ enormously in c₃ but the magnifier is shared.
    wb.add_assertion(
        name="c3_ratio_equals_cosine_residual_ratio",
        computed=fmt(cD["c3_implied"] / cC["c3_implied"]),
        expected=fmt(
            ((QCOD / (ME * q_a_over_me(p["q"]) * mp.cos(cD["alpha"] - p["u"] / 2)
                      * (1 + C2 * p["u"] ** 2)) - 1)
             / (QCOD / (ME * q_a_over_me(p["q"]) * mp.cos(cC["alpha"] - p["u"] / 2)
                        * (1 + C2 * p["u"] ** 2)) - 1))
        ),
        tolerance=mp.mpf("1e-40"),
        source="The 1/u³ divisor is identical for both conventions, so the c₃ "
               "ratio is exactly the ratio of the raw cosine residuals. This "
               "is what makes c₃ the wrong unit for comparing conventions.",
    )
    # D is outside the window by a wide margin — the pruning statement.
    wb.add_assertion(
        name="zD_phase_outside_ladder_window_by_over_100x",
        computed=str(int(
            mp.fabs(cD["alpha_minus_required"]) >
            100 * p["alpha_window_for_c3_le_1"])),
        expected="1", tolerance=0,
        source=f"|α_D − α_req| = {mp.nstr(mp.fabs(cD['alpha_minus_required']), 6)} rad vs "
               f"window {mp.nstr(p['alpha_window_for_c3_le_1'], 6)} rad. Scope-(a): the "
               "one-parameter class α = (z−1)h/2 cannot supply a D-frame "
               "ladder; the functional form must change.",
    )
    wb.add_data("q_dependence", [
        {k: (fmt(v) if isinstance(v, mp.mpf) else v) for k, v in row.items()}
        for row in slope_rows
    ])
    if live:
        s = live[0]
        wb.add_assertion(
            name="alpha_required_and_alpha_C_slopes_have_opposite_sign",
            computed=str(int(
                s["d_alpha_required_dq"] * s["d_alpha_C_dq"] < 0)),
            expected="1", tolerance=0,
            source=(
                f"dα_req/dq = {mp.nstr(s['d_alpha_required_dq'], 8)}, "
                f"dα_C/dq = {mp.nstr(s['d_alpha_C_dq'], 8)} (central difference, "
                "±1e-4 relative in q). Opposite signs ⇒ the two curves cross "
                "transversally at q₀ rather than coincide, so the 2.3e-5 rad "
                "agreement there is a point coincidence, not a functional "
                "identity. A phase derived from the representation would "
                "track α_req as q moves. Scope-(a): this is a statement about "
                "the committed ansatz, not a proved exclusion of any frame."
            ),
        )
    if swing is not None:
        wb.add_data("cross_anchor_swing", {
            k: fmt(v) for k, v in swing.items()
        })
        wb.add_assertion(
            name="cross_anchor_c3_swing_is_the_slope_mismatch",
            computed=fmt(swing["predicted_swing"]),
            expected=fmt(swing["observed_swing"]),
            tolerance=mp.mpf("1e-3"),
            source=(
                "Predicted from the two slopes ALONE — "
                "Δc₃ = [tan(α−u/2)/u³]·(dα_C/dq − dα_req/dq)·Δq — with no "
                "fibre content: "
                f"{mp.nstr(swing['predicted_swing'], 8)} vs measured "
                f"{mp.nstr(swing['observed_swing'], 8)}, agreeing to "
                f"{float(swing['rel_agreement']):.2%}. Scope-(a): removes the "
                "cross-anchor swing as EVIDENCE FOR a complex-analytic "
                "fibre-level c₃(q) (the reading in AGENTS.md's fibre-vs-"
                "observable banner and registry §9g's 'REFUTED-as-real-q "
                "survives'); does NOT refute fibre structure, which stands or "
                "falls on other grounds. Also fixes the S_leak genericity "
                "window width, which is |c₃(p) − c₃(m)| by definition."
            ),
        )
    out = wb.save()
    print(f"Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
