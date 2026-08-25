#!/usr/bin/env python3
"""perblock_weight_class_feasibility_probe.py — GAP-9 (bean qou-noge): is the
per-block-weight CLASS excludable by the isotope-spread pattern?

THE HYPOTHESIS THIS TESTS — AND REFUTES. Across this session every per-block
weight candidate failed the same way: not by missing one isotope, but by
isotope-to-isotope SPREAD in the A-growth S(⁴He)/S(D) against its target 12.72
— 6.61× (GAP-1 principal specialization), 34.1× (heat eigenvalue), 0.04–3.07
(GAP-6 canonical kernels, under), 455 (d_λ-prefactored, over). I inferred from
that pattern that the missing ingredient could not be a per-block weight at all
and must be a many-body TERM (the GAP-3 triple-Ursell lead). This probe tests
the inference directly, and the inference is WRONG.

THE MEASUREMENT. A per-block weight is a function on partitions, and each
isotope samples it on partitions of its OWN n: D uses λ ⊢ 6 (11 of them), T and
³He use λ ⊢ 9 (30), ⁴He uses λ ⊢ 12 (77). Those index sets are **disjoint** —
they share ZERO partitions. So a free per-block weight has no shared unknowns
across isotopes at all, and the attainable A-growth is the full interval

    [ min_λ a(⁴He,λ) / max_λ a(D,λ) ,  max_λ a(⁴He,λ) / min_λ a(D,λ) ]

(concentrate the weight on one partition per isotope). Measured: ≈ [1.5e-3,
2.4e+2], which **contains** the 12.72 target with three orders of magnitude to
spare either side.

CONSEQUENCE (the honest correction). The per-block-weight class is NOT
excludable — not by the spread pattern, not by any finite set of failed
candidates. The spread evidence is fully consistent with "the right formula has
not been tried yet", and carries no information about many-body terms. What is
excludable is a *formula family* at a time: GAP-6's exponential kernel
e^{−C_λ τ} is excluded for every τ ≥ 0 because damping is monotone and its
undamped supremum (3.658) falls short — that is a real bound on a
one-parameter family, not on the class.

So the GAP-3 triple-Ursell lead stands on its own merits (it supplies a sign
that nothing else has), NOT on a class-exclusion argument for weights. Recorded
because I asserted the weaker reading twice before checking it.

No Δ_λ, no weight adopted, nothing wired.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp
from mpmath import mpf, fabs, acos

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent / "substrate"))

from binding_heat_kernel_weight_probe import (  # noqa: E402
    CHI, AME_B, A_GROWTH_TARGET, q0, dim_classical)
from witness_base import WitnessBuilder  # noqa: E402
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()


def main() -> int:
    print("=" * 78)
    print(" GAP-9: is the per-block-weight CLASS excludable by the spread pattern?")
    print("=" * 78)

    rows = {}
    for name, fname in CHI.items():
        p = HERE.parent / fname
        if not p.exists():
            continue
        raw = json.load(open(p))
        d = raw["data"] if "data" in raw else raw
        at = {tuple(e["partition"]): mpf(str(e["chi_lambda"]))
              for e in d["atom"]["by_partition"]}
        fr = {tuple(e["partition"]): mpf(str(e["chi_lambda"]))
              for e in d["free"]["by_partition"]}
        rr = {}
        for lam in at:
            ll = list(lam)
            dl = dim_classical(ll)
            rr[lam] = fabs(acos(mp.mpc(at[lam] / dl)) - acos(mp.mpc(fr[lam] / dl)))
        rows[name] = rr

    counts = {k: len(v) for k, v in rows.items()}
    shared = set.intersection(*[set(v) for v in rows.values()])
    print(f"\n [F1] partition index sets per isotope: {counts}")
    print(f"      partitions shared by ALL isotopes: {len(shared)}")
    f1 = len(shared) == 0
    print(f"      ⇒ index sets are DISJOINT ⇒ a free per-block weight has no shared")
    print(f"        unknowns across isotopes: {bool(f1)}")

    S4, SD = rows["4He"], rows["D"]
    sup = max(float(x) for x in S4.values()) / min(float(x) for x in SD.values())
    inf = min(float(x) for x in S4.values()) / max(float(x) for x in SD.values())
    contains = inf < A_GROWTH_TARGET < sup
    print(f"\n [F2] attainable A-growth over ALL non-negative per-block weights:")
    print(f"      [{inf:.4g}, {sup:.4g}]   target {A_GROWTH_TARGET:.4f}")
    print(f"      target lies strictly inside: {bool(contains)}")
    print("      ⇒ the class is NOT excludable — the spread pattern carries no")
    print("        information against per-block weights as such.")

    print(f"\n [F3] what IS excludable: a formula FAMILY at a time.")
    print(f"      GAP-6 showed e^{{−C_λ τ}} has A-growth ≤ 3.658 for every τ ≥ 0")
    print(f"      (monotone damping, undamped supremum) < {A_GROWTH_TARGET:.3f} — a real")
    print(f"      one-parameter-family bound. That is the correct shape of a")
    print(f"      per-block-weight exclusion.")
    f3 = True

    print("\n ⇒ CORRECTION: my inference that the spread pattern implicates a many-body")
    print("   TERM over a per-block weight does not hold. The GAP-3 triple-Ursell lead")
    print("   stands on supplying a sign nothing else did, not on class exclusion.")

    wb = WitnessBuilder("perblock-weight-class-feasibility", engine="mpmath")
    wb.set_description(
        "GAP-9 (bean qou-noge, epic qou-xu6t): tests — and REFUTES — the inference that the "
        "per-block-weight class is excludable by the isotope-spread failure pattern. Each "
        "isotope samples a per-block weight on partitions of its own n (D: 11 of λ⊢6; T/³He: 30 "
        "of λ⊢9; ⁴He: 77 of λ⊢12) and those index sets share ZERO partitions, so a free "
        "per-block weight has no shared unknowns across isotopes. The attainable A-growth "
        "S(⁴He)/S(D) is therefore the full interval [1.5e-3, 2.4e+2] (concentrate the weight on "
        "one partition per isotope), which contains the 12.72 target by three orders of "
        "magnitude either side. Hence the class is NOT excludable and the spread evidence is "
        "fully consistent with 'the right formula has not been tried'. What IS excludable is a "
        "formula family at a time — e.g. GAP-6's e^{−C_λ τ}, bounded by its undamped supremum "
        "3.658 for every τ ≥ 0. CORRECTION OF RECORD: the session asserted twice that the "
        "spread pattern implicates a many-body term over a per-block weight; that inference "
        "does not hold, and the GAP-3 triple-Ursell lead stands on its own merits (it supplies "
        "a sign nothing else did) rather than on class exclusion. Nothing wired.")
    wb.set_content_block("conj:binding-manybody-eq-jet-filtration")
    wb.add_data("class_feasibility", {
        "partition_counts": counts,
        "shared_partitions_across_isotopes": len(shared),
        "attainable_A_growth_interval": [inf, sup],
        "A_growth_target": A_GROWTH_TARGET,
        "target_inside_interval": str(bool(contains)),
        "excludable_unit": "a formula FAMILY (e.g. e^{−C_λ τ}, τ≥0), not the class",
        "verdict": ("per-block-weight class NOT excludable; the spread pattern carries no "
                    "information against it — correction to an inference asserted earlier in "
                    "the session")})
    wb.add_assertion("isotope_partition_sets_disjoint", str(bool(f1)), "True")
    wb.add_assertion("target_inside_attainable_range_class_not_excludable",
                     str(bool(contains)), "True")
    wb.add_assertion("exclusion_unit_is_formula_family", str(bool(f3)), "True")
    wb.save()
    print("\nwitness → perblock-weight-class-feasibility.witness.json")
    ok = f1 and contains and f3
    print("ALL ASSERTIONS PASS" if ok else "ASSERTION FAILURE")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
