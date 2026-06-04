"""qbeta_chain4_kashiwara_step4_n5 — Step 4 of Chain 4.

Extends PR #1772's NEGATIVE n≤4 sweep to partitions of n=5 against
the **corrected** target prefactor A / ℏ_q^15 ≈ 2.07 (per the
predecessor audit's h_q-bug honest correction — ℏ_q = (q − 1)/q,
not 0.0922502).

PARTITIONS OF n=5 (7 total):
  (5)          — single row; f^λ = 1, hooks = [5,4,3,2,1], cocharge=0
  (4,1)        — f^λ = 4, hooks = [5,3,2,1; 1]
  (3,2)        — f^λ = 5, hooks = [4,3,1; 2,1]
  (3,1,1)      — f^λ = 6, hooks = [5,2,1; 2; 1]
  (2,2,1)      — f^λ = 5, hooks = [4,2; 3,1; 1]
  (2,1,1,1)    — f^λ = 4, hooks = [5,1; 3; 2; 1]
  (1,1,1,1,1)  — single column; f^λ = 1, hooks = [5,4,3,2,1]

Total: 1 + 16 + 25 + 36 + 25 + 16 + 1 = 120 = 5! (Frobenius reciprocity)

WHY n=5: the n=4 sweep produced NEAR-FUZZY hits at q-dim_(2,2) ≈ 2.04
and cocharge_(2,2) = 2 (≈ 3.5% off target ≈ 2.07). The (2,2)-shaped
family has structural pull; the n=5 (2,2,1) partition is the natural
one-cell extension. If a (2,2,1)-derived invariant reaches NEAR-1PCT,
the family is structurally meaningful; if it remains NEAR-FUZZY only,
the predecessor's NEGATIVE verdict tightens further.

ANTI-PATTERN GUARDS:
  - TIERED reporting only.
  - NO ansatz proposed.
  - Cross-anchor BEFORE structural claim (Step 5b).
  - h_q computed from (q − 1)/q, not hard-coded.
"""

from __future__ import annotations

from pathlib import Path

import mpmath as mp

mp.mp.dps = 50

# Residue A — established by PR #1727 (simple pole, fibre-level, anchor-independent)
RESIDUE_A = mp.mpf("1.804e-15")
# Proton-pinned q_0 (post 2026-05-28 re-pin)
Q_PROTON_50 = mp.mpf("1.10997858275138080759166909561")
# Muon-pinned q_0 for cross-anchor (Step 5b)
Q_MUON_50 = mp.mpf("1.10997868769193107842185960213")


def h_q(q: mp.mpf) -> mp.mpf:
    """ℏ_q = (q − 1) / q — per predecessor audit's honest correction.

    DO NOT hard-code; compute from q to avoid the h_q = 0.0922502 bug
    that produced the spurious Step 2 NEAR-1PCT.
    """
    return (q - 1) / q


def enumerate_syt(shape: tuple[int, ...]) -> list[tuple[tuple[int, ...], ...]]:
    """Enumerate Standard Young Tableaux of given partition shape.

    Returns a list of tuples (each row is a tuple of ints). A SYT
    fills cells with 1..n such that rows increase L→R and columns
    increase top→bottom.

    Implemented by recursive cell-by-cell extension, keeping the
    invariant that the in-progress tableau is always a valid SYT
    prefix (insertions land at corners).
    """
    n = sum(shape)
    rows = len(shape)

    def add_one(tab: list[list[int]], k: int) -> list[list[list[int]]]:
        out = []
        for i in range(rows):
            row_len = len(tab[i])
            if row_len >= shape[i]:
                continue
            # Must be at a corner: row above must extend at least this far
            if i > 0 and len(tab[i - 1]) <= row_len:
                continue
            new_tab = [list(r) for r in tab]
            new_tab[i].append(k)
            out.append(new_tab)
        return out

    partials = [[[] for _ in range(rows)]]
    for k in range(1, n + 1):
        next_partials = []
        for tab in partials:
            next_partials.extend(add_one(tab, k))
        partials = next_partials
    return [tuple(tuple(r) for r in t) for t in partials]


