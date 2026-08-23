#!/usr/bin/env python3
"""mu3_target_robustness_audit_probe.py — RED-TEAM audit of the A=3 magnitude
target μ₃ ≈ +0.4708 (the numerator of r* = μ₃/c₃ ≈ 1.585 that ROUTE 1-4 chase).

QUESTION (meta / sanity-check, ROUTE 5): is μ₃ a robust STRUCTURAL constant worth
deriving, or a residual-DECOMPOSITION ARTIFACT whose value drifts under reasonable
re-choices of (a) which A=3 isotope + isospin correction, (b) the subtracted
"model" ladder ρ_grad convention, (c) the moment-extraction method?

This probe DERIVES nothing new and wires nothing.  It only re-runs the canonical
μ₃ recipe under a matrix of defensible convention choices and reports the SPREAD.
A structural constant is stable under such re-choices; an artifact drifts.

Canonical recipe (from deltalambda_kappa_interface_residual_simplex_probe.py #4320):
    ρ_grad(A) = [A]_q! / [2]_q!           (subtracted graded "model" baseline)
    ρ_strong(A) = B_strong(A) / B(²H)     (isospin/Coulomb-corrected AME target)
    M(A) = ρ_strong(A) − ρ_grad(A)
    simplex solve over C(A,k):  μ₂ = M(2),  μ₃ = M(3) − 3μ₂,  μ₄ = M(4) − 6μ₂ − 4μ₃
Because the 3×3 counts matrix [[1,0,0],[3,1,0],[6,4,1]] is UNIT-triangular and
M(2)=0 by the deuteron self-reference, μ₃ = M(3) EXACTLY — μ₃ is a single-isotope
residual re-labelled, NOT a statistical moment of a distribution.  There is no
"raw-central-moment vs Richardson vs cumulant" freedom: 3 points, 3 unknowns,
exact invertible solve.  Axis (c) therefore collapses; the only live knobs are
(a) ρ_strong(3) and (b) ρ_grad(3).
"""
import json
import hashlib
import subprocess
from pathlib import Path
import mpmath as mp
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

# ── canonical substrate q₀ (muon-canonical computations layer) ──────────────
Q0_MUON = mp.mpf("1.10997859555733471989976322048322502665620840878015368660798114614493")
# proton-pinned q₀ (package layer) — for the pin-sensitivity check
Q0_PROTON = mp.mpf("1.10997859")  # ~identical to 8 sig figs; the pin swing is ~11.5 ppb

# ── AME2020 connected binding energies (MeV), from the #3943 committed witness ──
B_AME = {
    "2H":  mp.mpf("2.224566"),
    "3H":  mp.mpf("8.481821"),
    "3He": mp.mpf("7.718058"),
    "4He": mp.mpf("28.295673"),
}
# Coulomb energy of the A=3 mirror (³He), two standard models (from #3990):
E_C_3HE_SPHERE = mp.mpf("0.8487393706040641")   # 3/5 uniform charged sphere
E_C_3HE_PAIR   = mp.mpf("0.7072828088367201")   # 1/2 discrete pp pair

B_D = B_AME["2H"]


def qint_unbalanced(n, q):
    """[n]_q = 1 + q + ... + q^{n-1}  (the recipe's convention)."""
    return sum(q ** k for k in range(n))


def qint_balanced(n, q):
    """[n]_q = (q^n − q^{-n})/(q − q^{-1})  (the Hecke/skein convention, AGENTS §7a)."""
    return (q ** n - q ** (-n)) / (q - q ** (-1))


def rho_grad3(q, conv):
    """ρ_grad(3) = [3]_q!/[2]_q! = [3]_q under the chosen q-integer convention."""
    return conv(3, q)


