# Δ_λ collective term: the normal-surface class candidate (idea B3) — orbit structure + conjecture draft

**Date:** 2026-07-25 · **Bean:** qou-099h (B3) · **Axis:** per-isotope binding
`B(K) = m_e·Σ_λ y_λ χ^λ Δ_λ`, collective (non-additive) residual.

> **Tier banner (STRICT).** Structure-hunt tier · audit-only · **scope-(a)** ·
> **NO FIT**. **No number in this document is fitted to any observable.** The
> probe below is pure integer topology/combinatorics: no $q_0$, no binding
> energy, no comparison to the 1.22× mirror split, nothing wired to production.
> The deliverable is a **falsifiable conjecture shape** — an isotope →
> cusp-labeling → surface-class weighting proposal whose remaining freedom is
> counted exactly (6 DOF) and stated as the thing a derivation must eliminate,
> not as a knob to tune.

**Lineage:** idea B3 of
[`2026-07-18-uploaded-papers-binding-mass-gap-ideas.md`](2026-07-18-uploaded-papers-binding-mass-gap-ideas.md)
§B3; consumes the W9 surface enumeration of
[`2026-07-24-angle-structure-lp-sdp-dictionary.md`](2026-07-24-angle-structure-lp-sdp-dictionary.md)
§4; motivated by the pn-blindness prune and the #3943 collective residual of
[`2026-07-18-deltalambda-attack-vector-map.md`](2026-07-18-deltalambda-attack-vector-map.md)
§2.1 + §3; must not fall to the exchange-determinant no-go of
[`2026-07-18-deltalambda-exchange-determinant-family-nogo.md`](2026-07-18-deltalambda-exchange-determinant-family-nogo.md)
(§4 below verifies it does not).

**Probe:**
[`computations/probes/deltalambda_normal_surface_classes_probe.py`](../../computations/probes/deltalambda_normal_surface_classes_probe.py)
(exit 0, all 14 assertions passed) · **Witness:**
[`computations/probes/deltalambda-normal-surface-classes-probe.witness.json`](../../computations/probes/deltalambda-normal-surface-classes-probe.witness.json),
gated on exact per-index agreement with the committed W9 witness
(`borromean-angle-structure-lp-probe.witness.json`, upstream-hashed).

## 1. Why this object: the pn-capability question

The attack-map §2.1 prune is a proved invariant: the Slater-antisymmetrizer
trace and the `C(4,A)` occupation combinatorics depend on $A = Z + N$ only —
**pn-blind**. The #3943 forward test showed the additive per-pair magnitude
misses collectively (³H/³He diagnostic: 2.25× per-pair-predicted vs 1.22×
observed). So the missing collective term must live on an object that (i) is
genuinely many-body (not a per-pair bond) and (ii) **can** carry a
$(Z,N)$-distinguishing decoration. The vertex spun-normal surfaces of the
$\mathcal{B}_3$ triangulation are the first corpus object with both
properties: each class carries a per-cusp boundary grading
$[\partial S] \in H_1(\partial M;\mathbb{Z}) = \mathbb{Z}^6$ (three cusps =
three strands = three nucleon carriers), and each surface spans many
tetrahedra. This probe computes **exactly** which classes distinguish the
cusps, the full orbit/stabilizer structure under the cusp symmetry, and the
resulting degrees of freedom of any symmetry-respecting weighting.

## 2. Probe results (exact, from the witness)

### 2.1 Census (re-derived, gated on W9)

SnapPy `L6a4` (Borromean rings complement $\mathcal{B}_3$, 8 ideal
tetrahedra, 3 cusps); m004 convention re-pin $\sigma = (1,2,0)$,
$\varepsilon = -1$; GHHR 1604.02688 Prop A.3 pairing, $\alpha$-independent on
all classes; per-index quad vectors, slopes and $\chi$ **equal** to the
committed W9 witness for all 52 indices.

