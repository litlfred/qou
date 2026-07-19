# α_EM F-construction T1 — the cover structure (2026-07-19)

**Bean:** `qou-bi1u` (T1) of milestone `qou-a46k` — the F-construction plan
(archimedean τ-functor via cyclic-cover monodromy), opened after #4035
typed the target.

**Probe:** [`computations/alpha_em/alpha_em_f_t1_cover_structure_probe.py`](../../computations/alpha_em/alpha_em_f_t1_cover_structure_probe.py)
→ [`alpha-em-f-t1-cover-structure.witness.json`](../../computations/alpha_em/alpha-em-f-t1-cover-structure.witness.json)
— 4/4 PASS, exact integer/rational arithmetic.

**Literature grounding** (the owner's standing "from the lit?" test): the
route is a known species — braid/Hecke representations at roots of unity on
cyclic-cover cohomology, with the Hodge (anti-)unitary structure attached to
the deck character: Deligne–Mostow (Publ. IHES 63, 1986); McMullen, *Braid
groups and Hodge theory* (Math. Ann. 355, 2013); eigenspace dims by
Chevalley–Weil (1934). What stays honestly open is T5's residual: that the
*framework's* τ restricts to this functor.

**Scope guard (STRICT):** cover side only; F not yet constructed; weight
*values* not derived (T4); no fit; nothing wired; `1/(8π)` stays phase-4.

## Results

1. **Riemann–Hurwitz closure + selection.** For the degree-4 cyclic cover
   `Bring → E := Bring/⟨U⟩` (g 4 → 1): `Σ(e_p−1) = 6`, with ℤ₄ solutions
   (n₂,n₄) ∈ {(6,0),(3,1),(0,2)}. The #3942 carrier (two genuine fixed
   points V, W with derivative multipliers i, −i ⟺ total ramification)
   **selects (0,2)**: branched totally at exactly the two carrier vertices.
2. **The multiplier pair is derived.** The branch-cycle sum rule
   `a_V + a_W ≡ 0 (mod 4)` with both of order 4 forces `{a_V,a_W} = {1,3}` —
   deck derivatives (i, −i). The #3942 pair is now a *consequence* of the
   cover axioms, not an observation.
3. **Chevalley–Weil derives the (3,1).**
   `dim H^{1,0}_{χ^k} = g_E−1+⟨k·a_V/4⟩+⟨k·a_W/4⟩ = 1` for k = 1,2,3;
   invariant part = g_E = 1; total 4 = g_B. The isotypic split is
   **(moving, invariant) = (3, 1)** with zero adjustable input — moving ↔
   `E_{5τ₀}³`, invariant ↔ `E_{τ₀}` (pullback of H¹(E)), the
   `spec(M) = {5,5,5,1}` multiplicities. **Consistency-1 (#4019) is
   upgraded from a low-entropy match to a structural derivation.**
4. **The χ=i eigenline is 1-dimensional** — the geometric home of the
   forced B2 shadow (#3960): T2's Hecke module at q = i acts on this line
   and its conjugate.

## Plan state (milestone `qou-a46k`)

```
T1 cover structure        THIS — delivered
T2 monodromy Hecke module at q=i (Burau-at-i vs the Jordan block)   next
T3 ρ-equivariance theorem (CW conjugation)                          open
T4 weight transport (dims derived; VALUES (¾,¼) still to derive)    open
T5 assembly + residual identification (F = framework τ)             open
```
