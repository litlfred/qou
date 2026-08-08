---
# qou-8yph
title: 'MATHLIB-INFRA: rectangular Cauchy-Binet det(AB) = Σ_J det(A_J)det(B^J) — absent from Mathlib, gates sp01'
status: in-progress
type: task
priority: high
created_at: 2026-08-08T08:19:02Z
updated_at: 2026-08-08T08:19:02Z
---

`sp01` (the critical path into the whole Specht cluster) names two possible
routes and rules on the first:

> Needs char-0 Cauchy-Binet (det(A A^T) = Σ det(A_J)^2 > 0, **Mathlib lacks
> usable rectangular CB**) OR base-change of the radical to Q/R +
> positive-definiteness of the tabloid-orthonormal form.

Verified that claim: Mathlib has **zero** files matching Cauchy-Binet /
cauchy_binet / CauchyBinet, and no lemma expressing a determinant as a sum
over column subsets. `det_mul` covers only the square case.

## What this unblocks

`specht_form_nondegenerate` (sp01 / qou-0xyc) → `specht_isSimple` → the five
downstream Specht sorries. It is also the natural tool for the ℤ-Gram
corank argument `qou-0xyc` calls its "surviving route", since
`det(G) = det(M Mᵀ) = Σ_J det(M_J)² > 0` gives non-degeneracy directly over
any char-0 field, without the ℝ specialization the owner declined in 2026-07-25.

## Statement

For `A : Matrix (Fin r) (Fin n) R`, `B : Matrix (Fin n) (Fin r) R` over a
`CommRing`:

    det (A * B) = ∑ over strictly monotone f : Fin r → Fin n,
                    det (A.submatrix id f) * det (B.submatrix f id)

with the positive-semidefinite corollary `det (A * Aᵀ) = Σ_f det(A_f)²` that
sp01 actually wants.

## Proof route (standard, and the reason this is not small)

Expand by Leibniz and interchange:

    det(AB) = Σ_σ sgn σ ∏_i Σ_k A(σi,k) B(k,i)
            = Σ_{φ : Fin r → Fin n} Σ_σ sgn σ ∏_i A(σi, φi) B(φi, i)

then group by `φ`. Two facts carry it:
1. **non-injective `φ` contributes 0** — the inner alternating sum cancels;
2. **injective `φ` factors** uniquely as (strictly monotone `f`) ∘ (permutation
   of `Fin r`), and the permutation's sign pulls out.

Honest sizing: this is a few hundred lines and a plausible Mathlib PR in its
own right. Multi-session. Partial progress will be committed with the
frontier marked, never with a weakened statement.

## Todo

- [ ] Statement + square-case sanity specialization (r = n reduces to det_mul)
- [ ] Leibniz expansion and the sum interchange
- [ ] Non-injective φ vanishes
- [ ] Injective φ factors as strictMono ∘ perm
- [ ] Assemble
- [ ] `det (A * Aᵀ) = Σ det(A_f)²` corollary
- [ ] Wire into sp01 / qou-0xyc

## Progress 2026-08-08 — scaffold + Leibniz step

`QOU/MathlibExt/CauchyBinet.lean`, building green.

Proved, axiom-clean (`#print axioms` → propext / Classical.choice /
Quot.sound only):
- `mul_apply'` — `(A * B) i j = ∑ k, A i k * B k j`.
- `det_mul_leibniz` — `det (A * B) = ∑_σ sgn σ • ∏_i ∑_k A (σ i) k * B k i`.
  The Leibniz starting point, no rearrangement yet.

Defined: `Selector r n` (strictly monotone `Fin r → Fin n`, with its `Fintype`
instance), and `minorA` / `minorB`.

`det_mul_eq_sum_minors` carries an honest `sorry`, labelled as the frontier in
the file itself. It is stated so the remaining steps have a target, not so the
conclusion can be cited early — `#print axioms` shows `sorryAx` on it and on
nothing else.

### Dropped a decorative lemma rather than sink time into it

I started with a square-case sanity check (`Selector n n` is a subsingleton,
so `r = n` collapses to `det_mul`). It needs "a strictly monotone
`Fin n → Fin n` is the identity", which Mathlib does not have in usable form —
`Fin.strictMono_unique` does not exist, and the counting proof is a detour.
Since it is decorative rather than load-bearing, it is out. Worth re-adding
later as a test, not as a prerequisite.

### Next

`Finset.prod_sum` to interchange `∏_i ∑_k` into `∑_{φ} ∏_i`. That is the step
that introduces the `φ : Fin r → Fin n` indexing everything after it runs on.
