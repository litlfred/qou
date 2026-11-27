#!/usr/bin/env python3
"""rule1_pure_junction_a3_search.py — rule (1) "cheapest passing pure-junction γγ bond" at A = 3.

Bean `qou-brng` (brief C2, front E). Rule (1) is the corpus `FrobeniusSelected` rule as applied to
the deuteron on owner card 1 (2026-11-25): a bond is a pure-junction γγ word (vertices on junction
strands only), and among those that pass reading 3 the bond is the cheapest by crossing count. At
A = 2 it gives V(1)^3 / V(2)^3 (PR #9426). At A = 3 the population of `binding_ceiling_q0_probe.py`
(lengths 1..4) holds NO passing pure-junction word, so the rule is undefined there. This script
extends the pure-junction population (alphabet V1, V2, V4, V5; every junction bonded) length by
length from 5 and stops after the first length at which some word passes. Exhaustive per length,
so "cheapest" is exact for the lengths covered. Scorecard only; nothing adopted or wired.

Reading 3 and the trace use the same corpus seminormal helpers as the ceiling probe (convention D,
proton pin, mpmath 40 dps). Results stream to a .jsonl checkpoint (resumable).

-- Ref: [leitner2026] bean qou-brng; QOU.MassTheory.GammaGammaFrobeniusSelection
"""
from __future__ import annotations

import itertools
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.argv = [sys.argv[0], "4", "3"]          # ceiling-probe globals: L (unused here), A = 3
sys.path.insert(0, str(HERE.parent / "binding_ceiling_q0"))
import binding_ceiling_q0_probe as bc  # noqa: E402

mp = bc.mp
LMAX = 7
CKPT = HERE / "rule1-pure-junction-a3.checkpoint.jsonl"
ALPHABET = sorted(set().union(*bc.JUNCTIONS))   # [1, 2, 4, 5]


def main() -> int:
    done = {}
    if CKPT.exists():
        for line in CKPT.read_text().splitlines():
            r = json.loads(line)
            done[r["word"]] = r
    x = [(s + 3 * a, i) for a in range(bc.A) for (s, i) in bc.V(0) * 3]
    trx, okx = bc.corpus_trace_and_pass(x)
    assert okx
    c_free = bc.n_cycles(bc.perm(x))
    for L in range(5, LMAX + 1):
        words = [w for w in itertools.product(ALPHABET, repeat=L)
                 if all(J & set(w) for J in bc.JUNCTIONS)]
        t0 = time.time()
        print(f"L={L}: {len(words)} pure-junction bond words", flush=True)
        with CKPT.open("a") as fh:
            for k, w in enumerate(words, 1):
                name = "".join(f"V{s}" for s in w)
                if name in done:
                    continue
                K = [lt for s in w for lt in bc.V(s)]
                tr, ok = bc.corpus_trace_and_pass(x + K)
                rec = {"word": name, "length": L, "pass": bool(ok)}
                if ok:
                    r = tr / trx
                    rec.update({"ratio": mp.nstr(r, 25), "minus_ln_r": mp.nstr(-mp.log(r), 25) if r > 0 else None,
                                "merges": c_free - bc.n_cycles(bc.perm(x + K)),
                                "sw_dev": mp.nstr(abs(tr - bc.sw_trace(x + K)), 5)})
                    print("  PASS", rec, flush=True)
                fh.write(json.dumps(rec) + "\n")
                fh.flush()
                done[name] = rec
                if k % 100 == 0:
                    el = time.time() - t0
                    print(f"  {k}/{len(words)} elapsed {el:.0f}s ETA {el / k * (len(words) - k):.0f}s", flush=True)
        if any(done[n]["pass"] for n in done if done[n]["length"] == L):
            print(f"first passing length {L}; stop", flush=True)
            break
    lengths = sorted({r["length"] for r in done.values()})
    first = min((r["length"] for r in done.values() if r["pass"]), default=None)
    passing = sorted((r for r in done.values() if r["pass"] and r["length"] == first),
                     key=lambda r: mp.mpf(r["minus_ln_r"]))
    E0 = mp.mpf("4.2274833556290305503")
    by_m = {}
    for r in passing:
        by_m.setdefault(r["merges"], []).append(r)
    wb = (bc.WitnessBuilder("rule1-pure-junction-a3", engine="mpmath")
          .set_description(
              "PROBE (bean qou-brng, brief C2 front E): rule (1) 'cheapest passing pure-junction gamma-gamma bond' "
              "at A = 3. Pure-junction words (V1, V2, V4, V5) bonding both junctions, exhaustive per length from 5 "
              "(lengths <= 4 hold no passing pure-junction word, ceiling witness A3). Reading 3 at q0 by the corpus "
              "seminormal helpers; trace cross-checked by Schur-Weyl. Scorecard only; nothing adopted.")
          .set_audit_only("docs/audits/2026-11-27-bond-rules-and-length-cutoff.md")
          .add_parameter("A", bc.A).add_parameter("lengths_searched", lengths)
          .add_parameter("E0_tower_MeV", mp.nstr(E0, 20))
          .add_data("summary", {"n_searched": len(done), "first_passing_length": first, "n_tied": len(passing),
                                "minus_ln_r_min": passing[0]["minus_ln_r"] if passing else None,
                                "minus_ln_r_max": passing[-1]["minus_ln_r"] if passing else None,
                                "B_MeV_min": mp.nstr(E0 * mp.mpf(passing[0]["minus_ln_r"]), 12) if passing else None,
                                "B_MeV_max": mp.nstr(E0 * mp.mpf(passing[-1]["minus_ln_r"]), 12) if passing else None,
                                "count_by_merges": {str(k): len(v) for k, v in sorted(by_m.items())},
                                "max_schur_weyl_dev": max((r["sw_dev"] for r in passing), key=lambda v: mp.mpf(v)) if passing else None})
          .add_data("passing_at_first_length", passing))
    wb.add_assertion("some_pure_junction_word_passes", computed=first is not None, expected=True, tolerance=0,
                     source="exhaustive per length")
    wb.add_assertion("schur_weyl_agrees", computed=all(mp.mpf(r["sw_dev"]) < bc.TOL for r in passing),
                     expected=True, tolerance=0, source="independent trace, 1e-25")
    wb.save({"q0Anchor": "proton", "q0Value": mp.nstr(bc.Q, 50),
             "q0AnchorReason": "q0 enters through cf.Q (committed y-lambda-at-q0 witness, proton pin)"})
    return 0


if __name__ == "__main__":
    sys.exit(main())
