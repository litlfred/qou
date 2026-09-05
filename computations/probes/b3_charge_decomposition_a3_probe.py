#!/usr/bin/env python3
"""The A=3 charge decomposition: which part of b3 the framework can even address.

WHAT THE CORPUS ALREADY SETTLED (not disturbed here).

  * Any saturating product model `B(S) = c(1 - PROD f)` with `f in [0,1]` has a
    non-positive beyond-pairwise 3-body content -- Lean-proved sorry-free,
    `QOU.BraidKnot.Cluster.productModel_3body_nonpos`.
  * The only pairwise escape (enhancing `f > 1`) is foreclosed: every canonical
    interface factor at q0 lies in (0,1).
  * A non-product combiner escapes the theorem, and the chirality-weighted trace
    `sum_lambda y_lambda sgn(w0^{S_lambda'}) chi_lambda` does flip the sign.
    `docs/audits/2026-06-23-interface-operator-derivation-and-4body-assembly.md`
    records this, with the honest caveat that the magnitude is "10-24x" short.

WHAT THIS ADDS.

That "10-24x" is a RANGE because it was measured per atom: ~24x at 3H, ~8.7x at
3He. A range invites the reading that one unknown constant is missing and the
spread is noise. It is not noise, and the two numbers are not two estimates of
one quantity -- 3H and 3He are MIRROR nuclei, and essentially all of what
separates them is Coulomb.

  b3(3H) - b3(3He) = B(3H) - B(3He)                       exactly, since the
                                                          pair-additive 3*B(2H)
                                                          cancels in the difference
                   = 0.763755 MeV

  and that difference IS the Coulomb displacement energy, up to the Nolen-Schiffer
  residual (a known ~5-10% charge-symmetry-breaking anomaly, not accounted for by
  Coulomb alone -- see nolen1969).

So the honest decomposition of the A=3 data is into a charge-SYMMETRIC part,
which the strong channel is responsible for, and a charge-ANTIsymmetric part,
which is the EM channel:

  b3_sym  = (b3(3H) + b3(3He)) / 2     <- what a strong-channel object must supply
  b3_asym = (b3(3H) - b3(3He)) / 2     <- Coulomb (+ Nolen-Schiffer residual)

This probe splits every candidate 3-body object the same way and reports both
halves separately. Two consequences follow, and neither is visible in a per-atom
comparison:

  1. The scale question becomes ONE number per candidate, not a range. The
     "10-24x" for the chirality route is 14.5x on the symmetric part -- and the
     range was never the candidate's spread, it was the Coulomb splitting leaking
     into a strong-channel comparison.

  2. The antisymmetric part is a direct measurement of how much EM channel the
     framework's A=3 objects carry. The per-bond factors are f_pp = z,
     f_nn = z - h, f_pn = z - h(1/2 - delta/4): purely strong-channel, with no
     Coulomb term anywhere. Whatever asymmetry they produce is a byproduct of
     the pp/nn factor difference, and this probe measures its sign and size
     against the Coulomb displacement it would have to reproduce.

An earlier version of this probe reported the cross-atom ORDERING as a
discriminator among 3-body candidates. That was wrong-headed and is withdrawn:
the ordering of the mirror pair is a Coulomb observable, so ranking strong-channel
candidates by it grades them on a channel none of them has. The ordering FACTS are
still reported below, because they are correct and they are what makes the point;
they are simply not evidence about which 3-body operator is right.

EXPLORATORY -- audit + witness only. No production wiring, no fit: every ratio is
reported, none is solved for, and nothing introduced here feeds anything.

DATA PROVENANCE. All source witnesses are proton-pinned (q0 = 1.10997858275138...)
and share E0 = 4.185981363294... MeV, so there is no ideal/experimental layer
straddle. Values are read as strings and carried as mpmath.mpf; nothing is
computed in float.

## References

- [nolen1969] Nolen & Schiffer, "Coulomb Energies", Ann. Rev. Nucl. Sci. 19, 471.
"""
from __future__ import annotations

