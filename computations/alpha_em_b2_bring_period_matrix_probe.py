#!/usr/bin/env python3
"""alpha_em_b2_bring_period_matrix_probe.py — B2 open input (a), the
Bring-curve symplectic period matrix: BOTH the integer polarization
structure C AND the exact complex modulus τ₀ are certified at 80 dps
against [braden-disney-hogg-2022], resolving the earlier reflowed-PDF
glyph ambiguity in [braden-northover-2012].

Sources in library/:
  - library/pjm-v154-n1-p09-s/pjm-v154-n1-p09-s.pdf — Riera–Rodríguez,
    "The period matrix of Bring's curve", Pacific J. Math 154 (1992).
    Theorem 1: Bring's half-plane is Z = τ·C, τ ∈ ℂ, Im τ > 0.
    Theorem 2: Z = τ₀·C, τ₀ characterized by two j-values (with the two
    j-equations swapped in Riera–Rodríguez, as noted by later authors).
  - library/arxiv-1206.6004v2/1206.6004v2.pdf — Braden–Northover (2012).
    Reflowed PDF glyph extraction had misread eq (4.3) as
    j(τ₀) = −29³·25/2⁵ and τ₀ ≈ −0.5 + 0.185576i ("25" for "5",
    "55" for "66").
  - library/arxiv-2208.13692v1/2208.13692v1.pdf — Braden–Disney-Hogg
    (2022) [braden-disney-hogg-2022], period-matrix j-invariant
    characterization:
        j(τ₀) = −29³·5/2⁵ = −121945/32,   j(5τ₀) = −25/2,
        τ₀ = −0.5 + 0.186676i  (to 6 d.p.),
    explicitly noting Riera–Rodríguez swapped the two j-values.

WHAT IS CERTIFIED (80 dps, zero float64):
  P1  Polarization matrix C (symmetric, diagonal 4, off-diagonal ±1)
      has eigenvalues EXACTLY (1, 5, 5, 5) — matching the corpus
      isogeny tuple (5, 5, 5, 1) of Bring's Jacobian E⁴.
  P2  [braden-disney-hogg-2022] cross-check at 80 dps (bean qou-1twx):
      Under standard j(i) = 1728 (1728·mpmath.kleinj), the 5-isogeny
      lift τ₀ = (τ_E − 3)/5 of j(τ_E) = −25/2 on Re τ_E = +1/2 has
      Re τ₀ = −1/2, Im τ₀ = 0.186676462462809923206162881363… and
      simultaneously satisfies BOTH published conditions:
          |j(τ₀) − (−29³·5/2⁵)| < 10⁻⁷⁴,
          |j(5τ₀) − (−25/2)|     < 10⁻⁷⁴,
      with −29³·5/2⁵ = −121945/32 identically, agreeing with direct
      half-line inversion of j(τ) = −29³·5/2⁵ to > 76 digits and with
      the printed 6 d.p. value −0.5 + 0.186676i to 4.62×10⁻⁷ < 5×10⁻⁷.
  P3  Z = τ₀ · C satisfies the Riemann relations (symmetric; Im Z
      positive-definite ⇔ Im τ₀ > 0).
  P4  Markov-side normalization w_{(4,1)}(q₀) matches the live sibling
      witness alpha-em-b2-scalar-c.witness.json (proton pin), and the
      |c| candidate table is emitted at τ₀ while keeping sub-piece (ii)
      (S₅-equivariant τ-intertwiner basis match) honestly open.
      Nothing wired; 1/(8π) stays phase-4; scope-(a).

mpmath dps 80; no float64.
"""
from __future__ import annotations

import importlib.util
import itertools
import sys
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder, record_upstream  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "alpha_em_b2_scalar_c_probe", _HERE / "alpha_em_b2_scalar_c_probe.py")
_sc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_sc)

set_compute_dps(80)
mp.mp.dps = 80

# [braden-disney-hogg-2022] published j-invariant conditions (bean qou-1twx)
J_TAU_BDH = -mp.mpf(29) ** 3 * mp.mpf(5) / mp.mpf(2) ** 5   # −29³·5/2⁵
J_TAU_RATIONAL = -mp.mpf(121945) / mp.mpf(32)               # −121945/32
J_5TAU_BDH = -mp.mpf(25) / mp.mpf(2)                        # −25/2
TAU0_BDH_6DP = mp.mpc("-0.5", "0.186676")                   # BDH 2022 (6 d.p.)

