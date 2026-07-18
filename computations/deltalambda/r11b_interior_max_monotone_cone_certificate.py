#!/usr/bin/env python3
"""
r11b_interior_max_monotone_cone_certificate.py — R11-b: a Farkas certificate that the ladder-miss
k=3 interior maximum CANNOT arise from the monotone additive cone ⇒ the missing binding channel is
necessarily NON-monotone (resonant) in k. (bean z2bn / round-11, follows the merged R11-a #3840.)

CONTEXT. R10 (merged) established that the Model-G miss `miss(k, A_light)` peaks at a FIXED interior
k=3 across all three `(kα)+X` ladders (X = n/d/t, A_light = 1/2/3). R11-a (#3840, merged) refuted the
multiplicative 3-factor closure and the pure Brunnian hard-gate, leaving the honest structure as an
additive 2-channel. R9 ASSERTED the P1 prune ("a non-negative additive cone cannot have a strict
interior maximum"). THIS PROBE upgrades that assertion to an explicit Farkas CERTIFICATE on the
actual merged 3-ladder miss data, and shows the exclusion is scope-(b) (a proved structural
impossibility, not a scope-(a) numerical near-miss).

THE CERTIFICATE (elementary, exact — no LP solver, no fit). Let B = {f_i(k)} be ANY family of basis
functions that are NON-DECREASING in k (f_i(k+1) ≥ f_i(k) for all k) — every additive structural
count is of this form: the constant 1, the α count k, the α-α pair count C(k,2), the α-α-α triple
count C(k,3), the core-α interface count k·A_light, …). Consider the linear functional

    φ  :=  e_{k=4} − e_{k=3}          (evaluate at k=4 minus at k=3).

For every non-decreasing f_i,  φ(f_i) = f_i(4) − f_i(3) ≥ 0. Hence for any non-negative combination
g = Σ_i c_i f_i  (c_i ≥ 0),  φ(g) = Σ_i c_i (f_i(4) − f_i(3)) ≥ 0, i.e. g(4) ≥ g(3): every element
of the monotone cone is non-decreasing from k=3 to k=4. But the miss has

    miss(4) − miss(3) < 0   on ALL THREE ladders   (n: −1.461, d: −4.186, t: −5.370 MeV).

So φ SEPARATES the miss from the cone: miss ∉ cone(B). The pair (k=3, k=4) with the strict decrease
is the Farkas witness. This is a scope-(b) exclusion — it holds for the WHOLE monotone additive
class simultaneously, via a proved invariant (monotonicity ⇒ φ ≥ 0), not a fit to any particular
basis. Therefore the missing binding channel is necessarily NON-MONOTONE in k — a genuine RESONANCE
(interior peak), consistent with R9's P1/P2 and now certified.

WHY THE FALL IS ALSO NOT A SEPARABLE PARITY FACTOR. #3808 floated a "bar-parity fall" as a separable
third factor. The fall ratio miss(4)/miss(3) is 0.485 / 0.281 / 0.333 across A_light = 1/2/3 — it is
A_light-DEPENDENT, so the fall does not factor out of A_light either. Combined with R11-a's
A_light-dependent k=2 envelope, the miss is IRREDUCIBLY 2D in (k, A_light): no product, no
additive-monotone sum, no separable parity factor reproduces it.

REDIRECT (formalize-first). The certified non-monotonicity is the R11-b Lean target ("a non-negative
combination of non-decreasing functions is non-decreasing, hence has no strict interior maximum" — a
clean order lemma). It also redirects the per-isotope binding closure AWAY from closed-form
k-envelopes and TOWARD the operator-valued branching combiner / confinement SDP (the mandated route),
where a resonant (non-monotone) k-profile is natural. No fit; scope-(b) via explicit certificate;
magnitudes not interpreted.

Audit: docs/audits/2026-07-18-r11b-interior-max-monotone-cone-certificate.md
"""
from __future__ import annotations
import json
import sys
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
WITNESS = HERE / "deuteron-ladder-falsification.witness.json"


