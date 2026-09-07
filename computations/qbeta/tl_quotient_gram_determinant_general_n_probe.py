#!/usr/bin/env python3
"""`det G_TL(n)` in closed form at n = 3, 4, 5 — non-singular for EVERY real q > 0.

Bean `qou-8iru` (the TL_n compute move) / `qou-cds2` (the Gram singularity).
Formalize-first brick, run BEFORE the remaining engine work, per AGENTS.md §3.3.

## The gap this closes

PR #5572 (`tl3_gram_nonsingular_probe.py`) established the n = 3 determinant in
closed form and read off **scope-(b)**: the TL_3 quotient form is non-singular
for *every real q > 0*, not merely generically.

PR #5592 (`tl_quotient_gram_probe.py`) then built the general-`n` quotient form
in `pyhecke.tl` — but was explicit that at n >= 4 it could only claim
**non-singular over Q(q)**, i.e. "the determinant is not identically zero",
because it evaluated the rank at a single rational point.  Its own scope note
says so, and `qou-8iru` records the residual as open:

    "Open: the symbolic det G_TL(n) for n >= 4, which is what would upgrade
     those to the n=3 scope-(b) statement."

The bean also records that the symbolic route was **attempted and abandoned** —
sympy's unsimplified rational-function sums blow up and it was killed at
> 10 min.  That is a statement about the *arithmetic domain*, not about the
problem: the obstruction is doing linear algebra over Q(q) with unnormalised
fractions.

## The move that makes it cheap

The entries of `G_TL(n)` are rational in `q` with denominators that are pure
powers of `(q^2 + 1)` — measured, not assumed (leg 1).  So clearing a single
common denominator `D = (q^2+1)^(n-1)` turns the matrix into one over the
*polynomial ring* Z[q], where a fraction-free Bareiss determinant is fast:

    det G_TL(n) = det( D * G_TL(n) ) / D^dim,      dim = Catalan(n)

n = 4 takes < 1 s and n = 5 about 80 s, against the > 10 min that failed over
Q(q).  Nothing here is a better algorithm — it is the same determinant in a
domain where the coefficients do not grow.

## Result

    n=3   -(q^4+1) (q^2-q+1)^4 (q^2+q+1)^4 / (q^2+1)^10
    n=4   +(q^4+1)^6 (q^2-q+1)^13 (q^2+q+1)^13 Phi_10 Phi_5 / (q^2+1)^42
    n=5   +(q^4+1)^26 (q^2-q+1)^41 (q^2+q+1)^41 Phi_12 Phi_10^8 Phi_5^8
                                                            / (q^2+1)^168

with `Phi_5 = q^4+q^3+q^2+q+1`, `Phi_10 = q^4-q^3+q^2-q+1`, `Phi_12 = q^4-q^2+1`.

**Every irreducible factor is strictly positive on q > 0**, so the quotient
form is non-singular for every real q > 0 at n = 3, 4 and 5 — the scope-(b)
upgrade.  This is checked by exact Sturm-sequence root counting on the interval
`(0, oo)` (leg 3), not by inspecting coefficient signs by eye: two of the
factors (`q^2-q+1`, and `Phi_10`) *have* negative coefficients and are positive
anyway, so eyeballing would have been wrong.

## Two independent cross-checks that the determinant is right

**1. n = 3 reproduces PR #5572 byte-for-byte** (leg 2), from general-`n` code
through a different arithmetic domain than either earlier probe used.

**2. The Wedderburn law reproduces the SIGN, which is not free** (leg 5).  The
change-of-basis law `det_B(G) = det(P)^2 det_W(G)` predicts that

    det G_TL(n) / prod_lambda y_lambda^(dim_lambda^2)

is a perfect square *up to a sign*, and predicts the sign exactly.  On a
Wedderburn block `M_d` with weight `y` the trace pairing is
`<e_ij, e_kl> = y * delta_jk delta_il`, i.e. `y` times the transpose
permutation, whose determinant is `(-1)^(d(d-1)/2)`.  So

    sign( det G_TL(n) )  =  prod over surviving lambda of  (-1)^(d_lambda(d_lambda-1)/2)

    n=3  dims (1,2)    -> (+)(-)     = -1     matches the leading minus
    n=4  dims (1,3,2)  -> (+)(-)(-)  = +1
    n=5  dims (1,4,5)  -> (+)(+)(+)  = +1

All three agree.  A determinant that was wrong by any factor other than a
perfect square with exactly this sign would have failed here, so the leg is a
genuine check and not a restatement.

## Scope — stated narrowly

- **Scope-(b) structural, n = 3, 4, 5 only**, citing a proved invariant (the
  determinant, exactly over Q(q), plus exact real-root counts).  It does *not*
  establish anything for n >= 6; the determinant grows fast and n = 6 was not
  attempted.
- The **sign** claims are about the *bilinear* determinant.  They say nothing
  about the signature of the Hecke `*`-form `T_w* = T_{w^-1}`, which is a
  different pairing — quote `QOU.QBeta.GramSignature` only after its in-file
  retraction (commit 748ba9b1), where D is `(5,0,1)` positive semidefinite on
  the full basis.  A negative bilinear determinant at n = 3 is the transpose
  permutation's sign, not an indefiniteness claim.
- **Nothing is migrated and nothing is wired.**  `gram.py`'s `G_PINV`,
  `gram.rs`'s rank-one shift, `gram_inverse()`'s raise and
  `confinement-operator-selection.py`'s `_pg_safe_inverse` are all untouched.

Everything is exact sympy over Q(q) and exact Sturm root counting.  No float64,
no q_0 evaluation, no anchor — so the result is pin-independent and carries no
muon/proton layer question (AGENTS.md: probes are not exempt from NO-FLOAT64).
"""
from __future__ import annotations

