---
# qou-yof3
title: 'qbeta_crossing_weight_hecke_probe: np.linalg.solve against the identically-singular Gram'
status: completed
type: bug
priority: high
created_at: 2026-08-16T13:39:23Z
updated_at: 2026-08-23T16:35:53Z
---

`computations/qbeta/qbeta_crossing_weight_hecke_probe.py:128` runs

    np.linalg.solve(gram.G, np.ones(6))

to obtain the cointegral `omega = G^-1 . 1`. Under convention D the H_3 Gram
form `G` is **identically singular over Q(q)** — its radical is exactly
ker(H_3 -> TL_3), of dimension `3! - Catalan(3) = 6 - 5 = 1`. This is not a
q_0 artefact: `det G == 0` generically in q
(docs/audits/2026-08-16-s2-gram-radical-independent-revalidation.md), and the
vanishing is proved sorry-free for all n by
`QOU.QBeta.WenzlWeight.conventionD_weight_eq_zero_iff`
(docs/audits/2026-08-16-tl-all-n-weight-vanishing.md).

The call is UNGUARDED. Every other site in the corpus that touches this form
handles the degeneracy: `pyhecke/gram.py:407` uses `np.linalg.pinv`,
`gram.rs:339` uses a rank-one-shift Moore-Penrose, `pyhecke.gram.gram_inverse`
deliberately raises, and `confinement-operator-selection.py:195` routes through
`_pg_safe_inverse` (an SVD rank guard). This one does not — so it either raises
LinAlgError or, worse, returns a numerically meaningless vector from a
near-singular float64 solve.

This is a WRONG ANSWER, not a slow one, which distinguishes it from the rest of
the TL_n compute move (where the discarded dimensions contribute exactly zero
and the change is pure speed).

Scope (a): the defect is in this call site. I have not checked whether any
result derived from this probe was carried into an audit doc or a downstream
probe; that is the follow-up. It is a probe, so this is not a production defect.

Fix options, cheapest first:
  1. Route through `pyhecke.gram.safe_inverse` (the existing SVD rank guard).
  2. Solve on the 5-dimensional TL_3 quotient, where the form is genuinely
     non-singular and no pseudo-inverse is needed. This is the correct fix and
     is the same move tracked under qou-8iru.

Estimated effort ~1 h for option 1. Independent of the wider TL_n move.

Found during the TL_n consumer survey, PR #5241.


## FIXED 2026-08-23 — and BOTH prescribed fixes are refuted, exactly

The call was worse than 'unguarded'. Measured on main: **numpy raises
nothing.** It returns

    omega = [-6.85e14, 6.17e14, 6.17e14, -5.56e14, -5.56e14, 5.01e14]
    residual ||G.omega - 1|| = 0.1398

i.e. it does not solve the system at all, then the assertion compares that to
a reference of order 1. So the leg failed loudly rather than passing
silently — but with a meaningless number, not a diagnosis.

### The obstruction, exactly over Q(q)

G's radical is spanned by the q-antisymmetriser `v_i = (-1/q)^len(w_i)`
(gram.py's own closed form). Pair it with the all-ones RHS:

    <v,1> = 1 - 2/q + 2/q^2 - 1/q^3 = (q-1)(q^2-q+1) / q^3

The numerator vanishes ONLY at q = 1: `q^2-q+1` has discriminant
`1-4 = -3 < 0` with positive leading coefficient, so it is **positive for
every real q**. Hence `<v,1> != 0` for every real q > 1 — the whole
substrate regime.

### Consequences — this kills both fix options in the original bean

- **Option 1 (route through `safe_inverse`/`pinv`) is WRONG.**
  `<v,1> != 0` means `1 is not in range(G)`, so `G.omega = 1` is
  **inconsistent**. A pseudo-inverse returns the least-squares vector for an
  unsolvable system (measured: residual 0.0427, `max|w-ref| = 0.223`). That
  converts a loudly wrong answer into a **quietly** wrong one — the worse
  failure mode by this repo's own standard.
- **Option 2 (solve on the TL_3 quotient) does not rescue THIS system
  either.** For the problem to descend to `H_3/rad` the RHS functional must
  annihilate the radical. It does not — by the same nonzero `<v,1>`. So this
  is **not** blocked on `qou-8iru`; that move is orthogonal to it.

**The cointegral `omega = G^-1 . 1` simply does not exist under convention
D.** The old assertion was not merely unguarded, it was **ill-posed**.

### What shipped instead

The leg now asserts the obstruction itself — exact, G-dependent (it moves if
the radical or the convention drifts), and the well-posed statement of what
the old assertion was groping at:

    W1_cointegral_obstruction_is_exactly_(q-1)(q^2-q+1)/q^3       PASS
    W1_cointegral_obstruction_nonzero_for_every_real_q_gt_1       PASS

**No float64 in the replacement**: nonvanishing is established from the
discriminant, not by evaluating at q_0 (AGENTS.md — probes are not exempt).
The C-frame net-ansatz `[0.601, ...]` is retained in the detail string as
provenance only.

Probe exits 0, 9/9. `precision-gates.sh --changed`: all blocking gates green.

### Scope note

Still scope-(a): I have not traced whether any result derived from the old
broken leg was carried into an audit doc or downstream probe. Since the leg
**failed** rather than passed, contamination is unlikely — but 'unlikely' is
not 'checked'.
