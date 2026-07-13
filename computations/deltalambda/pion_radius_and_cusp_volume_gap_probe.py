#!/usr/bin/env python3
"""
pion_radius_and_cusp_volume_gap_probe.py — R2-e: attack the TWO named underived
steps of the continuum-EM mirror-split result
(docs/audits/2026-07-13-mirror-split-continuum-em-derivation-attempt.md):

  GAP 1 — the Yukawa packing radius: why is the per-nucleon packing length the
          pion Compton wavelength λ̄_π = ℏ/(m_π c) at coefficient EXACTLY 1
          (measured 0.985 ± 0.069)?
  GAP 2 — the hyperbolic-volume→Euclidean-radius identification behind A^{1/3}.

FORMALIZE-FIRST (compute-author §3.3) — the structural arguments come BEFORE the
numbers; the probe verifies them, it does not search for them. No scan, no fit.

GAP 1 candidates:
  (a) CLASS-SELECTION (the centerpiece). The corpus supplies three independent
      identifications that, composed, DERIVE the scale-class of the packing
      length (though not its coefficient):
        (a1) the inter-nucleon bond of the bond-count law is a 2-body (n=2)
             sub-link = the HOPF link, with Vol(Hopf) = 0 — geometric fact
             (binding-scale-is-hyperbolic-volume.md ledger row;
              degree-one-braid-trivial-volume-proof.md; SnapPy live check);
        (a2) the W-plane classes (CAL-1 scale m_e + CAL-2 modulus q₀) enter
             per-link binding ONLY through m_e·Vol(K) (the ledger
             identification) and the dimensionless modulus — so on the bond
             channel the W-plane contribution is m_e·Vol(Hopf) = 0
             IDENTICALLY, and q₀ alone supplies no length;
        (a3) CAL-3 is characterized in the corpus as EXACTLY "the
             Vol(Hopf) = 0 meson scale (independent of m_e, q₀)"
             (three-calibration-discipline.md §table), and the meson binding
             channel is "Hopf link binding" (frobenius-lepton-meson-bridge.md);
             the mass functional 𝔪 = m_e^a·m_π^c·Q(q₀) gives c = 0 in the
             baryon sector — m_μ and m_p are W-plane (a=1, c=0) objects.
      Composition: the only calibration class with nonzero support on the
      Vol = 0 inter-nucleon (Hopf) channel is CAL-3 ⇒ the bond's length unit
      is ℏc/(m_π·Q(q₀)) with Q ∈ ℚ(q₀). The parent audit's "2-bit selection
      among 4 mass scales" collapses to a 0-bit CLASS selection — this is the
      categorical face of the Yukawa-range identification. CONDITIONAL on the
      same ledger identification (B = m_e·Vol, per-link volume conjecture
      instances) that GAP 2 rides on; assembled from corpus identifications,
      NOT a Lean-proved theorem.
  (b) 2-BODY ENERGY→LENGTH (negative). The deuteron channel energies
      (B_D = 2.2246 MeV AME; the derived per-crossing scale
      μ₀ = m_e/(3(q₀−q₀⁻¹)/2) ≈ 1.63 MeV) give Compton lengths ℏc/E of
      ~89–121 fm — 60–90× λ̄_π. The packing length is NOT the inverse of the
      bond energy. Scope-(a) negative.
  (c) COEFFICIENT-1 STATUS (the honest confrontation). The measured 0.985 ±
      0.069 is consistent with 1 at 0.22σ — but ALSO with ≥ 7 other simple
      Q(q₀) values (1/q₀, √q₀, [2]_q/2, 1−ℏ_q², …) within 1.25σ. At the 7%
      systematics scatter the data CANNOT select "exactly 1"; distinguishing
      1 from 1−ℏ_q² at 3σ needs ~0.3% scatter (≈ 21× better). "One CAL-3
      quantum per bond" is a minimality reading, not a derivation.

GAP 2 candidates:
  (d) ARCHIMEDEAN-FUNCTOR TRANSPORT (negative, documentary). The functor-
      taxonomy audit (2026-07-11-archimedean-functor-taxonomy.md) shows every
      "archimedean functor" is an evaluation/ring hom into ℝ — there is NO
      categorical volume→length transport in the corpus. All corpus lengths
      arise as Compton inversions ℏc/mass. USEFUL RE-SCOPING: R = λ̄_π·A^{1/3}
      is algebraically identical to the pure-MeV statement
      E_pack(A) = m_π·A^{−1/3}; the "Euclidean radius" need not exist as a
      categorical object — the gap is the A^{−1/3} ENERGY exponent, not a
      geometry-type transport.
  (e) CUSP-VOLUME ROUTE (partial; negative-leaning on the numbers). Cusp
      cross-sections of hyperbolic link complements ARE Euclidean tori
      (horosphere geometry — theorem), so a cusp-based packing volume removes
      the "hyperbolic behaves like Euclidean" category error. But:
        (e1) cusp-count extensivity FAILS on the corpus's own A=3 links
             (³H = 8₁₁ is a KNOT: 1 cusp for 3 nucleons; ³He = L6a4 has 3);
        (e2) maximal-cusp volume per nucleon varies 1.32–2.01 (±20%) and cusp
             density varies 0.604–0.853 (1.41×) across the corpus family — NOT
             more uniform than complement volume;
        (e3) face-value coefficients: per-nucleon Borromean cusp volume
             (exactly 2 in hyperbolic units) ⇒ radius coefficient
             (3·2/4π)^{1/3} = 0.782 (2.9σ low); whole-𝓑₃ cusp volume 6 ⇒
             1.127 (2.1σ high; 1.4σ in ratio-space); the measured coefficient
             needs a per-nucleon Euclidean volume of 4.38·λ̄_π³ — between the
             two, matching neither pinned normalization. Selecting a
             normalization post-hoc to land on 1 would be the
             PSLQ-coincidence antipattern; NOT done.

ANTI-FIT: nothing tuned; every candidate value is pinned in advance by a named
structural object; negatives are scope-(a); no production wiring, no content-
block change. EXPLORATORY.

Run:  python3 -u pion_radius_and_cusp_volume_gap_probe.py [--live]
      (--live re-verifies the baked SnapPy 3.3.2 cusp data)
"""
from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent          # computations/deltalambda/
_COMP = _HERE.parent                             # computations/
for _d in (_HERE, _COMP, _COMP / "substrate", _COMP / "hecke", _COMP / "habiro"):
    _p = str(_d)
    if _p not in sys.path:
        sys.path.insert(0, _p)