import json
import sys
import time as _time
from pathlib import Path

_T0 = _time.monotonic()

import mpmath as mp

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)
from _precision import set_compute_dps  # noqa: E402
from codata_constants import (
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
)

try:  # P30 provenance stamp; optional so a bare container still runs
    from qou_substrate.witness import WitnessBuilder as _WitnessBuilder
except ImportError:  # pragma: no cover
    from witness_base import WitnessBuilder as _WitnessBuilder

set_compute_dps()

TRIANGLE_W = _COMP / "binding-triangle-3body-cluster.witness.json"
CHIRAL_W = _COMP / "chirality-weighted-3body-cluster.witness.json"
STRUCT_W = _COMP / "structured-combiner-and-triangle.witness.json"

# AME2020 binding energies, as the source probes define them.
AME = {"T": AME_B_TRITIUM_MEV_VALIDATION, "3He": AME_B_HE3_MEV_VALIDATION}
B2 = AME_B_DEUTERON_MEV_VALIDATION
ATOMS = ["T", "3He"]
CANONICAL_CONV = "bring_color_weighted (canonical, R3)"


def _load(path: Path) -> dict:
    with path.open() as fh:
        return json.load(fh)


def _split(v: dict[str, mp.mpf]) -> tuple[mp.mpf, mp.mpf]:
    """Charge-symmetric and charge-antisymmetric parts of a mirror-pair quantity."""
    return (v["T"] + v["3He"]) / 2, (v["T"] - v["3He"]) / 2


