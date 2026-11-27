#!/usr/bin/env python3
"""binding_three_body_perms_probe.py — three-nucleon γγ bond words that are not pair products.

Bean `qou-brng` (brief C2, front A, epic `qou-myts`). Open item 3 of
`docs/audits/2026-11-27-classical-log-binding-cycle-count.md`: classify the nine-strand (A = 3) γγ
bond words whose permutation is NOT a product of pair-bond permutations, and measure their merges
at q0 against 3·m(²H) and against the classical b3.

Setting. Free word x = V^3 on each nucleon (strands 0-2, 3-5, 6-8), V(s) = σ_s σ_{s+1}^{-1} (the
chiral vertex of the ruled photon). Bond word K = V(s1)...V(sL), s in 0..6, bonding both junctions
(contains V1 or V2, and V4 or V5). Letters by support: V0 inside nucleon 1, V3 inside nucleon 2,
V6 inside nucleon 3; V1, V2 on pair (12); V4, V5 on pair (23). No vertex spans nucleons 1 and 3.

Two classifications, both exact (integer permutation data):
  * WORD level (the hypothesis of `classicalB3_nonpos_of_product`): pi(K) equals the product, in
    either order, of the permutation of its pair-(12) letters and of its pair-(23) letters, for
    some placement of each V3 letter on one side. A word failing this is "word-level non-product".
  * GROUP level (intrinsic): pi(K) lies in Sym{0..5}·Sym{3..8} ∪ Sym{3..8}·Sym{0..5} (141048 of
    9! = 362880 permutations). A word failing this is "intrinsically three-body": no choice of
    pair words reproduces it with two factors.

Classical connected term, by inclusion-exclusion over the letters supported in each nucleon set S
(K|S = subsequence of letters whose three strands lie in S):
    b3 = B(K) - B(K|12) - B(K|23) - B(K|13) + B(K|1) + B(K|2) + B(K|3).
At q = 1 each B is E0 ln2 times a merge count (ClassicalLogBindingCycleCount.classicalLogBinding_eq);
for V3-free words this is exactly the Lean `classicalB3` (B(K|13) = B(K|1) + B(K|3)). The same
combination is evaluated at q0 with B = -E0 ln r, r = tr(x+K')/tr(x).

Reading 3 (corpus seminormal helpers ../h2_one_rule, ../h2_gg_atom: convention D, proton pin,
40 dps) is evaluated on every word; it selects, the ratio is reported. Classical reading 3 (q = 1,
every level, Young's rule) is evaluated exactly. AME is not read. Nothing fitted, selected against
data, or wired. mpmath throughout; no float arithmetic.

Population: all bond words of length 1..4 (1360) and, at length 5, every word-level non-product
word plus every word with nonzero classical b3.

-- Ref: [leitner2026] bean qou-brng; QOU.MassTheory.ClassicalLogBindingCycleCount
"""
from __future__ import annotations

import itertools
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "binding_ceiling_q0"))
_argv, sys.argv = sys.argv, [sys.argv[0], "4", "3"]      # the ceiling probe reads (L, A) at import
import binding_ceiling_q0_probe as bc  # noqa: E402
sys.argv = _argv

mp = bc.mp
ONE, ZERO, TOL = bc.ONE, bc.ZERO, bc.TOL
Q = bc.Q
from qou_substrate.witness import WitnessBuilder  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402

N = 9
assert bc.N == N
L5 = int(_argv[1]) if len(_argv) > 1 else 5
JUNCTIONS = [{1, 2}, {4, 5}]
LN2 = mp.log(2)
SUPPORT = {"12": {0, 1, 2, 3}, "23": {3, 4, 5, 6}, "13": {0, 6}, "1": {0}, "2": {3}, "3": {6}}
MOBIUS = {"12": -1, "23": -1, "13": -1, "1": 1, "2": 1, "3": 1}


def V(s):
    return bc.V(s)


def perm_of(K):
    return tuple(bc.perm([lt for s in K for lt in V(s)]))


def merges(K):
    return N - bc.n_cycles(list(perm_of(K)))


