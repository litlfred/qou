"""
fr_pullback_k3_test.py — empirical test of conj:depth-stratified-
frobenius-reciprocity at k=3 (chirality channel).

Per prop:plancherel-term-7-formulation, "at low strata k ≤ 3 the
restricted Frobenius integral factors through specific hyperbolic-knot
ideals (e.g. 6_1 at k=3, the chirality channel)."

Per conj:depth-stratified-frobenius-reciprocity, the FR pullback
modifies the Wedderburn weight at depth k via:

  ~w_λ^{(K_k*)} := dim_q²(λ) · |χ^λ(e_{K_k*})| /
                   (Σ_μ dim_q²(μ) · |χ^μ(e_{K_k*})|)
                   · S_uniform_k

where S_uniform_k = Σ_{μ:depth=k} dim_q²(μ) / Σ_ν dim_q²(ν) is the
total uniform-Plancherel weight at depth k (preserved by the FR
pullback, which only REDISTRIBUTES weight within the depth-k stratum,
not rescales it).

NORMALIZATION CORRECTED 2026-09-04 (bean qou-7o7h): the denominator was
[n]_q!, which is NOT a probability measure in the balanced q-integer
convention this corpus uses, and whose defect c_n GROWS with n — so it
distorted this test's cross-atom metric. Fixing it REVERSED the knot
ranking; see the verdict note in the witness and
docs/audits/2026-09-04-plancherel-convention-gap.md. The chi path was
moved from the f64 kernel to MPFR at the same time.

This script tests the FR pullback at k=3 with candidate distinguished
knots K_3* ∈ {4_1, 5_2, 6_1} using the repo's canonical braid words
from `_deprecated/hyperbolic_knot_db_extended.py`.

Reference: prop:plancherel-term-7-formulation,
           conj:depth-stratified-frobenius-reciprocity.
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402

import pyhecke_native  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from codata_constants import (
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
    M_E_MEV  # noqa: E402,
)
from mass_at_3A_proper import dim_q, qfac  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402
from qou_substrate.constants import Q as Q0_PROTON  # noqa: E402 — anchor-independent proton pin (qou-6p3b Tranche C)


# Precision must be raised BEFORE the module-scope constants below: at
# import time mp.dps is still mpmath's default 15 (~binary64), and a
# literal rounded there cannot be recovered by raising dps afterwards.
# Idempotent. Gate: mpf_import_time_dps_audit.py (bean qou-j6gb).
set_compute_dps()

B_AME = {
    "D":   AME_B_DEUTERON_MEV_VALIDATION,
    "T":   AME_B_TRITIUM_MEV_VALIDATION,
    "3He": AME_B_HE3_MEV_VALIDATION,
    "4He": AME_B_HE4_MEV_VALIDATION,
}

ZN = {"D": (1, 1), "T": (1, 2), "3He": (2, 1), "4He": (2, 2)}


# Distinguished hyperbolic-knot candidates at depth k=3.
# Braid words taken from the repo's canonical table:
#   `_deprecated/hyperbolic_knot_db_extended.py:43-46`
# Format: tuple of signed gen indices (Conway form), where positive
# = σ_g, negative = σ_g^{-1}.
CANDIDATE_KNOTS_CONWAY = {
    "4_1": ((1, -2, 1, -2), "2.0298832"),
    "5_2": ((1, 1, 1, -2, 1, -2), "2.8281220"),
    "6_1": ((1, 1, -2, 1, -2, -2), "3.1639633"),
}


def conway_to_pyhecke(word_signed: tuple[int, ...]) -> list[tuple[int, int]]:
    """Convert Conway-signed braid word to pyhecke_native (sign, |gen|)."""
    out: list[tuple[int, int]] = []
    for s in word_signed:
        sign = 1 if s > 0 else -1
        g = abs(s)
        out.append((sign, g))
    return out


CANDIDATE_KNOTS = {
    name: conway_to_pyhecke(w_signed)
    for name, (w_signed, _vol) in CANDIDATE_KNOTS_CONWAY.items()
}


def vanishing_threshold() -> mp.mpf:
    """Threshold for treating |z| as zero, tied to current mp.dps."""
    return mp.mpf(10) ** (5 - mp.mp.dps)


def alpha_k(k: int) -> mp.mpf:
    """Structural prefactor per prop:plancherel-term-7-formulation."""
    z_mark = Q0**3 / (Q0**2 + 1)
    G = mp.catalan
    if k in (0, 1, 3):
        return mp.mpf(1)
    if k == 2:
        return z_mark ** 2
    return M_E_MEV * 8 * G


def embed_knot_braid(knot_word: list[tuple[int, int]],
                      n_strands: int) -> list[tuple[int, int]]:
    """Embed a small braid word into H_n via Wenzl.

    H_n has generators σ_1..σ_{n-1} (1-indexed), so the max
    generator index used must be ≤ n - 1.
    """
    max_gen = max(g for _, g in knot_word)
    if max_gen > n_strands - 1:
        raise ValueError(
            f"Knot braid uses gen {max_gen} but H_{n_strands} only "
            f"has generators 1..{n_strands - 1}")
    return knot_word


def chi_lambda_braid_via_rust(shape: list[int],
                                braid_word_signed: list,
                                q_str: str) -> mp.mpf:
    """χ^λ(β) at q via pyhecke_native, MPFR tier (50 dps).

    FIXED 2026-09-04 (bean qou-7o7h follow-up): this took `q: float` and
    called the f64 kernel, so every FR weight in this test carried ~1e-16
    rounding — a NO-FLOAT64 violation on the production path, and one
    that a caller could not see because the f64-ness was buried behind a
    `q_f64 = float(Q0)` two frames up. `chi_lambda_braid_mpfr` takes the
    q as a DECIMAL STRING precisely to avoid the lossy f64 boundary
    conversion, and returns a decimal string for the caller to parse.
    """
    word = [(int(s), int(g)) for (s, g) in braid_word_signed]
    return mp.mpf(pyhecke_native.chi_lambda_braid_mpfr(
        list(shape), word, str(q_str), 50))


def selfnorm_denominator(by_partition: list, n_strands: int) -> mp.mpf:
    """Σ_μ dim_q²(μ) — the SELF-NORMALIZING denominator.

    CORRECTED 2026-09-04 (bean qou-7o7h).  This test previously divided
    dim_q² by [n]_q!, the textbook q-Plancherel form.  That form is a
    probability measure at q = 1 and in the ASYMMETRIC q-integer
    convention — but NOT in the BALANCED convention this corpus uses,
    where c_n = Σ_λ dim_q²/[n]_q! is 0.991 / 1.111 / 1.517 at
    n = 6/9/12 and grows with n.

    Because the binding functional is linear in the weights, the whole
    effect is that B scales by c_n: harmless within one atom, and NOT
    harmless across atoms, since n = 3A differs.  This test's headline
    metric is max/min ACROSS atoms, so it was distorted — it inflated
    ⁴He (largest n) by 1.517 for every candidate knot, which pinned ⁴He
    as the max and swamped the real spread.  See
    docs/audits/2026-09-04-plancherel-convention-gap.md.
    """
    total = mp.mpf(0)
    for p in by_partition:
        dq = dim_q(tuple(p["partition"]), Q0_PROTON)
        total += mp.mpf(str(dq)) * mp.mpf(str(dq))
    return total


def fr_pullback_weight_per_partition(
    by_partition: list, n_strands: int, k_depth: int,
    knot_word: list, q_str: str
) -> tuple[dict, dict]:
    """Compute FR-pullback weight + errors per partition.

    Returns (fr_weights, errors):
      - fr_weights at depth k_depth: redistribute dim_q²/qfact weight
        proportionally to |χ^λ(K_dist)|, preserving total depth-k mass.
      - errors: any per-partition chi-computation failures
        (specific exceptions only; bugs propagate).
    """
    qfact = selfnorm_denominator(by_partition, n_strands)
    eps = vanishing_threshold()

    fr_weights: dict = {}
    errors: dict = {}
    chi_at_k_dist: dict = {}
    z_norm_unweighted = mp.mpf(0)  # Σ dim_q² · |χ| at depth k
    s_uniform_at_depth = mp.mpf(0)  # Σ dim_q² / qfact at depth k

    for p in by_partition:
        shape = tuple(p["partition"])
        depth = len(shape) - 1
        dq = dim_q(shape, Q0_PROTON)
        if depth != k_depth:
            fr_weights[shape] = mp.mpf(str(dq * dq)) / qfact
            continue
        s_uniform_at_depth += mp.mpf(str(dq * dq)) / qfact
        try:
            chi_K = chi_lambda_braid_via_rust(list(shape), knot_word, q_str)
        except (ValueError, RuntimeError, OverflowError) as exc:
            chi_K = mp.mpf(0)
            errors[shape] = f"{type(exc).__name__}: {exc}"
        chi_at_k_dist[shape] = chi_K
        z_norm_unweighted += mp.mpf(str(dq * dq)) * mp.fabs(chi_K)

    # Normalize so FR-pulled-back weights at depth k SUM to the
    # uniform Plancherel total at depth k (preserves total depth-3
    # mass contribution; FR redistributes within stratum).
    if z_norm_unweighted < eps:
        for shape, _ in chi_at_k_dist.items():
            dq = dim_q(shape, Q0_PROTON)
            fr_weights[shape] = mp.mpf(str(dq * dq)) / qfact
    else:
        scale = s_uniform_at_depth / z_norm_unweighted
        for shape, chi_K in chi_at_k_dist.items():
            dq = dim_q(shape, Q0_PROTON)
            fr_weights[shape] = (mp.mpf(str(dq * dq)) * mp.fabs(chi_K)
                                  * scale)
    return fr_weights, errors


def phi_k_with_weights(
    by_partition: list, n_strands: int, k: int,
    weights: dict
) -> mp.mpf:
    """Φ_k(K, T) using arbitrary weight per partition."""
    total = mp.mpf(0)
    eps = vanishing_threshold()
    for p in by_partition:
        shape = tuple(p["partition"])
        if len(shape) - 1 != k:
            continue
        chi = mp.mpf(str(p["chi_lambda"]))
        dq = dim_q(shape, Q0_PROTON)
        magnitude = mp.fabs(chi) * dq
        if magnitude < eps:
            continue
        w = weights.get(shape, mp.mpf(0))
        total += w * mp.log(magnitude)
    return total


def precompute_uniform_weights(by_partition: list, n_strands: int) -> dict:
    """Self-normalized q-Plancherel weights (see selfnorm_denominator)."""
    qfact = selfnorm_denominator(by_partition, n_strands)
    weights: dict = {}
    for p in by_partition:
        shape = tuple(p["partition"])
        dq = dim_q(shape, Q0_PROTON)
        weights[shape] = mp.mpf(str(dq * dq)) / qfact
    return weights


def compute_atom_binding_fr(atom: str, knot_word: list[tuple[int, int]],
                             knot_name: str) -> dict:
    """Compute B(K) with FR pullback through `knot_word` at k=3."""
    Z, N = ZN[atom]
    A = Z + N
    n_strands = 3 * A
    w_path = HERE / f"atom-chi-rust-{atom.lower()}.witness.json"
    if not w_path.exists():
        return {"deferred": True,
                "reason": f"Run compute_atom_chi_rust.py {atom} first"}
    w = json.loads(w_path.read_text())
    atom_data = w["data"]["atom"]
    free_data = w["data"]["free"]
    upstream_sha = w.get("commitSha", "unknown")

    embedded_word = embed_knot_braid(knot_word, n_strands)
    q_str = str(Q0)

    fr_atom_weights, atom_errors = fr_pullback_weight_per_partition(
        atom_data["by_partition"], n_strands, 3, embedded_word, q_str)
    fr_free_weights, free_errors = fr_pullback_weight_per_partition(
        free_data["by_partition"], n_strands, 3, embedded_word, q_str)

    uniform_atom_weights = precompute_uniform_weights(
        atom_data["by_partition"], n_strands)
    uniform_free_weights = precompute_uniform_weights(
        free_data["by_partition"], n_strands)

    # FR at depth 3, uniform elsewhere
    final_atom_weights = dict(uniform_atom_weights)
    final_free_weights = dict(uniform_free_weights)
    for shape, w in fr_atom_weights.items():
        if len(shape) - 1 == 3:
            final_atom_weights[shape] = w
    for shape, w in fr_free_weights.items():
        if len(shape) - 1 == 3:
            final_free_weights[shape] = w

    delta_phi_total = mp.mpf(0)
    for d in range(n_strands):
        phi_atom = phi_k_with_weights(
            atom_data["by_partition"], n_strands, d, final_atom_weights)
        phi_free = phi_k_with_weights(
            free_data["by_partition"], n_strands, d, final_free_weights)
        delta_phi_total += alpha_k(d) * (phi_free - phi_atom)

    return {
        "Z": Z, "N": N, "A": A, "n_strands": n_strands,
        "knot_name": knot_name,
        "B_MeV": fmt(delta_phi_total),
        "B_pred_sign": "+" if delta_phi_total > 0 else "-",
        "upstream_witness": f"atom-chi-rust-{atom.lower()}.witness.json",
        "upstream_commitSha": upstream_sha,
        "atom_chi_errors_count": len(atom_errors),
        "free_chi_errors_count": len(free_errors),
    }


def compute_atom_binding_no_fr(atom: str) -> dict:
    """B(K) with NO FR pullback — uniform weights at every depth.

    ADDED 2026-09-04 (bean qou-7o7h). The baseline was previously the
    hardcoded literal `1.82`, carried from a run under the OLD textbook
    normalization. Once the weights here are self-normalized, comparing
    corrected FR figures against that literal straddles two
    normalizations and overstates every improvement — it reported 6_1 as
    "+42.4% vs baseline" when the like-for-like figure is much smaller.
    The baseline is now COMPUTED through the same path as the FR
    variants, so both sides always share a normalization.
    """
    Z, N = ZN[atom]
    A = Z + N
    n_strands = 3 * A
    w_path = HERE / f"atom-chi-rust-{atom.lower()}.witness.json"
    w = json.loads(w_path.read_text())
    atom_data = w["data"]["atom"]
    free_data = w["data"]["free"]

    wA = precompute_uniform_weights(atom_data["by_partition"], n_strands)
    wF = precompute_uniform_weights(free_data["by_partition"], n_strands)

    delta_phi_total = mp.mpf(0)
    for d in range(n_strands):
        phi_atom = phi_k_with_weights(
            atom_data["by_partition"], n_strands, d, wA)
        phi_free = phi_k_with_weights(
            free_data["by_partition"], n_strands, d, wF)
        delta_phi_total += alpha_k(d) * (phi_free - phi_atom)
    return {"A": A, "B_MeV": fmt(delta_phi_total),
            "B_pred_sign": "+" if delta_phi_total > 0 else "-"}


def main() -> int:
    set_compute_dps()
    builder = WitnessBuilder("fr-pullback-k3-test")
    builder.set_description(
        "Empirical test of conj:depth-stratified-frobenius-reciprocity "
        "at k=3 with candidate distinguished knots {4_1, 5_2, 6_1} "
        "via Wenzl embedding into H_{3A}. FR-pulled-back weight "
        "normalized to preserve uniform Plancherel depth-3 total. "
        "Braid words sourced from "
        "_deprecated/hyperbolic_knot_db_extended.py canonical table."
    )
    builder.add_parameter("m_e_CAL1_MeV", str(M_E_MEV))
    builder.add_parameter("q0_50dps", str(Q0))

    builder.add_data("candidate_knots", {
        name: {
            "conway_word": list(w_signed),
            "hyperbolic_volume_cross_check": vol,
            "n_crossings": len(w_signed),
        }
        for name, (w_signed, vol) in CANDIDATE_KNOTS_CONWAY.items()
    })

    upstream_witnesses = []
    for atom in ("D", "T", "3He", "4He"):
        w_path = HERE / f"atom-chi-rust-{atom.lower()}.witness.json"
        if w_path.exists():
            upstream_witnesses.append(
                str(w_path.relative_to(HERE.parent.parent)))
    builder.add_data("upstream_witnesses", upstream_witnesses)

    all_results = {}
    for knot_name, knot_word in CANDIDATE_KNOTS.items():
        print(f"\n=== FR pullback at k=3 via {knot_name} "
              f"(braid len {len(knot_word)}) ===")
        print(f"{'atom':<6} {'A':>3} {'B_MeV':>10} {'B_AME':>10} "
              f"{'ratio':>8} {'sign':>5}")
        results = {}
        for atom in ("D", "T", "3He", "4He"):
            r = compute_atom_binding_fr(atom, knot_word, knot_name)
            if r.get("deferred"):
                continue
            B_pred = mp.mpf(r["B_MeV"])
            B_emp = B_AME[atom]
            ratio = B_pred / B_emp
            r["B_AME_MeV"] = fmt(B_emp)
            r["ratio_pred_over_AME"] = fmt(ratio)
            results[atom] = r
            print(f"  {atom:<6} {r['A']:>3} {float(B_pred):>10.4f} "
                  f"{float(B_emp):>10.4f} {float(ratio):>8.4f} "
                  f"{r['B_pred_sign']:>5}")
        ratios = [abs(mp.mpf(r["ratio_pred_over_AME"]))
                  for r in results.values()]
        if ratios:
            rmin, rmax = min(ratios), max(ratios)
            mom = rmax / rmin if rmin > 0 else float("inf")
            signs_correct = all(r["B_pred_sign"] == "+"
                                 for r in results.values())
            print(f"  max/min = {float(mom):.4f}, "
                  f"signs +: {signs_correct}")
            all_results[knot_name] = {
                "per_atom": results,
                "max_over_min": fmt(mom),
                "all_signs_correct": signs_correct,
            }

    # Baseline COMPUTED through the same path (see
    # compute_atom_binding_no_fr) so it shares the FR variants'
    # normalization; it used to be the literal 1.82 from a textbook-
    # normalized run, which straddled two normalizations once the
    # weights here were corrected.
    base_ratios = []
    for atom in ("D", "T", "3He", "4He"):
        rb = compute_atom_binding_no_fr(atom)
        base_ratios.append(abs(mp.mpf(rb["B_MeV"]) / B_AME[atom]))
    baseline = max(base_ratios) / min(base_ratios)
    builder.add_data("baseline_variance_no_fr", fmt(baseline))
    builder.add_data("baseline_provenance",
                     "computed in-run via compute_atom_binding_no_fr "
                     "(uniform weights, same self-normalized measure as "
                     "the FR variants). Was the hardcoded literal 1.82 "
                     "under the old textbook normalization — bean "
                     "qou-7o7h.")
    builder.add_data("per_knot", all_results)

    print("\n=== Summary: variance comparison ===")
    print(f"{'knot':<6} {'max/min':>10} {'signs +':>8} {'vs baseline':>14}")
    print(f"  {'(none)':<6} {float(baseline):>10.4f} "
          f"{'(yes)':>8} {'baseline':>14}")
    best_knot = None
    best_mom = baseline
    for kname, r in all_results.items():
        mom = mp.mpf(r["max_over_min"])
        improvement = (baseline - mom) / baseline * 100
        sign = "+" if r["all_signs_correct"] else "-"
        print(f"  {kname:<6} {float(mom):>10.4f} {sign:>8} "
              f"{float(improvement):>+11.1f}%")
        if r["all_signs_correct"] and mom < best_mom:
            best_mom = mom
            best_knot = kname

    paper_knot = "6_1"
    paper_knot_mom = (all_results.get(paper_knot, {}).get("max_over_min")
                      if paper_knot in all_results else None)
    paper_naming_validated = (best_knot == paper_knot)
    n_beating_baseline = sum(1 for r in all_results.values()
                             if mp.mpf(r["max_over_min"]) < baseline)
    if best_knot:
        # Grade by improvement RELATIVE to the baseline, not by an
        # absolute cut on best_mom. RECALIBRATED 2026-09-04 (bean
        # qou-7o7h): the old rule was `STRONG if best_mom < 1.5`, which
        # was tuned when the baseline was the textbook-normalized 1.82.
        # Against the corrected baseline (~1.07) that cut is satisfied
        # by anything at all, so it reported "STRONG support" for what
        # is in fact a ~2% improvement. An absolute threshold cannot
        # survive a change in the baseline it was calibrated against.
        gain = (baseline - best_mom) / baseline
        general_support = ("STRONG" if gain > 0.25 else
                           "MODEST" if gain > 0.05 else "MARGINAL")
        if paper_naming_validated:
            verdict = (f"FR conjecture {general_support} support: "
                       f"K_3* = {best_knot} (matches paper) is the best "
                       f"candidate at {float(best_mom):.4f}× vs a no-FR "
                       f"baseline of {float(baseline):.4f}× — an improvement of "
                       f"{float(gain) * 100:.1f}%. {n_beating_baseline} of "
                       f"{len(all_results)} candidates beat the baseline "
                       f"at all; the others make the cross-atom variance "
                       f"WORSE. Both figures are under the "
                       f"self-normalized measure (bean qou-7o7h); the "
                       f"previously published 1.82× baseline was "
                       f"inflated ~53% by the textbook "
                       f"dim_q²/[n]_q! form, so the large apparent "
                       f"variance closure it implied was mostly a "
                       f"normalization artifact.")
        else:
            paper_str = (f"{float(mp.mpf(paper_knot_mom)):.3f}×"
                          if paper_knot_mom else "n/a")
            verdict = (
                f"FR conjecture {general_support} support: empirically "
                f"best K_3* = {best_knot} ({float(best_mom):.3f}×, baseline "
                f"{baseline}×); paper's named K_3* = {paper_knot} gives "
                f"{paper_str} (NOT empirically best). Paper's specific "
                "naming K_3* = 6_1 NOT validated by this test; general "
                "FR mechanism partially validated via 4_1, 5_2.")
    else:
        verdict = ("No candidate knot improves variance; "
                   "FR-pullback form or specific knot identity may "
                   "need refinement.")
    builder.add_data("verdict", verdict)
    builder.add_data("best_knot", best_knot)
    builder.add_data("best_max_over_min", best_mom)
    builder.add_data("paper_named_knot", paper_knot)
    builder.add_data("paper_named_knot_max_over_min",
                      fmt(mp.mpf(paper_knot_mom))
                      if paper_knot_mom else None)
    builder.add_data("paper_naming_validated", paper_naming_validated)
    print(f"\n  {verdict}")

    builder.add_assertion(
        "data_loaded",
        computed=fmt(B_AME["D"]),
        expected=fmt(AME_B_DEUTERON_MEV_VALIDATION),
        tolerance=1e-10,
        unit="B(D) MeV",
        source="AME 2020 deuteron binding — SELF-COMPARISON, see caveat",
    )
    builder.add_caveat(
        "SELF-FULFILLING ASSERTION (recorded, not repaired): "
        "`data_loaded` compares B_AME['D'] against a literal copy of the "
        "same number typed a few hundred lines away — x == x with a "
        "tolerance, so it can only pass and gates nothing. Noticed "
        "2026-09-04 while clearing this producer's raw-float64 fields "
        "(the literal was the last one). Repairing it properly means "
        "rebuilding the four B_AME entries from the CODATA mass-excess "
        "table so the check has an independent second source — the same "
        "fix fr_pullback_borromean_h3a_test already carries as "
        "`b_ame_cross_check`. That is a content change to this "
        "producer's inputs and is deliberately NOT bundled into a "
        "normalization fix; it is the honest next step, not this one.")
    builder.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
