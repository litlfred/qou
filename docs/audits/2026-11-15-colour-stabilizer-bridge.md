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

**Both files compile.** Command, run from `folio/quantum-observable-universe/lean`:
`lean -DautoImplicit=false -s 65536 <file>`, exit 0, no errors and no warnings.

**Import cone.** The real one, not a stub:
- restored Mathlib (3480 oleans);
- a hardlink mirror of the restored QOU tree;
- `QOU.IwahoriHecke.TensorEmbeddingGL`, which had no olean and was built lean-direct (exit 0).

Every other cone module was checked FRESH by comparing Lake's source hash against its `.trace`.

**Axioms.** `#print axioms` on all 12 public theorems gives `[propext, Classical.choice, Quot.sound]`.
There is no `sorry`, `native_decide` or `axiom`.

**Proof repairs during verification.** No statement changed meaning.
1. `comm_entry_q` / `comm_entry_qi` were ill-typed as first written (a matrix applied to a single
   pair). They are now applied curried, as row `(0,0)` with column `(1,0)` / `(0,1)`, which is what
   the docstrings say.
2. The `←` direction of `primitive_commute_rCheckN_iff` is now proved via `Ř(1,1) = flip`. This
   proof holds for any `x`, not only `E₀₁`.
3. Minor tactic fixes: `Odd 3`, and a `calc` in `Le_neg_ne`.

The commutator signs came out as computed in integer arithmetic beforehand:
`((0,0),(1,0)) = q − 1` and `((0,0),(0,1)) = qi − 1`.

**Not done.**
- No `lean-library-sweep`.
- No drop-one hypothesis check.
- The real-form (compact vs split) fact of §0 is not formalised.

## 8. Option C probe: a q-deformed colour stabilizer inside U_q(g₂) (owner choice "q2c", scope (a))

**Question.** Is there a q-analogue of `su3 e ⊂ Der 𝕆` that meets the tower's Jimbo `Ř` at `q₀ ≠ 1`?
The natural candidate is the long-root `U_q(sl₃)` inside `U_q(g₂)`, acting on the 7-dimensional module
`V₇`, which deforms `Im 𝕆 = 1 ⊕ 3 ⊕ 3̄`.

**Producer.**
[`computations/eightfold/quantum_g2_colour_stabilizer_probe.py`](../../computations/eightfold/quantum_g2_colour_stabilizer_probe.py)
and its witness `quantum-g2-colour-stabilizer-probe.witness.json`.
- Arithmetic is `fractions.Fraction` only, evaluated at exact rational points q ∈ {1, 2, 3, 5/2}; it is not symbolic in q.
- Conventions are Jantzen's: α₁ is short (q₁ = q), α₂ is long (q₂ = q³), and Δ(E) = E⊗1 + K⊗E.
- **Module check (M):** every `U_q(g₂)` relation holds exactly on `V₇` at q = 2, 3, 5/2. This covers K–E, K–F and [E,F], plus both quantum Serre relations; the Serre relation with exponent 4 uses q-binomials.

| check | q = 1 | q ∈ {2, 3, 5/2} |
|---|---|---|
| **A** Restriction to `1 ⊕ 3 ⊕ 3̄` | holds (by weights alone) | holds (by weights alone). The long-root Cartan acts through **q³**, so the colour sl₃ inside g₂ is deformed at `q_long = q³`, not q. |
| **B** Elements of weight 3α₁+α₂ in `U_q(n⁺)` (a 4-dimensional space) whose coproduct maps `3⊗3` into `3⊗3` | exactly one, `ad_{E₁}³ E₂`, i.e. the classical root vector | **none** (kernel dimension 0) |
| **C** `Hom(V₇⊗V₇, V₇)` (the q-cross-product) | 1-dimensional. L_e = +1 on the 3 and −1 on the 3̄; R_e = −L_e | 1-dimensional. The eigenvalues of L_e are **(1, q⁻⁴, q⁻⁴) on the 3** and **(−q⁻⁶, −q⁻², −q⁻²) on the 3̄**, up to one overall scale. The ratio R_e/L_e on the 3 is (−q⁻⁶, −q², −q²) |

**Reading.**
- **(a) Yes, at the module level only.** The decomposition `V₇ = 1 ⊕ 3 ⊕ 3̄` survives, because it is forced by weights. The induced colour deformation parameter is q³. Matching it to the tower's Jimbo `U_q(gl₃)` at q₀ would therefore need `q_{g₂} = q₀^{1/3}`, which is one more choice (a cube root).
- **(b) No at the coproduct level, within the searched space.**
  - No weight-(3α₁+α₂) element of `U_q(n⁺)` has a coproduct that preserves `3⊗3` once q ≠ 1. So the triplet is not a sub-object of `V₇ ⊗ V₇`, and Jimbo's Ř on `3⊗3` cannot be the restriction of the g₂ braiding along it.
  - This is the quantum shadow of a known structural fact: sl₃ ⊂ g₂ is a maximal-rank subalgebra but **not a Levi subalgebra**. Only Levi subalgebras give Hopf subalgebras `U_q(l) ⊂ U_q(g)`.
  - Nor is sl₃ the fixed-point subalgebra of an involution, since G₂/SU(3) = S⁶ is not a symmetric space. So the quantum-symmetric-pair (coideal) framework does not apply directly either.
  - Combined with `primitive_commute_rCheckN_iff` (§3), neither the primitive coproduct (classical su₃ e) nor the U_q(g₂) coproduct (quantum G₂) carries the colour triplet onto the tower's Ř at q ≠ 1.
