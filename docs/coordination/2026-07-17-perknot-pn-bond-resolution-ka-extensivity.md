# Per-knot p≠n bond-resolution vs the k(A) extensivity gap (beans qou-cqqs / qou-r1sr)

**Date:** 2026-07-17 · **PR:** #3841 · **Base:** current `main` (`074dfccb4a`).

Coordination record for the λ_A per-knot salvage's two attacks on the single
open GAP-A-3/A-4 item — the **derived** k(A) extensivity multiplier
μ_ext(K) = B_AME/B_base (targets D 5.85, T 4.44, ³He 3.29, ⁴He 9.31;
non-monotone, "not fit-closable" for symmetric models;
`computations/deltalambda/deltalambda-extensivity-gap-synthesis.witness.json`).
Both attacks come from a **different context** than the active fronts
(deliberately, per owner steer — a fresh angle may find what a crowded front
misses); the outcomes are reported honestly against that mature state.

## What is already closed / mature on main (do not re-derive)

- **Magnitude base + sign CLOSED:** `|Δ_λ| = classical dim(λ)` (#3537), sign
  `(−1)^{n(λ)}` (g_ρ grading). B_base = m_e·|Σ y_λ χ^λ sgn·dim| is parameter-free.
- **Carrier is PROVED intensive:** `carrier-saturation-mechanism.witness.json`
  — via `prop:wedderburn-trace-identity` (Σ y_λ dim_λ = tr_M(1) = 1),
  S = E_p[|Δθ|] is a bounded mean (0.72–0.88 rad at all A). "The carrier was
  never extensive."
- **Level-selection NOT linear:** paper proposition
  `content/.../mass-theory/level-selection-not-linear.md` (§3b-cond).
- Active fronts: #3808 (mixed-interface 3-factor closure: envelope × A_light-amp
  × bar-parity fall), #3802 (A=4 binding-K PSD), deuteron-wall alien-resummation
  + Ursell-operator scoping (`docs/scope/2026-07-05-gap-a4-ursell-*`).

## Attack 1 — per-knot additive S(K) → μ_ext: **PRUNE** (bean qou-cqqs)

`computations/probes/perknot-additive-sk-vs-kA-extensivity.witness.json`.
The per-knot additive S(K) (PR #3205 verdict #5, the sole λ_A-artifact) is
uniform/compressed in A (spread ×1.14 vs μ_ext's ×2.83) and puts the deuteron
**smallest** (rank 4) where μ_ext has it 2nd; best real candidate Spearman
+0.40 does not beat the junk control (A itself, +0.32) at n=4. This is the
expected shadow of the **proved** carrier-saturation intensivity — a quantity
uniform in A cannot supply a non-monotone μ_ext. Scope-(a); not a structural
exclusion of tr_M in a richer operator-valued combiner.

## Attack 2 — per-knot p≠n bond-resolution → the T/³He split: **LEAD** (bean qou-r1sr)

`computations/deltalambda/perknot-pn-bond-resolved-extensivity.witness.json`.
The genuinely non-duplicative angle: **T=(p,n,n) and ³He=(p,p,n) have identical
A=3 and 3 bonds, yet μ_ext = 4.44 vs 3.29 (ratio 1.3501)** — a split every
symmetric/equal-weight bond model (main's `bond_extensivity_equal_weight.py`)
gives as exactly **1.000**. The p≠n-distinct traces resolve the pairs into
pp/pn/nn with distinct weights.

Result: the parameter-free **inverse-product** per-bond weight
`w(a,b) = 1/(tr_M(a)·tr_M(b))` under the product aggregate reproduces the split
to **−1.38%** (pred 1.3315). Under that aggregate the ratio reduces to
`w(nn)/w(pp)`, so the p≠n resolution supplies the sign+magnitude of the T≠³He
degeneracy-break — plausibly the same physics as #3808's bar-parity-fall factor.

**LEAD, not closure (honest bounds):**
- Does **not** reproduce the full non-monotone μ_ext: ⁴He is not the maximum;
  per-isotope magnitudes off by tens of %.
- 1 hit among ~8 screened weights with a binary direction choice — entropy
  caveat (PSLQ-bound discipline): a single <5% match is a lead to verify.
- **No categorical derivation of "why inverse"** — the open verification step.

## Grounding verdict — **GROUNDED (partial)** (2026-07-17, bean qou-r1sr)

`computations/deltalambda/perknot-pn-bond-mayer-grounding.witness.json`. The
"why inverse?" question is answered three ways (all 3 assertions pass):

1. **Structural reduction (exact).** T=(p,n,n) has bonds {pn,pn,nn}; ³He=(p,p,n)
   has {pp,pn,pn} — the *only* difference is one pp↔nn swap. Under the product
   aggregate the split reduces **exactly** to `w(nn)/w(pp) = (tr_p/tr_n)²`
   (verified rel_eps 1e-40). The exponent 2 is a same-type bond's two endpoints
   — not tuned.
2. **Categorical home.** `1/(tr_M(a)·tr_M(b))` is the ideal-gas / **Mayer
   normalization** of the pair correlation `g₂ = tr(ab)/(tr(a)tr(b)) − 1` — the
   **b₂ (pairwise) level** of the Ursell cluster expansion `B/m_e = Σ_k b_k`
   that main already uses (`docs/scope/2026-07-05-gap-a4-ursell-*`); `tr_M` is a
   Plancherel-weighted partition sum `Σ_λ y_λ χ_λ`. So the weight is *not* a
   free ansatz.
3. **Physics sign.** `tr_n < tr_p ⇒ w(nn) > w(pp) ⇒` nn binds more `⇒` ³He (two
   protons) less bound than T — the **correct Coulomb/isospin sign** (AME
   B(T)=8.482 > B(³He)=7.718 MeV), magnitude −1.38%.

**Net:** the lead upgrades from "1-of-8 numerology-adjacent" to a
**categorically-grounded p≠n isospin discriminator** (Mayer b₂ normalization,
correct Coulomb sign, −1.38%).

**Honest bound — orthogonal to the open gap.** This is a **b₂/pairwise** object,
and main's Ursell frame identifies pairwise b₂ as the **saturated ceiling**; the
open *magnitude* gap is the **connected b₄**. So this grounds the *isospin
discriminator* (the T/³He degeneracy-break) but does **not** address the
extensivity magnitude closure (it does not reproduce the full non-monotone
μ_ext; ⁴He is not the max). Anti-numerology flag: true exponent 2.097 ≈ 2.093
(the ⁴He super-pairwise excess) — recorded as a **coincidence, NOT fit** (Rule-14
hidden-DOF guardrail).

## Next (if pursued)

1. **Feed the discriminator, not the magnitude.** The natural consumer is a
   factor that already carries the p≠n / isospin split — #3808's bar-parity-fall
   (comment posted). If their factor derives the same (tr_p/tr_n)²-type split,
   this is a cross-confirmation; if it uses a free constant, the Mayer b₂
   normalization is a parameter-free candidate for it.
2. **Do not** promote to the magnitude gap — that is the connected b₄
   (`docs/scope/2026-07-05-gap-a4-ursell-operator-magnitude-scoping.md`),
   a different object; the b₂ ceiling is closed.
3. **Do not** widen to a free-coefficient bond fit or chase the 2.097≈2.093
   coincidence (adhb + Ursell-doc guardrails).
