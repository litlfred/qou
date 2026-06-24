import Mathlib.Tactic

namespace QOU.Conjectures

class KnotFactorFrobeniusPairing where
  holds : True

instance canonical : KnotFactorFrobeniusPairing where
  holds := trivial

end QOU.Conjectures
