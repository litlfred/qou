This category is the categorical counterpart of the Feynman path
integral: rather than integrating over all field configurations, we
follow a single deterministic flow on a finite bundle.  Concretely, a
configuration is a fixed collection of knots pinned to base points in
the projective fibres — if a cosmological initial state exists in the
given affine chart, it is one such $\mathcal{S}_0$ — and the content of
the theory is the trajectory that configuration traces as the torsion
flow carries it forward.  We formalize this picture as follows.

The bundle initial conditions and the torsion-driven knot flow together
define a category $\mathrm{Bun}(\mathbb{P}(V))$:

- **Objects**: bundle initial conditions $\mathcal{S}_0 = \{(p_i, K_i)\}$
  ([Definition](#def:bundle-initial-conditions)).
- **Morphisms**: $\mathcal{S}_0 \to \mathcal{S}_0'$ are pairs $(\sigma, \{\phi_i\})$
  consisting of a permutation $\sigma \in S_N$ and a family of
  ambient isotopies $\phi_i \colon K_{\sigma(i)} \simeq K_{\sigma(i)}'$
  in the respective fibres.  In particular, morphisms preserve the total
  knot content.
- **Identity**: the identity permutation with trivial isotopies.
- **Composition**: permutation composition followed by isotopy
  concatenation.

The torsion flow $\Phi_t^q$ ([Definition](#def:torsion-knot-flow)) is an
endofunctor $\Phi_t^q \colon \mathrm{Bun}(\mathbb{P}(V)) \to \mathrm{Bun}(\mathbb{P}(V))$ that acts on objects by moving base points
and acts on morphisms by conjugating the isotopies with the flow.  The
family $\{\Phi_t^q\}_{t \geq 0}$ assembles into a continuous functor from
$(\mathbb{R}_{\geq 0}, +)$ — viewed as a one-object category — into the
endofunctor category $\mathrm{End}(\mathrm{Bun}(\mathbb{P}(V)))$.

The reference configuration $\mathcal{S}_0$ sits at $t = 0$; the physics
is the trajectory $t \mapsto \mathcal{S}_t$ in $\mathrm{Bun}(\mathbb{P}(V))$.  The
braid-group action on fibres ([Chapter 3](#chap:path-integrals-braiding)) then encodes the interactions
that occur when two knots approach within Planck-scale separation.
