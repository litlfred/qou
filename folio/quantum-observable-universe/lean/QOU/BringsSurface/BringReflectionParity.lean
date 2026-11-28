import QOU.BringsSurface.BringHarmonicTypes

/-!
# Reflection parity of the harmonics of Bring's surface (`S₅ × C₂`)

Bean `qou-u81q`, next step after `BringHarmonicTypes.lean` (recommended option, 2026-11-28).
The full isometry group of Bring's surface `B` is `S₅ × C₂`, of order `240`. This file brings
the orientation-reversing isometries into the finite Bring map, and splits every harmonic type
`ρ` into a reflection-even part `ρ⁺` and a reflection-odd part `ρ⁻`. Everything is finite.

## The reflection of the map

Darts are `S₅`, with vertex rotation `σ x = x S` and edge involution `α x = x A`
(`QOU/BringsSurface/BringMapChain.lean`). Put `T = (2 4)`. Then `T S T = S⁻¹`, `T A T = A` and
`T² = 1` (`T_inverts_S`, `T_fixes_A`, `T_involutive`), so `c x = x T` reverses `σ`, keeps `α`, and
commutes with every rotation `x ↦ g x`. It is the central orientation-reversing isometry, and
`(g, c) : x ↦ g x T` runs over the other 120 isometries. `T` is the unique such element
(`T_unique`).

## Results

1. **`c` has no fixed point** (`c_fixes_no_vertex`, `c_fixes_no_edge`, `c_fixes_no_face`). It
   fixes no vertex, no edge and no face of the map, so it acts freely on `B`. Hence `B/c` is a
   closed non-orientable surface with `χ = −6/2 = −3`, the connected sum of five projective planes
   (`quotient_by_c_euler`). It agrees with the curve: `c` is complex conjugation, which commutes
   with the permutations of the coordinates, and Bring's curve has no real point, because
   `Σ xᵢ² = 0` with `xᵢ` real forces `x = 0` (`no_real_points`).

2. **The flag triangle** (`triangle_reflections`). The three sides of the `(2,4,5)` triangle are
   the mirrors of `(T, c)` (along an edge), `(S T, c)` (vertex to face centre) and `(A T, c)`
   (edge midpoint to face centre). Their products are `S⁻¹`, `A` and `S A`, of orders `4`, `2`,
   `5`. `T` is a transposition and `S T`, `A T` are double transpositions (`triangle_parities`).

3. **The four one-dimensional types are boundary problems on the triangle**
   (`one_dim_boundary_conditions`). A type `ρ ⊗ ε` with `ρ ∈ {triv, sgn}` takes the value
   `χ_ρ(g) ε` on the side reflection `(g, c)`; `+1` is a Neumann side and `−1` a Dirichlet side:
   * `triv⁺`: Neumann on all three sides;
   * `triv⁻`: Dirichlet on all three sides;
   * `sgn⁺`: Dirichlet on the edge side, Neumann on the two sides through the face centre;
   * `sgn⁻`: Neumann on the edge side, Dirichlet on the two sides through the face centre.

4. **Cells under the orientation-reversing isometries** (`rev_vertex_count`, `rev_edge_counts`,
   `rev_face_count`): `(g, c)` fixes vertices only for `g` a transposition (6) or a double
   transposition (4); it fixes 6 edges pointwise when `g` is a transposition and reverses 4 edges
   when `g` is a double transposition; it fixes faces only for a double transposition (8).
   Computed over all 120 darts by `decide`.

5. **`H¹ = [2,1,1,1]⁺ ⊕ [2,1,1,1]⁻`** (`hopf_trace_h1_reversing`). With `H⁰ = triv⁺` and
   `H² = triv⁻` (the orientation character), the Hopf trace formula gives
   `tr (g, c) | H¹ = 0` for every `g`. With `hopf_trace_h1` (`tr g | H¹ = 2 χ_{[2,1,1,1]}(g)`)
   this is the character of `[2,1,1,1] ⊗ (+) ⊕ [2,1,1,1] ⊗ (−)`: each holomorphic form `ω` gives
   one even and one odd real harmonic form, `ω ± c^* ω̄`.

6. **Parity of the cell functions** (`vertex_parity`, `edge_parity`, `face_parity`). The
   difference `m_ρ⁺ − m_ρ⁻` for the vertex functions, the oriented edge cochains and the face
   functions, by type.

