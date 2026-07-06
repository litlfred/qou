"""qbeta_chain4_mixed_wenzl_kashaev_kashiwara — Chain 4 mixed chains.

The only genuinely-unprobed legitimate direction in the residue-A
categorical-ID search (1ppQ ledger cont. 5): MIXED CHAINS. Products
combining

  - a WENZL invariant  W_λ   (Hecke / Markov-trace per-λ-block value),
  - a KASHAEV evaluation K_λ  (quantum-dilogarithm at z_λ), and
  - a KASHIWARA invariant      (partition / crystal statistic n(λ)).

Every single-chain family is TIERED-NEGATIVE (PR #1772 n≤4, PR #1787
n=5 + Demazure, residue-A probe 38 candidates). Mixed products are the
remaining structural direction.

TARGET (carried verbatim):
  Residue A = 1.804e-15 (PR #1727; simple pole, fibre-level, anchor-
  independent). ℏ_q = (q − 1)/q (NEVER hard-coded). Target prefactor
  A / ℏ_q^15 ≈ 2.072 at proton anchor.

COMPONENT LAYERS
----------------
Wenzl (per-λ-block, closed-form hook specialisation — native hecke-
engine is not built in this sandbox; the hook formula is the canonical
closed form, cross-checked by Σ_λ (f^λ)² = n! and the q→1 limit):
  f^λ        = n! / ∏ hook(c)                      (SYT count; Wenzl rank)
  qdim(λ)    = q^{n(λ)} · [n]_q! / ∏ [hook(c)]_q   (fake degree; graded
               q-dimension of the λ-isotypic block — the natural Wenzl-
               trace q-value)
  W_markov   = z^{n-1} · qdim(λ)                    (Markov-normalised,
               z = 1/(√q + 1/√q) the residue-probe Markov parameter)

Kashaev (real-q fibre; Faddeev non-compact Φ_b needs |q|=1 so does NOT
apply at q₀≈1.11 — use Rogers q-dilog + q-Pochhammer with base
p = q^{-1} < 1):
  Li2q(x)    = Σ_{m≥1} x^m / (m·(1 − q^{-m}))       (|x|<1)
  qPoch(x)   = ∏_{m≥0} (1 − x q^{-m})               (converges, p<1)
  Phi_q(x)   = 1 / qPoch(x)                          (quantum dilog form)
evaluated at z_λ = q^{−n(λ)} ∈ (0,1] (Kashiwara lowest-weight arg) and
at x = ℏ_q.

Mixed candidate = W_λ · K_λ, plus ratios W_λ / K_λ, conjugate-pair
products W_λ · W_{λ'}, and ℏ_q-normalised forms.

ANTI-PATTERN GUARDS (AGENTS.md):
  - TIERED reporting; NO ansatz at NEAR-FUZZY or coarser.
  - Cross-anchor BEFORE structural claim (proton + muon targets emitted).
  - ℏ_q from (q − 1)/q, never hard-coded.
  - Diagnostic-only; no production wiring.

Usage:
  python3 computations/qbeta/qbeta_chain4_mixed_wenzl_kashaev_kashiwara.py
Emits: qbeta-chain4-mixed-wenzl-kashaev-kashiwara.witness.json
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 50

RESIDUE_A = mp.mpf("1.804e-15")
Q_PROTON_50 = mp.mpf("1.10997858275138080759166909561")
Q_MUON_50 = mp.mpf("1.1099785955541805752815940796095093779932822799587")

# Kashaev series truncation (p = q^-1 ≈ 0.90; p^120 ≈ 4e-6, p^200 ≈ 8e-10).
KASHAEV_TRUNC = 400


# ───────────────────────── q-arithmetic ──────────────────────────────
def h_q(q: mp.mpf) -> mp.mpf:
    """ℏ_q = (q − 1) / q (predecessor honest correction; NEVER hard-coded)."""
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


# ───────────────────────── partitions ────────────────────────────────
def partitions_of(n: int) -> list[tuple[int, ...]]:
    """All partitions of n as weakly-decreasing tuples."""
    if n == 0:
        return [()]
    out: list[tuple[int, ...]] = []

    def rec(remaining: int, max_part: int, prefix: tuple[int, ...]) -> None:
        if remaining == 0:
            out.append(prefix)
            return
        for part in range(min(remaining, max_part), 0, -1):
            rec(remaining - part, part, prefix + (part,))

    rec(n, n, ())
    return out


def conjugate(lam: tuple[int, ...]) -> tuple[int, ...]:
    """Transpose / conjugate partition λ'."""
    if not lam:
        return ()
    return tuple(sum(1 for p in lam if p > j) for j in range(lam[0]))


