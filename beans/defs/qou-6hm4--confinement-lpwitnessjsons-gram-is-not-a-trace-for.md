---
# qou-6hm4
title: 'confinement-topological-proof part (i): wrong lambda_-, unlabelled lambda_0 = 0, and a descent mechanism that cannot hold'
status: in-progress
type: bug
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-22T15:30:19Z
updated_at: 2026-11-15T17:10:00Z
parent: qou-v2om
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


---

## 2026-08-22 (second) — part (iii) re-run live; it does not hold

`computations/probes/confinement_b3_enumeration_recheck_probe.py`, witness
committed, 10/10 assertions. All **5460** words of length 1–6 over
`{σ₀, σ₁, σ₀⁻¹, σ₁⁻¹}`, using the deprecated producer's own arithmetic
verbatim so the comparison is like-for-like.

### It was never blocked on the deprecated witness

`|Δnet|` is **trace-independent**: `expand_inverse`, `reduce_nf` and `crossing`
read only `HA`, and the metric is a sum of NF coefficients. The stale `tr_M`
that got the witness retired does not enter. So part (iii) was checkable the
whole time, and its conclusions were wrong the whole time. The
`da-reproducibility` warn framed this as *"not backed by a live witness"* —
citation hygiene. The actual problem is that the claims are false.

### Four claims, four problems

| proof says | measured |
|---|---|
| "all other words have `|Δnet| > 0.01`" | **382** proton, **167** neutron at or under 0.01 |
| "the mirror … an order of magnitude worse" | mirror ranks **12 / 5460** (proton), **111 / 5460** (neutron) |
| "and all shorter words" | producer loops `for length in [2, 4, 6]` — **odd lengths never enumerated** |
| "`B₃` achieves `|Δnet| = 0.000`" | **circular** — `target_net = float(sum(b3_confined))` |

- **The first claim fails inside the producer's own range.** 187 proton and 139
  neutron words at ≤ 0.01 have length ∈ {2, 4, 6}. Its own sorted table would
  have shown them; `group_results[:12]` prints twelve rows.
- **Odd lengths matter.** The proton's second-best word overall is the
  **length-5** `σ₀⁻¹σ₁σ₀⁻¹σ₁σ₁` at 0.001591 — better than every length-6 word
  except `B₃`, and better than the mirror. 195 odd-length proton words come in
  under 0.01.
- **`B₃` scoring 0 is a tautology.** The target is `B₃`'s own confined net, so
  any operator written into that line scores 0. Rank 1 of 5460 is not evidence
  of selection.

Every figure survives both `q₀` anchors — re-run under `QOU_Q0_ANCHOR=ideal`,
counts identical (382/195/187, 167/28/139), `B₃` rank 1, proton mirror rank 12;
the neutron mirror moves 111 → 109 inside a tie cluster. Measured, not assumed.

**This refutes the enumeration, not `B₃`.** A selection argument needs a metric
that is not defined from the answer.

### Correction: the asymmetry is the stale trace, not a row swap

This bean diagnosed `max|G - Gᵀ| = 0.4269` as a row-ordering error because
exchanging rows `L₊` and `L₋` symmetrises it exactly. **That was a coincidence
in the numbers.** Running the producer's own `build_gram` with two trace
vectors settles it:

```
stale power rule [1, z, z, z², z², z³]   max|G-Gᵀ| = 0.4612   rank 6   det -0.152
canonical pyhecke TR_M                    max|G-Gᵀ| = 0.0      rank 5   det  4.0e-17
                                          spec [-0.7527, 0, 0.7527, 0.7527, 0.7527, 4.2303]
```

They differ in **one entry** — `tr_M(e⁻) = z³` versus `h z² + z`. A Gram is
symmetric for any *genuine* trace, since `tr(ab) = tr(ba)`; the power rule is
not a trace, so the Gram it builds is not symmetric. One wrong entry turns a
symmetric rank-5 form into an asymmetric rank-6 one.

And the producer's line 41 imports the corrected `TR_M` from `pyhecke.gram`,
then line 58 overwrites it with the power rule. The fix was present and unused.

The canonical rank is **5** — the trace-form radical of `qou/k4f8`, which is
also the unlabelled `λ₀` in the proof's own spectrum. Three views of one fact.

## Next

- [ ] Part (i) needs rewriting: correct `λ₋`, say `λ₀ = 0` and what it means,
      replace the descent argument. **Authoring.**
- [ ] Part (iii) needs a metric not defined from `B₃`, or the claim retracted.
      **Authoring.**
- [ ] The `da-reproducibility` warn's `severity: minor` reads as citation
      hygiene; the claims are false, not merely unwitnessed. Owner call.
- [x] Re-run the enumeration live — done, refuted.
- [x] Establish the cause of the asymmetry — the stale `tr_M(e⁻)`, not a row
      swap. This bean's earlier diagnosis corrected.


## What is ESTABLISHED (two independent proofs)

The H_3 Markov-trace weight vector used across the corpus,

    TR_M = [1, z, z, z^2, z^2, z^3]

on the NF basis [(), (0,), (1,), (0,1), (1,0), (0,1,0)], is **not a trace**.

**Proof 1 — not cyclic.** With x = T_s0 and y = T_s1 T_s0, computed in the H_3
regular representation:

    tr(xy) - tr(yx) = z (z - q) (q z + 1) / q

