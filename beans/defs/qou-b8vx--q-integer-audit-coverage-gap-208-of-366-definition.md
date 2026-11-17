---
# qou-b8vx
title: 'q-integer audit coverage gap: 208 of 366 definitions are not symbolically evaluable (q0-pinned or needing module globals) — the convention of those 208 is UNMEASURED'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-07T14:02:19Z
updated_at: 2026-10-10T07:55:53Z
parent: qou-4cu3
---

MEASURED 2026-09-13. New audit: computations/audits/q_integer_global_resolution_audit.py. It resolves module globals instead of giving up on them -- walks each module's own top-level assignments, evaluates them symbolically against one root symbol, binds the result, and only then applies the function.

RESULT: 63 of 173 previously-unmeasurable definitions are now measured (36.4%, previously 0).

  53  symmetric
   5  classical
   3  symmetric[n=2]   (fixed-n, argument is the MODULUS)
   2  OTHER            (not q-integers at all -- name-pattern false positives:
                        L2_bracket is a dilogarithm bracket, _qbeta_dln_dlnq a
                        log-derivative)
 110  UNRESOLVED

So 61 of the 63 are genuine q-integers and ALL of them are accounted: 56 symmetric, 5 classical. Zero new conventions.

THE 5 CLASSICAL, and 4 of them are fine:
   c1_kernel_door_v_residual_probe.py::qint_geo
   c1_kernel_level_reading_probe.py::qint_geo
   derivative_only_dq_vs_c1_kernel_probe.py::qint_geo
   ramified_shift_calculus_prune_probe.py::qint_geo
   qbessel_mu_lambda_vs_qlommel_zeros.py::q_int          <-- the one to check
The four  SELF-DECLARE: the classical bracket IS the geometric sum
1+q+...+q^(n-1), so the name states the convention. Deliberate. The fifth sits
under the ambiguous name  and needs a per-file basis determination --
that is qou-gl58 territory, handed over rather than guessed at here.

A DEFECT IN MY OWN FIRST VERSION, caught and fixed before reporting. It assumed
a one-argument definition's argument is the INDEX. It is not always:  is [2]_q -- complete, symbolically comparable, no
module global involved. Calling it as f(2),f(3),f(5) computes 2+1/2, 3+1/3 and
classifies noise; five definitions were reported OTHER on that basis. The
duplication audit's symbolic_signature ALREADY guards this by trying both
argument orders (its own docstring records the  incident); I wrote
the successor without the guard. Third instance of the same class this session.
Fixed by classify_fixed_n, which tries f(q) FIRST and reads the fixed n off.

WHY 110 REMAIN, measured not guessed:
   47  no top-level assignment (the global is a parameter, an import, or set
       in a function)
   19  q-independent (the global resolves to a constant, so the definition is
       genuinely q0-pinned in the strong sense)
   13  depends on unresolvable Q_MP
    5  Q0   4  q0   2  _Q0_RESOLVED   2  _TBL   2  HERE  
The Q_MP cluster (13) is the largest single lever and is the obvious next step.

SCOPE, stated so the number is not misread: this audit counts TOP-LEVEL
FunctionDefs only (173). A walk that also descends into nested functions finds
259. Neither is wrong; they answer different questions, and the 173 is the
population the duplication audit actually skips.

An UNRESOLVED definition is UNMEASURED, not agreeing -- the conflation this
bean exists to prevent. Bean stays IN-PROGRESS: 110 of 173 are still dark.

SHELL-MANGLING NOTE 2026-09-13: the append above, and the commit message of
the same change, were written with backtick-quoted identifiers inside a
double-quoted shell string, so the shell ran them as command substitution and
ATE them. Lost from the commit message: h, qint_geo, q_int, q_int2, Q_MP, Q0,
q0, _Q0_RESOLVED, _TBL, HERE, and the example 'def q_int2(q): return q + 1/q'.
The measurements are unaffected -- only the prose lost identifiers. Repaired
here via a quoted heredoc, which cannot substitute. The commit message itself
is left as it landed rather than force-pushing over a branch that already has
an open PR; this bean is the durable record.

FULL TEXT OF WHAT WAS EATEN:
  - the unresolvable-global histogram: 13 Q_MP, 5 Q0, 4 q0, 2 _Q0_RESOLVED,
    2 _TBL, 2 HERE
  - the argument-order example: a one-arg definition whose argument is the
    MODULUS, e.g. one returning q + 1/q, is [2]_q -- complete and comparable,
    no module global involved. Calling it as f(2),f(3),f(5) computes 2+1/2,
    3+1/3 and classifies noise.
  - the four self-declaring classical definitions are named qint_geo; the
    fifth, needing a basis determination, is named q_int.

