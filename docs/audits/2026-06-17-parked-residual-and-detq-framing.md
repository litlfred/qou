# Two parked questions — proton intra-Borromean 47% residual + det_q = framing-anomaly Lean feasibility

**Date:** 2026-06-17
**Scope:** READ-ONLY investigation. No compute/content/Lean edited. Numbers reproduced
from a live run of `entanglement_emitted_energy.py` + corpus-grep of the existing record.

---

## Q1 — what the proton intra-Borromean 47% residual IS

### The decomposition (reproduced, raw)

`computations/entanglement_emitted_energy.py` (run 2026-06-17, 40 dps) gives, with
`scale = m_e·Vol(𝓑₃)/ℏ_q² = 966.05 MeV` per unit linking weight:

| reading of linking weight LW | LW at q₀ | m_p (MeV) |
|---|---:|---:|
| classical (h⁰, word count) | 2.50000 | 2415.124 |
| Family A (PROVED, terminates at h²) | 2.53278 | 2446.791 |
| via Jones (full β_Bor Markov trace, all h-orders) | 2.49425 | 2409.568 |
| exact (CODATA-anchor inverse target) | 2.45995 | 2376.436 |

- total gap (Family A − exact) = **+70.354 MeV (+2.96% of m_p)**
- captured by Jones h⁴⁺ (Family A − Jones) = **+37.223 MeV (52.9% of the gap)**
- **residual beyond Borromean Jones (Jones − exact) = +33.131 MeV (47.1% of the gap)**

> ⚠ Framing correction to the parked-question wording. The "47%" is *not* "47% beyond
> the single Jones trace as a fraction of m_p"; it is **47.1% of the +70.35 MeV gap**.
> And note `linking_weight_via_jones` (`gamma_gamma_pair_production_decomposition.py:191`)
> is the *full* H₃ β_Bor Jones trace via the bridge `5/2 + 4·(tr_M − 1)`, and at q₀ it
> lands at 2.494 — **below** exact (2.460)? No: 2.494 > 2.460 > Family-A-distance. The
> ordering is `family_a (2.533) > jones (2.494) > exact (2.460)`. Jones *overshoots
> downward past* exact only relative to Family A: it closes 52.9% of Family A's
> excess and leaves a 47.1% residual on the SAME side (Jones still 33 MeV above exact).

### Why exact < Jones < family_a (file:line answer)

- **Family A = 2.533** is `linking_weight_family_a` (`_li_2_q_util.py:172-208`):
  `(1/4)Σ_{λ⊢4} dim_q V_λ = 5/2 + (3/4)h²`. It is an **H₄ Wedderburn dimension average**
  that TERMINATES exactly at h² (all h⁴⁺ coefficients identically zero — Lean-proved).
- **Jones = 2.494** is `linking_weight_via_jones` (`gamma_gamma_pair_production_decomposition.py:191-205`)
  = `5/2 + 4·(tr_M(β_Bor) − 1)`, the H₃ Markov trace of the actual 3-strand Borromean
  braid via its Jones polynomial (`:140-188`), closed form `(4 + h² − 3h⁴ − h⁶)/(h²+4)`.
  Its h² coefficient is **exactly 0** (Lean `BorromeanMarkovTrace.lean`), and it carries
  **non-zero h⁴⁺ corrections** (h⁴ coeff ≈ 3.03). So Jones is a *different mathematical
  object* from Family A — they disagree at h² (Family A +3/4 vs Jones 0).
- **What the Jones trace MISSES**: the residual 33.1 MeV is what the CODATA-anchor needs
  that **neither** Family A's H₄ average **nor** the H₃ single-Borromean Jones trace
  supplies. The probe (`:437-448`) and the merged confirm/refute audit
  [`2026-06-01-linking-weight-residual-fix.md`](2026-06-01-linking-weight-residual-fix.md)
  establish the hard facts: switching the index set H₄→H₃ does NOT close it (the bare H₃
  trace regresses m_p to −57% to −59%), and **eight independent structural searches**
  (Family A, 32 H₄ sign-flips, Hecke levels H₂–H₇, transcendental ansätze, single-knot,
  q-locality, …) all FAILED to derive the exact 2.461 categorically. The 2.89% is the
  acknowledged **CAL-4 categorical-exactness residual**, not a wiring bug.

