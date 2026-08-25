# J/ψ = c̄c as a bound-state braid volume — sharpened negative (2026-08-02)

**Branch:** `claude/jpsi-boundstate-mass-2026-08-02`
**Probe:** [`computations/jpsi_boundstate_mass_probe.py`](../../computations/jpsi_boundstate_mass_probe.py)
**Witness:** [`computations/jpsi-boundstate-mass.witness.json`](../../computations/jpsi-boundstate-mass.witness.json)
**Serves:** owner bean `qou-jsx5` (lattice-QCD-from-QOU), PR #4600.

## The reframing (why J/ψ, not m_charm)

A confined quark mass `m_c` is a **scheme-dependent Lagrangian parameter**
extracted from color-singlet bound states — not a direct observable. The RIGHT
target is the **observable** J/ψ (3096.9 MeV, `J^PC = 1^--`) and its spin
partner η_c (2983.9 MeV, `0^-+`), both color singlets.

Per PR #4589 (`sm_carrier_vs_mass_knot_map.py`): every torus-knot *carrier* is
Vol = 0 (it sets the channel / quantum numbers, not the mass); the mass lives in
a **distinct hyperbolic bound-state knot**. The proton's mass-knot is the
Borromean link `(σ₁σ₂⁻¹)³` (Vol = 2·V_oct = 7.32772 → 938 MeV). J/ψ is a
**meson**: the bare c̄c closure is a 2-strand torus `T(2,k)` (Vol = 0), so any
hyperbolic structure must come from the gluon flux-tube binding.

## Method (derive-then-check, anti-fit)

Scale fixed **only** on the proton: `scale = 938.272 / Vol(Borromean) = 128.044`
MeV per `Vol·ρ` unit (ρ ≡ 1). Then:
- J/ψ (3096.9) needs `Vol·ρ = 24.186`
- η_c (2983.9) needs `Vol·ρ = 23.304`
- The J/ψ−η_c splitting is **113 MeV (3.6 %)** — spin hyperfine, i.e. the *same*
  c̄c system in two spin states. A correct construction gives **one base braid**
  for both, with the splitting as a small correction — **not** two different
  volumes.

## Findings

### 1. The proton's own family does NOT contain J/ψ

`(σ₁σ₂⁻¹)^k`:

| k | Vol | mass (MeV) |
|---|-----|-----------|
| 3 | 7.328 | 938 (proton) |
| 6 | 21.632 | 2770 |
| 7 | 26.054 | 3336 |

J/ψ (3097) falls **strictly between k=6 and k=7** — no integer winding hits it.
**J/ψ is not "the proton braid wound tighter."** A different-topology braid is
required, and choosing one to hit 3097 is a fit.

### 2. Volume spectrum is dense near the target (entropy)

Enumerating 196 simple `(base)^k` braids (3–5 strands, all sign patterns,
powers 2–8): **8 land in the 230-MeV band [2869, 3148] MeV (~4 % of the
space)**. With a 4-sig-fig target and a dense spectrum, a close hit carries
essentially no information (PR #1805 discipline).

### 3. J/ψ and η_c are best-fit by DIFFERENT braids (the discriminator)

| observable | best braid | mass | err |
|-----------|-----------|------|-----|
| J/ψ | 4-str `(σ₁σ₂⁻¹σ₃)⁴` | 3084.9 | −0.39 % |
| η_c | 5-str `(σ₁σ₂⁻¹σ₃σ₄⁻¹)³` | 2964.4 | −0.65 % |

The two are **different topologies** (4-strand vs 5-strand, different words) for
two states split by only 3.7 %. This is the classic **per-state fitting
signature** — the opposite of a single derived c̄c bound-state object. (A
genuinely derived object would give the same braid for both, with the ~113 MeV
hyperfine as a perturbation.)

> Note the tempting coincidence: `(σ₁σ₂⁻¹σ₃)⁴` (the "exp = strand-count, fully
> alternating" generalization of the proton's `(σ₁σ₂⁻¹)³`) hits J/ψ to 0.39 %,
> with a clean `CS = −1/12`. But `n = 4` strands is **not derivable** from a
> 2-quark c̄c system, so this is a dense-spectrum coincidence, not a derivation.

## Verdict — SHARPENED NEGATIVE (scope (a))

**Positive half.** The J/ψ mass scale is **IN-RANGE** for the hyperbolic
bound-state mechanism — hyperbolic braids with Vol ≈ 24 give ≈ 3097 MeV. This
**distinguishes J/ψ from the neutrino**, whose volume-density mass was
scope-(b) *excluded* by the minimum-volume theorem
(`neutrino_mass_volume_exclusion.py`). The meson mass scale is reachable; the
mechanism class is confirmed applicable.

**Negative half.** No **derived** c̄c braid exists. Evidence it is a fit, not a
derivation: (i) the proton family misses J/ψ at every integer winding; (ii) the
spectrum is dense near target; (iii) J/ψ/η_c best-fit by different braids.
Closest-hit reporting here would be numerology.

This is scope **(a)** (scope-limited negative), not scope (b): the volume-density
*ingredient* is **not** excluded (it is in-range) — only the specific braid is
undefined. Per AGENTS.md "refuted/ruled-out" discipline, we do NOT write "the
volume mechanism cannot give J/ψ."

## The precise open wall (beaned)

**"Thread c̄c through the gluon `T(2,9)` color tube" is topologically
under-defined.** There are many inequivalent ways to combine the meson carrier
with the gluon tube — satellite/companion, cable, connected sum (non-hyperbolic),
strand-insertion at each of several sites — each giving a different volume. No
canonical topological operation is specified by the framework, so no unique
volume is *derived*. Until "the flux-tube threading" is a **single, canonical,
parameter-free topological operation** (fixing strand count, insertion sites, and
winding from the c̄c + gluon quantum numbers *without reference to 3097*), J/ψ
cannot be predicted — only fitted.

`m_c` / J/ψ stays **OPEN**; the volume-density mechanism class is confirmed
in-range but the bound-state braid remains **underived**. Next honest step: a
derivation of the canonical meson flux-tube operation (e.g. from the Y-junction
→ single-tube reduction of the proton's 3-tube Borromean vertex), which would
fix the braid a priori — then check, once, against J/ψ and η_c jointly.