EXTENDED 2026-09-13, same session: 63 -> 81 of 173 resolved (36.4% -> 46.8%).

Three blockers removed, each a real gap in the resolver rather than a corpus fact:

1. IMPORTS. resolve() read only a module's OWN assignments, so any name bound
   by "from M import X" was invisible. Now follows the import to M and resolves
   there, with a cycle guard and depth limit. Also walks function bodies,
   because this corpus routinely defers an import into a def to dodge a
   circular import, and such a binding is as real as a module-level one.

2. INDENTATION IS NOT SCOPE. q_parameter binds its entire anchor block inside a
   module-level try:, so a scan of unindented statements missed Q_MP -- the
   single most-imported modulus name in the corpus -- and every definition
   downstream of it read as unmeasurable. Now walks module-level try/if/with
   bodies and except handlers.

3. THE ANCHOR ROOT. q_parameter builds the block as Q_MP = mpf(_d["q"]) from
   the anchor witness, which no ROOT_SOURCES entry matched. Now recognised --
   but ONLY inside modules AGENTS.md designates as the canonical q0 accessors
   (q_parameter, qou_substrate.constants). Scoping it that way is the
   difference between citing the corpus's own designation and inferring
   meaning from a spelling, which this audit otherwise refuses to do.

TALLY NOW:
    70  symmetric
     5  classical
     3  symmetric[n=2]        (fixed-n; argument is the modulus)
     1  symmetric_in_sqrt_q
     2  OTHER                 (not q-integers: a dilogarithm bracket and a
                               log-derivative -- name-pattern false positives)
    92  UNRESOLVED

THE ONE sqrt-VARIABLE HIT IS CORRECT, AND THE FILE IS EXEMPLARY.
deuteron_trefoil_qinvariant_closed_form_probe.py defines BOTH, adjacently:
    qint(n)    in A = sqrt(q)
    qint_q(n)  in q, under the comment "balanced quantum integer in q (not
               sqrt q): [n]_{q} = (q^n - q^-n)/(q-q^-1)"
The author was aware of exactly the distinction that made the q-Hankel probe a
defect (qou-9nn0) and handled it explicitly. This is the corpus getting it
right; recorded so a future sweep does not "fix" it.

WHAT THE REMAINING 92 ARE, and the first bucket is an ANSWER not a gap:
    29  q-independent -- the global resolves to a CONSTANT, so the definition
        is genuinely q0-pinned in the strong sense. Its convention is not
        symbolically askable; it is a number. That is the answer for those 29,
        not a failure to measure them.
    25  no top-level assignment (bound in a function, or a parameter)
    14  Q_MP chain still failing -- the anchor-module root fires, so these
        reach Q_MP by some route other than a module-level import; UNDIAGNOSED
     3  import cycle or depth limit
     2  _TBL   2  HERE   2  Q   1  json   (data-file loads; correctly opaque)

So the honest split of 173 is: 81 classified, 29 established as genuinely
q0-pinned, 63 still dark. Bean stays IN-PROGRESS.

CORRECTION + THIRD PASS 2026-09-13: 81 -> 102 of 173 (46.8% -> 59.0%).

*** I MUST RETRACT THE "29 GENUINELY q0-PINNED" FIGURE FROM THE APPEND ABOVE. ***
I reported 29 definitions as "q-independent -- the global resolves to a
CONSTANT, so the definition is genuinely q0-pinned... That is the answer for
those 29, not a failure to measure them." It was a failure to measure them.
23 of the 29 were MY OWN BUG manufacturing a reassuring answer. The real
figure is 6.

THE BUG. The corpus writes, idiomatically:
      from q_parameter import Q_MP as Q0
      q = mp.mpf(str(Q0))
My shim's mpf did sympify(str(x)). A str() round-trip through sympify rebuilds
Symbol('q') WITHOUT the positive=True assumption -- a DIFFERENT symbol object
from the canonical Q this audit tests against. So `free_symbols & {Q}` came
back empty and the resolver concluded "q-independent (a constant, not the
modulus)" about a value that IS the modulus, reached by the corpus's own
canonical accessor.

