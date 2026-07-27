# Coordination — derive the SPIN part of u(q₀) (continuation of #4391)

**Goal.** Close (or honestly bound) the last open half of the
`conj:binding-qbeta-complex-volume` S-channel map `u(q₀)`. After #4372/#4391
the picture is:

- `V₄₁(u)` concrete; `Im 𝔙₄₁ = (√3/4)(Re²u − Im²u)` (proved `imV₄₁`).
- The **real-boost** part of `u(q₀)` is geometrically fixed: `Re u = ln q₀`
  (`meridian-holonomy-boost.md`, proved) — muon sign-correct + ballpark, but
  **refuted as the full map** (nearly constant across the ~1e-8-apart anchors;
  can't give `S(proton)<0`).
- The **sign-flip** needs `Im²u > Re²u` at the proton anchor — the meridian
  holonomy's **boost→spin transition** (real q₀ boost vs `|q|=1` spin). The
  spin/imaginary part of `u(q₀)` is the OPEN piece.

## Workplan (beans milestone `qou-h2k4`)

- **[SP1] (`qou-x581`) geometric origin of the spin part.** Candidate: the
  **fibre** meridian holonomy. `PhiBSArgumentIdentification` fixes the physical
  regime as the fibre branch (real `b` ⇒ `|q_b|=1`), with
  `q_b = e^{i·ln q₀/2}` (`fibreQParam_fibreB`, proved). So the fibre log
  meridian holonomy is `log q_b = i·(ln q₀/2)` — a **pure spin** (imaginary),
  exactly the `|q|=1` compact regime. Test `u = ln q₀ + i·(ln q₀/2)` (boost +
  fibre spin) under `Im 𝔙₄₁`; derive-then-check, no fit.
- **[SP2] (`qou-4kr1`) the hypersensitivity crux (the hard open frontier).**
  `S(muon)/S(proton)` flips sign and changes magnitude ~4× while the anchor
  q₀'s differ by only ~1e-8 (slope `k≈2.2e6`, #3773 hypersensitivity witness).
  A *smooth* function of q₀ (boost `ln q₀`, spin `ln q₀/2`) cannot be that
  hypersensitive — so the sign-flip source must be a **resonance / near-
  degeneracy / fractional-part** structure, not a smooth geometric term. This
  is the genuine open question: what geometric quantity is hypersensitive to
  q₀ at the 1e-8 level? (Connects to the c₃ flip-flop hypersensitivity saga.)

## Discipline

Derive-then-check; anti-fit (every component of `u` must come from geometry —
`ln q₀` boost, `ln q₀/2` fibre spin — never chosen to match `S`);
anti-laundering (no `SDeformedVolumeChannel` instance fabricated; if the
smooth boost+spin candidate cannot reproduce the hypersensitive flip, that is
an honest scope-(a) result — the map needs a non-smooth/resonance ingredient,
recorded not buried). Expected likely outcome: **SP1 sharpens the smooth part;
SP2 is the residual open crux** (a smooth u cannot be hypersensitive).
