# Internal derivation of the q→0 3d-index DT count — context, formulae, attack options (2026-08-11)

Exploration memo for the one genuinely-open leg of the G3 / `A_ω` keystone:
an **internal** (QOU-categorical) combinatorial formula for the q→0 3d-index
Donaldson–Thomas count of a knot, reproducing `S⁺(0)₁₂ = 3` for `4₁` and the
companion `4` / surviving the `5₂` cross-knot test. This is *not* a wiring
gap; it is open in the DT-categorification literature itself. This memo
explains why, gives the objects and formulae, and enumerates attack routes —
including the one that unifies this with the Newton-polygon / q-difference-slope
thread. Nothing here is a derivation or a claim; it is a map.

## 0. What "DT" means, and what "open in the literature" means

**DT = Donaldson–Thomas.** DT invariants (Donaldson–Thomas 1998; generalized by
Joyce–Song and Kontsevich–Soibelman) are the algebraic-geometry / string-theory
count of **BPS states**: signed/weighted counts of stable objects in a
3-Calabi–Yau category (ideal sheaves on a CY 3-fold, or representations of a
quiver with potential) at a stability condition. The **motivic / refined** DT
invariant (Kontsevich–Soibelman) carries a `q`-grading; setting `q→1` (or taking
the numerical Euler characteristic) recovers the integer BPS index.

**Categorification of DT** = upgrading the DT *number* to a graded *vector space*
(a BPS cohomology / cohomological Hall algebra module) whose graded dimension or
Euler characteristic *is* the DT invariant. The machinery is the **cohomological
Hall algebra (CoHA)** of Kontsevich–Soibelman and **BPS cohomology**
(Davison, Davison–Meinhardt). For a quiver with potential this is understood in
cases; for the 3-CY category attached to a hyperbolic knot complement it is
**not** a closed combinatorial formula.

**Why the QOU ask is literature-open.** The knot 3d-index `I_M(m,e)(q)` (below)
is *defined from the ideal triangulation* — the Neumann–Zagier gluing data — not
from the knot's quantum-group / Hecke representation data. GGM's peacock theorem
(for `4₁`) says the resurgent Stokes constants of the state integral **equal**
the DT invariants of `T[M]`, and GPPV realise those as BPS Hilbert-space
dimensions — but *no formula* expresses that count as a function of the knot's
Iwahori–Hecke `H_n(q)` Wedderburn data / Markov trace / Bring embedding.
Producing one would be a **categorified AJ / a Hecke-algebraic formula for BPS
counts** — a new theorem in the DT/quantum-topology literature, not a QOU
bookkeeping step. Recomputing `I_M` "internally" via the colored Jones state
integral *is re-importing GGM*, not a categorical shortcut.

## 1. The objects and the exact target

**Tetrahedron index (Dimofte–Gaiotto–Gukov 2011; Garoufalidis arXiv:1208.1663).**

  I_Δ(m,e)(q) = Σ_{n=max(0,−e)}^∞ (−1)ⁿ · q^{ ½n(n+1) − (n + e/2)m } / ( (q;q)_n (q;q)_{n+e} ),
  (q;q)_n = Π_{j=1}^n (1 − qʲ).

**Figure-eight (2 tetrahedra), rotated total index** (GHHR Ex 4.1; certified in
corpus `figure_eight_3d_index.py`):

  Ind_{4₁}(q) = Σ_{k∈ℤ} I_Δ(k₁,k₂) I_Δ(k₂,k₁) = 1 − 8q − 9q² + 18q³ + 46q⁴ + …
  I_{4₁}(0,·)  = 1 − 2q − 3q² + 2q³ + 8q⁴ + …

**q→0 Stokes matrix and the target integer** (GGM eq 60; corpus
`StokesQZeroDTCount.lean`, sorry-free, decidable integer algebra):

  S⁺(0) = [[1, 3], [0, 1]]  ⇒  the physics integer is  A_ω(4₁) = S⁺(0)₁₂ = 3.

**GGM symmetry (eq 65), certified through q⁴⁰⁰:**

  S₁₂(q) + S₂₁(q) = 3 · S₁₁(q),   det S⁺(q) = 1,

so the *symmetry constant* `(S₁₂+S₂₁)/S₁₁ = 3` is q-independent — it equals its
own q→0 value (`StokesSymmetryConstant.lean`).

