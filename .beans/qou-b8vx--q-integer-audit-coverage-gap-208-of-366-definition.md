---
# qou-b8vx
title: 'q-integer audit coverage gap: 208 of 366 definitions are not symbolically evaluable (q0-pinned or needing module globals) — the convention of those 208 is UNMEASURED'
status: in-progress
type: task
priority: normal
created_at: 2026-09-07T14:02:19Z
updated_at: 2026-09-13T06:38:25Z
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
