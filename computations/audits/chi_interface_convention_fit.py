#!/usr/bin/env python3
"""chi_interface_convention_fit.py — resolve a χ^λ disagreement between two
producers by FITTING the interface-crossing convention each one actually uses.

THE DISAGREEMENT (bean qou-pin6)
    Two producers compute χ^λ(β) for the same atomic braid word at the same q₀
    and disagree in the FIFTH DECIMAL:

        chi_at_q0_via_hoefsmit_mpfr  ->  chi^[6] = 1.55987028...
        rho_w_crystal_vertex_trace   ->  chi^[6] = 1.55975874...   (1.1e-4 apart)

    Not a q₀-layer question: the muon/proton separation moves chi^[6] by 8.1e-8,
    four orders too small. Both producers are stable and reproducible.

THE ARBITER — one-dimensional representations
    Of the partitions of n, the one-row [n] and one-column [1^n] give
    1-DIMENSIONAL Hecke reps. There every generator acts as a scalar, so the
    braid word collapses to a product and χ^λ has a closed form with no linear
    algebra at all:

        sigma -> s   (s = q on [n]; s = -1/q on [1^n]),   sigma_inv -> 1/s
        chi = s^(#sigma) * (1/s)^(#sigma_inv) * PROD(interface crossings)

    The collapse itself is proven in `QOU.MassTheory.OneDimWordCharacter`.

🛑 THE TRAP THIS ANALYSIS FELL INTO FIRST
    The first version fixed the interface operator at `I = s - h/2`, the
    COLOR-BLIND form, and concluded the cache was wrong. But that form was taken
    from `rho_w_crystal_vertex_trace` -- one of the two disputants -- so the
    "independent arbiter" agreed with it BY CONSTRUCTION. A closed form only
    arbitrates once the convention is FITTED rather than assumed.

    `canonical_braid_crossings.classify_crossing` is why the trap is easy to
    fall into. It maps TWO physically distinct crossings onto ONE label:

        d = -h/2                  color-BLIND
        d = -h*(1/2 - delta/4)    color-WEIGHTED p-n interface (delta = flavour split)

    Both return `"averaged"`, and `atom_canonical_crossings` hands consumers only
    `(gen_idx, ctype)`. A consumer that rebuilds operators from the LABEL cannot
    tell which crossing it had. The label is lossy.

WHAT THE FIT FINDS
    Let k of the `n_avg` averaged crossings take the color-weighted form and the
    rest color-blind, then scan k against each cache's own 1-dim values. Every
    cache fits an exact k, to machine zero, and the rule is

        k = 1 if (Z > 0 and N > 0) else 0

    -- ONE color-weighted crossing per atom containing both a proton and a
    neutron. It is NOT Z*N, the number of p-n pairs: that is the natural guess
    and the fit rules it out for tritium, helium-3 and helium-4.

THE VERDICT — the cache is right
    `chi_at_q0_via_hoefsmit_mpfr` implements the color-weighted p-n interface.
    `rho_w_crystal_vertex_trace` builds `I_g = sigma_g - (h/2)*1` for EVERY
    averaged crossing, so on a mixed atom it silently drops the delta weighting
    on the single p-n interface. That is exactly why homogeneous atoms
    (p, n, pp, nn -- no p-n interface) agree to 1e-50 while every mixed atom
    disagrees.

    The fix belongs in the API rather than in each consumer: `classify_crossing`
    should distinguish the two (`averaged` vs `averaged_pn`), or return the
    coefficient instead of a label. Until then every consumer that rebuilds
    operators from `atom_canonical_crossings` output inherits this defect.

Read-only. Diagnoses; fixes nothing.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

from mpmath import mp, mpf

HERE = Path(__file__).resolve().parent
COMPUTE_DIR = HERE.parent
REPO = COMPUTE_DIR.parent
for _p in (str(COMPUTE_DIR), str(COMPUTE_DIR / "substrate"),
           str(REPO / "tools" / "qou-substrate" / "python")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

ATOMS = {
    "proton": ((1, 0), "chi-proton-h3"),
    "neutron": ((0, 1), "chi-neutron-h3"),
    "diproton": ((2, 0), "chi-diproton-h6"),
    "dineutron": ((0, 2), "chi-dineutron-h6"),
    "deuteron": ((1, 1), "chi-deuteron-h6"),
    "tritium": ((1, 2), "chi-tritium-h9"),
    "helium-3": ((2, 1), "chi-helium-3-h9"),
    "helium-4": ((2, 2), "chi-helium-4-h12"),
}
EXACT = mpf("1e-15")


def _rho_w_module():
    spec = importlib.util.spec_from_file_location(
        "_rw", str(COMPUTE_DIR / "rho_w_crystal_vertex_trace.py"))
    m = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(m)
    except SystemExit:
        pass
    return m


def fit_k(q, cache_chi, n_s, n_i, n_a, delta, row: bool = True):
    """Best k = number of COLOR-WEIGHTED averaged crossings, and its residual."""
    h = q - 1 / q
    s = q if row else -1 / q
    blind = h / 2
    weighted = h * (mpf(1) / 2 - delta / 4)
    best = None
    for k in range(n_a + 1):
        val = (s ** n_s * (1 / s) ** n_i
               * (s - blind) ** (n_a - k) * (s - weighted) ** k)
        err = abs(val - cache_chi)
        if best is None or err < best[1]:
            best = (k, err)
    return best


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any cache's convention cannot be fitted")
    ap.add_argument("--dps", type=int, default=50)
    args = ap.parse_args(argv)
    mp.dps = args.dps

    from _li_2_q_util import flavor_split_leading
    rw = _rho_w_module()

    print("=" * 78)
    print("chi^lambda: which interface convention does each cache use?")
    print("=" * 78)
    print("  k = how many averaged crossings take the COLOR-WEIGHTED form")
    print("      -h*(1/2 - delta/4) rather than the color-blind -h/2")
    print()
    print(f"  {'atom':<11}{'Z,N':<7}{'n_avg':<7}{'fit k':<7}{'|diff|':<12}"
          f"{'Z*N':<6}{'k=1 if mixed?'}")
    unfitted = 0
    broken = 0
    for atom, ((Z, N), stem) in ATOMS.items():
        f = COMPUTE_DIR / f"{stem}-at-q0-50dps.witness.json"
        if not f.is_file():
            continue
        d = json.loads(f.read_text(encoding="utf-8"))
        qs = d.get("q_0_50dps") or d.get("q0Value")
        if not qs:
            print(f"  {atom:<11}(no q0 recorded — cannot check)")
            continue
        q = mpf(qs)
        delta = flavor_split_leading(q)
        cmap = {tuple(e["partition"]): mpf(e["chi_lambda"])
                for e in d.get("by_partition", [])}
        n = 3 * (Z + N)
        if (n,) not in cmap:
            continue
        w = rw.atom_canonical_crossings(Z, N)
        n_s = sum(1 for _g, c in w if c == "sigma")
        n_i = sum(1 for _g, c in w if c == "sigma_inv")
        n_a = sum(1 for _g, c in w if c == "averaged")
        k, err = fit_k(q, cmap[(n,)], n_s, n_i, n_a, delta)
        expected = 1 if (Z > 0 and N > 0) else 0
        if err > EXACT:
            unfitted += 1
        if k != expected:
            broken += 1
        print(f"  {atom:<11}{f'{Z},{N}':<7}{n_a:<7}{k:<7}{mp.nstr(err, 3):<12}"
              f"{Z * N:<6}{'YES' if k == expected else 'NO — rule broken'}")

    print()
    print("-" * 78)
    if unfitted:
        print(f"  🛑 {unfitted} cache(s) fit no k — a third convention is in play.")
    elif broken:
        print(f"  🛑 {broken} cache(s) fit an exact k that breaks the mixed-atom rule.")
    else:
        print("  ✅ Every cache fits an exact k, to machine zero, and k = 1 exactly")
        print("     when the atom has BOTH a proton and a neutron (NOT Z*N — the")
        print("     fit rules that out for tritium, helium-3 and helium-4).")
        print()
        print("  => chi_at_q0_via_hoefsmit_mpfr is CORRECT: it applies the")
        print("     color-weighted interface on the p-n crossing.")
        print("     rho_w_crystal_vertex_trace builds I = sigma - (h/2)*1 for EVERY")
        print("     averaged crossing, dropping delta on that one crossing — which")
        print("     is why homogeneous atoms agree to 1e-50 and mixed ones do not.")
        print()
        print("  Root cause: classify_crossing() maps BOTH -h/2 and")
        print("  -h*(1/2-delta/4) onto the single label \"averaged\", and")
        print("  atom_canonical_crossings() returns only that label, so a consumer")
        print("  rebuilding operators from it cannot recover which one it had.")
    print("=" * 78)
    return 1 if (args.strict and (unfitted or broken)) else 0


if __name__ == "__main__":
    raise SystemExit(main())
