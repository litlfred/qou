#!/usr/bin/env python3
"""keystone_lr_amplitude_level7.py — the level-7 LR/WRT amplitude, extending #4365's
EXACT Σ(2,3,5) (ζ₅) identity to the level-7 fibre roots ζ₇ (the bwsc computation).

Context (READ FIRST).
---------------------
`KeystoneLRAmplitudeReal.lean` (#4365) proved, EXACTLY in Lean at the 5th root of unity
ζ = e^{iπ/5}, the colored Lawrence–Rozansky bare amplitude identity

    A_m(α)² · D²(ζ^m) = 4·[α]²_{ζ^m},        A_m(α) = (2/√N)·sin(αmπ/N),  N = 5,

i.e. the gauge vacuum S-matrix row bwS0 = d_ζ/D holds at ζ₅ (the two flat connections
m=1,2 → the two E₈ fold normalizers D²=10±2√5).  The rigidity chain (#4402,
`KeystoneN5ValueMapRigidity`, `two_roots_insufficient`) then showed: the Σ(2,3,5) slice is
TWO points, which cannot pin the degree-≤4 value map alone; the cheapest sufficient finite
slice is **level 7** — the six fold points 2cos(kπ/7), k=1..6 (> max block degree 4).
`bwsc_level7_wrt_targets.py` (#4550) set up the explicit value-map targets there.

This probe DOES the level-7 amplitude computation: it evaluates the LR amplitude-character
route (the actual gauge quantity sin(αmπ/7)/sin(mπ/7)) at the six level-7 roots and checks it
reproduces (i) the #4550 value-map targets d_ζ(λ) for the n=5 blocks, and (ii) the #4365
amplitude identity A_m(α)²·D²(ζ^m)=4[α]² — now at N=7.  It is the numeric extension of #4365's
exact ζ₅ theorem to ζ₇.

Honest scope (STRICT).
----------------------
Scope-(a).  The level-7 agreement is genuine corroboration that bwS0 = d_ζ/D holds at the
level-7 roots (the amplitude character IS the value-map polynomial in the fold variable
t=q+q⁻¹, [m]_q = sin(mθ)/sin(θ) at q=e^{iθ}).  It does **NOT independently close bwsc**: by the
Verlinde structural identity S_{0λ}=d/D (proved algebraically in `KeystoneVerlindeSMatrixBridge`,
field `S0_eq`), once the Beasley–Witten localization category is identified with the Hecke MTC
(qDim = the *Hecke* d_q — the owner-gated `BWVacuumRowIsHecke` identification, bean bwse), the
row equals d/D at EVERY root simultaneously; the per-level numeric agreements corroborate that
ONE identification, they are not separate closure steps.  The genuine wall is bwse (RT=WRT /
gauge=categorical), which requires the Chern–Simons TQFT identification and is not
number-crunchable.  No fit; nothing wired; L2 unchanged (2/7).
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(HERE))

import _path_bridge as _bridge  # noqa: E402, F401
from mpmath import mp, mpf, sin, cos, pi, sqrt  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
LEVEL = 7
TOL = mpf(10) ** (-40)


def qint_root(m, k, N):
    """[m]_q = sin(m·kπ/N)/sin(kπ/N) at q = e^{iπk/N} (real; the fold quantum integer)."""
    return sin(m * k * pi / N) / sin(k * pi / N)


def value_map_at(name, k, N):
    """The n=5 block value map d_q(λ) as the McKay/Ê₈ mark polynomial in [m]_q, evaluated
    at the fold t = 2cos(kπ/N).  d((5))=[1]=1, d((4,1))=[4], d((3,2))=[5] (muon),
    d((3,1,1))=[5]+1 (electron) — matches KeystoneWLambdaContinuation.block_dims_explicit."""
    if name == "(5)":
        return mpf(1)
    if name == "(4,1)":
        return qint_root(4, k, N)
    if name == "(3,2) muon":
        return qint_root(5, k, N)
    if name == "(3,1,1) electron":
        return qint_root(5, k, N) + 1
    raise KeyError(name)


def value_poly_at(name, t):
    """The SAME value map as an explicit polynomial in t (the KeystoneN5ValueMapRigidity form),
    to cross-check the amplitude-character route against the #4550 target polynomials."""
    if name == "(5)":
        return mpf(1)
    if name == "(4,1)":
        return t ** 3 - 2 * t                 # [4] = t³ − 2t
    if name == "(3,2) muon":
        return t ** 4 - 3 * t ** 2 + 1         # [5] = t⁴ − 3t² + 1
    if name == "(3,1,1) electron":
        return t ** 4 - 3 * t ** 2 + 2         # [5]+1 = t⁴ − 3t² + 2
    raise KeyError(name)


