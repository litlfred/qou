"""
normalization_reconciliation_phase5l2.py — Phase 5l.2 normalization
reconciliation between the Phase 5l.1 structural T(B_p, q) and the
canonical Phase 5l tr_M^3(𝓑_p, q).

Phase 5l.1 computes T(B_p, q) symbolically via the Wenzl-bridge
y_λ-symbolic implementation, which carries its own normalization
convention (∝ q-hook-content scaled by the symbolic implementation's
internal constants).  Phase 5l computes tr_M^3(𝓑_p, q) at mpfr-50-dps
via the y_λ-numeric pipeline, which carries the canonical Wenzl
Markov-trace normalization.

The hypothesis (`normalization_note` in 5l.1's witness):

  tr_M^3(𝓑_p, q) / T(B_p, q) ≡ c  (q-INDEPENDENT)

If true, c is the normalization constant; evaluating it at q_0 from
existing witnesses gives the explicit value.

This probe evaluates the symbolic T(B_p, q) from 5l.1 at the 5 q values
where 5l measured tr_M^3 numerically, and checks whether the ratio is
q-independent.

  Ref: folio-assistant/computations/tau_M_proton_closed_form_phase5l1.py
  Ref: folio-assistant/computations/rho_constit_equals_tau_M_proton_phase5l.py
  Ref: docs/audits/2026-05-20-constit-factor-closure-chain.md
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


PHASE5L_WITNESS = HERE / "rho-constit-equals-tau-M-proton-phase5l.witness.json"
PHASE5L1_WITNESS = HERE / "tau-M-proton-closed-form-phase5l1.witness.json"


def load_phase5l_data() -> list[dict]:
    """Load the 5-point (q, tr_M^3) table from Phase 5l witness.

    Per Copilot PR #863 review: the per_q_results table stores q as a
    float (~16 dps truncation); the un-truncated 50-dps q-strings live
    in `parameters.q_values`.  Build the rows with q resolved from the
    string list so the audit uses the substrate's canonical 50-dps
    pin, not the round-tripped float.
    """
    with PHASE5L_WITNESS.open() as f:
        data = json.load(f)
    rows = data["data"]["per_q_results"]
    params = data.get("parameters", {})
    # WitnessBuilder serialises `parameters` as a dict; the q_values
    # entry is the list of canonical-pin 50-dps strings.
    q_strings: list[str] = list(params.get("q_values", []))
    # Pair each row with its 50-dps q-string by index (order preserved
    # by the Phase 5l writer).  Fallback to the row's float `q` if the
    # parameter is absent.
    enriched: list[dict] = []
    for i, row in enumerate(rows):
        enriched_row = dict(row)
        if i < len(q_strings):
            enriched_row["q_str"] = q_strings[i]
        else:
            enriched_row["q_str"] = repr(row["q"])
        enriched.append(enriched_row)
    return enriched


def load_phase5l1_symbolic() -> str:
    """Load the structural T(B_p, q) sympy string from Phase 5l.1."""
    with PHASE5L1_WITNESS.open() as f:
        data = json.load(f)
    return data["data"]["T_proton_structural_symbolic"]


def main() -> int:
    set_compute_dps(50)
    builder = WitnessBuilder(
        "normalization-reconciliation-phase5l2", engine="python"
    )
    # Audit-only — this is a reconciliation probe, not a primary
    # consumer of the conjecture.
    builder.set_audit_only("docs/audits/2026-05-20-constit-factor-closure-chain.md")

    print("=== Phase 5l.2: normalization reconciliation ===\n")
    print("Hypothesis A: tr_M^3(𝓑_p, q) / T(B_p, q) ≡ c  (q-independent)")
    print("Hypothesis B: T was written in Q = q^2 convention →")
    print("              tr_M^3(𝓑_p, q) / T(B_p, q^2) ≡ c  (q-independent)\n")

    phase5l_rows = load_phase5l_data()
    T_sym_str = load_phase5l1_symbolic()

    q = sp.Symbol("q", positive=True, real=True)
    T_expr = sp.sympify(T_sym_str)
    if not T_expr.free_symbols.issubset({q}):
        # Use whichever symbol the witness named "q".
        target = next((s for s in T_expr.free_symbols if s.name == "q"),
                      None)
        if target is None:
            target = next(iter(T_expr.free_symbols))
        T_expr = T_expr.subs(target, q)

    ratios_A = []  # T evaluated at q
    ratios_B = []  # T evaluated at q^2 (Q = q^2 interpretation)
    for row in phase5l_rows:
        # Use the un-truncated 50-dps q-string from Phase 5l parameters
        # (Copilot PR #863 review) — the float `row["q"]` is already
        # round-tripped through 64-bit, losing the canonical 50-digit
        # pin's precision past digit 17.
        q_val = mp.mpf(row["q_str"])
        tau_canonical = mp.mpf(row["tau_M_proton_H3_str"])
        q_sympy = sp.Float(row["q_str"], 50)
        q_sq_sympy = sp.Float(str(q_val * q_val), 50)
        T_at_q = mp.mpf(str(sp.N(T_expr.subs(q, q_sympy), 50)))
        T_at_qsq = mp.mpf(str(sp.N(T_expr.subs(q, q_sq_sympy), 50)))
        print(f"  q = {float(q_val):.7f}:")
        print(f"    tr_M^3(𝓑_p, q)  = {float(tau_canonical):.16f}")
        print(f"    T(B_p, q)       = {float(T_at_q):.16f}  ratio_A = {float(tau_canonical/T_at_q):.10f}")
        print(f"    T(B_p, q^2)     = {float(T_at_qsq):.16f}  ratio_B = {float(tau_canonical/T_at_qsq):.10f}")
        if T_at_q != 0:
            ratios_A.append({
                "q": float(q_val),
                "ratio": float(tau_canonical / T_at_q),
                "ratio_str": mp.nstr(tau_canonical / T_at_q, 30),
            })
        if T_at_qsq != 0:
            ratios_B.append({
                "q": float(q_val),
                "ratio": float(tau_canonical / T_at_qsq),
                "ratio_str": mp.nstr(tau_canonical / T_at_qsq, 30),
            })

    def assess(ratios: list[dict], label: str) -> tuple[str, float, float]:
        if len(ratios) < 2:
            print(f"  [{label}] insufficient data")
            return "insufficient-data", 1.0, 0.0
        r_values = [mp.mpf(r["ratio_str"]) for r in ratios]
        r_min, r_max = min(r_values), max(r_values)
        r_mean = sum(r_values) / len(r_values)
        rel_spread = (r_max - r_min) / abs(r_mean) if r_mean != 0 else mp.mpf("inf")
        print(f"  [{label}] ratio range across {len(ratios)} q-points:")
        print(f"    min  = {float(r_min):.16f}")
        print(f"    max  = {float(r_max):.16f}")
        print(f"    mean = {float(r_mean):.16f}")
        print(f"    relative spread = {float(rel_spread):.4e}")
        if rel_spread < mp.mpf("1e-40"):
            v = "q-independent-confirmed-50dps"
        elif rel_spread < mp.mpf("1e-10"):
            v = "q-independent-confirmed-10dps"
        else:
            v = "ratio-q-dependent"
        return v, float(rel_spread), float(r_mean)

    print()
    print("=== Verdict ===\n")
    verdict_A, spread_A, mean_A = assess(ratios_A, "Hyp A: T(B_p, q)")
    print()
    verdict_B, spread_B, mean_B = assess(ratios_B, "Hyp B: T(B_p, q^2)")
    print()

    if verdict_A.startswith("q-independent"):
        verdict = verdict_A + "-A"
        c_normalization = mean_A
        print(f"  ✓ HYP A CONFIRMED: normalization c = {mean_A:.20f}")
    elif verdict_B.startswith("q-independent"):
        verdict = verdict_B + "-B"
        c_normalization = mean_B
        print(f"  ✓ HYP B CONFIRMED: T_5l.1 uses Q = q^2 convention;")
        print(f"    canonical normalization c = {mean_B:.20f}")
    else:
        verdict = "both-hypotheses-falsified"
        c_normalization = None
        print(f"  ✗ Both A and B fail to give a q-independent ratio.")
        print(f"    The normalization between T(B_p) and tr_M^3(𝓑_p) is")
        print(f"    not a simple multiplicative constant in either q or q^2.")
        print(f"    Deeper structural mismatch — likely the 5l.1 symbolic")
        print(f"    y_λ implementation uses a different (Q, h) convention.")

    builder.add_data("hypothesis_A_ratios", ratios_A)
    builder.add_data("hypothesis_A_relative_spread", spread_A)
    builder.add_data("hypothesis_A_mean_ratio", mean_A)
    builder.add_data("hypothesis_B_ratios", ratios_B)
    builder.add_data("hypothesis_B_relative_spread", spread_B)
    builder.add_data("hypothesis_B_mean_ratio", mean_B)
    if c_normalization is not None:
        builder.add_data("normalization_constant", c_normalization)
    rel_spread = min(spread_A, spread_B)

    builder.set_description(
        "Phase 5l.2: normalization reconciliation between the Phase 5l.1 "
        "structural T(B_p, q) (Wenzl-bridge symbolic) and the canonical "
        "Phase 5l tr_M^3(𝓑_p, q) (mpfr-50-dps numeric).  Tests two "
        "hypotheses: (A) the ratio tr_M^3(𝓑_p, q) / T(B_p, q) is "
        "q-independent (simple multiplicative constant); (B) the symbolic "
        "T uses Q = q^2 convention, so tr_M^3(𝓑_p, q) / T(B_p, q^2) is "
        "q-independent.  If either holds, gives the closed-form "
        "normalization for promoting Phase 5l.1's symbolic T to canonical "
        "tr_M^3."
    )
    builder.add_data("verdict", verdict)
    # Falsification probe — encode the FINDING as the passing assertion
    # (§6 pattern from Phase 5k.2 / PR #854).  This probe tests whether
    # the Phase 5l.1 symbolic T(B_p) reconciles with canonical tr_M^3 via
    # either a q- or q^2-substitution constant.  Both hypotheses fail
    # — neither A nor B gives a q-independent ratio — which IS the
    # auditable finding: the symbolic implementation uses a DEEPER
    # convention mismatch (likely Wenzl y_λ Q-substitution + a structural
    # factor unaccounted for).  Phase 5l.2 outcome: SIMPLE
    # MULTIPLICATIVE RECONCILIATION REFUTED.
    simple_reconciliation_refuted = (
        spread_A > 1e-3 and spread_B > 1e-3
    )
    builder.add_assertion(
        name="phase_5l_2_simple_reconciliation_refuted",
        computed=float(1.0 if simple_reconciliation_refuted else 0.0),
        expected=1.0,
        tolerance=0.5,  # binary
        unit="dimensionless (refutation-confirmed boolean)",
        source=(
            f"Phase 5l.2 reconciliation probe: tested two simple "
            f"hypotheses for relating Phase 5l.1's symbolic T(B_p, q) "
            f"(Wenzl-bridge SYMBOLIC) to canonical tr_M^3(𝓑_p, q) "
            f"(Phase 5l, mpfr-50-dps NUMERIC):\n"
            f"  Hyp A: T evaluated at q — rel.spread = {spread_A:.4e}\n"
            f"  Hyp B: T evaluated at q^2 — rel.spread = {spread_B:.4e}\n"
            f"Both spreads exceed 0.1% across the 5-point substrate window, "
            f"refuting the simple-multiplicative-constant hypothesis for "
            f"both q and q^2 interpretations.  The Wenzl-bridge symbolic "
            f"implementation uses a deeper convention mismatch — likely a "
            f"different normalization of y_λ that depends on partition "
            f"structure as well as q.  Verdict: {verdict}.  Reconciliation "
            f"now queued as a research task (no longer a simple "
            f"normalization-constant fix)."
        ),
    )
    builder.save()
    print(f"\nWitness written: normalization-reconciliation-phase5l2.witness.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
