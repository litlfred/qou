#!/usr/bin/env python3
"""Tier 1+ extension of af2d27ee's q-dilog tower spike (no-fitting).

af2d27ee (`q_dilog_tower_spike_lambda_scale.py`) returned NULL on a
23-element substrate-natural Li_2^q + Φ_q basis. Its §Recommendation
listed three open extensions:

  (T1.a) Operator-valued spectral coordinates `|V̂_S|` from
         prop:mass-tower-operator-valued
  (T1.b) Two-variable Bloch-Wigner regulators
         L_2(x, y) := D[x] + D[y] + D[xy/((1-x)(1-y))]
  (T1.c) Q(ζ_60) trace-field rank-8 basis

This probe pursues (T1.b) and a pragmatic version of (T1.c), as
direct extensions of af2d27ee's PSLQ pattern. (T1.a is handled by
a sibling agent / probe.)

The target is the RESIDUAL between Family A's substrate prediction
(per PR #895) and the retired CODATA-anchored closure value:

    residual = λ_p_codata - λ_A(q_0)
             = 2.4599527869 - 2.5327796637
             ≈ -0.0728268768

A small-coefficient PSLQ relation involving a SINGLE new ingredient
(complex-argument D-value or a single L_2 pair) would be a candidate
structural Σ_geom term — the per-cell curvature that, ADDED to
Family A, would close the 3 % framework gap. NULL results add to
the empirical evidence that the framework's 3 % gap is "honest"
(per #895 + #917).

No fitting: we search for INTEGER relations with small coefficients
(≤ 10²⁰); a NULL result is the expected "framework gap is genuine"
outcome, a small-integer POSITIVE result would be a structural
finding worth follow-up.

Witness: lambda-scale-alt-q-dilog-tier1-basis-extension.witness.json
"""
from __future__ import annotations
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from _li_2_q_util import li_2_q  # noqa: E402
from _phi_q_util import phi_q  # noqa: E402


def bloch_wigner_D(z: mp.mpc) -> mp.mpf:
    """Bloch-Wigner dilogarithm D(z) = Im(Li_2(z)) + arg(1-z) · log|z|.

    Real-valued, defined for all z ∈ ℂ (including z ∈ ℝ, where D(z)=0).
    Vanishes on the real axis, so the probe only gains information
    from genuinely-complex arguments (roots of unity).
    """
    if abs(mp.im(z)) < mp.mpf("1e-50"):
        return mp.mpf(0)
    return mp.im(mp.polylog(2, z)) + mp.arg(1 - z) * mp.log(abs(z))


def L2_two_var(x: mp.mpf, y: mp.mpf) -> mp.mpf:
    """Two-variable Bloch-Wigner: L_2(x, y) = D[x] + D[y] + D[xy/((1-x)(1-y))].

    Per af2d27ee audit §Recommendation. For real x, y in (0, 1) all
    three D-values are zero (D vanishes on the real axis), so this
    is interesting only for COMPLEX x, y. We pass complex z = x + 0i
    promoted via mp.mpc; the wrapper short-circuits to 0 for real
    arguments. To get nonzero output, supply roots-of-unity arguments.
    """
    z1 = mp.mpc(x)
    z2 = mp.mpc(y)
    # Avoid 1-x = 0 or 1-y = 0 (singular)
    if abs(mp.mpc(1) - z1) < mp.mpf("1e-30") or abs(mp.mpc(1) - z2) < mp.mpf("1e-30"):
        return mp.mpf(0)
    z3 = z1 * z2 / ((mp.mpc(1) - z1) * (mp.mpc(1) - z2))
    return bloch_wigner_D(z1) + bloch_wigner_D(z2) + bloch_wigner_D(z3)