import _path_bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from codata_constants import (  # noqa: E402
    _ame_binding_mev,
    M_E_MEV,
    M_PI_PM_MEV_VALIDATION,
)
# Reuse the parent probe's exact code paths (no duplication):
from mirror_split_continuum_em_probe import (  # noqa: E402
    PAIRS,
    alpha_derived,
    pred_continuum,
    split_ame,
    q0,
    M_MU_MEV,
    M_P_MEV,
    HBAR_C_MEV_FM,
)

try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except ImportError:
    WitnessBuilder = None
    _HAVE_WB = False

set_compute_dps()

# ── Baked SnapPy 3.3.2 cusp geometry (2026-07-13; --live reproduces) ─────────
# cusp areas via Manifold(name).cusp_areas(policy='unbiased'); maximal-cusp
# volume = area/2 (horoball neighborhood). Exact forms noted where recognised.
CUSP = {
    # name: (n_cusps, complement vol, per-cusp area, corpus role, A-assignment)
    "4_1":   (1, 2.029883212819307, 3.464101615137751,   # 2√3 ⇒ cusp vol √3
              "muon anchor (figure-8)", 1),
    "L6a4":  (3, 7.327724753417752, 4.000000000000000,   # EXACT 4 ⇒ cusp vol 2
              "3He binding link / B3 nucleon (Borromean)", 3),
    "8_11":  (1, 8.286316817806592, 10.013094699147005,  # single cusp
              "3H binding link (knot!)", 3),
    "L8a21": (4, 10.149416064096537, 3.464101615137757,  # 2√3 per cusp
              "linear 4-chain (vol4 probe family)", 4),
    "L8a20": (3, 10.149416064096535, 4.898979485566350,  # 2√6 per cusp
              "3-component 8-crossing chain (vol4 family)", 4),
    "L6a5":  (3, 5.333489566898119, 2.645751311064590,   # √7 per cusp
              "3-chain link (magic manifold)", 3),
}
# Hopf link L2a1: SnapPy solution type 'contains degenerate tetrahedra',
# vol = 0 (non-hyperbolic) — the (a1) geometric fact.
HOPF_VOL = 0.0


