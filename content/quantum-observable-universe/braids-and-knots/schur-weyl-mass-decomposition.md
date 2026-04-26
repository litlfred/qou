Let $(Z, N)$ be an atom with atomic braid
$\mathcal{A} \in H_{3A}(q)$ on $3A$ strands
([atomic braid](#def:atomic-braid)), and let
$V^{\otimes 3A} \cong \bigoplus_{\lambda \vdash 3A} S^\lambda
\otimes V_\lambda$ be the Schur–Weyl decomposition, with $S^\lambda$
the Specht module of $H_{3A}(q)$ and $V_\lambda$ the corresponding
$\mathrm{GL}_q$-irreducible.

**Proposition.**
*The Markov trace of the atomic braid decomposes over partitions
$\lambda \vdash 3A$ as*

$$
  \mathrm{tr}_M(\mathcal{A})
  \;=\;
  \sum_{\lambda \,\vdash\, 3A}
    \frac{s_\lambda(\mathbf{q})}{H_q(\lambda)}
    \cdot
    \chi^\lambda(\mathcal{A}),
$$

*where $s_\lambda$ is the Schur function evaluated on
$\mathbf{q} = (q, q^{-1})$, $H_q(\lambda) = \prod_{x \in \lambda}
[h_x(\lambda)]_q$ is the $q$-hook product
([hook-weight derivation](#prop:hook-weight-derivation)), and
$\chi^\lambda$ is the Specht-module character.  Equivalently,
writing $w_\lambda(q) = s_\lambda(\mathbf{q})/H_q(\lambda)$ and
$\mathrm{tr}_\lambda = \chi^\lambda(\mathcal{A})$:*

$$
  \mathrm{tr}_M(\mathcal{A})
  \;=\;
  \sum_{\lambda \,\vdash\, 3A} w_\lambda(q)\, \mathrm{tr}_\lambda,
  \qquad
  w_\lambda(q) \in \mathbb{Z}[q, q^{-1}].
$$

**Three-channel regrouping for $A = 1$.**
*When $A = 1$ (single nucleon, $H_3(R, q)$), the partitions of $3$
are $\{(3), (2,1), (1,1,1)\}$ corresponding respectively to the
symmetric, standard, and antisymmetric Wedderburn blocks:*

$$
  w_{\mathrm{sym}} = w_{(3)} = \frac{[3]_q [2]_q}{[3]_q [2]_q [1]_q},
  \quad
  w_{\mathrm{std}} = w_{(2,1)} = \frac{[2]_q}{[3]_q [1]_q^2},
  \quad
  w_{\mathrm{alt}} = w_{(1,1,1)} = \frac{1}{[3]_q [2]_q [1]_q}.
$$

*These match the three-parameter Wedderburn weights
([three parameters Wedderburn](#prop:three-parameters-wedderburn))
and recover the three-invariant formula
([Wedderburn mass formula](#thm:wedderburn-mass-formula)) as the
$A=1$ specialisation.*

**Additive-Wedderburn approximation and its failure mode.**
*The current computation engine uses the **additive-Wedderburn**
approximation: for an $A$-nucleon atom it sums the $A=1$ weights
$(w_{\mathrm{sym}}, w_{\mathrm{std}}, w_{\mathrm{alt}})$ over
each of the $3A-1$ generators of $\mathcal{A}$.  This is exact
only when the atomic braid factors through independent copies
of $H_3(R, q)$, which is not the case in general:*

1. *For $A \geq 2$ the exact sum runs over all
   $p(3A)$ partitions of $3A$, not over $A$ copies of
   $\{(3), (2,1), (1,1,1)\}$.*
2. *The additive-Wedderburn trace drops the partitions whose
   Young diagrams have rows longer than $3$, i.e., the
   Schur–Weyl content coming from inter-nucleon entanglement.*
3. *For light atoms ($A \leq 3$) the excluded partitions carry
   small $w_\lambda(q_0)$ and the approximation is within
   $\lesssim 1\%$.  For $A \geq 6$ the excluded partitions
   include configurations like $(3A - 2, 2)$ and $(3A - 2, 1, 1)$
   whose weights grow with $A$, producing the observed
   $5\%$–$20\%$ binding-energy discrepancies in the
   mass-table-best witness at $^4$He through $^{40}$Ca.*

**Algebraic origin of each channel.**
*Schur–Weyl duality assigns each partition $\lambda$ a role:*

1. *$\lambda = (3A)$ **(fully symmetric)** — base-volume channel.
   Scales as the trace of the identity on the $\mathrm{Sym}^{3A}$
   representation; contributes a term proportional to $A$ (forced
   by extensivity of the Markov trace on a tensor product).*
2. *$\lambda = (3A-1, 1)$ **(standard defect)** — boundary channel.
   Scales as $A^{2/3}$ by the Weyl dimension formula for boundary
   Specht modules; this is the algebraic origin of the
   surface-like correction.*
3. *$\lambda = (3A-2, 2)$, $\lambda = (3A-2, 1, 1)$ **(pair defects)**
   — pair-crossing channels.  Scale as
   $\binom{A}{2}/A^{1/3}$ by counting pairs of generators whose
   transfer matrices share a Schur–Weyl component.  These are the
   algebraic origin of the pair-crossing correction captured in
   the SDP cross-channel path
   ([Markov pair, $\mathbb{Z}_2$](#prop:markov-pair-z2)).*
4. *Rectangular $\lambda$ **(closed-shell)** — shell-closure
   channel.  When $\lambda$ is rectangular of size $3A$, the
   hook product $H_q(\lambda)$ factorises sharply and $w_\lambda$
   acquires a large value at $q = q_0$; this is the algebraic
   origin of shell-closure enhancement at the magic nucleon
   counts
   ([shell–Schur–Weyl self-duality](#prop:shell-schur-weyl-self-duality)).*

*Each physical correction is therefore a named stratum of the
Schur–Weyl sum, with its scaling exponent determined by the Weyl
dimension formula applied to the corresponding Young diagram.*

**Relation to the GB residue spectral sum.**
*The Schur–Weyl sum above is the **descended** ($E^0$) term of the
residue spectral sum
([GB residue spectral sum](#prop:gb-residue-spectral-sum)):
both sums are over the partitions of $3A$, but the residue sum
adds the Mittag-Leffler contributions from strata $\lambda$ whose
weight $w_\lambda(q)$ has a pole at some $\zeta_\ell$.  The two
propositions together give the full mass:*

$$
  \mathfrak{m}(\mathcal{A}, q_0)
  =
  \sum_{\lambda \,\vdash\, 3A} w_\lambda(q_0)\,\mathrm{tr}_\lambda
  +
  \sum_\ell \frac{\operatorname{Res}_{q=\zeta_\ell}[w_\lambda \mathrm{tr}_\lambda]}
                  {q_0 - \zeta_\ell},
$$

*where the first sum is over regular partitions (analytic at
$q_0$) and the second is over filtration strata with root-of-unity
poles.*
