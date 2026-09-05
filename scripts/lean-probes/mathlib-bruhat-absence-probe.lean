import Mathlib.GroupTheory.Coxeter.Length
import Mathlib.GroupTheory.Coxeter.Inversion

open Lean Elab Command in
run_cmd do
  let env ← getEnv
  let mut bruhat := 0
  let mut subword := 0
  let mut coxeterTotal := 0
  let mut hits : Array Name := #[]
  for (n, _) in env.constants.toList do
    let s := n.toString
    if (s.splitOn "ruhat").length ≥ 2 then
      bruhat := bruhat + 1
      if hits.size < 12 then hits := hits.push n
    if (s.splitOn "ubword").length ≥ 2 then
      subword := subword + 1
      if hits.size < 12 then hits := hits.push n
    if (s.splitOn "Coxeter").length ≥ 2 then
      coxeterTotal := coxeterTotal + 1
  logInfo s!"Coxeter constants reachable: {coxeterTotal}"
  logInfo s!"  containing 'ruhat' : {bruhat}"
  logInfo s!"  containing 'ubword': {subword}"
  logInfo s!"  sample: {hits.toList}"
