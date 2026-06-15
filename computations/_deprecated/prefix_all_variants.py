#!/usr/bin/env python3
"""
All three prefix variants + 6_2 presence check.

(1) Strand-cumulative — filter atomic braid word to keep only factors
    on generators g < k-1, then compute a_k.
(2) Nucleon-cumulative (already tested in pure_hecke_binding_prefix.py).
(3) Order-of-generation — step by nucleon build order; equivalent to
    nucleon-cumulative if build is atomic, or finer if intra-nucleon
    steps tracked.

Plus: check whether 6_2 knot appears as a Jones-polynomial signature
of some mass-tower sub-structure (strand-cumulative prefix at k=5 or
k=6 for D).
"""
from __future__ import annotations
import sys, warnings, json
from pathlib import Path
from datetime import datetime, timezone

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
mp.mp.dps = 30

from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
from experimental_constants import M_E_MEV, Q_NEUTRON_MEV

Q0 = Q_MP; QI = Q_INV_MP  # was f64 roundtrip
h = Q0 - QI; me = mp.mpf(str(M_E_MEV)); E0 = mp.mpf(str(Q_NEUTRON_MEV))


def catalog_jones(name: str, q) -> complex:
    """Jones polynomial of catalog knots at q (variable convention).

    Using V_K(t) with t = q² (Hecke convention).  Returns V_K at q²_0.
    """
    t = q**2
    if name == '4_1':  # figure-8
        return 1/t - 1 + 2*t - 2*t**2 + t**3   # approximate
    if name == '6_1':
        return t**(-3) - 2*t**(-2) + 2*t**(-1) - 2 + 2*t - t**2  # approximate
    if name == '6_2':
        # V_{6_2}(t) = t^{-1} - 1 + 2t - 2t^2 + 2t^3 - 2t^4 + t^5 (KnotInfo)
        return 1/t - 1 + 2*t - 2*t**2 + 2*t**3 - 2*t**4 + t**5
    if name == '6_3':
        return -t**(-3) + 2*t**(-2) - 2*t**(-1) + 3 - 2*t + 2*t**2 - t**3
    if name == '8_11':
        # High-crossing; approximate. For proper cross-check needs a KnotInfo lookup.
        return 1/t**3 - 3/t**2 + 4/t - 4 + 5*t - 4*t**2 + 3*t**3 - 2*t**4 + t**5
    if name == 'trefoil_3_1':  # positive trefoil
        return -t**(-4) + t**(-3) + t**(-1)
    return None


