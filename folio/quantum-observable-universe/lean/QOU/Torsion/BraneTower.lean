import QOU.Torsion.JetProlongation

/-!
# §2–§6  Brane Tower, Characteristic Classes, Direct Limit Algebra,
         Vacuum State, Euler Characteristic Stability

The recursive brane tower `{E₀, E₁, …}`, quantum characteristic classes,
the direct limit algebra `𝒜_∞`, the unique vacuum state, and Euler
characteristic stability across the tower.
-/


namespace QOU.Torsion

/-! ## §2  Recursive Brane Tower -/

/-- **Recursive Brane Tower**: `E₀ = E, E_{n+1} = J¹(E_n)`.
    LaTeX: `\label{def:recursive-brane-tower}` -/
structure RecursiveBraneTower where
  level : ℕ → CQuantumObservableUniverse
  connection : (n : ℕ) → InstantonConnection (level n).toCRManifoldData
  jet_prolongation : (n : ℕ) → JetProlongationQOU

def baseLevel (tower : RecursiveBraneTower) :
    CQuantumObservableUniverse :=
  tower.level 0

/-! ## §3  Quantum Characteristic Classes -/

/-- **Quantum Characteristic Classes**: `κ_n ∈ H*(E_{n+1}, ℤ)`.
    LaTeX: `\label{def:quantum-characteristic-classes}` -/
structure QuantumCharacteristicClasses where
  tower : RecursiveBraneTower
  classAt : ℕ → Type*
  obstructs_collapse : ∀ n, Nonempty (classAt n)

/-! ## §4  Direct Limit Algebra -/

/-- **Direct Limit Algebra**: `𝒜_∞ = lim→ Γ(J¹ E_n, SU_{q_n}(2))`.
    LaTeX: `\label{def:direct-limit-algebra}`

    **Repaired 2026-11-20 (bean `qou-dx7g`).**  The invariance of the Haar and
    limit states was encoded as *constancy* (`haarState n a = haarState n b`),
    which is not invariance under the quantum gauge group but the statement
    that the state ignores its argument; and `prop:vacuum-state`'s uniqueness
    was proved from that constancy.  Now:

    * invariance is invariance under the gauge action — the sets `gaugeAt n`
      and `gauge` of transformations through which `G_q = Aut^⊗(τ)` acts by
      conjugation (`prop:vacuum-state` md);
    * `embed_surjective` records the defining property of a direct limit —
      every element of `𝒜_∞` comes from a finite level — which is what
      uniqueness actually rests on.

    **Residual.**  `G_q` is not constructed here, so `gaugeAt`/`gauge` are data;
    the identity-only gauge set satisfies the invariance fields. -/
structure DirectLimitAlgebra where
  tower : RecursiveBraneTower
  substrateAt : (n : ℕ) → ArchimedeanSubstrateField (tower.level n).M
  sectionAlgebra : ℕ → Type*
  transitionMap : (n : ℕ) → sectionAlgebra n → sectionAlgebra (n + 1)
  limitAlgebra : Type*
  embed : (n : ℕ) → sectionAlgebra n → limitAlgebra
  embed_compat : ∀ (n : ℕ) (a : sectionAlgebra n),
    embed (n + 1) (transitionMap n a) = embed n a
  /-- **Direct limit**: every element of `𝒜_∞` is embedded from some level. -/
  embed_surjective : ∀ a : limitAlgebra, ∃ (n : ℕ) (x : sectionAlgebra n), embed n x = a
  one : limitAlgebra
  /-- The gauge action at level `n` (conjugation by `G_q`). -/
  gaugeAt : (n : ℕ) → Set (sectionAlgebra n → sectionAlgebra n)
  /-- The gauge action on `𝒜_∞`. -/
  gauge : Set (limitAlgebra → limitAlgebra)
  haarState : (n : ℕ) → sectionAlgebra n → ℝ
  haarState_compat : ∀ (n : ℕ) (a : sectionAlgebra n),
    haarState (n + 1) (transitionMap n a) = haarState n a
  /-- The Haar state at each level is gauge-invariant. -/
  haarState_invariant : ∀ (n : ℕ), ∀ g ∈ gaugeAt n, ∀ a : sectionAlgebra n,
    haarState n (g a) = haarState n a
  limitState : limitAlgebra → ℝ
  limitState_extends : ∀ (n : ℕ) (a : sectionAlgebra n),
    limitState (embed n a) = haarState n a
  /-- The limit state is gauge-invariant. -/
  limitState_invariant : ∀ g ∈ gauge, ∀ a : limitAlgebra,
    limitState (g a) = limitState a

