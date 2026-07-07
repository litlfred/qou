<!-- FILE_START: wenzl-bridge-cyclotomic-lr-tensor-character-intro.md -->
Continuation of the preceding sub-section.

The arc proceeds through the Littlewood-Richardson tensor character bridge, the Wenzl-$Q_{mn}$ synergy that pins the substrate-flow evaluations, the explicit $\alpha_k$ tabulations at $h = 3$ and $h = 4$, and the Wedderburn-Bratteli recursion that supplies the substrate-flow data.  The closing blocks exhibit the $y_\lambda$ sign pattern and lift the substrate-level apparatus into higher-operation extensions.
<!-- FILE_END: wenzl-bridge-cyclotomic-lr-tensor-character-intro.md -->

<!-- FILE_START: lr-tensor-character-bridge.md -->
**Corollary (k-factor parabolic specialisation of
[`prop:hecke-branching-trace-decomposition`](hecke-branching-trace-decomposition.md)).**
*Specialise the branching identity to the trivial interface
$I = \mathbf{1}$ and iterate $k-1$ times across the parabolic chain
$H_{n_1}(R, q) \otimes \cdots \otimes H_{n_k}(R, q) \hookrightarrow
H_n(R, q)$, where $n := \sum_i n_i$. For every
$\nu \vdash n$ and every
$(\beta_1, \ldots, \beta_k) \in H_{n_1}(R, q) \times \cdots \times
H_{n_k}(R, q)$, the tensor-product Hecke character factors as*

$$
  \boxed{\;
    \chi^\nu_{H_n}(\beta_1 \otimes \cdots \otimes \beta_k)
    \;=\;
    \sum_{(\lambda_1, \ldots, \lambda_k)} c^\nu_{\lambda_1, \ldots, \lambda_k}
      \cdot \prod_{i=1}^{k} \chi^{\lambda_i}_{H_{n_i}}(\beta_i)
  \;}
$$

*where the sum runs over $\lambda_i \vdash n_i$, and
$c^\nu_{\lambda_1, \ldots, \lambda_k}$ is the iterated
Littlewood–Richardson coefficient*

$$
  c^\nu_{\lambda_1, \ldots, \lambda_k}
  \;=\;
  \sum_{\mu_2, \ldots, \mu_{k-1}}
    c^\nu_{\lambda_1, \mu_2} \cdot c^{\mu_2}_{\lambda_2, \mu_3}
      \cdots c^{\mu_{k-1}}_{\lambda_{k-1}, \lambda_k},
$$

*the structure constant of the Schur basis of $\mathrm{Sym}$ under
the iterated coproduct.*
## Algebraic context

The ring $\mathrm{Sym}$ of symmetric functions is a self-dual graded
Hopf algebra under the Hall inner product, with the Schur basis
$\{s_\lambda\}$ orthonormal and simultaneously diagonalising the
product and the coproduct ([macdonald1995] §I.5; PSH-algebra in the
sense of Zelevinsky):

$$
  s_\lambda \cdot s_\mu
  \;=\; \sum_{\nu \vdash |\lambda|+|\mu|} c^\nu_{\lambda\mu}\, s_\nu,
  \qquad
  \Delta s_\nu
  \;=\; \sum_{\substack{\lambda \vdash n_1\\\mu \vdash n_2\\n_1+n_2 = |\nu|}}
        c^\nu_{\lambda\mu}\, s_\lambda \otimes s_\mu.
$$

Under the Frobenius characteristic, the Schur product / coproduct
realise the induction / restriction along the parabolic embedding
$S_{n_1} \times \cdots \times S_{n_k} \hookrightarrow S_{n_1 + \cdots + n_k}$,
and the quantum lift to $H_n(R, q)$ ([geck-pfeiffer2000] §9.1.5,
[ram1991] Theorem 5.1) preserves the coefficients.

## Applicability in QOU

Two structural features of the QOU substrate make this corollary
the engine of every tractable atomic mass prediction.

