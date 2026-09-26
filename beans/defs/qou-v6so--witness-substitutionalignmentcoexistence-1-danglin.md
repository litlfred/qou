---
# qou-v6so
title: 'WITNESS: substitution/alignment/coexistence — 1 dangling, 5 unaligned, and 28% on the anchor-defining witness'
status: todo
type: epic
priority: normal
created_at: 2026-09-26T17:56:12Z
updated_at: 2026-09-26T17:56:12Z
---

Owner, 2026-09-26: *"one of the biggest issue ... witness variable
substution/alignement/coexistence"*.

Measured by **loading `content/values/registry.ts` as a module**, not by grepping it —
two regex passes over the TypeScript gave wrong per-entry answers before that (the
fields appear in a different order than a forward scan assumes, so `witnessFile` was
attributed to the previous entry). Flat counts from a regex are fine; per-entry
association is not. Ground truth below.

## The mechanism, for the record

`content/values/registry.ts` maps a stable `name` → (`witnessFile`, dotted `path`).
Prose cites `:val[name]`; the render pipeline substitutes the live witness value, so
"the paper cannot drift away from its computations" (the file's own docstring).
`needsReview: true` means *the canonical witness is not yet identified* and the
pointer is an admitted placeholder at "the closest existing witness".

**68 entries over 17 witness files.**

## 1. SUBSTITUTION — one entry cannot resolve at all

    inv_alpha  ->  computations/alpha/alpha-high-precision.witness.json   MISSING

The file does not exist. So `:val[inv_alpha]` has no value to substitute. This is
not a marginal symbol: `inv_alpha` is α_em⁻¹, which AGENTS.md records as an L2
dashboard row **added 2026-09-07** (`d626761a34`, 238.3×) and which its §"Precision
goals" leans on when it states the scoreable denominator moved 5 → 6. A headline
constant with a broken substitution source.

## 2. ALIGNMENT — 5 of 68 point at a witness that is admittedly not theirs

    inv_alpha   ->  computations/alpha/alpha-high-precision.witness.json  (also missing)
    c_q         ->  computations/q-pinning-50-digit.witness.json
    eta_q       ->  computations/q-pinning-50-digit.witness.json
    chi_q       ->  computations/q-pinning-50-digit.witness.json
    d_H         ->  computations/q-pinning-50-digit.witness.json

Four of the five name the **anchor-defining** q₀ witness as a placeholder — not
because those quantities live there, but because it was the closest file to hand.
`c_q`, `eta_q`, `chi_q` and `d_H` are substrate quantities with their own producers;
pointing them at the pin file means a change to the pin re-renders numbers that do
not depend on the pin.

## 3. COEXISTENCE — this is the structural one, and the registry cannot express it

`q-pinning-50-digit.witness.json` carries **19 of the 68 (28 %)**:

    q_0, q_inv, H_A, hbar_q, hbar_q_sq, two_q, qint_3, qint_4, qint_5,
    z_markov, rho_q, s_skein, codata_rel_unc, Vol_4_1, m_mu_over_e,
    c_q, eta_q, chi_q, d_H

That file is the one AGENTS.md singles out as **ANCHOR-DEFINING** —
`witness._q0_value_for_anchor("muon")` reads it, and re-pinning it in a bulk pass
took `main` red in 2026-08-19 (262 witnesses flipped to `Q0_FLIP`). So **28 % of
every witnessed number in the paper substitutes from the single file at the centre
of the two-pin question.**

**The schema is one `name` → one `witnessFile`.** But this corpus has quantities
that are genuinely two-valued *at the same time*:

- **q₀ has two live pins** — ideal CAL-2 (muon) and experimental (proton), 11.6 ppb
  apart, and AGENTS.md is explicit that both are correct at their own layer and that
  mixing them inside one computed number is a defect.
- **The Markov parameter has two conventions** — C (`√q/(q+1)`, excised but recorded)
  and D (`q³/(q²+1)`, canonical). `z_markov` is in the list above, as ONE entry.

So `:val[z_markov]` renders one number where the corpus holds two, and `:val[q_0]`
cannot say which layer it means. That is not a stale pointer to fix; it is a missing
dimension in the registry's key. The straddle AGENTS.md forbids ("never straddle the
two layers inside one quantity") is *unrepresentable* rather than merely discouraged,
which means prose cannot even state the pair correctly through the mechanism designed
to keep prose honest.

## Options — not started, and 3 needs the owner

1. **Fix `inv_alpha`** — find the real α_em witness and re-point it. Cheap, isolated,
   pure win. Needs no decision.
2. **Re-point the 4 placeholder entries** to their actual producers. Per-entry
   research (each has a real home); mechanical once identified.
3. **Give the key a convention/anchor dimension** — e.g. `:val[q_0]{pin=proton}`,
   or `name` + `variant`. This is a schema change to a platform-consumed registry
   and a change to how every `:val` site reads. **Owner's call**, and it is the only
   one that addresses coexistence rather than working around it.

**Default if nothing is done:** `inv_alpha` keeps failing to substitute, the 4 stay
mis-aimed, and `q_0`/`z_markov` keep rendering one of two correct values with nothing
in the prose to say which. Nothing breaks loudly — which is the problem.

## Related, and NOT the same thing

`qou-cite` covers the bibliography half of the owner's message (`manuscript` is not a
held entry while ~3.8k Lean `-- Ref:` sites cite it). Keep them separate: one is about
numbers substituting from witnesses, the other about keys resolving to references.