import os as _os_sidu  # noqa: E402 -- atomic witness write (qou-sidu)

import json
import os
import sys
import time
from math import comb

import sympy as sp
from sympy.polys.domains import ZZ
from sympy.polys.matrices import DomainMatrix

sys.path.insert(
    0,
    os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
        "tools",
        "pyhecke",
        "python",
    ),
)

from pyhecke import tl  # noqa: E402

q = sp.Symbol("q")

_CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    _CHECKS.append((name, bool(passed), detail))
    print(f"[{'PASS' if passed else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))


# ══════════════════════════════════════════════════════════════
# the determinant, over Z[q] rather than Q(q)
# ══════════════════════════════════════════════════════════════


def _cleared(n: int):
    """`(M, D)` with `M = D * G_TL(n)` over Z[q] and `D` the common denominator."""
    rows = tl.tl_gram(n, q, one=sp.Integer(1))
    rows = [[sp.cancel(e) for e in r] for r in rows]
    dens = [sp.fraction(e)[1] for r in rows for e in r]
    D = sp.lcm(dens)
    M = [[sp.expand(sp.cancel(e * D)) for e in r] for r in rows]
    return M, sp.cancel(D)


def det_tl(n: int):
    """`det G_TL(n)` exactly, by fraction-free Bareiss over Z[q]."""
    M, D = _cleared(n)
    dm = DomainMatrix.from_Matrix(sp.Matrix(M)).convert_to(ZZ[q])
    return sp.cancel(dm.det().as_expr() / D ** len(M))


# ══════════════════════════════════════════════════════════════
# the Wedderburn prediction
# ══════════════════════════════════════════════════════════════


def qint(m: int):
    """`[m]_q` as a rational function — no `Real.sqrt`, no evaluation."""
    return sp.cancel((q ** m - q ** (-m)) / (q - q ** (-1)))


def surviving_blocks(n: int):
    """`(lambda, dim)` for the two-row-or-fewer partitions — the TL blocks.

    `y_lambda = 0` for `l(lambda) >= 3` under convention D
    (`QOU.QBeta.WenzlWeight.conventionD_weight_eq_zero_iff`, sorry-free, all n),
    which is what makes the quotient Temperley-Lieb.  `dim (n-k,k)` is the
    ballot number `C(n,k) - C(n,k-1)`.
    """
    out = []
    for k in range(0, n // 2 + 1):
        dim = comb(n, k) - (comb(n, k - 1) if k > 0 else 0)
        out.append(((n - k, k) if k else (n,), dim))
    return out


def det_wedderburn(n: int):
    """`prod_lambda y_lambda^(dim^2)` from the closed form `y_(n-k,k) = [n-2k+1]/[2]^n`."""
    acc = sp.Integer(1)
    for k in range(0, n // 2 + 1):
        dim = comb(n, k) - (comb(n, k - 1) if k > 0 else 0)
        acc *= sp.cancel(qint(n - 2 * k + 1) / qint(2) ** n) ** (dim * dim)
    return sp.cancel(acc)


def predicted_sign(n: int) -> int:
    """`prod_lambda (-1)^(d(d-1)/2)` — the transpose permutation on each block."""
    s = 1
    for _lam, d in surviving_blocks(n):
        s *= (-1) ** ((d * (d - 1)) // 2)
    return s


# ══════════════════════════════════════════════════════════════
# exact positivity on (0, oo)
# ══════════════════════════════════════════════════════════════


def positive_roots(poly_expr) -> int:
    """Number of real roots in `(0, oo)`, counted exactly by Sturm sequence.

    `Poly.count_roots` is exact integer arithmetic on the coefficients -- this
    is NOT a numerical root find, and NOT a coefficient-sign heuristic.  The
    distinction matters here: `q^2 - q + 1` and `q^4 - q^3 + q^2 - q + 1` both
    carry negative coefficients and are both strictly positive on q > 0.
    """
    return sp.Poly(poly_expr, q).count_roots(0, sp.oo)


def _factor_list(expr):
    """Irreducible factors (numerator and denominator) with multiplicities."""
    num, den = sp.fraction(sp.cancel(expr))
    out = []
    for part, where in ((num, "num"), (den, "den")):
        c, facs = sp.factor_list(part)
        out.append((where, sp.nsimplify(c), [(f, m) for f, m in facs]))
    return out


# ══════════════════════════════════════════════════════════════

# PR #5572's n=3 closed form, transcribed for a cross-implementation check.
DET_TL3_REFERENCE = -(q ** 4 + 1) * (q ** 2 - q + 1) ** 4 * (q ** 2 + q + 1) ** 4 / (q ** 2 + 1) ** 10


def main() -> int:
    max_n = int(os.environ.get("TL_DET_MAX_N", "5"))
    dets: dict[int, sp.Expr] = {}
    timings: dict[int, float] = {}
    payload: dict[str, object] = {}

    # ── 1. the denominators are pure powers of (q^2+1) ─────────────────────
    # This is what makes the Z[q] route available at all.  Measured per n, not
    # assumed: if an entry ever acquired a q^-k the clearing step would be wrong
    # and every determinant below with it.
    dens_ok = True
    den_report = {}
    for n in range(3, max_n + 1):
        _M, D = _cleared(n)
        expected = (q ** 2 + 1) ** (n - 1)
        same = sp.simplify(D - expected) == 0
        den_report[n] = str(sp.factor(D))
        dens_ok = dens_ok and same
    check(
        "entry_denominators_are_exactly_(q^2+1)^(n-1)_so_the_Z[q]_route_is_valid",
        dens_ok,
        f"common denominators: {den_report}; no q^-k appears, so clearing is exact",
    )
    payload["common_denominator_by_n"] = den_report

    # ── 2. compute, and reproduce #5572 at n=3 ─────────────────────────────
    for n in range(3, max_n + 1):
        t0 = time.time()
        dets[n] = det_tl(n)
        timings[n] = time.time() - t0
        print(f"    n={n}: det computed in {timings[n]:.1f}s")

    check(
        "n3_reproduces_PR5572_closed_form_from_general_n_code",
        sp.simplify(dets[3] - DET_TL3_REFERENCE) == 0,
        "general-n Bareiss-over-Z[q] agrees with #5572's transcribed n=3 "
        "determinant exactly -- a different arithmetic domain, so this is a "
        "cross-implementation check on the METHOD, not internal consistency",
    )

    # ── 3. non-singular for EVERY real q > 0 ───────────────────────────────
    # The claim that upgrades n>=4 from "generic in q" (#5592) to scope-(b).
    for n in range(3, max_n + 1):
        facs = _factor_list(dets[n])
        bad = []
        for _where, _c, fl in facs:
            for f, _m in fl:
                if f.free_symbols and positive_roots(f) != 0:
                    bad.append(str(f))
        check(
            f"det_G_TL({n})_has_NO_real_root_with_q_gt_0__scope_b",
            not bad,
            f"every irreducible factor is root-free on (0,oo) by exact Sturm "
            f"counting; offenders: {bad or 'none'}",
        )

    # ── 4. the closed forms, recorded ──────────────────────────────────────
    forms = {n: str(sp.factor(dets[n])) for n in dets}
    for n in sorted(forms):
        print(f"    det G_TL({n}) = {forms[n]}")
    payload["det_closed_form"] = forms
    payload["seconds_by_n"] = {str(k): round(v, 3) for k, v in timings.items()}

    # ── 5. Wedderburn law: perfect square TIMES the predicted sign ─────────
    # The sign is the real content of this leg -- a perfect-square ratio alone
    # would be much weaker, since |ratio| being a square is nearly automatic.
    ratios = {}
    for n in range(3, max_n + 1):
        ratio = sp.cancel(dets[n] / det_wedderburn(n))
        # `factor_list` wants a polynomial, and the ratio is a rational
        # function -- split it and test numerator and denominator separately.
        r_num, r_den = sp.fraction(ratio)
        c_num, f_num = sp.factor_list(sp.expand(r_num))
        c_den, f_den = sp.factor_list(sp.expand(r_den))
        # every exponent even (both halves), and the rational constant is +/- 1
        all_even = all(m % 2 == 0 for _f, m in f_num + f_den)
        const = sp.nsimplify(c_num / c_den)
        sgn = predicted_sign(n)
        sign_ok = sp.simplify(sp.Abs(const) - 1) == 0 and sp.sign(const) == sgn
        c = const
        ratios[n] = str(sp.factor(ratio))
        dims = [d for _l, d in surviving_blocks(n)]
        check(
            f"n{n}_wedderburn_law_ratio_is_a_perfect_square_times_the_transpose_sign",
            all_even and sign_ok,
            f"dims {dims} -> predicted sign {sgn:+d}; ratio constant {c}; "
            f"all factor multiplicities even: {all_even}",
        )
    payload["det_over_wedderburn_ratio"] = ratios
    payload["predicted_sign_by_n"] = {str(n): predicted_sign(n) for n in dets}

    # ── 6. the surviving-block dimensions really are Catalan ───────────────
    # Ties the determinant back to qou-8iru's original measurement: it is the
    # <=2-row partitions that survive, and their dim^2 sum to Catalan(n).
    cat_ok = all(
        sum(d * d for _l, d in surviving_blocks(n)) == tl.catalan(n)
        and len(tl.tl_basis(n)) == tl.catalan(n)
        for n in range(3, max_n + 1)
    )
    check(
        "surviving_block_dims_squared_sum_to_Catalan_n_eq_quotient_dim",
        cat_ok,
        "; ".join(
            f"n={n}: dims {[d for _l, d in surviving_blocks(n)]} -> "
            f"{sum(d*d for _l,d in surviving_blocks(n))} = Catalan({n})"
            for n in range(3, max_n + 1)
        ),
    )

    # ── witness ────────────────────────────────────────────────────────────
    n_fail = sum(1 for _n, p, _d in _CHECKS if not p)
    payload["checks"] = [{"name": n, "pass": p, "detail": d} for n, p, d in _CHECKS]
    payload["max_n"] = max_n
    payload["scope"] = (
        "scope-(b) structural for every real q > 0 at n=3,4,5 only; nothing "
        "attempted or claimed at n>=6. Exact sympy over Q(q) plus exact Sturm "
        "root counting. No float64, no q_0 evaluation, no anchor -- "
        "pin-independent. Migrates no consumer."
    )
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "tl-quotient-gram-determinant-general-n.probe.json")
    # Atomic write (bean `qou-sidu`): serialize to a sibling temp file and
    # `os.replace` it into position. `open(..., "w")` TRUNCATES before the
    # dump runs, so any exception in between leaves the committed witness
    # empty or partial -- the shape that emptied 22 witnesses to zero bytes
    # in one `producer_importability_audit` run. `os.replace` is atomic on
    # POSIX within a filesystem, hence a SIBLING temp file.
    _wpath_sidu = out
    _wtmp_sidu = str(_wpath_sidu) + ".tmp"
    with open(_wtmp_sidu, "w") as fh:
        json.dump(payload, fh, indent=2, sort_keys=True)
        fh.write("\n")

    _os_sidu.replace(_wtmp_sidu, _wpath_sidu)
    print()
    print("=== det G_TL(n): the n>=4 scope upgrade ===")
    print(
        f"VERDICT: {len(_CHECKS) - n_fail}/{len(_CHECKS)} PASS. The TL quotient "
        f"form's determinant is now known in closed form at "
        f"n = {', '.join(str(k) for k in sorted(dets))}, and every irreducible "
        "factor is root-free on q > 0 by exact Sturm "
        "counting. That upgrades n >= 4 from #5592's 'non-singular "
        "over Q(q)' to the n = 3 scope-(b) statement: non-singular for EVERY "
        "real q > 0. The Wedderburn change-of-basis law reproduces the sign at "
        "every n measured, from the transpose-permutation signature, which is the "
        "check that would have caught a wrong determinant. Nothing is migrated: "
        "G_PINV, gram.rs's rank-one shift, gram_inverse()'s raise and "
        "_pg_safe_inverse are untouched."
    )
    print(f"    probe record: {os.path.relpath(out)}")
    return 1 if n_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
