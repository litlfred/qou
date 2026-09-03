#!/usr/bin/env python3
"""Every order of the trace difference is a permutation count: the diagonal-insertion expansion.

Bean `qou-qqm4` (stage 2). Successor to the `c₁` derivation (`qou-pdg9`, PR #6492).

## The observation that makes ALL orders combinatorial

In the tensor picture (`tensor_picture_markov_trace_probe`), the Hecke generator
on an adjacent pair is EXACTLY

    Ř  =  s  +  Δ_R(q),      Δ_R = (q − 1)·(E₁₁ + E₂₂)  +  h·E₂₁,₂₁,   h = q − q⁻¹,

i.e. the transposition `s` plus a DIAGONAL operator that vanishes at `q = 1`
(this is `Ř e₁₁ = q e₁₁`, `Ř e₁₂ = e₂₁`, `Ř e₂₁ = e₁₂ + h e₂₁`, `Ř e₂₂ = q e₂₂`
rewritten). Every letter is therefore

    L_ℓ  =  s_{g_ℓ}  +  Δ_ℓ,     Δ_ℓ  =  Δ_R at pair g_ℓ  +  d_ℓ(q)·1      (diagonal, O(ε))

with `d_ℓ ∈ {0, −h, −h/2, −h(½ − δ/4)}`. Expanding the product over the word by
choosing, at each letter, either `s` or `Δ`:

    Tr(K·Π_ℓ L_ℓ)  =  Σ_{S ⊆ letters}  Σ_{b : P_S b = b}  K_b · Π_{ℓ ∈ S} Δ_ℓ(b at ℓ)         [◇]

where `P_S` is the product of the transpositions of the letters NOT in `S`,
the sum is over basis states `b` fixed by `P_S`, `K_b = q^{2·#down(b)}`, and
`Δ_ℓ(b at ℓ)` is the diagonal scalar of `Δ_ℓ` on the pair pattern the state
carries when it reaches letter `ℓ` (a diagonal insertion does not move the
state). Since every `Δ` is `O(ε)`, **order `ε^k` needs only `|S| ≤ k`**:

    [ε⁰]  =  |S| = 0                          →  2^{c(σ)}                              (the floor c₀)
    [ε¹]  =  |S| ≤ 1                          →  n·2^c + Σ_ℓ w_ℓ 2^{c(σ^{(ℓ)})}        (the c₁ formula [★])
    [ε²]  =  |S| ≤ 2                          →  … + Σ_{a<b} (pair terms)              (this probe)

after the normaliser `(1+q²)^{−n} = 2^{−n}(1 − nε + (n²/2)ε² − …)`. This is a
complete, exact, all-orders derivation of the Markov trace of a braid word as
a **fixed-point count over sub-words**, conditional only on the Schur–Weyl
identification [SW] (which the stage-1 probe verifies on the words themselves).

## What this probe does

1. Implements [◇] truncated at order `k` by propagating each basis state through
   the word with at most `k` diagonal insertions, carrying the scalar as an
   exact `ε`-polynomial (`Fraction` coefficients). Cost `2^n · C(L, ≤k)`.
2. Checks `[ε⁰], [ε¹], [ε²]` of `Δtr` against the exact series values for the
   six words (pp, pn, nn, T, ³He, ⁴He) — `Fraction ==`.
3. Splits `c₂` into its insertion classes `|S| = 0, 1, 2` (after the normaliser
   is folded in) and reports them per word, so the structure is visible.
4. Reports the second-order chain/atom ratios exactly.

## What is NOT claimed

No closed form in `(Z, N)` for `c₂` is asserted here; the class split is the
raw material for one. Nothing is fitted; no scale enters; nothing at `q₀`.
"""
from __future__ import annotations

import importlib.util
import sys
import time
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "hecke"), str(_COMP / "markov"),
           str(_COMP / "substrate"), str(_COMP / "habiro")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge as _bridge  # noqa: E402, F401

from canonical_braid_crossings import atom_canonical_crossings  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "c1probe", _HERE / "c1_leading_coefficient_derived_probe.py")
_c1 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_c1)


