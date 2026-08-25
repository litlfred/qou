#!/usr/bin/env python3
"""Δ_λ binding-MAGNITUDE — the DAMPED graded dimension (Demazure sub-crystal).

Follow-on to #4012 (`deltalambda_jet_filtration_magnitude_probe.py` /
`JetFiltrationGradedDimEscape.lean`).  That probe showed the FULL coinvariant
graded dimension

        W_A(q) = [A]_q! = ∏_{k=1}^{A} [k]_q = Σ_{w∈S_A} q^{ℓ(w)}      (NON-determinant),
        ρ_grad(A) = W_A(q₀)/W_2(q₀),

ESCAPES the C(A,2) exchange-determinant cap (`SaturationRhoCap.lean`, ρ_A ≤ C(A,2))
but OVERSHOOTS the A=4 target: ρ_grad(3)=3.34 (−12% vs 3.81), ρ_grad(4)=15.74
(+21% vs 13.03).  #4012's reading: the physical magnitude lives strictly between
the sub-extensive log-det (capped, undershoots) and the super-extensive full graded
dim (overshoots) — the missing piece is a **bounded A=3→A=4 growth damping** of the
factorial growth [4]_q ≈ 4.71 toward the observed data step ≈ 3.42, WITHOUT falling
back below the C(A,2) cap.

AGENTS.md §7b names the interpolating object precisely: a **Demazure SUB-crystal**
graded dimension — a partial sum of [A]_q! over a Bruhat prefix {w ≤ v}
("incomplete / resonance state").  This probe forward-tests that object.

--------------------------------------------------------------------------------
The object (parameter-free, NOT a fit, NOT a determinant, NOT the prior
Demazure-FIBRE ansatz)
--------------------------------------------------------------------------------
Distinct from the FAILED prior "Demazure-fibre" ansatz
(`demazure-fiber-markov-trace.md`, one of the six refuted closures), which
RE-WEIGHTS the per-partition Jones–Markov coefficient
`T^Dem(λ;w) = y_λ · D_w(λ)/D_{w_0}(λ)`.  Here the object is the cross-A
**graded dimension** itself, truncated to a Bruhat sub-interval.

`[A]_q!` factors as a product of coset length-generating functions:
`[A]_q! = ∏_{k=1}^A [k]_q`, and `[k]_q = 1+q+…+q^{k-1}` IS the Poincaré polynomial
of the minimal-coset-representative set of `S_k/S_{k-1}` (reps of lengths
0,1,…,k−1).  A **coset-chain Demazure sub-crystal** truncates each coset at a
level `t_k ≤ k−1` (keep reps of length `0..t_k`, i.e. the Bruhat prefix up to the
length-`t_k` element), giving

        W^dem_A(t) = ∏_{k=2}^A [t_k + 1]_q ,     t_k ∈ {0,…,k−1} ,
        ρ_dem(A)   = W^dem_A(t) / W^dem_2 ,       W^dem_2 = [2]_q (deuteron reference,
                                                  the SATURATED 2-body state, kept full).

Full truncation `t_k = k−1` recovers `[k]_q` and `ρ_dem = ρ_grad` (#4012).  The
ONLY choices are the DISCRETE truncation levels `t_k` (no continuous fitted knob),
and q₀ is fixed from the substrate BEFORE any comparison.

--------------------------------------------------------------------------------
Decisive questions
--------------------------------------------------------------------------------
  (Q1) Does a parameter-free Demazure sub-crystal LAND both {3.81, 13.03}?
  (Q2) If not, does the family at least BRACKET / TIGHTEN the #4012 range?
  (Q3) What is the structural obstruction — where does pure damping fail?

Result (forward-tested below):
  (Q1) NO.  Pure damping is MONOTONE-DECREASING (a Bruhat sub-sum of a
       non-negative-power series), so ρ_dem(A) ≤ ρ_grad(A) for every truncation.
       The FULL A=3 ratio ρ_grad(3)=[3]_{q0}=3.34 ALREADY undershoots the target
       3.81 — hence the ENTIRE Demazure sub-crystal family lies BELOW the A=3
       target (max member = full = 3.34 < 3.81).  Damping can only make A=3 worse.
       This is the sign obstruction: A=3 needs AMPLIFICATION (q>1 pushing [3]_q up),
       the exact OPPOSITE of a sub-crystal truncation.
  (Q2) YES for A=4.  The A=4 target 13.03 is BRACKETED between two CONSECUTIVE
       top-coset truncations of the A=3→A=4 step:
         drop-top  (t3=2,t4=2): ρ_dem(4) = [3]_q·[3]_q = 11.17  (−14%)
         full      (t3=2,t4=3): ρ_dem(4) = [3]_q·[4]_q = 15.74  (+21%).
       This TIGHTENS #4012's bracket {C(4,2)=6 (det cap) , 15.74 (full graded)}
       to {11.17 , 15.74} — the lower end rises from 6 to 11.17 with a genuinely
       structural (non-determinant, non-fitted) object.
  (Q3) The damping direction is CORRECT for the A=4 overshoot but WRONG for the
       A=3 undershoot.  A pure Demazure sub-crystal (monotone ≤ full) cannot be
       the whole correction: it needs to be composed with a q-amplification that
       lifts A=3 above the classical coinvariant ceiling 3!/2! = 3.

Verdict scope-(a): the Demazure sub-crystal graded dimension, ALONE, does not
reproduce {3.81, 13.03} at a single parameter-free q₀ — it BRACKETS A=4 (a real
tightening) but structurally cannot reach A=3 (monotone the wrong way).  It is NOT
excluded as an ingredient (permanence): a damping factor of this form may combine
with an A=3 amplification term.  No fit; nothing wired.  Selecting a truncation
level `t_k` to hit the data would be the forbidden 7th fit — NOT done.

Cross-refs: deltalambda_jet_filtration_magnitude_probe.py (#4012, the FULL graded
dim this damps); JetFiltrationGradedDimEscape.lean; DemazureSubcrystalGradedDim.lean
(this branch, the scope-(b) monotonicity certificate); SaturationRhoCap.lean (the
det cap this escapes); demazure-fiber-markov-trace.md (the DISTINCT prior
per-partition ansatz); docs/audits/2026-07-18-deltalambda-demazure-subcrystal.md.
"""
from __future__ import annotations

