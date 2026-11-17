/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: QOU Formalization Lane
-/

namespace QOU.MassTheory.FullTowerSurfaceSplitAndPairingTwoBitParity

/-!
# Full-Tower $H_{3A}$ Surface Split at $^{16}\mathrm{O}$ & Two-Bit Pairing Parity (`qou-hu1f`, `qou-nvoq`)

This module formalizes two structural results under `qou-v2om`:

1. **`qou-hu1f` (Full-Tower Ruling vs $H_3$ Mass/Binding Surface Split, Including $^{16}\mathrm{O}$ $A = 16$):**
   - At mass number $A$, the nominal full-tower braid algebra $H_{3A}(q)$ has $3A$ strands
     and $p(3A)$ irreducible partition blocks, whereas both live mass/binding pipelines
     operate strictly at the $H_3(q)$ surface ($3$ strands, $p(3) = 3$ partitions,
     $3! = 6$ normal-form basis components):
     - the normal-form route (`build_atom_nf_mp`) projects every crossing down to $6$
       components, discarding $3A - 6$ strand degrees of freedom ($48 - 6 = 42$ at
       $^{16}\mathrm{O}$, $A = 16$);
     - the canonical route (`binding_canonical`) composes $A$ per-nucleon $H_3$ traces
       without constructing $H_{3A}$.
   - We prove strict monotonicity of the discarded strand excess $3A - 3$ and the exact
     $^{16}\mathrm{O}$ ($A = 16$) collapse invariants ($3A = 48$ vs $6$ NF components).

2. **`qou-nvoq` (Bethe-Weizsäcker Pairing Term $\delta_{\mathrm{pair}} \in \{+1, 0, -1\}$: Single-Bit Impossibility & $A$-Parity Resolution):**
   - A single $\mathbb{Z}/2\mathbb{Z}$ bit (such as $(-1)^{n(\lambda)}$ alone) has image
     cardinality at most $2$ and therefore cannot represent the three-valued
     Bethe-Weizsäcker pairing sign $\delta_{\mathrm{pair}}(Z, N) \in \{+1, 0, -1\}$ across
     even-even ($+1$), odd-$A$ ($0$), and odd-odd ($-1$) nuclei.
   - Supplying $A$-parity $(Z + N) \bmod 2$ as the second bit resolves the obstruction:
     the product of the even-$A$ gate $(1 - ((Z + N) \bmod 2))$ and the nucleon-pair
     chirality sign $(-1)^Z$ equals $\delta_{\mathrm{pair}}(Z, N)$ identically across all
     four $(Z \bmod 2, N \bmod 2)$ parity classes, and satisfies
     $2 \delta_{\mathrm{pair}}(Z, N) = (-1)^Z + (-1)^N$.
-/

/-- Nominal braid strand count $n(A) = 3A$ in the full tower $H_{3A}(q)$ (`qou-hu1f`). -/
def fullTowerStrandCount (A : Nat) : Nat :=
  3 * A

/-- Fixed normal-form component dimension $3! = 6$ of the $H_3(q)$ surface (`qou-hu1f`). -/
def h3NormalFormComponents : Nat := 6

/-- Fixed strand count $3$ of the single-nucleon $H_3(q)$ algebra (`qou-hu1f`). -/
def h3StrandCount : Nat := 3

/-- Exact partition counts $p(3A)$ of the full Hecke algebra $H_{3A}(q)$ for $A \in \{1, 2, 3, 4\}$ (`qou-hu1f`). -/
def fullTowerPartitionCountSmall (A : Nat) : Nat :=
  match A with
  | 1 => 3
  | 2 => 11
  | 3 => 30
  | 4 => 77
  | _ => 0

/-- At $^{16}\mathrm{O}$ ($A = 16$), the full tower has $3A = 48$ strands whereas the $H_3$
normal-form surface retains $6$ components ($48 = 8 \times 6$, discarding $42$ strand degrees
of freedom relative to $6$ and $45$ relative to $3$ strands), and already at $^4\mathrm{He}$
($A = 4$) $p(12) - p(3) = 77 - 3 = 74$ partition blocks are omitted (`qou-hu1f`). -/
theorem oxygen16_and_helium4_fullTower_vs_h3_surface :
    fullTowerStrandCount 1 = 3 ∧
      fullTowerStrandCount 4 = 12 ∧
      fullTowerStrandCount 16 = 48 ∧
      fullTowerStrandCount 16 - h3NormalFormComponents = 42 ∧
      fullTowerStrandCount 16 - h3StrandCount = 45 ∧
      fullTowerPartitionCountSmall 4 - fullTowerPartitionCountSmall 1 = 74 := by
  dsimp [fullTowerStrandCount, h3NormalFormComponents, h3StrandCount, fullTowerPartitionCountSmall]
  refine ⟨rfl, rfl, rfl, rfl, rfl, rfl⟩

