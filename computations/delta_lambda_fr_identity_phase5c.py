"""
delta_lambda_fr_identity_phase5c.py — Phase 5c.1 of the Δ_λ thread.

Test the Frobenius-reciprocity identity predicted by the Phase 5b
bar-symmetric synthesis (audit doc
`docs/audits/2026-05-19-delta-lambda-phase5-alpha-derivation-progress.md`):

For each (Z=1 → Z=2) transition at fixed N:

    Σ_λ y_λ χ_λ(β_K^{Z=2})  ≟  [3]_q² · cosh(h) ·
                                Σ_μ y_μ χ_μ(β_K^{Z=1})
                              + (Li_2^q interface correction)

where:
  - β_K^Z   is the canonical 3A-strand atomic braid for atom K=(Z, N)
  - y_λ     is the Jones-Markov weight at H_n (cached in
              `y-lambda-at-q0.witness.json`)
  - χ_λ     is the Hecke character (computed via pyhecke_native)
  - [3]_q²  is the categorical per-Z gain factor
  - cosh(h) is the Hecke-deformed identity correction (Phase 5b finding)
  - the residual (Li_2^q interface correction) is the constituent-vacuum
    discrepancy from PR #801's interface-knot Δ_I^K

If the residual is at the bar-symmetric level (small, structurally clean),
the FR identity is empirically validated and α = [3]_q²·cosh(h) is the
per-Z step factor. If the residual is large or sign-flipping, the
bar-symmetric synthesis needs more work (Phase 5d).

Compares both:
  (a) FULL canonical braid (include_inter=True) — what tr_M(β_K) actually is
  (b) CONSTITUENT vacuum (include_inter=False) — disjoint Hecke product

The difference between (a) and (b) is the interface-knot contribution
Δ_I^K from PR #801.

  Ref: [manuscript] conj:delta-lambda-categorical-closure
  Ref: docs/audits/2026-05-19-delta-lambda-phase5-alpha-derivation-progress.md
  Ref: PR #801 (interface-knot Δ_I^K binding)
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp

from witness_base import WitnessBuilder, record_upstream

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []
# 50-dps source. `set_q` does `mp.mpf(str(...))` internally, so a STRING
# input gives the full 50 digits where the f64 `Q` gave 17. Alias renamed
# from Q0_STR: it is no longer a float, and a name that says otherwise is
# the label problem this sweep exists to remove.
from q_parameter import Q_50_DIGIT_STR as Q0_STR
from q_mpmath import set_q, qint
from _precision import set_compute_dps  # noqa: E402
set_q(Q0_STR)

set_compute_dps()
Q0 = mp.mpf(str(Q0_STR))

# Per-(Z, N) atoms to test
ATOMS = [
    ("D",   1, 1),   # H_6
    ("T",   1, 2),   # H_9
    ("3He", 2, 1),   # H_9
    ("4He", 2, 2),   # H_12  — slowest; still feasible with Rust kernel
]


def load_y_lambda_at_q0() -> dict[int, dict[tuple, mp.mpf]]:
    """Jones-Markov weights y_λ at THIS producer's q_0, computed live.

    🛑 Was: read `y-lambda-at-q0.witness.json`. That witness is **muon-built**
    (`q0Anchor: "muon"`), while this producer sets `q` from `q_parameter.Q`,
    which resolves **proton** for this stem. `compute_tr_M_decomposition` then
    forms `τ_M(β) = Σ_λ y_λ · χ_λ(β)` — muon-built `y_λ` against
    proton-evaluated `χ_λ`, a layer straddle inside one quantity.

    That is the exact defect AGENTS.md §q₀-anchor documents for the μ₃ Fréchet
    probe ("took `y_λ` from the muon-built cache while evaluating `χ_λ` at the
    proton `q₀` — an 11.54 ppb layer separation"), and it was invisible here
    because the witness is stamped `proton` and so looked layer-clean.

    Fix is the one that section prescribes: call the live closed form at the
    producer's own `q₀` instead of the cached witness, so both factors come
    from the same layer by construction and the quantity cannot straddle
    whatever the pin resolves to.
    """
    from schur_principal_mpmath import y_lambda_at_q0_mpmath  # noqa: E402
    return {n: y_lambda_at_q0_mpmath(n, Q0) for n in range(2, 13)}


def compute_tr_M_decomposition(Z: int, N: int, include_inter: bool,
                               y_at_q0: dict) -> dict:
    """Compute τ_M(β) = Σ_λ y_λ · χ_λ(β) using pyhecke_native.

    Returns dict with per-λ decomposition + total + dominant block.
    """
    from mass_at_3A_proper import atom_braid_word_3A
    from hecke_characters import chi_lambda_braid, partitions_of

    A = Z + N
    n = 3 * A
    word_tuples = atom_braid_word_3A(Z, N, include_inter=include_inter)
    # Convert (c, d, gen_idx) → (sign, gen_1indexed) for chi_lambda_braid
    word_marshalled = []
    h_val = float(Q0 - 1 / Q0)  # noqa: I8 — sign-classification param for marshal_to_chi_lambda_braid (matched vs d within eps=1e-10), not a precision coefficient
    for c, d, g in word_tuples:
        cf = float(c)
        df = float(d)
        if abs(cf - 1.0) < 1e-10 and abs(df) < 1e-10:
            word_marshalled.append((1, g + 1))
        elif abs(cf - 1.0) < 1e-10 and abs(df + h_val) < 1e-10:
            word_marshalled.append((-1, g + 1))
        elif abs(cf - 1.0) < 1e-10 and abs(df + h_val / 2) < 1e-10:
            word_marshalled.append((1, g + 1))  # averaged → σ convention
        else:
            word_marshalled.append((1, g + 1))

    parts = list(partitions_of(n))
    # Batch character evaluation across partitions — single PyO3
    # call instead of N per-shape FFI crossings (ffi-roundtrip-audit
    # F-A: `chi_lambdas_braid` is rayon-parallel on the Rust side).
    from hecke_characters import chi_lambdas_braid
    chi_values = chi_lambdas_braid(parts, word_marshalled, q_value=float(Q0))
    rows = []
    total = mp.mpf(0)
    for lam, chi in zip(parts, chi_values):
        y = y_at_q0.get(n, {}).get(lam, mp.mpf(0))
        if y == 0:
            # try without the trailing zero entries
            for k in y_at_q0.get(n, {}):
                if k == lam[:len(k)] and all(x == 0 for x in lam[len(k):]):
                    y = y_at_q0[n][k]
                    break
        c_lam = y * mp.mpf(str(chi))
        total += c_lam
        rows.append({
            "lambda": list(lam),
            "y": float(y),
            "chi": chi,
            "y_chi": float(c_lam),
            "abs_y_chi": float(abs(c_lam)),
        })

    # Dominant block (largest |y · χ|)
    rows.sort(key=lambda r: -r["abs_y_chi"])
    dominant = rows[0]
    return {
        "Z": Z, "N": N, "n": n, "word_length": len(word_marshalled),
        "include_inter": include_inter,
        "total_tr_M": float(total),
        "abs_total_tr_M": float(abs(total)),
        "dominant_lambda": dominant["lambda"],
        "dominant_y_chi": dominant["y_chi"],
        "dominant_abs_y_chi": dominant["abs_y_chi"],
        "top_5_blocks": rows[:5],
    }


def main() -> int:
    builder = WitnessBuilder("delta-lambda-fr-identity-phase5c")
    builder.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    builder.set_description(
        "Phase 5c.1 of the Δ_λ thread: numerical test of the "
        "Frobenius-reciprocity identity predicted by the Phase 5b "
        "bar-symmetric synthesis. Computes τ_M(β) = Σ_λ y_λ · χ_λ(β) "
        "at q_0 for D, T, ³He, ⁴He via cached y_λ + pyhecke_native "
        "χ_λ. Compares both the full canonical braid (include_inter=True) "
        "and the constituent-vacuum baseline (include_inter=False; "
        "PR #801's T_constit). The ratio τ_M(β_{Z=2}^N) / τ_M(β_{Z=1}^N) "
        "is the Ind-side per-Z step factor; under FR it should equal "
        "[3]_q² · cosh(h) · (interface-knot correction)."
    )
    builder.set_content_block("conj:delta-lambda-categorical-closure")
    builder.add_parameter("q0", str(Q0))

    h = Q0 - 1 / Q0
    qint_3 = qint(3)
    qint_3_sq = qint_3 ** 2
    alpha_pred = qint_3_sq * mp.cosh(h)
    builder.add_parameter("h", str(h))
    builder.add_parameter("3_q_squared", str(qint_3_sq))
    builder.add_parameter("cosh_h", str(mp.cosh(h)))
    builder.add_parameter("alpha_predicted", str(alpha_pred))

    y_at_q0 = load_y_lambda_at_q0()
    print(f"  Loaded y_λ at q_0 for n ∈ {sorted(y_at_q0.keys())}")
    print(f"  q_0 = {Q0}")
    print(f"  h = q - q⁻¹ = {float(h):.6f}")
    print(f"  [3]_q² = {float(qint_3_sq):.6f}")
    print(f"  cosh(h) = {float(mp.cosh(h)):.6f}")
    print(f"  α_pred = [3]_q² · cosh(h) = {float(alpha_pred):.6f}")
    print()

    results_full = {}
    results_constit = {}
    for name, Z, N in ATOMS:
        for include_inter, label, dest in [
            (True, "FULL (β_K)", results_full),
            (False, "CONSTIT (no interface)", results_constit),
        ]:
            print(f"  Computing {name} {label} ({Z=}, {N=})...")
            t0 = time.time()
            try:
                result = compute_tr_M_decomposition(Z, N, include_inter, y_at_q0)
                dt = time.time() - t0
                print(f"    Took {dt:.2f}s; τ_M = {result['total_tr_M']:+.6f}, "
                      f"|τ_M| = {result['abs_total_tr_M']:.6f}, "
                      f"dominant λ = {result['dominant_lambda']}")
                dest[name] = result
            except Exception as e:
                print(f"    ERR: {type(e).__name__}: {e}")
                dest[name] = {"error": str(e)}

    builder.add_data("results_full", results_full)
    builder.add_data("results_constit", results_constit)

    # ── FR identity test ──────────────────────────────────────────
    print("\n=== FR-identity test: per-Z step factor ===")
    print(f"  Predicted: τ_M(β_{{Z=2}}) / τ_M(β_{{Z=1}}) at fixed N "
          f"≈ α_pred = [3]_q² · cosh(h) = {float(alpha_pred):.4f}")
    print(f"  (modulo Li_2^q interface-knot correction from PR #801)")
    print()

    fr_tests = []
    for N_val, (Z1_name, Z2_name) in [(1, ("D", "3He")), (2, ("T", "4He"))]:
        if "error" in results_full.get(Z1_name, {}) or "error" in results_full.get(Z2_name, {}):
            continue
        for label, results in [("FULL", results_full), ("CONSTIT", results_constit)]:
            try:
                trM_z1 = mp.mpf(str(results[Z1_name]["total_tr_M"]))
                trM_z2 = mp.mpf(str(results[Z2_name]["total_tr_M"]))
                ratio = trM_z2 / trM_z1 if trM_z1 != 0 else mp.mpf("inf")

                # Use |τ_M| ratio (FR identity is for magnitudes)
                abs_trM_z1 = mp.mpf(str(results[Z1_name]["abs_total_tr_M"]))
                abs_trM_z2 = mp.mpf(str(results[Z2_name]["abs_total_tr_M"]))
                abs_ratio = abs_trM_z2 / abs_trM_z1 if abs_trM_z1 != 0 else mp.mpf("inf")

                rel_err_signed = (ratio - alpha_pred) / alpha_pred if alpha_pred != 0 else mp.mpf("inf")
                rel_err_abs = (abs_ratio - alpha_pred) / alpha_pred if alpha_pred != 0 else mp.mpf("inf")

                fr_tests.append({
                    "transition": f"{Z2_name}/{Z1_name} (N={N_val})",
                    "scope": label,
                    "tr_M_Z1": float(trM_z1),
                    "tr_M_Z2": float(trM_z2),
                    "ratio_signed": float(ratio),
                    "abs_ratio": float(abs_ratio),
                    "alpha_pred": float(alpha_pred),
                    "rel_err_signed": float(rel_err_signed),
                    "rel_err_abs": float(rel_err_abs),
                })
                print(f"  {label:<8} {Z2_name}/{Z1_name} at N={N_val}: "
                      f"τ ratio = {float(ratio):+.5f}, |τ| ratio = {float(abs_ratio):.5f}, "
                      f"vs α_pred = {float(alpha_pred):.4f}; "
                      f"rel.err |τ|: {float(rel_err_abs)*100:+.2f}%")
            except Exception as e:
                print(f"  {label} {Z2_name}/{Z1_name}: ERR {e}")

    builder.add_data("fr_identity_tests", fr_tests)

    # Cross-check: dominant-block ratio (the |Δ_λ*| analogue)
    print("\n=== Dominant-block ratio test (|Δ_λ*|-style) ===")
    dominant_tests = []
    for N_val, (Z1_name, Z2_name) in [(1, ("D", "3He")), (2, ("T", "4He"))]:
        if "error" in results_full.get(Z1_name, {}) or "error" in results_full.get(Z2_name, {}):
            continue
        abs1 = mp.mpf(str(results_full[Z1_name]["dominant_abs_y_chi"]))
        abs2 = mp.mpf(str(results_full[Z2_name]["dominant_abs_y_chi"]))
        ratio = abs2 / abs1 if abs1 != 0 else mp.mpf("inf")
        dominant_tests.append({
            "transition": f"{Z2_name}/{Z1_name} (N={N_val})",
            "dom_abs_y_chi_Z1": float(abs1),
            "dom_abs_y_chi_Z2": float(abs2),
            "dom_ratio": float(ratio),
            "alpha_pred": float(alpha_pred),
            "rel_err": float((ratio - alpha_pred) / alpha_pred),
        })
        print(f"  {Z2_name}/{Z1_name} at N={N_val}: "
              f"dominant |y·χ| ratio = {float(ratio):.4f}, vs α_pred = {float(alpha_pred):.4f}; "
              f"rel.err: {float((ratio - alpha_pred)/alpha_pred)*100:+.2f}%")
    builder.add_data("dominant_block_tests", dominant_tests)

    # ── Primary assertion: z-identity (the proposition's actual claim) ──
    # τ_M(β_K^FULL) / τ_M(β_K^CONSTIT) should equal z exactly per the
    # Markov axiom (prop:interface-knot-markov-z). This is the
    # categorical content of the Phase 5c.1 finding.
    z_markov = Q0**3 / (Q0**2 + 1)
    h_hecke = Q0 - 1 / Q0
    z_minus_h = z_markov - h_hecke
    # Per Markov axiom + Hecke skein σ⁻¹ = σ - h·1:
    #   tr_M(α · σ)  = z · tr_M(α)        (positive interface)
    #   tr_M(α · σ⁻¹) = (z - h) · tr_M(α) (negative interface)
    # Canonical atomic-braid interface census (per atom_braid_word_3A):
    #   D    = p · σ_3       · n           → 1 pos
    #   T    = p · σ_3       · n · σ_6⁻¹ · n → 1 pos + 1 neg
    #   ³He  = p · σ_3       · p · σ_6     · n → 2 pos
    #   ⁴He  = p · σ_3 · p · σ_6 · n · σ_9⁻¹ · n → 2 pos + 1 neg
    interface_census = {
        "D":   {"pos": 1, "neg": 0},
        "T":   {"pos": 1, "neg": 1},
        "3He": {"pos": 2, "neg": 0},
        "4He": {"pos": 2, "neg": 1},
    }
    z_ratio_tests = []
    atom_zn = {name: (Z, N) for name, Z, N in ATOMS}
    for atom_name in ("D", "T", "3He", "4He"):
        if atom_name not in results_full or atom_name not in results_constit:
            continue
        if "error" in results_full.get(atom_name, {}) or "error" in results_constit.get(atom_name, {}):
            continue
        try:
            tm_full = mp.mpf(str(results_full[atom_name]["total_tr_M"]))
            tm_constit = mp.mpf(str(results_constit[atom_name]["total_tr_M"]))
            if tm_constit == 0:
                continue
            ratio = tm_full / tm_constit
            Z_atom, N_atom = atom_zn[atom_name]
            A = Z_atom + N_atom
            census = interface_census[atom_name]
            expected = (z_markov ** census["pos"]) * (z_minus_h ** census["neg"])
            rel_err = abs(ratio - expected) / expected if expected != 0 else mp.mpf("inf")
            z_ratio_tests.append({
                "atom": atom_name, "A": A,
                "interfaces_positive": census["pos"],
                "interfaces_negative": census["neg"],
                "tau_M_full": float(tm_full), "tau_M_constit": float(tm_constit),
                "empirical_ratio": float(ratio),
                "predicted": float(expected),
                "predicted_formula": f"z^{census['pos']} · (z-h)^{census['neg']}",
                "rel_err": float(rel_err),
            })
        except Exception as e:
            print(f"  z-ratio test {atom_name}: ERR {e}")
    builder.add_data("z_ratio_tests", z_ratio_tests)

    print("\n=== Markov-axiom interface identity (proposition's content) ===")
    print(f"  Predicted: τ_M(β_K^FULL) / τ_M(β_K^CONSTIT) = z^(# pos) · (z-h)^(# neg)")
    print(f"  per Markov axiom + Hecke skein σ⁻¹ = σ - h·1")
    for t in z_ratio_tests:
        print(f"    {t['atom']} (A={t['A']}, {t['interfaces_positive']} pos + {t['interfaces_negative']} neg): "
              f"empirical = {t['empirical_ratio']:.8f}, "
              f"predicted {t['predicted_formula']} = {t['predicted']:.8f}, "
              f"rel.err = {t['rel_err']:.2e}")

    if z_ratio_tests:
        z_max_rel_err = max(t["rel_err"] for t in z_ratio_tests)
        builder.add_assertion(
            "markov_interface_identity_max_rel_err",
            computed=float(z_max_rel_err),
            expected=0.0,
            tolerance=1e-6,  # numerical precision floor of pyhecke_native f64
            unit="rel_err",
            source=(
                "τ_M(β_K^FULL) / τ_M(β_K^CONSTIT) = z^(# pos σ) · (z-h)^(# neg σ⁻¹) "
                "per Markov axiom + Hecke skein σ⁻¹ = σ − h·1 "
                "(prop:interface-knot-markov-z). Verified across "
                f"{len(z_ratio_tests)} atoms (D, T, ³He, ⁴He); max rel.err. "
                f"{float(z_max_rel_err) * 1e8:.2f}×10⁻⁸ (well below the "
                f"f64 numerical floor)."
            ),
        )

    # ── Exploratory assertion: FR identity (kept but separated as exploratory) ──
    if fr_tests:
        max_rel_err_abs = max(abs(t["rel_err_abs"]) for t in fr_tests
                              if t["scope"] == "FULL")
        builder.add_assertion(
            "fr_identity_max_rel_err_exploratory",
            computed=float(max_rel_err_abs),
            expected=0.0,
            tolerance=10.0,  # very loose — this is exploratory
            unit="rel_err",
            source=(
                "EXPLORATORY: FR identity τ_M(β_{Z=2}) / τ_M(β_{Z=1}) "
                "?= [3]_q²·cosh(h) does NOT hold for the full τ_M (the "
                "Phase 5b cosh(h) match is at the single-block |Δ_λ*| "
                "level, not the full sum). Recorded here for the "
                "negative-result audit trail. The primary z_ratio "
                "assertion above is the proposition's actual content."
            ),
        )

    # Lean SDP-uniqueness cross-reference (post-#1537 wiring).

    builder.add_data("lean_uniqueness_ref", {

        "generic": "qou:QOU.BraidKnot.@nucleus_uniqueness_closed (3*A)",

        "framework_doc":

            "content/quantum-observable-universe/lean/QOU/BraidKnot/NucleusEmptySDPUniqueness.lean",

        "note": "Certifies T_w uniqueness at the abstract empty-constraint SDP level (PR #1537 parameterised module). Workplan: docs/workplans/2026-05-31-witness-lean-uniqueness-ref-wiring.md.",

    })


    builder.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
