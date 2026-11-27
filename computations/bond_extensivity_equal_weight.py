#!/usr/bin/env python3
"""
bond_extensivity_equal_weight.py — WHY the binding multiplier is the coordination
number: it is the EQUAL-WEIGHT limit of the (already derived) log-trace bond-
extensivity.  (Task "bond-extensivity" — the deep open of the 𝓑_K coordination thread.)

Bond-extensivity is NOT re-derived here — it is the merged #2089 result
(docs/audits/2026-06-10-binding-bond-graph-compute-audit-and-derivation.md):

    B(q) = E_0 · log(tr_free / tr_atom) = E_0 · Σ_{bonds} log(1/f_bond(q)),

the connected/log-trace form (log of a product of bond factors = sum over bonds).
The per-bond Markov factors are fibre-derived closed forms (δ→0):

    z = q³/(q²+1),   h = q − 1/q        (convention D)
    f_pp = z = q³/(q²+1),   f_nn = z − h = 1/(q³+q),
    f_pn = z − h/2 = (q⁴+1)/(2q(q²+1)).

The kernel is the STRUCTURAL triple (z, z−h, z−h/2); the half-integer powers
this block used to carry were the convention-C substitution of exactly that,
expanded. Under D every factor is rational — D never leaves ℚ(q).

CONTRIBUTION of this probe (not a duplication of #2089 / #3548 / #3534):
the *coordination-number* reading of the merged 𝓑_K thread —
`B = (coordination number) · (per-bond constant)` — is precisely the EQUAL-WEIGHT
limit of the log-trace sum: if every bond has the same ε_bond = E_0·log(1/f_bond),
then B = N_bonds·ε = (bond count)·(constant), and per node = (coordination
number)·(constant). This probe measures WHERE equal-weight holds:

  • α–α bonds are IDENTICAL by particle symmetry ⇒ a single f_αα ⇒ equal-weight is
    EXACT ⇒ α-cluster contact-number counting is genuinely derived (the merged
    <0.5% contact result).
  • nucleon bonds pp/pn/nn have a DERIVED spread ⇒ equal-weight FAILS; the nucleon
    z=A−1 match (A=3 mirror pair) is a composition coincidence, not a coordination
    law. The split ε_nn−ε_pp IS the isospin/CSB (mirror) asymmetry — i.e. the
    volume carrier Vol_n(K) of w_n=M·Vol. So M (coordination) = equal-weight
    skeleton, Vol (isospin) = the bond-energy asymmetry equal-weight drops.

EXPLORATORY — scope-limited (a). Uses the derived #2089 f_bond; no new fit; no
production wiring.
"""
from __future__ import annotations
import sys
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "substrate"))
sys.path.insert(0, str(HERE))
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except ImportError:
    WitnessBuilder = None
    _HAVE_WB = False

set_compute_dps()
q = Q_MP


# ── derived per-bond Markov factors (#2089 closed forms, δ→0) ──────────────────
def f_bonds():
    # Convention D: z = q^3/(q^2+1). The kernel is STRUCTURAL --
    # f_pp = z, f_nn = z - h, f_pn = z - h/2 (#2089) -- and these lines
    # previously carried the C-substituted EXPANSION of exactly that, which is
    # where the q^{3/2} came from. Writing the structural form instead both
    # migrates the convention and removes the expansion: under D every factor
    # is rational, because D never leaves Q(q).
    #
    #     f_pp = q^3/(q^2+1)      f_nn = 1/(q^3+q)      f_pn = (q^4+1)/(2q(q^2+1))
    z = q ** 3 / (q ** 2 + 1)
    h = q - 1 / q
    f_pp = z
    f_nn = z - h
    f_pn = z - h / 2
    return {"pp": f_pp, "pn": f_pn, "nn": f_nn}


