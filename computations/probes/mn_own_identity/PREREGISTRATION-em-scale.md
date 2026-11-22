# Pre-registration: does the corpus fix the energy scale of the matter-Coulomb term? (2026-11-22)

Written before `mn_em_scale_probe.py` exists or is run. Context: §40 of `LITERATURE-COMPARISON.md`
and `PREREGISTRATION-em-term.md`. Completion time of this file: **2026-11-22T09:21Z** (UTC,
`date -u` taken immediately before writing; the probe file is created after this one).

## Order of events, stated because it lowers the weight of any agreement

The corpus search below was done **after** seeing that EM-1 (α·S on the electron map) gives
−0.358 keV at q₀, about 3000× short of the lattice electromagnetic part (−1.00 MeV). The search
was motivated by that gap. Any scale it turned up that lands near −1 MeV would therefore carry
reduced weight, and a scale chosen because it lands there is forbidden (AGENTS.md "NO FITTING":
selection against the target).

Also stated: while reading the corpus I saw, before writing this file,
(a) that E₀·ħ_q = m_e/q² (one line of algebra from E₀ = m_e/(q(q−1)), ħ_q = 1 − q⁻¹), and
(b) that `docs/audits/2026-11-18-two-term-qed-downstream-and-211ppb-audit.md` line 77 already
records E₀·(1/3)·Δtr((Q₁₂+Q₂₃)V³) = −0.926 MeV. So the number an "E₀ scale" reading would give
is already known to me. It is not a blind prediction, and it is not computed again here.

## What qualifies

Only a scale that the corpus states **for this term** — the Reeb-contracted matter coupling
(1 − q⁻¹)·τ(costate ≫ state ≫ reeb), i.e. the charge-insertion (Coulomb) term of
`CategoricalLagrangian` — with a Lean declaration or a content block that says so. A scale that
exists in the corpus but is not stated to be the unit of this term does not qualify. A scale the
corpus itself records as compared against targets does not qualify.

## Corpus search (surfaces read, and what each says)

1. **`CategoricalLagrangianTwoTermBridge.lean`** (Gap 5).
   - `hadronicScale (m_e q) := m_e / (q * (q − 1))` is a `def`.
   - `hadronicScale_mul_q_sq_hbar_eq_me`: E₀·(q²·(1 − q⁻¹)) = m_e, proof `unfold; field_simp`.
   - `hadronicScale_strong_to_matter_ratio`: (E₀·(1 − q⁻¹))/(1 − q⁻¹)² = m_e/(q − 1)², proof
     `unfold; field_simp`.
   Both are identities in free variables m_e and q. They hold for any m_e, so they relate E₀ to
   m_e and to the ħ_q prefactors, but **neither states that E₀ (or E₀·ħ_q) is the energy unit
   of the matter Reeb term.** No theorem in the file multiplies a trace by `hadronicScale`.
   The twin `NucleonWeightSpaceTwoTerm.hadronicScaleE0_mul_hbar_eq_me` (line 685) is the same
   identity.
2. **`observations/neutron-proton-mass-splitting.ts`** (`prop:neutron-proton-mass-splitting`),
   authorNotes:
   - 2026-11-15 caveat: *"The scale step (H_α) is not derived (owner ruling 2026-11-15: state it
     as a named hypothesis)."*
   - 2026-11-18 status: the two-term files *"formalize two-term charge-insertion algebra … The
     mass scale and the adjacent-pair restriction are choices."*
   - 2026-11-19 caveat: *"The scale (m_e, E_0, α_bind) and the four weightings were compared
     against targets. Measured in bean qou-99qc."*
   - 2026-11-20 note: *"E_0 = m_e/(q(q−1)) (a definition; `hadronicScale_mul_q_sq_hbar_eq_me`
     unfolds it)."*
3. **`docs/audits/2026-11-18-two-term-qed-downstream-and-211ppb-audit.md`**, correction box
   (lines 10–15): *"The scale and weighting were picked against targets. m_e, E_0 and α_bind,
   under four weightings, were compared … `hadronicScale_mul_q_sq_hbar_eq_me` unfolds a
   definition and does not derive a scale."* The −0.926 MeV "at E₀" figure in that audit is thus
   already on record as a selection.
4. **`docs/audits/2026-11-20-qbeta-epsilon-is-ruled-not-derived.md`** line 21: E₀ as the
   MeV-per-unit-trace scale is **posited**, *"the derivation of its series is still open."*
5. **`docs/audits/2026-11-16-bridge-b-np-mass-scale-exclusions.md`** §2: the three q-dressings
   c_q², 1/ħ_q², q⁻²/ħ_q (= E₀/m_e) are *"underived"*; the proposal that they are 𝒟² weight
   ratios is refuted there.
6. **`docs/audits/2026-11-15-np-splitting-error-budget.md`** line 254: E₀ is used linearly on
   trace differences (Q_β), and no block derives a scale for the n − p use.

Surfaces **not** searched, so this is a negative over the surfaces above, not over the corpus:
the beans mount (`beans/defs/` is absent in this container, so bean `qou-99qc` itself was not
read; its conclusion is quoted from the two artifacts that cite it), the knowledge-graph search
(`scripts/corpus-search.ts` fails here: the platform module `cat-harness-tools/src/tools/graph.ts`
is missing), and `library/`.

## Result of the search, recorded before any computation

**The corpus does not fix the energy scale of the matter-Coulomb term.** It states the opposite
explicitly: the scale step is a named, underived hypothesis (H_α), and E₀ in particular is a
definition whose use as this term's unit was compared against targets (2026-11-19). The Gap-5
lemmas are field identities that hold for any value of m_e; they cannot single out a unit.

This is a **scope (a) negative**: the corpus, over the surfaces listed, supplies no scale for
this term. It is not an exclusion of an EM term or of E₀; it says only that adopting E₀ (or any
other scale) here would be a choice, and one the corpus has already marked as a selection.

## What the probe does (and only this)

Per the instruction "if the corpus does not fix it, compute nothing beyond what the
pre-registration says", `mn_em_scale_probe.py` does exactly two things and evaluates **no**
n − p energy:

- **S1.** Symbolically (sympy, free symbols m_e, q) confirm that both Gap-5 statements reduce to
  0 = 0 for arbitrary m_e and q (predicted: both hold identically). This checks the claim that
  they carry no information about which term rides which scale.
- **S2.** Record, from the Lean source text, that no declaration in
  `CategoricalLagrangianTwoTermBridge.lean` or `NucleonWeightSpaceTwoTerm.lean` applies
  `hadronicScale`/`hadronicScaleE0` to a trace (predicted: the only occurrences are the `def`
  and the two identities, plus docstrings).

No evaluation at q₀, no MeV number, no comparison with −1.00 MeV. The comparison values are
listed only so the reader sees what is *not* being compared: lattice QED part ≈ −1.00 MeV
(BMW 2015), CODATA m_n − m_p = 1.29333 MeV.
