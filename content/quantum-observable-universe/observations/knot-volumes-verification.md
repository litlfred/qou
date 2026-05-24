The hyperbolic volume claims in this paper are independently verified by
computing them from scratch using the SnapPea kernel (SnapPy 3.3).

**Verified assertions** (11 total, all passing):

See [Table 1](#tbl:knot-volumes-verification-table1-data).

**Derived quantities** (from $\mathrm{Vol}(4_1)$ and CODATA 2022):

See [Table 2](#tbl:knot-volumes-verification-table2-data).

**Reproducibility**: Run `python3 computations/knot-volumes.py` to regenerate
the witness file.  Requires `pip install snappy`.

The witness file `computations/knot-volumes.witness.json` is committed to the
repository for CI verification.  Lean declarations that depend on these
volumes use `axiom` with `-- Ref: [computation]` annotations pointing to
this witness.
