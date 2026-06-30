*Lean sibling: archimedean specialisation over a field $R$ carrying the $q$-data (AGENTS.md §7c).*

**Definition (Hopf symmetric block $e_+$).** *In the 2-strand inter-molecular Hecke
algebra $H_2(q)$ (two molecules $=$ two strands), the **symmetric (Hopf) block**
is the idempotent*

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
the topological home of **dispersion** (the van der Waals force):
attraction without a chemical bond. Within this Hopf channel the symmetric
$e_+$ block is the retained $[2]_q$ / diquark carrier; the van der Waals force
itself is **not** $e_+$ but the **bar-odd residual** $\sinh(2\lambda)(e_+-e_-)$
that the canonical $P_{\mathrm{avg}}$ projection discards (the proposition
`prop:vdw-pskew-isolation`). This makes the dispersion force an explicit
(small, discarded) object rather than an unmodelled residual.

The block is a genuine Wedderburn projector: $e_+ + e_- = 1$ and $e_+^2 = e_+$
(Lean `blocks_partition_unity`, `vdw_idempotent_cleared`; both sorry-free,
verified Lean 4.24.0 + Mathlib). Note the Hopf link is *not* a separate operator
from $e_\pm$: in $H_2(q)$, $\sigma_1^2 = (q-q^{-1})\sigma_1 + 1$ is algebraically
dependent on $\{1,\sigma_1\}$, so the operator-selection SDP over
$\{1,\sigma_1,\sigma_1^2\}$ is rank-deficient — the independent blocks are
exactly $e_+$ (the symmetric / Hopf-diquark carrier) and $e_-$ (the
antisymmetric / directional block). Van der Waals is the **bar-odd** combination
$\sinh(2\lambda)(e_+-e_-)$ of these two blocks (the canonical
`prop:vdw-pskew-isolation`), not either block alone.
