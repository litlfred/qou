---
# qou-jfr8
title: 'SW-5: irreducibility + pairwise inequivalence of the ρ_λ'
status: in-progress
type: task
priority: normal
created_at: 2026-08-02T19:33:07Z
updated_at: 2026-08-19T13:41:54Z
parent: qou-59vq
blocked_by:
    - qou-u86i
---

Each Hoefsmit rep is irreducible and ρ_λ ≇ ρ_μ for λ≠μ (distinct central characters). Ref: [wenzl1988].

## ✅ Concrete (2,1) case PROVED (2026-08-10) — sorry-free, axiom-clean

[`QOU/SchurWeyl/Irreducibility.lean`](https://github.com/litlfred/qou/blob/claude/agent-task-662242-vag458/content/quantum-observable-universe/lean/QOU/SchurWeyl/Irreducibility.lean):
`seminormal21_no_common_eigenvector` (q≠0) — S0, S1 have no common eigenvector,
hence no common 1-dim invariant subspace, hence the 2-dim shape-(2,1) rep is
IRREDUCIBLE. Proof: an S0-eigenvector is axis-aligned (distinct eigenvalues
q≠-q⁻¹ via q+q⁻¹≠0), but S1 fixes neither axis (c₀₁=1, c₁₀=(q⁴+q²+1)/(q²+1)²>0).
lean-direct EXIT=0; axioms [propext, Classical.choice, Quot.sound]; wired into QOU.lean.

General-λ irreducibility depends on the general seminormal construction — stays
with residual bean qou-im9l (needs SW-4-gen first).


## Re-scoped 2026-08-19 — the general case is now REACHABLE, and the enabling input just landed

Prior state: only the concrete shape-(2,1) case
(`Irreducibility.seminormal21_no_common_eigenvector`, q != 0). The general case
looked blocked on the general seminormal rep. **It no longer is.** Two things
landed since:

- `hoefsmit_seminormal_rep` for all lambda (#5279, qou-im9l) — the reps exist.
- `seminormalRep_qJM` (#5290, qou-t8qh) — **Ram Thm 4.1**: the q-Jucys-Murphy
  element L_k acts DIAGONALLY on the SYT basis with entry q^{2.cellContent} at
  the cell holding k+1.

Ram 4.1 is exactly the classical engine for general irreducibility, and it is now
available as a proved lemma rather than a plan:

1. The JM family {L_1..L_n} acts diagonally, so it generates a commutative
   subalgebra whose joint eigenspaces are spanned by subsets of the SYT basis.
2. **Separation**: distinct SYT of the same shape have distinct content
   *sequences* (c(T,1),...,c(T,n)) — a standard tableau is determined by its
   content vector. Hence the joint eigenvalue sequences (q^{2c(T,k)})_k are
   pairwise distinct at generic q, so each joint eigenspace is ONE line.
   => every H_n(q)-invariant subspace is a span of a SUBSET of the SYT basis.
3. **Connectivity**: an invariant subspace containing T also contains s_k.T
   whenever the swap is admissible, since genMat's off-diagonal entry is nonzero
   (`offDiag`, and `genMat_ne_scalar`). SYT of a fixed shape are connected under
   admissible swaps.
   => the only invariant subspaces are 0 and everything. IRREDUCIBLE.

Step 2 is the one with real content and is where the work is: *content vector
determines the tableau*, plus the genericity that q^{2a} = q^{2b} implies a = b
(which is exactly the q^2 not a root of unity hypothesis already carried by
`seminormalRep`). Step 3 needs SYT connectivity under admissible swaps — check
`SytRowSuperstandard.syt_all_connect_to_some` and
`SytAdmissible.exists_swapAdmissible_of_one_lt_card` before building it.

Pairwise inequivalence rho_lambda !=~ rho_mu for lambda != mu is the second half and
falls out of the same separation: the L_k eigenvalue MULTISET is the multiset of
cell contents of lambda, which determines lambda.

CLAIMED by this session 2026-08-19.
