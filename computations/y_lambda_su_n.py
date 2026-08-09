#!/usr/bin/env python3
# polynomial_q_not_applicable: closed-form weights in q; no symbolic-q polynomial output.
"""y_λ for the SU(N) Markov trace — the N-generalisation of `y_lambda_at`.

`wedderburn_jones_markov.y_lambda_at(n, q)` computes ONE member of the Ocneanu
family: convention **C** of `docs/coordination/trace-convention-registry.md`, the
full-Hecke Ocneanu / Wenzl z-trace at `z = 1/(q^{1/2}+q^{-1/2})`. There is no `N`
argument, and no `z` argument — the member is baked in.

The eightfold-way chapter needs a *different* member. Every flavour statement
there — meson octet, baryon decuplet, the quark rows of the dictionary — is
conditional on `N = 3` (`eightfold-open-problems.md`, item 1), and
`RowCapObstruction.lean` proves sorry-free that `N = 2` cannot host the
decomposition because the alternating channel `dim V_{(1^3)} = C(N,3)` vanishes
iff `N < 3`. `ocneanu_N_lockin_probe.py` separately proves the mass channel
cannot simply be *retuned* to `N = 3` — moving N re-weights channels the mass
pipeline already evaluates — so flavour needs a SECOND trace on the same
`H_n(q)`, not a modified first one. `HnMarkovTrace.lean` already types the
Markov parameter as a free class field, so two instances are typeable today.

This module supplies the weights for that second trace.

## The formula

For the `U_q(gl_N)` Schur–Weyl dual trace, the λ-block weight is proportional to
the quantum dimension of the λ-irrep, i.e. the principal specialisation
`s_λ(1, q, …, q^{N-1})`, which the hook-content formula gives as

    s_λ  ∝  Π_{(i,j) ∈ λ}  [N + j − i]_q / [h(i,j)]_q

with `[m]_q = (q^m − q^{−m})/(q − q^{−1})` the balanced quantum integer,
`j − i` the content and `h(i,j)` the hook length. Normalised by
`Σ_λ y_λ f^λ = 1` (the Markov condition `tr_M(1) = 1`), where `f^λ` is the
`S_n` irrep dimension.

The row cap is automatic rather than imposed: a λ with more than `N` rows has a
cell at `(N+1, 1)` of content `−N`, so the factor `[N + (−N)]_q = [0]_q = 0`
kills the whole weight. That is `RowCapObstruction.lean`'s statement arriving as
arithmetic.

## What this module found, and it is not what was expected

Validated against the registry: at `N = 2` these weights reproduce convention
**D** (SU(2)/Temperley–Lieb, Jones) exactly — `(0.5054042, 0.2472979, 0)` at
`n = 3`, `y_{(1^3)} = 0` on the nose.

But the production trace is convention **C**, `(0.4153958, 0.2809296,
0.0227449)`, and **C matches no integer N**. Solving for the real `N` that
reproduces C's `y_{(1^3)}/y_{(3)}` ratio gives

    N = 2.5995155…

so the mass channel sits BETWEEN SU(2) and SU(3) and is not an `SU(N)`
quantum-group trace at all. Two consequences worth stating plainly:

* C has `y_{(1^3)} ≠ 0`, so the mass trace does **not** carry the `N = 2` row
  cap. The ledger's "framework supplies `dim V = 2`" is a statement about the
  single-fibre tower, not about the trace the masses are computed with.
* The often-repeated shorthand that the framework's `z` is "the
  Temperley–Lieb / SU(2) value" is **false** — that is convention D, at
  `z = q^3/(q^2+1) = 0.6126880`, and `D ≠ C` is Lean-proved
  (`QOU.BraidsAndKnots.BorromeanTraceConventionSplit.conventionD_ne_conventionC`).
  The two differ by 195.8 ppm on `β_Bor`.

Nothing here is wired into any production path. It is the weight function the
flavour channel would need, plus the measurement of where C actually sits.

Read-only: writes no witness, runs no producer.

Usage:
    python3 computations/y_lambda_su_n.py --self-test
    python3 computations/y_lambda_su_n.py            # table + the effective-N fit
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: F401, E402
import mpmath as mp  # noqa: E402


def q_int(m, q: "mp.mpf") -> "mp.mpf":
    """Balanced quantum integer `[m]_q = (q^m − q^{−m})/(q − q^{−1})`.

    Balanced (not `(q^m−1)/(q−1)`) because that is the convention the registry's
    conventions C and D are quoted in, and the one `[2]_q = q + q^{−1}` that
    `charge_independence_iff` and the projector work use.
    """
    m = mp.mpf(m)
    return (q ** m - q ** (-m)) / (q - 1 / q)


def partitions_of(n: int) -> list[tuple[int, ...]]:
    """Partitions of `n` as weakly decreasing tuples."""
    def _p(rem: int, cap: int) -> list[tuple[int, ...]]:
        if rem == 0:
            return [()]
        out = []
        for part in range(min(rem, cap), 0, -1):
            out += [(part,) + rest for rest in _p(rem - part, part)]
        return out
    return _p(n, n)


def f_lambda(shape: tuple[int, ...]) -> int:
    """`f^λ`, the `S_n` irrep dimension, by the hook-length formula."""
    n = sum(shape)
    num = 1
    for k in range(2, n + 1):
        num *= k
    den = 1
    for h in hooks(shape):
        den *= h
    return num // den


def hooks(shape: tuple[int, ...]) -> list[int]:
    """Hook length of every cell, row-major."""
    conj = conjugate(shape)
    return [shape[i] - j + conj[j] - i - 1
            for i, row in enumerate(shape) for j in range(row)]


def contents(shape: tuple[int, ...]) -> list[int]:
    """Content `j − i` of every cell, row-major (0-indexed i, j)."""
    return [j - i for i, row in enumerate(shape) for j in range(row)]


def conjugate(shape: tuple[int, ...]) -> tuple[int, ...]:
    if not shape:
        return ()
    return tuple(sum(1 for r in shape if r > j) for j in range(shape[0]))


def schur_principal(shape: tuple[int, ...], N: int | float,
                    q: "mp.mpf") -> "mp.mpf":
    """`s_λ(1, q, …, q^{N-1})` up to a q-power, by hook-content.

    Returns exactly `0` when λ has more than `N` rows — the factor
    `[N + c]_q` hits `[0]_q = 0` at the cell `(N+1, 1)`. `N` may be
    non-integral, which is what makes the effective-N fit below possible.
    """
    num = mp.mpf(1)
    for c in contents(shape):
        num *= q_int(mp.mpf(N) + c, q)
    den = mp.mpf(1)
    for h in hooks(shape):
        den *= q_int(h, q)
    return num / den


def y_lambda_su_n(n: int, q: "mp.mpf", N: int | float) -> dict:
    """`{λ: y_λ}` for the SU(N) Markov trace on `H_n(q)`.

    Normalised so `Σ_λ y_λ f^λ = 1`, i.e. `tr_M(1) = 1` — the same
    normalisation `y_lambda_at` uses, so the two are directly comparable.
    """
    shapes = partitions_of(n)
    s = {sh: schur_principal(sh, N, q) for sh in shapes}
    Z = mp.fsum(s[sh] * f_lambda(sh) for sh in shapes)
    if Z == 0:
        raise ValueError(f"degenerate normalisation at n={n}, N={N}")
    return {sh: s[sh] / Z for sh in shapes}


def z_from_weights(q: "mp.mpf", y: dict) -> "mp.mpf":
    """The Markov parameter implied by an `n = 2` weight system.

    `z = tr_M(σ) = y_{(2)}·q + y_{(1,1)}·(−q^{−1})`, and with the normalisation
    `y_{(2)} + y_{(1,1)} = 1` that is `y_{(2)}(q + q^{−1}) − q^{−1}` — the Lean
    `QOU.QBeta.InterfaceScalar.markov_param_determined`. So z is a CONSEQUENCE
    of the weights, never an independent input.
    """
    return y[(2,)] * q + y[(1, 1)] * (-1 / q)


# ── self-test ────────────────────────────────────────────────────────────
_Q = "1.1099785827513808075916690956107688798744991218736"
# docs/coordination/trace-convention-registry.md, at the proton pin
REG_C = (mp.mpf("0.4153958"), mp.mpf("0.2809296"), mp.mpf("0.0227449"))
REG_D = (mp.mpf("0.5054042"), mp.mpf("0.2472979"), mp.mpf("0"))
REG_ZC = mp.mpf("0.49932033418369445")
REG_ZD = mp.mpf("0.61268803714646524")


def self_test() -> int:
    mp.mp.dps = 30
    q = mp.mpf(_Q)
    fails = 0

    def chk(label, ok):
        nonlocal fails
        fails += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  {label}")

    # combinatorics
    chk("p(6) = 11", len(partitions_of(6)) == 11)
    chk("f^(2,1) = 2", f_lambda((2, 1)) == 2)
    chk("Σ (f^λ)² = n! at n=4",
        sum(f_lambda(s) ** 2 for s in partitions_of(4)) == 24)
    chk("conjugate((3,1)) = (2,1,1)", conjugate((3, 1)) == (2, 1, 1))
    chk("hooks((2,1)) = [3,1,1]", sorted(hooks((2, 1))) == [1, 1, 3])

    # N = 2 must reproduce registry convention D exactly
    y3 = y_lambda_su_n(3, q, 2)
    got = (y3[(3,)], y3[(2, 1)], y3[(1, 1, 1)])
    for nm, g, r in zip(("y_(3)", "y_(2,1)", "y_(1^3)"), got, REG_D):
        chk(f"N=2 reproduces registry convention D: {nm}", abs(g - r) < mp.mpf("5e-7"))
    chk("N=2 gives y_(1^3) = 0 EXACTLY (the row cap)", y3[(1, 1, 1)] == 0)

    # z implied at N = 2 must be convention D's z
    zD = z_from_weights(q, y_lambda_su_n(2, q, 2))
    chk("N=2 implies z_D = q³/(q²+1)", abs(zD - REG_ZD) < mp.mpf("1e-15"))
    chk("…and z_D ≠ z_C (Lean conventionD_ne_conventionC)",
        abs(zD - REG_ZC) > mp.mpf("0.1"))

    # normalisation and the row cap, generally
    for n in (2, 3, 4, 5):
        for N in (2, 3, 4):
            y = y_lambda_su_n(n, q, N)
            tot = mp.fsum(y[s] * f_lambda(s) for s in y)
            chk(f"Σ y_λ f^λ = 1 at n={n}, N={N}", abs(tot - 1) < mp.mpf("1e-25"))
            capped = [s for s in y if len(s) > N]
            chk(f"row cap: y_λ = 0 for λ with >{N} rows at n={n} "
                f"({len(capped)} shapes)", all(y[s] == 0 for s in capped))

    # production is convention C, and C is NOT any integer N
    from wedderburn_jones_markov import y_lambda_at
    prod = {k: mp.mpf(str(v)) for k, v in y_lambda_at(3, q).items()}
    chk("production y_λ matches registry C, not D",
        abs(prod[(3,)] - REG_C[0]) < mp.mpf("5e-7")
        and abs(prod[(1, 1, 1)] - REG_C[2]) < mp.mpf("5e-7"))
    chk("production y_(1^3) ≠ 0 — C does NOT carry the N=2 row cap",
        prod[(1, 1, 1)] > mp.mpf("0.02"))
    for N in (2, 3, 4, 5):
        y = y_lambda_su_n(3, q, N)
        chk(f"C ≠ SU({N})", abs(y[(3,)] - prod[(3,)]) > mp.mpf("1e-3"))

    total = 33
    print(f"\n{total - fails}/{total} passed")
    return 1 if fails else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--n", type=int, default=3)
    a = ap.parse_args()
    if a.self_test:
        return self_test()

    mp.mp.dps = 30
    q = mp.mpf(_Q)
    n = a.n
    shapes = partitions_of(n)
    print("=" * 78)
    print(f" y_λ for the SU(N) Markov trace on H_{n}(q₀)  "
          f"(normalised Σ y_λ f^λ = 1)")
    print("=" * 78)
    hdr = "  N  " + "".join(f"{str(s):>17}" for s in shapes)
    print(hdr)
    for N in (2, 3, 4, 5, 6):
        y = y_lambda_su_n(n, q, N)
        print(f" {N:>3} " + "".join(f"{mp.nstr(y[s], 10):>17}" for s in shapes))

    from wedderburn_jones_markov import y_lambda_at
    prod = {k: mp.mpf(str(v)) for k, v in y_lambda_at(n, q).items()}
    print(f" {'C':>3} " + "".join(f"{mp.nstr(prod.get(s, mp.mpf(0)), 10):>17}"
                                  for s in shapes)
          + "   <- production (registry convention C)")

    if n == 3:
        print("\n" + "-" * 78)
        print(" where does convention C actually sit?")
        print("-" * 78)
        tgt = prod[(1, 1, 1)] / prod[(3,)]
        def f(N):
            y = y_lambda_su_n(3, q, N)
            return y[(1, 1, 1)] / y[(3,)] - tgt
        Nstar = mp.findroot(f, mp.mpf("2.6"))
        print(f" C's y_(1³)/y_(3)          = {mp.nstr(tgt, 12)}")
        print(f" real N reproducing it     = {mp.nstr(Nstar, 12)}")
        print(" NON-INTEGER, between SU(2) and SU(3): the mass channel is not an")
        print(" SU(N) quantum-group trace, and does not carry the N=2 row cap.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
