# A=3 magnitude ROUTE 3 — the multi-sub-link channel sum is killed by Brunnian triviality (scope-b)

**Date:** 2026-08-01
**Branch:** `claude/a3-magnitude-multi-sublink-channel-sum-2026-08-01`
**Axis:** Δ_λ / Option-E · A=3 magnitude cross-channel program (ROUTE 3)
**Free parameters:** 0 · **Nothing wired** · derive-then-check · honest negative

## The gap

`#4364` reached `c₃ = E₀·(1 − τ_Borr) = +0.297 MeV = 0.63× μ₃` — the complete
finite-type sum of the **one** Borromean deficit — a `~1.6×` near-miss against the
derived target `μ₃ = +0.4708` (`AdditiveResidualSimplex`, #4320). The missing
magnitude factor `r* = μ₃/c₃ ≈ 1.585` is **bracketed out of every SINGLE-Markov-
trace ingredient** (level / geometric-`W_λ` / edge / exact-order-μ̄_A / Vassiliev-
weight — three-walls audit `2026-07-26-deltalambda-a3-magnitude-source-three-walls.md`).
Each of those was a **re-weighting of the one 3-body Borromean trace**. The
missing factor must be genuinely many-body.

## ROUTE 3 — the channel-sum reading

The triton is 3 nucleons = **three 2-body sub-channels PLUS the 3-body
Borromean** link. Structurally different from every bracketed probe: a sum over
**distinct** trace objects (different sub-links), not a re-weighting of one. With
per-sub-link deficit `fᵢ = 1 − τ(sub-linkᵢ)` (unit unlink baseline), two candidate
closures:

* additive        `Σ = f₁₂ + f₁₃ + f₂₃ + f₁₂₃`,
* multiplicative  `C = 1 − ∏ᵢ(1 − fᵢ)`   (interface-product / Ursell form).

The AGENTS.md "compositional/trace object is already many-body" caveat says a
"pairwise can't do it" argument against `1 − ∏(1−fᵢ)` is a category error *when
the pairwise deficits are nonzero* — then the cross terms measure a live missing
higher term. So the honest question is: **are the pairwise sub-link deficits
nonzero, or does Brunnian triviality make them exactly zero?**

## Result — WALL (scope-b), Brunnian sub-link triviality (invariant cited)

The Borromean rings `𝓑₃` are the **archetype Brunnian** link: *every proper
2-sub-link is the unlink*. Verified exactly (`borromean_sublink_channel_sum_probe.py`):

1. **Strand-forgetting.** In the band-word model `w₃ = [A₀₁, A₁₂] =
   A₀₁ A₁₂ A₀₁⁻¹ A₁₂⁻¹`, deleting any one strand deletes one commutator argument,
   so the 2-sub-word **freely reduces to the empty word**:

   | forget strand | pairwise sub-word | free-reduce |
   |:---:|---|:---:|
   | 0 | `[A₀₁, A₀₁⁻¹]` | **∅** (unlink) |
   | 1 | `∅` | **∅** (unlink) |
   | 2 | `[A₀₁, A₀₁⁻¹]` | **∅** (unlink) |

2. **Deficits are exactly zero.** Through the corpus symbolic pipeline (Hoefsmit
   `χ_λ` over ℚ(q), Jones–Markov `y_λ`), each pairwise sub-link normalized trace
   `τ = 1` (empty σ-word) ⇒ **`f₁₂ = f₁₃ = f₂₃ = 0` exactly** (rational, no
   floating point). Not small — identically zero, by the topological invariant.

3. **Both closures collapse to the single 3-body deficit.** With the three
   pairwise deficits `= 0`, every cross term of `1 − ∏(1−fᵢ)` vanishes (each factor
   `1 − fᵢ = 1`), so `Σ = C = f₁₂₃` (verified symbolically). The channel
   decomposition supplies **magnitude factor exactly `1`** — it reproduces `c₃` and
   adds nothing. The target `r* ≈ 1.585 ≠ 1` is **NOT supplied**.

This is the AGENTS.md caveat *turned decisive*: because the pairwise deficits are
**provably zero** (Brunnian), the cross terms the caveat protects are themselves
zero. The route does not measure "the size of a missing higher term" — the higher
term **is** `c₃`, and there are no lower terms to add.

## Lean (formalize-first, sorry-free, lean-direct exit 0)

`QOU.MassTheory.BorromeanSubLinkChannelSum`
(`content/quantum-observable-universe/lean/QOU/MassTheory/BorromeanSubLinkChannelSum.lean`):

| decl | content |
|---|---|
| `channelSumAdd` / `channelClosureMul` | additive + multiplicative `1 − ∏(1−fᵢ)` sub-link closures |
| `brunnian_channelSumAdd_eq_triple` | Brunnian (`τ pairwise = 1`) ⇒ additive sum `= 1 − τ₁₂₃` |
| `brunnian_channelClosureMul_eq_triple` | **decisive** — multiplicative closure's cross terms all vanish, `= 1 − τ₁₂₃` |
| `brunnian_closures_agree` | both closures agree = single deficit |
| `brunnian_channel_no_magnitude` `[IsDomain]` | closure `= r*·c₃` only if `c₃ = 0` ⇒ factor exactly 1 |
| `borromean_channelClosure_eq_c3` (ℝ) | concrete collapse to exactly `h⁴(3+h²)/(h²+4)` |
| `borromean_channel_ne_r_star` (ℝ) | `≠ r*·c₃` for `r* ≈ 1.585 ≠ 1`, `h ≠ 0` |

Generic `[CommRing R]` per §7c; `ℝ` only for the concrete positivity corollary.

## Scope classification — genuine (b), not (a)

This is a **scope-(b) structural exclusion** (not merely scope-(a) "this
construction alone"): the invariant is **Brunnian sub-link triviality** — a proved
topological fact that the proper 2-sub-links of `𝓑₃` are unlinks, hence their
trace deficit against the unlink baseline is *identically* zero, not merely small.
The sub-link channel decomposition of the **canonical Borromean triton model**
therefore *cannot* supply any magnitude factor `≠ 1`.

**Caveat (the (b) is scoped to the canonical model).** A *non*-Brunnian
3-component link (linked pairs) would give nonzero pairwise channels. But that is
a different, non-canonical link choice — the Borromean/Brunnian structure *is* the
physical content of the triton (3-body bound, no 2-body sub-bound; the Efimov
signature). Selecting a non-Brunnian link whose sub-link weighting hits `1.585`
would be a **FIT** and is not made here.

## Where this leaves the A=3 magnitude source

ROUTE 3 joins the bracketed list: the missing `1.585×` is **not** in the sub-link
decomposition. Combined with the three-walls audit (level / `W_λ` / cable-width /
Vassiliev all wall) and the sibling ROUTE 1 (operator-branching) / ROUTE 2
(super-Berezinian) attacks in flight, the A=3 magnitude source remains **open**.
The surviving structural distinction ROUTE 3 sharpens: the source cannot be any
*sub-link-additive* or *sub-link-multiplicative* object over the Borromean model —
it must be an *irreducible* enhancement of the single 3-body trace itself (the
three-walls "strictly larger `h⁴`-coefficient that no substrate rule supplies"),
or a departure from the pure-Borromean model that is independently derived (not
fitted).

## Provenance

- Probe: `computations/deltalambda/borromean_sublink_channel_sum_probe.py`
  (witness `borromean-sublink-channel-sum.witness.json`, `closes=false`,
  `free_parameters=0`, `verdict=WALL(scope-b)-brunnian-sublink-triviality`).
- Lean: `QOU.MassTheory.BorromeanSubLinkChannelSum` (sorry-free, lean-direct exit 0).
- Ledger row: `docs/coordination/option-e.md`.
- Bean: `qou-dka4`.
- Companion (the forward-sign complement this refutes the *magnitude* leg of):
  `QOU.MassTheory.BorromeanThreeBodyCluster` (#4354/#4364), which already noted
  "Being Brunnian, no pairwise part is subtracted — it vanishes." ROUTE 3 turns
  that observation into a proved exclusion of the whole channel-sum construction.
