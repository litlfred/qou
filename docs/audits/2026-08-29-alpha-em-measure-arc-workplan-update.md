# α_EM per-loop-measure arc — work-plan update (2026-08-29)

**Purpose.** My mid-July α_EM per-loop-measure arc (`1/(8π) = 1/(π·b₁)`) is ~6
weeks and tens of thousands of commits stale. This re-baselines it against
current `main` (tip `914a13857e`) and records **one observation the corpus is
missing**. It is a plan-currency + single-observation note, **not** progress on
the wall. Nothing wired; `1/(8π)` stays phase-4 (2026-07-19 owner ruling).

## Current state of the measure (unchanged in substance since 2026-08-02)

`1/(8π)` is **OPEN, phase-4, owner-gated.** The July reduction (F-construction
T1–T5, R1 closed) left a single open item **R2**; the owner ruled R2 **not
Lean/derived-proved** (2026-07-19,
[`2026-07-19-alpha-em-r2-owner-ruling.md`](2026-07-19-alpha-em-r2-owner-ruling.md)),
canonization declined. The 2026-08-02 refactor **renamed and re-localized** R2 —
it did not close it:

> R2  →  B2 τ-lift  →  **MOC / Φ**: the holomorphic period map
> `Φ: q ↦ H¹(E_{τ(q)}) ⊂ H¹(Bring)` — *the framework's foundational open bridge,
> the same object as the E(q) genus-1 Gauss–Manin keystone (epic `08a2`)*.

[`2026-08-02-moc-gauss-manin-not-derivable.md`](2026-08-02-moc-gauss-manin-not-derivable.md)
proves Φ is **not derivable from the E⁴ model** even in the rank-2 genus-1
reduction; it is an irreducible categorical→archimedean input, multi-week infra.

**Program value: low.** The measure is a *last correction* (the α_EM tower still
misses CODATA by −8.4 ppm with A+B derived); it is **not** on the current ranked
L2 lever list
([`2026-08-02-1ppq-lever-map-post-q0-gate.md`](../coordination/2026-08-02-1ppq-lever-map-post-q0-gate.md);
the movers are Δ_λ/deuteron, Option-E A=3, absolute binding via non-q₀ routes).
L2 scoreboard: **1/5 scoreable beats 100×** (m_K/m_π only).

## The precise obstruction, and the one observation the corpus is missing

The MOC wall is stated sharply on main: the discrete `q = i` shadow (the
F-construction / Burau-at-i cover-monodromy) **fixes one point value of Φ and
supplies no germ** — the discrete-shadow → continuous-map gap *is* the wall
([`2026-08-02-hodge-lift-bring-h1-model.md` §line 72],
[`…-moc-gauss-manin-not-derivable.md` §line 28]).

**Missing from the corpus (recorded here):** the two "non-abelian" routes differ
*exactly on the germ*.

- **F-construction (cover-monodromy):** Burau monodromy evaluated at the discrete
  point `q_H = i` (→ Burau integral point `q_B = −1`). A **point value; no germ**
  — this is precisely the MOC obstruction.
- **Yekutieli non-abelian Stokes holonomy** (the canonical chain step-3 object
  the owner steered toward, 2026-07-19): `Hol_γ(q) = ∏ σᵢ(q)` is a **germ in `q`
  by construction** (each `σᵢ(q)` is Laurent-polynomial-valued, so the
  path-ordered product is q-analytic; the germ is `∂_q Hol` via Leibniz). It is
  the object that *supplies* what the abelian period map lacks.

So the owner's non-abelian-Stokes steer is **not** the F-construction: it is the
route whose germ exists by construction. This distinction is the single new
content of this note.

## But: germ-existing ≠ germ-useful (the binding-side warning)

A live caution from the binding arc, which used exactly this germ:
[`2026-08-09-nastokes-gauge-fixing-germ-root-vector.md`](2026-08-09-nastokes-gauge-fixing-germ-root-vector.md)
(PR #4848) defines `δqᵢ = q·(∂_q σᵢ)·σᵢ⁻¹`, proves it an `Ad(ρ(σ₁))` root vector
— and finds the transverse pairing **vanishes identically on single-generator
words** (deuteron/trefoil): the germ *exists but is sterile* at order 2. That
sterility is a real risk signal for the measure route too, and must be tested
before any multi-week commitment.

## Retired sub-threads (do not re-walk)

- **Chowla–Selberg / CM periods** (my old AG-2): dead — `E = Bring/S₄` is
  **proved NOT CM** (`j(τ₀) = −121945/32` non-integral;
  [`2026-07-25-alpha-em-b2-cm-weierstrass-scale.md`](2026-07-25-alpha-em-b2-cm-weierstrass-scale.md) W1).
- **Flat-torus Maxwell measure** (bean `qou-0rzk`): scrapped 2026-07-18.
- **Abelian Hodge / Prym as the primary route** (my old AG-1/AG-4): the
  EM-Prym-is-an-elliptic-curve *result* survives (Lean `BringEllipticFactor`),
  but as a route it is the one that hit the no-germ wall and the owner
  de-prioritized it in favour of non-abelian Stokes.

## Plan — one bounded decision task, then hand off

1. **Germ-viability probe (bounded, formalize-first) — the one live task.**
   Test whether the EM-word holonomy germ `∂_q Hol_γ(q₀)` is **non-sterile and
   carries period-map direction** (does it move `H¹(E_{τ(q)})` inside
   `H¹(Bring)`), or whether it decouples like the binding-side transverse pairing.
   Outcome decides the lead **live or dead** cheaply, *without* committing to the
   multi-week Φ keystone. Bean below.
2. **θ-graph 2-loop** (`qou-i7rk`, still `todo`, 1.3σ): **stays gated** on the
   measure; no action until (1) resolves.
3. **If (1) is dead or the Φ setup needs the 08a2 infra:** stop — the measure is
   an owner-gated, low-program-value last-correction. Re-point capacity at the
   ranked Δ_λ/deuteron lever, or hand back to the owner.

**Honesty guardrails (unchanged):** no lift instance for the physical loop
weights; `1/(8π)` stays phase-4; all status language says "conditional on R2/Φ
(unproven identification)"; the germ distinction above is an *observation about
routes*, not a derivation of Φ.
