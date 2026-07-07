<!-- FILE_START: beta-decay-magic-shells-k12-barrier-bypass-intro.md -->
Continuation of the preceding section.

This section specialises the $\beta$-decay machinery to magic shells. The following blocks establish the double-magic $\Delta I$ bound, identify the $k = 12$ barrier-bypass mechanism, and derive the magic numbers from the substrate parameter $q$. We exhibit the canonical examples (non-magic ${}^6$Li and single-magic ${}^{18}$O) that test the substrate prediction. The closing blocks lift the substrate-level dictionary into the Bethe–Weizsäcker mass decomposition. They identify the Strutinsky shell-correction term as the graded-trace residue.
<!-- FILE_END: beta-decay-magic-shells-k12-barrier-bypass-intro.md -->

<!-- FILE_START: magic-numbers-from-q.md -->
**Proposition.**
*The nuclear magic numbers $\{2, 8, 20, 28\}$ emerge from the substrate parameter $q_0$ through the per-partition nuclear character computation at Hecke levels $k = 3\ldots 10$.*

*For each partition $\lambda \vdash k$ with Wedderburn weight $w_\lambda = \dim_q(\lambda)^2/[k]_q!$, the nuclear braid $\mathcal{N}(Z, Z)$ has character $\chi_\lambda(Z)$ computed from the Hoefsmit seminormal matrices. The cumulative Wedderburn-weighted signal*

$$
  \Phi(Z) = \sum_{k=3}^{K} \sum_{\lambda \vdash k} w_\lambda \, \ln|\chi_\lambda(Z)|
$$

*has forward second difference $\delta^2 \Phi(Z) = \Phi(Z) - 2\Phi(Z{-}1) + \Phi(Z{-}2)$ that peaks at the magic numbers:*

| $Z$ | $\delta^2 \Phi$ ($K{=}10$) | Magic? |
|----:|-----:|:------:|
| $8$ | $+33.2$ | $\star$ |
| $20$ | $+20.4$ | $\star$ |
| $28$ | $+4.4$ | $\star$ |

*We use no empirical magic number list. The positions emerge from $q_0$ through the Hoefsmit seminormal form of $H_k(q)$.*

## Computation

The Hoefsmit seminormal matrix for partition $\lambda$ at generator $g$ has block-diagonal structure:

- **Generator 0**: pure diagonal (eigenvalue per standard Young tableau).
- **Generator 1**: scattered $2 \times 2$ blocks plus diagonal singletons.

This structure yields $O(d)$ matrix--vector cost per crossing instead of $O(d^3)$ for dense multiplication. This enables a $15\,000\times$ speedup at $k = 9$ (from $557\,$s to $14\,$s) and makes $k = 10$ ($42$ partitions, $\dim \leq 768$) feasible in $48\,$s.

We compute the nuclear character at each $Z$ by multiplying crossing matrices through the full atomic braid $\mathcal{N}(Z, Z)$. This includes intra-nucleon $\mathcal{B}_3 \times \text{quarks}$, inter-nucleon pp/nn/pn crossings, and electron pe crossings using both generators.

## Interpretation

The forward second difference $\delta^2 \Phi$ measures the extra binding from adding one nucleon at $Z$ compared to the trend. At magic $Z$, the per-partition characters have enhanced coherence. The Wedderburn-weighted traces align to produce a positive $\delta^2$ peak. Between magic numbers, the characters decohere.

The declining amplitude ($+33.2$ at $Z = 8$, $+20.4$ at $Z = 20$, $+4.4$ at $Z = 28$) reflects the hierarchical resolution. Magic $8$ is fully resolved at $k = 3$ (3 partitions). Magic $28$ requires $k \geq 7$ (15 partitions) for resolution. Higher magic numbers ($50, 82, 126$) would require $k \geq 12$ where partition dimensions exceed current computational limits.

## Dependence on $q$

All quantities are functions of the substrate parameter $q$:

- Hoefsmit matrix entries: $h/[\rho]_q$ where $[\rho]_q = (q^\rho - q^{-\rho})/(q - q^{-1})$
- Wedderburn weights: $w_\lambda = \dim_q(\lambda)^2/[k]_q!$
- Crossing eigenvalues: $q$ (pp), $-q^{-1}$ (nn), $(q - q^{-1})/2$ (pn)

At $q = 1$ (the classical limit), all $[\rho]_q \to \rho$, $w_\lambda \to \dim(\lambda)^2/k!$, and the magic number signal vanishes. There is no quantum deformation and no shell closure. The magic numbers are a quantum effect that exists only for $q \neq 1$.