| quantity | value |
|---|---|
| vertex spun-normal surfaces | **52** |
| $\chi$ distribution | $\chi = -1$: 36 · $\chi = -2$: 16 |
| cusps-touched pattern | 1-cusp: $4+4+4$ · 2-cusp: $8+8+8$ · 3-cusp: $16$ |
| (support, $\chi$) cross-tab | 1-cusp, $\chi=-1$: 12 · 2-cusp, $\chi=-1$: 24 · 3-cusp, $\chi=-2$: 16 |
| distinct $(\text{slope}, \chi)$ classes | **46** (6 pure-longitude classes $(p_h,q_h) = (0,\pm 1)$ occur with multiplicity 2; all others multiplicity 1) |
| closed classes | none (all 52 have nonempty boundary) |

### 2.2 Symmetry bookkeeping (honesty note)

| quantity | value |
|---|---|
| isometry group order | 48; realizes the **full $S_3$** on cusps |
| sign kernel $K$ (trivial cusp permutation) | order 8 |
| combinatorial automorphisms of THIS triangulation | 16, realizing only $\{ \mathrm{id}, (0\,2)\}$ |
| peripheral-action convention | all four candidates (matrix / transpose / inverse / inverse-transpose) preserve the census slope multiset under all 48 isometries; `matrix` used — the convention ambiguity is immaterial for the class action |

Only a $\mathbb{Z}_2$ of the $S_3$ is realized combinatorially on this
triangulation, so all $S_3$ statements below are made at the **peripheral
level** — the induced action of the isometries on $(\text{slope}, \chi)$
classes via their cusp maps — not on quad vectors. Well-definedness of the
class action ($\chi$ + multiplicity preserved, all 48 isometries) and of the
induced $S_3$ action on $K$-orbits ($K$ normal; all isometries with the same
cusp permutation induce the same map) is machine-verified.

### 2.3 Orbit/stabilizer table (the core result)

The 46 classes fall into **11 $K$-orbits** ("unsigned peripheral classes"),
which fall into **3 $S_3$-orbits**. Exact table (orbit-stabilizer identity
$|\text{orbit}| \cdot |\text{stab}| = 6$ machine-verified for each row):

| $S_3$-orbit | rep slope $(p_1,q_1,p_2,q_2,p_3,q_3)$ | $\chi$ | support | classes per $K$-orbit | $S_3$-orbit size ($K$-orbits) | surfaces | stabilizer | character |
|---|---|---|---|---|---|---|---|---|
| 0 | $(0,0,\,0,0,\,0,-1)$ | $-1$ | 1 cusp | 2 | 3 | 12 | order **2**: $\langle(0\,1)\rangle$ (the transposition fixing the supporting cusp) | 1-cusp-distinguishing |
| 1 | $(0,0,\,0,-1,\,-2,0)$ | $-1$ | 2 cusps | 4 | 6 | 24 | order **1** (trivial) | fully asymmetric: distinguishes an **ordered** cusp pair |
| 2 | $(-2,-1,\,-2,-1,\,-2,-1)$ | $-2$ | 3 cusps | 8 | 2 | 16 | order **3**: $A_3$ (cyclic) | chirality pair: cyclically symmetric; the two $K$-orbits swap under every transposition |

Checks: $3 + 6 + 2 = 11$ $K$-orbits; $12 + 24 + 16 = 52$ surfaces. Orbit 1's
trivial stabilizer is notable: even when the transposition preserves the
*support* $\{1,2\}$, the slope data (longitude $(0,-1)$ on one cusp, meridian
$(-2,0)$ on the other) breaks it — the classes see the meridian/longitude
framing asymmetry, consistent with the graded-index finding
([`2026-07-24-borromean-index-bridge-invariant.md`](2026-07-24-borromean-index-bridge-invariant.md)
§2: the meridian ↔ longitude swap is **not** a symmetry of the index table).

**Two witness-reporting caveats (recorded honestly):**

1. The witness's summary dict `orbits_by_stabilizer_order` buckets only
   orders 6/2/1 (`{"6": 0, "2": 1, "1": 1}`) and so **omits the order-3
   orbit**; the per-row `orbit_table` (reproduced above) is the authoritative
   record. Actual stabilizer orders across the 3 orbits: **2 / 1 / 3**.
