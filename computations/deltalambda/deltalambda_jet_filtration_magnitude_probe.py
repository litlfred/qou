#!/usr/bin/env python3
"""Δ_λ binding-MAGNITUDE, NON-determinant object class (jet-filtration graded dimension).

The three merged Lean no-gos (IsospinMirrorInvariance, SaturationRhoCap,
B4CumulantBarEven) close the ENTIRE exchange-DETERMINANT-cumulant family: for the
isospin-even complete-graph exchange matrix `I + m(J−I)` the connected cumulant
`b_A = −ln det_A` is EXTENSIVE and *saturates*, capping the binding-magnitude ratio at

        ρ_A = b_A / b_2  ≤  C(A,2) = A(A−1)/2      (SaturationRhoCap, machine-verified).

At A=3 the cap is 3, at A=4 the cap is 6.  The isospin-corrected STRONG targets
ρ_strong(3) ≈ 3.81 > 3 and ρ_strong(4) ≈ 13.03 > 6 EXCEED the caps, so no
`−ln det(exchange matrix)` can reach them for any m — a proved scope-(b) exclusion.

This probe attacks from OUTSIDE that family with a genuinely different object:
a **jet-filtration graded dimension**, NOT a determinant / log-det.  A `−ln det`
is sub-extensive in the mode count (that is WHY it caps at C(A,2)); a graded
dimension is FACTORIAL and is not so capped.

--------------------------------------------------------------------------------
The object (parameter-free, no fit, NOT a determinant)
--------------------------------------------------------------------------------
The QOU principal grading g_ρ is the Gröbner–Shirshov / jet-order (word-length =
Coxeter-length) filtration on the A-nucleon Hecke module H_A(q) (DERIVED, #3542 /
`PrincipalGradingJetOrder.lean`; n(λ)=min maj(SYT(λ)) is its bottom degree on V_λ,
the fake-degree valuation).  The corresponding EXTENSIVE object is the **graded
dimension** of that principal filtration — the Poincaré polynomial of the
coinvariant algebra of S_A:

        W_A(q) = Σ_{w ∈ S_A} q^{ℓ(w)} = [A]_q!  =  ∏_{k=1}^{A} [k]_q ,
                 [k]_q = 1 + q + ⋯ + q^{k−1} ,

equivalently the fake-degree sum  W_A(q) = Σ_{λ⊢A} dim(λ)·f^λ(q)  (f^λ = fake
degree, the graded multiplicity of V_λ in the coinvariant algebra).  This is
Σ_k dim(gr_k)·q^k — a graded dimension, a sum of POSITIVE q-powers.  It is NOT
`−ln det` of any exchange matrix, so it is outside the Lean-excluded family.

Magnitude candidate:  ρ_grad(A) = W_A(q₀) / W_2(q₀)  (deuteron A=2 reference),
tested at the FIXED substrate q₀ (no free knob) BEFORE any comparison.

--------------------------------------------------------------------------------
Decisive questions
--------------------------------------------------------------------------------
  (Q1) Does the graded dimension ESCAPE the C(A,2) cap — can it even REACH
       ρ_4 = 13.03, which the determinant provably cannot (cap 6)?
  (Q2) Does it LAND both {3.81, 13.03} at a single parameter-free q₀?

Result (forward-tested below):
  (Q1) YES — and the escape is q-INDEPENDENT: the classical (q=1) ratio A!/2! is
       {3, 12}; at A=4 that is 12 > 6 = C(4,2).  Factorial dimension growth is
       super-quadratic, so the graded dimension is structurally NOT bounded by the
       C(A,2) determinant cap.  This is the first non-determinant object that can
       reach ρ_4 = 13.03.  STRUCTURAL ADVANCE.
  (Q2) NO — at q₀ the ratios are ρ_grad(3) ≈ 3.342 (target 3.813, −12%) and
       ρ_grad(4) ≈ 15.74 (target 13.03, +21%).  It UNDERSHOOTS A=3 and OVERSHOOTS
       A=4: the growth step ρ(4)/ρ(3) = [4]_{q₀} ≈ 4.71 is too steep vs the data
       ratio 13.03/3.81 = 3.42.  The step is ≥ 4 for ALL q ≥ 1 (and A=3 needs
       q ≈ 1.25 to reach 3.81, which sends A=4 to ≈ 22), so NO single parameter-free
       q lands both.  Sharpest single fact: ρ_strong(3) = 3.81 EXCEEDS even the full
       classical coinvariant ratio 3!/2! = 3.

Reading (bracket):  sub-extensive log-det (ρ_A ≤ C(A,2), undershoots BOTH targets)
   <  true binding magnitude  <  super-extensive graded dim (overshoots A=4 growth).
The physical magnitude lives strictly BETWEEN quadratic-capped and factorial.

Verdict scope-(a) (honest negative on the crack; positive on the escape): the
coinvariant graded dimension, ALONE, does not reproduce {3.81, 13.03} at a single
parameter-free q₀.  It is NOT excluded as an ingredient — permanence: a proved
graded-dim factor may combine with a growth-DAMPING term; this probe measures the
size and DIRECTION of the missing correction (a damping of the A=3→A=4 step from
factorial ~4.7 toward the observed ~3.4).  Nothing wired; no fit.

Cross-refs: SaturationRhoCap.lean / B4CumulantBarEven.lean / IsospinMirrorInvariance.lean
(the no-go family); deltalambda_grho_jet_order_derivation_probe.py (g_ρ = jet-order
grading, DERIVED); deltalambda_binding_block_trace_probe.py (#3542, the per-partition
dim² block trace — my object is its cross-A EXTENSIVE lift);
docs/audits/2026-07-18-deltalambda-attack-vector-map.md.
"""
from __future__ import annotations

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

