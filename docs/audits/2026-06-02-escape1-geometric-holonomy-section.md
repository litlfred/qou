# Escape 1 (geometric / icosahedral-holonomy section): does A₅ geometry force a canonical (2,1)-section, or only separate it?

**Date:** 2026-06-02
**Branch:** `claude/escape1-geometric-holonomy-section-2026-06-02` (PR #1699)
**Trigger:** Author directive "run Escape 1" after Escape 2 (native-5-strand) was
falsified (#1694). Tests the first of the two non-fit escapes named by the
Young-lattice synthesis
([`2026-06-02-young-lattice-gauge-synthesis.md`](2026-06-02-young-lattice-gauge-synthesis.md),
#1691) and the spinor-resolution audit
([`2026-06-02-su2-spinor-multiplicity-resolution.md`](2026-06-02-su2-spinor-multiplicity-resolution.md),
#1687): the canonical **section** of the (2,1)-multiplicity space, if it exists,
comes from GEOMETRIC structure outside Hecke rep theory — the icosahedral A₅
holonomy / Bring color-tube cross-ratio acting on the dim-5 ℓ=2 fiber.
**Scope:** Does the icosahedral geometry FORCE a canonical line (a section) in the
2-dim Hom-space, or does selecting a line still require a free parameter (a fit)?
**Compute:**
[`escape1_geometric_holonomy_section.py`](../../computations/escape1_geometric_holonomy_section.py),
witness
[`escape1-geometric-holonomy-section.witness.json`](../../computations/escape1-geometric-holonomy-section.witness.json)
(audit-only; exact permutation-group combinatorics + explicit numerical rep
matrices for the ℂ² realization + RAW golden-ratio cross-ratios @ the canonical
`compute_dps`; 15 assertions pass). **No tuning to h⁴ = −3/4, m_n − m_p, B_AME,
spin, or hypercharge.** The mult-2 Hom-space and every A₅/S₃ group-theoretic fact
is computed FIRST, RAW; the comparison to h⁴ comes LAST and only if a canonical
line is forced — which it is not.

---

## VERDICT (one line)

**CASE (ii) — the icosahedral A₅ geometry gives STRUCTURE but does NOT FORCE a
canonical section. It realizes the mult-2 Hom-space `V = Hom_{S₃}((2,1), Res^{A₅}_{S₃}(H)) ≅ ℂ²`
with the Okounkov–Vershik content eigenbasis (refining #1687), but the centralizer
`C_{A₅}(S₃) = {e}` and the normalizer `N_{A₅}(S₃) = S₃` (self-normalizing) are BOTH
trivial-modulo-S₃, so the ONLY A₅-forced operator on V is the scalar identity
(degenerate spectrum {1,1}, no distinguished eigenline). Geometry SEPARATES but
does NOT SELECT — exactly the spinor failure mode (#1687: separation YES, selection
NO). Selecting a line (a cross-ratio value, a holonomy phase) is a FREE parameter
⇒ fit. The keystone STANDS: Escape 1 fails the same way Escape 2 did
(relocation, not closure). h⁴ = −3/4 is a falsification reference only; no fit
performed.**

---

## 1. The object, pinned RAW (Task 1)

The keystone's missing object is a canonical **section** — a forced 1-dimensional
sub-line — of the multiplicity space

$$
  V \;:=\; \operatorname{Hom}_{S_3}\!\bigl((2,1)_{\mathrm{std}},\; \operatorname{Res}^{A_5}_{S_3}(H)\bigr) \;\cong\; \mathbb{C}^2,
$$

where `H` is the **dim-5 ℓ=2 irrep** of `A₅ ≅ I` (the icosahedral fiber carrier,
[`s5-so3 audit`](2026-06-01-s5-so3-su2-u1-fiber-action.md)) and
`S₃ = ⟨(123),(12)(45)⟩ ⊂ A₅` is the genuine order-6 color-sheet stabilizer
(the same S₃ the keystone Candidate 4 used,
[`h5-h3 keystone`](2026-06-02-h5-h3-functor-keystone.md)).

The probe realizes `H` **explicitly** (not just by character): the 10-dim
permutation rep of A₅ on unordered pairs decomposes as `triv ⊕ G(4) ⊕ H(5)`
(verified by inner products, each multiplicity 1), and the H-isotypic projector
`P_H = (5/60)·Σ_g χ_H(g)·ρ_pair(g)` has rank 5. Restricting these explicit 5×5
matrices to `S₃` gives a genuine 5-dim representation of `S₃` (homomorphism check
on the generators passes), with character per S₃-class `(e, 3-cycle, transposition)
= (5, −1, 1)`, hence

$$
  \operatorname{Res}^{A_5}_{S_3}(H) \;=\; \mathrm{triv} \;\oplus\; 2\cdot(2,1),
  \qquad \dim V = 2.
$$

(`mult triv = 1`, `mult sign = 0`, `mult (2,1) = 2`; the (2,1)-isotypic projector
has rank 4 = 2 copies × dim 2.) This reproduces, by explicit matrices, the
character count of the keystone Candidate 4. The OV/JM content eigenbasis of this
ℂ² is the one #1687 established (the content tuple separates the two copies).

## 2. The forced-geometry criterion (Task 2)

The decisive question is **what can act on V without a free parameter.** By
Schur's lemma, the endomorphism algebra of the (2,1)-isotypic component of `Res H`
is `M₂(ℂ)` acting on the ℂ² multiplicity index. An operator on V is **canonical /
forced** (basis-independent, dictated by the ambient A₅ geometry) iff it is the
image of a group element that

- **commutes** with the S₃-action — i.e. lies in the **centralizer** `C_{A₅}(S₃)`
  (a genuine endomorphism of the isotypic block), or
- **normalizes** S₃ — i.e. lies in `N_{A₅}(S₃)` and acts (semilinearly, via the
  induced S₃-automorphism) on the isotypic block, possibly **mixing the two
  copies**.

Computed RAW over the 60 elements of A₅:

| structure | result | order | meaning |
|---|---|---|---|
| `C_{A₅}(S₃)` (centralizer) | `{e}` | 1 | **trivial** — no forced endomorphism |
| `N_{A₅}(S₃)` (normalizer) | `S₃` | 6 | **self-normalizing** — `N/S₃` trivial |

Both are trivial-modulo-S₃. The centralizer being `{e}` means the only A₅-element
commuting with the whole S₃-action is the identity, which acts on V as the scalar
`1`. The normalizer equalling S₃ means **no A₅-element outside S₃** maps the
S₃-isotypic structure to itself — so there is no group element that mixes the two
(2,1)-copies (which is what a copy-selecting operator would have to do). Hence:

> The only A₅-forced operator on `V ≅ ℂ²` is the **scalar identity**, with
> degenerate spectrum {1,1}.

## 3. THE TEST — simple spectrum / unique invariant line? (Task 3)

The keystone needs a forced operator with a **simple spectrum** (distinct
eigenvalues ⇒ a unique invariant line ⇒ canonical section). The scalar identity
has a **degenerate** spectrum {1,1}: every line of ℂ² is invariant, so **no line
is distinguished.**

| property | result |
|---|---|
| forced non-scalar operator exists | **NO** (`C_{A₅}(S₃) = {e}`, `N/S₃` trivial) |
| forced operator spectrum simple | **NO** (only the scalar identity) |
| unique invariant line on V | **NO** (degenerate ⇒ all lines invariant) |
| **canonical section forced** | **NO** |

This is **separation without selection** — the exact distinction the spinor audit
#1687 drew. The icosahedral A₅ DOES produce the structured object `V = ℂ²` (with
the OV/JM content basis), so it separates the copies; but it supplies no forced
rule nominating one copy as the physical (2,1)/h⁴ carrier. Any such nomination is
an externally-chosen vector in ℂ² — a fit.

## 4. Cross-ratio / holonomy candidate — forced or free? (Task 4)

Could the **Bring color-tube cross-ratio** or an **icosahedral holonomy phase**
supply the selector instead of a group element? The probe records the standard
icosahedral special cross-ratios (golden-ratio rigidity) RAW: `φ`, `1/φ`, `1−φ`,
`φ²`, harmonic `−1`, equianharmonic `e^{iπ/3}` — **several** distinct A₅-special
values, the 12 icosahedron vertices forming an A₅-orbit on `ℂP¹`. None is a
forced selector of a line in V, for three reasons that compound:

1. **No derived cross-ratio → line map.** A holonomy/monodromy operator from the
   Bring covering would still have to act ON V, and any operator on V factors
   through `End_{S₃}(Res H)|_{(2,1)\text{-iso}} = M₂(ℂ)`, whose only A₅-forced
   element is the scalar (§2–§3). There is no derived assignment from a cross-ratio
   value to a non-scalar `M₂(ℂ)` element.
2. **The color-tube cross-ratio is knot-independent and p/n-blind.** The
   complex-fibre audit
   ([#1669](2026-06-01-complex-fibre-cross-ratio.md)) showed `Σ D(z_c) = 0`
   (conjugate-pair cancellation) for the universal color-tube cubic, and the
   flavor-cusp audit ([#1670](2026-06-01-flavor-dependent-cusp-shape.md)) showed
   proton and neutron share the same `ℬ₃` complement ⇒ identical shapes. The
   cross-ratio carries the absolute volume (a `K₃` datum), not a per-copy
   selection.
3. **"Which cross-ratio" is itself a free choice.** There are several icosahedral
   special values; picking one to select the line is a free modulus. **"The
   cross-ratio that gives h⁴" is THE fit** — exactly the latent fit the
   flavor-cusp audit flagged for the root-selection rule.

So the cross-ratio is a **free modulus** with respect to the section, not a forced
selector.

## 5. Falsification (Task 5) — not performed, by discipline

Because §3 forces **no** canonical line, there is no derived section to test
against `h⁴ = −3/4`. Assigning a line or a cross-ratio value to reproduce `−3/4`
would be exactly the fit the discipline review catches, so it is **not performed**
(witness `task5_h4_falsification.fit_performed = false`). `h⁴ = −3/4` remains the
RAW invariant of the **(2,1) block itself**
([`borromean_h3_2_1_irrep_derivation.py`](../../computations/borromean_h3_2_1_irrep_derivation.py)) —
a block invariant, not a per-copy quantity (#1687), so even a chosen copy would
not change it. No closure, no fit.

## 6. Why (ii), not (i) or (iii)

- **Not (i)** (geometry forces a derived section). (i) would require a forced
  non-scalar operator with simple spectrum / unique invariant line. The
  centralizer and normalizer/S₃ are both trivial, so the only forced operator is
  the scalar identity — no such structure exists.
- **Not (iii)** (no geometric structure on V). The geometry DOES act: A₅ realizes
  `V = ℂ²` and S₃ acts block-diagonally on it (each S₃-element acts within each
  (2,1)-copy as the same (2,1)-matrix). The structure exists; it just fails to
  SELECT a line.
- **(ii)** is therefore the honest classification: structure without selection.

## 7. The delimitation — both escapes now fail

With Escape 2 (native-5-strand) falsified (#1694: Brunnian-5 deletion → unlink ≠
B₃; S₅-braid Markov trace misses by 96.5%) and Escape 1 now failing the
forced-section test, the named non-fit routes past the vertical obstruction are
**both exhausted**. The synthesis #1691 listed exactly two geometric/structural
escapes plus the conjectural second-charge lead; this audit closes the geometric
one negatively.

> **Delimitation.** The missing object — the **vertical baryon-number charge** /
> canonical **section** of the (2,1)-multiplicity space — is **NOT derivable** from
> existing **categorical** structure (Hecke branching, OV/JM content eigenbasis,
> ribbon-twist spin) **OR** existing **geometric** structure (icosahedral A₅
> holonomy, Bring color-tube cross-ratio). It is a genuine **new physical input**:
> a forced nominator of the physical copy that neither the representation theory
> nor the icosahedral rigidity supplies.

This is a strong, valuable negative: it converts the keystone from "find the
missing functor/section in the existing structure" into "the section is a new
input" — sharpening the synthesis's vertical-obstruction statement to its final
form.

## 8. What this audit does and does not claim

- **Does** realize, RAW and explicitly (not just by character), the dim-5 ℓ=2 A₅
  irrep H, restrict it to the color-sheet S₃ ⊂ A₅, and pin
  `Res^{A₅}_{S₃}(H) = triv ⊕ 2·(2,1)`, `dim V = 2` (homomorphism + dim checks).
- **Does** compute, RAW over all 60 A₅ elements, `C_{A₅}(S₃) = {e}` and
  `N_{A₅}(S₃) = S₃` (self-normalizing) — establishing the only forced operator on
  V is the scalar identity (degenerate spectrum {1,1}).
- **Does** prove the forced-section test FAILS: no simple spectrum, no unique
  invariant line, no canonical section — geometry separates but does not select.
- **Does** record the icosahedral special cross-ratios RAW and argue (with the
  #1669/#1670 results) that the cross-ratio is a free modulus, not a forced
  selector.
- **Does** classify the result as **(ii)** and state the delimitation that, with
  Escape 2 already falsified, the missing object is a genuine new physical input.
- **Does NOT** propose, fit, or tune any operator, line, cross-ratio value,
  holonomy phase, spin, or normalization; `h⁴ = −3/4`, m_n − m_p, B_AME,
  hypercharge are falsification references only; no per-copy h⁴ assigned (would be
  a fit).
- **Does NOT** wire to production; does NOT advance L2 numerically; does NOT
  discharge any Lean `sorry`. No LP/SDP solve appears (no dual emission required).

---

## Cross-references

- The keystone synthesis (the two escapes named):
  [`2026-06-02-young-lattice-gauge-synthesis.md`](2026-06-02-young-lattice-gauge-synthesis.md)
  (#1691).
- The precise missing object (canonical section, OV/JM basis exists):
  [`2026-06-02-su2-spinor-multiplicity-resolution.md`](2026-06-02-su2-spinor-multiplicity-resolution.md)
  (#1687) — the separation-vs-selection distinction this audit reuses.
- The mult-2 Hom-space source (`Res^{A₅}_{S₃}(H) = triv ⊕ 2·(2,1)`):
  [`2026-06-02-h5-h3-functor-keystone.md`](2026-06-02-h5-h3-functor-keystone.md)
  (#1684, Candidate 4),
  [`h5_h3_functor_keystone.py`](../../computations/h5_h3_functor_keystone.py).
- The icosahedral A₅ fiber + the dim-5 ℓ=2 irrep:
  [`2026-06-01-s5-so3-su2-u1-fiber-action.md`](2026-06-01-s5-so3-su2-u1-fiber-action.md)
  (#1672).
- The Bring cross-ratio is p/n-blind / a free modulus:
  [`2026-06-01-complex-fibre-cross-ratio.md`](2026-06-01-complex-fibre-cross-ratio.md)
  (#1669),
  [`2026-06-01-flavor-dependent-cusp-shape.md`](2026-06-01-flavor-dependent-cusp-shape.md)
  (#1670).
- The h⁴ = −3/4 block invariant (falsification reference):
  [`borromean-markov-trace-closed-form.md`](../../content/quantum-observable-universe/mass-theory/borromean-markov-trace-closed-form.md),
  [`borromean_h3_2_1_irrep_derivation.py`](../../computations/borromean_h3_2_1_irrep_derivation.py).
- Escape 2 (falsified, for the both-escapes-fail delimitation): the native-5-strand
  probe (#1694).
