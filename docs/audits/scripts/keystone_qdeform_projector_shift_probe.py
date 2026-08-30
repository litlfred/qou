#!/usr/bin/env python3
"""
q-deformed keystone (muon) shift — the E_λ-PROJECTED H_5 Markov trace.

This is the object the functor-resolution doc
(`docs/audits/2026-06-13-s5-so3-fiber-action-functor-resolution.md` §4 step 2)
asks for and that the "first crack" probe
(`docs/audits/2026-06-20-keystone-branching-shift-first-crack.md`) flagged as
STILL NOT RUN:

    > whether the q-deformed Wenzl projector weights w_λ(q) — as opposed to
    > classical multiplicities — break the (2,1) symmetry between the H_5 blocks.

The first-crack Model A weighted the (2,1) channel by the *H_3* Markov weight
y_ν^{H3} (generation-independent) × the classical branching multiplicity 2, so
the h⁴-bearing (2,1) term was identical in both generations and CANCELLED.

The correct §4-step-2 object is the **E_λ-projected H_5 Markov trace** of the
Borromean braid embedded in B_5:

    T_g = tr_M^{H5}( E_{λ_g} · ι(β_Bor) ) = y_{λ_g}^{H5} · χ^{λ_g}( ι(β_Bor) )

    muon:     λ = (3,2)    (ℓ=2 home block)
    electron: λ = (3,1,1)  (ℓ=1 home block)

Here ι(β_Bor) = (σ₁⁻¹σ₂)³ is the SAME Borromean braid word, now read on 5
strands (σ₃,σ₄ are spectators).  The branching is automatic inside χ^λ:

    χ^{(3,2)}(β)   = 1·χ_(3) + 2·χ_(2,1)
    χ^{(3,1,1)}(β) = χ_(1,1,1) + 2·χ_(2,1) + 1·χ_(3)

so the (2,1) channel (which carries the Borromean h⁴: χ_(2,1) = 2 − 3h⁴ − h⁶)
is present in BOTH — but now weighted by the *different* H_5 home-block weights
y_(3,2)^{H5} ≠ y_(3,1,1)^{H5}.  So unlike Model A, the (2,1)/h⁴ channel does NOT
cancel.  The question is the SIZE and the BAR-PARITY of the resulting shift.

DISCIPLINE (critical-distance + 2026-06-13 §1 + pyhk bean): the 210 ppb muon
figure is a re-pin ARTIFACT.  This script does NOT fit 1.000000210.  It reports
what the projected trace gives, its order of magnitude vs 210 ppb, and whether
the shift is bar-even (a precondition for being a sub-ppm correction candidate).

Tool: pyhecke_native v0.9.0 (built in-sandbox, PR #2511 recipe).
"""
import sys
from pathlib import Path

import pyhecke_native as ph
from mpmath import mp, mpf, mpmathify

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "computations" / "substrate"))
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
# The substrate pin is READ, not transcribed. This file previously carried
#     Q0 = "1.1099785955541805"          # tools/hecke-engine/src/gram.rs::Q_0
# -- the CODATA-2018 muon derivation B, 11.54 ppb from the canonical proton pin.
# Two files in this group cited `tools/hecke-engine/src/gram.rs::Q_0` as the
# source of that number; gram.rs was RE-PINNED to proton on 2026-08-15 (owner
# decision, bean `qou-m7py`) and now holds 1.1099785827513808, so the citation
# had outlived the value it pointed at. AGENTS.md's 2026-08-07 directive makes
# the experimental/proton pin the default for all touched compute.
#
# `docs/audits/scripts/` is outside `hardcoded_q0_literal_families_audit.py`'s
# `_SCAN_ROOT` (which is `computations/`), so nothing flagged these -- bean
# `qou-2whe`. Reading the pin means a future re-pin reaches this file without
# anyone editing a digit.
import sys as _sys, pathlib as _pl  # noqa: E402
_ROOT = _pl.Path(__file__).resolve().parents[3]
for _p in (_ROOT / "computations", _ROOT / "computations" / "substrate"):
    if str(_p) not in _sys.path:
        _sys.path.insert(0, str(_p))
