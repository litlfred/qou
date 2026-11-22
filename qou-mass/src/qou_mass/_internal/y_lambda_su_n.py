#!/usr/bin/env python3
# polynomial_q_not_applicable: closed-form weights in q; no symbolic-q polynomial output.
"""y_λ for the SU(N) Markov trace — the N-generalisation of `y_lambda_at`.

`wedderburn_jones_markov.y_lambda_at(n, q)` computes ONE member of the Ocneanu
family. Until 2026-08-09 that was convention **C** of
`docs/coordination/trace-convention-registry.md`, the full-Hecke Ocneanu / Wenzl
z-trace at `z = 1/(q^{1/2}+q^{-1/2})`; C was then excised and it returns
convention **D** (`z = q³/(q²+1)`), which is the `N = 2` member of the family
below. There is still no `N` argument and no `z` argument — the member is baked
in, and both of its paths now route here (numeric via `y_lambda_su_n`, symbolic
via `y_lambda_su_n_symbolic`).

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

## What this module found

Validated against the registry: at `N = 2` these weights reproduce convention
**D** (SU(2)/Temperley–Lieb, Jones) exactly — `(0.5054042, 0.2472979, 0)` at
`n = 3`, `y_{(1^3)} = 0` on the nose. That is the live statement: **D is the
production trace**, so the shipped pipeline *is* an `SU(N)` quantum-group trace,
at `N = 2`, carrying the row cap.

> **UPDATED 2026-08-09.** This section previously read "the production trace is
> convention **C**" and led with the measurement `N = 2.5995155…` — the real `N`
> reproducing C's `y_{(1^3)}/y_{(3)}` ratio, showing C sat between SU(2) and
> SU(3) and was no `SU(N)` trace at all. **C was excised from this branch**
> (commits `73311b57`, `33a6c7aa`), so that headline described a convention no
> longer in the pipeline. The C measurement is retained below as a historical
> finding — it is *why* C was excised — but it is no longer a statement about
> production. Nothing computational changed; `_y_lambda_at_convention_C_HISTORICAL`
> is the only remaining C path and it is unwired.
>
> **UPDATED 2026-08-09 (bean `qou-wgta`, item 9).** The line above was wrong in
> both halves. `_y_lambda_at_convention_C_HISTORICAL` was never a C
> *implementation* — it was a delegation to
> `schur_principal_mpmath.y_lambda_at_q0_mpmath`, which the excision had left
> on C — and it was not unwired, `main()` below called it. That function is now
> convention D, so C is preserved explicitly as
> `schur_principal_mpmath.y_lambda_at_q0_mpmath_convention_C_HISTORICAL` and
> `main()` quotes that directly. `_y_lambda_at_convention_C_HISTORICAL` is now
> genuinely unwired **and mislabelled** (it returns D); it is on the bean's
> do-not-touch list, so it is left for the owner.

Historical (pre-excision), kept because it is the evidence against C:

* C's weights were `(0.4153958, 0.2809296, 0.0227449)` and **C matched no
  integer N** — the implied real `N` was `2.5995155…`.
* C had `y_{(1^3)} ≠ 0`, so the C mass trace did **not** carry the `N = 2` row
  cap, and the deepest partition was never killed.
* The shorthand that the framework's `z` is "the Temperley–Lieb / SU(2) value"
  was **false under C** — that is convention D, at `z = q^3/(q^2+1) =
  0.6126880`, and `D ≠ C` is Lean-proved
  (`QOU.BraidsAndKnots.BorromeanTraceConventionSplit.conventionD_ne_conventionC`).
  The two differ by 195.8 ppm on `β_Bor`. Under D the shorthand is now correct.

This module itself is still read-only and wired into no production path. It is
the weight function the flavour channel would need at general `N`, plus the
`N = 2` cross-check on the shipped convention.

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

import mpmath as mp  # noqa: E402
from _precision import COMPUTE_DPS  # noqa: E402


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


# ── symbolic (exact) convention-D weights ────────────────────────────────
# Added 2026-08-09. `wedderburn_jones_markov.y_lambda_at(n, q_val=None)` — the
# symbolic path, ~155 consumers — was made to RAISE when convention C was
# excised, because returning C silently would have been worse. That left
# `deltalambda/a4_brunnian_deficit_closed_form.py` (which calls
# `y_lambda_at(4, None)`) with nowhere to go. These three functions are the
# missing symbolic D solver: the same hook-content formula as above, over
# `sympy` instead of `mpmath`, so the answer is an exact rational function of q.
#
# It is also strictly faster than the C path it replaces: C needed an ~18 min
# linear solve at n=4 (hence that producer's file cache); this is a product
# formula and returns instantly.


def q_int_sym(m, q):
    """Symbolic `[m]_q = (q^m − q^{−m})/(q − q^{−1})`, exactly.

    Balanced convention, matching `q_int`. For integer `m` the result is a
    Laurent polynomial; `cancel` puts it in canonical rational form.
    """
    import sympy as sp
    return sp.cancel(sp.together((q ** m - q ** (-m)) / (q - 1 / q)))


def schur_principal_sym(shape: tuple[int, ...], N: int, q):
    """Symbolic `s_λ(1, q, …, q^{N-1})` up to a q-power, by hook-content.

    Returns exactly `0` when `λ` has more than `N` rows: the cell `(N+1, 1)` has
    content `−N`, so the numerator picks up `[N + (−N)]_q = [0]_q = 0`. The row
    cap is therefore automatic here too, not imposed.
    """
    import sympy as sp
    num = sp.Integer(1)
    for c in contents(shape):
        num *= q_int_sym(N + c, q)
    den = sp.Integer(1)
    for h in hooks(shape):
        den *= q_int_sym(h, q)
    return sp.cancel(num / den)


def y_lambda_su_n_symbolic(n: int, q, N: int = 2) -> dict:
    """`{λ: y_λ}` for the SU(N) Markov trace on `H_n(q)`, EXACT in `q`.

    Symbolic twin of `y_lambda_su_n`, same normalisation `Σ_λ y_λ f^λ = 1`.
    `N = 2` is registry convention **D**; at that value `z_from_weights` returns
    `q³/(q²+1)` identically, which the self-test checks symbolically.
    """
    import sympy as sp
    shapes = partitions_of(n)
    s = {sh: schur_principal_sym(sh, N, q) for sh in shapes}
    Z = sp.cancel(sp.together(sum(s[sh] * f_lambda(sh) for sh in shapes)))
    if Z == 0:
        raise ValueError(f"degenerate normalisation at n={n}, N={N}")
    return {sh: sp.cancel(s[sh] / Z) for sh in shapes}


def z_from_weights(q: "mp.mpf", y: dict) -> "mp.mpf":
    """The Markov parameter implied by an `n = 2` weight system.

    `z = tr_M(σ) = y_{(2)}·q + y_{(1,1)}·(−q^{−1})`, and with the normalisation
    `y_{(2)} + y_{(1,1)} = 1` that is `y_{(2)}(q + q^{−1}) − q^{−1}` — the Lean
    `QOU.QBeta.InterfaceScalar.markov_param_determined`. So z is a CONSEQUENCE
    of the weights, never an independent input.
    """
    return y[(2,)] * q + y[(1, 1)] * (-1 / q)


# ── self-test ────────────────────────────────────────────────────────────
# The registry constants below MUST be parsed at full precision: at mpmath's
# default 15 dps they are rounded to 53 bits and are ALREADY WRONG when built
# (`module_const_precision_audit --strict` flags exactly REG_ZC / REG_ZD).
#
# They are built inside a LOCAL `mp.workdps(COMPUTE_DPS)`, NOT under a
# module-scope `set_compute_dps(50)`. That call used to sit here, and it
# ASSIGNS the global `mp.dps` — so merely importing this module (including the
# lazy import inside `wedderburn_jones_markov.y_lambda_at`) LOWERED every
# caller already running at 60/70 dps to 50 for the rest of the process.
# Measured: `paper_six_term_isotope_sweep` sat at 70 after import and at 50
# after its first `aK_v2` call, then serialized at OUTPUT_DPS = 60 — ten
# digits manufactured. Importing a library must not change the caller's
# precision in either direction; `workdps` restores it on exit.
with mp.workdps(COMPUTE_DPS):
    _Q = "1.1099785827513808075916690956107688798744991218736"
    # docs/coordination/trace-convention-registry.md, at the proton pin
    REG_C = (mp.mpf("0.4153958"), mp.mpf("0.2809296"), mp.mpf("0.0227449"))
    # ── convention-D constants at 50 dps ──────────────────────────────────────
    # RE-EMITTED 2026-09-04 (bean qou-90k2).  These were carried at 17 significant
    # digits, and REG_ZD's 17th digit was WRONG: it read ...524 where the correct
    # rounding is ...525.  It was not merely short — it was worse than plain
    # float64 (rel err 1.89e-17 against float64's 6.69e-18), i.e. a float64 value
    # truncated once more.  It is the residue of the historical mis-record the
    # registry doc's own §Provenance records ("z_D was recorded ...524365, correct
    # is ...525160"); the doc was corrected and the Python was not.
    #
    # It survived because the self-test cross-checked it at 1e-15 while every
    # INTERNAL check in the same function runs at 1e-25 — the one check tying this
    # module to the corpus's published number was pinned ten orders of magnitude
    # looser than its neighbours, so an error of 1.16e-17 passed by a factor of 86.
    # The tolerances below are now 1e-40, which is what makes these constants
    # load-bearing rather than decorative.
    #
    # Derived, not transcribed: z = q^3/(q^2+1) and the exact n=3 weights
    # y_(3) = (q^4+1)/(q^2+1)^2, y_(2,1) = q^2/(q^2+1)^2, y_(1^3) = 0, evaluated at
    # the 50-digit proton pin _Q.  Cross-checked against y_lambda_su_n(3, q, 2) at
    # 60 dps: agreement to 3e-62.  Regenerate the same way if _Q moves.
    REG_D = (mp.mpf("0.50540422650393080318755870324047227566035119774981"),
             mp.mpf("0.24729788674803459840622064837976386216982440112509"),
             mp.mpf("0"))
    REG_ZC = mp.mpf("0.49932033418369445241344268025766630375194816404153")
    REG_ZD = mp.mpf("0.61268803714646525159582986394589924802630839154509")


def self_test() -> int:
    # 60 dps, not 30: the registry cross-checks below are now at 1e-40, and a
    # 30-dps working precision cannot resolve a 1e-40 difference at all.
    mp.mp.dps = 60
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
        chk(f"N=2 reproduces registry convention D: {nm}", abs(g - r) < mp.mpf("1e-40"))
    chk("N=2 gives y_(1^3) = 0 EXACTLY (the row cap)", y3[(1, 1, 1)] == 0)

    # z implied at N = 2 must be convention D's z
    zD = z_from_weights(q, y_lambda_su_n(2, q, 2))
    chk("N=2 implies z_D = q³/(q²+1)", abs(zD - REG_ZD) < mp.mpf("1e-40"))
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

    # POST-EXCISION (2026-08-09): production is convention D, and D IS SU(2).
    # These three checks previously asserted the C state; C was excised on this
    # branch (73311b57, 33a6c7aa), so they now pin the live convention instead.
    # They are the regression guard against a silent slide back to C.
    from wedderburn_jones_markov import y_lambda_at
    prod = {k: mp.mpf(str(v)) for k, v in y_lambda_at(3, q).items()}
    chk("production y_λ matches registry D, not C",
        abs(prod[(3,)] - REG_D[0]) < mp.mpf("1e-40")
        and abs(prod[(1, 1, 1)] - REG_D[2]) < mp.mpf("1e-40"))
    chk("production y_(1^3) = 0 — D DOES carry the N=2 row cap",
        prod[(1, 1, 1)] == 0)
    chk("production IS SU(2) exactly", all(
        abs(y_lambda_su_n(3, q, 2)[s] - prod[s]) < mp.mpf("1e-25")
        for s in ((3,), (2, 1), (1, 1, 1))))
    for N in (3, 4, 5):
        y = y_lambda_su_n(3, q, N)
        chk(f"production ≠ SU({N})",
            abs(y[(3,)] - prod[(3,)]) > mp.mpf("1e-3"))

    # ── symbolic convention-D twin (added 2026-08-09) ────────────────────
    import sympy as sp
    qs = sp.Symbol("q", positive=True)
    qf = sp.Float(_Q, 50)
    # Compare at 50 dps, not the self-test's working 30: at dps=30 the NUMERIC
    # side is only good to ~1e-31, so a 30-dps comparison would cap the test's
    # resolution at round-off (measured 9.86e-32) and could not tell a correct
    # symbolic form from one wrong in the 32nd digit.
    _dps_save = mp.mp.dps
    mp.mp.dps = 50
    q50 = mp.mpf(_Q)
    for n_ in (2, 3, 4):
        ysym = y_lambda_su_n_symbolic(n_, qs, 2)
        ynum = y_lambda_su_n(n_, q50, 2)
        worst = max(abs(mp.mpf(str(sp.N(ysym[sh].subs(qs, qf), 50))) - ynum[sh])
                    for sh in ysym)
        chk(f"symbolic == numeric at n={n_} (worst {mp.nstr(worst, 3)})",
            worst < mp.mpf("1e-45"))
        chk(f"symbolic normalisation Sum y_l f^l = 1 at n={n_}",
            sp.simplify(sum(ysym[sh] * f_lambda(sh) for sh in ysym)) == 1)
        capped = [sh for sh in ysym if len(sh) > 2]
        chk(f"symbolic row cap: y_l = 0 for l with >2 rows at n={n_} "
            f"({len(capped)} shapes)",
            all(sp.simplify(ysym[sh]) == 0 for sh in capped))
    # the registry D value must fall out of the n=2 symbolic weights EXACTLY
    mp.mp.dps = _dps_save
    y2s = y_lambda_su_n_symbolic(2, qs, 2)
    zsym = sp.simplify(y2s[(2,)] * qs + y2s[(1, 1)] * (-1 / qs))
    chk("symbolic z == q^3/(q^2+1) EXACTLY (registry convention D)",
        sp.simplify(zsym - qs ** 3 / (qs ** 2 + 1)) == 0)

    total = 43
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
    print(f" {'D':>3} " + "".join(f"{mp.nstr(prod.get(s, mp.mpf(0)), 10):>17}"
                                  for s in shapes)
          + "   <- production (registry convention D = SU(2))")

    if n == 3:
        print("\n" + "-" * 78)
        print(" where does the EXCISED convention C sit?  (historical)")
        print("-" * 78)
        # Source of C: schur_principal_mpmath's explicitly-preserved C pair.
        #
        # This used to read wedderburn_jones_markov's
        # `_y_lambda_at_convention_C_HISTORICAL`, which was only ever C
        # because it delegated to `schur_principal_mpmath.y_lambda_at_q0_mpmath`
        # -- and that function moved to convention D in the qou-wgta sweep
        # (2026-08-09).  Left pointing there, this block printed
        # "C's y_(1³)/y_(3) = 0.0" and "real N reproducing it = 2.0" under a
        # banner reading NON-INTEGER: a D-vs-D comparison asserting the
        # opposite of the finding it exists to display.
        #
        # A convention that no longer exists in the pipeline still has to be
        # *quotable*, so C is kept as a named historical implementation rather
        # than inferred from whatever happens to be unswitched.
        from schur_principal_mpmath import (
            y_lambda_at_q0_mpmath_convention_C_HISTORICAL as _yC)
        cprod = {k: mp.mpf(str(v)) for k, v in _yC(n, q).items()}
        tgt = cprod[(1, 1, 1)] / cprod[(3,)]
        def f(N):
            y = y_lambda_su_n(3, q, N)
            return y[(1, 1, 1)] / y[(3,)] - tgt
        Nstar = mp.findroot(f, mp.mpf("2.6"))
        print(f" C's y_(1³)/y_(3)          = {mp.nstr(tgt, 12)}")
        print(f" real N reproducing it     = {mp.nstr(Nstar, 12)}")
        print(" NON-INTEGER, between SU(2) and SU(3): C was not an SU(N)")
        print(" quantum-group trace and did not carry the N=2 row cap.")
        print(" That is why it was excised. Production (D) is SU(2) exactly.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