**The full DT spectrum is the pair {3,4}** (GGM eq 98); `5₂` (chiral) splits it
across chirality — `S⁺(0)` carries 4, `S⁻(0)` carries 3
(`FiveTwoDTSpectrumSplit.lean`). So the internal formula must reproduce **both**
`3` and `4`, and survive `5₂` — a single scalar for `3` is already excluded.

**Target (open):** a combinatorial `F` with

  F( Wedderburn mult. of H_n(q), Markov-trace data, Bring embedding of K )  =  DT-spectrum(K),

giving `{3,4}` for `4₁` and the correct chirality-split for `5₂`.

## 2. The three contexts

### 2a. Physics — 3d–3d correspondence

`T[M]` is the 3d `N=2` theory of the DGG 3d–3d correspondence; its `S²×S¹`
superconformal index **is** the 3d-index `I_M(m,e)(q)`. Its BPS Hilbert space
`H_BPS(T[M])` has graded dimensions = the DT/BPS degeneracies (GPPV `Ẑ`). The
Stokes data of the `S³_b` state integral (Andersen–Kashaev) resums these; GGM's
"peacock" says the Stokes constants = DT counts. The `A_ω` observable is the
odd-face monodromy datum of that irregular `q`-difference connection. Physically,
`A_ω = 3` is *"the figure-eight theory `T[4₁]` has 3 BPS states in the relevant
sector."*

### 2b. Algebra — Hecke, quantum A-polynomial, AJ

The QOU categorical data is the Iwahori–Hecke algebra `H_n(q)` (Wedderburn blocks
↔ partitions `λ⊢n`) and the Markov trace `tr_M` (= Jones/colored Jones). The
**AJ conjecture** (Garoufalidis) says the colored Jones `J_K(N)` satisfies a
`q`-difference (`q`-holonomic) recursion

  Â_K( L̂, M̂; q ) J_K = 0,   L̂ J(N) = J(N+1),  M̂ J(N) = q^{N/2} J(N),  L̂ M̂ = q M̂ L̂,

and the **quantum A-polynomial** `Â_K` reduces at `q=1` to the classical
A-polynomial `A_K(L,M)` (up to the abelian `(L−1)`). This is the bridge from
Hecke/quantum-group data to the character variety. The corpus's proved **C1
binding carrier**

  [m+2]_q · b_{m+2} = b_{m+1} + b_m        (Lean `qlift_normalized_kernel_exists`)

is a genuine `q`-difference operator; `conj:qdifference-kernel-prolongation-symbol`
posits it is the principal symbol of the SW jet-prolongation. Whether C1 is (a
factor of) the reduced `Â_{4₁}` is a QOU-internal identification question.

### 2c. Geometry — character variety, A-polynomial, boundary slopes

The `SL₂(ℂ)` character variety of `∂M` carries the A-polynomial curve
`A_K(L,M)=0`. For the figure-eight (geometric component):

  A_{4₁}(M,L) = −M⁴ + L(1 − M² − 2M⁴ − M⁶ + M⁸) − L²M⁴.

Its **Newton polygon** (in `(deg_M, deg_L)`) has edge slopes equal to the
**boundary slopes** of `4₁`: `{ 0, ±4 }` (Hatcher–Thurston; `4₁` is a
once-punctured-torus bundle). The 3d-index is *supported/charged* on sectors
governed by exactly this Newton polygon (normal-surface / spun-normal theory,
Garoufalidis–Hodgson–Rubinstein–Segerman). **The integer `4` is a boundary
slope**; the `3` is the number of boundary-parabolic `SL₂(ℂ)` flat connections
`{0, g, ḡ}` (equivalently the `(σ₃,σ₁)` DT entry). Both are geometric, but
neither is yet *derived from QOU data*.

## 3. Attack options

Ranked by how much they reuse already-landed corpus infrastructure and how
falsifiable they are. All are gated by the **cross-knot anti-numerology rule**
(a single-`4₁` coincidence is not a derivation unless it survives `5₂`, whose
block is `3×3`) — the rule that already killed the `disc(ℚ(√−3))=−3` route.

**Route A — Newton polygon of the QOU quantum A-polynomial (unifies with the
slope/q-difference thread; highest leverage).**
The chain is:
  QOU Hecke/Markov data → colored Jones → quantum A-polynomial `Â_K` (a
  `q`-difference operator, of which C1 is a candidate symbol) → its **Newton
  polygon boundary slopes** → 3d-index charged sectors → DT spectrum.
