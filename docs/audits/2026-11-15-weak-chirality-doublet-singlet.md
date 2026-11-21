# Weak chirality: can "L couples, R does not" be derived? (|q| > 1, quaternion sides, literature)

Bean `qou-wkcd` (epic `qou-qs0e`, blocks `qou-hlx7`). Branch
`claude/weak-chirality-doublet-singlet-2026-11-15`. Session
https://claude.ai/code/session_01Qmmkt6RTXyN5gg3AQBGRy7.

Owner questions: *"L vs R on singlet vs doublets should be derivable somehow / related?
anything in the lit?"* and *"does it depend on |q| > 1 vs |q| < 1, or is it derivable from
that? Is that the same as the convention of which crossing carries q in the skein
weighting?"*

## 0. Short answers

1. **"Which crossing carries `q`" and "L vs R" are the same bit.** They are also the same
   bit as "which root of `t² − h t − 1` is called `q`". A Hecke letter fixes only
   `h = q − q⁻¹`, and `h` is unchanged by `q ↦ −q⁻¹`. Relabelling the root swaps the
   eigenlines and turns `W_L` into `W_R` while the letter stays the same. This is proved
   (§1).
2. **`|q| > 1` does not derive L.** It makes a second available rule, "the line whose
   eigenvalue has modulus > 1", agree with the owner's labelling (D-H1 = A, the `+q`
   line) on letters with `h > 0`. It disagrees on their inverses. Under the #7836 reading
   that flavour is letter orientation, the modulus rule would put `u_L` and `d_L` on
   different lines. That is a scope-(b) negative, conditional on that reading (§1.3).
3. **Whether `q₀ > 1` is forced**: see §1.5. Through the Hecke relation alone, `q₀ > 1`
   is the statement "the generator called σ has `h > 0`", so it is an orientation
   convention. The mass formula `ℏ_q = 1 − q⁻¹` is not bar-symmetric, and it is where the
   `> 1` root gets picked.
4. **Quaternion sides give a real one-sided structure, and it has the right shape.**
   Fixing the complex (Reeb) structure on the right breaks `Sp(1) × Sp(1)` to
   `Sp(1)_left × U(1)_right`. That is `SU(2) × U(1)`, the same mechanism as the `ℍ` factor
   in Connes–Chamseddine. Which side carries it is again one bit: quaternion conjugation
   swaps the sides. The left `Sp(1)` also does **not** preserve the corpus chirality
   grading `Γ_u`; it moves `u`. So on one `ℍ` this is not "SU(2) on L, trivial on R".
   Proved (§2). Identifying it with weak isospin is scope (a), not derived.
5. **Literature**: no held source derives which side couples. The best derive *that* the
   coupling is one-sided and fix the label by convention: Connes–Chamseddine, Furey, and
   SO(10) (Baez–Huerta). Left–right symmetric models put the one-sidedness in as a vacuum
   inequality `v_R > v_L`. Preon and knot models label it arbitrarily. (§3)

**Common verdict.** Every route ends at the same one-bit structure. Each one *derives* a
two-element set {L-coupled, R-coupled}, exchanged by an involution: the root relabelling,
bar, quaternion conjugation, or `γ_F ↦ −γ_F`. None selects an element without an input.
This is the Ozma situation. The physical content is that the coupling is one-sided, and
the corpus now has that one-sidedness in three forms: the non-letter vertex `q^{∓1} J`,
the right-ℂ / left-ℍ split, and the dominant-line limit. The label "L" is a convention,
and choosing it because nature is left-handed is a naming choice, not a fit. That holds
only so long as nothing *else* is tuned on it.

## 1. Route 1: `|q| > 1`

Lean: `QOU/QuarkState/WeakChiralityRootLabel.lean`.

### 1.1 The parameter is a root label

| claim | lemma |
|---|---|
| `IsLetter q s ↔ IsLetter (−q⁻¹) s` | `isLetter_neg_inv` |
| `P₊(−q⁻¹) = P₋(q)`, `P₋(−q⁻¹) = P₊(q)`, `J ↦ −J` | `Pp_neg_inv`, `Pm_neg_inv`, `grading_neg_inv` |
| `W_L(−q⁻¹, s) = W_R(q, s)` (same letter) | `oneSidedL_neg_inv` |
| `(−q⁻¹)s − (−q)s⁻¹ = −(q⁻¹ s − q s⁻¹)` | `skein_neg_inv` |

So the owner's second question has a yes answer, made precise. The skein weighting
`q[L₊] − q⁻¹[L₋]` with `q` on the positive crossing is the same choice as calling the
`q`-root `q`. That is the same as the L-only vertex. The mirror weighting is the other
root.

This is the third involution that exchanges `W_L` and `W_R`:

| involution | letter | parameter | lines | `W_L ↦` |
|---|---|---|---|---|
| bar (#7844 `oneSidedL_flip`) | `s ↦ s⁻¹` | `q ↦ q⁻¹` | fixed | `W_R` |
| eigenline swap (#7836 `swap_hecke`) | `s ↦ −s⁻¹` | `q` | swapped | (conjugate) |
| root relabel (here) | `s` | `q ↦ −q⁻¹` | swapped | `W_R` |

### 1.2 At `q² = 1` there is one vertex

`oneSidedL_eq_oneSidedR_iff`: `W_L = W_R ⇔ h = 0`. At the classical point the L-only and
R-only vertices coincide.

So the one-sided structure is algebraic and exists for every `h ≠ 0`, formal `q`
included. It does not need the archimedean side. What does need an order or an absolute
value is a *rule that picks one* element without a convention (§1.3).

On `|q| = 1` (complex `q`) the two roots `q` and `−q̄` have equal modulus, so the modulus
rule is undefined. Bar there coincides with complex conjugation. That is reminiscent of
`(½,0) ↔ (0,½)` being complex-conjugate representations, but it is an observation and is
not used.

### 1.3 Two intrinsic selectors, and the flavour obstacle

Over an ordered field with `h ≠ 0`, the roots have opposite signs, and their moduli lie on
opposite sides of 1. So a letter determines two lines through `h` alone. Both are
independent of the label (`signLine_neg_inv`, `modLine_neg_inv`).

| selector | depends on | under `s ↦ s⁻¹` (flavour, #7836) | lemma |
|---|---|---|---|
| `signLine`: positive eigenvalue | order | **same line** | `signLine_flip` |
| `modLine`: eigenvalue of modulus `> 1` | absolute value | **other line** | `modLine_flip` |

`modLine_eq_signLine_iff`: on a letter with positive parameter they agree iff `q > 1`,
iff `h > 0` (`h_pos_iff`). The handedness each selector assigns is
`sign(log q) × (orientation of the letter)`:

| | `u = σ` | `u = σ⁻¹` |
|---|---|---|
| `q > 1` | mod = sign = `P₊` | mod = `P₋`, sign = `P₊` |
| `q < 1` | mod = `P₋`, sign = `P₊` | mod = sign = `P₊` |

Bar maps `(q, σ) ↦ (q⁻¹, σ⁻¹)` and keeps the product. **The 9a obstacle is confirmed and
sharpened.** Flavour inverts the letter. Inversion keeps signs and inverts moduli. So the
modulus rule assigns `u` and `d` to different lines, and a doublet labelled that way
would mix chiralities.

This is a scope-(b) negative for "the weak vertex acts on the dominant line of each
flavour". The invariant is that inversion inverts moduli. The claim is **conditional on
"flavour = letter orientation"** (#7836); if that reading changes, it must be rechecked.
What survives is the modulus rule applied to *one reference letter*. That is the sign
rule plus the condition `q > 1`, so it adds nothing beyond a convention on that letter.

### 1.4 The archimedean selector: long positive braids

`pow_eq`: `s^N = q^N P₊ + (−q⁻¹)^N P₋` (generic). Over `ℝ` with `|q| > 1`,
`q^{−N} s^N → P₊` (`tendsto_normalised_pow`). This is the one place `|q₀| > 1` *derives*
a line rather than labelling one: the dominant line is what a long braid in the letter
projects onto. It is still relative to the letter, since the same limit for `s⁻¹` gives
`P₋`, so it inherits the flavour obstacle of §1.3. Whether a physical quantity is
computed as such a limit is not established; that would be scope (a).

### 1.5 Is `q₀ > 1` forced?

`m_μ/m_e = Vol(4₁)/ℏ_q²` with `ℏ_q = 1 − q⁻¹` has two roots,
`q = 1/(1 ∓ √(Vol/r))`: `1.10998` (`ℏ > 0`) and `0.9098` (`ℏ < 0`). They are **not** bar
images of each other (`q₀⁻¹ = 0.9009`), because `ℏ_{q⁻¹} = −q ℏ_q`. So the formula itself
breaks bar, and the root is chosen through the sign of `ℏ_q`.

**§1.5a: why the corpus takes the `> 1` root.** A corpus grep (six paths) finds no
argument for it. It is a stated convention, and the solvers encode it:

- `mass-theory/q-zero-complex-extension.md:11` says: *"The current convention
  $q_0\in\mathbb R$, $q_0>1$ is one valid specialization."*
- `qou_substrate/constants.py:281-282` (`q_muon_at`) hardcodes `q = 1/(1 − hbar)`. The
  proton solver is seeded at `1.11` (Newton, `:134`) and at `findroot(…, 1.10997858)`
  (`:314`).
- The Lean files assume `1 < q` as a hypothesis: `MuOverDetermination.lean` (the ratio is
  injective *on* `q > 1`), and `hbarQ_pos (hq : 1 < q)`.
- `substrate-parameter-unique.md` selects the positive root of `{q, −q⁻¹}`. Both CAL-2
  roots are positive, so that rule does not decide between them.
- The `0.9098` root is recorded as a real intersection point
  (`conj-im-q-physical-role.md:160`, `2026-09-04-imq-reality-locus…md:135`), but no source
  excludes it.
- **Counter-pressure:** q-series fibre carriers converge at `q₀⁻¹ < 1`, not at `q₀`
  (bean `qou-qb8g`, `modular-s-transform-q-q-tilde.md:14`: *"Only $q_0^{-1}\approx0.901<1$
  lands in $\mathbb H$"*). Convergence therefore points the other way. The corpus does
  not reconcile this with the `q₀ > 1` convention.

So `q₀ > 1` is **declared, not derived**. Measured against the routes above, it is the
orientation convention for σ, expressed through `ℏ_q = 1 − q⁻¹`.

Inside the Hecke algebra alone, `q₀ > 1` and "the generator σ has `h > 0`" are the same
statement (`h_pos_iff`). If the corpus had used σ⁻¹ as its generator, its positive
parameter would be `q₀⁻¹ < 1`. So `q₀ > 1` is not an independent fact about chirality. It
is the orientation convention for σ, made visible through a formula (`ℏ_q`) that is not
bar-symmetric.

### 1.6 Owner ruling 2026-11-15: the left line, and how it resolves the 9a obstacle

The ruling, verbatim: *"Define left = the line on which the positive-crossing generator σ
acts with eigenvalue of size > 1"*. It is formalised as a **definition**, `leftLine`, in
`QOU/QuarkState/LeftLineDefinition.lean`; every consequence below is derived from it.

**Why this avoids the obstacle of §1.3.** The modulus criterion is applied once, to the
generator `σ`, and not to each letter. The eigenlines are shared by `σ` and `σ⁻¹`
(`flip_Pp`), so a single line serves every flavour. The obstacle in §1.3 comes from
applying the criterion letter by letter. Its scope-(b) negative stands for that reading
and does not bear on the ruled definition.

| consequence | lemma |
|---|---|
| independent of the root label (`q` or `−q⁻¹`) when `|q| ≠ 1`, so independent of D-H1 | `leftLine_neg_inv` |
| flavour-blind: the left line is an eigenline of `σ⁻¹` | `flip_eigenline_left` |
| universal: `σ` and `σ⁻¹` both act on the same line by scalars | `leftLine_eigen_sigma`, `leftLine_eigen_flip` |
| the vertex `weakVertex` (`W_L` if `|q| > 1`, otherwise `W_R`) acts as `σ⁻¹` on the left line and as `σ` on the right line, so it changes flavour on the left only: `u_L ↔ d_L` | `weakVertex_mul_leftLine`, `weakVertex_mul_rightLine` |
| `leftLine = P₊` iff `|q| > 1` | `leftLine_eq_Pp_iff` |
| under the mirror, `σ⁻¹` becomes the positive crossing (at parameter `q⁻¹`) and its left line is the old right line | `leftLine_mirror` |
| "positive-crossing generator" is well posed: given an index character `σ_i ↦ q > 0`, `−σ⁻¹` is the image of no braid word (sign argument); that the character exists on `H_n` is cited | `neg_flip_ne_braid_image` |

**Handedness = (orientation of space) × (side of `|q| = 1`).** The first factor is the
Ozma convention. The second is the measured `q₀ > 1`, which in the corpus is a declared
root (§1.5a). Consistency checks:

- At `|q| = 1` neither eigenvalue qualifies. The definition then picks nothing, and its
  `else` branch is only a default, which the label-independence lemma excludes.
- At `q = 1` the two vertices coincide (`oneSidedL_eq_oneSidedR_iff`).

In the generic fibre, bar and the root relabelling both exchange the two lines. On this
reading, parity violation is an observable-level (archimedean) effect of `q₀` lying off
the unit circle. The **"local measurement / domains" reading** is that `q₀ < 1` elsewhere
would mean opposite handedness there. That is a reading of `leftLine_eq_Pp_iff`, not a
derivation, and nothing in the corpus models regions with different `q₀`.

**Conflicts.** With D-H1 = A (the `+q` line is L) the ruling agrees whenever `q > 1`,
since then `leftLine = P₊` = the `q`-line. It does not depend on D-H1 otherwise
(`leftLine_neg_inv`). D-H2 (no swap bit) is kept: the swap `σ ↦ −σ⁻¹` is not a braid
image, so it is not a choice of positive crossing.

## 2. Route 2: quaternion left vs right multiplication

Lean: `QOU/StandardModel/QuaternionSidedSymmetry.lean` (generic `[CommRing R]`).

| claim | lemma |
|---|---|
| left multiplication is complex-linear for the right complex structure | `leftMul_complexLinear` |
| right multiplication by `b` is complex-linear ⇔ `b i = i b` ⇔ `b ∈ ℂ` | `rightMul_complexLinear_iff`, `comm_unitI_iff` |
| `x ↦ a x b` (unit `a`) is complex-linear ⇔ `b ∈ ℂ` | `bilateral_complexLinear_iff` |
| conjugation swaps sides, and carries `R_i` to `−L_i` | `star_bilateral`, `star_reeb` |
| `L_a` commutes with `Γ_u = L_u R_i` ⇔ `a u = u a` | `leftMul_comm_chiralGammaU_iff` |

**Derived.** The corpus fixed its complex (Reeb) structure on the right (#7825). That
fixes a residual symmetry of `ℂ`-linear two-sided maps equal to `Sp(1)_left × U(1)_right`.
This is a genuine one-sided structure with the `SU(2) × U(1)` shape. It is also the
mechanism by which the NCG and quaternionic models get `SU(2)` on one side (Morita 1982,
held as `67-6-1860`; Connes–Chamseddine).

**Not derived, and limits.**

- The side is the conjugation bit. The corpus chose it when the Reeb triad was defined as
  right multiplication.
- Within one `ℍ` carrying the corpus grading `Γ_u`, the left `Sp(1)` moves `u`; that is
  the gauge of #7820. Only the stabiliser `U(1)_u` acts inside a chirality. So the
  structure "SU(2) acts on the L subspace and trivially on the R subspace" is **not**
  present on one `ℍ`. In NCG models it needs a separate right-handed space (`ℂ ⊕ ℂ`
  singlets), and that space is an input there.
- There is no map from quaternion sides to the Hecke eigenlines `P±`. #7825 proves that
  the polarization action reaches only the eigenline pair of a single letter.
- "Left-multiplication `Sp(1)` is weak isospin" is scope (a).

**Already in the corpus, in prose:** `brings-surface/tetraplectic-su2-gauge-reading.md:43-49`
cites Morita 1982 and notes that the construction *"has no way to prefer $g\psi$ over
$\psi g$"* and *"owes an account of how the right-handed factor is broken"*. The results
above make that precise in two ways. Fixing the right complex structure is what breaks the
right factor to `U(1)`. And making that choice is the conjugation bit.

**Furey's convention is the reverse of the corpus's.** She builds the chirality/isospin
operators from right multiplication. Her "explanation" cannot be imported without
checking which side does what.

## 3. Route 3: literature

The library search (`INDEX.md`, `sections/`, `ocr/`) was done by a sub-agent, and the
quotes below were checked against the files it named.

| work | held? | derives | input |
|---|---|---|---|
| Connes–Chamseddine spectral SM, "Why the SM" | **not held** | that the algebra is forced to `ℍ⊕ℍ⊕M₄(ℂ)` → `ℂ⊕ℍ⊕M₃(ℂ)`, and that `ℍ` acts on one chirality only | the spectral-triple axioms (`γ_F`, `J_F`, KO-dim 6, order one); the label "L" = sign of `γ_F` |
| Chamseddine–Connes–van Suijlekom 2013 (Pati–Salam from NCG) | not held | dropping order-one gives `SU(2)_R × SU(2)_L × SU(4)` | parity breaking via the vacuum |
| Morita, *Quaternionic Weinberg–Salam* (1982) | `67-6-1860` (ocr) | `SU(2)_L × SU(2)_R` from quaternion left/right ideals | "spontaneous parity violation is guaranteed by assuming v_R > v_L" (p.1870) |
| Baez–Huerta, *Algebra of GUTs* | `arxiv-0904.1556v2` | a whole generation in one 16 of Spin(10); L vs R is "the only distinction … Spin(10) knows about" | "We *choose* to have this pattern" (§sec-014): which 16 is called L |
| Furey thesis | `arxiv-1611.09182v1` | from the chosen ladder operators, an su(2) "acts automatically on states of only one chirality" | the ladder operators, the vacuum, the labels; earlier chapter: "nothing to specify that these … act only on left-handed" |
| Krasnov, Spin(11,3) | `arxiv-2104.01786v1` | a complex structure `J̃` splits states into two chiralities | "we don't know of any mechanism that would select" `J̃` (closest analogue to the corpus `u`) |
| Bilson-Thompson helons | `arxiv-hep-ph-0503213v2`, `0603022v2` | neutrinos in one handedness (counting) | "We then arbitrarily label the chirality" |
| Gresnigt, braided fermions | `arxiv-1901.01312v1` | braids → minimal left ideals of Cl(6) | chirality taken from Bilson-Thompson |
| Finkelstein, knot model | `arxiv-0806.3105v3` | trefoil writhe ↔ **t₃** (up/down), not spacetime chirality | only `t = ½` doublets are tabulated; R singlets absent by omission |
| Jones 1985 | `s0273-0979-1985-15304-2` | `V_{L̃}(t) = V_L(1/t)`: mirror = `q ↔ q⁻¹` | — |
| Ozma problem | not held | the physical content is one-sidedness; the labels are conventional | — |

**Mapping onto QOU.** Finkelstein's knot mirror is a `t₃` flip, and the corpus's knot
mirror is the flavour flip (#7836). The two agree: knot chirality is isospin-like and
blind to spacetime chirality. Connes, Furey and Baez–Huerta all reach the corpus verdict:
one-sidedness is derivable, the label is not. Morita's left–right quaternion model is the
literature twin of §2, and in it parity breaking is an inequality between vacua.

## 4. Owner decisions

**D-W1. Accept "one-sidedness derived, label conventional" as the target, and record L as
a naming convention.**
- *What it means:* write in the corpus that the derived content is the two-element family
  `{q⁻¹J, qJ}` (and its quaternion and literature twins), and that "L = the `+q` line"
  (D-H1 = A) names one element.
- *Cost:* one content remark, after this PR; no compute.
- *Risk:* none to any number. It forecloses claiming the label is derived, which no
  source does.
- *Commits to:* treating any later "derivation of L" as needing an input external to the
  algebra, such as a vacuum or the orientation of σ.

**D-W2. Pursue the archimedean dominant-line route (§1.4) as a physical mechanism.**
- *What it means:* test whether some observable in the corpus is a long-braid limit, so
  that `|q₀| > 1` would select `P₊`.
- *Cost:* one probe plus Lean, a few hours.
- *Risk:* it inherits the flavour obstacle (§1.3) unless the limit is taken in a
  flavour-blind way. That makes it likely to fail, which would be a scope-(a) negative.
- *Commits to:* nothing until measured.

**D-W3. Investigate the quaternion route further (§2) by building a second space.**
- *What it means:* a right-handed singlet space on which the left `Sp(1)` acts trivially,
  as in NCG.
- *Cost:* a new construction, days.
- *Risk:* the second space is an input in every model that has one, so this would import
  Connes' structure rather than derive it.
- *Commits to:* a modelling choice the owner would have to own.

**Update after the owner's ruling (§1.6).** D-W1 is effectively taken, in a sharper form: the label is fixed by a definition tied to the measured `q₀ > 1` and to the orientation that makes `σ` the positive crossing. D-W2 remains open as a *mechanism* (why a long-braid limit would be physical); it is no longer needed to fix the label.

**Default (no answer):** nothing changes. The bean `qou-hlx7` stays open with this audit
attached, nothing is written into content, and no number moves.

**Recommendation (judgement, not finding):** D-W1. Every route and every held source
lands on the same Ozma structure. Spending more on deriving the label is chasing
something no framework has. D-W2 is the only remaining place where `|q₀| > 1` might do
real work, and it is cheap enough to try once.

## 6. Owner decisions 2026-11-15 (relayed by coordinator): results

### 6.1 Decision 1: a flavour `su(2)` acting on the left line only? Not inside one letter (scope b)

Lean: `QOU/QuarkState/FlavourDoubletOnLeftLine.lean`.

| claim | lemma |
|---|---|
| on the left line `u` and `d` are proportional: `q⁻¹(σP₊) = q(σ⁻¹P₊)` (same for `P₋`) | `flavours_proportional_on_Pp`, `_on_Pm` |
| each flavour has a component on both lines: `σ = qP₊ − q⁻¹P₋`, `σ⁻¹ = q⁻¹P₊ − qP₋` | `sigma_split`, `flip_split` |
| the corner over a line is a line: `P₊(a + bσ)P₊ = (a + bq)P₊`, so corner elements commute | `corner_Pp`, `corner_comm` |
| a commuting `sl₂` triple is zero | `sl2_triple_trivial_of_comm` |

**Verdict.** In the algebra generated by one letter, the left line is one-dimensional,
so `u_L` and `d_L` are the same vector up to scale. No flavour `sl₂` acts on the left
line only. The invariant is the commutativity of the corner.

The two-dimensional flavour space `span{σ, σ⁻¹}` is `L ⊕ R`. An `sl₂` on the pair
`(u, d)` therefore mixes the lines, which is the same failure as the quaternion
`Sp(1)_left` of §2. **So a flavour SU(2) does not avoid the quaternion problem in this
setting.**

The SM structure is `V_flav ⊗ V_chir` (dimension 4), with `su(2)` acting as `E ⊗ P_L`.
Here flavour (letter orientation) and chirality (eigenline) share one 2-dimensional
space. Beyond one letter:

- **`H₃`.** The corner `P₊ H₃ P₊ ≅ K ⊕ K` is commutative (Wedderburn decomposition,
  cited), so the same negative holds there.
- **`n ≥ 4`.** The corner is non-commutative. The commuting letters `σ₁, σ₃` give
  `K[σ₁] ⊗ K[σ₃]` of dimension 4, which has the shape chirality ⊗ flavour. **Open lead,
  not built.**

### 6.2 Decision 2: is the long-braid limit a physical mechanism? Not for any current observable (scope a)

Probe: `computations/probes/long_braid_limit_dominant_line_probe.py`. It computes
exactly in sympy, then evaluates in mpmath at 70 dps at the proton `q₀`. All checks pass.

- In `H₃`, `(σ₁σ₂)^N` is dominated by the trivial block, where `σ₁σ₂` has eigenvalue
  `q²`. On the `(2,1)` block `(σ₁σ₂)³ = 1`, so its eigenvalues have modulus 1. The
  non-dominant part therefore decays by `q₀⁻¹ = 0.9009` per crossing, an e-folding
  length of **9.58 crossings**.
- **T(3,5), the corpus weak knot (10 crossings), is not in the limit regime.** Its
  normalised trace is **17.2 %** from the limit. The probe reproduces the corpus
  `W(q) = q²(q¹²+q⁸−1)/(q²+1)²` (bean `qou-egvf`) exactly. The limit is reached to
  `10⁻³` only at **N = 31 (62 crossings)**.
- A corpus grep (six paths) finds **no observable that is a long-braid-word limit**.
  Every knot observable is a finite-N evaluation. The one genuine `N → ∞` sum feeding a
  dashboard row is the tower-summed `E₀` of `Q_β` (`qbeta_e0.py`), and that sum runs
  over powers of `ℏ_q²`, not over braid length.
- Verdict: the mechanism is real mathematics (`tendsto_normalised_pow`), but no current
  observable sits in its regime. **Scope (a) negative.**

**New finding from the probe: convention D is itself one-sided.**

- At `n = 3` the convention-D weights are `y₍₃₎ = (q⁴+1)/(q²+1)²`,
  `y₍₂,₁₎ = q²/(q²+1)²`, `y₍₁³₎ = 0`.
- The killed block `(1³)` is the sign block, where every letter acts by `−q⁻¹`: the
  all-right-line block. The trivial (all-left-line) block survives. So:
  - positive long braids converge to the trivial block;
  - mirror (negative) long braids, whose dominant block is the sign block, have **no
    normalised limit**, because the trace stays `O(1)` and oscillates with `N mod 3`.
- `z_D(−q⁻¹) = −1/(q³+q) ≠ z_D(q)`, so the owner-ruled convention D is not invariant
  under the root relabel (the L↔R bit). **Choosing D already chose a side**, and the
  side it chose agrees with `leftLine = P₊` at `q > 1`.
- This is an observation about the ruled convention, not an identification with weak
  chirality (scope a). The general-`n` form of the vanishing is the corpus lemma
  `ocneanuWeight_conventionD_eq_zero_of_three_rows` (all shapes with ≥ 3 rows, the sign
  shape included).

### 6.3 Decision 3: the index character, proved, so the cited step is gone

Lean: `QOU/QuarkState/BalancedIndexCharacter.lean`. It composes the corpus's existing
`indexRep` / `signRep` (built from the universal property of `H(M, Q)`) with the §7a
rescaling `σ_i = qi·T_i` at `Q = q²`.

| claim | lemma |
|---|---|
| `χ₊(σ_i) = q`, `χ₊(σ_i⁻¹) = qi` | `index_sigma`, `index_negCrossing` |
| `χ₋(σ_i) = −qi`, `χ₋(σ_i⁻¹) = −q` | `sign_sigma`, `sign_negCrossing` |
| a braid word maps to `q^{#pos} qi^{#neg}` | `index_wordImage` (and `sign_wordImage`) |
| **`−σ_j⁻¹` is the image of no braid word** (`0 < q`), with no cited step | `wordImage_ne_neg_negCrossing` |
| the sign character cannot separate them (`σ_iσ_i` and `−σ_j⁻¹` both have positive sign value) | `sign_cannot_separate` |

### 6.4 Decision 1 follow-up: the Furey-type test (`T_j = τ_j · P_left`)

The coordinator relayed Furey, arXiv:1806.00612 §5 (uploaded to `uploads/1806.00612v1.pdf`;
not yet ingested into `library/`). In ℂ⊗ℍ, left multiplication rotates spin and right
multiplication rotates chirality. Isospin `τ_j` lives on a second right-acting `Cl(2)`, and
`T_j = ½ τ_j (1 + i·i₃)` acts on one chirality only, giving `L ∼ 1 ⊕ 2 ⊕ 1`.

The QOU analogue: `T_j = τ_j P_left` with `[τ_j, P_left] = 0` gives
`[T_i, T_j] = [τ_i, τ_j] P_left`. Any such `T_j` lies in the corner `P_left A P_left`,
which **annihilates the right line automatically**, because `x P₋ = P₊ x P₊ P₋ = 0`. So the
question is only whether that corner contains `sl₂`.

- **(a) One letter, and `H₃`: no.** In the algebra generated by one letter, every element
  commuting with `P±` is a polynomial in `σ`, hence diagonal, so `τ_j P_left ∈ K · P_left`
  and the `T_j` commute (§6.1, `sl2_triple_trivial_of_comm`). `H₃` gives the same negative.
- **(b) `H_n` for n ≥ 4: yes, from the multiplicities.** Probe
  `computations/probes/corner_sl2_multiplicity_probe.py` (exact SYT counting, all checks
  pass) uses the Wedderburn decomposition, which is cited. In block `λ`, the `q`-line of
  `σ₁` has rank equal to the number of standard tableaux with 2 in the first row. The
  corner is `⊕_λ M_{rank}(K)`, so it contains `sl₂` once a rank is ≥ 2:

  | n | `sl₂` carriers, left corner | `sl₂` carriers, right corner | kept by convention D |
  |---|---|---|---|
  | 3 | none | none | — |
  | 4 | `(3,1)`, rank 2 | `(2,1,1)`, rank 2 | left `(3,1)` only; the right carrier has ≥ 3 rows, so trace weight 0 |
  | 5 | `(4,1)`, `(3,2)`, … | `(3,2)`, … | **both** sides keep `(3,2)` |

  So a Furey-type `SU(2)`, acting on the left line and trivially on the right, **exists
  in `H₄`**. The doublet is the multiplicity space of `(3,1)`. Its two tableaux differ in
  where 3 and 4 sit, so it is tied to the strands of the commuting letter `σ₃`. That is
  the n ≥ 4 lead of §6.1.
- **But it is not one-sided.** The right corner has its own `sl₂`. At `n = 4`, convention D
  gives the right carrier zero trace weight, which is one-sided **in what the trace sees**.
  At `n = 5` both sides have D-kept carriers. The `H₄` one-sidedness is an artefact of
  small `n` (scope a).
- **(c) `W_L` is not one of the `T_j`.** `W_L P_left = q⁻¹ P_left` is a scalar on the
  corner, so it is central and traceless only if zero. At most it is a `U(1)` direction,
  like Furey's `U(2) → U(1)`. That is noted for the hypercharge question and **not
  adopted**.
- **Furey's sign** (`1 ± i·i₃`) is the same Ozma bit as in §3.

**Verdict.** The mechanism "isospin × chirality idempotent" works in QOU from `n = 4`,
using the corner algebra. It gives an `SU(2)` that is trivial on the right line by
construction. It does **not** derive one-sidedness, because the mirror corner carries
the same structure. Which corner is "weak" is again the bit, fixed by `leftLine` (owner
ruling). Identifying the `(3,1)` multiplicity doublet with the `(u, d)` doublet is scope (a).

## 7. Owner decisions after #7855 merged: the remark, and whether the corner `sl₂` persists

Bean `qou-wkcj`.

**Headline: the exclusive one-sidedness of §6.4 is an `n = 4` accident.**

- At `n = 4` the right corner's only `sl₂` carrier is `(2,1,1)`, which convention D gives
  weight zero.
- At `n = 5` the right corner already has a carrier that D keeps, `(3,2)` of rank 2.
- So no level beyond 4 shows the structure "SU(2) visible to the trace on L only".

**What survives at every `n` is a weighted bias of `[3]_q : 1`.**
`QOU/QuarkState/ConventionDLineWeights.lean` proves the following for any linear
functional with `τ(1) = 1` and `τ(σ) = z`:

- `trace_Pp`: `τ(P₊) = (z+q⁻¹)/[2]`.
- `trace_Pm`: `τ(P₋) = (q−z)/[2]`.
- `zD_line_ratio`: at `z_D`, `τ(P₊) = [3]_q τ(P₋)`.
- `zD_trace_Pm`: `τ(P₋)` is nonzero.
- `three_bar_invariant`, `three_relabel_invariant`: `[3]_q` is unchanged by bar and by
  the root relabel.
- `zD_ratio_at_one`: at `q = 1` the ratio is `3 : 1`.

These values do not depend on `n`.

Probe `corner_sl2_weighted_persistence_probe.py` (all checks pass; exact sympy, then
mpmath at 70 dps at the proton `q₀`):

- `T_L = (z_D+q⁻¹)/[2]` and `T_R = (q−z_D)/[2]` hold exactly for `n = 2…16`, using the
  closed-form weights `y_(n−k,k) = [n−2k+1]/[2]ⁿ`.
- The `sl₂`-carrying parts of the two corners have weighted ratio ∞ at `n = 4`, then
  4.566, 3.786, 3.440, …, 3.046 at `n = 16`. They tend to `[3]_{q₀} = 3.0437`.

**Reading (observation, scope a).**

- `[3]_q : 1` is `qdim Sym²V : qdim Λ²V` for the `SU_q(2)` fundamental. It is the
  fibre that defines convention D.
- The bias is present at `q = 1` (`3 : 1`) and is bar-invariant in size. It is therefore
  a property of **convention D**, not of `|q₀| > 1`.
- `|q₀| > 1` enters only through the owner's `leftLine` definition. At `q > 1` that
  definition lands on the line D favours, so the ruled definition and the ruled trace
  convention point to the **same** side.
- A Plancherel or Wenzl weight share is exactly this computation: `y_λ` is the Wenzl
  weight at `z_D`. The limit is not a new mechanism; it reproduces `[3]_q`.

**Remark added.** `mass-theory/convention-d-chirality-side.{ts,md}`
(`rem:convention-d-chirality-side`, interprets `prop:markov-trace-frobenius-selection`)
records all three forms of the one-sidedness:

1. at `n = 3`, the all-right block `(1³)` has weight 0;
2. `z_D` is not invariant under the root relabel;
3. the `[3]_q : 1` line weights.

It states explicitly that no identification with physical chirality or with the weak
coupling is made. The corner `n = 4` / `n = 5` rank facts are probe-only (exact integer
counts that rest on the cited seminormal form); they are not formalised in Lean.

## 5. What is not established

- That convention D's one-sidedness (§6.2) is the weak chirality. Scope (a).
- That the weak coupling *is* `q^{∓1} J`, or the skein difference (#7844). Scope (a).
- That left-multiplication `Sp(1)` is weak isospin. Scope (a).
- Any map between quaternion sides and Hecke eigenlines.
- An argument for the `> 1` root of the mass formula (§1.5a: none found; convergence points the other way).

## 8. Does the corner asymmetry alternate with n, or with a sign? No: it is monotone (owner question, 2026-11-15)

Probe: `computations/probes/corner_sl2_parity_probe.py` (all checks pass; exact SYT counts,
sympy symbolic, mpmath 70 dps at the proton `q₀`).

- **Exclusivity, by parity of n.** For each `n = 4…16` the probe lists the corner `sl₂`
  carriers that convention D keeps. The right corner has **none** only at `n = 4`. From
  `n = 5` on, the right corner keeps every two-row shape `(n−k, k)` with `k ≥ 2`, and the
  left corner keeps those plus `(n−1, 1)`. Exclusivity does not return at even `n`, at
  `n ≡ 0 (mod 4)`, or anywhere else in the range.
- **The weighted ratio sequence.** `S_L/S_R` (computed for `n = 5…16`) **decreases
  monotonically**. Every increment is negative: −0.779, −0.346, −0.177, −0.0960, −0.0537,
  −0.0304, −0.0172, −0.00978, −0.00553, −0.00312, −0.00175. Every deviation from
  `[3]_{q₀} = 3.0437` is positive, from 1.522 down to 0.00222, so the ratio approaches
  `[3]_{q₀}` from above. The difference `S_L − S_R` **increases monotonically**, from 0.436
  to 0.5053. None of the three sequences alternates.
- **Transpose `λ ↔ λ'`** (the sign twist).
  - It swaps the two line ranks, `a ↔ b`. This holds for every `λ`, `n ≤ 16`.
  - Convention D is not transpose-symmetric. It kills the transpose of a two-row shape
    exactly when that shape has ≥ 3 columns. The only kept transposes are two-column
    shapes, such as `(2,2)`.
  - My first version of this check claimed "always killed" for `n ≥ 4`. That was wrong:
    `(2,2)` is its own transpose. The probe caught it, and the check now states the exact
    condition.
- **Root relabel `q ↦ −q⁻¹`.** At `z_D(−q⁻¹)` the line weights are `1 : [3]_q`: the bias
  flips side and keeps the same size. At `n = 3` the relabelled weights are
  `y_(3) = 0`, `y_(2,1) = q²/(q²+1)²`, `y_(1³) = (q⁴+1)/(q²+1)²`. That is exactly the
  transpose of convention D: the all-q block is now the one that is killed.

**Verdict: monotone, not alternating.** The only sign change anywhere is the single global
L↔R swap under the root relabel or the transpose. That is the same one bit as §1.1, not
an alternation in `n`.

## 9. Is the `n = 4` corner doublet the same thing as flavour (`σ₃ ↦ σ₃⁻¹`)? No (owner priority 3, 2026-11-15)

Probe: `computations/probes/corner_doublet_vs_flavour_probe.py` (all checks pass; exact
sympy over symbolic `q`; no floats, no fit, no witness). The probe builds Young's
seminormal form itself and **checks** the quadratic and braid relations, so the matrices
below do not rest on the cited form.

Setting: `D` is the `q`-line of `σ₁` inside the block `(3,1)` of `H₄`, spanned by the two
tableaux with 1, 2 in the first row. It is the doublet of §6.4. Flavour is read as letter
orientation (#7836): `u ~ σ₃`, `d ~ σ₃⁻¹`. `σ₃` commutes with `σ₁`, so it acts inside the
corner.

- **`dim D = 2`** and `σ₃|_D` has eigenvalues `q` and `−q⁻¹`, once each.
- **`σ₃⁻¹|_D = σ₃|_D − h·I`.** This is the corpus definition `flip q s = s − h·1`
  (`HelicityCommonSource.lean`) seen on `D`. The flavour flip is a shift by a central
  scalar.
- Consequences on `D`:
  - in `σ₃`'s eigenbasis the flip is `diag(−q, q⁻¹)` against `diag(−q⁻¹, q)`: it **fixes both
    doublet states** and never exchanges them;
  - `span{I, σ₃|_D, σ₃⁻¹|_D}` has dimension 2 and is commutative: the Cartan part of `gl₂`,
    with no raising or lowering element;
  - the off-diagonal part of the corner `sl₂` comes from `P₊σ₂P₊`, the letter that does
    **not** commute with `σ₁`; with it the corner acts on `D` as all of `M₂(K)`.
- **The doublet's two states are the two eigenlines of `σ₃`**: one on `σ₃`'s `q`-line, one on
  its `−q⁻¹`-line. The doublet label is `σ₃`'s chirality bit, not its orientation.
- Sweep: every `sl₂`-carrying block of the left corner for `n = 4…6`, and every letter
  `σ_j` (`j ≥ 3`) commuting with `σ₁`: 33 cases. The flip is a central shift on the
  multiplicity space in all of them.

**Verdict, scope (b) for this identification.** The invariant is the quadratic relation:
`σ⁻¹ = σ − h` holds in every corner of every `H_n`, so letter orientation can only ever
move a multiplicity space by a scalar. It can supply at most a `U(1)` direction, never the
two states of a doublet. Conditional on the #7836 reading "flavour = letter orientation";
if that reading changes, this must be rechecked. The `(3,1)` doublet itself is real
(§6.4), but what it doubles is `L₁ ∩ L₃` vs `L₁ ∩ R₃`: chirality of a second letter, not
`u` vs `d`.

**Consequence for the plan.** Building the `H₄` doublet in Lean **as a flavour doublet** is
not supported. What a build could still claim is "a left-only `sl₂` whose doublet is the
`σ₃` chirality pair", which needs a different physical reading and is an owner call.
