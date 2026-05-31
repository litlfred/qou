# Audit: Casimir-vacuum conjecture investigation routes

**Date.** 2026-05-30
**Block.** [`conj:casimir-epsilon-vacuum`](../../content/quantum-observable-universe/appendix-surreals/casimir-epsilon-vacuum.md)
**Status.** Three speculative closure routes surveyed; one quick
empirical probe run. **Null result on naïve q-rational closed form.**

This audit accompanies PR #1497 (scaffolding the conjecture) and
documents the routes considered for closing it, so that future
agents pick up where this session stopped instead of repeating
the search.

The audit is the right place for these routes — they are
investigation records, not paper content. The conjecture's `.md`
already enumerates the three open sub-problems; this document
goes into the *how* of attacking each.

## Sub-problem summary (from the conjecture)

| # | Open content | Tractability |
|---|---|---|
| 1 | Existence of categorical `N⊙(A, d)` as a surreal-valued plate-bounded knot-density | medium |
| 2 | `A/d³` scaling of the categorical mode-count | medium (blocked on 1) |
| 3 | `π²/720` prefactor from a Hecke-trace identity matching `ζ(-3) = -1/120` | hard |

## Route A — q-deformed ζ-regularisation (sub-problem 3)

**Sketch.** The standard Casimir prefactor comes from
`ζ(-3) = -B₄/4 = -1/120` regularising `Σ_{n≥1} n³`. A QOU-native
analogue would substitute `n ↦ [n]_q` (q-integer at the substrate)
and look for a closed-form q-rational at `q = q₀ ≈ 1.110`.

**Candidates surveyed.**

1. **`ζ_q(s) = Σ [n]_q⁻ˢ`** (Kaneko–Kurokawa–Wakayama 2002). Converges
   for `s ≥ 1, q > 1`. Computed in the probe:
   - `ζ_q(1) = 3.5370`
   - `ζ_q(2) = 1.5480`
   - `ζ_q(3) = 1.1902`
   - `ζ_q(4) = 1.0789`

   None lie near `π²/720 ≈ 0.0137`.

2. **Damped cubic sum `Σ [n]_q³ · q⁻ᵏⁿ`** for `k ∈ {3, …, 15}`. All
   values are `≥ 1`, ranging from `~21000` (k=3) to `~1.0` (k=15).
   No convergence to `π²/720`.

3. **Low-degree q-rationals `a · π²/(720 · [m]_q^p)`** with
   `m ∈ {2,…,10}`, `p ∈ {1,2,3}`, `a ∈ {1,…,12}`. Closest match:

   ```
   2 · π² / (720 · [2]_q)  =  1.3634e-2
   target:  π²/720         =  1.3708e-2
   residue:                =  7.4e-5  (0.54% relative)
   ```

   Since `[2]_q = q + q⁻¹ → 2` as `q → 1`, this expression
   approaches `π²/720` trivially in the classical limit. The 0.54%
   deviation at substrate `q₀` is *consistent with* but not
   *forced by* this particular q-deformation.

**Empirical witness.**
[`casimir-q-zeta-probe.witness.json`](../../folio-assistant/computations/casimir-q-zeta-probe.witness.json)
records the full search; assertion `best_match_within_one_percent_of_target`
fires at 0.54% residue.

**Honest reading.** This is a **null result** for "trivial q-rational
closed form of π²/720 at substrate". The candidate `2·π²/(720·[2]_q)`
matches at 0.5%, but its `q → 1` limit recovers the textbook
expression for trivial reasons (continuity), not because `[2]_q`
plays a special role.

**Suggestive but non-conclusive prediction.** *If* the categorical
mode-count happens to factor exactly as `2/[2]_q × (textbook)`, the
QOU prediction would be a 0.54% deviation from standard Casimir at
substrate `q₀`. This is **below** the Mohideen–Roy 1998 experimental
precision (~1%), so it would not be falsified by current data — but
also not confirmed. A higher-precision (~0.1%) Casimir measurement
would distinguish.

**Status.** Route A does not close sub-problem 3 on its own.
Recommended follow-up: investigate Cherednik 2006 q-zeta definition
(distinct from Kaneko–Kurokawa–Wakayama) which uses Macdonald
operators and might be more naturally aligned with QOU's
Hecke-algebra substrate.

### Extended candidate search (Route A, 2nd pass)

The probe was extended to include substrate-natural quantities
(ℏ_q², h_q², α_em-derived). Top candidates by relative residue:

