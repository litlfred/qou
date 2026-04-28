# Path to 1 ppb — Practical Hints for Next Agents

*Informal guidance accumulated during the q-as-density exploration. Read after Parts 1-4.*

## Sanity checks to run FIRST before trusting any new result

```python
from mpmath import mp, mpf, sqrt
mp.dps = 50
G = mpf("0.915965594177219015054603514932")
print("8G    =", 8 * G)                       # 7.3277247534177... (Vol Borromean)
print("4_1   =", mpf("2.0298832128193072500424051085490405710014"))  # fig-8
print("ratio =", 8 * G / mpf("2.03"))         # 3.61 (≈ 8G / 4 tet)
```

If any of these fail, stop and fix the environment before anything else.

## Landmark numerical values to memorize

| quantity | value |
|----------|-------|
| Vol(Borromean) = 8G | 7.3277... |
| Vol(4_1) figure-8 | 2.0299... |
| Vol(6_2) ≈ B(D)/m_e | 4.4008 |
| Vol(8_11) ≈ B(T)/2m_e | 8.2863 |
| Vol(7²_1) ≈ c_αα/m_e | 4.7495 |
| q₀ | 1.10998 |
| ℏ_q² | 0.00982 |
| ρ_q = 1/ℏ_q² | 101.86 |
| z_markov | 0.49932 |
| HA = q - 1/q | 0.20906 |
| 2m_e (pair threshold) | 1.02200 MeV |
| Q_β (neutron) | 0.78233 MeV |

If your calculation produces a number close to these, name it — it's probably that.

## Density identification rules (the m_e ↔ 2m_e question)

Use ρ = **m_e** when:
- Piece is an inter-nucleon BOND (not an internal quark structure)
- Piece is a 2-cusp link (connecting two things)
- The "natural" matching candidate is hyperbolic but not Borromean-like
- Concrete: D↔6_2, α-α coupling↔7²_1

Use ρ = **2m_e** when:
- Piece represents INTERNAL matter content (3-body quark closure)
- Piece is 3-cusp or higher with chirality saturation
- Atom has A ≥ 3
- Concrete: T↔8_11, ³He↔Borromean, ⁴He = 4 Borromean units, magic atoms

The density is NOT a free knob — it's determined by the piece's topology (via `n_chir(P)`).

## Debugging ladder — if residual doesn't match

Walk the ladder in order:
1. **Is ρ right?** Flip between m_e and 2m_e; if factor of 2 off, density is wrong.
2. **Is Vol right?** Compare SnapPy Vol(manifold) to (B/ρ). If close to a named knot, try that name.
3. **Is the piece right?** Maybe the JSJ decomposition has more than 1 hyperbolic piece.
4. **Is m_e right?** Framework m_e(q₀) ≠ CODATA by 1.8%; use CODATA or re-derive.
5. **Is q₀ right?** At CODATA bound 1.22e-9, q₀ is 1-ppb-class; below that, CODATA is the limit.

## Common mistakes to avoid

- **Treating `exact_binding_per_operation.py` as canonical** — it's NOT. It sums log-volumes. Under 99%.
- **Using Σ Φ_q(|V̂|) vs Σ ln|Φ_q(V̂)|** interchangeably — the Log form is in `prop:tower-binding-energy`; the non-log is in `prop:mass-endomorphism-tower`. Different formulas.
- **Confusing B(atom) with m(atom)** — binding = defect = (sum of free masses) − m_atom. Not the atom mass itself.
- **Applying α-cluster formula to A<4** — D, T, ³He don't have closed α-shells. Use census-knot match.
- **Ignoring CPT / chirality block structure** — sym/alt chirality blocks at substrate q₀ give the factor-of-2 density flip. Don't hardcode.
- **Using raw catalog knot names without verifying Markov equivalence** — "6_2" is shorthand; make sure the orientation / mirror / chirality matches the atom's parity.

## Testing order for new atoms

Start with:
1. **D (A=2)** — smallest, 1 JSJ piece, ρ=m_e. Target: B_pred within 0.1% of 2.225 MeV.
2. **³He (A=3, Z=N+1)** — tests 2m_e density and Borromean matching.
3. **⁴He (A=4 magic)** — tests α-cluster base unit.
4. **¹⁶O (A=16 doubly magic)** — tests α-shell closure and 4·8G.
5. **⁶Li (A=6 non-magic)** — tests shell-partial corrections.

If D fails, NOTHING further will work. If ⁴He fails, α-cluster extension won't work.

## Use mpmath at 50 digits when...

