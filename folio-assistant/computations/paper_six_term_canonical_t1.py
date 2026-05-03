#!/usr/bin/env python3
"""
6-term mass formula with CANONICAL Term 1 from the Hoefsmit+Wenzl
bridge witness (replacing the buggy per-generator-product approximation
in `paper_six_term_isotope_sweep.py`).

Background:

  Three-path comparison (`canonical_tr_m_three_path_comparison.py`)
  established that:

  - Hoefsmit+Wenzl bridge witness ≡ markov_peel: BOTH compute the
    canonical Markov trace `Σ_λ y_λ(q) · χ^λ(β)` and agree to 15+
    digits.

  - The 6-term formula's existing Term 1
    (`Π |V̂_i|` in `paper_six_term_isotope_sweep.py`) is a per-
    generator-product APPROXIMATION, NOT the canonical Markov
    trace — that's the source of the formula's isospin-violating
    T − ³He = −737 MeV pathology.

This script:

  1. Reads canonical Term 1 values from `atomic-tr-m-mpfr-50dps.witness.json`
  2. Reuses Terms 2–6 implementations from paper_six_term_isotope_sweep
     (which compute per-generator brane-tower / Frobenius / chirality /
     residue contributions)
  3. Recalibrates the Hecke→MeV conversion (E_0) from proton mass
  4. Predicts atomic masses and compares to CODATA

Open caveats:
  - Terms 2 (`Σ Φ_q(|V̂_i|)`) and 3 (`z² Σ Φ_q(|V̂_i V̂_j|)`) still
    use per-generator |V̂_i| from `atom_per_generator_volumes`.
    Whether THESE are isospin-respecting on the production atomic
    braid is an open audit; the per-strand (c, d) parameters do
    encode quark content, so per-generator volumes likely differ
    between mirror nuclei (T vs ³He) — but maybe by less than the
    Term 1 discrepancy.
  - Term 5 (chirality) sign pattern is hand-encoded per isotope in
    the existing sweep; for now reuse the same pattern.
  - Term 6 (cyclotomic residues) is currently treated as zero in the
    existing sweep at q_0; this is the term the user emphasized as
    "the series" — need to wire `term6_full_pole_sum` for a real value.

Output: `paper-six-term-canonical-t1.witness.json`
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from itertools import combinations
from pathlib import Path

import mpmath as mp

mp.mp.dps = 50

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP  # noqa: E402
from hecke_core import (  # noqa: E402
    atom_per_generator_volumes, h as h_val, z as z_mark,
)
from mass_endomorphism import Phi_q  # noqa: E402

Q0 = Q_MP
Z_MARK = mp.mpf(str(float(z_mark)))
H_VAL = mp.mpf(str(float(h_val)))


def abs_mpf(v):
    x = v['full'] if isinstance(v, dict) else v
    return abs(mp.mpf(str(float(x))))


# ── Canonical Term 1 from bridge witness ────────────────────────────
def load_canonical_term1() -> dict[str, mp.mpf]:
    """Map atom name → canonical |tr_M(β)| from bridge witness."""
    path = HERE / "atomic-tr-m-mpfr-50dps.witness.json"
    if not path.exists():
        raise FileNotFoundError(path)
    d = json.loads(path.read_text())
    out = {}
    for r in d.get("results", []):
        s = r["tr_M_at_q0_50dps"]
        out[r["atom"]] = abs(mp.mpf(s))
    return out


# Inline markov_peel values for atoms not in the bridge witness (e.g. ⁴He)
_PEEL_INLINE = {
    "helium-4": "0.055348345876697992162807082650033407844603061676025",
}


# ── Canonical Term 6 from Habiro residue witness ────────────────────
def load_canonical_term6_MeV() -> dict[int, mp.mpf]:
    """Map mass number A → Term 6 contribution in MeV.

    The Habiro residue is per-A (depends only on strand count n=3A),
    so T and ³He share a value.
    """
    path = HERE / "term6-habiro-residue-mpfr-50dps.witness.json"
    if not path.exists():
        return {}
    d = json.loads(path.read_text())
    out: dict[int, mp.mpf] = {}
    for r in d.get("results_by_atom", []):
        # entries keyed "A=1", "A=2", ...
        try:
            A = int(r["atom"].split("=")[1])
            out[A] = mp.mpf(r["term6_b_pred_mev_50dps"])
        except (KeyError, IndexError, ValueError):
            continue
    return out


# ── Terms 2-6 reuse from paper_six_term_isotope_sweep ───────────────
def term2_single_gen_tower(vols):
    total = mp.mpf(0)
    for v in vols:
        try:
            phi = Phi_q(abs_mpf(v))
            if not mp.isinf(phi) and not mp.isnan(phi):
                total += phi
        except Exception:
            pass
    return total


def term3_pair_gen_tower(vols):
    total = mp.mpf(0)
    for (i, j) in combinations(range(len(vols)), 2):
        arg = abs_mpf(vols[i]) * abs_mpf(vols[j])
        try:
            phi = Phi_q(arg)
            if not mp.isinf(phi) and not mp.isnan(phi):
                total += Z_MARK ** 2 * phi
        except Exception:
            pass
    return total


def term4_frobenius_codim(A):
    from schur_weyl_symbolic import partitions_of
    from hecke_characters import young_hooks, qfac
    n = 3 * A
    nfac_val = mp.mpf(qfac(n))
    q = Q0; q_inv = 1 / q; denom = q - q_inv
    total = mp.mpf(0)
    for lam in partitions_of(n):
        hooks = young_hooks(lam)
        dim_q_val = nfac_val
        for h in hooks:
            hl_val = (q ** h - q_inv ** h) / denom
            dim_q_val /= hl_val
        if abs(dim_q_val) > mp.mpf("1e-40"):
            total += 1 / dim_q_val
    return total


def term5_chirality(Z, N, chirality_signs):
    a_K = mp.mpf(1)
    for s in chirality_signs:
        a_K *= (1 + s * H_VAL)
    return a_K


def chirality_signs_for_isotope(iso):
    return {
        "p": [], "n": [],
        "deuteron": [+1], "tritium": [+1, -1],
        "helium-3": [+1, -1], "helium-4": [+1, -1, +1, -1],
    }.get(iso, [])


def six_term_mass_canonical(
    atom_name, Z, N, m_e_hecke, *, include_inter=True,
    chirality_signs=None, term5_mode="multiplicative_on_t1",
):
    """6-term formula with Term 1 from canonical bridge witness."""
    # Term 1: canonical bridge value
    canonical_t1 = load_canonical_term1()
    if atom_name in canonical_t1:
        t1 = canonical_t1[atom_name]
    elif atom_name in _PEEL_INLINE:
        t1 = abs(mp.mpf(_PEEL_INLINE[atom_name]))
    else:
        raise KeyError(f"no canonical Term 1 for {atom_name!r}")

    # Per-generator volumes (still used by Terms 2, 3)
    vols = atom_per_generator_volumes(Z, N, include_inter=include_inter)
    t2 = term2_single_gen_tower(vols)
    t3 = term3_pair_gen_tower(vols)
    t4_raw = term4_frobenius_codim(Z + N) if Z + N >= 1 else mp.mpf(0)
    t4 = mp.mpf(str(m_e_hecke)) * t4_raw

    if chirality_signs is None:
        chirality_signs = []
    t5_factor = term5_chirality(Z, N, chirality_signs)

    if term5_mode == "additive":
        t1_with = t1
        t5 = (t5_factor - 1) * t1
    elif term5_mode == "multiplicative_on_t1":
        t1_with = t1 * t5_factor
        t5 = t1_with - t1
    else:
        raise ValueError(term5_mode)

    # Term 6: cyclotomic residue series, loaded from the canonical
    # Habiro residue witness.  Per-A only (T and ³He share the value).
    # NOTE: t6 from the witness is in MeV directly (term6_b_pred_mev),
    # not in Hecke units.  We convert back to Hecke units by dividing
    # by m_e_MeV (since the witness scales by m_e), then multiply by
    # m_e_hecke at assembly time — a clean conversion in Hecke units
    # would need a more careful audit.  For now: report the raw MeV
    # value in the witness so downstream readers see the contribution
    # directly, and add 0 to the Hecke-unit total below to keep the
    # calibration unchanged (Term 6 affects the prediction additively
    # in MeV, post-calibration).
    t6_per_A_MeV = load_canonical_term6_MeV()
    A_atom = Z + N
    t6_MeV = t6_per_A_MeV.get(A_atom, mp.mpf(0))

    # Hecke-unit assembly (calibration target): t1+t2+t3+t4 (Term 5
    # absorbed into t1_with above; Term 6 added as MeV at output)
    total = float(t1_with) + float(t2) + float(t3) + float(t4)
    return {
        "term1_canonical": float(t1),
        "term2_single_gen_tower": float(t2),
        "term3_pair_gen_tower": float(t3),
        "term4_frobenius_codim_scaled": float(t4),
        "term5_additive_contribution": float(t5),
        "term5_chirality_factor_a_K": float(t5_factor),
        "term6_higher_residues_MeV": float(t6_MeV),
        "term5_mode": term5_mode,
        "m_e_hecke": float(m_e_hecke),
        "total_hecke": total,
    }


def main() -> int:
    print("=" * 80)
    print("  6-TERM MASS FORMULA — CANONICAL TERM 1 from bridge witness")
    print(f"  q_0 = {float(Q0):.10f}")
    print("=" * 80)

    # Proton calibration: Term 1 = canonical proton value, no chirality
    p_terms = six_term_mass_canonical(
        "proton", 1, 0,
        m_e_hecke=mp.mpf(1),  # Will be recomputed after E_0 known
        include_inter=False,
        chirality_signs=[],
    )
    # Bootstrap: pretend m_e_hecke = 1, then recompute E_0
    m_p_hecke_initial = p_terms["total_hecke"]
    M_P_CODATA = 938.27208816
    E_0 = M_P_CODATA / m_p_hecke_initial
    # Real m_e_hecke = 0.51099895 / E_0
    m_e_hecke = mp.mpf("0.51099895") / mp.mpf(str(E_0))

    # Recompute proton with proper m_e_hecke
    p_terms = six_term_mass_canonical(
        "proton", 1, 0, m_e_hecke=m_e_hecke,
        include_inter=False, chirality_signs=[],
    )
    m_p_hecke = p_terms["total_hecke"]
    E_0 = M_P_CODATA / m_p_hecke

    print(f"\n  Proton calibration:")
    print(f"    canonical t1 (proton) = {p_terms['term1_canonical']:.6f}")
    print(f"    t2={p_terms['term2_single_gen_tower']:.3e}  "
          f"t3={p_terms['term3_pair_gen_tower']:.3e}  "
          f"t4={p_terms['term4_frobenius_codim_scaled']:.3e}")
    print(f"    m_p_hecke = {m_p_hecke:.6e}")
    print(f"    E_0       = {E_0:.6e} MeV/Hecke-unit")

    print(f"\n  {'iso':<10} {'A':>3} {'total_H':>12} {'M_pred':>10} {'M_CODATA':>10} {'err%':>8}")
    print("  " + "-" * 60)

    cases = [
        ("proton",   1, 0,    938.272),
        ("neutron",  0, 1,    939.565),
        ("deuteron", 1, 1,   1876.124),
        ("tritium",  1, 2,   2809.432),
        ("helium-3", 2, 1,   2809.413),
        ("helium-4", 2, 2,   3728.401),
    ]
    rows = []
    for atom, Z, N, M_codata in cases:
        try:
            t = six_term_mass_canonical(
                atom, Z, N, m_e_hecke=m_e_hecke,
                include_inter=(Z + N >= 2),
                chirality_signs=chirality_signs_for_isotope(atom),
            )
            M_pred_no_t6 = t["total_hecke"] * E_0
            t6_MeV = t["term6_higher_residues_MeV"]
            M_pred = M_pred_no_t6 + t6_MeV
            err = (M_pred - M_codata) / M_codata * 100
            err_no_t6 = (M_pred_no_t6 - M_codata) / M_codata * 100
            print(f"  {atom:<10} {Z+N:>3} {t['total_hecke']:>12.4e} "
                  f"{M_pred:>10.3f} {M_codata:>10.3f} {err:>+8.3f}% "
                  f"(t6={t6_MeV:>+7.4f}, no-t6 err={err_no_t6:+.3f}%)")
            rows.append({
                "atom": atom, "Z": Z, "N": N, "A": Z + N,
                "M_pred_MeV_no_t6": M_pred_no_t6,
                "M_pred_MeV": M_pred,
                "term6_MeV": t6_MeV,
                "M_codata_MeV": M_codata,
                "err_pct": err,
                "err_pct_no_t6": err_no_t6,
                **t,
            })
        except Exception as e:
            print(f"  {atom:<10} ERROR: {e}")

    # Isospin check
    print(f"\n  Isospin (T vs ³He):")
    rT = next((r for r in rows if r["atom"] == "tritium"), None)
    r3 = next((r for r in rows if r["atom"] == "helium-3"), None)
    if rT and r3:
        print(f"    Predicted T - ³He = {rT['M_pred_MeV'] - r3['M_pred_MeV']:+.4f} MeV")
        print(f"    CODATA    T - ³He = {rT['M_codata_MeV'] - r3['M_codata_MeV']:+.4f} MeV")
        print(f"    (CODATA is +0.019; non-zero from Coulomb + m_n − m_p)")

    witness = {
        "computation": "paper-six-term-canonical-t1",
        "description": (
            "6-term mass formula with Term 1 replaced by canonical "
            "Hoefsmit+Wenzl bridge values (instead of the legacy "
            "per-generator-product approximation in "
            "paper_six_term_isotope_sweep.py).  Tests whether the "
            "isospin-violating T - ³He = -738 MeV pathology in the "
            "original 6-term sweep was caused by Term 1 alone or by "
            "additional terms."
        ),
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "E_0_MeV_per_hecke": float(E_0),
        "m_e_hecke": float(m_e_hecke),
        "rows": rows,
    }
    out = HERE / "paper-six-term-canonical-t1.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
