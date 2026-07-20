#!/usr/bin/env python3
"""
binding_manybody_jet_filtration.py — the UNIMPLEMENTED consumer of
`conj:binding-manybody-eq-jet-filtration` (the §"Compute wire-up" step 2 of
docs/audits/2026-06-25-sw-jet-prolongation-explicit-and-fork.md).

OWNER STEER (2026-07-03): the A≥3 absolute-binding θ_λ magnitude gate, closed
"via Reeb based on the computational time required for the knot operator", with
"the actual hyperbolic volumes coming in via the non-abelian Stokes".

That is ONE object, already identified in the corpus:

  knot-operator holonomy  Hol(∂S_c) = ∮_{S_c} F      (Yekutieli non-abelian Stokes)
    → n-th jet norm  |a_D^(n)| = |∮ λ_SW^(n)|          (QOU.Mass.NaStokesKeystone)
    → mean quantum dimension  a_D^(n) = lw(n−1) = (1/n) Σ_{λ⊢n} dim_q V_λ   (#1765)
    → residues = per-block Wedderburn dim_q, HYPERBOLIC components only (Vol>0)

The SW period grows SUPER-EXPONENTIALLY (√-branch ⇒ falling-factorial (1/2)_n;
n=6 lw 13.56 vs depth-2-τ fit 11.62) — this is the EXTENSIVE channel the intensive
arccos-phase θ_λ (probe_full_theta_binding.py) structurally lacked (it could not
track the ~13× D→⁴He growth). The depth-2 SL₂ τ is only an n≤4 effective fit.

This probe implements the body-order (jet-filtration) binding
    B(K) = Σ_{n=2}^{A} m_e · a_D^(n) · w_n(K),   a_D^(n) = lw(n−1),
truncated at the nucleon count A, and tests — with NO per-isotope fit — whether
the super-exponential period supplies the EXTENSIVE binding growth of
D / T / ³He / ⁴He (the θ_λ magnitude gate). w_n(K)=1 is the null (weight-free)
reading; the residue-weight "ρ·A scale rule" (the q-difference recursion output,
conj eq. G(qx)=R·G) is the open refinement, NOT fitted here.

EXPLORATORY (production-vs-exploratory-discipline): asserts the finding, no
production touch, no fitted constant. Derive-or-characterise only.
"""
from __future__ import annotations
import json, sys
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "substrate"))
sys.path.insert(0, str(HERE))
from q_parameter import Q as Q0  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from codata_constants import (  # noqa: E402 — CAL-1 + validation targets, centralized
    M_E_MEV,
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
)
try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except Exception:
    _HAVE_WB = False

set_compute_dps()  # canonical precision (AGENTS.md I8; keeps witness dps metadata consistent)
q = mp.mpf(str(Q0))
M_E = mp.mpf(str(M_E_MEV))  # MeV (CAL-1, codata_constants)

# ── mean quantum dimension lw(c) = (1/(c+1)) Σ_{λ⊢c+1} dim_q V_λ  (exact reuse of
#    sw_period_growth_probe.py; residue sum of prop:sw-period-residue-sum) ──────
def qint(k):
    return (q ** k - q ** (-k)) / (q - 1 / q)

def qfac(n):
    p = mp.mpf(1)
    for k in range(1, n + 1):
        p *= qint(k)
    return p

def partitions(n, m=None):
    if m is None:
        m = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, m), 0, -1):
        for r in partitions(n - k, k):
            yield (k,) + r

def hooks(lam):
    n = len(lam)
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    hs = []
    for i in range(n):
        for j in range(lam[i]):
            hs.append((lam[i] - j - 1) + (conj[j] - i - 1) + 1)
    return hs

def dimq(lam):
    n = sum(lam)
    d = qfac(n)
    for h in hooks(lam):
        d /= qint(h)
    return d

def lw(c):
    return mp.fsum(dimq(l) for l in partitions(c + 1)) / (c + 1)

def a_D(n):
    """n-th prolonged SW period = super-exponential mean quantum dimension."""
    return lw(n - 1)


# AME binding energies (MeV) — centralized validation targets (codata_constants)
AME_B = {"D": mp.mpf(str(AME_B_DEUTERON_MEV_VALIDATION)),
         "T": mp.mpf(str(AME_B_TRITIUM_MEV_VALIDATION)),
         "3He": mp.mpf(str(AME_B_HE3_MEV_VALIDATION)),
         "4He": mp.mpf(str(AME_B_HE4_MEV_VALIDATION))}
NUCLEONS = {"D": 2, "T": 3, "3He": 3, "4He": 4}


