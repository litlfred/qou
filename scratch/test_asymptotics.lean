import Mathlib.Analysis.Asymptotics.Asymptotics
import Mathlib.Topology.Instances.Real
import Mathlib.Analysis.SpecialFunctions.Pow.Real

open Filter Asymptotics

example (a_K : ℝ → ℝ) (writhe : ℤ) (avg_content : ℝ) : Prop :=
  IsO (𝓝 0) (fun h => a_K h - (1 + (writhe : ℝ) * avg_content * h)) (fun h => h^2)