def major_index(tab: tuple[tuple[int, ...], ...]) -> int:
    """Major index of a SYT: Σ i over descents.

    A descent of T is a position i ∈ {1, ..., n−1} such that i+1
    appears in a row STRICTLY below i in T.
    """
    pos = {}  # value → (row, col)
    for r, row in enumerate(tab):
        for c, v in enumerate(row):
            pos[v] = (r, c)
    n = sum(len(r) for r in tab)
    maj = 0
    for i in range(1, n):
        if pos[i + 1][0] > pos[i][0]:
            maj += i
    return maj


def maj_sum_syt(shape: tuple[int, ...]) -> int:
    """Σ over T ∈ SYT(shape) of maj(T) (sum of descent positions).

    The major index is the standard, well-defined SYT statistic:
      maj(T) = Σ i s.t. i is a descent of T
    where i is a descent if i+1 appears in a row STRICTLY below i.

    Note: the predecessor PR #1772 Step 2 hand-coded a field labeled
    "cocharge_sum" whose values do not match the rigorously-defined
    cocharge statistic (Lascoux-Schützenberger reading-word algorithm
    on SYT). We use the major index instead because (a) it is fully
    well-defined, (b) the q-Kostka identity
    Σ_T q^{maj(T)} = q^{n(λ)} · [n]_q! / ∏ [h(c)]_q
    (q-hook formula at µ = (1^n)) makes it the canonical SYT q-stat.
    """
    return sum(major_index(t) for t in enumerate_syt(shape))


def partition_invariants_n5() -> dict:
    """Compute basic invariants for the 7 partitions of n=5.

    SYT statistic `maj_sum` computed via full SYT enumeration and
    the descent-position major index. f^λ values are cross-checked
    against the enumeration count (assertion). `comaj_sum` was
    removed during the round-1 fixes; only `maj_sum` is populated.

    Cross-check: Σ (f^λ)² = n! gives 1+16+25+36+25+16+1 = 120 ✓
    """
    base = {
        "(5)":         {"f_lambda": 1, "shape": (5,),           "hooks": [5,4,3,2,1], "hook_product": 120, "shape_name": "row"},
        "(4,1)":       {"f_lambda": 4, "shape": (4,1),          "hooks": [5,3,2,1,1], "hook_product": 30,  "shape_name": "L-thin"},
        "(3,2)":       {"f_lambda": 5, "shape": (3,2),          "hooks": [4,3,1,2,1], "hook_product": 24,  "shape_name": "2-row"},
        "(3,1,1)":     {"f_lambda": 6, "shape": (3,1,1),        "hooks": [5,2,1,2,1], "hook_product": 20,  "shape_name": "T-rot"},
        "(2,2,1)":     {"f_lambda": 5, "shape": (2,2,1),        "hooks": [4,2,3,1,1], "hook_product": 24,  "shape_name": "(2,2)+1"},
        "(2,1,1,1)":   {"f_lambda": 4, "shape": (2,1,1,1),      "hooks": [5,1,3,2,1], "hook_product": 30,  "shape_name": "L-rot"},
        "(1,1,1,1,1)": {"f_lambda": 1, "shape": (1,1,1,1,1),    "hooks": [5,4,3,2,1], "hook_product": 120, "shape_name": "column"},
    }
    for name, d in base.items():
        sh = d["shape"]
        syt_list = enumerate_syt(sh)
        assert len(syt_list) == d["f_lambda"], (
            f"f^{name}: enumerated {len(syt_list)}, expected {d['f_lambda']}"
        )
        d["maj_sum"] = maj_sum_syt(sh)
        d["shape"] = list(sh)  # JSON-friendly
    return base


def q_integer(n: int, q: mp.mpf) -> mp.mpf:
    """[n]_q = (q^n - q^(-n)) / (q - q^(-1))."""
    if n == 0:
        return mp.mpf(0)
    return (q**n - q**(-n)) / (q - q**(-1))


def q_factorial(n: int, q: mp.mpf) -> mp.mpf:
    """[n]_q! = [1]_q · [2]_q · ... · [n]_q."""
    out = mp.mpf(1)
    for k in range(1, n + 1):
        out *= q_integer(k, q)
    return out


def q_dim_partition(hooks: list[int], q: mp.mpf, n: int) -> mp.mpf:
    """q-dim_q(λ) = [n]_q! / ∏ [h(c)]_q (q-hook formula)."""
    nf = q_factorial(n, q)
    hf = mp.mpf(1)
    for h in hooks:
        hf *= q_integer(h, q)
    return nf / hf


