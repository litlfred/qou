# Can the weak vertex be a non-letter element? The one-sided flavour flip

Bean `qou-hlx7` (epic `qou-qs0e`, tracker #7735). Builds on `qou-hlx6` / draft PR #7836
(`HelicityCommonSource.lean`), whose `no_one_sided_letter` shows that a flavour flip on one
eigenline only is not a Hecke letter. This audit asks whether a **non-letter** element does
the job, whether it is canonical, and what it would do to the Q_β computation.

* Lean: `folio/quantum-observable-universe/lean/QOU/QuarkState/OneSidedWeakVertex.lean`
* Probe (prints only, writes **no** witness, dashboard untouched):
  `computations/qbeta/qbeta_one_sided_weak_vertex_probe.py`, 7/7 checks.

Nothing here is written into content, and no identification is made.

## 0. Result in four lines

1. **Yes, a non-letter one-sided flip exists, and it is the chirality grading up to a scalar.**
   With J := P₊ − P₋, the L-only flip W_L := P₊ s⁻¹ P₊ + P₋ s P₋ equals **q⁻¹·J**, and the
   R-only flip W_R := P₊ s P₊ + P₋ s⁻¹ P₋ equals **q·J**. J² = 1, J = (s + s⁻¹)/[2]_q.
2. **Forced up to a two-element choice.** Any element is fixed by its action on the two
   eigenlines (`eq_of_eigen_action`, since P₊ + P₋ = 1). So once you say *which* line, the
   vertex has no freedom. But "which line" is a genuine binary choice: {W_L, W_R}, mutually
   inverse, **exchanged by the bar involution** (which fixes J). That two-element family is
   the finding; nothing inside one letter picks L over R.
3. **The corpus nucleon word already contains J.** Its mixed `ud` crossing letter
   s − h/2 equals ([2]_q/2)·J exactly. This is an observation about the existing word, not a
   claim that the `ud` letter is a weak vertex.
4. **Q_β is very sensitive to inserting such a vertex, and in a choice-dependent way**: from
   −83 % to +273 % change in |tr| depending on L vs R and on where it goes. No placement is
   forced by anything proved, so none of these numbers is a prediction.

## 1. The proved statements (all sorry-free)

Setting: one letter s in a K-algebra A, s² = h s + 1, h = q − q⁻¹, q ≠ 0, [2] := q + q⁻¹ ≠ 0;
P₊ = (s + q⁻¹)/[2] (eigenvalue q), P₋ = (q − s)/[2] (eigenvalue −q⁻¹). Generic `[Field K]`,
`[Ring A] [Algebra K A]`, no ℝ.

| theorem | statement |
|---|---|
| `Pm_mul_Pp`, `Pm_idem`, `Pp_comm`, `Pm_comm` | the projectors are orthogonal idempotents commuting with s |
| `eq_of_eigen_action` | x P₊ = a P₊ ∧ x P₋ = b P₋ ⇒ x = a P₊ + b P₋, for **any** x ∈ A |
| `grading_sq` | J² = 1 |
| `grading_comm` | J commutes with s |
| `two_smul_grading` | [2]·J = s + s⁻¹ |
| `grading_flip` | J is bar-invariant: J(q⁻¹, s⁻¹) = J(q, s) |
| `oneSidedL_eq` | W_L = q⁻¹·J |
| `oneSidedR_eq` | W_R = q·J |
| `oneSidedL_mul_Pp/Pm`, `oneSidedR_mul_Pp/Pm` | W_L acts by (q⁻¹, −q⁻¹), W_R by (q, −q) on (P₊, P₋) |
| `oneSidedL_not_letter` | W_L is a letter at no parameter unless q² = 1 (via `no_one_sided_letter`) |
| `oneSidedL_mul_oneSidedR` | W_L·W_R = 1 |
| `oneSidedL_flip` | W_L(q⁻¹, s⁻¹) = W_R(q, s): bar exchanges L-only and R-only |
| `ud_letter_eq_grading` | s − (h/2)·1 = ([2]/2)·J (needs 2 ≠ 0) |
| `netFlavour_grading` | on 6a's formal-h NF, net flavour of σ + σ⁻¹ = [2]J is −1 = 0 + (−1) |

Answers to the brief's item 1:

* **Idempotent / involution:** J is an involution; W_L, W_R are involutions only up to the
  scalars q^{∓2} (W_L² = q⁻²). Neither is idempotent.
* **Commutation with P±:** all of J, W_L, W_R commute with P± (they are polynomials in s).
* **Action on quarkState / net flavour:** W_L and W_R are not in 6a's formal-h ring as they
  stand (they need [2]⁻¹, and [2] = √(h² + 4) is not a polynomial in h). The doubled form
  [2]J = σ + σ⁻¹ is, and its net flavour is **−1, the sum of the u and d shifts**. So a
  chirality-selective element reads, in 6a's flavour coordinate, as "u plus d", not as a
  flavour change. Composing a one-sided vertex with net flavour is therefore **not** a
  derived quantum number. Scope (a).

## 2. Item 2: canonical or a family?

**Within a single letter's algebra: forced up to one binary choice.**

* Given the prescription "invert the eigenvalue on line X, keep it on the other",
  `eq_of_eigen_action` leaves no freedom at all, in any ambient algebra (not just K[s]).
* The choice X ∈ {L, R} is real and **nothing in the letter breaks it**: the two answers are
  q⁻¹J and qJ, exchanged by the bar involution (`oneSidedL_flip`). Choosing L because the
  physical weak current is left-handed would be inserting the observation, not deriving it.
* If the prescription is relaxed to "any element commuting with P± and separating them", the
  family is all a P₊ + b P₋ with a ≠ b: two continuous parameters. The one-sided flips are
  the two points of that plane fixed by "act as s or s⁻¹ on each line".

So the honest summary is: **a two-element family {q⁻¹J, qJ}, i.e. one chirality bit, which
the bar involution swaps.** This is consistent with D-H2 = no (chirality is not a second
per-letter datum *of the letter*): the bit has to be supplied from outside the letter, which
in the 6b picture is the cone polarization point u.

Multi-letter remark (not proved here): for n ≥ 3, J_i = (σ_i + σ_i⁻¹)/[2] does **not**
commute with σ_{i±1}. So a one-sided vertex on one crossing does not commute with the rest
of the word, and its placement matters. §3 measures exactly that.

## 3. Item 3: what a one-sided vertex does to the Q_β computation

The ruled cell is Q_β = |tr^{z_D}(Δ)|·E₀, Δ = n − p, z_D = q³/(q² + 1), on the γγ-selected
word `nuc11_interleaved`. The probe rebuilds that word letter by letter with the census's own
multiplier (`hm`, letters c σ_g + d) and reproduces the scored trace
**tr = −0.1541948850472397056592555** to 1e-24 (Q_β = 0.65185631006 MeV, −16.678 %). All
numbers below are exact sympy, read out at 60 dps; no float64.

**Replace the neutron's single tail d letter σ₁⁻¹:**

| replacement | tr^{z_D}(Δ′) | Q_β′ (MeV) | |tr′|/|tr₀| − 1 |
|---|---|---|---|
| none (base) | −0.154194885047 | 0.651856 | 0 |
| σ₁ (chirality-blind d → u) | +0.083599548061 | 0.353416 | −45.78 % |
| q J₁ (L-only d → u) | +0.026459970469 | 0.111859 | −82.84 % |
| q⁻¹ J₁ (R-only d → u) | −0.097055307455 | 0.410300 | −37.06 % |

**Insert a vertex at the end of the neutron word (n → n·V):**

| V | tr^{z_D}(Δ′) | |tr′|/|tr₀| − 1 |
|---|---|---|
| J₀ | −0.295254964439 | +91.48 % |
| q⁻¹ J₀ | −0.328355533937 | +112.95 % |
| q J₀ | −0.258514041218 | +67.65 % |
| J₁ | +0.455510015037 | +195.41 % |
| q⁻¹ J₁ | +0.348022363026 | +125.70 % |
| q J₁ | +0.574819006679 | +272.79 % |

What this establishes:

* **The Markov trace is not chirality-blind.** L-only and R-only replacements differ by
  0.1235 in tr (checked). At a single letter, tr(P₊) = (z + q⁻¹)/[2] and tr(P₋) = (q − z)/[2]
  are different (at z_D, tr(P₋) = 1/[2]²). What is chirality-blind is the **word**: it
  contains no element that picks a line. The brief's "a trace that never distinguishes
  chirality" is right about the word and wrong about the trace.
* **The effect is O(1), not a correction.** Every placement moves |tr| by 37 % to 273 %.
* **Cross-check against the corpus:** the chirality-blind replacement reproduces
  Q_β = 0.353415698 MeV (−54.825 %), the "bar-odd survivor" value already recorded in
  AGENTS.md (`qbeta_bar_parity_forces_a_unique_quark_letter_probe.py`). So the probe's word
  is the corpus's word.
* **No row was re-scored and no witness was written.** The −16.678 % cell is unchanged.

What it does not establish (scope (a) throughout):

* Which placement, if any, is the weak vertex. **Choosing among the rows above by closeness
  to CODATA would be selection against the target**, the fit AGENTS.md forbids. None of them
  is proposed.
* Whether the existing `ud` letters (which are ([2]/2)·J, §1) already play this role. That
  would be an identification; it is not made.

## 4. The bar observation (observation, not a claim)

AGENTS.md calls Q_β "the bar-odd (sinh) partner" of m_π, and the bar involution is 6a's
flavour flip. Measured on the ruled cell:

* f(q) := tr^{z_D(q)}(Δ)(q). **f(q₀) = −0.154194885047, f(1/q₀) = +0.109290225931.**
  f(q₀) + f(1/q₀) = −0.0449 ≠ 0, so **the ruled Q_β trace is not bar-odd** (nor bar-even).
* The letter-level bar (σ + d(h) ↦ σ − h + d(−h), same algebra) maps u ↔ d and **fixes the
  `ud` letter** (it is ∝ J, which is bar-invariant). Traced at z_D(q) it gives exactly
  f(1/q₀) (agreement to 7e-52). So the Markov trace at z_D intertwines the bar involution with
  q ↦ q⁻¹ on this word, but Δ is not bar-anti-invariant.

Reading: the "bar-odd" label belongs to the **retired z = 1 closed form**
|q² − 2q − 1|(q + 1)/(2q³), not to the ruled z_D cell. That the bar involution is the flavour
flip, and Q_β is a flavour difference, is **consistent in spirit but not literally borne
out**: the measured trace has no definite bar parity. Treat the label as historical for the
ruled cell. This is the agent's reading; nothing is edited.

## 5. Scope of every negative

* "No single letter is a one-sided flip": **(b)**, invariant `no_one_sided_letter`.
* "The one-sided flip is not canonical in L vs R": **(b)** within one letter, invariant
  `oneSidedL_flip` + `grading_flip` (the bar involution is a symmetry of everything in the
  letter and swaps the two answers). **(a)** for the full algebra with a cone point u.
* "A one-sided vertex does not yield an integer flavour change in 6a's coordinate": **(a)**,
  measured on the doubled grading only.
* "The ruled Q_β trace is not bar-odd": a measurement at q₀, not a structural exclusion.

## 6. Verification

* Mathlib oleans restored from `cat/folio-assistant-sci/lake-cache/qou-v4-24-0` (3758 oleans,
  100 % traced) plus the gap addon (95 oleans).
* The QOU dependency chain compiled lean-direct into a scratch olean dir, each exit 0:
  `MarkovTraceOnHecke`, `HeckeH3AlgebraLaws`, `HeckeH3AlgebraInstance`, `PhotonPairNormalForm`,
  `HelicityCommonSource` (the last from draft PR #7836, which this branch is based on).
* `lean -DautoImplicit=false -s 65536 OneSidedWeakVertex.lean`: exit 0, no output, 0 `sorry`.
* `#print axioms` on 11 declarations (`eq_of_eigen_action`, `grading_sq`, `two_smul_grading`,
  `grading_flip`, `oneSidedL_eq`, `oneSidedR_eq`, `oneSidedL_not_letter`,
  `oneSidedL_mul_oneSidedR`, `oneSidedL_flip`, `ud_letter_eq_grading`, `netFlavour_grading`):
  `[propext, Classical.choice, Quot.sound]` only.
* Probe: 7/7 checks, sympy exact + mpmath 60 dps.
* `lean-library-sweep.py` not run: paper-tree Mathlib oleans are 99 here, so it would report
  UNVERIFIED on the cache, not the source.

## 7. Owner decisions

### D-W1: should the chirality bit for the weak vertex be taken from the cone point u (6b)?

* **(A) Yes, as a working hypothesis.** *Means:* a child bean that tries to derive which of
  {q⁻¹J, qJ} the cone point u selects, from the 6b polarization structure. *Costs:* Lean
  linking 6b's `PolarizationActionHecke` to this file; hours. *Risks:* u is a gauge globally
  (#7825), so it may select nothing, which would be a clean scope-(b) negative. *Commits to:*
  locating V−A outside the letter algebra.
* **(B) No.** *Means:* leave `qou-hlx7` open with this result recorded. *Costs:* none.

**Default if nothing is said: (B).** **Recommendation (judgement): (A)**, because §2 shows
the bit is not in the letter and 6b is the only place the corpus puts chirality.

### D-W2: should the "bar-odd sinh partner" description of Q_β be scoped to the retired z = 1 form?

* **(yes)** *Means:* a one-line scoping note where AGENTS.md / content call Q_β bar-odd.
  *Costs:* a small prose edit. *Risks:* none to numbers. *Commits to:* not using bar parity
  as an argument about the ruled cell.
* **(no)** *Means:* nothing changes; the label stays unscoped.

**Default: (no), nothing edited.** **Recommendation (judgement): (yes)**; f(q₀) + f(1/q₀) ≠ 0
is measured and anyone reasoning from the label about the ruled cell would be misled.

### Not a decision, a warning

No row of the §3 tables should be adopted. If anyone wants a weak-vertex insertion in the Q_β
word, the placement and the L/R bit must come from a derivation (D-W1), not from the residual.

## 8. Addendum: composing with 9a's skein difference (coordinator input)

9a's `skein_asym_eq` gives the corpus parity element q s − q⁻¹ s⁻¹ = h·[2]_q·P₊. It composes
with this file's result exactly. Both identities below are sorry-free and use standard axioms
only.

| theorem | statement |
|---|---|
| `two_smul_oneSidedL_eq_skein` | [2]·W_L = [2]·s − (q s − q⁻¹ s⁻¹) |
| `two_smul_oneSidedR_eq_mirror` | [2]·W_R = [2]·s − (q⁻¹ s − q s⁻¹) |

**Reading.** The one-sided flip is **the letter, corrected by the normalised skein
difference**. So the corpus's q ≠ 1 parity mechanism and the one-sided flavour vertex are the
same element up to the letter. Equivalently, W_L = s − h·P₊, so the correction is the
letter's h¹ part restricted to the L line.

**The risk 9a flagged is confirmed, scope (b) within one letter.** The L-only and R-only
vertices differ **only** by which crossing carries the weight q. q s − q⁻¹ s⁻¹ gives W_L, and
the mirror weighting q⁻¹ s − q s⁻¹ gives W_R. The bar involution exchanges the two weightings,
since the skein difference is bar-odd (`skein_asym_bar_odd`), and it exchanges W_L ↔ W_R
(`oneSidedL_flip`). So "the weak coupling is left-handed" is, inside the letter algebra,
**the same datum as the convention that q weights L₊**. It moves the L/R choice to that
convention; it does not derive it. Breaking the tie needs data outside the letter (D-W1).