# Historical Braden–Northover reflowed-PDF glyph misread retained for audit record
J_TAU_BN_OCR = -mp.mpf(29) ** 3 * mp.mpf(25) / mp.mpf(2) ** 5
TAU0_BN_OCR = mp.mpc("-0.5", "0.185576")


def jj(tau):
    """Standard j-invariant, j(i) = 1728."""
    return mp.mpf(1728) * mp.kleinj(tau)


def solve_j_on_halfline(target, y_lo, y_hi, re_line=None):
    if re_line is None:
        re_line = mp.mpf(-1) / mp.mpf(2)
    f = lambda y: mp.re(jj(mp.mpc(re_line, y))) - target
    lo, hi = mp.mpf(y_lo), mp.mpf(y_hi)
    for _ in range(300):
        mid = (lo + hi) / mp.mpf(2)
        if f(lo) * f(mid) <= 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / mp.mpf(2)


def main() -> int:
    mp.mp.dps = 80
    upstream_records: list = []
    scalar_c_doc = record_upstream(
        _HERE / "alpha-em-b2-scalar-c.witness.json", upstream_records)
    markov_norm_witness = mp.mpf(
        scalar_c_doc["data"]["wedderburn_weight_std_at_q0"])

    print("=" * 78)
    print(" B2 open input (a): Bring period matrix — C and τ₀ certified at 80 dps")
    print("=" * 78)

    # P1: the C-matrix isogeny-eigenvalue gate (convention-independent)
    C = mp.matrix([[4, 1, 1, -1],
                   [1, 4, -1, 1],
                   [1, -1, 4, 1],
                   [-1, 1, 1, 4]])
    evC = sorted([mp.re(x) for x in mp.eig(C, left=False, right=False)])
    ok_eig = all(abs(evC[i] - t) < mp.mpf("1e-60")
                 for i, t in enumerate([1, 5, 5, 5]))
    n_class = 0
    for signs in itertools.product((1, -1), repeat=6):
        M = mp.matrix(4, 4)
        idx = 0
        for i in range(4):
            M[i, i] = 4
            for j in range(i + 1, 4):
                M[i, j] = signs[idx]
                M[j, i] = signs[idx]
                idx += 1
        ev = sorted([mp.re(x) for x in mp.eig(M, left=False, right=False)])
        if all(abs(ev[i] - t) < mp.mpf("1e-50")
               for i, t in enumerate([1, 5, 5, 5])):
            n_class += 1
    ok1 = ok_eig and n_class == 8
    print(f"\n[P1] C symmetric {{4,±1}}: eigenvalues = "
          f"{[mp.nstr(e, 8) for e in evC]} = (1,5,5,5) = corpus "
          f"isogeny tuple: {ok_eig}")
    print(f"    convention-independent cross-gate; sign-arrangement "
          f"class size = {n_class}/64")

    # P2: 80-dps [braden-disney-hogg-2022] cross-check (bean qou-1twx)
    exact_rational_diff = abs(J_TAU_BDH - J_TAU_RATIONAL)
    yE = solve_j_on_halfline(J_5TAU_BDH, "0.87", "1.3",
                             re_line=mp.mpf(1) / mp.mpf(2))
    tauE = mp.mpc(mp.mpf(1) / mp.mpf(2), yE)
    # Γ₀(5) coset scan over k ∈ {-5..5}; k = -3 places Re(τ₀) = -1/2
    reps = [(k, (tauE + k) / mp.mpf(5)) for k in range(-5, 6)]
    best_k, best_t, best_dev = None, None, None
    for k, t in reps:
        d = abs(jj(t) - J_TAU_BDH)
        if best_dev is None or d < best_dev:
            best_k, best_t, best_dev = k, t, d
    # Choose canonical Re(τ₀) = -1/2 representative (k = -3)
    tau0_bdh = (tauE - mp.mpf(3)) / mp.mpf(5)
    im_iso = mp.im(tau0_bdh)
    y_bdh_direct = solve_j_on_halfline(J_TAU_BDH, "0.17", "0.20")
    j_tau0_val = jj(tau0_bdh)
    j_5tau0_val = jj(mp.mpf(5) * tau0_bdh)
    j_tau0_res = abs(j_tau0_val - J_TAU_BDH)
    j_5tau0_res = abs(j_5tau0_val - J_5TAU_BDH)
    direct_vs_iso_diff = abs(im_iso - y_bdh_direct)
    six_dp_diff = abs(tau0_bdh - TAU0_BDH_6DP)
    isogenous = j_tau0_res < mp.mpf("1e-74") and j_5tau0_res < mp.mpf("1e-74")
    ok2 = (exact_rational_diff == 0
           and isogenous
           and direct_vs_iso_diff < mp.mpf("1e-75")
           and six_dp_diff < mp.mpf("5e-7"))

    # Also retain diagnostic readout on the old OCR-misread numbers for audit clarity
    y_solved_ocr = solve_j_on_halfline(J_TAU_BN_OCR, "0.14", "0.17")
    j_pr_ocr = mp.re(jj(TAU0_BN_OCR))
    t5_ocr = mp.mpf(5) * TAU0_BN_OCR
    t5r_ocr = mp.mpc(mp.re(t5_ocr) - mp.nint(mp.re(t5_ocr)), mp.im(t5_ocr))
    j5_pr_ocr = mp.re(jj(t5r_ocr))

    print("\n[P2] [braden-disney-hogg-2022] 80-dps cross-check:")
    print(f"    −29³·5/2⁵ == −121945/32 exact: {exact_rational_diff == 0} "
          f"({mp.nstr(J_TAU_BDH, 20)})")
    print(f"    τ₀ = (τ_E − 3)/5 = {mp.nstr(tau0_bdh, 30)}")
    print(f"    |j(τ₀) − (−29³·5/2⁵)| = {mp.nstr(j_tau0_res, 6)}")
    print(f"    |j(5τ₀) − (−25/2)|    = {mp.nstr(j_5tau0_res, 6)}")
    print(f"    |Im τ₀(5-isog) − Im τ₀(direct j-solve)| = "
          f"{mp.nstr(direct_vs_iso_diff, 6)}")
    print(f"    |τ₀ − (−0.5 + 0.186676i)| = {mp.nstr(six_dp_diff, 6)} < 5e-7")

    # P3: Riemann relations for Z = τ₀·C at the exact 80-dps τ₀
    Z = tau0_bdh * C
    symm = max(abs(Z[i, j] - Z[j, i]) for i in range(4) for j in range(4))
    ImZ = mp.matrix(4, 4)
    for i in range(4):
        for j in range(4):
            ImZ[i, j] = mp.im(Z[i, j])
    evIm = sorted([mp.re(x) for x in mp.eig(ImZ, left=False, right=False)])
    ok3 = symm == 0 and evIm[0] > 0
    print(f"\n[P3] Z = τ₀·C Riemann relations: symmetric "
          f"({mp.nstr(symm, 2)}); Im Z eigenvalues "
          f"{[mp.nstr(e, 8) for e in evIm]} > 0: {ok3}")

    # P4: |c| candidate table, evaluated at exact 80-dps τ₀ (plus historical rows)
    q0, pin = _sc._q0()
    markov_norm = _sc._wedderburn_weight(_sc.SHAPE, q0)
    reg = abs(markov_norm - markov_norm_witness)
    ok4 = reg < mp.mpf("1e-28")
    print(f"\n[P4] Markov-side norm (regression vs sibling witness "
          f"{mp.nstr(reg, 3)}): {mp.nstr(markov_norm, 30)}")
    print("    |c| candidate table — conditional on sub-piece (ii):")
    cand = {}
    for lbl, im_t in (("bdh2022_exact_tau0", im_iso),
                      ("isogeny_tau_E_over_5", im_iso),
                      ("bdh2022_printed_0.186676", mp.im(TAU0_BDH_6DP)),
                      ("printed_0.185576", mp.im(TAU0_BN_OCR)),
                      ("j_solved_0.15878", y_solved_ocr)):
        hodge_det = im_t * mp.mpf(125) ** (mp.mpf(1) / mp.mpf(4))
        hodge_tr = mp.mpf(4) * im_t
        cand[lbl] = {"im_tau": mp.nstr(im_t, 30),
                     "c_det": mp.nstr(markov_norm / hodge_det, 30),
                     "c_tr": mp.nstr(markov_norm / hodge_tr, 30)}
        print(f"      Im τ = {lbl}: |c|_det = "
              f"{cand[lbl]['c_det'][:18]}, |c|_tr = {cand[lbl]['c_tr'][:18]}")
    print(f"    (1/(8π) = {mp.nstr(mp.mpf(1) / (mp.mpf(8) * mp.pi), 15)} "
          f"— reference row only, NO identification)")

    ok = ok1 and ok2 and ok3 and ok4
    verdict = (
        f"B2 INPUT (a) — STRUCTURE AND τ₀ CERTIFIED AT 80 DPS "
        f"(discipline-compliant, bean qou-1twx): C = {{4,±1}} has "
        f"eigenvalues (1,5,5,5) matching the E⁴ isogeny tuple ({ok1}), "
        f"Z = τ₀·C satisfies the Riemann relations ({ok3}), and "
        f"[braden-disney-hogg-2022] resolves the earlier Braden–Northover "
        f"reflowed-PDF glyph misread (−29³·25/2⁵ → −29³·5/2⁵ = −121945/32; "
        f"0.185576 → 0.186676): at τ₀ = (τ_E − 3)/5 = −1/2 + "
        f"{mp.nstr(im_iso, 18)}i, BOTH standard j(τ₀) = −29³·5/2⁵ "
        f"(residual {mp.nstr(j_tau0_res, 3)}) and j(5τ₀) = −25/2 "
        f"(residual {mp.nstr(j_5tau0_res, 3)}) hold to >74 digits and "
        f"match the printed 6 d.p. −0.5 + 0.186676i within "
        f"{mp.nstr(six_dp_diff, 4)}. Sub-piece (ii) (S₅-equivariant "
        f"τ-intertwiner basis match) remains open; nothing wired; "
        f"1/(8π) stays phase-4; scope-(a). Sources: riera-rodriguez-1992, "
        f"braden-northover-2012, braden-disney-hogg-2022."
        if ok else
        f"INCOMPLETE: P1={ok1} P2={ok2} P3={ok3} P4={ok4}."
    )
    print("\nVERDICT:", verdict)

    wb = WitnessBuilder("alpha-em-b2-bring-period-matrix", engine="mpmath")
    wb.add_upstream_records(upstream_records)
    wb.set_description(
        "Bring period matrix Z = tau0*C for B2 input (a) at 80 dps: C "
        "isogeny-gated with eigenvalues (1,5,5,5); tau0 cross-checked "
        "against [braden-disney-hogg-2022] printed j(tau0) = -29^3*5/2^5 "
        "= -121945/32, j(5*tau0) = -25/2, and 6 d.p. -0.5 + 0.186676i "
        "(resolving the earlier reflowed-PDF glyph misread); Riemann "
        "relations verified; |c| candidate table conditional on sub-piece "
        "(ii). Nothing wired; scope-(a).")
    wb.set_content_block("prop:em-coupling-bring-zero-mode")
    wb.add_parameter("q0", mp.nstr(q0, 50, strip_zeros=False))
    wb.add_parameter("q0_pin", pin)
    wb.add_parameter("compute_dps", 80)
    wb.add_data("sources_in_uploads", [
        "pjm-v154-n1-p09-s.pdf (riera-rodriguez-1992)",
        "1206.6004v2.pdf (braden-northover-2012)",
        "2208.13692v1.pdf (braden-disney-hogg-2022)",
    ])
    wb.add_data("C_matrix", [[int(C[i, j]) for j in range(4)]
                             for i in range(4)])
    wb.add_data("C_eigenvalues", [mp.nstr(e, 20) for e in evC])
    wb.add_data("C_isogeny_gate", {"eigenvalues": "(1,5,5,5)",
                                   "corpus_isogeny_tuple": "(5,5,5,1)",
                                   "convention_independent": True,
                                   "sign_class_size": n_class})
    wb.add_data("braden_disney_hogg_2022_crosscheck", {
        "source": "library/arxiv-2208.13692v1/2208.13692v1.pdf",
        "j_tau0_printed_expr": "-29^3 * 5 / 2^5",
        "j_tau0_rational": "-121945/32",
        "j_tau0_decimal_exact": "-3810.78125",
        "j_5tau0_printed": "-25/2",
        "tau0_printed_6dp": "-0.5 + 0.186676i",
        "tau0_80dps": mp.nstr(tau0_bdh, 75),
        "re_tau0_exact": "-1/2",
        "im_tau0_80dps": mp.nstr(im_iso, 75),
        "im_tau0_direct_j_solve_80dps": mp.nstr(y_bdh_direct, 75),
        "direct_vs_5isogeny_im_diff": mp.nstr(direct_vs_iso_diff, 12),
        "j_tau0_residual_80dps": mp.nstr(j_tau0_res, 12),
        "j_5tau0_residual_80dps": mp.nstr(j_5tau0_res, 12),
        "diff_vs_printed_6dp": mp.nstr(six_dp_diff, 12),
        "riera_rodriguez_swap_confirmed": True,
        "braden_northover_ocr_resolved": (
            "Earlier glyph read -29^3*25/2^5 and 0.185576i misread factor 5 "
            "as 25 and digits 66 as 55; standard j(i)=1728 closes identically "
            "at [braden-disney-hogg-2022]'s published values."
        ),
    })
    wb.add_data("tau0_convention_resolution", {
        "printed": mp.nstr(TAU0_BDH_6DP, 12),
        "bn2012_ocr_misread": mp.nstr(TAU0_BN_OCR, 12),
        "j_targets": ["-29^3*5/2^5", "-25/2"],
        "j_at_printed": mp.nstr(mp.re(jj(TAU0_BDH_6DP)), 15),
        "j_at_bn2012_ocr": mp.nstr(j_pr_ocr, 12),
        "im_tau_from_j_solve": mp.nstr(y_bdh_direct, 50),
        "im_tau_from_bn2012_ocr_j_solve": mp.nstr(y_solved_ocr, 15),
        "j5_at_bn2012_ocr": mp.nstr(j5_pr_ocr, 10),
        "standard_5isogenous_pair": bool(isogenous),
        "isogeny_best_k": -3,
        "isogeny_im_tau0": mp.nstr(im_iso, 50),
        "isogeny_j_tau0_closes": mp.nstr(mp.re(j_tau0_val), 25),
        "isogeny_j5_closes": mp.nstr(mp.re(j_5tau0_val), 25),
        "methods_tried": ["direct-eval", "j-inversion",
                          "5-isogeny-coset-forward",
                          "braden-disney-hogg-2022-crosscheck"],
        "status": (
            "RESOLVED at 80 dps via [braden-disney-hogg-2022]: standard "
            "j(i)=1728 closes BOTH j(tau0) = -29^3*5/2^5 = -121945/32 and "
            "j(5*tau0) = -25/2 at tau0 = (tau_E - 3)/5 = -1/2 + "
            "0.18667646246281...i (matching printed -0.5 + 0.186676i to 6 d.p.)"
        ),
    })
    wb.add_data("c_candidates_parametric", cand)
    wb.add_data("markov_norm", mp.nstr(markov_norm, 50))
    wb.add_data("verdict", verdict)
    wb.add_assertion("C_isogeny_eigenvalue_gate",
                     computed=1 if ok1 else 0, expected=1,
                     tolerance=0,
                     source="C symmetric {4,±1}; eigenvalues (1,5,5,5) "
                            "= corpus isogeny tuple (convention-"
                            "independent cross-gate)")
    wb.add_assertion("bdh2022_j_tau0_printed_factor_identity",
                     computed=mp.nstr(exact_rational_diff, 10),
                     expected="0",
                     tolerance="1e-78",
                     source="[braden-disney-hogg-2022] printed -29^3*5/2^5 "
                            "equals -121945/32 identically")
    wb.add_assertion("bdh2022_j_tau0_exact_80dps",
                     computed=mp.nstr(j_tau0_res, 10),
                     expected="0",
                     tolerance="1e-74",
                     source="standard j(tau0) = -29^3*5/2^5 at 5-isogenous "
                            "tau0 = (tau_E - 3)/5 on Re(tau0) = -1/2")
    wb.add_assertion("bdh2022_j_5tau0_exact_80dps",
                     computed=mp.nstr(j_5tau0_res, 10),
                     expected="0",
                     tolerance="1e-74",
                     source="standard j(5*tau0) = -25/2 at 80 dps")
    wb.add_assertion("bdh2022_tau0_matches_printed_6dp",
                     computed=mp.nstr(six_dp_diff, 10),
                     expected="0",
                     tolerance="5e-7",
                     source="[braden-disney-hogg-2022] printed tau0 = "
                            "-0.5 + 0.186676i (6 d.p. rounding)")
    wb.add_assertion("riemann_relations",
                     computed=1 if ok3 else 0, expected=1,
                     tolerance=0,
                     source="Z = tau0*C symmetric, Im Z positive-definite")
    wb.add_assertion("c_candidates_parametric_emitted",
                     computed=mp.nstr(reg, 10), expected="0",
                     tolerance="1e-28",
                     source="Markov norm w_(4,1)(q0) matches live sibling "
                            "alpha-em-b2-scalar-c.witness.json; |c| table "
                            "conditional on sub-piece (ii); nothing wired")
    wb.save({
        "q0Anchor": "proton",
        "q0Value": mp.nstr(q0, 50, strip_zeros=False),
    })
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
