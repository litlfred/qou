#!/usr/bin/env python3
"""Gap #2 — the substrate DOES fix a knot invariant, and it kills all three picks.

WHAT WAS ALREADY KNOWN, AND IS NOT RE-ARGUED HERE
--------------------------------------------------
`docs/audits/2026-08-25-knot-id-is-an-admitted-fit.md` (bean `qou-8ms1`)
established that the `6_2` / `8_11` / `L6a4` assignments in
`conj-canonical-knot-id-sdp.md` are an **admitted fit** — `mass_table_ppb.py`
says so verbatim, `jsj_verification.py` performs the search, and the criterion
is proximity to `B_AME/(rho*m_e)` with `rho` the corpus's own "hand-pick rho".
It measured the resulting census degeneracy (796 / 1,101 / 26,671 manifolds
strictly closer over `OrientableCuspedCensus`) and showed the SDP is a
feasibility check on a presupposed element, so uniqueness cannot be a property
of it. **All of that is prior work.** This probe re-measures it as a guard
(A5) and otherwise takes it as given.

That audit named one next step as the highest-value thing to do:

> **Derive a complexity bound on `K(²H)` from the substrate — braid index
> and/or crossing number — with no reference to `B_AME`; then ask whether the
> volume match is unique inside that class.** ... **check whether `n_braid: 3`,
> `n_0: 6` is derived or also handed over.**

**This probe does that**, with a different invariant than the two suggested —
the closure's **component count**, which the substrate fixes outright — and
carries it to `A = 3`, which the audit did not reach. The answer is negative
and it is not close.

THE DERIVED INVARIANT
----------------------
The canonical word `atom_braid_word_3A(Z, N)` is a Hecke element, not a braid
word: its letters are `c*sigma_g + d*1`, and the averaged ones resolve into
`sigma_g` or `sigma_g^-1`. **Both project to the same transposition `(g, g+1)`**,
so the underlying permutation — and therefore the number of components of the
closure, which is its cycle count — is identical on every branch and under
every crossing-sign convention. Nothing empirical enters.

Measured on the canonical word, over `0 <= Z, N <= 5`, `2 <= A <= 6`, both
`pn_convention`s and nine bond-multiplicity settings:

    c_free = 2A                                   exact, 0 deviations
    c_atom = 2A - #{bonds of ODD multiplicity}    exact, 414/414

A bond merges two components only when its crossing count is odd; an even
multiplicity is a full twist and merges nothing. At the unit multiplicities the
trace pipeline actually uses, all `A-1` chain bonds are odd, so

    c_atom = 2A - (A - 1) = A + 1                 3, 4, 4, 5 for 2H, 3H, 3He, 4He

**This independently corroborates `QOU.MassTheory.ClassicalTraceFloor`.** That
Lean file (bean `qou-zrx2`, sorry-free) derives `cAtom = A + 1` from
`cFree = 2*A` together with `cFree = cAtom + (A - 1)` — a combinatorial merge
argument. Here the same two counts fall out of the permutation of the actual
canonical word, a genuinely different route, so this is corroboration and not a
restatement (`qou-l81w`).

ALL THREE ASSIGNMENTS FAIL IT
-------------------------------
    atom   assigned link   components   required A+1   verdict
    ------------------------------------------------------------
    2H     6_2                  1            3         MISMATCH
    2H     Hopf L2a1 (bind)     2            3         MISMATCH
    3H     8_11                 1            4         MISMATCH   <- new
    3He    L6a4 (Borromean)     3            4         MISMATCH   <- new

The `2H` rows reproduce the audit's scope-(b) finding. **The `3H` and `3He`
rows are new**: `8_11` is a knot where a 4-component link is required, and
`L6a4` — the one assignment with a reason independent of its volume — is off by
exactly one component. So the arity objection is not a deuteron peculiarity; it
is uniform across the registry.

AND THE TWO CONSTRAINTS TOGETHER ARE EMPTY
--------------------------------------------
This is the audit's question answered. Intersect the derived arity with the
volume window each pick's own accuracy defines (no tolerance chosen):

    atom   manifolds in the volume window   ... of which have A+1 cusps
    ---------------------------------------------------------------------
    2H                      799                          0
    3H                    1,102                          0
    3He                  26,843                         29

**At `2H` and `3H` the candidate set is empty.** No census manifold has both
the derived component count and a volume matching `B_AME/(rho*m_e)` as well as
the named knot does. So the answer to "is the volume match unique inside the
derived class?" is not "yes" and not "no" — the class contains **nothing**, the
named knot included, because the named knot is not in it either.

At `3He`, 29 survive, and the best of them beats the incumbent by fivefold:

    L14n62525   Vol = 7.597116   B_pred = 7.76424 MeV   +0.598 %
    L6a4        Vol = 7.327725   B_pred = 7.48892 MeV   -2.969 %   (3 cusps)

`L14n62525` is not proposed as a replacement — it is a 14-crossing link with no
structural motivation, and offering it would repeat exactly the census-fitting
this probe is documenting. It is reported because it shows the incumbent is not
even the best candidate in its own restricted class.

WHAT THIS DOES AND DOES NOT SHOW
----------------------------------
Component count is a **necessary** condition on the closure, so an empty
intersection is a real refutation while a survivor is only a candidate. The
restriction is to census manifolds with `A+1` cusps; a link exterior's cusp
count is its component count, and the census is not exhausted by link
exteriors, so the counts above are upper bounds on true link candidates and the
emptiness at `2H`/`3H` only strengthens.

It does **not** show that `6_2`, `8_11` and `L6a4` are the wrong objects for
whatever `K` the conjecture intends — the registry carries `knot_name` and
`binding_link_name` as separate fields, and the audit is careful that only the
*identification with the closure of the canonical mass word* is excluded. What
is new is that the exclusion now covers `A = 3`, and that the substrate's own
derived invariant leaves nothing behind at `A = 2, 3`.

Consistent with `docs/audits/2026-08-25-atom-word-closures-are-not-hyperbolic.md`:
if the closure is non-hyperbolic it is in no cusped hyperbolic census at all,
which is one reason the intersection is empty.

DISCIPLINE
----------
No fit; no wiring; no tier change; no knot proposed. Volumes come from SnapPy
and are cross-checked against the canonical `knot_volumes.py` registry.

-- Ref: [manuscript] bean t7qv (Gap #2); prior: qou-8ms1,
   docs/audits/2026-08-25-knot-id-is-an-admitted-fit.md
"""
from __future__ import annotations

