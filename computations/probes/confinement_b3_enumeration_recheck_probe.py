#!/usr/bin/env python3
"""Re-run of `prf:confinement-topological` part (iii), live.

Bean `qou/6hm4`. The proof's part (iii) cites
`confinement-lp.witness.json`, which was retired to `_deprecated/` in
May 2026 — an open `da-reproducibility` warn on
`prop:confinement-topological` records that the enumeration is not
backed by a live witness. This re-runs it.

## What the proof claims

> Among the 4^6 = 4096 braid words of length exactly 6 over the
> generators {s0, s1, s0^-1, s1^-1}, **and all shorter words**:
>   - B_3 = s0 s1^-1 s0 s1^-1 s0 s1^-1 achieves |dnet| = 0.000 for both
>     proton and neutron.
>   - The mirror achieves |dnet| = 0.004, an order of magnitude worse.
>   - All other words have |dnet| > 0.01.

## What this script finds

Three of the four statements do not hold, and the fourth is circular.

1. **B_3's |dnet| = 0 is true by construction, not by search.** The
   deprecated producer sets `target_net = float(sum(b3_confined))` —
   the target IS B_3's own confined net. Any operator put in that line
   would score 0. Rank 1 of 5460 is not evidence of selection.
2. **"All other words have |dnet| > 0.01" is false.** 382 words for
   the proton and 167 for the neutron come in at or under 0.01.
3. **The mirror is not the runner-up.** It ranks 12th of 5460 for the
   proton and 111th for the neutron; the best non-B_3 words reach
   0.0016 and 0.0020, well inside the mirror's 0.0035 / 0.0039.
4. **"All shorter words" were never enumerated.** The producer loops
   `for length in [2, 4, 6]` — odd lengths are absent, and they
   matter: the proton's second-best word overall is the length-5
   `s0^-1 s1 s0^-1 s1 s1` at 0.001591, better than every length-6 word
   but B_3 itself.

Point 2 does not even need the odd lengths. The proton's ranks 3-6 are
length 6 at 0.001728 and the neutron's rank 3 is length 4 at 0.002016 —
inside the producer's own enumerated set. Its own table contradicted its
prose.

## Why this is reproducible now and was not the concern before

`|dnet|` is **trace-independent**: `expand_inverse`, `reduce_nf` and
`crossing` read only `HA`, and the metric is a sum of NF coefficients.
So the stale `tr_M` that got the old witness deprecated does not touch
this result — the enumeration was always checkable, and its conclusions
were always wrong.

## Bonus: where the old witness's asymmetric Gram came from

Same `build_gram` code path, two trace vectors (`gram_check` below):

  - stale power rule `[1, z, z, z^2, z^2, z^3]` -> max|G - G^T| = 0.46,
    rank 6, spurious +/- eigenvalue pair
  - canonical `pyhecke.gram.TR_M`             -> max|G - G^T| = 0.0,
    rank 5, spectrum [-a, 0, a, a, a, b]

They differ in **one entry**, `tr_M(e^-)`: `z^3` versus `h z^2 + z`. A
Gram is symmetric for any genuine trace, since `tr(ab) = tr(ba)`; the
power rule is not a trace, so the Gram it builds is not symmetric. The
asymmetry is a consequence of the stale value, not a separate
row-ordering bug (`qou/6hm4` first diagnosed it as one — a coincidence
in the numbers: exchanging rows L+ and L- happens to symmetrise it).

The canonical rank is **5** — the trace-form radical of `qou/k4f8`,
which is also the unlabelled `lambda_0` in the proof's own spectrum.
"""
from __future__ import annotations

import itertools
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import _path_bridge  # noqa: F401, E402
sys.path.insert(0, str(HERE.parent.parent / "tools" / "pyhecke" / "python"))

from q_parameter import HA, Q as q0  # noqa: E402
from pyhecke.gram import NF_BASIS, TR_M as CANON_TR_M, z as PG_Z  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q0_stamp import anchor_of_value, pin_value_for_anchor  # noqa: E402