7. **Exhaustiveness for `S₅ × C₂`** (`parity_split`). A class function of `S₅ × C₂` is a pair
   `(f₀, f₁)` (values on `g` and on `(g, c)`); it is `Σ_ρ (m_ρ⁺ χ_ρ⊗⁺ + m_ρ⁻ χ_ρ⊗⁻)` with
   `m_ρ^± = ⟨f₀ ± f₁, χ_ρ⟩ / 240`, uniquely. So there are exactly fourteen types.

Inputs cited, not derived: the character table of `S₅` (as in `BringHarmonicTypes.lean`), the Hopf
trace formula, Hodge theory for item 5's reading, and that `c` is complex conjugation on the
curve. No empirical value enters.
-/

namespace QOU.Brings.ReflectionParity

open Equiv QOU.BringRegularMap QOU.Brings.S5Char QOU.Brings.HarmonicTypes

set_option maxRecDepth 100000

/-! ## The reflection `T` -/

/-- `T = (2 4)`. -/
def T : Perm (Fin 5) := swap 2 4

theorem T_inverts_S : T * S * T⁻¹ = S⁻¹ := by decide
theorem T_fixes_A : T * A * T⁻¹ = A := by decide
theorem T_involutive : T * T = 1 := by decide

/-- `T` is the only element inverting `S`, fixing `A`, and squaring to `1`. -/
theorem T_unique :
    ∀ t : Perm (Fin 5), t * S * t⁻¹ = S⁻¹ → t * A * t⁻¹ = A → t * t = 1 → t = T := by
  decide

/-! ## 1. `c` acts freely -/

/-- The vertex stabiliser `⟨S⟩` as a list. -/
def vStab : List (Perm (Fin 5)) := [1, S, S ^ 2, S ^ 3]
/-- The face stabiliser `⟨A S⟩` (faces are the cycles of `σ α = (· * (A * S))`). -/
def fStab : List (Perm (Fin 5)) := [1, A * S, (A * S) ^ 2, (A * S) ^ 3, (A * S) ^ 4]

/-- `c` maps the vertex `x⟨S⟩` to `x T ⟨S⟩`; it is fixed iff `T ∈ ⟨S⟩`. -/
theorem c_fixes_no_vertex : T ∉ vStab := by decide
/-- `c` maps the dart `x` to `x T`; an edge `{x, x A}` is fixed iff `T = 1` or `T = A`. -/
theorem c_fixes_no_edge : T ≠ 1 ∧ T ≠ A := by decide
/-- The face through `x` goes to the face through `x T A`; it is fixed iff `T A ∈ ⟨A S⟩`. -/
theorem c_fixes_no_face : T * A ∉ fStab := by decide

/-- `B/c` has `χ = −3`: 15 vertices, 30 edges, 12 faces. -/
theorem quotient_by_c_euler : (30 / 2 : ℤ) - 60 / 2 + 24 / 2 = -3 := by norm_num

/-- Bring's curve has no real point: `Σ xᵢ² = 0` over `ℚ` (and likewise any ordered field)
forces every `xᵢ = 0`. -/
theorem no_real_points (x : Fin 5 → ℚ)
    (h : x 0 ^ 2 + x 1 ^ 2 + x 2 ^ 2 + x 3 ^ 2 + x 4 ^ 2 = 0) : ∀ i, x i = 0 := by
  have h0 := sq_nonneg (x 0); have h1 := sq_nonneg (x 1); have h2 := sq_nonneg (x 2)
  have h3 := sq_nonneg (x 3); have h4 := sq_nonneg (x 4)
  intro i
  fin_cases i <;> simp <;> nlinarith