2. The probe's `kind` label falls through to `"fully-asymmetric"` for any
   stabilizer order other than 6 or 2, so orbit 2 is labeled
   `fully-asymmetric` in the witness although its stabilizer is the cyclic
   $A_3$ — it is *transposition*-asymmetric (chirality-sensitive) but
   *rotation*-symmetric. The table above uses the corrected character.

### 2.4 pn-capability and the equivariant-weighting DOF

- **No class is $S_3$-symmetric**: `surfaces_in_s3_symmetric_orbits` $= 0$;
  all **52/52** surfaces lie in orbits with stabilizer a proper subgroup of
  $S_3$. Operationally, "pn-capable" means: the class is moved by some cusp
  permutation, so a weighting supported on it can distinguish a labeling of
  the three cusps by nucleon species.
- **$H$-equivariant weighting DOF $= 6$.** Fix a pnn-type labeling: one
  distinguished (minority-species) cusp $d$, two majority cusps $\{a,b\}$;
  its stabilizer inside $S_3$ is $H = \langle (a\,b) \rangle \cong
  \mathbb{Z}_2$. A weighting $w$ on the 11 unsigned peripheral classes that
  respects the labeling symmetry (constant on $H$-orbits) has exactly
  **6 degrees of freedom** — the $H$-orbit count, machine-verified identical
  for all 3 choices of distinguished cusp (conjugate subgroups). The 6
  orbits, read off the table: (i) the 1-cusp class at $d$; (ii) the two
  1-cusp classes at $\{a,b\}$; (iii) the ordered pairs within the majority
  pair, $(a,b) \sim (b,a)$; (iv) the ordered pairs $(d,\cdot)$; (v) the
  ordered pairs $(\cdot,d)$; (vi) the 3-cusp chirality pair (its two
  $K$-orbits merge under the transposition). Totals: $2 + 3 + 1 = 6$.

### 2.5 Non-additivity data

- Tetrahedra-touched distribution (of 8): $\{2\!: 8,\ 3\!: 16,\ 4\!: 12,\
  6\!: 16\}$; every 3-cusp class spans **6 of 8** tetrahedra. A vertex
  surface is a global object of the triangulation, not a per-pair bond.
- **Pairwise-sum extremality holds**: no census quad-vector is the sum of two
  census quad-vectors (vertex/extreme-ray property, exhaustively checked) —
  no class decomposes as "a pair-object plus a pair-object".

## 3. Conjecture draft (formalize-first; markdown only, no content-block files)

The following is a **conjecture shape**, stated so that each ingredient is
independently falsifiable. It is *not* asserted, *not* wired, and creates no
content blocks; if it survives the gap list of §5 it would enter the corpus
as a `conjecture` block per the §3b discipline.

**Conjecture draft (B3-NS, collective term via labeled surface classes).**
*There exist*

1. *a* **cusp-labeling map** $\ell$: *for each light isotope $(Z,N)$ carried
   by the Borromean tower, an assignment of nucleon species to the cusps of
   the carrier — for $A = 3$, a map* $\ell(Z,N)\colon \{c_0, c_1, c_2\} \to
   \{\mathfrak{p}, \mathfrak{n}\}$ *(³H $\mapsto$ pnn, ³He $\mapsto$ ppn, up
   to cusp permutation), with stabilizer $H_\ell \le S_3$;*
2. *a* **weight function** $w$ *on unsigned peripheral classes* $[S]$ *of
   $\mathcal{B}_3$, jointly $S_3$-equivariant in class and labeling:*
   $w(g\cdot[S],\, g\cdot\ell) = w([S], \ell)$ *for all $g \in S_3$ — hence
   determined, per labeling type, by its values on the $H_\ell$-orbits (6
   values for a pnn/ppn labeling, per §2.4);*
3. *a* **per-class contribution** $I([S])$ *derived from canonical class
   data — the natural candidate being the GHHR normal-surface expansion of
   the 3D-index (Def 8.1 / Cor 8.2:* $I([S]) = (-q^{1/2})^{-\chi(S^*)} J(S^*)$*),
   composed with an admissible index-to-observable functional per the W1
   bridge invariants —*

*such that the collective (non-additive) residual of the light-isotope
binding is*

$$
B_{\mathrm{coll}}(Z,N) \;=\; m_e \sum_{[S]} w\bigl([S], \ell(Z,N)\bigr)\, I\bigl([S]\bigr),
$$