NF_NAMES = ["gamma", "s0", "s1", "L+", "L-", "e-"]
GENS = [0, 1, -1, -2]                      # s0, s1, s0^-1, s1^-1
B3 = (0, -2, 0, -2, 0, -2)
MIRROR = (-1, 1, -1, 1, -1, 1)
NUCLEONS = (("proton", ["u", "u", "d"]), ("neutron", ["u", "d", "d"]))

# Verbatim from `computations/_deprecated/confinement-lp.py` so the
# comparison is against the same arithmetic, not a reimplementation.


def hecke_mul(t1, t2):
    r: dict = {}
    for w1, c1 in t1.items():
        for w2, c2 in t2.items():
            r[w1 + w2] = r.get(w1 + w2, 0.0) + c1 * c2
    return {w: c for w, c in r.items() if abs(c) > 1e-15}


def reduce_nf(terms):
    changed = True
    while changed:
        changed = False
        new: dict = {}
        for word, coeff in terms.items():
            if abs(coeff) < 1e-15:
                continue
            done = False
            for pos in range(len(word) - 1):
                if word[pos] == word[pos + 1]:
                    i = word[pos]
                    pre, suf = word[:pos], word[pos + 2:]
                    new[pre + (i,) + suf] = new.get(pre + (i,) + suf, 0.0) + coeff * HA
                    new[pre + suf] = new.get(pre + suf, 0.0) + coeff
                    done = changed = True
                    break
            if done:
                continue
            for pos in range(len(word) - 2):
                a, b, c = word[pos], word[pos + 1], word[pos + 2]
                if a == c and abs(a - b) == 1 and (b, a, b) < (a, b, a):
                    nw = word[:pos] + (b, a, b) + word[pos + 3:]
                    new[nw] = new.get(nw, 0.0) + coeff
                    done = changed = True
                    break
            if not done:
                new[word] = new.get(word, 0.0) + coeff
        terms = {w: c for w, c in new.items() if abs(c) > 1e-15}
    return terms


def to_vec(t):
    return np.array([t.get(b, 0.0) for b in NF_BASIS])


def expand_inverse(word):
    terms = {(): 1.0}
    for g in word:
        new: dict = {}
        if g >= 0:
            for w, c in terms.items():
                new[w + (g,)] = new.get(w + (g,), 0.0) + c
        else:
            i = -g - 1
            for w, c in terms.items():
                new[w + (i,)] = new.get(w + (i,), 0.0) + c
                new[w] = new.get(w, 0.0) - c * HA
        terms = {w: c for w, c in new.items() if abs(c) > 1e-15}
    return terms


def crossing(ti, tj, gen):
    if ti == tj == "u":
        return {(gen,): 1.0}
    if ti == tj == "d":
        return {(gen,): 1.0, (): -HA}
    return {(gen,): 1.0, (): -HA / 2}


def apply_typed_crossings(vec, types):
    elem = {NF_BASIS[i]: vec[i] for i in range(6) if abs(vec[i]) > 1e-15}
    for i in range(len(types)):
        for j in range(i + 1, len(types)):
            elem = reduce_nf(hecke_mul(elem, crossing(types[i], types[j],
                                                      min(min(i, j), 1))))
    return to_vec(elem)


def build_gram(trace_vec):
    G = np.zeros((6, 6))
    for i in range(6):
        for j in range(6):
            v = to_vec(reduce_nf(hecke_mul({NF_BASIS[i]: 1.0},
                                           {NF_BASIS[j]: 1.0})))
            G[i, j] = float(v @ trace_vec)
    return G


def wstr(w):
    return "".join(f"s{abs(g)-1 if g < 0 else g}{'^-1' if g < 0 else ''}"
                   for g in w)


def gram_check():
    stale = np.array([1.0, PG_Z, PG_Z, PG_Z ** 2, PG_Z ** 2, PG_Z ** 3])
    canon = np.array(CANON_TR_M, dtype=float)
    out = {}
    for label, tv in (("stale_power_rule", stale), ("canonical_TR_M", canon)):
        G = build_gram(tv)
        ev = np.sort(np.linalg.eigvals(G).real)
        out[label] = {
            "trace_vector": [repr(float(x)) for x in tv],
            "max_abs_asymmetry": repr(float(abs(G - G.T).max())),
            "eigenvalues": [repr(float(x)) for x in ev],
            "det": repr(float(np.linalg.det(G))),
            "rank": int(np.linalg.matrix_rank(G)),
        }
    return out