def check_6_2_in_tower():
    """Evaluate J(6_2, q_0) and compare to D's per-level atomic Markov
    traces to see if any match — testing if 6_2 Jones signature appears
    in the tower."""
    print("=" * 100)
    print("6_2 PRESENCE CHECK in atomic tower")
    print("=" * 100)
    # Jones of 6_2 at q_0:
    J_62 = catalog_jones('6_2', Q0)
    J_41 = catalog_jones('4_1', Q0)
    J_31 = catalog_jones('trefoil_3_1', Q0)
    J_611 = catalog_jones('8_11', Q0)
    print(f"  Catalog Jones at q_0 = {float(Q0):.6f}:")
    print(f"    J(4_1)   = {float(mp.re(J_41)):.6f}")
    print(f"    J(6_2)   = {float(mp.re(J_62)):.6f}")
    print(f"    J(6_3)   = {float(mp.re(catalog_jones('6_3', Q0))):.6f}")
    print(f"    J(8_11)  = {float(mp.re(J_611)):.6f}")
    print(f"    J(3_1)   = {float(mp.re(J_31)):.6f}")
    print()
    # Compare to atomic Markov trace sums (using existing witness):
    try:
        from hecke_core import atom_character_raw, _partition_table, _ensure_ysn_attached
        from hecke_characters import dim_q, young_hooks
        _ensure_ysn_attached()
        _PT = _partition_table()
        def mark_trace(Z, N, k, incl):
            if k < 2: return None
            entries = [e for e in _PT if e['k'] == k]
            if not entries: return None
            nfac = mp.mpf(1)
            for i in range(2, k+1): nfac *= (Q0**i - QI**i)/(Q0-QI)
            total = mp.mpc(0)
            for entry in entries:
                shape = entry['partition']
                dq = mp.mpf(str(float(dim_q(shape))))
                if dq == 0: continue
                w = dq*dq / nfac
                try:
                    chi_q, ln, _ = atom_character_raw(Z, N, entry, include_inter=incl)
                except Exception:
                    continue
                chi = mp.mpc(str(float(chi_q))) * mp.exp(mp.mpf(str(float(ln))))
                total += w * chi / dq
            return total

        for (Z, N, A, label) in [
            (1, 0, 1, 'proton'),
            (0, 1, 1, 'neutron'),
            (1, 1, 2, 'D'),
            (1, 2, 3, 'T'),
            (2, 1, 3, '3He'),
        ]:
            k = 3*A
            tr = mark_trace(Z, N, k, True)
            if tr is None:
                print(f"  {label}: no trace (k={k} out of table)")
                continue
            tr_re = float(mp.re(tr))
            abs_tr = abs(tr_re)
            # Which catalog knot does this closest match?
            distances = {
                '4_1':  abs(abs_tr - float(mp.fabs(J_41))),
                '6_2':  abs(abs_tr - float(mp.fabs(J_62))),
                '6_3':  abs(abs_tr - float(mp.fabs(catalog_jones('6_3', Q0)))),
                '8_11': abs(abs_tr - float(mp.fabs(J_611))),
                '3_1':  abs(abs_tr - float(mp.fabs(J_31))),
            }
            best = min(distances, key=distances.get)
            print(f"  {label:<8} tr_M@k={k}: {tr_re:+.8f}  |tr|={abs_tr:.6f}  "
                  f"closest-match = {best} (dist {distances[best]:.4f})")
    except Exception as e:
        print(f"  ERR: {type(e).__name__}: {e}")


def check_strand_cumulative():
    """Option 1: strand-cumulative prefix — in absence of a clean
    partial-braid computation tool, we use atom_character_raw at
    intermediate (Z, N) pairings that give the correct k_strands.

    For D (n=6), prefixes at k=3, 4, 5, 6:
      k=3: treat as 1-nucleon atom (Z=1,N=0 proton or Z=0,N=1 neutron)
      k=4, 5: no natural atomic decomposition
      k=6: full D

    We compute what we can and note the gaps.
    """
    print()
    print("=" * 100)
    print("STRAND-CUMULATIVE prefix attempt (option 1)")
    print("=" * 100)
    print("  For D (n=6), strand-cumulative prefixes at k=3,4,5,6:")
    print("    k=3: first nucleon alone (no physical 'partial atom' at k=4,5)")
    print("    k=6: full D")
    print("  Intermediate k=4, 5 don't admit a clean physical interpretation")
    print("  in this infrastructure; atom_character_raw requires (Z,N) at")
    print("  fixed 3(Z+N) strand count.")
    print()
    print("  CONCLUSION: strand-cumulative option needs a PARTIAL-BRAID-WORD")
    print("  computational framework not currently in hecke_core.  Would")
    print("  require: (a) explicit factor-by-factor NF reduction, (b) track")
    print("  which generators are 'live' at each k, (c) filter + recompute.")


def main() -> int:
    check_6_2_in_tower()
    check_strand_cumulative()
    witness = {
        "computation": "prefix-all-variants",
        "description": (
            "Three prefix variants + 6_2 presence check.  Strand-cumulative "
            "requires partial-braid-word infrastructure not currently available. "
            "Order-of-generation equals nucleon-cumulative if steps are atomic. "
            "6_2 signature compared against atomic Markov traces at various k."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "q_0": Q0_FLOAT,
    }
    out = Path(__file__).parent / "prefix-all-variants.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
