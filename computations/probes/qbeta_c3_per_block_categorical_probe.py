"""T2 probe: per-block categorical c_3 derivation from q_0.

The order audit `2026-05-31-qbeta-c3-order-audit-accidental-coincidence.md`
established that:

  • The per-Wedderburn-block contributions to Δtr_M live at order
    ε¹ = √u (ε = q-1).
  • The ladder c_3 lives at order ε⁶ = u³.
  • They are 5 ε-orders apart; the shared `−2` is a cross-order
    coincidence, not a value identity.
  • The OPEN problem is the categorical map
        f: Δtr_M (√u, ε¹) → Q_β (c_3 at u³, ε⁶)
    a q-dependent eigenphase/scaling map.

The T3 background exploration on this branch identified that the right
reframing is **per-block linear relations** (Wenzl annihilator at q = ζ_8
forcing constraints on the Markov-trace decomposition of pair-
differences), NOT a multiplicative prefactor as PR #1642's refuted ansatz.

This probe attempts the per-block c_3 derivation:

  c_3 = Σ_λ c_3^(λ)

where c_3^(λ) is the u³ Taylor coefficient of the per-block
Q_β^(λ) / Q_base ladder, derived from the per-block paper closed
forms χ_λ(β_n − β_p) AND the q_0 spectral data y_λ(q).

If each c_3^(λ) is a closed form in q_0 (not from fitting against
Q_codata), then c_3 IS a categorical function of q_0 — the keystone.

Acceptance criteria:

  AC-1: c_2 = Σ_λ c_2^(λ) = −1 (consistency — Lean-proved c_2 must
        reproduce as block-sum)
  AC-2: c_3 = Σ_λ c_3^(λ) reproduces measured c_3 = −2.0693 at q_0
        to compute precision (10⁻⁵⁰)
  AC-3: q_0 stability — re-evaluating Σ_λ c_3^(λ) at muon-pin q_0
        reproduces muon-pin c_3 = −2.0097 (matching the empirical
        2.88% cross-anchor swing structurally, NOT as a fit)

If AC-2 and AC-3 hold, the categorical c_3 derivation is achieved.

If AC-2 fails: the additive per-block ε-ladder decomposition is NOT
the right form, and the categorical map must mix per-block terms
non-trivially (perhaps via the Wenzl annihilator linear relation
identified in PR #1625).

If AC-2 holds but AC-3 fails: the per-block sum reproduces c_3 at the
fitting anchor but doesn't carry the q_0-dependence — the swing lives
elsewhere and the additive form is sound but incomplete.

This is a SCAFFOLD — the core arithmetic is a series-expansion probe
that takes < 2 minutes to run; full c_3 categorical derivation may
require additional structural reasoning in subsequent probes.
"""



from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402


# Paper's per-block χ_λ(β_n − β_p) closed forms — qbeta_per_block_paper_closed_forms.py:52
def chi_lambda_diff(q: sp.Symbol) -> dict[str, sp.Expr]:
    """Per-Wedderburn-block χ_λ(β_n − β_p) at n=3 (single-particle level).

    These are the differences χ_λ(β_n) − χ_λ(β_p), where β_p, β_n are
    the canonical Hecke-algebra braid representations of the proton
    and neutron at A=1. Algebraically simplified per the paper +
    `qbeta_per_block_paper_closed_forms.py`.
    """
    return {
        "(3)":     -(q**2 + 1)**2 * (q**2 - 1) / (4 * q),
        "(2,1)":   -(q**4 + 1) * (q**2 - 1) / (4 * q**3),
        "(1,1,1)": -(q**2 + 1)**2 * (q**2 - 1) / (4 * q**5),
    }


def load_q0_50_digit() -> str:
    """Load canonical q_0 substrate value (50-decimal-digit string)."""
    p = _pb.witness_path("q-pinning-50-digit.witness.json", HERE)
    data = json.load(open(p))
    return data["derived_50_digit"]["q"]


