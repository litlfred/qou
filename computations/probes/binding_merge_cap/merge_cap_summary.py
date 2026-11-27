#!/usr/bin/env python3
"""merge_cap_summary.py — witness for the per-component q0 merge cap (bean qou-brng, C2 front B).

Reads the per-word censuses written by merge_cap_census.py (A = 2, 3), the A = 4 length <= 4
checkpoint of binding_ceiling_q0_a4_probe.py (read-only, whatever rows exist when this runs), and
the A = 4 length-5 targeted runs of merge_cap_a4_targeted.py. For every word it splits the bond
word into support components (vertices V(s) occupy strands s..s+2; overlapping vertices join) and
computes each component's merges exactly from its own permutation. It then tests

    (H) every word passing reading 3 at q0 has every support component merging <= 2,

which with QOU.MassTheory.MergeComponentAdditivity.merges_prod_le gives merges <= 2 * components.
Also records whether each q0-failing, classically-passing four-merge word fails only on cells where
the classical (q = 1) two-row character is exactly 0. Counts only; no ratio, AME not read; no
floats. q0 enters only through the censuses (proton pin, convention D, corpus seminormal helpers).

-- Ref: [leitner2026] bean qou-brng; docs/audits/2026-11-27-binding-merge-cap-invariant.md
"""
from __future__ import annotations
import json, sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
import os
A4_CKPT = Path(os.environ.get("MERGE_CAP_A4_CKPT",
               HERE.parent / "binding_ceiling_q0" / "binding-ceiling-q0-A4-L4.checkpoint.jsonl"))


def cyc_lengths(p):
    seen, out = [False] * len(p), []
    for i in range(len(p)):
        if not seen[i]:
            ln, j = 0, i
            while not seen[j]:
                seen[j], j, ln = True, p[j], ln + 1
            out.append(ln)
    return out


def a_seq(lengths, n):
    a = [1] + [0] * n
    for ln in lengths:
        bb = a[:]
        for k in range(n + 1 - ln):
            bb[k + ln] += a[k]
        a = bb
    return a


def restrict(p, m):
    out = []
    for i in range(m):
        j = p[i]
        while j >= m:
            j = p[j]
        out.append(j)
    return out


def perm_of(gens, n):
    p = list(range(n))
    for s in gens:
        for g in (s, s + 1):
            p[g], p[g + 1] = p[g + 1], p[g]
    return p


