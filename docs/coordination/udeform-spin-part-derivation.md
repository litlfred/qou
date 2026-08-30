# Coordination — derive the SPIN part of u(q₀) (continuation of #4391)

**Goal.** Close (or honestly bound) the last open half of the
`conj:binding-qbeta-complex-volume` S-channel map `u(q₀)`. After #4372/#4391
the picture is:

- `V₄₁(u)` concrete; `Im 𝔙₄₁ = (√3/4)(Re²u − Im²u)` (proved `imV₄₁`).
- The **real-boost** part of `u(q₀)` is geometrically fixed: `Re u = ln q₀`
  (`meridian-holonomy-boost.md`, proved) — muon sign-correct + ballpark, but
  **refuted as the full map** (nearly constant across the ~1e-8-apart anchors;
  can't give `S(proton)<0`).
- The **sign-flip** needs `Im²u > Re²u` at the proton anchor — the meridian
  holonomy's **boost→spin transition** (real q₀ boost vs `|q|=1` spin). The
  spin/imaginary part of `u(q₀)` is the OPEN piece.

## Workplan (beans milestone `qou-h2k4`)

- **[SP1] (`qou-x581`) geometric origin of the spin part.** Candidate: the
  **fibre** meridian holonomy. `PhiBSArgumentIdentification` fixes the physical
  regime as the fibre branch (real `b` ⇒ `|q_b|=1`), with
  `q_b = e^{i·ln q₀/2}` (`fibreQParam_fibreB`, proved). So the fibre log
  meridian holonomy is `log q_b = i·(ln q₀/2)` — a **pure spin** (imaginary),
  exactly the `|q|=1` compact regime. Test `u = ln q₀ + i·(ln q₀/2)` (boost +
  fibre spin) under `Im 𝔙₄₁`; derive-then-check, no fit.
- **[SP2] (`qou-4kr1`) the hypersensitivity crux (the hard open frontier).**
  `S(muon)/S(proton)` flips sign and changes magnitude ~4× while the anchor
  q₀'s differ by only ~1e-8 (slope `k≈2.2e6`, #3773 hypersensitivity witness).
  A *smooth* function of q₀ (boost `ln q₀`, spin `ln q₀/2`) cannot be that
  hypersensitive — so the sign-flip source must be a **resonance / near-
  degeneracy / fractional-part** structure, not a smooth geometric term. This
  is the genuine open question: what geometric quantity is hypersensitive to
  q₀ at the 1e-8 level? (Connects to the c₃ flip-flop hypersensitivity saga.)

## Discipline

Derive-then-check; anti-fit (every component of `u` must come from geometry —
`ln q₀` boost, `ln q₀/2` fibre spin — never chosen to match `S`);
anti-laundering (no `SDeformedVolumeChannel` instance fabricated; if the
smooth boost+spin candidate cannot reproduce the hypersensitive flip, that is
an honest scope-(a) result — the map needs a non-smooth/resonance ingredient,
recorded not buried). Expected likely outcome: **SP1 sharpens the smooth part;
SP2 is the residual open crux** (a smooth u cannot be hypersensitive).

## SP1 outcome (2026-07-27): smooth geometric fibre-spin REFUTED (scope-(a))

Probe [`qbeta_spin_part_udeform_probe.py`](../../computations/qbeta/qbeta_spin_part_udeform_probe.py)
(50 dps, exit 0, 4 assertions). Tested `u = ln q₀ + i·(ln q₀/2)` (boost + fibre
holonomy spin) under `Im 𝔙₄₁ = (√3/4)(Re²u−Im²u)`:

- The fibre spin angle `ln q₀/2` is **smaller** than the boost `ln q₀`
  (`Im u/Re u = 1/2`), so `Re²u > Im²u` ⇒ `Im 𝔙₄₁ = +0.003536 > 0` at **both**
  anchors (muon sign-correct, proton **wrong sign**). Smooth boost+fibre-spin
  **cannot** reach `S(proton) < 0` — REFUTED as the full map (scope-(a)).
- Reaching the diagonal (`Im²u > Re²u`, needed for `S<0`) requires `Im u > Re u
  = ln q₀ ≈ 0.104`. Even the **full** fibre angle `ln q₀` only reaches the
  diagonal (`Im 𝔙 = 0`), never past it. No smooth geometric holonomy from
  `q₀≈1.11` supplies `Im u > Re u`.

**Sharpened SP2 (the open crux).** The sign-flip source therefore **cannot** be
a smooth geometric meridian holonomy. It requires a spin part that is (i)
*larger than the boost* (`Im u > Re u`) AND (ii) *hypersensitive* to q₀ at the
~1e-8 anchor gap (slope `k≈2.2e6`). A smooth function of q₀ is neither. So `u(q₀)`,
if it exists, is a **non-smooth / resonance / near-degeneracy** object — the same
hypersensitivity class as the c₃ flip-flop saga.

**Honest status.** This is a scope-(a) refutation of the *smooth geometric* `u(q₀)`
candidate, not a closure and not a scope-(b) exclusion of the channel (a different,
non-meridian deformation could in principle carry a larger imaginary part). Per the
anti-fit discipline, a resonance `u(q₀)` will **not** be constructed to match the
anchors here — that would be a fit. Identifying (or proving impossible) a *derivable*
non-smooth spin part is the remaining open frontier (SP2, `qou-4kr1`), left open.

## [W] Winding lattice (2026-07-27): SP1's diagonal wall FALLS

Author steering: *"associate to a braid word a geodesic (flow) on the torus for the
particle/vortex path; odd and even channels; sinh/cosh should align at this geometry"*
— and *"this is mapped on Bring's surface"*. Probe
[`qbeta_cusp_lattice_geodesic_probe.py`](../../computations/qbeta/qbeta_cusp_lattice_geodesic_probe.py)
(50 dps, exit 0, 5 assertions). Two **proved** corpus inputs, no fit: meridian
log-holonomy `= ln q₀` (`meridian-holonomy-boost`) and cusp shape `ω = e^{iπ/3}`
(`cusp-shape-bar-parity`). The `(m,ℓ)` winding geodesic has `u = ln q₀·(m+ℓω)` and

$$
  \mathrm{Im}\,\mathfrak{V}_{4_1} = \tfrac{\sqrt3}{16}(\ln q_0)^2\,\bigl[(2m+\ell)^2 - 3\ell^2\bigr]
$$

exactly (residual `3e-53`) — the **norm form of `ℤ[√3]`** (disc 12), matching the
cusp's own `√−3` (`barOdd(ω)² = −3`). Consequences:

- **The sign is ARITHMETIC, not q₀-sensitive.** `sign Im 𝔙₄₁ = sign G(m,ℓ)`, a discrete
  invariant of the winding carrying **no q₀-dependence at all**. Different knots ⇒
  different winding slopes ⇒ sign flip, with no hypersensitive `u(q₀)` required. This is
  the first *derivable, non-smooth* candidate for the SP2 crux, and it dissolves the
  premise that the flip must come from a 1e-8 q₀ gap.
- **SP1's wall falls.** Longitude `(0,1)`: `Im u/Re u = √3 > 1` ⇒ `G = −2 < 0`, the
  spin-dominated regime SP1 called unreachable. SP1's *"no geometric holonomy from
  q₀≈1.11 supplies `Im u > Re u`"* was an artifact of its **off-lattice** fibre ansatz
  `u = ln q₀(1 + i/2)`; the 60° cusp angle supplies `√3` free of q₀. Meridian `(1,0)`
  gives `G = +4`, reproducing the #4391 boost value to 40 digits (cross-check).
- **sinh/cosh alignment is exact.** `G = 1` is the **Pell equation** `x²−3y²=1`, whose
  solutions are the units `(2+√3)ⁿ` of `ℤ[√3]`: `x_n = cosh(nρ)`, `√3·y_n = sinh(nρ)`
  with fundamental rapidity `ρ = arccosh 2 = ln(2+√3)`. Under `(barEven, barOdd) =
  (2x, 2√3 y)` this is **exactly** the proved holonomy hyperbola `barEven² − barOdd² = 4`.
  *The proved boost identity IS the Pell equation of the cusp winding lattice*, and its
  integer solutions are a discrete boost subgroup of rapidity `n·arccosh 2`.
- **No null geodesic** (`√3` irrational ⇒ `G ≠ 0` on all 14640 classes tested): every
  class is strictly boost- or spin-dominated. Spin sector = winding-slope window
  `m/ℓ ∈ (−1.366, 0.366)`, i.e. integer slopes `{0, −1}` (longitude-dominated).

**Honest negative (scope-(a)).** At the derived scale `c = ln q₀` the magnitudes are
**not** reproduced: `S_muon/B ≈ 8.22` and `S_proton/B ≈ −33.48` are not `G` values
(spectrum ≤50: `4, 6, 16, 22, 24, 36, 46`), and the canonical meridian/longitude pair
predicts ratio `−1/2` against the observed `−4.075`. **Fit trap:** 1833 `G`-value pairs
match that ratio within 1% by chance, so ratio-matching here is *not evidence*. No
`(m,ℓ)` adopted; sign mechanism only.

## Literature drop (owner uploads `eb5ecc5c`, `cc8cc47a`, 2026-07-26) — triage

Nine PDFs landed on `main`, several decisive for the [W] result:

| File | Paper | Bearing |
|---|---|---|
| `CuspShapes.pdf` | Dang–Purcell, *Cusp shape and tunnel number* | **Sharpens the fit trap to a theorem.** Cusp shapes of tunnel-number-one manifolds are **dense in the Teichmüller space of the torus**. For general `τ` the form is `G_τ = (m+ℓτ₁)² − ℓ²τ₂²`; density ⇒ choosing a knot to get a desired cusp shape is an *unbounded* fit resource. The [W] `W5` negative is now literature-backed, not just a heuristic count. |
| `0410233v4.pdf` | Purcell, *Cusp shapes under cone deformation* | **The right tool for the standing objection** "does `ω` move with q₀?" Bounds cusp-shape change under cone deformation preserving the cusp, in terms of the change near the singular locus alone. Quantifies whether `ω = e^{iπ/3}` is rigid to the substrate deformation — i.e. whether [W]'s no-q₀-dependence survives. Top follow-up. |
| `4GEO-DEDI-REV.pdf` | Baseilhac–Benedetti, *Quantum Teichmüller invariants of fibred cusped 3-manifolds* | **The literature home of the author's picture.** A braid-closure complement *is* a fibred cusped 3-manifold (punctured-disc mapping torus); the braid is the monodromy and the "flow" is the suspension flow. Reduced quantum hyperbolic invariants of pseudo-Anosov maps as intertwiners of quantum-Teichmüller local reps. |
| `agt-v7-n2-p13-s.pdf`, `0611504v1.pdf` | Baseilhac–Benedetti, *Quantum hyperbolic geometry* (AGT 7 (2007) 845–917; arXiv v1) | QHFT machinery behind `𝔙 = Vol + i·CS` at roots of unity — the published + preprint pair. |
| `topological.invariance.3Dindex.pdf` | Garoufalidis–Hodgson–Rubinstein–Segerman, *1-efficient triangulations and the index of a cusped hyperbolic 3-manifold* | 3D index (Dimofte–Gaiotto–Gukov) promoted to a **topological invariant**: a canonical `q`-series attached to a cusped hyperbolic 3-manifold. Strong candidate for the *fibre-level* q-series the `c_k`/Habiro thread wants (AGENTS.md Im(q) fibre-vs-observable framing). |
| `0806.4741v1.pdf` | Bieliavsky–Detournay, *Deformation quantizations of the hyperbolic plane* | Deformation-quantization side of the `q`-hyperbolic structure. |
| `1311.6841v1.pdf` | Dupuis–Girelli, *Observables in LQG with a cosmological constant* | `q`-deformed observables; external comparison point. |
| `2507.13873v1.pdf` | Belaey–Mertens–Papalini, *Probing the singularity at the holographic screen via q-holography* | Recent (2025-07) `q`-deformed spacetime emergence; external comparison point. |

**Net effect on [W].** The sign mechanism stands as *derived for the proved `4₁` cusp
shape*. Dang–Purcell **strengthens the honest negative** — the cross-knot extension is
a dense fit resource, so magnitudes must not be pursued by cusp-shape selection.
Purcell's cone-deformation bounds are the next real check (is `ω` rigid under the
substrate deformation?), and Baseilhac–Benedetti supply the fibred/monodromy framework
the author's geodesic-flow picture actually lives in.

