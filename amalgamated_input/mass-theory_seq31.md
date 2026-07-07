<!-- FILE_START: nuclear-binding-beta-stability-intro.md -->
The confinement filtration of the previous section fixed which knot operators are admissible. We now ask which of them actually bind. The binding mechanism is a character-ratio decomposition per jet level; the level-$\ell$ coefficient is the LP-dual variable of a Frobenius-positivity constraint, with cost given by the $\ell$-th elementary symmetric polynomial in the Jucys--Murphy elements. The resulting iterative LP-dual recursion replaces seven ad-hoc mass-formula terms with a single recursion, and the beta-stability valley falls out as the level set of the Skein binding Lagrangian.

The opening triad sets the binding mechanism. Proposition: Confined knot binding mechanism: character ratio decomposition per jet level names the per-level decomposition, Definition: Jet-filtered knot factor and Proposition: Jet-convergence classical limit supply the filtration and its convergence, and Remark: Wigner $np$-pairing records the empirical pairing pattern. The structural pivot is the trio Proposition: Canonical q-deformed Wedderburn-block weight $\tilde w_\lambda$ and named scalings (BW, LP for all $\lambda$; Wenzl-bridge on the self-conjugate stratum), Proposition: Hook-weight derivation, and Proposition: Mass coefficient as LP shadow price, which identify each Wedderburn weight as an LP shadow price. Proposition: Frobenius self-duality forces LP-dual extraction and Proposition: Elementary symmetric polynomials in Jucys--Murphy elements are central in $H_n(q)$ with closed-form spectrum on each Wedderburn block supply the central elements, and Proposition: QOU mass formula as iterative LP-dual compiles them into the iterative recursion.

The body unwinds the corrections. Proposition: Schur--Weyl mass decomposition, Proposition: Mass spectrum generating function, and the graded Markov-trace blocks fix the analytic structure. The conditional blocks Proposition: Categorical mass positivity, the Gröbner--Shirshov existence and trace-decomposition conjectures, Theorem: Frobenius codimension universal, Theorem: Knot mass formula unified, and Theorem: Six-term mass formula complete close the algebraic chain. Spectral structure is added in Proposition: GB spectral sequence, Proposition: Curvature-rank GB stratification, and Proposition: Spectral sequence collapse, with Proposition: Universal residue at curvature-rank $k \geq 4$ (q-deformed Wedderburn-weighted log functional), the Proposition: E-infinity page identifications, and Proposition: Chirality-writhe-ribbon derivation supplying the closed-form residue terms. The knot-factor blocks — amphicheiral, Borromean composite, shell-closed, spectral summary — and the Pauli-factor Wedderburn block complete the bookkeeping.

The closing arc connects mass to beta stability. Proposition: $\alpha_k$ derivation procedure and Proposition: $\alpha_k$ categorical closure reduce every per-block coefficient to a derivable q-rational; Proposition: Closed form for Jones-Markov $y_\lambda$ via Wenzl Schur-element bridge and its cyclotomic factorisation, together with Proposition: Macdonald hook telescope and Proposition: Wedderburn-Bratteli recursion, supply the explicit telescope. The atom-knot mass derivation closes the chain to physical masses, Proposition: Plancherel weight boundedness anchors the trace expansion analytically, and Proposition: Joint tower SDP confinement packages the operator-selection LP. The section ends with Proposition: Energy scale Planck, Example: Topological mass of the trefoil knot (electron), Definition: Skein binding Lagrangian, and Proposition: Beta-stability line from the Skein binding Lagrangian together with its interpretation. The next section, **Pre-Archimedean Derivation Chain and Audit**, takes the unified mass formula and beta-stability line as fixed and audits every conditional step in the derivation chain.
<!-- FILE_END: nuclear-binding-beta-stability-intro.md -->

