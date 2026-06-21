*Lean sibling: archimedean specialisation over a field $R$ carrying the $q$-data (AGENTS.md §7c).*

**Definition (van der Waals channel).** *In the 2-strand inter-molecular Hecke
algebra $H_2(q)$ (two molecules $=$ two strands), the **van der Waals channel**
is the symmetric-block idempotent*

$$
  e_+ \;=\; \frac{\sigma + q^{-1}}{q + q^{-1}},
  \qquad \sigma \mapsto q \ \ (\text{trivial rep}),
$$

*the Hopf $/[2]_q$ block. Its complement is the directional (hydrogen-bond)
block $e_- = (q-\sigma)/(q+q^{-1})$ (sign rep, $\sigma\mapsto -q^{-1}$).*

The Hopf link $\mathcal{L}_H = T_{2,2} = \widehat{\sigma_1^2}$
([`def:hopf-diquark`](#def:hopf-diquark)) has **vanishing hyperbolic volume**,
$\mathrm{Vol}(\mathcal{L}_H)=0$ — a linking, *volume-less* correlation: two
molecules **linked but not bonded**, with no shared bonded volume. That is
exactly the topological signature of **dispersion** (the van der Waals force):
the attraction without a chemical bond. The framework already carried this
object as the symmetric / diquark block (the same $[2]_q$ channel as the Hopf
diquark); naming it the **van der Waals channel** makes the dispersion force an
explicit object rather than an unmodelled residual.

The block is a genuine Wedderburn projector: $e_+ + e_- = 1$ and $e_+^2 = e_+$
(Lean `blocks_partition_unity`, `vdw_idempotent_cleared`; both sorry-free,
verified Lean 4.24.0 + Mathlib). Note the Hopf link is *not* a separate operator
from $e_\pm$: in $H_2(q)$, $\sigma_1^2 = (q-q^{-1})\sigma_1 + 1$ is algebraically
dependent on $\{1,\sigma_1\}$, so the operator-selection SDP over
$\{1,\sigma_1,\sigma_1^2\}$ is rank-deficient — the independent channels are
exactly $e_+$ (van der Waals) and $e_-$ (hydrogen bond).
