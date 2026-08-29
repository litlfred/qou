#!/usr/bin/env python3
"""Is the `-|S_3|*m_e` term in the canonical mass formula a unit convention
or a physical count?  (bean qou-mrel)

The canonical nucleon mass (docs/canonical-mass-formula-guardrail.md) is

    m_p = dim V_{(2,1)} * ( m_mu * F_Bor  -  |S_3| * m_e )
        = 2 * ( m_mu * F_Bor - 6 * m_e )
    m_mu  = m_e * Vol(4_1) / hbar_q^2
    F_Bor = |tr_M(beta_Bor)| * [3]_q! / q^3          (dimensionless)

Substituting the muon anchor,

    m_p = 2 * m_e * ( Vol(4_1) * F_Bor / hbar_q^2  -  6 )
    m_p / m_e = 2 * Vol(4_1) * F_Bor / hbar_q^2  -  12

so m_e factors out completely: QOU predicts only the RATIO m_p/m_e, never an
absolute mass.  That is the precise sense in which mass here is relational --
there is no intrinsic mass anywhere in the formula.

But m_e appears TWICE, and only the first appearance is the scale:

  (1) the overall unit, via the muon anchor -- absorbed, uncontroversial;
  (2) `- |S_3| * m_e`, SUBTRACTED, once per Hecke block, x2 via
      dim V_{(2,1)}  ==>  -12 * m_e in total.

Appearance (2) is a q-INDEPENDENT ADDITIVE INTEGER multiple of m_e.  The
framework's own reading ("m_e = CAL-1, the dimensional unit") explains (1) and
says nothing about (2).

This script asks three falsifiable questions about (2):

  Q1  How load-bearing is it?  Delete the term and see how far m_p moves,
      in MeV, in relative terms, and in units of the CODATA uncertainty.
  Q2  Is the coefficient finely determined?  Sweep the integer coefficient c
      in `- c * m_e` and see how sharply the data selects c = 6.
  Q3  Is it really an integer, or does a fitted real do better?  Solve for the
      real c* that reproduces CODATA exactly and measure |c* - 6|.

A term that is merely a unit convention should fail Q1 (deleting it costs
nothing measurable).  A term that is a post-hoc fit should fail Q2/Q3 (the
best c would be a non-integer with no structural identity).

Precision: exact 50-dps inputs from the committed substrate-identity witness;
mpmath at 65 dps compute / 50 dps serialization per _precision.py convention.
No float64 anywhere in the arithmetic.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from mpmath import mp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: F401, E402
from codata_constants import M_P_MEV_VALIDATION  # noqa: E402

mp.dps = 65

_WITNESS = HERE / "m-p-substrate-identity-50dps.witness.json"
_OUT = HERE / "me-additive-term-structure.witness.json"

# CODATA 2022 electron mass and its 1-sigma, MeV.
# m_e = 0.51099895069(16) MeV  (relative u_r = 3.1e-10)
M_E_MEV = mp.mpf("0.51099895069")
M_E_SIGMA = mp.mpf("0.00000000016")

# CODATA 2022 proton mass and its 1-sigma, MeV.
# m_p = 938.27208816(29) MeV
#
# P31: sourced from the registry rather than retyped. A hand-typed CODATA
# literal drifts silently when the registry moves — the same class as the
# CODATA-2018 U_MEV literal fixed in #4653. Value-identical today
# (938.27208816), so this changes provenance, not arithmetic.
#
# The VALIDATION alias is the correct import: codata_constants deprecates
# plain M_P_MEV because m_p may be used to CHECK a prediction, never to make
# one (three-calibration discipline, CAL-1/2/3). See the note at `c_star`
# below — this file does both, and only one of them is sanctioned.
M_P_CODATA = M_P_MEV_VALIDATION
M_P_SIGMA = mp.mpf("0.00000029")

DIM_V21 = 2   # Wedderburn dimension of the (2,1) block of H_3(q)
ORDER_S3 = 6  # |S_3|


def _load():
    d = json.loads(_WITNESS.read_text())["data"]
    m_p = mp.mpf(d["predictions"]["m_p_MeV"])
    f_bor = mp.mpf(d["substrate_building_blocks"]["F_Bor"])
    return m_p, f_bor


def constituent_term(m_p_canonical: mp.mpf) -> mp.mpf:
    """Recover `m_mu * F_Bor` from the canonical m_p by inverting the formula.

    m_p = 2*(E_constit - 6*m_e)  ==>  E_constit = m_p/2 + 6*m_e

    Using the committed m_p (rather than recomputing the muon anchor) keeps
    this probe independent of which q0 pin produced the witness: whatever
    E_constit is, the question here is only about the ADDITIVE term.
    """
    return m_p_canonical / DIM_V21 + ORDER_S3 * M_E_MEV


def m_p_with_coefficient(e_constit: mp.mpf, c) -> mp.mpf:
    """m_p as a function of the subtracted electron count c."""
    return DIM_V21 * (e_constit - mp.mpf(c) * M_E_MEV)


def main() -> int:
    m_p_canon, f_bor = _load()
    e_constit = constituent_term(m_p_canon)

    # --- Q1: load-bearing? Delete the term (c = 0). -----------------------
    m_p_no_term = m_p_with_coefficient(e_constit, 0)
    shift_mev = m_p_no_term - m_p_canon           # = +12*m_e exactly
    shift_rel = shift_mev / m_p_canon
    shift_sigma = shift_mev / M_P_SIGMA

    # --- Q2: integer sweep around c = 6 -----------------------------------
    sweep = []
    for c in range(0, 13):
        m_p_c = m_p_with_coefficient(e_constit, c)
        resid_ppm = (m_p_c - M_P_CODATA) / M_P_CODATA * mp.mpf(10) ** 6
        sweep.append(
            {
                "c": c,
                "m_p_MeV": mp.nstr(m_p_c, 22),
                "residual_vs_codata_ppm": mp.nstr(resid_ppm, 12),
                "abs_residual_ppm": mp.nstr(abs(resid_ppm), 12),
            }
        )
    best = min(sweep, key=lambda r: abs(mp.mpf(r["abs_residual_ppm"])))

    # --- Q3: best-fit REAL coefficient ------------------------------------
    # m_p(c) = 2*(E - c*m_e) = M_P_CODATA  =>  c* = (E - M_P_CODATA/2)/m_e
    c_star = (e_constit - M_P_CODATA / DIM_V21) / M_E_MEV
    c_dev = c_star - ORDER_S3
    # How far is c* from 6, in units of the spacing between adjacent integers?
    # Adjacent integers shift m_p by 2*m_e = 1.022 MeV, so this is the
    # fraction of one integer step.
    c_dev_frac = abs(c_dev)

    # separation ratio: how much better c=6 is than the next-best integer
    ordered = sorted(sweep, key=lambda r: abs(mp.mpf(r["abs_residual_ppm"])))
    sep = mp.mpf(ordered[1]["abs_residual_ppm"]) / mp.mpf(ordered[0]["abs_residual_ppm"])

    print("=" * 74)
    print("Q1  Is the -|S_3|*m_e term load-bearing, or a unit convention?")
    print("=" * 74)
    print(f"  m_p canonical (c=6)      = {mp.nstr(m_p_canon, 22)} MeV")
    print(f"  m_p with term DELETED    = {mp.nstr(m_p_no_term, 22)} MeV")
    print(f"  shift                    = {mp.nstr(shift_mev, 16)} MeV   (= 12*m_e)")
    print(f"  shift, relative          = {mp.nstr(shift_rel * 100, 8)} %")
    print(f"  shift, in CODATA sigma   = {mp.nstr(shift_sigma, 8)} sigma")
    print()
    print("  VERDICT: a unit convention is unobservable by construction.")
    print("  Deleting this term moves m_p by 0.65% -- ~2e7 sigma. It is NOT")
    print("  a convention; it is a load-bearing physical term.")
    print()
    print("=" * 74)
    print("Q2  Integer sweep: how sharply does the data select c = |S_3| = 6?")
    print("=" * 74)
    print(f"  {'c':>3}  {'m_p (MeV)':>26}  {'residual vs CODATA (ppm)':>26}")
    for r in sweep:
        mark = "   <== |S_3|" if r["c"] == ORDER_S3 else ""
        print(f"  {r['c']:>3}  {r['m_p_MeV']:>26}  {r['residual_vs_codata_ppm']:>26}{mark}")
    print()
    print(f"  best integer             = c = {best['c']}")
    print(f"  |residual| at best       = {best['abs_residual_ppm']} ppm")
    print(f"  |residual| at runner-up  = {ordered[1]['abs_residual_ppm']} ppm (c={ordered[1]['c']})")
    print(f"  separation ratio         = {mp.nstr(sep, 8)}x")
    print()
    print("=" * 74)
    print("Q3  Is the coefficient an integer, or does a fitted real do better?")
    print("=" * 74)
    print(f"  best-fit REAL c*         = {mp.nstr(c_star, 20)}")
    print(f"  c* - 6                   = {mp.nstr(c_dev, 12)}")
    print(f"  |c* - 6| as fraction of")
    print(f"    one integer step       = {mp.nstr(c_dev_frac, 12)}")
    print()
    print("  A fitted coefficient would land on a generic real. This one lands")
    print(f"  on the integer 6 = |S_3| to {mp.nstr(c_dev_frac, 4)} of one step.")
    print()
    print("=" * 74)
    print("READING (bean qou-mrel)")
    print("=" * 74)
    print("  m_e factors out of the formula entirely: only m_p/m_e is predicted,")
    print("  so mass in QOU is relational -- there is no intrinsic mass. That")
    print("  much the 'CAL-1 = dimensional unit' framing already covers.")
    print()
    print("  What it does NOT cover is this term. It is (i) additive, not")
    print("  multiplicative; (ii) q-independent, so it does not scale with the")
    print("  substrate; (iii) an INTEGER multiple of m_e, the integer being")
    print("  |S_3|; and (iv) load-bearing at 0.65%. A dimensional unit cannot")
    print("  be any of those things. A COUNT of electron-mass quanta can be")
    print("  all four.")
    print()
    print("  This is consistent with -- and is the sharpest evidence for -- the")
    print("  reading that the formula measures an INTERACTION energy against an")
    print("  electron probe rather than an intrinsic property of the braid.")
    print("  It does not by itself PROVE that reading: |S_3| is the order of the")
    print("  strand-permutation group and is supplied by the Hecke structure, so")
    print("  a derivation must still show WHY that count enters denominated in")
    print("  m_e. That derivation is the open content of bean qou-mrel.")

    payload = {
        "schema": "witness/v1",
        "description": (
            "Structure of the -|S_3|*m_e additive term in the canonical nucleon "
            "mass: load-bearing test, integer sweep, and best-fit real coefficient. "
            "Bean qou-mrel."
        ),
        "computation": {
            "script": "computations/me_additive_term_structure.py",
            "inputs": "computations/m-p-substrate-identity-50dps.witness.json",
            "precision_dps": 65,
        },
        "data": {
            "formula": "m_p = dim V_{(2,1)} * (m_mu*F_Bor - |S_3|*m_e), dim V_{(2,1)}=2, |S_3|=6",
            "m_e_MeV": mp.nstr(M_E_MEV, 20),
            "F_Bor": mp.nstr(f_bor, 25),
            "E_constit_MeV": mp.nstr(e_constit, 25),
            "q1_load_bearing": {
                "m_p_canonical_MeV": mp.nstr(m_p_canon, 25),
                "m_p_term_deleted_MeV": mp.nstr(m_p_no_term, 25),
                "shift_MeV": mp.nstr(shift_mev, 20),
                "shift_percent": mp.nstr(shift_rel * 100, 12),
                "shift_in_codata_sigma": mp.nstr(shift_sigma, 12),
                "verdict": "load-bearing, not a convention",
            },
            "q2_integer_sweep": sweep,
            "q2_best_integer": best["c"],
            "q2_separation_ratio": mp.nstr(sep, 12),
            "q3_best_fit_real_coefficient": mp.nstr(c_star, 20),
            "q3_deviation_from_6": mp.nstr(c_dev, 12),
            "scope": (
                "scope-(a) structural observation. Establishes that the additive "
                "term is a load-bearing integer count of m_e quanta, NOT a unit "
                "convention. Does NOT establish the interaction/test-particle "
                "reading, which requires deriving why |S_3| enters denominated "
                "in m_e."
            ),
        },
    }
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    payload.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        payload, script_path=__file__, engine=None, q0_anchor=False)
    _OUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"\nwrote {_OUT.relative_to(HERE.parent)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
