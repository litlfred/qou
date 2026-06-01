# 2026-06-01 — Is M_λ a FORCED categorical composite? (twist × character × q-dim)

**Branch:** `claude/e0-lambda-composite-2026-06-01`
**Sibling branches (do NOT touch):** `claude/e0-lambda-map-options-2026-06-01` (option-ranking
scoping doc — `docs/audits/2026-06-01-e0-lambda-substrate-derivation-options.md`),
`claude/e0-lambda-tryall-lean-2026-06-01` (5 candidates tested in isolation).
**This task is DIFFERENT:** not "which single object wins" but "is M_λ a STRUCTURED COMPOSITE
of several substrate objects, with the composition FORCED by the mass functor's categorical
definition (zero free parameters, zero chosen exponents)?"

**Status (this section is the DERIVATION-FIRST step — written before any number is computed).**

---

## BLUF (derivation-first; the verdict appears after the probe runs)

The discipline knife-edge: a composite `M_λ = [θ_λ ▷ χ^λ(K)] · dim_q(λ) · (Archimedean eval)`
is LEGITIMATE only if every factor and every exponent is **read off the functor's definition**.
If we *choose* which factors multiply or tune any power to hit {e⁻, p, n}, it is a LATENT FIT
(🔴) — exactly the trap that killed the six prior ansätze, and the trap the sibling option-doc
flags for Candidates 1–6.

This doc does the derivation FIRST, then tests. The test against {e⁻, p, n} is a
**falsification test, not a fit target** — no tuning, no back-solve.

---

## Step 1 — What does the mass functor's DEFINITION actually say? (read off the code/props)

### 1a. The production mass formula is a SINGLE Geom call (no per-λ sum)

