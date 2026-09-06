#!/usr/bin/env python3
# polynomial_q_not_applicable: consumes pre-computed numerical
# per-partition caches at q_0 (50 dps); no q-polynomial arithmetic.
"""Stratify the categorical binding sum by row-length ℓ(λ), and measure
cancellation, for D / T / ³He / ⁴He.

WHY
---
`two_row_vs_higher_row_binding_split.py` found the binding sum is ≥3-row
*dominated* (26 % at D → 100 % at ⁴He) and that including the ≥3-row
sector does **not** close the magnitude (deficit spread 3.29–9.31,
worst at ⁴He).  Two follow-on questions the same cached data answers
with zero free parameters:

  Q1  **Is the magnitude present but cancelling?**  Compare the ℓ¹ norm
      `Σ_λ |y_λ χ^λ Δ_λ|` against the AME target.  If ℓ¹ ≥ target the
      magnitude EXISTS in the terms and the problem is signs/phases; if
      ℓ¹ < target the magnitude is genuinely absent and no re-signing
      can help.  (Cross-check: the corpus ℓ¹-ceiling prune reports
      ‖c‖₁/|target| = {D 0.52, T 0.36, ³He 0.59, ⁴He 0.41} — this probe
      recomputes those four independently.)

  Q2  **Where does the ℓ¹ mass sit?**  Per-stratum ℓ(λ) = 1,2,3,…
      signed sum and ℓ¹ norm, with the per-stratum cancellation ratio
      `|Σ| / Σ|·|`.  Near-total cancellation inside a stratum is a
      selection-rule signature, not a small-signal one — ⁴He's two-row
      sector sums to 0.0007 MeV, which is such a case.

Δ_λ = (−1)^{n(λ)}·f^λ is the PROVED value (sorry-free, general-n,
`QOU.BraidsAndKnots.dtEuler_eq_deltaLambda_unconditional`).

INPUT   committed `chi-<atom>-h<n>-at-q0-50dps.witness.json`
OUTPUT  `binding-row-length-stratification.witness.json`

PRECISION  stdlib `decimal` at 60 dps against 50-dps inputs.  No float64
(repo NO-FLOAT64 rule).  `free_parameters = 0`.  Audit-only; nothing wired.
"""
from __future__ import annotations

import json
from decimal import Decimal, getcontext
from math import factorial
from pathlib import Path

getcontext().prec = 60

HERE = Path(__file__).resolve().parent

# The AME table below is READ from the vendored evaluation, not typed. It used
# to be four Decimal literals and every one had drifted (bean qou-zv46):
# deuteron -0.2 eV, tritium +24.8 eV (the typo PR #1105 named), helium-3
# +1.9 eV, helium-4 +10.6 eV.
#
# mpmath appears here ONLY to read the registry and render the value as the
# decimal string AME itself quotes; all arithmetic in this module stays
# Decimal at prec 60, which is what its NO-FLOAT64 note is about.
import sys as _sys  # noqa: E402
_sys.path.insert(0, str(Path(__file__).resolve().parent / "substrate"))
import mpmath as _mp  # noqa: E402
from codata_constants import ame_binding_mev as _ame_b  # noqa: E402


def _B(Z, A):
    """AME2020 total binding energy (MeV) as Decimal, via the registry."""
    return Decimal(_mp.nstr(_ame_b(Z, A), 12))


M_E_MEV = Decimal("0.51099895069")
AME_B = {
    "deuteron":  _B(1, 2),
    "tritium":   _B(1, 3),
    "helium-3":  _B(2, 3),
    "helium-4":  _B(2, 4),
}
WITNESS = {
    "deuteron":  "chi-deuteron-h6-at-q0-50dps.witness.json",
    "tritium":   "chi-tritium-h9-at-q0-50dps.witness.json",
    "helium-3":  "chi-helium-3-h9-at-q0-50dps.witness.json",
    "helium-4":  "chi-helium-4-h12-at-q0-50dps.witness.json",
}


def hook_length_dim(lam: list[int]) -> int:
    n = sum(lam)
    conj = [sum(1 for p in lam if p > j) for j in range(lam[0])]
    prod = 1
    for i, row in enumerate(lam):
        for j in range(row):
            prod *= row - j + conj[j] - i - 1
    return factorial(n) // prod


def n_of_lambda(lam: list[int]) -> int:
    return sum(i * p for i, p in enumerate(lam))


def _partitions(n: int, cap: int | None = None):
    cap = n if cap is None else cap
    if n == 0:
        yield []
        return
    for k in range(min(n, cap), 0, -1):
        for rest in _partitions(n - k, k):
            yield [k] + rest


def _selftest() -> None:
    assert hook_length_dim([3]) == 1 and hook_length_dim([1, 1, 1]) == 1
    assert hook_length_dim([2, 1]) == 2
    for n in (4, 5, 6):
        assert sum(hook_length_dim(p) ** 2 for p in _partitions(n)) == factorial(n)
    assert n_of_lambda([2, 1]) == 1


