---
# qou-gxsd
title: 'mp.mpf(repr(x)) is a latent trap at 73 live sites: repr is wrong for str, Decimal and numpy scalars, and str is identical for float'
status: todo
type: bug
created_at: 2026-09-07T10:44:14Z
updated_at: 2026-09-07T10:44:14Z
---

Found while regenerating witnesses after the 435-commit main merge (bean qou-uiut's branch).

`computations/probe_option_e_phase2_crystal_vertex_candidates.py:141` died with
`ValueError` from mpmath's `MPZ`:

    chi_w0 = mp.mpf(repr(h6_block["chi_lambda_w0_direct"]))

The field WAS a float. Under NO-FLOAT64 its producer converted it to a 50-digit
`fmt` string, and `repr` of a str keeps the QUOTES — mpmath is handed
"'4.783...'" and rejects it. The probe has been dead at that line since the
upstream conversion. Fixed there with `str`.

## The general fact, measured

`str` and `repr` are IDENTICAL for float and int in Python 3 (both give the
shortest round-tripping form), and `repr` is WRONG for three types this corpus
actually passes:

    str        repr('1.23')            -> "'1.23'"          quotes -> MPZ error
    Decimal    repr(Decimal('1.5'))    -> "Decimal('1.5')"  unparseable
    numpy      repr(np.float64(0.1))   -> 'np.float64(0.1)' unparseable (numpy 2.x)

So `mp.mpf(str(x))` strictly dominates `mp.mpf(repr(x))`: identical output
wherever repr is correct, correct in three cases where it is not.

## Scope

**73 live sites** (excluding `_deprecated/`), concentrated in
`computations/deltalambda/`. Enumerate with:

    grep -rn 'mp\\.mpf(repr(' --include=*.py computations/ qou-mass/ tools/ | grep -v _deprecated

## Why this is safe to sweep, and how to prove it

The change is NUMERICALLY INERT wherever the value is a float, because the
string produced is byte-identical. So a sweep should move no witness digit.
That is the gate: regenerate a sample and require byte-identity apart from
timestamps. Anywhere a number DOES move, the site was reading a non-float and
was already broken or already wrong — which is a finding, not a regression.

## Do NOT

Do not "fix" this by switching to `float(x)` — that caps a 50-digit witness
string at 53 bits, which is the defect NO-FLOAT64 exists to prevent, and it
would be invisible because the value still parses.

## Note on the counter-argument

`codata_constants._ame_binding_mev` deliberately documents `repr` (not `str`)
on a parsed float as "the shortest round-tripping form". That reasoning is
correct and unaffected: for a float the two are the same, so switching to
`str` keeps that property and adds the three cases above.