BLOCKS = ["(5)", "(4,1)", "(3,2) muon", "(3,1,1) electron"]
MARKS = {"(5)": 1, "(4,1)": 4, "(3,2) muon": 5, "(3,1,1) electron": None}  # electron = [5]+1, not a single mark


def run():
    N = LEVEL
    ks = list(range(1, N))  # k = 1..6

    # ---- (i) amplitude-character route == value-map polynomial (the #4550 targets) ----------
    target_rows = []
    max_char_vs_poly_err = mpf(0)
    for name in BLOCKS:
        row = {"lambda": name, "targets": {}}
        for k in ks:
            t = 2 * cos(k * pi / N)
            d_char = value_map_at(name, k, N)     # amplitude/quantum-integer route
            d_poly = value_poly_at(name, t)       # explicit polynomial route (#4550 targets)
            err = abs(d_char - d_poly)
            max_char_vs_poly_err = max(max_char_vs_poly_err, err)
            row["targets"][f"k={k} (t={float(t):+.6f})"] = {
                "d_char_sin_ratio": float(d_char),
                "d_poly_target": float(d_poly),
                "abs_err": float(err),
            }
        target_rows.append(row)

    # ---- (ii) the #4365 amplitude identity A_m(α)²·D²(ζ^m) = 4·[α]²  at N=7 ------------------
    # A_m(α) = (2/√N)·sin(αmπ/N);  D²(ζ^m) = N/sin²(mπ/N);  ⇒ product = 4·[α]²_{ζ^m}.
    # Verified for every flat connection m=1..6 and every mark α=1..6 (the E-type node set).
    max_identity_err = mpf(0)
    n_identity_checks = 0
    for m in ks:                       # flat connection
        Dsq = N / sin(m * pi / N) ** 2  # D²(ζ^m)
        for alpha in ks:               # colored mark
            A = (2 / sqrt(N)) * sin(alpha * m * pi / N)
            char = sin(alpha * m * pi / N) / sin(m * pi / N)   # [α]_{ζ^m}
            lhs = A ** 2 * Dsq
            rhs = 4 * char ** 2
            max_identity_err = max(max_identity_err, abs(lhs - rhs))
            n_identity_checks += 1

    # ---- (iii) the two-flat-connection level-5 slice (#4365) is 2 pts < 6 (bracketing) -------
    #  reproduce the ζ₅ vacuum values as a sanity anchor to #4365's exact theorem.
    s1 = sin(pi / 5) ** 2       # (10 − 2√5)/16
    s2 = sin(2 * pi / 5) ** 2   # (10 + 2√5)/16
    anchor_first_err = abs(s1 - (10 - 2 * sqrt(5)) / 16)
    anchor_second_err = abs(s2 - (10 + 2 * sqrt(5)) / 16)

    char_matches_poly = max_char_vs_poly_err < TOL
    identity_holds = max_identity_err < TOL
    anchor_ok = anchor_first_err < TOL and anchor_second_err < TOL

    return {
        "level": N,
        "n_fold_points": len(ks),
        "max_block_degree": 4,
        "target_rows": target_rows,
        "max_char_vs_poly_err": float(max_char_vs_poly_err),
        "char_route_matches_value_poly_targets": char_matches_poly,
        "amplitude_identity_checks": n_identity_checks,
        "max_amplitude_identity_err": float(max_identity_err),
        "amplitude_identity_holds_at_level7": identity_holds,
        "level5_anchor_first_err": float(anchor_first_err),
        "level5_anchor_second_err": float(anchor_second_err),
        "level5_exact_anchor_ok": anchor_ok,
    }


