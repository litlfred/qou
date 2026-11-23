# Generator for `QOU/QBeta/HydrogenFlavourSplit.lean`

`python3 -I gen2.py emit` in this directory writes `HydrogenFlavourSplit.lean`. It needs exact sympy only.

- `gen.py`: the weight blocks `z = 1, 2, 3` of the level-2 Jimbo braiding on four strands, and the words.
- `intw.py`, `intw_emit.py`: solve for the intertwiners `P32`, `P21` and the matrices `N32`, `N21`. These give `tn − q⁻²tp = Σ tr(M_z W_z)`, and that sum cancels by cyclicity.
- `intw_tmpl.lean`: the hand-written proof of `left_ratio`.

Run `python3 -I gen.py check` for the sympy closed forms. No numerical value enters.
