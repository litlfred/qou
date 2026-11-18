---
# qou-avt2
title: 'ATTACK 2: general-n per-block Hecke characters via Halverson-Ram / Jing-Liu'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-26T04:14:19Z
updated_at: 2026-11-18T08:22:48Z
parent: qou-59vq
---

Newly enabled by the owner's 2026-08-26 Murnaghan-Nakayama upload drop
(commit 548de479), now ingested and greppable under library/.

WHAT THE CORPUS HAS NOW. chi_block_3 / chi_block_21 / chi_block_111 in
qbeta_utils.py are hand-derived and exist ONLY at n = 3, and the one-crossing
"character collapse" 2*chi_lambda(sigma_1) - h*f^lambda = [2]_q*chi^lambda(tau)
was likewise derived by hand (2026-08-21 ladder-phase audit).

WHAT THE LITERATURE SUPPLIES. A Murnaghan-Nakayama rule for IWAHORI-HECKE
characters on standard elements:

  library/9511222v1/          Halverson & Ram, MN rules for H(G(r,p,n))
  library/arxiv-2504.18825v2/ Jing & Liu (v2, 2026-03) -- STRONGER, PREFER THIS:
                              Shoji determinacy gives the FULL irreducible
                              character table of H_{m,n}(q,u), and Jing-Liu note
                              that HR "computed characters only on certain
                              standard elements and did not prove" completeness.
                              Also a DUAL MN rule via vertex operators.

So the deliverable is a general-n closed form for the per-block Hecke characters
-- taking the ladder's per-block structure past n = 3 without re-deriving by
hand each time.

TRAP, DO NOT FALL IN. library/arxiv-2406.05311v1/ (quantum MN rule for the FLAG
MANIFOLD) has a "quantum" that is the quantum-cohomology NOVIKOV parameter, NOT
the Hecke q. Identifying them is the overloaded-symbol failure registry section
2 exists for. Cite it for the hook-Schur reduction via quantum Bruhat order
(Leung-Li, Postnikov); do not import its q.

NOTE what this does NOT do: it does not bridge to the Xi_k weight moments --
those collapse to a function of h (qou-ximf, retracted 2026-08-26).


## Delivered 2026-08-26 — three probes, and a correction

**Part 1** `qbeta_hecke_mn_character_engine_probe.py` (7/7) — the Jing-Liu
cyclotomic MN rule at m=1, exact sympy over Q(q), characters on standard
elements. Collapsed form: chi = sum q^{k-cc-2ht} (-1)^ht h^{cc-1} chi'.
Validated against the eigenvalues of sigma, the hook-length formula, an
independent Frobenius/Schur expansion at q->1, column orthogonality, and the
index/sign reps.

**Part 2** `qbeta_hecke_symbolic_seminormal_probe.py` (5/5) — exact symbolic
characters for ARBITRARY words. This is the symbolic half of the corpus's own
NAMED deferred item "F3" (`chi_lambda_braid` precision='symbolic_q' raises
NotImplementedError citing Murnaghan-Nakayama). Cross-checks against part 1
SYMBOLICALLY on standard elements -- two unrelated algorithms.

**Part 3** `qbeta_chi_block_symbolic_closure_probe.py` (9/9) — RESULT:
`chi_block_{3,21,111}` are the EXACT q-rational characters of beta_n - beta_p,
not q0 coincidences. qou-avt5 flagged exactly this as unmeasured ("the words
are q0-BAKED"); they are not -- `nucleon_gen_chains` takes a symbolic q and
only the module-level CONSTANTS are baked.

**CORRECTION to this bean's premise.** It said the corpus has no general-n
machinery. Too broad: `computations/hecke/hecke_characters.py` has had a
general-n NUMERICAL seminormal engine all along, and
`_deprecated/jing_liu_characters.py` has partial symbolic closed forms (hooks
and two-row lambda only). What was missing, and is now supplied, is EXACT
SYMBOLIC evaluation for general lambda.

## Next

Un-defer F3 properly: wire the symbolic path into
`hecke_characters.chi_lambda_braid(precision='symbolic_q')` instead of raising,
so consumers get it through the ordinary entry point. Separate bean.


## 2026-09-02 — cross-link from qou-0y6h / qou-kwoa (no action needed here)

Your symbolic chi_lambda is the supplier for a second consumer, recorded so the
dependency is visible from this side too.

qou-0y6h measured that the blocker for det(twGram) at rank >= 2 — the diagonal
structure constant [T_u T_w : T_w] of the T_w basis — is NOT determined by
length, cycle type, or the pair (refuted with an S_5 witness). It is a character
sum, and computations/hecke/tw_trace_equals_character_sum_probe.py verifies

    tr(L_{T_u}) = sum_lambda d_lambda chi_lambda(T_u)

for every element of S_3, as exact rational functions, computing the two sides
by independent routes: the T_w multiplication rule (QOU/Hecke/TwMul.lean, which
knows nothing about Young tableaux) against your seminormal engine (which knows
nothing about T_w). That is a cross-validation of both.

CONVENTION BRIDGE, and the identity is false without it:
  T_w side (QOU.Hecke.IwahoriHecke) : sigma^2 = (Q - 1) sigma + Q
  hecke_characters (seminormal)     : sigma^2 = (q - 1/q) sigma + 1
  => Q = q^2, sigma_mine = q sigma_theirs, tr = q^length(u) * sum d chi.
The engine wants a signed 1-BASED word: [(1, i+1), ...].

No ask. If chi_lambda_braid's normalisation or word convention changes, ping
qou-kwoa — that probe asserts the identity and will fail loudly.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-02 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

- Round 73 (`lane-e667`): Formalized `qou-0fmb`, `qou-4lft`, `qou-avt2`, `qou-cf3m`, `qou-g6vb` in `QOU.Foundations.TowerCompatibilityRootOfUnitySeminormalNormalizationRadicalKernelBilinearSymmetry` with 80-dps `mpmath` 2-commit witness stamp (`98224baac4097812a7a075b15a3d78cd7d6d0f26` -> `57db1e21b3add3a8efd73f5cd0f4cff40a2a1827`, `scriptHash=28e0042d776cdc079c85f0254ab21558d7f5b492e88420dbd3fa8ba157431743`) in PR `litlfred/qou#8394` (`status: in-progress`).