### Does the keystone `dd95f9bc` Habiro/Ohtsuki lead bear on this residual?

**Read in full** (`docs/audits/2026-06-16-keystone-habiro-coupling-lead-and-ck-exposition.md`
+ `docs/audits/scripts/keystone_habiro_coupling_lead.py`, exit 0). Verdict: **NO — not as a
derivation, and not even targeted at this residual.**

- The commit is, by its own STRICT critical-distance flag, an **identification + exposition
  reframing, not a derivation**: it NAMES two Habiro elements (spacetime `WRT(S³/2I)` =
  Lawrence–Zagier quantum modular form; colour = full-Hecke trace at q₀) and explicitly
  **refuses** the unfalsifiable `2I→E₈→Poincaré→…→masses` chain. The coupling stays OPEN.
- Its concrete payoff is scoped to the **Q_β c_k ladder** (reframing c_k as Ohtsuki
  invariants of one Habiro element), NOT the proton mass. Corpus-grep confirms: "Ohtsuki"
  is tied to Q_β / α_EM throughout the corpus; **no doc ties Ohtsuki/LMO/higher-loop to the
  2.89% proton VolDensity gap.**
- The *abstract* idea in the parked question — "Ohtsuki/LMO = higher-loop perturbative
  expansion of WRT, exactly 'beyond the Jones trace'" — is structurally coherent: the
  Jones trace is the leading WRT content and the Ohtsuki series is its near-q=1 perturbative
  tail. So "the 33 MeV residual is the Ohtsuki/higher-loop tail of the SAME 𝓑₃ invariant"
  is a **physically plausible hypothesis**. BUT: (a) it is currently UNFORMALIZED and
  unconnected to mass in the corpus; (b) `linking_weight_via_jones` is the *full* β_Bor
  Jones trace (all h-orders of that 3-component link), so the residual is NOT simply
  "higher h-orders of 𝓑₃ that Jones drops" — Jones already has them. The residual is
  *beyond the single-Borromean-link invariant altogether*.

### Is there an existing multi-brane candidate for the 47%?

Partially, but **refuted in its current form**. `canonical_plus_multibrane.py`,
`canonical_brane_tower.py`, `canonical_brane_tower_decomposition.py` implement
`prop:mass-endomorphism-tower`'s Σ_n brane-level corrections. Key findings already on
record:

- The archimedean `Φ_q(|V̂_i|)` tower form is **PATHOLOGICAL** (`canonical_brane_tower.py:3-6`):
  `Φ_q(0.99) ≈ 6.7e5`, amplifying p/n asymmetries by ~10⁵× (predicts T-³He ≈ −737 MeV).
  The canonical Markov-trace `Vol_q^(S)` form replaces it.
- The brane-tower / GAP-A-3 level-selection work
  (`docs/audits/2026-06-04-gap-a3-brane-tower-level-selection-scope.md`) is aimed at
  per-isotope **binding energy** B(K), not the intra-Borromean single-proton mass residual.

### Q1 VERDICT

The intra-Borromean 47.1% (≈ 33.1 MeV) residual is the **categorical-exactness gap of the
single-Borromean linking weight**: the difference between the best available categorical
LW (whether the H₄ average 2.533 or the full H₃ β_Bor Jones trace 2.494) and the
CODATA-anchor 2.461. It is the SAME open object as the long-standing **+2.89% CAL-4
VolDensity(𝓑₃) residual**, *not* a new quantity. Eight structural searches have failed to
derive it; it is NOT closable by changing the Hecke index set.

**Most likely source, ranked:**
1. **(plausible, unformalized)** Ohtsuki/Habiro higher-loop tail of the 𝓑₃ WRT invariant
   beyond its leading Jones content — coherent with the keystone reframing, but the keystone
   commit explicitly does NOT claim or compute this for mass, and "beyond Jones" here means
   beyond the *whole* link invariant, not its dropped h-orders.
2. **(refuted in current form)** multi-brane tower — implemented, but the archimedean form is
   pathological and the canonical form is targeted at binding, not this mass residual.
