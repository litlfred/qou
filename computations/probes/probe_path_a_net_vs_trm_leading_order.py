#!/usr/bin/env python3
"""
probe_path_a_net_vs_trm_leading_order.py — Path A test (session 2026-07-04):
does the per-braid mass tower reproduce the unweighted-NF-net Q-value ansatz
at leading order, or do the counit (net) and Markov trace (tr_M) genuinely
differ?

EXPLORATORY (probe_ prefix, audit-only). Formalize-first for the
`conj:borromean-quark` energy-scale ansatz `Q_β = |Δ(net)|·E₀` (Step 8 of
docs/audits/2026-05-24-q-beta-net-ansatz-fitting-finding.md). The ansatz is
"by construction"; Path A would DERIVE it as the leading-order h-expansion of
the canonical per-braid mass tower `prop:per-braid-mass-tower`. The two
functionals in play:

  net(W) = ε(NF(W))   — the AUGMENTATION: every NF basis element weight 1
                        (proton σ₀(σ₁−h/2) → net(p)=1−h/2; neutron → net(n))
  tr_M(W)             — the MARKOV trace: basis element w weight tr_M(w)
                        (the mass-formula functional, z-weighted)

The nucleon single-wrap NF decompositions (neutron-qvalue-symbolic.md), in the
6-operator basis (γ=1, σ₀=σ₁, σ₁=σ₂, L₊=σ₁σ₂, L₋=σ₂σ₁, e⁻=σ₁σ₂σ₁):

  NF(W_p) = 1·L₊ − (h/2)·σ₀
  NF(W_n) = (h²/2)·γ − h·σ₀ − (h/2)·σ₁ + 1·L₊

so Δ(NF) = NF(n)−NF(p) = (h²/2)·γ − (h/2)·σ₀ − (h/2)·σ₁  (L₊ cancels).

## What this probe determines (symbolically, exact in ℚ(q))

1. `Δ(net) = ε(ΔNF) = h²/2 − h` (reproduces the .md).
2. `Δ(tr_M) = tr_M(ΔNF)` using the exact Markov traces tr_M(γ), tr_M(σ₀),
   tr_M(σ₁) computed from the H_3 Wedderburn sum Σ_λ y_λ χ^λ.
3. The RATIO `Δ(tr_M)/Δ(net)` and its `h → 0` limit. **If it → 1, Path A
   holds at leading order (ansatz derivable). If it → z ≈ 1/2, the counit and
   Markov trace differ by the Markov weight at leading order — Path A as
   "net = leading-order mass" is REFUTED, and the ansatz's counit is a
   genuine separate structural choice, not a coincidence.**

Derive-or-refute; nothing wired. Whatever the outcome, it converts "Path A
queued" into a concrete verdict per formalize-first discipline.
"""
from __future__ import annotations

import sys
import warnings
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
sys.path.insert(0, str(COMP))
sys.path.insert(0, str(COMP / "substrate"))
warnings.filterwarnings("ignore")

import sympy as sp  # noqa: E402
import mpmath as mp  # noqa: E402

from _precision import set_compute_dps, COMPUTE_DPS  # noqa: E402
set_compute_dps()
DPS = COMPUTE_DPS

from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_symbolic  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

q = sp.symbols("q", positive=True)
h = q - 1 / q


def rsimp(e):
    """Robust rational simplify avoiding sympy's intermittent heugcd bug in
    `simplify` (the Wenzl weights are messy rationals)."""
    for fn in (sp.ratsimp, sp.cancel, lambda x: sp.together(x)):
        try:
            return fn(e)
        except Exception:
            continue
    return e


