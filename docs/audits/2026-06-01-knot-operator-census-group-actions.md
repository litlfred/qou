# Knot-operator census + group-action map: beyond Borromean for color tubes

**Date:** 2026-06-01
**Branch:** `claude/knot-operator-census-group-actions-2026-06-01` (PR #1677)
**Scope:** Author 2026-06-01 — *"keep exploring group actions. we have
different knot operators show up (not just Borromean for color tubes)."*
Catalogue every distinct knot/link operator the framework attaches to
color tubes / nucleons / channels / observables; map the group action
per operator; assess two live leads — (1) the **5-strand ↔ 3-strand
bridge** that the just-merged s5-so3 fiber audit and flavor-cusp audit
both name as their single missing object, and (2) whether a
**nonzero-writhe** operator (T(2,2m)) carries the U(1)_framing that the
writhe-0 Borromean cannot.
**Compute:**
[`knot_operator_census_group_actions.py`](../../computations/knot_operator_census_group_actions.py),
witness
[`knot-operator-census-group-actions.witness.json`](../../computations/knot-operator-census-group-actions.witness.json)
(audit-only, RAW @ 60 dps, 7 assertions pass). **No tuning to m_n−m_p,
B_AME, spin, hypercharge, or any h^k.**

---

## VERDICT (one line)

**The framework's knot-operator census is genuinely richer than
Borromean-only — it is a TWO-FAMILY landscape: a 2-strand `T(2,n)`
tower (leptons / mesons / fermion-boson statistics, indexed by
partitions of 2) and a 3-strand `H₃` family (Borromean baryon,
figure-eight, the six S₃ "knot operators", T(3,n) color/weak carriers,
indexed by partitions of 3), with the `S₅`/SO(3) fiber object living a
level up on 5 strands. The canonical strand-count-changing map IS Markov
(de)stabilization (`markov-moves-brane-tower.md`, the vertical α_V) — but
it does NOT bridge the 5↔3 gap, because the Borromean braid is Brunnian
and uses both B₃ generators, so no strand de-stabilizes cleanly (Markov
axiom 3 fails). The bridge stays OPEN and is the SAME missing object the
s5-so3 / flavor-cusp audits name. The U(1)_framing lead is real but
not derived: `T(2,2m)` has writhe `+2m ≠ 0` (computed raw), so a
torus-knot color-tube operator WOULD carry a nontrivial framing phase
`q^{w·c}` — but production uses the writhe-0 Borromean, so the framing
U(1) is trivial there, and `writhe → hypercharge` is undefined. This is
a CLEAN MAP of the landscape: two operator families, one
strand-count-changing functor (Markov), and a precise statement of why
it does not close the keystone gap.**

---

## 1. The census table

Strand count `n` = the braid group `Bₙ` the operator's word lives in
(= the meridional winding `m` for a torus knot `T(m,k)`). Wedderburn
block λ ⊢ n. Writhe = Σ crossing signs (RAW from the braid word). All
sourced to a content file.

| Operator | Word | Strands `Bₙ` / `Hₙ(q)` | Wedderburn block λ ⊢ n | Writhe | Observable / channel | Source |
|---|---|---|---|---|---|---|
| unknot `T(1,0)` | `𝟙` | 1 / `H₁` | `(1)` | 0 | vacuum / identity | `torus-knot-generators.md` |
| Hopf `T(2,2)` | `σ₁²` | 2 / `H₂` | `(2)`,`(1,1)` | **+2** | diquark; Hopf-bound pair | `trm-hopf-sigma1-sq-closed-form.md`, `hopf-diquark.md` |
| trefoil `T(2,3)` | `σ₁³` | 2 / `H₂` | `(2)`,`(1,1)` | +3 | **electron** `e⁻` (lepton gen 1) | `lepton-meson-torus-knot-dictionary.md`, `knot-operator-basis-table.md` (L.2) |
| cinquefoil `T(2,5)` | `σ₁⁵` | 2 / `H₂` | `(2)`,`(1,1)` | +5 | **muon** (gen 2) | `lepton-meson-torus-knot-dictionary.md` |
| septafoil `T(2,7)` | `σ₁⁷` | 2 / `H₂` | `(2)`,`(1,1)` | +7 | **tau** (gen 3, symmetry-broken) | `s5-equivariant-torus-knots.md` |
| `T(2,9)` | `σ₁⁹` | 2 / `H₂` | `(2)`,`(1,1)` | +9 | genus-4 saturation (no 4th gen) | `torus-knot-generators.md` |
| `T(3,4)` | `(σ₁σ₂)⁴` | 3 / `H₃` | λ ⊢ 3 | +8 | **Hopf² color binding** `H^{0,1}` | `torus-knot-generators.md` (quark sector) |
| `T(3,5)` | `(σ₁σ₂)⁵` | 3 / `H₃` | λ ⊢ 3 | +10 | **weak mediator**; `α_EM⁻¹ = q[9]_q[10]_q` | `torus-knot-generators.md`, `alpha-shift-torus-knot.md` |
| **Borromean** | `(σ₁⁻¹σ₂)³` | 3 / `H₃` | **`(2,1)` std** carries h⁴ | **0** | **nucleon / baryon** | `borromean-markov-trace-closed-form.md`, `borromean-baryon.md` |
| figure-eight `4₁` | `σ₁σ₂⁻¹σ₁⁻¹σ₂` | 3 / `H₃` | branching via `(3)`,`(2,1)`,`(1³)` | 0 | **Higgs / pion-half**; hyperbolic | `figure-eight-branching-rule.md`, `pion-half-figure-eight.md` |
| six S₃ "knot operators" | `𝟙,σ₁,σ₂,σ₁σ₂σ₁,σ₁σ₂,σ₂σ₁` | 3 / `B₃→S₃` | — (group elements, not knots) | varies | **color-tube Galois perms** `(r,g,b)` | `six-canonical-knot-operators.md` |
| NF basis operators | `γ,σ₀,σ₁,L₊,L₋,e⁻` | 3 / `H₃` channel basis | — | varies | photon/crossing/link/electron channels | `knot-operator-basis-table.md` |

**Two clarifications the census forced (both already in-corpus):**

1. The "**six canonical knot operators**" of
   [`six-canonical-knot-operators.md`](../../content/quantum-observable-universe/mass-theory/six-canonical-knot-operators.md)
   are NOT six distinct knots — they are the **six elements of S₃**
   (`B₃/⟨σᵢ²⟩`) realised as Galois permutations of the color-tube
   triple `(r,g,b)`. They are a single 3-strand structure, not a
   strand-count census.

2. The genuine multi-operator census is the **`T(m,n)` torus family**
   (`torus-knot-generators.md`): the genus bound `(m−1)(n−1)/2 ≤ 4`
   from `χ(Bring) = −6` selects exactly 6 nontrivial generators
   `{T(2,3), T(2,5), T(2,7), T(2,9), T(3,4), T(3,5)}` plus the unknot —
   `|𝒢| = 7 = 1 − χ`. **Meridional winding `m` IS the strand count.**
   The `m = 2` family (leptons) and the `m = 3` family (quark/color
   carriers) are the two distinct strand-count sectors.

---

## 2. Group-action-per-operator map

For each operator there is a tower of group actions
`Bₙ ↠ Hₙ(q) ↠ Sₙ`, plus a continuous symmetry from the knot type and a
gauge action from the framing/fiber. RAW structural reading:

| Operator family | Braid group | Hecke quotient | Symmetric quotient | Knot-type symmetry | Gauge/fiber |
|---|---|---|---|---|---|
| `T(2,n)` (m=2) | `B₂ = ℤ` (one generator `σ₁`) | `H₂(q)`, 1-dim per block | `S₂ = ℤ₂` | **cyclic `ℤ_n`** (torus-knot rotation) | SU(2)_q ribbon twist `θ_j = q^{j(j+1)}` (spin); U(1)_framing `q^{w·c}`, `w = n` |
| `T(3,n)` (m=3) | `B₃` (`σ₁,σ₂`, braid relation) | `H₃(q)` (blocks `(3),(2,1),(1³)`) | `S₃` | **cyclic `ℤ_n`** | same ribbon/framing; `w = 2n` |
| Borromean `(σ₁⁻¹σ₂)³` | `B₃` | `H₃(q)`, carries h⁴ in `(2,1)` | maps to `S₃` (writhe-0 ⇒ trivial sign) | **`S₃` holonomy** of `ρ:B₃→SU(2)` on Lagrange resolvents | writhe 0 ⇒ U(1)_framing TRIVIAL |
| figure-eight `4₁` | `B₃` | `H₃(q)` branching `(3),(2,1),(1³)` | `S₃` (3-cycle class) | **hyperbolic** (no cyclic torus sym; `ℤ/2` amphichiral) | writhe 0 |
| six S₃ ops | `B₃` | — | **`S₃` exhaustively** | — | color-tube `(r,g,b)` Galois |
| `S₅`/SO(3) fiber | — (5-strand index) | — | **`A₅ ⊂ S₅`** | `I ⊂ SO(3) ≅ SU(2)/ℤ₂` (icosahedral) | spin SU(2) `2I`; U(1) writhe |

**The B_n → H_n(q) → S_n correspondences (the requested systematic
thread), per strand count:**

- **n=2:** `B₂ = ℤ → H₂(q)` (one `σ₁`, two 1-dim blocks `(2),(1,1)`)
  `→ S₂ = ℤ₂`. The `T(2,n)` tower is `σ₁ⁿ`; the `ℤ₂` sign quotient is
  exactly the **fermion/boson statistics**: `gcd(2,n)` components, odd
  `n` = knot = fermion, even `n` = 2-component link = boson
  ([`fermion-boson-knot-link.md`](../../content/quantum-observable-universe/particle-interactions/fermion-boson-knot-link.md)).
- **n=3:** `B₃ → H₃(q)` (blocks `(3),(2,1),(1³)`; the `(2,1)` std irrep
  carries the Borromean h⁴=−3/4) `→ S₃`. SO(3) finite subgroup: the
  triangle-rotation `S₃ ⊂ SO(3)` (the s5-so3 audit showed this sees the
  std irrep at every ℓ≥1 — the "ℓ≤1 only" premise is FALSE).
- **n=5:** the fiber index set. `A₅ ⊂ S₅ ≅ I ⊂ SO(3)` (icosahedral),
  `ℓ=2 → dim-5 irrep H` (derived). SU(2) double cover → binary
  icosahedral `2I` (perfect, |2I|=120 ≠ S₅ structurally).

The **continuous knot-type symmetry** is the cleanest new entry: every
`T(2,n)` carries an intrinsic **cyclic `ℤ_n`** (rotation of the torus
knot), and `T(2,n)` is `S₅`-equivariantly embeddable iff `ℤ_n ↪ S₅`,
i.e. `n ∈ {3,5}` — exactly electron + muon
([`s5-equivariant-torus-knots.md`](../../content/quantum-observable-universe/observations/s5-equivariant-torus-knots.md)).
This is a torus-knot cyclic symmetry feeding the `S₅` fiber group — a
group-action link the census makes explicit.

---

## 3. The strand-count bridge (the LIVE gap) — VERDICT: OPEN

The s5-so3 fiber audit's open object is a functor from the **5-strand**
`S₅`/SO(3) level ℓ to a **3-strand** `H₃` Wedderburn coefficient. The
canonical strand-count-changing operations are Markov (de)stabilization
and cabling/satellite. Assessment, RAW:

### (a) Markov (de)stabilization — the canonical operation, but BLOCKED here

[`markov-moves-brane-tower.md`](../../content/quantum-observable-universe/braids-and-knots/markov-moves-brane-tower.md)
already identifies **stabilization** `β ↦ β·σₙ^{±1}` (`Bₙ ↪ B_{n+1}`)
as the **vertical α_V direction** of the brane tower — it IS the
framework's strand-count-changing functor, with trace scaling
`tr_M(β·σₙ^{±1}) = z^{±1} tr_M(β)`, `z = 1/(q^{1/2}+q^{-1/2})`. Computed
raw at q₀: `z(q₀) = 0.49932031756820496…`, `z⁻¹(q₀) =
2.00272…`. Two de-stabilizations H₅→H₃ would scale by
`z⁻² = 4.0109…` (raw, witness).

**But the bridge is BLOCKED by Markov axiom 3.** De-stabilization
`tr_M(β·σₙ^{±1}) = z^{±1} tr_M(β)` requires the removed strand be
**disjoint** from the closure. The Borromean braid `(σ₁⁻¹σ₂)³` uses
**both** generators of `B₃` non-trivially and is **Brunnian** (every
proper sublink is the unlink —
[`brunnian-property-of-borromean.md`](../../content/quantum-observable-universe/particle-interactions/brunnian-property-of-borromean.md)):
removing any single strand changes the link type (to the unlink), so no
strand de-stabilizes cleanly into the Borromean trace. **Plain Markov
de-stabilization is NOT the derived H₅(fiber)→H₃(Borromean) functor.**
The witness records `z⁻²` raw with the explicit caveat that the
disjointness hypothesis fails.

*Sanity that Markov works where disjointness holds:* `tr_M(σ₁²)` (Hopf)
is **n-independent** across H₃,…,H₆ precisely because the added strand
IS disjoint from `σ₁²` (`trm-hopf-sigma1-sq-closed-form.md`). Computed
raw: `tr_M(σ₁²)(q₀) = 1.1043893368…`, matching the Hecke closed form
`(q−q⁻¹)z + 1` to 10⁻⁵⁰ (witness assertion). So the obstruction is
specifically the Brunnian non-disjointness, not a flaw in the
stabilization machinery.

### (b) Cabling / satellite — wrong arithmetic for 5

A 2-cable of a 3-strand pattern produces a **6-strand** braid, not 5;
an `r`-cable multiplies strand count, never adding a single strand.
There is no cabling/satellite operation taking a 3-strand pattern to a
5-strand companion within the framework's generator set. (Cabling is
in-corpus for composite construction — `cabl` appears in 246 files —
but as pattern-on-companion, not as a 3→5 map.)

