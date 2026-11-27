#!/usr/bin/env python3
"""PROBE (bean qou-brng, brief C2 front C): which corpus selection rules pick which gamma-gamma bond.

Question. The corpus holds several rules that could pick the nuclear bond word without reading the
binding. This probe applies each one to the same populations and reports what it selects at A = 2, 3, 4.

Populations (reading 3 at the proton pin, convention D, corpus seminormal helpers):
  * A = 2: the 408 passing bond words of length <= 6 on six strands
    (binding_ceiling_q0/binding-ceiling-q0.witness.json, = PR #9426 Phase A);
  * A = 3: the 28 passing words of length <= 4 on nine strands (binding-ceiling-q0-A3.witness.json),
    PLUS, computed here, every junction-vertex-only word (vertices V1, V2, V4, V5) of length 2..5
    and the four length-6 words V(a)^3 V(b)^3, a in {1,2}, b in {4,5};
  * A = 4: V2V3V4V8 (passing, PR #9526 section 7) and V2^3 V5^3 V8^3, computed here.

Classical structure is exact integer arithmetic on the braid word (nucleons V(3k)^3 first, bond appended
on the right): free reduction, crossing count, merges split into inter-nucleon and intra-nucleon,
whole-word linking neutrality (every component's self-writhe and every pairwise linking number zero,
PhotonU1NeutralCut.Neutral), purity (trivial permutation).

Nothing here reads AME. Ratios are carried from the witnesses as strings or computed in mpmath; they are
reported, never used to select. No float arithmetic.
"""
from __future__ import annotations

import itertools
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
CEIL = HERE.parent / "binding_ceiling_q0"

LEN_MAX_A3 = int(sys.argv[1]) if len(sys.argv) > 1 else 5


# ---------------------------------------------------------------- exact classical structure
def V(s):
    return [(s, False), (s + 1, True)]


def parse(word):
    return [int(t) for t in word.split("V") if t]


def reduce_free(letters):
    st = []
    for g, inv in letters:
        if st and st[-1] == (g, not inv):
            st.pop()
        else:
            st.append((g, inv))
    return st


