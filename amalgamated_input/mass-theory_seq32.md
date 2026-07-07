<!-- FILE_START: intro-lp-dual-jucys-murphy.md -->
The operator-selection LP introduced in the previous sections
admits a dual programme whose variables are the shadow prices of
the Frobenius positivity constraints.  The Jucys–Murphy central
elements of the Hecke algebra furnish a canonical basis in which
the dual variables have a transparent categorical interpretation
— each shadow price is the residue of a Jucys–Murphy operator
at a Wedderburn block.

The arc establishes the LP dual–Jucys–Murphy correspondence,
proves the central-element identities needed to read off the
shadow prices, and verifies that the active demand channels
(those with positive shadow price) coincide with the most
receptive sub-braids.  The closing blocks tabulate the
Jucys–Murphy spectra for small $n$ and connect the active-set
identification to the binding-energy substrate formula from the
Particles chapter.
<!-- FILE_END: intro-lp-dual-jucys-murphy.md -->

<!-- FILE_START: jucys-murphy-central-elements-qou.md -->
**Proposition.**
*In the Iwahori–Hecke algebra $H_n(q)$, the Jucys–Murphy
elements*

$$
  J_k \;=\; q^{1-k}\sum_{i < k} \sigma_{i,k},
  \qquad k = 1, 2, \ldots, n
$$

*generate a maximal commutative subalgebra. The elementary
symmetric polynomials*

$$
  P_\ell \;:=\; e_\ell(J_1, J_2, \ldots, J_n)
  \;\in\; Z\bigl(H_n(q)\bigr)
$$

*lie in the centre, and act on the Wedderburn block $V_\lambda$
($\lambda \vdash n$) as the scalar*

$$
  c_\ell(\lambda) \;=\; e_\ell\!\left(\{q^{2c(\square)} :
    \square \in \lambda\}\right)
$$

*where $c(\square) = j - i$ is the content of cell
$\square = (i,j)$.*
<!-- FILE_END: jucys-murphy-central-elements-qou.md -->

<!-- FILE_START: jucys-murphy-central-elements-qou-interpretation.md -->
**Remark (categorical content).** The Jucys–Murphy elements
are the Hecke-algebraic shadow of *commuting Casimirs* in
$U_q(\mathfrak{sl}_n)$: they are the natural commuting
operators that read off the highest weight of an irreducible
representation. Cell content $c(\square)$ at cell $(i,j)$ is
the magnetic quantum number $m_j$ of the corresponding
$\mathrm{SU}_q(2)$ weight space, so $c_\ell(\lambda)$ is a
$q$-deformation of the $\ell$-th Casimir eigenvalue on
$V_\lambda$. The crystal limit $q \to 0$ recovers the
classical content combinatorics of the Kashiwara crystal.
<!-- FILE_END: jucys-murphy-central-elements-qou-interpretation.md -->

<!-- FILE_START: spin-involution.md -->
**Definition (spin involution on a Frobenius $*$-algebra).**
Let $(A, \tau, {}^*)$ be a Frobenius $*$-algebra over a
commutative ring $R$ — i.e., a Frobenius algebra equipped with
an $R$-linear involutive anti-homomorphism ${}^* : A \to A$
($(ab)^* = b^* a^*$, $(a^*)^* = a$) such that $\tau$ is
$*$-compatible ($\tau(a^*) = \tau(a)$ in the real case;
$\tau(a^*) = \overline{\tau(a)}$ otherwise). A *spin involution*
on $(A, \tau, {}^*)$ is an $R$-linear map $\sigma : A \to A$
satisfying

1. **Involution**: $\sigma \circ \sigma = \mathrm{id}_A$.
2. **Anti-multiplicative**:
   $\sigma(a b) = \sigma(b)\, \sigma(a)$ for all $a, b \in A$.
3. **Trace-invariant**: $\tau \circ \sigma = \tau$.
4. **$*$-compatible**: $\sigma(a^*) = \sigma(a)^*$ for all $a$.

The $\mathbb{Z}/2$ grading $A = A_+ \oplus A_-$ by
$\sigma$-eigenvalue is the *spin grading*; $A_+$ is the
*spin-singlet sector* and $A_-$ is the *spin-doublet sector*.

**Hypothesis (2 invertible).** When using the $A_\pm$ projections
we assume $2 \in R^\times$ — i.e., the base ring $R$ contains
$\tfrac{1}{2}$. This is satisfied when $R$ is a field of
characteristic $\neq 2$ (in particular $\mathbb{Q}$,
$\mathbb{R}$, $\mathbb{C}$, $\mathbb{Z}[\tfrac{1}{2}]$, or any
$\mathbb{Q}$-algebra). For the QOU substrate $R = \mathbb{R}$ or
$R = \mathbb{Q}(q)$ this holds. Without this hypothesis, the
$A_\pm$ projections $a_\pm := \tfrac{1}{2}(a \pm \sigma(a))$ are
ill-defined; an alternative additive decomposition (without
division) exists when $A$ has an idempotent splitting
$\mathbf{1} = e_+ + e_-$ with $\sigma(e_\pm) = \pm e_\pm$, but
that is more restrictive.

Every $a \in A$ has the canonical decomposition
$a = a_+ + a_-$ with $a_\pm := \tfrac{1}{2}(a \pm \sigma(a)) \in
A_\pm$. The *isospin third-component* is **defined on
$\sigma$-eigenvectors**:

$$
  T_3(a) \;=\; \tfrac{1}{2}\,\mathrm{sgn}_\sigma(a)
  \;\in\; \{-\tfrac{1}{2},\, 0,\, +\tfrac{1}{2}\},
$$

with $T_3(a) = 0$ for $a \in A_+$ (singlet, $\sigma(a) = a$)
and $T_3(a) = \pm \tfrac{1}{2}$ for $a \in A_-$ realising
$\sigma(a) = \pm a$. For a general $a \in A$, $T_3$ is read
off the $A_\pm$-projection $a = a_+ + a_-$.

**Derived spin grading (formalised sorry-free).** The Lean sibling proves
the following facts about the grading, over any commutative ring $R$ with
$\tfrac{1}{2} \in R$ (so $2 \in R^\times$):

