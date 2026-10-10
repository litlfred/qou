---
# qou-owzq
title: Does the Sym2 parity exclusion survive root-of-unity truncation?
status: completed
type: task
priority: normal
created_at: 2026-08-25T16:45:18Z
updated_at: 2026-08-25T19:47:22Z
parent: qou-8lxd
---

Spun off from qou-60o2 (PR #5764), which proved: any object of the SINGLE-FIBRE
tensor category passing the Sym^2 gate has EVEN dimension, so no dim-3 object
passes, reducible or not. That result is stated for the CLASSICAL fusion data,
which Drinfeld-Jimbo preserves at GENERIC q (same fusion rules, same
orthogonal/symplectic type).

At a ROOT OF UNITY the category is truncated to the tilting/negligible quotient
and is a DIFFERENT category. Whether the parity argument survives there is NOT
settled by that file, and I did not attempt it.

WHY THIS MATTERS RATHER THAN BEING A PEDANTIC CAVEAT: root-of-unity truncation
is the eightfold chapter's OWN candidate mechanism — §8 item 5, 'Truncation
mechanism' (T4). So this is a live escape route from the exclusion, sitting
exactly where the chapter already suspects the answer might be. Naming it is the
difference between a scope-(b) exclusion honestly bounded and one quietly
over-stated.

WHAT WOULD SETTLE IT (not yet done, do not cite the following as evidence):
- In C(sl2, l) the simples V_0..V_{l-2} are still self-dual with FS type
  (-1)^{2j}, and V_j still has VECTOR-SPACE dimension 2j+1. If both survive
  truncation, the multiplicity count and hence the parity argument should carry
  over verbatim, and the exclusion extends. PLAUSIBLE, UNVERIFIED.
- The genuine subtlety is WHICH dimension the downstream arguments use. The
  Schur-Weyl row cap l(lambda) <= dim V uses the honest vector-space dimension;
  the Ocneanu relation dim_q V = [N]_q => z.[N]_q = q^N uses the QUANTUM
  dimension, and at a root of unity those come apart (quantum dimensions can
  vanish or go negative). An argument that silently swaps one for the other is
  exactly the arity/type conflation the da-arity-conflation criterion exists to
  catch.
- A NEGATIVE is equally valuable: if truncation genuinely admits a 3-dimensional
  gate-passing object, that is a live N=3 route and reopens the chapter's
  principal problem from a direction currently written off.

Scope discipline: nothing above is a result. It is a statement of what evidence
would look like.

## Corpus check 2026-08-25 — the existing three-row results do NOT answer this

Relevant finding surfaced in the PR #5762 thread (the >=3-row stratum audit), and it
sharpens rather than closes this bean.

I had assumed the corpus's '>=3-row stratum is a structural zero under convention D'
result might already be the root-of-unity story, in which case this bean would be
partly answered. IT IS NOT. Quoting the measured finding there:

  wenzlWeight_eq_zero_iff carries hQ : forall k : Z, k != 0 -> Q^k != 1 — i.e. Q is
  explicitly GENERIC, NOT a root of unity. What vanishes is a Schur polynomial in r
  variables when l(lambda) > r, since schurPrincipal r Q mu = s_mu(1, Q, ..., Q^{r-1})
  has only r of them. So at q_0 nothing is truncated away: H_n(q) is semisimple, every
  lambda |- n is a block of it, each with NONZERO dim_q.

Two consequences for this bean:

1. The corpus's three-row vanishing is a GENERIC-q weight vanishing, in the same
   regime my Sym^2 parity result is stated for. So it is not evidence about the
   truncated category either way, and this bean cannot be closed by citing it.
2. It is a live worked example of the exact trap I flagged as the likely failure mode
   here: 'y_lambda = 0' (weight) and 'dim_q = 0' (quantum dimension) are DIFFERENT
   functions, and the sibling measured seven blocks at n = 6 with y_lambda = 0 and
   min dim_q = 1.0 — none zero. Conflating them changed a downstream sum by more
   than 2x (Sigma 1/dim_q = 3.202 over all eleven blocks vs 1.479 over the <=2-row
   ones). Anyone attacking this bean will meet the same vector-space-vs-quantum
   dimension distinction, and that measurement is the concrete warning.

So: still open, still generic-q-only, and now with a corpus-verified reason that the
nearby three-row results are not a substitute for doing it.

## 2026-08-25 — ingredient (c) COMPUTED at k = 1..12. NOT Lean-proved. Read the split below.

**Answering the owner's question 'lean proved?' directly: NO.** The FS result
below is a numerical probe over finitely many levels, not machine-checked
mathematics. What IS Lean-proved is a different half, and the two must not be
conflated:

| | status |
|---|---|
| CONSEQUENCE: parity-split multiplicity count ⇒ even dimension ⇒ never 3 | **Lean-proved, sorry-free** (Sym2GateMultiplicity, PR #5764) — and CATEGORY-AGNOSTIC: `sym2SingletCount` is defined over an arbitrary `S : Finset ℕ`, `m : ℕ → ℕ` with the split keyed only on `Even j`, so it never mentions generic-q vs truncated and applies to both |
| PREMISE: the FS split follows the parity of the index | **NOT Lean-proved in either case.** Cited literature for generic q; numerically computed at k = 1..12 here for truncated. Mathlib has no SU(2) representation type to state it in |

So the truncated case is now in the SAME epistemic position as the generic-q
case, no better: a Lean-proved consequence resting on a modelling premise that
is supplied from outside Lean. The probe moved the premise from *unverified* to
*computed at finite k*. It did not make anything proved.

Computed, not argued. computations/eightfold/su2k_frobenius_schur_indicator_probe.py
evaluates the Frobenius-Schur indicator directly from the modular data of the
TRUNCATED category via Bantay's formula:

    nu_2(X_c) = (1/D^2) sum_{a,b} N_{ab}^c d_a d_b (theta_a/theta_b)^2

with SU(2)_k data: d_c = sin(pi(c+1)/(k+2))/sin(pi/(k+2)), theta_c = exp(2 pi i h_c),
h_c = c(c+2)/(4(k+2)), Verlinde fusion with the level truncation
c <= min(a+b, 2k-a-b).

RESULT: nu_2(V_c) = (-1)^c for every simple of every SU(2)_k with k = 1..12.

THE AGREEMENT IS EXACT, AND THAT CLAIM IS EARNED RATHER THAN ASSUMED. First run
gave worst residual 1.5e-60 at mp.dps=60 -- i.e. AT the arithmetic floor, which
AGENTS.md correctly forbids reporting as 'exact'. So the probe now re-runs the
whole comparison at four precisions:

    mp.dps= 40  worst = 1.03348e-40   floor ~1e-40
    mp.dps= 60  worst = 6.22354e-61   floor ~1e-60
    mp.dps= 90  worst = 4.92769e-91   floor ~1e-90
    mp.dps=120  worst = 1.2596e-120   floor ~1e-120

The residual tracks the floor across all four, so it is roundoff and the identity
is exact. Had it plateaued at a fixed size, that size would have been a real
deviation and the answer would be the opposite one.

CONSEQUENCE: all three ingredients of the parity argument hold in the truncated
category --
  (a) distinct simples pairwise non-isomorphic  -- holds
  (b) cross terms killed by self-duality        -- holds (simples still self-dual)
  (c) FS type still (-1)^{2j}                   -- COMPUTED, holds
so the multiplicity count carries over verbatim: a gate-passing object is a sum of
pairwise distinct even-dimensional simples, hence has even vector-space dimension,
hence is never 3-dimensional. The Sym^2 parity exclusion proved for generic q in
PR #5764 EXTENDS to root-of-unity truncation.

WHAT THIS CLOSES: the escape route. Root-of-unity truncation is the eightfold
chapter's own candidate truncation mechanism (§8 item 5), and it does NOT supply a
3-dimensional gate-passing object. The N=3 problem is not solved by truncating.

SCOPE: (a)-(c) are the ingredients of the MULTIPLICITY COUNT. The count itself is
the model, cited not formalised (Mathlib has no SU(2) rep type), exactly as in the
generic-q file. k = 1..12 is finite; the pattern is uniform and structural but no
all-k proof is given here. Probe emits no witness by design; precision discipline
was applied in full regardless (scripts/precision-gates.sh --changed: all blocking
gates green).
