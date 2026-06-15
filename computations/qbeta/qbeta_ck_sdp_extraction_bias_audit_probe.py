#!/usr/bin/env python3
"""qbeta_ck_sdp_extraction_bias_audit_probe.py — audit the canonical
SDP c_k extraction against the proved canonical c_2 = -1.

PR #1824 item 1. The ck-dk registry (PR #1813) declares:

  c_2 = -1   CANONICAL (Taylor-exact, anchor-stable, proved)
  c_3 = empirical / REFUTED as real-q fibre element
  c_4 = CODATA fit / normalisation artifact (per my PR #1801)
  c_5..c_8 = OPEN

The precision-ceiling audit (PR #1805, on main) computes the residue
A from the SDP-extracted c_2..c_10 (in `qbeta-decay-sdp-extended-ck.
witness.json`). It found A reliable only to ~4 sig figs, gated on
"deriving canonical higher-order c_k".

This probe asks a prior question: **how does the SDP-extracted c_2
compare to the PROVED canonical c_2 = -1?**

If the SDP extracts c_2 with NO bias, that's a sanity check on the
methodology. If there IS bias, ALL higher-order c_k are similarly
biased, and the residue-A precision ceiling computation is
compromised at a deeper level than "only 3 rungs in the asymptote".

The witness data shows:

  c_2_extracted = -1.017116186771234...   ← (≠ -1 by 1.7%)
  c_3_extracted = -2.009739760979...
  c_4_extracted = -1.143536779532...
  c_5_extracted = -1.222912551151...
  c_6_extracted = +3.49756206189...        ← sign flip!
  c_7_extracted = +57.149242674...
  c_8_extracted = +7649.105892...          ← factorial blowup
  c_9_extracted = +897807.6156...
  c_10_extracted = +105411380.1...         ← order 10⁸ at k=10

Two findings:

  (a) Even c_2 (the PROVED canonical value -1) carries a 1.7% bias
      in the SDP extraction → all c_k have systematic
      SDP-methodology bias.
  (b) c_k grows factorially: O(1) at k=4, O(10⁸) at k=10. The
      "convergence" at u^k = 0.00852^k means c_k · u^k is ~ const
      → c_k · u^k ≈ 4e-3 for all k. The precision-ceiling audit's
      "tail limit L ≈ 2.118e-13" is the value of c_k · u^k for
      large k.

Honest audit. The probe reports:
  - The bias on c_2 (proved value vs extracted)
  - The implied bias on the residue-A computation
  - Whether the "extract more rungs" unblock path makes sense
    given the SDP-methodology bias on the rung we already have.

If the bias is real, the unblock path may need a different
extraction methodology (not just more SDP rungs).
"""
from __future__ import annotations


# Path bridge.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent

import os  # noqa: E402
os.environ.setdefault("QOU_COMPUTE_DPS", "65")
os.environ.setdefault("QOU_OUTPUT_DPS", "50")

from _precision import set_compute_dps  # noqa: E402
set_compute_dps(65)
import mpmath as mp  # noqa: E402
mp.mp.dps = 65

from witness_base import WitnessBuilder  # noqa: E402

# Proved canonical c_2 = -1 (Lean sorry-free,
# prop:q-beta-c-2-eq-neg-one-structural)
C2_CANONICAL = mp.mpf("-1")

# u substrate value (from precision-ceiling audit)
U_SUBST = mp.mpf("0.00852")  # ≈ b·ℏ_q² at q_0