# ═══════════════════════════════════════════════════════════════════════════
#  exact ε-polynomials (truncated at order K) — plain lists, no valuation needed
# ═══════════════════════════════════════════════════════════════════════════
def pmul(a: list, b: list, K: int) -> list:
    out = [F(0)] * (K + 1)
    for i, x in enumerate(a):
        if x == 0:
            continue
        for j, y in enumerate(b):
            if i + j > K:
                break
            out[i + j] += x * y
    return out


def padd(a: list, b: list) -> list:
    return [x + y for x, y in zip(a, b)]


def series_h(K: int) -> list:
    """h = q − 1/q = (1+ε) − (1+ε)^{-1} = 2ε − ε² + ε³ − …"""
    out = [F(0)] * (K + 1)
    for k in range(1, K + 1):
        out[k] = F(2) if k == 1 else F((-1) ** (k + 1))
    return out


def series_delta(K: int) -> list:
    """δ = (q−1)²(1 − q⁻⁴)/3 = ε²(1 − (1+ε)^{-4})/3 = (4/3)ε³ − (10/3)ε⁴ + … """
    inv4 = [F(0)] * (K + 1)          # (1+ε)^{-4} = Σ (-1)^k C(k+3,3) ε^k
    for k in range(K + 1):
        c = 1
        for j in range(1, 4):
            c = c * (k + j) // j
        inv4[k] = F((-1) ** k * c)
    one_minus = [F(1) - inv4[0]] + [-x for x in inv4[1:]]
    out = [F(0)] * (K + 1)
    for k in range(K + 1):
        if k + 2 <= K:
            out[k + 2] = one_minus[k] / 3
    return out


def letter_d_series(kind: str, K: int) -> list:
    h = series_h(K)
    if kind == "sigma":
        return [F(0)] * (K + 1)
    if kind == "sigma_inv":
        return [-x for x in h]
    if kind == "averaged":
        return [-x / 2 for x in h]
    if kind == "averaged_weighted":
        # d = −h·(1/2 − δ/4), δ = (q−1)²(1−q⁻⁴)/3 = O(ε³)
        dl = series_delta(K)
        fac = padd([F(1, 2)] + [F(0)] * K, [-x / 4 for x in dl])
        return [-x for x in pmul(h, fac, K)]
    raise ValueError(kind)


# ═══════════════════════════════════════════════════════════════════════════
#  the insertion expansion [◇]
# ═══════════════════════════════════════════════════════════════════════════
def pattern_scalar(b: int, g: int, eps_series: list, h: list, d: list, K: int) -> list:
    """Δ_ℓ(b at pair g): (q−1) on e11/e22, h on e21, 0 on e12, plus d."""
    bg, bg1 = (b >> g) & 1, (b >> (g + 1)) & 1
    if bg == bg1:
        return padd(eps_series, d)
    if bg == 1 and bg1 == 0:          # e21: site g down, site g+1 up  (h placed on e21)
        return padd(h, d)
    return list(d)                    # e12


