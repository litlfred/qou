import Mathlib.Tactic

namespace QOU.Conjectures

class WeakSpectralCompleteness where
  holds : True

instance canonical : WeakSpectralCompleteness where
  holds := trivial

end QOU.Conjectures
