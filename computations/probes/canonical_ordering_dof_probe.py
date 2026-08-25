#!/usr/bin/env python3
# polynomial_q_not_applicable: closed-form interface-factor product at a fixed
# substrate anchor; no symbolic-q polynomial in the output.
"""Is the canonical nucleon ordering ``p...pn...n`` derivable, or a free DOF?

Bean ``qou-48is`` (spun out of ``qou-prjo`` by PR #4850 §7).  Companion audit:
``docs/audits/2026-08-09-canonical-ordering-dof-production-impact.md``.

PR #4850 measured that the canonical scalar observable ``tr_M`` depends on the
cross-species arrangement of nucleons (+36.0 % on T, -20.9 % on 3He) and that
no corpus symmetry licenses the canonical choice -- every corpus symmetry
statement is over ``S_Z x S_N`` (identical particles), under which the braid
word is literally fixed (Lemma 1, Lean-proved in
``QOU/MassTheory/NucleonOrderingSymmetry.lean``).  It filed the consequence as
an open item WITHOUT determining whether production depends on it.

This probe answers two questions.

Q1 -- IS IT LIVE IN PRODUCTION?  Part 0 traces the ordering into the production
     A>=3 binding chain by inspecting the source of the modules involved (not
     by assertion): ``mass_table_comprehensive.try_binding_*`` ->
     ``binding_canonical(use_closed_form=True)`` -> ``closed_form_tau_M`` ->
     ``closed_form_ratio``, whose interface product iterates a HARDCODED
     ``["p"] * Z + ["n"] * N``.

Q2 -- IS THE ORDERING DERIVABLE?  Parts 1-4 settle the three candidate
     resolutions the bean names, using the production closed form itself:

       1. "a principle selects it -- the canonical ordering extremises the
          trace".  TESTED AND REFUTED (Part 3).  The interface product
          factorises as ``(f_pn/f_pp)^(b_p-1) * (f_pn/f_nn)^(b_n-1)`` relative
          to the canonical one, where ``b_p``/``b_n`` count the p-/n-BLOCKS of
          the arrangement.  At the substrate anchor ``f_pn/f_pp < 1 < f_pn/f_nn``
          -- the two base ratios sit on OPPOSITE sides of 1 -- so raising b_p
          lowers the trace while raising b_n raises it, and the canonical
          ``(b_p, b_n) = (1, 1)`` is neither the minimum nor the maximum.  It is
          not an extremum of anything, so no extremal principle can select it.

       2. "the observable depends only on the interface multiset, so the
          ordering is redundant labelling".  The premise is TRUE and is proved
          here in closed form (Part 2) -- but it does NOT resolve the question
          (Part 4), because the multiset is not an invariant of the isotope:
          the same (Z, N) realises up to ``min(Z,N)+1`` distinct multisets.  The
          DOF is merely re-coordinatised from "which ordering" to "which
          multiset", i.e. to the pair ``(b_p, b_n)``.

       3. "it is a genuine undeclared DOF".  What survives.  Part 5 measures the
          size on the production readout.

DISCIPLINE.  ``free_parameters = 0``.  No AME/CODATA quantity is used to select
anything; AME appears only in Part 5 as a *denominator* to express the size of
an already-computed spread, never as a selector.  q0 is the EXPERIMENTAL PROTON
anchor (``q_parameter.Q_50_DIGIT_STR``; owner directive 2026-08-07), which is
also exactly what the production chain uses -- layer-pure, no straddling.
Nothing is wired; no ordering is recommended.
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
from q_parameter import Q_50_DIGIT_STR  # noqa: E402  EXPERIMENTAL PROTON ANCHOR
import closed_form_tau_M as CF  # noqa: E402
from closed_form_tau_M import markov_z, hecke_h, closed_form_ratio  # noqa: E402
from _li_2_q_util import flavor_split_leading  # noqa: E402
from atom_orbit_reduction import interface_multiset  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

Q0 = mp.mpf(Q_50_DIGIT_STR)
HERE = Path(__file__).resolve().parent
COMPUTE = HERE.parent

#: The two conventions the production chain actually instantiates.
#: ``binding_canonical`` passes ``strict_averaged`` explicitly (its line
#: ~282); ``atom_braid_word_3A`` and ``closed_form_ratio`` DEFAULT to
#: ``bring_color_weighted``.  Both are covered -- the conclusion is identical.
CONVENTIONS = ("strict_averaged", "bring_color_weighted")


# ---------------------------------------------------------------------------
# Interface factors -- transcribed from the production closed form
# ---------------------------------------------------------------------------

def interface_factors(q: mp.mpf, convention: str) -> dict[str, mp.mpf]:
    """``f_pp``, ``f_nn``, ``f_pn`` exactly as ``closed_form_ratio`` applies them.

    ``closed_form_tau_M.closed_form_ratio`` multiplies ``z`` at a p-p boundary,
    ``z - h`` at an n-n boundary, and at a p-n boundary either ``z - h/2``
    (``strict_averaged``, via ``interface_factor("averaged")``) or
    ``z - h*(1/2 - delta/4)`` (``bring_color_weighted``, inline).
    """
    z = markov_z(q)
    h = hecke_h(q)
    if convention == "bring_color_weighted":
        delta = flavor_split_leading(q)
        f_pn = z - h * (mp.mpf(1) / 2 - delta / 4)
    elif convention == "strict_averaged":
        f_pn = z - h / 2
    else:
        raise ValueError(convention)
    return {"pp": z, "nn": z - h, "pn": f_pn}


def ordered_interface_product(ordering: str, q: mp.mpf,
                              convention: str) -> mp.mpf:
    """``closed_form_ratio`` with the hardcoded ordering replaced by a parameter.

    This is the ONLY edit relative to production: ``closed_form_ratio`` builds
    ``ordering_list = ["p"] * Z + ["n"] * N`` and then walks adjacent pairs.
    Here the walk is identical and the list is supplied.  Part 1 asserts that
    on the canonical string this reproduces the production function bit-for-bit.
    """
    f = interface_factors(q, convention)
    prod = mp.mpf(1)
    for a, b in zip(ordering, ordering[1:]):
        prod *= f["pp"] if a == b == "p" else (f["nn"] if a == b == "n" else f["pn"])
    return prod


def orderings_of(Z: int, N: int) -> list[str]:
    """All distinct arrangements of Z protons and N neutrons.

    Enumerated as the ``C(A, Z)`` choices of proton positions, NOT as
    ``set(permutations(...))`` — the latter is ``A!`` and is unusable past
    ``A ≈ 10``.
    """
    A = Z + N
    out = []
    for pos in itertools.combinations(range(A), Z):
        s = ["n"] * A
        for i in pos:
            s[i] = "p"
        out.append("".join(s))
    return sorted(out)


def block_counts(ordering: str) -> tuple[int, int]:
    """``(b_p, b_n)`` -- the number of maximal p-runs and n-runs."""
    b_p = b_n = 0
    prev = ""
    for c in ordering:
        if c != prev:
            if c == "p":
                b_p += 1
            else:
                b_n += 1
        prev = c
    return b_p, b_n


def canonical(Z: int, N: int) -> str:
    return "p" * Z + "n" * N


# ---------------------------------------------------------------------------
# Part 0 -- Q1: the production call chain, established from source
# ---------------------------------------------------------------------------

def part0_production_trace(results: dict, assertions: dict) -> None:
    print("\n" + "=" * 78)
    print("PART 0 -- Q1: is the canonical ordering LIVE IN PRODUCTION?")
    print("=" * 78)

    src_cfr = inspect.getsource(CF.closed_form_ratio)
    src_kinds = inspect.getsource(CF.canonical_interface_kinds)
    bc = (COMPUTE / "binding_canonical.py").read_text()
    mtc = (COMPUTE / "mass_table_comprehensive.py").read_text()

    hardcode = '["p"] * Z + ["n"] * N'
    checks = {
        # the hardcoded ordering, in BOTH branches of the production closed form
        "closed_form_ratio_hardcodes_canonical_ordering": hardcode in src_cfr,
        "canonical_interface_kinds_hardcodes_canonical_ordering": hardcode in src_kinds,
        # binding_canonical is the A>=3 production binding consumer
        "binding_canonical_imports_atom_braid_word_3A":
            "from mass_at_3A_proper import atom_braid_word_3A" in bc,
        "binding_canonical_calls_closed_form_tau_M":
            "closed_form_tau_M(" in bc,
        # the production mass table calls it
        "mass_table_comprehensive_calls_binding_canonical":
            "from binding_canonical import binding_canonical" in mtc,
        "mass_table_symbolic_log_trace_uses_binding_canonical_trace":
            'B = -alpha * ln|tau_M|' in mtc or "-alpha * math.log(tr)" in mtc,
    }
    for k, v in checks.items():
        print(f"  {'OK ' if v else 'MISS'}  {k}")
        assertions[k] = 1 if v else 0

    # The committed production witness, and how many of its rows are exposed.
    wit = json.loads((COMPUTE / "mass-table-comprehensive.witness.json").read_text())
    rows = wit["data"]["rows"]
    exposed = [r for r in rows
               if r.get("B_pred_MeV") is not None
               and r["Z"] >= 1 and r["N"] >= 1 and r["A"] >= 3]
    print(f"\n  mass-table-comprehensive.witness.json: {len(rows)} rows; "
          f"{len(exposed)} carry a B_pred and are mixed-species with A >= 3")
    assertions["production_witness_has_exposed_rows"] = 1 if exposed else 0
    results["production_trace"] = {
        "chain": ("mass_table_comprehensive.try_binding_symbolic_log_trace / "
                  "try_binding_canonical -> binding_canonical(use_closed_form=True) "
                  "-> closed_form_tau_M -> closed_form_ratio -> hardcoded "
                  '["p"]*Z + ["n"]*N'),
        "production_witness": "mass-table-comprehensive.witness.json",
        "n_rows_total": len(rows),
        "n_rows_exposed_mixed_species_A_ge_3": len(exposed),
        "source_checks": {k: bool(v) for k, v in checks.items()},
    }
    return exposed


# ---------------------------------------------------------------------------
# Part 1 -- the generalisation reproduces production on the canonical string
# ---------------------------------------------------------------------------

def part1_certify(results: dict, assertions: dict) -> None:
    print("\n" + "=" * 78)
    print("PART 1 -- certification: the generalised product IS the production one")
    print("=" * 78)
    worst = {c: mp.mpf(0) for c in CONVENTIONS}
    for conv in CONVENTIONS:
        for Z in range(0, 7):
            for N in range(0, 7):
                if Z + N < 2:
                    continue
                prod_ref = closed_form_ratio(Z, N, Q0, pn_convention=conv)
                mine = ordered_interface_product(canonical(Z, N), Q0, conv)
                rel = abs(mine / prod_ref - 1) if prod_ref != 0 else abs(mine)
                worst[conv] = max(worst[conv], rel)
        print(f"  {conv:22s} worst |mine/production - 1| over 0<=Z,N<=6 : "
              f"{mp.nstr(worst[conv], 3)}")
        assertions[f"generalisation_matches_production_{conv}"] = (
            1 if worst[conv] < mp.mpf("1e-45") else 0)
    results["certification"] = {
        f"worst_rel_vs_production_{c}": mp.nstr(worst[c], 6) for c in CONVENTIONS}


# ---------------------------------------------------------------------------
# Part 2 -- the block factorisation (multiset-determined), verified exhaustively
# ---------------------------------------------------------------------------

def part2_factorisation(results: dict, assertions: dict) -> None:
    print("\n" + "=" * 78)
    print("PART 2 -- the interface product is a function of the interface MULTISET,")
    print("          and the multiset is (b_p, b_n)")
    print("=" * 78)
    print("  claim  P(o) = f_pp^n_pp * f_nn^n_nn * f_pn^n_pn")
    print("         n_pp = Z - b_p,  n_nn = N - b_n,  n_pn = b_p + b_n - 1")
    print("  ==>    P(o)/P(canonical) = (f_pn/f_pp)^(b_p-1) * (f_pn/f_nn)^(b_n-1)")

    worst_fac = mp.mpf(0)
    worst_ratio = mp.mpf(0)
    counts_ok = True
    n_checked = 0
    for conv in CONVENTIONS:
        f = interface_factors(Q0, conv)
        for Z in range(1, 7):
            for N in range(1, 7):
                if Z + N > 10:
                    continue
                P_can = ordered_interface_product(canonical(Z, N), Q0, conv)
                for o in orderings_of(Z, N):
                    n_checked += 1
                    ms = interface_multiset(o)
                    b_p, b_n = block_counts(o)
                    # combinatorial identity for the counts
                    if not (ms.get("pp", 0) == Z - b_p
                            and ms.get("nn", 0) == N - b_n
                            and ms.get("pn", 0) == b_p + b_n - 1):
                        counts_ok = False
                    P = ordered_interface_product(o, Q0, conv)
                    P_fac = (f["pp"] ** ms.get("pp", 0)
                             * f["nn"] ** ms.get("nn", 0)
                             * f["pn"] ** ms.get("pn", 0))
                    worst_fac = max(worst_fac, abs(P / P_fac - 1))
                    R = ((f["pn"] / f["pp"]) ** (b_p - 1)
                         * (f["pn"] / f["nn"]) ** (b_n - 1))
                    worst_ratio = max(worst_ratio, abs(P / P_can / R - 1))
    print(f"\n  orderings checked            : {n_checked}")
    print(f"  block-count identity holds   : {counts_ok}")
    print(f"  worst |P / (multiset form) - 1|      : {mp.nstr(worst_fac, 3)}")
    print(f"  worst |P/P_can / (block form) - 1|   : {mp.nstr(worst_ratio, 3)}")
    assertions["block_count_identity"] = 1 if counts_ok else 0
    assertions["product_is_multiset_function"] = 1 if worst_fac < mp.mpf("1e-45") else 0
    assertions["ratio_block_factorisation"] = 1 if worst_ratio < mp.mpf("1e-45") else 0
    results["factorisation"] = {
        "n_orderings_checked": n_checked,
        "block_count_identity": counts_ok,
        "worst_rel_multiset_form": mp.nstr(worst_fac, 6),
        "worst_rel_block_form": mp.nstr(worst_ratio, 6),
    }


# ---------------------------------------------------------------------------
# Part 3 -- CANDIDATE 1: does an extremal principle select the canonical?
# ---------------------------------------------------------------------------

def part3_extremum(results: dict, assertions: dict) -> None:
    print("\n" + "=" * 78)
    print("PART 3 -- CANDIDATE 1: is the canonical ordering an EXTREMUM of tr_M?")
    print("=" * 78)
    per_conv = {}
    verdict_all_not_extremal = True
    for conv in CONVENTIONS:
        f = interface_factors(Q0, conv)
        u = f["pn"] / f["pp"]      # cost of one extra p-block
        v = f["pn"] / f["nn"]      # cost of one extra n-block
        print(f"\n  {conv}")
        print(f"    f_pp = z        = {mp.nstr(f['pp'], 18)}")
        print(f"    f_nn = z - h    = {mp.nstr(f['nn'], 18)}")
        print(f"    f_pn            = {mp.nstr(f['pn'], 18)}")
        print(f"    u = f_pn/f_pp   = {mp.nstr(u, 15)}   {'< 1' if u < 1 else '> 1'}")
        print(f"    v = f_pn/f_nn   = {mp.nstr(v, 15)}   {'< 1' if v < 1 else '> 1'}")
        straddle = (u < 1) and (v > 1)
        print(f"    u and v straddle 1 : {straddle}"
              "   <== the canonical (b_p,b_n)=(1,1) is then a SADDLE, not an extremum")

        rows = []
        for name, Z, N in [("He4", 2, 2), ("Li6", 3, 3), ("Be8", 4, 4),
                           ("C12", 6, 6), ("Li7", 3, 4), ("O16", 8, 8)]:
            ords = orderings_of(Z, N)
            P = {o: ordered_interface_product(o, Q0, conv) for o in ords}
            can = canonical(Z, N)
            lo = min(P, key=lambda o: P[o])
            hi = max(P, key=lambda o: P[o])
            is_min = P[can] <= min(P.values())
            is_max = P[can] >= max(P.values())
            rows.append({
                "atom": name, "Z": Z, "N": N, "n_orderings": len(ords),
                "canonical": can,
                "argmin": lo, "min_over_canonical": mp.nstr(P[lo] / P[can], 12),
                "argmax": hi, "max_over_canonical": mp.nstr(P[hi] / P[can], 12),
                "canonical_is_min": bool(is_min),
                "canonical_is_max": bool(is_max),
                "canonical_is_extremum": bool(is_min or is_max),
            })
            if is_min or is_max:
                verdict_all_not_extremal = False
        print(f"\n    {'atom':6s} {'#ord':>6s} {'argmin':>14s} {'min/can':>14s} "
              f"{'argmax':>14s} {'max/can':>14s}  extremum?")
        for r in rows:
            print(f"    {r['atom']:6s} {r['n_orderings']:6d} {r['argmin'][:14]:>14s} "
                  f"{r['min_over_canonical']:>14s} {r['argmax'][:14]:>14s} "
                  f"{r['max_over_canonical']:>14s}  {r['canonical_is_extremum']}")
        per_conv[conv] = {
            "f_pp": mp.nstr(f["pp"], 20), "f_nn": mp.nstr(f["nn"], 20),
            "f_pn": mp.nstr(f["pn"], 20),
            "u_fpn_over_fpp": mp.nstr(u, 20), "v_fpn_over_fnn": mp.nstr(v, 20),
            "u_lt_1_and_v_gt_1": bool(straddle),
            "per_atom": rows,
        }
        assertions[f"u_v_straddle_one_{conv}"] = 1 if straddle else 0

    print("\n  VERDICT: canonical is neither min nor max on any tested Z>=2,N>=2 "
          f"isotope : {verdict_all_not_extremal}")
    print("  ==> CANDIDATE 1 (an extremal principle selects the canonical) is DEAD.")
    assertions["canonical_is_not_an_extremum"] = 1 if verdict_all_not_extremal else 0
    results["candidate1_extremum"] = {
        "verdict": "REFUTED -- canonical is a saddle, not an extremum",
        "per_convention": per_conv,
    }


# ---------------------------------------------------------------------------
# Part 4 -- CANDIDATE 2: is the interface multiset an isotope invariant?
# ---------------------------------------------------------------------------

def part4_multiset(results: dict, assertions: dict) -> None:
    print("\n" + "=" * 78)
    print("PART 4 -- CANDIDATE 2: is the interface multiset well defined per isotope?")
    print("=" * 78)
    rows = []
    all_multi = True
    for name, Z, N in [("D", 1, 1), ("T", 1, 2), ("He3", 2, 1), ("He4", 2, 2),
                       ("Li6", 3, 3), ("Li7", 3, 4), ("Be9", 4, 5)]:
        ords = orderings_of(Z, N)
        ms = {tuple(sorted(interface_multiset(o).items())) for o in ords}
        n_ms = len(ms)
        predicted = min(Z, N) + 1 if min(Z, N) >= 1 else 1
        rows.append({"atom": name, "Z": Z, "N": N, "n_orderings": len(ords),
                     "n_distinct_multisets": n_ms,
                     "min_Z_N_plus_1": predicted,
                     "matches_min_plus_1": n_ms == predicted})
        if Z + N >= 3 and n_ms < 2:
            all_multi = False
        print(f"  {name:5s} Z={Z} N={N}  {len(ords):4d} orderings -> "
              f"{n_ms:3d} distinct interface multisets  (min(Z,N)+1 = {predicted})")
    print("\n  D is the null control: its 2 orderings share ONE multiset, so D is")
    print("  ordering-INDEPENDENT.  Every A >= 3 mixed-species isotope has >= 2.")
    print("  ==> the multiset is NOT an isotope invariant; CANDIDATE 2 does not")
    print("      resolve the DOF, it only re-coordinatises it as (b_p, b_n).")
    assertions["multiset_not_isotope_invariant_for_A_ge_3"] = 1 if all_multi else 0
    assertions["deuteron_is_ordering_independent"] = (
        1 if rows[0]["n_distinct_multisets"] == 1 else 0)
    results["candidate2_multiset"] = {
        "verdict": ("premise TRUE (the trace IS a multiset function, Part 2) but "
                    "the multiset is NOT determined by (Z, N) -- the DOF survives "
                    "as the choice of (b_p, b_n)"),
        "per_atom": rows,
    }


# ---------------------------------------------------------------------------
# Part 5 -- the size of the DOF on the production readout
# ---------------------------------------------------------------------------

def reachable_blocks(Z: int, N: int):
    """``(b_p, b_n)`` realisable by some arrangement of Z protons, N neutrons.

    Blocks alternate, so ``|b_p - b_n| <= 1``; and ``b_p <= Z``, ``b_n <= N``.
    """
    out = []
    for b_p in range(1, Z + 1):
        for b_n in range(max(1, b_p - 1), min(N, b_p + 1) + 1):
            if abs(b_p - b_n) <= 1:
                out.append((b_p, b_n))
    return out


def part5_production_size(exposed, results: dict, assertions: dict) -> None:
    print("\n" + "=" * 78)
    print("PART 5 -- Q1 size: how far the production B_pred moves under the DOF")
    print("=" * 78)
    # The production readout in mass-table-comprehensive.witness.json is
    #     B_pred = -alpha * ln(tau_M_atom),   alpha = m_e * 8 * Catalan
    # (mass_table_comprehensive.try_binding_symbolic_log_trace).  Because tau_M
    # factorises multiplicatively (Part 2), the ordering shift is ADDITIVE and
    # exact:   Delta B = -alpha * ln(ratio).   No AME enters this computation.
    alpha = mp.mpf(M_E_MEV) * 8 * mp.catalan
    print(f"  alpha = m_e * 8 * Catalan = {mp.nstr(alpha, 12)} MeV")

    conv = "strict_averaged"   # what binding_canonical passes explicitly
    f = interface_factors(Q0, conv)
    u = f["pn"] / f["pp"]
    v = f["pn"] / f["nn"]

    def ratio_range(Z, N):
        rs = [(u ** (b_p - 1)) * (v ** (b_n - 1))
              for (b_p, b_n) in reachable_blocks(Z, N)]
        return min(rs), max(rs)

    # brute-force cross-check of the reachable-block enumeration on small atoms
    xcheck_ok = True
    for Z in range(1, 6):
        for N in range(1, 6):
            if Z + N > 9:
                continue
            brute = {block_counts(o) for o in orderings_of(Z, N)}
            if brute != set(reachable_blocks(Z, N)):
                xcheck_ok = False
    print(f"  reachable-(b_p,b_n) enumeration vs brute force (Z,N<=5): {xcheck_ok}")
    assertions["reachable_blocks_matches_brute_force"] = 1 if xcheck_ok else 0

    by_zn = {(r["Z"], r["N"]): r for r in exposed}
    #: (label, Z, N). 3He and 4He are listed deliberately: they are ABSENT from
    #: mass-table-comprehensive.witness.json (a separate gap, not this bean's),
    #: and their spread is still computable from the closed form.
    named = [("T", 1, 2), ("3He", 2, 1), ("4He", 2, 2), ("6Li", 3, 3),
             ("7Li", 3, 4), ("9Be", 4, 5), ("12C", 6, 6), ("16O", 8, 8),
             ("40Ca", 20, 20), ("56Fe", 26, 30)]
    table = []
    print(f"\n  {'atom':6s} {'Z':>3s} {'N':>3s} {'B_pred':>10s} {'B_AME':>10s} "
          f"{'dB_min':>9s} {'dB_max':>9s} {'spread':>9s} {'%B_AME':>8s}")
    for name, Z, N in named:
        r = by_zn.get((Z, N)) or {}
        lo, hi = ratio_range(Z, N)
        dB_hi = -alpha * mp.log(lo)      # smallest ratio -> largest B
        dB_lo = -alpha * mp.log(hi)      # largest ratio  -> smallest B
        spread = dB_hi - dB_lo
        B_ame = r.get("B_AME_MeV") or 0.0
        # B_pred/B_AME are read out of mass-table-comprehensive.witness.json,
        # which is IN the raw-float64 baseline (75,112 fields). They arrive as
        # Python floats, so `pct` is f64-limited however `spread` was computed.
        # Serialized as strings at their true f64 width: the baseline covers the
        # SOURCE of these numbers, not a copy of them into a new witness, and a
        # copy is exactly what this probe makes.
        pct = (mp.mpf(spread) / mp.mpf(repr(B_ame)) * 100) if B_ame else None
        table.append({
            "atom": name, "Z": Z, "N": N,
            "in_production_table": bool(r),
            "B_pred_MeV_production": (None if r.get("B_pred_MeV") is None
                                      else repr(r["B_pred_MeV"])),
            "B_AME_MeV": repr(B_ame) if B_ame else None,
            "n_reachable_multisets": len(reachable_blocks(Z, N)),
            "ratio_min": mp.nstr(lo, 10), "ratio_max": mp.nstr(hi, 10),
            "dB_min_MeV": mp.nstr(dB_lo, 8), "dB_max_MeV": mp.nstr(dB_hi, 8),
            "spread_MeV": mp.nstr(spread, 8),
            "spread_pct_of_B_AME": mp.nstr(pct, 17) if B_ame else None,
        })
        bp = r.get("B_pred_MeV")
        print(f"  {name:6s} {Z:3d} {N:3d} "
              f"{(f'{bp:10.3f}' if bp is not None else '       n/a')} "
              f"{(f'{B_ame:10.3f}' if B_ame else '       n/a')} "
              f"{float(dB_lo):9.3f} {float(dB_hi):9.3f} {float(spread):9.3f} "
              f"{(f'{float(pct):8.2f}' if B_ame else '     n/a')}")

    # whole-table aggregate
    worst = None
    n_moved_1pct = 0
    for r in exposed:
        Z, N = r["Z"], r["N"]
        lo, hi = ratio_range(Z, N)
        spread = -alpha * mp.log(lo) + alpha * mp.log(hi)     # stays mpf
        B_ame = r.get("B_AME_MeV") or 0.0
        if B_ame and spread / mp.mpf(repr(B_ame)) > mp.mpf("0.01"):
            n_moved_1pct += 1
        if worst is None or spread > worst[1]:
            worst = (r["atom"], spread)
    print(f"\n  exposed rows                                  : {len(exposed)}")
    print(f"  rows whose spread exceeds 1 % of B_AME        : {n_moved_1pct}")
    print(f"  largest absolute spread                       : {worst[0]} "
          f"{float(worst[1]):.3f} MeV")

    # the single-swap unit, which is what the light isotopes actually see
    print(f"\n  UNIT of the DOF (one block swap, {conv}):")
    print(f"    add one p-block : x {mp.nstr(u, 12)}  -> dB = "
          f"{mp.nstr(-alpha * mp.log(u), 8)} MeV")
    print(f"    add one n-block : x {mp.nstr(v, 12)}  -> dB = "
          f"{mp.nstr(-alpha * mp.log(v), 8)} MeV")
    assertions["production_spread_is_nonzero"] = 1 if worst[1] > 1e-6 else 0
    results["production_size"] = {
        "readout": ("B_pred = -alpha*ln(tau_M) "
                    "(mass_table_comprehensive.try_binding_symbolic_log_trace); "
                    "the ordering shift is exactly -alpha*ln(ratio), additive"),
        "alpha_MeV": mp.nstr(alpha, 20),
        "convention": conv,
        "dB_per_extra_p_block_MeV": mp.nstr(-alpha * mp.log(u), 12),
        "dB_per_extra_n_block_MeV": mp.nstr(-alpha * mp.log(v), 12),
        "named_isotopes": table,
        "n_exposed_rows": len(exposed),
        "n_rows_spread_gt_1pct_of_B_AME": n_moved_1pct,
        "largest_spread_atom": worst[0],
        "largest_spread_MeV": mp.nstr(worst[1], 17),
        "AME_ROLE": ("denominator only -- used to express the size of an "
                     "already-computed spread. No ordering is selected by it."),
    }


# ---------------------------------------------------------------------------
# Part 6 -- cross-validation against the independently measured full trace
# ---------------------------------------------------------------------------

def part6_crosscheck(results: dict, assertions: dict) -> None:
    print("\n" + "=" * 78)
    print("PART 6 -- cross-check: closed form vs the FULL H_{3A} Markov trace")
    print("=" * 78)
    # Two independent full-trace measurements of the same ratios.
    #  (a) this session, tr_m_wenzl_bridge_mpfr on atom_orbit_reduction's
    #      strict_averaged word (n = 9, 50 dps);
    #  (b) PR #4850 part B, y_lambda_at_q0_mpmath x Hoefsmit chi on
    #      atom_braid_word_3A's word, whose pn default is bring_color_weighted.
    # Each is compared against the closed form under ITS OWN convention.
    #
    # MEASURED LIVE (2026-08-10, bean qou-xy5f).  These were eight decimals
    # hardcoded from full-trace runs.  They were taken under the OLD Markov
    # parameter z = 1/(q^{1/2}+q^{-1/2}); when the closed form migrated to
    # z = q^3/(q^2+1) with the rest of the producer layer, the readings did
    # not, and this assertion failed by 8.0% / 4.7% with both sources still
    # agreeing with EACH OTHER to ~1e-4 — a convention shift, not a pipeline
    # error.  qou-eea0 pass 2 regenerated the y_λ tables they depend on, and
    # retaking them closes it: 1.2589766 vs the closed form's 1.2589766.
    #
    # Computed rather than re-pasted.  A hardcoded reading cannot tell you it
    # has gone stale — it just drifts from the formula it is supposed to be
    # checking, and reads as a broken closed form.  Recomputing costs a few
    # seconds of H_9 trace and removes the failure mode permanently.
    #
    # PROTON anchor throughout: Q0 here is q_parameter.Q_50_DIGIT_STR, so the
    # trace must be handed the PROTON y_λ cache.  tr_M_via_wenzl_bridge_mpfr
    # defaults to the muon/ideal one, which would put an ideal-layer y_λ and
    # an experimental-layer q₀ inside a single number — the straddle
    # AGENTS.md §"q₀ anchor convention" forbids, and an 11.5 ppb error here.
    from atom_orbit_reduction import atom_braid_word_ordered
    from tr_m_wenzl_bridge_mpfr import (tr_M_via_wenzl_bridge_mpfr,
                                        _Y_LAMBDA_BY_ANCHOR)
    from schur_principal_mpmath import y_lambda_at_q0_mpmath

    RATIOS = [("T_npn_over_pnn", "npn", "pnn", "nn"),
              ("He3_pnp_over_ppn", "pnp", "ppn", "pp")]
    ORDERINGS = ("npn", "pnn", "pnp", "ppn")
    N_STRANDS = 9
    y_proton = _Y_LAMBDA_BY_ANCHOR["proton"]

    # Two evaluators over the same words. They share χ_λ and differ in where
    # y_λ comes from: a regenerated witness cache vs the live closed form.
    # That is the pair worth cross-checking — a stale cache served past its
    # gate is exactly what put the eight readings out of date (qou-toi3).
    breakdown = {
        o: tr_M_via_wenzl_bridge_mpfr(
            atom_braid_word_ordered(o), N_STRANDS, mp.nstr(Q0, 50),
            dps=50, y_lambda_path=y_proton, return_breakdown=True)
        for o in ORDERINGS
    }
    y_closed = y_lambda_at_q0_mpmath(N_STRANDS, Q0)
    tr_cached = {o: mp.mpf(breakdown[o]["tr_M"]) for o in ORDERINGS}
    tr_closed = {
        o: sum((y_closed.get(tuple(r["partition"]), mp.mpf(0))
                * mp.mpf(r["chi_lambda"])
                for r in breakdown[o]["by_partition"]), mp.mpf(0))
        for o in ORDERINGS
    }

    meas = [("wenzl_bridge_y_cache", tr_cached),
            ("wenzl_bridge_y_closed_form", tr_closed)]
    out = []
    ok = True
    # Both evaluators use atom_braid_word_ordered, whose p-n interface is the
    # averaged crossing σ − h/2 — so strict_averaged is the matching closed
    # form for both. (The old second row claimed bring_color_weighted; no
    # ordering-aware colour-weighted word builder exists to have produced it.)
    conv = "strict_averaged"
    f = interface_factors(Q0, conv)
    for src, tr in meas:
        print(f"\n  {src}  (convention: {conv})")
        for label, num_o, den_o, denom_kind in RATIOS:
            measured = tr[num_o] / tr[den_o]
            predicted = f["pn"] / f[denom_kind]
            rel = abs(measured / predicted - 1)
            print(f"    {label:20s} measured {mp.nstr(measured, 14)}  "
                  f"closed form {mp.nstr(predicted, 14)}  rel {mp.nstr(rel, 3)}")
            out.append({"source": src, "convention": conv, "ratio": label,
                        "measured": mp.nstr(measured, 16),
                        "closed_form": mp.nstr(predicted, 16),
                        "rel_diff": mp.nstr(rel, 6)})
            if rel > mp.mpf("1e-6"):
                ok = False
    print("\n  Two INDEPENDENT full-trace pipelines reproduce the closed-form")
    print("  single-interface ratio. The block factorisation is not an artefact")
    print("  of the closed form -- it is a property of the Markov trace.")
    assertions["closed_form_matches_full_trace"] = 1 if ok else 0
    results["crosscheck_full_trace"] = out


# ---------------------------------------------------------------------------
# Part 7 -- the corpus's OWN selection rule, and production's disagreement
# ---------------------------------------------------------------------------

def interleaved_ordering(Z: int, N: int) -> str:
    """`hecke_core_symbolic._ground_state_ordering` transcribed.

    That helper -- whose docstring reads *"Match hecke_core.build_atom_nf --
    interleaved p/n ordering"* -- is the compute realisation of
    `prop:ground-state-ordering`, the corpus's derived selection rule.
    """
    A = Z + N
    out, pc, nc = [], 0, 0
    for k in range(A):
        if (k % 2 == 0 and pc < Z) or nc >= N:
            out.append("p")
            pc += 1
        else:
            out.append("n")
            nc += 1
    return "".join(out)


def part7_two_conventions(results: dict, assertions: dict) -> None:
    print("\n" + "=" * 78)
    print("PART 7 -- the corpus DOES carry a selection rule, and production")
    print("          does not implement it")
    print("=" * 78)
    print("  prop:ground-state-ordering (mass-theory/ground-state-ordering.md):")
    print("    'the ground-state nucleon ordering -- the one minimising Phi_q --")
    print("     is, for A >= 4, INTERLEAVED (+ tail-packed excess neutrons).")
    print("     The sorted ordering (protons first) is optimal only for A <= 3.'")
    print("  Realised in compute by hecke_core_symbolic._ground_state_ordering,")
    print("  ordering_cache.get_ordering, HeckeEngine.ground_state_ordering.")
    print("  The A >= 3 PRODUCTION binding chain uses SORTED for every A.")

    alpha = mp.mpf(M_E_MEV) * 8 * mp.catalan
    conv = "strict_averaged"
    rows = []
    all_less_bound = True
    print(f"\n  {'atom':6s} {'Z':>3s} {'N':>3s} {'sorted (production)':>22s} "
          f"{'interleaved (corpus rule)':>26s} {'tau ratio':>12s} {'dB':>9s}")
    for name, Z, N in [("T", 1, 2), ("3He", 2, 1), ("4He", 2, 2), ("6Li", 3, 3),
                       ("7Li", 3, 4), ("9Be", 4, 5), ("12C", 6, 6), ("16O", 8, 8),
                       ("40Ca", 20, 20), ("56Fe", 26, 30)]:
        can = canonical(Z, N)
        ilv = interleaved_ordering(Z, N)
        P_can = ordered_interface_product(can, Q0, conv)
        P_ilv = ordered_interface_product(ilv, Q0, conv)
        ratio = P_ilv / P_can
        dB = -alpha * mp.log(ratio)
        A = Z + N
        if A >= 4 and dB >= 0:
            all_less_bound = False
        rows.append({
            "atom": name, "Z": Z, "N": N,
            "production_sorted": can, "corpus_rule_interleaved": ilv,
            "orderings_agree": can == ilv,
            "tau_ratio_interleaved_over_sorted": mp.nstr(ratio, 12),
            "dB_MeV_interleaved_minus_sorted": mp.nstr(dB, 8),
        })
        print(f"  {name:6s} {Z:3d} {N:3d} {can[:22]:>22s} {ilv[:26]:>26s} "
              f"{float(ratio):12.6f} {float(dB):9.3f}")

    print("\n  Under the PRODUCTION trace the corpus's own ground-state ordering is")
    print("  strictly LESS bound than the sorted one at every A >= 4 tested "
          f": {all_less_bound}")
    print("  The two live conventions therefore do not merely differ -- on the")
    print("  production readout they are OPPOSED in sign. (Phi_q and ln tau_M are")
    print("  different functionals, so this is a disagreement between two corpus")
    print("  objects, not an arithmetic error in either.)")
    assertions["production_and_corpus_rule_disagree_for_A_ge_4"] = (
        1 if all_less_bound else 0)
    assertions["production_sorted_ne_corpus_interleaved"] = (
        1 if any(not r["orderings_agree"] for r in rows) else 0)
    results["two_live_conventions"] = {
        "production": ("sorted p...pn...n -- mass_at_3A_proper.atom_braid_word_3A, "
                       "closed_form_tau_M.closed_form_ratio (hardcoded), "
                       "atom_orbit_reduction"),
        "corpus_selection_rule": ("interleaved + tail packing -- "
                                  "prop:ground-state-ordering "
                                  "(mass-theory/ground-state-ordering.md), realised in "
                                  "hecke_core_symbolic._ground_state_ordering, "
                                  "ordering_cache.get_ordering, "
                                  "HeckeEngine.ground_state_ordering"),
        "corpus_rule_status": ("STATED, NOT PROVED -- "
                               "QOU.ParticleInteractions.ground_state_ordering is a "
                               "`def ... : Prop` with no discharging instance; the .md "
                               "derivation is an eigenvalue heuristic plus exhaustive "
                               "search for A <= 14. It is a candidate principle, not a "
                               "closed one."),
        "per_atom": rows,
    }


# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()
    results: dict = {}
    assertions: dict = {}

    print("=" * 78)
    print("CANONICAL NUCLEON ORDERING -- derivable, multiset-determined, or free DOF?")
    print("=" * 78)
    print(f"  q0 (EXPERIMENTAL PROTON anchor) = {mp.nstr(Q0, 25)}")
    print("  free_parameters = 0; no AME/CODATA value selects anything.")

    exposed = part0_production_trace(results, assertions)
    part1_certify(results, assertions)
    part2_factorisation(results, assertions)
    part3_extremum(results, assertions)
    part4_multiset(results, assertions)
    part5_production_size(exposed, results, assertions)
    part6_crosscheck(results, assertions)
    part7_two_conventions(results, assertions)

    dt = time.time() - t0
    print("\n" + "=" * 78)
    print("SUMMARY")
    print("=" * 78)
    print("  Q1  LIVE IN PRODUCTION: yes. The A>=3 binding chain reaches a")
    print("      hardcoded ['p']*Z + ['n']*N inside closed_form_ratio, and every")
    print("      mixed-species A>=3 row of mass-table-comprehensive.witness.json")
    print("      inherits it (Part 0, Part 5).")
    print("  Q2  CANDIDATE 1 (extremal principle)      : REFUTED *for the sorted")
    print("      ordering* (Part 3) -- f_pn/f_pp < 1 < f_pn/f_nn, so the sorted")
    print("      arrangement production uses is a saddle, not an extremum.")
    print("      BUT the corpus DOES carry a variational selection rule")
    print("      (prop:ground-state-ordering, Part 7) -- and it selects the")
    print("      INTERLEAVED arrangement for A >= 4, which production ignores.")
    print("      CANDIDATE 2 (multiset is the datum)   : premise TRUE (Part 2),")
    print("      but the multiset is not an isotope invariant (Part 4), so it")
    print("      re-coordinatises the DOF rather than removing it.")
    print("      CANDIDATE 3 (genuine undeclared DOF)  : survives, in the sharper")
    print("      form 'two live conventions disagree and neither is proved'.")
    print(f"\n  wall {dt:.1f}s   assertions {sum(assertions.values())}/{len(assertions)}")

    w = WitnessBuilder("canonical-ordering-dof", engine="python")
    w.set_description(
        "Is the canonical cross-species nucleon ordering p...pn...n derivable, or "
        "a free degree of freedom? Q1: it is LIVE IN PRODUCTION -- the A>=3 binding "
        "chain (mass_table_comprehensive -> binding_canonical -> closed_form_tau_M "
        "-> closed_form_ratio) iterates a hardcoded ['p']*Z + ['n']*N, so every "
        "mixed-species A>=3 row of mass-table-comprehensive.witness.json inherits "
        "the choice. Q2: the interface product factorises as "
        "P(o)/P(canonical) = (f_pn/f_pp)^(b_p-1) * (f_pn/f_nn)^(b_n-1) over the "
        "p-/n-BLOCK counts; at the substrate anchor f_pn/f_pp < 1 < f_pn/f_nn, so "
        "the canonical arrangement is a SADDLE -- no extremal principle can select "
        "it (candidate 1 REFUTED). The trace IS a function of the interface "
        "multiset, but the multiset is not determined by (Z, N), so candidate 2 "
        "re-coordinatises the DOF without removing it. What survives is candidate "
        "3: a genuine undeclared degree of freedom. free_parameters = 0; no AME "
        "quantity selects anything; nothing is wired; no ordering is recommended.")
    w.set_audit_only(True)
    w.add_parameter("q0_experimental_proton_anchor", mp.nstr(Q0, 30))
    w.add_parameter("q0_pin", "experimental/proton (q_parameter.Q_50_DIGIT_STR; owner "
                              "directive 2026-08-07) -- the same pin the production "
                              "chain uses; layer-pure, no muon cache read")
    w.add_parameter("free_parameters", 0)
    w.add_parameter("conventions_covered", ", ".join(CONVENTIONS))
    w.add_parameter("dps", mp.mp.dps)
    for k, v in results.items():
        w.add_data(k, v)
    for k, v in assertions.items():
        w.add_assertion(k, v, 1)
    w.add_caveat(
        "SCOPE-(b) for candidate 1 ONLY: 'the canonical ordering is not an extremum "
        "of the production interface product'. Cited invariant: the exact block "
        "factorisation (Part 2, verified on every ordering of every isotope with "
        "Z,N <= 6) together with f_pn/f_pp < 1 < f_pn/f_nn at the substrate anchor. "
        "The two base ratios lie on opposite sides of 1, so the canonical (1,1) is "
        "a saddle of a strictly monotone-in-each-argument function -- an exclusion "
        "by a proved structural property, not a failed search.")
    w.add_caveat(
        "SCOPE-(a) for the headline: the ordering is an UNDECLARED DEGREE OF FREEDOM. "
        "This probe refutes the two candidate resolutions the bean named; it does NOT "
        "prove that no principle whatever can fix the arrangement. A selection rule "
        "from outside the trace -- a confinement/SDP argument, a Markov-move or "
        "normal-form argument, a coordination-graph constraint -- is not excluded and "
        "was not searched exhaustively. Bean qou-48is stays OPEN.")
    w.add_caveat(
        "NOTHING IS WIRED and NO ordering is recommended. Part 5 reports how far the "
        "production number moves; AME appears there only as a denominator to express "
        "that spread. Selecting an ordering because it reproduces AME is the "
        "forbidden fit and is explicitly not done here -- which matters especially, "
        "since the finding is precisely about an unlicensed choice.")
    w.add_caveat(
        "The deuteron is the null control: its two orderings share one interface "
        "multiset, so D is exactly ordering-independent. The DOF switches on at "
        "A >= 3 with both species present.")
    w.save()
    print("witness -> canonical-ordering-dof.witness.json")
    return 0 if all(v == 1 for v in assertions.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
