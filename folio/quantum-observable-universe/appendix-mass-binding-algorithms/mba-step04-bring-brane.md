**Algorithm (Bring brane constants).**
*Return the substrate constants of the
Bring surface $\mathcal{E}_q$ (Euler characteristic $\chi = -6$,
six torus-knot embeddings, fundamental-group presentation) used by
every downstream step.*

### Input

- *(none — the Bring brane is a fixed geometric object).*

### Output

- *Tuple $(\chi, g, k, \mathrm{Aut})$ with $\chi = -6$, genus
  $g = 4$, $k = 6$ torus-knot embeddings $T_{p_i, q_i}$, and
  $\mathrm{Aut}(\mathcal{E}_q) = S_5$.*

### Algorithm

```
1. Return χ = -6, g = 4.
2. Return the six embeddings T_{p_i, q_i} for i = 1, …, 6.
3. Return Aut group S_5 (the small simple group acting on
   Bring's coordinate ring).
```

### Correctness conditions

*Settled by [the Bring-surface definition](#def:brings-surface): the
Bring surface is uniquely characterised (up to isomorphism) by
its Euler characteristic and the six-fold $S_5$-symmetric
embedding. No upstream calibration; the values are categorical
constants.*

### Complexity

*$O(1)$ — table lookup.*

### Python API entry point

*The Bring constants are produced by the canonical script
[`bring_chiral_fibre_figure.py`](../../../computations/bring_chiral_fibre_figure.py),
which emits the witness JSON consumed by every downstream step.
The substrate parameter $q_0$ and its derived constants live in
[`qou_substrate.constants`](../../../tools/qou-substrate/python/qou_substrate/constants.py).*

### Witness contract

*Canonical witness:
[`bring-chiral-fibre-figure.witness.json`](../../../computations/bring-chiral-fibre-figure.witness.json).
Records the six torus-knot embeddings, their chirality, and the
$S_5$ action.*

### Notes

*The Bring brane is **not** a calibration input — it is a
mathematical constant fixed by the rigid-monoidal premise. The
choice of $\chi = -6$ is what gives the substrate its
6-knot decomposition and ultimately the torsion structure that
feeds Step 7 (GB filtration).*
