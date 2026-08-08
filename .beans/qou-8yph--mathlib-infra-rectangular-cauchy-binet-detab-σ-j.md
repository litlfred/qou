---
# qou-8yph
title: 'MATHLIB-INFRA: rectangular Cauchy-Binet det(AB) = Σ_J det(A_J)det(B^J) — absent from Mathlib, gates sp01'
status: completed
type: task
priority: high
created_at: 2026-08-08T08:19:02Z
updated_at: 2026-08-08T09:22:03Z
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

## Progress 2026-08-08 (cont) — steps 2 and 3 proved

All axiom-clean; the file still carries exactly ONE `sorry`, the target.

**Step 2 — regroup by `φ`.**
- `prod_sum_interchange` — `∏_i ∑_k` becomes `∑_{φ : Fin r → Fin n} ∏_i`,
  via `Fintype.prod_sum`.
- `det_mul_eq_sum_over_functions` — `det (A * B) = ∑_φ ∑_σ sgn σ • ∏_i …`.
  Every later step is now a statement about a single `φ`.

**Step 3 — a non-injective `φ` contributes 0.** Done, and by a better route
than the textbook one.

The standard argument pairs `σ` with `σ ∘ (swap i j)` and cancels. That
does not work cleanly here: the term is `∏_i A(σi)(φi) · B(φi)(i)`, and
reindexing by the swap leaves the `B` factor carrying `τ i` rather than `i`,
so the two products are not equal termwise. A hand-rolled involution would
have to fight that.

Instead: the `B` product is `σ`-independent, so factor it out. What remains
is `∑_σ sgn σ ∏_k A(σk)(φk)`, which **is** `Matrix.det_apply` for
`A.submatrix id φ`. A non-injective `φ` repeats a column of that submatrix,
and Mathlib's `det_zero_of_row_eq` (through `det_transpose`) already kills
it. Three short lemmas instead of an involution argument:
`sum_perm_eq_det_submatrix`, `det_submatrix_eq_zero_of_not_injective`,
`sum_over_perms_eq_zero_of_not_injective`.

### Two Lean-side snags worth recording

- `(Matrix.det_apply _).symm` as a **term** blew the heartbeat budget
  ("(deterministic) timeout at `whnf`"). The same proof as
  `by rw [Matrix.det_apply]; rfl` is instant — the term-mode elaboration was
  the problem, not the mathematics.
- `simp_rw` through the split/factor chain made no progress; spelling the
  rewrite out with an explicit `Finset.sum_congr` worked first time.

### Next

Step 4, the harder half: an **injective** `φ` factors uniquely as
`f ∘ π` with `f` strictly monotone and `π : Equiv.Perm (Fin r)`, and
`sign π` pulls out. That factorization is where `Selector` finally gets used,
and it is the piece with no Mathlib support — the sorting of an injective
`Fin r → Fin n` into monotone-composed-with-permutation has to be built.

## Progress 2026-08-08 (cont) — step 4 sorting infra proved

Back to ONE `sorry` in the file (the target). Everything below is
axiom-clean.

**Step 4 — an injective `φ` sorts into selector ∘ permutation.** This is the
piece the bean flagged as having no Mathlib support, and it is now built:

- `imageFinset` / `mem_imageFinset` — `φ`'s image as a `Finset`.
- `card_imageFinset` — an injective `φ` has an image of exactly `r` elements.
- `sortSelector` — that image enumerated in increasing order. Strict
  monotonicity comes free, since `Finset.orderEmbOfFin` is an order embedding.
- `toImage` / `toImage_bijective` — `φ` as a bijection onto its own image.
  Injectivity is `hφ`; surjectivity is `Finset.mem_image`.
- `sortPerm` — the induced `Equiv.Perm (Fin r)`, as
  `Equiv.ofBijective (toImage φ)` composed with `(orderIsoOfFin …).symm`.
- `sortSelector_comp_sortPerm` — **the factorization**: `f (π i) = φ i`.

The factorization proof turned out to be three lines. `orderEmbOfFin` is
definitionally the coercion of `orderIsoOfFin`
(`Finset.coe_orderIsoOfFin_apply` is `rfl`), so the whole thing is one
`OrderIso.apply_symm_apply` round trip plus two `rfl`s. `Finset.orderEmbOfFin`
carrying the strict monotonicity for free was the other saving — `Selector`'s
proof obligation is discharged by `.strictMono` on the embedding.

