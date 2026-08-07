/-
# The electron count in the canonical mass formula is rigid, not conventional

The canonical nucleon mass (`docs/canonical-mass-formula-guardrail.md`) has the
shape

    m_p = dim V_{(2,1)} * ( m_mu * F_Bor  -  |S_3| * m_e )
        = 2 * ( E_constit - 6 * m_e )

and substituting the muon anchor `m_mu = m_e * Vol(4_1) / hbar_q^2` gives

    m_p = m_e * ( 2 * Vol(4_1) * F_Bor / hbar_q^2 - 12 ).

So `m_e` **factors out completely**: the framework predicts the dimensionless
ratio `m_p / m_e` and never an absolute mass.  That is the precise sense in
which mass here is *relational* — §1 below proves it as a homogeneity
statement.

But `m_e` occurs **twice**, and only the first occurrence is the scale:

1. the overall unit, through the muon anchor — absorbed, uncontroversial;
2. `- |S_3| * m_e`, **subtracted**, once per Hecke block, doubled by
   `dim V_{(2,1)}`.

Occurrence (2) is additive, `q`-independent, and an **integer** multiple of
`m_e`.  The corpus framing "`m_e` = CAL-1, the dimensional unit" accounts for
(1) and says nothing about (2).  A dimensional unit is by construction
unobservable — rescaling it rescales everything — so it cannot produce a term
whose *presence* is measurable.  This file proves that (2)'s presence **is**
measurable, in the strongest available sense: the integer is uniquely
determined by any measurement good to better than one electron mass (§3).

Numerical companion: `computations/me_additive_term_structure.py`
(witness `me-additive-term-structure.witness.json`), which finds
* deleting the term moves `m_p` by `12*m_e = 6.13 MeV` = 0.65% = ~2.1e7 sigma;
* the integer sweep selects `c = 6` over the runner-up `c = 7` by 806421x;
* the best-fit **real** coefficient is `6.0000012400…`, i.e. the integer `6`
  to `1.24e-6` of one integer step.

## What this file does and does not establish

**Does.**  That the additive term is a *rigid integer count of `m_e` quanta*,
not a unit convention: §1 (relational mass / homogeneity), §2 (distinct counts
give distinct masses, with an exact gap), §3 (uniqueness of the count at
sub-`m_e` precision), §4 (the instance at `dim V_{(2,1)} = 2`).

**Does not.**  That the count is an *interaction* energy against an electron
probe.  §3 shows the count is forced by the data; it does not show *why* a
count denominated in `m_e` should appear at all.  `|S_3|` is the order of the
strand-permutation group and is supplied by the Hecke structure, so a
derivation must still connect that combinatorial count to the electron scale.
That connection is open — bean `qou-mrel`.  Nothing here may be cited as
proving the test-particle reading.

