---
# qou-0ndb
title: to_u_polynomial serializes in the CALLER's symbol name — two copies disagree (u vs check_q), 3 consumers broke
status: in-progress
type: bug
priority: normal
created_at: 2026-08-10T02:36:12Z
updated_at: 2026-08-10T18:46:22Z
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


## The open call is answered: the two copies do NOT become one helper

PR #4926. The bean left this as "a separate call". Resolved: normalise the
**serialization step** in the probe copy, do not merge the functions.

`probes/qbeta_habiro_phi8_squared_from_z_squared_probe.py` was serializing
three committed witness fields — `denom_in_u`, `p_in_u_factored`,
`diff_p_in_u` — with a bare `str()`. So the symbol name in those fields was
a property of one local variable (line 357), not of the format. It read `u`
only because that variable is spelled `u`: correct by luck, and one rename
from being wrong in exactly the way that cost this family four instances.

All three now route through `str_in_u`. That imports the canonical
SERIALIZER, not the canonical algorithm — the probe's local primitives stay
a deliberate mirror, which is what its own comment says they are for.

**Why not merge.** The defect never lived in the algorithm; the two copies
compute the same thing correctly. It lived entirely in the step that turns
an expression into text. Merging would collapse a deliberately
self-contained probe into a dependency on the module it mirrors to fix a
problem one line of that module already fixes. Normalising the one step
buys the invariant without the coupling.

**No witness regenerated, and none needed.** The probe's symbol is
`sp.Symbol("u", positive=True, real=True)`, which IS `U_CANONICAL`, so
`str_in_u` takes its identity fast path and returns exactly what `str()`
returned. Verified byte-identical on four representative expressions
including the zero case.

## The two-name `locals` workaround: retirement condition partly met

The bean's standing rule is that `locals={"u": u, "check_q": u}` must stay
until every affected witness is regenerated. Status after #4926:

* all 20 `_habiro_coefficient_extract.ATOMS` witnesses — regenerated;
* the 5 `extend_even_a_mirror_pair_test.EVEN_A_OPEN` witnesses — regenerated;
* `habiro-coefficients-atomic.witness.json` — **not** regenerated. Its
  `p_in_u` / `denom_in_u` still say `check_q`, and it is the upstream input
  every one of the above loads `τ_p` / `τ_n` from.

So the workaround **stays**. It is not yet a cleanup that can be done
safely, and the file that pins it is now identified rather than merely
suspected. Retiring it means regenerating the atomic witness first and
re-running everything downstream of it — a larger, separate arc.

## Consumer survey: which `check_q`-only readers are armed, and which are safe

Following the PR #4926 catch, surveyed every remaining consumer that
sympifies with `locals={"check_q": u}` alone. The discriminator is whether
the reader's own `u` carries sympy assumptions:

    sympify("3*u + 1") mints Symbol('u') with NO assumptions
      == sp.Symbol('u')                        ->  True   (SAFE)
      == sp.Symbol('u', positive=True, real=True) -> False (ARMED)

So a `check_q`-only reader breaks on a `u`-string **only if its own symbol
is assumption-bearing**. Survey:

    markov/markov_substrate_realizer.py       u = sp.symbols("u")     SAFE
    probes/habiro_frobenius_probe.py          u = sp.symbols("u")     SAFE
    probes/habiro_expansion_atomic_probe.py   u = sp.Symbol("u")      SAFE
    probes/probe_direct_cyclotomic_map.py     u = sp.Symbol('u')      SAFE
    probes/qbeta_habiro_phi8_squared…probe.py u = sp.Symbol("u", …)   ARMED  <- fixed

All four survivors read only `habiro-coefficients-atomic*.witness.json`,
which still says `check_q`, AND all four are assumption-free. The one
reader with an assumption-bearing `u` was the one that got caught.

**Consequence for the retirement condition.** Regenerating the atomic
witness (migrating it `check_q` -> `u`) will NOT break these four: a fresh
assumption-free `Symbol('u')` equals theirs. That removes the objection
that made the atomic migration look risky. It is still a real arc — the
atomic witness is the upstream every per-atom extract loads τ_p / τ_n
from — but the blocker is now scoped rather than open-ended.

The two-name `locals` still stays until that migration actually happens.

---

## The `check_q` retirement is BLOCKED, and by something bigger than naming

Attempted in PR #4948. Two blockers, the second decisive.

### Blocker 1 — it is 19 witnesses, not one