def trace_expansion(Z: int, N: int, include_inter: bool, K: int, *, log=None) -> tuple[list, dict]:
    """Return [ε^k] of tr_M(word) for k ≤ K, and the split by insertion class |S|
    (before the normaliser is applied the classes are reported raw; after, per k)."""
    n = 3 * (Z + N)
    crossings = atom_canonical_crossings(Z, N, include_inter=include_inter)
    L = len(crossings)
    gens = [g for g, _ in crossings]
    d_ser = [letter_d_series(kind, K) for _, kind in crossings]
    eps_series = [F(0), F(1)] + [F(0)] * (K - 1)
    h = series_h(K)
    # K_b = (1+ε)^{2m}, m = #down: series
    kpow = {}
    for m in range(n + 1):
        s = [F(1)] + [F(0)] * K
        base = [F(1), F(2), F(1)] + [F(0)] * (K - 2) if K >= 2 else [F(1), F(2)]
        for _ in range(m):
            s = pmul(s, base, K)
        kpow[m] = s
    # normaliser (1+q²)^{-n} = 2^{-n} (1 + ε + ε²/2)^{-n}
    u = [F(0), F(1), F(1, 2)] + [F(0)] * (K - 2) if K >= 2 else [F(0), F(1)]
    inv = [F(1)] + [F(0)] * K           # (1+u)^{-n} = Σ_j C(-n, j) u^j
    upow = [F(1)] + [F(0)] * K
    coef = F(1)
    for j in range(1, K + 1):
        upow = pmul(upow, u, K)
        coef = coef * F(-n - j + 1) / j
        inv = padd(inv, [coef * x for x in upow])
    norm = [x / F(2) ** n for x in inv]

    raw_by_class = {k: [F(0)] * (K + 1) for k in range(K + 1)}
    t0 = time.time()
    # letters are applied as in chi_at: reversed(factors) acting on the vector, so
    # the state passes letters L-1, L-2, …, 0 in that order.
    order = list(range(L - 1, -1, -1))
    for b in range(1 << n):
        kb = kpow[bin(b).count("1")]
        for size in range(K + 1):
            for S in combinations(range(L), size):
                Sset = set(S)
                state, scal = b, [F(1)] + [F(0)] * K
                for idx in order:
                    g = gens[idx]
                    if idx in Sset:
                        scal = pmul(scal, pattern_scalar(state, g, eps_series, h, d_ser[idx], K), K)
                    else:
                        m_g, m_g1 = 1 << g, 1 << (g + 1)
                        if ((state >> g) & 1) != ((state >> (g + 1)) & 1):
                            state ^= (m_g | m_g1)
                if state == b:
                    raw_by_class[size] = padd(raw_by_class[size], pmul(kb, scal, K))
        if log and b and b % 512 == 0:
            log(f"      {b}/{1 << n} basis states, {time.time()-t0:.0f}s")
    total_raw = [F(0)] * (K + 1)
    for s in raw_by_class.values():
        total_raw = padd(total_raw, s)
    coeffs = pmul(total_raw, norm, K)
    by_class = {size: pmul(raw_by_class[size], norm, K) for size in raw_by_class}
    return coeffs, by_class


RECORDED_C1 = {"pp": F(19, 8), "pn": F(37, 16), "nn": F(9, 4),
               "T": F(163, 64), "3He": F(85, 32), "4He": F(259, 128)}
EXACT_C2 = {"pp": F(357, 32), "pn": F(403, 32), "nn": F(217, 16),
            "T": F(3285, 128), "3He": F(3451, 128), "4He": F(15307, 512)}
CASES = [("pp", (2, 0)), ("pn", (1, 1)), ("nn", (0, 2)),
         ("T", (1, 2)), ("3He", (2, 1)), ("4He", (2, 2))]


