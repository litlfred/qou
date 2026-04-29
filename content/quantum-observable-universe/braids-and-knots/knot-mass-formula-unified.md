Let $\varrho \colon \mathbf{1} \to A$ be a vortex with braid
representative $\beta \in B_n$ and Hecke mass element
$T_w \in H_n(R, q)$
([Hecke mass element](#def:hecke-mass-element)).  Let
$\hat V_i^{\mathrm{full}}$ denote the additive-Wedderburn traced
volume at generator $i$ of the braid word.  Let
$\Phi_q(z) = \prod_{k \geq 1} (1 - q^{-k} z)^{-1}$ be the quantum
dilogarithm and $z = 1/(q^{1/2} + q^{-1/2})$ the Markov parameter.

**Theorem (unified knot mass formula).**
*The categorical mass of the vortex $\varrho$ is*

$$
  \boxed{
    \mathfrak{m}(\varrho)
    \;=\;
    \underbrace{\bigl|\mathrm{tr}_M(T_w)\bigr|}_{\text{descended}}
    \;+\;
    \underbrace{\sum_{i=0}^{n-2} \Phi_q\bigl(|\hat V_i^{\mathrm{full}}|\bigr)
               + z^2 \sum_{0 \leq i < j \leq n-2}
                  \Phi_q\bigl(|\hat V_i^{\mathrm{full}} \hat V_j^{\mathrm{full}}|\bigr)}_{\text{brane tower}}
    \;+\;
    \underbrace{m_e \cdot \mathrm{tr}_M\bigl(C_{\dim_q}^{H_n(R, q)}\bigr)}_{\text{Frobenius co-Casimir}}
  }
$$

*where*

$$
  C_{\dim_q}^{H_n(R, q)}
  \;=\;
  \sum_{\lambda \,\vdash\, n}
    \frac{[n]_q!}{\dim_q(\lambda)^2 \cdot d_\lambda}
    \cdot e_\lambda
  \;\in\; Z\bigl(H_n(R, q)\bigr)
$$

*is the Frobenius co-Casimir element
([universal Frobenius co-dimension](#thm:frobenius-codim-universal))
with trace*

$$
  \mathrm{tr}_M\bigl(C_{\dim_q}^{H_n(R, q)}\bigr)
  \;=\;
  \sum_{\lambda \,\vdash\, n} \frac{1}{\dim_q(\lambda)}.
$$

**Three-part structure.**

| piece | algebraic origin | physical content |
|---|---|---|
| descended $\|\mathrm{tr}_M(T_w)\|$ | Markov trace of braid word | $E^0$ term of filtration |
| brane tower $\sum \Phi_q$ | quantum-dilogarithm resolution | single + pair blow-ups |
| Frobenius $m_e \cdot \mathrm{tr}_M(C_{\dim_q})$ | self-dual co-Casimir | universal fibre-functor residual |

*Each piece is computable from the braid word $T_w$ and the
quantum dimensions $\{\dim_q(\lambda) : \lambda \vdash n\}$ alone.
No empirical constant enters except the single fibre-functor
calibration $m_e$ (or equivalently $E_0$) that converts
categorical mass to MeV
([categorical mass, Markov](#prop:categorical-mass-markov)).*

**Specialisations by braid size $n$.**

*For a trefoil / single nucleon ($n = 3$):*

$$
  \mathfrak{m}_{\mathfrak{p}}
  \;=\;
  |\mathrm{tr}_M(T_w^{\mathfrak{p}})|
  + \text{brane-tower}(n{=}3)
  + m_e \cdot \left(2 + \frac{1}{[2]_q}\right).
$$

*The Frobenius piece $m_e \cdot (2 + 1/[2]_q) \approx 1.276\;\mathrm{MeV}$
matches the observed proton tower residual to $0.14\%$
([proton residual](#prop:partition-sum-proton-residual)).
The same $n = 3$ Frobenius piece also closes the deuteron
binding gap to $3.9\%$
([deuteron first principles](#rem:deuteron-first-principles)),
consistent with the per-vortex (not per-atom-partition)
character of the Frobenius correction.*

*For a general isotope braid ($n = 3A$):*

$$
  \mathfrak{m}_{\text{isotope}}
  \;=\;
  |\mathrm{tr}_M(T_w)|
  + \text{brane-tower}(n{=}3A)
  + m_e \cdot \sum_{\lambda \,\vdash\, 3A} \frac{1}{\dim_q(\lambda)}.
$$

*The right object is the $(3A)$-level Frobenius sum
$\tau\bigl(C_{\dim_q}^{H_{3A}(R, q)}\bigr) = \sum_{\lambda \vdash 3A} 1/\dim_q(\lambda)$,
not $A$ copies of the single-vortex $(n=3)$ value.*

*This is forced by the algebraic content of
[Frobenius co-Casimir universal](#thm:frobenius-codim-universal):
when the isotope's braid lives in $H_{3A}(R, q)$, the central
idempotents $p_\lambda$ are indexed by partitions $\lambda \vdash 3A$,
not by partitions of $3$.  The per-A heuristic
$A \cdot \tau(C_{\dim_q}^{H_3})$ would correspond to a disconnected sum
of $A$ independent $H_3$-blocks, which is**not** the algebra
hosting an isotope braid.*

*Numerical values per
[`probe_term4_conventions.py`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/probe_term4_conventions.py):*

| atom | $A$ | per-vortex $1{\cdot}m_e\Sigma_3$ | per-A $A{\cdot}m_e\Sigma_3$ | **per-$3A$ $m_e\Sigma_{3A}$ (algebraic)** |
|---|---:|---:|---:|---:|
| D | 2 | 1.276 MeV | 2.552 MeV | **1.636 MeV** |
| T, ³He | 3 | 1.276 MeV | 3.828 MeV | **1.300 MeV** |
| ⁴He | 4 | 1.276 MeV | 5.105 MeV | **1.151 MeV** |

*The per-$3A$ values are close to the per-vortex value ($\sim
1.2$–$1.6$ MeV) because $\sum_{\lambda \vdash 3A} 1/\dim_q(\lambda)$
is dominated by the two extreme blocks $((3A))$ and $((1^{3A}))$
each contributing $1$, plus a $q$-dependent middle that grows
slowly in $A$.  This explains why the per-vortex heuristic was
empirically a good approximation, but it is not the rigorous
statement.*

*Compute side: scripts that use $A \cdot m_e \cdot (2 + 1/[2]_q)$
([`mass_formula_6term.py`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/mass_formula_6term.py),
[`unified_low_isotope_predictor.py`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/unified_low_isotope_predictor.py))
are using the per-A heuristic and need to be migrated to the
per-$3A$ algebraic form before any "best prediction" claim.*

**Specialisations by knot type.**

*For a single braid generator ($n = 2$, electron candidate):*
$\widehat{H_2(R, q)} = \{(2), (1,1)\}$ both with $\dim_q = 1$, so
$\sum 1/\dim_q = 2$, giving Frobenius residual $2 m_e \approx
1.022\;\mathrm{MeV}$.

*For Borromean-type braids ($n \geq 6$):*
the Frobenius sum grows with $n$; see table in
[Frobenius universal](#thm:frobenius-codim-universal).

**Classical limit ($q \to 1$).**
*The Hecke algebra reduces to $\mathbb{C}[S_n]$; $\dim_q \to d_\lambda$
and $[2]_q \to 2$.  The Frobenius co-Casimir trace reduces to
$\sum_\lambda 1/d_\lambda$ (classical reciprocal-dimension sum).
For $n = 3$ this is exactly $5/2$ — recovering the upstream
classical discovery
(`residual_partition_sum.py`).*

**Why "unified":**
*The three pieces were previously distinct objects with separate
derivations:*

1. *Descended $|\mathrm{tr}_M|$ — `prop:categorical-mass-markov`,
   the mass-identity prescription.*
2. *Brane tower $\sum \Phi_q$ — `prop:mass-endomorphism-tower`,
   derived from the quantum-dilogarithm resolution of the
   exceptional divisor.*
3. *Frobenius correction — `thm:frobenius-codim-universal` (new),
   derived from self-dual Frobenius structure of $H_n(R, q)$.*

*This theorem combines them into a single three-term formula.
Each term is independently derived; the sum is the total mass.*

**Limitation: the Frobenius piece is vortex-blind.**

*The Frobenius correction $m_e \cdot \mathrm{tr}_M(C_{\dim_q})$
**does not depend on the specific vortex $\varrho$** — only on
the ambient Hecke algebra $H_n(R, q)$.  All trefoil-like vortices
on $H_3(R, q)$ (proton, neutron, any quark configuration) get
the same additive offset $(2 + 1/[2]_q) \cdot m_e$.  Mass
differences between such vortices therefore must come from
the first two pieces (descended + brane tower).*

**Isotope binding: chirality factors are a FOURTH tier.**

*For compound isotope bindings, the paper's full formula
([figure-eight BW coefficients](#prop:figure-eight-bw-coefficients))
adds a **vortex-dependent chirality factor**
$a_K \in \{1 + h,\; 1 - h^2,\; (1 - h^2)^2\}$ for $\{D, T, ^4\mathrm{He}\}$
respectively — reflecting the knot type (chiral+, amphichiral,
Borromean×2).  Upstream verification
(`folio-assistant/computations/bw_chirality_isotopes.py`) gives
$T: 0.505\%$ and $^3\mathrm{He}: 0.856\%$ agreement with AME
using these factors.*

*The chirality factor is a fourth structural layer beyond the
three Frobenius-universal layers of this theorem.  It is vortex-
dependent, like the descended and tower pieces, but algebra-
independent in form (depends only on the knot type of the
isotope braid, not on the specific $T_w$ expansion).  A
complete mass formula is therefore:*

$$
  \mathfrak{m}(\varrho)
  \;=\;
  |\mathrm{tr}_M(T_w)|
  \;+\;
  \sum \Phi_q(\cdot)
  \;+\;
  m_e \cdot \mathrm{tr}_M(C_{\dim_q})
  \;+\;
  a_K \cdot B_{\mathrm{bulk}}
  \;+\;
  (\text{jet-level corrections}),
$$

*where $a_K$ is the chirality factor and the jet-level
corrections reflect the open-problem prefix-word structure
per upstream `pure_hecke_binding.py`.*

**Consistency checks.**

1. *At $q = 1$: classical Hecke reduces to $\mathbb{C}[S_n]$, brane
   tower collapses ($\Phi_1$ singular — handled by a separate
   classical-limit argument), Frobenius term reduces to $\sum
   1/d_\lambda$ (number of conjugacy classes / involutions).*
2. *For the identity braid $T_e = 1 \in H_n(R, q)$:
   $|\mathrm{tr}_M(1)| = 1$; brane tower vanishes (no crossings);
   Frobenius term is pure $\sum 1/\dim_q$ — this is the
   **vacuum mass** of the trivial vortex, consistent with
   the unit object's fibre-functor value.*
3. *Under braid concatenation $T_{w_1 w_2} = T_{w_1} T_{w_2}$
   (Hecke multiplication): the descended piece is multiplicative
   in $|\mathrm{tr}_M|$; the brane tower is additive;
   the Frobenius piece is **vortex-count-additive** (per
   deuteron observation).  Total mass is therefore not simply
   additive or multiplicative — the three pieces compose by
   their own rules and the sum respects the expected
   thermodynamic behaviour of bound-state mass defects.*
