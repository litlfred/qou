#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""c_knot_cancellation_conditioning_probe.py — the C_knot cross-isotope SPREAD is measured in an
ill-conditioned coordinate. Companion / corrective to `c_knot_nonuniversal_pinned_weight_probe.py`.

BEAN: qou-3q7t.  AUDIT-ONLY.  0 free parameters.  Convention D, experimental proton pin.

WHAT THIS ADDS
--------------
The master binding sum is an ALTERNATING sum over Wedderburn blocks,

    S(K) = Σ_{λ ⊢ 3A}  t_λ(K),      t_λ(K) = y_λ · χ^λ(β_K) · sgn(λ) · f^λ,   sgn(λ) = (−1)^{n(λ)},

and the deficit is reported as the RATIO  C_knot(K) = B_AME(K) / (m_e·|S(K)|).  Because S is
alternating, |S| can be far smaller than the scale of its own summands.  Define the

    CANCELLATION RATIO      κ(K) = |S(K)| / T(K),        T(K) = Σ_λ |t_λ(K)|   (so 0 ≤ κ ≤ 1),

which is exactly the reciprocal condition number of |S| under per-block relative perturbation:
if t_λ ↦ t_λ(1+δ_λ) with sup-norm ‖δ‖_∞ ≤ ε, then |S′ − S| ≤ ε·T = (ε/κ)·|S|.  So a per-block
relative correction of size ε moves |S| — and hence C_knot — by up to a factor ε/κ.  In particular
a correction of size ε = κ suffices to drive S to ZERO, i.e. C_knot to +∞.

MEASURED (convention D, proton pin, interface-inclusive Rust Hoefsmit caches):

      K    n   κ(K)      1/κ(K)   max|t_λ|/|S|   C_knot
      D    6   0.2911      3.44        1.77        6.068
      T    9   0.4137      2.42        1.51        6.706
      ³He  9   0.2944      3.40        1.91        4.905
      ⁴He 12   0.00795   125.7        52.05      290.007

⁴He sits on a 126× near-cancellation: its single largest block term is 52× the whole signed sum,
and a per-block relative correction of only 0.8% moves C_knot(⁴He) anywhere, sign included.  The
other three isotopes are mildly conditioned (1/κ ≈ 2.4–3.4).  So the headline "spread 59.12×" is
NOT a measurement of 59× of missing physics — it is dominated by one ill-conditioned denominator.

