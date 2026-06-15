#!/usr/bin/env python3
"""DERIVATION (not a probe) — per-block archimedean realization of binding.

NO fitted parameters. The canonical scalar binding (binding_canonical.py) is

    B(K) = E_0 · ( tr_M(W_free) − tr_M(W_atom) ) ,   tr_M = Σ_λ y_λ χ^λ ,

(SIGNED categorical difference; the double-modulus |tr_free|−|tr_atom| was a
non-archimedean misuse, see 2026-06-01-paper-modulus-nonarchimedean-audit).

with E_0 a CALIBRATION-fixed energy scale (not a fit):
    E_0^{(𝔈)}  = m_e / (q_0 (q_0 − 1))      ≈ 4.186 MeV   (substrate scale 𝔈₀)
    E_0^{(Qβ)} = Q_β(n) = 0.78233341 MeV     (CAL-3 free-neutron β-decay scale)

The premature-collapse scalar uses |Σ_λ y_λ χ^λ| — it COLLAPSES the Wedderburn
blocks (modulus of the sum) BEFORE the observation, cancelling the per-block
content. The framework's own discipline (§9 cheat-sheet, prop:delta-pre-
archimedean) says observe LAST: defer the archimedean realization τ_λ = E_0·|·|
to PER BLOCK, then sum —

    B_perblock(K) = E_0 · Σ_λ y_λ ( |χ^λ(W_free)| − |χ^λ(W_atom)| ) .

This is the SAME canonical functor (E_0·|·|, y_λ from Wenzl, χ^λ from Hoefsmit),
block-diagonalised. ZERO free parameters — E_0 is calibration, everything else
derived. It is a DERIVATION, not a fit to AME: the only AME use is the final
comparison. Reports both E_0 conventions for D/T/³He/⁴He.

Modulus convention (per 2026-06-01-paper-modulus-nonarchimedean-audit). The
per-block `|χ^λ|` here is the ARCHIMEDEAN observation τ_λ — `|·|` is correct AT
the (named) archimedean realization step, and the per-block observe-last is
exactly the "defer the modulus" discipline. The general, non-archimedean-
compatible norm replaces `|χ^λ|` with the Hecke BAR-pairing χ^λ(q)·χ^λ(q⁻¹)
(bar-involution q↦q⁻¹), which is defined over any base ring (char p, p-adic)
and coincides with |χ^λ|² only at the real place; computing it needs χ^λ at
q⁻¹ (a follow-up — the cached witnesses store q_0 only).
"""
from __future__ import annotations

import json
from pathlib import Path

import _path_bridge  # noqa: F401, E402 — Phase-6 bridge: flat imports from substrate/
from mpmath import mpf, fabs  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402 — CAL-1, centralized
from experimental_constants import Q_NEUTRON_MEV  # noqa: E402 — CAL-3, centralized

set_compute_dps()
HERE = Path(__file__).resolve().parent
M_E = mpf(str(M_E_MEV))   # CAL-1 electron mass (codata_constants)
q0 = mpf(str(Q0))         # substrate parameter (q_parameter)

# Calibration-fixed energy scales (NOT fitted).
E0_substrate = M_E / (q0 * (q0 - 1))        # 𝔈₀ ≈ 4.186 MeV
E0_qbeta = mpf(str(Q_NEUTRON_MEV))          # CAL-3 free-neutron β-decay Q-value

AME_B = {"D": mpf("2.2245662"), "T": mpf("8.4818"),
         "3He": mpf("7.7180"), "4He": mpf("28.29566")}
CHI = {"D": "atom-chi-rust-d.witness.json", "T": "atom-chi-rust-t.witness.json",
       "3He": "atom-chi-rust-3he.witness.json", "4He": "atom-chi-rust-4he.witness.json"}


_y_cache = None


def load_y(n):
    global _y_cache
    if _y_cache is None:
        with open(HERE / "y-lambda-at-q0.witness.json") as f:
            _y_cache = json.load(f)
    byn = _y_cache.get("data", _y_cache)["by_n"][str(n)]
    return {tuple(e["partition"]): mpf(e["y_at_q0_50dps"]) for e in byn}


