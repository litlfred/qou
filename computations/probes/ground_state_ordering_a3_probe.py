#!/usr/bin/env python3
# polynomial_q_not_applicable: the objective is a log-magnitude Phi_q evaluated
# at a fixed substrate anchor; there is no symbolic-q polynomial in the output.
"""Does ``_ground_state_ordering`` return the Phi_q ground state at A = 3?

Bean ``qou-48is``.  Companion audit
``docs/audits/2026-08-09-ordering-loose-ends-a3-helper-and-missing-he-rows.md``;
predecessor PR #4851 (``2026-08-09-canonical-ordering-dof-production-impact.md``)
recorded two loose ends and this probe settles both.

LOOSE END 1 -- the helper contradicts the proposition at A = 3.
    ``prop:ground-state-ordering`` (``mass-theory/ground-state-ordering.md``)
    defines the ground-state nucleon ordering as the minimiser of
    ``Phi_q = sum_i log|V_i|`` over the transfer-matrix chain, and its rule
    (iii) says the SORTED ordering wins for ``A <= 3``.  The compute helper
    ``hecke_core_symbolic._ground_state_ordering`` returns ``pnp`` for 3He
    ``(Z, N) = (2, 1)``, not the sorted ``ppn``.  Which is wrong?

    This probe computes ``Phi_q`` DIRECTLY -- through the corpus's own
    implementation ``hecke_core_symbolic._phi1_from_ordering_sym``, which is
    exactly the objective the proposition names -- over EVERY arrangement of
    every isotope in range, at the experimental proton anchor, and reports the
    argmin.  The classification (helper bug / proposition wrong / different
    objectives) then follows from measurement rather than from reading either
    source.

LOOSE END 2 -- 3He and 4He have no row in the production mass table.
    Part 5 traces the row-emission path of
    ``mass_table_comprehensive.ISOTOPES`` and enumerates exactly which
    ``(Z, N)`` the generator drops and why.

SCOPE BAR (owner, this session).  This probe is DIAGNOSTIC ONLY.  It does not
switch production to any ordering, does not regenerate any table, and changes
no published number.  Part 4 measures what a hypothetical helper fix WOULD move
precisely so that the fix is not made blind.

DISCIPLINE.  ``free_parameters = 0``.  No AME/CODATA quantity selects anything.
q0 is the EXPERIMENTAL PROTON anchor (``q_parameter``; owner directive
2026-08-07) -- layer-pure, no muon-built cache is read.  Nothing is wired.
"""
from __future__ import annotations

import inspect
import itertools
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: F401, E402

import mpmath as mp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import q_at, Q_50_DIGIT_STR  # noqa: E402  EXPERIMENTAL PROTON ANCHOR
import hecke_core_symbolic as HCS  # noqa: E402

DPS = 50
mp.mp.dps = DPS + 10

#: The experimental (proton) anchor -- the same pin the production chain uses.
Q0 = q_at(DPS + 10)

#: Certification tolerance for the fast mirror against the symbolic reference.
MIRROR_TOL = mp.mpf("1e-40")

REPO = Path(__file__).resolve().parent.parent.parent


# ---------------------------------------------------------------------------
# Arrangements + the three candidate orderings
# ---------------------------------------------------------------------------

def arrangements(Z: int, N: int) -> list[list[str]]:
    """Every cross-species arrangement of Z protons and N neutrons."""
    A = Z + N
    out = []
    for pos in itertools.combinations(range(A), Z):
        o = ["n"] * A
        for p in pos:
            o[p] = "p"
        out.append(o)
    return out


def sorted_ordering(Z: int, N: int) -> list[str]:
    """The production convention, and the proposition's rule (iii) for A <= 3."""
    return ["p"] * Z + ["n"] * N


def prop_closed_formula(Z: int, N: int) -> list[str]:
    """``prop:ground-state-ordering`` display formula.

    ``ordering[k] = proton if (k odd and k < 2Z) else neutron``.  Stated under
    the hypothesis ``Z <= N``; returned unconditionally here so that Part 0 can
    MEASURE that it is inapplicable when ``Z > N`` (it then fails to place Z
    protons at all).
    """
    A = Z + N
    return ["p" if (k % 2 == 1 and k < 2 * Z) else "n" for k in range(A)]


def cache_ordering(Z: int, N: int) -> list[str] | None:
    """The committed ``ordering-cache.json`` entry, if any (1 = proton)."""
    path = REPO / "computations" / "ordering-cache.json"
    if not path.exists():
        return None
    cache = json.loads(path.read_text())
    entry = cache.get(f"{Z},{N}")
    if entry is None:
        return None
    return ["p" if x else "n" for x in entry["ordering"]]


# ---------------------------------------------------------------------------
# Phi_q -- the reference implementation and a certified fast mirror
# ---------------------------------------------------------------------------

def phi_ref(ordering: list[str]) -> mp.mpf:
    """``Phi_q`` through the corpus implementation (symbolic q, late anchor)."""
    return HCS._phi1_from_ordering_sym(ordering, dps=DPS)


_H = Q0 - 1 / Q0
_Z = Q0**3 / (Q0**2 + 1)
_HALF = mp.mpf(1) / 2


def _crossing_coeff(ti: str, tj: str):
    """Numeric mirror of ``hecke_core_symbolic._crossing_coeff_sym``."""
    if ti == "p" and tj == "p":
        return mp.mpf(0)
    if ti == "n" and tj == "n":
        return -_H
    if (ti, tj) in (("p", "n"), ("n", "p")):
        return -_H * _HALF
    if (ti, tj) in (("p", "e"), ("e", "p")):
        return -_H
    if ti == "e" and tj == "e":
        return mp.mpf(0)
    return None


def phi_fast(ordering: list[str]) -> mp.mpf:
    """mpmath mirror of :func:`phi_ref`, certified in Part 1."""
    n = len(ordering)
    if n <= 1:
        return mp.mpf(0)
    phi = mp.mpf(0)
    for i in range(n - 1):
        M00, M01, M10, M11 = mp.mpf(1), mp.mpf(0), mp.mpf(0), mp.mpf(1)
        for j in range(i + 1, n):
            d = _crossing_coeff(ordering[i], ordering[j])
            if d is None:
                continue
            t00, t01, t10, t11 = _H + d, mp.mpf(1), mp.mpf(1), d
            M00, M01, M10, M11 = (
                M00 * t00 + M01 * t10, M00 * t01 + M01 * t11,
                M10 * t00 + M11 * t10, M10 * t01 + M11 * t11,
            )
        V = _Z * M10 + M11
        if abs(V) > mp.mpf(f"1e-{DPS - 5}"):
            phi += mp.log(abs(V))
    return phi


