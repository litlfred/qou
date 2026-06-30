-- Ref: [manuscript] Ch. 6, §atomic-braid
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

/-- Mass number A = Z + N (a derived quantity, not independent data). -/
def NeutralAtom.A (atom : NeutralAtom) : Nat := atom.Z + atom.N

/-- Total strand count = A + Z (nucleons + electrons). -/
def NeutralAtom.totalStrands (atom : NeutralAtom) : Nat := atom.A + atom.Z

/-- The total strand count of an atomic braid is `A + Z = Z + N + Z`. -/
theorem atomic_braid_crossing_count (atom : NeutralAtom) :
    atom.totalStrands = atom.Z + atom.N + atom.Z := by
  simp [NeutralAtom.totalStrands, NeutralAtom.A]