def run_live() -> None:
    """Re-verify the baked cusp data + Hopf non-hyperbolicity with SnapPy."""
    import snappy  # noqa: PLC0415
    for nm, (nc, vol, area, _role, _A) in CUSP.items():
        M = snappy.Manifold(nm)
        assert M.num_cusps() == nc, (nm, "cusp count")
        assert abs(float(M.volume()) - vol) < 1e-9, (nm, "volume")
        live_areas = [float(a) for a in M.cusp_areas(policy="unbiased")]
        for a in live_areas:
            assert abs(a - area) < 1e-6, (nm, "cusp area", a, area)
    H = snappy.Manifold("L2a1")
    assert "degenerate" in H.solution_type() or abs(float(H.volume())) < 1e-6
    print("  [--live] SnapPy 3.3.2 re-verification: all baked values match.\n")


def main() -> int:
    live = "--live" in sys.argv[1:]
    print("=== R2-e: the pion packing radius (GAP 1) and the volume→radius "
          "step (GAP 2) ===\n")
    if live:
        run_live()

    m_pi = M_PI_PM_MEV_VALIDATION
    m_e = M_E_MEV
    a_der = alpha_derived(q0)
    lam_pi_fm = HBAR_C_MEV_FM / m_pi
    hbar_q = 1 - 1 / q0

    # ── measured packing coefficient (recomputed via the parent's code path) ─
    ratios = [split_ame(Z1, Z2, A) / pred_continuum(A, Z1, Z2, a_der, m_pi)
              for _, Z1, Z2, A in PAIRS]
    mean_r = sum(ratios) / len(ratios)
    rms = mp.sqrt(sum((r - mean_r) ** 2 for r in ratios) / len(ratios))
    monotone = all(ratios[i] < ratios[i + 1] for i in range(len(ratios) - 1))
    print(f"measured packing coefficient (8 T_z mirror pairs, parent probe path):"
          f" {float(mean_r):.3f} ± {float(rms):.3f}"
          f"  (A-trend monotone: {monotone}, "
          f"{float(ratios[0]):.3f}→{float(ratios[-1]):.3f})\n")

    # ═════ GAP 1 (a): class selection — W-plane annihilation on the bond ════
    print("── GAP 1 (a): scale-CLASS selection (the Yukawa identification, "
          "categorically) ──")
    wplane_bond = m_e * mp.mpf(HOPF_VOL)          # m_e·Vol(Hopf)
    print(f"  (a1) bond sub-link = Hopf, Vol(Hopf) = {HOPF_VOL} "
          f"(non-hyperbolic; ledger row; SnapPy{' live' if live else ' baked'})")
    print(f"  (a2) W-plane contribution to the bond channel = m_e·Vol(Hopf) = "
          f"{float(wplane_bond)} MeV — IDENTICALLY ZERO; q₀ is dimensionless")
    print("  (a3) CAL-3 is corpus-defined as 'the Vol(Hopf)=0 meson scale "
          "(independent of m_e, q₀)';")
    print("       meson binding channel = 'Hopf link binding' "
          "(frobenius-lepton-meson-bridge);")
    print("       mass functional m_e^a·m_π^c·Q(q₀) has c=0 in the baryon "
          "sector ⇒ m_μ, m_p are W-plane objects")
    print("  ⇒ the ONLY calibration class with nonzero support on the Vol=0 "
          "bond channel is CAL-3:")
    print("    bond length unit = ℏc/(m_π·Q(q₀)),  Q ∈ ℚ(q₀).  The 2-bit "
          "mass-scale selection collapses")
    print("    to a 0-bit CLASS selection (conditional on the B = m_e·Vol "
          "ledger identification).\n")

    # selection table recompute (the parent's 4-scale table, reread as (a)):
    sel = {}
    for lbl, m in [("m_e (CAL-1, W-plane)", m_e),
                   ("m_mu (CAL-2 proxy, W-plane a=1)", M_MU_MEV),
                   ("m_pi (CAL-3, orthogonal class)", m_pi),
                   ("m_p (baryon c=0, W-plane a=1)", M_P_MEV)]:
        rs = [split_ame(Z1, Z2, A) / pred_continuum(A, Z1, Z2, a_der, m)
              for _, Z1, Z2, A in PAIRS]
        sel[lbl] = float(sum(rs) / len(rs))
        print(f"    {lbl:<34}: coefficient needed = {sel[lbl]:>9.3f}")
    only_pi_near_1 = sum(1 for v in sel.values() if abs(v - 1) < 0.25) == 1 \
        and abs(sel["m_pi (CAL-3, orthogonal class)"] - 1) < 0.25
    print(f"    unique scale within ±25% of 1: m_π only "
          f"[{'PASS' if only_pi_near_1 else 'FAIL'}] — and it is the unique "
          f"non-W-plane class\n")

    # ═════ GAP 1 (b): 2-body channel energies do NOT give the length ════════
    print("── GAP 1 (b): length from the 2-body (deuteron) channel — "
          "NEGATIVE ──")
    B_D = mp.mpf(str(_ame_binding_mev(1, 2)))     # deuteron binding, AME
    mu0 = m_e / (3 * (q0 - 1 / q0) / 2)           # derived per-crossing scale
    len_BD = HBAR_C_MEV_FM / B_D
    len_mu0 = HBAR_C_MEV_FM / mu0
    print(f"    λ̄_π = ℏc/m_π                = {float(lam_pi_fm):9.4f} fm")
    print(f"    ℏc/B_D  (B_D = {float(B_D):.4f} MeV) = {float(len_BD):9.2f} fm"
          f"  = {float(len_BD / lam_pi_fm):6.1f}× λ̄_π")
    print(f"    ℏc/μ₀   (μ₀  = {float(mu0):.4f} MeV) = {float(len_mu0):9.2f} fm"
          f"  = {float(len_mu0 / lam_pi_fm):6.1f}× λ̄_π")
    two_body_neg = min(len_BD, len_mu0) / lam_pi_fm > 50
    print(f"    2-body channel ENERGIES give 60–90× λ̄_π — they are binding "
          f"scales, not range scales [scope-(a) NEGATIVE: "
          f"{'PASS' if two_body_neg else 'FAIL'}]\n")

    # ═════ GAP 1 (c): coefficient-1 status — confronted head-on ═════════════
    print("── GAP 1 (c): what selects coefficient EXACTLY 1? (honest "
          "discrimination table) ──")
    cands = {
        "1 (one CAL-3 quantum/bond)": mp.mpf(1),
        "q0": q0,
        "1/q0": 1 / q0,
        "sqrt(q0)": mp.sqrt(q0),
        "1/sqrt(q0)": 1 / mp.sqrt(q0),
        "[2]_q/2 = (q0+1/q0)/2": (q0 + 1 / q0) / 2,
        "(1+1/q0)/2": (1 + 1 / q0) / 2,
        "1+hbar_q^2": 1 + hbar_q ** 2,
        "1-hbar_q^2": 1 - hbar_q ** 2,
    }
    n_within = 0
    for lbl, v in cands.items():
        d = abs(v - mean_r) / rms
        n_within += int(d < mp.mpf("1.25"))
        print(f"    Q(q0) = {lbl:<28}: value {float(v):8.5f}   "
              f"|Q − measured|/rms = {float(d):5.2f}σ"
              f"{'   ← within 1.25σ' if d < mp.mpf('1.25') else ''}")
    d_one = abs(mp.mpf(1) - mean_r) / rms
    # scatter needed to separate 1 from its nearest rival at 3σ:
    gaps = sorted(abs(v - 1) for lbl, v in cands.items() if v != 1)
    scatter_needed = gaps[0] / 3
    print(f"    coefficient 1 is consistent at {float(d_one):.2f}σ — but "
          f"{n_within}/{len(cands)} candidates sit within 1.25σ.")
    print(f"    Separating 1 from its nearest rival (Δ = {float(gaps[0]):.4f}) "
          f"at 3σ needs scatter ≤ {float(100 * scatter_needed):.2f}% "
          f"(current {float(100 * rms / mean_r):.1f}% — "
          f"{float((rms / mean_r) / scatter_needed):.0f}× too coarse).")
    print("    ⇒ 'coefficient exactly 1' is UNDERIVED and currently "
          "UNDISCRIMINABLE; the class argument (a)")
    print("      fixes the unit to m_π·Q(q₀) — the residual freedom is Q, "
          "not the mass scale.\n")

    # ═════ GAP 2 (d): no functorial volume→length transport; re-scoping ═════
    print("── GAP 2 (d): archimedean-functor transport — NEGATIVE, with a "
          "re-scoping ──")
    print("    Taxonomy audit (2026-07-11): every 'archimedean functor' is an "
          "evaluation/ring hom into ℝ;")
    print("    NO categorical volume→length transport exists. All corpus "
          "lengths are Compton inversions ℏc/mass.")
    # algebraic identity: the radius law never needs a length object —
    #   (3/5)·α·ΔZZ·ℏc/(λ̄_π·A^{1/3}) ≡ (3/5)·α·ΔZZ·m_π·A^{-1/3}
    lhs = HBAR_C_MEV_FM / (lam_pi_fm * mp.cbrt(7))
    rhs = m_pi / mp.cbrt(7)
    resc_ok = abs(lhs / rhs - 1) < mp.mpf("1e-40")
    print(f"    Re-scoping identity ℏc/(λ̄_π·A^(1/3)) = m_π·A^(-1/3) "
          f"[{'PASS' if resc_ok else 'FAIL'}]: the gap is the A^(-1/3)")
    print("    ENERGY exponent (a pure-MeV statement inside the calibration "
          "discipline), not a geometry-type transport.\n")

    # ═════ GAP 2 (e): the cusp-volume route (Euclidean tori) ════════════════
    print("── GAP 2 (e): cusp volumes — Euclidean cross-sections, honest "
          "numbers ──")
    print("    (cusp cross-sections are flat tori — horosphere geometry, "
          "theorem; the Euclidean-ness is genuine)")
    print(f"    {'link':<7}{'cusps':>6}{'Vol':>10}{'cusp vol':>10}"
          f"{'density':>9}{'A':>4}{'cusp vol/A':>12}   role")
    dens, per_nuc = {}, {}
    for nm, (nc, vol, area, role, A) in CUSP.items():
        cv = nc * area / 2
        dens[nm] = cv / vol
        per_nuc[nm] = cv / A
        print(f"    {nm:<7}{nc:>6}{vol:>10.4f}{cv:>10.4f}{dens[nm]:>9.4f}"
              f"{A:>4}{per_nuc[nm]:>12.4f}   {role}")
    bor_per_cusp = CUSP["L6a4"][2] / 2            # exactly 2
    e1 = abs(bor_per_cusp - 2) < 1e-9
    e2 = CUSP["8_11"][0] != 3                     # cusp count ≠ nucleon count
    dens_spread = max(dens.values()) / min(dens.values())
    e3 = dens_spread > 1.3
    print(f"\n    Borromean per-cusp maximal-cusp volume = {bor_per_cusp} "
          f"(EXACT 2 in hyperbolic units) [{'PASS' if e1 else 'FAIL'}]")
    print(f"    cusp-count extensivity at ³H: 8₁₁ has "
          f"{CUSP['8_11'][0]} cusp for A = 3 nucleons — FAILS on the corpus's "
          f"own link [{'PASS' if e2 else 'FAIL'}]")
    print(f"    cusp-density spread across the family: "
          f"{min(dens.values()):.3f}–{max(dens.values()):.3f} "
          f"(×{dens_spread:.2f}) — NOT more uniform than complement volume "
          f"[{'PASS' if e3 else 'FAIL'}]")

    # face-value coefficients (pinned in advance; no post-hoc normalization):
    def coeff_of_volume(V):
        """radius coefficient c s.t. R = c·λ̄_π·A^{1/3} for per-nucleon
        Euclidean volume V·λ̄_π³ (sphere packing: (4π/3)(cA^{1/3})³ = V·A)."""
        return mp.cbrt(3 * mp.mpf(V) / (4 * mp.pi))

    c_percusp = coeff_of_volume(2.0)              # Borromean per-cusp
    c_b3total = coeff_of_volume(6.0)              # whole-B3 cusp volume
    V_required = (4 * mp.pi / 3) * (1 / mean_r) ** 3
    # coefficient-space distances — the SAME metric as the (c) table:
    d_percusp = abs(c_percusp - mean_r) / rms
    d_b3total = abs(c_b3total - mean_r) / rms
    # alternate (ratio-space) normalization, reported for honesty:
    d_b3_alt = abs(mean_r * c_b3total - 1) / (rms * c_b3total)
    print(f"\n    face-value radius coefficients (R = c·λ̄_π·A^(1/3)); "
          f"distances in the (c)-table coefficient-space metric:")
    print(f"      per-nucleon cusp vol 2.0·λ̄_π³ (Borromean) ⇒ c = "
          f"{float(c_percusp):.4f} → miss {float(d_percusp):.1f}σ (low)")
    print(f"      whole-𝓑₃ cusp vol 6.0·λ̄_π³             ⇒ c = "
          f"{float(c_b3total):.4f} → miss {float(d_b3total):.1f}σ (high; "
          f"{float(d_b3_alt):.1f}σ in ratio-space)")
    print(f"      measured coefficient needs per-nucleon Euclidean volume "
          f"{float(V_required):.2f}·λ̄_π³ — between the two;")
    print(f"      available per-nucleon cusp volumes are 1.32–2.01. Neither "
          f"pinned normalization matches at 1σ;")
    print(f"      selecting one post-hoc would be the PSLQ-coincidence "
          f"antipattern — NOT done.")
    e4 = min(d_percusp, d_b3total) > mp.mpf("1.5")

    # ═════ verdicts ══════════════════════════════════════════════════════════
    print("\nVERDICTS (scope-(a) throughout; nothing wired):")
    print("  GAP 1: PARTIAL, substantially narrowed — the scale-CLASS is now "
          "derived at the structural level")
    print("    (W-plane annihilation on the Vol=0 Hopf bond ⇒ CAL-3 is the "
          "unique surviving class; 2 bits → 0 bits),")
    print("    CONDITIONAL on the B = m_e·Vol ledger identification. The "
          "COEFFICIENT (Q(q₀) = 1) stays underived and")
    print("    is undiscriminable at 7% scatter (8/9 simple Q within 1.25σ). "
          "2-body energy→length: negative.")
    print("  GAP 2: OPEN, re-scoped — no functorial volume→length transport "
          "exists (taxonomy audit); the honest gap is")
    print("    the A^(-1/3) ENERGY exponent. The cusp route removes the "
          "geometry-type category error (cusp tori are")
    print("    Euclidean) but fails cusp-count extensivity at ³H, shows 1.41× "
          "density spread, and its two pinned")
    print(f"    normalizations miss the measured coefficient at "
          f"{float(d_percusp):.1f}σ / {float(d_b3total):.1f}σ "
          f"(coefficient-space).")

    # ═════ witness ═══════════════════════════════════════════════════════════
    ok = True
    asserts = [
        ("hopf_bond_wplane_annihilated", int(float(wplane_bond) == 0.0), 1,
         "m_e·Vol(Hopf) = 0 identically — the W-plane (CAL-1×CAL-2) classes "
         "have zero support on the 2-body inter-nucleon bond channel "
         "(Hopf non-hyperbolic; ledger identification B = m_e·Vol)"),
        ("cal3_unique_surviving_class", int(only_pi_near_1), 1,
         "the 4-scale selection table re-read: m_pi is the unique scale whose "
         "required coefficient is within 25% of 1 AND the unique non-W-plane "
         "calibration class — the 2-bit selection collapses to class selection"),
        ("coefficient_one_consistent", int(d_one < 1), 1,
         f"|1 − measured|/rms = {float(d_one):.2f}σ < 1σ — coefficient 1 is "
         "consistent with the 8-pair systematics"),
        ("coefficient_not_uniquely_selected", int(n_within >= 4), 1,
         f"{n_within}/9 simple Q(q0) candidates within 1.25σ of the measured "
         "coefficient — 'exactly 1' is NOT selected by the data at 7% scatter "
         "(honesty assertion; needs ~0.3% scatter to discriminate at 3σ)"),
        ("two_body_energy_length_negative", int(two_body_neg), 1,
         "hbar*c/B_D and hbar*c/mu0 are 60-90x lambda_pi — the packing length "
         "is not the inverse of a 2-body channel energy (scope-(a))"),
        ("radius_energy_rescoping_identity", int(resc_ok), 1,
         "hbar*c/(lambda_pi*A^(1/3)) = m_pi*A^(-1/3) exactly — GAP 2 re-scopes "
         "to the A^(-1/3) energy exponent; no length object needed"),
        ("borromean_per_cusp_volume_two", int(e1), 1,
         "Borromean maximal-cusp volume per cusp = 2 exactly (area 4, "
         "SnapPy unbiased policy) — the candidate Euclidean packing unit"),
        ("cusp_count_extensivity_fails_3h", int(e2), 1,
         "8_11 (the corpus 3H binding link) is a knot: 1 cusp for A=3 — "
         "cusp-per-nucleon extensivity fails on the corpus's own links"),
        ("cusp_density_not_constant", int(e3), 1,
         f"maximal-cusp density spread x{dens_spread:.2f} (0.604-0.853) across "
         "the corpus family — cusp volume is NOT more uniformly extensive than "
         "complement volume"),
        ("cusp_facevalue_coefficients_miss", int(e4), 1,
         f"both pinned cusp normalizations miss the measured packing "
         f"coefficient (coefficient-space metric, same as the Q(q0) table): "
         f"per-cusp 2.0 at {float(d_percusp):.1f} sigma, whole-B3 6.0 at "
         f"{float(d_b3total):.1f} sigma ({float(d_b3_alt):.1f} in ratio-space) "
         f"— no post-hoc selection made"),
    ]
    if _HAVE_WB:
        try:
            wb = WitnessBuilder("pion-radius-and-cusp-volume-gaps",
                                engine="mpmath")
            wb.set_description(
                "R2-e attack on the two underived steps of the continuum-EM "
                "mirror split. GAP 1 (pion packing radius): the scale-CLASS is "
                "derived by W-plane annihilation — the inter-nucleon bond is a "
                "Vol=0 Hopf sub-link, so m_e·Vol vanishes identically and q0 is "
                "dimensionless; CAL-3 ('the Vol(Hopf)=0 meson scale') is the "
                "unique class with nonzero support, giving bond unit "
                "hbar*c/(m_pi*Q(q0)) — the 2-bit mass-scale selection collapses "
                "to 0 bits (conditional on B = m_e*Vol). The COEFFICIENT Q=1 "
                "stays underived: measured %.3f ± %.3f, consistent at %.2f "
                "sigma but with %d/9 simple Q(q0) within 1.25 sigma. GAP 2 "
                "(volume->radius): no functorial transport exists (taxonomy "
                "audit); re-scoped to the A^(-1/3) energy exponent. Cusp route: "
                "Euclidean tori genuine, but cusp-count extensivity fails at 3H "
                "(8_11 = knot), density spread x%.2f, and both pinned "
                "normalizations miss at >=1.6 sigma. Scope-(a); exploratory; "
                "nothing wired." % (float(mean_r), float(rms), float(d_one),
                                    n_within, dens_spread))
            wb.add_data("measured_coefficient_mean", float(mean_r))
            wb.add_data("measured_coefficient_rms", float(rms))
            wb.add_data("ratio_A_trend_monotone", bool(monotone))
            wb.add_data("lambda_pi_fm", float(lam_pi_fm))
            wb.add_data("selection_table_required_coefficients", sel)
            wb.add_data("q_coefficient_candidates_sigma",
                        {lbl: float(abs(v - mean_r) / rms)
                         for lbl, v in cands.items()})
            wb.add_data("scatter_needed_for_3sigma_discrimination",
                        float(scatter_needed))
            wb.add_data("two_body_lengths_fm",
                        {"hbarc_over_B_D": float(len_BD),
                         "hbarc_over_mu0": float(len_mu0)})
            wb.add_data("cusp_geometry", {
                nm: {"n_cusps": nc, "vol": vol, "cusp_vol": nc * area / 2,
                     "density": dens[nm], "A_assignment": A,
                     "cusp_vol_per_A": per_nuc[nm]}
                for nm, (nc, vol, area, _r, A) in CUSP.items()})
            wb.add_data("cusp_density_spread", float(dens_spread))
            wb.add_data("facevalue_radius_coefficients",
                        {"per_cusp_V2": float(c_percusp),
                         "whole_B3_V6": float(c_b3total),
                         "required_V_for_coeff_1": float(V_required)})
            for name, comp, exp, src in asserts:
                wb.add_assertion(name=name, computed=str(comp),
                                 expected=str(exp), tolerance=0, source=src)
            out = wb.save()
            print(f"\nWitness: {out}")
        except Exception as e:  # pragma: no cover
            print(f"\n(witness skipped: {e})")
    for _name, comp, exp, _src in asserts:
        ok = ok and (comp == exp)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
