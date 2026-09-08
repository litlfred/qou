#!/usr/bin/env python3
"""
A=3 magnitude ROUTE 2 — the super-Berezinian even/odd cross-sector mixing.

Question: does the Berezinian off-diagonal cross-term  t = B·D⁻¹·C  (the first
even↔odd sector mixing order) supply the missing A=3 magnitude factor
    r* = μ₃ / c₃ ≈ 1.585
where μ₃ = +0.4708 MeV is the AME residual 3-body moment (additive-residual
simplex, #4320) and c₃ = +0.297 MeV is the single-trace derived Borromean H₉
cluster deficit (#4364)?  Every SINGLE-Markov-trace ingredient (level / geometric
W_λ / edge / exact-order μ̄_A / Vassiliev-weight) is bracketed at c₃ = 0.63·μ₃ —
the missing 1.585× must be genuinely cross-channel (option-e.md).

This probe is the EMPIRICAL COMPANION to the Lean invariant
QOU.QBeta.SuperBerezinianA3Magnitude.crossTerm_magnitude_surjective (sorry-free):
the even-face correction (A − t)/A is a FREE parameter of the off-block, so r*
is reachable but only as a FIT.  We DEMONSTRATE (not fit-to-close):

  (1) record r* and the r* ≈ log₂3 coincidence (already flagged, Vassiliev row);
  (2) show block-diagonal (t=0) gives correction ≡ 1 — no lift (why single-trace
      is bracketed);
  (3) enumerate NATURAL parameter-free readings of ρ = t/A from the substrate
      (ℏ_q, h, h², odd/even sector ratio, ±1, ±2, (1+q)/2−1, …) and show the
      resulting corrections 1−ρ SCATTER — none lands r* without tuning ρ to the
      target value −0.585 (a fit, no natural substrate constant sits there);
  (4) exhibit the fit witness B* that hits r* exactly (the surjectivity map),
      confirming the magnitude is a hidden DOF (Rule 14).

NO value is wired; μ₃/c₃ are never inverted to DERIVE a substrate constant.
free_parameters = 0 in every DERIVED reading; the closure would need the
DM-cubic-derived off-block (qou-jqof), which is open.
"""
from __future__ import annotations

import json
import math
from datetime import datetime, timezone
from pathlib import Path

# q0 read BY NAME (bean qou-9ugp, 2026-09-04). This file bound the RETIRED
# self-certified muon pin A as a literal -- superseded 2026-08-22 by the
# CODATA-2022 derivation, so the value was ~46 ppb stale AND could not follow
# the anchor. This stem is not in `ideal_muon`, so `Q_50_DIGIT_STR` resolves to
# the PROTON pin, which the 2026-08-30 owner ruling makes the default.
import sys as _sys_qp  # noqa: E402
from pathlib import Path as _Path_qp  # noqa: E402
for _p_qp in (_Path_qp(__file__).resolve().parent,
              _Path_qp(__file__).resolve().parent / 'substrate',
              _Path_qp(__file__).resolve().parent.parent / 'computations',
              _Path_qp(__file__).resolve().parent.parent / 'computations' / 'substrate'):
    if str(_p_qp) not in _sys_qp.path:
        _sys_qp.path.insert(0, str(_p_qp))
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

# --- Framework constants (muon-q0 canonical computations/ layer) ---
Q0 = float(Q_50_DIGIT_STR)       # proton pin, read by name (computations/ layer)
H = Q0 - 1.0                     # h = q - 1
HBAR_Q = (Q0 - 1.0) / Q0         # ℏ_q = (q-1)/q

# --- The A=3 magnitude targets (from the option-e ledger; NOT recomputed here) ---
MU3 = 0.4708                     # AME residual 3-body moment (additive-residual simplex, #4320)
C3_SINGLE = 0.297                # single-trace derived Borromean H₉ cluster deficit (#4364)
R_STAR = MU3 / C3_SINGLE         # the missing magnitude factor
RHO_NEEDED = 1.0 - R_STAR        # t/A that a fit would require:  (A−t)/A = r*  ⟺  t/A = 1 − r*


def even_face_correction(rho: float) -> float:
    """(A − t)/A = 1 − t/A = 1 − rho.  The multiplicative lift the Berezinian
    cross-term supplies to the bar-even (mass/C1) face."""
    return 1.0 - rho


