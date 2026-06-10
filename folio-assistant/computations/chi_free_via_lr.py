#!/usr/bin/env python3
"""chi_free_via_lr — FREE-config χ^λ(β_free) via nucleon-cache + active-set LR.

The free atomic config β_free = β_{nuc_1} · β_{nuc_2} · … · β_{nuc_A}
(disjoint nucleon blocks, no inter-nucleon interface) is a parabolic
element of H_{3A} in the Young subgroup (H_3)^A. Its character is the
LR / induction-product formula:

    χ^λ(β_free) = Σ_{(μ_1,…,μ_A): μ_i ⊢ 3}
                    c^λ_{μ_1…μ_A} · Π_i χ^{μ_i}(β_{nuc_i})

This NEVER materialises the d_λ-dim Hoefsmit matrix — it needs only:

  - the **6 cached nucleon characters** χ^{μ⊢3}(β_{p,n}) (from the
    chi-{proton,neutron}-h3 MPFR witnesses), computed once; and
  - the **active set** of λ (tuples with c^λ_{μ_1…μ_A} > 0), enumerated
    by `active_set_lr_profile.multi_lr`.

⇒ scales to any A in ~ms at MPFR (canonical tier), versus the O(L·d_λ²)
per-basis-vector path that hits a 3.6-year wall at ⁶Li
(docs/audits/2026-06-09-large-A-chi-bottleneck-scaling-plan.md §7a/§8).

This implements the FREE half of the binding χ via the LR decomposition.
The ATOM config additionally needs the inter-nucleon interface operator
(the H_9 A-extract validated at A=3 in PR #2080, generalised to A−1
nested interfaces — audit §8a) and is the next step.

Usage:
    python3 chi_free_via_lr.py            # validate D/3He/4He vs witnesses
    python3 chi_free_via_lr.py 6Li 7Li    # compute free χ for large A
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import json  # noqa: E402
import sys  # noqa: E402
import time  # noqa: E402
from pathlib import Path  # noqa: E402

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402

from active_set_lr_profile import multi_lr  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

ZN = {
    "D": (1, 1), "T": (1, 2), "3He": (2, 1), "4He": (2, 2),
    "6Li": (3, 3), "7Li": (3, 4), "9Be": (4, 5), "10B": (5, 5),
}

# atom → existing FREE-config witness (for validation), where present.
FREE_WITNESS = {
    "D": "chi-deuteron-free-h6-at-q0-50dps.witness.json",
    "3He": "chi-helium-3-free-h9-at-q0-50dps.witness.json",
    "4He": "chi-helium-4-free-h12-at-q0-50dps.witness.json",
}


def load_nucleon_chi(dps: int = 50) -> dict[str, dict[tuple, "mp.mpf"]]:
    """The 6 base nucleon characters χ^{μ⊢3}(β_{p,n}) at MPFR.

    Read from the chi-{proton,neutron}-h3-at-q0-50dps witnesses (the
    per-nucleon H_3 characters). Computed once; reused for every atom.
    """
    if mp.mp.dps < dps:
        mp.mp.dps = dps
    files = {"p": "chi-proton-h3-at-q0-50dps.witness.json",
             "n": "chi-neutron-h3-at-q0-50dps.witness.json"}
    cache: dict[str, dict[tuple, mp.mpf]] = {}
    for nuc, f in files.items():
        d = json.loads((HERE / f).read_text())
        bp = d.get("by_partition") or d["data"]["by_partition"]
        cache[nuc] = {tuple(p["partition"]): mp.mpf(str(p["chi_lambda"]))
                      for p in bp}
    return cache


def chi_free_lr(Z: int, N: int, *, dps: int = 50,
                nuc_chi: dict | None = None) -> dict[tuple, "mp.mpf"]:
    """`{λ ⊢ 3A: χ^λ(β_free)}` via the nucleon-cache + active-set LR sum."""
    if mp.mp.dps < dps:
        mp.mp.dps = dps
    A = Z + N
    if nuc_chi is None:
        nuc_chi = load_nucleon_chi(dps)
    ordering = ["p"] * Z + ["n"] * N
    active = multi_lr(A)  # {λ: {(μ_1,…,μ_A): c}}
    out: dict[tuple, mp.mpf] = {}
    for lam, tuples in active.items():
        s = mp.mpf(0)
        for tup, c in tuples.items():
            term = mp.mpf(c)
            for i, mu in enumerate(tup):
                term *= nuc_chi[ordering[i]][mu]
            s += term
        out[lam] = s
    return out


def main() -> int:
    atoms = sys.argv[1:] or list(FREE_WITNESS)
    nuc_chi = load_nucleon_chi()
    rows = []
    max_rel_overall = mp.mpf(0)
    for atom in atoms:
        if atom not in ZN:
            print(f"  unknown atom {atom!r}; skip"); continue
        Z, N = ZN[atom]
        t0 = time.time()
        chi = chi_free_lr(Z, N, nuc_chi=nuc_chi)
        wall = time.time() - t0
        n = 3 * (Z + N)
        row = {"atom": atom, "n_strands": n, "n_partitions": len(chi),
               "wall_sec": round(wall, 4)}
        # validate against the existing free witness, if present
        wf = FREE_WITNESS.get(atom)
        if wf and (HERE / wf).exists():
            ref = json.loads((HERE / wf).read_text())
            bp = ref.get("by_partition") or ref["data"]["by_partition"]
            refd = {tuple(p["partition"]): mp.mpf(str(p["chi_lambda"]))
                    for p in bp}
            max_rel = mp.mpf(0)
            for k, v in chi.items():
                if k in refd and refd[k] != 0:
                    max_rel = max(max_rel, abs(v - refd[k]) / abs(refd[k]))
                elif k in refd:
                    max_rel = max(max_rel, abs(v - refd[k]))
            row["max_rel_vs_witness"] = mp.nstr(max_rel, 4)
            row["validated"] = bool(max_rel < mp.mpf(10) ** -12)
            max_rel_overall = max(max_rel_overall, max_rel)
            tag = "OK" if row["validated"] else "MISMATCH"
            print(f"  {atom:<5} n={n:<3} p(n)={len(chi):<4} {wall*1000:7.1f} ms "
                  f"max_rel_vs_witness={mp.nstr(max_rel,3):>10}  {tag}")
        else:
            print(f"  {atom:<5} n={n:<3} p(n)={len(chi):<4} {wall*1000:7.1f} ms "
                  f"(no free witness — large-A compute)")
        rows.append(row)

    w = WitnessBuilder("chi-free-via-lr", engine="python")
    w.set_description(
        "FREE-config χ^λ(β_free) via nucleon-cache + active-set LR "
        "(parabolic character formula). Validates D/3He/4He against the "
        "existing chi-*-free MPFR witnesses and demonstrates the same "
        "compute at large A (6Li/7Li) in ms — the d_λ²-free scaling path "
        "(docs/audits/2026-06-09-large-A-chi-bottleneck-scaling-plan.md)."
    )
    w.add_data("rows", rows)
    w.add_data("nucleon_cache", "6 base χ^{μ⊢3}(β_{p,n}) from chi-{p,n}-h3 MPFR")
    validated = [r for r in rows if r.get("validated")]
    if validated:
        w.add_assertion(
            "free_lr_matches_witnesses_machine_eps",
            computed=float(max_rel_overall),
            expected=0.0,
            tolerance=1e-12,
            source="chi_free_lr vs chi-*-free witnesses",
        )
    w.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
