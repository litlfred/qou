#!/usr/bin/env python3
# polynomial_q_not_applicable: consumes pre-computed numerical
# per-partition caches at q_0 (50 dps); no q-polynomial arithmetic.
"""Split tr_M and the categorical binding sum into the two-row stratum
and its DISCARDED complement, for D / T / ³He / ⁴He.

WHY
---
`def:two-row-stratum` L22: *"Partitions with ℓ(λ) > 2 map to zero. They
correspond to higher-rank symmetry components absent from the SU(2)
spin-pairing observable."*  Combined with the Schur–Weyl row cap
(`dim V_λ = 0` when `ℓ(λ) > N`) and `dim V = 2` (Descartes), this makes

    N = 2  ⟺  ℓ(λ) ≤ 2  ⟺  pairwise-only  ⟺  the proved ρ_A ≤ C(A,2) cap.

So the missing super-pairwise extensive binding term is not absent from
the theory — it is the explicitly discarded complement
`(1 − π_2row)·tr_M`.  This probe MEASURES that complement.

TWO DIFFERENT SUMS (do not conflate)
------------------------------------
  (a) Markov trace     tr_M      = Σ_λ y_λ χ^λ
  (b) binding sum      B/m_e     = |Σ_λ y_λ χ^λ Δ_λ|,  Δ_λ = (−1)^{n(λ)}·f^λ

`prop:he4-two-row-dominance` is about (a).  Binding is (b).  The
question that matters for the missing magnitude is (b).

Δ_λ = (−1)^{n(λ)}·dim V_λ is the PROVED value (sorry-free, general-n,
`QOU.BraidsAndKnots.dtEuler_eq_deltaLambda_unconditional`), with
n(λ) = Σ(i−1)λᵢ and dim V_λ = f^λ the hook-length / SYT count.

INPUT   committed `chi-<atom>-h<n>-at-q0-50dps.witness.json`
        (`by_partition`: partition, y_lambda, chi_lambda, contribution)
OUTPUT  `two-row-vs-higher-row-binding-split.witness.json`

PRECISION  stdlib `decimal` at 60 dps against 50-dps inputs.  No float64
anywhere (repo NO-FLOAT64 rule).  Audit-only; nothing wired.
"""
from __future__ import annotations

import json
import sys
from decimal import Decimal, getcontext
from math import factorial
from pathlib import Path

# The provenance stamp at the end of main() does
# `from qou_substrate.witness import WitnessBuilder`, which lives at
# tools/qou-substrate/python and is not on the default path. Without this the
# script computed everything and then died on its very last line with
# ModuleNotFoundError, so its witness could never be regenerated — which is
# why it still carried grouped-era values long after the 2026-09-05 ordering
# ruling (bean qou-4383).
sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge  # noqa: E402, F401
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION, AME_B_HE3_MEV_VALIDATION, AME_B_HE4_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION  # noqa: E402  (AME registry)
from mpmath import nstr as _ame_nstr  # noqa: E402  (AME registry, string form)

getcontext().prec = 60

HERE = Path(__file__).resolve().parent

# CODATA electron mass (MeV) and AME2020 binding energies (MeV), as
# decimal strings — validation targets only, never fitted to.
M_E_MEV = Decimal("0.51099895069")
AME_B = {
    "deuteron":  Decimal(_ame_nstr(AME_B_DEUTERON_MEV_VALIDATION, 30)),
    "tritium":   Decimal(_ame_nstr(AME_B_TRITIUM_MEV_VALIDATION, 30)),
    "helium-3":  Decimal(_ame_nstr(AME_B_HE3_MEV_VALIDATION, 30)),
    "helium-4":  Decimal(_ame_nstr(AME_B_HE4_MEV_VALIDATION, 30)),
}
WITNESS = {
    "deuteron":  "chi-deuteron-h6-at-q0-50dps.witness.json",
    "tritium":   "chi-tritium-h9-at-q0-50dps.witness.json",
    "helium-3":  "chi-helium-3-h9-at-q0-50dps.witness.json",
    "helium-4":  "chi-helium-4-h12-at-q0-50dps.witness.json",
}


def hook_length_dim(lam: list[int]) -> int:
    """f^λ = n!/Π hooks — the number of standard Young tableaux."""
    n = sum(lam)
    conj = [sum(1 for p in lam if p > j) for j in range(lam[0])]
    prod = 1
    for i, row in enumerate(lam):
        for j in range(row):
            prod *= row - j + conj[j] - i - 1
    return factorial(n) // prod


def n_of_lambda(lam: list[int]) -> int:
    """n(λ) = Σ (i−1)·λ_i — the jet-order valuation."""
    return sum(i * p for i, p in enumerate(lam))


def _selftest() -> None:
    """Guard the two combinatorial helpers before trusting any number."""
    assert hook_length_dim([3]) == 1 and hook_length_dim([1, 1, 1]) == 1
    assert hook_length_dim([2, 1]) == 2
    for n in (4, 5, 6):
        parts = list(_partitions(n))
        assert sum(hook_length_dim(p) ** 2 for p in parts) == factorial(n), n
    assert n_of_lambda([2, 1]) == 1 and n_of_lambda([1, 1, 1]) == 3


