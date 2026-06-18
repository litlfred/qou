/-!
# QOU.Knots.KauffmanTL3 — a computable link invariant for 3-braid closures

The crossing-minimality half of the Brunnian confinement selection
([`prop:confinement-operator-selection`](../../../quantum-observable-universe/particle-interactions/confinement-operator-selection.md))
needs to recognise when a 3-braid closure is a **nontrivial** link — and `B₃` is
non-abelian, so (unlike the 2-sublink triviality, decided by the `B₂ ≅ ℤ`
exponent sum in `confinement_operator_selection.lean`) this cannot be read off a
linking number. This module builds the smallest sufficient machinery: the
**Temperley–Lieb algebra `TL₃`** (only 5-dimensional, `Catalan 3 = 5`) and the
**Kauffman bracket** of a 3-braid closure, as an integer **Laurent polynomial**
in `A`. The bracket is a computable, decidable link invariant.

`borromean_link_nontrivial` then proves **by `decide` (axiom-free)** that the
Borromean braid `(σ₀σ₁⁻¹)³` closes to a link whose bracket differs from the
3-component unlink's — i.e. the Borromean rings are a *nontrivial* link. Both
have writhe `0`, so the unnormalised bracket already separates them.

This is the first brick of the link-invariant library that will close
crossing-minimality (enumerate pure 3-braids of length `≤ 6`, compute each
bracket, confirm the minimal nontrivial Brunnian closure is the Borromean — the
"enumerate in Python, assert in Lean" plan; the full enumeration will use
`native_decide` for speed, documented as such). See
`docs/workplans/2026-06-17-lean-link-invariant-library.md`.
-/

namespace QOU.Knots

/-- Integer Laurent polynomial: `cs[k]` is the coefficient of `A^(lo+k)`.
    Normalised — no leading/trailing zero coeffs; the zero polynomial is
    `⟨0, []⟩` — so structural `DecidableEq` is equality of polynomials. -/
structure LP where
  lo : Int
  cs : List Int
deriving DecidableEq, Repr

namespace LP

