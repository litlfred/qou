# α_EM per-loop fibre-level `rho`: its Hodge-side target exists concretely on `Jac(Bring)` — witnessed by the real j-invariants (Braden–Northover real structure)

**Date:** 2026-07-18 · **Axis:** α_EM per-loop measure (fibre-level correspondence) ·
**Tier:** exact arithmetic (scope-(a) — concrete grounding; convergent with sibling
B1–B5; does NOT close the wall) · **Discipline:** no fit, nothing wired, `1/(8π)`
stays a phase-4 identification.

## Context — the fibre-level correspondence, and this concrete leg

After #3941/#3949 sharpened the per-loop `2`-unification to a *type* obstruction
(the Hecke channel-swap `q↦−q⁻¹` is ℂ-linear/holomorphic; Hodge conjugation is
ℂ-anti-linear), the sibling fibre-reality-structure chain (bean `qou-b5qg`,
B1–B5) resolved it abstractly: the anti-holomorphic ingredient is the **fibre
parameter-conjugation** `rho: q ↦ conj(q)` (`rho ↔ τ ↦ −conj(τ)`, the Hodge type —
no obstruction), the `1/2` is `rho`-forced conditionally (B4b), and a conditional
per-loop Lean theorem is stated shadow-sorry-free (B5). The single remaining lift
is **B2**: the functorial identity `τ(rho) = Hodge conjugation`.

This audit grounds **B2's target** — the Hodge conjugation on `Jac(Bring)` — on the
concrete genus-4 Bring arithmetic, using the newly-registered period-matrix
literature (`[riera-rodriguez-1992]`, `[braden-northover-2012]`, `library/` intake;
registered this PR).

## Result (exact rational arithmetic)

`Jac(Bring) ~ E_{5τ₀}³ × E_τ₀` (the isogeny diagonalising the period matrix
`Z = τ₀·C` to `(5τ, 5τ, 5τ, τ)`), with the two j-invariants (Braden–Northover
convention):

```
j(τ₀)  = −5·29³/2⁵ = −121945/32   (REAL rational)
j(5τ₀) = −25/2                    (REAL rational)
```

**Key fact:** a **real** j-invariant ⟹ the elliptic curve has a model over `ℝ` ⟹
it admits an **anti-holomorphic involution** (a real structure). Both factors of
`Jac(Bring)` have real j, so `Jac(Bring)` carries an anti-holomorphic involution —
precisely the one **Braden–Northover 2012 construct explicitly** (real structure +
Hilbert ovals + Vector of Riemann Constants).

So B2's target (the Hodge conjugation `rho` must map to) is **not abstract**: it is
the explicit Braden–Northover involution, and its **existence is witnessed by the
reality of the j-invariants** — an arithmetic fact on the actual Bring Jacobian, not
a type argument. Consistency with #3949 is preserved: the channel-swap `q↦−q⁻¹` is
ℂ-linear (holomorphic) and is **not** this involution; `rho` (anti-holomorphic) is.

## What this does and does NOT establish

- **DOES:** verifies both Bring elliptic j-invariants are real (rational); concludes
  each factor — hence `Jac(Bring)` — admits an anti-holomorphic involution;
  identifies it with Braden–Northover's explicit real structure = the concrete
  target of the sibling's `rho`; confirms the #3949 type-split.
- **DOES NOT:** prove the functorial identity `τ(rho) = Hodge conjugation` (that is
  the sibling's open **B2**), derive any α_EM clause, or close the wall. It supplies
  the concrete *existence* and *literature realisation* of `rho`'s target.

## Coordination

Convergent with — not a duplicate of — the sibling `qou-b5qg` B1–B5 chain: they
build the abstract `rho`-dictionary and the conditional assembly; this grounds B2's
geometric target on explicit Bring period data + the two newly-registered papers.
Two independent routes to the same object strengthen it.

## Scope discipline (anti-laundering)

Exact rational arithmetic; no CODATA read; no convention tuned toward `8π`; the
j-values are the registered literature values (Braden–Northover); the functorial
identity is left OPEN (sibling B2). No `α_k` wired; no fit; no tier change.

## Cross-references

- Registered sources (this PR): `[riera-rodriguez-1992]`, `[braden-northover-2012]`, `[braden-disney-hogg-2022]` in `content/schema/references.ts`
- Keystone doc (tool-block removed by these papers): [`2026-06-24-keystone-bring-jacobian-E4-elliptic-W-plane.md`](2026-06-24-keystone-bring-jacobian-E4-elliptic-W-plane.md)
- The `2`-type obstruction this grounds the resolution of: [`2026-07-18-alpha-em-involution-type-nome-independent.md`](2026-07-18-alpha-em-involution-type-nome-independent.md) (#3949)
- Sibling fibre-reality-structure chain: [`2026-07-18-alpha-em-b1-fibre-reality-structure.md`](2026-07-18-alpha-em-b1-fibre-reality-structure.md) (bean `qou-b5qg`, B1–B5)
- Probe + witness: [`../../computations/alpha_em/alpha_em_bring_real_structure_probe.py`](../../computations/alpha_em/alpha_em_bring_real_structure_probe.py), `computations/alpha_em/alpha-em-bring-real-structure.witness.json`
- Ledger: [`../coordination/alpha-em.md`](../coordination/alpha-em.md)
