#!/usr/bin/env python3
"""binding_ceiling_q0_a4_probe.py — the q0 merge cap at A = 4 (12 strands).

Bean `qou-brng` (brief C2), follow-up of `binding_ceiling_q0_probe.py` (PR #9526). There, every
γγ bond word passing reading 3 merged exactly 2 closure components at A = 2 and A = 3. At A = 4,
every word of length <= 4 that bonds all three junctions merges at least 4 (classical, exact), so
the question "is the q0 cap 2 for every A" becomes: does ANY such word pass reading 3?

Population: concatenations of V(0)..V(9) of length 3..L bonding every junction (1392 words for
L = 4). Words that pass reading 3 classically (q = 1, all levels; Young's rule) are evaluated first,
so a partial run already covers the likeliest passers. Reading 3 at q0 uses the corpus seminormal
helpers exactly as the A = 2, 3 probe does (~19 s per word at n = 12, run on a process pool). Ratio
reported for passing words, never used to select. AME not read. Nothing fitted or wired. mpmath
throughout, no float arithmetic. Results stream to a .jsonl checkpoint so a stopped run resumes.

-- Ref: [leitner2026] bean qou-brng; bean qou-ales; QOU.MassTheory.ClassicalReading3MergeBound
"""
from __future__ import annotations

import itertools
import json
import sys
import time
from multiprocessing import Pool
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
L = int(sys.argv[1]) if len(sys.argv) > 1 else 4
WORKERS = int(sys.argv[2]) if len(sys.argv) > 2 else 3
A, N = 4, 12
JUNCTIONS = [{3 * j - 2, 3 * j - 1} for j in range(1, A)]
CKPT = HERE / f"binding-ceiling-q0-A4-L{L}.checkpoint.jsonl"


def perm(gens):
    p = list(range(N))
    for g in gens:
        p[g], p[g + 1] = p[g + 1], p[g]
    return p


def cyc_lengths(p):
    seen, out = [False] * len(p), []
    for i in range(len(p)):
        if not seen[i]:
            ln, j = 0, i
            while not seen[j]:
                seen[j], j, ln = True, p[j], ln + 1
            out.append(ln)
    return out


def classical_two_row_ok(lengths, n):
    """a_k (invariant k-subsets) nondecreasing up to n/2, i.e. chi_{(n-k,k)} >= 0 (Young's rule)."""
    a = [1] + [0] * n
    for ln in lengths:
        b = a[:]
        for k in range(n + 1 - ln):
            b[k + ln] += a[k]
        a = b
    return all(a[k] <= a[k + 1] for k in range(n // 2))


def restrict(p, m):
    out = []
    for i in range(m):
        j = p[i]
        while j >= m:
            j = p[j]
        out.append(j)
    return out


BASE_GENS = [g for a in range(A) for _ in range(3) for g in (3 * a, 3 * a + 1)]


def classify(w):
    p = perm(BASE_GENS + [g for s in w for g in (s, s + 1)])
    merges = N - len(cyc_lengths(p))
    ok = all(classical_two_row_ok(cyc_lengths(restrict(p, m)), m) for m in range(1, N + 1))
    return merges, ok


_B = None


def _init():
    global _B
    sys.argv = [sys.argv[0], "1", str(A)]
    sys.path.insert(0, str(HERE))
    import binding_ceiling_q0_probe as b
    _B = b


def evaluate(w):
    b = _B
    x = [(s + 3 * a, i) for a in range(A) for (s, i) in b.V(0) * 3]
    K = [lt for s in w for lt in b.V(s)]
    tr, ok = b.corpus_trace_and_pass(x + K)
    return {"word": "".join(f"V{s}" for s in w), "pass_q0": ok, "trace": mp.nstr(tr, 30)}


def main() -> int:
    words = [w for n in range(3, L + 1) for w in itertools.product(range(N - 2), repeat=n)
             if all(J & set(w) for J in JUNCTIONS)]
    info = {w: classify(w) for w in words}
    words.sort(key=lambda w: (not info[w][1], len(w), w))
    done = {}
    if CKPT.exists():
        for line in CKPT.read_text().splitlines():
            r = json.loads(line)
            done[r["word"]] = r
    todo = [w for w in words if "".join(f"V{s}" for s in w) not in done]
    print(f"A=4 L={L}: {len(words)} words ({sum(v[1] for v in info.values())} classically admissible), "
          f"{len(done)} checkpointed, {len(todo)} to run on {WORKERS} workers", flush=True)
    t0 = time.time()
    with Pool(WORKERS, initializer=_init) as pool, CKPT.open("a") as fh:
        for k, r in enumerate(pool.imap(evaluate, todo), 1):
            w = tuple(int(c) for c in r["word"].split("V")[1:])
            r["merges"], r["classical_pass"] = info[w]
            fh.write(json.dumps(r) + "\n")
            fh.flush()
            done[r["word"]] = r
            if k % 12 == 0 or r["pass_q0"]:
                el = time.time() - t0
                print(f"  {k}/{len(todo)} elapsed {el:.0f}s ETA {el / k * (len(todo) - k):.0f}s"
                      f"{'  PASS ' + r['word'] if r['pass_q0'] else ''}", flush=True)
    rows = list(done.values())
    summary = {}
    for r in rows:
        key = f"merges={r['merges']},classical={'pass' if r['classical_pass'] else 'fail'}"
        s = summary.setdefault(key, {"n": 0, "pass_q0": 0})
        s["n"] += 1
        s["pass_q0"] += r["pass_q0"]
    print(json.dumps(summary, indent=1), flush=True)

    sys.argv = [sys.argv[0], "1", str(A)]
    sys.path.insert(0, str(HERE))
    import binding_ceiling_q0_probe as b
    from qou_substrate.witness import WitnessBuilder
    n_pass = sum(r["pass_q0"] for r in rows)
    wb = (WitnessBuilder(f"binding-ceiling-q0-A4-L{L}", engine="mpmath")
          .set_description(
              "PROBE (bean qou-brng, brief C2): reading 3 at the proton-pin q0 on every gamma-gamma bond "
              f"word of 3..{L} vertices bonding all three junctions of the 12-strand A = 4 word with V^3 "
              "nucleons. Every such word merges >= 4 components (exact). Ratio reported for passing words "
              "only, never used to select. AME not read. Nothing fitted or wired.")
          .set_audit_only("docs/audits/2026-11-27-binding-ceiling-at-q0.md")
          .add_parameter("L", L).add_parameter("A", A).add_parameter("n_strands", N)
          .add_data("summary_by_merges_and_classical_reading3", summary)
          .add_data("passing", [r for r in rows if r["pass_q0"]]))
    wb.add_assertion("every_word_evaluated", computed=len(rows), expected=len(words), tolerance=0,
                     source="checkpoint covers the whole population")
    wb.add_assertion("min_merges_at_least_4", computed=min(r["merges"] for r in rows), expected=4,
                     tolerance=0, source="classical permutation of every population word")
    wb.save({"q0Anchor": "proton", "q0Value": mp.nstr(b.Q, 50),
             "q0AnchorReason": "q0 enters through cf.Q (committed y-lambda-at-q0 witness, proton pin)"})
    print(f"{n_pass} of {len(rows)} pass reading 3 at q0", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
