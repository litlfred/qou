
---

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