Comparing symbols by IDENTITY when the corpus round-trips them through STRINGS
is the same wrong-object comparison that has now bitten this work four times
(audit sec 21.3 item 2; the sqrt-variable misclassification in qou-9nn0; the
index-vs-modulus argument bug earlier today). What makes this instance the
worst is its DIRECTION: the other three produced visible nonsense -- 4**q/2**q,
2+1/2 -- that invited inspection. This one produced a calm, plausible,
WRONG negative and I wrote it up as a finding.

Fixed by _canonical_q(), which collapses every symbol named q onto the
canonical Q before the dependence test.

TALLY NOW:
    91  symmetric
     5  classical
     3  symmetric[n=2]
     1  symmetric_in_sqrt_q       (correct and deliberate -- see above)
     2  OTHER                     (not q-integers at all)
    71  UNRESOLVED

HONEST SPLIT OF 173:  102 classified by convention
                        6 genuinely q-independent (was claimed 29)
                       65 still dark

Still zero new conventions across all 102. The remaining 71:
    26  no top-level assignment
    14  Q_MP chain -- DIAGNOSED but NOT fixed. The blocker is ALIASED imports:
        `from q_parameter import Q_MP as Q0` keys my import map under Q0, so a
        module that also mentions Q_MP by its original name does not resolve
        it. Tractable; not attempted here.
     6  q-independent (genuine)
     3  import cycle or depth limit
     2  _TBL   2  HERE   2  Q   1  json   (data-file loads, correctly opaque)

FOURTH PASS 2026-09-13: 102 -> 117 of 173 (59.0% -> 67.6%). Q_MP cluster gone.

*** MY "DIAGNOSED: ALIASED IMPORTS" CLAIM IN THE APPEND ABOVE WAS WRONG. ***
I wrote that the 14-strong Q_MP cluster was blocked because "from q_parameter
import Q_MP as Q0 keys my import map under Q0". Measured: the imports were
captured CORRECTLY the whole time -- instrumenting the failing path shows
'Q_MP' in module imports? True -> q_parameter::Q_MP on every one of them.

THE ACTUAL CAUSE: my cycle guard tripped on itself across a module hop. The
corpus writes
      from q_parameter import Q_MP
      Q = Q_MP
Resolving Q walks to Q_MP with seen = {Q, Q_MP}, hops into q_parameter, and
the FIRST line of resolve() sees Q_MP already in seen and reports a cycle --
against a chain two steps long and perfectly acyclic. The guard was keyed by
BARE NAME, so a name that legitimately appears in two modules looked like a
loop.

Fixed by keying the guard MODULE::NAME across a hop.

That is TWO wrong diagnoses I asserted in this area today (the other: reporting
23 of my own str()-roundtrip failures as "genuinely q0-pinned"). Both were
stated confidently in a commit message before being instrumented. The cheap
guard that caught both, and that I should have reached for first BOTH times:
run the resolver on the actual failing path and print what it returns, instead
of reasoning about why it ought to work.

TALLY NOW:
   105  symmetric
     6  classical
     3  symmetric[n=2]
     1  symmetric_in_sqrt_q     (correct + deliberate; see above)
     2  OTHER                   (not q-integers at all)
    56  UNRESOLVED

HONEST SPLIT OF 173:  117 classified / 6 genuinely q-independent / 50 dark
Still ZERO new conventions across all 117 -- that result has now survived four
passes and a tripling of the measured population.

REMAINING 56:
    27  no top-level assignment (bound inside a function, or a parameter) --
        now the dominant blocker and the obvious next lever
     6  q-independent (genuine)
     2  Q_INV_MP   2  _TBL   2  HERE   2  Q   1  json

FIFTH PASS 2026-09-13: 117 -> 128 of 173 (67.6% -> 74.0%). Bean's question is now
substantially answered.

*** A THIRD FIGURE OF MINE RETRACTED: the "27 blocked on function-scope
binding" in the append above was mostly MY OWN DETECTOR NOISE. *** Measured by
listing what those 27 actually block on, the free names were i, k, j, r, eta,
f, hv, fmt, at_q0, _sub, trace_poly_closed, c3_target_at -- ordinary loop and
comprehension variables, and the names of helper FUNCTIONS. My free-name
detector collected only ast.Assign targets as local, so every comprehension
target, for-target, walrus, nested def name, lambda arg and except-alias in the
function read as an unresolved module global. "no top-level assignment" is now
27 -> 7.

