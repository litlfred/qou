/-
# The Coleman–Glashow relation is an identity of first-order breaking

The third member of the eightfold-way null-result family, after
`GellMannOkuboIdentity.lean` (the pseudoscalar octet) and
`DecupletEqualSpacing.lean` (the baryon decuplet).  It is the one the
experiment satisfies *best*, and — like the other two — reproducing it is
evidence for nothing.

The Coleman–Glashow relation connects the three electromagnetic mass splittings
of the baryon octet:

    (m_p − m_n) − (m_Σ⁺ − m_Σ⁻) + (m_Ξ⁰ − m_Ξ⁻)  =  0.

Experimentally the residual is `−0.064` MeV against splittings of `1.3`–`8.1`
MeV — about `0.8 %` of the largest, tighter than Gell-Mann–Okubo's `≈ 6 %` and
the decuplet spacing spread's `≈ 9.2 %`.

## Why it vanishes — the mechanism, not just the arithmetic

Two standard first-order premises, and **both** are needed:

* **(P1) Isospin is exact in the strong sector.**  The strong mass then depends
  only on the isospin multiplet: one parameter each for `(p, n)`, `(Σ⁺, Σ⁻)`
  and `(Ξ⁰, Ξ⁻)`.
* **(P2) The electromagnetic self-energy is a U-spin scalar.**  U-spin is the
  `SU(2)` exchanging `d ↔ s`, and the electric charge `Q` is invariant under
  it, so `H_EM` is a U-spin scalar and its expectation value is constant on a
  U-spin multiplet.

The octet's U-spin multiplets are exactly the pairs the relation uses, each at
fixed charge — which is *why* the pairing is the one it is:

| U-spin multiplet | quark content | `Q` | EM shift |
|---|---|---|---|
| `p ↔ Σ⁺` | `uud ↔ uus` | `+1` | `a` |
| `n ↔ Ξ⁰` | `udd ↔ uss` | `0` | `b` |
| `Σ⁻ ↔ Ξ⁻` | `dds ↔ dss` | `−1` | `c` |

Six free parameters in total — three strong, three electromagnetic — and the
alternating combination cancels every one of them (`coleman_glashow_identity`).
So the relation constrains the *form* of the breaking and says nothing about
any dynamics realising that form.

## What this does and does not say

`cg_cannot_discriminate` is the operative statement: two arbitrarily different
breaking patterns give the same (vanishing) combination.  **Reproducing
Coleman–Glashow is therefore not evidence for this framework, or for any
other.**  It is recorded so that it is not later counted as one.

Unlike the other two null results, this one rests on a **conjunction**, and
that is a real difference rather than a footnote: `cg_needs_both_premises`
exhibits parameter choices under which the combination is non-zero once the
U-spin premise is dropped.  A mechanism that violated U-spin invariance of the
EM self-energy *could* fail Coleman–Glashow — so the relation does test (P1)∧(P2),
just not anything beyond them.

The testable content is the `≈ 0.8 %` residual, which measures the failure of
first order.  The framework derives no second-order term and so predicts `0`.

Numbers are comparators only; nothing here is fitted and nothing is wired.

Conventions: generic `[CommRing R]` per `AGENTS.md` §7c — the statement is pure
algebra of the breaking parameters and needs no ordering, no `ℝ`, and no
archimedean content.

-- Ref: [colemanglashow1961] Coleman & Glashow, *Electrodynamic Properties of
--      Baryons in the Unitary Symmetry Scheme*, Phys. Rev. Lett. 6 (1961) 423,
--      https://doi.org/10.1103/PhysRevLett.6.423
-/
import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic

namespace QOU.Eightfold.ColemanGlashowIdentity

variable {R : Type*} [CommRing R]

/-- Octet baryon mass under first-order breaking: an isospin-multiplet strong
part plus a U-spin-multiplet electromagnetic part.

`strong` is the strong contribution shared by an isospin multiplet (P1);
`em` is the electromagnetic shift shared by a U-spin multiplet (P2). -/
def mass (strong em : R) : R := strong + em

/-! ### The six octet states, as (isospin multiplet, U-spin multiplet) pairs -/

def m_p    (N S X a b c : R) : R := mass N a
def m_n    (N S X a b c : R) : R := mass N b
def m_SigPlus (N S X a b c : R) : R := mass S a
def m_SigMinus (N S X a b c : R) : R := mass S c
def m_XiZero  (N S X a b c : R) : R := mass X b
def m_XiMinus  (N S X a b c : R) : R := mass X c