def build_candidates(inv: dict, q: mp.mpf) -> dict[str, mp.mpf]:
    """Build a ~50-candidate set of prefactor candidates from n=5 data.

    Includes per-partition invariants, cross-partition sums, and ratios
    specifically designed to extend the n=4 (2,2)-shaped NEAR-FUZZY thread.
    """
    out: dict[str, mp.mpf] = {}

    # Basic per-partition invariants
    for lam, d in inv.items():
        out[f"f^{lam}"] = mp.mpf(d["f_lambda"])
        out[f"hook_prod_{lam}"] = mp.mpf(d["hook_product"])
        out[f"1/hook_prod_{lam}"] = mp.mpf(1) / mp.mpf(d["hook_product"])
        out[f"maj_sum_{lam}"] = mp.mpf(d["maj_sum"])

    # q-dim_q for each partition at q_0
    for lam, d in inv.items():
        qd = q_dim_partition(d["hooks"], q, 5)
        out[f"q-dim_{lam}"] = qd
        out[f"q-dim²_{lam}"] = qd * qd

    # Cross-partition sums
    out["Σ f^λ (5-partitions)"] = sum(
        mp.mpf(d["f_lambda"]) for d in inv.values()
    )
    out["Σ q-dim (5-partitions)"] = sum(
        q_dim_partition(d["hooks"], q, 5) for d in inv.values()
    )
    out["Σ maj_sum (5-partitions)"] = sum(
        mp.mpf(d["maj_sum"]) for d in inv.values()
    )

    # Self-conjugate (2,2,1) extension of the n=4 (2,2) NEAR-FUZZY thread
    f_221 = mp.mpf(inv["(2,2,1)"]["f_lambda"])
    qd_221 = q_dim_partition(inv["(2,2,1)"]["hooks"], q, 5)
    out["q-dim_(2,2,1) · f^(2,2,1)"] = qd_221 * f_221
    out["q-dim_(2,2,1) / f^(2,2,1)"] = qd_221 / f_221

    # (3,2) — the other 2-row partition (potential bridge to Hecke n=5)
    f_32 = mp.mpf(inv["(3,2)"]["f_lambda"])
    qd_32 = q_dim_partition(inv["(3,2)"]["hooks"], q, 5)
    out["q-dim_(3,2) · f^(3,2)"] = qd_32 * f_32
    out["q-dim_(3,2) / f^(3,2)"] = qd_32 / f_32
    out["q-dim_(3,2) + q-dim_(2,2,1)"] = qd_32 + qd_221

    return out


