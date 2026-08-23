# Re-posed Frobenius admissibility test — honest NEGATIVE (bean qou-vd7j, 2026-08-02)

**Lead answer: NO. Re-posing the Frobenius per-nucleus admissibility test without
the inconsistent net row does NOT recover a selective ν_SDP. Both re-posed
variants are trivially feasible and NON-SELECTIVE.** The active-channel count is a
constant `1` (the `γ` channel) for every nucleus, so the test reproduces neither
the census target `{²H:1, ³H:2, ³He:2}` nor any discrimination between nuclei.

Probe: [`computations/probes/frobenius_repose_probe.py`](../../computations/probes/frobenius_repose_probe.py).
Witness: [`computations/probes/frobenius-repose.witness.json`](../../computations/probes/frobenius-repose.witness.json).
Log: `/tmp/frobenius_repose.log`. Follows the diagnostic
[`frobenius_admissibility_diagnostic.py`](../../computations/probes/frobenius_admissibility_diagnostic.py)
and audit [`2026-08-02-gemini-q-saddle-offset-salvage.md`](2026-08-02-gemini-q-saddle-offset-salvage.md).

> ## ⚠ CORRECTED 2026-08-23 — the premise below is false (bean `qou/ftuv`)
>
> This audit reasons throughout from *"G … is 6×6 **rank-6, invertible**, so
> `Gx = nf` already fixes `x = G⁻¹nf` uniquely"*. **G is exactly singular.**
> Its determinant tracks the working precision instead of converging —
> `-2.008684335e-57` at 60 dps, `+5.724314033e-117` at 120 dps, sign flip
> included — which is what an exactly-zero determinant looks like in floating
> point. `G` has a one-dimensional kernel
>
> ```
> γ  -0.47268915   σ₀  0.4258543   σ₁  0.4258543
> L₊ -0.38365992   L₋ -0.38365992  e⁻  0.34564624
> ```
>
> confirmed by `‖Gv‖∞ = 3.4e-76` at 80 dps. It is an exact linear relation
> among the six normal-form channels, and it respects the conjugation symmetry
> (`σ₀ = σ₁`, `L₊ = L₋`): under the Frobenius pairing the "6-channel basis"
> spans only five dimensions.
>
> Two consequences for the text below.
>
> **`x = G⁻¹nf` does not exist**, so every statement of the form "the test is
> an invertible linear solve dressed as an LP" describes a solve that cannot
> be performed. `range(G)` is the kernel-perp, and the nuclide `nf` vectors are
> not in it — `|v·nf| / ‖nf‖` runs 0.0027 (¹⁶O) to 0.41 (n). `Gx = nf` has **no
> solution** for them.
>
> **The reported feasibility counts were false positives.** `|G⁻¹| ~ 7.6e15`,
> so the computed `x` is large enough that `G @ x` reproduces `nf` to `2e-16`
> through round-off alone, and the relative-residual check passed on that. The
> corrected figures:
>
> | | audit (f64 inverse) | corrected (MPFR pseudo-inverse) |
> |---|---|---|
> | variant (a) feasible | 1514 / 3558 | **0 / 3558** |
> | variant (b) feasible | 181 / 3558 | **0 / 3558** |
>
> **The lead answer is unaffected, and is strengthened.** The test was
> non-selective because the active-channel count was a constant `1` for every
> nucleus; it is now non-selective because the system is unsolvable for every
> nucleus. Either way it reproduces neither the census `{²H:1, ³H:2, ³He:2}`
> nor any discrimination between nuclei, and ν_SDP stays underived. What was
> wrong was the *mechanism*, not the conclusion.
>
> One quantity the corrected posing does produce, which the old one did not:
> the out-of-range fraction `|v·nf| / ‖nf‖` **varies by nucleus** and falls
> with A (0.369 p, 0.409 n, 0.323 ²H, 0.332 ³H, 0.223 ³He, 0.214 ⁴He, 0.188
> ⁷Li, 0.026 ¹²C, 0.0027 ¹⁶O) where the old active-count was constant. It does
> **not** reproduce the census — ²H (target 1) sits at 0.323 and ³H (target 2)
> at 0.332, effectively equal — so this is a new observable, not a rescue.

## What was tested

The original Frobenius LP (`solve_frobenius_dual_lp`) imposes 7 equalities —
`1ᵀx = A` (net) + `G x = nf` (6 Frobenius rows) — on 6 unknowns. The diagnostic
showed the 0/3558 is an over-determination artifact: `G` (the H₃ NF Gram at q₀)
is 6×6 **rank-6, invertible**, so `Gx = nf` already fixes `x = G⁻¹nf` uniquely,
and its implied net `1ᵀG⁻¹nf` (O(1)) ≠ the mass number A → the net row is
inconsistent for every nucleus.

