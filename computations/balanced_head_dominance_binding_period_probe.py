"""Head-dominance probe: is T_q(n) = sum dim_q concentrated on few balanced shapes at q_0?

Audit-only decisive probe (2026-07-03 audit
docs/audits/2026-07-03-parabolic-cylinder-channel-interpolation.md sec 11;
owner-approved follow-up to the sec-10 stable-range NEGATIVE).

Sec 10 established that the Deligne stable range (long-first-row shapes) captures a
collapsing fraction of the binding period T_q(n) at q_0 — the mass sits on BALANCED
shapes. The surviving question for a fast high-A evaluator: how concentrated is the
head? Measurements (no fit):

  (a) top-K capture: fraction of T_q(n) from the K largest dim_q terms, K = 1, 5, 20;
  (b) the argmax shape lambda*(n) and whether its aspect (rows/cols) is balanced;
  (c) head width: minimal K for 99% capture, vs p(n) — if K_99 grows slowly while
      p(n) grows super-polynomially, a head expansion is viable in principle.

Range n = 4..20 (p(20) = 627 — cheap numerically at 50 dps).

Discipline: measurement only; a "viable in principle" outcome does NOT wire anything —
generating the top shapes without full enumeration is the (harder) follow-up question.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import sys
from datetime import datetime, timezone

import mpmath as mp

from q_parameter import Q as Q0  # noqa: E402
from phase5_n8_dim_q_table import hook_lengths, partitions_of  # noqa: E402

DPS = 50
N_MIN, N_MAX = 4, 20
TOP_KS = (1, 5, 20)


def dim_q_numeric(lam: tuple[int, ...], q0: mp.mpf) -> mp.mpf:
    """Numeric symmetric-convention q-hook quantum dimension at q0 (canonical)."""
    def qi(h: int) -> mp.mpf:
        return (q0**h - q0**(-h)) / (q0 - q0**(-1))
    val = mp.mpf(1)
    for k in range(1, sum(lam) + 1):
        val *= qi(k)
    for h in hook_lengths(lam):
        val /= qi(h)
    return val


def main() -> int:
    mp.mp.dps = DPS
    q0 = mp.mpf(str(Q0))

    rows = {}
    print("    n |  p(n) |  top-1    top-5    top-20 |  K99  K99/p(n) | argmax shape (rows x cols)")
    for n in range(N_MIN, N_MAX + 1):
        parts = partitions_of(n)
        vals = sorted(((dim_q_numeric(lam, q0), lam) for lam in parts),
                      key=lambda t: t[0], reverse=True)
        T = mp.fsum(v for v, _ in vals)
        cum, k99 = mp.mpf(0), None
        capture = {}
        for k, (v, _) in enumerate(vals, start=1):
            cum += v
            if k in TOP_KS:
                capture[k] = cum / T
            if k99 is None and cum / T >= mp.mpf("0.99"):
                k99 = k
        for k in TOP_KS:
            if k not in capture:
                capture[k] = mp.mpf(1)
        lam_star = vals[0][1]
        aspect = f"{len(lam_star)}x{lam_star[0]}"
        rows[n] = {
            "p_n": len(parts),
            "top_capture": {str(k): mp.nstr(capture[k], 8) for k in TOP_KS},
            "K99": k99,
            "K99_over_pn": mp.nstr(mp.mpf(k99) / len(parts), 6),
            "argmax_shape": list(lam_star),
            "argmax_aspect_rows_x_cols": aspect,
        }
        print(f"   {n:2d} | {len(parts):5d} |  {float(capture[1]):.4f}   "
              f"{float(capture[5]):.4f}   {float(capture[20]):.4f} | {k99:4d}  "
              f"{float(mp.mpf(k99)/len(parts)):.4f} | {lam_star} ({aspect})")

    k99_ratio_falling = all(
        mp.mpf(rows[n + 1]["K99"]) / rows[n + 1]["p_n"]
        <= mp.mpf(rows[n]["K99"]) / rows[n]["p_n"] + mp.mpf("0.02")
        for n in range(max(N_MIN, 8), N_MAX))

    witness = {
        "description": ("Head-dominance of T_q(n)=sum dim_q at substrate q_0: top-K "
                        "captured fraction, argmax (balanced) shape, and 99%-head width "
                        "K99 vs p(n). Follow-up to the stable-range negative (audit "
                        "sec 10): measures whether a balanced-head expansion is viable "
                        "in principle for high-A binding-period evaluation."),
        "audit_only": True,
        "tier": "decisive measurement (no fit, no wiring)",
        "precision_dps": DPS,
        "constants": {"q_0": mp.nstr(q0, 20)},
        "range": {"n_min": N_MIN, "n_max": N_MAX},
        "per_n": {str(n): rows[n] for n in rows},
        "verdict": {
            "head_concentrated": bool(
                mp.mpf(rows[N_MAX]["top_capture"]["20"]) > mp.mpf("0.5")),
            "K99_fraction_of_pn_nonincreasing": bool(k99_ratio_falling),
        },
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    from witness_base import WitnessBuilder  # noqa: E402
    out = WitnessBuilder.wrap_legacy(
        "balanced-head-dominance-binding-period-probe", witness,
        script_path=__file__, engine="mpmath",
    ).save()
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
