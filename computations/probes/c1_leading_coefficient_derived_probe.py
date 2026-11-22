#!/usr/bin/env python3
"""The leading `ℏ_q` coefficient `c₁` of the trace difference — EXACT, then DERIVED.

Bean `qou-pdg9`, successor to `qou-zrx2`; re-derived under the Borromean ruling in `qou-j1e5`.

WHAT THIS REPLACES
------------------
`binding_chain_floor_corrected_probe` measured the leading coefficient
`c₁ = lim (Δtr − c₀(A))/ℏ_q` of `Δtr = tr_M(W_free) − tr_M(W_atom)` by Richardson
extrapolation and matched each to a rational with denominator ≤ 4096:

    borromean (current):   pp 1/8    pn 1/16   nn 0     T 1/64    ³He 1/8    ⁴He 7/128
    grouped (superseded):  pp 19/8   pn 37/16  nn 9/4   T 163/64  ³He 85/32  ⁴He 259/128

Those six numbers entered `QOU/MassTheory/PairwiseChainLeadingOrder.lean` as
**definitions**, flagged as measurements. This probe does two things to them.

PART A — EXACT, BY SERIES ARITHMETIC (no extrapolation)
-------------------------------------------------------
`exact_rational_chi_gauge_probe` evaluates `χ^λ` in exact `Fraction` arithmetic at
any rational `q` via the trace-invariant asymmetric seminormal gauge (no square
root), and is validated 11/11 against the cached deuteron characters. Its
functions are duck-typed on `+ − × ÷ **`. Run over **truncated power series in
`ε = q − 1`** instead of `Fraction`, the same code returns `χ^λ(1+ε)` as an
exact series, and with the symbolic convention-D weights `y_λ(q)`
(`wedderburn_jones_markov.y_lambda_at`, rational in `q`, two-row cap exact) the
Markov trace follows as an exact series. Then

    Δtr(1+ε) = a₀ + a₁ ε + a₂ ε² + …      exactly, as Fractions

and since `ℏ_q = 1 − 1/q = ε/(1+ε)`, i.e. `ε = ℏ_q + ℏ_q² + …`,

    c₀ = a₀        c₁ = a₁        c₂ = a₁ + a₂ .

No Richardson, no `limit_denominator`, no float anywhere.

PART B — DERIVED, BY A PERMUTATION COUNT (the same route as c₀)
----------------------------------------------------------------
By quantum Schur–Weyl the convention-D Markov trace is the normalised quantum
trace on `(ℂ²)^{⊗n}`: `tr_M(x) = Tr(K·ρ(x)) / (1+q²)^n` with `K = diag(1,q²)^{⊗n}`
(check: `Tr K = (1+q²)^n = Z(n)`, `Σ_λ s_λ(1,q²)χ^λ = Tr(K·)`, and the weights
printed by `y_lambda_at(6)` are exactly `s_λ(1,q²)/(1+q²)^6`). Every letter is
`L_ℓ = σ_g + d_ℓ(q)·1` with `d_ℓ ∈ {0, −h, −h/2, −h(½ − δ/4)}`, `h = q − q⁻¹`.

Expand at `q = 1 + ε`, where each letter degenerates to the transposition `s_g`:

  1. **The generator's first-order term is `1 + Y`, with `Y` anticommuting with
     `s_g`.** Write `σ = s + εX + O(ε²)`. The Hecke relation `σ² = hσ + 1` with
     `h = 2ε + O(ε²)` and `s² = 1` gives `sX + Xs = 2s`, so `X = 1 + Y` with
     `sY = −Ys`. (Lean: `QOU.MassTheory.HeckeFirstOrderDeformation`.)
  2. **`Tr(Y·P) = 0` for every permutation `P`.** `Y` is supported on the
     `(e₁₂, e₂₁)` sector of factors `(g, g+1)`, is traceless there, and its two
     off-diagonal entries are opposite; the global spin flip `e₁ ↔ e₂` commutes
     with every permutation and swaps the two sectors, so the fixed-point and
     swapped-point sums cancel pairwise.
  3. **The `K′` term cancels the normaliser's.** `K′ = 2·N_down`, and
     `Tr(N_down·P) = n·2^{c(P)−1}`, so `Tr(K′P) = n·2^{c(P)}`; while
     `(1+q²)^{−n} = 2^{−n}(1 − nε + …)`. The two `n·2^{c}` terms cancel.
  4. **Each letter's own first-order term is the scalar `1 + d′_ℓ(0)`,** and
     `d′(0) ∈ {0, −2, −1, −1}` for `{σ, σ⁻¹, averaged, averaged_weighted}` — the
     colour weight `δ = (q−1)²(1−q⁻⁴)/3 = O(ε³)` is invisible at this order.

Therefore

    d tr_M / dε |₀  =  2^{−n} · Σ_ℓ w_ℓ · 2^{c(σ^{(ℓ)})}          [★]

    w_ℓ = +1 (σ),  −1 (σ⁻¹),  0 (either averaged letter);
    σ^{(ℓ)} = the permutation of the word with letter ℓ DELETED.

and `c₁ = [★](free) − [★](atom)`. This is a pure permutation count — no Hecke
algebra, no trace evaluation — and it runs to `A = 20` for free, exactly as
the `c₀` derivation did.

WHAT IS CHECKED
---------------
* Part A's `ε⁰` reproduces the DERIVED floor `c₀(A) = 2^{−A} − 2^{1−2A}` for all
  six cases — an independent re-derivation of `ClassicalTraceFloor` by a
  completely different computation (seminormal series vs cycle counting).
* Part A's `ε¹` equals the six recorded rationals EXACTLY (`Fraction ==`).
* Part B [★] equals Part A's `ε¹` EXACTLY for all six — the derivation, tested.
* The exact-`Fraction` pipeline at `q = 8/7` agrees with the production
  transfer kernel `tr_m_atom_zn(q=8/7)` at 50 dps — ties this pipeline to the
  witness path the six measurements came from.
* Colour-blind vs colour-weighted p-n factor give identical `ε¹, ε², ε³` for the
  deuteron and first differ at `ε⁴` — step 4 above, measured.

Part B then tabulates `c₁` for every `(Z, N)` with `A = 2 … 20`.

Precision: `fractions.Fraction` end to end in Parts A and B; mpmath only in the
transfer-kernel cross-check. No float enters any computed value. Proton-pin
irrelevant: nothing here is evaluated at `q₀`.

Usage:
    python3 -u computations/probes/c1_leading_coefficient_derived_probe.py 2>&1 | tee /tmp/c1.log
"""
from __future__ import annotations