That is the THIRD time in this bean that a number I published described my
tooling rather than the corpus (the others: 29 "genuinely q0-pinned" -> 6; the
Q_MP cluster "diagnosed as aliased imports" -> a self-tripping cycle guard).
Every one was found the same way: LIST THE MEMBERS, do not reason about the
bucket. I have now relearned this five times in one session.

THE ONE REAL GAP among those 27, and it was worth the pass: TUPLE UNPACKING.
      q, h = sp.symbols('q h', positive=True)
      Q, H, TOL, WALL = (Q_MP, HA_MP, mp.mpf('1e-9'), 3)
Both bind q at module scope; top_level_assignments took only ast.Name targets
and skipped both. Now records each element as a SUBSCRIPT of the right-hand
side, so resolve() evaluates RHS[i] with machinery it already had.

TALLY NOW:
   112  symmetric
    10  classical
     3  symmetric[n=2]
     1  symmetric_in_sqrt_q   (correct + deliberate)
     2  OTHER                 (not q-integers at all)
    45  UNRESOLVED

HONEST SPLIT OF 173:  128 classified / 6 genuinely q-independent / 39 dark
STILL ZERO NEW CONVENTIONS across all 128 -- survived five passes while the
measured population went 0 -> 128.

THE 10 CLASSICAL, which is the actionable output for qou-gl58:
   binding_weight_markov_pinning_probe.py::qint
   gs_tower_jet_degree_body_order_probe.py::q_int
   hecke/tw_gram_square_class_crosscheck.py::q_int
   lever1_kernel_maj_involution_identification.py::qint_u
   probes/c1_kernel_door_v_residual_probe.py::qint_geo        ) self-declaring:
   probes/c1_kernel_level_reading_probe.py::qint_geo          ) "geo" IS the
   probes/derivative_only_dq_vs_c1_kernel_probe.py::qint_geo  ) geometric sum
   probes/ramified_shift_calculus_prune_probe.py::qint_geo    )
   qbeta/qbessel_mu_lambda_vs_qlommel_zeros.py::q_int
   substrate/lever1_qinvolution_kernel_test.py::qint_asym     <- "asym" declares it too
So 5 of 10 SELF-DECLARE their convention in the function name (4x _geo, 1x
_asym). The remaining 5 sit under the ambiguous names q_int / qint and need a
per-file basis determination -- handed to qou-gl58, not guessed at here. Note
tw_gram_square_class_crosscheck is a T_w/Iwahori-basis file, where audit sec 22
established the classical bracket is CORRECT; that one is very likely fine.

REMAINING 45: 7 no top-level assignment, 6 genuinely q-independent, 2
Q_INV_MP, 2 not-evaluable TypeError, 2 q0, and a tail of data-file loads that
are correctly opaque. Heterogeneous -- better left measured and characterised
than chased with a sixth heuristic.


---

## 2026-09-13 (pass 6) — 133/175, and the "heterogeneous" judgement was wrong

I stopped this bean at 128/173 saying the rest were *"heterogeneous and better
left measured than chased with a sixth heuristic."* **That judgement was the
thing to distrust**, and my own closing line said so: *"LIST THE MEMBERS, do
not reason about the bucket."* I listed them, and 5 of the 47 were a sixth
detector gap.

**POPULATION MOVED: 175, not 173** — main landed two new producers. Re-measure;
do not quote 173.

| | pass 5 | pass 6 |
|---|---|---|
| symmetric | 112 | **117** |
| classical | 10 | 10 |
| `symmetric[n=2]` | 3 | 3 |
| `symmetric_in_sqrt_q` | 1 | 1 |
| OTHER (not q-integers) | 2 | 2 |
| **UNRESOLVED** | 47 | **42** |
| **RESOLVED** | 128/173 | **133/175 (76.0 %)** |

**STILL ZERO NEW CONVENTIONS** — six passes, population 0 → 133. All five
newly-measured are symmetric.

### The sixth gap: a module's own import ALIAS

`q_parameter` writes `import mpmath as _mp`. The evaluator bound only `mp` and
`mpmath`, so every constant in that module needing evaluation died on the name
`_mp`:

    Q_INV_MP     = _mp.mpf(1) / Q_MP        -> 1/q
    HA_MP        = Q_MP - Q_INV_MP          -> q - 1/q

That is 3 + 2 = 5 definitions, reported as `depends on unresolvable
Q_INV_MP` / `HA_MP` and reading exactly like corpus opacity.

