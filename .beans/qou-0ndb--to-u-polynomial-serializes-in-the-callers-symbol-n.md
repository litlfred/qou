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

---

## FIXED AT THE SOURCE — serialization is now canonical

Chosen route: **render in one fixed name**, the first of the two options above.
The witness fields are called `p_in_u` / `denom_in_u`, so their strings now say
`u` regardless of which symbol the producer computed with.

    computations/habiro/habiro_coefficients_atomic.py

    U_CANONICAL = sp.Symbol('u', positive=True, real=True)

    def str_in_u(expr, sym) -> str:
        """Serialize `expr` (written in `sym`) as a string in the canonical `u`."""
        if sym == U_CANONICAL:
            return str(expr)
        return str(sp.sympify(expr).subs(sym, U_CANONICAL))

Applied at every site that turns an expression into text:

    to_u_polynomial      -> returns `denom` via str_in_u  (both return paths)
    cyclotomic_expansion -> "a_m": str_in_u(...)          ← the field it rode on
    analyse_atomic_braid -> "p_in_u": str_in_u(...)
    _habiro_coefficient_extract.analyse_atom -> same, routed through str_in_u
                            even though its symbol IS canonical, so the
                            invariant is stated at the site rather than held in
                            someone's head

The in-memory expression deliberately keeps the caller's symbol — callers go on
computing with it. Only the SERIALIZED form is normalised, which is the only
part consumers parse.

### Verified: the two call sites now produce identical text

    caller symbol = check_q     caller symbol = u
      denom_in_u  u**4 - u**2 + 1      u**4 - u**2 + 1
      a_1         -u - 1               -u - 1
      p_in_u      u**2 + 1             u**2 + 1
      reconstruct == p   True                 True

and end-to-end, proton / neutron / deuteron still reconstruct `True` and the
mirror-pair Φ₈ multiplicities still match 2⌊(A−1)/2⌋ on all five tested pairs.

### The two-name `locals` must STAY, and here is the exact reason

Every witness currently on disk was written by the old code, so its strings say
`check_q` where the producer used that symbol. `reconstruct`'s
`locals={"u": check_q, "check_q": check_q}` and each `load_a_m`'s
`locals={'u': u, 'check_q': u}` are what let those old files still parse. Remove
them before every affected witness has been regenerated and the corpus breaks
silently — the same silent failure this bean is about, in the other direction.

Retire the workaround only after a full regeneration, and check the strings
rather than assuming.

## Still open

The second copy — `computations/probes/qbeta_habiro_phi8_squared_from_z_squared_probe.py:78`,
`def to_u_polynomial(expr_in_q, q, u)` — is untouched. It takes `u` already, so
it emits canonical text by luck rather than by construction, and it is a second
implementation of the same function that can drift again. Whether the two should
be one shared helper is the open call; they should at minimum not be able to
disagree about their output format.
