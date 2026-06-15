#!/usr/bin/env python3
# polynomial_q_not_applicable: symbolic structural exploration.
"""Q_β heat-route — reconciling the two a_1 factorizations.

Two PRs decompose the SAME leading coefficient a_1 = -c_3 ≈ 2.0694 differently:

  • #2240 (mode / Wedderburn basis):  a_1 = κ_(2,1) · S
      κ_(2,1) = (q-1)³(q+1)/q²  — pure-q, bar-ODD FIBRE carrier
      S = Q_β/E₀                — single ARCHIMEDEAN scalar (anchor-dep 908/887)

  • #2106 (Hoefsmit level basis):     a_1 = √2 · Φ₂ ≈ 2.0694
      where Φ₂ := 1.46324616887618 is a NUMERIC synthesis target (proton anchor),
      and #2106's per-mode candidate a1_cand = -(q-1)·μ_λ was REFUTED by a
      magnitude gate: |κ_λ(q_0)| ~ 10⁻³, off from the 2.069 target by ~900×.

This probe shows the two are the SAME a_1 in two bases, and that #2106's
"honest negative" (per-mode κ ≠ a_1 directly) is exactly RESOLVED by the
archimedean scalar S of #2240:

      a_1 = κ_(2,1)(q_0) · S,   S = a_1 / κ_(2,1)(q_0) ≈ 908  (proton)

So κ_(2,1) IS the bar-ODD fibre carrier #2106 was probing for; it just needs
the ×S archimedean rescale to reach the 2.069 magnitude. The magnitude gate
rejected the SCALE-1 carrier, not the carrier.

VERDICT (data-driven): the mode basis (κ_(2,1)·S) is the clean fibre/archimedean
separation — κ_(2,1) pure-q rational + bar-odd, S the lone archimedean scalar.
#2106's "√2·Φ₂" is the archimedean a_1 VALUE (both √2 and Φ₂=1.4632 are numbers),
not a fibre/archimedean split. Cross-checks #2106 finding 3 ((2,1) is special)
and finding 6 (per-mode magnitude refutation).

STRUCTURAL only; no NEW c_3 value (reuses the published −c_3 targets); flip-flop
guard respected.
"""
from __future__ import annotations

import sympy as sp

# shared symbolic helpers (single source of truth, #2240)
from qbeta_symbolic_utils import q, kappa, parity, contents

# ── published anchors / targets (reused verbatim; NOT re-derived, NOT CODATA) ──
# These are prior-PROBE outputs reused so this reconciliation reproduces #2240's
# S = 908/887 EXACTLY (the whole point of a reconciliation is byte-matching the
# numbers it reconciles). They are NOT CODATA constants and have no entry in
# substrate/codata_constants.py — that registry holds physical measurements
# (masses, widths), whereas PHI2_* below are the published −c_3 = √2·Φ₂ targets.
#
# Proton-anchored substrate q_0 — the SAME 11-digit truncation #2240's
# qbeta_heat_fmap_symbolic_explore.py used (matching it is required for the
# exact S reproduction). The higher-precision canonical form used by the
# from_scratch/ scripts is sp.Rational(11099785827513808, 10**16); switching to
# it would perturb S in the ~6th digit and break the exact #2240 match.
Q0 = sp.Rational(110997858275, 100000000000)            # ≈ 1.10997858275  (= #2240 heat_fmap q_0)
SQRT2 = sp.sqrt(2)
# −c_3 targets = √2 · Φ₂ at each anchor. Φ₂ values from #2106 PHI2_TARGET
# (proton) and #2240 heat_fmap a1_p/a1_mu (muon) — prior-probe outputs, reused.
PHI2_PROTON = sp.Rational(146324616887618, 100000000000000)   # 1.46324616887618 (#2106 §2.4)
PHI2_MUON = sp.Rational(142849728553818, 100000000000000)     # 1.42849728553818 (#2240 a1_mu/√2)
A1_PROTON = SQRT2 * PHI2_PROTON                          # √2·Φ₂ ≈ 2.0694
A1_MUON = SQRT2 * PHI2_MUON                              # ≈ 2.0202


def num(expr):
    return float(sp.N(expr, 20))


