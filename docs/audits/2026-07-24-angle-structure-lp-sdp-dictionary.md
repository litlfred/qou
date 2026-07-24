# The angle-structure LP ↔ confinement-SDP dual dictionary (idea B2) — audit

**Date:** 2026-07-24 · **Bean:** qou-h8yc (W9) · **Scope:** audit-only, scope-(a),
comparison-only, **NO FIT**, nothing wired to production.
**Lineage:** idea B2 of
[`2026-07-18-uploaded-papers-binding-mass-gap-ideas.md`](2026-07-18-uploaded-papers-binding-mass-gap-ideas.md)
(§B2 + the Cluster-B facts appendix). Unclaimed before this tranche.

**Probe:**
[`computations/probes/borromean_angle_structure_lp_probe.py`](../../computations/probes/borromean_angle_structure_lp_probe.py)
(exit 0) · **Witness:**
[`computations/probes/borromean-angle-structure-lp-probe.witness.json`](../../computations/probes/borromean-angle-structure-lp-probe.witness.json)
(10 assertions, all passed; `verify_dual_present` → `ok: true`).

## 1. What was built

Both sides of the Casson–Rivin duality for the Borromean rings complement
$\mathcal{B}_3$ (SnapPy `L6a4`, 8 ideal tetrahedra, 3 cusps — the same NZ gluing
data as the sibling 3D-index probe `borromean_3d_index.py`), in exact rational
arithmetic:

1. the **generalized-angle-structure LP** of Garoufalidis
   [1208.1663 §2.2–2.3, eq (2.7)], solved max–min with **full LP-dual emission**
   per the AGENTS.md STRICT rule;
2. the **vertex spun-normal surface census** of the same triangulation
   (quad-coordinate vertex enumeration), with the GHHR
   [1604.02688 Prop A.3] Gauss–Bonnet pairing verified exactly;
3. the **comparison table** against the committed confinement-SDP witnesses for
   $\beta_{\mathrm{Bor}}$ — counts/ranks/structure only, no numeric fitting.

## 2. Conventions (pinned, then frozen)

Per 1208.1663 §2.2 (footnote 2: angles "traditionally $\pi$"; we work in
$\pi$-units) and eq (2.7):

$$
\bar A\alpha + \bar B\beta + \bar C\gamma = (2,\dots,2)^{T},
\qquad
\alpha + \beta + \gamma = (1,\dots,1)^{T},
$$

i.e. per-tetrahedron sums equal $1$ and per-edge sums equal $2$; *strict* means
all 24 angles are positive. The equality rows are taken verbatim from SnapPy's
`gluing_equations()` (8 edge rows + 6 peripheral rows in the per-tet
$(a\,|\,b\,|\,c)$ exponent convention).

The Prop A.3 pairing [1604.02688, eq (34)],

$$
\chi(S) = -\sum_{q}\frac{\alpha(q)\,x_q}{\pi} + \frac{\rho_\alpha(\partial S)}{2\pi},
$$

needs two implementation conventions relative to SnapPy's data: the *facing
permutation* $\sigma$ (which angle slot faces quad type $t$) and the boundary
orientation sign $\varepsilon$ in
$\rho_\alpha(\partial S) = \varepsilon\,\pi \sum_h (p_h\,\mu_h + q_h\,\lambda_h)\cdot\alpha$.
All $6\times 2$ candidates were scanned on m004; **exactly one** —
$\sigma = (1,2,0)$, $\varepsilon = -1$ — makes the pairing
$\alpha$-independent, and it reproduces GHHR Ex 10.23 / Ex A.10 exactly: the four
vertex spun-normal surfaces of m004 are once-punctured Klein bottles with
boundary $\pm 4\mu \pm \lambda$ and $\chi = -1$ (verified for all four, over 5
random generalized angle structures). The m004 angle LP also returns
$s^* = 1/3$, the regular-ideal-tetrahedron value — an independent sanity check.