1. $\sigma$ is an additive group homomorphism ($\sigma 0 = 0$,
   $\sigma(-a) = -\sigma(a)$, $\sigma(a-b) = \sigma a - \sigma b$).
2. The projections $a_\pm = \tfrac{1}{2}(a \pm \sigma(a))$ satisfy
   $\sigma(a_+) = a_+$ and $\sigma(a_-) = -a_-$; the decomposition
   $a = a_+ + a_-$ holds, and $\sigma(a) = a_+ - a_-$.
3. The sectors meet trivially: $\sigma(x) = x$ and $\sigma(x) = -x$ force
   $x = 0$, so $A_+ \cap A_- = 0$.
4. The isospin third component $T_3 = \tfrac{1}{2}\,\mathrm{sgn}_\sigma$
   satisfies $T_3 = 0$ on the singlet sector and $T_3 = \pm\tfrac{1}{2}$ on
   the two doublet components, with $2\,T_3 = \mathrm{sgn}_\sigma$.
<!-- FILE_END: spin-involution.md -->

<!-- FILE_START: spin-involution-lp-dual-invariance.md -->
**Proposition (spin-invariance of the LP-dual).**
*Let $(A, \tau)$ be a Frobenius algebra with spin involution
$\sigma$ ([def:spin-involution](#def:spin-involution)). Let
$c \in A$ be $\sigma$-invariant ($\sigma(c) = c$).
Let $\Sigma$ be a $\sigma$-stable set of central idempotents of
$A$ (i.e., $\sigma(\pi_\lambda) \in \{\pi_\mu : \mu \in
\Sigma\}$ for every $\lambda \in \Sigma$). For any $\beta \in A$,
the optimal dual variable $y_0^*$ of the operator-selection LP*

$$
  \min_{x \in A}\; \tau(c \cdot x)
  \quad \text{s.t.} \quad
  \tau(\beta^* \beta \cdot x) = n_{\mathrm{target}}(\beta), \;\;
  \tau(\pi_\lambda \cdot x) \geq 0 \;\; \forall \lambda \in \Sigma
$$

*satisfies*

$$
  y_0^*\bigl(\sigma(\beta)\bigr) \;=\; y_0^*(\beta).
$$
<!-- FILE_END: spin-involution-lp-dual-invariance.md -->

<!-- FILE_START: spin-involution-lp-dual-invariance-interpretation.md -->
**Remark (mathematical content of "isospin").**
Isospin is *not* a feature peculiar to nucleons; it is the
$\mathbb{Z}/2$ grading attached to *any* Frobenius algebra
equipped with a spin involution. Whenever physical observables
are extracted as $\tau$-traces of products of central elements
and braid recipes, the spin-singlet sector ($T_3 = 0$) and
spin-doublet sector ($T_3 = \pm 1/2$) decompose canonically
under the LP-dual. The "Wigner energy term"
$\sim |Z - N|/A$ in the BW formula is the $T_3$-projection of
this grading; it appears because $|Z - N|$ is the $\mathbb{Z}/2$
*charge* of the recipe, which the LP-dual reads off
mechanically.

**Remark (why this proof works generically).**
The proof never invokes the specific structure of nucleons,
quarks, $SU(2)$, or even Lie theory. The only inputs are:

1. A Frobenius algebra $(A, \tau)$ with non-degenerate trace,
2. An involutive anti-homomorphism $\sigma$ preserving $\tau$,
3. A $\sigma$-invariant central cost $c$,
4. A $\sigma$-stable channel set $\Sigma$.

Any quantum-algebraic system with these four ingredients has
LP-dual spin-invariance. The QOU paper inherits it because
$(H_n(R, q), \tau_{\mathrm{Markov}}, S, P_\ell, \Sigma)$
satisfies all four. Particle physics gets isospin because
nucleons are realised as a 2-row Wedderburn stratum (per
empirics)
inside this same algebra; the Wigner-energy phenomenology is
the LP-dual shadow of the categorical $\mathbb{Z}/2$ grading.
<!-- FILE_END: spin-involution-lp-dual-invariance-interpretation.md -->

<!-- FILE_START: lp-dual-scaling-conjecture.md -->
**Remark.**

Empirical data on $y_0^*$ from
[`alpha-5-lp-dual-crystal.witness.json`](computations/alpha/alpha-5-lp-dual-crystal.witness.json)
(2-row stratum, $\ell = 5$):

| $q$ | $y_0^*(D)$ <br/>$(A=2,|T_3|=0)$ | $y_0^*(T) = y_0^*({}^3\mathrm{He})$ <br/>$(A=3,|T_3|=\tfrac{1}{2})$ | ratio $T/D$ |
|----:|------------:|--------------:|--------:|
| 1.110 | 10.31 | 570.68 | 55.34 |
| 1.050 | 7.69 | 247.93 | 32.24 |
| 1.001 | 6.03 | 127.69 | 21.18 |

**Mirror-pair invariance** ($T = {}^3\mathrm{He}$) holds exactly,
as proved by [`prop:spin-involution-lp-dual-invariance`](#prop:spin-involution-lp-dual-invariance).

**Non-separability of $g(q) \cdot h(A, |T_3|)$.** The ratio
$T/D$ depends on $q$ non-by definition (21 $\to$ 55 across the physical
regime). This rules out the simplest separable closed form

$$
  y_0^*(A, |T_3|) \stackrel{?}{=} g_\ell(q) \cdot h_\ell(A, |T_3|),
$$

since separability would force $T/D$ to be $q$-independent.

**Candidate closed forms (research directions).** Listed in
order of increasing structural specificity:

(a) **Partition-of-unity decomposition.** Sum over the
LP-dual active set:

$$
  y_0^*(A, |T_3|) \;=\;
  \sum_{\lambda \in \mathrm{active}(A, |T_3|)}
  a_\lambda(A, |T_3|) \cdot b_\lambda(q).
$$

At $q_0$ the active set is $3/4$ channels for $D$ and $4/5$
channels for $T, {}^3\mathrm{He}$. The $q$-dependent ratio
arises because the LP constraints re-weight at different $q$.

(b) **Wedderburn-block-resolved form.** Each $y_0^*$
decomposes as a sum over per-block contributions

$$
  y_0^*(A, |T_3|)
  \;=\;
  \sum_{\lambda \in \mathrm{active}}
  u_\lambda^*\bigl(A, |T_3|, q\bigr),
$$

with each $u_\lambda^*$ depending on the per-block Frobenius
pairing $y_\lambda \cdot \chi^\lambda(\mathcal{B}_K)$. Mirror-pair
invariance follows because the active sets of $T$ and
${}^3\mathrm{He}$ are $\lambda$-conjugate under the Hopf
antipode (per
[`prop:spin-involution-lp-dual-invariance`](#prop:spin-involution-lp-dual-invariance)).

(c) **$q \to 1$ classical limit.** At $q = 1$ the $q$-numbers
collapse to ordinary integers and the LP-dual should reduce
to a Specht-dim-weighted sum recovering the classical BW
coefficients $\alpha_k$. Empirically the $q = 1.001$ numbers
($D = 6.03$, $T = 127.69$) suggest the limit exists but with
a non-trivial $T/D$ ratio that needs a Specht-combinatorial
explanation.

(d) **Kashiwara crystal limit $q \to 0^+$.** The genuine
Kashiwara crystal limit (NOT $q \to 1$). In that limit the
JM eigenvalues become integer content multiplicities and the
LP becomes integer programming over a Kashiwara crystal graph
(open
follow-up (H)). The current canonical evaluation sweeps $q \to 1^+$ only;
a separate $q \to 0^+$ canonical evaluation is needed.

(e) **Demazure sub-crystal selector.**  empirically
found that the categorical rule for $\lambda^*(Z, N)$ is
$\max(y_\lambda \cdot |\chi^\lambda|)$ — not a pure structural
property of $\lambda$. This selector picks out a Demazure
sub-crystal of the canonical basis. The LP-dual $u_\lambda^*$
may decompose along Demazure components, yielding
$y_0^*(A, |T_3|)$ as a sum of crystal-graph weights.

**Witness-able next probes.**

1. **${}^4\mathrm{He}$ canonical evaluation** ($A = 4, |T_3| = 0$, $n = 12$;
 sympy expensive). *Hypothesis*:
 $y_0^*({}^4\mathrm{He}) / y_0^*(D)$ is $q$-rational — both
 sit on the $|T_3| = 0$ branch — distinct from the
 $|T_3| = \tfrac{1}{2}$ branch ($T, {}^3\mathrm{He}$).

2. **$q \to 0^+$ crystal sweep** at $q \in \{1/2, 1/4, \ldots\}$
 to approach the Kashiwara crystal limit.

3. **Demazure-sliced LP**: solve the LP restricted to a
 single Demazure sub-crystal (chosen by the
 $\max(y_\lambda \cdot |\chi^\lambda|)$ selector of #619)
 to test (e).

**No closed form is asserted as proved.** This remark
consolidates the empirical structure (mirror-pair invariance
holds; simple separable form refuted) and lists the next
research probes. Resolving the $A$-scaling is the highest-
leverage next step for the iterative-LP-dual mass formula.
<!-- FILE_END: lp-dual-scaling-conjecture.md -->

<!-- FILE_START: wigner-2-coefficient.md -->
**Proposition.**
*For any self-conjugate partition $\lambda = \lambda'$ of $k$,
the per-generator trace in the Hoefsmit seminormal representation
satisfies*

$$
  \frac{\mathrm{tr}(\sigma_g^{(\lambda)})}{\dim(\lambda)}
  = \frac{h}{2}
  = \frac{q - q^{-1}}{2}
$$

*for every generator $g = 1, \ldots, k{-}1$.  Consequently, the
BW coefficient ([shadow price](#prop:mass-coefficient-shadow-price))
for $\lambda$ is*

$$
  C_\lambda = w_\lambda \cdot \frac{h}{2}
  = \frac{\dim_q(\lambda)^2}{[k]_q!} \cdot \frac{q - q^{-1}}{2}
$$

*In particular, for $\lambda = [3,2,1] \vdash 6$:*

$$
  C_{[3,2,1]}
  = \frac{[2]_q\,[4]_q\,[6]_q \cdot h}
         {2\,[3]_q^2\,[5]_q}
$$
<!-- FILE_END: wigner-2-coefficient.md -->

<!-- FILE_START: wigner-2-coefficient-interpretation.md -->
**Remark (isospin midpoint).**
The value $h/2 = (q - q^{-1})/2$ is the arithmetic mean of the
symmetric eigenvalue $q$ and the antisymmetric eigenvalue $-q^{-1}$
of the Hecke generators.  Self-conjugate partitions sit at the
exact isospin midpoint of the Hecke spectrum.

**Remark (pn invisibility).**
The per-crossing trace contribution in the $[3,2,1]$ representation
is:

| Crossing type | Coefficient $d$ | $\mathrm{tr}(\sigma + d \cdot I)/\dim$ |
|:---:|:---:|:---:|
| $pp$ | $0$ | $h/2$ |
| $nn$ | $-h$ | $-h/2$ |
| $pn$ | $-h/2$ | $0$ |

The proton-neutron crossing is **invisible** to $[3,2,1]$: its
trace contribution $h/2 - h/2 = 0$ vanishes exactly.  Only
$pp$ ($+h/2$) and $nn$ ($-h/2$) crossings contribute, with
opposite signs.

Consequently the $[3,2,1]$ BW scaling is

$$
  S_{[3,2,1]}(Z,N) = \frac{(Z - N)(A - 1)}{A^{4/3}}
$$

where $(Z{-}N)(A{-}1) = Z(Z{-}1) - N(N{-}1)$ counts the net
$pp$ minus $nn$ crossing asymmetry, NOT the isospin Casimir
$T(T{+}1)$.  This is why $\chi_{[3,2,1]}$ vanishes for deuterium
(pure $pn$) and ${}^3\mathrm{He}$ (where the single $pp$
crossing's contribution is cancelled by the full matrix
product structure at second order in $h$).

**Remark (character structure).**
The nuclear character $\chi_{[3,2,1]}$ has universal factor
$h^2 \cdot \Phi_6(q^2)$ where $\Phi_6(q^2) = q^4 - q^2 + 1
= (q^6 + 1)/(q^2 + 1)$ is the 6th cyclotomic polynomial evaluated
at $q^2$.  The $h^2$ factor encodes the isospin sensitivity (the
character vanishes at $q = 1$, i.e., in the classical limit).
$\square$
<!-- FILE_END: wigner-2-coefficient-interpretation.md -->

<!-- FILE_START: mass-endomorphism-tower.md -->
> **TOP-OF-FILE SUPERSEDED-$\rho_q$ BANNER (promoted).**
> The substrate density $\rho_q = 1/\hbar_q^2$ used in the algebraic
> form below is **STRUCTURALLY WRONG** per the inline SUPERSEDED
> note (lines 28-51). The correct dimensional factor is the
> operator-valued $A^\lambda_{\mu, \nu}(I)$ from
> [`prop:hecke-branching-trace-decomposition`](#prop:hecke-branching-trace-decomposition);
> the corrected graded expansion is [`prop:rho-k-graded-expansion`](rho-k-graded-expansion.md).
> The corrected canonical form of the mass tower uses
> $-\mathrm{Li}_2^q(-|\hat V_i|)$ in place of $\Phi_q(|\hat V_i|)$
> (resolution, lines 133-150). Full purge tracking:
> [`docs/audits/-superseded-rho-q-purge.md`](../../../docs/audits/-superseded-rho-q-purge.md).
> The substrate-density $\rho_q$ display in this file is retained
> for historical readability of the brane-tower spectral structure
> only; do **NOT** use it for production computations.

Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
substrate parameter $q$
([quantum observable universe](#def:quantum-observable-universe)).
Let $\hat{V}_i^{\mathrm{full}}$ denote the additive Wedderburn traced
volume at generator $i$
([three-invariant mass formula](#sec:atomic-braid-mass-foundations)).

### Algebraic form

Via the Kashaev volume--density reading
([Kashaev volume--density](#rem:kashaev-volume-density)), the tower
admits a compact algebraic statement: *for every braid
$\beta \in B_{n}$ with $n - 1$ generators,*

$$
  \mathfrak{m}(\varrho)
  \;=\;
  \rho_{q} \cdot
  \mathrm{Vol}_{q}^{\mathrm{tower}}(\beta),
  \qquad
  \mathrm{Vol}_{q}^{\mathrm{tower}}(\beta)
  \;\in\; \mathbb{Z}[q^{1/2}, q^{-1/2}],
$$

*where $\rho_{q} = 1/\hbar_{q}^{2}$ is the substrate density
([quantum Planck constant](#def:quantum-planck-constant)) and*

**SUPERSEDED.** *The substrate-only ansatz
$\rho_q = 1/\hbar_q^2 \approx 102$ is **structurally wrong**: it is
braid-class-independent, but the categorical density $\rho_K$
varies $\sim 30\times$ across atoms ($A = 1$ to $A = 3$;
[graded ρ\_K expansion](#prop:rho-k-graded-expansion)). The
correct dimensional factor is the **operator-valued**
$A^\lambda_{\mu, \nu}(I) \in \mathrm{End}(V_\mu \otimes V_\nu)$
from [hecke branching trace decomp](#prop:hecke-branching-trace-decomposition),
which depends on the specific braid through its LR-block decomposition.
The iterated $(Z+N)$-factor extension to atomic braids — explicitly
replacing the scalar Wedderburn-volume tower with the operator-trace
form — is stated in [`prop:mass-tower-operator-valued`](mass-tower-operator-valued.md)
(authored as the Stage-1 unblock).
The graded expansion
$\mathcal{M}(K)/(m_e \cdot |\!\operatorname{tr}_M(\mathcal{B}_K)|) = \rho_K^{\mathrm{LO}} + \rho_K^{\text{single-gen}} + \rho_K^{\text{pair-gen}} + \dots$
([prop:rho-k-graded-expansion](#prop:rho-k-graded-expansion))
replaces the $\rho_q$ ansatz with a categorically-derived series
where the LO piece is the constituent-mass ratio (Markov
multiplicativity, \[Wenzl 1988] Theorem 5) and the single-gen
piece is the proven $\tfrac{\alpha}{2} \cdot \sum \ln(\hat V_i^{\mathrm{full}} \cdot \overline{\hat V_i^{\mathrm{full}}})$
binding correction at $0.18\%$ accuracy across $Z = 1..20$. The
$\rho_q$ display below is retained for historical readability of
the brane-tower spectral structure but does not represent the
correct dimensional scaling.*

$$
  \mathrm{Vol}_{q}^{\mathrm{tower}}(\beta)
  \;=\;
  \prod_{i=0}^{n-2} \hat{V}_{i}^{\mathrm{full}}
  \;+\;
  \sum_{\emptyset \neq S \subseteq \{0,\ldots,n-2\},\;\lvert S \rvert \leq 2}
    z^{\lvert S \rvert}
    \cdot \mathrm{Vol}_{q}^{(S)}(\beta),
$$

*with each $\mathrm{Vol}_{q}^{(S)}(\beta) \in \mathbb{Z}[q^{1/2}, q^{-1/2}]$
a Markov trace over the transfer-matrix chain supported on $S$
([Markov trace product](#thm:markov-trace-product)), and
$z = 1/(q^{1/2} + q^{-1/2})$ the Markov parameter.*

Every per-generator contribution is a finite Laurent polynomial in $q$;
no quantum-dilogarithm evaluation is required to **state** the tower.
The archimedean realisation $\mathrm{Vol}_{q}^{(S)} \rightsquigarrow
\Phi_{q}$ is a specialisation via the Kashaev limit, recorded in the
expanded form below.

### Quantum-dilogarithm form (archimedean specialisation)

Let $\Phi_q(z) = \prod_{k=1}^{\infty}(1 - q^{-k}z)^{-1}$ denote
the non-perturbative quantum dilogarithm
([quantum Bloch group](#def:quantum-bloch-group)).

**Kashaev-integration-identity audit (added).**
*The proof step claims*

$$
  \Phi_q(z_p) \;=\; \int_0^{z_p} \frac{\ln_q(1+t)}{t}\,dt
              \;=\; \prod_{k\geq 1}(1 - q^{-k} z_p)^{-1}.
$$

*canonical canonical evaluation (`kashaev-integration-identity.witness.json`): the
left integral at $q_0 \approx 1.110$ for $V \in (0, 1)$ is bounded
in $[0.1, 0.82]$, while the right-hand product $\Phi_q(V)$ grows
unboundedly (e.g. $\Phi_q(0.989) \approx 6.7 \times 10^5$).  The
two sides differ by 6 orders of magnitude at $V = 0.989$ — the
identity does NOT hold canonical.*

*The integral is a $q$-deformed dilogarithm $-\mathrm{Li}_2^q(-V)$,
not the quantum dilogarithm $\Phi_q$.  These are distinct functions
($\mathrm{Li}_2^q$ is regular on $(-1, 1)$; $\Phi_q$ has a pole
structure tied to the q-Pochhammer denominators).  The proof step
appears to conflate them.*

*Implication: the boxed theorem's specialisation
$\mathrm{Vol}_q^{(S)} \rightsquigarrow \Phi_q(|\hat V_i|)$ is not
the Kashaev limit of the R-side algebraic form.  Its empirical
consequence is the $-737$ MeV mirror-nucleus pathology
(`brane-tower-isospin-diagnosis.witness.json`).*

*The paper's `sec:atomic-braid-mass-foundations` uses the alternative form
$\tfrac{\alpha}{2} \cdot \sum_i \ln(\hat V_i^{\mathrm{full}} \cdot \overline{\hat V_i^{\mathrm{full}}})$ (with $\alpha = m_e \cdot 8G$,
the Borromean binding scale `prop:binding-scale-catalan`), which gives
0.19% mean atomic-mass error across $Z = 1$..$10$ with zero fitted
parameters — but the integration canonical evaluation shows the
$\int (\ln_q(1+t)/t)\,dt = -\mathrm{Li}_2^q(-V)$ identity doesn't
reduce to $\alpha \cdot \ln|V|$ either.*

*Both forms above are concrete evaluations of the abstract GB-NF
statement
([atomic mass via GB-NF](#prop:atomic-mass-gb-nf))
$\mathcal{M}(K) = m_e \cdot \rho_K \cdot \lvert\!\operatorname{tr}_M\!(\mathrm{NF}_{\mathrm{GS}}(\mathcal{B}_K))\!\rvert$.
The substrate density $\rho_q = 1/\hbar_q^2$ above is a substrate-only
ansatz for the categorical density $\rho_K$; empirically
$\rho_K^{\mathrm{CODATA}}$ is strongly braid-class-dependent
(see `rho-k-codata-vs-six-term.witness.json`: $\rho_K^{\mathrm{CODATA}}(D)/\rho_K^{\mathrm{CODATA}}(\mathfrak{p}) \approx 5.5$),
so any candidate dimensional factor must absorb that scaling either
into $\rho_q$ itself or into $\mathrm{Vol}_q^{\mathrm{tower}}(\beta)$.*

*Open: the correct Kashaev limit of $\mathrm{Vol}_q^{(S)}$ at $q_0$
needs derivation.  Two candidates the integral does NOT support:
($\Phi_q(|V|)$) blows up; ($\alpha\cdot\ln|V|$) is empirically close
but not the literal integration evaluation.  The dilogarithm form
$-\mathrm{Li}_2^q(-|V|)$ is the actual integration result and may be
the correct specialisation; this needs paper-side verification.*

**Resolution (added).** *The corrected canonical form of
the mass-endomorphism tower uses $-\mathrm{Li}_2^q(-|\hat V_i|)$ in
place of $\Phi_q(|\hat V_i|)$; see the proposition statement below.
The production compute pipeline at
the canonical formalism
and
the canonical formalism
use `tower_mode="li2q"` and evaluate $-\mathrm{Li}_2^q(-|V|)$ via the
symmetric q-dilogarithm series
$\mathrm{Li}_2^q(z) = \sum_{n \geq 1} z^n / (n \cdot [n]_q)$. The
$\Phi_q$ product form survives only in
the canonical formalism
as a **diagnostic** that exposes the $-737$ MeV mirror-nucleus
pathology — it documents the bug, not the corrected mass formula.
The Lean stub
[`QOU.BraidKnot.QuantumDilogarithm`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidKnot/QuantumDilogarithm.lean)
axiomatises both functions and their distinct definitions to
prevent regression.*

**Trace-vs-evaluation note (added).**
The R-side algebraic form of the tower above expresses each
$\mathrm{Vol}_q^{(S)}(\beta)$ as a Markov trace over the chain on $S$
— each term is therefore Markov-invariant.  The archimedean
specialisation $\mathrm{Vol}_q^{(S)} \rightsquigarrow \Phi_q$ below
replaces this trace with $\Phi_q(|\hat V_i^{\mathrm{full}}|)$, which
evaluates the dilogarithm on a per-generator amplitude.  Per-generator
amplitudes are **not** Markov-invariant — different reduced words for
the same braid give different per-generator amplitudes — so the
literal $\Phi_q(|\hat V_i|)$ form is a basis-dependent expansion, not
itself a trace.  At $q_0 \approx 1.11$ the divergence of $\Phi_q$
near $|\hat V_i| \to 1$ amplifies tiny p/n asymmetries into hundreds
of MeV (mirror nuclei T = 1p+2n vs $^3$He = 2p+1n predict T − $^3$He
$\approx -737$ MeV against CODATA $+0.019$ MeV; see
`brane-tower-isospin-diagnosis.witness.json`).

**Trace reformulation (Plancherel series).**
The Heine identity recovers Markov-invariance term-by-term:

$$
  \Phi_q(z) \;=\; (1 - z) \cdot \sum_{n \geq 0} \frac{z^n}{(q^{-1}; q^{-1})_n},
  \qquad (q^{-1}; q^{-1})_n = \prod_{k=1}^{n}(1 - q^{-k}).
$$

With $z = |\hat V_i^{\mathrm{full}}|$ and the standard recognition of
$|\hat V_i|^n$ as the $n$-th power evaluation of the per-generator
transfer-matrix chain, each $z^n$ summand factors through
$\mathrm{tr}_M(\sigma_i^n)$ — which IS Markov-invariant.  See
the formal derivation for a canonical scaffold; the
production wiring depends on the term-trace infrastructure noted
above. An equivalent Kähler-derivative reformulation is available
via the formal derivation (recursion-fixed).

**Proposition.**
*The mass of a vortex $\varrho$ with braid representative
$\beta \in B_n$ and $n - 1$ generators is*

$$
  \mathfrak{m}(\varrho)
  =
  \Bigl\lvert \prod_{i=0}^{n-2} \hat{V}_i^{\mathrm{full}} \Bigr\rvert
  -
  \sum_{i=0}^{n-2}
    \mathrm{Li}_2^q\!\bigl(-\lvert\hat{V}_i^{\mathrm{full}}\rvert\bigr)
  -
  \sum_{0 \leq i < j \leq n-2}
    z^2 \cdot \mathrm{Li}_2^q\!\bigl(-\lvert\hat{V}_i^{\mathrm{full}}
      \cdot \hat{V}_j^{\mathrm{full}}\rvert\bigr),
$$

*where $z = 1/(q^{1/2} + q^{-1/2})$ is the Markov parameter
([Jones--Markov trace](#thm:jones-markov-trace)) and
$\mathrm{Li}_2^q$ is the symmetric q-dilogarithm
$\mathrm{Li}_2^q(z) = \sum_{n \geq 1} z^n / (n \cdot [n]_q)$ with
$[n]_q = (q^n - q^{-n})/(q - q^{-1})$.*

**Note.**
*The previous version of this proposition wrote
$\Phi_q(\lvert\hat V_i\rvert)$ (Faddeev quantum dilogarithm) where this
revision uses $-\mathrm{Li}_2^q(-\lvert\hat V_i\rvert)$ (symmetric
q-dilogarithm).  Both are q-deformations of the classical dilogarithm
but use different q-integer conventions
(asymmetric $(q^n - 1)$ vs symmetric $[n]_q$).  canonical canonical evaluation
`kashaev-integration-identity.witness.json` shows the literal Briggs–Klein
integration evaluates to $-\mathrm{Li}_2^q(-z_p)$ in the symmetric
convention (see proof below).  The Faddeev $\Phi_q$ form is empirically
incompatible with isospin symmetry at $q_0$
(`brane-tower-isospin-diagnosis.witness.json`).*

*The three sums correspond to the three types of blow-up centre
in the brane tower
([topological decomposition](#thm:topological-mass)):*

1. *The **descended term** $\lvert\prod \hat{V}_i^{\mathrm{full}}\rvert$ is the
   base-level **regular-representation (Wedderburn) trace** — the trace of the
   left-multiplication endomorphism
   ([Hecke mass element](#def:hecke-mass-element)) — distinct from the
   single-channel Jones--Markov trace $\prod \hat{V}_i^{\mathrm{std}}$ of the
   categorical-mass reading
   ([categorical mass as Markov trace](#prop:categorical-mass-markov)).*
2. *Each **single-generator blow-up** at generator $i$ contributes
   $\Phi_q(\lvert\hat{V}_i\rvert)$.  (The Markov weight
   $\mathrm{tr}_M(\sigma_i) = z$ is already absorbed into the
   traced volume $\hat{V}_i$, which is computed via the Markov
   trace of the transfer chain.)*
3. *Each **pair blow-up** at the product $\sigma_i\sigma_j$
   (any $i < j$) contributes
   $z^2 \cdot \Phi_q(\lvert\hat{V}_i \hat{V}_j\rvert)$, weighted by
   $\mathrm{tr}_M(\sigma_i\sigma_j) = z^2$.*

*The weight $z^2$ holds for every pair $(i, j)$ with $i < j$ by
the Markov-trace factorization theorem
([Markov trace factorization](#thm:markov-trace-factorization)):
for adjacent generators ($\lvert i - j\rvert = 1$) it reduces
$\sigma_i\sigma_j$ via the Hecke braid relation and applies the
Markov property $\mathrm{tr}_M(x\sigma_{n-2}) = z\,\mathrm{tr}_M(x)$;
for non-adjacent generators ($\lvert i - j\rvert \geq 2$)
far-commutativity makes $\sigma_j$ the rightmost active generator,
and the Markov property peels first $\sigma_j$ then $\sigma_i$ — two
successive Markov reductions each contributing a factor $z$, giving
$\mathrm{tr}_M(\sigma_i\sigma_j) = z^2$.  In both cases the pair
supports an independent blow-up centre at the product spectral
coordinate $\hat{V}_i\hat{V}_j$.*

*The element $\sigma_i\sigma_j\sigma_i$
($\lvert i - j\rvert = 1$) reduces via the Yang--Baxter relation
to $\sigma_j\sigma_i\sigma_j$ and does not contribute an independent
order-3 centre; such triple interactions ascend to the next jet
level ([jet-tower reformulation](#rem:mass-endomorphism-jet-tower))
rather than appearing as explicit cubic terms.*
## Application to the proton--electron mass ratio

For the electron (trefoil $\sigma_1^3$ on $2$ strands,
$1$ generator, additive Wedderburn
$\hat{V}_e^{\mathrm{full}} \approx 0.594$):

$$
  \mathfrak{m}_e
  =
  \lvert\hat{V}_e\rvert
  + \Phi_q(\lvert\hat{V}_e\rvert).
$$

For the proton ($\mathcal{B}_3 \times \mathfrak{u}\mathfrak{u}\mathfrak{d}$
with gluon self-coupling on $3$ strands, $2$ generators,
$\hat{V}_0^{\mathrm{full}} \approx 0.989$,
$\hat{V}_1^{\mathrm{full}} \approx 0.971$):

$$
  \mathfrak{m}_{\mathfrak{p}}
  =
  \lvert\hat{V}_0\hat{V}_1\rvert
  + \Phi_q(\lvert\hat{V}_0\rvert)
  + \Phi_q(\lvert\hat{V}_1\rvert)
  + z^2 \cdot \Phi_q(\lvert\hat{V}_0\hat{V}_1\rvert).
$$

The proton's $11$ crossings (from the $4$-channel production vertex
$\gamma\gamma \to \mathfrak{q}\bar{\mathfrak{q}}$,
[photon channel chain](#rem:photon-channel-wedderburn-chain)) produce
spectral coordinates near $1$, where $\Phi_q$ diverges.  The
electron's $3$ crossings produce $\hat{V}_e \approx 0.594$, well
below the singularity.  The mass ratio is:

$$
  \frac{\mathfrak{m}_{\mathfrak{p}}}{\mathfrak{m}_e}
  \approx 1870
  \qquad (\text{CODATA: } 1836.15, \;\text{error } 1.8\%).
$$

No parameters are fitted.  The inputs are the substrate parameter
$q_0$ and the electron mass $m_e$ (energy scale).

## Gluon derivation from the integer LP dual

The proton's $11$ crossings decompose as $6$ (Borromean
$\mathcal{B}_3$) $+ 3$ (quark Garside $\Delta_3$) $+ 2$ (gluon).
The gluon count is **derived** from the integer LP dual:

1. **LP instability.**  The $9$-crossing element
   $\mathcal{B}_3 \times \Delta_3(\mathfrak{u}\mathfrak{u}\mathfrak{d})$
   violates Frobenius positivity: $(Gx)_\gamma < 0$.

2. **Integer LP.**  Enumerate all feasible integer gluon
   combinations (up to $3$ operations from
   $\{\sigma_0, \sigma_1, L_+, L_-\}$), requiring Frobenius
   stability $Gx \geq 0$ at every intermediate step.
   Among the $84$ feasible solutions, minimize $|\mathrm{tr}_M|$.

3. **Solution: $\sigma_0 \to \sigma_0$** (two bare $\sigma_0$
   crossings on generator\~$0$).  This is the **unique integer
   optimum** with $|\mathrm{tr}_M| = 0.027$ — the closest
   integer point to the continuous LP boundary
   $\mathrm{tr}_M = 0$.

The shadow price is $y_\gamma = -1$: the photon channel
is the sole binding Frobenius constraint.  The gluon's role
is to push the proton from $\mathrm{tr}_M < 0$ (unstable)
to $\mathrm{tr}_M > 0$ (stable) with minimum categorical
action.

**Witness**: `mass-endomorphism.witness.json`.

**Extension beyond $|S| = 2$ (archimedean realisation).**
*The tower formula $\mathrm{Vol}_q^{\mathrm{tower}}(\beta)$ above is
truncated at subset size $|S| \leq 2$.  Higher subset sizes
$|S| \geq 3$ are accessible — but only on the archimedean side of
$\tau \colon R \hookrightarrow \mathbb{C}$ — via the
(jet-GB-PL correspondence).
The $|S| = 3$ contribution corresponds to the simultaneous product
of three colour-sheet prolongations on the color-tube cubic
([baryon product from Alt](#prop:baryon-product-from-alt)), which
under the fibre functor becomes the baryon Picard–Lefschetz period
$\Pi^{(3)}$
(SW-period thimble equivalence).
Higher $|S| \geq 4$ contributions correspond to higher-jet bundles
$J^p\mathcal{S}$ for $p \geq 4$ and their PL evaluations.*

*Strict archimedean split: the truncation at $|S| \leq 2$ is the
maximal $R$-side statement available without invoking PL machinery
(which is intrinsically $\mathbb{C}$-side); the extension to
$|S| \geq 3$ requires moving across $\tau$ and so is recorded as an
archimedean addendum, not as part of the $R$-side tower formula.*

**Archimedean specialisation (§7c).** The proton–electron ratio is stated over $\mathbb{R}$ (a real Frobenius-norm map $\mathbb{R}\to\mathbb{R}$ and real $q, v$); it is the archimedean numerical evaluation of the generic mass-endomorphism tower, acknowledged here.
<!-- FILE_END: mass-endomorphism-tower.md -->

<!-- FILE_START: mass-endomorphism-jet-tower.md -->
Let $(\mathbf{C}, A, \tau)$ be a
([quantum observable universe](#def:quantum-observable-universe)) with
substrate parameter $q$ and jet tower
$A_{n+1} = A_n \otimes \Omega^1(A_n)$
([recursive brane tower](#def:recursive-brane-tower)). Let
$\hat{V}_i^{\mathrm{full},(n)}$ denote the additive Wedderburn
traced volume at generator $i$ evaluated at jet level $n$.

This remark reframes
([mass endomorphism tower](#prop:mass-endomorphism-tower))
in **jet-brane** language.

## Sufficiency of quadratic terms per jet level

The prop's formula keeps at most quadratic $\hat{V}_i \hat{V}_j$
spectral coordinates (the $z^2 \Phi_q(|\hat V_i \hat V_j|)$ term)
and no explicit triple or higher terms. This is not a truncation
in the prop: it is the intended content.

$q$ calculations are not linear: the Hecke relation
$\sigma_i^2 = H_A \sigma_i + 1$ is quadratic, and the pentagon
identity of $\Phi_q$ ([quantum Bloch group](#def:quantum-bloch-group))
closes on pairs. **Per jet level**, the transient contribution
therefore contains:

* **$\Phi_q(|\hat V_i|)$ singletons** (order-1: single blow-up centres).
* **$z^2 \Phi_q(|\hat V_i \hat V_j|)$ pairs** (order-2: quadratic
 blow-up centres, $i < j$).

The **descended** contribution is **not** summed over jet levels.
By ([:refterm[descent]{#descent} eigenspaces](#prop:descent-eigenspaces)) the descended
subalgebra
$\mathcal{A}^{\mathrm{desc}} = \mathrm{im}\,\hat{\tau}_n$ is the
image of the :refterm[descent]{#descent} involution onto the base level; it carries
a **single** holonomy contribution from the level-$0$ unknot core
$\varrho_0$ ([topological mass proof](#prf:topological-mass), Step 2).
Successive jet prolongations add only transient modes
$\mathcal{A}_{n+1}^{\mathrm{trans}} = \ker\hat\tau_n$ (the modes
with no pre-image at level $n$, cf.
([:refterm[descent]{#descent} involution](#def:descent-involution))). Including a
separate descended product at every jet level would double-count
the level-$0$ holonomy.

A triple or quadruple interaction at level $n$ is not an
independent order-3/4 term; it ascends to jet level $n+1$ as a
new singleton or pair, and is already captured by the
level-$(n{+}1)$ contribution in the tower sum.

## Pentagon ascension of higher-order interactions

The quantum dilogarithm satisfies the **pentagon identity**
([quantum Bloch group](#def:quantum-bloch-group)): for operators
$u, v$ with $uv = q\,vu$,

$$
  \Phi_q(v)\,\Phi_q(u) \;=\; \Phi_q(u)\,\Phi_q(uv)\,\Phi_q(v).
$$

Applied to a would-be order-3 contribution
$\Phi_q(|\hat V_i^{(n)} \hat V_j^{(n)} \hat V_k^{(n)}|)$ with
$u = \hat V_i^{(n)} \hat V_j^{(n)}$ and $v = \hat V_k^{(n)}$, the
pentagon relation rewrites the triple as a product of order-$\leq 2$
factors at level $n$ plus a residual that cannot be absorbed at
level $n$. The unabsorbed residual is the image of the jet
prolongation map
$\mathcal{A}_n \to \mathcal{A}_{n+1}^{\mathrm{trans}}$ on the
$uv$-module — a new singleton or pair blow-up centre at
**level $n+1$**. Iterating the pentagon over all triples shows
the same pattern for every higher order: level-$n$ closure is
quadratic, and all defects of order $\geq 3$ ascend one jet level.

The full mass is therefore a tower sum with **one** descended
term (at $n=0$) and per-level transient contributions:

```tex
\begin{equation}\label{eq:jet-tower-mass}
  \mathfrak{m}(\varrho)
  =
  \underbrace{\bigl\lvert\textstyle\prod_i \hat V_i^{(0)}\bigr\rvert}_{\text{descended (level 0 only)}}
  +
  \sum_{n=0}^{N}
    \Bigl(
    \underbrace{\textstyle\sum_i \Phi_q(|\hat V_i^{(n)}|)}_{\text{singletons}_n}
    + \underbrace{z^2 \textstyle\sum_{(i,j) \in \mathcal{P}_n}
       \Phi_q(|\hat V_i^{(n)} \hat V_j^{(n)}|)}_{\text{quadratic pairs}_n}
    \Bigr)
\end{equation}
```

where $\mathcal{P}_n$ is the set of pair blow-up centres at jet
level $n$.

## $\mathcal{P}_n$ is the full set $\{(i,j) : i < j\}$ at every level

The pair set is the full set of unordered pairs at every jet level,
not only adjacent ones — the Markov-trace factorization theorem
gives weight $z^2$ for every pair $(i, j)$, by the same argument
([mass endomorphism tower](#prop:mass-endomorphism-tower) §proof,
Markov-trace factorization paragraph) used at level $0$. The jet
ascension argument above lifts that level-$0$ proof to every
subsequent level.

The empirical verification on stable atoms $A \geq 6$:

See [Table 1](#tbl:mass-endomorphism-jet-tower-table1-data).

Including all pair centres closes the 2–3% heavy-atom bias to
under 1%, consistent with the categorical derivation.

Triple terms with $z^3 \Phi_q(|\hat V_i \hat V_j \hat V_k|)$
inserted as explicit level-$n$ contributions overshoot the target
(0.6–1.3% at the same atoms), confirming the pentagon ascension:
order-$\geq 3$ defects belong at level $n+1$, not as explicit
cubic terms at level $n$
(see `adjacent-vs-full-canonical evaluation.witness.json`).

## Remaining open subconjectures

1. **Jet-level sum convergence** — *(conjectural)* path-(b) closure via
 [`conj:jet-tower-uniform-delta-max`](#conj:jet-tower-uniform-delta-max)
 (workplan **P3.4** path (b)). A geometric-series tail bound
 has been proved conditional on uniform boundedness of
 $\Delta^{(n)}$
 ([brane-tower tail bound](#prop:jet-tower-convergence)):
 if $|\Delta^{(n)}| \leq \Delta_{\max}$ for all $n$, then the
 $N$-term truncation error is
 $\leq \Delta_{\max} \hbar_q^{2(N+1)} / (1 - \hbar_q^{2})$.
 The uniform bound is now an explicit conjecture with empirical
 support: the
 the canonical formalism
 measurement formalism confirms `uniform_bound_pass = true` for
 D, T, ${}^{3}$He across $n = 1, \dots, 7$. The path-(a) proof from
 GS spectral-sequence $E_2$-collapse remains open.
2. **Pentagon $\to$ uv-commutation** — *(resolved)* by
 [`lem:vhat-pair-commutation-trace`](#lem:vhat-pair-commutation-trace).
 The traced volumes $\hat V_i \in \mathbb{Z}[q^{\pm 1/2}, z]$
 are scalar polynomials and commute by definition; the pentagon
 identity in its operator form does not apply to scalars. The
 ascension argument's rigorous content is Markov-trace
 factorization
 ([thm:markov-trace-factorization](#thm:markov-trace-factorization))
 plus the brane-tower's $q$-graded jet ascension between
 adjacent levels — which is where the operator pentagon $uv =
   q\,vu$ does apply (on inter-level lifts $\widehat U_i$,
 $\widehat V_j$).
3. **:refterm[Descent]{#descent} involution on pairs / pair-formula sharpness** — *(resolved)*
 resolved by
 [`lem:tower-pair-equality-fixed-level`](#lem:tower-pair-equality-fixed-level).
 The level-$n$ pair contribution $z^2 \sum_{(i, j) \in
   \mathcal{P}_n} \Phi_q(|\hat V_i^{(n)} \hat V_j^{(n)}|)$ is an
 **exact equality**, not an upper bound — the pentagon-bound
 framing was vacuous (per item 2 above the pentagon doesn't apply
 to scalar $\hat V$'s), and the Markov-pair identity
 ([prop:markov-pair-z2](#prop:markov-pair-z2)) is itself an
 equality. The empirical residual to CODATA at light atoms
 ($\sim 0.5$–$0.9\%$) reflects incomplete tower truncation
 (level $\ge 1$ contributions), not a sharpness gap in the
 level-$n$ formula. The remaining open piece is the uniform
 $\Delta_{\max}$ bound for the truncation-error formula
 ([prop:jet-tower-convergence](#prop:jet-tower-convergence)),
 tracked as workplan **P3.4** (item 1 above).
<!-- FILE_END: mass-endomorphism-jet-tower.md -->