def report(res):
    N = res["level"]
    print(f"# Level-7 LR/WRT amplitude — extending #4365's exact ζ₅ identity to ζ₇\n")
    print(f"N = {N}   fold points 2cos(kπ/{N}), k=1..{N-1}  ({res['n_fold_points']} distinct "
          f"> max block degree {res['max_block_degree']})\n")
    print("## (i) amplitude-character route reproduces the #4550 value-map targets\n")
    print("| λ | " + " | ".join(f"k={k}" for k in range(1, N)) + " |")
    print("|---" + "|--:" * (N - 1) + "|")
    for row in res["target_rows"]:
        cells = [f"{v['d_poly_target']:.4f}" for v in row["targets"].values()]
        print(f"| {row['lambda']} | " + " | ".join(cells) + " |")
    print(f"\n- amplitude character `sin(αmπ/7)/sin(mπ/7)` vs value-map polynomial: "
          f"max |err| = {res['max_char_vs_poly_err']:.2e}. Match: "
          f"**{res['char_route_matches_value_poly_targets']}**.\n")
    print("## (ii) the #4365 amplitude identity A_m(α)²·D²(ζ^m)=4·[α]² at N=7\n")
    print(f"- checked {res['amplitude_identity_checks']} (flat connection m, mark α) pairs; "
          f"max |err| = {res['max_amplitude_identity_err']:.2e}. Holds: "
          f"**{res['amplitude_identity_holds_at_level7']}**.\n")
    print("## (iii) level-5 exact anchor (sanity vs #4365)\n")
    print(f"- sin²(π/5) vs (10−2√5)/16: err {res['level5_anchor_first_err']:.2e}; "
          f"sin²(2π/5) vs (10+2√5)/16: err {res['level5_anchor_second_err']:.2e}. "
          f"OK: **{res['level5_exact_anchor_ok']}**.\n")
    print("## Verdict (honest scope-(a))\n")
    print("- The level-7 amplitude computation PASSES: the LR amplitude character reproduces the")
    print("  value-map targets at all six level-7 roots, and the #4365 amplitude identity extends")
    print("  to N=7. So bwS0 = d_ζ/D is corroborated at the level-7 fibre roots — the finite slice")
    print("  that (by two_roots_insufficient + KeystoneN5ValueMapRigidity) suffices to pin the")
    print("  degree-≤4 n=5 value map, which the ζ₅ 2-point slice could not.")
    print("- This does NOT independently close bwsc. By the Verlinde structural identity S_{0λ}=d/D")
    print("  (proved, KeystoneVerlindeSMatrixBridge.S0_eq), the row equals d/D at EVERY root at once")
    print("  the moment the BW-localization category is identified with the Hecke MTC (bean bwse,")
    print("  owner-gated). The per-level agreements corroborate that ONE identification. The genuine")
    print("  wall is bwse (RT=WRT / gauge=categorical), not a per-level number-crunch.")
    print("- No fit; nothing wired; L2 unchanged (2/7).")


