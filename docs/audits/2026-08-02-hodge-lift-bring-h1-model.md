# B2 τ-lift: explicit H¹(Bring) Hodge model reduces the wall to one existence axiom (2026-08-02)

Branch `claude/q-deformed-saddle-offsets-bdn992`. Bean qou-l1je. Follows
`2026-08-02-alpha-em-perloop-clauses-obstruction.md` §Correction (the wall is the
functorial LIFT, not the holo/anti-holo mismatch). Compute:
`computations/alpha_em/hodge_lift_bring_model.py` (10/10 PASS, re-verified).

## Outcome

**The lift is NOT closed** — but the wall is **reduced to a single existence axiom**, and
two ingredients that looked open are **proved automatic**. Net: real infra progress; the
"obstruction" that started this exploration is dead; the residual is the framework's
foundational q↔period bridge.

## 1. Bring's Jacobian: ~ E⁴, and E is NOT CM (proved)

- Genus 4, `Aut = S₅`. `H^{1,0}` (dim 4) = the irreducible 4-dim **standard rep (4,1)**
  (discriminator `dim(std^{S₄})=1`, elliptic `Bring/S₄`, vs `std⊗sign` → genus 0). So
  `Jac(Bring)` is isotypic ⇒ isogenous to a power of one simple factor.
- `Jac(Bring) ~ E⁴`, `E` = conductor-50 class **50a**; as complex tori
  `Jac(Bring) ≅ E_{5τ₀}³ × E_{τ₀}` (Riera–Rodríguez / Braden–Northover), the two moduli
  `5`-isogenous (**X₀(5)**).
- **No CM (proved):** `j(τ₀) = −121945/32`, `j(5τ₀) = −25/2` are **non-integral**
  rationals; a CM `j` is an algebraic integer, so no factor has CM; `τ₀ = −½+0.18668i`
  satisfies no small imaginary-quadratic (searched A≤39). Matches the corpus's
  `2026-07-25-alpha-em-b2-cm-weierstrass-scale.md`. **The "CM periods close it" route is
  foreclosed at the premise.**

## 2. ρ ↔ Hodge conjugation is CANONICAL/automatic (the ex-obstruction is dead)

On the explicit 8-dim `H¹ = H^{1,0}⊕H^{0,1}` (basis `[dz₁…dz₄ | dz̄₁…dz̄₄]`):

| involution | matrix | linearity | swaps pieces | Fix |
|---|---|---|---|---|
| **Weil real structure `c`** (= B2's "Hodge conjugation") | `SWAP∘conj` | antilinear | yes | `H¹(ℝ)`, dim_ℝ 8 |
| Galois `F = σ*` | `SWAP` | ℂ-linear | yes | — |

- `c` is the anti-linear involution B2 names; `Fix(c) = H¹(ℝ)` is the canonical real form.
- **ρ (`q↦q̄`) ↦ `c`** and this identification is **canonical — `c = SWAP∘conj` for ANY
  moduli** (rebuilt for a different τ: identical). So "ρ ↔ Hodge conjugation" carries **no
  arithmetic content**; it is automatically true at the Hodge-structure level.
- The **anti-holo equivariance `τ(q̄) = −conj(τ(q))`** is **forced by the nome**
  `q=e^{2πiτ}` (verified identically, err 0.0).
- The earlier "holo channel-swap vs anti-holo Hodge" framing tripped on `F` (the ℂ-linear
  Galois structure); the B2 object is `c` (anti-linear), type-consistent as B1 established.
  **The obstruction is confirmed a non-issue.**

## 3. The minimal open core (MOC) — a single existence field

With the involution-match and the equivariance proved automatic, the two-field lift
collapses to one:

> **(MOC)** The categorical τ-functor produces a **holomorphic period map**
> `Φ: q ↦ H¹(E_{τ(q)}) ⊂ H¹(Bring)`, nome-normalized (`τ(q₀)=τ₀`), carrying the conformal
> Laplacian (B3) as a real self-adjoint weight.

This is **option (a) existence**, and **narrower than (b)**: the loop occupies a **rank-2
sub-object** `H¹(E_{τ(q)})`, so `Φ` need only land in *that factor's* period domain — not
be an isomorphism of the full 8-dim Hodge structure. Given (MOC), both fields of the
merged `TauRhoHodgeLift` class follow (equal-split + doubled-total, mirroring the merged
proved lemmas). Proposed Lean sharpening: a single-field class `PeriodMapWeight` from
which equal-split + doubled-total derive (mirroring the merged proved lemmas) — a
reduction proposal, not yet built, no instance fabricated.

## 4. Honest verdict: not closable from the model

The explicit E⁴ model pins the **codomain** completely (periods `τ₀·diag(5,5,5,1)`, the
real structure `c`, the X₀(5) isogeny — literature + partly Lean-locked). The open (MOC)
is the **domain→codomain map** `Φ` — exactly the categorical→archimedean **q↔period
dictionary**, the framework's foundational open bridge (same object as the keystone
`E(q)` genus-1 Gauss–Manin reduction; multi-week, not a fit). The `q=i` shadow is
Lean-proved forced but fixes a *point value*, supplying **no germ** of `Φ` — the
discrete-shadow → continuous-map gap is the genuine wall.

**Deepest point:** the lift is about *the map*; CM only ever pins *the target's values*.
So the absence of CM (proved) does not worsen it, and CM's presence would not have closed
it. This is a clean "conditional-proved ≠ premise-established": the class scaffold exists,
the premise (Φ) is not derived.

## Net

Real infra: the wall is now a **single existence axiom (MOC)**, with the
involution-match + nome-equivariance **proved automatic** and stripped from the open part
— and the exploration's holo/anti-holo "obstruction" is definitively a non-issue. What
remains is the foundational q↔period functor, which no brick yet supplies and which is not
a single-session close. Nothing here is CODATA/fit/wired; `1/(8π)` stays phase-4.
