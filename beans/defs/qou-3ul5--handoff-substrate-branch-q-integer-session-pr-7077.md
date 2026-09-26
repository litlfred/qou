---
# qou-3ul5
title: 'HANDOFF: substrate-branch / q-integer session — PR #7077 merged, 6 items open, 3 gated on the owner'
status: in-progress
type: milestone
priority: normal
created_at: 2026-09-07T18:29:42Z
updated_at: 2026-09-13T05:55:51Z
---

WRITTEN 2026-09-07 ~18:40Z at the end of the session that merged PR #7077 (rebase-merge, main 8360a30ff). Written for an agent who was NOT in that session. Every identifier is expanded on first use.

=== WHAT LANDED (do not redo any of it) ===

PR #7077, 25 files, +2435/-55, merged. Two tranches.

TRANCHE 1 — substrate geometry. docs/audits/2026-09-07-substrate-branch-and-the-q-eq-1-interface.md, sections 0-24. The colour elliptic fibre's modulus is z = s - 1/s (s = sqrt(q)); its second Weierstrass coefficient is r(z) = (5/27)(z+1)(4z^2-z+4), which equals the q_W(z) already in t-duality-elliptic.md (symbolic difference 0). Consequences: bar (q -> 1/q) sends z -> -z and r is NOT even, so matter and antimatter colour fibres are DIFFERENT elliptic curves (7.878% apart at q0); they coincide iff q = 1. Three scope-(b) exclusions established: interfaces cannot be dark matter (codimension forces rho ~ a^-1 vs a^-3); the 7.878% cannot reach a baryon asymmetry (every counting object is exactly bar-even, so there is no channel, not merely a suppressed one); a bar-conjugate domain is excluded observationally (Delta-alpha/alpha = 23.16% vs quasar bounds 1e-6).

TRANCHE 2 — the q-integer convention split. computations/audits/q_integer_duplication_audit.py compares every local [n]_q definition SYMBOLICALLY in a sympy symbol q, never at q0. 366 definitions in 363 files, FOUR forms: 126 symmetric (q^n-q^-n)/(q-q^-1), 30 classical/Gaussian (q^n-1)/(q-1), 1 sqrt-normalised, 1 symmetric-in-q^2. Root cause: canonical qou_substrate.constants.q_int(n) takes n ONLY (Q/Q_INV/HA are module globals), so it is q0-pinned and no q-parametric caller could import it.

LEAN, both sorry-free, both import Mathlib ONLY (zero 'import QOU'):
  QOU/BringsSurface/ColourCurveModulus.lean   9 theorems
  QOU/Substrate/QIntegerConventions.lean      8 theorems; the load-bearing one is
    conventions_never_agree — qSymm 2 q - qClas 2 q = (1-q)/q, nonzero for every
    q not in {0, +-1}, so the two conventions NEVER coincide at any admissible q.

CODE: constants.py gained q_int_at(n,q) / q_int_classical_at(n,q), purely additive (62 -> 64 public names, none removed). computations/term7_chi5_basis.py FIXED — it used the classical bracket while its own docstring computes a Wedderburn weight; the correction is not a rescale, Sigma_lambda w_lambda moves by a ratio running 1.951 -> 0.497 across A = 2..6 and crosses 1 between A=3 and A=4.

=== OPEN ITEMS, PRIORITY ORDER ===

GATED ON THE OWNER — do NOT start these without an explicit go:

  qou-itdn  Selective interface / charge separation. V_L(1) = (-2)^(c-1), so at
            q = 1 knots trivialise but LINKS do not (Hopf -> -2, Borromean -> 4).
            Does a q=1 surface therefore separate charge? Needs a transport
            calculation and that is NOT cheap. The owner has been asked twice and
            has not answered; do not infer a go from silence.
  qou-gl58  The 29 remaining classical-convention files. This is a PER-FILE BASIS
            determination, NOT a sweep: the discriminator is which basis the file
            works in (T_w/Iwahori takes classical; normalised / quantum-dimension
            takes symmetric). term7_chi5_basis was catchable only because its
            docstring NAMED the quantity and the notation register PUBLISHES a
            figure to test against (Sigma w_lambda = 0.987/0.982/0.982/0.991).
            Neither handle exists for most of the rest. At least two of the three
            checked so far are CORRECT AS WRITTEN, so this is not a drain.
  The four content proposals in section 7 of the audit doc. Nothing under content/
            has been touched, deliberately.

UNGATED — measurement, allowed under the new ask-the-owner rule because measuring
is not changing:

  qou-b8vx  208 of the 366 q-integer definitions are symbolically UNMEASURED —
            they are q0-pinned (take n only) or need module globals, so the AST
            audit cannot evaluate them. Extending it to resolve module globals is
            the work.
  qou-9nn0  The two outlier brackets: one sqrt-q-normalised, one symmetric-in-q^2.
            Identify what each is for.
  qou-hv27  NEW THIS SESSION, infra, probably the highest-value ungated item: the
            paper package's Lake dependency trees are half the root's, which makes
            the repo's own merge gate emit hundreds of FALSE corpus REDs. Full
            measurement + a per-session repair are in that bean. The real fix is
            at the cache seed/restore, which is untouched.
  qou-6mij  main's computations/witness-raw-float64-audit.witness.json is stale by
            eight drain commits (says 1009 dirty / 31226 fields; a fresh run gives
            996 / 28152). Belongs to qou-r47m / qou-kfeg / qou-sv7h, not to me.
  qou-fi93, qou-ndt5 — stay open per AGENTS.md 13a, both subjects are open
            conjectures. Do NOT close them; their ANALYSIS is done and recorded.

=== TRAPS THIS SESSION PAID FOR ===

1. echo "exit=$?" AFTER A PIPE reports the last pipeline element. It reported
   exit 0 for two Lean files that were in fact failing on 'unknown module prefix
   Mathlib'. Capture rc directly.
2. LEAN_PATH needs the lib/lean suffix. Root dirs are
   .lake/packages/<pkg>/.lake/build/lib/lean, NOT .../lib.
3. A bare 'lean' invocation is a WEAKER check than lake -- it does not read the
   lakefile, so autoImplicit defaults TRUE and unbound identifiers are silently
   auto-bound instead of erroring. Pass -DautoImplicit=false -s 65536.
4. The precision gates and the raw-float64 ratchet REWRITE witness files as a side
   effect. Restore them (git checkout -- computations/) or you commit someone
   else's bookkeeping as your own work.
5. precision-gates.sh exits 1 with TEN REDs on main itself — measured identical
   with a change stashed. Do not report 'gates pass'; there is no green baseline.
6. Sibling PRs are worth reading BEFORE writing up a finding. #7099 reached this
   session's disk-vs-corpus conclusion an hour earlier by a different route.

=== SESSION LINK ===
https://claude.ai/code/session_01QdzbDVufzGssqqYjkw7Ykm
PR #7077: https://github.com/litlfred/qou/pull/7077 (merged 8360a30ff)

CORRECTION 2026-09-13 (qou-9nn0 resolved): this handoff says 'FOUR forms: 126 symmetric, 30 classical, 1 sqrt-normalised, 1 symmetric-in-q^2' and lists qou-9nn0 as 'the two outlier brackets'. Both halves are wrong. There are TWO conventions -- 128 symmetric / 30 classical / ZERO outliers. The two 'outliers' were the symmetric bracket written in a square-root variable, verified symbolically at n=2,3,5,7. One of them (keystone_qhankel_eq2_vacuum_row) was nonetheless a real defect for a different reason -- wrong ARGUMENT, not wrong convention -- and is fixed. Full account in qou-9nn0.