3. The "γγ̄ emitted-energy" reading in `entanglement_emitted_energy.py` is a *physical
   narrative* over the same arithmetic, not an independent mechanism.

**Computable with existing machinery?** The *decomposition* is already computed (above).
A genuine *closure* is NOT available with existing machinery — it would require either an
Ohtsuki-invariant compute of 𝓑₃ wired into the mass formula (does not exist; would be new
infra) or a categorical derivation of LW = 2.461 that eight prior searches did not find.
This sits under Subgoal-2 (research-grade, below the CAL-2 floor) and should NOT be
attacked with a ninth fit-based ansatz.

---

## Q2 — the det_q = framing-anomaly equality and its Lean feasibility

### There is no literal "det_q = framing anomaly" claim. Two distinct candidates:

**Candidate A (the writhe/ribbon-twist framing claim — the intended one).**
`content/quantum-observable-universe/mass-theory/chirality-writhe-ribbon-derivation.md`
+ Lean `lean/QOU/BraidKnot/ChiralityWritheRibbon.lean`. The exact claimed equality is the
**Kauffman framing formula**: the ribbon twist Θ_λ ∈ Z(H_n(q)) acts on V_λ by
`q^{2c(λ)}`, `c(λ) = Σ_{x∈λ}(col−row)` (the Jucys–Murphy content), and a framing change by
writhe w multiplies the Markov trace in each channel by `q^{2w·c(λ)}` (the **framing
anomaly / ribbon phase**). The chirality factor is the Wedderburn-weighted ratio
`a_K(β) = Σ_λ w_λ Θ_λ^{w/2} χ^λ(β) / Σ_λ w_λ χ^λ(β) = 1 + w·h·⟨c⟩_β + O(h²)`
(`.md:35-104`).

