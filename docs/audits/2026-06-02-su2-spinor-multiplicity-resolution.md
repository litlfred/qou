# SU(2) spinor structure and the keystone (2,1) multiplicity: a canonical eigenbasis exists, but spin separates without selecting

**Date:** 2026-06-02
**Branch:** `claude/su2-spinor-multiplicity-resolution-2026-06-02` (PR #1687)
**Scope:** Does the Gelfand–Tsetlin / Jucys–Murphy / Okounkov–Vershik canonical
eigenbasis — and specifically the SU(2) spinor (ribbon-twist `θ_j = q^{j(j+1)}`)
structure — resolve the keystone (2,1)-multiplicity that audit #1684
([`2026-06-02-h5-h3-functor-keystone.md`](2026-06-02-h5-h3-functor-keystone.md),
PR #1684) found has multiplicity {1,2} in `Res^{H₅}_{H₃}`, concluding "no
canonical basis vector"? Author-steered follow-up: #1684's nonexistence may be
too strong, since OV theory gives a canonical content-eigenbasis of the
multiplicity space, and #1683's twist ladder assigns the baryon block (2,1) the
spin `j = ½`.
**Compute:**
[`su2_spinor_multiplicity_resolution.py`](../../computations/su2_spinor_multiplicity_resolution.py),
witness
[`su2-spinor-multiplicity-resolution.witness.json`](../../computations/su2-spinor-multiplicity-resolution.witness.json)
(audit-only, exact integer/rational SYT-chain combinatorics + RAW q-contents
@ 60 dps at the substrate `q₀`, 11 assertions pass). **No tuning to h⁴ = −3/4,
m_n − m_p, B_AME, spin, or hypercharge.** Every content and spin is computed
FIRST from the GT chain; the comparison to h⁴ comes SECOND.

---

## VERDICT (one line)

**CASE (ii) — SHARPENED, not overturned. The Okounkov–Vershik content
eigenbasis EXISTS: the Jucys–Murphy content tuple separates the two copies of
(2,1) in every multiplicity-2 case, so #1684's "no canonical basis vector" is
REFUTED — the multiplicity space DOES have a canonical content-eigenbasis. The
SU(2) spinor / ribbon-twist spin also has a SIMPLE spectrum on each
multiplicity-2 space (the two copies carry distinct intermediate-`H₄` spins), so
spin SEPARATES the copies. But spin does NOT canonically SELECT one copy: there
is NO single spin value distinguished consistently across the three `λ ⊢ 5`
multiplicity-2 spaces (the copy-spins are `{0,1}`, `{½,1}`, `{0,½}` — empty
intersection), and the literal "(2,1) is spin-½" datum is CONSTANT across every
copy so cannot separate anything. Selecting a copy by choosing a spin value
would be a fit (and would not even be self-consistent across `λ`). Therefore:
the keystone gains a canonical eigenbasis (refining #1684), but the PHYSICAL
selection of the h⁴ = −3/4 carrier remains open — spin labels the copies, it
does not nominate one.**

---

## 1. TASK 1 — Jucys–Murphy / content resolution (Okounkov–Vershik)

A **GT basis vector** of the (2,1)-multiplicity space inside `S^{λ}` (`λ ⊢ 5`)
under `Res^{H₅}_{H₃}` is a standard-Young-tableau **upper chain**

```
(2,1) = λ⁽³⁾  ⊂  λ⁽⁴⁾  ⊂  λ⁽⁵⁾ = λ ,     λ⁽ᵏ⁾ ⊢ k,
```

i.e. a way of adding one box at the `H₃→H₄` step and one at the `H₄→H₅` step.
The number of such chains equals the restriction multiplicity (branching duality:
forward add-box count = backward remove-box count), reproducing #1684's vector
`[0,1,2,2,2,1,0]` exactly. The **Jucys–Murphy element** `X_k` acts diagonally on
the GT vector with eigenvalue the **q-content** `[c]_q = (q^c − q^{−c})/(q − q^{−1})`
of the box added at step `k`, where `c = col − row` (Murphy / Ram, q-seminormal
form). The Okounkov–Vershik theorem says the content tuple `(c₄, c₅)` **uniquely
labels** each GT vector.

Per copy, RAW at `q₀ ≈ 1.10998` (60 dps; truncated display):

| `λ ⊢ 5` | m | copy `λ⁽⁴⁾` | box₄ (r,c) | `c₄` | `[c₄]_q` | box₅ (r,c) | `c₅` | `[c₅]_q` |
|---|---|---|---|---:|---|---|---:|---|
| (4,1) | 1 | (3,1) | (0,2) | 2 | 2.010896… | (0,3) | 3 | 3.043706… |
| (3,2) | 2 | (3,1) | (0,2) | 2 | 2.010896… | (1,1) | 0 | 0 (exact) |
|       |   | (2,2) | (1,1) | 0 | 0 (exact) | (0,2) | 2 | 2.010896… |
| (3,1,1) | 2 | (3,1) | (0,2) | 2 | 2.010896… | (2,0) | −2 | −2.010896… |
|         |   | (2,1,1) | (2,0) | −2 | −2.010896… | (0,2) | 2 | 2.010896… |
| (2,2,1) | 2 | (2,2) | (1,1) | 0 | 0 (exact) | (2,0) | −2 | −2.010896… |
|         |   | (2,1,1) | (2,0) | −2 | −2.010896… | (1,1) | 0 | 0 (exact) |
| (2,1,1,1) | 1 | (2,1,1) | (2,0) | −2 | −2.010896… | (3,0) | −3 | −3.043706… |

**Reading.** In every multiplicity-2 space the two content tuples are distinct
(they are the two orderings of the same pair, e.g. `(2,0)` vs `(0,2)`), so the
JM spectrum is simple and the OV content eigenbasis exists. Witness assertion
`ov_content_separates_all_multiplicity_spaces = 1`. **This refines #1684**: the
Hom-space `Hom_{H₃}((2,1), Res λ)` is not just an abstract ≥2-dimensional space
with "no canonical basis vector" — it has the canonical OV content-eigenbasis,
the same basis the whole derivation chain already uses for `tr_M`.

---

## 2. TASK 2 — Spin labels per copy (ribbon twist `θ_j = q^{j(j+1)}`)

Per #1683 ([`2026-06-02-u1-hypercharge-assignment.md`](2026-06-02-u1-hypercharge-assignment.md))
the SU(2)_q spin of a Wedderburn block is `j = (λ₁ − λ₂)/2` (the leading
two-row content the twist ladder evaluates), giving `(2)→1, (1,1)→0, (3)→3/2,
(2,1)→½, (1³)→0` — all five reproduced (assertions `spin_ladder_*`). The ribbon
twist `θ_j = q^{j(j+1)}` is the Reshetikhin–Turaev framing element with the
SU(2)_q Casimir `j(j+1)` in the exponent.

Two distinct spin data per copy:

- **Final-block spin** = `j((2,1)) = ½` → `θ_½ = q^{3/4} ≈ 1.081399…`.
  **CONSTANT across every copy** (assertion
  `final_2_1_block_spin_constant_one_half = 1`). This is the literal "the baryon
  is spin-½" datum — and it is the SAME for all copies, so it cannot separate
  anything.
- **Intermediate-`H₄`-block spin** = `j(λ⁽⁴⁾)`, which DIFFERS between copies:

| `λ ⊢ 5` | copy `λ⁽⁴⁾` | `j(λ⁽⁴⁾)` | `θ_{j(λ⁽⁴⁾)}` @ q₀ |
|---|---|---:|---|
| (3,2) | (3,1) / (2,2) | 1 / 0 | 1.232052… / 1 |
| (3,1,1) | (3,1) / (2,1,1) | 1 / ½ | 1.232052… / 1.081399… |
| (2,2,1) | (2,2) / (2,1,1) | 0 / ½ | 1 / 1.081399… |

**The two copies DO carry different spin** — but only at the intermediate-`H₄`
level, not at the (2,1) final-block level.

---

## 3. TASK 3 — THE TEST: does spin canonically SELECT one copy?

The decisive distinction (the fit epicenter): **separation ≠ selection.** A
simple spectrum (each copy a distinct eigenvalue) is necessary but NOT
sufficient for a canonical section. To SELECT one copy as "the ℓ=2 / h⁴
carrier" you need a FORCED rule that nominates a distinguished spin value
**consistently across every** `λ`.

- **Simple spectrum (separation): YES.** The intermediate-`H₄` spin separates
  the two copies in all three m=2 spaces (assertion
  `intermediate_H4_spin_simple_on_all_m2_spaces = 1`), in lockstep with the OV
  content separation (assertion `content_simple_on_all_m2_spaces = 1`).
- **Global canonical selector: NO.** The intermediate-spin sets are
  `{0,1}` (for (3,2)), `{½,1}` (for (3,1,1)), `{0,½}` (for (2,2,1)). Their
  intersection is **empty** — there is no spin value present in every m=2 space
  that could canonically pick "one copy". Assertion
  `global_canonical_spin_selector_exists = 0`. The same `j=1` is a copy in two
  spaces but absent from the third; `j=½` and `j=0` likewise. Choosing "always
  take the `j=1` copy" (or any fixed value) is both a fit AND ill-defined (it
  picks no copy in (2,2,1)).

**Verdict code (ii)** (witness `task3_verdict_code = "ii"`): spin SEPARATES
(simple spectrum) but does NOT canonically SELECT (no forced global selector).
The canonical eigenbasis exists via the full GT/JM algebra; **spin alone is
insufficient** for the physical selection.

Why not (i): (i) would require a forced global spin selector, which is empty.
Why not (iii): (iii) would require copies to SHARE a spin (no separation), but
the spectra are simple. The answer sits squarely at (ii).

---

## 4. TASK 4 — Falsification (h⁴ = −3/4), with fit-flag

The Borromean `h⁴ = −3/4` is an **invariant of the (2,1) block itself**
(computed in
[`borromean_h3_2_1_irrep_derivation.py`](../../computations/borromean_h3_2_1_irrep_derivation.py)),
not a per-copy quantity. JM/spin select **which copy of the (2,1) block embeds**
into a given `λ ⊢ 5`; they do not assign different `h⁴` values to different
copies. There is therefore **no forced rule** by which a single selected copy
"carries" a distinct `h⁴`:

- Since spin gives no canonical selection (Task 3, verdict ii), there is no
  forced copy to test against `h⁴` in the first place.
- Assigning a per-copy `h⁴` by choosing a spin/content value to reproduce `−3/4`
  would be exactly the fit the discipline review catches. **Not performed**
  (assertion `no_h4_fit_performed`; witness `task4_h4_falsification.fit_performed
  = false`).

So the falsification step returns **no derived closure and no fit**: `h⁴ = −3/4`
remains the block's RAW invariant; the keystone selection problem is not closed
by spin.

---

## 5. What this means for #1684

| #1684 claim | This audit |
|---|---|
| "`Hom(fiber,(2,1))` is a multiplicity space with **no canonical basis vector**." | **Refined / partially refuted.** The multiplicity space HAS the canonical **Okounkov–Vershik content eigenbasis**; the JM content tuple separates the copies (Task 1). |
| Multiplicities `{0,1,2}`, vector `[0,1,2,2,2,1,0]`. | **Confirmed** (reproduced exactly via forward SYT add-box chains). |
| "Any normalization that hits −3/4 is a fit." | **Confirmed and sharpened.** Even WITH the canonical eigenbasis and the SU(2) spin labels, there is no FORCED rule selecting one copy: spin separates but does not select (empty global selector), so the h⁴ carrier is still chosen, not derived. |

**Net:** #1684's nonexistence is **SHARPENED, not overturned**. The precise
statement upgrades from "no canonical basis" to:

> The (2,1)-multiplicity space in `Res^{H₅}_{H₃}` carries a canonical
> Okounkov–Vershik content eigenbasis (JM contents separate the copies), and
> the SU(2)_q ribbon-twist spin has a simple spectrum on it (intermediate-`H₄`
> spins separate the copies). But neither datum **canonically selects** a single
> copy as the h⁴ = −3/4 carrier: the (2,1)-block spin is constant (½) across
> copies, and the separating intermediate spins admit no globally consistent
> distinguished value (`{0,1} ∩ {½,1} ∩ {0,½} = ∅`). The physical selection
> rule is the missing object — a canonical SECTION of the content/spin
> eigenbasis, not a canonical BASIS (which now exists).

This is consistent with #1683's separate finding that `θ_j = q^{j(j+1)}` is a
spin/Casimir ladder (monotone, no sign change) — a labelling structure, not a
selection structure.

---

## 6. The missing object (what a real selection would be)

The refined obstruction is a **canonical section** of the OV eigenbasis: a
forced rule `λ ↦ (one distinguished copy)` that is natural in `λ`. Candidates a
follow-up could test (each must be FORCED, not fitted):

1. **A geometric / holonomy datum** (per #1684 reframe 1): the icosahedral
   fiber's holonomy acting on the color-tube cubic (flavor-cusp audit) could
   pick a copy via a cross-ratio, NOT via a Hecke label. This would resolve the
   selection without a categorical selector.
2. **A second crossing/trace charge** (per #1683's "missing second charge"):
   the baryon-number / color-trace invariant `B` that #1683 named as the missing
   object for `Y` could ALSO be the missing selector here — a per-copy `B` value
   forced by the trace would nominate a copy. This unifies the two open objects.
3. **Markov-destabilization native level** (per #1684 reframe 2): if the baryon
   is natively 5-strand, the h⁴ lives at the 5-strand level and the
   "select a 3-strand copy" question dissolves (the `z²` destabilization is
   blocked for the Brunnian Borromean — census §3a).

None is pursued here; each is a distinct testable hypothesis, and each must be
DERIVED, never fitted to `−3/4`.

---

## 7. What this audit does and does not claim

- **Does** compute, RAW and exactly, the OV content eigenbasis of the
  (2,1)-multiplicity space (JM q-contents per GT chain at `q₀`), and verify the
  content tuple separates the copies in every multiplicity-2 case.
- **Does** compute the ribbon-twist spin `θ_j = q^{j(j+1)}` per copy (final
  block ½, constant; intermediate `H₄` spin, separating), cross-checked against
  the #1683 twist ladder.
- **Does** prove (RAW) that spin SEPARATES but does NOT canonically SELECT: no
  global spin selector (`{0,1} ∩ {½,1} ∩ {0,½} = ∅`); final-block spin constant.
- **Does** classify the result as case **(ii)** and sharpen #1684 from "no
  canonical basis" to "canonical eigenbasis exists, canonical section does not".
- **Does NOT** propose, fit, or tune any selection, spin value, content, or
  normalization; `h⁴ = −3/4`, m_n − m_p, hypercharge are falsification
  references only; no per-copy `h⁴` assigned (would be a fit).
- **Does NOT** wire to production; does NOT advance L2 numerically; does NOT
  discharge any Lean `sorry`. No LP/SDP solve appears (no dual emission
  required).

---

## Cross-references

- The keystone this audit refines:
  [`2026-06-02-h5-h3-functor-keystone.md`](2026-06-02-h5-h3-functor-keystone.md)
  (PR #1684) — the `[0,1,2,2,2,1,0]` restriction vector, the nonexistence theorem.
- The twist ladder + (2,1)→j=½ spinor datum:
  [`2026-06-02-u1-hypercharge-assignment.md`](2026-06-02-u1-hypercharge-assignment.md)
  (PR #1683) — `θ_j = q^{j(j+1)}`, the "missing second charge" framing.
- SU(2) = ribbon-twist double cover; spin-ℤ₂ ≠ sign-ℤ₂; the ℓ=2 fiber:
  [`2026-06-01-s5-so3-su2-u1-fiber-action.md`](2026-06-01-s5-so3-su2-u1-fiber-action.md)
  (PR #1672).
- The (2,1) block h⁴ = −3/4 falsification reference:
  [`borromean-markov-trace-closed-form.md`](../../content/quantum-observable-universe/mass-theory/borromean-markov-trace-closed-form.md),
  [`borromean_h3_2_1_irrep_derivation.py`](../../computations/borromean_h3_2_1_irrep_derivation.py).
- Okounkov–Vershik / Jucys–Murphy seminormal form: standard (Okounkov–Vershik
  1996; Murphy 1981; Ram q-deformation) — the JM content tuple labels the GT
  basis uniquely.