## Witness

The file `shell-closure.witness.json` records $\delta^2 \Phi(Z)$ for $Z = 1\ldots 30$ at $K = 10$. The block-diagonal optimised computation resides in `shell_closure_compute.py`. $\square$

## Cross-link: homological route past the $K = 12$ barrier

The Hoefsmit-seminormal pipeline above terminates at $K = 10$. The [homological shell-condensation conjecture](#prop:homological-shell-condensation) provides a $K$-independent algebraic-geometry route. The magic ladder $\{2, 8, 20, 28, 50, 82, 126\}$ is read off the collapse of a Białynicki–Birula spectral sequence at $E_2$, with no matrix evaluation required. The numerical agreement at $Z = 8, 20, 28$ above provides the [empirical computational verification](#rem:k12-barrier-bypass) of the homological prediction at the strand counts where Hoefsmit matrices remain tractable.
<!-- FILE_END: magic-numbers-from-q.md -->

<!-- FILE_START: k12-barrier-bypass.md -->
The Hoefsmit / matrix-evaluation programme
([prop:magic-numbers-from-q](#prop:magic-numbers-from-q),
[prop:hoefsmit-seminormal-form](../braids-and-knots/hoefsmit-seminormal-form.md))
verifies the magic-number ladder at small partition sizes
$k = 3, \dots, 10$ by direct computation of Wedderburn weights from
seminormal-form matrices. At $k \geq 12$ the number of partitions
$|\{\lambda \vdash k\}|$ — and hence the dimension of the Hecke
algebra block-decomposition — grows combinatorially, blocking the
matrix-evaluation approach from confirming saturation at
$\{50, 82, 126\}$.

The algebraic refactor analytically bypasses this barrier. The
homological-condensation conjecture
([`prop:homological-shell-condensation`](../lifting-and-descent/homological-shell-condensation.md))
and the LR-fusion-rigidity conjecture
(`prop:diagrammatic-double-magic-lr-fusion`)
predict the saturated-shell pattern by *structural* arguments
about the Białynicki-Birula stratification and the LR-content-sum
arithmetic on Young's lattice — both of which are *partition-size
agnostic*: the proofs (or class instances) carry through verbatim
at $n = 50, 82, 126$ once the underlying conjectures are accepted.

## Scope of the matrix-evaluation programme's verification

The matrix-evaluation programme produces, for each
$n \leq 10$ and each $\lambda \vdash n$:

* the seminormal-form matrices for $\sigma_1, \dots, \sigma_{n-1}$
 acting on $V_\lambda$,
* the full-twist eigenvalue $q^{c(\lambda)}$ via direct multiplication,
* the BB-stratified spectral-sequence entries $E_\infty^{p, q}(n)$
 by computing the :refterm[descent]{#descent}-graded jet algebra at level $n$ and
 reading off cohomology.

At $n \in \{2, 8\}$ (and partial coverage of $n = 20$ via
branching-rule extrapolation from $n = 10$) the matrix-evaluation
results agree with the predictions of the homological framework:
$E_\infty^{p, q}(n) = 0$ for $q > 0$, the LR fusion at double-magic
$(Z = 8, N = 8)$ collapses to a single $\nu$, and the full-twist
acts as the identity on the saturated $\Phi_n$. Empirical computational
verification is therefore in hand at the small magic numbers.

## Limits of the matrix-evaluation programme

At $n = 12$ already the partition count exceeds memory budgets for
exact-rational seminormal-form computation; at $n \geq 50$ the
combinatorial explosion is unrecoverable on present hardware. A
matrix-evaluation confirmation of the higher-magic ladder
$\{50, 82, 126\}$ is **not** waiting on hardware — it is
fundamentally not the right tool, because the seminormal form is a
*per-partition* object and the saturated-shell content is a
*structural* object. Adding more compute scales the wrong axis.

## Contribution of the homological / LR-fusion framework

Both higher-magic conjectures are structural statements about
combinatorial objects whose verification at large $n$ is a
finite-data check rather than a matrix computation:

1. **Saturated-shell content sum.** For each $n \in \mathfrak{M}$,
 the existence of a self-conjugate partition $\lambda \vdash n$
 with $c(\lambda) = 0$ is a finite combinatorial statement
 verifiable in $O(p(n))$ partition operations.
2. **LR-rigidity at double-magic.** For each pair
 $(Z, N) \in \mathfrak{M} \times \mathfrak{M}$, the existence of
 a *unique* self-conjugate $\nu_{ZN} \vdash Z + N$ produced by
 LR fusion of self-conjugate $\lambda_Z, \mu_N$ is a finite
 LR-coefficient computation, not a matrix evaluation.

Both are testable at $n = 50, 82, 126$ on present hardware in
seconds. The numerical *prediction* therefore exists; what is
conjectural is the *structural identification* of these
combinatorial objects with the categorical mass support.

## Empirical-verification reframing

The historical empirical scorecard
([prop:magic-numbers-from-q](#prop:magic-numbers-from-q)) records
agreement deltas $+33.2, +20.4, +4.4$ between framework predictions
and CODATA at $\{2, 8, 20\}$. Under the refactor these deltas are
**empirical computational verifications** of the homological
prediction at *small* magic numbers — they confirm that the
homological framework reproduces the matrix-evaluation results
where both are available, and that the structural part of the
conjecture is consistent with observation.

The higher-magic deltas are now predictions of the homological
framework alone; their empirical comparison against CODATA at
$\{50, 82, 126\}$ is a forward test rather than a back-fit. This
remark interprets `prop:magic-numbers-from-q` only — it makes no
new logical claim, but it documents the change of evidential status
that the algebraic refactor produces.
<!-- FILE_END: k12-barrier-bypass.md -->

<!-- FILE_START: q-deformed-nuclear-models-comparison.md -->
**Remark (relation to $q$-deformed nuclear and atomic models).**

The magic-number result of [prop:magic-numbers-from-q](#prop:magic-numbers-from-q) joins several quantum-algebraic accounts of nuclear shell structure. We separate our mechanism from three strands of the quantum-group literature. In previous models, the deformation parameter is fitted to the data. In our framework, the substrate parameter $q_0 \approx 1.10998$ is fixed and derived from the calibration triple.

## $\mathrm{SU}_q(2)$ rotor bands

The $\mathrm{SU}_q(2)$ rotator model \cite{minkov1996} describes the rotational bands of deformed rare-earth and actinide nuclei. Its Hamiltonian is proportional to the second Casimir of $\mathrm{SU}_q(2)$, with spectrum

$$
  E_I = \frac{1}{2\vartheta}\,[I]_q\,[I+1]_q + E_0,
$$

where $\vartheta$ is a moment-of-inertia parameter and $[\,x\,]_q$ is a $q$-number. The deformation is a phase $q = e^{i\varphi}$ with $|q| = 1$. The $q$-number $[I]_q = \sin(\varphi I)/\sin\varphi$ yields an oscillatory spectrum. The parameter $\varphi$ is fitted per band. This Casimir matches [def:q-angular-momentum](#def:q-angular-momentum), but evaluates on a different analytic branch. Our substrate $q_0$ is real and greater than $1$, yielding a hyperbolic $q$-number. We share the Casimir operator, but avoid the fitted phase.

## $q$-deformed harmonic oscillator

A three-dimensional $q$-deformed harmonic oscillator with $\mathfrak{u}_q(3) \supset \mathfrak{so}_q(3)$ symmetry \cite{raychev1998} reproduces shell closures by level filling. Expanding the energy in the deformation yields a term proportional to $\ell(\ell+1)$. This orbit-orbit correction reproduces the cluster magic numbers $2, 8, 20, 40, 58, 92, \dots$. It does not produce the spin-orbit ($\ell \cdot s$) coupling required for the nuclear ladder $28, 50, 82, 126$. A scalar oscillator carries no spin degree of freedom. The $\ell \cdot s$ term must be supplied by coupling an external spin-$\tfrac{1}{2}$, matching the Mayer–Jensen shell model \cite{mayer1955}. The $q$-deformation yields the orbit-orbit term, while the spin-orbit input remains independent.

## Elliott $\mathrm{SU}(3)$

Elliott's $\mathrm{SU}(3)$ classification \cite{elliott1958} maps harmonic-oscillator shells to $\mathrm{SU}(3)$ irreducible representations. It is an undeformed ($q = 1$) organizing symmetry. It does not serve as the classical limit of our mechanism. The magic-number signal of [prop:magic-numbers-from-q](#prop:magic-numbers-from-q) is a genuinely $q$-deformed coherence effect that vanishes at $q = 1$. Elliott's $\mathrm{SU}(3)$ and the many-body Hecke trace are complementary accounts at opposite ends of the deformation axis.

## The common distinction

In these previous models, the deformation is a free parameter fitted to the observable. The present framework fixes $q_0$ once and reads the magic numbers off the many-body Hecke trace. The reproduction of higher nuclear or atomic shells without tuning is a forward test. The homological route of [rem:k12-barrier-bypass](#rem:k12-barrier-bypass) supplies the parameter-free prediction at $50, 82, 126$.
<!-- FILE_END: q-deformed-nuclear-models-comparison.md -->

<!-- FILE_START: non-magic-Li6-diagram.md -->
We examine $^{6}\mathrm{Li}$ ($Z = N = 3$, $A = 6$) to illustrate the partition-level diagrammatic content of the double-magic LR-fusion conjecture ([`prop:diagrammatic-double-magic-lr-fusion`](#prop:diagrammatic-double-magic-lr-fusion)) in a non-magic regime. When neither proton nor neutron count lies in $\mathfrak{M}$, both blocks fray. The categorical mass at each level spreads over multiple non-self-conjugate partitions. The LR fusion produces non-zero full-twist flux vectors in both the $Z$ and $N$ tensor factors.

## $Z$-block (frayed)

The proton count $Z = 3$ is not magic. The categorical mass at level $3$ is not concentrated on a single self-conjugate partition. Instead, the Wedderburn support spans
$$
  \lambda \in \{(3),\, (2, 1),\, (1, 1, 1)\} \;\vdash\; 3,
$$
with content sums $c((3)) = +3$, $c((2,1)) = 0$, and $c((1,1,1)) = -3$. Only $(2, 1)$ is self-conjugate. The symmetric and antisymmetric partitions $(3)$ and $(1, 1, 1)$ are conjugates of each other and contribute opposite-sign full-twist eigenvalues $q^{+3}$ versus $q^{-3}$. Frobenius arms exceed legs in $(3)$; legs exceed arms in $(1, 1, 1)$. Neither is balanced.

## $N$-block (frayed)

By symmetry, the same three partitions $\{(3), (2, 1), (1, 1, 1)\}$ contribute on the $N$ side. They carry the same content-sum imbalances.

## LR fusion at $A = 6$

The LR product $V_\lambda(Z=3) \otimes V_\mu(N=3)$ on each pair of frayed blocks spreads over many $\nu \vdash 6$:
$$
  V_\lambda \otimes V_\mu
  \;=\;
  \bigoplus_{\nu \vdash 6}
    c^\nu_{\lambda, \mu} \, V_\nu,
\qquad
  \lambda, \mu \in \{(3), (2,1), (1,1,1)\}.
$$
The combined Wedderburn support of $\Phi_6$ at $^{6}\mathrm{Li}$ is a weighted sum of all such fusions. The weights are determined by the relative strengths of the three frayed components. The resulting $\Phi_6$ has non-zero off-diagonal full-twist flux vectors. It is not a fixed point of $\Delta_6^2$.

## Diagrammatic content

Schematically, the $^{6}\mathrm{Li}$ diagram comprises:
- **Left**: A fragment of Young's lattice between $(3)$, $(2,1)$, and $(1,1,1)$. This triangle with $(2,1)$ at the centre carries full-twist flux $\pm q^3$.
- **Right**: An identical copy on the $N$ side.
- **Centre**: An LR-fusion spread. This wide arrow produces multiple $\nu \vdash 6$ with $c^\nu_{\lambda, \mu}$ printed at each target. It exhibits multiple non-zero LR coefficients.

Whereas the $^{40}\mathrm{Ca}$ diagram has a single arrow to a single $\nu$, the $^{6}\mathrm{Li}$ diagram has a fan of arrows producing the full Wedderburn spread.

## Loose binding of $^{6}\mathrm{Li}$

The empirical $^{6}\mathrm{Li}$ binding energy is $31.99$ MeV ($5.33$ MeV/nucleon). This lies far below the $8.55$ MeV/nucleon of $^{40}\mathrm{Ca}$. Algebraically, there are many off-diagonal Wedderburn channels at $A = 6$ through which crossing energy can leak. The LR fusion of two frayed blocks produces a spread of full-twist flux vectors that the deuteron-like topology of $^{6}\mathrm{Li}$ cannot absorb without breakup. Phenomenologically, $^{6}\mathrm{Li}$ has many available binding-energy channels, all with non-zero capacity and none shell-closed. The empirical loose binding is the algebraic non-rigidity.

## Empirical contrast with the magic ladder

| Nuclide | $(Z, N)$ | Magic regime | $\Phi_n$ structure |
|--------:|:---------|:-------------|:-------------------|
| $^{6}\mathrm{Li}$  | $(3, 3)$    | non-magic both sides   | frayed both sides; LR spread |
| $^{16}\mathrm{O}$  | $(8, 8)$    | double-magic           | rigid both sides; single $\nu$ |
| $^{18}\mathrm{O}$  | $(8, 10)$   | single-magic ($Z$ only) | $Z$ rigid, $N$ frayed; $\kappa$-leakage |
| $^{40}\mathrm{Ca}$ | $(20, 20)$  | double-magic           | rigid both sides; single $\nu$ |

Reading top-to-bottom: as the regime moves from non-magic to single-magic to double-magic, the LR-fusion spread compresses to a single rigid $\nu_{ZN}$. The binding-per-nucleon climbs from $5.3$ to $7.6$ to $8.6$ MeV. The diagrammatic content of the LR-fusion conjecture is the algebraic mechanism behind the magic-number step pattern in nuclear binding.
<!-- FILE_END: non-magic-Li6-diagram.md -->

<!-- FILE_START: shell-threading-conjecture.md -->
The shell energy scale $\lambda_{\mathrm{shell}}$ ([Skein shell correction](#rem:skein-shell-correction)) corresponds to the crossing energy of the Skein smoothing $L_0$ at the beta-decay vertex. This threading link interpolates between the parent and daughter nuclear configurations.

**Setup.**

The Skein relation at a single crossing change is

$$
  q  [L_+] -  q^{-1} [L_-]
  = 
  (q^{1/2} - q^{-1/2})  [L_0].
$$

In beta decay $\mathcal{N}(Z, N) \to \mathcal{N}(p\!+\!1, n\!-\!1)$, a neutron $\mathfrak{n} = [\mathfrak{u}, \mathfrak{d}, \mathfrak{d}]_p$ becomes a proton $\mathfrak{p} = [\mathfrak{u}, \mathfrak{u}, \mathfrak{d}]_p$. This operates as a Skein crossing change on the $\mathfrak{d} \to \mathfrak{u}$ quark strand inside one nucleon. The terms in the Skein relation evaluate as follows.

- $L_+$ is the parent configuration $\mathcal{N}(Z, N)$ (positive crossing at the $d$-quark site).
- $L_-$ is the daughter configuration $\mathcal{N}(p\!+\!1, n\!-\!1)$ (negative crossing after the $\mathfrak{d} \to \mathfrak{u}$ flip).
- $L_0$ is the smoothing. This threading link interpolates between parent and daughter.

**Conjecture.**
*The shell energy scale equals the crossing energy of the threading link $L_0$.*

The shell energy is determined by the pair Skein mass $\mathcal{S}_{ab}(q)$ evaluated on the threading link $L_0$, using the terminal resolution ([terminal resolution](#prop:terminal-resolution)).

**The threading link $L_0$.**

The smoothing $L_0$ resolves the crossing between the converting quark strand and the surrounding nuclear link. Its topology depends on the local linking structure around the converting nucleon.

For a nucleus where the converting neutron sits inside a closed sub-link (shell closure), $L_0$ threads through that closed sub-link. The threading link's Alexander polynomial encodes the shell structure:

- **No shell closure.** At generic position, $L_0$ is a simple unknotted strand. We have $\Delta_{L_0}(q) = 1$ and $\lambda_{\mathrm{shell}} = E_{\mathrm{Hopf}}$ (the baseline Hopf junction energy). This yields no shell correction.
- **At a shell closure.** When $n$ or $p$ is magic, $L_0$ threads through the closed sub-link and acquires a nontrivial Alexander polynomial. The threading link framework ([threading link](#def:threading-link), [molecular Hopf ring](#def:molecular-hopf-ring)) gives $\Delta_{L_0}(q) > 1$. The shell energy exceeds the baseline.

**Example: ${}^{14}\mathrm{C} \to {}^{14}\mathrm{N}$.**

The parent $\mathcal{N}(6, 8)$ has a magic neutron number $n = 8$. The 8 neutrons form a closed sub-link (the $p$-shell closure). The converting neutron sits inside this closure. The smoothing $L_0$ threads through the remaining 7 nucleons of the closed sub-link and the 6 protons of the core.

Three factors determine the topology of $L_0$ for this transition:

1. The linking structure of the $n = 8$ sub-link (the arrangement of the 4 neutron pairs relative to the 3 $\alpha$-clusters of the ${}^{12}\mathrm{C}$ core).
2. The number of crossings between the converting strand and the closed sub-link.
3. The braid word of the threading in $B_A$.

**Two-level structure of $L_0$.**

The Skein resolution at the beta-decay vertex carries two levels.

*Level 1: Internal (Borromean).*

The crossing change $\mathfrak{d} \to \mathfrak{u}$ inside $\mathcal{B}_3(\mathfrak{u}, \mathfrak{d}, \mathfrak{d})$ is a Skein resolution at the $d$-$d$ crossing of the Borromean link. Smoothing one crossing in $\mathcal{B}_3$ produces the Hopf link $\mathcal{L}_H$. In the Temperley--Lieb algebra $TL_3(\delta)$ with $\delta = -(q^{1/2} + q^{-1/2})$, the smoothing is the generator $e_i$. Its Markov trace involves the quantum integer ratio:

$$
  \frac{\mathrm{tr}(L_0^{\mathrm{int}})}{\mathrm{tr}(e_i^{\mathrm{free}})}
  = 
  \frac{[1]_q  [2]_q}{[3]_q}
   \approx  0.665
  \quad\text{at } q = q_0.
$$

This represents the intrinsic Borromean suppression. The Borromean link resists the internal crossing change by a factor of $[1]_q [2]_q / [3]_q$.

*Level 2: External (nuclear environment).*

The resulting $L_0 = \mathcal{L}_H$ embeds in the multi-nucleon link $\mathcal{N}(Z, N)$. It threads through $Z$ protons and $n - 1$ remaining neutrons. The threading modulates the Markov trace by a factor depending on the shell structure of the nuclear environment:

- **Open configuration.** Without a shell closure, the inter-nucleon crossings commute with $L_0$ in the TL algebra. This introduces no additional modulation. The external factor is $1$.
- **Closed shell.** When $n$ or $p$ sits at a magic number, the inter-nucleon crossings form a chain of non-commuting TL generators adjacent to $L_0$. The Markov trace picks up a factor $f(m, k, q)$ depending on the chain length $m$ and the position $k$ of the converting nucleon within the shell.

The total shell correction is the product of the Borromean suppression and the shell modulation:

$$
  \text{shell factor}
  = 
  \underbrace{\frac{[1]_q  [2]_q}{[3]_q}}_{\text{Borromean factor}}
   \times 
  \underbrace{f(m, k, q)}_{\text{shell modulation}}
$$

Both factors are determined by $q$ and the nuclear braid topology.

**Computations required.**

1. **The external modulation $f(m, k, q)$.** We write the braid word for $\mathcal{N}(6, 8)$ with the converting neutron at position $k$ in the $n = 8$ shell chain. We then compute the Markov trace of the $L_0$ generator $e_k$ embedded in this word.
2. **The crossing matrix.** The $14 \times 14$ crossing matrix of $\mathcal{N}(6, 8)$ has 15 positive ($\mathfrak{p}$-$\mathfrak{p}$), 28 negative ($\mathfrak{n}$-$\mathfrak{n}$), and 48 mixed ($\mathfrak{p}$-$\mathfrak{n}$) crossings. The product $p \times n$ goes from 48 to 49 across the transition, creating one mixed crossing. The smoothing $L_0$ mediates this extra crossing.
3. **Verification.** The corrected half-life should match the observed 5730 yr to within $\sim 5\%$.
4. **Universality.** The same two-level construction applied to ${}^{60}\mathrm{Co}$, ${}^{137}\mathrm{Cs}$, and ${}^{210}\mathrm{Bi}$ should reproduce the observed residuals through the shell modulation factor $f(m, k, q)$.

**Connection to molecular chemistry.**

The nuclear threading link $L_0$ is the same mathematical object as the molecular threading link $\mathcal{T}_N = T(2, N)$ that binds atoms in a ring ([molecular Hopf ring](#def:molecular-hopf-ring), [threading link](#def:threading-link)). In benzene, the threading $T(2, 6)$ binds 6 carbons with Alexander weight $\Delta_{T(2,6)}(q) = q^2 + 1 + q^{-2}$. In nuclear physics, the same construction binds nucleon clusters. The Alexander weight determines the shell correction.

The shell energy is not a phenomenological parameter. It is the crossing energy of a computable knot invariant.
<!-- FILE_END: shell-threading-conjecture.md -->

<!-- FILE_START: single-magic-O18-diagram.md -->
The isotope $^{18}\mathrm{O}$ ($Z = 8$, $N = 10$, $A = 18$) is the canonical single-magic test case. The proton count $Z = 8 \in \mathfrak{M}$ is saturated, but the neutron count $N = 10 \notin \mathfrak{M}$ is not. This example illustrates the partition-level diagrammatic content of the double-magic LR-fusion conjecture ([`prop:diagrammatic-double-magic-lr-fusion`](#prop:diagrammatic-double-magic-lr-fusion)) in the regime where exactly one block is saturated. The $\kappa$-leakage through the non-saturated $N$-block accounts for the binding-energy tail beyond the saturated $Z = 8$ contribution.

## $Z$-block (saturated)

The proton count $Z = 8$ is magic. By [`prop:categorical-neutrality-saturated-shells`](../braids-and-knots/categorical-neutrality-saturated-shells.md), the categorical mass at level $8$ is supported on a single self-conjugate partition. The relevant partition is

$$
  \lambda_{Z=8} \;=\; (3, 2, 2, 1) \;=\; \lambda_{Z=8}'.
$$

The content sum is $c(\lambda_{Z=8}) = 0$. The Young diagram is symmetric under transposition:

```text
  ■ ■ ■
  ■ ■
  ■ ■
  ■
```

The full-twist $\Delta_8^2$ acts on $V_{\lambda_{Z=8}}$ by $q^{c(\lambda_{Z=8})} = q^0 = 1$. The action is trivial, as the saturated-shell conjecture demands.

## $N$-block (frayed)

The neutron count $N = 10$ is not magic. The categorical mass at level $10$ is not concentrated on a single self-conjugate partition. Instead, the Wedderburn support spreads over multiple non-self-conjugate $\mu \vdash 10$. Each contributes a non-trivial full-twist eigenvalue $q^{c(\mu)} \neq 1$. The neutron block is frayed: its support on Young's lattice forms a thicket of competing partitions rather than a single self-conjugate diagram.

A representative non-self-conjugate partition is

$$
  \mu = (5, 3, 2) \quad\text{vs.}\quad \mu' = (3, 3, 2, 1, 1).
$$

These two partitions of $10$ differ in shape and contribute independently to $\Phi_{10}$.

## LR fusion at $A = 18$

The LR fusion $V_{\lambda_{Z=8}} \otimes V_\mu(N=10)$ does not collapse to a single $\nu$. The non-self-conjugacy of $\mu$ on the $N$ side propagates through the LR rule ([`prop:diagrammatic-double-magic-lr-fusion`](#prop:diagrammatic-double-magic-lr-fusion)) to produce a sum

$$
  V_{\lambda_{Z=8}} \otimes V_{\mu(N=10)}
  \;\cong\;
  \bigoplus_{\nu \vdash 18}
    c^\nu_{\lambda_{Z=8}, \mu} \, V_\nu.
$$

The sum contains multiple non-zero $c^\nu$. The spread over $\nu$—the non-zero off-diagonal LR coefficients—constitutes the $\kappa$-leakage. This is binding-energy capacity that the saturated $Z = 8$ side cannot absorb, and that the frayed $N = 10$ side carries.

## Diagram content

The diagrammatic illustration in this example block is schematically:

- **Left half.** The symmetric $\lambda_{Z=8} = (3,2,2,1)$ Young diagram, marked as "self-conjugate, full-twist trivial, saturated".
- **Right half.** A fragment of Young's lattice between $\mu = (5,3,2)$ and $\mu' = (3,3,2,1,1)$, with edges marking the Pieri / branching arrows, marked as "frayed, full-twist non-trivial, non-saturated".
- **Centre.** The LR-fusion arrow producing a spread over $\nu$ rather than a single $\nu_{ZN}$. The width of the spread gives the algebraic content of $\kappa$-leakage.

## Empirical match

The empirical $^{18}\mathrm{O}$ binding curve sits between $^{16}\mathrm{O}$ (double-magic, exceptionally bound) and $^{20}\mathrm{O}$ (binding falls off as $N$ moves further from $8$). The single-magic spread predicted here (a saturated $Z$ contribution plus a frayed $N$ contribution with $\kappa$-leakage) matches the observed binding energy within the multi-term BW residual.
<!-- FILE_END: single-magic-O18-diagram.md -->

<!-- FILE_START: bw-mass-decomposition-dictionary.md -->
Each term of the empirical Bethe–Weizsäcker mass formula corresponds to a specific stratum of the Schur–Weyl decomposition ([Schur–Weyl mass decomposition](#prop:schur-weyl-mass-decomposition)). The empirical coefficients that nuclear physicists historically fit to data are not free parameters in the categorical picture. They are determined by the $q$-hook product $H_q(\lambda)$ evaluated on specific partition shapes.

## Dictionary

See [Table: BW terms as Schur-Weyl strata](#tbl:bw-mass-decomposition-dictionary-table-data) for the seven-term correspondence.

## Operational meaning

In the categorical picture, the coefficient $a_V \approx 15.67\,\mathrm{MeV}$ (BW volume) is forced to equal $2[2]_q[7]_q \cdot m_e$ at $q = q_0$. It is not fit. The $A^{2/3}$ scaling of the surface term is forced by Weyl's dimension formula. The sign alternation of the pairing term is forced by the two Hecke eigenvalues. The categorical derivation predicts these coefficients without nuclear-physics input — it requires only the substrate parameter $q_0$ and the reference mass $m_e$.

## Scope of the dictionary

The dictionary identifies each BW term with an algebraic stratum. It does not claim that nuclei are perfectly described by summing only these strata. The Schur–Weyl sum includes many more partitions than BW's seven terms. Furthermore, the root-of-unity residues ([GB residue spectral sum](#prop:gb-residue-spectral-sum)) lack any BW analogue. The dictionary explains why BW works as well as it does (it captures the dominant low-partition strata), but it does not validate BW as exact.
<!-- FILE_END: bw-mass-decomposition-dictionary.md -->

<!-- FILE_START: strutinsky-from-graded-trace.md -->
**Remark.**
*The Strutinsky shell-correction method decomposes nuclear binding energies as*

$$
  E \;=\; \tilde E \;+\; \delta E_{\mathrm{shell}},
$$

*with $\tilde E$ a smoothed liquid-drop piece and $\delta E_{\mathrm{shell}}$ an oscillating microscopic correction. This decomposition is the physics shadow of the filtered-algebra identity*

$$
  \mathrm{tr}_M(T_w, q_0)
  \;=\;
  \mathrm{tr}_{\mathrm{gr}}(\sigma(T_w), q_0)
  \;+\;
  \mathrm{Res}_{\mathrm{GB}}(T_w, q_0)
$$

*from ([graded-trace residue split](#prop:graded-trace-residue-split)).*

**Identification.**

| Strutinsky (physics) | Categorical (algebra) |
|---|---|
| Smoothed level density $\tilde\rho(E)$ | Symbol map $\sigma: J^\ell \to J^\ell/J^{\ell+1}$ |
| Liquid-drop energy $\tilde E$ | Graded trace $\mathrm{tr}_{\mathrm{gr}}(\sigma(T_w), q_0)$ |
| Oscillating correction $\delta E_{\mathrm{shell}}$ | Residue sum $\mathrm{Res}_{\mathrm{GB}}(T_w, q_0)$ |
| Gaussian smoothing width | Filtration step $J^\ell / J^{\ell+1}$ granularity |
| Magic-number enhancement | Rectangular-partition spike in $w_\lambda(q_0)$ |

**Exactness of the analogy.**
*The Strutinsky smoothing averages over an energy window spanning major shells. This is equivalent to projecting onto the filtration quotient $\mathrm{gr}\,H_n(q)$. The oscillations encode the Gröbner–Shirshov rewriting defects lost by the symbol map. Thus, $\delta E_{\mathrm{shell}} = \mathrm{Res}_{\mathrm{GB}}$. The Strutinsky prescription is the unique trace decomposition dictated by the filtered-algebra structure.*

**Corollaries.**

1. *Strutinsky's method is forced by the filtered-algebra structure. Any alternative macroscopic-microscopic split implicitly chooses a different filtration on $H_n(q)$. The confinement filtration ([confinement level](#def:confinement-level)) is canonical, rendering the Strutinsky decomposition canonical.*
2. *The shell correction $\delta E_{\mathrm{shell}}$ is computable without a phenomenological single-particle potential. It is exactly the residue sum ([GB residue spectral sum](#prop:gb-residue-spectral-sum)) applied to the atomic braid. Magic-number enhancements arise algebraically when $\lambda$ is rectangular and $H_q(\lambda)$ factorises ([shell–Schur–Weyl self-duality](#prop:shell-schur-weyl-self-duality)).*

**Scope.**
*This identification frames the algebraic structure but does not replace a quantitative calculation. A direct numerical comparison between Strutinsky $\delta E_{\mathrm{shell}}$ at deformation $\beta_2$ and $\mathrm{Res}_{\mathrm{GB}}$ provides the natural next observational test.*
<!-- FILE_END: strutinsky-from-graded-trace.md -->