def classical_pass(p, n):
    for m in range(1, n + 1):
        a = a_seq(cyc_lengths(restrict(p, m)), m)
        if not all(a[k] <= a[k + 1] for k in range(m // 2)):
            return False
    return True


def classical_char(p, m, k):
    a = a_seq(cyc_lengths(restrict(p, m)), m)
    return a[k] - (a[k - 1] if k > 0 else 0)


def component_merges(gens, n):
    comps = []
    for s in set(gens):
        span, mem = set(range(s, s + 3)), {s}
        for c in [c for c in comps if c[0] & span]:
            comps.remove(c); span |= c[0]; mem |= c[1]
        comps.append((span, mem))
    return [n - len(cyc_lengths(perm_of([s for s in gens if s in mem], n))) for _, mem in comps]


def load(path, A):
    rows = []
    for line in Path(path).read_text().splitlines():
        r = json.loads(line)
        r["gens"] = r.get("gens") or [int(c) for c in r["word"].split("V")[1:]]
        r["A"] = A
        rows.append(r)
    return rows


def main() -> int:
    sources = [("A2-L6-census", HERE / "merge-cap-census-A2-L6.jsonl", 2),
               ("A3-L4-census", HERE / "merge-cap-census-A3-L4.jsonl", 3),
               ("A4-L4-checkpoint", A4_CKPT, 4)]
    sources += [(f.stem, f, int(f.stem.split("-")[2][1:])) for f in sorted(HERE.glob("merge-cap-A[0-9]-L5-*.jsonl"))]
    table, violations, marginal, nrows = {}, [], Counter(), {}
    for tag, path, A in sources:
        if not Path(path).exists():
            continue
        n = 3 * A
        t = Counter()
        nrows[tag] = len(Path(path).read_text().splitlines())
        for r in load(path, A):
            p = perm_of(r["gens"], n)
            cm = component_merges(r["gens"], n)
            assert sum(cm) == n - len(cyc_lengths(p))
            cp = classical_pass(p, n)
            t[f"pass_q0={r['pass_q0']},classical={cp},max_component_merges={max(cm)},components={len(cm)}"] += 1
            if r["pass_q0"] and max(cm) > 2:
                violations.append({"source": tag, "word": r["word"]})
            if (not r["pass_q0"]) and cp and sum(cm) >= 4 and "fails_q0" in r:
                vals = [classical_char(p, int(c.split(":")[0]), int(c.split(":")[1].split(",")[1]))
                        for c in r["fails_q0"]]
                marginal[f"{tag}: classical value on every q0-failing cell is 0 = {all(v == 0 for v in vals)}"] += 1
        table[tag] = dict(sorted(t.items()))
        print(tag, json.dumps(table[tag], indent=1), flush=True)
    print("marginal", dict(marginal), flush=True)
    print("violations of (H):", violations, flush=True)

    # Exhaustive classical fact (S_n, n <= 9): among permutations passing classical reading 3 at
    # every level, which merge counts force a vanishing top-level two-row character?
    import itertools
    exhaustive = {}
    for n in range(4, 10):
        cnt = Counter()
        for p in itertools.permutations(range(n)):
            p = list(p)
            if not classical_pass(p, n):
                continue
            a = a_seq(cyc_lengths(p), n)
            ztop = any(a[k] == a[k + 1] for k in range(n // 2))
            cnt[f"merges={n - len(cyc_lengths(p))},top_level_zero={ztop}"] += 1
        exhaustive[str(n)] = dict(sorted(cnt.items()))
        print(n, exhaustive[str(n)], flush=True)
    s9 = exhaustive["9"]
    s9_ok = all(not (int(k.split(",")[0].split("=")[1]) >= 4 and k.endswith("False")) for k in s9)
    viol_lengths = sorted({len([c for c in v["word"].split("V") if c]) for v in violations})

    sys.path.insert(0, str(HERE.parent / "binding_ceiling_q0"))
    sys.argv = [sys.argv[0], "1", "2"]
    import binding_ceiling_q0_probe as b
    from qou_substrate.witness import WitnessBuilder
    wb = (WitnessBuilder("binding-merge-cap-per-component", engine="mpmath")
          .set_description(
              "PROBE (bean qou-brng, brief C2 front B): per-support-component merge counts of every "
              "gamma-gamma bond word in the reading-3 censuses at the proton-pin q0 (A = 2, 3, 4). Tests "
              "(H): every q0-passing word has each support component merging <= 2 (falsified at A = 3, length 5); "
              "exhaustive S_n (n <= 9) top-level-zero fact. Counts only; no ratio; "
              "AME not read; nothing fitted or wired.")
          .set_audit_only("docs/audits/2026-11-27-binding-merge-cap-invariant.md")
          .add_data("rows_per_source", nrows)
          .add_data("tallies", table)
          .add_data("marginal_failures", dict(marginal))
          .add_data("violations_of_H", violations)
          .add_data("classical_exhaustive_top_level_zero", exhaustive))
    wb.add_assertion("H_per_component_cap_2_violated_only_by_length_5_words", computed=viol_lengths,
                     expected=[5], tolerance=0,
                     source="(H) holds on every word of length <= 4; its counterexamples are length-5 A = 3 words")
    wb.add_assertion("S9_classical_admissible_with_merges_ge_4_has_top_level_zero", computed=s9_ok,
                     expected=True, tolerance=0, source="exhaustive over S_9, Young's rule a_k")
    wb.save({"q0Anchor": "proton", "q0Value": str(b.mp.nstr(b.Q, 50)),
             "q0AnchorReason": "q0 enters through the censuses via cf.Q (committed y-lambda-at-q0 witness, proton pin)"})
    return 0 if (viol_lengths == [5] and s9_ok) else 1


if __name__ == "__main__":
    sys.exit(main())
