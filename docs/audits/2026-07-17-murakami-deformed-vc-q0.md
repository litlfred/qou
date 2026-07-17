# Murakami deformed-VC route to an anchor-free q₀ — categorical N-selection analysis

**Date:** 2026-07-17 · **Axis:** L2 / μ–p substrate tension (Subgoal-2, absolute q₀) ·
**Tier:** assessment / scope-(a) numerical falsification. **No fit; nothing wired
to production; the μ–p tension is NOT resolved.**
**PR:** #3855 · **Producer:** `computations/murakami_deformed_vc_q0.py`
(witness `murakami-deformed-vc-q0.witness.json`, 60 dps) · **Lean:**
`QOU/Knot/FigureEightDeformedMeridianWinding.lean` (sorry-free, lean-direct exit 0
against the root-workspace Mathlib oleans; theorems `meridian_normSq`,
`meridian_normSq_ge`, `meridian_normSq_ge_floor`, `meridian_ne_zero`).

## 0. Why this exact task

The pin-sensitivity map (#3847,
[`2026-07-17-mu-p-pin-sensitivity-map.md`](2026-07-17-mu-p-pin-sensitivity-map.md))
PROVED (sorry-free Lean `PinRobustnessOfRatios`) that the 11.5 ppb μ–p pin
tension lives **entirely** in the absolute anchor `ℏ_q² = ((q₀−1)/q₀)²`: every
dimensionless ratio (`W_λ`, `m_p/m_μ`, `m_n/m_p`, the whole McKay keystone) is
`ℏ_q`-homogeneity-degree-0 and cancels it. The two live pins — muon
(`q₀ = 1.10997859555733471…`) and proton (`≈ 1.10997858275`) — are both **anchor
inversions**, so neither adjudicates. The map's §3 grading identified the
**Murakami deformed volume conjecture (C2)** as "the only route that could give
q₀ to < 11.5 ppb independent of both anchors … structurally richest", gated on a
**categorical selection of `N` (no fit)** — a formalize-first item. This note
executes that gate.

**Exact claim under test:** does a categorically-derived deformation datum on
the figure-eight 4₁ give `Vol(4₁; α) ⇒ ℏ_q ⇒ q₀` **absolutely**, independent of
the μ/p mass anchors?

## 1. Corpus map — what the VC/Kashaev/deformed-volume corpus already provides

The route is not virgin ground. The relevant prior work (corpus-grep on
`murakami|volume conjecture|deformed volume|kashaev|colored jones`):