def n_statistic(lam: tuple[int, ...]) -> int:
    """n(λ) = Σ_i (i−1)·λ_i  (rows 1-indexed)."""
    return sum(i * part for i, part in enumerate(lam))


def hook_lengths(lam: tuple[int, ...]) -> list[int]:
    """All hook lengths of the Young diagram of λ."""
    conj = conjugate(lam)
    hooks: list[int] = []
    for i, row in enumerate(lam):
        for j in range(row):
            arm = row - (j + 1)
            leg = conj[j] - (i + 1)
            hooks.append(arm + leg + 1)
    return hooks


def num_syt(lam: tuple[int, ...]) -> int:
    """f^λ = n! / ∏ hook(c) (number of standard Young tableaux)."""
    n = sum(lam)
    num = mp.factorial(n)
    den = mp.mpf(1)
    for h in hook_lengths(lam):
        den *= h
    return int(mp.nint(num / den))


def q_dim_fake_degree(lam: tuple[int, ...], q: mp.mpf) -> mp.mpf:
    """qdim(λ) = q^{n(λ)} · [n]_q! / ∏ [hook(c)]_q  (graded q-dim / fake degree)."""
    n = sum(lam)
    num = q ** n_statistic(lam) * q_factorial(n, q)
    den = mp.mpf(1)
    for h in hook_lengths(lam):
        den *= q_integer(h, q)
    return num / den


# ───────────────────────── Kashaev layer ─────────────────────────────
def rogers_dilog(x: mp.mpf, q: mp.mpf, trunc: int = KASHAEV_TRUNC) -> mp.mpf:
    """Rogers q-dilogarithm Li_2^q(x) = Σ_{m≥1} x^m / (m (1 − q^{−m})).

    Base q^{-1} < 1 for q > 1, so 1 − q^{-m} ∈ (0, 1). Converges for
    |x| < 1; x = q^{−n(λ)} ∈ (0, 1] is in range.
    """
    s = mp.mpf(0)
    xm = mp.mpf(1)
    for m in range(1, trunc + 1):
        xm *= x
        denom = m * (1 - q ** (-m))
        if denom == 0:
            continue
        s += xm / denom
    return s


def qpoch_inf(x: mp.mpf, q: mp.mpf, trunc: int = KASHAEV_TRUNC) -> mp.mpf:
    """(x; q^{-1})_∞ = ∏_{m≥0} (1 − x q^{−m}). Converges (p = q^{-1} < 1)."""
    p = mp.mpf(1)
    for m in range(0, trunc + 1):
        p *= (1 - x * q ** (-m))
    return p


# ───────────────────────── candidate build ───────────────────────────
def wenzl_invariants(lam: tuple[int, ...], q: mp.mpf, z: mp.mpf) -> dict[str, mp.mpf]:
    """The three Wenzl per-block values for λ."""
    n = sum(lam)
    qd = q_dim_fake_degree(lam, q)
    return {
        "f": mp.mpf(num_syt(lam)),
        "qdim": qd,
        "wmarkov": z ** (n - 1) * qd,
    }


def kashaev_evals(lam: tuple[int, ...], q: mp.mpf, hbar: mp.mpf) -> dict[str, mp.mpf]:
    """Kashaev quantum-dilog evaluations at z_λ = q^{−(n(λ)+1)} and at ℏ_q.

    The +1 is a ρ-shift ensuring z_λ ∈ (0, 1) strictly — the un-shifted
    q^{−n(λ)} hits z_λ = 1 for the single-row partition (n(λ)=0), which
    is the quantum-dilog pole (Poch factor (1−x)=0; Li_2^q harmonic
    divergence). The ρ-shifted lowest-weight argument is the standard
    crystal evaluation point.
    """
    z_lam = q ** (-(n_statistic(lam) + 1))    # ∈ (0, 1) strictly
    out = {
        "Li2q_zlam": rogers_dilog(z_lam, q),
        "Phi_zlam": 1 / qpoch_inf(z_lam, q),
        "Poch_zlam": qpoch_inf(z_lam, q),
    }
    # ℏ_q-argument variants (independent of λ shape but paired per block)
    out["Li2q_hbar"] = rogers_dilog(hbar, q)
    out["Phi_hbar"] = 1 / qpoch_inf(hbar, q)
    return out


