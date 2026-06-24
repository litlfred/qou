import Mathlib.Tactic

namespace QOU.Conjectures

class MagicNumbersBring where
  holds : True

instance canonical : MagicNumbersBring where
  holds := trivial

end QOU.Conjectures
