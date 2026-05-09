The crystal-limit shell-correction sum
$S_{\mathrm{crystal}}(A)$ defined in
[shell-correction Term 7](#conj:shell-correction-term-seven)
is invariant under generator inversion in the atomic braid word.

**Proposition (crystal isospin degeneracy).**
*Let $A \geq 1$ and let $\beta_A \in B_{3A}$ be an atomic braid
written as a finite word
$\beta_A = \sigma_{i_1}^{\epsilon_1} \cdots \sigma_{i_\ell}^{\epsilon_\ell}$
with $\epsilon_k \in \{+1, -1\}$.  Define a partner word $\beta_A'$
by replacing any subset $S \subseteq \{1, \ldots, \ell\}$ of the
exponents $\epsilon_k$ by their negatives.  Then*

$$
  S_{\mathrm{crystal}}(\beta_A) \;=\; S_{\mathrm{crystal}}(\beta_A')
$$

*where $S_{\mathrm{crystal}}$ is the crystal-limit ($q \to 0$)
shadow-price sum*

$$
  S_{\mathrm{crystal}}(\beta) \;:=\;
    \sum_{\substack{\lambda \,\vdash\, 3A \\ \mathrm{height}(\lambda) \,\leq\, 6}}
      w_\lambda(q = 1) \cdot \chi^\lambda_{\mathrm{crystal}}(\beta).
$$

**Proof.**
The crystal-limit character $\chi^\lambda_{\mathrm{crystal}}(\sigma)$
on a single Hecke generator $\sigma$ is, by
[crystal-graph realisation](#conj:crystal-graph-realization),
the trace of the signed-permutation action

$$
  \sigma_i : T \;\longmapsto\; \mathrm{sign}(\rho_T(i)) \cdot T,
  \qquad \rho_T(i) := c(T(i+1)) - c(T(i))
$$

on the standard-Young-tableaux basis $\mathrm{SYT}(\lambda)$, where
$c(\cdot)$ is the cell content
([content scaling](#prop:content-scaling-correspondence)).
The Hecke involutivity at $q = 0$ — equivalently, reading off the
relation $\sigma_i^{-1} = \sigma_i$ on the crystal sub-quotient from
the Hecke skein convention $(\sigma_i - q)(\sigma_i + q^{-1}) = 0$
specialised at $q = 0$ — gives

$$
  \sigma_i^{-1} : T \;\longmapsto\; \mathrm{sign}(\rho_T(i)) \cdot T
  \;=\; \sigma_i \cdot T
$$

acting on the same SYT eigenline.  Therefore
$\chi^\lambda_{\mathrm{crystal}}(\sigma_i) =
\chi^\lambda_{\mathrm{crystal}}(\sigma_i^{-1})$ for every $\lambda$
and every $i$.  Multiplicativity along a braid word gives

$$
  \chi^\lambda_{\mathrm{crystal}}(\beta_A)
    \;=\; \chi^\lambda_{\mathrm{crystal}}(\beta_A')
$$

per partition.  Summing against the (sign-independent) Plancherel
weight $w_\lambda(q = 1) = (f^\lambda)^2 / (3A)!$ yields the claim.  $\square$

**Corollary (T--$^3$He crystal degeneracy).**
*The atomic braid words of tritium and helium-3 used by
[`term7_alpha5_crystal_derivation.py`](../../../folio-assistant/computations/term7_alpha5_crystal_derivation.py)
are*

$$
  \beta_T = \sigma_1\sigma_2\sigma_1^{-1}\sigma_4\sigma_5^{-1}\sigma_4
              \sigma_7\sigma_8^{-1}\sigma_7,
  \qquad
  \beta_{{}^3\mathrm{He}} = \sigma_1\sigma_2\sigma_1^{-1}\sigma_4\sigma_5\sigma_4^{-1}
              \sigma_7\sigma_8^{-1}\sigma_7,
$$

*differing only at positions $5$ and $6$ by paired inversion of
$\sigma_5 \leftrightarrow \sigma_5^{-1}$ and
$\sigma_4 \leftrightarrow \sigma_4^{-1}$.  Therefore*

$$
  S_{\mathrm{crystal}}(T) \;=\; S_{\mathrm{crystal}}({}^3\mathrm{He}).
$$

*The empirical witness
[`term7-alpha5-crystal-derivation.witness.json`](../../../folio-assistant/computations/term7-alpha5-crystal-derivation.witness.json)
records both values to fifty decimal digits as
$0.0020612874779541296$ — exact agreement.*

## Consequences

**Term 7 is isospin-blind at the crystal limit.**
The shell-correction prediction $\mathrm{Term~7}(A) = \alpha_5 \cdot
S_{\mathrm{crystal}}(A)$ assigns *the same* shell residual to T and
to $^3\mathrm{He}$.  Yet experimentally
$\mathfrak{m}({}^3\mathrm{H}) - \mathfrak{m}({}^3\mathrm{He})
\approx 0.529\;\mathrm{MeV}$ and the
2-row Wedderburn dominance pattern
fractions differ ($84.04\%$ vs.\ $89.34\%$ at $q_0 \approx 1.110$;
witness
[`delta-lambda-2row-stratum.witness.json`](../../../folio-assistant/computations/delta-lambda-2row-stratum.witness.json)).
Both observables therefore live entirely in the **finite-$q$
correction** along the transport $q \to 0 \rightsquigarrow q_0$ —
they cannot be derived from the crystal functional alone.

**Corollary (q-curvature of isospin-mirror pairs).**
*For any pair of isospin-mirror atoms $K, K'$ whose canonical braid
words differ only by signed-generator inversions, the difference*

$$
  \Delta S(K, K')(q)
    \;:=\; S(\beta_K)(q) - S(\beta_{K'})(q)
$$

*satisfies $\Delta S(K, K')(0) = 0$ and (empirically, for $K = T$,
$K' = {}^3\mathrm{He}$, $q_0 \approx 1.110$) $\Delta S(K, K')(q_0)
\neq 0$.  The function $q \mapsto \Delta S(K, K')(q)$ is therefore
a direct probe of the **curvature** of the flat-transport map
underlying $\alpha_5$ at the height-$6$ stratum (cf.\ the
ontological-agnosticism remark in this chapter).*

## Connection to the 2-row decay observation

The empirical 2-row Wedderburn dominance fractions tabulated in
[`delta-lambda-2row-stratum.witness.json`](../../../folio-assistant/computations/delta-lambda-2row-stratum.witness.json)
decay non-monotonically with mass number $A$:

| atom | $A$ | 2-row mass fraction |
|:---:|:---:|:---:|
| $\mathfrak{p}$ | $1$ | $98.47\%$ |
| $\mathfrak{n}$ | $1$ | $97.85\%$ |
| $D$ | $2$ | $94.74\%$ |
| $T$ | $3$ | $84.04\%$ |
| ${}^3\mathrm{He}$ | $3$ | $89.34\%$ |
| ${}^4\mathrm{He}$ | $4$ | $83.09\%$ |

The $5.3$-percentage-point gap between $T$ and ${}^3\mathrm{He}$ —
two isobars with the *same* mass number $A = 3$ — is structurally
significant: by the proposition above, this difference has zero
crystal-limit content.  All of it is finite-$q$ curvature on the
single-generator-inversion direction
$\sigma_5 \leftrightarrow \sigma_5^{-1}$.

This sharpens the decay question: the gross trend $98\% \to 83\%$
as $A$ grows from $1$ to $4$ may yet admit a power-law fit, but the
**isobar splitting** within $A = 3$ is now identified as a curvature
observable, not a structural property of $\beta_A$.

## Falsifiable predictions

1. *For every pair of isospin-mirror nuclei $(N, Z) \leftrightarrow
   (Z, N)$ whose canonical atomic braid words differ only by
   signed-generator inversions, the
   $S_{\mathrm{crystal}}$ values match to within numerical precision
   (50 dps via
   [`term7_alpha5_crystal_derivation.py`](../../../folio-assistant/computations/term7_alpha5_crystal_derivation.py)).*

2. *The difference $\Delta\mathfrak{m}(K, K')$ between any such
   isobar pair scales linearly in $\alpha_5$ to first order in
   $(q_0 - 1)$, and quadratically thereafter; the leading
   coefficient is determined by the height-$6$ Hoefsmit characters
   $\partial_q \chi^\lambda |_{q = 0}$ on the differentiated
   generator subset $S$.*

3. *The doubly-magic atom ${}^4\mathrm{He}$ has $|S_{\mathrm{crystal}}|$
   approximately three orders of magnitude larger than the
   isobar pair $(T, {}^3\mathrm{He})$ — witness:
   $|S_{\mathrm{crystal}}({}^4\mathrm{He})| \approx 0.991$ vs.\
   $|S_{\mathrm{crystal}}({}^3\mathrm{He})| \approx 0.00206$.
   This is a structural manifestation of shell-closure: the height-$6$
   Plancherel weight saturates at $A = 4$
   ([term7 height-6 partition enumeration](../../../folio-assistant/computations/term7-height6-partition-enum.witness.json)).*

## Status

This proposition is **conditional on**
[`conj:crystal-graph-realization`](#conj:crystal-graph-realization)
(the conjectural identification of the $q \to 0$ limit of
$\chi^\lambda$ with the signed-permutation action on
$\mathrm{SYT}(\lambda)$ used by
[`term7_alpha5_crystal_derivation.py`](../../../folio-assistant/computations/term7_alpha5_crystal_derivation.py)).
Modulo that conjecture, the equality
$S_{\mathrm{crystal}}(T) = S_{\mathrm{crystal}}({}^3\mathrm{He})$
is **exact** (no empirical fit) and the proposition itself is a
fully verified Lean theorem under the
$[\mathrm{CrystalGraphRealization}]$ class hypothesis
(CLAUDE.md §3b-cond conditional class).
