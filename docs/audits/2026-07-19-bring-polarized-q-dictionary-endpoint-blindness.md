# 2026-07-19 — Endpoint-anchored q-dictionaries are polarization-blind (α_EM magnitude leg)

**Script**: [`computations/alpha_em/bring_polarized_q_dictionary_endpoint_blindness_probe.py`](../../computations/alpha_em/bring_polarized_q_dictionary_endpoint_blindness_probe.py)
**Witness**: `computations/alpha_em/bring-polarized-q-dictionary-endpoint-blindness.witness.json`
**Builds on**: [#4043](https://github.com/litlfred/qou/pull/4043) (polarized/product genus-4
measures + FP machinery, merged), the tranche-5 endpoint-only prune
(`alpha_em_period_qdeformation_probe.py`), and the per-loop arc's
"irreducibly categorical" verdict (#4030 + `TauFunctorTargetSpec`).

## The question

After #4043 the natural next step on the magnitude leg looked like a
**q-deformation of the polarized determinant** (the "q-holomorphic det"
suggestion): replace the classical modular building blocks by fibre-level
q-deformed ones and evaluate at the substrate. Before running any such scan,
formalize-first discipline requires asking what invariant the whole method
class must satisfy.

## The result (symbolic-exact, numerically confirmed)

Per the tranche-5 prune, a period-side q-dictionary carries
dictionary-independent content **only at its asymptotic endpoints** (interior
matching of monotone families under a free reparameterization is vacuous).
Both endpoints are **identical** for the principally polarized period τ₀·M and
the product period τ₀·diag(5,5,5,1):

- **t → 0**: Jacobi inversion gives θ_H(t) = t^{−n/2} det(H)^{−1/2} θ_{H⁻¹}(1/t),
  so θ ~ t⁻⁴/√det G — and det G is polarization-independent (det M = det diag
  = 125). Equality is **exact**, not approximate. (Numerics: ratio → 1 to
  1e−10 by t = 0.05.)
- **t → ∞**: θ → 1 for every positive-definite form — trivially equal.
  (Numerics: ratio → 1 monotonically, deviation decaying at the
  shortest-vector rate e^{−π·0.139·t}.)

Meanwhile the **entire ~12-orders polarization effect** (#4043: measure
1.38758 polarized vs 1.4724e12 product) lives in the interior (θ-ratio 0.72
at t = 1) — exactly the dictionary-gated zone where matching proves nothing.

## Consequence

Any endpoint-anchored q-dictionary — the only non-vacuous kind — assigns the
polarized and product periods the **same q-image**, so the period-side
q-deformation route cannot see the polarization data that #4043 showed
dominates the determinant. The magnitude leg's q-deformation route therefore
carries no dictionary-independent content beyond the product form, and the leg
**collapses onto the τ-functor (categorical) wall** — an independent,
geometry-side convergence with the per-loop leg's #4030 verdict. The two α_EM
legs now point at the *same* single wall: functorial provenance
(`ArchimedeanTauRealization` inhabitation, per the target spec).

## Scope

Scope-(a) **method-class** constraint: it prunes endpoint-anchored period-side
dictionaries, not any categorical ingredient. The τ-functor route is untouched
and remains the open wall. No dictionary fitted, no 8π manufactured, nothing
wired, no tier change.