from q_parameter import Q_50_DIGIT_STR as Q0  # noqa: E402
from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_numeric  # noqa: E402
DPS = 50
BORROMEAN = [(-1, 1), (1, 2)] * 3   # β = (σ₁⁻¹ σ₂)³, generators 1,2 only

H3 = [(3,), (2, 1), (1, 1, 1)]
BRANCH = {                          # classical S_5→S_3 multiplicities m(ν; λ)
    (3, 2):    {(3,): 1, (2, 1): 2, (1, 1, 1): 0},
    (3, 1, 1): {(3,): 1, (2, 1): 2, (1, 1, 1): 1},
}


def chi(lam, q):
    """χ^λ(β_Bor) on |λ| strands as an mpf."""
    return mpmathify(ph.chi_lambda_braid_mpfr(list(lam), BORROMEAN, q, DPS))


def weights5(q):
    """H_5 Markov weights y_λ, λ⊢5, as a dict.

    Was `ph.trace_weights_n(5, float(q))` wrapped in `mpf(str(w))`. That is a
    NO-FLOAT64 violation with a real consequence here, not a stylistic one: the
    `float(q)` downgrades the 50-dps pin to 53 bits, the Rust routine is float64
    internally (it returns a Python float even when handed an mpf), and the
    `mpf(str(...))` then dresses 53-bit data as 50 dps.

    What it cost: **four of the seven y_λ are EXACTLY ZERO** and the float64
    route returned noise for all four --

        lambda        float64 route          exact route
        (3,1,1)       1.094436485732e-17     0
        (2,2,1)       1.9631309013882e-17    0
        (2,1,1,1)     -3.2754415082272e-17   0
        (1,1,1,1,1)   3.5151413120942e-18    0

    -- while agreeing to 14 digits on the three that are nonzero. The zeros are
    structural, not accidental: y_λ = 0 exactly iff λ has MORE THAN TWO ROWS,
    which is the SU(2)/N=2 truncation. (5,), (4,1) and (3,2) have <= 2 rows and
    survive; every deeper partition is killed.

    This is the direct cause of the qou-j3u0 witness disagreement: the committed
    witness records y_(3,1,1) = 0.0167666089588 for a quantity that is exactly
    zero.
    """
    parts = [tuple(p) for p in ph.partitions_of(5)]
    return {p: y_lambda_wenzl_bridge_numeric(list(p), q) for p in parts}


def projected_traces(q):
    """(T_muon, T_electron, supporting dict) at substrate value q."""
    y5 = weights5(q)
    chi32 = chi((3, 2), q)
    chi311 = chi((3, 1, 1), q)
    Tmu = y5[(3, 2)] * chi32
    Te = y5[(3, 1, 1)] * chi311
    # H_3 branching cross-check (numerical)
    chi3 = {nu: chi(nu, q) for nu in H3}
    bran32 = mp.fsum(BRANCH[(3, 2)][nu] * chi3[nu] for nu in H3)
    bran311 = mp.fsum(BRANCH[(3, 1, 1)][nu] * chi3[nu] for nu in H3)
    return Tmu, Te, {
        "y_32": y5[(3, 2)], "y_311": y5[(3, 1, 1)],
        "chi_32": chi32, "chi_311": chi311,
        "chi3": chi3, "bran_check_32": bran32, "bran_check_311": bran311,
    }


