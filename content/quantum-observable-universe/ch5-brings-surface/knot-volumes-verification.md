The hyperbolic volume claims in this paper are independently verified by
computing them from scratch using the SnapPea kernel (SnapPy 3.3).

**Verified assertions** (11 total, all passing):

| Claim | Computed | Expected | Tolerance | Source |
|-------|----------|----------|-----------|--------|
| $\mathrm{Vol}(0_1)$ — unknot | $0$ | $0$ | $10^{-10}$ | Trivial |
| $\mathrm{Vol}(3_1)$ — trefoil | $0$ | $0$ | $10^{-10}$ | Torus knot |
| $\mathrm{Vol}(4_1)$ — figure-eight | $2.02988321282$ | $2.02988321281931$ | $10^{-10}$ | OEIS A091518 |
| $\mathrm{Vol}(5_1)$ — cinquefoil | $0$ | $0$ | $10^{-10}$ | Torus knot |
| $\mathrm{Vol}(5_2)$ — three-twist | $2.82812208833$ | $2.82812208832975$ | $10^{-10}$ | SnapPy census |
| $\mathrm{Vol}(7_1)$ — torus(7,2) | $0$ | $0$ | $10^{-10}$ | Torus knot |
| $\mathrm{Vol}(L2a1)$ — Hopf link | $\approx 0$ | $0$ | $10^{-6}$ | Torus link |
| $\mathrm{Vol}(L6a4)$ — Borromean | $7.32772475342$ | $7.32772475341775$ | $10^{-10}$ | OEIS A006752 |

**Derived quantities** (from $\mathrm{Vol}(4_1)$ and CODATA 2022):

| Quantity | Computed | Expected | Tolerance |
|----------|----------|----------|-----------|
| $m_\mu / m_e$ | $206.7682830$ | $206.7682830$ | $10^{-7}$ |
| Substrate $q$ | $1.10998$ | $1.10997$ | $10^{-3}$ |
| $\hbar_q = 1 - 1/q$ | $0.09908$ | $0.09905$ | $10^{-3}$ |

**Reproducibility**: Run `python3 computations/knot-volumes.py` to regenerate
the witness file.  Requires `pip install snappy`.

The witness file `computations/knot-volumes.witness.json` is committed to the
repository for CI verification.  Lean declarations that depend on these
volumes use `axiom` with `-- Ref: [computation]` annotations pointing to
this witness.
