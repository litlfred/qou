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

*Status: **DERIVED**.*

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

*Status: **DERIVED**.*

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
  (universal theorem); specialisation to $H_3(q)$ gives
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
  `hochschild_h3.py` for $H_3(q)$ structure.*

---

### Term 5: chirality factor $a_K \cdot \mathcal{C}_K$

*Status: **PARTIAL** — structural form derived, coefficient
requires quantum-group ribbon machinery.*

- *Source: [figure-eight BW coefficients](#prop:figure-eight-bw-coefficients)
  (paper's derivation for amphichiral $4_1$ via Fricke identity
  gives $a_{4_1} = 1 - h^2$);
  [chirality Frobenius self-pairing](#prop:chirality-from-frobenius-self-pairing)
  (categorical framing as $\tau(\beta \beta^*)$);
  [chirality writhe-ribbon](#prop:chirality-writhe-ribbon-derivation)
  (writhe linearisation form, coefficient fails).*
- *Derived: **amphichiral form** $a_K = 1 - c_K h^2$ via paper's
  Fricke-identity proof.*
- *Open: **chiral coefficient** $a_K = 1 + w \cdot (\text{coeff}) \cdot h$;
  the coefficient requires quantum-group ribbon / $U_q(\mathfrak{sl}_2)$
  machinery beyond Markov trace (all 8 writhe-ribbon variants
  tested empirically fail to reproduce $1 + h$ for $D$).*
- *Empirical observation (not derived): the pattern
  $a_D = 1 + h$, $a_T = 1 - h^2$, $a_{^4\mathrm{He}} = (1 - h^2)^2$
  factorises as product $\prod_{pn} (1 \pm h)$ over pn crossings
  — matches for all three isotopes but categorical derivation
  is open.*
- *Computation: `ribbon_content_average.py`,
  `chirality_variants_probe.py`, `d_chirality_probe.py`
  (all confirm paper's coefficient is empirical / not
  Hecke-trace-derivable in the forms tested).*

---

### Term 6: higher-stratum residues $\sum_{\ell \geq 2} \mathrm{Res}_{\zeta_\ell}$

*Status: **DERIVED** (Mittag-Leffler structure); prefix-product
conjecture (earlier framing) is now **superseded**.*

- *Source: [GB residue spectral sum](#prop:gb-residue-spectral-sum)
  gives Mittag-Leffler identity; reclassified in
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

| term | derivation source(s) | computation script | status |
|---|---|---|---|
| 1 | categorical-mass-markov, Jones-Markov | crt_markov.py, light_isotope_sweep.py | DERIVED ✓ |
| 2 | mass-endomorphism-tower, three-parameters-wedderburn, Habiro | tower formulas + Wedderburn | DERIVED ✓ |
| 3 | mass-endomorphism-tower, Markov factorisation | same as Term 2 | DERIVED ✓ |
| 4 | Frobenius co-Casimir (Lean-proved) | frobenius_partition_sum.py | DERIVED ✓ |
| 5 | figure-eight BW + chirality writhe-ribbon | ribbon_content_average.py, chirality_variants_probe.py | PARTIAL (coefficient open) |
| 6 | GB residue spectral sum, Habiro | gb_residue_tower.py, habiro_residue_symbolic.py | DERIVED ✓ |

**Master conclusion.**
*Five of six terms are algebraically derived using paper's existing
machinery (Wedderburn weights, Frobenius co-Casimir, Hecke mass
trace, Habiro/colored-Jones, GB residue spectral sum).  Term 5's
amphichiral case is derived; its chiral coefficient is the one
remaining open item, requiring quantum-group ribbon structure
beyond Hecke/Markov.*

*All computation scripts are present; most with witness JSON files
in `folio-assistant/computations/`.  The paper side is **complete
up to Term 5's chiral coefficient**.*

**Outstanding items.**

1. *Rigorous derivation of $a_D = 1 + h$ from quantum-group ribbon
   or from the multiplicative $(1 \pm h)$ per-pn-crossing observation.*
2. *Verification of Habiro cyclotomic expansion coefficients $a_m(K)$
   for specific atomic braids.*
3. *Complete Lean formalisation (currently only Term 4 has a working
   proof; other Lean stubs have axiomatized `opaque` definitions).*