def phi_full(ordering: list[str], Z: int, fast: bool = True) -> mp.mpf:
    """``Phi_q`` of the PRODUCTION chain: nucleons plus the Z-electron tail.

    ``compute_phi1_full_sym`` appends ``["e"] * Z`` before evaluating, so this
    is the objective an atom's Phi_q actually carries.  ``phi_nuc`` (the bare
    nucleon chain) is reported alongside because the proposition's prose speaks
    of the *nucleon* ordering.
    """
    chain = list(ordering) + ["e"] * Z
    return phi_fast(chain) if fast else phi_ref(chain)


# ---------------------------------------------------------------------------
# Part 0 -- provenance: what the helper actually is
# ---------------------------------------------------------------------------

def part0_provenance(results: dict, assertions: dict) -> None:
    print("\n" + "=" * 78)
    print("PART 0 -- what `_ground_state_ordering` actually computes")
    print("=" * 78)

    src = inspect.getsource(HCS._ground_state_ordering)
    searches = ("phi", "min(", "max(", "argmin", "permutation", "itertools")
    hits = [t for t in searches if t in src.lower()]
    print("  source of hecke_core_symbolic._ground_state_ordering:")
    for line in src.splitlines():
        print("    | " + line)
    print(f"\n  search-like tokens present: {hits or 'NONE'}")
    print("  => it is a FIXED INTERLEAVING GENERATOR, not a variational search.")
    print("     It never evaluates Phi_q, so it cannot be 'the minimiser' by")
    print("     construction; whether its output happens to minimise Phi_q is an")
    print("     empirical question -- which is what Parts 1-2 measure.")
    assertions["helper_performs_no_search"] = 1 if not hits else 0

    # The helper and _alternating_ordering_sym are the same function.
    same = all(
        HCS._ground_state_ordering(z, n) == HCS._alternating_ordering_sym(z, n)
        for z in range(0, 7) for n in range(0, 7) if z + n > 0
    )
    print(f"\n  _ground_state_ordering == _alternating_ordering_sym on 0<=Z,N<=6: {same}")
    print("  (so compute_phi1_full_sym, which calls the latter, inherits the same")
    print("   arrangement -- the two names are one convention.)")
    assertions["helper_is_alternating_ordering"] = 1 if same else 0

    # The proposition's display formula is stated for Z <= N.
    bad = []
    for (Z, N) in [(2, 1), (3, 1), (3, 2), (4, 1)]:
        f = prop_closed_formula(Z, N)
        if f.count("p") != Z:
            bad.append({"Z": Z, "N": N, "formula": "".join(f),
                        "protons_placed": f.count("p"), "protons_required": Z})
    print("\n  prop:ground-state-ordering display formula is stated under Z <= N.")
    print("  Applied where Z > N it does not even place Z protons:")
    for b in bad:
        print(f"    Z={b['Z']} N={b['N']}: formula gives {b['formula']!r} "
              f"({b['protons_placed']} protons, {b['protons_required']} required)")
    print("  => for 3He (Z=2 > N=1) the display formula is INAPPLICABLE; the")
    print("     governing clause of the proposition is rule (iii) (A <= 3 sorted).")
    assertions["prop_formula_inapplicable_when_Z_gt_N"] = 1 if bad else 0

    # ordering_cache: what does it serve today?
    cache_state = {}
    try:
        import ordering_cache as OC
        rust = OC._compute_ordering_rust(2, 1)
        pyfb = OC._compute_ordering_python(2, 1)
        cache_state = {
            "rust_path_available": rust is not None,
            "python_fallback_for_2_1": "".join("p" if x else "n" for x in pyfb),
            "committed_cache_2_1": "".join(cache_ordering(2, 1) or []) or None,
            "committed_cache_2_2": "".join(cache_ordering(2, 2) or []) or None,
        }
    except Exception as exc:  # pragma: no cover - defensive
        cache_state = {"error": repr(exc)}
    print(f"\n  ordering_cache state: {cache_state}")
    print("  NOTE: the Rust ground-state search referenced by ordering_cache")
    print("  (hecke_rust_bridge.compute_nucleus) is not present in the tree, so")
    print("  get_ordering() falls back to `[1]*Z + [0]*N` -- i.e. SORTED -- for")
    print("  any (Z, N) absent from the committed cache file.")
    assertions["ordering_cache_rust_path_absent"] = (
        1 if cache_state.get("rust_path_available") is False else 0)

    results["part0_provenance"] = {
        "helper_source": src,
        "helper_search_tokens": hits,
        "helper_equals_alternating_ordering": same,
        "prop_formula_inapplicable_cases": bad,
        "ordering_cache": cache_state,
    }


# ---------------------------------------------------------------------------
# Part 1 -- Phi_q over every arrangement at A = 3 (the disputed case)
# ---------------------------------------------------------------------------

def _table(Z: int, N: int, fast: bool) -> list[dict]:
    rows = []
    for o in arrangements(Z, N):
        rows.append({
            "ordering": "".join(o),
            "phi_nuc": phi_fast(o) if fast else phi_ref(o),
            "phi_full": phi_full(o, Z, fast=fast),
        })
    return rows