**Candidate B (the Gram-determinant ratio).**
`predicted-spectra/em-coupling-chern-simons.md:38-104` + `.lean`. Here
`κ = det G_CS^cl / det G_CS^q` is a Chern–Simons Gram-determinant ratio feeding the α_EM
correction. This is the closest thing to a literal "q-determinant = framing" object, but it
is explicitly an **OPEN, unproved, dimensionally-ambiguous conjecture** ("This identification
is not proved … Closing κ structurally is an open problem"). The Lean already axiomatizes it
as `opaque ChernSimonsGramDeterminantIdentityHolds` + `class AlphaEmGluonOctetConjecture`
(`.lean:55-80`, demoted theorem→conjecture per §3b-cond).

### Is it Lean-formalized?

- **Candidate A: YES, partially — and the framing-anomaly *eigenvalue identity itself* is
  the part to want.** `ChiralityWritheRibbon.lean` builds. It has:
  - `class RibbonTwistEigenvalue` (`:78-86`): axiomatizes `framing_eigenvalue w κ = q^{w·κ}`
    — i.e. **the det_q/framing equality is currently an AXIOM (class field), not proved**.
  - `theorem log_q_first_order` (`:119-143`): the analytic input `q^{2κ} = 1 + κ·h + R·h²`
    — **fully proved, sorry-free**, by an elementary case split (q=1 vs algebraic residual).
  - `theorem chirality_writhe_ribbon` (`:164-209`): the writhe-linearisation —
    **sorry-free**, but it discharges the existential by exhibiting `c_avg = 0` and absorbing
    everything into the O(h²) residual (i.e. it proves the *shape* `1 + w·h·c_avg + R·h²`
    trivially, not the *substantive* `c_avg = ⟨c⟩_β`). The substantive content is parked in
    the `RibbonTwistEigenvalue` axiom.
  - Note: the content-block sibling `mass-theory/chirality-writhe-ribbon-derivation.lean`
    is a `: True := trivial` shadowing stub (`:19`) pointing at the real file — a §"No
    shadowing stubs" flag, separate from this question.
- **Candidate B: NO** (opaque Prop only; conjecture by design).

### What would the *substantive* Lean statement look like — ring-identity or transcendental?

The det_q = framing-anomaly equality has **two cleanly separable tiers**:

1. **The eigenvalue identity `Θ_λ^{w/2}|_{V_λ} = q^{2w·c(λ)}`** — this is a **polynomial /
   ring identity** over the seminormal Hecke representation. `c(λ) ∈ ℤ`, `q^{2w·c} ` for
   integer exponent is `GroupWithZero`/`Field`-provable (§7c), no archimedean content. It is
   exactly the *kind* of thing the color-tube quadric identities proved by `linear_combination`
   are — provided the ribbon element's action on the Hoefsmit/seminormal basis is available.
   **This is the tractable, ring-provable core.** What is missing is the Lean construction of
   Θ_λ acting on the seminormal idempotents (Mathlib has no Hecke ribbon element; it would
   need building on the existing `IwahoriHecke` / seminormal infrastructure).
2. **The first-order expansion `q^{2c} = 1 + c·h + O(h²)`** — already proved sorry-free
   (`log_q_first_order`). The `ln q = h/2 + O(h³)` step is stated but discharged
   *algebraically* (residual absorption), avoiding transcendental `Real.log` — so even this
   stays ring-flavored. A *quantitative* O(h²) bound (vs the current existential remainder)
   WOULD need archimedean `ℝ` analysis, but the identity as stated does not.

### Q2 VERDICT

The intended claim is **Candidate A**: the Kauffman framing-anomaly eigenvalue
`Θ_λ acts as q^{2w·c(λ)}`, with the chirality factor the writhe-weighted Markov-trace ratio.

- It is **partially formalized** (`ChiralityWritheRibbon.lean` builds; the linearisation
  *shape* + the `q^{2κ}=1+κh+O(h²)` lemma are sorry-free), but the **load-bearing
  det_q/framing equality itself is an axiom** (`RibbonTwistEigenvalue.framing_formula`), and
  the substantive coefficient `⟨c⟩_β` is set to 0 in the proved theorem — so the *physics
  content* is currently un-proved.
- **Feasibility: the eigenvalue identity is a TRACTABLE ring-identity** (integer-power
  q-monomial over a `Field`/`GroupWithZero`, §7c — same flavor as the color-tube quadrics),
  **conditional on building the missing Hecke-ribbon-element-on-seminormal-basis
  infrastructure in Lean** (Mathlib lacks it). That construction — not the final identity —
  is the real cost. It is **not** open-ended/transcendental; it is "tractable but needs a
  supporting module," roughly a medium Lean lemma, not a one-liner.
- The Gram-determinant κ (Candidate B) is genuinely **open** (admitted conjecture, opaque
  Prop) and should NOT be confused with the tractable writhe-ribbon identity.

**Honest flag:** the empirically-verified part of Candidate A (the multiplicative
per-pn-crossing rule `a_K = Π(1 + sign(c)·h)` reproducing D/T/³He/⁴He) is a **conjecture
without categorical derivation** (`.md:162-250`, `PNCrossingRule` class) and 8 tested
Hecke-trace variants all miss it by >20%. So while the *framing eigenvalue* is formalizable,
the *paper's specific chirality factors* are NOT yet derived from it — that gap is real.

---

## Cross-references
- `computations/entanglement_emitted_energy.py`, `gamma_gamma_pair_production_decomposition.py`
- `computations/_li_2_q_util.py:172-377` (`linking_weight_family_a`, `vol_density_borromean`)
- [`2026-06-01-linking-weight-residual-fix.md`](2026-06-01-linking-weight-residual-fix.md) (8-search refutation; H₃ regresses)
- `docs/lambda-scale-absorbed-into-vol-density.md` (the 2.89% framing)
- [`2026-06-16-keystone-habiro-coupling-lead-and-ck-exposition.md`](2026-06-16-keystone-habiro-coupling-lead-and-ck-exposition.md) + `scripts/keystone_habiro_coupling_lead.py` (dd95f9bc)
- `content/quantum-observable-universe/lean/QOU/BraidKnot/ChiralityWritheRibbon.lean`
- `content/quantum-observable-universe/mass-theory/chirality-writhe-ribbon-derivation.md`
- `content/quantum-observable-universe/predicted-spectra/em-coupling-chern-simons.{md,lean}` (Candidate B, open)
