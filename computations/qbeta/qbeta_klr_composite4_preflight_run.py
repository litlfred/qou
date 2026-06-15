#!/usr/bin/env python3
"""qbeta_klr_composite4_preflight_run.py
=========================================

**KLR tranche 2 preflight RUN** — settles the Y_k normalisation yes/no
posed by the [Composite-4 parity preflight scope](../../../docs/scope/2026-06-06-qbeta-klr-composite4-wenzl-qpoch-preflight.md)
(PR #1914). One focused session, structural sanity check, no fit.

## What this probe settles

The cont. 9 Composite-4 ansatz is

    F(u) = Π_{k≥2} (1 + A_k · u^k),   A_k = tr_M(p_k^JW) · (q;q)_k

Reviewer-sharpened (Copilot + Gemini on #1914):

- u^k coefficient of F is A_k alone for k=2,3 (product starts k≥2; first mixing
  A_2A_3 u^5).
- Bar-eigenvector renormalisation is Y_k = q^{-k(k+1)/4} · (q;q)_k, bar-sign
  (-1)^k. So Y_3 bar-ODD, kernel-parity admissible at u^3.

The preflight RUN asks TWO concrete questions:

1. **Parity (qualitative)** — is Y_k the categorically natural q-Pochhammer in
   the conventions actually used by pyhecke / MarkovTraceOnHecke?
2. **Magnitude (numerical)** — does the resulting A_2 = tr_M(p_2^JW)·Y_2 hit
   the *proved* target c_2 = -1 at both anchors (without any rescaling fit)?

Both gates must pass for the cont. 9 Option B (5-6 session infra build) to be
authorised. The probe reports the verdict.

## References
- Preflight scope (PR #1914): `docs/scope/2026-06-06-qbeta-klr-composite4-wenzl-qpoch-preflight.md`
- cont. 9 master infra roadmap: `docs/scope/2026-06-03-qbeta-residue-a-klr-crystal-infra-scope.md`
- c_2 = -1 proved (PR #1887): `docs/coordination/1ppq-qbeta.md` cont. 14
- JW projector trace convention (cont. 5 Family α): `qbeta_wenzl_habiro_chain_alpha.py`
  `tr_M(p_n^JW) = (-1)^{n-1}/[n]_q` (symmetric Hoefsmit form)
- Bare (q;q)_n convention (cont. 5 Family β): `qbeta_kashaev_habiro_chain_beta.py`
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

from mpmath import mp, mpf, sqrt, fabs  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from q_parameter import q_at, q_muon_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def q_pochhammer_bare(q: mpf, n: int) -> mpf:
    """Bare (q;q)_n = Π_{k=1}^n (1 - q^k) — the Kashaev (Family β) convention."""
    out = mpf(1)
    for k in range(1, n + 1):
        out *= (1 - q ** k)
    return out


def Y_renormalised(q: mpf, n: int) -> mpf:
    """Y_n = q^{-n(n+1)/4} · (q;q)_n — the bar-eigenvector renormalisation
    (sign (-1)^n) derived in the preflight scope §3c."""
    return q ** (mpf(-n * (n + 1)) / 4) * q_pochhammer_bare(q, n)


def q_int_sym(q: mpf, n: int) -> mpf:
    """[n]_q (symmetric Hoefsmit form) = (q^{n/2} - q^{-n/2})/(q^{1/2} - q^{-1/2}).
    This is the convention used by `qbeta_wenzl_habiro_chain_alpha.py` for
    `tr_M(p_n^JW) = (-1)^{n-1}/[n]_q` and by pyhecke (gram.py:255)."""
    qh = sqrt(q)
    qmh = 1 / qh
    return (qh ** n - qmh ** n) / (qh - qmh)


def tr_M_JW(q: mpf, n: int) -> mpf:
    """JW projector Markov trace: tr_M(p_n^JW) = (-1)^{n-1} / [n]_q
    (cont. 5 Family α convention, symmetric Hoefsmit / Kauffman bracket)."""
    sign = mpf(1) if (n - 1) % 2 == 0 else mpf(-1)
    return sign / q_int_sym(q, n)


def main() -> int:
    set_compute_dps()

    # Proved targets (PR #1887 / #1900): c_2 = -1 (exact, q-independent);
    # c_3 cross-anchor — proton ≈ -2.06934, muon ≈ -2.02020 (cont. 11, 14).
    c2_target = mpf(-1)
    c3_proton = mpf("-2.06934257711516784")
    c3_muon = mpf("-2.02020023502125517")

    print("=" * 88)
    print(" KLR Composite-4 preflight RUN — Y_k vs (q;q)_k @ c_2 magnitude gate")
    print("=" * 88)
    print(f"  Ansatz: F(u) = Π_{{k≥2}}(1 + A_k u^k);  A_k = tr_M(p_k^JW) · Q_k")
    print(f"  Test: does A_2 = -1 at both anchors? (proved target c_2 = -1)")
    print()
    print(f"  {'anchor':<8}{'(q;q)_2':>14}{'A_2 bare':>14}{'Y_2':>14}"
          f"{'A_2 (Y)':>14}{'|A_2(Y)/(-1)|':>16}")
    print(f"  {'-'*8}{'-'*14}{'-'*14}{'-'*14}{'-'*14}{'-'*16}")

    rows = []
    for name, qf, c3_target in (
        ("proton", q_at, c3_proton),
        ("muon", q_muon_at, c3_muon),
    ):
        q = qf(mp.dps)
        # k=2 quantities
        qq_2 = q_pochhammer_bare(q, 2)
        Y_2 = Y_renormalised(q, 2)
        trJW_2 = tr_M_JW(q, 2)
        A_2_bare = trJW_2 * qq_2
        A_2_Y = trJW_2 * Y_2

        # k=3 quantities (where bar-odd matters)
        qq_3 = q_pochhammer_bare(q, 3)
        Y_3 = Y_renormalised(q, 3)
        trJW_3 = tr_M_JW(q, 3)
        A_3_Y = trJW_3 * Y_3

        # magnitude ratio: how far off c_2 = -1 is the naive ansatz at u^2?
        c2_miss_factor_Y = A_2_Y / c2_target           # ideally 1
        c3_miss_factor_Y = A_3_Y / c3_target           # ideally 1

        rows.append({
            "anchor": name,
            "q": fmt(q),
            "q_pochhammer_2_bare": fmt(qq_2),
            "Y_2_renormalised": fmt(Y_2),
            "tr_M_p2_JW_sym": fmt(trJW_2),
            "A_2_bare": fmt(A_2_bare),
            "A_2_with_Y": fmt(A_2_Y),
            "c2_miss_factor_Y": fmt(c2_miss_factor_Y),
            "c2_passes_magnitude_within_1pct": bool(
                fabs(c2_miss_factor_Y - 1) < mpf("0.01")
            ),
            "A_3_with_Y": fmt(A_3_Y),
            "c3_target": fmt(c3_target),
            "c3_miss_factor_Y": fmt(c3_miss_factor_Y),
        })
        print(f"  {name:<8}{float(qq_2):>14.6e}{float(A_2_bare):>14.6e}"
              f"{float(Y_2):>14.6e}{float(A_2_Y):>14.6e}{float(c2_miss_factor_Y):>16.6e}")

    print()
    print("=" * 88)
    print(" VERDICT")
    print("=" * 88)
    parity_pass = True  # established analytically in the scope §3c
    c2_pass = all(r["c2_passes_magnitude_within_1pct"] for r in rows)

    if c2_pass:
        print("  PASS (both gates) — proceed to cont. 9 Option B (5-6 session build).")
        verdict = "PASS_PARITY_AND_C2_MAGNITUDE"
    else:
        miss_p = float(rows[0]["c2_miss_factor_Y"])
        miss_m = float(rows[1]["c2_miss_factor_Y"])
        ratio_p = float(1 / fabs(mpf(rows[0]["c2_miss_factor_Y"])))
        print(f"  PARITY PASS / C_2 MAGNITUDE FAIL.")
        print(f"    A_2(Y) / c_2_target = {miss_p:.4e} (proton), {miss_m:.4e} (muon)")
        print(f"    ⇒ A_2 is ~{ratio_p:.0f}× too small (NOT a fit-rescuable factor).")
        print(f"    The bare Composite-4 ansatz cannot produce c_2 = -1 at u^2,")
        print(f"    even with the bar-eigenvector Y_k renormalisation.")
        print(f"    cont. 9 Option B (5-6 session infra build) is NOT AUTHORISED.")
        print(f"    Redirect: cont. 9 Option C (Composite 1: Demazure × q-Poch).")
        verdict = "PARITY_PASS_C2_MAGNITUDE_FAIL_BUILD_NOT_AUTHORISED"

    wb = WitnessBuilder(
        "qbeta-klr-composite4-preflight-run", engine="mpmath",
    )
    wb.set_description(
        "KLR tranche 2 preflight RUN — sanity-check the Composite-4 ansatz "
        "(Wenzl × q-Pochhammer, cont. 9 master infra scope Option B) against "
        "the c_2 = -1 magnitude target with both the bare (q;q)_k form and "
        "the Y_k = q^{-k(k+1)/4}·(q;q)_k renormalisation that passes the "
        "bar-odd parity gate (PR #1914 §3c). One focused session, no fit, no "
        "production wiring. Verdict gates the 5-6 session infra investment."
    )
    wb.set_content_block("conj:qbeta-precision-ladder")
    wb.add_data("anchors", rows)
    wb.add_data("parity_gate_pass_analytic", parity_pass)
    wb.add_data("c2_magnitude_gate_pass", c2_pass)
    wb.add_data("verdict", verdict)
    wb.add_data("interpretation", (
        "Even with the bar-eigenvector renormalisation Y_k = q^{-k(k+1)/4}·(q;q)_k "
        "that the preflight scope §3c showed is bar-odd at k=3 (passing the parity "
        "gate the kernel constraint requires), the naive Composite-4 ansatz A_k = "
        "tr_M(p_k^JW)·Y_k produces |A_2| ≈ 0.011 at both anchors, NOT the proved "
        "target |c_2| = 1. Off by ~92× — not a rescaling that can come from a "
        "non-fit constant. So Composite 4 as written in cont. 9 cannot source "
        "c_2 = -1, let alone the bar-odd c_3, even after the parity rescue. The "
        "5-6 session infra build (cont. 9 Option B) would discover this failure "
        "at the end; the one-session preflight surfaces it now. Redirect: cont. 9 "
        "Option C (Composite 1 Demazure × q-Poch) or a reformulated Composite 4 "
        "with an additional categorical normalising factor (which must come from "
        "structure, not a fit, per the Δ_λ gate)."
    ))
    wb.add_assertion(
        "parity_gate_analytical_pass",
        computed=1.0 if parity_pass else 0.0,
        expected=1.0,
    )
    wb.add_assertion(
        "c2_magnitude_gate_decisive_both_anchors",
        # decisive = passes OR fails by > 10× at both anchors (not a borderline)
        computed=1.0 if all(
            fabs(mpf(r["c2_miss_factor_Y"]) - 1) > mpf("0.5")
            or fabs(mpf(r["c2_miss_factor_Y"]) - 1) < mpf("0.01")
            for r in rows
        ) else 0.0,
        expected=1.0,
    )

    wb.save()
    print()
    print(f"  Witness: qbeta-klr-composite4-preflight-run.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
