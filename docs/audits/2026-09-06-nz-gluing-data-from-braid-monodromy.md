# Neumann–Zagier gluing data derived from the braid word — Route E, first rung (2026-09-06)

**Beans:** `qou-n2cl` (attacked, stays open), `qou-yvyd` (two-bridge follow-on, new),
`qou-htsi` (convention-C excision, queued on owner instruction).
**Producer:** [`computations/probes/nz_gluing_from_braid_monodromy_probe.py`](../../computations/probes/nz_gluing_from_braid_monodromy_probe.py)
(25/25 assertions, `q0Anchor: independent`, no float64, no `q`, no Markov parameter).
**Lean:** `QOU/Mass/FigureEightGluingFromMonodromy.lean` (sorry-free; the algebraic spine).
**Owner request (verbatim):** *"Derive neumann-zaifler gluing data"*, after asking whether
restricting to Bring's surface could do more on `A_ω`.

## 0. What was asked, and what "derived" means here

The 2026-08-11 memo
([`2026-08-11-aomega-internal-derivation-attack-options.md`](2026-08-11-aomega-internal-derivation-attack-options.md)
§3, Route E) observed that the 3d-index of a knot — and hence the q→0 Stokes/DT count that
`A_ω = 3` is — needs only the Neumann–Zagier (NZ) gluing data of an ideal triangulation of
`S³∖K`. Every NZ datum in the corpus was **imported** from SnapPy (e.g. the transcribed rows in
`borromean_nz_adjoint_torsion.py`). "Derived" in this audit means: produced from the framework's
own braid data by a chain of theorems and exact combinatorics, with SnapPy nowhere in the
computation, and then **checked** against facts that were not inputs.

## 1. The chain

| step | input | output | status |
|---|---|---|---|
| Stallings–Gabai | canonical 3-braid `(σ₁σ₂⁻¹)²` (homogeneous; closure `4₁`) | fibre monodromy `φ = T_{γ₁}T_{γ₂}⁻¹ = [[2,1],[1,1]]`, `tr φ = 3`, `det(t−φ) = t²−3t+1 = Δ_{4₁}` | theorem (`stallings_monodromy_eq`, `stallings_charpoly`); trefoil control `σ₁σ₂σ₁σ₂ ↦ tr 1` |
| LR factorisation | `φ` | word `RL` (`R = [[1,1],[0,1]]`, `L = [[1,0],[1,1]]`) | exact |
| Floyd–Hatcher layering | word | one flip tetrahedron per letter, face gluings, closing map `M = [[1,1],[1,2]] = L·R` | exact combinatorics (the probe) |
| NZ rows | layered triangulation | edge rows `(1,1 \| 1,1)`, `(−1,−1 \| −1,−1)`; meridian `(−1,0 \| 0,−1)`; longitude `(1,−1 \| 1,−1)` (rect form `Π z^a(1−z)^b = ±1`) | exact combinatorics |

The edge equation reads `z₀ z₁ (1−z₀)(1−z₁) = 1` — Thurston's classical figure-eight equation,
which was **not** an input.

## 2. Checks (none of them inputs)

| check | derived | reference | result |
|---|---|---|---|
| exact solution | `z₀ = z₁ = ω` with `ω² − ω + 1 = 0` (symbolic solve) | `e^{iπ/3}` | ✓ (`figure_eight_gluing_at_sixth_root`, generic ring) |
| volume | `2·D(ω)` at 50 dps | `Vol(4₁) = 2·Cl₂(π/3)` | equal to `10⁻⁴⁰` |
| cusp modulus | developed cusp lattice, reduced | `2√3·i` | equal to `10⁻³⁰` |
| sister | same word, closing map `−M` | `m003`: same volume, hexagonal cusp | modulus `(1+√3 i)/2`, differs ✓ |
| NZ symplectic | Gram of `(edges, μ, λ)` | edges isotropic, `ω(μ,λ) = ±2` | `[[0,0,0,0],[0,0,0,0],[0,0,0,−2],[0,0,2,0]]` ✓ |
| adjoint torsion | `\|det J_NZ\|` from derived rows | `√3` (corpus value, obtained from SnapPy rows) | equal to `10⁻³⁰` |
| A-polynomial | resultant elimination of `z₀, z₁` from (edge, `H(μ) = M²`, `H(λ) = L²`) | `A_{4₁} = −M⁴ + L(1 − M² − 2M⁴ − M⁶ + M⁸) − L²M⁴` (memo §2c) | matches exactly, up to `L→±L^{±1}, M→±M^{±1}` |

**Addendum 2026-09-07 (bean `qou-6cu7`, citation only; the table above is unchanged).** Two of the
checks now have a held textbook form in Martelli, *An Introduction to Geometric Topology*
(`[martelli2016]`, `library/arxiv-1610.02592v3`): the **exact solution** row is Prop 14.1.8 +
Fig 14.7 (the two-tetrahedron, valence-6 triangulation with all shapes `e^{iπ/3}` is the
figure-eight complement; §14.1, Prop 14.1.7 for consistency/completeness ⇒ complete structure),
and the **NZ symplectic** row is Prop 15.2.9 / 15.2.11 (the incidence rows of an ideal
triangulation generate a Lagrangian subspace), with Cor 15.2.8 (`rk A = 2n − c`) giving the rank
a cross-knot gate should expect. The Guéritaud / Floyd–Hatcher layerings are *not* in that book
(§11.4 covers closed torus bundles only); those stay on Futer–Kalfagianni–Purcell.

