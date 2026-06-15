"""
Jet-Stratified Gröbner–Shirshov Benchmark

Compares naive Buchberger vs jet-stratified GS verification on
the Hecke algebra H_n(q) at increasing jet levels.

Measures:
  1. S-polynomial pair counts (naive vs stratified)
  2. Proxy reduction step counts (naive vs degree-bucketed)
  3. Wall-clock time for both algorithms

Caveat: reduction is a monomial-rewriting proxy (replaces by first
RHS term, not full polynomial reduction).  Pair-count savings are
exact; wall-clock speedups are indicative of structure, not a
faithful GS verification runtime.

The Hecke algebra with n generators has:
  - n Hecke relations (degree 2): σᵢ² → (q-q⁻¹)σᵢ + 1
  - ~n Yang–Baxter relations (degree 3): σᵢσⱼσᵢ → σⱼσᵢσⱼ
  - ~n² far-commutativity relations (degree 2): σᵢσⱼ → σⱼσᵢ

Jet prolongation adds 3 new generators per level (SU(2) case).

Usage:
    python jet-stratified-benchmark.py
"""

import time
import json
from dataclasses import dataclass
from typing import List, Tuple, Optional
from q_parameter import Q, Q_INV

# ══════════════════════════════════════════════════════════════
# §1  Hecke Algebra Rewriting System
# ══════════════════════════════════════════════════════════════


@dataclass
class ReductionRule:
    """A reduction rule: leading monomial → replacement terms."""
    lm: Tuple[int, ...]          # leading monomial (generator indices)
    rhs: List[Tuple[float, Tuple[int, ...]]]  # [(coeff, monomial), ...]
    degree: int = 0              # len(lm), cached
    rule_class: str = "descended"  # "descended" or "transient"

    def __post_init__(self):
        self.degree = len(self.lm)


def hecke_rules(n_gens: int) -> List[ReductionRule]:
    """Build the Hecke rewriting system for n_gens generators."""
    rules = []
    qq = Q - Q_INV  # q - q⁻¹

    # Hecke relations: σᵢ² → (q-q⁻¹)σᵢ + 1
    for i in range(n_gens):
        rules.append(ReductionRule(
            lm=(i, i),
            rhs=[(qq, (i,)), (1.0, ())],
        ))

    # Yang–Baxter: σᵢσⱼσᵢ → σⱼσᵢσⱼ for adjacent pairs
    for i in range(n_gens - 1):
        j = i + 1
        rules.append(ReductionRule(
            lm=(i, j, i),
            rhs=[(1.0, (j, i, j))],
        ))

    # Far-commutativity: σᵢσⱼ → σⱼσᵢ for |i-j| ≥ 2, i > j
    for i in range(n_gens):
        for j in range(n_gens):
            if i > j + 1:
                rules.append(ReductionRule(
                    lm=(i, j),
                    rhs=[(1.0, (j, i))],
                ))

    return rules


# ══════════════════════════════════════════════════════════════
# §2  S-Polynomial Overlap Detection
# ══════════════════════════════════════════════════════════════

def find_overlaps(lm1: Tuple[int, ...],
                  lm2: Tuple[int, ...]) -> List[Tuple[int, ...]]:
    """Find all proper overlaps between two leading monomials.

    An overlap exists when a proper suffix of lm1 equals a proper
    prefix of lm2.  Full-word overlaps (k == len) are excluded
    since those correspond to inclusion compositions."""
    overlaps = []
    max_overlap = min(len(lm1), len(lm2))
    for k in range(1, max_overlap):
        if lm1[-k:] == lm2[:k]:
            overlaps.append(lm1[-k:])
    return overlaps


def has_inclusion(lm_inner: Tuple[int, ...],
                  lm_outer: Tuple[int, ...]) -> bool:
    """Check if lm_inner appears as a proper subword of lm_outer."""
    n, m = len(lm_outer), len(lm_inner)
    if m >= n:
        return False  # must be strictly shorter
    for start in range(n - m + 1):
        if lm_outer[start:start + m] == lm_inner:
            return True
    return False


