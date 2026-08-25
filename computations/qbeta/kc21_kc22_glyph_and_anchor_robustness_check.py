#!/usr/bin/env python3
"""Two defects in the c₃ registry rows KC21/KC22, measured from committed witnesses.

Adjudication work for bean `qou-qb8f` item (c) ("should the registry's c_3 row
carry a pointer either way?"), which that bean left to the registry maintainers.
Read-only: no production script re-run, no witness written, no c_k wired, no fit.

DEFECT 1 — GLYPH COLLISION (`qou-kp9f`).  Registry rows KC21 and KC22 are
adjacent and use `q*`, `h*` and `ũ(q*)` for two *different* points:

  KC21  q* := the S = 0 point            ≈ 1.10998  (a decay-sector determination of q₀)
  KC22  q* := the real root > 1 of the    ≈ 1.48989  (a Q_b zero; ρ = ũ(q*) is the
              degree-12 Δ_net factor                  D-ladder radius of convergence)

Neither row says "the other q*".  This is the overloaded-symbol trap named in
AGENTS.md §"Conditional-proved ≠ premise-established" rule 4.

DEFECT 2 — ANCHOR-SELECTIVE SCALE CLAIM (`qou-uoo0`).  KC21 states the Φ_b
state-integral saddle "supplies the |S| scale from geometry ... smooth +
anchor-blind", citing volume deficit 0.0094 ≈ |S(muon)| = 0.00968.  The deficit
IS anchor-blind (sub-ppm).  |S_leak| is NOT — it swings by a factor ≈ 4 between
the two anchors.  An anchor-blind quantity cannot supply an anchor-dependent
scale: the 2.9 % agreement holds at the muon and misses the proton by ≈ 76 %.
The producing witness records both anchors and says "|S(muon)|" explicitly; it
is the registry summary that generalises a muon-only match into "the |S| scale".

This is the same objection the corpus already accepts against `h·D(ũ)` ("the
carrier is anchor-blind ... and is NOT the swinging empirical S, so `S = h·D(ũ)`
is schematic, not a tight identity" — `qbeta-c3-qstar-k31-repin.witness.json`).
KC21 does not carry it for the Φ_b deficit, which is (H1)'s sole surviving
geometric backing.

Scope-(a) throughout: this measures what the committed numbers say.  It does not
refute the Φ_b saddle, 4₁ amphichirality, Vol(4₁) as an ingredient elsewhere, or
any theorem in SLeakZeroCrossing.lean (all generic + hypothesis-carrying).
"""

import json
import pathlib
import sys

from mpmath import mp, mpf

import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qbeta_utils import substrate_ladder_quantities  # noqa: E402


def utilde(q):
    """ũ = q·b·ℏ_q² (= q·u), matching `utilde` in the k=31 re-pin probe."""
    return q * substrate_ladder_quantities(q)["u"]

HERE = pathlib.Path(__file__).resolve().parent


def load(name):
    return json.loads((HERE / name).read_text())


def rel(a, b):
    """Relative separation of a from b, as a fraction of b."""
    return abs(a - b) / abs(b)


# KC22's q*: the Q_b zero — the degree-12 factor of the Δ_net numerator, as
# recorded in the 2026-08-09 correction audit.  Coefficients q^12 … q^0.
POLY = [1, 2, -4, -8, 6, 16, -10, -16, 6, 8, -4, -2, 1]


def deg12(x):
    acc = mpf(0)
    for c in POLY:
        acc = acc * x + c
    return acc


def defect_1_glyph_collision():
    """KC21 and KC22 use `q*`, `h*`, `ũ(q*)` for two different points."""
    print("=" * 72)
    print("DEFECT 1 — `q*` / `h*` / `ũ(q*)` name two different points in KC21 vs KC22")
    print("=" * 72)

    # KC21's q*: the S = 0 point, read by stable path from the k=31 re-pin witness.
    repin = load("qbeta-c3-qstar-k31-repin.witness.json")["data"]
    q_star_S0 = mpf(repin["qstar"]["value"])
    h_star_S0 = mpf(repin["carrier_saturation"]["h_qstar"])
    u_star_S0 = mpf(repin["carrier_saturation"]["utilde_qstar"])

    # KC22's q*: recomputed from the polynomial rather than quoted, so the two
    # numbers are independently derived.
    q_star_Qb = mp.findroot(deg12, mpf("1.49"))
    h_star_Qb = q_star_Qb - 1 / q_star_Qb
    # ρ is DERIVED from the recomputed root, not quoted: the registry's KC22
    # claim is precisely `ρ = ũ(q*_ρ)`, so deriving it here tests that identity
    # instead of assuming it.  Both KC22 numbers now come from the polynomial.
    rho_KC22 = utilde(q_star_Qb)
    RHO_PUBLISHED = mpf("0.14279999664468968890572088577932032058109273315046")

    assert abs(deg12(q_star_Qb)) < mpf("1e-30"), "degree-12 root did not converge"
    assert q_star_Qb > 1, "expected the real root > 1"
    assert rel(h_star_Qb, mpf("0.818706471352")) < mpf("1e-11"), "h* mismatch vs KC22"
    # The identity the registry asserts, now checked rather than assumed.
    assert rel(rho_KC22, RHO_PUBLISHED) < mpf("1e-30"), (
        f"ũ(q*_ρ) = {mp.nstr(rho_KC22, 30)} does not reproduce the published "
        f"radius ρ = {mp.nstr(RHO_PUBLISHED, 30)} — KC22's `ρ = ũ(q*_ρ)` fails"
    )

    print(f"  KC21  q* (S = 0 point)      = {mp.nstr(q_star_S0, 22)}")
    print(f"  KC22  q* (Q_b degree-12)    = {mp.nstr(q_star_Qb, 22)}")
    print(f"        ratio                 = {mp.nstr(q_star_Qb / q_star_S0, 8)}")
    print()
    print(f"  KC21  h* = q*−1/q*          = {mp.nstr(h_star_S0, 14)}")
    print(f"  KC22  h* = q*−1/q*          = {mp.nstr(h_star_Qb, 14)}")
    print(f"        ratio                 = {mp.nstr(h_star_Qb / h_star_S0, 8)}")
    print()
    print(f"  KC21  ũ(q*)                 = {mp.nstr(u_star_S0, 14)}")
    print(f"  KC22  ũ(q*) = ρ             = {mp.nstr(rho_KC22, 14)}")
    print(f"        ratio                 = {mp.nstr(rho_KC22 / u_star_S0, 8)}")

    assert rel(q_star_S0, q_star_Qb) > mpf("0.25"), "expected the two q* to differ by >25%"
    assert h_star_Qb / h_star_S0 > 3, "expected h* to differ by >3x"
    assert rho_KC22 / u_star_S0 > 10, "expected ũ(q*) to differ by >10x"
    print("\n  => three glyphs, two points. Both rows must name which q* they mean.")

    # ũ at the S=0 point equals ũ at the substrate to 8 digits; defect 2 reuses it.
    return u_star_S0