# muon-canonical q₀ (computations/ layer convention); matches the sibling
# deltalambda probes.  The ESCAPE result is q-independent (q=1 ratio already
# exceeds the cap), so the q₀ pin only affects the (failing) landing test.
Q0_STR = "1.10997859555733471"


def q_int(k: int, q: mp.mpf) -> mp.mpf:
    """[k]_q = 1 + q + ... + q^{k-1} (unbalanced q-integer; the Coxeter-length /
    coinvariant Poincaré convention, NOT the balanced (q^k−q^{−k})/(q−q^{−1})).
    [k]_1 = k."""
    return sum((q ** j for j in range(k)), mp.mpf(0))


def q_factorial(A: int, q: mp.mpf) -> mp.mpf:
    """W_A(q) = [A]_q! = ∏_{k=1}^{A} [k]_q = Σ_{w∈S_A} q^{ℓ(w)} — the graded
    dimension (Poincaré polynomial) of the S_A coinvariant algebra / the principal
    (jet-order) filtration on H_A(q).  A product of q-integers — NOT a determinant."""
    out = mp.mpf(1)
    for k in range(1, A + 1):
        out *= q_int(k, q)
    return out


def classical_factorial(A: int) -> int:
    out = 1
    for k in range(2, A + 1):
        out *= k
    return out