## Coordination — takeover of PR #4405 + critical review (2026-07-27)

PR #4405 (`claude/delta-lambda-magnitude-derivation-2026-07-27`, Δ_λ magnitude via
ϑ_K + Stokes) stalled at quota; taken up per owner request. Pushed `540d5fd5` there:
37 scratch-litter files removed, `DeltaLambdaBindingAssembly.lean` header corrected
(promised a nonexistent `wall_forces_stokes`; its "real substrate cannot source ϑ_K"
narrative leaned on wall theorems that PR's own audit shows are wrong), bean
`qou-3kos` re-scoped from "A_ω = 3 REQUIRED" to scope-(a) conditional (anchor-
inversion viability under the questioned linear form; A ≳ 2.05 bound, A = 3 not
derived). Full review in the PR comment.

**Convention cross-validation.** #4405's A-polynomial audit confirms the
`FigureEightComplexVolume` κ = +√3/4 half-potential convention — the same κ this
branch's winding-lattice identity and parity probes are built on. The sin-vs-cos
bug is confined to `ArgUPhaseBranchSelection.nzImVolume` (fix pending, bean
`qou-u14x`). Consequence for the sign story: the "phase wall" is dead — Im 𝔙₄₁ > 0
on the real ray — so the surviving statement is this branch's: the diagonal
crossing is a discrete winding/parity datum, not a q₀-hypersensitivity.

**Lattice ⟷ ϑ_K dictionary.** ϑ_K = Im 𝔲_K is quantized on the cusp lattice:
ϑ_{m,ℓ} = (√3/2)·ℓ·ln q₀ ≈ 0.0902·ℓ. The #4405 back-solved values (0.203 proton,
0.059 muon under A = 3) are NOT on this lattice — consistent with the [W]/[D4]
honest negatives: sign is lattice-arithmetic, magnitudes are not (at scale ln q₀).

