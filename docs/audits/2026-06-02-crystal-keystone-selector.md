# Crystal (Kashiwara / Option-E) selector test of the keystone (2,1)-multiplicity section

**Date:** 2026-06-02
**Branch:** `claude/crystal-keystone-selector-2026-06-02` (PR #1703)
**Trigger:** Author directive "explore Option-E/Kashiwara crystal selector" after
both non-fit escapes (Escape 2 native-5-strand #1694, Escape 1
geometric/holonomy #1699) closed, and the SU(2)-spin selector (#1687) closed —
all separate-not-select. This is the THIRD and final structural selector test of
the keystone arc.
**Compute:**
[`crystal_keystone_selector.py`](../../computations/crystal_keystone_selector.py),
witness
[`crystal-keystone-selector.witness.json`](../../computations/crystal-keystone-selector.witness.json)
(audit-only; exact integer / SYT / partition-transpose combinatorics + RAW
q-contents @ the canonical `compute_dps`; 10 assertions pass). **No tuning to
h⁴ = −3/4, m_n − m_p, B_AME, spin, or hypercharge.** Reuses the validated
`crystal_basis.py` Kashiwara primitives and #1687's SYT chains.

---

## VERDICT (one line)

**CASE (ii) — the Kashiwara / lower-global crystal SEPARATES but does NOT SELECT.
The Lusztig bar involution (`q → q⁻¹`, equivalently JM content `c → −c`) maps the
(2,1)-multiplicity space `V_λ` to `V_{λᵀ}` (the transpose block), so it is an
*endomorphism* of `V_λ` only when `λ` is self-conjugate. The non-self-conjugate
m=2 cases `(3,2)` and `(2,2,1)` are a TRANSPOSE PAIR — the bar maps one mult space
to the other, distinguishing no line in either. The only self-conjugate m=2 case
`(3,1,1)` has its bar act as an endomorphism that SWAPS its two copies
(`(2,−2) ↔ (−2,2)`) with NO bar-fixed OV vector (no content tuple equals its own
negation). Hence NO `V_λ` carries a bar-fixed distinguished line: the crystal
canonical basis = the OV/JM basis of #1687 — NO new selection. The crystal JOINS
spin (#1687) and geometry (#1699): all three SEPARATE, none SELECT. KEYSTONE
STANDS — the section is a genuine new physical input (triple-confirmed). `h⁴ = −3/4`
is a block invariant; no fit performed.**

---

## 0. A first-pass error, caught and corrected (discipline note)

This was flagged up front as the highest re-pitch-risk probe of the session, and
the first implementation produced a FALSE positive — verdict (i), "crystal
SELECTS" — exactly the predicted fit-trap shape. The error was **testing the
wrong object**: it Schützenberger-evacuated the full 5-box SYT of `S^{λ⁵}` and
recorded coincidental fixed-points of that *whole-tableau* involution as
"selection". Those fixed-points are unrelated to selecting a line in the
*multiplicity space*: full-SYT evacuation scrambles the `H₁⊂H₂⊂H₃` prefix and
does not preserve the `(2,1)` sub-object, so its fixed-points are an artifact.

The corrected test acts on the genuine object — the **(2,1)-multiplicity space**
`V_λ = Hom_{H₃}((2,1), Res^{H₅}_{H₃} S^{λ⁵})`, whose OV basis is the two
upper-chains — and computes the bar at the JM-**content** level (exact,
convention-free). That gives the honest, expected (ii). The episode is recorded
here precisely because a clean (i) "closes the keystone" and must survive ruthless
scrutiny; the first (i) did not.

## 1. The object, re-pinned (Task 1)

The keystone's missing object is a canonical **section** — a forced 1-dimensional
sub-line — of the multiplicity space

$$
  V \;:=\; \operatorname{Hom}_{S_3}\!\bigl((2,1)_{\mathrm{std}},\; \operatorname{Res}^{A_5}_{S_3}(H)\bigr) \;\cong\; \mathbb{C}^2,
$$

equivalently (the Hecke side, where the crystal actually lives — `A₅` itself is
not a type-A Weyl group and carries no Kashiwara crystal) the multiplicity space
of `(2,1)` in `Res^{H₅}_{H₃}`. Its OV/JM content-eigenbasis is the
`(2,0)/(0,2)` symmetric pair (#1687). The three m=2 cases, with their OV content
tuples `(c₄,c₅)` RAW:

| `λ ⊢ 5` | copy 1 `(c₄,c₅)` | copy 2 `(c₄,c₅)` |
|---|---|---|
| `(3,2)` | `(2,0)` | `(0,2)` |
| `(3,1,1)` | `(2,−2)` | `(−2,2)` |
| `(2,2,1)` | `(0,−2)` | `(−2,0)` |

## 2. The crystal structure on V (Task 2)

The canonical basis vector of each copy is its standard tableau / its `B((2,1))`
crystal component. Reusing the validated `crystal_basis.py` (Kashiwara `f_i/e_i`
via the signature rule, cross-checked against the Weyl dimension formula), the
`sl₃` crystal `B((2,1))` has a **unique highest-weight vector** (assertion
`B_2_1_sl3_unique_highest_weight_vector = 1`). Crucially, **both** copies are
isomorphic `B((2,1))` components, each with its **own** unique highest-weight
vector — so "a crystal component has a unique highest weight" does NOT by itself
distinguish the two copies. A genuine selection requires a bar-asymmetry
*between* them.

## 3. THE TEST — the bar involution on the multiplicity space (Task 3)

The Lusztig **bar involution** is `q → q⁻¹`. On the JM eigenvalue
`[c]_q = (q^c − q^{−c})/(q − q^{−1})` it acts by `[c]_{q⁻¹} = −[c]_q`, i.e.
**content negation** `c → −c` on every box. Negating the contents of an entire
upper-chain sends it to a chain of the **conjugate (transpose)** shapes, so the
bar maps the (2,1)-multiplicity space of `S^{λ⁵}` to that of `S^{(λ⁵)ᵀ}`:

$$
  \overline{(\;\cdot\;)} : V_\lambda \;\longrightarrow\; V_{\lambda^{\mathsf T}}.
$$

Verified RAW (assertion `bar_maps_each_V_lam_to_V_lamT = 1`):
`negate(contents(V_λ)) == contents(V_{λᵀ})` in all three cases.

**The selection criterion.** A crystal/bar SELECTS a distinguished line in a
*fixed* `V_λ` iff the bar is an **endomorphism** of `V_λ` (i.e. `λ = λᵀ`) AND has
a **bar-fixed OV basis vector** (a distinguished self-conjugate line). The
computation:

| `λ ⊢ 5` | `λᵀ` | self-conj? | bar endo of `V_λ`? | bar action | bar-fixed line? |
|---|---|---|---|---|---|
| `(3,2)` | `(2,2,1)` | no | **no** | maps `V_{(3,2)} → V_{(2,2,1)}` | — |
| `(3,1,1)` | `(3,1,1)` | **yes** | **yes** | **SWAPS** `(2,−2) ↔ (−2,2)` | **none** |
| `(2,2,1)` | `(3,2)` | no | **no** | maps `V_{(2,2,1)} → V_{(3,2)}` | — |

- For the non-self-conjugate cases `(3,2)` and `(2,2,1)` (a transpose pair), the
  bar is **not even an endomorphism** of `V_λ` — it maps one block's mult space to
  the other's. No intra-`V_λ` line can be bar-distinguished.
- For the only self-conjugate m=2 case `(3,1,1)`, the bar IS an endomorphism and
  **swaps the two copies** (assertion
  `self_conjugate_case_bar_swaps_two_copies = 1`), with NO bar-fixed OV vector
  (assertion `self_conjugate_case_has_no_bar_fixed_OV_line = 0`) — because no
  content tuple equals its own negation (`(2,−2) ≠ (−2,2)`).

Therefore **no `V_λ` carries a bar-fixed distinguished line** (assertion
`any_V_lam_has_bar_fixed_distinguished_line = 0`). The crystal SEPARATES (it
confirms the OV/JM canonical basis — the very basis #1687 already has) but does
NOT SELECT.

This is **separation without selection** — the exact distinction the spinor audit
#1687 drew and the geometry audit #1699 reused.

## 4. Falsification (Task 5) — not performed, by discipline

Because §3 forces **no** distinguished line, there is no derived section to test
against `h⁴ = −3/4` (assertion `no_h4_fit_performed`; witness
`task4_h4_falsification.fit_performed = false`). Choosing a crystal convention /
orientation / Demazure window to make a line appear (and land `−3/4`) would be
exactly the §7b / 2026-05-30-KLR-dialog fit trap. `h⁴ = −3/4` remains the RAW
invariant of the **(2,1) block itself**, a block invariant not a per-copy quantity
(#1687), so even a distinguished copy would carry the same `h⁴`. No closure, no
fit.

## 5. Why (ii), not (i) or (iii)

- **Not (i)** (crystal forces a derived section). (i) would require a bar-FIXED OV
  line in a fixed `V_λ`. For non-self-conjugate `λ` the bar isn't an endomorphism
  of `V_λ`; for the self-conjugate `(3,1,1)` the bar swaps the two copies with no
  fixed OV vector. No distinguished line exists.
- **Not (iii)** (no crystal structure on V). The crystal DOES act: each copy is a
  canonical-basis vector / a `B((2,1))` component, and the bar involution acts
  (mapping `V_λ → V_{λᵀ}`, and within the self-conjugate case swapping the
  copies). The structure exists; it just fails to SELECT a line within any `V_λ`.
- **(ii)** is the honest classification: structure (a canonical basis + a bar
  involution) without selection.

## 6. The triple-confirmed delimitation

With the SU(2)-spin selector (#1687), the icosahedral-geometry selector (#1699),
and now the Kashiwara-crystal selector (this audit) ALL giving **separation, not
selection**, the named structural routes past the vertical obstruction are
exhausted.

> **Delimitation (final form).** The missing object — the canonical **section** /
> vertical **baryon-number charge** of the (2,1)-multiplicity space — is **NOT
> derivable** from existing **categorical** structure (Hecke branching, OV/JM
> content eigenbasis, ribbon-twist spin, **Kashiwara crystal / Lusztig bar
> involution**) **OR** existing **geometric** structure (icosahedral A₅ holonomy,
> Bring color-tube cross-ratio). It is **definitively a genuine new physical
> input**: a forced nominator of the physical copy that none of the representation
> theory, the icosahedral rigidity, or the crystal/bar structure supplies.

The crystal was the strongest remaining candidate — the canonical basis is
distinguished by construction and a crystal component has a unique highest-weight
vector. The reason it still fails: those distinguishing features live at the level
of the **individual irreducible** `B((2,1))` (each copy has its own), not at the
level of the **multiplicity index** that the section must choose. The only crystal
structure that *acts on the multiplicity index* — the bar involution — either
leaves `V_λ` entirely (transpose pair) or swaps the copies (self-conjugate),
never fixing a line.

## 7. What this audit does and does not claim

- **Does** re-pin, RAW, the (2,1)-multiplicity space `V ≅ ℂ²` and its OV/JM
  content basis (the `(2,0)/(0,2)` symmetric pair), reusing #1687's SYT chains.
- **Does** put the Kashiwara crystal structure on it (validated `crystal_basis.py`
  primitives): each copy is a `B((2,1))` component with a unique highest-weight
  vector.
- **Does** compute, RAW and exactly, the Lusztig bar (`q → q⁻¹`, content `c → −c`)
  on the multiplicity space and prove it maps `V_λ → V_{λᵀ}`; the only
  self-conjugate m=2 case `(3,1,1)` has its bar swap the two copies with no
  bar-fixed line.
- **Does** prove the forced-selection test FAILS in every m=2 case: no `V_λ` has a
  bar-fixed distinguished line — the crystal separates but does not select.
- **Does** classify the result as **(ii)** and state the triple-confirmed
  delimitation.
- **Does** record (and correct) a first-pass (i) false positive caused by testing
  the wrong object (whole-SYT evacuation vs the multiplicity-space bar).
- **Does NOT** propose, fit, or tune any line, crystal convention, orientation,
  Demazure window, spin, content, or normalization; `h⁴ = −3/4`, m_n − m_p,
  B_AME, hypercharge are falsification references only; no per-copy `h⁴` assigned
  (would be a fit).
- **Does NOT** re-derive any known-dead re-pitch — the purged `λ_scale`
  mass-formula and the Bloch-Wigner / dilog-on-the-non-hyperbolic-trefoil
  arguments (2026-05-30 KLR-dialog assessment) do not appear.
- **Does NOT** wire to production; does NOT advance L2 numerically; does NOT
  discharge any Lean `sorry`. No LP/SDP solve appears (no dual emission required).

---

## Cross-references

- The keystone synthesis (the structural candidate this audit tests):
  [`2026-06-02-young-lattice-gauge-synthesis.md`](2026-06-02-young-lattice-gauge-synthesis.md)
  (#1691).
- The precise missing object (canonical section; OV/JM basis exists) and the
  separation-vs-selection distinction this audit reuses:
  [`2026-06-02-su2-spinor-multiplicity-resolution.md`](2026-06-02-su2-spinor-multiplicity-resolution.md)
  (#1687).
- The geometric selector that also separates-not-selects:
  [`2026-06-02-escape1-geometric-holonomy-section.md`](2026-06-02-escape1-geometric-holonomy-section.md)
  (#1699).
- The mult-2 Hom-space source (`Res^{A₅}_{S₃}(H) = triv ⊕ 2·(2,1)`):
  [`2026-06-02-h5-h3-functor-keystone.md`](2026-06-02-h5-h3-functor-keystone.md)
  (#1684).
- The validated Kashiwara primitives reused here:
  [`crystal_basis.py`](../../computations/crystal_basis.py).
- The discipline guardrails (re-pitch failure modes; §7b authoring-guidance
  framing): [`2026-05-30-klr-dialog-assessment.md`](2026-05-30-klr-dialog-assessment.md);
  CLAUDE.md §7b; the Δ_λ gate warning.
- The `h⁴ = −3/4` block invariant (falsification reference):
  [`borromean_h3_2_1_irrep_derivation.py`](../../computations/borromean_h3_2_1_irrep_derivation.py).
- Lusztig bar / Schützenberger evacuation realizing it on type-A canonical bases:
  Lascoux–Leclerc–Thibon 1995; Lusztig 1990; Kashiwara 1991.