The A-polynomial check is the one that pins the **cusp rows**: the meridian was identified as
the shortest vector of the derived cusp lattice and the longitude as its `2√3 i` partner; a wrong
`μ + kλ` would change the eliminated curve.

**General layering, second word.** `R²L` (trace 4): three tetrahedra, three edge classes, two
cusp cycles independent of the edge span; the complete structure has shapes **exactly** in
`ℚ(√−7)`: `z₀ = (5+√−7)/4`, `z₁ = z₂ = (3+√−7)/4` (numeric root identified, then re-verified
symbolically; `rrl_gluing_at_sqrt_minus_seven` proves the content row from `r² = −7`). Volume
`2.666744783449059790796712…`. The census value for the trace-4 once-punctured-torus bundle
(`m009`/`m010`) is `2.666744783449061` **as I recall it, not from a held source**; the witness
records that figure as data, not as an assertion.

## 3. Scope, stated without softening

* **The chain reaches `4₁` and nothing else in S³.** Step 1 needs a homogeneous braid whose
  closure is fibred with once-punctured-torus fibre; the hyperbolic knots with that fibre are
  `4₁` alone. `5₂` is not fibred. So the **cross-knot gate** of the `A_ω` arc (the `{3,4}`
  chirality split at `5₂`) is untouched by this probe.
* **What became internal is the NZ data, not `A_ω`.** The 3d-index and its Stokes/DT count are
  downstream computations on that data and were not re-run here. The memo's warning stands:
  recomputing `I_M` from NZ data "is re-importing GGM, not a categorical shortcut."
* **Orientation.** The ambient orientation is (fibre orientation) ∧ dt with class-O vertex
  ordering `(P,Q,S,R)`. `4₁` is amphichiral, so this probe cannot detect a global mirror. A
  chiral case must pin it before any `S⁺`/`S⁻` claim is made on derived data.
* **Convention.** No `q`, no Markov parameter, no anchor enters; the probe's AST import scan is
  an assertion (`no_convention_dependence_imports`). The owner's same-day instruction — *"as you
  write probes validate not dependent on convention C"* — is met by construction here, and
  queued as `qou-htsi` for the rest of the corpus (the value audit reports **136 confirmed C
  bindings, 25 blocking** on `main` today, against the 85 recorded in AGENTS.md).

## 4. Does every hyperbolic knot need its own decomposition, or a generating set?

Owner's question, verbatim: *"Do we need this decomposition for each of the hyperbolic knot
convolutions? (Or generating set thereof?)"*

NZ data is **per manifold** and is not multiplicative under skein moves, Murasugi sums, or the
Bring embeddability closure — a descendant's triangulation is not assembled from its
generators' triangulations. So there is no generating set of knots from which the rest follow.
What *is* generating is the **word**: the whole construction is a functor from a letter sequence
to a triangulation, and the letters `R, L` generate. Two classes are covered by one such
functor each:

1. **once-punctured-torus bundles** ← LR word of the monodromy (this audit; `4₁` and its
   sisters);
2. **two-bridge links** `S(p,q)` ← LR word of the continued fraction of `p/q` (Guéritaud 2006;
   Futer–Kalfagianni–Purcell §2.4, held as `library/arxiv-0808.2716v4`). `4₁ = S(5,2)` and
   `5₂ = S(7,3)` are both here, so this **one** functor reaches the cross-knot gate on derived
   data. Bean `qou-yvyd`.

Outside those two classes (e.g. `8₁₆`, `𝓑₃`) there is no word-to-triangulation functor in the
corpus or the library; the honest answer for a general hyperbolic knot in the dictionary is
"import the triangulation, and say so."

## 5. The PGL(ℂ) route — two different "Route E"s

The owner asked whether the PGL(ℂ) route was explored. Two things carry that name:

* **Binding-gap Route E, `PGL(3,ℂ)`** (`2026-09-05-route-e-the-induced-pgl3-rep-is-real-type.md`,
  beans `qou-g1m8`, `qou-47nf`): explored and pruned structurally — the induced `Sym²` of the
  hyperbolic holonomy is self-dual, hence real or quaternionic, hence fails the Sym² gate for
  every knot. The survivor is a `ρ₃` in the `PGL(3,ℂ)` character variety **away from the image of
  `PGL(2,ℂ)`**, i.e. the non-geometric component of the **Ptolemy variety** at `n = 3`
  (Garoufalidis–Goerner–Zickert, `library/arxiv-1207.6711v1`). That is bean `qou-47nf`, at
  `todo`.
* **`A_ω` Route E, NZ from Bring** — this audit.

They meet here in one concrete way: the Ptolemy variety at `n = 3` is computed **from a
triangulation**, and until today the only triangulation of `S³∖4₁` in the corpus was SnapPy's.
The layered triangulation derived above (two tetrahedra, face gluings explicit) is the input
`qou-47nf` needs, so its non-geometric component can now be computed on derived data. Nothing
in this audit claims anything about that component.

## 6. What this does not change

`A_ω = 3` remains certified-as-GGM-DT-count, conditional on `conj:stokes-dt-bps-bridge`; the
scalar avenue remains provably exhausted; `A_ω → S` remains unsupported (`qou-q3np`, open). The
gain is one rung: the triangulation whose 3d-index GGM's Stokes constants resum is now a
theorem-plus-combinatorics of the braid word, for the one knot where that chain exists.