**Magnitude path (owner question: "can use q-bar norm to get magnitude?").**
On the lattice the bar-norm IS the sign datum (N = G(m,ℓ), integer — angle/parity
side). The derivable magnitude candidate is the OTHER channel of the same 𝔙:
under the exponential bridge form (bean qou-dtd3), |δf| ~ e^{−Re 𝔙/ℏ_q}, and on
the lattice Re 𝔙₄₁(u_{m,ℓ}) = Vol₄₁ − (3/8)(ln q₀)²·(2m+ℓ)ℓ — the CROSS form
(2m+ℓ)ℓ, bar-even/cosh channel — while sign comes from the norm form (bar-odd
parity channel). Magnitude = even channel, sign = odd parity: the two-channel
split, one integer form each. Next probe (derive-then-check, canonical windings
only, no tuning): does e^{−ΔRe 𝔙/ℏ_q} at the canonical w²/w³ windings reproduce
|S_p/S_m| ≈ 4.075? A miss is recorded as a miss.

## Method redirect (owner, 2026-08-01): EMBED into Bring's surface for the asymmetry — don't graft disc-5 onto disc-12

Owner steering: *"are you embedding into Bring's to get [the] asymmetry?"* — putting a
finger on the real seam in the [W] result. **Honest answer: no, not yet.** The [W]
work splits one geometry into two mismatched quadratic orders:

- **geodesic geometry** on the **cusp torus** → `ℤ[√3]` (disc-12, `ω=e^{iπ/3}`); this
  gives the winding `(m,ℓ)` and `Im 𝔙 = (√3/16)(ln q₀)²[(2m+ℓ)²−3ℓ²]`.
- **sign parity** grafted from Bring's **disc-5 golden order** (`ℤ[φ]`, norm −1,
  `N(φⁿ)=(−1)ⁿ`) via the braid power `wⁿ`.

The tell that this split is wrong: the **sign** came out clean (2/2) but the
**magnitude** MISSED — `|S_p/S_m|≈4.075` is not a disc-12 `G`-ratio, and ratio-matching
there is a fit trap (1833 chance pairs). The magnitude is being sought on the cusp
torus, where it does not live.

**The fix (this redirect).** disc-5 is **not external** to Bring's surface — it is its
**intrinsic automorphism structure** (`x5-z5-automorphism.lean`,
`x5-bring-weight-identification`, the genus-4 `sw-period-residue-sum.lean`). So embed the cusp-torus
winding geodesic **into Bring's genus-4 curve** and let the asymmetry — *both* sign and
the `4.075` magnitude — fall out of that ONE embedding:

- **sign** = the disc-5 (X5/Z5) parity, now intrinsic to the surface (already found);
- **magnitude** = a **Bring period / X5-weight ratio** of the `w²`(4₁, muon) vs
  `w³`(Borromean, proton) embeddings — a period/metric datum of the genus-4 curve, NOT
  a cusp-lattice `G`-value. This is the channel the cusp lattice structurally cannot
  reach.

