In the algebraic refactor of the magic-number / shell-closure
framework, the categorical mass endomorphism $\Phi_n$ acts globally, not
locally. It is not built per-vortex and combined by tensor product.
Instead $\Phi_n$ forms the global section of the categorical mass
functor over the rigid :refterm[braided monoidal category]{#braided-monoidal-category} $\mathbf{C}$, in
the strict sense of monoidal-category global sections:
$\Phi_n \in \mathrm{End}_{\mathbf{C}}(A^{\otimes n})$ is determined
by its compatibility with the Frobenius-Hopf substrate axioms across
every sub-tensor-factor of $A^{\otimes n}$, not by an additive
combination of local pieces.

## Necessity of dropping locality

Local trivialisation—"screening"—provided the framework's earlier
explanation of shell closure: that something local at each vortex
trivialises the full-twist action. That picture carries two flaws:

1. **Anomalous ribbon flux.** A non-trivial ribbon (= framing)
   action on $\Phi_n$ at a non-magic level $n$ would propagate
   unboundedly up the brane tower
   ([recursive-brane-tower](#def:recursive-brane-tower)). Each
   brane level $A_{n+1} = A_n \otimes \Omega^1(A_n)$ inherits the
   framing flux. Without a global cancellation mechanism, the
   accumulated flux at the :refterm[descent]{#descent} limit diverges.
2. **Finite observable mass.** The categorical mass identity
   ([def:hecke-mass-element](#def:hecke-mass-element)) is finite:
   $\mathfrak{m}(\varrho) \in \mathbb{R}$ for every observed
   hadron. Finite observable mass remains incompatible with
   unbounded framing flux.

The only consistent reconciliation requires global topological
neutrality at saturation: at $n \in \mathfrak{M}$, the ribbon
action on $\Phi_n$ evaluates globally to zero (in the centre-of-the-braid-group sense), not locally trivialised by some spectator structure.
This forms precisely the
[categorical neutrality of saturated shells](#prop:categorical-neutrality-saturated-shells)
statement. It provides the structural reason a non-trivial action
cannot coexist with finite mass at saturated $n$.

## The categorical-functor view

In the language of monoidal functors, $\Phi_n$ is

$$
  \Phi_n = (\text{global section of } \mathcal{F}_{\text{mass}})_n,
\qquad
  \mathcal{F}_{\text{mass}}:
    \mathbf{C} \to \mathbf{C},
\qquad
  X \mapsto (\int_A \otimes \mathrm{id}) \circ \Delta \circ (X \otimes -).
$$

The functor $\mathcal{F}_{\text{mass}}$ takes a substrate object
$X$ to its mass endomorphism. The global section $\Phi_n$ at level
$n$ provides the assignment of $\mathcal{F}_{\text{mass}}(A^{\otimes n})$
that respects all the substrate's monoidal-functor structure
simultaneously—including the central full-twist action on each
$A^{\otimes n}$. Demanding that $\Phi_n$ form a single global
section, rather than a colimit of local pieces, enforces the
substrate-level constraint that the central action vanishes at
saturated $n$.

## Implications for the conjecture

[Mass endomorphism conjecture](#conj:mass-endomorphism) (the open
problem of finding a closed-form NF for $\Phi_{\mathrm{mass}}$) is
correspondingly reframed. The conjecture is no longer "find the
local NF generators and combine". It becomes "find the categorical
global section that satisfies the saturated-shell global-neutrality
constraint". The reframing constructs the magic-number ladder as a
structural prediction rather than a numerical phenomenon.

This remark interprets the [mass endomorphism conjecture](#conj:mass-endomorphism) only. It makes no
new logical claim. The mathematical content resides in the
saturated-shell
and [shell-condensation](./homological-shell-condensation.md)
conjectures, which are themselves conditional on the algebraic
refactor.
