---
# qou-ck0g
title: 'INFRA: q-deformed Jucys-Murphy family L_k in H_n(q) + seminormal eigenvalues'
status: todo
type: task
priority: high
created_at: 2026-08-10T19:02:23Z
updated_at: 2026-08-10T19:02:23Z
---


## Why

`qou-8vt2` needs the per-mode rates `μ_λ(q)` of the q-heat kernel over the Hecke
modules. Everything upstream of them is now forced (owner ruling on
`ℤ[q^{±1/2}]`, the bar-parity law, the refutation of the `Σ q^c` convention), and
everything downstream is proved (the depth-1 Jackson kernel and two-mode depth-2
composition in `QOU/BraidKnot/QBetaPreArchHeatDepthOneKernel.lean`, sorry-free
over a generic `[CommRing R]`).

The rates are the missing link, and they cannot be read off the corpus: searched
the whole Hecke + Schur–Weyl tree, including today's `SW-1..SW-9` landings, and
there is **no q-deformed central element, no q-Casimir, and no q-JM family**. The
only Jucys–Murphy present is `JucysMurphy.lean:123`, over
`MonoidAlgebra k (Equiv.Perm (Fin n))` — the classical `S_n` one.

**This is a formalisation task, not research.** It is standard material.

## What is needed

1. The family `L_1, …, L_n ∈ H_n(q)` (q-deformed Jucys–Murphy / Murphy elements).
2. Their action on the seminormal basis: eigenvalue `q^{2c}` on the vector
   indexed by a standard tableau, `c` the content of the cell holding `k`.
   **Cite the convention** — it is not currently stated anywhere in this corpus,
   and conventions differ by `q ↔ q²` and by sign across the literature.
3. Commutativity, and that symmetric functions of the `L_k` are central.
4. The bar-symmetrised sum `Σ_k (L_k + L_k⁻¹)`, whose block eigenvalue is
   `Σ_{c∈λ} (q^{2c} + q^{−2c})` — the bar-even ("cosh") form `qou-8vt2` requires.

Refs to use: Dipper–James (Hecke algebras of type A), Murphy (the JM basis), Ram
(seminormal / Hoefsmit forms). Every `sorry` gets a `-- Ref:` per AGENTS.md §1.

## Substrate

Build on `QOU/SchurWeyl/HoefsmitRep.lean` (SW-4, seminormal reps — 1-dim and the
(2,1) 2×2 braid sorry-free; general-λ is a Ref'd gap) and
`QOU/SchurWeyl/HeckeAlgebra.lean` (SW-1, `H_n(q)` + universal property,
sorry-free). Both landed 2026-08-10. Coordinate with the `qou-59vq` SW epic
before starting — this is plausibly SW-10 rather than a separate lane.

## Base ring

Keep it generic: `{R : Type*} [CommRing R]` with `q : R` (§7c). No `ℝ` — nothing
here is archimedean. Note `qou-8vt2` needs `q^{±1/2}`, so the eventual rate lives
over a ring where that exists; the JM family itself does not need it.

## One free identity, already checked

`q^{2c} + q^{−2c} = (q − q⁻¹)²·[c]_q² + 2` per cell, hence over λ with `n` cells

    Σ_{c∈λ} (q^{2c} + q^{−2c}) = (q − q⁻¹)²·Σ_{c∈λ} [c]_q² + 2n

Verified symbolically. One line in Lean, and it is what shows the two candidate
bar-even brackets are the same object up to a bar-even scalar and a
λ-independent shift.