# ══════════════════════════════════════════════════════════════
# §3  Naive Buchberger Verification
# ══════════════════════════════════════════════════════════════

@dataclass
class BenchmarkResult:
    """Results from one benchmark run."""
    n_gens: int
    n_rules: int
    n_desc_rules: int = 0
    n_trans_rules: int = 0

    # Naive Buchberger
    naive_pairs_checked: int = 0
    naive_overlaps_found: int = 0
    naive_inclusions_found: int = 0
    naive_reductions: int = 0
    naive_time_ms: float = 0.0

    # Jet-stratified
    strat_pairs_checked: int = 0
    strat_pairs_skipped: int = 0
    strat_overlaps_found: int = 0
    strat_inclusions_found: int = 0
    strat_reductions: int = 0
    strat_time_ms: float = 0.0

    # Degree-bucketed reduction
    bucket_scan_saved: int = 0  # rules not scanned due to bucketing

    # Speedup
    pair_speedup: float = 0.0
    time_speedup: float = 0.0


def reduce_element(monomial: Tuple[int, ...],
                   rules: List[ReductionRule],
                   max_degree: Optional[int] = None) -> Tuple[int, int]:
    """Proxy reduction: rewrite a monomial using first RHS terms.

    This is NOT full polynomial reduction — it substitutes only
    the first RHS term of each matching rule.  Used for counting
    reduction steps and benchmarking pair-screening structure.

    Returns (reduction_steps, rules_scanned).
    If max_degree is set, only scan rules with degree ≤ max_degree."""
    steps = 0
    scanned = 0
    current = list(monomial)

    changed = True
    while changed:
        changed = False
        for rule in rules:
            if max_degree is not None and rule.degree > len(current):
                continue
            scanned += 1
            lm = list(rule.lm)
            # Check if lm appears as subword of current
            n, m = len(current), len(lm)
            for start in range(n - m + 1):
                if current[start:start + m] == lm:
                    # Replace with first RHS term (proxy reduction)
                    if rule.rhs:
                        _, replacement = rule.rhs[0]
                        current = current[:start] + list(replacement) + current[start + m:]
                    else:
                        current = current[:start] + current[start + m:]
                    steps += 1
                    changed = True
                    break
            if changed:
                break

    return steps, scanned


def naive_buchberger(rules: List[ReductionRule]) -> BenchmarkResult:
    """Run naive Buchberger: check ALL S-polynomial pairs (i < j)."""
    result = BenchmarkResult(n_gens=0, n_rules=len(rules))
    t0 = time.perf_counter()

    n = len(rules)
    for i in range(n):
        for j in range(i + 1, n):
            result.naive_pairs_checked += 1

            # Check overlaps in both directions
            for lm_a, lm_b in [(rules[i].lm, rules[j].lm),
                                (rules[j].lm, rules[i].lm)]:
                overlaps = find_overlaps(lm_a, lm_b)
                if overlaps:
                    result.naive_overlaps_found += len(overlaps)
                    for ov in overlaps:
                        ambient = lm_a + lm_b[len(ov):]
                        steps, _ = reduce_element(ambient, rules)
                        result.naive_reductions += steps

            # Check inclusions in both directions
            if has_inclusion(rules[i].lm, rules[j].lm):
                result.naive_inclusions_found += 1
                steps, _ = reduce_element(rules[j].lm, rules)
                result.naive_reductions += steps
            if has_inclusion(rules[j].lm, rules[i].lm):
                result.naive_inclusions_found += 1
                steps, _ = reduce_element(rules[i].lm, rules)
                result.naive_reductions += steps

    t1 = time.perf_counter()
    result.naive_time_ms = (t1 - t0) * 1000
    return result


# ══════════════════════════════════════════════════════════════
# §4  Jet-Stratified Verification
# ══════════════════════════════════════════════════════════════

