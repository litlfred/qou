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

**Default (no answer):** nothing changes. The bean `qou-hlx7` stays open with this audit
attached, nothing is written into content, and no number moves.

**Recommendation (judgement, not finding):** D-W1. Every route and every held source
lands on the same Ozma structure. Spending more on deriving the label is chasing
something no framework has. D-W2 is the only remaining place where `|q₀| > 1` might do
real work, and it is cheap enough to try once.

## 5. What is not established

- That the weak coupling *is* `q^{∓1} J`, or the skein difference (#7844). Scope (a).
- That left-multiplication `Sp(1)` is weak isospin. Scope (a).
- Any map between quaternion sides and Hecke eigenlines.
- An argument for the `> 1` root of the mass formula (§1.5a: none found; convergence points the other way).