def report_proximity(
    cands: dict[str, mp.mpf], target: mp.mpf
) -> dict[str, dict]:
    """TIERED proximity report (predecessor convention).

    Tier thresholds match their unit-clear names:
      NEAR-1PPM   = rel_err < 1e-6   (within 1 part per million)
      NEAR-0.1PCT = rel_err < 1e-3   (within 0.1%)
      NEAR-1PCT   = rel_err < 0.01   (within 1%)
      NEAR-FUZZY  = rel_err < 0.1    (within 10%)
      NEAR-CLOSE  = rel_err < 0.5    (within 50%)
      MISS        = rel_err ≥ 0.5

    Per-candidate dict carries BOTH `_num` (mp.mpf, used for sort) and
    a 6-digit display string. The witness emitter strips `_num` keys
    so the JSON payload stays clean.
    """
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
    print("Q_β Chain 4 Step 4 — Kashiwara crystal at n=5")
    print("Continuation of PR #1772 (NEGATIVE at n ≤ 4)")
    print("=" * 78)
    print()

    h_q_val = h_q(Q_PROTON_50)
    prefactor_target = RESIDUE_A / (h_q_val ** 15)
    print(f"ℏ_q (computed) = {mp.nstr(h_q_val, 8)}")
    print(f"ℏ_q^15 = {mp.nstr(h_q_val ** 15, 4)}")
    print(f"Target prefactor: A / ℏ_q^15 = {mp.nstr(prefactor_target, 8)}")
    print(f"  A = {mp.nstr(RESIDUE_A, 4)}")
    print()

    inv = partition_invariants_n5()
    print("Partition invariants (n=5):")
    print(f"  {'partition':12s} {'f^λ':5s} {'hook∏':8s} {'maj_sum':10s}")
    for lam, d in inv.items():
        print(f"  {lam:12s} {d['f_lambda']:3d}    "
              f"{d['hook_product']:6d}    {d['maj_sum']:3d}")
    print()

    cands = build_candidates(inv, Q_PROTON_50)
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

    print(f"Step 4 proximity results ({len(cands)} candidates):")
    print(f"  {'Candidate':40s} {'value':12s} {'ratio':12s} {'tier'}")
    for name, r in sorted_items[:20]:  # top 20
        print(f"  {name:40s} {r['value']:12s} {r['ratio']:12s} {r['tier']}")
    print()
    # Secondary cross-anchor target — emitted into witness for Step 6 use
    h_q_muon = h_q(Q_MUON_50)
    prefactor_target_muon = RESIDUE_A / (h_q_muon ** 15)

    best_tier = sorted_items[0][1]["tier"]
    best_name = sorted_items[0][0]
    best_ratio = sorted_items[0][1]["ratio"]

    print(f"BEST: {best_name} → {best_tier} (ratio {best_ratio})")
    print()

    near_matches = [
        (name, r) for name, r in results.items()
        if r["tier"] in (
            "NEAR-1PPM", "NEAR-0.1PCT", "NEAR-1PCT", "NEAR-FUZZY"
        )
    ]
    if near_matches:
        print(f"NEAR-MATCHES found ({len(near_matches)}):")
        for name, r in near_matches:
            print(f"  {name} → {r['tier']} (ratio {r['ratio']})")
        print()
        print("⚠ Single-anchor result (m_p-pin q_0 only). Step 5b must")
        print("  cross-anchor at q_muon BEFORE any structural claim.")
    else:
        print("VERDICT: NO near-matches at n=5 single-anchor probe.")
        print("The n=5 partition algebra at fixed cocharge / hook")
        print("does NOT yield the residue prefactor categorically here.")

    # Emit witness
    wb = WitnessBuilder(
        name="qbeta-chain4-kashiwara-step4-n5",
        engine="mpmath",
        output_dir=here,
    )
    wb.set_description(
        f"Step 4 of Chain 4 — Kashiwara crystal probe at n=5. "
        f"Continuation of PR #1772 NEGATIVE at n ≤ 4. Survey of "
        f"{len(cands)} prefactor candidates derived from partition "
        f"invariants of the 7 partitions of 5: f^λ, hook products, "
        f"major index sums (maj_sum, via SYT enumeration), and "
        f"q-dimensions at proton-pinned q_0. Target computed with "
        f"corrected ℏ_q = (q − 1)/q, NOT the buggy hard-coded "
        f"0.0922502 from Step 2. "
        f"Best near-match: {best_name} → {best_tier} (ratio {best_ratio}). "
        f"Anti-pattern guards respected: TIERED reporting; cross-anchor "
        f"deferred to Step 6; NO ansatz proposed."
    )
    wb.add_assertion(
        name="step4_enumeration_complete",
        computed=len(cands) >= 30,
        expected=True,
        source=f"Step 4 enumerated {len(cands)} candidates (target ≥ 30)",
    )
    wb.add_assertion(
        name="h_q_computed_not_hardcoded",
        computed=abs(h_q_val - mp.mpf("0.0922502")) > mp.mpf("0.005"),
        expected=True,
        source=(
            "ℏ_q = (q − 1)/q ≈ 0.09908, distinct from the Step 2 bug value "
            "0.0922502. Honest-correction guard."
        ),
    )
    wb.add_data("residue_target_A", str(RESIDUE_A))
    wb.add_data("prefactor_target_proton", str(prefactor_target))
    wb.add_data("prefactor_target_muon", str(prefactor_target_muon))
    wb.add_data("h_q_substrate_proton", str(h_q_val))
    wb.add_data("h_q_substrate_muon", str(h_q_muon))
    wb.add_data("q_proton", str(Q_PROTON_50))
    wb.add_data("q_muon", str(Q_MUON_50))
    wb.add_data("partition_invariants_n5", inv)
    wb.add_data(
        "step4_results_top10",
        {name: witness_safe(r) for name, r in sorted_items[:10]},
    )
    wb.add_data("best_match", {
        "candidate": best_name,
        "tier": best_tier,
        "ratio": best_ratio,
    })
    wb.add_data("near_match_count", len(near_matches))
    wb.add_data("next_step", "Step 5: Demazure characters at fundamental weights")
    out_path = wb.save()
    print(f"  Witness: {out_path.name}")


if __name__ == "__main__":
    main()