def jet_stratified_buchberger(rules: List[ReductionRule],
                              n_desc: int) -> BenchmarkResult:
    """Run jet-stratified Buchberger: skip desc×desc pairs.

    rules[:n_desc] are descended, rules[n_desc:] are transient."""
    result = BenchmarkResult(n_gens=0, n_rules=len(rules))
    result.n_desc_rules = n_desc
    result.n_trans_rules = len(rules) - n_desc
    t0 = time.perf_counter()

    # Classify rules
    for i, r in enumerate(rules):
        r.rule_class = "descended" if i < n_desc else "transient"

    # Degree buckets for filtered reduction
    max_deg = max(r.degree for r in rules) if rules else 0
    buckets = {d: [] for d in range(max_deg + 1)}
    for r in rules:
        buckets[r.degree].append(r)

    # Pre-compute cumulative buckets: cumulative_buckets[d] = rules with degree ≤ d
    cumulative_buckets = {}
    current_rules = []
    for d in range(max_deg + 1):
        if d in buckets:
            current_rules = current_rules + buckets[d]
        cumulative_buckets[d] = current_rules

    n = len(rules)
    for i in range(n):
        for j in range(i + 1, n):
            both_desc = (i < n_desc and j < n_desc)

            if both_desc:
                result.strat_pairs_skipped += 1
                continue

            result.strat_pairs_checked += 1

            # Check overlaps in both directions, with degree-bucketed reduction
            for lm_a, lm_b in [(rules[i].lm, rules[j].lm),
                                (rules[j].lm, rules[i].lm)]:
                overlaps = find_overlaps(lm_a, lm_b)
                if overlaps:
                    result.strat_overlaps_found += len(overlaps)
                    for ov in overlaps:
                        ambient = lm_a + lm_b[len(ov):]
                        ambient_deg = min(len(ambient), max_deg)
                        bucket_rules = cumulative_buckets[ambient_deg]
                        result.bucket_scan_saved += len(rules) - len(bucket_rules)
                        steps, _ = reduce_element(ambient, bucket_rules,
                                                   max_degree=len(ambient))
                        result.strat_reductions += steps

            # Check inclusions in both directions
            if has_inclusion(rules[i].lm, rules[j].lm):
                result.strat_inclusions_found += 1
                steps, _ = reduce_element(rules[j].lm, rules,
                                          max_degree=len(rules[j].lm))
                result.strat_reductions += steps
            if has_inclusion(rules[j].lm, rules[i].lm):
                result.strat_inclusions_found += 1
                steps, _ = reduce_element(rules[i].lm, rules,
                                          max_degree=len(rules[i].lm))
                result.strat_reductions += steps

    t1 = time.perf_counter()
    result.strat_time_ms = (t1 - t0) * 1000
    return result


# ══════════════════════════════════════════════════════════════
# §5  Benchmark: Varying Jet Levels
# ══════════════════════════════════════════════════════════════

