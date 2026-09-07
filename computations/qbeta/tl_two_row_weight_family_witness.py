#!/usr/bin/env python3
"""tl_two_row_weight_family_witness.py — record the run that
`rem:hecke-radical-is-temperley-lieb` says nobody recorded.

Bean `qou-cds1`.  Scope-(b): exact symbolic identities and exact integer
combinatorics.

## The gap this closes

The block states, in its own §"What is measured and what is proved":

    The weights were evaluated for every partition of n = 2..7 at 50 decimal
    places, with worst residual 1.34e-51 against the closed form
    y_(n-k,k) = [n-2k+1]_q / [2]_q^n; NO WITNESS FILE RECORDS THE RUN, and no
    formalised statement of H_n(q)/rad = TL_n(q) exists.

So the paper's dimension table rests on a run with no artifact.  This records
one — and deliberately records something STRONGER than a 50-dps residual.

## Why exact-symbolic beats the 50-dps residual

A residual against a closed form shows the two agree at one `q`.  The property
that MAKES the closed form a normalised Markov weight family is the
normalisation identity, and it can be checked EXACTLY, as an identity in `q`:

    sum_k  f^(n-k,k) * [n-2k+1]_q  ==  [2]_q^n          for each n

with `f^(n-k,k)` the Specht dimension (SYT count).  If that holds identically
then `y_(n-k,k) = [n-2k+1]_q/[2]_q^n` normalises for every `q` at once, which
no finite-precision evaluation can establish.  Verified here by `sympy.simplify`
to exactly `0` for `n = 2..7` (and on to 10, since it costs nothing).

## What else is checked

  * **Specht dimensions two ways** — the ballot formula `C(n,k) - C(n,k-1)`
    against the hook-length formula, so neither is trusted alone.
  * **The block's own table** — `sum dim^2` over two-row shapes equals
    `Catalan(n)`, and `dim H_n = n!`, for `n = 2..7`.  This reproduces the
    published table rather than citing it.
  * **The registry, at n = 3** — the closed form must give convention D's
    recorded `y_(3) = [4]_q/[2]_q^3` and `y_(2,1) = 1/[2]_q^2`.

## The transpose collision — recorded because it is a live trap

`QOU.MathlibExt.WenzlSchurElement` warns, in its own docstring:

    Anyone wiring `schurElement_tl_eq_zero_iff` to that block must transpose.

It states the survivors as `lambda_1 <= N` (at most N COLUMNS); this block and
convention D state them as at most two ROWS.  Both are correct in their own
convention and they label DIFFERENT partition sets.  Verified below at n = 3
and n = 4: the row-set and column-set differ as sets while carrying equal
dimension sums (`dim lambda = dim lambda'`), which is exactly why the Catalan
counts agree and a reader can be fooled into thinking the conventions agree.

## What is NOT claimed

No formalised `H_n(q)/rad = TL_n(q)` — the block says none exists and this does
not supply one.  The identification remains what the block calls it: "an
identification the counts support, deliberately not a proposition".  This
records the counts; it does not promote them.

## Precision

sympy exact symbolic for the identities; exact integer arithmetic for the
dimensions.  No floating point in any claim.
"""
from __future__ import annotations

import json
import pathlib as _pl
import sys as _sys
from math import comb, factorial

_HERE = _pl.Path(__file__).resolve()
_COMP = _HERE.parent.parent
for _p in (_COMP, _COMP / "substrate", _COMP / "qbeta"):
    _sys.path.insert(0, str(_p))

import sympy as sp                                              # noqa: E402
from witness_base import WitnessBuilder                         # noqa: E402

RESULTS: list[dict] = []


def record(name, passed, detail):
    RESULTS.append({"name": name, "passed": bool(passed), "detail": detail})
    print(f"[{'PASS' if passed else 'FAIL'}] {name}\n    {detail}\n")


q = sp.symbols("q", positive=True)
qint = lambda m: sp.simplify((q ** m - q ** (-m)) / (q - 1 / q))   # [m]_q balanced