**Why it hid so well, and this is the reusable part.** `Q_MP` itself resolves
FINE — it short-circuits on `_ANCHOR_KEYS` at the top of `resolve()`, *before*
any evaluation happens. So the one name a reader would test to check whether
the anchor module is reachable is **the one name that does not need the
alias**. A spot-check on `Q_MP` returns a confident green while every sibling
constant in the same block is dark.

The fix reads the module's OWN `import` statement (plain `import X as Y` is
now recorded as `Y -> X::*`) and binds that alias. It is corpus-derived, not
spelling inference: the module says what `_mp` means.

Note `HA_MP = q - 1/q` is the **symmetric-bracket denominator**, so these
definitions were always likely symmetric — which is exactly why measuring
rather than assuming was the point.

### What actually remains (42), listed not characterised

    8  no top-level assignment
    6  q-independent (a constant, not the modulus)   <- ANSWERED, not dark
    4  not evaluable (TypeError)                     <- was 2; +2 new producers
    2  depends on `q0`
    2  depends on `_TBL`      <- a json.loads of a data file; correctly opaque
    2  depends on `HERE`      <- a path constant; q-independent by construction
    2  depends on `Q`
    2  call failed (SympifyError)
    …tail

So the honest split is **133 classified / 6 genuinely q-independent / 36
dark** — and `_TBL` and `HERE` are two more that are *correctly* unresolvable
rather than gaps, which would make it 32.

**I am not claiming the remaining 36 are all real opacity.** That is the claim
that was wrong last time. They are unmeasured, and on this session's record
the prior should be that some fraction are still my tooling.


---

## 2026-09-13 (pass 7) — 134/175, and the audit was dark on the CANONICAL q-integer

**133 -> 134 (76.6 %)**, UNRESOLVED 42 -> 41. Small numerically; the identity
of the recovered definition is the finding.

### It was `qou_substrate.constants.q_int`

The corpus's **canonical q-integer entry point** — the one AGENTS.md's package
layer publishes, and the one I excised a float64 fallback from earlier in this
same session. The audit could not measure the definition the whole bean is
about. It now classifies **symmetric**.

### Two gaps, and I got the first one wrong

**My first hypothesis was the anchor SOLVER**, and it was not sufficient.
`constants.py` binds `Q = _solve_q_proton_f64(MASS_RATIO_P_E, VOL_FIGURE_EIGHT)`
— a numerical root-find no symbolic evaluator can execute. Adding
`ANCHOR_SOLVERS` was **correct and necessary** (AGENTS.md names that function
verbatim as what makes `constants.py` proton-pinned, so recognising it cites
the corpus rather than inferring from a spelling) — but the run came back
**unchanged at 133**, which is how I learned it was not the whole story.

**The real blocker was scope.** `in_anchor_module` was set ONLY when
`resolve()` **hopped into** a module via an import, and defaulted `False` at
the top-level call site. So for a definition that already **lives in**
`constants.py` or `q_parameter.py`, none of the anchor-module special cases
could ever fire. *"The module I'm in"* and *"the module I hopped to"* were
being treated as different questions when they are the same one. One argument
at one call site.

Both fixes are in; the solver recognition is load-bearing once the scope fix
lets it run.

### `q_int_err` correctly stays unresolved

Its body is `|d[n]_q/dq| * Q_ERR` — an **uncertainty propagation**, not a
bracket. It depends on `Q_ERR`, and it should not classify as a q-integer.
Recording this so a later pass does not chase it as a gap.

### Tally

| | pass 6 | pass 7 |
|---|---|---|
| symmetric | 117 | **118** |
| UNRESOLVED | 42 | **41** |
| **RESOLVED** | 133/175 | **134/175 (76.6 %)** |

**Still zero new conventions** — seven passes, population 0 -> 134.

### The audit now LISTS its unresolved members

Added, because this bean's own closing line is *"LIST THE MEMBERS, do not
reason about the bucket"* and the script printed only counts — so using it
correctly required leaving it. Grouped by reason. That listing is how pass 7's
gap was found at all.

### What the listing shows about the remaining 41

Several of the `[8] no top-level assignment` group are **not q-integer
definitions**: `verify_bracket_cancellation`, `check_bracketing` (test
helpers), `load_qbeta_precision_ladder` (a loader). So the name-pattern
candidate selection has false positives here, and 41 overstates the genuinely
dark set. Not chased further this pass — recorded rather than estimated.