def main() -> None:
    print(f"q0            = {Q0}")
    print(f"h = q-1       = {H:.6f}")
    print(f"ℏ_q = (q-1)/q = {HBAR_Q:.6f}")
    print(f"μ3 (AME resid, +)  = {MU3}")
    print(f"c3 (single-trace)  = {C3_SINGLE}")
    print(f"r* = μ3/c3         = {R_STAR:.6f}")
    print(f"log2(3)            = {math.log2(3):.6f}   (r* ≈ log2 3: flagged coincidence, Vassiliev row)")
    print(f"ρ_needed = 1 − r*  = {RHO_NEEDED:.6f}   (the t/A a FIT would require — must be NEGATIVE, |ρ|~0.585)")
    print()

    # (2) no mixing => correction ≡ 1 (single-trace bracket)
    corr_nomix = even_face_correction(0.0)
    print(f"[no mixing, t=0] correction = {corr_nomix:.4f}  (≡1 → NO lift; every single-trace ingredient sits here)")
    print()

    # (3) natural parameter-free readings of ρ = t/A (0 free parameters each)
    # sector-ratio candidate: the odd/even A=3 sector value ratio, if the mixing
    # amplitude were the geometric coupling of the two diagonal sector scales.
    odd_over_even = C3_SINGLE / MU3   # a scale ratio available with no tuning (= 1/r*)
    candidates = {
        "ℏ_q":              HBAR_Q,
        "-ℏ_q":            -HBAR_Q,
        "h":                H,
        "-h":              -H,
        "h^2":              H * H,
        "-h^2":            -H * H,
        "(1+q)/2 - 1":      (1.0 + Q0) / 2.0 - 1.0,
        "odd/even ratio":   odd_over_even,
        "-odd/even ratio": -odd_over_even,
        "+1":               1.0,
        "-1":              -1.0,
        "+2":               2.0,
        "-2":              -2.0,
    }
    print("[natural parameter-free readings ρ = t/A]  correction 1−ρ  vs  r* = %.4f" % R_STAR)
    scatter = []
    for name, rho in candidates.items():
        corr = even_face_correction(rho)
        hit = abs(corr - R_STAR) < 0.02
        scatter.append({"reading": name, "rho": rho, "correction": corr,
                        "abs_err_vs_rstar": abs(corr - R_STAR), "lands_rstar": hit})
        flag = "  <-- lands r*!" if hit else ""
        print(f"   ρ = {name:18s} = {rho:+.4f}   ->  correction = {corr:+.4f}{flag}")
    n_hit = sum(1 for s in scatter if s["lands_rstar"])
    print(f"   => {n_hit}/{len(candidates)} natural readings land r* within 2%  "
          f"(none = no parameter-free substrate constant sits at ρ = {RHO_NEEDED:.3f})")
    print()

    # (4) the fit witness: surjectivity — pick B to hit r* exactly (Lean crossTerm_magnitude_surjective)
    # Model A = 1, C = 1, D = 1 (any nonzero); B* = A(1−r*)DC⁻¹ = 1 − r* = ρ_needed.
    A, C, D = 1.0, 1.0, 1.0
    B_fit = A * (1.0 - R_STAR) * D / C     # the Lean witness B = A(1−r)DC⁻¹
    t_fit = B_fit * (1.0 / D) * C
    corr_fit = (A - t_fit) / A
    print(f"[surjectivity fit witness] B* = A(1−r*)DC⁻¹ = {B_fit:+.6f}")
    print(f"   t* = B*·D⁻¹·C = {t_fit:+.6f}   ->  correction = (A−t*)/A = {corr_fit:.6f}  (= r*, exact)")
    print(f"   => magnitude reachable ONLY by pinning B to the target = a FIT (hidden DOF, Rule 14).")
    print()

    verdict = (
        "scope-(a): the Berezinian cross-term does NOT derive r*. Its magnitude "
        "(A−t)/A is a free parameter of the off-block B (Lean crossTerm_magnitude_surjective); "
        "no natural parameter-free substrate reading lands r* — matching it pins B to the "
        "target (a fit). The route is NOT excluded (unlike the bracketed single-trace family it "
        "CAN reach O(1)), but it relocates the wall to deriving B,C from the DM q-cubic (qou-jqof, open). "
        "r* ≈ log2 3 is a flagged coincidence."
    )
    print("VERDICT:", verdict)

    witness = {
        "computation": "a3-magnitude-berezinian-crossterm",
        "scriptFile": "a3_magnitude_berezinian_crossterm_probe.py",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "engine": "python-float (demonstration; no high-precision needed — structural, 0 free params)",
        "free_parameters": 0,
        "inputs": {"q0": Q0, "h": H, "hbar_q": HBAR_Q,
                   "mu3_MeV": MU3, "c3_single_trace_MeV": C3_SINGLE,
                   "mu3_source": "additive-residual-simplex #4320",
                   "c3_source": "borromean-H9-magnitude-lift #4364"},
        "results": {
            "r_star": R_STAR,
            "log2_3": math.log2(3),
            "r_star_is_log2_3_coincidence": abs(R_STAR - math.log2(3)) < 0.01,
            "rho_needed_for_fit": RHO_NEEDED,
            "correction_no_mixing": corr_nomix,
            "natural_readings_scatter": scatter,
            "n_natural_readings_landing_rstar": n_hit,
            "fit_witness_B_star": B_fit,
            "fit_witness_correction": corr_fit,
        },
        "verdict": verdict,
        "scope": "(a) scope-limited: magnitude underdetermined (free off-block), not a structural exclusion",
        "lean": "QOU.QBeta.SuperBerezinianA3Magnitude.crossTerm_magnitude_surjective (sorry-free)",
        "wired": False,
        "notes": "μ3/c3 never inverted to derive a substrate constant; DEMONSTRATES the free-parameter "
                 "structure, does not fit-to-close. Closure needs the DM-cubic-derived off-block (qou-jqof).",
    }
    out = Path(__file__).parent / "a3-magnitude-berezinian-crossterm.witness.json"
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added.
    #
    # q0 anchor (bean qou-v6wz sibling): this witness IS q0-dependent -- Q0 is
    # read from the anchor (Q_50_DIGIT_STR), and inputs.q0 / inputs.h /
    # inputs.hbar_q and every results.natural_readings_scatter[*] value move
    # under QOU_Q0_ANCHOR=muon vs =proton (24 substantive fields, ~1e-8 = the
    # mu-p tension). The prior `q0_anchor=False` (= stamp `independent`) was a
    # copy-paste of the wrong stamp block (with a stale `# no q0 in this
    # producer's cone` comment): it declared layer-freedom on a q0-dependent
    # witness, so the q0-anchor-flip audit skipped it (an audit-escape). Resolve
    # the anchor from the manifest instead: this stem is not in `ideal_muon`, so
    # it resolves to the PROTON pin (the 2026-08-30 owner default).
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=None)
    out.write_text(json.dumps(witness, indent=2))
    print(f"\nwitness -> {out}")


if __name__ == "__main__":
    main()
