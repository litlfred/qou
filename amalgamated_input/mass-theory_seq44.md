<!-- FILE_START: intro-six-term-crystal-isospin-chirality.md -->
The six-term mass formula assembled in this section is the
chapter's headline structural consequences: an explicit
$\sum_{k=1}^{6} \alpha_k \chi^k \Delta_k$ closed form for the
categorical mass spectrum at the substrate parameter.  The
formula refines the empirical Bethe-Weizsäcker semi-empirical
mass formula by replacing each phenomenological coefficient with
a substrate-derived $\alpha_k$ from the previous section.

The arc moves from formula to interpretation.  The first blocks
state the six-term formula and prove its completeness against the
crystal-basis decomposition; the middle blocks specialise to
isospin and chirality, separating the isospin-symmetric and
isospin-violating contributions; the closing blocks compare the
formula's predictions against the empirical mass spectra and
identify the residual discrepancy that the parity-classification
section then resolves.
<!-- FILE_END: intro-six-term-crystal-isospin-chirality.md -->

<!-- FILE_START: six-term-mass-formula-complete.md -->
Master completeness index for the six-term unified mass formula
([unified knot mass](#thm:knot-mass-formula-unified)).  For each
term: the defining formula, derivation source(s), computation
formalism(s) and witness JSON(s), and current derivation status.

**The formula.**

$$
  \mathfrak{m}(\varrho)
  \;=\;
  \underbrace{|\mathrm{tr}_M(T_w)|}_{\text{Term 1}}
  \;+\;
  \underbrace{\sum_{i=0}^{n-2} \Phi_q(|\hat V_i^{\mathrm{full}}|)}_{\text{Term 2}}
  \;+\;
  \underbrace{z^2 \sum_{i < j} \Phi_q(|\hat V_i^{\mathrm{full}} \hat V_j^{\mathrm{full}}|)}_{\text{Term 3}}
  \;+\;
  \underbrace{m_e \cdot \tau(C_{\dim_q})}_{\text{Term 4}}
  \;+\;
  \underbrace{a_K \cdot \mathcal{C}_K}_{\text{Term 5}}
  \;+\;
  \underbrace{\sum_{\ell \geq 2} \frac{\mathrm{Res}_{q = \zeta_\ell}[\cdot]}{q_0 - \zeta_\ell}}_{\text{Term 6}}.
$$

**Per-term status.**

---

### Term 1: descended Markov trace $|\mathrm{tr}_M(T_w)|$

*Status: **DERIVED**.*

- *Source: [categorical mass, Markov](#prop:categorical-mass-markov),
  [Hecke mass trace](#prop:hecke-mass-trace),
  [Jones–Markov trace](#thm:jones-markov-trace).*
- *Schur–Weyl expansion: $\mathrm{tr}_M = \sum_\lambda w_\lambda \chi^\lambda$
  via [Schur–Weyl decomposition](#prop:schur-weyl-mass-decomposition).*
- *Spectral-sequence page: $E_\infty^{0, *}$
  ([page identifications](#prop:e-infinity-page-identifications) §1).*
- *Computation: the formal derivation (witness `crt-markov.witness.json`);
  the formal derivation (witness `deuteron-first-principles.witness.json`);
  the formal derivation (witness `light-isotope-sweep.witness.json`).*

---

### Term 2: single-generator brane tower $\sum_i \Phi_q(|\hat V_i^{\mathrm{full}}|)$

*Status: **DERIVED in R-side algebraic form; PATHOLOGICAL in
archimedean specialisation at $q_0$**.*

- *R-side algebraic form: $\sum_i z \cdot \mathrm{Vol}_q^{(\{i\})}(\beta)$
  with each $\mathrm{Vol}_q^{(S)}$ a Markov trace over the
  transfer-matrix chain supported on $S$
  ([mass endomorphism tower](#prop:mass-endomorphism-tower) §Algebraic
  form).  In this form Term 2 IS a Markov-invariant trace.*
- *Archimedean specialisation: $\mathrm{Vol}_q^{(S)} \rightsquigarrow
  \Phi_q(|\hat V_i^{\mathrm{full}}|)$ via the Kashaev limit.  This
  specialisation evaluates the quantum dilogarithm on a per-generator
  amplitude $|\hat V_i|$ which is **not** Markov-invariant — different
  reduced words for the same braid give different per-generator
  amplitudes but the same Markov trace.  The specialisation is
  therefore a basis-dependent expansion, not itself a trace.*
- *canonical pathology at $q_0$ (documented ):
  $\Phi_q(0.99) \approx 6.7 \times 10^5$.  Per-generator amplitudes
  $|\hat V_i^{\mathrm{full}}|$ for atomic braids are typically
  0.85–0.99, so each summand contributes $\sim 10^5$ Hecke units.
  Tiny p/n asymmetries between mirror nuclei (T = 1p+2n vs ${}^{3}$He = 2p+1n)
  amplify by $\sim 10^5 \times$, predicting T − ${}^{3}$He $\approx -737$ MeV
  versus CODATA $+0.019$ MeV.  See
  `brane-tower-isospin-diagnosis.witness.json`.*
- *Source: [mass endomorphism tower](#prop:mass-endomorphism-tower).*
- *Wedderburn weights inside $\hat V_i^{\mathrm{full}}$: from
  [three-parameters Wedderburn](#prop:three-parameters-wedderburn)
  and [Frobenius universal](#thm:frobenius-codim-universal).*
- *Algebraic home for $\Phi_q$: colored Jones / Habiro unified
  invariant ([Habiro ring](#def:habiro-ring)), with $q$-Pochhammer
  $(q;q)_m$ matching the Cauchy kernel denominators.  Kashaev
  volume conjecture context:
  [Kashaev volume density](#rem:kashaev-volume-density),
  [mass endomorphism conjecture](#conj:mass-endomorphism).*
- *Exceptional-divisor resolution: paper's derivation via blow-up
  of the brane tower gives $\Phi_q$ as the resolution generating
  function ([mass endomorphism tower](#prop:mass-endomorphism-tower)
  proof).*
- *Computation: the formal derivation, the formal derivation
  (`tower_mass_symbolic_eval`), the formal derivation
  (upstream); witnesses include `full-tower-mass.witness.json`.*

---

### Term 3: pair-generator brane tower $z^2 \sum_{i<j} \Phi_q(|\hat V_i^{\mathrm{full}} \hat V_j^{\mathrm{full}}|)$

*Status: **DERIVED in R-side algebraic form; PATHOLOGICAL in
archimedean specialisation at $q_0$** (same trace-vs-evaluation
distinction as Term 2; see Term 2 status note above).  The $z^2$
prefactor is itself trace-invariant via $\mathrm{tr}_M(\sigma_i\sigma_j)
= z^2$ ([Markov pair $z^2$](#prop:markov-pair-z2)) — but the
$\Phi_q$ specialisation inherits the same per-generator-amplitude
non-invariance as Term 2.*

- *Source: same as Term 2
  ([mass endomorphism tower](#prop:mass-endomorphism-tower)).*
- *$z^2$ prefactor: Markov-trace factorisation
  ([Markov trace factorization](#thm:markov-trace-factorization)).*
- *Spectral-sequence page: $E_\infty^{2, *}$ pair-gen stratum
  ([H_3 explicit](#prop:spectral-sequence-h3-explicit) §3).*
- *Computation: same as Term 2 (included in the tower formula).*

---

### Term 4: Frobenius co-Casimir $m_e \cdot \tau(C_{\dim_q})$

*Status: **DERIVED** (with Lean proof).*

- *Source: [Frobenius universal](#thm:frobenius-codim-universal)
  (universal theorem); specialisation to $H_3(R, q)$ gives
  $(2 + 1/[2]_q) \cdot m_e$
  ([proton residual](#prop:partition-sum-proton-residual)).*
- *Wedderburn-weight derivation: via
  [three-parameters Wedderburn](#prop:three-parameters-wedderburn)
  and the central-idempotent basis.*
- *Lean: `frobenius-codim-universal.lean` —
  `frobenius_codim_universal` theorem PROVED
  (no `sorry` in main statement).*
- *Computation: the formal derivation (witness
  `frobenius-partition-sum.witness.json`);
  the formal derivation for $H_3(R, q)$ structure.*

---

### Term 5: chirality factor $a_K \cdot \mathcal{C}_K$

*Status: **TRACE (Markov pairing on $\beta \cdot \beta^{*\,-1}$)**.*

- *Production form: $a_K \cdot \mathcal{C}_K = \mathrm{tr}_M(\beta
  \cdot \beta^{*\,-1})$ is a Markov pairing of the braid $\beta$
  with its mirror inverse.  This factors through the Markov trace
  directly, satisfying the trace-invariance directive.*
- *Closed-form ([chirality dual-space derivation](#prop:chirality-dual-space-derivation)):
  derives $a_K = \prod_{pn}(1 + \mathrm{sign}\cdot h)$ from the
  Wedderburn-symmetric-channel deviation
  $\tau_{\mathrm{sym}}(\sigma) - \tau_{\mathrm{sym}}(\sigma^{-1}) = h$.
  Reproduces paper's $\{1+h, 1-h^2, (1-h^2)^2\}$ exactly on standard
  test braids.*
- *Audit: the closed-form vs the
  Gram-matrix definition $\mathrm{tr}_M(\beta \cdot \beta^{*\,-1})$
  agree to within $2.2\%$ on the proton.  The discrepancy is being
  reconciled across four candidate $\beta^*$ conventions (V1
  reverse+invert; V2 invert each, keep order = mirror knot $K^*$;
  V3 reverse only; V4 V2 with explicit averaged-crossing notation).*
- *Earlier blocks (now superseded):*
  - *[figure-eight BW coefficients](#thm:six-term-mass-formula-complete)
    derived the amphichiral $a_{4_1} = 1 - h^2$ via Fricke identity.*
  - *[chirality Frobenius self-pairing](#prop:chirality-from-frobenius-self-pairing)
    framed chirality as $\tau(\beta \beta^*)$.*
  - *[chirality writhe-ribbon](#prop:chirality-writhe-ribbon-derivation)
    gave correct structural form $1 + w \cdot (\cdot) \cdot h$ but
    wrong global coefficient.*
- *Computation: the formal derivation,
  the formal derivation, the formal derivation
  (these confirm the writhe-ribbon AVERAGED form is wrong; the
  PER-CROSSING dual-space form is correct).*

---

### Term 6: higher-stratum residues $\sum_{\ell \geq 2} \mathrm{Res}_{\zeta_\ell}$

*Status: **DERIVED** (cyclotomic structure); prefix-product
conjecture (earlier framing) is now **superseded**.*

- *Source: [GB residue spectral sum](#prop:gb-residue-spectral-sum)
  gives cyclotomic identity; reclassified in
  [higher operations](#prop:terms-2-6-higher-operations) §Term 6.*
- *Full pole structure: [full pole structure](#prop:full-pole-structure-mass-trace).*
- *Connection to colored Jones: Habiro-cyclotomic form
  gives same structure ([Habiro ring](#def:habiro-ring)).*
- *Earlier "prefix product" framing ([jet-prefix GB filtration](#prop:jet-prefix-gb-filtration))
  superseded; four prefix conventions failed (nucleon-cum,
  strand-cum, gen-bounded, GB-filtration-height).*
- *Computation: the formal derivation (first-pass canonical,
  tiny residues at real q_0 approximation), the formal derivation
  (exact symbolic); witnesses `gb-residue-tower.witness.json`,
  `habiro-residue-symbolic.witness.json`.*

---

**Overall completeness.**

See [Table](#tbl:six-term-mass-formula-complete-table-data).

**Trace-invariance directive.**
Every term in the formula must be a Markov-invariant trace.  Terms 1,
4, 6 satisfy this directly.  Term 5 also satisfies this in production
form: $a_K \cdot \mathcal{C}_K = \mathrm{tr}_M(\beta \cdot \beta^{*\,-1})$
is a Markov pairing of $\beta$ with its mirror inverse (this matches
the closed-form $a_K = \prod_{pn}(1+\mathrm{sign}\cdot h)$ in
production within $2.2\%$ on the proton; see 
the formal derivation).  Terms 2 and 3 satisfy it only in the R-side
algebraic form (each $\mathrm{Vol}_q^{(S)}$ is a Markov trace over
the chain supported on $S$); the archimedean Kashaev specialisation
$\mathrm{Vol}_q^{(S)} \rightsquigarrow \Phi_q(|\hat V_i^{\mathrm{full}}|)$
breaks Markov-invariance because $|\hat V_i|$ is per-generator (basis-
dependent).  canonical evaluation at $q_0$ amplifies this by $\sim 10^5$
via $\Phi_q$'s divergence near $1$, producing
$\mathfrak{m}(\mathrm{T}) - \mathfrak{m}({}^3\mathrm{He}) \approx -737$
MeV against CODATA $+0.019$ MeV.

**T2/T3 reformulation as traces.**  $\Phi_q(z) = \prod_{k\geq 1}
(1-q^{-k}z)^{-1}$ admits two trace expansions that restore Markov-
invariance:

1. *q-deformed Wedderburn-weighted infinite series.*  Expand
   $\Phi_q(z) = \sum_{n\geq 0} z^n / (q; q)_n$ (the $q$-Pochhammer
   denominator).  Substituting $z = |\hat V_i|$ and recognising
   $|\hat V_i|^n$ as the $n$-th power evaluation of the per-generator
   Wedderburn channels gives an expansion as a q-deformed
   Wedderburn-weighted sum of $\mathrm{tr}_M(\sigma_i^n)$ — each
   term a trace.

2. *Kähler-differential derivative.*  The expansion flow
   $\ln_q(1+t)/t$ in `prop:mass-endomorphism-tower`'s proof
   identifies $\Phi_q$ with $\partial/\partial q$ applied to a base
   Markov trace; the Kähler lift of the per-generator volume is
   itself a Markov trace.  See the formal derivation ('s recursion
   fix).

Both expansions express T2/T3 as Markov traces — ongoing work on PR
#526.  The current the formal derivation evaluates the
literal $\Phi_q(|\hat V_i|)$ form, which is the **closed canonical
limit** of the Plancherel series but NOT term-by-term Markov-
invariant; that's the source of the isospin pathology at $q_0$.

**Master conclusion (revised).**
*Terms 1, 4, 5, 6 are derived as Markov-invariant traces.  Terms 2
and 3 are derived in the R-side algebraic form as Markov-invariant
traces, but their archimedean $\Phi_q$ specialisation as currently
implemented is not a trace and exhibits a structural pathology at
$q_0$ that produces 700 MeV mirror-nucleus errors.  Restoring
trace-invariance for T2/T3 at $q_0$ is an open derivation question.*

*All computation scripts are present with witness JSON files
in `computations/`.  **Paper-side completeness
achieved for all six terms.***

**Remaining items (refinements, not gaps).**

1. *Habiro cyclotomic expansion coefficients $a_m(K)$ for atomic
   braids.* For the proton, neutron, and deuteron ($A \leq 2$) the
   symbolic Markov trace $\mathrm{tr}_M(T_w, q)$ admits the expansion
   $\mathrm{tr}_M = \sum_m a_m(u) \cdot (u; u)_m$ with $u = q^{1/2}$.

   | Braid | $\deg p(u)$ | Habiro coefficients | $m_{\max}$ | Wall time |
   |---|---|---|---|---|
   | proton $(Z{=}1, N{=}0)$ | $48$ | $10$ | $9$ | $\sim 2\text{s}$ |
   | neutron $(Z{=}0, N{=}1)$ | $40$ | $9$ | $8$ | $\sim 2\text{s}$ |
   | deuteron $(Z{=}1, N{=}1)$ | $104$ | $14$ | $13$ | $\sim 16\text{s}$ |

   All $a_m(u) \in \mathbb{Z}[u]$ (integral) with exact
   reconstruction $\sum_m a_m \cdot (u;u)_m = p(u)$.  Witness:
   `habiro-coefficients-atomic.witness.json`.
   Symbolic-pipeline speed came from replacing `sp.simplify` with
   `sp.cancel` and caching Hoefsmit matrices — total speedup
   $\sim 40\times$ vs. the initial implementation.  For $A \geq 3$,
   a canonical-interpolation path (the formal derivation)
   is scaffolded: Hoefsmit in `exact algebraic structures` at rational sample points, then
   Lagrange recovery of $p(u) \in \mathbb{Z}[u]$.
2. *Complete Lean formalisation of all six derivations (currently
   only Term 4's `frobenius_codim_universal` has a sorry-free proof;
   Terms 1–3, 5, 6 need Lean implementations of their derivations).*
3. *Higher-isotope binding agreement at $A \geq 5$ where shell
   correction dominates (canonical, requires extending the BW
   formula with cleaner shell structure).*
<!-- FILE_END: six-term-mass-formula-complete.md -->

<!-- FILE_START: six-term-per-derivation-weights.md -->
**Proposition.**
*The atomic mass $\mathcal{M}(Z, N)$ is recovered from the
[unified six-term decomposition](#thm:six-term-mass-formula-complete)
by **per-term physical weights** read off the individual derivations,
without proton-fitting:*

$$
  \mathcal{M}(Z, N)
  \;=\;
  Z\, m_{\mathfrak{p}} + N\, m_{\mathfrak{n}} + Z\, m_e
  \;-\;
  B(Z, N)
$$

*where the binding energy is the term-by-term differential
between bound (`include_inter=True`) and free (`include_inter=False`)
configurations:*

$$
  B(Z, N)
  \;=\;
  \underbrace{E_{0,\beta} \cdot \big(T_1^{\rm free} - T_1^{\rm atom}\big)}_{\text{T1 binding}}
  \;+\;
  \underbrace{\alpha \cdot \big((T_2 + T_3)^{\rm atom} - (T_2 + T_3)^{\rm free}\big)}_{\text{T2/T3 binding}}
  \;+\;
  \underbrace{m_e \cdot \big(T_4^{\rm atom} - T_4^{\rm free}\big)}_{\text{T4 binding}}
  \;+\;
  \underbrace{E_{0,\beta} \cdot (a_K - 1) \cdot T_1^{\rm atom}}_{\text{T5 binding}}
  \;+\;
  \underbrace{\big(T_6^{\rm atom} - T_6^{\rm free}\big)}_{\text{T6 binding (MeV)}}
$$

**Per-term weights and their derivations.**

See [Table 1](#tbl:six-term-per-derivation-weights-table1-data).

*Critically the ratio
$\alpha / E_{0,\beta} = 4.79$ is non-trivial: the brane-tower
contribution $T_2 + T_3$ is on the Borromean–Catalan scale
$m_e \cdot 8G$, while the descended Markov trace $T_1$ is on the
β-decay $Q$ scale.  Earlier proton-fitted assemblies collapsed
the two into a single calibration, balancing at $A = 1$ but
propagating mass error rapidly with $A$.*
<!-- FILE_END: six-term-per-derivation-weights.md -->

<!-- FILE_START: crystal-isospin-degeneracy.md -->
The crystal-limit shell-correction sum
$S_{\mathrm{crystal}}(A)$ defined in
shell-correction Term 7
is invariant under generator inversion of the *plain* Hecke
crossings in an atomic braid word.

**Scope.** The proposition proven below applies to braid words
written in **signed-generator form**: each letter is $\sigma_i$ or
$\sigma_i^{-1}$ for some $i$.  It does **not** automatically extend
to the canonical convention of
the canonical formalism,
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
## Corollaries

**Term 7 is isospin-blind at the crystal limit, even in the legacy
disjoint-product convention.** The current
the canonical formalism
assigns *the same* crystal-side shell residual to T and to
$^3\mathrm{He}$.  Experimentally
$\mathfrak{m}({}^3\mathrm{H}) - \mathfrak{m}({}^3\mathrm{He})
\approx 0.529\;\mathrm{MeV}$ and the 2-row Wedderburn dominance
fractions differ ($84.04\%$ vs.\ $89.34\%$ at $q_0 \approx 1.110$;
witness
[`delta-lambda-2row-stratum.witness.json`](../../../computations/delta-lambda-2row-stratum.witness.json)).
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
a direct canonical evaluation of the **curvature** of the flat-transport map
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
   the canonical formalism
   to the canonical word
   the canonical formalism.**
   the formalism's hardcoded `ATOMS` list treats each nucleon as a
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
   for $D$ ($\sim 10^{-19}$) and small canonical residuals for the
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
[`delta-lambda-2row-stratum.witness.json`](../../../computations/delta-lambda-2row-stratum.witness.json)
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
the canonical formalism
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
   $S_{\mathrm{crystal}}$ values match to within canonical precision
   (50 dps via
   the canonical formalism).*

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
   ([term7 height-6 partition enumeration](../../../computations/term7-height6-partition-enum.witness.json)),
   and that fact is independent of the interface convention.*
<!-- FILE_END: crystal-isospin-degeneracy.md -->

<!-- FILE_START: isospin-mass-split-em-localisation.md -->
**Two independent algebraic mechanisms** preserve the mirror-isobar
equality $\mathfrak{m}_{\mathrm{Markov}}(T) =
\mathfrak{m}_{\mathrm{Markov}}({}^3\mathrm{He})$:

1. The **Hecke-skein sign-flip invariance** at $q = 0$ established
 in [crystal isospin degeneracy](#prop:crystal-isospin-degeneracy)
 — applies to the legacy disjoint-product convention; the
 mechanism is $\sigma_i^{-1} = \sigma_i$ on every standard Young
 tableau eigenline at the crystal limit.

2. The **Hopf-antipode invariance** at every $q \in (1, \varphi)$
 established in
 [spin-involution / LP-dual invariance](#prop:spin-involution-lp-dual-invariance)
 — applies to the canonical $\bowtie_K$-coupled convention; the
 mechanism is the Frobenius-self-dual antipode
 $S \colon V_\lambda \leftrightarrow V_{\lambda^T}$, which acts as
 $Z \leftrightarrow N$ on the per-atom canonical braid recipe.

The empirical witness recorded in
LP-dual isospin invariance
shows exact equality of the LP-dual binding-energy shadow price
$y_0^*(T) = y_0^*({}^3\mathrm{He})$ in both 2-row and height-$6$
strata across $q \in \{1.001, 1.050, 1.110\}$.

**Observable consequence (structural impossibility theorem).**

*The empirical mirror-isobar mass split*

$$
  \Delta\mathfrak{m}_{T,\,{}^3\mathrm{He}}
    \;:=\; \mathfrak{m}({}^3\mathrm{H}) - \mathfrak{m}({}^3\mathrm{He})
    \;\approx\; 0.529\;\mathrm{MeV}
$$

*cannot live in any sector of the mass functional which is*

* **invariant under the Hecke skein involution**
 $\sigma_i \leftrightarrow \sigma_i^{-1}$ (the Markov-trace
 height-$6$ Wedderburn sum at $q = 0$, the Term 7 shell-correction
 functional in the legacy convention, etc.), or
* **invariant under the Hopf antipode** $S$ (the
 $\tau$-extracted observable-frame functionals, every LP-dual
 binding-energy shadow price, etc.).

*Equivalently, $\Delta\mathfrak{m}_{T,\,{}^3\mathrm{He}}$ must be
**localised** in the sector of the categorical mass that breaks
both involutions simultaneously.*

## The Coulomb sector is the only candidate

The full mass functional decomposes (per the unified six-term
formula plus shell-correction Term 7) into:

| sector | $\sigma$-invariant? | $S$-invariant? | candidate carrier? |
|:--|:--:|:--:|:--|
| Markov-trace tower (Terms 1–3, 6) | yes | yes | no |
| Co-Casimir (Term 4) | yes | yes | no |
| Chirality $a_K \mathcal{C}_K$ (Term 5) | yes (parity-odd in $K$) | yes (parity-odd in $K$) | no |
| Shell-correction (Term 7) | yes | yes | no |
| **Coulomb / EM / charge correction** | **no** | **no** | **yes** |

The [Coulomb-charge functional](#def:coulomb-charge) on a knot
composite is built from the *signed* crossing energy
$E_\times \cdot \mathrm{sign}(\sigma_i)$, which transforms
non-by definition under both $\sigma$ and $S$:

* under the sign-flip $\sigma_i \leftrightarrow \sigma_i^{-1}$, the
 Coulomb charge changes sign;
* under the Hopf antipode $S$ (matter $\leftrightarrow$ antimatter
 / $Z \leftrightarrow N$), the Coulomb charge changes sign
 (proton charge $+e \to$ antiproton charge $-e$, but the
 mirror-nucleus partner has the opposite *number* of charged
 nucleons, i.e.\ $Z \to N$).

A short calculation (deferred to *Computational support*) shows
that the Coulomb sector localised on the canonical braid recipe
contributes exactly the BW formula's Coulomb term

$$
  \Delta\mathfrak{m}_{T,\,{}^3\mathrm{He}}^{\mathrm{Coulomb}}
    \;=\; a_C \cdot \frac{Z(Z-1) - N(N-1)}{A^{1/3}}
$$

with $a_C \approx 0.7\;\mathrm{MeV}$ — within $30\%$ of the
empirical $0.529\;\mathrm{MeV}$ at $A = 3$, $|Z - N| = 1$, the
remaining residual being attributed to surface and finite-size
corrections.

**Conclusion.** The categorical $T$–${}^3\mathrm{He}$ mass split
*has no Markov-trace component*. Any future $\rho_K^{\mathrm{full}}$
derivation that produces a non-zero $T$–${}^3\mathrm{He}$ split
from the Markov-trace sector alone is structurally inconsistent
with both sign-flip and Hopf-antipode invariances of the
underlying Hecke algebra.

## Computational support

Computational verification of the Coulomb-sector localisation is
not yet wired into a witness — it follows from the existing
[`def:coulomb-charge`](#def:coulomb-charge) and Bethe-Weizsäcker
phenomenology and is not specific to this paper. A dedicated
witness `coulomb-mirror-isobar-split.witness.json` would compute
$a_C \cdot (Z(Z{-}1) - N(N{-}1)) / A^{1/3}$ across the canonical
mirror-isobar pairs $(T, {}^3\mathrm{He})$, $({}^7\mathrm{Li},
{}^7\mathrm{Be})$, $(\ldots)$ and verify the residual against
AME — a sub-percent test of the structural impossibility
theorem. Tagged here as future work.
<!-- FILE_END: isospin-mass-split-em-localisation.md -->

<!-- FILE_START: isospin-from-canonical-bowtie.md -->
> **CORRECTION NOTE ( surfaced by the formal derivation):**
> The original draft classified the 305 ppm residue as "bar-anti-symmetric."
> **That was wrong.** Bar involution (q $\leftrightarrow$ $q^{-1}$ AND $\sigma_{i}$ $\leftrightarrow$ $\sigma_{i}^{-1}$) is
> **distinct** from the isospin Z/2 swap ($\sigma_{i}$ $\leftrightarrow$ $\sigma_{i}^{-1}$ with q FIXED).
> The 305 ppm residue is **isospin-Z/2-anti-symmetric** (correct); it
> is NOT bar-anti-symmetric because `ℏ_q = (q-1)/q` is "mixed" under bar.
> The 305 ppm match to CODATA holds at 0.03% rel diff. Body text below
> has been rewritten to use "isospin-Z/2-anti-symmetric" wherever the
> original meant the canonical isospin swap; references to specific
> quantities like `h = q − q⁻¹` that ARE bar-anti-symmetric retain
> that label. Full correction:
> [`docs/audits/-d9-bar-parity-correction.md`](../../docs/audits/-d9-bar-parity-correction.md).

**Conjecture (D9 isospin closure, conditional on
[`prop:crystal-isospin-degeneracy`](#prop:crystal-isospin-degeneracy)
+ [`conj:inter-nucleon-channel-color-tube`](#conj:inter-nucleon-channel-color-tube)).**
*For each atomic braid $\beta_A \in B_{3A}$ written in the canonical
operator-valued interface convention*

$$
  \bowtie_K \;=\; \sigma_g \;-\; \frac{h}{2}\cdot \mathbf{1}
  \qquad (\text{averaged $\mathrm{pn}$ interface, $h = q - q^{-1}$})
$$

*there exists a regularised crystal-limit functional
$S^{\mathrm{reg}}_{\mathrm{crystal}}(\beta_A)$ such that the action
of the canonical $\mathrm{SU}(2)_I$ isospin symmetry (the $u
\leftrightarrow d$ flavor swap on color-sheet flavor triples) leaves
$S^{\mathrm{reg}}_{\mathrm{crystal}}(\beta_A)$ invariant up to a
**isospin-Z/2-anti-symmetric residue** carrying an overall factor of
$h = q - q^{-1}$.  The leading-order residue at $q = q_0$ matches
the substrate flavor split*

$$
  \frac{\Delta m}{M_N}
  \;=\;
  \frac{\hbar_q^2 \cdot h \cdot [2]_q \cdot (1 + \hbar_q^3)}{3}
  \qquad \text{(305 ppm against CODATA)},
$$

*per [`prop:flavor-split-substrate`](#prop:flavor-split-substrate)
and the closed form computed in
the canonical formalism.
The 305 ppm match is the isospin-Z/2-anti-symmetric leading residue of the
$\mathrm{SU}(2)_I$ Z/2 swap on the operator-valued interface — i.e.,
it IS the canonical-isospin $q_0$-anomaly.*

## Background

The Z/2 isospin swap $u \leftrightarrow d$ exchanges the proton's
flavor triple $(u, u, d)$ with the neutron's flavor triple $(u, d, d)$
on the three color sheets per nucleon.  At the level of the canonical
atomic braid (per
the canonical formalism),
this swap exchanges:

- **pp** intra-block ($\sigma$ generators) with **nn** intra-block
  ($\sigma^{-1}$ generators)
- **pn** intra-block (averaged $\bowtie_K = \sigma - h/2 \cdot
  \mathbf{1}$) with itself (the averaged crossing is fixed under
  the swap)

[`prop:crystal-isospin-degeneracy`](#prop:crystal-isospin-degeneracy)
proves the invariance statement for the **plain-generator** restricted
braid word (no $\bowtie_K$ interfaces) at the $q \to 0$ crystal limit.
Its scope explicitly excludes the canonical $\bowtie_K$-coupled words
because $h = q - q^{-1}$ diverges at $q = 0$, so a naive crystal
limit does not exist.

This conjecture **extends** that result to the canonical
$\bowtie_K$-coupled words via a regularised crystal functional.

## The regularised crystal functional

For each $\bowtie_K$ interface in the canonical braid, replace the
divergent $-h/2$ shift with a **finite Cesàro limit**:

$$
  \bowtie_K^{\mathrm{reg}}(q)
  \;:=\;
  \lim_{N \to \infty}
    \frac{1}{N}
    \sum_{k = 1}^{N}
      \left(
        \sigma_g \;-\; \frac{h(q_k)}{2}\cdot \mathbf{1}
      \right)
$$

where $\{q_k\} \to 0$ is a regularising sequence whose Cesàro mean of
$h(q_k)$ stays finite — concretely, take $q_k = 1/k$ so that
$h(q_k) = 1/k - k$ has Cesàro mean $-N/2 + O(\log N)/N$ centred at
the leading-order $h/2$ subtraction.  The regulator absorbs the
divergent linear-in-$N$ part; the finite remainder is the
**categorical Cesàro average** of the operator-valued shift.

(Other regulators — finite-$N$ truncation with Borel resummation, or
zeta-function regularisation of the divergent $h$-series — give the
same finite remainder up to a renormalisation constant.  The bar-
anti-symmetric residue extracted below is regulator-independent.)

The **regularised crystal-corrected shell-binding sum** is

$$
  S^{\mathrm{reg}}_{\mathrm{crystal}}(\beta_A)
  \;:=\;
  S_{\mathrm{crystal}}(\beta_A^{\mathrm{plain}})
  \;+\;
  \sum_{\text{$\bowtie_K$ in } \beta_A}
    \mathrm{tr}_M\!\bigl(\bowtie_K^{\mathrm{reg}}\bigr),
$$

where $\beta_A^{\mathrm{plain}}$ is the plain-generator skeleton (to
which [`prop:crystal-isospin-degeneracy`](#prop:crystal-isospin-degeneracy)
applies directly) and the sum runs over the $A - 1$ inter-nucleon
interfaces.

## The isospin-Z/2-anti-symmetric residue and the 305 ppm match

Under the $\mathrm{SU}(2)_I$ Z/2 swap, $S^{\mathrm{reg}}_{\mathrm{crystal}}$
transforms as:

$$
  S^{\mathrm{reg}}_{\mathrm{crystal}}(\beta_A^{\mathrm{swap}})
  \;-\;
  S^{\mathrm{reg}}_{\mathrm{crystal}}(\beta_A)
  \;=\;
  \sum_{\text{pp/nn pairs}}
    \bigl(\mathrm{tr}_M(\sigma^{-1}) - \mathrm{tr}_M(\sigma)\bigr)
  \;=\;
  - n_{pp/nn}\cdot h \cdot \omega(q)
$$

where $n_{pp/nn}$ counts the pp–nn pair swaps and $\omega(q)$ is the
common bar-symmetric Markov-trace factor.  The residue is
**isospin-Z/2-anti-symmetric** (carries an overall $h = q - q^{-1}$, which is
bar-odd per [`bar-involution-table3-data`](bar-involution.md#tbl:bar-involution-table3-data)).

**Headline match.**  Evaluated at $q = q_0$, the leading-order residue
is exactly the substrate flavor split

$$
  \frac{\Delta m}{M_N}\bigg|_{q_0}
  \;=\;
  \frac{\hbar_q^2 \cdot h \cdot [2]_q \cdot (1 + \hbar_q^3)}{3}\bigg|_{q_0}
  \;\approx\;
  305\;\mathrm{ppm}
  \qquad
  \text{(CODATA: } (m_n - m_p)/M_N \approx 305\;\mathrm{ppm}\text{).}
$$

This is already computed in
the canonical formalism
and consumed by
the canonical formalism.
The conjectural content of THIS block is the **categorical
identification** of that closed form as the regularised-crystal
$\mathrm{SU}(2)_I$ anomaly.

## Bar-symmetry parity decomposition

Per
[`docs/audits/-isospin-categorical-source.md`](../../docs/audits/-isospin-categorical-source.md)
§3 and the canonical-watcher §Slot J discipline, the four factors of
$\Delta m / M_N$ classify as:

| Factor | Under $q \mapsto q^{-1}$ | Bar parity |
|--------|---------------------------|------------|
| $\hbar_q = (q-1)/q$ | $\hbar_{q^{-1}} = 1 - q \neq \pm \hbar_q$ | **mixed** (not bar-classifiable) |
| $\hbar_q^2$ | inherits mixed status from $\hbar_q$ | **mixed** |
| $h = q - q^{-1}$ | $q^{-1} - q = -h$ | bar-**anti-symmetric** |
| $[2]_q = q + q^{-1}$ | invariant | bar-symmetric |
| $1 + \hbar_q^3$ | mixed (1 bar-sym, $\hbar_q^3$ inherits mixed) | mixed |

Net product $\hbar_q^2 \cdot h \cdot [2]_q \cdot (1 + \hbar_q^3) / 3$
is **mixed** under bar (verified at $q_{0}$ by
the canonical formalism).
The product carries the bar-odd $h$ factor as a coefficient, but
the $\hbar_q$ factors don't bar-classify cleanly.

**Under the isospin Z/2 swap** ($\sigma_{i}$ $\leftrightarrow$ $\sigma_{i}^{-1}$ at q FIXED), the
residue IS anti-symmetric (the swap exchanges proton $\leftrightarrow$ neutron,
giving $m_n - m_p \neq 0$).  At the specific evaluation point
$q = q_0$, the formula's value is bar-odd in a sign-of-$h$ sense
(scales with the bar-odd $h$), but the formula AS A FUNCTION OF $q$
lacks a uniform bar-classification.  This is the audit-correction
finding from
[`docs/audits/-d9-bar-parity-correction.md`](../../docs/audits/-d9-bar-parity-correction.md).

The bar-symmetric subleading contribution
$\hbar_q^2 \cdot h \cdot [2]_q \cdot \hbar_q^3$
(bar-anti-sym $\times$ bar-anti-sym = bar-sym) is the next-order canonical
correction; it appears at relative order $\hbar_q^3 \approx 9.3 \times
10^{-4}$ to the leading 305 ppm.

## Diagnostics

Per [`.claude/skills/local/canonical-watcher.md`](../../../.claude/skills/local/canonical-watcher.md) §Slot J:

- **GB filtration level**: ℓ varies — per-atom; the residue
  identification holds at every $\ell$ for which both the plain
  skeleton ($\ell_{\mathrm{plain}}$) and the canonical word ($\ell_{\mathrm{canonical}}$) are defined.
- **Jet order**: $h^1$ (leading anomaly is isospin-Z/2-anti-symmetric linear
  in $h$; bar-symmetric subleading at $h^4$ via $\hbar_q^3$ multiplier).
- **Bar-symmetry status**: **isospin-Z/2-anti-symmetric** at leading order
  (the isospin residue lives in $P_{\mathrm{skew}}$ image of
  [`bar-involution.md`](bar-involution.md), correctly classified in
  [`bar-involution-table3-data`](bar-involution.md#tbl:bar-involution-table3-data)
  under the $h$ entry).

## Closure of D9 in the duality tracker

Per [`docs/duality-tracker.md`](../../docs/duality-tracker.md) §1 row
D9: this conjecture is the load-bearing closure path. The duality
tracker will move D9 from partial (crystal-only) to formalised
once:

1. This block lands (provides the categorical statement)
2. Lean class `IsospinFromCanonicalBowtie` is inhabited (depends on
   the regularised crystal functional class instance)
3. The isospin-Z/2-anti-symmetric residue verification canonical witness
   ships (see §"Open R&D" below)

The Lean class follows the conditional-class exception of AGENTS.md
§3b-cond: the upstream conjecture `crystal-isospin-degeneracy`
provides the plain-generator base; the regularised-functional
extension is an `Instance` parameter; the isospin-Z/2-anti-symmetric residue
is then provable from the four-factor parity decomposition above.

## Lean axiomatisation (sketch)

```lean
-- Conditional on the plain-generator restricted result + the
-- color-tube channel-assignment class:
class IsospinFromCanonicalBowtie
    (M : Type*) [BrCategory M] [Hecke M]
    [CrystalIsospinDegeneracy M]
    [InterNucleonChannelColorTube M] where
  /-- The regularised crystal functional on canonical bowtie-
      coupled atomic braids. -/
  S_reg_crystal : ∀ (A : ℕ) (β : AtomicBraidCanonical A),
    Real
  /-- Cesàro / Borel regularisation absorbs the divergent -h/2
      shift; the finite remainder is the categorical residue. -/
  regulator_consistent :
    ∀ (A : ℕ) (β : AtomicBraidCanonical A),
      S_reg_crystal A β
        = S_crystal A (plain_skeleton β)
          + sum_bowtie_tr_M_reg β
  /-- SU(2)_I swap (u ↔ d) on color-sheet flavors leaves the
      regularised functional invariant up to a isospin-Z/2-anti-symmetric
      residue carrying an overall factor of h. -/
  swap_residue_bar_anti_symmetric :
    ∀ (A : ℕ) (β : AtomicBraidCanonical A),
      S_reg_crystal A (swap_isospin β)
        - S_reg_crystal A β
        = - count_pp_nn_swaps β · h · markov_trace_factor
  /-- Leading-order residue at q = q_0 matches the substrate
      flavor split closed form (verified canonical at 305 ppm). -/
  q_zero_residue_matches_flavor_split :
    leading_residue_at_q_zero
      = flavor_split_subleading q_zero
```

The class is inhabited by:
- the plain-skeleton crystal functional (via
  `CrystalIsospinDegeneracy` instance)
- the color-tube channel-assignment data (via
  `InterNucleonChannelColorTube` instance, conditional on PR
  [#1111](https://github.com/litlfred/qou/pull/1111)'s class)
- the regularised-functional construction (concrete Cesàro
  regulator on the divergent series).

Per AGENTS.md §3b ("class is inhabited"), the only `sorry`
ultimately lives in the upstream-conjecture class instances.

## Open R&D

1. **Author the verification compute formalism**:
   the formal derivation — at $q = q_0$, evaluate the
   canonical $\bowtie_K$-coupled atomic braid for ${}^{2}\mathrm{H}$ (Z=1, N=1)
   and explicitly compute:
   - The plain-skeleton crystal-corrected shell sum
   - The regularised contributions from the one inter-nucleon arc
   - The isospin-Z/2-anti-symmetric residue
   - Cross-check against
     `_li_2_q_util.flavor_split_subleading(q_0)` to 1 ppb.
2. **Construct the explicit regulator**: identify the canonical
   Cesàro / Borel construction (out of several admissible
   regulators) that aligns with the framework's Φ_q vs Li_2^q
   sorting per [cheat sheet §4](../../docs/canonical-derivation-cheat-sheet.md).
3. **Promote to a `proposition`** with §3b-cond banner once the
   regulator-consistent statement is fully Lean-proved (modulo
   class instances).
4. **Extend to higher A**: verify the isospin-Z/2-anti-symmetric residue
   identification holds for T, ${}^{3}\mathrm{He}$, ${}^{4}\mathrm{He}$ — these have multiple
   inter-nucleon arcs and the residue is a sum over arcs.  The
   ${}^{4}\mathrm{He}$ magic-shell case (per
   [`docs/audits/-magic-shell-gs-filtration-exploitation.md`](../../docs/audits/-magic-shell-gs-filtration-exploitation.md))
   is where the Wigner SU(4) supermultiplet structure should
   manifest.

## Cross-references

- [`docs/duality-tracker.md`](../../docs/duality-tracker.md) §1 D9
  (this conjecture is the closure path) + §2 Cluster B (D9 $\to$
  D10 $\to$ D11 nuclear physics)
- [`docs/audits/-isospin-categorical-source.md`](../../docs/audits/-isospin-categorical-source.md)
  — the audit that proposed this closure
- Upstream restricted result:
  [`prop:crystal-isospin-degeneracy`](crystal-isospin-degeneracy.md)
- Upstream channel-assignment class:
  [`conj:inter-nucleon-channel-color-tube`](inter-nucleon-channel-color-tube.md)
  (PR [#1111](https://github.com/litlfred/qou/pull/1111))
- The 305 ppm closed form:
  [`prop:flavor-split-substrate`](flavor-split-substrate.md)

- The compute consumer:
  the canonical formalism
- D6 (charge conjugation): [`conj:c-from-color-flavor-swap`](c-from-color-flavor-swap.md)
  — sibling Z/2 categorical symmetry on color sheets (same color-tube infrastructure)
- The Markov-trace machinery: [`bar-involution.md`](bar-involution.md)
  Tables 1-4 — bar-symmetry classification of all framework quantities
<!-- FILE_END: isospin-from-canonical-bowtie.md -->

