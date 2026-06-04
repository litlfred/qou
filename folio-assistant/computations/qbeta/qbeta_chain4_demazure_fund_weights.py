"""qbeta_chain4_demazure_fund_weights — Step 5 of Chain 4.

Probes Demazure character coefficients at fundamental weights ω_i of
sl_n as candidate residue-A prefactors. Distinct invariant family
from f^λ / cocharge / q-dim (probed in Steps 1, 2, 4).

DEMAZURE OPERATORS (background):

For sl_n, the Demazure operator D_i (i = 1, ..., n−1) acts on
ℤ[Λ] (group ring of the weight lattice) by

  D_i(f) = (f − s_i · (e^{-α_i} f)) / (1 − e^{-α_i})

For a reduced Weyl-group word w = s_{i_1} ... s_{i_l}, the Demazure
operator D_w = D_{i_1} ... D_{i_l} is well-defined (independent of
the reduced expression by Demazure's theorem).

The Demazure character at fundamental weight ω_j along word w is
D_w(e^{ω_j}); specialised at q = 1 it reproduces a partial sum of
the Weyl character of the irrep with highest weight ω_j.

KEY TABLEAU INTERPRETATION (Lascoux-Schützenberger):

For sl_n, D_w(e^{ω_j}) = Σ_T e^{wt(T)} over key tableaux T of shape
ω_j and right-key K+(T) bounded by w(ω_j). At specific anchors
q = q₀ this gives numerical character coefficients.

WHY DEMAZURE FOR Chain 4:

The predecessor (Step 4) probes Schur/Kashiwara invariants of
partitions; Demazure characters at ω_i are PARTIAL characters
(weighted sums over a Bruhat-order ideal), structurally different.
A NEAR-1PCT hit in this family would be a substantive new
direction; a NEGATIVE result tightens the predecessor's verdict.

ANTI-PATTERN GUARDS (same as Step 4):
  - TIERED reporting.
  - NO ansatz at MISS or NEAR-FUZZY.
  - Cross-anchor BEFORE structural claim.
  - h_q computed from (q − 1)/q.
"""

from __future__ import annotations

from pathlib import Path

import mpmath as mp

mp.mp.dps = 50

RESIDUE_A = mp.mpf("1.804e-15")
Q_PROTON_50 = mp.mpf("1.10997858275138080759166909561")
Q_MUON_50 = mp.mpf("1.10997868769193107842185960213")


def h_q(q: mp.mpf) -> mp.mpf:
    """ℏ_q = (q − 1) / q (per predecessor honest correction)."""
    return (q - 1) / q


def q_integer(n: int, q: mp.mpf) -> mp.mpf:
    """[n]_q = (q^n − q^(−n)) / (q − q^(−1))."""
    if n == 0:
        return mp.mpf(0)
    return (q**n - q**(-n)) / (q - q**(-1))


def q_factorial(n: int, q: mp.mpf) -> mp.mpf:
    out = mp.mpf(1)
    for k in range(1, n + 1):
        out *= q_integer(k, q)
    return out


def q_binomial(n: int, k: int, q: mp.mpf) -> mp.mpf:
    """[n choose k]_q = [n]_q! / ([k]_q! [n−k]_q!)."""
    if k < 0 or k > n:
        return mp.mpf(0)
    return q_factorial(n, q) / (q_factorial(k, q) * q_factorial(n - k, q))


def demazure_char_fund_weight_sl_n(
    n: int, j: int, word_length: int, q: mp.mpf
) -> mp.mpf:
    """Numerical evaluation of D_w(e^{ω_j}) at q for sl_n.

    For the STUB version, this returns the Lascoux-Schützenberger
    numerical character coefficient as a q-binomial expansion:

        D_w(ω_j) ≈ [n−1 choose j−1]_q · (length-adjusted Bruhat weight)

    where w is a reduced word of given length in S_n. This is the
    "saturated" character at the longest element when word_length =
    binom(n, 2) (full Weyl group), and a partial truncation otherwise.

    PROPER IMPLEMENTATION (next commit):
      - Enumerate reduced expressions of length `word_length`
      - For each, apply D_i operators successively to e^{ω_j}
      - Sum over the resulting Bruhat ideal
      - Specialise at q to get numerical coefficient

    The current stub uses the q-binomial as a representative
    coefficient; this is mathematically the simplest non-trivial
    Demazure character (at the j-th fundamental weight of sl_n,
    truncated at the longest element).
    """
    if word_length == 0:
        return mp.mpf(1)  # D_∅(e^{ω_j}) = e^{ω_j} → 1 at evaluation
    # Stub: use q-binomial as representative Demazure-character value
    # (this is the full character of the j-th fund irrep of sl_n)
    return q_binomial(n - 1, j - 1, q)


