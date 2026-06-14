The crystal-limit shell-correction sum
$S_{\mathrm{crystal}}(A)$ defined in
shell-correction Term 7
is invariant under generator inversion of the *plain* Hecke
crossings in an atomic braid word.

**Scope.** The proposition proven below applies to braid words
written in **signed-generator form**: each letter is $\sigma_i$ or
$\sigma_i^{-1}$ for some $i$.  It does **not** automatically extend
to the canonical convention of
[`mass_at_3A_proper.atom_braid_word_3A`](../../../folio-assistant/computations/mass_at_3A_proper.py),
which uses an operator-valued **dual-pairing interface**
$\bowtie_K = \sigma_g - \frac{h}{2} \cdot \mathbf{1}$
(the "averaged" crossing) between unlike-isospin nucleons,
$\sigma_g^{-1}$ between like-neutron pairs, and plain $\sigma_g$
between like-proton pairs.  The interface coefficient $h = q - q^{-1}$
diverges at $q = 0$, so $\bowtie_K$ does **not** have a naive crystal
limit; extending the proposition to canonical $\bowtie_K$-coupled
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

acting on the same SYT eigenline.  The crystal-limit generators
therefore act *diagonally* on the SYT basis with eigenvalues
that are individually invariant under $\sigma_i \leftrightarrow
\sigma_i^{-1}$.  For any fixed $T \in \mathrm{SYT}(\lambda)$, the
eigenvalue product along a braid word

$$
  \mu^\lambda_T(\beta) \;:=\; \prod_{\ell \,\in\, \beta} \mathrm{eigval}_T(\ell)
$$

is therefore equal under $\beta \to \beta'$.  Note that
$\mu^\lambda_T$ is *not* the character $\chi^\lambda$ — it is the
eigenvalue product *on the line through $T$*; the character is the
trace

$$
  \chi^\lambda_{\mathrm{crystal}}(\beta) \;=\; \sum_{T \in \mathrm{SYT}(\lambda)}
      \mu^\lambda_T(\beta).
$$

The trace is *not* multiplicative in $\beta$, but it is a sum of
sign-flip-invariant per-eigenline contributions, so

