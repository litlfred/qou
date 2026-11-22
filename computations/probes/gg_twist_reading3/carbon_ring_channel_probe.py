#!/usr/bin/env python3
"""carbon_ring_channel_probe.py -- the convolution-flow channel expansion of the 6-carbon chain and ring.

Each bond is sigma^2. Under the convolution flow (ConvolutionFlowParity.lean) it splits into a Sym
and an Alt channel; in the Temperley-Lieb bracket, sigma^2 = A^2 * 1 + (1 - A^-4) * e. Expanding
every bond gives 2^b channel states. For a state S (the bonds in the Alt channel), the
independent-bond value is the closure of a forest of cup-caps, d^(5 - |S|). This probe lists the
states whose closure differs from that value. Exact integer polynomials in A; no floats.

-- Ref: [leitner2026] bean qou-a1hh
"""
from __future__ import annotations

import itertools
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from tl_bracket import closure_loops, compose, egen, ident, padd, pmul, ppow, D_LOOP  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

N = 6


def br(items):
    state = {ident(N): {0: 1}}
    for it in items:
        new = defaultdict(dict)
        E = egen(it[1], N)
        if it[0] == "e":
            for D, c in state.items():
                D2, L = compose(D, E, N)
                new[D2] = padd(new[D2], pmul(c, ppow(D_LOOP, L)))
        else:
            a_id, a_e = (1, -1) if it[2] > 0 else (-1, 1)
            for D, c in state.items():
                new[D] = padd(new[D], pmul(c, {a_id: 1}))
                D2, L = compose(D, E, N)
                new[D2] = padd(new[D2], pmul(c, pmul({a_e: 1}, ppow(D_LOOP, L))))
        state = {D: c for D, c in new.items() if c}
    tot = {}
    for D, c in state.items():
        tot = padd(tot, pmul(c, ppow(D_LOOP, closure_loops(D, N) - 1)))
    return tot


def rho(front):
    return [("s", g, 1 if front else -1) for g in range(5)]


def inv(w):
    return [("s", g, -s) for _, g, s in reversed(w)]


def state_word(S, front):
    w = []
    for i in sorted(S):
        if i < 5:
            w.append(("e", i))
        else:
            r = rho(front)
            w += r + [("e", 4)] + inv(r)
    return w


def swap(g):
    D = list(ident(N))
    D[g], D[g + 1] = N + g + 1, N + g
    D[N + g], D[N + g + 1] = g + 1, g
    return tuple(D)


def components(items):
    D, L = ident(N), 0
    for it in items:
        D, l = compose(D, egen(it[1], N) if it[0] == "e" else swap(it[1]), N)
        L += l
    return L + closure_loops(D, N)


def jones_of_state(T):  # writhe of a state word is 0; A = t^(-1/4); exponents in quarter-powers of t
    return {f"{-k}/4": v for k, v in sorted(T.items(), reverse=True)}


def deviations(bonds, front):
    out = []
    for k in range(len(bonds) + 1):
        for S in itertools.combinations(bonds, k):
            T = br(state_word(S, front))
            if len(S) <= 5 and T == ppow(D_LOOP, 5 - len(S)):
                continue
            out.append({"alt_bonds": list(S), "components": components(state_word(S, front)),
                        "jones_t_exponent_over_4": jones_of_state(T)})
    return out


def main() -> int:
    alt = padd({0: 2}, pmul({-2: 1}, D_LOOP))
    chain = deviations(range(5), True)
    ring_f = deviations(range(6), True)
    ring_b = deviations(range(6), False)
    checks = [
        ("alt_coefficient_is_1_minus_A^-4", alt == {0: 1, -4: -1}, "sigma^2 = A^2 + (1 - A^-4) e"),
        ("chain_is_pure_convolution", chain == [], "all 32 chain states are forest-valued"),
        ("ring_one_nonconvolution_state_front", [d["alt_bonds"] for d in ring_f] == [list(range(6))],
         "only the all-Alt state deviates"),
        ("ring_one_nonconvolution_state_back", [d["alt_bonds"] for d in ring_b] == [list(range(6))],
         "same for the back closing band"),
    ]
    for n, ok, s in checks:
        print(("PASS " if ok else "FAIL ") + n, "-", s)
    print("ring front:", ring_f)
    print("ring back:", ring_b)
    wb = WitnessBuilder("carbon-ring-channel", engine="exact-integer", output_dir=HERE)
    for n, ok, s in checks:
        wb.add_assertion(n, computed="1" if ok else "0", expected="1", source=s)
    wb.save({
        "q0Anchor": "independent",
        "q0AnchorReason": "exact polynomial identity in A; no evaluation at q0",
        "description": "PROBE stage 5b (bean qou-a1hh): convolution-flow channel expansion of the 6-carbon "
                       "chain and ring. Nothing fitted or selected.",
        "sym_coefficient": "A^2", "alt_coefficient": "1 - A^-4",
        "chain_nonconvolution_states": chain,
        "ring_nonconvolution_states_front": ring_f,
        "ring_nonconvolution_states_back": ring_b,
    })
    return 0 if all(ok for _, ok, _ in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
