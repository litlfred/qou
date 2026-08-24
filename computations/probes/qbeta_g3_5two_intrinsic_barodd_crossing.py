#!/usr/bin/env python3
"""qbeta_g3_5two_intrinsic_barodd_crossing.py — the substrate bar-pair
at BLOCK level: the pole-family SWAP and the reality null (independent
confirmation + sharpening of the part-2c-2 obstruction).

Relation to the landed part 2c-2 (`qbeta_g3_5two_wall_crossing_barpair.py`
+ audit `docs/audits/2026-07-18-5two-part2c-wall-crossing-barpair.md`,
worked in parallel per the owner's parallel-exploration directive):
that probe found the substrate is exactly the (250) 0/0 lattice node
and the φ_odd strip is precision-limited. THIS probe, from a different
angle (per-block Laurent coefficients at the lattice point rather than
the assembled Z or the (250) prefactor), derives the structural
MECHANISM behind that obstruction and two exact facts it implies:

  F1  POLE-FAMILY SWAP: the bar involution q → q⁻¹ swaps which blocks
      carry the substrate lattice pole. At u_sub = 2t (x = q⁻² on the
      q-side lattice, x = q̄² on the bar-side): q-side A is REGULAR
      (leading Laurent order 0) while B, C carry the DOUBLE POLE
      (order −2); on the bar side it is exactly reversed (A: −2;
      B, C: 0). This is the (250) crossing made visible blockwise —
      Ā is a determinant of B/C-type H's — and it is WHY no per-block
      bar ratio exists at matched block label: the classical 0/0 the
      sibling probe hit is the same swap seen through the assembled Z.
  F2  REALITY NULL: every significant Laurent coefficient of every
      block on BOTH bar sides is REAL (worst |Im|/|c| ≈ 1e-41 at dps
      50) — on the substrate ray the function-value intrinsic bar
      phase is EXACTLY 0 or π. Consequence (scope-(a), method-level):
      a genuine bar-odd PHASE cannot be a function value of the block
      data on the ray; it must be a lateral/Stokes effect (the S± of
      the merged part 2b, q̃-suppressed on-ray) or live in another
      structural slot. This independently supports the part-2c-2
      verdict that the #3987 φ_odd = −0.004145 (conj-symmetry
      predicts 0) stands only as a ~1-sig-fig 2-loop preliminary.
  F3  the intrinsic REAL bar data that DOES exist at the node — the
      matched-order, swap-covariant cross-family ratios:
      c₋₂(Ā)/c₋₂(B), c₋₂(Ā)/c₋₂(C), c₀(B̄)/c₀(A), c₀(C̄)/c₀(A),
      all real, with the B/C degeneracy (ratio 1 to 1e-45) as the
      internal consistency check. Recorded as scope-(a) rows (with
      u³ and the S anchors), NO identification claimed.

The tilde side is exactly trivial at the substrate (x̃ = e^{−4πi} = 1,
|q̃| ≈ 10^{−164}) — recorded, not assumed. Anti-laundering: nothing
inverted from anchors; inputs are the proven Theorem-22 structure at
t = ln q₀ and the parts-1/2 certified machinery. mpmath dps 50, no
float64; scope-(a).
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
from qou_substrate.constants import q_at  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "qbeta_g3_5two_deformed_bilinear",
    _HERE / "qbeta_g3_5two_deformed_bilinear.py")
_db = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_db)

set_compute_dps()

S_MUON = mp.mpf("0.00968298")
S_PROTON = mp.mpf("-0.03945936")


def laurent_coeffs(f, u0, r, K=24, orders=(-2, -1, 0)):
    """Laurent coefficients c_w of f around u0 by ring integrals."""
    samples = []
    for j in range(K):
        z = r * mp.e ** (2 * mp.pi * mp.mpc(0, 1) * j / K)
        samples.append((z, f(u0 + z)))
    out = {}
    for w in orders:
        acc = mp.mpc(0)
        for z, fv in samples:
            acc += fv * z ** (-w)
        out[w] = acc / K
    return out


def main() -> int:
    print("=" * 78)
    print(" 5₂ substrate bar-pair, block level — pole-family swap + "
          "reality null")
    print("=" * 78)

    t = mp.log(q_at(50))
    u_sub = 2 * t
    q = mp.e ** (-t)
    qh = mp.e ** (-t / 2)
    qb, qbh = 1 / q, 1 / qh

    log10_qt = float(-4 * mp.pi ** 2 / t / mp.log(10))
    print(f"\n[tilde side] x̃ = e^(−4πi) = 1 exactly; |q̃| = "
          f"10^{log10_qt:.1f} → trivial on both bar sides (recorded)")

    r_ring = mp.mpf("1e-3")
    C = {}
    for side, (qq, qqh) in (("q", (q, qh)), ("qbar", (qb, qbh))):
        for iT, nm in enumerate(("A", "B", "C")):
            f = lambda u, iT=iT, qq=qq, qqh=qqh: \
                _db.blocks_m(0, mp.e ** u, qq, qqh)[iT]
            C[(side, nm)] = laurent_coeffs(f, u_sub, r_ring)

    def lead(c):
        for w in (-2, -1, 0):
            if abs(c[w]) > r_ring ** 2 * abs(c[0]) + mp.mpf("1e-40"):
                return w
        return 0

    # F1: the pole-family swap
    print("\n[F1] leading Laurent orders (q-side | bar-side):")
    orders = {}
    for nm in ("A", "B", "C"):
        wq = lead(C[("q", nm)])
        wb = lead(C[("qbar", nm)])
        orders[nm] = (wq, wb)
        print(f"    {nm}: {wq:+d} | {wb:+d}")
    ok1 = orders["A"] == (0, -2) and orders["B"] == (-2, 0) \
        and orders["C"] == (-2, 0)
    print(f"    SWAP (A regular↔double-pole, B/C double-pole↔regular): "
          f"{ok1}")

    # F2: reality of all significant coefficients
    worst = mp.mpf(0)
    for v in C.values():
        for c in v.values():
            if abs(c) > mp.mpf("1e-30"):
                worst = max(worst, abs(mp.im(c)) / abs(c))
    ok2 = worst < mp.mpf("1e-35")
    print(f"\n[F2] reality: worst |Im c|/|c| over significant "
          f"coefficients = {mp.nstr(worst, 4)}: {ok2}")
    print("    ⇒ on the substrate ray the function-value intrinsic bar "
          "phase is EXACTLY 0/π — a bar-odd PHASE must be lateral/"
          "Stokes or live elsewhere (supports the 2c-2 obstruction "
          "verdict independently)")

    # F3: matched-order swap-covariant cross-family ratios
    r1 = C[("qbar", "A")][-2] / C[("q", "B")][-2]
    r2 = C[("qbar", "A")][-2] / C[("q", "C")][-2]
    r3 = C[("qbar", "B")][0] / C[("q", "A")][0]
    r4 = C[("qbar", "C")][0] / C[("q", "A")][0]
    bc_q = C[("q", "B")][-2] / C[("q", "C")][-2]
    bc_b = C[("qbar", "B")][0] / C[("qbar", "C")][0]
    ok3 = abs(bc_q - 1) < mp.mpf("1e-40") and abs(bc_b - 1) < mp.mpf("1e-40")
    print("\n[F3] matched-order cross-family bar ratios (all real):")
    for tag, v in (("c-2(Ā)/c-2(B)", r1), ("c-2(Ā)/c-2(C)", r2),
                   ("c0(B̄)/c0(A)", r3), ("c0(C̄)/c0(A)", r4)):
        print(f"    {tag} = {mp.nstr(mp.re(v), 15)}   "
              f"log|·| = {mp.nstr(mp.log(abs(v)), 10)}")
    print(f"    B/C degeneracy: q-side {mp.nstr(abs(bc_q - 1), 3)}, "
          f"bar-side {mp.nstr(abs(bc_b - 1), 3)}: {ok3}")

    rows = {"log_ratio_pole": mp.log(abs(r1)),
            "log_ratio_reg": mp.log(abs(r3)),
            "u_cubed": u_sub ** 3,
            "S_muon": S_MUON, "S_proton": S_PROTON}
    print("\n[rows] scope-(a) comparison (NOT identifications):")
    for k, v in rows.items():
        print(f"     {k:>15} = {mp.nstr(v, 10)}")

    ok = ok1 and ok2 and ok3
    verdict = (
        f"INDEPENDENT CONFIRMATION + MECHANISM for the part-2c-2 "
        f"obstruction (parallel-route per owner directive; cite audit "
        f"2026-07-18-5two-part2c-wall-crossing-barpair): (F1) the bar "
        f"involution SWAPS the block pole families at the substrate "
        f"lattice node — q-side A regular/B,C double-pole, bar-side "
        f"reversed — the blockwise face of the (250) crossing (Abar is "
        f"a determinant of B/C-type H's), which is WHY the classical "
        f"prefactor strip hits 0/0 there; (F2) every significant block "
        f"Laurent coefficient on both bar sides is REAL (worst "
        f"{mp.nstr(worst, 3)}), so on the substrate ray the function-"
        f"value intrinsic bar phase is exactly 0/pi — a genuine bar-odd "
        f"phase must be a lateral/Stokes effect (the derived part-2b "
        f"S±, qtilde-suppressed on-ray) or live in another structural "
        f"slot, independently supporting phi_odd = -0.004145 as a "
        f"~1-sig-fig preliminary only; (F3) the intrinsic REAL bar "
        f"data at the node is recorded as the matched-order swap-"
        f"covariant cross-family ratios (B/C-degeneracy-checked to "
        f"1e-45), scope-(a), no identification. Method consequence: "
        f"the derived-precision odd datum should be sought in the "
        f"EXACT higher-loop saddle expansion (algebraic in the trace "
        f"field) or the Masbaum cyclotomic face — not in on-ray block "
        f"values. No fit; no c_k wired."
        if ok else
        f"INCOMPLETE (honest): F1={ok1} F2={ok2} F3={ok3} — data "
        f"recorded; the failing check localizes the decode. No fit; "
        f"no c_k wired; scope-(a)."
    )
    print("\nVERDICT:", verdict)

    wb = WitnessBuilder("qbeta-g3-5two-intrinsic-barodd-crossing",
                        engine="mpmath")
    wb.set_description(
        "Block-level substrate bar-pair: the bar involution swaps the "
        "5_2 block pole families at the lattice node (mechanism of the "
        "part-2c-2 0/0 obstruction) and all on-ray block Laurent data "
        "is real — the function-value intrinsic bar phase is exactly "
        "0/pi. Independent parallel-route confirmation; scope-(a).")
    wb.set_content_block("conj:im-q-physical-role")
    wb.add_data("inputs", {"t": mp.nstr(t, 25), "u_sub": "2t",
                           "x_tilde": "1 (exact)",
                           "log10_qtilde": log10_qt,
                           "ring": {"radius": mp.nstr(r_ring, 4),
                                    "K": 24}})
    wb.add_data("f1_pole_swap", {nm: {"q_side": orders[nm][0],
                                      "bar_side": orders[nm][1]}
                                 for nm in ("A", "B", "C")})
    wb.add_data("f2_reality", {"worst_im_over_abs": mp.nstr(worst, 8)})
    wb.add_data("f3_cross_family_ratios", {
        "c_m2_Abar_over_B": mp.nstr(r1, 20),
        "c_m2_Abar_over_C": mp.nstr(r2, 20),
        "c_0_Bbar_over_A": mp.nstr(r3, 20),
        "c_0_Cbar_over_A": mp.nstr(r4, 20),
        "BC_degeneracy_q": mp.nstr(abs(bc_q - 1), 8),
        "BC_degeneracy_bar": mp.nstr(abs(bc_b - 1), 8)})
    wb.add_data("comparison_rows", {k: mp.nstr(v, 12)
                                    for k, v in rows.items()})
    wb.add_data("verdict", verdict)
    wb.add_assertion("pole_family_swap_derived",
                     computed=1.0 if ok1 else 0.0, expected=1.0,
                     tolerance=0.5,
                     source="leading Laurent orders: A (0|-2), "
                            "B (-2|0), C (-2|0) across the bar")
    wb.add_assertion("onray_reality_null",
                     computed=1.0 if ok2 else 0.0, expected=1.0,
                     tolerance=0.5,
                     source="all significant block Laurent coefficients "
                            "real to < 1e-35 on both bar sides")
    wb.add_assertion("cross_family_ratios_recorded",
                     computed=1.0 if ok3 else 0.0, expected=1.0,
                     tolerance=0.5,
                     source="matched-order swap-covariant ratios with "
                            "B/C degeneracy check < 1e-40")
    wb.save()
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