$$
  \chi^\lambda_{\mathrm{crystal}}(\beta_A)
    \;=\; \sum_{T \in \mathrm{SYT}(\lambda)} \mu^\lambda_T(\beta_A)
    \;=\; \sum_{T \in \mathrm{SYT}(\lambda)} \mu^\lambda_T(\beta_A')
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
$\bowtie_K$-coupled convention
[`mass_at_3A_proper.atom_braid_word_3A`](../../../folio-assistant/computations/mass_at_3A_proper.py),
${}^3\mathrm{H}$ has interface types $(pn{=}\bowtie_K,\;nn{=}\sigma^{-1})$
while ${}^3\mathrm{He}$ has $(pp{=}\sigma,\;pn{=}\bowtie_K)$ — the
words differ in *interface type*, not just generator signs, so the
sign-flip proposition does not apply directly.  The legacy
disjoint-product witness used by `term7_alpha5_crystal_derivation`
artificially erases this isospin asymmetry.

## Consequences

**Term 7 is isospin-blind at the crystal limit, even in the legacy
disjoint-product convention.** The current
[`term7_alpha5_crystal_derivation.py`](../../../folio-assistant/computations/term7_alpha5_crystal_derivation.py)
assigns *the same* crystal-side shell residual to T and to
$^3\mathrm{He}$.  Experimentally
$\mathfrak{m}({}^3\mathrm{H}) - \mathfrak{m}({}^3\mathrm{He})
\approx 0.529\;\mathrm{MeV}$ and the 2-row Wedderburn dominance
fractions differ ($84.04\%$ vs.\ $89.34\%$ at $q_0 \approx 1.110$;
witness
[`delta-lambda-2row-stratum.witness.json`](../../../folio-assistant/computations/delta-lambda-2row-stratum.witness.json)).
The proposition derives the legacy-convention equality from a
*specific* mechanism (Hecke skein at $q = 0$ collapses
$\sigma_i \leftrightarrow \sigma_i^{-1}$ to the same SYT action).

**Convergent finding from
[spin-involution / LP-dual invariance](#prop:spin-involution-lp-dual-invariance):**
the LP-dual binding-energy shadow price $y_0^*(K)$ at *finite* $q$
in the *canonical* $\bowtie_K$-coupled convention also satisfies
$y_0^*(T) = y_0^*({}^3\mathrm{He})$ exactly, in both 2-row and
height-$6$ strata, at every probed
$q \in \{1.001, 1.050, 1.110\}$ (witness:
LP-dual isospin invariance).
That proposition derives the equality from a **deeper structural
mechanism** — the Hopf antipode
$S \colon V_\lambda \leftrightarrow V_{\lambda^T}$ exchanging
matter and antimatter (equivalently $Z \leftrightarrow N$) — which
applies to the canonical convention without requiring the crystal
limit.

The two derivations are independent: this proposition proves
$T = {}^3\mathrm{He}$ at $q = 0$ under the legacy convention via
sign-flip invariance;
[spin-involution invariance](#prop:spin-involution-lp-dual-invariance)
proves $T = {}^3\mathrm{He}$ at $q = q_0$ under the canonical
convention via the Hopf antipode.  Both predict the same
observable equality through different algebraic levers.  The
empirical $0.529$ MeV mass split must therefore live in a
*different* sector that breaks the $Z \leftrightarrow N$ symmetry
— most plausibly the electromagnetic / Coulomb correction, which
is not a $\sigma$- or $S$-invariant perturbation of the Markov
trace (see
[mirror-isobar EM localisation](#rem:isospin-mass-split-em-localisation)).

**Corollary (q-curvature of isospin-mirror pairs).**
*For any pair of isospin-mirror atoms $K, K'$ whose canonical braid
words differ only by signed-generator inversions, the difference*

$$
  \Delta S(K, K')(q)
    \;:=\; S(\mathcal{B}_K)(q) - S(\beta_{K'})(q)
$$

*satisfies $\Delta S(K, K')(0) = 0$ and (empirically, for $K = T$,
$K' = {}^3\mathrm{He}$, $q_0 \approx 1.110$) $\Delta S(K, K')(q_0)
\neq 0$.  The function $q \mapsto \Delta S(K, K')(q)$ is therefore
a direct probe of the **curvature** of the flat-transport map
underlying $\alpha_5$ at the height-$6$ stratum (cf.\ the
ontological-agnosticism remark in this chapter).*

## Open work: canonical $\bowtie_K$ extension

The proposition above is a structural identity proved at $q = 0$
under the **legacy disjoint-product convention**.  The
[Hopf-antipode invariance](#prop:spin-involution-lp-dual-invariance)
shows the analogous equality $T \leftrightarrow {}^3\mathrm{He}$
persists in the canonical $\bowtie_K$-coupled convention at finite
$q$.  Two follow-ups remain to bridge the two:

1. **Migrate
   [`term7_alpha5_crystal_derivation.py`](../../../folio-assistant/computations/term7_alpha5_crystal_derivation.py)
   to the canonical word
   [`mass_at_3A_proper.atom_braid_word_3A`](../../../folio-assistant/computations/mass_at_3A_proper.py).**
   The script's hardcoded `ATOMS` list treats each nucleon as a
   disjoint 3-strand sub-word with no inter-nucleon coupling.  The
   canonical word emits triples $(c, d, g)$ with
   $d \in \{0, -h, -h/2\}$ encoding $\sigma_g$, $\sigma_g^{-1}$, and
   $\bowtie_K = \sigma_g - (h/2)\cdot\mathbf{1}$.

2. **Define a regularised crystal functional for $\bowtie_K$.**  The
   averaged interface coefficient $h = q - q^{-1}$ diverges at
   $q = 0$, so a naive $q \to 0$ limit of the canonical word is
   ill-defined.  A per-letter $q$-power renormalisation
   $\hat\sigma := q\sigma$, $\hat\sigma^{-1} := q\sigma^{-1}$,
   $\hat\bowtie_K := q\bowtie_K$ yields bounded eigenvalues at
   $q = 0$:

   $$
     \hat\sigma  \xrightarrow{q \to 0} {-P_-}, \qquad
     \hat\sigma^{-1} \xrightarrow{q \to 0} P_+, \qquad
     \hat\bowtie_K \xrightarrow{q \to 0} \tfrac{1}{2}(P_+ - P_-)
   $$

   where $P_\pm$ are the (anti)symmetric SYT projectors.  At the
   algebra level, $\hat\sigma^2 = (q^2 - 1)\hat\sigma + q^2
   \xrightarrow{q \to 0} -\hat\sigma$, which correctly reproduces
   the *0-Hecke algebra* relation $\hat\sigma^2 = -\hat\sigma$.

   The pitfall a per-letter renormalisation runs into is *not* an
   algebraic zero, but a *generic vanishing on shared eigenlines*:
   $\hat\sigma$ acts as $0$ on every symmetric SYT eigenline, so
   any word containing $\hat\sigma_g$ acting on a symmetric SYT
   collapses to zero contribution from that SYT.  For canonical
   words like the proton intra (five consecutive $\sigma_g$ at
   gen $0$), this cuts the surviving contributions to those SYTs
   that are antisymmetric at gen $0$ — a much smaller subset than
   the bare Plancherel weight expects.  The empirical result of
   running this renormalisation on the canonical $D$, $T$,
   $^3\mathrm{He}$, $^4\mathrm{He}$ words is essentially zero
   for $D$ ($\sim 10^{-19}$) and small numerical residuals for the
   isobars — non-trivial but quantitatively unconvincing as a
   replacement for the legacy crystal functional.

   A correct regularisation must take the limit at the level of
   the trace $\chi^\lambda(\beta_{\mathrm{can}})$ (whole-word
   renormalisation), or use a different categorical-limit
   prescription such as Kashiwara's crystal basis on the
   Lusztig-canonical lattice.  Once defined, the canonical
   crystal functional should preserve the
   $T \leftrightarrow {}^3\mathrm{He}$ equality predicted by the
   [Hopf-antipode proposition](#prop:spin-involution-lp-dual-invariance)
   while distinguishing $D$ and ${}^4\mathrm{He}$ structurally.

## Connection to the 2-row decay observation

The empirical 2-row Wedderburn dominance fractions tabulated in
[`delta-lambda-2row-stratum.witness.json`](../../../folio-assistant/computations/delta-lambda-2row-stratum.witness.json)
decay non-monotonically with mass number $A$:

See [Table](#tbl:crystal-isospin-degeneracy-table-data).

The $5.3$-percentage-point gap between $T$ and ${}^3\mathrm{He}$ —
two isobars with the *same* mass number $A = 3$ — is structurally
significant: by the proposition above, this difference has zero
crystal-limit content.  All of it is finite-$q$ curvature on the
single-generator-inversion direction
$\sigma_5 \leftrightarrow \sigma_5^{-1}$.

**Scoping caveat.** The 2-row dominance fractions in the table
are computed from the canonical $\bowtie_K$-coupled atomic braid
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
convention until the canonical $\bowtie_K$ migration completes
(see Open work).*

1. *For every pair of legacy-convention atomic braid words that
   differ only by signed-generator inversions, the
   $S_{\mathrm{crystal}}$ values match to within numerical precision
   (50 dps via
   [`term7_alpha5_crystal_derivation.py`](../../../folio-assistant/computations/term7_alpha5_crystal_derivation.py)).*

2. *Once the canonical $\bowtie_K$ extension is in place, the
   crystal-side prediction of the $T$–${}^3\mathrm{He}$ mass
   splitting will be non-zero (the tensor-product artefact removed)
   and should match $\approx 0.529$ MeV when paired with the AME-
   calibrated $\alpha_5$.  Failure of that match diagnoses curvature
   in the $q \to 0 \rightsquigarrow q_0$ transport at the
   $\bowtie_K$-stratum.*

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
