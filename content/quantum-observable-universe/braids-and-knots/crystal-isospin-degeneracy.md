The crystal-limit shell-correction sum
$S_{\mathrm{crystal}}(A)$ defined in
[shell-correction Term 7](#conj:shell-correction-term-seven)
is invariant under generator inversion of the *plain* Hecke
crossings in an atomic braid word.

**Scope.** The proposition proven below applies to braid words
written in **signed-generator form**: each letter is $\sigma_i$ or
$\sigma_i^{-1}$ for some $i$.  It does **not** automatically extend
to the canonical convention of
[`mass_at_3A_proper.atom_braid_word_3A`](../../../folio-assistant/computations/mass_at_3A_proper.py),
which uses an operator-valued **dual-pairing interface**
$\Delta_I = \sigma_g - \frac{h}{2} \cdot \mathbf{1}$
(the "averaged" crossing) between unlike-isospin nucleons,
$\sigma_g^{-1}$ between like-neutron pairs, and plain $\sigma_g$
between like-proton pairs.  The interface coefficient $h = q - q^{-1}$
diverges at $q = 0$, so $\Delta_I$ does **not** have a naive crystal
limit; extending the proposition to canonical $\Delta_I$-coupled
words requires a regularised (or renormalised) crystal functional
and is left as separate work (see the *Open work* section below).

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

**Conditional corollary (legacy disjoint-product convention).**
*Suppose tritium and helium-3 are presented by the simplified
disjoint-product words used by
[`term7_alpha5_crystal_derivation.py`](../../../folio-assistant/computations/term7_alpha5_crystal_derivation.py)*

$$
  \tilde\beta_T = \sigma_1\sigma_2\sigma_1^{-1}\sigma_4\sigma_5^{-1}\sigma_4
              \sigma_7\sigma_8^{-1}\sigma_7,
  \qquad
  \tilde\beta_{{}^3\mathrm{He}} = \sigma_1\sigma_2\sigma_1^{-1}\sigma_4\sigma_5\sigma_4^{-1}
              \sigma_7\sigma_8^{-1}\sigma_7
$$

*(differing only at positions $5$ and $6$ by paired inversion).
Then*

$$
  S_{\mathrm{crystal}}(\tilde\beta_T) \;=\; S_{\mathrm{crystal}}(\tilde\beta_{{}^3\mathrm{He}}),
$$

*matching the witness
[`term7-alpha5-crystal-derivation.witness.json`](../../../folio-assistant/computations/term7-alpha5-crystal-derivation.witness.json)
which records both values to fifty decimal digits as
$0.0020612874779541296$.*

**Caveat — this corollary is *not* a statement about physical
${}^3\mathrm{H}$ vs.\ ${}^3\mathrm{He}$.** Under the canonical
$\Delta_I$-coupled convention
[`mass_at_3A_proper.atom_braid_word_3A`](../../../folio-assistant/computations/mass_at_3A_proper.py),
${}^3\mathrm{H}$ has interface types $(pn{=}\Delta_I,\;nn{=}\sigma^{-1})$
while ${}^3\mathrm{He}$ has $(pp{=}\sigma,\;pn{=}\Delta_I)$ — the
words differ in *interface type*, not just generator signs, so the
sign-flip proposition does not apply directly.  The legacy
disjoint-product witness used by `term7_alpha5_crystal_derivation`
artificially erases this isospin asymmetry.

## Consequences

**Within the legacy disjoint-product convention, Term 7 is
isospin-blind at the crystal limit.** The current
[`term7_alpha5_crystal_derivation.py`](../../../folio-assistant/computations/term7_alpha5_crystal_derivation.py)
assigns *the same* shell residual to T and to $^3\mathrm{He}$,
even though experimentally
$\mathfrak{m}({}^3\mathrm{H}) - \mathfrak{m}({}^3\mathrm{He})
\approx 0.529\;\mathrm{MeV}$ and the 2-row Wedderburn dominance
fractions differ ($84.04\%$ vs.\ $89.34\%$ at $q_0 \approx 1.110$;
witness
[`delta-lambda-2row-stratum.witness.json`](../../../folio-assistant/computations/delta-lambda-2row-stratum.witness.json)).
This isospin-blindness is **a known artefact** of the legacy
disjoint-product convention — it goes away once the canonical
$\Delta_I$-coupled word is used, because canonical T and
${}^3\mathrm{He}$ words differ in interface *type*
($pn{=}\Delta_I + nn{=}\sigma^{-1}$ vs.\
$pp{=}\sigma + pn{=}\Delta_I$), not just generator sign.  Migrating
the crystal derivation to canonical words is tracked separately
(see *Open work* below).

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

## Open work: canonical $\Delta_I$ extension

The proposition above is a structural identity of the **legacy
disjoint-product convention**.  Two follow-ups are required to
turn it into a physical statement:

1. **Migrate
   [`term7_alpha5_crystal_derivation.py`](../../../folio-assistant/computations/term7_alpha5_crystal_derivation.py)
   to the canonical word
   [`mass_at_3A_proper.atom_braid_word_3A`](../../../folio-assistant/computations/mass_at_3A_proper.py).**
   The script's hardcoded `ATOMS` list (signed integer words) treats
   each nucleon as a disjoint 3-strand sub-word with no inter-nucleon
   coupling.  The canonical word emits triples $(c, d, g)$ with
   $d \in \{0, -h, -h/2\}$ encoding $\sigma_g$, $\sigma_g^{-1}$, and
   $\Delta_I = \sigma_g - (h/2)\cdot\mathbf{1}$.

2. **Define a regularised crystal functional for $\Delta_I$.**  The
   averaged interface coefficient $h = q - q^{-1}$ diverges at
   $q = 0$, so a naive $q \to 0$ limit of the canonical word is
   ill-defined.  A finite renormalised functional $S_{\mathrm{crystal}}^{\mathrm{can}}$
   would identify the regularised image of $\Delta_I$ as a
   crystal-graph operator (e.g. an explicit Kashiwara $\tilde{e}$
   / $\tilde{f}$ combination, or the level-crossing average on
   $\mathrm{SYT}(\lambda)$).  Once defined, the analogue of this
   proposition for $S_{\mathrm{crystal}}^{\mathrm{can}}$ would
   distinguish T from ${}^3\mathrm{He}$ structurally and yield a
   crystal-side prediction of the $T$–${}^3\mathrm{He}$ mass
   splitting without empirical AME calibration.

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

**Scoping caveat.** The 2-row dominance fractions in the table
are computed from the canonical $\Delta_I$-coupled atomic braid
words via
[`global_wedderburn_sum_q_hecke_seminormal`](../../../folio-assistant/computations/wedderburn_jones_markov.py)
at $q = q_0$.  They are **physical** quantities.  The proposition
above, by contrast, currently lives in the legacy disjoint-product
convention, so it can only address the structural part of the
T--${}^3\mathrm{He}$ split that survives in *both* conventions.
Sharpening the decay question to "what does the canonical-convention
crystal limit say about the $T$--${}^3\mathrm{He}$ 2-row gap?"
requires the canonical migration in *Open work* above.

## Falsifiable predictions

*All predictions below are scoped to the legacy disjoint-product
convention until the canonical $\Delta_I$ migration completes
(see Open work).*

1. *For every pair of legacy-convention atomic braid words that
   differ only by signed-generator inversions, the
   $S_{\mathrm{crystal}}$ values match to within numerical precision
   (50 dps via
   [`term7_alpha5_crystal_derivation.py`](../../../folio-assistant/computations/term7_alpha5_crystal_derivation.py)).*

2. *Once the canonical $\Delta_I$ extension is in place, the
   crystal-side prediction of the $T$–${}^3\mathrm{He}$ mass
   splitting will be non-zero (the tensor-product artefact removed)
   and should match $\approx 0.529$ MeV when paired with the AME-
   calibrated $\alpha_5$.  Failure of that match diagnoses curvature
   in the $q \to 0 \rightsquigarrow q_0$ transport at the
   $\Delta_I$-stratum.*

3. *The doubly-magic atom ${}^4\mathrm{He}$ has
   $|S_{\mathrm{crystal}}|$ approximately three orders of magnitude
   larger than the (legacy-convention) isobar pair
   $(T, {}^3\mathrm{He})$ — witness:
   $|S_{\mathrm{crystal}}({}^4\mathrm{He})| \approx 0.991$ vs.\
   $|S_{\mathrm{crystal}}({}^3\mathrm{He})| \approx 0.00206$.
   This shell-closure feature is expected to **persist** under the
   canonical migration: the height-$6$ Plancherel weight saturates
   at $A = 4$
   ([term7 height-6 partition enumeration](../../../folio-assistant/computations/term7-height6-partition-enum.witness.json)),
   and that fact is independent of the interface convention.*

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