### (c) What WOULD close it (DERIVED requirement, not claimed)

The missing functor is one of:
- an explicit **branching/restriction functor** `Res: Rep(H₅) →
  Rep(H₃)` composed with the `S₅`/SO(3) fiber decoration, sending the
  ℓ=2 dim-5 irrep `H` to a specific coefficient of `tr_M((σ₁⁻¹σ₂)³)`'s
  `(2,1)` block — but no canonical such functor is supplied, and
  choosing the normalization to hit h⁴=−3/4 is exactly the fit the
  discipline review catches (s5-so3 audit §SO(3)); OR
- a **Markov-tower embedding that respects Brunnian structure** — i.e.
  a strand-count-changing map defined on the Brunnian sub-poset, which
  is NOT plain (de)stabilization and is currently undefined.

**The bridge is the SAME missing object** the s5-so3 fiber audit
(`partition_to_rotation` field of `BringFiberAction`) and the
flavor-cusp audit (the flavor→root map ρ) both name. The census
confirms there is **no non-Borromean operator in the existing generator
set** that supplies it — the operators that change strand count
(Markov stabilization) are blocked by Brunnianness, and the
torus-knot family changes `m` but each `T(m,n)` is a self-contained knot,
not a map between the fiber and the trace.

---

## 4. Which operators carry which gauge structure — U(1) on writhe