/-! ## §5  Vacuum State -/

/-- **Proposition (Existence and Uniqueness of the Vacuum State).**
    LaTeX: `\label{prop:vacuum-state}`

    A vacuum state is a gauge-invariant state on `𝒜_∞` extending the Haar
    states.  Until 2026-11-20 `invariant` read `state a = state b` for all
    `a b` (constancy), bean `qou-dx7g`. -/
structure VacuumState (dla : DirectLimitAlgebra) where
  state : dla.limitAlgebra → ℝ
  /-- Gauge invariance: `φ(g · a) = φ(a)` for every `g` in the gauge action. -/
  invariant : ∀ g ∈ dla.gauge, ∀ a : dla.limitAlgebra, state (g a) = state a
  extends_haar : ∀ (n : ℕ) (a : dla.sectionAlgebra n),
    state (dla.embed n a) = dla.haarState n a

/-- **Existence**: the limit state is a vacuum state. -/
theorem vacuum_state_exists (dla : DirectLimitAlgebra) :
    Nonempty (VacuumState dla) :=
  ⟨⟨dla.limitState, dla.limitState_invariant, dla.limitState_extends⟩⟩

/-- **Uniqueness of the vacuum state**: any two vacuum states on the
    same direct limit algebra agree on all elements.

    **Proof (2026-11-20, bean `qou-dx7g`).**  Every element of `𝒜_∞` is
    embedded from a finite level (`embed_surjective`), and on embedded
    elements both states equal the Haar state (`extends_haar`).  The previous
    proof used the constancy that `invariant` then encoded; the level-`n`
    witness arguments `n`, `a₀` it needed are kept for signature stability
    and are unused. -/
-- Ref: [leitner2026] §3, Proposition: Vacuum state (uniqueness)
theorem vacuum_state_state_eq (dla : DirectLimitAlgebra)
    (v₁ v₂ : VacuumState dla)
    (_n : ℕ) (_a₀ : dla.sectionAlgebra _n) :
    ∀ (a : dla.limitAlgebra), v₁.state a = v₂.state a := by
  intro a
  obtain ⟨m, x, rfl⟩ := dla.embed_surjective a
  rw [v₁.extends_haar m x, v₂.extends_haar m x]

/-- The vacuum state value is determined by the Haar state at level 0. -/
theorem vacuum_state_value_eq_haar (dla : DirectLimitAlgebra)
    (v : VacuumState dla) (n : ℕ) (a : dla.sectionAlgebra n) :
    v.state (dla.embed n a) = dla.haarState n a :=
  v.extends_haar n a

/-! ## §6  Euler Characteristic Stability -/

/-- **Proposition (Stability of the Euler Characteristic).**
    LaTeX: `\label{prop:euler-char-stability}` -/
structure EulerCharStability (tower : RecursiveBraneTower) where
  eulerChar : ℕ → ℤ
  stable : ∀ (n : ℕ), eulerChar (n + 1) = eulerChar n

theorem euler_char_constant (tower : RecursiveBraneTower)
    (ecs : EulerCharStability tower) (n : ℕ) :
    ecs.eulerChar n = ecs.eulerChar 0 := by
  induction n with
  | zero => rfl
  | succ n ih => rw [ecs.stable n, ih]

end QOU.Torsion