import importlib.util
import sys
import time
from fractions import Fraction as F
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "hecke"), str(_COMP / "markov"),
           str(_COMP / "substrate"), str(_COMP / "habiro")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge as _bridge  # noqa: E402, F401
import sympy as sp  # noqa: E402
import mpmath as mp  # noqa: E402

from canonical_braid_crossings import atom_canonical_crossings, CTYPES  # noqa: E402
from wedderburn_jones_markov import y_lambda_at, Q_SYM  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

# the validated exact-Fraction seminormal pipeline, reused verbatim
_spec = importlib.util.spec_from_file_location(
    "erc", _HERE / "exact_rational_chi_gauge_probe.py")
_erc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_erc)
blocks_at, chi_at, factors_for = _erc.blocks_at, _erc.chi_at, _erc.factors_for

BIG = 10 ** 9   # "exact" absolute precision for constants


# ═══════════════════════════════════════════════════════════════════════════
#  Truncated Laurent series in ε with Fraction coefficients + valuation
# ═══════════════════════════════════════════════════════════════════════════
class Ser:
    """`Σ_{k≥v} c_k ε^k`, known exactly for `k < p`. Zero has `v = None`.

    The seminormal entries `h/(1 − q^{−2ρ})` are 0/0 at `ε = 0`; tracking the
    valuation `v` and absolute precision `p` makes those quotients exact rather
    than a special case. Precision bookkeeping: products `p = min(v₁+p₂, v₂+p₁)`,
    sums `p = min(p₁, p₂)`, inverse `(v, p) ↦ (−v, p − 2v)`.
    """
    __slots__ = ("v", "c", "p")

    def __init__(self, v, c, p):
        # normalise: strip leading zeros
        while c and c[0] == 0:
            c = c[1:]
            v += 1
        if not c or v >= p:
            self.v, self.c, self.p = None, [], p
        else:
            self.v, self.c, self.p = v, [F(x) for x in c[: p - v]], p

    # ---- constructors ------------------------------------------------------
    @staticmethod
    def const(x) -> "Ser":
        return Ser(0, [F(x)], BIG)

    @staticmethod
    def eps(P: int) -> "Ser":          # the variable q = 1 + ε, exact to order P
        return Ser(0, [F(1), F(1)], P)

    @staticmethod
    def _lift(x) -> "Ser":
        return x if isinstance(x, Ser) else Ser.const(x)

    # ---- access ------------------------------------------------------------
    def coeff(self, k: int) -> F:
        if k >= self.p:
            raise ValueError(f"coefficient ε^{k} not known (precision {self.p})")
        if self.v is None or k < self.v or k - self.v >= len(self.c):
            return F(0)
        return self.c[k - self.v]

    def is_zero(self) -> bool:
        return self.v is None

    # ---- arithmetic --------------------------------------------------------
    def __add__(self, o):
        o = Ser._lift(o)
        p = min(self.p, o.p)
        if self.v is None:
            return Ser(o.v if o.v is not None else 0, list(o.c), p)
        if o.v is None:
            return Ser(self.v, list(self.c), p)
        v = min(self.v, o.v)
        # coefficients are structurally zero past each operand's stored list,
        # so never allocate past the longer one (an exact constant has p = BIG).
        n = min(p - v, max(self.v + len(self.c), o.v + len(o.c)) - v)
        c = [F(0)] * max(n, 0)
        for s in (self, o):
            for i, x in enumerate(s.c):
                k = s.v + i - v
                if k < n:
                    c[k] += x
        return Ser(v, c, p)

    __radd__ = __add__

    def __neg__(self):
        return Ser(self.v if self.v is not None else 0, [-x for x in self.c], self.p)

    def __sub__(self, o):
        return self + (-Ser._lift(o))

    def __rsub__(self, o):
        return Ser._lift(o) + (-self)

    def __mul__(self, o):
        o = Ser._lift(o)
        if self.v is None or o.v is None:
            # 0 × (anything): precision of the product is v_other + p_zero-ish;
            # a zero known to precision p times a series of valuation v is zero
            # to precision p + v.
            pz = self.p if self.v is None else o.p
            vo = o.v if self.v is None else self.v
            return Ser(0, [], pz + (vo if vo is not None else 0))
        v = self.v + o.v
        p = min(self.v + o.p, o.v + self.p)
        # a product of two stored lists has at most la + lb - 1 nonzero terms;
        # two exact constants would otherwise ask for p - v = 1e9 of them.
        n = min(p - v, len(self.c) + len(o.c) - 1)
        c = [F(0)] * max(n, 0)
        for i, x in enumerate(self.c):
            if i >= n:
                break
            for j, y in enumerate(o.c):
                if i + j >= n:
                    break
                c[i + j] += x * y
        return Ser(v, c, p)

    __rmul__ = __mul__

    def inv(self) -> "Ser":
        if self.v is None:
            raise ZeroDivisionError("series is zero to working precision")
        if self.p >= BIG:
            # an exact scalar (the only exact objects that arise are constants);
            # its inverse is exact. Without this branch `n` below would be 1e9
            # and the list allocation OOM-kills the process (measured: exit 137).
            if len(self.c) != 1:
                raise ValueError("exact non-constant series cannot be inverted")
            return Ser(-self.v, [1 / self.c[0]], BIG)
        # self = ε^v · u, u = c0 + c1 ε + …, unit part inverted by recursion
        n = self.p - self.v              # number of known coefficients of u
        u = self.c + [F(0)] * (n - len(self.c))
        inv = [F(0)] * n
        inv[0] = 1 / u[0]
        for k in range(1, n):
            s = F(0)
            for j in range(1, k + 1):
                s += u[j] * inv[k - j]
            inv[k] = -s * inv[0]
        return Ser(-self.v, inv, self.p - 2 * self.v)

    def __truediv__(self, o):
        return self * Ser._lift(o).inv()

    def __rtruediv__(self, o):
        return Ser._lift(o) * self.inv()

    def __pow__(self, k: int):
        if k < 0:
            return self.inv() ** (-k)
        out = Ser.const(1)
        base = self
        while k:
            if k & 1:
                out = out * base
            base = base * base
            k >>= 1
        return out

    def __eq__(self, o):   # only used by the pipeline's `x == 0`-style tests
        o = Ser._lift(o)
        return self.v == o.v and self.c == o.c

    def __repr__(self):
        if self.v is None:
            return f"Ser(0; p={self.p})"
        return "Ser(" + " + ".join(f"({x})ε^{self.v + i}" for i, x in enumerate(self.c)) + f"; p={self.p})"


