---
# qou-b8vx
title: 'q-integer audit coverage gap: 208 of 366 definitions are not symbolically evaluable (q0-pinned or needing module globals) — the convention of those 208 is UNMEASURED'
status: in-progress
type: task
priority: normal
created_at: 2026-09-07T14:02:19Z
updated_at: 2026-09-13T06:16:22Z
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