# ── the canonical value, reproduced exactly ─────────────────────────────────
rho_strong3_canonical = B_AME["3H"] / B_D                    # triton, "Coulomb-free mirror"
rho_grad3_canonical = rho_grad3(Q0_MUON, qint_unbalanced)    # unbalanced [3]_q
mu3_canonical = rho_strong3_canonical - rho_grad3_canonical
C3_borromean = mp.mpf("0.297")                               # #4364 derived c₃ (H₉ lift)
r_star_canonical = mu3_canonical / C3_borromean

# ============================================================================
# AXIS (a): which A=3 "strong binding" enters ρ_strong(3)?
# ============================================================================
Bstrong3_choices = {
    "triton_3H_direct (canonical)":      B_AME["3H"],                       # Z=1, no pp Coulomb
    "3He + E_C(sphere)":                 B_AME["3He"] + E_C_3HE_SPHERE,     # isospin-restore ³He
    "3He + E_C(pair)":                   B_AME["3He"] + E_C_3HE_PAIR,
    "mean(3H, 3He+E_C_sphere)":          (B_AME["3H"] + B_AME["3He"] + E_C_3HE_SPHERE) / 2,
    "3He raw (NO Coulomb corr.)":        B_AME["3He"],                      # physically wrong but "reasonable-looking"
    "mean(3H, 3He raw)":                 (B_AME["3H"] + B_AME["3He"]) / 2,
}
axis_a = {}
for name, Bs in Bstrong3_choices.items():
    rs3 = Bs / B_D
    mu3 = rs3 - rho_grad3_canonical               # hold ladder = canonical (unbalanced [3]_q at q₀)
    axis_a[name] = {
        "B_strong3_MeV": mp.nstr(Bs, 8),
        "rho_strong3": mp.nstr(rs3, 8),
        "mu3": mp.nstr(mu3, 6),
        "r_star = mu3/c3": mp.nstr(mu3 / C3_borromean, 5),
        "vs_canonical_mu3": mp.nstr(mu3 / mu3_canonical, 5),
    }

# isospin-corrected-strong sub-family only (the physically defensible set)
strong_family = ["triton_3H_direct (canonical)", "3He + E_C(sphere)", "3He + E_C(pair)",
                 "mean(3H, 3He+E_C_sphere)"]
mu3_family = [Bstrong3_choices[n] / B_D - rho_grad3_canonical for n in strong_family]
axis_a_family_spread = max(mu3_family) / min(mu3_family)

# ============================================================================
# AXIS (b): the subtracted "model" ladder ρ_grad(3) convention.
# For A=3, ρ_grad(3) = [3]_q!/[2]_q! = [3]_q. Two sub-questions:
#   (b1) the q-integer convention (balanced vs unbalanced) — is it FREE or PINNED?
#   (b2) the q₀ pin (muon vs proton).
# FAIRNESS PIN (checked against damping_nonmonotone_wall_probe / #4300): ρ_grad =
# [A]_q! is the "q-scaled COINVARIANT GRADED DIMENSION". By Chevalley the graded
# dimension of the S_A coinvariant algebra is ∏_{k=1}^A [k]_q with the GAUSSIAN
# (unbalanced) [k]_q = 1+q+...+q^{k-1}.  So the unbalanced convention is *forced*
# by ρ_grad's categorical meaning — the "balanced" row below is recorded for
# transparency but is NOT a legitimate re-choice (it would not be a graded
# dimension). Its swing is therefore an illustration of sensitivity, not evidence
# of a free knob.
# ============================================================================
axis_b = {}
for name, (conv, q, legit) in {
    "unbalanced [3]_q @ q0_muon (CANONICAL, pinned)": (qint_unbalanced, Q0_MUON, "pinned-correct"),
    "balanced [3]_q @ q0_muon (NOT a graded dim)":    (qint_balanced,   Q0_MUON, "illegitimate"),
    "unbalanced [3]_q @ q0_proton":                   (qint_unbalanced, Q0_PROTON, "pinned-correct"),
    "classical A=3 (q->1: [3]=3)":                    (lambda n, q: mp.mpf(n), Q0_MUON, "limit-only"),
}.items():
    rg3 = rho_grad3(q, conv)
    mu3 = rho_strong3_canonical - rg3             # hold ρ_strong = canonical triton
    axis_b[name] = {
        "rho_grad3": mp.nstr(rg3, 8),
        "mu3": mp.nstr(mu3, 6),
        "r_star = mu3/c3": mp.nstr(mu3 / C3_borromean, 5),
        "vs_canonical_mu3": mp.nstr(mu3 / mu3_canonical, 5),
        "legitimacy": legit,
    }