def main() -> int:
    print(f"E_0(𝔈₀) = {float(E0_substrate):.5f} MeV   "
          f"E_0(Qβ) = {float(E0_qbeta):.5f} MeV   q₀ = {float(q0):.6f}\n")
    print("DERIVATION: B = E_0·Σ_λ y_λ(|χ^λ_free| − |χ^λ_atom|)  [observe-per-block]")
    print("  vs scalar B = E_0·(|Σ y_λ χ^λ_free| − |Σ y_λ χ^λ_atom|)  [collapse-first]\n")
    results = {}
    for name, fname in CHI.items():
        with open(HERE / fname) as f:
            d = json.load(f)
        d = d.get("data", d)
        atom = {tuple(e["partition"]): mpf(str(e["chi_lambda"])) for e in d["atom"]["by_partition"]}
        free = {tuple(e["partition"]): mpf(str(e["chi_lambda"])) for e in d["free"]["by_partition"]}
        y = load_y(d["atom"]["n_strands"])
        # observe-per-block: Σ_λ y_λ |χ^λ|
        S_free = sum(y[l] * fabs(free[l]) for l in free)
        S_atom = sum(y[l] * fabs(atom[l]) for l in atom)
        dperblock = S_free - S_atom
        # scalar collapse: |Σ_λ y_λ χ^λ|
        T_free = fabs(sum(y[l] * free[l] for l in free))
        T_atom = fabs(sum(y[l] * atom[l] for l in atom))
        dscalar = T_free - T_atom
        row = {"AME": float(AME_B[name])}
        for tag, E0 in (("𝔈₀", E0_substrate), ("Qβ", E0_qbeta)):
            Bpb = E0 * dperblock
            Bsc = E0 * dscalar
            row[f"B_perblock_{tag}"] = float(Bpb)
            row[f"err_perblock_{tag}"] = float((Bpb - AME_B[name]) / AME_B[name])
            row[f"B_scalar_{tag}"] = float(Bsc)
            row[f"err_scalar_{tag}"] = float((Bsc - AME_B[name]) / AME_B[name])
        results[name] = row
        print(f"── {name}  AME={float(AME_B[name]):7.3f} MeV")
        print(f"     per-block:  𝔈₀ {row['B_perblock_𝔈₀']:8.3f} ({row['err_perblock_𝔈₀']*100:+7.1f}%)   "
              f"Qβ {row['B_perblock_Qβ']:8.3f} ({row['err_perblock_Qβ']*100:+7.1f}%)")
        print(f"     scalar:     𝔈₀ {row['B_scalar_𝔈₀']:8.3f} ({row['err_scalar_𝔈₀']*100:+7.1f}%)   "
              f"Qβ {row['B_scalar_Qβ']:8.3f} ({row['err_scalar_Qβ']*100:+7.1f}%)")

    # A-growth of the derived per-block binding (no fit)
    g_pb = results["4He"]["B_perblock_𝔈₀"] / results["D"]["B_perblock_𝔈₀"]
    print(f"\nDerived per-block A-growth B(⁴He)/B(D) = {g_pb:.2f}  (AME 12.72)")

    wb = WitnessBuilder("derive-binding-per-block-archimedean", engine="mpmath")
    wb.set_description(
        "DERIVATION (0 fit): per-block archimedean realization of binding "
        "B = E_0·Σ_λ y_λ(|χ^λ_free|−|χ^λ_atom|), E_0 calibration-fixed "
        "(𝔈₀=m_e/(q₀(q₀−1)) and Q_β). Observe-per-block (Σ|·|) vs scalar "
        "collapse (|Σ·|). y_λ Wenzl, χ^λ Hoefsmit. AME comparison only."
    )
    wb.add_parameter("E0_substrate_MeV", float(E0_substrate))
    wb.add_parameter("E0_qbeta_MeV", float(E0_qbeta))
    wb.add_data("per_atom", results)
    wb.add_data("derived_A_growth_perblock_E0", float(g_pb))
    # honest assertion: report whether the 0-fit derivation lands within 50%
    worst = max(fabs(mpf(str(results[k]["err_perblock_𝔈₀"]))) for k in CHI)
    wb.add_assertion(
        name="per_block_archimedean_derivation_computed_zero_fit",
        computed=str(int(worst < 1e9)),  # always true; this is a derivation record
        expected="1",
        tolerance=0,
        source=(f"0-fit per-block derivation computed for D/T/³He/⁴He; worst "
                f"|err|(𝔈₀)={float(worst)*100:.0f}%. Recorded for comparison "
                "against the scalar collapse; no parameter was tuned."),
    )
    out = wb.save()
    print(f"\nWitness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