From the fiber audit: spin = ribbon twist (SU(2), framing), U(1) =
writhe phase `q^{w·c}` (R-I anomaly). The census makes the writhe
spectrum explicit (RAW from braid words):

| Operator | Writhe `w` | U(1)_framing `q^{w·c}` |
|---|---|---|
| Borromean `(σ₁⁻¹σ₂)³` | **0** | **trivial** (3 positive, 3 negative crossings) |
| figure-eight `4₁` | **0** | trivial (2 positive, 2 negative) |
| Hopf `σ₁²` | **+2** | **nontrivial** |
| `T(2,2m)` (m=1..5) | **+2m** | **nontrivial** (all positive crossings) |
| `T(2,3)` trefoil | +3 | nontrivial |
| `T(3,5)` weak | +10 | nontrivial |

The closed form **`writhe(T(2,2m)) = 2m`** is verified raw for m=1..5
(witness assertions `writhe_T(2,2m)_eq_2m`). So:

- **The production nucleon is writhe-0** (Borromean), so its
  U(1)_framing is trivial — consistent with the s5-so3 audit's "U(1)
  trivial on the baryon" finding. Hypercharge does NOT live on the
  baryon's framing.
- **But a nonzero-writhe color-tube operator (e.g. a `T(2,2m)` even
  torus link) WOULD carry a nontrivial framing phase.** The even
  `T(2,2m)` family is exactly the **boson** sector
  (`fermion-boson-knot-link.md`: `gcd(2,2m)=2` ⇒ 2-component link ⇒
  boson). So the place where the U(1)_framing is nontrivial is the
  **bosonic / linked** sector, NOT the fermionic Borromean baryon.

