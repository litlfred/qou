# Two false axioms: `proton_mass_from_substrate` and `neutron_mass_from_substrate`

**Kernel-verified 2026-09-04 on `origin/main`.** Not a gap, not an over-claim —
two `axiom` declarations assert propositions whose **negations are provable**
from the definitions in the same file. Each file is therefore inconsistent:
`False` is derivable in it, and so is anything else.

## The proton

`content/quantum-observable-universe/knots-particles-confinement/categorical-proton.lean`

```lean
noncomputable def q₀ : ℝ := 1.10998

noncomputable def proton_mass (q : ℝ) : ℝ :=
  let vol_borromean := 7.32772475341775
  let hbar_q := 1 - q⁻¹
  vol_borromean / hbar_q ^ 2

axiom proton_mass_from_substrate_axiom : |proton_mass q₀ - 938.272| < 1

theorem proton_mass_from_substrate : |proton_mass q₀ - 938.272| < 1 :=
  proton_mass_from_substrate_axiom
```

`ℏ_q = 1 − 1/1.10998 = 0.099082866358`, so

    proton_mass q₀ = 7.32772475341775 / 0.099082866358² = 746.400676451

and `|746.400676451 − 938.272| = 191.87`, not `< 1`.

**Verified by the Lean kernel, not by arithmetic**: `¬(|proton_mass q₀ −
938.272| < 1)` is proved by `norm_num [abs_lt]` after unfolding, `lean`-direct
exit 0. Every constant involved is a decimal literal in that same file, so this
is decidable arithmetic with nothing to interpret.

## The neutron

`.../categorical-neutron.lean`, same shape:

```lean
axiom neutron_mass_from_substrate_axiom : |neutron_mass q₀ - 939.565| < 1
```

`neutron_mass q₀ = 746.505207884`; `|746.505 − 939.565| = 193.06`. Negation
likewise kernel-proved, exit 0.

## Why this is not merely a wrong constant

The gap is ~192 MeV, about 20 %. It is not a precision problem, and correcting
`vol_borromean` would not be the fix: **the construction itself is retired.**
`Vol(𝓑₃)/ℏ_q²` for an absolute nucleon mass is the shape AGENTS.md marks with a
🛑 (owner ruling 2026-06-24) — *"NOT the canonical ABSOLUTE nucleon mass"*, the
form that yields 966 or 406 rather than 938 — and the 2026-08-11 ruling
**excised absolute mass as a prediction altogether**. There is also no `m_e`
anywhere in these files, so the expression is not even dimensionally the
`m(K) = m_e · Vol(K) · ρ(K)/ℏ_q²` shape it resembles.

So the honest reading is that these two files predate both rulings and were
never revisited. The axioms are what the rulings exist to prevent, in the most
literal form: a nucleon mass in MeV, asserted, matching CODATA to <1 MeV by
fiat while the formula beneath it produces 746.

## Scope and blast radius

- **Neither theorem has a consumer.** `proton_mass_from_substrate` and
  `neutron_mass_from_substrate` are referenced nowhere else in `content/`.
  The inconsistency is confined to these two files — which is why this is a
  finding to act on deliberately, not an emergency.
- Both are **content-block siblings**, so under AGENTS.md §0a they are what a
  `lean.ref` resolves to first. They are outside the Lake globs, and CI is
  `workflow_dispatch`-only, so nothing has ever compiled them.
- Both axioms are among the **46 uncited** ones (no `-- Ref:` line above the
  `axiom`), though each file carries a `[manuscript]` reference in nearby prose.

## What I did not do, and why

I did not change these files. The fix is not mechanical: deleting the axioms
breaks the theorems, "correcting" the constants would enshrine a construction
two owner rulings retired, and deciding what `def:categorical-proton`'s
formalisation should say **now that absolute mass is excised** is an authoring
judgement about the paper's physics, not a repair. That is the author's call.

The measurement is complete and reproducible; the disposition is open.

## Reproduce

```lean
noncomputable def q₀ : ℝ := 1.10998
noncomputable def proton_mass (q : ℝ) : ℝ :=
  let vol_borromean := 7.32772475341775
  let hbar_q := 1 - q⁻¹
  vol_borromean / hbar_q ^ 2

theorem axiom_is_false : ¬ (|proton_mass q₀ - 938.272| < 1) := by
  unfold proton_mass q₀
  norm_num [abs_lt]
```

## How it was found

By fixing an unrelated scope bug. The audit script walked only
`content/quantum-observable-universe/lean` — the Lake library tree — so all 944
content-block siblings were invisible, and with them 148 of the corpus's 182
axioms. These two were in that blind spot. Nothing was looking for false
axioms; they surfaced from a citation-key survey of the 46 uncited ones.

## Resolution (2026-11-16 — `qou-4paj`)

Both inconsistent `axiom` declarations (`proton_mass_from_substrate_axiom` in
`folio/quantum-observable-universe/knots-particles-confinement/categorical-proton.lean`
and `neutron_mass_from_substrate_axiom` in
`folio/quantum-observable-universe/knots-particles-confinement/categorical-neutron.lean`)
have been removed and replaced by sorry-free theorems (`proton_mass_from_substrate`,
`bare_borromean_carrier_not_938`, `neutron_mass_from_substrate`, and
`bare_neutron_carrier_not_939`), documenting that the retired bare-volume
carrier `Vol(𝓑₃)/ℏ_q² ≈ 746.40` is superseded by the canonical Wedderburn /
Borromean trace ratio per the 2026-06-24 and 2026-08-11 owner rulings.