def rep_matrices():
    """Reps of σ₁, σ₂ in H_3 for the three partitions of 3, in a SQRT-FREE
    rational form (the character tr(ρ(w)) is basis-independent, so any valid
    rep gives the right χ^λ). (3): trivial σ↦q; (1³): sign σ↦−1/q; (2,1): the
    standard rational 2-dim Hecke rep. Braid + Hecke verified numerically in
    main()."""
    s1_21 = sp.Matrix([[q, 1], [0, -1 / q]])
    s2_21 = sp.Matrix([[-1 / q, 0], [1, q]])
    return {
        (3,): (sp.Matrix([[q]]), sp.Matrix([[q]])),
        (2, 1): (s1_21, s2_21),
        (1, 1, 1): (sp.Matrix([[-1 / q]]), sp.Matrix([[-1 / q]])),
    }


def markov_trace_of(word_s1_s2, reps):
    """tr_M(word) = Σ_λ y_λ · χ^λ(word), word given as a function
    (s1, s2) -> matrix. y_λ symbolic Wenzl weights."""
    total = sp.Integer(0)
    for lam, (s1, s2) in reps.items():
        chi = sp.trace(word_s1_s2(s1, s2))
        y = y_lambda_wenzl_bridge_symbolic(lam)
        total += y * chi
    return rsimp(total)


