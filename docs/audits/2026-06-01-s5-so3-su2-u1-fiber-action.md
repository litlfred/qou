# S₅ → SO(3) ≅ SU(2)/ℤ₂ × U(1) fiber action: deriving the geometric fiber map

**Date:** 2026-06-01
**Branch:** `claude/s5-so3-su2-u1-fiber-action-2026-06-01` (PR #1672)
**Scope:** The L2-keystone open step — the **geometric fiber map** of
`conj:s5-so3-fiber-action` (Lean class `BringFiberAction`). Three gauge
correspondences investigated: **SO(3)/h⁴**, **SU(2)/spin**, **U(1)/hypercharge**.
**Compute:**
[`s5_so3_su2_u1_fiber_action.py`](../../computations/s5_so3_su2_u1_fiber_action.py),
witness
[`s5-so3-su2-u1-fiber-action.witness.json`](../../computations/s5-so3-su2-u1-fiber-action.witness.json).
All RAW @ 60 dps, audit-only. **No tuning to h⁴=−3/4, m_n−m_p, spin, or
hypercharge.** The icosahedral character decomposition was computed FIRST;
the comparison to −3/4 came SECOND.

---

## VERDICT (one line)

**The geometric fiber map is NOT derivable from the current structure. The
icosahedral branching IS exactly derived (ℓ=2 → one copy of the dim-5 irrep
H of I), and the Borromean h⁴ = −3/4 IS reproduced raw, but THESE LIVE IN
TWO DIFFERENT GROUP ALGEBRAS (A₅⊂S₅ on 5 strands vs the S₃/H₃ Borromean
trace on 3 strands) and no canonical map links them. Worse, the conjecture's
load-bearing premise — "the S₃ truncation sees only ℓ≤1, so ℓ=2 is the NEW
thing the full SO(3) opens" — is FALSE: the (2,1)/std irrep that carries h⁴
already appears at BOTH ℓ=1 and ℓ=2 (multiplicities 1 and 2), so h⁴ cannot
be cleanly attributed to "ℓ=2 only". The SU(2) lift gives a genuine derived
structural result (the spin ℤ₂ is provably NOT the sign ℤ₂). The three
correspondences FACTOR — they do not unify into one fiber action. This is a
CLEAN NEGATIVE that sharpens the obstruction and corrects a false premise in
the source files.**

---

## Per-correspondence findings

### SO(3) / h⁴ — **OPEN** (multiplicities derived; the link is not)

**Derived (RAW, from the I≅A₅ character table — computed before any
comparison):** decomposing the SO(3) angular-momentum reps `V_ℓ` under the
icosahedral subgroup I ⊂ SO(3) (5 conjugacy classes E, 12C₅, 12C₅², 20C₃,
15C₂ at rotation angles 0, 2π/5, 4π/5, 2π/3, π; SO(3) character
`χ_ℓ(θ)=sin((2ℓ+1)θ/2)/sin(θ/2)`):

| ℓ | A(1) | T₁(3) | T₂(3) | G(4) | H(5) | Σdim | (2ℓ+1) |
|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 0 | 0 | 1 | 1 |
| 1 | 0 | **1** | 0 | 0 | 0 | 3 | 3 |
| 2 | 0 | 0 | 0 | 0 | **1** | 5 | 5 |
| 3 | 0 | 0 | 1 | 1 | 0 | 7 | 7 |
| 4 | 0 | 0 | 0 | 1 | 1 | 9 | 9 |
| 5 | 0 | 1 | 1 | 0 | 1 | 11 | 11 |
| 6 | 1 | 1 | 0 | 1 | 1 | 13 | 13 |

All integrality residuals < 10⁻¹⁴; all dim checks pass. This table is
EXACT and DERIVED. **ℓ=2 → exactly ONE copy of the dim-5 irrep H** (the first
ℓ at which H appears). So "ℓ=2 opens the dim-5 icosahedral irrep" is a true,
derived statement.

**Borromean falsification reference (RAW, reproduced exactly):** the
Markov-trace closed form
([`prop:borromean-markov-trace-closed-form`](../../content/quantum-observable-universe/mass-theory/borromean-markov-trace-closed-form.md))
`tr_M(β_Bor) = (4 + h² − 3h⁴ − h⁶)/(h²+4)` Taylor-expands to

```
  tr_M = 1 + 0·h²  − (3/4)·h⁴ − (1/16)·h⁶ + (1/64)·h⁸ + …
```

h² = 0 (confirmed), **h⁴ = −3/4** (confirmed raw). Per the source proof, all
correction terms originate from the **(2,1) standard irrep of S₃/H₃** alone.

**Why the link is NOT derived — TWO independent obstructions:**

1. **Different group algebras.** The icosahedral fiber action is
   `A₅ ⊂ S₅ ≅ I ⊂ SO(3)` — it lives on **5 strands** (the index set of
   partitions of 5). The Borromean h⁴ = −3/4 lives on **H₃(q)** — the
   **3-strand** Markov trace, indexed by partitions of **3**. The dim-5
   irrep `H` of I (an A₅/S₅ object) and the dim-2 irrep `(2,1)` of S₃ (an
   H₃ object) are in **different representation rings**. There is no
   canonical identity `H_irrep_amplitude ↦ (2,1)_h⁴_coefficient`; supplying
   one is exactly the missing categorical map. Choosing a normalisation to
   send the H-amplitude to −3/4 would be the fit the discipline review
   catches.

2. **The "S₃ sees only ℓ≤1" premise is FALSE.** The source files
   ([`spin-from-so3-fiber.md`](../../content/quantum-observable-universe/particle-interactions/spin-from-so3-fiber.md),
   [`2026-05-24-h4-coefficient-source-trace-and-so3-gap.md`](2026-05-24-h4-coefficient-source-trace-and-so3-gap.md))
   claim the discrete S₃ subgroup "sees up to ℓ=1 (h²) but NOT ℓ=2 (h⁴)",
   so the full SO(3) lift is what "opens ℓ=2". We tested this directly by
   branching `V_ℓ` under **S₃ realised as the triangle-rotation subgroup of
   SO(3)** (classes E, 2C₃ at 2π/3, 3C₂ at π):

   | ℓ | triv | sign | **std (=(2,1))** |
   |---|---|---|---|
   | 0 | 1 | 0 | 0 |
   | 1 | 0 | 1 | **1** |
   | 2 | 1 | 0 | **2** |
   | 3 | 1 | 2 | 2 |
   | 4 | 2 | 1 | 3 |

   The **std irrep — the very irrep that carries the Borromean h⁴ —
   appears at BOTH ℓ=1 (mult 1) AND ℓ=2 (mult 2)**. So S₃ does NOT "see only
   ℓ≤1"; via the natural rotation embedding it sees the std irrep at every
   ℓ≥1. The premise that ℓ=2 is the unique new source of h⁴ does not hold —
   the std/(2,1) channel is degenerate across ℓ levels and cannot be cleanly
   assigned to "ℓ=2 only". (The source files' premise likely conflated the
   *permutation* representation of S₃ on 3 points — which does cut off — with
   the *rotation* embedding S₃ ⊂ SO(3), which does not; these branch
   differently.)

**Status: OPEN.** ℓ=2 → H is derived. h⁴ = −3/4 is derived. The map linking
them is undefined, and the premise that would have justified the link is
false. The precise missing object: **a canonical functor from the SO(3)/I
spherical-harmonic level ℓ on the 5-strand color×nucleon space to a specific
Wedderburn-block coefficient of the 3-strand Borromean H₃(q) Markov trace.**
This is the SAME missing object — the `S₅`/SO(3)-fiber decoration of the
color sheets — that `conj:inter-nucleon-channel-color-tube` (K₁) and the
flavor→root map of
[`2026-06-01-flavor-dependent-cusp-shape.md`](2026-06-01-flavor-dependent-cusp-shape.md)
(K₃, PR #1670) both name.

### SU(2) / spin — **PARTIALLY DERIVED** (a genuine structural result)

**Derived (RAW, group theory):** the double cover SU(2) → SO(3) ≅ SU(2)/ℤ₂
pulls I ≅ A₅ back to the **binary icosahedral group 2I**, with |2I| = 120 =
|S₅|. The tempting identification "2I ≅ S₅" (both order 120) is **FALSE**:

- **2I is perfect** (its own commutator subgroup; abelianisation trivial).
- **S₅ is not perfect** — it has A₅ as an index-2 normal subgroup; its
  abelianisation is ℤ₂ (the sign character).

Therefore the **spin ℤ₂** (the kernel of SU(2)→SO(3)) is provably **NOT** the
**sign ℤ₂** (S₅/A₅). The spin double cover is a *different* ℤ₂ extension from
the one separating S₅ from A₅. This is a clean derived negative: spin does
NOT arise as "the S₅ sign-character lift of A₅".

**The constructive half (the candidate source, ribbon twist):** the half-
integer spin lift is the natural categorical home of the **ribbon twist**
θ_j = q^{j(j+1)} (the R-T framing element). The j=1/2 object lives in Rep of
the quantum group SU(2)_q but NOT in SO(3)_q (integer ℓ only); its 4π-
periodicity is the categorical ℤ₂ signature. Raw twist phases at the
substrate q₀ ≈ 1.10998 are recorded in the witness (reference only, no
tuning). **What is missing:** a derivation that the QOU braid/framing
structure on the color tube actually *requires* the SU(2)_q (half-integer)
extension rather than SO(3)_q (integer-only). The ribbon element exists, but
the proof that the nucleon braid carries a 2-framing (spin structure) is not
supplied. **Status: structurally derived that spin ℤ₂ ≠ sign ℤ₂; the
positive identification spin = ribbon-twist is a candidate, not closed.**

### U(1) / hypercharge — **OPEN** (writhe identified; no derived charge)

**Derived (RAW):** the framed Markov trace carries a Reidemeister-I anomaly
`q^{w·c}` where `w` = writhe — the natural **U(1)_framing**. Writhe values:
β_Bor = (σ₁⁻¹σ₂)³ has **writhe 0** (three +1, three −1); inter-nucleon arcs
in the production assignment have writhe pp = +1, nn = −1, pn = 0.

**Why no hypercharge:** these writhe values are integers determined by the
braid word, not a derived continuous U(1) charge, and there is no derived
map writhe → hypercharge Y. The writhe-0 of the Borromean braid means the
U(1)_framing phase is **trivial** on the canonical baryon — so the framing
U(1) does NOT supply a nonzero hypercharge for the nucleon in the current
model. **Status: OPEN.** The U(1) candidate (writhe/framing phase) is
identified from existing structure but is trivial on the relevant braid and
carries no derived hypercharge assignment.

---

## The unifying question — do they factor?

**They FACTOR; there is no single derived fiber action.**

- SO(3)/h⁴ lives on the **5-strand A₅⊂S₅** index set (partitions of 5).
- The h⁴ = −3/4 it is meant to explain lives on the **3-strand H₃** Borromean
  trace (partitions of 3).
- SU(2)/spin is the **double cover** ℤ₂ — provably a *different* ℤ₂ from the
  S₅/A₅ sign ℤ₂, with the constructive content in the **ribbon twist** (a
  q-deformation/framing object, not a permutation-group object).
- U(1)/framing is the **writhe** — a third, abelian, framing datum, trivial
  on the Borromean braid.

These are three structurally independent objects (a 5-strand branching, a
double-cover central extension, an abelian framing phase) bridged only by
informal analogy. No categorical construction in the current framework ties
them into one map `S₅ → SO(3) ≅ SU(2)/ℤ₂ × U(1)` that simultaneously closes
h⁴, lifts to spin, and gives the U(1) phase.

---

## What this audit does and does not claim

- **Does** derive, RAW from the I≅A₅ character table, the exact icosahedral
  branching of `V_ℓ` for ℓ≤6 (ℓ=2 → one copy of the dim-5 irrep H; all
  integrality + dim checks pass).
- **Does** reproduce, RAW, the Borromean h⁴ = −3/4 (and h² = 0).
- **Does** show, RAW, that the source-file premise "S₃ sees only ℓ≤1" is
  FALSE under the natural S₃⊂SO(3) rotation embedding: the std/(2,1) irrep
  appears at ℓ=1 (mult 1) and ℓ=2 (mult 2). This corrects a load-bearing
  claim in two source files.
- **Does** derive, RAW, that the binary icosahedral 2I is perfect (|2I|=120)
  while S₅ is not, so the spin ℤ₂ ≠ sign ℤ₂.
- **Does** identify the U(1)_framing = writhe phase and show it is trivial
  (writhe 0) on the Borromean baryon braid.
- **Does NOT** propose, fit, or tune any fiber map, normalisation, spin
  value, or hypercharge. −3/4, m_n−m_p, spin, hypercharge are falsification
  references only.
- **Does NOT** discharge the `BringFiberAction` Lean class sorry; the
  geometric fiber map remains axiomatised. Downstream
  `conj:inter-nucleon-channel-color-tube` and `conj:spin-from-so3-fiber`
  stay CONDITIONAL on the class.
- **Does NOT** wire to production; does NOT close or advance L2 numerically.

## Impact on the L2 keystone

This **does NOT close** the L2 keystone, but it **advances** it by sharpening
and correcting the obstruction:

1. It pinpoints the missing object as a functor from SO(3)/I level ℓ on the
   5-strand space to a Wedderburn coefficient of the 3-strand H₃ trace — and
   shows this is the SAME gap as the K₁/K₃ flavor→sheet map (PR #1670).
2. It **falsifies** the "ℓ=2 is the unique new source of h⁴" mechanism that
   the conjecture and two source files relied on, removing a dead end.
3. It contributes a genuine positive: spin ℤ₂ ≠ sign ℤ₂ (the spin lift is a
   ribbon/framing phenomenon, not a permutation-sign one).

## Lean

The `BringFiberAction` class
([`S5SO3FiberAction.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/S5SO3FiberAction.lean))
is extended with the DERIVED, sorry-free facts this audit established — the
icosahedral branching multiplicities (ℓ=2 → H), the S₃-rotation-subgroup
branching that contradicts the "ℓ≤1" premise, and the 2I-not-≅-S₅ structural
distinction — added as standalone `theorem`s with `native_decide` / explicit
data. The geometric `partition_to_rotation` field's content (the missing
functor) remains the only conjectural input; **no NEW sorry is introduced.**

## Cross-references

- Source conjecture / class:
  `conj:s5-so3-fiber-action`,
  [`S5SO3FiberAction.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/S5SO3FiberAction.lean).
- The premise this audit corrects:
  [`spin-from-so3-fiber.md`](../../content/quantum-observable-universe/particle-interactions/spin-from-so3-fiber.md),
  [`2026-05-24-h4-coefficient-source-trace-and-so3-gap.md`](2026-05-24-h4-coefficient-source-trace-and-so3-gap.md).
- The falsification reference:
  [`borromean-markov-trace-closed-form.md`](../../content/quantum-observable-universe/mass-theory/borromean-markov-trace-closed-form.md).
- The SAME missing object on the K₁/K₃ sides:
  [`inter-nucleon-channel-color-tube.md`](../../content/quantum-observable-universe/brings-surface/inter-nucleon-channel-color-tube.md),
  [`2026-06-01-flavor-dependent-cusp-shape.md`](2026-06-01-flavor-dependent-cusp-shape.md) (PR #1670).
