#!/usr/bin/env python3
# polynomial_q_not_applicable: probe of closed-form candidates at q_0
"""P3.A — Closed-form `f` candidate probe for Δ_coupling at magic shells.

Per docs/audits/2026-05-11-1ppb-gap-narrowing-plan.md §Path A and
content/quantum-observable-universe/braids-and-knots/conj-magic-shell-stabilization.md:160,
the empirical magic-shell anchor (extracted, NOT calibrated) is

    Δ_coupling(2, 2) = +13.20 MeV

obtained from doubly-magic ⁴He via the cross-coupling decomposition

    Δ_coupling(Z=2, N=2)
        = M(⁴He) − 2·M(D) + 2·Δ_cat(³He)
        = 28.211 − 15.014 = +13.20  MeV.

P3.A asks: which structural closed form `f` reproduces this value
when evaluated at the appropriate substrate parameter `t`?

The gap-narrowing plan lists four candidates (P1.1):

  C1  f₁(t) = log(1/t)
  C2  f₂(t) = 1/t − 1
  C3  f₃(t) = log Φ_q^{(∞)}(t)        (log of full Faddeev dilogarithm)
  C4  f₄(t) = KLR canonical-basis dim count at the relevant shell

The probe evaluates each candidate at three natural substrate values
of `t`:
  - t = q_0 ≈ 1.110            (full substrate parameter)
  - t = q_0 − 1 = 1/q_0·E_0    (β-decay-energy normalisation)
  - t = h(q_0) = q_0 − q_0⁻¹   (Hecke deformation parameter)

and reports the multiplicative factor `Δ_coupling / (E_0 · f(t))`
needed to match +13.20 MeV.  A candidate is "structurally promising"
if that factor is a small rational or matches a known categorical
invariant (n_strands, dim of a Casimir, etc.).

This is a DIAGNOSTIC PROBE, NOT a fit.  Per CLAUDE.md three-cal
discipline, calibrating Δ_coupling to AME is forbidden — this script
identifies which closed form the structural derivation should target,
not which one to tune.

Output: delta-coupling-closed-form-probe.witness.json
Reference blocks:
  - conj:magic-shell-stabilization
  - prop:beta-decay-energy-scale
  - thm:knot-mass-formula-unified
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

mp.mp.dps = 50

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_MP as Q0  # noqa: E402
from derived_masses import e_0_full_mev  # noqa: E402

# Empirical anchor (extracted from AME via the cross-coupling
# decomposition; see conj-magic-shell-stabilization.md:160).
DELTA_COUPLING_2_2_MEV = mp.mpf("13.20")


def f1_log_inv(t):
    """C1:  f₁(t) = log(1/t).  Vanishes at t=1 (q→1 base point)."""
    return -mp.log(t)


def f2_inv_minus_1(t):
    """C2:  f₂(t) = 1/t − 1.  Linear-leading at t→1."""
    return 1 / t - 1


def f3_log_phi_q_full(t):
    """C3:  f₃(t) = log Φ_q^{(∞)}(t)  where Φ_q is the full Faddeev
    quantum dilogarithm (infinite product form).  Numerically:

        Φ_q^{(∞)}(t) = Σ_{n≥0} t^n / (q;q)_n

    Truncated at n_max = 60 (sufficient at q_0 ≈ 1.11; per-term ratio
    ≈ t·q^n / (1−q^{n+1}) decays fast enough by n=60).
    """
    q = Q0
    total = mp.mpf(0)
    qq_n = mp.mpf(1)  # (q;q)_0 = 1
    t_n = mp.mpf(1)   # t^0 = 1
    for n in range(60):
        if n > 0:
            qq_n = qq_n * (1 - q ** n)  # extend (q;q)_{n-1} → (q;q)_n
            t_n = t_n * t
        if abs(qq_n) < mp.mpf("1e-50"):
            break
        total += t_n / qq_n
    if total <= 0:
        return mp.nan
    return mp.log(total)


def f4_klr_dim(_t):
    """C4:  f₄ = KLR canonical-basis dimension count at the doubly-magic
    (2,2) shell.  For S_4 (4 strands) under the KLR algebra the canonical
    basis has |dim| = number of standard Young tableaux of size 4 = 14
    (sum of f^λ for λ ⊢ 4: 1 + 3 + 2 + 3 + 1 = wait — actually 1+3+2+3+1 is
    for f^λ of partitions [4],[3,1],[2,2],[2,1,1],[1^4] = 1, 3, 2, 3, 1 → 10).

    For the (2,2) shell the relevant block is the one with content vector
    (1, 1, −1, −1) for S_4, dim = 2 (the [2,2] partition).

    This candidate is t-independent — included as a "what if Δ_coupling
    is purely combinatorial" sanity check.
    """
    return mp.mpf(2)  # dim of S_4 partition [2,2]


CANDIDATES = [
    ("C1_log_inv_t",       f1_log_inv,         "log(1/t)"),
    ("C2_inv_t_minus_1",   f2_inv_minus_1,     "1/t - 1"),
    ("C3_log_phi_q_full",  f3_log_phi_q_full,  "log Φ_q^{(∞)}(t)"),
    ("C4_klr_dim",         f4_klr_dim,         "KLR canonical-basis dim count"),
]


def t_values():
    """Three natural substrate values to evaluate `t` at."""
    h = Q0 - 1 / Q0
    return [
        ("q_0",        Q0),
        ("q_0_minus_1", Q0 - 1),
        ("h(q_0)",     h),
    ]


def main() -> int:
    print("=" * 78)
    print("P3.A — closed-form f candidate probe for Δ_coupling(2,2)")
    print("=" * 78)
    print(f"  q_0          = {mp.nstr(Q0, 12)}")
    print(f"  E_0 (full)   = {mp.nstr(e_0_full_mev(), 12)} MeV")
    print(f"  Δ_coupling target = {mp.nstr(DELTA_COUPLING_2_2_MEV, 6)} MeV")
    print()

    E_0 = e_0_full_mev()
    rows = []

    for cand_name, fn, label_human in CANDIDATES:
        for t_name, t_val in t_values():
            try:
                fval = fn(t_val)
                if mp.isnan(fval) or mp.isinf(fval):
                    raise ValueError("non-finite")
                # Direct prediction in MeV: E_0 · f(t)
                pred_MeV = E_0 * fval
                # Multiplicative factor needed to match Δ_coupling:
                if pred_MeV == 0:
                    factor = mp.nan
                else:
                    factor = DELTA_COUPLING_2_2_MEV / pred_MeV
                # Also: pure-combinatorial form (no E_0 prefactor)
                if fval == 0:
                    factor_no_E0 = mp.nan
                else:
                    factor_no_E0 = DELTA_COUPLING_2_2_MEV / fval
                row = {
                    "candidate": cand_name,
                    "candidate_human": label_human,
                    "t_name": t_name,
                    "t_value": float(t_val),
                    "f_at_t": float(fval),
                    "E0_times_f_MeV": float(pred_MeV),
                    "factor_to_match_Delta": float(factor),
                    "factor_no_E0_prefactor": float(factor_no_E0),
                }
                rows.append(row)
                print(f"  {cand_name:<22} @ t={t_name:<12} "
                      f"f={float(fval):+.6e}  "
                      f"E0·f={float(pred_MeV):+10.4f} MeV  "
                      f"need×{float(factor):+8.4f}")
            except Exception as exc:  # noqa: BLE001
                row = {
                    "candidate": cand_name,
                    "candidate_human": label_human,
                    "t_name": t_name,
                    "t_value": float(t_val),
                    "error": f"{type(exc).__name__}: {exc}",
                }
                rows.append(row)
                print(f"  {cand_name:<22} @ t={t_name:<12} ERROR: {exc}")

    # Identify candidates whose multiplicative factor is closest to
    # a small integer or simple fraction — the structurally-promising
    # ones.
    print()
    print("Candidates with |factor| close to 1, 2, 3, 1/2, 1/3:")
    SIMPLE = [mp.mpf(k) for k in (1, 2, 3, 4)] + \
             [mp.mpf(1) / k for k in (2, 3, 4)]
    promising = []
    for r in rows:
        f = r.get("factor_to_match_Delta")
        if f is None or not mp.isfinite(mp.mpf(f)):
            continue
        for s in SIMPLE:
            gap = abs(mp.mpf(f) - s) / s
            if gap < mp.mpf("0.05"):  # within 5%
                promising.append((r, float(s), float(gap)))
                print(f"  ✓ {r['candidate']} @ {r['t_name']}: "
                      f"factor ≈ {f:+.4f}, near {float(s):.4f} "
                      f"(gap {float(gap)*100:.2f}%)")

    builder = WitnessBuilder("delta-coupling-closed-form-probe", engine="mpmath")
    builder.set_description(
        "P3.A diagnostic probe: which closed form `f` reproduces the "
        "empirical magic-shell anchor Δ_coupling(2,2) = +13.20 MeV when "
        "evaluated at a natural substrate value t (q_0, q_0−1, or h(q_0))? "
        "Tests four candidates from the gap-narrowing plan: log(1/t), "
        "1/t−1, log Φ_q^{(∞)}(t), KLR canonical-basis dim. Candidates "
        "whose multiplicative match-factor is a small rational identify "
        "structural targets for the derivation; no fitting performed."
    )
    builder.set_content_block("conj:magic-shell-stabilization")
    builder.add_parameter("q_0", str(Q0))
    builder.add_parameter("E_0_full_MeV", str(e_0_full_mev()))
    builder.add_parameter("delta_coupling_target_MeV",
                           str(DELTA_COUPLING_2_2_MEV))
    builder.add_data("rows", rows)
    builder.add_data("promising_matches", [
        {"row": r, "near_value": near, "fractional_gap": gap}
        for (r, near, gap) in promising
    ])
    out = builder.save()
    print(f"\n  → wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
