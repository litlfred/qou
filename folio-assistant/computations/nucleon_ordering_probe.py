#!/usr/bin/env python3
"""
Nucleon-ordering probe: how sensitive is tr_M to the p/n interleaving?

Background (session finding): two ordering conventions exist in the
codebase for the atom braid word:

- hecke_core.build_atom_nf line 870:      ordering = ['p']*Z + ['n']*N   →  ppnn
- mass_at_3A_proper.atom_braid_word_3A:   same (ppnn)
- hecke_core.atom_gen_chains:             k%2==0 → p if pc<Z else n     →  pnpn interleaved

After the electron-inclusion patch, D / T / 3He mass predictions
shifted asymmetrically: 3He IMPROVED (0.0035% → 0.0023%), D and T
WORSENED.  One hypothesis: nucleon ordering is a fragile choice.

This probe: for each atom (T, 3He, 4He, 6Li), enumerate all
distinct p/n permutations, compute tr_M per ordering, report the
spread.  If |Δ tr_M| across orderings is large relative to the
binding prediction, ordering matters physically.

Note: D has only one distinct ordering (Z=N=1 → pn), so no probe.
"""
from __future__ import annotations

import sys
import json
import time
import itertools
from pathlib import Path
from datetime import datetime, timezone

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as Q0, HA as h
from canonical_plus_multibrane import E_0_BETA_DECAY_MEV
from hecke_characters import partitions_of, dim_q, qfac
from mass_at_3A_proper import _cached_seminormal
from hecke_core import _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1


def atom_word_ordered(Z: int, N: int, ordering: list[str], *,
                         include_inter: bool = True,
                         include_electrons: bool = True,
                         m_pp: int = 1, m_pn: int = 1, m_nn: int = 1
                         ) -> list[tuple[float, float, int]]:
    """Atom braid word for a specified nucleon ordering.

    ordering: list like ['p','n','p','n'] specifying the order of
    nucleons along the strand axis.  Must contain exactly Z 'p' and
    N 'n' entries.
    """
    assert ordering.count('p') == Z, f"ordering has {ordering.count('p')} p, expected {Z}"
    assert ordering.count('n') == N, f"ordering has {ordering.count('n')} n, expected {N}"
    A = Z + N
    word: list[tuple[float, float, int]] = []
    for k, nuc in enumerate(ordering):
        intra_g0 = _PROTON_G0 if nuc == 'p' else _NEUTRON_G0
        intra_g1 = _PROTON_G1 if nuc == 'p' else _NEUTRON_G1
        base_g0 = 3 * k
        base_g1 = 3 * k + 1
        for (c, d) in intra_g0:
            word.append((float(c), float(d), base_g0))
        for (c, d) in intra_g1:
            word.append((float(c), float(d), base_g1))
        if include_inter and k < A - 1:
            nxt = ordering[k + 1]
            gen = 3 * k + 2
            if nuc == 'p' and nxt == 'p':
                c, d, m = 1.0, 0.0, m_pp
            elif nuc == 'n' and nxt == 'n':
                c, d, m = 1.0, -h, m_nn
            else:
                c, d, m = 1.0, -h / 2, m_pn
            for _ in range(m):
                word.append((c, d, gen))
    # Electrons at end (Z × σ₁⁻¹ at gen 1).
    if include_electrons:
        for _ in range(Z):
            word.append((1.0, -float(h), 1))
    return word


def trM_plancherel(Z: int, N: int, ordering: list[str],
                     include_inter: bool, include_electrons: bool = True
                     ) -> float:
    from scipy.sparse import issparse, eye as speye
    word = atom_word_ordered(Z, N, ordering,
                                 include_inter=include_inter,
                                 include_electrons=include_electrons)
    A = Z + N
    n = 3 * A
    nfac = qfac(n)
    total = 0.0
    for shape in partitions_of(n):
        sigmas, dim, _ = _cached_seminormal(shape)
        if dim == 0:
            continue
        dq = dim_q(shape)
        if dq == 0:
            continue
        w = (dq * dq) / nfac
        sparse = bool(sigmas) and issparse(sigmas[0])
        if sparse:
            prod = speye(dim, format='csr'); I = speye(dim, format='csr')
        else:
            prod = np.eye(dim); I = np.eye(dim)
        for (c, d, g) in word:
            if g < len(sigmas):
                prod = prod @ (c * sigmas[g] + d * I)
        chi = float(prod.diagonal().sum()) if sparse else float(np.trace(prod))
        total += w * chi / dim
    return total


