# Pre-registration: a derived energy scale for the Coulomb term of n − p (2026-11-22)

Written before `mn_em_scale_derivation_probe.py` exists or is run. `date -u` immediately before
writing: **2026-11-22T10:04:42Z**. Context: §40–§41 of `LITERATURE-COMPARISON.md`,
`PREREGISTRATION-em-term.md`, `PREREGISTRATION-em-scale.md`.

Fixed inputs (unchanged from §40/§41): weight model on C²⊗³, `Rc` as in `mn_em_term_probe.py`,
V = σ₀σ₁⁻¹, hol = V³, 𝒟 = (hol − 1)/q + (1 − q⁻¹)T³, K = q^{2T³}, W_p = two 0-bits, W_n = one
0-bit, S = QPair·hol with adopted charges +⅔, −⅓, α = q⁻¹/([9]_q[10]_q) (defining relation only),
owner ruling 2026-11-22 option A (ℒ ⊃ −α·S, energy ⊃ +α·S). Photon γ = 1 + φ₀σ₀ + φ₁σ₁ +
φ₀₁·σ₀σ₁⁻¹. Convention D. Proton pin `Q_50_DIGIT_STR`.

## Honesty clause, stated first

I already know the target: the lattice electromagnetic part of m_n − m_p is ≈ −1.00 MeV
(Borsanyi et al. 2015, comparison only), EM-1 is −0.358 keV and EM-2 is −0.764 MeV. Before writing
this file I also evaluated, in a scratch one-liner, the two prefactors used below
(tanh(ln q₀) = 0.1039637 and M_QCD(q₀) = 944.404 MeV, so (α/3)·M_QCD = 2.3008 MeV). The
predictions below are therefore **not blind**. Closeness of any candidate to −1 MeV carries
**reduced weight**, and no candidate is adopted for landing near it. Swapping to another scale
after seeing the numbers would be selection against the target and is not done.

## Corpus search (what was searched, and what it gave)

- `bun scripts/corpus-search.ts` (works in this container, `--limit 200`): "Coulomb" (36 seeds),
  "Breit-Wheeler" (11), "Cottingham" (14, all ingested), "fine structure" (3),
  "electromagnetic self-energy" (1, ingested). No seeds: "charge radius", "photon coefficient",
  "gamma gamma atom", "electron capture", "electromagnetic mass", "Coulomb energy nucleus".
- grep over `docs/audits/`, `folio/**/*.md`, `computations/**/*.py`, `beans/defs/` (mounted, 5875
  beans) and `library/INDEX.md` for: self-energy, charge radius, Bohr radius, Rydberg, φ₀₁/phi01,
  electron capture, Cottingham, "EM self", electromagnetic part/contribution.
- Read in full or in the relevant part: bean `qou-bn8e` (intra-nucleon EM self-energy, the gap
  itself, in-progress), `def:coulomb-charge`, `prop:crossing-energy-decomposition`,
  `prop:coulomb-strong-ratio-q-rational`, `prop:skein-crossing-asymmetry`,
  `def:breit-wheeler-pair-production` + its derivation and observation blocks,
  `docs/audits/2026-11-21-magic-shells-gamma-gamma-model.md`, `GammaGammaAtom.lean` declarations,
  `docs/audits/2026-11-20-two-term-qed-derivation.md` §4–§6,
  `QEDHigherOrderCovariance.lean` (`scalar_insertion_shift`, `degreeZero_values`),
  `computations/canonical_mass.py` header, `m_p_substrate_identity_50dps.py::trM_borromean/F_Bor`.

**Considered and excluded (not derived):**

- **Breit–Wheeler threshold** E₀(φ) = 2m_e/(net(e⁺) − S·h): depends on the photon weights φ, and the
  derivation block states the weights "are fits" to the 2m_e threshold. Selection, excluded.