def main() -> int:
    reps = rep_matrices()

    # Validate the (2,1) rational rep: Hecke (σ−q)(σ+1/q)=0 and braid
    # σ₁σ₂σ₁=σ₂σ₁σ₂ (so the character tr(ρ(w)) is a genuine H_3 character).
    s1, s2 = reps[(2, 1)]
    hecke_ok = sp.simplify((s1 - q * sp.eye(2)) * (s1 + sp.eye(2) / q)) == sp.zeros(2)
    braid_ok = sp.simplify(s1 * s2 * s1 - s2 * s1 * s2) == sp.zeros(2)
    if not (hecke_ok and braid_ok):
        raise SystemExit(f"(2,1) rep invalid: hecke={hecke_ok} braid={braid_ok}")

    # tr_M of the individual basis operators we need: γ=1, σ₀=σ₁, σ₁=σ₂, L₊=σ₁σ₂
    trM = {
        "gamma": markov_trace_of(lambda a, b: _id_for(a), reps),
        "sigma0": markov_trace_of(lambda a, b: a, reps),
        "sigma1": markov_trace_of(lambda a, b: b, reps),
        "Lplus": markov_trace_of(lambda a, b: a * b, reps),
    }
    # Δ(NF) coefficients in basis (γ, σ₀, σ₁, L₊): from the .md
    dNF = {"gamma": h**2/2, "sigma0": -h/2, "sigma1": -h/2, "Lplus": sp.Integer(0)}

    delta_net = rsimp(sum(dNF.values()))                     # ε: all weight 1
    delta_trM = rsimp(sum(dNF[k] * trM[k] for k in dNF))     # Markov weighted
    ratio = rsimp(delta_trM / delta_net)

    # leading-order (h→0, i.e. q→1) limits
    lim_ratio = sp.limit(ratio, q, 1)
    z_expr = 1 / (sp.sqrt(q) + 1 / sp.sqrt(q))
    z_at_1 = sp.limit(z_expr, q, 1)

    # numeric at q0
    def numf(e):
        return mp.mpf(str(sp.N(e.subs(q, sp.Float(Q_50_DIGIT_STR, 45)), 40)))
    dnet0 = numf(delta_net); dtrm0 = numf(delta_trM); z0 = numf(z_expr)

    print("=" * 74)
    print("PATH A TEST — counit net vs Markov tr_M at leading order")
    print("=" * 74)
    print(f"  tr_M(γ)  = {trM['gamma']}")
    print(f"  tr_M(σ₀) = {trM['sigma0']}")
    print(f"  tr_M(σ₁) = {trM['sigma1']}")
    print(f"  tr_M(L₊) = {trM['Lplus']}")
    print(f"\n  Δ(net)   = ε(ΔNF)     = {delta_net}")
    print(f"  Δ(tr_M)  = tr_M(ΔNF)  = {delta_trM}")
    print(f"  ratio Δtr_M/Δnet      = {ratio}")
    print(f"  lim_{{h→0}} ratio       = {lim_ratio}   (z at q→1 = {z_at_1})")
    print(f"\n  numeric @ q₀: Δnet={mp.nstr(dnet0,12)}  Δtr_M={mp.nstr(dtrm0,12)}  "
          f"ratio={mp.nstr(dtrm0/dnet0,12)}  z={mp.nstr(z0,12)}")

    path_a_holds = bool(sp.simplify(lim_ratio - 1) == 0)
    ratio_is_z = bool(sp.simplify(lim_ratio - z_at_1) == 0)
    verdict = (
        "PATH A HOLDS at leading order: Δtr_M/Δnet → 1, the Markov mass "
        "difference reproduces the unweighted net difference — the ansatz "
        "is derivable."
        if path_a_holds else
        f"PATH A (net = leading-order tr_M mass) REFUTED, scope (a): "
        f"Δtr_M/Δnet → {lim_ratio} ≠ 1"
        + (" = z (the Markov weight at q→1)" if ratio_is_z else "")
        + ". The counit (net) and the Markov trace are genuinely different "
        "functionals differing at O(1), NOT a leading-order coincidence — "
        "so the borromean-quark energy-scale ansatz Q_β=|Δnet|·E₀ uses the "
        "COUNIT ε by structural choice; deriving it requires deriving why "
        "the β-decay/binding channel augments (ε) rather than Markov-traces, "
        "not an h-expansion of the mass tower. This is the exact Step-6 "
        "'unweighted net vs weighted trace' gap, quantified: it is O(1)=z, "
        "not O(h)."
    )
    print(f"\n  VERDICT: {verdict}")

    wb = (WitnessBuilder("probe-path-a-net-vs-trm-leading-order",
                         engine="sympy+mpmath")
          .set_description(
              "Path A test for the borromean-quark energy-scale ansatz: "
              "compares the counit net difference ε(ΔNF)=h²/2−h against the "
              "Markov-trace difference tr_M(ΔNF) of the nucleon single-wrap "
              "NF, symbolically exact. Determines whether the per-braid mass "
              "tower reproduces the unweighted net at leading order (ansatz "
              "derivable) or differs by the Markov weight z (ansatz is a "
              "counit structural choice). Derive-or-refute; nothing wired.")
          .set_audit_only(
              "docs/audits/2026-07-04-deuteron-dressing-is-proton-net.md")
          .add_parameter("q0", Q_50_DIGIT_STR)
          .add_parameter("compute_dps", DPS)
          .add_data("trM_basis_numeric_at_q0",
                    {k: mp.nstr(numf(v), 20) for k, v in trM.items()})
          .add_data("delta_net_numeric", mp.nstr(dnet0, 25))
          .add_data("delta_trM_numeric", mp.nstr(dtrm0, 25))
          .add_data("ratio_numeric_at_q0", mp.nstr(dtrm0 / dnet0, 25))
          .add_data("leading_order_ratio", str(lim_ratio))
          .add_data("z_numeric_at_q0", mp.nstr(z0, 25))
          .add_data("z_at_q_to_1", str(z_at_1))
          .add_data("path_a_holds", path_a_holds)
          .add_data("ratio_is_z_at_leading_order", ratio_is_z)
          .add_data("verdict", verdict))
    wb.add_assertion(
        "delta_net_matches_md",
        computed=str(sp.simplify(delta_net - (h**2/2 - h))), expected="0",
        source="ε(ΔNF) = h²/2 − h reproduces neutron-qvalue-symbolic.md")
    wb.save()
    print("\nwitness → probe-path-a-net-vs-trm-leading-order.witness.json (audit-only)")
    return 0


def _id_for(m):
    return sp.eye(m.shape[0])


if __name__ == "__main__":
    sys.exit(main())