def load_y_lambda_at_q0() -> dict[str, mp.mpf]:
    """Load shadow weights y_λ(q_0) for n=3 partitions."""
    p = _pb.witness_path("y-lambda-at-q0.witness.json", HERE)
    data = json.load(open(p))
    out = {}
    for entry in data["data"]["by_n"]["3"]:
        ptn = tuple(entry["partition"])
        if ptn == (3,):
            label = "(3)"
        elif ptn == (2, 1):
            label = "(2,1)"
        elif ptn == (1, 1, 1):
            label = "(1,1,1)"
        else:
            continue
        out[label] = mp.mpf(entry["y_at_q0_50dps"])
    return out


def per_block_c_k_at_q0(q_str: str, K: int = 7) -> dict:
    """Compute per-block c_k coefficients (k = 0..K) at q_0.

    Per-block ε-series in (q − 1):
      χ_λ(β_n − β_p) = c_λ_ε¹·ε + c_λ_ε²·ε² + …

    Then the per-block contribution to Δtr_M is:
      f_λ(q) = y_λ(q) · χ_λ(β_n − β_p)(q)

    The full Δtr_M = Σ_λ f_λ.

    To get the per-block c_k of Q_β/Q_base − 1, we need the full
    machinery from Q_A (Form A) plus the N_1 cosine + Habiro ladder.
    Here we compute ONLY the per-block ε-series of f_λ at q=1 as the
    foundation; AC-2 and AC-3 require linking these to the u^k
    Habiro ladder which is itself an ε^(2k) series.

    Returns the per-block ε-series coefficients (k = 0..K) of f_λ,
    evaluated symbolically at q=1 and numerically at q_0.
    """
    mp.mp.dps = 65  # canonical precision

    q = sp.Symbol("q", positive=True)
    eps = sp.Symbol("eps", real=True)

    chi = chi_lambda_diff(q)
    y_at_q0 = load_y_lambda_at_q0()

    print("=" * 78)
    print("  Per-block ε-series at q = 1 (Taylor expansion of χ_λ(β_n − β_p))")
    print("=" * 78)
    series_at_eps = {}
    for shape, expr in chi.items():
        s = sp.series(expr.subs(q, 1 + eps), eps, 0, K + 1).removeO()
        coefs = [sp.simplify(s.coeff(eps, k)) for k in range(K + 1)]
        series_at_eps[shape] = coefs
        print(f"  χ_{shape}(β_n − β_p) ≈ {s}")
    print()

    print("=" * 78)
    print("  Leading per-block coefficients (ε¹ and ε²) — order-audit table:")
    print("=" * 78)
    table = []
    total_eps1 = sp.Integer(0)
    for shape, coefs in series_at_eps.items():
        c1 = coefs[1]
        c2 = coefs[2]
        total_eps1 += c1
        table.append((shape, c1, c2))
        print(f"  {shape}:  ε¹ = {c1}    ε² = {c2}")
    print(f"  Σ ε¹ = {sp.simplify(total_eps1)}  "
          f"(should match −5 per the order audit)")
    print()

    # ─── Numerical at q_0 ───────────────────────────────────────────
    q0 = mp.mpf(q_str)
    print("=" * 78)
    print(f"  Per-block at q_0 = {mp.nstr(q0, 12)}")
    print("=" * 78)

    chi_at_q0 = {}
    f_lambda_at_q0 = {}
    sum_f = mp.mpf(0)
    for shape, expr in chi.items():
        v = mp.mpf(str(sp.N(expr.subs(q, sp.Float(q_str, 50)), 50)))
        chi_at_q0[shape] = v
        f = y_at_q0[shape] * v
        f_lambda_at_q0[shape] = f
        sum_f += f
        print(f"  y_{shape} = {mp.nstr(y_at_q0[shape], 12)}, "
              f"χ_{shape} = {mp.nstr(v, 12)}, "
              f"f_{shape} = {mp.nstr(f, 12)}")
    print(f"  Σ f_λ = Δtr_M(q_0) = {mp.nstr(sum_f, 12)}")
    print()

    return {
        "epsilon_series_per_block": {
            shape: [str(sp.simplify(c)) for c in coefs]
            for shape, coefs in series_at_eps.items()
        },
        "total_epsilon_1_coefficient": str(sp.simplify(total_eps1)),
        "chi_at_q0": {s: str(v) for s, v in chi_at_q0.items()},
        "y_at_q0": {s: str(v) for s, v in y_at_q0.items()},
        "f_lambda_at_q0": {s: str(v) for s, v in f_lambda_at_q0.items()},
        "sum_f_lambda_at_q0": str(sum_f),
    }