**This is a structurally suggestive lead but NOT a derived
hypercharge.** To make it rigorous one must DERIVE:
1. a map `writhe → Y` (continuous hypercharge from an integer framing
   datum — currently undefined; the writhe is quantized, Y is not
   obviously so);
2. why the bosonic `T(2,2m)` framing U(1) would act on the *baryon's*
   hypercharge when the baryon itself is writhe-0; this requires the
   inter-nucleon channel
   ([`conj:inter-nucleon-channel-color-tube`](../../content/quantum-observable-universe/brings-surface/inter-nucleon-channel-color-tube.md))
   to carry the linked (writhe-nonzero) operator — the s5-so3 audit
   already noted inter-nucleon arcs have writhe pp=+1, nn=−1, pn=0, a
   nonzero but undecorated framing.

No fit attempted. `Y` (experimental hypercharges) is a falsification
reference only; no writhe value is tuned to it.

---

## 5. The single most promising DERIVED lead for follow-up

**Lead: the inter-nucleon (linked) channel, where writhe is nonzero,
is the natural home for BOTH the strand-count bridge AND the U(1).**

The census surfaces a convergence: the Borromean baryon is writhe-0 and
Brunnian (blocks both Markov de-stabilization and the U(1)), but the
**inter-nucleon channel** is where linked, writhe-nonzero operators
live — pp arc writhe +1, nn arc −1
([`inter-nucleon-channel-color-tube.md`](../../content/quantum-observable-universe/brings-surface/inter-nucleon-channel-color-tube.md),
s5-so3 audit). A linked (non-Brunnian) inter-nucleon operator:
- **CAN** Markov-(de)stabilize (a linked arc has disjoint-removable
  strands in a way the Brunnian Borromean does not), giving a candidate
  strand-count-changing map that is NOT blocked by axiom 3; and