- **γγ atom** (`GammaGammaAtom.lean`, magic-shells audit): φ is kept as a free variable ("φ is
  **not derived**"); the construction carries no energy unit. Excluded.
- **Photon coefficient φ₀₁**: no corpus value. Excluded.
- **Pion Compton length** λ̄_π as the Coulomb length (bean `qou-bn8e`, first entry): the
  identification is r₀ = 1.2 fm matched to λ̄_π through an empirical rescale factor, for the
  **nuclear** Coulomb term; the bean itself records its intra-nucleon use as −0.339 MeV, 2.9× off.
  A numerical match transported to a different object; excluded as not derived.
- **E₀ = m_e/(q(q−1))**: already recorded as a selection (`PREREGISTRATION-em-scale.md`). Excluded.

## The three candidates

### C1 — the crossing-energy Coulomb channel (word level)

Chain: `def:crossing-energy` 𝔈_cross = n₊q − n₋q⁻¹; `def:coulomb-charge` splits it into the
symmetric (strong) part ½(n₊ − n₋)(q + q⁻¹) and the antisymmetric (Coulomb) part
½(n₊ + n₋)(q − q⁻¹). The corpus calls the second the electromagnetic correction (and flags that the
identification with electric charge is not established). Both nucleons carry the same word
V³ = (σ₀σ₁⁻¹)³, so n₊ = n₋ = 3 for each.

Prediction (exact, all q): Coulomb channel = 3h for both, **ΔC1 = 0**. The channel cannot see the
p/n weight-block label. No energy unit is needed for a zero. This is a structural negative for the
word-level channel, expected in advance.

### C2 — the theorem-backed Coulomb/strong ratio times the live strong arm

Chain: `prop:coulomb-strong-ratio-q-rational` (h/[2]_q = tanh(ln q) = (q² − 1)/(q² + 1), a theorem)
and bean `qou-m3vl` via `qou-bn8e` ("the only derived EM mechanism is tanh(ln q₀) × strong bond").
Strong arm: the live 𝒟² arm M1 of §35/§40, E_M1 = 2m_μ([3]_q!/q³)(τ_n − τ_p)(𝒟²),
m_μ = m_e·Vol(4₁)/ℏ_q². Candidate: E_C2 = tanh(ln q)·E_M1.

What is derived and what is not: the ratio is a theorem; the corpus states the mechanism for an
**inter**-nucleon bond, and transporting it to the n − p difference of the strong arm is my
choice. C2 also uses no quark charge. It is a weak candidate and is labelled so.

Predictions: E_C2(q₀) ≈ 0.10396 × 0.171 MeV ≈ **+0.018 MeV** (neutron heavier, the opposite of
the QED sign). As q → 1, E_M1/(m_e Vol(4₁)) = −(9/4)ε + O(ε²) and tanh(ln q) = ε + O(ε²), so
**E_C2 → 0 like −(9/4)·m_e·Vol(4₁)·ε²**.

### C3 — α·S as a degree-0 insertion on the canonical nucleon functional

Chain: `QEDHigherOrderCovariance.scalar_insertion_shift` (sorry-free, `ring`): a scalar insertion
(1 + a) on the F_Bor term of m_p = 2m_μ·T·[3]_q!/q³ − 12m_e shifts the mass by exactly
a·M_QCD, M_QCD = 2m_μ|tr_M(β_Bor)|[3]_q!/q³. The two-term QED audit §4 states it in words: "No
separate electromagnetic scale appears anywhere in the functional: the only thing that multiplies
the QED trace is the QCD term itself." |tr_M(β_Bor)| = (4 + h² − 3h⁴ − h⁶)/(h² + 4)
(`BorromeanMarkovTrace.lean`, convention D). The `−12m_e` term is recorded as a fit; it is
additive and does not enter M_QCD.

The insertion: inserting (1 + α·QPair) into the weight-model trace of the nucleon holonomy gives
tr_W(K(1 + αQPair)hol) = tr_W(K hol) + α·tr_W(K S), so the relative insertion is
a_W = α·tr_W(K S)/tr_W(K hol). Candidate:

    E_C3 = M_QCD · (a_n − a_p).

Choices stated: the same M_QCD multiplies both nucleons (both carry V³ in this model; the corpus
builds m_n differently, as m_p + Q_β + m_e). The per-block relative insertion is used, because
that is what "(1 + a) on the trace" means for a nucleon living in its block. The convention-D
sector-share normalisation (τ, dividing by [2]³ instead of tr_W(K hol)) is reported as a labelled
diagnostic; it equals EM-2 × |tr_M(β_Bor)|.

Predictions: at q = 1, hol = 1, so a_p = 0, a_n = −α/3. At q₀,
E_C3 ≈ −(α/3)·M_QCD·(1 + O(h)) ≈ **−2.3 MeV**, magnitude predicted within [1.5, 3.5] MeV, sign
**negative** (proton heavier, the QED sign, imported through option A). As q → 1, M_QCD diverges
through m_μ: **ℏ_q²·E_C3/(m_e·Vol(4₁)) → 2·1·6·(1/90)·(−1/3) = −2/45**. The divergence is that of
the canonical nucleon mass itself, so E_C3/M_QCD stays finite (→ −1/270).

## What would count

- A candidate is reported as **derived** only if every link in its chain is a corpus theorem,
  definition or ruling. C1 meets that and gives zero. C2 does not (the transport is mine). C3's
  multiplier is corpus-stated and Lean-backed; its insertion normalisation and the use of the
  proton functional for the neutron are stated choices.
- No candidate is adopted. If C3 lands near −1 MeV or −2.3 MeV, that is recorded with the reduced
  weight above. Scope (a) throughout.

Comparison printed after only: lattice QED part ≈ −1.00 MeV (BMW 2015), CODATA
m_n − m_p = 1.29333 MeV, EM-1 −0.358 keV, EM-2 −0.764 MeV.