def main():
    q = mpf(Q0)
    qbar = 1 / q
    print(f"pyhecke_native v{ph.__version__} | q_0 = {Q0} | dps = {DPS}\n")

    Tmu, Te, d = projected_traces(Q0)
    print("H_3 Borromean characters χ_ν:")
    for nu in H3:
        print(f"  ν={str(nu):<11} χ_Bor = {mp.nstr(d['chi3'][nu], 14)}")
    print()
    print("H_5 home-block weights and projected-block characters:")
    print(f"  (3,2)   : y^H5 = {mp.nstr(d['y_32'], 12)}   χ^(3,2)(β)   = {mp.nstr(d['chi_32'], 14)}")
    print(f"  (3,1,1) : y^H5 = {mp.nstr(d['y_311'], 12)}   χ^(3,1,1)(β) = {mp.nstr(d['chi_311'], 14)}")
    print()
    print("Branching cross-check  χ^λ(β) =? Σ_ν m(ν;λ) χ_ν(β)  (must be ~0):")
    print(f"  |χ^(3,2)   − [χ_(3)+2χ_(2,1)]|         = {mp.nstr(abs(d['chi_32']  - d['bran_check_32']), 4)}")
    print(f"  |χ^(3,1,1) − [χ_(1,1,1)+2χ_(2,1)+χ_(3)]| = {mp.nstr(abs(d['chi_311'] - d['bran_check_311']), 4)}")
    print()

    # --- the projected E_λ traces and their shift -------------------------
    delta = Tmu - Te
    rel_mu = delta / Tmu
    # T_e is EXACTLY zero (y_(3,1,1) = 0; see weights5), so delta/T_e is not a
    # large number -- it is undefined. It previously read 4.65e+15, which was
    # delta divided by the float64 noise floor and therefore a statement about
    # the arithmetic rather than about the traces.
    rel_e = None if Te == 0 else delta / Te
    print("E_λ-PROJECTED H_5 Markov traces  T_g = y_{λ_g}^{H5} · χ^{λ_g}(β):")
    print(f"  T_muon     (3,2)   = {mp.nstr(Tmu, 14)}")
    print(f"  T_electron (3,1,1) = {mp.nstr(Te, 14)}")
    print(f"  δ = T_μ − T_e      = {mp.nstr(delta, 14)}")
    print(f"  δ / T_μ            = {mp.nstr(rel_mu, 10)}")
    print("  δ / T_e            = UNDEFINED (T_e is exactly 0)" if rel_e is None
          else f"  δ / T_e            = {mp.nstr(rel_e, 10)}")
    print()

    # --- magnitude vs the 210 ppb anchor-shift (NO fitting) ---------------
    target = mpf("210e-9")
    print("Magnitude vs the 210 ppb muon re-pin artifact (NOT a fit target):")
    for name, val in (("δ/T_μ", rel_mu), ("δ/T_e", rel_e)):
        if val is None:
            print(f"  |{name}| / 210ppb = UNDEFINED (T_e is exactly 0 -- the "
                  f"(3,1,1) block carries no Markov weight at all)")
            continue
        ratio = abs(val) / target
        print(f"  |{name}| / 210ppb = {mp.nstr(ratio, 6)}  "
              f"({'too large' if ratio > 10 else 'too small' if ratio < 0.1 else 'ON-SCALE'} "
              f"by ~{mp.nstr(ratio if ratio>1 else 1/ratio, 3)}×)")
    print()

    # --- bar-parity: evaluate the shift at q and at 1/q -------------------
    Tmu_b, Te_b, _ = projected_traces(mp.nstr(qbar, 40))
    delta_b = Tmu_b - Te_b
    print("Bar-parity (q ↦ q⁻¹) of the shift δ:")
    print(f"  δ(q_0)    = {mp.nstr(delta, 14)}")
    print(f"  δ(1/q_0)  = {mp.nstr(delta_b, 14)}")
    s = delta + delta_b
    diff = delta - delta_b
    print(f"  δ(q)+δ(1/q) = {mp.nstr(s, 8)}   (≈0 ⟹ bar-ODD)")
    print(f"  δ(q)−δ(1/q) = {mp.nstr(diff, 8)}   (≈0 ⟹ bar-EVEN)")
    if abs(s) < abs(diff) * mpf("1e-6"):
        verdict = "bar-ODD"
    elif abs(diff) < abs(s) * mpf("1e-6"):
        verdict = "bar-EVEN"
    else:
        verdict = "bar-MIXED (neither even nor odd)"
    print(f"  ⇒ {verdict}")
    print()
    print("PROBE COMPLETE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
