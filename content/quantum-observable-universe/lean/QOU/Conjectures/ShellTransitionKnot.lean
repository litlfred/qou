import Mathlib.Tactic

namespace QOU.Conjectures

class ShellTransitionKnot where
  holds : True

instance canonical : ShellTransitionKnot where
  holds := trivial

end QOU.Conjectures