Canonical (post-PR #1080, `docs/lambda-scale-absorbed-into-geom-full.md`):

```
m(K) = m_e · Geom_full(K, q₀)
```

`folio-assistant/computations/_li_2_q_util.py :: geom_full_borromean(q)` computes

```
Geom_full(𝓑₃, q) = [ Vol(𝓑₃) / ℏ_q² ] · linking_weight_family_a(q)
                  = [ 8·G / ℏ_q² ]      · (5/2 + (3/4) h²)
```

with `ℏ_q = 1 − q⁻¹`, `h = q − q⁻¹`, `G = Catalan`. **This is a single opaque scalar.** It does
NOT carry a `Σ_λ` per-Wedderburn-block decomposition. So the cleanest-possible outcome —
"`Geom_full` already decomposes per-block, just extract M_λ" — is **FALSE for the production
Geom_full**. The proton's `Geom_full` is `Vol/ℏ² × q-dim-block-sum`, not `Σ_λ M_λ`.

**Finding 1: production `Geom_full` is NOT a per-λ composite.** It is a hyperbolic-volume scalar
times an H_4-Wedderburn q-dimension AVERAGE (`linking_weight_A = (1/4)·Σ_{λ⊢4} dim_q V_λ`,
proved identity in `lambda-scale-substrate-form.lean`). The block-sum that appears is over the
*ambient H_4 representation* (a measure factor), NOT over the knot's own character per block.

### 1b. The pre-Archimedean chain's mass identity DOES have a per-λ form (step 6 + step 9)

Cheat-sheet (`docs/canonical-derivation-cheat-sheet.md`, step 6 + step 9):

```
tr_M(β) = Σ_λ y_λ(q) · χ_λ(β)              (Markov-trace = Frobenius pairing, Wenzl bridge)
B(𝔥)   = m_e · ρ · [ |tr_M(T_w)| + tower(T_w) + tr_M(C_{dim_q}) ] |_{q=q₀}
```

So the mass functor's INPUT `tr_M` is genuinely a per-λ sum `Σ_λ y_λ χ_λ`. The Archimedean
functor `τ : 𝐂 → Vec_ℝ` then evaluates at `q = q₀`. **A per-block summand is therefore
`y_λ(q₀) · χ^λ(β_K)` evaluated archimedean-ly** — this IS a forced per-block object, with NO
free parameter (`y_λ` is Wenzl-unique, `χ^λ` is Hoefsmit, both cached at 50 dps).

### 1c. Where do θ_λ (ribbon twist) and dim_q(λ) enter the DEFINITION?

- **dim_q(λ):** appears in the functor as the `tr_M(C_{dim_q})` term in 1b (the third bracket
  term) AND inside `linking_weight_A` (1a). It is a categorical *measure* on block λ. Forced
  presence: YES (it is literally a bracket term). Forced as a per-block *multiplier* of the
  character: NOT stated — the definition ADDS `tr_M(C_{dim_q})`, it does not MULTIPLY `χ^λ` by
  `dim_q(λ)`.
- **θ_λ (ribbon twist):** the ribbon eigenvalue on block λ is `θ_λ = q^{2·content(λ)}`. It does
  NOT appear in the production mass formula 1a/1b at all. The only place a *Reeb phase*
  `θ = arccos(χ^(2,1)/2)` enters is the EXPLORATORY `spectral_correction_borromean`
  (`_li_2_q_util.py`, explicitly marked UNPROVED, "trivial Lean stub", do-not-wire-to-production).

**Finding 2: the owner's candidate composite `M_λ = m_e·[Archimedean(θ_λ ▷ χ^λ(K)) weighted by
dim_q(λ)]` is NOT dictated by the functor's definition.** The definition gives a *sum*
`|tr_M| + tower + tr_M(C_dim_q)`, not a *product* `θ_λ · χ^λ · dim_q`. To assemble the product
one must CHOOSE to multiply the three factors and CHOOSE the dim_q exponent (=1). That choice is
not forced; it is a modeling decision → by the knife-edge, **a product composite is a latent fit
unless the multiplication is itself a categorical identity.**

The one place the framework DOES multiply a phase into Geom is the spectral correction (1c), and
it is single-block (V_(2,1) only), explicitly unproved, and produces `m_avg` not per-block M_λ.

---

## Step 2 — The decisive obstruction the composite must survive (BEFORE numbers)

`rho-prefactor-structural-verifier.witness.json` (`allPassed: True`, GAP-A-4) proves:

> proton and neutron have **bit-for-bit identical** `(χ_λ, y_λ, dim_q λ)` profiles at H_3
> (both: `χ^{[2,1]}=1.99419`, `y=0.28093`, `dim_q=2.01090`, etc. — the trefoil 3_1 image).

Therefore ANY composite `M_λ = F(χ_λ, y_λ, dim_q λ, content_λ, θ_λ, q₀)` — including the owner's
`θ_λ·χ^λ·dim_q` product, archimedean-evaluated — yields **IDENTICAL per-block energies for the
proton and the neutron.** But `m_p = 938.272 MeV ≠ m_n = 939.565 MeV` (Δ = 1.293 MeV).

**This is the falsification test, fixed before any computation:** a per-block composite that is a
function of the block's own (character, q-dim, twist) at the H_3 braid strand count *cannot*
reproduce m_p ≠ m_n. The p/n split lives in the braid WORD (the `−HA` vs `−HA/2` crossings in
`per_block_phi_q.particle_braids`), which the *per-λ character at H_3* already collapses to the
same trefoil profile. The only thing that distinguishes p from n in the deprecated
`fit_three_E0` is the `mass_per_block` per-GENERATOR `V̂` values (Φ_q of the raw crossings),
NOT a per-λ character composite.

So the probe (Step 3) will compute the composite and confirm/deny: **does the functor-dictated
per-block object `y_λ(q₀)·χ^λ(β_K)` (1b), and the owner's product variant `θ_λ·χ^λ·dim_q` (1c),
distinguish p from n at all?** If they collapse p≡n, the composite is FORCED-BUT-MISSES (it
cannot even represent the p/n anchor split), independent of any scale.

---

## Step 3 — The probe (raw numbers; falsification, not fit)

`e0_lambda_composite.py` computes, with ZERO free parameters, at the canonical q₀ (50 dps):

1. The functor-dictated per-block summand `s_λ(K) = y_λ(q₀) · χ^λ(β_K)` for `K ∈
   {e⁻, p (trefoil), n (trefoil)}` and the owner's product variant
   `c_λ(K) = θ_λ · χ^λ(β_K) · dim_q(λ)` with `θ_λ = arccos(χ^λ/d_λ)` (Reeb) — both archimedean.
2. The total `Σ_λ s_λ` and `Σ_λ c_λ` per particle, ratioed to `m_e` (the only derived scale in
   the production formula — NOT a fitted E₀).
3. The p−n per-block differences (the falsification: are they zero?).
4. Comparison to the deprecated `fit_three_E0` structure: does the composite need 1 scale, 3
   scales, or 0?

**No quantity is tuned to {e⁻, p, n} or to B_AME.** The anchors are read, the composite is
computed independently, residuals reported raw.

---

## Verdict

_(filled in after the probe — see witness `e0-lambda-composite.witness.json`)_

---

## Cross-references

- `docs/audits/2026-06-01-e0-lambda-substrate-derivation-options.md` — sibling option-ranking (Candidates 1–6, GAP-A-4 obstruction).
- `docs/audits/2026-05-31-gap-a3-a4-feasibility-assessment.md` — GAP-A-4 H_3 impossibility theorem.
- `docs/lambda-scale-absorbed-into-geom-full.md` — m(K) = m_e·Geom_full single-call framing.
- `folio-assistant/computations/_li_2_q_util.py` — geom_full_borromean (production) + spectral_correction (exploratory composite).
- `folio-assistant/computations/_deprecated/per_block_phi_q.py` — the fit_three_E0 (the thing to replace).
- `folio-assistant/computations/rho-prefactor-structural-verifier.witness.json` — proton≡neutron≡he3 at H_3 (the falsification data).
