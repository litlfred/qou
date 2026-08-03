import QOU.Basic

/-!
# QOU.ParticleInteractions.AtomKnot — atom as a closed braid via NF block decomposition

Atom-knot of type (Z, N): closed braid with NF
T_w = T_{w_q^Z} · T_{w_qbar^N} · T_{w_inter} on n(K) = 3(Z+N) strands.

LaTeX: `\label{def:atom-knot}`
-/

namespace QOU.BraidKnot

universe u

/-- **Atom-knot** of type `(Z, N)`.

    Records the proton-quark NF block, the neutron-quark NF block,
    and the inter-nucleon connector permutation.  The total NF is
    the product of the three blocks; the closed braid is the Markov
    closure of any braid representative realising this NF. -/
structure AtomKnot where
  /-- Proton count Z. -/
  Z : ℕ
  /-- Neutron count N. -/
  N : ℕ
  /-- Proton-quark NF block (encoded as a list of generator indices). -/
  protonBlock : List ℕ
  /-- Neutron-quark NF block. -/
  neutronBlock : List ℕ
  /-- Inter-nucleon connector permutation. -/
  interBlock : List ℕ

/-- Braid index `n(K) = 3(Z + N)`. -/
def nStrands (K : AtomKnot) : ℕ := 3 * (K.Z + K.N)

end QOU.BraidKnot