/-- Strip leading/trailing zero coefficients to the canonical form. -/
def normalize (p : LP) : LP :=
  let rec dropLead (l : Int) (cs : List Int) : Int × List Int := match cs with
    | [] => (0, [])
    | 0 :: t => dropLead (l + 1) t
    | c :: t => (l, c :: t)
  let (lo', cs') := dropLead p.lo p.cs
  let cs'' := (cs'.reverse.dropWhile (· == 0)).reverse
  if cs''.isEmpty then ⟨0, []⟩ else ⟨lo', cs''⟩

def zero : LP := ⟨0, []⟩
def one : LP := ⟨0, [1]⟩
def mono (e c : Int) : LP := normalize ⟨e, [c]⟩

def coeff (p : LP) (e : Int) : Int :=
  let i := e - p.lo
  if i < 0 then 0 else (p.cs.get? i.toNat).getD 0

def add (p q : LP) : LP :=
  let lo := min p.lo q.lo
  let n := (max (p.lo + p.cs.length) (q.lo + q.cs.length) - lo).toNat
  normalize ⟨lo, (List.range n).map (fun k => coeff p (lo + Int.ofNat k) + coeff q (lo + Int.ofNat k))⟩

def neg (p : LP) : LP := ⟨p.lo, p.cs.map (- ·)⟩

def mul (p q : LP) : LP :=
  ((List.range p.cs.length).flatMap (fun i =>
    (List.range q.cs.length).map (fun j =>
      mono (p.lo + Int.ofNat i + q.lo + Int.ofNat j)
        ((p.cs.get? i).getD 0 * (q.cs.get? j).getD 0)))).foldl add zero

end LP

open LP

/-- A `TL₃` element in the basis `(1, e₁, e₂, e₁e₂, e₂e₁)`, coefficients in
    `ℤ[A, A⁻¹]`. -/
structure TL where
  v0 : LP
  v1 : LP
  v2 : LP
  v3 : LP
  v4 : LP
deriving DecidableEq, Repr

namespace TL

/-- The loop value `δ = -A² - A⁻²`. -/
def delta : LP := add (neg (mul (mono 1 1) (mono 1 1))) (neg (mul (mono (-1) 1) (mono (-1) 1)))

def get (x : TL) : Nat → LP
  | 0 => x.v0 | 1 => x.v1 | 2 => x.v2 | 3 => x.v3 | _ => x.v4

def addAt (x : TL) (i : Nat) (p : LP) : TL := match i with
  | 0 => {x with v0 := add x.v0 p}
  | 1 => {x with v1 := add x.v1 p}
  | 2 => {x with v2 := add x.v2 p}
  | 3 => {x with v3 := add x.v3 p}
  | _ => {x with v4 := add x.v4 p}

def zeroTL : TL := ⟨LP.zero, LP.zero, LP.zero, LP.zero, LP.zero⟩
def oneTL : TL := ⟨LP.one, LP.zero, LP.zero, LP.zero, LP.zero⟩

/-- Product of two `TL₃` basis elements (index, scalar `1` or `δ`), from the
    relations `eᵢ² = δ eᵢ`, `e₁e₂e₁ = e₁`, `e₂e₁e₂ = e₂`. -/
def bmul : Nat → Nat → Nat × LP
  | 0, j => (j, one)
  | 1, 0 => (1, one) | 1, 1 => (1, delta) | 1, 2 => (3, one) | 1, 3 => (3, delta) | 1, 4 => (1, one)
  | 2, 0 => (2, one) | 2, 1 => (4, one) | 2, 2 => (2, delta) | 2, 3 => (2, one) | 2, 4 => (4, delta)
  | 3, 0 => (3, one) | 3, 1 => (1, one) | 3, 2 => (3, delta) | 3, 3 => (3, one) | 3, 4 => (1, delta)
  | 4, 0 => (4, one) | 4, 1 => (4, delta) | 4, 2 => (2, one) | 4, 3 => (2, delta) | _, _ => (4, one)

def mul (x y : TL) : TL :=
  (List.range 5).foldl (fun acc i => (List.range 5).foldl (fun acc2 j =>
    let (k, sc) := bmul i j
    addAt acc2 k (LP.mul (LP.mul (x.get i) (y.get j)) sc)) acc) zeroTL

/-- Kauffman image of a braid generator: `σᵢ ↦ A·1 + A⁻¹·eᵢ`, inverse
    `σᵢ⁻¹ ↦ A⁻¹·1 + A·eᵢ` (`i ∈ {1,2}`). -/
def sig (i : Nat) (pos : Bool) : TL :=
  let a := if pos then mono 1 1 else mono (-1) 1
  let b := if pos then mono (-1) 1 else mono 1 1
  if i == 1 then ⟨a, b, LP.zero, LP.zero, LP.zero⟩ else ⟨a, LP.zero, b, LP.zero, LP.zero⟩

/-- A 3-braid word as a list of `(generator ∈ {1,2}, positive?)`. -/
def evalWord (w : List (Nat × Bool)) : TL :=
  w.foldl (fun acc (i, s) => mul acc (sig i s)) oneTL

def d2 : LP := LP.mul delta delta
def d3 : LP := LP.mul d2 delta

/-- Kauffman bracket of the braid's plat/trace closure. Loop counts of the
    closed `TL₃` basis diagrams: `1 ↦ δ³`, `e₁,e₂ ↦ δ²`, `e₁e₂,e₂e₁ ↦ δ`. -/
def bracket (w : List (Nat × Bool)) : LP :=
  let x := evalWord w
  LP.add (LP.add (LP.add (LP.add (LP.mul x.v0 d3) (LP.mul x.v1 d2)) (LP.mul x.v2 d2))
    (LP.mul x.v3 delta)) (LP.mul x.v4 delta)

/-- The Borromean braid `(σ₀σ₁⁻¹)³` (generators 1-indexed here as `σ₁,σ₂`). -/
def borromean : List (Nat × Bool) := [(1, true), (2, false), (1, true), (2, false), (1, true), (2, false)]

/-- The trivial 3-braid (closes to the 3-component unlink). -/
def unlink3 : List (Nat × Bool) := []

set_option maxRecDepth 100000 in
/-- **The Borromean rings are a nontrivial link** (machine-proved, axiom-free):
    the Kauffman bracket of `(σ₀σ₁⁻¹)³`'s closure differs from the 3-unlink's.
    Both closures have writhe `0`, so the unnormalised bracket separates them.
    This is the link-nontriviality invariant the crossing-minimality proof needs
    (where the `B₂ ≅ ℤ` exponent-sum test of sublink triviality does not reach,
    `B₃` being non-abelian). -/
theorem borromean_link_nontrivial : bracket borromean ≠ bracket unlink3 := by decide

end TL
end QOU.Knots