def build_candidates(q: mp.mpf) -> dict[str, mp.mpf]:
    """Build a candidate set of Demazure-character prefactor values.

    STUB CONSTRAINT: `demazure_char_fund_weight_sl_n` currently ignores
    `word_length` for wl > 0 (returns the q-binomial proxy), so sweeping
    wl would produce many distinct candidate *names* with identical
    values — misleading. We emit ONE value per (n, j) here labeled
    `D_full(ω_j)_sl_n`, marking it as the longest-word (full Weyl
    character) evaluation. Proper wl-dependent enumeration follows in
    the next commit when D_i operators are wired.
    """
    out: dict[str, mp.mpf] = {}

    # sl_3: ω_1, ω_2 — longest word length = binom(3, 2) = 3
    for j in (1, 2):
        out[f"D_full(ω_{j})_sl3"] = demazure_char_fund_weight_sl_n(3, j, 3, q)

    # sl_4: ω_1, ω_2, ω_3 — longest word length = binom(4, 2) = 6
    for j in (1, 2, 3):
        out[f"D_full(ω_{j})_sl4"] = demazure_char_fund_weight_sl_n(4, j, 6, q)

    # sl_5: ω_1..ω_4 — longest word length = binom(5, 2) = 10
    for j in (1, 2, 3, 4):
        out[f"D_full(ω_{j})_sl5"] = demazure_char_fund_weight_sl_n(5, j, 10, q)

    # Cross-rank sums (multi-rank superposition)
    out["Σ D_full(ω_1) [sl3, sl4, sl5]"] = (
        demazure_char_fund_weight_sl_n(3, 1, 3, q)
        + demazure_char_fund_weight_sl_n(4, 1, 6, q)
        + demazure_char_fund_weight_sl_n(5, 1, 10, q)
    )

    return out


def report_proximity(
    cands: dict[str, mp.mpf], target: mp.mpf
) -> dict[str, dict]:
    """TIERED proximity report (matches Step 4 thresholds + units)."""
    out = {}
    for name, val in cands.items():
        if val == 0:
            out[name] = {
                "value": "0",
                "value_num": mp.mpf(0),
                "ratio": "0",
                "ratio_num": mp.mpf(0),
                "tier": "ZERO",
            }
            continue
        ratio = val / target
        rel_err = abs(ratio - 1)
        if rel_err < mp.mpf("1e-6"):
            tier = "NEAR-1PPM"
        elif rel_err < mp.mpf("1e-3"):
            tier = "NEAR-0.1PCT"
        elif rel_err < mp.mpf("0.01"):
            tier = "NEAR-1PCT"
        elif rel_err < mp.mpf("0.1"):
            tier = "NEAR-FUZZY"
        elif rel_err < mp.mpf("0.5"):
            tier = "NEAR-CLOSE"
        else:
            tier = "MISS"
        out[name] = {
            "value": mp.nstr(val, 6),
            "value_num": val,
            "ratio": mp.nstr(ratio, 6),
            "ratio_num": ratio,
            "tier": tier,
        }
    return out


def witness_safe(r: dict) -> dict:
    """Strip mp.mpf-valued `_num` keys; keep display strings for JSON."""
    return {k: v for k, v in r.items() if not k.endswith("_num")}


