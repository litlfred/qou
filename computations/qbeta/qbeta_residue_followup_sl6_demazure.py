"""qbeta_residue_followup_sl6_demazure — Direction 1: sl_6 control.

Extends the PR #1787 real-D_i Demazure-character residue-A probe to
sl_6 (720 permutations × 5 fundamental weights ω_1…ω_5 ≈ 3600
candidates). Reuses the Kashiwara-crystal subset model verbatim from
qbeta_chain4_demazure_fund_weights.

EXPECTED LOW YIELD: sl_3/4/5 (PR #1787) showed no scaling toward the
target prefactor A/ℏ_q^15 ≈ 2.072, so this is a CONTROL that closes the
higher-rank door — not a hopeful probe. TIERED; cross-anchor any
NEAR-1PCT.

ANTI-PATTERN GUARDS: TIERED; no ansatz; cross-anchor before claim;
ℏ_q from (q−1)/q; diagnostic-only.

Usage:
  python3 computations/qbeta/qbeta_residue_followup_sl6_demazure.py
Emits: qbeta-residue-followup-sl6-demazure.witness.json
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

# Reuse the PR #1787 real-D_i Demazure machinery verbatim.
from qbeta_chain4_demazure_fund_weights import (  # noqa: E402
    h_q,
    demazure_char_at_word,
    sample_reduced_words,
    report_proximity,
    witness_safe,
)

mp.mp.dps = 50

RESIDUE_A = mp.mpf("1.804e-15")
Q_PROTON_50 = mp.mpf("1.10997858275138080759166909561")
Q_MUON_50 = mp.mpf("1.10997868769193107842185960213")

RANK = 6  # sl_6


def build_sl6_candidates(q: mp.mpf) -> dict[str, mp.mpf]:
    """Demazure characters χ_w(ω_j) for w ∈ S_6, j = 1..5."""
    out: dict[str, mp.mpf] = {}
    words = sample_reduced_words(RANK)
    for j in range(1, RANK):  # ω_1 … ω_5
        for w in words:
            wstr = "·".join(f"s{k}" for k in w) if w else "e"
            out[f"D_{wstr}(ω_{j})_sl{RANK}"] = demazure_char_at_word(
                RANK, j, w, q
            )
    return out


def run_anchor(q: mp.mpf) -> tuple[dict, mp.mpf]:
    hbar = h_q(q)
    target = RESIDUE_A / (hbar ** 15)
    cands = build_sl6_candidates(q)
    return report_proximity(cands, target), target


def main() -> int:
    print("=" * 78)
    print("Q_β residue-A follow-up — Direction 1: sl_6 Demazure control")
    print("=" * 78)

    hbar_p = h_q(Q_PROTON_50)
    target_p = RESIDUE_A / (hbar_p ** 15)
    hbar_m = h_q(Q_MUON_50)
    target_m = RESIDUE_A / (hbar_m ** 15)
    print(f"ℏ_q (proton, computed) = {mp.nstr(hbar_p, 8)}")
    print(f"Target prefactor (proton): A / ℏ_q^15 = {mp.nstr(target_p, 8)}")
    print()

    n_words = len(sample_reduced_words(RANK))
    print(f"sl_6: {n_words} permutations × 5 weights = {5 * n_words} chars")

    results_p, _ = run_anchor(Q_PROTON_50)
    print(f"Candidates enumerated: {len(results_p)}")
    print()

    tier_order = {"NEAR-1PPM": 0, "NEAR-0.1PCT": 1, "NEAR-1PCT": 2,
                  "NEAR-FUZZY": 3, "NEAR-CLOSE": 4, "MISS": 5, "ZERO": 6}
    sorted_items = sorted(
        results_p.items(),
        key=lambda kv: (tier_order.get(kv[1]["tier"], 99),
                        abs(kv[1]["ratio_num"] - 1)),
    )

    print(f"  {'Candidate':40s} {'value':12s} {'ratio':11s} tier")
    for name, r in sorted_items[:15]:
        print(f"  {name:40s} {r['value']:12s} {r['ratio']:11s} {r['tier']}")
    print()

    best_name, best = sorted_items[0]
    print(f"BEST (proton): {best_name} → {best['tier']} (ratio {best['ratio']})")
    print()

    hist: dict[str, int] = {}
    for r in results_p.values():
        hist[r["tier"]] = hist.get(r["tier"], 0) + 1
    print("Tier histogram (proton):")
    for t in ["NEAR-1PPM", "NEAR-0.1PCT", "NEAR-1PCT", "NEAR-FUZZY",
              "NEAR-CLOSE", "MISS", "ZERO"]:
        if hist.get(t):
            print(f"  {t:12s}: {hist[t]}")
    print()

    # Cross-anchor any proton NEAR-1PCT-or-better.
    near = [(name, r) for name, r in results_p.items()
            if r["tier"] in ("NEAR-1PPM", "NEAR-0.1PCT", "NEAR-1PCT")]
    cross_anchor: dict[str, dict] = {}
    if near:
        print(f"⚠ {len(near)} NEAR-1PCT-or-better at proton — cross-anchoring:")
        results_m, _ = run_anchor(Q_MUON_50)
        for name, r in near:
            rm = results_m.get(name, {})
            swing = "n/a"
            if rm and rm.get("ratio_num"):
                swing = mp.nstr(abs(r["ratio_num"] / rm["ratio_num"] - 1) * 100, 5)
            cross_anchor[name] = {
                "proton_ratio": r["ratio"], "proton_tier": r["tier"],
                "muon_ratio": rm.get("ratio", "?"), "muon_tier": rm.get("tier", "?"),
                "cross_anchor_swing_pct": swing,
            }
            print(f"  {name}: proton {r['ratio']} | muon {rm.get('ratio','?')} "
                  f"| swing {swing}%")
        print()
        print("  NOTE: anchors differ ~1e-7; swing near-vacuous for closed-form")
        print("  candidates — proximity tier is the operative discriminator.")
    else:
        print("VERDICT: NO sl_6 Demazure character reaches NEAR-1PCT at proton.")
    print()

    # ─── Witness ──────────────────────────────────────────────────────
    w = WitnessBuilder("qbeta-residue-followup-sl6-demazure", engine="mpmath")
    w.set_description(
        f"Direction 1 (sl_6 control) of the residue-A follow-up. Extends the "
        f"PR #1787 real-D_i Demazure probe to sl_6: {n_words} permutations × "
        f"5 fundamental weights ω_1..ω_5 = {len(results_p)} candidates, "
        f"Kashiwara-crystal subset model, principal q-specialisation at "
        f"proton q_0. Target A/ℏ_q^15 ≈ {mp.nstr(target_p, 6)}. Best: "
        f"{best_name} → {best['tier']} (ratio {best['ratio']}). Expected low "
        f"yield (control). TIERED; cross-anchor; ℏ_q=(q-1)/q; diagnostic-only."
    )
    w.add_data("residue_target_A", str(RESIDUE_A))
    w.add_data("prefactor_target_proton", str(target_p))
    w.add_data("prefactor_target_muon", str(target_m))
    w.add_data("h_q_proton", str(hbar_p))
    w.add_data("q_proton", str(Q_PROTON_50))
    w.add_data("q_muon", str(Q_MUON_50))
    w.add_data("rank", str(RANK))
    w.add_data("permutation_count", str(n_words))
    w.add_data("candidate_count", str(len(results_p)))
    w.add_data("tier_histogram", {k: str(v) for k, v in hist.items()})
    w.add_data("top10", {name: witness_safe(r) for name, r in sorted_items[:10]})
    w.add_data("best_match", {"candidate": best_name, "tier": best["tier"],
                              "ratio": best["ratio"]})
    w.add_data("near_1pct_count", str(len(near)))
    if cross_anchor:
        w.add_data("cross_anchor", cross_anchor)
    w.add_assertion(
        name="sl6_demazure_reaches_near_1pct",
        computed=bool(len(near) > 0),
        expected=False, tolerance=0,
        source="Control: sl_3/4/5 showed no scaling toward target (PR #1787). "
               "Default expectation: no sl_6 Demazure character reaches "
               "NEAR-1PCT either.",
    )
    out = w.save()
    print(f"  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
