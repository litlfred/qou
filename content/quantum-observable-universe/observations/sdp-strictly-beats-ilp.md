Semidefinite-programming (SDP) decisions on the $H_A(q)$ 3-channel
Wedderburn framework ([tower binding energy](#prop:tower-binding-energy))
strictly beat integer-linear-programming (ILP) decisions on the
earlier $H_{3A}(q)$ Plancherel framework for every light nucleus
tested.

## Statement

**Observation.**
*Let $(m_{pp}, m_{pn}, m_{nn}) \in \{1, 2, 3\}^3$ be the integer
multiplicities of inter-nucleon crossings in the atom braid word.
Let $(m_p, m_n) \in \{1, 2\}^2$ be per-nucleon gluon counts.
Two candidate frameworks produce predictions:*

*- **ILP on $H_{3A}$ Plancherel**: single-vortex mass formula
  ([mass endomorphism tower](#prop:mass-endomorphism-tower))
  applied to the $3A$-strand braid with $3A - 1$ generators,
  Wedderburn-weighted over all partitions of $3A$.*
*- **SDP on $H_A$ 3-channel**: $A$-strand nucleon-level algebra
  with $A - 1$ generators, 3 Wedderburn channels (sym/std/alt)
  per generator, analytic-form $\ln|\Phi_q|$ per channel.*

*Evaluated at $q_0 \approx 1.11$ with per-atom optimal
crossing multiplicities, SDP on $H_A$ achieves strictly lower
mass error on every atom tested:*

| Atom  | ILP on $H_{3A}$ | SDP on $H_A$ | Ratio |
|:-----:|----------------:|-------------:|------:|
| $^2$H |        $0.144\%$ |    $0.142\%$ |  $0.99$ |
| $^3$H |        $0.436\%$ |    $0.297\%$ |  $0.68$ |
| $^3$He |        $0.256\%$ |    $0.170\%$ |  $0.66$ |
| $^4$He |        $5.006\%$ |    $0.020\%$ |  $0.004$ |
| $^6$Li |        $\sim 0.0035\%$ |  $0.0036\%$ |  $\approx 1$ |
| $^7$Li |        $0.052\%$ |    $0.0059\%$ |  $0.11$ |

*The gap is dramatic at doubly-magic $^4$He (factor $250 \times$)
where the single-vortex $\prod \hat{V}$ over $3A - 1 = 11$
generators blows up (raw level-1 tower value $21{,}745$ MeV vs
AME $28$ MeV).  The $H_A$ framework's per-generator
$\Sigma \ln|\Phi_q|$ avoids this per-A blow-up by design.*

## Two sources of the ILP disadvantage

1. **Framework mismatch (dominant).** The single-vortex mass
   formula is derived for **one** vortex (single particle, $n$
   strands, $n - 1$ generators).  Applying it to a multi-nucleon
   atom with $3A - 1$ quark-level generators inflates the
   $\prod \hat{V}$ term unphysically.  The correct per-atom
   formula — [tower binding energy](#prop:tower-binding-energy)
   — uses $A - 1$ nucleon-level generators with 3-channel
   Wedderburn projection, not $3A - 1$ with single-vortex
   structure.  See
   [Framework mismatch audit 2026-04-19](docs/framework-mismatch-audit-2026-04-19.md).

2. **Decision method (secondary).** Even within the same
   framework, SDP gives strictly better candidate selection
   than ILP because the Lasserre moment-matrix lift expresses
   quadratic Frobenius positivity $x^T G x \geq 0$ directly,
   while the scalar ILP $G \cdot x \geq 0$ is a strictly
   weaker relaxation.  See [confinement SDP](#prop:confinement-sdp).

## Code references

- SDP on $H_A$: `folio-assistant/computations/sdp_inter_nucleon_hA.py`,
  `sdp_gluon_multiplicity_hA.py`.
- ILP on $H_{3A}$ (deprecated): `folio-assistant/computations/mass_at_3A_proper.py`
  (docstring header flags deprecation),
  `canonical_plus_multibrane.py` (docstring header flags deprecation).
- Witnesses: `inter-nucleon-sdp-hA.witness.json`,
  `gluon-multiplicity-sdp-hA.witness.json`.

**Witness**: `inter-nucleon-sdp-hA.witness.json`.