**Solver note (found during this tranche).** sympy 1.14's
`sympy.solvers.simplex._simplex` **returns infeasible points without raising**
on small infeasible inequality systems (minimal repro embedded in the probe's
preflight: the system $\{c = 1,\ c = 0\}$, $c \ge 0$ returns $c = 1$). An early
draft of the decomposition test below was silently wrong because of this. The
probe therefore embeds a small exact two-phase simplex (Fraction arithmetic,
Bland's rule) and verifies **every** certificate exactly — primal feasibility,
dual feasibility, complementary slackness, strong duality — so no conclusion
rests on trusting a solver.

## 3. The LP and its duals (exact)

Max–min form: maximize $s$ subject to eq (2.7) and $x_i \ge s$, $x, s \ge 0$.

| quantity | value |
|---|---|
| GA equality rank | 13 (of 16 rows) |
| GA polytope dimension | 11 $= N + r$ (Neumann) ✓ |
| $s^*$ (max–min angle, $\pi$-units) | $1/4$ **exactly** → strict structure exists (GHRS Rmk 1.10 predicted existence; here certified) |
| primal $x^*$ | per-tet $(1/2, 1/4, 1/4)$ patterns — **equals the geometric structure exactly** (all shapes $z = i$: two regular ideal octahedra; quarter-integer angle vector verified GA-feasible exactly, and the LP optimizer coincides with it slot-by-slot) |
| primal binding set | 16 slots (the two $\pi/4$-angles of each tet) |
| dual $y^*$ (= `y_star`, angle-positivity shadow prices) | support $\{0,1,6,8,9,11,12,14\}$, each $1/8$; $\sum_i y^*_i = 1$ |
| equality shadow prices | `w_tet_star` $= (1/8,0,1/8,1/8,1/8,0,0,0)$, `w_edge_star` $= (0,0,-1/8,0,0,0,0,0)$ |
| dual objective | $\sum_t w_t + 2\sum_e w_e = 1/4 = s^*$; `duality_gap` $= 0$ exactly |
| certificate identity | $y^* = E^{T} w$ componentwise (verified exactly) |

**Dual-emission contract.** `solve_operator_selection_lp`
([`computations/lp_dual_solver.py`](../../computations/lp_dual_solver.py) →
`pyhecke.lp_dual_solver`) solves $\min t\cdot x$ subject to
$\mathbf{1}^{T}x = n_{\mathrm{target}}$, $Gx \ge 0$ with a square Gram $G$ — its
shape does not fit the max–min angle LP (no Gram/target pair), so the probe
**mirrors its output contract exactly** (`x_star`, `y0_star`, `y_star`,
`active_set`, `primal_obj`, `dual_obj`, `duality_gap`), with the mapping
documented in the witness (`dual_contract_note`); the committed witness passes
`verify_dual_present`.

## 4. The vertex normal-surface cone (tool: SnapPy 3.3.2 t3mlite/FXrays)

`Manifold("L6a4").normal_surfaces()` — quad-coordinate vertex enumeration of
spun-normal surfaces (recorded in the witness; regina is not available in this
sandbox, and was not needed at 8 tetrahedra).

| property | value |
|---|---|
| vertex classes | 52 |
| $\chi$ distribution (via Prop A.3, exact) | $\chi = -1$: 36 · $\chi = -2$: 16 |
| $\alpha$-independence | verified on all 52 over **6** angle structures (4 random generalized + the LP optimum + the geometric structure) — far above the required 3 pairs |
| integrality | $\chi \in \mathbb{Z}$ for all 52 |
| $\chi \ge 0$ classes | **none** — Farkas-consistent (GHHR Thm A.11) with the strict structure of §3 |
| closed classes ($[\partial S] = 0$) | none |
| cusps-touched grading | 1-cusp: $4+4+4$ · 2-cusp: $8+8+8$ · 3-cusp: $16$ — **$S_3$-symmetric** |

Symmetry facts: the isometry group has order 48 and realizes the **full $S_3$**
on cusps (`is_isometric_to(..., return_isometries=True)`); the combinatorial
automorphism group of *this* 8-tet triangulation (16 elements) realizes only the
$\mathbb{Z}_2$ swap $(0\,2)$. So $S_3$ statements about the vertex census are
made through the basis-free grading above, not through a combinatorial action.

## 5. Casson–Rivin duality made concrete: the dual certificate is a surface class

Rearranging Prop A.3, each surface gives a vector
$Q_S := P_S + \tfrac12\,\mathrm{per}_S$ with $Q_S\cdot\alpha = -\chi(S)$ for
*every* generalized angle structure; the tetrahedral classes $\tau_t$ (GHHR
Rmk A.9 / Ex A.10's "$1T_2$" term, formal $\chi = -1$, trivial in the Q-normal
class group) pair to the constant $1$. Exact decomposition tests for the LP dual
certificate $y^* = z$:

| test | result |
|---|---|
| (a) $z \in \mathrm{cone}(Q_S,\ \tau_t \ge 0)$ | **NO** ($\ell_1$ distance $1/3$, exact) |
| (b) $z \in \mathrm{cone}(Q_S \ge 0) + \mathrm{span}(\tau_t)$ | **YES**: $z = \tfrac14\,Q_{S_3} + \tfrac14\,Q_{S_7} + \tfrac14\,Q_{S_{35}} - \tfrac14(\tau_0 + \tau_1)$ |

The three support surfaces all have $\chi = -1$ and boundary slopes
$(0,0,\,2,0,\,0,-1)$, $(0,0,\,0,1,\,2,0)$, $(0,0,\,-2,0,\,0,1)$ (each touching
cusps 1 and 2); bookkeeping
$\tfrac14\cdot 3\cdot(-\chi) - \tfrac12 = \tfrac14 = s^*$ verified exactly.
The decomposition is **not unique** (a different exact-simplex pivot order
produced support $\{S_0, S_{16}, S_{25}\}$, one surface per cusp-pair — the
optimal face of the decomposition LP is positive-dimensional). What is
pivot-independent: *the dual optimum lies in the vertex-normal-surface cone
modulo trivial classes* — the Luo–Tillmann / Casson–Rivin duality realized as an
explicit exact certificate. This is the genuinely new structural handle on the
LP side: the "binding channels" of the angle LP **are** spun-normal surface
classes.

## 6. The dictionary comparison (counts / ranks / structure only)

Confinement-SDP side, read from committed witnesses (recorded per task):

- [`computations/borromean-axial-coupling.witness.json`](../../computations/borromean-axial-coupling.witness.json)
  — **the $\beta_{\mathrm{Bor}}$ witness**: operator-selection LP over the
  6-element $H_3(q)$ normal-form basis
  $\{1, \sigma_1, \sigma_2, \sigma_1\sigma_2, \sigma_2\sigma_1, \sigma_1\sigma_2\sigma_1\}$,
  `active_set` $= [0]$ (the identity word), `duality_gap` $\approx 1.4\times10^{-15}$;
- [`computations/nucleus-real-sdp-proton.witness.json`](../../computations/nucleus-real-sdp-proton.witness.json)
  — proton positive-norm subspace solve over the **3 Wedderburn blocks**
  $\lambda \vdash 3 \in \{(1^3), (2,1), (3)\}$, `active_set` $= [1,2]$
  (blocks $(2,1)$ and $(3)$).

| | angle-structure LP (this probe) | confinement SDP/LP ($\beta_{\mathrm{Bor}}$) |
|---|---|---|
| ambient index set | 24 quad/angle slots (8 tets × 3) | 6 NF-basis braids · 3 Wedderburn blocks |
| feasible-set dimension | 11 ($= N + r$) | ≤ 6 (NF LP) · 3 (block solve) |
| positivity constraints priced by the dual | 24 angle positivities $x_i \ge s$ | 6 / 3 Frobenius-positivity channels |
| dual support ("active channels") | 8 slots → **3 surface classes** mod trivial | 1 of 6 (identity word) · 2 of 3 (blocks $(2,1),(3)$) |
| extreme rays of the dual-side cone | 52 vertex surfaces ($\chi \in \{-1,-2\}$) | 6 / 3 |
| grading on the dual objects | $[\partial S] \in H_1(\partial M;\mathbb{Z}) = \mathbb{Z}^6$ | characters of $S_3$ ($\lambda \vdash 3$) |
| $S_3$ action | on **cusps** (geometric $S_3$; census grading $4/4/4$, $8/8/8$, $16$ symmetric) | on **strands** (blocks = $S_3$-irreps) |
| strong duality | gap $= 0$ exactly (rational) | gap $\sim 10^{-15}$ (f64) |

**Count verdict:** no coincidence. $3 \ne 2 \ne 1$ active objects; $52$ rays vs
$3$ (or $6$) channels; dim $11$ vs $3$ (or $\le 6$). The two $S_3$'s act on
different objects (cusps vs strands): the LP-side dual is graded by the abelian
$H_1(\partial M;\mathbb{Z}) = \mathbb{Z}^6$ with $S_3$ permuting cusp blocks,
the SDP-side dual by the *representation theory* of $S_3$. No bijection of
index sets is available at any level the counts can see.

## 7. The formal question a real dictionary must answer

A genuine dictionary would be a functor (or at least a cone map)

$$
\Phi:\ \bigl(\text{normal-surface cone } Q(\mathcal{T};\mathbb{R})_{\ge 0},\ \chi\text{-pairing}\bigr)
\longrightarrow
\bigl(\text{Frobenius cone of } H_3(q),\ \mathrm{tr}_M\text{-pairing}\bigr)
$$

sending the Casson–Rivin dual (surface classes pricing angle positivity) to the
Wedderburn dual (blocks pricing trace positivity), compatible with (i) the two
pairings, (ii) the two $S_3$ actions, and (iii) the gradings
$[\partial S] \in \mathbb{Z}^6 \mapsto \lambda \vdash 3$. The natural candidate
bridge is GHHR's own normal-surface expansion of the 3D-index (Def 8.1: the
index is a generating series over normal classes) matched against the
block expansion of the Markov trace — i.e. a dictionary would have to factor
through the (still underived) index $\to \rho(\mathcal{B}_3)$ bridge flagged in
the B1 probe.