*summed over the unsigned peripheral classes of §2.3.*

### Testable consequences

**(a) $Z = N$ isotopes: no mirror split from this mechanism.** The global
$\mathfrak{p} \leftrightarrow \mathfrak{n}$ flip fixes (up to cusp
permutation) any species-balanced labeling; by the joint equivariance of
$w$, the term is then mirror-even, and moreover only the **3 $S_3$-orbit
sums** of $w$ can contribute (3 effective DOF in the balanced channel, not
6). Falsifiable: if a derived $w$ produced a mirror split for a $Z = N$
isotope through this term, the shape as stated is refuted.

**(b) The ³H/³He split can only come from the asymmetric classes — and the
freedom is NOT yet predictive.** The mirror flip maps the pnn labeling to
ppn $=$ a transposition-translate; the difference of the two evaluations is
supported exactly on the classes **not** fixed by the relevant transposition
— orbit 1's ordered-pair classes (the (iv)/(v) split of §2.4) and orbit 2's
chirality pair. Since the census has **zero** $S_3$-symmetric classes, in
principle *every* class family is available to the difference; which
combination survives is fixed by $w$. **Stated plainly: the $H$-equivariant
weighting has 6 DOF per labeling, against 4 light-isotope anchors (²H, ³H,
³He, ⁴He) — of which only the $A = 3$ pair is even directly 3-cusp-labelable
without a composition rule (2 usable constraints). 6 DOF $>$ 4 (and $\gg$ 2)
constraints: this shape is NOT predictive as it stands.** Any $w$ obtained by
solving against the anchors is a **fit**, must be labeled one, and may not be
wired (Δ_λ anti-fit rule). The only honest path is a principle that pins all
6 values (§5, gap 1).