which is nonzero: -0.426952471076 at z_C and -0.461171580324 at z_D. A trace is
cyclic by definition. (Note the factor: it IS cyclic exactly at z = q and
z = -1/q, the two degenerate roots -- which is why this can hide.)

**Proof 2 — not a class function.** Solving TR_M = y_3 chi^(3) + y_21 chi^(2,1)
+ y_111 chi^(1^3) over the three irreducible characters returns NO SOLUTION.
By Wedderburn any trace on H_3 must decompose that way.

## The correct value, and where it comes from

From the DEFINING Markov property tr(x T_n y) = z tr(x y) plus the Hecke
relation T^2 = h T + 1:

    tr(T_{s1 s2 s1}) = z * tr(T_{s1}^2) = z (h z + 1)      NOT z^3

`z^3` is what you get from assuming tr(T_w) = z^{len(w)}, which holds for
len <= 2 in H_3 and fails at len 3 because the Hecke relation kicks in. The
comment at hecke_core_symbolic.py:160 says exactly that: "Word lengths
0,1,1,2,2,3".

**Convention-INDEPENDENT.** Both steps hold whatever value z takes, so this is
wrong under C and under D alike. It is not the excision question.

## Cross-check against the corpus's own record

With z(hz+1) the solve reproduces `y-lambda-symbolic-witness.json` EXACTLY at
z_D -- y_(3) = (q^4+1)/(q^2+1)^2, y_(2,1) = q^2/(q^2+1)^2, y_(1^3) = 0. With
z^3 there is no solution at all. So the corpus already holds the correct
weights in one place while computing with the incorrect ones in another.

Corroborating: `h4_markov_weights_closed_form.py` DOES carry Hecke corrections
throughout (h*z^2 + z, h*z^3 + z^2, h^2*z^3 + ...), and its `h*z**2 + z` entry
is precisely z(hz+1).

## Blast radius — MEASURED IN PART, NOT COMPLETE

`substrate/hecke_core_symbolic.py:161` defines TR_M_SYM with z^3 and is
IMPORTED by `shift_from_nf_basis.py`, which computes
`tr_q = sum(nf_list[i] * TR_M_SYM[i])` and describes it as "canonical Markov
via TR_M_SYM".

13 further live files carry the same literal (atom_mass_derived:102,
basis_knot_tables:54, ch-bond-writhe-lp:30, compound_shift_nf:257,
h4_markov_character_decomposition:111, h4_markov_weights_closed_form:111,
hh-trefoil-corrected:51, intermediate_knot_detection:31, jet_knot_invariants:56,
photon_operator_table:60, probes/markov_reduction_h3_to_h4_verify:115,
probes/nucleon-lp-convention-probe:91), plus 14 in _deprecated/.

**NOT established: that every downstream number is wrong.** A use whose words
never reach the 6th basis element is unaffected, and I have not checked which
do. Do not quote "13 broken producers" -- quote "13 live sites carry it;
consumption not yet traced".

## How I found it

Chasing why the convention-D migration of compound_shift_nf moved 95 fields. I
noticed the 6th weight looked wrong, and deliberately did NOT conflate it with
the migration. It turns out to be the larger of the two problems, and it means
the migration measurement was of a doubly-wrong quantity.


## 2026-08-30 — ROOT CAUSE IDENTIFIED: see qou-isu5

Part (i)'s asymmetry is NOT a row-ordering artefact. The H_3 Markov weight
vector used to build this Gram is [1, z, z, z^2, z^2, z^3], and z^3 on the
longest element is wrong -- the Ocneanu value is z(h z + 1), from the defining
Markov property plus the Hecke relation. The z^3 functional is therefore NOT
CYCLIC (tr(xy) - tr(yx) = z(z-q)(qz+1)/q, nonzero), hence not a trace, hence
G = tr(b_i b_j) is not symmetric.

At this witness's own q0 = 1.1099785955541805 and z_C:
    z(hz+1) = 0.551443419919830  = this bean's G[1][3] = 0.551443
    z^3     = 0.124490943129969  = this bean's G[3][1] = 0.124491
    diff    = 0.4270             = this bean's max|G - G^T| = 0.4269

Three figures to six digits. The row permutation this bean found hides the
asymmetry without fixing the functional, which is exactly why the permuted
matrix still has the WRONG RANK (6, not 5) -- that rank is the tell.

(The append above this section, dated the same day, landed here by a shell
glob error while filing qou-isu5. It is the correct analysis and it belongs
with this bean, so it stays; qou-isu5 carries the same text as the primary.)

Full derivation, blast radius and cross-checks: qou-isu5.

## 2026-11-15 — re-scoped by the γγ rule

The owner ruled that the γγ selection rule also covers the nuclear bond letters. Any number in this bean computed on the single-crossing interface letters of `atom_braid_word_3A` (`d_k`, `μ_e`, the chain law `∏(z_D + d_k)`, the `b₃` magnitudes −1.2277 / −0.7973 MeV, or a sign map on that word) is now a record of a superseded word, not a current result. Lean results stated for generic bond weights are unaffected. The redo waits on a γγ-selected word per nucleus (PR #7876). Record: `docs/audits/2026-11-15-gg-rule-rescopes-old-letter-binding.md`. The bean stays open.