| corpus object | what it gives | status |
|---|---|---|
| `Vol(4₁) = 2·Cl₂(π/3) ≈ 2.02988` | the **complete**-structure volume; the α=1/u=0 limit; the numerator of the muon anchor | exact constant, q-independent (S=0 in the pin map) |
| `m_μ/m_e = Vol(4₁)/ℏ_q²` (CAL-2 proxy) | the muon anchor relation | this **is** the inversion `q₀ = f(Vol(4₁), m_μ/m_e)` |
| `def:kashaev-volume-conjecture`, `VolumeConjecture41` (Lean class) | KVC axiomatised per-knot; Re-face `Vol(4₁)` cited (Andersen–Hansen/Ohtsuki) | conditional class; Re-face literature-proved, carried as `has_sorry`+`-- Ref:` |
| `FigureEightSelfDuality.lean` | **CS(4₁)=0** over generic `(R,σ)`: self-dual ⇒ bar-odd part vanishes | sorry-free (the Im-face of the complete structure) |
| `qbeta_c3_mq0_nk_scan.py` (#3704) + `2026-07-12-mq0-nk-scan-result.md` | the **DERIVED** substrate matching `u(N,k)=N·t−2πik`; branch-tracked `𝔙(u)` for 4₁ from Murakami–Yokota (math/0401084), validated 5/5 | ran the named N∈{3,6,60,120}×k∈{1,2} menu **against the odd-S value**: 0/8 |
| `2026-07-12-mq0-unified-boundary-selection.md` | the three candidate families (Gukov / Murakami / Hikami) are **one** parametrization by the meridian log-holonomy `u`; the N-selection is a discrete question | formalize-first scoping |
| `2026-07-12-mq0-literature-candidates.md` | C1–C4 candidate survey; C2 (Murakami) "structurally richest, needs categorical N (no fit)" | literature scoping |
| `s5-so3-keystone.md` | icosahedral orders 60=\|A₅\|, 120=\|2I\| enter as **McKay marks/dims** for the pin-**blind** `W_λ`; SU(2)/WRT(S³/2I) is scope-(b) excluded from reproducing `W_λ` (#2717/#2744) | does **not** feed a colored-Jones level N into a deformed volume |

**Key corpus fact #1 (pin map line 86):** `Vol(4₁)` alone does **not** determine
q₀; it is the fixed geometric numerator of the anchor inversion. To get q₀ from
the volume you must supply the second, q-dependent input — the mass ratio.

**Key corpus fact #2 (#3704):** the substrate matching that produces `u` from a
**real** q₀ is `u(N,k)=N·ln q₀ − 2πik`; the named integer menu overshoots and
lands off the 4₁ geometric component because the winding forces `|u| ≥ 2π`.

The distinction this note adds: #3704 aimed the machinery at the **odd-S value**
`S(μ)=+0.00968, S(p)=−0.03946` (the c₃/Q_β discriminant). #3847 showed the
actual μ–p discriminant is the **absolute anchor**, not any value/ratio. This
note re-aims the *same* deformed-VC dictionary at that absolute q₀.

## 2. The precise question, and the deformation freedom

For an **anchor-free** q₀ the deformed volume must supply a self-consistent
equation for q₀ that references no mass observable:

    ℏ_q² = Vol(4₁; α*(q₀)) / C        (schematically)

with **both** `α*(·)` (the substrate → deformation map) and `C` (a categorical
constant) derived, not fitted. The deformation parameters and which the
substrate fixes without a mass observable:

| datum | fixed by substrate without a mass? |
|---|---|
| complete structure `u=0` (α=1) | yes — but then `Vol` is constant, no q₀-handle (B1) |
| level `N` (color) | **the open question** — must be a categorical integer |
| winding `k` | matching forces `k∈ℤ₊`, principal `k=1` |
| meridian `u=N·t−2πik` | **derived** from matching `q_eval=e^{(u+2πi)/N}` to `q₀=e^t` (#3704) |
| the closing constant `C` | the corpus's only candidate is `m_μ/m_e` (a mass — the inversion) |

## 3. The three branches — each fails to give an anchor-free q₀ (scope-(a))

### B1 — Undeformed (u=0): the volume is q-independent ⇒ anchor inversion

`Vol(4₁)=2Cl₂(π/3)` carries no q₀ argument: `S(Vol)=d log Vol/d log q₀ = 0`
(exact). The muon relation `m_μ/m_e = Vol(4₁)/ℏ_q²` therefore has its **entire**
pin-sensitivity in `ℏ_q⁻²` (`S(ℏ_q²)=+2/(q₀−1)=18.185`, verified 40 digits in
the pin map). Determining q₀ from the volume needs a second q-dependent input;
the corpus's is `m_μ/m_e`. Using it **is** the anchor inversion. B1 gives no
anchor-free q₀.

### B2 — Real deformation: no CS handle, no geometric target

For real `u`, `Im 𝔙(u)=0` identically (the real-meridian/geometric locus; the
`FigureEightSelfDuality` CS=0 face). The real-volume deformation
`Re 𝔙(u)=Vol(4₁)−(√3/4)u²+O(u⁴)` (Neumann–Zagier, even in `u`) *does* carry a
q₀-handle if `u=u(q₀)`, but there is **no purely-geometric target** to close it:
setting `Vol(4₁;u)=Vol(4₁)` forces `u=0` (trivial); any other target is a mass.
The one purely-geometric quantization — `Im 𝔙=0` on the covering sheet, i.e. the
decay-sector `q*` — is genuinely independent but measurement-limited to 296 ppb
(needs σ(Q_β)≈0.024 eV), per the pin map §3. B2 gives no derivation-limited
anchor-free q₀.

### B3 — Winding deformation: |u|≥2π off-component, and the integer-N miss

The **derived** substrate matching is `u(N,k)=N·ln q₀ − 2πik`, so
`Im(u)=−2πk ⇒ |u| ≥ 2πk ≥ 2π` (the winding lower bound; Lean carrier below).
Two independent obstructions:

1. **Off the geometric component.** `|u|≥2π` is far outside Murakami's proven
   small-`|u|` neighborhood of 0 where `Vol(4₁;u)` tracks the geometric branch;
   #3704 found the named endpoints give negative/≈0 Bloch–Wigner volume
   (non-geometric sheet).
2. **The integer-N miss.** The naive quantization `q₀=exp(2π/N)` (the `N·t≈2π`
   condition, `N~2π/t*≈60.2` from the unified-boundary memo §3) requires
   `N_req = 2π/ln q₀ = **60.218** — a NON-INTEGER`. The nearest categorical
   integer N=60 gives `exp(2π/60)=1.11040`, missing q₀ by **379,095 ppb
   (~33,000× the 11.5 ppb tension)**; N∈{3,6,59,61,120} miss by 10⁶–5×10⁷ ppb.
   Hitting q₀ to 11.5 ppb requires tuning N to 60.218 — a **fit**, forbidden by
   the "no seventh fit-based ansatz" / anti-laundering discipline.

**Integer-N degeneracy (a second, independent obstruction to adjudication).**
The continuous `N_req` moves ~110 ppb between the two pins (it is a
reparametrisation of q₀, *not* pin-blind), but `⌊N_req⌉ = 60` for **both** pins.
A categorical selection yields one integer N, which cannot produce two distinct
`q₀=exp(2π/N)` — so the integer-N route is degenerate w.r.t. the μ–p split
regardless of the absolute miss.

## 4. Tiered verdict

1. **Structural (proved / exact).** `Vol(4₁)` is q-independent (B1); the
   substrate-matched meridian has `|u|≥2π` (B3 — Lean-carried sorry-free:
   `meridian_normSq_ge_floor : (2π)² ≤ normSq(u)` for `k≥1`, i.e. `|u|≥2π`,
   from `Im u = −2πk`); `CS(4₁)=0` for the complete structure
   (`FigureEightSelfDuality`, existing). These are the three exact facts that
   close the three branches.

2. **Scope-(a) negative.** **No anchor-free categorical N-selection currently
   exists.** The Murakami deformed-VC route, as the corpus can instantiate it
   today, either (B1) reduces to the anchor inversion, (B2) has no
   derivation-limited geometric closure, or (B3) needs a non-integer/fitted N and
   lands off the 4₁ geometric component. This confirms and sharpens the pin map's
   §3 grading ("only route that *could* … all OPEN/unowned") into an explicit
   obstruction.

3. **NOT scope-(b).** No proved invariant forbids a future categorical
   N-selection. In particular the meridian side leaves one honest surviving
   direction (flagged by #3704): a **small-`|u|` complex (phase-channel)**
   datum from a not-yet-derived substrate-functor level — the winding lattice is
   excluded, not the small-complex regime. A categorical level `N` for 4₁
   arising from the s5-so3 / GGM-3d-index structure (as an actual colored-Jones
   *level*, not a winding `k` and not a McKay mark) would be exactly the missing
   selection principle; it does not exist in the corpus today.

4. **Not resolved; nothing wired.** The μ–p tension is untouched. A q₀ obtained
   by inverting `Vol(4₁;α)` against the muon anchor is the existing inversion in
   disguise and would be a fit — not written, not wired.

## 5. What the next session should do

- **Do NOT** re-scan the winding lattice `u=N·t−2πik` — B3 + #3704 close it, and
  the integer-N route is degenerate w.r.t. the split.
- **The one live meridian-side direction** is the small-`|u|` complex
  phase-channel: a categorical level `N` for 4₁ that is *not* a winding and *not*
  a McKay mark. Watch #3805's GGM 3d-index work — if it surfaces such a level,
  re-run `murakami_deformed_vc_q0.py` against it (harness ready).
- **Highest-leverage remains** the decay-sector `q*` (measurement-limited, not
  derivation-limited) and the Subgoal-2 substrate derivations broadly (open for
  all, 2026-07-11).

## Cross-references

- Pin map: [`2026-07-17-mu-p-pin-sensitivity-map.md`](2026-07-17-mu-p-pin-sensitivity-map.md) §3 (C2 grading)
- Prior N-scan (odd-S value): [`2026-07-12-mq0-nk-scan-result.md`](../scope/2026-07-12-mq0-nk-scan-result.md), [`2026-07-12-mq0-unified-boundary-selection.md`](../scope/2026-07-12-mq0-unified-boundary-selection.md), [`2026-07-12-mq0-literature-candidates.md`](../scope/2026-07-12-mq0-literature-candidates.md)
- VC carriers: `def:kashaev-volume-conjecture`, `QOU/Knot/FigureEightVolume.lean`, `QOU/Knot/FigureEightSelfDuality.lean`
- Sibling anchor-free front: #3805 (GGM 3d-index Stokes integer)
- Convention: AGENTS.md §"q₀ anchor convention"; Subgoal-2 open-for-all [`2026-07-11-subgoal2-owner-reversal-open-for-all.md`](2026-07-11-subgoal2-owner-reversal-open-for-all.md)
