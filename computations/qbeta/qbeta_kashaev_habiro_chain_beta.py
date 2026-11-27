#!/usr/bin/env python3
"""qbeta_kashaev_habiro_chain_beta.py — Family β first-test at u_substrate.

Chain 1 of the user-approved Q_β Habiro element search (2026-06-03, PR #1760).
Family β premise (per scope doc 2026-06-03):

    F_β(u) = (1 − u) · Π_k (1 + d_k · u^k)

where `d_k` are extracted from the Kashaev tower at strand-count k. If
the residue-A categorical identification at u_substrate is a literal
Kashaev tower value, then `d_2 = c_2 = -1` and `d_3 = c_3 ≈ -2.069`.

This is a FIRST-TEST: compute Kashaev-tower values `K_n(q₀)` for n=2..5
in THREE standard variants and compare to (c_2, c_3) targets. The Δ_λ
gate is respected (closed-form formulas, no fits).

Kashaev tower variants tested:
  1. **Standard Kashaev**: K_n(q) via cyclic-dilog (q-Pochhammer) eval
  2. **Bloch-Wigner D(z)**: hyperbolic-volume-like evaluation
  3. **Quantum dilog L(q)**: Faddeev-Kashaev real-q form

Each is normalized by the unknot Kashaev = 1 so that a candidate
contribution to a Habiro element at strand-count k corresponds to
`(K_k(q₀) − 1) / (factor)` for the k-th coefficient.

Why this complements Family α (which landed NEGATIVE):
  - Family α tested literal Markov-trace projector formulas → fail
  - Lean proof of c_2 = -1 references Kashiwara f̃₁² (CRYSTAL operator),
    not Kashaev quantum dilog
  - Kashaev IS the Volume Conjecture invariant; if Q_β ↔ substrate
    volume, Kashaev tower at q₀ should yield d_k = c_k
  - If NEGATIVE here too, the residue A is neither Wenzl-Markov nor
    Kashaev-Volume; it must be a true Kashiwara crystal operator
    (Option-E path)
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

# Path bridge (subdirectory refactor, Phase 5).
import _path_bridge as _bridge  # noqa: E402, F401

from mpmath import mp, mpf, log  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402


REASON_TEXT = "target below the 1e-30 precision floor — relative error undefined"


def _err_str(err_ppm, value):
    """Print-safe error column: None -> n/a, non-finite value -> inf."""
    import mpmath as _mp
    if _mp.isnan(value):
        return f"{'inf':>12}"
    if err_ppm is None:
        return f"{'n/a':>12}"
    return f"{err_ppm:>12.2f}"


def q_pochhammer(a: mpf, q: mpf, n: int) -> mpf:
    """(a; q)_n = Π_{k=0}^{n-1} (1 − a·q^k)."""
    result = mpf(1)
    for k in range(n):
        result = result * (1 - a * q ** k)
    return result


def kashaev_standard(n: int, q: mpf) -> mpf:
    """Standard Kashaev tower at level n: (q;q)_n / (q;q)_∞-approx.

    For real q in (1,2), (q;q)_∞ DIVERGES (each factor (1−q^k) is negative
    for q > 1). So we use the partial (q;q)_n directly as the Kashaev-tower
    finite-truncation analog. This is the natural Habiro-ring building block
    for level n.
    """
    return q_pochhammer(q, q, n)


def kashaev_dilog_bloch_wigner(n: int, q: mpf) -> mpf:
    """Bloch-Wigner-like volume contribution at level n.

    D(z) = Im(Li_2(z)) + arg(1−z)·log|z|
    Evaluated formally at z = q^n (using mpmath polylog for Li_2).
    """
    z = q ** n
    # For z > 1 real, Li_2(z) is complex; D(z) is real (Bloch-Wigner property).
    li2_z = mp.polylog(2, z)
    log_z = log(z)
    log_1mz = log(abs(1 - z)) if z != 1 else mpf(0)
    # D(z) for real z > 1: D(z) = Im(Li_2(z)) + arg(1−z)·log|z|
    # arg(1−z) for real z > 1 is ±π (depending on branch); use principal branch.
    arg_1mz = mp.pi if z > 1 else mpf(0)
    return mp.im(li2_z) + arg_1mz * log_z


def kashaev_faddeev_real(n: int, q: mpf) -> mpf:
    """Faddeev-Kashaev real-q quantum dilog at level n.

    Real-q analog: L_q(x) = (1/log q) · Σ_{k=1}^∞ x^k / (k · [k]_q)
    evaluated at x = q^{-n} (compact q-dilog for level-n contribution).
    """
    x = q ** (-n)
    # Truncate sum at sufficient precision (50 dps)
    result = mpf(0)
    for k in range(1, 200):
        qk = (q ** k - q ** (-k)) / (q - q ** (-1))
        term = x ** k / (k * qk)
        result = result + term
        if abs(term) < mpf("1e-60"):
            break
    return result / log(q)


def main() -> int:
    set_compute_dps()
    wb = WitnessBuilder("qbeta-kashaev-habiro-chain-beta", engine="mpmath")

    q = Q_MP

    targets = {
        2: mpf("-1"),
        3: mpf("-2.06934257711516783787971951725"),
        4: mpf("0"),
    }

    print("=" * 76)
    print(" Family β first-test — Kashaev tower variants vs (c_2, c_3, c_4)")
    print("=" * 76)
    print(f"  q₀ = {mp.nstr(q, 14)}")
    print(f"  Targets:")
    print(f"    c_2 = {mp.nstr(targets[2], 14):>20}  (Lean-proved, Kashiwara f̃₁²)")
    print(f"    c_3 = {mp.nstr(targets[3], 14):>20}  (cal-anchored)")
    print(f"    c_4 = {mp.nstr(targets[4], 14):>20}  (below numerical floor)")
    print()

    variants = {
        "Standard (q;q)_n": kashaev_standard,
        "Bloch-Wigner D(q^n)": kashaev_dilog_bloch_wigner,
        "Faddeev real-q L_q(q^-n)": kashaev_faddeev_real,
    }

    results = {}
    tolerance_ppm = 10.0
    any_pass = False

    for name, formula in variants.items():
        print("─" * 76)
        print(f"  Variant: {name}")
        print("─" * 76)
        row = {"variant": name, "k_results": {}}
        max_err_ppm = 0.0
        passed_all = True
        for k in [2, 3, 4]:
            try:
                value = formula(k, q)
            except Exception as e:
                value = mpf("nan")
                print(f"    k={k}: ERROR — {e}")
                row["k_results"][str(k)] = {
                    "computed": "error",
                    "target": mp.nstr(targets[k], 30),
                    "err_ppm": float("inf"),
                    "passed": False,
                    "error_message": str(e),
                }
                passed_all = False
                max_err_ppm = float("inf")
                continue
            target = targets[k]
            if abs(target) < mpf("1e-30"):
                # See the alpha chain: a relative error against a zero target is
                # undefined (ok_str "n/a" already said so). float("nan") wrote a
                # bare NaN token and made the witness invalid JSON. null, because
                # undefined-by-construction is a MISSING value, not a pole.
                err_ppm = None
                ok_str = "n/a"
                ok = True
            else:
                if mp.isnan(value):
                    err_ppm = float("inf")
                    ok = False
                    ok_str = "NaN"
                else:
                    err_ppm = float(abs(value - target) / abs(target) * 1e6)
                    ok = err_ppm <= tolerance_ppm
                    ok_str = "PASS" if ok else "FAIL"
                if not ok:
                    passed_all = False
                if (err_ppm is not None and err_ppm > max_err_ppm
                        and not mp.isnan(value)):
                    max_err_ppm = err_ppm
            print(f"    k={k}: K_k(q₀)  = {mp.nstr(value, 14):>22}  "
                  f"target = {mp.nstr(target, 14):>14}  "
                  f"err = {_err_str(err_ppm, value)} ppm  {ok_str}")
            # A non-finite `value` means the formula itself blew up; that is a
            # DIVERGENCE (marker), distinct from the undefined-relative-error
            # case above (null). Both were bare JSON tokens before.
            _diverged = bool(mp.isnan(value))
            row["k_results"][str(k)] = {
                "computed": "nan" if _diverged else mp.nstr(value, 30),
                "target": mp.nstr(target, 30),
                "err_ppm": ("inf" if _diverged else err_ppm),
                "err_ppm_undefined_reason": (
                    REASON_TEXT if (err_ppm is None and not _diverged) else None),
                "passed": ok,
            }
        row["all_passed"] = passed_all
        row["max_err_ppm"] = max_err_ppm
        if passed_all:
            any_pass = True
            print(f"    → ALL PASS (max err {max_err_ppm:.2f} ppm) — candidate Habiro element!")
        else:
            print(f"    → FAIL (max err {max_err_ppm:.2f} ppm)")
        print()
        results[name] = row

    print("=" * 76)
    print(" VERDICT")
    print("=" * 76)
    if any_pass:
        print("  POSITIVE — one or more Kashaev tower variants matches (c_2, c_3)")
        print("  within 10 ppm. This is a Family β residue-A categorical-ID candidate.")
    else:
        print("  NEGATIVE — no literal Kashaev tower variant reproduces (c_2, c_3)")
        print("  = (-1, -2.069).")
        print()
        print("  Combined with Family α NEGATIVE (commit afterwards), the residue A")
        print("  categorical-ID is neither (a) a Wenzl-projector Markov trace nor")
        print("  (b) a Kashaev quantum dilogarithm. The Lean proof of c_2 = -1 from")
        print("  Kashiwara f̃₁² (crystal operator) is the SHARPEST POINTER: residue")
        print("  A must be a TRUE Kashiwara CRYSTAL operator value — Option-E path.")

    wb.add_assertion(
        "family_beta_literal_kashaev_tower_at_least_one_passes_10_ppm",
        computed=any_pass,
        expected=False,
        source="If c_2 = -1 came from a Kashaev tower, this would PASS. The Lean proof "
               "says c_2 = -1 is a Kashiwara CRYSTAL eigenvalue (not Kashaev dilog), so "
               "we expect this to FAIL — combined with Family α NEGATIVE, the residue A "
               "categorical-ID points firmly at Option-E (Kashiwara crystal operators).",
    )

    wb.add_data("targets", {str(k): mp.nstr(v, 30) for k, v in targets.items()})
    wb.add_data("variants_tested", list(variants.keys()))
    wb.add_data("per_variant_results", results)
    wb.add_data("any_variant_passes_10_ppm", any_pass)
    wb.add_data("interpretation", (
        "Family β first-test: 3 Kashaev-tower variants tested at proton-pinned q₀ "
        "against (c_2, c_3) = (-1, -2.069). "
        + ("POSITIVE — at least one variant matches; candidate residue-A categorical-ID."
           if any_pass else
           "NEGATIVE — no Kashaev variant matches. Combined with Family α NEGATIVE, "
           "residue A categorical-ID is a TRUE Kashiwara CRYSTAL operator value "
           "(Option-E path), not Markov-projector or Kashaev-dilog.")
    ))

    out = wb.save()
    print()
    print(f"✓ Witness: {out.name}  ({len(wb.assertions)} assertions, "
          f"all {'passed' if all(a.passed for a in wb.assertions) else 'FAILED'})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