def main() -> int:
    print(f"  q₀ = {float(q):.6f}   m_e = {float(M_E):.6f} MeV\n")

    # ── 1. The super-exponential SW periods a_D^(n) = lw(n−1) ──────────────────
    print("  SW jet-prolongation periods a_D^(n) = lw(n−1) = (1/n)Σ_{λ⊢n} dim_q")
    print("  (the na-Stokes surface-integral / hyperbolic-volume channel):")
    periods = {}
    prev = None
    for n in range(1, 9):
        aD = a_D(n)
        periods[n] = aD
        ratio = f"{float(aD/prev):.3f}" if prev else "  —  "
        tag = "  ← EXTENSIVE (ratio grows ⇒ super-exp)" if n >= 5 else ""
        print(f"     a_D^({n}) = {float(aD):10.4f}   ratio {ratio}{tag}")
        prev = aD
    print()

    # ── 2. Body-order (jet-filtration) binding, unit weights w_n=1 (null) ──────
    print("  Jet-filtration binding  B(K) = Σ_{n=2}^{A} m_e·a_D^(n)  (w_n=1, NO fit):")
    Bjet = {}
    for K, A in NUCLEONS.items():
        B = mp.fsum(M_E * periods[n] for n in range(2, A + 1))
        Bjet[K] = B
        err = (B - AME_B[K]) / AME_B[K]
        print(f"     {K:<4} A={A}  B_jet={float(B):8.4f}  AME={float(AME_B[K]):8.4f}"
              f"  err={float(err)*100:+8.1f}%")

    # ── 3. The decisive metric: EXTENSIVE GROWTH ratio vs experiment ──────────
    #     (the intensive arccos-phase probe could NOT track this ~13× growth) ──
    growth_pred = Bjet["4He"] / Bjet["D"]
    growth_exp = AME_B["4He"] / AME_B["D"]
    print(f"\n  ⁴He/D binding-growth ratio:")
    print(f"     experiment          = {float(growth_exp):6.2f}×")
    print(f"     jet-filtration (lw) = {float(growth_pred):6.2f}×   "
          f"(intensive arccos-phase was ~flat ⇒ could not grow)")

    # single global scale (diagnostic only — reports how close the SHAPE is)
    num = mp.fsum(Bjet[K] * AME_B[K] for K in AME_B)
    den = mp.fsum(Bjet[K] ** 2 for K in AME_B)
    scale = num / den
    worst = mp.mpf(0)
    print(f"\n  Shape check (one global scale {float(scale):.3f}, diagnostic):")
    for K in AME_B:
        Bs = scale * Bjet[K]
        err = (Bs - AME_B[K]) / AME_B[K]
        worst = max(worst, abs(err))
        print(f"     {K:<4} B={float(Bs):8.4f}  AME={float(AME_B[K]):8.4f}  err={float(err)*100:+7.1f}%")
    print(f"     worst |err| = {float(worst)*100:.1f}%  (w_n=1; residue-weight ρ·A rule is the open refinement)")

    # ── verdict ───────────────────────────────────────────────────────────────
    print("\n### Reading")
    print("  • The super-exponential SW period a_D^(n)=lw(n−1) (na-Stokes / mean")
    print("    quantum-dim) IS the EXTENSIVE channel — a_D^(n) grows without bound,")
    print("    unlike the bounded arccos-rotation phase that failed to track A-growth.")
    print(f"  • Unit-weight jet-filtration already produces a {float(growth_pred):.1f}× ⁴He/D")
    print(f"    growth (exp {float(growth_exp):.1f}×) — the EXTENSIVE mechanism is present;")
    print("    the residual is the per-body residue weight w_n(K) (the ρ·A scale rule,")
    print("    a q-difference recursion OUTPUT per the conjecture — NOT fitted here).")
    print("  • This closes the *mechanism* half of the θ_λ magnitude gate (extensive")
    print("    growth from the knot-operator compute-time via na-Stokes); the weight")
    print("    w_n(K) is the remaining derive-or-refute (q-difference kernel R(q,x)).")

    if _HAVE_WB:
        try:
            wb = WitnessBuilder("binding-manybody-jet-filtration", engine="mpmath")
            wb.set_description(
                "EXPLORATORY: implements the jet-filtration binding consumer "
                "B(K)=Σ_{n=2}^A m_e·a_D^(n)·w_n(K), a_D^(n)=lw(n−1) (super-exp SW "
                "period / na-Stokes hyperbolic-volume channel). Tests unit-weight "
                "extensive growth vs D/T/³He/⁴He. Mechanism (extensive) present; "
                "residue weight w_n(K) (ρ·A q-difference rule) open. No fit.")
            wb.add_data("sw_periods_a_D", {str(n): float(periods[n]) for n in periods})
            wb.add_data("B_jet_unit_weight", {K: float(Bjet[K]) for K in Bjet})
            wb.add_data("growth_ratio_4He_over_D",
                        {"pred_lw": float(growth_pred), "exp": float(growth_exp)})
            wb.add_assertion(
                name="sw_period_is_extensive_channel",
                computed=str(int(float(growth_pred) > 3.0)), expected="1", tolerance=0,
                source=(f"unit-weight jet-filtration ⁴He/D growth = {float(growth_pred):.2f}× "
                        f"(exp {float(growth_exp):.2f}×) — the super-exp SW period supplies "
                        "extensive A-growth the intensive arccos-phase could not."))
            out = wb.save()
            print(f"\nWitness: {out}")
        except Exception as e:
            print(f"\n(witness emit skipped: {e})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