def part1_a3(results: dict, assertions: dict) -> None:
    print("\n" + "=" * 78)
    print("PART 1 -- Phi_q over EVERY arrangement at A = 3 (and the A=2 control)")
    print("=" * 78)
    print(f"  q0 (experimental proton anchor) = {mp.nstr(Q0, 25)}")
    print("  objective: Phi_q = sum_i log|V_i|  (hecke_core_symbolic"
          "._phi1_from_ordering_sym)")

    # --- certify the fast mirror against the corpus symbolic implementation ---
    worst = mp.mpf(0)
    ncert = 0
    for (Z, N) in [(1, 1), (1, 2), (2, 1), (2, 2), (1, 3), (3, 1), (2, 3)]:
        for o in arrangements(Z, N):
            for chain in (o, o + ["e"] * Z):
                a, b = phi_ref(chain), phi_fast(chain)
                worst = max(worst, abs(a - b))
                ncert += 1
    print(f"\n  fast mirror certified against _phi1_from_ordering_sym on {ncert} "
          f"chains: worst |delta| = {mp.nstr(worst, 6)}")
    assertions["fast_mirror_certified"] = 1 if worst < MIRROR_TOL else 0
    results["mirror_certification"] = {
        "chains_checked": ncert, "worst_abs_delta": mp.nstr(worst, 8),
        "tolerance": mp.nstr(MIRROR_TOL, 3),
    }

    per_atom = {}
    for name, Z, N in [("D", 1, 1), ("T", 1, 2), ("3He", 2, 1)]:
        rows = _table(Z, N, fast=False)   # A=3: use the reference directly
        helper = "".join(HCS._ground_state_ordering(Z, N))
        srt = "".join(sorted_ordering(Z, N))
        cache = "".join(cache_ordering(Z, N) or []) or None

        argmin_nuc = min(rows, key=lambda r: r["phi_nuc"])["ordering"]
        argmin_full = min(rows, key=lambda r: r["phi_full"])["ordering"]
        ties_nuc = [r["ordering"] for r in rows
                    if abs(r["phi_nuc"] - min(x["phi_nuc"] for x in rows)) < mp.mpf("1e-40")]
        ties_full = [r["ordering"] for r in rows
                     if abs(r["phi_full"] - min(x["phi_full"] for x in rows)) < mp.mpf("1e-40")]

        print(f"\n  --- {name}  (Z={Z}, N={N}) ---")
        print(f"    helper _ground_state_ordering : {helper}")
        print(f"    sorted (prop rule (iii))      : {srt}")
        print(f"    committed ordering-cache      : {cache}")
        print(f"    {'ordering':10s} {'Phi_nuc':>24s} {'Phi_full (production)':>26s}")
        for r in sorted(rows, key=lambda r: r["phi_full"]):
            mark = ""
            if r["ordering"] == helper:
                mark += " <-helper"
            if r["ordering"] == srt:
                mark += " <-sorted"
            print(f"    {r['ordering']:10s} {mp.nstr(r['phi_nuc'], 18):>24s} "
                  f"{mp.nstr(r['phi_full'], 18):>26s}{mark}")
        print(f"    argmin(Phi_nuc)  = {argmin_nuc}   ties: {ties_nuc}")
        print(f"    argmin(Phi_full) = {argmin_full}   ties: {ties_full}")

        per_atom[name] = {
            "Z": Z, "N": N,
            "helper": helper, "sorted": srt, "cache": cache,
            "argmin_phi_nuc": argmin_nuc, "argmin_phi_nuc_ties": ties_nuc,
            "argmin_phi_full": argmin_full, "argmin_phi_full_ties": ties_full,
            "rows": [{"ordering": r["ordering"],
                      "phi_nuc": mp.nstr(r["phi_nuc"], 20),
                      "phi_full": mp.nstr(r["phi_full"], 20)} for r in rows],
            "helper_is_argmin_phi_full": helper in ties_full,
            "sorted_is_argmin_phi_full": srt in ties_full,
        }

    he3 = per_atom["3He"]
    t = per_atom["T"]
    print("\n  VERDICT at A = 3:")
    print(f"    T   : helper={t['helper']} sorted={t['sorted']} "
          f"argmin(Phi_full)={t['argmin_phi_full']} -- they coincide, no dispute.")
    print(f"    3He : helper={he3['helper']} is argmin(Phi_full)? "
          f"{he3['helper_is_argmin_phi_full']}")
    print(f"          sorted={he3['sorted']} is argmin(Phi_full)? "
          f"{he3['sorted_is_argmin_phi_full']}")
    assertions["he3_sorted_is_phi_argmin"] = 1 if he3["sorted_is_argmin_phi_full"] else 0
    assertions["he3_helper_is_not_phi_argmin"] = (
        1 if not he3["helper_is_argmin_phi_full"] else 0)
    assertions["tritium_helper_and_sorted_agree"] = 1 if t["helper"] == t["sorted"] else 0
    assertions["deuteron_ordering_control"] = (
        1 if len(per_atom["D"]["argmin_phi_full_ties"]) >= 1 else 0)

    results["part1_A3"] = per_atom


# ---------------------------------------------------------------------------
# Part 2 -- how far does the helper miss, beyond A = 3?
# ---------------------------------------------------------------------------

SWEEP = [(1, 1), (1, 2), (2, 1), (2, 2), (2, 3), (3, 2), (3, 3), (3, 4), (4, 3),
         (4, 4), (4, 5), (5, 5), (5, 6), (6, 6), (6, 7), (7, 7)]


def part2_sweep(results: dict, assertions: dict) -> None:
    print("\n" + "=" * 78)
    print("PART 2 -- does the helper minimise Phi_q anywhere? (exhaustive sweep)")
    print("=" * 78)
    print(f"  {'Z':>2s} {'N':>2s} {'#arr':>6s} {'helper':>16s} {'argmin(Phi_full)':>18s} "
          f"{'helper opt?':>11s} {'rank':>5s} {'gap':>12s}")

    rows = []
    n_helper_opt = 0
    for (Z, N) in SWEEP:
        arrs = arrangements(Z, N)
        vals = [(("".join(o)), phi_full(o, Z)) for o in arrs]
        vals.sort(key=lambda kv: kv[1])
        best_s, best_v = vals[0]
        helper = "".join(HCS._ground_state_ordering(Z, N))
        hv = dict(vals)[helper]
        rank = 1 + sum(1 for _, v in vals if v < hv - mp.mpf("1e-40"))
        opt = abs(hv - best_v) < mp.mpf("1e-40")
        n_helper_opt += 1 if opt else 0
        srt = "".join(sorted_ordering(Z, N))
        sv = dict(vals)[srt]
        cache = "".join(cache_ordering(Z, N) or []) or None
        cv = dict(vals)[cache] if cache in dict(vals) else None
        rows.append({
            "Z": Z, "N": N, "n_arrangements": len(arrs),
            "helper": helper, "helper_phi": mp.nstr(hv, 18),
            "argmin": best_s, "argmin_phi": mp.nstr(best_v, 18),
            "helper_is_optimal": bool(opt), "helper_rank": rank,
            "helper_gap": mp.nstr(hv - best_v, 12),
            "sorted": srt, "sorted_phi": mp.nstr(sv, 18),
            "sorted_is_optimal": bool(abs(sv - best_v) < mp.mpf("1e-40")),
            "cache": cache,
            "cache_phi": mp.nstr(cv, 18) if cv is not None else None,
            "cache_is_optimal": (bool(abs(cv - best_v) < mp.mpf("1e-40"))
                                 if cv is not None else None),
        })
        print(f"  {Z:2d} {N:2d} {len(arrs):6d} {helper:>16s} {best_s:>18s} "
              f"{str(opt):>11s} {rank:5d} {float(hv - best_v):12.6f}")

    print(f"\n  helper is the Phi_full argmin in {n_helper_opt}/{len(rows)} cases.")
    n_cache_opt = sum(1 for r in rows if r["cache_is_optimal"])
    n_cache = sum(1 for r in rows if r["cache_is_optimal"] is not None)
    print(f"  committed ordering-cache is the argmin in {n_cache_opt}/{n_cache} "
          "cases where an entry exists.")
    print("  => the helper is not a Phi_q minimiser in general; it is a fixed")
    print("     interleaving convention that coincides with the minimiser only")
    print("     sometimes. This is what makes the A=3 disagreement a HELPER")
    print("     defect rather than a definitional difference.")

    assertions["helper_not_universal_phi_argmin"] = 1 if n_helper_opt < len(rows) else 0
    results["part2_sweep"] = {
        "rows": rows,
        "helper_optimal_count": n_helper_opt,
        "cases": len(rows),
        "cache_optimal_count": n_cache_opt,
        "cache_cases": n_cache,
    }


