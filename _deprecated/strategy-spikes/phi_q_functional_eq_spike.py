#!/usr/bin/env python3
"""Spike: Φ_q functional-equation / pentagon-identity route to λ_scale.

PR #928 audit listed three remaining open paths for deriving
λ_scale ≈ 2.4599527869. PR #939 audit closed the remaining "linear
PSLQ over substrate-natural q-dilog/Bloch basis" route as
empirically null. This spike opens the third, structurally distinct
path:

  **Φ_q functional equation.** Faddeev's quantum dilogarithm satisfies
  Φ_q(q·z) = (1/(1 - z)) · Φ_q(z), so ratios Φ_q(q·z)/Φ_q(z) carry
  structural information that linear PSLQ over individual Φ_q values
  cannot see. Pentagon identities (Φ_q(U)Φ_q(V) = Φ_q(V)Φ_q(UV)Φ_q(U)
  in non-commutative Heisenberg variables) give further structural
  constraints.

This spike probes:

  (1) **Direct functional-equation hits**: is λ_scale =
      1/(1 - z_*) for some substrate-natural z_* ∈ (0, 1)?
  (2) **Φ_q ratios at substrate-natural arguments**: compute
      Φ_q(z)/Φ_q(w) for z, w in {h_q, -h_q, ±h_q², 1/φ, 1/φ²,
      1/[2]_q, ...} and look for matches to λ_scale.
  (3) **Pentagon-implied identities**: for arg pairs (z, w),
      check whether
        Φ_q(z) · Φ_q(w) / Φ_q(z + w - zw)
      lands near λ_scale or its derived forms.

If any of (1)-(3) lands within mpf precision of λ_scale, that's a
candidate functional-equation closed form. If all exhaust to no
match within 1 ppb, that's another empirical constraint.

PSLQ not used here — the goal is to find *non-linear* relations,
not integer combinations.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _phi_q_util import phi_q
from q_parameter import Q_50_DIGIT_STR
from witness_base import WitnessBuilder


def main():
    t_start = time.monotonic()
    mp.mp.dps = 80

    Q0 = mp.mpf(Q_50_DIGIT_STR)
    Q0i = 1 / Q0
    h = Q0 - Q0i
    G = mp.catalan
    PHI = (1 + mp.sqrt(5)) / 2
    PHI_INV = 1 / PHI
    PHI_INV2 = 1 / (PHI * PHI)
    PI = mp.pi

    def qint(n):
        return (Q0**n - Q0**(-n)) / h

    lambda_p = mp.mpf("2.4599527869")
    print(f"target λ_p = {mp.nstr(lambda_p, 12)}")
    print(f"q_0       = {mp.nstr(Q0, 12)}")
    print(f"h_q       = {mp.nstr(h, 12)}")
    print()

    findings = []

    # ── (1) Direct functional-equation: λ_p = 1/(1 - z_*) ────────
    # If λ_p = Φ_q(q·z_*) / Φ_q(z_*), then by the functional eq.
    # Φ_q(qz) = (1/(1-z)) Φ_q(z), we get λ_p = 1/(1 - z_*) so
    # z_* = 1 - 1/λ_p.
    z_star = 1 - 1 / lambda_p
    print(f"(1) Functional-equation back-solve:")
    print(f"    z_* = 1 - 1/λ_p = {mp.nstr(z_star, 14)}")
    # Compare to substrate-natural candidates
    z_candidates = {
        "h_q":       h,
        "h_q²":      h * h,
        "1/φ":       PHI_INV,
        "1/φ²":      PHI_INV2,
        "1/[2]_q":   1 / qint(2),
        "1/[3]_q":   1 / qint(3),
        "1/[4]_q":   1 / qint(4),
        "(q-1)/q":   (Q0 - 1) / Q0,
        "(q-1)/(q+1)":  (Q0 - 1) / (Q0 + 1),
        "z_c_Re":    mp.mpf("0.10582958"),  # PL critical-point Re part
        "3/7":       mp.mpf(3) / 7,
    }
    best_z = (None, mp.inf)
    for name, val in z_candidates.items():
        diff = abs(val - z_star)
        rel = diff / abs(z_star) if z_star != 0 else mp.inf
        marker = " ← MATCH (<1 ppb)" if rel < mp.mpf(10)**(-9) else ""
        print(f"    z = {name:<22s} = {mp.nstr(val, 12)} (Δ/z_* = {mp.nstr(rel, 5)}){marker}")
        if diff < best_z[1]:
            best_z = (name, diff)
        if rel < mp.mpf(10)**(-9):
            findings.append({
                "path": "1-functional-eq-back-solve",
                "candidate": name,
                "value": mp.nstr(val, 16),
                "target_z_star": mp.nstr(z_star, 16),
                "rel_err": mp.nstr(rel, 8),
            })
    print(f"    closest: {best_z[0]} (|Δ| = {mp.nstr(best_z[1], 8)})")
    print()

    # ── (2) Φ_q ratios at substrate-natural arguments ────────────
    print(f"(2) Φ_q(z)/Φ_q(w) ratios:")
    ratio_vals = {
        "h_q":     h,
        "-h_q":    -h,
        "h_q²":    h*h,
        "-h_q²":   -h*h,
        "1/φ":     PHI_INV,
        "1/φ²":    PHI_INV2,
        "1/[2]_q": 1/qint(2),
        "(q-1)/q": (Q0 - 1)/Q0,
        "z_c_Re":  mp.mpf("0.10582958"),
    }
    phi_at = {}
    phi_eval_errors: list[str] = []
    for name, z in ratio_vals.items():
        if abs(z) >= 1 / Q0i:  # |z| < q convergence
            continue
        try:
            phi_at[name] = phi_q(z, Q0i)
        except Exception as e:
            phi_eval_errors.append(f"{name}: {type(e).__name__}: {e}")

    print(f"    Computed Φ_q at {len(phi_at)} substrate-natural arguments")
    matched_ratios = 0
    best_ratio_err = mp.inf
    for a in phi_at:
        for b in phi_at:
            if a == b:
                continue
            r = phi_at[a] / phi_at[b]
            rel = abs(r - lambda_p) / lambda_p
            if rel < mp.mpf(10)**(-3):  # within 0.1%
                marker = " ← <0.1%"
                print(f"    Φ_q({a:<10s}) / Φ_q({b:<10s}) = {mp.nstr(r, 10)} "
                      f"(Δ rel = {mp.nstr(rel, 5)}){marker}")
                matched_ratios += 1
                if rel < mp.mpf(10)**(-9):
                    findings.append({
                        "path": "2-phi-q-ratio",
                        "z": a,
                        "w": b,
                        "ratio": mp.nstr(r, 16),
                        "target": mp.nstr(lambda_p, 16),
                        "rel_err": mp.nstr(rel, 8),
                    })
            if rel < best_ratio_err:
                best_ratio_err = rel
    print(f"    {matched_ratios} ratios within 0.1% of λ_p (smallest err: {mp.nstr(best_ratio_err, 5)})")
    print()

    # ── (3) Pentagon-implied identities ───────────────────────────
    # 5-term Faddeev pentagon: Φ_q(U)Φ_q(V) = Φ_q(V)Φ_q(UV)Φ_q(U) for
    # Heisenberg pair UV = q²·VU. On the real line, the commutative
    # analog is:
    #     Φ_q(z) · Φ_q(w) = Φ_q(z + w − zw)  ?  (commutative Rogers)
    # This is the famous Rogers' identity for Li_2; the Faddeev
    # analog needs operator-theoretic interpretation. For numerical
    # spike: check whether Φ_q(z) · Φ_q(w) / Φ_q(z + w − zw) ≈ λ_p
    # for substrate-natural (z, w) pairs.
    print(f"(3) Pentagon-like ratios Φ_q(z) Φ_q(w) / Φ_q(z+w−zw):")
    pent_matched = 0
    best_pent_err = mp.inf
    for a in list(phi_at)[:6]:  # cap combinations
        for b in list(phi_at)[:6]:
            za, zb = ratio_vals[a], ratio_vals[b]
            zc = za + zb - za * zb
            if abs(zc) >= 1 / Q0i:
                continue
            try:
                phi_c = phi_q(zc, Q0i)
            except Exception as e:
                phi_eval_errors.append(f"phi_c({a}+{b}-{a}·{b}): {type(e).__name__}: {e}")
                continue
            v = phi_at[a] * phi_at[b] / phi_c
            rel = abs(v - lambda_p) / lambda_p
            if rel < mp.mpf(10)**(-3):
                marker = " ← <0.1%"
                print(f"    Φ_q({a}) Φ_q({b}) / Φ_q({a}+{b}−{a}·{b}) = "
                      f"{mp.nstr(v, 10)} (Δ rel = {mp.nstr(rel, 5)}){marker}")
                pent_matched += 1
                if rel < mp.mpf(10)**(-9):
                    findings.append({
                        "path": "3-pentagon-like",
                        "z": a, "w": b,
                        "value": mp.nstr(v, 16),
                        "rel_err": mp.nstr(rel, 8),
                    })
            if rel < best_pent_err:
                best_pent_err = rel
    print(f"    {pent_matched} pentagon-like values within 0.1% of λ_p "
          f"(smallest: {mp.nstr(best_pent_err, 5)})")
    if phi_eval_errors:
        print(f"    Note: {len(phi_eval_errors)} Φ_q evaluations failed (recorded in witness)")
    print()

    # Summary
    print(f"SUMMARY: {len(findings)} candidate <1 ppb matches found.")

    # Witness
    w = WitnessBuilder("phi-q-functional-eq-spike", engine="mpmath",
                       start_time=t_start)
    w.set_description(
        "Spike: Φ_q (Faddeev quantum dilog) functional-equation / "
        "pentagon-identity route to λ_scale ≈ 2.4599527869. Tests "
        "(1) λ_p = 1/(1 - z_*) back-solve against substrate-natural z, "
        "(2) Φ_q(z)/Φ_q(w) ratios, (3) commutative pentagon-like "
        "Φ_q(z)Φ_q(w)/Φ_q(z+w-zw) values. Companion to PR #888/892/"
        "904/923/928/939 — non-linear route distinct from PSLQ "
        "linear-combination tests."
    )
    w.set_content_block("conj:lambda-scale-bring-bloch-identity")
    w.add_parameter("dps", 80)
    w.add_data("z_star_target", mp.nstr(z_star, 20))
    w.add_data("closest_z_candidate", best_z[0])
    w.add_data("closest_z_diff", mp.nstr(best_z[1], 10))
    w.add_data("smallest_ratio_rel_err", mp.nstr(best_ratio_err, 10))
    w.add_data("smallest_pentagon_rel_err", mp.nstr(best_pent_err, 10))
    w.add_data("n_ppb_matches", len(findings))
    w.add_data("findings", findings)
    w.add_data("phi_eval_errors", phi_eval_errors)
    w.add_data("n_phi_eval_errors", len(phi_eval_errors))
    # Assertion fails (computed=0) if any Φ_q evaluation raised, so
    # the witness honestly reflects compute-state — not just whether
    # the script's main loop completed.
    w.add_assertion(
        "spike_completed_no_compute_errors",
        computed=float(len(phi_eval_errors) == 0),
        expected=1.0,
    )
    if findings:
        # Positive result — record but don't fail
        w.add_assertion(
            "candidate_ppb_match_found",
            computed=float(len(findings)),
            expected=float(len(findings)),
        )
    out = w.save()
    print(f"\nWitness: {out.name}")


if __name__ == "__main__":
    main()