### Remaining

- the sign bookkeeping: `sgn σ` vs `sgn (σ ∘ π)` when the `σ`-sum is
  reindexed by the induced permutation;
- assembly: `φ ↦ (sortSelector, sortPerm)` is a bijection from injective `φ`
  onto `Selector r n × Equiv.Perm (Fin r)`, which converts the sum over
  injective `φ` into the sum over selectors.

The injectivity/non-injectivity split is now fully covered on both sides —
step 3 kills the non-injective half, step 4 parameterizes the injective half.

## Progress 2026-08-08 (cont) — steps 3b, 5, and both round trips

Still ONE `sorry` (the target). All of the following axiom-clean.

**Step 3b — drop the injectivity hypothesis.** The factoring never needed it:
for *every* `φ`, the `σ`-sum is `det (A.submatrix id φ)` times the
`σ`-independent `B` product. `sum_over_perms_eq` states that, and
`det_mul_eq_sum_det_submatrix` gives

    det (A * B) = ∑_φ det (A.submatrix id φ) * ∏_i B (φ i) i

which is the form assembly consumes. Step 3 is now the special case where the
determinant is zero.

**Step 5 — sign bookkeeping.** `det_submatrix_comp_perm`:
`det (A.submatrix id (f ∘ π)) = sign π * det (A.submatrix id f)`. One line
once spotted: `A.submatrix id (f ∘ π)` is *definitionally*
`(A.submatrix id f).submatrix id π`, so Mathlib's `det_permute'` applies
directly. No sign lemma had to be built.

**Both round trips** for the `(f, π) ↦ f ∘ π` bijection:
- `sortSelector_comp` — sorting `f ∘ π` recovers `f`. `f` is already the
  increasing enumeration of that image, and `Finset.orderEmbOfFin_unique`
  says there is only one such map.
- `sortPerm_comp` — sorting `f ∘ π` recovers `π`, since the factorization
  pins it and `f` is injective.

Note: `ext` on an `Equiv.Perm (Fin r)` goal unfolds to `Fin.val` equality,
which does not match a proof of the `Fin` equality itself; `Equiv.ext` is the
right entry point.

### What is left

Only the assembly. Every ingredient exists:

- non-injective `φ` ⇒ term is 0 (`det_submatrix_eq_zero_of_not_injective`);
- injective `φ` ⇔ a unique `(f, π)` (`sortSelector_comp` + `sortPerm_comp`
  give both round trips, `comp_perm_injective` the forward direction);
- the sign (`det_submatrix_comp_perm`);
- `det (minorB B f) = ∑_π sign π ∏_i B (f (π i)) i` is `Matrix.det_apply`.

Remaining work is a `Finset.sum_nbij'` (or an `Equiv` between injective `φ`
and `Selector × Perm`) plus the arithmetic regrouping — bookkeeping, not new
mathematics.

## Progress 2026-08-08 (cont) — step 6 pieces; only the reindexing left

27 declarations, **1 `sorry`** (the target). Everything else axiom-clean.

Added:
- `term` — the summand, named so the reindexing has something to talk about.
- `term_eq_zero_of_not_injective` — only injective `φ` contribute.
- `sum_term_comp_perm` — **for a fixed selector, summing the term over all
  permutations gives `det (minorA A f) * det (minorB B f)`**. This is the
  whole right-hand side, per selector.

### What is genuinely left

One thing: `∑_φ term = ∑_{(f,π)} term (f ∘ π)`, i.e. the `Finset.sum_bij'`
reindexing. Both round trips (`sortSelector_comp`, `sortPerm_comp`), the
forward map (`comp_perm_injective`) and the vanishing
(`term_eq_zero_of_not_injective`) are all in hand — the remaining work is
plumbing them into `sum_bij'`, whose dependent-membership signature is why
`sum_nbij'` will not do.

### Lean friction worth recording (all cost real time)

- `rw [Matrix.det_apply]` rewrote the **wrong** determinant — it matched
  `minorA`'s before `minorB`'s. Fixed by stating the `minorB` expansion as a
  named `have` instead of rewriting in place.
- `ring` fails where the two sides differ only by `(f ∘ π) i` vs `f (π i)`:
  it treats them as distinct atoms. `simp only [Function.comp_apply]` first,
  then `ring`.
- `rfl` also fails there — `Function.comp` does not reduce in that position
  without the explicit unfolding.