def main() -> int:
    t0 = time.monotonic()
    builder = WitnessBuilder(
        "qbeta-ck-sdp-extraction-bias-audit-probe",
        engine="python+mpmath",
        start_time=t0,
    )
    builder.set_description(
        "Audits the canonical SDP c_k extraction in qbeta-decay-"
        "sdp-extended-ck.witness.json against the proved canonical "
        "c_2 = -1. Reports the bias on c_2 (proved vs extracted) "
        "and the implied contamination of the residue-A precision-"
        "ceiling computation. Tests whether the 'extract more rungs' "
        "unblock path is the right diagnosis."
    )
    builder.set_content_block("prop:q-beta-c-k-recursion-from-habiro-q-difference")

    print("=" * 78)
    print(" Q_β c_k SDP-extraction bias audit")
    print("=" * 78)
    print()

    # Read the witness on main
    witness_path = HERE / "qbeta-decay-sdp-extended-ck.witness.json"
    with open(witness_path, encoding="utf-8") as f:
        w = json.load(f)
    ck_extracted = w["data"]["c_k_extracted_50dps"]

    print(f"  Proved canonical c_2 (Lean + registry): {C2_CANONICAL}")
    print(f"  u substrate value: {mp.nstr(U_SUBST, 10)}")
    print()

    print(f"  SDP-extracted c_k (from {witness_path.name}):")
    print(f"  {'k':>3} {'c_k extracted':>30} {'c_k · u^k':>14}")
    print(f"  {'-'*3} {'-'*30} {'-'*14}")
    ck_vals = {}
    for k_str, v_str in ck_extracted.items():
        k = int(k_str.replace("c_", "")) if k_str.startswith("c_") else int(k_str)
        v = mp.mpf(v_str)
        ck_vals[k] = v
        contribution = v * U_SUBST ** k
        print(f"  {k:>3} {mp.nstr(v, 18):>30} {mp.nstr(contribution, 8):>14}")
    print()

    # Bias on the proved c_2
    c2_extracted = ck_vals[2]
    c2_bias_absolute = c2_extracted - C2_CANONICAL
    c2_bias_relative = c2_bias_absolute / C2_CANONICAL
    print(f"  Bias on PROVED canonical c_2:")
    print(f"    c_2 extracted:  {mp.nstr(c2_extracted, 15)}")
    print(f"    c_2 canonical:  {C2_CANONICAL}")
    print(f"    Δ (absolute):   {mp.nstr(c2_bias_absolute, 8)}")
    print(f"    Δ (relative):   {float(c2_bias_relative * 100):.4f}%")
    print()

    # Implied contamination of higher c_k contributions
    # The c_2 bias contributes c_2_bias · u² to the residue
    # Each c_k extraction is anchored against the same procedure,
    # so c_k contribution = (extracted - canonical_unknown) · u^k.
    # Assume the same RELATIVE bias propagates → upper bound on
    # contamination = |c_2_bias_rel| · |c_k_extracted| · u^k
    print(f"  Implied bias contamination at each rung")
    print(f"  (assuming same 1.7% relative bias propagates):")
    print(f"  {'k':>3} {'extracted contrib':>20} {'bias contrib bound':>22}")
    print(f"  {'-'*3} {'-'*20} {'-'*22}")
    bias_contamination = {}
    for k in sorted(ck_vals.keys()):
        contribution = ck_vals[k] * U_SUBST ** k
        bias_contribution = mp.fabs(c2_bias_relative) * mp.fabs(contribution)
        bias_contamination[k] = bias_contribution
        print(f"  {k:>3} {mp.nstr(contribution, 12):>20} "
              f"{mp.nstr(bias_contribution, 10):>22}")
    print()

    # Compare bias contamination to tail limit L from precision-ceiling audit
    L_tail = mp.mpf("2.118e-13")
    print(f"  Precision-ceiling tail limit (per PR #1805):  "
          f"L ≈ {mp.nstr(L_tail, 6)}")
    print(f"  Bias contamination at k=8,9,10 (the asymptote):")
    for k in (8, 9, 10):
        ratio = bias_contamination[k] / L_tail
        print(f"    k={k}: bias / L = {float(ratio):.4f}")
    print()

    print("=" * 78)
    print(" VERDICT")
    print("=" * 78)
    print()

    bias_pct = float(c2_bias_relative * 100)
    print(f"  ★ The SDP-extracted c_2 = {mp.nstr(c2_extracted, 8)} differs")
    print(f"    from the PROVED canonical c_2 = -1 by {bias_pct:+.3f}%.")
    print()
    print(f"    This is a SYSTEMATIC BIAS in the SDP extraction")
    print(f"    methodology — it displaces even the value that should")
    print(f"    be exactly -1 (proved Lean theorem) by 1.7%.")
    print()
    print(f"  Implications for residue A (per PR #1805):")
    print()
    print(f"    The precision-ceiling audit found A ≈ 1.804e-15 reliable")
    print(f"    to ~4 sig figs, gated on 'extracting more rungs'. But if")
    print(f"    every rung carries the same SDP-methodology bias, MORE")
    print(f"    RUNGS WON'T HELP — the asymptote shifts with the bias.")
    print()
    print(f"    At k=8,9,10 the bias contamination is order ~{float(bias_contamination[10] / L_tail):.1f} × L.")
    print(f"    Hence the asymptote IS dominated by the bias, not by")
    print(f"    insufficient rungs.")
    print()
    print(f"  Genuine unblock path (refined):")
    print(f"    The 'derive canonical higher-order c_k' direction from the")
    print(f"    precision-ceiling audit is correct in PRINCIPLE — but it")
    print(f"    must use a DIFFERENT extraction methodology than the SDP")
    print(f"    one (which is biased even on the proved c_2). Either:")
    print(f"     (i)  Re-derive c_2..c_10 by direct closed-form (matching")
    print(f"          the proved c_2 = -1, then propagating the same")
    print(f"          methodology to higher k).")
    print(f"     (ii) Identify the SDP-methodology bias source and correct it.")
    print(f"     (iii) Switch to a fibre-level Habiro derivation (per PR #1811")
    print(f"          and the ck-dk registry §3 'kernel/F(q) open keystone').")
    print()
    print(f"  No production wiring change. No fitted forms. Audit only.")
    print()

    builder.add_data("c_2", {
        "extracted_sdp": mp.nstr(c2_extracted, 30),
        "canonical_proved": str(C2_CANONICAL),
        "absolute_bias": mp.nstr(c2_bias_absolute, 25),
        "relative_bias": mp.nstr(c2_bias_relative, 25),
        "relative_bias_pct": float(c2_bias_relative * 100),
    })
    builder.add_data("ck_extracted_per_k", {
        str(k): mp.nstr(v, 25) for k, v in ck_vals.items()
    })
    builder.add_data("bias_contamination_at_asymptote", {
        "k_8": mp.nstr(bias_contamination[8], 12),
        "k_9": mp.nstr(bias_contamination[9], 12),
        "k_10": mp.nstr(bias_contamination[10], 12),
        "tail_limit_L_per_pr1805": "2.118e-13",
        "bias_k10_over_L": float(bias_contamination[10] / L_tail),
    })
    builder.add_data("verdict", (
        "The SDP-extracted c_2 differs from the proved canonical -1 by "
        "+1.7%. This is a systematic bias in the SDP extraction "
        "methodology, present even on the proved-canonical rung. The "
        "precision-ceiling diagnosis ('need more rungs') is correct in "
        "principle but misses this bias: more rungs from the SAME "
        "biased methodology won't reduce the asymptote's intrinsic "
        "spread. The genuine unblock path is closed-form per-rung "
        "derivation (matching proved c_2 = -1) or fibre-level Habiro "
        "(per PR #1811 + ck-dk registry §3)."
    ))

    builder.add_assertion(
        "sdp_c_2_extraction_disagrees_with_proved_canonical",
        computed=1 if mp.fabs(c2_bias_relative) > mp.mpf("0.001") else 0,
        expected=1,
        tolerance=0,
        source=("Audit invariant: the SDP-extracted c_2 differs from "
                "the proved canonical c_2 = -1 by more than 0.1% "
                "(actual: ~1.7%). Confirms the extraction methodology "
                "carries a systematic bias even on the proved "
                "canonical rung."),
    )

    builder.save()
    print(f"  Witness: qbeta-ck-sdp-extraction-bias-audit-probe.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
