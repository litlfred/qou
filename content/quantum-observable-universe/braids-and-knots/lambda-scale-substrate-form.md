**Status (revised 2026-05-18 after exhaustive R&D — Class-A canonical-discipline note):**
*The original substrate-form claim*
$\lambda_{\mathrm{scale}}^{(u, d)} = 5/2 - h^2 \cdot G + O(h^4)$
*matches CODATA $m_p$ to 5.4 ppm but is* **NOT structurally derived**
*— it is a PSLQ-style numerical near-coincidence ([2026-05-18 falsification audit](https://github.com/litlfred/qou/blob/main/docs/audits/2026-05-18-conjecture-falsification.md)).
What IS proved (Family A theorem):*

$$
  \lambda_A(q) \;:=\; \frac{1}{4} \sum_{\lambda \vdash 4} \dim_q V_\lambda
                \;=\; \frac{3q^2 + 4 + 3q^{-2}}{4}
                \;=\; \frac{5}{2} \;+\; \frac{3}{4} \cdot h^2
$$

*The series TERMINATES exactly at $h^2$; all higher $h^{2k}$ vanish.
The h² coefficient is $+3/4$, NOT $-G$ — different sign and value
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
  \qquad (\text{5.4 ppm match to CODATA $m_p$, NO categorical derivation})
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
   (closest: 9·Vol(4_1) at +1.35%).

**Therefore:** the original conjecture's specific form is a
**PSLQ-style numerical coincidence**, not a categorical identity.
The proton's mass-formula derivation requires either (a) a
fundamentally different categorical construction, or (b) revision
of the Borromean baryon mass formula itself.

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
| Relative residual | $+5.4$ ppm |

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
- The numerical match $\lambda_p = 5/2 - h^2 G$ at 5.4 ppm is **justified**
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
   (already empirically consistent at 5.4 ppm given the Skein split).
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
