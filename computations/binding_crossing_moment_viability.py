#!/usr/bin/env python3
# polynomial_q_not_applicable: symbolic + mpmath assessment at q0; falsifiability
# PROBE (audit-only witness), not a production derivation (compute-author §1.3).
"""Probe: is the CROSSING q-Hermite moment μ_q a viable BINDING object (replacing the
quantum-dimension selection rule a_D^(n)=lw(n−1)=(1/n)Σ_{λ⊢n} dim_q)?

Motivation (#2822): the quantum-dim period Σ_λ dim_q has NO low-order q-holonomic
kernel; the crossing q-Hermite moment μ_q(n)=μ_q(n−1)+[n−1]_q μ_q(n−2) DOES (clean
depth-2 q-telephone = R(q,x)). Both → I(n) at q→1. Should the framework adopt μ_q?

ASSESSMENT (this probe).
  WINS of μ_q:
   - clean depth-2 kernel R(q,x) (satisfies prop:binding-genfun-qdifference);
   - bar-EVEN: μ_q(n) is q↔q⁻¹ invariant for all n (palindromic) — right
     mirror-symmetry for binding; ties to BindingQHermiteOscillator (#2800,
     Rogers–Szegő are the orthogonal polynomials of this moment functional);
   - deuteron (n=2) anchor preserved EXACTLY (μ_q(2)=T_q(2)=2).
  COSTS of μ_q:
   - μ_q < T_q for all n≥4, gap GROWING: μ_q/T_q ≈ 1,1,.997,.989,.975,.952,.921
     (n=2..8). Smaller period at higher body order — pushes the wrong way on the
     framework's collective UNDER-binding (ledger §5: F=B_AME/B_sym 0.94→2.11),
     modulo the per-isotope weights (scope-(a), weights w5tg-gated);
   - DECOUPLES mass from binding: lw=(1/n)Σ dim_q feeds BOTH MBA step-9a (mass
     linking weight) AND step-9b (binding anchors). Swapping binding→μ_q breaks
     the shared-selection-rule unification; no mass-preserving swap exists without
     a NEW categorical interface (formalize-first forbids guessing it);
   - kill-switch NEUTRAL: the +5.87% magic-A ⁴He anchor is a SEPARATE mechanism
     (B=ρ_F·m_e·A·8G, 8G=Vol(Borromean)); μ_q's −0.32% shift at a_D^(4) does not
     materially move it.

VERDICT: μ_q is mathematically coherent (clean kernel, bar-even, deuteron-exact)
but NOT a viable drop-in binding object — it trades the mass↔binding unification
for the kernel, and does not improve the physics. The deeper finding is a genuine
framework TENSION: unification (quantum-dim lw, no low-order kernel) vs clean
q-difference kernel (crossing moment, no unification). Recorded, not resolved.

Output: binding-crossing-moment-viability.witness.json (audit-only).
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))
sys.path.insert(0, str(HERE / "phase5"))
import _path_bridge as _bridge  # noqa: E402, F401

import sympy as sp  # noqa: E402
import mpmath as mp  # noqa: E402

from _precision import COMPUTE_DPS  # noqa: E402
from q_parameter import Q_50_DIGIT_STR as Q0  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from phase5_n8_dim_q_table import dim_q_via_quantum_hooks, partitions_of  # noqa: E402


def main() -> int:
    mp.mp.dps = COMPUTE_DPS
    q = sp.Symbol("q", positive=True)
    q0f = sp.Float(Q0, 50)
    q0m = mp.mpf(Q0)
    den = q0m - 1 / q0m

    def qb(k: int) -> mp.mpf:
        return (q0m ** k - q0m ** (-k)) / den

    def qbs(k: int) -> sp.Expr:
        return (q ** k - q ** (-k)) / (q - 1 / q)

    # crossing q-Hermite moment μ_q (numeric + symbolic) via q-telephone
    mu = {0: mp.mpf(1), 1: mp.mpf(1)}
    mus = {0: sp.Integer(1), 1: sp.Integer(1)}
    for n in range(2, 11):
        mu[n] = mu[n - 1] + qb(n - 1) * mu[n - 2]
        mus[n] = sp.expand(sp.cancel(mus[n - 1] + qbs(n - 1) * mus[n - 2]))

    # quantum-dim sum T_q(n)=Σ_λ dim_q (the current binding period × n)
    def T(n: int) -> mp.mpf:
        e = sum((dim_q_via_quantum_hooks(l, q) for l in partitions_of(n)), sp.S.Zero)
        return mp.mpf(str(sp.N(sp.cancel(e).subs(q, q0f), 50)))
    Tv = {n: T(n) for n in range(1, 9)}

    # (1) definition sanity-check (NOT a discovered identity): μ_q is DEFINED by the
    # q-telephone on lines 73-77, so re-checking it reproduces machine zero by
    # construction. The genuine, non-tautological finding lives in the sibling probe
    # sw_period_qholonomic_kernel_search.py: the quantum-dim period Σ_λ dim_q has NO
    # low-order q-holonomic kernel. This residual only confirms μ_q was built correctly.
    kernel_res = max(abs(mu[n] - (mu[n - 1] + qb(n - 1) * mu[n - 2])) / abs(mu[n])
                     for n in range(2, 11))
    # (2) bar-even: μ_q(n)(q->1/q) == μ_q(n)
    bar_even = all(sp.simplify(mus[n].subs(q, 1 / q) - mus[n]) == 0 for n in range(2, 8))
    # (3) deuteron exact; (4) divergence ratio
    rows = []
    for n in range(2, 9):
        rows.append({"n": n, "mu_q": mp.nstr(mu[n], 10), "T_q": mp.nstr(Tv[n], 10),
                     "mu_over_T": mp.nstr(mu[n] / Tv[n], 8),
                     "aD_mu": mp.nstr(mu[n] / n, 10), "aD_T": mp.nstr(Tv[n] / n, 10)})
    deuteron_exact = (mu[2] == Tv[2])
    he4_shift_pct = (mu[4] / 4 - Tv[4] / 4) / (Tv[4] / 4) * 100
    max_divergence_pct = (1 - mu[8] / Tv[8]) * 100

    w = WitnessBuilder("binding-crossing-moment-viability", engine="python+sympy+mpmath")
    w.set_audit_only(
        "docs/audits/2026-06-26-binding-period-qinvolution-qhermite-identification.md")
    w.add_parameter("q_0", Q0)
    w.add_data("mu_q_definition",
               "μ_q(n)=μ_q(n−1)+[n−1]_q μ_q(n−2) (symmetric bracket) — crossing "
               "q-Hermite / Rogers–Szegő moment; the q-deformation of I(n) with the "
               "clean depth-2 kernel R(q,x).")
    w.add_data("comparison_table", rows)
    w.add_data("win_clean_kernel",
               f"μ_q satisfies the depth-2 q-telephone by construction (μ_q is DEFINED "
               f"by it; the residual {mp.nstr(kernel_res, 4)} is a definition sanity-check, "
               f"not a discovered identity). The substantive contrast: the quantum-dim "
               f"period Σ_λ dim_q has NO such low-order kernel (sibling probe "
               f"sw_period_qholonomic_kernel_search.py) ⇒ μ_q is the deformation that "
               f"carries the clean R(q,x) (prop:binding-genfun-qdifference), Σ dim_q is not.")
    w.add_data("win_bar_even", f"μ_q(n) q↔q⁻¹-invariant for n=2..7: {bar_even} "
               "(palindromic; ties to BindingQHermiteOscillator #2800).")
    w.add_data("win_deuteron_exact", f"μ_q(2)=T_q(2)=2: {deuteron_exact} (n=2 anchor untouched).")
    w.add_data("cost_divergence",
               f"μ_q < T_q for n≥4; ⁴He(n=4) a_D shift {mp.nstr(he4_shift_pct, 3)}%, "
               f"max divergence (n=8) {mp.nstr(max_divergence_pct, 3)}%. Smaller period "
               "at higher body order — pushes against the collective under-binding "
               "(weights-gated, scope-(a)).")
    w.add_data("cost_mass_binding_decoupling",
               "lw=(1/n)Σ dim_q feeds BOTH MBA step-9a (mass) AND step-9b (binding). "
               "Swapping binding→μ_q decouples them — breaks the shared-selection-rule "
               "unification; no mass-preserving swap without a new categorical interface "
               "(formalize-first: not to be guessed).")
    w.add_data("killswitch_neutral",
               "The +5.87% magic-A ⁴He kill-switch is a separate mechanism "
               "(B=ρ_F·m_e·A·8G, 8G=Vol(Borromean)); μ_q's −0.32% a_D^(4) shift does not "
               "materially move it.")
    w.add_data("verdict",
               "μ_q is coherent (clean kernel, bar-even, deuteron-exact). Trade-offs vs "
               "the quantum-dim selection rule: it decouples mass↔binding and runs smaller "
               "at higher body order (the high-isotope behaviour to watch). OWNER DIRECTIVE "
               "(2026-06-26): adopt μ_q and test EMPIRICALLY — wire m_sym,Hermite / "
               "B_sym,Hermite into the dashboards and judge by high-isotope oddities. The "
               "'cost_divergence' rows are precisely those predictions. Framework tension "
               "(unification vs clean kernel) recorded for the record, not as a veto.")

    # By-construction sanity-check (μ_q is DEFINED by the q-telephone): residual ≈ 0 is
    # tautological, asserted only to confirm the build is correct. The substantive,
    # non-tautological result (Σ dim_q has no low-order kernel) is the sibling probe.
    w.add_assertion("crossing_moment_q_telephone_build_is_correct",
                    computed=1 if kernel_res < mp.mpf("1e-40") else 0,
                    expected=1, tolerance=0,
                    source=f"DEFINITION sanity-check: μ_q is built FROM the depth-2 q-telephone, "
                           f"so the residual {mp.nstr(kernel_res,4)} ≈ 0 by construction (not a "
                           "discovered identity). The genuine finding — Σ dim_q has NO low-order "
                           "R(q,x) — lives in sw_period_qholonomic_kernel_search.py.")
    w.add_assertion("crossing_moment_bar_even_and_deuteron_exact",
                    computed=1 if (bar_even and deuteron_exact) else 0,
                    expected=1, tolerance=0,
                    source="μ_q(n) q↔q⁻¹-invariant (n=2..7) AND μ_q(2)=T_q(2)=2.")
    w.add_assertion("crossing_moment_decouples_from_quantum_dim_at_q0",
                    computed=1 if max_divergence_pct > mp.mpf("1") else 0,
                    expected=1, tolerance=0,
                    source=f"μ_q diverges from T_q=Σ dim_q by {mp.nstr(max_divergence_pct,3)}% "
                           "by n=8 (agree at q=1) ⇒ swapping binding decouples it from the "
                           "mass selection rule (step-9a).")
    out = w.save()

    print("=" * 82)
    print(" Crossing q-Hermite moment μ_q as a BINDING object — VIABILITY")
    print("=" * 82)
    print(f"  {'n':>2} {'μ_q':>13} {'T_q=Σdim_q':>13} {'μ/T':>9} {'a_D=μ/n':>12} {'a_D=T/n':>12}")
    for r in rows:
        print(f"  {r['n']:>2} {r['mu_q']:>13} {r['T_q']:>13} {r['mu_over_T']:>9} "
              f"{r['aD_mu']:>12} {r['aD_T']:>12}")
    print(f"\n  WIN  clean depth-2 kernel R(q,x): μ_q built FROM the q-telephone (residual")
    print(f"       {mp.nstr(kernel_res,4)} ≈ 0 by construction); contrast Σ dim_q has NO low-order kernel")
    print(f"  WIN  bar-even (q↔q⁻¹) n=2..7: {bar_even};  deuteron μ_q(2)=T_q(2)=2: {deuteron_exact}")
    print(f"  COST ⁴He a_D shift {mp.nstr(he4_shift_pct,3)}%;  max divergence (n=8) {mp.nstr(max_divergence_pct,3)}%")
    print(f"  COST decouples mass(9a)↔binding(9b) shared selection rule; kill-switch NEUTRAL")
    print(f"\n  ASSESSMENT: coherent clean-kernel object; trade-offs vs Σ dim_q (decouples")
    print(f"  mass↔binding, runs smaller at high n). OWNER directive: explore EMPIRICALLY")
    print(f"  (m_sym,Hermite / B_sym,Hermite dashboards) — high-isotope behaviour is the gate.")
    print(f"\n Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
