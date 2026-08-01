# qou-ujmw: A_ω = 3 is a DT/3d-index count — status synthesis + q→0 base-case Lean brick

**Date:** 2026-08-01 · **Bean:** `qou-ujmw` (G3 Stokes keystone, c₃-odd bridge) ·
**Branch:** `claude/ujmw-aomega-dt-index-derivation-2026-08-01` ·
**Tier:** synthesis + formalize-first (Lean, sorry-free) · **Scope:** (a);
nothing fitted; nothing wired to production; L2 unchanged.

## The task, and the honest headline

The bean asks to **derive the integer Stokes constant `A_ω = 3` as a
Donaldson–Thomas / 3d-index count** for the figure-eight `4₁` (the physics-content
leg of the c₃-odd gap), *rather than assuming it*. The corpus-first read shows the
premise is already partly met and localizes exactly what remains open.

**`A_ω = 3` is NOT an assumed value in the corpus — it is a DT/3d-index count,
computed exactly and certified.** What is still open is the *internal* derivation
of that integer from the QOU categorical drivers (as opposed to *importing* it
from Garoufalidis–Gu–Mariño's proven theorem for `4₁`), and the value→observable
normalization. This audit states the established chain precisely and adds one new,
machine-checked, unconditional piece: the **q→0 base case**.

## What the corpus already establishes (verified by corpus read)

1. **The `4₁` 3d-index is validated exactly.** The tetrahedron index passes its S₃
   triality self-test (49/49, `tetrahedron_index_triality_pin.py`), and the
   figure-eight index `I_{4₁}(0) = 1 − 2q − 3q² + 2q³ + 8q⁴ + …` reproduces GHHR
   Ex 4.1 exactly (`figure_eight_3d_index.py`,
   [`2026-07-18-figure-eight-3d-index-closed.md`](2026-07-18-figure-eight-3d-index-closed.md)).
   The rotated index `Ind_{4₁}(q) = Σ I_Δ(k₁,k₂)I_Δ(k₂,k₁) = 1 − 8q − 9q² + …` is
   the ground-truth object.
2. **The GGM Stokes data is implemented and internally certified.**
   `qbeta_g3_ggm_stokes_41.py` builds the eq-(59a) sandwich
   `S⁺ = ±½·A·W₋₁·B·W₋₁ᵀ·C` from the GGM q-series (Theorem 9: `det W_m = 2`,
   q-difference eq 49), reproducing the four printed towers (eq 61–64, 28
   coefficients) and the **q→0 limit `S⁺(0) = [[1,3],[0,1]]`** (eq 60). The
   off-diagonal is the integer **3**.
3. **`A_ω = 3` IS a DT invariant.** GGM Conjecture 2/4 (a **theorem** for `4₁`)
   identifies the Stokes constants with the rotated 3d-index / DT–BPS invariants
   of `T[4₁]`. The full off-diagonal Stokes-constant matrix (GGM eq 98) carries
   the invariants `{3, 4}`; the `−3` is the `(σ₃,σ₁)` DT entry
   ([`2026-07-18-aomega-stokes3-is-dt-invariant-not-tracefield-disc.md`](2026-07-18-aomega-stokes3-is-dt-invariant-not-tracefield-disc.md)).
   *(That audit refuted, scope-(a), the tempting identification of the `−3` with
   the trace-field discriminant `disc(ℚ(√−3)) = −3` — a `4` co-occurs, so the
   discriminant reading is a small-integer coincidence. Do not resurrect it.)*
4. **The distinguished reading is the symmetry constant, and it is exact.** The
   `4₁` Stokes matrix satisfies the exact integer q-series identities
   `S⁺₁₂(q) + S⁺₂₁(q) = 3·S⁺₁₁(q)` and `det S⁺(q) = 1` (GGM symmetry eq 65),
   certified coefficient-by-coefficient through q⁴⁰⁰
   (`qbeta_3bp8_w3_stokes_symmetry_constant.py`). `StokesSymmetryConstant.lean`
   (sorry-free) proves the *conditional* structural fact: **if** the symmetry
   holds with constant `c`, **then** the symmetry constant `(S₁₂+S₂₁)/S₁₁ = c` at
   *every* q — q-independence is forced, not accidental. The `A ≥ 2.054`
   ϑ-reality bound (`ThetaRealityBound.lean`) excludes the raw-entry reading.
5. **The rigidity leg (zero fitting freedom) is essentially closed.** The
   Faddeev–Volkov `uniqueUpToScalar` reduction is down to two named open inputs
   (`hibinv`, bean `qou-q95i`; `hratio` entireness/divisor-cancellation, bean
   `qou-2cvs`); the elliptic-Liouville and `hspan` inputs are proved sorry-free.

## What this PR adds — the q→0 base-case brick (Lean, sorry-free)

[`QOU/QBeta/StokesQZeroDTCount.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/StokesQZeroDTCount.lean),
`lean`-direct **exit 0**. A *decidable integer-matrix* computation of the
semiclassical limit, complementing the conditional `StokesSymmetryConstant`:

- At q→0 the GGM fundamental-solution matrix collapses to the exact integer matrix
  `W₋₁(0) = [[0,-2],[1,1]]` (q→0 of the certified `G⁰_m, G¹_m` series).
- `detW0` — `det W₋₁(0) = 2` (GGM Theorem 9 at q→0).
- `ggm_sandwich_qzero` — **every entry** of `A·W₋₁·B·W₋₁ᵀ·C` at q→0 equals
  `−2·S⁺(0)` with `S⁺(0) = [[1,3],[0,1]]`; hence `S⁺(0) = −½·(sandwich)`.
- `sandwich_offdiagonal_qzero` / `stokes_qzero_offdiagonal` — the off-diagonal
  DT/Stokes constant is exactly **3**.

**What the brick is (and is not).** It *reduces* "`A_ω = 3` at q→0" to the single
concrete input `W₋₁(0) = [[0,-2],[1,1]]` — a certified q→0 evaluation of the
GGM/DGG q-series — and closes the arithmetic from there by pure integer matrix
algebra. In the sense of GGM Conjecture 4 (a theorem for `4₁`), this off-diagonal
`3` **is** the rotated-3d-index / DT invariant. So the brick machine-checks the
DT-count identification at the semiclassical anchor: `A_ω = 3` is a *computed
count*, not an assumption.

It does **not** (anti-laundering, explicit):

- **derive `3` from the 13 QOU categorical drivers.** The `W₋₁(0)` input is
  GGM/DGG q-series data (a topological fact about `4₁`), not a Hecke/Wedderburn/
  Bring construction. Internal derivation stays open (below).
- **carry the q-dependence.** That `(S₁₂+S₂₁)/S₁₁ = 3` at *every* q is the
  companion conditional lemma; this brick is its unconditional q→0 base value.
- **close the value→observable normalization** (`Im 𝔙_q → N_odd`, magnitude
  `A′ ≈ 2.37`) — a separate open capstone (`qou-2cvs`,
  [`2026-07-25-aomega-normalization-one-instanton-map.md`](2026-07-25-aomega-normalization-one-instanton-map.md)).

## Verdict: reduced-to-named-sub-obstruction (not fully derived)

The integer identification `A_ω = 3` as a DT/3d-index count is **established** in
the corpus (imported from GGM's proven Conjecture 4 + internally certified through
q⁴⁰⁰), and this PR machine-checks its q→0 anchor unconditionally. The two genuinely
open legs are unchanged:

| open leg | precise sub-obstruction | bean |
|---|---|---|
| **Internal derivation of `3`** | derive the symmetry constant `3` (equivalently the `4₁` DT/BPS invariant) from the QOU categorical drivers — Hecke `H₃` / Bring / Wedderburn — rather than importing GGM's theorem. The `4₁` DT spectrum `{3,4}` (GGM eq 98) is the object; a `3`-from-`disc` shortcut is refuted (a `4` co-occurs). | `qou-qnnq` (+ this PR's `qou-ujmw`) |
| **Value normalization** | the map from the Stokes integer `3` to the observable amplitude `A′ ≈ 2.37` (one-instanton `Im 𝔙_q → N_odd`) | `qou-2cvs`, `qou-q95i` |

**Anti-numerology note for successors (a trap to avoid).** It is tempting to read
`3` as a bare topological count of `4₁` (three boundary-parabolic SL₂(ℂ)
connections `{σ₀,σ₁,σ₂}`; `|disc(ℚ(√−3))| = 3`; …). Every such single-knot match
is a small-integer coincidence until it is shown to hold *across knots* AND be
*structurally forced* — for `5₂` the geometric block is `3×3` (three σ's) and the
symmetry structure differs, so a "`A_ω = #connections`" rule is not supported and
must not be asserted. The DT spectrum is the object (GGM eq 98, Conjecture 4); a
discriminant/count identity is not the tool (the `−3`-vs-`disc` refutation already
recorded this).

## Discipline

Corpus-grep run over `A_omega|A_ω|3d.?index|donaldson.?thomas|stokes.*integer|peacock`
across `docs/audits/ docs/coordination/ content/ computations/`; this synthesizes the
existing chain (evidence base #3813; `3bp8` §4; the DT-invariant and normalization
audits) and adds one unconditional Lean brick — no new open-item declaration beyond
the two beans above, no refutation, nothing wired. Primary sources:
GGM [2012.00062](https://arxiv.org/abs/2012.00062) (eq 59a/60/65/98, Thm 9);
GHHR [1604.02688](https://arxiv.org/abs/1604.02688) (3d-index).

## Cross-references

- Lean: [`StokesQZeroDTCount.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/StokesQZeroDTCount.lean) (new), [`StokesSymmetryConstant.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/StokesSymmetryConstant.lean) (companion conditional).
- Probe: [`qbeta_g3_ggm_stokes_41.py`](../../computations/probes/qbeta_g3_ggm_stokes_41.py); witness [`aomega-qzero-dt-count.witness.json`](../../computations/aomega-qzero-dt-count.witness.json) (this PR).
- Audits: [`2026-07-18-g3-stokes-keystone-evidence-base.md`](2026-07-18-g3-stokes-keystone-evidence-base.md), [`2026-07-18-aomega-stokes3-is-dt-invariant-not-tracefield-disc.md`](2026-07-18-aomega-stokes3-is-dt-invariant-not-tracefield-disc.md), [`2026-08-01-3bp8-entirety-and-channel-correctness.md`](2026-08-01-3bp8-entirety-and-channel-correctness.md), [`2026-07-25-aomega-normalization-one-instanton-map.md`](2026-07-25-aomega-normalization-one-instanton-map.md).
- Ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md).
- AGENTS.md §"Axiomatization is NOT a Proof"; §"Before declaring refuted"; §"Strict Lean Discipline".
