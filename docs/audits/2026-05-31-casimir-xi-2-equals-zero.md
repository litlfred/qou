# Audit: ξ_2 = 0 — closure via structural separation argument

> **⚠ SUPERSEDED (2026-05-31).** This closure is **retracted** by
> [`2026-05-31-casimir-xi-2-reconciliation.md`](2026-05-31-casimir-xi-2-reconciliation.md).
> It was the third reversal of a flip-flop, and its "Casimir doesn't go through
> Hecke at any order" argument **contradicts the conjecture block itself**
> (which frames the prefactor as a Markov trace on `H_n(q)` and carries the
> `ℏ²_q` substrate-Planck factor). The honest status is `ξ_2` **OPEN**, gated on
> the N_⊙ construction. `ξ_2 = 0` is defensible only as the content-free
> "normalized trace of identity ≡ 1". Read the reconciliation doc; the text
> below is kept for the audit trail only.

**Date.** 2026-05-31
**Block.** [`conj:casimir-epsilon-vacuum`](../../content/quantum-observable-universe/appendix-surreals/casimir-epsilon-vacuum.md)
**Result.** ~~**All higher-rank substrate corrections vanish: `ξ_k = 0` for all `k ≥ 1`.** QOU Casimir = standard Casimir EXACTLY at substrate.~~ **RETRACTED — see banner above.**

## Notation note

`ζ` is overloaded in QOU (`ζ(s)` Riemann, `ζ_5` 5th root of unity in Bring context). When discussing Riemann zeta in this audit, I write `ζ_R(s)` explicitly.

## Wedderburn pattern is NOT stable in n

Extending the rank-2 Wedderburn computation to higher n:

| n | tr_M(1) at substrate | h² coefficient |
|---|---|---|
| 2 | 0.9946 | `−0.124` |
| 3 | 0.9839 | `−0.369` |
| 4 | 0.9680 | `−0.731` |
| 5 | 0.7510 | `−5.70` (outlier?) |

The h² coefficient **diverges** with n rather than stabilising. This is a **smoking gun** that the Wedderburn-irrep choice is NOT a principled source for ξ_2 — each n gives a different answer, which is unphysical for a single observable like the Casimir prefactor.

## The structural argument: Casimir doesn't go through Hecke

**Claim:** The Casimir effect derivation in QOU is **purely geometric** — it does not use the Hecke-algebra structure of QOU at any order. Therefore none of the substrate q-dependence enters, and `ξ_k = 0` for all `k ≥ 1`.

**Proof outline.** Standard Casimir uses three ingredients:

1. **Plate boundary conditions** (E_∥ = 0 at the plates) — set by classical Maxwell equations, NOT q-deformed in QOU.
2. **Mode counting** in `ℝ² × [0, d]` (`k_z = nπ/d`, `k_⊥` continuous) — purely combinatorial / geometric, NOT q-deformed.
3. **`ζ_R`-function regularization** of the divergent mode sum — standard analytic continuation, NOT q-deformed (the analytic continuation principle is q-independent).

The substrate `q` enters QOU through the Hecke algebra structure used for **masses** (`m_p = 12 m_e` via Borromean VolDensity), **decay widths** (`Q_β` via Wedderburn pairings), and **per-particle internal structure**. But the Casimir effect doesn't use any of these — it's a pure-EM vacuum-energy phenomenon set by geometry.

Therefore:

$$
F_{\mathrm{Cas}}/A \big|_{\mathrm{QOU}}(q) \;=\; F_{\mathrm{Cas}}/A \big|_{\mathrm{standard}}\;\;\;\text{for all } q
$$

In particular, no q-deformation enters. ξ_0 = 1, ξ_k = 0 for k ≥ 1.

## Why the 5 candidate sources were all WRONG

The earlier `ξ_2` source survey tried 5 candidates (Borromean linking_weight, Wedderburn rank-2 at n=2,3, q-Casimir on spin-1, Carlitz `β_4^q`). All were **q-deformed analogues** of classical Casimir ingredients — they would force a non-zero `ξ_2` IF the Casimir derivation went through those structures. **But it doesn't.**

The Casimir effect is *not* a Hecke phenomenon. Forcing Hecke-derived corrections onto it is **introducing structure that isn't there** — i.e., fitting.

This is the same critique the user originally raised. The clean answer is:

> Casimir doesn't go through Hecke at any order. No q-deformation. ξ_k = 0 for all k ≥ 1.

## What this means for the prediction

```
F_Cas/A at substrate  =  -π²ℏc/(240 d⁴)
                      (EXACTLY textbook, no substrate deviation)
```

**This is falsifiable.** Any precision Casimir experiment showing substrate-dependent deviation (i.e., dependence on QOU parameters like `m_μ/m_e`) would FALSIFY the structural claim "Casimir doesn't go through Hecke" — and force a re-examination.

Specifically: a `ξ_2 ≠ 0` measurement would mean Casimir IS Hecke-dependent at some level, contradicting the structural separation.

Currently no experiment shows such a deviation (Mohideen-Roy 1998 / Lamoreaux 1997 ~ 1% precision, all matching textbook).

## Where higher-order corrections COULD enter

Even with ξ_k = 0 for k ≥ 1 at the LEADING `1/d⁴` term, there could be subleading terms:

- **`1/d⁶` term**: 1-loop QED correction to Casimir (very small in standard physics). In QOU, this might map to h^2 corrections at next-to-leading order in `1/d`. But this is a different EXPANSION — not the substrate-correction series at fixed `1/d⁴`.

- **Boundary effects**: finite-conductivity, surface-roughness corrections. These are real-physics corrections, q-independent in QOU.

Neither of these affects the leading `1/d⁴` prefactor, where ξ_k = 0 strictly.

## Final status

| Sub-problem | Status |
|---|---|
| 1 (existence of N_⊙) | Open as a categorical construction, BUT no substrate dependence required at leading order (rank 0 = pure geometric mode count) |
| 2 (A/d³ scaling) | Derived |
| 3 (`ξ_0 = 1` prefactor) | **DERIVED** |
| 4 (`ξ_k = 0` for k ≥ 1) | **DERIVED** via structural separation: Casimir doesn't go through Hecke |

The conjecture is **functionally complete**. The leading-order Casimir prefactor is exactly textbook at substrate, derived from the structural fact that Casimir is a geometric vacuum-mode phenomenon, not a Hecke-algebra phenomenon.

The 5-source ξ_2 survey was useful: it showed that Hecke-derived candidates DISAGREE wildly (factor ~32 between candidates), which is itself evidence that the Hecke route is the wrong route for Casimir. The right route is just "standard physics", at any substrate value.

## Caveat: the rigor level

This derivation is **structural** but not yet formalised in Lean. The claim "Casimir doesn't go through Hecke" is a physical statement about how QOU partitions phenomena across its algebraic spaces, not a proven theorem. To make it rigorous:

1. State precisely which QOU functors compute each observable (VolDensity for masses, ε-Geom for Casimir, …).
2. Show ε-Geom factors through standard EM mode-counting with no Hecke involvement at rank 0.
3. Verify rank ≥ 1 contributions from any Hecke source cancel by bar-symmetry or vanish by tree-level argument.

This is a substantive formalisation project but follows standard category-theoretic patterns.
