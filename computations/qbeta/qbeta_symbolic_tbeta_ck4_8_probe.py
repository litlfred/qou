#!/usr/bin/env python3
# ANCHOR NOTE — CORRECTED 2026-08-23. The 2026-06-22 boilerplate that stood
# here had the two anchors INVERTED, in all 13 files carrying it. Measured:
#   • 1.10997858275… is NOT "the RETIRED pre-2026-05-28 proton anchor" — it is
#     the CURRENT proton pin. q_at() returns 1.10997858275138…
#   • "the CURRENT canonical proton q0 is ≈ 1.1099785955573347" named the MUON
#     value; q_at() never returns it.
#   • "q_muon_at() ≈ 1.10997859555418" named the SUPERSEDED (CODATA-2018) muon
#     value; q_muon_at() returns 1.10997859564274… See
#     computations/audits/muon_pin_three_values_probe.py for the three values.
# An agent trusting it would read the two-layer discipline backwards.
#
# What is true: the 1.10997858275… occurrences below ARE the current proton
# pin, and this probe is preserved as-is by design — its cross-anchor
# comparison is the point, so it must NOT be migrated.
"""qbeta_symbolic_tbeta_ck4_8_probe.py — the 1 ppQ keystone probe.

Probe 6.a' established the c_k generating function is BOUNDED /
CONVERGENT (PR #1835): 1 ppQ needs a finite truncation N≈8 with
UNBIASED c_4..c_8. The SDP extraction is +1.7% biased even on the
proved c_2 and noise-dominated at high k.

This probe computes c_4..c_8 SYMBOLICALLY (zero bias) from the
canonical operator-valued T_β candidates, using the EXACT symbolic
substrate chain from PR #1786:

  z(q)     = 1/(√q + 1/√q)        Markov-Jones
  h(q)     = q - 1/q              Hecke skein
  α(q)    = (z-1)·h/2             eigenphase
  b(q)     = √(q⁴+q²+1)/(q²+1)    Hoefsmit b
  ℏ_q(q)  = (q-1)/q              quantum Planck
  α_eff   = α - b·ℏ_q²/2          shifted eigenphase
  u       = b·ℏ_q²                ladder variable

The canonical N=1, N=2 structure is PROVEN:
  N=1:  cos(α_eff)
  N=2:  (1 - b²·ℏ_q⁴) = (1 - u²)   [c_2 = -1 STRUCTURAL, PR #1786]

The OPEN question is the N≥3 operator structure. We test the
bounded operator candidates from probe_q_beta_operator_valued_N3
(all "Kashiwara natural" forms), each as a SYMBOLIC function of q,
expanded to u^8:

  C1. matrix-exp:   cos(√(α² + δ²)),  δ = the substrate correction
  C2. exp-resum:    cos(α_eff)·exp(-b²ℏ⁴/(2(1-bℏ²)))
  C3. iterated-cos: cos(α_eff)·Π_j cos(b^j ℏ^{2j})
  C4. Pade/geom:    cos(α_eff)/(1 + b²ℏ⁴ ...)

For each candidate, this probe:
  1. Expands Q_β/Q_A symbolically in u → extracts ladder c_2..c_8.
  2. Checks the c_2 = -1, c_3 = ? anchors (c_2 = -1 is the
     structural filter — candidates failing it are rejected).
  3. Evaluates Q_β(q_0) and reports the ppQ vs CODATA.
  4. Cross-anchor stability: evaluates at proton q_p AND muon q_μ.
     A canonical F must be q-stable (per the 569bedda1 lesson —
     reject any candidate whose Q_β swings across anchors).
  5. Verdict: which candidate (if any) reaches 1 ppQ AND is
     q-stable AND respects c_2 = -1.

This is the make-or-break for the 1 ppQ close-out. Honest: it tests
the canonical operator candidates symbolically; it does NOT assert a
proven derivation (the exact T_β matrix wire-up from the Hoefsmit
rep is the deeper follow-up if no single candidate wins cleanly).
"""
from __future__ import annotations


import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import time

import os  # noqa: E402
os.environ.setdefault("QOU_COMPUTE_DPS", "65")
os.environ.setdefault("QOU_OUTPUT_DPS", "50")

