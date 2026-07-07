**Conjecture (CWF linking normalization).**
*Let $K$ be a field containing the bond-factor algebra, with
$[2]_v = v + v^{-1}$ invertible. There is a linking-amplitude assignment
$\ell : K \to K$ on bond factors such that*

$$
  \ell(z)^2\,\bigl(1 + z^2\bigr) \;=\; z^2
$$

*for every bond factor $z$, and the physical pn-bond magnitude is
$g = \ell(z)$ evaluated at the Markov bond factor $z = 1/[2]_v$.*

The equation states, square-root-free, that the amplitude is the
unit-normalized transverse component $\ell(z) = z/\sqrt{1+z^2} =
\sin(\arctan z)$: the bond strand's direction in the two-channel
Temperley–Lieb decomposition is $(1, z)$ — the direct channel with
amplitude $1$ and the exchange channel with the Markov conditional-expectation
weight $z = \delta^{-1}$ — and the Gauss–Călugăreanu–White–Fuller linking
integrand reads that direction through unit tangents per unit arc length.
The tangent identification is the Markov property (a theorem); the sine
normalization is the CWF unit-tangent structure (a theorem); what this
conjecture asserts is the remaining physical identification: *the Reeb
linking amplitude is the CWF functional evaluated on the channel-space
direction*.

## Consequence (proved conditional on this conjecture)

Given the class, the pn-bond magnitude satisfies the deformed-criticality
equation of
[the criticality proposition](reeb-pn-magnitude-criticality.md):
$g^2\,(1 + [2]_v^2) = 1$, equivalently $g^2\,(5 + (v - v^{-1})^2) = 1$
(`amplitude_bond_criticality` in the Lean sibling, sorry-free modulo the
class).

## What this conjecture does not claim

It does not supply the MeV unit for the deuteron binding law: the linear
$B(^2\mathrm{H}) = 5g$ rule remains a near-match with its unit anchor open
(constraint ledger in
[`docs/audits/2026-07-06-reeb-flow-pn-magnitude-provenance-and-1four-extension.md`](https://github.com/litlfred/qou/blob/main/docs/audits/2026-07-06-reeb-flow-pn-magnitude-provenance-and-1four-extension.md)
§2e–§2f). No instance of the class is provided; per the corpus discipline,
axiomatization is not proof and this block does not unblock any production
wiring.