**Attack (bean qou-mssy, derive-then-check, no tuning).** Compute the X5 Bring weights /
SW periods of the `w²` and `w³` embeddings and test whether their ratio gives `4.075`.
A miss is recorded as a miss (the anti-fit / dense-resource discipline from the [D4]
negative stands — no cusp-shape/period selection to match). Grounding: `brings-is-qou`,
`torus-knot-generators`, `bring-trefoil-cinquefoil-channel`, `x5-bring-weight-*`,
`sw-period-residue-sum`.

### Outcome (2026-08-01, bean qou-mssy): clean honest NEGATIVE

Probe [`qbeta_bring_embedding_magnitude_probe.py`](../../computations/qbeta/qbeta_bring_embedding_magnitude_probe.py)
(60 dps, exit 0, 4 assertions); audit
[`docs/audits/2026-08-01-bring-embedding-magnitude.md`](../audits/2026-08-01-bring-embedding-magnitude.md).
The Bring-embedding route does **not** resolve the magnitude — and the probe shows
why, in four facts (all evaluated at q₀ per the sharpened method):

- **[A1] `4.075` is an anchor-offset ratio, not a period.** `S(q)=c₃-target+Vol(4₁)`
  is one function; muon/proton are two evaluations at pins `1.28e-8` apart. `S` is
  hypersensitive (`dS/dq≈3.8e6`) and straddles a zero `q*=1.10997859303`: muon sits
  `+2.5e-9` above it, proton `−1.0e-8` below, and
  `|S_p/S_m|=4.075127 = |(q_p−q*)/(q_m−q*)|=4.075124` (verified to 6 digits). This is
  q-anchor arithmetic (where the pins fall vs the S-root), **not** a knot period.
- **[A2] X5/Z5 weight is a U(1) phase** (`x5-bring-weight-geometric-content.md`:
  "categorical, not a morphism of curves … U(1) phase tube"): `|ζ₅⁻³|/|ζ₅⁻²|=1`,
  unit modulus — structurally not a magnitude.
- **[A3] Only forced numeric period misses.** SW periods `a_D^{(n)}` are abstract ℂ
  fields (no numeric realisation; jet degree ≠ winding power). The one forced numeric
  period — hyperbolic volume `8G/(2·Cl₂(π/3))=3.610` — misses by **11.4 %**; every
  q₀-boost candidate (sinh/cosh at `ln q₀` or `ln φ`, `φⁿ`, Lucas/Fib) misses ≫0.1 %
  (closest `φ³` at 3.95 %, a non-forced coincidence, not adopted).
- **[A4] Structural wall.** A q₀-evaluated period is smooth ⇒ its w³/w² value is
  identical at both anchors to `~2e-9` (factor ≈ 1); it cannot be a factor-4
  hypersensitive ratio. The magnitude lives in the S near-zero crossing, not in any
  period — the **SP1 smoothness wall restated on Bring**.

**Missing to force a period:** a canonical genus-4 homology cycle per embedding
(the corpus gives only existence via the genus bound `g(K)≤4`,
`embeddability-closure.lean`) **and** a numeric realisation of `a_D^{(n)}` with jet
degree tied to the braid winding. Absent these, any period ratio needs a free
cycle/winding choice — the [D4] dense-fit resource, forbidden.

**Net.** Sign result (disc-5 parity, 2/2) stands. Magnitude stays **OPEN** and is
confirmed to belong to the hypersensitive near-degeneracy class (SP2, `qou-4kr1`),
which no smooth q₀-evaluated geometric quantity — Bring-intrinsic or otherwise —
can supply. No period adopted, no `SDeformedVolumeChannel` instance, no `c_k` wired.