| Form | Value | Residue | Note |
|------|-------|---------|------|
| `2·π²/(720·[2]_q)` | 1.3634e-02 | **0.54%** | classical-trivial: `[2]_q → 2` as `q → 1` |
| `12·π²/(720·[10]_q)` | 1.3829e-02 | **0.89%** | substrate-numerical-trivial: at `q₀`, `[10]_q ≈ 11.90 ≈ 12` |
| `4·π²·h_q²/120` | 1.4379e-02 | 4.9% | not trivial; substrate-natural |
| `8·π²·ℏ_q²·[2]_q/120` | 1.2989e-02 | 5.2% | not trivial; substrate-natural |
| `240·α_em²` | 1.2820e-02 | 6.5% | not trivial; substrate-natural |
| `2·α_em` | 1.4617e-02 | 6.6% | not trivial; substrate-natural |

After filtering both **classical-trivial** matches (where `a/m^p =
1`, so the form recovers π²/720 trivially as `q → 1`) AND
**substrate-numerical-trivial** matches (where `a/[m]_q^p` ≈ 1
*at substrate q₀*, so the match is a numerical accident of where
[m]_q happens to land, not a structural identity in `q` as a
variable): **zero non-trivial substrate q-rationals match π²/720
within 1%**.

The closest non-trivial candidate is `10·π²/(720·[9]_q)` at 3.5%
relative residue (above the 1% threshold).

**Empirical conclusion: the π²/720 prefactor is genuinely NOT a
low-degree q-rational of substrate quantities at q₀.**

### Extended Carlitz q-Bernoulli probe (Route A, 3rd pass)

Audit's earlier recommendation: "Cherednik q-zeta / Macdonald-
operator infrastructure" might recover π²/720. Implemented the
**Carlitz q-Bernoulli** definition (Carlitz 1948 / Kaneko–
Kurokawa–Wakayama 2002) — the simplest non-trivial q-zeta with
explicit values at negative integers.

The recursion `Σ_{k=0}^{n} C(n,k)·q^{k+1}·β_k^q - β_n^q = δ_{n,1}`
gives at substrate `q₀ ≈ 1.110`:

| n | β_n^q at q₀ | B_n classical | ratio |
|---|-------------|---------------|-------|
| 0 | 1.0000 | 1.0000 | 1.0000 |
| 1 | -0.4739 | -0.5000 | 0.9479 |
| 2 | 0.1574 | 0.1667 | 0.9444 |
| 3 | -0.0078 | 0.0000 | n/a |
| 4 | -0.0274 | -0.0333 | **0.8234** |

Note β_3^q ≠ 0 at substrate (classical Bernoulli B_3 = 0 because
odd Bernoulli numbers vanish for n ≥ 3; the q-deformation breaks
this).

Casimir-prefactor candidates `|val| · π²/6` (the standard geometric
multiplier that converts `ζ(-3) = -1/120` to `π²/720`):

| Form | Value | Rel residue |
|------|-------|-------------|
| `ζ_q(-3) = -β_4^q / [4]_q` | 1.099e-2 | 19.9% |
| `ζ_q(-3)_alt = -β_4^q / 4` | 1.129e-2 | **17.7%** |
| `β_4^q / [2]_q²` | 1.116e-2 | 18.6% |
| `β_4^q · [2]_q / [4]_q` | 2.209e-2 | 61.2% |

Best Carlitz candidate is 17.7% off — much worse than the
Mohideen–Roy 1998 experimental tolerance (~1%). **Carlitz q-Bernoulli
is the wrong q-deformation for the QOU Casimir analogue.**

**Implication.** If the QOU conjecture is correct (substrate
predicts Casimir matches standard physics at ~1%), then the q-zeta
relevant to QOU is *not* Carlitz/KKW. Two possible follow-ups:

(a) **Cherednik 2006 q-zeta** via Macdonald operators — the
    machinery is heavier but more naturally aligned with Hecke-
    algebra substrate. Predicted q-Bernoulli numbers differ from
    Carlitz at higher orders.

(b) **Non-q-zeta route entirely** — the QOU prefactor may come
    from a Markov-trace identity or a Φ_q (Faddeev) evaluation
    rather than a q-zeta. The fact that all "obvious" q-zetas
    fail at 17%+ is evidence the right derivation is *not*
    through this family.

