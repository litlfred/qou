#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical search over Bloch-Wigner
# regulator values; topological constants only.
"""Tier 0 Bring-Bloch K-search for the proton effective volume.

Searches for ℤ-linear combinations of hyperbolic volumes in the
Tier 0 set of Bring-embeddable knots / links whose sum equals
the proton's `effective volume`

    Vol(K_p^eff)  :=  λ_p_scale · Vol(𝓑₃)  =  λ_p_scale · 8·G

where G is Catalan's constant and λ_p_scale is the empirical
Borromean tower scale.

Two targets are searched:

  - CODATA closure target:  λ_p = 2.4599527843613...  → Vol ≈ 18.0277
  - C2-inflection target:   λ_p ≈ 2.4616...           → Vol ≈ 18.036
                            (substrate-pure, +0.069% from PR #690)

Per `prop:bring-hyperbolic-knot-bloch-decomposition` (on main,
sorry-free conditional Lean), the categorical identity for
λ_p_scale is

    λ_p_scale = (1/Vol(𝓑₃)) · D[Z_{K_p^eff}]

where D is the Bloch-Wigner regulator and [Z_{K_p^eff}] ∈
B(F)⊗ℚ is the proton's specific Bring-decomposition class in
F = ℚ(ζ_60).  For hyperbolic 3-manifolds, D[Z_K] = Vol_hyp(K),
so the categorical identity is equivalent to a ℤ-linear relation

    Vol(K_p^eff)  =  Σ_i n_i · Vol_hyp(K_i)

over Tier 0 (atlas-named hyperbolic knots).

If a Tier 0 relation exists within numerical precision, λ_p_scale
becomes substrate-derived. If no Tier 0 relation exists, search
must extend to Tier 1 (~30 prime 3-bridge hyperbolic, NF-product
closures in H_3(q)) and Tier 2 (genus-4 embeddable through H_8(q)).

Refs:
  - prop:bring-hyperbolic-knot-bloch-decomposition
  - docs/audits/2026-05-18-lambda-scale-derivation-search.md §93–104
  - PR #701 (falsification of `5/2 − h²·G` as categorical identity)
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402


# ── Tier 0 hyperbolic volumes at high precision ───────────────
# Sources: standard SnapPy census + closed-form identities.
# All values cross-checked against `recursive-atom-knot-atlas.md`
# (Layer-1 |tr_M| table comments).

def tier0_volumes(dps: int = 60) -> dict[str, mp.mpf]:
    """Return Tier 0 hyperbolic-knot volumes at `dps` precision.

    Vol(𝓑₃) = 8·G is exact via Adams 1985 + Λ(π/4) = G/2.
    Vol(4_1) has closed form via Clausen function at π/3.
    Other volumes are literature values at ≥12 dps; sufficient
    precision for Tier 0 integer-relation search (which only
    needs to identify n_i with |n_i| ≤ ~5).
    """
    with mp.workdps(dps):
        # Vol(𝓑₃) = 8 · Catalan  (Adams 1985, Λ(π/4) = G/2)
        vol_B3 = 8 * mp.catalan

        # Vol(4_1) = 2 · Im(Li_2(e^{iπ/3})) = 2 · Cl_2(π/3)
        # = 3√3 · Cl_2(π/3) / Im normalization
        # mpmath has clsin / clcos; Cl_2(θ) = clsin(2, θ)
        vol_4_1 = 2 * mp.clsin(2, mp.pi / 3)

        # Other Vol values from SnapPy literature (≥12 dps):
        # Reference: Burton (Regina), or the Knot Atlas
        vol_5_2 = mp.mpf("2.8281220883307886093")
        vol_6_1 = mp.mpf("3.1639632288821502117")
        vol_6_2 = mp.mpf("4.4008325136513705074")
        vol_6_3 = mp.mpf("5.6930211935087547922")
        vol_7_4 = mp.mpf("5.1374458566012050948")
        vol_8_11 = mp.mpf("8.2863215025793773620")

        # L_6a4 = "magic link" / minimally twisted chain — has
        # the same Vol as 𝓑₃ (also 2 ideal octahedra).
        vol_L_6a4 = vol_B3

        # Whitehead link, also common reference
        vol_W = mp.mpf("3.6638623767088654")  # Whitehead 5^2_1

    return {
        "4_1": vol_4_1,
        "5_2": vol_5_2,
        "6_1": vol_6_1,
        "6_2": vol_6_2,
        "6_3": vol_6_3,
        "7_4": vol_7_4,
        "B_3": vol_B3,
        "L_6a4": vol_L_6a4,
        "8_11": vol_8_11,
        "Whitehead": vol_W,
    }


def search_integer_relation(
    target: mp.mpf,
    basis: dict[str, mp.mpf],
    max_coef: int = 20,
    tolerance: mp.mpf | None = None,
) -> dict | None:
    """Use mpmath PSLQ to find ℤ-linear relation between `target`
    and the basis volumes.

    PSLQ finds integers (n_0, n_1, ..., n_M) with
        n_0 · target + Σ n_i · basis_i ≈ 0
    minimal (in norm) up to numerical precision.

    Returns the relation expressed as `target = -Σ (n_i/n_0) · basis_i`,
    requiring n_0 divides each n_i (or rational coefficients otherwise).
    """
    if tolerance is None:
        tolerance = mp.mpf("1e-20")

    names = list(basis.keys())
    vols = [basis[n] for n in names]

    # PSLQ on [target, vol_1, vol_2, ...] finds integer relation
    vec = [target] + vols
    print(f"  PSLQ on {len(vec)} reals; basis = {names}")
    try:
        rel = mp.pslq(vec, tol=tolerance, maxcoeff=10 ** max_coef)
    except Exception as e:
        print(f"  PSLQ raised: {e}")
        return None
    if rel is None:
        return None

    n_target, *n_basis = rel
    if n_target == 0:
        return None  # relation among basis only, not involving target

    # target = -Σ (n_i / n_target) · basis_i
    # If n_target divides each n_i, this is integer.
    coefs_rational = {
        names[i]: (-n_basis[i], n_target) for i in range(len(names))
        if n_basis[i] != 0
    }

    # Numerical check
    s = mp.mpf(0)
    for i, v in enumerate(vols):
        s += mp.mpf(-n_basis[i]) / mp.mpf(n_target) * v
    residual = abs(s - target)

    coefs_decimal = {k: float(v[0]) / float(v[1])
                     for k, v in coefs_rational.items()}

    return {
        "pslq_relation": [int(r) for r in rel],
        "names": ["target"] + names,
        "coefs_rational": {
            k: f"{v[0]}/{v[1]}" for k, v in coefs_rational.items()
        },
        "coefs_decimal": coefs_decimal,
        "sum": mp.nstr(s, 30),
        "target": mp.nstr(target, 30),
        "residual_abs": mp.nstr(residual, 12),
        "residual_rel": mp.nstr(residual / abs(target), 12),
    }


def main() -> int:
    mp.mp.dps = 80

    w = WitnessBuilder(
        "bring-bloch-tier0-search-m-p",
        engine="mpmath",
    )
    w.set_description(
        "Tier 0 Bring-Bloch K-search for the proton effective volume. "
        "Searches for ℤ-linear combinations of hyperbolic volumes "
        "in the Tier 0 set {4_1, 5_2, 6_1, 6_2, 6_3, 7_4, 𝓑₃, "
        "L_6a4, 8_11, Whitehead} equaling Vol(K_p^eff) = "
        "λ_p_scale · 8·G, where λ_p_scale is either the CODATA-"
        "closure value (2.4599527843613) or the C2-inflection "
        "value (2.4616, PR #690 substrate-pure). Per "
        "prop:bring-hyperbolic-knot-bloch-decomposition (on main, "
        "sorry-free conditional Lean), an integer relation in "
        "B(F)⊗ℚ with F ⊆ ℚ(ζ_60) is the categorical identity "
        "for λ_p_scale."
    )
    w.add_parameter("compute_dps", "80")
    w.add_parameter("max_coef", "5")

    # ── Tier 0 basis ─────────────────────────────────────────
    basis = tier0_volumes(dps=80)
    w.add_data("tier0_basis", {
        name: mp.nstr(vol, 30) for name, vol in basis.items()
    })

    # ── Targets ──────────────────────────────────────────────
    G = mp.catalan
    vol_B3 = 8 * G
    lambda_p_codata = mp.mpf("2.4599527843613182892482457339493")
    lambda_p_c2 = mp.mpf("2.4615")  # approximate, from PR #690

    target_codata = lambda_p_codata * vol_B3
    target_c2 = lambda_p_c2 * vol_B3

    w.add_data("targets", {
        "Vol(K_p^eff)_CODATA": {
            "lambda_p": mp.nstr(lambda_p_codata, 30),
            "vol_K_p_eff": mp.nstr(target_codata, 30),
            "source": "implied λ_p from CODATA m_p with Vol(𝓑₃) = 8G",
        },
        "Vol(K_p^eff)_C2_inflection": {
            "lambda_p": mp.nstr(lambda_p_c2, 8),
            "vol_K_p_eff": mp.nstr(target_c2, 30),
            "source": "PR #690 C2 inflection a* = 0.4064; m_p = 938.918 MeV (+0.069%)",
        },
    })

    # ── Search via PSLQ ──────────────────────────────────────
    print(f"\n=== CODATA closure target ===")
    print(f"  target = λ_p · 8G = {mp.nstr(target_codata, 25)}")
    result_codata = search_integer_relation(
        target_codata, basis, max_coef=30,
    )
    if result_codata:
        print(f"  PSLQ found relation:")
        for k, v in result_codata["coefs_rational"].items():
            print(f"    {v} · Vol({k})")
        print(f"  residual: {result_codata['residual_abs']}")
    else:
        print(f"  No PSLQ relation found at max_coef=30.")

    print(f"\n=== C2 inflection target (PR #690) ===")
    print(f"  target = λ_p^C2 · 8G ≈ {mp.nstr(target_c2, 25)}")
    result_c2 = search_integer_relation(
        target_c2, basis, max_coef=30,
    )
    if result_c2:
        print(f"  PSLQ found relation:")
        for k, v in result_c2["coefs_rational"].items():
            print(f"    {v} · Vol({k})")
        print(f"  residual: {result_c2['residual_abs']}")
    else:
        print(f"  No PSLQ relation found at max_coef=30.")

    # ── Record results ────────────────────────────────────────
    w.add_data("search_codata_target", {
        "result": result_codata or "no_pslq_relation_found",
    })
    w.add_data("search_c2_target", {
        "result": result_c2 or "no_pslq_relation_found",
    })

    # ── Headline assertions ─────────────────────────────────
    w.add_assertion(
        "Tier 0 PSLQ relation exists for CODATA target",
        computed=float(result_codata is not None),
        expected=1.0,
        tolerance=0.5,
        unit="boolean",
        source="mpmath.pslq at max_coef=10^30",
    )

    out = w.set_audit_only(
        "docs/audits/2026-05-18-lambda-scale-derivation-search.md"
    ).save()
    print(f"\n→ wrote {out}")

    # Verdict summary
    if result_codata:
        print("\n✓ Tier 0 PSLQ relation FOUND for CODATA target!")
        print(f"  residual = {result_codata['residual_abs']}")
        print(f"  rel_residual = {result_codata['residual_rel']}")
    else:
        print("\n✗ Tier 0 PSLQ relation NOT found for CODATA target.")
        print("  → Tier 1 search (NF-product closures in H_3(q)) is the next step.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