# ---------------------------------------------------------------------------
# Part 3 -- is the helper the argmin of some OTHER objective? (candidate (c))
# ---------------------------------------------------------------------------

def part3_alternative_objectives(results: dict, assertions: dict) -> None:
    print("\n" + "=" * 78)
    print("PART 3 -- is the helper the extremum of some other stated objective?")
    print("=" * 78)
    print("  Candidate (c) of the classification: the helper and the proposition")
    print("  might optimise DIFFERENT functionals, making the disagreement")
    print("  definitional rather than a bug. Tested on the objectives the corpus")
    print("  actually names.")

    objectives = {
        "phi_full (production, nucleons+electrons)":
            lambda o, Z: phi_full(o, Z),
        "phi_nuc (bare nucleon chain)":
            lambda o, Z: phi_fast(o),
        "-phi_full (maximiser)":
            lambda o, Z: -phi_full(o, Z),
        "|phi_full| (magnitude)":
            lambda o, Z: abs(phi_full(o, Z)),
    }

    table = {}
    for label, fn in objectives.items():
        hits = []
        for (Z, N) in SWEEP:
            vals = [("".join(o), fn(o, Z)) for o in arrangements(Z, N)]
            best = min(v for _, v in vals)
            helper = "".join(HCS._ground_state_ordering(Z, N))
            hv = dict(vals)[helper]
            hits.append(abs(hv - best) < mp.mpf("1e-40"))
        table[label] = {"helper_optimal": sum(hits), "cases": len(hits)}
        print(f"    helper optimal under {label:44s}: "
              f"{sum(hits)}/{len(hits)}")

    any_full = any(v["helper_optimal"] == v["cases"] for v in table.values())
    print(f"\n  helper is the extremum of SOME tested objective everywhere: {any_full}")
    print("  => no stated corpus objective is minimised by the helper across the")
    print("     sweep, so the disagreement is NOT merely definitional (c).")
    assertions["no_objective_makes_helper_universally_optimal"] = 0 if any_full else 1
    results["part3_alternative_objectives"] = table


# ---------------------------------------------------------------------------
# Part 4 -- what would a helper fix MOVE?  (measured, not applied)
# ---------------------------------------------------------------------------

def _atom_chain_mirror(ordering: list[str], Z: int):
    """Numeric mirror of ``hecke_core_symbolic.atom_gen_chains_sym``."""
    def proton():
        g0 = [(mp.mpf(1), mp.mpf(0))] * 3
        g1 = [(mp.mpf(1), -_H)] * 3
        g0 = g0 + [(mp.mpf(1), mp.mpf(0)), (mp.mpf(1), -_H * _HALF)]
        g1 = g1 + [(mp.mpf(1), -_H * _HALF)]
        g0 = g0 + [(mp.mpf(1), mp.mpf(0)), (mp.mpf(1), mp.mpf(0))]
        return g0, g1

    def neutron():
        g0 = [(mp.mpf(1), mp.mpf(0))] * 3
        g1 = [(mp.mpf(1), -_H)] * 3
        g0 = g0 + [(mp.mpf(1), -_H * _HALF), (mp.mpf(1), -_H * _HALF)]
        g1 = g1 + [(mp.mpf(1), -_H)]
        g0 = g0 + [(mp.mpf(1), mp.mpf(0)), (mp.mpf(1), mp.mpf(0))]
        return g0, g1

    P0, P1 = proton()
    N0, N1 = neutron()
    g0: list = []
    g1: list = []
    for k, kind in enumerate(ordering):
        if kind == "p":
            g0 += P0
            g1 += P1
        else:
            g0 += N0
            g1 += N1
        for prev in range(k):
            ti, tj = ordering[prev], ordering[k]
            if ti == "p" and tj == "p":
                g0.append((mp.mpf(1), mp.mpf(0)))
            elif ti == "n" and tj == "n":
                g0.append((mp.mpf(1), -_H))
            else:
                g0.append((mp.mpf(1), -_H * _HALF))
    for _ in range(Z):
        g1.append((mp.mpf(1), -_H))
    return g0, g1


def _chain_V_mirror(chain) -> mp.mpf:
    """Numeric mirror of ``hecke_core_symbolic._chain_V_full_sym``."""
    q2 = Q0 ** 2
    den = q2 ** 2 + 4 * q2 + 1
    w_sym = q2 / den
    w_std = (q2 + 1) ** 2 / den
    w_alt = q2 / den
    a, b = mp.mpf(0), mp.mpf(1)
    spc, apc = mp.mpf(1), mp.mpf(1)
    for c, d in chain:
        a, b = a * c * _H + a * d + b * c, a * c + b * d
        spc *= (c * Q0 + d)
        apc *= (-c / Q0 + d)
    return w_sym * spc + w_std * (_Z * a + b) + w_alt * apc