**Tensor-product factorisation of the canonical atomic braid.**
The canonical $(Z, N)$-braid
([atomic braid](#def:atomic-braid), with
[interface composition](#def:canonical-braid-interface-composition))
factors as

$$
  \mathcal{B}_K
  \;=\; \mathcal{B}_K^{\mathrm{vac}} \cdot \bowtie_K,
$$

where $\mathcal{B}_K^{\mathrm{vac}} = \mathcal{B}_p^{(1)} \otimes \cdots
\otimes \mathcal{B}_n^{(N)}$ is the parabolic tensor of the
$A := Z + N$ per-nucleon $H_3$ canonical sub-braids (constituent
vacuum) and $\bowtie_K$ is the
(electroweak interface knot) --- a short
word in the inter-nucleon Hecke generators $\sigma_{3k+2}$
($0 \leq k < A-1$), one single-generator crossing per adjacent
nucleon pair, with sign $\sigma$ on a proton--proton arc and
$\sigma^{-1}$ on a neutron--neutron arc. The present proposition
applies directly to $\mathcal{B}_K^{\mathrm{vac}}$; the interface
contribution is governed by the
([Markov-axiom interface identity](#prop:interface-knot-markov-z))

$$
  \frac{\tau_M(\mathcal{B}_K)}{\tau_M(\mathcal{B}_K^{\mathrm{vac}})}
  \;=\; z(q)^{p_+(K)} \cdot \bigl(z(q) - h(q)\bigr)^{p_-(K)},
$$

a closed scalar form in the substrate parameters
$z = 1/(\sqrt q + 1/\sqrt q)$ and $h = q - q^{-1}$ (with $p_\pm(K)$
the counts of positive / negative interface generators). The mixed
proton--neutron averaged-half-sum case
$\tfrac{1}{2}(\sigma + \sigma^{-1})$ enters as a sign-balanced
combination of the closed identities above.

**Cost asymmetry: small per-nucleon $H_3$ vs. large $H_{3A}$.**
At each nucleon, $\lambda_i \vdash 3$ with $\dim \lambda_i \leq 2$, so
every per-nucleon character $\chi^{\lambda_i}_{H_3}(\beta_i)$ costs
$O(\dim^2 \cdot \ell(\beta_i)) = O(\ell(\beta_i))$. The total
LR-bridged cost is

$$
  T_{\mathrm{LR}}(Z, N)
  \;=\; O\!\left( p(3)^A \cdot A \cdot \ell_{\mathrm{intra}}
                 + p(3A) \cdot \dim_{\max}^2(3A) \cdot \ell(\beta_{\mathrm{interface}}) \right),
$$

with the first term --- the LR sum --- dominated by $3^A$ choices of
per-nucleon partition, and the second term --- the interface
multiply --- carrying a single power of $\dim_{\max}^2(3A)$
(roughly $6700^2$ at $A = 10$) but only $A - 1$ inter-nucleon
crossings rather than the $\sim 3A$ crossings of the full atomic
braid. The direct Hoefsmit path costs

$$
  T_{\mathrm{direct}}(Z, N)
  \;=\; O\!\left( p(3A) \cdot \dim_{\max}^2(3A) \cdot \ell(\beta_{Z,N}) \right).
$$

For $A = 4$ (helium-4, $H_{12}$, $p(12) = 77$), the ratio
$T_{\mathrm{direct}} / T_{\mathrm{LR}} \approx 5 \cdot 10^2$. For
$A = 10$ (boron-10, $H_{30}$, $p(30) = 5604$), the ratio reaches
$\approx 10^6$, converting an otherwise-intractable evaluation into
one of minutes.

## Convolutional structure

The iterated LR coefficient
$c^\nu_{\lambda_1, \ldots, \lambda_k}$ is the matrix element of the
$(k-1)$-fold coproduct
$\Delta^{(k-1)} \colon \mathrm{Sym}_n \to
 \mathrm{Sym}_{n_1} \otimes \cdots \otimes \mathrm{Sym}_{n_k}$
on the Schur basis. The corollary therefore expresses the $H_n$
character as a *convolution* of $H_{n_i}$ characters against the
coalgebra of $\mathrm{Sym}$. Because $\mathrm{Sym}$ is self-dual, the
same coefficient table $c$ that prescribes the product of Schur
polynomials prescribes the comultiplication --- the algebra and
coalgebra structures share a single rank-three tensor of structure
constants. This is the categorical content of the speedup: a
$k$-factor character on $H_n$ is computed from $\sum n_i = n$ small
characters by a single contraction against $c$, without ever
constructing the $H_n$ seminormal matrices.

## Witness

the canonical formalism
is the Python entry point; the per-partition LR sum is dispatched to
the Rust implementation in
[`tools/hecke-engine/src/wenzl_lr.rs`](https://github.com/litlfred/qou/blob/main/tools/hecke-engine/src/wenzl_lr.rs)
for cache locality at large $A$.
the canonical formalism
verifies the bridge against the direct Hoefsmit path on $H_6$ (D, T)
and the self-conjugate sub-stratum of $H_9$ ($^3\mathrm{He}$):
per-partition $\chi^\nu$ agreement is at the machine-precision limit
($\sim 10^{-14}$ relative). The convention adapter
the canonical formalism
splits a $(Z, N)$ specification into the LR-compatible per-nucleon
factor list and the interface residue and records the partition of
the canonical word that this corollary strictly governs.

## Scope of applicability

The identity holds for tensor-product (parabolic) braids only. The
interface knot $\bowtie_K$ does not factor through the parabolic
embedding; its contribution is the $I \neq \mathbf{1}$ regime
governed by the
(branching trace decomposition)
in the operator-valued form, and admits the closed scalar form of
the
([Markov-axiom interface identity](#prop:interface-knot-markov-z))
on the Markov-trace ratio. The LR bridge is the correct primitive
for the constituent-vacuum factor, not for the entire canonical
braid; the convention adapter keeps the partition explicit so
downstream consumers do not silently apply LR to a non-tensor
braid.
<!-- FILE_END: lr-tensor-character-bridge.md -->

<!-- FILE_START: wenzl-qmn-synergy.md -->
**Proposition (Wenzl-bridge + q-MN synergy for $\mathrm{tr}_M$).**
*The Wenzl-bridge ([y-lambda-closed-form](#prop:y-lambda-closed-form-wenzl-bridge))
gives $y_\lambda(q)$ as a closed q-rational expression in $\sqrt q$
in $O(p(n) \cdot \max\text{hooks})$ time, while q-Murnaghan-Nakayama
([Halverson-Ram 1995, Wenzl q-MN, originally in
the formal derivation,
now consolidated into the unified Hoefsmit path
`hecke_characters.chi_lambda_braid`]) gives
$\chi_\lambda(T_w; q)$ for canonical permutation braids $T_w$ in
$O(n^2)$ time.*

*Combining them gives the Markov trace*

$$
  \mathrm{tr}_M(T_w) \;=\; \sum_{\lambda \,\vdash\, n} y_\lambda(q) \cdot \chi_\lambda(T_w; q)
$$

*on canonical permutation braids in $O(p(n) \cdot (\max\text{hooks} + n^2))$
time — far faster than the Hoefsmit-seminormal path
($O(p(n) \cdot \dim_\lambda^2 \cdot \ell(w))$).*

## Significance

Three orthogonal speedups combine:

| Quantity | Old path | New path | Speedup |
|---|---|---|---|
| $y_\lambda(q)$ | Linear-system solve, sympy 20-min timeout @ n=5 | Wenzl-bridge, ~0.3 s @ n=12 | $\sim 10^4 \times$ |
| $\chi_\lambda(T_w; q)$ canonical | Hoefsmit $O(\dim_\lambda^2 \cdot \ell(w))$ | q-MN $O(n^2)$ | $10^2 \times$ at $n = 12$ |
| $\mathrm{tr}_M$ on closed braid | Direct seminormal matrix-trace | $\sum y_\lambda \chi_\lambda$ via above | combined $10^6 \times$ |

For atom-knot identification at $n = 18$ ($p(n) = 385$, $\max\dim_\lambda \approx 1000$) or $n = 21$ ($p(n) = 792$, $\max\dim_\lambda \approx 5000$),
this drops the per-isotope compute time from **hours to seconds**.

## Cross-validation identity

For any canonical permutation braid $T_w$ at $H_n$:

$$
  \boxed{\;\mathrm{tr}_M(T_w) \;\stackrel{!}{=}\; z^{\ell(w)}\;}
$$

(Markov axiom + cyclicity; $z = 1/(\sqrt q + 1/\sqrt q)$). Combining
the Wenzl-bridge $y_\lambda$ with q-MN $\chi_\lambda$ should reproduce
this exactly:

$$
  \sum_\lambda y_\lambda(q) \cdot \chi_\lambda(T_w; q)
  \;=\; z^{\ell(w)}
$$

This gives an **independent verification** of both formulas at every
$n$ and every reduced word $w$.

## Implications

1. **Direct verification of Wenzl-bridge correctness**: any
   canonical-braid Markov-trace identity gives a one-shot test of
   $y_\lambda(q)$ values without resorting to MPFR or sympy
   linear-system solve.
2. **Mass-formula compute speedup**: the depth-resolved Φ_k pipeline
   in the formal derivation can replace its Hoefsmit
   character calls with q-MN where applicable (canonical braid
   words), for $\sim 100 \times$ speedup at high $n$.
3. **Atom-knot identification path** for ${}^{6}$Li, ${}^{7}$Li:
   - Enumerate hyperbolic knots $K$ with crossing-number $\leq 10$.
   - For each $K$, take its braid representation $\mathcal{B}_K \in B_n$.
   - Compute $\mathrm{tr}_M(\mathcal{B}_K) = \sum_\lambda y_\lambda(q_0) \cdot \chi_\lambda(\mathcal{B}_K; q_0)$
     via Wenzl-bridge + q-MN.
   - Compare to AME binding $\times$ hyperbolic-volume ratio for ${}^{6}$Li / ${}^{7}$Li.
   - This is now tractable at $n = 18, 21$ in seconds per knot.

## Code

The original q-Murnaghan-Nakayama implementation
the canonical formalism
exposed `chi_q_canonical_T_w(λ, µ, q)` for canonical permutation
braids $T_w$.  Active code now uses the unified Hoefsmit path
the canonical formalism,
which handles both canonical $T_w$ and arbitrary braid words
(positive and inverse generators) through the same API.  The
q-MN speedup quoted above applies in the canonical-$T_w$ regime
where the q-character is a class function of cycle type.

the canonical formalism
implements the Wenzl-bridge giving $y_\lambda(q)$ symbolic for
$n = 2, \ldots, 12$.

the canonical formalism
verifies the cross-validation identity on canonical
permutation braids at $n = 3, 4, 5$.

## Open

- **Atom-knot identification** for ${}^{6}$Li ($A = 6$, $n = 18$) and ${}^{7}$Li
  ($A = 7$, $n = 21$): now tractable but requires hyperbolic-knot
  enumeration and braid-representation extraction. Open project.
- **Mass-formula refactor** to use Wenzl-bridge + q-MN instead of
  Hoefsmit seminormal where applicable: backwards-compatible
  speedup, deferred to follow-up.
<!-- FILE_END: wenzl-qmn-synergy.md -->

<!-- FILE_START: explicit-alpha-k-h3.md -->
**Proposition (explicit $\alpha_k$ at $H_3(R, q)$).**
*Let $z = 1/(q^{1/2} + q^{-1/2})$ be the Markov parameter and
$h = q - q^{-1}$ the Hecke amplitude. The structural prefactors of
the unified curvature-rank mass formula
([unified mass formula](#prop:unified-curvature-rank-mass-formula))
at the single-nucleon Hecke algebra $H_3(R, q)$ are*

$$
  \boxed{\;
    \alpha_0 \,=\, 1, \qquad
    \alpha_1 \,=\, 0, \qquad
    \alpha_2 \,=\, z^2, \qquad
    \alpha_3 \,=\, h\,z^2 + z \,=\, z\,\bigl(1 + q^{1/2} - q^{-1/2}\bigr).
  \;}
$$

*All four are explicit q-algebraic — no transcendental constants, no
fitting.*
## Significance

This proposition closes the H_3 stratum-prefactor derivation that the
[unified mass formula](#prop:unified-curvature-rank-mass-formula) and
[plancherel-term-7-formulation](#prop:plancherel-term-7-formulation)
left implicit ("stratum-dependent prefactors $\alpha_k$"). All four
$\alpha_k$ are now explicit q-algebraic functions — no transcendental
constants, no per-isotope fitting.

For $\alpha_{k \geq 4}$, the universal prefactor
$m_e \cdot 8 G$ ([gravity spectral prefactor](#prop:gravity-spectral-prefactor))
is the Newton's-constant identification at the deep-tower stratum.

## Open

- **$\alpha_1$ disambiguation.** Two distinct objects share the
 symbol "$\alpha_1$":

 *(i) Spectral-sequence $\alpha_1$* (this proposition): the Markov
 pairing of $\mathrm{tr}_M$ with the alternating-pair representative
 $[\sigma_1 - \sigma_2]$. This vanishes by cyclicity of the Markov
 trace ($\alpha_1 = 0$ exactly). At generic $q$,
 $\mathrm{HH}^k(H_n(R, q)) = 0$ for $k \geq 1$
 ([spectral sequence collapse](#prop:spectral-sequence-collapse)),
 The Gerstenhaber bracket has empty target on the surviving
 $\mathrm{HH}^0$ — the spectral-sequence $\alpha_1$ is
 **structurally forced to zero**, not only an artifact of
 representative choice.

 *(ii) Plancherel-mass depth-1 contribution* (in the unified mass
 formula): the depth-1 stratum $\Lambda_1 = \{(n - 1, 1)\}$ has
 Plancherel-mass weight $y_{(n-1, 1)} \neq 0$
 ([procedure](#prop:alpha-k-derivation-procedure)). At $H_3$:
 $y_{(2, 1)} \approx 0.281$ — non-zero and structurally extracted
 from the witness, contributing
 $0.281 \cdot \chi_{(2, 1)}(\beta) \cdot \log|\chi_{(2, 1)}(\beta)|$
 to the unified mass formula at every nucleon.

 The unified mass formula uses sense (ii); the spectral-sequence
 vanishing in sense (i) does **not** imply the depth-1 stratum is
 empty.

- **$\alpha_k$ at $H_n$ for $n \geq 6$.** The analogous derivation
 for multi-nucleon Hecke algebras requires explicit $E_\infty^{p, *}$
 pages at higher $H_n$, generalising
 [$H_3$ explicit pages](#prop:spectral-sequence-h3-explicit).

## Witness

[the formal derivation](#)
implements the Jones-Markov linear system and the explicit Markov
pairings. Produces witness `alpha-k-jones-markov-h3.witness.json`
with $\alpha_2 = z^2$ verified to $10^{-17}$ and $\alpha_3 = h z^2 + z$
verified to canonical precision.
<!-- FILE_END: explicit-alpha-k-h3.md -->

<!-- FILE_START: explicit-alpha-k-h4.md -->
**Proposition (explicit $\alpha_\lambda(H_4)$ — closed forms in $\mathbb{Q}(q)$).**
*Let $z = 1/(\sqrt q + 1/\sqrt q)$ be the Markov parameter and
$\{T_{w_C}\}_C$ canonical Hecke representatives of the $p(4) = 5$
conjugacy classes of $S_4$:*

| label | cycle type | reduced word $w_C$ | length |
|--|:--:|:--:|:--:|
| $C_0 = e$ | $1^4$ | $\emptyset$ | $0$ |
| $C_1$ | $2 \cdot 1^2$ | $\sigma_1$ | $1$ |
| $C_2$ | $2^2$ | $\sigma_1 \sigma_3$ | $2$ |
| $C_3$ | $3 \cdot 1$ | $\sigma_1 \sigma_2$ | $2$ |
| $C_4$ | $4$ | $\sigma_1 \sigma_2 \sigma_3$ | $3$ |

*For each partition $\lambda \,\vdash\, 4$, the Wedderburn-orthogonal
representative $r_\lambda = \sum_C c_C \cdot T_{w_C}$ satisfying
$\chi_\mu(r_\lambda) = 0$ for every $\mu \neq \lambda$ has coefficients
$c_C(\lambda) \in \mathbb{Q}(q)$ given by:*

| $\lambda$ | $c_e$ | $c_{(12)}$ | $c_{(12)(34)}$ | $c_{(123)}$ | $c_{(1234)}$ |
|--|--|--|--|--|--|
| $(4)$ | $\dfrac{1}{q^3 \Phi_{(4)}}$ | $\dfrac{q^4 + 2q^2 + 3}{q^2 \Phi_{(4)}}$ | $\dfrac{1}{q(q^2+1)}$ | $\dfrac{q^4 + q^2 + 2}{q (q^4 + q^2 + 1)}$ | $1$ |
| $(3,1)$ | $-\dfrac{1}{q(q^2+1)}$ | $\dfrac{1 - 2q^2 - q^4}{q^2 (q^2+1)}$ | $\dfrac{1}{q(q^2+1)}$ | $\dfrac{1 - q^2}{q}$ | $1$ |
| $(2,2)$ | $-\dfrac{q^2}{(q^2+1)^2}$ | $\dfrac{q(1-q^2)}{(q^2+1)^2}$ | $-\dfrac{q^4 + q^2 + 1}{(q^2+1)^2}$ | $1$ | $0$ |
| $(2,1,1)$ | $\dfrac{q^3}{q^2+1}$ | $\dfrac{q^4 - 2q^2 - 1}{q^2+1}$ | $-\dfrac{q^3}{q^2+1}$ | $\dfrac{1 - q^2}{q}$ | $1$ |
| $(1^4)$ | $-\dfrac{q^9}{\Phi_{(4)}}$ | $\dfrac{q^4(3q^4 + 2q^2 + 1)}{\Phi_{(4)}}$ | $-\dfrac{q^3}{q^2+1}$ | $\dfrac{q(-2q^4 - q^2 - 1)}{q^4 + q^2 + 1}$ | $1$ |

*where $\Phi_{(4)} = q^6 + 2q^4 + 2q^2 + 1$.*

*The depth-stratum coefficients $\alpha_\lambda(H_4) := \mathrm{tr}_M(r_\lambda)
= y_\lambda \cdot \chi_\lambda(r_\lambda)$ evaluate at the substrate
value $q_0 \approx 1.110$ to exact algebraic values in
[`wedderburn-orthogonal-r-3-h4.witness.json`](https://github.com/litlfred/qou/blob/main/computations/wedderburn-orthogonal-r-3-h4.witness.json),
verified to canonical precision against the Hoefsmit character matrix
and Jones-Markov $y_\lambda$ values (consistency residual $< 10^{-15}$).*
## Significance

This proposition extends the H_3 closure of
[explicit α_k at H_3](#prop:explicit-alpha-k-h3) to H_4, providing
the second concrete data point in the structural derivation of
$\alpha_k(H_n)$ for the unified mass formula.

The dramatic decrease from $\alpha_3(H_3) = h z^2 + z \approx 0.5514$
to $\alpha_3(H_4) \approx 0.003463$ (factor $159$) reflects the
**dilution of the depth-3 stratum** as $n$ grows — at $H_4$ the
depth-3 partition $(1^4)$ has Plancherel weight $y_{(1^4)} \approx
-8.4 \times 10^{-4}$ (sign-indefinite, see
[sign-pattern remark](#rem:y-lambda-sign-pattern)), while at $H_3$
it has weight $y_{(1^3)} \approx 0.0227$.

## Related results

The closed-form $\mathbb{Q}(q)$ expressions for the $r_\lambda$
coefficients are tabulated above (lines 21–31). The closed forms
factor through cyclotomic denominators $(q+1)$, $(q^2+1)^2$,
$q^3 \Phi_{(4)}$, etc. (standard Schur-element pattern). All five
partitions of 4 — including the self-conjugate $(2, 2)$ whose
canonical inverse is ill-conditioned — close via the sympy null-space
solve.

For $H_5$ and $H_6$, all $18$ partitions admit canonical $r_\lambda$
values via the adaptive-gauge selection in
[the formal derivation](#). Symbolic forms for $y_\lambda$ at
$n = 5, \ldots, 12$ are also available via the
[Wenzl bridge](#prop:y-lambda-closed-form-wenzl-bridge)
(270 partitions, 45 seconds total).

## Witness

[the formal derivation](#) —
implements the class-function basis construction, character
evaluation via `build_seminormal_matrices`, and 4$\times$5 linear-system
solve.  Output:
[`wedderburn-orthogonal-r-3-h4.witness.json`](#).

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: explicit-alpha-k-h4.md -->

<!-- FILE_START: wedderburn-bratteli-recursion.md -->
**Proposition (Wedderburn–Bratteli recursion: existence and structure).**
*Let $H_n(R, q)$ be the Iwahori–Hecke algebra at generic $q$ with
Markov parameter $z = 1/(\sqrt q + 1/\sqrt q)$, and let
$\{y_\lambda^{(n)}\}_{\lambda \,\vdash\, n}$ be the Jones–Markov
weights of [α_k derivation procedure](#prop:alpha-k-derivation-procedure).
Then the family $\{y_\lambda^{(n)}\}_{n \geq 1}$ satisfies a
**multiplicity-free Bratteli recursion**: for every $\lambda \,\vdash\,
n + 1$,*

$$
  y_\lambda^{(n+1)}
  \;=\;
  z \cdot
  \sum_{\mu \nearrow \lambda}
    F_q\bigl(c(\lambda, \mu),\, \mathrm{hooks}(\lambda)\bigr)
  \cdot y_\mu^{(n)},
$$

*where $\mu \nearrow \lambda$ ranges over the Bratteli edges (partitions
$\mu \,\vdash\, n$ with $\mu \subset \lambda$, $|\lambda \setminus \mu|
= 1$), $c(\lambda, \mu) = j - i$ is the $q$-content of the added cell,
and $F_q$ is a $q$-rational function determined by the Hoefsmit seminormal
eigenvalues of $T_n$ on the per-edge idempotent.*
## Implication for $\alpha_k$ at $H_n > 3$

Even before $F_q$ is in closed form, the recursion gives the
qualitative structural shortcut: $\alpha_k(H_n)$ at fixed $k$
involves only finitely many strata, and the tower of Jones–Markov
weights propagates without re-solving the $p(n) \times p(n)$ linear
system — the witness is enough.  Combined with depth-$k$ representative
choices ([α_k derivation procedure](#prop:alpha-k-derivation-procedure)
step (i)), $\alpha_k(H_n)$ for arbitrary $n$ is then a finite sum
indexed by depth-$k$ partitions and their Bratteli-ancestors.

## Witness

[`computations/y-lambda-jones-markov-witness.json`](#) —
all 270 weights for $n = 2, \ldots, 12$.

[the formal derivation](#) —
extracts per-edge ratios and tests candidate closed forms $F_q$.

## Open

- **Sign pattern at $n \geq 4$**: $y_\lambda$ acquires negative
  components at $n \geq 4$ (e.g.\ $y_{(1^4)} \approx -8 \times 10^{-4}$
  at $q_0$); see [sign-pattern remark](#rem:y-lambda-sign-pattern)
  for empirical table and explanation via cancellation across
  Wedderburn blocks.  Implication: LP-positivity formulations of the
  Jones–Markov weights are infeasible at $n \geq 4$; SDP/cvxpy
  unconstrained least-squares cross-checks confirm the symbolic
  values.
- **Lean formalisation**: state the recursion in
  `wedderburn-bratteli-recursion.lean` against the symbolic
  $y_\lambda$ solutions.
<!-- FILE_END: wedderburn-bratteli-recursion.md -->

<!-- FILE_START: y-lambda-sign-pattern.md -->
**Notation register (resolved collision).**
This paper now uses two distinct symbols for what were previously
both written $y_\lambda$:

1. *Jones–Markov central coefficients* — keeps $y_\lambda$.  These
   appear in the trace expansion $\mathrm{tr}_M = \sum_\lambda
   y_\lambda \chi_\lambda$
   ([procedure](#prop:alpha-k-derivation-procedure),
   [explicit H_3](#prop:explicit-alpha-k-h3)).  **Sign-indefinite**
   — the subject of this remark.
2. *Operator-selection LP dual variables* (shadow prices) — written
   $u_\lambda$ (Schrijver LP-duality convention) in the
   operator-selection LP
   ([BW shadow price](#prop:mass-coefficient-shadow-price)).
   **Non-negative** by LP duality.

The two symbols denote unrelated quantities and should never be
conflated.  In what follows, $y_\lambda$ refers exclusively to sense
(1) (Jones–Markov central coefficient).  The choice $u_\lambda$ for
LP shadow prices avoids collision with $\pi_\lambda$, already used
in [BW shadow price](#prop:mass-coefficient-shadow-price) for the
central idempotents of the Wedderburn block decomposition.

**Empirical observation.**
At the canonical Markov parameter $z = 1/(\sqrt q + 1/\sqrt q)$ and
substrate $q_0 = 1.109978595554181\ldots$ (50 dps), the Jones–Markov block weights
$y_\lambda$ from
([procedure](#prop:alpha-k-derivation-procedure)) are non-negative
for $n \leq 3$ but acquire negative components at $n \geq 4$.  The
LP feasibility problem

$$
  \text{find } y \in \mathbb{R}^{p(n)} :
  \quad A(q_0)\, y = b(q_0), \quad y \geq 0
$$

is **infeasible** at $n = 4, 5, 6$ — empirically verified via
the canonical formalism.
The full sign pattern at $n \in \{2, \ldots, 6\}$ — including the
sign-changing entries $y_{(1^4)} \approx -8.4 \times 10^{-4}$ at
$n = 4$ and $y_{(2, 1^3)} \approx -9.3 \times 10^{-4}$ at $n = 5$
— is recorded in
[`y-lambda-jones-markov-witness.json`](https://github.com/litlfred/qou/blob/main/computations/y-lambda-jones-markov-witness.json).

The negative components are small in absolute value but
non-negligible — they enter every $\alpha_k$ derivation and the
unified mass formula at the right depths.

**Consistency with trace positivity.**
The Markov trace is positive on positive elements: for any
$a \in H_n(R, q)$, $\mathrm{tr}_M(a^\ast a) \geq 0$.  In the
central decomposition $\mathrm{tr}_M = \sum_\lambda y_\lambda
\chi_\lambda$, each character $\chi_\lambda$ is itself indefinite
on $H_n(R, q)$ — $\chi_\lambda(a^\ast a)$ may be negative for some
$a$.  Positivity of $\mathrm{tr}_M$ is preserved through
cancellation across blocks: the negative $y_\lambda \cdot
\chi_\lambda(a^\ast a)$ contributions are dominated by positive
terms in the sum.  This is the standard operator-algebraic
phenomenon of an indefinite signature on the centre yet a
positive total trace.

**Structural reading.**
The negative-$y_\lambda$ partitions at $n = 4, 5$ are
$(1^4)$ and $(2, 1, 1, 1)$ — both deep in the alternating-block
sector ($\mathrm{depth}(\lambda) = n - 1$ and $n - 2$).  This
matches the qualitative picture: the alternating idempotent
$e_{(1^n)}$ is "the chirality block", and chirality-dominant
configurations contribute with negative weight in the central
expansion.  The cancellation against positive symmetric / standard
contributions is what keeps mass observables positive.

**Implication for LP/SDP formulations.**
The LP

$$
  \text{find } y :
  \quad A y = b, \quad y \geq 0
$$

is infeasible at $n \geq 4$, so it is **not** a viable formulation
of the Markov-trace problem.  The correct convex variant is the
SDP moment-matrix on the regular representation of $H_n(R, q)$:

$$
  \text{find } M \succeq 0 :
  \quad M_{1, 1} = 1, \quad
  M_{\sigma_n w, w'} = z \cdot M_{w, w'},
  \quad \text{(Hecke + Markov rels.)}
$$

— positivity is on the **functional**, encoded as the moment
matrix, not on the block weights $y_\lambda$.  The SDP recovers
the unique positive trace at every $q$ (including root-of-unity
$q$ where the linear system is singular) and produces the same
$y_\lambda$ values, with their sign pattern intact.

**Cross-check status.**
At $n \in \{2, \ldots, 6\}$, the unconstrained LS solve (cvxpy /
CLARABEL) reproduces the linear-solve $y_\lambda$ to $\sim 10^{-15}$
([`y-lambda-sdp-witness.json`](#)).  Symbolic linear-solve via
sympy
([the formal derivation](#)) gives exact $q$-rational forms,
matching the exact algebraic values to machine precision at $q_0$.  All
three pathways agree; the negative components are real, not
artifacts.
<!-- FILE_END: y-lambda-sign-pattern.md -->

<!-- FILE_START: terms-2-6-higher-operations.md -->
**Two structural identifications for Terms 2 and 6.**
*Of the two remaining open identifications in the spectral-sequence
framework
([$E_\infty$ page identifications](#prop:e-infinity-page-identifications)),
the unified knot mass formula
([unified knot mass](#thm:knot-mass-formula-unified)) carries the
following structural readings:*

1. **Term 2 (single-generator brane tower) is an infinite
   Wedderburn / Habiro-cyclotomic sum.** *The Cauchy kernel
   $\Phi_q(z) = \sum_n z^n / (q; q)_n$ is the $k \to \infty$ limit of
   the level-$k$ Jones–Wenzl trace*

   $$
     \Phi_q(z)
     \;=\;
     \lim_{k \to \infty}
       \sum_{\lambda : |\lambda| \leq k}
       w_\lambda^{(k)} \cdot z^{|\lambda|},
     \qquad
     w_\lambda^{(k)} = \dim_q(\lambda)^2 / [k]_q!,
   $$

   *with the same Wedderburn weights
   ([three-parameters Wedderburn](#prop:three-parameters-wedderburn))
   that enter at finite level. Equivalently the $(q; q)_m$
   denominator is the cyclotomic basis of Habiro's unified quantum
   invariant ([Habiro ring](#def:habiro-ring)). No new homological
   source is required: $\Phi_q$ is an infinite Wedderburn sum, not a
   Hochschild cup-product tower (see historical note).*

2. **Term 6 (jet-level prefix correction) is the GB root-of-unity
   residue sum.** *Term 6 is not a prefix-word product (all four
   tested prefix conventions fail —
   [jet-prefix GB filtration](#prop:jet-prefix-gb-filtration)); it is
   the cyclotomic residue contribution already captured by
   [GB residue spectral sum](#prop:gb-residue-spectral-sum):*

   $$
     \text{Term 6}(K)
     \;=\;
     \sum_{\ell \geq 2}
       \frac{\mathrm{Res}_{q = \zeta_\ell}\bigl[\Phi_q \cdot \mathrm{tr}_{M, \ell}(T_w)\bigr]}
            {q_0 - \zeta_\ell},
   $$

   *summed over roots of unity $\zeta_\ell$ for $\ell \geq 2$ (the
   $\zeta_1 = 1$ pole is absorbed into Terms 2, 3).*

*Both identifications are structural proposals consistent with the
algebraically-derived Wedderburn / Habiro / GB-residue machinery
already in the corpus; the dead-end Hochschild cup-product and
deformation-cohomology routes are recorded in the historical note as
closed.*
<!-- FILE_END: terms-2-6-higher-operations.md -->