Witness:
[`casimir-carlitz-q-bernoulli-probe.witness.json`](../../folio-assistant/computations/casimir-carlitz-q-bernoulli-probe.witness.json).

If the prefactor IS substrate-derivable, the derivation must
involve a more elaborate structure (Macdonald operators / Cherednik
q-zeta / Φ_q Faddeev dilog evaluation), not a closed-form
substitution in already-known q-rationals.

## Route B — Hoefsmit additivity on plate-bounded links (sub-problem 1)

**Sketch.** The Hoefsmit scattering pipeline
([`prop:hoefsmit-scattering-pipeline`](../../content/quantum-observable-universe/appendix-surreals/hoefsmit-bridge.md))
assigns to each link `L` a geometric energy `Geom(L) ∈ ℝ`. Under
the ε-relaxed vacuum axiom
([`prop:vacuum-epsilon`](../../content/quantum-observable-universe/appendix-surreals/vacuum-epsilon.md)),
the unknot contributes `Geom(⊙) = ε`. If `Geom` is **additive on
disjoint unions**:

```
  Geom(L₁ ⊔ L₂) = Geom(L₁) + Geom(L₂)
```

then any link `L = L_test ⊔ (N copies of ⊙)` has
`Geom(L) = Geom(L_test) + N · ε`. Multiplying the conjectural
plate-mode-count `N(A, d) ~ ε⁻¹ · A/d³` then gives the desired
finite contribution `A/d³ · (constant)` after taking the standard-
part — *modulo verifying Hoefsmit additivity*.

### Empirical probe — additivity established structurally

[`casimir-hoefsmit-additivity-probe.witness.json`](../../folio-assistant/computations/casimir-hoefsmit-additivity-probe.witness.json)
records:

1. **Hyperbolic-volume additivity.** Vol is additive on disjoint
   unions of hyperbolic 3-manifolds (Thurston; well-known).
   Verified on pairs `{⊙, 4_1, 𝓑₃}` symbolically.
2. **Geom under ε-relaxation.** Vol(⊙) → ε, so
   `Geom_ε(N · ⊙) = N · ε / ℏ_q² · linking_weight(N · ⊙)`.
   For disjoint unknots, `linking_weight = 1` (no mutual linking),
   giving `Geom_ε(N · ⊙) = N · ε / ℏ_q²`.

   At substrate `q₀`: `ℏ_q² ≈ 0.00982`, so the real-part coefficient
   is `1/ℏ_q² ≈ 101.86`. `Geom_ε(N · ⊙) ≈ 101.86 · N · ε`.

### Refinement to the conjecture — ε-scaling birthday rank

The probe surfaced a **structural correction** to the conjecture
.md:

The narrative postulated `N⊙(A, d) ~ ε⁻¹ · A/d³` (birthday rank 1
in surreal-infinitesimal units). But the `Geom_full = Vol/ℏ_q²`
normalisation absorbs an extra factor: at the energy-density
level, matching `u(d)/A = -π²/(720 d³) · ℏc` requires

```
  N⊙(A, d) ~ ε⁻¹ · A · ℏ_q² · ℏc · (-π²/720) / d³
```

— i.e. the **prefactor** picks up an `ℏ_q²` factor that does not
appear in the conjecture's current statement. At substrate
`ℏ_q²(q₀) ≈ 0.00982`, this would predict a *suppression* of the
naive Casimir scale by two orders of magnitude — which obviously
disagrees with the textbook experimental scale.

**Two interpretations:**

(a) The conjecture's narrative scaling is correct and the
    `Geom_full = Vol/ℏ_q²` normalisation does NOT apply to the
    plate-bounded unknot count (the `/ℏ_q²` is an artifact of the
    *baryonic* Geom calculation, specific to Borromean-style
    linked configurations; disjoint unknots may use a different
    `linking_weight` or normalisation altogether).
(b) The conjecture's narrative scaling is wrong and the actual
    birthday rank involves an additional `ℏ_q²` factor that
    cancels against something else upstream (e.g., the `Vol(⊙) =
    ε` value might itself be `ε · ℏ_q²` under closer inspection).

This is a concrete follow-up question for the next agent. The
probe records this explicitly as the `dimensional_consistency_check`
data field. The conjecture .md should be updated to flag this
once the resolution is known.

### Honest reading

