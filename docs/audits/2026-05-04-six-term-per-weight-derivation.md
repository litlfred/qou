# 2026-05-04 — Per-Term Weights from the Derivation

## Question

Why does the 5-mode sweep on `paper_six_term_isotope_sweep`
(li2q tower mode, A ≤ 9 spectrum) give **14.7 % mean mass
error** when the standalone `li2q_six_term_probe` gives
**0.14 % mean error** — both using the same Li₂_q identity?

## Answer

The 6-term assembly in `paper_six_term_isotope_sweep` applies a
single proton-fitted E₀ as the multiplier for every term:

  M_pred = E₀ · (T1 + T2 + T3 + T4) + T5_factor + T6_MeV

But the paper's derivation specifies **different scales per term**.
The single-E₀ assembly mixes them, and proton-fitting only happens
to balance at A = 1; the error grows quickly with A.

## What the derivation actually says (per term)

### Term 1 — `|tr_M(T_w)|` (descended Markov trace)

Source: `prop:categorical-mass-markov`, `thm:jones-markov-trace`.
The descended Markov trace contributes to **binding**, not mass.
Its physical scale is the **β-decay Q value**:

  B(Z, N)_canon  =  E_0_β · ( |tr_M(W_free)| − |tr_M(W_atom)| )

with **E_0_β ≈ 0.782 MeV** (free-neutron β-decay Q,
`E_0_BETA_DECAY_MEV` in `canonical_plus_multibrane.py`).

So T1's "weight" is **0.782 MeV per cat unit**, but only the
*difference* `|tr_free| − |tr_atom|` enters the mass formula.
Adding `E_0_β · T1_atom` directly to a mass prediction is
double-counting against the constituent baseline.

### Term 2, Term 3 — brane tower

Source: `prop:atomic-braid-mass` + `prop:binding-scale-catalan`.
The paper's atomic mass formula is:

  M(Z, N)  =  Z·m_p + N·m_n + Z·m_e  +  α · Σ_i ln|V̂_i^full|

with **α = m_e · 8G ≈ 3.7445 MeV** (Borromean hyperbolic volume
× electron mass; `prop:binding-scale-catalan`).  The audit branch
(`841cab890`) reconciles: α·ln|V| is the leading-order expansion
of -α·Li₂_q(-|V|).  So in li2q form:

  T2 weight: **α ≈ 3.7445 MeV per cat unit** (single-tower)
  T3 weight: **α ≈ 3.7445 MeV per cat unit** (pair-tower, with z² factor inside)

### Term 4 — Frobenius co-Casimir `m_e · τ(C_dim_q)`

Source: `thm:frobenius-codim-universal`.  The factor m_e is
**already inside** the term; T4 is dimensionful **MeV** as written.

  T4 weight: **1** (no additional multiplier)

### Term 5 — chirality factor `a_K · C_K`

Source: `prop:chirality-dual-space-derivation`.  a_K is the
Wedderburn deviation `∏_pn (1 + sign·h)`; C_K is the chirality
content invariant.  Per the doc this is a **multiplicative**
correction on T1, not an additive one:

  M  =  M_free  +  α · (T2 + T3)  +  T4  +  ( T5_factor − 1 ) · T1
                                                          ^^^^^^
                                                multiplicative

That's the convention in `paper_six_term_isotope_sweep.py` for
`term5_mode = "additive"`.

  T5 weight: **multiplicative on T1** (additive equivalent =
  (a_K·C_K − 1) · T1)

### Term 6 — cyclotomic residue tail

Source: `prop:gb-residue-spectral-sum`, `prop:full-pole-structure-mass-trace`.
Per the audit branch's `_load_canonical_t6_MeV` helper, T6 is
loaded from the Habiro residue witness **already in MeV**:

  T6 weight: **1** (already MeV)

## Corrected assembly

Summing the per-term scales:

```
B(Z, N) = E_0_β · (|tr_M(W_free)| − |tr_M(W_atom)|)         ← T1 (binding component)
        + α · ( T2_atom − T2_free )                         ← T2 (li2q form)
        + α · ( T3_atom − T3_free )                         ← T3 (li2q form, with z²)
        + T4_atom_MeV − T4_free_MeV                         ← T4
        + ( a_K − 1 ) · T1_atom · E_0_β                     ← T5 (chirality)
        + T6_atom_MeV − T6_free_MeV                         ← T6 (cyclotomic)
```

Crucially, **α ≠ E_0_β**.  Their ratio is α / E_0_β = 3.7445 /
0.782 ≈ **4.79×**.  The 6-term assembly's single-E₀ convention
under-weights T2/T3 by exactly this factor on the binding piece
(or over-weights T1 by it, depending on which way you read it).

## Empirical check against the audit branch's standalone

`li2q_six_term_probe.predict_atom_three_forms` uses:

```python
correction_li2q = α · Σ -Li_2^q(-|V_i|)        # T2 only, with α weight
M_li2q          = constituent − correction_li2q
```

This omits T1, T3, T4, T5, T6 entirely — yet gives 0.14 % mean
mass error.  The implication: at leading order, T1+T3+T4+T5+T6
are **small corrections** on top of T2, and the simple form
recovers most of the physics.

The 6-term assembly's 14.7 % error in the same spectrum suggests
the *additional* terms (T1 with E_0_β, T3 with z² multiplier on α,
T4 in MeV, T5 multiplicative, T6 in MeV) are being mis-combined
when pushed through the single-E₀-fits-proton calibration.

## Recommendation for `paper_six_term_isotope_sweep`

Replace the single-E_0 calibration:

```python
# BEFORE (current):
total = (T1 + T2 + T3 + T4)
M_pred = E_0_calib · total + T5_factor_terms + T6_MeV

# AFTER (proposed):
binding_T1 = E_0_β · (T1_free − T1_atom)
binding_T23 = α · (T2_atom − T2_free + T3_atom − T3_free)  # li2q gives positive sum
binding_T4 = T4_atom_MeV − T4_free_MeV
binding_T5 = (a_K − 1) · T1_atom · E_0_β
binding_T6 = T6_atom_MeV − T6_free_MeV
B_pred = binding_T1 + binding_T23 + binding_T4 + binding_T5 + binding_T6
M_pred = constituent − B_pred
```

with hardcoded **E_0_β = 0.782 MeV** (β-decay Q) and
**α = m_e · 8G ≈ 3.7445 MeV** (Borromean volume × m_e).
Both constants come from the derivation, not from proton-fitting.

## Open question

Whether T2/T3 should both carry the α weight, or only T2 (with T3
contributing higher-order via z² ≈ 0.249 dampening), depends on
the precise form of `prop:mass-endomorphism-tower`'s expansion.
The audit branch's `li2q_six_term_probe.py` only uses T2 and gets
0.14 % — so empirically T3 may already be small enough that the
T3 contribution is sub-percent regardless of weight.

A clean test: run the sweep with the corrected per-term weights
and compare to the 0.14 % standalone benchmark.  If it matches,
the weights are right; if it overshoots, T3 is double-counting.