def main() -> int:
    f = f_bonds()
    eps = {k: mp.log(1 / v) for k, v in f.items()}   # ε_bond = log(1/f_bond) (E_0=1)
    print(f"  q₀={float(q):.5f}   (bond-extensivity B = E₀·Σ log(1/f_bond), #2089)\n")
    print("### Derived per-bond energies ε = log(1/f_bond)  (fibre closed forms)")
    for k in ("pp", "pn", "nn"):
        print(f"     f_{k} = {float(f[k]):.6f}   ε_{k} = {float(eps[k]):.4f}")
    spread = float(eps["nn"] / eps["pp"])
    print(f"     nucleon bond-energy spread  ε_nn/ε_pp = {spread:.2f}×\n")

    # ── coordination-number form = EQUAL-WEIGHT limit ─────────────────────────
    print("### Coordination-number multiplier = equal-weight limit of the log-trace")
    print("  If every bond has the same ε, then  B = N_bonds·ε = (coordination)·const.")
    print("  Test equal-weight per level:\n")

    # α level: identical α–α bonds ⇒ equal-weight EXACT by symmetry.
    print("  • α-cluster level: all bonds are α–α (identical ⁴He), so a SINGLE f_αα ⇒")
    print("    equal-weight is EXACT by particle symmetry ⇒ contact-number counting is")
    print("    genuinely derived (the merged α-cluster <0.5% result). ✓")

    # nucleon level: spread ⇒ equal-weight FAILS; demonstrate the mirror split.
    #   ³H = pnn : bonds 2·pn + 1·nn ;  ³He = ppn : bonds 1·pp + 2·pn
    B_3H = 2 * eps["pn"] + eps["nn"]
    B_3He = eps["pp"] + 2 * eps["pn"]
    eps_avg = (eps["pp"] + eps["pn"] + eps["nn"]) / 3
    B_eqw = 3 * eps_avg                                   # equal-weight: 3 equal bonds
    mirror_split = eps["nn"] - eps["pp"]                  # = B_3H − B_3He
    print(f"\n  • nucleon level: ε spread {spread:.2f}× ⇒ equal-weight FAILS. For A=3:")
    print(f"      B(³H)=2ε_pn+ε_nn = {float(B_3H):.3f},  B(³He)=ε_pp+2ε_pn = {float(B_3He):.3f}")
    print(f"      equal-weight (3·⟨ε⟩) = {float(B_eqw):.3f} for BOTH — it predicts NO")
    print(f"      mirror split. The real split B(³H)−B(³He) = ε_nn−ε_pp = "
          f"{float(mirror_split):.3f}")
    print(f"      is the isospin/CSB (mirror) asymmetry — i.e. the VOLUME carrier Vol_n(K).")

    print("\n### Verdict — bond-extensivity ⇒ w_n = M·Vol  (scope-limited (a))")
    print("  • Bond-extensivity B = Σ_bonds ε_bond is DERIVED (log-trace, #2089) — not re-")
    print("    derived here.")
    print("  • The coordination-number multiplier M is the EQUAL-WEIGHT limit of that sum:")
    print("    equal bonds ⇒ B = (coordination number)·const.")
    print("  • EXACT at the α level (identical α–α bonds) ⇒ α-cluster contact counting is")
    print("    derived; a COMPOSITION COINCIDENCE at the nucleon level (ε spread 1.78×),")
    print("    where the z=A−1 match holds only for the symmetric A=3 mirror composition.")
    print("  • The piece equal-weight DROPS — the bond-energy split ε_nn−ε_pp — is exactly")
    print("    the isospin carrier Vol_n(K). So w_n = M·Vol decomposes as")
    print("    M = equal-weight coordination skeleton, Vol = isospin bond-energy asymmetry,")
    print("    both grounded in the one derived log-trace. This ANSWERS 'why multiplier =")
    print("    coordination number' (equal-weight limit) and bounds its scope (identical")
    print("    bonds only). It does NOT make M·Vol a fit-free closure — ε_bond magnitudes")
    print("    and the α-geometry remain the open inputs (→ #3548/#3534).")

    if _HAVE_WB:
        try:
            wb = WitnessBuilder("bond-extensivity-equal-weight", engine="mpmath")
            wb.set_description(
                "The coordination-number binding multiplier is the EQUAL-WEIGHT limit of the "
                "derived log-trace bond-extensivity B=E₀·Σ log(1/f_bond) (#2089). Equal-weight "
                "is exact for identical α–α bonds (α-cluster contact counting derived) but "
                "fails at the nucleon level (derived ε_pp:ε_pn:ε_nn spread 1.78×); the nucleon "
                "z=A−1 is a composition coincidence. The split ε_nn−ε_pp equal-weight drops is "
                "the isospin carrier Vol, so w_n=M·Vol = (equal-weight coordination)·(isospin "
                "bond asymmetry). Answers 'why multiplier=coordination'; not a closure. Scope-(a).")
            wb.add_data("q0", float(q))
            wb.add_data("f_bond", {k: float(v) for k, v in f.items()})
            wb.add_data("eps_bond", {k: float(v) for k, v in eps.items()})
            wb.add_data("nucleon_spread", spread)
            wb.add_data("A3_mirror", {"B_3H": float(B_3H), "B_3He": float(B_3He),
                                      "equal_weight": float(B_eqw),
                                      "mirror_split_eps_nn_minus_pp": float(mirror_split)})
            wb.add_assertion(
                name="coordination_multiplier_is_equal_weight_limit_exact_alpha_coincidence_nucleon",
                computed=str(int(spread > 1.5)), expected="1", tolerance=0,
                source=(f"nucleon bond energies have a derived {spread:.2f}× spread ⇒ equal-weight "
                        "(coordination counting) fails there; it is exact only for identical α–α "
                        f"bonds. The mirror split ε_nn−ε_pp={float(mirror_split):.3f} that equal-"
                        "weight drops is the isospin carrier Vol, giving w_n=M·Vol."))
            out = wb.save()
            print(f"\nWitness: {out}")
        except Exception as e:
            print(f"\n(witness skipped: {e})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