def structure(bond, A):
    """bond: list of vertex sites. Returns exact classical data of nucleons V(3k)^3 then the bond."""
    n = 3 * A
    x = [lt for k in range(A) for lt in V(3 * k) * 3]
    K = [lt for s in bond for lt in V(s)]
    red = reduce_free(K)
    pos = list(range(n))           # pos[p] = strand currently at position p
    cross = []                     # (strand_a, strand_b, sign)
    for g, inv in x + K:
        a, b = pos[g], pos[g + 1]
        cross.append((a, b, -1 if inv else 1))
        pos[g], pos[g + 1] = b, a
    # closure: strand pos[p] ends at position p and continues as strand p
    nxt = {pos[p]: p for p in range(n)}
    comp, c = [-1] * n, 0
    for i in range(n):
        if comp[i] < 0:
            j = i
            while comp[j] < 0:
                comp[j] = c
                j = nxt[j]
            c += 1
    self_w = [0] * c
    pair = {}
    for a, b, sg in cross:
        ca, cb = comp[a], comp[b]
        if ca == cb:
            self_w[ca] += sg
        else:
            key = (min(ca, cb), max(ca, cb))
            pair[key] = pair.get(key, 0) + sg
    neutral = all(w == 0 for w in self_w) and all(v == 0 for v in pair.values())
    merges = n - c
    groups = {frozenset(i // 3 for i in range(n) if comp[i] == k) for k in range(c)}
    # block-level connectivity: union blocks sharing a component
    parent = list(range(A))

    def f(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u
    for g_ in groups:
        g_ = sorted(g_)
        for u in g_[1:]:
            parent[f(u)] = f(g_[0])
    inter = A - len({f(u) for u in range(A)})
    junction_sites = {3 * j - 2 for j in range(1, A)} | {3 * j - 1 for j in range(1, A)}
    return {
        "bond_vertices": len(bond),
        "bond_crossings_reduced": len(red),
        "bond_reduced": "".join(f"s{g}{'-' if inv else ''}" for g, inv in red),
        "junction_vertex_only": set(bond) <= junction_sites,
        "merges": merges,
        "merges_inter_nucleon": inter,
        "merges_intra_nucleon": merges - inter,
        "linking_neutral": neutral,
        "pure": all(nxt[i] == i for i in range(n)),
        "self_writhes": sorted(w for w in self_w if w != 0),
    }


# ---------------------------------------------------------------- rules
COSTS = {
    # crossing count of the word as written in vertices (2 per vertex): the cost PR #9426 used
    "written": lambda r: 2 * r["bond_vertices"],
    # crossing count after free reduction (sigma sigma^-1 cancelled): crossing energy on reduced words
    "reduced": lambda r: r["bond_crossings_reduced"],
}


def cheapest(rows, pred, cost):
    cands = [r for r in rows if pred(r)]
    if not cands:
        return None, []
    m = min(cost(r) for r in cands)
    return m, sorted(r["word"] for r in cands if cost(r) == m)


RULES = {
    "R1_frobenius_selected_all_bond_words": lambda r: True,
    "R2_frobenius_selected_junction_vertices_only": lambda r: r["junction_vertex_only"],
    "R3_whole_word_linking_neutral": lambda r: r["linking_neutral"],
    "R4_pure_zero_linking": lambda r: r["pure"] and r["linking_neutral"],
    "R5_no_intra_nucleon_merge": lambda r: r["merges_intra_nucleon"] == 0,
    "R6_cheapest_that_merges": lambda r: r["merges"] > 0,
}


def apply_rules(rows):
    out = {}
    for cname, cost in COSTS.items():
        for name, pred in RULES.items():
            m, ws = cheapest(rows, pred, cost)
            sel = [r for r in rows if r["word"] in ws]
            out[f"{name}__cost_{cname}"] = {
                "cost": m, "selected": ws,
                "merges": sorted({r["merges"] for r in sel}),
                "merges_intra_nucleon": sorted({r["merges_intra_nucleon"] for r in sel}),
                "linking_neutral": sorted({r["linking_neutral"] for r in sel}),
                "ratio": sorted({r["ratio"][:16] for r in sel})}
    return out


def main() -> int:
    checks = []

    def check(name, ok, src):
        checks.append((name, bool(ok), src))
        print(f"[{'PASS' if ok else 'FAIL'}] {name}", flush=True)

    # K0: the nucleon V^3 alone is pure, neutral, merges 0 (BorromeanWordForcing / PhotonU1NeutralCut)
    s0 = structure([], 2)
    check("K0_free_word_pure_neutral", s0["pure"] and s0["linking_neutral"] and s0["merges"] == 0,
          "V^3 x V^3 is a pure zero-linking braid")

    pops = {}
    for A, fn in ((2, "binding-ceiling-q0.witness.json"), (3, "binding-ceiling-q0-A3.witness.json")):
        w = json.loads((CEIL / fn).read_text())
        rows = []
        for p in w["data"]["passing"]:
            st = structure(parse(p["word"]), A)
            assert st["merges"] == p["merges"], (p["word"], st["merges"], p["merges"])
            rows.append({"word": p["word"], "ratio": p["ratio"], "source": fn, **st})
        pops[A] = rows
    check("K1_merge_counts_reproduce_ceiling_witnesses", True,
          "exact recomputation agrees with every merges field of both ceiling witnesses (assert)")

    # ---- reading 3 for the junction-vertex-only population at A = 3 (and A = 4 spot words)
    import mpmath as mp  # noqa: E402
    sys.argv = [sys.argv[0], "1", "3"]
    sys.path.insert(0, str(CEIL))
    import binding_ceiling_q0_probe as P3  # noqa: E402  (module-level N = 9)

    x3 = [(s + 3 * a, i) for a in range(3) for (s, i) in V(0) * 3]
    tr3, ok3 = P3.corpus_trace_and_pass(x3)
    check("K2_A3_free_passes", ok3, "nine-strand V^3 x V^3 x V^3 passes reading 3")
    J1, J2, alpha = {1, 2}, {4, 5}, (1, 2, 4, 5)
    words = [w for n in range(2, LEN_MAX_A3 + 1) for w in itertools.product(alpha, repeat=n)
             if J1 & set(w) and J2 & set(w)]
    words += [(a,) * 3 + (b,) * 3 for a in (1, 2) for b in (4, 5)]
    t0, step = time.time(), max(1, len(words) // 20)
    jrows, n_eval = [], 0
    for k, wd in enumerate(words, 1):
        K = [lt for s in wd for lt in V(s)]
        tr, ok = P3.corpus_trace_and_pass(x3 + K)
        n_eval += 1
        if k % step == 0:
            el = time.time() - t0
            print(f"  A3 junction-only {k}/{len(words)} elapsed {el:.0f}s ETA {el / k * (len(words) - k):.0f}s",
                  flush=True)
        if ok:
            word = "".join(f"V{s}" for s in wd)
            jrows.append({"word": word, "ratio": mp.nstr(tr / tr3, 25), "source": "computed here",
                          **structure(list(wd), 3)})
    print(f"A3 junction-vertex-only: {len(jrows)} of {n_eval} pass", flush=True)
    known = {r["word"] for r in pops[3]}
    pops[3] += [r for r in jrows if r["word"] not in known]

    # A = 4 spot words (twelve strands): needs a fresh module instance with N = 12
    import importlib.util
    spec = importlib.util.spec_from_file_location("P4", CEIL / "binding_ceiling_q0_probe.py")
    sys.argv = [sys.argv[0], "1", "4"]
    P4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(P4)
    x4 = [(s + 3 * a, i) for a in range(4) for (s, i) in V(0) * 3]
    tr4, ok4 = P4.corpus_trace_and_pass(x4)
    a4 = []
    for wd in ((2, 3, 4, 8), (2, 2, 2, 5, 5, 5, 8, 8, 8)):
        K = [lt for s in wd for lt in V(s)]
        tr, ok = P4.corpus_trace_and_pass(x4 + K)
        a4.append({"word": "".join(f"V{s}" for s in wd), "passes_reading3": ok,
                   "ratio": mp.nstr(tr / tr4, 25), **structure(list(wd), 4)})
        print("A4", a4[-1], flush=True)
    check("K3_A4_V2V3V4V8_passes", a4[0]["passes_reading3"], "PR #9526 section 7 reproduced")

    sel = {A: apply_rules(rows) for A, rows in pops.items()}
    for A in sel:
        for k, v in sel[A].items():
            print(f"A={A} {k}: {v}", flush=True)
    check("K4_R2_written_cost_reproduces_PR9426_selection",
          sel[2]["R2_frobenius_selected_junction_vertices_only__cost_written"]["selected"] == ["V1V1V1", "V2V2V2"],
          "gg_deuteron_bond/results.md: cheapest passing pure-junction bond is V(1)^3 / V(2)^3")
    check("K5_R1_written_cost_is_V2V3_tie",
          sel[2]["R1_frobenius_selected_all_bond_words__cost_written"]["selected"] == ["V2V3", "V3V2"],
          "unrestricted cheapest passing bond at A = 2, written cost (2026-11-27 ceiling audit section 6)")

    # V2V3 dissected
    vv = structure([2, 3], 2)
    print("V2V3 structure:", vv, flush=True)

    from qou_substrate.witness import WitnessBuilder  # noqa: E402
    stats = {A: {"n_rows": len(r), "n_linking_neutral": sum(x["linking_neutral"] for x in r),
                 "n_pure": sum(x["pure"] for x in r),
                 "n_merging_neutral": sum(x["linking_neutral"] and x["merges"] > 0 for x in r),
                 "n_intra_merge": sum(x["merges_intra_nucleon"] > 0 for x in r)} for A, r in pops.items()}
    print("stats", stats, flush=True)
    wb = (WitnessBuilder("bond-selection-rules", engine="mpmath")
          .set_description(
              "PROBE (bean qou-brng, brief C2 front C): six corpus selection rules applied to the passing "
              "gamma-gamma bond words at A = 2, 3, 4. Exact classical structure (merges split inter/intra "
              "nucleon, whole-word linking neutrality, purity); reading 3 at q0 from the corpus seminormal "
              "helpers. Ratios reported, never used to select. AME not read. Nothing fitted or wired.")
          .set_audit_only("docs/audits/2026-11-27-bond-selection-rule-search.md")
          .add_parameter("len_max_A3_junction_only", LEN_MAX_A3)
          .add_data("selections", {str(A): v for A, v in sel.items()})
          .add_data("population_stats", {str(A): v for A, v in stats.items()})
          .add_data("A4_spot_words", a4)
          .add_data("V2V3_structure", vv)
          .add_data("A3_junction_only_passing", jrows)
          .add_data("A3_junction_only_n_evaluated", n_eval))
    for name, ok, src in checks:
        wb.add_assertion(name, computed=ok, expected=True, tolerance=0, source=src)
    wb.save({"q0Anchor": "proton", "q0Value": mp.nstr(P3.Q, 50),
             "q0AnchorReason": "q0 enters through cf.Q (committed y-lambda-at-q0 witness, proton pin)"})
    return 0 if all(ok for _, ok, _ in checks) else 1


if __name__ == "__main__":
    sys.exit(main())