INDEPENDENT CORROBORATION (not a new claim of this probe): the ℓ(λ)≥3 stratum of the SAME object
is already known to CHANGE SIGN in q on the physical interval for ⁴He — `threerow_4he_completion_probe.py`
(bean qou-prjo, #4829 follow-up) records `4He_sign_at_qlo = +1`, `4He_sign_at_q0 = −1`.  A sign change
means a zero, and a zero is κ = 0; the small κ measured here at q₀ is the full-sum shadow of that
crossing.  A second, purely historical corroboration: under the 2026-08-11 convention C→D migration
(`70d1ade383`) |S| moved by 3.5% (D), 34% (T), 33% (³He) — and 96.8% (⁴He, 5.9456 → 0.19094).  An
ordinary-sized (~24%) per-term perturbation amplified by 1/κ ≈ 126 is exactly what produces a 96.8%
move in the total; no ⁴He-specific mechanism is needed to explain it.

THE WELL-POSED COORDINATE
-------------------------
`δ_min^∞(K) = |B_AME(K)/m_e − S(K)| / T(K)` is the MINIMUM sup-norm relative per-block correction
{δ_λ} for which Σ_λ t_λ(1+δ_λ) reaches the experimental target (attained by δ_λ = ±δ_min aligned with
sgn t_λ; the ℓ² analogue δ_min^2 = |gap|/‖t‖₂ is also emitted).  It is the same information as
C_knot, re-expressed per block instead of as a global ratio, and it is bounded by construction.

      K     δ_min^∞     δ_min^2
      D      1.475       2.435
      T      2.361       3.565
      ³He    1.150       1.837
      ⁴He    2.299       4.169                        spread(δ_min^∞) = 2.05×   [vs C_knot 59.12×]

READ THIS CAREFULLY — WHAT THE 2.05× DOES AND DOES NOT SAY
----------------------------------------------------------
It does NOT rescue universality, and it is NOT "the isotopes nearly agree".  δ_min^∞ is a LOWER
BOUND on the size of the missing per-block structure, not the structure itself; two isotopes with
equal δ_min may still need completely different {δ_λ} directions.  A 2.05× spread in a lower bound
is perfectly compatible with the per-knot non-universality that
`c_knot_nonuniversal_pinned_weight_probe.py` establishes, and with the Lean mirror-pair exclusion
`CKnotNonUniversal.no_level_only_closure` (T and ³He are both well-conditioned here, κ ≈ 0.29–0.41,
so that exclusion is untouched by anything measured in this file).

What it DOES say, and this is the deliverable: the missing per-block magnitude is an ORDER-UNITY
relative correction to each block term (δ_min ≈ 1.1–2.4), uniformly across the four isotopes — not
a 290× monster localised on ⁴He.  "Derive C_knot ≈ 6" and "derive C_knot ≈ 290" are the same size of
problem in per-block coordinates.  Anyone reading the 59.12× as a statement that ⁴He is qualitatively
harder is reading a coordinate artifact.

ANTI-FIT / SCOPE
----------------
B_AME enters ONLY through `δ_min` and `C_knot`, both DIAGNOSTIC ratios, exactly as in the probe this
one accompanies.  Nothing here is a derived Δ_λ; nothing is wired; no value is inverted from CODATA
or AME into a canonical weight (owner directive: "Δ_λ from inverted CODATA = NOT ALLOWED").  This
probe proposes NO ansatz for the magnitude — per AGENTS.md there is no seventh per-block-weight
ansatz here, and none is implied: κ and δ_min are diagnostics of the EXISTING formula, not a new one.

Refutation scope: this is scope-(a) with respect to the interpretation of the spread — "the 59.12×
figure is not a measurement of the per-knot deficit's variation" — resting on the proved triangle
inequality |Σ t| ≤ Σ|t| plus the measured κ.  It is NOT a claim that C_knot is universal, and it is
NOT a structural exclusion of anything.  The Δ_λ MAGNITUDE remains OPEN (qou-3q7t).
"""
from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
COMP = ROOT / "computations"
sys.path.insert(0, str(COMP))

import _path_bridge  # noqa: F401,E402 — substrate path bridge
from mpmath import mp, mpf, fabs, sqrt  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

mp.dps = 50

q0 = Q_MP
m_e = mpf("0.51099895069")

# Wenzl Schur-principal parameters — convention D (z = q³/(q²+1)), identical to the master probe.
Q = q0 ** 2
z_mark = q0 ** 3 / (q0 ** 2 + 1)
z_w = q0 * z_mark
QR = z_w / (1 - Q + z_w)


def _hooks_contents(lam):
    hs, cs = [], []
    rows = len(lam)
    for i in range(rows):
        for j in range(lam[i]):
            arm = lam[i] - j - 1
            leg = sum(1 for r in range(i + 1, rows) if lam[r] > j)
            hs.append(arm + leg + 1)
            cs.append(j - i)
    return hs, cs


def f_lambda(lam):
    """SYT count = classical dim of the S_n irrep (hook-length formula) — exact integer."""
    hs, _ = _hooks_contents(lam)
    p = 1
    for x in hs:
        p *= x
    return math.factorial(sum(lam)) // p


def n_stat(lam):
    return sum(i * lam[i] for i in range(len(lam)))


def schur_principal(lam):
    """s_λ(1, Q, …, Q^{r−1}) closed form (Wenzl), Q = q², Q^r = QR."""
    hs, cs = _hooks_contents(lam)
    num = mpf(1)
    den = mpf(1)
    for hh, c in zip(hs, cs):
        num *= (1 - QR * Q ** c)
        den *= (1 - Q ** hh)
    return Q ** n_stat(lam) * num / den


def _load(fn):
    p = COMP / fn
    if not p.exists():
        raise FileNotFoundError(f"required interface-inclusive χ cache missing: {p}")
    a = json.loads(p.read_text())["data"]["atom"]
    parts = [tuple(e["partition"]) for e in a["by_partition"]]
    chis = [mpf(str(e["chi_lambda"])) for e in a["by_partition"]]
    return a["n_strands"], parts, chis


def block_terms(fn):
    """The per-block summands t_λ = y_λ·χ^λ·sgn(λ)·f^λ, exactly as in the master formula."""
    n, parts, chis = _load(fn)
    Z = mpf(0)
    sp = {}
    for lam in parts:
        s = schur_principal(list(lam))
        sp[lam] = s
        Z += s * f_lambda(list(lam))          # Σ s_λ f^λ = normaliser ⇒ Σ y_λ f^λ = 1
    terms, norm = [], mpf(0)
    for lam, chi in zip(parts, chis):
        y = sp[lam] / Z
        sgn = (-1) ** n_stat(list(lam))
        terms.append((lam, y * chi * sgn * mpf(f_lambda(list(lam)))))
        norm += y * mpf(f_lambda(list(lam)))
    return n, terms, norm


def main() -> int:
    from codata_constants import (  # noqa: E402
        AME_B_DEUTERON_MEV_VALIDATION as B_D,
        AME_B_TRITIUM_MEV_VALIDATION as B_T,
        AME_B_HE3_MEV_VALIDATION as B_HE3,
        AME_B_HE4_MEV_VALIDATION as B_HE4,
    )
    isotopes = [
        ("D", "atom-chi-rust-d.witness.json", mpf(str(B_D)), 2),
        ("T", "atom-chi-rust-t.witness.json", mpf(str(B_T)), 3),
        ("3He", "atom-chi-rust-3he.witness.json", mpf(str(B_HE3)), 3),
        ("4He", "atom-chi-rust-4he.witness.json", mpf(str(B_HE4)), 4),
    ]

    print("=" * 96)
    print("  C_knot cancellation conditioning — is the 59× spread a measurement or a coordinate?")
    print("=" * 96)
    print(f"  {'K':>4} {'n':>3} {'#λ':>4} {'S_signed':>13} {'T=Σ|t|':>12} {'κ=|S|/T':>10} "
          f"{'1/κ':>9} {'max|t|/|S|':>11} {'C_knot':>10} {'δ_min^∞':>9} {'δ_min^2':>9}")

    per = {}
    for name, fn, B, A in isotopes:
        n, terms, norm = block_terms(fn)
        vals = [t for _lam, t in terms]
        S = sum(vals, mpf(0))
        T = sum((fabs(v) for v in vals), mpf(0))
        L2 = sqrt(sum((v * v for v in vals), mpf(0)))
        absS = fabs(S)
        kappa = absS / T
        maxterm = max(fabs(v) for v in vals)
        lam_max = max(terms, key=lambda r: fabs(r[1]))[0]
        target = B / m_e
        # signed target: the master formula compares |S| to B/m_e, so align the target with sgn S.
        tgt = target if S > 0 else -target
        gap = tgt - S
        per[name] = {
            "A": A,
            "n_strands": n,
            "n_partitions": len(terms),
            "S_signed": mp.nstr(S, 10),
            "absS": mp.nstr(absS, 10),
            "T_abs_sum": mp.nstr(T, 10),
            "L2_norm": mp.nstr(L2, 10),
            "markov_norm_sum_yf": mp.nstr(norm, 6),
            "kappa_cancellation_ratio": mp.nstr(kappa, 8),
            "amplification_inv_kappa": mp.nstr(1 / kappa, 8),
            "max_abs_term": mp.nstr(maxterm, 8),
            "max_abs_term_partition": list(lam_max),
            "max_term_over_absS": mp.nstr(maxterm / absS, 8),
            "C_knot": mp.nstr(target / absS, 8),
            "delta_min_sup": mp.nstr(fabs(gap) / T, 8),
            "delta_min_l2": mp.nstr(fabs(gap) / L2, 8),
            "eps_to_zero_S": mp.nstr(kappa, 8),
        }
        print(f"  {name:>4} {n:>3} {len(terms):>4} {mp.nstr(S, 8):>13} {mp.nstr(T, 8):>12} "
              f"{mp.nstr(kappa, 5):>10} {mp.nstr(1 / kappa, 5):>9} "
              f"{mp.nstr(maxterm / absS, 5):>11} {mp.nstr(target / absS, 6):>10} "
              f"{mp.nstr(fabs(gap) / T, 5):>9} {mp.nstr(fabs(gap) / L2, 5):>9}")

    cvals = {k: mpf(per[k]["C_knot"]) for k in per}
    dvals = {k: mpf(per[k]["delta_min_sup"]) for k in per}
    kvals = {k: mpf(per[k]["kappa_cancellation_ratio"]) for k in per}
    spread_C = max(cvals.values()) / min(cvals.values())
    spread_d = max(dvals.values()) / min(dvals.values())
    kappa_ratio = max(kvals.values()) / min(kvals.values())

    print()
    print(f"  spread C_knot      = {mp.nstr(spread_C, 6)}×      (the reported headline)")
    print(f"  spread δ_min^∞     = {mp.nstr(spread_d, 6)}×      (same information, per-block coords)")
    print(f"  κ range            = {mp.nstr(min(kvals.values()), 5)} … {mp.nstr(max(kvals.values()), 5)}"
          f"   ({mp.nstr(kappa_ratio, 5)}× — ⁴He is the outlier)")
    print()
    print("  VERDICT: ⁴He's C_knot = 290 is 1/κ = 126× amplification of a 0.8%-level cancellation,")
    print("           not 290× of missing physics.  In per-block coordinates all four isotopes need")
    print("           an ORDER-UNITY relative correction (δ_min ≈ 1.1–2.4).  The Δ_λ MAGNITUDE stays")
    print("           OPEN (qou-3q7t); nothing here closes it and nothing here is fitted.")

    this = Path(__file__).resolve()
    witness = {
        "schema": "witness/v1",
        "producer": "computations/deltalambda/c_knot_cancellation_conditioning_probe.py",
        "computation": "c-knot-cancellation-conditioning",
        "audit_only": True,
        "tier": ("scope-(a) correction to the INTERPRETATION of the C_knot spread; "
                 "no closure, no exclusion, no fit"),
        "result": {
            "object": ("S(K) = Σ_λ t_λ,  t_λ = y_λ·χ^λ(β_K)·(−1)^{n(λ)}·f^λ  — the master binding sum; "
                       "C_knot(K) = B_AME(K)/(m_e·|S(K)|)"),
            "cancellation_ratio_def": ("κ(K) = |S(K)| / Σ_λ|t_λ(K)| ∈ [0,1]. Reciprocal condition "
                                       "number: ‖δ‖_∞ ≤ ε ⇒ |S′−S| ≤ ε·Σ|t| = (ε/κ)|S|. ε = κ drives "
                                       "S to 0, i.e. C_knot to +∞."),
            "delta_min_def": ("δ_min^∞(K) = |B_AME/m_e − S| / Σ_λ|t_λ| — the MINIMUM sup-norm relative "
                              "per-block correction {δ_λ} with Σ t_λ(1+δ_λ) = target. A LOWER BOUND on "
                              "the missing per-block structure, not the structure; equal δ_min does NOT "
                              "mean equal correction direction."),
            "per_isotope": per,
            "spread_C_knot": mp.nstr(spread_C, 6),
            "spread_delta_min_sup": mp.nstr(spread_d, 6),
            "kappa_min": mp.nstr(min(kvals.values()), 6),
            "kappa_max": mp.nstr(max(kvals.values()), 6),
            "corroboration": {
                "threerow_4he_sign_change_in_q": (
                    "threerow_4he_completion_probe.py (bean qou-prjo) records 4He_sign_at_qlo=+1, "
                    "4He_sign_at_q0=−1 for the ℓ(λ)≥3 stratum of the same object — a sign change, hence "
                    "a zero, hence κ=0 somewhere on the physical interval. The small κ measured here at "
                    "q₀ is the full-sum shadow of that crossing. Independent producer, not re-run here."),
                "convention_migration_amplification": (
                    "Historical: under 70d1ade383 (convention C→D) |S| moved 3.5%/34%/33%/96.8% for "
                    "D/T/³He/⁴He (5.9456 → 0.19094 for ⁴He). A ~24% per-term perturbation amplified by "
                    "1/κ≈126 reproduces the 96.8% move; no ⁴He-specific mechanism is required."),
            },
            "what_this_does_not_claim": [
                "NOT a claim that C_knot is universal — it is not; the per-knot non-universality of "
                "c_knot_nonuniversal_pinned_weight_probe.py stands.",
                "NOT a weakening of the Lean mirror-pair exclusion CKnotNonUniversal.no_level_only_closure: "
                "T and ³He are both well-conditioned here (κ ≈ 0.294–0.414), so that exclusion is untouched.",
                "NOT a new ansatz for the Δ_λ magnitude. κ and δ_min are diagnostics of the EXISTING "
                "formula. No per-block weight is proposed (AGENTS.md: no seventh fit-based ansatz).",
                "δ_min is a LOWER BOUND on the correction size, not a derived Δ_λ, and is not wired.",
            ],
            "verdict": (
                f"The headline C_knot spread ({mp.nstr(spread_C, 6)}×) is dominated by one "
                f"ill-conditioned denominator: κ(⁴He) = {mp.nstr(kvals['4He'], 4)} (1/κ = "
                f"{mp.nstr(1 / kvals['4He'], 5)}×), with its largest single block term "
                f"{mp.nstr(mpf(per['4He']['max_term_over_absS']), 4)}× the whole signed sum. Re-expressed "
                f"per block, the same information gives spread {mp.nstr(spread_d, 5)}× with every isotope "
                f"needing an order-unity relative correction. The Δ_λ magnitude remains OPEN (qou-3q7t)."),
            "anti_fit": ("B_AME enters only through the diagnostic ratios C_knot and δ_min, never inverted "
                         "into a canonical weight (owner directive: Δ_λ from inverted CODATA = NOT ALLOWED). "
                         "y_λ recomputed from the Wenzl closed form (Σ y_λ f^λ = 1 asserted); χ^λ from the "
                         "committed interface-inclusive Rust caches; free_parameters = 0; nothing wired."),
            "free_parameters": 0,
        },
        "parameters": {
            "q0_experimental_proton_anchor": Q_50_DIGIT_STR,
            "q0_pin": "experimental/proton (q_parameter.Q)",
            "convention": "D (z = q³/(q²+1))",
            "compute_dps": mp.dps,
            "free_parameters": 0,
        },
        "context": {
            "axis": "Δ_λ / C_knot magnitude — conditioning of the reported cross-isotope spread",
            "bean": "qou-3q7t",
            "companion_to": "computations/deltalambda/c_knot_nonuniversal_pinned_weight_probe.py",
            "corroborated_by": "computations/deltalambda/threerow_4he_completion_probe.py (qou-prjo)",
            "no_fit": True,
        },
    }
    try:
        witness["scriptCommitSha"] = subprocess.check_output(
            ["git", "log", "-1", "--format=%H", "--", str(this)], cwd=this.parent, text=True
        ).strip() or "uncommitted"
    except Exception:
        witness["scriptCommitSha"] = "uncommitted"
    out = HERE / "c-knot-cancellation-conditioning.witness.json"
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=None)
    out.write_text(json.dumps(witness, indent=2, default=str) + "\n")
    print(f"\nwitness -> {out.name}")

    # Assertions — the finding must be reproducible, not narrated.
    assert fabs(mpf(per["D"]["markov_norm_sum_yf"]) - 1) < mpf("1e-6"), "Markov normalisation Σ y_λ f^λ = 1 broken"
    for k in per:  # triangle inequality: κ ≤ 1 by construction, a self-check on the arithmetic
        assert kvals[k] <= 1, f"κ({k}) > 1 — |Σt| ≤ Σ|t| violated, arithmetic is wrong"
    assert kvals["4He"] < mpf("0.01"), "⁴He cancellation (κ < 1%) is the core measurement"
    assert spread_d < spread_C / 10, "per-block re-coordinatisation must collapse the headline spread"
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