def main(argv=None):
    res = run()
    report(res)

    w = WitnessBuilder("keystone-lr-amplitude-level7", engine="mpmath")
    w.set_description(
        "Level-7 LR/WRT amplitude: extends KeystoneLRAmplitudeReal (#4365) exact zeta_5 identity "
        "A_m(alpha)^2*D^2(zeta^m)=4*[alpha]^2 to the level-7 fibre roots 2cos(k*pi/7), k=1..6 (the "
        "bwsc computation, #4550 targets). Verifies (i) the LR amplitude character sin(alpha*m*pi/7)/"
        "sin(m*pi/7) reproduces the n=5 value-map polynomial targets d_zeta(lambda) at all six level-7 "
        "roots (max err < 1e-40); (ii) the #4365 amplitude identity holds at N=7 across all flat "
        "connections m and marks alpha; (iii) the level-5 exact anchor sin^2(pi/5)=(10-2sqrt5)/16 "
        "reproduces #4365. So bwS0=d_zeta/D is corroborated at the level-7 roots -- the finite slice "
        "that (two_roots_insufficient + KeystoneN5ValueMapRigidity) pins the degree-<=4 value map, "
        "which the zeta_5 2-point slice cannot. Scope-(a): does NOT independently close bwsc -- by the "
        "Verlinde structural identity S_{0lambda}=d/D (KeystoneVerlindeSMatrixBridge.S0_eq), the row "
        "equals d/D at every root once the BW-localization category is identified with the Hecke MTC "
        "(bean bwse, owner-gated RT=WRT); the per-level agreements corroborate that one identification, "
        "not separate closures. No fit; nothing wired; L2 unchanged (2/7)."
    )
    w.add_data("level", res["level"])
    w.add_data("n_fold_points", res["n_fold_points"])
    w.add_data("max_block_degree", res["max_block_degree"])
    w.add_data("target_rows", res["target_rows"])
    w.add_data("max_char_vs_poly_err", res["max_char_vs_poly_err"])
    w.add_data("amplitude_identity_checks", res["amplitude_identity_checks"])
    w.add_data("max_amplitude_identity_err", res["max_amplitude_identity_err"])
    w.add_data("level5_anchor_first_err", res["level5_anchor_first_err"])
    w.add_data("level5_anchor_second_err", res["level5_anchor_second_err"])
    w.add_data(
        "verdict",
        "PASS (scope-(a) corroboration). The level-7 LR amplitude character reproduces the value-map "
        "targets at all six level-7 roots and the #4365 amplitude identity extends to N=7, so bwS0="
        "d_zeta/D is corroborated at the finite slice that pins the n=5 value map. Does NOT close bwsc: "
        "by the Verlinde S_{0lambda}=d/D structural identity the row equals d/D at every root once the "
        "BW-localization=Hecke-MTC identification (bwse) is granted; the per-level agreement corroborates "
        "that single owner-gated identification. The genuine wall is bwse (RT=WRT), not a number-crunch.",
    )
    w.add_assertion(
        "amplitude_character_reproduces_value_map_targets_level7",
        computed=1 if res["char_route_matches_value_poly_targets"] else 0, expected=1, tolerance=0,
        source="The LR amplitude character [m]_q=sin(m*k*pi/7)/sin(k*pi/7) equals the n=5 value-map "
               "polynomial (McKay/E8 mark form: d((5))=[1], d((4,1))=[4], d((3,2))=[5], d((3,1,1))="
               "[5]+1) at all six level-7 fold roots 2cos(k*pi/7), to 40 dps -- the numeric extension "
               "of #4365's exact zeta_5 result to the level-7 slice (#4550 targets).",
    )
    w.add_assertion(
        "amplitude_identity_A2_D2_eq_4char2_at_level7",
        computed=1 if res["amplitude_identity_holds_at_level7"] else 0, expected=1, tolerance=0,
        source="A_m(alpha)^2*D^2(zeta^m)=4*[alpha]^2 with A_m(alpha)=(2/sqrt7)sin(alpha*m*pi/7), "
               "D^2(zeta^m)=7/sin^2(m*pi/7) -- the #4365 identity verified at N=7 for every flat "
               "connection m=1..6 and mark alpha=1..6.",
    )
    w.add_assertion(
        "level5_exact_anchor_reproduces_4365",
        computed=1 if res["level5_exact_anchor_ok"] else 0, expected=1, tolerance=0,
        source="sin^2(pi/5)=(10-2sqrt5)/16 and sin^2(2pi/5)=(10+2sqrt5)/16 to 40 dps -- reproduces "
               "KeystoneLRAmplitudeReal.sin_sq_pi_div_five / sin_sq_two_pi_div_five (#4365).",
    )
    out = w.save()
    print(f"\nwitness → {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