Scope: this is a scope-(a) structural result (see AGENTS.md §"Before declaring
'refuted'").  It rules out the *conventional* reading of the additive term.  It
does not rule in any particular physical reading.

## Base ring (§7c)

§1–§2 are pure algebra and are stated over a generic `[CommRing R]`.  §3–§4
concern *measured* masses — they use ordering and `|·|`, and they live on the
archimedean side of the wall — so they are stated over `ℝ`.
-/
import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Order.AbsoluteValue.Basic
import Mathlib.Tactic

namespace QOU.MassTheory.ElectronCountRigidity

/-! ## 1. The mass shape, and relational mass (generic `R`) -/

/-- The canonical nucleon-mass shape: a block multiplicity `d`, a constituent
energy `E`, and an integer count `c` of subtracted electron masses `mₑ`.

    `nucleonMass d E c mₑ = d * (E - c * mₑ)`

Instantiated in the corpus at `d = dim V_{(2,1)} = 2`, `c = |S₃| = 6`,
`E = m_μ · F_Bor`. -/
def nucleonMass {R : Type*} [CommRing R] (d : ℕ) (E : R) (c : ℕ) (mₑ : R) : R :=
  (d : R) * (E - (c : R) * mₑ)

variable {R : Type*} [CommRing R]

/-- **Relational mass — the factorisation.**  When the constituent energy is
itself `mₑ` times a dimensionless factor `G` (as it is: `E = m_μ·F_Bor` with
`m_μ = mₑ·Vol(4₁)/ℏ_q²`), the whole mass is `mₑ` times a dimensionless number.

There is no intrinsic mass in the formula: only the ratio `m/mₑ` is predicted. -/
theorem nucleonMass_factors (d : ℕ) (G : R) (c : ℕ) (mₑ : R) :
    nucleonMass d (mₑ * G) c mₑ = mₑ * ((d : R) * (G - (c : R))) := by
  unfold nucleonMass; ring

/-- **Relational mass — homogeneity of degree 1 in `mₑ`.**  Rescaling the
electron mass rescales the nucleon mass by exactly the same factor.

This is the falsifiable content of "mass is relational": a formula carrying an
`mₑ²` term, or an additive constant with mass dimension not supplied by `mₑ`,
would fail this. -/
theorem nucleonMass_homogeneous (d : ℕ) (G : R) (c : ℕ) (mₑ lam : R) :
    nucleonMass d (lam * mₑ * G) c (lam * mₑ)
      = lam * nucleonMass d (mₑ * G) c mₑ := by
  unfold nucleonMass; ring

/-! ## 2. The additive term is not absorbable (generic `R`)

The count enters with an exact, `E`-independent gap.  This is what makes it
*observable* — and it is the algebraic engine of §3. -/

/-- **Exact gap between counts.**  Changing the electron count from `c` to `c'`
shifts the mass by exactly `d · mₑ · (c' - c)`, independently of the
constituent energy `E`.

The `E`-independence matters: the shift cannot be reabsorbed by re-tuning the
multiplicative dressing at fixed `c`, because the dressing enters through `E`
and cancels here. -/
theorem nucleonMass_sub_count (d : ℕ) (E : R) (c c' : ℕ) (mₑ : R) :
    nucleonMass d E c mₑ - nucleonMass d E c' mₑ
      = (d : R) * mₑ * ((c' : R) - (c : R)) := by
  unfold nucleonMass; ring

/-- Deleting the additive term entirely (count `0`) shifts the mass by exactly
`d · c · mₑ` — for the corpus instance, `2 · 6 · mₑ = 12 mₑ ≈ 6.13 MeV`. -/
theorem nucleonMass_delete_term (d : ℕ) (E : R) (c : ℕ) (mₑ : R) :
    nucleonMass d E 0 mₑ - nucleonMass d E c mₑ = (d : R) * (c : R) * mₑ := by
  unfold nucleonMass; ring

/-! ## 3. Rigidity: the count is forced by the data (archimedean, `ℝ`)

The theorem that distinguishes a *count* from a *convention*.  A convention can
be changed without observable consequence.  This count cannot: any two integer
counts that both reproduce an observed mass to better than half the gap must be
the same integer. -/

/-- **Count rigidity.**  If integer counts `c` and `c'` both reproduce the
observed mass `m_obs` to within `d·mₑ/2`, then `c = c'`.

For the corpus instance `d = 2` the tolerance is exactly one electron mass:
*any* measurement of `m_p` good to better than `mₑ ≈ 0.511 MeV` pins the
electron count uniquely.  The actual residual at `c = 6` is `≈ 1.3·10⁻⁶ MeV`,
roughly `4·10⁵` times inside the window — so the count is not merely
determined, it is determined with enormous margin.

This is the formal statement that the additive term is **not** a unit
convention: a convention admits many equally good values, and this admits
exactly one. -/
theorem count_unique_of_close (d : ℕ) (hd : 0 < d) (E mₑ m_obs : ℝ) (hme : 0 < mₑ)
    (c c' : ℕ)
    (h  : |nucleonMass d E c  mₑ - m_obs| < (d : ℝ) * mₑ / 2)
    (h' : |nucleonMass d E c' mₑ - m_obs| < (d : ℝ) * mₑ / 2) :
    c = c' := by
  have hd' : (0 : ℝ) < (d : ℝ) := by exact_mod_cast hd
  have hdm : (0 : ℝ) < (d : ℝ) * mₑ := mul_pos hd' hme
  -- The two masses are within `d*mₑ` of each other.
  have hgap : |nucleonMass d E c mₑ - nucleonMass d E c' mₑ| < (d : ℝ) * mₑ := by
    calc |nucleonMass d E c mₑ - nucleonMass d E c' mₑ|
        = |(nucleonMass d E c mₑ - m_obs) - (nucleonMass d E c' mₑ - m_obs)| := by
          ring_nf
      _ ≤ |nucleonMass d E c mₑ - m_obs| + |nucleonMass d E c' mₑ - m_obs| :=
          abs_sub _ _
      _ < (d : ℝ) * mₑ / 2 + (d : ℝ) * mₑ / 2 := by linarith
      _ = (d : ℝ) * mₑ := by ring
  -- But that difference is exactly `d*mₑ*(c' - c)`.
  rw [nucleonMass_sub_count, abs_mul, abs_of_pos hdm] at hgap
  -- Hence `|c' - c| < 1` in `ℝ`, so the naturals agree.
  have hlt : |(c' : ℝ) - (c : ℝ)| < 1 := by
    by_contra hcon
    push_neg at hcon
    nlinarith [abs_nonneg ((c' : ℝ) - (c : ℝ))]
  by_contra hne
  have : (1 : ℝ) ≤ |(c' : ℝ) - (c : ℝ)| := by
    rcases Nat.lt_or_ge c c' with hcc | hcc
    · have : (c : ℝ) + 1 ≤ (c' : ℝ) := by exact_mod_cast hcc
      rw [abs_of_nonneg (by linarith)]; linarith
    · have hcc' : c' < c := lt_of_le_of_ne hcc (fun hh => hne hh.symm)
      have : (c' : ℝ) + 1 ≤ (c : ℝ) := by exact_mod_cast hcc'
      rw [abs_of_nonpos (by linarith)]; linarith
  linarith

/-! ## 4. The corpus instance -/

/-- **The proton instance.**  At `d = dim V_{(2,1)} = 2` the rigidity window is
exactly one electron mass.

Read against the numerics (`me_additive_term_structure.py`): the observed
residual at `c = |S₃| = 6` is `≈ 1.3·10⁻⁶ MeV`, far inside the window, while
the nearest competing integer `c = 7` misses by `≈ 1.02 MeV` — twice outside
it.  So `|S₃|` is the unique integer count compatible with the measured proton
mass. -/
theorem proton_count_unique (E mₑ m_obs : ℝ) (hme : 0 < mₑ) (c c' : ℕ)
    (h  : |nucleonMass 2 E c  mₑ - m_obs| < mₑ)
    (h' : |nucleonMass 2 E c' mₑ - m_obs| < mₑ) :
    c = c' := by
  refine count_unique_of_close 2 (by norm_num) E mₑ m_obs hme c c' ?_ ?_
  · simpa using (by push_cast; linarith [h] : |nucleonMass 2 E c mₑ - m_obs|
      < ((2 : ℕ) : ℝ) * mₑ / 2)
  · simpa using (by push_cast; linarith [h'] : |nucleonMass 2 E c' mₑ - m_obs|
      < ((2 : ℕ) : ℝ) * mₑ / 2)

end QOU.MassTheory.ElectronCountRigidity
