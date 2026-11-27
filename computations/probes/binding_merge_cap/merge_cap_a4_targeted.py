#!/usr/bin/env python3
"""merge_cap_a4_targeted.py — test the "2 merges per support component" hypothesis (A = 4 default; A = 3 via 4th arg).

Bean qou-brng (brief C2, front B). The A = 4, length <= 4 population of
binding_ceiling_q0_a4_probe.py has no single-component word that merges 4, so it cannot test
whether the q0 cap counts merges per connected component of the bond word's support (strand
intervals [s, s+2] of its vertices V(s), joined when they overlap). This probe takes the length-L
bond words bonding all three junctions, keeps those with a chosen (merges, components) that pass
reading 3 classically (q = 1, every level; Young's rule), collapses words equal as Hecke elements
under the commutation V(s)V(t) = V(t)V(s) for |s - t| >= 3 (Cartier-Foata normal form), and runs
reading 3 at the proton-pin q0 with the corpus seminormal helpers on one representative per class.
Records failing (level, two-row mu) cells. Ratio is not computed; AME not read; nothing fitted.
mpmath only. Results stream to a .jsonl checkpoint (resumable), single process.

Usage: merge_cap_a4_targeted.py L MERGES COMPONENTS [A=4]
-- Ref: [leitner2026] bean qou-brng; computations/probes/binding_ceiling_q0/binding_ceiling_q0_a4_probe.py
"""
from __future__ import annotations
import itertools, json, sys, time
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).resolve().parent
L, MERGES, NCOMP = (int(a) for a in sys.argv[1:4])
A = int(sys.argv[4]) if len(sys.argv) > 4 else 4
N = 3 * A
JUNCTIONS = [{3 * j - 2, 3 * j - 1} for j in range(1, A)]
CKPT = HERE / f"merge-cap-A{A}-L{L}-m{MERGES}-c{NCOMP}.jsonl"
sys.argv = [sys.argv[0], "1", str(A)]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent / "binding_ceiling_q0"))
import binding_ceiling_q0_probe as b  # noqa: E402
from merge_cap_census import cyc_lengths, classical_fail_levels  # noqa: E402  (N read from argv: A=4)


def components(w):
    cs = []
    for s in set(w):
        s = set(range(s, s + 3))
        for c in [c for c in cs if c & s]:
            cs.remove(c); s |= c
        cs.append(s)
    return len(cs)


def foata(w):
    """Cartier-Foata normal form for the commutation |s - t| >= 3 (equal Hecke elements)."""
    w, out = list(w), []
    while w:
        layer, rest, blocked = [], [], []
        for s in w:
            if all(abs(s - t) >= 3 for t in blocked) and s not in layer:
                layer.append(s)
            else:
                rest.append(s)
            blocked.append(s)
        out.append(tuple(sorted(layer)))
        w = rest
    return tuple(out)


def main():
    x = [(s + 3 * a, i) for a in range(A) for (s, i) in b.V(0) * 3]
    reps = {}
    for w in itertools.product(range(N - 2), repeat=L):
        if not all(J & set(w) for J in JUNCTIONS):
            continue
        if components(w) != NCOMP:
            continue
        p = b.perm(x + [lt for s in w for lt in b.V(s)])
        if N - len(cyc_lengths(p)) != MERGES or classical_fail_levels(p):
            continue
        reps.setdefault(foata(w), w)
    done = set()
    if CKPT.exists():
        done = {json.loads(l)["word"] for l in CKPT.read_text().splitlines()}
    todo = [w for w in reps.values() if "".join(f"V{s}" for s in w) not in done]
    print(f"A={A} L={L} merges={MERGES} comps={NCOMP}: {len(reps)} commutation classes, "
          f"{len(done)} done, {len(todo)} to run", flush=True)
    t0 = time.time()
    with CKPT.open("a") as fh:
        for k, w in enumerate(todo, 1):
            K = [lt for s in w for lt in b.V(s)]
            d = b.base.diag_of(b.corpus_letters(x + K), N)
            lc = b.gga.level_chars(d, N, 1)
            fails = {f"{m}:{','.join(map(str, mu))}": mp.nstr(v, 12)
                     for (m, mu), v in lc.items() if v < -b.TOL}
            rec = {"word": "".join(f"V{s}" for s in w), "gens": list(w), "pass_q0": not fails,
                   "fails_q0": fails, "merges": MERGES, "components": NCOMP, "A": A}
            fh.write(json.dumps(rec) + "\n"); fh.flush()
            el = time.time() - t0
            print(f"  {k}/{len(todo)} {el:.0f}s ETA {el / k * (len(todo) - k):.0f}s "
                  f"{rec['word']} {'PASS' if rec['pass_q0'] else 'fail'}", flush=True)
    print("done", flush=True)


if __name__ == "__main__":
    main()
