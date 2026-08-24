#!/usr/bin/env python3
"""qbeta_g3_5two_state_integral_split_pin.py — the ANALYTIC 5₂
M-dictionary, part 2a: the (82) u=0 state-integral match, which PINS
the (c⁺, c⁻) split that part 1 (merged #4011) proved Theorem-11-
invisible.

Structure: eq (82) (glyph-decoded from library/arxiv-2012.00062v3/2012.00062v3.pdf p.19,
cmsy-offset discipline for the minus signs; sub/superscript rows read
at y-band resolution):

  Z₅₂(0;τ) = −(e^{πi/4}/2)·(q/q̃)^{1/8}
             ·( τ·H₀⁻(q̃)·H₂⁺(q) − 2·H₁⁻(q̃)·H₁⁺(q)
                + τ⁻¹·H₂⁻(q̃)·H₀⁺(q) ),   q = e^{2πiτ}, q̃ = e^{−2πi/τ}

— the same antidiag(1,−2,1) pairing shape as the (92) bilinear that
part 1 certified, with the τ-automorphy weights (τ, 1, τ⁻¹) of (83).

Why this pins the split: H₂⁺(q) carries c⁺(q) while H₂⁻(q̃) carries
c⁻(q̃) — DIFFERENT arguments — so unlike every Theorem-11 bilinear
(which pairs both slots at one argument and sees only the sum
σ_c = c⁺+c⁻ = 1/4 − 6Ê₂, derived exactly in part 1), the state
integral separates them. With c⁺ = a⁺ + b⁺·Ê₂ and
c⁻ = (1/4 − a⁺) + (−6 − b⁺)·Ê₂ (the part-1 sum constraint), the
match is LINEAR in (a⁺, b⁺):

  Z_towers(τ) = pref·[ B₀(τ) + a⁺·(τ⁻¹ − τ)·h₀⁻(q̃)h₀⁺(q)
                       + b⁺·(τ⁻¹Ê₂(q̃) − τ·Ê₂(q))·h₀⁻(q̃)h₀⁺(q) ]

Checks:
  P1  solve (a⁺, b⁺) exactly from two τ-points against the INDEPENDENT
      certified exact side — the Theorem-22 three-block Z₅₂ (#3951
      assembly, #3944 positions) at u→0 by circle-average (u=0 is a
      block-lattice pole; Z is entire).
  P2  held-out τ: the solved pair must reproduce the exact side at a
      third τ to the working precision (the certificate that the (82)
      reading — including the glyph-decoded overall minus and the −2
      middle coefficient — and the split are BOTH right).
  P3  rational snap: compare (a⁺, b⁺) with the print-consistent split
      c⁺ = (1/6)E₂, c⁻ = (1/12)E₂ (⇒ a⁺ = 1/6, b⁺ = −4). A snap to
      exactly these values upgrades the printed reading to DERIVED.
  P0  (guard) an overall convention factor between the Theorem-22
      normalization and (82) would corrupt the solve; a discrete
      phase set σ ∈ {1, −1, i, −i, e^{±πi/4}} is scanned and the one
      (reported openly) whose solution passes the held-out test is
      kept — if none passes, the mismatch is reported honestly.

Anti-fabrication: the (82) reading is glyph-derived, then CERTIFIED by
the held-out match to the independently-proven exact side; the split
is solved, not assumed; the phase scan is reported. No fit; no c_k
wired; mpmath dps 45, no float64; scope-(a).
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(_HERE.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402


def _load(name):
    spec = importlib.util.spec_from_file_location(name, _HERE / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_tw = _load("qbeta_g3_5two_analytic_hm_tower")     # towers + E2hat
_bs = _load("qbeta_g3_5two_barodd_substrate")      # exact Z52 (Thm 22)

set_compute_dps()

PHASES = [mp.mpc(1), mp.mpc(-1), mp.mpc(0, 1), mp.mpc(0, -1),
          mp.e ** (mp.mpc(0, 1) * mp.pi / 4),
          mp.e ** (-mp.mpc(0, 1) * mp.pi / 4)]
PHASE_TAGS = ["1", "-1", "i", "-i", "e^{ipi/4}", "e^{-ipi/4}"]


def qq(tau):
    return mp.e ** (2 * mp.pi * mp.mpc(0, 1) * tau), \
        mp.e ** (-2 * mp.pi * mp.mpc(0, 1) / tau)


def towers_at(x):
    """(h₀, h₁, h₂ c-slot-free) for both branches at argument x."""
    hp = [_tw.tower(+1, k, 0, x) for k in range(3)]
    hm = [_tw.tower(-1, k, 0, x) for k in range(3)]
    return hp, hm


def z_pieces(tau):
    """(B₀, X_a, X_b, pref): Z_towers = pref·(B₀ + a⁺X_a + b⁺X_b)."""
    q, qt = qq(tau)
    hp, _ = towers_at(q)
    _, hm = towers_at(qt)
    E2q = _tw.E2hat(q)
    E2qt = _tw.E2hat(qt)
    sig_qt = mp.mpf(1) / 4 - 6 * E2qt
    pref = -mp.e ** (mp.mpc(0, 1) * mp.pi / 4) / 2 * (q / qt) ** \
        (mp.mpf(1) / 8)
    B0 = tau * hm[0] * hp[2] - 2 * hm[1] * hp[1] \
        + (hm[2] - sig_qt * hm[0]) * hp[0] / tau
    G = hm[0] * hp[0]
    X_a = (1 / tau - tau) * G
    X_b = (E2qt / tau - tau * E2q) * G
    return B0, X_a, X_b, pref


def main() -> int:
    print("=" * 78)
    print(" 5₂ analytic M-dictionary part 2a — (82) state-integral match "
          "pins the split")
    print("=" * 78)

    # τ-points chosen ASYMMETRIC (one q-dominant, one q̃-dominant) so the
    # (a⁺, b⁺) columns are well-conditioned (symmetric points make Ê₂
    # tiny at both arguments and the solve numerically singular — the
    # first-run failure mode, kept honest here).
    taus = [mp.mpc(0, 1) * mp.mpf("0.5"), mp.mpc(0, 1) * mp.mpf("1.6"),
            mp.mpc(0, 1) * mp.mpf("0.8")]

    print("\n[exact side] Theorem-22 Z₅₂(u→0; τ) by circle-average "
          "(certified #3951/#3944):")
    z_ex = []
    for tt in taus:
        z = _bs.Z52_avg(mp.mpf(0), tt, K=20, r=mp.mpf("1e-2"))
        z_ex.append(z)
        print(f"    τ = {mp.nstr(tt, 6)}:  Z_exact = {mp.nstr(z, 18)}")

    print("\n[tower side] (82) pieces + phase-scanned linear solve:")
    pieces = [z_pieces(tt) for tt in taus]
    Xa1, Xb1 = pieces[0][1], pieces[0][2]
    Xa2, Xb2 = pieces[1][1], pieces[1][2]
    det = Xa1 * Xb2 - Xb1 * Xa2
    print(f"    solve conditioning: |det| = {mp.nstr(abs(det), 6)} vs "
          f"scale {mp.nstr(abs(Xa1 * Xb2) + abs(Xb1 * Xa2), 6)}")

    best = None
    for ph, tag in zip(PHASES, PHASE_TAGS):
        r1 = ph * z_ex[0] / pieces[0][3] - pieces[0][0]
        r2 = ph * z_ex[1] / pieces[1][3] - pieces[1][0]
        a_p = (r1 * Xb2 - r2 * Xb1) / det
        b_p = (Xa1 * r2 - Xa2 * r1) / det
        B0, X_a, X_b, pref = pieces[2]
        z_pred = pref * (B0 + a_p * X_a + b_p * X_b)
        dev = abs(z_pred - ph * z_ex[2]) / abs(z_ex[2])
        if best is None or dev < best[3]:
            best = (tag, a_p, b_p, dev)
        print(f"    σ = {tag:>10}: a⁺ = {mp.nstr(a_p, 12)}, b⁺ = "
              f"{mp.nstr(b_p, 12)}, held-out rel dev = {mp.nstr(dev, 4)}")

    tag, a_p, b_p, dev = best
    ok2 = dev < mp.mpf("1e-30")
    print(f"\n[P2] winning phase σ = {tag}; held-out certification "
          f"(rel < 1e-30): {ok2}")

    # P3: rational snap vs print-consistent (1/6, −4)
    da = abs(a_p - mp.mpf(1) / 6)
    db = abs(b_p - mp.mpf(-4))
    ok3 = da < mp.mpf("1e-28") and db < mp.mpf("1e-28")
    print(f"[P3] split snap: |a⁺ − 1/6| = {mp.nstr(da, 4)}, |b⁺ + 4| = "
          f"{mp.nstr(db, 4)} → print-consistent split DERIVED: {ok3}")

    ok = ok2 and ok3
    verdict = (
        f"SPLIT PINNED — the (82) u=0 state integral, glyph-decoded as "
        f"-(e^(i pi/4)/2)(q/qt)^(1/8)(tau H0-(qt)H2+(q) - 2H1-(qt)H1+(q) "
        f"+ tau^-1 H2-(qt)H0+(q)) and matched against the independently "
        f"certified Theorem-22 exact Z_52 (u->0 circle-average), SOLVES "
        f"the Theorem-11-invisible c-slot split linearly: a+ = 1/6, "
        f"b+ = -4 to {mp.nstr(max(da, db), 3)} (held-out tau rel dev "
        f"{mp.nstr(dev, 3)}, phase sigma = {tag}) — i.e. c+ = (1/6)E2, "
        f"c- = (1/12)E2 with E2 = 1 - 24*E2hat is now DERIVED, not "
        f"print-trusted, completing the part-1 deferral. The tower layer "
        f"is fully pinned and TIED to the #3951 deformed-block exact "
        f"side through the state integral. NEXT (part 2b): the (94)-(95) "
        f"M/S sandwiches vs the q->0 targets (96/97), then wall-crossing "
        f"to deformed x for the derived phi_odd. No fit; no c_k wired; "
        f"scope-(a)."
        if ok else
        f"PART 2a INCOMPLETE (honest): held-out dev {mp.nstr(dev, 3)} "
        f"(phase {tag}), split residuals ({mp.nstr(da, 3)}, "
        f"{mp.nstr(db, 3)}) — the failing check localizes either the "
        f"(82) reading or a Theorem-22 normalization mismatch; data "
        f"recorded. No fit; no c_k wired; scope-(a)."
    )
    print("\nVERDICT:", verdict)

    wb = WitnessBuilder("qbeta-g3-5two-state-integral-split-pin",
                        engine="mpmath")
    wb.set_description(
        "Analytic 5_2 M-dictionary part 2a: the glyph-decoded (82) u=0 "
        "state integral matched against the certified Theorem-22 exact "
        "Z_52 solves the (c+, c-) E2-slot split (Theorem-11-invisible, "
        "deferred from part 1): a+ = 1/6, b+ = -4 — the printed "
        "(1/6)E2/(1/12)E2 split derived, held-out-tau certified.")
    wb.set_content_block("conj:im-q-physical-role")
    wb.add_data("eq82_reading", {
        "prefactor": "-(e^(i pi/4)/2) * (q/qtilde)^(1/8)",
        "terms": "tau*H0-(qt)*H2+(q) - 2*H1-(qt)*H1+(q) "
                 "+ tau^-1*H2-(qt)*H0+(q)",
        "provenance": "glyph-decoded (cmsy minus-offset discipline), "
                      "then held-out-certified against Thm-22 exact"})
    wb.add_data("solve", {"phase": tag,
                          "a_plus": mp.nstr(a_p, 25),
                          "b_plus": mp.nstr(b_p, 25),
                          "heldout_rel_dev": mp.nstr(dev, 10),
                          "snap_residuals": [mp.nstr(da, 10),
                                             mp.nstr(db, 10)]})
    wb.add_data("exact_side", {f"tau={mp.nstr(taus[i], 6)}":
                               mp.nstr(z_ex[i], 25) for i in range(3)})
    wb.add_data("verdict", verdict)
    wb.add_assertion("heldout_tau_certifies_reading",
                     computed=1.0 if ok2 else 0.0, expected=1.0,
                     tolerance=0.5,
                     source="solved split reproduces the certified exact "
                            "Z_52 at held-out tau to < 1e-30 relative")
    wb.add_assertion("split_snaps_to_printed",
                     computed=1.0 if ok3 else 0.0, expected=1.0,
                     tolerance=0.5,
                     source="a+ = 1/6, b+ = -4 to < 1e-28 — c+ = (1/6)E2 "
                            "and c- = (1/12)E2 derived")
    wb.save()
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