**What the counts say about its possibility:** any such $\Phi$ is forced to be a
massively non-injective projection ($52$ rays $\to 3$ blocks) that collapses the
$\mathbb{Z}^6$ boundary grading onto three $S_3$-characters, and the observed
active sets do not correspond under any obvious collapse (3 cusp-pair surfaces
vs blocks $\{(2,1),(3)\}$ vs the identity NF word). Nothing here *forbids* a
functor at the generating-series level (per §Before-declaring-refuted: this is a
scope-(a) observation about these two specific duals, not a structural
exclusion), but nothing supports one beyond the shared LP-duality formalism.

## 8. Honest verdict

**Analogy-only** (not count-coincidence, not structural-map-candidate).

- The *shared* content is the duality formalism itself: both duals price
  positivity constraints and both active sets are small structured subsets.
  That is a property of LP/SDP duality, not of $\mathcal{B}_3$.
- The *new, real* structural result is on the LP side alone: the angle LP's dual
  optimum is exactly a positive combination of vertex spun-normal surfaces
  modulo trivial classes (§5) — Casson–Rivin duality as an explicit certified
  certificate, with the theorem-level Prop A.3 pairing machine-verified on all
  52 classes and pinned against GHHR's worked m004 example.
- The dictionary question is now sharply posed (§7) and its cheap falsification
  criterion (count mismatch) has fired: an isomorphism-level dictionary is dead;
  only a projection-through-the-index remains logically open, and it is blocked
  on the same underived index-to-$\rho$ bridge as idea B1.

## 9. Files

- [`computations/probes/borromean_angle_structure_lp_probe.py`](../../computations/probes/borromean_angle_structure_lp_probe.py) — the probe (exit 0; run log `/tmp/borromean_angle_structure_lp_probe.log`, wall ≈ 3 s)
- [`computations/probes/borromean-angle-structure-lp-probe.witness.json`](../../computations/probes/borromean-angle-structure-lp-probe.witness.json) — witness with the full LP-dual contract fields + the 52-surface table (10 assertions, all passed)
- this audit doc

**Render-QA note.** The `folio-assistant` pipeline is not set up in this
sandbox, so the machine render check could not run; the full manual preflight
grep battery was run instead (balanced `$`/`$$`/braces, no `\operatorname`, no
list-marker lines inside display math, no `align` environments outside `tex`
fences) — all clean, but this doc was **not machine-render-validated**.

Related: sibling B1 probe
[`computations/probes/borromean_3d_index.py`](../../computations/probes/borromean_3d_index.py)
(same triangulation, same anti-guessing sourcing);
[`docs/audits/2026-07-18-uploaded-papers-binding-mass-gap-ideas.md`](2026-07-18-uploaded-papers-binding-mass-gap-ideas.md) §B2.