def main() -> int:
    set_compute_dps()
    q0 = mp.mpf(Q0_STR)

    assertions = []

    def check(name, passed, detail=""):
        assertions.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {detail}")

    # -- isospin-corrected STRONG targets (identical construction to the sibling
    #    bareven / coulomb-mirror probes, from AME2020 + the #3986/#3990 premise) --
    BD = mp.mpf("2.224566")        # deuteron binding (A=2 reference)
    B3H = mp.mpf("8.481821")       # ³H (Z=1: Coulomb-free ⇒ pure strong)
    B3He = mp.mpf("7.718058")      # ³He
    B4 = mp.mpf("28.295673")       # ⁴He
    EC3He = B3H - B3He             # Lean #3986: strong ³H/³He split = 0 ⇒ split is all Coulomb
    EC4 = EC3He * (mp.mpf(3) / 4) ** (mp.mpf(1) / 3)   # #3990: pp-Coulomb, radius ~ A^{1/3}
    rho_strong_3 = B3H / BD                            # ≈ 3.813
    rho_strong_4 = (B4 + EC4) / BD                     # ≈ 13.03
    T3, T4 = rho_strong_3, rho_strong_4
    print(f"strong targets:  ρ_strong(3) = {mp.nstr(T3,6)}   ρ_strong(4) = {mp.nstr(T4,6)}")

    cap3, cap4 = mp.mpf(3), mp.mpf(6)                  # C(3,2), C(4,2) — the det cap

    # ---------------------------------------------------------------------------
    # 0. sanity: W_A(q) is the length generating function (NOT a determinant).
    #    W_A(1) = A!  and  W_A(q) = Σ_{w∈S_A} q^{ℓ(w)} (check A=3 coefficient list).
    # ---------------------------------------------------------------------------
    w_classical_ok = all(q_factorial(A, mp.mpf(1)) == classical_factorial(A) for A in (2, 3, 4, 5))
    # S_3 length distribution: lengths {0,1,1,2,2,3} → Poincaré 1+2q+2q²+q³ = [2]_q[3]_q.
    q_sym = mp.mpf("1.7")
    poincare_s3 = 1 + 2 * q_sym + 2 * q_sym ** 2 + q_sym ** 3
    w3_match = abs(q_factorial(3, q_sym) - poincare_s3) < mp.mpf(10) ** -40
    check("W_A_is_length_gen_func_not_determinant", w_classical_ok and w3_match,
          "W_A(q)=[A]_q!=∏[k]_q: W_A(1)=A! (A=2..5) and W_3(q)=1+2q+2q²+q³="
          "Σ_{w∈S_3}q^{ℓ(w)} (a Poincaré polynomial, a sum of positive q-powers — "
          "NOT −ln det of any exchange matrix ⇒ outside the Lean-excluded family)")

    # ---------------------------------------------------------------------------
    # 1. ESCAPE the C(A,2) cap — and the escape is q-INDEPENDENT (holds at q=1).
    #    Classical (q=1) graded-dim ratio A!/2!: A=3→3, A=4→12.  12 > 6 = C(4,2).
    # ---------------------------------------------------------------------------
    rho_cl_3 = mp.mpf(classical_factorial(3)) / classical_factorial(2)   # 3
    rho_cl_4 = mp.mpf(classical_factorial(4)) / classical_factorial(2)   # 12
    escape_q1 = rho_cl_4 > cap4                                          # 12 > 6
    check("graded_dim_escapes_C_A_2_cap_at_q1", escape_q1,
          f"classical (q=1) ratio A!/2!: ρ(3)={int(rho_cl_3)}, ρ(4)={int(rho_cl_4)}; "
          f"ρ(4)=12 > 6 = C(4,2) ⇒ the graded dimension escapes the determinant cap "
          f"WITHOUT any q (factorial growth is super-quadratic)")

    # q₀ Poincaré ratios (the parameter-free substrate reading).
    W2 = q_factorial(2, q0)
    W3 = q_factorial(3, q0)
    W4 = q_factorial(4, q0)
    rho_grad_3 = W3 / W2      # = [3]_{q0}
    rho_grad_4 = W4 / W2      # = [3]_{q0}·[4]_{q0}
    escape_q0_reaches_T4 = rho_grad_4 > T4   # 15.74 > 13.03 ⇒ can REACH ρ_4
    check("graded_dim_at_q0_reaches_rho4_target", escape_q0_reaches_T4,
          f"ρ_grad(4)(q₀)={mp.nstr(rho_grad_4,6)} > {mp.nstr(T4,6)}=ρ_strong(4) ⇒ "
          f"the object CAN reach the A=4 target magnitude (the determinant, capped "
          f"at 6, provably cannot). First non-determinant object to clear ρ_4.")

    # ---------------------------------------------------------------------------
    # 2. A=3 is genuinely hard: ρ_strong(3)=3.81 EXCEEDS even A!/2!=3 (classical cap).
    # ---------------------------------------------------------------------------
    a3_exceeds_classical = T3 > rho_cl_3     # 3.813 > 3
    check("rho3_target_exceeds_classical_coinvariant_ratio", a3_exceeds_classical,
          f"ρ_strong(3)={mp.nstr(T3,6)} > 3 = 3!/2! (the full classical coinvariant "
          f"dimension ratio) ⇒ A=3 needs q>1; at q₀, [3]_{{q0}}={mp.nstr(rho_grad_3,6)} "
          f"still < {mp.nstr(T3,6)} (undershoots by "
          f"{mp.nstr((rho_grad_3/T3-1)*100,3)}%)")

    # ---------------------------------------------------------------------------
    # 3. WRONG growth rate: the A=3→A=4 step [4]_q is too steep for ALL q ≥ 1.
    #    data step = T4/T3 = 3.42; graded step [4]_q ≥ 4 for q ≥ 1; at q₀ = 4.71.
    # ---------------------------------------------------------------------------
    data_step = T4 / T3                       # ≈ 3.418
    grad_step_q0 = W4 / W3                     # = [4]_{q0} ≈ 4.710
    grad_step_q1 = q_int(4, mp.mpf(1))         # [4]_1 = 4
    step_too_steep = grad_step_q1 > data_step  # 4 > 3.42 already at q=1 (monotone ↑ in q)
    check("graded_step_too_steep_for_all_q_ge_1", step_too_steep,
          f"data step T4/T3={mp.nstr(data_step,5)}; graded step [4]_q is {int(grad_step_q1)} "
          f"at q=1 and {mp.nstr(grad_step_q0,5)} at q₀ — monotone ↑ in q, so [4]_q ≥ 4 > "
          f"{mp.nstr(data_step,5)} for ALL q ≥ 1 ⇒ the A=3→A=4 growth is intrinsically "
          f"too steep; no q flattens it to the data ratio")

    # ---------------------------------------------------------------------------
    # 4. no single parameter-free q lands BOTH (fixing A=3 up sends A=4 over).
    #    Solve [3]_q = T3 (q≈1.25); report the forced ρ_grad(4) at that q.
    # ---------------------------------------------------------------------------
    #  [3]_q = 1+q+q² = T3  ⇒  q = (−1+√(4T3−3))/2
    q_fix3 = (-1 + mp.sqrt(4 * T3 - 3)) / 2
    rho4_forced = q_factorial(4, q_fix3) / q_factorial(2, q_fix3)   # [3][4] at q_fix3
    forced_overshoot = abs(rho4_forced / T4 - 1) > mp.mpf("0.05")
    check("single_q_cannot_land_both", forced_overshoot,
          f"forcing ρ_grad(3)=ρ_strong(3) needs q={mp.nstr(q_fix3,6)}; at that q "
          f"ρ_grad(4)={mp.nstr(rho4_forced,6)} vs target {mp.nstr(T4,6)} "
          f"(+{mp.nstr((rho4_forced/T4-1)*100,3)}%) ⇒ no single parameter-free q lands both")

    # convenience roll-ups for the witness
    rows = [
        {"A": 2, "target_rho": 1.0, "C_A_2_cap": 1.0,
         "classical_A!/2!": 1.0, "graded_q0_ratio": 1.0},
        {"A": 3, "target_rho": float(T3), "C_A_2_cap": float(cap3),
         "classical_A!/2!": float(rho_cl_3), "graded_q0_ratio": float(rho_grad_3)},
        {"A": 4, "target_rho": float(T4), "C_A_2_cap": float(cap4),
         "classical_A!/2!": float(rho_cl_4), "graded_q0_ratio": float(rho_grad_4)},
    ]

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "SCOPE-(a) HONEST NEGATIVE on the crack, STRUCTURAL ADVANCE on the escape. "
        "The jet-filtration graded dimension W_A(q)=[A]_q!=Σ_{w∈S_A}q^{ℓ(w)} "
        "(=Σ_λ dim(λ)f^λ(q), coinvariant Poincaré / graded dim of the principal "
        "filtration on H_A) is a NON-determinant object — a sum of positive q-powers, "
        "not −ln det — so it is outside the three Lean-excluded exchange-determinant "
        "no-gos. It ESCAPES the C(A,2) cap, q-INDEPENDENTLY: the classical ratio "
        "A!/2!={3,12} already has 12 > 6=C(4,2), and at q₀ ρ_grad(4)=15.74 > 13.03 "
        "⇒ it is the FIRST non-determinant object that can REACH ρ_4=13.03 (the "
        "determinant provably cannot). It does NOT land both parameter-free: at q₀ "
        "ρ_grad(3)=3.34 (−12%) and ρ_grad(4)=15.74 (+21%); it undershoots A=3 and "
        "overshoots A=4. The A=3→A=4 step [4]_q ≥ 4 for all q≥1 is too steep vs the "
        "data ratio 3.42, and ρ_strong(3)=3.81 exceeds even the classical 3!/2!=3, so "
        "no single parameter-free q lands both. BRACKET: sub-extensive log-det "
        "(undershoots both, capped) < true binding < super-extensive graded dim "
        "(overshoots A=4). NOT excluded as an ingredient (permanence): a graded-dim "
        "factor may combine with a growth-DAMPING term; this probe measures the "
        "direction of the missing correction. No fit; nothing wired."
        if all_passed else
        "INCONCLUSIVE — an assertion failed; re-derive before citing."
    )
    print("\nVERDICT:", verdict)

    # ---------------------------------------------------------------------------
    from substrate.witness_base import WitnessBuilder  # noqa: E402
    wb = WitnessBuilder(
        "deltalambda-jet-filtration-magnitude", engine="mpmath",
        output_dir=os.path.join(_COMP, "deltalambda"), _script_path=__file__,
    )
    wb.set_description(
        "Non-determinant Δ_λ binding-magnitude object: the jet-filtration graded "
        "dimension W_A(q)=[A]_q!=Σ_{w∈S_A}q^{ℓ(w)} (coinvariant Poincaré / graded dim "
        "of the principal filtration on H_A). Escapes the C(A,2) determinant cap "
        "q-independently (A!/2!={3,12}, 12>6) and can reach ρ_4=13.03, but does NOT "
        "land both {3.81,13.03} at a single parameter-free q₀ (undershoots A=3, "
        "overshoots A=4 growth). Scope-(a) honest negative + escape advance; no fit; "
        "nothing wired.")
    wb.set_content_block("conj:binding-manybody-eq-jet-filtration")
    wb.add_parameter("q0", Q0_STR)
    wb.add_parameter("q0_convention", "muon-canonical (computations/ layer)")
    wb.add_data("strong_targets", {"rho_strong_3": mp.nstr(T3, 8),
                                   "rho_strong_4": mp.nstr(T4, 8),
                                   "construction": "AME2020 + Lean #3986/#3990 Coulomb premise"})
    wb.add_data("det_cap_C_A_2", {"A3": 3, "A4": 6,
                                  "source": "SaturationRhoCap.lean (ρ_A ≤ C(A,2))"})
    wb.add_data("object", "W_A(q)=[A]_q!=prod_{k=1}^A [k]_q = sum_{w in S_A} q^{len(w)} "
                          "(coinvariant Poincaré / jet-filtration graded dim); "
                          "NON-determinant (no -ln det)")
    wb.add_data("forward_test_rows", rows)
    wb.add_data("graded_step_A3_to_A4", {"data_T4/T3": mp.nstr(data_step, 6),
                                         "graded_[4]_q1": 4,
                                         "graded_[4]_q0": mp.nstr(grad_step_q0, 6)})
    wb.add_data("forced_fit_check", {"q_forcing_rho3": mp.nstr(q_fix3, 8),
                                     "rho4_forced": mp.nstr(rho4_forced, 6),
                                     "overshoot_pct": mp.nstr((rho4_forced / T4 - 1) * 100, 4)})
    wb.add_data("verdict", verdict)
    wb.add_caveat("Scope-(a): the graded dimension ALONE does not close the magnitude; "
                  "it is not excluded as an ingredient (permanence).")
    wb.add_caveat("The ESCAPE (graded dim > C(A,2) cap) is proved q-independently "
                  "(A!/2!=12>6) — a structural advance, not a numerical near-match.")
    wb.add_caveat("No fit: q₀ fixed from substrate BEFORE comparison; the q_forcing_rho3 "
                  "solve is shown ONLY to demonstrate no single q lands both — it is NOT wired.")

    for a in assertions:
        wb.add_assertion(a["name"], computed=str(a["passed"]), expected="True",
                         source=a["detail"])
    wb.add_assertion("lands_both_targets_parameter_free", computed="False", expected="False",
                     source="honest negative: no single parameter-free q lands both {3.81,13.03}")

    out = wb.save(extra={"auditOnly": "docs/audits/2026-07-18-deltalambda-jet-filtration-magnitude.md"})
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