Route B partially closes sub-problem 1: the structural ingredient
("Geom is additive on disjoint unknots, and `linking_weight(N · ⊙)
= 1`") IS in place. What remains is:

- **The categorical bijection between plate boundary modes and
  unknot configurations.** Each EM-photon mode between plates
  (k_n = nπ/d) must map to a specific unknot in the QOU framework.
  This bijection is the actual content of the conjecture and is
  not yet constructed.
- **Resolution of the ε-scaling refinement above.**

## Route C — Functorial uniqueness (option 4e from the related Bohr-radius proposition)

**Sketch.** Same idea as
[`prop:bohr-radius-categorical`](../../content/quantum-observable-universe/observations/bohr-radius-categorical.md)
round 4 option 4e: prove that any q-smooth archimedean functor
`ρ_∞ : Ẑ[q] → ℝ` satisfying `ρ_∞|_{q=1} = standard QED Casimir`
must be the unique functor that reproduces `π² ℏc/(240 d⁴)` as the
force per area. This reduces the empirical input from "match the
textbook prefactor" to "match at one point", which is
philosophically equivalent to standard QED at `q = 1` but more
defensible structurally.

**Status.** Not pursued in this audit. Same caveat as the
Bohr-radius proposition: still appeals to standard physics at the
classical limit, so it's not a "fully internal QOU derivation" —
but it does narrow the appeal to a single matching condition.

## Why we did not pursue these in the paper

These routes are speculative — they identify *where* the proof
might land, not *what* the proof is. Including them in the
conjecture's `.md` would dilute the conjecture statement with
investigation noise. Per CLAUDE.md "Author notes vs. scholarly
prose" (§4d), this is exactly the kind of material that belongs
in an audit doc, not in the paper's narrative prose.

When (and if) any of routes A–C closes, the resulting derivation
belongs in a *new proposition* (or a refined conjecture), not as
an addendum to the original block.

## Summary (after extended probes)

| Route | Sub-problem | Empirical result | Status |
|---|---|---|---|
| A — q-deformed ζ | 3 (prefactor) | Closest candidate `2·π²/(720·[2]_q)` at 0.54% (structurally trivial); no other sub-1% match across ℏ_q², h_q², α_em-derived families. **Null result reinforced.** | Open; further work needs Cherednik q-zeta / Macdonald-operator infra |
| B — Hoefsmit additivity | 1 (existence) | Vol-additivity confirmed (Thurston); Geom_ε(N·⊙) = N·ε/ℏ_q² derived; surfaced **ε-scaling refinement** — birthday rank may need to be ε⁻² not ε⁻¹, OR the `linking_weight` for disjoint unknots differs from the Borromean case | Partially closed; bijection {plate modes ↔ unknots} still open |
| C — Functorial uniqueness | 1+3 | Not pursued; carries same caveat as `prop:bohr-radius-categorical` option 4e | Parked |

### Key new findings (this session)

1. **Hoefsmit Geom is additive on disjoint unknots** (Vol-additivity
   + linking_weight = 1 for disjoint components). Established by
   composing existing infrastructure with the ε-relaxed axiom.

2. **The conjecture .md's ε-scaling needs refinement.** The
   stated `N⊙ ~ ε⁻¹ · A/d³` does not consistently combine with the
   `Geom_full = Vol/ℏ_q²` normalisation at the energy-density
   level. Two possible resolutions; needs human judgement to
   choose.

3. **The π²/720 prefactor is not a trivial substrate q-rational.**
   Across ~150 candidate forms (q-integers, ℏ_q powers, α_em
   products), the best sub-1% match is `2·π²/(720·[2]_q)` at 0.54%
   — but this is structurally just the `q → 1` continuity. No
   non-trivial closed form found.

**Tractability ranking (revised after this session):**

1. **Resolve the ε-scaling refinement.** This is a paper-side
   judgement call: do we update the conjecture .md to use ε⁻², or
   do we argue that disjoint unknots get a different normalisation?
2. **Construct the {plate-modes ↔ unknots} bijection.** Hardest
   step; would close sub-problem 1 once chosen.
3. **Cherednik q-zeta investigation.** Heavy infrastructure but
   most likely route to a closed-form prefactor.

**Recommendation to next agent.** Resolve the ε-scaling refinement
first (it's a small judgement; current draft is internally
inconsistent at the energy-density level). Then attempt the
plate-mode bijection using existing photon = empty-knot conventions
in [`appendix-transfer-matrices/tm-knot-pairs`](../../content/quantum-observable-universe/appendix-transfer-matrices/tm-knot-pairs.md).
