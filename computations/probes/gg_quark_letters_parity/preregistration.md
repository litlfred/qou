# Does the γγ construction fix each quark letter's through-strand parity? Pre-registration

Written and committed **before any number in this directory was computed**. Issue #7777. Beans `qou-ales`, `qou-99qc`, `qou-y2np`. Step 3 of owner option 4 (ruling 2026-10-12, PR #7718): the quark sign map and the letter placement must be **outputs** of the γγ (pair-production) construction plus reading 3 at every strand count, never picked by hand. Owner instruction relayed 2026-10-13: derive each produced line's through-strand parity from γγ **and the Jones-pair closure**; if the parity is undetermined, record it as a gap.

Nothing here is adopted, ranked, or chosen. No rule is ranked or selected by its reading-3 verdict or by any number. Nothing is compared with Q_β, CODATA, AME or any mass.

## 0. Inputs (all on `main`)

- **Step 2 (#7779):** in the Jones (Temperley–Lieb) basis {1, e₀, e₁, e₀e₁, e₁e₀} of TL₃ = H₃/(1³), e_i = (q − σ_i)/[2]_q, every template letter on generator g is L = c·1 − [2]_q·e_g. The cap–cup coefficient is flavour-blind; flavour is the through coefficient c: σ ↦ q, σ⁻¹ ↦ q⁻¹, averaged ud letter ↦ [2]_q/2. V = σ₀σ₁⁻¹ = 1 − [2]q⁻¹e₀ − [2]q·e₁ + [2]²e₀e₁.
- **Step 1 (#7760):** V³ = 1 + h²(T_{s₀s₁} − T_{s₁s₀}) + h³(σ₁ − σ₀) + O(h⁴); the first single letters are −σ₀, +σ₁ at h³.
- **#7718:** nucleon element V³·L₀₁·L₀₂·L₁₂ (pairs (0,1),(0,2),(1,2) on generators given by the placement; builder placement 001); 8 templates; exact χ's in `computations/probes/quark_template/results.json`.
- **#7733:** top, bottom and Jones-pair closures; the pair closure evaluates a crossing on the annihilated singlet pair at its e-eigenvalue (σ ↦ −q⁻¹, σ⁻¹ ↦ −q).

## 1. Corpus-grep result (done before writing this)

Searched beans `qou-ales`, `qou-99qc`, `qou-y2np` (full bodies), and `docs/audits/`, `folio/`, `computations/`, `beans/defs/`, `library/INDEX.md` for "through-strand", "through coefficient", "quark letter", "Jones pair", "γγ / gamma-gamma". **No artifact fixes a rule mapping a quark flavour, or a quark-pair letter, to a through parity.** What exists: the γγ vertex parity pattern (letters come in (positive, negative) pairs, `gammaGamma_snd_neg`, which selects the interleaved core); `−h/2` is the unique bar-fixed shift (`qbeta_quark_block_is_the_bar_fixed_letters_probe.py`); a bar-odd constraint on Δ (`qbeta_bar_parity_forces_a_unique_quark_letter_probe.py`), which is about the p − n difference, not a γγ rule. The builder's u = σ, d = σ⁻¹ is the template under question, not a derivation.

## 2. The output space

A rule's output for a nucleon N ∈ {p, n} is, for each of the three pair letters j ∈ {(0,1), (0,2), (1,2)}: a generator g_j ∈ {0, 1} (the **placement**) and a through coefficient c_j (the **parity**: q, q⁻¹, the bar-fixed [2]/2, or "other"). A rule may output a value, a family it does not choose within, or "cannot".

For each output we also report whether it is **template-expressible**, i.e. equal for both nucleons to some #7718 template (sign map S±, S0, S1 with pair rule AVG/LO/HI) at some placement, and if so which.

## 3. Candidate construction rules (fixed now; all reported side by side)

- **R1 — vertex inheritance.** A letter on generator g inherits the through parity of the crossing the γγ vertex V = σ₀σ₁⁻¹ places on g: g = 0 ↦ σ₀ (c = q), g = 1 ↦ σ₁⁻¹ (c = q⁻¹). Placement: R1 says nothing; it outputs the 8-placement family without choosing.
- **R2 — h-leading residue of the core.** The letter on g is the core's first single-letter residue on g, read with the sign of its coefficient as the crossing's orientation: coefficient −1 on σ₀ ↦ σ₀⁻¹ (c = q⁻¹), +1 on σ₁ ↦ σ₁ (c = q). (Reading a coefficient sign as an orientation is an interpretive step, stated here as part of the rule.) Placement: not fixed; 8-placement family.
- **R3 — Jones-pair closure (survivor rule).** Annihilate one pair of a γγ word W as a singlet with the Jones projection and read the through coefficient of the line left on the other generator. Concretely, in TL₃, W·e₁ ∈ span{e₁, e₀e₁} and e₁·W ∈ span{e₁, e₁e₀}, so W·e₁ = (a + b e₀)e₁ and e₁W = e₁(a′ + b′e₀); writing a + b e₀ = α(c − [2]e₀) gives the survivor's through coefficient **c = −[2]a/b** on generator 0. Likewise e₀ on either side leaves a survivor on generator 1. Four closures per word (annihilated pair 0 or 1 × right or left). Computed for **R3a: W = V** (one vertex) and **R3b: W = V³** (the confined core). A closure fixes a parity on the surviving generator only if c ∈ {q, q⁻¹}; c = [2]/2 is the bar-fixed letter; anything else is "no letter parity". Placement: not fixed by R3. If the four closures of one word give different parities for the same generator, R3 is ambiguous for that word, and it is reported as such.
- **R4 — pair-production balance.** Each quark-pair letter is itself a produced pair, and a γγ vertex produces one line of each through parity, so each pair letter is the balanced (bar-fixed) letter (σ + σ⁻¹)/2, c = [2]/2. Placement: not fixed; 8-placement family.
- **R5 — flavour dictionary.** A rule must map *flavours* (u, d) to lines. The only γγ datum distinguishing two produced lines is their parity (one q, one q⁻¹), and the two dictionaries u ↔ q and u ↔ q⁻¹ are exchanged by the bar involution. R5 asks whether anything in the construction (V, V³, the closures) is invariant under neither exchange in a way that names a flavour. **Stated now:** R1–R4 take only the vertex, the core and a generator as input, never the quark content, so each gives the proton and neutron the same element. Whether that is so is checked (P1 below), not assumed.

## 4. Checks (pass/fail fixed in advance)

- **P0.** Reproduce step 2: the TL coefficients of V and V³ equal the strings in `gg_quark_letters_tl/gg-quark-letters-tl.witness.json` exactly (difference simplifies to 0).
- **P1.** Reproduce #7718: for the 8 templates at the builder placement, χ_(3) and χ_(2,1) equal `quark_template/results.json` `primary_k0` exactly; and for S+AVG the reading-3 verdict at q₀ for all 8 placements equals `tertiary_joint_k0` (proton and neutron, 4/8 each).
- **P2.** Hand-derived identities for the pair closure, fixed now: V·e₁ = −q·σ₀·e₁ and e₀·V = −q⁻¹·e₀·σ₁⁻¹ (so R3a's adjacent closures give c = q on generator 0 and c = q⁻¹ on generator 1). Exact equality required.
- **P3.** Ideal sanity: for W ∈ {V, V³}, W·e₁ has zero coefficients on 1, e₀, e₁e₀; e₁·W on 1, e₀, e₀e₁; and the mirrored statements for e₀.

If a check fails, it is reported as failed and its rows are not interpreted.

## 5. Reported for every rule

The output (placement family, parity per generator, p vs n equal or not, template-expressible or not); then, for every element in the rule's output family, χ_(3) and χ_(2,1) exactly, their sign on all of (1, ∞) (Sturm counts on numerator and denominator), and their value at the proton pin q₀ (`qou_substrate.constants.Q_50_DIGIT_STR`, mpmath 60 dps, display only). Under convention D the y > 0 blocks at n = 3 are (3) and (2,1); every element here lives in H₃, so "every strand count m = 3..n" is the single level m = 3. Reading 3 holds iff both characters are ≥ 0. No rule is extended to more strands here.

## 6. Outcomes (stated in advance)

- **(i)** Some rule forces a unique sign map **and** placement, and the result passes reading 3 at every level for both nucleons.
- **(ii)** Some rule forces a unique sign map and placement, and it fails reading 3.
- **(iii)** Rules that each fix a parity disagree with one another.
- **(iv)** No rule fixes the flavour parity (sign map).

These are not exclusive across sub-questions: a rule may fix a **generator** parity while fixing no **flavour** sign map. The report separates the two. Expected structurally, and to be confirmed by P1/R5: no rule here can reach (i) or (ii) for the flavour sign map, because none of them reads the quark content. That would make the flavour question outcome (iv), and the gap that remains is a flavour-to-line dictionary, which this step records and does not fill.

## 7. Not done

No strand counts above 3, no gluon pair, no second nucleon, no comparison with data. Exact arithmetic over ℚ(q) (sympy); no float in any verdict.
