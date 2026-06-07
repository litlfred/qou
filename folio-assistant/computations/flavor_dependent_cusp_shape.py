#!/usr/bin/env python3
# polynomial_q_not_applicable: structural audit probe. No production
# wiring, no q-polynomial state sum. Evaluates the Bloch-Wigner
# dilogarithm D on candidate flavor-decorated complex shapes derived
# from the color-tube cubic roots and the Thurston cusp shapes; tests
# whether the uud-vs-udd flavor content can break the conjugate-pair
# cancellation Σ D = 0 found by PR #1669. Audit-only.
"""Flavor-dependent cusp shape probe — does uud-vs-udd reach the K_3
hyperbolic volume (Σ D), or only the K_1 real regulator?

The single missing object delimited by PR #1669 / #1663:
  a DERIVED flavor-dependent complex shape map Z(braid, flavor) → z_i
  ∈ ℂ∖ℝ giving DISTINCT proton/neutron complex shapes, so isospin
  enters Σ D (K_3 Bloch-Wigner volume), not just Σ ln|V̂_i| (K_1 Borel).

ESTABLISHED (PR #1669, do not re-litigate):
  - D(z) = Im Li_2(z) + arg(1−z)·log|z| reproduces Vol(4_1)=2Cl₂(π/3),
    Vol(ℬ_3)=8G EXACTLY (zero-param). D real, vanishes on real z.
  - Proton (uud) and neutron (udd) share the SAME ℬ_3 complement →
    identical Thurston shapes z_k → Σ D difference = 0.
  - The color-tube cubic complex discriminant roots come in conjugate
    pairs with D(z̄) = −D(z) → Σ D = 0 (knot-independent).
  - The flavor signal lives in the REAL V̂_i (K_1, D(V̂)=0).

THIS PROBE asks the next question precisely: the color-tube cubic at a
fixed real z has THREE roots (the three color sheets c_r, c_g, c_b).
At real z these are exactly {one real, one conjugate pair x±iy}
(verified: negative discriminant). The nucleon flavor content assigns
quark flavors (uud / udd) to the three color sheets. Candidate DERIVED
mechanisms:

  (a) Flavored cusp decoration — meridian/longitude holonomy
      eigenvalues carry the flavor (color-tube root selected per
      strand). Is there a derived per-strand flavor→shape map?
  (b) Per-strand color-tube root assignment — assign the 3 cubic roots
      {c_real, c_+, c_−} to the 3 strands BY FLAVOR. Does a derived
      rule break the conjugate-pair cancellation D(c_+)+D(c_−)=0?
  (c) Shared-denominator holonomy — does conj:shared-denominator-cusp-
      holonomy supply a flavor-dependent z?

DISCIPLINE: no tuning to m_n−m_p / B_AME / known volumes. Each
candidate rule is DERIVED from the color-tube / holonomy structure,
computed, and falsification-tested against the raw p/n split. A clean
negative naming the precise missing categorical object is the win.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import os
import sys
import time
from functools import reduce

import mpmath as mp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from _precision import set_compute_dps
except Exception:  # pragma: no cover
    def set_compute_dps():
        mp.mp.dps = 65

from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()
mp.mp.dps = 70  # 60 output + 10 guard

_START = time.monotonic()

from _li_2_q_util import load_q_50dps  # noqa: E402


# ── Bloch-Wigner dilogarithm (the DERIVED archimedean real image, K_3) ─
def bloch_wigner(z):
    """D(z) = Im Li_2(z) + arg(1−z)·log|z|. Real, vanishes on real z."""
    z = mp.mpc(z)
    if mp.fabs(z) < mp.mpf(10) ** (10 - mp.mp.dps):
        return mp.mpf(0)
    if mp.fabs(z - 1) < mp.mpf(10) ** (10 - mp.mp.dps):
        return mp.mpf(0)
    li2 = mp.polylog(2, z)
    return mp.im(li2) + mp.arg(1 - z) * mp.log(mp.fabs(z))


# ── Color-tube cubic roots at fixed z (the 3 color sheets c_r,c_g,c_b) ─
# F(c,z)=c³+(4z+1)c²+(6z²+3z+1)c+(4z³+3z²+2z+1)  (def:color-tube-cubic)
def color_tube_roots(z):
    """Three roots (color sheets) of the color-tube cubic at fixed z."""
    z = mp.mpc(z)
    coeffs = [
        mp.mpf(1),
        4 * z + 1,
        6 * z ** 2 + 3 * z + 1,
        4 * z ** 3 + 3 * z ** 2 + 2 * z + 1,
    ]
    return mp.polyroots(coeffs, maxsteps=400, extraprec=300)


def _sort_roots(roots):
    """Return (real_root, conj_plus, conj_minus) for a real-z cubic with
    negative discriminant: exactly one real root, one conjugate pair.
    conj_plus has Im > 0. If all three are real (positive discriminant),
    returns them sorted by Re with the convention (r0, r1, r2)."""
    reals = [r for r in roots if mp.fabs(mp.im(r)) < mp.mpf("1e-30")]
    cplx = [r for r in roots if mp.fabs(mp.im(r)) >= mp.mpf("1e-30")]
    if len(cplx) == 2:
        plus = cplx[0] if mp.im(cplx[0]) > 0 else cplx[1]
        minus = cplx[1] if mp.im(cplx[0]) > 0 else cplx[0]
        return reals[0], plus, minus, "one_real_one_pair"
    rs = sorted(roots, key=lambda r: mp.re(r))
    return rs[0], rs[1], rs[2], "all_real"


# ── Nucleon flavor content (uud / udd over the 3 color sheets) ─────────
# proton (uud): sheet flavors (u, u, d)
# neutron (udd): sheet flavors (u, d, d)
PROTON = ("u", "u", "d")
NEUTRON = ("u", "d", "d")


def _zget(name):
    """Substrate z = q0 (real), and the figure-8 cusp shape e^{iπ/3}."""
    if name == "q0":
        q, _, _ = load_q_50dps()
        return q
    raise ValueError(name)


def D_of_color_root_as_shape(c):
    """Candidate (b)-naive: treat the color-tube root c directly as a
    shape parameter and evaluate D(c). NOT geometrically a tetrahedron
    cross-ratio, recorded only to expose the conjugate-pair structure."""
    return bloch_wigner(c)


# ── Mechanism (b): per-strand color-tube root assignment by flavor ─────
# The 3 color sheets carry roots {c_real, c_+, c_−}. A flavor→sheet
# assignment is a map from the quark-flavor triple to which root each
# strand's shape uses. Σ D over the three strands. We enumerate the
# DERIVED-candidate assignment rules and check whether ANY gives a
# nonzero p/n difference WITHOUT a free choice tuned to the split.
def sum_D_strands(flavor_triple, root_map):
    """root_map: dict 'u'->root, 'd'->root. Σ D over the 3 strands."""
    return sum(bloch_wigner(root_map[f]) for f in flavor_triple)


def main():
    out = {}
    q = _zget("q0")
    out["q0"] = mp.nstr(q, 50)
    out["dps"] = mp.mp.dps

    # ====================================================================
    # FACT 0: color-tube cubic root structure at the real substrate z=q0
    # ====================================================================
    roots = color_tube_roots(q)
    c_real, c_plus, c_minus, kind = _sort_roots(roots)
    out["cubic_root_structure"] = {
        "z": mp.nstr(q, 30),
        "kind": kind,
        "c_real": mp.nstr(mp.re(c_real), 30),
        "c_plus": [mp.nstr(mp.re(c_plus), 30), mp.nstr(mp.im(c_plus), 30)],
        "c_minus": [mp.nstr(mp.re(c_minus), 30), mp.nstr(mp.im(c_minus), 30)],
        "note": (
            "At any real z the color-tube cubic (negative discriminant) "
            "has exactly ONE real root and ONE complex-conjugate pair "
            "c_± = x ± iy. The three roots ARE the three color sheets "
            "(c_r,c_g,c_b); flavor decorates which sheet a strand carries."
        ),
    }

    # D on each color-tube root (exposes conjugate-pair antisymmetry)
    D_real = bloch_wigner(c_real)
    D_plus = bloch_wigner(c_plus)
    D_minus = bloch_wigner(c_minus)
    out["D_on_color_roots"] = {
        "D_c_real": mp.nstr(D_real, 30),
        "D_c_plus": mp.nstr(D_plus, 30),
        "D_c_minus": mp.nstr(D_minus, 30),
        "D_plus_plus_minus": mp.nstr(D_plus + D_minus, 30),
        "D_real_is_zero": bool(mp.fabs(D_real) < mp.mpf("1e-25")),
        "pair_cancels": bool(mp.fabs(D_plus + D_minus) < mp.mpf("1e-25")),
        "note": (
            "D(real root)=0 (D vanishes on real args). The conjugate pair "
            "obeys D(z̄)=−D(z) so D(c_+)+D(c_-)=0. Total Σ D over all "
            "three roots = 0 — the universal cubic carries NO net volume."
        ),
    }
    sum_D_all = D_real + D_plus + D_minus
    out["D_on_color_roots"]["sum_D_all_three"] = mp.nstr(sum_D_all, 30)

    # ====================================================================
    # MECHANISM (b): per-strand root assignment by flavor.
    # The flavor triple selects, for each strand, WHICH root is its shape.
    # Enumerate the candidate DERIVED assignment rules.
    # ====================================================================
    # Rule b1: flavor → fixed sheet color. The standard color-tube reading
    # assigns u→one sheet, d→another. But a flavor triple uud just
    # PERMUTES three sheets that already each carry one of {c_real,c_+,c_-}.
    # Whatever bijection strand→sheet, the MULTISET of shapes used by p and
    # n is the SAME three roots {c_real,c_+,c_-} (each nucleon has 3 sheets,
    # the cubic has exactly 3 roots). So Σ D over strands = Σ D over roots
    # = 0 for BOTH p and n — independent of the flavor labeling.
    out["mechanism_b1_one_sheet_per_root"] = {
        "claim": (
            "Each nucleon has exactly 3 color sheets; the cubic has exactly "
            "3 roots. Any strand→sheet→root bijection uses the SAME root "
            "multiset {c_real,c_+,c_-} for both p and n. Σ D is the SAME "
            "(=0) for proton and neutron — flavor only PERMUTES the sum."
        ),
        "sum_D_proton": mp.nstr(sum_D_all, 30),
        "sum_D_neutron": mp.nstr(sum_D_all, 30),
        "pn_difference": mp.nstr(mp.mpf(0), 5),
        "is_derived": True,
        "carries_pn": False,
    }

    # Rule b2: flavor → root selection (same flavor uses same root). A
    # genuinely flavor-DISCRIMINATING rule must map 'u' and 'd' to
    # DIFFERENT roots, and reuse a root when a flavor repeats. e.g.
    #   u -> c_plus, d -> c_real  (or any 2-of-3 selection)
    # Then proton (u,u,d) uses {c_plus, c_plus, c_real}; neutron (u,d,d)
    # uses {c_plus, c_real, c_real}. These ARE different multisets → the
    # Σ D differ. BUT: which root maps to 'u' vs 'd' is a CHOICE with no
    # derivation. We enumerate ALL 3·2=6 injective two-root selections and
    # report the p/n difference for each, FLAGGING that the selection rule
    # is not derived (it is the missing categorical input).
    selections = []
    root_named = {"c_real": c_real, "c_plus": c_plus, "c_minus": c_minus}
    names = list(root_named.keys())
    for u_name in names:
        for d_name in names:
            if u_name == d_name:
                continue  # must discriminate flavor
            rmap = {"u": root_named[u_name], "d": root_named[d_name]}
            sD_p = sum_D_strands(PROTON, rmap)
            sD_n = sum_D_strands(NEUTRON, rmap)
            selections.append({
                "u_root": u_name,
                "d_root": d_name,
                "sum_D_proton": mp.nstr(mp.re(sD_p), 25),
                "sum_D_neutron": mp.nstr(mp.re(sD_n), 25),
                "pn_difference": mp.nstr(mp.re(sD_p - sD_n), 25),
                "pn_diff_imag": mp.nstr(mp.im(sD_p - sD_n), 10),
            })
    out["mechanism_b2_flavor_root_selection"] = {
        "selections": selections,
        "derivation_status": "NOT DERIVED",
        "note": (
            "A flavor-discriminating rule (u and d map to DIFFERENT roots) "
            "DOES give a nonzero p/n Σ D difference — because p=(u,u,d) and "
            "n=(u,d,d) then use different root multisets. BUT the choice of "
            "WHICH root is 'u' vs 'd' is a free 2-of-3 selection with NO "
            "categorical derivation. Every entry here is a LATENT FIT: the "
            "selection rule is exactly the missing input. The difference is "
            "D(c_+ or c_-)−D(c_real)=±D(c_±) (since D(c_real)=0), i.e. it is "
            "merely +D(c_+) or its negation — set by the unjustified choice "
            "of sign/root, not by the quark content."
        ),
    }

    # ====================================================================
    # MECHANISM (a): flavored cusp decoration. Does the flavor modify the
    # Thurston cusp shape z_k itself? The cusp shape is fixed by the
    # complement's hyperbolic structure (m004/m003/L6a4 give z=e^{iπ/3} or
    # (1+i)/2 INDEPENDENT of the algebraic seed — snappy-cusp-seeding).
    # A flavored Dehn FILLING would change the manifold (filled cusp →
    # different volume), but p and n are the SAME unfilled ℬ_3 complement.
    # There is no derived map flavor → meridian/longitude eigenvalue.
    # We record the canonical shapes and confirm they are flavor-blind.
    # ====================================================================
    z_fig8 = mp.e ** (1j * mp.pi / 3)  # figure-8 cusp shape
    z_borr = mp.mpc("0.5", "0.5")      # ideal octahedron corner (L6a4)
    out["mechanism_a_cusp_decoration"] = {
        "z_figure8": [mp.nstr(mp.re(z_fig8), 20), mp.nstr(mp.im(z_fig8), 20)],
        "D_figure8_x2": mp.nstr(2 * bloch_wigner(z_fig8), 30),
        "two_Cl2_pi3": mp.nstr(2 * mp.clsin(2, mp.pi / 3), 30),
        "vol_borromean_8G": mp.nstr(8 * mp.catalan, 30),
        "note": (
            "Thurston cusp shapes are fixed by the topological complement "
            "(snappy-cusp-seeding: m004/m003 → e^{iπ/3}, L6a4 → (1+i)/2, "
            "INDEPENDENT of the algebraic seed). Proton and neutron are the "
            "SAME unfilled ℬ_3 complement → SAME shapes → SAME Σ D. There "
            "is NO derived map flavor → meridian/longitude holonomy "
            "eigenvalue. A flavored Dehn FILLING would change the manifold, "
            "but that is not the QOU nucleon model (both are unfilled ℬ_3)."
        ),
        "carries_pn": False,
        "is_derived": False,
    }

    # ====================================================================
    # RAW falsification reference (NOT a fit target): the magnitude of the
    # color-tube-root D values vs the physical isospin split. Report raw.
    # ====================================================================
    out["raw_reference"] = {
        "abs_D_c_plus": mp.nstr(mp.fabs(D_plus), 20),
        "m_n_minus_m_p_MeV": "1.293332",  # PDG, falsification ref ONLY
        "delta_over_mp_ppm": "1378",      # (m_n−m_p)/m_p in ppm, ref ONLY
        "note": (
            "D(c_+) ≈ O(1) is a pure dimensionless hyperbolic volume; the "
            "physical isospin split is 1.29 MeV ≈ 1378 ppm of m_p. These "
            "are NOT comparable without the full VolDensity/m_e MeV chain, "
            "and NO value here is tuned to the split. Listed for "
            "falsification scope only."
        ),
    }

    # ====================================================================
    # VERDICT
    # ====================================================================
    out["VERDICT"] = (
        "NO DERIVED flavor→complex-shape map reaches Σ D (the K_3 "
        "Bloch-Wigner volume). Three structural facts: (0) at real z the "
        "color-tube cubic has one real root + one conjugate pair, and "
        "D(real)=0, D(c_+)+D(c_-)=0 ⇒ Σ D over the 3 roots = 0. "
        "(b1) each nucleon has 3 color sheets = the 3 cubic roots; any "
        "strand→root bijection uses the SAME root multiset for p and n, so "
        "Σ D is identical (=0) — flavor only PERMUTES. (b2) a flavor-"
        "DISCRIMINATING rule (u,d → different roots) DOES split p/n, but "
        "the root-selection is a free 2-of-3 CHOICE with no derivation — a "
        "latent fit, and the split is just ±D(c_±) set by the unjustified "
        "sign. (a) Thurston cusp shapes are fixed by the topological "
        "complement (flavor-blind); p and n are the same unfilled ℬ_3, no "
        "derived flavor→holonomy-eigenvalue map exists. The PRECISE "
        "missing categorical object is a DERIVED per-strand flavor→root "
        "(equivalently flavor→meridian-eigenvalue) selection rule whose "
        "sign/root is fixed by the quark content — i.e. a flavored "
        "decoration of the color sheets that is currently UNDEFINED. This "
        "is the same gap conj:inter-nucleon-channel-color-tube names on "
        "the REAL (K_1) side, now shown to be exactly what blocks the K_3 "
        "side too. CLEAN NEGATIVE; does not close or advance L2 numerically."
    )

    wpath = (
        WitnessBuilder.wrap_legacy(
            "flavor-dependent-cusp-shape",
            out,
            script_path=__file__,
            engine="mpmath",
            start_time=_START,
        )
        .set_audit_only("docs/audits/2026-06-01-flavor-dependent-cusp-shape.md")
        .save()
    )
    print(f"Wrote {wpath}")
    print("Root structure:", kind)
    print("D(c_real)=", mp.nstr(D_real, 10),
          " D(c_+)+D(c_-)=", mp.nstr(D_plus + D_minus, 10))
    print("b2 first selection p/n diff:",
          out["mechanism_b2_flavor_root_selection"]["selections"][0]["pn_difference"])
    print("VERDICT:", out["VERDICT"][:160], "...")


if __name__ == "__main__":
    main()
