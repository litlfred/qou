*Lean sibling: archimedean specialisation over $\mathbb{R}$ (CLAUDE.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

> **Status — $\lambda_{\mathrm{scale}}$ ABSORBED INTO `Geom_full`.**
>
> Per [`docs/lambda-scale-absorbed-into-geom-full.md`](../../../docs/lambda-scale-absorbed-into-geom-full.md)
> (canonical framing, settled 2026-05-23 in PR #1080),
> **`λ_scale` is no longer a separate object** in the framework.
> The canonical mass formula is
>
> $$m(K) = m_e \cdot \mathrm{Geom_{full}}(K, q_0)$$
>
> — a single Geom-functor evaluation per knot. What older docs
> called `λ_scale(K, q)` is the **ratio**
> $\mathrm{Geom_{full}}(K, q) / \mathrm{Geom_{leading}}(K, q)$,
> i.e., what Geom assigns to multi-component links above their
> bare hyperbolic volume. There is nothing to "derive from
> substrate" — the value is *output* of Geom, not input.
>
> **What remains canonical in this block:**
> - The Family A theorem
>   $\lambda_A(q) = (1/4) \sum_{\lambda \vdash 4} \dim_q V_\lambda
>     = 5/2 + (3/4) h^2$
>   IS the current production value of `linking_weight(𝓑_3, q)`
>   inside `Geom_full(𝓑_3, q)`. It is PROVED (Wenzl bridge,
>   PR #895/#942).
>
> **What is OBSOLETE in this block:**
> - The original substrate-form claim
>   $\lambda_{\mathrm{scale}}^{(u, d)} = 5/2 - h^2 \cdot G + O(h^4)$
>   was **structurally falsified** 2026-05-18 (PSLQ coincidence;
>   no Wedderburn derivation gives $-G \cdot h^2$). See
>   [`docs/audits/2026-05-18-conjecture-falsification.md`](https://github.com/litlfred/qou/blob/main/docs/audits/2026-05-18-conjecture-falsification.md).
> - The CAL-4 framing ($\lambda_{\mathrm{scale}}$ as a "4th
>   calibration anchor") is **purged 2026-05-24** (commit
>   `71d674da1`). The production literal
>   `LAMBDA_PROTON_FITTED_FROM_CODATA` was removed from
>   `m_p_borromean_verification_50dps.py`; production now uses
>   Family A directly.
> - The "Bring-Bloch identity" research direction was closed at
>   PSLQ tier 5 (see
>   [`bring_bloch_tier5_search_m_p.py`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/bring_bloch_tier5_search_m_p.py)).
> - The Yekutieli per-cell ADD form
>   $5/2 + (3/4 - G) h^2$ was also purged 2026-05-24 as
>   non-canonical (PR #985 bijection NEGATIVE).
>
> **Current research direction**: refine `Geom_full(𝓑_3)`'s
> categorical exactness at higher $h^2$ orders, NOT derive
> $\lambda_{\mathrm{scale}}$ from substrate. The +2.89 % gap is
> a `Geom_full` refinement question; the structural Markov-trace
> finding (`tr_M(\beta_{\mathrm{Bor}}) = 1 + 0 \cdot h^2 - (3/4)h^4 + \cdots`)
> brings it to +1.948 % with zero free parameters
> (see [`folio-assistant/computations/geom_full_borromean_h4_probe.py`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/geom_full_borromean_h4_probe.py)).
>
> **Block-conservation rationale**: the label
> `conj:lambda-scale-substrate-form` is retained for graph-stability
> across already-cited references; the §Family A theorem section
> below is canonical-preserving content. Sections covering the
> falsified / purged forms are kept as **historical record** so
> future agents see what was tried, why it was rejected, and where
> to find the post-purge canonical framing. Do not propose
> reviving the falsified $5/2 - h^2 \cdot G$ form, the Yekutieli
> ADD form, or the Bring-Bloch identity as production candidates.

What IS proved (Family A theorem):*

$$
  \lambda_A(q) \;:=\; \frac{1}{4} \sum_{\lambda \vdash 4} \dim_q V_\lambda
                \;=\; \frac{3q^2 + 4 + 3q^{-2}}{4}
                \;=\; \frac{5}{2} \;+\; \frac{3}{4} \cdot h^2
$$

*The series TERMINATES exactly at $h^2$; all higher $h^{2k}$ vanish.
The $h^2$ coefficient is $+3/4$, NOT $-G$ --- different sign and value
than the original conjecture. Proved in*
[`lambda_scale_all_c_i_family_a.py`](../../folio-assistant/computations/lambda_scale_all_c_i_family_a.py)
*and formalised in Lean*
[`lambda-scale-substrate-form.lean`](./lambda-scale-substrate-form.lean).

**Original conjecture (now classified as empirical only):**
*The Borromean baryon $\lambda_{\mathrm{scale}}$ in*
([conj:borromean-baryon-mass-formula](#conj:borromean-baryon-mass-formula))
*was hypothesised to equal $5/2 - h^2 \cdot G + O(h^4)$ where
$G = \mathrm{Vol}(\mathcal{B}_3)/8$ is Catalan's constant. This
empirical match is recorded for historical reference:*

$$
  \lambda_{\mathrm{scale}}^{(u, d)} \stackrel{?}{=} \frac{5}{2} - h^2 \cdot G + O(h^4)
  \qquad (\text{5.6 ppm match to CODATA $m_p$, NO categorical derivation})
$$

**Why the original form is NOT derived (cumulative falsification):**

1. **Family A (natural Wedderburn sum):** gives $+3 h^2/4$, opposite
   sign and different magnitude than $-G$.
2. **Sign-flipped Wedderburn sums (32 variants at $H_4$):** only the
   all-positive combination preserves the leading 5/2, forcing
   $+3 h^2/4$. No sign flip can produce a negative $h^2$.
3. **Other Hecke levels ($H_2$ through $H_7$):** all natural
   $(1/X) \sum_\lambda \dim_q V_\lambda$ normalisations give
   POSITIVE $h^2$ coefficients.
4. **Transcendental ansätze (Bloch-Wigner, Clausen, $\zeta(3)$,
   $\mathrm{Cl}_2$):** no candidate matches the empirical
   $\Sigma_{\mathrm{geom}}$ value within $10^{-3}$.
5. **Single-knot ansatz $\mathrm{Vol}(K_p)/\hbar_q^2$:** no standard
   hyperbolic 3-manifold has $\mathrm{Vol} = 18.03$ within 0.28%
   (closest: $9 \cdot \mathrm{Vol}(4_1)$ at $+1.35\%$).

6. **Q-locality (PR #951, 2026-05-23):** at the substrate window
   $q \in [q_0 - 0.05, q_0 + 0.05]$, the residual
   $(\frac{5}{2} - h^2 \cdot G) - \lambda_p(q)$ has slope
   $\sim -1.7 \times 10^7$ ppm/q and curvature $\sim 4.4 \times 10^4$
   ppm. Per the standing discipline that $q_0$ is "not special,
   just where we happen to be," the form is **non-smooth in $q$** —
   the 5.6 ppm match at $q_0$ is a residual zero-crossing, not a
   structural identity. The same diagnostic refutes all four
   known $h_q$-axis near-matches ($\frac{5}{2}-h^2 G$,
   $1/(1 - h_q \cdot q_0^{10})$, V$_7$, Strategy G).

7. **Reframing (PR #957, 2026-05-23):** $\lambda_p(q) = (m_p/m_e)
   \cdot \hbar_q^2 / (8 G) = C \cdot \hbar_q^2$ exactly, with
   $\hbar_q := (q - 1) / q$ and $C = (m_p/m_e) / (8 G) \approx
   250.576$. This is a degree-0 polynomial in $q$ over
   $\mathbb{R}[\hbar_q]$ — a constant times $\hbar_q^2$, with no
   leading $h^2$ coefficient when expressed in $\hbar_q$. All
   prior $h_q$-axis candidates (including the present $5/2 - h^2 G$
   form) use $h_q = q - 1/q = (q+1) \cdot \hbar_q$, which has
   varying coefficients when viewed as a function of $q$ — the
   **wrong q-parametrization** for $\lambda_p$. The structural
   question becomes "derive the *constant* $C \approx 250.576$
   from substrate," not "find $F(q) \approx \lambda_p(q)$." Tier 5's
   search for $T = \lambda_p \cdot 8G \approx 18.03$ as a
   $\mathbb{Z}$-combination of knot volumes was equivalent to
   searching for $C$ (the two targets are related by a single
   multiplicative substrate factor: $T = C \cdot \hbar_q^2 \cdot 8G$,
   so a $\mathbb{Z}$-relation expressing one as a knot-volume sum
   immediately gives the other), and was negative.

8. **Strategy J (PR #969, 2026-05-23):** no natural ratio of
   $\{\operatorname{tr}_M(\beta_p), \operatorname{tr}_M(\beta_n), \hbar_q, h_q, q_0, G\}$
   structurally predicts $m_n / m_p$ either. Best pure-substrate
   match at 0.45% --- 4,500 times worse than 1 ppb.

**Therefore (post-2026-05-23 acknowledged-CAL-4 status):** after
**eight independent structural searches** across every tested axis
(Tier 5 PSLQ; q-dilog substrate-natural; V̂$_S$ + $\mathbb{Q}(\zeta_{60})$;
commutative + operator-theoretic Φ$_q$; q-locality; reframing;
Strategy J), the original conjecture's specific form is recorded
as **PSLQ-style empirical fit (no categorical derivation)**, the conjecture
$\lambda_{\mathrm{scale}}$ is recorded as an
**acknowledged-CAL-4** empirically falsifiable prediction (see
[`conj:lambda-scale-bring-bloch-identity`](#conj:lambda-scale-bring-bloch-identity)
for the formal statement), and the proton's mass-formula
derivation continues to be sourced through the 3-calibration
chain at the precision-dashboard level rather than from a closed
form for $\lambda_{\mathrm{scale}}$.

## Family A theorem (what IS proved)

*Let $q_0 \in \mathbb{R}$ be the substrate parameter
([def:substrate-parameter](#def:substrate-parameter)), $h = q_0 - q_0^{-1}$
the Hecke deformation, and $\dim_q V_\lambda$ the q-deformed dimension
of the irreducible $H_4(q)$-module indexed by partition $\lambda \vdash 4$
(Frame-Robinson-Thrall hook-content formula).*

**Theorem (Family A closed form).** *The half-symmetric Wedderburn-sum
projection at $H_4$ has the closed form*

$$
  \lambda_A(q) = \frac{1}{4} \sum_{\lambda \vdash 4} \dim_q V_\lambda
             = \frac{3 q^2 + 4 + 3 q^{-2}}{4}
             = \frac{5}{2} + \frac{3}{4} \cdot h^2
$$

*with no $h^4, h^6, \ldots$ corrections. All odd $h$ coefficients
vanish by $q \leftrightarrow q^{-1}$ symmetry.*

**Proof.** *Direct computation in sympy and Lean. The quantum
dimensions at $H_4$ are $\dim_q V_{(4)} = 1$, $\dim_q V_{(3,1)} = [3]_q$,
$\dim_q V_{(2,2)} = [4]_q/[2]_q$, $\dim_q V_{(2,1,1)} = [3]_q$,
$\dim_q V_{(1,1,1,1)} = 1$. Their sum is $3q^2 + 4 + 3q^{-2}$
(verified symbolically). Division by 4 and substitution $h = q - q^{-1}$
yields the claimed form via `field_simp; ring`.* $\square$

## Structural interpretation

### The "$5/2$" leading term

At Hecke level $H_4(q)$ the partition spectrum is $p(4) = 5$:

| Partition | Conjugate | Type | Half-weight |
|-----------|-----------|------|-------------|
| $(4)$ | $(1, 1, 1, 1)$ | conjugate pair | $1$ |
| $(3, 1)$ | $(2, 1, 1)$ | conjugate pair | $1$ |
| $(2, 2)$ | $(2, 2)$ | **self-conjugate** | $\tfrac{1}{2}$ |

The half-symmetric count (1 + 1 + 1/2) = **5/2**.

### The $h^2 \cdot G$ correction

The leading quantum correction from the q-deformation of the Markov trace
on $H_4(q)$ at the canonical Borromean braid scales as

$$
  \Delta(\tau_q) \;\sim\; h^2 \cdot \underbrace{\frac{\mathrm{Vol}(\mathcal{B}_3)}{8}}_{= G}
                  \;+\; O(h^4),
$$

where $\mathrm{Vol}(\mathcal{B}_3)/8 = G$ is the per-cell hyperbolic volume
(the complement of the Borromean rings decomposes into 8 ideal regular
octahedra; each octahedron contributes $G$ via the Lobachevsky function:
$\Lambda(\pi/4) = G/2$, $V_{\mathrm{oct}} = 8\Lambda(\pi/4) = 4G$, and
$\mathrm{Vol}(\mathcal{B}_3) = 2 V_{\mathrm{oct}} = 8G$ exactly, per Adams 1985).

The structural identity $\mathrm{Vol}(\mathcal{B}_3) = 8G$ is **derived**;
the appearance of $h^2 \cdot G$ as the leading correction to $5/2$ is
the open conjectural content.

## Numerical evidence (q_0 at MPFR 80 dps)

| Quantity | Value |
|----------|-------|
| $\lambda_p$ from CODATA $m_p/m_e$, $S(p) = 0$ | $2.4599534044$ |
| $5/2 - h^2 \cdot G$ predicted | $2.4599666078$ |
| Relative residual | $+5.6$ ppm |

The neutron is **structurally consistent** under the same
common-substrate hypothesis: $\lambda_n = \lambda_p$ shared, with
$\Delta m_{pn} = 1.293\;\mathrm{MeV}$ arising entirely from the
Skein contribution $S(n) - S(p)$
([conj:borromean-baryon-mass-formula](#conj:borromean-baryon-mass-formula)
common-scale hypothesis).

## Comparison with the FSC derivation pattern

The fine-structure-constant identification
([rem:alpha-em-categorical-trace](#rem:alpha-em-categorical-trace))
follows a similar pattern: substrate q-integer products times a
topological-invariant prefactor. There:

$$
  \frac{1}{\alpha_{EM}}
  \;=\; q \cdot [9]_q \cdot [10]_q
$$

matches CODATA to $6.7 \times 10^{-9}$ via the force-carrier sector
$\{T_{2,9}, T_{3,5}\}$. The present conjecture is the analogous
**substrate q-integer + topological invariant** ansatz for the
baryon-mass Borromean scale:

$$
  \lambda_{\mathrm{scale}}^{(u, d)}
  \;=\; \underbrace{\frac{p(4)/2}{1}}_{\text{partition count}}
  \;-\; \underbrace{h^2 \cdot \frac{\mathrm{Vol}(\mathcal{B}_3)}{8}}_{\text{topological invariant}}
  \;+\; O(h^4).
$$

## Status: justification, not derivation

Per the audit
([2026-05-18 λ-scale derivation search §13](https://github.com/litlfred/qou/blob/main/docs/audits/2026-05-18-lambda-scale-derivation-search.md)):

- $\mathrm{Vol}(\mathcal{B}_3) = 8G$ is **derived** (standard topology).
- The numerical match $\lambda_p = 5/2 - h^2 G$ at 5.6 ppm is **justified**
  (PSLQ-style ansatz with plausible categorical interpretation).
- The structural link between $\lambda_{\mathrm{scale}}$ and the
  H_4 partition count is **conjectural**.

This block records the conjecture for systematic proof investigation.

## Proof strategy (outline)

To upgrade from justification to derivation, the proof must establish:

1. **Markov-stabilised Hecke level.** The proton's canonical 3-strand
   braid $\mathcal{N}_p \in B_3$, viewed at the next Markov-stabilisation
   level $H_4(q)$, has its Wedderburn-trace expansion controlled by
   the partition spectrum of $4$.

2. **Conjugate-pair half-symmetric count.** The proton's amphichiral
   internal symmetry (3 quarks distinguishable only by color) projects
   the H_4 Wedderburn decomposition onto a *half-symmetric* combination
   of conjugate partition pairs, with each pair contributing weight $1$
   and the self-conjugate $(2,2)$ partition contributing weight $\tfrac{1}{2}$.
   Total: $5/2$.

3. **q-expansion of the Markov trace.** Expanding $\tau_q$ around
   $q = 1$ as $\tau_q = \tau_1 + h^2 \cdot \tau^{(2)} + O(h^4)$ on
   the H_4 Markov basis, the second-order coefficient $\tau^{(2)}$
   evaluates to $-G$ on the canonical Borromean braid — via the
   Yekutieli categorical nonabelian Stokes theorem
   ([rem:yekutieli-stokes](#rem:yekutieli-stokes)) applied to the
   Borromean ribbon surface, whose hyperbolic 3-volume normalisation
   is exactly $\mathrm{Vol}(\mathcal{B}_3)/8 = G$.

4. **$O(h^4)$ remainder.** The next-order correction $\tau^{(4)}$
   is bounded by a finite Wedderburn-block computation; numerical
   probe gives $\tau^{(4)} \approx +0.0069$, but the structural form
   (e.g. $\tau^{(4)} = c \cdot G^2$ for some rational $c$) is open.

5. **Skein contribution.** $S(p) = 0$ for the canonical Borromean
   orientation (closed under symmetric $(u, u, d)$ permutation);
   $S(n) = \Delta S = 2.531$ in categorical units (giving the
   $1.293\;\mathrm{MeV}$ proton-neutron mass split exactly). The
   derivation of $S(n)$ from the asymmetric $(u, d, d)$ orientation
   is a separate subgoal.

## Verifiable predictions if proved

1. The neutron $\lambda_n$ equals the same $5/2 - h^2 G + O(h^4)$
   (already empirically consistent at 5.6 ppm given the Skein split).
2. The h^4 coefficient $c$ in the next-order expansion is a rational
   function of $q_0$ derivable from $H_4$ block characters.
3. Higher-A nuclei have their own $\lambda$ values determined by
   higher-Hecke-level partition counts, but **NOT** by the simple
   $p(n)/2$ generation pattern (see audit §11 probe results: Σ/Λ
   baryons follow a different SU(3) structure).

## Witness

- [`folio-assistant/computations/lambda_scale_substrate_probe.py`](../../folio-assistant/computations/lambda_scale_substrate_probe.py)
- [`folio-assistant/computations/lambda_scale_derivation_probes_123.py`](../../folio-assistant/computations/lambda_scale_derivation_probes_123.py)
- [`folio-assistant/computations/m_p_borromean_verification_50dps.py`](../../folio-assistant/computations/m_p_borromean_verification_50dps.py)
- [`docs/audits/2026-05-18-lambda-scale-derivation-search.md`](../../../docs/audits/2026-05-18-lambda-scale-derivation-search.md)
