<!-- FILE_START: nuclear-binding-beta-stability-intro.md -->
This section translates the admissible knot operators into physical binding states. A character-ratio decomposition per jet level drives the binding mechanism. At level $\ell$, the decomposition coefficient represents the LP-dual variable of a Frobenius-positivity constraint, driven by the elementary symmetric polynomials in the Jucys-Murphy elements. This iterative LP-dual recursion replaces seven disparate mass-formula corrections with a single unified framework, projecting the beta-stability valley naturally as the level set of the Skein binding Lagrangian.

The sequence begins by detailing the confined knot binding decomposition, explicitly tracking the Wedderburn volume deviations across jet levels. The structural pivot links the Wedderburn weights directly to LP shadow prices via the classical Framed-Robinson-Thrall identity. The central symmetric polynomials in the Jucys-Murphy elements supply the closed-form spectrum, executing the iterative recursion.

The derivation subsequently integrates the algebraic mass tools: the Schur-Weyl decomposition, the generating function structure, and the exact pole behavior of the mass trace. A synthesis of magic-shell corrections, Borromean composites, and Pauli exclusions finalizes the knot-factor bookkeeping. The section concludes by deploying the Macdonald hook telescope to explicitize the coefficients, translating the categorical trace cleanly into the macroscopic Skein binding Lagrangian and the physical beta-stability line.
<!-- FILE_END: nuclear-binding-beta-stability-intro.md -->

<!-- FILE_START: confined-knot-binding.md -->
*Let $\beta \in H_3(R, q)$ be a confined nuclear braid built from crossing operators at generators $\sigma_{i_k}$. The Wedderburn-Artin decomposition separates each crossing's contribution into three channels:*

$$
  \hat{V}(c, d)
  = W_{\mathrm{sym}} \cdot \chi_{\mathrm{sym}}(c, d)
  + W_{\mathrm{std}} \cdot \chi_{\mathrm{std}}(c, d)
  + W_{\mathrm{alt}} \cdot \chi_{\mathrm{alt}}(c, d).
$$

*The extremal contributions exactly cancel for symmetric crossings encoding the proton-neutron force. The binding volume transfers entirely to the standard representation:*

$$
  \hat{V}_{\mathrm{pn}}
  = W_{\mathrm{std}} \cdot \Bigl(z - \frac{H_A}{2}\Bigr).
$$

*The 2-dimensional standard representation creates non-commuting cross-channel interactions between adjacent generators. This generates the Markov-weighted pair interaction term $\delta_{\times}$.*

For an $A$-nucleon system constructed sequentially through quark, nucleon, and nuclear jet levels, the character ratio measures the volume departure from the free constituents. The total knot factor multiplies these strict, empirically-independent character ratios across all levels.
<!-- FILE_END: confined-knot-binding.md -->

<!-- FILE_START: molecular-bond-binding-from-trefoil-insertion.md -->
*A covalent bond functions categorically as an inverse trefoil $T^{-1}$ inserted between two atomic braids $\mathcal{A}$ and $\mathcal{B}$. The molecular binding energy scales via the per-channel volume shifts:*

$$
  E_{\mathrm{bond}}
  = \bigl(
      W_{\mathrm{sym}} \cdot \Delta\Phi_{\mathrm{sym}}
    + W_{\mathrm{std}} \cdot \Delta\Phi_{\mathrm{std}}
    + W_{\mathrm{alt}} \cdot \Delta\Phi_{\mathrm{alt}}
    \bigr) \times E_{\mathrm{mol}},
$$

*where $E_{\mathrm{mol}} = m_e \alpha^2 / 2$ supplies the Hartree energy scale. Double and triple bonds insert multiple inverse trefoils, driving the $1 : 2 : 3$ bond-energy scaling directly from the categorical multiplier.*
<!-- FILE_END: molecular-bond-binding-from-trefoil-insertion.md -->

<!-- FILE_START: jet-filtered-knot-factor.md -->
**Conjecture.**
*The Bethe-Weizsäcker knot factor $a(Z, N)$ governing bulk binding evaluates directly from the jet-filtered character convergence of the nuclear quotient braid $\bar\beta$.*