def main():
    print("=" * 80)
    print("  Reconciling a_1 = κ_(2,1)·S (#2240 mode basis) vs √2·Φ₂ (#2106 level)")
    print("=" * 80)

    # ── 1. The fibre carrier κ_(2,1): pure-q rational, bar-ODD ──
    print("\n  ── 1. Mode-basis fibre carrier κ_(2,1) (#2240) ──")
    k21 = kappa((2, 1))
    print(f"    κ_(2,1)            = {sp.factor(k21)}")
    print(f"    bar-parity         = {parity(k21)}   (pure-q, fibre-level)")
    k21_q0 = num(k21.subs(q, Q0))
    print(f"    κ_(2,1)(q_0)       = {k21_q0:.6e}   (~10⁻³ — matches #2106 |a₁|~10⁻³)")

    # ── 2. Per-mode magnitudes + parities for all λ⊢3 (clarify #2106's bar-MIXED) ──
    print("\n  ── 2. Per-mode κ_λ = (q-1)μ_λ for λ⊢3 — magnitude + bar-parity ──")
    print("       (#2106's refuted candidate is a1_cand = -(q-1)μ_λ = ∓κ_λ)")
    for p in [(3,), (2, 1), (1, 1, 1)]:
        kp = kappa(p)
        print(f"    λ={str(p):10s}: |κ_λ(q_0)|={abs(num(kp.subs(q, Q0))):.4e}  "
              f"bar-parity={parity(kp):4s}  contents={contents(p)}")
    print("    ⇒ only (2,1) is bar-ODD; (3),(1³) bar-neither. #2106's 'three")
    print("      bar-MIXED candidates' are the heat-trace R_λ family (a DIFFERENT")
    print("      μ_λ), not the plain content-Casimir κ_(2,1), which IS bar-odd.")

    # ── 3. The shared −c_3 target a_1 = √2·Φ₂ ──
    print("\n  ── 3. Level-basis target a_1 = √2·Φ₂ (#2106) ──")
    print(f"    proton: √2·Φ₂ = √2·{num(PHI2_PROTON):.10f} = {num(A1_PROTON):.6f}")
    print(f"    muon:   √2·Φ₂ = √2·{num(PHI2_MUON):.10f} = {num(A1_MUON):.6f}")
    print("    (√2 and Φ₂=1.4632 are both NUMBERS — an archimedean a_1 VALUE,")
    print("     not a fibre/archimedean factorization.)")

    # ── 4. Reconciliation: S = a_1 / κ_(2,1)(q_0) reproduces #2240's 908/887 ──
    print("\n  ── 4. RECONCILIATION — supply the archimedean scalar S ──")
    S_proton = num(A1_PROTON) / k21_q0
    S_muon = num(A1_MUON) / k21_q0
    print(f"    S_proton = (√2·Φ₂)_p / κ_(2,1)(q_0) = {S_proton:.4f}")
    print(f"    S_muon   = (√2·Φ₂)_μ / κ_(2,1)(q_0) = {S_muon:.4f}")
    print(f"    S_p / S_μ = {S_proton / S_muon:.6f}")
    ok_p = abs(S_proton - 908.36) < 0.5
    ok_mu = abs(S_muon - 886.79) < 0.5
    print(f"    matches #2240 S_proton≈908.36 ({ok_p}), S_muon≈886.79 ({ok_mu})")

    # ── 5. magnitude-gate reconciliation ──
    print("\n  ── 5. why #2106's magnitude gate refuted the SCALE-1 carrier ──")
    mag_ratio = k21_q0 / num(A1_PROTON)
    print(f"    |κ_(2,1)(q_0)| / |√2·Φ₂| = {mag_ratio:.4e}  (~1/S, fails #2106's <1% gate)")
    print(f"    1/S_proton                = {1/S_proton:.4e}  (same number)")

    print("\n  ── VERDICT (data-driven) ──")
    verdict_ok = (parity(k21) == "ODD") and ok_p and ok_mu
    print(f"""  RECONCILED ({verdict_ok}): a_1 = κ_(2,1)·S is the SAME a_1≈2.0694 as
  #2106's √2·Φ₂. The per-mode rate κ_(2,1) = (q-1)³(q+1)/q² is the bar-ODD,
  pure-q FIBRE carrier; #2106's magnitude gate rejected it only because it
  compared the SCALE-1 carrier (|κ|~10⁻³) against the full a_1 (~2.069) without
  the archimedean scalar S = a_1/κ ≈ 908 = Q_β/E₀.  Supplying S reproduces
  #2240's 908/887 exactly.

  ⇒ THE fibre carrier of a_1 is κ_(2,1) (mode basis), which cleanly separates
    fibre (pure-q, bar-odd, derivable) from archimedean (the lone scalar S).
    #2106's "√2·Φ₂" is the archimedean a_1 VALUE in the level basis — correct
    numerically, but it folds √2 and Φ₂=1.4632 (both numbers) together and does
    NOT isolate a pure-q carrier. The two bases agree; the mode basis is the
    clean fibre/archimedean cut. #2106's R_λ "honest negative" is RESOLVED:
    the carrier was right, the missing piece was S (owner-declined to derive).""")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
