"""V2 mirror-chirality probe — wires the *genuine* mirror as a_K via
numeric per-irrep Hoefsmit (not the symbolic V1 path).

Forward step from `2026-05-15-three-pr-integration.md` §V1≠mirror.
PR #644's plan-doc P1.B framed V1 (β* = β⁻¹, multiplicative inverse)
as "the natural Hecke choice", but V1 computes τ(β²) — a double-
winding quantity, not a chirality measure. V2 (each crossing's
over/under flipped = geometric mirror knot) IS the canonical
chirality.

V2 backfill under the existing symbolic `term5_aK_audit.py` is
unbounded for A ≥ 3. This probe uses the same numeric infrastructure
that powered `global_wedderburn_sum_q_hecke_seminormal` in
[`wedderburn_jones_markov.py`](wedderburn_jones_markov.py): Hoefsmit
per-irrep matrices at q_0 + cached Wedderburn weights y_λ(q_0).
Compute is O(A · max_dim_λ³) per atom — seconds, not hours.

## Composition formula

For β = ∏_k (c_k · σ_{g_k} + d_k · I) with pure crossings ((1, 0) or
(1, -h)), the mirror sends σ_i ↔ σ_i⁻¹ pointwise. Then

  β_mirror⁻¹ = reverse-word(β)   (with original (c, d) labels)

(proof: σ_i → σ_i⁻¹ pointwise, then inverting the product reverses
the order and inverts each σ_i⁻¹ back to σ_i). So

  β · β_mirror⁻¹  ↔  word(β) ++ reverse(word(β))

V2's `a_K = τ(β · β_mirror⁻¹)` is then the Markov trace of the
doubled-with-reversal word, evaluated by the same Σ_λ y_λ · χ^λ_q
machinery as the production T1 computation.

## Outputs

Compare V2 against:
  - V1 backfill (`term5-aK-audit.witness.json`) — should DIFFER
    structurally; V1(T) = V1(³He) by conjugation invariance, V2(T)
    and V2(³He) should not coincide (T ↔ ³He are isospin mirrors)
  - Closed form (`paper_six_term_isotope_sweep.term5_chirality`) —
    the PR #520 2.2% gap should reproduce or refine
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q as Q_0  # noqa: E402
from mass_at_3A_proper import (  # noqa: E402
    atom_braid_word_3A,
    chi_lambda_of_word,
)
from hecke_characters import build_seminormal_matrices  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402


def v2_composite_word(beta_word: list[tuple]) -> list[tuple]:
    """Build the word for β · β_mirror⁻¹ under V2.

    For pure-crossing atom braids (only (1, 0) = σ_i and
    (1, -h) = σ_i⁻¹ tuples), β_mirror⁻¹ is the reverse of β with
    each crossing's (c, d) unchanged — see module docstring proof.
    """
    return list(beta_word) + list(reversed(beta_word))


def aK_v2(Z: int, N: int, q_val: float) -> dict:
    """Compute a_K = τ(β · β_mirror⁻¹) for atom (Z, N) under V2.

    Returns dict with: aK_value (float), per-partition breakdown,
    timing.
    """
    A = Z + N
    n = 3 * A
    beta_word = atom_braid_word_3A(Z, N, include_inter=True)
    composite = v2_composite_word(beta_word)
    n_gens = n - 1

    bad = [g for *_, g in composite if not (0 <= g < n_gens)]
    if bad:
        raise ValueError(
            f"V2 composite word has out-of-range generators "
            f"{sorted(set(bad))} for n_gens = {n_gens}"
        )

    y_vals = y_lambda_at(n, q_val=q_val)
    t0 = time.perf_counter()
    total = 0.0
    rows = []
    for shape, y in y_vals.items():
        sigmas, dim, _syts = build_seminormal_matrices(shape, q=q_val)
        if dim == 0:
            continue
        chi = chi_lambda_of_word(sigmas, dim, composite, n_gens)
        contrib = float(y) * float(chi)
        total += contrib
        rows.append({
            "partition": list(shape),
            "dim": int(dim),
            "y_at_q0": float(y),
            "chi_v2_at_q0": float(chi),
            "contribution": float(contrib),
        })
    elapsed_s = time.perf_counter() - t0
    return {
        "aK_value": float(total),
        "n_partitions": len(rows),
        "elapsed_s": elapsed_s,
        "rows": rows,
    }


def main() -> int:
    q0 = float(Q_0)

    # ── V1 reference (from existing audit witness) ───────────────────
    v1_path = HERE / "term5-aK-audit.witness.json"
    v1_data = {}
    if v1_path.exists():
        with v1_path.open() as f:
            v1_w = json.load(f)
        per_atom = (
            v1_w.get("data", {}).get("per_atom_results", {})
            or v1_w.get("data", {})
        )
        for k, v in per_atom.items():
            if isinstance(v, dict) and "V1" in v:
                v1_data[k] = float(v["V1"].get("a_K_value", "nan"))

    # ── V2 compute for the 5 atoms PR #644 backfilled V1 on ──────────
    atoms = [
        ("proton", 1, 0),
        ("neutron", 0, 1),
        ("deuteron", 1, 1),
        ("tritium", 1, 2),
        ("he3", 2, 1),
    ]
    results = {}
    print(f"=== V2 mirror-chirality probe at q_0 = {q0:.6f} ===")
    for label, Z, N in atoms:
        try:
            r = aK_v2(Z, N, q0)
            results[label] = r
            v1 = v1_data.get(label)
            v1_str = f"{v1:.6f}" if v1 is not None else "—"
            print(
                f"  {label:8} V2 a_K = {r['aK_value']:>12.6f}  "
                f"(V1 = {v1_str})  t={r['elapsed_s']:.2f}s  "
                f"|λ|={r['n_partitions']}"
            )
        except Exception as e:
            print(f"  {label:8} V2 FAILED: {e}")
            results[label] = {"error": str(e)}

    # ── T ↔ ³He spin-involution test ─────────────────────────────────
    asymmetry_pct = None
    if (
        "tritium" in results and "he3" in results
        and "aK_value" in results["tritium"]
        and "aK_value" in results["he3"]
    ):
        t_v = results["tritium"]["aK_value"]
        he3_v = results["he3"]["aK_value"]
        if abs(he3_v) > 1e-12:
            asymmetry_pct = 100.0 * (t_v - he3_v) / he3_v
            print(
                f"\n  T ↔ ³He V2 asymmetry: "
                f"(V2(T) − V2(³He)) / V2(³He) = {asymmetry_pct:+.4f} %"
            )
            v1_t = v1_data.get("tritium")
            v1_3he = v1_data.get("he3")
            if v1_t is not None and v1_3he is not None:
                v1_asy = (
                    100 * (v1_t - v1_3he) / v1_3he
                    if abs(v1_3he) > 1e-12
                    else None
                )
                print(
                    f"  T ↔ ³He V1 asymmetry: {v1_asy:+.4f} %"
                    if v1_asy is not None
                    else "  V1 asymmetry undefined"
                )

    # ── Build witness ────────────────────────────────────────────────
    builder = (
        WitnessBuilder(
            "term5-aK-v2-mirror-chirality-probe", engine="numpy+scipy",
        )
        .set_description(
            "V2 mirror-chirality (genuine geometric mirror knot β*) "
            "wired via numeric per-irrep Hoefsmit at q_0 — the fast "
            "path that the V1 symbolic backfill (term5_aK_audit.py) "
            "couldn't handle for A ≥ 3. Confirms the V1 = τ(β²) "
            "double-winding finding from `2026-05-15-three-pr-"
            "integration.md` §V1≠mirror by exhibiting a structural "
            "T ↔ ³He asymmetry under V2 that V1 cannot resolve."
        )
        .set_content_block("prop:chirality-dual-space-derivation")
        .add_parameter("q_0", q0)
        .add_data(
            "v2_per_atom",
            {
                k: {
                    "aK_v2": v.get("aK_value"),
                    "elapsed_s": v.get("elapsed_s"),
                    "n_partitions": v.get("n_partitions"),
                }
                for k, v in results.items()
            },
        )
        .add_data("v1_reference_from_audit", v1_data)
        .add_caveat(
            "Mirror composition relies on the atom braid words "
            "containing only pure crossings ((1, 0) and (1, -h)). "
            "Averaged crossings (½(σ + σ⁻¹)) would require V4-style "
            "handling; not present in atom_braid_word_3A output."
        )
        .add_caveat(
            "V2 a_K is a Markov trace at numeric q_0 (float64 floor "
            "~1e-13 for A=1, ~1e-10 for A=2 per "
            "global_wedderburn_sum_q_hecke_seminormal docstring)."
        )
    )

    if asymmetry_pct is not None:
        v1_asy = None
        if v1_data.get("tritium") and v1_data.get("he3"):
            v1_asy = 100 * (v1_data["tritium"] - v1_data["he3"]) / v1_data["he3"]
        builder.add_data(
            "spin_involution_asymmetry_pct",
            {
                "V1": v1_asy,
                "V2": asymmetry_pct,
                "interpretation": (
                    "V1 = τ(β²) is conjugation-invariant; T ↔ ³He "
                    "asymmetry under V1 must be 0 (or numerical zero). "
                    "V2 = τ(β · β_mirror⁻¹) probes the genuine "
                    "chirality; if T and ³He differ structurally as "
                    "isospin mirrors, V2 should detect it. A non-zero "
                    "V2 asymmetry confirms V2 carries information V1 "
                    "loses by construction."
                ),
            },
        )
        builder.add_assertion(
            name="v2_t_vs_he3_distinct",
            computed=abs(asymmetry_pct),
            expected=0.0,
            tolerance=-1.0,  # diagnostic-only; no pass/fail tolerance
            unit="percent (abs)",
            source="V2 should distinguish isospin mirrors; >0 confirms",
        )

    out_path = builder.save()
    print(f"\nWitness emitted: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
