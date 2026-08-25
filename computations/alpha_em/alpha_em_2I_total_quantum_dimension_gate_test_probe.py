#!/usr/bin/env python3
"""alpha_em_2I_total_quantum_dimension_gate_test_probe.py

Runs the merged α_EM↔W_λ shared-wall ACCEPTANCE GATE (#3853) against the corpus's
OWN fixed modular data — the decisive self-test that does NOT wait on Front-2's
colored-LR amplitude compute (the total quantum dimension D is a coarser invariant
than |S_{0λ}|, computable from the quantum dimensions d_q(λ) alone).

The gate (#3853): the α_EM per-loop measure 1/(π b₁)=1/(8π) (b₁=dim H¹(M_Bring)=8)
and the m_p/m_μ W_λ keystone are ONE wall via a nonabelian S₀₀=1/D IFF
    D_{genus-4}(ζ→q₀) = b₁ = 8    (π = universal 1-loop factor), or
    D_{genus-4}(ζ→q₀) = π·b₁ = 8π (π categorical).

The modular data is fixed unambiguously by the corpus (no level scan):
`QOU.…KeystoneVerlindeSMatrixBridge` defines the Verlinde vacuum row
    bwS0(λ) = d_q(λ) / √(Σ_{μ∈P} d_q(μ)²) ,   D := √(Σ_{μ∈P} d_q(μ)²),
and the McKay / A₅⊂S₅ / binary-icosahedral (2I, |S₅|=|2I|=120) object fixes
P = partitions of n=5 (the lepton generation). d_q(λ) is the hook-content quantum
dimension [n]_q!/∏_{cells}[hook]_q. At the OBSERVABLE substrate q₀ (real ≈1.11,
NOT a root of unity) the full untruncated λ⊢5 set is the only well-defined choice
— the non-unitary object the merged keystone gate identified (Σ_λ W_λ=Z(q₀)<1).

RESULT — the gate FALSIFIES the shared-wall hypothesis in its literal form
(scope-(a) NEGATIVE; C14; no fit; no α_k wired):

    D(q₀) = √(Σ_{λ⊢5} d_q(λ)²) = 11.3569 …   ≠ 8   and   ≠ 8π (25.1327).
    (D(1) = √(5!) = √120 = 10.9545, the RSK/Burnside anchor; D grows with q>1.)
    D/8 = 1.4196,  D/8π = 0.4519 — neither a clean integer-b₁ nor a π·b₁ match.

So on the OBSERVABLE side, the keystone total quantum dimension D (from the n=5
partition modular data) is NOT the photon count b₁=8 nor 8π: the α_EM per-loop
measure 1/(π b₁) and the W_λ keystone 1/D are **distinct normalizations** under
the naive S₀₀=1/D identification. b₁=8 (genus-4 homology count) and D(q₀)=11.357
(n=5 partition-modular datum) are different objects.

SCOPE (STRICT — this is a scope-(a) negative, NOT a structural exclusion): it
refutes the *specific* identification "photon b₁ = keystone D at q₀", tested
against the corpus's fixed data. It does NOT exclude every shared-wall form — a
FIBRE-side level-truncated admissible D(ζ) at a root of unity (Front-2's
colored-LR territory), a different index/combination, or b₁ entering via a route
other than the total quantum dimension could still link the two walls. Recorded
as (a) per the anti-over-claim discipline. The gate did its job: it was
falsifiable, fed non-tunable corpus data, and returned NO — no fitting, nothing
wired, 1/(8π) stays a phase-4 identification.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402

# reuse ONLY the pure-python partition + hook enumerators from the merged keystone gate
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "docs" / "audits" / "scripts"))
import keystone_wlambda_unitarity_normalization_gate_probe as kg  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
B1 = 8  # dim H¹(M_Bring) = 2g, g=4


def qint(q, k):
    return (q ** k - q ** (-k)) / (q - 1 / q)


def qfact(q, n):
    r = mp.mpf(1)
    for k in range(1, n + 1):
        r *= qint(q, k)
    return r


def dq(q, lam):
    """Hook-content quantum dimension d_q(λ) = [n]_q!/∏_cells [hook]_q."""
    num = qfact(q, sum(lam))
    den = mp.mpf(1)
    for h in kg.hooks(lam):
        den *= qint(q, h)
    return num / den


def total_D(q, n):
    return mp.sqrt(mp.fsum(dq(q, lam) ** 2 for lam in kg.parts(n)))


def main() -> int:
    print("=" * 78)
    print(" α_EM shared-wall gate SELF-TEST — corpus D(q₀) vs the targets {8, 8π}")
    print("=" * 78)
    q0 = q_at(40)

    print("\n Total quantum dimension D(q) = √(Σ_{λ⊢n} d_q(λ)²) [KeystoneVerlindeSMatrixBridge]:")
    rows = []
    for n in (2, 3, 4, 5):
        D0 = total_D(q0, n)
        D1 = mp.sqrt(mp.mpf(mp.factorial(n)))
        tag = "  ← n=5: the fixed 2I/A₅⊂S₅ keystone datum" if n == 5 else ""
        print(f"   n={n}: D(q₀)={mp.nstr(D0,12)}   D(1)=√{n}!={mp.nstr(D1,8)}{tag}")
        rows.append({"n": n, "D_q0": mp.nstr(D0, 20), "D_1_sqrt_nfact": mp.nstr(D1, 12)})

    D = total_D(q0, 5)
    t8, t8pi = mp.mpf(8), 8 * mp.pi
    match_8 = abs(D - t8) < mp.mpf("1e-3")
    match_8pi = abs(D - t8pi) < mp.mpf("1e-3")
    print(f"\n TARGETS: b₁ = 8;  π·b₁ = 8π = {mp.nstr(t8pi,10)}")
    print(f" D(q₀) (n=5) = {mp.nstr(D,12)}")
    print(f"   D/8   = {mp.nstr(D/t8,8)}   (match 8?   {match_8})")
    print(f"   D/8π  = {mp.nstr(D/t8pi,8)}  (match 8π?  {match_8pi})")
    print("\n ⇒ D(q₀)=11.357 ∉ {8, 8π}: the shared-wall identification 'photon b₁ = keystone D'")
    print("   is FALSIFIED on the observable side (scope-(a) negative). b₁=8 (genus-4 homology")
    print("   count) and D(q₀)=11.357 (n=5 partition modular datum) are DISTINCT objects.")
    print("   NOT excluded: a fibre-side truncated D(ζ) at a root of unity (Front-2 colored-LR),")
    print("   or a different index route. No fit; nothing wired; 1/(8π) stays a phase-4 id.")

    wb = WitnessBuilder("alpha-em-2I-total-quantum-dimension-gate-test", engine="mpmath")
    wb.set_description(
        "Self-test of the merged α_EM↔W_λ shared-wall acceptance gate (#3853) against the "
        "corpus's OWN fixed modular data — no wait on Front-2's colored-LR, no level scan. "
        "KeystoneVerlindeSMatrixBridge fixes D=√(Σ_{λ∈P} d_q(λ)²) with P=partitions of n=5 "
        "(McKay/A₅⊂S₅/2I, |S₅|=|2I|=120); d_q = hook-content quantum dimension; observable q₀ "
        "⇒ full untruncated non-unitary set. RESULT: D(q₀)=11.3569 — NEITHER 8 NOR 8π "
        "(25.1327); D(1)=√120=10.9545; D/8=1.4196, D/8π=0.4519. So the naive S₀₀=1/D "
        "identification FALSIFIES the shared-wall in its literal form: the keystone total "
        "quantum dimension D (n=5 partition datum) ≠ the photon count b₁=8 (genus-4 homology) "
        "≠ 8π. α_EM 1/(π b₁) and the W_λ keystone 1/D are DISTINCT normalizations on the "
        "observable side. Scope-(a) NEGATIVE (not a structural exclusion): a fibre-side "
        "truncated admissible D(ζ) at a root of unity, or a different index route, could still "
        "link them. The gate was falsifiable, fed non-tunable corpus data, returned NO. No "
        "fit; no α_k wired; 1/(8π) stays a phase-4 identification."
    )
    wb.set_content_block("prop:alpha-em-categorical-trace")
    wb.add_data("D_by_n", rows)
    wb.add_data("gate_result", {
        "D_q0_n5": mp.nstr(D, 20), "target_b1": 8, "target_pi_b1": mp.nstr(t8pi, 12),
        "ratio_D_over_8": mp.nstr(D / t8, 12), "ratio_D_over_8pi": mp.nstr(D / t8pi, 12),
        "matches_8": bool(match_8), "matches_8pi": bool(match_8pi),
        "verdict": "D(q₀)=11.357 ∉ {8,8π} ⇒ shared-wall 'photon b₁ = keystone D' FALSIFIED on "
                   "the observable side (scope-(a) negative); distinct normalizations"})
    wb.add_data("scope", {
        "classification": "(a) scope-limited negative",
        "not_excluded": "fibre-side truncated admissible D(ζ) at a root of unity (Front-2 "
                        "colored-LR), or a different index route linking b₁ and the keystone data"})
    wb.add_assertion("shared_wall_D_equals_b1_or_pi_b1_FALSIFIED",
                     computed=0.0 if not (match_8 or match_8pi) else 1.0, expected=0.0, tolerance=0.5,
                     source="D(q₀)=√(Σ_{λ⊢5} d_q²)=11.357 ∉ {8, 8π} (corpus-fixed n=5 data, no scan) => "
                            "the naive S₀₀=1/D shared-wall identification is falsified on the observable side")
    wb.save()
    print("\n  RESULT: D(q₀)=11.357 ∉ {8,8π} ⇒ shared-wall FALSIFIED (observable side, scope-(a)).")
    print("          The gate did its job: falsifiable, non-tunable data, honest NO.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
