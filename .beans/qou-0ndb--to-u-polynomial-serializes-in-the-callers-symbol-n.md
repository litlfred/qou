---
# qou-0ndb
title: to_u_polynomial serializes in the CALLER's symbol name — two copies disagree (u vs check_q), 3 consumers broke
status: todo
type: bug
created_at: 2026-08-10T02:36:12Z
updated_at: 2026-08-10T02:36:12Z
---


## The finding

`to_u_polynomial` returns `str(...)` of a sympy expression built in **whatever
symbol the caller passed**, so the variable name in the serialized string is a
property of the call site, not of the format. There are two copies, and they
disagree:

    computations/probes/qbeta_habiro_phi8_squared_from_z_squared_probe.py:78
        def to_u_polynomial(expr_in_q, q, u)          → strings say "u"

    computations/habiro/habiro_coefficients_atomic.py:158
        def to_u_polynomial(expr_in_q, q, check_q)    → strings say "check_q"

The second writes `p_in_u` / `denom_in_u` into
`habiro-coefficients-atomic.witness.json` — fields whose NAMES say `u` while
their CONTENTS say `check_q`.

## What it cost — three consumers, and the failure is silent

Any consumer doing `sp.sympify(s)` without `locals` gets a fresh free symbol.
`.subs(u, ...)` then matches nothing and **no-ops** — no exception, the
expression simply stays symbolic until something later tries to make a number of
it:

    _habiro_coefficient_extract.py   2 sites   →  NaN in tr_M_at_q0_via_u_poly
                                                  and tr_M_at_q0_rel_err
    term6_full_pole_sum.py           1 site    →  "Cannot convert expression to
                                                  float"; producer DEAD on main

All three were fixed the same way, by teaching each consumer both names:

    sp.sympify(s, locals={"u": u, "check_q": u})

That is three patches for one defect, and it only works because someone
eventually noticed which symbol the producer had used. A fourth consumer written
tomorrow starts from the same trap.

## Fix at the source, not at each reader

Either:

  * **render in one fixed name.** Have `to_u_polynomial` build its output string
    against a canonical `Symbol('u')` regardless of the symbol it was handed —
    the parameter then names the *substitution* variable, not the *output
    format*; or
  * **record the name.** Emit `p_in_u_symbol: "u"` beside `p_in_u` so a consumer
    can parse without guessing.

The first is better: it makes the string self-describing and needs no consumer
change beyond deleting the two-name `locals` workarounds. The second is
compatible with witnesses already on disk, which the first is not — the
`check_q` strings in `habiro-coefficients-atomic.witness.json` stay `check_q`
until that witness is regenerated, so whichever route is taken, **the existing
two-name `locals` must stay** until every affected witness has been rewritten.

## Also worth deciding

Two copies of a function with the same name, different parameter names, and the
same job is itself the bug's enabling condition. Whether they should be one
shared helper is a separate call, but they should at least not disagree about
what their output looks like.
