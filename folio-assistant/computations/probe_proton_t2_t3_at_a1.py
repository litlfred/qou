"""
probe_proton_t2_t3_at_a1.py — m_p chain Item A from PR #671 audit.

Question: what do T2 + T3 actually contribute for A=1 (proton, neutron)
under the production Li_2^q tower form (post-#682)?

The audit doc reported a `KeyError at A=1` for T2+T3, but as of
PR #682 + #687 the per-gen witness `terms-2-3-atom-per-gen-mpfr-50dps`
DOES include A=1 entries with valid `wedderburn_vols`.  PR #684
identified the KeyError as a CONSUMER bug (mass-formula-6term-mpfr-50dps
was hardcoded to skip A=1) and fixed it.

This probe RE-COMPUTES T2 + T3 at A=1 using the canonical Li_2^q
form (single source of truth helper from #687) and reports the
contributions vs the CODATA target.

The mass-endomorphism tower at A=1 produces:

  T1 = ∏_g |V_g^full|    (descended Markov-trace product)
  T2 = Σ_g Li_2^q(|V_g^full|)
  T3 = z² · Σ_{i<j} Li_2^q(|V_i V_j|)

  T1 + T2 + T3 = full mass-endomorphism brane-tower

For proton (3 strands, 2 generators) and neutron (3 strands, 2 generators)
under the substrate Q_0:
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from mpmath import mp, mpf

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402
from _li_2_q_util import li_2_q  # noqa: E402
from codata_constants import (  # noqa: E402
    M_E_MEV, M_P_MEV_VALIDATION, M_N_MEV_VALIDATION,
)

mp.dps = 50

PER_GEN_WIT = HERE / "terms-2-3-atom-per-gen-mpfr-50dps.witness.json"
Q_WIT = HERE / "q-pinning-50-digit.witness.json"


def _fmt(x, dps=40):
    try:
        return mp.nstr(x, dps, strip_zeros=False)
    except Exception:
        return str(x)


def main() -> int:
    print("=" * 78)
    print("  m_p chain Item A: T2 + T3 at A=1 via Li_2^q (post-#682)")
    print("=" * 78)

    w = (WitnessBuilder("probe-proton-t2-t3-at-a1", engine="mpmath")
         .set_description(
             "m_p chain Item A from PR #671 audit: compute T2 and T3 at A=1 "
             "for proton + neutron under the canonical Li_2^q tower.  The "
             "audit reported KeyError; PR #684 identified that as a "
             "consumer bug.  Reports the actual contributions."))
    q_body = w.add_upstream(Q_WIT)
    pg_body = w.add_upstream(PER_GEN_WIT)

    q = mpf(q_body["derived_50_digit"]["q"])
    qi = mpf(1) / q
    z = mpf(1) / (mp.sqrt(q) + mp.sqrt(qi))
    print(f"  q_0 = {_fmt(q)}")
    print(f"  z   = {_fmt(z)}")
    print()

    rows = pg_body.get("data", {}).get("results") or pg_body.get("results", [])
    out = []
    for r in rows:
        atom = r.get("atom")
        if r.get("A") != 1 or atom not in ("proton", "neutron"):
            continue
        vols = [mpf(v["full"]) for v in r["wedderburn_vols"]]
        # T1
        t1 = mp.mpf(1)
        for v in vols:
            t1 = t1 * v
        t1 = mp.fabs(t1)
        # T2 = Σ_g Li_2^q(|V_g|)
        t2 = mp.mpf(0)
        for v in vols:
            t2 = t2 + li_2_q(mp.fabs(v), q, qi)
        # T3 = z² · Σ_{i<j} Li_2^q(|V_i V_j|)
        t3 = mp.mpf(0)
        for i, vi in enumerate(vols):
            for vj in vols[i + 1:]:
                t3 = t3 + li_2_q(mp.fabs(vi * vj), q, qi)
        t3 = t3 * z ** 2

        total = t1 + t2 + t3
        print(f"  {atom:10s}  n_gens={len(vols)}")
        print(f"    |V_g| = {[float(mp.fabs(v)) for v in vols]}")
        print(f"    T1 = ∏ |V_g|              = {_fmt(t1, 30)}")
        print(f"    T2 = Σ Li_2^q(|V|)        = {_fmt(t2, 30)}")
        print(f"    T3 = z²·Σ Li_2^q(|V·V|)   = {_fmt(t3, 30)}")
        print(f"    T1+T2+T3 (tower at A=1)   = {_fmt(total, 30)}")
        print()
        out.append({
            "atom": atom,
            "n_gens": len(vols),
            "vols_abs": [_fmt(mp.fabs(v)) for v in vols],
            "T1_50dps": _fmt(t1),
            "T2_li2q_50dps": _fmt(t2),
            "T3_li2q_50dps": _fmt(t3),
            "T1_plus_T2_plus_T3_50dps": _fmt(total),
        })

    # Compare T1+T2+T3 (dimensionless) · m_e to CODATA m_p / m_n
    print("  CODATA comparison (T_tower · m_e vs experimental mass):")
    m_e = mpf(str(M_E_MEV))
    codata_map = {
        "proton": mpf(str(M_P_MEV_VALIDATION)),
        "neutron": mpf(str(M_N_MEV_VALIDATION)),
    }
    for r in out:
        atom = r["atom"]
        tower = mpf(r["T1_plus_T2_plus_T3_50dps"])
        pred_MeV = tower * m_e
        codata = codata_map[atom]
        pct = float((pred_MeV - codata) / codata * 100)
        print(f"    {atom:10s} T_tower · m_e = {_fmt(pred_MeV, 12)} MeV  "
              f"(CODATA {codata}, residual {pct:+.4f} %)")
        r["pred_MeV_T_tower_times_m_e"] = _fmt(pred_MeV)
        r["codata_MeV"] = _fmt(codata)
        r["residual_pct"] = pct

    w.add_data("q_pinned", _fmt(q))
    w.add_data("z_markov", _fmt(z))
    w.add_data("rows", out)
    w.add_data("status",
               "T2 + T3 ARE computed at A=1 via canonical Li_2^q form.  "
               "The earlier KeyError was a consumer-side bug (per PR #684).  "
               "Tower at A=1 still under-shoots CODATA by ~99 % because the "
               "T1+T2+T3 contribution is structurally small at A=1 (single-"
               "particle truncation does not reproduce m_p/m_e ≈ 1836).  "
               "Resolution requires Items B (T5 categorical) and C (full "
               "Habiro residue) per PR #671 audit.")
    w.add_assertion("t2_t3_computable_at_a1",
                    computed=len(out), expected=2, tolerance=0)
    print(f"  Witness: {w.save().name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
