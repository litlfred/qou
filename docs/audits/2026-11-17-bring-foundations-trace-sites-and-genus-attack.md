# Bring foundations: the trace sites, and an attack on the genus

PR #8365, issue #8364, bean `qou-qhcr` (open; never close while the derivation is open).

## 1. What the trace sites were, and how each was resolved

The 2026-09-15 rulings make `tr(id_A) = dim_q(A)` a q-dependent quantum dimension
and keep `chi_eu(M_0) = -6` as a separate, topological object
(`rem:three-euler-characteristics`). Five blocks used a trace identity.

| block | what it wrote | resolution | status |
|---|---|---|---|
| `brings-is-qou-verification` | `chi(A) = tr(id_A) = 2-2g = -6` | middle equality removed; nothing used it | resolved |
| `ns-kummer-specialisation` | `tr(kappa_0) = chi(A)` | the integer is `e(xi)[S]`, equal to `chi_eu(S)` by Poincare–Hopf **iff `xi` is the unit tangent bundle**; hypothesis now stated | resolved, conditional on (H_T) |
| `q-bsd-classical-limit` | `tr(kappa_0) = chi(A) = -6` | `kappa_0[M_0] = chi_eu(M_0)`, citing the above | resolved, conditional on (H_T) |
| `archimedean-yekutieli` | `chi(A) = -6` with lepton-generation reading | rename done; the `S_3 < S_5` three-pairs reading stays open | partly |
| `terminal-morphism-brings` | Step 1: `q + q^{-1} = -6` | not resolved: it forces `q = -3 ± 2√2`, and the Descartes condition no longer fixes `q` | **owner choice** |

### The hypothesis (H_T), and where the paper already has it

(H_T): *the circle bundle `xi` whose Euler class gives the Kummer obstructions is the
unit tangent bundle `UT(M_0)` of the base curve.*

- `thm:qu-to-qou` item 2 states it as a conditional ("when `xi` is the unit tangent bundle").
- `def:reeb-bundle` does **not** supply it: that bundle is the Hopf fibration over the
  fibre `S_p ≅ S^2`, Euler number `-1`.
- `lem:bring-cone-reeb-quaternionic-twist` **does** supply it for Bring: the link of the
  canonical cone over `Sigma_4` is `UT(Sigma_4)` with Euler number `-deg K = -6`, and its
  Reeb flow is the geodesic flow.

So for the Descartes universe the Kummer integer is derived, with no trace of `A`
anywhere. For a general QOU, (H_T) is an open hypothesis. **Gap G1:** derive that the
QOU contact form `Θ` restricts on the base to the canonical (Liouville) contact form of
the unit cotangent bundle. If it does, then (H_T) follows, the Reeb flow is the geodesic
flow, and the result holds at every genus, not only for Bring.

### `terminal-morphism-brings` — the options

Step 1 used `[2]_q = -6` to force equal substrate parameters on source and target.
Under the ruling, `[2]_q` is `dim_q(V) > 0` at real `q > 1`, so this step is false.
Options for the owner:

1. Make `q` part of the data of the category `C_{-6}` (objects at a fixed `q`). Step 1
   then holds by definition, and terminality becomes a statement per value of `q`.
2. Let a morphism carry a change of base ring `Z[q,q^{-1}] -> k`. Uniqueness would then
   have to be re-proved, because Step 4 relies on identical `q`.
3. Demote the block to a conjecture until (1) or (2) is chosen.

## 2. The conjecture: derive `g = 4` (`chi_eu(M_0) = -6`) from the axioms

### Where it stands (bean `qou-qhcr`, measured, sorry-free Lean on main)

- Riemann–Roch (Step 3) plus `g ≥ 1` (Step 4) plus observability (`chi ≠ 0`) give
  `g ≥ 2`, and nothing more.
- Transitivity of `Aut` on the Weierstrass points **alone narrows nothing**. This is a
  scope-(b) result: Accola–Maclachlan curves are transitive at every genus
  (Reyes-Carocca–Speziali, held in `library/arxiv-2211.08164v2`).