def comp(a, b):
    """perm of word1+word2 = comp(perm(word1), perm(word2)) (bc.perm acts on positions)."""
    return tuple(a[b[i]] for i in range(N))


def cycles(p):
    seen, out = set(), []
    for i in range(len(p)):
        if i not in seen:
            c, j = [], i
            while j not in seen:
                seen.add(j)
                c.append(j)
                j = p[j]
            out.append(c)
    return out


def _subset_count(lens, k):
    dp = [1] + [0] * k
    for ln in lens:
        for t in range(k, ln - 1, -1):
            dp[t] += dp[t - ln]
    return dp[k]


def classical_reading3(p):
    """q = 1: E_{n->m} sends a permutation to a positive multiple of its restriction to {0..m-1};
    two-row characters chi_(m-k,k) = a_k - a_{k-1}, a_k = invariant k-subsets (Young's rule)."""
    for m in range(1, N + 1):
        lens = [len(c2) for c2 in ([x for x in c if x < m] for c in cycles(p)) if c2]
        a = [_subset_count(lens, k) for k in range(m // 2 + 1)]
        if any(a[k] < a[k - 1] for k in range(1, len(a))):
            return False
    return True


def sym_on(S):
    S = sorted(S)
    out = set()
    for img in itertools.permutations(S):
        p = list(range(N))
        for a, b in zip(S, img):
            p[a] = b
        out.add(tuple(p))
    return out


S12, S23 = sym_on(range(6)), sym_on(range(3, 9))
PAIR_GROUP_PRODUCTS = {comp(a, b) for a in S12 for b in S23} | {comp(b, a) for a in S12 for b in S23}


def word_level_product(K):
    p = perm_of(K)
    idx3 = [i for i, s in enumerate(K) if s == 3]
    for bits in itertools.product((0, 1), repeat=len(idx3)):
        side = dict(zip(idx3, bits))
        k12 = tuple(s for i, s in enumerate(K) if s in (0, 1, 2) or (s == 3 and side[i] == 0))
        k23 = tuple(s for i, s in enumerate(K) if s in (4, 5, 6) or (s == 3 and side[i] == 1))
        p12, p23 = perm_of(k12), perm_of(k23)
        if p == comp(p12, p23) or p == comp(p23, p12):
            return True
    return False


def restrict(K, S):
    return tuple(s for s in K if s in S)


def classical_b3(K):
    return merges(K) + sum(c * merges(restrict(K, SUPPORT[k])) for k, c in MOBIUS.items())


def main() -> int:
    m_e = mp.mpf(str(M_E_MEV))
    hbar = 1 - 1 / Q
    E0_tower = m_e / (Q * (Q - 1) * (1 - hbar ** 2))
    checks = []

    def check(name, ok, src):
        checks.append((name, bool(ok), src))
        print(f"[{'PASS' if ok else 'FAIL'}] {name} -- {src}", flush=True)

    x = [(s + 3 * a, i) for a in range(3) for (s, i) in V(0) * 3]
    trx, okx = bc.corpus_trace_and_pass(x)
    check("K0_free_word_passes_and_traces_agree", okx and abs(trx - bc.sw_trace(x)) < TOL,
          "corpus seminormal trace vs independent Schur-Weyl trace on (C^2)^9")

    def bonds(n):
        return [w for w in itertools.product(range(N - 2), repeat=n) if all(J & set(w) for J in JUNCTIONS)]

    words = [w for n in range(1, 5) for w in bonds(n)]
    n_short = len(words)
    extra = [w for w in bonds(L5) if not word_level_product(w) or classical_b3(w) != 0] if L5 >= 5 else []
    words += extra
    print(f"{n_short} words of length <= 4, {len(extra)} of length {L5}", flush=True)

    # exact classification
    cls = {}
    for w in words:
        p = perm_of(w)
        cls[w] = {"merges": merges(w), "word_level_product": word_level_product(w),
                  "intrinsic_three_body": p not in PAIR_GROUP_PRODUCTS,
                  "classical_b3_merge_units": classical_b3(w), "classical_reading3": classical_reading3(p),
                  "v3_free": 3 not in w}
    short = [cls[w] for w in words[:n_short]]
    n_cl2 = sum(c["classical_reading3"] and c["merges"] == 2 for c in short)
    n_cl4 = sum(c["classical_reading3"] and c["merges"] == 4 for c in short)
    check("K2_classical_reading3_reproduces_ceiling_audit_27_and_120", (n_short, n_cl2, n_cl4) == (1360, 27, 120),
          f"docs/audits/2026-11-27-binding-ceiling-at-q0.md §2: ({n_short}, {n_cl2}, {n_cl4})")
    bad = [w for w in words if cls[w]["v3_free"] and cls[w]["word_level_product"]
           and cls[w]["classical_b3_merge_units"] > 0]
    check("K3_lean_classicalB3_nonpos_of_product_holds_on_V3_free_products", not bad,
          f"{len(bad)} V3-free word-level products with classical b3 > 0")
    check("K4_intrinsic_three_body_implies_word_level_non_product",
          all(not c["word_level_product"] for c in cls.values() if c["intrinsic_three_body"]),
          "group-level membership is necessary for a word-level product")

    # q0: reading 3 and trace on every word and on every restriction
    cache = {}

    def tr_ok(K):
        if K not in cache:
            cache[K] = bc.corpus_trace_and_pass(x + [lt for s in K for lt in V(s)])
        return cache[K]

    def mlnr(K):
        t, _ = tr_ok(K)
        r = t / trx
        return -mp.log(r) if r > 0 else None

    t0, step = time.time(), max(1, len(words) // 25)
    rows, max_dev = [], ZERO
    for k, w in enumerate(words, 1):
        t, ok = tr_ok(w)
        rec = dict(cls[w])
        rec.update({"word": "".join(f"V{s}" for s in w), "length": len(w), "pass_q0": ok})
        parts = {key: mlnr(restrict(w, S)) for key, S in SUPPORT.items()}
        full = mlnr(w)
        rec["minus_ln_r"] = full
        if full is not None and all(v is not None for v in parts.values()):
            rec["b3_q0_merge_units"] = (full + sum(MOBIUS[key] * parts[key] for key in SUPPORT)) / LN2
        else:
            rec["b3_q0_merge_units"] = None
        rec["pairs_minus_ln_r"] = {key: parts[key] for key in ("12", "23")}
        if ok:
            max_dev = max(max_dev, abs(t - bc.sw_trace(x + [lt for s in w for lt in V(s)])))
        rows.append(rec)
        if k % step == 0:
            el = time.time() - t0
            print(f"  {k}/{len(words)} elapsed {el:.0f}s ETA {el / k * (len(words) - k):.0f}s", flush=True)

    check("K1_independent_trace_agrees_on_every_q0_passing_word", max_dev < TOL,
          f"max |seminormal - Schur-Weyl| = {mp.nstr(max_dev, 5)}")

    # tables
    def key(r):
        return (r["length"] <= 4, r["word_level_product"], r["intrinsic_three_body"], r["merges"],
                r["classical_b3_merge_units"])

    table = {}
    for r in rows:
        g = table.setdefault(key(r), {"n": 0, "n_pass_q0": 0, "n_pass_classical": 0, "q0": [], "b3": []})
        g["n"] += 1
        g["n_pass_classical"] += r["classical_reading3"]
        if r["pass_q0"]:
            g["n_pass_q0"] += 1
            g["q0"].append(r["minus_ln_r"])
            if r["b3_q0_merge_units"] is not None:
                g["b3"].append(r["b3_q0_merge_units"])
    summary = []
    for kk in sorted(table, key=lambda t: (not t[0], t[1], t[2], t[3], t[4])):
        g = table[kk]
        row = {"population": "len<=4" if kk[0] else f"len={L5}", "word_level_product": kk[1],
               "intrinsic_three_body": kk[2], "merges": kk[3], "classical_b3_merge_units": kk[4],
               "n": g["n"], "n_pass_q0": g["n_pass_q0"], "n_pass_classical": g["n_pass_classical"],
               "q0_merge_units_range": [mp.nstr(min(g["q0"]) / LN2, 6), mp.nstr(max(g["q0"]) / LN2, 6)] if g["q0"] else None,
               "b3_q0_merge_units_range": [mp.nstr(min(g["b3"]), 6), mp.nstr(max(g["b3"]), 6)] if g["b3"] else None}
        summary.append(row)
        print(row, flush=True)

    passing = [r for r in rows if r["pass_q0"]]
    check("K5_all_q0_passing_ratios_positive", all(r["minus_ln_r"] is not None for r in passing), "log law defined")
    nonprod_pass = [r for r in passing if not r["word_level_product"]]
    pos_b3_pass = [r for r in passing if r["b3_q0_merge_units"] is not None and r["b3_q0_merge_units"] > 0]
    pos_b3cl_pass = [r for r in passing if r["classical_b3_merge_units"] > 0]
    max_m_pass = max((r["merges"] for r in passing), default=None)
    print(f"q0-passing: {len(passing)}; non-product {len(nonprod_pass)}; intrinsic "
          f"{sum(r['intrinsic_three_body'] for r in passing)}; max merges {max_m_pass} (3*m(2H) = 6); "
          f"b3_q0 > 0: {len(pos_b3_pass)}; classical b3 > 0: {len(pos_b3cl_pass)}", flush=True)

    def ser(r):
        o = dict(r)
        o["minus_ln_r"] = mp.nstr(r["minus_ln_r"], 25) if r["minus_ln_r"] is not None else None
        o["b3_q0_merge_units"] = mp.nstr(r["b3_q0_merge_units"], 20) if r["b3_q0_merge_units"] is not None else None
        o["pairs_minus_ln_r"] = {k: (mp.nstr(v, 20) if v is not None else None) for k, v in r["pairs_minus_ln_r"].items()}
        return o

    wb = (WitnessBuilder("binding-three-body-perms", engine="mpmath")
          .set_description(
              "PROBE (bean qou-brng, brief C2 front A): nine-strand A=3 gamma-gamma bond words "
              "classified by whether their permutation is a product of pair-bond permutations (word "
              "level, the hypothesis of classicalB3_nonpos_of_product; and group level, "
              "Sym{0..5}Sym{3..8}), with merges, classical b3 and the q0 b3 by inclusion-exclusion. "
              "Reading 3 selects (corpus seminormal helpers); ratio reported, never used to select. "
              "AME not read. Nothing fitted or wired.")
          .set_audit_only("docs/audits/2026-11-27-binding-three-body-perms.md")
          .add_parameter("A", 3).add_parameter("n_strands", N).add_parameter("extra_length", L5)
          .add_parameter("E0_tower_MeV", mp.nstr(E0_tower, 20))
          .add_parameter("merge_unit_MeV", mp.nstr(E0_tower * LN2, 20))
          .add_data("summary", {"n_words": len(words), "n_len_le_4": n_short, "n_len_extra": len(extra),
                                "n_pass_q0": len(passing), "n_pass_q0_word_level_non_product": len(nonprod_pass),
                                "n_pass_q0_intrinsic_three_body": sum(r["intrinsic_three_body"] for r in passing),
                                "max_merges_pass_q0": max_m_pass, "three_m_2H": 6,
                                "n_pass_q0_b3_q0_positive": len(pos_b3_pass),
                                "n_pass_q0_classical_b3_positive": len(pos_b3cl_pass),
                                "n_pair_group_products_of_9_factorial": len(PAIR_GROUP_PRODUCTS),
                                "max_seminormal_vs_schur_weyl_dev": mp.nstr(max_dev, 5)})
          .add_data("table", summary)
          .add_data("passing_q0", [ser(r) for r in passing])
          .add_data("non_product_all", [ser(r) for r in rows if not r["word_level_product"]]))
    for name, ok, src in checks:
        wb.add_assertion(name, computed=ok, expected=True, tolerance=0, source=src)
    wb.save({"q0Anchor": "proton", "q0Value": mp.nstr(Q, 50),
             "q0AnchorReason": "q0 enters through cf.Q (committed y-lambda-at-q0 witness, proton pin)"})
    return 0 if all(ok for _, ok, _ in checks) else 1


if __name__ == "__main__":
    sys.exit(main())