At higher jet levels, the per-level invariant converges strictly to a topology-independent $q$-dimension-weighted average. The intermediate nucleon-by-nucleon normal forms align with distinct knot patterns, mapping odd $Z$ to trefoils and even $Z$ to Hopf links. Double-magic nuclei converge strongly to the unknot.

The full bulk knot factor $a(Z, N)$ equals the evaluated Jones polynomial of the nuclear quotient braid $J_{\bar\beta}(q)$. The quotient tracks exclusively the $A(A-1)/2$ inter-nucleon crossings, suppressing internal nucleon structure.
<!-- FILE_END: jet-filtered-knot-factor.md -->

<!-- FILE_START: jet-convergence-classical-limit.md -->
**Conjecture (exact at $k = 3$, convergence at $k > 3$).**
*At $k = 3$, the jet-filtered knot invariant evaluates exactly using the $q$-deformed Wedderburn weights $W_\lambda = d_q(\lambda)^2 / [3]_q!$. As the jet level $k \to \infty$, the invariant converges to the linear $q$-dimension scaling $f_\mu^\infty = d_q(\mu)/\sum d_q(\nu)$.*

The classical branching multiplicities remain $q$-independent, but the $q$-hook corrections do not factorize over the branching. The Kerov $q$-hook walk and the Féray-Méliot $q$-Plancherel Central Limit Theorem ensure $O(1/\sqrt{k})$ convergence. The $q$-deformation critically enhances the standard channel at low $k$, explaining why the nuclear topology dominates binding exclusively at physical energy scales.
<!-- FILE_END: jet-convergence-classical-limit.md -->

<!-- FILE_START: wigner-np-pairing.md -->
*The self-conjugate $(2,2) \vdash 4$ partition at Hecke level $k = 4$ introduces the categorical Wigner energy from $T=0$ isoscalar np pairing. The energy scale equals exactly the $(2,2)$ $q$-hook product:*

$$
  \mathbf{\Delta}_{(2,2)}
  = m_e \cdot [3]_q \cdot [2]_q^2
  \approx 6.29\;\mathrm{MeV}.
$$

The scale matches the empirical Wigner value without fitting. The $(2,2)$ channel and the bulk shell corrections derive from identical categorical dimensions. The unified iterative recursion subsumes this specific binding increment, accumulating the Wedderburn projection step-by-step from $A=1$.
<!-- FILE_END: wigner-np-pairing.md -->

<!-- FILE_START: reeb-pn-magnitude-criticality.md -->
*Let $R$ be a commutative ring, $v \in R$ invertible, $[2]_v = v + v^{-1}$,
and let*

```tex
\begin{align*}
  M(b) &= \begin{pmatrix} 1 & b \\ b & -1 \end{pmatrix},
  &S(a,w) &= \begin{pmatrix}
     0 & a & w & w\\
     a & 0 & w & w\\
     w & w & 0 & -a\\
     w & w & -a & 0
  \end{pmatrix}
\end{align*}
```

*denote the symmetric-sector exchange matrix and the uniform-magnitude
$[1^4]$ complete-graph exchange matrix on nucleon blocks $[p,p,n,n]$. Then:*

1. *(Deformation identity)* $5 + (v - v^{-1})^2 = 1 + [2]_v^2$.
2. *(Cayley–Hamilton form)* $M(b)^2 = (1 + b^2)\cdot\mathbf{1}$; in
   particular the classical $b = 2$ gives the scalar $5$.
3. *(Marginal stability)* $\det\bigl(\mathbf{1} + g\,M(b)\bigr)
   = 1 - g^2(1+b^2)$ for every $b$; hence, specializing to the deformed
   pn-degree $b = [2]_v$, any $g$ with $g^2(1 + [2]_v^2) = 1$ is exactly
   the point where the deformed symmetric-sector determinant
   $\det\bigl(\mathbf{1} + g\,M([2]_v)\bigr)$ vanishes.