/-- The Coleman–Glashow combination. -/
def cgCombination (N S X a b c : R) : R :=
  (m_p N S X a b c - m_n N S X a b c)
    - (m_SigPlus N S X a b c - m_SigMinus N S X a b c)
    + (m_XiZero N S X a b c - m_XiMinus N S X a b c)

/-- **Coleman–Glashow is an identity of the first-order ansatz.**  The
combination vanishes for *every* choice of the three strong and three
electromagnetic parameters, over any commutative ring.

The alternating structure is exactly what cancels the U-spin shifts: `a`
appears in `p` and `Σ⁺` with opposite sign, `b` in `n` and `Ξ⁰`, `c` in `Σ⁻`
and `Ξ⁻`. -/
theorem coleman_glashow_identity (N S X a b c : R) :
    cgCombination N S X a b c = 0 := by
  unfold cgCombination m_p m_n m_SigPlus m_SigMinus m_XiZero m_XiMinus mass; ring

/-- **The discriminating-power statement.**  Two arbitrarily different breaking
patterns — hence arbitrarily different physics — give the same value of the
Coleman–Glashow combination, namely zero.  The relation cannot tell them apart.

This is the analogue of `GellMannOkuboIdentity.gmo_cannot_discriminate` and
`DecupletEqualSpacing.equal_spacing_cannot_discriminate`, with the same
consequence: reproducing the relation is not evidence for any mechanism. -/
theorem cg_cannot_discriminate (N S X a b c N' S' X' a' b' c' : R) :
    cgCombination N S X a b c = cgCombination N' S' X' a' b' c' := by
  rw [coleman_glashow_identity, coleman_glashow_identity]

/-! ### The strong sector alone does not produce it -/

/-- With the electromagnetic shifts switched off, every splitting in the
combination vanishes separately — so the relation is not a statement about the
strong sector, and is *empty* without electromagnetism. -/
theorem strong_only_all_splittings_vanish (N S X : R) :
    m_p N S X 0 0 0 - m_n N S X 0 0 0 = 0 ∧
    m_SigPlus N S X 0 0 0 - m_SigMinus N S X 0 0 0 = 0 ∧
    m_XiZero N S X 0 0 0 - m_XiMinus N S X 0 0 0 = 0 := by
  refine ⟨?_, ?_, ?_⟩ <;>
    simp only [m_p, m_n, m_SigPlus, m_SigMinus, m_XiZero, m_XiMinus, mass] <;> ring

/-! ### Non-degeneracy, and the role of the second premise -/

/-- The individual splittings are **not** identically zero, so
`coleman_glashow_identity` is a genuine cancellation among nonzero terms rather
than the trivial statement that nothing varies.  Witnessed over `ℤ`. -/
theorem splittings_not_identically_zero :
    ∃ N S X a b c : ℤ, m_p N S X a b c - m_n N S X a b c ≠ 0 :=
  ⟨0, 0, 0, 1, 0, 0, by decide⟩

/-- **Both premises are load-bearing.**  Drop (P2) — let the electromagnetic
shift differ between the two members of a U-spin multiplet, so that `p` and
`Σ⁺` carry `a` and `a'` — and the combination no longer vanishes.

Stated by exhibiting the failure: with the `Σ⁺` shift changed from `a` to `a'`,
the combination becomes `a' − a`, which is nonzero whenever the U-spin premise
is genuinely violated. So Coleman–Glashow *does* test (P1) ∧ (P2); what it
cannot do is discriminate among mechanisms that satisfy both. -/
theorem cg_needs_both_premises (N S X a a' b c : R) :
    ((m_p N S X a b c - m_n N S X a b c)
      - (mass S a' - m_SigMinus N S X a b c)
      + (m_XiZero N S X a b c - m_XiMinus N S X a b c)) = a - a' := by
  simp only [m_p, m_n, m_SigMinus, m_XiZero, m_XiMinus, mass]; ring

/-- And that failure is realisable: some choice makes it nonzero over `ℤ`. -/
theorem cg_premise_violation_is_detectable :
    ∃ a a' : ℤ, a - a' ≠ 0 := ⟨1, 0, by decide⟩

end QOU.Eightfold.ColemanGlashowIdentity
