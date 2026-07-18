# α_EM per-loop `2`: the unification obstruction is nome-independent — Hecke swap is ℂ-linear, Hodge conjugation is ℂ-anti-linear (caveat on #3941 removed)

**Date:** 2026-07-18 · **Axis:** α_EM per-loop measure (the single load-bearing wall) ·
**Tier:** exact algebra (scope-(a) — strengthens #3941; does NOT close the wall) ·
**Discipline:** no fit, nothing wired, `1/(8π)` stays a phase-4 identification.

## What this strengthens

#3941 showed that under the **standard nome** `q = e^{2πiτ}`, the Hecke
channel-swap `q ↦ −q⁻¹` (#3936) maps to the *holomorphic* modular involution
`τ ↦ ½ − τ`, distinct from the *anti-holomorphic* Hodge conjugation `τ ↦ −τ̄` —
but flagged the nome as a caveated choice. This audit **removes the caveat**: the
analytic-type mismatch is intrinsic to the two involutions, independent of any
nome, uniformizer, or coordinate.

## Result (exact `ℚ(q)` / ℂ algebra, machine-checked)

| involution | acts on `i` | type |
|---|---|---|
| Hecke channel-swap `q ↦ −q⁻¹` (#3936) | fixes `i` (`swap(i·x)=i·swap(x)`) | **ℂ-LINEAR** (holomorphic) |
| Hodge conjugation (fixes `H¹(M,ℝ)`, swaps `H^{1,0}↔H^{0,1}`) | negates `i` (`conj(i·w)=−i·conj(w)`) | **ℂ-ANTI-LINEAR** |

- `q ↦ −q⁻¹` is an **involutive automorphism** of `ℚ(q)` (a ring homomorphism:
  additive + multiplicative), hence ℂ-linear — it commutes with scalar
  multiplication by `i`. It is holomorphic in `q`.
- Complex conjugation is the anti-linear involution fixing the real structure
  `H¹(M,ℝ)`; it sends `i ↦ −i`.

A ℂ-linear involution and a ℂ-anti-linear involution act **oppositely** on `i·w`
and are therefore of different analytic **type**. No change of coordinate (nome,
uniformizer, modular parameter) converts one into the other — so the #3941
obstruction is **intrinsic**, not an artifact of `q = e^{2πiτ}`.

## What a unification would require (named, not derived)

A genuine identification of the Hecke `2` with the Hodge `2` needs an
**anti-linear real structure** `R` on the categorical fibre such that Hodge
conjugation factors through the Hecke swap:

```
conj  =  swap ∘ R,   equivalently   R := swap ∘ conj   (anti-linear).
```

`R = swap ∘ conj` is anti-linear (ℂ-linear ∘ ℂ-anti-linear = ℂ-anti-linear;
verified: `R(i·w) = −i·R(w)`). The existence of a compatible `R` on the fibre is
the precise open input the τ-functor must supply — this **names** the fibre-level
reality structure that #3936/#3941 pointed to. Whether such an `R` exists
compatibly with the substrate structure is the genuinely open research question;
it is not closed here.

## What this does and does NOT establish

- **DOES:** proves the linear-vs-anti-linear type mismatch exactly and
  nome-independently (removes #3941's caveat); names the required bridge as an
  anti-linear real structure `R = swap ∘ conj`.
- **DOES NOT:** derive the unification, exhibit `R`, or close the wall. It pins
  the open input to "a compatible anti-linear `R` on the fibre."

## Scope discipline (anti-laundering)

Exact algebra, machine-checked; no CODATA read; no nome assumed (the point is
nome-independence); the unification is stated OPEN. No `α_k` wired; no fit; no
tier change.

## Cross-references

- τ-correspondence (the nome-dependent form this strengthens): [`2026-07-18-alpha-em-tau-correspondence.md`](2026-07-18-alpha-em-tau-correspondence.md) (#3941)
- Channel-swap involution `q↦−q⁻¹`: [`2026-07-18-alpha-em-channel-swap-involution.md`](2026-07-18-alpha-em-channel-swap-involution.md) (#3936)
- Hodge doubling (`H^{1,0}↔H^{0,1}`): [`2026-07-18-alpha-em-multiplicity2-realcomplex-count.md`](2026-07-18-alpha-em-multiplicity2-realcomplex-count.md) (#3920)
- Cluster status consolidation: [`2026-07-18-alpha-em-perloop-measure-status-consolidation.md`](2026-07-18-alpha-em-perloop-measure-status-consolidation.md)
- Probe + witness: [`../../computations/alpha_em/alpha_em_involution_type_probe.py`](../../computations/alpha_em/alpha_em_involution_type_probe.py), `computations/alpha_em/alpha-em-involution-type.witness.json`
- Ledger: [`../coordination/alpha-em.md`](../coordination/alpha-em.md)