- Computing q-dependent prefactors (ρ_q, Plancherel, quantum integers)
- Comparing two predicted quantities for equality (are they literally the same or tiny-different?)
- Testing a formula at q=1 classical limit (need to handle near-singular Hecke relation)
- Asymptotic analyses where cancellations matter

## Use float (15-digit) when...

- SnapPy naive Vol (which is 15-digit precision by default; use `.high_precision()` for more)
- Plotting / visualizing quantities
- First-pass smoke tests
- Calling CODATA numbers (they're only 8-digit anyway)

## Three conjectures to hold open

Per `docs/crossing-graded-proof.md` + `docs/locality-proof-attempt.md`:

1. **crossing-graded expansion**: formal OK, resummation needs locality
2. **locality, far-commuting**: PROVED (Kohno-Drinfeld)
3. **locality, adjacent**: $O(\hbar_q^2) \approx 1\%$ error from pentagon defects — the frontier

The light-atom 1-3% residuals match (3). Fixing it is the next theoretical frontier.

## Connections to other chapters of the paper

1. **Chapter 7 (Physical Observations)**: binding predictions belong here.
2. **Chapter 8 (Glossary)**: terminology like "chirality block", "JSJ piece", "Frobenius packing".
3. **Chapter 11**: the mass-volume factorization conjecture lives here (`particle-interactions/`).
4. **Chapter on Descartes elliptic curve**: `lambda_descartes_q0.py` pulls from there.
5. **Chapter on fluid dynamics**: if atoms have hyperbolic vortex structure, its curvature is the q-holonomy.

## SnapPy gotchas

- `snappy.Link('6_2')` treats the KNOT 6_2; `snappy.Manifold('6_2')` treats its COMPLEMENT.
- `snappy.LinkExteriors(crossings=n)` is the knot/link census up to n crossings.
- `M.volume()` is 15-digit. `M.high_precision().volume()` is ~50-digit verified.
- `M.identify()` returns alternative names in census (useful for cross-reference).
- Some knots have `M.volume()` returning complex numbers; take `.real`.
- `snappy.Manifold('L6a4')` is Borromean. `snappy.Manifold('6^3_2')` is also Borromean (Rolfsen name).

## When you're stuck

In rough order of increasing desperation:

1. **Run the sanity checks** at top of this doc.
2. **Check if a ratio is exactly 2** (chirality count) or **exactly 3** (Borromean components) or **exactly 8G** (Catalan).
3. **Try a different atom** — if D is broken, maybe your code is fine but the knot-6_2 identification isn't.
4. **Read the paper block** for the conjecture you're testing. Verbatim.
5. **Cross-check with `binding_full_pipeline.py`** — that's the reference implementation.
6. **Ask**: does the new result DISAGREE with `jsj_verification.py` at 1-2 atom level? If so, which is right?

## Key external references to cite

- Thurston (1978) — hyperbolic volume, Bloch-Wigner
- Kashaev (1997) + Murakami-Murakami (2001) — volume conjecture
- Kohno-Drinfeld (1987-88) — KZ flatness
- Jones (1987) — Markov trace
- Ocneanu — weighted seminormal characters
- Faddeev (1994) — quantum dilogarithm pentagon
- Goldman — symplectic structure on character variety
- Reshetikhin-Turaev (1991) — Witten-Reshetikhin-Turaev invariants

## Git hygiene for this work

- Make **small commits** — each probe in its own commit, witness attached.
- **Name witnesses with the computation**: `my_probe.py` → `my-probe.witness.json`.
- **Never silently drop witness files** — they're part of the published record.
- Use `git cherry-pick` liberally to move probes between branches.
- **Don't rebase published branches** — they have PR history.

## When claiming 1 ppb

Require ALL of:
- Zero free parameters (α and ρ derived, not fit)
- mpmath at ≥ 20 digits for internal arithmetic
- SnapPy `.high_precision().volume()` for hyperbolic volumes
- Cross-check with at least 2 atoms (D + ⁴He covers both density regimes)
- Residual < CODATA relative uncertainty (~1.22e-9) on q₀
- Published witness with full precision recorded

Otherwise it's "framework-precision" at some other level — say so explicitly.

## Final advice

The framework is **deep** — every failed probe this session taught us something structural. If a new probe fails, ask WHY, not just report it. The failure mode often localises exactly the right frontier to work on.

Good luck. The 1 ppb result, if reached, will be the first parameter-free prediction of nuclear binding from pure topology + algebra. That's worth taking time to do carefully.