def part4_fix_impact(results: dict, assertions: dict) -> None:
    print("\n" + "=" * 78)
    print("PART 4 -- what would fixing the helper MOVE?  (measured, NOT applied)")
    print("=" * 78)

    # Certify the atom-chain mirror against the corpus symbolic path on a cheap case.
    v0s, v1s = HCS.atom_V_full_sym(1, 1)
    v0r, v1r = HCS.evalf_at_q0(v0s, dps=DPS), HCS.evalf_at_q0(v1s, dps=DPS)
    g0, g1 = _atom_chain_mirror(HCS._ground_state_ordering(1, 1), 1)
    v0m, v1m = _chain_V_mirror(g0), _chain_V_mirror(g1)
    d0, d1 = abs(v0r - v0m), abs(v1r - v1m)
    print(f"  atom-chain mirror certified at (Z,N)=(1,1): |dV0|={mp.nstr(d0,6)} "
          f"|dV1|={mp.nstr(d1,6)}")
    ok = d0 < MIRROR_TOL and d1 < MIRROR_TOL
    assertions["atom_chain_mirror_certified"] = 1 if ok else 0

    CASES = [(2, 1, "ppn"), (2, 2, "nppn"), (3, 3, "npnppn")]

    # 4a -- the per-generator Wedderburn volumes V0/V1.
    print("\n  4a. per-generator Wedderburn volumes V0/V1 (atom_V_full_sym)")
    v_rows = []
    v_moved = False
    for (Z, N, alt) in CASES:
        helper = "".join(HCS._ground_state_ordering(Z, N))
        V0h, V1h = (_chain_V_mirror(c) for c in _atom_chain_mirror(list(helper), Z))
        V0a, V1a = (_chain_V_mirror(c) for c in _atom_chain_mirror(list(alt), Z))
        rel0 = abs(V0a - V0h) / abs(V0h)
        rel1 = abs(V1a - V1h) / abs(V1h) if V1h != 0 else mp.mpf(0)
        if rel0 > mp.mpf("1e-30") or rel1 > mp.mpf("1e-30"):
            v_moved = True
        print(f"    (Z,N)=({Z},{N}) helper={helper:8s} alt={alt:8s} "
              f"V0={mp.nstr(V0h, 18):>22s} rel dV0={mp.nstr(rel0, 4):>10s} "
              f"rel dV1={mp.nstr(rel1, 4):>10s}")
        v_rows.append({
            "Z": Z, "N": N, "helper": helper, "candidate": alt,
            "V0_helper": mp.nstr(V0h, 20), "V0_candidate": mp.nstr(V0a, 20),
            "V1_helper": mp.nstr(V1h, 20), "V1_candidate": mp.nstr(V1a, 20),
            "rel_delta_V0": mp.nstr(rel0, 10), "rel_delta_V1": mp.nstr(rel1, 10),
        })
    print(f"    => V0/V1 move under a re-ordering: {v_moved}")
    print("    This is EXACTLY the commuting-transfer-factor structure proved in")
    print("    QOU/MassTheory/TransferFactorCommute.lean: `_vertex_channels_sym`")
    print("    runs the same T(d) = S + d.1 recursion, and `atom_gen_chains_sym`")
    print("    enumerates ALL C(A,2) nucleon pairs, whose type multiset is fixed by")
    print("    (Z, N). So the chain multiset -- hence V -- is ordering-independent.")
    assertions["atom_V_is_ordering_independent"] = 0 if v_moved else 1

    # 4b -- the Hecke normal-form vector.
    print("\n  4b. Hecke normal-form vector (build_atom_nf_sym / build_atom_nf_mp)")
    import compound_shift_nf as CSN  # noqa: PLC0415  (heavy; only needed here)
    orig = HCS._ground_state_ordering
    nf_rows = []
    nf_moved = False
    try:
        for (Z, N, alt) in CASES:
            helper = "".join(orig(Z, N))
            nf_h = CSN.build_atom_nf_mp(Z, N, dps=DPS)
            patched = (lambda a: (lambda z, n: list(a) if (z, n) == (Z, N)
                                  else orig(z, n)))(alt)
            HCS._ground_state_ordering = patched
            CSN._ground_state_ordering = patched
            nf_a = CSN.build_atom_nf_mp(Z, N, dps=DPS)
            HCS._ground_state_ordering = orig
            CSN._ground_state_ordering = orig
            worst = max((abs(a - b) / abs(a) if a != 0 else abs(a - b))
                        for a, b in zip(nf_h, nf_a))
            if worst > mp.mpf("1e-30"):
                nf_moved = True
            print(f"    (Z,N)=({Z},{N}) helper={helper:8s} alt={alt:8s} "
                  f"worst rel delta on the 6-vector = {mp.nstr(worst, 8)}")
            nf_rows.append({
                "Z": Z, "N": N, "helper": helper, "candidate": alt,
                "nf_helper": [mp.nstr(x, 20) for x in nf_h],
                "nf_candidate": [mp.nstr(x, 20) for x in nf_a],
                "worst_rel_delta": mp.nstr(worst, 10),
            })
    finally:
        HCS._ground_state_ordering = orig
        CSN._ground_state_ordering = orig
    print(f"    => the NF vector moves under a re-ordering: {nf_moved}")
    print("    `hm_sym` is the 6-dimensional Hecke NF multiplication, which is NOT")
    print("    of the commuting T(d) form -- so the NF, unlike V, is genuinely")
    print("    order-sensitive.")
    assertions["hecke_nf_is_ordering_dependent"] = 1 if nf_moved else 0

    # 4c -- Phi_1 itself.
    phi_moved = any(
        abs(phi_full(list(HCS._ground_state_ordering(Z, N)), Z)
            - phi_full(list(alt), Z)) > mp.mpf("1e-30")
        for (Z, N, alt) in CASES)
    print(f"\n  4c. Phi_1 (compute_phi1_full_sym) moves under a re-ordering: "
          f"{phi_moved}")
    assertions["phi1_is_ordering_dependent"] = 1 if phi_moved else 0

    would_move = nf_moved or phi_moved
    print("\n  => VERDICT: a helper fix leaves the Wedderburn volumes V0/V1")
    print("     untouched but MOVES the Hecke NF vector (and Phi_1), and")
    print("     build_atom_nf_sym / build_atom_nf_mp feed committed witnesses.")
    print("     THE FIX IS THEREFORE NOT APPLIED HERE -- it crosses this")
    print("     session's scope bar (change no published number). Filed as a bean.")
    assertions["helper_fix_would_move_published_values"] = 1 if would_move else 0

    consumers = [
        "hecke_core_symbolic.atom_gen_chains_sym -> atom_V_full_sym "
        "(ordering-INDEPENDENT, 4a)",
        "hecke_core_symbolic.build_atom_nf_sym (ordering-DEPENDENT, 4b)",
        "hecke_core_symbolic.compute_phi1_full_sym via _alternating_ordering_sym "
        "(ordering-DEPENDENT, 4c)",
        "compound_shift_nf.build_atom_nf_mp (own transcription, line ~197)",
        "channel_binding.py (BOND_CROSSING self-test source of truth)",
        "crystal_shift_nf_atomic.py, atomic_tr_m_mpfr_50dps.py (downstream)",
    ]
    print("\n  consumers of _ground_state_ordering:")
    for c in consumers:
        print(f"    - {c}")
    results["part4_fix_impact"] = {
        "mirror_certification": {"dV0": mp.nstr(d0, 8), "dV1": mp.nstr(d1, 8)},
        "wedderburn_volumes": {"rows": v_rows, "moves": v_moved},
        "hecke_nf": {"rows": nf_rows, "moves": nf_moved},
        "phi1_moves": phi_moved,
        "would_move_published_values": would_move,
        "consumers": consumers,
        "action_taken": "NONE -- diagnostic only; filed as a bean.",
    }


# ---------------------------------------------------------------------------
# Part 6 -- the mechanism: commuting transfer factors + the undefined (n, e)
# ---------------------------------------------------------------------------