- `Units.smul_def` has to be applied to **both** sides; a single `rw` hits
  only the first occurrence and leaves a `•` behind that `ring` cannot see
  through.

### Revised sizing

The bean estimated "a few hundred lines, multi-session, plausible Mathlib PR".
Line count is tracking well under that — Mathlib's `Finset.Sort` API and
`det_permute'` did more than expected, and the two hardest-looking steps
(sign bookkeeping, the sorting factorization) were each a handful of lines.
The Mathlib-PR judgement stands: Cauchy–Binet is genuinely absent upstream.
## DONE 2026-08-08 — complete and sorry-free

`QOU/MathlibExt/CauchyBinet.lean`: 489 lines, 37 declarations, **zero
`sorry`**. `lake build QOU.MathlibExt.CauchyBinet` green (1304 jobs).
Every headline declaration verified with `#print axioms` reporting only
`propext, Classical.choice, Quot.sound`.

### The theorem

    det_mul_eq_sum_minors :
      (A * B).det = ∑ f : Selector r n, (minorA A f).det * (minorB B f).det

over any `[CommRing R]`, `Selector r n = {f : Fin r → Fin n // StrictMono f}`.

### The corollaries sp01 actually consumes

- `det_mul_transpose_eq_sum_sq` — `det (A Aᵀ) = ∑_f (det A_f)²`. The
  `minorB Aᵀ f = (minorA A f)ᵀ` identity is `rfl`, so this is three lines.
- `det_mul_transpose_nonneg` / `det_mul_transpose_pos` — over
  `[CommRing S] [LinearOrder S] [IsStrictOrderedRing S]`, the Gram
  determinant is `≥ 0`, and `> 0` as soon as **one** minor is nonzero
  (`Finset.sum_pos'`; the other terms are squares and cannot cancel it).
- `det_gram_map_ne_zero` — **the transfer**. For `M : Matrix (Fin r) (Fin n) ℤ`
  with one nonzero `r × r` minor, `det (N Nᵀ) ≠ 0` where `N = M.map Int.cast`
  into any `[Field k] [CharZero k]`. The order is used only over `ℤ`; `k`
  never needs to be ordered.

That last one is the point of the whole bean: it is exactly the route sp01
named, and it keeps the hypothesis at `[Field k] [CharZero k]` instead of
collapsing to `ℝ` — the specialization the owner declined on 2026-07-25.

### The final step (the reindexing) — how it went

`Finset.sum_bij'` on the nose, first compile. Maps:

- `i : φ ↦ (sortSelector hφ, sortPerm hφ)` — **dependent on membership**, which
  is precisely why `sum_nbij'` cannot express it: `sortSelector` needs the
  injectivity proof that membership in `injFns r n` carries.
- `j : (f, π) ↦ f.1 ∘ π`

and the four obligations are the lemmas already banked: `left_inv` is
`sortSelector_comp_sortPerm` under `funext`, `right_inv` is
`sortSelector_comp` + `sortPerm_comp` under `Prod.mk.injEq`, and `h` is
`congrArg (term A B)` of the same factorization.

Two things made this land clean:

- **Definitional proof irrelevance.** `right_inv`'s goal carries the
  membership-derived injectivity proof, not `comp_perm_injective f π`.
  `exact` accepts the mismatch because `Function.Injective φ` is a `Prop`.
  No `Subsingleton.elim`, no proof-transport.
- **Letting `sum_bij'` derive injectivity.** Going the other direction
  (`sum_bij` from pairs to functions, with the non-dependent `i`) would have
  needed `i_inj` proved by hand, which means rewriting under `sortSelector`'s
  dependent proof argument. `sum_bij'` gets injectivity free from the two
  round trips.

### Final sizing verdict

The bean opened with "a few hundred lines, multi-session, plausible Mathlib
PR". Landed at 489 lines including ~150 of docstring, in-session. Mathlib's
`Finset.Sort` API (`orderEmbOfFin`, `orderIsoOfFin`, `orderEmbOfFin_unique`)
and `det_permute'` carried more than budgeted.

**The Mathlib-PR judgement stands** — rectangular Cauchy–Binet is genuinely
absent upstream (no file matches `Cauchy-Binet`/`cauchy_binet`/`CauchyBinet`;
`det_mul` is square-only), and this file is self-contained apart from those
Mathlib APIs.

### Next

Wire `det_gram_map_ne_zero` into `sp01` / `qou-0xyc` — that is a separate
bean's work, not this one's.