def run_benchmark(max_level: int = 12,
                  new_gens_per_level: int = 3) -> dict:
    """Run the full benchmark across jet levels 1..max_level.

    At each level, we simulate jet prolongation by adding
    new_gens_per_level generators to the Hecke algebra.
    The previous level's rules are "descended" and the new
    rules are "transient".
    """
    results = []

    # Level 0: base algebra H₄(q) (4 strands, 3 generators σ₀,σ₁,σ₂)
    base_gens = 3

    print(f"{'Level':>5} {'Gens':>5} {'Rules':>6} "
          f"{'Naive':>8} {'Strat':>8} {'Skip':>8} "
          f"{'T_naive':>10} {'T_strat':>10} {'Speedup':>8}")
    print("-" * 85)

    for level in range(1, max_level + 1):
        n_gens = base_gens + level * new_gens_per_level
        all_rules = hecke_rules(n_gens)

        # Descended = rules involving only generators < prev_n_gens
        prev_n_gens = base_gens + (level - 1) * new_gens_per_level
        desc_rules = [r for r in all_rules if all(g < prev_n_gens for g in r.lm)]
        trans_rules = [r for r in all_rules if not all(g < prev_n_gens for g in r.lm)]
        sorted_rules = desc_rules + trans_rules
        n_desc = len(desc_rules)

        # Run naive
        naive_result = naive_buchberger(sorted_rules)
        naive_result.n_gens = n_gens

        # Run jet-stratified
        strat_result = jet_stratified_buchberger(sorted_rules, n_desc)
        strat_result.n_gens = n_gens

        # Compute speedups
        pair_speedup = (naive_result.naive_pairs_checked /
                        max(strat_result.strat_pairs_checked, 1))
        time_speedup = (naive_result.naive_time_ms /
                        max(strat_result.strat_time_ms, 0.001))

        print(f"{level:>5} {n_gens:>5} {len(sorted_rules):>6} "
              f"{naive_result.naive_pairs_checked:>8} "
              f"{strat_result.strat_pairs_checked:>8} "
              f"{strat_result.strat_pairs_skipped:>8} "
              f"{naive_result.naive_time_ms:>9.2f}ms "
              f"{strat_result.strat_time_ms:>9.2f}ms "
              f"{time_speedup:>7.2f}x")

        results.append({
            "level": level,
            "n_gens": n_gens,
            "n_rules": len(sorted_rules),
            "n_desc_rules": n_desc,
            "n_trans_rules": len(trans_rules),
            "naive_pairs": naive_result.naive_pairs_checked,
            "naive_overlaps": naive_result.naive_overlaps_found,
            "naive_inclusions": naive_result.naive_inclusions_found,
            "naive_reductions": naive_result.naive_reductions,
            "naive_time_ms": round(naive_result.naive_time_ms, 3),
            "strat_pairs": strat_result.strat_pairs_checked,
            "strat_skipped": strat_result.strat_pairs_skipped,
            "strat_overlaps": strat_result.strat_overlaps_found,
            "strat_inclusions": strat_result.strat_inclusions_found,
            "strat_reductions": strat_result.strat_reductions,
            "strat_bucket_saved": strat_result.bucket_scan_saved,
            "strat_time_ms": round(strat_result.strat_time_ms, 3),
            "pair_speedup": round(pair_speedup, 2),
            "time_speedup": round(time_speedup, 2),
        })

    return {
        "algorithm": "jet-stratified-groebner-shirshov",
        "q": Q,
        "base_gens": base_gens,
        "new_gens_per_level": new_gens_per_level,
        "max_level": max_level,
        "results": results,
    }


# ══════════════════════════════════════════════════════════════
# §6  Main
# ══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 85)
    print("Jet-Stratified Gröbner–Shirshov Benchmark")
    print("Hecke algebra H_n(q), q = {:.4f}".format(Q))
    print("Base: H₄(q) (4 strands, 3 generators), +3 generators per jet level")
    print("=" * 85)
    print()

    witness = run_benchmark(max_level=12, new_gens_per_level=3)

    print()
    print("=" * 85)
    print("Summary:")
    print("=" * 85)

    if witness["results"]:
        first = witness["results"][0]
        last = witness["results"][-1]
        print(f"  Level 1:  {first['naive_pairs']:>6} naive pairs → "
              f"{first['strat_pairs']:>6} stratified "
              f"({first['pair_speedup']:.1f}x pair reduction)")
        print(f"  Level {last['level']:>2}: {last['naive_pairs']:>6} naive pairs → "
              f"{last['strat_pairs']:>6} stratified "
              f"({last['pair_speedup']:.1f}x pair reduction)")
        print(f"  Time speedup at level {last['level']}: "
              f"{last['time_speedup']:.1f}x")

    # Write witness
    witness_path = "jet-stratified-benchmark.witness.json"
    with open(witness_path, "w") as f:
        json.dump(witness, f, indent=2)
    print(f"\nWitness written to {witness_path}")