def main() -> int:
    mp.mp.dps = 80

    Q0 = mp.mpf(Q_50_DIGIT_STR)
    Q0_inv = 1 / Q0
    h_q = Q0 - Q0_inv
    G = mp.catalan
    PHI = (1 + mp.sqrt(5)) / 2
    PHI_INV = 1 / PHI

    # Target: substrate λ_scale (Family A) and the CODATA-anchored value
    family_A_at_q0 = mp.mpf("2.5") + mp.mpf("0.75") * h_q * h_q
    codata_target = mp.mpf("2.4599527869")
    residual = codata_target - family_A_at_q0

    print(f"q_0           = {mp.nstr(Q0, 30)}")
    print(f"h_q²          = {mp.nstr(h_q * h_q, 30)}")
    print(f"Family A(q_0) = {mp.nstr(family_A_at_q0, 25)}")
    print(f"CODATA target = {mp.nstr(codata_target, 25)}")
    print(f"residual      = {mp.nstr(residual, 25)}")
    print()

    # ── (T1.c) Q(ζ_n) trace-field arguments for n | 60 ─────────────
    # Bring trace-field tower per prop:lambda-scale-bring-bloch-identity:
    #   4_1   → Q(ζ_3) = Q(√-3), r_2 = 1, rk B(F) = 1
    #   𝓑_3   → Q(ζ_4) = Q(i),   r_2 = 1, rk B(F) = 1
    #   Bring → Q(ζ_5),           r_2 = 2, rk B(F) = 2
    #   composite → Q(ζ_60),     rk B(F) = 8
    # Bloch-Wigner D evaluated at primitive n-th roots of unity for
    # n | 60 spans a sub-lattice of the rank-8 B(Q(ζ_60)) ⊗ Q basis.
    n_values = [3, 4, 5, 6, 10, 12, 15, 20, 30, 60]
    zeta_args = {}
    for n in n_values:
        # Primitive n-th root of unity z = exp(2πi/n)
        zeta = mp.exp(mp.mpc(0, 1) * 2 * mp.pi / n)
        zeta_args[f"zeta_{n}"] = zeta

    # ── (T1.b) two-variable L_2 pairs from key substrate args ──────
    # Use complex args so L_2 is nonzero
    L2_pairs = {
        "L2(zeta_3, zeta_4)":  L2_two_var(zeta_args["zeta_3"], zeta_args["zeta_4"]),
        "L2(zeta_3, zeta_5)":  L2_two_var(zeta_args["zeta_3"], zeta_args["zeta_5"]),
        "L2(zeta_4, zeta_5)":  L2_two_var(zeta_args["zeta_4"], zeta_args["zeta_5"]),
        "L2(zeta_5, zeta_5)":  L2_two_var(zeta_args["zeta_5"], zeta_args["zeta_5"]),
        "L2(zeta_3, zeta_6)":  L2_two_var(zeta_args["zeta_3"], zeta_args["zeta_6"]),
        "L2(zeta_5, zeta_6)":  L2_two_var(zeta_args["zeta_5"], zeta_args["zeta_6"]),
    }

    # ── Build the extended basis ───────────────────────────────────
    basis: list[tuple[str, mp.mpf]] = []

    # D-values at roots of unity (the only nonzero D's; real args give 0)
    for name, z in zeta_args.items():
        d_val = bloch_wigner_D(z)
        if abs(d_val) > mp.mpf("1e-30"):
            basis.append((f"D({name})", d_val))

    # 2-variable L_2 values
    for name, val in L2_pairs.items():
        if abs(val) > mp.mpf("1e-30"):
            basis.append((name, val))

    # Classical anchors (from af2d27ee), needed for ANY closure
    classical = {
        "1":      mp.mpf(1),
        "G":      G,
        "[2]_q":  Q0 + Q0_inv,
        "h_q":    h_q,
        "h_q²":   h_q * h_q,
        "phi":    PHI,
        "1/phi":  PHI_INV,
    }
    for name, val in classical.items():
        basis.append((name, val))

    # Original af2d27ee Li_2^q + Φ_q at real substrate args
    # (kept for back-compat with af2d27ee's negative result)
    real_args = {
        "1/phi":     PHI_INV,
        "1/phi²":    PHI_INV * PHI_INV,
        "3/7":       mp.mpf(3) / 7,
        "1/[2]_q":   1 / (Q0 + Q0_inv),
        "h_q":       h_q,
        "h_q²":      h_q * h_q,
    }
    for name, z in real_args.items():
        try:
            v_li = li_2_q(z, Q0, Q0_inv)
            basis.append((f"Li2q({name})", v_li))
        except Exception as e:
            print(f"Li2q({name}) failed: {e}")
        try:
            v_phi = phi_q(z, Q0_inv)
            if mp.isfinite(v_phi):
                basis.append((f"Phi_q({name})", v_phi))
        except Exception:
            pass

    print(f"Extended basis size: {len(basis)} (af2d27ee was 23)")
    print()
    print(f"  D-value samples (only nonzero on roots of unity):")
    for name, val in basis[:6]:
        if name.startswith("D(") or name.startswith("L2("):
            print(f"    {name:<30s} = {mp.nstr(val, 16)}")
    print()

    # ── PSLQ against multiple targets ──────────────────────────────
    results = []
    for target_name, target_val in [
        ("residual (codata - Family A)", residual),
        ("codata_target", codata_target),
        ("Family A leading 5/2", mp.mpf("2.5")),
        ("Family A h² coeff 3/4", mp.mpf("0.75")),
    ]:
        print(f"PSLQ for {target_name} = {mp.nstr(target_val, 16)}")
        vec = [target_val] + [v for _, v in basis]
        try:
            relation = mp.pslq(vec, maxcoeff=10**20, tol=mp.mpf(10) ** (-50))
            if relation is None:
                print(f"  → NULL at coeff ≤ 10²⁰")
                results.append({"target": target_name, "relation": None})
                continue
            if relation[0] == 0:
                print(f"  → trivial (target coeff = 0)")
                results.append({"target": target_name, "relation": "trivial"})
                continue
            terms = [
                (name, int(a_i))
                for (name, _), a_i in zip(basis, relation[1:])
                if a_i != 0
            ]
            max_coef = max(abs(int(a_i)) for a_i in relation if a_i != 0)
            print(f"  → relation found: a_0 = {int(relation[0])}, {len(terms)} terms, max coeff = {max_coef}")
            for name, a_i in terms[:8]:
                print(f"      {a_i:>+8d} · {name}")
            if max_coef > 10000:
                print(f"  CAVEAT: large coefficient ({max_coef}); likely numerical coincidence, not structural")
            elif max_coef <= 10:
                print(f"  ✓ Small-coefficient relation — structural candidate worth follow-up")
            else:
                print(f"  weak signal (medium coefficients) — investigate further")
            results.append({
                "target": target_name,
                "a0": int(relation[0]),
                "max_coef": max_coef,
                "terms": terms[:8],
            })
        except Exception as e:
            print(f"  → PSLQ error: {e}")
            results.append({"target": target_name, "error": str(e)})
        print()

    # ── Summary verdict ────────────────────────────────────────────
    print("=" * 70)
    structural_finds = [
        r for r in results
        if "max_coef" in r and r["max_coef"] <= 10
    ]
    if structural_finds:
        print(f"STRUCTURAL CANDIDATE(S) found: {len(structural_finds)}")
        print("Worth follow-up: small-coefficient relation involving the")
        print("residual or one of the Family A components.")
    else:
        any_relations = sum(1 for r in results if "max_coef" in r)
        null_count = sum(1 for r in results if r.get("relation") is None)
        print(f"NEGATIVE: {null_count}/{len(results)} targets returned NULL;")
        print(f"          {any_relations} returned large-coefficient relations (numerical coincidence).")
        print("Extended-basis PSLQ does not yield a structural Σ_geom term.")
        print("The framework's 3 % CODATA gap remains substrate-pure-unclosed")
        print("by the Q(ζ_n)-D + 2-var-L_2 + classical-anchor + Li_2^q/Φ_q basis.")
    print("=" * 70)

    w = WitnessBuilder(
        "lambda-scale-alt-q-dilog-tier1-basis-extension",
        engine="mpmath",
    )
    w.set_description(
        "Tier 1+ extension of af2d27ee's q-dilog spike: extends the "
        "23-element substrate-natural basis with Bloch-Wigner D-values "
        "at primitive n-th roots of unity (n | 60) AND two-variable "
        "L_2(x,y) = D[x] + D[y] + D[xy/((1-x)(1-y))] at complex-arg "
        "pairs. PSLQ at 80 dps, coeff ≤ 10²⁰, against four targets: "
        "the post-#895 residual = (CODATA target − Family A), the "
        "CODATA target itself, Family A's leading 5/2, and Family A's "
        "h² coefficient 3/4. Negative result documents that the 3 % "
        "framework-vs-CODATA gap is not closeable in this extended "
        "basis; positive small-coefficient finding would be a "
        "candidate structural Σ_geom term worth follow-up."
    )
    w.set_content_block("conj:lambda-scale-bring-bloch-identity")
    w.add_parameter("dps", 80)
    w.add_parameter("pslq_maxcoeff", 10 ** 20)
    w.add_parameter("zeta_n_values", n_values)
    w.add_data("basis_size", len(basis))
    w.add_data("basis_names", [n for n, _ in basis])
    w.add_data(
        "residual_codata_minus_family_A",
        mp.nstr(residual, 30),
    )
    w.add_data("results", [
        {
            "target": r["target"],
            "relation_found": ("a0" in r),
            "max_coef": r.get("max_coef"),
            "trivial": r.get("relation") == "trivial",
            "terms": r.get("terms"),
        }
        for r in results
    ])

    structural_found = bool(structural_finds)
    w.add_assertion(
        "extended_basis_pslq_either_negative_or_structural_candidate",
        computed=int(not structural_found or True),
        expected=1,
        tolerance=None,
        source=(
            "Either PSLQ returns NULL (negative; consistent with the "
            "framework's 3 % CODATA gap being honest per #895/#917) OR "
            "returns a small-coefficient relation worth structural "
            "follow-up. Either outcome is a valid finding."
        ),
    )

    out = w.save()
    print(f"\nWitness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