# the q-integer-convention swing alone (balanced vs unbalanced) — RECORDED but the
# balanced convention is categorically illegitimate for a graded dimension, so this
# is NOT a live degree of freedom:
mu3_unbal = rho_strong3_canonical - qint_unbalanced(3, Q0_MUON)
mu3_bal   = rho_strong3_canonical - qint_balanced(3, Q0_MUON)
qconv_swing = mu3_bal / mu3_unbal
# q₀-pin swing (muon vs proton), the one genuinely-live axis-(b) knob:
mu3_muon   = rho_strong3_canonical - qint_unbalanced(3, Q0_MUON)
mu3_proton = rho_strong3_canonical - qint_unbalanced(3, Q0_PROTON)
qpin_swing = mu3_proton / mu3_muon

# ============================================================================
# AXIS (c): the "moment-extraction method". SHOW it is not a moment at all.
# 3 data points → 3 coefficients via a UNIT-triangular matrix ⇒ exact solve,
# μ₃ = M(3) identically. No raw/Richardson/cumulant freedom exists.
# ============================================================================
M2 = mp.mpf(0)                                             # deuteron self-reference forces it
M3 = mu3_canonical                                         # = ρ_strong(3) − ρ_grad(3)
mu3_from_solve = M3 - 3 * M2
axis_c = {
    "is_statistical_moment": False,
    "reason": "3 isotopes (A=2,3,4) pin 3 coefficients via unit-triangular counts "
              "matrix det=1 ⇒ EXACT invertible relabel, not a fit/moment. No "
              "residual, no over-determination, no method freedom.",
    "mu3_equals_M3_identically": bool(abs(mu3_from_solve - M3) < mp.mpf("1e-40")),
    "mu3 = M(3) = rho_strong(3) - rho_grad(3)": mp.nstr(M3, 8),
    "cancellation_structure": {
        "rho_strong3": mp.nstr(rho_strong3_canonical, 8),
        "rho_grad3":   mp.nstr(rho_grad3_canonical, 8),
        "mu3":         mp.nstr(mu3_canonical, 6),
        "mu3_as_fraction_of_operands": mp.nstr(mu3_canonical / rho_strong3_canonical, 4),
        "note": "μ₃ is a ~12% residual of two O(3.4) numbers ⇒ a catastrophic-"
                "cancellation object: small absolute perturbations to EITHER operand "
                "move μ₃ by a large RELATIVE amount (condition number ≈ "
                + mp.nstr(rho_strong3_canonical / mu3_canonical, 4) + ").",
    },
}

# condition number: d(mu3)/mu3 per d(operand)/operand
condition_number = rho_strong3_canonical / mu3_canonical

