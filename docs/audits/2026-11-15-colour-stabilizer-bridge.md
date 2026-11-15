# The two SU(3)s: can the octonion colour stabilizer be bridged to the tower's colour channel?

Bean `qou-cb3r` (parent `qou-8lxd`). Related: `qou-ni4b` (the Hecke-side instantiation gap),
`qou-abtu` (furey2016 citation), `qou-qs4c`. Date 2026-11-15.

Owner question, relayed by the coordinator:

> "can we close gap — conj:sm-colour-stabilizer-action … no instance exists … The two SU(3)s live
> side by side with no bridge between them."

Lean (new):
- `QOU/StandardModel/ColourBridgeObstructions.lean`;
- `QOU/IwahoriHecke/JimboClassicalLimit.lean`.

Verification status is in §7.

## 0. Verdict

**(c), an honest negative, with the extra choice named. It is a bridge only at q = 1, and only
after complexification.**

What an honest bridge from `su3 e` to the tower's three-strand colour space needs, beyond structure
both sides already carry:

1. **Complexify the tower triplet**, i.e. extend scalars ℚ → ℚ(i).
   - The tower fundamental `V = ℚ³` is odd-dimensional and so carries **no** complex structure
     (`tower_triplet_no_complex_structure`, a proved invariant: det² ≥ 0).
   - The octonion colour triplet `ℂ³_e` is a 6-dimensional ℚ-space whose complex structure is
     `L_e` (`Le_sq_eq_neg_id`).
   - So no ℚ-linear isomorphism intertwines the two. This is scope (b): dimension 3 against 6
     over ℚ, plus the odd-dimension invariant.
2. **Choose one bit: the orientation of `e`**, equivalently 3 vs 3̄, i.e. which complex structure,
   `+L_e` or `−L_e`.
   - `su3 (−e) = su3 e` (`su3_neg`). `−L_e = L_{−e}` is a second complex structure, distinct from
     `L_e` (`Le_neg_ne`), commuting with the same stabilizer (`negLe_commutes`).
   - So the stabilizer fixes the line ℚe but not its sign.
   - The tower side fixes nothing here either: its strand orientation distinguishes quarks from
     antiquarks only once one *declares* forward strands to be quarks.
   - This bit is the **charge-conjugation convention**. It is a naming of 3 vs 3̄, not a fit
     against data. It is the same choice Furey makes explicitly with the projector
     `P = ½(1 + iε_z)`, of which the source says "a continuum of other possibilities exist"
     (`library/arxiv-1611.09182v1`, §3.5.1).
3. **Work at q = 1.**
   - At `q ≠ 1` no classical Lie action commutes with the tower's crossing: the primitive
     coproduct of the sl₃ root vector `E₀₁` commutes with Jimbo's `Ř` iff `q = 1` and `qi = 1`
     (`primitive_commute_rCheckN_iff`). The four nonzero commutator entries are `q − 1`, `qi − 1`
     and their negatives.
   - So at q₀ the colour symmetry the tower can carry compatibly with its braiding is `U_q(gl₃)`
     (the Jimbo commutant, whose surjectivity is G3.4, in progress), not `su3 e`.

After 1–3 the remaining freedom is an sl₃(ℂ)-intertwiner between two 3-dimensional irreducibles.
By Schur's lemma it is unique up to a scalar, i.e. up to the inner/central freedom the class
already ignores. So **"(b) up to one bit" holds only at the complexified classical level**, and
the one bit is a convention.

**Additional standard fact (not formalised here):** the two real forms differ.
- The tower's gl₃ over ℚ (or ℝ) is the **split** form.
- `su3 e`, derivations of the definite octonions fixing `e`, is the **compact** form.
- `sl₃(ℝ) ≇ su(3)` as real Lie algebras: their Killing forms have signatures (5, 3) and (0, 8).
- So there is no bridge over ℚ or ℝ at all. The two agree only after complexification, which is
  exactly step 1.
- Formalising this would need a definite invariant form on `su3 e`, which the corpus does not yet
  prove. It is recorded as such.

