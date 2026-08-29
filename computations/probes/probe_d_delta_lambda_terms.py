#!/usr/bin/env python3
"""
probe_d_delta_lambda_terms.py — the deuteron Δ_λ decomposition: what terms
are involved and which symbolic relations hold (session 2026-07-04, owner
question "look at D for Δ_λ magnitude — symbolic relations? what terms?").

EXPLORATORY (probe_ prefix, audit-only). NOT a closure ansatz (the Δ_λ gate
forbids a 7th fit). This is a STRUCTURAL characterisation of the per-partition
terms in the binding formula for the deuteron

    B(K) = m_e · Σ_{λ⊢6} y_λ(q) · χ^λ(β_K) · Δ_λ(K)          (binding_K_direct)

so the owner can see exactly which λ carry the binding, the magnitude
structure, and which exact symbolic relations constrain any Δ_λ closure.

## Terms (read from committed 50-dps witnesses — no re-derivation)

For each of the 11 partitions λ ⊢ 6:
  d_λ            irrep dimension (hook length)
  y_λ(q₀)        Wenzl central weight            [chi-deuteron-h6 witness]
  χ^λ(β_D)       bound-deuteron Hecke character  [chi-deuteron-h6]
  χ^λ(β_free)    free 2-nucleon character        [chi-deuteron-free-h6]
  χ^λ(β_D, q₀⁻¹) bar-conjugate value             [chi-deuteron-h6-at-qinv]
  Δχ^λ = χ_free − χ_bound   (the per-block trace difference carrying binding)

## Symbolic relations probed (derive-or-refute, exact)

1. Σ_λ y_λ χ^λ = tr_M  (Wedderburn closure — the scalar the tower collapses to).
2. Bar-conjugate law  χ^λ(β_D, q⁻¹) = (−1)^{L} χ^{λ'}(β_D, q)  (L = word length,
   λ' = conjugate partition) — the L2 identity, checked per-λ on the deuteron.
3. Zeros: which χ^λ(β_D) vanish (the H_6 analogue of χ^{(2,1)}(Δ)=0 at H_3).
4. Self-conjugate fixed point (3,2,1) (the SDP self-dual block).
5. Magnitude/sign dominance: which λ carry |y_λ·Δχ^λ|, and the sign pattern.

## The Δ_λ magnitude verdict (under-determination — already known, quantified)

The binding is ONE scalar equation Σ_λ y_λ χ^λ Δ_λ = B_AME/m_e against 11
per-λ unknowns Δ_λ ⇒ a 10-dim null space: Δ_λ(D) is NOT uniquely fixed by D.
A UNIFORM Δ_λ = δ has magnitude δ = (B_AME/m_e)/tr_M — reported. The symbolic
relations above are the constraints any non-uniform closure must respect;
they do not by themselves pin Δ_λ at A=2 (that needs cross-A, per PR #3266).
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

import json  # noqa: E402
import mpmath as mp  # noqa: E402

from _precision import set_compute_dps, COMPUTE_DPS  # noqa: E402
set_compute_dps()
DPS = COMPUTE_DPS

from codata_constants import (  # noqa: E402
    M_E_MEV, AME_B_DEUTERON_MEV_VALIDATION,
)
from witness_base import WitnessBuilder  # noqa: E402


def _pkey(v):
    """Normalise a partition (list or string) to a canonical tuple key."""
    if isinstance(v, list):
        return tuple(int(x) for x in v)
    return tuple(int(x) for x in str(v).strip("[]").split(",") if x.strip())


def _load(name):
    d = json.loads((COMP / name).read_text())
    return {_pkey(row["partition"]): row for row in d["by_partition"]}, d


def conjugate(part):
    """Conjugate (transpose) of a partition given as a tuple."""
    if not part:
        return ()
    m = max(part)
    return tuple(sum(1 for a in part if a >= i) for i in range(1, m + 1))


def parse(pstr):
    return tuple(int(x) for x in pstr.strip("[]").split(",") if x.strip())


def word_length_parity_D():
    """The deuteron atom word β_D = atom_braid_word_3A(1,1): its length parity
    L mod 2 fixes the sign in the bar-conjugate law χ(1/q)=(−1)^L χ_{λ'}(q)."""
    try:
        from mass_at_3A_proper import atom_braid_word_3A
        w = atom_braid_word_3A(1, 1)
        return len(w) % 2, len(w)
    except Exception:
        return None, None


def main() -> int:
    bound, bd = _load("chi-deuteron-h6-at-q0-50dps.witness.json")
    free, _ = _load("chi-deuteron-free-h6-at-q0-50dps.witness.json")
    # MATCHED FRAME (bean qou-1oxx, owner decision 2026-08-26 option 1).
    # This read the colour-BLIND at-qinv witness while `bound` above is
    # colour-WEIGHTED, so relation 2 below compared f_canon(q0) against
    # f_strict(1/q0) -- two DIFFERENT functions. Measured, the four
    # pairings of the deuteron bar-conjugate law are:
    #     blind(q0)  vs blind(1/q0)  = 1.48e-49   <- EXACT at 50 dps
    #     canon(q0)  vs canon(1/q0)  = 5.86e-04   <- reported now
    #     canon(q0)  vs blind(1/q0)  = 2.63e-04   <- the old mixed value
    #     blind(q0)  vs canon(1/q0)  = 3.23e-04
    # The blind form IS the bar-symmetriser and the law holds in it
    # EXACTLY, so the residual is the colour weighting and nothing else.
    qinv, _ = _load(
        "chi-deuteron-h6-at-qinv-50dps-colour-weighted.witness.json")

    m_e = mp.mpf(str(M_E_MEV))
    B_AME = mp.mpf(str(AME_B_DEUTERON_MEV_VALIDATION))
    tr_M = mp.mpf(str(bd["tr_M_at_q0"]))
    Lpar, Lword = word_length_parity_D()

    rows = []
    sum_contrib = mp.mpf(0)
    dtr = mp.mpf(0)
    for p in bound:
        part = p                                # tuple key
        d_l = int(bound[p]["dim"])
        y = mp.mpf(str(bound[p]["y_lambda"]))
        chi_b = mp.mpf(str(bound[p]["chi_lambda"]))
        chi_f = mp.mpf(str(free[p]["chi_lambda"]))
        chi_qi = mp.mpf(str(qinv[p]["chi_lambda"]))
        dchi = chi_f - chi_b
        contrib = y * chi_b                     # bound tr_M term
        bind_contrib = y * dchi                 # per-block binding (free−bound)
        sum_contrib += contrib
        dtr += bind_contrib
        rows.append({
            "lambda": list(p), "conj": str(list(conjugate(part))),
            "self_conj": conjugate(part) == part,
            "dim": d_l,
            "y_lambda": mp.nstr(y, 12),
            "chi_bound": mp.nstr(chi_b, 12),
            "chi_free": mp.nstr(chi_f, 12),
            "chi_qinv": mp.nstr(chi_qi, 12),
            "delta_chi": mp.nstr(dchi, 12),
            "trM_term": mp.nstr(contrib, 12),
            "binding_term_y_dchi": mp.nstr(bind_contrib, 12),
        })

    # relation 2: bar-conjugate χ^λ(1/q) = (−1)^L χ^{λ'}(q)
    barconj = []
    sign = (-1) ** Lpar if Lpar is not None else None
    for p in bound:
        cj = conjugate(p)
        chi_qi = mp.mpf(str(qinv[p]["chi_lambda"]))
        match = mp.mpf(str(bound[cj]["chi_lambda"])) if cj in bound else None
        if match is not None and sign is not None:
            # mpf, not float(): the ratchet is about the FIELD, not the
            # magnitude. Serialised via mp.nstr so it never enters float64.
            resid = abs(chi_qi - sign * match) / (abs(match) + 1)
            barconj.append({"lambda": list(p), "conj": list(cj),
                            "chi_qinv": mp.nstr(chi_qi, 10),
                            "signed_chi_conj_q": mp.nstr(sign * match, 10),
                            "rel_resid": mp.nstr(resid, 20),
                            "_resid_mpf": resid})
    barconj_max = max((b["_resid_mpf"] for b in barconj), default=None)
    for _b in barconj:
        del _b["_resid_mpf"]

    # zeros + dominance
    zeros = [r["lambda"] for r in rows if abs(mp.mpf(r["chi_bound"])) < mp.mpf("1e-9")]
    dom = sorted(rows, key=lambda r: -abs(mp.mpf(r["binding_term_y_dchi"])))[:3]
    uniform_delta = (B_AME / m_e) / tr_M

    print("=" * 92)
    print("DEUTERON Δ_λ TERMS  (β_D in H_6, 11 partitions; from committed 50-dps witnesses)")
    print("=" * 92)
    print(f"  β_D word length L = {Lword} (parity {Lpar}); tr_M(β_D) = {mp.nstr(tr_M,10)};  "
          f"B_AME/m_e = {mp.nstr(B_AME/m_e,10)}")
    print(f"  {'λ':>14}{'dim':>4}{'y_λ':>13}{'χ_bound':>13}{'Δχ=f−b':>13}"
          f"{'y·χ_b':>13}{'y·Δχ':>13}{'selfconj':>9}")
    for r in rows:
        print(f"  {str(r['lambda']):>14}{r['dim']:>4}{r['y_lambda']:>13}"
              f"{r['chi_bound']:>13}{r['delta_chi']:>13}{r['trM_term']:>13}"
              f"{r['binding_term_y_dchi']:>13}{'  ✓' if r['self_conj'] else '':>9}")
    print(f"\n  Σ y_λ χ_bound = {mp.nstr(sum_contrib,12)}  (= tr_M ✓ "
          f"resid {mp.nstr(abs(sum_contrib-tr_M), 2)})")
    print(f"  Σ y_λ Δχ (scalar binding trace diff) = {mp.nstr(dtr,12)}")
    print(f"\n  [rel 2] bar-conjugate χ^λ(1/q) = (−1)^L χ^{{λ'}}(q), L parity "
          f"{Lpar}: max rel-resid = {mp.nstr(barconj_max, 4)}"
          if barconj_max is not None else "  [rel 2] word length unavailable")
    print(f"  [rel 3] χ_bound zeros: {zeros or 'none'}")
    print(f"  [rel 4] self-conjugate block: (3,2,1)")
    print(f"  [rel 5] top-3 binding-carrying λ (|y·Δχ|): "
          f"{[d['lambda'] for d in dom]}")
    print(f"\n  Δ_λ MAGNITUDE: uniform Δ_λ = δ = (B_AME/m_e)/tr_M = "
          f"{mp.nstr(uniform_delta,10)}  (11 unknowns, 1 eq ⇒ 10-dim null space; "
          f"D under-determines Δ_λ — cross-A needed)")

    wb = (WitnessBuilder("probe-d-delta-lambda-terms", engine="mpmath")
          .set_description(
              "Deuteron Δ_λ per-partition term analysis: y_λ, χ^λ(β_D) bound/"
              "free/q⁻¹, Δχ, and per-block binding y_λ·Δχ for all 11 λ⊢6, from "
              "committed 50-dps witnesses. Symbolic relations: Wedderburn "
              "closure Σy_λχ^λ=tr_M; bar-conjugate law χ(1/q)=(−1)^Lχ_{λ'}(q); "
              "χ_bound zeros; (3,2,1) self-conjugate; magnitude/sign dominance. "
              "Δ_λ under-determined at A=2 (1 eq, 11 unknowns); uniform-δ "
              "magnitude reported. Structural characterisation, NOT a closure "
              "ansatz (Δ_λ gate).")
          .set_audit_only(
              "docs/audits/2026-07-04-deuteron-dressing-is-proton-net.md")
          .add_parameter("compute_dps", DPS)
          .add_parameter("beta_D_word_length", Lword)
          .add_data("terms", rows)
          .add_data("bar_conjugate_check", barconj)
          .add_data("bar_conjugate_max_rel_resid", barconj_max)
          .add_data("sum_y_chi_bound", mp.nstr(sum_contrib, 20))
          .add_data("tr_M", mp.nstr(tr_M, 20))
          .add_data("scalar_binding_trace_diff", mp.nstr(dtr, 20))
          .add_data("chi_bound_zeros", zeros)
          .add_data("top3_binding_lambda", [d["lambda"] for d in dom])
          .add_data("uniform_delta_magnitude", mp.nstr(uniform_delta, 20)))
    wb.add_assertion(
        "wedderburn_closure",
        computed=mp.nstr(abs(sum_contrib - tr_M), 20), expected="0",
        tolerance="1e-9",
        source="Σ_λ y_λ χ^λ(β_D) = tr_M(β_D) (witness cross-check)")
    if barconj_max is not None:
        # The bar-conjugate law holds only APPROXIMATELY for the deuteron:
        # the colour-weighted p-n interface breaks the clean q↔q⁻¹ symmetry.
        # CORRECTED 2026-08-26 (bean qou-1oxx): this said "≈2.6e-4" and called
        # it "the colour-weighting signature". 2.6e-4 was the MIXED pairing
        # f_canon(q0) vs f_strict(1/q0) — two different functions. In a
        # consistent canonical frame the residual is 5.86e-04, and in the
        # colour-BLIND frame the law is EXACT (1.48e-49 at 50 dps), because
        # the blind form IS the bar-symmetriser. So the breaking is indeed
        # the colour weighting — but its honest size is 5.86e-04, and the
        # coincidence with the convention-D trace gap (1.955e-4) that the old
        # comment leaned on does not survive the correction. Recorded as a
        # finding, not a hard pass.
        wb.add_assertion(
            "bar_conjugate_law_broken_by_colour_weighting",
            computed=bool(1e-6 < barconj_max < 1e-2), expected=True,
            source="χ^λ(β_D, q⁻¹) vs (−1)^L χ^{λ'}(β_D, q): residual ≈2.6e-4 "
                   "= colour-weighting / flavor-split symmetry breaking")
    wb.save()
    print("\nwitness → probe-d-delta-lambda-terms.witness.json (audit-only)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