def main() -> int:
    tri, chi, st = _load(TRIANGLE_W), _load(CHIRAL_W), _load(STRUCT_W)

    b3 = {a: AME[a] - 3 * B2 for a in ATOMS}
    b3_sym, b3_asym = _split(b3)

    tri_rows = {r["atom"]: r for r in tri["data"]["rows"]
                if r["pn_convention"] == CANONICAL_CONV}
    chi_rows = {r["atom"]: r for r in chi["data"]["rows"]}
    st_rows = {r["atom"]: r for r in st["data"]["rows"]}

    candidates: dict[str, dict[str, mp.mpf]] = {
        "product_beyond_pairwise": {a: mp.mpf(tri_rows[a]["beyond_pairwise_MeV"]) for a in ATOMS},
        "product_two_bond_only": {a: mp.mpf(tri_rows[a]["two_bond_MeV"]) for a in ATOMS},
        "product_three_bond_only": {a: mp.mpf(tri_rows[a]["three_bond_MeV"]) for a in ATOMS},
        "joint_trace_abs_c3": {a: mp.mpf(chi_rows[a]["abs_c3_MeV"]) for a in ATOMS},
        "joint_trace_signed_c3": {a: mp.mpf(chi_rows[a]["signed_c3_MeV"]) for a in ATOMS},
        "joint_trace_chiral_c3": {a: mp.mpf(chi_rows[a]["chiral_c3_MeV"]) for a in ATOMS},
        "chiral_c3_two_bond": {a: mp.mpf(st_rows[a]["c3_chiral_MeV"]) for a in ATOMS},
        "chiral_joint_triangle": {a: mp.mpf(st_rows[a]["triangle_chiral_joint_MeV"]) for a in ATOMS},
        "chiral_joint_longrange": {a: mp.mpf(st_rows[a]["chiral_joint_MeV"]) for a in ATOMS},
        "abs_joint_triangle": {a: mp.mpf(st_rows[a]["triangle_abs_joint_MeV"]) for a in ATOMS},
    }

    print("=" * 84)
    print("A=3 charge decomposition of the 3-body cumulant")
    print("=" * 84)
    print(f"  b3(3H)  = {mp.nstr(b3['T'], 8):>12s} MeV")
    print(f"  b3(3He) = {mp.nstr(b3['3He'], 8):>12s} MeV")
    print(f"  b3_sym  = {mp.nstr(b3_sym, 8):>12s} MeV   <- strong channel's job")
    print(f"  b3_asym = {mp.nstr(b3_asym, 8):>12s} MeV   <- Coulomb displacement / 2")
    print(f"  (full displacement B(3H)-B(3He) = {mp.nstr(2 * b3_asym, 8)} MeV,")
    print("   which is Coulomb up to the Nolen-Schiffer residual)")
    print()
    print(f"  {'candidate':26s} {'sym':>11s} {'asym':>11s} {'b3_sym/sym':>11s} "
          f"{'asym/b3_asym':>13s}")
    print("  " + "-" * 82)

    rows = []
    for name, vals in candidates.items():
        s, a = _split(vals)
        sym_ratio = b3_sym / s if s != 0 else None
        asym_frac = a / b3_asym
        print(f"  {name:26s} {mp.nstr(s, 6):>11s} {mp.nstr(a, 6):>11s} "
              f"{(mp.nstr(sym_ratio, 6) if sym_ratio is not None else 'n/a'):>11s} "
              f"{mp.nstr(asym_frac, 4):>13s}")
        rows.append({
            "candidate": name,
            "value_3H_MeV": mp.nstr(vals["T"], 10),
            "value_3He_MeV": mp.nstr(vals["3He"], 10),
            "sym_MeV": mp.nstr(s, 10),
            "asym_MeV": mp.nstr(a, 10),
            "sym_attractive": bool(s > 0),
            "b3_sym_over_sym": (mp.nstr(sym_ratio, 10) if sym_ratio is not None else None),
            "asym_over_b3_asym": mp.nstr(asym_frac, 10),
            "asym_sign_matches_coulomb": bool(a > 0),
        })

    # Mechanism: the two competing non-EM sources of charge asymmetry.
    tau_p = mp.mpf(tri["parameters"]["tau_p"])
    tau_n = mp.mpf(tri["parameters"]["tau_n"])
    # tau_vac(3He)/tau_vac(3H) = (tau_p^2 tau_n)/(tau_p tau_n^2) = tau_p/tau_n.
    tau_ratio = tau_p / tau_n
    # The triangle witness records one_bond = c*sum(x) and three_bond = c*prod(x)
    # with c = E0*tau_vac, so the bond-only ratios follow by dividing tau_ratio out.
    # No recomputation and no new import: this is algebra on the recorded numbers.
    sumx_ratio = (mp.mpf(tri_rows["3He"]["one_bond_MeV"])
                  / mp.mpf(tri_rows["T"]["one_bond_MeV"])) / tau_ratio
    prodx_ratio = (mp.mpf(tri_rows["3He"]["three_bond_MeV"])
                   / mp.mpf(tri_rows["T"]["three_bond_MeV"])) / tau_ratio

    chiral_names = [n for n in candidates if n.startswith("chiral") or "chiral" in n]
    chiral_asym_all_wrong = all(
        not next(r for r in rows if r["candidate"] == n)["asym_sign_matches_coulomb"]
        for n in chiral_names)
    max_asym_frac = max(abs(mp.mpf(r["asym_over_b3_asym"])) for r in rows)
    right_signed = [r["candidate"] for r in rows if r["asym_sign_matches_coulomb"]]
    best_right_frac = max(
        [mp.mpf(r["asym_over_b3_asym"]) for r in rows if r["asym_sign_matches_coulomb"]],
        default=mp.mpf(0))

    print()
    print("=" * 84)
    print("READING (scope-limited -- n = 2 atoms; this is a decomposition, not a closure)")
    print("=" * 84)
    print("  1. The chirality route's magnitude gap is ONE number, not a 10-24x range.")
    print("     On the charge-symmetric part the 2-bond chiral c3 is 14.5x short and the")
    print("     triangle-closed one 8.4x short. The corpus's range was the Coulomb")
    print("     splitting leaking into a strong-channel comparison, not candidate spread.")
    print()
    print("  2. EVERY chiral variant in the corpus -- 2-bond, triangle-closed, and with")
    print("     the long-range 1-3 bond -- has an antisymmetric part of the WRONG SIGN:")
    print(f"     chiral_asym_all_wrong_sign = {chiral_asym_all_wrong}")
    print("     So the inversion is not an artifact of the 2-adjacent-bond truncation the")
    print("     2026-06-23 audit flags. Closing the triangle does not repair it either.")
    print()
    print(f"  3. NINE of the ten candidates get the mirror asymmetry BACKWARDS.")
    print(f"     Only {right_signed or 'none'} has a positive asym, at "
          f"{mp.nstr(best_right_frac * 100, 4)}% of the Coulomb displacement.")
    print("     Every chiral variant, both signed and abs joint traces, and the whole")
    print("     beyond-pairwise product content bind 3He MORE than 3H -- opposite to")
    print("     reality. (The wrong-signed ones reach larger MAGNITUDES, up to")
    print(f"     {mp.nstr(max_asym_frac * 100, 4)}%, which is worse, not better.)")
    print()
    print("  4. MECHANISM. The framework's A=3 charge asymmetry comes from two competing")
    print("     non-EM sources, and which one wins is term-dependent -- that is why the")
    print("     sign is not stable across candidates:")
    print(f"       vacuum factor   tau_vac(3He)/tau_vac(3H) = {mp.nstr(tau_ratio, 8)}  (>1: favours 3He)")
    print(f"       bond sum        sum_x(3He)/sum_x(3H)     = {mp.nstr(sumx_ratio, 8)}  (<1: favours 3H)")
    print(f"       bond product    prod_x(3He)/prod_x(3H)   = {mp.nstr(prodx_ratio, 8)}  (<1: favours 3H)")
    print("     The 1-bond term is dominated by tau_vac and lands on 3He; the 3-bond term")
    print("     is dominated by the triple product and lands on 3H. Neither source is")
    print("     electromagnetic: tau_p/tau_n is a vacuum-trace ratio and f_pp > f_nn is a")
    print("     strong-channel factor difference. So the sign of the mirror splitting in")
    print("     this framework is an accident of which term dominates, not a prediction.")
    print()
    print("  Consequence for the search: a cross-atom ordering test over the mirror pair")
    print("  cannot discriminate 3-body candidates, because it grades them on a channel")
    print("  none of them has. Candidates must be compared on b3_sym; the mirror splitting")
    print("  is a separate, EM-channel obligation.")

    assertions = [
        {"name": "b3 antisymmetric part equals half the 3H-3He binding difference",
         "passed": bool(abs(2 * b3_asym - (AME["T"] - AME["3He"])) < mp.mpf("1e-40"))},
        {"name": "every chiral variant has wrong-signed charge asymmetry",
         "passed": bool(chiral_asym_all_wrong)},
        {"name": "at most one candidate has a right-signed charge asymmetry",
         "passed": bool(len(right_signed) <= 1)},
        {"name": "the right-signed candidate supplies under half the Coulomb displacement",
         "passed": bool(best_right_frac < mp.mpf("0.5"))},
        {"name": "tau_vac favours 3He while the bond product favours 3H (competing sources)",
         "passed": bool(tau_ratio > 1 and prodx_ratio < 1)},
    ]
    print()
    for a_ in assertions:
        print(f"  assertion: {a_['name']} -> {a_['passed']}")

    out = {
        "engine": "mpmath",
        "engineVersion": f"mpmath {mp.__version__}",
        "computation": "b3-charge-decomposition-a3",
        "scriptFile": "b3_charge_decomposition_a3_probe.py",
        "description": (
            "Charge-symmetric / charge-antisymmetric decomposition of the A=3 3-body "
            "cumulant b3 and of every candidate 3-body object in the corpus. 3H and 3He "
            "are mirror nuclei, so b3(3H)-b3(3He) is exactly the binding difference and "
            "is the Coulomb displacement up to the Nolen-Schiffer residual. FINDINGS: "
            "(1) the chirality route's '10-24x' magnitude gap is one number per variant "
            "on the symmetric part -- 14.5x (2-bond), 8.4x (triangle-closed) -- the range "
            "was Coulomb splitting leaking into a strong-channel comparison; (2) every "
            "chiral variant, including triangle-closed and long-range, has a WRONG-SIGNED "
            "charge asymmetry, so the inversion is not an artifact of the 2-adjacent-bond "
            "truncation; (3) no candidate supplies more than ~22% of the Coulomb "
            "displacement and the per-bond factors carry no EM term, so the A=3 charge "
            "asymmetry is a missing CHANNEL, not a wrong 3-body operator. Scope-limited: "
            "n=2 atoms, a decomposition rather than a closure. Exploratory; no production "
            "wiring, no fit."),
        "sources": [
            {"witness": TRIANGLE_W.name, "scriptHash": tri.get("scriptHash"),
             "convention_row_used": CANONICAL_CONV},
            {"witness": CHIRAL_W.name, "scriptHash": chi.get("scriptHash"),
             "q0Anchor": chi.get("q0Anchor")},
            {"witness": STRUCT_W.name, "scriptHash": st.get("scriptHash")},
        ],
        "parameters": {
            "b3_definition": "AME(A=3) - 3 * B(2H)",
            "B2_MeV": str(B2),
            "AME_MeV": {a: str(AME[a]) for a in ATOMS},
            "free_parameters": 0,
        },
        "data": {
            "b3_empirical_MeV": {a: mp.nstr(b3[a], 10) for a in ATOMS},
            "b3_sym_MeV": mp.nstr(b3_sym, 10),
            "b3_asym_MeV": mp.nstr(b3_asym, 10),
            "coulomb_displacement_MeV": mp.nstr(2 * b3_asym, 10),
            "rows": rows,
            "chiral_asym_all_wrong_sign": bool(chiral_asym_all_wrong),
            "right_signed_asym_candidates": right_signed,
            "best_right_signed_asym_fraction_of_coulomb": mp.nstr(best_right_frac, 10),
            "mechanism": {
                "tau_vac_ratio_3He_over_3H": mp.nstr(tau_ratio, 10),
                "bond_sum_ratio_3He_over_3H": mp.nstr(sumx_ratio, 10),
                "bond_product_ratio_3He_over_3H": mp.nstr(prodx_ratio, 10),
                "note": ("Two competing NON-EM sources: tau_p/tau_n favours 3He, "
                         "f_pp > f_nn (so x_pp < x_nn) favours 3H. Which dominates is "
                         "term-dependent, so the sign of the mirror splitting is an "
                         "accident of the term, not a prediction."),
            },
            "max_abs_asym_fraction_of_coulomb": mp.nstr(max_asym_frac, 10),
        },
        # Every source witness is proton-pinned; this probe is pure algebra on
        # their recorded numbers, so it inherits that anchor rather than choosing
        # one. Stamped explicitly per AGENTS.md "Say which pin you used" -- an
        # unstamped witness is a Q0_ANCHOR_MISSING red on the q0-anchor gate.
        "q0Anchor": "proton",
        "q0Value": tri["parameters"]["q_0"],
        "assertions": assertions,
        "allPassed": all(a_["passed"] for a_ in assertions),
        "durationMs": int((_time.monotonic() - _T0) * 1000),
    }
    dest = _COMP / "b3-charge-decomposition-a3.witness.json"
    with dest.open("w") as fh:
        # P30: add the staleness provenance (scriptHash / commitSha /
        # engine) that a hand-rolled dump cannot get from build().
        _WitnessBuilder.stamp_staleness_metadata(
            out, script_path=__file__, engine="python",
            q0_anchor=False,
            q0_anchor_reason=(
                "the producer performs no q0-dependent computation "
                "(zero q_parameter / q_at / Q_50_DIGIT references)"),
        )
        json.dump(out, fh, indent=1)
        fh.write("\n")
    print(f"\n  wrote {dest.relative_to(_COMP.parent)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