- **CARRIES** a nonzero writhe, hence a live U(1)_framing.

**What must be DERIVED (the precise follow-up task):** the braid word of
the inter-nucleon channel operator (the linked `H_{≥4}` operator joining
two `H₃` baryons), then check (i) whether its Markov de-stabilization
lands on the single-baryon `H₃` trace with a derived `z`-power, and
(ii) whether its writhe `q^{w·c}` reproduces a relative phase between p
and n. This is a DERIVATION task (write the operator, compute its trace
and writhe), not a fit — and it targets the exact channel the K₁/K₃
flavor gap lives in. It is the natural next deep-dive because it
attacks the strand-count bridge and the U(1) **simultaneously**, using a
linked operator that escapes both Borromean obstructions.

---

## What this audit does and does not claim

- **Does** catalogue, with source files, the two operator families
  (2-strand `T(2,n)` tower; 3-strand `H₃` family) + the 5-strand fiber
  object, and clarify that the "six canonical knot operators" are S₃
  group elements, not six knots.
- **Does** compute RAW @ 60 dps: writhe per canonical braid word,
  `writhe(T(2,2m)) = 2m`, `writhe(Borromean) = 0`, the Markov
  stabilization factor `z(q₀)`, `z⁻²(q₀)`, and the n-independent Hopf
  trace `tr_M(σ₁²)(q₀)` (7 assertions pass).