Correctly opaque and not gaps: `_TBL` (2, a `json.loads` of a data file),
`HERE` (2, a path constant), and the 6 already answered as q-independent.


---

## 2026-09-13 (pass 8) — the DENOMINATOR was wrong: 175 -> 164, coverage 76.6 % -> 81.1 %

Pass 7 recorded, without measuring, that *"several of the `[8] no top-level
assignment` group are not q-integer definitions ... 41 overstates the
genuinely dark set."* This measures it.

### The selector is a SUBSTRING match

`NAMEPAT = ('q_int', 'qint', 'qb', 'q_bracket', 'qbracket', 'q_num',
'bracket')` tested with `any(k in node.name.lower() ...)`. Two
false-positive families, both measured on the full tree:

* **`qb` inside `qbeta` (8).** In this corpus `qbeta` is the **beta-decay
  Q-value** — a different quantity from `[n]_q` entirely (AGENTS.md's CAL-2
  row). `_sigma_qbeta`, `dc3_dQbeta`, `_qbeta_dln_dlnq`,
  `load_qbeta_precision_ladder` have no bracket in them at all.
* **A verb-named helper (4).** `verify_bracket_cancellation` returns `bool`;
  `check_bracketing` returns a dict report — test helpers, not definitions.
  `L2_bracket` is a dilogarithm bracket `ln z/(1-z)^2 - ln(1-z)/z^2`;
  `mirror_bracket` is `5*2^(-A-1) - 13*4^(-A)`.

**The thirteenth is GENUINE and was NOT excluded**: `_bracket` in
`em_linking_invariant_probe.py`, whose docstring and body are exactly
`(q^n - q^-n)/(q - q^-1)`. So the inner-substring match is narrowed by the
two measured families, not thrown away — a blanket "no inner matches" rule
would have lost a real definition.

### THE CHECK THAT MATTERS: the tally was never contaminated

Every one of the 12 false positives landed in **OTHER (2)** or
**UNRESOLVED (10)**. **Not one was counted as a convention.** Confirmed
from the other side by the re-run: `symmetric` stayed **118** and `classical`
stayed **10** across the narrowing. So the "zero new conventions" result —
which is what this bean actually exists to establish — was never at risk.
They only inflated the denominator and the dark set.

### Corrected figures

| | pass 7 | pass 8 |
|---|---|---|
| denominator | 175 | **164** |
| UNRESOLVED | 41 | **31** |
| **RESOLVED** | 134/175 (76.6 %) | **133/164 (81.1 %)** |
| symmetric | 118 | 118 |
| classical | 10 | 10 |

Resolved moves 134 -> 133 because one of the two removed OTHERs was counted
as resolved. The percentage rises because the denominator falls further.

### Secondary defect: the two audits disagreed about test files

Reconciling an off-by-one (my check said 10 dropped, the audit's denominator
moved 11) found it: **this audit skipped only `_deprecated`, while the
sibling `q_integer_duplication_audit` skips `_deprecated`, `/tests/`,
`.lake`, `node_modules`.** So it was walking test files and counting
`test_smoke.py::test_q_int_quantum_integers` as a definition. A test
ASSERTS a bracket; it does not DEFINE one, and two sibling audits
disagreeing about that is a difference with no reason behind it. Skip lists
now aligned.

That alignment changes **no number today** — the `test_` prefix rule already
caught that one function — but it removes a divergence that would bite the
next time either audit is extended.

### Still zero new conventions

Eight passes, measured population 0 -> 133. That invariant has now survived
a change of denominator as well as a sevenfold expansion.

### What remains: 31

Not re-characterised here. Pass 7's listing stands, minus the 10 removed.
Two known false positives deliberately survive the narrowing (`L2_bracket`,
`mirror_bracket`) because excluding them would need a rule I have not
measured, and an unmeasured rule is how the denominator got wrong in the
first place.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-13 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## 2026-10-10 re-audit verdict: **REPARENT** (bean `qou-am5t`)

Not the Markov-parameter convention. q-integer definitions are a DIFFERENT
convention axis (Gaussian bracket vs classical `(q^n-1)/(q-1)`); conflating
the two is how the convention question came to look 57 beans deep. Keep open,
re-home with `qou-qint`/`qou-gl58`.

Full 41-bean triage table and the method behind it: [`docs/coordination/convention-d-migration-status.md`](../../docs/coordination/convention-d-migration-status.md) §9.
