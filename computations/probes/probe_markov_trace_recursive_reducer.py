#!/usr/bin/env python3
"""
probe_markov_trace_recursive_reducer.py — I1 probe for
`prop:markov-trace-recursive-reducer`.

The proposition: the recursive Markov-trace reducer (the algorithmic
content of the Markov-trace EXISTENCE theorem — the trace is uniquely
determined by its axioms, and the recursion constructs that unique value
for any word) agrees with the canonical seminormal / Hoefsmit–Wedderburn
engine on all values. Both routes compute tr_M; they must coincide.

This probe checks that agreement, exact in ℚ(q), across single-top,
multi-top, and multi-strand (H_2, H_3, H_4) braid words.

Conventions reconciled (verified):
  * recursive `markov_trace_of_word(n, word)` — word is 1-indexed signed
    generators ([1] = σ_0), result in (z_sym, q) with
    z_sym = 1/(√q + 1/√q).
  * canonical `tr_M_word(word, n, z, h)` — word is 0-indexed, result in
    (z, h) with h = q − 1/q.
  * map: recursive index i ↔ canonical i−1; z_sym ↔ z; h ↔ q − 1/q.

Note: this probe is what the `tr_M_word` IndexError fix (the
`max_gen != n−2` normalization) unblocked — multi-top words such as
(1,0,1) exercise the previously-crashing branch.

Output: probe-markov-trace-recursive-reducer.witness.json
"""
from __future__ import annotations

import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from pathlib import Path

import sympy as sp

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent / "markov"))
sys.path.insert(0, str(HERE.parent / "substrate"))

import markov_trace_recursive as R  # noqa: E402
from markov_trace_canonical import tr_M_word, Z_SYMB, H_SYMB  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def main() -> int:
    q = sp.symbols("q", positive=True)
    q_rec = R.q
    z_rec = R.z_sym

    # Recursive words are 1-indexed signed generators; canonical 0-indexed.
    # Cover single-top, σ², multi-top H_3, and H_4/H_5 multi-top-1 words.
    #
    # The H_4 words below recurse to subwords like (1,0,0,1) that used to
    # hit `_tr_M_word_impl`'s `NotImplementedError("Complex braid case
    # (multiple top-1 in segment)")`. That branch is now implemented (the
    # σ_top·segment·σ_top block is expanded through the generic Hecke word
    # reducer into ≤1-top normal-form words), so the agreement check now
    # covers them. An H_5 word is included as a beyond-H_4 spot-check.
    rec_words = [
        [1],                  # σ_0 in H_2
        [1, 1],               # σ_0²  (Hecke relation)
        [1, 2, 1],            # H_3 braid
        [1, 2],               # H_3 chain
        [2, 1, 2, 1],         # H_3, multi-top (exercises the fixed branch)
        [2, 1, 2],            # H_3, multi-top
        [1, 2, 3, 2, 1],      # H_4, multi-top-1 (was NotImplementedError)
        [1, 2, 3, 2],         # H_4 chain-back
        [1, 2, 3, 1, 2],      # H_4 multi-top
        [2, 3, 2, 3],         # H_4 multi-top, top=σ_2 repeated
        [1, 2, 3, 4, 3, 2, 1],  # H_5 spot-check (5-strand analogue)
    ]

    print("=" * 78)
    print("  Probe — prop:markov-trace-recursive-reducer")
    print("  recursive reducer  vs  canonical seminormal/Hoefsmit engine")
    print("=" * 78)

    rows = []
    all_agree = True
    for rw in rec_words:
        n = max(abs(i) for i in rw) + 1          # 1-indexed top gen i ⇒ n = i+1
        cw = tuple(i - 1 for i in rw)            # 0-indexed
        rec = sp.cancel(R.markov_trace_of_word(n, list(rw))).subs({q_rec: q, z_rec: Z_SYMB})
        can = sp.sympify(tr_M_word(cw, n, Z_SYMB, H_SYMB)).subs(H_SYMB, q - 1 / q)
        diff = sp.simplify(rec - can)
        agree = diff == 0
        all_agree = all_agree and agree
        mark = "✓" if agree else "✗"
        print(f"  rec{rw} (n={n}) vs can{cw}: diff={diff}  {mark}")
        rows.append({"rec_word": rw, "n": n, "can_word": list(cw), "agree": bool(agree)})

    if not all_agree:
        print("  ✗ a route DISAGREEMENT was found")
        return 1
    print(f"  ✓ both routes agree (exact in ℚ(q)) on all {len(rec_words)} words")

    wb = WitnessBuilder("probe-markov-trace-recursive-reducer", engine="sympy")
    wb.set_content_block("prop:markov-trace-recursive-reducer")
    wb.set_description(
        "I1 probe: the recursive Markov-trace reducer agrees with the "
        "canonical seminormal/Hoefsmit–Wedderburn engine, exact in ℚ(q), "
        "across single-top, multi-top, and H_2/H_3/H_4/H_5 words. "
        "Conventions reconciled (recursive 1-indexed (z_sym,q) ↔ canonical "
        "0-indexed (z,h), h=q−1/q). The H_4 multi-top-1 words (e.g. "
        "[1,2,3,2,1], which recurses to the subword (1,0,0,1)) exercise the "
        "previously-unimplemented braid branch, now reduced via the generic "
        "Hecke word reducer; an H_5 word confirms the fix generalizes."
    )
    for r in rows:
        wb.add_assertion(
            f"routes_agree_{''.join(map(str, r['rec_word']))}_n{r['n']}",
            computed=int(r["agree"]), expected=1,
        )
    wb.add_data("words_checked", rows)
    out = wb.save()
    print(f"  ✓ Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