def build_candidates(q: mp.mpf, hbar: mp.mpf) -> dict[str, mp.mpf]:
    """Mixed Wenzl × Kashaev × Kashiwara candidates for n ∈ {3, 4, 5}."""
    z = 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))   # Markov parameter (residue probe)
    cands: dict[str, mp.mpf] = {}
    for n in (3, 4, 5):
        parts = partitions_of(n)
        wvals = {lam: wenzl_invariants(lam, q, z) for lam in parts}
        kvals = {lam: kashaev_evals(lam, q, hbar) for lam in parts}
        for lam in parts:
            lam_s = "".join(str(p) for p in lam)
            W = wvals[lam]
            K = kvals[lam]
            # Mixed products W_λ · K_λ and ratios W_λ / K_λ
            for wk, wv in W.items():
                for kk, kv in K.items():
                    base = f"n{n}_{lam_s}"
                    cands[f"{base}:{wk}·{kk}"] = wv * kv
                    if kv != 0:
                        cands[f"{base}:{wk}/{kk}"] = wv / kv
            # Conjugate-pair Wenzl products (Kashiwara bar-symmetry)
            lam_c = conjugate(lam)
            Wc = wvals[lam_c]
            cands[f"n{n}_{lam_s}:qdim·qdimT"] = W["qdim"] * Wc["qdim"]
            cands[f"n{n}_{lam_s}:f·qdimT_K"] = (
                W["f"] * Wc["qdim"] * K["Phi_zlam"]
            )
    return cands


# ───────────────────────── reporting ─────────────────────────────────
def report_proximity(cands: dict[str, mp.mpf], target: mp.mpf) -> dict[str, dict]:
    """TIERED proximity report (matches PR #1787 thresholds)."""
    out: dict[str, dict] = {}
    for name, val in cands.items():
        if not mp.isfinite(val) or val == 0:
            out[name] = {"value": "0/inf", "value_num": mp.mpf(0),
                         "ratio": "0", "ratio_num": mp.mpf("1e99"), "tier": "ZERO"}
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
        out[name] = {"value": mp.nstr(val, 7), "value_num": val,
                     "ratio": mp.nstr(ratio, 7), "ratio_num": ratio, "tier": tier}
    return out


def witness_safe(r: dict) -> dict:
    """Strip mp.mpf-valued `_num` keys; keep display strings for JSON."""
    return {k: v for k, v in r.items() if not k.endswith("_num")}


# ───────────────────────── cross-checks ──────────────────────────────
def self_check() -> None:
    """Sanity cross-checks before the probe (fail loudly)."""
    # Σ_λ (f^λ)² = n!
    for n in (3, 4, 5):
        s = sum(num_syt(lam) ** 2 for lam in partitions_of(n))
        assert s == mp.factorial(n), f"Σ(f^λ)² ≠ {n}! for n={n}: {s}"
    # q→1 limit of qdim = f^λ
    q1 = mp.mpf(1) + mp.mpf("1e-30")
    for lam in partitions_of(4):
        qd = q_dim_fake_degree(lam, q1)
        assert abs(qd - num_syt(lam)) < mp.mpf("1e-6"), \
            f"qdim(λ={lam}) → f^λ failed: {qd} vs {num_syt(lam)}"


def run_anchor(q: mp.mpf, label: str) -> tuple[dict, mp.mpf]:
    hbar = h_q(q)
    target = RESIDUE_A / (hbar ** 15)
    cands = build_candidates(q, hbar)
    results = report_proximity(cands, target)
    return results, target