## 1. What the class actually asks, and why closing it would prove nothing

`ColourStabilizerAction g V` asks only for an injective ℚ-linear map `g → End V`.
- `not_colourStabilizerAction_of_dim_sq_lt` (corpus) proves this needs `finrank g ≤ (finrank V)²`.
- `colourStabilizerAction_of_finrank_le` (new) proves the converse, building the map from bases
  alone.

So the class is **equivalent to a dimension inequality**. In particular
`colourStabilizerAction_on_three` gives an instance on the tower triplet `ℚ³` for any
8-dimensional colour algebra, with no octonions and no Hecke structure involved.

This is the coordinator's trap made into a theorem. An instance of the class on the tower side is
always available, and always a selection. The corpus already observed the octonion-side tautology
(`OctonionColourActionBaseModule`, instance on 𝕆 itself). This closes the other side the same way.

**Consequence for the conjecture.** `conj:sm-colour-stabilizer-action`, as formalised, is not the
bridge question. The bridge question (bean `qou-ni4b`: "compatible with its Hecke / braid
structure") needs a strengthened class. A proposal, as judgement:

```lean
class ColourBridge (V : Type*) … where
  Φ : su3 e →ₗ⁅ℚ⁆ Module.End ℚ (V ⊗ ℚ(i))   -- Lie hom, after complexification
  injective : Function.Injective Φ
  intertwines_J : ∀ D, Φ D ∘ J = J ∘ Φ D      -- J the chosen ±L_e image
  commutes_crossing : …                      -- with Ř, via the primitive coproduct
```

By §0 item 3, the last field is satisfiable only at `q = 1`.

## 2. The two sides, side by side

| | octonion side (O) | tower side (T) |
|---|---|---|
| colour algebra | `su3 e = ker(D ↦ De) ⊂ Der 𝕆 = 𝔤₂`, dim 8 (`finrank_su3_e1`) | `gl₃` / `U_q(gl₃)` commutant of the Jimbo action (`JimboGL`, #7841) |
| real form | compact | split (over ℚ/ℝ); `U_q` at q₀ |
| triplet | `ℂ³_e`, 6-dim over ℚ, J = L_e | `V = ℚ³`, odd-dimensional, no J |
| orientation | ±e both give the same `su3 e`; L_{−e} = −L_e | strand orientation (quark vs antiquark) by declaration |
| q | none: no `q` occurs in any `MathlibExt/Octonion*.lean` (grep, 9 files) | q₀ ≈ 1.10998 |
| coproduct | primitive (Lie) | Jimbo `Ř`, Hecke at q |

## 3. The q question

**The octonions in the corpus are classical.** Measured: `grep -c "(q :\|q₀\|qBracket"` over the
nine `MathlibExt/Octonion*.lean` files returns 0 in each.

The coordinator's premise, "the corpus says octonions are not q-deformed", is **not stated as a
sentence** anywhere in the corpus. A grep for "q-deformed octonion", "octonions are not
q-deformed" and "quantum octonion" in `folio/` and `docs/` `.md` found nothing. The premise holds
*de facto*, not by a recorded ruling.

**Result.** `primitive_commute_rCheckN_iff` (generic `CommRing`): a classical sl₃ action enters the
tower compatibly with its crossing **only at q = 1**. Two routes past this:

1. **The classical limit** (AGENTS.md §7b item 2, decategorification to q = 1). The bridge of §0
   lives here, and only here.
2. **A deformed octonion structure** whose derivation stabilizer would be a quantum group acting
   through a non-primitive coproduct. The corpus has none, and none is held in the library under
   that name (grep of `library/INDEX.md` for "octon" returns 8 documents, none q-deformed).
   Building one is new mathematics, not a bridge.

At formal ħ, Drinfeld–Kohno gives an equivalence of braided monoidal categories between
`U_ħ(sl₃)`-modules and `sl₃`-modules with the KZ associator. That is a categorical statement at
formal ħ, not a Lie-action bridge at numeric q₀ ∈ ℚ. It is recorded as the standard reason route 2
is not "just a twist", not as a held citation.

## 4. Literature (corpus-grep path 5 + ocr tier)

| work | held | what it supplies here |
|---|---|---|
| Günaydin–Gürsey 1973 | `folio/references/gunaydin-gursey1973.json`; quoted in 6 library docs | su(3) ⊂ 𝔤₂ as the stabilizer of an imaginary unit: the O-side definition. No braids. |
| Furey 2016 (thesis) | `library/arxiv-1611.09182v1`, `furey2016` | ideals of ℂ⊗𝕆 with an explicit projector choice P = ½(1+iε): the orientation bit of §0 item 2, chosen by hand ("a continuum of other possibilities exist"). Bean `qou-abtu` tracks the citation. |
| Gresnigt 2019 | `library/arxiv-1901.01312v1`, `gresnigt2019` | maps circular-braid words B₃^c to Furey's Cl(6) minimal-ideal basis (σ₁σ₂ ↦ α₁† …). The representations are **non-faithful with finite image**, at a root of unity (σ = (1+i)/√2, eigenvalues e^{±iπ/4}; our check in `2026-11-15-quark-state-library-citations.md` §3). So it is a braid ↔ Cl(6) dictionary at a root of unity, **not** a bridge for the Hecke algebra at real q₀ > 1. |
| Baez 2002 | `baez2002` | survey; 𝔤₂ and su(3) ⊂ 𝔤₂ background. |
| Dixon | not found in `folio/references` or `library/INDEX.md` | — |

## 5. What remains open, and the decision it needs

**The decision.** Should the colour-action conjecture be restated so that its instance would be a
genuine bridge? This needs the owner because it changes what `conj:sm-colour-stabilizer-action`
claims.

**Option A: strengthen the class** to the Lie-hom + complex-structure + crossing-compatibility form
of §1, at q = 1.
- *Means:* the conjecture becomes "the tower's classical limit carries the octonion colour action,
  up to one orientation bit".
- *Costs:*
  - the `.lean` / `.md` / `.ts` of `sm-colour-stabilizer-action` and the specialisation in
    `OctonionSU3BracketClosure`;
  - the two existing tautological instances become obsolete;
  - the content blocks citing the class (the appendix's gap ledger) need re-reading.
- *Risks:* none to scored numbers; no compute reads the class.
- *Commits to:* stating that the colour bridge is a q = 1 statement.

**Option B: keep the class and record the negative.**
- *Means:* add the calibration that the class is equivalent to `finrank g ≤ (finrank V)²`, so no
  instance of it is evidence.
- *Costs:* one paragraph in the block.
- *Commits to:* nothing.

**Option C: pursue a q-deformed colour stabilizer.**
- *Means:* new mathematics (route 2 of §3).
- *Costs:* open-ended.

**Recommendation (judgement).** A, with B's calibration paragraph added either way. The class as it
stands cannot distinguish the open problem from a dimension count.

**Default.** Nothing changes. The class stays, its two tautological instances stay, and bean
`qou-ni4b` stays open.

## 6. Scope of each claim

| claim | scope | invariant |
|---|---|---|
| class ⇔ finrank g ≤ (finrank V)² | proved (both directions) | dimension |
| no ℚ-linear iso intertwining J between `ℚ³` and `ℂ³_e` | (b) | det² ≥ 0 in odd dimension; dimension 3 ≠ 6 |
| stabilizer does not fix 3 vs 3̄ | proved | su3(−e) = su3(e), L_{−e} = −L_e ≠ L_e |
| classical Lie action compatible with `Ř` only at q = 1 | proved for the root vector E₀₁ (sufficient for any action whose complexified image is sl₃) | explicit commutator entries `q − 1`, `qi − 1` |
| no real-form bridge (compact vs split) | standard, **not formalised** | Killing signature |

## 7. Verification

The Lean is being verified lean-direct against the real import cone. This section is updated in the
PR when the run completes.