results = {
    "canonical": {
        "rho_strong3_triton": mp.nstr(rho_strong3_canonical, 8),
        "rho_grad3_unbalanced": mp.nstr(rho_grad3_canonical, 8),
        "mu3": mp.nstr(mu3_canonical, 8),
        "c3_borromean_4364": mp.nstr(C3_borromean, 6),
        "r_star": mp.nstr(r_star_canonical, 6),
        "condition_number_mu3": mp.nstr(condition_number, 5),
    },
    "axis_a_isotope_isospin": axis_a,
    "axis_a_strong_family_spread_max_over_min": mp.nstr(axis_a_family_spread, 5),
    "axis_b_ladder_convention": axis_b,
    "axis_b_qinteger_balanced_vs_unbalanced_swing_ILLEGITIMATE": mp.nstr(qconv_swing, 5),
    "axis_b_q0_pin_muon_vs_proton_swing_LIVE": mp.nstr(qpin_swing, 8),
    "axis_c_moment_method": axis_c,
    "verdict": {
        "mu3_is_a_decomposition_artifact": False,
        "mu3_is_well_posed_to_3_sigfigs": False,
        "mu3_is_well_posed_at_~10pct": True,
        "classification": "scope-(a) WELL-POSED-AT-~10%%, NOT-3-SIG-FIG. After the "
            "fairness checks, μ₃ is NOT a free-floating decomposition artifact: (i) its "
            "SIGN (+) is corpus-PROVED robust — it holds for BOTH raw and isospin-"
            "corrected AME, and the required correction is non-monotone so it cannot be "
            "a damping (#4300 / DampingNonMonotoneWall); (ii) the subtracted ladder's "
            "q-integer convention is PINNED (coinvariant graded dimension ⇒ Gaussian/"
            "unbalanced, not free); (iii) the q₀ pin (muon vs proton) is not a lever "
            "(identical to 8 sf); (iv) within the isospin-corrected-strong isotope "
            "family μ₃ varies only ~±8% (0.445–0.509 ⇒ r* ∈ [1.50,1.71]). What is NOT "
            "well-posed is the 3-sig-fig VALUE: μ₃ is a condition-number-≈8 residual "
            "(12% of two O(3.4) operands), so the ±8% isospin-correction band is "
            "irreducible and 0.4708 over-states precision — the honest target is "
            "r* ≈ 1.6 ± ~0.1.",
        "what_IS_robust": "μ₂ = 0 (FORCED, deuteron self-reference, Lean-proved); "
            "sign(μ₃)=+ and sign(μ₄)=− (corpus-proved, raw+corrected); the ≥3-body "
            "purity; the unbalanced graded-dimension convention; order-of-magnitude "
            "μ₃ ≈ 0.47 ± 0.04.",
        "what_is_soft": "the 3-sig-fig value 0.4708 and hence r*=1.585 to 4 sf — a "
            "condition-number-8 residual with an irreducible ~±8% isospin-correction "
            "band; NOT a high-precision (sub-%) target and never will be.",
        "advice_to_siblings": "The cross-channel hunt IS justified — the target (sign + "
            "O(1.6) magnitude) is a real structural fact, not an artifact. BUT: score a "
            "derived c₃ by SIGN and by landing r* within the [1.50,1.71] band (~±8%), "
            "NOT by matching 1.585 to 3 sig figs. A mechanism tuned to reproduce 1.585 "
            "exactly would be over-fitting the isospin-correction convention inside a "
            "12%-residual — the residual simply cannot carry 3 sig figs of meaning.",
    },
}

# ── console report ──────────────────────────────────────────────────────────
print("=== μ₃ TARGET ROBUSTNESS AUDIT (ROUTE 5, red-team) ===")
print(f"canonical: μ₃ = ρ_strong(3) − ρ_grad(3) = {mp.nstr(rho_strong3_canonical,7)} "
      f"− {mp.nstr(rho_grad3_canonical,7)} = {mp.nstr(mu3_canonical,6)}")
print(f"           r* = μ₃/c₃ = {mp.nstr(mu3_canonical,6)}/{mp.nstr(C3_borromean,4)} "
      f"= {mp.nstr(r_star_canonical,5)}")
print(f"           condition number ≈ {mp.nstr(condition_number,4)} "
      f"(μ₃ is a {mp.nstr(100*mu3_canonical/rho_strong3_canonical,3)}% residual of O(3.4) operands)")
print()
print("── AXIS (a) isotope / isospin choice for ρ_strong(3) ──")
for name, d in axis_a.items():
    print(f"  {name:34s}  μ₃={d['mu3']:>9s}  r*={d['r_star = mu3/c3']:>7s}  "
          f"({d['vs_canonical_mu3']}× canonical)")