# ═══════════════════════════════════════════════════════════════════════════
#  helpers
# ═══════════════════════════════════════════════════════════════════════════
def two_row_partitions(n: int) -> list[list[int]]:
    return [[n - k, k] if k else [n] for k in range(0, n // 2 + 1)]


def y_lambda_series(n: int, P: int) -> tuple[dict, list]:
    """Convention-D weights as ε-series for the two-row partitions; also the
    list of ≥3-row partitions whose symbolic weight is NOT identically zero
    (expected empty — the row cap)."""
    y = y_lambda_at(n)
    e = sp.Symbol("e")
    out, bad = {}, []
    for lam, expr in y.items():
        if len(lam) > 2:
            if sp.simplify(expr) != 0:
                bad.append(list(lam))
            continue
        ser = sp.series(sp.together(expr).subs(Q_SYM, 1 + e), e, 0, P).removeO()
        poly = sp.Poly(sp.expand(ser), e)
        coeffs = [F(0)] * P
        for (k,), cval in poly.terms():
            if k < P:
                coeffs[k] = F(int(cval.p), int(cval.q))
        out[tuple(lam)] = Ser(0, coeffs, P)
    return out, bad


def tr_M_series(Z: int, N: int, include_inter: bool, P: int, *,
                colour_weighted: bool = True, log=None) -> Ser:
    n = 3 * (Z + N)
    q = Ser.eps(P)
    crossings = atom_canonical_crossings(Z, N, include_inter=include_inter)
    facs = factors_for(crossings, q, colour_weighted=colour_weighted)
    ys, _ = y_lambda_series(n, P)
    tot = Ser.const(0)
    for lam in two_row_partitions(n):
        t0 = time.time()
        chi = chi_at(lam, facs, q)
        tot = tot + ys[tuple(lam)] * chi
        if log:
            log(f"      λ={lam} dim={len(_erc.syts(lam))}  {time.time()-t0:.1f}s")
    return tot


def tr_M_fraction(Z: int, N: int, include_inter: bool, qv: F) -> F:
    """Exact Fraction Markov trace at rational qv (Part A's pipeline, no series)."""
    n = 3 * (Z + N)
    crossings = atom_canonical_crossings(Z, N, include_inter=include_inter)
    facs = factors_for(crossings, qv, colour_weighted=True)
    y = y_lambda_at(n)
    tot = F(0)
    qs = sp.Rational(qv.numerator, qv.denominator)
    for lam in two_row_partitions(n):
        # `sp.nsimplify` does NOT always return a Rational here: at q = 3/2 (and
        # other points) `together(...).subs(...)` stays an unevaluated `Mul` with
        # a `Pow(..., -1)` factor, and `.p` then raises AttributeError. Latent
        # bug in the merged version (bean qou-i719): the two points that probe
        # used, 8/7 and 11/10, happened to reduce. `cancel` reduces a rational
        # function at a rational point to a Rational in every case, and the
        # `as_numer_denom` route below never depends on auto-simplification.
        num, den = sp.cancel(sp.together(y[tuple(lam)]).subs(Q_SYM, qs)).as_numer_denom()
        yv = F(int(num), int(den))
        tot += yv * chi_at(lam, facs, qv)
    return tot


# ---- Part B: the permutation formula [★] ------------------------------------
W_OF = {"sigma": 1, "sigma_inv": -1, "averaged": 0, "averaged_weighted": 0}


def cycles_of_product(gens: list[int], n: int) -> int:
    perm = list(range(n))
    for g in gens:
        perm[g], perm[g + 1] = perm[g + 1], perm[g]
    seen, c = set(), 0
    for s in range(n):
        if s in seen:
            continue
        c += 1
        x = s
        while x not in seen:
            seen.add(x)
            x = perm[x]
    return c


def star(Z: int, N: int, include_inter: bool) -> tuple[F, int, dict]:
    """[★] for one word: 2^{-n} Σ_ℓ w_ℓ 2^{c(σ^{(ℓ)})}; also c(σ) and a tally."""
    n = 3 * (Z + N)
    crossings = atom_canonical_crossings(Z, N, include_inter=include_inter)
    missing = set(k for _, k in crossings) - set(W_OF)
    if missing:
        raise ValueError(f"ctype(s) {sorted(missing)} have no first-order weight here")
    gens = [g for g, _ in crossings]
    c_full = cycles_of_product(gens, n)
    total, tally = F(0), {k: 0 for k in CTYPES}
    for i, (g, kind) in enumerate(crossings):
        tally[kind] += 1
        w = W_OF[kind]
        if w == 0:
            continue
        c_del = cycles_of_product(gens[:i] + gens[i + 1:], n)
        total += w * F(2) ** (c_del - n)
    return total, c_full, tally


def c0_derived(A: int) -> F:
    return F(2) ** (-A) - F(2) ** (1 - 2 * A)


RECORDED_GROUPED_SUPERSEDED = {  # pre-2026-09-05 grouped atom word (qou-zrx2)
    "pp": F(19, 8), "pn": F(37, 16), "nn": F(9, 4),
    "T": F(163, 64), "3He": F(85, 32), "4He": F(259, 128),
}
RECORDED = {  # PairwiseChainLeadingOrder.lean, Borromean word (qou-j1e5)
    "pp": F(1, 8), "pn": F(1, 16), "nn": F(0),
    "T": F(1, 64), "3He": F(1, 8), "4He": F(7, 128),
}
# Exact Borromean higher-order coefficients c₂ = a₁+a₂, c₃ = a₂+a₃, c₄ = a₃+a₄
# (from c2_diagonal_insertion_expansion_probe and qou-yaig / P=4,5,6 runs;
# ⁴He at P=4 gives a₂ = 411/512 -> c₂ = 439/512, P=5 gives a₃ = 2247/512 -> c₃ = 1329/256,
# P=6 gives a₄ = 16115/6144 -> c₄ = 43079/6144).
EXACT_C2_BORROMEAN = {
    "pp": F(33, 32), "pn": F(25, 32), "nn": F(1, 16),
    "T": F(99, 128), "3He": F(157, 128), "4He": F(439, 512),
}
EXACT_C3_BORROMEAN = {
    "pp": F(67, 16), "pn": F(43, 8), "nn": F(27, 4),
    "T": F(101, 16), "3He": F(839, 128), "4He": F(1329, 256),
}
EXACT_C4_BORROMEAN = {
    "pp": F(-585, 128), "pn": F(109, 192), "nn": F(27, 32),
    "T": F(371, 192), "3He": F(9989, 1536), "4He": F(43079, 6144),
}
CASES = [("pp", (2, 0)), ("pn", (1, 1)), ("nn", (0, 2)),
         ("T", (1, 2)), ("3He", (2, 1)), ("4He", (2, 2))]
# series precision per case: c₁ needs orders 0,1 known after one order is lost
# to the 0/0 seminormal quotients; the small cases also get c₂ (order 2).
P_OF = {"pp": 6, "pn": 6, "nn": 6, "T": 5, "3He": 5, "4He": 3}


def main() -> int:
    T0 = time.time()

    def log(msg):
        print(f"  [{time.time()-T0:7.1f}s] {msg}", flush=True)

    w = WitnessBuilder("c1-leading-coefficient-derived-probe")
    w.set_description(
        "The leading hbar_q coefficient c1 of tr_M(W_free) - tr_M(W_atom): computed EXACTLY "
        "as a power series in eps = q - 1 through the validated exact-Fraction seminormal "
        "pipeline (no Richardson), then DERIVED as a permutation count "
        "2^-n sum_letters w_l 2^c(sigma with letter l deleted), w = +1/-1/0 for "
        "sigma/sigma^-1/averaged, by the same Schur-Weyl route that derived c0. The two "
        "agree exactly on all six recorded cases, and the derivation runs to A = 20."
    )

    print("=" * 78)
    print("  c₁ — exact by series, then derived by a permutation count")
    print("=" * 78)

    # ---- assertion 1: the row cap is exact in the symbolic weights -----------
    bad_all = {}
    for n in (6, 9, 12):
        _, bad = y_lambda_series(n, 2)
        bad_all[n] = bad
    w.add_assertion(
        "three_row_weights_vanish_identically_at_n_6_9_12",
        computed="1" if not any(bad_all.values()) else "0", expected="1",
        source=f"sympy simplify of y_lambda_at(n)[λ] for every ℓ(λ) ≥ 3 at n = 6, 9, 12; "
               f"non-vanishing: {bad_all}. This is what lets the series sum run over "
               f"two-row partitions only.",
    )
    log(f"row cap: non-vanishing ≥3-row weights = {bad_all}")

    # ---- Part A: exact series for the six cases ------------------------------
    series_rows, a_eq_c0, a_eq_recorded = [], True, True
    exact_c1, exact_c2 = {}, {}
    for name, (Z, N) in CASES:
        A, P = Z + N, P_OF[name]
        log(f"Part A  {name} (Z={Z},N={N}, n={3*A}, P={P}) …")
        tf = tr_M_series(Z, N, False, P, log=log)
        ta = tr_M_series(Z, N, True, P, log=log)
        d = tf - ta
        a0, a1 = d.coeff(0), d.coeff(1)
        a2 = d.coeff(2) if d.p > 2 else None
        a3 = d.coeff(3) if d.p > 3 else None
        c1 = a1
        c2 = (a1 + a2) if a2 is not None else EXACT_C2_BORROMEAN[name]
        c3 = (a2 + a3) if (a2 is not None and a3 is not None) else EXACT_C3_BORROMEAN[name]
        exact_c1[name] = c1
        exact_c2[name] = c2
        ok0, ok1 = (a0 == c0_derived(A)), (c1 == RECORDED[name])
        a_eq_c0 &= ok0
        a_eq_recorded &= ok1
        series_rows.append({
            "case": name, "Z": Z, "N": N, "A": A, "n_strands": 3 * A,
            "series_precision": P, "precision_after_pipeline": d.p,
            "a0": str(a0), "c0_derived": str(c0_derived(A)), "a0_eq_c0": ok0,
            "c1_exact": str(c1), "c1_recorded": str(RECORDED[name]),
            "c1_eq_recorded": ok1,
            "c2_exact": str(c2),
            "c3_exact": str(c3),
            "c4_exact": str(EXACT_C4_BORROMEAN[name]),
        })
        log(f"        a0 = {a0}  (c0 derived {c0_derived(A)}: {ok0})   "
            f"c1 = {c1}  (recorded {RECORDED[name]}: {ok1})   c2 = {c2}")

    w.add_assertion(
        "series_order_zero_reproduces_the_derived_floor_c0",
        computed="1" if a_eq_c0 else "0", expected="1",
        source="[ε⁰] of Δtr(1+ε) vs 2^-A - 2^(1-2A) as exact Fractions, all six cases. An "
               "independent re-derivation of ClassicalTraceFloor by the seminormal series "
               "rather than by cycle counting.",
    )
    w.add_assertion(
        "series_order_one_equals_the_six_recorded_rationals_exactly",
        computed="1" if a_eq_recorded else "0", expected="1",
        source="[ε¹] of Δtr(1+ε) (= c1, since ε = ℏ_q + O(ℏ_q²)) vs the Richardson-measured "
               "rationals in PairwiseChainLeadingOrder.lean, Fraction equality: "
               + ", ".join(f"{r['case']} {r['c1_exact']}" for r in series_rows),
    )

    # ---- Part B: the permutation formula, checked against Part A -------------
    star_rows, b_eq_a = [], True
    for name, (Z, N) in CASES:
        sf, cf, tf_ = star(Z, N, False)
        sa, ca, ta_ = star(Z, N, True)
        c1_star = sf - sa
        ok = (c1_star == exact_c1[name])
        b_eq_a &= ok
        star_rows.append({"case": name, "A": Z + N, "star_free": str(sf), "star_atom": str(sa),
                          "c1_star": str(c1_star), "c1_series": str(exact_c1[name]),
                          "equal": ok, "c_free": cf, "c_atom": ca,
                          "letters_free": tf_, "letters_atom": ta_})
        log(f"Part B  {name}: [★]free = {sf}, [★]atom = {sa}, c1 = {c1_star}  "
            f"(series {exact_c1[name]}: {ok})")
    w.add_assertion(
        "permutation_formula_equals_exact_series_c1_for_all_six",
        computed="1" if b_eq_a else "0", expected="1",
        source="c1 = 2^-n Σ_ℓ w_ℓ 2^c(σ^(ℓ)) over the free word minus the same over the atom "
               "word, w = +1 (σ), -1 (σ^-1), 0 (averaged), vs Part A's exact [ε¹]; Fraction "
               "equality in all six cases. This is the derivation [★], tested — a pure "
               "permutation count with no Hecke evaluation.",
    )

    # ---- cross-check: the exact pipeline vs the production transfer kernel ---
    import tr_m_atom_via_transfer as TR
    mp.mp.dps = 50
    # q = 8/7: a non-terminating decimal, so the 50-dps mpf carries genuine
    # 50-digit information and passes `reject_float64_q` (which correctly
    # rejects mpf("1.1") as float64-equivalent — measured, first run).
    q_rat = F(8, 7)
    q_mp = mp.mpf(8) / 7
    xrows, worst = [], mp.mpf(0)
    for name, (Z, N) in [("D", (1, 1)), ("T", (1, 2)), ("3He", (2, 1)), ("4He", (2, 2))]:
        log(f"cross-check {name} at q = 8/7 …")
        ex = tr_M_fraction(Z, N, False, q_rat) - tr_M_fraction(Z, N, True, q_rat)
        ta, tf, _c, _w = TR.tr_m_atom_zn(Z, N, dps=50, q=q_mp)
        kern = tf - ta
        exm = mp.mpf(ex.numerator) / ex.denominator
        rel = abs(exm - kern) / abs(kern)
        worst = max(worst, rel)
        xrows.append({"case": name, "exact_fraction": str(ex), "exact_mpf": mp.nstr(exm, 30),
                      "transfer_kernel": mp.nstr(kern, 30), "rel_diff": mp.nstr(rel, 4)})
        log(f"        rel diff {mp.nstr(rel, 4)}")
    w.add_assertion(
        "exact_fraction_pipeline_matches_transfer_kernel_at_q_8_over_7",
        computed=mp.nstr(worst, 6), expected="0", tolerance="1e-40",
        source="Δtr at q = 8/7: exact Fraction via the asymmetric seminormal gauge + symbolic "
               "y_λ, vs tr_m_atom_zn(q=mpf(8)/7) at 50 dps, D/T/3He/4He. Ties the series "
               "pipeline to the witness path the six measurements came from.",
    )

    # ---- colour enters at ε⁴: deuteron, weighted vs blind ---------------------
    log("colour-weight order check (deuteron, P=6) …")
    dw = tr_M_series(1, 1, True, 6, colour_weighted=True)
    db = tr_M_series(1, 1, True, 6, colour_weighted=False)
    diff = dw - db
    same123 = all(diff.coeff(k) == 0 for k in (0, 1, 2, 3))
    e4 = diff.coeff(4)
    w.add_assertion(
        "colour_weight_first_enters_at_order_eps4",
        computed="1" if (same123 and e4 != 0) else "0", expected="1",
        source=f"tr_M(atom) with the colour-weighted vs colour-blind p-n factor, deuteron: "
               f"coefficients ε⁰..ε³ identical, ε⁴ differs by {e4}. δ = (q-1)²(1-q⁻⁴)/3 is "
               f"O(ε³) and enters through h·δ = O(ε⁴), so c₁ (and c₂, c₃) are colour-blind.",
    )
    log(f"        ε⁰..ε³ identical: {same123};  [ε⁴] difference = {e4}")

    # ---- Part B to A = 20, and the CLOSED FORM ------------------------------------
    # Under the Borromean intra-nucleon ordering (ruling qou-hu1f; re-derived in
    # qou-j1e5 / PairwiseChainLeadingOrder.c1Closed), each nucleon contributes
    # half its signed deletion sum (S_p, S_n)/2 = (6, -4)/2 = (3, -2) to the
    # (2^{-A-1} - 2^{-2A}) coefficient (superseded grouped ordering: (42, 32)/2 =
    # (21, 16) because every intra-nucleon deletion shifted c by ±1). A pp
    # interface (σ) adds +4·2^{c−1}, an nn interface (σ⁻¹) −4·2^{c−1}, a pn
    # interface (averaged) 0. With c_free = 2A and c_atom = A+1:
    #     c₁(Z,N) = (3Z − 2N)·(2^{−A−1} − 2^{−2A}) − 4·(I_pp − I_nn)·2^{−2A}
    def closed_form(Z: int, N: int) -> F:
        A = Z + N
        i_pp, i_nn = max(Z - 1, 0), max(N - 1, 0)
        return (3 * Z - 2 * N) * (F(2) ** (-A - 1) - F(2) ** (-2 * A)) \
            - 4 * (i_pp - i_nn) * F(2) ** (-2 * A)

    table, closed_ok = [], True
    for A in range(2, 21):
        for Z in range(0, A + 1):
            N = A - Z
            sf, _, _ = star(Z, N, False)
            sa, _, _ = star(Z, N, True)
            v = sf - sa
            cf = closed_form(Z, N)
            closed_ok &= (v == cf)
            table.append({"Z": Z, "N": N, "A": A, "c1": str(v), "closed_form": str(cf),
                          "equal": v == cf, "c1_times_2^(3A)": str(v * 2 ** (3 * A))})
    log(f"tabulated c1 for {len(table)} (Z,N) with A = 2..20; closed form matches all: {closed_ok}")
    w.add_assertion(
        "closed_form_equals_permutation_count_for_every_ZN_with_A_2_to_20",
        computed="1" if closed_ok else "0", expected="1",
        source=f"c1(Z,N) = (3Z-2N)(2^(-A-1) - 2^(-2A)) - 4(I_pp - I_nn) 2^(-2A), I_pp = max(Z-1,0), "
               f"I_nn = max(N-1,0), vs [★](free) - [★](atom) for all {len(table)} (Z,N) with "
               f"A = 2..20, Fraction equality. The 3 and -2 are the Borromean nucleon deletion "
               f"weights (S_p, S_n)/2 = (6, -4)/2 (superseded grouped: 21 and 16 from (42, 32)/2); "
               f"the ±4 are the pp/nn interface letters.",
    )
    closed_eq_recorded = all(closed_form(Z, N) == RECORDED[name] for name, (Z, N) in CASES)
    w.add_assertion(
        "closed_form_reproduces_the_six_recorded_rationals",
        computed="1" if closed_eq_recorded else "0", expected="1",
        source=", ".join(f"{name}: {closed_form(Z, N)}" for name, (Z, N) in CASES),
    )

    # ---- report ----------------------------------------------------------------
    print()
    print(f"  {'case':5}{'A':>3}{'a0=c0':>10}{'c1 exact':>12}{'c1 [★]':>12}{'recorded':>12}{'c2 exact':>14}")
    for r, s in zip(series_rows, star_rows):
        print(f"  {r['case']:5}{r['A']:>3}{r['a0']:>10}{r['c1_exact']:>12}{s['c1_star']:>12}"
              f"{r['c1_recorded']:>12}{str(r['c2_exact']):>14}")
    print()
    print("  c1 by the permutation count, A = 2..8 (Z,N → c1):")
    for A in range(2, 9):
        row = [t for t in table if t["A"] == A]
        print(f"    A={A}: " + "  ".join(f"({t['Z']},{t['N']})={t['c1']}" for t in row))

    w.add_data("series", series_rows)
    w.add_data("permutation_formula", star_rows)
    w.add_data("transfer_kernel_crosscheck", xrows)
    w.add_data("colour_order", {"eps0_to_eps3_identical": same123, "eps4_difference": str(e4)})
    w.add_data("c1_table_A2_to_A20", table)
    w.add_data("derivation", {
        "1_first_order_generator": "σ = s + ε(1 + Y) + O(ε²) with sY = -Ys, forced by "
                                   "σ² = hσ + 1, h = 2ε + O(ε²), s² = 1.",
        "2_Y_is_trace_invisible": "Tr(Y·P) = 0 for every permutation P: Y lives on the "
                                  "(e12,e21) sector of one adjacent pair, is traceless there "
                                  "with opposite off-diagonal entries, and the global spin flip "
                                  "commutes with every permutation, so the two sectors cancel.",
        "3_normaliser_cancels": "K' = 2 N_down, Tr(K' P) = n 2^c(P); (1+q²)^-n = 2^-n(1 - nε + …). "
                                "The two n·2^c terms cancel.",
        "4_letter_scalars": "L_ℓ' = (1 + d_ℓ'(0))·1 with d'(0) = 0, -2, -1, -1 for σ, σ⁻¹, "
                            "averaged, averaged_weighted; δ = O(ε³) is invisible.",
        "result": "d tr_M/dε|₀ = 2^-n Σ_ℓ w_ℓ 2^c(σ^(ℓ)), w = +1, -1, 0, 0; c1 = free - atom.",
        "hypotheses_not_proved_here": "quantum Schur-Weyl (tr_M = Tr(K ρ)/Z with K = "
                                      "diag(1,q²)^⊗n) — the same input ClassicalTraceFloor "
                                      "carries as a hypothesis; the rest is finite algebra.",
    })
    w.add_data("verdict", (
        "c1 is DERIVED: the leading hbar_q coefficient of the trace difference is a signed "
        "sum over the word's non-averaged letters of 2^(c(σ with that letter deleted) - n), "
        "exactly like the floor c0 is 2^(c-n). Checked three ways — exact series, the "
        "permutation count, and the six Richardson measurements — all equal as Fractions. "
        "The six Lean definitions in PairwiseChainLeadingOrder.lean can become theorems "
        "conditional on Schur-Weyl."
    ))
    out = w.save()
    print(f"\n  witness -> {out}")
    ok = (not any(bad_all.values())) and a_eq_c0 and a_eq_recorded and b_eq_a \
        and worst < mp.mpf("1e-40") and same123 and e4 != 0 and closed_ok \
        and closed_eq_recorded
    print(f"  ALL PASSED: {ok}   ({time.time()-T0:.0f}s)")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