def enumerate_words():
    b3_vec = to_vec(reduce_nf(expand_inverse(B3)))
    words = [w for L in range(1, 7) for w in itertools.product(GENS, repeat=L)]
    out = {}
    for name, types in NUCLEONS:
        target = float(sum(apply_typed_crossings(b3_vec, types)))
        rows = []
        for w in words:
            v = to_vec(reduce_nf(expand_inverse(w)))
            d = abs(float(sum(apply_typed_crossings(v, types))) - target)
            rows.append((d, len(w), w))
        rows.sort(key=lambda r: r[0])
        rank = {w: i for i, (_, _, w) in enumerate(rows, 1)}
        out[name] = {
            "target_net_from_B3": repr(target),
            "n_words": len(rows),
            "n_delta_le_1e-9": sum(1 for d, _, _ in rows if d <= 1e-9),
            "n_delta_le_0.01": sum(1 for d, _, _ in rows if d <= 0.01),
            "n_odd_length_delta_le_0.01":
                sum(1 for d, L, _ in rows if L % 2 and d <= 0.01),
            "n_delta_le_0.01_within_original_lengths_2_4_6":
                sum(1 for d, L, _ in rows if L in (2, 4, 6) and d <= 0.01),
            "B3_rank": rank[B3],
            "B3_delta": repr(rows[rank[B3] - 1][0]),
            "mirror_rank": rank[MIRROR],
            "mirror_delta": repr(rows[rank[MIRROR] - 1][0]),
            "top_12": [{"rank": i, "delta": repr(d), "length": L,
                        "word": wstr(w)}
                       for i, (d, L, w) in enumerate(rows[:12], 1)],
        }
    return out