Two re-posings remove the inconsistent net row:

- **(a) Drop `1ᵀx = A` entirely.** LP → `min t·x s.t. Gx = nf`. Feasible ⟺
  `nf ∈ range(G)`.
- **(b) Replace the net RHS `A` with the consistent value `1ᵀG⁻¹nf`.** LP →
  `min t·x s.t. Gx = nf AND 1ᵀx = 1ᵀG⁻¹nf`; the net row is now redundant.

## Numbers (the evidence)

`G` eigenvalues `[-0.855, 0.102, 0.855, 0.855, 0.855, 3.477]`, rank 6.

Variant (a) Frobenius shadow prices `y = G⁻ᵀt = (γ:1, σ₀:0, σ₁:0, L₊:0, L₋:0,
e⁻:0)` — **nucleus-independent** (they depend only on `t`, `G`, not on `nf`), so
the active channel is always `{γ}`, count 1, for every nucleus.

| nucleus | A | ν_SDP target | (a) feasible | (a) #chan | (b) feasible | (b) #chan |
|--|--:|--:|--|--:|--|--:|
| ²H | 2 | **1** | True | 1 | True | 1 |
| ³H | 3 | **2** | True | 1 | True | 1 |
| ³He | 3 | **2** | True | 1 | True | 1 |
| ⁴He | 4 | — | True | 1 | True | 1 |
| ⁷Li | 7 | — | True | 1 | True | 1 |
| ¹²C | 12 | — | True | 1 | True | 1 |
| ¹⁶O | 16 | — | True | 1 | True | 1 |
| ⁴⁰Ca | 40 | — | True (mpfr-limited) | 1 | False (HiGHS tol) | 0 |
| ⁵⁶Fe | 56 | — | True (mpfr-limited) | 1 | False (HiGHS tol) | 0 |

Full AME chart (3558 entries, A≥1; 2218 f64-finite, 1340 heavy-A overflow):

- variant (a): **1514/3558 feasible**, active-count histogram `{1: 1514}`
- variant (b): **181/3558 feasible**, active-count histogram `{1: 181}`

The census active-counts are `{²H:1, ³H:1, ³He:1}` for **both** variants — flat,
not `{1, 2, 2}`.

## Why the counts are not the point

`nf ∈ range(G)` is **mathematically guaranteed** for any finite `nf` (G is
full-rank ⇒ range = ℝ⁶), so feasibility is universal in exact arithmetic. The
measured f64 counts (1514, 181) are capped by two **infra** effects, not physics:

1. the 1340 heavy-A `build_atom_nf`/`G⁻¹nf` f64 overflows (needs the mpfr native
   path), and
2. f64 ill-conditioning of `G⁻¹nf` at large-magnitude `nf` (variant (a) uses a
   relative-residual test < 1e-9; variant (b)'s HiGHS solver applies its own
   feasibility tolerance that rejects large-RHS problems).

Both vanish under mpfr. The physics content is the **structure**, not the count:
`Gx = nf` is an invertible linear solve, so the "test" has zero degrees of
freedom to optimise and no way to discriminate nuclei.

## Verdict (scope-(a), per AGENTS.md §"refuted/ruled out")

Re-posing **succeeds** at removing the 0/3558 over-determination artifact but
**fails** to recover any selective power:

- **Trivially feasible.** With the inconsistent net row gone, the Frobenius
  admissibility test is an invertible linear solve dressed as an LP — feasible for
  every nucleus (modulo f64 conditioning). This is the honest negative the bean
  asked us to distinguish: dropping the net makes the test *lose its (spurious)
  selectivity*, it does not *gain* real selectivity.
- **Non-selective.** The active-channel set is constant `{γ}` across the whole
  chart because the Frobenius shadow prices `G⁻ᵀt` are independent of `nf`. The
  test cannot reproduce the census `{²H:1, ³H:2, ³He:2}`, nor tell any two nuclei
  apart.

This is a **scope-(a)** finding — "the Frobenius per-nucleus admissibility LP,
*as posed and re-posed here*, has no selective power for ν_SDP." It is **not** a
scope-(b) structural exclusion: it does not prove ν_SDP is underivable by *any*
operator-selection route. What it does show, concretely, is that the nucleus's
identity lives entirely in `nf` and `x = G⁻¹nf` carries no additional selection —
so the discriminating structure, if any, must come from something the H₃ Gram
solve does not see (the tower / Δ_λ, a PSD *inequality* relaxation with genuine
optimisation freedom, or a rank-deficient demand map where `nf ∈ range(G)` is a
real constraint). None of that is wired here.

**ν_SDP stays honestly underived** (`conj:canonical-knot-id-sdp` /
`conj:kashaev-density-equals-sdp-multiplicity` remain open). No fit was wired; no
net normalization was tuned to hit `{1,2}`.