- **Does** establish the bridge is OPEN: Markov (de)stabilization is the
  canonical strand-count map but is BLOCKED on the Brunnian Borromean
  (axiom-3 disjointness fails); cabling gives 6 not 5; the missing
  functor is the same object the s5-so3 / flavor-cusp audits name.
- **Does** establish the U(1)_framing lead: nonzero-writhe operators
  (T(2,2m), the bosonic sector) carry a nontrivial framing phase, but
  the production Borromean baryon is writhe-0, and `writhe → Y` is
  undefined.
- **Does** identify the inter-nucleon linked channel as the single most
  promising DERIVED follow-up (escapes both Borromean obstructions;
  attacks bridge + U(1) at once).
- **Does NOT** propose, fit, or tune any fiber map, normalization,
  hypercharge, or h^k. m_n−m_p, B_AME, Y are falsification references
  only. Does NOT wire to production. Does NOT close or advance L2
  numerically. Does NOT discharge any Lean `sorry`.

---

## Cross-references

- The 5↔3 gap (same missing object):
  [`2026-06-01-s5-so3-su2-u1-fiber-action.md`](2026-06-01-s5-so3-su2-u1-fiber-action.md)
  (PR #1672),
  [`2026-06-01-flavor-dependent-cusp-shape.md`](2026-06-01-flavor-dependent-cusp-shape.md)
  (PR #1670).
- Torus-knot generators (the `T(m,n)` family + genus bound):
  [`torus-knot-generators.md`](../../content/quantum-observable-universe/brings-surface/torus-knot-generators.md),
  [`lepton-meson-torus-knot-dictionary.md`](../../content/quantum-observable-universe/particle-interactions/lepton-meson-torus-knot-dictionary.md),
  [`alpha-shift-torus-knot.md`](../../content/quantum-observable-universe/mass-theory/alpha-shift-torus-knot.md).
- Markov (de)stabilization = vertical α_V:
  [`markov-moves-brane-tower.md`](../../content/quantum-observable-universe/braids-and-knots/markov-moves-brane-tower.md),
  [`trm-hopf-sigma1-sq-closed-form.md`](../../content/quantum-observable-universe/braids-and-knots/trm-hopf-sigma1-sq-closed-form.md).
- Borromean baryon (writhe 0, Brunnian, `(2,1)` h⁴):
  [`borromean-markov-trace-closed-form.md`](../../content/quantum-observable-universe/mass-theory/borromean-markov-trace-closed-form.md),
  [`brunnian-property-of-borromean.md`](../../content/quantum-observable-universe/particle-interactions/brunnian-property-of-borromean.md).
- Fermion/boson = knot/link, `gcd(2,n)`:
  [`fermion-boson-knot-link.md`](../../content/quantum-observable-universe/particle-interactions/fermion-boson-knot-link.md).
- Figure-eight `4₁` (H₃, hyperbolic):
  [`figure-eight-branching-rule.md`](../../content/quantum-observable-universe/mass-theory/figure-eight-branching-rule.md).
- Six S₃ "knot operators" (color-tube Galois):
  [`six-canonical-knot-operators.md`](../../content/quantum-observable-universe/mass-theory/six-canonical-knot-operators.md).
- NF channel basis (γ,σ₀,σ₁,L±,e⁻ under T(2,n)):
  [`knot-operator-basis-table.md`](../../content/quantum-observable-universe/appendix-knot-operations/knot-operator-basis-table.md).
- The inter-nucleon channel (the follow-up target):
  [`inter-nucleon-channel-color-tube.md`](../../content/quantum-observable-universe/brings-surface/inter-nucleon-channel-color-tube.md).
- S₅-equivariant torus knots (`ℤ_n ↪ S₅`):
  [`s5-equivariant-torus-knots.md`](../../content/quantum-observable-universe/observations/s5-equivariant-torus-knots.md).
