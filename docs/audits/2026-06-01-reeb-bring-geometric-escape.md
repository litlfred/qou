# Reeb–Bring geometric escape test — does Reeb rotation distinguish p from n?

**Status:** COMPLETE — negative result for the Reeb-rotation channel
(branch `claude/reeb-bring-geometric-escape-2026-06-01`).
**Date:** 2026-06-01.
**Probe:** [`computations/reeb_rotation_pn_test.py`](../../computations/reeb_rotation_pn_test.py)
**Witness:** `computations/reeb-rotation-pn-test-reeb.witness.json`

## The hypothesis under test

Sessions on `main` (PRs #1604/#1605/#1606) proved a *per-partition*
impossibility theorem: any function `f(λ)` of abstract partition
(character-level) data is constant across Markov-equivalent knots and
therefore cannot produce `m_n − m_p = 1.293 MeV`. The signal localises to
"the braid word / strand count," not per-partition data.

**The escape:** the binding/mass energy may be GEOMETRIC — the rotation of
the Reeb bundle, a per-knot-**operator** quantity computed from the actual
braid word, NOT from the abstract character. If the proton-knot operator
and the neutron-knot operator act with different Reeb rotation, the geometry
distinguishes p from n even when their characters coincide.

**Decisive test (zero free parameters):** compute the q-Reeb rotation
(eigen-phase structure of the seminormal braid-word operator, per Wedderburn
block) for the proton braid and the neutron braid at substrate `q₀`, and ask:
does it DIFFER? Report raw numbers either way. No tuning to `m_n − m_p`.

## What the operators are (substrate-derived, zero tuning)

`q₀ = 1.1099785827513808`, `h = q₀ − q₀⁻¹ = 0.20906029879563937`.

Single nucleon ⇒ `A = 1` ⇒ 3-strand braid in `H₃(q)` (gens 0, 1), no
inter-nucleon crossing. The braid words come from
`mass_at_3A_proper.atom_braid_word_3A(Z, N)`, built from B₃ = (σ₀σ₁⁻¹)³ plus
typed quark crossings (proton = `uud`, neutron = `udd`). The proton and
neutron are **genuinely different elements of H₃(q)**:

| | g0 averaged (`−h/2`) crossings | g1 full (`−h`) crossings |
|---|---|---|
| proton (uud) | 1 | three `−h` + one `−h/2` |
| neutron (udd) | 2 | four `−h` |

Canonical-convention check (`atom_canonical_crossings`) agrees: proton g0 has
one `averaged`, neutron g0 has two `averaged`; proton g1 ends `…sigma_inv,
averaged`, neutron g1 ends `…sigma_inv, sigma_inv`.

## Preliminary result (full numbers in witness)

Per Wedderburn block λ ⊢ 3, eigenvalues of the braid-word operator
`Π (c·σ_g + d·I)`:

- **Eigenvalue PHASES (the Reeb rotation `arg(eigenvalue)`) are bit-identical
  for p and n** — every eigenvalue is real, phases ∈ {0, π} in both. The
  phase-sum difference is exactly 0 in all three blocks.
- **Eigenvalue MODULI differ** between p and n (e.g. block (3): 1.382 vs
  1.122; block (1,1,1): 0.739 vs 0.911). The distinguishing data is in the
  growth/writhe channel (`|eigenvalue|`), not the rotation/phase channel.

So under the standard q-Reeb reading (`θ_λ = arccos(χ_λ/dim_λ)`, phase =
`arg`), **the Reeb ROTATION does NOT distinguish p from n; the WRITHE/growth
amplitude does.** (Full block table, characters, and difference signs in the
witness.)

## Decisive numbers (per Wedderburn block λ ⊢ 3, from the witness)

Operator = `Π_k (c_k σ_{g_k} + d_k I)` on each seminormal block; `|λ|` =
eigenvalue moduli, `arg` = eigen-phase = **q-Reeb rotation**.

| λ | dim | proton χ | neutron χ | proton \|λ\| | neutron \|λ\| | proton arg | neutron arg |
|---|-----|----------|-----------|-----------|------------|-----------|------------|
| (3) | 1 | +1.382494463 | +1.122106822 | 1.382494 | 1.122107 | 0 | 0 |
| (2,1) | 2 | +1.807703064 | +1.700888606 | 0.452216, 2.259919 | 0.470626, 2.171515 | 0, π | 0, π |
| (1,1,1) | 1 | −0.739223571 | −0.910762215 | 0.739224 | 0.910762 | π | π |

Aggregate (witness `aggregate`):

| quantity | proton | neutron | Δ (p − n) | distinguishes p/n? |
|----------|--------|---------|-----------|--------------------|
| **Reeb rotation** (unit-modulus eigen-phase) | 0.000000000 | 0.000000000 | **0** | **NO** |
| sum\|arg\| (incl. real-sign π) | 6.283185307 | 6.283185307 | 0 | NO |
| writhe Σ log\|λ\| = log\|det\| | 0.043469155 | 0.043469155 | 0 | NO |
| eigenvalue **moduli** (per-block) | (see table) | (see table) | ≠ 0 in (3), (1,1,1) | **YES** |
| character χ (per-block) | (see table) | (see table) | ≠ 0 in every block | **YES** |

## Interpretation — the Reeb-rotation escape FAILS (clean negative result)

**The q-Reeb ROTATION does NOT distinguish proton from neutron.** Every
eigen-phase is bit-identical (Δ = 0 to machine precision) in every block.
The reason is structural, from
[`figure-eight-reeb-rotation.md`](../../content/quantum-observable-universe/braids-and-knots/figure-eight-reeb-rotation.md):
the q-Reeb rotation is the **phase `arg(λ)` of a UNIT-modulus eigenvalue**,
and unit-modulus eigenvalues arise only for **alternating** braids like the
figure-eight `(σ₁σ₂⁻¹)²` (`det = 1`, complex-conjugate pair `e^{±iθ}`). The
proton/neutron canonical braids are B₃ + typed-quark crossings — **not
alternating** — so their seminormal eigenvalues are **real** (`arg ∈ {0,
π}`). The π is the sign of a negative real eigenvalue, not a Reeb rotation.
There is no genuine rotation phase in these operators, hence nothing for the
Reeb-rotation channel to distinguish.

**Where the p/n signal actually lives.** The operators *are* genuinely
different (proton has 1 averaged g0-crossing, neutron has 2), and that
difference shows up in:
1. the per-block **eigenvalue moduli** (block (3): 1.382 vs 1.122; block
   (1,1,1): 0.739 vs 0.911), and
2. the per-block **characters** χ_λ (different in every block).

Both are **growth/amplitude** quantities, not rotation. So the geometry that
distinguishes p from n is the **writhe/growth amplitude**, exactly the
channel the scalar Markov trace already sees — and which the existing
`atom_mass_derived` model maps to mass via `tr_M`.

**Critical caveat on the "Markov-equivalent at H₃" framing.** The task
premise (proton/neutron bit-identical χ_λ at H₃) refers to a DIFFERENT
extraction — the averaged-crossing χ^{[2,1]} = 1.994185810381214 convention.
Under the **B₃ + typed-quark-crossing braid words** (`atom_braid_word_3A`,
the substrate operators), proton and neutron already differ at the SCALAR
character level (e.g. χ^{(3)} = 1.382 vs 1.122). So these single-nucleon
operators are NOT character-degenerate; the impossibility theorem's
degeneracy is a property of the averaged-crossing per-partition extraction,
not of these braid-word operators.

## Does the writhe/character channel give the right mass splitting? NO

The existing scalar model `atom_mass_derived` maps these same operators to
MeV: `m_p = tr_M(β_p)·E₀`, `m_n = tr_M(β_n)·E₀` with
`E₀ = m_p / tr_M(β_p)` (the proton-mass calibration). It yields

```
tr_M(proton)  = 0.43800985…   tr_M(neutron) = 0.32053947…
E₀            = 2142.126 MeV   (fitted: m_p / tr_M(proton))
derived m_n   = 686.636 MeV    (CODATA 939.565)
derived m_n − m_p = −251.64 MeV   (CODATA +1.293; wrong sign, ~195× off)
```

So even the writhe/character channel — the one that *does* differ p vs n —
gives the **wrong sign and ~200× wrong scale** for `m_n − m_p`. The p/n
operator difference exists but does not reproduce the splitting.

## Is the MeV scale derived or fitted? FITTED (RED)

There is **no derived MeV-per-(writhe) scale** on the substrate. The only
`tr_M → MeV` map is `E₀ = m_p / tr_M(proton)` — the proton-mass
**calibration**, a fitted constant. Mapping any geometric quantity
(Δχ, Δlog|λ|) to `1.293 MeV` would require choosing such a scale, i.e. a
**latent fit (RED)** unless a q-hyperbolic-volume / m_e derivation supplies
it independently. None exists for the splitting.

## How knot operators map to Bring-curve fibres

The Reeb bundle lives over the Bring curve `M_Bring` (the substrate's
Riemann surface). Per
[`figure-eight-reeb-rotation.md`](../../content/quantum-observable-universe/braids-and-knots/figure-eight-reeb-rotation.md)
the q-Reeb flow advances the **coral-sector angular coordinate** by `q·t`
per crossing, mixing the two lepton channels `V_{(2)} ↔ V_{(1,1)}` inside
`V_{(2,1)}`. A knot operator acts on the **same** seminormal blocks
(`V_{(3)}, V_{(2,1)}, V_{(1,1,1)}`) — proton and neutron do **not** act on
different fibres/sections; they act on the **same** Wedderburn blocks over
the **same** Bring fibre, differing only by the **coefficients** `(c, d)` of
the crossing word. The Reeb bundle is the SAME bundle for both; the operators
differ as endomorphisms of its fibre, not by living over different points.
This is precisely why the rotation (a property of the bundle/fibre geometry,
captured by unit-modulus eigen-phases) is degenerate: same bundle, same
phase structure (real eigenvalues), different amplitude.

## Verdict

- **Reeb ROTATION escape: FAILS.** The rotation phase is bit-identical p=n
  (Δ = 0). The proton/neutron braids are non-alternating ⇒ real eigenvalues
  ⇒ no rotation to distinguish them.
- The p/n distinction is real but lives in the **writhe/growth amplitude**
  (moduli + characters), the same channel the scalar trace sees — and that
  channel gives `m_n − m_p` with the **wrong sign and ~200× wrong scale**.
- Any MeV mapping of the differing channel would need a **fitted** constant
  (RED, latent fit); no derived scale exists.

Honest negative result: the geometric Reeb-rotation reading does not escape
the per-partition obstruction for the p/n mass splitting. The signal, where
it exists, is amplitude, not rotation, and is not reproduced at the right
scale or sign.

