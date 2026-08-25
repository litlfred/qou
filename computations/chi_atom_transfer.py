#!/usr/bin/env python3
"""chi_atom_transfer — scalable ATOM-config χ^λ via the LR transfer matrix.

Companion to `chi_free_via_lr` (the FREE config, already validated +
scalable). The atom config β_atom = β_{n_1}·I_1·β_{n_2}·I_2·…·β_{n_A}
adds the inter-nucleon interface crossings I_k = σ at each junction.
Those couple adjacent (H_3)-blocks, so χ^λ(β_atom) is NOT the simple
parabolic product of the free case — it needs the interface operator in
the LR-decomposed (running-multiplicity) basis.

Strategy (audit docs/audits/2026-06-09-large-A-chi-bottleneck-scaling-
plan.md §8a/§8b): an iterative transfer matrix over the running partition
ξ ⊢ 3k. At each step we fuse nucleon k+1 (a diagonal χ^{μ}-weighted op on
its H_3 block) and apply the junction interface operator, tracking the
running multiplicity. The per-λ cost is bounded by the running Bratteli
multiplicity (90M at ⁶Li, vs the n! = 6.4e15 per-basis-vector wall).

Status / build order (each piece validated against the cached atom
witnesses before the next is added):

  [1] foundation: nucleon-χ cache, Bratteli-path enumerator, and a
      ground-truth oracle (existing chi-{atom}-h{n} witnesses).         <-- THIS COMMIT
  [2] small-λ junction operator from char_fast seminormal + transfer
      contraction; validate A=2 (deuteron), A=3 (tritium/³He).
  [3] multiplicity-space (F-matrix) junction tensor that avoids the full
      d_λ matrix → A=4 (⁴He) and large A (⁶Li/⁷Li) at canonical MPFR.

NO float64 on the canonical path (owner ruling 2026-06-09): all numeric
work is mpmath at the 50-dps floor; char_fast f64 seminormal is used only
as a small-λ structural/validation aid in step [2], cross-checked at MPFR.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import json  # noqa: E402
import sys  # noqa: E402
from pathlib import Path  # noqa: E402

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402

from active_set_lr_profile import multi_lr  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

ZN = {
    "D": (1, 1), "T": (1, 2), "3He": (2, 1), "4He": (2, 2),
    "6Li": (3, 3), "7Li": (3, 4),
}

# Existing cached ATOM-config χ witnesses (validation oracle).
ATOM_WITNESS = {
    "D": "chi-deuteron-h6-at-q0-50dps.witness.json",
    "T": "chi-tritium-h9-at-q0-50dps.witness.json",
    "3He": "chi-helium-3-h9-at-q0-50dps.witness.json",
    "4He": "chi-helium-4-h12-at-q0-50dps.witness.json",
}


def load_nucleon_chi(dps: int = 50) -> dict[str, dict[tuple, "mp.mpf"]]:
    """6 base nucleon characters χ^{μ⊢3}(β_{p,n}) at MPFR (cached once)."""
    if mp.mp.dps < dps:
        mp.mp.dps = dps
    files = {"p": "chi-proton-h3-at-q0-50dps.witness.json",
             "n": "chi-neutron-h3-at-q0-50dps.witness.json"}
    out: dict[str, dict[tuple, mp.mpf]] = {}
    for nuc, f in files.items():
        d = json.loads((HERE / f).read_text())
        bp = d.get("by_partition") or d["data"]["by_partition"]
        out[nuc] = {tuple(p["partition"]): mp.mpf(str(p["chi_lambda"]))
                    for p in bp}
    return out


def load_atom_chi_oracle(atom: str, dps: int = 50) -> dict[tuple, "mp.mpf"]:
    """Ground-truth χ^λ(β_atom) from the existing cached witness (for
    validating the transfer-matrix output during build-up)."""
    if mp.mp.dps < dps:
        mp.mp.dps = dps
    f = ATOM_WITNESS.get(atom)
    if not f or not (HERE / f).exists():
        return {}
    d = json.loads((HERE / f).read_text())
    bp = d.get("by_partition") or d["data"]["by_partition"]
    return {tuple(p["partition"]): mp.mpf(str(p["chi_lambda"])) for p in bp}


def bratteli_state_sizes(A: int) -> list[tuple[int, int, int]]:
    """Per-level (k, p(3k), Σ_ξ running-multiplicity) — the transfer-matrix
    state size, i.e. how much the iterative calc must carry at each step.
    Cross-check of the audit §8b table.
    """
    from lr_coefficients import get_lr_table, partitions_of
    P3 = [tuple(p) for p in partitions_of(3)]
    m = {(): 1}
    rows = []
    for k in range(1, A + 1):
        nm: dict[tuple, int] = {}
        if k == 1:
            for mu in P3:
                nm[mu] = 1
        else:
            for (xi, nu, lam), c in get_lr_table(3 * (k - 1), 3).items():
                if c and xi in m and nu in P3:
                    nm[lam] = nm.get(lam, 0) + m[xi] * c
        m = nm
        rows.append((k, len(m), sum(m.values())))
    return rows


def _self_test() -> int:
    """Foundation sanity: caches load, enumerator matches the oracle's
    partition set, Bratteli sizes match the audit."""
    set_compute_dps()
    nuc = load_nucleon_chi()
    assert set(nuc) == {"p", "n"}, "nucleon cache species"
    assert len(nuc["p"]) == 3 and len(nuc["n"]) == 3, "3 partitions ⊢3 each"
    print(f"  nucleon cache: 6 base χ^(μ⊢3)(β_p,β_n) loaded "
          f"(p:{[mp.nstr(v,6) for v in nuc['p'].values()]})")
    for atom in ("D", "T", "3He", "4He"):
        Z, N = ZN[atom]
        n = 3 * (Z + N)
        oracle = load_atom_chi_oracle(atom)
        ml = multi_lr(Z + N)
        ok = set(ml) == set(oracle) if oracle else None
        print(f"  {atom:<4} n={n:<3} oracle λ={len(oracle):<4} "
              f"enumerator λ={len(ml):<4} partition-sets match: {ok}")
        if oracle:
            assert ok, f"{atom}: enumerator/oracle partition mismatch"
    print("  Bratteli transfer-state sizes (k, p(3k), Σ running-mult):")
    for k, pn, tot in bratteli_state_sizes(4):
        print(f"    k={k} p(3k)={pn:<4} Σ m_k[ξ]={tot:,}")
    print("  foundation OK")
    return 0


if __name__ == "__main__":
    sys.exit(_self_test())