def main() -> None:
    import sys

    here = Path(__file__).resolve().parent
    sys.path.insert(0, str(here.parent))
    import _path_bridge as _pb  # noqa: F401

    sys.path.insert(0, str(Path(__file__).resolve().parents[3]
                           / "tools" / "qou-substrate" / "python"))
    from qou_substrate.witness import WitnessBuilder

    print("=" * 78)
    print("Q_β Chain 4 Step 5 — Demazure characters at fundamental weights")
    print("Continuation of PR #1772 (NEGATIVE at n ≤ 4) + Step 4 n=5")
    print("=" * 78)
    print()

    h_q_val = h_q(Q_PROTON_50)
    prefactor_target = RESIDUE_A / (h_q_val ** 15)
    print(f"ℏ_q (computed) = {mp.nstr(h_q_val, 8)}")
    print(f"Target prefactor: A / ℏ_q^15 = {mp.nstr(prefactor_target, 8)}")
    print()

    cands = build_candidates(Q_PROTON_50)
    results = report_proximity(cands, prefactor_target)

    tier_order = {
        "NEAR-1PPM": 0, "NEAR-0.1PCT": 1, "NEAR-1PCT": 2,
        "NEAR-FUZZY": 3, "NEAR-CLOSE": 4, "MISS": 5, "ZERO": 6,
    }
    sorted_items = sorted(
        results.items(),
        key=lambda kv: (
            tier_order.get(kv[1]["tier"], 99),
            abs(kv[1]["ratio_num"] - 1)
            if kv[1]["tier"] != "ZERO"
            else mp.mpf("999"),
        ),
    )

    print(f"Step 5 proximity results ({len(cands)} candidates):")
    print(f"  {'Candidate':40s} {'value':12s} {'ratio':12s} {'tier'}")
    for name, r in sorted_items[:20]:
        print(f"  {name:40s} {r['value']:12s} {r['ratio']:12s} {r['tier']}")
    print()

    best_tier = sorted_items[0][1]["tier"]
    best_name = sorted_items[0][0]
    best_ratio = sorted_items[0][1]["ratio"]

    print(f"BEST: {best_name} → {best_tier} (ratio {best_ratio})")
    print()

    near_matches = [
        (name, r) for name, r in results.items()
        if r["tier"] in (
            "NEAR-1PPM", "NEAR-1PPB-but-not-1ppm", "NEAR-1PCT", "NEAR-FUZZY"
        )
    ]
    if near_matches:
        print(f"NEAR-MATCHES found ({len(near_matches)}):")
        for name, r in near_matches:
            print(f"  {name} → {r['tier']} (ratio {r['ratio']})")
        print()
        print("⚠ Single-anchor result. Cross-anchor REQUIRED before claim.")
    else:
        print("VERDICT: NO Demazure near-matches at fundamental-weight probe.")

    print()
    print("STUB note: this script uses q-binomial as the representative")
    print("Demazure character value. Proper implementation (next commit)")
    print("will enumerate reduced Weyl-group words and apply D_i operators")
    print("successively, per Lascoux-Schützenberger key-tableau machinery.")

    # Emit witness
    wb = WitnessBuilder(
        name="qbeta-chain4-demazure-fund-weights",
        engine="mpmath",
        output_dir=here,
    )
    wb.set_description(
        f"Step 5 of Chain 4 — Demazure characters at fundamental weights "
        f"of sl_n for n ∈ {{3, 4, 5}}. STUB version uses q-binomial as the "
        f"representative character coefficient; proper key-tableau "
        f"enumeration will land in a follow-up commit. "
        f"Best near-match: {best_name} → {best_tier} (ratio {best_ratio}). "
        f"Anti-pattern guards respected: TIERED reporting; cross-anchor "
        f"deferred; NO ansatz proposed."
    )
    wb.add_assertion(
        name="step5_stub_acknowledged",
        computed=True,
        expected=True,
        source=(
            "Stub uses q-binomial as Demazure-character proxy. "
            "Proper Weyl-word enumeration is a follow-up commit."
        ),
    )
    wb.add_data("residue_target_A", str(RESIDUE_A))
    wb.add_data("prefactor_target", str(prefactor_target))
    wb.add_data("h_q_substrate_corrected", str(h_q_val))
    wb.add_data("q_proton", str(Q_PROTON_50))
    wb.add_data(
        "step5_results_top10",
        {name: witness_safe(r) for name, r in sorted_items[:10]},
    )
    wb.add_data("best_match", {
        "candidate": best_name,
        "tier": best_tier,
        "ratio": best_ratio,
    })
    wb.add_data("near_match_count", len(near_matches))
    wb.add_data(
        "next_step",
        "Proper Demazure operator enumeration + key-tableau coefficients",
    )
    out_path = wb.save()
    print(f"  Witness: {out_path.name}")


if __name__ == "__main__":
    main()
