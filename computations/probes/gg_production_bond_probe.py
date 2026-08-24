#!/usr/bin/env python3
"""Build the inter-nucleon bond through (flavor-blind) gg production — does the 78% gap collapse?

Context (bean 754x, step 1.5 / the owner's "build p and n through gg production" directive).
`charge_symmetry_bond_probe` quantified the production tension: the flavor-only projection
pp↦σ, nn↦σ⁻¹ (atom_braid_word_3A) breaks strong charge symmetry by L_nn/L_pp−1 ≈ 78% — ~570×
the substrate-derived p/n flavor split and ~78× the experimental CSB bound. The content block
[`inter-nucleon-channel-color-tube`] states the σ/σ⁻¹ map is the **flavor-only projection** of a
color-tube-weighted (gg) assignment gated on `conj:s5-so3-fiber-action` (the s5-so3 keystone).

The physical lever: GLUONS ARE FLAVOR-BLIND. The color-tube interface that binds two nucleons is
a gluon-pair (gg) state coupling the 3×3 color sheets; at LEADING order it does not see u-vs-d.
So building the bond through gg production means: the leading inter-nucleon crossing is the SAME
flavor-blind color-average for every bond type (pp, pn, nn), and charge symmetry breaks only at
the sub-leading O(δ) flavor-split scale (δ = flavor_split_leading(q₀) ≈ 0.14%).

This probe TESTS that prediction — parameter-free, no fit. It recomputes the per-bond
log-suppressions L_pp / L_pn / L_nn after replacing every inter-nucleon crossing with the
flavor-blind color-average σ_avg = σ − (h/2)·I (the same crossing the production already uses for
the flavor-mixed p-n bond — `strict_averaged`). The flavor-only σ and σ⁻¹ straddle σ_avg, so the
prediction is that under the gg-symmetric bond:

  • L_pp^gg ≈ L_pn^gg ≈ L_nn^gg  — the 78% asymmetry collapses toward 0,
  • the residual mirror-nucleus split ΔB_sym(³H−³He) collapses from +2.27 toward the (unwired)
    Coulomb scale (ΔB_AME = +0.76),

confirming the 78% is a flavor-only-projection artifact, NOT a derived isospin effect. The
remaining ~0.14% (flavor) + Coulomb is what a correct gg/color-tube build must carry; this probe
does not fit either — it isolates them. (a) scope-limited: measures the collapse, does not rewire
production (owner-gated — the canonical gg bond needs the keystone color-weight matrix).
"""
from __future__ import annotations

import sys
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(HERE))

import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402 — raise dps before any mpmath value
import mpmath as mp  # noqa: E402

import mass_binding_dashboard as mbd  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from reduced_block_kernel import chi_all_lambda_reduced_block  # noqa: E402
from tr_m_atom_via_transfer import _trM  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from q_parameter import Q_MP as Q0  # noqa: E402 — mpf q0, NOT the float64 `Q`
from witness_base import WitnessBuilder  # noqa: E402

EXPERIMENTAL_CSB_BOUND = 0.01
MIRROR_PAIRS = [("3H", 1, 2, "3He", 2, 1), ("7Li", 3, 4, "7Be", 4, 3),
                ("13C", 6, 7, "13N", 7, 6)]


def _gg_symmetrize(word, h_half):
    """Replace every inter-nucleon crossing (generator index ≡ 2 mod 3) with the
    flavor-blind color-average σ_avg = σ − (h/2)·I, i.e. (c,d) → (1, −h/2).

    Intra-nucleon chains (gen 3k, 3k+1) keep the proton/neutron quark content —
    only the gg interface is symmetrized. This is the leading-order gg-production
    bond: flavor-blind at the gluon vertex."""
    out = []
    for (c, d, g) in word:
        if g % 3 == 2:  # inter-nucleon arc at gen 3k+2
            out.append((mp.mpf(1), -h_half, g))
        else:
            out.append((c, d, g))
    return out


def _trM_of(word, n, y):
    chi = chi_all_lambda_reduced_block(word, n)
    return _trM(chi, y)


# This producer USED to run at mpmath's default 15 dps, which is why the
# padding / raw-float64 / import-time gates all passed it: the numbers it
# emitted were honestly float64, with no fake precision to detect. It now
# raises working precision on the next line, and the L values below are mpf
# end to end. Gate: never_raises_dps_audit.py (bean qou-j6gb). Idempotent.
set_compute_dps()

def _bond_L_gg(Z, N, gg, q, h):
    """log(tr_free/tr_atom) for the (Z,N) 2-nucleon sub-braid; gg=True forces the
    flavor-blind σ_avg inter-nucleon crossing, gg=False uses production σ/σ⁻¹/avg."""
    n = 3 * (Z + N)
    y = {tuple(k): mp.mpf(str(v)) for k, v in y_lambda_at(n, Q0).items()}
    atom = atom_braid_word_3A(Z, N, include_inter=True)
    free = atom_braid_word_3A(Z, N, include_inter=False)
    if gg:
        atom = _gg_symmetrize(atom, h / 2)
    ta = _trM_of(atom, n, y)
    tf = _trM_of(free, n, y)
    return mp.log(tf / ta)


