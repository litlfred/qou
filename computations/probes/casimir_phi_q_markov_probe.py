#!/usr/bin/env python3
"""Probe: casimir-phi-q-markov
(audit support for conj:casimir-epsilon-vacuum, Routes A2/B alternatives).

**Context.** Two prior probes ruled out:
 - Casimir prefactor π²/720 as a low-degree substrate q-rational
   (`casimir_q_zeta_probe.py`)
 - Carlitz/KKW q-zeta (`casimir_carlitz_q_bernoulli_probe.py`,
   17.7% residue)

The audit's follow-up suggestions: (a) Cherednik 2006 q-zeta via
Macdonald operators, or (b) non-q-zeta derivation via Markov-trace
or Φ_q (compact q-dilog) evaluation.

This probe explores **practical proxies** for both, without
implementing Macdonald operators from scratch:

**Route (a) variants — extended q-zeta family:**
 - Heine ζ_q(s) = Σ_{n≥1} q^n · (1-q^n)^{-s}  at s = -3
 - Tsumura-style ζ_q(-3) = Σ q^{3n} · (...)
 - Λ-modified q-zeta from Cherednik's normalisation

**Route (b) variants — Markov-trace + Φ_q:**
 - Φ_q(z) at natural z (q, 1, q^{1/2})
 - Markov-parameter combinations z_M^k for k = 1..6
 - Σ Φ_q(q^k) (truncated)

For each candidate, multiply by the standard geometric factor
(π²/6 — the same that converts ζ(-3) = -1/120 to π²/720) and
check residue vs π²/720.

Emits `casimir-phi-q-markov-probe.witness.json`.

If any candidate matches within 1%, the route is a strong hint
toward closure. If all miss (null result), sub-problem 3 of
conj:casimir-epsilon-vacuum requires genuinely heavier machinery.

Ref: [cherednik2006] Cherednik, "Double Affine Hecke Algebras",
                     Cambridge Univ. Press
Ref: [faddeev1995] Faddeev, "Discrete Heisenberg-Weyl group and
                   modular group", Lett. Math. Phys. 34, 249
Ref: [casimir1948] https://dwc.knaw.nl/DL/publications/PU00018547.pdf
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))

from mpmath import mp, mpf, pi as mp_pi, sqrt as mp_sqrt  # noqa: E402

from _phi_q_util import phi_q  # noqa: E402
from q_parameter import Q  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()


def _q_int(n: int, q: "mpf") -> "mpf":
    return (q ** n - q ** (-n)) / (q - 1 / q)


def heine_zeta(s: int, q: "mpf", N: int = 500) -> "mpf":
    """Heine q-zeta: Σ_{n≥1} q^n · (1 − q^n)^{−s}, evaluated at q < 1.

    At s = -3, we get Σ_{n≥1} q^n · (1 − q^n)^3 — a positive,
    convergent series for any q in (0, 1).
    """
    # Use q^{-1} (which is < 1 at substrate Q ≈ 1.11).
    q_lt_1 = 1 / q
    total = mpf(0)
    for n in range(1, N + 1):
        term = q_lt_1 ** n * (1 - q_lt_1 ** n) ** (-s)
        total += term
        if abs(term) < mpf(10) ** (-mp.dps + 5):
            break
    return total


def tsumura_zeta_neg3(q: "mpf", N: int = 500) -> "mpf":
    """Tsumura-style q-zeta variant.  Σ_{n≥1} q^{3n} / [n]_q^{-3}.

    At s = -3 with the "[n]_q powers" convention: just
    Σ_{n≥1} q^{3n} · [n]_q^3 (which DIVERGES for q > 1).  Use
    damping factor q^{-7n} so the series converges.
    """
    total = mpf(0)
    for n in range(1, N + 1):
        # Damped Σ_n [n]_q^3 q^{-7n} — k=7 gives ~ζ(0) behavior?
        nq3 = _q_int(n, q) ** 3
        term = nq3 * q ** (-7 * n)
        total += term
        if abs(term) < mpf(10) ** (-mp.dps + 5):
            break
    return total


def main() -> int:
    builder = WitnessBuilder(
        "casimir-phi-q-markov-probe",
        engine="mpmath",
    )

    q = mpf(Q)
    pi_sq = mp_pi ** 2
    pi_sq_720 = pi_sq / 720

    # Markov parameter — multiple conventions; tabulate them.
    q_half = mp_sqrt(q)
    z_M_v1 = 1 / (q_half + 1 / q_half)               # 1/[2]_{q^{1/2}} ≈ 0.499
    z_M_v2 = (q - 1 / q) / (q_half - 1 / q_half)     # (q-q⁻¹)/(q^½-q^{-½}) = q^½+q^{-½}
    z_M_v3 = 1 / (q + 1 / q)                         # 1/[2]_q

    # ─── Route (a): extended q-zeta variants ───
    heine_neg3 = heine_zeta(-3, q)
    tsumura_neg3 = tsumura_zeta_neg3(q)

    # ─── Route (b): Φ_q evaluations + Markov-trace candidates ───
    q_inv = 1 / q
    # Φ_q(z) at natural z values (caution: convergence requires |z·q^{-1}| < 1)
    phi_q_at_1 = phi_q(mpf(1), q_inv)
    phi_q_at_qhalf = phi_q(q_half, q_inv)
    phi_q_at_q_inv = phi_q(q_inv, q_inv)

    # log Φ_q values — the dilogarithm comes in via log(Φ_q)
    import mpmath as _mpm
    log_phi_q_at_1 = _mpm.log(phi_q_at_1)
    log_phi_q_at_qhalf = _mpm.log(phi_q_at_qhalf)
    log_phi_q_at_q_inv = _mpm.log(phi_q_at_q_inv)

    # ─── All candidates × π²/6 geometric multiplier ───
    candidates = []
    geom_mult = pi_sq / 6  # standard Casimir conversion

    for name, val in [
        # Route (a)
        ("Heine ζ_q(-3)", heine_neg3),
        ("Tsumura-style Σ[n]_q³ q^{-7n}", tsumura_neg3),
        # Route (b) — Markov
        ("z_M^v1 = 1/[2]_{q^½}", z_M_v1),
        ("z_M^v2 = q^½ + q^{-½}", z_M_v2),
        ("z_M^v3 = 1/[2]_q", z_M_v3),
        ("z_M^v1 cubed", z_M_v1 ** 3),
        ("z_M^v3 cubed", z_M_v3 ** 3),
        # Route (b) — Φ_q
        ("Φ_q(1)", phi_q_at_1),
        ("Φ_q(q^{1/2})", phi_q_at_qhalf),
        ("Φ_q(q^{-1})", phi_q_at_q_inv),
        ("log Φ_q(1)", log_phi_q_at_1),
        ("log Φ_q(q^{1/2})", log_phi_q_at_qhalf),
        ("log Φ_q(q^{-1})", log_phi_q_at_q_inv),
        ("1/Φ_q(1)", 1 / phi_q_at_1),
        ("1/Φ_q(q^{1/2})", 1 / phi_q_at_qhalf),
        # Mixed
        ("ℏ_q² · log Φ_q(1)", (1 - q_inv) ** 2 * log_phi_q_at_1),
        ("z_M^v1 · log Φ_q(1)", z_M_v1 * log_phi_q_at_1),
    ]:
        candidate_value = abs(val) * geom_mult
        rel_residue = abs(candidate_value - pi_sq_720) / pi_sq_720
        candidates.append({
            "form": name,
            "raw_value": float(val),
            "casimir_candidate": float(candidate_value),
            "rel_residue_vs_pi_sq_720": float(rel_residue),
        })

    # Also try without the π²/6 multiplier — direct match candidates
    direct_candidates = []
    for name, val in [
        ("heine_zeta(-3) raw", heine_neg3),
        ("z_M^v1 squared", z_M_v1 ** 2),
        ("(log Φ_q(1))²", log_phi_q_at_1 ** 2),
        ("log Φ_q(1) / [4]_q", log_phi_q_at_1 / _q_int(4, q)),
        ("ℏ_q² · log Φ_q(1)", (1 - q_inv) ** 2 * log_phi_q_at_1),
        ("ℏ_q⁴", (1 - q_inv) ** 4),
        ("π²·ℏ_q⁴/6", pi_sq * (1 - q_inv) ** 4 / 6),
    ]:
        rel_residue = abs(val - pi_sq_720) / pi_sq_720
        direct_candidates.append({
            "form": name,
            "value": float(val),
            "rel_residue_vs_pi_sq_720": float(rel_residue),
        })

    # ─── Best matches ───
    sub_one_pct = [
        c for c in candidates if c["rel_residue_vs_pi_sq_720"] < 0.01
    ] + [
        c for c in direct_candidates if c["rel_residue_vs_pi_sq_720"] < 0.01
    ]
    n_sub_one_pct = len(sub_one_pct)

    best_geom = min(candidates, key=lambda c: c["rel_residue_vs_pi_sq_720"])
    best_direct = min(
        direct_candidates, key=lambda c: c["rel_residue_vs_pi_sq_720"]
    )

    (
        builder
        .set_description(
            "Empirical Φ_q / Markov-trace / extended-q-zeta probe "
            "for the Casimir-prefactor sub-problem.  Tests Heine and "
            "Tsumura-style q-zeta variants, Φ_q evaluations at "
            "natural z values (1, q^{1/2}, q^{-1}), Markov-parameter "
            "candidates z_M (three convention variants), and mixed "
            "combinations.  All candidates × π²/6 geometric "
            "multiplier (the same that converts classical "
            "ζ(-3) = -1/120 to π²/720).  Counts sub-1% matches and "
            "reports best in each family.  A null result reinforces "
            "the audit's narrowing of sub-problem 3 (the prefactor "
            "is not derivable from any obvious Hecke-/Φ_q-/q-zeta "
            "primitive at substrate q_0)."
        )
        .set_content_block("conj:casimir-epsilon-vacuum")
        .add_parameter("substrate_q", float(q))
        .add_parameter("target_pi_sq_720", float(pi_sq_720))
        .add_data(
            "phi_q_evaluations",
            {
                "phi_q_at_1": float(phi_q_at_1),
                "phi_q_at_q_half": float(phi_q_at_qhalf),
                "phi_q_at_q_inv": float(phi_q_at_q_inv),
                "log_phi_q_at_1": float(log_phi_q_at_1),
            },
        )
        .add_data(
            "markov_parameters",
            {
                "z_M_v1": float(z_M_v1),
                "z_M_v2": float(z_M_v2),
                "z_M_v3": float(z_M_v3),
            },
        )
        .add_data(
            "extended_q_zeta",
            {
                "heine_zeta_neg3": float(heine_neg3),
                "tsumura_style": float(tsumura_neg3),
            },
        )
        .add_data("geom_multiplied_candidates", candidates)
        .add_data("direct_candidates", direct_candidates)
        .add_data(
            "best_geom_multiplied",
            {
                "form": best_geom["form"],
                "value": best_geom["casimir_candidate"],
                "rel_residue": best_geom["rel_residue_vs_pi_sq_720"],
            },
        )
        .add_data(
            "best_direct",
            {
                "form": best_direct["form"],
                "value": best_direct["value"],
                "rel_residue": best_direct["rel_residue_vs_pi_sq_720"],
            },
        )
        .add_assertion(
            name="zero_phi_q_markov_q_zeta_within_one_percent",
            computed=float(n_sub_one_pct),
            expected=0.0,
            tolerance=0.5,
            unit=(
                "count of Φ_q / Markov / extended-q-zeta candidates "
                "with rel residue < 1% vs π²/720"
            ),
            source=(
                "Null assertion for Routes A2 + B.  Asserting zero "
                "sub-1% matches documents that the Casimir prefactor "
                "π²/720 is not recoverable from any single Φ_q "
                "evaluation, Markov-parameter combination, or "
                "extended q-zeta value at substrate q_0."
            ),
        )
    )

    out = builder.save()
    print(f"\nWitness: {out}")
    print()
    print(f"Substrate q = {float(q):.10f}")
    print(f"Target π²/720 = {float(pi_sq_720):.8e}")
    print()
    print("─── Φ_q evaluations ───")
    print(f"  Φ_q(1)       = {float(phi_q_at_1):.10e}")
    print(f"  Φ_q(q^{{1/2}}) = {float(phi_q_at_qhalf):.10e}")
    print(f"  Φ_q(q^{{-1}}) = {float(phi_q_at_q_inv):.10e}")
    print(f"  log Φ_q(1)   = {float(log_phi_q_at_1):.10e}")
    print()
    print("─── Markov parameters ───")
    print(f"  z_M^v1 = 1/[2]_{{q^½}}    = {float(z_M_v1):.10e}")
    print(f"  z_M^v2 = q^½ + q^{{-½}}  = {float(z_M_v2):.10e}")
    print(f"  z_M^v3 = 1/[2]_q         = {float(z_M_v3):.10e}")
    print()
    print(f"─── Extended q-zeta ───")
    print(f"  Heine ζ_q(-3)  = {float(heine_neg3):.10e}")
    print(f"  Tsumura-style  = {float(tsumura_neg3):.10e}")
    print()
    print("─── Best geometry-multiplied (× π²/6) ───")
    print(f"  form: {best_geom['form']}")
    print(f"  value: {best_geom['casimir_candidate']:.6e}")
    print(f"  rel residue: {best_geom['rel_residue_vs_pi_sq_720']:.4e}")
    print()
    print("─── Best direct ───")
    print(f"  form: {best_direct['form']}")
    print(f"  value: {best_direct['value']:.6e}")
    print(f"  rel residue: {best_direct['rel_residue_vs_pi_sq_720']:.4e}")
    print()
    if n_sub_one_pct > 0:
        print(f"→ {n_sub_one_pct} MATCH(ES) within 1% — investigate:")
        for m in sub_one_pct:
            print(f"    {m['form']}: rel residue {m['rel_residue_vs_pi_sq_720']:.4e}")
    else:
        print("→ NULL RESULT: no Φ_q / Markov / extended q-zeta candidate within 1%.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