4. *(pn-sign blindness)* With $D = \mathrm{diag}(1,1,-1,-1)$ one has
   $D\,S(a,w)\,D = S(a,-w)$, and consequently
   $\det(\mathbf{1} + S(a,w)) = \det(\mathbf{1} + S(a,-w))$ and
   $\mathrm{tr}\bigl(T\,S(a,w)^k\bigr) = \mathrm{tr}\bigl(T\,S(a,-w)^k\bigr)$
   for every $k$ and every $T$ commuting with $D$.

*In particular the magnitude $g$ with $g^2(1+[2]_v^2) = 1$ equals
$z/\sqrt{1+z^2}$ evaluated at the Markov bond factor $z = 1/[2]_v$ whenever
square roots are available, and satisfies
$g^2\,(5 + (v-v^{-1})^2) = 1$ by item 1.*

## Lean formalization

All four items are proved sorry-free over generic base rings in
`QOU.MassTheory.ReebPnMagnitude`: `deformation_eq_ceiling` (item 1),
`ss_matrix_sq` (item 2), `ss_det_marginal` and
`ss_det_zero_at_criticality` (item 3), `pn_sign_conjugation`,
`pn_sign_det_invariant` and `pn_sign_trace_blind` (item 4).

## Scope

The proposition is pure exchange-matrix algebra; it carries no physical
identification. The physical reading of $g$ as the pn-bond linking
amplitude is the separate
[conjecture](reeb-linking-cwf-normalization.md), and the derivation
record is
[`docs/audits/2026-07-06-reeb-flow-pn-magnitude-provenance-and-1four-extension.md`](https://github.com/litlfred/qou/blob/main/docs/audits/2026-07-06-reeb-flow-pn-magnitude-provenance-and-1four-extension.md).
Item 4 implies the $[1^4]$ pn writhe sign is invisible to every
grading-commuting observable class; sign sensitivity requires $p{\leftrightarrow}n$
mixing operators.
<!-- FILE_END: reeb-pn-magnitude-criticality.md -->

<!-- FILE_START: reeb-linking-cwf-normalization.md -->
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
<!-- FILE_END: reeb-linking-cwf-normalization.md -->

<!-- FILE_START: unified-iterative-correction.md -->
*The unified iterative correction accumulates binding energy sequentially over the Young seminormal trace. The per-partition binding corresponds directly to its Frobenius positivity LP shadow price $u_\lambda$, scaled by its $q$-hook product:*

$$
  B_\lambda(Z, N)
  = m_e \cdot H_q(\lambda) \cdot u_\lambda \cdot
    \big( \ln\big| \mathrm{tr}\, \mathbf{M}_\lambda^{(0..A)} \big|
          - \ln d_\lambda \big).
$$

*Only multi-dimensional mixing partitions carry non-zero shadow prices. The total unified correction sums these strictly over all $\lambda$.*

The formulation bypasses special-case branching entirely. Each atomic step computes an independent energy increment from the transition trace difference. The process extracts the precise binding energy incrementally via identical algebraic mechanisms across all values of $A$.
<!-- FILE_END: unified-iterative-correction.md -->

<!-- FILE_START: knot-factor-frobenius-pairing.md -->
**Conjecture.**
*The mass-identity Markov-trace defect replaces the empirical Bethe-Weizsäcker bulk terms. Using the single-level categorical mass identity, the bulk binding energy calculates directly as:*

$$
  B_{\mathrm{bulk}}(Z, N)
  \;=\; E_0 \cdot
  \bigl(
    |\mathrm{tr}_M(W_{\mathrm{free}})|
    \;-\; |\mathrm{tr}_M(W_{\mathrm{atom}})|
  \bigr).
$$

The binding corresponds strictly to the non-abelian action integral difference between the atom and the free constituent baseline. A single archimedean calibration constant $E_0$, fixed by neutron beta decay, maps the pure Markov defect to the physical MeV scale. The categorical knot factor identifies as the closed-form Skein eigenvalue product over all signed proton-neutron crossings.
<!-- FILE_END: knot-factor-frobenius-pairing.md -->

<!-- FILE_START: wedderburn-weight-canonical.md -->
*The Bethe-Weizsäcker mass coefficient and the LP shadow-price scale the identical canonical $q$-deformed Wedderburn-block weight:*

$$
  \tilde w_\lambda
  \;:=\;
  \frac{\dim_q(\lambda)^2}{[n]_q!}.
$$

*The quantum hook-length dimension $\dim_q(\lambda)$ defines via the $q$-deformed Frame-Robinson-Thrall formula. This identity holds universally across all $\lambda$. The Wenzl-bridge reduction $y_\lambda = \tilde w_\lambda$ applies exclusively to the self-conjugate stratum.*

This establishes the central canonicity of the weight $\tilde w_\lambda$. The LP form strictly multiplies this weight by $h/2$. The non-self-conjugate partitions diverge predictably via Wenzl's rigorous hook-content closed form.
<!-- FILE_END: wedderburn-weight-canonical.md -->

<!-- FILE_START: hook-weight-derivation.md -->
**Proposition (conditional on [`conj:shell-transition-knot`](#conj:shell-transition-knot)).**
*The coefficient of the hook invariant $\Phi_4$ in the
four-channel mass formula is*

$$
  \beta_4 = -\tfrac{1}{2}\, w_{[2,2]}(4)
          = -\frac{\dim_q([2,2])^2}{2\,[4]_q!}
          \approx -0.083
$$

*where $w_{[2,2]}(4) = \dim_q([2,2])^2 / [4]_q!$ is the
Wedderburn-Artin weight of the hook partition $[2,2]$ in $H_4(R, q)$,
the baryon's internal Hecke algebra (3 quarks + gluon =
4 strands).*
<!-- FILE_END: hook-weight-derivation.md -->

<!-- FILE_START: wigner-coefficient-derivation.md -->
**Proposition (conditional on [`conj:q-integer-mass-formula`](#conj:q-integer-mass-formula) — Wigner term coefficient $[5]_q!\cdot m_e$).**
*The Wigner term (term 9) of the BW mass formula has coefficient
$[5]_q! \cdot m_e$, where $[5]_q! = [2]_q [3]_q [4]_q [5]_q$
is the quantum factorial of $H_5(R, q)$.*

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: wigner-coefficient-derivation.md -->

<!-- FILE_START: mass-coefficient-shadow-price.md -->
*Each coefficient of the QOU mass formula
([six-term mass formula](#thm:six-term-mass-formula-complete))
is the shadow price (LP dual variable) of the corresponding
partition's Frobenius positivity constraint in the nuclear
operator selection LP.*
<!-- FILE_END: mass-coefficient-shadow-price.md -->

<!-- FILE_START: frobenius-self-duality-forces-lp-dual-extraction.md -->
*The Markov trace $\tau$ on $H_n(R,q)$ is a non-degenerate
symmetric bilinear pairing. This makes $(H_n(R,q),\tau)$ a
Frobenius algebra, hence canonically isomorphic to its
$R$-linear dual. Under this isomorphism, the primal LP variable
$x \in H_n$ and the dual LP variable $u \in H_n^*$ live in the
same space, and the Observation Frame
$\mathrm{Obs}_\tau(a) := \tau(a \cdot -)$ extracts the
shadow-price representative of every observable.*
<!-- FILE_END: frobenius-self-duality-forces-lp-dual-extraction.md -->

<!-- FILE_START: frobenius-self-duality-forces-lp-dual-extraction-interpretation.md -->
**Remark (categorical content).** The Frobenius self-duality
holds at the categorical level: the rigid monoidal category
$\mathbf{Rep}(H_n(R,q))$ is self-dual under the
$\tau$-pairing, and $\tau$ is precisely the categorical trace
$\mathrm{tr}_C$ on the unit object. The "primal vs. dual"
distinction in the LP is a $K$-theoretic shadow of the
categorical self-duality; there is no other choice.

## Lean formalization

The companion Lean encodes `observationFrame`, `frobeniusSelfDualityMap`, and the theorem `frobenius_self_duality_forces_lp_dual_extraction`, with the construction deferred via `sorry` (`-- Ref: [manuscript]`).
<!-- FILE_END: frobenius-self-duality-forces-lp-dual-extraction-interpretation.md -->