def main() -> int:
    T0 = time.time()

    def log(msg):
        print(f"  [{time.time()-T0:7.1f}s] {msg}", flush=True)

    K = 2
    w = WitnessBuilder("c2-diagonal-insertion-expansion-probe")
    w.set_description(
        "The Hecke generator in the tensor picture is EXACTLY a transposition plus a diagonal "
        "O(eps) operator, so the Markov trace of a braid word expands as a sum over subsets S of "
        "letters of fixed-point counts of the sub-word with S deleted, weighted by pattern scalars; "
        "order eps^k needs |S| <= k. Implements the expansion to order 2, reproduces c0, c1 and the "
        "exact c2 of all six words, and splits c2 by insertion class."
    )

    print("=" * 78)
    print("  The diagonal-insertion expansion: c0, c1, c2 as fixed-point counts")
    print("=" * 78)

    rows, ok0, ok1, ok2 = [], True, True, True
    for name, (Z, N) in CASES:
        A = Z + N
        log(f"{name} (Z={Z},N={N}, n={3*A}) …")
        cf, cls_f = trace_expansion(Z, N, False, K, log=log if A >= 4 else None)
        ca, cls_a = trace_expansion(Z, N, True, K, log=log if A >= 4 else None)
        d = [x - y for x, y in zip(cf, ca)]
        a0, a1, a2 = d[0], d[1], d[2]
        c0 = _c1.c0_derived(A)
        c1, c2 = a1, a1 + a2
        cls = {s: [x - y for x, y in zip(cls_f[s], cls_a[s])] for s in cls_f}
        # c2 by class: c2 = [ε¹] + [ε²]; attribute each by class
        c2_by_class = {s: cls[s][1] + cls[s][2] for s in cls}
        o0, o1, o2 = (a0 == c0), (c1 == RECORDED_C1[name]), (c2 == EXACT_C2[name])
        ok0 &= o0; ok1 &= o1; ok2 &= o2
        rows.append({"case": name, "A": A, "a0": str(a0), "c0_derived": str(c0), "a0_ok": o0,
                     "c1": str(c1), "c1_recorded": str(RECORDED_C1[name]), "c1_ok": o1,
                     "c2": str(c2), "c2_exact_series": str(EXACT_C2[name]), "c2_ok": o2,
                     "c2_by_insertion_class": {str(s): str(v) for s, v in c2_by_class.items()},
                     "eps2_coefficient_a2": str(a2)})
        log(f"    a0={a0} ({o0})  c1={c1} ({o1})  c2={c2} ({o2})  "
            f"c2 by |S|: {{{', '.join(f'{s}: {v}' for s, v in c2_by_class.items())}}}")

    w.add_assertion("insertion_expansion_order0_equals_derived_floor",
                    computed="1" if ok0 else "0", expected="1",
                    source="[ε⁰] of the |S|=0 class vs 2^-A - 2^(1-2A), six words, Fraction ==.")
    w.add_assertion("insertion_expansion_order1_equals_c1",
                    computed="1" if ok1 else "0", expected="1",
                    source="[ε¹] (|S| ≤ 1, normaliser folded) vs the six derived/recorded c1 values.")
    w.add_assertion("insertion_expansion_order2_equals_exact_series_c2",
                    computed="1" if ok2 else "0", expected="1",
                    source="[ε¹]+[ε²] (|S| ≤ 2) vs the exact series c2 from "
                           "c1_leading_coefficient_derived_probe (4He: 15307/512 from the order-4 "
                           "run). Fraction == on all six. This is the derivation of c2: a "
                           "fixed-point count over sub-words with ≤ 2 letters deleted, weighted by "
                           "the diagonal pattern scalars (q−1 on e11/e22, h on e21, d_ℓ).")

    # second-order chain/atom ratios, exact
    chain = {"T": EXACT_C2["pn"] + EXACT_C2["nn"], "3He": EXACT_C2["pp"] + EXACT_C2["pn"],
             "4He": EXACT_C2["pp"] + EXACT_C2["pn"] + EXACT_C2["nn"]}
    ratios = {k: chain[k] / EXACT_C2[k] for k in chain}
    first = {"T": F(292, 163), "3He": F(30, 17), "4He": F(24, 7)}
    # `ratio` and `first_order` are the exact Fractions as strings. There was a
    # `"float": float(v)` twin beside each; it is dropped, not reformatted. The
    # twin carried no information the exact string does not — it was the SAME
    # rational rounded to a double — and the three of them were the whole of
    # this witness's raw-float64 count. Nothing in the tree reads the field.
    w.add_data("second_order_chain_over_atom", {k: {"ratio": str(v),
                                                    "first_order": str(first[k])} for k, v in ratios.items()})
    w.add_assertion("second_order_overcount_is_smaller_than_first_order_at_every_A3_A4",
                    computed="1" if all(abs(ratios[k] - 1) < abs(first[k] - 1) for k in ratios) else "0",
                    expected="1",
                    source="|chain/atom − 1| at second order vs first order: "
                           + ", ".join(f"{k}: {float(ratios[k]):.4f} vs {float(first[k]):.4f}" for k in ratios)
                           + ". Smaller in every case, but NOT uniformly ≈ 1 (4He 1.248): the "
                             "leading-order over-count is partly cancelled one order up, not removed.")
    w.add_data("rows", rows)
    w.add_data("verdict", (
        "c2 is DERIVED by the same mechanism as c0 and c1, one insertion deeper. The Hecke "
        "generator is exactly s + (diagonal, O(eps)), so the trace of any word at any order is a "
        "weighted fixed-point count over sub-words; order k needs at most k deletions. Conditional "
        "only on the Schur-Weyl identification, which the stage-1 probe checks on these words."
    ))
    out = w.save()
    print(f"\n  witness -> {out}")
    ok = ok0 and ok1 and ok2
    print(f"  ALL PASSED: {ok}   ({time.time()-T0:.0f}s)")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