<!-- FILE_START: confined-knot-binding.md -->
**Proposition.**
*Let $\beta \in H_3(R, q)$ be a confined nuclear braid
([atomic braid](#def:atomic-braid)) — typically
$\beta = T_w = \mathtt{atom\_braid\_word\_3A}(Z, N)$
(the canonical formalism)
— built from crossing operators
$c_k \sigma_{i_k} + d_k \cdot 1 \in H_3(R, q)$ at generators
$\sigma_{i_k}$ with parameters $(c_k, d_k)$ (the $k$-th letter of
$T_w$ in its GB normal form). The Wedderburn-Artin decomposition
([three-parameter decomposition](#prop:three-parameters-wedderburn))
separates each crossing's contribution into three channels:*

$$
  \hat{V}(c, d)
  = W_{\mathrm{sym}} \cdot \chi_{\mathrm{sym}}(c, d)
  + W_{\mathrm{std}} \cdot \chi_{\mathrm{std}}(c, d)
  + W_{\mathrm{alt}} \cdot \chi_{\mathrm{alt}}(c, d)
$$

*where the Wedderburn weights are:*

$$
  W_{\mathrm{sym}} = W_{\mathrm{alt}}
  = \frac{q^2}{q^4 + 4q^2 + 1},
  \qquad
  W_{\mathrm{std}}
  = \frac{(q^2 + 1)^2}{q^4 + 4q^2 + 1}
$$

*and the channel characters are:*

$$
  \chi_{\mathrm{sym}}(c, d) = cq + d,
  \quad
  \chi_{\mathrm{alt}}(c, d) = -\frac{c}{q} + d,
  \quad
  \chi_{\mathrm{std}}(c, d) = z \cdot a + b
$$

*with $(a, b)$ accumulated via the transfer-matrix recurrence
$\bigl[\begin{smallmatrix} a' \\ b' \end{smallmatrix}\bigr]
= \bigl[\begin{smallmatrix} cH_A + d & c \\ c & d
\end{smallmatrix}\bigr]
\bigl[\begin{smallmatrix} a \\ b \end{smallmatrix}\bigr]$,
$H_A = q - q^{-1}$, $z = 1/(\sqrt{q} + 1/\sqrt{q})$.*

**Extremal cancellation (symmetric crossings).**
*For any crossing with $d = -H_A/2$ (the symmetric mixing
$\tfrac{1}{2}(\sigma + \sigma^{-1})$, which encodes the
proton-neutron nuclear force):*

$$
  \chi_{\mathrm{sym}} = \frac{q^2 + 1}{2q},
  \qquad
  \chi_{\mathrm{alt}} = -\frac{q^2 + 1}{2q}
$$

*Since $W_{\mathrm{sym}} = W_{\mathrm{alt}}$, the extremal
contributions cancel exactly:*

$$
  W_{\mathrm{sym}} \cdot \chi_{\mathrm{sym}}
  + W_{\mathrm{alt}} \cdot \chi_{\mathrm{alt}} = 0
$$

*The binding volume of a symmetric crossing is carried entirely
by the standard representation:*

$$
  \hat{V}_{\mathrm{pn}}
  = W_{\mathrm{std}} \cdot \Bigl(z - \frac{H_A}{2}\Bigr)
$$

**Cross-channel interaction (adjacent generators).**
*The symmetric and alternating representations are $1$-dimensional,
so products of consecutive crossings on the same generator are
scalar: $\chi_{\mathrm{sym}}(\beta) = \prod_k (c_k q + d_k)$.
The standard representation is $2$-dimensional — consecutive
crossings compose as $2 \times 2$ matrix products:*

$$
  M_i = \prod_k \begin{pmatrix}
    c_k H_A + d_k & c_k \\ c_k & d_k
  \end{pmatrix}
$$

*This non-commutativity produces the cross-channel term between
adjacent generators $i$ and $i{+}1$, weighted by the Markov
parameter $z^2 = \mathrm{tr}_M(\sigma_i \sigma_{i+1})$:*

$$
  \delta_{\times}
  = z^2 \sum_{|i-j|=1}
    \ln\bigl\lvert
      \hat{V}_i^{\mathrm{full}} \cdot \hat{V}_j^{\mathrm{full}}
    \bigr\rvert
$$

*The weight $z^2$ is derived from the Hecke algebra (not fitted):
it is the Markov trace of the adjacent generator product
$\mathrm{tr}_M(\sigma_0 \sigma_1) = z^2$.*

**General confined-state character ratio.**
*For an $A$-nucleon system with construction at jet levels
$\ell = 0$ (quark), $\ell = 1$ (nucleon), $\ell = 2$ (nucleus),
the knot factor at each level is the character ratio:*

$$
  a_\ell
  = \frac{\hat{V}_\ell(\text{confined})}
         {\hat{V}_\ell(\text{free})}
$$

*measuring how the confined state's Wedderburn volume departs from
the free constituent product at that jet level.  The total knot
factor is:*

$$
  a(Z, N) = \prod_\ell a_\ell
$$

*This product emerges from the algebraic structure of $H_3(R, q)$ —
the character ratios are functions of $q$ alone, with no empirical
input.*
<!-- FILE_END: confined-knot-binding.md -->

<!-- FILE_START: molecular-bond-binding-from-trefoil-insertion.md -->
**Proposition (molecular bond binding energy from inverse-trefoil insertion).**
*The Wedderburn-channel decomposition of
[prop:confined-knot-binding](#prop:confined-knot-binding) applies at
the molecular level.  A covalent bond is an inverse trefoil $T^{-1}$
inserted between two atomic braids $\mathcal{A}$, $\mathcal{B}$.  The
molecular binding energy is:*

$$
  E_{\mathrm{bond}}
  = \bigl(
      W_{\mathrm{sym}} \cdot \Delta\Phi_{\mathrm{sym}}
    + W_{\mathrm{std}} \cdot \Delta\Phi_{\mathrm{std}}
    + W_{\mathrm{alt}} \cdot \Delta\Phi_{\mathrm{alt}}
    \bigr) \times E_{\mathrm{mol}}
$$

*where $\Delta\Phi_\lambda = \bigl\lvert
\ln|\chi_\lambda(\mathcal{A} \cdot \mathcal{B})|
- \ln|\chi_\lambda(\mathcal{A} \cdot T^{-1} \cdot \mathcal{B})|
\bigr\rvert$
is the per-channel volume shift from inserting the bond, and
$E_{\mathrm{mol}} = m_e \alpha^2 / 2$ is the Hartree energy
scale (derived from $q$).  Double and triple bonds use $n$
inverse trefoils: $\Delta\Phi \propto n$, so bond energies
scale as $1 : 2 : 3$.*
<!-- FILE_END: molecular-bond-binding-from-trefoil-insertion.md -->

<!-- FILE_START: jet-filtered-knot-factor.md -->
**Conjecture.**
*Let $\beta(Z, N)$ be the nuclear braid of an $(Z, N)$ atom
([atomic braid](#def:atomic-braid)), and let $a(Z, N)$ be the
Bethe--Weizsäcker knot factor that multiplies the bulk binding
$B_{\mathrm{bulk}}$.  Then $a(Z, N)$ is determined by the
**jet-filtered character convergence** of the nuclear quotient
braid $\bar\beta$, obtained by collapsing each nucleon to its
Wedderburn trace.*

**Part 1 (Established).** *At each jet level $k \geq 3$, define
the per-level knot invariant*

$$
  a_k(\beta)
  = \frac{\sum_\lambda w_\lambda \,
    \chi_\lambda^{(k)}(\beta)}
  {\sum_\lambda w_\lambda \,
    \dim \mathrm{Res}^{H_k}_{H_3}(V_\lambda)}
$$

*where $w_\lambda = d_q(\lambda)^2/[k]_q!$ are the Wedderburn
weights and $\chi_\lambda^{(k)}(\beta)$ is the character of
$\beta$ in $V_\lambda$ restricted to $H_3(R, q)$ via the branching
rule.*

*Then $a_k$ **converges by $k = 4$**: for all $k \geq 4$, the
ratio $a_k$ is topology-independent (depends on $q$ but not on
$(Z, N)$ beyond the $H_3$ characters of $\beta$).*

*The denominator simplifies:
$\sum_\lambda w_\lambda \dim \mathrm{Res} = 1 + W_{\mathrm{std}}$
where $W_{\mathrm{std}} = (q^2 + 1)^2/(q^4 + 4q^2 + 1)$.*

**Part 2 (Established).** *The three $H_3(R, q)$ characters of the
inter-nucleon braid satisfy exact algebraic identities:*

1. *Extremal cancellation
  ([confined knot binding](#prop:confined-knot-binding)):
  for each proton-neutron crossing,
  $W_{\mathrm{sym}} \chi_{\mathrm{sym}} +
   W_{\mathrm{alt}} \chi_{\mathrm{alt}} = 0$.*

2. *Crossing balance: $\hat{V}_{\mathrm{pp}} +
  \hat{V}_{\mathrm{nn}} = 2\hat{V}_{\mathrm{pn}}$ exactly,
  where $\hat{V}_{xy}$ is the Wedderburn volume of a single
  $xy$-crossing.  The deviation is
  $\delta V = \hat{V}_{\mathrm{pp}} - \hat{V}_{\mathrm{pn}}
  = h/2$ (half the Hecke parameter).*

3. *For $Z = N$ even-even nuclei ($\mathrm{sp} = \mathrm{ap}
  = V_{\mathrm{std}}^{\mathrm{inter}}$):
  $a_k = V_{\mathrm{std}}^{\mathrm{inter}} / (1 + W_{\mathrm{std}})$.*

4. *For $Z = N$ odd-odd nuclei ($\mathrm{sp} = -\mathrm{ap}$,
  extremal cancellation):
  $a_k = W_{\mathrm{std}} \cdot V_{\mathrm{std}}^{\mathrm{inter}}
  / (1 + W_{\mathrm{std}})$.*

**Part 3 (Intermediate knot detection).** *During nucleon-by-nucleon
construction of $\beta(Z, N)$, the intermediate NF at each step
$A' \leq A$ matches a reference knot pattern (trefoil, Hopf link,
figure-eight, unknot) with measurable cosine similarity.  For $Z = N$
nuclei, the pattern **alternates**: trefoil at odd $Z$, Hopf link at
even $Z$.  Double-magic nuclei (${}^{16}\mathrm{O}$) converge to the
**unknot** ($\cos \approx 0.66$).*

**Part 4 (Conjecture).** *The BW knot factor $a(Z, N)$ is the
Jones polynomial of the **nuclear quotient braid** $\bar\beta$,
evaluated at $q$:*

$$
  a(Z, N) = J_{\bar\beta}(q)
$$

*where $\bar\beta$ is the braid obtained from $\beta(Z, N)$
by collapsing each nucleon (B$_{3}$ confinement + quark crossings +
gluon dressing) to a single effective crossing, retaining only
the inter-nucleon topology.*

*For known knot types:*

| $A$ | Quotient braid | $J(q)$ | Verified |
|-----|---------------|--------|----------|
| $2$ | single pn crossing | $1$ (satellite) | $\checkmark$ |
| $3$ | figure-eight $4_1$ | $1 - h^2$ | $\checkmark$ |
| $4$ | Borromean $B_3^2$ | $(1 - h^2)^2$ | $\checkmark$ |
| $\geq 5$ | quotient nuclear braid | $J_{\bar\beta}(q)$ | **open** |

*The quotient braid $\bar\beta$ for $A \geq 5$ involves
$\binom{A}{2}$ inter-nucleon crossings of types pp, nn, pn.
Its Jones polynomial is a Laurent polynomial in $q$, computable
from the transfer matrix $V_{\mathrm{std}}$ of the inter-nucleon
crossing chain.  The conjecture asserts that this polynomial,
properly normalised, gives the BW knot factor.*

*Evidence: for ${}^6\mathrm{Li}$, the needed knot factor
$a \approx 1.134$ satisfies
$(1 - h^2)^2 \cdot (1 + h^2)^5 \approx 1.133$ — suggestive of
$2$ amphicheiral channels (from the ${}^4\mathrm{He}$ core) and
$5$ chiral channels (from the additional pn structure).  The
exponent $5$ and its algebraic origin are open.*

*The **NF transition lifting** approach (tracking how the NF
changes at each nucleon addition and using the transition element
to weight confinement channels) provides a potential path to a
closed-form recursive formula.*

**Witness**: `jet-knot-invariants.witness.json`,
`intermediate-knot-detection.witness.json`.
<!-- FILE_END: jet-filtered-knot-factor.md -->

<!-- FILE_START: jet-convergence-classical-limit.md -->
**Conjecture (exact at $k = 3$, convergence at $k > 3$ conditional on conj:jet-filtered-knot-factor).**

**Part A (Proved).** *At $k = 3$, the jet-filtered knot invariant
is exact:*

$$
  a_3(\beta)
  = \frac{W_{\mathrm{sym}} \, \chi_{\mathrm{sym}}
    + W_{\mathrm{std}} \, \chi_{\mathrm{std}}
    + W_{\mathrm{alt}} \, \chi_{\mathrm{alt}}}
  {1 + W_{\mathrm{std}}}
$$

*where $W_\lambda = d_q(\lambda)^2 / [3]_q!$ are the $q$-deformed
Wedderburn weights.  The denominator simplifies because
$W_{\mathrm{sym}} + 2 W_{\mathrm{std}} + W_{\mathrm{alt}} =
1 + W_{\mathrm{std}}$.*

*Proof.* Direct computation from the Wedderburn-Artin
decomposition $H_3(R, q) \cong M_1 \oplus M_2 \oplus M_1$
with weights $W_\lambda$ and restricted characters
$\chi_\lambda(\beta)$. $\square$

**Part B (Proved).** *The branching multiplicities
$m_\mu^\lambda = \#\mathrm{SYT}(\lambda/\mu)$ are $q$-independent
(purely combinatorial).  They satisfy the classical dimension
identity $\sum_\mu m_\mu^\lambda \dim(\mu) = \dim(\lambda)$ at
$q = 1$, but the $q$-deformed version*

$$
  \sum_\mu m_\mu^\lambda \, d_q(\mu) \neq d_q(\lambda)
  \quad\text{for } k \geq 4
$$

*fails with error $O(h^2)$ per skew cell.  This is because the
$q$-hook formula for $d_q(\lambda)$ involves content-dependent
$q$-corrections that do not factorise over the branching.*

**Part C (Convergence to $q$-deformed dimensions).**
*The per-level invariant $a_k(\beta)$ converges as $k \to \infty$
to the $q$-dimension-weighted average:*

$$
  a_\infty(\beta)
  = \frac{\chi_{\mathrm{sym}} + \chi_{\mathrm{alt}}
    + d_q((2{,}1)) \cdot \chi_{\mathrm{std}}}
  {2 + d_q((2{,}1))^2}
$$

*where $d_q((2{,}1)) = [2]_q = q + q^{-1}$.
The asymptotic branching fractions are:*

$$
  f_\mu^\infty = \frac{d_q(\mu)}{\sum_\nu d_q(\nu)}
  = \frac{d_q(\mu)}{2 + [2]_q}
$$

*transitioning from the $k = 3$ Wedderburn weights
$W_\mu = d_q(\mu)^2/[3]_q!$ (squared scaling) to the
$k = \infty$ linear scaling $d_q(\mu)/\sum d_q(\nu)$.*

*Proof sketch.*
In the seminormal basis of $H_k(R, q)$, each standard Young
tableau $t$ of shape $\lambda$ restricts to $H_3$ by
reading its first $3$ entries, giving a SYT of shape $\mu$.
The branching multiplicity $m_\mu^\lambda = \#\mathrm{SYT}(\lambda/\mu)$
is $q$-independent.

For the $q$-Plancherel measure $w_\lambda = d_q(\lambda)^2/[k]_q!$:
the ``typical'' partition $\lambda$ (concentrating the measure)
has $d_q(\lambda) \approx \dim(\lambda) \cdot (1 + O(h^2/k))$,
The weighted branching is dominated by the first-order
$q$-correction to the classical Plancherel branching.

The classical Plancherel branching gives
$f_\mu^{(1)} = \dim(\mu)/4$, and the leading $q$-correction is
$f_\mu = \dim(\mu)/4 + (d_q(\mu) - \dim(\mu)) \cdot C_k$
where $C_k \to 1/(4 \sum d_q)$ as $k \to \infty$, yielding
$f_\mu^\infty = d_q(\mu)/(2 + [2]_q)$.

The convergence rate is $O(1/k)$: at each jet level, the
new partitions contribute branching proportional to
$d_q(\mu)$ (first order) rather than $d_q(\mu)^2$ (zeroth order).
$\square$

*The convergence rate is $O(1/\sqrt{k})$ by the Kerov $q$-hook
walk \cite{kerov1996} and the Féray--Méliot $q$-Plancherel CLT
\cite{feray2010}: the $q$-hook walk on the Young lattice has
transition probabilities
$p(\lambda \to \lambda \setminus c) = d_q(\lambda \setminus c)^2
\cdot [h(c)]_q / d_q(\lambda)^2$
whose stationary distribution restricted to partitions of $3$ IS
$d_q(\mu)/\sum d_q(\nu)$.  Character fluctuations have variance
$O(1/k)$, giving $O(1/\sqrt{k})$ convergence.  Combined with
the ratio perturbation lemma (proved in Lean):*

$$
  \bigl\lvert f_\mu^{(k)} - f_\mu^\infty \bigr\rvert
  \leq \frac{C_q}{\sqrt{k - 3}}
$$

*where $C_q = O(h^2 \cdot [2]_q)$.  At $k = 9$:
bound $\approx 0.11$, actual error $0.008$ (well within).*

*canonical structural verification ($k = 3 \ldots 9$): the
$q$-deformed target $d_q/\Sigma d_q = (0.249, 0.501, 0.249)$
matches within $0.008$ at $k = 9$, with monotone convergence
from above for $f_{\mathrm{std}}^{(k)}$.*

**Corollaries.**

1. *For $Z = N$ even-even nuclei
  ($\chi_{\mathrm{sym}} = \chi_{\mathrm{alt}} =
  V_{\mathrm{std}}^{\mathrm{inter}} = V$):*

$$
  a_\infty = \frac{(2 + [2]_q) \cdot V}{2 + [2]_q^2}
$$

2. *For $Z = N$ odd-odd nuclei
  ($\chi_{\mathrm{sym}} = -\chi_{\mathrm{alt}}$,
  extremal cancellation
  [confined knot binding](#prop:confined-knot-binding)):*

$$
  a_\infty = \frac{[2]_q \cdot V_{\mathrm{std}}}{2 + [2]_q^2}
$$

3. *The transition $k = 3 \to k = \infty$ is from
  **squared** to **linear** $q$-dimension scaling:*

| Level | Fraction $f_\mu$ | Scaling |
|-------|------------------|---------|
| $k = 3$ | $d_q(\mu)^2 / [3]_q!$ | quadratic |
| $k \to \infty$ | $d_q(\mu) / \sum d_q(\nu)$ | linear |

*At $k = 3$: $W_{\mathrm{std}} = [2]_q^2/([2]_q^2 + 2) \approx 0.669$.
At $k = \infty$: $f_{\mathrm{std}} = [2]_q/([2]_q + 2) \approx 0.501$.
The $q$-deformation enhances the standard channel at low $k$,
explaining why nuclear topology (carried by the $2$-dimensional
standard representation) dominates binding at the physical level.*

**Witness**: `jet-knot-invariants.witness.json`.
<!-- FILE_END: jet-convergence-classical-limit.md -->

<!-- FILE_START: wigner-np-pairing.md -->
**Proposition.**
*The self-conjugate partition $(2,2) \vdash 4$ at Hecke level
$k = 4$ contributes an additional binding term for nuclei with
both protons and neutrons.  This is the categorical Wigner
energy from $T{=}0$ isoscalar np pairing, with energy scale
fixed by the $q$-hook product of $(2,2)$:*

$$
  \mathbf{\Delta}_{(2,2)}
  = m_e \cdot H_q\big((2,2)\big)
  = m_e \cdot [3]_q \cdot [2]_q^2
  \approx 6.29\;\mathrm{MeV},
$$

*matching the empirical Wigner scale $\Delta_W \approx 6.3$ MeV
\cite{satula1997} **without fitting**.  The hook lengths
$\{3, 2, 2, 1\}$ of the $2 \times 2$ Young diagram give the
product $[3]_q \cdot [2]_q \cdot [2]_q \cdot [1]_q$, which is
exactly $\mathbf{\Delta}_S = \mathbf{\Delta}_{(2,2)}$ — the
$(2,2)$ channel and the shell correction share **one**
categorical scale.*

*The binding increment is:*

$$
  \Delta B_{\mathrm{Wigner}}
  = \hat{V}_{\mathrm{pn}} \cdot \alpha
    \cdot \frac{\min(Z, N)}{A}
$$

*where:*
- *$\hat{V}_{\mathrm{pn}} = W_{\mathrm{std}} \cdot (z - H_A/2)$
  is the pn crossing volume
  ([confined knot binding](#prop:confined-knot-binding)),*
- *$\alpha = m_e \times 8G$
  ([binding scale](#prop:binding-scale-catalan)),*
- *$\min(Z, N)/A$ counts the fraction of nucleons that can form
  $T{=}0$ pairs.*

*This dedicated formulation is subsumed by the
[unified iterative $(2,2)$ correction](#prop:unified-iterative-correction),
which accumulates the Wedderburn projection step by step from
$A = 1$ — replacing $\hat V_{\mathrm{pn}} \cdot \alpha \cdot
\min(Z,N)/A$, the deuteron formula, and the knot factor by
**one** mechanism.*

*This term is:*
- *Nonzero for all nuclei with $Z \geq 1$ and $N \geq 1$,*
- *Largest for $N = Z$ (Wigner energy),*
- *Constructive from $A = 1$ upward (no conditional on $A$),*
- *Derived from the $(2,2)$ partition's Wedderburn weight, not
  fitted to data.*
<!-- FILE_END: wigner-np-pairing.md -->

<!-- FILE_START: unified-iterative-correction.md -->
**Proposition.**
*Every per-partition contribution to the binding energy is the
LP-dual shadow price of that partition's Frobenius positivity
constraint, multiplied by its $q$-hook product and accumulated
step by step from $A = 1$ over the per-step (Young seminormal)
trace of the NF transition.  No special-case branching is
required for any value of $A$.*

*The unified accumulator is, for any partition $\lambda \vdash k$
($k = 2, \ldots, K$):*

$$
  B_\lambda(Z, N)
  = m_e \cdot H_q(\lambda) \cdot u_\lambda \cdot
    \big( \ln\big| \mathrm{tr}\, \mathbf{M}_\lambda^{(0..A)} \big|
          - \ln d_\lambda \big),
$$

*and the total unified correction is the sum:*

$$
  B_{\mathrm{unified}}(Z, N) = \sum_{\lambda} B_\lambda(Z, N).
$$

*Components:*
- *$H_q(\lambda) = \prod_{x \in \lambda} [h_x(\lambda)]_q$ is the
  $q$-hook product (the categorical scale $C_\lambda = m_e \cdot
  H_q(\lambda)$ — for $\lambda = (2,2)$ this is
  $[3]_q \cdot [2]_q^2 \approx 6.29$ MeV, the empirical Wigner
  scale \cite{satula1997});*
- *$u_\lambda = w_\lambda / d_\lambda - 1/[k]_q!$ is the LP-dual
  shadow price of $\lambda$'s Frobenius positivity constraint
  ([prop:mass-coefficient-shadow-price](#prop:mass-coefficient-shadow-price));
  the constant $1/[k]_q!$ is the dual variable of the
  normalisation $\mathbf{1}^T x = n_{\mathrm{target}}$ (the
  smallest $w_\lambda / d_\lambda$ across partitions of $k$,
  attained by the trivial sym/alt one-dimensional reps);*
- *$d_\lambda = \dim(\lambda)$ is the classical dimension (number
  of standard Young tableaux);*
- *$\mathbf{M}_\lambda^{(0..A)}$ is the Young-seminormal-form
  matrix product over all NF crossings introduced through
  step $A$, embedded into the Hecke generators
  $\sigma_1, \ldots, \sigma_{k-1}$ of $H_k(R, q)$ with cyclic
  generator index.*

*One-dimensional representations have $w_\lambda / d_\lambda =
1/[k]_q!$ (so $u_\lambda = 0$); they contribute nothing to
$B_{\mathrm{unified}}$.  Only mixing partitions
($d_\lambda \geq 2$) carry shadow-price weight.*

*Per-step formulation (energy-additive, restartable witness):*

$$
  \Delta B_\lambda(\mathrm{step}\ k)
  = m_e \cdot H_q(\lambda) \cdot u_\lambda \cdot
    \Big( \ln\big| \mathrm{tr}\, \mathbf{M}_\lambda^{(0..k)} \big|
        - \ln\big| \mathrm{tr}\, \mathbf{M}_\lambda^{(0..k-1)} \big| \Big),
$$

*so witness rows
$(A, Z_k, N_k, \mathrm{nuc}, \{\Delta B_\lambda\}_\lambda,
\mathrm{cumulative})$ uniquely determine the next.*
<!-- FILE_END: unified-iterative-correction.md -->

<!-- FILE_START: knot-factor-frobenius-pairing.md -->
**Conjecture.**
*The categorical replacement for the empirical Bethe-Weizsäcker bulk
($\lambda_V \cdot A$, $\lambda_S \cdot A^{2/3}$) and the knot factor
$a(N)$ is the **mass-identity Markov-trace defect**.  Using the
categorical mass at a single brane level
([single-level Markov mass](#prop:categorical-mass-markov)):*

$$
  \mathfrak{m}(\varrho)\big|_{\text{single level}}
  \;=\; \bigl| \mathrm{tr}_M( \rho(\beta) ) \bigr|
$$

*— the categorical mass of a braid $\beta$ equals the absolute value
of its Jones–Markov trace — the **bulk binding energy** of atom
$(Z, N)$ is the mass defect*

$$
  \boxed{\;
    B_{\mathrm{bulk}}(Z, N)
    \;=\; E_0 \cdot
    \bigl(
      |\mathrm{tr}_M(W_{\mathrm{free}})|
      \;-\; |\mathrm{tr}_M(W_{\mathrm{atom}})|
    \bigr)
  \;}
$$

*with a SINGLE archimedean calibration constant $E_0$ (the fibre
functor $\tau\colon R \to \mathbb{R}$) fixed by ONE reference
experiment.  Per
[categorical-mass-markov](#prop:categorical-mass-markov): "To obtain
physical masses in MeV, multiply by a calibration constant $E_0$,
determined by matching one experimental value (e.g. the free
neutron $\beta$-decay $Q$-value)."*

*Proof.*

**Step 1: Mass identity at single brane level.**
The [mass identity](#def:mass-identity) defines

$$
  \mathfrak{m}(\varrho)
  = \bigl\lVert \mathrm{tr}\bigl(
     (\textstyle\int_A \otimes \mathrm{id}) \circ \Delta \circ \varrho
   \bigr) \bigr\rVert.
$$

By [categorical-mass-markov](#prop:categorical-mass-markov) Steps 1–3:
- the categorical trace $\mathrm{tr}$ descends under the fibre
  functor $\tau$ to the Jones–Markov trace $\mathrm{tr}_M$ on
  $H_n(R, q)$;
- the Nakayama automorphism $\Psi = (\int_A \otimes \mathrm{id}) \circ \Delta$
  equals $S^2$ for a Frobenius–Hopf algebra, and $S^2 = \mathrm{id}$
  on $H_n(R, q)$ generators (antipode $S(\sigma_i) = \sigma_i^{-1}$, so
  $S^2(\sigma_i) = \sigma_i$);
- therefore $\mathfrak{m}(\varrho) = |\mathrm{tr}_M(\rho(\beta))|$.

**Step 2: Binding = mass defect of Markov traces.**
The binding energy is the classical mass defect:

$$
  B \;=\; \sum_{k=1}^A \mathfrak{m}(\varrho_k^{\text{free}})
       \;-\; \mathfrak{m}(\varrho^{\text{atom}}).
$$

Applying Step 1 and using the disconnected-tensor factorisation of
the free-nucleon braid $W_{\mathrm{free}} =
W_{\mathrm{nucleon}}^{\otimes A}$ under
$H_3(R, q)^{\otimes A} \hookrightarrow H_{3A}(q)$:

$$
  B \;=\; |\mathrm{tr}_M(W_{\mathrm{free}})|
      \;-\; |\mathrm{tr}_M(W_{\mathrm{atom}})|,
$$

where each $\mathrm{tr}_M$ is computed via the Wedderburn
decomposition:

$$
  \mathrm{tr}_M(W) \;=\; \sum_\lambda w_\lambda \cdot
  \frac{\chi_\lambda(W)}{d_\lambda}.
$$

**Step 3: Yekutieli 2D nonabelian Stokes.**
[Yekutieli (2015)](#rem:yekutieli-stokes) identifies the
Markov trace with the nonabelian multiplicative integral of the
instanton connection $A$ over the surface bounded by the braid
closure.  The mass identity is therefore the **categorical action
functional**: binding energy is the difference of nonabelian
action integrals between the atom braid and the disconnected
baseline.

**Step 4: Knot factor via Skein eigenvalues.**
For small $A = 2, 3, 4$ the binding chirality is dominated by the
local knot type. The categorical knot factor $a_K$ is the
**Skein eigenvalue** of the canonical atomic braid at the
relevant Hecke representation — equivalently, the **closed-form
product** over signed pn-crossings:

$$
  a_K \;=\;
    \prod_{c \in \text{pn-crossings}}
      \bigl(1 + \mathrm{sign}(c) \cdot h\bigr),
  \qquad h = q - q^{-1}.
$$

This recovers the empirical BW knot factors:
- $A = 1$ (free nucleon, no pn-crossings): $a_K = 1$
- $A = 2$ (satellite): $a_K = 1 + h$
- $A = 3$ (figure-8): $a_K = 1 - h^2 = 4 - [3]_q$
  (Skein eigenvalue of $4_1$ at $\sigma^2$, cf.
  `nuclear-knot-classification`)
- $A = 4$ (Borromean): $a_K = (1 - h^2)^2$

*(The product $\prod_c(1+\mathrm{sign}(c)\,h)$ expands exactly to these
values for the crossing-sign assignment of `nuclear-knot-classification`,
and $1-h^2 = 4-[3]_q$. Here $a_K$ is the **h-content reduction** — $1$
minus the summed h-content of the pn-crossings — not the literal
figure-eight Jones polynomial $V(4_1)$, which is a distinct
higher-degree invariant; "Skein eigenvalue of $4_1$" denotes this
reduced quantity. See
[audit](../../../docs/audits/2026-06-07-knot-factor-skein-verification.md)
+ witness
[`knot-factor-skein-verification.witness.json`](../../../computations/knot-factor-skein-verification.witness.json).
The crossing-sign assignment, the $A\geq5$ extension, and the
identification of $a_K$ as the canonical mass-formula knot factor remain
conjectural.)*

For $A \geq 5$ the closed-form product generalises beyond the
local-knot regime via the Wenzl-LR branching identity on the
self-conjugate stratum (cf.
`hecke-branching-trace-decomposition`);
the Markov trace remains the universal categorical quantity.

*Historical note:* an earlier formulation of this
step proposed
$a(N) = \lvert\mathrm{tr}_M(W_{\mathrm{atom}})\rvert / \lvert\mathrm{tr}_M(W_{\mathrm{free}})\rvert$
as the ratio form. Empirical verification at 50dps
([`a-K-via-lp-dual` witness](../../computations/a-K-via-lp-dual.witness.json),
see `-m-p-item-b-t5-categorical-attribution.md §7c`)
finds this ratio is 6–17$\times$ off the Skein values above for
A=2,3,4. The ratio form measures the **mass-defect envelope**
$\mathcal{B}_{\mathrm{bulk}}$, not the chirality factor $a_K$;
the closed-form Skein-product **is** the canonical $a_K$ entering
the QOU six-term mass formula
([`six-term-mass-formula-complete`](#thm:six-term-mass-formula-complete)).

$\square$

**Relation to q-Casimir.**
The Markov trace decomposes via the Wedderburn blocks indexed by
partitions; each block's character $\chi_\lambda(W)$ can be
expanded in the basis of q-Casimir eigenstates
([q-Casimir element](#def:q-casimir)) of $\mathcal{U}_q(\mathfrak{su}(2))$.
The eigenvalue $[j]_q[j+1]_q$ on spin-$j$ irreducibles relates to
the q-Laplacian on the corresponding Peter-Weyl component
([q-heat kernel Peter-Weyl](#prop:q-heat-kernel-peter-weyl)).

**Base-ring behaviour.**
Both $\mathrm{tr}_M(W) \in R$ and the ratio
$|\mathrm{tr}_M(W_{\mathrm{atom}})| / |\mathrm{tr}_M(W_{\mathrm{free}})|$
are base-ring-independent
([base-field independence](#rem:base-field-independence)).
The absolute value $|\cdot|$ is archimedean — over $\mathbb{F}_p$
the Markov trace lives in a finite field with no ordering; over
$\mathbb{Q}_p$ there is a $p$-adic absolute value.  The
archimedean realisation at $q = q_0$ gives the physical MeV scale
via $E_0$.

**Witness.**
- `computations/substrate/the formal derivation::atom_markov_trace`:
  $\mathrm{tr}_M(W_{\mathrm{atom}})$ and $\mathrm{tr}_M(W_{\mathrm{free}})$
  via Wedderburn-block Markov trace.
- `computations/substrate/the formal derivation::binding_from_frobenius_pairing`:
  $B_{\mathrm{bulk}} = E_0 \cdot (|\mathrm{tr}_M^{\mathrm{free}}| -
  |\mathrm{tr}_M^{\mathrm{atom}}|)$ with
  $E_0 = 0.782$ MeV (free-neutron $\beta$-decay $Q$).

**Scope.**
Per [categorical-mass-markov](#prop:categorical-mass-markov):
"single-level Markov trace does NOT produce mass ratios like
$\mathfrak{m}_\mu / \mathfrak{m}_e \approx 206.8$; those require
the full tower sum, which evaluates to
$\mathrm{Vol}(K)/\hbar_q^2$ in the archimedean realisation."  The
current implementation is SINGLE-LEVEL only.  Extension to the
full brane-tower sum (accounting for the $\Sigma \|\Phi_q(z_i)\|$
contributions over exceptional divisors) is
[conj:mass-endomorphism](#conj:mass-endomorphism).
<!-- FILE_END: knot-factor-frobenius-pairing.md -->

<!-- FILE_START: wedderburn-weight-canonical.md -->
**Proposition (Canonical Wedderburn-block weight; BW and LP
scalings).** *The BW mass coefficient and the LP shadow-price are
both scalings, valid for every $\lambda \vdash n$, of a single
combinatorial quantity — the canonical
**q-deformed Wedderburn-block weight***

$$
  \tilde w_\lambda
  \;:=\;
  \frac{\dim_q(\lambda)^2}{[n]_q!}
  \;\in\;
  \mathbb{Q}(q),
$$

*where $\dim_q(\lambda)$ is the **quantum hook-length dimension**
defined by the $q$-deformed Frame–Robinson–Thrall formula*

$$
  \dim_q(\lambda) \;=\; \frac{[n]_q!}{\displaystyle\prod_{x \in \lambda} [h_x]_q},
  \qquad
  [k]_q \;=\; \frac{q^k - q^{-k}}{q - q^{-1}},
$$

*with $h_x$ the hook length of cell $x$ in $\lambda$, and
$[n]_q! = \prod_{k=1}^{n}[k]_q$ is the $q$-factorial. At $q = 1$,
$\dim_q(\lambda) \to d_\lambda := n! / \prod_x h_x$ (classical
Frame–Robinson–Thrall), recovering the $S_n$-irrep dimension.
The convention is universal across this paper — the same
$\dim_q$ appears in
[`hecke_n6_frobenius_codim`](frobenius-codim-universal.lean),
[`hecke_n7_frobenius_codim`](frobenius-codim-universal.lean), and
[`hecke_n8_frobenius_codim`](frobenius-codim-universal.lean) Lean
closures, in the Wenzl-bridge $y_\lambda$ closed form
([y-lambda-closed-form-wenzl-bridge](#prop:y-lambda-closed-form-wenzl-bridge)),
and in the q-deformed Wedderburn-block weight $\tilde w_\lambda = \dim_q(\lambda)^2 / [n]_q!$
above. Two of the three named coefficient forms below are immediate
scalings of $\tilde w_\lambda$ for **all** $\lambda$; the third (the
Markov coefficient $y_\lambda$) is related to $\tilde w_\lambda$ **only on
self-conjugate $\lambda$** and otherwise has its own Wenzl
hook–content closed form:*

| Named form | Identity | Domain | Where used |
|------------|----------|--------|------------|
| **BW form** | $\beta_\lambda \;=\; -\tfrac12\,\tilde w_\lambda$ | all $\lambda$ (definitional) | mass coefficient ([hook-weight-derivation](#prop:hook-weight-derivation)) |
| **LP shadow-price** | $C_\lambda \;=\; \tilde w_\lambda \cdot h/2$, $h := q - q^{-1}$ | all $\lambda$ (definitional) | nuclear operator-selection LP dual ([mass-coefficient-shadow-price](#prop:mass-coefficient-shadow-price)) |
| **Wenzl-bridge (self-conjugate case)** | $y_\lambda \;=\; \tilde w_\lambda$ when $\kappa_\lambda = 0$, $\kappa_\lambda := \sum_{x\in\lambda} c(x)$ | self-conjugate $\lambda$ only | sign-tracked closed form ([y-lambda-closed-form-wenzl-bridge](#prop:y-lambda-closed-form-wenzl-bridge)) |

*For self-conjugate partitions ($\kappa_\lambda = 0$), the
Wenzl-bridge form reduces to $y_\lambda = \tilde w_\lambda$ — verified
symbolically for $\lambda = (2,2)$ and $\lambda = (3,2,1)$ by the
P1.3a equivalence audit
([witness](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/docs/audits/-p1-3a-bw-equivalence.witness.json)).
The BW and LP forms are scalings of the same canonical $\tilde w_\lambda$
for every $\lambda$; the Wenzl-bridge identification with
$\tilde w_\lambda$ holds **only** on the self-conjugate stratum. For
non-self-conjugate $\lambda$, $y_\lambda$ is given by Wenzl's
hook–content closed form [wenzl1988] and is, in general, distinct
from $(-1)^{\kappa_\lambda} \tilde w_\lambda$ — see the
[non-self-conjugate categorical witness](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/canonical evaluation-wedderburn-weight-scheme.witness.json),
which records $|y_\lambda / \tilde w_\lambda|$ ratios from $0.14$ to
$2.54$ at $q_0$ for $n \in \{2, 3\}$, confirming the two are
distinct weight families away from self-conjugate $\lambda$.*

## Canonicity of $\tilde w_\lambda$

The Wedderburn–Artin decomposition
([Wedderburn mass formula](#thm:wedderburn-mass-formula))
identifies the Hecke algebra $H_n(R, q)$ with a direct sum of
matrix blocks indexed by partitions $\lambda \vdash n$:

$$
  H_n(R, q) \;\cong\; \bigoplus_{\lambda \vdash n} M_{f_\lambda}\bigl(\mathbb{Q}(q)\bigr),
  \qquad
  f_\lambda \;=\; \dim V_\lambda \;\in\; \mathbb{Z}_{>0}
$$

(the $\mathbb{Q}(q)$-dimensions $f_\lambda$ are the classical
$S_n$-irrep dimensions; the algebra is a flat deformation of
$\mathbb{Q}S_n$). The combinatorial weight

$$
  \tilde w_\lambda \;=\; \frac{\dim_q(\lambda)^2}{[n]_q!}
$$

is the **q-deformed Wedderburn-block weight** — the
$\mathbb{Q}(q)$-rational analogue of the classical block-size
fraction $f_\lambda^2 / n!$. It is determined by the algebra alone,
before any choice of mass / LP convention, and it specialises to
the classical Plancherel measure
([prop:plancherel-weight-boundedness](#prop:plancherel-weight-boundedness))
at $q = 1$.

The Markov trace on $H_n(R, q)$
([Jones–Markov](#thm:jones-markov-trace))
decomposes along the blocks as

$$
  \mathrm{tr}_M
  \;=\;
  \sum_{\lambda \vdash n} y_\lambda(q) \cdot \chi_\lambda,
$$

where $\chi_\lambda$ is the Hecke-irrep character on the
$\lambda$-block and $y_\lambda(q)$ is the **Markov coefficient**
given by Wenzl's hook–content closed form [wenzl1988]
([y-lambda-closed-form-wenzl-bridge](#prop:y-lambda-closed-form-wenzl-bridge)).
For self-conjugate $\lambda$ the Markov coefficient and the
Wedderburn-block weight coincide, $y_\lambda(q) = \tilde w_\lambda$; for
non-self-conjugate $\lambda$ they are distinct.

## The three named scalings — derivations

### BW form: $\beta_\lambda = -\tfrac12 \tilde w_\lambda$

Mass coefficients in the BW formula carry a sign and a factor of
$\tfrac12$:

- The sign is fixed by the channel structure (sym/std/alt
  alternation in [Wedderburn mass formula](#thm:wedderburn-mass-formula)).
- The $\tfrac12$ comes from the Wigner $T=0$ doubling convention:
  each $\mathfrak{p}\mathfrak{n}$ crossing uses $c=2$ in the hook
  channel, and $\beta$ compensates
  ([hook-weight-derivation](#prop:hook-weight-derivation)).

So $\beta_\lambda = -\tfrac12 \tilde w_\lambda$ is the BW-ready mass
coefficient — what one multiplies by $m_e$ to get a MeV-scale
correction.

### LP shadow-price: $C_\lambda = \tilde w_\lambda \cdot h/2$

In the nuclear operator-selection LP
([mass-coefficient-shadow-price](#prop:mass-coefficient-shadow-price)),
each partition $\lambda$ contributes a Frobenius-positivity
constraint, and its dual variable (shadow price) is

$$
  C_\lambda
  \;=\;
  \tilde w_\lambda \cdot \frac{h}{2},
  \qquad h = q - q^{-1}.
$$

The factor $h$ is the Hecke-generator scalar
$\sigma_i^2 = h\,\sigma_i + 1$; it appears because the LP
constraint involves Hecke-generator action, not pure Markov
trace.

### Wenzl-bridge on the self-conjugate stratum: $y_\lambda = \tilde w_\lambda$ when $\kappa_\lambda = 0$

The Wenzl-bridge closed form
([y-lambda-closed-form-wenzl-bridge](#prop:y-lambda-closed-form-wenzl-bridge))
tracks the **content sum**

$$
  \kappa_\lambda
  \;:=\;
  \sum_{x \in \lambda}\,c(x)
  \;=\;
  \sum_{x = (i,j) \in \lambda}\,(j - i).
$$

For self-conjugate $\lambda$ (those with $\lambda = \lambda'$),
$\kappa_\lambda = 0$ and the Markov coefficient coincides with
the Wedderburn-block weight: $y_\lambda = \tilde w_\lambda$.

For non-self-conjugate $\lambda$, $y_\lambda$ and $\tilde w_\lambda$ are
**distinct**: $y_\lambda$ is given by Wenzl's content-distance
closed form [wenzl1988] and is not, in general, a sign multiple of
$\tilde w_\lambda$. The empirical witness
[`canonical evaluation-wedderburn-weight-scheme.witness.json`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/canonical evaluation-wedderburn-weight-scheme.witness.json)
records $|y_\lambda / \tilde w_\lambda|$ ratios ranging from $\approx 0.14$
to $\approx 2.54$ at $q_0$ for $n \in \{2, 3\}$, confirming that
Markov $y_\lambda$ and Wedderburn $\tilde w_\lambda$ are distinct weight
families away from the self-conjugate stratum.

## Symbolic verification (self-conjugate stratum)

The BW and LP scaling identities — and the Wenzl-bridge identity
restricted to the self-conjugate stratum — are verified at the
level of explicit $\mathbb{Q}(q)$ rational expressions for the
partitions $\lambda = (2,2) \vdash 4$ (used in BW-8 / BW-11 hook
terms) and $\lambda = (3,2,1) \vdash 6$ (Wigner-2 BW-7). Sympy
simplifies the differences to $0$ exactly. Both partitions are
self-conjugate, so the witness establishes the BW/LP identities in
general (definitional) and the Wenzl-bridge identity on the
self-conjugate stratum. Witness:
[`docs/audits/-p1-3a-bw-equivalence.witness.json`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/docs/audits/-p1-3a-bw-equivalence.witness.json).

## Form selection by context

| Context | Form chosen | Reason |
|---------|-------------|--------|
| Mass formula | $\beta_\lambda = -\tfrac12 \tilde w_\lambda$ | Already includes the sign and Wigner $\tfrac12$ doubling needed to multiply by $m_e$ and produce a MeV correction. |
| Operator-selection LP | $C_\lambda = \tilde w_\lambda h/2$ | LP duality on the Frobenius-positivity constraint involves the Hecke generator $\sigma_i$ with eigenvalue $h$; the dual variable inherits the $h$ factor. |
| Sign-tracked closed form (self-conjugate) | $y_\lambda = \tilde w_\lambda$ when $\kappa_\lambda = 0$ | On self-conjugate $\lambda$, the Markov coefficient agrees with the Wedderburn-block weight up to the (trivial) content-sum sign. For non-self-conjugate $\lambda$ use Wenzl's hook–content closed form ([y-lambda-closed-form-wenzl-bridge](#prop:y-lambda-closed-form-wenzl-bridge)) directly. |

The BW and LP forms are scalings of $\tilde w_\lambda$ for every
$\lambda$ (definitional). The Wenzl-bridge identification with
$\tilde w_\lambda$ is exact on the self-conjugate stratum; off that
stratum, the Markov coefficient $y_\lambda$ is a distinct weight
family and must be obtained from the Wenzl closed form.

## Corollaries for downstream use

- Any new BW mass coefficient or LP shadow-price at a new
  partition can be derived in three steps: (1) compute $\tilde w_\lambda$
  from $\dim_q(\lambda)$ and $[n]_q!$; (2) apply the BW or LP
  scaling identity natural in the surrounding context; (3) cite
  this proposition for the rationale.
- A Markov coefficient $y_\lambda$ at a non-self-conjugate
  $\lambda$ must come from the Wenzl closed form
  ([y-lambda-closed-form-wenzl-bridge](#prop:y-lambda-closed-form-wenzl-bridge)),
  not from a sign of $\tilde w_\lambda$.
- Cross-checks between BW and LP forms reduce to a one-line
  scaling identity. Cross-checks between Markov $y_\lambda$ and
  Wedderburn $\tilde w_\lambda$ are non-trivial off the self-conjugate
  stratum.
- The earlier "BW vs Wenzl-bridge vs shadow-price" question of
  *which derivation is correct* dissolves: all three are correct
  views of the same canonical $\tilde w_\lambda$.

$\square$
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
**Proposition.**
*Each coefficient of the QOU mass formula
([six-term mass formula](#thm:six-term-mass-formula-complete))
is the shadow price (LP dual variable) of the corresponding
partition's Frobenius positivity constraint in the nuclear
operator selection LP.*
<!-- FILE_END: mass-coefficient-shadow-price.md -->

<!-- FILE_START: frobenius-self-duality-forces-lp-dual-extraction.md -->
**Proposition.**
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