/-- The same over any linearly ordered field (in particular the real closure of `ℚ`). -/
theorem no_real_points_field {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    (x : Fin 5 → K) (h : x 0 ^ 2 + x 1 ^ 2 + x 2 ^ 2 + x 3 ^ 2 + x 4 ^ 2 = 0) :
    ∀ i, x i = 0 := by
  have h0 := sq_nonneg (x 0); have h1 := sq_nonneg (x 1); have h2 := sq_nonneg (x 2)
  have h3 := sq_nonneg (x 3); have h4 := sq_nonneg (x 4)
  intro i
  fin_cases i <;> simp <;> nlinarith

/-! ## 2. The flag triangle -/

/-- Side reflections `(T, c)`, `(S T, c)`, `(A T, c)` are involutions, and their pairwise products
are the rotations `S⁻¹`, `A`, `S A` at the vertex, the edge midpoint and the face centre. -/
theorem triangle_reflections :
    T * T = 1 ∧ (S * T) * (S * T) = 1 ∧ (A * T) * (A * T) = 1 ∧
      T * (S * T) = S⁻¹ ∧ T * (A * T) = A ∧ (S * T) * (A * T) = S * A := by
  decide

/-- `T` is odd; `S T` and `A T` are even. -/
theorem triangle_parities :
    Perm.sign T = -1 ∧ Perm.sign (S * T) = 1 ∧ Perm.sign (A * T) = 1 := by
  decide

/-- **The four one-dimensional types on the three sides** `(edge, vertex–face, edge–face)`.
`χ_ρ(g)·ε` with `χ_triv = 1`, `χ_sgn = sign`; `+1` = Neumann, `−1` = Dirichlet. -/
theorem one_dim_boundary_conditions :
    let sides : List (Perm (Fin 5)) := [T, S * T, A * T]
    sides.map (fun _ => (1 : ℤ) * 1) = [1, 1, 1] ∧
    sides.map (fun _ => (1 : ℤ) * (-1)) = [-1, -1, -1] ∧
    sides.map (fun g => ((Perm.sign g : ℤˣ) : ℤ) * 1) = [-1, 1, 1] ∧
    sides.map (fun g => ((Perm.sign g : ℤˣ) : ℤ) * (-1)) = [1, -1, -1] := by
  decide

/-! ## 4. Cells under `(g, c) : x ↦ g x T` -/

/-- Class representatives `1, (01), (01)(23), (012), (012)(34), (0123), (01234)` (as products
of swaps, in the order of `S5Char`). -/
def rep : Fin 7 → Perm (Fin 5) :=
  ![1, swap 0 1, swap 0 1 * swap 2 3, swap 0 1 * swap 1 2, swap 0 1 * swap 1 2 * swap 3 4,
    swap 0 1 * swap 1 2 * swap 2 3, swap 0 1 * swap 1 2 * swap 2 3 * swap 3 4]

/-- Fixed vertices of `(g, c)`, times 4 (each vertex has 4 darts). -/
theorem rev_vertex_count :
    ∀ i, (Finset.univ.filter (fun x : Perm (Fin 5) => x⁻¹ * rep i * x * T ∈ vStab)).card =
      4 * ![0, 6, 4, 0, 0, 0, 0] i := by
  decide

/-- Fixed edges of `(g, c)`, times 2: kept in direction (`g x T = x`) and reversed
(`g x T = x A`). -/
theorem rev_edge_counts :
    ∀ i, (Finset.univ.filter (fun x : Perm (Fin 5) => rep i * x * T = x)).card =
        2 * ![0, 6, 0, 0, 0, 0, 0] i ∧
      (Finset.univ.filter (fun x : Perm (Fin 5) => rep i * x * T = x * A)).card =
        2 * ![0, 0, 4, 0, 0, 0, 0] i := by
  decide

/-- Fixed faces of `(g, c)`, times 5. -/
theorem rev_face_count :
    ∀ i, (Finset.univ.filter (fun x : Perm (Fin 5) => x⁻¹ * rep i * x * T * A ∈ fStab)).card =
      5 * ![0, 0, 8, 0, 0, 0, 0] i := by
  decide

/-- Traces of `(g, c)` on the cochains. `C⁰`: fixed vertices. `C¹`: fixed edges, `+1` if kept,
`−1` if reversed. `C²`: fixed faces, each with sign `−1` (an orientation-reversing isometry that
keeps a face reverses its orientation). -/
def revC0 : Fin 7 → ℤ := ![0, 6, 4, 0, 0, 0, 0]
def revC1 : Fin 7 → ℤ := ![0, 6, -4, 0, 0, 0, 0]
def revC2 : Fin 7 → ℤ := ![0, 0, -8, 0, 0, 0, 0]

/-! ## 5. `H¹ = [2,1,1,1]⁺ ⊕ [2,1,1,1]⁻` -/

/-- **Hopf trace for the orientation-reversing isometries.** `tr H⁰ = 1`, `tr H² = −1`, so
`tr (g, c) | H¹ = 1 + (−1) − (C⁰ − C¹ + C²) = 0` for every class. -/
theorem hopf_trace_h1_reversing :
    (fun i => (1 : ℤ) + (-1) - (revC0 i - revC1 i + revC2 i)) = fun _ => 0 := by
  decide

/-- So `m⁺ − m⁻ = ⟨tr (·, c) | H¹, χ_ρ⟩ = 0` for every type: `H¹` is even and odd in equal
measure, `[2,1,1,1]⁺ ⊕ [2,1,1,1]⁻`. -/
theorem h1_parity_balanced :
    (List.finRange 7).map (fun r => inner (fun i => (1 : ℤ) + (-1) -
      (revC0 i - revC1 i + revC2 i)) (irr r)) = [0, 0, 0, 0, 0, 0, 0] := by
  decide

/-! ## 6. Parity of the cell functions -/

/-- `120 (m⁺ − m⁻)` for each type is `⟨revCᵢ, χ_ρ⟩`. Vertex functions:
`m⁺ − m⁻ = (1, 0, 1, −1, 1, 0, −1)`, so `triv⁺ + [4,1]⁺ + [2,1,1,1]⁻ + [3,2]⁺ + [2,2,1]⁺ +
[2,2,1]⁻ + [3,1,1]⁻`. -/
theorem vertex_parity :
    (List.finRange 7).map (fun r => inner revC0 (irr r)) =
      [120, 0, 120, -120, 120, 0, -120] := by
  decide

/-- Oriented edge cochains: `m⁺ − m⁻ = (0, −1, 1, −1, 0, −1, 1)`, so `sgn⁻ + [4,1]⁺ +
([2,1,1,1]⁺ + 2[2,1,1,1]⁻) + ([3,2]⁺ + [3,2]⁻) + ([2,2,1]⁺ + 2[2,2,1]⁻) + (2[3,1,1]⁺ +
[3,1,1]⁻)`: thirty dimensions of each parity. -/
theorem edge_parity :
    (List.finRange 7).map (fun r => inner revC1 (irr r)) =
      [0, -120, 120, -120, 0, -120, 120] := by
  decide

/-- Face functions (each fixed face counted `+1` as a function): `m⁺ − m⁻ =
(1, 1, 0, 0, 1, 1, −2)`, so `triv⁺ + sgn⁺ + [3,2]⁺ + [2,2,1]⁺ + 2[3,1,1]⁻`. -/
theorem face_parity :
    (List.finRange 7).map (fun r => inner (fun i => -revC2 i) (irr r)) =
      [120, 120, 0, 0, 120, 120, -240] := by
  decide

/-! ## 7. Fourteen types, exhaustively -/

/-- **Parity split.** A class function `(f₀, f₁)` of `S₅ × C₂` is
`Σ_ρ (m_ρ⁺ (χ_ρ, χ_ρ) + m_ρ⁻ (χ_ρ, −χ_ρ))` with `m_ρ^± = ⟨f₀ ± f₁, χ_ρ⟩/240`. -/
theorem parity_split (f₀ f₁ : Fin 7 → ℚ) (i : Fin 7) :
    combo (fun r => pairQ (fun j => f₀ j + f₁ j) r / 240) i +
        combo (fun r => pairQ (fun j => f₀ j - f₁ j) r / 240) i = f₀ i ∧
      combo (fun r => pairQ (fun j => f₀ j + f₁ j) r / 240) i -
        combo (fun r => pairQ (fun j => f₀ j - f₁ j) r / 240) i = f₁ i := by
  have hp := class_function_expansion (fun j => f₀ j + f₁ j) i
  have hm := class_function_expansion (fun j => f₀ j - f₁ j) i
  have e1 : ∀ g : Fin 7 → ℚ, combo (fun r => pairQ g r / 240) i =
      combo (fun r => pairQ g r / 120) i / 2 := by
    intro g; simp only [combo]; ring
  rw [e1, e1]
  constructor <;> simp only at hp hm <;> linarith

/-- Uniqueness of the fourteen-type expansion. -/
theorem parity_unique (a b : Fin 7 → ℚ)
    (h₀ : ∀ i, combo a i + combo b i = 0) (h₁ : ∀ i, combo a i - combo b i = 0) :
    a = 0 ∧ b = 0 := by
  have ha : ∀ i, combo a i = 0 := fun i => by linarith [h₀ i, h₁ i]
  have hb : ∀ i, combo b i = 0 := fun i => by linarith [h₀ i, h₁ i]
  exact ⟨expansion_unique a ha, expansion_unique b hb⟩

end QOU.Brings.ReflectionParity