The retirement note above named `habiro-coefficients-atomic.witness.json`
as the pin. A corpus survey (parsed fields only, excluding prose mentions in
`description` / `verdict`) says the real figure is **19 witnesses carrying
`check_q` in fields a consumer sympifies**, ~750 fields total:

    154  qbeta/qbeta-habiro-cross-pair-factorization
    101  qbeta/qbeta-habiro-all-10-pairs-phi8-universality
     70  _deprecated/habiro-mirror-pair-li7-be7
     69  habiro-coefficients-extended
     67  probes/habiro-frobenius-probe
     65  qbeta/qbeta-habiro-delta-am-factorization
     62  qbeta/qbeta-habiro-delta-am-partial-sum-scan
     41  probes/qbeta-habiro-p8-identification
     30  probes/qbeta-habiro-recursion
     26  qbeta/qbeta-habiro-partition-followup
     12  kite-tail-reconciliation      12  _deprecated/kite_tail_reconciliation
     12  qbeta/qbeta-habiro-delta-a-m-pattern-probe
      8  habiro/habiro-q-difference-mode-solve      8  qbeta/…-wenzl-tower-zeta-n
      6  probes/qbeta-habiro-element-probe           4  qbeta/…-depth15-interpretation
      3  mass-from-q-symbolic                        3  habiro/habiro-q-difference-fourier

Each has its own producer and its own runtime. So the `locals` workaround
protects far more than the one file, and deleting it now would break every
reader of those 19.

### Blocker 2 — the atomic witness is convention-C stale, and it is qou-eea0's

I ran the atomic producer (`HABIRO_WITH_DEUTERON=1`) expecting a pure
`check_q` → `u` rename. **The values moved**, which is why this is recorded
rather than committed:

    proton   a_1        -74*check_q - 74      ->  -172*u - 172
             deg_p_u    40                    ->  44
             tr_M_in_q  half-integer powers   ->  integer powers
                        q**(39/2), q**(35/2)      q**22, q**20

The producer itself changed in only 3 commits since the witness was written
(2026-07-18), two of which are the serialization fixes that cannot move a
value. The cause is upstream: the **convention C → D migration**
(`70d1ade383` excise C tiers 2+3, `7665e0e4bf` regen 54 witnesses,
`8d32249ad6`). The committed atomic witness is convention **C**; the
producer layer is convention **D**.