def load_ladders():
    w = json.load(open(WITNESS))
    out = {}
    for key, Al in [("neutron_ladder_A_light_1", 1),
                    ("deuteron_ladder_A_light_2", 2),
                    ("triton_ladder_A_light_3", 3)]:
        out[Al] = {rec["k"]: rec["miss_MeV"] for rec in w[key].values()}
    return out


# candidate monotone (non-decreasing in k) additive structural basis functions
def basis(A_light):
    return {
        "const_1":      lambda k: 1.0,
        "alpha_count_k": lambda k: float(k),
        "pair_C(k,2)":  lambda k: float(comb(k, 2)),
        "triple_C(k,3)": lambda k: float(comb(k, 3)),
        "core_alpha_kA": lambda k: float(k * A_light),
    }


def main() -> int:
    lad = load_ladders()
    print("=== R11-b: Farkas certificate — the k=3 interior max is outside the monotone additive cone ===\n")

    # (1) confirm the strict interior maximum on all three ladders
    print("--- (1) strict interior maximum at k=3 (from merged R10 witness) ---")
    all_interior = True
    falls = {}
    for Al in (1, 2, 3):
        m2, m3, m4 = lad[Al][2], lad[Al][3], lad[Al][4]
        interior = (m3 > m2) and (m3 > m4)
        all_interior = all_interior and interior
        falls[Al] = m4 / m3
        print(f"  A_light={Al}: miss(2)={m2:7.3f} miss(3)={m3:7.3f} miss(4)={m4:7.3f}"
              f"  interior_max={interior}  Δ(4−3)={m4-m3:+.3f}")

    # (2) the separating functional φ = e_4 − e_3 : ≥0 on every non-decreasing basis fn, <0 on miss
    print("\n--- (2) Farkas certificate  φ = e_{k=4} − e_{k=3} ---")
    print("  φ(f) = f(4) − f(3).  For any NON-DECREASING f, φ(f) ≥ 0, so φ ≥ 0 on the whole")
    print("  monotone cone {Σ cᵢ fᵢ : cᵢ ≥ 0}. Verify each structural basis function:")
    B = basis(1)  # k-shape is A_light-independent for these basis fns except core_alpha (checked below)
    cone_monotone = True
    for name, f in B.items():
        d = f(4) - f(3)
        mono = all(f(k + 1) >= f(k) for k in range(1, 6))
        cone_monotone = cone_monotone and mono and (d >= 0)
        print(f"    {name:16} f(3)={f(3):5.1f} f(4)={f(4):5.1f}  φ(f)=f(4)−f(3)={d:+5.1f}  non-decreasing={mono}")
    # core_alpha_kA depends on A_light but is still non-decreasing in k for each A_light
    for Al in (1, 2, 3):
        f = basis(Al)["core_alpha_kA"]
        assert f(4) - f(3) >= 0
    print(f"  ⇒ every non-decreasing basis fn has φ(f) ≥ 0  (cone is φ-nonnegative: {cone_monotone})")

    print("\n  But on the miss:")
    separated = True
    for Al in (1, 2, 3):
        phi_miss = lad[Al][4] - lad[Al][3]
        sep = phi_miss < 0
        separated = separated and sep
        print(f"    A_light={Al}:  φ(miss) = miss(4)−miss(3) = {phi_miss:+.3f} MeV  {'< 0 ⇒ SEPARATED' if sep else ''}")
    print(f"\n  ⇒ φ separates miss from the monotone cone on all three ladders: {separated}")
    print("     miss ∉ cone(non-decreasing structural counts)  — scope-(b) EXCLUSION (proved invariant:")
    print("     monotone ⇒ φ ≥ 0; the (k=3,k=4) decrease is the Farkas witness). No fit.")

    # (3) the fall is not a separable parity factor either (A_light-dependent)
    print("\n--- (3) the fall miss(4)/miss(3) is A_light-DEPENDENT ⇒ not a separable parity factor ---")
    print(f"  fall ratios: A_light=1 → {falls[1]:.3f},  A_light=2 → {falls[2]:.3f},  A_light=3 → {falls[3]:.3f}")
    fall_separable = (max(falls.values()) / min(falls.values())) < 1.15
    print(f"  spread {max(falls.values())/min(falls.values()):.2f}× ⇒ separable parity factor: {fall_separable}")

    # (4) conclusion
    print("\n### Net (scope-(b) via explicit certificate):")
    print("  • The k=3 interior maximum is OUTSIDE the monotone additive cone (Farkas certificate φ).")
    print("  • ⇒ the missing binding channel is necessarily NON-monotone in k — a RESONANCE.")
    print("  • The fall is A_light-dependent ⇒ not a separable parity factor; combined with R11-a's")
    print("    A_light-dependent k=2 envelope, the miss is IRREDUCIBLY 2D in (k, A_light).")
    print("  • Redirect: closed-form k-envelopes are excluded; the per-isotope closure route is the")
    print("    operator-valued branching combiner / confinement SDP (mandated), where a resonant")
    print("    k-profile is natural. Formalize-first target = the R11-b order lemma. No fit.")

    ok = all_interior and cone_monotone and separated and (not fall_separable)
    try:
        sys.path.insert(0, str(HERE.parent / "substrate"))
        from witness_base import WitnessBuilder
        wb = WitnessBuilder("r11b-interior-max-monotone-cone-certificate",
                            engine="python (exact; witness-fed R10)")
        wb.set_description(
            "R11-b (z2bn/round-11): Farkas certificate that the ladder-miss k=3 interior maximum is "
            "outside the monotone additive cone. For any basis of functions non-decreasing in k "
            "(const 1, k, C(k,2), C(k,3), k·A_light, …) the functional φ=e_{k=4}−e_{k=3} is ≥0, so "
            "≥0 on the whole non-negative cone; but miss(4)−miss(3)<0 on all three (kα)+X ladders "
            "(n −1.46, d −4.19, t −5.37 MeV), so φ separates the miss from the cone. This is a "
            "scope-(b) exclusion (proved invariant monotone⇒φ≥0; the (k=3,k=4) decrease is the Farkas "
            "witness), not a scope-(a) near-miss: the missing binding channel is necessarily "
            "NON-monotone in k (a resonance). The fall ratio miss(4)/miss(3)=0.485/0.281/0.333 is "
            "A_light-dependent ⇒ not a separable parity factor; with R11-a's A_light-dependent k=2 "
            "envelope the miss is irreducibly 2D in (k,A_light). Redirects per-isotope closure to the "
            "operator-valued branching combiner / confinement SDP; formalize-first target = the R11-b "
            "order lemma. Consumes merged R10 witness (no recompute). No fit; magnitudes not interpreted.")
        wb.add_data("interior_max_all_ladders", bool(all_interior))
        wb.add_data("phi_miss_MeV", {f"A{Al}": lad[Al][4] - lad[Al][3] for Al in (1, 2, 3)})
        wb.add_data("fall_ratio_miss4_over_miss3", {f"A{Al}": falls[Al] for Al in (1, 2, 3)})
        wb.add_data("cone_phi_nonnegative", bool(cone_monotone))
        wb.add_data("fall_separable_parity_factor", bool(fall_separable))
        wb.add_assertion(
            name="interior_max_outside_monotone_cone",
            computed=str(int(bool(ok))), expected="1", tolerance=0,
            source=("Farkas certificate: φ=e_{k=4}−e_{k=3} is ≥0 on every non-decreasing basis "
                    "function hence on the whole non-negative additive cone, but φ(miss)=miss(4)−"
                    "miss(3)<0 on all three ladders ⇒ miss ∉ monotone cone (scope-(b), proved "
                    "invariant). The missing channel is non-monotone (resonant); the fall is "
                    "A_light-dependent (not separable). No fit."))
        out = wb.save()
        print(f"\nWitness: {out}")
    except Exception as e:
        print(f"\n(witness skipped: {e})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
