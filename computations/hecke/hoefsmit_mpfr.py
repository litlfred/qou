#!/usr/bin/env python3
"""Hoefsmit seminormal generators ρ_λ(T_k) in mpmath, at a numeric q.

WHY THIS EXISTS
---------------
Ten committed probes under `computations/probes/` did

    from probe_staircase_ew_k3_categorical import build_hoefsmit_mpfr

and that module is **not in the repository**. It lived in one of the five
root-level agent-scratch directories untracked by `0763606e4f`
("chore: untrack the five root-level agent-scratch dirs (2,344 files)"), so
every one of those probes has been unrunnable in a fresh clone ever since —
their committed witnesses could not be reproduced by anyone, including the
author. `hoefsmit_seminormal_form_probe.py` states the stakes in its own
docstring: "A failure here would invalidate every probe that uses canonical
Hoefsmit downstream (the entire H_n cluster of PR #818 and beyond)."

Discovered 2026-08-24 while re-running producers for the q₀ migration: 10 of
24 failures were this one `ModuleNotFoundError`. Bean `qou-ti1n`.

The repo already knew about the CLASS. `producer-importability-audit` records
"72 producers cannot import a module that lives in this repo ... Each one owns
at least one committed witness that cannot be regenerated, so no staleness
check can ever fire on it" — and closes with **"Reported, not fixed."** This
module fixes the `probe_staircase_ew_k3_categorical` slice of that, 10 of the
72. The other causes it names (pyhecke 35, qou_substrate 10, ValueError 14)
are untouched.

WHAT THIS IS, AND WHY IT IS NOT A GUESS
---------------------------------------
This is a transcription of `_hoefsmit_build` from
`computations/hecke/hecke_character_symbolic.py` — the live, canonical,
symbolic builder — into mpmath arithmetic at the ambient working precision.
The two are checked against each other by `_selftest` below: build
symbolically in a sympy Symbol, substitute q₀, and compare entrywise against
this module's output on every partition λ ⊢ n for n = 2..6. The reconstruction
is therefore verified against the surviving implementation rather than
asserted to match the lost one.

Doing it in mpf rather than `sympy.subs(...).evalf()` is the point of the
`_mpfr` suffix: the seminormal entries are built from `q - 1/q` and
`1 - q^{∓2ρ}` and a square root, all of which are exact-to-working-precision
in mpmath, whereas substituting into a cancelled rational function and
evaluating re-rounds through sympy's own float path.

THE SHAPE OF THE ANSWER
-----------------------
Each ρ_λ(T_k) is diagonal plus, for each 2×2 block, one symmetric off-diagonal
pair — so at most two non-zeros per column. That structure is what makes the
downstream `chi_lambda_of_word` fast path legal; see `mass_at_3A_proper`.

    build_hoefsmit_mpfr(shape, q) -> (matrices, dim)

`matrices` is [ρ_λ(T_1), …, ρ_λ(T_{n-1})] as `mp.matrix`; `dim` is the number
of standard Young tableaux of `shape`. An empty shape gives `([], 0)`, matching
the symbolic builder.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

if str(_Path(__file__).resolve().parent) not in _sys.path:
    _sys.path.insert(0, str(_Path(__file__).resolve().parent))

import mpmath as mp  # noqa: E402

from hecke_character_symbolic import standard_young_tableaux  # noqa: E402

__all__ = ["build_hoefsmit_mpfr"]


def build_hoefsmit_mpfr(shape, q):
    """ρ_λ(T_1), …, ρ_λ(T_{n-1}) at numeric ``q``; returns ``(matrices, dim)``.

    ``shape`` is a partition as a tuple/list; ``q`` is anything ``mp.mpf``
    accepts (an ``mpf``, a decimal string, an int). Arithmetic runs at the
    ambient ``mp.dps``, so callers set precision the usual way.
    """
    shape = tuple(int(p) for p in shape if int(p) > 0)
    n = sum(shape)
    syts, _cells, contents = standard_young_tableaux(shape)
    dim = len(syts)
    if dim == 0:
        return [], 0

    q = mp.mpf(q) if not isinstance(q, mp.mpf) else q
    h = q - 1 / q

    matrices = []
    for k in range(1, n):
        M = mp.zeros(dim, dim)
        processed = set()
        for i in range(dim):
            if i in processed:
                continue
            ci_k = syts[i][k]
            ci_k1 = syts[i][k + 1]
            rho = contents[ci_k1] - contents[ci_k]

            a = h / (1 - q ** (-2 * rho))

            swap_map = dict(syts[i])
            swap_map[k], swap_map[k + 1] = ci_k1, ci_k
            j = None
            for jj in range(dim):
                if jj != i and syts[jj] == swap_map:
                    j = jj
                    break

            if j is None:
                # 1x1 block: k and k+1 sit in the same row (rho = 1, giving
                # eigenvalue q) or the same column (rho = -1, giving -1/q).
                M[i, i] = a
                processed.add(i)
            else:
                a_prime = h / (1 - q ** (2 * rho))
                b = mp.sqrt(a * a_prime + 1)
                M[i, i] = a
                M[j, j] = a_prime
                M[i, j] = b
                M[j, i] = b
                processed.add(i)
                processed.add(j)
        matrices.append(M)
    return matrices, dim


def _selftest(nmax: int = 6, dps: int = 40) -> int:
    """Compare against the symbolic builder on every λ ⊢ n, n = 2..nmax.

    Exit 0 iff every entry of every generator agrees to `dps - 6` digits.
    Run: ``python3 computations/hecke/hoefsmit_mpfr.py``
    """
    import sympy as sp
    from hecke_character_symbolic import hoefsmit_matrices_symbolic

    def partitions(m, cap=None):
        cap = m if cap is None else cap
        if m == 0:
            yield ()
            return
        for first in range(min(m, cap), 0, -1):
            for rest in partitions(m - first, first):
                yield (first,) + rest

    mp.mp.dps = dps
    qs = sp.Symbol("q", positive=True, real=True)
    q0 = mp.mpf("1.10997859555733471989976322048322502665620840878015")
    tol = mp.mpf(10) ** (-(dps - 6))
    checked = worst_shape = 0
    worst = mp.mpf(0)
    for n in range(2, nmax + 1):
        for shape in partitions(n):
            got, dim = build_hoefsmit_mpfr(shape, q0)
            sym, sdim, _ = hoefsmit_matrices_symbolic(shape, qs)
            if dim != sdim:
                print(f"  FAIL {shape}: dim {dim} != symbolic {sdim}")
                return 1
            for k, (G, S) in enumerate(zip(got, sym)):
                Sn = S.subs(qs, sp.Float(str(q0), dps))
                for r in range(dim):
                    for c in range(dim):
                        ref = mp.mpf(str(sp.N(Sn[r, c], dps)))
                        d = abs(G[r, c] - ref)
                        scale = max(abs(ref), mp.mpf(1))
                        if d / scale > worst:
                            worst, worst_shape = d / scale, (shape, k + 1, r, c)
                        checked += 1
                        if d / scale > tol:
                            print(f"  FAIL {shape} T_{k+1}[{r},{c}]: "
                                  f"{G[r, c]} vs {ref}  (rel {d / scale})")
                            return 1
    print(f"hoefsmit_mpfr self-test: {checked} entries agree with the symbolic "
          f"builder at {dps} dps")
    print(f"  worst relative difference {mp.nstr(worst, 6)} at {worst_shape}")
    return 0


if __name__ == "__main__":
    raise SystemExit(_selftest())