**That regeneration belongs to `qou-eea0`, not here.** It is a live,
owner-directed campaign ("just do them all… I want to see total impact not
partial results", "work slowly diligently") with two hard constraints this
would have violated: *never two producers concurrently in one checkout*, and
*no commit until every producer has been attempted, so the impact is reported
whole rather than in fragments*. Committing one atomic regeneration is
exactly the fragmentary partial result that campaign exists to avoid.

**Reverted.** The witness on this branch is untouched.

### What this means for the retirement

Retiring the two-name `locals` is downstream of the convention-D migration,
not of a naming decision — the atomic witness has to be regenerated anyway,
and when `qou-eea0` regenerates it, it will come back in `u` for free
(the producer already routes every serialization site through `str_in_u`).
So the right sequencing is: **let qou-eea0 land, then retire.** Do not
regenerate the atomic witness outside that campaign.

### One thing this does NOT impugn

The whole 26-witness habiro family descends from the convention-C atomic
witness (`_load_p_n_symbolic` reads its `tr_M_in_q` for τ_p / τ_n), so the
family is convention-C too. PR #4926 did not introduce that and did not mask
it: it regenerated those witnesses from the *same* atomic input they had
always used, and verified the coefficients came back byte-identical. The Φ_8
correction there was to the *verification* code and is orthogonal to which
convention the coefficients encode. But the family being convention-C is a
real item, and it is material to qou-eea0's "total impact" accounting.

---

## Re-measured 2026-08-18, +1260 commits on. Still blocked — and the predicted mixed witness landed.

### The retirement condition has not moved

    witnesses with PARSED check_q:  19  ->  20      fields: ~750 -> 767

Not progress. The two-name `locals` still protects 20 readers and must stay.

### The mixed C/D atomic witness I warned about is now live on main

`qou-eea0` reached `habiro-coefficients-atomic.witness.json` (regenerated
2026-08-15, `scriptCommitSha 7bcfeb61d3`). It is **internally inconsistent**:

    row                 deg_p_u   symbol      convention
    p (proton, A=1)        44     u           D
    n (neutron, A=1)       36     u           D
    D (deuteron, A=2)      86     check_q     C     <-- stale row

This is exactly the failure recorded on this bean on 2026-08-10 and posted to
PR #4924 at the time:

> the default run computes **only p, n** and merge-preserves D from the prior
> file, so a default invocation would leave a *mixed* C/D witness — the
> deuteron flag is needed for a clean one.

A default run was used, `merge-preserve` kept the convention-C deuteron, and
the mixed file is on main. `HABIRO_WITH_DEUTERON=1` is what produces a clean
one.

Why it matters beyond tidiness: the merge-preserve comment in the producer
says `path_b_habiro_mass_probe` calibrates α_M off the **D row**. That reader
now takes a convention-C deuteron while τ_p / τ_n beside it are convention-D —
a straddle inside one witness, which AGENTS.md forbids by name.

### The 26-witness family is convention-C by descent, and now DISAGREES with its upstream

Measured, not inferred:

    family  proton tr_M_in_q :  q**(39/2) + q**(35/2) - ...   half-integer  = C
    atomic  proton tr_M_in_q :  q**22 + q**20 + 2*q**18 ...   integer       = D
    MATCH: False

Independently corroborated by the migration's own table in `b86f406962`:

    atom      C          D
    proton    1.065306   1.145760

and the family's committed `tr_M_at_q0` for the proton is `1.0653061442…` —
the C column exactly. So the family is C, unambiguously.

Before eea0 reached the atomic witness, atomic and family were both C, i.e.
*consistent*. They are now inconsistent. All 26 say `u` in their serialized
symbol (this bean's fix), which is why a `check_q` grep does not find them —
the symbol was normalised, the mathematics was not migrated. **A count of
files carrying a direct C fingerprint undercounts this family by 26**, which
is the point flagged to #4924 and still unaddressed.

### What this does to the Φ_8 result (PR #4926)

It stands **as a convention-C result** and is not retracted: it was computed
from a self-consistent C family, and the correction it made was to the
*verification* code (a mixed-symbol `sympify`), which is orthogonal to
convention. What is now true and was not then: the family is stale against its
own upstream, so regenerating it under D will move the coefficients and may
move Φ_8. The `2⌊(A−1)/2⌋` agreement should be re-checked after that
regeneration, not assumed to carry over.

### Sequencing, unchanged

`qou-eea0` is still `in-progress` and its own bean names the gap — *"The
missed set is the nuclear layer: deuteron at H₆, helium-3 at H₉…"*. The
deuteron row is therefore already on its list. This stays sequenced behind
that campaign; nothing here is for this bean to run.

## D-only directive executed (owner, 2026-08-18) — and the Φ_k structure does NOT survive

Owner: *"no C family. D only."* Done, in two steps.

**1. The mixed atomic witness is fixed.** Re-ran with `HABIRO_WITH_DEUTERON=1`.
All three rows now convention D, zero `check_q`, all `reconstruction_matches`
true. Deuteron `deg_p_u` 86 → 100, coefficients 13 → 14. That removes the
straddle `path_b_habiro_mass_probe` was reading (it calibrates α_M off the D
row).

**2. The 26-witness family regenerated under D.** 316 s, 0 failures, 20/20
reconstructions true with `tr_M_at_q0_rel_err = 0.0` throughout — so the
serialization fix and the refuse-guard both hold under D.

### The result nobody should skim past

Every Φ_k multiplicity is **0 on all seven mirror pairs** under D, with
`diff_zero: false` — the differences are nonzero, they simply carry no
cyclotomic structure:

    A    pair                          Φ_1  Φ_2  Φ_4  Φ_8      (C had:)
    1    proton − neutron                0    0    0    0       1 1 0 0
    3    helium-3 − tritium              0    0    0    0       1 0 0 2
    5    lithium-5 − helium-5            0    0    0    0       1 0 0 4
    7    beryllium-7 − lithium-7         0    0    0    0       1 0 0 6
    8    boron-8 − lithium-8             0    0    0    0       1 1 0 6
    9    boron-9 − beryllium-9           0    0    0    0       1 0 0 8
   10    carbon-10 − beryllium-10        0    0    0    0       1 1 0 8

**Φ_1 is the alarming one.** Its universality under C had a *structural*
justification — at q=1 the two mirror halves coincide, so `(u−1)` must divide
their difference. Under D it does not: the p−n difference factors as

    u^4·(u^2−u+1)·(u^2+u+1)·(u^4−u^2+1)·(u^32+3u^20−2u^16+3u^12−4u^8+3u^4−2)

which evaluates to **6 at u = 1**. The classical-limit coincidence fails.
Note the factors present are Φ_6, Φ_3, Φ_12 — Φ_8 does not appear at all.

### What this is, and what it is NOT

**It is NOT a refutation of `Φ_8 = 2⌊(A−1)/2⌋`.** Scope-(a): this construction,
as written, yields no cyclotomic structure under D. Whether the law was a
convention-C artifact, or the u-parametrisation is simply the wrong reading
under D, is **open** — and I do not have an established explanation.

One partial mechanism, recorded with its own limit: under D `tr_M_in_q` has
integer q powers where C had half-integer, so `u = √q` is at least partly
vestigial — the proton's `p_in_u` is all-even under D (exponents 4,8,16,…)
versus mixed parity under C (4,5,7,9,…), and an even `P(u) = R(u²)` divides by
`(u−1)` only if it vanishes at u=1. **But this does not generalise**: only
**4 of 25** family witnesses are all-even. I checked, and it does not explain
the other 21. Do not cite parity as the explanation.

### Do not publish the zeros as a result

The summary witness now carries `phi_8_mult: 0` for all seven pairs — the same
uniform-zero shape that this arc spent PR #4926 correcting. It is the correct
output of the current producer under D, and it is also exactly the kind of
number that reads as a finding when it is an artifact of an inapplicable
construction. Either the mirror-pair Φ_k analysis needs redoing in the right
variable for D, or it needs a guard that says "not applicable" rather than 0.
Flagged, not silently shipped.