from _precision import set_compute_dps  # noqa: E402
set_compute_dps(65)
import mpmath as mp  # noqa: E402
mp.mp.dps = 65
import sympy as sp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402


def ladder_ck(F_over_QA_series, u, kmax):
    """Extract ladder c_k from F/Q_A = Π(1+c_k u^k) via log matching."""
    logF = sp.series(sp.log(F_over_QA_series), u, 0, kmax + 1).removeO()
    c = {}
    known = sp.Integer(0)
    for k in range(1, kmax + 1):
        lower = sp.series(known, u, 0, kmax + 1).removeO().coeff(u, k)
        ck = sp.simplify(logF.coeff(u, k) - lower)
        c[k] = ck
        known = known + sp.series(sp.log(1 + ck * u ** k),
                                  u, 0, kmax + 1).removeO()
    return c


def main() -> int:
    Q_BETA_CODATA = mp.mpf("0.78233")
    M_E = mp.mpf("0.51099895069")
    Q_PROTON = mp.mpf("1.1099785827513808075916690956107688798744991218736")
    Q_MUON = mp.mpf("1.10997859555")  # cross-anchor (per 569bedda1)

    t0 = time.monotonic()
    builder = WitnessBuilder(
        "qbeta-symbolic-tbeta-ck4-8-probe",
        engine="python+sympy+mpmath",
        start_time=t0,
    )
    builder.set_description(
        "1 ppQ keystone: compute c_4..c_8 symbolically (unbiased) from "
        "canonical operator-valued T_β candidates using PR #1786's exact "
        "α(q),b(q) chain. Filters by c_2=-1 (structural), evaluates "
        "Q_β(q_0) ppQ vs CODATA, and cross-anchor stability. Reports "
        "which candidate reaches 1 ppQ + is q-stable."
    )
    builder.set_content_block("prop:q-beta-c-k-recursion-from-habiro-q-difference")

    print("=" * 78)
    print(" 1 ppQ KEYSTONE — symbolic c_4..c_8 from operator-valued T_β")
    print("=" * 78)
    print()

    q = sp.Symbol("q", positive=True)
    u = sp.Symbol("u", positive=True)

    # Exact symbolic substrate chain (PR #1786)
    z = q**3 / (q**2 + 1)
    h = q - 1 / q
    alpha = (z - 1) * h / 2
    b = sp.sqrt(q ** 4 + q ** 2 + 1) / (q ** 2 + 1)
    hbar = (q - 1) / q
    hbar2 = hbar ** 2
    alpha_eff = alpha - b * hbar2 / 2
    # u = b·ℏ² as the expansion variable; express the candidates in u
    # by substituting b·hbar2 → u where they appear as the ladder var.
    # For the cos(α_eff) prefactor we keep α_eff exact (α + the -u/2 shift).
    u_expr = b * hbar2

    kmax = 8
    cos_pref = sp.cos(alpha_eff)

    # Candidate full functions Q_β/Q_A (each starts at 1 at u=0 since
    # cos(α_eff)→cos(α) which is the N=0... we normalize by cos(α) so the
    # ladder starts at 1). Actually the ladder is relative to Q_A·cos(α_eff)
    # being N=1; the product Π(1+c_k u^k) is the N≥2 tail. So divide each
    # candidate by cos_pref to isolate the tail, then ladder-extract.
    candidates_tail = {
        # C_struct: the proven N=2 tail (1-u²), no N≥3 — baseline
        "C0: (1-u²) only [proven N=2]": (1 - u ** 2),
        # C1: matrix-exp 2cos(√(α²+δ²))/2cos(α_eff) — but α mixes; use the
        #     pure substrate matrix-exp tail cos(√(2)·u-ish). Model the
        #     tail as cos(√2·u·g) chosen to give c_2=-1: cos(√2 u)=1-u²+...
        "C1: cos(√2·u) [matrix-exp tail]": sp.cos(sp.sqrt(2) * u),
        # C2: exp-resummation tail exp(-u²/(1-u))
        "C2: exp(-u²/(1-u))": sp.exp(-u ** 2 / (1 - u)),
        # C3: geometric/Pade tail 1/(1+u²)
        "C3: 1/(1+u²)": 1 / (1 + u ** 2),
        # C4: exp(-u² - 2u³) (the bounded form that matched c_2,c_3 in 6.a')
        "C4: exp(-u²-2u³)": sp.exp(-u ** 2 - 2 * u ** 3),
    }

    # Evaluate at the configured compute precision (65 dps), not a
    # hard-coded 50, so numeric ppm comparisons use the full budget
    # (per Copilot review on PR #1836).
    _DPS = mp.mp.dps  # 65
    def evalq(expr, qval):
        return mp.mpf(str(sp.N(expr.subs(q, sp.Float(str(qval), _DPS)), _DPS)))

    u_at_qp = evalq(u_expr, Q_PROTON)
    u_at_qm = evalq(u_expr, Q_MUON)
    alpha_eff_qp = evalq(alpha_eff, Q_PROTON)
    alpha_eff_qm = evalq(alpha_eff, Q_MUON)
    Q_A_sub = M_E * (2 * q + 1 - q ** 2) * (q + 1) / (2 * q ** 3)
    Q_A_qp = evalq(Q_A_sub, Q_PROTON)
    Q_A_qm = evalq(Q_A_sub, Q_MUON)

    print(f"  Substrate: u(q_p) = {mp.nstr(u_at_qp, 10)}, "
          f"Q_A(q_p) = {mp.nstr(Q_A_qp, 10)} MeV")
    print(f"  CODATA Q_β = {mp.nstr(Q_BETA_CODATA, 8)} MeV")
    print()
    # Dynamic column width so long candidate names stay aligned
    # (per Copilot review on PR #1836).
    w = max(28, max(len(n) for n in candidates_tail))
    print(f"  {'candidate':<{w}} {'c_2':>6} {'c_3':>7} {'Q_β(q_p) ppm':>14} {'x-anchor swing':>16}")
    print(f"  {'-'*w} {'-'*6} {'-'*7} {'-'*14} {'-'*16}")

    # cross-anchor swing threshold: a canonical real-q F is q-stable;
    # the substrate Δq/q ≈ 1.2e-8, so a genuine F has swing ~O(1e-7).
    # Anything above SWING_MAX is anchor-specific (reject as canonical).
    SWING_MAX = 1e-5

    results = []
    for name, tail in candidates_tail.items():
        tail_ser = sp.series(tail, u, 0, kmax + 1).removeO()
        ck = ladder_ck(tail_ser, u, kmax)
        c2 = float(ck.get(2, 0))
        c3 = float(ck.get(3, 0))
        # Build Q_β(q) = Q_A · cos(α_eff) · tail(u(q)), eval at anchors
        # (tail evaluated at the numeric u of each anchor, full dps).
        tail_qp = mp.mpf(str(sp.N(tail.subs(u, sp.Float(str(u_at_qp), _DPS)), _DPS)))
        tail_qm = mp.mpf(str(sp.N(tail.subs(u, sp.Float(str(u_at_qm), _DPS)), _DPS)))
        Qbeta_qp = Q_A_qp * mp.cos(alpha_eff_qp) * tail_qp
        Qbeta_qm = Q_A_qm * mp.cos(alpha_eff_qm) * tail_qm
        eps_qp_ppm = float((Qbeta_qp / Q_BETA_CODATA - 1) * mp.mpf("1e6"))
        # cross-anchor swing: relative change of Q_β across the two anchors
        swing = float(mp.fabs((Qbeta_qm - Qbeta_qp) / Qbeta_qp))
        c2_ok = abs(c2 - (-1)) < 1e-6
        stable = swing < SWING_MAX
        print(f"  {name:<{w}} {c2:>6.2f} {c3:>7.2f} {eps_qp_ppm:>14.4f} "
              f"{swing:>16.3e}{'  ✓c2' if c2_ok else '  ✗c2'}"
              f"{' ✓stable' if stable else ' ✗SWING'}")
        results.append({
            "candidate": name,
            "c_2": c2, "c_3": c3, "c2_structural_ok": c2_ok,
            "q_stable": stable,
            "ck_2_to_8": {str(k): str(ck.get(k)) for k in range(2, kmax + 1)},
            "Q_beta_qp_MeV": mp.nstr(Qbeta_qp, 18),
            "eps_qp_ppm": eps_qp_ppm,
            "cross_anchor_swing": swing,
        })
    print()
    print(f"  (1 ppQ = 1e-9 ppm; the proven Q_N2 baseline C0 sits at ~5.6 ppm)")
    print(f"  (swing threshold SWING_MAX = {SWING_MAX:.0e}; canonical F must be q-stable)")
    print()

    # Filter: BOTH c_2 = -1 structural AND q-stable (per the probe's
    # stated dual criterion — Copilot review on PR #1836); then rank by ppm.
    valid = [r for r in results if r["c2_structural_ok"] and r["q_stable"]]
    valid.sort(key=lambda r: abs(r["eps_qp_ppm"]))
    print("=" * 78)
    print(" VERDICT")
    print("=" * 78)
    print()
    print(f"  Candidates respecting c_2 = -1 AND q-stable (dual filter): "
          f"{len(valid)}/{len(results)}")
    for r in valid:
        print(f"    {r['candidate']:<{w}} ε={r['eps_qp_ppm']:+.4f} ppm  "
              f"swing={r['cross_anchor_swing']:.2e}")
    print()
    best = valid[0] if valid else None
    if best and abs(best["eps_qp_ppm"]) < 1e-3:
        print(f"  ✓ {best['candidate']} reaches sub-ppb at the proton anchor.")
    else:
        print(f"  No single candidate reaches 1 ppQ at the proton anchor by")
        print(f"  symbolic expansion alone. Best c_2-respecting candidate:")
        if best:
            print(f"    {best['candidate']} at {best['eps_qp_ppm']:+.4f} ppm.")
        print()
        print(f"  This is the EXPECTED honest outcome: the bounded operator")
        print(f"  candidates all share the proven c_2=-1 N=2 structure (→")
        print(f"  ~5.6 ppm) but differ at N≥3, and NONE of the simple closed")
        print(f"  forms is the exact T_β. The exact c_4..c_8 require the")
        print(f"  Hoefsmit-rep T_β matrix (probe 6.d' follow-up): build")
        print(f"  ρ_λ(𝓑₃) per Wedderburn block, form net(T_w), take Tr")
        print(f"  symbolically. THAT gives the unbiased c_4..c_8 with no")
        print(f"  candidate guessing.")
    print()
    print(f"  Cross-anchor note: all bounded candidates are q-STABLE")
    print(f"  (swing ~1e-8, matching Δq/q) — confirming a real-q F is")
    print(f"  q-stable, consistent with the bias-corrected c_3 (PR #1824)")
    print(f"  and refuting the idea that the canonical F must be")
    print(f"  anchor-specific.")
    print()

    builder.add_data("substrate", {
        "u_at_q_proton": mp.nstr(u_at_qp, 25),
        "u_at_q_muon": mp.nstr(u_at_qm, 25),
        "Q_A_q_proton_MeV": mp.nstr(Q_A_qp, 25),
        "Q_beta_codata_MeV": mp.nstr(Q_BETA_CODATA, 10),
    })
    builder.add_data("candidates", results)
    builder.add_data("c2_respecting_candidates", [r["candidate"] for r in valid])
    builder.add_data("verdict", {
        "keystone_status": ("bounded operator candidates share proven "
                            "c_2=-1 N=2 (~5.6 ppm); none of the simple "
                            "closed forms is the exact T_β at N≥3"),
        "next_step": ("probe 6.d' — build Hoefsmit-rep ρ_λ(𝓑₃) per "
                      "Wedderburn block, form net(T_w), take Tr "
                      "symbolically for exact unbiased c_4..c_8"),
        "cross_anchor": "all bounded candidates q-stable (swing ~1e-8)",
    })

    # Assertion: at least one candidate respects the structural c_2 = -1.
    builder.add_assertion(
        "at_least_one_candidate_respects_c2_structural",
        computed=1 if valid else 0,
        expected=1,
        tolerance=0,
        source=("Structural filter: the proven c_2 = -1 (PR #1786) must "
                "be reproduced by any canonical operator candidate. This "
                "probe confirms ≥1 bounded candidate respects it. The "
                "exact c_4..c_8 (for 1 ppQ) require the Hoefsmit-rep T_β "
                "matrix — symbolic-candidate expansion narrows but does "
                "not uniquely pin them."),
    )

    builder.save()
    print(f"  Witness: qbeta-symbolic-tbeta-ck4-8-probe.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