def _partitions(n: int, cap: int | None = None):
    cap = n if cap is None else cap
    if n == 0:
        yield []
        return
    for k in range(min(n, cap), 0, -1):
        for rest in _partitions(n - k, k):
            yield [k] + rest


def analyse(atom: str) -> dict:
    w = json.loads((HERE / WITNESS[atom]).read_text())
    rows = w["by_partition"]

    tr_lo = tr_hi = Decimal(0)     # tr_M   : two-row / ≥3-row
    bd_lo = bd_hi = Decimal(0)     # binding: two-row / ≥3-row

    for r in rows:
        lam = list(r["partition"])
        c = Decimal(r["contribution"])              # = y_λ · χ^λ
        delta = Decimal((-1) ** n_of_lambda(lam) * hook_length_dim(lam))
        if len(lam) <= 2:
            tr_lo += c
            bd_lo += c * delta
        else:
            tr_hi += c
            bd_hi += c * delta

    tr_tot, bd_tot = tr_lo + tr_hi, bd_lo + bd_hi
    B_ame = AME_B[atom]

    def frac(x, tot):
        return x / tot if tot != 0 else Decimal(0)

    return {
        "atom": atom,
        "n_strands": w["n_strands"],
        "n_partitions": len(rows),
        # --- (a) Markov trace split ---
        "tr_M_total": str(tr_tot),
        "tr_M_two_row": str(tr_lo),
        "tr_M_higher_row": str(tr_hi),
        "tr_M_two_row_fraction": str(abs(frac(tr_lo, tr_tot))),
        "tr_M_discarded_fraction": str(abs(frac(tr_hi, tr_tot))),
        # --- (b) binding-sum split (the one that matters) ---
        "binding_sum_total": str(bd_tot),
        "binding_sum_two_row": str(bd_lo),
        "binding_sum_higher_row": str(bd_hi),
        "binding_sum_discarded_fraction": str(abs(frac(bd_hi, bd_tot))),
        # --- against AME ---
        "B_two_row_MeV": str(M_E_MEV * abs(bd_lo)),
        "B_full_MeV": str(M_E_MEV * abs(bd_tot)),
        "B_AME_MeV": str(B_ame),
        "deficit_ratio_two_row": str(B_ame / (M_E_MEV * abs(bd_lo)))
        if bd_lo != 0 else None,
        "deficit_ratio_full": str(B_ame / (M_E_MEV * abs(bd_tot)))
        if bd_tot != 0 else None,
    }


def main() -> None:
    _selftest()
    results = [analyse(a) for a in ("deuteron", "tritium", "helium-3", "helium-4")]

    print(f"{'atom':10} {'trM disc%':>10} {'bind disc%':>11} "
          f"{'B_2row':>9} {'B_full':>9} {'B_AME':>9} "
          f"{'defic_2row':>11} {'defic_full':>11}")
    for r in results:
        print(f"{r['atom']:10} "
              f"{Decimal(r['tr_M_discarded_fraction'])*100:10.3f} "
              f"{Decimal(r['binding_sum_discarded_fraction'])*100:11.3f} "
              f"{Decimal(r['B_two_row_MeV']):9.4f} "
              f"{Decimal(r['B_full_MeV']):9.4f} "
              f"{Decimal(r['B_AME_MeV']):9.4f} "
              f"{Decimal(r['deficit_ratio_two_row'] or 0):11.4f} "
              f"{Decimal(r['deficit_ratio_full'] or 0):11.4f}")

    out = {
        "computation": "two-row-vs-higher-row-binding-split",
        "description": (
            "Splits tr_M and the categorical binding sum "
            "Sigma_lambda y_lambda chi^lambda Delta_lambda into the two-row "
            "stratum (ell(lambda)<=2, the SU(2)/N=2 Schur-Weyl image that "
            "def:two-row-stratum keeps) and the DISCARDED complement "
            "(ell(lambda)>2, which that block maps to zero). Tests whether "
            "the discarded >=3-row sector -- the only irreducibly "
            ">=3-body part of the trace, and the sector the proved "
            "pairwise cap rho_A <= C(A,2) is the shadow of -- supplies the "
            "missing super-pairwise binding magnitude. Audit-only; no fit, "
            "nothing wired to production."
        ),
        "free_parameters": 0,
        "precision": {"engine": "python-decimal", "prec_dps": 60,
                      "input_dps": 50, "float64_used": False},
        "delta_lambda": "(-1)^{n(lambda)} * f^lambda (PROVED, sorry-free, "
                        "QOU.BraidsAndKnots.dtEuler_eq_deltaLambda_unconditional)",
        "results": results,
    }
    p = HERE / "two-row-vs-higher-row-binding-split.witness.json"
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