def main() -> int:
    print("=" * 78)
    print("Q_β Chain 4 — Mixed chains: Wenzl × Kashaev × Kashiwara")
    print("=" * 78)
    self_check()
    print("✓ self-checks passed (Σ(f^λ)²=n!, qdim→f^λ at q→1)")
    print()

    hbar_p = h_q(Q_PROTON_50)
    target_p = RESIDUE_A / (hbar_p ** 15)
    hbar_m = h_q(Q_MUON_50)
    target_m = RESIDUE_A / (hbar_m ** 15)
    print(f"ℏ_q (proton, computed) = {mp.nstr(hbar_p, 8)}")
    print(f"Target prefactor (proton): A / ℏ_q^15 = {mp.nstr(target_p, 8)}")
    print(f"Target prefactor (muon):   A / ℏ_q^15 = {mp.nstr(target_m, 8)}")
    print()

    results_p, _ = run_anchor(Q_PROTON_50, "proton")
    print(f"Mixed candidates enumerated: {len(results_p)}")
    print()

    tier_order = {"NEAR-1PPM": 0, "NEAR-0.1PCT": 1, "NEAR-1PCT": 2,
                  "NEAR-FUZZY": 3, "NEAR-CLOSE": 4, "MISS": 5, "ZERO": 6}
    sorted_items = sorted(
        results_p.items(),
        key=lambda kv: (tier_order.get(kv[1]["tier"], 99),
                        abs(kv[1]["ratio_num"] - 1)),
    )

    print(f"  {'Candidate':44s} {'value':13s} {'ratio':11s} tier")
    for name, r in sorted_items[:20]:
        print(f"  {name:44s} {r['value']:13s} {r['ratio']:11s} {r['tier']}")
    print()

    best_name, best = sorted_items[0]
    print(f"BEST (proton): {best_name} → {best['tier']} (ratio {best['ratio']})")
    print()

    # Tier histogram
    hist: dict[str, int] = {}
    for r in results_p.values():
        hist[r["tier"]] = hist.get(r["tier"], 0) + 1
    print("Tier histogram (proton):")
    for t in ["NEAR-1PPM", "NEAR-0.1PCT", "NEAR-1PCT", "NEAR-FUZZY",
              "NEAR-CLOSE", "MISS", "ZERO"]:
        if hist.get(t):
            print(f"  {t:12s}: {hist[t]}")
    print()

    # A candidate is a GENUINE mixed q-product only if its Wenzl factor
    # is q-DEPENDENT (qdim / wmarkov). Candidates whose Wenzl factor is
    # f^λ (a q-independent integer block-dimension) are "single-chain
    # Kashaev × integer" — the q-structure lives entirely in the
    # Kashaev factor, so they do NOT test the mixed-chain hypothesis.
    def is_genuine_mixed(name: str) -> bool:
        spec = name.split(":", 1)[1] if ":" in name else name
        # genuine iff the Wenzl operand (left of ·// op) is q-dependent
        wenzl_token = spec.replace("/", "·").split("·")[0]
        return wenzl_token in ("qdim", "wmarkov")

    # Cross-anchor: any proton NEAR-1PCT-or-better gets muon check.
    near = [(name, r) for name, r in results_p.items()
            if r["tier"] in ("NEAR-1PPM", "NEAR-0.1PCT", "NEAR-1PCT")]
    near_genuine = [(n, r) for n, r in near if is_genuine_mixed(n)]
    cross_anchor: dict[str, dict] = {}
    if near:
        print(f"⚠ {len(near)} NEAR-1PCT-or-better at proton "
              f"({len(near_genuine)} GENUINE q-mixed) — cross-anchoring:")
        results_m, _ = run_anchor(Q_MUON_50, "muon")
        for name, r in near:
            rm = results_m.get(name, {})
            swing = "n/a"
            if rm and rm.get("ratio_num"):
                swing = mp.nstr(abs(r["ratio_num"] / rm["ratio_num"] - 1) * 100, 5)
            cross_anchor[name] = {
                "proton_ratio": r["ratio"], "proton_tier": r["tier"],
                "muon_ratio": rm.get("ratio", "?"), "muon_tier": rm.get("tier", "?"),
                "cross_anchor_swing_pct": swing,
                "genuine_q_mixed": is_genuine_mixed(name),
            }
            tag = "GENUINE-MIXED" if is_genuine_mixed(name) else "Kashaev×int"
            print(f"  {name} [{tag}]: proton {r['ratio']} ({r['tier']}) | "
                  f"muon {rm.get('ratio','?')} ({rm.get('tier','?')}) | "
                  f"swing {swing}%")
        print()
        print("  ⚑ METHOD NOTE: the two q₀ anchors differ by only ~1e-7, so")
        print("    cross-anchor swing is near-vacuous for ANY closed-form")
        print("    candidate (≠ the c_3 FITTED-coefficient swing test). The")
        print("    real discriminators here are (a) the proximity tier and")
        print("    (b) whether the Wenzl factor is q-dependent (genuine mixed).")
    else:
        print("VERDICT: NO mixed candidate reaches NEAR-1PCT at proton anchor.")
    print()

    print(f"GENUINE q-mixed products reaching NEAR-1PCT: {len(near_genuine)}")
    if not near_genuine:
        # Best genuine candidate (for the record)
        gen_sorted = [(n, r) for n, r in sorted_items if is_genuine_mixed(n)]
        if gen_sorted:
            gn, gr = gen_sorted[0]
            print(f"  Best GENUINE q-mixed: {gn} → {gr['tier']} (ratio {gr['ratio']})")
    print()

    # ─── Witness ──────────────────────────────────────────────────────
    w = WitnessBuilder("qbeta-chain4-mixed-wenzl-kashaev-kashiwara", engine="mpmath")
    w.set_description(
        f"Chain 4 mixed chains — products of a Wenzl per-λ-block invariant "
        f"(f^λ, fake-degree qdim, Markov-normalised z^{{n-1}}·qdim via closed-"
        f"form hook specialisation), a Kashaev quantum-dilog evaluation "
        f"(Rogers Li_2^q, q-Pochhammer / Phi_q at z_λ=q^{{-n(λ)}} and ℏ_q, "
        f"base q^{{-1}}<1 since Faddeev Φ_b needs |q|=1), and a Kashiwara "
        f"statistic n(λ), for λ ⊢ n, n ∈ {{3,4,5}}. Target prefactor "
        f"A/ℏ_q^15 ≈ {mp.nstr(target_p, 6)} (proton). {len(results_p)} "
        f"candidates. Best: {best_name} → {best['tier']} (ratio {best['ratio']}). "
        f"TIERED; cross-anchor emitted; ℏ_q=(q-1)/q; diagnostic-only, no "
        f"production wiring."
    )
    w.add_data("residue_target_A", str(RESIDUE_A))
    w.add_data("prefactor_target_proton", str(target_p))
    w.add_data("prefactor_target_muon", str(target_m))
    w.add_data("h_q_proton", str(hbar_p))
    w.add_data("h_q_muon", str(hbar_m))
    w.add_data("q_proton", str(Q_PROTON_50))
    w.add_data("q_muon", str(Q_MUON_50))
    w.add_data("candidate_count", str(len(results_p)))
    w.add_data("tier_histogram", {k: str(v) for k, v in hist.items()})
    w.add_data("top10", {name: witness_safe(r) for name, r in sorted_items[:10]})
    w.add_data("best_match", {"candidate": best_name, "tier": best["tier"],
                              "ratio": best["ratio"]})
    w.add_data("near_1pct_count", str(len(near)))
    w.add_data("near_1pct_genuine_qmixed_count", str(len(near_genuine)))
    if cross_anchor:
        w.add_data("cross_anchor", cross_anchor)
    w.add_data("kashaev_truncation", str(KASHAEV_TRUNC))
    w.add_data("note_native_engine",
               "hecke-engine not built in sandbox; Wenzl values via closed-form "
               "hook specialisation, cross-checked Σ(f^λ)²=n! and qdim→f^λ at q→1.")
    w.add_data(
        "note_cross_anchor_vacuous",
        "The proton/muon q₀ anchors differ by ~1e-7, so cross-anchor swing "
        "is near-zero for ANY closed-form candidate (unlike the c_3 FITTED-"
        "coefficient swing test). Discriminators here: proximity tier + "
        "Wenzl-factor q-dependence (genuine mixed vs Kashaev×integer).",
    )
    w.add_data(
        "note_best_near_match_is_kashaev_x_integer",
        "The proton best (f·Li2q_hbar, ratio≈0.9918, NEAR-1PCT) is "
        "2·Li_2^q(ℏ_q): Wenzl factor f^λ=2 is a q-INDEPENDENT integer "
        "block-dimension, so all q-structure is the single-chain Kashaev "
        "Rogers-dilog. It is NOT a genuine mixed q-product, and at 0.82% off "
        "it is a NEAR-1PCT artifact (cf. the 1+q q-binomial artifact of "
        "PR #1787), not a closure.",
    )
    w.add_assertion(
        name="self_checks_passed",
        computed=True, expected=True,
        source="Σ_λ(f^λ)²=n! for n∈{3,4,5}; qdim(λ)→f^λ as q→1.",
    )
    # Substantive negative: no GENUINE q-mixed product (q-dependent Wenzl
    # factor × Kashaev) reaches NEAR-1PCT. f^λ×Kashaev hits do not count —
    # their Wenzl factor is a q-independent integer.
    w.add_assertion(
        name="genuine_mixed_chain_id_found",
        computed=bool(len(near_genuine) > 0),
        expected=False, tolerance=0,
        source="A genuine mixed-chain categorical ID requires a q-DEPENDENT "
               "Wenzl factor (qdim/wmarkov) × Kashaev product reaching "
               "NEAR-1PCT. Default expectation: none (single-chain families "
               "all NEGATIVE). The f^λ×Li2q NEAR-1PCT hits are Kashaev×integer, "
               "excluded by construction.",
    )
    out = w.save()
    print(f"  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
