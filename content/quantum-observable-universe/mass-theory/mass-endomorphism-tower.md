> **TOP-OF-FILE SUPERSEDED-$\rho_q$ BANNER (promoted).**
> The substrate density $\rho_q = 1/\hbar_q^2$ used in the algebraic
> form below is **STRUCTURALLY WRONG** per the inline SUPERSEDED
> note (lines 28-51). The correct dimensional factor is the
> operator-valued $A^\lambda_{\mu, \nu}(I)$ from
> [`prop:hecke-branching-trace-decomposition`](#prop\:hecke-branching-trace-decomposition);
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
([quantum observable universe](#def\:quantum-observable-universe)).
Let $\hat{V}_i^{\mathrm{full}}$ denote the additive Wedderburn traced
volume at generator $i$
([three-invariant mass formula](#sec\:atomic-braid-mass)).

### Algebraic form

Via the Kashaev volume--density reading
([Kashaev volume--density](#rem\:kashaev-volume-density)), the tower
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
([quantum Planck constant](#def\:quantum-planck-constant)) and*

**SUPERSEDED.** *The substrate-only ansatz
$\rho_q = 1/\hbar_q^2 \approx 102$ is **structurally wrong**: it is
braid-class-independent, but the categorical density $\rho_K$
varies $\sim 30\times$ across atoms ($A = 1$ to $A = 3$;
[graded ρ\_K expansion](#prop\:rho-k-graded-expansion)). The
correct dimensional factor is the **operator-valued**
$A^\lambda_{\mu, \nu}(I) \in \mathrm{End}(V_\mu \otimes V_\nu)$
from [hecke branching trace decomp](#prop\:hecke-branching-trace-decomposition),
which depends on the specific braid through its LR-block decomposition.
The iterated $(Z+N)$-factor extension to atomic braids — explicitly
replacing the scalar Wedderburn-volume tower with the operator-trace
form — is stated in [`prop:mass-tower-operator-valued`](mass-tower-operator-valued.md)
(authored as the Stage-1 unblock).
The graded expansion
$\mathcal{M}(K)/(m_e \cdot |\!\operatorname{tr}_M(\mathcal{B}_K)|) = \rho_K^{\mathrm{LO}} + \rho_K^{\text{single-gen}} + \rho_K^{\text{pair-gen}} + \dots$
([prop:rho-k-graded-expansion](#prop\:rho-k-graded-expansion))
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
([Markov trace product](#thm\:markov-trace-product)), and
$z = 1/(q^{1/2} + q^{-1/2})$ the Markov parameter.*

Every per-generator contribution is a finite Laurent polynomial in $q$;
no quantum-dilogarithm evaluation is required to **state** the tower.
The archimedean realisation $\mathrm{Vol}_{q}^{(S)} \rightsquigarrow
\Phi_{q}$ is a specialisation via the Kashaev limit, recorded in the
expanded form below.

### Quantum-dilogarithm form (archimedean specialisation)

Let $\Phi_q(z) = \prod_{k=1}^{\infty}(1 - q^{-k}z)^{-1}$ denote
the non-perturbative quantum dilogarithm
([quantum Bloch group](#def\:quantum-bloch-group)).

**Kashaev-integration-identity audit (added).**
*The proof step claims*

$$
  \Phi_q(z_p) \;=\; \int_0^{z_p} \frac{\ln_q(1+t)}{t}\,dt
              \;=\; \prod_{k\geq 1}(1 - q^{-k} z_p)^{-1}.
$$

*Numerical probe (`kashaev-integration-identity.witness.json`): the
left integral at $q_0 \approx 1.110$ for $V \in (0, 1)$ is bounded
in $[0.1, 0.82]$, while the right-hand product $\Phi_q(V)$ grows
unboundedly (e.g. $\Phi_q(0.989) \approx 6.7 \times 10^5$).  The
two sides differ by 6 orders of magnitude at $V = 0.989$ — the
identity does NOT hold numerically.*

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

*The paper's `prop:atomic-braid-mass` uses the alternative form
$\tfrac{\alpha}{2} \cdot \sum_i \ln(\hat V_i^{\mathrm{full}} \cdot \overline{\hat V_i^{\mathrm{full}}})$ (with $\alpha = m_e \cdot 8G$,
the Borromean binding scale `prop:binding-scale-catalan`), which gives
0.19% mean atomic-mass error across $Z = 1$..$10$ with zero fitted
parameters — but the integration probe shows the
$\int (\ln_q(1+t)/t)\,dt = -\mathrm{Li}_2^q(-V)$ identity doesn't
reduce to $\alpha \cdot \ln|V|$ either.*

*Both forms above are concrete evaluations of the abstract GB-NF
statement
([atomic mass via GB-NF](#prop\:atomic-mass-gb-nf))
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
[`canonical_plus_multibrane.py`](computations/canonical_plus_multibrane.py)
and
[`paper_six_term_isotope_sweep.py`](computations/sweeps/paper_six_term_isotope_sweep.py)
use `tower_mode="li2q"` and evaluate $-\mathrm{Li}_2^q(-|V|)$ via the
symmetric q-dilogarithm series
$\mathrm{Li}_2^q(z) = \sum_{n \geq 1} z^n / (n \cdot [n]_q)$. The
$\Phi_q$ product form survives only in
[`brane_tower_isospin_diagnosis.py`](computations/brane_tower_isospin_diagnosis.py)
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
`brane_tower_plancherel_scaffold.py` for a numerical scaffold; the
production wiring depends on the term-trace infrastructure noted
above. An equivalent Kähler-derivative reformulation is available
via `kahler_lift.py` (recursion-fixed).

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
([Jones--Markov trace](#thm\:jones-markov-trace)) and
$\mathrm{Li}_2^q$ is the symmetric q-dilogarithm
$\mathrm{Li}_2^q(z) = \sum_{n \geq 1} z^n / (n \cdot [n]_q)$ with
$[n]_q = (q^n - q^{-n})/(q - q^{-1})$.*

**Note.**
*The previous version of this proposition wrote
$\Phi_q(\lvert\hat V_i\rvert)$ (Faddeev quantum dilogarithm) where this
revision uses $-\mathrm{Li}_2^q(-\lvert\hat V_i\rvert)$ (symmetric
q-dilogarithm).  Both are q-deformations of the classical dilogarithm
but use different q-integer conventions
(asymmetric $(q^n - 1)$ vs symmetric $[n]_q$).  Numerical probe
`kashaev-integration-identity.witness.json` shows the literal Briggs–Klein
integration evaluates to $-\mathrm{Li}_2^q(-z_p)$ in the symmetric
convention (see proof below).  The Faddeev $\Phi_q$ form is empirically
incompatible with isospin symmetry at $q_0$
(`brane-tower-isospin-diagnosis.witness.json`).*

*The three sums correspond to the three types of blow-up centre
in the brane tower
([topological decomposition](#thm\:topological-mass)):*

1. *The **descended term** $\lvert\prod \hat{V}_i^{\mathrm{full}}\rvert$ is the
   base-level **regular-representation (Wedderburn) trace** — the trace of the
   left-multiplication endomorphism
   ([Hecke mass element](#def\:hecke-mass-element)) — distinct from the
   single-channel Jones--Markov trace $\prod \hat{V}_i^{\mathrm{std}}$ of the
   categorical-mass reading
   ([categorical mass as Markov trace](#prop\:categorical-mass-markov)).*
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
([Markov trace factorization](#thm\:markov-trace-factorization)):
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
level ([jet-tower reformulation](#rem\:mass-endomorphism-jet-tower))
rather than appearing as explicit cubic terms.*

*Proof.*
The Hecke mass element $\Phi_{\mathrm{mass}}(\beta) \in H_n(R, q)$
([Hecke mass element](#def\:hecke-mass-element)) decomposes via the
:refterm[descent]{#descent} involution into descended and transient contributions.  The
transient trace localises to blow-up centres $p$ in the brane tower
([topological decomposition](#thm\:topological-mass)); integrating the
$q$-deformed expansion flow $\ln_q(1+t)/t$ along the radial
coordinate of the Briggs--Klein chart
([Briggs--Klein chart](#def\:briggs-klein-chart)) over each resolved
defect $E_i \cong \mathbb{P}^1(\mathbb{C})$ yields the symmetric
q-dilogarithm:

$$
  \int_0^{V} \frac{\ln_q(1+t)}{t}\,dt
  \;=\; -\mathrm{Li}_2^q(-V),
  \qquad
  \mathrm{Li}_2^q(z) := \sum_{n \geq 1} \frac{z^n}{n \cdot [n]_q},
$$

*where $[n]_q = (q^n - q^{-n})/(q - q^{-1})$ is the symmetric
q-integer.*

*Subproof.*  The q-deformed natural log has Taylor series
$\ln_q(1-z) = -\sum_{n\geq 1} z^n/[n]_q$ (\[definition of q-log]).
Termwise differentiation of $\mathrm{Li}_2^q$ gives\*

$$
  \frac{d}{dz}\mathrm{Li}_2^q(z)
  = \sum_{n \geq 1} \frac{z^{n-1}}{[n]_q}
  = -\frac{\ln_q(1-z)}{z}.
$$

*Integrating from $0$ to $z$ (with $\mathrm{Li}_2^q(0) = 0$):
$\mathrm{Li}_2^q(z) = -\int_0^z (\ln_q(1-u)/u)\,du$.  Substituting
$u = -t$, $z = -V$:*

$$
  \mathrm{Li}_2^q(-V)
  = -\int_0^{-V}\!\frac{\ln_q(1-u)}{u}du
  = -\int_0^{V}\!\frac{\ln_q(1+t)}{t}dt
$$

*so $\int_0^V (\ln_q(1+t)/t)\,dt = -\mathrm{Li}_2^q(-V)$.  $\square_{\text{sub}}$*

*Numerical verification: the integration value matches
$-\mathrm{Li}_2^q(-V)$ to all displayed digits at $q_0 \approx 1.110$
for $V \in \{0.1, 0.3, 0.5, 0.7, 0.85, 0.95, 0.989\}$
(`kashaev-integration-identity.witness.json`).*

*Earlier versions of this proof identified the integral with the
Faddeev quantum dilogarithm $\Phi_q(V) = \prod_{k\geq 1}(1 - q^{-k}V)^{-1}$,
whose logarithm uses asymmetric q-integers $(q^n - 1)$.  Both
$\mathrm{Li}_2^q$ and $\log\Phi_q$ are q-deformations of the
classical dilogarithm, but they use different q-integer conventions;
the Hecke setting requires the symmetric form $[n]_q$, so
$\mathrm{Li}_2^q$ is the correct identification.*

The NF basis of $H_n(R, q)$ decomposes by generator content.  Each
subset $S \subseteq \{0,\dots,n-2\}$ contributes a blow-up centre
with spectral coordinate $\prod_{i\in S}\hat{V}_i$ and Markov
weight $z^{|S|}$; triples and higher generator subsets are not
independent at level $n$ (they ascend to jet level $n+1$ via the
pentagon closure of $\Phi_q$, see
[quantum Bloch group](#def\:quantum-bloch-group)).  The independent
order-1 and order-2 subsets enumerate exactly the singleton and
pair sums above.

For the adjacent pair $\{i, i+1\}$ the NF elements
$\sigma_i\sigma_{i+1}$ and $\sigma_{i+1}\sigma_i$ share the same
spectral support $\hat{V}_i\hat{V}_{i+1}$ (the same blow-up centre,
distinct elements of $H_n(R, q)$ modulo Yang--Baxter); their combined
weight is $z^2$, not $2z^2$.  For a non-adjacent pair
$\{i, j\}$ with $\lvert i-j\rvert\geq 2$ far-commutativity gives
$\sigma_i\sigma_j = \sigma_j\sigma_i$ and
$\mathrm{tr}_M(\sigma_i\sigma_j) = z \cdot z = z^2$ — a single NF
element supporting a single blow-up centre.  In every case the
combined pair weight is $z^2$.  Summing over all pairs $i<j$ gives
the claimed quadratic term.

The element $\sigma_0\sigma_1\sigma_0$ is not an independent blow-up
centre: it decomposes as $\sigma_1\sigma_0\sigma_1$ via Yang--Baxter,
the same transient support as the adjacent pair.  Higher-order
subsets of size $\geq 3$ are similarly subsumed — not into level-$n$
singletons and pairs, but into the level-$(n{+}1)$ jet contribution
via the pentagon identity of the quantum dilogarithm (for the
explicit ascension see [jet-tower reformulation](#rem\:mass-endomorphism-jet-tower)).
$\square$

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
[photon channel chain](#rem\:photon-channel-wedderburn-chain)) produce
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
([jet-GB-PL correspondence](#prop\:jet-gb-pl-correspondence)).
The $|S| = 3$ contribution corresponds to the simultaneous product
of three colour-sheet prolongations on the color-tube cubic
([baryon product from Alt](#prop\:baryon-product-from-alt)), which
under the fibre functor becomes the baryon Picard–Lefschetz period
$\Pi^{(3)}$
([SW-period thimble equivalence](#prop\:sw-period-thimble-equivalence)).
Higher $|S| \geq 4$ contributions correspond to higher-jet bundles
$J^p\mathcal{S}$ for $p \geq 4$ and their PL evaluations.*

*Strict archimedean split: the truncation at $|S| \leq 2$ is the
maximal $R$-side statement available without invoking PL machinery
(which is intrinsically $\mathbb{C}$-side); the extension to
$|S| \geq 3$ requires moving across $\tau$ and so is recorded as an
archimedean addendum, not as part of the $R$-side tower formula.*