def distinct_orderings(Z: int, N: int) -> list[list[str]]:
    """Return all distinct permutations of Z p's and N n's."""
    seen = set()
    out = []
    for perm in itertools.permutations(['p'] * Z + ['n'] * N):
        if perm not in seen:
            seen.add(perm)
            out.append(list(perm))
    return out


if __name__ == "__main__":
    ATOMS = [
        ("T",   1, 2,  8.481821),
        ("3He", 2, 1,  7.71804),
        ("4He", 2, 2, 28.295674),
    ]

    print("=" * 110)
    print("NUCLEON-ORDERING PROBE")
    print(f"q0 = {Q0}, E_0 = {E_0_BETA_DECAY_MEV} MeV, electrons=INCLUDED")
    print("=" * 110)

    results = []
    for name, Z, N, B_AME in ATOMS:
        A = Z + N
        Mtot = A * 938.272
        orderings = distinct_orderings(Z, N)
        print(f"\n{name} (Z={Z}, N={N}, A={A}, {len(orderings)} orderings)")
        print(f"  {'ordering':<20} {'trM_atom':>14} {'trM_free':>14} "
              f"{'B_pred':>10} {'err %':>10}  {'time':>6}")
        print("  " + "-" * 82)
        rows = []
        for ordering in orderings:
            t0 = time.time()
            trM_a = trM_plancherel(Z, N, ordering, include_inter=True)
            trM_f = trM_plancherel(Z, N, ordering, include_inter=False)
            B_pred = E_0_BETA_DECAY_MEV * (abs(trM_f) - abs(trM_a))
            err = abs(B_pred - B_AME) / Mtot * 100
            dt = time.time() - t0
            print(f"  {''.join(ordering):<20} {trM_a:>+14.6e} {trM_f:>+14.6e} "
                  f"{B_pred:>+10.4f} {err:>9.4f}%  {dt:>5.1f}s")
            rows.append({
                "ordering": ''.join(ordering),
                "trM_atom": trM_a, "trM_free": trM_f,
                "B_pred_MeV": B_pred, "err_pct": err,
                "time_sec": dt,
            })
        # Spread analysis
        trM_atoms = [r["trM_atom"] for r in rows]
        B_preds = [r["B_pred_MeV"] for r in rows]
        spread_trM = max(trM_atoms) - min(trM_atoms)
        spread_B = max(B_preds) - min(B_preds)
        print(f"\n  spread |Δ tr_M_atom| across orderings: {spread_trM:.3e}")
        print(f"  spread |Δ B_pred| across orderings:     {spread_B:.3f} MeV")
        print(f"  best ordering: {min(rows, key=lambda r: r['err_pct'])['ordering']} "
              f"(err {min(r['err_pct'] for r in rows):.4f}%)")
        results.append({"atom": name, "Z": Z, "N": N, "A": A,
                          "B_AME": B_AME, "orderings": rows,
                          "spread_trM_atom": spread_trM,
                          "spread_B_pred_MeV": spread_B})

    witness = {
        "computation": "nucleon-ordering-probe",
        "description": (
            "Sensitivity of the atom Markov trace to nucleon "
            "ordering along the strand axis.  For T, 3He, 4He, 6Li, "
            "enumerates all distinct p/n permutations and computes "
            "tr_M per ordering.  Spread across orderings quantifies "
            "the physical significance of the ordering choice."),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q0": Q0, "E_0_MeV": E_0_BETA_DECAY_MEV,
                          "electrons": True},
        "results": results,
    }
    out = Path(__file__).parent / "nucleon-ordering-probe.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