/-- For all mass numbers $A_2 > A_1 \ge 2$, the full-tower strand excess over $H_3$
($3A - 3$) is strictly positive and strictly increasing (`qou-hu1f`). -/
theorem fullTower_strand_excess_strictly_increasing (A1 A2 : Nat)
    (hge : A1 ≥ 2) (hlt : A1 < A2) :
    fullTowerStrandCount A1 - h3StrandCount > 0 ∧
      fullTowerStrandCount A1 - h3StrandCount < fullTowerStrandCount A2 - h3StrandCount := by
  dsimp [fullTowerStrandCount, h3StrandCount]
  omega

/-- Parity sign $\pm 1 \in \mathbb{Z}$ associated with a parity bit $b \in \mathrm{Bool}$
(`false` = even $\mapsto +1$, `true` = odd $\mapsto -1$) (`qou-nvoq`). -/
def boolParitySign (b : Bool) : Int :=
  match b with
  | false => 1
  | true => -1

/-- Even-$A$ gate in $\{0, 1\} \subset \mathbb{Z}$ from the $A$-parity bit $a_p = Z \oplus N$
(`false` = even $A \mapsto 1$, `true` = odd $A \mapsto 0$) (`qou-nvoq`). -/
def evenAGate (aParity : Bool) : Int :=
  match aParity with
  | false => 1
  | true => 0

/-- Three-valued Bethe-Weizsäcker pairing sign $\delta_{\mathrm{pair}}(z_p, n_p) \in \{+1, 0, -1\}$
on proton/neutron parity bits $(z_p, n_p) \in \mathrm{Bool} \times \mathrm{Bool}$ (`qou-nvoq`):
- `(false, false)` (even-even) $\mapsto +1$
- `(true, false)` or `(false, true)` (odd-$A$) $\mapsto 0$
- `(true, true)` (odd-odd) $\mapsto -1$. -/
def bwPairingSign (zOdd nOdd : Bool) : Int :=
  match zOdd, nOdd with
  | false, false => 1
  | true, false => 0
  | false, true => 0
  | true, true => -1

/-- Single-bit impossibility theorem (`qou-nvoq`): no single-bit classifier
$b : \mathrm{Bool} \times \mathrm{Bool} \to \mathrm{Bool}$ composed with a readout
$g : \mathrm{Bool} \to \mathbb{Z}$ can reproduce all three values $\{+1, 0, -1\}$ of
$\delta_{\mathrm{pair}}$ across even-even `(false, false)`, odd-$A$ `(true, false)`,
and odd-odd `(true, true)`. -/
theorem single_bit_cannot_encode_bw_pairing
    (b : Bool → Bool → Bool) (g : Bool → Int) :
    ¬ (g (b false false) = bwPairingSign false false ∧
        g (b true false) = bwPairingSign true false ∧
        g (b true true) = bwPairingSign true true) := by
  dsimp [bwPairingSign]
  intro h
  rcases h with ⟨h00, h10, h11⟩
  revert h00 h10 h11
  cases b false false <;> cases b true false <;> cases b true true <;> intro h00 h10 h11 <;> omega

/-- Two-bit resolution theorem (`qou-nvoq`): combining the $A$-parity bit
$\mathrm{xor}\ z_{\mathrm{odd}}\ n_{\mathrm{odd}}$ (via `evenAGate`) with a single
chirality sign `boolParitySign zOdd` reproduces the three-valued Bethe-Weizsäcker
pairing sign $\delta_{\mathrm{pair}}$ identically across all four $(Z \bmod 2, N \bmod 2)$
sectors, and satisfies $2 \delta_{\mathrm{pair}} = (-1)^Z + (-1)^N$. -/
theorem two_bit_a_parity_times_chirality_eq_bw_pairing (zOdd nOdd : Bool) :
    evenAGate (xor zOdd nOdd) * boolParitySign zOdd = bwPairingSign zOdd nOdd ∧
      2 * bwPairingSign zOdd nOdd = boolParitySign zOdd + boolParitySign nOdd := by
  cases zOdd <;> cases nOdd <;> decide

end QOU.MassTheory.FullTowerSurfaceSplitAndPairingTwoBitParity
