# Capstone: the Δ_λ chirality sign is the principal (ρ) Z-grading at ζ₄ — a grading, not a twist

**Date:** 2026-07-11 · **Axis:** Δ_λ chirality-sign carrier (strong sector), closure ·
**Follows:** [`2026-07-11-deltalambda-sign-operator-narrowing.md`](2026-07-11-deltalambda-sign-operator-narrowing.md) (#3523) ·
**Tier:** symbolic-exact (parameter-free) · **No fit; nothing wired.**

## What this closes

Across the session the Δ_λ per-partition chirality sign was traced from "which knot?"
down to a single algebraic object. This audit closes the **sign-operator identification**:
the sign is the **principal (ρ) Z-grading**, evaluated at ζ₄ — an *external* grading of
the category, **not** an intrinsic ribbon/pivotal/Frobenius–Schur invariant of `V_λ`, and
not a twist.

Probe [`deltalambda_sign_pivotal_grading_capstone_probe.py`](../../computations/deltalambda/deltalambda_sign_pivotal_grading_capstone_probe.py)
→ [witness](../../computations/deltalambda/deltalambda-sign-pivotal-grading-capstone.witness.json) (5/5).

## The full elimination chain

`sgn(Δ_λ) = sgn(w₀^{S_{λ'}}) = (−1)^{n(λ)} = q^{2n(λ)}|_{q=i}` is **not**:

| candidate | why it fails | where |
|---|---|---|
| a knot's Markov character | raw T(2,5) sign mismatches 4/7 | #3509 (t25 probe) |
| a re-framing `χ·θ^{−w}` | `θ_λ > 0` at real q₀ ⇒ framing preserves sign | #3509 |
| a framing power (full/half twist) | graded by content sum `n(λ')−n(λ)`, not `n(λ)` | #3509 / #3523 |
| a low-degree JM central element | not a content power-sum polynomial (complete basis, deg ≤ 6) | #3523 |
| the **Frobenius–Schur indicator** | every S_n irrep is real ⇒ `ν₂ = +1` ∀λ; target is mixed | **this audit** |
| a **sgn-twist ratio** `θ_{λ'}/θ_λ` | `= i^{−4(n(λ')−n(λ))} = +1` ∀λ at ζ₄ | **this audit** |
| the **ribbon self-twist** `θ_λ` | content-graded, misses at ζ₄ | this audit |

**What it IS:** the principal specialization exponent `n(λ) = Σ_box row(box)`
(`s_λ(1,q,q²,…) = q^{n(λ)}·∏…`), a `q^{2ρ}`-type **principal (ρ) grading** — an external
`ℤ`-grading, distinct from the content grading `c = col − row` that framings and JM
elements see. The sign is not carried by the object's braiding/duality data at all.

## The clean characterization

`Δ_λ = sgn(w₀^{S_{λ'}})·dim(λ) = (q^{2n(λ)}|_{q=i})·dim(λ)` is a **ρ-graded dimension**:
the **sign** is the principal grading evaluated at ζ₄, and the **magnitude** is the
ordinary (ungraded) dimension of `V_λ`. This is coherent with the whole session's
fibre-vs-archimedean theme — the chirality is a categorical (root-of-unity, ρ-grading)
datum, structurally invisible to every real-q₀ braid-trace construction.

## Still open (Track A, gated)

The **magnitude** `|Δ_λ| = dim` as a *categorical closure* (a canonical construction
delivering the ungraded dimension in the binding formula) remains Track-A / Subgoal-2,
owner-gated. This audit closes the **sign** question and characterizes Δ_λ as a
ρ-graded dimension; it does not derive the magnitude and wires nothing.

## Cross-references

- Narrowing (prior): [`2026-07-11-deltalambda-sign-operator-narrowing.md`](2026-07-11-deltalambda-sign-operator-narrowing.md) (#3523)
- Locus: [`2026-07-11-gemini-session-c3-overclaim-continuum-and-lean-audit.md` §Findings 6–8](2026-07-11-gemini-session-c3-overclaim-continuum-and-lean-audit.md) (#3509)
- Selection-rule engine (on main): `QOU/SelectionRules.lean`