**(b′) Consistency with the Coulomb-mirror split-off.** On the merged
`IsospinMirrorInvariance` premise
([`2026-07-18-deltalambda-exchange-determinant-family-nogo.md`](2026-07-18-deltalambda-exchange-determinant-family-nogo.md);
#3990), the *observed* ³H/³He split is already accounted parameter-free as
pure-EM Coulomb, so the **strong-sector** collective term should be
(approximately) mirror-even. That is itself a falsifiable constraint on any
derived $w$: its transposition-odd component on the asymmetric classes must
vanish (or be demonstrably sub-Coulomb) in the strong channel. A derivation
that pins the 6 values and lands a large strong-sector mirror split is
refuted by the mirror data *on that premise*; conversely, the pn-capable
classes remain the only carrier available if any strong-sector
$(Z,N)$-dependence beyond $A$ survives.

## 4. Prune-consistency (why this shape is not already excluded)

**(i) Not in the excluded exchange-determinant family.** The no-go closes
the hypothesis "ρ_A is a cumulant of the $K_A$ exchange determinant"
($b_A = -\ln\det(I + m\,G_A)$, obstructions 1–3). The B3-NS term is a
**class-weighted sum over normal-surface classes** — no Gram matrix on
$K_A$, no bond scalar $m$, no determinant, no logarithm; it is not touched
by the mirror fixed-point (obstruction 1), the $C(A,2)$ spectral cap
(obstruction 2), or the det-evenness no-op (obstruction 3). It is exactly
the kind of "structurally different object" the no-go's permanence caveat
leaves open.

**(ii) Genuinely non-additive.** Probe data (§2.5): every surface spans 2–6
of the 8 tetrahedra, all 16 3-cusp classes span 6; and no census class is
the quad-vector sum of two census classes (pairwise-sum extremality,
machine-verified). A weighting on these classes cannot be rewritten as an
additive per-pair bond object — the classes themselves are the collective
carriers the #3943 residual calls for.

**(iii) Not fighting the $y_\lambda$-suppression prune.** The prune excludes
magnitudes that grow with $\dim(\lambda)$ inside the Frobenius pairing. The
B3-NS weighting is indexed by peripheral surface classes, not by partitions;
it carries no $\dim(\lambda)$ growth and enters as the collective residual
alongside the (derived, permanent) per-pair pieces, orthogonal to the
Plancherel/Frobenius normalization. (It also does not lean on $d_q(\lambda)$,
so it does not inherit the hidden-$q$ DOF of the total-quantum-dimension
route, attack-map §2 item 3.)

## 5. Honest gap list — what a derivation must supply

1. **The weighting from a principle.** All 6 $H$-equivariant DOF must be
   pinned by canonical data — e.g. the GHHR per-class index contribution
   $I([S])$ with min-degree $d([S]) = -\chi(S^*) + \delta(S^*)$, or the
   Casson–Rivin dual certificate structure of W9 §5 (the angle-LP dual is a
   positive combination of exactly these classes) — with **zero** values
   chosen by proximity to any observable. Until then, any numerical
   comparison is laundering by construction.
2. **The isotope → cusp-labeling map as a stated conjecture.** Per the B3
   risk note (ideas doc §B3): without $\ell$ stated as its own conjecture
   block (with its $A > 3$ extension or composition rule — cf. idea B6's
   index convolution for gluing carriers), any match is laundering. The
   $A = 3$ case is canonical (3 cusps = 3 strands); ²H and ⁴He are **not**
   covered by this probe's object and need the composition story first.
3. **The index-q vs Hecke-q bridge (W1 invariants).** If $I([S])$ comes from
   the 3D-index, the bridge to an archimedean observable must satisfy the W1
   invariant list
   ([`2026-07-24-borromean-index-bridge-invariant.md`](2026-07-24-borromean-index-bridge-invariant.md)
   §1): cusp-symmetry equivariance (a) — automatic here by construction of
   $w$; **triangulation independence (b) — NOT automatic**: this probe reads
   the normal-surface coordinates of *one* triangulation, and only the
   index-level class sum inherits 2–3-move invariance, so a derivation must
   either consume $I_{\mathcal{B}_3}$ itself or prove its own invariance;
   the two-q's fibre-level identification (c); evaluation/limit rather than
   coefficient match (d), with coefficientwise $q_0$ evaluation excluded at
   scope-(a) (e); and the anti-fit discipline (f).
4. **The chirality-pair question.** Orbit 2's two $K$-orbits form a
   transposition-swapped pair (stabilizer $A_3$). Whether the derived sign
   front ($\mathrm{sgn}(w_0^{S_{\lambda'}})$ via the principal-grading jet
   order — already closed) interacts with this chirality structure is open;
   a weighting that distinguishes the pair is chirality-sensitive and must
   say why.
5. **Witness/probe cosmetics (follow-up, non-blocking).** (i) The
   `orbits_by_stabilizer_order` summary should carry a `"3"` bucket and the
   `kind` fallthrough should name the cyclic case (§2.3 caveats); the
   underlying `orbit_table` is correct. (ii) The probe docstring and the
   witness `auditOnly` field point to a `2026-07-24-…` filename for this
   audit doc; the doc landed as `2026-07-25-…` (this file). Fixing either is
   a one-line follow-up; note that editing the probe re-hashes it and stales
   the witness, so the pointer fix should ride a deliberate refresh.

## 6. Files

- Probe: [`computations/probes/deltalambda_normal_surface_classes_probe.py`](../../computations/probes/deltalambda_normal_surface_classes_probe.py)
  (exit 0; 14/14 assertions)
- Witness: [`computations/probes/deltalambda-normal-surface-classes-probe.witness.json`](../../computations/probes/deltalambda-normal-surface-classes-probe.witness.json)
  (upstream-gated on the W9 witness, sha256-pinned)
- Upstream census: [`computations/probes/borromean-angle-structure-lp-probe.witness.json`](../../computations/probes/borromean-angle-structure-lp-probe.witness.json)
  + [`2026-07-24-angle-structure-lp-sdp-dictionary.md`](2026-07-24-angle-structure-lp-sdp-dictionary.md)
- this audit doc

**Render-QA note.** The `folio-assistant` pipeline is not set up in this
sandbox, so the machine render check could not run; the full manual preflight
grep battery was run instead (balanced `$`/`$$`/braces, no `\operatorname`,
no list-marker lines inside display math, no `align`-family environments
outside `tex` fences) — all clean, but this doc was **not
machine-render-validated**.