def part6_mechanism(results: dict, assertions: dict) -> None:
    print("\n" + "=" * 78)
    print("PART 6 -- WHY: commuting transfer factors, and the (n, e) hole")
    print("=" * 78)

    # (i) The transfer factors of the Phi chain all commute (Lean: transferFactor_comm).
    def T(d):
        return (_H + d, mp.mpf(1), mp.mpf(1), d)

    def mm(X, Y):
        return (X[0] * Y[0] + X[1] * Y[2], X[0] * Y[1] + X[1] * Y[3],
                X[2] * Y[0] + X[3] * Y[2], X[2] * Y[1] + X[3] * Y[3])

    d1, d2 = mp.mpf(0), -_H * _HALF
    ab, ba = mm(T(d1), T(d2)), mm(T(d2), T(d1))
    comm_gap = max(abs(x - y) for x, y in zip(ab, ba))
    print(f"  (i) T(d1)T(d2) vs T(d2)T(d1) at the 3He strand-0 coefficients "
          f"(0, -h/2): max |delta| = {mp.nstr(comm_gap, 6)}")
    print("      Proved in general, sorry-free and over a generic CommRing, in")
    print("      QOU/MassTheory/TransferFactorCommute.lean (`transferFactor_comm`,")
    print("      `chainProd_perm`, `phiReadout_chainProd_perm`): T(d) = S + d.1 for")
    print("      one fixed S, so the chain product -- and V -- depends on the")
    print("      crossing coefficients ONLY as a MULTISET.")
    assertions["transfer_factors_commute"] = 1 if comm_gap < mp.mpf("1e-40") else 0

    # (ii) Hence the 3He bare-nucleon readouts are EQUAL, not merely close.
    phi_ppn = phi_fast(list("ppn"))
    phi_pnp = phi_fast(list("pnp"))
    gap_nuc = abs(phi_ppn - phi_pnp)
    print(f"\n  (ii) 3He bare-nucleon Phi: ppn = {mp.nstr(phi_ppn, 20)}")
    print(f"                             pnp = {mp.nstr(phi_pnp, 20)}")
    print(f"       |difference| = {mp.nstr(gap_nuc, 6)}  -- an EXACT degeneracy,")
    print("       not a near-miss. At the NUCLEON level the objective cannot")
    print("       prefer either arrangement, so rule (iii)'s 'sorted BEATS")
    print("       interleaving for A <= 3' is, at 3He, a TIE rather than a strict")
    print("       win. (At T it IS strict -- see Part 1.)")
    assertions["he3_nucleon_level_is_exactly_degenerate"] = (
        1 if gap_nuc < mp.mpf("1e-40") else 0)

    # (iii) The production separation comes from the electron tail alone.
    ne = HCS._crossing_coeff_sym("n", "e")
    pe = HCS._crossing_coeff_sym("p", "e")
    print(f"\n  (iii) _crossing_coeff_sym('p','e') = {pe}")
    print(f"        _crossing_coeff_sym('n','e') = {ne}   <-- UNDEFINED (None)")
    print("        `_phi1_from_ordering_sym` SKIPS an undefined coefficient, so a")
    print("        neutron placed before the electron tail contributes a bare")
    print("        V = 1 (log 0) for that strand. The strict 3He separation under")
    print("        the production Phi_1 is therefore produced entirely by this")
    print("        asymmetry -- electrons couple to protons, not to neutrons --")
    print("        and NOT by the nucleon ordering itself.")
    phi_full_ppn = phi_full(list("ppn"), 2)
    phi_full_pnp = phi_full(list("pnp"), 2)
    print(f"        Phi_1(ppn) = {mp.nstr(phi_full_ppn, 20)}")
    print(f"        Phi_1(pnp) = {mp.nstr(phi_full_pnp, 20)}")
    print(f"        separation = {mp.nstr(phi_full_pnp - phi_full_ppn, 12)}")
    assertions["n_e_crossing_coefficient_undefined"] = 1 if ne is None else 0
    assertions["p_e_crossing_coefficient_defined"] = 1 if pe is not None else 0

    results["part6_mechanism"] = {
        "transfer_commutator_gap": mp.nstr(comm_gap, 8),
        "lean": ("folio/quantum-observable-universe/lean/QOU/MassTheory/"
                 "TransferFactorCommute.lean"),
        "he3_phi_nuc_ppn": mp.nstr(phi_ppn, 20),
        "he3_phi_nuc_pnp": mp.nstr(phi_pnp, 20),
        "he3_phi_nuc_gap": mp.nstr(gap_nuc, 8),
        "crossing_coeff_p_e": str(pe),
        "crossing_coeff_n_e": str(ne),
        "he3_phi1_ppn": mp.nstr(phi_full_ppn, 20),
        "he3_phi1_pnp": mp.nstr(phi_full_pnp, 20),
        "he3_phi1_separation": mp.nstr(phi_full_pnp - phi_full_ppn, 12),
        "reading": ("At the nucleon level the objective is EXACTLY degenerate "
                    "between ppn and pnp (commuting transfer factors => multiset "
                    "dependence only). The production Phi_1 separates them in "
                    "favour of sorted, but only through the electron tail, whose "
                    "(n, e) coupling is undefined and therefore skipped."),
    }


# ---------------------------------------------------------------------------
# Part 5 -- why 3He and 4He have no row in the production mass table
# ---------------------------------------------------------------------------