- (H1) transitivity, plus (H2) all Weierstrass points simple, plus the Hurwitz bound
  give `g ≤ 8`. This is derived and needs no classification
  (`BringsSurface/WeierstrassTransitivityNotForced.lean`).

### New this session: adding an order-5 automorphism (H3) gives `g ≤ 6` by arithmetic alone

`|W| = g^3 - g` divides `|Aut|` (H1+H2), `5` divides `|Aut|` (H3), and
`|Aut| ≤ 84(g-1)` (Hurwitz). So `lcm(g^3-g, 5) ≤ 84(g-1)`:

| g | g³−g | lcm with 5 | Hurwitz 84(g−1) | admissible orders | known max \|Aut\| at g | survives |
|---|---|---|---|---|---|---|
| 2 | 6 | 30 | 84 | 30, 60 | 48 | 30 only |
| 3 | 24 | 120 | 168 | 120 | 168 | 120 only |
| 4 | 60 | 60 | 252 | 60…240 | 120 | 60, 120 |
| 5 | 120 | 120 | 336 | 120, 240 | 192 | 120 only |
| 6 | 210 | 210 | 420 | 210, 420 | 150 | **none** |
| 7, 8 | — | — | — | none | — | **none** |

The Hurwitz arithmetic is exact and is computed in the table. The column of maximal
automorphism-group orders per genus is classical (Conder's tables), but **it is not yet
held in `library/`**, so the column is a citation still to be added and not yet a
derivation. With it, `g ≤ 5`. Separating `g = 4` from the survivors needs one fact per
genus:

- `g = 2`: no genus-2 automorphism group has order 30. This is classical: the genus-2
  groups have orders in {2,4,6,8,10,12,16,24,48}.
- `g = 3`: no genus-3 group has order 120.
- `g = 5`: does a genus-5 surface with `|Aut| = 120` act **freely and transitively** on
  120 simple Weierstrass points? Freely, because the stabiliser has order `120/120 = 1`.
  **This is the sharpest open arithmetic question, and Conder's genus-5 list settles it.**

### Attack strategy, ranked by cost

1. **Lean, cheap.** State and prove `H1 ∧ H2 ∧ H3 ∧ Hurwitz ⟹ g ≤ 6` over ℕ, as a
   companion to `WeierstrassTransitivityNotForced.lean`. It has no `sorry` and no
   classification input.
2. **Library, cheap.** Ingest Conder's genus 2–6 automorphism-group lists. Then turn
   `g ∈ {2,3,5}` into theorems taking those lists as hypotheses, with a `-- Ref:` to
   the source. The output would be `H1 ∧ H2 ∧ H3 ⟹ g = 4`, conditional on the lists,
   and Bring's curve then follows from the genus-4 classification.
3. **Paper link.** Add `conj:descartes-genus-from-axioms`, stating: *the five QOU axioms
   imply (H1), (H2) and (H3) for the base curve*. Re-state `ex:chi-minus-six-derivation`
   Step 5 as conditional on it, i.e. §3b-cond with a content-bearing class whose three
   fields are H1, H2 and H3. This turns the one unsourced integer, 6, into three named
   group-theoretic inputs.
4. **Research, hard: source (H3).** Every order-5 structure in the corpus is downstream
   of Bring (`ζ₅` pentad, the Bring–Jerrard quintic, the (2,4,5) triangle group, `2I`).
   Any candidate must come from the axioms and must not be selected because it gives 5
   (§NO FITTING).
5. **Research, hard: source (H2).** Simplicity is a *genericity* condition. In the
   held classification data it is anti-correlated with symmetry: Fermat's quartic fails
   it. So an observability-style axiom is the wrong shape for it. Look for a
   non-degeneracy statement instead. One candidate: the canonical series has an
   everywhere non-vanishing Wronskian of order `g`.
6. **G1** (§1): derive (H_T) from `Θ`. This is independent of 1–5, and it makes the
   Kummer results hold at every genus.

### The honest default

If none of 3–5 is closed, the paper should say plainly that `g = 4` is an **input**,
chosen as the maximally symmetric case satisfying (H1)–(H3). That choice is a selection,
and the §NO FITTING rule asks for it to be stated as one.

## 3. The "real route": genus from an irreducible symmetry on H¹ (2026-11-18)

### What the corpus already says, and where the genus enters

- `thm:descartes` makes Bring **terminal in `C_{-6}`**, the category of QOUs whose base
  has `χ_eu(M_0) = -6`. The genus is the **input** that defines the category, not an
  output. `rem:universality-general` expects a terminal object at every admissible `χ_eu`.
- `calibration-cohomology-alignment` states `H¹ = 2W`, rank 8, `dim W = 4`, opening with
  "Bring's curve has first cohomology…". `prop:prolonged-periods-fixed-depth` uses
  "`2g = 8` for the genus-4 Bring curve". Both read the dimension **off Bring**.
- `klein-bring-icosahedral-bridge` puts an `A_5` action on the **fibre** `P(V) ≅ CP¹`
  (`ζ₅` pentad plus an order-2 operation), with the EM involution in `S_5 \ A_5`.

So nothing in the corpus derives `rank H¹ = 8` from the axioms. The route below turns the
statement around and asks what forces it.

### The hypothesis (H_W)

*(H_W): the icosahedral group `A_5` acts faithfully on the base curve `M_0`, and
`H¹(M_0) ⊗ ℂ = 2W` with `W` an irreducible `A_5`-representation.*

### Result (exact, computed): (H_W) gives `g ∈ {4, 5}`; adding the `S_5` extension gives `g = 4`

Method: enumerate every generating vector of `A_5` and `S_5` with signature `(0; m_1, …, m_r)`
(Riemann–Hurwitz), compute the character of `H¹` by Lefschetz,
`χ_{H¹}(h) = 2 − #Fix(h)` for `h ≠ 1`, with `#Fix(h)` counted on cosets `G/⟨c_i⟩`, and
decompose. Exact integer arithmetic; script at the end of this section.

| group | signature | g | `χ_{H¹}` decomposition | `H¹ = 2W`, W irreducible? |
|---|---|---|---|---|
| `A_5` | (2,5,5) | **4** | `2·χ_4` | **yes** |
| `A_5` | (3,3,5) | 5 | `2·χ_5` | yes |
| `A_5` | (2,2,2,3) | 6 | `2·(χ_3 + χ_3')` | no |
| `A_5` | (3,5,5) | 9 | `2·(χ_4 + χ_5)` | no |
| `A_5` | (2,2,2,5) | 10 | reducible | no |
| `S_5` | (2,4,5) | **4** | `2·(sign ⊗ std_4)` | **yes** |
| `S_5` | (2,4,6) | 6 | `2·χ_6` | yes for `S_5`; restricts to `χ_3 + χ_3'` on `A_5` |
| `S_5` | (2,5,6) | 9 | reducible | no |

Completeness: an irreducible `A_5`-representation has dimension at most 5, so
`2g = 2 dim W ≤ 10`, i.e. `g ≤ 5`, and the search covers every genus that can occur. The
same bound for `S_5` is `g ≤ 6`.

Consequences:
1. (H_W) alone gives **`g ∈ {4, 5}`**.
2. `S_5` has **no** action on a genus-5 curve: the smallest signatures give `g = 4, 6, 9, 11, …`.
   So if the `A_5` action extends to `S_5` (the parity-odd EM coset that
   `klein-bring-icosahedral-bridge` already names), **`g = 4`**. A genus-4 curve with
   `S_5` action is unique, namely Bring.
3. This replaces the three inputs H1–H3 of §2 by two: the `A_5`/`S_5` symmetry of `M_0`, and
   the irreducibility of `H¹` as twice one representation. Order 5 (H3) is automatic.

### What is still open (gaps, named)

- **G2.** The corpus has `A_5`/`S_5` on the **fibre** `CP¹`, not on the base curve `M_0`.
  A derivation must lift that action to `M_0` from the axioms. Every order-5 structure in
  the corpus is currently downstream of Bring (§2, item 4), so this must not be chosen
  because it yields 4 (§NO FITTING).
- **G3.** Irreducibility of `H¹ = 2W` is an *input* here. A source could be a
  "no proper invariant subsystem of periods" statement. Note `prop:prolonged-periods-fixed-depth`
  uses the rank of the Gauss–Manin system, which would be the natural carrier.
- Not yet in Lean. The finite group computation is decidable and would be a sorry-free
  lemma over explicit permutation groups.

### Script

```python
# H^1 character of A5/S5 curves via Lefschetz; exact; sympy permutation groups.
import itertools
from fractions import Fraction as F
from sympy.combinatorics import Permutation, PermutationGroup
from sympy.combinatorics.named_groups import AlternatingGroup, SymmetricGroup
def run(G, name):
    els = list(G.elements); n = len(els)
    classes, seen = [], set()
    for e in els:
        if e in seen: continue
        c = {x*e*x**-1 for x in els}; seen |= c; classes.append(sorted(c, key=lambda p: p.array_form))
    reps = [c[0] for c in classes]
    ords = sorted({e.order() for e in els if e.order() > 1})
    for r in (3, 4):
        for sig in itertools.combinations_with_replacement(ords, r):
            g = 1 + F(n, 2)*(-2 + sum(1 - F(1, m) for m in sig))
            if g < 2 or g > 10 or g.denominator != 1: continue
            byord = {m: [e for e in els if e.order() == m] for m in sig}
            found = None
            for c in itertools.product(*[byord[m] for m in sig[:-1]]):
                p = Permutation(list(range(G.degree)))
                for x in c: p = p*x
                last = p**-1
                if last.order() != sig[-1]: continue
                if PermutationGroup(list(c)+[last]).order() == n: found = list(c)+[last]; break
            if not found: continue
            chi = []
            for h in reps:
                if h.is_Identity: chi.append(2*int(g)); continue
                fix = sum(sum(1 for x in els if x**-1*h*x in {c**j for j in range(c.order())})//c.order() for c in found)
                chi.append(2 - fix)
            print(name, sig, int(g), chi, [h.order() for h in reps])
run(AlternatingGroup(5), "A5"); run(SymmetricGroup(5), "S5")
```

### Lean (2026-11-18)

`QOU/BringsSurface/IrreducibleH1ForcesGenusFour.lean`, sorry-free, core Lean only.
`lean -DautoImplicit=false` exit 0; `#print axioms` shows `propext` and `Quot.sound`
only. It proves the arithmetic step: Riemann–Hurwitz (hypothesis `RH`) plus the
irreducible dimensions of `A_5` (hypothesis `hdim`) give `g ∈ {4,5}`
(`genus_four_or_five_of_A5_irreducible`); an `S_5` action excludes `g = 5`
(`s5_genus_ne_five`), so `g = 4` (`genus_eq_four_of_A5_irreducible_and_S5`).
`genus_four_attained` checks that the hypotheses hold for Bring's signatures, so the
conclusion is not vacuous. Riemann–Hurwitz and the `A_5` character table are not in
Mathlib and enter as hypotheses, not axioms. G2 and G3 are untouched.

### Lean, Riemann–Hurwitz infrastructure (2026-11-18, later)

`QOU/BringsSurface/RiemannHurwitzCellular.lean`, sorry-free, on Mathlib (lean-direct
against the restored `lake-cache/qou-v4-24-0` oleans, `-DautoImplicit=false`, exit 0;
`#print axioms`: `propext`, `Classical.choice`, `Quot.sound`).

- `riemann_hurwitz_cellular`: a finite group acting on a finite cell structure, freely
  on edges and faces, satisfies
  `χ(X) = |G|·χ(X/G) − Σ_{vertex orbits} (|G| − |G|/|Stab|)`. The proof is
  orbit–stabilizer (`MulAction.card_eq_sum_card_group_div_card_stabilizer`).
- `rh_of_cellular`: with `χ = 2 − 2g` this **proves** the predicate `RH` that the arithmetic
  file used to assume.
- `genus_eq_four_of_cellular`: the capstone. `A₅` and `S₅` acting through such cell
  structures, with cyclic point stabilisers and `g ∈ {1,3,4,5}` from (H_W), give `g = 4`.

Still taken as given (topology and representation theory Mathlib lacks): existence of a
`G`-equivariant cell structure on a compact Riemann surface with `χ = 2 − 2g`; point
stabilisers cyclic of element order; the irreducible dimensions of `A₅`. Non-vacuity of the
capstone at the level of cell structures is not shown; `genus_four_attained` shows it at the
level of `RH`. Gaps G2 and G3 unchanged.

`farkas-kra1992` added to `folio/references/` and `references.ts`. `references.bib` was
appended by hand in the generator's style, because `check-references-bib.ts` needs the
folio-assistant pipeline, which is not installed here. Run it once the pipeline is back.

### Riemann-surface layer, milestone M1 (2026-11-18)

`QOU/RiemannSurface/TangentJetRigidity.lean`, sorry-free on Mathlib (lean-direct exit 0;
axioms `propext`, `Classical.choice`, `Quot.sound`). It targets the hypothesis that point
stabilisers are cyclic.

- `jet_comp`, `jet_iterate`: order-`k` jets `X + aXᵏ` add under composition, so the `n`-fold
  iterate is `X + n·a·Xᵏ`.
- `jet_step`, `eq_X_of_finite_order`: over a characteristic-zero domain, a map tangent to the
  identity with finite compositional order is the identity (shown for polynomial maps).
- `isCyclic_of_injective_derivative`: an injective `g ↦ g'(0)` into a domain's units makes
  the stabiliser cyclic (Mathlib `isCyclic_of_subgroup_isDomain`).

Roadmap to discharge the remaining hypotheses of `genus_eq_four_of_cellular`:
- M1b: analytic germs (Taylor jets of compositions, then the identity theorem).
- M2: globalise on a connected Riemann surface.
- M3: an equivariant triangulation with `χ = 2 − 2g`. This is the largest, since Mathlib has
  no surface topology.
- M4: the irreducible dimensions of `A₅`.

M1b and M3 are written up as beans for another agent: `qou-m1bg` (analytic germs) and
`qou-m3tr` (equivariant triangulation), both children of `qou-qhcr`.

### Milestone M4, character bound (2026-11-18)

`QOU/BringsSurface/CharacterBound.lean`, sorry-free on Mathlib (lean-direct exit 0;
axioms `propext`, `Classical.choice`, `Quot.sound`). No group-specific input.

- `trace_inv_eq_star_trace`, `character_inv_eq_conj` (M4a): `χ(g⁻¹) = conj χ(g)`, by the
  unitary trick. `P = Σ_g ρ(g)ᴴρ(g)` is positive definite and `ρ(h)ᴴ P ρ(h) = P`.
- `finrank_sq_le_card` (M4b): an irreducible complex representation of a finite group has
  `(dim V)² ≤ |G|`. From `FDRep.char_orthonormal`, `Σ_g |χ(g)|² = |G|`, and the `g = 1` term is
  `(dim V)²`.
- `genus_four_or_six_of_irreducible`: with `|A₅| = 60` this gives `g ≤ 7`. Riemann–Hurwitz
  for `A₅` excludes 2, 3, 7, and for `S₅` excludes 5. So `g ∈ {4, 6}`.
  New arithmetic lemmas: `a5_genus_ne_seven`, `genus_four_or_six_of_le_seven`.
- `genus_eq_four_of_irreducible`: `g = 4`, given the one remaining fact `dim W ≠ 6`.

So the old hypothesis `hdim` (the list `1, 3, 3, 4, 5`) is narrowed to one fact: `A₅` has no
6-dimensional irreducible representation. This is M4c, and it is still open in Lean. It needs
either `Σ (dim Vᵢ)² = |G|` plus the count of irreducibles, or the explicit character table.
Neither is in Mathlib. Note that the arithmetic alone cannot exclude 6: `A₅` does act on
genus-6 curves, with `H¹ = 2(χ₃ + χ₃′)`, which is reducible.