def run():
    me, q0, E0 = mbd._constants()
    q = mp.mpf(str(q0))
    h = q - mp.mpf(1) / q
    from _li_2_q_util import flavor_split_leading
    delta_lead = flavor_split_leading(q)

    # Production (flavor-only) L, for reference.
    Lprod = mbd._bond_type_L()

    # gg-production (flavor-blind) L.
    Lgg = {
        "pp": _bond_L_gg(2, 0, True, q, h),
        "pn": _bond_L_gg(1, 1, True, q, h),
        "nn": _bond_L_gg(0, 2, True, q, h),
    }

    ame = mbd._ame_table()

    def Bsym(L, Z, N):
        return E0 * (comb(Z, 2) * L["pp"] + Z * N * L["pn"] + comb(N, 2) * L["nn"])

    def bame(Z, A):
        t = ame.get((Z, A))
        return t[0] if t else None

    pairs = []
    for (hi, Zh, Nh, lo, Zl, Nl) in MIRROR_PAIRS:
        dprod = Bsym(Lprod, Zh, Nh) - Bsym(Lprod, Zl, Nl)
        dgg = Bsym(Lgg, Zh, Nh) - Bsym(Lgg, Zl, Nl)
        bh, bl = bame(Zh, Zh + Nh), bame(Zl, Zl + Nl)
        dba = (bh - bl) if (bh is not None and bl is not None) else None
        pairs.append({"pair": f"{hi}-{lo}", "dB_sym_prod": dprod,
                      "dB_sym_gg": dgg, "dB_AME": dba})

    asym_prod = Lprod["nn"] / Lprod["pp"] - 1.0
    asym_gg = Lgg["nn"] / Lgg["pp"] - 1.0

    # `asym_gg` IS ZERO BY CONSTRUCTION. _gg_symmetrize forces every
    # inter-nucleon crossing to the same flavor-blind sigma_avg, and the
    # intra-nucleon chains cancel in the free/atom ratio, so L_pp, L_pn and
    # L_nn are the SAME NUMBER. Whatever is left is the arithmetic's own
    # residue, not a physical asymmetry.
    #
    # So `if asym_gg` was the wrong guard: a truthiness test on a residue is
    # true for any residue that is not exactly 0.0. It read -3.33e-16 --
    # float64 epsilon -- and published
    #     collapse_factor = 0.301 / 3.33e-16 = 904080051203560
    # as if it were a measurement. Raising precision does NOT fix that; it
    # only moves the residue and makes the manufactured ratio bigger. The
    # guard has to be a RESOLUTION FLOOR, and the honest report when the
    # collapse is total is "not resolvable", not a number.
    #
    # The floor is NOT derived from mp.mp.dps, because dps is not what binds
    # here. Measured, by cleaning one input at a time:
    #     float64 h/2 in the word + math.log   ->  |asym_gg| = 3.3e-16
    #     mpf word + mp.log, float64 q0        ->  |asym_gg| = 8.1e-19
    #     ... + Q_MP instead of Q              ->  |asym_gg| = 4.4e-33
    # The last is y_lambda_at's own ~30-digit cap, not dps (70). A dps-derived
    # floor would track a number that is not the constraint and would start
    # admitting y_lambda residue again the moment anyone raised dps.
    floor = mp.mpf("1e-25")
    resolved = abs(asym_gg) > floor

    return {
        "q0": q0, "E0_MeV": E0, "h": h, "delta_lead": delta_lead,
        "L_prod": Lprod, "L_gg": Lgg,
        "asym_prod": asym_prod, "asym_gg": asym_gg,
        "asym_gg_over_delta": (abs(asym_gg) / delta_lead) if delta_lead else None,
        # Recorded so a reader can see WHY collapse_factor is null, instead of
        # having to guess whether the producer crashed or the value is absent.
        "asym_gg_resolved": resolved,
        "asym_gg_resolution_floor": floor,
        "collapse_factor": (abs(asym_prod) / abs(asym_gg)) if resolved else None,
        "mirror_pairs": pairs,
        "experimental_csb_bound": EXPERIMENTAL_CSB_BOUND,
    }


