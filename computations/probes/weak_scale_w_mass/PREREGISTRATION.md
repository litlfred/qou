# Pre-registration — weak scale for the β-decay rate (bean qou-99qc)

Written 2026-11-20, before any number in this directory was computed.
Branch `claude/beta-rate-w-mass-gf-2026-11-20`.

## Question

The rate `𝔇_n(q) = G_F² |M(q)|² m_e⁵ f(Q_β) / (2π³)` needs a weak scale.
`|M|² = (q²−1)²` is derived (#8638, `QOU/QuarkState/ChargedCurrentW.lean`);
`G_F` is not. Can the corpus supply `m_W` (and so `G_F = √2 g²/(8 m_W²)`)
from its own canonical mass channel, without choosing anything?

## Corpus designations (read before computing; cited, not chosen)

- β-decay vertex knot: `T_{3,5}` = `(σ₁σ₂)⁵` — `predicted-spectra/beta-decay-skein.md`,
  `knot-particle-dictionary-table1-data.md` ("Weak force (β-decay)").
- W± boson: `T(2,4)` — **conjecture** `conj:electroweak-higgs-torus-link-triplet`
  (C1, C_sector, C_top open; W vs Z slot "a free label").
- Canonical mass channel: `m(K) = m_e·Vol(K)·ρ(K)/ℏ_q²`, which by
  `rem:pion-mass-hyperbolic-threshold` "reaches exactly the hyperbolic sector";
  `Vol = 0` means the mass is *not derivable from volume*, not that it is zero.

## Predictions fixed in advance

P1. Both designated weak objects are torus knots/links (Seifert-fibred),
    `Vol = 0`. So the canonical channel gives **no** `m_W/m_e` and no `m_W/m_p`.
    If this holds, step (1) of the task **stops here**: I will not pick a
    hyperbolic knot, a ρ, or a character ratio to stand in for the W.
P2. No corpus Hecke-character ratio links `m_W` to a `Vol = 0` anchor (`m_e`, `m_π`).
    The only W ratios on record are `m_Z/m_W` and `m_H/m_W` (W-relative).
P3. The coupling `g` is not fixed by the strand-tracked crossing: the h-term
    is dimensionless and its identification with `g`, `g²`, or `g²/8` is a
    normalisation the corpus does not state. I will report `h`, `hq`, `h/q`
    at `q₀` and select none.
P4. `𝔇_n/G_F²` is derived up to the Q_β cell; report both cells
    (label-C T⁺ round trip ≈ 0.5887 MeV; owner-scored cell 0.3254 MeV), select neither.
P5. The corpus `N_v = v/m_p` fixed point (`ElectroweakVevFixedPointClass`) is
    **conditional** with three underived slots (beans qou-rpt1, qou-myxi). I
    will evaluate it only as a labelled conditional comparison, never as the
    derived weak scale.

## Comparison values (read only in the final block)

m_W = 80.37 GeV; G_F = 1.1664e-5 GeV⁻²; 𝔇_n = ħ/878.4 s = 7.49e-25 MeV.

## Discipline

70 dps, proton q₀ (`qou_substrate.constants.Q_50_DIGIT_STR`), `_precision.fmt`.
Lean for algebraic identities: generic `Field`, sorry-free, lean-direct.