def analyse(atom: str) -> dict:
    w = json.loads((HERE / WITNESS[atom]).read_text())
    rows = w["by_partition"]
    B_ame = AME_B[atom]
    target = B_ame / M_E_MEV                       # dimensionless target

    signed: dict[int, Decimal] = {}
    absval: dict[int, Decimal] = {}
    for r in rows:
        lam = list(r["partition"])
        term = Decimal(r["contribution"]) * Decimal(
            (-1) ** n_of_lambda(lam) * hook_length_dim(lam))
        L = len(lam)
        signed[L] = signed.get(L, Decimal(0)) + term
        absval[L] = absval.get(L, Decimal(0)) + abs(term)

    tot_signed = sum(signed.values(), Decimal(0))
    tot_abs = sum(absval.values(), Decimal(0))

    strata = []
    for L in sorted(signed):
        s, a = signed[L], absval[L]
        strata.append({
            "row_length": L,
            "signed_sum": str(s),
            "l1_norm": str(a),
            "l1_share_of_total": str(a / tot_abs) if tot_abs else "0",
            # |sum| / sum|.| : 1 = no cancellation, ~0 = near-total
            "cancellation_ratio": str(abs(s) / a) if a else None,
        })

    return {
        "atom": atom,
        "A": w["Z"] + w["N"],
        "n_strands": w["n_strands"],
        "target_dimensionless": str(target),
        "signed_total": str(tot_signed),
        "l1_total": str(tot_abs),
        # Q1 — the decisive ratio. <1 ⇒ magnitude genuinely absent.
        "l1_over_target": str(tot_abs / target),
        "global_cancellation_ratio": str(abs(tot_signed) / tot_abs) if tot_abs else None,
        "B_full_MeV": str(M_E_MEV * abs(tot_signed)),
        "B_l1_ceiling_MeV": str(M_E_MEV * tot_abs),
        "B_AME_MeV": str(B_ame),
        "strata": strata,
    }


def main() -> None:
    _selftest()
    res = [analyse(a) for a in ("deuteron", "tritium", "helium-3", "helium-4")]

    print("Q1 — is the magnitude present but cancelling?")
    print(f"{'atom':10} {'A':>2} {'l1/target':>10} {'cancel':>8} "
          f"{'B_full':>8} {'B_l1cap':>9} {'B_AME':>9}")
    for r in res:
        print(f"{r['atom']:10} {r['A']:>2} "
              f"{Decimal(r['l1_over_target']):10.4f} "
              f"{Decimal(r['global_cancellation_ratio']):8.4f} "
              f"{Decimal(r['B_full_MeV']):8.4f} "
              f"{Decimal(r['B_l1_ceiling_MeV']):9.4f} "
              f"{Decimal(r['B_AME_MeV']):9.4f}")
    print("\n  corpus l1-ceiling prune reports {D 0.52, T 0.36, He3 0.59, He4 0.41}")
    print("  -> the l1/target column above is the independent recomputation\n")

    print("Q2 — where does the l1 mass sit, and how much cancels?")
    for r in res:
        print(f"\n  {r['atom']} (A={r['A']}, n={r['n_strands']}):")
        print(f"    {'l(lam)':>7} {'l1 share':>10} {'cancel':>8}")
        for s in r["strata"]:
            print(f"    {s['row_length']:>7} "
                  f"{Decimal(s['l1_share_of_total'])*100:9.3f}% "
                  f"{Decimal(s['cancellation_ratio'] or 0):8.5f}")

    out = {
        "computation": "binding-row-length-stratification",
        "description": (
            "Stratifies the categorical binding sum "
            "Sigma_lambda y_lambda chi^lambda Delta_lambda by row length "
            "ell(lambda), for D/T/3He/4He. Q1: compares the l1 norm against "
            "the AME target -- l1 < target means the magnitude is genuinely "
            "absent from the terms and no re-signing can reach it (this "
            "independently recomputes the corpus l1-ceiling prune values). "
            "Q2: per-stratum l1 share and cancellation ratio |sum|/sum|.|, "
            "locating where the magnitude sits and where it self-cancels. "
            "Audit-only; no fit, nothing wired to production."
        ),
        "free_parameters": 0,
        "precision": {"engine": "python-decimal", "prec_dps": 60,
                      "input_dps": 50, "float64_used": False},
        "delta_lambda": "(-1)^{n(lambda)} * f^lambda (PROVED, sorry-free, "
                        "QOU.BraidsAndKnots.dtEuler_eq_deltaLambda_unconditional)",
        "results": res,
    }
    p = HERE / "binding-row-length-stratification.witness.json"
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    out.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        out, script_path=__file__, engine=None, q0_anchor=False)
    p.write_text(json.dumps(out, indent=2) + "\n")
    print(f"\nwrote {p.name}")


if __name__ == "__main__":
    main()