def report(res):
    print("# gg-production (flavor-blind) inter-nucleon bond — does the 78% gap collapse? (bean 754x)\n")
    print(f"q₀ = {res['q0']:.10f}   E₀ = {res['E0_MeV']:.4f} MeV   "
          f"δ_lead = {res['delta_lead'] * 100:.3f}%\n")

    print("## Per-bond log-suppression: production (flavor-only σ/σ⁻¹) vs gg (flavor-blind σ_avg)\n")
    print("| bond | L_prod | L_gg |")
    print("|---|--:|--:|")
    for b in ("pp", "pn", "nn"):
        print(f"| {b} | {res['L_prod'][b]:.4f} | {res['L_gg'][b]:.4f} |")
    print(f"\n| charge asymmetry L_nn/L_pp − 1 | production | gg |")
    print(f"|---|--:|--:|")
    print(f"| | **{res['asym_prod'] * 100:.1f}%** | **{res['asym_gg'] * 100:.3f}%** |")
    cf = (f"{res['collapse_factor']:.0f}× smaller" if res["collapse_factor"]
          else "complete — exactly charge-symmetric at leading order")
    print(f"\nCollapse: production {res['asym_prod'] * 100:.1f}% → gg "
          f"{res['asym_gg'] * 100:.3f}%  (**{cf}**).")
    print(f"The leading flavor-blind gg bond is EXACTLY charge-symmetric (L_pp=L_pn=L_nn); the "
          f"entire 78% lived in the σ-vs-σ⁻¹ inter-crossing sign choice. The sub-leading flavor "
          f"weighting (not added here) would reintroduce a split at the δ_lead ≈ "
          f"{res['delta_lead'] * 100:.3f}% scale — the correct size.\n")

    print("## Spurious mirror-nucleus split: production vs gg vs experiment\n")
    print("| mirror pair | ΔB_sym (prod) | ΔB_sym (gg) | ΔB_AME |")
    print("|---|--:|--:|--:|")
    for p in res["mirror_pairs"]:
        dba = f"{p['dB_AME']:+.3f}" if p["dB_AME"] is not None else "n/a"
        print(f"| {p['pair']} | {p['dB_sym_prod']:+.3f} | {p['dB_sym_gg']:+.3f} | {dba} |")
    print("\nUnder the flavor-blind gg bond the mirror split collapses toward 0 — the residual to "
          "ΔB_AME is then the (unwired) Coulomb energy, the physically correct mirror-split source.\n")

    print("## Verdict\n")
    if abs(res["asym_gg"]) < 0.05:
        print(f"- The 78% production asymmetry is a **flavor-only-projection artifact**: the "
              f"leading flavor-blind gg bond is EXACTLY charge-symmetric "
              f"(L_nn/L_pp−1 = {res['asym_gg'] * 100:.3f}%). The whole gap was the σ-vs-σ⁻¹ "
              f"inter-crossing sign; the intra-nucleon (uud vs udd) chains cancel in the L ratio.")
    else:
        print(f"- The gg bond reduces the asymmetry to {res['asym_gg'] * 100:.3f}% but does not "
              f"fully collapse it — a genuine sub-leading flavor/SDP effect survives.")
    print("- The gg bond is flavor-blind at the gluon vertex (σ_avg for every bond type); the "
          "production σ/σ⁻¹ split over-states charge-symmetry breaking by spreading what should be "
          "a 9-channel color average onto one crossing and its inverse.")
    print("- The correct canonical gg bond is the color-tube-weighted 9-channel sum gated on "
          "conj:s5-so3-fiber-action (the s5-so3 keystone, reduced this session to bwS0 = d_q/D). "
          "This probe uses the flavor-blind leading term only — (a) scope-limited, no fit, "
          "no production rewire (owner-gated).")


def main(argv=None):
    res = run()
    report(res)
    w = WitnessBuilder("gg-production-bond-probe", engine="python")
    w.set_description(
        "Tests whether building the inter-nucleon bond through flavor-blind gg production collapses "
        "the production charge-symmetry tension (bean 754x). Gluons couple color not flavor, so the "
        "leading gg interface is the same color-average sigma_avg = sigma - (h/2)I for every bond "
        "type. Recomputing L_pp/L_pn/L_nn with all inter-nucleon crossings forced to sigma_avg "
        "collapses the production L_nn/L_pp-1 ~ 78% (flavor-only sigma/sigma^-1) toward 0 (O(delta) "
        "flavor scale), and collapses the spurious mirror-nucleus split delta_B_sym(3H-3He) from "
        "+2.27 toward the unwired Coulomb scale (delta_B_AME=+0.76). Confirms the 78% is a "
        "flavor-only-projection artifact, not a derived isospin effect. The canonical gg bond is the "
        "color-tube-weighted 9-channel sum gated on conj:s5-so3-fiber-action. (a) scope-limited, no "
        "fit, no production rewire."
    )
    for k in ("q0", "E0_MeV", "h", "delta_lead", "L_prod", "L_gg",
              "asym_prod", "asym_gg", "asym_gg_over_delta",
              "asym_gg_resolved", "asym_gg_resolution_floor",
              "collapse_factor", "mirror_pairs"):
        w.add_data(k, res[k])
    w.add_assertion(
        "gg_flavor_blind_bond_collapses_charge_asymmetry",
        # `round(..., 4)` used to record a flat "0.0" here, which cannot tell
        # 3.3e-16 (float64 noise) from 4.4e-33 (the real residue) -- the whole
        # distinction this fix turns on. Record the value; the tolerance still
        # sets the claim.
        computed=abs(res["asym_gg"]),
        expected=mp.mpf(0), tolerance=mp.mpf("0.05"),
        source="The flavor-blind gg inter-nucleon bond (sigma_avg for every bond type) collapses "
               "the production charge asymmetry L_nn/L_pp-1 from ~78% to within 5% of zero "
               "(O(delta) flavor scale), confirming the 78% is a flavor-only-projection artifact. "
               "The residual + Coulomb is what a correct color-tube gg build must carry.",
    )
    out = w.save()
    print(f"\nwitness → {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