- **(c) The octonion product deforms to the unique U_q(g₂)-equivariant q-cross-product.**
  - The product no longer pairs e with the triplet by a scalar. L_e is not constant on the 3, so it **does not commute** with the long-root operators, which mix the three weight lines. The q-analogue of `su3_comp_Le_eq_Le_comp` fails at q ≠ 1.
  - Left and right multiplication by e differ by powers of q, not by a sign. That is braided antisymmetry, not alternativity.
  - The 3 ↔ 3̄ bit **survives**: L_e is positive on the 3 and negative on the 3̄ for every q > 0, and the sign of the normalisation (equivalently e ↦ −e) flips which is which.
  - Note the classical baseline here is the **split** form (L_e² = +1 on 3 ⊕ 3̄, para-complex), because U_q(g₂) over ℚ(q) is split. The compact form's L_e² = −1 is recovered only after complexification, consistent with §2's complexification requirement.

**Scope (a), stated precisely.**
- Exact at four rational points, not proved symbolically in q.
- B searches `U_q(n⁺)` (Cartan twists are irrelevant to leakage) with one coproduct convention. The opposite coproduct is related by the flip, which preserves 3⊗3. B does **not** search q-deformed embeddings of the triplet other than the weight subspace, nor elements outside `U_q(n⁺)·U⁰`.
- Nothing in this section is a bridge or a refutation of one. It records what the obvious q-analogue does and does not do.
- No Lean was written for this section: the facts are 49×49 matrix computations, and the small sorry-free pieces (weights) are trivial.

**Literature (path 5 + ocr).** None of the following is held in `library/`; the matches found were bibliography entries only. For stream 13:
- Kuperberg, *The quantum G₂ link invariant*, Int. J. Math. 5 (1994). This is the G₂ spider: the q-cross-product as a trivalent vertex, with its relations replacing octonion identities.
- Kuperberg, *Spiders for rank 2 Lie algebras*, CMP 180 (1996), arXiv q-alg/9712003.
- Albuquerque & Majid, *Quasialgebra structure of the octonions*, J. Algebra 220 (1999), arXiv math/9802116. It is already a bib key `albuquerque-majid1999` cited in `OctonionCocycle.lean`, but the text is not held. Its deformation is a sign 3-cocycle on (ℤ/2)³ (q = −1-type), not a continuous q, so it does not by itself answer the q₀ question.
- A standard source for PBW root vectors and their coproducts in U_q(g₂) (Jantzen, *Lectures on Quantum Groups*, or Lusztig's book) would let B be stated symbolically.

### 8.1 Check D: no U_q(g₂) braiding restricts to a Hecke operator on 3⊗3 (generic q)

Added 2026-11-15 by the thread that took over stream 6c. Producer
[`computations/eightfold/quantum_g2_braiding_on_colour_triplet_probe.py`](../../computations/eightfold/quantum_g2_braiding_on_colour_triplet_probe.py),
witness `quantum-g2-braiding-on-colour-triplet.witness.json`. Exact linear algebra over the field
ℚ(q) (sympy `DomainMatrix`), with q a symbol, not a sample. Same module and coproduct as §8.

**Why the triplet is forced.** Each weight of the 3 = span{v₁, v₆, v₅} has multiplicity 1 in V₇. So
any K-stable 3-dimensional subspace carrying the triplet's weights *is* this span. This closes the
§8 scope gap "other q-deformed embeddings of the triplet" for K-stable embeddings.

**Result.**
- dim End_{U_q(g₂)}(V₇ ⊗ V₇) = 4 over ℚ(q), as expected from V₇⊗V₇ = 1 ⊕ 7 ⊕ 14 ⊕ 27.
- The elements of that algebra that map W = 3⊗3 into itself form a 2-dimensional subspace.
- **Every one of them acts on W as a scalar.**
- Classical control at q = 1 (exact rationals, classical U(g₂); companion producer `quantum_g2_braiding_on_colour_triplet_points_probe.py`, which also re-checks q = 2, 3, 5/2): the W-preserving subspace is
  3-dimensional and contains non-scalar elements (the flip).

**Consequence.** Every braiding Ř_{V₇,V₇} is a U_q(g₂)-endomorphism of V₇⊗V₇. If one restricted to W
as a Hecke operator with two distinct eigenvalues, as Jimbo's Ř does on ℚ³⊗ℚ³, it would appear above
as a non-scalar W-preserving element. None exists over ℚ(q). So, for generic q, **no element of the
quantum-G₂ braid algebra on V₇⊗V₇ restricts to the tower's crossing on the colour triplet**, whatever
the value of q_{g₂}, including q₀^{1/3}. This upgrades §8 (b) from "four rational points, U_q(n⁺)
only" to a statement over ℚ(q) for the whole intertwiner algebra.

**Scope.** (b) for the statement over ℚ(q), i.e. generic q. Specialisation to a particular q₀ can
only enlarge the W-preserving subspace at finitely many q, and is not claimed. No Lean.