def main() -> int:
    print(f"q0 = {q0:.10f}   HA = {HA:.10f}")
    gram = gram_check()
    for k, v in gram.items():
        print(f"\n{k}: max|G-G^T| = {v['max_abs_asymmetry']}  rank {v['rank']}")
        print(f"  eig {v['eigenvalues']}")
    enum = enumerate_words()
    for name, r in enum.items():
        print(f"\n{name}: {r['n_words']} words, target {r['target_net_from_B3']}")
        print(f"  |d| <= 0.01: {r['n_delta_le_0.01']}   "
              f"odd-length among them: {r['n_odd_length_delta_le_0.01']}   "
              f"within lengths 2/4/6: "
              f"{r['n_delta_le_0.01_within_original_lengths_2_4_6']}")
        print(f"  B3 rank {r['B3_rank']}   mirror rank {r['mirror_rank']} "
              f"(delta {r['mirror_delta']})")
        for e in r["top_12"][:6]:
            print(f"    {e['rank']:>3} {e['delta']:>22}  len {e['length']}  "
                  f"{e['word']}")

    w = WitnessBuilder("confinement-b3-enumeration-recheck-probe",
                       engine="numpy")
    w.set_content_block("prf:confinement-topological")
    w.set_description(
        "Live re-run of prf:confinement-topological part (iii), whose cited "
        "witness (confinement-lp.witness.json) is deprecated. Enumerates all "
        "5460 braid words of length 1..6 over {s0, s1, s0^-1, s1^-1} — the "
        "original producer covered only lengths 2, 4, 6 despite the prose "
        "claiming 'all shorter words'. Result: 'all other words have |dnet| > "
        "0.01' is FALSE (382 proton / 167 neutron words are at or under "
        "0.01), the mirror is NOT the runner-up (rank 12 / rank 111 of 5460), "
        "and B_3's |dnet| = 0 is circular — the producer defines target_net "
        "as B_3's own confined net. |dnet| is trace-independent, so the stale "
        "tr_M that got the old witness deprecated does not affect any of "
        "this. Also reproduces the old Gram's asymmetry from that single "
        "stale entry tr_M(e^-) = z^3 rather than h z^2 + z."
    )
    for name, r in enum.items():
        w.add_assertion(f"all_others_above_0.01_is_false[{name}]",
                        computed=str(r["n_delta_le_0.01"] > 1), expected="True")
        w.add_assertion(f"mirror_is_not_runner_up[{name}]",
                        computed=str(r["mirror_rank"] > 2), expected="True")
        w.add_assertion(f"odd_lengths_were_unchecked_and_score[{name}]",
                        computed=str(r["n_odd_length_delta_le_0.01"] > 0),
                        expected="True")
        w.add_assertion(f"claim_false_within_original_lengths[{name}]",
                        computed=str(
                            r["n_delta_le_0.01_within_original_lengths_2_4_6"] > 1),
                        expected="True")
    w.add_assertion("stale_trace_makes_gram_asymmetric",
                    computed=str(float(
                        gram["stale_power_rule"]["max_abs_asymmetry"]) > 1e-9),
                    expected="True")
    w.add_assertion("canonical_trace_gram_is_symmetric_and_rank_5",
                    computed=str(
                        float(gram["canonical_TR_M"]["max_abs_asymmetry"]) < 1e-12
                        and gram["canonical_TR_M"]["rank"] == 5),
                    expected="True")
    w.add_parameter("generators", ["s0", "s1", "s0^-1", "s1^-1"])
    w.add_parameter("lengths_enumerated", list(range(1, 7)))
    w.add_parameter("lengths_enumerated_by_original", [2, 4, 6])
    w.add_data("enumeration", enum)
    w.add_data("gram_check", gram)
    w.add_caveat(
        "|dnet| is the distance to B_3's own confined net, which is how the "
        "deprecated producer defined the target. This probe keeps that "
        "definition so the comparison is like-for-like; it is not an "
        "endorsement of the metric. Under it, B_3 scoring 0 is a tautology."
    )
    w.add_caveat(
        "Refutes part (iii) as stated. It does NOT show B_3 is the wrong "
        "confinement operator — only that this enumeration does not select "
        "it. A selection argument needs a metric not defined from the answer."
    )
    # Read the anchor off the q0 THIS RUN computed with, never off a literal.
    # The literal that used to sit here said "proton" -- true of the default
    # this stem resolves to, and false of the run that actually produced the
    # committed witness, which had QOU_Q0_ANCHOR=ideal set for the cross-check
    # below. The witness went out labelled proton carrying the muon value, and
    # nothing could catch it: a hardcoded label cannot disagree with itself.
    # `q0_anchor_consistency_audit` scored it Q0_FLIP. Bean `qou/ftuv`.
    anchor = anchor_of_value(q0)
    stamp = {
        "q0AnchorReason": (
            "HA = q - 1/q enters |dnet| through `crossing` and `reduce_nf`, so "
            "the values are anchor-dependent, and this field reports the pin "
            "the run used rather than the one the stem defaults to. Unset, "
            "the stem resolves to `proton` -- the q_parameter runtime default "
            "and the same one the deprecated producer ran under. The "
            "CONCLUSIONS are not anchor-dependent. Measured, not assumed: "
            "re-run under QOU_Q0_ANCHOR=ideal every count is identical "
            "(proton 382 / 195 / 187, neutron 167 / 28 / 139), B_3 stays rank "
            "1 and the proton mirror stays rank 12; the neutron mirror moves "
            "111 -> 109 within a tie cluster. Each figure refuting part (iii) "
            "survives both anchors."),
    }
    # An unrecognised q0 stays UNSTAMPED on purpose: Q0_ANCHOR_MISSING is a
    # tolerated, visible state; a guessed pin is a silent wrong one.
    #
    # `q0Value` is declared HERE, not left to the builder. `WitnessBuilder`
    # stamps it only inside its `if "q0Anchor" not in payload` branch, so a
    # producer that states the anchor itself gets no value -- and the
    # preserve-forward step then fills it from the PREVIOUS witness. That is
    # what produced the Q0_FLIP: this run resolves proton, the file on disk
    # still held the muon value from the QOU_Q0_ANCHOR=ideal cross-check, and
    # the two were written side by side. Declaring both closes the gap.
    if anchor is not None:
        stamp["q0Anchor"] = anchor
        pin = pin_value_for_anchor(anchor)
        if pin is not None:
            stamp["q0Value"] = pin
    path = w.save(stamp)
    print(f"\nWrote {Path(path).name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
