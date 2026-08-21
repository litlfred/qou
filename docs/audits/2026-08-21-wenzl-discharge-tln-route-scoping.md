# Can the `TL_n` route discharge the Wenzl 1988 dependency?

**Status: scoping in progress.** This document is the deliverable; it will
carry either a walked route or a precise statement of which step fails.

## The dependency being attacked

[`WenzlWeightVanishing.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/WenzlWeightVanishing.lean)
proves `schurPrincipal r Q μ / Z = 0 ⟺ ℓ(λ) > r` unconditionally, about an
explicit named expression. Reading that expression as the mass channel's
**actual Ocneanu weight** is Wenzl (1988), axiomatised in #5230 as the class
`QOU.QBeta.WenzlWeight.IsOcneanuWeightSystem` and threaded via `_of_wenzl`.

`#print axioms` cannot see that dependency (bean `qou-fpjy`): the conditional
rows are byte-identical to the unconditional ones.

## The candidate route

[`2026-08-16-ocneanu-weight-axiomatisation.md` §"Is there a cheaper route?"](2026-08-16-ocneanu-weight-axiomatisation.md)
costed one:

> prove only the **vanishing set** via `TL_n`, skipping items 5 and 6 (the
> symmetric-function and hook-content stack) — because downstream consumes the
> vanishing set, not the weight values.

That audit already flagged the route "is not free: it still needs items 1–4."
This document tests whether that is right, and what the residue is.