import math
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
sys.path.insert(0, str(COMP / "substrate"))
sys.path.insert(0, str(COMP))
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from codata_constants import (  # noqa: E402
    M_E_MEV,
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
)
from knot_volumes import (  # noqa: E402
    VOL_6_2_MPF,
    VOL_8_11_MPF,
    VOL_BORROMEAN_MPF,
)
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402

try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except Exception:  # pragma: no cover
    _HAVE_WB = False

set_compute_dps()

# (atom, B_AME, hand-picked ρ, knot, canonical Vol, components of that link, A).
# Every numeric is mpf; SnapPy's census slicing is the only float boundary.
PICKS = [
    ("2H",  AME_B_DEUTERON_MEV_VALIDATION, 1, "6_2",  VOL_6_2_MPF,       1, 2),
    ("3H",  AME_B_TRITIUM_MEV_VALIDATION,  2, "8_11", VOL_8_11_MPF,      1, 3),
    ("3He", AME_B_HE3_MEV_VALIDATION,      2, "L6a4", VOL_BORROMEAN_MPF, 3, 3),
]

# The ²H *binding* link, carried in a separate registry field from knot_name.
HOPF_COMPONENTS = 2


def cycle_count(word, n: int) -> int:
    """Components of the closure = cycles of the underlying permutation.

    Branch-independent: `sigma_g` and `sigma_g^-1` are the same transposition,
    so no crossing-sign convention or superposition resolution can change this.
    """
    p = list(range(n))
    for (_c, _d, g) in word:
        p[g], p[g + 1] = p[g + 1], p[g]
    seen = [False] * n
    cycles = 0
    for i in range(n):
        if not seen[i]:
            cycles += 1
            j = i
            while not seen[j]:
                seen[j] = True
                j = p[j]
    return cycles