import itertools
import os
import sys

import mpmath as mp
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

_HERE = os.path.dirname(os.path.abspath(__file__))
_COMP = os.path.abspath(os.path.join(_HERE, ".."))
_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))
for _p in (_COMP, os.path.join(_ROOT, "tools", "qou-substrate", "python")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

# muon-canonical q₀ (computations/ layer convention); matches #4012 + sibling probes.
Q0_STR = "1.10997859555733471"


def q_int(k: int, q: mp.mpf) -> mp.mpf:
    """[k]_q = 1 + q + ... + q^{k-1} — the Coxeter-length / coinvariant Poincaré
    convention (the length-gen function of the minimal coset reps of S_k/S_{k-1})."""
    return sum((q ** j for j in range(k)), mp.mpf(0))


def demazure_ratio(trunc, q: mp.mpf) -> mp.mpf:
    """ρ_dem(A) for coset-chain truncation trunc = (t_3, ..., t_A), t_k ∈ {0..k-1}.
    W^dem_A = [2]_q · ∏_{k=3..A} [t_k+1]_q ; reference W^dem_2 = [2]_q ; so
    ρ_dem(A) = ∏_{k=3..A} [t_k+1]_q.  (deuteron A=2 kept FULL = saturated reference)."""
    out = mp.mpf(1)
    for k, tk in enumerate(trunc, start=3):
        out *= q_int(tk + 1, q)
    return out


def main() -> int:
    set_compute_dps()
    q0 = mp.mpf(Q0_STR)
    assertions = []

    def check(name, passed, detail=""):
        assertions.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {detail}")

    # -- isospin-corrected STRONG targets (identical construction to #4012 and the
    #    sibling bareven / coulomb-mirror probes; AME2020 + #3986/#3990 premise) --
    BD = mp.mpf("2.224566")
    B3H = mp.mpf("8.481821")
    B3He = mp.mpf("7.718058")
    B4 = mp.mpf("28.295673")
    EC3He = B3H - B3He
    EC4 = EC3He * (mp.mpf(3) / 4) ** (mp.mpf(1) / 3)
    T3 = B3H / BD                       # ≈ 3.813
    T4 = (B4 + EC4) / BD                # ≈ 13.03
    data_step = T4 / T3                 # ≈ 3.418
    print(f"strong targets:  ρ_strong(3) = {mp.nstr(T3,6)}   ρ_strong(4) = {mp.nstr(T4,6)}"
          f"   data step = {mp.nstr(data_step,6)}")

    det_cap4 = mp.mpf(6)                # C(4,2), the SaturationRhoCap ceiling (#4012)

    q1 = q_int(1, q0)
    q2 = q_int(2, q0)
    q3 = q_int(3, q0)
    q4 = q_int(4, q0)
    print(f"[1]={mp.nstr(q1,5)} [2]={mp.nstr(q2,5)} [3]={mp.nstr(q3,5)} [4]={mp.nstr(q4,5)}")

    # ---------------------------------------------------------------------------
    # 0. The object is a Bruhat SUB-SUM of [A]_q! (a graded dim), not the prior
    #    per-partition Demazure-FIBRE reweight, and not a determinant.  Verify each
    #    truncated coset factor [t_k+1]_q ≤ [k]_q (sub-sum of positive powers).
    # ---------------------------------------------------------------------------
    subsum_ok = all(q_int(t + 1, q0) <= q_int(k, q0) + mp.mpf(10) ** -40
                    for k in (2, 3, 4) for t in range(k))
    check("object_is_bruhat_subsum_graded_dim", subsum_ok,
          "each truncated coset factor [t_k+1]_q ≤ [k]_q (a Bruhat-prefix sub-sum of "
          "the positive-power coinvariant Poincaré [A]_q!) — a graded dimension, NOT "
          "−ln det and NOT the per-partition Demazure-fibre reweight y_λ·D_w/D_{w0}")

    # ---------------------------------------------------------------------------
    # 1. Enumerate the WHOLE parameter-free coset-chain Demazure family for A=3, A=4.
    # ---------------------------------------------------------------------------
    # A=3: t_3 ∈ {0,1,2}. ρ_dem(3) = [t_3+1]_q.
    rho3 = {t3: demazure_ratio((t3,), q0) for t3 in range(3)}
    rho3_max = max(rho3.values())                      # = [3]_{q0} (full)
    print("A=3 truncations:", {t: mp.nstr(v, 5) for t, v in rho3.items()})

    # A=4: (t_3,t_4) ∈ {0,1,2}×{0,1,2,3}. ρ_dem(4) = [t_3+1]_q·[t_4+1]_q.
    rho4 = {(t3, t4): demazure_ratio((t3, t4), q0)
            for t3 in range(3) for t4 in range(4)}

    # ---------------------------------------------------------------------------
    # 2. (Q3 obstruction) A=3 target lies ABOVE the ENTIRE family — pure damping
    #    is monotone ≤ full, and the full A=3 ratio already undershoots.
    # ---------------------------------------------------------------------------
    a3_family_all_below = rho3_max < T3                # 3.342 < 3.813
    check("A3_target_above_entire_demazure_family", a3_family_all_below,
          f"max over ALL A=3 truncations = ρ_grad(3) = [3]_{{q0}}={mp.nstr(rho3_max,6)} "
          f"< {mp.nstr(T3,6)} = ρ_strong(3).  A Bruhat sub-sum is ≤ the full sum, so "
          f"NO Demazure sub-crystal reaches A=3 — damping is monotone the WRONG way "
          f"(A=3 needs amplification: ρ_strong(3) > 3 = 3!/2!, the classical ceiling)")

    # ---------------------------------------------------------------------------
    # 3. (Q2 tightening) A=4 target is BRACKETED between two CONSECUTIVE top-coset
    #    truncations: drop-top (t3=2,t4=2)=[3][3] and full (t3=2,t4=3)=[3][4].
    # ---------------------------------------------------------------------------
    lo = rho4[(2, 2)]                                  # [3]_q·[3]_q  (drop top A3→A4 rep)
    hi = rho4[(2, 3)]                                  # [3]_q·[4]_q  (full = ρ_grad(4), #4012)
    a4_bracketed = lo < T4 < hi
    check("A4_target_bracketed_by_consecutive_truncations", a4_bracketed,
          f"drop-top ρ_dem(4)=[3]·[3]={mp.nstr(lo,6)} ({mp.nstr((lo/T4-1)*100,3)}%) "
          f"< {mp.nstr(T4,6)}=ρ_strong(4) < full [3]·[4]={mp.nstr(hi,6)} "
          f"(+{mp.nstr((hi/T4-1)*100,3)}%): the target sits between keeping 3 vs 4 "
          f"reps of the A=3→A=4 coset — a two-sided structural bracket")

    # ---------------------------------------------------------------------------
    # 4. (Q2 tightening) the bracket TIGHTENS #4012 {det cap 6, full 15.74}:
    #    the lower end rises from the determinant cap 6 to the structural 11.17.
    # ---------------------------------------------------------------------------
    tightens = lo > det_cap4                           # 11.17 > 6
    check("demazure_lower_bracket_tightens_pr4012", tightens,
          f"lower bracket rises from det cap C(4,2)={int(det_cap4)} (#4012, log-det) "
          f"to the Demazure drop-top {mp.nstr(lo,6)} — a genuine narrowing of the A=4 "
          f"magnitude window by a non-determinant, non-fitted object")

    # ---------------------------------------------------------------------------
    # 5. (Q1 honest negative) NO parameter-free member lands BOTH within 5%.
    #    (A=3 is impossible for the whole family; verify no (t3,t4) is jointly close.)
    # ---------------------------------------------------------------------------
    def close(v, t, tol=mp.mpf("0.05")):
        return abs(v / t - 1) < tol
    landed = [(t3, t4) for t3 in range(3) for t4 in range(4)
              if close(rho3[t3], T3) and close(rho4[(t3, t4)], T4)]
    no_member_lands_both = len(landed) == 0
    check("no_parameter_free_member_lands_both", no_member_lands_both,
          f"scanned all {len(rho4)} truncations: {len(landed)} land BOTH within 5% "
          f"(A=3 impossible — whole family ≤ 3.34 < 3.81); a truncation that hit the "
          f"data would be the forbidden 7th fit and is NOT wired")

    # convenience roll-ups
    rows = [
        {"A": 3, "target": float(T3), "family_max_rho_grad": float(rho3_max),
         "all_truncations": {str(t): float(v) for t, v in rho3.items()}},
        {"A": 4, "target": float(T4), "det_cap": float(det_cap4),
         "bracket_lo_droptop": float(lo), "bracket_hi_full": float(hi),
         "all_truncations": {f"{t3},{t4}": float(rho4[(t3, t4)])
                             for t3 in range(3) for t4 in range(4)}},
    ]

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "SCOPE-(a) HONEST NEGATIVE (does not land) + genuine A=4 TIGHTENING. "
        "The Demazure sub-crystal graded dimension ρ_dem(A)=W^dem_A/W^dem_2 "
        "(a Bruhat-prefix sub-sum of the coinvariant Poincaré [A]_q!, the DAMPED "
        "version of #4012's full graded dim; NON-determinant, and distinct from the "
        "prior per-partition Demazure-FIBRE reweight) is MONOTONE ≤ the full graded "
        "dim. It BRACKETS the A=4 target: drop-top [3]·[3]=11.17 < 13.03 < 15.74=full, "
        "tightening #4012's window {det cap 6, full 15.74} to {11.17, 15.74}. But it "
        "CANNOT land A=3: the whole family is ≤ ρ_grad(3)=[3]_{q0}=3.34 < 3.81, so "
        "damping is monotone the WRONG way for the A=3 undershoot (which needs "
        "amplification above the classical ceiling 3!/2!=3). Pure damping is thus the "
        "correct sign for A=4 but the wrong sign for A=3 — a Demazure sub-crystal "
        "alone is not the whole correction; it must compose with an A=3 amplification. "
        "NOT excluded as an ingredient (permanence). No fit; nothing wired; selecting "
        "a truncation level to hit the data is the forbidden 7th fit and is NOT done."
        if all_passed else
        "INCONCLUSIVE — an assertion failed; re-derive before citing."
    )
    print("\nVERDICT:", verdict)

    from substrate.witness_base import WitnessBuilder  # noqa: E402
    wb = WitnessBuilder(
        "deltalambda-demazure-subcrystal-magnitude", engine="mpmath",
        output_dir=os.path.join(_COMP, "deltalambda"), _script_path=__file__,
    )
    wb.set_description(
        "Damped graded dimension (Demazure sub-crystal) as the Δ_λ binding-magnitude "
        "interpolator between #4012's capped log-det and full coinvariant graded dim. "
        "A Bruhat-prefix sub-sum of [A]_q! (NON-determinant; distinct from the prior "
        "per-partition Demazure-fibre reweight). BRACKETS A=4 (tightens {6,15.74} to "
        "{11.17,15.74}) but structurally CANNOT land A=3 (whole family ≤ 3.34 < 3.81: "
        "pure damping is monotone the wrong way). Scope-(a) honest negative + A=4 "
        "tightening; no fit; nothing wired.")
    wb.set_content_block("conj:binding-manybody-eq-jet-filtration")
    wb.add_parameter("q0", Q0_STR)
    wb.add_parameter("q0_convention", "muon-canonical (computations/ layer)")
    wb.add_data("strong_targets", {"rho_strong_3": mp.nstr(T3, 8),
                                   "rho_strong_4": mp.nstr(T4, 8),
                                   "data_step_A3_to_A4": mp.nstr(data_step, 8),
                                   "construction": "AME2020 + Lean #3986/#3990 Coulomb premise"})
    wb.add_data("object", "rho_dem(A)=W^dem_A/W^dem_2 = prod_{k=3..A}[t_k+1]_q, "
                          "t_k in {0..k-1}: coset-chain Demazure sub-crystal graded dim "
                          "(Bruhat-prefix sub-sum of [A]_q!); NON-determinant; deuteron "
                          "W2=[2]_q kept full (saturated reference)")
    wb.add_data("distinct_from_prior_ansatz",
                "NOT the failed Demazure-FIBRE ansatz T^Dem(lambda;w)=y_lambda*D_w/D_w0 "
                "(per-partition reweight, demazure-fiber-markov-trace.md); this is the "
                "cross-A GRADED DIMENSION itself, Bruhat-truncated")
    wb.add_data("forward_test_rows", rows)
    wb.add_data("A4_bracket", {"lower_droptop_[3][3]": mp.nstr(lo, 8),
                               "target": mp.nstr(T4, 8),
                               "upper_full_[3][4]": mp.nstr(hi, 8),
                               "pr4012_lower_det_cap": 6,
                               "note": "lower bracket rises 6 -> 11.17 (tightening)"})
    wb.add_data("A3_obstruction", {"family_max_[3]_q0": mp.nstr(rho3_max, 8),
                                   "target": mp.nstr(T3, 8),
                                   "classical_ceiling_3!/2!": 3,
                                   "note": "whole Demazure family <= full graded dim, "
                                           "which already undershoots; damping monotone "
                                           "the WRONG way for A=3"})
    wb.add_data("verdict", verdict)
    wb.add_caveat("Scope-(a): the Demazure sub-crystal ALONE does not close the "
                  "magnitude; it is not excluded as an ingredient (permanence).")
    wb.add_caveat("A=3 obstruction is a monotonicity fact (sub-sum <= full sum), "
                  "proved q-independently in DemazureSubcrystalGradedDim.lean.")
    wb.add_caveat("No fit: q₀ fixed from substrate BEFORE comparison; truncation "
                  "levels are DISCRETE structural choices, enumerated exhaustively, "
                  "not fitted to the data. Selecting t_k to hit the data = 7th fit, "
                  "NOT done.")

    for a in assertions:
        wb.add_assertion(a["name"], computed=str(a["passed"]), expected="True",
                         source=a["detail"])
    wb.add_assertion("lands_both_targets_parameter_free", computed="False",
                     expected="False",
                     source="honest negative: brackets A=4, cannot reach A=3")

    out = wb.save(extra={"auditOnly": "docs/audits/2026-07-18-deltalambda-demazure-subcrystal.md"})
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
