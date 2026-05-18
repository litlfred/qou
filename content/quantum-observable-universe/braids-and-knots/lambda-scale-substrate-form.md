**Conjecture (Borromean baryon $\lambda_{\mathrm{scale}}$ substrate form).**
*Let $q_0 \in \mathbb{R}$ be the substrate parameter
([def:substrate-parameter](#def:substrate-parameter)), $h = q_0 - q_0^{-1}$
the Hecke deformation, and $G = \mathrm{Vol}(\mathcal{B}_3)/8$ Catalan's
constant (equivalently, the per-cell hyperbolic volume of the Borromean
rings complement; see Adams 1985). The Borromean baryon $\lambda_{\mathrm{scale}}$
factor in the mass formula
([conj:borromean-baryon-mass-formula](#conj:borromean-baryon-mass-formula))
admits the substrate form*

$$
  \boxed{\;
    \lambda_{\mathrm{scale}}^{(u, d)}
    \;=\; \frac{5}{2} \;-\; h^2 \cdot G \;+\; O(h^4)
  \;}
$$

*for the canonical $(u, d)$-Borromean baryon family (proton and neutron),
where the leading "$5/2$" arises from the conjugate-pair half-symmetric
partition count at the proton's Markov-stabilised Hecke level $H_4(q)$.*

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
