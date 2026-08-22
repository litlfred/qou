---
# qou-6hm4
title: confinement-lp.witness.json's Gram is not a trace form, and its uniqueness claim is what the LP degeneracy denies
status: todo
type: bug
priority: normal
created_at: 2026-08-22T15:30:19Z
updated_at: 2026-08-22T15:30:49Z
---


Split out of `qou/augu`, which swept every committed witness carrying a
`y0_star` field. Two independent problems in one artifact, dated 2026-05-02,
`git_sha c8dbe912`.

## 1. The committed `gram_matrix` cannot be `tr_M(bᵢbⱼ)`

Three checks, any one of which is disqualifying.

**It is not symmetric.** `max|G - Gᵀ| = 0.4269`. A trace form is symmetric
because `tr_M(ab) = tr_M(ba)`. Concretely `G[1][3] = 0.551443` while
`G[3][1] = 0.124491`.

**The asymmetry is a row swap, not noise.** Permuting rows to `(0,1,2,4,3,5)`
— i.e. exchanging `L₊` and `L₋` — makes it **exactly** symmetric,
`max|G - Gᵀ| = 0.0`. Rows 3 and 4 are transposed relative to the columns.

**Even repaired it is the wrong rank.** The row-swapped matrix is rank 6,
`det = 0.3608`, eigenvalues `[0.414, 0.428, 0.428, 1.282, 1.282, 2.893]` — all
positive. The H₃ Markov-trace Gram is **rank 5 for every `q ≠ 1`**: `det G = 0`
identically in ℚ(q) (`k4f8`), and the canonical `pyhecke.gram` at the substrate
`q₀` gives

```
eigenvalues  [-0.75270211, 0.0, 0.75270211, 0.75270211, 0.75270211, 4.23033923]
rank 5   det 4.0e-17   min|eig| 1.85e-16   max|G - Gᵀ| 0.0
```

No `q` and no braid insertion `G^w = tr_M(bᵢ w bⱼ)` produces rank 6 — `k4f8`
showed the sign-block ideal is annihilated for any `w`. So the row swap alone
does not recover the trace form; the committed matrix is a different object.

**`q` does not explain it.** The witness records
`q0 = 1.1099785955541805` against the canonical `1.1099785827513808` — 8
figures. What differs is the Markov parameter: the witness has
`z = 0.4993203340335982 = G[0][1]`, canonical `tr_M(σ₀) = 0.61268804`.

**Downstream.** The committed `gram_eigenvalues`
`[-0.7408, 0.4140, 0.4281, 0.7408, 1.2820, 2.8931]` are the eigenvalues of the
**asymmetric** matrix — the `±0.7408` pair is the fingerprint of an
antisymmetric component, not a real spectrum. `lp-duality-check` reports
`±0.9557` around the same `0.414 / 0.428 / 1.282 / 2.893` core and flags
`"indefinite": true`. Whether any downstream claim rests on "the Frobenius Gram
is indefinite" needs checking; the canonical form's negative eigenvalue is
`-0.7527`, so indefiniteness itself is real — but these particular numbers are
not its spectrum.

The witness is internally consistent in one respect: its `markov_traces` field
equals its own row 0, so the `t = G e₀` identity holds for whatever the object
is, which is why its duals still come out `y* = e₀`.

## 2. "Unique optimal" is what the LP's own duals deny

The description reads

> "LP proof that B₃ is the **unique** optimal confinement operator over all of
> H₃(q)"

while the same file records

```
y0_star -0.0    dual_obj -0.0    primal_obj -2.04e-16
y_star  [1, 0, 0, 0, 0, 0]       active_set [0]
```

Optimal value 0, certificate `e₀`. That is the `t = G e₀` degeneracy: the
objective is bounded below by one of its own constraints, the bound is `0`, and
the optimal face is whatever satisfies `(Gx)₀ = 0` — not a point.
`qbeta-confinement-sdp-offset-homogeneity` states the consequence in its own
witness data:

> "the optimal face is not a point, so `x*` and hence the offset are not
> determined by the LP; the returned point is a solver choice"

Uniqueness is precisely what a non-singleton optimal face precludes. The
returned `x_star` is one vertex among many.

**Not claimed:** that B₃ is not the confinement operator. Only that *this LP,
as committed*, does not prove it unique — its optimum is a face and its optimal
value is 0 for every target.

## Next

- [ ] Re-derive the Gram from `pyhecke.gram` (importable — see `augu`) and
      re-emit, or establish what the committed matrix actually is and relabel.
- [ ] Check whether the row swap is in the producing script or in
      serialisation. The producer is not named in the witness (`scriptFile`
      absent); find it first.
- [ ] Re-read "unique optimal B₃" against a degenerate optimal face. If
      uniqueness is wanted, it has to come from a tie-break the LP does not
      currently encode — compare `qou/ndsa`, which argues a formulation that
      survives has to change the **objective**.
- [ ] Audit whether anything downstream cites this witness's
      `gram_eigenvalues` or its indefiniteness.
