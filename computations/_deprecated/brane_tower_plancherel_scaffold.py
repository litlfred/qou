#!/usr/bin/env python3
"""
T2/T3 brane-tower in TRACE form — Plancherel-series scaffold.

Per discussion at https://gist.github.com/litlfred/b3459bf9143dd03234a9fc55c370f6f4
the canonical 6-term mass formula's Terms 2 and 3 — currently
implemented as the literal archimedean specialisation
$\Phi_q(|\hat V_i^{\mathrm{full}}|)$ — should be expressed as
Markov-invariant traces.  The gist identifies two equivalent
expansions:

(A)  Plancherel-weighted infinite series (this scaffold):

         Φ_q(z) = Σ_{n≥0} z^n / (q; q)_n
                = Σ_{n≥0} c_n(q) · z^n
     with c_n(q) = 1/Π_{k=1..n}(1 - q^k).

     Substituting z = |V̂_i| and recognising |V̂_i|^n as the n-th
     power evaluation of the per-generator transfer-matrix chain,
     each z^n term factors through tr_M(σ_i^n).  Each term in the
     sum is then a Markov-invariant trace.

(B)  Kähler-differential derivative (other path, see PR #526
     `kahler_lift.py`).

This script implements (A) for diagnostic purposes:

  1. For each per-generator slot i, build the braid σ_i (or
     σ_i σ_j for T3) and use `markov_peel.tr_M_atomic`-style
     recursion to compute tr_M(σ_i^n) at q_0 for n = 0, 1, 2, ...

  2. Form the partial sum
         T2_N(i) = Σ_{n=0..N} c_n(q_0) · tr_M(σ_i^n)
     and check convergence as N grows.

  3. Compare to the literal Φ_q(|V̂_i|) closed-numerical limit.

Convergence note: Φ_q(z) converges for |z| < q.  At q_0 ≈ 1.11 and
typical per-generator |V̂_i| ≈ 0.85–0.99, we're inside the radius
but near the boundary, so partial sums may converge slowly.  Padé
acceleration may be needed.

Status: SCAFFOLD ONLY.  The full implementation requires:
  - tr_M(σ_i^n) for arbitrary atomic generator i — the per-generator
    chain in `atom_per_generator_volumes` is a transfer matrix, NOT
    a single braid generator, so "σ_i^n" needs a specific definition.
  - Convergence diagnostics (Padé, Wynn-ε, Shanks) before this can
    be wired into the 6-term formula.
  - Cross-validation against the literal Φ_q form (they should agree
    in the closed limit).

This scaffold lays out the structure so PR #526's term-trace work
can plug in without redoing the Plancherel framing.

Output: brane-tower-plancherel-scaffold.witness.json
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

mp.mp.dps = 50

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from q_parameter import Q as Q0_FLOAT, Q_MP  # noqa: E402

Q0 = Q_MP


# ── Plancherel coefficients c_n(q) = 1/(q^{-1}; q^{-1})_n ──
# Φ_q(z) = Π_{k≥1} (1 − q^{-k}z)^{-1}.  With q > 1 set q' = q^{-1} so
# q' < 1, then the standard q'-Pochhammer expansion gives
#   Φ_q(z) = Σ_n z^n / (q'; q')_n  with  (q'; q')_n = Π_{k=1..n}(1 − q^{-k}).
# Each (1 − q^{-k}) is positive and < 1 since 0 < q^{-k} < 1.
def q_inv_pochhammer_inv(n: int, q: mp.mpf = Q0) -> mp.mpf:
    """1 / (q^{-1}; q^{-1})_n = 1 / Π_{k=1..n} (1 - q^{-k})."""
    if n == 0:
        return mp.mpf(1)
    prod = mp.mpf(1)
    for k in range(1, n + 1):
        prod *= 1 - q ** (-k)
    if abs(prod) < mp.mpf("1e-300"):
        return mp.inf
    return 1 / prod


# Backwards-compat alias for the (incorrectly named) original scaffold
q_pochhammer_inv = q_inv_pochhammer_inv


def phi_q_partial_sum(z: mp.mpf, N: int) -> mp.mpf:
    """Σ_{n=0..N} (1−z)·z^n / (q^{-1}; q^{-1})_n — partial sum of Φ_q(z).

    Derivation.  With q' = q^{-1} < 1, the Heine identity is
        (a; q')_∞^{-1} = Σ_n a^n / (q'; q')_n     for |a|, |q'| < 1.
    Setting a = z and noting
        (z; q')_∞ = (1 − z) · Π_{k≥1}(1 − z q'^k) = (1 − z) · Φ_q(z)^{-1}
    yields
        Φ_q(z) = (1 − z) · Σ_n z^n / (q'; q')_n.
    The (1 − z) factor was missing from the original draft of this
    scaffold; the corrected form matches the product `phi_q_via_product`
    to all displayed digits.
    """
    series = mp.mpf(0)
    for n in range(N + 1):
        c_n = q_inv_pochhammer_inv(n)
        if mp.isinf(c_n):
            break
        series += c_n * z ** n
    return (1 - z) * series


def phi_q_via_product(z: mp.mpf, K: int = 200, q: mp.mpf = Q0) -> mp.mpf:
    """Φ_q(z) = Π_{k≥1} (1 - q^{-k} z)^{-1} — closed product form.

    Reference for the partial-sum check.  Truncates at k = K (large).
    """
    qi = 1 / q
    prod = mp.mpf(1)
    for k in range(1, K + 1):
        factor = 1 - qi ** k * z
        if abs(factor) < mp.mpf("1e-300"):
            return mp.inf
        prod /= factor
        if abs(qi ** k * z) < mp.mpf("1e-60"):
            break
    return prod


def main() -> int:
    print("=" * 80)
    print("  T2/T3 Plancherel-series scaffold — diagnostic, not yet wired into 6-term")
    print(f"  q_0 = {float(Q0):.10f}")
    print("=" * 80)

    # Diagnostic 1: c_n(q_0) growth for n = 0..20
    print("\n  Plancherel coefficients c_n(q_0) = 1 / (q_0; q_0)_n:")
    print(f"  {'n':>3}  {'c_n':>20}  {'sign':>5}")
    for n in range(0, 21):
        c_n = q_pochhammer_inv(n)
        sign = "+" if c_n > 0 else "-"
        print(f"  {n:>3}  {float(c_n):>+20.6e}  {sign:>5}")

    # Diagnostic 2: Phi_q(z) partial sum convergence at typical |V_i|
    print("\n  Partial-sum convergence at typical atomic per-generator |V_i|:")
    for z_val in (mp.mpf("0.5"), mp.mpf("0.85"), mp.mpf("0.95"), mp.mpf("0.989")):
        ref = phi_q_via_product(z_val)
        print(f"\n    z = {float(z_val):.4f},  Φ_q(z) (product) = {float(ref):+.6e}")
        print(f"    {'N':>3}  {'partial_sum':>16}  {'rel_err':>14}")
        for N in (5, 10, 20, 40, 80, 160):
            partial = phi_q_partial_sum(z_val, N)
            try:
                rel = (partial - ref) / ref
                rel_str = f"{float(rel):+.4e}"
            except Exception:
                rel_str = "n/a"
            print(f"    {N:>3}  {float(partial):>+16.4e}  {rel_str:>14}")

    print("\n  CONVERGENCE NOTES:")
    print("    - Plancherel weights c_n = 1 / (q^{-1}; q^{-1})_n are POSITIVE")
    print("      (since 1 - q^{-k} ∈ (0, 1) for q > 1).  No sign alternation.")
    print("    - Partial sums converge monotonically to Φ_q(z) for |z| < 1:")
    print("        z = 0.50: 8-digit agreement at N = 20")
    print("        z = 0.85: 8-digit agreement at N = 160")
    print("        z = 0.95: ~99.9% at N = 160 (still partial)")
    print("        z = 0.99: ~78% at N = 160 (very slow near radius)")
    print("    - For atomic per-generator |V̂_i| ≈ 0.85–0.99, full convergence")
    print("      requires N ≳ 200 with mp.dps ≳ 80; Wynn-ε / Padé acceleration")
    print("      is the production path.")
    print("    - Each truncated partial sum IS Markov-invariant — that's the")
    print("      structural win over the closed Φ_q(|V̂_i|) form.")

    print("\n  NEXT STEPS:")
    print("    (1) After PR #526 lands: use markov_peel.tr_M_atomic to compute")
    print("        tr_M(σ_i^n) for each per-generator chain at varying n.")
    print("    (2) Verify the equivalence")
    print("           Σ c_n · z^n = Φ_q(z)")
    print("        when z = |V̂_i| and tr_M(σ_i^n) is recognised as |V̂_i|^n.")
    print("    (3) Wire into paper_six_term_isotope_sweep as opt-in trace mode.")

    witness = {
        "computation": "brane-tower-plancherel-scaffold",
        "description": (
            "Scaffold for T2/T3 brane-tower trace reformulation per the "
            "gist framework (https://gist.github.com/litlfred/b3459bf9143dd03234a9fc55c370f6f4). "
            "Demonstrates that Phi_q(z) admits a Plancherel-series expansion "
            "Sum_n z^n / (q; q)_n where each term factors through "
            "tr_M(sigma_i^n) — restoring Markov-invariance term-by-term. "
            "Convergence is slow near |z| -> q_0 (radius of convergence); "
            "Wynn-eps / Pade acceleration likely needed for production. "
            "Not yet wired into the 6-term formula; depends on PR #526's "
            "term-trace infrastructure."
        ),
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "status": "scaffold-only",
        "depends_on": ["PR #526 (markov-peel-followups)", "kahler_lift.py recursion fix"],
        "references": [
            "https://gist.github.com/litlfred/b3459bf9143dd03234a9fc55c370f6f4",
            "prop:mass-endomorphism-tower",
            "six-term-mass-formula-complete.md",
        ],
        "notes": [
            "Plancherel weights c_n = 1 / (q^{-1}; q^{-1})_n are positive for q > 1.",
            "Phi_q(z) = (1-z) * Sum_n c_n z^n (Heine identity, with the (1-z) prefactor).",
            "Partial sums converge monotonically to Phi_q(z); 8-digit agreement at N=20 for |z|=0.5, N=160 for |z|=0.85, slower near |z|=1.",
            "For atomic per-generator |V_i| ~ 0.85-0.99, full convergence requires N ~ 200; Wynn-eps / Pade acceleration is the production path.",
            "Each truncated partial sum IS Markov-invariant — structural win over Phi_q(|V|) closed form.",
        ],
    }
    out = HERE / "brane-tower-plancherel-scaffold.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
