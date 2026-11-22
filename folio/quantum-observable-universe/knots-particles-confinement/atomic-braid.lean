-- Ref: [leitner2026] Ch. 6, §atomic-braid
-- Atomic braid in H_{A+Z}(q)

/-- Particle pair type for crossing coefficients. -/
inductive PairType where
  | pp : PairType  -- proton-proton
  | nn : PairType  -- neutron-neutron
  | pn : PairType  -- proton-neutron
  | pe : PairType  -- proton-electron
  | ne : PairType  -- neutron-electron
  | ee : PairType  -- electron-electron
  deriving DecidableEq, Repr

/-- The **atomic braid** of a neutral atom (Z, N) as an element
    of H_{A+Z}(q), where A = Z + N.

    - A strands for nucleons
    - Z strands for electrons
    - Ground-state ordering via nuclear permutation minimizing Φ₁
    - Greedy electron insertion producing ep pairs -/
structure NeutralAtom where
  /-- Atomic number (proton count). -/
  Z : Nat
  /-- Neutron number. -/
  N : Nat
  /-- Mass number A = Z + N. -/
  A : Nat := Z + N
  /-- Total strand count = A + Z (nucleons + electrons). -/
  totalStrands : Nat := A + Z

/-- Strand count of a default-constructed neutral atom `(Z, N)`:
    with the field defaults `A = Z + N` and `totalStrands = A + Z`,
    the total strand count is `Z + N + Z = A + Z`.

    Stated for `⟨Z, N⟩` (defaults applied) because for an arbitrary
    `NeutralAtom` the `A` and `totalStrands` fields are independent
    and may be set to non-default values. -/
theorem atomic_braid_crossing_count (Z N : Nat) :
    ({ Z := Z, N := N } : NeutralAtom).totalStrands = Z + N + Z := by
  rfl
