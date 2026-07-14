# α_EM phase-3 Schwinger coefficient — the exact vertex moments do NOT reproduce (1−h²α)

**Date:** 2026-07-14 · **Branch:** `claude/canonical-derivation-c-k-n00n2h` ·
**Probe:** [`alpha_em_rt_phase3b_exact_vertex_moments.py`](../../computations/alpha_em_rt_phase3b_exact_vertex_moments.py)
(+ witness) · **Tier:** exact (fundamental rep, ℚ(q), quantum trace) ·
**Scope:** (a) — the exact realizations tested here fail to produce the
phase-3 claim; a different categorical realization could still derive it. No
value changes; an epistemic **tier** is at stake, not a number.

## Context — why this matters for 1 ppQ

The 1 ppQ flagship (α_EM at +0.313 ppb ≈ 2.1σ) rests on the ladder
`1/α = T + αH·(1−h²α)` with the `(1−h²α)` factor labeled **"derived (RT
phase 3), not fitted."** Phase 3's own docstring records the coefficient
match as open — its leading-order bookkeeping yields `1−h·q⁻¹ = 1−h+O(h²)`,
not `1−h²`, before appealing to a cross-vertex commutator for the h². This
probe executes the deferred check exactly.

## The computation (all exact, validated)

Fundamental rep A = ℂ², Hecke-normalized braiding (σ² = hσ+1), pivotal
μ = diag(q, q⁻¹), quantum trace; singlet idempotent `e₋ = (q−σ)/(q+q⁻¹)` of
the EM projection block. Validations all pass exactly: Hecke + braid
relations, `e₋² = e₋`, `dim_q A = [2]_q`, `qTr(e₋) = 1`. Photon pair =
strands (1,2), matter = strand 3 (or 3,4); vertex = σ₂; moments
`m[w] = qTr(E·w·E)/qTr(E)`, `E = e₋⊗1`.

## Findings

1. **The 2-vertex excess is order (q−1)¹, not h².** Exactly:
   `m₂ − 1 = h·m₁ = (q⁴−q²)/(q²+1)`, with `(m₂−1)/h² = q⁴/(q⁴−1)` — a pole
   at q = 1, not a unit. At the proton pin the excess is **+0.1281** against
   the claimed `−h² = −0.0437`: **wrong order, wrong sign, ratio −2.93**.
2. **The σ⁻¹-vertex reading also fails** (excess `h·(h−m₁)` — still leading
   order (q−1)¹, value −0.0844 ≈ 1.9×(−h²), coefficient not 1).
3. **The commutator escape hatch does not supply −h² either.** The exact
   cross-position 4-letter words (`⟨σ₂σ₃σ₂σ₃⟩`, `⟨σ₂σ₃²σ₂⟩`, …) were all
   computed; the cross-position connected part is −0.608 at q₀ — not
   h²-sized, and the words' (q−1)-expansions start at order 0 or 1.
4. **O(α²) slot single-shot:** neither raw-moment candidate (connected
   4-vertex +0.0329; cross-position −0.608) lands in the required
   `C₂ ≈ −8.1e-4 (±50%)` window — the raw vertex-moment class is pruned
   for the 2-loop slot (consistent with the EmFermionLoop −445% refutation).

## What this changes (and what it does not)

- **Unchanged:** the α_EM numbers. Form B still lands at +0.313 ppb; the
  value of `(1−h²α)` is what it is.
- **Changed (recommended):** the **tier** of the Schwinger factor. "Derived
  (RT phase 3)" over-claims: phase 3 established a *motivation sketch* whose
  exact evaluation fails in the natural realizations. Until a genuine
  derivation exists, the honest label is **structurally-motivated /
  empirically-anchored** — and the 1 ppQ flagship's "the remaining gap is
  only c₂" framing should carry this asterisk: the O(α)·h² term's
  *derivation* is part of the same open program as c₂.
- The **c₂ attack inherits the gap**: there is no exact vertex-moment
  prescription to extend. The honest route to both terms is one and the
  same genuine 2-loop categorical calculation (the multi-week #1495 scope).

## Scope note

Scope-(a): the failure is of the phase-3 prescription **as stated, in the
natural exact realizations** (fundamental rep, quantum trace, singlet
sandwich, σ±-vertices, same/cross-position words — all reported, none
selected). A different realization (different rep for the matter loop, a
different trace normalization, an α-dependent vertex weight) could still
produce `−h²α` — but constructing one *is* the open derivation, and any
candidate must now pass this probe's exact gate.

## Cross-references

- Phase 3: `computations/alpha_em_rt_phase3_schwinger_derivation.py` (its own
  "honest caveat" section anticipates this).
- Headline: [`2026-07-11-path-to-1ppq-alpha-em-opportunity.md`](2026-07-11-path-to-1ppq-alpha-em-opportunity.md)
  (calibration banner added this branch); `alpha_em_schwinger_ladder_probe.py` (#3625).
- 2-loop entropy block: `alpha_em_two_loop_structure_probe.py`.
- EM projection conventions: `predicted-spectra/em-coupling-projection.md`.
