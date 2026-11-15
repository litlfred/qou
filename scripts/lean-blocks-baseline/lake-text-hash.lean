import Lake
open Lake
def main (args : List String) : IO Unit := do
  for p in args do
    let t ← IO.FS.readFile p
    IO.println s!"{(Hash.ofText t).val}\t{p}"
