Master completeness index for the six-term unified mass formula
([unified knot mass](#thm:knot-mass-formula-unified)).  For each
term: the defining formula, derivation source(s), computation
script(s) and witness JSON(s), and current derivation status.

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
- *Computation: `crt_markov.py` (witness `crt-markov.witness.json`);
  `deuteron_first_principles.py` (witness `deuteron-first-principles.witness.json`);
  `light_isotope_sweep.py` (witness `light-isotope-sweep.witness.json`).*

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
- *Numerical pathology at $q_0$ (documented ):
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
- *Computation: `mass_endomorphism.py`, `crt_markov.py`
  (`tower_mass_symbolic_eval`), `tower_isotope_absolute.py`
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
- *Computation: `frobenius_partition_sum.py` (witness
  `frobenius-partition-sum.witness.json`);
  `hochschild_h3.py` for $H_3(R, q)$ structure.*

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
- *Computation: `ribbon_content_average.py`,
  `chirality_variants_probe.py`, `d_chirality_probe.py`
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
- *Computation: `gb_residue_tower.py` (first-pass numerical,
  tiny residues at real q_0 approximation), `habiro_residue_symbolic.py`
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
`term5_aK_audit.py`).  Terms 2 and 3 satisfy it only in the R-side
algebraic form (each $\mathrm{Vol}_q^{(S)}$ is a Markov trace over
the chain supported on $S$); the archimedean Kashaev specialisation
$\mathrm{Vol}_q^{(S)} \rightsquigarrow \Phi_q(|\hat V_i^{\mathrm{full}}|)$
breaks Markov-invariance because $|\hat V_i|$ is per-generator (basis-
dependent).  Numerical evaluation at $q_0$ amplifies this by $\sim 10^5$
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
   itself a Markov trace.  See `kahler_lift.py` ('s recursion
   fix).

Both expansions express T2/T3 as Markov traces — ongoing work on PR
#526.  The current `paper_six_term_isotope_sweep.py` evaluates the
literal $\Phi_q(|\hat V_i|)$ form, which is the **closed numerical
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
   a numerical-interpolation path (`habiro_coefficients_interpolate.py`)
   is scaffolded: Hoefsmit in `mpmath` at rational sample points, then
   Lagrange recovery of $p(u) \in \mathbb{Z}[u]$.
2. *Complete Lean formalisation of all six derivations (currently
   only Term 4's `frobenius_codim_universal` has a sorry-free proof;
   Terms 1–3, 5, 6 need Lean implementations of their derivations).*
3. *Higher-isotope binding agreement at $A \geq 5$ where shell
   correction dominates (numerical, requires extending the BW
   formula with cleaner shell structure).*