def chain_bonds(Z: int, N: int) -> list[str]:
    """Bond types along the chain, protons first then neutrons."""
    seq = ["p"] * Z + ["n"] * N
    return [seq[i] + seq[i + 1] for i in range(len(seq) - 1)]


def sweep_cycle_laws() -> dict:
    """Measure `c_free` and `c_atom` across (Z, N), conventions, multiplicities."""
    mults = [(1, 1, 1), (2, 1, 1), (1, 2, 1), (1, 1, 2), (2, 3, 2),
             (3, 3, 3), (2, 2, 2), (1, 3, 5), (4, 1, 1)]
    free_tested = free_bad = atom_tested = atom_bad = 0
    for Z in range(6):
        for N in range(6):
            A = Z + N
            if not (2 <= A <= 6):
                continue
            free_tested += 1
            if cycle_count(atom_braid_word_3A(Z, N, include_inter=False),
                           3 * A) != 2 * A:
                free_bad += 1
            for conv in ("bring_color_weighted", "strict_averaged"):
                for m_pp, m_pn, m_nn in mults:
                    mm = {"pp": m_pp, "pn": m_pn, "np": m_pn, "nn": m_nn}
                    w = atom_braid_word_3A(
                        Z, N, include_inter=True, pn_convention=conv,
                        m_pp=m_pp, m_pn=m_pn, m_nn=m_nn)
                    odd = sum(1 for b in chain_bonds(Z, N) if mm[b] % 2 == 1)
                    atom_tested += 1
                    if cycle_count(w, 3 * A) != 2 * A - odd:
                        atom_bad += 1
    return {"free_tested": free_tested, "free_deviations": free_bad,
            "atom_tested": atom_tested, "atom_deviations": atom_bad}


def _censuses():
    """SnapPy censuses, or `None` when SnapPy is absent.

    `m_tau_census_sweep.py` imports SnapPy unguarded; this probe guards so the
    derived-arity half — which needs no census — still reports without it.
    """
    try:
        import snappy  # noqa: PLC0415
    except Exception:
        return None, None
    return snappy, [
        ("OrientableCuspedCensus", snappy.OrientableCuspedCensus()),
        ("HTLinkExteriors", snappy.HTLinkExteriors()),
    ]


def window_counts(censuses, vol_target, vol_pick, want_cusps: int) -> dict:
    """Census manifolds at least as close as the pick, and how many have
    the derived component count.

    The window is the pick's own error, so no tolerance is chosen. Bounds are
    widened one ulp before the float cast SnapPy requires, so the count can
    only over-report — the direction that keeps an empty result honest.
    """
    d = abs(vol_pick - vol_target)
    lo = math.nextafter(float(vol_target - d), -math.inf)
    hi = math.nextafter(float(vol_target + d), math.inf)
    total = right_arity = 0
    for _name, cen in censuses:
        for m in cen[lo:hi]:
            total += 1
            if m.num_cusps() == want_cusps:
                right_arity += 1
    return {"in_volume_window": total, "with_derived_arity": right_arity}


