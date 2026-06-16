# `λ_scale` is absorbed into `VolDensity(K)` — the canonical framing

> **Status: settled (2026-05-23). This is the canonical framing — do not propose a separate "λ_scale derivation".**
>
> **Origin commit:** `ffdd84409 — coord: λ_scale absorbed into VolDensity — no more separate constant`
>
> **Authoritative discussion (with numerics):** [`coordination/2026-05-23-algebraic-geometric-observable-consistency.md`](coordination/2026-05-23-algebraic-geometric-observable-consistency.md) §"λ_scale is NOT a separate object — it's what VolDensity produces".

## The rule

For every knot/link `K`, the framework has **one** canonical Geom evaluation per `prop:geom-universality`:

```
m(K) = m_e · VolDensity(K, q₀)
```

There is **no separate** numerical factor named `λ_scale`. The factor that older docs call `λ_scale` is:

```
linking_weight(K, q) := VolDensity(K, q) / Geom_leading(K, q)
                     := VolDensity(K, q) / (Vol(K) / ℏ_q²)
```

— i.e. it is *what Geom assigns to a multi-component link above its bare hyperbolic volume*. For knots, `linking_weight = 1` by definition; for links like the Borromean `𝓑₃`, `linking_weight ≈ 2.46` at `q₀`. The 2.46 is **inside Geom**, not a separately-named constant.

## What this means for "the 2.89% gap"

The proton prediction `m_p ≈ 965 MeV` (+2.89% vs CODATA 938.27 MeV) reflects the **current categorical computation** of `VolDensity(𝓑₃, q₀)`. The open R&D question is:

> Refine the categorical computation of `VolDensity(𝓑₃)` so it lands on its categorically-exact value (which would round-trip the muon anchor and give m_p ≈ 938.27 MeV).

The question is **not** "derive λ_scale = 2.46 from substrate". `λ_scale = 2.46` is the *output* of the current `VolDensity(𝓑₃)` evaluation; refining the input → output mapping is the categorical refinement problem.

## Why this gets repeatedly mis-framed (agent failure mode)

Older code, audit docs, and content blocks (pre-2026-05-23) called the numerical factor `λ_scale` and treated it as if it were a fourth calibration parameter to derive from substrate. Agents pattern-match on that wording and propose:

- "Strategy F/G/H to derive `λ_scale` from H_4 substrate" ← **wrong frame**
- "Bring-Bloch identity for `λ_scale`" ← **wrong frame**
- "Yekutieli per-cell curvature gives λ_scale = 5/2 + (3/4 − G)h²" ← **wrong frame**
- "PSLQ search for `λ_scale` over `[Q, ℏ_q, G, π, ζ(3)]`" ← **wrong frame**

All of these are actually **alternative categorical computations of `VolDensity(𝓑₃)`** — and they have all been tested:

| Attempt | Outcome | Reference |
|---|---|---|
| Bring-Bloch tier 0-5 PSLQ | REFUTED — no integer combination matches | PR #904, audit chain |
| V_7 substrate (Strategy H) | REFUTED non-canonical — no `[4]_q`-normaliser substrate justification | PR #916, #952 |
| q^10 pentagon Bloch-Wigner | REFUTED q-locality non-smooth | PR #951 |
| Unit-circle Bloch-Wigner class | REFUTED literal-rfl loophole; substrate-q₀ coincidence | PR #952, #985 |
| Yekutieli per-cell curvature | Briefly in production 2026-05-23 (a1f68d5e5); PURGED 2026-05-24 (71d674da1) as non-canonical — bijection NEGATIVE per PR #985, Reading A is substrate-q₀ coincidence |

So the negative-result trail is **already** documented across the audit chain. New attempts that re-frame the problem as "derive λ_scale" miss the absorption finding and waste cycles.

## What canonical code does

- [`computations/_li_2_q_util.py`](../computations/_li_2_q_util.py)
  `vol_density_borromean(q)` returns `Vol(𝓑₃)/ℏ_q² × linking_weight(q)`; the linking_weight currently uses the PROVED Family A `5/2 + (3/4)h²` from H_4 Wedderburn as the best categorical input.
- [`computations/m_p_borromean_verification_50dps.py`](../computations/m_p_borromean_verification_50dps.py)
  consumes `vol_density_borromean(q₀)` to predict m_p ≈ 965 MeV.

The `lambda_*_FITTED_FROM_CODATA = 2.4599527869` literals were PURGED from production on 2026-05-22 (PR #888) and are retained ONLY as `*_AUDIT_ONLY` comparison columns in the witness JSON. They will never be consumed by a production prediction.

## When to cite this doc

Cite this doc when:

- An audit or commit message frames the open work as "λ_scale derivation" or "λ_scale closure".
- A new strategy probe is structured as "find the substrate formula that produces λ_scale = 2.46".
- A workplan or coord doc speaks of the residual as a separate calibration gap to close.

Reply (or refactor) to use `VolDensity(K)` language and link here.

## See also

- [`coordination/2026-05-23-algebraic-geometric-observable-consistency.md`](coordination/2026-05-23-algebraic-geometric-observable-consistency.md) — the original numerical demonstration that the 2.46 factor doesn't come from any standard invariant (Markov trace, Jones polynomial, Wedderburn sum) directly.
- [`canonical-derivation-cheat-sheet.md`](canonical-derivation-cheat-sheet.md) §"⚠ Critical framing" — the top-line warning at the start of the cheat sheet.
- [`../CLAUDE.md`](../CLAUDE.md) §"Canonical derivation chain — cheat sheet" — the warning is also at the chain pointer in CLAUDE.md.
- `prop:geom-universality` (content block) — the underlying mathematical statement that `Geom(K)` is the unique functional satisfying additivity + functoriality + normalisation.
