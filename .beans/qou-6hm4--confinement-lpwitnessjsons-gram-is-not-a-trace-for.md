---
# qou-6hm4
title: 'confinement-topological-proof part (i): wrong lambda_-, unlabelled lambda_0 = 0, and a descent mechanism that cannot hold'
status: todo
type: bug
priority: normal
created_at: 2026-08-22T15:30:19Z
updated_at: 2026-08-22T20:30:00Z
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


---

## 2026-08-22 — corrections to this filing, and where the live problem actually is

### The witness is already deprecated, and the corpus already knew part of this

This bean was filed off a sweep of witness *contents* and did not check the
witness's location or history first. It should have. The file is
`computations/_deprecated/confinement-lp.witness.json`, and the retirement is
documented:

> "The prior producer asserted `tr_M(s0 s1 s0) = z^3` via an invalid Markov-move
> chain (the M2 peel requires the maximal generator to appear exactly once; in
> `s1 s0 s1` it appears twice), contradicting the corrected pyhecke
> `TR_M[5] = h z^2 + z` (fix commit be773569; 2026-05-19 deprecated-scripts
> catalog). Its upstream witnesses (`confinement-lp.witness.json`,
> `breit-wheeler-nucleon-nf.witness.json`) were retired to `_deprecated/`."
> — `prop-rigid-monoidal-structural-gap-invariance.ts`

That explains the numbers this bean flagged as unexplained: its
`markov_traces = [1, 0.4993, 0.4993, 0.2493, 0.2493, 0.1245]` against canonical
`TR_M = [1, 0.6127, 0.6127, 0.3754, 0.3754, 0.6912]`. Stale traces, known since
May. The producer is `computations/_deprecated/confinement-lp.py`.

There is also an open QA finding — `confinement-topological.qa.json`,
`da-reproducibility`, `result: warn`, `severity: minor`, devils-advocate
watcher 2026-07-07:

> "the proposition's only empirical support is **Witness**:
> confinement-lp.witness.json (md:99), but that file lives at
> computations/_deprecated/… — the 4^6 enumeration and the LP vertex x* are
> not backed by a live witness."

**So the novelty this bean claimed is smaller than stated.** Corrected.

### What is genuinely new, and it is not about the deprecated file

**1. The asymmetry is a separate defect from the stale traces.** `Gᵢⱼ =
tr(bᵢbⱼ)` is symmetric for **any** trace, correct or stale, because
`tr(ab) = tr(ba)`. So `max|G - Gᵀ| = 0.4269` is not explained by wrong `tr_M`
values, and the row-3/4 swap that repairs it exactly is a real bug. Its
committed `gram_eigenvalues` are therefore the spectrum of an asymmetric
matrix. The rank-6 observation, by contrast, **is** explained by the stale
traces and is not independent — this bean listed it as if it were.

**2. `confinement-topological-proof.md` part (i) is live, and it is wrong in
its numbers and in its mechanism.** This is the finding that matters; the
deprecated witness is cited by part (iii), but part (i) needs no witness and
is checkable directly.

The prose spectrum `{λ₊, λ₊, λ₊, λ_max, λ₀, λ₋}` is **exactly right in shape**.
Against canonical `pyhecke.gram` at `q₀`:

```
canonical   [-0.7527021133, 0.0, 0.7527021133, 0.7527021133, 0.7527021133, 4.230339225]
λ₋          -0.7527        prose says "λ₋ ≈ -0.855"
λ₊ (×3)     +0.7527        λ₋ = -λ₊ exactly
λ₀           0.0           exact: |λ₀| = 1.85e-16
λ_max        4.2303
```

- `λ₋ < 0` is **true**. Part (i)'s headline stands.
- `λ₋ ≈ -0.855` is **wrong**; that figure belongs to a different Gram — it
  appears in `molecular-frobenius-lp` and
  `qbeta-symbolic-sdp-strict-complementarity`.
- **`λ₀ = 0` exactly, and the proof names it without saying so.** That zero is
  the trace-form radical, the q-antisymmetriser, the thing `k4f8` proves is
  identically singular in ℚ(q) and `8na1` builds its whole case on. The
  proof's own eigendecomposition contains the degeneracy, unlabelled.
- `λ₋ = -λ₊` exactly at `q₀`. Observed numerically at one point; whether it is
  an identity in `q` is not established here and would be worth proving.

**The stated descent mechanism fails on both clauses.** The proof says

> "The eigenvector `v₋` corresponding to `λ₋` satisfies `t · v₋ < 0` while
> `Gv₋ ≥ 0` in certain components. Moving along `v₋` decreases the objective
> without violating Frobenius positivity."

At `q₀`, `v₋ = (0, 0, 0, 1/√2, -1/√2, 0)` — the `L₊ - L₋` direction — and

```
t · v₋  = 5.55e-17   (zero, not negative)
G v₋    = (0, 0, 0, -0.532, +0.532, 0)   (has a negative component)
```

`t · v₋ = 0` is forced: `t · v = (Gv)₀ = λ(v)₀` for an eigenvector, and
`(v₋)₀ = 0`. So moving along `v₋` changes the objective not at all, and
violates Frobenius positivity immediately in component 3.

**And no direction can do what the sentence asks.** Because the basis contains
`𝟙`, `t` is row 0 of `G`, so `t · x = (Gx)₀` for *every* `x` — verified
numerically — hence `t · x ≥ 0` for every feasible `x`. The objective is
bounded below by one of its own constraints and cannot be decreased below `0`
inside the feasible set. A negative eigenvalue of `G` is real; it is not what
this LP exploits.

Recorded as a `caveat` authorNote on `prf:confinement-topological`.

## Next

- [ ] Part (i) needs rewriting: correct `λ₋`, say that `λ₀ = 0` and what it
      means, and replace the descent argument. **Authoring, not mechanical.**
- [ ] Part (iii)'s `4^6` enumeration still cites a deprecated witness — the
      existing `da-reproducibility` warn. Re-running it live is the fix, and
      `pyhecke` now imports, so it is no longer blocked.
- [ ] The `severity: minor` on that warn reads as citation hygiene. The
      claim it supports is structurally unprovable by this LP (see above), so
      the severity is arguably understated. Owner call.
- [x] Find the producer — `computations/_deprecated/confinement-lp.py`.
- [x] Establish whether the row swap is real — it is, and it is independent of
      the stale traces.
