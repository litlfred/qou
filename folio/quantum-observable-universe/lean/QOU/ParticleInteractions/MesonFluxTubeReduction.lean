/-
Copyright (c) 2026 Frederick Carl Leitner. All rights reserved.
-/
import Mathlib.Tactic
import Mathlib.Algebra.Group.TypeTags.Basic
import Mathlib.Data.Multiset.Basic

/-!
# QOU.ParticleInteractions.MesonFluxTubeReduction

## Two structural obstructions to a canonical D-meson flux-tube braid

**Reading of the quark labels in Obstruction B (owner rulings 2026-11-20 and
2026-11-21).** A quark is an **unknot strand** carrying one crossing letter,
not a torus knot. The numbers `3, 5, 7` that Obstruction B attaches to quarks
are the **crossing counts of their lepton partners** `T(2,3), T(2,5), T(2,7)`,
i.e. generation labels; "the quark's winding" below means that label. The
theorems are unchanged: `windingContent` is a multiset of labels, and the
D/kaon collision is a collision of labels. Obstruction A (the 2-strand
reduction) is about the tube braid and is not affected.

Formalises the pruning invariants behind the honest negative in
`docs/audits/2026-08-02-meson-fluxtube-junction-reduction.md`
(bean `qou-qpj9`, the underived meson-binding braid from PR #4608).

The proton mass-knot is the Borromean link `6₂³ = (σ₁σ₂⁻¹)³`, a
**3-strand** braid whose exterior is hyperbolic (`Vol = 2·V_oct ≈
7.32772`, SnapPy-verified). QCD reading: three quarks, three colour
flux tubes at a string (Y-)junction. A meson `q̄q` has two endpoints
and a single colour flux tube — no junction. The proposed derivation
was the *Y-junction → single-tube reduction*.

### Obstruction A — the naive single-tube reduction is `Vol = 0`

The literal reduction (drop one colour tube) takes the strand count
`3 → 2`. But a 2-strand braid has **no braiding freedom beyond one
winding number**: `B₂ ≅ ℤ` is abelian (the braid relation
`σ₁σ₂σ₁ = σ₂σ₁σ₂` needs a *third* strand). Hence every 2-strand braid
is a torus braid `σ₁^k`, closure `T(2,k)`, `Vol = 0` (Thurston; SnapPy-
verified `k = 2..10`, incl. the named gluon tube `T(2,9)`). So the
naive reduction yields only a `Vol = 0` *carrier* (quantum numbers),
never a hyperbolic mass-knot — strand *removal* cannot build the
Brunnian (3-component) structure that hyperbolicity needs. The
framework itself avoids this by placing the meson at **`H₃(q)`** with
the Hopf-binding supplying the third strand
(`lepton-meson-parallel.md`), not at `H₂(q)`.

`twoStrand_comm` / `twoStrand_commutator_trivial` /
`twoStrand_winding_bijective` are all **false** for `B₃` (nonabelian;
the alternating word `(σ₁σ₂⁻¹)³` lives in its nontrivial commutator
structure and *is* the hyperbolic Borromean). That contrast is the
content.

### Obstruction B — the winding dictionary cannot separate D from K

The owner-redirected route (D meson `c̄u`, the asymmetric single tube
`c̄`(n) | light(3)) fixes the braid via the symbolic gg→`c̄c`
operator-selection, which selects a *generation label* `n ∈ {3,5,7}` (the
crossing count of the quark's lepton partner `T(2,n)`).

**CORRECTED 2026-08-24.** This docstring claimed the corpus assigns
**charm two incompatible windings**, `T(2,5)` and `T(2,7)`. It does
not. Both tables say `T(2,5)`; the reported `(2,7)`/`7₁` is the value
on the **preceding line** of `knot-notation-convention-table1-data.md`
— line 8, the **tau lepton** `7₁` — read together with line 9's charm
label. Verified: that line was created as `(2,5)`, no commit ever wrote
a charm `7₁` row, and charm maps to 7 nowhere in the corpus.

So charm's winding is unambiguous at **n = 5**, and under the meson
crossing-count rule `crossings = n₁ + n₂`
(`lepton-meson-torus-knot-dictionary.lean` `meson_crossing_is_sum`):

* charm `= 5` ⇒ D `= {5,3}` collides with kaon `{3,5}` (8 crossings).

The correction makes this obstruction **sharper, not weaker**: with no
`n = 7` alternative the collision is exact and unavoidable, rather than
one of two bad options.

The winding dictionary is a symmetric function of the two windings, so
it maps D and K (or D and η/φ) to the **same** value while they are
physically distinct (`m_D ≈ 1865 ≈ 3.8·m_K`). `windingContent` is
therefore **non-injective** (`winding_content_not_injective`): the
operator-selection input for the D meson is not canonically fixed. The
precise missing datum is a **weak-isospin / up-down-type grading**
`T₃` orthogonal to the generation winding `n` — charm (up-type gen-2)
and strange (down-type gen-2) collide at the same `n`, and the up/down
distinction lives in the framework's *weak* generator `T(3,5)`
(`force-knot-identification.md`), not in the `T(2,n)` winding number.

Refs:
  - docs/audits/2026-08-02-meson-fluxtube-junction-reduction.md
  - docs/audits/2026-08-02-jpsi-boundstate-mass.md (the gate)
  - bean qou-qpj9
-/

namespace QOU.ParticleInteractions.MesonFluxTube

/-! ### Obstruction A — 2-strand reduction has no braiding freedom -/

/-- The **winding group of a 2-strand braid**, `B₂ ≅ ℤ`. With fewer
    than three strands the braid relation cannot be written, so `B₂`
    is the free group on the single generator `σ₁`, i.e. `ℤ` (written
    multiplicatively). This is the object the naive single-tube
    reduction lands in. -/
abbrev TwoStrandWinding := Multiplicative ℤ

/-- **2-strand braiding is commutative.** `B₂` is abelian — the meson
    carrier retains no braiding degree of freedom beyond its winding.
    Contrast `B₃`, which is nonabelian: exactly the room the
    hyperbolic Borromean `(σ₁σ₂⁻¹)³` needs. -/
theorem twoStrand_comm (a b : TwoStrandWinding) : a * b = b * a :=
  mul_comm a b

/-- **The commutator is trivial on `B₂`.** `⁅a,b⁆ = 1` for all
    2-strand braids — the sharp contrast with `B₃`, whose nontrivial
    commutator subgroup houses the Brunnian/hyperbolic Borromean. A
    carrier with trivial commutator admits no Brunnian linking, hence
    no hyperbolic bound-state volume. -/
theorem twoStrand_commutator_trivial (a b : TwoStrandWinding) :
    a * b * a⁻¹ * b⁻¹ = 1 := by
  rw [twoStrand_comm a b]; group

/-- **The winding number is a complete invariant of a 2-strand
    braid.** `B₂ → ℤ` is a bijection: the whole carrier is fixed by
    one integer, which cannot index a hyperbolic knot family (the
    `T(2,k)` closures are `Vol = 0` for every `k`). -/
theorem twoStrand_winding_bijective :
    Function.Bijective (Multiplicative.toAdd : TwoStrandWinding → ℤ) :=
  (Equiv.refl ℤ).bijective

/-! ### Obstruction B — the winding dictionary is charm-degenerate -/

/-- The four meson generations of `lepton-meson-torus-knot-dictionary`,
    plus the D meson. -/
inductive Meson
  | pion    -- ū d
  | kaon    -- ū s
  | etaPhi  -- s̄ s
  | Dmeson  -- c̄ u  (open charm)
deriving DecidableEq

/-- The **generation-label content** the `T(2,n)` dictionary sees:
    the unordered pair `{n₁, n₂}` of the two quarks' generation labels
    (each the crossing count of the quark's lepton partner; the quarks
    themselves are unknot strands), with the corpus assignment
    `u,d = 3`, `s = 5`, and **charm `= 5`**
    (`knot-formula-table` row 11). The operator-selection / crossing-
    count rule is a symmetric function of this multiset. -/
def windingContent : Meson → Multiset ℕ
  | .pion   => {3, 3}
  | .kaon   => {3, 5}
  | .etaPhi => {5, 5}
  | .Dmeson => {5, 3}   -- charm = 5

/-- **D and kaon carry the same winding content.** With charm `= 5`
    the open-charm D meson `{c̄=5, u=3}` and the kaon `{ū=3, s=5}` are
    the *same* multiset — so every symmetric function of the windings
    (crossing count `n₁+n₂ = 8`, product, …) agrees on them. -/
theorem D_kaon_same_winding : windingContent .Dmeson = windingContent .kaon := by
  decide

/-- **The winding dictionary is not injective.** It cannot separate
    the D meson from the kaon, though they are physically distinct
    (`m_D ≈ 3.8·m_K`). Hence the gg→`c̄c` operator-selection input for
    the D meson is *not* canonically fixed by the `T(2,n)` winding
    number alone: a weak-isospin (up/down-type) grading orthogonal to
    `n` is the missing datum.

    **REFINED 2026-08-24.** Non-injectivity is a property of
    `windingContent`, which maps each meson to a `Multiset ℕ`. The
    corpus itself *does* separate charm from strange: table 2 gives
    `c = T(2,5)` and `s = T(2,5)^σ`, and `σ` is present iff the quark
    is down-type across all five quark rows (`u/d` at 3, `c/s` at 5,
    `b` at 7). `knot-notation-convention.md` defines
    `T_{m,n}^σ = T_{m,-n}`. So the degeneracy is this projection
    **discarding `σ`**, not an absent structure — the discriminator
    survives one level up.

    **WEAKENED on a second pass, same day.** The caveat above read
    "`σ` is overloaded … whether it *is* `T₃` is the open question".
    That is too generous. `knot-notation-convention.md` *documents*
    `σ` on a knot as **charge conjugation** ("the superscript
    distinguishes a particle from its antiparticle via mirror
    reflection"), instantiated on leptons as electron `T(2,3)` /
    positron `T(2,3)^σ`. Under that meaning the quark rows assert
    `d = ū`, `s = c̄`, `b = t̄` — charge `−1/3` identified with
    charge `−2/3`, which cannot be intended.

    So `σ` cannot be the `T₃` grading *as documented*: one superscript
    carries two relations and only the unusable one is defined. The
    5/5 down-type alignment is real and suggestive, but the
    discriminating assignment is **undefined**, not merely
    unprojected — a prerequisite for the `T₃` work rather than a step
    within it. -/
theorem winding_content_not_injective : ¬ Function.Injective windingContent := by
  intro hinj
  have : Meson.Dmeson = Meson.kaon := hinj D_kaon_same_winding
  exact absurd this (by decide)

/-- **A hypothetical charm `= 7` would collide too** — kept as a
    robustness remark, NOT as a corpus fact.

    This previously read "under the other corpus value charm `= 7`
    (`knot-notation-convention` row 9)". **There is no such corpus
    value** (correction at Obstruction B above): the corpus fixes charm
    at `n = 5`, and `7₁` on the adjacent line is the tau lepton. The
    arithmetic below is true and worth keeping — it shows the
    degeneracy is not an artifact of the particular assignment, since
    even a counterfactual `n = 7` would land on `η/φ`'s crossing count
    — but it must not be cited as evidence of corpus ambiguity. -/
theorem D_charm7_crossing_collides_etaPhi :
    (7 + 3 : ℕ) = (Multiset.sum {5, 5} : ℕ) := by decide

end QOU.ParticleInteractions.MesonFluxTube