The corpus already proved **rung 1** of this ladder in a different guise:
`slope = q-Gevrey level` (`slopeKCoeff_order`, general `k`, sorry-free, bean
`qou-slvl`) connects a `q`-difference operator's Newton slope to its Gevrey
level. The *open* rung is **slope → DT count**: show the boundary slope `±4`
(hence the DT `4`) and the connection-count `3` fall out of the Newton polygon of
`Â_{4₁}` / the C1 operator, and that the `5₂` Newton polygon reproduces its
split. This is the route that makes the user's Newton-polyhedra intuition
load-bearing: *the DT integers are Newton-polygon data of the internal
`q`-difference recursion.* Falsifier: compute the C1/`Â` Newton polygon for `5₂`
and check the slopes match its `{3,4}` chirality split. **Status: the single most
promising unclaimed route; rung-1 done, rung-2 open.** *(Update 2026-09-07: run on
the corpus-derived `A_{5₂}` (#6985) — slopes `{−10,−4,0}`, connections `4`, same
verdict as the literature-recalled run, and the falsifier is answered in the
negative structurally: both Route-A inputs are mirror-invariant, so the
chirality split is not Newton-polygon data in any frame.
`RouteANewtonPolygonDT.absSlopeEq_mirror` / `lProfile_mirror`; audit
`2026-09-06-two-bridge-layering-from-farey-word.md` §3b.)*

**Route B — Character-variety Euler characteristic (Driver 14; scaffolded).**
`Driver14CharacterVarietyDTMenu.lean` already enumerates the menu: realise the DT
count as a (signed / motivic) Euler characteristic of the knot character variety
/ its moduli of flat connections. The `3 = #{0,g,ḡ}` boundary-parabolic
connections is the naive term; the refined statement needs the KS motivic weight
so the `4` also appears. Falsifier: the same Euler-characteristic rule must give
`5₂`'s `3×3` split. **Status: Lean menu scaffolded; the motivic-weight formula is
the open piece — this is a facet of the literature-open categorification.**

**Route C — CoHA / BPS-cohomology from the Hecke category (the deep route).**
Build the cohomological Hall algebra of the 3-CY category attached to `T[K]`
directly from the QOU Hecke/Soergel-bimodule categorification, and read the DT
count as `dim` of its BPS cohomology. This is the "honest categorification" and
would *close* the literature gap — but it is a research programme (Davison-style),
not a session. **Status: the real prize; out of session scope; the correct target
if the owner wants the literature gap itself closed.**

**Route D — Knots–quivers correspondence (already tested, wrong sector — recorded
so it is not retried).** Kucharski–Reineke–Stošić–Sułkowski assign a quiver to a
knot with one node per HOMFLY-homology generator; the count is `det(K)`. For `4₁`
that gives `det(4₁) = 5 ∉ {3,4}` — the **open**-HOMFLY BPS sector, *not* the
closed state-integral sector GGM's DT count lives in. **Status: refuted as the
bridge (audit `2026-08-02-aomega-conditional-gukov-stosic-bps-bridge.md`); do not
resurrect.**

**Route E — Neumann–Zagier data from the Bring embedding.** The 3d-index needs
only the NZ gluing matrix of the triangulation. If the QOU Bring embedding of `K`
*derives* the NZ data of a canonical triangulation (rather than importing it from
SnapPy), then `I_K` — and its DT count — becomes internal by construction. This
sidesteps categorification but demands a Bring→triangulation dictionary.
**Status: no such dictionary exists yet; a concrete but heavy geometry target.**

## 4. Recommendation and discipline

- **Route A** is where to push: it is the only route whose first rung is already
  a sorry-free corpus theorem, it is falsifiable on `5₂`, and it *unifies* the
  `A_ω` keystone with the Newton-polygon / q-difference-slope / Bessel–Askey
  thread the owner is independently pursuing. Concrete first probe: compute the
  Newton polygon of the reduced quantum A-polynomial `Â_{4₁}` (or the C1
  operator) and test whether its edge slopes `{0,±4}` and connection count `3`
  reproduce the DT spectrum `{3,4}`; then repeat on `5₂` as the anti-numerology
  gate.
- Everything above is a **map, not a result.** The internal derivation remains
  open; `A_ω=3` stays *certified-as-GGM-DT-count, conditionally adopted* (Rule-14,
  landed) until Route A/B/C actually produces `F`. Claiming otherwise violates the
  anti-laundering rule. "DT count imported and proven-for-`4₁`" ≠ "derived from the
  13 drivers."

## 5. Route A — EXECUTED (2026-08-11): partial, and it refutes its own slope leg

Probe `computations/probes/qbeta_g3_aomega_route_a_newton_polygon.py`
(audit-only, scope-(a); 4/5 assertions — the one FAIL is the intended
falsification). Airtight on `4₁`:

- The DT integers `{3,4}` **are** Newton-polygon data of `A_{4₁}`:
  `3 = full-A L-degree = #boundary-parabolic connections {0,g,ḡ}`;
  `4 = |max boundary slope|` (hull `(0,1),(4,0),(8,1),(4,2)`, edge slopes `±4`).
- **The QOU C1 binding carrier is NOT the quantum A-polynomial of `4₁`** — its
  Newton polygon (hull `(−1,2),(0,0),(1,2)`) has slopes `±½`, not `±4`. Route A
  must use the true colored-Jones recursion `Â_K`, not the binding carrier.

Cross-knot gate (5₂ boundary data literature-recalled — verify with SnapPy):

- **Slope reading R2 (DT integer = boundary slope) is REFUTED on 5₂** (max slope
  `10 ∉ {3,4}`) — the `4 = slope` match on `4₁` is a single-knot coincidence.
- **L-degree reading R1 (DT integer = #connections = A-poly L-degree) SURVIVES**
  (`4₁→3`, `5₂→4`, both `∈ {3,4}`).

**Verdict.** Route A does **not** close the gap; it *narrows* it: the internal
handle is the **connection count / A-polynomial L-degree — a motivic
Euler-characteristic datum — not the Newton-polygon slope**, read off `Â_K` not
the binding carrier. That surviving `R1` reading is precisely the
**decategorified shadow of Route C** (its `χ`; the categorification is the
BPS-cohomology / CoHA of Route C). Honest pivot (owner "if not then C"):
**Route C, entered through its Euler-characteristic shadow R1**; the companion
`4` still needs the motivic weight R1's bare count lacks. Tracked in beans
`qou-rt0a` / `qou-rtec` / `qou-52sn`.

## 6. Route C entry — the scalar avenue is provably exhausted (2026-08-11)

Route A's surviving reading R1 (`DT integer = #boundary-parabolic connections =
A-polynomial L-degree`) hits the `dtMax` vector `(4₁,5₂) ↦ (3,4)` exactly — and
it is a **new scalar not in the `Driver14CharacterVarietyDTMenu` menu** (which
tested blockCountH3, partitionEulerAbs, recursionOrder, crossingNumber,
determinant, idealTetrahedra, braidIndex, seifertGenus — none of which hits
(3,4)). So R1 is the **best scalar candidate found to date**.

But it does **not** close Route C, and now we know it *provably cannot*:
`Driver14CharacterVarietyDTMenu.no_scalar_matches_chirality_split_datum`
(sorry-free) proves the `5₂` DT datum is a genuine **2-element set `{3,4}`**
(chirality-split: `4` in `S⁺`, `3` in `S⁻`), while every scalar invariant is
single-valued per knot — so **no scalar** (R1 included) can equal the true
set-valued DT datum. R1 matches only the `dtMax` projection, not the datum.

**Consequence (the honest Route-C terminus for the scalar family).** The internal
`A_ω` count is inherently a **chirality-refined, set-valued moduli count** — a
Behrend-weighted DT moduli / `T[K]` BPS Hilbert space (the "driver-14" object),
categorical by nature. No scalar Wedderburn Euler characteristic, recursion
order, block count, or A-polynomial L-degree supplies it; that whole family is
now proved insufficient. Route C proper (BPS cohomology / CoHA producing a
chirality-graded, set-valued count) is therefore **required, not optional** — and
it is a research programme (out of session scope), tracked in `qou-rtec`. The
positive residue of this session: R1 is the sharpest scalar shadow (hits `dtMax`),
and the impossibility of any scalar is now a proved, cited fact rather than a
suspicion.