print(f"  → isospin-corrected-strong FAMILY spread (max/min) = {mp.nstr(axis_a_family_spread,4)}")
print()
print("── AXIS (b) subtracted ladder ρ_grad(3) convention ──")
for name, d in axis_b.items():
    print(f"  {name:46s}  μ₃={d['mu3']:>9s}  r*={d['r_star = mu3/c3']:>7s}  "
          f"[{d['legitimacy']}]")
print(f"  → balanced-vs-unbalanced swing = {mp.nstr(qconv_swing,4)}× but balanced is "
      f"ILLEGITIMATE (ρ_grad = coinvariant graded dim ⇒ Gaussian/unbalanced forced)")
print(f"  → q0-pin (muon vs proton) swing = {mp.nstr(qpin_swing,8)}× (NOT a lever)")
print()
print("── AXIS (c) 'moment method' ──")
print(f"  statistical moment? {axis_c['is_statistical_moment']}  "
      f"(μ₃ = M(3) identically, exact 3×3 solve — no method freedom)")
print()
print("VERDICT:", results["verdict"]["classification"])

# ── witness ──────────────────────────────────────────────────────────────────
out = Path(__file__).resolve().parent / "mu3-target-robustness-audit.witness.json"
this = Path(__file__).resolve()
witness = {
    "schema": "witness/v1",
    "producer": str(this.relative_to(this.parents[2])),
    "description": "RED-TEAM robustness audit of the A=3 magnitude target μ₃≈+0.4708 "
        "(numerator of r*=μ₃/c₃≈1.585). μ₃ = ρ_strong(3) − ρ_grad(3) = B(³H)/B(²H) − "
        "[3]_q is a ~12% residual of two O(3.4) numbers (condition number ≈8), and μ₃ "
        "= M(3) EXACTLY (unit-triangular 3×3 solve, μ₂=0 forced) — NOT a statistical "
        "moment, so there is no raw/Richardson/cumulant method freedom. FINDINGS after "
        "fairness checks: (a) within the isospin-corrected-strong isotope family μ₃ is "
        "stable ±~8% (0.445–0.509 ⇒ r*∈[1.50,1.71]); it only collapses to 0.127 under "
        "the physically-inconsistent raw-³He (no-Coulomb) choice, which is not "
        "defensible. (b) the q-integer convention is PINNED: ρ_grad=[A]_q! is the "
        "coinvariant graded dimension ⇒ Gaussian/unbalanced is forced by Chevalley, so "
        "the 1.63× balanced swing is NOT a legitimate re-choice; the q₀ pin (muon vs "
        "proton) is not a lever (identical to 8sf). (c) sign(μ₃)=+/sign(μ₄)=− are "
        "corpus-PROVED robust (#4300 / DampingNonMonotoneWall — holds raw+corrected, "
        "non-monotone ⇒ not a damping). VERDICT scope-(a): μ₃ is NOT a decomposition "
        "artifact — its sign, ≥3-body purity, and O(1.6) magnitude are well-posed "
        "structural facts and the cross-channel hunt is JUSTIFIED. What is NOT well-"
        "posed is the 3-sig-fig VALUE 0.4708 / r*=1.585: a condition-number-8 residual "
        "with an irreducible ±8% isospin-correction band, honest target r*≈1.6±0.1. "
        "Siblings should score by sign + landing in [1.50,1.71], NOT by matching 1.585 "
        "to 3 sf (that would over-fit the isospin convention). Nothing wired.",
    "scriptHash": hashlib.sha256(this.read_bytes()).hexdigest()[:16],
    "results": results,
}
try:
    witness["scriptCommitSha"] = subprocess.check_output(
        ["git", "log", "-1", "--format=%H", "--", str(this)],
        cwd=this.parent, text=True).strip() or "uncommitted"
except Exception:
    witness["scriptCommitSha"] = "uncommitted"
out.write_text(json.dumps(witness, indent=2) + "\n")
print(f"\nwitness -> {out.name}")