def main() -> int:
    snappy, censuses = _censuses()
    assertions, rows = [], []

    # ── A1/A2. The substrate fixes the closure's component count ──────
    laws = sweep_cycle_laws()
    print("Gap #2 — what does the substrate actually fix about the knot?")
    print()
    print("  the closure's component count, and it is branch-independent:")
    print(f"    c_free = 2A ................................ "
          f"{laws['free_tested'] - laws['free_deviations']}/{laws['free_tested']} exact")
    print(f"    c_atom = 2A - #(odd-multiplicity bonds) ..... "
          f"{laws['atom_tested'] - laws['atom_deviations']}/{laws['atom_tested']} exact")
    print("    at unit multiplicity this is c_atom = A + 1 = 3, 4, 4, 5")
    print("    for 2H, 3H, 3He, 4He — corroborating, by a different route,")
    print("    QOU.MassTheory.ClassicalTraceFloor (bean qou-zrx2, sorry-free).")

    ok = laws["free_deviations"] == 0
    print(f"\n  A1  c_free = 2A holds with no deviations ................. "
          f"{'PASS' if ok else 'FAIL'}")
    assertions.append(("c_free_equals_2A", ok,
                       f"{laws['free_deviations']} deviations in "
                       f"{laws['free_tested']} cases"))

    ok = laws["atom_deviations"] == 0
    print(f"  A2  c_atom = 2A - #odd-bonds holds with no deviations .... "
          f"{'PASS' if ok else 'FAIL'}")
    assertions.append(("c_atom_equals_2A_minus_odd_bonds", ok,
                       f"{laws['atom_deviations']} deviations in "
                       f"{laws['atom_tested']} cases"))

    # ── A3. Every assignment fails the derived arity ──────────────────
    print()
    print("  the assigned links against it:")
    print(f"    {'atom':5s} {'link':16s} {'components':>10s} {'required':>9s}   verdict")
    mismatches = []
    checks = [(a, k, c, A) for a, _B, _r, k, _V, c, A in PICKS]
    checks.insert(1, ("2H", "Hopf L2a1 (bind)", HOPF_COMPONENTS, 2))
    for atom, link, comps, A in checks:
        need = A + 1
        bad = comps != need
        mismatches.append(bad)
        print(f"    {atom:5s} {link:16s} {comps:>10d} {need:>9d}   "
              f"{'MISMATCH' if bad else 'match'}")
    ok = all(mismatches)
    print(f"\n  A3  every assigned link fails the derived arity .......... "
          f"{'PASS' if ok else 'FAIL'}")
    print("      (the 2H rows reproduce the 2026-08-25 audit; 3H and 3He are new)")
    assertions.append(("all_assignments_fail_derived_arity", ok,
                       "; ".join(f"{a}:{k} {c} vs {A + 1}"
                                 for (a, k, c, A) in checks)))

    # ── A4/A5. Arity ∧ volume ─────────────────────────────────────────
    if censuses is not None:
        print()
        print("  intersecting the derived arity with the volume window:")
        print(f"    {'atom':5s} {'knot':6s} {'err%':>8s} {'in window':>10s} "
              f"{'+ arity':>8s}")
        empties, degeneracy = [], {}
        for atom, B, rho, knot, vol, _comps, A in PICKS:
            vol_target = B / (M_E_MEV * rho)
            b_pred = rho * M_E_MEV * vol
            err = (b_pred - B) / B * 100
            wc = window_counts(censuses, vol_target, vol, A + 1)
            degeneracy[atom] = wc["in_volume_window"]
            empties.append((atom, wc["with_derived_arity"]))
            rows.append({
                "atom": atom, "knot": knot, "rho_handpicked": rho,
                "B_AME_MeV": fmt(B), "vol": fmt(vol),
                "vol_target": fmt(vol_target), "B_pred_MeV": fmt(b_pred),
                "err_pct": fmt(err), "derived_components": A + 1, **wc,
            })
            print(f"    {atom:5s} {knot:6s} {mp.nstr(err, 4):>8s} "
                  f"{wc['in_volume_window']:>10,} {wc['with_derived_arity']:>8,}")

        ok = all(n == 0 for a, n in empties if a in ("2H", "3H"))
        print(f"\n  A4  at 2H and 3H the derived class is EMPTY ............. "
              f"{'PASS' if ok else 'FAIL'}")
        print("      no census manifold has both the derived component count")
        print("      and a volume matching as well as the named knot does —")
        print("      the named knot included. This is the audit's question")
        print("      answered: the class contains nothing.")
        assertions.append(("arity_and_volume_intersection_empty_at_A2_A3", ok,
                           f"survivors {dict(empties)}"))

        # Guard: the degeneracy the prior audit measured is reproduced.
        prior = {"2H": 796, "3H": 1101, "3He": 26671}
        ok = all(abs(degeneracy[a] - prior[a]) <= max(5, prior[a] * 0.01)
                 for a in prior)
        print(f"\n  A5  reproduces the 2026-08-25 audit's census degeneracy .. "
              f"{'PASS' if ok else 'FAIL'}")
        print(f"      prior (strictly closer, OCC only): {prior}")
        print(f"      here (at least as good, OCC+HTLink): {degeneracy}")
        assertions.append(("reproduces_prior_census_degeneracy", ok,
                           f"prior {prior}; here {degeneracy}"))

    print()
    print("### VERDICT: the substrate fixes the closure arity at A+1, and all")
    print("    three assignments violate it. Intersected with the volume")
    print("    window the candidate set is EMPTY at 2H and 3H. The complexity")
    print("    restriction the 2026-08-25 audit asked for exists, is derived,")
    print("    takes no B_AME input — and leaves nothing standing.")

    all_ok = all(a[1] for a in assertions)

    if _HAVE_WB:
        try:
            wb = WitnessBuilder("link-assignment-census-selectivity",
                                engine="snappy" if snappy else "python",
                                output_dir=COMP)
            wb.set_description(
                "Gap #2 (bean t7qv). The 2026-08-25 audit "
                "(qou-8ms1, knot-id-is-an-admitted-fit) asked for a complexity "
                "bound on K derived from the substrate with no B_AME input, "
                "then whether the volume match is unique inside that class. "
                "This supplies one — the closure's COMPONENT COUNT, fixed by "
                "the permutation of the canonical word and identical on every "
                "branch since sigma and sigma^-1 are the same transposition. "
                "Measured exact: c_free = 2A (0 deviations) and c_atom = 2A - "
                "#(odd-multiplicity bonds) (414/414), = A+1 at unit "
                "multiplicity, corroborating QOU.MassTheory.ClassicalTraceFloor "
                "by an independent route. All three assignments FAIL it: 6_2 "
                "(1 vs 3), 8_11 (1 vs 4), L6a4 (3 vs 4) — the 3H and 3He rows "
                "are new, the audit reached only 2H. Intersected with each "
                "pick's own volume window the class is EMPTY at 2H (0 of 799) "
                "and 3H (0 of 1,102), and 29 of 26,843 at 3He. No fit; no "
                "wiring; no knot proposed.")
            wb.add_data("cycle_count_laws", laws)
            wb.add_data("assignment_arity", [
                {"atom": a, "link": k, "components": c, "required_A_plus_1": A + 1}
                for (a, k, c, A) in checks])
            wb.add_data("picks", rows)
            wb.add_data("snappy_version", snappy.version() if snappy else None)
            wb.add_data("census_sizes",
                        {n: len(c) for n, c in censuses} if censuses else None)
            for name, passed, detail in assertions:
                wb.add_assertion(
                    name=name, computed=str(int(bool(passed))), expected="1",
                    tolerance=0, source=detail)
            wb.add_caveat(
                "Component count is a NECESSARY condition on the closure, so an "
                "empty intersection refutes while a survivor is only a "
                "candidate. Cusp count equals component count for link "
                "exteriors and the census is not exhausted by link exteriors, "
                "so the arity-restricted counts are UPPER bounds on genuine "
                "link candidates — the emptiness at 2H/3H only strengthens.")
            wb.add_caveat(
                "The census-degeneracy measurement (A5) is prior work, "
                "docs/audits/2026-08-25-knot-id-is-an-admitted-fit.md; it is "
                "re-measured here as a guard, not claimed. The counts differ "
                "slightly because that audit counted STRICTLY closer over "
                "OrientableCuspedCensus alone and this counts AT LEAST AS GOOD "
                "over OCC + HTLinkExteriors.")
            wb.add_caveat(
                "L14n62525 (Vol 7.597116, +0.598%) beats L6a4 (-2.969%) inside "
                "3He's arity-restricted class. It is NOT proposed as a "
                "replacement — a 14-crossing link with no structural motivation "
                "would repeat the census-fitting this probe documents. It is "
                "reported only to show the incumbent is not the best candidate "
                "in its own class.")
            out = wb.save()
            print(f"\nWitness: {out}")
        except Exception as e:  # pragma: no cover
            print(f"\n(witness emit skipped: {e})")

    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