def defect_2_anchor_selective_scale(u0):
    """The Φ_b deficit → |S| scale match holds at the muon only."""
    print()
    print("=" * 72)
    print("DEFECT 2 — the Φ_b deficit → |S| scale claim is ANCHOR-SELECTIVE")
    print("=" * 72)

    phib = load("qbeta-c3-phib-saddle-state-integral.witness.json")
    saddle = {row["anchor"]: row for row in phib["data"]["saddle"]}

    deficit = {k: mpf(v["vol_deficit"]) for k, v in saddle.items()}
    S_leak = {k: mpf(v["S_target"]) for k, v in saddle.items()}

    # The registry quotes the deficit as anchor-blind. Confirm, and quantify.
    deficit_spread = rel(deficit["proton"], deficit["muon"])
    S_swing = abs(S_leak["proton"]) / abs(S_leak["muon"])

    print(f"  vol_deficit(proton)   = {mp.nstr(deficit['proton'], 20)}")
    print(f"  vol_deficit(muon)     = {mp.nstr(deficit['muon'], 20)}")
    print(f"  deficit spread        = {mp.nstr(deficit_spread, 4)}  (anchor-BLIND)")
    print()
    print(f"  |S_leak(muon)|        = {mp.nstr(abs(S_leak['muon']), 12)}")
    print(f"  |S_leak(proton)|      = {mp.nstr(abs(S_leak['proton']), 12)}")
    print(f"  |S_leak| swing        = {mp.nstr(S_swing, 6)}x  (anchor-DEPENDENT)")
    print()

    miss_mu = rel(deficit["muon"], abs(S_leak["muon"]))
    miss_p = rel(deficit["proton"], abs(S_leak["proton"]))
    print(f"  deficit vs |S_leak(muon)|    miss = {mp.nstr(miss_mu * 100, 4)} %   <- the quoted match")
    print(f"  deficit vs |S_leak(proton)|  miss = {mp.nstr(miss_p * 100, 4)} %   <- NOT quoted")
    print(f"  ratio of misses             = {mp.nstr(miss_p / miss_mu, 5)}x")

    assert deficit_spread < mpf("1e-6"), "deficit should be anchor-blind"
    assert S_swing > 4, "S_leak should swing by >4x between anchors"
    assert miss_mu < mpf("0.03"), "muon match should be within 3%"
    assert miss_p > mpf("0.7"), "proton miss should exceed 70%"
    assert miss_p / miss_mu > 20, "the two anchors should disagree by >20x"

    print(
        "\n  => an anchor-BLIND deficit cannot supply an anchor-DEPENDENT scale.\n"
        "     The match is a property of WHICH anchor is quoted, not of the geometry."
    )

    # ------------------------------------------ how tight is 2.9%, really?
    print()
    print("-" * 72)
    print("Calibration: the substrate expansion variable ũ₀ sits INSIDE the window")
    print("-" * 72)

    miss_u0 = rel(deficit["muon"], u0)
    print(f"  ũ₀ (ladder expansion variable) = {mp.nstr(u0, 14)}")
    print(f"  deficit vs ũ₀                  = {mp.nstr(miss_u0 * 100, 4)} %")
    print(f"  deficit vs |S_leak(muon)|      = {mp.nstr(miss_mu * 100, 4)} %")
    print(f"  => the deficit is {mp.nstr(miss_mu / miss_u0, 4)}x CLOSER to ũ₀ than to |S(muon)|.")
    assert miss_u0 < miss_mu, "expected ũ₀ to be the closer of the two"
    print(
        "     ũ₀ carries no 4₁-volume content, so at a 2.9 % tolerance the match\n"
        "     does not discriminate a geometric reading from a numerological one."
    )


def main():
    u0 = defect_1_glyph_collision()
    defect_2_anchor_selective_scale(u0)
    print()
    print("=" * 72)
    print("ALL CHECKS PASSED — both defects confirmed from committed witnesses.")
    print("Scope-(a). Nothing refuted; nothing wired; no fit; no witness written.")
    print("=" * 72)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