def main() -> int:
    t0 = time.perf_counter()
    q_str = load_q0_50_digit()
    print(f"q_0 = {q_str[:30]}...")
    print()

    result = per_block_c_k_at_q0(q_str, K=7)

    # The next step (c_3 derivation) requires:
    #   1. Form A archimedean Q_A formula at q (= m_e·|q² − 2q − 1|·(q+1) / (2q³))
    #   2. N_1 cosine factor (cos(α − bℏ²/2)) at q
    #   3. The c_2·u² Habiro correction (Taylor-exact −1)
    #   4. The full Q_β/Q_base series expansion in u = b·ℏ_q²
    #   5. Compute u³ coefficient = c_3 and compare to measured −2.0693
    #
    # Implementing those 5 steps + the per-block additive split is the
    # follow-up probe. The scaffold here provides the per-block ε¹/ε²
    # structural data + the q_0 numerical values that the next probe
    # will consume.

    payload = {
        "computation": "qbeta-c3-per-block-categorical-probe",
        "description": (
            "T2 scaffold for per-block categorical c_3 derivation. "
            "Reproduces the order-audit ε-series per Wedderburn block "
            "and provides q_0 numerical values of y_λ, χ_λ, f_λ "
            "for the (n − p) pair-difference. The full c_3 derivation "
            "(connecting per-block ε¹ data to u³ ladder coefficient via "
            "a level-2 SU(2) Wenzl eigenphase / scaling map) is the "
            "follow-up probe — this scaffold provides the foundational "
            "per-block decomposition data."
        ),
        "reference_blocks": [
            "docs/audits/2026-05-31-qbeta-c3-order-audit-accidental-coincidence.md",
            "docs/audits/2026-06-01-qbeta-habiro-zeta8-categorical-witness.md",
            "docs/audits/2026-06-01-qbeta-habiro-a6-refutes-refined-scaling-law.md",
            "PR #1625 (level-2 SU(2) Wenzl identification)",
            "PR #1642 (multiplicative-prefactor ansatz REFUTED)",
            "PR #1649 (this branch)",
        ],
        "data": result,
        "acceptance_criteria": {
            "AC-1_c2_sum_equals_minus_one":
                "PENDING — requires implementing per-block c_2 via "
                "full Q_β/Q_base series.",
            "AC-2_c3_sum_reproduces_measured":
                "PENDING — requires implementing per-block c_3 via "
                "u³ Taylor coefficient.",
            "AC-3_q0_stability":
                "PENDING — requires re-evaluating at muon-pin q_0.",
        },
        "next_steps": [
            "Build Form A archimedean Q_A^(λ) per block",
            "Apply N_1 cosine factor + c_2 = -1 correction",
            "Compute u³ Taylor coefficient per block",
            "Sum and compare to measured c_3 = -2.0693 at proton-anchor q_0",
            "Re-evaluate at muon-anchor q_0 and check 2.88% swing structurally",
        ],
    }
    wb = WitnessBuilder.wrap_legacy(
        name="qbeta-c3-per-block-categorical-probe",
        payload=payload,
        script_path=__file__,
        engine="sympy series + mpmath 65 dps",
        output_dir=HERE,
    )
    wb.save()
    elapsed = time.perf_counter() - t0
    print(f"\n  Elapsed: {elapsed:.1f} s")
    print(f"  Witness: qbeta-c3-per-block-categorical-probe.witness.json")
    print()
    print("Next probe: complete c_3 derivation per the 'next_steps' field.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
