**Conjecture (Aeon recycling).**
*Let $\mathrm{CMB}$ be the CMB functor
([CMB functor](#def:cmb-functor)),
let $\Phi_1^q$ denote the first Planck step of the torsion flow
([torsion-driven knot flow](#def:torsion-knot-flow)),
and let $\nabla_q$ be the $q$-connection.*

*If the degree-$1$ component of $\mathrm{CMB}(\mathcal{A})$
satisfies the integrability condition of $\nabla_q$, then the
composition*

$$
  \Phi_1^q \circ \mathrm{CMB}
   \colon 
  \pi_0\!\bigl(\mathrm{Bun}^{\circ}\bigr)
   \longrightarrow 
  \mathrm{Bun}^{\circ}(\mathbb{P}(V))
$$

*is well-defined — i.e.\ the first Planck step applied to
the CMB of an aeon produces an object with $A_0 \neq 0$,
landing back inside $\mathrm{Bun}^{\circ}$.*

**Content of the conjecture.**

1. **The CMB regenerates particles.**  The degree-$1$ transport
   data (winding modes) in $\mathrm{CMB}(\mathcal{A})$, when
   iterated once by the Reeb flow $f_q$, produces non-trivial
   degree-$0$ fibre data.  This is the "condensation" of
   thermal radiation into particle states.

2. **The recycling map lands in a new aeon.**  The output
   $\Phi_1^q(\mathrm{CMB}(\mathcal{A}))$ lies in
   $\mathrm{Bun}^{\circ}$, hence in some connected component
   — a (possibly new) aeon $\mathcal{A}'$.

3. **Adjacent aeons are connected by the recycling map.**
   If $\mathcal{A}$ and $\mathcal{A}'$ are adjacent
   ([aeon](#def:aeon)), then
   $\Phi_1^q(\mathrm{CMB}(\mathcal{A})) \in \mathcal{A}'$.

**The integrability condition.**
The $q$-connection $\nabla_q$ defines parallel transport
along the Reeb flow.  The integrability condition is
$\nabla_q^2 = F_{\nabla_q}$ — the curvature of the
connection controls whether degree-$1$ data can be iterated
coherently.  When $F_{\nabla_q}$ is compatible with the
degree-$2$ component of the CMB, the transport data fits
together globally and the recycling map is well-defined.

**Categorical formulation.**
If the conjecture holds for all aeons, then
$\Phi_1^q \circ \mathrm{CMB}$ extends to a functor

$$
  \mathcal{R}
   \colon 
  \pi_0(\mathrm{Bun}^{\circ})
   \longrightarrow 
  \pi_0(\mathrm{Bun}^{\circ})
$$

— the **recycling functor** — that sends each aeon to its
successor.  A fixed point of $\mathcal{R}$ would be a
self-recycling aeon: one whose CMB regenerates itself.