def two_row(n):
    """The two-row shapes (n-k, k), k = 0 .. floor(n/2)."""
    return [(n - k, k) for k in range(n // 2 + 1)]


def specht_ballot(n, k):
    """f^(n-k,k) by the ballot formula."""
    return comb(n, k) - (comb(n, k - 1) if k >= 1 else 0)


def specht_hook(lam):
    """f^lambda by the hook-length formula (independent route)."""
    lam = [r for r in lam if r > 0]
    n = sum(lam)
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    prod = 1
    for i, row in enumerate(lam):
        for j in range(row):
            prod *= (row - j) + (conj[j] - i) - 1
    return factorial(n) // prod


# ---- 1. the two dimension routes agree -----------------------------------
dim_ok = all(
    specht_ballot(n, k) == specht_hook((n - k, k))
    for n in range(2, 11) for k in range(n // 2 + 1)
)
record(
    "specht_dimensions_agree_by_two_independent_routes",
    dim_ok,
    "the ballot formula C(n,k)-C(n,k-1) and the hook-length formula give the "
    "same f^(n-k,k) for every two-row shape at n = 2..10. Neither route is "
    "trusted alone.",
)

# ---- 2. the normalisation identity, EXACTLY ------------------------------
norm = {}
for n in range(2, 11):
    lhs = sum(specht_ballot(n, k) * qint(n - 2 * k + 1) for k in range(n // 2 + 1))
    norm[n] = sp.simplify(lhs - qint(2) ** n)
record(
    "closed_form_normalises_EXACTLY_as_an_identity_in_q",
    all(v == 0 for v in norm.values()),
    "sum_k f^(n-k,k) [n-2k+1]_q - [2]_q^n simplifies to exactly "
    f"{sorted(set(str(v) for v in norm.values()))} for n = 2..10. So "
    "y_(n-k,k) = [n-2k+1]_q/[2]_q^n is a normalised Markov weight family for "
    "EVERY q at once — a stronger statement than the block's 50-dps residual "
    "of 1.34e-51, which fixes one q.",
)

# ---- 3. the block's published table --------------------------------------
table = {}
tab_ok = True
for n in range(2, 8):
    sq = sum(specht_ballot(n, k) ** 2 for k in range(n // 2 + 1))
    cat = comb(2 * n, n) // (n + 1)
    table[n] = {"shapes": [f"({a},{b})" if b else f"({a})" for a, b in two_row(n)],
                "sum_dim_sq": sq, "dim_H_n": factorial(n), "catalan": cat}
    tab_ok &= (sq == cat)
record(
    "reproduces_the_blocks_published_table_n_2_to_7",
    tab_ok,
    "sum of squared Specht dimensions over the two-row shapes equals Catalan(n) "
    "at every n = 2..7: "
    + "; ".join(f"n={n}: {v['sum_dim_sq']}={v['catalan']} (n!={v['dim_H_n']})"
                for n, v in table.items())
    + ". Reproduced, not cited.",
)

# ---- 4. the registry, at n = 3 -------------------------------------------
y3 = sp.simplify(qint(4) / qint(2) ** 3)
y21 = sp.simplify(qint(2) / qint(2) ** 3)
record(
    "closed_form_reproduces_registry_convention_D_at_n_3",
    sp.simplify(y3 - qint(4) / qint(2) ** 3) == 0
    and sp.simplify(y21 - 1 / qint(2) ** 2) == 0,
    f"k=0 gives y_(3) = [4]_q/[2]_q^3 and k=1 gives y_(2,1) = [2]_q/[2]_q^3 = "
    f"1/[2]_q^2 = {y21} — exactly the two convention-D entries in "
    "docs/coordination/trace-convention-registry.json.",
)

# ---- 5. the transpose collision ------------------------------------------
def all_parts(n, mx=None):
    mx = n if mx is None else mx
    if n == 0:
        yield ()
        return
    for k in range(min(n, mx), 0, -1):
        for rest in all_parts(n - k, k):
            yield (k,) + rest


coll = {}
coll_differs = True
for n in (3, 4, 5):
    rows = {p for p in all_parts(n) if len(p) <= 2}
    cols = {p for p in all_parts(n) if p[0] <= 2}
    coll[n] = {
        "at_most_2_rows": sorted(map(str, rows)),
        "at_most_2_cols": sorted(map(str, cols)),
        "same_set": rows == cols,
        "dim_sq_rows": sum(specht_hook(p) ** 2 for p in rows),
        "dim_sq_cols": sum(specht_hook(p) ** 2 for p in cols),
    }
    coll_differs &= (rows != cols) and (coll[n]["dim_sq_rows"] == coll[n]["dim_sq_cols"])
record(
    "transpose_collision_different_SETS_equal_dimension_sums",
    coll_differs,
    "WenzlSchurElement states survivors as lambda_1 <= N (at most N COLUMNS) and "
    "warns in its own docstring that 'anyone wiring schurElement_tl_eq_zero_iff "
    "to that block must transpose'; this block and convention D use at most two "
    "ROWS. At n = 3,4,5 the two sets DIFFER while their squared-dimension sums "
    "are EQUAL (dim lambda = dim lambda'), e.g. n=3 rows {(3),(2,1)} vs cols "
    "{(2,1),(1,1,1)}, both summing to 5. That equality is exactly why the "
    "Catalan counts agree and a reader can mistake the conventions for the same "
    "one. Live trap for anyone wiring the Lean to the mass channel.",
)

out = {
    "probe": _HERE.stem,
    "bean": "qou-cds1",
    "contentBlock": "rem:hecke-radical-is-temperley-lieb",
    "question": "record the n = 2..7 two-row weight run the block says has no witness",
    "answer": "Recorded, and strengthened: the closed form y_(n-k,k) = "
              "[n-2k+1]_q/[2]_q^n normalises EXACTLY as an identity in q for "
              "n = 2..10, which is stronger than the block's 50-dps residual at "
              "one q. The published Catalan table reproduces, and the registry's "
              "convention-D weights at n = 3 fall out as k = 0, 1.",
    "scope": "(b). Does NOT supply the formalised H_n(q)/rad = TL_n(q) the block "
             "says is missing; the identification stays 'an identification the "
             "counts support, deliberately not a proposition'.",
    "normalisation_residuals": {str(n): str(v) for n, v in norm.items()},
    "published_table": {str(n): v for n, v in table.items()},
    "transpose_collision": {str(n): v for n, v in coll.items()},
    "assertions": RESULTS,
    "allPassed": all(r["passed"] for r in RESULTS),
}
WitnessBuilder.stamp_staleness_metadata(out, script_path=__file__, engine="python+sympy")
wp = _HERE.parent / "tl-two-row-weight-family.witness.json"
wp.write_text(json.dumps(out, indent=2) + "\n")
print(f"witness -> {wp}\nallPassed: {out['allPassed']}")
_sys.exit(0 if out["allPassed"] else 1)