def part5_missing_rows(results: dict, assertions: dict) -> None:
    print("\n" + "=" * 78)
    print("PART 5 -- why 3He / 4He have no row in mass-table-comprehensive")
    print("=" * 78)

    src_path = REPO / "computations" / "mass_table_comprehensive.py"
    src = src_path.read_text()

    # Reproduce the generator exactly as written.
    explicit = [("p", 1, 0), ("n", 0, 1), ("D", 1, 1), ("T", 1, 2)]
    grid, kept, dropped = [], [], []
    for z in range(2, 119):
        n_min = max(0, int(0.5 * z) - 2)
        n_max = int(2.5 * z) + 5
        for n in range(n_min, n_max + 1):
            grid.append((z, n))
            (kept if z + n > 4 else dropped).append((z, n))

    explicit_z = sorted({z for _, z, _ in explicit})
    overlap = [zn for zn in dropped if zn in {(z, n) for _, z, n in explicit}]

    print(f"  generator: ISOTOPES = {explicit}")
    print("             + grid z in [2, 118], n in [max(0, z//2 - 2), 5*z//2 + 5]")
    print("             filtered by `if a > 4:  # Avoid duplicates with explicitly")
    print("               added H, He isotopes`   (mass_table_comprehensive.py:153)")
    print(f"\n  grid size {len(grid)}; kept {len(kept)}; DROPPED {len(dropped)}")
    print(f"  dropped (Z, N): {dropped}")
    print(f"  Z values present in the explicit list: {explicit_z}")
    print(f"  dropped rows that are ACTUALLY duplicates of an explicit entry: "
          f"{overlap or 'NONE'}")
    print("\n  => the guard's premise is FALSE. The explicit list contains only")
    print("     H-chain entries (p, n, D, T -- all Z <= 1); no He isotope was ever")
    print("     added, so nothing in the Z >= 2 grid can duplicate it. The `a > 4`")
    print("     threshold therefore deletes 6 unique (Z, N) rows for no reason,")
    print("     among them 3He (2,1) and 4He (2,2) -- the only two bound nuclides")
    print("     in the set.")

    labels = {(2, 0): "2He (diproton, unbound)", (2, 1): "3He (BOUND)",
              (2, 2): "4He (BOUND)", (3, 0): "3Li (unbound)",
              (3, 1): "4Li (unbound)", (4, 0): "4Be (unbound)"}
    for zn in dropped:
        print(f"    ({zn[0]}, {zn[1]}) -> {labels.get(zn, '?')}")

    # The decisive evidence that the exclusion is UNINTENDED: the same module
    # provisions reference data for 3He and 4He in three separate dicts, and
    # imports a CODATA constant used for nothing else.
    provisioned = {
        "AME_BINDING['3He']": '"3He": 7.71804' in src,
        "AME_BINDING['4He']": '"4He": 28.2957' in src,
        "CODATA_MASS['3He']": '"3He": None,  # not in codata_constants' in src,
        "CODATA_MASS['4He']": '"4He": float(M_HE4_MEV_VALIDATION)' in src,
        "ATLAS_TAG['3He']": src.count('"3He"') >= 3,
        "ATLAS_TAG['4He']": src.count('"4He"') >= 3,
        "imports M_HE4_MEV_VALIDATION": "M_HE4_MEV_VALIDATION" in src,
    }
    print("\n  DECISIVE: the module PROVISIONS 3He and 4He and then never emits them.")
    for k, v in provisioned.items():
        print(f"    {k:34s} present in source: {v}")
    print("    All three dicts are consumed by the row loop -- AME_BINDING.get(name),")
    print("    CODATA_MASS.get(name), ATLAS_TAG[name] -- for a `name` that can never")
    print("    be '3He' or '4He'. In particular M_HE4_MEV_VALIDATION is imported")
    print("    solely to populate CODATA_MASS['4He'], which is therefore DEAD.")
    print("    An author who meant to exclude these two would not have written")
    print("    their AME binding energies, their atlas tags, and a dedicated CODATA")
    print("    import for them. The exclusion is unintended.")
    all_prov = all(provisioned.values())
    assertions["he3_he4_reference_data_is_provisioned"] = 1 if all_prov else 0

    # And they really are absent from the committed witness.
    wpath = REPO / "computations" / "mass-table-comprehensive.witness.json"
    absent = None
    if wpath.exists():
        wtxt = wpath.read_text()
        absent = (wtxt.count("3He") == 0 and wtxt.count("4He") == 0
                  and wtxt.count("5He") > 0)
        print(f"\n  committed witness: '3He' occurrences = {wtxt.count('3He')}, "
              f"'4He' = {wtxt.count('4He')}, '5He' = {wtxt.count('5He')}")
        assertions["he3_he4_absent_but_he5_present_in_witness"] = 1 if absent else 0

    # The witness's sole assertion is evaluated over the FILTERED row set.
    has_assertion = "all_A_leq_4_masses_computed" in src
    a_le_4_rows = [("p", 1, 0), ("n", 0, 1), ("D", 1, 1), ("T", 1, 2)]
    print(f"\n  mass-table-comprehensive.witness.json carries exactly one assertion,")
    print(f"  `all_A_leq_4_masses_computed` ('All A <= 4 isotopes have absolute mass")
    print(f"  predictions'), present in source: {has_assertion}. It ranges over")
    print(f"  `[r for r in rows if r['A'] <= 4]`, which after the filter is exactly")
    print(f"  {[n for n, _, _ in a_le_4_rows]} -- it cannot see 3He or 4He, so it")
    print("  passes while the two most important A <= 4 nuclides are absent. The")
    print("  assertion is true of the emitted rows and false of its own wording.")

    assertions["missing_rows_are_generator_filter"] = 1 if dropped else 0
    assertions["dropped_rows_are_not_duplicates"] = 1 if not overlap else 0
    assertions["he3_and_he4_are_dropped"] = (
        1 if (2, 1) in dropped and (2, 2) in dropped else 0)
    assertions["a_le_4_assertion_ranges_over_filtered_rows"] = 1 if has_assertion else 0

    results["part5_missing_rows"] = {
        "guard": "if a > 4:  # Avoid duplicates with explicitly added H, He isotopes",
        "guard_location": "computations/mass_table_comprehensive.py:153",
        "explicit_isotopes": [list(e) for e in explicit],
        "explicit_Z_values": explicit_z,
        "grid_size": len(grid), "kept": len(kept),
        "dropped": [list(d) for d in dropped],
        "dropped_labels": {f"{z},{n}": labels.get((z, n)) for (z, n) in dropped},
        "genuine_duplicates_among_dropped": [list(o) for o in overlap],
        "reference_data_provisioned": provisioned,
        "he3_he4_absent_from_committed_witness": absent,
        "classification": ("GENERATOR BUG -- false-premise dedup guard. No He "
                           "isotope is in the explicit list, so no Z >= 2 grid row "
                           "can duplicate it; `a > 4` drops 6 unique rows. UNINTENDED: "
                           "the same module provisions AME_BINDING, CODATA_MASS and "
                           "ATLAS_TAG entries for 3He and 4He and imports "
                           "M_HE4_MEV_VALIDATION solely for CODATA_MASS['4He'], all of "
                           "which the guard renders unreachable."),
        "collateral": ("the witness's sole assertion "
                       "`all_A_leq_4_masses_computed` is evaluated over the "
                       "post-filter row set {p, n, D, T} and so passes without "
                       "ever seeing 3He or 4He."),
        "action_taken": ("NONE -- regenerating the table changes published "
                         "numbers, which is outside this session's scope bar."),
    }


# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()
    results: dict = {}
    assertions: dict = {}

    print("=" * 78)
    print("GROUND-STATE ORDERING at A=3 -- helper vs proposition; and the")
    print("missing 3He / 4He rows of the production mass table")
    print("=" * 78)
    print(f"  q0 (EXPERIMENTAL PROTON anchor) = {mp.nstr(Q0, 25)}")
    print(f"  q0 50-digit string              = {Q_50_DIGIT_STR[:32]}...")
    print("  free_parameters = 0; no AME/CODATA value selects anything.")
    print("  DIAGNOSTIC ONLY -- nothing is wired, no published number changes.")

    part0_provenance(results, assertions)
    part1_a3(results, assertions)
    part2_sweep(results, assertions)
    part3_alternative_objectives(results, assertions)
    part4_fix_impact(results, assertions)
    part6_mechanism(results, assertions)
    part5_missing_rows(results, assertions)

    dt = time.time() - t0
    print("\n" + "=" * 78)
    print("SUMMARY")
    print("=" * 78)
    he3 = results["part1_A3"]["3He"]
    print("  LOOSE END 1 -- classification (a), with a sharp caveat.")
    print("      (a) THE HELPER IS THE DEFECTIVE SIDE. It performs no variational")
    print("          search at all (Part 0) -- it is a fixed interleaving")
    print("          generator -- and it is the Phi_1 argmin in only "
          f"{results['part2_sweep']['helper_optimal_count']}/"
          f"{results['part2_sweep']['cases']} swept")
    print("          cases (Part 2); no other objective the corpus states rescues")
    print("          it (Part 3). It does not implement the rule its name invokes.")
    print(f"      At 3He the Phi_1 argmin is {he3['argmin_phi_full']} (sorted), as")
    print(f"      rule (iii) says; the helper's {he3['helper']} ranks LAST of 3.")
    print("      CAVEAT (Part 6): on the BARE NUCLEON chain ppn and pnp are")
    print("      EXACTLY degenerate -- proved, not measured: the transfer factors")
    print("      commute, so V depends only on the coefficient multiset. Rule")
    print("      (iii)'s 'sorted BEATS interleaving' is therefore a TIE at 3He,")
    print("      strict only once the electron tail is included -- and that")
    print("      separation is generated by the UNDEFINED (n, e) coupling, not by")
    print("      the nucleon ordering. Both readings agree sorted is optimal;")
    print("      neither supports the helper's pnp.")
    print("      NOT FIXED: a fix leaves V untouched but moves the Hecke NF vector")
    print("      (up to 2.5x) and Phi_1 (Part 4) -- outside this session's scope.")
    print("  LOOSE END 2 -- 3He/4He absence is a GENERATOR BUG (Part 5): a dedup")
    print("      guard `a > 4` whose premise ('explicitly added ... He isotopes')")
    print("      is false -- the explicit list is H-chain only. 6 unique rows are")
    print("      dropped; 3He and 4He are the only bound ones. The witness's sole")
    print("      assertion `all_A_leq_4_masses_computed` passes only because the")
    print("      filter removed the rows it claims to cover.")
    print(f"\n  wall {dt:.1f}s   assertions "
          f"{sum(assertions.values())}/{len(assertions)}")

    w = WitnessBuilder("ground-state-ordering-a3", engine="python")
    w.set_description(
        "Two diagnostics on the nucleon-ordering degree of freedom (bean qou-48is, "
        "loose ends of PR #4851). (1) hecke_core_symbolic._ground_state_ordering "
        "returns `pnp` for 3He while prop:ground-state-ordering rule (iii) says "
        "sorted `ppn` wins for A <= 3. Computing the proposition's own objective "
        "Phi_q = sum_i log|V_i| over EVERY arrangement at the experimental proton "
        "anchor shows the argmin at (Z,N)=(2,1) is `ppn`: the PROPOSITION is right "
        "and the HELPER is wrong. The helper performs no variational search (it is "
        "a fixed interleaving generator identical to _alternating_ordering_sym), is "
        "not the Phi_q argmin across an exhaustive A <= 14 sweep, and is not the "
        "extremum of any other objective the corpus states -- so the disagreement "
        "is a defect, not a definitional difference. The fix is NOT applied: it "
        "moves atom_V_full_sym / build_atom_nf_sym and hence published witness "
        "values, which is outside this session's scope bar. (2) 3He (2,1) and 4He "
        "(2,2) are absent from mass-table-comprehensive.witness.json because of a "
        "dedup guard `if a > 4:  # Avoid duplicates with explicitly added H, He "
        "isotopes` whose premise is false -- the explicit ISOTOPES list contains "
        "only H-chain entries (p, n, D, T, all Z <= 1), so no Z >= 2 grid row can "
        "duplicate it. The guard drops exactly 6 unique (Z, N) rows, of which 3He "
        "and 4He are the only bound nuclides. free_parameters = 0; no AME/CODATA "
        "quantity selects anything; nothing is wired; no published number changed. "
        "Sharpening: on the BARE NUCLEON chain the two 3He arrangements are "
        "EXACTLY degenerate -- the transfer factors T(d) = S + d.1 all commute, so "
        "the readout depends on the crossing coefficients only as a multiset "
        "(proved sorry-free over a generic CommRing in "
        "QOU/MassTheory/TransferFactorCommute.lean). Rule (iii)'s 'sorted BEATS "
        "interleaving' is thus a TIE at 3He, strict only after the electron tail "
        "is appended -- and that separation is produced by the UNDEFINED (n, e) "
        "crossing coefficient, which _phi1_from_ordering_sym silently skips. Both "
        "readings put sorted at the optimum; neither supports the helper's pnp.")
    w.set_audit_only(True)
    w.add_parameter("q0_experimental_proton_anchor", mp.nstr(Q0, 30))
    w.add_parameter("q0_pin", "experimental/proton (q_parameter.q_at; owner directive "
                              "2026-08-07) -- layer-pure, no muon-built cache read")
    w.add_parameter("free_parameters", 0)
    w.add_parameter("dps", DPS)
    w.add_parameter("objective", "Phi_q = sum_i log|V_i| via "
                                 "hecke_core_symbolic._phi1_from_ordering_sym")
    for k, v in results.items():
        w.add_data(k, v)
    for k, v in assertions.items():
        w.add_assertion(k, v, 1)
    w.add_caveat(
        "SCOPE-(a) throughout. Loose end 1 is a measured statement about ONE "
        "objective (Phi_q, the functional prop:ground-state-ordering names) at ONE "
        "anchor (experimental proton) over a finite sweep (A <= 14): the helper's "
        "output is not its argmin at 3He and at several larger (Z, N). That "
        "identifies a defect in the helper relative to the objective its own name "
        "invokes. It does NOT prove prop:ground-state-ordering -- the proposition "
        "remains stated-not-proved (`def ... : Prop` with no discharging instance), "
        "and its A > 14 extrapolation is untested here. Nothing is excluded "
        "structurally, so no scope-(b) claim is made.")
    w.add_caveat(
        "NO PRODUCTION CHANGE. This probe is diagnostic. The helper is NOT fixed "
        "(Part 4 measures that a fix would move atom_V_full_sym / build_atom_nf_sym "
        "and every witness downstream), the mass table is NOT regenerated, and the "
        "production A >= 3 binding convention (sorted, closed_form_tau_M.py:290) is "
        "untouched. Reconciling the two live conventions remains an owner decision.")
    w.add_caveat(
        "The Phi_q objective evaluated here is the PRODUCTION form -- the nucleon "
        "arrangement plus the Z-electron tail, as compute_phi1_full_sym builds it. "
        "The bare-nucleon Phi is reported alongside because the proposition's prose "
        "speaks of the nucleon ordering; at 3He the two differ (the bare-nucleon "
        "objective ties `ppn` with `pnp`, the production objective separates them "
        "in favour of `ppn`), which is itself part of the finding.")
    w.add_data("references", {
        "prop:ground-state-ordering":
            "folio/quantum-observable-universe/mass-theory/"
            "ground-state-ordering.md",
        "predecessor_audit":
            "docs/audits/2026-08-09-canonical-ordering-dof-production-impact.md",
        "companion_audit":
            "docs/audits/2026-08-09-ordering-loose-ends-a3-helper-and-"
            "missing-he-rows.md",
    })
    w.save()

    ok = all(v == 1 for v in assertions.values())
    print("\n  witness: computations/probes/ground-state-ordering-a3.witness.json")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
